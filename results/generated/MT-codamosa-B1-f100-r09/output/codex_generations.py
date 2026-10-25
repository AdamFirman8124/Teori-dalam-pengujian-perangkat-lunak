

# Generated at 2026-10-24 12:59:53.207698
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(6) == [6, 8, 10, 12, 14, 16]

    # general properties: length, start value, step of 2
    for n in [1, 2, 3, 4, 7, 10]:
        result = module_0.make_a_pile(n)
        assert len(result) == n
        assert result[0] == n
        assert all(result[i+1] - result[i] == 2 for i in range(n-1))
        assert all(x % 2 == n % 2 for x in result)

# Generated at 2026-10-24 12:59:55.776205
# Unit test for function make_a_pile

# Generated at 2026-10-24 12:59:58.203375
# Unit test for function make_a_pile

# Generated at 2026-10-24 13:00:00.617022
# Unit test for function make_a_pile

# Generated at 2026-10-24 13:00:03.033477
# Unit test for function make_a_pile

# Generated at 2026-10-24 13:00:05.447484
# Unit test for function make_a_pile

# Generated at 2026-10-24 13:00:07.860919
# Unit test for function make_a_pile

# Generated at 2026-10-24 13:00:24.057602
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(0) == []

# Generated at 2026-10-24 13:00:25.518349
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(6) == [6, 8, 10, 12, 14, 16]

    # general properties: length, start value, step of 2
    for n in [1, 2, 3, 4, 7, 10]:
        result = module_0.make_a_pile(n)
        assert len(result) == n
        assert result[0] == n
        assert all(result[i+1] - result[i] == 2 for i in range(n-1))
        assert all(x % 2 == n % 2 for x in result)