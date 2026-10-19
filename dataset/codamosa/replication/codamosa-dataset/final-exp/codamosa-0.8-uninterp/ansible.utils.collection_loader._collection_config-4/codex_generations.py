

# Generated at 2022-06-13 15:49:04.627105
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    def handler(a):
        return a * 2

    event += handler
    assert event.fire(11) == 22, 'handler(a) should return a * 2'

# Generated at 2022-06-13 15:49:14.221380
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    # Create an event source and define variable to verify that a handler is called
    event = _EventSource()
    handler_called = False

    # Create a handler for the event
    def handler():
        nonlocal handler_called
        handler_called = True

    # Subscribe to the event the handler
    event += handler

    # Fire the event
    event.fire()

    # Verify that the handler was called
    assert handler_called

    # Subscribe to the event with a handler that raises an exception
    event += lambda: 1/0

    # Verify that the exception is not trapped, but passed up the call chain
    with pytest.raises(ZeroDivisionError):
        event.fire()

    # Verify that the '_on_exception' method is not called for the handler that does not raise an exception
    def handler():
        non

# Generated at 2022-06-13 15:49:19.394144
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class FakeHandler:
        def __call__(self, *args, **kwargs):
            pass

    src = _EventSource()

    handler1 = FakeHandler()
    src += handler1

    handler2 = FakeHandler()
    src += handler2

    # should not raise
    src.fire()

    # Should not raise
    src -= handler1

    # Should not raise
    src -= handler2

    # Should not raise
    src.fire()

# Generated at 2022-06-13 15:49:23.635839
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    # Test case: event source is initially empty
    es = _EventSource()
    assert len(es._handlers) == 0

    # Test case: handler is callable
    handler = lambda: None
    es += handler
    assert handler in es._handlers

    # Test case: handler is not callable
    with pytest.raises(ValueError):
        es += 'notCallable'


# Generated at 2022-06-13 15:49:25.556764
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    assert len(source._handlers) == 0

    handler = lambda a: None
    source += handler

    assert len(source._handlers) == 1

    source.fire()

    source -= handler

    assert len(source._handlers) == 0

# Generated at 2022-06-13 15:49:30.203525
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """Unit test for _EventSource.fire"""
    on_collection_load = AnsibleCollectionConfig.on_collection_load

    # no handlers
    on_collection_load.fire(None, None)

    # one handler
    def handler_1(arg1, arg2, kwarg1=None):
        assert (arg1 == 'arg1')
        assert (arg2 == 'arg2')
        assert (kwarg1 == 'kwarg1')

    on_collection_load += handler_1
    on_collection_load.fire('arg1', 'arg2', kwarg1='kwarg1')
    on_collection_load -= handler_1

    # one handler raises exception
    def handler_2(arg1, arg2, kwarg1=None):
        assert (arg1 == 'arg1')

# Generated at 2022-06-13 15:49:34.027422
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class CallableClass:
        def __call__(self):
            pass

    callable_func = CallableClass()
    callable_lambda = lambda: None

    event_source = _EventSource()

    # Test __iadd__ with callable function and method
    event_source += callable_func
    event_source += callable_lambda

    # Test that adding the same function twice does not raise an error
    event_source += callable_func

    # Test that adding a non-callable function will raise an exception
    try:
        event_source += 0
        raise AssertionError('Expected ValueError when adding non-callable to _EventSource instance')
    except ValueError:
        pass



# Generated at 2022-06-13 15:49:41.055602
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import six

    class Handler(object):

        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            self.func(*args, **kwargs)

    def handler1(x, y):
        raise Exception('handler1')

    def handler2(x):
        raise Exception('handler2')

    def handler3(x):
        raise Exception('handler3')
        return True

    def handler4(x, y):
        pass

    default_expected = 'handler1'

    #
    # multiple handlers : each exception is unique
    #
    x = _EventSource()
    x += Handler(handler1)
    x += Handler(handler2)
    x += Handler(handler3)
    x += Handler(handler4)


# Generated at 2022-06-13 15:49:44.886084
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self.handler_fired = False

        def handler(self):
            self.handler_fired = True

    es = TestEventSource()
    es += es.handler
    assert not es.handler_fired

    es.fire()
    assert es.handler_fired


