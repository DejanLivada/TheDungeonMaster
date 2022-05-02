import pygame
pygame.init()
from Text_Files.credits_imena import *
#----------------------FONTOVI---------------------------------
credits_font = pygame.font.SysFont('Consolas', 30)

#---------------------TEXTOVI----------------------------------
credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_daniil = credits_font.render(f"Programming teacher : {programming_teacher2}", True, (255, 255, 255))
credits_text_tata = credits_font.render(f"Programming teacher : {programming_teacher}", True, (255, 255, 255))

#--------------------------------------------------------------
