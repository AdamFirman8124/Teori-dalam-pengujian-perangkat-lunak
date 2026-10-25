

# Generated at 2026-10-24 14:43:39.356858
# Unit test for function normalize_repr

# Generated at 2026-10-24 14:43:41.772820
# Unit test for function normalize_repr

# Generated at 2026-10-24 14:43:44.182906
# Unit test for function normalize_repr

# Generated at 2026-10-24 14:43:46.595084
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 14:43:49.007377
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 14:44:03.261389
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 14:44:12.067430
# Unit test for function normalize_repr
def test_normalize_repr():
    # A default repr with a memory address gets the address stripped
    repr_with_address = '<foo.Foo object at 0x7f8b2c3d4e5f>'
    result = module_0.normalize_repr(repr_with_address)
    assert result == '<foo.Foo object>'

    # Idempotent: normalizing an already-normalized repr changes nothing
    assert module_0.normalize_repr(result) == result

    # A repr without an address is returned unchanged
    assert module_0.normalize_repr('<foo.Foo object>') == '<foo.Foo object>'

    # Addresses shorter/longer than typical are still caught (4+ hex chars)
    assert module_0.normalize_repr('<X at 0x1234>') == '<X>'
    assert module_0.normalize_repr('<X at 0xabcdef0123>') == '<X>'

    # Uppercase hex is covered by the pattern
    assert module_0.normalize_repr('<X at 0xABCDEF12>') == '<X>'

    # 1â3 hex "addresses" are NOT addresses â left alone
    assert module_0.normalize_repr('<X at 0x12>') == '<X at 0x12>'

# Generated at 2026-10-24 14:44:14.483708
# Unit test for function ensure_tuple

# Generated at 2026-10-24 14:44:16.898205
# Unit test for function ensure_tuple

# Generated at 2026-10-24 14:44:19.311201
# Unit test for function ensure_tuple

# Generated at 2026-10-24 14:44:21.723737
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:24.336705
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:26.762658
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:29.173701
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:31.586208
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:34.000106
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:36.411573
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:38.824433
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:41.238530
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:44:43.652114
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:46.068663
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:48.480360
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:44:54.870879
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # A class with a `write` method is recognized as a subclass via
    # __subclasshook__, even without explicit inheritance.
    class MyStream:
        def __init__(self):
            self.data = ''

        def module_0.write(self, s):
            self.data += s

    assert issubclass(MyStream, WritableStream)

    # A class without a `write` method is not recognized.
    class NotAStream:
        pass

    assert not issubclass(NotAStream, WritableStream)

    # The abstract base class itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should be abstract.')

    # A concrete subclass of WritableStream works and `write` functions.
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.data = ''

        def module_0.write(self, s):
            self.data += s

    stream = MyWritableStream()
    stream.write('foo')
    stream.write('bar')
    assert stream.data == 'foobar'

    # Writing to a recognized duck-typed stream works too.
    my_stream = MyStream()
    my_stream.write('hello')
    assert my_stream.data == 'hello'

# Generated at 2026-10-24 14:45:27.605195
# Unit test for function truncate
def test_truncate():assert module_0.truncate('', None) == ''

# Generated at 2026-10-24 14:45:30.111175
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:32.524930
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:35.062585
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:37.658072
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:40.072204
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:42.490663
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:44.902968
# Unit test for function truncate

# Generated at 2026-10-24 14:45:47.316417
# Unit test for function truncate

# Generated at 2026-10-24 14:45:49.731309
# Unit test for function truncate

# Generated at 2026-10-24 14:45:52.149965
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:54.557207
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:56.968756
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:45:59.379862
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:46:01.790966
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:46:04.207897
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:46:06.618750
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:46:09.033092
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:46:11.447958
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:46:13.863158
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:46:16.278158
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:46:47.512785
# Unit test for function get_repr_function
def test_get_repr_function():
    # Default fallback is builtin repr
    assert module_0.get_repr_function(42, ()) is repr
    assert module_0.get_repr_function('x', ()) is repr

    # Type condition matched -> returns the paired action
    def int_action(x):
        return 'INT<%d>' % x

    assert module_0.get_repr_function(5, ((int, int_action),)) is int_action
    assert module_0.get_repr_function(5, ((int, int_action),))(5) == 'INT<5>'

    # Type conditions use isinstance, so subclasses match
    assert module_0.get_repr_function(True, ((int, int_action),)) is int_action

    # Non-matching type condition falls through to repr
    assert module_0.get_repr_function('5', ((int, int_action),)) is repr

    # Non-type callable condition
    def is_negative(x):
        return x < 0

    def neg_action(x):
        return 'NEG%d' % x

    assert module_0.get_repr_function(-3, ((is_negative, neg_action),)) is neg_action
    assert module_0.get_repr_function(3, ((is_negative, neg_action),)) is repr

    # First matching condition wins
    def str_action(x):
        return 'STR'

    custom = ((int, int_action), (is_negative, neg_action), (str, str_action))
    assert module_0.get_repr_function(-1, custom) is int_action
    assert module_0.get_repr_function('a', custom) is str_action
    assert module_0.get_repr_function(1.5, custom) is repr

# Generated at 2026-10-24 14:46:48.948654
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

# Generated at 2026-10-24 14:46:50.379103
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

# Generated at 2026-10-24 14:46:51.688596
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

