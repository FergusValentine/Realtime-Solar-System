import csv

from typing import List
from source.planet import Planet

class Model:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24

    def __init__(self):
        self.planets: List[Planet] = []

    def load_planets(self, filename):
        with open(filename, 'r') as planets_file:
            csv_reader = csv.DictReader(planets_file)

            for planet_data in csv_reader:
                self.planets.append(Planet(planet_data))

    def update(self):
        for planet in self.planets:
            planet.update(self.planets)