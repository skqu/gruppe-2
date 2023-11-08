import pygame
from sys import exit

pygame.init()

bottom_panel = 350
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 + bottom_panel

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon and Dragons")


font = pygame.font.SysFont("Times New Roman", 30)
panel_img = pygame.image.load("panel.png").convert_alpha()
aragorn_surface = pygame.image.load("aragorn.jpg")
dragon_surface = pygame.image.load("dragon.jpg")



class Hero:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

class Monster:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

hero = Hero("Aragorn", 30, 100, 8)
monster = Monster("Dragon", 12, 30, 5)




def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x, y))
    
def draw_panel():

    screen.blit(panel_img, (0,SCREEN_HEIGHT - bottom_panel))

    screen.blit(aragorn_surface,(150, SCREEN_HEIGHT - bottom_panel + 40))
    draw_text(f"{hero.name}", font, (255, 0, 0), 150, SCREEN_HEIGHT - bottom_panel + 150)
    draw_text(f"Health: {hero.health}", font, (255, 0, 0), 150, SCREEN_HEIGHT - bottom_panel + 190)
    draw_text(f"Strenght: {hero.attack}", font, (255, 0, 0), 150, SCREEN_HEIGHT - bottom_panel + 230)
    draw_text(f"Defence: {hero.defense}", font, (255, 0, 0), 150, SCREEN_HEIGHT - bottom_panel + 270)
    

    screen.blit(dragon_surface,(525, SCREEN_HEIGHT - bottom_panel + 40))
    draw_text(f"{monster.name}", font, (255, 0, 0), 525, SCREEN_HEIGHT - bottom_panel + 150)
    draw_text(f"Health: {monster.health}", font, (255, 0, 0), 525, SCREEN_HEIGHT - bottom_panel + 190)
    draw_text(f"Strenght: {monster.attack}", font, (255, 0, 0), 525, SCREEN_HEIGHT - bottom_panel + 230)
    draw_text(f"Defence: {monster.defense}", font, (255, 0, 0), 525, SCREEN_HEIGHT - bottom_panel + 270)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    draw_panel()
    
   

    pygame.display.update()

