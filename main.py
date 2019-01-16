#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

from Scripts.lecture import *
from Scripts.matrices import *
from Scripts.creation_paraview import *
import os
# Pour le chronométrage
import time 

print("\n")
print("Bonjour et bienvenue dans le projet de MEF réalisé par Fatine Bentires Alj et Alexia Zounias-Sirabella !!\n")
########################## Appel de fonctions ########################

fichier = "Maillage/sousmarin_simple.msh"
lecture = Lecture(fichier)
print("\n")

lecture.affichage("lecture_fichier_msh")
Nodes = []
Elements = []
Nombre_lignes, Nombre_Nodes, Nodes, Nombre_Elements, Elements = lecture.lecture_fichier_msh()
print("\n")

M = Matrice(Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements, Elements)

Matrice_de_Masse = []
lecture.affichage("calcul_matrice_masse")
start_time = time.time()
Matrice_de_Masse = M.calcul_matrice_masse()
print("\n")
print("Vous trouverez les résultats dans le fichier Matrice_masse.csv !\n")
print("Temps d exécution du calcul de la matrice de masse avec ecriture : %s secondes ---" % (time.time() - start_time))
print("\n")

Matrice_de_Rigidite = []
lecture.affichage("calcul_matrice_rigidite")
start_time = time.time()
Matrice_de_Rigidite = M.calcul_matrice_rigidite()
print("\n")
print("Vous trouverez les résultats dans le fichier Matrice_rigidite.csv !\n")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture : %s secondes ---" % (time.time() - start_time))
print("\n")

Membre_de_droite = []

lecture.affichage("calcul_membre_droite")
start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("point_du_milieu")
print("\n")
print("Vous trouverez les résultats dans le fichier second_membre_point_du_milieu.csv !\n")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("trapeze")
print("\n")
print("Vous trouverez les résultats dans le fichier second_membre_trapeze.csv !\n")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("simpson")
print("\n")
print("Vous trouverez les résultats dans le fichier second_membre_simpson.csv !\n")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

#lecture.affichage("resolution_systeme")
#resolution = M.resolution_systeme(Matrice_de_Masse,Matrice_de_Rigidite,Matrice_de_Droite)
#print("\n")

lecture.affichage("creation vue Paraview")
C = Creation_paraview(Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements, Elements)
C.script_paraview()
print("\n")

#déplace les fichiers caches dans un dossier cache (fait automatiquement en Python3 mais on utilise Python2)
os.system("mv Scripts/*.pyc Scripts/__pycache__")
os.system("mv *.csv CSV")

