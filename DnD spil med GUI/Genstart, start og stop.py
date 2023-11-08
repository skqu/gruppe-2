import pygame
import sys

# sørg for at class monster har self.active = False på

#Added fonts
font1 = pygame.font.SysFont('arial', 30, bold = True)
font2 = pygame.font.SysFont('arial', 20, bold = True)

# Add text to get the user to start the game
game_message = font1.render('Press space to start', False,(255, 0, 0))
game_message_rect = game_message.get_rect(center = (400,300))
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

 close_text = font2.render('Press ESCAPE to close the game', True, (255, 255, 255))
    restart_text = font2.render('Press R to restart the game', True, (255, 255, 255))
    screen.blit(close_text, (10, 10))
    screen.blit(restart_text, (10, 40))














