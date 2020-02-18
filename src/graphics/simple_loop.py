import pygame
from physics import Particle, Vector
import graphics.colors as colors

WIDTH = 600
HEIGHT = 600


class GraphicsWorkshop:
    def __init__(self):
        self.clock = None
        self.screen = None

    def run(self):
        self._init_pygame()
        self._loop()

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def _loop(self):
        particle = Particle(Vector(WIDTH/2, 0, 0), Vector(0,0,0), Vector(0, 10e-4, 0), 0.99, 10)
        self.clock.tick()
        while True:
            tick = self.clock.tick()
            particle.integrate(tick)
            self._draw(particle)

    def _draw(self, particle: Particle):
        self.screen.fill(colors.BLACK)
        self.screen.fill(colors.RED, pygame.Rect(particle.position.x, particle.position.y, 10, 10))
        pygame.display.flip()


if __name__ == "__main__":
    GraphicsWorkshop().run()
