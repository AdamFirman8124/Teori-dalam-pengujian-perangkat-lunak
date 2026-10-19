

# Generated at 2022-06-13 15:49:05.058584
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _event_source = _EventSource()
    assert isinstance(_event_source, _EventSource)

    def _callback():
        pass

    _event_source += _callback
    assert _callback in _event_source._handlers


# Generated at 2022-06-13 15:49:10.481104
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    es = _EventSource()
    handler_count = 10

    def _event_handler():
        pass

    # __iadd__
    es += _event_handler
    assert len(es._handlers) == 1
    es += _event_handler
    assert len(es._handlers) == 1

    def _event_handler2():
        pass

    es += _event_handler2
    assert len(es._handlers) == 2



# Generated at 2022-06-13 15:49:15.911713
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()

            self._fired = False

        def fire(self, *args, **kwargs):
            self._fired = True
            super(MyEventSource, self).fire(*args, **kwargs)

    m = MyEventSource()

    assert not m._fired

    m.fire()

    assert m._fired

# Generated at 2022-06-13 15:49:24.299445
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEvent:
        def __init__(self, value):
            self.value = value
    class TestArgs:
        def __init__(self, value):
            self.value = value
    class TestKwargs:
        def __init__(self, value):
            self.value = value

    def test_handler(event, args, kwargs):
        event.value = 'event.value'
        args.value = 'args.value'
        kwargs.value = 'kwargs.value'

    event_source = _EventSource()
    event_source += test_handler
    
    event = TestEvent('event.value')
    args = TestArgs('args.value')
    kwargs = TestKwargs('kwargs.value')

# Generated at 2022-06-13 15:49:33.348473
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEvent:
        def __init__(self):
            self._fire_result = None

        def handler(self, *args, **kwargs):
            self._fire_result = (args, kwargs)

    event_source = _EventSource()
    test_event = _TestEvent()

    # event_source has no handlers
    event_source.fire('arg1', 'arg2', kwarg1='kwarg1')

    # event_source has 1 handler
    event_source += test_event.handler
    event_source.fire('arg1', 'arg2', kwarg1='kwarg1')
    assert test_event._fire_result == (('arg1', 'arg2'), {'kwarg1': 'kwarg1'})

    # event_source has 2 handlers
    event_source += test_

# Generated at 2022-06-13 15:49:40.465236
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    class MyError(Exception):
        pass
    class TooMany(Exception):
        pass

    def handler1(a, b):
        if a == 1:
            raise MyError

    def handler2(a, b):
        if a == 2:
            raise MyError
        elif a == 3:
            raise TooMany

    def handler3(a, b):
        if a == 4:
            raise MyError

    # register the handlers
    event += handler1
    event += handler2
    event += handler3

    # test 1: exception caught and ignored
    try:
        event.fire(1, 'b')
    except TooMany:
        assert False, 'TooMany was raised instead of MyError'
    except MyError:
        pass

# Generated at 2022-06-13 15:49:45.129153
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSource(_EventSource):
        # overload with_metaclass to pass unit tests
        def __init__(self):
            _EventSource.__init__(self)

        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    def incr(x):
        x[0] += 1

    x = [0]
    s = EventSource()
    s += incr
    s.fire(x)

    assert x[0] == 1



# Generated at 2022-06-13 15:49:50.688995
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    assert len(event._handlers) == 0
    event += lambda: None
    assert len(event._handlers) == 1
    event += lambda: None
    assert len(event._handlers) == 2
    # Test exception
    try:
        event += None
        assert False
    except ValueError:
        assert True


# Generated at 2022-06-13 15:49:57.029764
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    events = _EventSource()
    event_count = {'count': 0}

    def handler():
        event_count['count'] += 1

    events += handler
    events += handler

    events.fire()

    assert event_count['count'] == 2


# Generated at 2022-06-13 15:50:02.570741
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

    event_handler = lambda x=None: None

    # event += handler
    event += event_handler
    assert event_handler in event._handlers

    # event += handler
    event += event_handler
    assert len(event._handlers) == 1
    assert event_handler in event._handlers

    # event += None
    try:
        event += None
        assert False
    except:
        assert True