# Generated at 2022-06-13 15:49:52.342952
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    events = _EventSource()
    events.fire()

    def handler(*args, **kwargs):
        pass

    events += handler

    events.fire()

    def handler_with_exception(*args, **kwargs):
        raise TestException()

    events += handler_with_exception

    try:
        events.fire()
        assert False, 'Expected TestException()'
    except TestException:
        pass

    events -= handler_with_exception
    events.fire()

    events -= handler
    events.fire()

# Generated at 2022-06-13 15:50:06.625657
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.module_utils.common._collections_compat import HashableDict
    from ansible.utils.collection_loader import AnsibleCollectionFinder

    AnsibleCollectionConfig.collection_finder = AnsibleCollectionFinder(
        playbook_paths=['/does/not/exist'],
        collection_paths=['/does/not/exist'] + [HashableDict(my_key='my_value')]
    )
    AnsibleCollectionConfig.on_collection_load += lambda *args, **kwargs: print('on_collection_load fired')

    import inspect
    import copy

    # test __iadd__ with a valid value
    test_1_handler = lambda *args, **kwargs: print('handler fired')
    AnsibleCollectionConfig.on_collection_load += test_1_handler
    assert Ansible

# Generated at 2022-06-13 15:50:10.740213
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def _callable():
        pass

    the_class = AnsibleCollectionConfig()

    the_class.on_collection_load += _callable

    the_class.on_collection_load.fire()

# Generated at 2022-06-13 15:50:19.384875
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class Source(_EventSource):
        pass

    result = []
    source = Source()
    source += lambda *a, **kw: result.append('1st')
    source += lambda *a, **kw: result.append('2nd')
    source += lambda *a, **kw: result.append('3rd')
    source.fire()

    assert set(result) == set(['1st', '2nd', '3rd'])
    assert len(result) == 3

    # try it again to test idempotence
    result.clear()
    source.fire()

    assert set(result) == set(['1st', '2nd', '3rd'])
    assert len(result) == 3



# Generated at 2022-06-13 15:50:27.120131
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible_collections.ansible.builtin.tests.unit.compat.mock import MagicMock
    mock_handler = MagicMock()

    # calling __iadd__ when no handler is already registered
    event_source = _EventSource()
    event_source += mock_handler
    assert mock_handler in event_source._handlers

    # calling __iadd__ when handler is already registered
    event_source += mock_handler
    assert len(mock_handler.mock_calls) == 0

    # calling __isub__ when handler is not present should not raise an exception
    event_source -= mock_handler
    assert len(mock_handler.mock_calls) == 0


# Generated at 2022-06-13 15:50:30.920880
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handle(arg):
        print('handle arg={}'.format(arg))

    event_source += handle

    event_source.fire('hi')



# Generated at 2022-06-13 15:50:38.947415
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible_collections.ansible.builtin.plugins.module_utils.collection_loader._pickle_compat import BaseException

    class CustomException(BaseException):
        pass

    class Handler1:
        def __call__(self, *args, **kwargs):
            pass

    class Handler2:
        def __call__(self, *args, **kwargs):
            raise CustomException()

    class Handler3:
        def __call__(self, *args, **kwargs):
            raise ValueError()

    handlers = (Handler1(), Handler2(), Handler3())

    event_source = _EventSource()

    for h in handlers:
        event_source += h

    try:
        event_source.fire()
    except CustomException:
        # custom exception should have propagated to caller
        pass

# Generated at 2022-06-13 15:50:48.474934
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test handler with no argument
    e = _EventSource()
    def f():
        f.cnt += 1
    f.cnt = 0
    e += f
    assert not f.cnt
    e.fire()
    assert f.cnt
    e.fire()
    assert f.cnt == 2

    # Test handler with one argument
    e = _EventSource()
    def g(arg):
        g.cnt += arg
    g.cnt = 0
    e += g
    assert not g.cnt
    e.fire('abc')
    assert g.cnt == 'abc'
    e.fire('def')
    assert g.cnt == 'abcdef'
    e.fire(g='xyz')
    assert g.cnt == 'abcdefxyz'

    # Test handler with

# Generated at 2022-06-13 15:50:51.166809
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    emitter = _EventSource()
    handler = MockEventHandler()

    emitter += handler

    assert handler in emitter._handlers


