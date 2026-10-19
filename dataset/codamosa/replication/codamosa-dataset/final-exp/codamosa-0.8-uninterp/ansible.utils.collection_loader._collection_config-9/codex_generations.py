

# Generated at 2022-06-13 15:49:06.643892
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()
    called = []

    def handler1(*args, **kwargs):
        called.append(1)

    e.fire()
    assert called == []

    e += handler1
    e.fire()
    assert called == [1]

    def handler2(*args, **kwargs):
        called.append(2)

    e += handler2
    e.fire()
    assert called == [1, 1, 2]

    e -= handler1
    e.fire()
    assert called == [1, 1, 2, 2]

    def handler3(*args, **kwargs):
        called.append(3)
        raise ValueError('This exception should not be propagated')

    e += handler3
    e.fire()
    assert called == [1, 1, 2, 2, 2, 3]



# Generated at 2022-06-13 15:49:13.024858
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest:
        def __init__(self):
            self.value = 0

        def handler(self, value):
            self.value += value

    test = EventSourceTest()
    event = _EventSource()
    event += test.handler
    event += test.handler
    event.fire(1)
    assert test.value == 2
    event.fire(1)
    assert test.value == 4
    event.fire(1)
    assert test.value == 6


# Unit tests for the properties of class AnsibleCollectionConfig

# Generated at 2022-06-13 15:49:19.086955
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Foo:
        def __init__(self):
            self.calls = []

        def bar(self, *args, **kwargs):
            self.calls.append((args, kwargs))

    # basic test
    source = _EventSource()

    foo = Foo()
    source += foo.bar
    source.fire('a', 'b', c='c')

    assert foo.calls == [((u'a', u'b'), {u'c': u'c'})]

    # test all handlers are called
    foo = Foo()
    bar = Foo()

    source += foo.bar
    source += bar.bar

    source.fire('a', 'b', c='c')

    assert foo.calls == [((u'a', u'b'), {u'c': u'c'})]


# Generated at 2022-06-13 15:49:24.388176
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class EventSourceTest:
        def __init__(self):
            self.handlers = set()

        def __iadd__(self, handler):
            if not callable(handler):
                raise ValueError('handler must be callable')
            self.handlers.add(handler)
            return self

    #-------------------------------------------------------------------
    # Success: handler is callable
    #-------------------------------------------------------------------
    def handler1():
        pass
    def handler2():
        pass
    def handler3():
        pass

    event = EventSourceTest()
    assert event.handlers == set()
    event += handler1
    assert event.handlers == {handler1}
    event += handler2
    assert event.handlers == {handler1, handler2}
    event += handler3
    assert event.handlers == {handler1, handler2, handler3}

# Generated at 2022-06-13 15:49:32.441342
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Foo:
        def __init__(self):
            self.bar = 0

    # init _EventSource
    o = _EventSource()

    # check that default event has no handlers
    try:
        o.fire()
        assert False
    except ValueError:
        pass

    # create a handler instance
    f = _Foo()

    # register a handler function
    o += f.handler
    o.fire()

    # check for incrementation
    assert f.bar == 1

    # unregister a handler function
    o -= f.handler
    o.fire()

    # check that incrementation did not occur
    assert f.bar == 1


# Generated at 2022-06-13 15:49:36.639208
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    n = 3
    is_called = [False] * n
    def handler(i):
        def f(self, e):
            is_called[i] = True
        return f

    event_source = _EventSource()
    for i in range(n):
        event_source += handler(i)
    event_source.fire()
    for i in range(n):
        assert(is_called[i])

# Generated at 2022-06-13 15:49:38.163584
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda: None
    assert len(source._handlers) == 1



# Generated at 2022-06-13 15:49:40.334602
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def callable(num):
        assert num == 49

    event += callable
    event.fire(49)

# Generated at 2022-06-13 15:49:45.247947
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    events = 0

    def handler1(a, b, c):
        global events
        assert a == 'a'
        assert b == 'b'
        assert c == 'c'
        events += 1

    def handler2(a, b, c):
        global events
        assert a == 'a'
        assert b == 'b'
        assert c == 'c'
        events += 1

    source = _EventSource()
    source += handler1
    source += handler2

    source.fire('a', 'b', 'c')

    assert events == 2

# Generated at 2022-06-13 15:49:54.776369
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # An instance to be used by the tests
    ev = _EventSource()

    # A "handler" function which will be called via instance.fire
    def handler(arg):
        handler.arg = arg

    handler.arg = None

    # Test that the handler can be added
    ev += handler
    assert handler in ev._handlers

    # Test that the handler can be removed
    ev -= handler
    assert handler not in ev._handlers

    # Test that the handler set can be cleared
    ev += handler
    ev._handlers.clear()
    assert handler not in ev._handlers

    # Test that double-adding a handler is handled gracefully
    ev += handler
    ev += handler
    assert handler in ev._handlers
    assert len(ev._handlers) == 1

    # Test that double-removal of a handler is handled grace

