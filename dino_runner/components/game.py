import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.utils.text_utils import FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score_list = []

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw_score(self):
        text = self.text_creator(f"Score: {self.score}",22)
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit (text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # '#FFFFFF'
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def text_creator(self, text_creater,font_size):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(text_creater, True, (83,83,83))
        return text
        
    def menu_creator_center(self, text_input, y):
        if self.death_count == 0:
           secreen_fill = self.screen.fill((255, 255, 255))
        else:
            secreen_fill = None
        
        secreen_fill
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        text = self.text_creator(text_input, 22)
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + y)
        self.screen.blit(text, text_rect)
        
    def show_menu(self):
        if self.death_count == 0:
            self.menu_creator_center("Press any key to start", 0)
            
        else:
            self.menu_creator_center(f"Press any key to restart. Deaths: {self.death_count}. Score: {self.score}", -50)
            self.menu_creator_center(f"TOP SCORE: {max(self.score_list)} ", -100)
            self.screen.blit(GAME_OVER,( (SCREEN_HEIGHT/2)+ 50, SCREEN_HEIGHT/2))


       
        pygame.display.flip()  # .update()
        self.handle_events_on_menu()