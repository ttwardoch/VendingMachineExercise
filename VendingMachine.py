from typing import Union, Tuple
from which_coins_to_return import which_coins_to_return


class VendingMachine:
    def __init__(self, item_dict: dict[str, dict[str, int]], coins_number: list[int]) -> None:
        """

        :param item_dict: dictionary of items, where key is name and value a dictionary with 2 keys: amount and price
        :param coins_number: 8 element list/tuple with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
        """

        # Check if coins_number has proper length
        denominations_count = 8
        if len(coins_number) != denominations_count:
            raise ValueError(f"Expected list size of coins_number: {denominations_count}, but got {len(coins_number)}")

        self._item_dictionary: dict[str, dict[str, int]] = item_dict
        self._coins: list[int] = list(coins_number)
        self._coins_values: tuple[int] = (200, 100, 50, 20, 10, 5, 2, 1)
        self._inserted_coins: list[int] = [0, 0, 0, 0, 0, 0, 0, 0]
        self._value_inserted = 0
        self._chosen_item = None

    def choose_item(self, item_name: str) -> None:
        if item_name not in self._item_dictionary.keys():
            raise ValueError(f"Item \"{item_name}\" does not exist")

        if self._item_dictionary[item_name]["amount"] == 0:
            raise ValueError(f"No {item_name} is left")

        self._chosen_item = item_name

    def insert_coin(self, coin_value: str) -> None:
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
        if self._value_inserted < self._item_dictionary[self._chosen_item]["price"]:
            expected_money = self._item_dictionary[self._chosen_item]["price"]
            raise ValueError(f"Not enough money inserted. Expected: £{expected_money/100} Got: £{self._value_inserted/100}")

        change_to_return: list[int] | None = self.return_change(self._value_inserted - self._item_dictionary[self._chosen_item]["price"])

        if change_to_return is None:
            raise ValueError(f"Impossible to give change")

        self._coins = [a+b-c for a, b, c in zip(self._coins, self._inserted_coins, change_to_return)]
        self._value_inserted = 0
        self._inserted_coins = [0, 0, 0, 0, 0, 0, 0, 0]

        returned_item = self._chosen_item
        self._item_dictionary[self._chosen_item]["amount"] -= 1
        self._chosen_item = None

        return returned_item, change_to_return

    def return_change(self, value: int) -> None | list[int]:

        total_number_of_coins = [a+b for a, b in zip(self._inserted_coins, self._coins)]
        list_of_return_coins = which_coins_to_return(value, total_number_of_coins, list(self._coins_values))

        return list_of_return_coins



if __name__ == "__main__":
    VM = VendingMachine({"ice": {"price": 73, "amount": 5}}, [5, 5, 5, 5, 5, 5, 5, 5])
    VM.choose_item("ice")
    VM.insert_coin("£1")
    print(VM._coins)
    item, change = VM.submit()
    print(change)
    print(VM._coins)
