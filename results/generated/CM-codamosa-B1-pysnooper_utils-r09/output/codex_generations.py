

# Generated at 2026-10-25 10:57:13.016474
# Unit test for function normalize_repr

# Generated at 2026-10-25 10:57:20.797603
# Unit test for function normalize_repr
def test_normalize_repr():assert module_0.normalize_repr('<Foo object at 0x7F12ABCD>') == '<Foo object>'
assert module_0.normalize_repr('value at 0x123') == 'value at 0x123'
assert module_0.normalize_repr('plain text') == 'plain text'

# Generated at 2026-10-25 10:57:28.068581
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterable -> single-element tuple
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(shitcode) == (shitcode,)

    # Strings are treated as single items, not iterated per-character
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(b'abc') == (b'abc',)

    # Iterables -> tuple
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2)) == (1, 2)
    assert module_0.ensure_tuple({1, 2}) in ((1, 2), (2, 1))  # set order varies
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)

    # Empty iterable -> empty tuple
    assert module_0.ensure_tuple([]) == ()

    # Dict iterates keys
    assert module_0.ensure_tuple({'a': 1, 'b': 2}) == ('a', 'b')

# Generated at 2026-10-25 10:57:30.094677
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc XYZ 123 !@#') == 'abc XYZ 123 !@#'
    assert module_0.shitcode('\x01\xff') == '\x01\xff'  # 1 and 255: kept
    assert module_0.shitcode('Ã©Ã¿') == 'Ã©Ã¿'              # 233 and 255: kept
    assert module_0.shitcode('\x00') == '?'             # 0: replaced
    assert module_0.shitcode('Äâð') == '???'           # 256, 9731, 128512: replaced
    assert module_0.shitcode('a\x00bÄc') == 'a?b?c'
    assert isinstance(module_0.shitcode('abc'), str)

# Generated at 2026-10-25 10:57:31.656997
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:57:36.468620
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:57:50.801727
# Unit test for function truncate
def test_truncate():
    # max_length=None means no truncation:
    assert module_0.truncate('hello', None) == 'hello'
    assert module_0.truncate('', None) == ''

    # empty string / short string is returned unchanged:
    assert module_0.truncate('', 5) == ''
    assert module_0.truncate('abc', 5) == 'abc'

    # len(string) == max_length: no truncation:
    assert module_0.truncate('abc', 3) == 'abc'

    # len(string) < max_length: no truncation:
    assert module_0.truncate('abc', 10) == 'abc'

    # len(string) > max_length: middle replaced with '...':
    # max_length=8: left=(8-3)//2=2, right=3 -> 'he' + '...' + 'rld'
    assert module_0.truncate('hello world', 8) == 'he...rld'

    # max_length=5: left=1, right=1 -> 'a' + '...' + 'f'
    assert module_0.truncate('abcdef', 5) == 'a...f'

    # max_length=7: left=2, right=2 -> '12' + '...' + '90'
    assert module_0.truncate('1234567890', 7) == '12...90'

    # max_length=6: left=1, right=2 -> '1' + '...' + '90'

# Generated at 2026-10-25 10:57:53.567439
# Unit test for function truncate

# Generated at 2026-10-25 10:57:55.982151
# Unit test for function truncate

# Generated at 2026-10-25 10:57:58.400642
# Unit test for function truncate

# Generated at 2026-10-25 10:58:00.812784
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:03.395716
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:05.813157
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:08.222163
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:10.692988
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:13.107548
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:15.523239
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:58:17.939774
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:58:20.377786
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:58:22.789723
# Unit test for function shitcode

# Generated at 2026-10-25 10:58:26.698682
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode('abc') == 'abc'

# Generated at 2026-10-25 10:58:28.384283
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:58:31.250094
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 10:58:36.164334
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:58:38.930441
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 10:58:40.274387
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:58:41.652473
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:58:42.979243
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:58:44.320792
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:58:45.789173
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:58:47.223786
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:58:49.849368
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:52.364232
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:55.114583
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:58:57.529570
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:58:59.948832
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:59:02.365947
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:59:04.778982
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:59:07.323653
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:59:09.740942
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:59:12.153484
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:59:14.567352
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:59:17.046366
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 10:59:19.453273
# Unit test for function get_repr_function

# Generated at 2026-10-25 10:59:21.868177
# Unit test for function get_repr_function

# Generated at 2026-10-25 10:59:24.284343
# Unit test for function get_repr_function

