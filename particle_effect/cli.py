from particle_effect.pg_config import pygame

from particle_effect.common import (CLI_ERROR_FORMAT, CLI_HELP_FORMAT,
                                    MAX_CLI_ARGS)


def _error_exit(msg):
    print(CLI_HELP_FORMAT)
    exit(CLI_ERROR_FORMAT.format(msg))


def consume_sys_args(sys_argv: list[str]) -> None:
    if len(sys_argv) > MAX_CLI_ARGS:
        _error_exit(
            f"We only support {MAX_CLI_ARGS} command line argument(s). "
            f"{len(sys_argv)} arguments provided."
        )
    
    if len(sys_argv) == 1:
        _error_exit(
            "Requires file_name argument."
        )

    file_name = sys_argv[1]
    try:
        image = pygame.image.load(file_name)
    except pygame.error:
        _error_exit("Unsupported image format.")
    except FileNotFoundError as e:
        _error_exit(e)

    return image
