

# Generated at 2026-10-24 07:06:16.362891
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("10 mangoes and 15 bananas", 50) == 25
    assert module_0.fruit_distribution("No fruits were distributed", 30) == 30
    assert module_0.fruit_distribution("20 apples 30 oranges 10 bananas", 100) == 40

# Generated at 2026-10-24 07:06:22.298384
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("10 apples and 15 oranges", 30) == 5
    assert module_0.fruit_distribution("0 apples and 3 oranges", 10) == 7

# Generated at 2026-10-24 07:06:30.798246
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("2 apples and 3 oranges", 10) == 5
    assert module_0.fruit_distribution("no fruits were distributed", 10) == 10

# Generated at 2026-10-24 07:06:38.039247
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 15) == 4
    assert module_0.fruit_distribution("2 apples and 3 bananas", 10) == 5
    assert module_0.fruit_distribution("There are no fruits", 10) == 10
    assert module_0.fruit_distribution("10 mangoes", 10) == 0

# Generated at 2026-10-24 07:06:44.519674
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("10 apples", 15) == 5
    assert module_0.fruit_distribution("No fruits were distributed", 12) == 12
    assert module_0.fruit_distribution("3 apples 4 oranges 2 bananas", 9) == 0