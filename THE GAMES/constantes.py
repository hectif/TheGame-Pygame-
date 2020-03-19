"""constantes du jeu de Labyrinthe """
import pygame
from pygame.locals import *

pygame.init()


#parametres de la fenetre
nombre_sprite_cote = 15
taille_sprite =45
cote_fenetre = nombre_sprite_cote*taille_sprite

#Personnalisation de la fênetre
titre_fenetre = "THE GAMES"
image_icone ="img/lab/heros.png"

#image du menu
image_accueil = "img/lab/accueil.png"

#images du labyrinthe
image_fond = "img/lab/fond.png"
image_mur = "img/lab/mur.png"
image_depart = "img/lab/depart.png"
image_arrivee = "img/lab/arrivee.png"
image_win="img/lab/win.png"

#liste des sons du labyrinthe
nop = pygame.mixer.Sound("sons/nop.wav")


