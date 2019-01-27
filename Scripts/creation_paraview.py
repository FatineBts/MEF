#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

#documentation : https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf

import numpy as np
from matrices import *

class Creation_paraview: 
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements,Resultat):
		M = Matrice(Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements, Elements)

		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements
		self.Nombre_Triangles = M.nombre_de_triangles() #on recupère le nombre de triangles
		self.Nombre_Segments = self.Nombre_Elements - self.Nombre_Triangles

		self.Resultat = Resultat

	def script_paraview(self):
		fichier = open('paraview.vtu','w') 
	
		fichier.write('<VTKFile type="UnstructuredGrid" version="1.0" byte_order="LittleEndian" header_type="UInt64">\n')
		fichier.write('<UnstructuredGrid>\n')
		fichier.write('<Piece NumberOfPoints="'+str(int(self.Nombre_Nodes))+ '" NumberOfCells= "' + str(self.Nombre_Triangles) + '">\n')
		fichier.write('<Points>\n')
		fichier.write('<DataArray NumberOfComponents="'+str(3)+'" type="Float64">\n') #nombre de colonnes
		################################ NumberOfComponents : Pour tous les points ############################
		#Explication : on recupère les coordonnées ainsi que le numéro de la ligne ie toute les lignes contenants les points
		for i in self.Nodes:  
				fichier.write(str(i[1]) + ' ')
				fichier.write(str(i[2]) + ' ')
				fichier.write(str(i[3]) + ' ')
				fichier.write('\n')
		fichier.write('</DataArray>\n')
		fichier.write('</Points>\n')
		fichier.write('<Cells>\n')

		fichier.write('<DataArray type="Int32" Name="connectivity">\n') 
		######## connectivity : Pour chaque element on prend les numéro des points qui le constitue  #############

		#pour les triangles 
		for k in self.Elements: 
			if(k[1]==2): #triangles
				fichier.write(str(k[len(k)-3]-1) + ' ') 
				fichier.write(str(k[len(k)-2]-1) + ' ')
				fichier.write(str(k[len(k)-1]-1) + ' ')
				fichier.write('\n')

		#pour les segments
		for k in self.Elements: 
			if(k[1]==1): #segments
				fichier.write(str(k[len(k)-2]-1) + ' ')
				fichier.write(str(k[len(k)-1]-1) + ' ')
				fichier.write('\n')

		fichier.write('</DataArray>\n')

		fichier.write('<DataArray type="Int32" Name="offsets">\n') 
		######## offsets : Récupération de la fin de position de chaque element dans la partie connectivity###########
		#Explication : on fait des pas de 3 pour les triangles et 2 pour les segments
		
		pas = 0
		for k in range(self.Nombre_Triangles): 
			fichier.write(str(pas+3) + '\n') 
			pas+=3

		pas = 0
		for k in range(self.Nombre_Segments): 
			fichier.write(str(pas+2) + '\n') 
			pas+=2

		fichier.write('</DataArray>\n')

		fichier.write('<DataArray type="UInt8" Name="types">\n') 

		########### types : On met les types des éléments ####################
		#Explication : Pour des triangles le type est 5. Pour les segments le type est 3. 

		for k in self.Elements:
			if(k[1]==2): #triangle
				fichier.write(str(5) + ' ' + '\n')

		for k in self.Elements:
			if(k[1]==1): 
				fichier.write(str(3) + ' ' + '\n')

		fichier.write('</DataArray>\n')
		fichier.write('</Cells>\n')
		fichier.write('<PointData Scalars="solution">\n')

		fichier.write('<DataArray type="Float64" Name="Real part" format="ascii">\n')

		########## real part : ##########
		#Explication : partie reelle des résultats obtenue par la fonction np.linalg.solve()

		for i in self.Resultat:
			fichier.write(str(np.real(i))+'\n')

		fichier.write('</DataArray>\n')

		fichier.write('<DataArray type="Float64" Name="Imag part" format="ascii">\n')
		
		########## im part : ############
		#Explication : partie imaginaire des résultats obtenue par la fonction np.linalg.solve()
		for i in self.Resultat: 
			fichier.write(str(np.imag(i))+'\n') 

		fichier.write('</DataArray>\n')
		fichier.write('</PointData>\n')
		fichier.write('</Piece>\n')
		fichier.write('</UnstructuredGrid>\n')
		fichier.write('</VTKFile>\n')

		fichier.close()