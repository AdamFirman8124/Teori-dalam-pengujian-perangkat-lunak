

# Generated at 2022-06-13 15:49:07.647988
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import pytest

    e = _EventSource()
    assert len(e._handlers) == 0

    # handler must be callable
    with pytest.raises(ValueError):
        e += 1

    # adding another callable handler should succeed
    def handler1(foo):
        pass
    e += handler1
    assert len(e._handlers) == 1



# Generated at 2022-06-13 15:49:12.696596
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # define listener
    def test_event_handler(event, source):
        #source.value = event.text
        print(event.text)

    # setup data
    event = 'unit test event'

    # setup test object
    event_source = _EventSource()

    # subscribe to event
    event_source += test_event_handler

    # fire event
    event_source.fire(event)

# Generated at 2022-06-13 15:49:15.941705
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    assert len(e._handlers) == 0

    def func():
        pass

    e += func
    assert len(e._handlers) == 1

    e += func
    assert len(e._handlers) == 1

# Generated at 2022-06-13 15:49:20.050124
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # given
    es = _EventSource()
    handler1 = lambda: None
    handler2 = lambda: None

    # when
    es += handler1
    es += handler2

    # then
    assert len(es._handlers) == 2
    assert handler1 in es._handlers
    assert handler2 in es._handlers



# Generated at 2022-06-13 15:49:21.210728
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _EventSource().__iadd__(None)


# Generated at 2022-06-13 15:49:26.705395
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from collections import namedtuple
    Event = namedtuple('Event', ['a', 'b'])
    events = []

    def handler1(event):
        events.append(event)

    def handler2(event):
        events.append(event)
        raise Exception('test')

    es = _EventSource()
    es += handler1
    es += handler2

    es.fire(Event(1, 2))

    assert len(events) == 2
    assert events[0].a == 1
    assert events[0].b == 2
    assert events[1].a == 1
    assert events[1].b == 2

# Generated at 2022-06-13 15:49:30.155557
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _val = []
    def _callback(x):
        _val.append(x)

    _es = _EventSource()
    _es += _callback
    _es.fire(1)
    assert _val == [1]

# Generated at 2022-06-13 15:49:33.393904
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    calls = []

    def handler_a(a, b, c):
        calls.append(('a', a, b, c))

    def handler_b(a, b, c):
        calls.append(('b', a, b, c))

    event_source += handler_a
    event_source += handler_b

    event_source.fire('a', 'b', 'c')
    assert calls == [('a', 'a', 'b', 'c'), ('b', 'a', 'b', 'c')]

# Generated at 2022-06-13 15:49:40.493916
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    target = _EventSource()

    class TestException(Exception):
        pass

    def test_handler(a, b, c):
        handler_called.append((a, b, c))

    def test_handler_raise(a, b, c):
        handler_called.append((a, b, c))
        raise TestException('test exception')

    def test_on_exception(handler, exc, a, b, c):
        on_exception_called.append((handler, exc, a, b, c))

    target._on_exception = test_on_exception
    target += test_handler
    target += test_handler_raise

    handler_called = []
    on_exception_called = []

# Generated at 2022-06-13 15:49:47.124404
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Given: an event handler function and an event source
    def handler(event_source, *args, **kwargs):
        if isinstance(args[0], RuntimeError):
            raise RuntimeError('ERROR')
        event_source._errors.append(args[0])

    event_source = EventSource()

    # When: we add the event handler to the event source
    event_source += handler

    # And: we fire the event source
    event_source.fire('event1')

    # Then: the event is recorded by the handler
    assert event_source._errors[0] == 'event1'

    # And: we fire the event source again
    event_source.fire('event2')

    # Then: the event is recorded by the handler again
    assert event_source._errors[1] == 'event2'

    # And: we

# Generated at 2022-06-13 15:49:54.179813
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event = _EventSource()
    event.fire = lambda : 0

    # test no handlers
    event.fire()

    # test a single handler
    event += lambda : 1
    assert event.fire()
    event -= lambda : 1

    # test two handlers
    event += lambda : 2
    event += lambda : 3
    assert event.fire()
    event -= lambda : 2
    event -= lambda : 3


