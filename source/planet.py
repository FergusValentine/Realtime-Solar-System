import math
from source.colours import COLOURS
from collections import deque

def get_distance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600*24

    def __init__(self, planet_data):
        self.name = planet_data["name"]
        self.x = float(planet_data["distance"]) * self.AU
        self.y = 0
        self.radius = float(planet_data["radius"])
        self.colour = COLOURS.get(planet_data["colour"], COLOURS["BLACK"])
        self.mass = float(planet_data["mass"]) * 10 ** float(planet_data["mass_exp"])
        self.x_velocity = 0
        self.y_velocity = float(planet_data["velocity"]) * 1000
        self.orbit = deque(maxlen=100)

    def get_position(self):
        return self.x, self.y

    def get_offset(self, neighbour):
        x1, y1 = self.get_position()
        x2, y2 = neighbour.get_position()

        return x2 - x1, y2 - y1

    def get_planet_attraction(self, neighbour):
        x_offset, y_offset = self.get_offset(neighbour)
        distance = get_distance(x_offset, y_offset)

        force = self.G * self.mass * neighbour.mass / distance ** 2
        theta = math.atan2(y_offset, x_offset)

        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update(self, planets):
        total_x: float = 0
        total_y: float = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.get_planet_attraction(planet)

            total_x += fx
            total_y += fy

        self.x_velocity += (total_x / self.mass) * self.TIMESTEP
        self.y_velocity += (total_y / self.mass) * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP

        self.orbit.append((self.x, self.y))
