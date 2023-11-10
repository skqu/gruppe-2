import pygame
import math
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
HERO_SIZE = 70
SPEED = 5

bg_level_one = pygame.image.load('../billeder/bane5.png')
bg_level_one = pygame.transform.scale(bg_level_one, (SCREEN_WIDTH, SCREEN_HEIGHT))

monster_image = pygame.image.load('../billeder/Dragon.png')
monster_image = pygame.transform.scale(monster_image, (HERO_SIZE, HERO_SIZE))

hero_image = pygame.image.load('../billeder/Knight.png')
hero_image = pygame.transform.scale(hero_image, (HERO_SIZE, HERO_SIZE))

class Hero:
    def __init__(self, name, health, strength, defense, x, y):
        self.x = x
        self.y = y
        self.image = hero_image  # add the hero image, Thomas

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x >= 0 and new_x <= SCREEN_WIDTH - HERO_SIZE:
            self.x = new_x
        if new_y >= 0 and new_y <= SCREEN_HEIGHT - HERO_SIZE:
            self.y = new_y

class Monster:
    def __init__(self, name, health, strength, defense, x, y):
        self.x = x
        self.y = y
        self.image = monster_image  # add the monster image, Thomas
        # Add to the monster won't move, Thomas
        self.active = False

    def move_towards_hero(self, hero):
        if not self.active:
            return
        dx = hero.x - self.x
        dy = hero.y - self.y
        angle = math.atan2(dy, dx)
        self.x += math.cos(angle)
        self.y += math.sin(angle)

pygame.init()

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


# Add the hero and monsters
hero = Hero("Aragorn", 100, 10, 5, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
monster1 = Monster("Dragon", 50, 8, 3, 100, 100)
monster2 = Monster("Giant", 50, 8, 3, 700, 500)

clock = pygame.time.Clock()
#Added fonts
font1 = pygame.font.SysFont('arial', 30, bold = True)
font2 = pygame.font.SysFont('arial', 20, bold = True)

# Add text to get the user to start the game
game_message = font1.render('Press space to start', False,(255, 0, 0))
game_message_rect = game_message.get_rect(center = (400,280))
game_active = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            if not game_active:
                if event.key == pygame.K_SPACE:
                    game_active = True
                # Activate the monsters
                monster1.active = True
                monster2.active = True


            else:
                # Add keypress R for restarting the game
                if event.key == pygame.K_r:
                    game_active = False
                    # Deactivate the monsters
                    monster1.active = False
                    monster2.active = False

                    # Reset the hero position to the middle
                    hero.x = SCREEN_WIDTH // 2
                    hero.y = SCREEN_HEIGHT // 2

                    # Reset the monster positions to the sides
                    monster1.x = 100
                    monster1.y = 100
                    monster2.x = 700
                    monster2.y = 500
            # Add ESCAPE for closing the game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(bg_level_one, (0, 0))

    if not game_active:
        screen.blit(game_message, game_message_rect)

    # Movement changed to WASD
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            hero.move(-SPEED, 0)
        if keys[pygame.K_d]:
            hero.move(SPEED, 0)
        if keys[pygame.K_w]:
            hero.move(0, -SPEED)
        if keys[pygame.K_s]:
            hero.move(0, SPEED)

        # Make sure the monster is not moving without SPACE being pressed first
        if monster1.active:
            monster1.move_towards_hero(hero)
        if monster2.active:
            monster2.move_towards_hero(hero)

    screen.blit(hero.image, (hero.x, hero.y))
    screen.blit(monster1.image, (monster1.x, monster1.y))
    screen.blit(monster2.image, (monster2.x, monster2.y))


    # added text for the user to know which buttons to use
    close_text = font2.render('Press ESCAPE to close the game', True, (255, 255, 255))
    restart_text = font2.render('Press R to restart the game', True, (255, 255, 255))
    screen.blit(close_text, (10, 10))
    screen.blit(restart_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