# Generated at 2022-06-13 15:50:01.751564
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    es = _EventSource()
    es += handler
    assert handler in es._handlers
    assert isinstance(es._handlers, set)

    es += handler

    assert len(es._handlers) == 1



# Generated at 2022-06-13 15:50:06.594146
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource();

    def on_event(*args, **kwargs):
        pass

    event_source += on_event
    assert(len(event_source._handlers) == 1)

    event_source.fire()
    assert(len(event_source._handlers) == 1)

    event_source -= on_event
    assert(len(event_source._handlers) == 0)

    event_source -= on_event
    assert(len(event_source._handlers) == 0)


# Generated at 2022-06-13 15:50:16.710485
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from .unit.ansible_test.lib.ansible_test._util.target.legacy_collection_loader.unit.fixtures.mock_collections import mock_collection_loader
    # set the collection config for this unit test
    mock_collection_loader()

    # create a temp event source
    e = _EventSource()

    # add some handler
    def dummy_handler(*args, **kwargs):
        return args, kwargs

    e += dummy_handler
    assert len(e._handlers) == 1
    assert dummy_handler in e._handlers

    # add the same handler again
    e += dummy_handler
    assert len(e._handlers) == 1
    assert dummy_handler in e._handlers

    # try to add a non callable value as a handler

# Generated at 2022-06-13 15:50:24.151974
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """Unit test for method fire of class _EventSource"""
    class _EventSourceTester(object):

        def __init__(self):
            self.count = 0

        def handler(self, *args, **kwargs):
            self.count += 1

    e = _EventSource()
    t = _EventSourceTester()
    e += t.handler
    e += t.handler
    e.fire()

    assert t.count == 2, "Expected count=2, but got %s" % t.count


# Generated at 2022-06-13 15:50:36.141362
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import mock

    class _Handler:
        def __init__(self, name, result):
            self._name = name
            self._result = result
            self._called = False

        def __call__(self, *args, **kwargs):
            self._called = True
            self._args = args
            self._kwargs = kwargs
            return self._result

    handlers = [_Handler(name, result) for name, result in [('a', False), ('b', True)]]

    event_source = _EventSource()
    for h in handlers:
        event_source += h

    result = event_source.fire(1, 2, three=4, five=6)

    for h in handlers:
        assert h._called
        assert h._args == (1, 2)

# Generated at 2022-06-13 15:50:40.295781
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test simple case
    src = _EventSource()

    def echo(value):
        return value

    src += echo
    assert src.fire(1) == 1

    # test exception handling
    def error(value):
        raise Exception('this is fine')

    src += error
    try:
        src.fire(1)
        raise Exception('did not see expected exception')
    except Exception as ex:
        assert ex.args == ('this is fine',)


# Generated at 2022-06-13 15:50:46.875410
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestHandler:
        def __init__(self):
            self._event_args = []

        def __call__(self, *args, **kwargs):
            self._event_args.append((args, kwargs))

    handler1 = TestHandler()
    handler2 = TestHandler()
    source = _EventSource()
    source += handler1
    source += handler2
    source.fire('a', 'b')
    assert handler1._event_args == [
        (('a', 'b'), {}),
    ]
    assert handler2._event_args == [
        (('a', 'b'), {}),
    ]
    source -= handler2
    source.fire('c', 'd')

# Generated at 2022-06-13 15:50:57.886443
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def on_exception(handler, ex, *args, **kwargs):
        assert handler is func
        assert ex.args[0] == 'raised in handler'
        assert args[0] == 'foo'
        assert kwargs['kwargs'] == 'bar'
        return False  # don't re-raise

    source = _EventSource()
    source._on_exception = on_exception

    def func():
        pass

    source += func

    # on_exception returns False, so we should not see an exception
    source.fire('foo', kwargs='bar')

    # on_exception returns True, so we should see an exception
    source._on_exception = lambda *a, **kw: True

# Generated at 2022-06-13 15:51:03.476460
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    """
    Test the __iadd__ method of class _EventSource
    """
    # pylint: disable=protected-access

    # arrange
    es = _EventSource()

    # act
    es += 123  # our handler should be callable

    # assert
    # we should not reach this statement
    assert False