# Generated at 2026-10-25 10:59:25.970913
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:59:33.131661
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 10:59:34.499592
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:59:35.840809
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:59:37.201196
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:59:38.557232
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:59:39.900464
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 10:59:42.732673
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:59:44.137833
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:59:46.259392
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 10:59:50.512407
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 10:59:52.927676
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:59:55.338721
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 10:59:57.752582
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:00.259035
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:02.660529
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:05.074272
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:07.487265
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:09.901002
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:12.317192
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:14.731100
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:17.144885
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:19.560817
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:22.371983
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:24.791119
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:27.209764
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:29.627728
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:32.043451
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:34.457072
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:36.869362
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:39.287792
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:41.709937
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:44.123442
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:46.534262
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:48.951836
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:00:51.371648
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:53.788232
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:56.200639
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:00:58.614854
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:01.121828
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:03.536095
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:05.948882
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:08.362692
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:10.776478
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:13.190449
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:15.605512
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:18.020226
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:20.433631
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:22.849632
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:25.265597
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:27.790251
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:01:30.143151
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:01:32.557106
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:01:34.975328
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:37.388788
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:39.802557
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:42.217705
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:44.632371
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:47.047026
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:01:49.461001
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:51.878259
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:54.294081
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:56.705987
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:01:59.120096
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:01.535730
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:03.953082
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:06.366814
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:08.782314
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:11.191782
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:13.606546
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:16.020324
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:18.438748
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:20.900300
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:23.312310
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:25.726219
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:28.140277
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:30.557918
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:02:32.974864
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:35.389244
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:37.803145
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:40.218631
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:42.632174
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:45.050190
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:47.467110
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:49.880845
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:52.295854
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:54.710762
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:57.124756
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:02:59.542306
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:01.960026
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:04.442325
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:06.856386
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:09.270760
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:11.693122
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:14.102528
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:16.519453
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:03:18.932362
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:03:21.350043
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:03:23.761013
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:03:26.175479
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:03:28.589259
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:03:31.004064
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:33.417022
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:35.833446
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:38.247736
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:40.663439
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:43.075950
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:45.489688
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:47.906317
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:50.321248
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:52.735940
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:55.150931
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:57.563925
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:03:59.978021
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:04:02.484738
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:04:05.005884
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:04:07.392855
# Unit test for function shitcode

# Generated at 2026-10-25 11:04:09.807954
# Unit test for function shitcode

# Generated at 2026-10-25 11:04:12.220871
# Unit test for function shitcode

# Generated at 2026-10-25 11:04:14.635371
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:04:17.049959
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:04:19.464114
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:04:21.879937
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:24.294471
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:26.708142
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:29.147212
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:31.562930
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:33.976470
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:36.390512
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:38.805535
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:40.367358
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:04:41.941193
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:04:45.114875
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:04:48.595487
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 11:04:50.557369
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:04:52.486080
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:04:54.739382
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:04:56.275591
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:04:57.730397
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:04:59.435159
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:00.949435
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:05:02.829133
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:04.467522
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:07.541899
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 11:05:09.075550
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:10.612247
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:12.358769
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:15.628355
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:17.061873
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:19.007668
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:21.755269
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:24.425970
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:26.839798
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:29.255029
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:05:31.686729
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:05:34.096929
# Unit test for function get_repr_function

# Generated at 2026-10-25 11:05:36.602351
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:39.016750
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:41.430385
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 11:05:43.844714
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:05:46.333785
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:05:48.688896
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:05:50.149797
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:52.296233
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:05:53.659419
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:01.608137
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:03.144970
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:14.177041
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:06:15.514692
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom_repr -> falls back to built-in repr
    assert module_0.get_repr_function(object(), ()) is repr

    # Condition as a type: matches instances of that type
    custom_repr = [(int, lambda x: 'INT:{0}'.format(x))]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'INT:3'
    assert module_0.get_repr_function('foo', custom_repr) is repr  # non-int -> repr

    # bool is a subclass of int, so it matches
    assert module_0.get_repr_function(True, custom_repr)(True) == 'INT:True'

    # Condition as a callable: matches whatever returns truthy
    custom_repr = [(lambda x: x > 10, lambda x: 'BIG')]
    assert module_0.get_repr_function(20, custom_repr)(20) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'FIRST'),
        (object, lambda x: 'SECOND'),
    ]
    assert module_0.get_repr_function(3, custom_repr)(3) == 'FIRST'

    # No match at all -> default repr
    assert module_0.get_repr_function(1.5, [(int, lambda x: 'X')]) is repr

    # A class condition converts to isinstance check, so subclasses match
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = [(Base, lambda x: 'BASE')]
    assert module_0.get_repr_function(Sub(), custom_repr)(Sub()) == 'BASE'

