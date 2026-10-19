

# Generated at 2022-06-13 15:49:08.715160
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test(a, b, c=3):
        raise RuntimeError('test_exception')

    event_source = _EventSource()
    event_source += test
    assert event_source._handlers == {test}

    try:
        event_source.fire('a', 'b')
        assert False, "Did not raise exception"
    except RuntimeError:
        pass

# Generated at 2022-06-13 15:49:10.529811
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def func(arg):
        pass

    source = _EventSource()
    source += func
    source.fire("test")

# Generated at 2022-06-13 15:49:17.541893
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Setup
    event = _EventSource()

    global listener_arg_receiever
    listener_arg_receiever = None
    def listener(arg):
        # we need to get the value from the global because
        # the listener method isn't returning anything to
        # record the value of arg
        global listener_arg_receiever
        listener_arg_receiever = arg

    event += listener
    payload = 'test payload'

    # Test
    event.fire(payload)

    # Assert
    assert listener_arg_receiever == payload

# Generated at 2022-06-13 15:49:22.816955
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    assert len(source._handlers) == 0

    def handler1():
        pass

    def handler2():
        pass

    source += handler1
    assert len(source._handlers) == 1
    assert handler1 in source._handlers

    source += handler2
    assert len(source._handlers) == 2
    assert handler1 in source._handlers
    assert handler2 in source._handlers

    source += handler2
    assert len(source._handlers) == 2


# Generated at 2022-06-13 15:49:25.154373
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class CollectionConfig(_AnsibleCollectionConfig):
        pass

    class CollectionLoader(object):
        class AnsibleCollectionConfig():
            pass

    loader = CollectionLoader()


# Generated at 2022-06-13 15:49:32.374848
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    def event_handler(arg):
        print('event handled - arg:' + str(arg))

    # Add one handler
    event += event_handler
    assert event._handlers == {event_handler}

    # Add another handler
    event += event_handler
    assert event._handlers == {event_handler}

    # Raise an exception because trying to add a handler that is not callable
    try:
        event += 'string'
    except ValueError as e:
        assert 'handler must be callable' in str(e)



# Generated at 2022-06-13 15:49:38.427167
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest(object):
        def __init__(self):
            self.n = 0
            self.increment = _EventSource()

    def handler(incr):
        def _handler():
            self.n += incr
        return _handler

    e = EventSourceTest()
    e.increment += handler(1)
    e.increment += handler(2)
    e.increment += handler(3)
    e.increment.fire()
    assert e.n == 6

    e.increment -= handler(2)
    e.increment.fire()
    assert e.n == 8



# Generated at 2022-06-13 15:49:38.903425
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    assert True

# Generated at 2022-06-13 15:49:42.781456
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Target:
        def __init__(self):
            self.fired = False

        def handler(self, *args, **kwargs):
            self.fired = True

    source = _EventSource()
    target = Target()

    source += target.handler

    source.fire()

    assert target.fired



# Generated at 2022-06-13 15:49:45.265852
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += 1
    assert len(source._handlers) == 0


# Generated at 2022-06-13 15:49:52.343114
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: True
    es += lambda: False
    assert len(es._handlers) == 2
    es += lambda: False
    assert len(es._handlers) == 2


# Generated at 2022-06-13 15:50:03.401358
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import unittest

    class MyTest(unittest.TestCase):
        def test_ValueError_raised_when_handler_is_none(self):
            source = _EventSource()
            with self.assertRaises(ValueError) as context:
                source += None

            self.assertEqual('handler must be callable', str(context.exception))

        def test_ValueError_raised_when_handler_is_str(self):
            source = _EventSource()
            with self.assertRaises(ValueError) as context:
                source += 'hello world'

            self.assertEqual('handler must be callable', str(context.exception))

        def test_ValueError_raised_when_handler_is_int(self):
            source = _EventSource()

# Generated at 2022-06-13 15:50:10.673372
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEvent(_EventSource):
        on_exception = None

        def _on_exception(self, handler, exc, *args, **kwargs):  # type: (Callable[..., None], Exception, Any, Any) -> bool
            self.on_exception = (handler, exc, args, kwargs)

    failed_handler = []

    def handler_exception_1(a, b):  # type: (int, int) -> None
        raise ValueError("handler_exception_1")

    def handler_exception_2(a, b):  # type: (int, int) -> None
        raise ValueError("handler_exception_2")

    def handler_not_called(a, b):  # type: (int, int) -> None
        raise ValueError("should not be called")


