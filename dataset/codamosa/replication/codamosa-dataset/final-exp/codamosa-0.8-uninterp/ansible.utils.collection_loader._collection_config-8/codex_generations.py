

# Generated at 2022-06-13 15:49:14.873700
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    exc = None
    called = 0
    my_event = _EventSource()

    @my_event.on_collection_load.fire
    def my_handler_one(a, b, c=1, d='hello'):
        nonlocal called
        called += 1
        assert a == 'a'
        assert b == 'b'
        assert c == 'c'
        assert d == 'd'

    @my_event.on_collection_load.fire
    def my_handler_two(a, b, c='foo', d='bar'):
        # the next line would raise an exception if it were called
        pass

    # fire each handler, handler one should be called, handled_two should be skipped
    exc = my_event.on_collection_load.fire('a', 'b', c='c', d='d')



# Generated at 2022-06-13 15:49:17.382835
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert isinstance(es, _EventSource)
    assert isinstance(es._handlers, set)
    assert not es._handlers


# Generated at 2022-06-13 15:49:25.234765
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """
    Confirm that _EventSource.fire() invokes all handlers without changing the exception.
    """
    source = _EventSource()

    def handler(ex):
        if ex is not exception:
            raise ValueError('handler changed exception')
        if state[1]:
            state[0] += 1

    def handler2(ex):
        if ex is not exception:
            raise ValueError('handler2 changed exception')
        state[0] += 1

    state = [0, True]
    exception = ValueError('handler will re-raise this exception')

    source += handler
    source += handler2

    try:
        source.fire(exception)
        raise AssertionError('failed to re-raise exception')
    except ValueError:
        pass

    state[1] = False

    source.fire(exception)

   

# Generated at 2022-06-13 15:49:29.261317
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()
    event_source += handler
    assert event_source._handlers == {handler}
    event_source += handler
    assert event_source._handlers == {handler}


# Generated at 2022-06-13 15:49:35.031014
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self._on_exception = mock
            self._handlers = [self._handler_that_raises, self._handler_that_does_not_raise]

        def _handler_that_raises(self):
            raise Exception()

        def _handler_that_does_not_raise(self):
            pass

    exc = None
    try:
        MyEventSource().fire()
    except Exception as e:
        exc = e

    assert type(exc) is Exception



# Generated at 2022-06-13 15:49:43.379334
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=too-few-public-methods

    class TestObject(object):
        def __init__(self, id):
            self.id = id
            self.event_calls = []

        def handler(self, msg):
            self.event_calls.append(('handler', self.id, msg))

        def bad_handler(self, msg):
            self.event_calls.append(('bad_handler', self.id, msg))
            raise RuntimeError('bad handler')

    event_source = _EventSource()
    test_objects = [TestObject('A'), TestObject('B')]

    for t in test_objects:
        event_source += t.handler


# Generated at 2022-06-13 15:49:51.435553
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Unit test for method fire of class _EventSource
    class EventSource_test(object):
        """Test class for _EventSource class."""

        def __init__(self):
            self.on_load = _EventSource()
            self._handlers = None

        def __iadd__(self, handler):
            if not callable(handler):
                raise ValueError('handler must be callable')
            self._handlers.add(handler)
            return self

    def test_function(parsed_collection):
        """Test function for on_load event."""
        raise Exception("The function should not be called.")

    event = EventSource_test()
    event.on_load += test_function
    event.on_load.fire('foo')
    # The test_function should not be called.
    # And the exception should

# Generated at 2022-06-13 15:50:02.805246
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    assert len(event._handlers) == 0
    assert event.fire(1, 2, 3) is None

    event += handler1
    assert handler1.call_count == 0
    assert handler2.call_count == 0
    assert event.fire(4, 5, 6) is None
    assert handler1.call_count == 1
    assert handler2.call_count == 0
    assert handler1.call_args[0] == (4, 5, 6)
    assert handler1.call_args[1] == {}

    event -= handler1
    assert handler1.call_count == 1
    assert handler2.call_count == 0
    event.fire(7)
    assert handler1.call_count == 1
    assert handler2.call_count == 0

    event += handler2
   

# Generated at 2022-06-13 15:50:04.376626
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += 'not callable'


# Generated at 2022-06-13 15:50:11.213065
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """
    Test proxy of class _EventSource to verify that a callable argument can be passed to the fire method of class _EventSource

    """
    def my_sample_func():
        return "sample code"

    eventsource = _EventSource()
    eventsource += my_sample_func
    assert eventsource._handlers == {my_sample_func}

