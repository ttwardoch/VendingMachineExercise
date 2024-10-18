import pytest
from VendingMachine import VendingMachine


def test_initialisation():
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1])
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1, 1])


def test_choose_item():
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.choose_item("iced")
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 0}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.choose_item("ice")

def test_insert_coin():
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.insert_coin("bleh")

    VM = VendingMachine({"ice": {"price": 50, "amount": 0}}, [1, 1, 1, 1, 1, 1, 1, 1])
    VM.insert_coin("1p")
    VM.insert_coin("2p")
    VM.insert_coin("5p")
    VM.insert_coin("10p")
    VM.insert_coin("20p")
    VM.insert_coin("50p")
    VM.insert_coin("£1")
    VM.insert_coin("£2")
    assert VM._inserted_coins == [1, 1, 1, 1, 1, 1, 1, 1]

    VM.insert_coin("£2")
    assert VM._inserted_coins == [2, 1, 1, 1, 1, 1, 1, 1]
