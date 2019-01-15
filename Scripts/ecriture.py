#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

#fonction de lecture de fichier .msh

import numpy

class Ecriture:
	def __init__(self,nom):
		self.nom = nom

	def affichage(self,nom):
		print("################################ Fonction",nom," : #########################################")


	def ecriture(self, matrice):
		fichier = open(self.nom, "w")
		n = len(matrice)
		for i in range(0,n):
			fichier.write(repr(matrice[i]))
			fichier.write('\n')
		fichier.write('\n')
		fichier.close()