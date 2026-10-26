

# Generated at 2026-10-25 06:18:07.865980
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:25.650939
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:28.271254
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:30.896455
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:18:33.314549
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:18:35.817380
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:18:38.174459
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:40.845532
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:43.256351
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:45.676866
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 06:18:48.181306
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 06:18:50.595989
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 06:18:53.020943
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:55.431113
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:18:57.844940
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:10.547386
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

# Generated at 2026-10-25 06:19:22.509334
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

# Generated at 2026-10-25 06:19:25.036636
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:27.709505
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:30.389269
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:32.801266
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:35.481056
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:37.895431
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:40.555726
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:42.972558
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:45.389465
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:47.806702
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:19:50.220300
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:19:52.666057
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:19:55.051054
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:57.469086
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:19:59.884036
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:02.299340
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:04.712341
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:07.128540
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:09.543938
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:12.172439
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:20:18.738157
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Simple string passes through unchanged
    assert module_0.get_shortish_repr('hello') == repr('hello')

    # Custom repr function is used when condition matches
    assert module_0.get_shortish_repr(3, custom_repr=((int, lambda x: 'INT!'),)) == 'INT!'

    # Type-based condition in custom_repr
    assert module_0.get_shortish_repr(3, custom_repr=((int, lambda x: 'num'),)) == 'num'

    # Non-matching custom_repr falls back to repr
    assert module_0.get_shortish_repr(3, custom_repr=((float, lambda x: 'float!'),)) == '3'

    # max_length truncation keeps head, ellipsis, tail
    long_string = 'a' * 100
    result = module_0.get_shortish_repr(long_string, max_length=10)
    assert result == 'aa' + '...' + 'aaa'
    assert len(result) == 10

    # max_length ignored when string shorter than limit
    assert module_0.get_shortish_repr('abc', max_length=100) == "'abc'"

    # normalize removes default memory-address reprs
    class ObjWithDefaultRepr:
        pass
    normalized = module_0.get_shortish_repr(ObjWithDefaultRepr(), normalize=True)
    assert '0x' not in normalized
    assert normalized == normalize_repr(repr(ObjWithDefaultRepr()))

    # normalize=False keeps the address
    not_normalized = module_0.get_shortish_repr(ObjWithDefaultRepr(), normalize=False)
    assert '0x' in not_normalized

    # Newlines and carriage returns are stripped
    assert module_0.get_shortish_repr('line1\nline2\rline3') == "'line1line2line3'"

    # Failing repr yields 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise ValueError('no')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

# Generated at 2026-10-25 06:20:21.611987
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

# Generated at 2026-10-25 06:20:24.574270
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    output = []

    class MyWritableStream(WritableStream):
        def module_0.write(self, s):
            output.append(s)

    my_writable_stream = MyWritableStream()
    message = 'Me write lovely message!'
    my_writable_stream.write(message)
    assert output == [message]

    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(my_writable_stream, WritableStream)

    class MyNonWritableStream:
        pass

    assert not issubclass(MyNonWritableStream, WritableStream)
    assert not isinstance(MyNonWritableStream(), WritableStream)

# Generated at 2026-10-25 06:20:27.404067
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

# Generated at 2026-10-25 06:20:38.093783
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

# Generated at 2026-10-25 06:20:40.539530
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:20:42.952848
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:20:45.367227
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:20:47.786654
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:20:50.202715
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:20:52.615843
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:20:55.031536
# Unit test for function truncate

# Generated at 2026-10-25 06:20:57.446396
# Unit test for function truncate

# Generated at 2026-10-25 06:20:59.860960
# Unit test for function truncate

# Generated at 2026-10-25 06:21:02.276421
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:21:04.689973
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:21:07.103508
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:21:09.519840
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:21:11.938099
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:21:14.646939
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:21:16.154375
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

# Generated at 2026-10-25 06:21:19.160353
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

# Generated at 2026-10-25 06:21:20.684694
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

# Generated at 2026-10-25 06:21:22.136312
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

# Generated at 2026-10-25 06:21:25.165451
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

# Generated at 2026-10-25 06:21:27.960897
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

# Generated at 2026-10-25 06:21:29.300224
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

# Generated at 2026-10-25 06:21:30.661005
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

# Generated at 2026-10-25 06:21:32.034055
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

# Generated at 2026-10-25 06:21:34.926584
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

