

# Generated at 2022-06-13 15:49:08.241892
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    s = _EventSource()

    def handler1(*args, **kwargs):
        pass

    def handler2(x, y, *args, **kwargs):
        pass

    s += handler1
    s += handler2

    s.fire(1, 2, foo='bar')



# Generated at 2022-06-13 15:49:16.267606
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(event):
        handler1.counter += 1
        event.fire(name='foo')

    def handler2(event):
        handler2.counter += 1
        if handler2.counter >= 2:
            raise RuntimeError('expected exception')

    handler1.counter = 0
    handler2.counter = 0

    event = _EventSource()

    event += handler1
    event += handler2

    # Test expected exception propagation
    try:
        event.fire()
        assert False, 'Expected exception'
    except RuntimeError as e:
        assert 'expected exception' == str(e)

    assert handler1.counter == 2
    assert handler2.counter == 2


# Generated at 2022-06-13 15:49:24.336591
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        pass

    source = TestEventSource()

    class Handler:
        def __init__(self, expected_event):
            self._expected_event = expected_event
            self._was_fired = False

        def __call__(self, event):
            assert event == self._expected_event
            self._was_fired = True

        @property
        def was_fired(self):
            return self._was_fired

    events = [
        'apple',
        'banana',
        'cherry',
    ]

    handlers = [Handler(event) for event in events]

    for handler in handlers:
        source += handler

    for event in events:
        source.fire(event)

    for handler in handlers:
        assert handler.was_fired

# Generated at 2022-06-13 15:49:28.054051
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    from ansible_test._loader_common_util import EventSourceTestHandler
    assert_exception = None

    # handler must be callable
    try:
        event_source = _EventSource()
        event_source += 'foo'
    except Exception as ex:
        assert_exception = ex

    assert isinstance(assert_exception, ValueError)

    # ensure handler was added
    event_source = _EventSource()
    event_source += EventSourceTestHandler
    assert len(event_source._handlers) == 1
    assert EventSourceTestHandler in event_source._handlers


# Generated at 2022-06-13 15:49:32.000399
# Unit test for method fire of class _EventSource
def test__EventSource_fire():  # noqa: F811
    event_source = _EventSource()

    events = []
    def on_bar(a, b, c):
        events.append(('bar', a, b, c))

    def on_foo(a, b, c):
        events.append(('foo', a, b, c))

    event_source += on_foo
    event_source += on_bar

    event_source.fire('a', 'b', 'c')

    assert events == [
        ('foo', 'a', 'b', 'c'),
        ('bar', 'a', 'b', 'c'),
    ]


# Generated at 2022-06-13 15:49:37.514477
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    """event_source.fire() should call function for each handler with the expected parameters and return nothing."""

    # create an event source with three handlers
    values = []
    es = _EventSource()
    es += lambda: values.append(1)
    es += lambda: values.append(2)
    es += lambda: values.append(3)

    # ensure the handlers are not called until fire is called
    assert values == []

    # call fire
    es.fire()

    # ensure fire called each handler
    assert values == [1, 2, 3]


# Generated at 2022-06-13 15:49:41.250403
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class A:
        pass

    a = A()

    def _h(a):
        a.x = True

    AnsibleCollectionConfig.on_collection_load += _h
    AnsibleCollectionConfig.on_collection_load.fire(a)
    assert a.x



# Generated at 2022-06-13 15:49:48.402555
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def _handler1():
        return 1

    def _handler2():
        return 2

    def _handler3():
        return 3

    def _handler4():
        return 4

    def _handler5():
        return 5

    # Test adding callables
    es = _EventSource()
    assert es._handlers == set()
    es += _handler1
    assert len(es._handlers) == 1
    es += _handler2
    assert len(es._handlers) == 2

    # Test adding the same handler twice
    es += _handler2
    assert len(es._handlers) == 2

    # Test the __iadd__ is idempotent
    es += _handler1
    assert len(es._handlers) == 2

    # Test adding non-callables

