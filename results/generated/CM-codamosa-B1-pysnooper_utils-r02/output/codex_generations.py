

# Generated at 2026-10-24 21:57:54.185076
# Unit test for function normalize_repr
def test_normalize_repr():
    assert module_0.normalize_repr('<Foo object at 0x7f8A12BC>') == '<Foo object>'
    assert module_0.normalize_repr('<Foo object at 0x0000>') == '<Foo object>'
    assert module_0.normalize_repr('value at 0xABCD and at 0x123456') == 'value and'
    assert module_0.normalize_repr('ordinary representation') == 'ordinary representation'
    assert module_0.normalize_repr('at 0x123') == 'at 0x123'  # Fewer than four hex digits.

# Generated at 2026-10-24 21:57:56.851368
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:57:59.365881
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:01.902711
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:04.322328
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:06.737171
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:09.353017
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:11.761093
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:58:14.179089
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:58:16.595599
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:58:19.011978
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:21.431162
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:23.847123
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:58:39.755582
# Unit test for function truncate
def test_truncate():
    value = 'abcdefghij'

    # No truncation required.
    assert module_0.truncate(value, None) == value
    assert module_0.truncate(value, 10) == value
    assert module_0.truncate(value, 20) == value

    # Odd and even maximum lengths.
    assert module_0.truncate(value, 9) == 'abc...hij'
    assert module_0.truncate(value, 8) == 'ab...hij'
    assert module_0.truncate(value, 7) == 'ab...ij'

    result = module_0.truncate(value, 6)
    assert result == 'a...ij'
    assert len(result) == 6

# Generated at 2026-10-24 21:58:45.144738
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:58:46.488413
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:58:47.805216
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:58:49.129335
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

# Generated at 2026-10-24 21:58:55.113078
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:58:56.442211
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:58:57.766292
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:11.752086
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritable:
        def __init__(self):
            self.written = None

        def module_0.write(self, s):
            self.written = s
            return len(s)

    stream = TestWritable()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.written == 'hello'

# Generated at 2026-10-24 21:59:14.174709
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:16.591091
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:19.008148
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:21.427583
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:23.842966
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:26.262455
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:28.679787
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:59:31.096341
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:59:32.464136
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:59:35.356090
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:59:36.790415
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:59:42.034564
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:43.444969
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:44.778783
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:59:59.114373
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream:
        def module_0.write(self, s):
            return len(s)

    stream = ConcreteWritableStream()

    assert issubclass(ConcreteWritableStream, WritableStream)
    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5

# Generated at 2026-10-24 22:00:00.442229
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:01.877099
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:03.249734
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

# Generated at 2026-10-24 22:00:04.644813
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:00:07.459359
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:00:08.791983
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:00:10.143984
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:00:15.701235
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:18.121398
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:20.539858
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:22.957533
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:25.374602
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:26.758791
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:28.157363
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

# Generated at 2026-10-24 22:00:29.524270
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:00:32.393260
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:00:33.718349
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:00:47.344119
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:48.679638
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:50.025087
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:00:52.769502
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:00:54.087962
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:00:56.970969
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:00:58.299931
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:00:59.633565
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:01:00.957933
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:01:03.754130
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:01:05.154995
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:01:20.008986
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream:
        def module_0.write(self, s):
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert issubclass(ConcreteWritableStream, WritableStream)
    assert stream.write("hello") == 5


def test_WritableStream_cannot_be_instantiated_without_write():
    with pytest.raises(TypeError):
        WritableStream()

# Generated at 2026-10-24 22:01:22.632514
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:01:25.054485
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:01:48.168982
# Unit test for function get_repr_function
def test_get_repr_function():assert module_0.get_repr_function(42, ()) is repr

# Generated at 2026-10-24 22:01:49.509546
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

# Generated at 2026-10-24 22:02:05.972719
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WithWrite(object):
        def module_0.write(self, s):
            return len(s)

    class WithoutWrite(object):
        pass

    class WithNoneWrite(object):
        write = None

    # Duck-typed subclasshook: having `write` is enough.
    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # Missing or None `write` must not qualify.
    assert not issubclass(WithoutWrite, WritableStream)
    assert not issubclass(WithNoneWrite, WritableStream)

    # Abstract base itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    # The method is actually callable on a concrete implementation.
    assert WithWrite().write('abc') == 3

# Generated at 2026-10-24 22:02:07.297246
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:02:08.623913
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:02:09.980714
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:02:21.961414
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream:
        def module_0.write(self, s):
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5


def test_WritableStream_requires_write():
    class NonWritableStream:
        pass

    assert not isinstance(NonWritableStream(), WritableStream)

# Generated at 2026-10-24 22:02:24.383827
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:02:26.801664
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:02:29.219330
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:02:31.639502
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:02:33.011033
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:02:50.832295
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

# Generated at 2026-10-24 22:02:53.704738
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:02:55.051041
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:02:56.403620
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:03:12.444462
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def module_0.write(self, s):
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert isinstance(stream, WritableStream)

    class DuckTypedWritableStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedWritableStream, WritableStream)
    assert isinstance(DuckTypedWritableStream(), WritableStream)

    class NonWritableStream:
        pass

    assert not issubclass(NonWritableStream, WritableStream)
    assert not isinstance(NonWritableStream(), WritableStream)


