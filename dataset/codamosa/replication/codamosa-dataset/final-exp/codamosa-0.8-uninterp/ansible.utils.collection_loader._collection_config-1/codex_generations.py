

# Generated at 2022-06-13 15:49:06.601926
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert event_source._handlers == set()
    assert event_source == 1

    def handler():
        pass
    event_source += handler
    assert event_source._handlers == set([handler])



# Generated at 2022-06-13 15:49:16.060491
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class DummyEventSource(_EventSource):
        def __init__(self):
            super(DummyEventSource, self).__init__()
            self.on_exception_handler_invoked = False

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.on_exception_handler_invoked = True
            self.on_exception_handler = handler
            self.on_exception_exc = exc
            self.on_exception_args = args
            self.on_exception_kwargs = kwargs

    cm = DummyEventSource()
    cm += lambda: None
    cm.fire()

    def handle_exception(bad_arg):
        raise TypeError('bad arg: %s' % bad_arg)

    cm += handle_exception
    cm

# Generated at 2022-06-13 15:49:20.478771
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    class Handler:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True

    handler = Handler()
    evt += handler
    evt.fire()

    assert handler.called, '_EventSource.fire failed to invoke handler'


# Generated at 2022-06-13 15:49:23.168349
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def handler():
        pass

    e += handler

    assert handler in e._handlers

    e += handler

    assert len(e._handlers) == 1
    assert handler in e._handlers



# Generated at 2022-06-13 15:49:28.955437
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    def check_fire_1(a1, a2, kw1, kw2):
        assert a1 == 1
        assert a2 == 2
        assert kw1 == 3
        assert kw2 == 4

    event_source += check_fire_1

    class check_fire_2:
        def __init__(self, ev, a1, a2, kw1, kw2):
            self.ev = ev
            self.a1 = a1
            self.a2 = a2
            self.kw1 = kw1
            self.kw2 = kw2

        def __call__(self):
            assert self.a1 == 1
            assert self.a2 == 2
            assert self.kw1 == 3
            assert self.kw2 == 4
           

# Generated at 2022-06-13 15:49:32.886823
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e.__iadd__(lambda: None)
    e.__iadd__(lambda: None)
    e.__iadd__(lambda: None)
    e.__iadd__(lambda: None)

    assert len(e._handlers) == 4

    e.__iadd__('should fail')



# Generated at 2022-06-13 15:49:40.150202
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import collections
    import sys
    import types

    # create a class representing an event source
    class MyEvents(_EventSource):
        def __init__(self):
            super(MyEvents, self).__init__()
            self._on_exception = lambda h, e, *args, **kwargs: False

    # attach events and verify those events can fire without failure
    e = MyEvents()
    e += lambda: isinstance(e, MyEvents)
    e += lambda: isinstance(e, _EventSource)
    e += lambda: isinstance(e, collections.Callable)
    e += lambda: isinstance(e, (MyEvents, types.ModuleType))
    e += lambda: isinstance((lambda: None), collections.Callable)
    e.fire()

    # attach events and verify those events can fire with failure
    e

# Generated at 2022-06-13 15:49:46.893856
# Unit test for method fire of class _EventSource
def test__EventSource_fire():  # pragma: no cover
    from ansible.module_utils.common.collections import _EventSource
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.six import integer_types
    import textwrap

    class PrintEventSource(_EventSource):
        def fire(self, *args, **kwargs):
            return super(PrintEventSource, self).fire(args, kwargs)

    es = PrintEventSource()

    # event source with no registered event handlers

    es.fire(
        message=to_bytes('Hello'),
        num=20,
    )

    # event source with registered event handlers, no exception generation

    def print_handler(message, num):
        if isinstance(num, integer_types):
            print(message * num)


# Generated at 2022-06-13 15:49:51.281208
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    sentinel = object()
    value = object()
    e = _EventSource()

    def handler(arg):
        nonlocal value
        value = arg

    def failing_handler(arg):
        raise Exception()

    e += failing_handler
    e += failing_handler
    e += failing_handler
    e += handler

    assert e._handlers == {failing_handler, handler}

    e.fire(sentinel)

    assert e._handlers == {handler}
    assert value is sentinel

