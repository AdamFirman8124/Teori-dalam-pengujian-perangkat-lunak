

# Generated at 2022-06-13 15:49:05.347246
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible.test.lib.test_util.target._legacy_collection_loader._event_source import __test__
    __test__()


# Generated at 2022-06-13 15:49:06.684301
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()
    event += lambda: None



# Generated at 2022-06-13 15:49:16.098543
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # On controller and ansible-test, this code is not part of the class _EventSource, so import it here
    from .._util.target.legacy_collection_loader._event_source import _EventSource

    # Create the event source
    event_source = _EventSource()

    # Create a couple event handlers
    def event_handler_1(arg1):
        print('test__EventSource_fire event_handler_1(%s)' % arg1)

    def event_handler_2(arg1):
        print('test__EventSource_fire event_handler_2(%s)' % arg1)

    # Test the initial state of the event source
    assert len(event_source._handlers) == 0

    # Fire an event when no handlers are configured
    event_source.fire('first event')

    # Test the initial state of

# Generated at 2022-06-13 15:49:21.763781
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    def handler1(a, b, c=5):
        print(a, b, c)

    def handler2(a, b, c=5):
        print(a, b, c)

    event_source += handler1
    event_source += handler2

    event_source.fire(1, 2, 3)

    event_source -= handler1
    event_source -= handler2


if __name__ == '__main__':
    test__EventSource_fire()

# Generated at 2022-06-13 15:49:25.841042
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Callable:
        def __init__(self):
            self.called = False

        def __call__(self, *args, **kwargs):
            self.called = True
            return True

    c = Callable()

    e = _EventSource()
    e += c
    assert len(e._handlers) == 1
    assert not c.called

    e.fire(1, 2, 3)
    assert c.called



# Generated at 2022-06-13 15:49:31.110096
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(arg):
        if arg == 'boom':
            raise Exception('Boom')
        return arg
    def handler_filter(arg):
        return arg.startswith('filter-')

    source = _EventSource()
    source += handler
    source += handler_filter

    source.fire('foo')
    source.fire('boom')


# Generated at 2022-06-13 15:49:33.439212
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # VALIDATE_ARG_COUNT: 2,3
    es = _EventSource()
    on_collection_load = es.__iadd__
    on_collection_load(None)

# Generated at 2022-06-13 15:49:37.876889
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    value = []
    event_source.fire(value, [1, 2, 3])
    assert value == []

    def handler(value, array):
        value[:] = array

    event_source += handler
    try:
        event_source.fire(value, [4, 5, 6])
        assert value == [4, 5, 6]
    finally:
        event_source -= handler



# Generated at 2022-06-13 15:49:45.598935
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Handler:
        def __init__(self):
            self.call_count = 0
            self.raise_count = 0

        def __call__(self):
            self.call_count += 1
            if self.raise_count > 0:
                self.raise_count -= 1
                raise Exception()

    # These tests are focused on testing the raise logic in _EventSource.fire().
    # The firing of the handlers is not a concern here.

    # No handlers, no exception
    # -----------------------
    es = _EventSource()
    es.fire()

    # Single handler, no exception
    # --------------------------
    h1 = Handler()
    es = _EventSource()
    es += h1
    es.fire()
    assert h1.call_count == 1
    assert h1.raise_count == 0

   

# Generated at 2022-06-13 15:49:52.456293
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def my_handler(arg1, arg2):
        if 'value2' not in locals():
            value2 = None
        raise Exception('value1: %s, value2: %s' % (arg1, value2))

    events = _EventSource()
    events += my_handler

    try:
        events.fire('value1', arg2='value2')
        raise Exception('expected exception')
    except Exception as ex:
        assert str(ex) == 'value1: value1, value2: value2'

# Generated at 2022-06-13 15:50:05.187998
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _UnitTestException(Exception):
        def __init__(self, number):
            self.number = number

    s = _EventSource()

    # fire on empty is a no-op
    s.fire('foo')

    # add a handler that throws a UnitTestException
    h = s.__iadd__(lambda *args, **kwargs: _UnitTestException(1001))

    # fire when only a single handler has been added raises an exception
    exception = None
    try:
        s.fire('bar')
    except Exception as ex:
        exception = ex
    assert isinstance(exception, _UnitTestException)
    assert exception.number == 1001

    # fire when one of several handlers has been added raises an exception
    s.__iadd__(lambda *args, **kwargs: _UnitTestException(1002))