# Generated at 2022-06-13 15:51:06.691000
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    handler = lambda: None
    ret = es.__iadd__(handler)

    assert ret is es
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:51:20.930886
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Events:
        did_fire = False
        got_args = None
        got_kwargs = None
        def handler(self, *args, **kwargs):
            self.did_fire = True
            self.got_args = args
            self.got_kwargs = kwargs
    # simple handler
    events = Events()
    es = _EventSource()
    es += events.handler
    es.fire('a', foo='bar')
    assert events.did_fire
    assert events.got_args == ('a',)
    assert events.got_kwargs == {'foo': 'bar'}
    # multiple handlers
    es += events.handler
    es.fire('a', foo='bar')
    assert events.did_fire
    assert events.got_args == ('a',)
    assert events.got_

# Generated at 2022-06-13 15:51:32.511185
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Foo:
        def __init__(self):
            self._source_ok = _EventSource()
            self._source_surprise = _EventSource()
            self._source_err = _EventSource()

            self._source_ok += self.on_ok
            self._source_surprise += self.on_surprise
            self._source_err += self.on_err

        def on_ok(self, event):
            print("OK: event=%s" % event)

        def on_surprise(self, event):
            raise Exception("SHOULD NOT HAPPEN")

        def on_err(self, event):
            raise Exception("SHOULD NOT HAPPEN")

    f = Foo()
    f._source_ok.fire("foo")
    print()

    old_on_exception = f._source_sur

# Generated at 2022-06-13 15:51:33.984184
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event = _EventSource()
    event += lambda s, e, m: print("Arguments: {}, {}".format(' '.join(s), m))

    event.fire("Hello", "there", message="have a nice day")


