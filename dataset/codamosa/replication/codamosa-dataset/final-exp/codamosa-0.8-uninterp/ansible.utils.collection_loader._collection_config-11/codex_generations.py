

# Generated at 2022-06-13 15:49:02.807998
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    event += print
    event += print
    assert len(event._handlers) == 1


# Generated at 2022-06-13 15:49:07.044129
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    events_fired = []

    def handler(arg):
        events_fired.append(arg)

    event_source += handler

    event_source.fire('Hello')
    event_source.fire('World')

    assert events_fired == ['Hello', 'World']



# Generated at 2022-06-13 15:49:16.441388
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Inject:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def register(self, event_source):
            for name, value in self.kwargs.items():
                event_source += getattr(self, name)
                setattr(self, name, value)

    def _func(value):
        pass

    inject = Inject(func=_func)

    event_source = _EventSource()

    event_source.on_exception = inject.register
    inject.on_exception = True

    with inject.func as func:
        func.return_value = (True, False)[False]

        try:
            event_source.fire(None)
            assert False, "Should have raised an exception"
        except Exception:
            pass

        func.return_value

# Generated at 2022-06-13 15:49:23.653386
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_passed = True

    class _EventArgs:
        def __init__(self, msg):
            self.msg = msg

    event = _EventSource()

    def handler_one(arg):
        print("Handler_one: %s" % arg.msg)

    def handler_two(arg):
        print("Handler: %s" % arg.msg)

    event += handler_one
    event.fire(_EventArgs("arg1"))

    print("\nTrying to fire more than one event at a time")
    event += handler_two
    event.fire(_EventArgs("arg1"), _EventArgs("arg2"))

    return test_passed


# Generated at 2022-06-13 15:49:31.307570
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _EventSource_fire = _EventSource.fire.__func__
    event = _EventSource()

    def handler_1(*args, **kwargs):
        args_copy = args
        kwargs_copy = kwargs
        return args_copy, kwargs_copy

    event += handler_1

    args = (1, 2, 3)
    kwargs = {'a': 'b', 'c': 'd'}
    (returned_args, returned_kwargs) = _EventSource_fire(event, *args, **kwargs)
    assert ((returned_args, returned_kwargs), (args, kwargs))

# Generated at 2022-06-13 15:49:36.028022
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def assert_fired(cnt):
        assert fired == cnt

    a = _EventSource()

    fired = 0

    a += (lambda: assert_fired(0))
    a += (lambda: assert_fired(1))
    a += (lambda: assert_fired(2))

    a.fire()

    a -= (lambda: assert_fired(0))

    a.fire()

    a -= (lambda: assert_fired(1))

    a.fire()

# Generated at 2022-06-13 15:49:40.326423
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    value = [0]

    def handler1(*args, **kwargs):
        value[0] += 1

    def handler2(*args, **kwargs):
        value[0] += 2

    event_source += handler1
    event_source += handler2

    event_source.fire()
    assert value == [3], value

    event_source -= handler1
    event_source.fire()
    assert value == [5], value



# Generated at 2022-06-13 15:49:47.012105
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # We will fire the event and expect the handler to be called.
    event = _EventSource()
    called = False

    def handler():
        nonlocal called
        called = True

    event += handler
    event.fire()

    assert called

    # If a handler raises an exception it must be relayed back to the caller.
    called2 = False

    def handler2():
        nonlocal called
        called = True
        raise Exception('test')

    event = _EventSource()
    event += handler2
    called = False
    try:
        event.fire()
        assert False, 'Expected exception'
    except:
        pass

    assert not called

    # If a handler raises an exception, on_exception can prevent the exception from being relayed to the caller.
    def handler3():
        nonlocal called
        called = True
       

# Generated at 2022-06-13 15:49:52.896809
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyFixture:
        def __init__(self):
            self.events = list()
            self.event = AnsibleCollectionConfig.on_collection_load
            self.event += self.on_event

        def on_event(self, *args, **kwargs):
            self.events.append((args, kwargs))

    fx = MyFixture()
    fx.event.fire(1)

    assert len(fx.events) == 1
    assert fx.events[0][0] == (1,)
    assert fx.events[0][1] == {}

    fx.event.fire(1, a=1, b=2)

    assert len(fx.events) == 2
    assert fx.events[1][0] == (1,)
    assert fx.events[1][1]