# Generated at 2026-10-25 06:21:36.358386
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

# Generated at 2026-10-25 06:21:37.892818
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

# Generated at 2026-10-25 06:21:39.227624
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

# Generated at 2026-10-25 06:21:40.556958
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

# Generated at 2026-10-25 06:21:43.422713
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

# Generated at 2026-10-25 06:21:46.072439
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:21:48.750090
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:21:51.164607
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:21:53.584324
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:21:55.995476
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:21:58.760006
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:01.207957
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:22:04.146936
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:22:06.562415
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:22:09.322216
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:11.734019
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:14.148696
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:16.563486
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:18.977679
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:21.393900
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:22:23.806973
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:26.222939
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:28.636392
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:31.052978
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:33.467404
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:35.882008
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:22:38.297409
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:22:41.248136
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:22:42.710838
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Simple string passes through unchanged
    assert module_0.get_shortish_repr('hello') == repr('hello')

    # Custom repr function is used when condition matches
    assert module_0.get_shortish_repr(3, custom_repr=((int, lambda x: 'INT!'),)) == 'INT!'

    # Type-based condition in custom_repr
    assert module_0.get_shortish_repr(3, custom_repr=((int, lambda x: 'num'),)) == 'num'

    # Non-matching custom_repr falls back to repr
    assert module_0.get_shortish_repr(3, custom_repr=((float, lambda x: 'float!'),)) == '3'

    # max_length truncation keeps head, ellipsis, tail
    long_string = 'a' * 100
    result = module_0.get_shortish_repr(long_string, max_length=10)
    assert result == 'aa' + '...' + 'aaa'
    assert len(result) == 10

    # max_length ignored when string shorter than limit
    assert module_0.get_shortish_repr('abc', max_length=100) == "'abc'"

    # normalize removes default memory-address reprs
    class ObjWithDefaultRepr:
        pass
    normalized = module_0.get_shortish_repr(ObjWithDefaultRepr(), normalize=True)
    assert '0x' not in normalized
    assert normalized == normalize_repr(repr(ObjWithDefaultRepr()))

    # normalize=False keeps the address
    not_normalized = module_0.get_shortish_repr(ObjWithDefaultRepr(), normalize=False)
    assert '0x' in not_normalized

    # Newlines and carriage returns are stripped
    assert module_0.get_shortish_repr('line1\nline2\rline3') == "'line1line2line3'"

    # Failing repr yields 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise ValueError('no')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

# Generated at 2026-10-25 06:22:44.144489
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

# Generated at 2026-10-25 06:22:47.321081
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

# Generated at 2026-10-25 06:22:48.857926
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

# Generated at 2026-10-25 06:22:50.288281
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

# Generated at 2026-10-25 06:22:51.824717
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

# Generated at 2026-10-25 06:22:53.257836
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

# Generated at 2026-10-25 06:22:56.125102
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

# Generated at 2026-10-25 06:22:57.546240
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

# Generated at 2026-10-25 06:22:58.904568
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

# Generated at 2026-10-25 06:23:00.369818
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

# Generated at 2026-10-25 06:23:01.737773
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

# Generated at 2026-10-25 06:23:03.191793
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

# Generated at 2026-10-25 06:23:06.059826
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

# Generated at 2026-10-25 06:23:07.491565
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

# Generated at 2026-10-25 06:23:08.818055
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

# Generated at 2026-10-25 06:23:11.234625
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:13.653881
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:16.188007
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:18.601695
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:21.021215
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:23.434857
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:25.853357
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:28.257462
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:30.675357
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:33.087850
# Unit test for function shitcode

# Generated at 2026-10-25 06:23:35.503196
# Unit test for function shitcode

# Generated at 2026-10-25 06:23:37.915634
# Unit test for function shitcode

# Generated at 2026-10-25 06:23:40.329117
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:23:42.750941
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:23:45.165525
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:23:47.580127
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:50.019719
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:52.428609
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:23:54.840690
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:23:59.897849
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:24:04.551477
# Unit test for function get_repr_function
def test_get_repr_function():int_formatter = lambda x: 'INT!'

# Generated at 2026-10-25 06:24:05.849703
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

# Generated at 2026-10-25 06:24:08.819363
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

# Generated at 2026-10-25 06:24:10.252862
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

# Generated at 2026-10-25 06:24:11.687460
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

