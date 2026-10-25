

# Generated at 2026-10-24 22:24:24.160895
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("1 apple and 2 oranges", 10) == 7
    assert module_0.fruit_distribution("0 apples and 0 oranges", 15) == 15
    assert module_0.fruit_distribution("10 apples and 5 oranges", 15) == 0

# Generated at 2026-10-24 22:24:28.970592
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("10 apples 5 bananas 3 oranges", 25) == 7
    assert module_0.fruit_distribution("no fruits", 10) == 10
    assert module_0.fruit_distribution("", 8) == 8

# Generated at 2026-10-24 22:24:34.601590
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 14) == 3
    assert module_0.fruit_distribution("10 apples 20 oranges", 40) == 10
    assert module_0.fruit_distribution("no fruits distributed", 25) == 25
    assert module_0.fruit_distribution("2 apples 3 oranges 4 bananas", 9) == 0

# Generated at 2026-10-24 22:24:40.593394
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution(
        "5 apples and 6 oranges are rotten in the basket", 50
    ) == 39

    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    assert module_0.fruit_distribution("There are no rotten fruits", 25) == 25
    assert module_0.fruit_distribution("", 10) == 10

# Generated at 2026-10-24 22:24:43.226679
# Unit test for function fruit_distribution

# Generated at 2026-10-24 22:24:45.637845
# Unit test for function fruit_distribution

# Generated at 2026-10-24 22:24:48.056187
# Unit test for function fruit_distribution