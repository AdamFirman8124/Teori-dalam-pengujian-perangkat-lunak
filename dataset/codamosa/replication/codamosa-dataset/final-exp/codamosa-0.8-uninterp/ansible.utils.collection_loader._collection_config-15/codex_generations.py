

# Generated at 2022-06-13 15:49:09.637443
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def foo():
        i = 1

    es = _EventSource()
    es += foo
    assert len(es._handlers) == 1
    assert list(es._handlers)[0] is foo

    es += foo
    assert len(es._handlers) == 1
    assert list(es._handlers)[0] is foo

    es += foo
    assert len(es._handlers) == 1
    assert list(es._handlers)[0] is foo


# Generated at 2022-06-13 15:49:19.124849
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(s):
        print('handler1({})'.format(s))

    def handler2(s):
        print('handler2({})'.format(s))
        raise Exception('handler2 exception')

    def handler3(s):
        print('handler3({})'.format(s))

    def handler4(s):
        print('handler4({})'.format(s))
        raise Exception('unhandled exception')

    def handler5(s):
        print('handler5({})'.format(s))
        raise Exception('handler5 exception')

    def handler6(s):
        print('handler6({})'.format(s))
        raise Exception('handler6 exception')


# Generated at 2022-06-13 15:49:24.434967
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    state = []

    def add_to_state(value: str):
        state.append(value)

    def clear_state():
        state.clear()

    def raise_an_exception():
        raise Exception('exception')

    def is_state_empty():
        return len(state) == 0

    def is_state_equal_to(*values: str) -> bool:
        return state == list(values)

    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            state.append('exception')

    events = MyEventSource()
    events.fire('fire1')
    assert is_state_empty()

    events += add_to_state
    events.fire('fire2')

# Generated at 2022-06-13 15:49:33.466878
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def handler1(s, e):
        s.append(e)

    def handler2(s, e):
        s.append(e + '2')

    def handler3(s, e):
        raise RuntimeError('handler3')

    def handler4(s, e):
        e.append('42')

    def handler5(s, e):
        return 42

    def handler6(s, e):
        return

    # Ensure this handler can be called multiple times without removing itself.
    es += handler1
    es += handler1
    es += handler2

    args = []
    es.fire(args, 'foo')
    assert args == ['foo', 'foo2']

    # Ensure that a exception raised by a handler is propagated.
    args = []
    es += handler3
   

# Generated at 2022-06-13 15:49:40.579424
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_EventSource, self).__init__()
            self._exceptions = []

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._exceptions.append((handler, exc, args, kwargs))

        def exceptions(self):
            return self._exceptions

    event = _TestEventSource()

    def return_none(arg):
        return None

    def raise_value_error(arg):
        raise ValueError('%s should be foo' % arg)

    event += return_none
    event += raise_value_error

    event.fire('foo')
    assert len(event.exceptions()) == 0

    event.fire('bar')
    assert len(event.exceptions()) == 1

# Generated at 2022-06-13 15:49:41.379357
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    pass


# Generated at 2022-06-13 15:49:44.153487
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class TestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            raise exc

    es = TestEventSource()
    es += lambda: None
    assert len(es._handlers) == 1



# Generated at 2022-06-13 15:49:48.163911
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: 'foo'
    assert len(es._handlers) == 1
    try:
        es += 'bar'
    except ValueError:
        pass
    else:
        raise AssertionError('Failed to raise ValueError')



# Generated at 2022-06-13 15:49:52.453402
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class test(object):
        def __init__(self):
            self.fire = True
            self.error = None
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            if self.fire:
                return
            raise Exception(self.error)

    tc1 = test()
    tc2 = test()
    tc3 = test()
    tc3.fire = False
    tc3.error = 'test3 exception'

    while True:
        es = _EventSource()
        es += tc1
        es += tc2
        es += tc3

        assert len(es._handlers) == 3
        assert tc1 in es._handlers
        assert tc2 in es._hand