# Generated at 2022-06-13 15:49:58.079925
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += lambda x: x
    assert len(e._handlers) == 1
    e += lambda x: x
    assert len(e._handlers) == 2


# Generated at 2022-06-13 15:50:02.488788
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Event:
        pass

    event = Event()

    fired = 0

    def handler(arg):
        assert arg is event
        nonlocal fired

        fired += 1

    cls = type('_EventSourceTest', (_EventSource,), {})

    evt = cls()
    evt += handler

    evt.fire(event)

    assert fired == 1



# Generated at 2022-06-13 15:50:10.535134
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            exceptions.append((handler, exc))
            return False

    # Test: no handlers
    events = MyEventSource()
    exceptions = []
    events.fire('a', 'b')
    assert not exceptions

    # Test: called once, no exceptions
    events = MyEventSource()
    exceptions = []
    events += lambda *args: None
    events.fire('a', 'b')
    assert not exceptions

    # Test: called once, with exception
    events = MyEventSource()
    exceptions = []
    events += lambda *args: raise_me()

# Generated at 2022-06-13 15:50:14.373597
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    obj = _EventSource()
    handler = lambda x: x + 1
    obj += handler  # should not raise

    try:
        obj += 'abc'
        raise AssertionError('expected ValueError not raised')
    except ValueError:
        pass



# Generated at 2022-06-13 15:50:19.076571
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    def foo():
        pass

    e += foo
    assert foo in e._handlers

    # Adding a non-callable should raise
    try:
        e += 'not a callable'
    except ValueError:
        pass
    else:
        assert False

    # Make sure foo is still there
    assert foo in e._handlers



# Generated at 2022-06-13 15:50:26.767607
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result = []
    esource = _EventSource()
    esource += lambda *args, **kwargs: result.append(('a', args, kwargs))
    esource += lambda *args, **kwargs: result.append(('b', args, kwargs))
    esource += lambda *args, **kwargs: result.append(('c', args, kwargs))
    esource.fire(1, 2, 3)
    assert result == [
        ('a', (1, 2, 3), {}),
        ('b', (1, 2, 3), {}),
        ('c', (1, 2, 3), {}),
    ]



# Generated at 2022-06-13 15:50:33.002782
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # event = _EventSource()
    # event += _print_args_kwargs
    # event += _print_args_kwargs
    # event.fire("test", "test")
    pass
#
# def _print_args_kwargs(*args, **kwargs):
#     print("args: {0}".format(args))
#     print("kwargs: {0}".format(kwargs))

# Generated at 2022-06-13 15:50:41.992347
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(message):
        errors.append("handler1 was executed")

    def handler2(message):
        errors.append("handler2 was executed")
        raise ValueError("handler2 exception")

    def handler3(message):
        errors.append("handler3 was executed")
        raise ValueError("handler3 exception")

    def on_exception(handler, exc, *args, **kwargs):
        errors.append("handler %s exception handler, message %s" % (handler, args[0]))

    errors = []
    event_source = _EventSource()
    event_source.fire(message="message_one")

    event_source += handler1
    event_source.fire(message="message_two")

    event_source += handler2
    event_source.fire(message="message_three")


# Generated at 2022-06-13 15:50:44.877799
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    m = _EventSource()
    assert m.fire() == None
    assert m.fire(1) == None
    assert m.fire(1, x=2) == None
    assert m.fire(1, 2, 3, z=4) == None



# Generated at 2022-06-13 15:50:58.033127
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def zero(x, y):
        raise ValueError

    def one(y, x):
        raise NameError

    def two(x, y):
        pass

    def on_exception(handler, exc, *args, **kwargs):
        assert isinstance(exc, ValueError)
        return False

    e = _EventSource()
    e._on_exception = on_exception

    e += zero
    e += one
    e += two

    # method one below should have raised a ValueError, but since on_exception returns False, the exception is omitted
    e.fire(1, 2)
    assert len(e._handlers) == 3

    del e

    e = _EventSource()
    e += zero
    e += one
    e += two

    # method one below should have raised a ValueError, but because

