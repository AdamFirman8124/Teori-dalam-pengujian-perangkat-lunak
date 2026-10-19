

# Generated at 2022-06-13 15:49:05.141708
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    called = [0]

    def handler():
        called[0] += 1

    event += handler
    event += handler
    event.fire()

    assert called[0] == 2



# Generated at 2022-06-13 15:49:14.794355
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test with no handlers registered
    no_handlers = _EventSource()
    result = no_handlers.fire()
    assert result is None

    # Test with a single handler registered
    single_handler = _EventSource()
    called = []
    single_handler += lambda: called.append(True)
    single_handler.fire()
    assert len(called) == 1

    # Test with multiple handlers registered
    multiple_handlers = _EventSource()
    called = []
    for arg in (1, 2, 3):
        multiple_handlers += lambda: called.append(arg)
        multiple_handlers += lambda arg=arg: called.append(arg)
    multiple_handlers.fire()
    assert called == [1, 1, 2, 2, 3, 3]

    # Test exception-handling in handler

# Generated at 2022-06-13 15:49:20.516512
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            self.fired = False
            _EventSource.__init__(self)

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.fired = True

        def handler(self, param):
            if param:
                raise Exception()

    tester = _TestEventSource()
    tester += tester.handler
    tester.fire(1)
    assert tester.fired


# Generated at 2022-06-13 15:49:22.603538
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    def return_none(a, b):
        return None
    es += return_none
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:49:31.929064
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    handlers = EventSource_fire__handlers()
    es = _EventSource()

    es += handlers.handler_1
    es += handlers.handler_2
    es += handlers.handler_3
    es += handlers.handler_4
    es += handlers.handler_5

    assert handlers.handler_1_call_count == 0
    assert handlers.handler_2_call_count == 0
    assert handlers.handler_3_call_count == 0
    assert handlers.handler_4_call_count == 0
    assert handlers.handler_5_call_count == 0

    es.fire(1, 'a', foo='bar')

    assert handlers.handler_1_call_count == 1
    assert handlers.handler_2_call_count == 1
    assert handlers.handler_3_call_count == 1
    assert handlers.handler_4

# Generated at 2022-06-13 15:49:39.214813
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    class MyEvent(object):
        pass

    source = _EventSource()

    # no handler yet

    try:
        source.fire(MyEvent())
        raise AssertionError('Expected _EventSource.fire() to raise ValueError')
    except ValueError:
        pass

    # add one handler

    def on_event(e):
        if isinstance(e, MyEvent):
            raise RuntimeError('Expected event')

    source += on_event
    source.fire(MyEvent())

    # add second handler

    def on_error(e):
        if isinstance(e, RuntimeError):
            raise AssertionError('Expected event to raise RuntimeError')

    source += on_error

# Generated at 2022-06-13 15:49:46.508941
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from unittest import TestCase

    tc = TestCase('__init__')

    event = _EventSource()

    def handler1(*args, **kwargs):
        tc.assertEqual(args, ('hi',))
        tc.assertEqual(kwargs, {'a': 1, 'b': 2})

    def handler2(*args, **kwargs):
        tc.assertEqual(args, ('hi',))
        tc.assertEqual(kwargs, {'a': 1, 'b': 2})
        raise RuntimeError('we expect this')

    event += handler1
    event += handler2

    try:
        event.fire('hi', a=1, b=2)
    except RuntimeError as ex:
        tc.assertEqual(to_text(ex), 'we expect this')
    else:
        tc

# Generated at 2022-06-13 15:49:55.667388
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    # no handlers - event should fire without error
    event = _EventSource()
    event.fire()

    # one handler, no exception - event should fire without error
    event = _EventSource()
    handler_calls = []

    def handler():
        handler_calls.append(True)

    event += handler
    event.fire()

    assert len(handler_calls) == 1

    # one handler, exception - expect re-raise
    event = _EventSource()
    handler_calls = []

    def handler():
        raise NotImplementedError()

    event += handler
    with pytest.raises(NotImplementedError):
        event.fire()

    # two handlers, no exceptions - expect both handlers to be called
    event = _EventSource()
    handler_calls = []

   

# Generated at 2022-06-13 15:50:02.076495
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler_one(value):
        pass

    def handler_two(value):
        pass

    event_source += handler_one
    event_source += handler_two

    event_source.fire(value=42)

    event_source -= handler_one
    event_source -= handler_one

    event_source -= handler_two
    event_source -= handler_two

    event_source.fire(value=42)