# Generated at 2022-06-13 15:50:03.468642
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class C:
        def __init__(self):
            self.args = None
            self.kwargs = None
            self.exc = None
        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            if self.exc is not None:
                raise self.exc

    c1 = C()
    c2 = C()

    def _on_exception(handler, exc, *args, **kwargs):
        return False

    event = _EventSource()
    event._on_exception = _on_exception
    event += c1
    event += c2
    event.fire(1, 2, a=3, b=4)

    assert c1.args == (1, 2)

# Generated at 2022-06-13 15:50:16.943195
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test basic functionality
    emitter = _EventSource()

    def handler_a(*args, **kwargs):
        return 'a'
    emitter += handler_a

    def handler_b(*args, **kwargs):
        return 'b'
    emitter += handler_b

    def handler_c(*args, **kwargs):
        return 'c'
    emitter += handler_c

    assert emitter.fire(1, 2) == 'c'

    # Test remove
    emitter -= handler_c

    assert emitter.fire(1, 2) == 'b'

    # Test raise exception
    def handler_d(*args, **kwargs):
        raise AssertionError('raised')
    emitter += handler_d


# Generated at 2022-06-13 15:50:21.661375
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsource = _EventSource()
    eventsource += lambda *args, **kwargs: print(args, kwargs)
    eventsource.fire(1, 2, 3, kwarg_a=4, kwarg_b=5)

# Generated at 2022-06-13 15:50:26.104647
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda: None

    try:
        source += []
        assert False, 'expected ValueError'
    except ValueError:
        pass


# Generated at 2022-06-13 15:50:33.274624
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result_list = []

    def handler(arg):
        result_list.append(arg)

    event_source = _EventSource()
    event_source += handler
    event_source += handler
    event_source += handler

    event_source.fire(1)
    assert result_list == [1, 1, 1]

    result_list = []
    event_source.fire(2)
    assert result_list == [2, 2, 2]



# Generated at 2022-06-13 15:50:37.192131
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventSourceTest:
        def __init__(self):
            self.event_source = _EventSource()

        def set_handler(self, handler):
            self.event_source += handler
    es = EventSourceTest()
    handler = lambda x: x
    es.set_handler(handler)
    assert es.event_source._handlers == {handler}

# Generated at 2022-06-13 15:50:46.716306
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Foo:
        def __init__(self):
            self.args = []

        def foo(self, *args, **kwargs):
            self.args.append([args, kwargs])

    foo = _Foo()

    event_source = _EventSource()
    event_source.fire()

    event_source += foo.foo
    event_source.fire()
    event_source.fire(1, 2, 3, a=1, b=2, c=3)

    event_source -= foo.foo
    event_source.fire()

    assert foo.args == [[], [], (1, 2, 3), {'a': 1, 'b': 2, 'c': 3}], foo.args


# Generated at 2022-06-13 15:50:53.638074
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_foo(evt):
        return 'handler_foo:evt=%s' % evt

    def handler_bar(evt):
        return 'handler_bar:evt=%s' % evt

    def handler_baz_exception(evt):
        raise Exception('Exception from handler_baz_exception')

    def handler_quux_exception_reraise(evt):
        raise Exception('Exception from handler_quux_exception_reraise')

    def handler_quux_exception_hide(evt):
        raise Exception('Exception from handler_quux_exception_hide')

    def _on_exception_reraise(handler, exc, evt):
        return True

    def _on_exception_hide(handler, exc, evt):
        return False

    evt

# Generated at 2022-06-13 15:51:03.567244
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    handlers = []
    c1 = 0
    def on_load1(*args, **kwargs):
        nonlocal c1
        c1 += 1

    c2 = 0
    def on_load2(*args, **kwargs):
        nonlocal c2
        c2 += 1

    handlers.append(on_load1)
    handlers.append(on_load2)

    event_source = _EventSource()

    # Install handlers
    event_source += on_load1
    event_source += on_load2

    assert c1 == 0
    assert c2 == 0
    event_source.fire()
    assert c1 == 1
    assert c2 == 1
    event_source.fire()
    assert c1 == 2
    assert c2 == 2

    # Remove handlers
    event_source -= on_load1