# Generated at 2022-06-13 15:50:00.078076
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def h1(*args, **kwargs):
        pass

    e += h1
    assert h1 in e._handlers

    e.add(h1)
    assert h1 in e._handlers

    e += h1  # duplicate is not a problem

    def h2(*args, **kwargs):
        pass

    e += h2
    assert h2 in e._handlers



# Generated at 2022-06-13 15:50:15.457554
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()

    # if handler is not callable
    try:
        event_source += None
    except Exception as ex:
        if type(ex) != ValueError:
            raise ex
        pass
    else:
        raise AssertionError('When handler is not callable, _EventSource.__iadd__ should raise an exception')

    event_source += handler

    if handler not in event_source._handlers:
        raise AssertionError('When handler is callable, _EventSource.__iadd__ should add handler to _handlers')

test__EventSource___iadd__()


# Generated at 2022-06-13 15:50:26.021139
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self, on_exception):
            super(_TestEventSource, self).__init__()
            self.on_exception = on_exception

        def _on_exception(self, handler, exc, *args, **kwargs):
            return self.on_exception(handler, exc, *args, **kwargs)

    event_source = _TestEventSource(lambda h, e, *a, **k: False)

    handler_count = 10
    handler_arguments = {
        'args': ('a1', 'a2'),
        'kwargs': {'k1': 1, 'k2': 2}
    }

    def handler(*args, **kwargs):
        if args != handler_arguments['args']:
            raise AssertionError

# Generated at 2022-06-13 15:50:30.170814
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(*args, **kwargs):
        pass

    event_source = _EventSource()
    event_source.fire()
    event_source += handler
    event_source.fire()
    event_source -= handler
    event_source.fire()


# Generated at 2022-06-13 15:50:36.825089
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler1():
        pass

    def handler2():
        pass

    ES = _EventSource()
    ES += handler1
    assert handler1 in ES._handlers
    ES += handler2
    assert handler2 in ES._handlers

    # duplicate handlers aren't an error
    ES += handler1
    assert handler1 in ES._handlers
    assert handler2 in ES._handlers

    # check that non-callables raise error
    try:
        ES += 1
    except ValueError as e:
        assert 'handler must be callable' in str(e)
    else:
        assert False



# Generated at 2022-06-13 15:50:46.906647
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest:
        def __init__(self):
            self._was_fired = False

        def __call__(self, *args, **kwargs):
            self._was_fired = True

        @property
        def was_fired(self):
            return self._was_fired

    t1 = EventSourceTest()
    t2 = EventSourceTest()

    # sanity check
    assert not t1.was_fired
    assert not t2.was_fired

    # creation of the EventSource should not fire the handlers
    es = _EventSource()
    assert not t1.was_fired
    assert not t2.was_fired

    # firing an empty EventSource should not fire the handlers
    es.fire()
    assert not t1.was_fired
    assert not t2.was_fired

    # adding a handler

# Generated at 2022-06-13 15:50:54.802759
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventSourceTest:
        def __init__(self):
            self.on_collection_load = _EventSource()

    eventsource_test = EventSourceTest()
    eventsource_test.on_collection_load += lambda x: True
    assert len(eventsource_test.on_collection_load._handlers) == 1
    eventsource_test.on_collection_load += lambda x: True
    assert len(eventsource_test.on_collection_load._handlers) == 2


# Generated at 2022-06-13 15:51:00.061053
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()

    # Non-callable handler.
    try:
        source += 0
        assert False, 'expected ValueError'
    except ValueError:
        pass

    # Callable handler.
    handler_1 = lambda: None
    source += handler_1
    try:
        source._on_exception = lambda handler, exc, *args, **kwargs: False
        source.fire('test1', test2='test2')
    except Exception:
        assert False, 'unexpected exception'