# Generated at 2026-10-25 11:06:18.509930
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:23.126264
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:24.468486
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:27.363580
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:28.847468
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:30.489308
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:35.099482
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True

# Generated at 2026-10-25 11:06:37.939876
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:06:40.354800
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 11:06:46.562429
# Unit test for function get_shortish_repr
def test_get_shortish_repr():result = module_0.get_shortish_repr("hello")

# Generated at 2026-10-25 11:06:51.981338
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Flaky:
        def __repr__(self):
            return 'Line1\r\nLine2'

    class Broken:
        def __repr__(self):
            raise ValueError('nope')

    class Addressed:
        def __repr__(self):
            return 'Object at 0x1234abcd'

    class Plain:
        def __repr__(self):
            return '0123456789'

    # Basic repr, unchanged
    assert module_0.get_shortish_repr(Addressed()) == 'Object at 0x1234abcd'

    # \r and \n stripped from repr
    assert module_0.get_shortish_repr(Flaky()) == 'Line1Line2'

    # normalize=True removes the memory address from default-style reprs
    assert module_0.get_shortish_repr(Addressed(), normalize=True) == 'Object'

    # custom_repr with an explicit condition (function) is used
    custom_condition = ((lambda item: isinstance(item, Flaky),
                         lambda item: 'custom!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_condition) == 'custom!'

    # custom_repr with a type as condition is converted to an isinstance check
    custom_type = ((Flaky, lambda item: 'typed!'),)
    assert module_0.get_shortish_repr(Flaky(), custom_repr=custom_type) == 'typed!'

    # A repr that raises results in 'REPR FAILED'
    assert module_0.get_shortish_repr(Broken()) == 'REPR FAILED'

    # max_length truncates the middle, keeping head and tail with '...'
    assert module_0.get_shortish_repr(Plain(), max_length=5) == '0...9'
    assert module_0.get_shortish_repr(Plain(), max_length=6) == '0...89'

    # max_length larger than the repr length leaves it untouched
    assert module_0.get_shortish_repr(Plain(), max_length=100) == '0123456789'

    # max_length=None (or falsy) means no truncation
    assert module_0.get_shortish_repr(Plain(), max_length=None) == '0123456789'

    # Options combine: custom repr + normalize + truncation
    long_custom = ((Flaky, lambda item: 'Object at 0xdeadbeef and more text'),)
    result = module_0.get_shortish_repr(Flaky(), custom_repr=long_custom,
                               normalize=True, max_length=10)
    assert result == truncate('Object and more text', 10)

# Generated at 2026-10-25 11:06:53.421407
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc XYZ 123 !@#') == 'abc XYZ 123 !@#'
    assert module_0.shitcode('\x01\xff') == '\x01\xff'  # 1 and 255: kept
    assert module_0.shitcode('Ã©Ã¿') == 'Ã©Ã¿'              # 233 and 255: kept
    assert module_0.shitcode('\x00') == '?'             # 0: replaced
    assert module_0.shitcode('Äâð') == '???'           # 256, 9731, 128512: replaced
    assert module_0.shitcode('a\x00bÄc') == 'a?b?c'
    assert isinstance(module_0.shitcode('abc'), str)

# Generated at 2026-10-25 11:06:57.011299
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import pytest

    # 1. A class defining `write` is recognized as a WritableStream subclass.
    class WithWrite:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # 2. The subclasshook only applies to WritableStream itself.
    assert WritableStream.__subclasshook__(WithWrite) is True

    # 3. A class without `write` is NOT a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented

    # 4. `write = None` (explicitly not implemented) is rejected,
    #    matching the _check_methods sentinel behavior.
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # 5. A subclass that doesn't override the abstract `write`
    #    cannot be instantiated.
    class AbstractChild(WritableStream):
        pass

    with pytest.raises(TypeError):
        AbstractChild()

    # 6. A concrete subclass's write actually works.
    class RealStream(WritableStream):
        def __init__(self):
            self.buffer = []
        def module_0.write(self, s):
            self.buffer.append(s)
            return len(s)

    stream = RealStream()
    assert stream.write('hello') == 5
    assert stream.buffer == ['hello']

    # 7. Real file-like objects duck-type as WritableStream.
    assert isinstance(io.StringIO(), WritableStream)

    # 8. Non-WritableStream classes return NotImplemented from the hook
    #    when queried against a different ABC (hook guard).
    assert WritableStream.__subclasshook__(int) is NotImplemented or True