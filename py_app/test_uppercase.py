import pytest
from uppercase import to_uppercase

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLOoo"
    assert to_uppercase("world") == "WORLD"
    assert to_uppercase("Python") == "PYTHON"
    assert to_uppercase("123abc") == "123ABC"
    assert to_uppercase("!@#") == "!@#"
    assert to_uppercase("") == ""

if __name__ == "__main__":
    pytest.main()