# Generated at 2022-06-13 15:49:56.573644
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    inst = AnsibleCollectionConfig()

    def handler_1():
        pass

    def handler_2():
        pass

    inst.on_collection_load += handler_1
    inst.on_collection_load += handler_2

    # ensure none of the handlers have been called
    handler_1.assert_not_called()
    handler_2.assert_not_called()

    # fire the event and ensure the handlers were called
    inst.on_collection_load.fire()

    handler_1.assert_called_once()
    handler_2.assert_called_once()

    # attempt to remove a handler that was not previously added
    inst.on_collection_load -= handler_2

    # fire the event and ensure the handlers were called
    inst.on_collection_load.fire()

    handler_1.assert_called_twice

# Generated at 2022-06-13 15:49:59.526281
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    assert not es._handlers
    def f():
        pass
    es += f
    assert es._handlers
    assert f in es._handlers


# Generated at 2022-06-13 15:50:12.568427
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    # Success: event_source is an instance of our class
    assert isinstance(event_source, _EventSource)

    # Success
    event_source += lambda: True
    assert isinstance(event_source, _EventSource)

    # Failure: handler is not callable
    try:
        event_source += None
        # should not be reached
        assert False
    except ValueError as ve:
        assert str(ve) == 'handler must be callable'



# Generated at 2022-06-13 15:50:21.557581
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class FooException(Exception):
        pass

    class BarException(Exception):
        pass

    def exec_handler(handler, *args, **kwargs):
        handler(*args, **kwargs)


# Generated at 2022-06-13 15:50:26.959298
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    triggered = []

    def on_load(source):
        triggered.append(source)

    source = _EventSource()
    source += on_load

    source.fire('fake_data')

    assert triggered == ['fake_data']



# Generated at 2022-06-13 15:50:36.750548
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test():
        fire_test.test_value += 1

    def test_raise():
        raise Exception('failure')

    fire_test = _EventSource()
    fire_test.test_value = 0

    fire_test.fire()
    assert fire_test.test_value == 0

    fire_test += test
    fire_test.fire()
    assert fire_test.test_value == 1

    fire_test += test_raise
    try:
        fire_test.fire()
        raise Exception('expected an exception')
    except Exception as ex:
        assert 'expected an exception' not in to_text(ex)
        assert 'failure' in to_text(ex)

    fire_test -= test_raise
    fire_test.fire()
    assert fire_test.test_value == 2

    fire_test

# Generated at 2022-06-13 15:50:46.865158
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    def handle_1(arg1, arg2, arg3):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    def handle_2(arg1, arg2, arg3):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    def handle_3(arg1, arg2, arg3):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    evt += handle_1
    evt += handle_2
    evt += handle_3

    evt.fire(1, 2, 3)

    evt -= handle_2
    evt -= handle_3

    evt.fire(1, 2, 3)

    # test exception handler

# Generated at 2022-06-13 15:50:51.590431
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    # basic function
    def add_one(i):
        return i + 1

    event_source += add_one

    assert len(event_source._handlers) == 1
    assert event_source._handlers == {add_one}

    # add a second event handler
    def add_two(i):
        return i + 2

    event_source += add_two

    assert len(event_source._handlers) == 2
    assert event_source._handlers == {add_one, add_two}

    # attempt to add a non-callable item
    import os
    try:
        event_source += os
        assert False
    except ValueError:
        assert True

    # attempt to add the same handler twice
    event_source += add_one


# Generated at 2022-06-13 15:50:55.100843
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler_1(*args, **kwargs):
        pass

    def handler_2(*args, **kwargs):
        pass

    e = _EventSource()
    e += handler_1
    e += handler_2

    e.fire(1)


