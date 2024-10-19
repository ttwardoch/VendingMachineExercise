from which_coins_to_return import which_coins_to_return, which_coins_to_return_recursive, which_coins_to_return_dynamic
import pytest

params = [
    (None, 100, [0, 0, 1, 3, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    (None, 100, [0, 0, 0, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    (None, 5000, [0, 0, 0, 0, 0, 1, 3, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    (None, 60, [0, 0, 12, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 1, 1, 0, 1, 1, 1], 78, [0, 0, 1, 1, 0, 1, 1, 1], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 0, 0, 0, 0, 0, 0], 0, [0, 0, 1, 1, 0, 1, 1, 1], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 0, 3, 0, 0, 0, 0], 60, [0, 1, 1, 3, 0, 1, 1, 1], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 0, 0, 1, 0, 0, 50], 60, [5, 5, 0, 0, 1, 0, 0, 50], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 0, 0, 0, 0, 3, 0], 6, [0, 0, 0, 0, 0, 1, 3, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 0, 0, 0, 1, 0, 0], 5, [0, 0, 0, 0, 0, 1, 3, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
    ([0, 0, 1, 0, 1, 0, 0, 0], 60, [0, 0, 12, 0, 1, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1]),
]


@pytest.mark.parametrize("output, v, t, c", params)
def test_which_coins_to_return(output, v, t, c):
    # Test equal length of lists
    with pytest.raises(ValueError):
        which_coins_to_return(100, [0, 0, 0, 0, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1])

    assert output == which_coins_to_return(v, t, c)


@pytest.mark.parametrize("output, v, t, c", params)
def test_which_coins_to_return_recursive(output, v, t, c):
    # Test equal length of lists
    with pytest.raises(ValueError):
        which_coins_to_return_recursive(100, [0, 0, 0, 0, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1])

    assert output == which_coins_to_return_recursive(v, t, c)


@pytest.mark.parametrize("output, v, t, c", params)
def test_which_coins_to_return_dynamic(output, v, t, c):
    # Test equal length of lists
    with pytest.raises(ValueError):
        which_coins_to_return_dynamic(100, [0, 0, 0, 0, 0, 0, 0, 0, 0], [200, 100, 50, 20, 10, 5, 2, 1])

    assert output == which_coins_to_return_dynamic(v, t, c)