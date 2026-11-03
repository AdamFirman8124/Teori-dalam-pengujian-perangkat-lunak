

# Generated at 2026-11-02 13:24:02.729238
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Basic cases use default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped from the repr
    class WithNewlines(object):
        def __repr__(self):
            return 'line1\rline2\nline3'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2line3'

    # A failing repr results in 'REPR FAILED'
    class BadRepr(object):
        def __repr__(self):
            raise ValueError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # max_length truncates the string, keeping both ends
    long_string = 'abcdefghijklmnopqrstuvwxyz'
    assert module_0.get_shortish_repr(long_string, max_length=10) == 'abc...wxyz'
    # No truncation when shorter than max_length
    assert module_0.get_shortish_repr('abc', max_length=10) == 'abc'
    # max_length=None means no truncation
    assert module_0.get_shortish_repr(long_string) == long_string

    # normalize=True removes memory addresses from default reprs
    class SomeObject(object):
        pass
    raw_repr = repr(SomeObject())
    normalized = module_0.get_shortish_repr(SomeObject(), normalize=True)
    assert ' at 0x' not in normalized
    if ' at 0x' in raw_repr:
        assert normalized == DEFAULT_REPR_RE.sub('', raw_repr)

    # custom_repr with a type condition overrides default repr
    class Custom(object):
        def __repr__(self):
            return 'default repr'
    result = module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'CUSTOM!'),))
    assert result == 'CUSTOM!'

    # custom_repr with a function condition also works
    result = module_0.get_shortish_repr(
        5, custom_repr=((lambda x: x > 3, lambda x: 'BIG'),))
    assert result == 'BIG'

    # custom_repr conditions that don't match fall back to default repr
    assert module_0.get_shortish_repr(
        2, custom_repr=((lambda x: x > 3, lambda x: 'BIG'),)) == '2'

# Generated at 2026-11-02 13:25:33.837428
# Unit test for function get_repr_function
def test_get_repr_function():
    # Test with a type as condition: matching item returns the custom action
    class Foo(object):
        def __repr__(self):
            return 'foo repr'

    class Bar(object):
        pass

    foo = Foo()
    bar = Bar()

    custom_repr = [(Foo, lambda x: 'CUSTOM FOO')]

    action = module_0.get_repr_function(foo, custom_repr)
    assert action is custom_repr[0][1]
    assert action(foo) == 'CUSTOM FOO'

    # Non-matching item should fall back to built-in repr
    assert module_0.get_repr_function(bar, custom_repr) is repr

    # Test with a callable (lambda) condition
    custom_repr = [(lambda x: x == 42, lambda x: 'THE ANSWER')]
    assert module_0.get_repr_function(42, custom_repr)(42) == 'THE ANSWER'
    assert module_0.get_repr_function(43, custom_repr) is repr

    # Test with multiple conditions: first match wins
    custom_repr = [
        (int, lambda x: 'INT: {}'.format(x)),
        (str, lambda x: 'STR: {}'.format(x)),
    ]
    assert module_0.get_repr_function(1, custom_repr)(1) == 'INT: 1'
    assert module_0.get_repr_function('a', custom_repr)('a') == 'STR: a'
    assert module_0.get_repr_function(1.5, custom_repr) is repr

    # Test with empty custom_repr
    assert module_0.get_repr_function(foo, ()) is repr

    # Test that the type-based condition uses isinstance (subclasses match)
    class SubFoo(Foo):
        pass

    custom_repr = [(Foo, lambda x: 'FOO-ISH')]
    assert module_0.get_repr_function(SubFoo(), custom_repr)(SubFoo()) == 'FOO-ISH'

    # Test that the returned action is actually called correctly
    custom_repr = [(Foo, repr)]
    assert module_0.get_repr_function(foo, custom_repr)(foo) == 'foo repr'