# Generated at 2022-06-13 15:51:42.709978
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''
    function assert_events_fired
    '''
    events_fired = []
    events = _EventSource()
    def handler1():
        events_fired.append(1)
    def handler2():
        events_fired.append(2)
    def handler3():
        raise Exception('exc')

    events += handler1
    events += handler2
    events += handler3
    events += handler1
    events += handler2

    events.fire()
    assert events_fired == [1, 2, 1, 2]



# Generated at 2022-06-13 15:51:49.544591
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def a(): nonlocal a_invocations
    def b(): nonlocal b_invocations; raise RuntimeError('foobar')
    def c(): nonlocal c_invocations; raise ValueError('spam')

    a_invocations = 0
    b_invocations = 0
    c_invocations = 0

    es = _EventSource()
    es += a
    es += b
    es += c

    es.fire()

    assert a_invocations == 1
    assert b_invocations == 1
    assert c_invocations == 1

# Generated at 2022-06-13 15:51:53.669754
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # setup
    event_source = _EventSource()
    results = []

    def handler():
        results.append('handler')

    # execute
    event_source.fire()

    event_source += handler
    event_source.fire()
    event_source += handler
    event_source.fire()
    event_source -= handler
    event_source.fire()

    # verify
    assert ['handler', 'handler', 'handler', 'handler'] == results

# Generated at 2022-06-13 15:52:00.906909
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self._test_event_fired = False

        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

        def _handler1(self, *args, **kwargs):
            self._test_event_fired = True

    tes = _TestEventSource()
    tes += tes._handler1

    with pytest.raises(NotImplementedError):
        tes.fire()

    assert tes._test_event_fired is True

# Generated at 2022-06-13 15:52:09.690503
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventHandler:
        def __init__(self):
            self.args = []
            self.kwargs = []
            self.ex = None

        def handle_event(self, *args, **kwargs):
            self.args.append(args)
            self.kwargs.append(kwargs)

        def handle_exception(self, ex):
            self.ex = ex

    # foo handler should get fired
    handler_foo = TestEventHandler()
    handler_foo_fired = False

    def foo(*args, **kwargs):
        nonlocal handler_foo_fired
        handler_foo_fired = True
        handler_foo.handle_event(*args, **kwargs)

    # bar handler should not get fired, as it is removed before the fire
    handler_bar = TestEventHandler()
    handler_bar_

# Generated at 2022-06-13 15:52:10.552061
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _EventSource.__init__()



# Generated at 2022-06-13 15:52:15.837937
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    fired = []

    def on_event(x, y=None):
        fired.append((x, y))

    event += on_event
    event += lambda x, y=None: fired.append((x, y))

    event.fire(1)
    assert fired == [(1, None)]

    event -= on_event
    event.fire(2)
    assert fired == [(1, None), (2, None)]



# Generated at 2022-06-13 15:52:26.720937
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest(_EventSource):
        def __init__(self):
            super(EventSourceTest, self).__init__()
            self._on_exception = self._on_exception_default

        def _on_exception_default(self, handler, exc, *args, **kwargs):
            return True

    ev = EventSourceTest()

    class ErrorEvent(Exception):
        pass

    def fail_func():
        raise ErrorEvent('a')

    def fail_func_args(a, b, c):
        raise ErrorEvent('a')

    def fail_func_kwargs(a=None):
        raise ErrorEvent('a')

    def fail_func_args_kwargs(a, b, c, d=None):
        raise ErrorEvent('a')

    def success_func():
        pass


# Generated at 2022-06-13 15:52:32.159627
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _on_exception = False
    def _on_exception_handler(handler, exc, args, kwargs):
        assert exc == exception
        assert args == (1, 2)
        assert kwargs == {'kwarg': 'kwarg'}
        nonlocal _on_exception
        _on_exception = True

    es = _EventSource()
    es._on_exception = _on_exception_handler
    exception = ValueError('test exception')

    def handler1(*args, **kwargs):
        raise exception

    def handler2(*args, **kwargs):
        pass

    assert len(es._handlers) == 0
    es += handler1
    es += handler2


# Generated at 2022-06-13 15:52:44.534124
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import os
    import re
    from ansible.module_utils.six.moves.urllib.parse import urlparse

    # Parameterize the test function
    class ParametrizedAnsibleCollectionConfig(AnsibleCollectionConfig):
        def __init__(self, cls, meta, name, bases):
            cls._collection_finder = None
            cls._default_collection = None
            cls._on_collection_load = _EventSource()

        def collection_finder(self):
            raise Exception('no')
    def test_parameters():
        # Create test parameters
        params = []
        # Create a parameter set for each test
        params.append(('', None))
        params.append((' ', None))
        params.append(('{0}'.format(os.sep), None))
        params

# Generated at 2022-06-13 15:52:49.290174
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def foo(x):
        raise ValueError(x)

    def bar(x):
        return x

    es += foo
    es += bar
    es -= foo

    assert es.fire('go away') == 'go away'

# Generated at 2022-06-13 15:52:59.923732
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event = _EventSource()

    def handler1(arg1, arg2):
        assert arg1 == 1
        assert arg2 == 2
        # We don't want to raise an exception, so we return normally

    def handler2(arg1, arg2):
        assert arg1 == 1
        assert arg2 == 2
        # We want to raise an exception, so we do that
        raise RuntimeError("handler2")

    def handler3(arg1, arg2):
        assert arg1 == 1
        assert arg2 == 2
        # We want to raise an exception, so we do that
        raise RuntimeError("handler3")

    def on_exception1(handler, exc, arg1, arg2):
        assert arg1 == 1
        assert arg2 == 2
        assert handler == handler1

# Generated at 2022-06-13 15:53:04.710503
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def test_handler(*args, **kwargs):
        assert args == ['arg1', 'arg2']
        assert kwargs == {'kw1': 'value1', 'kw2': 'value2'}

    e = _EventSource()
    e += test_handler
    e.fire('arg1', 'arg2', kw1='value1', kw2='value2')


# Generated at 2022-06-13 15:53:08.180525
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(arg1, arg2):
        handler._arg1 = arg1
        handler._arg2 = arg2

    o = _EventSource()
    o += handler
    o.fire('a', arg2='b')
    assert handler._arg1 == 'a'
    assert handler._arg2 == 'b'



# Generated at 2022-06-13 15:53:20.898092
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def on_one():
        raise Exception('Intentionally raised exception #1')

    def on_two():
        raise Exception('Intentionally raised exception #2')

    # ensure that no exceptions are raised
    source = _EventSource()
    source += on_one
    source += on_two
    source.fire()

    # ensure that exceptions are raised
    source = _EventSource()
    source._on_exception = lambda handler, exc: False
    source += on_one
    source += on_two
    source.fire()

    # ensure that exceptions are raised
    source = _EventSource()
    source._on_exception = lambda handler, exc: True
    source += on_one
    source += on_two
    with pytest.raises(Exception):
        source.fire()


# Generated at 2022-06-13 15:53:31.287916
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Tester:
        def __init__(self, name):
            self.name = name
            self.values = []

        def handler(self, *args, **kwargs):
            self.values.append([args, kwargs])

    t1 = Tester('t1')
    t2 = Tester('t2')
    t3 = Tester('t3')

    src = _EventSource()
    src += t1.handler
    src += t2.handler
    src += t3.handler

    src.fire('a', 'b', c='d')
    assert len(t1.values) == 1
    assert t1.values[0] == [['a', 'b'], {'c': 'd'}]
    assert len(t2.values) == 1

# Generated at 2022-06-13 15:53:38.776758
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Set up the test
    source = _EventSource()
    event_id = 123
    event_msg = 'Event raised'
    # Must not be called
    def handler_raise_exception(event_id, msg):
        raise Exception(msg)
    # Must be called
    def handler_consume_event(event_id, msg):
        def run_callable(name):
            called[name] = True

        if event_id == event_id:
            run_callable('handler_consume_event')
    # Must be called
    def handler_return_true(event_id, msg):
        def run_callable(name):
            called[name] = True

        if event_id == event_id:
            run_callable('handler_return_true')
            return True
    # Must not be

# Generated at 2022-06-13 15:53:51.757740
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # Test with handler that returns True
    def _handler_returns_true(a, b, c, d):
        return True
    event_source += _handler_returns_true
    assert event_source.fire(1, 2, 3, 4) is None

    # Test with handler that returns False
    def _handler_returns_false(a, b, c, d):
        return False
    event_source += _handler_returns_false
    assert event_source.fire(1, 2, 3, 4) is None

    # Test with handler that throws an exception
    def _handler_returns_none(a, b, c, d):
        raise Exception('This is an expected exception.')
    event_source += _handler_returns_none

# Generated at 2022-06-13 15:53:54.773844
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event += lambda x: x + 1
    event += lambda x: x + 2
    assert event.fire(3) == 6


# Generated at 2022-06-13 15:54:04.758397
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    # Exception handling: return value of _on_exception
    log = []
    e._on_exception = lambda self, handler, exc, *args, **kwargs: False
    e += lambda *args, **kwargs: log.append((0, args, kwargs))
    e.fire(0, a=0, b=1)
    e += lambda *args, **kwargs: log.append((1, args, kwargs))
    e += lambda *args, **kwargs: log.append((2, args, kwargs))
    e += lambda *args, **kwargs: log.append((3, args, kwargs))
    e += lambda *args, **kwargs: log.append((4, args, kwargs))
    e += lambda *args, **kwargs: 1

# Generated at 2022-06-13 15:54:09.803960
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(source, value):
        print("handler: source: %s  value: %s" % (source, value))

    source = _EventSource()
    source += handler
    source.fire("source1", value="value1")



# Generated at 2022-06-13 15:54:19.571293
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSourceTest(object):
        def __init__(self):
            self.test_data = {}
            self.test_ex = None

        def __call__(self, *args, **kwargs):
            self.test_data['args'] = args
            self.test_data['kwargs'] = kwargs

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.test_ex = exc


    class _EventSourceTestException(Exception):
        pass

    es = _EventSource()
    es += _EventSourceTest()

    es.fire(1, 2, kwarg1='foo', kwarg2='bar')

    assert es._handlers[0].test_data['args'] == (1, 2)
    assert es._handlers[0].test

# Generated at 2022-06-13 15:54:23.386995
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def func_ok():
        print('func_ok')

    def func_fail():
        print('func_fail')
        raise ValueError('simulated')

    source = _EventSource()
    source += func_ok
    source.fire()

    source += func_fail
    try:
        source.fire()
        assert False, 'expected ValueError'
    except ValueError:
        pass



# Generated at 2022-06-13 15:54:31.752033
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def f1():
        print("hello")

    def f2():
        print("world")

    # Create a class instance
    es = _EventSource()

    # Add two eventhandler to the class instance
    es.__iadd__(f1)
    es.__iadd__(f2)

    # Get the handlers from the class instance and iterate through them and call them
    for handler in es._handlers:
        handler()

    # Remove the eventhandler f2
    es.__isub__(f2)

    # Get the handlers from the class instance and iterate through them and call them
    for handler in es._handlers:
        handler()

# Test that class _AnsibleCollectionConfig is working as a metaclass

# Generated at 2022-06-13 15:54:36.821690
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    def sum(x, y): return x + y
    def mul(x, y): return x * y
    def div(x, y): return x / y

    event += sum
    event += mul
    event += div

    assert list(event.fire(10, 2)) == [20, 20, 5]
    assert len(list(event.fire(10, 2))) == 3



# Generated at 2022-06-13 15:54:47.355500
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    global_exception_caught = None

    def handler_1(evt_obj, event_data):
        event_data['handler_1'] = 'handler_1'

    def handler_2(evt_obj, event_data):
        raise ValueError('event handler raised exception')

    def handler_3(evt_obj, event_data):
        event_data['handler_3'] = 'handler_3'

    def handler_4(evt_obj, event_data):
        event_data['handler_4'] = 'handler_4'

    def handler_exception(handler, exception, *args, **kwargs):
        # remember the first exception we see, regardless of whether we
        # choose to re-raise it
        global global_exception_caught
        global_exception_caught = exception
        return

# Generated at 2022-06-13 15:54:58.342101
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_a(arg1, arg2, arg3):
        out.append('a1')
        out.append(arg1)
        out.append(arg2)
        out.append(arg3)
        return 'returned from a1'

    def handler_b(arg1, arg2, arg3):
        out.append('b1')
        out.append(arg1)
        out.append(arg2)
        out.append(arg3)
        raise ValueError('exception raised by b1')

    def handler_c(arg1, arg2, arg3):
        out.append('c1')
        out.append(arg1)
        out.append(arg2)
        out.append(arg3)
        return 'returned from c1'

    out = []
    es = _Event

# Generated at 2022-06-13 15:55:07.455969
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''Returns True if the test passes'''

    # smoke test of basic event handler.  We'll test invalid cases a different way

