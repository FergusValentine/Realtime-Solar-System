import pygame

from source.controller import SolarSystemController
from source.model import Model
from source.screen import Screen
from source.colours import COLOURS
from source.user_input import UserInput

ICON = pygame.image.load('source/icon.png')
TITLE = "Solar System Simulation"
WINDOW_SIZE = (800, 600)

class SolarSystemApplication:
    def __init__(self):
        self.window = None
        self.controller = None

    def create_window(self):
        pygame.display.set_icon(ICON)
        pygame.display.set_caption(TITLE)

        self.window = pygame.display.set_mode(WINDOW_SIZE)

    def create_app_components(self):
        model = Model()
        screen = Screen(self.window, COLOURS["BLACK"])
        user_input = UserInput(screen)

        self.controller = SolarSystemController(model, screen, user_input)

    def initialize(self):
        pygame.init()

        self.create_window()
        self.create_app_components()

    def run(self):
        self.controller.run()
        pygame.quit()

if __name__ == '__main__':
    application = SolarSystemApplication()
    application.initialize()
    application.run()

