

# Generated at 2026-10-25 12:23:00.298646
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(1, 2, 3) == [3, 1]

    # need == remaining
    assert module_0.eat(5, 10, 10) == [15, 0]

    # need > remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    assert module_0.eat(0, 5, 0) == [0, 0]

    # edge cases with zero
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-25 12:23:03.822529
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(1, 2, 3) == [3, 1]

    # need == remaining
    assert module_0.eat(5, 10, 10) == [15, 0]

    # need > remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    assert module_0.eat(0, 5, 0) == [0, 0]

    # edge cases with zero
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-25 12:23:10.323811
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(1, 2, 3) == [3, 1]

    # need == remaining
    assert module_0.eat(5, 10, 10) == [15, 0]

    # need > remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    assert module_0.eat(0, 5, 0) == [0, 0]

    # edge cases with zero
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-25 12:23:18.827320
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(1, 2, 3) == [3, 1]

    # need == remaining
    assert module_0.eat(5, 10, 10) == [15, 0]

    # need > remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    assert module_0.eat(0, 5, 0) == [0, 0]

    # edge cases with zero
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-25 12:23:22.623631
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(1, 2, 3) == [3, 1]

    # need == remaining
    assert module_0.eat(5, 10, 10) == [15, 0]

    # need > remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    assert module_0.eat(0, 5, 0) == [0, 0]

    # edge cases with zero
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(10, 0, 5) == [10, 5]