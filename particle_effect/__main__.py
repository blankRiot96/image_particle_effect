from particle_effect.pg_config import pygame
import asyncio
import sys
from particle_effect.common import SCREEN_SIZE, SCREEN_FLAGS, WINDOW_CAPTION_FORMAT
from particle_effect.cli import consume_sys_args


class App:
    def __init__(self) -> None:
        self._is_running = True
        self._screen = pygame.display.set_mode(SCREEN_SIZE, SCREEN_FLAGS)
        self._clock = pygame.time.Clock()
        consume_sys_args(sys.argv)

    def _update(self):
        fps = self._clock.get_fps()
        pygame.display.set_caption(WINDOW_CAPTION_FORMAT.format(fps=fps))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed!")
                self._is_running = False
        
        self._clock.tick()

    def _draw(self):
        self._screen.fill("white")

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

