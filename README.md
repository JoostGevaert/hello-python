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
1. Debloat Windows
2. Get WSL2 and the WindowsTerminal (Git Bash & Linux e.g. Ubuntu) up and running
    * https://towardsdatascience.com/data-science-on-windows-subsystem-for-linux-2-what-why-and-how-77545c9e5cdf
	* https://www.bradleysawler.com/engineering/python-conda-wsl-2-ubuntu-setup-on-windows-10/
	* ¡¡¡IMPORTANT!!!  
	  set `git config --global core.autocrlf true` in Window's Git Bash  
	  set `git config --global core.autocrlf input` in WSL2's Linux
3. Get miniconda for Windows and WSL2's Linux & get pyenv for WSL2's Linux for projects that use pipenv ect.  
  Initialize conda on Windows: https://stackoverflow.com/a/58211115  
  pyenv in WSL2's Linux: https://realpython.com/intro-to-pyenv/#installing-pyenv  
  pyenv + pipenv: https://towardsdatascience.com/python-environment-101-1d68bda3094d


## Questions:
* How does pipenv work with different versions of Python?
    * Q: Do I have to install the Python version I want to use in conda, before being able to create a pipenv with that version of Python?  
	  A: No. First of all, pyenv doesn't really work for Windows, it's meant to seperate the system Python from Python versions that are used for development.
	  In a Linux, or WSL2 OS, pyenv can complement pipenv (or poetry or venv + pip).
    * install pyenv: https://realpython.com/intro-to-pyenv/#installing-pyenv  
	  pyenv + pipenv: https://towardsdatascience.com/python-environment-101-1d68bda3094d  
	  https://pipenv.pypa.io/en/latest/advanced/#automatic-python-installation


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
