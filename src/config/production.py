LOGGING_CONFIG = {
      "version": 1,
      "formatters":{
          "default": {
              "class": "logging.Formatter",
              "format": "LEVEL: %(levelname)s TIME: %(asctime)s FILENAMEL %(filename)s MODULE: %(module)s MESSAGES: %(message)s \n"
          },
          "slackFormatter": {
              "class": "src.utils.logger.SlackFormatter"
          }
       },
       "handlers" : {
           "console": {
               "class": "logging.StreamHandler",
               "level": "NOTSET",
               "formatter": "default"
           },
           "slack": {
               "class": "src.utils.logger.SlackHandler",
               "level": "ERROR",
               "formatter": "slackFormatter"
           },
           "file": {
               "class": "logging.FileHandler",
               "filename": "./src/logs/production.log",
               "level": "DEBUG",
               "formatter": "default"
           }
        },
        "loggers": {
            "": {
                "handlers": [
                   "console", "slack", "file"
                ],
                "level": "NOTSET"
            }
        }
    } 