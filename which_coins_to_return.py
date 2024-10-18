def which_coins_to_return(value: int, total_number_of_coins: list[int], coins_values: list[int]) -> None | list[int]:
    # Stop the recurrence
    if value == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0]

    # Try to use all coins from biggest to smallest
    for i, (t, v) in enumerate(zip(total_number_of_coins, coins_values)):
        if value >= v and t >= 1:
            new_total_number_of_coins = total_number_of_coins.copy()
            new_total_number_of_coins[i] -= 1

            list_of_return_coins = which_coins_to_return(value-v, new_total_number_of_coins, coins_values)
            if list_of_return_coins is not None:
                list_of_return_coins[i] += 1
                return list_of_return_coins

    return None
