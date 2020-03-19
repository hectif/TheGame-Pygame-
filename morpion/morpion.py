#PALLIOT Willem
#Morpion inspiré, pas 100% personnel

#Import des bases
import time
import pygame
from pygame.locals import *


#Initialisation de pygame
pygame.init()
fenetre = pygame.display.set_mode((648,604), RESIZABLE)
depart = pygame.image.load("depart.png").convert()
fenetre.blit(depart, (0,0))
pygame.display.flip()

#Définition de l'écran d'aide
def help():
  help = pygame.image.load("help.png").convert()
  fenetre.blit(help, (0,0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type==KEYDOWN:
        initialisation()
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

#Lancement du jeu
def initialisation():
  depart = pygame.image.load("depart.png").convert()
  fenetre.blit(depart, (0,0))
  pygame.display.flip()
#Lancement de l'écrant d'aide
  while True:
    for event in pygame.event.get():
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          if 488<event.pos[1]:
            help()
      if event.type==KEYDOWN:
        morpion()

#Définition du programme du morpion
def morpion():
  fond = pygame.image.load("plateau2.png").convert()
  fenetre.blit(fond, (0,0))
  tcroix = pygame.image.load("tcroix.png").convert()
  fenetre.blit(tcroix, (580,542))
  pygame.display.flip()
  background=[0,0,0,0,0,0,0,0,0]
  croix=1
  rond=2
  player=croix
  case=-1
  while True:
    utilisateur=True
    while utilisateur:
      for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
          if event.button == 1:
            if 355<event.pos[1]<540:
              if 9<event.pos[0]<220:
                case=0
                utilisateur=False
              if 226<event.pos[0]<419:
                case=1
                utilisateur=False
              if 425<event.pos[0]<636:
                case=2
                utilisateur=False
            if 180<event.pos[1]<350:
              if 9<event.pos[0]<220:
                case=3
                utilisateur=False
              if 226<event.pos[0]<419:
                case=4
                utilisateur=False
              if 425<event.pos[0]<636:
                case=5
                utilisateur=False
            if 7<event.pos[1]<175:
              if 9<event.pos[0]<220:
                case=6
                utilisateur=False
              if 226<event.pos[0]<419:
                case=7
                utilisateur=False
              if 425<event.pos[0]<636:
                case=8
                utilisateur=False
        if event.type==KEYDOWN:
          if event.key == K_KP1:
            case=0
            utilisateur=False
          if event.key == K_KP2:
            case=1
            utilisateur=False
          if event.key == K_KP3:
            case=2
            utilisateur=False
          if event.key == K_KP4:
            case=3
            utilisateur=False
          if event.key == K_KP5:
            case=4
            utilisateur=False
          if event.key == K_KP6:
            case=5
            utilisateur=False
          if event.key == K_KP7:
            case=6
            utilisateur=False
          if event.key == K_KP8:
            case=7
            utilisateur=False
          if event.key == K_KP9:
            case=8
            utilisateur=False
    if background[case]==0:
      background[case]=player
      if case==0:
        case=(37,361)
      if case==1:
        case=(236,361)
      if case==2:
        case=(435,361)
      if case==3:
        case=(37,181)
      if case==4:
        case=(236,181)
      if case==5:
        case=(435,181)
      if case==6:
        case=(37,7)
      if case==7:
        case=(236,7)
      if case==8:
        case=(435,7)
      if player==1:
        croix = pygame.image.load("croix.png").convert()
        fenetre.blit(croix, case)
        pygame.display.flip()
        player=2
        case=-1
        g=gagnant(background)
        if g==1:
          gcroix = pygame.image.load("gcroix.png").convert()
          fenetre.blit(gcroix, (200,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()
          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  initialisation()
                if event.key == K_KP1:
                  morpion()
#le cas g==2 ne peut pas arriver car on vient de jouer une croix
        if g==3:
          egalite = pygame.image.load("egalite.png").convert()
          fenetre.blit(egalite, (230,542))
          blanc = pygame.image.load("blanc.png").convert()
          fenetre.blit(blanc, (580,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()
          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  initialisation()
                if event.key == K_KP1:
                  morpion()
        trond = pygame.image.load("trond.png").convert()
        fenetre.blit(trond, (580,542))
        pygame.display.flip()
      else:
        rond = pygame.image.load("rond.png").convert()
        fenetre.blit(rond, case)
        player=1
        pygame.display.flip()
        case=-1
        g=gagnant(background)
#le cas g==1 ne peut pas arriver car l'on vient de jouer un rond
        if g==2:
          grond = pygame.image.load("grond.png").convert()
          fenetre.blit(grond, (200,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()
          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  initialisation()
                if event.key == K_KP1:
                  morpion()
#le cas g==3 ne peut pas arriver car les croix commencent et terminent
        tcroix = pygame.image.load("tcroix.png").convert()
        fenetre.blit(tcroix, (580,542))
        pygame.display.flip()

def gagnant(b):
  if b[0]==b[1]==b[2] and b[0]!=0:
    l=b[0]
    return l
  if b[3]==b[4]==b[5] and b[3]!=0:
    l=b[3]
    return l
  if b[6]==b[7]==b[8] and b[6]!=0:
    l=b[6]
    return l
  if b[0]==b[3]==b[6] and b[0]!=0:
    l=b[0]
    return l
  if b[1]==b[4]==b[7] and b[1]!=0:
    l=b[1]
    return l
  if b[2]==b[5]==b[8] and b[2]!=0:
    l=b[2]
    return l
  if b[0]==b[4]==b[8] and b[4]!=0:
    l=b[4]
    return l
  if b[2]==b[4]==b[6] and b[4]!=0:
    l=b[4]
    return l
  if b[0]!=0 and b[1]!=0 and b[2]!=0 and b[3]!=0 and b[4]!=0 and b[5]!=0 and b[6]!=0 and b[7]!=0 and b[8]!=0:
    return 3
  return 0

initialisation()