# Generated at 2022-06-13 15:51:12.098303
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest
    test_data = list(range(3))

    def handler(*args, **kwargs):
        assert len(args) == 1
        assert args[0] == 'test'
        assert not kwargs
        test_data[0] += 1

    def handler_exception(*args, **kwargs):
        raise NotImplementedError()

    def handler_reraise(*args, **kwargs):
        raise OSError()

    def handler_ignore(*args, **kwargs):
        raise OSError()

    def handler_1(*args, **kwargs):
        test_data[1] += 1

    def handler_2(*args, **kwargs):
        test_data[2] += 1

    es = _EventSource()

    es += handler_1
    es += handler_2



# Generated at 2022-06-13 15:51:14.523843
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert len(es._handlers) == 0

    def h1():
        pass

    es += h1
    assert len(es._handlers) == 1
    assert h1 in es._handlers



# Generated at 2022-06-13 15:51:16.245012
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()

    event_source += handler

    assert handler in event_source._handlers


# Generated at 2022-06-13 15:51:34.343160
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Test:
        def __init__(self):
            self.num_events = 0

        def handler(self, data):
            self.num_events += 1

        def handler_exception(self, data):
            raise Exception('unexpected exception')

    event_source = _EventSource()
    test_instance = Test()

    event_source += test_instance.handler
    event_source += test_instance.handler_exception

    event_source.fire('data')
    assert test_instance.num_events == 1


# Generated at 2022-06-13 15:51:43.303249
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def foo(x, y):
        foo.called = True
        foo.x = x
        foo.y = y

    def bar(x, y):
        bar.called = True
        bar.x = x
        bar.y = y

    es = _EventSource()
    es += foo
    es += bar

    event = 'blah'
    es.fire(event)

    assert foo.called
    assert foo.x == event
    assert foo.y == {}
    assert bar.called
    assert bar.x == event
    assert bar.y == {}

# Generated at 2022-06-13 15:51:52.338279
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def increment(count):
        count[0] += 1

    def raise_exception(count):
        count[0] += 1
        raise ValueError('error')

    count = [0]

    event = _EventSource()
    event += increment
    event += raise_exception
    event += increment
    event += increment

    # ensure all handlers are called, but the exception is not passed through
    event.fire(count)
    assert count[0] == 4
    assert len(event._handlers) == 4

    # remove a handler, ensure it is not called again
    event -= increment
    event.fire(count)
    assert count[0] == 6
    assert len(event._handlers) == 3

    # replace the raise_exception handler and ensure the exception passes through
    def raise_exception(count):
        raise

# Generated at 2022-06-13 15:51:58.271311
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(a, b):
        raise RuntimeError('i am handler 1')

    def handler2(a, b, c=None):
        raise RuntimeError('i am handler 2')

    def handler3(a, b):
        raise RuntimeError('i am handler 3')

    on_collection_load = _EventSource()

    on_collection_load += handler1
    on_collection_load += handler2
    on_collection_load += handler3

    raised = False

    try:
        on_collection_load.fire(1, 2, 3)
    except RuntimeError as e:
        raised = e
        assert e.args[0] == 'i am handler 3'

    assert raised

    raised = False

# Generated at 2022-06-13 15:52:08.244540
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    handler_counter = {'counter': 0}

    def handler(*args, **kwargs):
        handler_counter['counter'] += 1

    event = _EventSource()

    event += handler
    event.fire()
    assert handler_counter['counter'] == 1

    try:
        event += None
        assert False, 'adding non-callable to EventSource failed to raise ValueError'
    except ValueError:
        pass

    # handler should be added, not just raised
    handler_counter['counter'] = 0
    try:
        event += object()
        assert False, 'adding non-callable to EventSource failed to raise ValueError'
    except ValueError:
        pass
    assert handler_counter['counter'] == 0

    handler_counter['counter'] = 0
    event.fire()
    assert handler_counter['counter'] == 1



# Generated at 2022-06-13 15:52:08.808016
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _EventSource()

