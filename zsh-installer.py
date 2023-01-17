#!/usr/bin/env python3
"""This installer is for installing zsh with oh-my-zsh 
and will include dependency checks and minor customization options
|| Wes Pritchard
"""

#### gathering modules
import modules.packagemanager_check as pm_check
import modules.package_deps_install as pkg_install
import importlib
import os
import sys
#### gathering variables
HOME = os.getenv('HOME')
PWD = os.getcwd()
#### importing python dependencies
with open(f"{PWD}/dependencies/python_dependencies.txt", "r") as deplist: 
    mods = []
    for line in deplist:
        modname= line.strip("\n")
        mods.append(modname)
    for mod in mods:
        globals()[mod] = importlib.import_module(mod)

def main():
    supported_pkgm = ["apt", "yum", "dnf"]
    pkg_m = pm_check.packagemanager_check()
    pkg_install(pkg_m)
    playbookpath = f'{PWD}/project/{pkg_m}playbook.yaml'

    if pkg_m in supported_pkgm:
        out, err, rc = ansible_runner.run_command(
            executable_cmd='ansible-playbook',
            cmdline_args=[playbookpath, '-K'],
            input_fd=sys.stdin,
            output_fd=sys.stdout,
            error_fd=sys.stderr,
        )
    else:
        print("Sorry, looks like your distro might not be supported.")
    
    print("Please log out and back in to see the effect!")

####add customizations
#edit .zshrc to include updated ~/bin PATH
#download selected plugins
#source .zshrc

if __name__ == "__main__":
    main()