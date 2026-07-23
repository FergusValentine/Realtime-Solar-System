import pygame

class Screen:
    def __init__(self, window, colour):
        self.window = window
        self.background_colour = colour

        self.offset_x = -self.window.get_width() / 2
        self.offset_y = -self.window.get_height() / 2

        self.scale_x = 1
        self.scale_y = 1

    def draw(self, solar_system_model):
        planets = solar_system_model.planets

        for planet in planets:
            x, y = self.world_to_screen(planet.x * planet.SCALE, planet.y * planet.SCALE)

            if len(planet.orbit) > 2:
                updated_points = []

                for point in planet.orbit:
                    px, py = self.world_to_screen(point[0] * planet.SCALE, point[1] * planet.SCALE)
                    updated_points.append((px, py))

                pygame.draw.lines(self.window, planet.colour, False, updated_points, 1)

            pygame.draw.circle(self.window, planet.colour, (x, y), planet.radius * self.scale_x)

    def refresh(self):
        self.window.fill(self.background_colour)

    def world_to_screen(self, x, y):
        return (x - self.offset_x) * self.scale_x, (y - self.offset_y) * self.scale_y

    def screen_to_world(self, x, y):
        return (x/self.scale_x) + self.offset_x, (y / self.scale_y) + self.offset_y