# Generated at 2022-06-13 15:52:13.813631
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    calls = 0
    def handler1(self, *args, **kwargs):
        nonlocal calls
        calls += 1

    def handler2(self, *args, **kwargs):
        nonlocal args, kwargs
        args = []
        kwargs = {}

    source = _EventSource()
    source += handler1
    source += handler2
    source.fire()
    assert calls == 1
    assert args == [] and kwargs == {}

# Generated at 2022-06-13 15:52:20.117118
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def foo():
        pass

    def bar():
        pass

    events = _EventSource()

    assert not foo in events._handlers
    assert not bar in events._handlers

    events += foo
    assert foo in events._handlers
    assert not bar in events._handlers

    events += bar
    assert foo in events._handlers
    assert bar in events._handlers

    events = _EventSource()
    events += foo
    events += bar
    assert foo in events._handlers
    assert bar in events._handlers



# Generated at 2022-06-13 15:52:30.533265
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import sys

    es = _EventSource()

    class ThrowingHandler:
        def myhandler(self, x):
            if x:
                raise RuntimeError('foo')

    def abc_(x):
        if x:
            raise ValueError('bar')

    def def_():
        raise TypeError('baz')

    es += abc_
    es += abc_
    es -= abc_

    th = ThrowingHandler()
    es += th.myhandler
    es += th.myhandler
    es -= th.myhandler

    es += def_
    es += def_
    es -= def_

    try:
        es.fire(1)
        assert 0
    except ValueError as ex:
        assert str(ex) == 'bar'

# Generated at 2022-06-13 15:52:43.155665
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    assert 0 == len(event._handlers)

    def handler_1(*args, **kwargs):
        pass

    event += handler_1
    assert 1 == len(event._handlers)
    assert handler_1 == event._handlers.pop()
    assert 0 == len(event._handlers)

    try:
        event += None
        assert False, 'Expected ValueError from event += None'
    except ValueError:
        pass

    try:
        event += 10
        assert False, 'Expected ValueError from event += 10'
    except ValueError:
        pass

    try:
        event += 'foo'
        assert False, 'Expected ValueError from event += "foo"'
    except ValueError:
        pass

    def handler_2(*args, **kwargs):
        raise Value

# Generated at 2022-06-13 15:53:19.348746
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    assert __name__ == '__main__.test_collection_loader'
    es = _EventSource()
    es += test__EventSource___iadd__

    def handler2(arg1, arg2):
        pass

    es += handler2
    assert len(es._handlers) == 2
    assert test__EventSource___iadd__ in es._handlers
    assert handler2 in es._handlers

    es += handler2
    assert len(es._handlers) == 2



# Generated at 2022-06-13 15:53:20.979816
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda x: print('test')



# Generated at 2022-06-13 15:53:26.366050
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    result = False

    def handler_one(*args, **kwargs):
        return

    def handler_two(*args, **kwargs):
        nonlocal result
        result = True
        return

    event += handler_one
    event += handler_two

    assert result is False
    event.fire()
    assert result is True

# Generated at 2022-06-13 15:53:29.240315
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    value = event_source.__iadd__(lambda x: x)
    assert value is event_source


# Generated at 2022-06-13 15:53:37.658413
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    class TestException(Exception):
        pass

    # define a handler which raises TestException
    def handler_one(data):
        raise TestException(data)

    # define a handler which will be passed an exception
    handler_two_exception = None
    def handler_two(data, ex):
        nonlocal handler_two_exception
        handler_two_exception = ex

    # define a handler which returns False for on_exception
    def handler_three(data):
        raise Exception('this handler will raise an exception but a return value of False from on_exception will stop re-raise')

    # define a handler which returns True for on_exception

# Generated at 2022-06-13 15:53:49.259239
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def callable1(o_self, *args, **kwargs):
        self1.fire_count += 1
        if kwargs.get('exc') is not None:
            self1.event_exceptions.append(kwargs['exc'])
        elif kwargs.get('success') is not None:
            self1.event_success = kwargs['success']
        else:
            self1.event_args = args

    def callable2(o_self, *args, **kwargs):
        self2.fire_count += 1
        if kwargs.get('exc') is not None:
            self2.event_exceptions.append(kwargs['exc'])
        elif kwargs.get('success') is not None:
            self2.event_

