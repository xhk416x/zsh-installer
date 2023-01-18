<p align="left"><img src="https://zsh.sourceforge.io/Images/color_vertical_icon.png" alt="zsh"><img src="https://ohmyzsh.s3.amazonaws.com/omz-ansi-github.png" alt="Oh My Zsh"></p>

# Zsh-installer
## This Repo is primarily a skills demonstration. 

The function of this repo is to make a fresh Linux install set up zsh, [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh), along with my personal favorite theme (Agnoster) and plugins ([zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting), [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)) while also installing all requisite packages.

## Installation

CAUTION: Zsh-installer requires the **fonts-powerline** package, which usually requires EPEL repos to be installed on Red Hat distros in order to work. </p>
CAUTION: Ansible 3.X is required at this time. </p>
NOTE: zsh-installer will autodetect distribution and download the respective packages based on the packages listed in **dependencies/{apt/dnf/yum}dependencies.txt**

To install, clone this repo to your user's home directory by running ```git clone https://github.com/xhk416x/zsh-installer.git``` from your linux command line. the cd into the directory with ```cd zsh-installer``` and then run the install.sh script by inputting ```bash install.sh```

## Compatibility

Currently zsh-installer works on:
1. Any debian based distro that has **Ansible 3.X** in its repo.
2. Any red-hat based distro that has the **fonts-powerline** package in its repo. For Red Hat proper this means enabling the EPEL repos.



## Known Issues
- Ansible 2.9 can cause the Ansible Playbooks to fail. 
- There is no check for package availability, which will cause Red Hat distros without EPEL enabled to fail. This will be corrected in the future to throw an error.
- With the Agnoster theme (which is the theme installed by zsh-installer)

## Documentation Refs
- [oh-my-zsh!](https://github.com/ohmyzsh/ohmyzsh) "In this repo you can find all the built-in plugins and themes"
- [Oh-My-Zsh! A Work of CLI Magic Tutorial for Ubuntu by Michiel Mulders](https://medium.com/wearetheledger/oh-my-zsh-made-for-cli-lovers-installation-guide-3131ca5491fb)
- [oh-my-zsh! themes screenshots](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

