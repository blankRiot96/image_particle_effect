import pygame
from particle_effect.common import CLI_HELP_FORMAT, MAX_CLI_ARGS, CLI_ERROR_FORMAT


def _error_exit(msg):
    print(CLI_HELP_FORMAT)
    exit(CLI_ERROR_FORMAT.format(msg))

def consume_sys_args(sys_argv: list[str]) -> None:
    if len(sys_argv) > MAX_CLI_ARGS:
        _error_exit(
            f"We only support {MAX_CLI_ARGS} command line argument(s). "
            f"{len(sys_argv)} arguments provided."
        )
    
    file_name = sys_argv[1]
    try:
        image = pygame.image.load(file_name)
    except pygame.error:
        _error_exit(
            "Unsupported image format."
        )

    return image