# Generated at 2022-06-13 15:50:00.419711
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Handler:
        pass

    event_source = _EventSource()

    handler1 = Handler()
    handler2 = Handler()
    handler3 = Handler()

    event_source += handler1
    event_source += handler2
    event_source += handler3

    assert handler1 in event_source._handlers
    assert handler2 in event_source._handlers
    assert handler3 in event_source._handlers

    try:
        event_source += object()
        assert False, 'Expected ValueError raised but not raised'
    except ValueError:
        pass


# Generated at 2022-06-13 15:50:15.214449
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # arrange
    def handler1(*args, **kwargs):
        handler1.called = True
        handler1.args = args
        handler1.kwargs = kwargs

    handler1.called = False

    def handler2(*args, **kwargs):
        handler2.called = True
        handler2.args = args
        handler2.kwargs = kwargs

    handler2.called = False

    my_event_source = _EventSource()
    my_event_source += handler1
    my_event_source += handler2

    # act
    my_event_source.fire("a", b="c")

    # assert
    assert handler1.called
    assert handler1.args == ("a",)
    assert handler1.kwargs == {"b": "c"}

    assert handler2.called
    assert handler2

# Generated at 2022-06-13 15:50:16.659413
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _EventSource().fire()


# Generated at 2022-06-13 15:50:21.176333
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def method_on_event_1(s):
        print("Event 1 args: %s" % s)

    def method_on_event_2(s):
        print("Event 2 args: %s" % s)

    es = _EventSource()
    es += method_on_event_1
    es += method_on_event_2

    test_args = "This is an event"
    es.fire(test_args)



# Generated at 2022-06-13 15:50:26.584692
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called = False

    def handler(x, y):
        nonlocal called
        assert x == 1
        assert y == 2
        called = True

    source = _EventSource()
    source += handler
    source.fire(1, y=2)
    assert called

# Generated at 2022-06-13 15:50:34.542674
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def foo(): raise ValueError('foo_exception')
    def bar(): pass

    event = _EventSource()
    events = []

    event += lambda: events.append('one')
    event += foo
    event += lambda: events.append('two')

    try:
        event.fire()
    except ValueError:
        # Expected because of foo()
        pass

    event += bar

    try:
        event.fire()
    except ValueError:
        # Unexpected because bar() should prevent re-raising
        assert False

    assert events == ['one', 'two']

# Generated at 2022-06-13 15:50:37.570102
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def f(a, b):
        print(a, b)

    x = _EventSource()
    x += f
    x.fire(1, 2)

# Generated at 2022-06-13 15:50:47.427184
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def error(x, y):
        raise ValueError('An error was reported')

    assert event_source.fire(1, 2) is None

    event_source += add
    event_source += subtract
    event_source += multiply
    event_source += divide
    assert event_source.fire(1, 2) is None

    event_source -= subtract
    try:
        event_source += error
        assert event_source.fire(1, 2) is None
    except ValueError:
        raise

# Generated at 2022-06-13 15:50:57.995685
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    mock_handler = MockEventHandler()
    es = _EventSource()
    es += mock_handler
    es.fire(1, 2, 3)
    print(mock_handler.event_args)
    print(mock_handler.event_kwargs)
    mock_handler_2 = MockEventHandler()
    es += mock_handler_2
    es.fire(1, 2, 3)
    print(mock_handler_2.event_args)
    print(mock_handler_2.event_kwargs)
    mock_handler_3 = MockEventHandler()
    es += mock_handler_3
    es.fire(1, 2, 3)
    print(mock_handler_3.event_args)
    print(mock_handler_3.event_kwargs)


