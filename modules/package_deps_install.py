"""This script installs linux package dependencies from a file called "../dependencies/package_dependencies.txt" when called"""

def install_pkg_deps():
    from os.path import dirname, abspath
    import packagemanager_check as pm_check
    dir_up = dirname(dirname(abspath(__file__)))
    with open(f"{dir_up}/dependencies/package_dependencies.txt", "r") as pkgs:
        if pm_check == "apt":
            import apt_pkg
            for pkg in pkgs:
                apt_pkg.do_install(pkg)
        elif pm_check == "dnf" or pm_check == "yum":
            deps = str(pkgs.read()).replace("\n",' ')
            print(f"sudo {pm_check} install {deps} -y")