# Generated at 2022-06-13 15:51:15.783418
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    arg_value = 'arg'
    kwarg_name = 'kwarg'
    kwarg_value = 'kwarg'

    class DummyHandler:
        called = False
        received_args = None
        received_kwargs = None

        def __call__(self, *args, **kwargs):
            self.called = True
            self.received_args = args
            self.received_kwargs = kwargs

    mock_exception = ValueError('mock exception')

    def test_handler(raise_exception=False):
        handler = DummyHandler()

        event_source = _EventSource()
        event_source += handler

        if raise_exception:
            def on_exception(handler, exc, *args, **kwargs):
                handler.exception = exc
                return False

            event_

# Generated at 2022-06-13 15:51:22.296302
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class A:
        def __init__(self, test):
            self.test = test

        def __call__(self, *args, **kwargs):
            self.test.called.append(args[0])

    import sys
    import unittest

    try:
        from unittest import mock
    except ImportError:
        import mock

    class TestEventSource(unittest.TestCase):

        def test_fire(self):
            self.called = []
            es = _EventSource()
            es += A(self)
            es += A(self)
            es.fire(1)
            self.assertEqual(self.called, [1, 1])

        def test_fire_remove_event(self):
            self.called = []
            es = _EventSource()

# Generated at 2022-06-13 15:51:36.187975
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-locals
    '''_EventSource.fire'''
    def handle_exception(handler):
        def f(exc, *args, **kwargs):
            assert exc.message == 'test exception'
            assert args == (0, 1, 2)
            assert kwargs == {'a': 'A', 'b': 'B', 'c': 'C'}
            assert handler == handler0 or handler == handler1 or handler == handler2 or handler == handler3
            if handler == handler3:
                return False
            return True
        return f

    handlers = set()
    callback0 = lambda: None
    callback1 = lambda: None
    callback2 = lambda: None
    callback3 = lambda: None
    mock_ex

# Generated at 2022-06-13 15:51:39.280883
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    target = _EventSource()
    def handler():
        target._handled = True

    target += handler
    target.fire()
    assert hasattr(target, '_handled')

# Generated at 2022-06-13 15:51:49.843068
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    call_log = []

    def handler1(*args, **kwargs):
        call_log.append(('handler1', args, kwargs))

    def handler2(*args, **kwargs):
        call_log.append(('handler2', args, kwargs))

    def handler3(*args, **kwargs):
        call_log.append(('handler3', args, kwargs))

    source = _EventSource()
    source += handler1
    source += handler2
    source.fire('x', 'y', a='a', b='b')

# Generated at 2022-06-13 15:51:59.054056
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    exc_catch = None
    es = _EventSource()

    # test __iadd__ on cls.__init__
    try:
        es.__iadd__(exc_catch)
    except Exception as e:
        exc_catch = e

    assert str(exc_catch) == 'handler must be callable'

    # test __iadd__ on cls.fire
    def test_handler(x):
        return x

    es = _EventSource()
    es.__iadd__(test_handler)

    assert len(es._handlers) == 1
    assert test_handler in es._handlers



# Generated at 2022-06-13 15:52:08.811971
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    config = AnsibleCollectionConfig()
    class TestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            config.ex = exc
            return False

    # verify test setup is not broken
    assert config.ex is None, 'config.ex should not be defined'

    # Create a TestEventSource instance
    tes = TestEventSource()

    # verify test setup is not broken
    assert tes._handlers == set(), '_handlers should be set()'

    # register a handler with tes
    def handler(arg1, arg2, kwarg=None):
        raise Exception('This exception should be caught by _on_exception')

    tes += handler

    # verify test setup is not broken

# Generated at 2022-06-13 15:52:12.219884
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_a(*args, **kwargs):
        print('handler_a')
        return None

    def handler_b():
        print('handler_b')

    e = _EventSource()
    e += handler_a
    e += handler_b

    e.fire()

