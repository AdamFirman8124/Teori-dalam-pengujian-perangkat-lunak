

# Generated at 2026-10-24 04:21:29.414534
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def test_make_a_pile_properties():
    for n in range(1, 50):
        pile = module_0.make_a_pile(n)
        assert len(pile) == n          # one pile per level
        assert pile[0] == n            # first pile has n stones
        assert all(b - a == 2 for a, b in zip(pile, pile[1:]))  # +2 each level

# Generated at 2026-10-24 04:21:30.734638
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def test_make_a_pile_properties():
    for n in range(1, 50):
        pile = module_0.make_a_pile(n)
        assert len(pile) == n          # one pile per level
        assert pile[0] == n            # first pile has n stones
        assert all(b - a == 2 for a, b in zip(pile, pile[1:]))  # +2 each level

# Generated at 2026-10-24 04:21:32.044209
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def test_make_a_pile_properties():
    for n in range(1, 50):
        pile = module_0.make_a_pile(n)
        assert len(pile) == n          # one pile per level
        assert pile[0] == n            # first pile has n stones
        assert all(b - a == 2 for a, b in zip(pile, pile[1:]))  # +2 each level

# Generated at 2026-10-24 04:21:34.630157
# Unit test for function make_a_pile

# Generated at 2026-10-24 04:21:37.048495
# Unit test for function make_a_pile

# Generated at 2026-10-24 04:21:39.547735
# Unit test for function make_a_pile

# Generated at 2026-10-24 04:21:41.962214
# Unit test for function make_a_pile

# Generated at 2026-10-24 04:21:44.377628
# Unit test for function make_a_pile

# Generated at 2026-10-24 04:21:46.791228
# Unit test for function make_a_pile