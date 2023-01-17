"""This script installs linux package dependencies from a file called "../dependencies/package_dependencies.txt" when called"""

def install_pkg_deps(pkgmgr):
    from os.path import dirname, abspath
    dir_up = dirname(dirname(abspath(__file__)))
    with open(f"{dir_up}/dependencies/package_dependencies.txt", "r") as pkgs:
        if pkgmgr == "apt":
            import apt_pkg
            for pkg in pkgs:
                apt_pkg.do_install(pkg)
        elif pkgmgr == "dnf" or pkgmgr == "yum":
            deps = str(pkgs.read()).replace("\n",' ')
            print(f"sudo {pkgmgr} install {deps} -y")

if __name__ == "__main__":
    install_pkg_deps()