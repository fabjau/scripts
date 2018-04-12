#!/bin/sh

#search all file .adef
cd /home/fabrice/Dev
find ./legato/apps/platformServices ./ucgv3 -name *.adef > listAppli.lst

#create csv with list of application and their version
python ../searchAppliVersion.py