# Generated at 2022-06-13 15:50:10.642259
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsource = _EventSource()
    seen = []
    eventsource += lambda *args, **kwargs: seen.extend(args)
    eventsource.fire('a', 'b', 'c')
    assert seen == ['a', 'b', 'c']

# Generated at 2022-06-13 15:50:20.180484
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    ev = _EventSource()
    assert len(ev._handlers) == 0

    def h1(*args, **kwargs):
        assert args == tuple([1, 2, 3])
        assert kwargs == dict(x=1, y=2, z=3)

    def h2(*args, **kwargs):
        assert args == tuple([1, 2, 3])
        assert kwargs == dict(x=1, y=2, z=3)

    ev += h1
    ev += h2

    assert len(ev._handlers) == 2

    ev.fire(1, 2, 3, x=1, y=2, z=3)

    ev -= h1

    assert len(ev._handlers) == 1

    ev -= h1

    assert len(ev._handlers) == 1


# Generated at 2022-06-13 15:50:23.263755
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventSource(_EventSource):
        def __init__(self):
            self._handlers = set()
            self.fired = False

        def fire(self, *args, **kwargs):
            self.fired = True

    test = EventSource()
    test += EventSource.fire
    test.fire()
    assert test.fired



# Generated at 2022-06-13 15:50:27.397391
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler():
        pass

    # pylint: disable=expression-not-assigned
    event_source += handler
    # pylint: enable=expression-not-assigned



# Generated at 2022-06-13 15:50:31.359343
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def foo():
        pass

    e += foo
    e += foo

    assert len(e._handlers) == 1
    assert foo in e._handlers


# Generated at 2022-06-13 15:50:35.084437
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    event = _EventSource()
    event += lambda x: print("Handler 1")
    event += lambda x: print("Handler 2")

    msg = "ValueError not raised when add non callable handler"
    try:
        event += "test"
        assert False, msg
    except ValueError:
        assert True, msg


# Generated at 2022-06-13 15:50:41.860831
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    # Test return value
    def retval_handler(event, value):
        return value

    # Test exception case
    def exc_handler(event):
        raise ValueError('test')

    # Test exception re-raise case
    def exc_reraise_handler(event):
        raise ValueError('test2')

    event += retval_handler
    event += retval_handler
    event += exc_handler
    event += exc_reraise_handler

    actual = []
    try:
        event.fire(actual, 1)
    except:
        assert False, 'exception expected'

    assert actual == [1, 1]

    try:
        event.fire()
    except ValueError:
        pass
    else:
        assert False, 'ValueError expected'


# Generated at 2022-06-13 15:50:43.793872
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    def f():
        pass
    es += f
    assert f in es._handlers


# Generated at 2022-06-13 15:50:49.596359
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    handler_1 = lambda: None
    handler_2 = lambda: None

    event.fire()

    event += handler_1
    event.fire()

    event += handler_2
    event.fire()

    event -= handler_1
    event.fire()

    event -= handler_2
    event.fire()

    event += handler_1
    event += handler_2
    event.fire()

    event -= handler_2
    event.fire()

    event -= handler_1
    event.fire()


# Generated at 2022-06-13 15:50:54.552869
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    handler = lambda: None

    def test_func(es, handler):
        es += handler
        es += handler
        es -= handler
        es -= handler
        es += 'not callable'

    try:
        test_func(es, handler)
    except ValueError:
        pass
    except Exception as err:
        raise AssertionError('__iadd__ did not raise ValueError when adding a non-callable handler: {}'.format(err))
    else:
        raise AssertionError('__iadd__ did not raise ValueError when adding a non-callable handler')


# Generated at 2022-06-13 15:51:12.811599
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def a(*args, **kwargs):
        pass

    def b(*args, **kwargs):
        raise Exception('b')

    def c(*args, **kwargs):
        raise Exception('c')

    def exception_handler(handler, exc, *args, **kwargs):
        if handler is b:
            raise Exception('exception_handler')
        else:
            return True

    e += a
    e += b
    e += c

    try:
        e.fire()
        assert False, 'expected exception'
    except Exception as ex:
        assert ex.args[0] == 'b'

    e -= b
    e -= c

    try:
        e.fire()
        assert False, 'expected exception'
    except Exception as ex:
        assert ex.args[0]

