

# Generated at 2026-11-03 01:43:52.345815
# Unit test for function compare
def test_compare():
    # Both lists identical -> all differences are 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Simple positive differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Absolute value handles reversed order (guess smaller than game)
    assert module_0.compare([4, 5, 6], [1, 2, 3]) == [3, 3, 3]

    # Mixed differences
    assert module_0.compare([1, 5, 10], [2, 3, 7]) == [1, 2, 3]

    # Negative numbers
    assert module_0.compare([-1, -5, -10], [1, 5, 10]) == [2, 10, 20]

    # Empty lists -> empty result
    assert module_0.compare([], []) == []

    # Single element lists
    assert module_0.compare([0], [0]) == [0]
    assert module_0.compare([7], [3]) == [4]

    # Result length matches input length
    game = [0, 1, 2, 3, 4]
    guess = [4, 3, 2, 1, 0]
    result = module_0.compare(game, guess)
    assert len(result) == len(game)
    assert result == [4, 2, 0, 2, 4]

# Generated at 2026-11-03 01:45:28.616686
# Unit test for function compare
def test_compare():import pytest
from solution import compare  # adjust import as needed


def test_compare_identical_lists():
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]


def test_compare_guess_lower():
    assert module_0.compare([5, 10, 15], [3, 8, 12]) == [2, 2, 3]


def test_compare_guess_higher():
    assert module_0.compare([3, 8, 12], [5, 10, 15]) == [2, 2, 3]


def test_compare_mixed_differences():
    assert module_0.compare([1, 5, 9], [4, 2, 9]) == [3, 3, 0]


def test_compare_with_zeros():
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]


def test_compare_single_element():
    assert module_0.compare([7], [4]) == [3]


def test_compare_empty_lists():
    assert module_0.compare([], []) == []


def test_compare_negative_numbers():
    assert module_0.compare([-1, -5, -3], [-4, -2, -3]) == [3, 3, 0]


def test_compare_result_uses_absolute_value():
    result = module_0.compare([1, 1, 1], [10, 10, 10])
    assert all(diff >= 0 for diff in result)
    assert result == [9, 9, 9]


def test_compare_lengths_must_match():
    # zip truncates to the shorter list
    assert module_0.compare([1, 2, 3], [10]) == [9]

# Generated at 2026-11-03 01:46:54.953083
# Unit test for function compare
def test_compare():
# nonce:d1c7cc28
    # Test with typical game/guess pairs
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert module_0.compare([0, 5, 0, 5, 0], [0, -1, -3, -3, -1]) == [0, 6, 3, 8, 1]
    
    # Test exact matches (all zeros)
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    
    # Test single elements
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([1], [4]) == [3]
    
    # Test empty lists
    assert module_0.compare([], []) == []
    
    # Test negative numbers
    assert module_0.compare([-1, -2, -3], [-3, -4, -5]) == [2, 2, 2]
    assert module_0.compare([-5, 0], [5, 0]) == [10, 0]
    
    # Test symmetric differences
    assert module_0.compare([10, 20, 30], [5, 25, 35]) == [5, 5, 5]
    assert module_0.compare([100], [50]) == [50]
    
    # Test result is always non-negative
    result = module_0.compare([3, 7, 1], [9, 2, 8])
    assert all(x >= 0 for x in result)
    assert result == [6, 5, 7]

# Generated at 2026-11-03 01:48:29.649749
# Unit test for function compare
def test_compare():import pytest
from solution import compare


def test_all_correct_guesses():
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]


def test_all_wrong_guesses():
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]


def test_mixed_results():
    assert module_0.compare([1, 2, 3, 4], [1, 3, 2, 4]) == [0, 1, 1, 0]


def test_empty_lists():
    assert module_0.compare([], []) == []


def test_single_element():
    assert module_0.compare([5], [3]) == [2]


def test_negative_numbers():
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]


def test_absolute_difference_order():
    assert module_0.compare([10, 20, 30], [5, 25, 15]) == [5, 5, 15]


def test_zero_values():
    assert module_0.compare([0, 0], [0, 1]) == [0, 1]


def test_large_numbers():
    assert module_0.compare([1000000], [999999]) == [1]


def test_float_values():
    assert module_0.compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]


def test_returns_list_type():
    result = module_0.compare([1, 2], [1, 2])
    assert isinstance(result, list)


def test_result_length_matches_input():
    game = [1, 2, 3, 4, 5]
    guess = [5, 4, 3, 2, 1]
    result = module_0.compare(game, guess)
    assert len(result) == len(game)


# nonce:8222c71f

# Generated at 2026-11-03 01:49:53.934726
# Unit test for function compare
def test_compare():
    # Test with identical values (all differences should be 0)
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with all guesses too low
    assert module_0.compare([1, 2, 3], [0, 1, 2]) == [1, 1, 1]

    # Test with all guesses too high
    assert module_0.compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1]

    # Test with mixed higher/lower guesses
    assert module_0.compare([1, 2, 3], [3, 0, 5]) == [2, 2, 2]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with larger numbers
    assert module_0.compare([10, 20, 30], [5, 25, 35]) == [5, 5, 5]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

    # Test with single element
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [8]) == [3]