---
title: Nginx Config
path: nginx-config
published: 2020-01-25
summary: Utilizing the Nginx reverse proxy when running Docker
---

Nginx is my preferred web server and I run it in a reverse proxy configuration for most of my services. The majority of my services are running in Docker containers with Nginx sending traffic to the correct container based on host headers.

Below I'm listing some cookie cutter server blocks I use quite a bit


### The Catch All

If you aren't forcing secure connections on your page, you're wrong!
Any and all inbound requests on port 80 should redirect to a secure URL.
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    add_header HEY-YOU "WHY U NO USE SSL?";
    return 301 https://$host$request_uri;
}
```
---
### Basic Reverse Proxy

As mentioned above, most of my services are running in Docker with a single exposed port listening on `localhost`. This means I need to route incoming traffic to that container. Luckily, Nginx is awesome and makes this config simple.

```
server {
    listen 443 ssl;
    server_name www.billben.net billben.net;

    ssl_certificate /etc/letsencrypt/live/billben.net/cert.pem;
    ssl_certificate_key /etc/letsencrypt/live/billben.net/privkey.pem;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:22000;
    }
}
```


`server_name` decides which requests are handled by this `server` block based on `host` header

`location` is where the actual `reverse proxy` part comes in. this is telling Nginx to pass the request off to another server (in my case a Docker container) listening on port `22000`

The directives prefixed with `ssl_` are the SSL cert config paths.
