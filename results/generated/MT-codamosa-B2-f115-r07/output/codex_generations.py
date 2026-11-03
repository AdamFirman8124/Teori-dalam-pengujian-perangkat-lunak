

# Generated at 2026-11-03 00:25:41.666168
# Unit test for function max_fill
def test_max_fill():
    # Basic cases: each row's sum divided by capacity, rounded up
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # No water present
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0
    assert module_0.max_fill([[0]], 1) == 0

    # Empty grid
    assert module_0.max_fill([], 1) == 0

    # Capacity larger than row sum -> single trip per non-empty row
    assert module_0.max_fill([[1, 1]], 10) == 1
    assert module_0.max_fill([[3]], 5) == 1

    # Exact division (no rounding needed)
    assert module_0.max_fill([[2, 2]], 2) == 2
    assert module_0.max_fill([[4, 4], [6]], 2) == 7  # ceil(8/2) + ceil(6/2) = 4 + 3

    # Ceiling behavior (partial capacity requires extra trip)
    assert module_0.max_fill([[5]], 3) == 2
    assert module_0.max_fill([[7, 3]], 4) == 3  # ceil(10/4) = 3

    # Single cell
    assert module_0.max_fill([[1]], 1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_max_fill()

# Generated at 2026-11-03 00:26:44.950224
# Unit test for function max_fill
def test_max_fill():
    # Each unit of water requires one trip per capacity units

    # Basic case: capacity 1, each 1 in the grid needs one trip
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity 2: rows sum to 2, 0, 4, 3 -> ceil gives 1, 0, 2, 2
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Empty wells: no water, no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Capacity exactly matches row sum
    assert module_0.max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 4) == 2

    # Capacity smaller than row sum requires ceiling rounding
    assert module_0.max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 3) == 4

    # Single well, single trip
    assert module_0.max_fill([[1, 1]], 2) == 1

    # Large capacity covers everything in one trip per non-empty well
    assert module_0.max_fill([[1, 1, 1], [0, 1, 0], [1, 0, 1]], 100) == 3

    # Fractional rounding: row sums 5 and 7 with capacity 3 -> 2 + 3
    assert module_0.max_fill([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]], 3) == 5

    print("All tests passed!")


test_max_fill()

# Generated at 2026-11-03 00:27:48.948040
# Unit test for function max_fill
def test_max_fill():
    # Basic example: each well needs ceil(sum/capacity) trips
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity of 2 groups units together
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Empty grid requires no trips
    assert module_0.max_fill([], 5) == 0

    # Grid with all empty wells requires no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 3) == 0

    # Single well, exact division
    assert module_0.max_fill([[1, 1, 1, 1]], 4) == 1

    # Single well, non-exact division requires rounding up
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Capacity larger than any well's water
    assert module_0.max_fill([[1, 1], [1, 0]], 10) == 2

    # Exact multiples of capacity
    assert module_0.max_fill([[2, 2], [4]], 4) == 2

    # Mixed empty and full wells
    assert module_0.max_fill([[0], [3], [0, 0]], 2) == 2

    # Larger capacity rounds down within a well
    assert module_0.max_fill([[5, 5], [1, 1, 1]], 5) == 3

    # Large grid stress check
    grid = [[1] * 10 for _ in range(7)]  # each row sums to 10
    assert module_0.max_fill(grid, 3) == 7 * math.ceil(10 / 3)  # 7 * 4 = 28

    print("All tests passed!")


import math

def module_0.max_fill(grid, capacity):
    import math
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

test_max_fill()

# Generated at 2026-11-03 00:28:53.479748
# Unit test for function max_fill
def test_max_fill():
    # Test case 1: Basic example
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Test case 2: Larger capacity
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Test case 3: Empty rows
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Test case 4: Exact division (no rounding needed)
    assert module_0.max_fill([[2, 2], [4, 4]], 4) == 3

    # Test case 5: Single row requiring ceiling
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Test case 6: Empty grid
    assert module_0.max_fill([], 1) == 0

    # Test case 7: Capacity exactly matches row sums
    assert module_0.max_fill([[3], [3], [3]], 3) == 3

    # Test case 8: Fractional division requires ceiling
    assert module_0.max_fill([[7]], 3) == 3  # ceil(7/3) = 3

    # Test case 9: Multiple rows with mixed values
    assert module_0.max_fill([[1, 2], [3, 4], [5, 6]], 5) == 4  # ceil(3/5)+ceil(7/5)+ceil(11/5)=1+2+3

    print("All tests passed!")

# Generated at 2026-11-03 00:29:48.550797
# Unit test for function max_fill
def test_max_fill():
    # Test with all zeros - no water to carry
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 1) == 0

    # Test with capacity 1 - every unit needs its own trip
    assert module_0.max_fill([[1, 1, 1], [1, 1, 1]], 1) == 6

    # Test from problem examples
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 7
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Test where row sums exactly match capacity
    assert module_0.max_fill([[1, 1, 0, 1], [1, 0, 1, 1]], 3) == 2

    # Test where row sum is less than capacity - still needs one trip
    assert module_0.max_fill([[1, 0, 0], [0, 1, 0]], 5) == 2

    # Test single row
    assert module_0.max_fill([[1, 1, 1, 1]], 2) == 2

    # Test empty grid
    assert module_0.max_fill([], 3) == 0

    # Test large capacity covering everything
    assert module_0.max_fill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 100) == 1

    # Test ceiling behavior with non-divisible sums
    assert module_0.max_fill([[1, 1, 1, 1, 1]], 2) == 3  # ceil(5/2) = 3

test_max_fill()