# Generated at 2022-06-13 15:51:15.418327
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # test success case
    event_source = _EventSource()
    handler = lambda: None
    event_source += handler
    assert handler in event_source._handlers

    # test failure
    with pytest.raises(ValueError):
        event_source += None


# Generated at 2022-06-13 15:51:17.986000
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handle_one(arg):
        pass

    def handle_two(arg):
        pass

    es += handle_one
    es += handle_two

    assert es._handlers == {handle_one, handle_two}



# Generated at 2022-06-13 15:51:25.468337
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    def handler1(message, *other):
        pass

    def handler2(message, *other):
        raise RuntimeError('handler2')

    def handler3(message, *other):
        raise RuntimeError('handler3')

    source += handler1
    source += handler2
    source += handler3

    source.fire(1, 2, 3)



# Generated at 2022-06-13 15:51:28.139372
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    source.fire()

__all__ = ('AnsibleCollectionConfig', 'test__EventSource_fire')

# Generated at 2022-06-13 15:51:39.016826
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def my_handler(arg1, arg2, arg3, kwarg1=None, kwarg2=None):
        my_handler.args.append((arg1, arg2, arg3))
        my_handler.kwargs.append({'kwarg1': kwarg1, 'kwarg2': kwarg2})

    my_handler.args = []
    my_handler.kwargs = []

    es = _EventSource()
    es += my_handler
    es.fire('myarg1', 'myarg2', 'myarg3', kwarg1='mykwarg1', kwarg2='mykwarg2')

    assert my_handler.args == [('myarg1', 'myarg2', 'myarg3')]

# Generated at 2022-06-13 15:51:48.278812
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class _EventSourceTest:
        def __init__(self):
            self._handlers = set()

        def __iadd__(self, handler):
            if not callable(handler):
                raise ValueError('handler must be callable')
            self._handlers.add(handler)
            return self

    obj = _EventSourceTest()
    assert isinstance(obj, _EventSourceTest)
    assert obj._handlers == set()

    def handler_func(a, b):
        return a + b

    obj += handler_func

    assert isinstance(obj, _EventSourceTest)
    assert obj._handlers == {handler_func}



# Generated at 2022-06-13 15:51:59.460097
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler1(a, b=1, c=2, d=3):
        pass

    def handler2(e, f=4, g=5, h=6):
        pass

    def handler3(i, j=7, k=8, l=9):
        raise RuntimeError('testing')

    e = _EventSource()
    e += handler1
    e += handler2

    # handlers are callable
    assert handler1.__call__ is not None
    assert handler2.__call__ is not None

    # we can add the same handler multiple times
    e += handler3
    e += handler3
    e += handler3

    # we can sub handlers that were not added
    e -= handler1
    e -= handler2


# Generated at 2022-06-13 15:52:05.165537
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    handler1 = lambda: None
    handler2 = lambda: None

    event_source += handler1
    event_source += handler2

    event_source.fire()

    event_source -= handler1
    event_source -= handler2

    assert not event_source._handlers


# Generated at 2022-06-13 15:52:14.882803
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = AnsibleCollectionConfig._on_collection_load
    assert len(source._handlers) == 0

    assert source.fire() is None
    assert source.fire(a=1) is None
    assert source.fire(1, 2) is None
    assert source.fire(1, 2, a=3) is None

    def func1(a, b):
        pass

    def func2(a, b, c=1, d=None):
        pass

    source += func1
    assert len(source._handlers) == 1
    assert source.fire(1, 2) is None
    assert source.fire(a=1, b=2) is None

    source += func2
    assert len(source._handlers) == 2
    assert source.fire(1, 2, c=3, d=4) is None


# Generated at 2022-06-13 15:52:22.852583
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += lambda x: x


# Generated at 2022-06-13 15:52:32.428185
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self._last_exception_args = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._last_exception_args = (handler, exc, args, kwargs)
            return False

    # Prepare to test _EventSource.fire
    es = TestEventSource()
    handler1_call_args = None
    handler1_call_kwargs = None
    handler2_call_args = None
    handler2_call_kwargs = None
    handler3_call_args = None
    handler3_call_kwargs = None
    handler4_call_args = None
    handler4_call_kwargs = None

