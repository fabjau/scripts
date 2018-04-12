#!/usr/bin/python 
# liste les applications et leur version
import csv

listAppli = open("listAppli.lst","r");
chaine = "version" ;
listAppliCsv = csv.writer(open("ListAppli.csv", "wb"));
listAppliCsv.writerow(["Application Name","Version"]);
for pathFile in listAppli:
	fichier = open(pathFile.rstrip('\n'),"r") ;
	for ligne in fichier: 
		if chaine in ligne: 
			version = ligne.split(" ")[1];
			appliName = pathFile.split("/");
			print appliName[len(appliName)-1].split(".")[0] + " " + version;
			listAppliCsv.writerow([appliName[len(appliName)-1].split(".")[0],version]);
listAppli.close();		
fichier.close() ;