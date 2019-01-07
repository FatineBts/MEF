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
	def __init__(self):
		self.nom_fichier="Maillage/submarine_simple.msh" 
	# Matrice associée à la formulation faible 
	def matrice_formulation_faible(self):
		k = 2*pi
		n_lambda = 15  
		h = 2*pi/(k*n_lambda)

	def calcul_matrice_masse(self):  
		print "En cours ... soyez patients !"

	def calcul_matrice_rigidite(self): 
		print "En cours ... soyez patients !"


	def calcul_membre_droite(self):
		print "En cours ... soyez patients !"

