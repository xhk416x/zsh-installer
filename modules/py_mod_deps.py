#!/usr/bin/env python3
"""This script installs 3rd party pip modules from a file called '../dependencies/python_dependencies.txt' """

import importlib
import pip
from os.path import dirname, abspath

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])

if __name__ == '__main__':
    dir_up = dirname(dirname(abspath(__file__)))
    with open(f"{dir_up}/dependencies/python_dependencies.txt", "r") as deps:
        mods = []
        for line in deps:
            modname= line.strip("\n")
            mods.append(modname)
            import_with_auto_install(modname)
