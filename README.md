            Projet réalisé dans le cadre du cours de Maillage des éléments finis encadré par Bertrand Thierry
   
  Enoncé : https://ljll.math.upmc.fr/bthierry/course/fem_tp/python_project/
  
  Modèle Mathématique : diffraction accoustique 
  
  Bibliothèques Python à avoir : 
  - scipy (https://www.scipy.org)
  - numpy (http://www.numpy.org)
  - math (https://docs.python.org/2/library/math.html)
  - Cmath (https://docs.python.org/2/library/cmath.html)
  - os (https://docs.python.org/fr/2.7/library/os.html)
  - sys (https://docs.python.org/fr/3/library/sys.html)
  
  Pour télécharger : 
  - gmsh : http://gmsh.info
  - Paraview : https://www.paraview.org

  Comment lancer le projet : (exemple avec sousmarin_simple.geo)
  1) gmsh Maillage/sousmarin_simple.geo -2 #pour produire le maillage 
  2) mv sous_marinsimple.msh Maillage #si le fichier produit n'est pas dans le dossier Maillage
  3) python main.py #pour lancer le projet 
  4) paraview paraview.vtu #pour visualiser le résultat sous paraview


  Fichiers : 
  - Fichier main.py : fichier qui va lancer tous les autres 
  
  Dossier Maillage : 
  - sousmarin_simple.geo : donne la représentation (figure 1 énoncé) du sous-marin, visualisable avec gmsh
  - sousmarin_simple.msh : maillage du sous-marin de la figure 1 
  - sousmarin.geo : donne la représentation avancée (figure 2 énoncé) du sous-marin, visualisable avec gmsh
  - sousmarin.msh : maillage du sous-marin de la figure 2 
  
  Dossier Script : contient les fichiers Python
  
  Dossier CSV : contient les fichiers csv correspondants aux matrices et au second membre 
  
![fig1](https://user-images.githubusercontent.com/23095219/50483647-97791880-09e4-11e9-97a7-15b73f5c5dc1.png)
![fig2](https://user-images.githubusercontent.com/23095219/50483645-96e08200-09e4-11e9-93b5-9447f223e7d8.png)
