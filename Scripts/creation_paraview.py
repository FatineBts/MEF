#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#Polytech Sorbonne - année 2018/2019
#Réalisé par : Fatine Bentires Alj et Alexia Zounias-Sirabella
#Cours de maillage des éléments finis de Bertrand Thierry
##################################################################

class Creation_paraview: 
	def __init__(self,Nombre_lignes, Nombre_Nodes,Nodes, Nombre_Elements,Elements):
		self.Nombre_lignes = Nombre_lignes 
		self.Nombre_Nodes = Nombre_Nodes
		self.Nodes = Nodes
		self.Elements = Elements
		self.Nombre_Elements = Nombre_Elements

	def script_paraview(self): 
		<VTKFile type="UnstructuredGrid" version="1.0" byte_order="LittleEndian" header_type="UInt64">
		<UnstructuredGrid>
		<Piece NumberOfPoints=self.Nombre_Nodes NumberOfCells=self.Nombre_Elements>
		<Points>
		<DataArray NumberOfComponents="3" type="Float64">
		0.0 0.0 0 
		1.0 0.0 0 
		1.0 1.0 0 
		0.0 1.0 0 
		0.5 0.5 0 
		</DataArray>
		</Points>
		<Cells>
		<DataArray type="Int32" Name="connectivity">
		0 1 4
		1 2 4
		2 3 4
		3 0 4
		</DataArray>
		<DataArray type="Int32" Name="offsets">
		3
		6
		9
		12
		</DataArray>
		<DataArray type="UInt8" Name="types">
		5 
		5 
		5 
		5 
		</DataArray>
		</Cells>
		<PointData Scalars="solution">
		<DataArray type="Float64" Name="Real part" format="ascii">
		1.0
		0.9999949269133752
		0.9999949269133752
		1.0
		-0.9999987317275395
		</DataArray>
		<DataArray type="Float64" Name="Imag part" format="ascii">
		0.0
		-0.0031853017931379904
		-0.0031853017931379904
		0.0
		0.0015926529164868282
		</DataArray>
		</PointData>
		</Piece>
		</UnstructuredGrid>
		</VTKFile>