# Generated at 2022-06-13 15:51:07.681455
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(name):
        assert name == 'hello'
        calls.append(handler1)

    def handler2(name):
        assert name == 'hello'
        calls.append(handler2)

    calls = []
    es = _EventSource()

    es += handler1
    es += handler2

    es.fire('hello')

    assert [handler1, handler2] == calls
    assert [handler1, handler2] == list(es._handlers)

    del calls[:]

    es -= handler1

    es.fire('hello')

    assert [handler2] == calls
    assert [handler2] == list(es._handlers)

# Generated at 2022-06-13 15:51:19.526965
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyException(Exception):
        pass

    def on_handler_exception(handler, exc, *args, **kwargs):
        if isinstance(exc, MyException):
            return False

        return True

    def handler_one(*args, **kwargs):
        print('handler_one: %s %s' % (args, kwargs))

    def handler_two(x):
        print('handler_two: %s' % x)

    def handler_three(x, y=None):
        print('handler_three: %s, %s' % (x, y))

    def handler_four(x, y=None):
        print('handler_four: %s, %s' % (x, y))
        raise MyException('exception in handler_four')

    ev = _EventSource()
    ev._on

# Generated at 2022-06-13 15:51:37.678594
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_handler1(value):
        assert value == 1

    def test_handler2(value):
        assert value == 2

    event_source = _EventSource()
    event_source += test_handler1
    event_source += test_handler2
    event_source.fire(1)
    event_source.fire(2)



# Generated at 2022-06-13 15:51:43.197388
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    source.fire()

    source += lambda *args, **kwargs: None
    source.fire()

    source += lambda *args, **kwargs: 1 / 0
    try:
        source.fire()
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError('ZeroDivisionError not raised')

# Generated at 2022-06-13 15:51:52.244237
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    class Handler:
        def __init__(self, f):
            self.f = f

        def __call__(self, *args, **kwargs):
            return self.f(*args, **kwargs)

    def handler1(*a, **kw):
        assert a[0] == 'a' and a[1] == 1 and kw['b'] == 2
        return 'ok1'

    def handler2(*a, **kw):
        assert a[0] == 'a' and a[1] == 1 and kw['b'] == 2
        raise TestException()

    def handler3(*a, **kw):
        assert a[0] == 'a' and a[1] == 1 and kw['b'] == 2
        return 'ok3'


# Generated at 2022-06-13 15:52:03.970850
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_a(*args, **kwargs):
        return args, kwargs

    def handler_b(*args, **kwargs):
        return args, kwargs

    handler_c = (lambda *args, **kwargs: (args, kwargs))

    event_source = _EventSource()
    event_source += handler_a
    event_source += handler_b
    event_source += handler_c

    def test(**kwargs):
        args = ('foo', 'bar')
        results = event_source.fire(*args, **kwargs)
        assert results == [(args, kwargs), (args, kwargs), (args, kwargs)]

    test(foo="bar", baz="qux")


# Generated at 2022-06-13 15:52:07.217193
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handle_event():
        return 'handle event'

    e = _EventSource()
    e += handle_event
    assert handle_event in e._handlers

    assert e.fire() == 'handle event'


# Generated at 2022-06-13 15:52:16.269899
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # test with no event handlers
    def test_no_handlers(state):
        cls = AnsibleCollectionConfig()
        cls.on_collection_load += foo

        cls.on_collection_load.fire(state)

        assert not state['fired']

    state = {'fired': False}
    test_no_handlers(state)
    assert state['fired'] == False

    # test with a single event handler
    def foo(state):
        state['fired'] = True
    def test_one_handler(state):
        state = {'fired': False}
        cls = AnsibleCollectionConfig()
        cls.on_collection_load += foo
        cls.on_collection_load.fire(state)
        assert state['fired']
    test_one_handler(state)

