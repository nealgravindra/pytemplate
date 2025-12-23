"""{{cookiecutter.__clean_slug}}."""

from {{cookiecutter.__clean_slug}}.logging import configure_logging, logger


def main() -> None:
    """Run the application."""
    configure_logging()
    logger.info("Hello, World!")


if __name__ == "__main__":
    main()
