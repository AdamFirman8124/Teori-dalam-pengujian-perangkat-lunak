

# Generated at 2026-10-24 21:25:16.287346
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:17.615614
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:25:19.051689
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

# Generated at 2026-10-24 21:25:25.171210
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-string iterables are converted to tuples.
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x for x in [1, 2]) == (1, 2)
    assert module_0.ensure_tuple([]) == ()

    # Strings and non-iterable values become single-item tuples.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-10-24 21:25:26.513299
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

# Generated at 2026-10-24 21:25:34.476137
# Unit test for function normalize_repr
def test_normalize_repr():
    assert module_0.normalize_repr('<Foo object at 0x1234>') == '<Foo object>'
    assert module_0.normalize_repr('<Foo object at 0x7fABC123>') == '<Foo object>'
    assert module_0.normalize_repr('value at 0x1234 and other at 0xABCDEF') == \
           'value and other'
    assert module_0.normalize_repr('plain representation') == 'plain representation'
    assert module_0.normalize_repr('value at 0x123') == 'value at 0x123'

# Generated at 2026-10-24 21:25:36.993016
# Unit test for function truncate

# Generated at 2026-10-24 21:25:39.533686
# Unit test for function truncate

# Generated at 2026-10-24 21:25:41.946808
# Unit test for function truncate

# Generated at 2026-10-24 21:25:44.365225
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:46.785532
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:49.373270
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:51.789566
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:54.210656
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:56.627838
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:25:59.044907
# Unit test for function shitcode

# Generated at 2026-10-24 21:26:01.462213
# Unit test for function shitcode

# Generated at 2026-10-24 21:26:03.881648
# Unit test for function shitcode

# Generated at 2026-10-24 21:26:06.299270
# Unit test for function truncate

# Generated at 2026-10-24 21:26:08.717314
# Unit test for function truncate

# Generated at 2026-10-24 21:26:11.139858
# Unit test for function truncate

# Generated at 2026-10-24 21:26:13.554591
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:15.972299
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:18.389675
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:20.805605
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:23.222495
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:25.638422
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:28.057203
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:26:30.504631
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:26:32.892339
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:26:35.310215
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:37.725358
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:40.140607
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:41.522202
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

# Generated at 2026-10-24 21:26:48.962260
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:50.392722
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:51.827663
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:26:53.262932
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

# Generated at 2026-10-24 21:26:54.593461
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

# Generated at 2026-10-24 21:26:55.947946
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

# Generated at 2026-10-24 21:27:12.525763
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

# Generated at 2026-10-24 21:27:14.937499
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:17.355923
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:19.976760
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:27:22.500825
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:27:24.920842
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:27:27.340706
# Unit test for function shitcode

# Generated at 2026-10-24 21:27:29.757137
# Unit test for function shitcode

# Generated at 2026-10-24 21:27:32.174196
# Unit test for function shitcode

# Generated at 2026-10-24 21:27:34.588775
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:37.007765
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:39.426381
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:41.845734
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:44.259408
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:46.675263
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:49.094505
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:51.508430
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:53.928326
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:27:56.344525
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:27:58.761629
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:28:01.181801
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:28:03.598075
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:06.013746
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:08.430306
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:10.847034
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:28:18.034158
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = ((int, str),)

# Generated at 2026-10-24 21:28:22.760226
# Unit test for function get_repr_function
def test_get_repr_function():custom = [(int, lambda value: f"integer:{value}")]

# Generated at 2026-10-24 21:28:24.192302
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

# Generated at 2026-10-24 21:28:25.633636
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

# Generated at 2026-10-24 21:28:26.950821
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

# Generated at 2026-10-24 21:28:36.392227
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:37.812620
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:39.139531
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:40.467511
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

# Generated at 2026-10-24 21:28:48.979324
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:50.306633
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:51.644151
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:28:52.975090
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

# Generated at 2026-10-24 21:29:17.952362
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

# Generated at 2026-10-24 21:29:20.214693
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

# Generated at 2026-10-24 21:29:21.539469
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

# Generated at 2026-10-24 21:29:24.280324
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:29:26.838490
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:29:29.371352
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:29:31.789501
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:34.209693
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:36.628270
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:39.225339
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:29:41.673072
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:29:44.062290
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:29:46.483552
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:48.901053
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:51.319266
# Unit test for function shitcode

# Generated at 2026-10-24 21:29:53.737292
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:05.567290
# Unit test for method write of class WritableStream
def test_WritableStream_write():assert WritableStream.write(object(), "hello") is None

