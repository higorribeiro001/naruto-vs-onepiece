import pygame

class Naruto:
    def sprites(self):
        return [
            {
                'sprites_right': [
                    pygame.image.load('character_naruto/naruto_base/naruto_right2.png'),
                    pygame.image.load('character_naruto/naruto_base/naruto_right3.png'),
                ],
            },
            {
                'sprites_left': [
                    pygame.image.load('character_naruto/naruto_base/naruto_left2.png'),
                    pygame.image.load('character_naruto/naruto_base/naruto_left3.png'),
                ],
            },
            {
                'sprites_run_right': [
                    pygame.image.load('character_naruto/naruto_run/naruto_run_right1.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_right2.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_right1.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_right2.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_right1.png'),
                ],
            },
            {
                'sprites_run_left': [
                    pygame.image.load('character_naruto/naruto_run/naruto_run_left1.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_left2.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_left1.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_left2.png'),
                    pygame.image.load('character_naruto/naruto_run/naruto_run_left1.png'),
                ],
            },
            {
                'sprites_jump_left': [
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_left.png'),
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_left1.png'),
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_left2.png')
                ],
            },
            {
                'sprites_jump_right': [
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_right.png'),
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_right1.png'),
                    pygame.image.load('character_naruto/naruto_jump/naruto_jump_right2.png')
                ],
            },
            {
                'sprites_punch_right': [
                    pygame.image.load('character_naruto/naruto_punch/naruto_punch_right1.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_punch_right2.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_right1.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_right2.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_right3.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_right4.png'),
                ],
            },
            {
                'sprites_punch_left': [
                    pygame.image.load('character_naruto/naruto_punch/naruto_punch_left1.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_punch_left2.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_left1.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_left2.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_left3.png'),
                    pygame.image.load('character_naruto/naruto_punch/naruto_head_left4.png'),
                ],
            },
            {
                'sprites_block_left': [
                    pygame.image.load('character_naruto/naruto_block/naruto_block_left.png'),
                ],
            },
            {
                'sprites_block_right': [
                    pygame.image.load('character_naruto/naruto_block/naruto_block_right.png'),
                ],
            },
            {
                'sprites_kick_left': [
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_left1.png'),
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_left2.png'),
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_left3.png'),
                ],
            },
            {
                'sprites_kick_right': [
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_right1.png'),
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_right2.png'),
                    pygame.image.load('character_naruto/naruto_kick/naruto_kick_right3.png'),
                ],
            },
            {
                'sprites_chakra_left': [
                    pygame.image.load('character_naruto/naruto_chakra/naruto_chakra_left.png'),
                ],
            },
            {
                'sprites_chakra_right': [
                    pygame.image.load('character_naruto/naruto_chakra/naruto_chakra_right.png'),
                ]
            },
            {
                'sprites_special_right': [
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right1.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right2.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right3.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right4.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right5.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right6.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right7.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right8.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right9.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right10.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right11.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right12.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right13.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right14.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right15.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right16.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right17.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right18.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right19.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right20.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right21.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right22.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right23.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right24.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right25.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right26.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right27.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right28.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right29.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right30.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_right31.png'),
                ]
            },
            {
                'sprites_special_left': [
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left1.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left2.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left3.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left4.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left5.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left6.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left7.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left8.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left9.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left10.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left11.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left12.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left13.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left14.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left15.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left16.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left17.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left18.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left19.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left20.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left21.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left22.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left23.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left24.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left25.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left26.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left27.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left28.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left29.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left30.png'),
                    pygame.image.load('character_naruto/naruto_special/naruto_special_left31.png'),
                ]
            },
            {
                'sprites_damage_right': [
                    pygame.image.load('character_naruto/naruto_damage/naruto_damage_right1.png'),
                    pygame.image.load('character_naruto/naruto_damage/naruto_damage_right2.png'),
                    pygame.image.load('character_naruto/naruto_base/naruto_right2.png'),
                ]
            },
            {
                'sprites_damage_left': [
                    pygame.image.load('character_naruto/naruto_damage/naruto_damage_left1.png'),
                    pygame.image.load('character_naruto/naruto_damage/naruto_damage_left2.png'),
                    pygame.image.load('character_naruto/naruto_base/naruto_left2.png'),
                ]
            },
            {
                'sprites_dead_left': [
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_left1.png'),
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_left2.png'),
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_left3.png'),
                ]
            },
            {
                'sprites_dead_right': [
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_right1.png'),
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_right2.png'),
                    pygame.image.load('character_naruto/naruto_dead/naruto_dead_right3.png'),
                ]
            }
        ]