# Generated at 2022-06-13 15:52:44.572742
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest
    from ansible.module_utils.six import PY2

    def foo1(a, b, c=None):
        foo1.call_count += 1
        foo1.args = a, b, c
        foo1.kwargs = {}

    def foo2(a, b, c=None):
        foo2.call_count += 1
        foo2.args = a, b, c
        foo2.kwargs = {}

    def on_exception(handler, exc, *args, **kwargs):
        on_exception.handler = handler
        on_exception.args = args
        on_exception.kwargs = kwargs
        return False

    foo1.call_count = 0
    foo2.call_count = 0
    on_exception.handler = None
    on_

# Generated at 2022-06-13 15:52:47.894519
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda: None
    assert len(source._handlers) == 1


# Generated at 2022-06-13 15:52:51.947277
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    assert callable(es.fire)
    assert callable(es.__iadd__)
    assert callable(es.__isub__)

    def handler(a, b):
        pass

    es += handler
    assert len(es._handlers) == 1
    es += handler
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:52:53.918906
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _event_source = _EventSource()
    assert _event_source.fire() is None

Conf = AnsibleCollectionConfig

# Generated at 2022-06-13 15:52:57.102747
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(src, event):
        assert src is es
        assert event == 'event_value'

    es = _EventSource()
    es += handler
    es.fire('event_value')
    es -= handler


# Generated at 2022-06-13 15:52:59.927866
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    def h(*args):
        pass

    es += h
    assert h in es._handlers


# Generated at 2022-06-13 15:53:06.174820
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """Test _EventSource.fire()."""
    global counter_EventSource_fire
    counter_EventSource_fire = 0
    def reset_counter_EventSource_fire():
        global counter_EventSource_fire
        counter_EventSource_fire = 0
    def inc_counter_EventSource_fire():
        global counter_EventSource_fire
        counter_EventSource_fire += 1
    reset_counter_EventSource_fire()

    test_obj = _EventSource()

    test_obj += inc_counter_EventSource_fire
    test_obj.fire()
    result = counter_EventSource_fire
    assert(result == 1)

    test_obj.fire()
    result = counter_EventSource_fire
    assert(result == 2)


# Generated at 2022-06-13 15:53:19.204362
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    s = _EventSource()

    # Use a class to maintain state between closures
    class HandlerState:
        def __init__(self, index):
            self.index = index

        def __call__(self, *args, **kwargs):
            return self.index

    state1 = HandlerState(index=1)
    state2 = HandlerState(index=2)

    s += state1
    s += state2

    assert state1.index == 1
    assert s.fire() == 2

    state1.index = 2
    state2.index = 1

    assert state2.index == 1
    assert s.fire() == 2

    s += state1
    s += state1
    s -= state1
    state1.index = 2
    state2.index = 1

    assert s.fire() == 1


# Generated at 2022-06-13 15:53:32.557463
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    log_msg = None
    event_source = _EventSource()

    def on_load_log(msg):
        nonlocal log_msg
        log_msg = msg

    def on_load_runtime_error():
        raise RuntimeError()

    event_source += on_load_log
    event_source += on_load_runtime_error

    event_source.fire('msg')

    assert log_msg == 'msg'



# Generated at 2022-06-13 15:53:37.608443
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'one': 'two'}

    def handler2(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'one': 'two'}

    e = _EventSource()
    e += handler1
    e += handler2
    e.fire(1, 2, one='two')



# Generated at 2022-06-13 15:53:40.688418
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler():
        pass

    event_source += handler
    assert handler in event_source._handlers


# Generated at 2022-06-13 15:53:51.228923
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    calls = []

    def f1(*args, **kwargs):
        calls.append('f1: args=%s kwargs=%s' % (args, kwargs))  # noqa

    def f2(*args, **kwargs):
        calls.append('f2: args=%s kwargs=%s' % (args, kwargs))  # noqa
        return 42

    def f3(*args, **kwargs):
        raise RuntimeError('f3 goes boom')

    event = _EventSource()
    event += f1
    event += f2
    event += f3

    event.fire('a', 'b', c=42)