def test_WritableStream_is_abstract():
    with pytest.raises(TypeError):
        WritableStream()

# Generated at 2026-10-24 22:03:13.801977
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:16.330956
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:18.863003
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:21.273872
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:23.694348
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:26.115867
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:28.530318
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:30.947194
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:33.367486
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:35.783376
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:38.201847
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:40.618689
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:43.037656
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:45.453144
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:03:47.871824
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:03:50.290782
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:03:52.705964
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:03:55.130139
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:03:57.546287
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:04:00.249992
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(123) == '123'

# Generated at 2026-10-24 22:04:25.776454
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import pytest

    # The abstract base class cannot be instantiated directly.
    with pytest.raises(TypeError):
        WritableStream()

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.contents == ['hello']

# Generated at 2026-10-24 22:04:27.104468
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:04:28.492783
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:04:29.840174
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:04:40.875225
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ExampleStream:
        def module_0.write(self, s):
            return len(s)

    stream = ExampleStream()
    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5

# Generated at 2026-10-24 22:04:42.200378
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:04:43.532100
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:04:46.182613
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:04:48.701839
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:04:51.122463
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:04:53.697893
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:04:56.117959
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:04:58.532359
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:05:00.948967
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:03.366079
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:05.783565
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:08.200544
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:05:10.617284
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:05:13.035553
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:05:15.454066
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:05:17.869865
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:05:20.287262
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:05:22.705858
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:25.123053
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:27.544185
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:29.959487
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:32.381059
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:33.700200
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:50.244458
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WithWrite(object):
        def module_0.write(self, s):
            return len(s)

    class WithoutWrite(object):
        pass

    class WithNoneWrite(object):
        write = None

    # Duck-typed subclasshook: having `write` is enough.
    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # Missing or None `write` must not qualify.
    assert not issubclass(WithoutWrite, WritableStream)
    assert not issubclass(WithNoneWrite, WritableStream)

    # Abstract base itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    # The method is actually callable on a concrete implementation.
    assert WithWrite().write('abc') == 3

# Generated at 2026-10-24 22:05:51.621456
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:52.948985
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:05:55.690670
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 22:05:57.018116
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 22:05:58.436444
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:06:05.399755
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:07.945720
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:10.461811
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:12.981841
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:15.400226
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:17.819037
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:20.238654
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:06:22.652136
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:06:25.071948
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:06:27.488147
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:29.906213
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:32.323379
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:06:55.885377
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream:
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = TestStream()

    assert issubclass(TestStream, WritableStream)
    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.contents == 'hello'

    class StreamWithoutWrite:
        pass

    class StreamWithDisabledWrite:
        write = None

    assert not issubclass(StreamWithoutWrite, WritableStream)
    assert not issubclass(StreamWithDisabledWrite, WritableStream)

# Generated at 2026-10-24 22:07:05.178023
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write.__isabstractmethod__

# Generated at 2026-10-24 22:07:06.505230
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1. No custom_repr -> falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is repr
    assert module_0.get_repr_function('a', []) is repr

    # 2. Type condition that matches -> returns that action
    action = lambda x: 'INT!'
    assert module_0.get_repr_function(1, [(int, action)]) is action

    # 3. Type condition that doesn't match -> falls through to repr
    assert module_0.get_repr_function('a', [(int, action)]) is repr

    # 4. Callable (non-type) condition
    is_even = lambda x: isinstance(x, int) and x % 2 == 0
    assert module_0.get_repr_function(2, [(is_even, action)]) is action
    assert module_0.get_repr_function(3, [(is_even, action)]) is repr

    # 5. First matching condition wins
    first = lambda x: 'first'
    second = lambda x: 'second'
    assert module_0.get_repr_function(0, [(int, first), (int, second)]) is first
    assert module_0.get_repr_function(0, [(str, first), (int, second)]) is second

    # 6. End-to-end: the returned function is the one that gets called
    fn = module_0.get_repr_function([1, 2], [(list, lambda x: 'a list')])
    assert fn([1, 2]) == 'a list'

# Generated at 2026-10-24 22:07:22.981301
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WithWrite(object):
        def module_0.write(self, s):
            return len(s)

    class WithoutWrite(object):
        pass

    class WithNoneWrite(object):
        write = None

    # Duck-typed subclasshook: having `write` is enough.
    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # Missing or None `write` must not qualify.
    assert not issubclass(WithoutWrite, WritableStream)
    assert not issubclass(WithNoneWrite, WritableStream)

    # Abstract base itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    # The method is actually callable on a concrete implementation.
    assert WithWrite().write('abc') == 3

# Generated at 2026-10-24 22:07:25.400164
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:07:27.820920
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:07:30.234963
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:32.650846
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:35.069033
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:37.486041
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:39.902860
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:42.319710
# Unit test for function get_repr_function

# Generated at 2026-10-24 22:07:44.737366
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:07:47.159976
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 22:07:48.527228
# Unit test for method write of class WritableStream