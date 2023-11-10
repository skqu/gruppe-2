import pygame
import math
import sys

class Game:
    SCREEN_WIDTH = 800
    SCREEN_BOTTOM_PANEL_HEIGHT = 250
    SCREEN_HEIGHT = 400
    #SCREEN_HEIGHT = 300 + SCREEN_BOTTOM_PANEL_HEIGHT
    HERO_SIZE = 70


    def __init__(self):
        pygame.init()

        self.FPS = 60
        self.SPEED = 5

        self.name = pygame.display.set_caption("DnD 2.0")

        self.bg_level_one = pygame.image.load('billeder/map.jpg')
        self.bg_level_one = pygame.transform.scale(self.bg_level_one, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.hero_image = pygame.image.load('billeder/hero2.png')
        self.dragon_image = pygame.image.load('billeder/dragon3.png')
        self.giant_image = pygame.image.load('billeder/giant2.png')

        self.SIZE = 70

        self.hero_image = pygame.transform.scale(self.hero_image, (self.SIZE, self.SIZE))
        self.dragon_image = pygame.transform.scale(self.dragon_image, (self.SIZE, self.SIZE))
        self.giant_image = pygame.transform.scale(self.giant_image, (self.SIZE, self.SIZE))

        self.icon = pygame.display.set_icon(self.hero_image)

        self.size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT + self.SCREEN_BOTTOM_PANEL_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.SysFont('Times New Roman', 30, bold=True)
        self.font2 = pygame.font.SysFont('Times New Roman', 20, bold=True)

        self.game_message = self.font1.render('Press space to start', False, ('white'))
        self.game_message_rect = self.game_message.get_rect(center=(400, 280))
        self.game_active = False

        self.hero = Hero("Aragorn", 100, 12, 5, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, self.hero_image)
        self.monster1 = Monster("Dragon", 40, 9, 3, 100, 100, self.dragon_image)
        self.monster2 = Monster("Giant", 60, 5, 2, 700, 300, self.giant_image)

        self.stats_panel = StatsPanel(self.hero, self.monster1, self.monster2, self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:


                    if not self.game_active:
                        if event.key == pygame.K_SPACE:
                            self.game_active = True
                            self.monster1.active = True
                            self.monster2.active = True
                    else:
                        if event.key == pygame.K_r:
                            self.game_active = False
                            self.monster1.active = False
                            self.monster2.active = False

                            self.hero.x = self.SCREEN_WIDTH // 2
                            self.hero.y = self.SCREEN_HEIGHT // 2

                            self.monster1.x = 100
                            self.monster1.y = 100
                            self.monster2.x = 700
                            self.monster2.y = 300

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.bg_level_one, (0, 0))

            if not self.game_active:
                self.screen.blit(self.game_message, self.game_message_rect)
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.hero.move(-self.SPEED, 0)
                if keys[pygame.K_RIGHT]:
                    self.hero.move(self.SPEED, 0)
                if keys[pygame.K_UP]:
                    self.hero.move(0, -self.SPEED)
                if keys[pygame.K_DOWN]:
                    self.hero.move(0, self.SPEED)

                if self.monster1.active:
                    self.monster1.move_towards_hero(self.hero)
                if self.monster2.active:
                    self.monster2.move_towards_hero(self.hero)

            self.screen.blit(self.hero.image, (self.hero.x, self.hero.y))
            self.screen.blit(self.monster1.image, (self.monster1.x, self.monster1.y))
            self.screen.blit(self.monster2.image, (self.monster2.x, self.monster2.y))

            self.stats_panel.draw_panel()

            close_text = self.font2.render('Press ESCAPE to close the game', True, (255, 255, 255))
            restart_text = self.font2.render('Press R to restart the game', True, (255, 255, 255))
            self.screen.blit(close_text, (10, 10))
            self.screen.blit(restart_text, (10, 40))

            pygame.display.flip()
            self.clock.tick(self.FPS)

class Hero:
    def __init__(self, name, health, strength, defense, x, y, image):
        self.name = name
        self.health = health
        self.attack = strength
        self.defense = defense
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x <= Game.SCREEN_WIDTH - Game.HERO_SIZE:
            self.x = new_x
        if 0 <= new_y <= Game.SCREEN_HEIGHT - Game.HERO_SIZE:
            self.y = new_y

class Monster:
    def __init__(self, name, health, strength, defense, x, y, image):
        self.name = name
        self.health = health
        self.attack = strength
        self.defense = defense
        self.x = x
        self.y = y
        self.image = image
        self.active = False

    def move_towards_hero(self, hero):
        if not self.active:
            return
        dx = hero.x - self.x
        dy = hero.y - self.y
        angle = math.atan2(dy, dx)
        self.x += math.cos(angle)
        self.y += math.sin(angle)

class StatsPanel:
    def __init__(self, hero, monster1, monster2, screen):
        self.red = (255, 0, 0)
        self.font = pygame.font.SysFont("Times New Roman", 20)
        panel_img = pygame.image.load("billeder/panel.png").convert_alpha()
        scaling_factor = 300 / panel_img.get_height()
        panel_width = int(panel_img.get_width() + scaling_factor)
        panel_height = 250
        self.panel_img = pygame.transform.scale(panel_img, (panel_width, panel_height))
        self.aragorn_surface = pygame.image.load("billeder/aragorn.jpg")
        self.dragon_surface = pygame.image.load("billeder/dragon_stat.jpg")
        self.giant_surface = pygame.image.load("billeder/giant_profile.png")


        self.hero = hero
        self.monster1 = monster1
        self.monster2 = monster2
        self.screen = screen

    def draw_text(self, text, text_col, x, y):
        text = self.font.render(text, True, text_col)
        self.screen.blit(text, (x, y))

    def draw_panel(self):
        self.screen.blit(self.panel_img, (0, Game.SCREEN_HEIGHT))

        hero_x, monster_drage, monster_giant = 150, 400, 550
        info_y = Game.SCREEN_HEIGHT + 30

        self.screen.blit(self.aragorn_surface, (hero_x, info_y))
        self.draw_text(f"{self.hero.name}", self.red, hero_x, info_y + 100)
        self.draw_text(f"Health: {self.hero.health}", self.red, hero_x, info_y + 130)
        self.draw_text(f"Strength: {self.hero.attack}", self.red, hero_x, info_y + 150)
        self.draw_text(f"Defense: {self.hero.defense}", self.red, hero_x, info_y + 170)

        self.screen.blit(self.dragon_surface, (monster_drage, info_y))
        self.draw_text(f"{self.monster1.name}", self.red, monster_drage, info_y + 100)
        self.draw_text(f"Health: {self.monster1.health}", self.red, monster_drage, info_y + 130)
        self.draw_text(f"Strength: {self.monster1.attack}", self.red, monster_drage, info_y + 150)
        self.draw_text(f"Defense: {self.monster1.defense}", self.red, monster_drage, info_y + 170)

        self.screen.blit(self.giant_surface, (monster_giant, info_y))
        self.draw_text(f"{self.monster2.name}", self.red, monster_giant, info_y + 100)
        self.draw_text(f"Health: {self.monster2.health}", self.red, monster_giant, info_y + 130)
        self.draw_text(f"Strength: {self.monster2.attack}", self.red, monster_giant, info_y + 150)
        self.draw_text(f"Defense: {self.monster2.defense}", self.red, monster_giant, info_y + 170)

if __name__ == "__main__":
    game = Game()
    game.run()