# Generated at 2022-06-13 15:50:55.538978
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import pytest

    e = _EventSource()

    def handler(arg):
        pass

    assert handler not in e._handlers

    e.__iadd__(handler)

    assert handler in e._handlers

    with pytest.raises(ValueError):
        e.__iadd__('not a callable')



# Generated at 2022-06-13 15:50:57.959804
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    method = _EventSource.__iadd__
    import unittest.mock as mock

    instance = _EventSource()
    method(instance, mock.Mock())
    assert len(instance._handlers) == 1

# Generated at 2022-06-13 15:51:08.707403
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    foo = []

    evt += (lambda: foo.append(1))
    evt += (lambda: foo.append(2))

    evt.fire()

    assert foo == [1, 2]

# Generated at 2022-06-13 15:51:11.191425
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    event_source.fire()


# Unit test to confirm unique symbols are defined in AnsibleCollectionConfig

# Generated at 2022-06-13 15:51:21.428625
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # The setUp and tearDown callbacks of the collection loader API are implemented as an _EventSource.
    # These unit tests verify the _EventSource.fire method.
    import pytest

    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self._log = []

        def _on_exception(self, handler, exc, *args, **kwargs):
            handler_name = getattr(handler, 'func_name', getattr(handler, 'im_func', None))
            raise_exception = getattr(handler, 'raise_exception', None)
            if raise_exception:
                self._log.append((handler_name, True, repr(exc)))
                return True

# Generated at 2022-06-13 15:51:32.510824
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(a1, k1=None):
        raise ValueError('test')

    def handler2(a1, k1=None):
        raise ValueError('test')

    def handler3(a1, k1=None):
        pass

    def handler4(a1, k1=None):
        raise ValueError('test')

    e = _EventSource()

    e += handler1
    e += handler2
    e += handler3
    e += handler4

    raised_exc = None

    try:
        e.fire('a', k='k')
    except Exception as ex:
        raised_exc = ex

    assert raised_exc is not None

    assert isinstance(raised_exc, ValueError)
    assert str(raised_exc) == 'test'


# Generated at 2022-06-13 15:51:36.363140
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    eventsource = _EventSource()
    def testfunc_one(x):
        return x * 2
    def testfunc_two(x):
        return x * 3
    assert testfunc_one not in eventsource._handlers
    assert testfunc_two not in eventsource._handlers
    eventsource += testfunc_one
    assert testfunc_one in eventsource._handlers
    assert testfunc_two not in eventsource._handlers


# Generated at 2022-06-13 15:51:42.801191
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def noop_handler(*args, **kwargs):
        pass

    es = _EventSource()
    assert len(es._handlers) == 0
    es += noop_handler
    assert len(es._handlers) == 1
    es += noop_handler
    assert len(es._handlers) == 2
    es += noop_handler
    assert len(es._handlers) == 3


# Generated at 2022-06-13 15:51:51.727059
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Prepare
    class MyTestObject():
        def __init__(self):
            self.__first_result = None
            self.__second_result = None

        def first_handler(self, foo, bar):
            self.__first_result = (foo, bar)

        def second_handler(self, foo, bar):
            self.__second_result = (foo, bar)

    t = MyTestObject()
    es = _EventSource()
    es += t.first_handler
    es += t.second_handler

    # Execute
    es.fire('bar', foo='foo')

    # Assert
    assert t.__first_result == ('bar', 'foo')
    assert t.__second_result == ('bar', 'foo')


# Generated at 2022-06-13 15:52:04.594606
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler_1(a):
        pass

    def handler_2(a):
        pass

    def handler_3(a):
        pass

    event_source = _EventSource()

    # WHEN
    event_source += handler_1
    event_source += handler_2
    # THEN
    assert len(event_source._handlers) == 2

    # WHEN
    event_source += handler_3
    # THEN
    assert len(event_source._handlers) == 3

    # WHEN
    event_source += handler_1
    # THEN
    assert len(event_source._handlers) == 3

    # WHEN
    event_source += handler_2
    # THEN
    assert len(event_source._handlers) == 3

    # WHEN