# Generated at 2022-06-13 15:51:10.331237
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # mock functions
    def mock_h1(*args, **kwargs):
        pass

    def mock_h2(*args, **kwargs):
        raise Exception('exception')

    def mock_on_exception(handler, exc):
        return False

    # set mock functions
    _EventSource._on_exception = mock_on_exception

    # fire method with empty handler
    e = _EventSource()
    e.fire()

    # fire method with one handler
    e = _EventSource()
    e += mock_h1
    e.fire()
    e -= mock_h1

    # fire method with two handlers
    e = _EventSource()
    e += mock_h1
    e += mock_h2
    e.fire()

    # fire method will raise an exception
    e = _EventSource()

# Generated at 2022-06-13 15:51:17.972244
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Foo:
        server = _EventSource()

    def handler_one(x, y):
        print(x + y)

    def handler_two(x, y):
        print(x - y)

    Foo.server += handler_one  # add handler
    assert handler_one in Foo.server._handlers

    Foo.server += handler_two  # add handler
    assert handler_one in Foo.server._handlers
    assert handler_two in Foo.server._handlers



# Generated at 2022-06-13 15:51:25.422323
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Test:
        def __init__(self):
            self.func_called = False

        def func(self, x):
            self.func_called = True
            self.x = x

    obj = Test()

    src = _EventSource()
    src += obj.func

    src.fire('foo')
    assert obj.func_called
    assert obj.x == 'foo'


# Generated at 2022-06-13 15:51:32.951394
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # test ValueError if not callable
    event = _EventSource()
    try:
        event += object()
    except ValueError:
        pass
    else:
        raise AssertionError('expected ValueError')

    # test expected behaivor if callable
    event += lambda: None
    assert len(event._handlers) == 1

    # test expected behaivor if multiple handlers
    event += lambda: None
    assert len(event._handlers) == 2

    # test expected behaivor if same handler added multiple times
    event += lambda: None
    assert len(event._handlers) == 2



# Generated at 2022-06-13 15:51:39.439556
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyHandler:
        def __init__(self, value):
            self.value = value

        def handler(self, *args, **kwargs):
            return self.value

    handler_name = MyHandler(5)
    handler_name2 = MyHandler(3)
    handler_name3 = MyHandler(1)
    handlers = AnsibleCollectionConfig.on_collection_load
    handlers += handler_name.handler

    assert handlers.fire() == 5

    handlers += handler_name2.handler
    handlers += handler_name3.handler

    assert handlers.fire() == 5

    handlers -= handler_name.handler
    assert handlers.fire() == 3

    handlers -= handler_name2.handler
    assert handlers.fire() == 1

    raise RuntimeError('test__EventSource_fire failed')

# Generated at 2022-06-13 15:51:43.026739
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    x = _EventSource()

    def dummy():
        pass

    x += dummy

    try:
        x += 1
        assert False, 'expected ValueError'
    except ValueError:
        pass



# Generated at 2022-06-13 15:51:52.149885
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(name, value):
        vars = locals()
        if 'expected' not in vars:
            raise ValueError('test handler not initialized')
        if vars['name'] != expected['name']:
            raise ValueError('name expected %s but was %s' % (expected['name'], vars['name']))
        if vars['value'] != expected['value']:
            raise ValueError('value expected %s but was %s' % (expected['value'], vars['value']))

    global expected
    expected = dict(name='expected name', value='expected value')
    source = _EventSource()
    source += handler
    try:
        source.fire(**expected)
    except ValueError as error:
        raise AssertionError('expected ValueError not raised: %s' % error)

# Generated at 2022-06-13 15:51:59.003918
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class test_class:
        def __init__(self):
            self.event_source = _EventSource()
            self.test_count = 0

        def test_fire(self):
            self.test_count = self.test_count + 1

    test_obj = test_class()
    test_obj.event_source += test_obj.test_fire
    test_obj.event_source.fire('test_param')


# Generated at 2022-06-13 15:52:04.109149
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    handlers = list(range(10))

    for handler in handlers:
        es += handler

    assert len(es._handlers) == 10

    for handler in handlers:
        es -= handler

    assert len(es._handlers) == 0



# Generated at 2022-06-13 15:52:13.265884
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def func1(*args, **kwargs):
        return 'func1'

    def func2(*args, **kwargs):
        return 'func2'

    event = _EventSource()

    event += func1
    event += func2

    assert event.fire() == ['func1', 'func2']