# Generated at 2022-06-13 15:50:19.912961
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTestCase:
        def setUp(self):
            self.event_source = _EventSource()
            self.processed = []

        def test(self):
            self.processed = []
            self.event_source += self.handler1
            self.assertEqual(self.processed, [])
            self.event_source.fire(1, 2)
            self.assertEqual(self.processed, [1, 2])
            self.event_source.fire(1, 2)
            self.assertEqual(self.processed, [1, 2, 1, 2])

        def handler1(self, *args, **kwargs):
            self.processed.extend(args)

    EventSourceTestCase().test()



# Generated at 2022-06-13 15:50:28.046841
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(x, y):
        if x == 1 and y == 2:
            return

        raise Exception('handler1')

    def handler2(x, y):
        if x == 3 and y == 4:
            return

        raise Exception('handler2')

    def handler3(x, y):
        if x == 5 and y == 6:
            return

        raise Exception('handler3')

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source += handler3

    # handlers do not raise exceptions
    event_source.fire(1, 2)
    event_source.fire(3, 4)

    # handler2 raises an exception
    with pytest.raises(Exception):
        event_source.fire(1, 2)

# Generated at 2022-06-13 15:50:33.682208
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    assert not e._handlers

    def foo(): pass
    e += foo
    assert e._handlers
    assert e._handlers == set([foo])

    with pytest.raises(ValueError) as ex:
        e += ''

    e -= foo
    assert not e._handlers



# Generated at 2022-06-13 15:50:40.296354
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSource_Fire_Test():

        def add_event(self, event_source):
            self.event_source = event_source
            self.event_count = 0

        def event(self):
            self.event_count += 1

        def fire_event(self):
            self.event_source.fire()

    test_obj = _EventSource_Fire_Test()
    test_source = _EventSource()
    test_source += test_obj.event
    test_obj.add_event(test_source)

    test_obj.fire_event()
    if test_obj.event_count != 1:
        raise ValueError('event_count expected to be 1, but was %d' % test_obj.event_count)

# Generated at 2022-06-13 15:50:46.890376
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSource(object):
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

        def _on_exception(self, handler, exc, *args, **kwargs):
            return True


# Generated at 2022-06-13 15:50:51.497937
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def test():
        print('hi')

    event = _EventSource()

    event += test

    assert len(event._handlers) == 1
    assert test in event._handlers



# Generated at 2022-06-13 15:50:56.410457
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    source += lambda: None
    source += lambda: None
    source -= lambda: None
    source -= lambda: None
    source += lambda: None
    source += lambda: None
    source -= lambda: None
    source -= lambda: None
    source.fire()

    source = _EventSource()
    source += lambda: None
    source += lambda: None
    source += lambda: None
    source.fire()

    source = _EventSource()
    source += lambda: None
    source += lambda: 1 / 0
    source.fire()

# Generated at 2022-06-13 15:51:16.167415
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_1(*args, **kwargs):
        pass

    def handler_2(*args, **kwargs):
        pass

    event = _EventSource()
    event.fire()

    event += handler_1
    event += handler_2

    event.fire(1, 2, 3)

    # the last handler raises an exception, so all handlers will be removed,
    # so there should be no exception
    def handler_3(*args, **kwargs):
        raise ValueError('abnormal return')

    event._on_exception = lambda h, exc, *a, **kw: False
    event += handler_3
    event.fire(4, 5, 6)

    # the last handler raises an exception and the handler's on_exception
    # returns True, so the last handler is removed

# Generated at 2022-06-13 15:51:22.592779
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test that nothing is happening if no handlers are registered
    es = _EventSource()
    es.fire()

    # Test passing an arg to handler
    handler = lambda arg: setattr(handler, 'test', arg)
    handler.test = None
    es += handler
    es.fire('test value')
    assert handler.test == 'test value'

    # Test passing a kwarg to handler
    handler = lambda kwarg1=None: setattr(handler, 'test', kwarg1)
    handler.test = None
    es += handler
    es.fire(kwarg1='test value')
    assert handler.test == 'test value'

    # Test passing a kwarg and an arg to handler

