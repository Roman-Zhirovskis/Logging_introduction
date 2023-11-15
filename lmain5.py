import json
import logging.config
import logging


def setup_json():
    with open("logging.json", "r") as f:
        json_config = json.load(f)
        logging.config.dictConfig(json_config)


def main():
    setup_json()


if __name__ == "__main__":
    main()
    logger = logging.getLogger(__name__)
    logger.info("hello world")
    logger.error("fatal error")