# Generated at 2022-06-13 15:52:17.887858
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert len(event_source._handlers) == 0

    def test_handler(arg1):
        return arg1

    event_source += test_handler
    assert len(event_source._handlers) == 1

    def test_handler_2(arg1):
        return arg1

    event_source += test_handler_2
    assert len(event_source._handlers) == 2

    assert not event_source._on_exception(None, None)


# Generated at 2022-06-13 15:52:21.358209
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Given: The class _EventSource has been defined in this module
    # When: When an instance of _EventSource is created
    event_source = _EventSource()

    # And: The method __iadd__ is called with a callable object
    event_source += lambda x: None

    # Then: The handler is added to the handlers set
    assert callable(list(event_source._handlers)[0])



# Generated at 2022-06-13 15:52:29.638269
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called = []

    def handler():
        called.append('handler')

    def handler2(ex):
        if ex is not None:
            called.append('handler2' + ex)

    def on_exception(handler, ex, *args, **kwargs):
        called.append('on_exception')
        return False

    es = _EventSource()
    es += handler
    es += handler2
    es._on_exception = on_exception

    es.fire()

    assert called == ['handler', 'handler2', 'handler2None', 'on_exception']



# Generated at 2022-06-13 15:52:36.282635
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _X:
        def __init__(self):
            self.flag = None

        def f(self):
            self.flag = True

        def g(self):
            self.flag = False
            raise ValueError('foo')

    s = _EventSource()

    x1, x2 = _X(), _X()

    s += x1.f
    s += x2.g

    s.fire()
    assert x1.flag
    assert not x2.flag

    x1.flag = x2.flag = None
    s -= x1.f
    s.fire()
    assert not x1.flag
    assert not x2.flag

    x1.flag = x2.flag = None

    s += x1.f
    s += x2.g


# Generated at 2022-06-13 15:52:46.437848
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # arrange
    handler_args = [False, False]

    def handler1(p1, p2):
        handler_args[0] = p1
        handler_args[1] = p2
        raise ValueError('my handler 1 exception')

    def handler2(p1, p2):
        handler_args[0] = p1
        handler_args[1] = p2
        raise ValueError('my handler 2 exception')

    def on_exception(handler, exc, p1, p2):
        handler_args[0] = p1
        handler_args[1] = p2
        return False

    source = _EventSource()
    source += handler1
    source += handler2
    source._on_exception = on_exception

    # act
    source.fire(True, True)

    # assert

# Generated at 2022-06-13 15:52:54.389562
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def f1(a1, a2):
        assert a1 == 'a1'
        assert a2 == 'a2'

    def f2(a1, a2):
        assert a1 == 'a1'
        assert a2 == 'a2'

    def f3(a1, a2):
        raise Exception('f3')

    def f4(a1, a2):
        raise Exception('f4')

    def f5(a1, a2):
        pass

    def f6(a1, a2):
        raise Exception('f6')

    def f7(a1, a2):
        pass

    def f8(a1, a2):
        raise Exception('f8')

    es = _EventSource()

    es += f1
    es += f2
    es += f3

# Generated at 2022-06-13 15:53:02.775870
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import MagicMock
    from ansible.module_utils.common.text.converters import to_bytes

    def _assert_add(obj, handler):
        obj += handler
        assert(handler in obj._handlers)

    def _get_handler():
        _handler = MagicMock()
        _handler.__call__ = MagicMock()
        return _handler

    handler = _get_handler()
    event_source = _EventSource()
    assert(not handler in event_source._handlers)
    # add the handler
    _assert_add(event_source, handler)
    # ignore adding the handler again
    _assert_add(event_source, handler)

    # confirm we can add a handler on different line
    _

# Generated at 2022-06-13 15:53:05.134972
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    eventsource = _EventSource()

    def handler1(param1, param2, param3):
        pass

    eventsource += handler1
    assert handler1 in eventsource._handlers



# Generated at 2022-06-13 15:53:17.889633
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSource(_EventSource):
        def __init__(self, fire_exception=None):
            super(EventSource, self).__init__()
            self._fire_exception = fire_exception

        def _on_exception(self, handler, exc, *args, **kwargs):
            return self._fire_exception

    fire_args = [1, 2]
    fire_kwargs = dict(a='a')

    # testing with no event handlers
    EventSource().fire(*fire_args, **fire_kwargs)

    # testing with a handler that does not raise
    def handler1(*args, **kwargs):
        for name in ('args', 'kwargs'):
            globals()[name] = globals()[name].copy()
        args.append(3)
        kwargs['b']

