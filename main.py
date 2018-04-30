import pygame

from pygame.locals import *


class App:

    def __init__(self):
        print("__init__")
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        print("on_init")
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        print("on_event")
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        print("on_loop")
        pass

    def on_render(self):
        print("on_render")
        pass

    def on_cleanup(self):
        print("on_cleanup")
        pygame.quit()

    def on_execute(self):
        print("on_execute")
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