# Generated at 2022-06-13 15:54:00.759580
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from unittest import TestCase

    class TestEventSource(TestCase):
        def test_exception_propagation(self):
            sources = [
                _EventSource(),
            ]

            for source in sources:
                source += lambda : 1 / 0  # bang!

                with self.assertRaises(ZeroDivisionError):
                    source.fire()

        def test_multiple_error_handlers(self):
            sources = [
                _EventSource(),
            ]

            for source in sources:
                source += lambda: 1 / 0  # bang!
                source += lambda: 1 / 0  # bang!

                with self.assertRaises(ZeroDivisionError):
                    source.fire()

        def test_error_handler(self):
            calls = []
            raised = [False]


# Generated at 2022-06-13 15:54:08.969769
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from _ast import Try
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    event_source = _EventSource()
    mock = Mock()

    # Test adding handler
    event_source += mock
    assert mock in event_source._handlers

    # Test removing handler that is not there
    event_source -= mock
    assert mock not in event_source._handlers

    # Test firing event handlers
    event_source += mock
    event_source.fire()
    mock.assert_called_once_with()

    # Test raising unhandled exception in event handler
    mock.reset_mock()
    event_source += mock
    mock.side_effect = RuntimeError
    try:
        event_source.fire()
    except RuntimeError:
        pass

# Generated at 2022-06-13 15:54:11.345946
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _eventsource = _EventSource()
    _eventsource += lambda: None


# Generated at 2022-06-13 15:54:13.515051
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    src = _EventSource()
    handler = lambda: True
    src += handler
    assert handler in src._handlers


# Generated at 2022-06-13 15:54:49.638394
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    counter = [0]

    def handler(*args, **kwargs):
        counter[0] += 1
        handler.args.append(args)
        handler.kwargs.append(kwargs)

    handler.args = []
    handler.kwargs = []

    source = _EventSource()
    source += handler

    source.fire(1, 2, a=3, b=4)
    source.fire(5, 6, a=7, b=8)

    assert counter[0] == 2
    assert handler.args == [(1, 2), (5, 6)]
    assert handler.kwargs == [dict(a=3, b=4), dict(a=7, b=8)]

# Generated at 2022-06-13 15:54:59.651058
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # No exception raised
    eventsource = _EventSource()
    eventsource += lambda: None
    eventsource.fire()

    # Exception raised into the handler
    raised = False
    eventsource = _EventSource()
    eventsource += lambda: 1 / 0
    try:
        eventsource.fire()
    except ZeroDivisionError:
        raised = True
    assert raised

    # Exception raised into the handler which is swallowed
    eventsource = _EventSource()
    eventsource._on_exception = lambda h, e, *a, **kw: False
    eventsource += lambda: 1 / 0
    eventsource.fire()

    # Exception raised into the handler which is rethrown
    eventsource = _EventSource()
    eventsource += lambda: 1 / 0
    raised = False

# Generated at 2022-06-13 15:55:08.108443
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test whether exception raised by event handler is re-raised
    def handler1():
        raise Exception("foo")

    def handler2():
        raise Exception("bar")

    event_source = _EventSource()

    event_source += handler1
    event_source += handler2

    try:
        event_source.fire()
        assert False, "Exception not raised"
    except Exception as ex:
        assert ex.args[0] == "foo"

    event_source.fire()


test__EventSource_fire()

# Generated at 2022-06-13 15:55:18.511019
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self.call_count = 0
            self.fired_args = None
            self.fired_kwargs = None

        def _caller(self, *args, **kwargs):
            self.call_count += 1
            self.fired_args = args
            self.fired_kwargs = kwargs

        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    # test 1, without exceptions
    a = MyEventSource()
    a += a._caller
    a.fire(1, 2, 3, foo='bar')
    assert a.call_count == 1
    assert a.fired_args == (1, 2, 3)


