import pygame

class SolarSystemController:
    def __init__(self, model, screen, user_input):
        self.clock = pygame.time.Clock()

        self.model = model
        self.screen = screen
        self.user_input = user_input

        self.model.load_planets("planets.csv")

        self.is_running = True

    def handle_user_input(self):
        self.is_running = self.user_input.process_input()

    def update_solar_system(self):
        self.model.update()

    def draw_solar_system(self):
        self.screen.refresh()
        self.screen.draw(self.model)

        pygame.display.update()

    def run(self):
        while self.is_running:
            self.clock.tick(60)

            self.handle_user_input()
            self.update_solar_system()
            self.draw_solar_system()