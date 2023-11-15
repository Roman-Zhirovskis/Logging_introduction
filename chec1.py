import logging.config
import logging

from settings import logger_config


def main():

    logging.config.dictConfig(logger_config)
    logger = logging.getLogger("app_logger")
    logger.info("Enter in to the main()")


if __name__ == "__main__":
    main()
