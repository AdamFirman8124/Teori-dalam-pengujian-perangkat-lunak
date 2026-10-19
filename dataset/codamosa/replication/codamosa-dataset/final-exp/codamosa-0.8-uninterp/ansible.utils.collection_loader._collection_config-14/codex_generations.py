

# Generated at 2022-06-13 15:49:10.034181
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def test_handler():
        pass

    event_source.fire()
    assert not event_source._handlers

    event_source += test_handler
    assert event_source._handlers == {test_handler}

    try:
        event_source += test_handler
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"

    try:
        event_source += ''
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"

    try:
        event_source += None
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"



# Generated at 2022-06-13 15:49:16.142313
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def event_handler1(sender, arg):
        messages.append('event_handler1: %s' % (arg,))

    def event_handler2(sender, arg):
        messages.append('event_handler2: %s' % (arg,))

    messages = []

    s = _EventSource()
    s += event_handler1
    s += event_handler2
    s.fire('hello')

    assert messages == ['event_handler1: hello', 'event_handler2: hello']



# Generated at 2022-06-13 15:49:22.403843
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSourceTest(_EventSource):
        def __init__(self):
            super(EventSourceTest, self).__init__()

            self.fired = False
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.fired = True
            self.args = args
            self.kwargs = kwargs

    test = EventSourceTest()
    test.fire('foo')

    assert test.fired
    assert test.args == ('foo', )
    assert test.kwargs == {}



# Generated at 2022-06-13 15:49:25.425084
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    event_source = _EventSource()

    with pytest.raises(ValueError):
        event_source.__iadd__('handler')

    event_source.__iadd__(handler)

    # no exception expected
    event_source.__iadd__(handler)



# Generated at 2022-06-13 15:49:26.477433
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event += fire_handler
    event.fire()


# Generated at 2022-06-13 15:49:34.460984
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(event_name, *args, **kwargs):
        rv.append((event_name, args, kwargs))

    rv = []
    e = _EventSource()
    e += handler

    e.fire('foo', 'bar', baz='qux')
    assert rv == [('foo', ('bar',), {'baz': 'qux'})]

    rv.clear()
    e.fire('bar', 'baz', qux='foo')
    assert rv == [('bar', ('baz',), {'qux': 'foo'})]

    e -= handler
    rv.clear()
    e.fire('bar', 'baz', qux='foo')
    assert rv == []


# Generated at 2022-06-13 15:49:42.818118
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible_test import _util
    from inspect import getfile
    from types import ModuleType

    def _get_function_name(function):
        # Function objects have no name attribute in Python 2
        return function.__name__

    def _assert_event_source_has_handler(event_source, member_name, handler):
        assert event_source[member_name] == handler, 'the specified handler was not added'

    event_source = _EventSource()
    handler = _util.mock.sentinel.handler
    event_source += handler
    _assert_event_source_has_handler(event_source._handlers, _get_function_name(handler), handler)

    # idempotent
    event_source += handler

# Generated at 2022-06-13 15:49:46.195535
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def func():
        pass

    event = _EventSource()
    event += func
    assert func in event._handlers

    event += func
    assert len(event._handlers) == 1



# Generated at 2022-06-13 15:49:50.169448
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    def event_handler(*args, **kwargs):
        pass

    event_source += event_handler
    event_source -= event_handler
    event_source.fire()

# Generated at 2022-06-13 15:49:53.752878
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e1 = _EventSource()
    e2 = _EventSource()
    e2.fire(3)
    e2 += e1
    e2.fire(3)
    e1.fire(3)
    e2 += e1
    e2 -= e1
    e1.fire(3)


# Generated at 2022-06-13 15:50:03.294288
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def test1():
        def test2():
            pass

        test3 = 3

        event_source = _EventSource()
        assert event_source._handlers == set()

        event_source += test1
        assert event_source._handlers == {test1}

        event_source += test2
        assert event_source._handlers == {test1, test2}

        try:
            event_source += test3
            assert False
        except ValueError:
            assert True

    test1()



# Generated at 2022-06-13 15:50:05.565879
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test that the callback function is called.
    def test1(x):
        test1.called = True

    test1.called = False
    es = _EventSource()
    es += test1
    es.fire()
    assert test1.called

