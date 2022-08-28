from particle_effect.pg_config import pygame
from dataclasses import dataclass
from typing import Any
from particle_effect.utils import Time, circle_surf
import random


@dataclass
class Particle:
    pos: pygame.Vector2
    color: Any
    size: Any 
    vel: pygame.Vector2
    reduction: float
    glow: bool = True
    alive: bool = True

class SwayingFireParticleEffect:
    def __init__(self, color, image: pygame.Surface) -> None:
        self._particle_color = color
        self._image = image.copy()
        self.particles: set[Particle] = set()
        self.particle_gen_time = Time(0.1)
    
    def move_particle(self, particle, dt):
        """
        Move a particle in place.
        """

        particle.vel.y += 0.01 * dt
        particle.pos += particle.vel * (dt, dt)
        particle.size -= particle.reduction

    def create_particle(self) -> Particle:
        pos_x_range = (0, self._image.get_width())
        pos_y_range = (0, self._image.get_height())
        x_pos = random.randrange(*pos_x_range)
        y_pos = random.randrange(*pos_y_range)

        colors = ("orange", "red", "yellow")
        
        size_range = (3, 7)

        vel_x_range = (0.5, 1.3)
        vel_y_range = (0.7, 1.5)
        vel_x = random.uniform(*vel_x_range)
        vel_y = random.uniform(*vel_y_range)

        reduction_range = (0.01, 0.03)

        pos = pygame.Vector2(x_pos, y_pos)
        color = random.choice(colors)
        size = random.uniform(*size_range)
        vel = pygame.Vector2(vel_x, vel_y)
        reduction = random.uniform(*reduction_range)

        return Particle(
            pos,
            color, 
            size,
            vel,
            reduction
        )

    def update(self, dt):
        # TODO: Generate particles
        if self.particle_gen_time.update():
            self.particles.add(self.create_particle())

        for particle in set(self.particles):
            self.move_particle(particle, dt)

            if not particle.alive:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            base_rect = pygame.draw.circle(screen, particle.color, particle.pos, particle.size)

            if particle.glow:
                glow_rect = pygame.Rect(base_rect.x, base_rect.y, base_rect.width + 1, base_rect.height + 1)
                screen.blit(circle_surf(glow_rect.width, (20, 20, 20)), glow_rect)