# Generated at 2022-06-13 15:50:07.737340
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # This test verifies that an exception raised during execution of
    # an event handler is propagated up to the caller of fire().

    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            # we don't want fire to re-raise this exception
            return False

    es = MyEventSource()
    es += lambda: raise_exception()

    try:
        es.fire()
    except Exception:
        pass
    else:
        raise AssertionError('fire() should propagate exceptions raised by event handlers')


# Generated at 2022-06-13 15:50:17.949918
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler1(x):
        raise ValueError

    def handler2(x):
        raise ValueError

    def handler3(x):
        raise ValueError

    def exception_handler(h, exc, *args, **kwargs):
        return h == handler1

    es = AnsibleCollectionConfig.on_collection_load
    es += handler1
    es += handler2
    es += handler3

    with pytest.raises(ValueError):
        es.fire()

    es._on_exception = exception_handler
    es.fire()

# Generated at 2022-06-13 15:50:27.531979
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    result = []

    def expect_fire(*args, **kwargs):
        result.append('expect_fire_{}_{}'.format(args, kwargs))

    def expect_exception(*args, **kwargs):
        result.append('expect_exception_{}_{}'.format(args, kwargs))
        raise Exception(result)

    def expect_rethrow(*args, **kwargs):
        result.append('expect_rethrow_{}_{}'.format(args, kwargs))
        raise Exception(result)

    def expect_not_rethrow(*args, **kwargs):
        result.append('expect_not_rethrow_{}_{}'.format(args, kwargs))
        raise Exception(result)

    # handlers are called in the order they

# Generated at 2022-06-13 15:50:37.051969
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.utils.collection_loader._event_source import _EventSource

    def handler(a, b, c):
        assert a == 1
        assert b == 2
        assert c == 3

    class MyEventSource(_EventSource):
        def __init__(self):
            super(MyEventSource, self).__init__()
            self._events_fired = 0

        def fire(self, *args, **kwargs):
            self._events_fired += 1

    event_source = MyEventSource()

    assert isinstance(event_source, MyEventSource)
    assert isinstance(event_source, AnsibleCollectionFinder)
    assert isinstance(event_source, _EventSource)

    assert len(event_source._handlers)

# Generated at 2022-06-13 15:50:47.190000
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # TODO
    # also add test for _on_exception
    from ansible.module_utils._text import to_bytes
    import collections
    import math

    # create mock object of _EventSource
    es = _EventSource()

    # create a mock function
    def test_func(a, b, c=None):
        return a + b + math.exp(c)
    # create an instance of it using a different name
    test_func_inst = test_func

    # create another mock function
    def test_func_2(a):
        return a
    # create an instance of it using a different name
    test_func_inst_2 = test_func_2

    # create a mock class

# Generated at 2022-06-13 15:50:57.922230
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # ensure that the event handler can handle errors by not raising
    class _TestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    event_source = _TestEventSource()

    foo = []

    event_source += lambda: foo.append(1)
    event_source += lambda: foo.append(2)
    event_source += lambda: foo.append(3)
    event_source += lambda: foo.append(4)
    event_source += lambda: 1 / 0
    event_source += lambda: foo.append(5)
    event_source += lambda: foo.append(6)

    event_source.fire()

    assert foo == [1, 2, 3, 4, 5, 6]

    # now ensure the event handler can re-raise

# Generated at 2022-06-13 15:51:03.834724
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Event(object):
        pass

    event = Event()
    count = [0]

    def on_event(source):
        count[0] += 1
        assert source is event

    event_source = _EventSource()
    event_source += on_event
    event_source.fire(event)

    assert count[0] == 1



# Generated at 2022-06-13 15:51:16.209158
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSource_Mock(object):
        def __init__(self):
            self.on_exception = _EventSource()

    _test_case = _EventSource_Mock()

    target = _EventSource()
    target._on_exception = _test_case.on_exception.fire

    def handler_one(*args, **kwargs):
        pass

    def handler_two(*args, **kwargs):
        raise ValueError('test')

    def handler_three(*args, **kwargs):
        raise RuntimeError('test')

    target += handler_one
    target += handler_two
    target += handler_three

    try:
        target.fire()
    except ValueError:
        pass
    else:
        assert False


