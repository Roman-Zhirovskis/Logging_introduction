logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": "logs/real_estate.log",
        },
    },
    "loggers": {
        # "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
        "apps": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
    },
}
