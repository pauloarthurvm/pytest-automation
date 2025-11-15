from tools.base_tool import tool_health

def test_tool_health_001():
    print("The first test")
    assert tool_health() == 1