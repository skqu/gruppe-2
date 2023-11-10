<<<<<<< HEAD
import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOTTOM_PANEL_HEIGHT = 350  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL_HEIGHT))
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
    screen.blit(panel_img, (0, SCREEN_HEIGHT))

    hero_x, monster_x = 150, 525
    info_y = SCREEN_HEIGHT + 40

    screen.blit(aragorn_surface, (hero_x, info_y))
    draw_text(f"{hero.name}", font, (255, 0, 0), hero_x, info_y + 110)
    draw_text(f"Health: {hero.health}", font, (255, 0, 0), hero_x, info_y + 150)
    draw_text(f"Strenght: {hero.attack}", font, (255, 0, 0), hero_x, info_y + 190)
    draw_text(f"Defence: {hero.defense}", font, (255, 0, 0), hero_x, info_y + 230)

    screen.blit(dragon_surface, (monster_x, info_y))
    draw_text(f"{monster.name}", font, (255, 0, 0), monster_x, info_y + 110)
    draw_text(f"Health: {monster.health}", font, (255, 0, 0), monster_x, info_y + 150)
    draw_text(f"Strenght: {monster.attack}", font, (255, 0, 0), monster_x, info_y + 190)
    draw_text(f"Defence: {monster.defense}", font, (255, 0, 0), monster_x, info_y + 230)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_panel()
    pygame.display.update()
=======
import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOTTOM_PANEL_HEIGHT = 350  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL_HEIGHT))
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
    screen.blit(panel_img, (0, SCREEN_HEIGHT))

    hero_x, monster_x = 150, 525
    info_y = SCREEN_HEIGHT + 40

    screen.blit(aragorn_surface, (hero_x, info_y))
    draw_text(f"{hero.name}", font, (255, 0, 0), hero_x, info_y + 110)
    draw_text(f"Health: {hero.health}", font, (255, 0, 0), hero_x, info_y + 150)
    draw_text(f"Strenght: {hero.attack}", font, (255, 0, 0), hero_x, info_y + 190)
    draw_text(f"Defence: {hero.defense}", font, (255, 0, 0), hero_x, info_y + 230)

    screen.blit(dragon_surface, (monster_x, info_y))
    draw_text(f"{monster.name}", font, (255, 0, 0), monster_x, info_y + 110)
    draw_text(f"Health: {monster.health}", font, (255, 0, 0), monster_x, info_y + 150)
    draw_text(f"Strenght: {monster.attack}", font, (255, 0, 0), monster_x, info_y + 190)
    draw_text(f"Defence: {monster.defense}", font, (255, 0, 0), monster_x, info_y + 230)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_panel()
    pygame.display.update()
>>>>>>> 53a5f1ebc07cda1b15adb0e8854a784a626703dd