# Generated at 2022-06-13 15:53:38.807629
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    calls = [0] * 10
    expected_call_counts = [0] * 10

    # event handlers, one per index of calls.
    # each handler increments its call count and adds delivered args to a list
    def _event_handlers(_index, _args, _kwargs):
        calls[_index] += 1
        _args[_index].append((_index, calls[_index], _args, _kwargs))

    # set up the expected call count of each handler
    expected_call_counts[0] = 2
    expected_call_counts[1] = 1
    expected_call_counts[2] = 1
    expected_call_counts[3] = 1
    expected_call_counts[4] = 2
    expected_call_counts[5] = 1

# Generated at 2022-06-13 15:53:50.077872
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def f(a, b, c=3, d=4):
        x[:] = a, b, c, d

    def g(a, b, c=3, d=4):
        x[:] = a, b, c, d

    x = [None, None, None, None]
    event_source = _EventSource()
    event_source += f
    event_source += g
    event_source.fire(1, 2, d=4)
    assert x == [1, 2, 3, 4]

    try:
        event_source.fire(None, None)
    except TypeError:
        pass
    else:
        assert False, 'event_source.fire() should raise TypeError'

    # test on_exception

# Generated at 2022-06-13 15:53:53.443878
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    my_event_source = _EventSource()

    def my_handler(x):
        return x

    my_event_source += my_handler
    assert my_event_source.fire(1) == 1

# Generated at 2022-06-13 15:53:58.354188
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class _Target:
        def f1(self, x):
            self.x = x

    target = _Target()
    event_source = _EventSource()

    event_source += target.f1
    event_source.fire(x='abc')
    assert target.x == 'abc'

# Generated at 2022-06-13 15:54:03.579569
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    callable_value = 0

    def callable_method():
        nonlocal callable_value
        callable_value += 1

    eventsource = _EventSource()

    eventsource += callable_method
    eventsource.fire()
    assert callable_value == 1
    eventsource.fire()
    assert callable_value == 2

    eventsource -= callable_method
    eventsource.fire()
    assert callable_value == 2

# Generated at 2022-06-13 15:54:08.596102
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def foo(*a, **b):
        pass

    def bar(*a, **b):
        pass

    def error(*a, **b):
        raise Exception()

    es += foo
    es += bar

    es.fire('a', 'b')

    es -= foo

    es.fire('c', 'd')

    es += error

    try:
        es.fire('e', 'f')
        raise AssertionError()
    except Exception:
        pass  # expected


# Unit tests for class _AnsibleCollectionConfig

# Generated at 2022-06-13 15:54:12.241363
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def handler1(arg1, arg2, kwarg1='bar', kwarg2=None):
        assert arg1 == 'foo'
        assert arg2 == 'bar'
        assert kwarg1 == 'bar'
        assert kwarg2 is None

    def handler2(arg1, arg2, kwarg1='bar', kwarg2=None):
        assert arg1 == 'foo'
        assert arg2 == 'bar'
        assert kwarg1 == 'bar'
        assert kwarg2 is None

    es += handler1
    es += handler2

    es.fire('foo', 'bar', kwarg1='bar')

    es -= handler1
    es -= handler2



# Generated at 2022-06-13 15:54:22.655815
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Variables
    data = []
    fun = lambda x : data.append(x)
    fun2 = lambda x : data.append(x+1)
    # Test
    evt = _EventSource()
    evt += fun
    assert 1 == len(evt._handlers)
    assert fun in evt._handlers
    evt += fun2
    assert 2 == len(evt._handlers)
    assert fun2 in evt._handlers
    # Test invalid input
    with pytest.raises(ValueError):
        evt += 'test'
    # Test already present handler
    evt += fun
    assert 2 == len(evt._handlers)
    assert fun in evt._handlers