# Generated at 2022-06-13 15:52:22.879558
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    test_event_source = _EventSource()

    def bad_handler_1(*args, **kwargs):
        raise AttributeError()

    def bad_handler_2(*args, **kwargs):
        raise TestException()

    def good_handler_1(*args, **kwargs):
        return True

    def good_handler_2(*args, **kwargs):
        return False

    test_event_source += bad_handler_1
    test_event_source += bad_handler_2
    test_event_source += good_handler_1
    test_event_source += good_handler_2

    try:
        test_event_source.fire()
    except TestException:
        pass
    else:
        assert 0, "Did not raise exception"

    test_event_

# Generated at 2022-06-13 15:52:31.535523
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(name):
        raise Exception('failed to fire')

    def handler2(name, val=None):
        if name != 'foo':
            raise Exception('name != foo')
        if val != 1:
            raise Exception('val != 1')

    event = _EventSource()
    event += handler1
    event += handler2

    try:
        event.fire('name')
    except Exception as ex:
        if to_text(ex) != 'failed to fire':
            raise

    try:
        event.fire(name='foo', val=1)
    except Exception as ex:
        raise Exception('unexpected exception: %s' % to_text(ex))


# Generated at 2022-06-13 15:52:44.493862
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    class Foo:
        def __init__(self):
            self.event_invocations = 0

        def event_handler(self, *args, **kwargs):
            self.event_invocations += 1
            self.args = args
            self.kwargs = kwargs

    foo = Foo()
    event_source.fire('one', 'two')
    assert foo.event_invocations == 0

    event_source += foo.event_handler
    event_source.fire('a', 'b', x=1)
    assert foo.event_invocations == 1
    assert foo.args == ('a', 'b')
    assert foo.kwargs == dict(x=1)

    event_source -= foo.event_handler
    event_source.fire('x', 'y')

# Generated at 2022-06-13 15:52:49.936061
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # setup
    event = _EventSource()

    # assert
    assert event._handlers == set(), "The set of handlers should be empty"

    # Act
    event.fire("a", "b", "c")

    # Assert
    assert event._handlers == set(), "The set of handlers should still be empty"



# Generated at 2022-06-13 15:53:06.195928
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _FakeException(Exception):
        pass

    class _FakeArg(object):
        pass

    class _FakeKwarg(object):
        pass

    class _FakeHandler(object):
        def __init__(self):
            self.args = None
            self.kwargs = None
            self.exc = None

        def __call__(self, *args, **kwargs):
            self.exc = None
            self.args = args
            self.kwargs = kwargs
            raise _FakeException('this is not a real exception')

    event = _EventSource()

    h = _FakeHandler()
    event += h
    event += h
    event += h

    event.fire('test')
    assert len(h.args) == 1
    assert h.args[0] == 'test'

# Generated at 2022-06-13 15:53:16.009652
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_1(a, b=None):
        assert a == 1
        assert b == 2

    def handler_2(a, b=None):
        assert a == 3
        assert b == 4

    event = _EventSource()
    event += handler_1
    event += handler_2
    event.fire(1, b=2)
    event.fire(3, b=4)
    event -= handler_1
    event.fire(5, b=6)
    event -= handler_2
    event.fire(7, b=8)


# Generated at 2022-06-13 15:53:24.730384
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest:
        def __init__(self):
            self._value = 0
            self._num_fires = 0

        def __call__(self, *args, **kwargs):
            self._num_fires += 1
            self._value += 1

    t = EventSourceTest()
    s = _EventSource()

    ex = Exception("Testing")
    try:
        s.fire()
    except Exception:
        assert False, "no subscribers should not raise an exception"

    s += t
    s.fire()
    assert t._num_fires == 1

    try:
        s._on_exception(t, ex, 0)
        assert False, "exception not re-raised"
    except Exception as actual:
        assert actual is ex, "exception not re-raised"


# Generated at 2022-06-13 15:53:31.193022
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    cls = _EventSource()
    def f():
        pass
    def g():
        raise ValueError('event handler exception')

    cls += f
    cls += g

    try:
        cls.fire()
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ('event handler exception',)