# Generated at 2022-06-13 15:52:20.942869
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    def test_handler1(*args, **kwargs):
        pass

    def test_handler2(*args, **kwargs):
        pass

    def test_handler3(*args, **kwargs):
        raise TestException()

    def test_handler4(*args, **kwargs):
        raise Exception()

    event_source = _EventSource()

    event_source += test_handler1
    event_source += test_handler2
    event_source += test_handler3
    event_source += test_handler4
    assert len(event_source._handlers) == 4

    try:
        event_source.fire()
    except TestException:
        pass

    # at this point, handler3 and handler4 got removed
    assert len(event_source._handlers) == 2

    event

# Generated at 2022-06-13 15:52:27.918129
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # if handler is not callable, raise ValueError
    obj = _EventSource()
    handler = 'I am not a callable'
    try:
        obj += handler
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError not raised')
    # if handler is callable, add handler to _handlers
    handler = lambda: None
    obj += handler
    assert obj._handlers == set([handler])


# Generated at 2022-06-13 15:52:34.399381
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class test_handler:
        def __init__(self, value):
            self.value = value

        def __call__(self, value):
            if not value == self.value:
                raise ValueError('invalid value ' + repr(value))



    collection_config = AnsibleCollectionConfig()
    h1 = test_handler(1)
    h2 = test_handler(2)

    collection_config.on_collection_load += h1
    collection_config.on_collection_load += h2

    collection_config.on_collection_load.fire(1)
    collection_config.on_collection_load.fire(2)



# Generated at 2022-06-13 15:52:39.789574
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _test_fired = False

    def _handler(*args, **kwargs):
        nonlocal _test_fired
        _test_fired = True

    _test_source = _EventSource()
    _test_source += _handler

    _test_source.fire()

    assert _test_fired

# Generated at 2022-06-13 15:53:01.554975
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    class Test(unittest.TestCase):
        def test_on_exception(self):
            es = _EventSource()
            es._on_exception = lambda h, e, *args, **kwargs: False

            def handler1(exc):
                raise exc

            es += handler1
            with self.assertRaises(Exception):
                es.fire(Exception())
            es -= handler1

            def handler2(exc):
                raise exc

            es += handler2
            es.fire(Exception())
            es -= handler2

            es += handler2
            with self.assertRaises(Exception):
                es._on_exception = lambda h, e, *args, **kwargs: True
                es.fire(Exception())
            es -= handler2

    unittest.main()

# Unit

# Generated at 2022-06-13 15:53:09.496567
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_no_exc(*args, **kwargs):
        print("handler_no_exc: " + str(args))

    def handler_with_exc(*args, **kwargs):
        print("handler_with_exc: " + str(args))
        raise ValueError("handler_with_exc")

    event_source = _EventSource()

    # Test with handler that does not raise an exception
    print("Test with handler that does not raise an exception")
    event_source += handler_no_exc
    event_source.fire(1, 2)

    # Test with handler that raises an exception caught by _EventSource.
    print("Test with handler that raises an exception caught by _EventSource.")
    event_source += handler_with_exc
    event_source.fire(3, 4)

    # Test with handler that raises an exception that

# Generated at 2022-06-13 15:53:12.221050
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    event_called = False

    def event_handler(message, event_source=event_source, event_called=event_called):
        assert event_source is event_source
        event_called = True

    event_source += event_handler
    event_called = False
    event_source.fire()
    assert event_called



# Generated at 2022-06-13 15:53:18.542177
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    test_handler = lambda x: print('test_handler1', x)
    event_source += test_handler
    event_source += test_handler
    event_source += test_handler
    assert len(event_source._handlers) == 1



# Generated at 2022-06-13 15:53:28.459053
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestHandler(object):
        def __init__(self):
            self.call_count = 0

        def handle(self, event_args):
            self.call_count += 1
            raise RuntimeError()

    def test_handler(event_args):
        raise RuntimeError()

    test_handler_instance = TestHandler()
    test_event = _EventSource()

    for handler in [test_handler, test_handler_instance.handle]:
        test_event += handler
        try:
            test_event.fire(event_args='event_args')
            raise RuntimeError('Should raise RuntimeError')
        except RuntimeError:
            pass
        test_event -= handler

    test_event += test_handler_instance.handle
    test_event += test_handler

