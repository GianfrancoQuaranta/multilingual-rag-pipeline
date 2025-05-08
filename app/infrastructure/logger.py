import logging

# Configure the base logger only if it hasn't been configured already
logger = logging.getLogger("app_logger")

if not logger.handlers:
    # Set up the logging format and level
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )

    logger.setLevel(logging.INFO)