# Generated at 2022-06-13 15:53:36.784835
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEvent:
        def __init__(self):
            self._called = False

        def __call__(self, *args, **kwargs):
            self._called = True

    e = _TestEvent()

    es = _EventSource()
    es += e

    assert not e._called
    es.fire()
    assert e._called
    e._called = False
    es.fire()
    assert e._called

# Generated at 2022-06-13 15:53:48.322744
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test with no handlers
    e = _EventSource()
    e.fire()

    # test with one handler and no exception
    def h():
        pass
    h_fired = [False]
    def h():
        h_fired[0] = True

    e += h
    e.fire()
    assert h_fired[0]

    # test with one handler and exception
    e = _EventSource()
    e += h
    try:
        e.fire('foo', 'bar', 'baz')
        assert False
    except ValueError:
        pass

    # test with multiple handlers and no exceptions
    e = _EventSource()
    handler_fired = [False, False, False]
    def h1():
        handler_fired[0] = True
    def h2():
        handler_fired[1] = True

# Generated at 2022-06-13 15:53:55.945385
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_call_counts = {}

    def test_handler1(*args, **kwargs):
        test_call_counts.setdefault('test_handler1', 0)
        test_call_counts['test_handler1'] += 1

    def test_handler2(*args, **kwargs):
        test_call_counts.setdefault('test_handler2', 0)
        test_call_counts['test_handler2'] += 1

    test_handler1.__name__ = 'test_handler1'
    test_handler2.__name__ = 'test_handler2'

    target = _EventSource()
    target += test_handler1
    target += test_handler2

    target.fire('a', 'b', 'c', d=1, e=2, f=3)


# Generated at 2022-06-13 15:53:58.404871
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(a, b, c):
        pass

    es = _EventSource()
    es += handler

    es.fire(1, 2, 3)

# Generated at 2022-06-13 15:54:01.234219
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    handler = _EventSource()
    def foo(*args, **kwargs):
        pass
    handler += foo
    handler.fire("hello")
    handler -= foo
    handler.fire("hello")

# Generated at 2022-06-13 15:54:08.186813
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self._fired = False
            self._exc = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._exc = None
            return True

        def run(self):
            self.fire()

        def handler(self):
            self._fired = True

    evt = _TestEventSource()
    evt += evt.handler

    evt.run()
    assert evt._fired is True
    assert evt._exc is None


# Generated at 2022-06-13 15:54:24.123968
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEvent:
        def __init__(self):
            self.event_fired = False

        def fire(self, *args, **kwargs):
            self.event_fired = True

    test_event = TestEvent()
    event_source = _EventSource()
    event_source += test_event.fire

    event_source.fire()

    assert test_event.event_fired is True



# Generated at 2022-06-13 15:54:32.878754
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSink:
        def __init__(self):
            self._events = []

        def __call__(self, *args, **kwargs):
            self._events.append((args, kwargs))

        @property
        def events(self):
            return self._events

    class _EventSource_Test(_EventSource):
        def __init__(self):
            super(_EventSource_Test, self).__init__()
            self._exception_count = 0

        def on_exception(self, exc):
            self._exception_count = self._exception_count + 1
            return True

    source = _EventSource_Test()
    sink = _EventSink()
    source += sink
    sink2 = _EventSink()

    source.fire('event1')

# Generated at 2022-06-13 15:54:43.316641
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(value):
        if value == 3:
            return value

    def handler2(value):
        if value == 2:
            raise ValueError('handler2')

    def handler3(value):
        if value == 2:
            raise ValueError('handler3')
        return value

    source = _EventSource()
    source += handler
    source += handler2
    source += handler3

    # no exceptions
    assert source.fire(1) is None
    assert source.fire(3) == 3

    # the exception thrown by the second handler is re-raised
    try:
        source.fire(2)
        assert False
    except Exception as e:
        assert 'handler2' in to_text(e)

    # reset the handlers
    source._handlers = set()

    # the first exception thrown is re-raised


