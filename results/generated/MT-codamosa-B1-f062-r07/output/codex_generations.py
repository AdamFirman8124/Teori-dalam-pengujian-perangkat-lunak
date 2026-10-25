

# Generated at 2026-10-25 01:03:16.987477
# Unit test for function derivative

# Generated at 2026-10-25 01:03:19.401698
# Unit test for function derivative

# Generated at 2026-10-25 01:03:21.816771
# Unit test for function derivative

# Generated at 2026-10-25 01:03:24.231710
# Unit test for function derivative

# Generated at 2026-10-25 01:03:26.648032
# Unit test for function derivative

# Generated at 2026-10-25 01:03:29.062884
# Unit test for function derivative

# Generated at 2026-10-25 01:03:31.478952
# Unit test for function derivative

# Generated at 2026-10-25 01:03:34.061811
# Unit test for function derivative

# Generated at 2026-10-25 01:03:36.479265
# Unit test for function derivative

# Generated at 2026-10-25 01:03:38.894632
# Unit test for function derivative

# Generated at 2026-10-25 01:03:41.308625
# Unit test for function derivative

# Generated at 2026-10-25 01:03:43.723600
# Unit test for function derivative

# Generated at 2026-10-25 01:03:46.143029
# Unit test for function derivative

# Generated at 2026-10-25 01:03:47.496315
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    assert module_0.derivative([3.5, 2.0, 4.0]) == [2.0, 8.0]
    assert module_0.derivative([5]) == []
    assert module_0.derivative([]) == []