

# Generated at 2026-10-24 05:59:55.519783
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

# Generated at 2026-10-24 05:59:56.823623
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

# Generated at 2026-10-24 05:59:58.145254
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

# Generated at 2026-10-24 05:59:59.454328
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

# Generated at 2026-10-24 06:00:00.781666
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