import pygame
import pyperclip
from pygame import Vector2
pygame.init()
Xrezolucija = 600
Yrezolucija = 600
kordinate_misa = []
prozor = pygame.display.set_mode((Xrezolucija,Yrezolucija))
sat = pygame.time.Clock()
mojFont = pygame.font.SysFont('Consolas', 20)
class Dugme:
    tekst = None
    rect = None
    boja = None
kopiraj_dugme = Dugme()
kopiraj_dugme.tekst = mojFont.render("Kopiraj Kordinate",True ,(255,255,255))
kopiraj_dugme.rect = pygame.Rect(180 , 182 ,300,50)
kopiraj_dugme.boja = (255,0,0)
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)
program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        prozor.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()

        pozicija_misa = str(mouse_pos)
        kordinate_misa.append(pozicija_misa)
        kordinate_text = mojFont.render("Kordinate klika su: " + pozicija_misa, True, (255, 255, 255))
        upozorenje_text = mojFont.render("Da bi kopirao kordinate klikni K_LEFT ", True, (255, 255, 255))
        prozor.blit(kordinate_text, (50, 100))
        prozor.blit(upozorenje_text , (50 , 70))
    if dogadjaj.type == pygame.KEYDOWN:
        if dogadjaj.key == pygame.K_LEFT:
            pyperclip.copy(kordinate_misa[-1])




    pygame.display.flip()


pygame.quit()