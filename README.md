# VendingMachineExercise
This repository contains a VendingMachine class keeping the state of products and change up to date.
It implements methods:
- .choose_item(item_name: str) - to choose an item
- .insert_coin(coin_value: str) - to insert pounds and pennies
- .submit() - to check if enough money was inserted and return the item and change
- .reload_change(coins_number: list[int]) - to reload coins to the machine
- .reload_items(item_dict: dict[str, int]) - to reload items to the machine
- .__str__() - To read internal state using print()

It is initialised using:

VendingMachine(item_dict: dict[str, dict[str, int]], coins_number: list[int])  
e.g. VM = VendingMachine({"ice": {"price": 77, "amount": 9}, "pepsi": {"price": 99, "amount": 15}}, [15, 22, 13, 9, 67, 5, 2, 5])  
to add 9 "ice" at a price of 77p, and 15 "pepsi" at a price of 99p to the machine, and a number of different coins: 15x£2, 22x£1, 13x50p, 9x20p, 67x10p, 5x5p, 2x2p, 5x1p

The change to give can be found using a recursive algorithm and a dynamic programming algorithm:
- recursive seems to be faster but may lead to stack overflow
- dynamic programming does not have this problem but seems to be slower for typical case
    
Currently, recursive algorithm is tried first, and only if it raises an error, the dynamic algorithm is used

VendingMachine class resides in VendingMachine.py and change algorithms are in which_coins_to_return.py  
Ale methods have tests implmented in test_VendingMachine.py and test_which_coins_to_return.py which should be used with pytest