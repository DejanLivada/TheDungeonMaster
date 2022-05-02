import pygame
pygame.init()

dugme_font = pygame.font.SysFont('Consolas', 60)

class Dugme():
    def __init__(self , tekst , rect ,boja):
        self.tekst = tekst
        self.rect = rect
        self.boja = boja

main_menu_dugme_quit = Dugme(dugme_font.render("EXIT", True, (255, 255, 255)) , pygame.Rect(320, 465 , 150 ,60) , pygame.Color("black"))
main_menu_dugme_credits = Dugme(dugme_font.render("CREDITS", True, (255, 255, 255)) ,pygame.Rect(270, 300 , 245 ,60)  , pygame.Color("black"))
credits_to_main_menu_button = Dugme(dugme_font.render("BACK", True, (255, 255, 255)) ,pygame.Rect(22, 470 , 200 ,60)  , pygame.Color("black"))
main_menu_play_button = Dugme(dugme_font.render("PLAY", True, (255, 255, 255)) ,pygame.Rect(320, 180 , 150 ,60)  , pygame.Color("black"))