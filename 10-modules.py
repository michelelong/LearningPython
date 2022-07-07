#!/usr/local/bin/python3

# Import a module with an alias
import multiprocessing.dummy.connection as mdc

# Use alias to access module methods
mdc.Queue(5)

# Import only a specified method from a module
# Module name is not needed to call method
from datetime import date
date()

# Import all methods from a module, adds many unneeded methods
# from abc import *

# Import without an alias or specific method
import math

# Module name is needed to call imported method
math.sqrt(5)

# Install 3rd party modules
# pip3 install modulename

# Create a virtual environment to separate dependancies
# python3 -m venv ~/venv/dirname
# source ~/venv/dirname/bin/activate
# pip install modulename to install modules into the venv
# deactivate to exit venv
# pipenv is an environment and dependancy manager
