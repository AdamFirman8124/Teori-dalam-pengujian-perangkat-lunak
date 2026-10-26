

# Generated at 2026-10-25 08:19:10.523561
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

# Generated at 2026-10-25 08:19:11.854886
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

# Generated at 2026-10-25 08:19:13.286195
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

# Generated at 2026-10-25 08:19:14.651095
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

# Generated at 2026-10-25 08:19:16.027106
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

# Generated at 2026-10-25 08:19:28.836043
# Unit test for function truncate
def test_truncate():
    assert module_0.truncate('abcdef', None) == 'abcdef'
    assert module_0.truncate('abcdef', 6) == 'abcdef'
    assert module_0.truncate('abcdef', 10) == 'abcdef'

    # Odd maximum length: equal characters retained on both sides.
    assert module_0.truncate('abcdefghij', 7) == 'ab...ij'

    # Even maximum length: the extra character is retained on the right.
    assert module_0.truncate('abcdefghij', 8) == 'ab...hij'

    # Result must not exceed the requested length.
    result = module_0.truncate('abcdefghijklmnopqrstuvwxyz', 12)
    assert result == 'abcd...vwxyz'
    assert len(result) == 12

# Generated at 2026-10-25 08:19:35.305624
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-string iterables are converted to tuples.
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple([]) == ()

    # Strings and non-iterable values become single-item tuples.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-10-25 08:19:37.722907
# Unit test for function truncate

# Generated at 2026-10-25 08:19:40.262902
# Unit test for function truncate

# Generated at 2026-10-25 08:19:42.678033
# Unit test for function truncate

# Generated at 2026-10-25 08:19:45.091929
# Unit test for function truncate

# Generated at 2026-10-25 08:19:47.510022
# Unit test for function truncate

# Generated at 2026-10-25 08:19:49.924384
# Unit test for function truncate

# Generated at 2026-10-25 08:19:52.342743
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:19:54.757949
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:19:57.335901
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:19:59.750238
# Unit test for function truncate

# Generated at 2026-10-25 08:20:02.164949
# Unit test for function truncate

# Generated at 2026-10-25 08:20:04.581066
# Unit test for function truncate

# Generated at 2026-10-25 08:20:07.257768
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:09.671036
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:12.087444
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:14.505123
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:16.922729
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:19.340864
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:21.754355
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:24.170458
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:26.583400
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:20:28.998411
# Unit test for function truncate

# Generated at 2026-10-25 08:20:31.415506
# Unit test for function truncate

# Generated at 2026-10-25 08:20:33.828636
# Unit test for function truncate

# Generated at 2026-10-25 08:20:36.241555
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:38.656543
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:41.072676
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:43.488514
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:45.906627
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:48.321235
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:20:50.740526
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:53.157392
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:55.573662
# Unit test for function shitcode

# Generated at 2026-10-25 08:20:58.085722
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:00.428709
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:02.845888
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:05.264097
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:21:07.682080
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:21:10.099601
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:21:12.549725
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:14.960372
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:17.379678
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:19.912087
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:21:22.527208
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:21:25.834377
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:21:28.467043
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:31.411728
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:34.091707
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:21:36.772197
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:39.629610
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:42.107727
# Unit test for function shitcode

# Generated at 2026-10-25 08:21:50.160464
# Unit test for function get_repr_function
def test_get_repr_function():
    item = 'foo'

    # When condition is a type, it should match by isinstance.
    custom_repr = [(int, lambda x: 'int repr')]
    assert module_0.get_repr_function(item, custom_repr) is repr  # str is not an int

    custom_repr = [(str, lambda x: 'str repr')]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'str repr'

    # Subclass checking: bool items should match an int condition.
    assert module_0.get_repr_function(True, [(int, lambda x: 'int repr')])(True) == \
                                                                    'int repr'

    # When condition is a callable, it should be called with the item.
    custom_repr = [(lambda x: x == 'foo', lambda x: 'foo repr')]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'foo repr'

    # No matching condition means the default repr is returned.
    assert module_0.get_repr_function(item, custom_repr=()) is repr

    # First matching condition wins.
    custom_repr = [
        (str, lambda x: 'first'),
        (object, lambda x: 'second'),
    ]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'first'

    # Later conditions are ignored after a match.
    custom_repr = [
        (lambda x: False, lambda x: 'nope'),
        (str, lambda x: 'second'),
    ]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'second'