# Generated at 2022-06-13 15:50:15.890391
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    callee = 0
    def one(*args, **kwargs):
        global callee
        callee = 1
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}

    def two(*args, **kwargs):
        global callee
        callee = 2
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}

    def three(*args, **kwargs):
        global callee
        callee = 3
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}

    ev = _EventSource()
    ev += one
    ev += two
    ev += three

    ev.fire(1, 2, a='b')

    assert callee == 3



# Generated at 2022-06-13 15:50:26.135816
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEventSource(_EventSource):
        def __init__(self):
            super(_TestEventSource, self).__init__()
            self.failures = []

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.failures.append((handler, exc))

    test_instance = _TestEventSource()

    def handler1(foo, bar, baz):
        pass

    def handler2(foo, bar, baz):
        pass

    def handler3(foo, bar, baz):
        pass

    def handler4(foo, bar, baz):
        raise Exception("")

    def handler5(foo, bar, baz):
        raise Exception("")

    def handler6(foo, bar, baz):
        raise Exception("")

    test_instance += handler

# Generated at 2022-06-13 15:50:37.224761
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test with a single handler
    ev = _EventSource()
    handler_called = [False]

    def handler():
        handler_called[0] = True

    ev += handler

    ev.fire()

    assert handler_called[0] is True

    # test with two handlers
    ev = _EventSource()
    handler1_called = [False]
    handler2_called = [False]

    def handler1():
        handler1_called[0] = True

    def handler2():
        handler2_called[0] = True

    ev += handler1
    ev += handler2

    ev.fire()

    assert handler1_called[0] is True
    assert handler2_called[0] is True


# Generated at 2022-06-13 15:50:47.430098
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    result_2_handlers_0_exceptions = None
    result_3_handlers_1_exceptions = None
    result_3_handlers_3_exceptions = None

    def handler_1(*args, **kwargs):
        pass

    def handler_2(*args, **kwargs):
        pass

    def handler_3(*args, **kwargs):
        raise Exception('handler_3')

    def handler_4(*args, **kwargs):
        raise Exception('handler_4')

    def handler_5(*args, **kwargs):
        raise Exception('handler_5')

    event_source += handler_1
    event_source += handler_2

# Generated at 2022-06-13 15:50:57.996458
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestException(Exception):
        pass

    class EventSourceTester:
        def __init__(self):
            self.events = []

        def test_event(self, *args, **kwargs):
            self.events.append((args, kwargs))

        def test_event_with_exception(self, *args, **kwargs):
            self.events.append('pre')
            raise TestException('testing')
            self.events.append('post')

    test_object = EventSourceTester()

    event_source = _EventSource()
    event_source += test_object.test_event

    event_source.fire('args', foo='bar')
    assert test_object.events == [((('args',), {'foo': 'bar'}),)]

    test_object.events.clear()
    event

# Generated at 2022-06-13 15:51:06.026752
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def handler(a, b, c):
        return True

    handlers = (lambda a, b, c: True, lambda a, b, c: None, handler)

    for h in handlers:
        event += h

    status = event.fire(1, 2, 3)

    # If any of the handlers returns True, then the fire method should return True
    assert status is True

    event -= handler

    status = event.fire(1, 2, 3)

    assert status is None



# Generated at 2022-06-13 15:51:18.697368
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()
    event_source_raised_exception = []

    def handler(event_source, *args, **kwargs):

        event_source.handler_call_args = args
        event_source.handler_call_kwargs = kwargs
        event_source.handler_called = True

    def exception_handler(exception, event_source):
        event_source_raised_exception.append(exception)

    handlers = [handler, handler]
    exception_handlers = [exception_handler, exception_handler]

    event_source += handlers[0]
    event_source += handlers[1]
    event_source._on_exception += exception_handlers[0]
    event_source._on_exception += exception_handlers[1]


# Generated at 2022-06-13 15:51:26.706707
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    def first_handler(*p, **kw):
        pass

    def second_handler(*p, **kw):
        raise Exception('An exception occurred in test handler')

    event += first_handler
    event += second_handler
    try:
        event.fire()
    except Exception as ex:
        assert ex.args[0] == 'An exception occurred in test handler'



