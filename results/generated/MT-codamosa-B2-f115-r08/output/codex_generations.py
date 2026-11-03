

# Generated at 2026-11-03 03:31:39.578553
# Unit test for function max_fill
def test_max_fill():
    # Each well with water needs ceil(water_units / capacity) bucket trips
    # Classic examples
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Single well, exact division
    assert module_0.max_fill([[1, 1, 1, 1]], 2) == 2

    # Single well, requires rounding up
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Large capacity covers entire well in one trip
    assert module_0.max_fill([[1, 1, 1, 1, 1]], 10) == 1

    # Empty grid
    assert module_0.max_fill([], 3) == 0

    # Grid with no water
    assert module_0.max_fill([[0, 0], [0, 0], [0, 0]], 1) == 0

    # Capacity of 1 means one trip per water unit
    assert module_0.max_fill([[1, 0, 1], [0, 1, 0]], 1) == 3

    # Multiple wells with mixed values
    assert module_0.max_fill([[1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1]], 3) == 4

    # Single cell grid
    assert module_0.max_fill([[1]], 1) == 1
    assert module_0.max_fill([[0]], 1) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_max_fill()

# Generated at 2026-11-03 03:33:31.402213
# Unit test for function max_fill
def test_max_fill():
    # Basic example: each row requires ceil(sum/capacity) trips
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity of 2
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Empty grid yields no trips
    assert module_0.max_fill([], 5) == 0

    # Grid with all zeros requires no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Single row where capacity exactly matches the sum
    assert module_0.max_fill([[1, 1, 1, 1]], 4) == 1

    # Single row where capacity exceeds the sum
    assert module_0.max_fill([[1, 1, 0, 0]], 10) == 1

    # Fractional division rounds up (ceil behavior)
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Larger capacity reduces the number of trips
    assert module_0.max_fill([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 5) == 2

    # Multiple rows with mixed values
    assert module_0.max_fill([[0, 1, 0], [1, 1, 1], [0, 0, 0], [1, 0, 1]], 3) == 3

    # Very large capacity: one trip per non-empty row
    assert module_0.max_fill([[1, 0, 1], [0, 1, 0]], 100) == 2

    print("All tests passed!")


test_max_fill()

# Generated at 2026-11-03 03:35:57.629425
# Unit test for function max_fill
def test_max_fill():
    # Classic example: three wells, capacity 1
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    # Larger capacity reduces number of trips
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    # All-zero rows require no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0
    # Exact division: 4 units / capacity 2 = 2 trips
    assert module_0.max_fill([[4]], 2) == 2
    # Rounding up: 3 units / capacity 2 = 2 trips
    assert module_0.max_fill([[3]], 2) == 2
    # Multiple rows, exact division
    assert module_0.max_fill([[1, 1, 1], [2, 2, 2]], 3) == 3
    # Empty grid -> zero trips
    assert module_0.max_fill([], 1) == 0
    # Single element, exact fit
    assert module_0.max_fill([[5]], 5) == 1
    # Single element, needs rounding up
    assert module_0.max_fill([[6]], 5) == 2
    # Capacity larger than any row sum
    assert module_0.max_fill([[2, 3], [4, 1]], 10) == 2
    # Fractional totals across rows
    assert module_0.max_fill([[7], [8]], 3) == 6

# Generated at 2026-11-03 03:37:32.657374
# Unit test for function max_fill
def test_max_fill():
    # Basic case: each well requires ceil(sum/capacity) trips
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity of 2: ceil(2/2)=1, ceil(0/2)=0, ceil(4/2)=2, ceil(3/2)=2
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Empty wells require no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Single well, single unit of water
    assert module_0.max_fill([[1]], 1) == 1

    # Capacity larger than any row sum: one trip per non-empty row
    assert module_0.max_fill([[0, 1], [1, 1]], 10) == 2

    # Fractional division requires ceiling: ceil(3/2) = 2
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Empty grid requires no trips
    assert module_0.max_fill([], 3) == 0

    # Larger capacity exact division
    assert module_0.max_fill([[1, 1, 1, 1, 1, 1]], 3) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_max_fill()

# Generated at 2026-11-03 03:39:06.356224
# Unit test for function max_fill
def test_max_fill():
    # Single row, capacity 1
    assert module_0.max_fill([[1, 1, 1, 1]], 1) == 4

    # Classic multi-row examples
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # All zeros: no trips needed
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Empty grid
    assert module_0.max_fill([], 1) == 0

    # Capacity larger than any row sum: one trip per non-empty row
    assert module_0.max_fill([[1, 1, 1]], 10) == 1
    assert module_0.max_fill([[1, 1], [0, 1], [1, 0]], 5) == 3

    # Capacity exactly equals a row sum: one trip
    assert module_0.max_fill([[1, 1]], 2) == 1

    # Ceiling behavior with partial trips
    assert module_0.max_fill([[1, 1, 1, 1, 1]], 2) == 3   # ceil(5/2) = 3
    assert module_0.max_fill([[1, 1, 1, 1]], 3) == 2      # ceil(4/3) = 2

    # Mixed rows with varying sums and capacity
    assert module_0.max_fill([[1, 0, 1], [0, 0, 0], [1, 1, 1, 1]], 3) == 3  # 1 + 0 + 2

    # Large capacity across many rows
    assert module_0.max_fill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9) == 3

    print("All tests passed!")


test_max_fill()