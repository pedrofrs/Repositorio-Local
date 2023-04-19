import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.helli import Helli



class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        
        

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(100,200)
            choice =  2 #random.randint(0,2)
            if choice == 0:
                self.power_ups.append(Shield())
            elif choice ==1 :
                self.power_ups.append(Hammer())
            else: 
                self.power_ups.append(Helli())
                
    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            checker = power_up.type
            if game.player.dino_rect.colliderect(power_up.rect) and checker == "hammer":
                power_up.start_time = pygame.time.get_ticks()
                game.player.hammer = True 
                game.player.hammer
                game.player.shield
                game.player.has_power_up = True
                game.player.type = self.power_up.type
                self.power_up_check(self, game)
                game.player.power_up_time = self.power_up.start_time + (self.power_up.duration * 1000)
                self.power_ups.remove(self.power_up)
            if game.player.dino_rect.colliderect(power_up.rect) and checker == "shield":
                power_up.start_time = pygame.time.get_ticks()
                game.player.shield = True
                game.player.has_power_up = True
                game.player.type = self.power_up.type
                self.power_up_check(self, game)
                game.player.power_up_time = self.power_up.start_time + (self.power_up.duration * 1000)
                self.power_ups.remove(self.power_up)
    



    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)