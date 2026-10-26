

# Generated at 2026-10-25 06:24:26.534325
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, "a", 2.5, None, 3]) == [1, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers(["a", None, 1.0]) == []
    assert module_0.filter_integers([[1], {"a": 1}, 7]) == [7]


def test_filter_integers_bool_behavior():
    # bool subclasses int, so isinstance(True, int) is True.
    # Current function KEEPS booleans. To exclude them, use:
    #     return [x for x in values if type(x) is int]
    assert module_0.filter_integers([True, False, 1, 0]) == [True, False, 1, 0]

# Generated at 2026-10-25 06:24:29.065561
# Unit test for function filter_integers

# Generated at 2026-10-25 06:24:31.402652
# Unit test for function filter_integers

# Generated at 2026-10-25 06:24:33.823769
# Unit test for function filter_integers

# Generated at 2026-10-25 06:24:35.147912
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, "a", 2.5, None, 3]) == [1, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers(["a", None, 1.0]) == []
    assert module_0.filter_integers([[1], {"a": 1}, 7]) == [7]


def test_filter_integers_bool_behavior():
    # bool subclasses int, so isinstance(True, int) is True.
    # Current function KEEPS booleans. To exclude them, use:
    #     return [x for x in values if type(x) is int]
    assert module_0.filter_integers([True, False, 1, 0]) == [True, False, 1, 0]

# Generated at 2026-10-25 06:24:36.593038
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, "a", 2.5, None, 3]) == [1, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers(["a", None, 1.0]) == []
    assert module_0.filter_integers([[1], {"a": 1}, 7]) == [7]


def test_filter_integers_bool_behavior():
    # bool subclasses int, so isinstance(True, int) is True.
    # Current function KEEPS booleans. To exclude them, use:
    #     return [x for x in values if type(x) is int]
    assert module_0.filter_integers([True, False, 1, 0]) == [True, False, 1, 0]

# Generated at 2026-10-25 06:24:37.993950
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, "a", 2.5, None, 3]) == [1, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers(["a", None, 1.0]) == []
    assert module_0.filter_integers([[1], {"a": 1}, 7]) == [7]


def test_filter_integers_bool_behavior():
    # bool subclasses int, so isinstance(True, int) is True.
    # Current function KEEPS booleans. To exclude them, use:
    #     return [x for x in values if type(x) is int]
    assert module_0.filter_integers([True, False, 1, 0]) == [True, False, 1, 0]