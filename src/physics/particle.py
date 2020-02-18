from .vector import Vector


class Particle:
    def __init__(self, position, velocity, acceleration, damping, mass, g=10e-2):
        # position, velocity, acceleration are all Vectors
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        # simulates drag
        self.damping = damping
        # acceleration is calculated based on F=ma
        # a = (1/m)F
        # Storing 1/m makes the code faster and lets us
        # simulate infinite mass (inverse mass <= 0)
        self.inverse_mass = 1/mass
        self.m = mass
        self.gravity = Vector(0, -g, 0)

    def integrate(self, delta_time):
        """
        Apply update after time has gone on
        :param delta_time:
        :return:
        """
        # infinite mass things don't move
        if self.inverse_mass <= 0:
            return
        self.position += self.velocity * delta_time
        self.velocity = self.velocity * pow(self.damping, delta_time) + self.acceleration * delta_time
