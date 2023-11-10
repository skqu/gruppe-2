import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOTTOM_PANEL_HEIGHT = 350
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL_HEIGHT))
pygame.display.set_caption("Dungeon and Dragons")

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

class stats_panel:
    def __init__(self):
        self.red = (255, 0, 0)
        self.font = pygame.font.SysFont("Times New Roman", 30)
        self.panel_img = pygame.image.load("panel.png").convert_alpha()
        self.aragorn_surface = pygame.image.load("aragorn.jpg")
        self.dragon_surface = pygame.image.load("dragon.jpg")

        self.hero = hero 
        self.monster = monster

    def draw_text(self, text, text_col, x, y):
        text = self.font.render(text, True, text_col)
        screen.blit(text, (x, y))

    def draw_panel(self):
        screen.blit(self.panel_img, (0, SCREEN_HEIGHT))

        hero_x, monster_x = 150, 525
        info_y = SCREEN_HEIGHT + 40

        screen.blit(self.aragorn_surface, (hero_x, info_y))
        self.draw_text(f"{self.hero.name}", self.red, hero_x, info_y + 110)
        self.draw_text(f"Health: {self.hero.health}", self.red, hero_x, info_y + 150)
        self.draw_text(f"Strength: {self.hero.attack}", self.red, hero_x, info_y + 190)
        self.draw_text(f"Defense: {self.hero.defense}", self.red, hero_x, info_y + 230)

        screen.blit(self.dragon_surface, (monster_x, info_y))
        self.draw_text(f"{self.monster.name}", self.red, monster_x, info_y + 110)
        self.draw_text(f"Health: {self.monster.health}", self.red, monster_x, info_y + 150)
        self.draw_text(f"Strength: {self.monster.attack}", self.red, monster_x, info_y + 190)
        self.draw_text(f"Defense: {self.monster.defense}", self.red, monster_x, info_y + 230)

def main():
    game = stats_panel()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game.draw_panel()
        pygame.display.update()

if __name__ == "__main__":
    main()