# Generated at 2022-06-13 15:55:15.992537
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _Test1:
        def __init__(self, name, do_raise=False):
            self.name = name
            self.received = []
            self.do_raise = do_raise

        def __call__(self, *args, **kwargs):
            if self.do_raise:
                raise ValueError('test')
            self.received.append(args)
            self.received.append(kwargs)

    class _Test2:
        def __init__(self, name, do_raise=False):
            self.name = name
            self.received = []
            self.do_raise = do_raise

        def __call__(self, *args, **kwargs):
            if self.do_raise:
                raise RuntimeError('test')
            self.received.append(args)
            self.received

# Generated at 2022-06-13 15:55:24.421220
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    calls = []

    def f1(*args, **kwargs):
        calls.append(('f1', args, kwargs))

    def f2(*args, **kwargs):
        calls.append(('f2', args, kwargs))
        raise ValueError('foo')

    def f3(*args, **kwargs):
        calls.append(('f3', args, kwargs))
        raise RuntimeError('bar')

    events = _EventSource()
    events += f1
    events += f2
    events += f3

    try:
        events.fire('a', 'b', 'c')
    except ValueError:
        pass


# Generated at 2022-06-13 15:55:32.009774
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class MyException(Exception):
        pass

    def handler0(*args, **kwargs):
        pass

    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        raise MyException('blah')

    es = _EventSource()
    es += handler0
    es += handler1
    es += handler2

    es.fire()


