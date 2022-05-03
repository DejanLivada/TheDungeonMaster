# ----------------------------IMPORTI------------------
import sys

import pygame
import pickle
import Text_Files.texts
from UI import Buttons
import player_pictures
from os import path
from Entity import player
from Other.game_states import GameStates

# -------------------------PLAYER SLIKE I DEFINISANJE PLAYERA------------------
player_picture_1 = pygame.image.load("player_pictures/player1.png")
player_picture_1 = pygame.transform.scale(player_picture_1 , (100,100))

igrac = player.Player(None , 100 , None)
if path.exists("Saves/player_name.pickle"):
    with open("Saves/player_name.pickle", "rb") as f:
        igrac.name = pickle.load(f)
else:
    pass
# ----------------------OSNOVNE DEFINICJE----------------
pygame.init()
Xres = 800
Yres = 600
prozor = pygame.display.set_mode((Xres, Yres))
sat = pygame.time.Clock()
trenutno_stanje = GameStates.DEFAULT

# *---------------------------GAME LOOPOVI---------------------
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)  # lepsi nacin od linije dole, TOPLEFT je pozicija gornje leve tacke
    # prozor.blit(dugme.tekst, (dugme.rect.x, dugme.rect.y) )



def main_menu():
    global trenutno_stanje
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
                if Buttons.main_menu_play_button.rect.collidepoint(dogadjaj.pos):
                    if path.exists("Saves/trenutno_stanje.pickle"):
                        with open("Saves/trenutno_stanje.pickle", "rb") as f:
                            trenutno_stanje = pickle.load(f)
                        if trenutno_stanje == GameStates.CHOOSE_CHARACTER:
                            choose_character()
                        if trenutno_stanje == GameStates.CHOOSE_NAME:
                            choose_name()
                        if trenutno_stanje == GameStates.PLAY:
                            play()
                    else:
                        choose_name()


        trenutno_stanje = GameStates.DEFAULT

        prozor.fill((pygame.Color("cyan")))
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_quit)
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_credits)
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_play_button)
        pygame.display.flip()
        sat.tick(30)

def choose_character():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
        prozor.fill((0,0,0))
        prozor.blit(player_picture_1 ,(96, 99) )
        global trenutno_stanje
        trenutno_stanje = GameStates.CHOOSE_CHARACTER
        with open("Saves/trenutno_stanje.pickle", "wb") as f:
            pickle.dump(trenutno_stanje, f)

        pygame.display.flip()
        sat.tick(30)

def choose_name():
    program_radi = True
    while program_radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Text_Files.texts.choose_name_input_active = True
                Text_Files.texts.player_name = ""
            elif event.type == pygame.KEYDOWN and Text_Files.texts.choose_name_input_active:
                if event.key == pygame.K_RETURN:
                    Text_Files.texts.choose_name_input_active = False
                    with open("Saves/player_name.pickle", "wb") as f:
                        pickle.dump(Text_Files.texts.player_name, f)

                    choose_character()
                elif event.key == pygame.K_BACKSPACE:
                    Text_Files.texts.player_name = Text_Files.texts.player_name[:-1]
                else:
                    Text_Files.texts.player_name += event.unicode
        prozor.fill((pygame.Color("black")))
        prozor.blit(Text_Files.texts.choose_name_title, (100, 70))
        text_surf = Text_Files.texts.choose_name_font.render(Text_Files.texts.player_name, True, (255, 255, 255))
        prozor.blit(text_surf, text_surf.get_rect(center=prozor.get_rect().center))
        global trenutno_stanje
        trenutno_stanje = GameStates.CHOOSE_NAME
        with open("Saves/trenutno_stanje.pickle", "wb") as f:
            pickle.dump(trenutno_stanje, f)
        sat.tick(30)
        pygame.display.flip()


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
        prozor.blit(Text_Files.texts.credits_text_developer, (189, 132))
        prozor.blit(Text_Files.texts.credits_text_daniil, (189, 242))
        prozor.blit(Text_Files.texts.credits_text_tata, (189, 359))
        nacrtaj_dugme_bez_centiranja(Buttons.credits_to_main_menu_button)
        pygame.display.flip()
        sat.tick(30)


def play():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
        prozor.fill((255, 255, 255))
        from Entity import player
        global trenutno_stanje
        trenutno_stanje = GameStates.PLAY
        with open("Saves/trenutno_stanje.pickle", "wb") as f:
            pickle.dump(trenutno_stanje, f)
        pygame.display.flip()
        sat.tick(30)


# ----------------------ZVANJE POCETNE FUNKCIJE-----------------
main_menu()
pygame.quit()
