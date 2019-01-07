#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy as np
import math 

class Matrice:
	def __init__(self,Nombre_Nodes,Nodes, Nombre_Elements):
		self.nom_fichier="Maillage/submarine_simple.msh" 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Nombre_Elements = Nombre_Elements
		
	# Matrice associée à la formulation faible 
	def matrice_formulation_faible(self):
		k = 2*pi
		n_lambda = 15  
		h = 2*pi/(k*n_lambda)

	def calcul_matrice_masse(self):  
		print "En cours ... soyez patients !"

		M_elem = np.zeros(3,3) # La matrice de masse élémentaire est de taille 3*3
		M_elem = [[2,1,1], [1,2,1], [1,1,2]]
		M = np.zeros(Nombre_Elements, Nombre_Elements) # Matrice de masse 

		for i in range(Nombre_Elements): # Pour chaque triangle 
			for j in range(Nombre_Nodes): # Pour chaque sommet du triangle 

		# La matrice de masse M = int(K) (phi_j(x) * phi_i_bar(x))
		# Etape 1 : On calcule les coefficients de la matrice de masse élémentaire
		# M_e_p(i,j) pour i et j = 1,2,3. C'est une matrice 3*3
		# Etape 2 : Chaque contribution élémentaire est ajoutée à M(I,J)
		# I = loc2Glob(p,i) et J = Loc2Glob(p,j)

	def calcul_matrice_rigidite(self): 
		print "En cours ... soyez patients !"
		# La matrice de rigidité D = int(K) (grad_phi_j(x) * grad_phi_i_bar(x))


	def calcul_membre_droite(self):
		print "En cours ... soyez patients !"