# Generated at 2022-06-13 15:54:02.011109
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    test_source = _EventSource()
    event_handler = lambda x, y : x + y

    assert test_source._handlers == set()

    # we do not allow non-callable objects to be assigned to an event source
    try:
        test_source += event_handler
    except ValueError:
        pass # this is what we want
    else:
        raise ValueError('ValueError not raised')

     # an event handler can only be assigned to an event source once
    test_source += event_handler
    try:
        test_source += event_handler
    except ValueError:
        pass # this is what we want
    else:
        raise ValueError('ValueError not raised')

    assert test_source._handlers == set([event_handler])



# Generated at 2022-06-13 15:54:09.523390
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import sys

    result = []

    def handler1(*args):
        result.append(args)

    def handler2(*args):
        result.append(args)

    def handler3(*args):
        raise NotImplementedError()

    def handler4(*args):
        raise ValueError()

    def handler5(*args):
        sys.exit(1)

    def handler6(*args):
        return 1

    def handler7(*args):
        return True

    event_source = _EventSource()

    event_source += handler1
    event_source += handler2

    event_source.fire('a', 'b')

    assert result == [('a', 'b'), ('a', 'b')]

    # simple removal of existing handler
    event_source -= handler1
    result = []

# Generated at 2022-06-13 15:54:17.405185
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result = []

    def handler1(x, y):
        result.append('handler1 {} {}'.format(x, y))

    def handler2(x, y):
        result.append('handler2 {} {}'.format(x, y))
        assert x == 'x'
        assert y == 'y'

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2

    event_source.fire('x', y='y')

    assert result == ['handler1 x y', 'handler2 x y']

# Unit tests for class AnsibleCollectionConfig

# Generated at 2022-06-13 15:54:27.577212
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            self._fired = None
            self._fired_with_args = None
            super(_TestEventSource, self).__init__()

        def __iadd__(self, func):
            # _EventSource.__iadd__ won't allow us to add a plain function object, so use a wrapper.
            def handler(*args, **kwargs):
                self._fired_with_args = (args, kwargs)
                if func:
                    func(*args, **kwargs)
                else:
                    self._fired = True

            return super(_TestEventSource, self).__iadd__(handler)


# Generated at 2022-06-13 15:54:29.960523
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    mock_handler = MockHandler()

    event = _EventSource()
    event += mock_handler
    event.fire(2, 3)

    assert mock_handler.called_with(2, 3)



# Generated at 2022-06-13 15:54:38.505639
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test 1) Calling handlers with a single argument
    event = _EventSource()
    def handler(arg):
        handler.call_count += 1
        handler.arg = arg
    handler.call_count = 0
    handler.arg = None
    event += handler

    event.fire('test')
    assert handler.call_count == 1, 'handler should have fired once, not %d' % handler.call_count
    assert handler.arg == 'test', 'handler should have fired with arg="test", not %r' % handler.arg

    # Test 2) Calling handlers that raise an exception
    def handler(arg):
        handler.call_count += 1
        raise Exception('expected exception')
    handler.call_count = 0
    handler.arg = None
    event += handler


# Generated at 2022-06-13 15:54:47.102259
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    event += lambda x: x
    assert callable(event)



# Generated at 2022-06-13 15:54:52.838558
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result = []
    A = _EventSource()
    A.fire()

    def handler(value):
        result.append(value)

    A += handler
    A.fire('hello')

    assert len(result) == 1
    assert result[0] == 'hello'


if __name__ == '__main__':
    test__EventSource_fire()

# Generated at 2022-06-13 15:55:01.851892
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _handler:
        def __init__(self, _raise):
            self._raise = _raise
            self._count = 0

        def __call__(self, *args, **kwargs):
            self._count += 1
            if self._raise:
                raise Exception()

        def count(self):
            return self._count

    # test basic functionality
    events = _EventSource()
    handler = _handler(False)
    events += handler
    events.fire()
    assert handler.count() == 1, 'Event handler not fired on event'

    # test event handler error handling
    events = _EventSource()
    handler = _handler(True)
    events += handler
    try:
        events.fire()
    except Exception:
        pass
    assert handler.count() == 1, 'Event handler not fired on event'



