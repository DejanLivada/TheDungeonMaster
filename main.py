# ----------------------------IMPORTI------------------
import sys

import pygame
import pickle

import Entity.player
import Text_Files.texts
import UI.Buttons
from UI import Buttons
import player_pictures
from os import path
from Entity import player
from Other.game_states import GameStates

# -------------------------PLAYER SLIKE I DEFINISANJE PLAYERA------------------
player_picture_1 = pygame.image.load("player_pictures/player1.png")
player_picture_1 = pygame.transform.scale(player_picture_1 , (200,200))
player_picture_2 = pygame.image.load("player_pictures/player2.png")
player_picture_2 = pygame.transform.smoothscale(player_picture_2 , (200,200))
player_picture_3 = pygame.image.load("player_pictures/player3.jpg")
player_picture_3 = pygame.transform.scale(player_picture_3 , (350,200))

igrac = Entity.player.Player(None , 100 , Entity.player.player_izabrana_slika)
if path.exists("Saves/player_name.pickle"):
    with open("Saves/player_name.pickle", "rb") as f:
        igrac.name = pickle.load(f)

else:
    pass
if path.exists("Saves/player_picture.pickle"):
    with open("Saves/player_picture.pickle", "rb") as f:
        if Entity.player.player_izabrana_slika == "Knight":
            igrac.slika = player_picture_1
        if Entity.player.player_izabrana_slika == "Pirate":
            igrac.slika = player_picture_2
        if Entity.player.player_izabrana_slika == "Furry":
            igrac.slika = player_picture_3
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

def choose_character():                     #PLAYER CHOOSING HIS CHARACTER
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if UI.Buttons.choose_player1.rect.collidepoint(dogadjaj.pos):
                    igrac.slika = player_picture_1
                    Entity.player.player_izabrana_slika = "Knight"
                    with open("Saves/player_picture.pickle", "wb") as f:
                        pickle.dump(Entity.player.player_izabrana_slika, f)
                    play()
                if UI.Buttons.choose_player2.rect.collidepoint(dogadjaj.pos):
                    igrac.slika = player_picture_2
                    Entity.player.player_izabrana_slika = "Pirate"
                    with open("Saves/player_picture.pickle", "wb") as f:
                        pickle.dump(Entity.player.player_izabrana_slika, f)
                    play()
                if UI.Buttons.choose_player3.rect.collidepoint(dogadjaj.pos):
                    igrac.slika = player_picture_3
                    Entity.player.player_izabrana_slika = "Furry"
                    with open("Saves/player_picture.pickle", "wb") as f:
                        pickle.dump(Entity.player.player_izabrana_slika, f)
                    play()
        prozor.fill((0,0,0))
        prozor.blit(player_picture_1 ,(64, 99) )
        prozor.blit(player_picture_2 , (300 , 85))
        prozor.blit(player_picture_3 , (500 , 99))
        prozor.blit(Text_Files.texts.character1_text , (100 , 50))
        prozor.blit(Text_Files.texts.character2_text, (350, 50))
        prozor.blit(Text_Files.texts.character3_text, (620, 50))
        if player_picture_1.get_rect().collidepoint(pygame.mouse.get_pos()):
            prozor.blit(Text_Files.texts.character1_stat_damage , (50 , 350))
            prozor.blit(Text_Files.texts.character1_stat_defense, (50, 390))
            prozor.blit(Text_Files.texts.character1_stat_stamina, (50, 430))
        if player_picture_2.get_rect().collidepoint(pygame.mouse.get_pos()):
            prozor.blit(Text_Files.texts.character2_stat_damage , (300 , 350))
            prozor.blit(Text_Files.texts.character2_stat_defense, (300, 390))
            prozor.blit(Text_Files.texts.character2_stat_stamina, (300, 430))
        if player_picture_3.get_rect().collidepoint(pygame.mouse.get_pos()):
            prozor.blit(Text_Files.texts.character3_stat_damage , (570 , 350))
            prozor.blit(Text_Files.texts.character3_stat_defense, (570, 390))
            prozor.blit(Text_Files.texts.character3_stat_stamina, (570, 430))
        nacrtaj_dugme_bez_centiranja(UI.Buttons.choose_player1)
        nacrtaj_dugme_bez_centiranja(UI.Buttons.choose_player2)
        nacrtaj_dugme_bez_centiranja(UI.Buttons.choose_player3)
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
        prozor.blit(igrac.slika , (100,300))
        with open("Saves/trenutno_stanje.pickle", "wb") as f:
            pickle.dump(trenutno_stanje, f)
        pygame.display.flip()
        sat.tick(30)


# ----------------------ZVANJE POCETNE FUNKCIJE-----------------
main_menu()
pygame.quit()
