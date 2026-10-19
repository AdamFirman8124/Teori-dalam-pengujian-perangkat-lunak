

# Generated at 2022-06-13 15:49:05.428038
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # test callable handler
    event = _EventSource()
    event += lambda: True
    assert len(event._handlers) == 1

    # test non-callable handler
    try:
        event += []
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    assert len(event._handlers) == 1

    # test non-callable handler
    try:
        event += 'not callable'
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    assert len(event._handlers) == 1


# Generated at 2022-06-13 15:49:14.751567
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def test_event_handler(*args, **kwargs):
        raise Exception()


# Generated at 2022-06-13 15:49:15.940560
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    event += lambda x: None



# Generated at 2022-06-13 15:49:20.316724
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __call__(self):
            self.fire('test1')
    es = TestEventSource()

    # test without handlers
    es()

    calls = []
    es += lambda: calls.append(1)
    es += lambda: calls.append(2)
    es()

    assert calls == [1, 2]


# Generated at 2022-06-13 15:49:22.100844
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    event_source += lambda x: x

    assert 1 == len(event_source._handlers)



# Generated at 2022-06-13 15:49:24.662136
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def dummyhandler(*args, **kwargs):
        pass

    es = _EventSource()
    es += dummyhandler
    assert es._handlers == set([dummyhandler])



# Generated at 2022-06-13 15:49:28.185044
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    fired = []

    def handler():
        fired.append('handler')

    es = _EventSource()
    es += handler

    es.fire()

    assert len(fired) == 1, "handler did not fire"

# Generated at 2022-06-13 15:49:31.388982
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # This test method can only be executed in Python 3.
    test_obj = _EventSource()
    test_obj += (lambda: True)
    test_obj += (lambda: True)
    assert len(test_obj._handlers) == 2


# Generated at 2022-06-13 15:49:34.395816
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    ev = _EventSource()
    assert isinstance(ev, _EventSource)
    def test_handler(foo):
        assert foo == 42
    ev += test_handler
    # this method will call test_handler with an argument of "42"
    ev.fire(42)


# Generated at 2022-06-13 15:49:42.745731
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self._on_exception = self._on_exception_default

        def _on_exception_default(self, handler, exc, *args, **kwargs):
            return True

        def _on_exception_ignore_FooExceptions(self, handler, exc, *args, **kwargs):
            if isinstance(exc, FooException):
                return False
            return True

    s = _TestEventSource()
    assert len(s._handlers) == 0

    def handler0():
        raise ValueError("handler0")

    def handler1():
        raise FooException("handler1")

    with pytest.raises(ValueError) as excinfo:
        s.fire()

# Generated at 2022-06-13 15:49:48.382023
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event += lambda: None
    event.fire()


# Generated at 2022-06-13 15:49:51.796449
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventTester(AnsibleCollectionConfig):
        pass

    EventTester.on_collection_load.__class__.__iadd__(EventTester.on_collection_load, lambda *args, **kwargs: None)



# Generated at 2022-06-13 15:50:03.010296
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import pytest

    eventsrc = _EventSource()
    handler = lambda *args, **kwargs: None

    # ensure that we can add a handler
    eventsrc += handler
    assert len(eventsrc._handlers) == 1
    assert handler in eventsrc._handlers

    # ensure that we can add another handler and that both handlers remain in the set
    eventsrc += lambda *args, **kwargs: 1/0
    assert len(eventsrc._handlers) == 2
    assert handler in eventsrc._handlers

    # ensure that we can't add something other than a handler
    with pytest.raises(ValueError):
        eventsrc += object()

    # ensure that we can't add a handler that is already in the set
    with pytest.raises(ValueError):
        eventsrc += handler

    # ensure that we can't add

# Generated at 2022-06-13 15:50:06.113192
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Foo(object):
        def __init__(self):
            self.fired = False

        def __call__(self, *args, **kwargs):
            self.fired = True

    foo = _Foo()
    foo += _EventSource()

    foo.fire()
    assert foo.fired

# Generated at 2022-06-13 15:50:11.335130
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event = _EventSource()
    calls = []

    def handler(*args, **kwargs):
        calls.append((args, kwargs))

    event += handler
    event.fire(1, 2, three=4)

    assert calls == [((1, 2), {'three': 4})]