# Generated at 2022-06-13 15:55:12.107960
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    cls = _EventSource()
    exc = None

    def handler1(*args, **kwargs):
        raise Exception('handler1_error')

    def handler2(*args, **kwargs):
        raise Exception('handler2_error')

    def handler3(*args, **kwargs):
        raise Exception('handler3_error')

    def on_exception(handler, exception, *args, **kwargs):
        nonlocal exc
        exc = exception

    cls += handler1
    cls += handler2

    cls._on_exception = on_exception

    try:
        cls.fire()
    except Exception:
        pass

    assert exc.args == ('handler1_error',)

    try:
        cls.fire()
    except Exception:
        pass


# Generated at 2022-06-13 15:55:22.633264
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # event source to test
    event_source = _EventSource()

    # our test handler
    handler_call_count = 0

    def handler(event_source, *args, **kwargs):
        nonlocal handler_call_count
        handler_call_count += 1

    # add handler and test
    event_source += handler
    event_source.fire()
    assert handler_call_count == 1

    # remove handler and test
    event_source -= handler
    event_source.fire()
    assert handler_call_count == 1

    # exception handler
    exception_handler_call_count = 0

    def exception_handler(event_source, handler, exc, *args, **kwargs):
        nonlocal exception_handler_call_count
        exception_handler_call_count += 1
        return (exc is None)

   

# Generated at 2022-06-13 15:55:35.057121
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Obs(object):
        def __init__(self):
            self.fire_calls = 0
            self.observe_exception_calls = 0

        def __call__(self, *args, **kwargs):
            self.fire_calls += 1

        def observe_exception(self, handler, exc, *args, **kwargs):
            self.observe_exception_calls += 1

    ob1 = Obs()
    ob2 = Obs()
    ob3 = Obs()

    src = _EventSource()
    src._on_exception = ob3.observe_exception

    src -= ob1
    src += ob1
    src += ob2

    src.fire()
    assert ob1.fire_calls == 1
    assert ob2.fire_calls == 1

   

# Generated at 2022-06-13 15:55:40.135294
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventTarget:
        def __init__(self):
            self.value = 0

        def __call__(self, *args, **kwargs):
            self.value += 1

    target = EventTarget()
    event = _EventSource()
    event += target
    event.fire()

    assert target.value == 1

# Generated at 2022-06-13 15:55:50.612956
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes

    def foo():
        return 'foo'

    def bar():
        return 'bar'

    def throws():
        raise Exception('throws')

    event = _EventSource()
    event += foo
    event += bar
    event += throws

    try:
        event.fire()
    except Exception as ex:
        assert to_bytes(ex) == b'fire: handler threw exception'

    event._on_exception = lambda handler, exc, *args, **kwargs: False
    event.fire()

    event._on_exception = lambda handler, exc, *args, **kwargs: True

# Generated at 2022-06-13 15:55:52.386896
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    evs = _EventSource()

    def handler_1(arg):
        pass

    evs += handler_1

    assert handler_1 in evs._handlers


# Generated at 2022-06-13 15:56:01.483553
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestHandler:
        def __init__(self):
            self.raise_exc = False
            self.exceptions = []
            self.events = []

        def handle(self, *args, **kwargs):
            if self.raise_exc:
                raise ValueError('handler raised an exception')

            self.events.append((args, kwargs))

    test_handler = TestHandler()
    event_source = _EventSource()

    event_source += test_handler.handle

    event_source.fire(1, 2, 3, keyword=True)
    event_source.fire(4, 5, 6, keyword=False)

    assert len(test_handler.events) == 2

    assert test_handler.events[0] == ((1, 2, 3), {'keyword': True})
    assert test_handler.events

# Generated at 2022-06-13 15:56:25.510657
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyException(Exception):
        pass

    class TestSubject:
        def __init__(self):
            self._called = False

        def method(self):
            self._called = True

    result = TestSubject()
    evt = _EventSource()
    handler = result.method
    evt += handler
    evt.fire()
    assert result._called is True

    result = TestSubject()
    evt = _EventSource()
    handler = result.method
    evt += handler
    evt.fire()
    assert result._called is True

    result = TestSubject()
    evt = _EventSource()
    handler = result.method
    evt += handler
    evt -= handler
    evt.fire()
    assert result._called is False

    result_1 = TestSubject()