# Generated at 2022-06-13 15:51:32.775828
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    observed = []

    def handler_a(*args, **kwargs):
        observed.append('called a')
        raise Exception('a')

    def handler_b(*args, **kwargs):
        observed.append('called b')

    def handler_c(*args, **kwargs):
        observed.append('called c')
        raise Exception('c')

    def handler_d(*args, **kwargs):
        observed.append('called d')
        raise Exception('d')

    def handler_e(*args, **kwargs):
        observed.append('called e')
        raise Exception('e')

    source = _EventSource()

    source += handler_a
    source += handler_b
    source += handler_c
    source += handler_d
    source += handler_e


# Generated at 2022-06-13 15:51:37.630958
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    count = 0

    def handler():
        nonlocal count
        count += 1

    evt = _EventSource()
    evt += handler
    assert len(evt._handlers) == 1
    assert count == 0

    evt.fire()
    assert count == 1

# Generated at 2022-06-13 15:51:48.403256
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import ansible_collections.ansible.unit_tests.test_collection_loader.test_events_test as event_test
    import unittest

    class TestEventSource(unittest.TestCase):
        def setUp(self):
            self.event_source = _EventSource()

        def test_fire_one_handler(self):
            event_test.handler_result = list()
            self.event_source += event_test.handler_one
            self.event_source.fire(1, 2, x='a', y='b')
            self.assertEqual([(1, 2, {'x': 'a', 'y': 'b'})], event_test.handler_result)

        def test_fire_two_handlers(self):
            event_test.handler_result = list()
            self.event

# Generated at 2022-06-13 15:51:55.482725
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler1():
        pass

    def handler2():
        raise Exception('error')

    def handler3():
        raise ValueError('error')

    # empty event source
    event_source.fire()

    # add one handler
    event_source += handler1
    event_source.fire()

    # add one handler and make it throw an exception
    event_source += handler2
    try:
        event_source.fire()
        assert False
    except Exception:
        pass

    # add one handler and make it throw an exception and make a handler raise a different type of exception
    event_source += handler3
    try:
        event_source.fire()
        assert False
    except Exception:
        pass

    # add one handler, remove it, and make a handler raise an exception
    event

# Generated at 2022-06-13 15:52:01.702811
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    def f():
        pass
    def g():
        pass
    f2 = f
    es += f
    es += g
    es += f2
    assert len(es._handlers) == 2
    assert f in es._handlers
    assert f2 in es._handlers
    assert g in es._handlers


# Generated at 2022-06-13 15:52:04.884251
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def test_func():
        pass

    e += test_func
    assert test_func in e._handlers



# Generated at 2022-06-13 15:52:12.580304
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    calls = [0, 0]

    def callme_one(*args, **kwargs):
        calls[0] += 1

    def callme_two(*args, **kwargs):
        calls[1] += 1

    es = _EventSource()
    es += callme_one
    es += callme_two

    assert calls[0] == 0
    assert calls[1] == 0

    es.fire()

    assert calls[0] == 1
    assert calls[1] == 1

    es.fire()

    assert calls[0] == 2
    assert calls[1] == 2

# Generated at 2022-06-13 15:52:14.345567
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda *args, **kwargs: None
    assert len(source._handlers) == 1


# Generated at 2022-06-13 15:52:33.850841
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            if exc.args[0] == 'pretend I am a ValueError':
                return False

            return True

    class Processed:
        def __init__(self):
            self.handled = False

    def handler1(p):
        p.handled = True

    def handler2(p):
        raise ValueError('I am a ValueError')

    def handler3(p):
        raise TypeError('I am a TypeError')

    def handler4(p):
        raise ValueError('pretend I am a ValueError')

    p = Processed()

    myeventsource = MyEventSource()

    myeventsource += handler1
    myeventsource += handler2
    myeventsource += handler3


# Generated at 2022-06-13 15:52:38.307896
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    assert len(e._handlers) == 0

    def handler():
        pass

    e.__iadd__(handler)
    assert len(e._handlers) == 1
    assert handler in e._handlers



