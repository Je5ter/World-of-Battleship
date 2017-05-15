# World of Battleship

World of Battleship is a battleship game made by three students from Polytech' Nantes, France.
This game was first created for a school project with the following theme : Optimisation, choice, random, constraints.
We've created differents A.I. to play against players or just to see A.I. vs A.I. matches.

## Tech

World of Battleship has been created with different sotware:

* [Atom](https://atom.io/) - A hackable text editor 
* [Python 3.4.3](https://www.python.org) - Programming language
* [Kivy 1.9.1](https://kivy.org/) - Open source Python library for rapid development of applications
* [Photoshop CC](http://www.adobe.com/products/photoshop.html) - The world’s best imaging and design app
* [Premiere Pro CC](http://www.adobe.com/products/premiere.html) -  The industry-leading video editing software
* [After Effects CC](http://www.adobe.com/products/aftereffects.html) - The industry-standard animation and creative compositing app

And of course Worlf of Battleship itself is open source with a [public repository][dill]
 on GitHub.
## Prerequisites

Simply download the _**World of Battleship (Alpha)**_ folder.

## Installation

World of Battleship requires [Python.exe](https://www.python.org/download/releases/3.4.3/) v3.4.3 to run.
First of all, go to the following [official Python website](https://www.python.org/downloads/release/python-343/) and download your corresponding OS version.

### _Windows_
During installation, in the "Customize Python" part, make sure that entire feature of Python will be installed. If not, click on the "Drive's icon" next to "Python" and select "Entire feature will be installed on local drive".

Now, follow the steps to install Kivy 1.9.1.
First of all, open a command prompt like so :
```sh
Press 'Windows + R'
Write 'cmd' and press 'Enter'
Write 'Python' and press 'Enter'
```

At this point we need to check if the latest version of PIP is installed.
```sh
python -m pip install --upgrade pip wheel setuptools
```

Then install kivy's dependencies.
```sh
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
```

Finally, install kivy.
```sh
python -m pip install kivy
```

For further informations about Kivy 1.9.1, please check this [website](https://kivy.org/docs/installation/installation.html).
Installation for [MacOS](https://kivy.org/docs/installation/installation-osx.html) and for [Linux](https://kivy.org/docs/installation/installation-linux.html).

## Running the game

Run the main.py file in the World of Battleship (Alpha) folder with python.
```sh
Right-Click on 'main.py'
Then 'Open with' and search for 'python.exe'
```

## Authors 

* **CAIL Alexandre** - _Game and A.I. development_
* **FROGER Donovan** - _A.I. development_
* **GALAN Yann** - _Game User Interface development_

## License

This is an **Open-source** project.

## About the game
This game is a school porject so it's not totally finished and will certainly not receive any update.
We share our work for non-commercial purposes.
The video used in this game belongs to Wargaming.net. All the rights come back to them. If you are the owner of this content, please contact me. 