# Generated at 2022-06-13 15:54:28.985097
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible_collections.ansible.builtin.plugins.filter.core import to_nice_yaml

    test_obj = _EventSource()
    test_obj.fire(_)
    # TODO: In future of collections, we want to use the correct AnsibleFilterModule (https://github.com/ansible/ansible/issues/63368#issuecomment-590772414)
    test_obj += AnsibleFilterModule
    test_obj += to_nice_yaml
    test_obj.fire({"key": "value"})

# Generated at 2022-06-13 15:54:31.581459
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += lambda: None
    assert len(event_source._handlers) == 1, 'event handler was not added'


# Generated at 2022-06-13 15:54:55.114963
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass

# Generated at 2022-06-13 15:55:02.721248
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    l = _EventSource()

    l1 = 0
    l2 = 0
    l3 = 0

    def l1_handler(*args, **kwargs):
        nonlocal l1
        l1 += 1

    def l2_handler(*args, **kwargs):
        nonlocal l2
        l2 += 1

    def l3_handler(*args, **kwargs):
        nonlocal l3
        l3 += 1

    l += l1_handler
    l += l2_handler
    l += l3_handler

    l.fire()
    assert l1 == 1
    assert l2 == 1
    assert l3 == 1

    l2_handler()

    assert l1 == 1
    assert l2 == 2
    assert l3 == 1

# Generated at 2022-06-13 15:55:12.521628
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Fizz(Exception): pass
    class Buzz(Exception): pass

    class FooBar(object):
        def __init__(self, id):
            self.id = id

        def __call__(self, value):
            if value == 'fizz':
                raise Fizz(self.id)
            if value == 'buzz':
                raise Buzz(self.id)
            return self.id, value

        def __eq__(self, other):
            return self.id == other.id

    # test calling a handler
    event = _EventSource()
    handler = FooBar('foo')
    event += handler
    assert event.fire('bar') == ('foo', 'bar')

    # test calling two handlers
    event = _EventSource()
    event += FooBar('foo')
    event += FooBar('bar')
   

# Generated at 2022-06-13 15:55:17.652343
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert len(event_source._handlers) == 0

    def f():
        pass

    event_source += f
    assert len(event_source._handlers) == 1
    assert event_source._handlers.pop() is f


# Generated at 2022-06-13 15:55:21.034262
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    result = []

    def foo(x):
        result.append(x)

    event += foo
    event += foo

    event.fire('bar')

    assert result == ['bar', 'bar'], 'expected 2 calls to foo'


# Generated at 2022-06-13 15:55:33.509664
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(source, event):
        assert source is event_source
        assert event == 'event'

    def exception_handler(source, event, ex):
        assert source is event_source
        assert event == 'event'
        assert ex == 'exception'

    event_source = _EventSource()
    event_source += handler
    event_source.fire('event')

    event_source += exception_handler
    try:
        event_source.fire('event')
    except Exception as ex:
        assert ex == 'exception'
    else:
        assert False

    event_source -= handler
    event_source.fire('event')

    event_source -= exception_handler
    try:
        event_source.fire('event')
    except Exception as ex:
        assert ex == 'exception'

# Generated at 2022-06-13 15:55:44.008648
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    mock_handler_a = MockHandler(result=None)
    mock_handler_b = MockHandler(result=RuntimeError)
    mock_handler_c = MockHandler(result=ValueError)

    sut = _EventSource()
    sut += mock_handler_a.handler
    sut += mock_handler_b.handler
    sut += mock_handler_c.handler

    sut.fire(1, 2, a=3, b=4)

    assert mock_handler_a.invocations == [(1, 2, (3, 4))]
    assert mock_handler_b.invocations == [(1, 2, (3, 4))]
    assert mock_handler_c.invocations == [(1, 2, (3, 4))]


# Generated at 2022-06-13 15:55:52.829104
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(a, b, c):
        test.assertEqual(a, 1)
        test.assertEqual(b, 2)
        test.assertEqual(c, 3)

    def handler2(a, b, c):
        test.assertEqual(a, 1)
        test.assertEqual(b, 2)
        test.assertEqual(c, 3)

    def handler3(a, b, c):
        raise Exception('test exception')

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source += handler3
    with test.raises(Exception):
        event_source.fire(1, 2, 3)

    event_source -= handler3
    event_source.fire(1, 2, 3)