# Generated at 2022-06-13 15:51:32.190022
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    fired = [0]
    class Test_EventSource_fire():
        def __init__(self, fired):
            self.fired = fired
        def handler1(self):
            self.fired[0] += 1
        def handler2(self):
            self.fired[0] += 1
            raise Exception
        def handler3(self):
            self.fired[0] += 1
            raise Exception
    event_source = _EventSource()
    event_source += Test_EventSource_fire(fired).handler1
    event_source += Test_EventSource_fire(fired).handler2
    event_source += Test_EventSource_fire(fired).handler3

    assert fired == [0]
    event_source.fire()
    assert fired == [2]


# Generated at 2022-06-13 15:51:47.953392
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    global status

    status = dict(success=False, raised=None)
    a = _EventSource()

    def handler1(*args, **kwargs):
        nonlocal status
        # mutate some global state
        status['raised'] = False

    def handler2(*args, **kwargs):
        nonlocal status
        # mutate some global state
        status['raised'] = True
        raise Exception('test')

    def handler3(*args, **kwargs):
        nonlocal status
        # mutate some global state
        status['success'] = True

    a += handler1
    a += handler2
    a += handler3
    try:
        a.fire()
        raise AssertionError('should have raised')
    except:
        pass

    assert status == dict(success=True, raised=True)



# Generated at 2022-06-13 15:51:52.541704
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(a, b=2, c=3):
        pass

    def handler2(a, b=2, c=3):
        pass

    es = _EventSource()
    es += handler1
    es += handler2
    es.fire('foo', b=2, c=3)


# Unit tests for class AnsibleCollectionConfig

# Generated at 2022-06-13 15:51:55.421578
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()


    def test_handler():
        return 2


    es += test_handler

    assert test_handler in es._handlers


# Generated at 2022-06-13 15:52:06.784380
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    # test the case where no exceptions are raised
    events = _EventSource()
    count = [0]

    def _incr(i):
        count[0] += i

    _ = events
    _ += _incr
    _ += _incr
    events.fire(1)

    assert count[0] == 2

    # test the case where exceptions are not handled
    count[0] = 0
    events = _EventSource()
    _ = events
    _ += _incr
    _ += _incr
    _ += lambda: 1 / 0
    _ += _incr

    with pytest.raises(ZeroDivisionError):
        events.fire(1)

    assert count[0] == 0

    # test case where exceptions are handled
    count[0] = 0
    events = _Event

# Generated at 2022-06-13 15:52:14.177731
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    events = []
    event_source += lambda *args, **kwargs: events.append((args, kwargs))
    event_source += lambda *args, **kwargs: events.append((args, kwargs))
    event_source.fire('A')
    assert events == [((('A',),), {}), (('A',), {})]
    events = []

    event_source += lambda *args, **kwargs: events.append((args, kwargs))
    event_source += lambda *args: events.append((args,))
    event_source += lambda: events.append(None)
    event_source.fire(1, 'two', three='four')

# Generated at 2022-06-13 15:52:22.505997
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceSubClass(_EventSource):
        def call_count(self):
            return len(self._handlers)

        def _on_exception(self, handler, ex, *args, **kwargs):
            return False

    e = EventSourceSubClass()
    assert e.call_count() == 0

    def f():
        pass

    e += f
    assert e.call_count() == 1

    e += f
    assert e.call_count() == 2

    e -= f
    assert e.call_count() == 1

    e -= f
    assert e.call_count() == 1

    def g():
        return True

    e += g
    assert e.call_count() == 2

    def h():
        raise Exception('test exception')

    e += h
    assert e.call_count()

# Generated at 2022-06-13 15:52:32.284659
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MockEventSource(_EventSource):
        def __init__(self):
            super(MockEventSource, self).__init__()
            self._on_exception_call_stack = []
            self._on_exception_default_return_value = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            # record call stack for unit test
            this_call_stack = self._on_exception_call_stack
            this_call_stack.append(str((handler, exc, args, kwargs)))

            # if we have been configured to return a specific return value for the next call, return that now
            if self._on_exception_default_return_value is not None:
                rval = self._on_exception_default_return_value
                self._on_ex