# Generated at 2022-06-13 15:54:50.832892
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_state = {
        'called': False,
        'args': None,
        'kwargs': None,
    }

    def handler(x, y, z):
        test_state['called'] = True
        test_state['args'] = (x, y, z)
        test_state['kwargs'] = None

    def handler2(q, w, **kwargs):
        test_state['called'] = True
        test_state['args'] = None
        test_state['kwargs'] = (q, w, kwargs)

    event_source = _EventSource()

    event_source += handler
    event_source += handler2

    event_source.fire(1, 2, 3)
    assert test_state['called']
    assert test_state['args'] == (1, 2, 3)
   

# Generated at 2022-06-13 15:54:55.884807
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    trace = []
    def handler1(value):
        trace.append(value)
    def handler2(value):
        trace.append(value)
    event += handler1
    event += handler2
    event.fire('foobar')
    assert trace == ['foobar', 'foobar']


# Generated at 2022-06-13 15:55:03.941922
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result = []

    def handler1(*args, **kwargs):
        result.append((args, kwargs))

    def handler2(*args, **kwargs):
        result.append((args, kwargs))

    es = _EventSource()
    es.fire()
    assert not result

    es = _EventSource()
    es += handler1
    es.fire()
    assert result == [((), {})]

    es = _EventSource()
    es += handler1
    es += handler2
    es.fire()
    assert result == [((), {}), ((), {})]

    es = _EventSource()
    es += handler1
    es += handler1
    es.fire()
    assert result == [((), {}), ((), {})]

    es = _EventSource()
    es += handler1

# Generated at 2022-06-13 15:55:13.327425
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Asdf:
        def __init__(self):
            self.a = False
            self.b = False
            self.c = False

        def a_set(self):
            self.a = True

        def b_set(self):
            self.b = True

        def c_set(self):
            self.c = True

        def bad_event(self):
            raise Exception('BAD')

    asdf = Asdf()
    evt = _EventSource()

    evt += asdf.a_set
    evt += asdf.b_set
    evt += asdf.c_set
    evt.fire()

    assert asdf.a
    assert asdf.b
    assert asdf.c

    evt -= asdf.b_set

# Generated at 2022-06-13 15:55:23.035828
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    global e  # pylint: disable=global-statement,invalid-name

    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self.tx = 0

        def event(self, x):
            self.tx += x

    # pylint: disable=too-few-public-methods
    class MyHandler(object):
        def __init__(self, x):
            self.x = x

        def __call__(self, *args, **kwargs):
            e.tx += self.x

    e = MyEventSource()
    for i in range(5):
        e += MyHandler(i)
    e += e.event

    e.fire(5)
    assert e.tx == 20



# Generated at 2022-06-13 15:55:35.429795
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest
    es = _EventSource()
    event_handlers = []
    for x in range(0, 3):
        event_handlers.append([x, []])

    def event_handler_factory(index):
        def event_handler(*args):
            event_handlers[index][1].append(args)
        return event_handler

    for index, handler in enumerate(event_handlers):
        es += event_handler_factory(index)

    es.fire('arg1', 'arg2')
    # ensure that all the handlers were called
    for handler in event_handlers:
        assert len(handler[1]) == 1
        assert handler[1][0] == ('arg1', 'arg2')

    for index, handler in enumerate(event_handlers):
        es -= event_handler

