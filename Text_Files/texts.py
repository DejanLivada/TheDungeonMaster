import pygame
pygame.init()
from Text_Files.credits_imena import *

choose_name_input_active = True
#----------------------FONTOVI---------------------------------
credits_font = pygame.font.SysFont('Consolas', 30)
choose_name_font = pygame.font.SysFont(None, 100)
welcome_font = pygame.font.SysFont(None, 70)
#---------------------TEXTOVI----------------------------------
credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_daniil = credits_font.render(f"Programming teacher : {programming_teacher2}", True, (255, 255, 255))
credits_text_tata = credits_font.render(f"Programming teacher : {programming_teacher}", True, (255, 255, 255))
player_name = ""
choose_name_title = choose_name_font.render("Choose your name", True, (255, 255, 255))
#----------------------CHOOSE YOUR CHARACTER TEXTS----------------------------
character1_text = credits_font.render("Knight", True, (255, 255, 255))
character2_text = credits_font.render("Pirate", True, (255, 255, 255))
character3_text = credits_font.render("Furry?", True, (255, 255, 255))
character1_stat_damage = credits_font.render("Damage : 50" , True , (255,255,255))
character1_stat_defense = credits_font.render("Defense : 10" , True , (255,255,255))
character1_stat_stamina = credits_font.render("Stamina : 40" , True , (255,255,255))
character2_stat_damage = credits_font.render("Damage : 40" , True , (255,255,255))
character2_stat_defense = credits_font.render("Defense : 20" , True , (255,255,255))
character2_stat_stamina = credits_font.render("Stamina : 40" , True , (255,255,255))
character3_stat_damage = credits_font.render("Damage : 30" , True , (255,255,255))
character3_stat_defense = credits_font.render("Defense : 10" , True , (255,255,255))
character3_stat_stamina = credits_font.render("Stamina : 60" , True , (255,255,255))