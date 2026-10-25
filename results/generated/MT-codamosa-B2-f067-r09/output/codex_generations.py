

# Generated at 2026-10-25 00:07:25.709971
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:28.284596
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:30.704854
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:33.138391
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:35.696149
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:38.116443
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:40.533160
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:42.954342
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:45.373742
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:47.794145
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:50.209867
# Unit test for function fruit_distribution

# Generated at 2026-10-25 00:07:58.530805
# Unit test for function fruit_distribution
def test_fruit_distribution():assert module_0.fruit_distribution("5 apples and 3 oranges", 20) == 12

# Generated at 2026-10-25 00:08:06.216076
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("10 apples 15 bananas 5 oranges", 40) == 10
    assert module_0.fruit_distribution("no fruits distributed", 25) == 25
    assert module_0.fruit_distribution("10 apples and 10 oranges", 20) == 0