# Generated at 2022-06-13 15:50:15.931809
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _EventSourceInit(object):
        def __init__(self):
            self._handlers = set()

    event_source_init = _EventSourceInit()

    event_source = _EventSource.__new__(_EventSource)
    event_source.__dict__ = event_source_init.__dict__

    event_source += lambda *x, **y: None
    assert len(event_source._handlers) == 1

    event_source += lambda *x, **y: None
    assert len(event_source._handlers) == 2

    assert event_source.__iadd__(lambda *x, **y: None) is event_source

    assert event_source.__isub__(lambda *x, **y: None) is event_source

    assert len(event_source._handlers) == 2

    event

# Generated at 2022-06-13 15:50:26.138917
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Mock():
        def __init__(self, value):
            self.value = value

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            raise Exception('{0}'.format(self.value))

    raise_1 = Mock('raise_1')
    reraise_1 = Mock('reraise_1')

    event_source = _EventSource()
    event_source += raise_1
    event_source += reraise_1

    try:
        event_source.fire('one', 'two', extra='three')
    except Exception as e:
        assert str(e) == 'reraise_1'

    assert raise_1.args == ('one', 'two')
    assert raise_1.kwargs == dict(extra='three')


# Generated at 2022-06-13 15:50:28.589448
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += lambda x: x
    assert callable(event_source._handlers.pop())



# Generated at 2022-06-13 15:50:31.531628
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    es = _EventSource()

    callback = lambda : None

    es += callback

    try:
        es += 1
        assert False, 'failed to raise'
    except ValueError:
        pass



# Generated at 2022-06-13 15:50:39.218442
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # metaclass is not applied to this class when running unit tests
    _AnsibleCollectionConfig.__init__(AnsibleCollectionConfig, '', ())

    def handler1(x):
        assert x == 'foo'

    def handler2(x):
        assert x == 'foo'

    def handler3(x):
        assert x == 'foo'
        raise RuntimeError('unexpected runtime error')

    AnsibleCollectionConfig.on_collection_load += handler1
    AnsibleCollectionConfig.on_collection_load += handler2
    AnsibleCollectionConfig.on_collection_load += handler3

    try:
        AnsibleCollectionConfig.on_collection_load.fire('foo')
    except RuntimeError as ex:
        assert str(ex) == 'unexpected runtime error'

    AnsibleCollectionConfig.on_collection_load -= handler3

# Generated at 2022-06-13 15:50:48.687960
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert set() == event_source._handlers

    def handler_1(event_source, *args, **kwargs):
        raise ValueError('handler_1 has been invoked')

    # add handler_1 to event_source
    event_source += handler_1

    assert 1 == len(event_source._handlers)
    assert event_source in event_source._handlers

    def handler_2(event_source, *args, **kwargs):
        raise ValueError('handler_2 has been invoked')

    # add handler_2 to event_source
    event_source += handler_2

    assert 2 == len(event_source._handlers)
    assert handler_1 in event_source._handlers
    assert handler_2 in event_source._handlers


# Generated at 2022-06-13 15:50:52.811685
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # on_collection_load = _EventSource()

    # on_collection_load += print(1)
    # on_collection_load += print(2)
    # on_collection_load += print(3)

    # on_collection_load.fire()

    pass

# Generated at 2022-06-13 15:51:00.629482
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_A(*args, **kwargs):
        pass

    def handler_B(*args, **kwargs):
        raise Exception()

    def handler_C(*args, **kwargs):
        raise Exception()

    event_source = _EventSource()
    assert len(event_source._handlers) == 0

    event_source += handler_A
    assert len(event_source._handlers) == 1
    assert handler_A in event_source._handlers

    event_source += handler_B
    assert len(event_source._handlers) == 2
    assert handler_B in event_source._handlers

    event_source -= handler_A
    assert len(event_source._handlers) == 1
    assert handler_A not in event_source._handlers
    assert handler_B in event_source._handlers

   

# Generated at 2022-06-13 15:51:08.370219
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import pytest
    test_object = _EventSource()
    with pytest.raises(ValueError):
        test_object.__iadd__(1)
    test_object.__iadd__(lambda: None)



