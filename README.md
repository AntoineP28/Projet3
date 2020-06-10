# *Projet3*

                                       ## Installation du jeu

                        Pour installer le jeu, il vous faudra cloner les fichiers. 
                                    Installation des requierments:

                                    - pip install -r requierments.txt
_____________________________________________________________________________________


                                    ## Fichier du  jeu                                   

Vous retrouverez alors le fichier principal goombalabyrinthe.py, il permet l'ouverture de la fenêtre de jeu, chargement de fond, création du personnage,  les touches directionnelles,  affiche des nouvelles positions, ainsi que la victoire et la défaite.

Fichier constantes.py: Vous pourrez retrouver les images enregistrés.

Dans le dossier images: il contient les images dont nous avons besoin pour le jeux.

Dans le dossier env: il contient l'environnement virtuel.

Dans le dossier data: il contient les map pour le jeu goombalabyrinthe.

Dans le dossier app: il contient le fichier images, il contient la class items, elle permet de mettre les objets à un endroit aléatoire de la map en fonction du niveau.
Il contient le fichier niveau, il contient la class niveau, elle permet de parcourir et de lire ligne par ligne la map, de charger les images et calculer la position réelle en pixels.
Il contient également le fichier perso, il contient la class perso, elle permet de définir les images directionnel de goomba, la position du personnage, le niveau dans lequel ce trouve le personnage, et ses déplacements gauche/droite/haut/bas.