# Generated at 2022-06-13 15:52:42.418988
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Setup test
    test_eventsource = _EventSource()

    # Call method
    test_eventsource.fire(1, 2, 3)

    # Verify results
    expected_result = None
    assert expected_result == None



# Generated at 2022-06-13 15:52:43.220262
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # eventsource = _EventSource()
    # eventsource.fire()
    pass

# Generated at 2022-06-13 15:52:48.591016
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(arg):
        print('handler1', arg)

    def handler2(arg):
        print('handler2', arg)

    def handler3(arg):
        print('handler3', arg)

    source = _EventSource()

    source += handler1
    source += handler2
    source += handler3

    source.fire('a')



# Generated at 2022-06-13 15:52:57.373016
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler_01():
        pass

    def handler_02():
        pass

    event_source = _EventSource()
    assert len(event_source._handlers) == 0

    event_source += handler_01
    assert len(event_source._handlers) == 1

    event_source += handler_01
    assert len(event_source._handlers) == 1

    event_source += handler_02
    assert len(event_source._handlers) == 2

    # test exception handling
    with __import__('pytest').raises(ValueError):
        event_source += object()


# Generated at 2022-06-13 15:53:06.715672
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler1(a, b):
        pass

    def handler2(a, b, c):
        pass

    def handler3(a, b):
        raise RuntimeError('broken')

    event_source += handler1

    with pytest.raises(ValueError):
        event_source += 1

    event_source += handler2
    event_source += handler3

    event_source.fire(1, 2)
    event_source.fire(1, 2, 3)
    with pytest.raises(RuntimeError):
        event_source.fire(1, 2)

    event_source -= handler1
    event_source -= handler1
    event_source -= handler2

    with pytest.raises(RuntimeError):
        event_source.fire(1, 2)

    event

# Generated at 2022-06-13 15:53:19.396270
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self._was_fired = False

        def _on_exception(self, handler, exception):
            pass

        def fire(self):
            self._was_fired = True
            super(MyEventSource, self).fire()

    def handler1():
        pass

    def handler2():
        pass

    def handler3():
        raise Exception('Test exception')

    my_event_source = MyEventSource()

    my_event_source += handler1
    my_event_source += handler2

    assert not my_event_source._was_fired

    my_event_source.fire()

    assert my_event_source._was_fired

# Generated at 2022-06-13 15:53:21.033975
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += (lambda: True)



# Generated at 2022-06-13 15:53:24.132738
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    events = _EventSource()

    def handler(x):
        pass

    events += handler

    assert events._handlers == {handler}



# Generated at 2022-06-13 15:54:04.792059
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # function does not raise exception
    handler1_fired = False

    def handler1():
        nonlocal handler1_fired
        handler1_fired = True

    event_source += handler1
    event_source.fire()
    assert handler1_fired

    # function raises exception, on_exception returns True
    handler2_fired = False

    def handler2():
        raise Exception('oops')

    try:
        event_source += handler2
        event_source.fire()
        assert False, 'event_source.fire did not re-raise exception'
    except Exception as ex:
        assert ex.args[0] == 'oops', 'event_source.fire did not pass exception through'

    # function raises exception, on_exception returns False
    handler3_fired = False


# Generated at 2022-06-13 15:54:12.210956
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    event_source.fire(1, 2, 3)
    event_source += lambda *args, **kwargs: print(args, kwargs)
    event_source.fire(1, 2, 3)
    event_source -= lambda *args, **kwargs: print(args, kwargs)
    event_source.fire(1, 2, 3)



# Generated at 2022-06-13 15:54:14.339532
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    h = lambda: None

    es += h
    assert h in es._handlers


# Generated at 2022-06-13 15:54:25.453114
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    # test no handlers
    es.fire(1, 2, 'three', {'four': 4})

    # test one handler
    def handler1(x, y, z, w):
        assert x == 1
        assert y == 2
        assert z == 'three'
        assert w == {'four': 4}

    es += handler1
    es.fire(1, 2, 'three', {'four': 4})

    # test two handlers
    def handler2(x, y, z, w):
        assert x == 1
        assert y == 2
        assert z == 'three'
        assert w == {'four': 4}

    es += handler2
    es.fire(1, 2, 'three', {'four': 4})