# Generated at 2022-06-13 15:52:36.483445
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    x = _EventSource()

    def f():
        pass

    x += f

    assert len(x._handlers) == 1
    assert x._handlers == set([f])


# Generated at 2022-06-13 15:52:41.061161
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_func():
        pass

    event_source = _EventSource()
    event_source += test_func

    event_source.fire()
    assert event_source._handlers == {test_func}


# Generated at 2022-06-13 15:52:43.869573
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():  # noqa: E302
    def dummy(*args, **kwargs):
        pass

    o = _EventSource()
    o += dummy
    o += dummy
    assert len(o._handlers) == 2

# Generated at 2022-06-13 15:52:48.982884
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    raise NotImplementedError()

# Generated at 2022-06-13 15:52:53.366789
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # arrange
    ev = _EventSource()
    assert not ev._handlers

    # act
    ev += lambda x: x

    # assert
    assert ev._handlers
    assert len(ev._handlers) == 1


# Generated at 2022-06-13 15:52:57.103226
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    handler_called = 0
    def handler(*args, **kwargs):
        nonlocal handler_called
        handler_called += 1
    event += handler

    event.fire()
    assert handler_called == 1



# Generated at 2022-06-13 15:53:06.679461
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    class TestError(Exception):
        pass

    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            if isinstance(exc, TestError):
                return False
            return True

    class Tests(unittest.TestCase):
        def test__EventSource_fire(self):
            target = MyEventSource()

            handlers = [self._create_handler(v) for v in range(100)]
            for h in handlers:
                target += h

            target.fire()

            self.assertEqual(handlers[0].count, 1)
            self.assertEqual(handlers[-1].count, 1)


# Generated at 2022-06-13 15:53:19.777085
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    ev = _EventSource()
    assert ev._handlers == set()


if __name__ == '__main__':
    args, _ = parser.parse_known_args()

    if args.test:
        test__EventSource___iadd__()
        sys.exit(0)

    test__EventSource___iadd__()
    sys.exit(1)


# -*- -*- -*- End included fragment: lib/ansible/utils/collection_loader/_collection_config.py -*- -*- -*-

# -*- -*- -*- Begin included fragment: lib/ansible/utils/collection_loader/_collection_finder_mixin.py -*- -*- -*-

# (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or

# Generated at 2022-06-13 15:53:29.273327
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def callback1(arg1, arg2, kwarg1=None):
        pass

    def callback2(arg1, arg2, kwarg1=None):
        pass

    e = _EventSource()
    e.fire(1, 2, kwarg1=0)
    e += callback1
    e.fire(1, 2, kwarg1=0)
    e += callback2
    e.fire(1, 2, kwarg1=0)
    e -= callback1
    e.fire(1, 2, kwarg1=0)
    e -= callback2
    e.fire(1, 2, kwarg1=0)



# Generated at 2022-06-13 15:53:38.027262
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    # test with no handler installed
    event_source.fire(1)

    # install handler
    def handler(n):
        handler.x += n

    handler.x = 0
    event_source += handler
    assert 1 == len(event_source._handlers)

    # fire with non-exception handler
    event_source.fire(1)
    assert 1 == handler.x

    # fire with non-exception handler
    event_source.fire(2)
    assert 3 == handler.x

    # remove handler
    event_source -= handler
    assert 0 == len(event_source._handlers)

    # fire with no handler installed
    event_source.fire(1)

# Generated at 2022-06-13 15:53:49.495238
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self.hits = set()
            self.errors = 0
            self.logs = dict()

        def log(self, logtext):
            self.hits.add(logtext)

        def fail(self, *args, **kwargs):
            self.errors += 1
            self.log('fail: %s %s' % (args, kwargs))

        def log_exception(self, handler, exc):
            self.log('exception: %s: %s' % (handler, exc))

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.log_exception(handler, exc)
            return False


# Generated at 2022-06-13 15:53:55.105598
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler1():
        pass
    def handler2():
        raise ValueError('test')

    event_source += handler1
    event_source += handler2
    assert len(event_source._handlers) == 2
    assert handler1 in event_source._handlers
    assert handler2 in event_source._handlers


# Generated at 2022-06-13 15:54:01.324062
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    handler_called_with = []

    def handler(*args, **kwargs):
        handler_called_with.append((args, kwargs))

    event_source = _EventSource()
    event_source += handler
    event_source.fire(1, 2, three=3, four=4)

    assert handler_called_with == [((), {}), ((1, 2), dict(three=3, four=4))]



