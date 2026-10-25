

# Generated at 2026-10-24 10:35:28.423187
# Unit test for function derivative
def test_derivative():
    # 3 + 2x + x^2  ->  2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # 1 + x  ->  1
    assert module_0.derivative([1, 1]) == [1]
    # 5x^3  ->  15x^2
    assert module_0.derivative([0, 0, 0, 5]) == [0, 0, 15]
    # constant  ->  empty (no terms left)
    assert module_0.derivative([7]) == []
    # empty input  ->  empty output
    assert module_0.derivative([]) == []
    # zero polynomial  ->  empty
    assert module_0.derivative([0, 0, 0]) == []


def test_derivative_does_not_mutate_input():
    xs = [3, 2, 1]
    module_0.derivative(xs)
    assert xs == [3, 2, 1]

# Generated at 2026-10-24 10:35:30.842624
# Unit test for function derivative

# Generated at 2026-10-24 10:35:33.265200
# Unit test for function derivative

# Generated at 2026-10-24 10:35:35.685441
# Unit test for function derivative

# Generated at 2026-10-24 10:35:38.121412
# Unit test for function derivative

# Generated at 2026-10-24 10:35:40.542459
# Unit test for function derivative

# Generated at 2026-10-24 10:35:42.962701
# Unit test for function derivative

# Generated at 2026-10-24 10:35:45.382476
# Unit test for function derivative

# Generated at 2026-10-24 10:35:47.800047
# Unit test for function derivative

# Generated at 2026-10-24 10:35:56.910684
# Unit test for function derivative
def test_derivative():assert module_0.derivative([3, 1, 2]) == [1, 4]

# Generated at 2026-10-24 10:35:58.232820
# Unit test for function derivative
def test_derivative():
    # 3 + 2x + x^2  ->  2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # 1 + x  ->  1
    assert module_0.derivative([1, 1]) == [1]
    # 5x^3  ->  15x^2
    assert module_0.derivative([0, 0, 0, 5]) == [0, 0, 15]
    # constant  ->  empty (no terms left)
    assert module_0.derivative([7]) == []
    # empty input  ->  empty output
    assert module_0.derivative([]) == []
    # zero polynomial  ->  empty
    assert module_0.derivative([0, 0, 0]) == []


def test_derivative_does_not_mutate_input():
    xs = [3, 2, 1]
    module_0.derivative(xs)
    assert xs == [3, 2, 1]