# Generated at 2026-10-24 21:30:06.901228
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

# Generated at 2026-10-24 21:30:09.765148
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:30:11.096418
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:30:26.662076
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:29.190967
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:31.607678
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:34.026656
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:36.442781
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:38.859156
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:41.277696
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:43.794990
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:46.211291
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:30:48.791816
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:31:04.335729
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(123) == '123'

# Generated at 2026-10-24 21:31:05.668558
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

# Generated at 2026-10-24 21:31:20.576912
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteStream:
        def module_0.write(self, s):
            return len(s)

    class NonWritableStream:
        pass

    class DisabledWriteStream:
        write = None

    assert issubclass(ConcreteStream, WritableStream)
    assert isinstance(ConcreteStream(), WritableStream)

    stream = ConcreteStream()
    assert stream.write("abc") == 3

    assert not issubclass(NonWritableStream, WritableStream)
    assert not issubclass(DisabledWriteStream, WritableStream)

# Generated at 2026-10-24 21:31:21.958493
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:31:23.391285
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:31:24.719392
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

# Generated at 2026-10-24 21:31:49.229107
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

    # WritableStream itself cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

# Generated at 2026-10-24 21:31:51.764883
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

# Generated at 2026-10-24 21:32:07.220697
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def module_0.write(self, s):
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5


def test_WritableStream_accepts_write_protocol():
    class DuckWritableStream:
        def module_0.write(self, s):
            return len(s)

    stream = DuckWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5

# Generated at 2026-10-24 21:32:08.639078
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:32:09.965656
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:32:16.540281
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:32:17.865408
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:32:19.193576
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:32:37.083724
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

# Generated at 2026-10-24 21:32:38.658704
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

# Generated at 2026-10-24 21:32:41.421271
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:32:43.950344
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:32:46.474277
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:32:48.894268
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:32:55.967244
# Unit test for function get_repr_function
def test_get_repr_function():int_repr = lambda item: "integer:{}".format(item)

# Generated at 2026-10-24 21:32:57.299121
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

# Generated at 2026-10-24 21:32:58.625707
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

# Generated at 2026-10-24 21:33:03.950646
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:05.376618
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:06.816200
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:23.081337
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream:
        def module_0.write(self, value):
            return len(value)

    stream = TestStream()

    assert issubclass(TestStream, WritableStream)
    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5

# Generated at 2026-10-24 21:33:24.402992
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:25.731243
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:30.472288
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:31.861995
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:33.188103
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:34.977921
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

# Generated at 2026-10-24 21:33:37.843763
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:33:39.169402
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:33:53.356346
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritable:
        def module_0.write(self, s):
            return len(s)

    class NotWritable:
        pass

    writable = ConcreteWritable()

    assert issubclass(ConcreteWritable, WritableStream)
    assert isinstance(writable, WritableStream)
    assert writable.write("abc") == 3

    assert not issubclass(NotWritable, WritableStream)

# Generated at 2026-10-24 21:33:54.755946
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:56.081744
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:33:57.416843
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

# Generated at 2026-10-24 21:33:58.837491
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

# Generated at 2026-10-24 21:34:01.706140
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:34:03.081914
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:34:19.418510
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream:
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    class NonWritableStream:
        pass

    stream = ConcreteWritableStream()

    # The presence of a write method should satisfy the subclass hook.
    assert issubclass(ConcreteWritableStream, WritableStream)
    assert isinstance(stream, WritableStream)

    # Verify that the write method behaves correctly.
    assert stream.write("hello") == 5
    assert stream.written == ["hello"]

    # Classes without write should not be considered writable streams.
    assert not issubclass(NonWritableStream, WritableStream)
    assert not isinstance(NonWritableStream(), WritableStream)

# Generated at 2026-10-24 21:34:43.894061
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated until module_0.write() is implemented.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should be abstract because module_0.write() is not implemented"
        )

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]

# Generated at 2026-10-24 21:34:46.658058
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:34:48.033870
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:34:50.449761
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:35:01.404427
# Unit test for method write of class WritableStream
def test_WritableStream_write():result = WritableStream.write(object(), "hello")

# Generated at 2026-10-24 21:35:03.223348
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

# Generated at 2026-10-24 21:35:04.551006
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

# Generated at 2026-10-24 21:35:05.907004
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

# Generated at 2026-10-24 21:35:07.238281
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

# Generated at 2026-10-24 21:35:10.089728
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:35:11.482292
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:35:14.407436
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:35:15.845899
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'