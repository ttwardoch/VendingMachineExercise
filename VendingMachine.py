from typing import Tuple
from which_coins_to_return import which_coins_to_return


class VendingMachine:
    """
    Once an item is selected and the appropriate amount of money is inserted,
        the vending machine should return the correct product.
    It should also return change if too much money is provided, or ask for more money
        if insufficient funds have been inserted.
    The machine should take an initial load of products and change. The change will be of denominations 1p, 2p, 5p, 10p,
        20p, 50p, £1, £2. There should be a way of reloading either products or change at a later point.
    The machine should keep the state of products and change that it contains up to date.
    """

    def __init__(self, item_dict: dict[str, dict[str, int]], coins_number: list[int]) -> None:
        """
        Initialise all variables, numer of coins, and items
        :param item_dict: dictionary of items, where key is name and value a dictionary with 2 keys: amount and price
                    e.g. {"ice": {"price": 77, "amount": 9}, "pepsi": {"price": 99, "amount": 15}}
        :param coins_number: 8 element list/tuple with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
                    e.g. [15, 22, 13, 9, 67, 5, 2, 5]
        """

        # Check if coins_number has proper length
        self.denominations_count = 8
        if len(coins_number) != self.denominations_count:
            raise ValueError(
                f"Expected list size of coins_number: {self.denominations_count}, but got {len(coins_number)}")

        self._item_dictionary: dict[str, dict[str, int]] = item_dict
        self._coins: list[int] = list(coins_number)
        self._coins_values: tuple[int, int, int, int, int, int, int, int] = (200, 100, 50, 20, 10, 5, 2, 1)
        self._inserted_coins: list[int] = [0, 0, 0, 0, 0, 0, 0, 0]
        self._value_inserted = 0
        self._chosen_item: str | None = None

    def choose_item(self, item_name: str) -> None:
        """
        Choose an item
        :param item_name: The name of an item in the VendingMachine
        :return:
        """
        if item_name not in self._item_dictionary.keys():
            raise ValueError(f"Item \"{item_name}\" does not exist")

        if self._item_dictionary[item_name]["amount"] == 0:
            raise ValueError(f"No {item_name} is left")

        self._chosen_item = item_name

    def insert_coin(self, coin_value: str) -> None:
        """
        Insert a coin into the Vending Machine
        :param coin_value: One value out of £2, £1, 50p, 20p, 10p, 5p, 2p, 1p
        :return:
        """
        match coin_value:
            case "1p":
                self._inserted_coins[7] += 1
                self._value_inserted += 1
            case "2p":
                self._inserted_coins[6] += 1
                self._value_inserted += 2
            case "5p":
                self._inserted_coins[5] += 1
                self._value_inserted += 5
            case "10p":
                self._inserted_coins[4] += 1
                self._value_inserted += 10
            case "20p":
                self._inserted_coins[3] += 1
                self._value_inserted += 20
            case "50p":
                self._inserted_coins[2] += 1
                self._value_inserted += 50
            case "£1":
                self._inserted_coins[1] += 1
                self._value_inserted += 100
            case "£2":
                self._inserted_coins[0] += 1
                self._value_inserted += 200
            case _:
                raise ValueError(f"No such coin")

    def submit(self) -> Tuple[str, list[int]]:
        """
        Check if enough money was inserted
        :exception: ValueError if not enough money inserted
        :exception: ValueError if it is impossible to give change
        :return: string representing the item, and an 8 element list of change [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]
        """
        if self._chosen_item is None:
            raise ValueError(
                f"Item not chosen: use VendingMachine.choose_item(item_name)")

        if self._value_inserted < self._item_dictionary[self._chosen_item]["price"]:
            expected_money = self._item_dictionary[self._chosen_item]["price"]
            raise ValueError(
                f"Not enough money inserted. Expected: £{expected_money / 100} Got: £{self._value_inserted / 100}")

        change_to_return: list[int] | None = self._return_change(
            self._value_inserted - self._item_dictionary[self._chosen_item]["price"])

        if change_to_return is None:
            raise ValueError(f"Impossible to give change")

        self._coins = [a + b - c for a, b, c in zip(self._coins, self._inserted_coins, change_to_return)]
        self._value_inserted = 0
        self._inserted_coins = [0, 0, 0, 0, 0, 0, 0, 0]

        returned_item = self._chosen_item
        self._item_dictionary[self._chosen_item]["amount"] -= 1
        self._chosen_item = None

        return returned_item, change_to_return

    def reload_change(self, coins_number: list[int]) -> None:
        """
        Add coins to the Vending Machine
        :param coins_number: 8 element list with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
        :return:
        """
        if len(coins_number) != self.denominations_count:
            raise ValueError(
                f"Expected list size of coins_number: {self.denominations_count}, but got {len(coins_number)}")

        self._coins = [a + b for a, b in zip(self._coins, coins_number)]

    def reload_items(self, item_dict: dict[str, int]) -> None:
        """
        Add items to the Vending Machine
        :param item_dict: dictionary of items, where key is name and value is amount
        :return:
        """
        for key in item_dict.keys():
            if key not in self._item_dictionary.keys():
                raise ValueError(f"Item {key} does not exist, nothing changed")

        for key, value in item_dict.items():
            self._item_dictionary[key]["amount"] += value

    def _return_change(self, value: int) -> None | list[int]:
        """
        Find which coins are available and return a list of coins to return given the constraint
        :param value: amount of change to return
        :return: 8 element list with number of coins of each type: [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]
        """

        total_number_of_coins = [a + b for a, b in zip(self._inserted_coins, self._coins)]
        list_of_return_coins = which_coins_to_return(value, total_number_of_coins, list(self._coins_values))

        return list_of_return_coins

    def __str__(self):
        """
        For print statement
        :return:
        """
        return f"Items in machine: {self._item_dictionary}\nCoin values [p]: {self._coins_values}\n" \
               f"Coins in machine: {self._coins}\nCoins inserted:   {self._inserted_coins}\n" \
               f"Value inserted [p]: {self._value_inserted}\nChosen item: {self._chosen_item}"


if __name__ == "__main__":
    VM = VendingMachine({"ice": {"price": 77, "amount": 9}, "pepsi": {"price": 99, "amount": 15}},
                        [15, 22, 13, 9, 67, 5, 2, 5])

    # Enough money
    print("When enough money: ")
    VM.choose_item("ice")
    VM.insert_coin("£1")
    try:
        item, change = VM.submit()
    except ValueError as e:
        print(e)
        item, change = None, None
    print(item, change)

    print("\nWhen not enough money: ")
    VM.choose_item("ice")
    VM.insert_coin("50p")
    try:
        item, change = VM.submit()
    except ValueError as e:
        print(e)
        item, change = None, None
    print(item, change)

    print("\nReloading 5 ice and 10 pepsi")
    VM.reload_items({"ice": 5, "pepsi": 10})

    print("\nReloading 50 1p coins")
    VM.reload_change([0, 0, 0, 0, 0, 0, 0, 50])

    print("\nCurrent state:")
    print(VM)
