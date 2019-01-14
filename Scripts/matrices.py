#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy as np
import math 
from scipy import sparse

class Matrice:
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements
	
	def calcul_matrice_masse(self):
		Matrix = []
		lignes = []
		colonnes = []
		debut = self.Nombre_lignes - self.Nombre_Elements
		fin = self.Nombre_lignes - debut
		for j in range(0,fin):
			#on recupère le nombre de colonnes pour savoir quel indice prendre 
			nombre_colonnes_Elements = len(self.Elements[j])
			#numéro des points qui constituent les triangles 
			num_p1 = self.Elements[j][nombre_colonnes_Elements-3]
			num_p2 = self.Elements[j][nombre_colonnes_Elements-2]
			num_p3 = self.Elements[j][nombre_colonnes_Elements-1]
			#liste des coordonnées pour chaque point (pas z car on est en 2 D)
			x1 = self.Nodes[num_p1-1] 
			x2 = self.Nodes[num_p2-1] 
			x3 = self.Nodes[num_p3-1]
			#Calcul de l'aire = 1/2 du det 
			Aire = (x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2]) # x2[1] = y2
			Aire = 1./2.*Aire
		#contruction de la matrice 
		for i in range(self.Nombre_Elements): 
			for j in range(self.Nombre_Elements):
				if(i==j): 
					Matrix.append(Aire/12.*2) #si c'est sur la diagonale
				else: 
					Matrix.append(Aire/12.*1) #autre
		#recuperation des lignes et des colonnes
		# A[i[k], j[k]] = data[k] donc  A[i[0], j[0]] = Matrix[0] 
		for i in range(len(self.Elements)): 
			for j in range(len(self.Elements)): 
				lignes.append(i) #on recupère les indices des lignes de Matrix 
				colonnes.append(j) #on recupère les indices des colonnes de Matrix

		#Pour pouvoir utiliser Scipy et ses matrices creuses (sparse matrices en anglais), nous devons utiliser Python2 (et non Python3). 
		#Le plus pratique pour construire la matrice du système au format CSR est certainement de créer une matrice au format COO (coo_matrix) en ajoutant chaque contribution élémentaire à la suite (sans les sommer) puis de convertir la matrice au format CSR à l’aide de tocsr. 
		#La sommation sera automatiquement effectuée par Scipy.

		#je suis pas sure que ce soit les bons arguments à mettre, demander au prof si il faut entrer shape ? cf documentation internet
		Matrix = sparse.coo_matrix(Matrix, (lignes,colonnes))
		Matrix = Matrix.tocsr() #retourne une matrice en forme de ligne (manière condensée)
		return Matrix 

	def calcul_matrice_rigidite(self): 
		Matrix = []
		debut = self.Nombre_lignes - self.Nombre_Elements
		fin = self.Nombre_lignes - debut
		for j in range(0,fin):
			#on recupère le nombre de colonnes pour savoir quel indice prendre 
			nombre_colonnes_Elements = len(self.Elements[j])
			#numéro des points qui constituent les triangles 
			num_p1 = self.Elements[j][nombre_colonnes_Elements-3]
			num_p2 = self.Elements[j][nombre_colonnes_Elements-2]
			num_p3 = self.Elements[j][nombre_colonnes_Elements-1]
			#liste des coordonnées pour chaque point (pas z car on est en 2 D)
			x1 = self.Nodes[num_p1-1] 
			x2 = self.Nodes[num_p2-1] 
			x3 = self.Nodes[num_p3-1]
			#Calcul de l'aire = 1/2 du det 
			Aire = (x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2])
			Aire = 1./2.*Aire
		#contruction de la matrice 
		for i in range(self.Nombre_Elements): 
			for j in range(self.Nombre_Elements): 
				if(i==0 and j == 0): 
					Matrix.append(1)
				if(i!=0 and j != 0 and i==j):
					Matrix.append(1./2.)
				if(i==0 and j!=0): #cf matrice cours Bertrand Thierry
					Matrix.append(-1./2.)
				if(i!=0 and j==0): #cf matrice cours Bertrand Thierry
					Matrix.append(-1./2.)				
				else: 
					Matrix.append(0)
		print("Calcul de la matrice de rigidité en cours de développement")
		Matrix = sparse.coo_matrix(Matrix)
		Matrix = Matrix.tocsr() #retourne une matrice en forme de ligne (manière condensée)	
		return Matrix

	def calcul_membre_droite(self):
		Vecteur = []
		print "Pas encore fait !"
		return Vecteur

	def resolution_systeme(self,Masse,Rigidite,membre_droite): 
		np.linalg.solve(Masse+Rigidite,membre_droite)