# Generated at 2022-06-13 15:54:19.539998
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from collections import namedtuple

    OldTuple = namedtuple('OldTuple', 'a b')
    NewTuple = namedtuple('NewTuple', 'a b c', rename=True)

    def make_handler():
        class _Handler(object):
            def __init__(self):
                self.called = False

            def __call__(self, *args, **kwargs):
                self.called = True

        return _Handler()

    source = _EventSource()
    handler = make_handler()

    # No handler registered, test method fire()
    source.fire()

    # Register a handler and test method fire()
    source += handler
    source.fire()
    assert handler.called

    # Can add a different handler of the same type
    handler2 = make_handler()
    source += handler2
    source

# Generated at 2022-06-13 15:54:23.940163
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler1():
        pass

    try:
        event_source += handler1
    except ValueError:
        assert False

    try:
        event_source += 1
    except ValueError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 15:54:32.073274
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    assert len(AnsibleCollectionConfig._on_collection_load._handlers) == 0
    test_events = []
    AnsibleCollectionConfig._on_collection_load += lambda c, p: test_events.append((c, p))
    assert len(AnsibleCollectionConfig._on_collection_load._handlers) == 1

    AnsibleCollectionConfig._on_collection_load.fire('collection', 'path')
    assert test_events == [('collection', 'path')]

# Generated at 2022-06-13 15:54:35.488360
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    counter = 0
    def handle(incr):
        nonlocal counter
        counter += incr

    event += handle

    event.fire(8)
    assert counter == 8

    event -= handle

    event.fire(16)
    assert counter == 8

# Generated at 2022-06-13 15:54:46.480266
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTester(object):
        def foo(self):
            self.calls.append('foo_called')
            raise RuntimeError('foo_error')

        def bar(self):
            self.calls.append('bar_called')

        @staticmethod
        def _on_exception(_, exc, *args, **kwargs):
            return exc.args[0] != 'foo_error'

        def test(self, handler):
            self.calls = []

            es = _EventSource()
            es.on_exception = self._on_exception
            es += handler

            es.fire('arg', kwarg='kwarg')
            return self.calls

    tester = EventSourceTester()

    assert tester.test(tester.foo) == ['foo_called']
    assert tester

# Generated at 2022-06-13 15:54:47.653307
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: print('foo')



# Generated at 2022-06-13 15:54:54.829796
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import mock

    def handler(arg, kwarg=None):
        pass

    handler_mock = mock.MagicMock(side_effect=handler)

    source = _EventSource()

    source += handler_mock
    source.fire('foo', kwarg='bar')

    handler_mock.assert_called_once_with('foo', kwarg='bar')

    source.fire('foo', kwarg='bar')
    assert handler_mock.call_count == 2

# Generated at 2022-06-13 15:54:58.384525
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    called_count = {'count': 0}

    def add():
        called_count['count'] += 1

    event_source += add
    event_source.fire()

    assert called_count['count'] == 1



# Generated at 2022-06-13 15:55:05.582334
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Arrange
    class MyException(Exception): pass

    def handler_one(n):
        return n

    def handler_two(n, m):
        return n + m

    def handler_three(n):
        return n + 2

    def handler_four(n):
        return n + 3

    source = _EventSource()

    exceptions = {}

    # Act
    source += handler_one
    source += handler_two
    source += handler_three
    source += handler_four

    # Remove handler_three
    source -= handler_three

    # Remove handler_four
    source -= handler_four

    try:
        # Call handlers
        source.fire(1, 2)
    except Exception as e:
        exceptions['source.fire'] = e

    # Assert

    # handler_one and handler_two should have

# Generated at 2022-06-13 15:55:08.678077
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    counter = [0]

    def handler():
        counter[0] += 1

    event = _EventSource()
    event += handler

    # test handler is called
    event.fire()
    assert counter[0] == 1