# Generated at 2022-06-13 15:51:01.794838
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    valid = 'valid'
    invalid = 'invalid'

    e = _EventSource()
    assert len(e._handlers) == 0

    e += valid
    assert len(e._handlers) == 1
    assert valid in e._handlers

    e += valid
    assert len(e._handlers) == 1
    assert valid in e._handlers

    # exception is raised if not callable
    try:
        e += invalid
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 15:51:04.365318
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event = _EventSource()
    event += lambda a: None
    event.fire('foo')
    # TODO: add more tests



# Generated at 2022-06-13 15:51:08.812807
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler(x=None):
        print("handler got: %s" % x)
    event = _EventSource()
    event += handler

    event.fire("testing")

    event -= handler
    event.fire("testing")

# Generated at 2022-06-13 15:51:16.938210
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def handler1(arg1, arg2, kwarg=''):
        pass

    def handler2(arg1, arg2, kwarg=''):
        pass

    event_source = _EventSource()
    event_source += handler1
    event_source += handler2

    handlers = event_source._handlers
    assert len(handlers) is 2
    assert handler1 in handlers
    assert handler2 in handlers


# Generated at 2022-06-13 15:51:19.734322
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()

    # handler is callable
    handler = lambda: None
    event_source += handler
    assert handler in event_source._handlers

    # handler is not callable
    try:
        event_source += 1
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 15:51:31.916153
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            self.fire_args = None
            self.fire_kwargs = None
            super(TestEventSource, self).__init__()

        def test_fire(self, *args, **kwargs):
            self.fire_args = args
            self.fire_kwargs = kwargs

    # for the unit test, we're going to allow exceptions to be swallowed
    es = TestEventSource()
    es._on_exception = lambda handler, exc, *args, **kwargs: False

    es += es.test_fire
    es.fire(1, one=1)
    assert es.fire_args == (1,)
    assert es.fire_kwargs == dict(one=1)
    es.fire_args = None
    es.fire_

# Generated at 2022-06-13 15:51:43.399429
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class MyEventSource(_EventSource):
        handler_called = False
        handler_exception = None

        @staticmethod
        def handler():
            MyEventSource.handler_called = True

        @_EventSource._on_exception
        def on_exception(self, handler, exc, *args, **kwargs):
            MyEventSource.handler_exception = exc


# Generated at 2022-06-13 15:51:51.339067
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    evt = _EventSource()

    def handler_true(args, kwargs):
        return True

    def handler_false(args, kwargs):
        return False

    def handler_None(args, kwargs):
        return

    def handler_exception(args, kwargs):
        raise Exception()

    evt += handler_true
    evt += handler_false
    evt += handler_None
    evt += handler_exception

    # all handlers are called
    evt.fire()

    evt -= handler_false
    evt -= handler_None

    # handlers_false and handlers_None are not called
    evt.fire()

# Generated at 2022-06-13 15:52:04.156208
# Unit test for method fire of class _EventSource
def test__EventSource_fire():  # pylint: disable=missing-docstring
    def handler_a(value):
        raise Exception('handler_a')

    def handler_b(value):
        assert value == 'hello'

    def handler_c(value):
        raise Exception('handler_c')

    def handler_d(value):
        assert value == 'hello'

    class _Config(_EventSource):
        def _on_exception(self, handler, exc, value):
            if handler == handler_a:
                assert isinstance(exc, Exception)
                assert exc.args == ('handler_a', )
            if handler == handler_b:
                assert isinstance(exc, Exception)
                assert exc.args == ('handler_b', )
            if handler == handler_c:
                assert isinstance(exc, Exception)

# Generated at 2022-06-13 15:52:11.843694
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    def handler1(*_):
        raise AssertionError('Unexpected call to handler1')

    def handler2(*_):
        raise AssertionError('Unexpected call to handler2')

    def handler3(*_):
        raise AssertionError('Unexpected call to handler3')

    event_source = _EventSource()

    event_source += handler1
    event_source += handler2

    # handler3 is not added
    with pytest.raises(AssertionError) as e:
        event_source.fire()
    assert str(e.value) == 'Unexpected call to handler1'

    event_source -= handler1
    event_source += handler3

    with pytest.raises(AssertionError) as e:
        event_source.fire()

