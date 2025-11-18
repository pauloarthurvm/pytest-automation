from tools.base_tool import tool_health
import logging

logger = logging.getLogger(__name__)

def test_tool_health_001():
    # print("The first test")
    logger.info("Testing base tool")
    assert tool_health() == 1