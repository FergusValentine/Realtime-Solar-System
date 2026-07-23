import pygame

class UserInput:
    def __init__(self, screen):
        self.mouse_pressed = False

        self.screen = screen
        self.start_pan = (0, 0)

    def process_input(self):
        is_running = True

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.mouse_pressed:
            offset_x = (mouse_x - self.start_pan[0]) / self.screen.camera.zoom
            offset_y = (mouse_y - self.start_pan[1]) / self.screen.camera.zoom
            self.screen.camera.move(-offset_x, -offset_y)

            self.start_pan = (mouse_x, mouse_y)

        mouse_x_before_zoom, mouse_y_before_zoom = self.screen.screen_to_world(mouse_x, mouse_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.mouse_pressed:
                    self.start_pan = (mouse_x, mouse_y)
                    self.mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.mouse_pressed:
                    self.mouse_pressed = False
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.screen.camera.zoom_in()
                elif event.y < 0:
                    self.screen.camera.zoom_out()

        mouse_x_after_zoom, mouse_y_after_zoom = self.screen.screen_to_world(mouse_x, mouse_y)

        self.screen.camera.move((mouse_x_before_zoom - mouse_x_after_zoom), (mouse_y_before_zoom - mouse_y_after_zoom))

        return is_running