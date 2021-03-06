#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy as np
from math import cos, sin, exp
from scipy import sparse
from ecriture import *
import array as arr
import numpy
from cmath import * #pour les nombres complexes

#gamma infini = bord exterieur
#gamma = bord interieur

class Matrice:
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.Nombre_lignes = int(Nombre_lignes) 
		self.Nombre_Nodes = int(Nombre_Nodes)
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = int(Nombre_Elements)
		self.alpha = 0 #énoncé
		self.k = 20

	def f(self,x):
		return 0

	def u_inc(self,x): #onde helgotz
		#return exp( 1j*self.k* (x[1]*np.cos(self.alpha) + x[2]*np.sin(self.alpha)) ) 
		return exp(1j*self.k* (x[1]*np.cos(self.alpha) + x[2]*np.sin(self.alpha)) ) + 2*exp(1j*self.k* (x[1]*np.cos(self.alpha+np.pi/2) + x[2]*np.sin(self.alpha+np.pi/2)) )

	def nombre_de_triangles(self): 
		nombre_triangles = 0
		for k in self.Elements: #donne le nombre de triangles 
			if(k[1]==2):
				nombre_triangles+=1
		return nombre_triangles

	def calcul_matrice_masse(self): 
		"""
		Résolution de l'équation diffraction accoustique : - intégrale sur omega (grad u * grad v) + k^2 intégrale sur omega (u * v) - i*k* intégrale sur gamma infini (u*v)
		En effet l'intégrale sur le bord de N s'annule au vu des conditions de Dirichlet (v nul sur le bord)
		Matrice de Masse = k^2 intégrale sur omega (u * v) - i*k* intégrale sur gamma infini (u*v)
		Comme on sait d'après le cours que la matrice vaut Aire/6 sur la diagonale et Aire/12 sur le reste 
		pour l'équation : intégrale sur omega (u * v), nous n'avons qu'à multiplier par k^2 
		pour l'équation : - i*k* intégrale sur gamma infini (u*v), nous n'avons qu'à multiplier par -i*k
		"""	

		Matrix = []
		L = []
		C = []
		nombre_triangles = 0

		for e in self.Elements: #donne le nombre de triangles 
			if(e[1]==2):
				nombre_triangles+=1

	################ 1ere partie : gestion de la matrice de masse sur omega #####################
		#pour chaque triangle k
		for e in self.Elements:
			if(e[1]==2): #si jamais on est sur un triangle et non un segment ou autre 
				p1 = e[len(e)-3] # Ca correspond au num des sommets
				p2 = e[len(e)-2]
				p3 = e[len(e)-1]
				#liste des coordonnées pour chaque point (pas z car on est en 2 D)
				x1 = self.Nodes[p1-1] # Equivalent de Loc2Glob
				x2 = self.Nodes[p2-1] # On aura accès à x y z 
				x3 = self.Nodes[p3-1]
				#Calcul de l'aire = 1/2 du det pour chaque triangle 
				det_e = np.abs((x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2]))
				Aire_e = 1./2.*det_e #Aire d'un triangle k

				for i in range(0,3):  #on met 3 car c'est un triangle
					for j in range(0,3):
						L.append(e[len(e)-3+i]-1) #pour acceder aux dernieres valeurs
						C.append(e[len(e)-3+j]-1) 
						if(i==j): 
							Matrix.append(self.k*self.k*(Aire_e/6.)) #si c'est sur la diagonale 
						else: 
							Matrix.append(self.k*self.k*(Aire_e/12.)) #autre
			
	################ 2nd partie : gestion de la matrice de masse sur le bord gamma infini = bord exterieur #####################

		for e in self.Elements:
			if(e[1]==1 and e[3]==1): #si c'est un segment et on est sur le bord exterieur
				p1 = e[len(e)-2] #on a que deux points 
				p2 = e[len(e)-1]
				#liste des coordonnées pour chaque point (pas z car on est en 2 D)
				x1 = self.Nodes[p1-1] #sommet pour le triangle e 
				x2 = self.Nodes[p2-1] 
				sigma_e = np.sqrt((x2[1]-x1[1])*(x2[1]-x1[1]) + (x2[2]-x1[2])*(x2[2]-x1[2]))

				for i in range(0,2):  #on met 2 car c'est un triangle
					for j in range(0,2):
						L.append(e[len(e)-2+i]-1) #pour acceder aux dernieres valeurs
						C.append(e[len(e)-2+j]-1) 
						if(i==j): 
							Matrix.append(-1j*self.k*sigma_e/3.) #si c'est sur la diagonale 
						else: 
							Matrix.append(-1j*self.k*sigma_e/6.) #autre	

		#conversion en array
		L = np.array(L)
		C = np.array(C)

		Matrix = sparse.coo_matrix((Matrix,(L,C)),shape=(self.Nombre_Nodes,self.Nombre_Nodes)) #pour former une matrice au format coo
		Matrix = Matrix.tocsr() #retourne une matrice en forme de ligne (manière condensée)

		ecriture = Ecriture("Matrice_masse.csv")
		ecriture.ecriture(Matrix.toarray()) 

		return Matrix 

	def calcul_matrice_rigidite(self): 
		"""
		Résolution de l'équation diffraction accoustique : - intégrale sur omega (grad u * grad v) + k^2 intégrale sur omega (u * v) - i*k* intégrale sur gamma infini (u*v)
		Matrice de Rigidité = - intégrale sur omega (grad u * grad v)
		Le cours nous donne la matrice pour la même équation : det_k/2 * (grad phi j)Transpose * (B_k_T*B_k)* (grad phi i)
		"""

		Matrix = []
		L = []
		C = []
		Dphi = []

		#gradient des fonctions de forme 
		Dphi.append(np.matrix([[-1],[-1]])) #l'ajout des crochets permet de les créer en colonnes et pas en ligne
		Dphi.append(np.matrix([[1],[0]]))
		Dphi.append(np.matrix([[0],[1]])) 
		Dphi = np.array(Dphi)
		
		for e in self.Elements:
			if(e[1]==2): #si jamais on est sur un triangle et non un segment ou autre 
				p1 = e[len(e)-3] 
				p2 = e[len(e)-2]
				p3 = e[len(e)-1]

				x1 = self.Nodes[p1-1] 
				x2 = self.Nodes[p2-1] 
				x3 = self.Nodes[p3-1]

				det_e = (x2[1]-x1[1])*(x3[2]-x1[2]) - (x3[1]-x1[1])*(x2[2]-x1[2]) 
				B_e = 1./(det_e)*np.matrix([[x3[2]-x1[2],x1[2]-x2[2]],[x1[1]-x3[1],x2[1]-x1[1]]])
				B_e_T = B_e.getT()
				
				for i in range(0,3):  #on met 3 car c'est un triangle
					for j in range(0,3):
						L.append(e[len(e)-3+i]-1) #pour acceder aux dernieres valeurs
						C.append(e[len(e)-3+j]-1) #pour acceder aux dernieres valeurs
						Matrix.append(float(-det_e/2*Dphi[j].T*B_e_T*B_e*Dphi[i]))

		#conversion en array
		L = np.array(L)
		C = np.array(C)
		Matrix = np.array(Matrix)

		Matrix = sparse.coo_matrix((Matrix,(L,C)),shape=(self.Nombre_Nodes,self.Nombre_Nodes)) 
		Matrix = Matrix.tocsr()

		ecriture = Ecriture("Matrice_rigidite.csv")
		ecriture.ecriture(Matrix.toarray())

		return Matrix

	def A_dirichlet(self,Masse,Rigidite):  # A = M + D 
		#il faut appliquer les conditions de dirichlet sur A 
		A = (Masse+Rigidite).toarray()

		for e in self.Elements: 
			if(e[1]==1 and e[3]==2): #bord intérieur
				for i in range(0,2):
					#sur toutes les lignes 0 
					A[e[len(e)-3+i]-1,:] = 0 
					#sur la diagonale on met 1 
					A[e[len(e)-3+i]-1,e[len(e)-3+i]-1] = 1

		ecriture = Ecriture("A_dirichlet.csv")
		ecriture.ecriture(A)

		return A

	def calcul_membre_droite(self):
		"""
		Dirichlet. A considérer = u = -u_inc
		"""  
		#il faut appliquer les conditions de dirichlet sur b (: u + u_inc)
		second_membre = [0]*self.Nombre_Nodes #pour mettre à la bonne taille		

		#Dirichlet : segment 
		for e in self.Elements: 
			if(e[1]==1 and e[3]==2): #alors il s'agit d'un segment et on est sur le bord intérieur
				p1 = e[len(e)-2] #on a que deux points 
				p2 = e[len(e)-1]

				s1 = self.Nodes[p1-1] #sommet pour le triangle e 
				s2 = self.Nodes[p2-1] 

				second_membre[p1-1] = -self.u_inc(s1)
				second_membre[p2-1] = -self.u_inc(s2)

		#pour mettre sous forme array 
		second_membre = np.array(second_membre)
		ecriture = Ecriture("calcul_membre_droite.csv")
		ecriture.ecriture(second_membre)

		return second_membre

	def resolution_systeme(self,A,membre_droite): 

		x = np.linalg.solve(A,membre_droite)
		j = 1
		for i in range(self.Nombre_Nodes): 
			point = self.Nodes[i]
			x1 = point[1]
			x2 = point[2]
			x3 = point[3]
			array = [0,x1,x2]

			x[i] = np.abs(x[i]+self.u_inc(array)) #car on veut observer u + u_inc et uniquement la partie réelle

		ecriture = Ecriture("resolution_systeme.csv")
		ecriture.ecriture(x)
		return x

