

# Generated at 2024-03-18 08:27:44.817087
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    connector.secondary_addrs = [(socket.AF_INET6, ('::1', 80))]
    connector.future = Future()
    connector.io_loop = IOLoop.current()
    connector.try_connect = MagicMock()

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(iter(connector.secondary_addrs))
    assert connector.timeout is None


# Generated at 2024-03-18 08:27:53.374615
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))

# Generated at 2024-03-18 08:28:11.756234
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    # Mocking the necessary components for the test
    mock_stream = unittest.mock.Mock(spec=IOStream)
    mock_future = unittest.mock.Mock(spec=Future)
    mock_addr = ('127.0.0.1', 12345)
    mock_af = socket.AF_INET
    mock_addrs = iter([(mock_af, mock_addr)])
    mock_io_loop = unittest.mock.Mock(spec=IOLoop)
    mock_io_loop.time.return_value = 0

    # Setting up the _Connector instance
    connector = _Connector(addrinfo=[(mock_af, mock_addr)], connect=lambda af, addr: (mock_stream, mock_future))
    connector.io_loop = mock_io_loop

    # Test case: successful connection
    mock_future.result.return_value = mock_stream
    connector.on_connect_done(mock_addrs, mock_af, mock_addr, mock_future)
    assert connector.future.done()

# Generated at 2024-03-18 08:28:19.251762
# Unit test for method start of class _Connector
def test__Connector_start():    # Arrange
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    connect_called_with = []

    async def fake_connect(af, addr):
        connect_called_with.append((af, addr))
        future = Future()
        future.set_result(IOStream(socket.socket(af)))
        return IOStream(socket.socket(af)), future

    connector = _Connector(addrinfo, fake_connect)

    # Act
    result_future = connector.start()

    # Assert
    assert not result_future.done(), "Future should not be completed immediately"
    assert len(connect_called_with) == 1, "Should have started one connection attempt"
    assert connect_called_with[0][0] == addrinfo[0][0], "Should start with the first address family"

# Generated at 2024-03-18 08:28:23.386912
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))], connect=lambda af, addr: (None, Future()))
    connector.try_connect = MagicMock()
    connector.secondary_addrs = iter([(socket.AF_INET6, ('::1', 80))])

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(connector.secondary_addrs)

# Generated at 2024-03-18 08:28:30.130107
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    timeout = 5.0
    expected_timeout = IOLoop.current().time() + timeout

    # Act
    connector.set_connect_timeout(timeout)
    actual_timeout = connector.connect_timeout.callback_time if connector.connect_timeout else None

    # Assert
    assert actual_timeout is not None, "Connect timeout was not set"
    assert abs(actual_timeout - expected_timeout) < 0.1, "Connect timeout was not set correctly"

# Generated at 2024-03-18 08:28:37.546678
# Unit test for method split of class _Connector
def test__Connector_split():    # Arrange
    addrinfo_ipv4 = (socket.AF_INET, ('127.0.0.1', 80))
    addrinfo_ipv6 = (socket.AF_INET6, ('::1', 80))
    addrinfo_mixed = [addrinfo_ipv4, addrinfo_ipv6]

    # Act
    primary, secondary = _Connector.split(addrinfo_mixed)

    # Assert
    assert primary == [addrinfo_ipv4], "Expected primary list to contain only IPv4 addresses"
    assert secondary == [addrinfo_ipv6], "Expected secondary list to contain only IPv6 addresses"

# Generated at 2024-03-18 08:28:43.939880
# Unit test for method start of class _Connector
def test__Connector_start():    # Arrange
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    connect = lambda af, addr: (IOStream(socket.socket(af)), Future())
    connector = _Connector(addrinfo, connect)

    # Act
    future = connector.start()

    # Assert
    assert isinstance(future, Future), "The start method must return a Future object."
    assert not future.done(), "The future should not be completed immediately."
    assert len(connector.streams) == 1, "One stream should be initiated immediately."


# Generated at 2024-03-18 08:28:56.270250
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():    # Setup the environment and objects needed for the test
    io_loop = IOLoop.current()
    connect_future = Future()
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = lambda af, addr: (IOStream(socket.socket(af)), connect_future)
    connector = _Connector(addrinfo, connect)

    # Start the connection process with a very short timeout to trigger the timeout handler
    connector.start(connect_timeout=0.001)

    # Allow IOLoop to run for a short time to process the timeout
    io_loop.call_later(0.002, io_loop.stop)
    io_loop.start()

    # Check that the future was set with a TimeoutError
    assert connector.future.done(), "Future should be done"
    assert isinstance(connector.future.exception(), TimeoutError), "Future should have a TimeoutError"

    # Check that the streams were closed
    assert not connector.streams