# Generated at 2022-06-13 15:55:36.419343
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    succeeded = False
    failed = False

    def on_event(arg):
        nonlocal succeeded
        succeeded = succeeded or arg

    def on_fail(arg):
        nonlocal failed
        failed = failed or arg

    es = _EventSource()
    es += on_event
    es += on_fail
    es -= on_fail
    es.fire(True)

    assert succeeded
    assert not failed

# Generated at 2022-06-13 15:55:48.458605
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()

            self.fired_count = 0  # how many times the event was fired
            self.handler0_count = 0  # how many times the event handler was called
            self.handler1_count = 0  # how many times the event handler was called
            self.handler2_count = 0  # how many times the event handler was called

            self += self._handler0
            self += self._handler1
            self += self._handler2

        def _handler0(self):
            self.handler0_count += 1

        def _handler1(self, arg1):
            self.handler1_count += 1
            return arg1


# Generated at 2022-06-13 15:56:00.208126
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler_a(*args, **kwargs):
        return (args, kwargs)

    def handler_b(*args, **kwargs):
        return (args, kwargs)

    def handler_c(*args, **kwargs):
        return (args, kwargs)

    def handler_d(*args, **kwargs):
        raise RuntimeError('handler_d error')

    def handler_e(*args, **kwargs):
        raise RuntimeError('handler_e error')

    event_source += handler_a
    event_source += handler_b
    event_source += handler_c
    event_source += handler_d
    event_source += handler_e


# Generated at 2022-06-13 15:56:07.445239
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    class TraceEvent:
        def __init__(self):
            self.events = []

        def handler(self, *args, **kwargs):
            self.events.append((args, kwargs))

    trace = TraceEvent()

    event += trace.handler

    event.fire(1, 2, a=1)
    event.fire(2, 3, b=2)
    event.fire(3, 4, c=3)

    assert trace.events == [((1, 2), {'a': 1}), ((2, 3), {'b': 2}), ((3, 4), {'c': 3})]

# Generated at 2022-06-13 15:56:19.243445
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    def raise_exception(exc):
        raise exc

    def always_return():
        return

    def when_exc_is_ValueError_return_true(exc):
        if isinstance(exc, ValueError):
            return True

    def when_exc_is_ValueError_raise_another_exception(exc):
        if isinstance(exc, ValueError):
            raise RuntimeError('value error')
        return True

    def when_exc_is_ValueError_return_false(exc):
        if isinstance(exc, ValueError):
            return False

    def when_true_always_raise(exc):
        if True:
            raise RuntimeError('always raise')

    on_exception = _EventSource._on_exception
    source._on_exception = when_exc_is_

