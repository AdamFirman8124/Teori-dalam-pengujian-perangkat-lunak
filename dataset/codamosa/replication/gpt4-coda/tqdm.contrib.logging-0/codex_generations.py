

# Generated at 2024-03-18 08:33:33.390427
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:33:38.312167
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    logger.setLevel(logging.NOTSET)


# Generated at 2024-03-18 08:33:46.332421
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=100,
        msg="Test message",
        args=(),
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Emit the record using the handler
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    expected_output = "test - INFO - Test message\n"
    assert stream_value == expected_output, f"Expected '{expected_output}', got '{stream_value}'"


# Generated at 2024-03-18 08:33:53.133172
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info("Test message without redirection")
    assert "Test message without redirection" in stream.getvalue()

    # Clear the stream
    stream.seek(0)
    stream.truncate(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message with redirection")
        assert "Test message with redirection" not in stream.getvalue()

    # Check if the message was redirected to tqdm.write
    assert "Test message with redirection" in std_tqdm.write.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    std_tqdm.write.getvalue().seek(0)
    std_tqdm.write.getvalue().truncate(0)


# Generated at 2024-03-18 08:33:59.391072
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info("Test message without redirection")
    assert "Test message without redirection" in stream.getvalue()

    # Clear the stream
    stream.seek(0)
    stream.truncate(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message with redirection")
        assert "Test message with redirection" not in stream.getvalue()

    # Check if the message was redirected to tqdm.write
    assert "Test message with redirection" in std_tqdm.write.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:34:06.352308
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:34:16.300336
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    handler.close()


# Generated at 2024-03-18 08:34:20.325635
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Capture the output of the logging
    from io import StringIO
    stream = StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Use the context manager to redirect logging
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message")

    # Check that the output was redirected to tqdm.write
    assert "Test message" in stream.getvalue()

    # Clean up by removing the handler
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:34:25.270845
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # Emit the record
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    assert stream_value.strip() == "test - INFO - Test message"


# Generated at 2024-03-18 08:34:31.702002
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Emit the record using the handler
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    assert stream_value.strip() == "test - INFO - Test message"


# Generated at 2024-03-18 08:34:49.425191
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=100,
        msg="Test message",
        args=(),
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Emit the record using the handler
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    expected_output = "test - INFO - Test message\n"
    assert stream_value == expected_output, f"Expected '{expected_output}', got '{stream_value}'"


# Generated at 2024-03-18 08:34:55.535315
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

    # Mock the tqdm class to avoid actual output during testing

# Generated at 2024-03-18 08:35:01.802957
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

    # Mock the tqdm class to avoid actual output during testing

# Generated at 2024-03-18 08:35:09.857874
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output of the tqdm.write method
    with unittest.mock.patch('tqdm.std.tqdm.write') as mock_write:
        # Create a log record
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=100,
            msg="Test message",
            args=None,
            exc_info=None,
        )

        # Create a _TqdmLoggingHandler instance
        handler = _TqdmLoggingHandler()

        # Set a simple formatter for the handler
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)

        # Emit the record using the handler
        handler.emit(record)

        # Check that tqdm.write was called with the formatted message
        mock_write.assert_called_once_with("Test message", file=None)


# Generated at 2024-03-18 08:35:18.350965
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:35:25.077450
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:35:33.103102
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:35:37.801966
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Capture the output of the logging
    from io import StringIO
    stream = StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Use the context manager to redirect logging
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message")

    # Check that the output was redirected to tqdm.write
    assert "Test message" in stream.getvalue()

    # Clean up by removing the handler
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:35:45.270646
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    from io import StringIO

# Generated at 2024-03-18 08:35:50.054427
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirect')
    assert 'Test without redirect' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirect')
        assert 'Test with redirect' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:36:11.986912
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:36:20.464232
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output of the tqdm.write method
    with unittest.mock.patch('tqdm.std.tqdm.write') as mock_write:
        # Create a log record
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=100,
            msg="Test message",
            args=None,
            exc_info=None
        )

        # Create a _TqdmLoggingHandler instance
        tqdm_handler = _TqdmLoggingHandler()

        # Set a simple formatter for the handler
        formatter = logging.Formatter('%(message)s')
        tqdm_handler.setFormatter(formatter)

        # Emit the log record using the handler
        tqdm_handler.emit(record)

        # Check that tqdm.write was called with the formatted message
        mock_write.assert_called_once_with("Test message", file=None)


# Generated at 2024-03-18 08:36:25.665403
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirect')
    assert 'Test without redirect' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirect')
        assert 'Test with redirect' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    logger.setLevel(logging.NOTSET)


# Generated at 2024-03-18 08:36:33.224088
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:36:40.334570
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:36:46.626266
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Create a tqdm progress bar and a log message
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message inside tqdm context")
        progress_bar = std_tqdm(range(1))
        for _ in progress_bar:
            pass

    # Check that the log message was redirected to the tqdm write method
    output = stream.getvalue()
    assert "Test message inside tqdm context" in output

    # Clean up by removing the handler
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:36:53.391423
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    import logging

# Generated at 2024-03-18 08:37:00.057239
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    handler.close()


# Generated at 2024-03-18 08:37:04.269458
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    handler.close()


