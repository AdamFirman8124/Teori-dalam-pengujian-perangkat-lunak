

# Generated at 2026-10-24 12:33:58.334565
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:00.890398
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:03.304167
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:05.877237
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:08.290479
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:10.706665
# Unit test for function shitcode

# Generated at 2026-10-24 12:34:13.294357
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:34:15.707403
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:34:18.123136
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:34:20.539396
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 12:34:22.955147
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 12:34:25.371016
# Unit test for constructor of class WritableStream

# Generated at 2026-10-24 12:34:37.106110
# Unit test for function normalize_repr

# Generated at 2026-10-24 12:34:41.697525
# Unit test for function normalize_repr
def test_normalize_repr():item_repr = '<Foo object at 0x7fABC123>'

# Generated at 2026-10-24 12:34:43.026211
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

# Generated at 2026-10-24 12:34:44.388762
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:34:45.737835
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:34:53.813457
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Existing tuples remain equivalent.
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)

    # Non-string iterables are converted to tuples.
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(iter([1, 2])) == (1, 2)

    # Strings are treated as single values, not iterables.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple('') == ('',)

    # Non-iterable values are wrapped in a one-element tuple.
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-10-24 12:34:56.363343
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:34:58.778148
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:01.190538
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:03.603253
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:06.016462
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:08.429006
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:10.842234
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:13.255233
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:15.669694
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:18.086043
# Unit test for function ensure_tuple

# Generated at 2026-10-24 12:35:20.499558
# Unit test for function ensure_tuple

# Generated at 2026-10-24 12:35:22.911675
# Unit test for function ensure_tuple

# Generated at 2026-10-24 12:35:25.479686
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:27.894240
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:30.310578
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:32.718888
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:35.133565
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:37.545798
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:39.958487
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:42.373582
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:44.785350
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:35:47.199694
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:35:49.614378
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:35:52.032152
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:35:54.449893
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:56.860616
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:35:59.276437
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:01.691071
# Unit test for function shitcode

# Generated at 2026-10-24 12:36:04.100717
# Unit test for function shitcode

# Generated at 2026-10-24 12:36:06.515798
# Unit test for function shitcode

# Generated at 2026-10-24 12:36:08.930622
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:11.341070
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:13.753696
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:16.166332
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:36:18.578244
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:36:20.991760
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:36:23.404918
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:25.820989
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:28.237271
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:30.652693
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:33.066725
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:35.480394
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:37.893790
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:40.307606
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:42.720953
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:45.134660
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:47.550246
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:49.961760
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:36:52.377027
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:54.787528
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:57.201232
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:36:59.613737
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:02.027686
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:04.445990
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:06.858151
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:09.271353
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:11.683358
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:14.097772
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:16.510104
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:18.927923
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:21.339521
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:23.751031
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:26.163863
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:28.575883
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:30.988489
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:33.400144
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:35.814894
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:38.230612
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:40.648724
# Unit test for function shitcode

# Generated at 2026-10-24 12:37:43.059284
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:37:45.504813
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:37:47.884089
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:37:50.296835
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:52.708332
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:55.123247
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:37:57.536131
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:37:59.960857
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:02.374103
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:04.788531
# Unit test for function truncate

# Generated at 2026-10-24 12:38:07.198163
# Unit test for function truncate

# Generated at 2026-10-24 12:38:09.609903
# Unit test for function truncate

# Generated at 2026-10-24 12:38:12.021885
# Unit test for function truncate

# Generated at 2026-10-24 12:38:14.437363
# Unit test for function truncate

# Generated at 2026-10-24 12:38:16.852927
# Unit test for function truncate

# Generated at 2026-10-24 12:38:19.262302
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:38:21.677294
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:38:24.087662
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:38:26.500596
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:28.913504
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:31.326868
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:33.740268
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:36.153873
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:38.565598
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:38:40.979152
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:38:43.392061
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:38:45.806347
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:38:48.220407
# Unit test for function shitcode

# Generated at 2026-10-24 12:38:50.635661
# Unit test for function shitcode

# Generated at 2026-10-24 12:38:53.048588
# Unit test for function shitcode

# Generated at 2026-10-24 12:38:55.460796
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:38:57.872945
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:39:00.287102
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:39:02.700489
# Unit test for function shitcode

# Generated at 2026-10-24 12:39:05.113341
# Unit test for function shitcode

