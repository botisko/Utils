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

################## EXTERNAL RPM PACKAGES ##################
echo -e "${YELLOW}--- EXTERNAL RPM PACKAGES ---${NC}"
### MASTER PDF EDITOR ###
# Download latest version - FIND OUT HOW!
echo -e "${LBLUE}Downloading MASTER PDF EDITOR...${NC}"
# wget https://code-industry.net/public/master-pdf-editor-5.0.36_qt5.x86_64.rpm
# Check SHA1 sum
echo -e "${LBLUE}Checking SHA1 sum...${NC}"
sha1sum master-pdf-editor-5.0.36_qt5.x86_64.rpm
# Install the package
# sudo dnf install master-pdf-editor-5.0.36_qt5.x86_64.rpm
# Remove RPM file
echo -e "${LBLUE}Removing RPM file(s)...${NC}"
# make variable from filename
rm master-pdf-editor-5.0.36_qt5.x86_64.rpm

### VIBER ###
# Download latest version
echo -e "${LBLUE}Downloading VIBER...${NC}"
# wget https://download.cdn.viber.com/desktop/Linux/viber.rpm
# Check SHA1 sum
echo -e "${LBLUE}Checking SHA1 sum...${NC}"
sha1sum viber.rpm
# Install the package
# sudo dnf install master-pdf-editor-5.0.36_qt5.x86_64.rpm
echo -e "${LBLUE}Removing RPM file(s)...${NC}"
# make variable from filename
rm viber.rpm

##################### SNAP PACKAGES ####################
echo -e "${YELLOW}--- SNAP PACKAGES ---${NC}"
# check for snap
### SPOTIFY ###
echo -e "${LBLUE}Installing SPOTIFY...${NC}"
# sudo snap install spotify

### ATOM ###
echo -e "${LBLUE}Installing ATOM...${NC}"
# sudo snap install atom

################## REPOSITORY PACKAGES ################
echo -e "${YELLOW}--- REPOSITORY PACKAGES ---${NC}"
### FIREFOX ###
echo -e "${LBLUE}Installing FIREFOX...${NC}"
# sudo dnf install firefox

### THUNDERBIRD ###
echo -e "${LBLUE}Installing THUNDERBIRD...${NC}"
# sudo dnf install thunderbird
## ANO/NE install lokalizace

### CLEMENTINE ###
echo -e "${LBLUE}Installing CLEMENTINE...${NC}"
# sudo dnf install clementine

### VLC ###
echo -e "${LBLUE}Installing VLC...${NC}"
# sudo dnf install vlc

### LIBREOFFICE ###
echo -e "${LBLUE}Installing LIBREOFFICE...${NC}"
# sudo dnf install libreoffice

### GIMP ###
echo -e "${LBLUE}Installing GIMP...${NC}"
# sudo dnf install gimp

### ECLIPSE ###
echo -e "${LBLUE}Installing ECLIPSE...${NC}"
# sudo dnf install gimp

##### CLEAN UP #####
echo -e "${LBLUE}Cleaning up...${NC}"
# sudo dnf autoremove
