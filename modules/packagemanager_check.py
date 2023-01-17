#!/usr/bin/env python3
"""check for package managers and return as string"""

import os

def packagemanager_check():
    try:
        apt = os.system("which apt >> /dev/null 2>&1")
        dnf = os.system("which dnf >> /dev/null 2>&1")
        yum = os.system("which yum >> /dev/null 2>&1")
        pacman = os.system("which pacman >> /dev/null 2>&1")
        if apt == 0:
            return "apt"
        elif dnf == 0:
            return "dnf"
        elif yum == 0:
            return "yum"
        elif pacman == 0:
            return "pacman"
    except:
        print("Uh oh. Spaghetti-o.")

if __name__ == "__main__":
    packagemanager_check()