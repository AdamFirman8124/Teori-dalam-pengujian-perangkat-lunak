

# Generated at 2026-10-25 06:53:34.285359
# Unit test for function derivative

# Generated at 2026-10-25 06:53:36.700518
# Unit test for function derivative

# Generated at 2026-10-25 06:53:39.116146
# Unit test for function derivative

# Generated at 2026-10-25 06:53:41.535291
# Unit test for function derivative

# Generated at 2026-10-25 06:53:43.949624
# Unit test for function derivative

# Generated at 2026-10-25 06:53:46.365134
# Unit test for function derivative

# Generated at 2026-10-25 06:53:48.779262
# Unit test for function derivative

# Generated at 2026-10-25 06:53:51.193300
# Unit test for function derivative

# Generated at 2026-10-25 06:53:53.607744
# Unit test for function derivative

# Generated at 2026-10-25 06:53:56.027999
# Unit test for function derivative

# Generated at 2026-10-25 06:53:58.435281
# Unit test for function derivative

# Generated at 2026-10-25 06:54:00.858919
# Unit test for function derivative

# Generated at 2026-10-25 06:54:02.372809
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4]) == [1, 4, 12]
    assert module_0.derivative([1, 2]) == [2]
    assert module_0.derivative([5]) == []          # constant -> empty
    assert module_0.derivative([]) == []           # empty stays empty