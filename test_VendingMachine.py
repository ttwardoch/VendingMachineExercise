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


def test_vending_machine():
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [5, 5, 5, 5, 5, 5, 5, 5])
    assert VM._coins == [5, 5, 5, 5, 5, 5, 5, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    VM.choose_item("ice")
    VM.insert_coin("£1")
    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 1, 0, 1, 1, 0]
    assert VM._coins == [5, 6, 5, 4, 5, 4, 4, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._value_inserted == 0
    assert VM._chosen_item is None

    VM = VendingMachine({"ice": {"price": 40, "amount": 5}}, [0, 0, 1, 3, 0, 0, 0, 0])
    VM.choose_item("ice")
    VM.insert_coin("£1")
    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 3, 0, 0, 0, 0]
    assert VM._coins == [0, 1, 1, 0, 0, 0, 0, 0]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._value_inserted == 0
    assert VM._chosen_item is None