# Generated at 2022-06-13 15:56:23.671903
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    counter = 0

    def handler():
        nonlocal counter
        counter += 1

    event_source += handler
    event_source += handler

    event_source.fire()
    assert counter == 2

    event_source -= handler
    event_source -= handler

    event_source.fire()
    assert counter == 2

# Generated at 2022-06-13 15:56:37.060305
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    events = _EventSource()

    @events.on_exception
    def on_exception(handler, exc, *args, **kwargs):
        assert handler is handler1
        assert exc is exception

    @events.on_exception
    def on_exception(handler, exc, *args, **kwargs):
        assert handler is handler3
        assert exc is exception

    handler1_count = [0]

    def handler1(*args, **kwargs):
        handler1_count[0] += 1
        raise ValueError('handler1')

    handler2_count = [0]

    def handler2(*args, **kwargs):
        handler2_count[0] += 1
        assert handler1_count[0] == 1

    handler3_count = [0]
    exception = ValueError('handler3')


# Generated at 2022-06-13 15:56:45.359893
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    calls = []

    def h1(*args, **kwargs):
        calls.append(('h1', args, kwargs))

    def h2(*args, **kwargs):
        calls.append(('h2', args, kwargs))

    def h3(*args, **kwargs):
        raise Exception('h3')

    def h4(*args, **kwargs):
        raise Exception('h4')

    event_source = _EventSource()
    event_source += h1
    event_source += h2
    event_source += h3
    event_source += h4

    event_source.fire('hi', 'there', arg='value')

# Generated at 2022-06-13 15:56:52.777391
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(arg):
        raise Exception(arg)

    e = _EventSource()
    e += handler

    handled = False
    try:
        e.fire('foo')
    except Exception as e:
        handled = True
        assert e.args == ('foo', )

    assert handled

    handled = False
    try:
        e.fire('bar')
    except Exception as e:
        handled = True
        assert e.args == ('bar', )

    assert handled


# Generated at 2022-06-13 15:56:54.622775
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler():
        handler.called = True

    handler.called = False

    event = _EventSource()
    event += handler

    event.fire()

    assert handler.called



# Generated at 2022-06-13 15:57:02.499510
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_1(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 3}

    def handler_2(x, y, a=None):
        assert (x, y, a) == (1, 2, 3)

    def handler_3(*args, **kwargs):
        raise Exception()

    def handler_4(*args, **kwargs):
        return False

    def handler_5(*args, **kwargs):
        return True

    def handler_6(*args, **kwargs):
        return True

    def handler_7(*args, **kwargs):
        raise Exception()

    def handler_8(*args, **kwargs):
        raise Exception()

    event = _EventSource()


# Generated at 2022-06-13 15:57:10.344089
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _called = []

    def handler1(*args, **kwargs):
        _called.append('handler1')

    def handler2(*args, **kwargs):
        _called.append('handler2')

    def handler3(*args, **kwargs):
        raise ValueError('oops')

    es = _EventSource()
    es += handler1
    es += handler2
    es += handler3
    es += handler2

    es.fire()

    assert _called == ['handler1', 'handler2', 'handler2']



# Generated at 2022-06-13 15:57:14.226749
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.utils.collection_loader._event_source import _EventSource

    def handler(*args, **kwargs):
        print("Handler called with:", args, kwargs)

    event_source = _EventSource()
    event_source += handler

    event_source.fire(1, 2, msg="hello")

# Generated at 2022-06-13 15:57:18.471456
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    targets = []

    def target(val):
        targets.append(val)

    src = _EventSource()
    src += target

    src.fire(1)
    src.fire(2)

    assert len(targets) == 2
    assert targets[0] == 1
    assert targets[1] == 2

# Generated at 2022-06-13 15:57:22.107547
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsource = _EventSource()
    def handler(arg):
        assert arg == 'hello'
        return True
    eventsource += handler
    eventsource.fire('hello')


# Generated at 2022-06-13 15:57:29.883845
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    sut = _EventSource()
    assert not sut._handlers

    sut.fire()

    handler = lambda x: x
    assert callable(handler)
    sut += handler
    assert sut._handlers == {handler}

    sut.fire('a', b='c')
    assert sut._handlers == {handler}

    sut += handler
    assert len(sut._handlers) == 2

    sut -= handler
    assert sut._handlers == {handler}

    sut -= handler

    error = ValueError()

    def handler_error(a, b):
        raise error

    sut += handler_error

    try:
        sut.fire('a', b='c')
    except ValueError:
        pass
    else:
        assert False, 'expected exception to be raised'