# Generated at 2022-06-13 15:55:36.123993
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class EventSourceStub(_EventSource):
        pass

    event_source = EventSourceStub()
    fired = []

    def handler_1(arg):
        fired.append('1_%s' % arg)

    def handler_2(arg):
        fired.append('2_%s' % arg)

    def handler_3(arg):
        fired.append('3_%s' % arg)

    event_source += handler_1
    event_source += handler_2
    event_source += handler_3

    arg = 'foo'
    event_source.fire(arg)

    assert len(fired) == 3
    assert fired[0] == '1_foo'
    assert fired[1] == '2_foo'
    assert fired[2] == '3_foo'



# Generated at 2022-06-13 15:55:47.493848
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # if we return True, we want the caller to re-raise
    def on_exception(handler, exception, *args, **kwargs):
        return True

    foo = _EventSource()
    foo._on_exception = on_exception

    def handler_one(*args, **kwargs):
        raise Exception('handler_one')

    def handler_two(*args, **kwargs):
        raise Exception('handler_two')

    foo += handler_one
    foo += handler_two

    try:
        foo.fire()
    except Exception as ex:
        assert str(ex) == 'handler_one'
    else:
        raise Exception('missing exception')

    # handler_one should have been removed as a result of the exception
    try:
        foo.fire()
    except Exception as ex:
        assert str(ex)

# Generated at 2022-06-13 15:55:52.113850
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    handler1 = lambda: None
    handler2 = lambda: None
    handler3 = "test"

    es = _EventSource()

    es += handler1
    es += handler2

    try:
        es += handler3
    except ValueError:
        pass

    assert handler1 in es._handlers
    assert handler2 in es._handlers
    assert handler3 not in es._handlers


# Generated at 2022-06-13 15:55:55.408784
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += _EventSource.__add__
    assert _EventSource.__add__ in es._handlers
    assert len(es._handlers) == 1


# Generated at 2022-06-13 15:55:58.230109
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # Setup
    test_class = _EventSource()

    # Test execution
    with pytest.raises(NotImplementedError):
        test_class.fire()



# Generated at 2022-06-13 15:56:06.516217
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MockException(Exception):
        pass

    cls1 = _EventSource()
    cls2 = _EventSource()
    source = _EventSource()

    # create events to fire
    def handler1(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}

    def handler2(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}
        raise MockException('i am meant to be raised')

    def handler3(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 'b'}
        raise Exception('not meant to be caught')

    # create mock handler for exception raised by handler2

# Generated at 2022-06-13 15:56:10.329579
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    from ansible.module_utils.six import PY3

    es = _EventSource()

    # emits no exceptions
    es.fire()

    with pytest.raises(TypeError):
        es += 'not callable'

    def handler_func(self):
        pass

    es += handler_func
    if PY3:
        es -= handler_func

    es.fire()

# Generated at 2022-06-13 15:56:13.106197
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += lambda x: x
    e += lambda x: x

    assert len(e._handlers) == 2  # nosec



# Generated at 2022-06-13 15:56:24.116648
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import os
    import sys
    import tempfile
    from ansible_test._internal.constants import CollectionLocations

    current_dir = os.path.dirname(os.path.abspath(__file__))
    collection_dir = os.path.dirname(os.path.dirname(current_dir))
    ansible_dir = os.path.dirname(collection_dir)
    ansible_test_dir = os.path.join(ansible_dir, 'test')
    test_lib_dir = os.path.join(ansible_test_dir, 'lib')

    sys.path.insert(0, test_lib_dir)
    from ansible_test.legacy_collection_loader import CollectionLoader

    AnsibleCollectionConfig.collection_finder = CollectionLoader()
    AnsibleCollectionConfig.collection_finder

# Generated at 2022-06-13 15:56:28.072128
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event = _EventSource()

    def handler(arg):
        pass

    first_handler = event + handler
    assert first_handler is event
    assert handler in event._handlers

    second_handler = event + handler
    assert second_handler is event
    assert handler in event._handlers


# Generated at 2022-06-13 15:57:12.859832
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible_collections.collection_loader._event_source import _EventSource
    from ansible_collections.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.module_utils.six import PY2
    import time

    es = _EventSource()
    a = []

    def handler1(a):
        a.append('handler1')

    def handler2(a):
        a.append('handler2')

    def handler3(a):
        a.append('handler3')

    def handler4(a):
        a.append('handler4')
        raise RuntimeError()

    es += handler1
    es += handler2
    es += handler3
    es += handler4

    es.fire(a)