# Generated at 2022-06-13 15:50:14.824348
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()
    es += lambda: 1
    es += lambda: 1 / 0

    try:
        es.fire()
    except Exception:
        pass
    else:
        raise Exception("Exception expected")


# Generated at 2022-06-13 15:50:17.234974
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += lambda x: 1
    assert callable(iter(e._handlers).__next__())



# Generated at 2022-06-13 15:50:19.346360
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def dummy_handler(a, b, c=None):
        pass

    evt = _EventSource()
    evt += dummy_handler


# Generated at 2022-06-13 15:50:27.869979
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _Test:
        def __init__(self, from_method_fire=False, from_handler=False, from_exc_handler=False, from_call=False):
            self.from_method_fire = from_method_fire
            self.from_handler = from_handler
            self.from_exc_handler = from_exc_handler
            self.from_call = from_call

            self.handler_calls = 0
            self.exc_handler_calls = 0

        def __call__(self, *args, **kwargs):
            self.from_call = True

        def handler(self, *args, **kwargs):
            self.from_handler = True
            self.handler_calls += 1

        def exc_handler(self, *args, **kwargs):
            self.from_exc_handler

# Generated at 2022-06-13 15:50:36.832298
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _ = AnsibleCollectionConfig()

    def f():
        pass

    def g():
        pass

    def h():
        pass

    event = _EventSource()
    assert len(event._handlers) == 0
    event += f
    assert len(event._handlers) ==  1
    assert f in event._handlers
    event += g
    assert len(event._handlers) ==  2
    assert g in event._handlers
    event += h
    assert len(event._handlers) ==  3
    assert h in event._handlers

    # If a function is added more than once, it will only be called once when the event is fired
    event += f
    assert len(event._handlers) ==  3
    assert f in event._handlers


# Generated at 2022-06-13 15:50:47.299389
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # event handlers
    calls = []

    def handler1(sender, *args, **kwargs):
        calls.appen((sender, args, kwargs))

    def handler2(sender, *args, **kwargs):
        calls.appen((sender, args, kwargs))

    # create a new class of the metaclass type and add a couple of handlers
    event = _EventSource()
    event += handler1
    event += handler2

    # fire event and test that handlers 1 and 2 were called
    event.fire(sender='sender')
    assert len(calls) == 2
    assert calls[0] == ('sender', (), {})
    assert calls[1] == ('sender', (), {})

    # add same handler again and make sure it only gets called once
    calls.clear()

# Generated at 2022-06-13 15:50:53.995724
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class ParameterError(Exception):
        pass

    class _TestEventSource(_EventSource):
        def _on_exception(cls, handler, exc, *args, **kwargs):
            super(_TestEventSource, cls)._on_exception(handler, exc, *args, **kwargs)

        def fire(cls, *args, **kwargs):
            cls._on_exception = _EventSource._on_exception
            super(_TestEventSource, cls).fire(*args, **kwargs)

    def handler_one(*args, **kwargs):
        raise ParameterError('handler_one')

    def handler_two(*args, **kwargs):
        return 'handler_two'

    event_source = _TestEventSource()
    event_source += handler_one
    event_source += handler_two

# Generated at 2022-06-13 15:51:00.654464
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def division(a, b):
        a / b
    def assignment(a, b):
        a = b
        
    src = _EventSource()
    src += division
    src += assignment
    
    try:
        src.fire(1, 0)
        assert False, 'test should have failed'
    except ZeroDivisionError:
        pass
    except Exception as e:
        assert False, 'unexpected exception {}'.format(e)

    try:
        src.fire(1, 0)
        assert False, 'test should have failed'
    except ZeroDivisionError:
        pass
    except Exception as e:
        assert False, 'unexpected exception {}'.format(e)



# Generated at 2022-06-13 15:51:02.012988
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: None



# Generated at 2022-06-13 15:51:07.389261
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Testee(_EventSource):
        def __init__(self):
            super(Testee, self).__init__()
            self.fired = False

        def event_handler(self, *args, **kwargs):
            self.fired = True

    testee = Testee()
    testee.fire()
    assert testee.fired

