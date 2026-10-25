

# Generated at 2026-10-24 07:07:43.231175
# Unit test for function sort_array
def test_sort_array():import random
import pytest

from solution import sort_array  # adjust to your module name


def popcount(x: int) -> int:
    return bin(x)[2:].count("1")


def reference(arr):
    """Sort by popcount asc, ties broken by value asc (stable-sort semantics)."""
    return sorted(arr, key=lambda x: (popcount(x), x))


def test_empty():
    assert module_0.sort_array([]) == []


def test_single_element():
    assert module_0.sort_array([42]) == [42]


def test_orders_by_popcount_then_value():
    # popcount 1: 1,2,4 | popcount 2: 3,5
    assert module_0.sort_array([5, 3, 2, 4, 1]) == [1, 2, 4, 3, 5]


def test_input_order_does_not_matter():
    assert module_0.sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]


def test_duplicates_preserved():
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_zero_and_powers_of_two():
    # 0 has popcount 0 and comes first; 1,2,4,8 all have popcount 1
    assert module_0.sort_array([8, 0, 4, 2, 1]) == [0, 1, 2, 4, 8]


def test_does_not_mutate_input():
    data = [7, 1, 4]
    original = list(data)
    module_0.sort_array(data)
    assert data == original


def test_matches_reference_on_range():
    data = list(range(0, 200))
    random.Random(0).shuffle(data)
    assert module_0.sort_array(data) == reference(data)


def test_matches_reference_on_random_inputs():
    rng = random.Random(1234)
    for _ in range(50):
        data = [rng.randint(0, 5000) for _ in range(rng.randint(0, 30))]
        assert module_0.sort_array(data) == reference(data)

# Generated at 2026-10-24 07:07:44.534863
# Unit test for function sort_array
def test_sort_array():import random
import pytest

from solution import sort_array  # adjust to your module name


def popcount(x: int) -> int:
    return bin(x)[2:].count("1")


def reference(arr):
    """Sort by popcount asc, ties broken by value asc (stable-sort semantics)."""
    return sorted(arr, key=lambda x: (popcount(x), x))


def test_empty():
    assert module_0.sort_array([]) == []


def test_single_element():
    assert module_0.sort_array([42]) == [42]


def test_orders_by_popcount_then_value():
    # popcount 1: 1,2,4 | popcount 2: 3,5
    assert module_0.sort_array([5, 3, 2, 4, 1]) == [1, 2, 4, 3, 5]


def test_input_order_does_not_matter():
    assert module_0.sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]


def test_duplicates_preserved():
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_zero_and_powers_of_two():
    # 0 has popcount 0 and comes first; 1,2,4,8 all have popcount 1
    assert module_0.sort_array([8, 0, 4, 2, 1]) == [0, 1, 2, 4, 8]


def test_does_not_mutate_input():
    data = [7, 1, 4]
    original = list(data)
    module_0.sort_array(data)
    assert data == original


def test_matches_reference_on_range():
    data = list(range(0, 200))
    random.Random(0).shuffle(data)
    assert module_0.sort_array(data) == reference(data)


def test_matches_reference_on_random_inputs():
    rng = random.Random(1234)
    for _ in range(50):
        data = [rng.randint(0, 5000) for _ in range(rng.randint(0, 30))]
        assert module_0.sort_array(data) == reference(data)

# Generated at 2026-10-24 07:07:45.834942
# Unit test for function sort_array
def test_sort_array():import random
import pytest

from solution import sort_array  # adjust to your module name


def popcount(x: int) -> int:
    return bin(x)[2:].count("1")


def reference(arr):
    """Sort by popcount asc, ties broken by value asc (stable-sort semantics)."""
    return sorted(arr, key=lambda x: (popcount(x), x))


def test_empty():
    assert module_0.sort_array([]) == []


def test_single_element():
    assert module_0.sort_array([42]) == [42]


def test_orders_by_popcount_then_value():
    # popcount 1: 1,2,4 | popcount 2: 3,5
    assert module_0.sort_array([5, 3, 2, 4, 1]) == [1, 2, 4, 3, 5]


def test_input_order_does_not_matter():
    assert module_0.sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]