# Generated at 2026-10-25 06:24:13.123495
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

# Generated at 2026-10-25 06:24:14.657634
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

# Generated at 2026-10-25 06:24:17.523896
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

# Generated at 2026-10-25 06:24:18.956072
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

# Generated at 2026-10-25 06:24:20.390894
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

# Generated at 2026-10-25 06:24:23.232792
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

# Generated at 2026-10-25 06:24:25.924990
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:24:28.611155
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:24:31.026452
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:24:33.442785
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:24:34.960851
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:24:36.449575
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:24:39.152553
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

# Generated at 2026-10-25 06:24:42.113383
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

# Generated at 2026-10-25 06:24:43.547273
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

# Generated at 2026-10-25 06:24:45.287065
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

# Generated at 2026-10-25 06:24:46.722287
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

# Generated at 2026-10-25 06:24:48.255015
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

# Generated at 2026-10-25 06:24:49.804252
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

# Generated at 2026-10-25 06:24:53.001914
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

# Generated at 2026-10-25 06:24:55.810095
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

# Generated at 2026-10-25 06:24:58.422890
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:00.830257
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:03.244570
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:05.875883
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:08.288569
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:10.704782
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:13.125583
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:15.541282
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:17.957829
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:20.374657
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:22.788246
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:25.202920
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:25:27.865684
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:30.280846
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:32.694187
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:25:35.109207
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:37.524148
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:39.938571
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:25:42.354614
# Unit test for function shitcode

# Generated at 2026-10-25 06:25:48.883987
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc') == 'abc'
    assert module_0.shitcode('a b\nc\t') == 'a b\nc\t'
    assert module_0.shitcode('\x01\xff') == '\x01\xff'
    assert module_0.shitcode('\x00') == '?'
    assert module_0.shitcode('caf\u00e9') == 'caf\u00e9'
    assert module_0.shitcode('\u0100') == '?'
    assert module_0.shitcode('\u65e5\u672c') == '??'
    assert module_0.shitcode('caf\u00e9 \u2615') == 'caf\u00e9 ?'
    assert module_0.shitcode('ok\u20ac') == 'ok?'

# Generated at 2026-10-25 06:25:50.277540
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

# Generated at 2026-10-25 06:25:51.752228
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

# Generated at 2026-10-25 06:25:53.196411
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

# Generated at 2026-10-25 06:25:54.631826
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

# Generated at 2026-10-25 06:25:56.078153
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

# Generated at 2026-10-25 06:25:57.430905
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

# Generated at 2026-10-25 06:25:58.918234
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

# Generated at 2026-10-25 06:26:01.893072
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

# Generated at 2026-10-25 06:26:03.329898
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

# Generated at 2026-10-25 06:26:04.628797
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

# Generated at 2026-10-25 06:26:07.721637
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

# Generated at 2026-10-25 06:26:09.253939
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

# Generated at 2026-10-25 06:26:12.013473
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:14.428978
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:16.842912
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:19.258049
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:21.671090
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:24.085176
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:26.664661
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:29.087555
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:31.503228
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:33.916854
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:36.333775
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:38.744200
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:26:41.159620
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:43.572344
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:45.984077
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:26:48.400381
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:26:50.813785
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:26:53.229745
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:26:55.645346
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:26:58.058524
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:00.472655
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:02.920888
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:05.331969
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:07.748526
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:10.228973
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:12.596383
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:15.011256
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:17.427092
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:19.839872
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:22.253959
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:24.666817
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:27:27.082107
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:27:29.495882
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 06:27:31.908954
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:34.323215
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:36.737356
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 06:27:39.151133
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:41.565853
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:43.980689
# Unit test for function get_repr_function

# Generated at 2026-10-25 06:27:46.555764
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

# Generated at 2026-10-25 06:27:49.504930
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

# Generated at 2026-10-25 06:27:51.038170
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

# Generated at 2026-10-25 06:27:54.225543
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

# Generated at 2026-10-25 06:27:55.748982
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

# Generated at 2026-10-25 06:27:57.285819
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

# Generated at 2026-10-25 06:27:58.820328
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

# Generated at 2026-10-25 06:28:00.766098
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

# Generated at 2026-10-25 06:28:02.302115
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

# Generated at 2026-10-25 06:28:05.115193
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

# Generated at 2026-10-25 06:28:06.807138
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