# Generated at 2022-06-13 15:57:45.651131
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class A:
        def __init__(self, name):
            self.name = name

        def __call__(self, *args, **kwargs):
            pass

    class B(_EventSource):
        pass

    b = B()
    a1 = A('a1')
    a2 = A('a2')
    a3 = A('a3')

    assert len(b._handlers) == 0
    b += a1
    b += a2
    b += a3
    assert len(b._handlers) == 3
    assert a1 in b._handlers
    assert a2 in b._handlers
    assert a3 in b._handlers

    b -= a2
    assert len(b._handlers) == 2
    assert a1 in b._handlers
    assert a2 not in b._handlers

# Generated at 2022-06-13 15:57:55.013211
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # handler with no arguments but still called
    def handler1():
        pass

    event_source += handler1

    event_source.fire()

    # handler with arguments but still called
    def handler2(a, b=None):
        pass

    event_source += handler2

    event_source.fire('a', b='b')

    # handler with _on_exception handler that does not re-raise
    def handler3(a, b=None):
        raise ValueError('handler3')

    def on_exception3(handler, err):
        pass

    event_source._on_exception = on_exception3

    event_source += handler3

    event_source.fire('a', b='b')

    # handler with _on_exception handler that re-raises


# Generated at 2022-06-13 15:58:02.431848
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=no-self-use
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common.text.converters import to_text
    from ansible.parsing.yaml.loader import AnsibleLoader

    class TestEventA(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    class TestEventB(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return True

    class TestEventC(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False


# Generated at 2022-06-13 15:58:11.616350
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_data = []

    def test_handler1(*args, **kwargs):
        test_data.append('handler1')

    def test_handler2(*args, **kwargs):
        test_data.append('handler2')

    event_source = _EventSource()
    event_source += test_handler1
    event_source += test_handler2
    event_source.fire()
    assert test_data == ['handler1', 'handler2'], 'EventSource.fire() did not raise handlers as expected'

    test_data.clear()
    event_source -= test_handler1
    event_source.fire()
    assert test_data == ['handler2'], 'EventSource.fire() did not raise handlers as expected'

# Generated at 2022-06-13 15:58:22.925043
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(event, source, source_type, source_name, source_module, source_module_args, source_action):
        assert source == source_args[0]
        assert source_type == source_args[1]
        assert source_name == source_args[2]
        assert source_module == source_args[3]
        assert source_module_args == source_args[4]
        assert source_action == source_args[5]
        assert event == 'loaded'

    source = _EventSource()

    source += handler

    source_args = (1, 2, 3, 4, 5, 6)


# Generated at 2022-06-13 15:58:29.429474
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()

    calls = []

    def handler(a, b, c):
        calls.append((a, b, c))

    source += handler
    assert not calls

    source.fire(1, 2, 3)
    assert calls == [(1, 2, 3)]

    calls.clear()
    source -= handler
    source.fire(1, 2, 3)
    assert not calls



# Generated at 2022-06-13 15:58:32.737340
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Handler:
        def _handler(self, *args, **kwargs):
            pass

    esrc = _EventSource()
    handler = Handler()
    esrc += handler._handler
    esrc.fire()



# Generated at 2022-06-13 15:58:39.490347
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSourceTest(_EventSource):
        def __init__(self):
            super(EventSourceTest, self).__init__()
            self._on_exception_handler_called = False

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._on_exception_handler_called = True
            return False

    event_source_test = EventSourceTest()
    event_source_test += lambda x: 1 / x
    try:
        event_source_test.fire(0)
    except ZeroDivisionError:
        assert True
    except Exception:
        assert False
    else:
        assert False

    assert event_source_test._on_exception_handler_called

# Generated at 2022-06-13 15:58:48.037331
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def f0(*args, **kwargs):
        pass
    def f1(*args, **kwargs):
        pass
    def f2(*args, **kwargs):
        raise ValueError('FAILED')
    def f3(*args, **kwargs):
        raise ValueError('FAILED')

    event_source += f0
    event_source += f1
    event_source += f2
    event_source += f3

    try:
        event_source.fire()
    except ValueError as e:
        assert str(e) == 'FAILED'
        assert isinstance(e, ValueError)

    event_source -= f0
    event_source -= f1
    event_source -= f2


# Generated at 2022-06-13 15:58:51.896024
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    ev = _EventSource()
    fired = []
    def fire_handler(*args, **kwargs):
        fired.append((args, kwargs))
    ev += fire_handler
    ev.fire(1, a=2)
    assert fired == [((1,), dict(a=2))]