# Generated at 2022-06-13 15:55:29.685452
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # prepare the unit test
    #   create a mock handler and let it store the args and kwargs it received
    mock_handler = type('mock_handler', (object,), dict(called=False, args=None, kwargs=None))

    def handler(*args, **kwargs):
        mock_handler.called = True
        mock_handler.args = args
        mock_handler.kwargs = kwargs

    #   add the mock handler to the event source
    event_source = _EventSource()
    event_source += handler

    #   create the args and kwargs to pass to the function fire
    args = (1, 2, 3)
    kwargs = dict(a=1, b=2, c=3)

    # execute the function fire
    event_source.fire(*args, **kwargs)



# Generated at 2022-06-13 15:55:38.202575
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler1(*args, **kwargs):
        assert 1 == len(args)
        assert 'p1' == args[0]
        assert 2 == len(kwargs)
        assert 'p2' == kwargs['arg1']
        assert 'p3' == kwargs['arg2']

    def handler2(*args, **kwargs):
        assert 1 == len(args)
        assert 'p4' == args[0]
        assert 2 == len(kwargs)
        assert 'p5' == kwargs['arg1']
        assert 'p6' == kwargs['arg2']

    event_source += handler1
    event_source += handler2

    event_source.fire('p1', arg1='p2', arg2='p3')
    event_source

# Generated at 2022-06-13 15:55:46.204304
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handle1(a, b):
        assert a == 123
        assert b == 'hello'
        handle1.called = True

    def handle2(a, b):
        assert a == 123
        assert b == 'hello'
        handle2.called = True

    handle1.called = False
    handle2.called = False

    evt = _EventSource()
    evt += handle1
    evt += handle2

    evt.fire(123, b='hello')

    assert handle1.called
    assert handle2.called

# Generated at 2022-06-13 15:55:54.025916
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def _handler(called, pass_return, error_return, *args, **kwargs):
        called.append((args, kwargs))
        if pass_return:
            return pass_return
        elif error_return:
            raise Exception(error_return)

    call_args = ()

    es = _EventSource()
    called = []
    es += _handler
    es.fire(*call_args, pass_return=None, error_return=None)
    assert len(called) == 1
    assert called[0] == (call_args, {})

    #
    # with exception
    #
    called = []
    es = _EventSource()
    es += _handler

# Generated at 2022-06-13 15:56:03.903449
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    hdl_call_result = [None]

    def _hdl(aa):
        hdl_call_result[0] = aa

    es = _EventSource()
    es += _hdl
    assert len(es._handlers) == 1
    assert hdl_call_result == [None]

    es.fire("arg")
    assert hdl_call_result == ["arg"]

    es -= _hdl
    assert len(es._handlers) == 0
    assert hdl_call_result == ["arg"]
    es.fire("second arg")
    assert hdl_call_result == ["arg"]

    hdl_call_result = [None]

    class _Exception(Exception):
        pass


# Generated at 2022-06-13 15:56:09.861508
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            # let the event source consume the exception
            pass

    class EventHandler1:
        def __call__(self, *args, **kwargs):
            raise Exception('EventHandler1')

    class EventHandler2:
        def __call__(self, *args, **kwargs):
            raise Exception('EventHandler2')

    evt = EventSource()
    evt += EventHandler1()
    evt += EventHandler2()

    evt.fire()



# Generated at 2022-06-13 15:57:28.365663
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _UnitTestEventSource(_EventSource):
        def __init__(self):
            super(_UnitTestEventSource, self).__init__()
            self._ex_caller = None
            self._ex_handler = None
            self._ex_handler_args = None
            self._ex_handler_kwargs = None
            self._ex_raised = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._ex_caller = args[0]
            self._ex_handler = handler
            self._ex_handler_args = args[1:]
            self._ex_handler_kwargs = kwargs
            self._ex_raised = exc
            raise exc

    def _hndlr1(*args, **kwargs):
        pass


