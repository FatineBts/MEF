#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy as np
from math import cos
from scipy import sparse
from ecriture import *
import array as arr

"""
Simulations numériques
1. Augmentez le nombre d’onde k. Attention, n’oubliez pas que le maillage doit lui aussi devenir de plus en plus fin. Quel est le nombre d’onde maximal que vous avez pu faire tourner ?
2. Ondes de Herglotz : plutôt qu’une seule onde plane, prenez comme onde incidente une somme d’ondes planes avec un poids particuliers pour chacune d’elles. Ce type d’onde est appelée Onde de Herglotz

Analyse du code
1. Profiling de code : quelle opération prend le plus de temps CPU ? De mémoire ?
2. Vitesse du programme en fonction du nombre d’inconnues
3. Analyse de l’erreur en norme L2
4. Pourquoi avez-vous fait tel ou tel choix ?

Améliorations
1. Que pourrions nous modifier pour accélérer le code ?
2. Que faudrait il modifier pour faire du P2 ? P3 ?

Astuces 
1. Apportez des résultats de simulation complets avec vous : image du résultat, paramètres utilisés
2. Soyez active/actif : “j’ai fait ci en utilisant ça, regardez comme je suis un boss”
3. Préparez un (voire des) exemple(s) ready-to-use : je n’aurais qu’à faire (par exemple) :
gmsh example.geo -2    # Génération du maillage
python example.py      # Résolution
paraview example.vtu   # Affichage

Et boum, ça me génére le maillage, résout le problème, et me l’affiche. Bien entendu, dans ce cas, il faut que le problème soit rapide à résoudre. Si ma machine tombe en rade, ça va probablement me déplaire…

4. N’oubliez pas le fichier README ! Il devrait par exemple m’expliquer comment lancer un exemple simple !
5. Préparez plusieurs exemples tout prêt, qui peuvent être (pas obligé !) rangés dans des dossiers. Le jour J, vous ne disposez que de 10 minutes pour me présenter votre travail. Rappelez-vous que je ne peux juger votre travail que sur ce que vous me montrez…
6. Last but not least: versionnez vos codes avec git!
"""

