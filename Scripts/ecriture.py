#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

#fonction d'écriture de fichier .msh

import numpy

class Ecriture:
	def __init__(self,nom):
		self.nom = nom

	def ecriture(self, matrice):
		numpy.savetxt(self.nom, matrice, delimiter=",") 