# Generated at 2022-06-13 15:51:19.236820
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(arg1, arg2, arg3):
        pass

    e = _EventSource()
    e += handler
    e.fire(1, 2, 3)

# Generated at 2022-06-13 15:51:31.490852
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class TestEventSource(object):
        pass

    from ansible.module_utils._text import to_text

    # test adding invalid callables
    try:
        TestEventSource.event += 10
    except ValueError:
        pass
    except Exception as err:
        fail_test('Unexpected exception "{0}" raised from adding invalid value'.format(to_text(err)))
    else:
        fail_test('Expected ValueError from adding invalid value')

    # test adding valid callables
    def test_callable_1():
        return 10

    def test_callable_2():
        return 20

    TestEventSource.event += test_callable_1
    TestEventSource.event += test_callable_2

    # test removing valid callables

# Generated at 2022-06-13 15:51:42.800993
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def no_args():
        pass

    def one_arg(a):
        pass

    def two_args(a, b):
        pass

    def one_arg_one_kw(a, b=2):
        pass

    def one_arg_two_kw(a, b=2, c=3):
        pass

    def one_arg_one_kw_no_default(a, b):
        pass

    def one_arg_one_kw_no_default_1(a, b=None):
        pass

    def two_args_two_kw(a, b, c=3, d=4):
        pass

    def two_args_two_kw_1(a, b, c=3, d=4):
        pass


# Generated at 2022-06-13 15:51:50.681008
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventHandler:
        def __init__(self):
            self.event_count = 0

        def call_me(self):
            self.event_count += 1

    event_sink = _EventSource()

    handler = EventHandler()

    event_sink += handler.call_me
    event_sink += handler.call_me

    event_sink.fire()

    assert handler.event_count == 2

# Generated at 2022-06-13 15:51:54.846133
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def some_handler(*args, **kwargs):
        a = args[0]
        _kwargs = kwargs

    event_source = _EventSource()
    event_source += some_handler
    assert event_source._handlers
    try:
        event_source.fire('some value', x=1, y=2)
    except Exception as ex:
        assert False, ex
    assert not some_handler.__contains__('some value')



# Generated at 2022-06-13 15:51:58.040170
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler(arg):
        return arg

    events = _EventSource()
    assert not events._handlers
    events += handler
    assert handler in events._handlers


# Generated at 2022-06-13 15:52:06.782848
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class Test:
        def test(self):
            pass

    test_instance = Test()

    # invalid parameters
    event_source = _EventSource()
    try:
        event_source += None
        assert False, 'expected ValueError'
    except ValueError:
        pass
    try:
        event_source += 123
        assert False, 'expected ValueError'
    except ValueError:
        pass

    # valid parameters
    event_source += test_instance.test
    assert len(event_source._handlers) == 1
    event_source += test_instance.test
    assert len(event_source._handlers) == 1


# Generated at 2022-06-13 15:52:10.919498
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class run_handler(object):
        def __init__(self):
            self.run = False

        def handler(self):
            self.run = True

    e = _EventSource()
    t = run_handler()
    e += t.handler
    e.fire()
    assert t.run

# Generated at 2022-06-13 15:52:18.276741
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(a, b):
        handler1.fired = True
        return a + b

    def handler2(a, b):
        if b == 2:
            raise Exception('a')

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2

    handler1.fired = False
    event_source.fire(1, 2)
    assert handler1.fired is True

    try:
        event_source.fire(1, 2)
        assert False
    except Exception as e:
        assert str(e) == 'a'

    try:
        event_source.fire(1)
        assert False
    except TypeError:
        pass

    try:
        event_source += handler1
        assert False
    except ValueError:
        pass

    event_source -= handler

# Generated at 2022-06-13 15:52:22.126846
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    results = []

    def handler1(value):
        results.append(value)

    def handler2(value):
        results.append(value * 2)

    @staticmethod
    def handler3(value):
        results.append(value ** 3)

    evt += handler1
    evt += handler2
    evt += handler3
    evt.fire(2)
    assert results == [2, 4, 8]

# Generated at 2022-06-13 15:52:26.894752
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handle_event(event):
        raise ValueError('test exception')

    event_source = _EventSource()
    event_source += handle_event

    try:
        event_source.fire()
        raise AssertionError('test expected ValueError')
    except ValueError:
        pass


