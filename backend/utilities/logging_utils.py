"""
This code is designed to set up the logging system in the application, ensuring that logs are written to the console and a file. Logs are used to track events, errors, and the general operation of the application.

Example:

    logger.info("Information message")

    logger.error("Error message")
"""

import logging


# Create a main logger named "app" and set the logging level to INFO
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Console handler: responsible for outputting logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

# File handler: responsible for writing logs to the file "app.log"
file_handler = logging.FileHandler("app.log", mode="a")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Add handlers (console and file) to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