# Generated at 2022-06-13 15:51:19.805515
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestClass:
        def __init__(self, id):
            self.id = id

        def handler(self, *args, **kwargs):
            return self.id

        def raise_exception(self, *args, **kwargs):
            raise RuntimeError('test' + str(self.id))

    def test_callable(thing, index):
        # The callable should be the TestClass instance, the args should be the collections list, and the kwargs should be empty
        if thing != test_objects[index]:
            raise AssertionError('Expected %s but instead got %s for TestClass[%d].handler()' % (test_objects[index], thing, index))

# Generated at 2022-06-13 15:51:31.984831
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class O1:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True

    class O2:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True

    class O3:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            raise Exception('test exception')

    source = _EventSource()
    source += O1()
    source += O2()
    source += O3()

    try:
        source.fire()
    except Exception:
        pass

    assert source._handlers[0].called
    assert source._hand

# Generated at 2022-06-13 15:51:35.442851
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # setup
    es = _EventSource()

    # execute
    es += lambda: print('foo')

    # verify
    assert len(es._handlers) == 1
    assert callable(es._handlers.pop())



# Generated at 2022-06-13 15:51:47.146904
# Unit test for method fire of class _EventSource
def test__EventSource_fire():  # noqa
    import traceback
    import sys

    class _SomeClass:
        def __init__(self):
            self.fired = False
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.fired = True
            self.args = args
            self.kwargs = kwargs

    def _get_exception_error(ex):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        error = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        return error

    def _get_exception_tb(ex):
        exc_type

# Generated at 2022-06-13 15:51:57.461129
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest(object):
        #set up the event source
        event = _EventSource()

        def __init__(self):
            self.test_value = 10

        def handle_event(self, value):
            self.test_value += value

        def handle_exception(self, exc, *args, **kwargs):
            if isinstance(exc, ValueError):
                return False

            return True

        def run_test(self):
            self.event += self.handle_event
            self.event._on_exception = self.handle_exception
            
            self.event.fire(10)
            assert self.test_value == 20, "test_value should be 20"
            self.event.fire(20)
            assert self.test_value == 40, "test_value should be 40"
           

# Generated at 2022-06-13 15:51:58.650088
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert not es._handlers

    def func():
        pass

    es += func
    assert es._handlers



# Generated at 2022-06-13 15:52:08.463926
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Test:
        def __init__(self):
            self.x = None

    x = Test()
    y = Test()
    z = Test()

    es = _EventSource()

    # Test __iadd__ correct operation
    es += x.__setattr__
    es += y.__setattr__
    es += z.__setattr__

    es.fire('x', 1)

    assert x.x == 1
    assert y.x == 1
    assert z.x == 1

    # Test __iadd__ validation
    try:
        es += 2
        assert False
    except ValueError:
        assert True

    # Test __isub__
    es -= y.__setattr__
    es.fire('x', 2)

    assert x.x == 2
    assert y.x == 1

# Generated at 2022-06-13 15:52:17.510876
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # no error
    event_source.fire()

    # no error
    def foo(a, b, c):
        pass

    event_source += foo
    event_source.fire()

    # error
    def foo2(a, b, c):
        raise Exception()

    event_source += foo2
    try:
        event_source.fire()
    except:
        pass
    else:
        assert False

    # no error
    def foo3(a, b, c):
        def _on_exception(handler, exc, *args, **kwargs):
            return False
        event_source._on_exception = _on_exception
        raise Exception()

    event_source += foo3
    event_source.fire()

# Generated at 2022-06-13 15:52:21.965198
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(s):
        assert s == 'pass'

    def handler2(s):
        assert s == 'pass'
        raise Exception('test')

    def handler3(s):
        assert s == 'pass'

    source = _EventSource()
    source += handler1
    source.fire('pass')

    source += handler2
    source += handler3
    source.fire('pass')

    source -= handler2
    source.fire('pass')



# Generated at 2022-06-13 15:52:30.197086
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda x: print(x)
    assert len(es._handlers) == 1