# Generated at 2024-03-18 08:29:02.616686
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    # Setup the environment and mocks
    io_loop = IOLoop.current()
    connect = MagicMock()
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    connector = _Connector(addrinfo, connect)
    connector.future = Future()
    connector.io_loop = io_loop
    stream = MagicMock(spec=IOStream)
    future = Future()
    future.set_result(stream)
    addrs = iter(addrinfo)

    # Test a successful connection
    connector.on_connect_done(addrs, socket.AF_INET, ('127.0.0.1', 80), future)
    assert not connector.future.done()
    assert stream not in connector.streams

    # Test a failed connection
    connector.remaining = 1
    failed_future = Future()
    failed_future.set_exception(IOError("connection failed"))

# Generated at 2024-03-18 08:29:43.438611
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    timeout = 0.1
    original_time = connector.io_loop.time()

    # Act
    connector.set_timeout(timeout)
    set_timeout_time = connector.io_loop.time()

    # Assert
    assert connector.timeout is not None, "Timeout should be set"
    assert set_timeout_time - original_time >= timeout, "Timeout should be set to at least the specified timeout duration"

# Generated at 2024-03-18 08:29:51.674266
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    connector.future = Future()
    connector.streams = {IOStream(socket.socket())}
    connector.set_connect_timeout(0.1)

    # Act
    connector.on_connect_timeout()

    # Assert
    assert connector.future.done()
    assert connector.future.exception() is not None
    assert isinstance(connector.future.exception(), TimeoutError)
    assert all(stream.closed() for stream in connector.streams)

# Generated at 2024-03-18 08:30:00.320010
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():    # Setup the connector with dummy address info
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connector = _Connector(addrinfo, lambda af, addr: (None, Future()))

    # Mock the IOLoop's add_timeout method
    mock_io_loop = unittest.mock.Mock(spec=IOLoop)
    connector.io_loop = mock_io_loop

    # Set a connect timeout and ensure the IOLoop's add_timeout was called
    timeout = 5.0
    connector.set_connect_timeout(timeout)
    mock_io_loop.add_timeout.assert_called_once_with(timeout, connector.on_connect_timeout)

    # Ensure that the connect_timeout attribute is set
    assert isinstance(connector.connect_timeout, object)

    # Trigger the timeout and ensure the future is set with a TimeoutError
    connector.on_connect_timeout()
    assert connector.future.done()
    with pytest.raises(TimeoutError):
        connector.future.result()

    # Ensure that

# Generated at 2024-03-18 08:30:05.349014
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    connector.secondary_addrs = [(socket.AF_INET6, ('::1', 80))]
    connector.future = Future()
    connector.io_loop = IOLoop.current()
    connector.try_connect = MagicMock()

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(iter(connector.secondary_addrs))
    assert connector.timeout is None


# Generated at 2024-03-18 08:30:14.658303
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    from unittest.mock import Mock, patch

# Generated at 2024-03-18 08:30:19.320766
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    connector.try_connect = mock.Mock()
    connector.future = Future()

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(iter(connector.secondary_addrs))
    assert connector.timeout is None


# Generated at 2024-03-18 08:30:33.222245
# Unit test for method split of class _Connector
def test__Connector_split():    # Prepare the addrinfo list with mixed address families
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET6, ('fe80::1', 80)),
    ]

    # Create an instance of _Connector
    connector = _Connector(addrinfo, lambda af, addr: (None, Future()))

    # Call the split method
    primary, secondary = connector.split(addrinfo)

    # Check if the primary list contains all AF_INET addresses
    assert all(af == socket.AF_INET for af, _ in primary), "Primary list should contain only AF_INET addresses"

    # Check if the secondary list contains all AF_INET6 addresses

# Generated at 2024-03-18 08:30:39.398510
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():    from unittest import TestCase, mock


# Generated at 2024-03-18 08:30:44.041753
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))], connect=lambda x, y: (None, Future()))
    connector.try_connect = MagicMock()
    connector.future = MagicMock()

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(iter(connector.secondary_addrs))
    assert connector.timeout is None
    connector.future.done.assert_not_called()

# Generated at 2024-03-18 08:30:45.757620
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():from tornado.testing import AsyncTestCase, gen_test
from unittest.mock import patch, Mock


# Generated at 2024-03-18 08:31:30.912073
# Unit test for method split of class _Connector
def test__Connector_split():    # Arrange
    addrinfo_ipv4 = (socket.AF_INET, ('127.0.0.1', 80))
    addrinfo_ipv6 = (socket.AF_INET6, ('::1', 80, 0, 0))
    addrinfo_mixed = [addrinfo_ipv4, addrinfo_ipv6]

    # Act
    primary, secondary = _Connector.split(addrinfo_mixed)

    # Assert
    assert primary == [addrinfo_ipv4], "Expected primary list to contain only IPv4 addresses"
    assert secondary == [addrinfo_ipv6], "Expected secondary list to contain only IPv6 addresses"