# Generated at 2022-06-13 15:55:45.816852
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestFire(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            raise exc

    def test_handler1(name):
        if name != 'test':
            raise ValueError('expected name to be "test" but got {}'.format(name))

    def test_handler2(name):
        if name == 'test':
            raise ValueError('unexpected name "{}"'.format(name))

    t = TestFire()
    t += test_handler1
    t += test_handler2

    try:
        t.fire('test')
        raise AssertionError('expected event to raise an exception')
    except ValueError:
        pass



# Generated at 2022-06-13 15:56:12.748880
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # @ToDo: Write unit test
    pass

# Generated at 2022-06-13 15:56:17.107481
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def handler1(*args, **kwargs):
        return 1

    def handler2(*args, **kwargs):
        return 2

    event += handler1
    event += handler2

    assert event.fire() == []

# Generated at 2022-06-13 15:56:26.847419
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1():
        raise RuntimeError()

    def handler2():
        raise Exception()

    def handler3():
        pass

    def handler4():
        raise ValueError()

    source = _EventSource()
    source += handler1
    source += handler2
    source += handler3
    source += handler4

    with pytest.raises(RuntimeError):
        source.fire()

    source = _EventSource()
    source += handler1
    source += handler2
    source += handler4

    with pytest.raises(ValueError):
        source.fire()

    source = _EventSource()
    source += handler1
    source += handler2
    source += handler3

    source.fire()

## class _CollectionInfo
#
#  A class which describes the location, validation and inspection of a collection
#

# Generated at 2022-06-13 15:56:32.129275
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    source += lambda: None
    source += lambda: raise_exception()
    source += lambda: None

    assert len(source._handlers) == 3

    source.fire()

    assert len(source._handlers) == 2



# Generated at 2022-06-13 15:56:37.665905
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    x = _EventSource()

    a = []

    def z1(n):
        a.append(n)

    x += z1

    x.fire(1)
    x.fire(2)

    assert a == [1, 2]

    def z2(n):
        a.append(n)

    x += z2

    x.fire(3)
    x.fire(4)

    assert a == [1, 2, 3, 4, 3, 4]


# Generated at 2022-06-13 15:56:45.821238
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # no callable handler
    event_source = _EventSource()

    try:
        # The following "fire" method call should not raise an exception.
        event_source.fire()
    except Exception as e:
        assert False, "An exception was raised: " + to_text(e)

    # handler raises exception
    handler_ran = False
    event_source = _EventSource()
    event_source += lambda: 1/0

    try:
        event_source.fire()
        assert False, "Expecting an exception. None was raised."
    except ZeroDivisionError as e:
        # This is the exception we want to see
        handler_ran = True
    except Exception as e:
        assert False, "Unexpected exception was raised: " + to_text(e)


# Generated at 2022-06-13 15:56:57.284487
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestException(Exception):
        pass

    class AssertException(Exception):
        pass

    def handler(a, b, c=None, d=None):
        assert a == 1, AssertException("a != 1")
        assert b == 2, AssertException("b != 2")
        assert c == 3, AssertException("c != 3")
        assert d == 'foo', AssertException("d != 'foo'")
        raise TestException("error")

    event = _EventSource()
    event += handler

    try:
        event.fire(1, 2, c=3, d='foo')
    except Exception:
        pass
    else:
        raise AssertException("_EventSource.fire() did not raise exception")

    event -= handler


# Generated at 2022-06-13 15:56:58.799461
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    raise NotImplementedError('Test for fire of class _EventSource needs to be implemented')


# Generated at 2022-06-13 15:57:05.313095
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class ExpectedError(Exception):
        pass

    class UnexpectedError(Exception):
        pass

    # this handler must be called exactly once
    def test_handler_ok():
        test_handler_ok.counter += 1
        if test_handler_ok.counter != 1:
            raise UnexpectedError("test_handler_ok called more than once")

    test_handler_ok.counter = 0

    # this handler must not be called
    def test_handler_not_called():
        raise UnexpectedError("test_handler_not_called was called")

    # this handler must throw an exception which is not caught by the handler that invokes it
    def test_handler_error():
        raise ExpectedError()

    # this handler must throw an exception which is caught by the handler that invokes it

# Generated at 2022-06-13 15:57:14.885619
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSourceSubclass(_EventSource):
        def __init__(self, *args, **kwargs):
            super(_EventSourceSubclass, self).__init__(*args, **kwargs)
            self._on_exception_call_count = 0

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._on_exception_call_count += 1
            return True

    class _EventHandler:
        def __init__(self, *args, **kwargs):
            self.handle_call_count = 0
            self.handle_args_list = []
            self.handle_kwargs_dict = []

        def __call__(self, *args, **kwargs):
            self.handle_call_count += 1

# Generated at 2022-06-13 15:58:13.056873
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    def handler(x):
        raise Exception('exception')

    source += handler

    try:
        source.fire()
    except Exception:
        pass
    finally:
        assert source._handlers == set()


# Generated at 2022-06-13 15:58:16.527363
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def handler_1(ex):
        raise ValueError()

    def handler_2(ex):
        raise TypeError()

    es += handler_1
    es += handler_2
    fired = False
    try:
        es.fire()
    except ValueError as exc:
        fired = True

    assert fired



# Generated at 2022-06-13 15:58:26.902760
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    counter = [0]

    def handler1(val):
        counter[0] += val

    def handler2(val):
        counter[0] -= val

    event += handler1
    event += handler2

    event.fire(3)
    assert counter[0] == 0

    event -= handler2
    event.fire(3)
    assert counter[0] == 3

    event -= handler1
    event.fire(3)
    assert counter[0] == 3

    # Now, use the event object to simulate our AnsibleCollectionConfig.on_collection_load
    event = AnsibleCollectionConfig.on_collection_load  # pylint: disable=no-member
    counter = [0]

    def handler1(val):
        counter[0] += val


# Generated at 2022-06-13 15:58:33.655937
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(msg, num):
        print('handler1: %s %s' % (msg, num))

    def handler2(msg, num):
        print('handler2: %s %s' % (msg, num))

    es = _EventSource()
    es += handler1
    es += handler2

    es.fire('hello', '1')

    es -= handler1

    es.fire('hello', '2')



# Generated at 2022-06-13 15:58:40.915820
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class DummyEventSource(_EventSource):
        def __init__(self):
            self._exceptions = []
            super(DummyEventSource, self).__init__()

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._exceptions.append((handler, exc, args, kwargs))
            return False

    source = DummyEventSource()

    num_callbacks = 3
    callback_values = []
    for i in range(0, num_callbacks):
        def callback(x):
            callback_values.append(x)
        source += callback

    # fire all callbacks and capture return values
    source.fire(1)

    assert set(callback_values) == {1}
    assert source._exceptions == []

    callback_values = []

# Generated at 2022-06-13 15:58:50.335832
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    class Test:
        def __init__(self):
            self.count = 0

        def on_load(self, path):
            assert path == 'some/path'
            self.count += 1

    test = Test()
    event_source = _EventSource()
    assert test.count == 0

    event_source += test.on_load
    event_source.fire('some/path')
    assert test.count == 1

    event_source -= test.on_load
    event_source.fire('some/path')
    assert test.count == 1

    event_source += test.on_load
    event_source += test.on_load
    event_source.fire('some/path')
    assert test.count == 3

    def handler(path):
        assert path == 'some/path'


# Generated at 2022-06-13 15:58:57.423955
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSourceTestHarness(object):
        def __init__(self):
            self.re_raise = False

        def fire_handler1(self, *args, **kwargs):
            self.handler1_args = args
            self.handler1_kwargs = kwargs

        def fire_handler2(self, *args, **kwargs):
            self.handler2_args = args
            self.handler2_kwargs = kwargs
            raise Exception('this is expected')

        def fire_handler3(self, *args, **kwargs):
            self.handler3_args = args
            self.handler3_kwargs = kwargs
            raise Exception('this is expected')

        def fire_on_exception(self, handler, exc, *args, **kwargs):
            return self.re_raise



# Generated at 2022-06-13 15:59:07.334636
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    evt = []

    def f1(*args):
        evt.append(args)

    def f2(*args):
        evt.append(args)
        raise Exception("Hello")

    def f3(*args):
        evt.append(args)
        raise Exception("World")

    es += f1
    es += f2
    es += f3

    es.fire(1, 2)

    assert len(evt) == 3

    assert evt[0] == (1, 2)
    assert evt[1] == (1, 2)
    assert evt[2] == (1, 2)

    es -= f2
    es -= f3

    es.fire(3, 4)

    assert len(evt) == 4
