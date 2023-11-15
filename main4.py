import logging.config
import logging

from settings2 import logger_config


def main():

    logging.config.dictConfig(logger_config)
    logger = logging.getLogger("apps")
    logger.warning("Enter in to the main()")


if __name__ == "__main__":
    main()
