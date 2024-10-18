from which_coins_to_return import which_coins_to_return

def test_which_coins_to_return():
    assert None is which_coins_to_return(100, [0, 0, 1, 3, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1])
    assert None is which_coins_to_return(100, [0, 0, 0, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 1, 1, 0, 1, 1, 1] == which_coins_to_return(78, [0, 0, 1, 1, 0, 1, 1, 1], [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 0, 3, 0, 0, 0, 0] == which_coins_to_return(60, [0, 1, 1, 3, 0, 1, 1, 1],
                                                             [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 0, 0, 1, 0, 0, 50] == which_coins_to_return(60, [5, 5, 0, 0, 1, 0, 0, 50],
                                                             [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 0, 0, 0, 0, 3, 0] == which_coins_to_return(6, [0, 0, 0, 0, 0, 1, 3, 0],
                                                              [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 0, 0, 0, 1, 0, 0] == which_coins_to_return(5, [0, 0, 0, 0, 0, 1, 3, 0],
                                                             [200, 100, 50, 20, 10, 5, 2, 1])
    assert None is which_coins_to_return(5000, [0, 0, 0, 0, 0, 1, 3, 0],
                                                             [200, 100, 50, 20, 10, 5, 2, 1])
    assert None is which_coins_to_return(60, [0, 0, 12, 0, 0, 0, 0, 0],
                                         [200, 100, 50, 20, 10, 5, 2, 1])
    assert [0, 0, 1, 0, 1, 0, 0, 0] == which_coins_to_return(60, [0, 0, 12, 0, 1, 0, 0, 0],
                                         [200, 100, 50, 20, 10, 5, 2, 1])