# Generated at 2026-10-24 12:39:07.525142
# Unit test for function shitcode

# Generated at 2026-10-24 12:39:09.937731
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:12.351603
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:14.764410
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:17.179763
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:39:19.599544
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:39:22.014375
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:39:24.428140
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:26.841256
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:29.252366
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:31.952293
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:34.365590
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:36.780102
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:39:39.192766
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:40.734812
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:42.156144
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:43.886111
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

# Generated at 2026-10-24 12:39:45.241191
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:39:46.663364
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:01.920926
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:03.364546
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:04.890001
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:06.252996
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

# Generated at 2026-10-24 12:40:07.668537
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

# Generated at 2026-10-24 12:40:18.304846
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = MemoryStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == 'hello world'

# Generated at 2026-10-24 12:40:20.837943
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:40:23.250608
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:40:25.664390
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:40:28.077230
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:30.490370
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:32.903844
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:35.316834
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:40:37.731519
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:40:40.145119
# Unit test for function get_shortish_repr

# Generated at 2026-10-24 12:40:42.556946
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:44.968195
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:46.363945
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:40:47.668192
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

# Generated at 2026-10-24 12:40:49.036959
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

# Generated at 2026-10-24 12:40:50.361861
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

# Generated at 2026-10-24 12:41:06.962409
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

# Generated at 2026-10-24 12:41:08.328365
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:41:09.710301
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:41:24.662294
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    pass

# Generated at 2026-10-24 12:41:47.291849
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

    stream = MemoryStream()
    result = stream.write("hello")

    assert result == 5
    assert stream.written == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-24 12:41:59.447801
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:00.836286
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:02.240859
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:03.572457
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Basic: default repr of an object
    assert module_0.get_shortish_repr(1) == '1'
    assert module_0.get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

    # Newlines and carriage returns are stripped
    class MultiLine:
        def __repr__(self):
            return 'line1\r\nline2\nline3'
    assert module_0.get_shortish_repr(MultiLine()) == 'line1line2line3'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # max_length truncation (middle truncated with '...')
    long_string = 'abcdefghijklmnopqrstuvwxyz' # 26 chars
    result = module_0.get_shortish_repr(long_string, max_length=10)
    assert result == 'abcdef...wxyz'
    assert len(result) == 10

    # max_length larger than string -> unchanged
    assert module_0.get_shortish_repr('abc', max_length=100) == 'abc'

    # custom_repr with a type condition
    class MyType:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        MyType(), custom_repr=((MyType, lambda x: 'custom'),)
    ) == 'custom'
    # Non-matching items fall back to default repr
    assert module_0.get_shortish_repr(
        1, custom_repr=((MyType, lambda x: 'custom'),)
    ) == '1'

    # custom_repr with a callable condition
    assert module_0.get_shortish_repr(
        1, custom_repr=((lambda x: x == 1, lambda x: 'one'),)
    ) == 'one'

    # First matching custom_repr entry wins
    assert module_0.get_shortish_repr(
        MyType(),
        custom_repr=(
            (MyType, lambda x: 'first'),
            (MyType, lambda x: 'second'),
        )
    ) == 'first'

    # normalize: strips memory addresses from default repr
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f8b2c3d4e5f>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    # Without normalize, address stays
    assert module_0.get_shortish_repr(WithAddress()) == \
        '<WithAddress object at 0x7f8b2c3d4e5f>'

    # normalize + max_length combined
    result = module_0.get_shortish_repr(WithAddress(), max_length=20, normalize=True)
    assert '0x' not in result
    assert len(result) == 20

# Generated at 2026-10-24 12:42:15.552805
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:17.293979
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:18.668759
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:19.989168
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

