#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy as np
import math 
import scipy as sp

class Matrice:
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.nom_fichier = "Maillage/submarine_simple.msh"
		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements
	
	# Génération d'une matrice creuse aléatoire
	def matrice_creuse(self): 
		# Taille de la matrice
		n = 5
		m = 5
		A = sp.rand(n,m)
		# Ecrire dans un fichier csr
		fichier = open("test.csr", "w")
		for i in range(0,n):
			for j in range(0,m):
				fichier.write(repr(A[i][j]))
				fichier.write('\t')
			fichier.write('\n')
		fichier.close()

	def calcul_matrice_masse(self):
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
			Aire = (x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2]) # x2[1] = y2
			Aire = 1./2.*Aire
		#contruction de la matrice 
		for i in range(self.Nombre_Elements): 
			for j in range(self.Nombre_Elements): 
				Matrix.append(Aire/12.*(2 if i==j else 1)) #si c'est sur la diagonale
		print("Calcul de la matrice de masse finie !")
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
		print("Calcul de la matrice de rigidité en cours de développement")
		#contruction de la matrice 
		for i in range(self.Nombre_Elements): 
			for j in range(self.Nombre_Elements): 
				toto = 1	
		print("En cours ...")
		return Matrix

	def calcul_membre_droite(self):
		Vecteur = []
		print "Pas encore fait !"
		return Vecteur


	def resolution_systeme(self,Masse,Rigidite,membre_droite): 
		np.linalg.solve(Masse+Rigidite,membre_droite)