# Generated at 2022-06-13 15:51:09.349634
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    raise NotImplementedError('test_collection_loader._EventSource_fire is not implemented')

# Generated at 2022-06-13 15:51:20.429858
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_A(a, b=1):
        assert a == 1

    def handler_B(a, b=1):
        assert b == 2

    def handler_C():
        raise ValueError('error')

    def handler_D(a, b=1):
        assert False

    es = _EventSource()
    es += handler_A
    es += handler_B
    es += handler_C
    es += handler_D

    # fire event handler_A
    es.fire(1, b=1)

    # fire event handler_B
    es.fire(1, b=2)

    try:
        es.fire(1, b=2)
    except ValueError:
        pass
    else:
        assert False


# Generated at 2022-06-13 15:51:30.942153
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_callback(a, b=None, **kwargs):
        test_callback.assertions.append((a, b, kwargs))

    test_callback.assertions = []

    event_source = _EventSource()
    event_source += test_callback
    event_source.fire(1, 2, a=3, b=4)
    event_source.fire(5, 6, a=7, b=8)

    assert test_callback.assertions == [(1, 2, {'a': 3, 'b': 4}), (5, 6, {'a': 7, 'b': 8})]


# Generated at 2022-06-13 15:51:41.990267
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        pass

    event_source = _EventSource()

    # invalid handler type
    try:
        event_source += 1
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError not raised')

    # valid handler type
    try:
        event_source += handler1
    except ValueError:
        raise AssertionError('ValueError not expected')

    # already added
    try:
        event_source += handler1
    except ValueError:
        raise AssertionError('ValueError not expected')

    # add another handler
    event_source += handler2

    # passed handlers
    if event_source._handlers != set([handler1, handler2]):
        raise Assertion

# Generated at 2022-06-13 15:51:42.978611
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event.fire()

# Generated at 2022-06-13 15:52:02.945620
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # test empty handler return without exception
    es = _EventSource()
    es.fire()

    # test single handler return without exception
    es = _EventSource()
    def _handler():
        pass
    es += _handler
    es.fire()

    # test multiple handlers return without exception
    es = _EventSource()
    def _handler_1():
        pass
    es += _handler_1
    def _handler_2():
        pass
    es += _handler_2
    es.fire()

    # test single handler raise exception
    es = _EventSource()
    def _handler():
        raise Exception('test')
    es += _handler
    try:
        es.fire()
        raise AssertionError('event handler failed to raise exception')
    except Exception as e:
        pass

    # test multiple handlers raise exception

# Generated at 2022-06-13 15:52:08.356175
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    a = _EventSource()
    _callable_1_calls = 0

    def _callable_1(*args):
        nonlocal _callable_1_calls
        _callable_1_calls += 1

    a += _callable_1
    assert _callable_1_calls == 0

    a.fire()
    assert _callable_1_calls == 1



# Generated at 2022-06-13 15:52:17.692916
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc):
            # don't re-raise
            return False

    def assert_on_exception_calls_event_source(event_source):
        def handler1(exception):
            raise exception

        def handler2(exception):
            raise exception

        event_source += handler1
        event_source += handler2

        try:
            event_source.fire(RuntimeError('foo'))
        except RuntimeError as e:
            assert str(e) == 'foo'
            assert str(e.__traceback__).endswith('handler2(), test__EventSource_fire()\n')  # pylint: disable=no-member

    assert_on_exception_calls_event_source(MyEventSource())


#

# Generated at 2022-06-13 15:52:24.701078
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        pass

    m = MyEventSource()

    class MyObj(object):
        def __init__(self):
            self.value = None

        def set_value(self, v):
            self.value = v

    x = MyObj()
    assert x.value is None
    m += x.set_value
    m.fire('foo')
    assert x.value == 'foo'

    y = MyObj()
    m += y.set_value
    m.fire('bar')
    assert x.value == 'bar'
    assert y.value == 'bar'

    m -= y.set_value
    m.fire('foobar')
    assert x.value == 'foobar'
    assert y.value == 'bar'


