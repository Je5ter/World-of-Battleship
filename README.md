# World of Battleship

World of Battleship is a battleship game made by three students from Polytech' Nantes, France.
This game was first created for a school project with the following theme : Optimisation, choice, random, constraints.
We've created differents A.I. to play against players or just to see A.I. vs A.I. matches.

## Tech

World of Battleship has been created with different sotware:

* [Atom](https://atom.io/) - A hackable text editor 
* [Python 3.5.4](https://www.python.org) - Programming language
* [Kivy 1.11.1](https://kivy.org/) - Open source Python library for rapid development of applications
* [Photoshop CC](http://www.adobe.com/products/photoshop.html) - The world’s best imaging and design app
* [Premiere Pro CC](http://www.adobe.com/products/premiere.html) -  The industry-leading video editing software
* [After Effects CC](http://www.adobe.com/products/aftereffects.html) - The industry-standard animation and creative compositing app
 
## Prerequisites

Simply download the _**World of Battleship (Alpha)**_ folder [here](https://github.com/Je5ter/World-of-Battleship/archive/master.zip).

## Installation

:warning: World of Battleship requires **Python v3.5.4** to run (*not yet tested with higher versions of Python*)  

### Using Conda

If you prefer, there is an easy way of installing **Python 3.5.4** and **Kivy** (with all dependencies) thanks to the **Conda** package manager. We recommend to use the lite version of **Anaconda**, wich is called **Miniconda**. To install this environnement, please check [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/). 

Once the Conda environnement is installed with Python 3.5.4, run the following command inside a command prompt :
```sh
conda install kivy -c conda-forge
```

### Windows

First of all, go to the following [official Python website](https://www.python.org/downloads/release/python-354/) and download your corresponding architecture version.

#### Python installation
During the Python installation setup, make sure that the `Add Python 3.5 to PATH` checkbox is checked, then click on `Install now` and let the installer do the rest.
To check if python is correclty installed, run the following command into a command prompt :
```sh
python --version
```

ℹ *If this command leads to the Windows Store, you needs to **remove Python from the `Application execution aliases`** in the Windows settings. For more information, please refer to [this post](https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor)*


#### Kivy installation
Once Python 3.5.4 is installed, we can focus on the Kivy installation process.

At this point, we need to install the latest version of PIP, the Python's package manager.
```sh
python -m pip install --upgrade pip wheel setuptools virtualenv
```

Then install kivy's dependencies.
```sh
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
```

Finally, install kivy.
```sh
python -m pip install kivy==1.11.1
```

ℹ *For further informations about Kivy 1.11.1, please check this [website](https://kivy.org/doc/stable/gettingstarted/installation.html).*

### Linux and MacOS

Python 3.5.4 installers can be found on the [official Python website](https://www.python.org/downloads/release/python-354/)

Installation guide for Kivy on these OS can be found there : 
* [MacOS](https://kivy.org/doc/stable/installation/installation-osx.html)
* [Linux](https://kivy.org/doc/stable/installation/installation-linux.html).

## Running the game
The game starts with the `main.py` script located in the `World of Battleship (Alpha)` folder. 
There is two ways of running this script : 
* Open the script with the Python executable (Right-click on the script, then `Open With`, then select `python.exe`)
* From a commmand prompt opened in the game folder, run the following command : 
```sh
python main.py
```

## Authors 

* **CAIL Alexandre** - _Game and A.I. development_
* **FROGER Donovan** - _A.I. development_
* **GALAN Yann** - _Game User Interface development_

## License

This is an **Open-source** project.

## About the game
This game is a school project so it's not totally finished and will certainly not receive any update.
We share our work for non-commercial purposes.
The video and the logo used in this game belongs to Wargaming.net. All the rights come back to them. If you are the owner of this content, please contact me. 
