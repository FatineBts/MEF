#!/usr/bin/env python
# -*- coding: utf-8 -*-

#fonction de lecture de fichier .msh
import numpy as np
import math 

def lecture_fichier_msh(fichier) : 
	Nodes = []
	Elements = []
	nombre_lignes = 0
	lignes = open(fichier, "r")
	l = lignes.readlines() #va permettre de lire le fichier 

	for i in l: #donne le nombre de lignes du fichier 
		nombre_lignes += 1
	
	print "Le fichier comporte " + str(nombre_lignes) + " lignes.\n"

	for i in range(0,nombre_lignes):
		if(l[i]=='$Nodes\n'): #si on rencontre des noeuds 
			for j in range(i+2,nombre_lignes):
				if l[j]!='$EndNodes\n':
					a = l[j].split(" ")[0] #sont toujours composés de 4 élements
					b = l[j].split(" ")[1]
					c = l[j].split(" ")[2]
					d = l[j].split(" ")[3]
					liste = [a,b,c,d]
					Nodes.append(liste)			
				else: 
					break; 

########################## Appel de fonctions ########################

lecture_fichier_msh("sousmarin_simple.msh")