# Generated at 2022-06-13 15:53:30.158654
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    evt = _EventSource()
    assert evt is evt.__iadd__(lambda: None)


# Generated at 2022-06-13 15:53:39.250413
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class X:
        def __init__(self):
            self.handler_called = None
            self.handler_args = None
            self.handler_kwargs = None
            self.exception_args = None
            self.exception_kwargs = None

        def _on_exception(self, handler, ex, *args, **kwargs):
            self.exception_args = args
            self.exception_kwargs = kwargs

        def handler(self, *args, **kwargs):
            self.handler_called = True
            self.handler_args = args
            self.handler_kwargs = kwargs

    # Assert that self._on_exception is called when the handler throws an exception.
    x = X()
    e = _EventSource()
    e += x._on_exception
    e

# Generated at 2022-06-13 15:53:45.953749
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    es = _EventSource()
    es += lambda x: print(x)
    es += (lambda x: print(x))

    def f(x):
        print(x)
    es += f

    def f2(x):
        print(x)
    es += f2

    try:
        es += "not callable"
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 15:53:54.399933
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    ev = _EventSource()
    calls = []

    def handler1(*args, **kwargs):
        calls.append(('handler1', args, kwargs))

    def handler1exception(*args, **kwargs):
        raise ValueError('handler1exception')

    def handler2(*args, **kwargs):
        calls.append(('handler2', args, kwargs))

    def handler2exception(*args, **kwargs):
        raise ValueError('handler2exception')

    def handler3(*args, **kwargs):
        calls.append(('handler3', args, kwargs))

    def handler3exception(*args, **kwargs):
        raise ValueError('handler3exception')

    def handler4(*args, **kwargs):
        calls.append(('handler4', args, kwargs))

# Generated at 2022-06-13 15:54:04.444189
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class Boogers:
        def __init__(self):
            self.baz = []

        def handle_booger(self, *args, **kwargs):
            self.baz.append((args, kwargs))

    class Foo:
        def __init__(self):
            self.bar = _EventSource()

    b = Boogers()
    f = Foo()
    f.bar += b.handle_booger

    args = ('foo',)
    kwargs = {'bar': 'baz'}
    f.bar.fire(*args, **kwargs)

    assert f.bar.fire(*args, **kwargs) is None
    assert b.baz[0][0] == args
    assert b.baz[0][1] == kwargs


# Generated at 2022-06-13 15:54:31.305318
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSource(_EventSource):
        def __init__(self):
            super(EventSource, self).__init__()
            self.raised = False

        def _on_exception(self, handler, ex, *args, **kwargs):
            self.raised = True

    es = EventSource()

    def handler1():
        raise ValueError('boom')

    es.fire()

    es += handler1
    es.fire()

    assert es.raised

    es.raised = False
    es.fire(1, 1, 1)
    assert es.raised
    assert len(es._handlers) == 1

    es.raised = False
    es -= handler1
    assert not es._handlers
    ip = es
    ip += handler1
    assert len(es._handlers) == 1
    es.fire()

# Generated at 2022-06-13 15:54:39.346118
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Handler:
        def __init__(self):
            self.last_event = None
            self.last_exception = None

        def handle(self, event):
            self.last_event = event

        def fail(self, event):
            # Cause the first handler to fail.
            # There is no way to guarantee the order of the handlers fired,
            # but there is a good probability that the first handler will be fired.
            raise RuntimeError('fail')

    evt_src = _EventSource()

    handler1 = Handler()
    handler2 = Handler()

    evt_src += handler1.handle
    evt_src += handler2.fail
    evt_src += handler2.handle

    evt_src.fire('event')

    assert handler1.last_event == 'event'
    assert handler2.last

