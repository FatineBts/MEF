#fonction de lecture de fichier .msh
import numpy as ny


def lecture_fichier_msh(fichier) : 
	f = open(fichier, "r")
	print f.readlines()
	return f 

fichier = lecture_fichier_msh("submarine.msh")
fichier.close()