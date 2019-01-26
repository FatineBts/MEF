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
  1) gmsh Maillage/sousmarin_simple.geo -2 #pour produire le maillage dans le dossier Maillage 
  OU placer votre maillage directement dans le dossier Maillage si vous l'avez déjà
  2) python main.py sousmarin_simple.msh #pour lancer le fichier sousmarin_simple.msh 
  3) paraview paraview.vtu #pour visualiser le résultat sous paraview
  OU ouvrir l'application paraview, charger le fichier puis appuyer sur apply

  Fichiers/Dossiers :
  - Fichier main.py : fichier qui va lancer tous les autres 
  - Fichier Maillage/sousmarin_simple.geo : donne la représentation d'un sous-marin simplifié, visualisable avec gmsh
  - Fichier Maillage/sousmarin_simple.msh : maillage du fichier précédent 
  - Dossier Script : contient les fichiers Python
  - Dossier CSV : contient les fichiers csv correspondants aux matrices et au second membre 
  - Dossier Images : contient des visualisations du résultat 
  
  Résultat obtenu avec un nombre d'onde k : 20 et alpha : 0

![apres_u_uinc_resolution_k_20](https://user-images.githubusercontent.com/23095219/51789632-194a9600-218b-11e9-9f2b-9f411ee0446a.png)
