import sys

import pygame

import Buttons
import credits_imena
from imports import *
pygame.init()
Xres = 800
Yres = 600
prozor = pygame.display.set_mode((Xres,Yres))
sat = pygame.time.Clock()
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect( prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)  # lepsi nacin od linije dole, TOPLEFT je pozicija gornje leve tacke
    # prozor.blit(dugme.tekst, (dugme.rect.x, dugme.rect.y) )
def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if Buttons.main_menu_dugme_quit.rect.collidepoint(dogadjaj.pos):

                    pygame.quit()
                    sys.exit()
                if Buttons.main_menu_dugme_credits.rect.collidepoint(dogadjaj.pos):
                    credits()

        prozor.fill((pygame.Color("cyan")))
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_quit)
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_credits)
        nacrtaj_dugme_bez_centiranja(main_menu_play_button)
        pygame.display.flip()
        sat.tick(30)
def credits():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:

                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if Buttons.credits_to_main_menu_button.rect.collidepoint(dogadjaj.pos):
                    return
        prozor.fill((pygame.Color("cyan")))
        prozor.blit(credits_text_developer  , (189, 132))
        prozor.blit(credits_text_daniil , (189, 242))
        prozor.blit(credits_text_tata, (189, 359))
        nacrtaj_dugme_bez_centiranja(credits_to_main_menu_button)
        pygame.display.flip()
        sat.tick(30)
def play():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()





        pygame.display.flip()
        sat.tick(30)
main_menu()
pygame.quit()
