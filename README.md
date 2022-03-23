# Hello Python
Some tips, tricks and explanations related to Python, Jupyter and git on Windows




# git
## CRLF (Windows) & LF (Linux & Mac) line endings merge issues
### TL;DR
Solving merge issues caused by a mix of CRLF (Carriage Return and Line Feed) and LF (Line Feed) line endings:
the fool proof fail proof solution: add a .gitattributes with the following three lines to your repo:
```
* text=auto eol=lf
*.{cmd,[cC][mM][dD]} text eol=crlf
*.{bat,[bB][aA][tT]} text eol=crlf
```
Recommended autocrlf configurations:  
set `git config --global core.autocrlf true` in Window  
set `git config --global core.autocrlf false` in WSL2's Linux  

### CRLF & LF line endings merge issues 
The cause of these merge problems: there is a mix of files where some have CRLF and others have LF line endings.  
In a git repo all files, except for Windows scripts, are supposed to have LF line endings.  
Therefore one has two options for setting the autocrlf configuration when developing on Windows:
1. set `git config --global core.autocrlf true`
2. set `git config --global core.autocrlf false` and set your IDE to create new files with LF line endings and __ONLY use that IDE__ to create new files in your git projects.

Setting the autocrlf configuration of git to true converts all line endings to CRLF when writing from git's object data base to your working directory and converts all files with CRLF line endings to LF line endings when committing to git. Therefore, 'true' is the recommended setting on Windows, because it ensures that your repository has LF line endings, while retaining CRLF in your working directory. When setting the autocrlf configuration to false no line ending conversion is applied, meaning that, if you're not careful, you could commit files with CRLF line ending to your repo. Note that for your WSL2's Linux distro your should NOT set the autocrlf configuration to true, because Linux cannot handle CRLF line endings.

Apart from the autocrlf configuration there is the fool proof and fail proof solution of adding a .gitattributes file with the three lines shown above to your repo. This automatically handles the CRLF - LF line ending conversion for all participants in the repo. No one can make a mess of the line endings anymore this way!

References:  
* [Great article that explains CRLF and LF in more detail](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/)  
* [Source of .gitattributes](https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files)

In case something went wrong, use the find_line_endings.sh and fix_git_crlf-lf.sh to fix all the line endings.


## Basic & handy `git` commands
* git commit + push command sequence
  1. `git status`
  2. `git add .`
  3. `git commit -m "semantic category: commit message"`
  4. `git push`
* "Semantic git commit messages" put commits into categories: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`, [see this GitHub Gist](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
* git log -ADOG -> git graph  
  `git log --all --decorate --oneline --graph`
* Access the global git configuration  
  `git config --global --edit`
* Manage remotes and setup to enable pushing to multiple:  
  ```
  git remote -v
  git remote add REMOTE-ID REMOTE-URL
  git remote remove REMOTE-ID
  
  # Create a new remote called "all" with the URL of the primary repo.
  git remote add all git@github.com:jigarius/toggl2redmine.git
  # Re-register the remote as a push URL.
  git remote set-url --add --push all git@github.com:jigarius/toggl2redmine.git
  # Add a push URL to a remote. This means that "git push" will also push to this git URL.
  git remote set-url --add --push all git@bitbucket.org:jigarius/toggl2redmine.git
  # Push to all remote branches using:
  git push all BRANCH
  ``` 
  [Source](https://jigarius.com/blog/multiple-git-remote-repositories#push-to-multiple-remotes)



# Python & Jupyter
## Intro to using Python, `conda` and Python package management
* Using Python in Arup is easiest by installing "Anaconda 3" from the Arup shop.
* After installing Anaconda 3 you'll have access to the `conda` command in the (Anaconda) Command Prompt (cmd).
* `conda` handles virtual environments for you and is also a package manager. 
* Virtual environments allow you to use a different version of Python and Python packages for every project. This way 
  you make sure that stuff works and you don't run into dependency issues where e.g. package A depends on version 1 of 
  package C, while at the same time package B depends on version 2 of package C (very unhandy).
* For Python the most well known package managers are 1. `pip` ([pypi.org](https://pypi.org/)) and 2. `conda` 
  ([anaconda.org/anaconda/repo](https://anaconda.org/anaconda/repo)).
* In a `conda` virtual environment you can install packages using both `pip install` and/or `conda install`.
* It is best practice (and easiest) to create a `conda` virtual environment (`conda create --name xxx python=3.#`) and 
  then either use `conda` as the package manager OR `pip` as the package manager, i.e. try not to mix 
  using `conda install` and `pip install` in a single virtual environment (dependency issues).

