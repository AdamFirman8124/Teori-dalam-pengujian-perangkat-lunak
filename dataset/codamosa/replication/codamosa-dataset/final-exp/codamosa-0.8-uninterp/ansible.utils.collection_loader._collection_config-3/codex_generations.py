

# Generated at 2022-06-13 15:49:02.462789
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass


# Generated at 2022-06-13 15:49:12.189137
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    mock_handler_1 = MagicMock(return_value="handler1")
    mock_handler_2 = MagicMock(return_value="handler2")
    mock_handler_3 = MagicMock(return_value="handler3")
    mock_handler_4 = MagicMock(return_value="handler4")

    event_source = _EventSource()
    event_source += mock_handler_1
    event_source += mock_handler_2
    event_source += mock_handler_3
    event_source += mock_handler_4
    event_source.fire()
    mock_handler_1.assert_called_once_with()
    mock_handler_2.assert_called_once_with()
    mock_handler_3.assert_called_once_with()
    mock_handler_4.assert_called_once_

# Generated at 2022-06-13 15:49:21.249161
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # No handlers, no exceptions
    evt = _EventSource()
    evt.fire()

    # No exceptions, one handler
    #
    # handle returns nothing
    evt = _EventSource()
    fires = 0
    called = []
    def handle(*args, **kwargs):
        fires += 1
        called.append(args)
        called.append(kwargs)
    evt += handle
    evt.fire('a', foo='bar')
    assert fires == 1
    assert called == [(('a',), {'foo': 'bar'})]

    # exception raised, handled by event source
    evt = _EventSource()
    fires = 0
    called = []
    def handle(*args, **kwargs):
        fires += 1
        called.append(args)
        called.append(kwargs)


# Generated at 2022-06-13 15:49:23.594552
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    state = None

    def handler():
        nonlocal state
        state = 'handled'

    event = _EventSource()
    event += handler

    event.fire()
    assert state == 'handled'

    state = None
    event -= handler

    event.fire()
    assert state is None



# Generated at 2022-06-13 15:49:28.830406
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def _handler(a, b):
        assert False

    e = _EventSource()

    e += callable(_handler)
    e -= _handler
    e -= _handler

    try:
        e += object()
        assert False
    except ValueError:
        pass

    class MyEventSource(object):
        pass

    try:
        e.__iadd__(MyEventSource())
    except AttributeError:
        pass

    try:
        e.__isub__(MyEventSource())
    except AttributeError:
        pass

    try:
        e += MyEventSource()
    except ValueError:
        pass

    try:
        e -= MyEventSource()
    except KeyError:
        pass


# Generated at 2022-06-13 15:49:32.538981
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler():
        raise RuntimeError()

    es = _EventSource()
    es += handler

    # Test fire with an exception
    try:
        es.fire()
    except RuntimeError:
        pass
    except Exception:
        raise Exception('fire failed to raise RuntimeError')

    # Test fire without an exception
    es.fire()


# Generated at 2022-06-13 15:49:38.340684
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

    assert not event._handlers
    event += 'test'
    assert not event._handlers

    def handler1(arg1, arg2):
        pass

    assert not event._handlers
    event += handler1
    assert handler1 in event._handlers

    def handler2(arg1, arg2):
        pass

    assert not event._handlers
    event += handler2
    assert handler2 in event._handlers

    assert event._handlers == {handler1, handler2}

    event += handler1
    assert event._handlers == {handler1, handler2}



# Generated at 2022-06-13 15:49:43.940409
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def callback_a(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 1}
        callback_a.called = True

    def callback_b(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 1}
        callback_b.called = True

    callback_a.called = False
    callback_b.called = False

    try:
        e += callback_a
        e += callback_b
        e.fire(1, 2, a=1)
        assert callback_a.called
        assert callback_b.called
    finally:
        e -= callback_a
        e -= callback_b



# Generated at 2022-06-13 15:49:51.621920
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def _event_handler(event_arg):
        event_arg.append(1)

    # handler must be callable
    event_source = _EventSource()

    try:
        event_source += 1
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError, but no exception raised')

    # handler must be callable
    event_source = _EventSource()

    try:
        event_source += 'bad_handler'
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError, but no exception raised')

    # handler must be callable
    event_source = _EventSource()
    event_source += _event_handler
    expect_result = []
    event_source.fire(expect_result)