# Generated at 2022-06-13 15:56:29.160305
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    try:
        event_source.fire()
        event_source += handler
        event_source.fire()
    except Exception:
        pass


# Generated at 2022-06-13 15:56:38.875470
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    class MyException(Exception):
        pass

    counter = 0

    def increment_counter(*args, **kwargs):
        global counter
        counter += 1

    def raiser1(*args, **kwargs):
        raise TestException()

    def raiser2(*args, **kwargs):
        raise MyException()

    def raiser3(*args, **kwargs):
        raise TestException()

    def raiser4(*args, **kwargs):
        raise MyException()

    es = _EventSource()

    es += raiser1
    es += raiser2

    try:
        es.fire()
        assert False, 'TestException was not raised'
    except TestException:
        # this is expected
        pass
    except:
        assert False, 'wrong exception was raised'



# Generated at 2022-06-13 15:56:41.976633
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    error = None
    try:
        event = _EventSource()
        event += 'x'
    except Exception as ex:
        error = ex
    assert isinstance(error, ValueError)

    event = _EventSource()
    event += lambda: 1



# Generated at 2022-06-13 15:56:44.923842
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def copy_args(the_args, the_kwargs):
        the_args.extend(args)
        the_kwargs.update(kwargs)

    args, kwargs = [], {}
    event_source = _EventSource()
    event_source += copy_args
    event_source.fire('foo', 'bar', biz='baz')
    assert args == ['foo', 'bar']
    assert kwargs == {'biz': 'baz'}


# Generated at 2022-06-13 15:56:54.780425
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def echo_handler(s):
        print(s)

    def raise_exception_handler(s):
        return s / 0

    def raise_exception_handler_no_re_raise(s):
        return s / 0

    event_source = _EventSource()
    event_source += echo_handler
    event_source += raise_exception_handler
    event_source += lambda: raise_exception_handler_no_re_raise(s)

    event_source.fire('Hello')
    event_source -= echo_handler
    try:
        event_source.fire('Hello')
    except ZeroDivisionError:
        pass



# Generated at 2022-06-13 15:56:59.687659
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Test:
        def __init__(self):
            self.fired = False

        def handler(self, source):
            self.fired = True

    t = Test()
    source = _EventSource()

    source.fire()
    assert not t.fired

    source += t.handler
    source.fire()
    assert t.fired
    t.fired = False

    source -= t.handler
    source.fire()
    assert not t.fired

# Generated at 2022-06-13 15:57:10.873145
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEvent(object):
        def __init__(self, v):
            self.value = v

    def handler(*args, **kwargs):
        pass

    e = _EventSource()
    e += handler

    was_called = False

    def on_exception(handler, exc, *args, **kwargs):
        nonlocal was_called
        was_called = True

    e._on_exception = on_exception

    e.fire(MyEvent(42))

    assert not was_called

    def raise_exception(x):
        raise Exception('called with {0}'.format(x.value))

    e += raise_exception
    e.fire(MyEvent(42))
    assert was_called

# Generated at 2022-06-13 15:57:18.429568
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        pass

    class Handler1:
        def __call__(self, *args, **kwargs):
            # raise the first time through
            if not hasattr(self, 'has_run'):
                self.has_run = True
                raise ValueError('expected exception')

    class Handler2:
        def __call__(self, *args, **kwargs):
            # raise the first time through
            if not hasattr(self, 'has_run'):
                self.has_run = True
                raise TypeError('another expected exception')

            # the second time through, we want to re-raise
            raise ValueError('another expected exception')


# Generated at 2022-06-13 15:57:23.001477
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Initialize an instance of _EventSource
    event_source = _EventSource()

    # Assert __add__ throws an exception if the handler is not callable
    with pytest.raises(ValueError, match="handler must be callable"):
        event_source.__iadd__(1)