# Generated at 2022-06-13 15:52:14.357729
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def func0():
        pass

    def func1(a):
        pass

    def func2(a, b):
        pass

    def func3(a, b, c):
        pass

    def func4(a, b, c, d):
        pass

    def func5(a, b, c, d, e):
        pass

    EventSource = _EventSource()
    EventSource += func0
    EventSource += func1
    EventSource += func2
    EventSource += func3
    EventSource += func4
    EventSource += func5
    EventSource -= func2
    EventSource -= func3
    EventSource -= func2

    # is the set of handlers to fire defined correctly?
    assert len(EventSource._handlers) == 4

    # do positional arguments work?
    EventSource.fire(1)


# Generated at 2022-06-13 15:52:22.630480
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=unused-variable
    # pylint: disable=too-few-public-methods
    class mock_obj:
        def __init__(self):
            self.target = ''

        def _handler(self, data):
            self.target += data

    # pylint: enable=too-few-public-methods
    # pylint: enable=unused-variable
    event = _EventSource()

    mock = mock_obj()

    # pylint: disable=no-member
    event += mock.handler

    event.fire('a')
    assert mock.target == 'a', "Failed to fire event correctly"

    event.fire('b')
    assert mock.target == 'ab', "Failed to fire event correctly"

    event.fire('c')

# Generated at 2022-06-13 15:52:31.816334
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    event_source += lambda: None
    assert len(event_source._handlers) == 1

    event_source += lambda: None
    assert len(event_source._handlers) == 2

    assert event_source == event_source

    try:
        event_source += None
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 15:52:44.496686
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    process_event = object()

    class SomeData:
        pass

    class TestException(Exception):
        pass

    test_event = _EventSource()
    test_event._on_exception = lambda self, handler, exc, *args, **kwargs: isinstance(exc, TestException)

    def handler(obj, from_process):
        return from_process

    def event_handler(obj, from_event):
        return from_event

    test_event += handler
    test_event += event_handler

    # Call the handler function with the process_event object we prepared
    r = test_event.fire(SomeData(), from_process=process_event)
    assert r == process_event
    # Call the handler function with the event_handler object we prepared

# Generated at 2022-06-13 15:52:54.086658
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    evs = _EventSource()

    def handler1(arg1, kwarg1='default'):
        return arg1, kwarg1

    def handler2(arg1, kwarg1='default'):
        return arg1.lower(), kwarg1.lower()

    def handler3(arg1, kwarg1='default'):
        raise ValueError('just testing')

    evs += handler1
    evs += handler2
    evs += handler3

    assert evs.fire('ARG1', kwarg1='KWARG1') == [('ARG1', 'KWARG1'), ('arg1', 'kwarg1')]
    assert evs.fire('ARG1', kwarg1='KWARG1') == [('arg1', 'kwarg1')]

# Generated at 2022-06-13 15:53:02.563165
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Arrange
    event_source = _EventSource()
    event_1 = False
    event_2 = False
    event_3 = False
    event_4 = False

    event_1_handler = lambda: setattr(event_1, 'test', True)
    event_2_handler = lambda: setattr(event_2, 'test', True)
    event_3_handler = lambda: setattr(event_3, 'test', True)
    event_4_handler = lambda: setattr(event_4, 'test', True)

    # Act
    event_source += event_1_handler
    event_source += event_2_handler
    event_source += event_3_handler
    event_source += event_4_handler

    event_source.fire()

    event_source -= event_1_handler
   

# Generated at 2022-06-13 15:53:06.650915
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called = []

    def handler(*args, **kwargs):
        called.append((args, kwargs))

    source = _EventSource()
    source += handler
    source.fire(1, 2, 3, a=4, b=5, c=6)
    source -= handler
    source.fire(7, 8, 9, a=10, b=11, c=12)

    assert called == [(
        (1, 2, 3),
        dict(a=4, b=5, c=6),
    )]



# Generated at 2022-06-13 15:53:19.731692
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self._on_exception_count = 0

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._on_exception_count += 1
            if not handler.__name__.startswith('_handler'):
                return False
            try:
                raise exc
            except:
                return False
            # We should never get here, but PyCharm flags this line as unreachable.
            # noinspection PyUnreachableCode
            return True

    def _handler_1(*args, **kwargs):
        print('_handler_1: args are {}'.format(args))

