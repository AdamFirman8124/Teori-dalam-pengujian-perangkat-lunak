

# Generated at 2026-10-25 09:42:51.936558
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9

# Generated at 2026-10-25 09:42:54.578484
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:42:56.992927
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:42:59.407003
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:01.825409
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:04.475218
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:06.890861
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:09.306700
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:11.724003
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:14.141873
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:16.742329
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:19.159371
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-25 09:43:21.572763
# Unit test for function mean_absolute_deviation