# Generated at 2022-06-13 15:52:27.778783
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(value):
        assert value == 1

    AnsibleCollectionConfig.on_collection_load += handler
    AnsibleCollectionConfig.on_collection_load.fire(1)


# Generated at 2022-06-13 15:52:31.769883
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    obj = _EventSource()

    def func(*args, **kwargs):
        obj.receive_result = (args, kwargs)

    obj += func
    obj.fire('a', 'b', c='d')
    assert obj.receive_result == (('a', 'b'), {'c': 'd'})



# Generated at 2022-06-13 15:52:44.498195
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    import pytest

    event_source = _EventSource()

    event_count = 0

    def event_handler_1(event_source, *args, **kwargs):
        nonlocal event_count
        event_count += 1

    def event_handler_2(event_source, *args, **kwargs):
        nonlocal event_count
        event_count += 2

    event_source += event_handler_1
    event_source += event_handler_2

    event_source.fire()
    assert event_count == 3

    event_source -= event_handler_1
    event_source.fire()
    assert event_count == 5

    event_source -= event_handler_2
    event_source.fire()
    assert event_count == 5  # no change


# Generated at 2022-06-13 15:52:48.982026
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += None

    try:
        es += None
    except ValueError as e:
        assert to_text(e) == 'handler must be callable'
    else:
        assert False



# Generated at 2022-06-13 15:52:51.658695
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert len(es._handlers) == 0
    es += print
    assert len(es._handlers) == 1
    es += print
    assert len(es._handlers) == 2


# Generated at 2022-06-13 15:53:00.981902
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Sequence:
        def __init__(self):
            self._elements = []

        def __getitem__(self, item):
            return self._elements[item]

        def append(self, *args, **kwargs):
            self._elements.append((args, kwargs))

    result = _Sequence()

    def handler1(*args, **kwargs):
        result.append(*args, **kwargs)

    def handler2(*args, **kwargs):
        result.append(*args, **kwargs)

    def handler3(*args, **kwargs):
        result.append(*args, **kwargs)
        raise RuntimeError('exception thrown')

    def handler4(*args, **kwargs):
        result.append(*args, **kwargs)


# Generated at 2022-06-13 15:53:25.165625
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSource(_EventSource):
        def __init__(self):
            self._calls = []

        def fire(self, *args, **kwargs):
            self._calls.append((args, kwargs))
            super(EventSource, self).fire(*args, **kwargs)

        @property
        def calls(self):
            return self._calls

    class Handler:
        def __init__(self, name):
            self.name = name
            self._calls = []

        def __call__(self, *args, **kwargs):
            self._calls.append((args, kwargs))

        @property
        def calls(self):
            return self._calls

    handler1 = Handler('1')
    handler2 = Handler('2')

    event_source = EventSource()

# Generated at 2022-06-13 15:53:36.496921
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyListener:
        def __init__(self):
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class MyListenerException(Exception):
        pass

    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    source = MyEventSource()
    listener = MyListener()
    source += listener

    source.fire(1, 2, kw1=1, kw2=2)

    assert listener.args == (1, 2)
    assert listener.kwargs == {'kw1': 1, 'kw2': 2}


# Generated at 2022-06-13 15:53:38.973192
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    target = _EventSource()
    collection = 1
    target += lambda: setattr(target, 'result', collection)
    target.fire(collection)
    assert target.result == collection

# Generated at 2022-06-13 15:53:50.232117
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # _EventSource: Test fire with an exception
    event = _EventSource()

    def handler(source, ex, *args, **kwargs):
        raise ex

    event.on_exception = handler

    called = [False]

    def handler(exc):
        called[0] = True
        raise RuntimeError('error')

    event += handler

    try:
        event.fire(RuntimeError('original cause'))
    except RuntimeError as exc:
        pass

    assert exc.args[0] == 'error'
    assert called[0]

    # _EventSource: Test fire without an exception
    called = [False]

    def handler(source, ex, *args, **kwargs):
        assert False

    event.on_exception = handler

    def handler1():
        called[0] = True


