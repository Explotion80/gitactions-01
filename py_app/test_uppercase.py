import pytest
from uppercase import to_upper

def test_to_uppercase():
    assert to_upper("hello") == "HELLO"
    assert to_upper("world") == "WORLD"
    assert to_upper("Python") == "PYTHON"
    assert to_upper("123abc") == "123ABC"
    assert to_upper("!@#") == "!@#"
    assert to_upper("") == ""

if __name__ == "__main__":
    pytest.main()