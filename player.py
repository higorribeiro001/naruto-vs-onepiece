import pygame
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, list_sprites, name, position_x, left_atack, right_atack, songs):
        pygame.sprite.Sprite.__init__(self) # contrutor da classe Sprite
        self.screen = screen
        self.sprites_right = list_sprites[0]['sprites_right']
        self.sprites_left = list_sprites[1]['sprites_left']
        self.sprites_run_right = list_sprites[2]['sprites_run_right']
        self.sprites_run_left = list_sprites[3]['sprites_run_left']
        self.sprites_jump_left = list_sprites[4]['sprites_jump_left']
        self.sprites_jump_right = list_sprites[5]['sprites_jump_right']
        self.sprites_punch_right = list_sprites[6]['sprites_punch_right']
        self.sprites_punch_left = list_sprites[7]['sprites_punch_left']
        self.sprites_block_left = list_sprites[8]['sprites_block_left']
        self.sprites_block_right = list_sprites[9]['sprites_block_right']
        self.sprites_kick_left = list_sprites[10]['sprites_kick_left']
        self.sprites_kick_right = list_sprites[11]['sprites_kick_right']
        self.sprites_chakra_left = list_sprites[12]['sprites_chakra_left']
        self.sprites_chakra_right = list_sprites[13]['sprites_chakra_right']
        self.sprites_special_right = list_sprites[14]['sprites_special_right']
        self.sprites_special_left = list_sprites[15]['sprites_special_left']
        self.sprites_damage_right = list_sprites[16]['sprites_damage_right']
        self.sprites_damage_left = list_sprites[17]['sprites_damage_left']
        self.sprites_dead_left = list_sprites[18]['sprites_dead_left']
        self.sprites_dead_right = list_sprites[19]['sprites_dead_right']

        self.songs_punch = songs[0]['songs_punch']
        self.songs_kick = songs[1]['songs_kick']
        self.songs_chakra = songs[2]['songs_chakra']
        self.songs_damage = songs[3]['songs_damage']
        self.songs_dead = songs[4]['songs_dead']
        self.songs_special = songs[5]['songs_special']

        self.atual = 0

        self.left_atack = left_atack
        self.right_atack = right_atack
        
        if self.left_atack:
            self.image = self.sprites_left[self.atual]
        if self.right_atack:
            self.image = self.sprites_right[self.atual]
        
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

        self.rect = self.image.get_rect() # retangulo ao qual a imagem está alocada
        self.rect.topleft = position_x, self.screen.get_height() / 2 # onde vai ficar a parte superior esquerda do retangulo

        self.life = 200
        self.stamina = 0

        self.name_character = name

    def image_sprite_left(self, atual):
        self.image = self.sprites_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))
        self.right_atack = False
        self.left_atack = True

    def image_sprite_right(self, atual):
        self.image = self.sprites_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))
        self.left_atack = False
        self.right_atack = True

    def image_sprite_jump_left(self, atual):
        self.image = self.sprites_jump_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_jump_right(self, atual):
        self.image = self.sprites_jump_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_run_right(self, atual):
        self.image = self.sprites_run_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))
        
    def image_sprite_run_left(self, atual):
        self.image = self.sprites_run_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_punch_left(self, atual):
        self.image = self.sprites_punch_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_punch_right(self, atual):
        self.image = self.sprites_punch_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_block_left(self, atual):
        self.image = self.sprites_block_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_block_right(self, atual):
        self.image = self.sprites_block_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_kick_left(self, atual):
        self.image = self.sprites_kick_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_kick_right(self, atual):
        self.image = self.sprites_kick_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_chakra_left(self, atual):
        self.image = self.sprites_chakra_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))
    
    def image_sprite_chakra_right(self, atual):
        self.image = self.sprites_chakra_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_special_right(self, atual):
        self.image = self.sprites_special_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_special_left(self, atual):
        self.image = self.sprites_special_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_damage_right(self, atual):
        self.image = self.sprites_damage_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_damage_left(self, atual):
        self.image = self.sprites_damage_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40*2))

    def image_sprite_dead_left(self, atual):
        self.image = self.sprites_dead_left[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40))
        self.rect.y = self.screen.get_height() / 2 + 40

    def image_sprite_dead_right(self, atual):
        self.image = self.sprites_dead_right[atual]
        self.image = pygame.transform.scale(self.image, (30*2, 40))
        self.rect.y = self.screen.get_height() / 2 + 40

    def up(self):
        if self.rect.y >= 180:
            if self.atual > 1:
                self.atual = 1
            self.rect.y -= 12

            if self.right_atack:
                self.image_sprite_jump_right(int(self.atual))

            if self.left_atack:
                self.image_sprite_jump_left(int(self.atual))

            self.atual += 0.2
        else:
            self.down()

    def down(self):
        while self.rect.y != (self.screen.get_height() / 2):
            if self.atual > 2:
                self.atual = 1
            
            if self.right_atack:
                self.image_sprite_jump_right(int(self.atual))

            if self.left_atack:
                self.image_sprite_jump_left(int(self.atual))

            self.rect.y += 1
            self.atual += 0.3
        self.base()

    def left(self):
        if self.atual > 4:
            self.atual = 0
        
        self.image_sprite_run_left(int(self.atual))
        self.rect.x -= 8
        self.atual += 0.5

    def right(self):
        if self.atual > 4:
            self.atual = 0
        
        self.image_sprite_run_right(int(self.atual))
        self.rect.x += 8
        self.atual += 0.5

    def punch(self):
        if self.atual > 5:
            self.atual = 0
            
        if self.right_atack:
            self.image_sprite_punch_right(int(self.atual))

        if self.left_atack:
            self.image_sprite_punch_left(int(self.atual))

        pygame.mixer.Sound(self.songs_punch).play()

        self.atual += 0.3

    def kick(self):
        if self.atual > 2:
            self.atual = 0
        
        if self.right_atack:
            self.image_sprite_kick_right(int(self.atual))

        if self.left_atack:
            self.image_sprite_kick_left(int(self.atual))

        pygame.mixer.Sound(self.songs_kick).play()

        self.atual += 0.3

    def block(self):
        if self.right_atack:
            self.image_sprite_block_right(int(0))

        if self.left_atack:
            self.image_sprite_block_left(int(0))

    def chakra(self):
        if self.right_atack:
            self.image_sprite_chakra_right(int(0))

        if self.left_atack:
            self.image_sprite_chakra_left(int(0))

        if self.stamina < 200: 
            self.stamina += 0.5

        # pygame.mixer.Sound(self.songs_chakra).play()

    def special(self):
        if self.atual > 30:
            self.stamina -= 100
            self.atual = 0
        
        if self.right_atack:
            self.image_sprite_special_right(int(self.atual))

            if self.atual > 16 and self.atual < 23:
                self.rect.x += 10

        if self.left_atack:
            self.image_sprite_special_left(int(self.atual))

            if self.atual > 16 and self.atual < 23:
                self.rect.x -= 10

        if self.atual > 25:
            pygame.mixer.Sound(self.songs_special).play()

        self.atual += 0.2

    def dead(self):
        while self.atual < 3:
            if self.right_atack:
                self.image_sprite_dead_right(int(self.atual))

            if self.left_atack:
                self.image_sprite_dead_left(int(self.atual))

            pygame.mixer.Sound(self.songs_kick).play()

            self.atual += 0.3

    def base_left(self):
        self.atual = 0
        self.image_sprite_left(self.atual)

    def base_right(self):
        self.atual = 0
        self.image_sprite_right(self.atual)

    def base(self):
        self.atual = 0
        if self.right_atack == True:
            self.image_sprite_right(self.atual)

        if self.left_atack == True:
            self.image_sprite_left(self.atual)

    def damage(self):
        if self.atual > 2:
            self.atual = 0

        if self.right_atack:
            self.image_sprite_damage_right(int(self.atual))

        if self.left_atack:
            self.image_sprite_damage_left(int(self.atual))

        pygame.mixer.Sound(self.songs_damage).play()

        self.atual += 0.3
  
    def update(self):
        # if self.atual > 1:
        #     self.atual = 0
        # self.image_sprite(int(self.atual))
        # self.atual += 0.5
        ...