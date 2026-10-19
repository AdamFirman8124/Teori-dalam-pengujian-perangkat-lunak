

# Generated at 2022-06-13 15:49:05.738090
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(value):
        print(value)

    def handler_with_exception(value):
        raise RuntimeError('oops')

    s = _EventSource()
    s += handler
    s += handler_with_exception

    s.fire(10)

# Generated at 2022-06-13 15:49:15.403146
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called_with = []

    def f1(*args, **kwargs):
        called_with.append((args, kwargs))

    def f2(*args, **kwargs):
        called_with.append((args, kwargs))

    def f3(*args, **kwargs):
        called_with.append((args, kwargs))
        raise Exception('f3')

    def f4(*args, **kwargs):
        called_with.append((args, kwargs))
        raise Exception('f4')

    class EventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            if handler is f4:
                # force handler f4 to re-raise
                return True
            return False

    es = EventSource()
    es += f1
   

# Generated at 2022-06-13 15:49:18.560529
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    def handler1():
        pass

    def handler2():
        pass

    event_source += handler1
    event_source += handler2

    assert len(event_source._handlers) == 2



# Generated at 2022-06-13 15:49:24.335855
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    global called
    called = 0

    def event_handler():
        global called
        called += 1

    event += event_handler
    event += event_handler

    event.fire()
    assert called == 2

    class TestException(Exception):
        pass

    def event_handler_that_raises():
        raise TestException('test exception')

    event += event_handler_that_raises
    called = 0

    try:
        event.fire()
        assert False, 'Expected TestException'
    except TestException:
        assert called == 1

# Generated at 2022-06-13 15:49:31.852316
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    def handler1(arg1, arg2, arg3='not used'):
        print('handler1: %s, %s' % (arg1, arg2))
    def handler2(arg1, arg2):
        print('handler2: %s, %s' % (arg1, arg2))
    print('handler1: %s' % handler1)
    print('handler2: %s' % handler2)
    es.__iadd__(handler1)
    es.__iadd__(handler2)
    es.fire('one', 'two')


# Generated at 2022-06-13 15:49:36.490522
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    called = []

    def handler1(*args, **kwargs):
        called.append((args, kwargs))

    def handler2(*args, **kwargs):
        raise RuntimeError("bad handler")

    event += handler1
    event += handler2

    with pytest.raises(RuntimeError, match="bad handler"):
        event.fire(1, 2, 3)

    assert called == [(1, 2, 3)]



