---
title: Blocking Reddit Promoted Posts
path: blocking-reddit-promoted-posts
published: 2020-03-19
summary: We've all seen them. They're annoying and you cannot even opt-out of specific brands. So, we much block them.
---

I already block ads on Reddit, but didn't think much of the promoted posts for a long time. They've gotten out of hand at this point. I literally only get Triplebyte promoted posts on Reddit and I refuse to see another one.

So I looked into a way to inject the following script into all `reddit.com` pages.

```javascript
setInterval(() => {
    for (let item of document.getElementsByClassName("promotedlink")) {
        item.style.display = 'none';
    }
}, 1000);
```

Every second, grab all the elements with a class of `promotedlink` and just hide it... thats it.

We do this every second because Reddit utilizes infinite scroll, therefore more promoted posts will appear as we scroll down.

To inject this code into `reddit.com` pages, we need to install this extension:

[https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija)

The final product looks like this...

<img src="/static/cjs.png" width="85%" height="85%" />
