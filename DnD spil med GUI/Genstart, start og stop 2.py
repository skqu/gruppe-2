import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.HERO_SIZE = 70
        self.SPEED = 5

        self.name = pygame.display.set_caption("DnD 2.0")

        self.bg_level_one = pygame.image.load('billeder/bane5.png')
        self.bg_level_one = pygame.transform.scale(self.bg_level_one, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.monster_image = pygame.image.load('billeder/Dragon.png')
        self.monster_image = pygame.transform.scale(self.monster_image, (self.HERO_SIZE, self.HERO_SIZE))

        self.hero_image = pygame.image.load('Knight.png')
        self.hero_image = pygame.transform.scale(self.hero_image, (self.HERO_SIZE, self.HERO_SIZE))

        self.icon = pygame.display.set_icon(self.hero_image)

        self.size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.SysFont('arial', 30, bold=True)
        self.font2 = pygame.font.SysFont('arial', 20, bold=True)

        self.game_message = self.font1.render('Press space to start', False, (255, 0, 0))
        self.game_message_rect = self.game_message.get_rect(center=(400, 280))
        self.game_active = False

        self.hero = Hero("Aragorn", 100, 10, 5, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, self.hero_image)
        self.monster1 = Monster("Dragon", 50, 8, 3, 100, 100, self.monster_image)
        self.monster2 = Monster("Giant", 50, 8, 3, 700, 500, self.monster_image)

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
                            self.monster2.y = 500
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.bg_level_one, (0, 0))

            if not self.game_active:
                self.screen.blit(self.game_message, self.game_message_rect)
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.hero.move(-self.SPEED, 0)
                if keys[pygame.K_d]:
                    self.hero.move(self.SPEED, 0)
                if keys[pygame.K_w]:
                    self.hero.move(0, -self.SPEED)
                if keys[pygame.K_s]:
                    self.hero.move(0, self.SPEED)

                if self.monster1.active:
                    self.monster1.move_towards_hero(self.hero)
                if self.monster2.active:
                    self.monster2.move_towards_hero(self.hero)

            self.screen.blit(self.hero.image, (self.hero.x, self.hero.y))
            self.screen.blit(self.monster1.image, (self.monster1.x, self.monster1.y))
            self.screen.blit(self.monster2.image, (self.monster2.x, self.monster2.y))

            close_text = self.font2.render('Press ESCAPE to close the game', True, (255, 255, 255))
            restart_text = self.font2.render('Press R to restart the game', True, (255, 255, 255))
            self.screen.blit(close_text, (10, 10))
            self.screen.blit(restart_text, (10, 40))

            pygame.display.flip()
            self.clock.tick(self.FPS)