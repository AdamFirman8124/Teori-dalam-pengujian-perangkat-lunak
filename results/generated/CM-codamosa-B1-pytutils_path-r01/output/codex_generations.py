

# Generated at 2026-10-23 19:27:40.348467
# Unit test for function join_each
def test_join_each():
    parent = "/base"
    names = ["a.txt", "sub", "b.log"]

    result = list(module_0.join_each(parent, names))

    assert result == [
        os.path.join("/base", "a.txt"),
        os.path.join("/base", "sub"),
        os.path.join("/base", "b.log"),
    ]


def test_join_each_empty():
    assert list(module_0.join_each("/base", [])) == []


def test_join_each_is_lazy():
    # join_each is a generator: nothing runs until consumed
    def exploding_iterable():
        raise AssertionError("should not be iterated before consumption")
        yield "x"

    gen = module_0.join_each("/base", exploding_iterable())
    assert gen is not iter(gen) or hasattr(gen, "__next__")  # it's a generator
    try:
        next(gen)
    except AssertionError:
        pass  # iterable only touched when consumed â correct


def test_join_each_uses_os_path_join():
    # verify os.path.join is actually called per item
    with patch("os.path.join", wraps=os.path.join) as mock_join:
        list(module_0.join_each("/base", ["x", "y"]))
    assert mock_join.call_count == 2
    mock_join.assert_any_call("/base", "x")
    mock_join.assert_any_call("/base", "y")

# Generated at 2026-10-23 19:27:41.707312
# Unit test for function join_each
def test_join_each():
    parent = "/base"
    names = ["a.txt", "sub", "b.log"]

    result = list(module_0.join_each(parent, names))

    assert result == [
        os.path.join("/base", "a.txt"),
        os.path.join("/base", "sub"),
        os.path.join("/base", "b.log"),
    ]


def test_join_each_empty():
    assert list(module_0.join_each("/base", [])) == []


def test_join_each_is_lazy():
    # join_each is a generator: nothing runs until consumed
    def exploding_iterable():
        raise AssertionError("should not be iterated before consumption")
        yield "x"

    gen = module_0.join_each("/base", exploding_iterable())
    assert gen is not iter(gen) or hasattr(gen, "__next__")  # it's a generator
    try:
        next(gen)
    except AssertionError:
        pass  # iterable only touched when consumed â correct


def test_join_each_uses_os_path_join():
    # verify os.path.join is actually called per item
    with patch("os.path.join", wraps=os.path.join) as mock_join:
        list(module_0.join_each("/base", ["x", "y"]))
    assert mock_join.call_count == 2
    mock_join.assert_any_call("/base", "x")
    mock_join.assert_any_call("/base", "y")

# Generated at 2026-10-23 19:27:43.045877
# Unit test for function join_each
def test_join_each():
    parent = "/base"
    names = ["a.txt", "sub", "b.log"]

    result = list(module_0.join_each(parent, names))

    assert result == [
        os.path.join("/base", "a.txt"),
        os.path.join("/base", "sub"),
        os.path.join("/base", "b.log"),
    ]


def test_join_each_empty():
    assert list(module_0.join_each("/base", [])) == []


def test_join_each_is_lazy():
    # join_each is a generator: nothing runs until consumed
    def exploding_iterable():
        raise AssertionError("should not be iterated before consumption")
        yield "x"

    gen = module_0.join_each("/base", exploding_iterable())
    assert gen is not iter(gen) or hasattr(gen, "__next__")  # it's a generator
    try:
        next(gen)
    except AssertionError:
        pass  # iterable only touched when consumed â correct


def test_join_each_uses_os_path_join():
    # verify os.path.join is actually called per item
    with patch("os.path.join", wraps=os.path.join) as mock_join:
        list(module_0.join_each("/base", ["x", "y"]))
    assert mock_join.call_count == 2
    mock_join.assert_any_call("/base", "x")
    mock_join.assert_any_call("/base", "y")

# Generated at 2026-10-23 19:27:44.310118
# Unit test for function join_each
def test_join_each():
    parent = "/base"
    names = ["a.txt", "sub", "b.log"]

    result = list(module_0.join_each(parent, names))

    assert result == [
        os.path.join("/base", "a.txt"),
        os.path.join("/base", "sub"),
        os.path.join("/base", "b.log"),
    ]


def test_join_each_empty():
    assert list(module_0.join_each("/base", [])) == []


def test_join_each_is_lazy():
    # join_each is a generator: nothing runs until consumed
    def exploding_iterable():
        raise AssertionError("should not be iterated before consumption")
        yield "x"

    gen = module_0.join_each("/base", exploding_iterable())
    assert gen is not iter(gen) or hasattr(gen, "__next__")  # it's a generator
    try:
        next(gen)
    except AssertionError:
        pass  # iterable only touched when consumed â correct


def test_join_each_uses_os_path_join():
    # verify os.path.join is actually called per item
    with patch("os.path.join", wraps=os.path.join) as mock_join:
        list(module_0.join_each("/base", ["x", "y"]))
    assert mock_join.call_count == 2
    mock_join.assert_any_call("/base", "x")
    mock_join.assert_any_call("/base", "y")

# Generated at 2026-10-23 19:27:45.980789
# Unit test for function join_each
def test_join_each():
    parent = "/base"
    names = ["a.txt", "sub", "b.log"]

    result = list(module_0.join_each(parent, names))

    assert result == [
        os.path.join("/base", "a.txt"),
        os.path.join("/base", "sub"),
        os.path.join("/base", "b.log"),
    ]


def test_join_each_empty():
    assert list(module_0.join_each("/base", [])) == []


def test_join_each_is_lazy():
    # join_each is a generator: nothing runs until consumed
    def exploding_iterable():
        raise AssertionError("should not be iterated before consumption")
        yield "x"

    gen = module_0.join_each("/base", exploding_iterable())
    assert gen is not iter(gen) or hasattr(gen, "__next__")  # it's a generator
    try:
        next(gen)
    except AssertionError:
        pass  # iterable only touched when consumed â correct


def test_join_each_uses_os_path_join():
    # verify os.path.join is actually called per item
    with patch("os.path.join", wraps=os.path.join) as mock_join:
        list(module_0.join_each("/base", ["x", "y"]))
    assert mock_join.call_count == 2
    mock_join.assert_any_call("/base", "x")
    mock_join.assert_any_call("/base", "y")