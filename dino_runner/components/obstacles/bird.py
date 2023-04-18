import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
  

HEIGHT_BIRD = [270,300]
class Bird(Obstacle):
   def __init__(self):
        self.type = 0
        self.index = 0
        super().__init__(BIRD, self.type)
        self.rect.y = random.choice(HEIGHT_BIRD)

   def draw(self, screen):
       screen.blit(self.image[self.index//5],self.rect)
       self.index += 1
       
       if self.index >= 9:
          self.index = 0
        
       