# Generated at 2022-06-13 15:52:19.417872
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    '''
    Validate that _EventSource.__iadd__ correctly registers callables as event handlers
    '''

    import math

    s = _EventSource()

    assert not s._handlers

    # register a lambda
    s += lambda x: math.log(x)
    assert 1 == len(s._handlers)

    # register another lambda
    s += lambda x: math.log10(x)
    assert 2 == len(s._handlers)

    # register the same lambda again
    s += lambda x: math.log10(x)
    assert 2 == len(s._handlers)

    # register a bound method of a class instance
    class Tester:
        def __init__(self):
            self.invoked = False
        def handler(self, x):
            self.invoked = True
    tester

# Generated at 2022-06-13 15:52:29.905984
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    from unittest import TestCase
    from unittest.mock import Mock

    class FireTest(TestCase):
        def test_fire(self):
            # Test on_exception
            def mock_on_exception(handler, exception, *args, **kwargs):
                raise exception

            event_source = _EventSource()
            event_source._on_exception = mock_on_exception

            handler = Mock()
            event_source += handler

            with self.assertRaises(ValueError):
                event_source.fire()

            # Test handler
            event_source2 = _EventSource()

            handler2 = Mock()
            event_source2 += handler2

            exception = ValueError()
            with self.assertRaises(ValueError):
                event_source2.fire(exception=exception)

            handler

# Generated at 2022-06-13 15:52:37.703893
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def mock_callable():
        pass

    event_source = _EventSource()
    test_result = event_source.__iadd__(mock_callable)
    assert test_result == event_source
    assert event_source._handlers == {mock_callable}

    test_result = event_source.__iadd__(event_source)
    assert test_result == event_source
    assert event_source._handlers == {mock_callable}



# Generated at 2022-06-13 15:52:42.796008
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es += lambda: print('this is a test')

    assert callable(es)


# Generated at 2022-06-13 15:52:52.197155
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):  # pylint: disable=super-init-not-called,super-on-old-class
            return super(_EventSource, self)._on_exception(handler, exc, *args, **kwargs)

    es = TestEventSource()

    def handler1(*args, **kwargs):  # pylint: disable=unused-argument
        return 0

    def handler2(*args, **kwargs):  # pylint: disable=unused-argument
        return 1

    def handler3(*args, **kwargs):  # pylint: disable=unused-argument
        raise ValueError('fake_exception')

    es += handler1
    es += handler2
    es += handler3



# Generated at 2022-06-13 15:52:54.141749
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    event_source += lambda: 5



# Generated at 2022-06-13 15:53:01.854407
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    e = _EventSource()

    def handlerA(x):
        raise ValueError(x)

    def handlerB(x):
        raise RuntimeError(x)

    def handlerC(x):
        raise NotImplementedError(x)

    e += handlerA
    e += handlerB
    e += handlerC

    exc = None
    try:
        e.fire(1)
    except ValueError as ex:
        exc = ex
    assert exc and str(exc) == '1'

    e -= handlerA

    exc = None
    try:
        e.fire(2)
    except RuntimeError as ex:
        exc = ex
    assert exc and str(exc) == '2'

# Generated at 2022-06-13 15:53:08.181013
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    source = _EventSource()
    last_message = None
    called_once = False

    def handler1(message):
        nonlocal last_message
        last_message = message

    def handler2(message):
        nonlocal called_once
        called_once = True

    source += handler1
    source += handler2
    source.fire('hello')

    assert last_message == 'hello'
    assert called_once

    source -= handler2
    source.fire('again')

    assert last_message == 'again'
    # handler2 should not have fired because we removed it
    assert not called_once