# Generated at 2022-06-13 15:52:33.066361
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    x = _EventSource()

    def foo(a, b, c):
        return a + b + c

    def bar(a, b, c):
        raise ValueError

    def baz():
        raise TypeError

    x += foo
    x += bar
    x += baz

    # we expect 3 exceptions to be raised
    try:
        x.fire(1, 2, 3)
    except TypeError:
        pass
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        raise AssertionError('expected an exception')

# Generated at 2022-06-13 15:52:41.418994
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def t1():
        raise Exception('test')

    def t2():
        raise Exception('test')

    event += t1
    event += t2

    try:
        event.fire()
    except Exception as err:
        pass

    event -= t1

    try:
        event.fire()
    except Exception as err:
        pass

    event -= t2

    try:
        event.fire()
    except Exception as err:
        raise Exception('Expected no exceptions')

# Generated at 2022-06-13 15:52:51.538643
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    result = []

    def handler(arg):
        result.append(arg)

    event = _EventSource()
    event += handler

    event.fire('One')
    event.fire('Two')
    event.fire('Three')

    if result != ['One', 'Two', 'Three']:
        raise AssertionError('Wrong result')

# Generated at 2022-06-13 15:52:58.688980
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyType:
        def __init__(self):
            self.events = 0

        def my_event(self):
            self.events += 1

    class MyListener:

        def __init__(self):
            self.events = 0

        def my_event(self):
            self.events += 1

    s = _EventSource()
    t = MyType()
    l = MyListener()

    s += l.my_event
    s += t.my_event

    s.fire()

    assert l.events == 1
    assert t.events == 1

# Generated at 2022-06-13 15:53:04.910707
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _SourceEvent(event.EventSource):
        def __init__(self):
            event.EventSource.__init__(self)
            self._count = 0

        def handler(self, *args, **kwargs):
            self._count += 1

    source = _SourceEvent()
    source += source.handler
    source.fire()
    assert source._count == 1, source._count
    source.fire(event=True, _type=True)
    assert source._count == 2, source._count

# Generated at 2022-06-13 15:53:06.642134
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    event += lambda: print('foo')
    event += lambda: print('bar')
    event.fire()


# Generated at 2022-06-13 15:53:12.691840
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _MyEvent:
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
            # if we return True, we want the caller to re-raise
            return True


# Generated at 2022-06-13 15:53:22.640755
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self.has_fired = False

        def __call__(self, *args, **kwargs):
            self.args_len = len(args)
            self.kwargs_len = len(kwargs)
            self.has_fired = True

    test_event_source = _TestEventSource()
    test_event_source.fire('foo', bar='baz')
    assert test_event_source.args_len == 1
    assert test_event_source.kwargs_len == 1
    assert test_event_source.has_fired

# Generated at 2022-06-13 15:53:31.967730
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class Call:

        call_count = 0

        def __init__(self, value):
            self.value = value
            Call.call_count += 1

        def __call__(self):
            return self.value

        def __str__(self):
            return 'CALL_' + str(self.value)

    # create a new instance
    e = _EventSource()

    # add a set of handlers
    e += Call(1)
    e += Call(2)
    e += Call(3)

    def callback(value):
        print('CALLBACK = ', value)

    e += callback

    # fire the handlers
    e.fire('A', 'B')

    # remove a handler
    e -= callback

    # fire the handlers
    e.fire('C')

# Generated at 2022-06-13 15:53:40.196348
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Verifies that the method fire correctly calls all handlers attached to the event
    # - Arguments are correctly passed to the handlers.
    # - If a handler raises an exception, the other handlers are still called.
    class _MockEventSource(_EventSource):
        def __init__(self):
            super(_MockEventSource, self).__init__()
            self._calls = list()

        def __len__(self):
            return len(self._calls)

        def __iter__(self):
            return iter(self._calls)

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._calls.append((handler, exc, args, kwargs))
            return False


# Generated at 2022-06-13 15:53:50.875224
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import unittest

    class Test(unittest.TestCase):
        def test_iadd_invalid(self):
            e = _EventSource()
            with self.assertRaises(ValueError):
                e += 'invalid'

        def test_iadd_first_handler(self):
            e = _EventSource()
            def first_handler(self):
                return True
            e += first_handler
            self.assertIn(first_handler, e._handlers)

        def test_iadd_second_handler(self):
            e = _EventSource()
            def first_handler(self):
                return True
            def second_handler(self):
                return True
            e += first_handler
            e += second_handler
            self.assertIn(first_handler, e._handlers)