# Generated at 2022-06-13 15:54:48.517587
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceUnitTest(object):
        def __init__(self):
            self.fire_called = False
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.fire_called = True


    event = _EventSource()
    callable1 = EventSourceUnitTest()
    callable2 = EventSourceUnitTest()
    event += callable1
    event += callable2

    event.fire('foo', bar='baz')

    assert callable1.fire_called
    assert callable2.fire_called
    assert callable1.args == ('foo',)
    assert callable1.kwargs == {'bar': 'baz'}
    assert callable

# Generated at 2022-06-13 15:54:58.645029
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    def _raise_exception(*args, **kwargs):
        raise Exception('bad')

    def _raise_exception_ignoring(handler, exc):
        return False


# Generated at 2022-06-13 15:55:10.735989
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def catch_result(result):
        catch_result.result = result

    es = _EventSource()
    es.fire(1, 2, 3, 4)     # should not crash

    es += catch_result
    es.fire('a', 'b', 'c')  # should not crash
    assert catch_result.result == ('a', 'b', 'c')

    del catch_result.result
    es -= catch_result      # should not crash
    es.fire('alpha', 'bravo', 'charlie')  # should not crash
    assert not hasattr(catch_result, 'result')


_CONFIG_INSTANCE = AnsibleCollectionConfig()

# BEGIN(obfuscated) - begin obfuscated code to hide implementation details which are not part of the public API (semantically)
_d = dict()
_d

# Generated at 2022-06-13 15:55:19.594588
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(arg1, arg2):
        handler1.arguments = (arg1, arg2)

    def handler2(arg1, arg2):
        handler2.arguments = (arg1, arg2)

    handler1.arguments = None
    handler2.arguments = None

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source.fire('foo', 'bar')

    assert handler1.arguments == ('foo', 'bar')
    assert handler2.arguments == ('foo', 'bar')



# Generated at 2022-06-13 15:55:31.529887
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_a(*args, **kwargs):
        raise RuntimeError('handler_a')

    def handler_b(*args, **kwargs):
        raise RuntimeError('handler_b')

    def handler_c(*args, **kwargs):
        raise RuntimeError('handler_c')

    def handler_d(*args, **kwargs):
        raise RuntimeError('handler_d')

    e = _EventSource()
    e += handler_a
    e += handler_b
    e += handler_c
    e += handler_d

    try:
        e.fire()
        assert False, 'Expected an exception'
    except RuntimeError as ex:
        assert str(ex) == 'handler_a'

    e -= handler_a

# Generated at 2022-06-13 15:55:34.260341
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    x = _EventSource()
    a_called = False
    x += lambda: setattr(test__EventSource_fire, 'a_called', True)
    x.fire()
    assert a_called



# Generated at 2022-06-13 15:55:46.076470
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test: handler is never called if no handlers are configured
    es = _EventSource()
    es.fire(1, x=2)

    # Test: handler is called once with no arguments
    h1 = lambda: setattr(h1, 'called', True)
    es += h1
    es -= h1
    es.fire()
    assert not hasattr(h1, 'called')

    # Test: handler is called once with arguments
    h2 = lambda a1, a2, a3=3, a4=4, a5=5: setattr(h2, 'called', (a1, a2, a3, a4, a5))
    es += h2
    es.fire(1, 2, 4, 5, a5=6)

# Generated at 2022-06-13 15:55:53.943382
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventHandler:
        def __init__(self):
            self.fired = False

        def handle(self, event):
            self.fired = True

    def _on_exception(handler, ex, *args, **kwargs):
        handler.ex = ex
        return True

    handlers = [EventHandler() for i in range(0, 2)]
    event = _EventSource()
    event._on_exception = _on_exception
    for h in handlers:
        event += h.handle
    event.fire(1)
    for h in handlers:
        assert h.fired, 'handler did not fire'
    event -= handlers[0].handle
    event -= handlers[0].handle
    event -= handlers[1].handle
    event.fire(2)

