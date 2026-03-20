import pygame
import random

longueur=800
largeur=600
taille_case=20
fps = 10

def initialiser_pygame():
    pygame.init()
    fenetre=pygame.display.set_mode((longueur,largeur))
    pygame.display.set_caption("SNAKE GAME")
    return fenetre 

def initialiser_jeu():
    serpent=[(100,100), (80,100), (60,100)]
    nourriture = generer_nourriture(longueur,largeur,taille_case,serpent)
    score = 0
    direction = (taille_case,0)
    return serpent , score ,nourriture ,direction 

def deplacer_serpent(serpent,direction):
    nouvelle_tete = (serpent[0][0] + direction[0],serpent[0][1]+ direction[1])
    serpent.insert(0, nouvelle_tete)
    serpent.pop()

def collusion_serpent(serpent):
    return serpent[0] in serpent[1:]

def collusion_murs(serpent,longueur,largeur):
    x , y = serpent[0]
    return x < 0 or x >=longueur  or y < 0 or y >=largeur 

def generer_nourriture(longeur,largeur,taille_case,serpent):
    while True :
        x = random.randrange (0,longeur,taille_case)
        y = random.randrange (0,largeur,taille_case)
        if (x,y) not in serpent :
            return (x,y)
    
def manger_nourriture(serpent,nourriture):
    return serpent[0] == nourriture

def gerer_clavier (event,direction):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and direction != (0,taille_case):#bas
            return (0,-taille_case)#haut
        elif event.key == pygame.K_DOWN and direction != (0,-taille_case):#haut
            return (0,taille_case)#bas
        elif event.key == pygame.K_LEFT and direction != (taille_case ,0):#droite
            return (-taille_case,0)#gauche
        elif event.key == pygame.K_RIGHT and direction != (-taille_case,0):#gauche
            return (taille_case ,0)#droite
    return direction 

def afficher_serpent(fenetre,serpent):
    for segment in serpent :
        pygame.draw.rect(fenetre,("green"),(*segment,taille_case,taille_case))

def afficher_nourriture(fenetre,nourriture):
    pygame.draw.rect(fenetre,("red"),(*nourriture,taille_case,taille_case))

def afficher_score(fenetre,score):
    position_texte=(10,10)
    police=pygame.font.Font(None,36)
    texte=police.render(f"score : {score}",True,"white")
    fenetre.blit(texte,position_texte)

def afficher_game_over(fenetre,score):
    fenetre.fill("black")
    police_titre=pygame.font.SysFont(None,72)
    police_score = pygame.font.Font(None, 36)
    police_rejouer = pygame.font.Font(None, 30)
    texte=police_titre.render("Game Over" ,True ,"red")
    texte_score = police_score.render(f"Score final : {score}", True, "white")
    texte_rejouer = police_rejouer.render("Appuyez sur R pour rejouer  ou Q pour quitter", True, "gray")

    fenetre.blit(texte, texte.get_rect(center=(longueur // 2, largeur // 2 - 60)))
    fenetre.blit(texte_score, texte_score.get_rect(center=(longueur // 2, largeur // 2)))
    fenetre.blit(texte_rejouer, texte_rejouer.get_rect(center=(longueur // 2, largeur // 2 + 60)))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False       # Quitter le programme
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True    # Rejouer
                if event.key == pygame.K_q:
                    return False   # Quitter

def boucle_principale():
    fenetre= initialiser_pygame()
    clock = pygame.time.Clock()
    serpent , score ,nourriture,direction =initialiser_jeu()
    running = True

    while running ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            else :
                direction = gerer_clavier(event,direction)
        deplacer_serpent(serpent,direction)
    
        if collusion_serpent(serpent) or collusion_murs(serpent, longueur, largeur):
            rejouer = afficher_game_over(fenetre, score)
            if rejouer:
                serpent, score, nourriture, direction = initialiser_jeu()
            else:
                running = False
            continue 

        if manger_nourriture (serpent,nourriture):
            score=score+1
            nourriture=generer_nourriture(longueur,largeur,taille_case ,serpent)
            serpent.append(serpent[-1])
    
        fenetre.fill("black")
        afficher_serpent(fenetre,serpent)
        afficher_nourriture(fenetre,nourriture)
        afficher_score(fenetre,score)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit() 

boucle_principale()