# Generated at 2022-06-13 15:57:46.898935
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    class DummyHandler:
        pass

    a = _EventSource()
    h1 = DummyHandler()
    h2 = DummyHandler()
    h3 = DummyHandler()

    assert h1 not in a._handlers
    assert h2 not in a._handlers
    assert h3 not in a._handlers

    a += h1

    assert h1 in a._handlers
    assert h2 not in a._handlers
    assert h3 not in a._handlers

    a += h2

    assert h1 in a._handlers
    assert h2 in a._handlers
    assert h3 not in a._handlers

    a += h3

    assert h1 in a._handlers
    assert h2 in a._handlers
    assert h3 in a._handlers

    def non_callable():
        pass

# Generated at 2022-06-13 15:57:53.987814
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    assert es._handlers == set()
    assert callable(es)

    es += print
    assert es._handlers == {print}

    try:
        es += 42
        assert False, 'Expected exception ValueError'
    except ValueError:
        assert True

    try:
        es += None
        assert False, 'Expected exception ValueError'
    except ValueError:
        assert True

    try:
        es += print
        assert False, 'Expected exception ValueError'
    except ValueError:
        assert True



# Generated at 2022-06-13 15:57:57.064311
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # setup
    event_source = _EventSource()
    def dummy_handler():
        return

    # test
    event_source += dummy_handler

    # assert
    assert len(event_source._handlers) == 1
    assert dummy_handler in event_source._handlers


# Generated at 2022-06-13 15:58:03.933191
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest(_EventSource):
        def __init__(self):
            super(EventSourceTest, self).__init__()
            self._args = None
            self._kwargs = None
            self._calls = []
            self._handled = False

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            self._handled = True
            return True

        def handler(self, *args, **kwargs):
            self._calls.append((args, kwargs))
            raise ValueError()

    ess = EventSourceTest()
    ess += ess.handler
    args = (1, 2, 3)
    kwargs = dict(kw1=4, kw2=5)


# Generated at 2022-06-13 15:58:13.387089
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''
    :Unit test for method fire of class _EventSource
    :return:
    '''
    def target_func_1(i):
        print(i)

    def target_func_2(i):
        raise Exception(i)

    def target_func_3(i):
        raise NotImplementedError(i)

    def test_event(i):
        test_event._events = i.split()

    test_event._events = None

    test_obj = _EventSource()
    test_obj += target_func_1
    test_obj += target_func_2
    test_obj += target_func_3
    test_obj += test_event

    try:
        test_obj.fire('hello')
    except:
        pass

# Generated at 2022-06-13 15:58:17.074528
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Test:
        pass

    a = Test()
    b = Test()

    callback = Test()

    def handler(a, b, callback, t):
        assert a is t.a
        assert b is t.b
        assert callback is t.callback

    event_source = _EventSource()
    event_source += handler

    event_source.fire(a, b, callback=callback, t=locals())

# Generated at 2022-06-13 15:58:21.005649
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def handler(self):
        return self

    event += handler
    assert event.fire('foo') == event

    def glitch():
        raise ValueError("Oops!")

    event += glitch
    try:
        event.fire("foo")
        assert False, "expected event to raise an exception"
    except ValueError as e:
        assert str(e) == "Oops!"
    finally:
        event -= glitch

    assert event.fire("foo") == event

# Generated at 2022-06-13 15:58:27.778661
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_expected_fail(x):
        raise Exception('expected failure')

    def handler_actual_fail(x):
        raise Exception('actual failure')

    es = _EventSource()
    es.fire('a', 'b', 'c')  # should work, no handlers
    es += handler_expected_fail
    es.fire('a', 'b', 'c')  # should work, handler declared but does not fail
    es += handler_actual_fail
    try:
        es.fire('a', 'b', 'c')
        assert False, 'expected exception'
    except Exception as e:
        assert str(e) == 'actual failure', 'expected exception'



# Generated at 2022-06-13 15:58:34.845409
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class Test:

        def __init__(self):
            self.call_count = 0

        def handler(self, *args, **kwargs):
            self.call_count += 1
            assert args == (1, 2, 3)
            assert kwargs['a'] == 7

    test = Test()
    fire_test = _EventSource()
    fire_test += test.handler

    fire_test.fire(1, 2, 3, a=7)
    assert test.call_count == 1

# Generated at 2022-06-13 15:58:37.186931
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # When called, handlers must be called.
    def handler(*args, **kwargs):
        pass

    obj = _EventSource()
    obj += handler
    assert handler in obj._handlers

