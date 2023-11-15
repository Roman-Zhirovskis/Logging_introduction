import logging


# RootLogger determ.

logging.basicConfig(level=logging.INFO, filename='mylog.log')
# logging.basicConfig(
#     level=logging.WARNING,
#     format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(funcName)s: %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     filename='mylog.log'
# )
logger = logging.getLogger()

# app.logger
app_logger = logging.getLogger("app_logger")
console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)
app_logger.setLevel(logging.WARNING)

f = logging.Formatter(fmt="app-logger; %(levelname)s - %(name)s - %(message)s")
console_handler.setFormatter(f)

# print(app_logger)
print("Apphandler", app_logger.handlers)

# print('Root handlers', app_logger.parent.handlers)

# determinating utils_logger
utils_logger = logging.getLogger("app_logger.utils")
# utils_logger.setLevel(logging.DEBUG)
# utils_logger.parent.propagate = False

# print('utilsLogger', utils_logger)
# print(utils_logger.handlers)


def main():
    utils_logger.debug("Enter in the main() function:name = Roman")


if __name__ == "__main__":
    main()