# Generated at 2024-03-18 08:37:12.664363
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:37:42.226780
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:37:49.276783
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:37:55.262361
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info("Test message without redirection")
    assert "Test message without redirection" in stream.getvalue()

    # Clear stream
    stream.seek(0)
    stream.truncate(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message with redirection")
        assert "Test message with redirection" not in stream.getvalue()

    # Check if the message was redirected to tqdm
    with std_tqdm.external_write_mode(file=io.StringIO()) as fake_output:
        std_tqdm.write("Test message with redirection", file=fake_output)
        assert "Test message with redirection" in fake_output.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:38:03.259968
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output of the tqdm.write method
    with unittest.mock.patch('tqdm.std.tqdm.write') as mock_write:
        handler = _TqdmLoggingHandler()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=100,
            msg="Test message",
            args=(),
            exc_info=None,
        )
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Emit a log record
        handler.emit(record)

        # Check that tqdm.write was called with the formatted message
        mock_write.assert_called_once_with('test - INFO - Test message', file=sys.stderr)


# Generated at 2024-03-18 08:38:09.696502
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:38:13.804983
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    stream.close()


# Generated at 2024-03-18 08:38:20.661192
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    from io import StringIO

# Generated at 2024-03-18 08:38:27.854275
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:38:33.410597
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    import logging

# Generated at 2024-03-18 08:38:39.849991
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:39:34.689446
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:39:40.801303
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output of the tqdm.write method
    with unittest.mock.patch('tqdm.std.tqdm.write') as mock_write:
        # Create a log record
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=100,
            msg="Test message",
            args=None,
            exc_info=None
        )

        # Create a _TqdmLoggingHandler instance
        handler = _TqdmLoggingHandler()

        # Set a simple formatter for the handler
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)

        # Emit the record using the handler
        handler.emit(record)

        # Check that tqdm.write was called with the formatted message
        mock_write.assert_called_once_with("Test message", file=None)


# Generated at 2024-03-18 08:39:45.476727
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from io import StringIO

# Generated at 2024-03-18 08:39:54.876287
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test message without redirection')
    assert 'Test message without redirection' in stream.getvalue()

    # Clear stream
    stream.seek(0)
    stream.truncate(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test message with redirection')
        assert 'Test message with redirection' not in stream.getvalue()

    # Check if the message was redirected to tqdm
    with std_tqdm.external_write_mode(file=io.StringIO()) as fake_output:
        logger.info('Test message with redirection')
        assert 'Test message with redirection' in fake_output.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:40:01.837404
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info("Test message without redirection")
    assert "Test message without redirection" in stream.getvalue()

    # Clear the stream
    stream.seek(0)
    stream.truncate(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message with redirection")
        assert "Test message with redirection" not in stream.getvalue()

    # Check if the message was redirected to tqdm's write method
    with std_tqdm.external_write_mode(file=io.StringIO()) as fake_output:
        logger.info("Test message with redirection")
        assert "Test message with redirection" in fake_output.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:40:05.483319
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirect')
    assert 'Test without redirect' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirect')
        assert 'Test with redirect' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    handler.close()


# Generated at 2024-03-18 08:40:09.198865
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test message without redirection')
    assert 'Test message without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test message with redirection')
        assert 'Test message with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:40:16.897552
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Create a mock tqdm class to capture write calls
    class MockTqdm:
        writes = []

        @classmethod
        def write(cls, msg, file=None):
            cls.writes.append(msg)

    # Use the context manager to redirect logging
    with logging_redirect_tqdm(loggers=[logger], tqdm_class=MockTqdm):
        logger.info("Test message")

    # Check that the message was redirected to tqdm, not the original stream
    assert "Test message" in MockTqdm.writes, "The message was not redirected to tqdm.write()"
    assert stream.getvalue() == "", "The message was not supposed to be in the original stream"

    # Clean up by removing the handler

# Generated at 2024-03-18 08:40:21.792019
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=100,
        msg="Test message",
        args=None,
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Emit the record using the handler
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    assert stream_value.strip() == "test - INFO - Test message"


# Generated at 2024-03-18 08:40:27.525069
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    handler.stream = stream

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None,
    )

    # Format the record
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Emit the record using the handler
    handler.emit(record)

    # Check the output
    stream_value = stream.getvalue()
    assert stream_value.strip() == "test - INFO - Test message"


# Generated at 2024-03-18 08:42:08.807134
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:42:14.837564
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:42:19.007178
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirect')
    assert 'Test without redirect' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirect')
        assert 'Test with redirect' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)
    handler.close()


# Generated at 2024-03-18 08:42:25.840912
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info("Test message without redirection")
    assert "Test message without redirection" in stream.getvalue()

    # Clear the stream
    stream.truncate(0)
    stream.seek(0)

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message with redirection")
        assert "Test message with redirection" not in stream.getvalue()

    # Check if the message was written to tqdm's output
    with std_tqdm(total=1, file=io.StringIO()) as pbar:
        pbar.write("Test message with redirection")
        assert "Test message with redirection" in pbar.fp.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:42:30.595788
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirection')
    assert 'Test without redirection' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirection')
        assert 'Test with redirection' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:42:35.981930
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Capture the output during the test
    from io import StringIO
    stream = StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Create a message to log
    test_message = "Test message for logging_redirect_tqdm"

    # Use the context manager to redirect logging
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info(test_message)

    # Check that the message was redirected to tqdm.write
    assert test_message in stream.getvalue()

    # Clean up by removing the handler
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:42:44.700481
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:42:53.121895
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock

# Generated at 2024-03-18 08:43:00.230184
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    # Setup
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging without redirection
    logger.info('Test without redirect')
    assert 'Test without redirect' in stream.getvalue()

    # Test logging with redirection
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('Test with redirect')
        assert 'Test with redirect' not in stream.getvalue()

    # Cleanup
    logger.removeHandler(handler)


# Generated at 2024-03-18 08:43:07.914642
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    from unittest.mock import patch, MagicMock