def test_duplicates_preserved():
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_zero_and_powers_of_two():
    # 0 has popcount 0 and comes first; 1,2,4,8 all have popcount 1
    assert module_0.sort_array([8, 0, 4, 2, 1]) == [0, 1, 2, 4, 8]


def test_does_not_mutate_input():
    data = [7, 1, 4]
    original = list(data)
    module_0.sort_array(data)
    assert data == original


def test_matches_reference_on_range():
    data = list(range(0, 200))
    random.Random(0).shuffle(data)
    assert module_0.sort_array(data) == reference(data)


def test_matches_reference_on_random_inputs():
    rng = random.Random(1234)
    for _ in range(50):
        data = [rng.randint(0, 5000) for _ in range(rng.randint(0, 30))]
        assert module_0.sort_array(data) == reference(data)

# Generated at 2026-10-24 07:07:47.207169
# Unit test for function sort_array
def test_sort_array():import random
import pytest

from solution import sort_array  # adjust to your module name


def popcount(x: int) -> int:
    return bin(x)[2:].count("1")


def reference(arr):
    """Sort by popcount asc, ties broken by value asc (stable-sort semantics)."""
    return sorted(arr, key=lambda x: (popcount(x), x))


def test_empty():
    assert module_0.sort_array([]) == []


def test_single_element():
    assert module_0.sort_array([42]) == [42]


def test_orders_by_popcount_then_value():
    # popcount 1: 1,2,4 | popcount 2: 3,5
    assert module_0.sort_array([5, 3, 2, 4, 1]) == [1, 2, 4, 3, 5]


def test_input_order_does_not_matter():
    assert module_0.sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]


def test_duplicates_preserved():
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_zero_and_powers_of_two():
    # 0 has popcount 0 and comes first; 1,2,4,8 all have popcount 1
    assert module_0.sort_array([8, 0, 4, 2, 1]) == [0, 1, 2, 4, 8]


def test_does_not_mutate_input():
    data = [7, 1, 4]
    original = list(data)
    module_0.sort_array(data)
    assert data == original


def test_matches_reference_on_range():
    data = list(range(0, 200))
    random.Random(0).shuffle(data)
    assert module_0.sort_array(data) == reference(data)


def test_matches_reference_on_random_inputs():
    rng = random.Random(1234)
    for _ in range(50):
        data = [rng.randint(0, 5000) for _ in range(rng.randint(0, 30))]
        assert module_0.sort_array(data) == reference(data)

# Generated at 2026-10-24 07:07:48.937717
# Unit test for function sort_array
def test_sort_array():import random
import pytest

from solution import sort_array  # adjust to your module name


def popcount(x: int) -> int:
    return bin(x)[2:].count("1")


def reference(arr):
    """Sort by popcount asc, ties broken by value asc (stable-sort semantics)."""
    return sorted(arr, key=lambda x: (popcount(x), x))


def test_empty():
    assert module_0.sort_array([]) == []


def test_single_element():
    assert module_0.sort_array([42]) == [42]


def test_orders_by_popcount_then_value():
    # popcount 1: 1,2,4 | popcount 2: 3,5
    assert module_0.sort_array([5, 3, 2, 4, 1]) == [1, 2, 4, 3, 5]


def test_input_order_does_not_matter():
    assert module_0.sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]


def test_duplicates_preserved():
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_zero_and_powers_of_two():
    # 0 has popcount 0 and comes first; 1,2,4,8 all have popcount 1
    assert module_0.sort_array([8, 0, 4, 2, 1]) == [0, 1, 2, 4, 8]


def test_does_not_mutate_input():
    data = [7, 1, 4]
    original = list(data)
    module_0.sort_array(data)
    assert data == original


def test_matches_reference_on_range():
    data = list(range(0, 200))
    random.Random(0).shuffle(data)
    assert module_0.sort_array(data) == reference(data)


def test_matches_reference_on_random_inputs():
    rng = random.Random(1234)
    for _ in range(50):
        data = [rng.randint(0, 5000) for _ in range(rng.randint(0, 30))]
        assert module_0.sort_array(data) == reference(data)