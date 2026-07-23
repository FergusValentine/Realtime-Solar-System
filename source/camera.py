class Camera:
    def __init__(self, width, height):
        self.x = -width / 2
        self.y = -height / 2

        self.zoom: float = 1.0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def zoom_in(self):
        self.zoom *= 1.1

    def zoom_out(self):
        self.zoom *= 0.9