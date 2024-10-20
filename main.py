from VendingMachine import VendingMachine


VM = VendingMachine({"ice": {"price": 77, "amount": 1}, "pepsi": {"price": 99, "amount": 1}},
                        [15, 22, 13, 9, 7, 5, 2, 1])
print("")
while True:
    command = input("Choose command: choose_item, insert_coin, submit, insert_and_submit, state\n")
    if command == "choose_item" or command == "choose":
        item = input("Choose ice or pepsi: ")
        try:
            VM.choose_item(item)
        except ValueError as e:
            print(e)
    elif command == "insert_coin" or command == "insert":
        coin = input("Choose one coin from the list [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]: ")
        while True:
            try:
                VM.insert_coin(coin)
                break
            except ValueError as e:
                print(e)
    elif command == "submit":
        try:
            item, change = VM.submit()
            print(f"You got {item}")
            output = "Change: "
            for value, amount in zip(['£2', '£1', '50p', '20p', '10p', '5p', '2p', '1p'], change):
                if amount > 0:
                    output += f"{amount} x {value}, "
            print(output)
        except ValueError as e:
            print(e)
    elif command == "insert_and_submit":
        coin = input("Choose one coin from the list [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]: ")
        while True:
            try:
                VM.insert_coin(coin)
                break
            except ValueError as e:
                print(e)
        try:
            item, change = VM.submit()
            print(f"You got {item}")
            output = "Change: "
            for value, amount in zip(['£2', '£1', '50p', '20p', '10p', '5p', '2p', '1p'], change):
                if amount > 0:
                    output += f"{amount} x {value}, "
            print(output)
        except ValueError as e:
            print(e)
    elif command == "state":
        print(VM)
    else:
        print("Wrong command")
