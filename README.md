# VendingMachineExercise
This repository contains a **VendingMachine** class keeping the state of products and coins up to date.

It is initialised using:
- **VendingMachine(item_dict: dict[str, dict[str, int]], coins_number: list[int])** 
- e.g. **VM = VendingMachine({"ice": {"price": 77, "amount": 9}}, [15, 2, 13, 9, 6, 5, 2, 5])**  
adds 9 "ice" at a price of 77p to the machine, and a number of different coins: 15 x £2, 2 x £1, 13 x 50p, 9 x 20p, 6 x 10p, 5 x 5p, 2 x 2p, 5 x 1p

It implements methods:
- **.choose_item(item_name: str)** - to choose an item
- **.insert_coin(coin_value: str)** - to insert pounds and pennies
- **.submit()** - to check if enough money was inserted and return the item and change
- **.reload_change(coins_number: list[int])** - to reload coins to the machine
- **.reload_items(item_dict: dict[str, int])** - to reload items to the machine
- **.\_\_str\_\_()** - To read internal state using **print()**

The change to give can be found using a recursive algorithm and a dynamic programming algorithm:
- recursive seems to be faster but may lead to stack overflow
- dynamic programming does not have this problem but seems to be slower for a typical case
    
Currently, recursive algorithm is tried first, and only if it raises an error, the dynamic algorithm is used.

VendingMachine class resides in **VendingMachine.py** and change algorithms are in **which_coins_to_return.py**

All methods have tests implemented in **test_VendingMachine.py** and **test_which_coins_to_return.py** which should be used with **pytest**.