# Generated at 2022-06-13 15:52:42.701128
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    class Recorder:
        def __init__(self):
            self.args = []
            self.kwargs = []

        def __call__(self, *args, **kwargs):
            self.args.extend(args)
            self.kwargs.update(kwargs)

    recorder = Recorder()

    event_source += recorder
    event_source.fire(1, 2, 3, name='value')

    try:
        event_source += None
        raise AssertionError('event_source += None should raise a ValueError')
    except ValueError:
        pass

    try:
        event_source -= None
        raise AssertionError('event_source -= None should raise a ValueError')
    except ValueError:
        pass


# Generated at 2022-06-13 15:52:44.361204
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += print
    assert callable(e._handlers.pop())



# Generated at 2022-06-13 15:52:53.355499
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEvents(object):
        def __init__(self):
            self.f1 = _EventSource()

    me = MyEvents()

    def handler1(a):
        if not a == 3:
            raise ValueError("Wrong value for a")

    def handler2(a):
        if not a == 3:
            raise ValueError("Wrong value for a")

    me.f1 += handler1
    me.f1 += handler2

    me.f1.fire(3)
    try:
        me.f1.fire(1)
    except ValueError as e:
        assert str(e) == "Wrong value for a"
    me.f1 -= handler1
    me.f1.fire(3)

# Generated at 2022-06-13 15:53:02.214012
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Helper variables
    events = 0
    errors = 0

    # Event handlers
    def handle_event(x):
        nonlocal events
        events += 1
    def handle_error(x):
        nonlocal errors
        errors += 1

    # Instantiate the event source
    es = _EventSource()

    # Add the event handlers
    es += handle_event
    es += handle_error
    es += handle_event
    es += handle_error
    es += handle_event

    # Fire the event source
    es.fire()

    # Make sure the handlers were called
    assert events == 3
    assert errors == 2

    # Remove the error handler and fire again
    es -= handle_error
    es.fire()

    # Make sure the error handler wasn't called
    assert events == 6
    assert errors == 2


#

# Generated at 2022-06-13 15:53:05.586300
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def callback(sender, **kwargs):
        pass

    source = _EventSource()
    source.fire(sender='source', msg='successfully fired')
    source += callback
    source.fire(sender='source', msg='successfully fired')



# Generated at 2022-06-13 15:53:10.849909
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Arrange
    source = _EventSource()

    class A:
        def __init__(self):
            self.count = 0

        def handler(self, *args, **kwargs):
            self.count += 1

    class B(A):
        def handler(self, *args, **kwargs):
            super(B, self).handler(*args, **kwargs)

    a = A()
    source += a.handler
    b = B()
    source += b.handler

    # Act
    source.fire()

    # Assert
    assert a.count == 1
    assert b.count == 1

# Generated at 2022-06-13 15:53:22.163671
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Fired(Exception):
        pass

    # No handlers defined
    source = _EventSource()
    source.fire()

    # _on_exception does not raise
    def handler(source, *args, **kwargs):
        raise Fired

    source = _EventSource()
    source += handler
    source._on_exception = lambda source, exc, *args, **kwargs: False
    source.fire()

    # _on_exception raises
    try:
        source = _EventSource()
        source += handler
        source._on_exception = lambda source, exc, *args, **kwargs: True
        source.fire()
    except Fired:
        pass
    else:
        assert False, 'Exception should have been raised'

# Generated at 2022-06-13 15:53:32.242835
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Method fire of class _EventSource does not throw an exception if all handlers
    # callable.
    es = _EventSource()
    es += lambda: None
    es += lambda: None
    es.fire()

    # Method fire of class _EventSource does not throw an exception if all handlers
    # callable and can accept arguments.
    es.fire(1, 2, 3)

    # Method fire of class _EventSource throws an exception if one of the handlers
    # is not callable.
    es += 42
    try:
        es.fire()
        assert False
    except Exception:
        assert True
    es -= 42

    # Method fire of class _EventSource throws an exception if one of the handlers
    # throws an exception.
    es += lambda: 1 / 0

# Generated at 2022-06-13 15:53:37.693061
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    handler1 = lambda: None
    handler2 = lambda: None

    es += handler1

    def handler3(name='foo', *args, **kwargs):
        pass

    es += handler3

    assert handler1 in es._handlers
    assert handler3 in es._handlers
    assert handler2 not in es._handlers

    assert len(es._handlers) == 2