# Generated at 2022-06-13 15:49:57.236191
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()
    evt.fire()
    evt += print
    evt += lambda text: print(text, " ", text)
    evt.fire("hello")
    evt -= print
    evt.fire("hello")


# Generated at 2022-06-13 15:50:07.946850
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        pass

    results = []

    def handler(value):
        results.append('handler called with: {}'.format(value))

    def exception_handler(value):
        results.append('exception_handler called with: {}'.format(value))
        return False

    my_event_source = MyEventSource()
    my_event_source.fire()
    assert len(results) == 0

    my_event_source += handler
    my_event_source += exception_handler
    my_event_source.fire()
    assert len(results) == 2
    assert results == ['handler called with: None', 'exception_handler called with: None']

    results.clear()
    my_event_source.fire('hello')
    assert len(results) == 2

# Generated at 2022-06-13 15:50:15.413185
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def testfunction1():
        pass

    def testfunction2():
        pass

    set1 = set([testfunction1, testfunction2])
    set2 = set([testfunction1])

    eventsource = _EventSource()
    eventsource += (lambda: None)
    eventsource += testfunction1
    eventsource += testfunction2
    eventsource += testfunction2

    assert set1 == set(eventsource._handlers)

    eventsource -= testfunction2

    assert set2 == set(eventsource._handlers)

    # raise exception as handler parameter is not callable
    try:
        eventsource += None
        assert False
    except ValueError:
        pass


# Generated at 2022-06-13 15:50:16.861903
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _EventSource___iadd__()



# Generated at 2022-06-13 15:50:19.611010
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        pass

    source = _EventSource()
    source += handler1
    source += handler2

    source.fire()

# Generated at 2022-06-13 15:50:26.442748
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Arrange
    event_source = _EventSource()
    def valid_handler(self, *args, **kwargs):
        pass
    def invalid_handler():
        pass

    # Assert
    assert event_source._handlers == set()
    assert event_source._handlers.__len__() == 0

    # Act
    event_source += valid_handler
    event_source += invalid_handler
    event_source += valid_handler

    # Assert
    assert event_source._handlers == {valid_handler}
    assert event_source._handlers.__len__() == 1


# Generated at 2022-06-13 15:50:38.130510
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # The tests of AnsibleCollectionConfig properties that depend on the class's _AnsibleCollectionConfig metaclass
    # require a concrete instance of the metaclass type
    cls = AnsibleCollectionConfig()

    # Define the event receivers that set flags in the scope around the call to cls.on_collection_load.fire
    # Every time fire is called, each handler sets the corresponding flag to True
    fired_handler_1 = False
    fired_handler_2 = False
    fired_handler_3 = False

    def handler_1(_):
        nonlocal fired_handler_1
        fired_handler_1 = True

    def handler_2(_):
        nonlocal fired_handler_2
        fired_handler_2 = True

    def handler_3(_):
        nonlocal fired_handler_3
        fired_handler_3 = True



# Generated at 2022-06-13 15:50:43.197247
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def func1():
        pass

    def func2():
        pass

    es += func1
    assert func1 in es._handlers

    es += func2
    assert func2 in es._handlers

    es += func1
    assert func1 in es._handlers

    return


# Generated at 2022-06-13 15:50:51.419485
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import copy
    import pytest

    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.six import with_metaclass

    # class _EventSource:
    #     def __init__(self):
    class Mock_EventSource:
        def __init__(self):
            self._handlers = set()
        def __iadd__(self, handler):
            if not callable(handler):
                raise ValueError('handler must be callable')
            self._handlers.add(handler)
            return self
        def __isub__(self, handler):
            try:
                self._handlers.remove(handler)
            except KeyError:
                pass
            return self

# Generated at 2022-06-13 15:50:55.577557
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.utils.collection_loader._target._text.converters import to_bytes
    from ansible.utils.collection_loader._target.util.callback_loader import PluginsLoader
    from ansible.utils.collection_loader._target.util.callback_plugins import callback_loader
    from ansible.utils.collection_loader._target.util.plugins import plugin_loader

    import collections
    import copy
    import os
    import os.path
    import tempfile
    import types

    import pytest

    class MyPluginClass:
        pass


