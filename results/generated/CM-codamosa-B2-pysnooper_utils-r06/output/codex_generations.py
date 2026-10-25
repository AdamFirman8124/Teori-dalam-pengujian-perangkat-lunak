

# Generated at 2026-10-24 21:40:39.807208
# Unit test for function normalize_repr

# Generated at 2026-10-24 21:40:42.226487
# Unit test for function normalize_repr

# Generated at 2026-10-24 21:40:44.642629
# Unit test for function normalize_repr

# Generated at 2026-10-24 21:40:47.062663
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:40:49.588956
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:40:52.003597
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:40:54.421137
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:40:56.837296
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:40:59.265817
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:41:01.681703
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:41:04.098118
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:41:06.515909
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 21:41:08.931645
# Unit test for function truncate

# Generated at 2026-10-24 21:41:11.348086
# Unit test for function truncate

# Generated at 2026-10-24 21:41:13.765248
# Unit test for function truncate

# Generated at 2026-10-24 21:41:16.181232
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:41:18.598215
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:41:21.014518
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:41:23.431399
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:41:33.906308
# Unit test for method write of class WritableStream
def test_WritableStream_write():result = WritableStream.write(object(), "hello")

# Generated at 2026-10-24 21:41:57.313888
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == ['hello', ' world']

    class IncompleteStream(WritableStream):
        pass

    try:
        IncompleteStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            'WritableStream subclasses without module_0.write() must not be instantiable'
        )

# Generated at 2026-10-24 21:42:00.219736
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:42:02.639849
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:42:05.057715
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:42:07.478134
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:42:09.894846
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:42:12.312643
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:42:14.729606
# Unit test for function shitcode

# Generated at 2026-10-24 21:42:17.149072
# Unit test for function shitcode

# Generated at 2026-10-24 21:42:19.566274
# Unit test for function shitcode

# Generated at 2026-10-24 21:42:21.981071
# Unit test for function shitcode

# Generated at 2026-10-24 21:42:24.399515
# Unit test for function shitcode

# Generated at 2026-10-24 21:42:28.790689
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode('\x00AÃ©â¬') == '?AÃ©?'

# Generated at 2026-10-24 21:42:34.586913
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:35.957111
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:37.282359
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:38.611392
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

# Generated at 2026-10-24 21:42:42.512241
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:42:43.909441
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:42:50.398638
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:53.061388
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:54.375676
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:42:57.004684
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:42:59.533862
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:43:02.065352
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:43:04.480719
# Unit test for function shitcode

# Generated at 2026-10-24 21:43:06.898078
# Unit test for function shitcode

# Generated at 2026-10-24 21:43:09.313298
# Unit test for function shitcode

# Generated at 2026-10-24 21:43:11.730595
# Unit test for function truncate

# Generated at 2026-10-24 21:43:14.150640
# Unit test for function truncate

# Generated at 2026-10-24 21:43:16.566434
# Unit test for function truncate

# Generated at 2026-10-24 21:43:18.982230
# Unit test for function truncate

# Generated at 2026-10-24 21:43:21.399324
# Unit test for function truncate

# Generated at 2026-10-24 21:43:23.817192
# Unit test for function truncate

# Generated at 2026-10-24 21:43:26.235951
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:28.657703
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:31.075208
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:33.492277
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:43:35.909354
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:43:38.326269
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:43:40.741215
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:43.158332
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:45.577780
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:43:47.994810
# Unit test for function truncate

# Generated at 2026-10-24 21:43:50.409556
# Unit test for function truncate

# Generated at 2026-10-24 21:43:52.826898
# Unit test for function truncate

# Generated at 2026-10-24 21:43:55.246691
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:44:00.938293
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = (
        (int, lambda item: "integer:{}".format(item)),
    )

# Generated at 2026-10-24 21:44:03.737670
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:05.063207
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:44:07.813264
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:09.124537
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:44:10.458830
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

# Generated at 2026-10-24 21:44:13.242773
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:14.617352
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:44:15.938650
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

# Generated at 2026-10-24 21:44:18.693164
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:20.036440
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:44:47.441749
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == ['hello', ' world']

# Generated at 2026-10-24 21:44:49.860931
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:52.277474
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:54.698682
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:57.113726
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:44:59.529576
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:45:00.904799
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:45:03.761951
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:45:05.086666
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:45:13.664098
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:14.993316
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:16.341851
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:22.773482
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:24.126180
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:25.444789
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:28.243216
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:45:29.608393
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr(1) == '1'

# Generated at 2026-10-24 21:45:36.592874
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:39.015529
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:41.430959
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:45:43.858986
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:46.264644
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:48.683646
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:51.110358
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:53.518540
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:55.931622
# Unit test for function shitcode

# Generated at 2026-10-24 21:45:58.347464
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:46:00.766124
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:46:06.698681
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = [(int, lambda value: "integer:{}".format(value))]

# Generated at 2026-10-24 21:46:31.582574
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert getattr(WritableStream.write, '__isabstractmethod__', False)

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write('hello') == 5
    assert stream.contents == ['hello']

# Generated at 2026-10-24 21:46:34.003142
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:46:36.419635
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:46:38.839409
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:46:41.254763
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:46:43.672175
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:46:46.087178
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:46:48.507604
# Unit test for function shitcode

# Generated at 2026-10-24 21:46:50.924480
# Unit test for function shitcode

# Generated at 2026-10-24 21:46:53.342319
# Unit test for function shitcode

# Generated at 2026-10-24 21:46:55.757692
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:46:58.176705
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:00.592870
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:15.102378
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream:
        def __init__(self):
            self.written = []

        def module_0.write(self, value):
            self.written.append(value)
            return len(value)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert issubclass(TestStream, WritableStream)

    assert stream.write("hello") == 5
    assert stream.written == ["hello"]

# Generated at 2026-10-24 21:47:20.899078
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:22.219638
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:24.644930
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:27.063425
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:29.478994
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:31.896954
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:34.314307
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:36.733127
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:39.154820
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:41.575229
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:43.994431
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:46.409726
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:47:48.825231
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:51.244105
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:53.659918
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:56.080948
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:47:58.498967
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:00.917224
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:03.337260
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:05.757633
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:08.173335
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:10.591257
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:48:13.009826
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:48:15.426146
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:48:17.841106
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:48:20.256340
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:48:22.671821
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:48:25.090358
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:27.508525
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:29.927821
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:48:32.347974
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:48:34.762745
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:48:40.709170
# Unit test for function get_repr_function
def test_get_repr_function():custom = lambda value: "<integer:{}>".format(value)

# Generated at 2026-10-24 21:48:57.503421
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

# Generated at 2026-10-24 21:48:58.925382
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:01.454571
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:03.990751
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:06.565727
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:08.984139
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:11.400267
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:13.816799
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:16.239262
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:18.652858
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:21.072514
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:23.489959
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 21:49:25.908110
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:28.497829
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:30.915607
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:33.330580
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:49:35.751690
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:49:38.169238
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:49:40.586599
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:43.007099
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:45.422625
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:47.836685
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:50.252020
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:52.668950
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:55.087800
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:49:57.504729
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:50:10.295531
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 21:50:35.404738
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import pytest

    # WritableStream cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]

# Generated at 2026-10-24 21:50:37.975155
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:50:40.394162
# Unit test for function get_repr_function

# Generated at 2026-10-24 21:50:42.810750
# Unit test for function get_repr_function