

# Generated at 2026-10-24 12:04:19.387443
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:21.898569
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:24.318317
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:26.739462
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:29.157592
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:31.576617
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:33.995487
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:36.415298
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:38.833244
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:41.252618
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:43.674461
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:46.090853
# Unit test for function smallest_change

# Generated at 2026-10-24 12:04:48.507292
# Unit test for function smallest_change

# Generated at 2026-10-24 12:05:05.270358
# Unit test for function smallest_change
def test_smallest_change():
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 2
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([7]) == 0
    assert module_0.smallest_change([1, 2]) == 1
    assert module_0.smallest_change([2, 2, 2, 2]) == 0
    assert module_0.smallest_change([1, 2, 3, 4, 5]) == 2