# Generated at 2022-06-13 15:49:46.049905
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _EventSourceTester:
        def __init__(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs
            self.exception = None

        def __call__(self, *args, **kwargs):
            try:
                self.func(*args, **kwargs)
            except BaseException as e:
                self.exception = e

    event_source = _EventSource()
    counter = 0
    exceptions = []

    def on_exception(handler, exc):
        nonlocal counter

        counter += 1
        if counter < 3:
            return True
        else:
            return False

    event_source._on_exception = on_exception


# Generated at 2022-06-13 15:49:50.127602
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    c = _EventSource()
    c += lambda x: x + 1
    assert callable(c._handlers.pop())
    c += 1
    assert False, 'should have raised a ValueError'

# Generated at 2022-06-13 15:49:52.278534
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def a(): pass
    es = _EventSource()
    es += a
    assert a in es._handlers
    assert 1 == len(es._handlers)


# Generated at 2022-06-13 15:50:03.367169
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def a():
        raise ValueError('test error')

    def b():
        raise Exception('test exception')

    def c(exc):
        raise exc

    def d():
        return 'test return'

    def e():
        return 'test return'

    def f():
        return 'test return'

    # prepare test

    source = _EventSource()

    assert len(source._handlers) == 0

    # add handlers

    source += a
    source += b
    source += c
    source += d
    source += e
    source += f

    assert len(source._handlers) == 6

    def on_exception(handler, exc, *args, **kwargs):
        e_result = e()
        del source._handlers
        return False

    source._on_exception = on_exception

    #

# Generated at 2022-06-13 15:50:12.044230
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler():
        pass

    e = _EventSource()
    assert len(e._handlers) == 0
    e += handler
    assert len(e._handlers) == 1
    e += handler
    assert len(e._handlers) == 1
    e -= handler
    assert len(e._handlers) == 0


# Generated at 2022-06-13 15:50:21.332024
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self.on_exception = _EventSource()
            self.exception = None

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.exception = exc
            self.on_exception.fire(handler=handler, exc=exc, args=args, kwargs=kwargs)

    def test_handler_1(arg):
        sum_of_args['test_handler_1'] += arg

    def test_handler_2(arg):
        sum_of_args['test_handler_2'] += arg

    def test_handler_3(arg):
        sum_of_args['test_handler_3'] += arg
        raise RuntimeError

# Generated at 2022-06-13 15:50:27.225771
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    foo = _EventSource()

    def f0():
        print("0")

    def f1():
        print("1")

    def f2():
        print("2")

    foo += f0
    foo += f1
    foo += f2
    foo += f0

    foo.fire()

# Generated at 2022-06-13 15:50:32.935816
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class _Foo:
        pass

    es = _EventSource()

    def foo(arg):
        pass

    def bar(arg):
        raise Exception('foo')

    def baz(arg):
        raise KeyboardInterrupt('foo')

    es += None
    es += foo
    es += bar
    es += baz

    assert(len(es._handlers) == 3)

# Generated at 2022-06-13 15:50:37.450037
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Foo(object):
        def f(self, a):
            self.a = a
    foo = Foo()

    es = _EventSource()
    es += foo.f
    assert len(es._handlers) == 1

    es.fire(3)
    assert foo.a == 3

    # Test removal
    assert len(es._handlers) == 1
    es -= foo.f
    assert len(es._handlers) == 0



# Generated at 2022-06-13 15:50:40.541136
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    event_source += lambda *args, **kwargs: None

    event_source.fire()

# Generated at 2022-06-13 15:50:42.416032
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    e = _EventSource()
    def handler(message):
        print(message)

    e += handler
    e.fire('Hello World!')

# Generated at 2022-06-13 15:50:44.457307
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += lambda e: None
    assert len(event_source._handlers) == 1


# Generated at 2022-06-13 15:50:48.220252
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_one(arg):
        assert arg == 'foo'

    def handler_two(arg):
        assert arg == 'foo'

    test_source = _EventSource()

    test_source += handler_one
    test_source += handler_two

    test_source.fire('foo')


# Generated at 2022-06-13 15:50:51.895595
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()

    assert len(es._handlers) == 0

    with pytest.raises(ValueError):
        es += 'not a callable'

    def handler(arg):
        pass

    es += handler

    assert len(es._handlers) == 1

    es += handler

    assert len(es._handlers) == 1


# Unit tests for class _AnsibleCollectionConfig

# Generated at 2022-06-13 15:51:01.615171
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    eventsource = _EventSource()

    def h1(*args, **kwargs):
        return 1

    def h2(*args, **kwargs):
        return 2

    def h3(*args, **kwargs):
        raise ValueError('boom')

    eventsource += h1
    eventsource += h2
    eventsource += h3

    assert eventsource.fire() == 1
    assert eventsource.fire() == 2
    try:
        eventsource.fire()
        assert False
    except ValueError:
        pass

# Generated at 2022-06-13 15:51:13.858023
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from collections import namedtuple
    from ansible_collections.ansible.builtin.plugins.module_utils.ansible_nxos_module import AnsibleNxosModule as M
    from ansible_collections.ansible.builtin.plugins.module_utils.collection_loader._collection_finder import _AnsibleCollectionFinder as _CF

    # define an event handler
    def handler():
        pass

    # define an AnsibleCollectionFinder
    cf = _CF()

    # install the AnsibleCollectionFinder
    AnsibleCollectionConfig.collection_finder = cf

    # install the handler on the on_collection_load event
    AnsibleCollectionConfig.on_collection_load += handler

    # define a collection name
    name = 'test-collection'

    # define a collection path
    path = '/tmp/'

   

# Generated at 2022-06-13 15:51:20.524895
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called = []

    def handler_one(x):
        called.append(('one', x))

    def handler_two(x):
        called.append(('two', x))

    evt = _EventSource()
    evt += handler_one
    evt += handler_two

    evt.fire(42)
    assert called == [('one', 42), ('two', 42)]

    del called[:]
    evt -= handler_one

    evt.fire('forty-two')
    assert called == [('two', 'forty-two')]

    # the next delete should be a no-op
    evt -= handler_one

    del called[:]
    evt.fire('one', 'two', 'three')
    assert called == [('two', 'one', 'two', 'three')]


#

# Generated at 2022-06-13 15:51:32.409322
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    global _EventSource

    class _EventSource:
        def __init__(self):
            self.events = []

        def __iadd__(self, handler):
            self.events.append(('__iadd__', handler))
            return self

        def __isub__(self, handler):
            self.events.append(('__isub__', handler))
            return self

        def _on_exception(self, handler, exc, *args, **kwargs):
            # if we return True, we want the caller to re-raise
            return True


# Generated at 2022-06-13 15:51:35.122880
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_handler(*args, **kwargs):
        return args, kwargs

    e = _EventSource()
    e += test_handler

    test_args = ('a', 'b')
    test_kwargs = dict(c=3)
    result = e.fire(*test_args, **test_kwargs)

    assert result == ((test_args, test_kwargs))


# Generated at 2022-06-13 15:51:46.963455
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # test successful execution without raising
    def test_handler(event):
        if event != 'test':
            raise Exception('expecting event == "test", got event: %s' % event)
    es = _EventSource()
    es += test_handler
    es.fire('test')

    # test exception case handled by on_exception handler
    def test_handler_error(event):
        raise Exception('test exception')

    def on_exception_handler(handler, exception, *args, **kwargs):
        # Return False to suppress re-raise of exception
        if isinstance(exception, Exception) and exception.args[0] == 'test exception':
            return False

        return True

    es = _EventSource()
    es += test_handler_error
    es._on_exception = on_exception_handler
    es

# Generated at 2022-06-13 15:51:54.733598
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class MyEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False

    # __iadd__ not exception
    e = MyEventSource()

    handler1 = [1, 2]
    e += handler1

    handler2 = lambda x: x
    e += handler2

    assert handler1 in e._handlers
    assert handler2 in e._handlers

    # __iadd__ throw value error
    e = MyEventSource()
    with pytest.raises(ValueError, match=r'handler must be callable'):
        e += 'hello world'


# Generated at 2022-06-13 15:52:06.278605
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    assert isinstance(_AnsibleCollectionConfig.on_collection_load, _EventSource)

    # test that fire with no handlers doesn't cause an error
    _AnsibleCollectionConfig.on_collection_load.fire(None)

    def handler1(*args, **kwargs):
        print('in handler1')

    def handler2(*args, **kwargs):
        print('in handler2')

    # test that the fire causes each handler to be called
    _AnsibleCollectionConfig.on_collection_load += handler1
    _AnsibleCollectionConfig.on_collection_load += handler2

    _AnsibleCollectionConfig.on_collection_load.fire(None)

    _AnsibleCollectionConfig.on_collection_load -= handler1
    _AnsibleCollectionConfig.on_collection_load -= handler2

# Generated at 2022-06-13 15:52:15.637934
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from ansible_collections.community.general.tests.unit.compat import unittest

    class TestClass(unittest.TestCase):
        def test_fire(self):

            def handler_a():
                raise ValueError('handler a')

            def handler_b():
                raise RuntimeError('handler b')

            def handler_c():
                raise AttributeError('handler c')

            def on_exception(handler, exc, *args, **kwargs):
                self.assertEqual('handler a', str(exc))
                self.assertTrue(callable(handler))
                self.assertEqual(0, len(args))
                self.assertEqual(0, len(kwargs))
                return False

            event_source = _EventSource()
            event_source += handler_a
            event_source += handler_

# Generated at 2022-06-13 15:52:20.078940
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    assert event_source._handlers is not None
    assert len(event_source._handlers) == 0
    assert event_source._on_exception is not None
    args = []
    kwargs = {}
    event_source.fire(args, kwargs)
    assert len(event_source._handlers) == 0

# Generated at 2022-06-13 15:52:27.438787
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # given
    e = _EventSource()
    flag = [0]
    def handler1(*args, **kwargs):
        flag[0] = 1
    e += handler1

    # when
    e.fire()

    # then
    assert flag[0] == 1

# Generated at 2022-06-13 15:52:32.337017
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    source = _EventSource()
    source.on_exception = lambda handler, ex, *args, **kwargs: True

    def one(*args, **kwargs):
        raise Exception('test__EventSource_fire')

    def two(*args, **kwargs):
        raise Exception('test__EventSource_fire')

    source += one
    source += two

    try:
        source.fire()
        assert False, 'expected exception'
    except Exception as ex:
        assert str(ex) == 'test__EventSource_fire', 'expected exception'

    source -= one

    try:
        source.fire()
        assert False, 'expected exception'
    except Exception as ex:
        assert str(ex) == 'test__EventSource_fire', 'expected exception'

# Generated at 2022-06-13 15:52:40.316416
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()

    state = {'result': None}

    def handler1(a, b):
        state['result'] = a + b

    def handler2(a, b):
        state['result'] = a - b

    event += handler1
    event += handler2

    event.fire(1, 2)
    assert state['result'] == 1

    event.fire(3, 2)
    assert state['result'] == 1

# Generated at 2022-06-13 15:52:48.765160
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _MockEventHandler:
        def __init__(self, expected_event_data=None, expected_event_data2=None):
            self.expected_event_data = expected_event_data
            self.expected_event_data2 = expected_event_data2

        def handle_event(self, event_data, event_data2):
            assert event_data == self.expected_event_data
            assert event_data2 == self.expected_event_data2

    e = _EventSource()

    e += _MockEventHandler(1, 2)
    e.fire(1, event_data2=2)

    e += _MockEventHandler(1, 2)
    e += _MockEventHandler(2, 3)
    e.fire(1, event_data2=2)

    e -= _

# Generated at 2022-06-13 15:52:53.874975
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_callable = getattr(event_source, '_on_exception')

    event_source += event_callable

    assert len(event_source._handlers) == 1
    assert event_callable in event_source._handlers

# Generated at 2022-06-13 15:53:02.438716
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    called = []

    class Handler:
        def __call__(self, *args, **kwargs):
            called.append((self, args, kwargs))

    e = _EventSource()
    h1 = Handler()
    h2 = Handler()
    e += h1
    e += h2

    e.fire(1, 2, 3)

    assert len(called) == 2
    assert called[0][0] == h1
    assert called[0][1] == (1, 2, 3)
    assert called[0][2] == {}
    assert called[1][0] == h2
    assert called[1][1] == (1, 2, 3)
    assert called[1][2] == {}

if __name__ == '__main__':
    test__EventSource_fire()

# Generated at 2022-06-13 15:53:10.207976
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import unittest

    class _EventSourceTest(unittest.TestCase):
        def test_fire(self):
            event_source = _EventSource()
            event_source.fire()

            self.calls_to_handlerA = 0
            self.calls_to_handlerB = 0
            def handlerA(sender, *args, **kwargs):
                self.calls_to_handlerA += 1
            def handlerB(sender, *args, **kwargs):
                self.calls_to_handlerB += 1

            event_source += handlerA
            event_source.fire()
            self.assertEqual(1, self.calls_to_handlerA)

            event_source += handlerB
            event_source.fire()

# Generated at 2022-06-13 15:53:12.353100
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += lambda *args, **kwargs: None



# Generated at 2022-06-13 15:53:23.556534
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def even(i):
        return not i % 2

    src = _EventSource()
    handlers = []
    src += handlers.append
    src += handlers.append
    src.fire(1, 2, 3)
    assert len(handlers) == 2
    assert handlers[0] == (1, 2, 3)
    assert handlers[1] == (1, 2, 3)


    def raise_exception(*args, **kwargs):
        raise ValueError()

    src = _EventSource()
    src += handlers.append
    src += raise_exception
    src += handlers.append
    try:
        src.fire(1, 2, 3)
        assert False  # should not be reached, exception should have been raised
    except ValueError:
        pass
    assert len(handlers) == 2

# Generated at 2022-06-13 15:53:26.166736
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # Test for ValueError when handler is not callable
    assert_exception(lambda: event_source.__iadd__(1), ValueError, 'must be callable')



# Generated at 2022-06-13 15:53:40.883291
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(x=None, y=None):
        return 1, x, y

    def handler2(x=None, y=None):
        return 2, x, y

    event_source = _EventSource()
    event_source.fire(x=10)
    assert event_source._handlers == set()

    event_source += handler1
    event_source += handler2
    event_source.fire(x=20)
    assert event_source._handlers == {handler1, handler2}

    event_source -= handler1
    event_source.fire(x=30)
    assert event_source._handlers == {handler2}

    event_source -= handler2
    event_source.fire(x=40)
    assert event_source._handlers == set()



# Generated at 2022-06-13 15:53:50.191970
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test1(x, y):
        pass

    def test2(x, y):
        pass

    def test3(x, y):
        raise RuntimeError('Test _EventSource.fire')

    def test4(x, y):
        raise RuntimeError('Test _EventSource.fire')

    s = _EventSource()

    s += test1
    s += test2
    s += test3
    s += test4

    try:
        s.fire(0, 1)
    except RuntimeError:
        pass

    s -= test3
    s -= test4

    try:
        s.fire(0, 1)
    except RuntimeError:
        assert False

    assert True

# Generated at 2022-06-13 15:54:00.105226
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(event, value):
        assert event == 'event1'
        assert value == 'value1'

    def handler2(event, value):
        assert event == 'event1'
        assert value == 'value1'

    # live test of __iadd__ (no asserts)
    src = _EventSource()
    src += handler1
    src -= handler1

    # handler1 should not be called because we removed it
    src += handler1
    src.fire(event='event1', value='value1')

    # handler2 will be called because we only remove handler1
    src -= handler1
    src += handler2
    src.fire(event='event1', value='value1')



# Generated at 2022-06-13 15:54:07.922610
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(a, b):
        raise Exception(a + b)

    def on_exception(a, b):
        raise Exception(a + b)

    event = _EventSource()
    event.on_exception += on_exception

    # raise exception
    caught = False
    try:
        event.fire('hello', 'world')
    except Exception as e:
        caught = True
        assert str(e) == 'helloworld'

    assert caught

    # do not raise exception
    caught = False
    def on_exception(a, b):
        return False

    event._on_exception = on_exception
    try:
        event.fire('hello', 'world')
        caught = True
    except Exception:
        pass

    assert caught



# Generated at 2022-06-13 15:54:11.737317
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def foo():
        return None

    ev = _EventSource()
    ev += foo
    assert ev._handlers
    assert foo in ev._handlers


# Generated at 2022-06-13 15:54:20.323364
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # mock handler used to capture calls
    class _MockEventHandler:
        def __init__(self):
            self._times_called = 0
            self._call_args = None
            self._call_kwargs = None

        def __call__(self, *args, **kwargs):
            self._times_called += 1
            self._call_args = args
            self._call_kwargs = kwargs

    source = _EventSource()

    # Test event handler without exception
    m1 = _MockEventHandler()
    source += m1
    source.fire('a', 1, kwarg='k')
    assert m1._times_called == 1
    assert m1._call_args == ('a', 1)
    assert m1._call_kwargs == {'kwarg': 'k'}

    # Test

# Generated at 2022-06-13 15:54:24.896510
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    func1 = lambda: print('function1')
    func2 = lambda: print('function2')

    event_source += func1
    event_source += func2

    assert func1 in event_source._handlers
    assert func2 in event_source._handlers



# Generated at 2022-06-13 15:54:30.654388
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: None
    es += lambda: None
    assert len(es._handlers) == 2
    try:
        es += 'bad value'
        assert False
    except ValueError:
        pass
    assert len(es._handlers) == 2

# Generated at 2022-06-13 15:54:37.403712
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    handler_counts = [0, 0, 0]

    def handler_0():
        handler_counts[0] += 1

    def handler_1(*args, **kwargs):
        handler_counts[1] += 1
        if kwargs.get('raise_exception', False):
            raise Exception()

    def handler_2(**kwargs):
        handler_counts[2] += 1
        return kwargs.get('return_value', None)

    event_source += handler_0
    event_source += handler_1
    event_source += handler_2

    # fire an event without arguments
    event_source.fire()
    assert handler_counts == [1, 1, 1]

    # fire an event with arguments

# Generated at 2022-06-13 15:54:41.269291
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _on_load = _EventSource()
    _on_load += _EventSource.__init__
    _on_load += str
    _on_load += str
    assert len(_on_load._handlers) == 2


# Generated at 2022-06-13 15:55:03.183998
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self.arg = []
            self.kwarg = []

        def test_handler1(self, *args, **kwargs):
            self.arg.append(args)

        def test_handler2(self, *args, **kwargs):
            self.kwarg.append(kwargs)

        def test_handler3(self, *args, **kwargs):
            raise ValueError('Test')

    # test event source fire
    es = TestEventSource()
    es.fire('test', name='John')
    assert len(es.arg) == 0  # no handler added
    assert len(es.kwarg) == 0  # no handler added

    es += es.test_handler1


# Generated at 2022-06-13 15:55:08.911588
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert len(es._handlers) == 0
    es += lambda: None
    assert len(es._handlers) == 1
    es += lambda: None
    assert len(es._handlers) == 2
    with pytest.raises(ValueError):
        es += 'not callable'
    assert len(es._handlers) == 2


# Generated at 2022-06-13 15:55:16.826769
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class _TestEvent:
        def __init__(self):
            self.called = False

        def handler(self, args, kwargs):
            self.called = True
            self.args = args
            self.kwargs = kwargs

        def assert_called_with(self, *args, **kwargs):
            if not self.called:
                raise AssertionError('handler not called')
            if self.args != args:
                raise AssertionError('handler not called with args: %r' % (args,))
            if self.kwargs != kwargs:
                raise AssertionError('handler not called with kwargs: %r' % (kwargs,))

    x = _TestEvent()
    y = _TestEvent()
    z = _TestEvent()
    e = _EventSource()

   

# Generated at 2022-06-13 15:55:21.630765
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    s = _EventSource()
    assert len(s._handlers) == 0

    s += lambda x: x
    s += lambda x: x
    assert len(s._handlers) == 2

    try:
        s += 123
    except ValueError:
        pass
    else:
        assert False, 'ValueError not raised'

    assert len(s._handlers) == 2


# Generated at 2022-06-13 15:55:25.917965
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MockHandler(object):
        def __init__(self, retval):
            self._retval = retval

        def __call__(self, *args, **kwargs):
            return self._retval

    def test(x, y):
        return (x, y)

    es = _EventSource()
    es += test
    es += MockHandler(1)
    es += MockHandler(2)

    assert es.fire(1, 2) == (1, 2)


# Generated at 2022-06-13 15:55:29.009035
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()
    e += lambda: None
    assert len(e._handlers) == 1


# Generated at 2022-06-13 15:55:37.824544
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestException(Exception):
        pass

    def handler1(arg1, arg2, arg3, **kwargs):
        assert arg1 == 'foo'
        assert arg2 == 'bar'
        assert arg3 == 3
        assert kwargs == {'baz': 42}

    def handler2(arg1, arg2, arg3):
        raise TestException('the handler2 exception')

    x = _EventSource()
    x += handler1
    x += handler2

    try:
        x.fire('foo', 'bar', 3, baz=42)
    except Exception as e:
        assert type(e) is TestException
        assert str(e) == 'the handler2 exception'
        assert e.args == ('the handler2 exception',)
    else:
        assert False, 'exception not raised'

# Generated at 2022-06-13 15:55:40.340915
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    x = _EventSource()
    x += lambda: 1 + 1
    assert x.fire() == None

# Generated at 2022-06-13 15:55:50.757015
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    raised = []

    def handler_one(*args, **kwargs):
        if not args:
            raise ValueError('args is empty')

        if kwargs.get('some_key') == 'some_value':
            # this exception should not be raised
            raise ValueError('calling handler_one with kwargs["some_key"] == "some_value" should not raise')

    def handler_two(first_arg, *args, **kwargs):
        if first_arg != 'first_value':
            raise ValueError('first_arg value is "%s" instead of "first_value"' % first_arg)


# Generated at 2022-06-13 15:56:00.644400
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    # Test case: function _is_module_active, which is called by all
    # handlers, raises a checked exception.
    # The exception is not re-raised by the loop in method fire.
    def event_handler(arg):
        raise ValueError('test')

    event_source = _EventSource()
    event_source += event_handler
    event_source.fire('arg')

    # Test case: function _is_module_active, which is called by all
    # handlers, raises an unchecked exception.
    # The exception is expected to be re-raised by the loop in method fire.
    def event_handler(arg):
        raise RuntimeError('test')

    event_source = _EventSource()
    event_source += event_handler
    try:
        event_source.fire('arg')
    except Exception:
        pass
   

# Generated at 2022-06-13 15:56:38.496911
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        pass

    s = MyEventSource()
    s.fire('one', 'two', 'three')

    def handler_basic(a, b, c):
        assert a == 'one'
        assert b == 'two'
        assert c == 'three'

    def handler_exception(a, b, c):
        raise RuntimeError('oops')

    def handler_on_exception(self, handler, exc, *args, **kwargs):
        assert exc.args[0] == 'oops'
        assert args == ('one', 'two', 'three')
        assert kwargs == {}

        # if we return True, we want the caller to re-raise
        return False


# Generated at 2022-06-13 15:56:41.947088
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    import pytest

    event = _EventSource()
    event += lambda:None
    assert len(event._handlers) == 1

    with pytest.raises(ValueError) as e:
        event += None
    assert to_text(e.value) == 'handler must be callable'


# Generated at 2022-06-13 15:56:48.928632
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyTestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            # we never want the caller to re-raise
            return False

    es = MyTestEventSource()
    assert len(es._handlers) == 0

    def handler1(*args, **kwargs):
        args[0]['handler1'] = 1
    def handler2(*args, **kwargs):
        args[0]['handler2'] = 2
        raise ValueError("handler2 caught exception")
    def handler3(*args, **kwargs):
        args[0]['handler3'] = 3

    # handler2 raises an exception and _on_exception returns False, so the caller will not see this exception
    es += handler1
    es += handler2
    es += handler3

# Generated at 2022-06-13 15:57:00.073115
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self._has_fired = False
            self._has_errored = False

        def handler(self, *args, **kwargs):
            self._has_fired = True
            return True

        def handler_error(self, *args, **kwargs):
            self._has_fired = True
            return False

        def handler_exception(self, *args, **kwargs):
            self._has_fired = True
            self._on_exception(None, None)

        def _on_exception(self, handler, exc, *args, **kwargs):
            self._has_errored = True

# Generated at 2022-06-13 15:57:04.482374
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source.fire()
    def func():
        pass
    source += func
    source += func
    source -= func
    source -= func



# Generated at 2022-06-13 15:57:11.093667
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Unit test for method fire of class _EventSource
    # It fires all the handlers and catches their exceptions
    # (assuming _on_exception returns True for all the exceptions)
    import pytest

    def handler1(*args, **kwargs):
        return

    def handler2(*args, **kwargs):
        raise Exception('Failed')

    source = _EventSource()
    source += handler1
    source += handler2

    with pytest.raises(Exception):
        source.fire()
    return


# Generated at 2022-06-13 15:57:13.084917
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    callback = lambda: 0
    es += callback


# Generated at 2022-06-13 15:57:20.081308
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestHandler:
        def __init__(self, fail_with=None):
            self.fail_with = fail_with
            self.invoked = False

        def __call__(self, *args, **kwargs):
            self.invoked = True
            if self.fail_with is not None:
                raise self.fail_with

    handlers = [TestHandler(), TestHandler()]
    event = _EventSource()

    [event.__iadd__(handler) for handler in handlers]

    event.fire()

    for handler in handlers:
        assert handler.invoked

    for handler in handlers:
        handler.invoked = False

    # fire again, no change
    event.fire()

    for handler in handlers:
        assert handler.invoked

    for handler in handlers:
        handler.invoked = False



# Generated at 2022-06-13 15:57:28.398355
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    _EventSource___iadd__ = _EventSource.__iadd__

    # test invalid input
    source = _EventSource()
    for handler in [None, True, '']:
        try:
            _EventSource___iadd__(source, handler)
        except ValueError:
            pass
        else:
            raise AssertionError('expected ValueError')

    # test valid input
    def handler1():
        pass
    def handler2():
        pass

    _EventSource___iadd__(source, handler1)
    if handler1 not in source._handlers:
        raise AssertionError('handler1 not in the set')

    _EventSource___iadd__(source, handler2)
    if handler2 not in source._handlers:
        raise AssertionError('handler2 not in the set')

# Unit test

# Generated at 2022-06-13 15:57:33.543576
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def do_nothing(*_, **__):
        pass

    test_target = _EventSource()

    test_target += do_nothing
    assert len(test_target._handlers) == 1

    test_target += do_nothing
    assert len(test_target._handlers) == 1



# Generated at 2022-06-13 15:58:41.783201
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event += lambda *args, **kwargs: 1 / 0

    try:
        event.fire()
    except Exception as e:  # noqa
        pass

# Generated at 2022-06-13 15:58:51.255744
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class MockEventSource(_EventSource):
        def __init__(self):
            self.events = []

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.events.append(('exception', handler, exc, args, kwargs))
            return True

    mock_event_source = MockEventSource()
    mock_event_source.exceptions = []

    def handler1(*args, **kwargs):
        mock_event_source.events.append(('handler1', args, kwargs))

    def handler2(*args, **kwargs):
        mock_event_source.events.append(('handler2', args, kwargs))

    def handler3(*args, **kwargs):
        mock_event_source.events.append(('handler3', args, kwargs))

# Generated at 2022-06-13 15:59:00.628990
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    # set up mock handler
    handler_calls = []

    def mock_handler(*args, **kwargs):
        handler_calls.append((args, kwargs))

    # set up event source
    source = _EventSource()

    # verify that adding our mock handler works
    source += mock_handler
    source.fire('test1', 'test2', a=1, b=2)
    assert len(handler_calls) == 1
    assert handler_calls[0] == ((('test1', 'test2'),), {'a': 1, 'b': 2})

    # verify that trying to non-callable handlers raises an error
    for handler in (None, 1, 'string', ['test'], {'test': 1}, object()):
        try:
            source += handler
        except ValueError:
            pass
