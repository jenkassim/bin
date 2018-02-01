#
# Python How-Tos
#http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
#https://developer.fedoraproject.org/start/sw/web-app/django.html
#https://virtualenvwrapper.readthedocs.io/en/latest/

Python PATH
/usr/lib/python2.x/site-packages/
/usr/bin/python*

Unix Python installed 
- Alternatives : sudo alternatives --config python

Install pip packages on ~/
- sudo dnf install python34-setuptools
- sudo python3 -m pip install pylint

Freeze current state of env packages
- pip freeze > requirements.txt

Re-install env with saved staticfiles
- pip install -r requirements.txt

=======================

## A) Use mkvirtual environment:
#### Installation
This method uses the virtualenvwrapper to create multiple env. 
Note: Should be installed into same global site-packages where virtualenv is installed (ie NOT within a virtualenv) but I didnt do this due to multiple alternatives on global site packages 

```
    $ pip install virtualwrapper
```

    - Add to shell startup to set location (added to ~/.bashrc):
```
    $ export WORKON_HOME=$HOME/bin/venv
        - where venv should live and location of dev projects directories
    $ source /usr/bin/virtualenvwrapper.sh
        - source to shell startup file for virtualenvwrapper.sh
```
    - Always source after changes to .bashrc to run the script
    - Check installed packages : lssitepackagesvirtu

#### Setup
    - Create virt env in folder $HOME/bin/venv/
```
    $ export PROJECT_HOME=<proj dir>
    $ mkvirtualenv -p /usr/bin/python3.6 <venv-name> 
```

    Alternatively, just use an alias: 
    alias as : ` $ mkvenv <venv-name> `

#### Activate / De-activate
- List of venv : `ls $WORKON_HOME`
- Switch between venv : `workon <venv_name>`
- Verify correct venv : `echo $VIRTUAL_ENV`
- To get list of virtual environment wrappers created: ` $ workon `
- To deactivate: ` $ deactivate `
- Able to create project directory which auto switched into when workon project is executed in ~/.bashrc ` $ export PROJECT_HOME=<path>`
- To delete env `$ rmvirtualenv <venv>`



## B) Setup Virtual Environment venv

#### Setup
    - Specifies which version of python to be installed
``` 
    $ mkdir <folder>
    $ virtualenv -p /usr/bin/python3.6 <venv-name>
```
    - Add python env var in ~/.bashrc
```
    $ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
```
   
    - Or use std default templates located below and copy to dev folder and rename
        ~/bin/venv/python3_6
        ~/bin/venv/python2_7

#### Activate / De-activate
    - To activate: 
``` 
    $ cd <venv-folder>
    $ source <venv-folder>/bin/activate
```

    - To deactivate: ` $ deactivate `




## Basic installation packages :
- pip install requests







