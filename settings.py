logger_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "std_format": {
            "format": "{asctime} - {levelname} - {name} - {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "std_format",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "std_format",
            "filename": "estate.log",
        },
    },
    "loggers": {
        "app_logger": {
            "level": "DEBUG",
            "handlers": [
                "console",
                "file",
            ],
        }
    },
}