# Generated at 2022-06-13 15:50:58.293660
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()

    # Test callable handler
    event_source += handler
    assert handler in event_source._handlers

    # Test ValueError raised with invalid handler
    try:
        event_source += 1
        assert False, 'ValueError not raised'
    except ValueError:
        pass
    except Exception as ex:
        assert False, 'unexpected exception {0}'.format(type(ex))

# Generated at 2022-06-13 15:51:04.597253
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    vs = _EventSource()
    vs += lambda x: x
    assert len(vs._handlers) == 1



# Generated at 2022-06-13 15:51:08.113851
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _es = _EventSource()
    _es += lambda : 1
    assert len(_es._handlers) == 1
    assert callable(_es._handlers.pop())


# Generated at 2022-06-13 15:51:19.703515
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def handler1(msg):
        raise RuntimeError('handler1 failed')

    def handler2(msg):
        raise SyntaxError('handler2 failed')

    def handler3(msg):
        raise ValueError('handler3 failed')

    event += handler1
    event += handler2
    event += handler3

    try:
        event.fire('test message')
        assert False, 'expected to raise exception'
    except ValueError as e:
        assert 'handler3 failed' in to_text(e)

    try:
        event.fire('test message')
        assert False, 'expected to raise exception'
    except SyntaxError as e:
        assert 'handler2 failed' in to_text(e)


# Generated at 2022-06-13 15:51:23.949985
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    # with a valid handler
    test_case = 1
    def test_handler():
        ''' test handler '''
        pass
    event_source = _EventSource()
    event_source += test_handler
    assert test_handler in event_source._handlers

    # with non-callable arguments, expecting an error
    test_case = 2
    event_source = _EventSource()
    try:
        event_source += 'abc'
    except ValueError:
        pass
    else:
        raise AssertionError('event_source += with non-callable argument should have raised ValueError')


# Generated at 2022-06-13 15:51:33.470806
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Error(Exception):
        pass

    # define a simple event handler
    def handler(message):
        print(message)

    # define an event handler that raises an exception
    def error(message):
        raise Error()

    # create an event source
    source = _EventSource()

    # add some handlers
    source += handler
    source += handler
    source += handler

    # fire the event
    source.fire('successful test')

    # add an error handler
    source += error

    # fire the event again
    try:
        source.fire('failing test')
    except Error:
        # we expect the handler to raise an exception, so we catch it and move on
        pass

# Generated at 2022-06-13 15:51:39.323929
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Foo:
        def bar(self, *args, **kwargs):
            self._called = True

    foo = Foo()
    assert not hasattr(foo, '_called')

    event_source = _EventSource()
    event_source += foo.bar

    event_source.fire()
    assert hasattr(foo, '_called')

# Generated at 2022-06-13 15:51:47.146129
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test _EventSource.fire()

    evt_source = _EventSource()

    def handler(*args):
        assert args == (1, 2, 3)

    evt_source += handler
    evt_source.fire(1, 2, 3)

    try:
        evt_source -= handler
    except Exception as ex:
        assert False, 'unexpected exception: %s' % ex

    try:
        evt_source.fire(1, 2, 3)
    except TypeError:
        assert False, 'Unexpected exception'

# Generated at 2022-06-13 15:51:53.847032
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def event_handler(x):
        pass

    event_source = _EventSource()
    event_source += event_handler
    n_handlers = len(event_source._handlers)
    assert n_handlers == 1

    event_source += event_handler
    n_handlers = len(event_source._handlers)
    assert n_handlers == 1

    event_source += event_handler
    n_handlers = len(event_source._handlers)
    assert n_handlers == 1



# Generated at 2022-06-13 15:52:05.626185
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # mock the ansible collection config class
    class MockAnsibleCollectionConfig(_AnsibleCollectionConfig):
        pass

    # create a new event source class to test
    event_source = MockAnsibleCollectionConfig._EventSource()

    # create a mock handler class
    class MockHandler:
        def __init__(self, handler_id):
            self.handler_id = handler_id
            self.call_count = 0
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.call_count += 1

    # create a handler that ignores its parameters
    handler1 = MockHandler(1)
    event_source += handler1

    # create a handler that raises an exception
   

