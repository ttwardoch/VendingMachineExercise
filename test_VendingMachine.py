import pytest
from VendingMachine import VendingMachine


def test_vending_machine_general():
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [5, 5, 5, 5, 5, 5, 5, 5])
    assert VM._coins == [5, 5, 5, 5, 5, 5, 5, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._coins_values == (200, 100, 50, 20, 10, 5, 2, 1)
    assert VM._value_inserted == 0
    assert VM._chosen_item is None
    assert VM._item_dictionary == {"ice": {"price": 73, "amount": 5}}

    VM.choose_item("ice")
    assert VM._chosen_item is "ice"

    VM.insert_coin("£1")
    assert VM._coins == [5, 5, 5, 5, 5, 5, 5, 5]
    assert VM._inserted_coins == [0, 1, 0, 0, 0, 0, 0, 0]
    assert VM._value_inserted == 100

    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 1, 0, 1, 1, 0]

    assert VM._coins == [5, 6, 5, 4, 5, 4, 4, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._coins_values == (200, 100, 50, 20, 10, 5, 2, 1)
    assert VM._value_inserted == 0
    assert VM._chosen_item is None
    assert VM._item_dictionary == {"ice": {"price": 73, "amount": 4}}

    VM.choose_item("ice")
    assert VM._chosen_item is "ice"

    VM.insert_coin("50p")
    VM.insert_coin("50p")
    assert VM._value_inserted == 100
    assert VM._coins == [5, 6, 5, 4, 5, 4, 4, 5]
    assert VM._inserted_coins == [0, 0, 2, 0, 0, 0, 0, 0]

    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 1, 0, 1, 1, 0]

    assert VM._coins == [5, 6, 7, 3, 5, 3, 3, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._coins_values == (200, 100, 50, 20, 10, 5, 2, 1)
    assert VM._value_inserted == 0
    assert VM._chosen_item is None
    assert VM._item_dictionary == {"ice": {"price": 73, "amount": 3}}


def test_initialisation():
    # Check if shorter list raises exception
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1])

    # Check if longer list raises exception
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1, 1])

    # Check if state is as it should be
    VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
    assert VM._item_dictionary == {"ice": {"price": 50, "amount": 5}}
    assert VM._coins == [1, 1, 1, 1, 1, 1, 1, 1]
    assert VM._coins_values == (200, 100, 50, 20, 10, 5, 2, 1)
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._value_inserted == 0
    assert VM._chosen_item is None


def test_choose_item():
    # Check if exception is raised if the item does not exist
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.choose_item("iced")

    # Check if exception is raised if the item is out of stock
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 0}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.choose_item("ice")

    # Check if state is recorded
    VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
    VM.choose_item("ice")
    assert VM._chosen_item is "ice"


def test_insert_coin():
    # Check if exception is raised for wrong coin
    with pytest.raises(ValueError):
        VM = VendingMachine({"ice": {"price": 50, "amount": 5}}, [1, 1, 1, 1, 1, 1, 1, 1])
        VM.insert_coin("bleh")

    # Check if it is properly recorded in state
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

    # Check if the list goes from biggest to smallest
    VM.insert_coin("£2")
    assert VM._inserted_coins == [2, 1, 1, 1, 1, 1, 1, 1]


def test_submit():
    # Check general function
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [5, 5, 5, 5, 5, 5, 5, 5])
    VM.choose_item("ice")
    VM.insert_coin("£1")
    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 1, 0, 1, 1, 0]

    # Check if exception is raised if no item is chosen
    with pytest.raises(ValueError):
        item, change = VM.submit()

    # Check if exception is raised if not enough money is inserted
    VM.choose_item("ice")
    VM.insert_coin("50p")
    with pytest.raises(ValueError):
        item, change = VM.submit()

    # Check if exception is raised if impossible to return change
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [0, 0, 0, 0, 0, 0, 0, 0])
    VM.choose_item("ice")
    VM.insert_coin("£1")
    with pytest.raises(ValueError):
        item, change = VM.submit()

    # Check if state at the end is right
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [5, 5, 5, 5, 5, 5, 5, 5])
    VM.choose_item("ice")
    VM.insert_coin("£1")
    item, change = VM.submit()
    assert item == "ice"
    assert change == [0, 0, 0, 1, 0, 1, 1, 0]

    assert VM._coins == [5, 6, 5, 4, 5, 4, 4, 5]
    assert VM._inserted_coins == [0, 0, 0, 0, 0, 0, 0, 0]
    assert VM._coins_values == (200, 100, 50, 20, 10, 5, 2, 1)
    assert VM._value_inserted == 0
    assert VM._chosen_item is None
    assert VM._item_dictionary == {"ice": {"price": 73, "amount": 4}}


def test_reload_change():
    VM = VendingMachine({"ice": {"price": 40, "amount": 5}}, [0, 0, 1, 3, 0, 0, 0, 0])

    # Check if change is added
    VM.reload_change([1, 1, 1, 1, 1, 1, 1, 1])
    assert VM._coins == [1, 1, 2, 4, 1, 1, 1, 1]

    # Check if change is added to the right bins
    VM.reload_change([1, 1, 1, 1, 0, 0, 0, 0])
    assert VM._coins == [2, 2, 3, 5, 1, 1, 1, 1]


def test_reload_items():
    VM = VendingMachine({"ice": {"price": 40, "amount": 5}, "pepsi": {"price": 40, "amount": 5}}, [0, 0, 1, 3, 0, 0, 0, 0])

    # Check if the amount changes to right value
    VM.reload_items({"ice": 5})
    assert VM._item_dictionary["ice"]["amount"] == 10

    # Check if exception is raised if wrong item is loaded
    with pytest.raises(ValueError):
        VM.reload_items({"cola": 5})

    # Check if multiple items can be reloaded at once
    VM.reload_items({"ice": 5, "pepsi": 10})
    assert VM._item_dictionary["ice"]["amount"] == 15
    assert VM._item_dictionary["pepsi"]["amount"] == 15