# Generated at 2026-10-24 12:42:21.301888
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Basic: default repr of an object
    assert module_0.get_shortish_repr(1) == '1'
    assert module_0.get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

    # Newlines and carriage returns are stripped
    class MultiLine:
        def __repr__(self):
            return 'line1\r\nline2\nline3'
    assert module_0.get_shortish_repr(MultiLine()) == 'line1line2line3'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # max_length truncation (middle truncated with '...')
    long_string = 'abcdefghijklmnopqrstuvwxyz' # 26 chars
    result = module_0.get_shortish_repr(long_string, max_length=10)
    assert result == 'abcdef...wxyz'
    assert len(result) == 10

    # max_length larger than string -> unchanged
    assert module_0.get_shortish_repr('abc', max_length=100) == 'abc'

    # custom_repr with a type condition
    class MyType:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        MyType(), custom_repr=((MyType, lambda x: 'custom'),)
    ) == 'custom'
    # Non-matching items fall back to default repr
    assert module_0.get_shortish_repr(
        1, custom_repr=((MyType, lambda x: 'custom'),)
    ) == '1'

    # custom_repr with a callable condition
    assert module_0.get_shortish_repr(
        1, custom_repr=((lambda x: x == 1, lambda x: 'one'),)
    ) == 'one'

    # First matching custom_repr entry wins
    assert module_0.get_shortish_repr(
        MyType(),
        custom_repr=(
            (MyType, lambda x: 'first'),
            (MyType, lambda x: 'second'),
        )
    ) == 'first'

    # normalize: strips memory addresses from default repr
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f8b2c3d4e5f>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    # Without normalize, address stays
    assert module_0.get_shortish_repr(WithAddress()) == \
        '<WithAddress object at 0x7f8b2c3d4e5f>'

    # normalize + max_length combined
    result = module_0.get_shortish_repr(WithAddress(), max_length=20, normalize=True)
    assert '0x' not in result
    assert len(result) == 20

# Generated at 2026-10-24 12:42:22.721578
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Basic: default repr of an object
    assert module_0.get_shortish_repr(1) == '1'
    assert module_0.get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

    # Newlines and carriage returns are stripped
    class MultiLine:
        def __repr__(self):
            return 'line1\r\nline2\nline3'
    assert module_0.get_shortish_repr(MultiLine()) == 'line1line2line3'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # max_length truncation (middle truncated with '...')
    long_string = 'abcdefghijklmnopqrstuvwxyz' # 26 chars
    result = module_0.get_shortish_repr(long_string, max_length=10)
    assert result == 'abcdef...wxyz'
    assert len(result) == 10

    # max_length larger than string -> unchanged
    assert module_0.get_shortish_repr('abc', max_length=100) == 'abc'

    # custom_repr with a type condition
    class MyType:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        MyType(), custom_repr=((MyType, lambda x: 'custom'),)
    ) == 'custom'
    # Non-matching items fall back to default repr
    assert module_0.get_shortish_repr(
        1, custom_repr=((MyType, lambda x: 'custom'),)
    ) == '1'

    # custom_repr with a callable condition
    assert module_0.get_shortish_repr(
        1, custom_repr=((lambda x: x == 1, lambda x: 'one'),)
    ) == 'one'

    # First matching custom_repr entry wins
    assert module_0.get_shortish_repr(
        MyType(),
        custom_repr=(
            (MyType, lambda x: 'first'),
            (MyType, lambda x: 'second'),
        )
    ) == 'first'

    # normalize: strips memory addresses from default repr
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f8b2c3d4e5f>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    # Without normalize, address stays
    assert module_0.get_shortish_repr(WithAddress()) == \
        '<WithAddress object at 0x7f8b2c3d4e5f>'

    # normalize + max_length combined
    result = module_0.get_shortish_repr(WithAddress(), max_length=20, normalize=True)
    assert '0x' not in result
    assert len(result) == 20

# Generated at 2026-10-24 12:42:24.041610
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

# Generated at 2026-10-24 12:42:40.540181
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

# Generated at 2026-10-24 12:42:42.961961
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:45.375865
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:42:47.791174
# Unit test for function get_repr_function

# Generated at 2026-10-24 12:42:54.159131
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = [
        (str, lambda value: "string:" + value),
        (lambda value: value == 42, lambda value: "the answer"),
    ]

# Generated at 2026-10-24 12:43:18.899277
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    stream = MemoryStream()
    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-24 12:43:30.714742
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:32.153842
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:33.520221
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:34.870872
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

# Generated at 2026-10-24 12:43:36.247965
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

# Generated at 2026-10-24 12:43:41.199453
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:43.618364
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:46.033294
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:48.558581
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:50.975496
# Unit test for method write of class WritableStream

# Generated at 2026-10-24 12:43:56.933135
# Unit test for method write of class WritableStream
def test_WritableStream_write():assert WritableStream.write(object(), "hello") is None

# Generated at 2026-10-24 12:43:58.298592
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