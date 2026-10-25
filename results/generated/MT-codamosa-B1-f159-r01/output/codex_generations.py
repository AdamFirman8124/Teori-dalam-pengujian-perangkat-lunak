

# Generated at 2026-10-24 04:10:22.642233
# Unit test for function eat
def test_eat():
    # Enough food remaining
    assert module_0.eat(10, 5, 20) == [15, 15]

    # Need exceeds remaining food
    assert module_0.eat(10, 20, 5) == [15, 0]

    # Need exactly equals remaining food
    assert module_0.eat(10, 5, 5) == [15, 0]

    # Nothing is needed
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-24 04:10:27.748188
# Unit test for function eat
def test_eat():
    # Enough food remaining
    assert module_0.eat(5, 3, 10) == [8, 7]

    # Need exactly equals remaining
    assert module_0.eat(5, 3, 3) == [8, 0]

    # Not enough food remaining
    assert module_0.eat(5, 10, 3) == [8, 0]

    # Nothing is needed
    assert module_0.eat(5, 0, 10) == [5, 10]

# Generated at 2026-10-24 04:10:33.093460
# Unit test for function eat
def test_eat():
    # Enough remaining
    assert module_0.eat(10, 5, 8) == [15, 3]

    # Exactly enough remaining
    assert module_0.eat(10, 5, 5) == [15, 0]

    # Not enough remaining
    assert module_0.eat(10, 8, 5) == [15, 0]

    # Nothing needed
    assert module_0.eat(10, 0, 5) == [10, 5]

# Generated at 2026-10-24 04:10:35.515188
# Unit test for function eat

# Generated at 2026-10-24 04:10:40.612291
# Unit test for function eat
def test_eat():assert module_0.eat(5, 3, 10) == [8, 7]

# Generated at 2026-10-24 04:10:45.988765
# Unit test for function eat
def test_eat():
    # Enough remaining
    assert module_0.eat(10, 5, 8) == [15, 3]

    # Exactly enough remaining
    assert module_0.eat(10, 5, 5) == [15, 0]

    # Not enough remaining
    assert module_0.eat(10, 8, 5) == [15, 0]