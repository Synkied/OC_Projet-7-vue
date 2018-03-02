# GrandPy Bot, the grandpa-bot !
## Test the app online:
https://grandpybot-ql.herokuapp.com/

# Features

# Installation:

### Python 3

Install from : https://www.python.org/downloads/  
Preferably choose Python 3.6.3

### Virtualenv and VirtualenvWrapper

```sh
pip install --user virtualenv
pip install --user virtualenvwrapper
```

#### Unix
After the installation it's time to add theses lines in ```~/.profile``` (maybe ```~/.bashrc``` or ```~/.bash_profile```)

```sh
export WORKON_HOME=~/.virtualenvs
mkdir -p $WORKON_HOME
export PROJECT_HOME=~/pyprojects
mkdir -p $PROJECT_HOME
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.x
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source .local/bin/virtualenvwrapper.sh
```

And finally reload this file :

```sh 
source ~/.profile
```

# Requirements
## Running the virtual environment
After the virtual environment is setup, you can then work on it:
```sh
workon {your_env_name}
```

## Installing the dependencies
```sh
pip install -r requirements.txt
```
or (Unix only)
```sh
make init
```

# Running the app
```sh
python run.py
```
or (Unix only)
```sh
make init
```

# Known issues
