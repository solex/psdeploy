=========
PS Deploy
=========

First, install `psdeploy` with `setuptools`::

    python setup.py install

It will additionally install `PasteScript`, `PasteDeploy` and `Paste`.

Then, in the directory where you store your projects, run::

    paster create --template=odesk_app myapp

It will ask you to enter some variables. For many of them you can just use
default values.

The result will be something like the following layout::

    `~myapp/
      |~myapp/
      | |+media/
      | |+templates/
      | |-__init__.py
      | |-local_settings.py
      | |-local_settings.py.def
      | |-manage.py
      | |-settings.py
      | `-urls.py
      |-README.rst
      `-requirements.txt

Then you can switch to a new project directory, initialize `git` repo and 
install basic requirements::

    cd myapp
    git init
    python bootstrap.py

.. note::
    Please note that `local_settings.py` will be ignored by `git`
