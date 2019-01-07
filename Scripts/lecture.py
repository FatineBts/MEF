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
		Entities = []
		Nodes = []
		Elements = []
		Nombre_Nodes = []
		Nombre_Elements = []
		Nombre_lignes = 0
		lignes = open(fichier, "r")
		l = lignes.readlines() #va permettre de lire le fichier 

		for i in l: #donne le nombre de lignes du fichier 
			Nombre_lignes += 1
		
		print "Le fichier comporte " + str(Nombre_lignes) + " lignes."


		for i in range(0,Nombre_lignes):
			if(l[i]=='$Entities\n'): #si on rencontre des noeuds
				for j in range(i+1,Nombre_lignes):
					if l[j]!='$EndEntities\n':
						l[j] = l[j].split(" ")
						Entities.append(l[j])		
					else: 
						break;

			if(l[i]=='$Nodes\n'): #si on rencontre des noeuds
				Nombre_Nodes = l[i+1].split(" ")
				for j in range(i+2,Nombre_lignes):
					if l[j]!='$EndNodes\n':
						l[j] = l[j].split(" ")
						Nodes.append(l[j])		
					else: 
						break; 

			if(l[i]=='$Elements\n'): #si on rencontre des noeuds 
				Nombre_Elements = l[i+1].split(" ") 
				for j in range(i+2,Nombre_lignes):
					if l[j]!='$EndElements\n':
						l[j] = l[j].split(" ") #pour convertir l[j] en liste avant de mettre dans Elements
						Elements.append(l[j])
					else: 
						break; 
		 
		print "Premier Entity : "
		print Entities[0]
		print "Premier triangle : "
		print Nodes[0]
		#print Nodes[0][1]
		print "Premier élement : "
		print Elements[0]
		print "Nombre de triangles :"
		print Nombre_Nodes
		print "Nombre d'élements :"
		print Nombre_Elements
		print "Test :"
		a = float(Nodes[5][1]) + 1 
		print a 