# Generated at 2022-06-13 15:57:18.581178
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Test with a valid handler
    event_source = _EventSource()
    event_source += lambda: None
    assert len(event_source._handlers) == 1

    # Test with an invalid handler, expect a ValueError
    event_source = _EventSource()
    try:
        event_source += 'not a callable'
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError for non callable handler'



# Generated at 2022-06-13 15:57:27.941281
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class EventSourceTest:
        def __init__(self):
            self.events = _EventSource()
            self.events += self._event_method
            self.event_method_invoked = False
            self.event_method_args = None

        def _event_method(self, *args, **kwargs):
            self.event_method_invoked = True
            self.event_method_args = (args, kwargs)

    instance = EventSourceTest()
    assert not instance.event_method_invoked

    instance.events.fire('a', bar='baz')
    assert instance.event_method_invoked
    args, kwargs = instance.event_method_args
    assert args == ('a',)
    assert kwargs == {'bar': 'baz'}

# Generated at 2022-06-13 15:57:35.433173
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert len(event_source._handlers) == 0
    def handler1(event_source):
        pass
    def handler2(event_source):
        pass
    event_source += handler1
    assert len(event_source._handlers) == 1
    assert handler1 in event_source._handlers
    event_source += handler2
    assert len(event_source._handlers) == 2
    assert handler1 in event_source._handlers
    assert handler2 in event_source._handlers


# Generated at 2022-06-13 15:57:40.188624
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def _h1(*args, **kwargs):
        pass

    def _h2(*args, **kwargs):
        pass

    es = _EventSource()
    es += _h1
    es += _h2
    assert len(es._handlers) == 2
    assert _h1 in es._handlers
    assert _h2 in es._handlers



# Generated at 2022-06-13 15:57:50.367470
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest
    import warnings

    class EventSourceTest(unittest.TestCase):
        def test_handler_called(self):
            called = {}

            def handler(**kwargs):
                called.update(kwargs)

            source = _EventSource()
            source += handler
            source.fire(key='value')

            self.assertEqual(called, {'key': 'value'})

        def test_handler_supports_multiple_arguments(self):
            called = {}

            def handler(key_value, name_value):
                called['key_value'] = key_value
                called['name_value'] = name_value

            source = _EventSource()
            source += handler
            source.fire('key', name_value='value')


# Generated at 2022-06-13 15:57:58.451548
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # pylint: disable=protected-access

    def on_exception(handler, exc, *args, **kwargs):
        raise NotImplementedError

    # test normal function call
    evt = _EventSource()
    evt._on_exception = on_exception

    calls = []

    def handler_1(*args, **kwargs):
        calls.append(('handler_1', args, kwargs))

    def handler_2(*args, **kwargs):
        calls.append(('handler_2', args, kwargs))
        return calls

    evt += handler_1
    evt += handler_2

    final = evt.fire('foo', 'bar', kw='zoo')

# Generated at 2022-06-13 15:58:05.151025
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_handler(arg1, arg2):
        return (arg1, arg2)

    def test_handler_bad(arg1, arg2):
        raise ValueError('bad')

    def test_handler_exception_filter(handler, exc, arg1, arg2):
        if isinstance(exc, ValueError):
            return False
        return True

    test_source = _EventSource()
    test_source += test_handler
    test_source += test_handler_bad

    # test fire
    assert test_source.fire('a', arg2='b') == [('a', 'b'), ('a', 'b')]

    # test handler removal
    test_source -= test_handler_bad
    assert test_source.fire('a', arg2='b') == [('a', 'b')]

    # test handler

# Generated at 2022-06-13 15:58:13.829157
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Note that this is the unit test for the ansible-test implementation of the event source,
    # not the controller implementation.
    es = _EventSource()
    args = (1, 2, 3)
    kwargs = dict(foo=1, bar=2)
    events = []

    # do not raise
    def handler1(*args, **kwargs):
        events.append((1, args, kwargs))

    es += handler1
    es.fire(*args, **kwargs)
    assert events == [(1, args, kwargs)]

    # raise but do not re-raise
    def handler2(*args, **kwargs):
        events.append((2, args, kwargs))
        raise Exception()

    es += handler2
    es.fire(*args, **kwargs)

# Generated at 2022-06-13 15:58:15.769359
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    assert not event_source._handlers
    event_source += lambda: None
    assert event_source._handlers
