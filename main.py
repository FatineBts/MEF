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
import sys 

print("\n")
print("Bonjour et bienvenue dans le projet de MEF réalisé par Fatine Bentires Alj et Alexia Zounias-Sirabella !! Tous les résultats se trouvent dans le dossier CSV. Les temps d'executions sont les suivants : \n")

########################## Appel de fonctions ########################

fichier = "Maillage/" + str(sys.argv[1])

print ("Vous avez lancé le fichier " + str(fichier) + "\n")
lecture = Lecture(fichier)

Nodes = []
Elements = []
Nombre_lignes, Nombre_Nodes, Nodes, Nombre_Elements, Elements = lecture.lecture_fichier_msh()


################### Etape 1 : calcul de M, D  ##########################
M = Matrice(Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements, Elements)

start_time = time.time()
Matrice_de_Masse = M.calcul_matrice_masse()
print("Matrice de masse avant Dirichlet avec ecriture : %s secondes ---" % (time.time() - start_time))

start_time = time.time()
Matrice_de_Rigidite = M.calcul_matrice_rigidite()
print("Matrice de rigidite avant Dirichlet avec ecriture : %s secondes ---" % (time.time() - start_time))


############### Etape 2 : application des conditions de Dirichlet à A et b #############################

start_time = time.time()
A_dirichlet = M.A_dirichlet(Matrice_de_Masse,Matrice_de_Rigidite)
print("Matrice A (Masse+Rigidité) après Dirichlet avec ecriture : %s secondes ---" % (time.time() - start_time))

start_time = time.time()
Membre_de_Droite = M.calcul_membre_droite()
print("Membre de droite après Dirichlet avec ecriture : %s secondes ---" % (time.time() - start_time))

############### Etape 3 : résolution du système ##################

print("\n")
print("Résolution du système en cours ...")
Resultat = M.resolution_systeme(A_dirichlet,Membre_de_Droite)
print("Système résolu !")

############# Etape 4 : visualisation avec Paraview #############

print("\n")
C = Creation_paraview(Nombre_lignes, Nombre_Nodes, Nodes, Nombre_Elements, Elements,Resultat)
C.script_paraview()
print("Fichier Paraview disponible. Pour le visualiser, tapez paraview paraview.vtu sur le terminal")
print("\n")

#déplace les fichiers caches dans un dossier cache (fait automatiquement en Python3 mais on utilise Python2)
os.system("mv Scripts/*.pyc Scripts/__pycache__")
os.system("mv *.csv CSV")


