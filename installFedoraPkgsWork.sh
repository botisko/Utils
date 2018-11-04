#!/bin/bash

### COLOUR OUTPUT
# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

LBLUE='\033[1;34m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check in advance if the packages are already installed
# dnf list | grep $package
# FIRSTLY check and/or install wget, sha1sum...

##################### SNAP PACKAGES ####################
echo -e "${YELLOW}--- SNAP PACKAGES ---${NC}"
# check for snap

### SPOTIFY ###
echo -e "${LBLUE}Installing SPOTIFY...${NC}"
sudo snap install spotify

##################### REPO PACKAGES ####################
echo -e "${YELLOW}--- REPOSITORY PACKAGES ---${NC}"

### FIREFOX ###
echo -e "${LBLUE}Installing FIREFOX...${NC}"
sudo dnf install firefox

### LIBREOFFICE ###
echo -e "${LBLUE}Installing LIBREOFFICE...${NC}"
sudo dnf install libreoffice

<<<<<<< HEAD
### GIT ###
echo -e "${LBLUE}Installing GIT...${NC}"
sudo dnf install git

### MC ###
echo -e "${LBLUE}Installing MC...${NC}"
sudo dnf install mc

=======
>>>>>>> 5463cb1aa3c7b1ebc5052d5e79411358d32096ac
##### CLEAN UP #####
echo -e "${LBLUE}Cleaning up...${NC}"
sudo dnf autoremove

################## AFTER INSTALL NOTES #################
# XFCE only
echo "see https://www.opendesktop.org/s/XFCE/browse/cat/138/ord/top/ and https://www.maketecheasier.com/xfce4-desktop-themes-linux/ for themes"
