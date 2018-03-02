from gpb_app import app

from logging.config import dictConfig
from gpb_app.logly.logging_config import logging_config

dictConfig(logging_config)

if __name__ == '__main__':
    app.run(debug=True, port=33507)
