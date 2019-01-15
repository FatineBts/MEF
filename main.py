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
# Pour le chronométrage
import time 

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
print("Temps d exécution du calcul de la matrice de masse avec ecriture : %s secondes ---" % (time.time() - start_time))
print("\n")

Matrice_de_Rigidite = []
lecture.affichage("calcul_matrice_rigidite")
start_time = time.time()
Matrice_de_Rigidite = M.calcul_matrice_rigidite()
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture : %s secondes ---" % (time.time() - start_time))
print("\n")

Membre_de_droite = []

lecture.affichage("calcul_membre_droite methode du point du milieu")
start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("point_du_milieu")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

lecture.affichage("calcul_membre_droite methode des trapezes")
start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("trapeze")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

lecture.affichage("calcul_membre_droite methode de simpson")
start_time = time.time()
Matrice_de_Droite = M.calcul_membre_droite("simpson")
print("Temps d exécution du calcul de la matrice de rigidite avec ecriture: %s secondes ---" % (time.time() - start_time))
print("\n")

#lecture.affichage("resolution_systeme")
#resolution = M.resolution_systeme(Matrice_de_Masse,Matrice_de_Rigidite,Matrice_de_Droite)
#print("\n")

#déplace les fichiers caches dans un dossier cache (fait automatiquement en Python3 mais on utilise Python2)
os.system("mkdir Scripts/__pycache__ | mv Scripts/*.pyc Scripts/__pycache__")
