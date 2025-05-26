import pygame
import random
import math

# --- Stałe ---
ROZMIAR_OKNA = 800
PROMIEN_OBIEKTU = 20
PREDKOSC_GRACZA = 5
PREDKOSC_WROGA = 1

# --- Funkcja sprawdzająca kolizje ---
def czy_mozna_ruszyc(obiekt_ruszajacy, przeszkody):
    for przeszkoda in przeszkody:
        dystans = math.hypot(obiekt_ruszajacy.x - przeszkoda.x, obiekt_ruszajacy.y - przeszkoda.y)
        if dystans < 2 * PROMIEN_OBIEKTU:
            return False
    return True

# --- Klasy gry ---
class Gracz:
    def __init__(self, x, y, kolor):
        self.x = x
        self.y = y
        self.kolor = kolor

    def rusz_sie(self, kierunek, przeszkody):
        stary_x, stary_y = self.x, self.y
        if kierunek == 'gora':
            self.y -= PREDKOSC_GRACZA
        elif kierunek == 'dol':
            self.y += PREDKOSC_GRACZA
        elif kierunek == 'lewo':
            self.x -= PREDKOSC_GRACZA
        elif kierunek == 'prawo':
            self.x += PREDKOSC_GRACZA
        
        if not czy_mozna_ruszyc(self, przeszkody):
            self.x, self.y = stary_x, stary_y

    def rysuj(self, okno):
        pygame.draw.circle(okno, self.kolor, (int(self.x), int(self.y)), PROMIEN_OBIEKTU)

class Przeszkoda:
    def __init__(self, x, y, kolor):
        self.x = x
        self.y = y
        self.kolor = kolor

    def rysuj(self, okno):
        pygame.draw.circle(okno, self.kolor, (int(self.x), int(self.y)), PROMIEN_OBIEKTU)

class Wrog:
    def __init__(self, x, y, kolor):
        self.x = float(x)
        self.y = float(y)
        self.kolor = kolor

    def rusz_sie(self, przeszkody):
        kat = random.uniform(0, 2 * math.pi)
        stary_x, stary_y = self.x, self.y
        self.x += PREDKOSC_WROGA * math.cos(kat)
        self.y += PREDKOSC_WROGA * math.sin(kat)

        if not czy_mozna_ruszyc(self, przeszkody):
            self.x, self.y = stary_x, stary_y

    def rysuj(self, okno):
        pygame.draw.circle(okno, self.kolor, (int(self.x), int(self.y)), PROMIEN_OBIEKTU)

# --- Inicjalizacja ---
pygame.init()
okno = pygame.display.set_mode((ROZMIAR_OKNA, ROZMIAR_OKNA))
pygame.display.set_caption("Prosta Gra")

# --- Tworzenie obiektów ---
gracz = Gracz(100, 100, (0, 255, 0))
wrog = Wrog(700, 700, (255, 0, 0))
przeszkody = [
    Przeszkoda(300, 300, (0, 0, 255)),
    Przeszkoda(400, 400, (0, 0, 255)),
    Przeszkoda(500, 200, (0, 0, 255))
]

zegar = pygame.time.Clock()
uruchomiona = True

# --- Pętla gry ---
while uruchomiona:
    zegar.tick(60)

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiona = False

    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_w]:
        gracz.rusz_sie('gora', przeszkody)
    if klawisze[pygame.K_s]:
        gracz.rusz_sie('dol', przeszkody)
    if klawisze[pygame.K_a]:
        gracz.rusz_sie('lewo', przeszkody)
    if klawisze[pygame.K_d]:
        gracz.rusz_sie('prawo', przeszkody)

    wrog.rusz_sie(przeszkody)

    # Sprawdzenie kolizji gracza z wrogiem
    if math.hypot(gracz.x - wrog.x, gracz.y - wrog.y) < 2 * PROMIEN_OBIEKTU:
        print("Koniec gry: wróg złapał gracza!")
        uruchomiona = False

    okno.fill((255, 255, 255))
    gracz.rysuj(okno)
    wrog.rysuj(okno)
    for przeszkoda in przeszkody:
        przeszkoda.rysuj(okno)
    pygame.display.flip()

pygame.quit()
