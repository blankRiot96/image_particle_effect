from particle_effect.pg_config import pygame
from dataclasses import dataclass
from typing import Sequence, Any
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
    def __init__(self, colors: Sequence, image: pygame.Surface) -> None:
        self._particle_colors = colors
        self._image = image
        self.particles: list[Particle] = []
        self.particle_gen_time = Time(0.1)
    
    def move_particle(self, particle, dt):
        """
        Move a particle in place.
        """

        particle.vel.y += 0.001 * dt
        delta_velocity = particle.vel.copy()
        delta_velocity.x *= dt
        delta_velocity.y *= dt
        particle.pos += delta_velocity
        particle.size -= particle.reduction

        if particle.size < 0:
            particle.alive = False

    def create_particle(self) -> Particle:
        if random.random() > 0.5:
            pos_x_range = (0, self._image.get_width())
            pos_y_range = (0, 1)
        else:
            pos_x_range = (0, 1)
            pos_y_range = (0, self._image.get_height())
        x_pos = random.randrange(*pos_x_range)
        y_pos = random.randrange(*pos_y_range)

        size_range = (3, 7)

        vel_x_range = (0.1, 0.7)
        vel_y_range = (0.3, 0.8)
        vel_x = random.uniform(*vel_x_range)
        vel_y = random.uniform(*vel_y_range)

        reduction_range = (0.01, 0.03)

        pos = pygame.Vector2(x_pos, y_pos)
        color = random.choice(self._particle_colors)
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
            self.particles.append(self.create_particle())

        for particle in list(self.particles):
            self.move_particle(particle, dt)

            if not particle.alive:
                self.particles.remove(particle)

    def draw(self):
        for particle in self.particles:
            base_rect = pygame.draw.circle(self._image, particle.color, particle.pos, particle.size)

            if particle.glow:
                glow_surf = circle_surf(particle.size + 1.8, (20, 20, 20))
                glow_rect = glow_surf.get_rect(center=base_rect.center)
                self._image.blit(glow_surf, glow_rect, special_flags=pygame.BLEND_RGB_ADD)

