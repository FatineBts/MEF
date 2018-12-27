#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Test d'utilisation des matrices creuses
import numpy as np
import math 
import scipy as sp

# Génération d'une matrice creuse aléatoire

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