# Generated at 2022-06-13 15:54:01.455034
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return isinstance(exc, KeyError)

    event_source = MyEventSource()

    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        raise Exception()

    def handler3(*args, **kwargs):
        raise KeyError()

    event_source += handler1
    event_source += handler2
    event_source += handler3

    event_source.fire()

    assert handler1 in event_source._handlers
    assert handler2 not in event_source._handlers
    assert handler3 in event_source._handlers

# Generated at 2022-06-13 15:54:04.402941
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda: x
    source += lambda: x
    source += lambda: x



# Generated at 2022-06-13 15:54:14.470358
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.module_utils._text import to_text

    def handler():
        return

    class Subclass(_EventSource):
        pass

    event_source = Subclass()

    # test with a handler which is callable
    event_source += handler
    assert callable(handler)
    assert set([handler]) == event_source._handlers

    # test with a handler which is not callable
    try:
        event_source += 'not callable'
    except ValueError as ex:
        assert 'handler must be callable' in to_text(ex)
    else:
        assert False  # exceptions are required to be raised



# Generated at 2022-06-13 15:54:25.902986
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def handler1(a, b, c):
        handler1.calls.append((a, b, c))

    handler1.calls = []

    def handler2(a):
        handler2.calls.append(a)

    handler2.calls = []

    def handler3(a, b, c, d=None):
        handler3.calls.append((a, b, c, d))

    handler3.calls = []

    def test_fixture():
        return _EventSource()

    es = test_fixture()
    es += handler1
    es += handler2
    es += handler3

    es.fire(1, 2, 3)
    es.fire(5)
    es.fire(5, 6, 7, d=8)


# Generated at 2022-06-13 15:54:36.603882
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    class EventLogger:
        def __init__(self):
            self.events = []

        def log(self, msg, *args, **kwargs):
            self.events.append((msg, args, kwargs))

        def __str__(self):
            return str(self.events)

    logger = EventLogger()

    event_source += logger.log

    event_source.fire('foo')
    assert logger.events == [('foo', (), {})]

    event_source.fire('bar', a='b')
    assert logger.events == [('foo', (), {}), ('bar', (), {'a': 'b'})]

    def raises(msg, *args, **kwargs):
        raise ValueError(msg)

    event_source += raises


# Generated at 2022-06-13 15:54:47.354976
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from types import FunctionType
    from ansible.module_utils.six import with_metaclass, integer_types

    class _FunctionEventSource(with_metaclass(_EventSource)):
        def _on_exception(self, handler, exc, *args, **kwargs):
            if not isinstance(handler, FunctionType):
                raise TypeError('handler must be callable')
            if not any(isinstance(arg, integer_types) for arg in args):
                raise ValueError('handler must receive at least one integer')
            return False

    class _ClassEventSource(with_metaclass(_EventSource)):
        pass

    assert _FunctionEventSource().fire(0) is None

    fes = _FunctionEventSource()
    fes += (lambda x: x)
    assert fes.fire(1) is None

   

# Generated at 2022-06-13 15:54:50.857694
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    # Set up handler
    handler = lambda msg: msg

    # Add handler
    event_source += handler

    # Remove handler
    event_source -= handler



# Generated at 2022-06-13 15:54:56.963455
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Mock:
        def callable(self, value):
            return True

    mock = Mock()

    event_source = _EventSource()
    event_source.__iadd__(mock.callable)

    try:
        event_source.__iadd__(None)
        assert False, 'ValueError not raised'
    except ValueError as e:
        assert "must be callable" in str(e)



# Generated at 2022-06-13 15:55:02.671719
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    s = _EventSource()
    def f1(*args, **kwargs):
        pass
    def f2(*args, **kwargs):
        pass
    def f3(*args, **kwargs):
        pass

    s.fire()
    # add a one handler
    s += f1
    s.fire()
    # add a hander multiple times
    s += f1
    s.fire()
    # add another handler
    s += f2
    s.fire()
    # add another handler
    s += f3
    s.fire()


# Generated at 2022-06-13 15:55:10.653070
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Foo:
        pass

    es = _EventSource()

    handler1 = Foo()
    handler2 = Foo()

    es += handler1
    es += handler2

    # handler1 must be in es
    assert handler1 in es._handlers
    assert handler2 in es._handlers

    # if we add the same handler again, it must not be added twice
    es += handler1
    assert len(es._handlers) == 2

    # adding a noncallable should raise an exception
    try:
        es += 'foo'
        assert False
    except ValueError:
        pass


