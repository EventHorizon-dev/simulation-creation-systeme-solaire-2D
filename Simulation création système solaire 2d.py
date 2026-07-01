import math
import random
import pygame
import sys


class Particule:
    def __init__(self,x,y,vx,vy,masse):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.masse=masse
        self.rayon=(masse)**(1/3)

    def deplacer(self,ax,ay,dt):
        self.vx+=ax*dt
        self.vy+=ay*dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt

def generer_nebuleuse(nb_particules):
    particules=[]
    #le centre de l'écran
    centre_x=400
    centre_y=400
    soleil = Particule(centre_x, centre_y, 0, 0, 50000)
    particules.append(soleil)



    for i in range(nb_particules):
        #On choisit un angle au hasard entre 0 et 2*pi (un cercle complet)
        angle=random.uniform(0,2*math.pi)
        #On choisit une distance (rayon) au hasard par rapport au centre
        R=random.uniform(50,300)
        #On choisit une petite masse au hasard pour notre poussière
        if random.random() < 0.1:
            masse = random.uniform(20, 50)  # Un gros astéroïde
        else:
            masse = random.uniform(1, 5)
        #position de x et y par rapport au centre
        x=centre_x+R*math.cos(angle)
        y=centre_y+R*math.sin(angle)

        v_orbitale=math.sqrt((G * 50000) / R)
        vx = -v_orbitale * math.sin(angle)
        vy = v_orbitale * math.cos(angle)
        facteur_chaos = random.uniform(0.85, 1.15)
        vx *= facteur_chaos
        vy *= facteur_chaos


        nouvelle_poussiere = Particule(x, y, vx, vy, masse)
        particules.append(nouvelle_poussiere)

    return particules

def mettre_a_jour_simulation(particules, dt, G):
    for p_actuelle in particules:  # On prend une particule (la cible)
        if p_actuelle.masse <= 0:
            continue
        force_totale_x = 0
        force_totale_y = 0
        for p_autre in particules:  # On regarde toutes les autres (les voisines)
            if p_actuelle == p_autre:
                continue  # L'ordinateur ignore tout ce qui est en dessous et passe directement à la particule suivante
            dx = p_autre.x - p_actuelle.x
            dy = p_autre.y - p_actuelle.y
            taille_combinee = p_actuelle.rayon + p_autre.rayon
            if abs(dx) > taille_combinee or abs(dy) > taille_combinee:
                if p_actuelle.masse < 50000 and p_autre.masse < 50000:
                    continue
            distance = math.sqrt(dx ** 2 + dy ** 2)#distance par l'hypothénuse

            if distance <= (p_actuelle.rayon + p_autre.rayon):
                if p_actuelle.masse >= p_autre.masse and p_autre.masse > 0:
                    m_totale = p_actuelle.masse + p_autre.masse
                    # Conservation de la quantité de mouvement (vitesse)
                    p_actuelle.vx = (p_actuelle.masse * p_actuelle.vx + p_autre.masse * p_autre.vx) / m_totale
                    p_actuelle.vy = (p_actuelle.masse * p_actuelle.vy + p_autre.masse * p_autre.vy) / m_totale

                    p_actuelle.masse = m_totale
                    p_actuelle.rayon = (p_actuelle.masse) ** (1 / 3) * 1.5
                    p_autre.masse = 0
                    continue




            #On calcule la force de gravitation qui s'applique sur nos particules grâce à la formule de Newton
            force=G*(p_actuelle.masse*p_autre.masse)/(distance**2)
            force_x = force * (dx / distance)
            force_y = force * (dy / distance)

            force_totale_x += force_x
            force_totale_y += force_y

        #On applique la formule de Newton pour que la force donne l'accélération à nos particules dans les deux axes
        if p_actuelle.masse >= 50000:
            ax = 0
            ay = 0
        else:
            ax = force_totale_x / p_actuelle.masse
            ay = force_totale_y / p_actuelle.masse
        p_actuelle.deplacer(ax,ay,dt)
    particules[:] = [p for p in particules if p.masse > 0 and -200 < p.x < 1000 and -200 < p.y < 1000]

pygame.init()
LARGEUR, HAUTEUR = 800, 800
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Simulation de Système Solaire")
horloge = pygame.time.Clock()
G = 2.0
particules = generer_nebuleuse(3000)
en_cours = True

while en_cours:
    dt = horloge.tick(60) / 1000.0
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                en_cours = False

    mettre_a_jour_simulation(particules, dt, G)
    ecran.fill((0, 0, 0))

    for p in particules:
        x_pixel = int(p.x)
        y_pixel = int(p.y)
        if p.masse >= 50000:
            couleur = (255, 255, 230)
        elif p.masse > 100:
            couleur = (255, 120, 30)
        elif p.masse > 10:
            couleur = (100, 180, 255)
        else:
            couleur = (80, 80, 180)

        pygame.draw.circle(ecran, couleur, (x_pixel, y_pixel), int(p.rayon))
    pygame.display.flip()

pygame.quit()
sys.exit()