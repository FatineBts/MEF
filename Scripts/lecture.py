#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

#fonction de lecture de fichier .msh

class Lecture:
	def affichage(self,nom):
		print("################################ Fonction",nom," : #########################################")

	def lecture_fichier_msh(self,fichier): 
		Nodes = []
		Elements = []
		Nombre_Nodes = 0
		Nombre_Elements = 0
		Nombre_lignes = 0
		lignes = open(fichier, "r")
		l = lignes.readlines() #va permettre de lire le fichier 

		for i in l: #donne le nombre de lignes du fichier 
			Nombre_lignes += 1
		
		print "Le fichier comporte " + str(Nombre_lignes) + " lignes."

		for i in range(0,Nombre_lignes):
			if(l[i]=='$Nodes\n'): #si on rencontre des noeuds
				tmp = l[i+1].split(" ")
				Nombre_Nodes = float(tmp[0])
				for j in range(i+2,Nombre_lignes):
					if l[j]!='$EndNodes\n':
						l[j] = l[j].split(" ")
						tmp = []
						for i in range(len(l[j])):
							tmp.append(float(l[j][i]))
						Nodes.append(tmp)		
					else: 
						break; 

			if(l[i]=='$Elements\n'): #si on rencontre des noeuds 
				tmp = l[i+1].split(" ")
				Nombre_Elements = float(tmp[0])
				for j in range(i+2,Nombre_lignes):
					if l[j]!='$EndElements\n':
						l[j] = l[j].split(" ") #pour convertir l[j] en liste avant de mettre dans Elements
						tmp = [] #pour convertir le tableau qui était en string en float 
						for i in range(len(l[j])-1):
							tmp.append(float(l[j][i]))
						Elements.append(tmp)
					else: 
						break; 
		 

		print "Premier sommet : "
		print Nodes[0]
		#print Nodes[0][1]
		print "Premier élement : "
		print Elements[0]
		print "Nombre de sommets :"
		print Nombre_Nodes
		print "Nombre d'élements :" #triangles; segments ...
		print Nombre_Elements
		print "Test :"
		a = float(Nodes[5][1]) + 1 
		print a 
		return Nombre_Nodes, Nodes, Nombre_Elements

