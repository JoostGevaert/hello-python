# Hello Python
An introduction to python basics and best practice.

The project sturcture is based on the Real Python tutorial found on:
https://realpython.com/python-application-layouts/

helloworld/  
│  
├── bin/  
│  
├── docs/  
│   ├── hello.md  
│   └── world.md  
│  
├── helloworld/  
│   ├── \_\_init\_\_.py  
│   ├── runner.py  
│   ├── hello/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── hello.py  
│   │   └── helpers.py  
│   │  
│   └── world/  
│       ├── \_\_init\_\_.py  
│       ├── helpers.py  
│       └── world.py  
│  
├── data/  
│   ├── input.csv  
│   └── output.xlsx  
│  
├── tests/  
│   ├── hello  
│   │   ├── helpers_tests.py  
│   │   └── hello_tests.py  
│   │  
│   └── world/  
│       ├── helpers_tests.py  
│       └── world_tests.py  
│  
├── .gitignore  
├── LICENSE  
├── README.md  
├── requirements.txt  
└── setup.py    (see: setuptools)  


## Setting up Windows for Development from new installation
0. Debloat Windows
1. Get WSL2 and the WindowsTerminal (Git Bash & Linux e.g. Ubuntu) up and running
    * https://towardsdatascience.com/data-science-on-windows-subsystem-for-linux-2-what-why-and-how-77545c9e5cdf
	* https://www.bradleysawler.com/engineering/python-conda-wsl-2-ubuntu-setup-on-windows-10/
	* ¡¡¡IMPORTANT!!! line ending (CRLF or LF) settings for git  
	  set `git config --global core.autocrlf false` in Window's Git Bash  
	  set `git config --global core.autocrlf false` in WSL2's Linux  
          Use a .gitattributes  
          In case something went wrong, use the find_line_endings.sh and fix_git_crlf-lf.sh to fix it.
2. Get miniconda for Windows and WSL2's Linux.  
    * Windows: see miniconda installation instructions and initialize conda in Windows PowerShell following these instructions: https://stackoverflow.com/a/58211115  
    * WSL2: see the two links in point 1.  
3. Get pyenv(-win) + pipenv for Windows and WSL2's Linux for projects that use pipenv or venv + pip  
    * Windows:  
	  (a) install pyenv-win (I used conda base's pip): https://pypi.org/project/pyenv-win/  
	  (b) install pipenv (I used pipx as recommended): https://pipenv.pypa.io/en/latest/install/#installing-pipenv  
	  note: `pipx` might not be recognized after `pip install --user pipx`. If true, read this note: https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv  
	  (bonus) nice article that clarifies a lot e.g. `pyenv rehash`: https://dev.to/dendihandian/pyenv-in-windows-4lpe
	* WSL2:  
	  (a) install pyenv with apt: https://realpython.com/intro-to-pyenv/#installing-pyenv  
      (b) pipenv with apt: https://pypi.org/project/pipenv/  
    * Use `pipenv install` to install correct Python version (using pyenv under the hood) and dependencies from Pipfile: https://pipenv.pypa.io/en/latest/advanced/#automatic-python-installation  
	  Note: the Windows or WSL2 pyenv + pipenv are used based on which shell is used to `pipenv install`.

## Questions:
* How does pipenv work with different versions of Python?
    * Q: Do I have to install the Python version I want to use in conda, before being able to create a pipenv with that version of Python?  
	  A: No. First of all, pyenv doesn't really work for Windows, it's meant to seperate the system Python from Python versions that are used for development.
	  In a Linux, or WSL2 OS, pyenv can complement pipenv (or poetry or venv + pip).
    * install pyenv: https://realpython.com/intro-to-pyenv/#installing-pyenv  
	  pyenv + pipenv: https://towardsdatascience.com/python-environment-101-1d68bda3094d  
	  https://pipenv.pypa.io/en/latest/advanced/#automatic-python-installation  
* What is the resulting structure of the Windows pyenv + pipenv installation?  
    1. (base) PS C:\Users\User1> pip install pyenv-win  
	  No need to use conda's python though. pyenv can also be installed with `chocolatey`.
	2. (base) PS C:\Users\User1> pip install --user pipx
	3. (base) PS C:\Users\User1> pipx install pipenv
	  Complication encountered with virtual environment creation. Seems no venv.

## git
* git commit + push command sequence
  1. `git status`
  2. `git add .`
  3. `git commit`
  4. `git push`
* git log -ADOG -> git graph  
  `git log --all --decorate --oneline --graph`


## PyCharm shortcuts & handy stuff
* `Ctrl + Shift + A` : Find a Pycharm shortcut.
* `Alt + Click` : Set multiple cursors.
* `Alt + F7` : Find usages of selected variable.
* `Alt + J / Shift + Alt + J` : Select / unselect next occurence of variable.
* `Shift + F6` : Refactor -> rename selected variable
* `Ctrl + B` : Go to file and location of definition of selected class or function.
* `Alt + Enter` : Show context actions.

handy PyCharm stuff  
* Debugging tutorial: https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html