# Generated at 2022-06-13 15:53:30.397247
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Source(object):
        pass

    source = Source()
    source.event = _EventSource()

    got_event = []

    def on_event1(*args, **kwargs):
        got_event.append("on_event1")
        return

    def on_event2(*args, **kwargs):
        got_event.append("on_event2")
        return

    def on_event3(*args, **kwargs):
        got_event.append("on_event3")
        raise Exception("ev3")

    def on_event4(*args, **kwargs):
        got_event.append("on_event4")
        raise Exception("ev4")

    source.event += on_event1
    source.event += on_event2
    source.event += on_event3
    source.event += on

# Generated at 2022-06-13 15:53:37.037670
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def my_callback():
        pass

    es = _EventSource()
    assert not es._handlers

    es += my_callback
    assert len(es._handlers) == 1

    es += my_callback
    assert len(es._handlers) == 1

    es -= my_callback
    assert len(es._handlers) == 0

    es -= my_callback
    assert len(es._handlers) == 0

    with pytest.raises(ValueError):
        es += 1



# Generated at 2022-06-13 15:53:48.649167
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Create class DummyClass
    class DummyClass:
        def __init__(self):
            self.result = []

        def add_to_result(self, event):
            self.result.append(event)

    # Create instance of DummyClass
    dummy = DummyClass()

    # Create event source
    es = _EventSource()

    # Check the handlers set initially is empty
    assert es._handlers == set()

    # Check the result initially is empty
    assert dummy.result == []

    # Register handler
    es += dummy.add_to_result

    # Check the handlers set after adding a handler
    assert es._handlers == {dummy.add_to_result}

    # Fire the event source
    es.fire('hello')

    # Check the result after firing
    assert dummy.result == ['hello']

# Generated at 2022-06-13 15:54:00.412221
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    class TestEventSource(unittest.TestCase):
        def test_empty(self):
            es = _EventSource()
            es.fire('foo')

        def test_one(self):
            es = _EventSource()
            calls = []

            def call(_, arg):
                calls.append(arg)

            es += call
            es.fire('abc')

            self.assertEqual(1, len(calls))
            self.assertEqual('abc', calls[0])

        def test_many(self):
            es = _EventSource()
            calls = []

            def call1(_, arg1):
                calls.append(arg1)

            def call2(_, arg2):
                calls.append(arg2)

            es += call1
            es += call2
            es

# Generated at 2022-06-13 15:54:12.521779
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda *args, **kwargs: None
    es += lambda *args, **kwargs: None

    # Call method twice to verify handlers are only added once
    es += lambda *args, **kwargs: None


# Generated at 2022-06-13 15:54:14.639104
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def foo():
        pass

    e += foo
    e += foo

    e.fire()

# Generated at 2022-06-13 15:54:26.073626
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # unit test EventSource with handler that does not raise an exception
    event_source = _EventSource()
    handler = lambda: None
    event_source.fire()
    event_source += handler
    event_source.fire()
    event_source -= handler
    event_source.fire()

    # unit test EventSource with handler that always raises an exception
    event_source = _EventSource()
    handler = lambda: raise_exception()
    event_source.fire()
    event_source += handler

    with pytest.raises(Exception):
        event_source.fire()

    event_source -= handler
    event_source.fire()

    # unit test EventSource with handler that raises an exception the first time called
    # but then returns normally on subsequent calls
    handler_mock = Mock()
    handler_mock.side_effect

# Generated at 2022-06-13 15:54:36.412703
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventListener:
        def first(self, foo, bar=None):
            self._foo = foo
            self._bar = bar
            self._called = True

        def second(self, foo, bar=None):
            self._foo = foo
            self._bar = bar
            self._called = True

        def third(self, foo, bar=None):
            self._foo = foo
            self._bar = bar
            self._called = True

    listener = _EventListener()

    event = _EventSource()
    event += listener.first
    event += listener.second
    event += listener.third

    event.fire('foo', bar='bar')

    assert listener._foo == 'foo'
    assert listener._bar == 'bar'
    assert listener._called



# Generated at 2022-06-13 15:54:41.779832
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()

    def func1(x):
        pass

    def func2(x):
        pass

    source += func1
    source += func2

    assert func1 in source._handlers
    assert func2 in source._handlers
    assert len(source._handlers) == 2