# Generated at 2022-06-13 15:56:00.190615
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    data = []
    def h1(value):
        data.append(value)
    event_source.fire(value='a')
    assert data == []
    event_source += h1
    event_source.fire(value='b')
    assert data == ['b']
    event_source -= h1
    event_source.fire(value='c')
    assert data == ['b']
    event_source -= h1
    event_source += h1
    event_source.fire(value='d')
    assert data == ['b', 'd']

# Generated at 2022-06-13 15:56:03.520745
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    handler = lambda *args, **kwargs: None
    assert handler not in event_source._handlers
    event_source += handler
    assert handler in event_source._handlers


# Generated at 2022-06-13 15:57:00.362481
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    calls = list()
    triggerer = _EventSource()

    def handler_A(exc):
        calls.append('A')

    def handler_B(exc):
        calls.append('B')
        raise RuntimeError('B')

    def handler_C(exc):
        calls.append('C')
        raise RuntimeError('C')

    def handler_D(exc):
        calls.append('D')
        raise RuntimeError('D')

    def handler_E(exc):
        calls.append('E')
        raise RuntimeError('E')

    triggerer += handler_A
    triggerer += handler_B
    triggerer += handler_C
    triggerer += handler_D
    triggerer.fire()
    assert calls == ['A', 'B', 'C', 'D']

    calls.clear()

# Generated at 2022-06-13 15:57:12.669988
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    result = []
    handler1 = lambda a: result.append('first: %s' % a)
    handler2 = lambda a: result.append('second: %s' % a)
    handler3 = lambda a: result.append('third: %s' % a)
    handler4 = lambda a: result.append('fourth: %s' % a)
    handler5 = lambda a: result.append('fifth: %s' % a)

    source += handler1
    source += handler2
    source += handler3
    source += handler4
    source += handler5

    # should call all handlers in the order they were added
    source.fire('one')
    assert result == ['first: one', 'second: one', 'third: one', 'fourth: one', 'fifth: one']

# Generated at 2022-06-13 15:57:14.017107
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler(arg):
        pass

    event = _EventSource()
    event += handler


# Generated at 2022-06-13 15:57:14.822831
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    raise NotImplementedError()


# Generated at 2022-06-13 15:57:23.541042
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    for f in (lambda: None,  # no argument
              lambda x: None,  # one argument
              lambda x, y, z: None):  # three arguments
        e = _EventSource()
        e += f
        assert e._handlers == {f}

    for f in (None,  # not callable
              'foo',  # string is not callable
              'foo'.__add__  # bound method is not callable
              ):
        e = _EventSource()
        try:
            e += f
        except ValueError:
            pass
        else:
            assert False, 'expected ValueError'


# Generated at 2022-06-13 15:57:26.598020
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import mock
    import pytest

    m = mock.Mock()

    e = _EventSource()
    e += m
    assert m in e._handlers

    with pytest.raises(ValueError):
        e += 'foo'



# Generated at 2022-06-13 15:57:30.785876
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def fail():
        raise Exception('test failure')

    es = _EventSource()

    es += fail

    try:
        es.fire()
    except Exception as e:
        assert e.args[0] == 'test failure'
    else:
        assert False  # expected exception not raised



# Generated at 2022-06-13 15:57:39.061696
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # GIVEN an event source
    es = _EventSource()

    # WHEN two handlers are added to the event source and one handler is called
    handler_one = object()
    handler_two = object()
    handler_one_called = False
    handler_two_called = False
    es += lambda: setattr(handler_one_called, 'handler_one_called', True)
    es += lambda: setattr(handler_two_called, 'handler_two_called', True)
    es.fire()

    # THEN both handlers should have been called
    assert(handler_one_called)
    assert(handler_two_called)

# Generated at 2022-06-13 15:57:42.169939
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    test_object = _EventSource()

    def _handler(x):
        pass

    # __iadd__ is the += operator
    test_object += _handler

    assert test_object._handlers == set([_handler])



# Generated at 2022-06-13 15:57:46.672300
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Foo:
        def __repr__(self):
            return 'Foo()'

    foo = Foo()
    event = _EventSource()

    event += foo
    assert event._handlers == {foo}

    event -= foo
    assert event._handlers == set()

