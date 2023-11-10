<<<<<<< HEAD
import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Dungeon and Dragons")


font = pygame.font.Font(None, 30)



def draw_text(text, x, y):
    text_surface = font.render(text, True, "Black")
    screen.blit(text_surface, (x, y))


class Hero:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

    def __str__(self):
        return f"{self.name}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}"


class Monster:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

    def __str__(self):
        return f" {self.name}\n Health: {self.health}\n Attack: {self.attack}\n Defense: {self.defense}"


hero = Hero("Aragorn", 30, 100, 8)
monster = Monster("Dragon", 12, 30, 5)



test_surface = pygame.Surface((1000,225))
test_surface.fill("Beige")
aragorn_surface = pygame.image.load("aragorn.jpg")
dragon_surface = pygame.image.load("dragon.jpg")

aragorn_surface


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.blit(test_surface,(0,0))
    screen.blit(aragorn_surface,(0,0))
    screen.blit(dragon_surface,(775,0))
    
    hero_text_x = 250
    hero_text_y = 50
    monster_text_x = 625
    monster_text_y = 50

    
    
    hero_text = str(hero)
    monster_text = str(monster)

    
    for i, line in enumerate(hero_text.split('\n')):
        draw_text(line, hero_text_x, hero_text_y + i * 30)
    for i, line in enumerate(monster_text.split('\n')):
        draw_text(line, monster_text_x, monster_text_y + i * 30)

    pygame.display.update()

=======
import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Dungeon and Dragons")


font = pygame.font.Font(None, 30)



def draw_text(text, x, y):
    text_surface = font.render(text, True, "Black")
    screen.blit(text_surface, (x, y))


class Hero:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

    def __str__(self):
        return f"{self.name}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}"


class Monster:
    def __init__(self, name, attack, health, defense):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense

    def __str__(self):
        return f" {self.name}\n Health: {self.health}\n Attack: {self.attack}\n Defense: {self.defense}"


hero = Hero("Aragorn", 30, 100, 8)
monster = Monster("Dragon", 12, 30, 5)



test_surface = pygame.Surface((1000,225))
test_surface.fill("Beige")
aragorn_surface = pygame.image.load("aragorn.jpg")
dragon_surface = pygame.image.load("dragon.jpg")

aragorn_surface


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.blit(test_surface,(0,0))
    screen.blit(aragorn_surface,(0,0))
    screen.blit(dragon_surface,(775,0))
    
    hero_text_x = 250
    hero_text_y = 50
    monster_text_x = 625
    monster_text_y = 50

    
    
    hero_text = str(hero)
    monster_text = str(monster)

    
    for i, line in enumerate(hero_text.split('\n')):
        draw_text(line, hero_text_x, hero_text_y + i * 30)
    for i, line in enumerate(monster_text.split('\n')):
        draw_text(line, monster_text_x, monster_text_y + i * 30)

    pygame.display.update()

>>>>>>> 53a5f1ebc07cda1b15adb0e8854a784a626703dd