# Generated at 2022-06-13 15:56:19.863490
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def f(*args, **kwargs):
        print(args, kwargs)

    def f2(*args, **kwargs):
        print(args, kwargs)
        raise ValueError('This is a test.')

    event = _EventSource()
    event += f
    event += f2
    event.fire(1, 2, 3, a='a', b='b', c='c')
    event -= f
    event.fire(1, 2, 3, a='a', b='b', c='c')
    event -= f2
    event.fire(1, 2, 3, a='a', b='b', c='c')

test__EventSource_fire()

# Generated at 2022-06-13 15:56:28.148586
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def handler1():
        pass

    def handler2():
        pass

    es += handler1
    es += handler2

    # should succeed without exception
    es.fire()

    # setup a handler that throws an exception
    def handler3(*args, **kwargs):
        raise Exception('error')
    es += handler3

    exception = None
    # should fail with an exception
    try:
        es.fire()
    except Exception as ex:
        exception = ex

    assert str(exception) == 'error'

    es -= handler3
    exception = None
    # should succeed without exception
    try:
        es.fire()
    except Exception as ex:
        exception = ex

    assert exception is None

# Generated at 2022-06-13 15:56:36.137112
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    is_called = False
    is_exception = False

    def handler():
        nonlocal is_called
        is_called = True

    def on_exception(handler, exc, *args, **kwargs):
        nonlocal is_exception
        is_exception = True
        return False

    source = _EventSource()
    source._on_exception = on_exception
    source += handler
    source.fire()

    assert is_called, "handler must be called"
    assert not is_exception, "on_exception must not be called"

# Generated at 2022-06-13 15:56:44.327808
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(exc):
        handler1.exceptions.append(exc)

    def handler2(exc):
        handler2.exceptions.append(exc)
        raise exc

    def handler3(exc):
        handler3.exceptions.append(exc)
        return False

    # Before each test we reset the _exceptions counters
    handler1.exceptions = []
    handler2.exceptions = []
    handler3.exceptions = []

    events = _EventSource()

    # Test without any event handler
    events.fire(ValueError('Test 1'))

    # Test with three handlers
    events += handler1
    events += handler2
    events += handler3


# Generated at 2022-06-13 15:56:50.471541
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Setup
    event_source = _EventSource()
    handler_1 = None
    handler_2 = None
    args = None
    kwargs = None
    try:
        # Exercise
        event_source.fire(args, kwargs)
    except ValueError as e:
        # Verify
        assert handler_1 is not None
        assert handler_2 is not None
        assert str(e) == "handler must be callable"
    else:
        assert False, "Test failure"


# Generated at 2022-06-13 15:56:59.769650
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(*args, **kwargs):
        assert args == [1, 2, 3]
        assert kwargs == {'a': 1, 'b': 2}

    def handler2(*args, **kwargs):
        assert args == [1, 2, 3]
        assert kwargs == {'a': 1, 'b': 2}

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source.fire([1, 2, 3], a=1, b=2)
    event_source -= handler2
    event_source.fire([1, 2, 3], a=1, b=2)

# Generated at 2022-06-13 15:57:12.120700
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    ev = _EventSource()

    class Z:
        def __init__(self):
            self.called = False

        def handler(self, *args, **kwargs):
            self.called = True
            assert args == (1, 2)
            assert kwargs == {'three': 'four'}

    z = Z()

    ev += z.handler
    ev.fire(1, 2, three='four')
    assert z.called

    class Y:
        def handler(self, *args, **kwargs):
            Z.handler(self, *args, **kwargs)
            assert hasattr(self, 'y')

    y = Y()
    y.y = 3

    ev += y.handler
    ev.fire(1, 2, three='four')
    assert z.called
    assert y.called



# Generated at 2022-06-13 15:57:16.510245
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(arg1):
        handler1.called.append(arg1)

    handler1.called = []

    def handler2(arg1):
        handler2.called.append(arg1)

    handler2.called = []

    es = _EventSource()
    es += handler1
    es += handler2

    es.fire('abc')
    assert handler1.called == ['abc']
    assert handler2.called == ['abc']