# Generated at 2026-11-02 13:28:09.163171
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterable objects are wrapped in a single-element tuple.
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(1.5) == (1.5,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(object()) is not None
    assert module_0.ensure_tuple(object) == (object,)

    # Strings are treated as single items, not iterated character-wise.
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(u'abc') == (u'abc',)
    assert module_0.ensure_tuple('') == ('',)
    assert module_0.ensure_tuple('') != ()

    # Iterables are converted to tuples.
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple({'a': 1, 'b': 2}) == ('a', 'b')

    # Sets / frozensets: converted to a tuple of their members.
    result = module_0.ensure_tuple({1, 2, 3})
    assert isinstance(result, tuple)
    assert set(result) == {1, 2, 3}

    # Empty iterables become empty tuples.
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple(()) == ()
    assert module_0.ensure_tuple({}) == ()

    # Custom iterable objects are converted to tuples.
    class MyIterable(object):
        def __iter__(self):
            return iter((1, 2, 3))
    assert module_0.ensure_tuple(MyIterable()) == (1, 2, 3)

    # Objects with only __getitem__ are not Iterable per
    # collections.abc, so they're wrapped as single items.
    class GetItemOnly(object):
        def __getitem__(self, i):
            raise IndexError
    result = module_0.ensure_tuple(GetItemOnly())
    assert isinstance(result, tuple) and len(result) == 1
    assert isinstance(result[0], GetItemOnly)

    # bytes handling differs between Python 2 and Python 3.
    if isinstance(b'abc', string_types):
        assert module_0.ensure_tuple(b'abc') == (b'abc',)
    else:
        assert module_0.ensure_tuple(b'abc') == (97, 98, 99)

    # Result is always a tuple.
    assert isinstance(module_0.ensure_tuple(1), tuple)
    assert isinstance(module_0.ensure_tuple('abc'), tuple)
    assert isinstance(module_0.ensure_tuple([1]), tuple)

# Generated at 2026-11-02 13:30:48.985821
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom reprs: falls back to the built-in repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('foo', ()) is repr

    # Condition given as a type is translated to an isinstance check
    int_action = lambda x: 'int:{}'.format(x)
    custom_repr = ((int, int_action),)
    assert module_0.get_repr_function(42, custom_repr) is int_action
    assert module_0.get_repr_function('not an int', custom_repr) is repr

    # Subclasses of the given type also match
    class MyInt(int):
        pass
    assert module_0.get_repr_function(MyInt(42), custom_repr) is int_action

    # Condition given as a plain function is called with the item
    calls = []
    def condition(item):
        calls.append(item)
        return item.startswith('yes')

# Generated at 2026-11-02 13:32:35.299897
# Unit test for function normalize_repr
def test_normalize_repr():
    # Removes a typical memory address from a default repr
    assert module_0.normalize_repr('<object object at 0x7f8b2c3d4e5f>') == '<object object>'

    # Handles uppercase hex digits after the 0x prefix
    assert module_0.normalize_repr('<Foo instance at 0xABCDEF12>') == '<Foo instance>'

    # Minimum of 4 hex digits required; shorter addresses are left intact
    assert module_0.normalize_repr('<Foo at 0x123>') == '<Foo at 0x123>'

    # Strings without memory addresses are unchanged
    assert module_0.normalize_repr('Foo(bar=1)') == 'Foo(bar=1)'
    assert module_0.normalize_repr('') == ''

    # Removes all occurrences in the string
    assert module_0.normalize_repr('<a at 0x1234abcd> vs <b at 0x5678ef90>') == '<a> vs <b>'

    # Works on an actual object's repr
    class Foo(object):
        pass
    foo_repr = repr(Foo())
    normalized = module_0.normalize_repr(foo_repr)
    assert ' at 0x' not in normalized
    assert normalized == DEFAULT_REPR_RE.sub('', foo_repr)

    # Non-string input is passed through re.sub, which raises TypeError
    try:
        module_0.normalize_repr(123)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected TypeError for non-string input')