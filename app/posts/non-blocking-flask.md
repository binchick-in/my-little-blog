---
title: Non-Blocking Flask Routes
path: non-blocking-flask-routes
published: 2020-03-18
summary: Sometimes you need your Flask routes to do work with an undetermined duration. How do you prevent timeouts and "slow" response times? Python3 Futures!
---

One of the coolest things I've been learning about and tinkering with over the past few months is the [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) library in python3.

### The Problem

I've taken on a couple of project at work that involved Flask apps. One project from the ground up, one was a rewrite/refactor of an existing project. Both, however, required a simple web interface for end users to input data which triggered bulk tasks server-side. I quickly found that I needed a way to separate the bulk tasks from the Flask app, otherwise the thread would block while the bulk actions where being taken.


```python
@app.route("/task", methods=["POST"])
def task():
    task_params = request.form
    do_something(task_params)
    return jsonify({"status": "ok"})
```

In this example, `do_something()` is called and then blocks the main thread from continuing to the `return` line. This means your browser is spinning, waiting for this to complete. The worst part is, we don't know how long this will take. 30 seconds? 10 minutes? Longer? The user is waiting...

We need a way to kick off a task and respond to the client ASAP!

### Enter Python3 Concurrency

In short, the `concurrent.futures` library gives you the ability to fire off asynchronous tasks into threads or processes that will not block your main program from continuing.

So let's revisit the above route in our Flask app.

```python
# ...other imports
from concurrent.futures import ThreadPoolExecutor

@app.route("/task", methods=["POST"])
def task():
    executor = ThreadPoolExecutor()
    task_params = request.form
    executor.submit(do_something, task_params)
    return jsonify({"status": "ok"})
```

1. Create an [Executor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor) object using the [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) class
2. Grab your params
3. Using the created `executor`, call the `submit` method and pass in the function you want to run asynchronously and the arguments that function takes.
4. `return` some json to your user indicating that the job started. Profit!


### Things to Note
Keep in mind that this does not guarantee your task will complete successfully. Your function should be written in a way where any potential errors are handled accordingly. This technique is what many would call `fire and forget`. The task is issued, and from there we don't care what happens to it.

You should also write your function in a way to handle the results. Since this task was `fired and forgotten about` the main program moved on and the results will need to be handled inside your asynchronous thread.

It is also worth mentioning that calling `submit` returns a [Future](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future) object which has its own set of methods enabling you to get the status and even the results of the function. We, however, cannot utilize these methods in our example because we've opted to `fire and forget`.

There are several ways to leverage this library so read up on the docs and try out some different techniques. There are plenty of examples online and Stackoverflow articles to help you along.