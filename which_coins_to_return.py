def which_coins_to_return(value: int, total_number_of_coins: list[int], coins_values: list[int], algorithm='default')\
        -> None | list[int]:
    """
    Function that looks for a way to give change using minimum number of coins given limited number of coins

    :param value: Value to find change for in p
    :param total_number_of_coins: list with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
    :param coins_values: list with values of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins in p
    :param algorithm: "default" to let the function decide, "recursive" for recursive, "dynamic" for dynamic
    :return: list of coins needed for change
    """
    # Chose an algorithm if specified
    if algorithm == "recursive":
        return which_coins_to_return_recursive(value, total_number_of_coins, coins_values)
    elif algorithm == "dynamic":
        return which_coins_to_return_dynamic(value, total_number_of_coins, coins_values)

    # Try recursion, if RecursionError, use dynamic programming
    try:
        return which_coins_to_return_recursive(value, total_number_of_coins, coins_values)
    except RecursionError:
        return which_coins_to_return_dynamic(value, total_number_of_coins, coins_values)


def which_coins_to_return_recursive(value: int, total_number_of_coins: list[int], coins_values: list[int])\
        -> None | list[int]:
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

            # See if it is possible to get change - coin_value using remaining coins
            list_of_return_coins = which_coins_to_return(value-v, new_total_number_of_coins, coins_values)
            if list_of_return_coins is not None:
                list_of_return_coins[i] += 1
                return list_of_return_coins

    return None


def which_coins_to_return_dynamic(change: int, total_number_of_coins: list[int], coins_values: list[int])\
        -> None | list[int]:
    """
    Dynamic programming function that looks for a way to give change using minimum number of coins
            given limited number of coins.

    Complexity: O(change * number_of_coins)

    :param change: Value to find change for in p
    :param total_number_of_coins: list with number of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins
    :param coins_values: list with values of [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p] coins in p
    :return: list of coins needed for change
    """
    if len(total_number_of_coins) != len(coins_values):
        raise ValueError(f"total_number_of_coins and coins_values are different lengths")

    # Create a list to store ways to get all changes from 0 to change, 0 and change inclusive
    all_values: list[list[int] | None] = [None for _ in range(change + 1)]
    all_values[0] = [0, 0, 0, 0, 0, 0, 0, 0]

    # Loop over all coins, two loops needed for that
    for i, (coin_value, coin_amount) in enumerate(zip(coins_values, total_number_of_coins)):
        if coin_amount == 0:
            continue
        for _ in range(coin_amount):

            # Loop over all values from the end and update possible way to obtain change changes
            for j in range(change-coin_value, -1, -1):
                if all_values[j] is None:
                    continue
                elif all_values[j+coin_value] is None:
                    all_values[j + coin_value] = all_values[j].copy()
                    all_values[j + coin_value][i] += 1
                elif sum(all_values[j+coin_value]) > sum(all_values[j]) + 1:
                    all_values[j + coin_value] = all_values[j].copy()
                    all_values[j + coin_value][i] += 1

    return all_values[-1]


if __name__ == "__main__":
    import time

    # For function timing
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()  # Record the start time
            result = func(*args, **kwargs)  # Execute the function
            end_time = time.time()  # Record the end time
            print(f"Execution time: {end_time - start_time:.6f} seconds")
            return result  # Return the result of the function

        return wrapper


    @timer_decorator
    def time_rec():
        for i in range(1000):
            which_coins_to_return_recursive(60, [5, 5, 0, 0, 1, 0, 0, 50],
                                            [200, 100, 50, 20, 10, 5, 2, 1])

    @timer_decorator
    def time_dyn():
        for i in range(1000):
            which_coins_to_return_dynamic(60, [5, 5, 0, 0, 1, 0, 0, 50],
                                          [200, 100, 50, 20, 10, 5, 2, 1])


    time_rec()
    time_dyn()
