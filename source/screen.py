import pygame

class Screen:
    def __init__(self, window, camera, colour):
        self.window = window
        self.camera = camera
        self.background_colour = colour

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

            pygame.draw.circle(self.window, planet.colour, (x, y), planet.radius * self.camera.zoom)

    def refresh(self):
        self.window.fill(self.background_colour)

    def world_to_screen(self, x, y):
        return (x - self.camera.x) * self.camera.zoom, (y - self.camera.y) * self.camera.zoom

    def screen_to_world(self, x, y):
        return (x/self.camera.zoom) + self.camera.x, (y / self.camera.zoom) + self.camera.y