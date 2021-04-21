# Hello Python
An introduction to python basics for Windows and what works best for me.

## Setting up Windows for Development
I recommend working with conda & conda + pip in Windows and conda & pyenv + pipenv in the Windows Subsystem for Linux (WSL2). Using pipenv in Windows without pyenv-win makes pipenv use the system Python, or the Python installed in the conda (base) environment and I found that working with pyenv-win is not convenient.
1. Get miniconda for Windows: https://stackoverflow.com/a/58211115
2. Install WSL2: https://docs.microsoft.com/en-us/windows/wsl/install-win10 & https://www.bradleysawler.com/engineering/python-conda-wsl-2-ubuntu-setup-on-windows-10/
3. Get the Windows Terminal from the Microsoft Store. The Windows terminal allows you to open multiple command lines (CMD, PowerShell, you WSL Linux Distro) in the same program.
4. Install git in the conda (base) environment on Windows. Note: in the WSL2 git comes preinstalled with your WSL2 Linux distro.
5. ¡¡¡IMPORTANT!!! line ending (CRLF or LF) settings for git and the `.gitattributes`, see the section `git` below.
6. Get pyenv + pipenv for WSL2's Linux for projects that use pipenv or venv + pip.  
  (a) install pyenv with apt: https://realpython.com/intro-to-pyenv/#installing-pyenv  
  (b) pipenv with apt: https://pypi.org/project/pipenv/  
    * Use `pipenv install` to install correct Python version (using pyenv under the hood) and dependencies from Pipfile: https://pipenv.pypa.io/en/latest/advanced/#automatic-python-installation


## git
#### TL;DR
Solving merge issues caused by a mix of CRLF (Carriage Return and Line Feed) and LF (Line Feed) line endings:
The fool proof solution: add a .gitattributes with the following three lines to your repo:
```
* text=auto eol=lf
*.{cmd,[cC][mM][dD]} text eol=crlf
*.{bat,[bB][aA][tT]} text eol=crlf
```
Recommended autocrlf configuration:  
set `git config --global core.autocrlf true` in Window  
set `git config --global core.autocrlf false` in WSL2's Linux  

Cause of merge problems: there is a mix of files where some have CRLF and others have LF line endings.  
In a git repo all files, except for Windows scripts, are supposed to have LF line endings.  
Therefore one has two options for setting the autocrlf configuration when developing on Windows:
1. set `git config --global core.autocrlf true`
2. set `git config --global core.autocrlf false` and set your IDE to create new files with LF line endings and __ONLY use that IDE__ to create new files in your git projects.

Setting the autocrlf configuration of git to true converts all line endings to CRLF when writing from git's object data base to your working directory and converts all files with CRLF line endings to LF line endings when committing. Therefore, this is the recommended setting on Windows because it ensures that your repository has LF line endings, while retaining CRLF in your working directory. When setting the autocrlf configuration to false no line ending conversion is applied, meaning that, if you're not careful, you could commit files with CRLF line ending to your repo. Note that for your WSL2's Linux distro your should NOT set the autocrlf configuration to true, because Linux cannot handle CRLF line endings.

Apart from the autocrlf configuration there is the fool proof and fail proof solution of adding a .gitattributes file with the three lines shown above to your repo. This automatically handles the CRLF - LF line ending conversion for all participants in the repo. No on can make a mess of the line endings anymore this way!.

References:
Great article: https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/
Source of .gitattributes: https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files

In case something went wrong, use the find_line_endings.sh and fix_git_crlf-lf.sh to fix all the line endings.

Basic git commands:
* git commit + push command sequence
  1. `git status`
  2. `git add .`
  3. `git commit`
  4. `git push`
* git log -ADOG -> git graph  
  `git log --all --decorate --oneline --graph`

## Project Structure
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
├── .gitattributes  
├── LICENSE  
├── README.md  
├── requirements.txt  
└── setup.py

## PyCharm shortcuts & handy stuff
* `Ctrl + Shift + A` : Find a Pycharm shortcut.
* `Alt + Click` : Set multiple cursors.
* `Alt + F7` : Find usages of selected variable.
* `Alt + J / Shift + Alt + J` : Select / unselect next occurence of variable.
* `Shift + F6` : Refactor -> rename selected variable
* `Ctrl + B` : Go to file and location of definition of selected class or function.
* `Alt + Enter` : Show context actions.

## Questions:
* How does pipenv work with different versions of Python?
    * Q: Do I have to install the Python version I want to use in conda, before being able to create a pipenv with that version of Python?  
	  A: No. First of all, pyenv is meant to seperate the system Python from Python versions that are used for development.
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