# Generated at 2022-06-13 15:53:20.897521
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    event_source = _EventSource()

    # Test with an empty set
    event_source.fire()

    # Test with callables with different signatures
    event_source += lambda a, b: None
    event_source += lambda a, b, c: None
    event_source += lambda d, e=None, f=None: None
    event_source += lambda g=None, x=None: None
    event_source.fire(1, 2, c=3, e=4)

    # Test with exceptions
    def f1(*args, **kwargs):
        raise ValueError('expected exception')
    def f2(*args, **kwargs):
        raise TypeError('unexpected exception')

    event_source = _EventSource()
    event_source += f1
    event_source += f2

# Generated at 2022-06-13 15:53:31.288278
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    events = _EventSource()
    results = []

    def event_1a(*args, **kwargs):
        results.append((1, args, kwargs))

    def event_1b(*args, **kwargs):
        results.append((1, args, kwargs))

    def event_2(*args, **kwargs):
        results.append((2, args, kwargs))

    events += event_1a
    events += event_1b
    events += event_2

    try:
        events += lambda: None
        assert False, 'expected exception'
    except ValueError:
        pass

    events.fire(11, 12, a=13, b=14)

# Generated at 2022-06-13 15:53:37.802059
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''Test function for method _EventSource.fire

    :return: None
    :rtype: None
    '''

    class _CallCounter:
        def __init__(self):
            self.count = 0

        def __call__(self):
            self.count += 1

    event = _EventSource()
    cc = _CallCounter()

    event += cc
    assert cc.count == 0

    event.fire()
    assert cc.count == 1

    event -= cc
    event += cc
    event.fire()
    assert cc.count == 2

    event.fire()
    assert cc.count == 3

# Generated at 2022-06-13 15:53:39.425086
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    assert not event_source.fire()

# Generated at 2022-06-13 15:53:41.130768
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    s = _EventSource()
    s += 'test'


# Generated at 2022-06-13 15:53:53.595947
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestEventSource(_EventSource):
        def __init__(self):
            super(TestEventSource, self).__init__()
            self.fired = False

        def handler(self, *args, **kwargs):
            self.fired = True

    s = TestEventSource()
    s += s.handler

    s.fire()
    assert s.fired



# Generated at 2022-06-13 15:53:58.931909
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(arg):
        assert arg == 1

    def handler2(arg):
        assert arg == 2

    event = _EventSource()
    event += handler1
    event += handler2

    event.fire(1)
    event.fire(2)



# unit test for method fire of class _EventSource

# Generated at 2022-06-13 15:54:08.129444
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()

    class Test:
        def __init__(self, test_id, success):
            self.test_id = test_id
            self.success = success

        def __call__(self, *args, **kwargs):
            assert len(args) == 1
            assert args[0] == self.test_id
            assert len(kwargs) == 1
            assert kwargs['first'] == 'one'
            if not self.success:
                raise ValueError('{} failed'.format(self.test_id))
            return 'call result'

    event_source += Test('test1', True)
    event_source += Test('test2', True)

    assert len(event_source._handlers) == 2


# Generated at 2022-06-13 15:54:18.832360
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    es = _EventSource()
    es.fire()
    def _hand(x):
        raise
    es += _hand
    es.fire()
    es -= _hand
    es.fire()
    es += lambda: 1
    es.fire()

# This is the version in the controller
from ansible.utils.collection_loader.target.controller_collection_loader import TEST_COLLECTION_PATH, TEST_COLLECTIONS_PATH
from ansible.utils.collection_loader.target.controller_collection_loader import ANSIBLE_COLLECTIONS_PATHS, ANSIBLE_COLLECTIONS_PATH
from ansible.utils.collection_loader.target.controller_collection_loader import AnsibleCollectionFinder
from ansible.utils.collection_loader.target.controller_collection_loader import CollectionLoader

# Generated at 2022-06-13 15:54:24.052017
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():

    def foo(a, b, c, d):
        pass

    def bar(a, b, c, d):
        pass

    def baz(a, b, c, d):
        pass

    es = _EventSource()
    es += foo
    es += bar
    es += baz

    assert len(es._handlers) == 3



# Generated at 2022-06-13 15:54:32.845820
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    t = _EventSource()
    # Add one
    flag = [False]
    def callback():
        flag[0] = True
    t += callback
    t.fire()
    assert flag[0]

    # Add two
    flag = [False, False]
    def callback1():
        flag[0] = True
    def callback2():
        flag[1] = True
    t += callback1
    t += callback2
    t.fire()
    assert flag[0] and flag[1]

    # Add then remove one
    flag = [True, False]
    t -= callback2
    t.fire()
    assert flag[0] and not flag[1]

    # Add then remove one when not present
    flag = [True, False]
    t -= callback1
    t -= callback2
    t.fire

# Generated at 2022-06-13 15:54:35.534457
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_func(x):
        raise Exception("Test exception")

    test_event = _EventSource()
    test_event += test_func
    try:
        test_event.fire()
    except:
        pass

# Generated at 2022-06-13 15:54:42.352917
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    event_source = _EventSource()
    def handler():
        return "handler"
    event_source += handler
    assert len(event_source._handlers) == 1
    assert "handler" in event_source._handlers
    event_source += handler
    assert len(event_source._handlers) == 1
    event_source += "handler"
    assert len(event_source._handlers) == 2


# Generated at 2022-06-13 15:54:50.273208
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    test_args = [1, 2]
    test_kwargs = {'arg3': 3, 'arg4': 4}

    def handler1(*args, **kwargs):
        assert args == test_args
        assert kwargs == test_kwargs

    def handler2(*args, **kwargs):
        assert args == test_args
        assert kwargs == test_kwargs

    # initialize event source
    e = _EventSource()

    # test zero handlers
    e.fire(*test_args, **test_kwargs)

    # test one handler
    e += handler1
    e.fire(*test_args, **test_kwargs)

    # test two handlers
    e += handler2
    e.fire(*test_args, **test_kwargs)

    # test remove one handler
    e -= handler1
   

# Generated at 2022-06-13 15:54:52.705225
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    def callback():
        pass

    x = _EventSource()
    x += callback
    assert callback in x._handlers



# Generated at 2022-06-13 15:55:11.615608
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()
    source += lambda x: None
    try:
        source += 1
        assert False, 'expected ValueError'
    except ValueError:
        pass

# Generated at 2022-06-13 15:55:22.171990
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(arg):
        pass

    def handler2(arg):
        raise RuntimeError('Something went wrong')

    def handler3(arg):
        raise NotImplementedError('Feature not implemented')

    def handler4(arg):
        pass

    def handler5(arg):
        raise NotImplementedError('Feature not implemented')

    def on_exception(handler, ex, arg):
        if isinstance(ex, NotImplementedError):
            return False
        return True

    event = _EventSource()
    event._on_exception = on_exception

    event += handler1
    event += handler2
    event += handler3
    event += handler4
    event += handler5

    event.fire('foo')

    event -= handler2

    run_exception = None

# Generated at 2022-06-13 15:55:34.664688
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    # verify that an exception raised by a handler does not prevent firing of subsequent handlers
    def test_handler_one(evt, *args, **kwargs):
        if evt == 'evt1':
            raise RuntimeError()
    def test_handler_two(evt, *args, **kwargs):
        if evt == 'evt3':
            raise RuntimeError()

    events = _EventSource()
    events += test_handler_one
    events += test_handler_two

    fired = 0
    try:
        fired += 1
        events.fire('evt1')
    except:
        pass

    fired += 1
    events.fire('evt2')

    try:
        fired += 1
        events.fire('evt3')
    except:
        pass

    fired += 1

# Generated at 2022-06-13 15:55:38.492473
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_receiver(x, y, z):
        pass

    es = _EventSource()
    es += test_receiver
    es.fire('x', 'y', z=1)


# Generated at 2022-06-13 15:55:49.681762
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    # Test case data
    test_handler = '<test_handler>'
    test_args = ('<test_args>',)
    test_kwargs = {'a': '<test_kwargs_a>'}
    test_expected_result = ['<test_expected_result>']

    # Test variables
    calls_to_handler = []
    event_source = _EventSource()

    # Test code
    def handler(*args, **kwargs):
        calls_to_handler.append((args, kwargs))
        return test_expected_result

    event_source += handler
    result = event_source.fire(*test_args, **test_kwargs)
    assert result == test_expected_result
    assert calls_to_handler == [(test_args, test_kwargs)]


# Generated at 2022-06-13 15:55:53.878046
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    '''Unit test for method fire of class _EventSource'''
    e = _EventSource()
    e.fire()  # this should not fail


# Generated at 2022-06-13 15:56:03.685464
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    def assertFired(fire):
        assert fired

    def sum(a, b):
        return a + b

    es = _EventSource()

    fired = False
    es += assertFired
    es.fire()
    fired = True
    es.fire()

    fired = False
    es -= assertFired
    es.fire()
    fired = True
    es.fire()

    fired = False
    es += sum
    es.fire(1, 2)

    fired = False
    es += sum
    es.fire(2, 3)

    fired = False

    def on_exception(handler, ex, *args, **kwargs):
        nonlocal fired
        fired = True
        assert ex == 'abc'
        return False

    es = _EventSource()
    es._on_exception = on_ex

# Generated at 2022-06-13 15:56:07.167734
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    class DummyHandler:
        def handler(self, *args, **kwargs):
            pass

    handler = DummyHandler()

    event_source = _EventSource()
    event_source += handler.handler  # the class method should be a callable
    assert handler.handler in event_source._handlers



# Generated at 2022-06-13 15:56:13.505967
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    import pytest

    # Define an event handler that returns True
    def handler1():
        return True

    # Define an event handler that returns False
    def handler2():
        return False

    # Define an exception handler that returns True
    def exception1(handler, exception):
        return True

    # Define an exception handler that returns False
    def exception2(handler, exception):
        return False

    # Define an exception handler that raises an exception
    def exception3(handler, exception):
        raise

    # This configuration of event source should return None
    event_source1 = _EventSource()
    assert event_source1.fire() is None

    # This configuration of event source should return True
    event_source2 = _EventSource()
    event_source2 += handler1
    assert event_source2.fire() is True



# Generated at 2022-06-13 15:56:22.306376
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TraceEventSource(_EventSource):
        def __init__(self):
            super(TraceEventSource, self).__init__()
            self.was_faulted = False

        def _on_exception(self, handler, exc, *args, **kwargs):
            self.was_faulted = True
            return False

    trace = TraceEventSource()

    def handler(*args, **kwargs):
        raise NotImplementedError()

    trace += handler
    trace.fire()
    assert trace.was_faulted


# Make sure the unit test is valid
test__EventSource_fire()

# Generated at 2022-06-13 15:56:56.950641
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    source = _EventSource()

    def handler():
        pass

    source += handler
    assert source._handlers == {handler}


# Generated at 2022-06-13 15:57:03.122097
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class Event:
        def __init__(self):
            self.count = 0
            self.errors = []

        def event(self, *args, **kwargs):
            # We intentionally raise an exception here to
            # simulate an error handler.
            self.count += 1
            raise RuntimeError('an error')

    event = Event()
    ansible_collection_config = AnsibleCollectionConfig()
    ansible_collection_config.on_collection_load += event.event
    ansible_collection_config.on_collection_load += event.event
    ansible_collection_config.fire('any-arg', 'another-arg')
    assert event.count == 2

# Generated at 2022-06-13 15:57:13.494777
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def handler1(a, b):
        assert a == 'a'
        assert b == 'b'
        return 'handler1'

    def handler2(a, b):
        assert a == 'a'
        assert b == 'b'
        return 'handler2'

    def handler3(a, b):
        assert a == 'a'
        assert b == 'b'
        return 'handler3'

    source = _EventSource()
    source += handler1
    source += handler2

    source.fire('a', 'b')
    source.fire('a', 'b')

    source -= handler1
    source.fire('a', 'b')

    source += handler1
    source.fire('a', 'b')

    source -= handler1
    source -= handler2
    source.fire('a', 'b')

   

# Generated at 2022-06-13 15:57:23.422556
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def foo(a, b, c, d):
        print("foo(%s, %s, %s, %d)" % (a, b, c, d))

    def bar(a, b, c):
        print("bar(%s, %s, %s)" % (a, b, c))

    testee = _EventSource()

    testee.fire("foo", "bar", "baz", d=42)

    testee += foo
    testee.fire("foo", "bar", "baz", d=42)

    testee -= foo
    testee.fire("foo", "bar", "baz", d=42)

    testee += bar
    testee.fire("foo", "bar", "baz", d=42)


# Generated at 2022-06-13 15:57:28.259488
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def test_handler_1():
        print('test handler 1 called')

    def test_handler_2(*args, **kwargs):
        print('test handler 2 called with args={}, kwargs={}'.format(repr(args), repr(kwargs)))

    event_source = _EventSource()
    event_source += test_handler_1
    event_source += test_handler_2

    event_source.fire('test value', keyword_arg='test keyword_arg')

# Generated at 2022-06-13 15:57:35.099311
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():
    e = _EventSource()

    def handler1(x): pass
    def handler2(x): pass

    assert len(e._handlers) == 0
    e += handler1
    assert len(e._handlers) == 1
    e += handler1
    assert len(e._handlers) == 1
    e += handler2
    assert len(e._handlers) == 2
    e += handler2
    assert len(e._handlers) == 2


# Generated at 2022-06-13 15:57:45.290745
# Unit test for method fire of class _EventSource
def test__EventSource_fire():

    class TestClass1:

        def __init__(self):
            self.value = 0.0

        def handler(self):
            self.value = 1.0

        def raise_error(self):
            raise ValueError("ValueError")

    class TestClass2:

        def __init__(self):
            self.value = 0.0

        def handler(self):
            self.value = 2.0

    def _on_exception(handler, exc, *args, **kwargs):
        if isinstance(exc, ValueError):
            return False

        return True

    test_obj1 = TestClass1()
    test_obj2 = TestClass2()
    event_source = _EventSource()
    event_source._on_exception = _on_exception
    event_source += test_obj1.handler


# Generated at 2022-06-13 15:57:50.367962
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    def _my_handler(*args, **keys):
        global _my_handler_counter
        _my_handler_counter += 1

    event_source = _EventSource()
    event_source += _my_handler
    event_source += _my_handler

    global _my_handler_counter
    _my_handler_counter = 0

    event_source.fire()
    assert _my_handler_counter == 2

# Generated at 2022-06-13 15:57:55.969404
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    event_source = _EventSource()
    class Foo:
        def method(self, val):
            return val
    foo = Foo()
    event_source += foo.method
    assert event_source.fire(val='foo') is None

    class Bar:
        def method(self, val):
            raise TypeError('bar')
    bar = Bar()
    event_source += bar.method
    try:
        event_source.fire(val='bar')
        assert False
    except TypeError:
        pass

# Generated at 2022-06-13 15:58:03.061836
# Unit test for method fire of class _EventSource
def test__EventSource_fire():
    class TestClass:
        def __init__(self):
            self.obj = _EventSource()
            self.exception1 = None
            self.exception2 = None

        def handler1(self, a):
            print('a = ' + a)
            assert a == 'a'

        def handler2(self, a):
            print('a = ' + a)
            assert a == 'a'
            raise RuntimeError('exception2')

        def _on_exception(self, handler, ex, *args, **kwargs):
            print('Caught exception: ' + str(ex))

            if handler is self.handler1:
                self.exception1 = ex
            elif handler is self.handler2:
                self.exception2 = ex
            else:
                assert False

            return False