# Generated at 2022-06-13 15:55:41.634063
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class MockEventSource(_EventSource):
        pass

    me = MockEventSource()

    def handler():
        pass

    me += handler
    assert handler in me._handlers


# Generated at 2022-06-13 15:55:51.546339
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class test_class:
        def __init__(self):
            self.hander1_handler_calls = 0
            self.hander2_handler_calls = 0
            self.handler3_handler_calls = 0

        def handler1_handler(self, *args, **kwargs):
            self.hander1_handler_calls += 1

        def handler2_handler(self, *args, **kwargs):
            self.hander2_handler_calls += 1

        def handler3_handler(self, *args, **kwargs):
            self.handler3_handler_calls += 1
            raise ValueError('an exception')

    def sub_handler1(self, *args, **kwargs):
        test_class_instance.handler1_handler(*args, **kwargs)


# Generated at 2022-06-13 15:55:54.335220
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler(msg):
        pass

    es += handler

    assert handler in es._handlers



# Generated at 2022-06-13 15:56:01.803707
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible_collections.ansible.builtin.tests.unit.compat import unittest

    class TestEventSource(unittest.TestCase):

        def setUp(self):
            self.handler = lambda msg: None

            self.event = _EventSource()
            self.event += self.handler

        def test_fire_success(self):
            self.event.fire('msg')

        def test_fire_exception(self):
            self.handler = lambda msg: 1 / 0

            with self.assertRaises(ZeroDivisionError):
                self.event.fire('msg')

# Generated at 2022-06-13 15:56:03.864344
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def h():
        pass

    assert callable(h)
    es += h



# Generated at 2022-06-13 15:56:11.294545
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EVENT:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    event = EVENT(x=1, y=2)
    event_source = _EventSource()

    def callback_1(*args, **kwargs):
        assert len(args) == 0 and len(kwargs) == 0

    def callback_2(*args, **kwargs):
        assert len(args) == 1 and len(kwargs) == 0
        arg = args[0]

        assert isinstance(arg, EVENT)
        assert arg.x == 1 and arg.y == 2

    def callback_3(*args, **kwargs):
        assert len(args) == 1 and len(kwargs) == 0
        arg = args[0]

        assert isinstance(arg, EVENT)
        assert arg

# Generated at 2022-06-13 15:56:22.746689
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes as _to_bytes
    from ansible.module_utils._text import to_text as _to_text
    from ansible.module_utils.six import string_types

    simple_handler = lambda *a, **kw: 42

    def handler_with_keyword_args(a, b, c=None):
        return a, b, c

    def handler_with_varargs(*args):
        return args

    def handler_with_kwargs(**kwargs):
        return kwargs

    def handler_that_raises(a, b, c=None):
        raise ValueError('my message')

# Generated at 2022-06-13 15:56:30.662481
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Foo():
        def handler(foo, a, b, c):
            foo.result = [to_text(a), b, c]

    event = _EventSource()
    foo = Foo()
    event += foo.handler
    event += lambda x, y, z: x._append_to_result(y, z)
    event += 'notcallable'
    event += lambda x, y, z: 'notreturnable'
    event.fire('a', 'b', 'c')
    assert foo.result == ['a', 'b', 'c']

    # test exception handling
    event += lambda x, y, z: raise_str(x.result)
    try:
        event.fire('x', 'y', 'z')
    except Exception as ex:
        assert str(ex) == 'abc'

# Generated at 2022-06-13 15:56:36.646889
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(*args, **kwargs):
        pass

    def other_handler(*args, **kwargs):
        pass

    _handler_fired = False
    _other_handler_fired = False

    event = _EventSource()
    event += handler
    event += other_handler

    # Fire it and check to see if our handler got called
    event.fire()
    assert _handler_fired

    # Fire it and check to see if our other handler got called
    event.fire()
    assert _other_handler_fired

# Generated at 2022-06-13 15:56:38.964510
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()
    e += lambda *args, **kwargs: True
    e += lambda *args, **kwargs: False
    assert e.fire(1, 2) is None

