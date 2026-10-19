

# Generated at 2024-03-18 04:32:57.272636
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:04.454550
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler that will record calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert that the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test that an exception in a handler is propagated
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Intentional exception for testing")

    # Add the handler that raises an exception
    event_source += handler_with_exception

    # Assert that firing the event now raises an exception


# Generated at 2024-03-18 04:33:10.712717
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(arg1, arg2=None):
        events_handled.append((arg1, arg2))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with arguments
    event_source.fire('event1', arg2='data1')

    # Check if the event was handled correctly
    assert events_handled == [('event1', 'data1')], "Event was not handled as expected"

    # Fire another event with different arguments
    event_source.fire('event2')

    # Check if the second event was also handled correctly
    assert events_handled == [('event1', 'data1'), ('event2', None)], "Second event was not handled as expected"

    # Define an exception-ra

# Generated at 2024-03-18 04:33:16.821500
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:23.649134
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:29.437333
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:36.522350
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:41.833365
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:47.099035
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:33:53.793318
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:07.920831
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Remove the handler and fire another event
    event_source -= handler

# Generated at 2024-03-18 04:34:16.593035
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:21.603001
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:28.053537
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler to track calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test exception handling
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Exception from handler")

    # Replace the _on_exception method to return False, indicating the exception should not be re-raised
    event_source._on_exception = MagicMock(return_value=False)

    # Add the handler that raises

# Generated at 2024-03-18 04:34:33.544580
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:38.646510
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:45.996018
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Define an exception-raising handler
    def bad_handler(*args, **kwargs):
        raise ValueError

# Generated at 2024-03-18 04:34:51.715249
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:34:56.940878
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:02.881724
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:17.606475
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:25.388580
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:32.589326
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:38.298252
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:43.208479
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

    # Define a simple callable handler

# Generated at 2024-03-18 04:35:47.963512
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:35:55.068015
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:36:04.336821
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:36:09.978272
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Test exception handling within the event
    def bad_handler(*args, **kwargs):
        raise ValueError

# Generated at 2024-03-18 04:36:17.199909
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler that will record calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert that the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test that an exception in a handler is propagated
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Intentional exception for testing")

    # Add the handler that raises an exception
    event_source += handler_with_exception

    # Assert that firing the event now raises an exception


# Generated at 2024-03-18 04:36:40.159181
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:36:46.442101
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler that will record calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert that the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test that an exception in a handler is propagated
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Intentional exception for testing")

    # Add the exception-raising handler
    event_source += handler_with_exception

    # Assert that firing the event now raises an exception
   

# Generated at 2024-03-18 04:36:54.867743
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:02.403333
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:07.588643
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:13.805451
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:19.423726
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:23.256781
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:30.437103
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(arg1, arg2):
        events_handled.append((arg1, arg2))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with arguments
    event_source.fire('event1', 'data1')

    # Check if the event was handled correctly
    assert events_handled == [('event1', 'data1')], "Event was not handled as expected"

    # Define an exception-raising handler
    def bad_handler(arg1, arg2):
        raise ValueError("Bad handler")

    # Add the bad handler to the event source
    event_source += bad_handler

    # Fire an event and expect an exception

# Generated at 2024-03-18 04:37:35.805754
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:37:59.921979
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler that will record calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test exception handling
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Test exception")

    # Replace the _on_exception method to return False, indicating the exception should not be re-raised
    event_source._on_exception = MagicMock(return_value=False)

    # Add the exception-raising

# Generated at 2024-03-18 04:38:05.803149
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:12.512134
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:21.064200
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:28.952807
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:35.495390
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:43.742535
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:48.741398
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:54.125200
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:38:59.022172
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Remove the handler and fire another event
    event_source -= handler

# Generated at 2024-03-18 04:39:21.871097
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:39:25.674142
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:39:32.752397
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:39:40.232061
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Remove the handler and fire another event
    event_source -= handler

# Generated at 2024-03-18 04:39:45.696838
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler that will record calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert that the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Create a handler that raises an exception
    def exception_raising_handler(*args, **kwargs):
        raise ValueError("Intentional exception for testing")

    # Add the exception-raising handler to the event source
    event_source += exception_raising_handler

    # Assert that firing the event now raises

# Generated at 2024-03-18 04:39:50.551940
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:39:55.520966
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

    # Define a simple callable handler

# Generated at 2024-03-18 04:39:58.999284
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:40:02.341601
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:40:09.361729
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:40:48.127612
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Create a mock handler to track calls
    mock_handler = MagicMock()

    # Add the mock handler to the event source
    event_source += mock_handler

    # Fire the event with some test arguments
    test_args = (1, 2, 3)
    test_kwargs = {'a': 'A', 'b': 'B'}
    event_source.fire(*test_args, **test_kwargs)

    # Assert the mock handler was called with the correct arguments
    mock_handler.assert_called_once_with(*test_args, **test_kwargs)

    # Test exception handling
    def handler_with_exception(*args, **kwargs):
        raise ValueError("Test exception")

    # Replace the mock handler with one that raises an exception
    event_source -= mock_handler
    event_source += handler_with_exception

    # Override the _on_exception method to return False, preventing re

# Generated at 2024-03-18 04:40:53.543816
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:40:58.471711
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:10.316977
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:15.959673
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:19.857755
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:24.833334
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:30.413094
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:35.395918
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:41:39.099505
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:42:18.917148
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the handler to the event source
    event_source += handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly."

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly."

    # Remove the handler and fire another event
    event_source -= handler

# Generated at 2024-03-18 04:42:25.311356
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:42:31.208654
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:42:36.638832
# Unit test for method __iadd__ of class _EventSource
def test__EventSource___iadd__():    event_source = _EventSource()

# Generated at 2024-03-18 04:42:43.385620
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    event_source = _EventSource()

# Generated at 2024-03-18 04:42:48.720249
# Unit test for method fire of class _EventSource
def test__EventSource_fire():    # Create an instance of _EventSource
    event_source = _EventSource()

    # Define a simple event handler that appends received arguments to a list
    events_handled = []

    def simple_handler(*args, **kwargs):
        events_handled.append((args, kwargs))

    # Add the simple handler to the event source
    event_source += simple_handler

    # Fire an event with no arguments
    event_source.fire()
    assert events_handled == [((), {})], "Event without arguments should be handled correctly"

    # Fire an event with arguments and keyword arguments
    event_source.fire(1, 2, three=3, four=4)
    assert events_handled == [((), {}), ((1, 2), {'three': 3, 'four': 4})], "Event with arguments should be handled correctly"

    # Define an event handler that raises an exception