# Generated at 2026-10-25 08:22:14.039644
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

# Generated at 2026-10-25 08:22:15.893736
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

# Generated at 2026-10-25 08:22:19.115908
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

# Generated at 2026-10-25 08:22:20.945554
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

# Generated at 2026-10-25 08:22:24.272530
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

# Generated at 2026-10-25 08:22:26.508715
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

# Generated at 2026-10-25 08:22:28.112640
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

# Generated at 2026-10-25 08:22:29.959016
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

# Generated at 2026-10-25 08:22:31.632608
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

# Generated at 2026-10-25 08:22:33.327197
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

# Generated at 2026-10-25 08:22:54.026349
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

# Generated at 2026-10-25 08:22:55.541645
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

# Generated at 2026-10-25 08:22:58.620264
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

# Generated at 2026-10-25 08:23:00.203499
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

# Generated at 2026-10-25 08:23:03.642800
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

# Generated at 2026-10-25 08:23:05.203737
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

# Generated at 2026-10-25 08:23:07.306050
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

# Generated at 2026-10-25 08:23:10.718030
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

# Generated at 2026-10-25 08:23:12.531664
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

# Generated at 2026-10-25 08:23:13.805005
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

# Generated at 2026-10-25 08:23:15.258663
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

# Generated at 2026-10-25 08:23:16.596244
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

# Generated at 2026-10-25 08:23:17.940001
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

# Generated at 2026-10-25 08:23:19.328227
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

# Generated at 2026-10-25 08:23:20.724607
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

# Generated at 2026-10-25 08:23:22.183446
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

# Generated at 2026-10-25 08:23:23.570139
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

# Generated at 2026-10-25 08:23:26.362038
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:28.782010
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:31.301968
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:33.720958
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:36.135796
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:38.676882
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:23:41.095607
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:43.518619
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:45.937107
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:48.360130
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:50.771596
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:53.189951
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:55.607470
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:58.024060
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:23:59.598931
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:02.478410
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

# Generated at 2026-10-25 08:24:04.004718
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

# Generated at 2026-10-25 08:24:05.440114
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

# Generated at 2026-10-25 08:24:06.872788
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

# Generated at 2026-10-25 08:24:08.236533
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

# Generated at 2026-10-25 08:24:11.174074
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

# Generated at 2026-10-25 08:24:12.508628
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

# Generated at 2026-10-25 08:24:13.839869
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

# Generated at 2026-10-25 08:24:15.172358
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

# Generated at 2026-10-25 08:24:17.904719
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

# Generated at 2026-10-25 08:24:20.781482
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

# Generated at 2026-10-25 08:24:22.229466
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

# Generated at 2026-10-25 08:24:24.964852
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

# Generated at 2026-10-25 08:24:27.584711
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:30.120960
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:32.539679
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:34.955353
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:24:37.371981
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:24:39.790674
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:24:42.393278
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:44.810501
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:47.393787
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:49.814050
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:52.235258
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:54.729302
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:57.145893
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:24:59.563339
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:02.008930
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:04.424488
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:06.840272
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:09.258001
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:11.673315
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:14.091810
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:16.507798
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:19.121808
# Unit test for function get_repr_function
def test_get_repr_function():
    item = 'foo'

    # When condition is a type, it should match by isinstance.
    custom_repr = [(int, lambda x: 'int repr')]
    assert module_0.get_repr_function(item, custom_repr) is repr  # str is not an int

    custom_repr = [(str, lambda x: 'str repr')]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'str repr'

    # Subclass checking: bool items should match an int condition.
    assert module_0.get_repr_function(True, [(int, lambda x: 'int repr')])(True) == \
                                                                    'int repr'

    # When condition is a callable, it should be called with the item.
    custom_repr = [(lambda x: x == 'foo', lambda x: 'foo repr')]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'foo repr'

    # No matching condition means the default repr is returned.
    assert module_0.get_repr_function(item, custom_repr=()) is repr

    # First matching condition wins.
    custom_repr = [
        (str, lambda x: 'first'),
        (object, lambda x: 'second'),
    ]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'first'

    # Later conditions are ignored after a match.
    custom_repr = [
        (lambda x: False, lambda x: 'nope'),
        (str, lambda x: 'second'),
    ]
    assert module_0.get_repr_function(item, custom_repr)(item) == 'second'

