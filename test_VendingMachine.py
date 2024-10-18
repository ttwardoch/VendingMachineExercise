import pytest
from VendingMachine import VendingMachine

def test_initialisation():
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": 50}, [1, 1, 1, 1, 1, 1, 1])