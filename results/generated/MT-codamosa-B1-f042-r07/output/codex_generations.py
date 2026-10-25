

# Generated at 2026-10-24 11:12:16.160927
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:18.579513
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:21.000076
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:23.419458
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:25.838877
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:28.258860
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:30.678095
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:33.092838
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:35.514622
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:37.937854
# Unit test for function incr_list

# Generated at 2026-10-24 11:12:44.843275
# Unit test for function incr_list
def test_incr_list():assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]

# Generated at 2026-10-24 11:12:46.175681
# Unit test for function incr_list
def test_incr_list():
    # Basic cases
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    assert module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

    # Edge cases
    assert module_0.incr_list([]) == []
    assert module_0.incr_list([0]) == [1]
    assert module_0.incr_list([-1, -5, -100]) == [0, -4, -99]

    # Original list is not mutated
    original = [1, 2, 3]
    module_0.incr_list(original)
    assert original == [1, 2, 3]

    print("All tests passed!")


test_incr_list()