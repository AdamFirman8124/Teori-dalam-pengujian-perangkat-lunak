

# Generated at 2026-11-01 22:14:51.639340
# Unit test for function eat
def test_eat():
    # Case where need <= remaining: rabbit eats what it needs, leftover remains
    assert module_0.eat(5, 5, 10) == [10, 5]      # eats 5, 5 left
    assert module_0.eat(0, 10, 10) == [10, 0]     # eats exactly all remaining
    assert module_0.eat(2, 3, 100) == [5, 97]     # plenty of grass remaining

    # Case where need > remaining: rabbit eats only what's available
    assert module_0.eat(5, 10, 3) == [8, 0]       # eats all 3 remaining, none left
    assert module_0.eat(1, 5, 4) == [5, 0]        # eats 4, 0 left
    assert module_0.eat(7, 2, 1) == [8, 0]        # needs 2 but only 1 available

    # Edge cases
    assert module_0.eat(0, 0, 0) == [0, 0]        # nothing to eat, nothing needed
    assert module_0.eat(100, 0, 50) == [100, 50]  # no need to eat, remaining unchanged
    assert module_0.eat(0, 1, 0) == [0, 0]        # needs but nothing remaining

    # Verify return type is a list of two integers
    result = module_0.eat(3, 4, 9)
    assert isinstance(result, list) and len(result) == 2
    assert all(isinstance(x, int) for x in result)

    print("All tests passed!")

# Generated at 2026-11-01 22:15:37.555504
# Unit test for function eat
def test_eat():
    # Case where need is less than remaining
    assert module_0.eat(5, 6, 10) == [11, 4], "Expected [11, 4] when need < remaining"

    # Case where need is greater than remaining
    assert module_0.eat(4, 8, 9) == [12, 1], "Expected [12, 1] when need < remaining"
    assert module_0.eat(2, 11, 5) == [7, 0], "Expected [7, 0] when need > remaining"

    # Case where need equals remaining
    assert module_0.eat(1, 10, 10) == [11, 0], "Expected [11, 0] when need == remaining"

    # Case where remaining is zero
    assert module_0.eat(10, 5, 0) == [10, 0], "Expected [10, 0] when remaining is 0"

    # Case where need is zero
    assert module_0.eat(0, 0, 5) == [0, 5], "Expected [0, 5] when need is 0"

    print("All tests passed!")


if __name__ == "__main__":
    test_eat()

# Generated at 2026-11-01 22:16:52.307085
# Unit test for function eat
def test_eat():
    # Case: need <= remaining, rabbit eats fully
    assert module_0.eat(5, 5, 10) == [10, 5]
    assert module_0.eat(0, 3, 7) == [3, 4]
    assert module_0.eat(100, 10, 50) == [110, 40]

    # Case: need == remaining, eats everything needed
    assert module_0.eat(2, 5, 5) == [7, 0]

    # Case: need > remaining, eats only what's available
    assert module_0.eat(5, 10, 3) == [8, 0]
    assert module_0.eat(1, 20, 0) == [1, 0]

    # Edge: need is zero
    assert module_0.eat(4, 0, 5) == [4, 5]

    # Edge: both need and remaining are zero
    assert module_0.eat(6, 0, 0) == [6, 0]

    print("All test_eat cases passed!")

# Generated at 2026-11-01 22:17:23.745147
# Unit test for function eat
def test_eat():
    # Case where need <= remaining: eats all needed, leftover remains
    assert module_0.eat(5, 5, 10) == [10, 5]
    assert module_0.eat(2, 3, 10) == [5, 7]
    assert module_0.eat(0, 1, 100) == [1, 99]

    # Edge case: need exactly equals remaining
    assert module_0.eat(3, 4, 4) == [7, 0]

    # Case where need > remaining: eats only what's available
    assert module_0.eat(4, 10, 5) == [9, 0]
    assert module_0.eat(1, 5, 0) == [1, 0]
    assert module_0.eat(10, 100, 50) == [60, 0]

    # Edge case: nothing needed, nothing eaten
    assert module_0.eat(7, 0, 3) == [7, 3]

    print("All eat tests passed!")


if __name__ == "__main__":
    test_eat()

# Generated at 2026-11-01 22:18:41.055518
# Unit test for function eat
def test_eat():
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestEat)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    unittest.main(verbosity=2)