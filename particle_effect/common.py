
from tkinter.tix import MAX


SCREEN_SIZE = 750, 380
SCREEN_FLAGS = 0

WINDOW_CAPTION_FORMAT = "Particle Effect Generator | {fps:.0f}"
CLI_HELP_FORMAT = """
USAGE: python -m image_particle_effect [file_name]
Your file can be of any of the supported types:
.png
.jpeg
"""
CLI_ERROR_FORMAT = "Error: {0}"

# The module name is counted as one arg.
MAX_CLI_ARGS = 2