# Generated at 2022-06-13 15:57:26.245049
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_that_returns_true(called):
        called[0] += 1
        return True

    def handler_that_returns_false(called):
        called[0] += 1
        return False

    called_handler = [0]
    event_source = _EventSource()
    event_source += handler_that_returns_false
    event_source += handler_that_returns_true
    event_source += handler_that_returns_false

    try:
        event_source.fire()
    except:
        # just to get coverage on regex
        assert False

    assert called_handler[0] == 3
    called_handler[0] = 0

    try:
        event_source.fire(raise_on_exception=True)
        assert False
    except ValueError:
        assert True
   

# Generated at 2022-06-13 15:57:36.316458
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self.value = 0

        def handler_one(self, *args, **kwargs):
            self.value = self.value + 1

        def handler_two(self, *args, **kwargs):
            self.value = self.value + 2

        def handler_three(self, *args, **kwargs):
            raise Exception('handler_three always fails')

        def handler_four(self, *args, **kwargs):
            raise Exception('handler_four always fails')

        def _on_exception(self, handler, exc, *args, **kwargs):
            return (handler == self.handler_three)

    source = MyEventSource()
    source += source.handler_one


# Generated at 2022-06-13 15:58:35.440623
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class Test:
        def __init__(self):
            self.calls = []

        def handler1(self, *args, **kwargs):
            self.calls.append('handler1')

        def handler2(self, *args, **kwargs):
            self.calls.append('handler2')

        def test(self):
            e = _EventSource()
            e += self.handler1
            e += self.handler2
            e.fire()
            assert self.calls == ['handler1', 'handler2']

    Test().test()

# Generated at 2022-06-13 15:58:40.332102
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler(value):
        return value

    def handler2(value):
        return value + 2

    event_source += handler

    assert event_source.fire(10) is None
    assert event_source.fire(10) is None

    event_source += handler2

    assert event_source.fire(10) is None

    event_source -= handler

    assert event_source.fire(10) is None

# Generated at 2022-06-13 15:58:41.511483
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # not implemented
    pass

# Generated at 2022-06-13 15:58:49.928604
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest(object):
        def __init__(self):
            self.fired = 0
            self.exception = None

        def fire(self, value):
            self.fired += 1
            if value:
                raise ValueError('test')
            else:
                return value

    source = _EventSource()
    source += EventSourceTest().fire

    # fire with a value that doesn't trigger an exception
    source.fire(False)

    assert source._handlers
    assert len(source._handlers) == 1

    # fire with a value that does trigger an exception
    try:
        source.fire(True)
    except ValueError:
        pass

    assert source._handlers
    assert len(source._handlers) == 1

    # unregister the handler
    source -= EventSourceTest().fire

    # fire with

# Generated at 2022-06-13 15:58:55.930415
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def f1(*args, **kwargs):
        pass

    def f2(*args, **kwargs):
        raise ValueError('')

    def f3(*args, **kwargs):
        return 'f3'

    def f4(*args, **kwargs):
        return 'f4'

    e += f1
    e += f2
    e += f3
    e += f4

    e.fire()

    e -= f2
    e.fire()

    try:
        e.fire()
    except Exception as e:
        if not isinstance(e, ValueError):
            raise

# Generated at 2022-06-13 15:59:05.329088
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """
    A method fire of class _EventSource should call its callable argument, which will be given to the method as
    a parameter. This callable argument should be called as a normal function.
    """

    # The implementation of _EventSource._on_exception(h, ex, *args, **kwargs) does nothing and returns True.
    # The method fire of class _EventSource will catch any exception raised by the call to the callable.
    # Since Python 2.6 doesn't support catching all exceptions, we'll test only ValueError, a subclass of
    # BaseException. See https://docs.python.org/2.6/library/exceptions.html.
    # If the call to the callable returns an exception of which the return value of _EventSource._on_exception(h, ex, *args,
    # **kwargs) is True,