# Generated at 2022-06-13 15:54:01.979896
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    e = _EventSource()

    def handler1(*args, **kwargs):
        print("HANDLER1 ARGS: %s KWARGS: %s" % (args, kwargs))

    def handler2(*args, **kwargs):
        # should not be invoked
        print("HANDLER2 ARGS: %s KWARGS: %s" % (args, kwargs))
        raise Exception()

    def handler3(*args, **kwargs):
        # should not be invoked
        print("HANDLER3 ARGS: %s KWARGS: %s" % (args, kwargs))
        raise Exception()

    e += handler1
    e += handler2

# Generated at 2022-06-13 15:54:25.038506
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def launch_chrome_browser(**kwargs):
        print(kwargs['url'])


    def launch_firefox_browser(**kwargs):
        print(kwargs['url'])

    # _EventSource instance
    event_source = _EventSource()

    # Append handlers: launch_chrome_browser and launch_firefox_browser for on_start event.
    event_source += launch_chrome_browser
    event_source += launch_firefox_browser

    # Remove handler: launch_firefox_browser from on_start event.
    event_source -= launch_firefox_browser

    # trigger "on_start" event
    event_source.fire(url='www.youtube.com')

test__EventSource_fire()

# Generated at 2022-06-13 15:54:36.454502
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(object):
        __metaclass__ = _AnsibleCollectionConfig

    event = MyEventSource()
    event.fire()

    class _TestHandler:
        def __init__(self, name):
            self._name = name
            self._on_call_count = 0

        def __call__(self, *args, **kwargs):
            self._on_call_count += 1

        @property
        def on_call_count(self):
            return self._on_call_count

    h1 = _TestHandler('h1')
    h2 = _TestHandler('h2')
    event += h1
    event.fire()
    assert h1.on_call_count == 1
    event += h2
    event.fire()
    assert h1.on_call_count == 2


# Generated at 2022-06-13 15:54:47.244431
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class _Dummy:
        did_handle = False
        handled_args = None
    dummy = _Dummy()

    # setup some dummy handlers
    def handler_1(foo, bar=None):
        dummy.did_handle = True
        dummy.handled_args = [foo, bar]

    def handler_2(foo, bar=None):
        dummy.handled_args = [foo, bar]
        raise Exception()

    # eventsource is setup exactly how it is in AnsibleCollectionConfig
    eventsource = _EventSource()
    eventsource._handlers = {handler_1, handler_2}

    # fire with args and kwargs
    eventsource.fire('foo', bar='bar')

    # did both handlers fire?
    assert len(eventsource._handlers) == 2

    # did the first handler store the args?


# Generated at 2022-06-13 15:54:55.318072
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    result = []

    def handler1(arg1, kwarg1=None):
        result.append((arg1, kwarg1))

    def handler_throws(*args, **kwargs):
        raise ValueError('Handler threw')

    event += handler1
    event += handler_throws

    with pytest.raises(ValueError):
        event.fire(1, kwarg1='foo')

    assert len(result) == 1
    assert result[0] == (1, 'foo')

# Generated at 2022-06-13 15:55:03.306626
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test setup
    log = []
    def handler_1(*args, **kwargs):
        log.append(('handler_1', args, kwargs))

    def handler_2(*args, **kwargs):
        log.append(('handler_2', args, kwargs))

    # Test
    es = _EventSource()
    es += handler_1
    es += handler_2
    es.fire(1, 2, 3)
    es.fire(a=1, b=2, c=3)

    # Verify

