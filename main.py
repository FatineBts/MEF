#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

from Scripts.lecture import *
from Scripts.matrices import *
import os

########################## Appel de fonctions ########################

lecture = Lecture()
fichier = "Maillage/sousmarin_simple.msh"
print("\n")

lecture.affichage("lecture_fichier_msh")
Nodes = []
Elements = []
Nombre_lignes, Nombre_Nodes, Nodes, Nombre_Elements, Elements = lecture.lecture_fichier_msh(fichier)
print("\n")

M = Matrice(Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements, Elements)

lecture.affichage("matrice_creuse")
M.matrice_creuse()
print("\n")

Matrice_de_Masse = []
lecture.affichage("calcul_matrice_masse")
Matrice_de_Masse = M.calcul_matrice_masse()
print("\n")

Matrice_de_Rigidite = []
lecture.affichage("calcul_matrice_rigidite")
Matrice_de_Rigidite = M.calcul_matrice_rigidite()
print("\n")

Membre_de_droite = []
lecture.affichage("calcul_membre_droite")
Matrice_de_Droite = M.calcul_membre_droite()
print("\n")

#lecture.affichage("resolution_systeme")
#resolution = M.resolution_systeme(Matrice_de_Masse,Matrice_de_Rigidite,Matrice_de_Droite)
#print("\n")

#déplace les fichiers caches dans un dossier cache (fait automatiquement en Python3 mais on utilise Python2)
os.system("mkdir Scripts/__pycache__ | mv Scripts/*.pyc Scripts/__pycache__")

#pour supprimer les fichiers inutiles 
os.system("rm test.csr")