# Generated at 2024-03-18 08:31:36.421059
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():    # Setup the connector with a mock connect method
    connector = _Connector(addrinfo=[], connect=lambda af, addr: (None, Future()))
    connector.io_loop = IOLoop.current()
    
    # Mock the IOStream to test if it's closed properly
    mock_stream = IOStream(socket.socket())
    connector.streams.add(mock_stream)
    
    # Set a future for the connector and check if it's not done
    assert not connector.future.done()
    
    # Call the on_connect_timeout method
    connector.on_connect_timeout()
    
    # Check if the future is done and raised a TimeoutError
    assert connector.future.done()
    try:
        connector.future.result()
        assert False, "Expected TimeoutError"
    except TimeoutError:
        pass
    
    # Check if the stream was closed
    assert mock_stream.closed()

# Generated at 2024-03-18 08:31:42.868154
# Unit test for method start of class _Connector
def test__Connector_start():    # Mock the connect method to return a future that will be set with a stream
    def mock_connect(af, addr):
        future = Future()
        stream = IOStream(socket.socket(af))
        future.set_result((stream, future))
        return stream, future

    # Create a list of addrinfo tuples
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]

    # Instantiate the _Connector with the mock connect method
    connector = _Connector(addrinfo, mock_connect)

    # Start the connector with a timeout
    result_future = connector.start(timeout=0.1)

    # Wait for the future to complete
    IOLoop.current().run_sync(lambda: result_future)

    # Check that the future has a result and it's an IOStream instance
    assert result_future.done()
    af, addr,

# Generated at 2024-03-18 08:31:52.841834
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():    from unittest import TestCase, mock


# Generated at 2024-03-18 08:31:59.196336
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():    from unittest import TestCase, mock


# Generated at 2024-03-18 08:32:08.285394
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    from unittest.mock import Mock, patch

# Generated at 2024-03-18 08:32:09.617180
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():from tornado.testing import AsyncTestCase, gen_test
from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 08:32:16.347716
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    timeout_duration = 5.0
    original_timeout = connector.connect_timeout

    # Act
    connector.set_connect_timeout(timeout_duration)
    new_timeout = connector.connect_timeout

    # Assert
    assert original_timeout is None
    assert new_timeout is not None
    assert connector.io_loop.time() + timeout_duration == new_timeout.callback_time

# Generated at 2024-03-18 08:32:24.247035
# Unit test for method start of class _Connector
def test__Connector_start():    # Mock the connect method to return a future that is already done
    def mock_connect(af, addr):
        future = Future()
        future.set_result((IOStream(socket.socket(af)), future))
        return IOStream(socket.socket(af)), future

    # Create a list of addrinfo tuples
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]

    # Instantiate the _Connector with the mock connect method
    connector = _Connector(addrinfo, mock_connect)

    # Start the connector with a timeout
    result_future = connector.start(timeout=0.1)

    # Run the IOLoop until the future is done
    IOLoop.current().run_sync(lambda: result_future)

    # Check that the result is as expected
    af, addr, stream = result_future.result()
    assert af

# Generated at 2024-03-18 08:32:28.980064
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))

# Generated at 2024-03-18 08:33:49.798598
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():    # Setup the test environment and objects
    io_loop = IOLoop.current()
    connector = _Connector(addrinfo=[], connect=lambda x, y: (None, Future()))

    # Mock the IOLoop's time and add_timeout functions
    current_time = 100
    io_loop.time = lambda: current_time
    timeouts = []

    def add_timeout(time, callback):
        timeouts.append((time, callback))
        return callback

    io_loop.add_timeout = add_timeout

    # Call the method under test
    timeout_seconds = 1.5
    connector.set_timeout(timeout_seconds)

    # Assert that the timeout was set correctly
    assert len(timeouts) == 1, "Expected one timeout to be set"
    set_time, callback = timeouts[0]
    assert set_time == current_time + timeout_seconds, "Timeout set for the wrong time"
    assert callback == connector.on_timeout, "Wrong callback set for the timeout"

    #

# Generated at 2024-03-18 08:33:56.837028
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    # Setup the environment and mocks
    io_loop = IOLoop.current()
    connect_mock = MagicMock()
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    connector = _Connector(addrinfo, connect_mock)
    connector.future = Future()
    connector.remaining = 2
    stream_mock = MagicMock(spec=IOStream)
    future_mock = Future()
    future_mock.set_result(stream_mock)
    connector.streams.add(stream_mock)

    # Test a successful connection
    connector.on_connect_done(iter(addrinfo), socket.AF_INET, ('127.0.0.1', 80), future_mock)
    assert connector.future.done()
    assert connector.future.result() == (socket.AF_INET, ('127.0.0.1', 80), stream_mock)
    assert stream_mock not in connector.streams

    # Reset for