# Generated at 2022-06-13 15:54:36.491756
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Exception raised by a method, but not handled by the event source
    class MyException(Exception):
        pass

    class TestObj:

        def __init__(self):
            self.fired = False
            self.fired_with = None

        def handler(self, *args, **kwargs):
            self.fired = True
            self.fired_with = (args, kwargs)

        def fail_handler(self, *args, **kwargs):
            raise MyException('I fail')

    # create the event source
    es = _EventSource()

    # create a handler object
    obj = TestObj()

    # add the handler
    es += obj.handler

    # fire the event
    es.fire('foo', 'bar', baz='qux')

    # handler is called
    assert obj.fired



# Generated at 2022-06-13 15:54:42.132703
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    event = _EventSource()
    handler_foo = lambda *args, **kwargs: 'foo'
    handler_bar = lambda *args, **kwargs: 'bar'

    event += handler_foo
    event += handler_bar

    assert handler_foo in event._handlers
    assert handler_bar in event._handlers


# Generated at 2022-06-13 15:54:47.420764
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    calls = []

    # Set up the reflector that will be used in the test.
    def reflector(val):
        calls.append(val)

    # Set up an event handler that will be added to the event source.
    e += reflector

    # File the event.
    e.fire('abc')

    # Ensure the event is reflected in the event handler.
    assert calls == ['abc']



# Generated at 2022-06-13 15:54:54.736208
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert len(event_source._handlers) == 0

    def _handler(arg1, arg2=None):
        pass

    event_source += _handler
    assert len(event_source._handlers) == 1
    assert _handler in event_source._handlers

    event_source += _handler
    assert len(event_source._handlers) == 1
    assert _handler in event_source._handlers



# Generated at 2022-06-13 15:55:02.967811
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # ensure that the event source calls all handlers
    events = _EventSource()
    count = [0]
    def _do_nothing(*args, **kwargs):
        count[0] += 1
    events += _do_nothing
    events += _do_nothing
    events += _do_nothing
    events.fire()
    assert count[0] == 3

    # ensure that exceptions raised by handlers do not prevent other handlers from being executed
    events = _EventSource()
    def _raise(*args, **kwargs):
        raise Exception('should not prevent subsequent handlers from executing')
    def _do_nothing(*args, **kwargs):
        count[0] += 1
    events += _raise
    events += _do_nothing
    events.fire()
    assert count[0] == 1

    # ensure that if the handler asks to re-

# Generated at 2022-06-13 15:55:12.749116
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    events = _EventSource()
    class C:
        def __init__(self):
            self.calls = []
        def __call__(self, *args, **kwargs):
            self.calls.append((args, kwargs))
            if len(self.calls) == 1:
                raise ValueError('problem')

    c1 = C()
    c2 = C()
    events += c1
    events += c2
    events += c1

    events.fire(1, 2, 3, a='b', c='d')

    assert c1.calls[0] == ((1, 2, 3), {'a': 'b', 'c': 'd'})
    assert c1.calls[1] == ((1, 2, 3), {'a': 'b', 'c': 'd'})

# Generated at 2022-06-13 15:56:23.466726
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    '''
    unit test for method __iadd__ of class _EventSource
    '''
    def test_callback(x, y):
        return x + y

    event_source = _EventSource()

    # test event source without any handlers
    assert len(event_source._handlers) == 0
    assert event_source.fire(1, 2) == None

    # test event source with one handler
    event_source += test_callback
    assert len(event_source._handlers) == 1
    assert event_source.fire(1, 2) == 3

    # test event source with two handlers
    event_source += test_callback
    assert len(event_source._handlers) == 2
    assert event_source.fire(1, 2) == 3