# Generated at 2022-06-13 15:55:12.904570
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # First, we test that the return value of a handler is passed upward.
    class EventSource1(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

        def my_handler(self, *args, **kwargs):
            return 'return value'

    es = EventSource1()
    assert es.fire() is None
    es += es.my_handler
    assert es.fire() == 'return value'

    # Next, we test that the exception raised from a handler is forwarded to the caller
    class EventSource2(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            raise exc

        def my_handler(self, *args, **kwargs):
            raise Exception('This is not a real error')

   

# Generated at 2022-06-13 15:55:22.742472
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible.module_utils._text import to_text

    def f1(s):
        assert s == 'a'

    def f2(s, n):
        assert s == 'b'
        assert n == 3

    def f3(s, n=None):
        assert s == 'c'
        assert n is None

    def f4(s, n=3):
        assert s == 'd'
        assert n == 3

    def f5(s, n=3, m=None):
        assert s == 'e'
        assert n == 7
        assert m is None

    def f6(s, n=3, m=4):
        assert s == 'f'
        assert n == 7
        assert m == 4


# Generated at 2022-06-13 15:55:35.172393
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from unittest import TestCase
    from unittest.mock import Mock

    class EventSourceTests(TestCase):
        def test_handler_does_not_raise(self):
            es = _EventSource()
            h = Mock()
            es += h
            es.fire()
            h.assert_called_once()

        def test_handler_raises_but_is_not_skipped(self):
            es = _EventSource()
            h = Mock(side_effect=Exception('testing 1 2 3'))
            es += h

            with self.assertRaisesRegex(Exception, 'testing 1 2 3'):
                es.fire()

            h.assert_called_once()

        def test_handler_raises_but_is_skipped(self):
            es = _EventSource()


# Generated at 2022-06-13 15:55:46.661843
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventHandler(object):
        def __init__(self):
            self.event_counter = 0
            self.exception_counter = 0
            self.event_catcher = None

        def __call__(self, *args, **kwargs):
            self.event_counter += 1
            self.event_catcher = (args, kwargs)
            return True

        def on_exception(self, handler, exc, *args, **kwargs):
            self.exception_counter += 1
            return True

    event_handler_1 = EventHandler()
    event_handler_2 = EventHandler()
    test_event_source = _EventSource()
    test_event_source += event_handler_1
    test_event_source += event_handler_2
    test_event_source._on_exception = event

# Generated at 2022-06-13 15:55:54.291390
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    # index the test classes by the number of parameters they specify
    class Events:
        class _0Args:
            def __call__(self):
                assert self.fired is False
                self.fired = True

        class _1Arg:
            def __call__(self, a):
                assert self.fired is False
                assert a == 1
                self.fired = True

        class _2Args:
            def __call__(self, a, b):
                assert self.fired is False
                assert a == 1
                assert b == 2
                self.fired = True

        class _1Arg1Kwarg:
            def __call__(self, a, d=4):
                assert self.fired is False
                assert a == 1
                assert d == 3
                self.fired = True


# Generated at 2022-06-13 15:56:27.582588
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class c:
        def test_handler1(self, a, b):
            self.handled1 += 1
            self.args1 = [a, b]
            self.kwargs1 = {}

    a1 = c()
    a1.handled1 = 0
    a2 = c()
    a2.handled1 = 0

    es = _EventSource()
    es += a1.test_handler1
    es += a2.test_handler1

    es.fire(1, 2)

    assert a1.handled1 == 1
    assert a1.args1 == [1, 2]
    assert a2.handled1 == 1
    assert a2.args1 == [1, 2]

# Generated at 2022-06-13 15:56:33.252787
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert len(event_source._handlers) == 0
    def my_handler():
        pass
    event_source += my_handler
    assert len(event_source._handlers) == 1
    assert my_handler in event_source._handlers


# Generated at 2022-06-13 15:56:40.831828
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    class _EventSourceTestCase:
        def get_handler(self, calls=None, raises=None, return_value=None, on_exception=None):
            from ansible.module_utils.common.collections import is_sequence

            calls = calls if calls is not None else []
            raises = raises if raises is not None else []
            return_value = return_value if return_value is not None else []

            def _handler(*args, **kwargs):
                calls.append((args, kwargs))
                if raises:
                    raise raises.pop(0)
                return return_value.pop(0) if return_value else None

            if on_exception:
                from ansible.module_utils.common.collections import is_sequence


# Generated at 2022-06-13 15:56:46.636750
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    es = _EventSource()

    # Test1: Test and validate fire method with no handlers
    assert not es.fire()

    # Test2: Test and validate fire method with a handler that returns None
    def test_fire_handler1():
        pass

    es += test_fire_handler1
    assert not es.fire()

    # Test3: Test and validate fire method with a handler that returns a value
    def test_fire_handler2():
        return 1

    es += test_fire_handler2
    assert es.fire() == 1

    # Test4: Test and validate fire method with a handler that raises an exception
    def test_fire_handler3():
        raise ValueError('unit test')

    es += test_fire_handler3
    try:
        es.fire()
    except ValueError as e:
        assert to_text

# Generated at 2022-06-13 15:56:58.155216
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _MockHandler:
        def __init__(self):
            self.handled_exception_count = 0
            self.handled_exception = None

        def _handle_exception(self, exc):
            self.handled_exception_count += 1
            self.handled_exception = exc

        @property
        def on_exception(self):
            return self._handle_exception

        @on_exception.setter
        def on_exception(self, value):
            if value is not self.on_exception:
                raise ValueError()

        def __call__(self, *args, **kwargs):
            raise KeyError('key')

    class _MockEventSource(_EventSource):
        def __init__(self):
            super(_MockEventSource, self).__init__()
           

# Generated at 2022-06-13 15:57:10.015432
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def on_exception(handler, exc, *args, **kwargs):
        raise exc

    es = _EventSource()
    es._on_exception = on_exception
    assert(es.fire(1, 2, 3, foo=4, bar=5) is None)

    es = _EventSource()
    es._on_exception = on_exception

# Generated at 2022-06-13 15:57:17.834583
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    assert event_source.fire() is None
    event_source += one
    assert event_source.fire() is None

    def two(*args, **kwargs):
        two.args = args
        two.kwargs = kwargs

    event_source += two
    assert event_source.fire(1, 2) is None
    assert one.args == (1, 2)
    assert one.kwargs == {}
    assert two.args == (1, 2)
    assert two.kwargs == {}

    event_source -= one
    assert event_source.fire(3, 4) is None
    assert one.args == (1, 2)
    assert one.kwargs == {}
    assert two.args == (3, 4)
    assert two.kwargs == {}

    event_source

# Generated at 2022-06-13 15:57:27.294256
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Given
    dummy_value = [1, 2, 3]
    different_value = [1, 2, 3, 4]
    parameters = 123, 'abc'
    keyword_parameters = {'a': 123, 'b': 'abc'}
    class ObjectReceiver:
        def __init__(self):
            self.values = []

        def handler(self, *args, **kwargs):
            self.values.append((args, kwargs))
    object_receiver = ObjectReceiver()

    def function_receiver(*args, **kwargs):
        function_receiver.values.append((args, kwargs))
    function_receiver.values = []

    es = _EventSource()

    # When
    es += object_receiver.handler
    es += object_receiver.handler

# Generated at 2022-06-13 15:57:30.685638
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def handler1(x):
        pass

    def handler2(x, y=0):
        pass

    def handler3(x):
        raise ArithmeticError()

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2
    event_source += handler3

    assert len(event_source._handlers) == 3



# Generated at 2022-06-13 15:57:40.749766
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSourceUnitTest(_EventSource):
        def __init__(self):
            super(_EventSourceUnitTest, self).__init__()
            self._called_handlers = []
            self._call_count = 0

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._call_count += 1
            self._called_handlers.append(handler)
            return False

    es = _EventSourceUnitTest()

    class _Handler:
        def __init__(self, name, exception=None):
            self._name = name
            self._exception = exception

        def __call__(self, *args, **kwargs):
            if self._exception:
                raise self._exception()

    class _Exception:
        pass


# Generated at 2022-06-13 15:58:47.814341
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def handler(a, b, c=10, d=20):
        assert a == 1
        assert b == 2
        assert c == 3
        assert d == 4

    event += handler
    event.fire(1, 2, c=3, d=4)

    class A:
        def fail(self):
            assert 0, 'this should never be called'

        def ok(self):
            assert 1

    a = A()

    def raise_error(a):
        if not a:
            raise ValueError()

    event += a.ok
    event += a.fail

    event._on_exception = lambda self, handler, exc, *args, **kwargs: handler == a.fail

    event.fire(1)

    # handler with non-matching "self"

# Generated at 2022-06-13 15:58:52.803814
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def handler_1(_):
        global seq
        seq.append(1)

    def handler_2(_):
        global seq
        seq.append(2)

    global seq
    seq = []

    event_source = _EventSource()
    event_source += handler_1
    event_source += handler_2

    event_source.fire()

    assert seq == [1, 2]



# Generated at 2022-06-13 15:58:59.617471
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # If handler is not callable, then a ValueError is raised.
    es = _EventSource()
    try:
        es += '/path/to/collection'
        assert False
    except ValueError:
        assert True

    # Otherwise, the handler is added to the set of registered handlers.
    es += (lambda *args, **kwargs: None)
    es += (lambda *args, **kwargs: None)
    handlers = es._handlers

    assert len(handlers) == 2
