import logging

logger = logging.getLogger(__name__)

def tool_health():
    # print(__name__)
    # print("You just called tool health.")
    logger.debug("tool health called")
    return 1