# Generated at 2022-06-13 15:52:14.922995
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    class MyException(Exception):
        pass

    def handler1(a, b):
        return a + b

    def handler2(a, b):
        raise MyException('This exception was raised on purpose')

    def handler3(a, b):
        return a + b + 1

    def bad_handler(a, b):
        return a + b + 1 + 'z'

    event_source += handler1
    event_source += handler2
    event_source += handler3

    result = event_source.fire(1, 2)
    assert result is None

    try:
        event_source.fire(1, 2)
    except MyException:
        pass
    else:
        assert False, 'MyException was not raised'


# Generated at 2022-06-13 15:52:32.107516
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test with no handlers
    sut = _EventSource()
    sut.fire()

    # test with handler that fails
    sut = _EventSource()
    sut += lambda: 1 / 0
    try:
        sut.fire(1)
        assert False, "unexpected"
    except ZeroDivisionError:
        pass

    # test with handler that fails, but not due to an exception
    sut = _EventSource()
    sut += lambda: 1 / 0
    sut._on_exception = lambda *_a, **_kw: False
    sut.fire(2)

    # test with a handler that works
    sut = _EventSource()
    value = [0]
    sut += lambda x: value.__setitem__(0, x)
    sut.fire(3)


# Generated at 2022-06-13 15:52:38.521940
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler():
        pass

    event_source += handler
    assert len(event_source._handlers) == 1

    event_source += handler
    assert len(event_source._handlers) == 2

    with pytest.raises(ValueError):
        event_source += 5


# Generated at 2022-06-13 15:52:47.795157
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MockHandler:
        def __init__(self, write_value):
            self.call_count = 0
            self.write_value = write_value

        def __call__(self, *args, **kwargs):
            self.call_count += 1
            print(self.write_value)

        def raise_exception(self):
            raise AssertionError('handler raised exception')

    mock_handler1 = MockHandler('mock_handler1')
    mock_handler2 = MockHandler('mock_handler2')

    mock_event_source = _EventSource()
    mock_event_source += mock_handler1
    mock_event_source += mock_handler2

    # test callable handlers in mock_event_source
    mock_event_source.fire()
    assert mock_handler1.call_count == 1

# Generated at 2022-06-13 15:52:58.178261
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # check that handler registered with += is called
    source = _EventSource()
    called = False

    def handler():
        nonlocal called
        called = True

    source += handler
    source.fire()
    assert called

    # check that handler registered with -= is not called
    called = False
    source -= handler
    source.fire()
    assert not called

    # check handler registered with += is called even if another handler throws
    # and check handler exception is not caught
    called = False

    def throwing_handler():
        raise RuntimeError()

    try:
        source += throwing_handler
        source.fire()
    except RuntimeError:
        pass

    assert called

    # check that calling -= on handler not registered does not raise
    source -= handler
    source -= throwing_handler

# Generated at 2022-06-13 15:53:07.552441
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEvent(object):
        pass

    class EventSourceTest(object):
        def __init__(self):
            # Create two event sources
            self.test_event = TestEvent()
            self.test_event2 = TestEvent()
            self.events = {  'test_event': self.test_event,
                             'test_event2': self.test_event2}
            self.test_values = [1, 2, 3]

            for event_name, event in self.events.items():
                # Register event handlers
                if event_name == 'test_event':
                    event += self.handle_test_event
                if event_name == 'test_event2':
                    event += self.handle_test_event2


# Generated at 2022-06-13 15:53:08.201863
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    pass

# Generated at 2022-06-13 15:53:14.664758
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Stub:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True

    stub = Stub()

    event_source = _EventSource()
    event_source += stub

    event_source.fire()
    assert stub.called



# Generated at 2022-06-13 15:53:17.166775
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # This is for control-level compatibility testing.
    cls = _EventSource()
    cls.fire(True)



# Generated at 2022-06-13 15:53:20.456712
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    handler = lambda: True
    event_source += handler
    assert len(event_source._handlers) == 1
    assert handler in event_source._handlers


# Generated at 2022-06-13 15:53:22.281301
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    source += lambda: None
    source += lambda: None
    source.fire()


# Generated at 2022-06-13 15:53:43.408829
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert not es._handlers

    def handler(a, b):
        pass

    es += handler
    assert handler in es._handlers

    es += handler

    # multiple additions should only add it once
    assert len(es._handlers) == 1

    def handler_2(c, d):
        pass

    es += handler_2
    assert handler_2 in es._handlers

    assert handler in es._handlers