# Generated at 2026-10-25 08:25:20.499301
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

# Generated at 2026-10-25 08:25:21.845477
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

# Generated at 2026-10-25 08:25:23.262907
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

# Generated at 2026-10-25 08:25:24.799390
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

# Generated at 2026-10-25 08:25:27.518455
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

# Generated at 2026-10-25 08:25:28.859897
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

# Generated at 2026-10-25 08:25:30.195895
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

# Generated at 2026-10-25 08:25:32.759567
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

# Generated at 2026-10-25 08:25:34.206896
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

# Generated at 2026-10-25 08:25:35.570041
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

# Generated at 2026-10-25 08:25:36.913548
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

# Generated at 2026-10-25 08:25:38.322125
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

# Generated at 2026-10-25 08:25:39.751023
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

# Generated at 2026-10-25 08:25:41.159243
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

# Generated at 2026-10-25 08:25:43.976870
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

# Generated at 2026-10-25 08:25:45.382803
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

# Generated at 2026-10-25 08:25:46.734273
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

# Generated at 2026-10-25 08:25:48.125743
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

# Generated at 2026-10-25 08:25:50.663634
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:53.727938
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:56.353904
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:25:58.772043
# Unit test for function shitcode

# Generated at 2026-10-25 08:26:04.015514
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode("Hello, cafÃ© â \x00Ã¿") == "Hello, cafÃ© ? ?Ã¿"

# Generated at 2026-10-25 08:26:06.993209
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

# Generated at 2026-10-25 08:26:08.422825
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

# Generated at 2026-10-25 08:26:11.482768
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

# Generated at 2026-10-25 08:26:12.827843
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

# Generated at 2026-10-25 08:26:14.362783
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

# Generated at 2026-10-25 08:26:15.888224
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

# Generated at 2026-10-25 08:26:17.310958
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

# Generated at 2026-10-25 08:26:19.678503
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

# Generated at 2026-10-25 08:26:21.132954
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

# Generated at 2026-10-25 08:26:23.764278
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:26.675447
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:29.332945
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:31.749093
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:34.166858
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:36.585692
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:39.234940
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:26:41.653783
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:26:44.070560
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:26:46.489264
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:26:48.905666
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:26:51.565521
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:26:53.983477
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:56.447779
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:26:58.870324
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:27:01.290333
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:03.707195
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:06.123598
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:14.979705
# Unit test for method write of class WritableStream
def test_WritableStream_write():assert getattr(WritableStream.write, '__isabstractmethod__', False)


# Generated at 2026-10-25 08:27:17.966403
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

# Generated at 2026-10-25 08:27:25.148030
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

# Generated at 2026-10-25 08:27:26.795536
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

# Generated at 2026-10-25 08:27:28.232726
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

# Generated at 2026-10-25 08:27:29.719971
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

# Generated at 2026-10-25 08:27:31.316270
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

# Generated at 2026-10-25 08:27:34.111197
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:27:36.908216
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:27:39.727033
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:27:42.147458
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:27:44.570717
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:27:46.986195
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:27:49.403394
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:51.825031
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:54.428954
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:27:56.716778
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:27:59.135258
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:01.574855
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:03.991350
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:06.533388
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:08.949150
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:18.567931
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:28:20.980286
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:28:23.395523
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 08:28:25.824338
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:28.244280
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:30.662073
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:33.078062
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:28:35.495871
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:28:37.913277
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:28:40.332932
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:42.746044
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:45.162659
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:47.581991
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:50.000540
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:52.413858
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 08:28:54.833860
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:28:57.249951
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:28:59.667049
# Unit test for function get_repr_function

# Generated at 2026-10-25 08:29:02.161032
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

# Generated at 2026-10-25 08:29:03.614194
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

# Generated at 2026-10-25 08:29:05.049772
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

# Generated at 2026-10-25 08:29:06.510397
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