"""This script installs linux package dependencies from a file called "../dependencies/package_dependencies.txt" when called"""

def install_pkg_deps(pkgmgr):
    from os.path import dirname, abspath
    import os
    from packagemanager_check import packagemanager_check as pm_check
    pm = pm_check()
    dir_up = dirname(dirname(abspath(__file__)))
    with open(f"{dir_up}/dependencies/{pm}package_dependencies.txt", "r") as pkgs:
        deps = str(pkgs.read()).replace("\n",' ')    
        if pkgmgr == "apt":
            os.system(f"sudo {pkgmgr} install -y {deps}")
        elif pkgmgr == "dnf" or pkgmgr == "yum":
            os.system(f"sudo {pkgmgr} install -y {deps}")

if __name__ == "__main__":
    from packagemanager_check import packagemanager_check as pm_check
    pm = pm_check()
    install_pkg_deps(pm)