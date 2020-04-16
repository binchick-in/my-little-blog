---
title: Scraping Slack Emojis
path: scraping-slack-emojis
published: 2020-04-15
summary: I wanted to export all the emojis in our Slack workspace, for science of course.
---

Say you needed to export all the emojis in your Slack workspace. How would you do that? There isn't (to my knowledge) a way to get them all. My company's workspace has 8k emojis and that increases everyday.

The best way I've found is to grab each CDN url and then run it through a `wget` loop. Slack's emojis CDN is seemingly public, if you have the URL, you have the emoji. Security risk? Possibly, if you store secrets in emojis for some reason.

When you're on the emoji page Slack, it does one of those continuous loading things. When you get to the bottom, more load. This means using the typical `getElementsByClassName()` method won't suffice when you're scrolling through hundreds of pages of emojis.

We need the `MutationObserver`. It will monitor for changes in a given element tree and apply the callback function to those changes. In our case, more emojis elements are added to the emoji list as we scroll down.

```javascript
var allEmojis = [];
var slackEmojiDomain = 'emoji.slack-edge.com';
new MutationObserver(() => {
    document.querySelectorAll('[class="p-customize_emoji_list__image"]').forEach((e) => {
        if (e.src.includes(slackEmojiDomain) & !allEmojis.includes(e.src)) {
            allEmojis.push(e.src);
            console.log(`New Emoji Found! We now have ${allEmojis.length}`);
        }
    })
}).observe(document, {childList:true, subtree:true});
```

Create an array for all the emojis, and start a new `MutationObserver` that grabs all the emoji elements, checks if the url matches the Slack emoji CDN, and if this url is already in our list. Then append that url to the list.

Once you get all the emojis urls, you can write them to the page and save as a `txt` file.

```javascript
document.write(allEmojis.join("<br>"))
```