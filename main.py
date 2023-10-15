import pygame
import time as t
from player import Player
from character_naruto.naruto import Naruto
from character_sasuke.sasuke import Sasuke
import sys


def menu_screen():
    screen.fill(WHITE)

    # Desenhe o título
    font = pygame.font.Font(None, 36)
    title_text = font.render("Menu Principal", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Desenhe os botões
    button_width, button_height = 200, 50
    play_button = pygame.Rect(
        WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height
    )
    quit_button = pygame.Rect(
        WIDTH // 2 - button_width // 2, HEIGHT // 2 + 70, button_width, button_height
    )

    pygame.draw.rect(screen, BLACK, play_button)
    pygame.draw.rect(screen, BLACK, quit_button)

    play_text = font.render("BATALHAR", True, WHITE)
    play_text_rect = play_text.get_rect(center=play_button.center)
    screen.blit(play_text, play_text_rect)

    quit_text = font.render("EXIT", True, WHITE)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_text_rect)

    # Lógica para detectar clique nos botões
    mouse_pos = pygame.mouse.get_pos()
    if play_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            return states["battle"]
    elif quit_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()

    return states["menu"]


def selection_screen():
    screen.fill(WHITE)

    # Desenhe o título
    font = pygame.font.Font(None, 36)
    title_text = font.render("Selecione Dois Personagens", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Desenhe os personagens
    character_width, character_height = 150, 150
    margin = 10
    num_characters = len(characters)

    for i in range(num_characters):
        x = (i % 3) * (character_width + margin) + (WIDTH // 4)
        y = (i // 3) * (character_height + margin) + (HEIGHT // 2)

        character_rect = pygame.Rect(x, y, character_width, character_height)
        pygame.draw.rect(screen, BLACK, character_rect)

        character_text = font.render(characters[i], True, WHITE)
        character_text_rect = character_text.get_rect(center=character_rect.center)
        screen.blit(character_text, character_text_rect)

        if character_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(
                screen, (0, 0, 255), character_rect, 3
            )  # Destacar personagem sob o cursor
            if pygame.mouse.get_pressed()[0]:
                if (
                    len(selected_characters) < 2
                    and characters[i] not in selected_characters
                ):
                    selected_characters.append(characters[i])

    if len(selected_characters) == 2:
        return states[
            "battle"
        ]  # Se dois personagens forem selecionados, vá para a tela de jogo

    return states["select_characters"]


def battle_screen(running, clock):
    end_game = False
    n = Naruto()
    s = Sasuke()
    p1 = Player(screen, s.sprites(), s.__class__.__name__, 100, False, True, s.songs())
    p2 = Player(screen, n.sprites(), n.__class__.__name__, 820, True, False, n.songs())

    group_sprite.add(p1)
    group_sprite.add(p2)

    G = 16
    time = clock
    T = time.get_time() / 1000  # tempo em segundos
    F = G * T
    acceleration_y = 0
    acceleration_y2 = 0

    def damage_p1(dif_pos_right, dif_pos_left, dif_pos_y_p1, dif_pos_y_p2, damage):
        if (-10 > dif_pos_right > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[
            pygame.K_DOWN
        ] is False:
            if p2.life > 0:
                p2.life -= damage
                p2.damage()

        if (-10 > dif_pos_left > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[
            pygame.K_DOWN
        ] == False:
            if p2.life > 0:
                p2.life -= damage
                p2.damage()

    def damage_p2(dif_pos_right, dif_pos_left, dif_pos_y_p1, dif_pos_y_p2, damage):
        if (-10 > dif_pos_right > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[
            pygame.K_DOWN
        ] is False:
            if p1.life > 0:
                p1.life -= damage
                p1.damage()

        if (-10 > dif_pos_left > -60 and dif_pos_y_p1 == dif_pos_y_p2) and keys[
            pygame.K_DOWN
        ] == False:
            if p1.life > 0:
                p1.life -= 5
                p1.damage()

    def down(player, acceleration_y):
        player.rect.y += acceleration_y

        if player.rect.y > screen.get_height() / 2:
            player.rect.y = 360
            acceleration_y = 0
            time = pygame.time.Clock()

    while running:
        dif_pos_x_right = p2.rect.topleft[0] - p1.rect.topright[0]
        dif_pos_x_left = p1.rect.topleft[0] - p2.rect.topright[0]
        dif_pos_y_p1 = p1.rect.topright[1]
        dif_pos_y_p2 = p2.rect.topleft[1]

        acceleration_y += F
        acceleration_y2 += F

        down(p1, acceleration_y)
        down(p2, acceleration_y2)

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

        screen.fill(WHITE)

        group_sprite.draw(screen)
        group_sprite.update()

        # player 1
        font_p1 = pygame.font.Font(None, 30)
        name_p1 = font_p1.render(p1.name_character, True, (0, 0, 0))
        name_p1_rect = name_p1.get_rect(center=(135, 100))  # posicionar o texto na tela
        screen.blit(name_p1, name_p1_rect)  # desenhar o texto na tela
        # vida
        pygame.draw.rect(screen, "green", (100, 120, p1.life, 20), border_radius=5)
        # estamina
        pygame.draw.rect(screen, "blue", (100, 145, p1.stamina, 10), border_radius=5)

        # player 2
        font_p2 = pygame.font.Font(None, 30)
        name_p2 = font_p2.render(p2.name_character, True, (0, 0, 0))
        name_p2_rect = name_p2.get_rect(center=(735, 100))  # posicionar o texto na tela
        screen.blit(name_p2, name_p2_rect)  # desenhar o texto na tela
        # vida
        pygame.draw.rect(screen, "green", (700, 120, p2.life, 20), border_radius=5)
        # estamina
        pygame.draw.rect(screen, "blue", (700, 145, p2.stamina, 10), border_radius=5)

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            acceleration_y = p1.up()

        if keys[pygame.K_d] and p1.rect.y == screen.get_height() / 2:
            p1.right()

        if keys[pygame.K_a] and p1.rect.y == screen.get_height() / 2:
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
                damage_p1(
                    dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 1
                )

        if keys[pygame.K_UP]:
            acceleration_y2 = p2.up()

        if keys[pygame.K_RIGHT] and p2.rect.y == screen.get_height() / 2:
            p2.right()

        if keys[pygame.K_LEFT] and p2.rect.y == screen.get_height() / 2:
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
                damage_p2(
                    dif_pos_x_right, dif_pos_x_left, dif_pos_y_p1, dif_pos_y_p2, 1
                )

        clock.tick(30)

        if p1.life <= 0:
            p1_win = pygame.mixer.Sound("soundtracks/sasuke_ending.wav").play()
            if p1_win.get_busy() == 0:
                break

        if p2.life <= 0:
            p2_win = pygame.mixer.Sound("soundtracks/naruto_ending.wav").play()
            if p2_win.get_busy() == 0:
                break

    pygame.quit()


def song_game(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    song_game("soundtracks/opening4.mp3")

    WIDTH, HEIGHT = 980, 720
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    characters = [
        "Character1",
        "Character2",
        "Character3",
        "Character4",
        "Character5",
        "Character6",
    ]
    selected_characters = []  # Personagens selecionados

    # Estados do jogo
    states = {
        "menu": "menu",
        "select_characters": "select_characters",
        "battle": "battle",
    }

    current_screen = states["menu"]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    battle = True

    group_sprite = pygame.sprite.Group()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_screen == states["menu"]:
            current_screen = menu_screen()
        # elif current_screen == states["select_characters"]:
        #     current_screen = selection_screen()
        elif current_screen == states["battle"]:
            song = "soundtracks/naruto.mp3"
            pygame.mixer.Sound("soundtracks/opening_sasuke.wav").play()
            song_game(song)
            battle = battle_screen(True, clock=clock)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
