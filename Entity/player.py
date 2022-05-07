import pickle
from pygame.math import Vector2
import pygame.key


class Player:
    def __init__(self , name , health , slika  ,pozicija: Vector2 , brzina : Vector2):
        self.slika = slika
        self.name = name
        self.health = health
        self.pozicija = pozicija
        self.brzina = brzina
    def move(self):
        dugmici = pygame.key.get_pressed()
        if dugmici[pygame.K_w]:
            self.pozicija.y -= self.brzina.y
        if dugmici[pygame.K_s]:
            self.pozicija.y += self.brzina.y
        if dugmici[pygame.K_a]:
            self.pozicija.x -= self.brzina.x
        if dugmici[pygame.K_d]:
            self.pozicija.x += self.brzina.x







player_izabrana_slika = None