# Generated at 2022-06-13 15:56:31.091828
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    obj = _EventSource()

    # empty
    obj.fire('foo')

    # no exception
    counter1 = 0
    counter2 = 0

    def callback1(arg):
        nonlocal counter1
        counter1 += 1
        assert counter1 == 1
        assert arg == 'foo'

    def callback2(arg):
        nonlocal counter2
        counter2 += 1
        assert counter2 == 1
        assert arg == 'foo'

    obj += callback1
    obj.fire('foo')

    obj += callback2
    obj.fire('foo')

    # exception
    counter1 = 0
    counter2 = 0
    counter3 = 0

    def callback3(arg):
        nonlocal counter3
        counter3 += 1
        assert counter3 == 1
        assert arg == 'foo'
        raise RuntimeError('oops')

# Generated at 2022-06-13 15:56:39.675179
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from collections import namedtuple
    from ansible.module_utils.six import PY2, PY3

    # create _EventSource
    es = _EventSource()

    # test success scenarios
    assert "f" not in es._handlers
    es += lambda: 1
    assert "f" in es._handlers

    # test failure scenarios
    if PY2:
        # in Python 2, unbound methods are callable
        es += namedtuple("Foo", "x y")._make.__func__
        assert "f" in es._handlers

# Generated at 2022-06-13 15:56:46.528403
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()

    def handler1(*args, **kwargs):
        raise TypeError('test')

    def handler2(*args, **kwargs):
        raise RuntimeError('test2')

    e += handler1
    e += handler2

    try:
        e.fire()
    except TypeError:
        pass
    else:
        raise Exception('handler1 should have raised a TypeError')

    try:
        e.fire()
    except RuntimeError:
        pass
    else:
        raise Exception('handler2 should have raised a RuntimeError')

    try:
        e._handlers = set()
        e.fire()
    except RuntimeError:
        raise Exception('no handlers should have been called')

# Generated at 2022-06-13 15:56:57.737622
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    args = [10, 20]
    kwargs = dict(a='A', b=['B1', 'B2'])

    def foo(*args, **kwargs):
        return 'foo called with %s %s' % (str(args), str(kwargs))

    def bar(*args, **kwargs):
        return 'bar called with %s %s' % (str(args), str(kwargs))

    src = _EventSource()
    src += foo
    src += bar

    ret = src.fire(*args, **kwargs)

    expected = [
        'foo called with %s %s' % (str(args), str(kwargs)),
        'bar called with %s %s' % (str(args), str(kwargs)),
    ]
    assert ret == expected

# Generated at 2022-06-13 15:57:03.437560
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # create an event source and register a handler
    event_source = _EventSource()
    handler_invoked = False

    def handler():
        nonlocal handler_invoked
        handler_invoked = True

    event_source += handler

    # fire the event source and see if the handler was invoked
    event_source.fire()
    assert handler_invoked is True, 'handler should have been invoked'

    # remove the handler, fire the event source and see if the handler was invoked
    event_source -= handler
    handler_invoked = False
    event_source.fire()
    assert handler_invoked is False, 'handler should not have been invoked'

# Generated at 2022-06-13 15:57:06.654479
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def _handler(value):
        return value

    source = _EventSource()
    source += _handler

    assert _handler in source._handlers
    assert source._handlers == {_handler}



# Generated at 2022-06-13 15:57:12.665358
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # arrange
    s = _EventSource()
    h = lambda: print('hello')

    # act
    s += h

    # assert we can add a callable
    assert h in s._handlers

    # assert we cannot add non-callable
    try:
        s += 'not callable'

    except ValueError:
        pass
    else:
        raise AssertionError('expected ValueError')



# Generated at 2022-06-13 15:57:14.298907
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(msg):
        pass

    es = _EventSource()
    es += handler

    assert handler in es._handlers



# Generated at 2022-06-13 15:57:24.611587
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.module_utils.common.text.converters import to_bytes

    event_source = _EventSource()
    event_source += _AnsibleCollectionConfig.on_collection_load  # use the on_collection_load classmethod

    def handle_collection_load(collection, loader_obj):
        print('test__EventSource___iadd__: handle_collection_load: collection=%s' % collection)
        print('test__EventSource___iadd__: handle_collection_load: loader_obj=%s' % loader_obj)
        print('test__EventSource___iadd__: handle_collection_load: loader_obj.meta_dir=%s' % loader_obj.meta_dir)

    event_source += handle_collection_load

    # example collection: the collection_loader installed at the ansible-base