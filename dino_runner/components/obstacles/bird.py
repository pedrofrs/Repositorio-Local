import random


from dino_runner.components.obstacles.obstacle import Obstacle


HEIGHT_BIRD = [270,300]
class Bird(Obstacle):
   def __init__(self, image):
        self.type = 0
        self.index = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(HEIGHT_BIRD)

   def draw(self, screen):
       if self.index >= 10:
          self.index = 0
       screen.blit(self.image[self.index//5],self.rect)
       self.index += 1
        
       