# #!/usr/bin/env python3
# """This script installs 3rd party pip modules from a file called 'dependencies.txt' """

import importlib
import os
import pip

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])

if __name__ == '__main__':
    import packagemanager_check as pm_check
    with open("package_dependencies.txt", "r") as pkgs:
        deps = []
        for pkg in pkgs:
            deps.append()
        depstring = {print(deps, sep=' ')}
        if pm_check == "apt":
            os.system(f"sudo apt update && sudo apt install {depstring} -y")
        elif pm_check == "dnf" or pm_check == "yum":
            os.system(f"sudo {pm_check} install {depstring} -y")
    
    with open("python_dependencies.txt", "r") as foo:
        mods = []
        for line in foo:
            modname= line.strip("\n")
            mods.append(modname)
            import_with_auto_install(modname)