# Generated at 2022-06-13 15:53:47.110945
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler():
        pass

    es += handler
    assert handler in es._handlers
    es += handler
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:53:55.117340
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import mock

    class DummyHandler:
        def __init__(self):
            self.calls = []

        def handler(self, *args):
            self.calls.append((args))

    dummy_handler1 = DummyHandler()
    dummy_handler2 = DummyHandler()

    es = _EventSource()
    es += dummy_handler1.handler
    es += dummy_handler2.handler

    es.fire(1, 2, 3)

    assert dummy_handler1.calls == [(1, 2, 3,)]
    assert dummy_handler2.calls == [(1, 2, 3,)]
    dummy_handler1.calls = []
    dummy_handler2.calls = []

    # test that an exception in a handler does not prevent other handlers from being invoked

# Generated at 2022-06-13 15:54:05.013229
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    events = _EventSource()
    fire_count = [0]
    fire_arg = [None]
    fire_kwarg = [None]

    # this decorator will let us see if the exception make it out of the handler or not
    def validate_exception(handler):
        def wrapper(arg, kwarg=None):
            fire_count[0] += 1
            fire_arg[0] = arg
            fire_kwarg[0] = kwarg
            raise RuntimeError('an error')

        return wrapper

    @validate_exception
    def handler1(arg, kwarg=None):
        pass

    @validate_exception
    def handler2(arg, kwarg=None):
        pass

    events += handler1
    events += handler2


# Generated at 2022-06-13 15:54:11.606768
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Arrange
    test_event_source = _EventSource()
    test_event_handler = lambda: None

    # Act
    test_event_source += test_event_handler

    # Assert
    assert callable(test_event_handler)
    assert test_event_handler in test_event_source._handlers


# Generated at 2022-06-13 15:54:20.274907
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsrc = _EventSource()

    class FakeHandler:
        def __init__(self):
            self.fired = []

        def __call__(self, *args, **kwargs):
            self.fired.append((self, args, kwargs))

    h1 = FakeHandler()
    h2 = FakeHandler()
    h3 = FakeHandler()

    eventsrc.fire()
    assert len(h1.fired) == 0
    assert len(h2.fired) == 0
    assert len(h3.fired) == 0

    eventsrc += h1
    eventsrc.fire()
    assert len(h1.fired) == 1
    assert len(h2.fired) == 0
    assert len(h3.fired) == 0

    eventsrc += h2
    eventsrc += h3
    eventsrc.fire

# Generated at 2022-06-13 15:54:23.846725
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import collections.abc

    class MyTarget(object):
        def __init__(self):
            self.f = _EventSource()

    target = MyTarget()
    assert isinstance(target.f, collections.abc.Callable)


# Generated at 2022-06-13 15:54:29.304803
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler1():
        pass

    def handler2():
        pass

    es += handler1

    assert es._handlers == {handler1}

    es += handler1

    assert es._handlers == {handler1}

    es += handler2

    assert es._handlers == {handler1, handler2}

    with raises(ValueError):
        es += None

    with raises(ValueError):
        es += 'not callable'



# Generated at 2022-06-13 15:54:35.487240
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        pass

    es += handler1
    es += handler2

    es.fire()

    es -= handler1
    es.fire()

    def handler3(*args, **kwargs):
        raise Exception()

    es += handler3

    raised = False

    try:
        es.fire()
    except Exception:
        raised = True

    assert raised



# Generated at 2022-06-13 15:54:46.535265
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # test that nothing happens if _EventSource is empty
    event_source.fire()

    # test that a callable which does not raise an exception is successful
    success = False
    handler_success = lambda: setattr(handler_success, 'success', True)
    event_source += handler_success
    event_source.fire()
    assert handler_success.success

    # test that a callable which raises an exception is caught but re-raised
    success = False
    handler_exception = lambda: 1 / 0
    handler_exception.exception_thrown = False
    event_source += handler_exception
    try:
        event_source.fire()
    except ZeroDivisionError:
        handler_exception.exception_thrown = True
    assert handler_exception.exception

# Generated at 2022-06-13 15:55:24.360391
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # this event source is not actually used during a collection load so the
    # arguments passed in when fired would be meaningless.  It is only here
    # to allow testing of this method.
    class EventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            # the handler that raises an exception will be called twice by both
            # the negative and positive tests.  We only want to re-raise the
            # exception for the second time it is called in the negative test
            # which is the second time it is called for the positive test.
            if not getattr(handler, '_called', None):
                handler._called = True
                return False
            return True