# Generated at 2022-06-13 15:54:01.280158
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.module_utils.six import assertRegex
    from ansible_test._utils.assertions import assert_not_regexp
    from ansible_test.mock import patch

    event_source = _EventSource()

    def mock_handler_a():
        pass

    def mock_handler_b():
        pass

    def mock_handler_c():
        pass

    def mock__on_exception(handler, exc, *args, **kwargs):
        if handler is mock_handler_c:
            return False

        return True

    event_source._on_exception = mock__on_exception

    with patch.object(event_source, '_handlers') as mock__handlers:
        event_source += mock_handler_a
        assert mock__handlers.add.call_count == 1
       

# Generated at 2022-06-13 15:54:09.325375
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    class AnException(Exception):
        pass

    def handler(arg, kwarg=None):
        if arg == 'a_raised_exception':
            raise AnException('exception handler')
        elif arg == 'an_exception':
            raise Exception('exception handler')
        elif arg == 'a_caught_exception':
            return

    # add two handlers
    e += handler
    e += handler

    # fire with no exceptions
    e.fire('no_exception')

    # fire with one exception that is caught by the handler
    e.fire('a_caught_exception')

    # fire with one exception that is not caught by the handler

# Generated at 2022-06-13 15:54:15.254812
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    calls = []

    def handler1(*args, **kwargs):
        calls.append(('handler1', args, kwargs))

    def handler2(*args, **kwargs):
        calls.append(('handler2', args, kwargs))

    event += handler1
    event += handler2
    event.fire()

    assert calls == [('handler1', (), {}), ('handler2', (), {})]

# Generated at 2022-06-13 15:54:25.499615
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # With no handlers
    with pytest.raises(RuntimeError):
        event = _EventSource()
        event.fire()

    # With a handler that raises an error
    with pytest.raises(RuntimeError):
        event = _EventSource()
        event += lambda: 1 / 0
        event.fire()

    # With a handler that returns True
    with pytest.raises(RuntimeError):
        event = _EventSource()

        def handler():
            return True

        event += handler
        event.fire()

    # With a handler that returns False
    with pytest.raises(Exception):
        event = _EventSource()

        def handler():
            return False

        event += handler
        event.fire()

# Generated at 2022-06-13 15:54:34.480468
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_1(a, b):
        handler_1.called = True
        assert a == 'a'
        assert b == 'b'

    def handler_2(a, b):
        handler_2.called = True
        assert a == 'a'
        assert b == 'b'

    handler_1.called = False
    handler_2.called = False
    event_source = _EventSource()
    event_source += handler_1
    event_source += handler_2

    event_source.fire('a', b='b')

    assert handler_1.called
    assert handler_2.called

# Generated at 2022-06-13 15:54:45.789943
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Test:
        def __init__(self):
            self.called = 0

        def handler(self, x, y):
            self.called += 1

        def handler_with_ex(self, x, y):
            raise RuntimeError()

        def handler_with_ex_and_re_raise(self, x, y):
            raise RuntimeError()

        def handler_with_ex_and_consume(self, x, y):
            pass

    e = _EventSource()
    t = Test()

    e += t.handler
    e.fire(1, y=2)
    assert t.called == 1

    e += t.handler_with_ex
    try:
        e.fire(1, y=2)
        assert False, "should have raised"
    except RuntimeError:
        pass

    t

# Generated at 2022-06-13 15:55:25.009725
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _CounterEventSource(_EventSource):
        def __init__(self):
            super(_CounterEventSource, self).__init__()
            self._counter = 0

        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

        def __call__(self, *args, **kwargs):
            self._counter += 1

    es = _CounterEventSource()

    def handler1(*args, **kwargs):
        pass

    def handler2(*, arg1):
        pass

    es += handler1
    es += handler2

    es.fire()
    assert es._counter == 1

    # handler1 raises an exception, so only handler 2 is called
    def handler1(*args, **kwargs):
        raise Exception()
    es += handler1
    es.fire()

# Generated at 2022-06-13 15:55:36.224647
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass


# Generated at 2022-06-13 15:55:47.573105
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class FooException(Exception):
        pass

    class BazException(Exception):
        pass

    source = _EventSource()

    def foo_handler(*args, **kwargs):
        raise FooException()

    def bar_handler(*args, **kwargs):
        return 'bar'

    def baz_handler(*args, **kwargs):
        raise BazException()

    def baz_handler_with_args(*args, **kwargs):
        raise BazException()
    baz_handler_with_args.args = ('oh no!',)

    def baz_handler_with_kwargs(*args, **kwargs):
        raise BazException()
    baz_handler_with_kwargs.kwargs = {'how': 'sad'}


# Generated at 2022-06-13 15:55:59.825045
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    def handler_1(*args, **kwargs):
        test_case.assertEqual(args, (1,))
        test_case.assertEqual(kwargs, {'k': 'v'})

    def handler_2(*args, **kwargs):
        test_case.assertEqual(args, (1,))
        test_case.assertEqual(kwargs, {'k': 'v'})
        1 / 0

    class MockException(Exception):
        pass

    def handler_3(*args, **kwargs):
        test_case.assertEqual(args, (1,))
        test_case.assertEqual(kwargs, {'k': 'v'})
        raise MockException('testing')


# Generated at 2022-06-13 15:56:07.365791
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            raise RuntimeError('test exception')

    e = TestEventSource()
    def h1(*args, **kwargs):
        print("h1 called")

    def h2(*args, **kwargs):
        print("h2 called")

    def h3(*args, **kwargs):
        raise RuntimeError('test exception')

    e += h1
    e += h2
    e += h3

    try:
        e.fire()
        assert False
    except RuntimeError as ex:
        assert str(ex) == 'test exception'

# Generated at 2022-06-13 15:56:11.284393
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def _handler(event, arg1, arg2, arg3):
        event.append((arg1, arg2, arg3))

    def _exception_handler(event, arg1, arg2, arg3):
        event.append((arg1, arg2, arg3))
        raise RuntimeError('event handler failed')

    # no handlers
    event = []
    source = _EventSource()
    source.fire(event, 'arg 1', 'arg 2', 'arg 3')
    assert event == []

    # 1 handler, no exceptions
    event = []
    source = _EventSource()
    source += _handler
    source.fire(event, 'arg 1', 'arg 2', 'arg 3')
    assert event == [('arg 1', 'arg 2', 'arg 3')]

    # 2 handlers, no exceptions
    event = []

# Generated at 2022-06-13 15:56:16.357813
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        pass

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source.fire('a', b='b')


# Generated at 2022-06-13 15:56:19.983635
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsource = _EventSource()

    raise_exception = False

    def handler_one():
        nonlocal raise_exception
        if raise_exception:
            raise Exception()

    def handler_two():
        nonlocal raise_exception
        if raise_exception:
            raise Exception()

    eventsource += handler_one
    eventsource += handler_two

    # verify no exceptions are raised
    raise_exception = False
    eventsource.fire()

    # verify that exceptions are raised
    raise_exception = True
    try:
        eventsource.fire()
    except Exception:
        pass
    else:
        assert False, 'Expected an exception'


# Generated at 2022-06-13 15:56:28.808289
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test data
    test_data = list()
    test_data.append((0, (), {}, []))                                                               # Empty
    test_data.append((1, (1, 2), {'a': 3, 'b': 4}, [lambda x: None, lambda x, y: None]))            # Multi-arg
    test_data.append((2, (), {}, [lambda: None, lambda: None, lambda: None]))                       # Multiple handlers
    test_data.append((3, (), {}, [lambda: None, lambda: None, lambda: None, lambda:0/0]))           # Exception in handler
    test_data.append((4, (), {}, [lambda: None, lambda: None, lambda: None, lambda:0/0, lambda:0/0]))  # Exceptions in multiple handlers

# Generated at 2022-06-13 15:56:33.477190
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test1(x):
        print('test1 got ' + x)

    def test2(x):
        print('test2 got ' + x)

    e = _EventSource()
    e += test1
    e += test2

    e.fire('junk')



# Generated at 2022-06-13 15:57:40.458623
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _EventSource.__iadd__(None, object)



