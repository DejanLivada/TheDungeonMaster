import pickle
from pygame.math import Vector2
import pygame.key


class Player:
    def __init__(self, name, health, slika, pozicija: Vector2, brzina_kretanja: Vector2):
        self.slika: pygame.Surface = slika
        self.smer = "DESNO"
        self.name = name
        self.health = health
        self.pozicija = pozicija
        self.brzina_kretanja = brzina_kretanja
        self.vertikalna_brzina = 0

    def touching_walls(self):
        if self.pozicija.x >= 700:
            self.pozicija.x = 700
        if self.pozicija.x <= 0:
            self.pozicija.x = 0
        if self.pozicija.y >= 500:
            self.pozicija.y = 500
        if self.pozicija.y <= 0:
            self.pozicija.y = 0

    def on_the_floor(self, platforms) -> bool:
        x, y = self.slika.get_rect().move(self.pozicija).midbottom
        if y >= 600:
            return True

        for pl in platforms:
            if pl.rect.collidepoint(x, y):
                return True


        return False

    def update(self, platforms):

        dugmici = pygame.key.get_pressed()

        if not self.on_the_floor(platforms):
            #print("U VAZDUHU")
            self.vertikalna_brzina += 0.3
        else:
            #print("NA PODU")
            self.vertikalna_brzina = 0
            if dugmici[pygame.K_w]:
                self.vertikalna_brzina = -10

        self.pozicija.y += self.vertikalna_brzina

        if dugmici[pygame.K_a]:
            self.pozicija.x -= self.brzina_kretanja.x
            if self.smer == "DESNO":
                self.smer = "LEVO"
                self.slika = pygame.transform.flip(self.slika, True, False)
        if dugmici[pygame.K_d]:
            self.pozicija.x += self.brzina_kretanja.x
            if self.smer == "LEVO":
                self.smer = "DESNO"
                self.slika = pygame.transform.flip(self.slika, True, False)
        self.touching_walls()


player_izabrana_slika = None