# Generated at 2022-06-13 15:55:36.018136
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_set = {1, 2, 3, 4}
    test_list = [1, 2, 3, 4]
    test_tuple = (1, 2, 3, 4)
    test_dict = {1: 1, 2: 2, 3: 3, 4: 4}
    test_kwargs = {1: 2, 3: 4}
    test_args = [4, 3, 2, 1]

    class TestCollection:
        def __init__(self, test_set, test_list, test_tuple, test_dict):
            self.result_set = set()
            self.result_list = []
            self.result_tuple = ()
            self.result_dict = {}

            self.test_set = test_set
            self.test_list = test_list
            self.test_tuple

# Generated at 2022-06-13 15:55:46.374848
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_handler(index):
        test_handler.index = index

    x = _EventSource()
    x += test_handler
    test_handler.index = 0

    x.fire(1)
    assert test_handler.index == 1

    # add another handler
    test_handler2_index = 0

    def test_handler2():
        nonlocal test_handler2_index
        test_handler2_index += 1

    x += test_handler2
    x.fire()
    assert test_handler2_index == 1

    # remove a handler
    x -= test_handler
    x.fire()
    assert test_handler.index == 1
    assert test_handler2_index == 2



# Generated at 2022-06-13 15:55:50.755917
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # any non-callable handler should cause ValueError
    event_source = _EventSource()
    try:
        event_source += object()
        assert False, 'non-callable handler should cause ValueError'
    except ValueError:
        pass

    # should not throw an exception
    event_source += lambda: None



# Generated at 2022-06-13 15:55:56.541141
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=protected-access
    # pylint: disable=unused-argument
    import unittest2 as unittest

    class TestEventSource(unittest.TestCase):
        def test_success(self):
            results = []
            def push_result(result):
                results.append(result)

            event_source = _EventSource()
            event_source.fire(1, 2, 3)
            event_source += push_result

            self.assertEqual(results, [])

            event_source.fire(4, 5, 6)
            self.assertEqual(results, [(4, 5, 6)])

            event_source.fire(7, 8, 9, 10)

# Generated at 2022-06-13 15:56:00.515956
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    R = []

    def t(v):
        R.append(v)

    es = _EventSource()
    es += t

    assert R == []

    es.fire(1)
    assert R == [1]

    es -= t

    es.fire(2)
    assert R == [1]

# Generated at 2022-06-13 15:56:02.841865
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Testing if no exception is raised
    eventsource = _EventSource()
    eventsource.fire(1,2,3)



# Generated at 2022-06-13 15:56:10.580005
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test that no exception is raised
    empty_event_source = _EventSource()
    empty_event_source.fire()

    # test a single handler
    def test_handler(*args, **kwargs):
        assert args == (1, 2, 3)
        assert kwargs == {'a': 4, 'b': 5}

    event_source = _EventSource()
    event_source += test_handler
    event_source.fire(1, 2, 3, a=4, b=5)

    # test multiple handlers, where one handler raises an exception
    def test_handler(*args, **kwargs):
        assert args == (1, 2, 3)
        assert kwargs == {'a': 4, 'b': 5}

    def test_exception_handler(*args, **kwargs):
        raise Exception()



# Generated at 2022-06-13 15:56:22.075508
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _DummyHandler:
        def __init__(self, name):
            self._name = name

        def __call__(self, *args, **kwargs):
            print('%s(%r, %r)' % (self._name, args, kwargs))

    def _exception(handler, exc, *args, **kwargs):
        print('%s: exception: %r' % (handler._name, exc))
        return False

    evt = _EventSource()
    evt._on_exception = _exception

    evt += _DummyHandler('handler1')
    evt += _DummyHandler('handler2')

    print('fire without args')
    evt.fire()

    print('fire with args')
    evt.fire('hello')

    print('fire with kwargs')


# Generated at 2022-06-13 15:56:30.234277
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    callable_handlers = [lambda: None, lambda: None, lambda: None]

    # add each of them individually
    for handler in callable_handlers:
        event_source += handler

    # remove the first one and make sure it is gone
    event_source -= callable_handlers[0]
    del callable_handlers[0]

    # and make sure it does not exist anymore
    assert callable_handlers != event_source._handlers

    # add multiple handlers at once
    event_source += callable_handlers[1:]

    # and make sure all the handlers exist
    assert callable_handlers == event_source._handlers

    # add a non-callable handler and make sure it raises an ValueError
    non_callable_handler = 'this must raise'