class Matrice:
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements
	
	def f(self,x): 
		return 0
		
	def g(self,x): 
		return x[0]*x[1]

	def nombre_de_triangles(self): 
		nombre_triangles = 0
		for k in self.Elements: #donne le nombre de triangles 
			if(k[1]==2):
				nombre_triangles+=1
		return nombre_triangles

	def calcul_matrice_masse(self): 
		Matrix = []
		L = []
		C = []
		nombre_triangles = 0

		for k in self.Elements: #donne le nombre de triangles 
			if(k[1]==2):
				nombre_triangles+=1

		#pour chaque triangle k
		for k in self.Elements:
			if(k[1]==2): #si jamais on est sur un triangle et non un segment ou autre 
				p1 = k[len(k)-3] # Ca correspond au num des sommets
				p2 = k[len(k)-2]
				p3 = k[len(k)-1]
				#liste des coordonnées pour chaque point (pas z car on est en 2 D)
				x1 = self.Nodes[p1-1] # Equivalent de Loc2Glob
				x2 = self.Nodes[p2-1] # On aura accès à x y z 
				x3 = self.Nodes[p3-1]
				#Calcul de l'aire = 1/2 du det pour chaque triangle 
				det_k = np.abs((x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2])) 
				Aire_k = 1./2.*det_k #Aire d'un triangle k 
				#contruction de la matrice en LOCAL
				for i in range(0,3):  #on met 3 car c'est un triangle
					for j in range(0,3):
						L.append(k[i])
						C.append(k[j])
						if(i==j): 
							Matrix.append(Aire_k/6.) #si c'est sur la diagonale
						else: 
							Matrix.append(Aire_k/12.) #autre

		print(len(L))

		#La construction GLOBALE de la matrice de masse se fait grace au append en ajoutant au fur et à mesure les 
		#élements avec append()
		# On écrit avant de la mettre sous forme de matrice creuse
		ecriture = Ecriture("Matrice_masse.csv")
		ecriture.affichage("Ecriture_matrice")
		ecriture.ecriture(Matrix)

		#Pour pouvoir utiliser Scipy et ses matrices creuses (sparse matrices en anglais), nous devons utiliser Python2 (et non Python3). 
		#Le plus pratique pour construire la matrice du système au format CSR est certainement de créer une matrice au format COO (coo_matrix) en ajoutant chaque contribution élémentaire à la suite (sans les sommer) puis de convertir la matrice au format CSR à l’aide de tocsr. 
		#La sommation sera automatiquement effectuée par Scipy.
		
		print(self.Nombre_Nodes)
		Matrix = sparse.coo_matrix((Matrix),shape=(self.Nombre_Nodes,self.Nombre_Nodes)) #pour former une matrice au format coo
		Matrix = Matrix.tocsr() #retourne une matrice en forme de ligne (manière condensée)
		print("Nombre de lignes obtenues :", np.size(Matrix))
		print("Nombre de lignes que l'on doit avoir dans la matrice de Masse : ", nombre_triangles*9)
		#on obtient le meme nombre car commence à 0 dans la matrice donc ok
		return Matrix 

	def calcul_matrice_rigidite(self): 
		Matrix = []
		coef = 1./2.
		nombre_triangles = 0
		B_k = []

		#pour chaque triangle k
		for k in self.Elements:
			if(k[1]==2): #si jamais on est sur un triangle et non un segment ou autre 
				p1 = k[len(k)-3] 
				p2 = k[len(k)-2]
				p3 = k[len(k)-1]
				#liste des coordonnées pour chaque point (pas z car on est en 2 D)
				x1 = self.Nodes[p1-1] 
				x2 = self.Nodes[p2-1] 
				x3 = self.Nodes[p3-1]
				determinant_k = np.abs((x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2])) # x2[1] = y2
				B_k = [[x3[2]-x1[2],x1[2]-x2[2]],[x1[1]-x3[1],x2[1]-x1[1]]]

				#on multiplie B_k par 1/deteminant pour chacune de ses valeurs
				for i in range(0,len(B_k)):
					for j in range(0,len(B_k)):
						B_k[i][j] = B_k[i][j] *(1./determinant_k)
				
				#contruction de la matrice en LOCAL
				for i in range(0,3):  #on met 3 car c'est un triangle
					for j in range(0,3):
						if(i==1 and j==1): 
							Matrix.append(coef*2.) #si c'est sur la diagonale
						if(i==j and i!=1 and j!=1): 
							Matrix.append(coef*1.) #si c'est sur la diagonale
						if(i==0 and j!=0): 
							Matrix.append(coef*(-1.)) #si c'est sur la diagonale
						if(j==0 and i!=0): 
							Matrix.append(coef*(-1.)) #si c'est sur la diagonale
						else: 
							Matrix.append(0) #si c'est sur la diagonale

		Matrix = sparse.coo_matrix(Matrix,shape=(self.Nombre_Nodes,self.Nombre_Nodes))
		Matrix = Matrix.tocsr()
		return Matrix

	def calcul_membre_droite(self,methode):
		second_membre = []
		sigma = 2
		#ici on considère les segments donc les bords
		for e in self.Elements: 
			if(e[1]==1): #alors il s'agit d'un segment 
				p1 = e[len(e)-2] #on a que deux points 
				p2 = e[len(e)-1]
				#liste des coordonnées pour chaque point (pas z car on est en 2 D)
				s1 = self.Nodes[p1-1] #sommet pour le triangle e 
				s2 = self.Nodes[p2-1] 
				#on va utiliser ici la méthode de Simpson car elle donne un degré de précision de 2
				s12 = [(s1[1]+s2[1])/2.,(s1[2]+s2[2])/2.] #pas vraiment besoin de la 3ème dimension car vaut 0
				#sigma = norm(s1-s2), on utilise la distance euclidienne car c'est la plus courante 
				sigma = np.sqrt((s1[0]-s2[0])**2+(s1[1]-s2[1])**2)
				if(methode=="point_du_milieu"): 
					pdm = self.g(s12)
					pdm = np.abs(sigma)/6.
					second_membre.append(pdm)
				if(methode=="trapeze"): 
					trapeze = (self.g(s1)+self.g(s2))
					trapeze = np.abs(sigma)/2.
					second_membre.append(trapeze)
				if(methode=="simpson"): 
					simpson = (self.g(s1)+4.*self.g(s12)+self.g(s2))
					simpson = np.abs(sigma)/6.
					second_membre.append(simpson)

		if(methode=="point_du_milieu"): 		
			ecriture = Ecriture("Second_membre_point_du_milieu.csv")
			ecriture.affichage("ecriture_second_membre_point_du_milieu")
			ecriture.ecriture(second_membre)
		if(methode=="trapeze"): 		
			ecriture = Ecriture("Second_membre_trapeze.csv")
			ecriture.affichage("ecriture_second_membre_trapeze")
			ecriture.ecriture(second_membre)
		if(methode=="simpson"): 		
			ecriture = Ecriture("Second_membre_simpson.csv")
			ecriture.affichage("ecriture_second_membre_simpson")
			ecriture.ecriture(second_membre)
	
		return second_membre

	def resolution_systeme(self,Masse,Rigidite,membre_droite): 
		np.linalg.solve(Masse+Rigidite,membre_droite)
