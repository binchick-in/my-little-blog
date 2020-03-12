---
title: Certbot Cheatsheet
path: certbot
published: 2020-03-11
summary: Some common tasks I tend to forget
---


#### Getting a wildcard SSL certificate
```
sudo certbot certonly \
	-d *.billben.net \
	-d billben.net \
	--agree-tos \
	--preferred-challenges=dns \
	--manual \
	--server https://acme-v02.api.letsencrypt.org/directory
```
You will be asked to set TXT records at `_acme-challenge.YOUR-DOMAIN.TLD`.
Once set, let them propagate and check for their existence with `dig`
```
dig -t TXT _acme-challenge.billben.net
```
When you reliably get a response back, its time to confirm with the `certbot` prompt that the records are there. If all
went well (`cerbot` found the records) you will be greeted with a success message and file paths to the cert files.