# Generated at 2022-06-13 15:57:42.474739
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def handler1(*args, **kwargs):
        pass

    def handler2(*args, **kwargs):
        pass

    eventsource = _EventSource()

    eventsource += handler1
    assert len(eventsource._handlers) == 1
    assert eventsource._handlers == {handler1}
    assert handler1 in eventsource._handlers

    eventsource += handler2
    assert len(eventsource._handlers) == 2
    assert eventsource._handlers == {handler1, handler2}
    assert handler1 in eventsource._handlers
    assert handler2 in eventsource._handlers


# Generated at 2022-06-13 15:57:52.302997
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class __EventSource(object):
        def on_exception(self, handler, exc, *args, **kwargs):
            self.exc = str(exc)
            self.args = args
            self.kwargs = kwargs
            return True

    class __EventHandler(object):
        def __init__(self, name, raises=None, args=None, kwargs=None):
            self.name = name
            self.raises = raises
            self.args = args
            self.kwargs = kwargs

        def __call__(self, *args, **kwargs):
            if self.args is not None:
                for i, arg in enumerate(args):
                    assert arg == self.args[i]

# Generated at 2022-06-13 15:57:58.258089
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        args = None
        kwargs = None

        def handler(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    event_source = MyEventSource()
    event_source += event_source.handler
    event_source.fire('arg1', 'arg2', kw1='val1')

    assert event_source.args == ('arg1', 'arg2')
    assert event_source.kwargs == {'kw1': 'val1'}

# Generated at 2022-06-13 15:58:04.771823
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEvent:
        def __init__(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs

        def __call__(self):
            self.func(*self.args, **self.kwargs)

    def _handler_a(a, b):
        t.append(a)
        t.append(b)

    def _handler_b(a, b=10):
        t.append(a)
        t.append(b)

    t = []
    s = _EventSource()

    # Test for _EventSource
    s += _handler_a
    s += _handler_b

    s.fire(1, 2)

    assert t == [1, 2, 1, 10]

    s -= _handler_a

# Generated at 2022-06-13 15:58:13.798649
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    event_source.fire(1, 2, 3)

    def handler1(a, b, c):
        assert a == 1
        assert b == 2
        assert c == 3

    def handler2(a, b, c):
        assert a == 1
        assert b == 2
        assert c == 3
        return

    event_source += handler1
    event_source.fire(1, 2, 3)

    event_source += handler2
    event_source.fire(1, 2, 3)

    event_source -= handler1
    event_source.fire(1, 2, 3)

    def handler3(a, b, c):
        assert a == 1
        assert b == 2
        assert c == 3
        raise ValueError('expected exception')

    event_source += handler3

# Generated at 2022-06-13 15:58:16.499026
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def fire_me(call_me_back):
        call_me_back()

    def call_me_back():
        return "A callback function was called."

    event += call_me_back

    assert event.fire(fire_me) is None

# Generated at 2022-06-13 15:58:19.223374
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler(index):
        assert index == 100

    es += handler

    es.fire(100)



# Generated at 2022-06-13 15:58:21.584610
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    counter = 0

    def increment(value):
        nonlocal counter
        counter += value

    event = _EventSource()
    event += increment

    event.fire(value=1)
    event.fire(value=2)
    event.fire(value=3)

    assert counter == 6



# Generated at 2022-06-13 15:58:29.196747
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    def handle_no_exception(value):
        assert value == 'test'
        return 'no_exception_handled'

    def handle_exception(value):
        assert value == 'test'
        raise Exception('exception_handled')

    def handle_exception_false(value):
        assert value == 'test'
        raise Exception('exception_handled_false')

    def handle_exception_true(value):
        assert value == 'test'
        raise Exception('exception_handled_true')

    event = _EventSource()

    event += handle_no_exception
    event += handle_exception
    event += handle_exception_false
    event += handle_exception_true

    assert event.fire('test') == 'no_exception_handled'


# Generated at 2022-06-13 15:58:33.856336
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    def handler():
        pass

    es += handler
    assert handler in es._handlers

    es -= handler
    assert handler not in es._handlers

    es += handler
    es += handler
    assert len(es._handlers) == 1

    es -= handler
    es -= handler
    assert len(es._handlers) == 0