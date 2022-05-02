import pygame
pygame.init()
from Text_Files.credits_imena import *

choose_name_input_active = True
#----------------------FONTOVI---------------------------------
credits_font = pygame.font.SysFont('Consolas', 30)
choose_name_font = pygame.font.SysFont(None, 100)
welcome_font = pygame.font.SysFont(None, 100)
#---------------------TEXTOVI----------------------------------
credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_daniil = credits_font.render(f"Programming teacher : {programming_teacher2}", True, (255, 255, 255))
credits_text_tata = credits_font.render(f"Programming teacher : {programming_teacher}", True, (255, 255, 255))
player_name = ""
choose_name_title = choose_name_font.render("Choose your name", True, (255, 255, 255))
welcome_text = welcome_font.render(f"Welcome {player_name}", True, (0, 128, 0))
#--------------------------------------------------------------
