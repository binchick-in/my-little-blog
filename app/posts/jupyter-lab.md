---
title: Jupyter Lab Is Awesome!
path: jupyter-lab
published: 2020-03-11
---

The best programming tool I have ever picked up is easily [JupyterLab](https://jupyter.org/). This amazing tool has allowed me to learn new Python concepts and libraries in a way a plain editor simply cannot. The successor to plain old Jupyter Notebooks, JupyterLab is a one stop shop for you to interact with all your individual Jupyter Notebooks.


## My Use Case

I'll add that I am not a data scientist, I'm not using JupyterLab for fancy visualization or data analysis. I use JupyterLab as scratch paper when I'm coding. When I wanna try out a python packge, I pip install into my environment, start a new notebook, import, and play.

## The Setup!

Alright, enough intro, let us begin!

#### Prerequisites
* Python3 (It's 2020, you better be using 3.5+ at this point)
* Virtualenv (used for sandboxing your environments)

#### Python Environments

I maintain a directory in which I place all my general purpose python environments. This directory is `~/pyenv` and it typically houses an environment per python version I have installed.

For example: `~/pyenv/env_37` would be a python3.7 environment.

#### Jupyter Notebooks

I'll say this once, keep all your notebooks in one directory. Since I use JupyterLab as a sort of scratch paper/development playground, there are a lot of files flying around. I keep them ***all*** in `~/jupyter_notebooks` this is also where I initialize the server on each run (more on that later)

#### Installation

Start by creating the directories mentioned above.

```
mkdir -p ~/pyenv/
mkdir -p ~/jupyter_notebooks
```

Create your virtual environment

> I'm using python3.7 in this guide!

```
virtualenv -p python3.7 ~/pyenv/env_37
```

The result will be a directory `~/pyenv/env_37`

Now, activate the environment

```
source ~/pyenv/env_37/bin/activate
```
Your terminal promprt will change and look like the following

>(env_37) bill@localhost:~/pyenv$

Now we need to install JupyterLab.

```
pip install jupyterlab
```

Once installed let's start the server.

**But first**, remember `~/jupyter_notebooks`? We need to be in that directory when we start the server. JupyterLab will use the directory it is started in as the base for all the files it reads and writes to. Using `~/jupyter_notebooks` as your base will ensure all your Jupyter Notebooks are in the same place and accessible for your every time you start the server.

Alright, start the server.
```
cd ~/jupyter_notebooks && jupyter lab
```
> Change into `~/jupyter_notebooks` and start the JupyterLab server

A browser window will pop open and you will be directed to `http://localhost:8888/lab`.

Thats really it for the base guide. You can begin using JupyterLab. Read the [JupyterLab Docs](https://jupyterlab.readthedocs.io/en/stable/) for more details on config options.

#### Bonus Details

Say you wanted to get your server up and running quickly. Well, I configure some aliases in my terminal to allow for fast server starts.

```
pylab='source /Users/bill/python_envs/env_37/bin/activate; cd /Users/bill/jupyter_notebooks/; jupyter lab --port 1337;'
```

1. Start the virtual environment
2. Change into the notebook directory
3. Start the JupyterLab server on port 1337

> Check `jupyter lab --help` for a TON more config options

I also have an alias to quickly activate the virtual environment. I use this mainly to quickly install/uninstall packages.

```
pyenv='source /Users/bill/python_envs/env_37/bin/activate;'
```

Thats all! Enjoy your shiny new playground!