# Generated at 2022-06-13 15:50:27.869809
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Test:
        def __init__(self, expected_arg1, expected_arg2, expected_kwarg1, expected_kwarg2):
            self.expected_arg1 = expected_arg1
            self.expected_arg2 = expected_arg2
            self.expected_kwarg1 = expected_kwarg1
            self.expected_kwarg2 = expected_kwarg2

            self.actual_arg1 = None
            self.actual_arg2 = None
            self.actual_kwarg1 = None
            self.actual_kwarg2 = None

        def __call__(self, arg1, arg2, kwarg1=None, kwarg2=None):
            self.actual_arg1 = arg1
            self.actual_arg2 = arg2
            self.actual_kwarg1 = kwarg1


# Generated at 2022-06-13 15:50:38.800384
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    mock_handler = lambda *args, **kwargs: (args, kwargs)
    listener = _EventSource()
    try:
        listener += mock_handler
        listener += mock_handler
        listener += lambda *args, **kwargs: (args[0], kwargs['kw'])
        listener += lambda *args, **kwargs: (args[0], kwargs['kw'])
        assert mock_handler(1, kw=2) == listener.fire(1, kw=2)
    finally:
        listener -= mock_handler
        listener -= mock_handler

    expected = [(1, 2), (1, 2), (1, 2), (1, 2)]
    actual = listener.fire(1, kw=2)
    assert expected == actual, actual

# Generated at 2022-06-13 15:50:44.853096
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()
    class Foo:
        def __init__(self):
            self.fired = False

        def handler(self, *args, **kwargs):
            self.fired = True

    foo = Foo()
    bar = Foo()

    assert not foo.fired
    assert not bar.fired

    evt += foo.handler
    evt += bar.handler

    evt.fire()

    assert foo.fired
    assert bar.fired

