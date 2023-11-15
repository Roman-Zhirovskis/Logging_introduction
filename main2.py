import logging
import requests

logging.basicConfig(level="DEBUG", filename='mylog.log')
logger = logging.getLogger()

for key in logging.Logger.manager.loggerDict:
    print(key)


def main(name: str) -> str:
    logger.debug(f'Enter in the main() function:name = {name}')
    r = requests.get('https://www.google.com/')
    print(r)


if __name__ == "__main__":
    main("Roman")
