

# Generated at 2026-10-24 19:59:38.944080
# Unit test for function shitcode

# Generated at 2026-10-24 19:59:41.366954
# Unit test for function shitcode

# Generated at 2026-10-24 19:59:43.782237
# Unit test for function shitcode

# Generated at 2026-10-24 19:59:46.200671
# Unit test for function get_repr_function

# Generated at 2026-10-24 19:59:48.622267
# Unit test for function get_repr_function

# Generated at 2026-10-24 19:59:51.039343
# Unit test for function get_repr_function

# Generated at 2026-10-24 19:59:53.460440
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 19:59:54.875314
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 19:59:57.451184
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 19:59:58.830504
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:00:00.257995
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

# Generated at 2026-10-24 20:00:27.921278
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract class cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class RecordingStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = RecordingStream()

    assert stream.write("hello") == 5
    assert stream.write("") == 0
    assert stream.written == ["hello", ""]

# Generated at 2026-10-24 20:00:36.202011
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterables are wrapped in a tuple.
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

    # Strings are treated as single values.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple(u'hello') == (u'hello',)

    # Other iterables are converted to tuples.
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(iter([1, 2, 3])) == (1, 2, 3)

# Generated at 2026-10-24 20:00:38.729035
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:00:41.144994
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:00:43.562917
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:00:45.979522
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:00:48.396224
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:00:50.811839
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:00:53.229247
# Unit test for function ensure_tuple

# Generated at 2026-10-24 20:01:01.534277
# Unit test for function ensure_tuple
def test_ensure_tuple():assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)

# Generated at 2026-10-24 20:01:08.663166
# Unit test for function ensure_tuple
def test_ensure_tuple():
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple('hello') == ('hello',)

    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(iter([1, 2, 3])) == (1, 2, 3)

# Generated at 2026-10-24 20:01:10.096332
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

# Generated at 2026-10-24 20:01:12.890316
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:01:14.205892
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:01:23.679385
# Unit test for function truncate
def test_truncate():
    assert module_0.truncate('hello', None) == 'hello'
    assert module_0.truncate('hello', 5) == 'hello'
    assert module_0.truncate('hello', 10) == 'hello'

    assert module_0.truncate('abcdefghij', 7) == 'ab...ij'
    assert module_0.truncate('abcdefghij', 8) == 'ab...hij'

    assert len(module_0.truncate('abcdefghij', 7)) == 7
    assert len(module_0.truncate('abcdefghij', 8)) == 8

# Generated at 2026-10-24 20:01:25.006871
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

# Generated at 2026-10-24 20:01:28.014788
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:01:29.345602
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:01:32.217239
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:01:33.565521
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:01:56.079271
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write.__isabstractmethod__

    with pytest.raises(TypeError):
        WritableStream()

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]

# Generated at 2026-10-24 20:01:57.432146
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

# Generated at 2026-10-24 20:02:13.890626
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

# Generated at 2026-10-24 20:02:15.217854
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:16.542230
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:22.696087
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:24.334815
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:25.675302
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:31.173179
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:32.606125
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:33.936953
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:02:43.279474
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    pass

# Generated at 2026-10-24 20:02:45.981721
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:02:48.513100
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:02:50.928802
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:02:53.346280
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:02:55.763076
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:03:01.711492
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = [
        (int, lambda item: "integer:{}".format(item)),
        (lambda item: item == "special", lambda item: "matched"),
    ]

# Generated at 2026-10-24 20:03:08.674745
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:09.994655
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:11.439022
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:12.861204
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

# Generated at 2026-10-24 20:03:29.361296
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

# Generated at 2026-10-24 20:03:30.685929
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:32.005471
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:55.473484
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-24 20:03:57.895083
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:03:59.362613
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:00.796590
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:03.622392
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:04.997065
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:04:11.154556
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:12.476101
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:13.795911
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:15.126676
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

# Generated at 2026-10-24 20:04:16.450966
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

# Generated at 2026-10-24 20:04:17.897139
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

# Generated at 2026-10-24 20:04:20.772175
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:22.198657
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:04:25.065047
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:26.715841
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:04:33.882958
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:35.198469
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:36.636054
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:38.058624
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

# Generated at 2026-10-24 20:04:40.701326
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:43.233521
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:45.755007
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:04:48.271977
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:50.784952
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:53.318401
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:04:55.734892
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:04:58.154258
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:00.572684
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:02.989906
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:05.407377
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:07.824771
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:10.239838
# Unit test for function shitcode

# Generated at 2026-10-24 20:05:18.302902
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode("A\x01\xff\x00\u0100z") == "A\x01\xff??z"

# Generated at 2026-10-24 20:05:21.142050
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:05:22.497795
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 20:05:30.033697
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:31.360758
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:32.682402
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:34.083739
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

# Generated at 2026-10-24 20:05:41.455702
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:42.774451
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:44.221808
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:45.536776
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

# Generated at 2026-10-24 20:05:46.883412
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

# Generated at 2026-10-24 20:05:49.422191
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:51.950746
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:54.462367
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:05:56.878262
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:05:59.298867
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:01.719294
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:04.136340
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:06.694147
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:09.110295
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:11.529390
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:06:13.943415
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:06:16.359571
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:06:18.779759
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:21.195220
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:32.248192
# Unit test for method write of class WritableStream
def test_WritableStream_write():assert WritableStream.write(object()) is None

# Generated at 2026-10-24 20:06:48.886815
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

# Generated at 2026-10-24 20:06:50.269533
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:51.702027
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:06:53.025820
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

# Generated at 2026-10-24 20:07:16.893945
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]

# Generated at 2026-10-24 20:07:19.404818
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:21.822023
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:24.242762
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:26.662231
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:07:29.079007
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:07:31.495662
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:07:33.912396
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:36.327729
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:38.744886
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 20:07:41.160832
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:07:43.577784
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:07:45.997337
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:07:48.413099
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:07:55.809103
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = lambda item: "integer: {}".format(item)

# Generated at 2026-10-24 20:08:02.871612
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:04.304742
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:05.738403
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:07.063370
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

# Generated at 2026-10-24 20:08:23.179891
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = TestWritableStream()

    result = stream.write("hello")

    assert result == 5
    assert stream.written == ["hello"]

# Generated at 2026-10-24 20:08:24.506785
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

# Generated at 2026-10-24 20:08:27.142547
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:29.559873
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:32.098696
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:34.516738
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:36.932524
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:39.351775
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:08:41.772722
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:44.185000
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:46.601051
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:49.022511
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:51.437724
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:53.854440
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:56.269959
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:08:58.686708
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:09:01.102653
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:09:03.520021
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:09:05.937384
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:09:08.354082
# Unit test for function get_repr_function

# Generated at 2026-10-24 20:09:10.771223
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:09:12.131138
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:09:13.518537
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:09:14.831164
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

# Generated at 2026-10-24 20:09:37.490518
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.content = ''

        def module_0.write(self, s):
            self.content += s
            return len(s)

    stream = TestStream()

    assert stream.write('hello') == 5
    assert stream.content == 'hello'
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-24 20:09:39.907704
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:09:42.321500
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 20:09:44.737875
# Unit test for method write of class WritableStream