# Generated at 2022-06-13 15:50:48.475121
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''
    Simple unit test to exercise the fire() method of _EventSource.
    '''

    called = [False]

    def handler():
        called[0] = True

    event_source = _EventSource()
    event_source += handler
    event_source.fire()

    assert called[0]

# Generated at 2022-06-13 15:50:52.646164
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    handler1 = lambda x, y: x + y
    handler2 = lambda x, y: x - y

    event_source = _EventSource()
    event_source += handler1
    assert event_source._handlers == {handler1}

    event_source += handler2
    assert event_source._handlers == {handler1, handler2}

    with pytest.raises(ValueError):
        event_source += 'not a callable'


# Generated at 2022-06-13 15:50:54.677490
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler(**kwargs):
        pass

    def handler2(**kwargs):
        pass

    es = _EventSource()
    es += handler
    es += handler
    es += handler2
    es += handler2

    assert len(es._handlers) == 2

# Generated at 2022-06-13 15:50:59.316321
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils.common.text.converters import to_bytes

    class _Target:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    def _handler_0(target):
        if target.value != to_bytes('foo'):
            raise ValueError('invalid argument to handler_0')

    def _handler_1(target):
        if target.value != to_bytes('foo'):
            raise ValueError('invalid argument to handler_1')

    def _handler_2(target):
        if target.value != to_bytes('foo'):
            raise ValueError('invalid argument to handler_2')
        raise ValueError('force an exception in handler_2')


# Generated at 2022-06-13 15:51:11.144474
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()
    es += lambda: True
    es += lambda: False
    assert es.fire() is None

    fired = [0, 0]
    es += lambda: fired.__setitem__(0, 1)
    es += lambda: fired.__setitem__(1, 2)
    es.fire()
    assert fired == [1, 2]

    fired = []
    es += lambda: fired.append(1)
    es += lambda: fired.append(2)
    es += lambda: fired.append(3)
    es += lambda: fired.append(4)
    es += lambda: fired.append(5)
    es.fire()
    assert fired == [1, 2, 3, 4, 5]


# Unit tests for methods collection_finder/collection_paths/playbook_paths of class

# Generated at 2022-06-13 15:51:20.930620
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_1(a, b, c=None):
        assert a == 1
        assert b == 2
        assert c is None

    def handler_2(a, b, c=None):
        assert a == 1
        assert b == 2
        assert c is None

    event_source = _EventSource()

    event_source += handler_1
    event_source += handler_2

    event_source.fire(1, 2)

    assert event_source._handlers == {handler_1, handler_2}

    event_source -= handler_1

    assert event_source._handlers == {handler_2}

    event_source -= handler_1

    assert event_source._handlers == {handler_2}


# Generated at 2022-06-13 15:51:24.478489
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert isinstance(event_source, _EventSource)


# Generated at 2022-06-13 15:51:37.946532
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    events = _EventSource()

    # we are testing around the private event source, so we need to access it via our
    # public property for coverage sake
    AnsibleCollectionConfig.on_collection_load += events

    # now test the addition of a valid handler
    events += lambda: None

    # now test the addition of a non-callable - which should raise a TypeError
    try:
        events += 42
        assert False
    except TypeError:
        pass

    # now test the addition of a lambda that throws - which should raise a similar exception

# Generated at 2022-06-13 15:51:48.726276
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    assert event._handlers == set()
    calls = []
    event += lambda *args, **kwargs: calls.append(('1', args, kwargs))
    event += lambda *args, **kwargs: calls.append(('2', args, kwargs))
    event += lambda *args, **kwargs: calls.append(('3', args, kwargs))
    event += lambda *args, **kwargs: calls.append(('4', args, kwargs))

    event.fire(1, 2, x=4, y=5)

    assert event._handlers == {calls[0][0], calls[1][0], calls[2][0], calls[3][0]}

# Generated at 2022-06-13 15:51:52.213008
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    a = 0
    def handler(*args, **kwargs):
        nonlocal a
        a += 1

    event_source = _EventSource()
    event_source += handler
    event_source.fire()
    assert a == 1

    event_source -= handler
    event_source.fire()
    assert a == 1



# Generated at 2022-06-13 15:51:58.193496
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.utils.collection_loader._util import fired

    ev = _EventSource()
    h = fired()

    ev.fire()
    assert not h.fired

    ev += h
    ev.fire()
    assert h.fired

    ev.fire()
    assert h.fired == 2

    ev -= h
    ev.fire()
    assert h.fired == 2

# Generated at 2022-06-13 15:52:05.126303
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    func1 = lambda : None
    func2 = lambda : 2/0

    event_source = _EventSource()

    event_source += func1
    event_source += func2

    event_source.fire()

    event_source -= func1
    event_source -= func2

    event_source += func1
    event_source += func2

    event_source.fire()

    event_source -= func1
    event_source -= func2

# Generated at 2022-06-13 15:52:09.746412
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(*args, **kwargs):
        assert args == ('x', 'y')
        assert kwargs == {'z': 3}

    test = _EventSource()
    test += handler
    test.fire('x', 'y', z=3)



# Generated at 2022-06-13 15:52:18.731930
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import os
    import tempfile

    temp = tempfile.NamedTemporaryFile(prefix='ansible-collections-loader-test', suffix='.py')
    temp.write(b'import sys\nprint("hello")\nsys.exit(0)')
    temp.flush()

    def handler(arg):
        os.system('python ' + temp.name)

    test1 = _EventSource()
    test1 += handler
    test1.fire(1)

    test1 -= handler
    test1 += ExampleEventSource__iadd__
    test1.fire(2)

    test1 -= ExampleEventSource__iadd__
    test1 += ExampleEventSource__iadd__
    test1 += ExampleEventSource__iadd__
    test1 -= ExampleEventSource__iadd__
    test1.fire(3)

   

# Generated at 2022-06-13 15:52:21.773732
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    handler = lambda: None
    event += handler

    try:
        event.fire()
        assert(True)
    except Exception as ex:
        assert(False)


# Generated at 2022-06-13 15:52:31.921547
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()
    result = []

    def handler1(s):
        result.append(s)
        return 1

    e += handler1
    e.fire('first')
    assert result == ['first']

    def handler2(s):
        raise Exception('should not have been called')

    result.clear()
    e += handler2
    e -= handler1

    def on_exception(handler, exc, *args, **kwargs):
        assert handler is handler2
        assert str(exc) == 'should not have been called'
        assert args == ('second',)
        assert kwargs == {'foo': 'bar'}
        return False

    e._on_exception = on_exception
    e.fire('second', foo='bar')

    assert result == []

# Generated at 2022-06-13 15:52:33.196739
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

# Generated at 2022-06-13 15:52:49.375958
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass

# Generated at 2022-06-13 15:52:57.951863
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def foo(arg):
        raise Exception("Failed")

    def bar(arg):
        return True

    event = _EventSource()

    event += foo
    event += bar
    try:
        event.fire("test")
    except Exception:
        raise AssertionError("The exception should be processed by the handler")
    else:
        # should get here
        pass

    event -= bar
    try:
        event.fire("test")
    except Exception:
        # should get here
        pass
    else:
        raise AssertionError("The exception should not be processed by the handler")

# Generated at 2022-06-13 15:53:05.239785
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # sets up a class to hold the handlers
    class EventObject(object):
        def __init__(self):
            self._handlers = []

        def handler(self, *args):
            self._handlers.append(args)

    # create an event source and register a handler
    source = _EventSource()
    obj = EventObject()
    source += obj.handler

    # fire the event and verify the handler was called
    source.fire('a', 'b', 'c')
    assert obj._handlers == [('a', 'b', 'c')]


# Generated at 2022-06-13 15:53:08.457488
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler():
        pass

    es += handler

    assert handler in es._handlers

# Unit tests for method __isub__ of class _EventSource

# Generated at 2022-06-13 15:53:21.114461
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(text):
        assert text == 'hello from the event fire'
        return

    def handler2(text):
        assert text == 'hello from the event fire'
        return

    def handler3(text):
        assert text == 'hello from the event fire'
        raise Exception()

    # exercises:
    #
    #  - fire with no handlers returns None
    #  - handler exceptions do not stop firings
    #  - on_exception ignores exceptions
    #  - on_exception returns True, which causes the exception to be re-raised

    es = _EventSource()
    assert es.fire('hello from the event fire') is None
    es += handler1
    assert es.fire('hello from the event fire') is None
    es += handler2
    assert es.fire('hello from the event fire') is None


# Generated at 2022-06-13 15:53:31.288350
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Tester:
        def __init__(self):
            self.called = 0

        def __call__(self, *args, **kwargs):
            self.called += 1

    es = _EventSource()

    assert len(es._handlers) == 0

    T1 = _Tester()
    T2 = _Tester()

    es += T1
    es += T2

    assert len(es._handlers) == 2

    es.fire()

    assert T1.called == 1
    assert T2.called == 1

    es -= T1

    assert len(es._handlers) == 1

    es.fire()

    assert T1.called == 1
    assert T2.called == 2

    es -= T2

    assert len(es._handlers) == 0

    es.fire()

   

# Generated at 2022-06-13 15:53:37.000330
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    call_count = 0
    ec = _EventSource()

    def handler0():
        nonlocal call_count
        call_count += 1

    ec += handler0
    ec += lambda: None
    assert ec._handlers == {handler0, lambda: None}
    ec.fire()

    assert call_count == 1
    with pytest.raises(ValueError):
        class BadHandler:
            pass

        ec += BadHandler
    assert call_count == 1

# Generated at 2022-06-13 15:53:46.129687
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def event_handler():
        pass

    def non_event_handler():
        pass

    event_source = _EventSource()

    assert len(event_source._handlers) == 0

    event_source += event_handler
    assert len(event_source._handlers) == 1

    event_source += event_handler
    assert len(event_source._handlers) == 1

    event_source += non_event_handler
    assert len(event_source._handlers) == 2

    event_source -= event_handler

    assert len(event_source._handlers) == 1


# Generated at 2022-06-13 15:53:54.528027
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Handler:
        def __init__(self, name):
            self._name = name

        def __call__(self, *args, **kwargs):
            print('Hello %s' % self._name)
            #return 'Hello %s' % self._name

    testEventSource = _EventSource()
    testEventSource += Handler('a')
    testEventSource += Handler('b')
    #output = testEventSource.fire()
    testEventSource.fire()
    #output = testEventSource.fire()
    #print(output)
    testEventSource.fire()
    testEventSource -= Handler('b')
    #output = testEventSource.fire()
    testEventSource.fire()
    #print(output)
    #testEventSource -= Handler('b')
    #output = testEventSource.fire()
   

# Generated at 2022-06-13 15:53:57.607426
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    def dummy_handler(x):
        return x

    evt += dummy_handler
    assert evt.fire(2) == 2



# Generated at 2022-06-13 15:54:36.683579
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    i = _EventSource()

    def f():
        pass

    f2 = f
    i += f
    assert len(i._handlers) == 1

    i += f  # test double-setting of handler
    assert len(i._handlers) == 1

    i += f2  # test double-setting of handler with a different but equivalent handle
    assert len(i._handlers) == 1

    def f3():
        pass

    i += f3

    assert len(i._handlers) == 2

    def bad_iadd():
        i += ('not a function',)

    import pytest
    with pytest.raises(ValueError):
        bad_iadd()



# Generated at 2022-06-13 15:54:43.054420
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def h1(*args, **kwargs):
        return args, kwargs

    def h2(*args, **kwargs):
        return args, kwargs

    source = _EventSource()

    source += h1
    source += h2

    assert source.fire(1, 2, a=3, b=4) is None
    assert h1 == h2


# mock for the AnsibleCollectionFinder class

# Generated at 2022-06-13 15:54:43.669864
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass

# Generated at 2022-06-13 15:54:50.965544
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    class Handler:
        def __init__(self, parent):
            self._parent = parent

        def __call__(self, value):
            self._parent.assertEqual('hi', value)

    class EventSource(_EventSource):
        def __init__(self, parent):
            super(EventSource, self).__init__()
            self._parent = parent

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._parent.assertFalse('should not be called')

    class Test_EventSource(unittest.TestCase):

        def test_single_handler(self):
            evt = EventSource(self)
            evt += Handler(self)

            evt.fire('hi')

        def test_multiple_handlers(self):
            evt

# Generated at 2022-06-13 15:54:55.536442
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    assert hasattr(AnsibleCollectionConfig._on_collection_load, '__iadd__')

    # test with a function
    def foo():
        pass

    # +=
    assert not (foo in AnsibleCollectionConfig._on_collection_load._handlers)
    AnsibleCollectionConfig.on_collection_load += foo
    assert (foo in AnsibleCollectionConfig._on_collection_load._handlers)
    AnsibleCollectionConfig.on_collection_load -= foo
    assert not (foo in AnsibleCollectionConfig._on_collection_load._handlers)

    # +
    collection_load_handlers = AnsibleCollectionConfig.on_collection_load._handlers
    AnsibleCollectionConfig.on_collection_load + foo
    assert (foo in AnsibleCollectionConfig._on_collection_load._handlers)

# Generated at 2022-06-13 15:54:58.296784
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()
    event_source += handler

    assert len(event_source._handlers) == 1
    assert handler in event_source._handlers



# Generated at 2022-06-13 15:55:01.495385
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    fired = []
    class MyEventSource(_EventSource):
        pass

    def handler(x):
        fired.append(x)
    es = MyEventSource()
    es += handler
    es.fire(10)
    es.fire(20)
    assert fired == [10, 20]



# Generated at 2022-06-13 15:55:09.633480
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Sample:
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    event_source = Sample()

    def handler_one(*args, **kwargs):
        return args

    def handler_two(*args, **kwargs):
        raise Exception('exception from handler_two')

    event_source += handler_one
    event_source += handler_two

    try:
        event_source.fire('one', 'two', 'three')
        assert False, "should have raised an Exception"
    except:
        pass

# Generated at 2022-06-13 15:55:20.785763
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible_collections.ansible.foo.plugins.action import ActionModule as ActionFoo
    from ansible_collections.ansible.bar.plugins.action import ActionModule as ActionBar

    def on_collection_load(collection):
        pass

    AnsibleCollectionConfig.on_collection_load += on_collection_load

    assert AnsibleCollectionConfig.on_collection_load._handlers == {on_collection_load}

    AnsibleCollectionConfig.on_collection_load += on_collection_load

    assert AnsibleCollectionConfig.on_collection_load._handlers == {on_collection_load}

    AnsibleCollectionConfig.on_collection_load -= on_collection_load

    assert AnsibleCollectionConfig.on_collection_load._handlers == set()

    AnsibleCollectionConfig.on_collection_load += on_collection_load

# Generated at 2022-06-13 15:55:33.246491
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test scenario:
    # Test case fire:
    #  - Test when handler raises exception
    #  - Test when handler returns True
    #  - Test when handler returns False

    class ExceptionHandler(object):
        def __call__(self, *args, **kwargs):
            raise RuntimeError('test ran')

    class TrueHandler(object):
        def __call__(self, *args, **kwargs):
            return True

    class FalseHandler(object):
        def __call__(self, *args, **kwargs):
            return False

    es = _EventSource()

    # handler raises exception
    es += ExceptionHandler()
    try:
        es.fire()
        raise AssertionError('_EventSource.fire() failed to re-raise exception')
    except RuntimeError:
        pass

    # handler returns True


# Generated at 2022-06-13 15:56:36.660222
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert isinstance(event_source, _EventSource)



# Generated at 2022-06-13 15:56:41.220316
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

    def handler_one():
        pass

    def handler_two():
        raise Exception()

    event += handler_one

    try:
        event += handler_two
        raise AssertionError('should have received an exception')
    except ValueError:
        pass

    # test that the callable value was not added
    assert len(event._handlers) == 1



# Generated at 2022-06-13 15:56:43.972386
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler():
        pass

    def add():
        event_source += handler

    def subtract():
        event_source -= handler

    add()
    subtract()
    # Subsequent invocations of add() and subtract() should not raise an exception due to the handler being removed
    add()
    subtract()



# Generated at 2022-06-13 15:56:50.410930
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    test_event_source = _EventSource()
    def handler_a(i):
        if i % 2 != 0:
            return "odd"
        else:
            return "even"

    def handler_b(i):
        if i > 100:
            return "> 100"
        else:
            return "<= 100"

    handler_c = lambda i: i

    test_event_source += handler_a
    assert handler_a in test_event_source._handlers

    test_event_source += handler_b
    assert handler_b in test_event_source._handlers

    test_event_source += handler_c
    assert handler_c in test_event_source._handlers

    test_event_source += handler_b
    assert handler_b in test_event_source._handlers


# Generated at 2022-06-13 15:57:00.884817
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    for _ in range(0, 2):
        event_source = _EventSource()
        event_source += handler_a
        event_source += handler_b

        fire_calls = []

        def handler_a(data):
            fire_calls.append('A')

        def handler_b(data):
            fire_calls.append('B')

        event_source.fire()
        assert fire_calls == ['A', 'B']

        fire_calls = []

        def handler_a(data):
            fire_calls.append('A')
            raise Exception('Exception in Handler A')

        def handler_b(data):
            fire_calls.append('B')


# Generated at 2022-06-13 15:57:12.897856
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test1: no handlers, expect no exception
    s = _EventSource()
    s.fire()

    # Test2: one handler, expect no exception
    s = _EventSource()
    s += lambda: None
    s.fire()

    # Test3: one handler raising an exception, expect no exception
    s = _EventSource()
    s += lambda: 1 / 0
    s.fire()

    # Test4: one handler raising an exception, overriding _on_exception to suppress the exception, expect no exception
    s = _EventSource()
    s += lambda: 1 / 0
    s._on_exception = lambda handler, err, *args, **kwargs: False
    s.fire()

    # Test5: one handler raising an exception, overriding _on_exception to re-raise the exception, expect exception
    s = _

# Generated at 2022-06-13 15:57:22.027300
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self, exc=None):
            super(_TestEventSource, self).__init__()
            self.exc = exc

        def _on_exception(self, handler, exc, *args, **kwargs):
            if isinstance(exc, self.exc):
                return False

            return True

    x = _TestEventSource()
    x += lambda: 1 / 0
    try:
        x.fire()
        assert False, 'RuntimeError should have been raised'
    except RuntimeError:
        pass

    x = _TestEventSource(ZeroDivisionError)
    x += lambda: 1 / 0
    x.fire()



# Generated at 2022-06-13 15:57:27.080023
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import sys

    def handler1(value):
        print('handler1 %s' % value)

    def handler2(value):
        print('handler2 %s' % value)

    es = _EventSource()
    es += handler1
    es += handler2
    es += handler2

    assert es._handlers == set([handler1, handler2])

    es += sys
    assert es._handlers == set([handler1, handler2])


# Generated at 2022-06-13 15:57:37.370613
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self, *events):
            super(MyEventSource, self).__init__()
            self.events = list(events)
            self.expect_exc = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            if exc is self.expect_exc:
                self.events.append(('handler %s raised (%s, %s, %s, %s)' % (handler, exc, args, kwargs, str(exc))))
                return True
            else:
                raise exc

    valid_event = ('valid event', ('arg',), {'kwarg': 'value'})
    expected_events = [valid_event, ]
    my_event_source = MyEventSource()

# Generated at 2022-06-13 15:57:42.223841
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    fired = []
    event = _EventSource()
    event += lambda *args, **kwargs: fired.append((args, kwargs))

    event.fire(1, 2, kw=3)

    assert len(fired) == 1
    assert fired[0][0] == (1, 2)
    assert fired[0][1] == {'kw': 3}

