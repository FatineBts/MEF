#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

from Scripts.lecture import *
from Scripts.matrices import *
from Scripts.mat_creuse import *

########################## Appel de fonctions ########################

lecture = Lecture()
fichier = "Maillage/sousmarin.msh"
lecture.affichage("lecture_fichier_msh")
lecture.lecture_fichier_msh(fichier)

matrice_creuse = Matrice_creuse()
lecture.affichage("test_matrice")
matrice_creuse.test_matrice()

ma_matrice = Matrice()
lecture.affichage("calcul_membre_droite")
ma_matrice.calcul_membre_droite()