# Generated at 2022-06-13 15:54:46.828360
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def print_hello(*args, **kwargs):
        print('hello')

    def print_fail():
        raise Exception('should not raise')

    es = _EventSource()

    es += print_hello
    es += print_fail

    assert len(es._handlers) == 2

    es.fire()

    es -= print_fail

    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:54:57.815317
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''
    _EventSource().fire() should call callables in its set.
    _EventSource().fire() should not call a callable not in its set.
    _EventSource().fire() should remove the callable from its set if the callable raises an exception.
    '''
    def f(a, b=None, c=None):
        return (a, b, c)

    # _EventSource().fire() should call callables in its set.
    e = _EventSource()
    e += f
    assert e.fire('a') == (('a', None, None),)

    # _EventSource().fire() should not call a callable not in its set.
    assert e.fire('a') == ()

    # _EventSource().fire() should remove the callable from its set if the callable raises an exception.
    e

# Generated at 2022-06-13 15:55:07.870218
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()
    def handler_1(arg):
        print('handler_1 = %s' % arg)
    def handler_2(arg):
        print('handler_2 = %s' % arg)
    def handler_3(arg):
        print('handler_3 = %s' % arg)
    def handler_4(arg):
        raise Exception('handler_4 = %s' % arg)
    es += handler_1
    es += handler_2
    es += handler_3
    es += handler_4
    es.fire('test')

# Generated at 2022-06-13 15:55:14.026034
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += 1
    assert len(es._handlers) == 1
    es += 2
    assert len(es._handlers) == 2
    es -= 1
    assert len(es._handlers) == 1
    es += 1
    assert len(es._handlers) == 2
    handler = es._handlers.pop()
    es -= handler
    assert len(es._handlers) == 1
    es -= handler
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:55:21.315959
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    has_exception = False
    try:
        def handle_event(x, y):
            raise Exception('event handler failed')

        # we use += because __iadd__ is implemented
        # and fires event handler
        AnsibleCollectionConfig.on_collection_load += handle_event
        AnsibleCollectionConfig.on_collection_load.fire('x', y='y')
    except Exception as e:
        has_exception = True
        assert str(e) == "event handler failed", 'event handler did not fail'
    assert has_exception, 'event handler did not raise an exception'

# Generated at 2022-06-13 15:55:42.509373
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils.six import print_
    es = _EventSource()

    # test with a single handler
    def test_handler(arg):
        print_(arg)

    es += test_handler
    assert len(es._handlers) == 1
    es.fire('test')

    # test with a second handler
    def test_handler2(arg):
        print_(2 * arg)

    es += test_handler2
    assert len(es._handlers) == 2
    es.fire('test')

# Generated at 2022-06-13 15:55:48.607627
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def add1(x, y):
        return x + y

    def add2(x, y):
        return x + y

    event_source += add1
    event_source += add2
    assert len(event_source._handlers) == 2
    assert add1 in event_source._handlers
    assert add2 in event_source._handlers


# Generated at 2022-06-13 15:56:00.353832
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class E(Exception):
        pass

    class F:
        pass

    class R:
        pass
        def _on_exception(x):
            return False

    class T:
        pass
        def _on_exception(x, exc, *args, **kwargs):
            return True

    es = _EventSource()

    x = [False]

    def _m(*args, **kwargs):
        x[0] = True

    def _n(*args, **kwargs):
        raise E

    def _o(*args, **kwargs):
        raise ValueError

    es += _m
    es += _n
    es += _o

    # confirm _n raises the exception that it raised
    try:
        es.fire()
    except E as ex:
        assert ex
    else:
        raise Exception

# Generated at 2022-06-13 15:56:07.286761
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_ok(a, b):
        return a + b

    def handler_failure(a, b):
        print('failing')
        raise ValueError('handler_failure')

    def handler_capture_exception(a, b):
        try:
            handler_failure(a, b)
        except ValueError as ex:
            return str(ex)

    es = _EventSource()
    es += handler_ok
    es += handler_failure
    es += handler_capture_exception
    ret = es.fire(2, 3)
    print(ret)

# Generated at 2022-06-13 15:56:11.219408
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self._n_handlers_called = 0

        def _on_exception(self, handler, exc, *args, **kwargs):
            if isinstance(exc, ValueError):
                return False
            else:
                return True

        def handler1(self, *args, **kwargs):
            self._n_handlers_called += 1

        def handler2(self, *args, **kwargs):
            self._n_handlers_called += 2
            raise ValueError()

        @property
        def handlers_called(self):
            return self._n_handlers_called

    # test that everything is callable as expected
    # should raise an exception because handler2 raises a ValueError


# Generated at 2022-06-13 15:56:20.511536
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    s = _EventSource()

    def handler1(*args, **kwargs):
        print("--Inside handler1")

    def handler2(*args, **kwargs):
        print("--Inside handler2")

    s += handler1
    s += handler2

    # Expected: handler1, handler2
    s.fire("Hi")

    # Expected: None
    s -= handler2
    s.fire("Hi")

    # Expected: None
    s.remove(handler1)
    s.fire("Hi")

    # Expected: handler1, handler2
    s.fire("Hi")



# Generated at 2022-06-13 15:56:29.202720
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _FIRED = 'fired'

    class _Handler:
        def __init__(self, test_case):
            self._test_case = test_case
            self._fired = False

        def __call__(self, *args, **kwargs):
            self._test_case.assertFalse(self._fired)
            self._fired = True

        def assert_not_fired(self, test_case):
            test_case.assertFalse(self._fired)

        def assert_fired(self, test_case):
            test_case.assertTrue(self._fired)

    class _Test_EventSource(object):
        def __init__(self):
            self.test_case = None
            self._handlers = []

        def _EventSource(self, name):
            event_source = _EventSource()
            event_

# Generated at 2022-06-13 15:56:38.875547
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import os
    import tempfile

    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, 'test_file.txt')

    with open(test_file, 'w') as f:
        f.write('this is a test file')

    def get_bad_handler():
        return 123

    def get_call_handler():
        def call_handler(param):
            ok = False
            with open(test_file) as f:
                data = f.read()
                if param == 'this is a test file':
                    ok = True
            return ok
        return call_handler

    def get_exception_handler():
        def exception_handler(param):
            if param == 'raise exception':
                raise Exception('this is a test exception')
        return exception_handler

# Generated at 2022-06-13 15:56:44.854608
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        pass

    call_count = 0

    def handler1(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise Exception('error')

    def handler2(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise Exception('error')

    def handler3(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise Exception('error')

    es1 = MyEventSource()
    es1 += handler1
    es1 += handler2

    # fire() should raise because one handler re-raises while the other swallows the exception
    try:
        es1.fire()
    except Exception as ex:
        assert str(ex) == 'error'
    else:
        assert False

# Generated at 2022-06-13 15:56:46.201986
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class DummyEvent:
        pass

    e = _EventSource()
    e.fire(*DummyEvent())

# Generated at 2022-06-13 15:57:04.375624
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    s = _EventSource()
    h1 = lambda: 10
    s += h1

    assert len(s._handlers) == 1
    assert h1 in s._handlers


# Generated at 2022-06-13 15:57:13.964413
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler1(event):
        nonlocal count
        count += 1
        assert event == 'event_x'

    count = 0
    on_collection_load = _EventSource()
    on_collection_load += handler1
    on_collection_load.fire('event_x')
    assert count == 1

    count = 0
    with_metaclass(_AnsibleCollectionConfig, 'AnsibleCollectionConfig').on_collection_load = on_collection_load
    AnsibleCollectionConfig.on_collection_load.fire('event_x')
    assert count == 2

    with_metaclass(_AnsibleCollectionConfig, 'AnsibleCollectionConfig').on_collection_load += handler1
    AnsibleCollectionConfig.on_collection_load.fire('event_x')
    assert count == 4

# Generated at 2022-06-13 15:57:20.892196
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def fail():
        raise ValueError('fail')
    def add_two(a, b):
        return a + b

    results = []

    for f in [lambda: 'a', lambda: 'b', fail, add_two]:
        e += f
        try:
            results.append(f())
        except Exception:
            pass

        e -= f

    e.fire()

    assert results == ['a', 'b', 12]

# Generated at 2022-06-13 15:57:25.391336
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class TestEventSource(_EventSource):
        pass

    class Foo:
        pass

    handler = Foo()
    evt = TestEventSource()
    assert handler not in evt._handlers

    # this is how the caller will use the code
    evt += handler
    assert handler in evt._handlers

    evt += handler
    assert len(evt._handlers) == 1



# Generated at 2022-06-13 15:57:31.073909
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventSource(metaclass=_EventSource):  # pylint: disable=function-redefined
        pass

    def on_event(a, b):
        return a + b

    def on_event_fail(a, b):
        raise ValueError(a + b)

    event_source = EventSource()
    event_source += on_event
    event_source += on_event_fail

    assert len(event_source._handlers) == 2

    event_source.fire(5, 10)
    with pytest.raises(ValueError):
        event_source.fire(5, 10)


# Generated at 2022-06-13 15:57:39.438606
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSource(_EventSource):
        def __init__(self):
            super(EventSource, self).__init__()

        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    event_source = EventSource()

    def callback(*args, **kwargs):
        return 42

    event_source += callback

    assert len(event_source._handlers) == 1

    a = [1, 2, 3]
    b = {'hello': 'world'}

    assert event_source.fire(a, b) is None

    event_source -= callback

    assert len(event_source._handlers) == 0



# Generated at 2022-06-13 15:57:45.766741
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.utils.collection_loader import _EventSource

    class _EventSourceTest(object):
        def __init__(self):
            self._fired = False

        def __call__(self, *args, **kwargs):
            self._fired = True

    event_source = _EventSource()

    handler = _EventSourceTest()
    event_source += handler
    assert not handler._fired

    event_source.fire()
    assert handler._fired


# Generated at 2022-06-13 15:57:52.408863
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    _call_count = 0

    _s = _EventSource()

    def _handler_one(*args, **kwargs):
        global _call_count
        _call_count += 1

    def _handler_two(*args, **kwargs):
        global _call_count
        _call_count += 1

    _s += _handler_one
    _s += _handler_two

    _s.fire()

    assert _call_count == 2

    _s -= _handler_one

    _s.fire()

    assert _call_count == 3



# Generated at 2022-06-13 15:58:00.009797
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def raise_exception(message):
        raise Exception(message)

    def receive_event(message):
        pass

    def receive_event2(message):
        pass

    # fire with no handler
    event_source = _EventSource()
    event_source.fire('this is a test')

    # fire with one handler
    event_source = _EventSource()
    event_source += receive_event
    event_source.fire('this is a test')

    # fire with one handler that raises an exception
    event_source = _EventSource()
    event_source += raise_exception
    try:
        event_source.fire('this is a test')
        assert False, 'an exception was expected'
    except Exception:
        pass

    # fire with two handlers and the first handler raises an exception
    event_source = _Event

# Generated at 2022-06-13 15:58:10.368597
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # The first parameter passed to a handler is the value passed to .fire().
    event_value = object()

    first_handler_called = False
    def first_handler(value):
        nonlocal first_handler_called
        assert value is event_value
        first_handler_called = True

    second_handler_called = False
    def second_handler(value):
        nonlocal second_handler_called
        assert value is event_value
        second_handler_called = True

    event_source += first_handler
    event_source += second_handler

    event_source.fire(event_value)

    assert first_handler_called is True
    assert second_handler_called is True

# Generated at 2022-06-13 15:58:52.400382
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    s = _EventSource()

    def f1(*args, **kwargs):
        pass

    def f2(*args, **kwargs):
        pass

    def f3(*args, **kwargs):
        raise ValueError('bad')

    s += f1
    s += f2
    s += f3
    s += f2

    s.fire(1, a=2)
    s.fire(1, a=2)
    s.fire(1, a=2)

    try:
        s.fire(1, a=2)
    except ValueError:
        pass
    except Exception as ex:
        raise AssertionError('expected ValueError, got %s' % ex.__class__.__name__)
    else:
        raise AssertionError('expected ValueError')

# Generated at 2022-06-13 15:58:59.464934
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import types
    import warnings

    def handler1(a, b, c, d):
        pass

    def handler2():
        raise RuntimeError('this is expected')

    def handler3(a):
        raise TypeError('I\'ve got a bad feeling')

    e = _EventSource()

    with warnings.catch_warnings(record=True) as w:
        e += 1

    assert type(w[-1].message) == DeprecationWarning
    assert str(w[-1].message) == 'the += operator for operator modules is deprecated'

    with warnings.catch_warnings(record=True) as w:
        e += []

    assert type(w[-1].message) == DeprecationWarning
    assert str(w[-1].message) == 'the += operator for operator modules is deprecated'

    e += handler