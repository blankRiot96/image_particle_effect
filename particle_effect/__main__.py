import asyncio
import sys

from particle_effect.cli import consume_sys_args
from particle_effect.common import (SCREEN_FLAGS, SCREEN_SIZE,
                                    WINDOW_CAPTION_FORMAT, FPS_CAP)
from particle_effect.pg_config import pygame
from particle_effect.effect import SwayingFireParticleEffect


class App:
    def __init__(self) -> None:
        self._is_running = True
        self._screen = pygame.display.set_mode(SCREEN_SIZE, SCREEN_FLAGS)
        self._clock = pygame.time.Clock()
        self._photo = consume_sys_args(sys.argv)
        self._photo = pygame.transform.scale(self._photo, (250, 250))
        self._blit_photo = self._photo.copy()
        self._effect = SwayingFireParticleEffect(
            ("orange", "red"),
            self._blit_photo
        )

    def _update(self):
        dt = self._clock.tick(FPS_CAP) / 10

        fps = self._clock.get_fps()
        pygame.display.set_caption(WINDOW_CAPTION_FORMAT.format(fps=fps))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed!")
                self._is_running = False
        
        self._effect.update(dt)


    def _draw(self):
        self._screen.fill("white")
        self._blit_photo.fill("black")
        self._blit_photo.blit(self._photo, (0, 0))
        self._effect.draw()

        self._screen.blit(self._blit_photo, (0, 0))

    async def _run(self):
        print("Running...")
        while self._is_running:
            self._update()
            self._draw()

            pygame.display.flip()
            await asyncio.sleep(0)

    def run(self):
        asyncio.run(self._run())


if __name__ == "__main__":
    app = App()
    app.run()
