import pygame
from pygame.locals import *
import time
from random import *

from classes import *
from constantes import *

pygame.init()

#DEFINITIONS BENJAMIN
def score(compte) :
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("score : " + str(compte), True, white)
    surface.blit(texte, [10,0])

def nuages(x_nuage, y_nuage, espace):
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage+ nuageH +espace))


def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYUP:
            continue
        return event.key

    return  None

def creaTexteObjs (texte, font):
    texteSurface = font.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()


def msgSurface (texte):
    GOTexte = pygame.font.Font('BradBunR.ttf', 150)
    petitTexte = pygame.font.Font('BradBunR.ttf',20)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = surfaceW/2,((surfaceH/2)-50)
    surface.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs\
        ("appuyer sur une touche pour continuer", petitTexte )
    petitTexteRect.center = surfaceW/2, ((surfaceH/2) +50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while rejoueOuQuitte() == None :
        clock.tick()

    main()

def gameOver():
    msgSurface("Oops... Tu as perdu!")

def heros(x,y, image):
    surface.blit(image, (x,y))

def main():
    x=150
    y=200
    y_move=0

    x_nuage = surfaceW
    y_nuage = randint(-300,10)
    espace = herosH*3
    nuage_vitesse = 6

    score_actuel = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -1
            if event.type ==pygame.KEYUP :
                y_move = 1

        y += y_move

        surface.fill(blue)
        heros(x,y,img)

        nuages(x_nuage,y_nuage, espace)

        score(score_actuel)

        x_nuage -=nuage_vitesse


        if y>surfaceH -40 or y <-10:
            gameOver()

        if x_nuage < (-1*nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-300,10)

            if 3 <= score_actuel < 5:
                nuage_vitesse = 7
                espace = herosH*2.8
            if 5 <= score_actuel < 7 :
                nuage_vitesse = 8
                espace = herosH*2.7
            if 7 <= score_actuel < 10 :
                nuage_vitesse = 9
                espace = herosH*2.5
            if 10 <= score_actuel <22:
                nuage_vitesse = 11
                espace = herosH*2.2
            if 22 <= score_actuel:
                nuage_vitesse = 13
                espace = herosH*2



        if x +herosW > x_nuage + 40 :
            if y < y_nuage + nuageH  -50:
                if x - herosW < x_nuage +nuageW -20 :
                    
                    gameOver()

        if x +herosW >x_nuage + 40 :
            if y +herosH > y_nuage + nuageH + espace +50 :
                if x -herosW < x_nuage+ nuageW - 20:
                    
                    gameOver()

        if x_nuage < (x-nuageW)<x_nuage+nuage_vitesse :
            score_actuel +=1

        pygame.display.update()

              


#DEFINITIONS DE WILLEM
#Définition de l'écran d'aide
def help():
  help = pygame.image.load("img/morp/help.png").convert() #Charger l'image
  fenetre.blit(help, (0,0)) #recharger l'image
  pygame.display.flip() #rafraîchir
  while morp:
    for event in pygame.event.get():
      if event.type==KEYDOWN: #sortir de l'aide lorsque l'on clique sur une touche
        initialisation()
      elif event.type==MOUSEBUTTONDOWN:#Sortir de l'aide lorsque l'on clique sur le clique gauche de la souris
        if event.button == 1:
          initialisation()

def gagnant(b):#Définition permettant de définir le gagnant
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
#Lancement du jeu
def initialisation():
  depart = pygame.image.load("img/morp/depart.png").convert()
  fenetre.blit(depart, (0,0))
  pygame.display.flip()
#Lancement de l'écrant d'aide
  while morp:
    for event in pygame.event.get():
      if event.type==MOUSEBUTTONDOWN:#Lancer l'aide lorsque l'on clique sur le cliqe gauche de la souris
        if event.button == 1:
          if 488<event.pos[1]:
            help()
      if event.type==KEYDOWN: #Lancer le jeu lorsque l'on clique sur une touche
        morpion()

#Définition du programme du morpion
def morpion():
  fond = pygame.image.load("img/morp/plateau2.png").convert() 
  fenetre.blit(fond, (0,0))
  tcroix = pygame.image.load("img/morp/tcroix.png").convert()
  fenetre.blit(tcroix, (580,542))
  pygame.display.flip()
  background=[0,0,0,0,0,0,0,0,0] #Donnée des valeur au case
  croix=1 #Donnée des valeur au croix
  rond=2 #Donnée des valeur au rond
  player=croix
  case=-1
  while True:
    utilisateur=True
    while utilisateur:
      for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN: #Déterminer la position de la souris
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
        if event.type==KEYDOWN: #Déterminer les valeur des touches numériques 
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
    if background[case]==0: #Définire les position des cases, cad la zone de "portée" du clique
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
        croix = pygame.image.load("img/morp/croix.png").convert()
        fenetre.blit(croix, case)
        pygame.display.flip()
        player=2
        case=-1
        g=gagnant(background) #Appelle de la fonction "gagnant"
        if g==1:
          gcroix = pygame.image.load("img/morp/gcroix.png").convert()
          fenetre.blit(gcroix, (200,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("img/morp/menu.png").convert()
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
          egalite = pygame.image.load("img/morp/egalite.png").convert()
          fenetre.blit(egalite, (230,542))
          blanc = pygame.image.load("img/morp/blanc.png").convert()
          fenetre.blit(blanc, (580,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("img/morp/menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()
          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  initialisation()
                if event.key == K_KP1:
                  morpion()
        trond = pygame.image.load("img/morp/trond.png").convert()
        fenetre.blit(trond, (580,542))
        pygame.display.flip()
      else:
        rond = pygame.image.load("img/morp/rond.png").convert()
        fenetre.blit(rond, case)
        player=1
        pygame.display.flip()
        case=-1
        g=gagnant(background)
#le cas g==1 ne peut pas arriver car l'on vient de jouer un rond
        if g==2:
          grond = pygame.image.load("img/morp/grond.png").convert()
          fenetre.blit(grond, (200,542))
          pygame.display.flip()
          time.sleep(1.5)
          menu = pygame.image.load("img/morp/menu.png").convert()
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
        tcroix = pygame.image.load("img/morp/tcroix.png").convert()
        fenetre.blit(tcroix, (580,542))
        pygame.display.flip()


#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = True
while continuer:
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))
    #Rafraichissement
    pygame.display.flip()
    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = True
    continuer_accueil = True
     
    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        
       
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        #Variable de choix du jeu
        choix=0

        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = False
                continuer_jeu = False
                continuer = False
                pygame.quit()
                quit()
            
            elif event.type == KEYDOWN:
                #Lancement du labyrinthe
                if event.key == K_l:
                    continuer_accueil = False   #On quitte l'accueil
                    choix = 1        #On définit le niveau à charger

                #Lancement du Jump it
                elif event.key == K_j:
                    continuer_accueil = False
                    choix = 2
                #Lancement du Morpion
                elif event.key == K_m:
                    continuer_accueil = False
                    choix = 3

        
        #lancement du Labyrinhte
        if choix == 1:
            n=nb_aleatoire(1, 3)
            print (n)
            if n==1:
             lv="1"
            elif n==2:
             lv="2"
            elif n==3:
             lv="3"
            #Chargement du fond-
            fond = pygame.image.load(image_fond).convert()
            #Génération d'un niveau à partir d'un fichier
            niveau = Niveau(lv)
            niveau.generer()
            niveau.afficher(fenetre)
            #Création de Donkey Kong
            heros = Perso("img/lab/heros droite.gif", "img/lab/heros gauche.gif","img/lab/heros haut.gif", "img/lab/heros bas.gif", niveau)

            #boucle du Labyrinthe
            while continuer_jeu:
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                    #si l'utilisateur quite, on met la variable qui continue le jeu
                    #Et la variable générame à 0 pour fermer la fenêtre
                    if event.type == QUIT:
                        continuer_jeu = False
                        continuer = False
                        pygame.quit()
                        quit()
                    elif event.type ==KEYDOWN:
                        #si l'utilisateur presse Echap ici,on revient seulement au menu
                        if event.key ==K_ESCAPE:
                            continuer_jeu = False
                        #touche de déplacement du héros
                        elif event.key ==K_RIGHT:
                            heros.deplacer('droite')
                        elif event.key ==K_LEFT:
                            heros.deplacer('gauche')
                        elif event.key ==K_UP:
                            heros.deplacer('haut')
                        elif event.key ==K_DOWN:
                            heros.deplacer('bas')

                        #Affichages aux nouvelles positions
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(heros.direction, (heros.x, heros.y))
                        #heros.direction = l'image dans la bonne direction
                        pygame.display.flip()
                        #Victoire -> Retour à l'accueil
                        if niveau.structure[heros.case_y][heros.case_x] == 'a':
                            w=0
                            #enigmes
                            e=nb_aleatoire(1,5)#création d'une variable aléatoire pour piocher une des énigmes
                            if e==1:
                                enigme=int(input("combien font 78*12?")) #on demande la reponse du joeur
                                if enigme==936: #si il a bon
                                    print("bravo à toi,tu as trouvé!")
                                    w=1
                                else :  #si il a faux
                                    print("FAUX")
                                    coninuer_jeu=False #on quite le labyrinthe
                                    pygame.display.flip()#on rafraichit

                            if e==2:
                                enigme=int(input("quelle est la racine carrée de 28 224?"))
                                if enigme==168:
                                       print("bravo à toi,tu as trouvé!")
                                       w=1
                                else :
                                       print("FAUX")
                                       continuer_jeu=False
                                       pygame.display.flip()

                            if e==3:
                                enigme=int(input("Soit x un nombre entier, si 4x-12=0 combien vaut x?"))
                                if enigme==3:
                                    print("bravo à toi,tu as trouvé!")
                                    w=1
                                else :
                                    print("FAUX")
                                    continuer_jeu=False
                                    pygame.display.flip()

                            if e==4:
                                enigme=str(input("Quel atome a le moins d'électrons? PS:ecrire sans accent"))
                                if enigme=="hydrogene":
                                    print("bravo à toi,tu as trouvé!")
                                    w=1
                                else :
                                    print("FAUX")
                                    continuer_jeu=False
                                    pygame.display.flip()

                            if e==5:
                                enigme=str(input("Comment se nomme la réaction chimique qui permet aux plante de créer de l'oxigène et des nutriments en échange de l'énergie solaire? PS:ecrire sans accents"))
                                if enigme=="photosynthese":
                                    print("bravo à toi,tu as trouvé!")
                                    w=1
                                else :
                                    print("FAUX")
                                    continuer_jeu=False
                                    pygame.display.flip()
                           
                            if w==1:
                                continuer_win=True                             
                                print("appuiez sur echap pour revenir au menu principal")
                                while continuer_win:
                                    win = pygame.image.load(image_win).convert() #affichage du message de victoire en image
                                    fenetre.blit(win, (0,0))
                                    for event in pygame.event.get():
                                        if event.type ==KEYDOWN and event.key ==K_ESCAPE: #si on apuit sur ECHAP on revient a l'accueil
                                            continuer_win=False
                                            continuer_jeu=False


        #lancement jump it
        elif choix==2:
            jump=True
            while jump:
                blue = (113,177,227) #valeur max =255.
                white = (255,255,255)

                pygame.init()

                surfaceW = 1200
                surfaceH = 800
                herosW = 45
                herosH = 45
                nuageW = 300
                nuageH = 300


                surface = pygame.display.set_mode((surfaceW,surfaceH))
                pygame.display.set_caption("jump it")
                clock = pygame.time.Clock()


                img = pygame.image.load('img/jump/heros.png')
                img_nuage01 = pygame.image.load('img/jump/NuageHaut.png')
                img_nuage02 = pygame.image.load('img/jump/NuageBas.png')

                main()
                pygame.quit()
                quit()
            
        
        #lancement morpion        
        elif choix==3:
            fenetre = pygame.display.set_mode((648,604), RESIZABLE)
            depart = pygame.image.load("img/morp/depart.png").convert()
            fenetre.blit(depart, (0,0))
            pygame.display.flip()
            morp=True
            initialisation()

               












