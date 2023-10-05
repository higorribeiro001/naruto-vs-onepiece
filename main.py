import pygame
from player import Player
from character_naruto.naruto import Naruto
from character_sasuke.sasuke import Sasuke

class Game:
    def main():
        pygame.init()

        screen = pygame.display.set_mode((980, 720))
        clock = pygame.time.Clock()
        running = True

        group_sprite = pygame.sprite.Group()

        n = Naruto()
        s = Sasuke()
        p1 = Player(screen, s.sprites(), s.__class__.__name__, 100, False, True)
        p2 = Player(screen, n.sprites(), n.__class__.__name__, 820, True, False)

        group_sprite.add(p1)
        group_sprite.add(p2)

        def damage_p1(dif_pos_right, dif_pos_left, dif_pos_y_p1, dif_pos_y_p2, damage):
            if (dif_pos_right < -10 and dif_pos_right > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[pygame.K_DOWN] == False:
                if p2.life > 0:
                    p2.life -= damage
                    p2.damage()

            if (dif_pos_left < -10 and dif_pos_left > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[pygame.K_DOWN] == False:
                if p2.life > 0:
                    p2.life -= damage
                    p2.damage()

        def damage_p2(dif_pos_right, dif_pos_left, dif_pos_y_p1, dif_pos_y_p2, damage):
            if (dif_pos_right < -10 and dif_pos_right > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[pygame.K_DOWN] == False:
                if p1.life > 0:
                    p1.life -= damage
                    p1.damage()

            if (dif_pos_left < -10 and dif_pos_left > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[pygame.K_DOWN] == False:
                if p1.life > 0:
                    p1.life -= 5
                    p1.damage()

        while running:
            dif_pos_x_right = p2.rect.topleft[0] - p1.rect.topright[0]
            dif_pos_x_left = p1.rect.topleft[0] - p2.rect.topright[0]
            dif_pos_y_p1 = p1.rect.topright[1]
            dif_pos_y_p2 = p2.rect.topleft[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    ...
                if event.type == pygame.KEYUP:
                    if p1.life == 0:
                        p1.dead()
                        p2.base()
                        break

                    elif p2.life == 0:
                        p2.dead()
                        p1.base()
                        break

                    else:
                        if event.key == pygame.K_a:
                            p1.base_left()

                        if event.key == pygame.K_w:
                            p1.down()

                        if event.key == pygame.K_d:
                            p1.base_right()

                        if event.key == pygame.K_g:
                            p1.base()
                            p2.base()

                        if event.key == pygame.K_s:
                            p1.base()

                        if event.key == pygame.K_h:
                            p1.base()
                            p2.base()

                        if event.key == pygame.K_f:
                            p1.base()

                        if event.key == pygame.K_j:
                            p1.base()
                            p2.base()

                        if event.key == pygame.K_RIGHT:
                            p2.base_right()

                        if event.key == pygame.K_LEFT:
                            p2.base_left()

                        if event.key == pygame.K_UP:
                            p2.down()

                        if event.key == pygame.K_i:
                            p2.base()
                            p1.base()

                        if event.key == pygame.K_DOWN:
                            p2.base()

                        if event.key == pygame.K_o:
                            p2.base()
                            p1.base()

                        if event.key == pygame.K_u:
                            p2.base()

                        if event.key == pygame.K_p:
                            p2.base()
                            p1.base()

            screen.fill("cyan")

            group_sprite.draw(screen)
            # group_sprite.update()

            # player 1
            font_p1 = pygame.font.Font(None, 30)
            name_p1 = font_p1.render(p1.name_character, True, (255,255,255))
            name_p1_rect = name_p1.get_rect(center=(135, 100)) # posicionar o texto na tela
            screen.blit(name_p1, name_p1_rect) # desenhar o texto na tela
            # vida
            pygame.draw.rect(screen, 'green', (100, 120, p1.life, 20), border_radius=5)
            # estamina
            pygame.draw.rect(screen, 'blue', (100, 145, p1.stamina, 10), border_radius=5)

            # player 2
            font_p2 = pygame.font.Font(None, 30)
            name_p2 = font_p2.render(p2.name_character, True, (255,255,255))
            name_p2_rect = name_p2.get_rect(center=(735, 100)) # posicionar o texto na tela
            screen.blit(name_p2, name_p2_rect) # desenhar o texto na tela
            # vida
            pygame.draw.rect(screen, 'green', (700, 120, p2.life, 20), border_radius=5)
            # estamina
            pygame.draw.rect(screen, 'blue', (700, 145, p2.stamina, 10), border_radius=5)

            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                p1.up()
                
            if keys[pygame.K_d]:
                p1.right()

            if keys[pygame.K_a]:
                p1.left()

            if keys[pygame.K_g]:
                p1.punch()
                damage_p1(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 0.5)
            
            if keys[pygame.K_s]:
                p1.block()

            if keys[pygame.K_h]:
                p1.kick()

                damage_p1(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 0.5)

            if keys[pygame.K_f]:
                p1.chakra()

            if keys[pygame.K_j]:
                if p1.stamina > 100:
                    p1.special()
                    damage_p1(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 1)

            if keys[pygame.K_UP]:
                p2.up()
                
            if keys[pygame.K_RIGHT]:
                p2.right()

            if keys[pygame.K_LEFT]:
                p2.left()

            if keys[pygame.K_i]:
                p2.punch()
                damage_p2(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 0.5)
            
            if keys[pygame.K_DOWN]:
                p2.block()

            if keys[pygame.K_o]:
                p2.kick()
                damage_p2(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 0.5)

            if keys[pygame.K_u]:
                p2.chakra()

            if keys[pygame.K_p]:
                if p2.stamina > 100:
                    p2.special()
                    damage_p2(dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 1)

            clock.tick(30)

        pygame.quit()

if __name__ == '__main__':
    Game.main()