# Generated at 2022-06-13 15:57:50.636326
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(arg1, arg2):
        pass

    def handler2(arg1, arg2):
        raise Exception('exception')

    class TestClass:
        pass

    test_class = TestClass()

    event_source = _EventSource()
    assert not event_source._handlers
    event_source += handler1
    assert handler1 in event_source._handlers
    event_source += handler2
    assert handler2 in event_source._handlers
    event_source += test_class
    assert test_class not in event_source._handlers

    event_source.fire(1, 2)

    event_source -= handler1
    assert handler1 not in event_source._handlers

    event_source -= handler2
    assert handler2 not in event_source._handlers

    event_source -= test_class


# Generated at 2022-06-13 15:57:58.642290
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # create the object
    es = _EventSource()

    # add a mock handler to the event source
    def handler(x):
        assert x == 1

    es += handler

    # call the method
    es.fire(1)

    # add a handler that raises an exception
    def bad_handler(x):
        raise RuntimeError('handler raised a RuntimeError')

    es += bad_handler

    # call the method again
    try:
        es.fire(1)
    except Exception:
        pass
    else:
        assert False, 'handler did not raise exception'

    # add a handler that raises an exception that is caught by the method
    def handled_handler(x):
        raise ValueError('handler raised a ValueError')

    es += handled_handler

    # override the method to return True

# Generated at 2022-06-13 15:58:09.627283
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    assercallback = lambda *args, **kwargs: None
    class MyListener:
        def __init__(self):
            self.exception = None
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            assercallback(self, *args, **kwargs)

    def on_exception(handler, exc, *args, **kwargs):
        listener.exception = exc
        listener.args = args
        listener.kwargs = kwargs
        return False

    source = _EventSource()
    source._on_exception = on_exception

    listener1 = MyListener()
    listener2 = MyListener()
    listener3 = MyListener()

    source += listener1
    source += listener2
    source += listener3

    ass

# Generated at 2022-06-13 15:58:12.422005
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    handler1 = lambda: None
    event_source += handler1
    event_source += handler1  # no error expected

    assert event_source._handlers == set([handler1])



# Generated at 2022-06-13 15:58:16.310867
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.module_utils.six import assertRaisesRegex

    es = _EventSource()
    with assertRaisesRegex(AssertionError, 'handler must be callable'):
        es += 42
    es += lambda: None
    es -= lambda: None
    es += lambda: None
    es -= lambda: None
    es -= lambda: None
    with assertRaisesRegex(AssertionError, 'handler must be callable'):
        es -= 42


# Generated at 2022-06-13 15:58:26.750940
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import mock
    import pytest

    event = _EventSource()

    def handler1_function(value):
        handler1_function.call_count += 1
        handler1_function.value = value

    handler1_function.call_count = 0
    handler1_function.value = None

    handler1_mock = mock.MagicMock()
    handler1_mock.side_effect = handler1_function

    def handler2_function(value):
        handler2_function.call_count += 1
        handler2_function.value = value

    handler2_function.call_count = 0
    handler2_function.value = None

    def handler3_function(value):
        handler3_function.call_count += 1
        handler3_function.value = value
        raise ValueError('handler 3 error')

    handler

# Generated at 2022-06-13 15:58:34.805465
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_one(*args, **kwargs):
        print('handler_one was called')

    def handler_two(*args, **kwargs):
        print('handler_two was called')

    def handler_three(*args, **kwargs):
        print('handler_three was called')

    event_source = _EventSource()
    event_source += handler_one
    event_source += handler_two

    event_source.fire(1, 2, 3)

    event_source -= handler_one
    event_source += handler_three

    event_source.fire(1, 2, 3)

# Generated at 2022-06-13 15:58:38.255136
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

    def handler():
        pass

    event += handler
    assert event._handlers == set([handler])
    assert handler in event._handlers

    # add the same handler again, should not raise an exception
    event += handler
    assert event._handlers == set([handler])
    assert handler in event._handlers


# Generated at 2022-06-13 15:58:42.631145
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # create a mock function
    def mock_handler(event_object):
        # store arguments passed in to the mock function
        mock_handler.expected_args = (event_object,)

    # instantiate an EventSource object
    event_source = _EventSource()

    # register the mock function as a handler
    event_source += mock_handler

    # fire the event
    event_source.fire('test event')

    # assert the handler was called with the expected arguments
    assert mock_handler.expected_args == ('test event',)
