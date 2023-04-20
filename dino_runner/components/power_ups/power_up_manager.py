import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.helli import Helly


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        power_up_type = [Shield(),Hammer(),Helly()]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(power_up_type[random.randint(0,2)])

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
        
            power_up_type = power_up.type  
            if game.player.dino_rect.colliderect(power_up.rect) :
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_up_game_changer(power_up_type,game)

                self.power_ups.remove(power_up)
        

    def power_up_game_changer(self, power_up_type, game):
        if power_up_type == 'helli':
            game.game_speed += 5
            game.player.dino_rect.y -= 80
        if power_up_type == 'shield':
            game.game_speed -= 5
             
            

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(20, 30)