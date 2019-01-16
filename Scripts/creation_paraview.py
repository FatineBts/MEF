#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

import numpy

class Creation_paraview: 
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements

	def script_paraview(self):
		fichier = open('paraview.vtu','w') 
		
		fichier.write('<VTKFile type="UnstructuredGrid" version="1.0" byte_order="LittleEndian" header_type="UInt64">\n')
		fichier.write('<UnstructuredGrid>\n')
		fichier.write('<Piece NumberOfPoints="'+str(self.Nombre_Nodes)+ '" NumberOfCells= "' + str(self.Nombre_Elements) + '">\n')
		fichier.write('<Points>\n')
		fichier.write('<DataArray NumberOfComponents="'+str(3)+'" type="Float64">\n')
		#0.0 0.0 0 
		#1.0 0.0 0 
		#1.0 1.0 0 
		#0.0 1.0 0 
		#0.5 0.5 0 
		fichier.write('</DataArray>\n')
		fichier.write('</Points>\n')
		fichier.write('<Cells>\n')
		fichier.write('<DataArray type="Int32" Name="connectivity">\n')
		#0 1 4
		#1 2 4
		#2 3 4
		#3 0 4
		fichier.write('</DataArray>\n')
		fichier.write('<DataArray type="Int32" Name="offsets">\n')
		#3
		#6
		#9
		#12
		fichier.write('</DataArray>\n')
		fichier.write('<DataArray type="UInt8" Name="types">\n')
		#5 
		#5 
		#5 
		#5 
		fichier.write('</DataArray>\n')
		fichier.write('<Cells>\n')
		fichier.write('<PointData Scalars="solution">\n')
		fichier.write('<DataArray type="Float64" Name="Real part" format="ascii">\n')
		#1.0
		#0.9999949269133752
		#0.9999949269133752
		#1.0
		#-0.9999987317275395
		fichier.write('</DataArray>\n')
		fichier.write('<DataArray type="Float64" Name="Imag part" format="ascii">\n')
		#0.0
		#-0.0031853017931379904
		#-0.0031853017931379904
		#0.0
		#0.0015926529164868282
		fichier.write('</DataArray>\n')
		fichier.write('</PointData>\n')
		fichier.write('</Piece>\n')
		fichier.write('</UnstructuredGrid>\n')
		fichier.write('</VTKFile>\n')

		fichier.close