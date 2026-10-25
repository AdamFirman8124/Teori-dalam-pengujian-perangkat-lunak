

# Generated at 2026-10-24 15:13:10.727075
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25

    # indices 0,1,2: 1**2 + 2

# Generated at 2026-10-24 15:13:13.147699
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:15.559081
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:17.972054
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:20.387253
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:22.930388
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:25.462866
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:27.876353
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:30.288571
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:32.701317
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:35.114827
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:37.530913
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:39.941878
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:42.354678
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:44.767335
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:47.182032
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:49.595519
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:52.006973
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:54.420120
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:56.832826
# Unit test for function sum_squares

# Generated at 2026-10-24 15:13:59.246271
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:01.666023
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:04.076463
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:06.490167
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:08.906853
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:11.319527
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:13.731320
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:16.144695
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:18.558473
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:20.973922
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:23.386706
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:25.797072
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:28.210774
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:30.626958
# Unit test for function sum_squares

# Generated at 2026-10-24 15:14:59.169545
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> sum is 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # No index hits %3 or %4 except 0
    # i=0: 1^2=1, i=1: 2, i=2: 3
    assert module_0.sum_squares([1, 2, 3]) == 6

    # i=3 (div by 3) -> 4^2=16; i=4 (div by 4, not 3) -> 5^3=125
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # 147

    # Index 12 is divisible by both 3 and 4 -> %3 branch wins (squared)
    lst = [2] * 13
    # i in {0,3,6,9,12} squared: 5 * 4 = 20; others unchanged: 8 * 2 = 16
    assert module_0.sum_squares(lst) == 36

    # Full check over indices 0..9
    # i0:0, i1:1, i2:2, i3:9, i4:64, i5:5, i6:36, i7:7, i8:512, i9:81
    assert module_0.sum_squares(list(range(10))) == 717

    # Negative numbers: squaring/cubing sign behavior
    # i0: (-1)^2=1, i1: -2, i2: -3, i3: (-4)^2=16
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    # i4 cubed with negative base: (-5)^3 = -125
    # i0: 1, i1: -2, i2: -3, i3: 16, i4: -125
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == -113

    # Floats pass through unchanged in the else branch
    # i0: 1.5^2=2.25, i1: 2.5 -> total 4.75
    assert abs(module_0.sum_squares([1.5, 2.5]) - 4.75) < 1e-9

    print("All tests passed.")

test_sum_squares()

# Generated at 2026-10-24 15:15:01.584192
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:04.192202
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:06.604346
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:09.017475
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:11.429930
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:13.842709
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:16.257635
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:18.676593
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:21.090420
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:23.503734
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:26.220733
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:28.629547
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:31.043132
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:33.460662
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:35.869523
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:38.283952
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:40.697379
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:43.111844
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:45.528898
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:47.943606
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:50.357874
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:52.769909
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:55.182822
# Unit test for function sum_squares

# Generated at 2026-10-24 15:15:57.595754
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:14.194701
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25

    # indices 0,1,2: 1**2 + 2

# Generated at 2026-10-24 15:16:24.042228
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:25.371509
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:26.686653
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:27.997467
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:29.304898
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:30.615406
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:16:33.117598
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:35.624850
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:38.032118
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:40.444531
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:42.858422
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:45.270966
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:47.684585
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:50.106108
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:52.513857
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:54.930698
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:57.501753
# Unit test for function sum_squares

# Generated at 2026-10-24 15:16:59.914751
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:02.327974
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:04.741241
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:07.153833
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:09.566223
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:11.979671
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:14.394936
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:16.807556
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:19.221383
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:21.637428
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:24.053052
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:26.463482
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:28.876793
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:30.232973
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:31.552979
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:32.862167
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:34.176750
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:35.495675
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:36.867469
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:38.216591
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:39.525190
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:40.836101
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:42.144137
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:43.453128
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:44.828431
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:46.154624
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:47.465082
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:48.780461
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:17:51.198091
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:53.749859
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:56.165712
# Unit test for function sum_squares

# Generated at 2026-10-24 15:17:58.579517
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:00.993265
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:03.406460
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:06.034749
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:08.446470
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:10.860622
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:13.273263
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:15.685474
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:18.098162
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:21.238571
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:23.651583
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:26.064441
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:28.476861
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:30.890486
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:33.303539
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:35.716241
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:38.128999
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:40.542020
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:42.955284
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:45.367970
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:47.784845
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:50.197570
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:52.609761
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:55.023287
# Unit test for function sum_squares

# Generated at 2026-10-24 15:18:56.449872
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:18:57.759866
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:18:59.113336
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:00.418162
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:01.736096
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:06.381662
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:07.733911
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:09.058099
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:10.394342
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:19:12.808869
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:15.222805
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:17.636094
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:20.135222
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:22.548932
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:24.967187
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:27.378972
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:29.791301
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:32.207699
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:34.622354
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:37.034943
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:39.448602
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:41.860503
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:44.277018
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:46.688335
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:49.100366
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:51.514397
# Unit test for function sum_squares

# Generated at 2026-10-24 15:19:53.928637
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:02.782291
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:05.194764
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:07.607707
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:10.022759
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:12.434870
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:14.847630
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:17.261803
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:19.674370
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:22.088502
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:24.505448
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:26.918712
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:29.331174
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:31.743961
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:34.156683
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:36.570771
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:38.983521
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:41.394828
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:43.807621
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:46.220292
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:48.633679
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:51.046132
# Unit test for function sum_squares

# Generated at 2026-10-24 15:20:52.424209
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:20:53.745116
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:20:55.061600
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:11.634578
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:12.976454
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:14.364239
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:15.799198
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:17.231532
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:18.614564
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:19.934212
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:21.255548
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:22.603790
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:21:25.124195
# Unit test for function sum_squares

# Generated at 2026-10-24 15:21:27.628826
# Unit test for function sum_squares

# Generated at 2026-10-24 15:21:30.041579
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:03.913612
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:06.332378
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:08.745984
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:11.158783
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:22.330455
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-24 15:22:23.640576
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:25.086263
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:26.421104
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:27.733111
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:29.057280
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:30.371331
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:31.690848
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # No index hits the %3 or %4 rules
    assert module_0.sum_squares([1, 2]) == 3

    # Basic %3 case: index 0 and 3 get squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Mixed %3 and %4: index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3**2 + 4 + 5**3  # == 155

    # Negatives (classic HumanEval case)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 0: 0 % 3 == 0, so squared (also 0 % 4 == 0, but %3 branch wins)
    assert module_0.sum_squares([7, 7, 7, 7, 7]) == 49 + 7 + 7 + 49 + 343  # == 455

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-24 15:22:34.195271
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:36.704038
# Unit test for function sum_squares

# Generated at 2026-10-24 15:22:39.114640
# Unit test for function sum_squares