# Generated at 2026-10-24 14:47:10.863290
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:47:13.402754
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:47:15.816742
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:47:18.231745
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:47:20.646965
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:47:23.059605
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:47:25.474920
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:47:27.887507
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:47:30.328976
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:47:32.769099
# Unit test for function shitcode

# Generated at 2026-10-24 14:47:35.194690
# Unit test for function shitcode

# Generated at 2026-10-24 14:47:37.606067
# Unit test for function shitcode

# Generated at 2026-10-24 14:47:40.021502
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:47:42.436512
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:47:44.850265
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:48:02.476985
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:48:18.753861
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 14:48:20.183583
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

# Generated at 2026-10-24 14:48:21.499665
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

# Generated at 2026-10-24 14:48:24.009193
# Unit test for function shitcode

# Generated at 2026-10-24 14:48:26.517629
# Unit test for function shitcode

# Generated at 2026-10-24 14:48:28.931827
# Unit test for function shitcode

# Generated at 2026-10-24 14:48:31.347047
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:48:33.760784
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:48:36.320250
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:48:38.733715
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:48:41.145103
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:48:43.557572
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:48:45.971110
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:48:48.417924
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:48:50.799631
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:48:53.213512
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:02.886586
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:04.319819
# Unit test for function get_repr_function
def test_get_repr_function():
    # Default fallback is builtin repr
    assert module_0.get_repr_function(42, ()) is repr
    assert module_0.get_repr_function('x', ()) is repr

    # Type condition matched -> returns the paired action
    def int_action(x):
        return 'INT<%d>' % x

    assert module_0.get_repr_function(5, ((int, int_action),)) is int_action
    assert module_0.get_repr_function(5, ((int, int_action),))(5) == 'INT<5>'

    # Type conditions use isinstance, so subclasses match
    assert module_0.get_repr_function(True, ((int, int_action),)) is int_action

    # Non-matching type condition falls through to repr
    assert module_0.get_repr_function('5', ((int, int_action),)) is repr

    # Non-type callable condition
    def is_negative(x):
        return x < 0

    def neg_action(x):
        return 'NEG%d' % x

    assert module_0.get_repr_function(-3, ((is_negative, neg_action),)) is neg_action
    assert module_0.get_repr_function(3, ((is_negative, neg_action),)) is repr

    # First matching condition wins
    def str_action(x):
        return 'STR'

    custom = ((int, int_action), (is_negative, neg_action), (str, str_action))
    assert module_0.get_repr_function(-1, custom) is int_action
    assert module_0.get_repr_function('a', custom) is str_action
    assert module_0.get_repr_function(1.5, custom) is repr

# Generated at 2026-10-24 14:49:05.657647
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

# Generated at 2026-10-24 14:49:22.137210
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

# Generated at 2026-10-24 14:49:24.552567
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:49:26.967463
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:49:29.381176
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:49:31.798399
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:49:34.211207
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:49:36.624918
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:39.041554
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:41.456049
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:43.867788
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:46.280903
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:48.826651
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:49:51.238886
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:49:53.653465
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:49:56.067117
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:49:58.481581
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:00.899322
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:03.313823
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:05.728422
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:08.142126
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:10.556962
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:12.968737
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:15.381518
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:17.793609
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:20.204949
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:22.616867
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:25.027806
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:27.438136
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:29.854074
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:32.265242
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:34.676455
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:37.089091
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:39.500324
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:41.913397
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:44.324169
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:46.736171
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:49.152284
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:51.563225
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:53.975617
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:50:56.389707
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:50:58.800955
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:01.215590
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:03.627143
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:06.040111
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:08.452060
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:10.865089
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:13.277994
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:15.692153
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:18.104131
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:20.516825
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:22.929980
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:25.346019
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:51:27.759084
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:51:30.172498
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:51:32.590027
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:35.002084
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:37.416839
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:39.831679
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:42.242968
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:44.655417
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:51:47.068345
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:49.481165
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:51.897875
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:51:54.306344
# Unit test for function shitcode

# Generated at 2026-10-24 14:52:00.449512
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode('hello') == 'hello'

# Generated at 2026-10-24 14:52:01.818622
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

# Generated at 2026-10-24 14:52:08.946422
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:10.270420
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:26.650988
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

# Generated at 2026-10-24 14:52:28.096289
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:29.633492
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:32.218174
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:34.631295
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:37.042853
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:39.594055
# Unit test for function shitcode

# Generated at 2026-10-24 14:52:42.010776
# Unit test for function shitcode

# Generated at 2026-10-24 14:52:44.422835
# Unit test for function shitcode

# Generated at 2026-10-24 14:52:46.837754
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:49.250125
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:51.664511
# Unit test for function get_repr_function

# Generated at 2026-10-24 14:52:54.079248
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:56.493509
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:52:58.905950
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:53:01.319517
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:53:03.732920
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:53:06.145746
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:53:07.540284
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

# Generated at 2026-10-24 14:53:08.939315
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

# Generated at 2026-10-24 14:53:10.323678
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:53:11.626996
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:53:12.940831
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

# Generated at 2026-10-24 14:53:29.376276
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

# Generated at 2026-10-24 14:53:30.704546
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:53:32.085368
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 14:53:33.399630
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

# Generated at 2026-10-24 14:53:36.126920
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:53:38.746033
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 14:53:41.161993
# Unit test for function get_shortish_repr