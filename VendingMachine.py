class VendingMachine:
    item_dictionary: dict[str, int] = {}
    coins_values = [1, 2, 5, 10, 20, 50, 100, 200]
    coins_number: list[int] = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, item_dict: dict[str, int], coins_number: list[int]) -> None:
        """

        :param item_dict: dictionary of items, where key is name and value is price in p
        :param coins_number: 8 element list with number of 1p, 2p, 5p, 10p, 20p, 50p, £1, £2 coins
        """
        denominations_count = 8
        if len(coins_number) != denominations_count:
            raise ValueError(f"Expected list size of coins_number: {denominations_count}, but got {len(coins_number)}")

        self.item_dictionary = item_dict
        self.coins_number = coins_number


if __name__ == "__main__":
    VM = VendingMachine({"ice": 50}, [0, 0, 0, 0, 0, 0, 0, 0])