# Generated at 2022-06-13 15:57:36.690191
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """_EventSource: verify that event handlers are called in order"""

    event_source = _EventSource()

    global_calls = []

    def handler1(*args, **kwargs):
        global_calls.append(1)

    def handler2(*args, **kwargs):
        global_calls.append(2)

    event_source += handler1
    event_source += handler2

    event_source.fire()

    assert global_calls == [1, 2], "handlers not called in order"

# Generated at 2022-06-13 15:57:46.972585
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    # "__iadd__" sets the value of an instance of _EventSource
    # The value is a set of functions
    def eventFunc_1():
        pass

    def eventFunc_2():
        pass

    def eventFunc_3():
        pass

    eventSource = _EventSource()
    eventSource += eventFunc_1
    eventSource += eventFunc_2

    assert eventSource._handlers == {eventFunc_1, eventFunc_2}

    # if the same function is added twice the set will only contain it once
    eventSource += eventFunc_2
    eventSource += eventFunc_3
    eventSource += eventFunc_3

    assert eventSource._handlers == {eventFunc_1, eventFunc_2, eventFunc_3}


# Generated at 2022-06-13 15:57:56.088368
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    my_eventsource = _EventSource()
    class DummyHandler(object):
        def __init__(self):
            self._rv_called = False
            self._rv_called_exception = None
            self._rv_calls = 0
            self._rv_calls_args = None
            self._rv_calls_kwargs = None

        def __call__(self, *args, **kwargs):
            self._rv_called = True
            self._rv_calls += 1
            self._rv_calls_args = args
            self._rv_calls_kwargs = kwargs

            if kwargs.get('raise_ex', False):
                raise Exception('test exception')

    # all handlers are called
    handler1 = DummyHandler()

# Generated at 2022-06-13 15:57:58.631949
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    _event_source = _EventSource()
    success = False
    def handler(result):
        nonlocal success
        success = result
    _event_source += handler
    _event_source.fire(True)
    assert success is True


# Generated at 2022-06-13 15:58:03.368345
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class A:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True

    x = _EventSource()
    a = A()
    x += a
    x.fire()
    assert a.called

# Generated at 2022-06-13 15:58:09.859182
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def exception_handler(ex, *args, **kwargs):
        raise ex

    eventsource = _EventSource()
    eventsource._on_exception = exception_handler

    def handler(param):
        # param can be anything, in this test it is a string
        assert param == "arg"

    eventsource += handler
    eventsource.fire("arg")

    # Must not raise since handler was unsubscribed
    eventsource -= handler
    eventsource.fire("arg")

# Generated at 2022-06-13 15:58:16.736091
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_value = []

    def handler1(*args, **kwargs):
        test_value.append(('handler1', args, kwargs))

    def handler2(*args, **kwargs):
        test_value.append(('handler2', args, kwargs))

    def handler3(*args, **kwargs):
        raise ValueError('handler3 exception')

    def handler4(*args, **kwargs):
        test_value.append(('handler4', args, kwargs))

    def handler5(*args, **kwargs):
        raise ValueError('handler5 exception')

    event = _EventSource()
    event += handler1
    event += handler2
    event += handler3
    event += handler4
    event += handler5


# Generated at 2022-06-13 15:58:19.607404
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(x):
        if x != 1:
            raise ValueError('1')

    def handler2(x):
        if x != 2:
            raise ValueError('2')

    es = _EventSource()
    es += handler1
    es += handler2

    es.fire(1)
    es.fire(2)

# Generated at 2022-06-13 15:58:22.240442
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    handler = lambda *args, **kwargs: None


# Generated at 2022-06-13 15:58:29.485224
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils._text import to_text
    from collections import namedtuple
    from io import StringIO

    MockLogger = namedtuple('MockLogger', ['warning'])

    def _load_module(args):
        return 37

    def _handler_1(args):
        return args

    def _handler_2(args):
        return args

    def _handler_3(args):
        raise Exception('handler_3 exception')

    def _handler_exception_silent(ex, args):
        return True

    def _handler_exception_raises(ex, args):
        return False
