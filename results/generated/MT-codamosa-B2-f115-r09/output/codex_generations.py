

# Generated at 2026-11-03 05:18:32.831707
# Unit test for function max_fill
def test_max_fill():
    # Example: capacity=1, one trip per unit of water
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity=2 groups water efficiently across wells
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # Empty wells require no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Empty grid
    assert module_0.max_fill([], 3) == 0

    # Capacity larger than any well's content: one trip per non-empty well
    assert module_0.max_fill([[1, 1], [0, 1], [1, 0]], 10) == 3

    # Single well needing multiple trips (rounding up)
    assert module_0.max_fill([[1, 1, 1, 1, 1]], 2) == 3

    # Exact multiple of capacity needs no extra trip
    assert module_0.max_fill([[1, 1, 1, 1]], 2) == 2

    # Mixed well sizes with capacity=3
    assert module_0.max_fill([[3, 2, 1], [4, 0, 0]], 3) == 4

    # Result should always be a non-negative integer
    result = module_0.max_fill([[1, 0], [0, 1]], 1)
    assert isinstance(result, int) and result >= 0

    print("All tests passed!")


test_max_fill()

# Generated at 2026-11-03 05:21:03.699556
# Unit test for function max_fill
def test_max_fill():
    # Basic case: each row needs partial buckets
    assert module_0.max_fill([[1, 1, 1], [1, 1, 1]], 4) == 2  # ceil(3/4)+ceil(3/4) = 1+1
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0  # empty wells need no buckets
    assert module_0.max_fill([[1, 1], [1, 1], [1, 1]], 2) == 3  # ceil(2/2)*3 = 3

    # Exact division
    assert module_0.max_fill([[4, 4], [8, 8]], 4) == 4  # 2+4 = 6? No: ceil(8/4)+ceil(16/4)=2+4=6
    # Correct the above expectation
    assert module_0.max_fill([[4, 4], [8, 8]], 4) == 6

    # Capacity larger than any row sum
    assert module_0.max_fill([[3], [5], [7]], 100) == 3  # each row = 1 bucket

    # Capacity of 1: every unit needs its own bucket
    assert module_0.max_fill([[2, 3], [4]], 1) == 9  # ceil(5/1)+ceil(4/1)=9

    # Single row, single element
    assert module_0.max_fill([[0]], 1) == 0
    assert module_0.max_fill([[1]], 1) == 1

    # Empty grid
    assert module_0.max_fill([], 5) == 0

    # Fractional results requiring ceiling
    assert module_0.max_fill([[7]], 3) == 3  # ceil(7/3)=3
    assert module_0.max_fill([[1, 2, 3]], 2) == 3  # ceil(6/2)=3

    # Mixed zeros and values
    assert module_0.max_fill([[0, 1, 0], [0, 0, 2], [3, 0, 0]], 2) == 4
    # ceil(1/2)+ceil(2/2)+ceil(3/2) = 1+1+2 = 4

    print("All tests passed!")

test_max_fill()

# Generated at 2026-11-03 05:23:33.416065
# Unit test for function max_fill
def test_max_fill():
    # Basic example: each well requires ceil(sum/capacity) trips
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6

    # Capacity of 2 with mixed wells (including an empty well)
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5

    # All-empty grid requires no trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Empty grid
    assert module_0.max_fill([], 1) == 0

    # Single well, exact division
    assert module_0.max_fill([[1, 1, 1, 1]], 2) == 2

    # Single well, non-exact division (rounds up)
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Capacity larger than any well: one trip per non-empty well
    assert module_0.max_fill([[1, 0, 1], [0, 1, 0]], 10) == 2

    # Multiple small wells, each needs one trip
    assert module_0.max_fill([[1], [1, 1], [1, 1, 1]], 3) == 3

    # Larger capacity reduces number of trips
    assert module_0.max_fill([[1, 1, 1, 1, 1, 1]], 3) == 2

    print("All tests passed!")


test_max_fill()

# Generated at 2026-11-03 05:25:23.594535
# Unit test for function max_fill
def test_max_fill():
    # Basic cases from problem description
    assert module_0.max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

    # Single row, exact division
    assert module_0.max_fill([[1, 1, 1, 1]], 4) == 1

    # Single row, requires ceiling
    assert module_0.max_fill([[1, 1, 1]], 2) == 2

    # Empty grid
    assert module_0.max_fill([], 3) == 0

    # Single cell grid
    assert module_0.max_fill([[1]], 1) == 1
    assert module_0.max_fill([[0]], 1) == 0

    # Capacity larger than any row sum
    assert module_0.max_fill([[1, 1, 1], [0, 1, 0]], 10) == 2

    # Capacity of 1 equals total water units
    assert module_0.max_fill([[1, 0, 1], [1, 1, 0]], 1) == 5

    # Larger capacity reduces bucket count
    assert module_0.max_fill([[1, 1, 1, 1, 1, 1]], 3) == 2

    # Mixed rows with zero and non-zero sums
    assert module_0.max_fill([[0, 0], [1, 1], [0, 0], [1, 0]], 2) == 2

    # Fractional division requiring ceiling across multiple rows
    assert module_0.max_fill([[2, 2], [3, 3], [1, 1]], 3) == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_max_fill()