Example creating and managing your virtual environments with `conda` in the command line:
* View a list of your virtual environments: `conda env list`
* Create a new virtual environment: `conda create --name example_env python=3.10` 
* Activate an environment: `conda activate example_env`
* View a list of the installed packages in your currently active virutal environment: `conda list`
* Deactivate currently active environment: `conda deactivate`
* Installing packages in your CURRENTLY ACTIVE virtual env: `pip install pandas`


## Jupyter Kernel setup
* Add the currently active virtual environment to the Jupyter Kernels  
  `python -m ipykernel install --name py36-test`
* List the available Jupyter Kernels  
  `jupyter kernelspec list`
* Remove a Jupyter Kernel  
  `jupyter kernelspec uninstall unwanted-kernel`

Source: https://janakiev.com/blog/jupyter-virtual-envs/


## Python project Structure
The project sturcture shown in the tree below and of this repo is based on [this Real Python tutorial](https://realpython.com/python-application-layouts/).

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


## Setting up Windows for Python development
TO BE UPDATED
I recommend working with conda & conda + pip in Windows and conda & pyenv + pipenv in the Windows Subsystem for Linux (WSL2). Using pipenv in Windows without pyenv-win makes pipenv use the system Python, or the Python installed in the conda (base) environment and I found that working with pyenv-win is not convenient.
1. Get miniconda for Windows: https://stackoverflow.com/a/58211115
2. Install WSL2: https://docs.microsoft.com/en-us/windows/wsl/install-win10 & https://www.bradleysawler.com/engineering/python-conda-wsl-2-ubuntu-setup-on-windows-10/
3. Get the Windows Terminal from the Microsoft Store. The Windows terminal allows you to open multiple command lines (CMD, PowerShell, you WSL Linux Distro) in the same program.
4. Install git in the conda (base) environment on Windows. Note: in the WSL2 git comes preinstalled with your WSL2 Linux distro.
5. ¡¡¡IMPORTANT!!! line ending (CRLF or LF) settings for git and the `.gitattributes`, see the section `git` below.
6. Get pyenv + pipenv for WSL2's Linux for projects where you want to use pipenv or venv + pip.  
  (a) install pyenv with apt: https://realpython.com/intro-to-pyenv/#installing-pyenv  
  (b) pipenv with apt: https://pypi.org/project/pipenv/  
  (c) Use `pipenv install` to install correct Python version (using pyenv under the hood) and dependencies from the Pipfile: https://pipenv.pypa.io/en/latest/advanced/#automatic-python-installation



# IDE Tips & Tricks
## VS Code
* [Windows keyboard shortcut cheatsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
* `` Ctrl + ` `` : Show integrated terminal
* `` Ctrl + Shift + ` `` : Create new integrated terminal
* `Alt +  ↑ / ↓` : Move line up / down
* `Alt + Shift +  ↑ / ↓` : Copy line above / below
* `Alt + Click` : Insert multiple cursors
* `Alt + Ctrl +  ↑ / ↓` : Insert cursor above / below
* `Ctrl + U` : Undo last multi-cursor operation
* `Ctrl + D` : Add selection to next Find match
* `F12` : Go to definition of selected variable, function or class
* `Alt + F12` : Peek Definition
* `Ctrl + K F12` : Open Definition to the side
* `F2` : Rename selected variable, function or class
* `Ctrl + Space, Ctrl + I` : Trigger suggestion
* `Ctrl + Shift + Space` : Trigger parameter hints
* `Ctrl + .` : Show "Quick fix" context actions
* `Shift + Alt + F` : Format document
* `Ctrl + K Ctrl + F` : Format selection

## PyCharm
* `Ctrl + Shift + A` : Find a Pycharm shortcut.
* `Alt + Click` : Set multiple cursors.
* `Alt + F7` : Find usages of selected variable.
* `Alt + J / Shift + Alt + J` : Select / unselect next occurence of variable.
* `Shift + F6` : Refactor -> rename selected variable
* `Ctrl + B` : Go to definition of selected class, function or variable.
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
