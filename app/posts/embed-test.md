---
title: Embedding JavaScript In Markdown
path: embedded-js-in-md
published: 2020-01-31
summary: Embedding JS into a markdown page is very straight forward. Even embedding pure JS can be very powerful
---

Playing around with HTML5 canvas tags a bit. Forget where I got this tutorial, but its meant to demonstrate basic animation in an HTML5 canvas. I thought it would be fun to play around with embeds in markdown documents to see how they turn out on a real life page.

Well, it turned out exactly as you'd expect. Injecting JS into single pages is simple with this technique.


<div style="algn: center;">
<br/>
<canvas style="border: 1px solid black; background-color: #d9d9d9;"></canvas>
<script>
var canvas = document.querySelector('canvas'),
    ctx = canvas.getContext('2d');
var colors = ['red', 'green', 'yellow',
              'purple', 'pink', 'blue',
             'cyan', 'magenta', 'orange'];
var resize = function () {
  canvas.width = 300;
  canvas.height = 250;
};
window.addEventListener('resize', resize);
window.addEventListener('load', function () {
  resize();

  var pos, vel;
  pos = {x: 10, y: 10};
  vel = {x: 1, y: 1};

  var loop = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pos.x += vel.x;
    pos.y += vel.y;
    if (pos.x < 5 || pos.x > canvas.width - 5) {
      var color =  colors[Math.floor(Math.random()*colors.length)];
      ctx.fillStyle = color
      vel.x *= -1;
    }
    if (pos.y < 5 || pos.y > canvas.height - 5) {
      var color =  colors[Math.floor(Math.random()*colors.length)];
      ctx.fillStyle = color
      vel.y *= -1;
    }
    ctx.fillRect(pos.x - 5, pos.y - 5, 10, 10);
  };

  setInterval(loop, 1000 / 60);
});
</script>
</div>


Start with a `cavas` tag

```
<canvas></canvas>
```

Then add a `script` tag and fill in your JS

```
<script>
var canvas = document.querySelector('canvas'),
    ctx = canvas.getContext('2d');
var colors = ['red', 'green', 'yellow',
              'purple', 'pink', 'blue',
             'cyan', 'magenta', 'orange'];
var resize = function () {
  canvas.width = 300;
  canvas.height = 250;
};
window.addEventListener('resize', resize);
window.addEventListener('load', function () {
  resize();

  var pos, vel;
  pos = {x: 10, y: 10};
  vel = {x: 1, y: 1};

  var loop = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pos.x += vel.x;
    pos.y += vel.y;
    if (pos.x < 5 || pos.x > canvas.width - 5) {
      var color =  colors[Math.floor(Math.random()*colors.length)];
      ctx.fillStyle = color
      vel.x *= -1;
    }
    if (pos.y < 5 || pos.y > canvas.height - 5) {
      var color =  colors[Math.floor(Math.random()*colors.length)];
      ctx.fillStyle = color
      vel.y *= -1;
    }
    ctx.fillRect(pos.x - 5, pos.y - 5, 10, 10);
  };

  setInterval(loop, 1000 / 60);
});
</script>

```