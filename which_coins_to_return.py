def which_coins_to_return(value: int, total_number_of_coins: list[int], coins_values: list[int]) -> None | list[int]:
    """
    Recursive function that looks for a way to give change using minimum number of coins given limited number of coins
    :param value: Value to find change for in p
    :param total_number_of_coins: list with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
    :param coins_values: list with values of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins in p
    :return: list of coins needed for change
    """
    if len(total_number_of_coins) != len(coins_values):
        raise ValueError(f"total_number_of_coins and coins_values are different lengths")

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