# Generated at 2022-06-13 15:57:36.565096
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Handler:
        def __init__(self):
            self.last_exception = None

        def __call__(self, *args, **kwargs):
            raise TypeError()

        def on_exception(self, handler, exc, *args, **kwargs):
            self.last_exception = exc

    handler = Handler()
    event = _EventSource().__iadd__(handler)
    event._on_exception = handler.on_exception

    try:
        event.fire()
    except TypeError:
        raise
    except Exception as ex:
        assert ex == handler.last_exception

# Generated at 2022-06-13 15:57:46.851880
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def foo(event_source, a, b):
        foo.fired = True
        foo.source = event_source
        foo.a = a
        foo.b = b

    # fire an event with no registered handlers
    event_source = _EventSource()
    event_source.fire('event1')

    # register a handler and fire an event with no args
    foo.fired = False
    event_source += foo
    event_source.fire('event2')
    assert foo.fired
    assert foo.source is event_source
    assert foo.a == 'event2'
    assert foo.b is None

    # register a handler and fire an event with args and kwargs
    foo.fired = False
    event_source += foo
    event_source.fire('event3', 1, 2)
    assert foo.fired
   

# Generated at 2022-06-13 15:57:51.146877
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event.fire()

    # make sure it does not blow up if one of the handlers throws
    def bad_handler():
        raise ValueError('something bad happened')

    event += bad_handler
    try:
        event.fire()
        assert False, 'exception was not raised'
    except:
        pass

# Generated at 2022-06-13 15:57:59.046397
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest
    import imp
    test_utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_utils.py')
    ansible_test_utils = imp.load_source('ansible_test_utils', test_utils_path)
    from ansible_test_utils import yaml_to_dict

    class TestEventSourceFire(unittest.TestCase):
        def test_no_handlers(self):
            evt = _EventSource()
            evt.fire(1, 2, 3)

        def test_passing_handlers(self):
            r = []
            evt = _EventSource()
            evt += r.append
            evt.fire(1, 2, 3)
            self.assertE

# Generated at 2022-06-13 15:58:10.200362
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def on_event1(event1_counter):
        event1_counter[0] += 1

    def on_event2(event2_counter):
        event2_counter[0] += 1

    def on_event3(event3_counter):
        event3_counter[0] += 1

    on_event1_counter = [0]
    on_event2_counter = [0]
    on_event3_counter = [0]

    event_source += on_event1
    event_source += on_event2
    event_source += on_event3

    event_source.fire(on_event1_counter, on_event2_counter, on_event3_counter)

    assert on_event1_counter == [1]

# Generated at 2022-06-13 15:58:16.774366
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            self._exceptions = []
            super(MyEventSource, self).__init__()

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._exceptions.append(exc)
            return True

        def exceptions(self):
            return self._exceptions

    def handler1(x, y, z):
        pass

    def handler2(x, y, z):
        raise ValueError()

    my_es = MyEventSource()
    my_es += handler1
    my_es += handler2

    assert my_es.exceptions() == []

    my_es.fire(1, 2, 3)

    assert len(my_es.exceptions()) == 1

    exc = my_es.ex

# Generated at 2022-06-13 15:58:17.839124
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass

# Generated at 2022-06-13 15:58:27.449850
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    source = _EventSource()
    result = False

    def handler1(*args, **kwargs):
        nonlocal result
        result = 'handler1'

    def handler2(*args, **kwargs):
        nonlocal result
        result = 'handler2'

    def handler3(*args, **kwargs):
        nonlocal result
        result = 'handler3'

    source += handler1
    source.fire()
    assert result == 'handler1'

    source += handler1
    source.fire()
    assert result == 'handler1'

    source += handler2
    source.fire()
    assert result == 'handler2'

    source -= handler2
    source.fire()
    assert result == 'handler1'

    source -= handler1
    source.fire()
    assert result is False

    source += handler1

# Generated at 2022-06-13 15:58:33.409690
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def test_handler(a, b, c):
        print("a = {}, b = {}, c = {}".format(a, b, c))

    event_source += test_handler
    event_source.fire(1, 2, 3)
    event_source -= test_handler
    event_source.fire(4, 5, 6)