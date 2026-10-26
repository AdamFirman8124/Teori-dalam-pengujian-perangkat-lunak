

# Generated at 2026-10-25 07:26:32.982794
# Unit test for function x_or_y
def test_x_or_y():
    # n is prime -> returns x
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(13, 1, 0) == 1

    # n is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(100, 1, 0) == 0

    # edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    assert module_0.x_or_y(0, "prime", "not") == "prime"  # loop skipped, falls to else
    assert module_0.x_or_y(-5, "prime", "not") == "prime"  # negative: loop skipped

    print("All tests passed.")

test_x_or_y()

# Generated at 2026-10-25 07:26:35.398316
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:37.811570
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:40.225157
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:42.754155
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:45.169206
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:47.583658
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:49.999383
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:52.411936
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:54.826682
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:57.242807
# Unit test for function x_or_y

# Generated at 2026-10-25 07:26:59.784343
# Unit test for function x_or_y

# Generated at 2026-10-25 07:27:02.129566
# Unit test for function x_or_y