# Generated at 2024-03-18 08:34:04.168566
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():    # Setup
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    primary, secondary = _Connector.split(addrinfo)

    def fake_connect(af, addr):
        future = Future()
        if addr[0] == '127.0.0.1':
            future.set_result((IOStream(socket.socket(af)), future))
        else:
            future.set_exception(ConnectionRefusedError())
        return IOStream(socket.socket(af)), future

    connector = _Connector(addrinfo, fake_connect)

    # Execute
    connector.try_connect(iter(primary))

    # Test that a connection attempt was made to the primary address
    assert len(connector.streams) == 1
    stream = next(iter(connector.streams))
    assert isinstance(stream, IOStream)
    assert stream.socket.family == socket.AF_INET
    assert stream

# Generated at 2024-03-18 08:34:15.443391
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    # Mocking the IOStream and Future objects
    mock_stream = unittest.mock.Mock(spec=IOStream)
    mock_future = unittest.mock.Mock(spec=Future)

    # Creating an instance of _Connector with mock data
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (mock_stream, mock_future))

    # Setting up the connector's future to be already resolved to simulate a successful connection
    connector.future.set_result((socket.AF_INET, ('127.0.0.1', 80), mock_stream))

    # Simulating a successful connection by setting the result of the mock future
    mock_future.result.return_value = mock_stream

    # Calling on_connect_done with mock parameters
    connector.on_connect_done(iter(connector.primary_addrs), socket.AF_INET, ('127.0.0.1', 80), mock_future)

    # Asserting that

# Generated at 2024-03-18 08:34:19.232087
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():    # Arrange
    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))
    connector.try_connect = mock.Mock()
    connector.future.done = mock.Mock(return_value=False)

    # Act
    connector.on_timeout()

    # Assert
    connector.try_connect.assert_called_once_with(iter(connector.secondary_addrs))


# Generated at 2024-03-18 08:34:27.817341
# Unit test for method start of class _Connector
def test__Connector_start():    # Arrange
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    connect_called_with = []

    def fake_connect(af, addr):
        future = Future()
        connect_called_with.append((af, addr))
        if addr[0] == '127.0.0.1':
            future.set_result((af, addr, IOStream(socket.socket(af))))
        else:
            future.set_exception(socket.error("connection failed"))
        return IOStream(socket.socket(af)), future

    connector = _Connector(addrinfo, fake_connect)

    # Act
    result_future = connector.start()

    # Assert
    assert not result_future.done(), "Future should not be done immediately"
    IOLoop.current().run_sync(lambda: result_future, timeout=1)

# Generated at 2024-03-18 08:34:35.460072
# Unit test for constructor of class _Connector
def test__Connector():    # Mock the connect function and addrinfo
    mock_connect = MagicMock()
    mock_addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET, ('192.168.1.1', 80))
    ]

    # Create an instance of _Connector
    connector = _Connector(mock_addrinfo, mock_connect)

    # Test if the instance is created with the correct attributes
    assert connector.connect == mock_connect
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector.last_error is None
    assert connector.remaining == len(mock_addrinfo)
    assert connector.primary_addrs == [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET, ('192.168.1.1', 80))]
   

# Generated at 2024-03-18 08:34:42.569614
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    # Mocking the necessary components for the test
    mock_stream = unittest.mock.Mock(spec=IOStream)
    mock_future = unittest.mock.Mock(spec=Future)
    mock_addrinfo = [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))]
    mock_connect = unittest.mock.Mock(return_value=(mock_stream, mock_future))
    connector = _Connector(mock_addrinfo, mock_connect)

    # Mocking the IOLoop's time and add_timeout functions
    mock_io_loop = unittest.mock.Mock(spec=IOLoop)
    mock_io_loop.time.return_value = 1000
    connector.io_loop = mock_io_loop

    # Test successful connection
    mock_future.result.return_value = mock_stream
    connector.on_connect_done(iter(mock_addrinfo), socket.AF_INET, ('127.0.0.1', 80), mock_future)
    assert connector.future.done()

# Generated at 2024-03-18 08:34:50.525047
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():    from unittest import TestCase, mock


# Generated at 2024-03-18 08:34:53.462184
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():    connector = _Connector(addrinfo=[(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda x, y: (None, Future()))

# Generated at 2024-03-18 08:37:26.458626
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():    from unittest.mock import Mock, patch