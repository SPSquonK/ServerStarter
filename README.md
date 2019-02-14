# ServerStarter

This is a small python script intended to FlyFF developpers.

## Install the script

This script uses python, so be sure python is installed on your system. As FlyFF is entirely running on Windows, the script is made to be compatible with Winbdows only. The script was developped on Python 3.6.

- You also need tkinter for the graphic UI `python -m pip install tkinter`

- The script can be started by running the provided bat file or `python LauncherWindow.py`

- This repo should be cloned in a repertory next to the Source, Program and Resource folders. (So for example, if your FlyFF development folder is `B:\FlyFF\`, your ouput folder will be `B:\FlyFF\Ouput`, your resource will be `B:\FlyFF\Resource`, and the files of this repository will be `B:\FlyFF\Starter`)

## Goal

- X can be AccountServer, CacheServer, Certifier, CoreServer, DatabaseServer, LoginServer or WorldServer

- This script uses the files found in `..\Output\X\Release\X.exe` as the "newly compiled files". The program check if theses files changes, and use them to copy them.

- Actually used files are found in `..\Program\X.exe`. This script will start the executable in the Program folder. These executable are called "Server programs". The script tracks which parts of the server it has started, and when the user press Start, the program check if a new version is available, if so copies it and then run the server executable. If processes are already started, it will kills by itself the releveant process.

- This script also enables to start `..\Resource\Neuz.exe`and edit its corresponding ini file. Original Neuz is found in `..\Output\Neuz\NoGameguard\Neuz.exe` for update purpose.


## Disclaimers

This script is only intended for development purpose, and should not be used in production

## Licence

This script is distributed under the MIT Licence.