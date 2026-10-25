

# Generated at 2026-10-25 02:00:22.767118
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = object()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-25 02:00:27.347996
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-25 02:00:28.771027
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():import logging

logger = logging.getLogger("test_logger")
decorator = LoggedFunction(logger)
assert decorator.logger is logger
assert callable(decorator)

# Generated at 2026-10-25 02:00:39.422458
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, increment=0):
        """Example function."""
        received_arguments.append((value, increment))
        return len(value) + increment

    result = example(" test ", increment=2)

    # The wrapped function receives the original, unmodified arguments.
    assert received_arguments == [(" test ", 2)]
    assert result == 8

    # functools.wraps preserves the wrapped function's metadata.
    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."

    assert logger.debug.call_args_list == [
        call("example('test', increment=2)"),
        call("example -> 8"),
    ]

# Generated at 2026-10-25 02:00:47.716254
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    implementation = Mock(return_value=3)

    @LoggedFunction(logger)
    def add(value, increment=0):
        return implementation(value, increment=increment)

    result = add(" test ", increment=2)

    assert result == 3
    implementation.assert_called_once_with(" test ", increment=2)
    assert logger.debug.call_args_list == [
        call("add('test', increment=2)"),
        call("add -> 3"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert add.__name__ == "add"

# Generated at 2026-10-25 02:00:51.912530
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"

# Generated at 2026-10-25 02:01:00.617020
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, count=0):
        return count + 1

    result = example("  test  ", count=2)

    assert result == 3
    assert example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('test', count=2)"),
        call("example -> 3"),
    ]

# Generated at 2026-10-25 02:01:10.755586
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def sample(name, count=1):
        """Sample function."""
        assert name == " Alice "  # Logging must not modify the actual argument
        return "done"

    result = sample(" Alice ", count=2)

    assert result == "done"
    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Sample function."
    assert logger.debug.call_args_list == [
        call("sample('Alice', count=2)"),
        call("sample -> done"),
    ]

# Generated at 2026-10-25 02:01:19.656933
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def sample_function(value, count=0):
        # Ensure the decorator passes the original value unchanged.
        assert value == "  hello  "
        return count + 1

    result = sample_function("  hello  ", count=2)

    assert result == 3
    assert sample_function.__name__ == "sample_function"
    logger.debug.assert_has_calls(
        [
            call("sample_function('hello', count=2)"),
            call("sample_function -> 3"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:01:29.290217
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()

    def normalize(value, suffix=""):
        return value.strip() + suffix.strip()

    decorated = LoggedFunction(logger)(normalize)

    result = decorated(" foo ", suffix=" bar ")

    assert result == "foobar"
    assert decorated.__name__ == "normalize"
    logger.debug.assert_has_calls(
        [
            call("normalize('foo', suffix='bar')"),
            call("normalize -> foobar"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:01:38.491840
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def repeat(value, times=1):
        """Repeat a value."""
        received_arguments.append((value, times))
        return value.strip() * times

    result = repeat(" hello ", times=2)

    assert result == "hellohello"
    assert received_arguments == [(" hello ", 2)]
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat a value."
    assert logger.debug.call_args_list == [
        call("repeat('hello', times=2)"),
        call("repeat -> hellohello"),
    ]

# Generated at 2026-10-25 02:01:48.028402
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        """Add an increment to a value."""
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add an increment to a value."
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 02:01:50.445883
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:01:52.862316
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:01:55.433975
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:01:57.849989
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:02:00.266330
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:02:21.721542
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session()

# Generated at 2026-10-25 02:02:31.128531
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def multiply(value, factor=1):
        """Multiply value by factor."""
        return value * factor

    result = multiply(4, factor=3)

    assert result == 12
    assert logger.debug.call_args_list == [
        call("multiply(4, factor=3)"),
        call("multiply -> 12"),
    ]

    # Verify functools.wraps preserves function metadata.
    assert multiply.__name__ == "multiply"
    assert multiply.__doc__ == "Multiply value by factor."

# Generated at 2026-10-25 02:02:33.654759
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:02:36.070598
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:02:38.596188
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:02:41.128046
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:43.664865
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:46.080544
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:48.497547
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:50.911006
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:53.326392
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:55.753180
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:02:58.168048
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:03:00.582129
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:03:02.996847
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:03:04.433498
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 02:03:15.891424
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    decorator = LoggedFunction(logger)

    def add(value, increment=0):
        """Add an increment to a value."""
        return value + increment

    logged_add = decorator(add)

    result = logged_add(2, increment=3)

    assert result == 5
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert logged_add.__name__ == "add"
    assert logged_add.__doc__ == "Add an increment to a value."
    assert logged_add.__wrapped__ is add

# Generated at 2026-10-25 02:03:24.618982
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def greet(name, punctuation="!"):
        """Return a greeting."""
        return f"Hello, {name.strip()}{punctuation}"

    result = greet(" Alice ", punctuation="?")

    assert result == "Hello, Alice?"
    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Return a greeting."
    assert logger.debug.call_args_list == [
        call("greet('Alice', punctuation='?')"),
        call("greet -> Hello, Alice?"),
    ]

# Generated at 2026-10-25 02:03:33.999233
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    implementation = Mock(return_value="success")

    def example(value, *, enabled=False):
        return implementation(value, enabled=enabled)

    decorated = LoggedFunction(logger)(example)

    result = decorated("  input  ", enabled=True)

    assert result == "success"
    implementation.assert_called_once_with("  input  ", enabled=True)
    assert logger.debug.call_args_list == [
        call("example('input', enabled=True)"),
        call("example -> success"),
    ]

    # Verify functools.wraps preserved the original function metadata.
    assert decorated.__name__ == "example"

# Generated at 2026-10-25 02:03:52.343380
# Unit test for function build_requests_session
def test_build_requests_session():
    custom_retry = Retry(total=3)

    with module_0.build_requests_session(retry=custom_retry) as session:
        assert isinstance(session, Session)

        # Verify raise_for_status response hook.
        assert len(session.hooks["response"]) == 1
        response = Mock()
        response.raise_for_status.return_value = None

        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Verify retry adapters are mounted for both protocols.
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert http_adapter.max_retries is custom_retry
        assert https_adapter.max_retries is custom_retry


def test_build_requests_session_without_raise_for_status():
    with module_0.build_requests_session(raise_for_status=False) as session:
        assert session.hooks["response"] == []


def test_build_requests_session_with_integer_retry_count():
    with module_0.build_requests_session(retry=5) as session:
        assert session.get_adapter("http://example.com").max_retries.total == 5
        assert session.get_adapter("https://example.com").max_retries.total == 5


def test_build_requests_session_without_retries():
    with module_0.build_requests_session(retry=False) as session:
        # Requests' default adapters have retries disabled.
        assert session.get_adapter("http://example.com").max_retries.total == 0
        assert session.get_adapter("https://example.com").max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:03:54.761267
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:03:57.288467
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:03:59.702318
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:04:02.116709
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:04.533864
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:11.430389
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:25.609545
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def length(value, *, extra=0):
        received_arguments.append((value, extra))
        return len(value) + extra

    result = length(" hello ", extra=2)

    assert result == 9
    assert received_arguments == [(" hello ", 2)]
    assert length.__name__ == "length"

    assert logger.debug.call_args_list == [
        call("length('hello', extra=2)"),
        call("length -> 9"),
    ]

    # A None result should not produce a result log entry.
    logger.reset_mock()

    @LoggedFunction(logger)
    def no_result(value):
        received_arguments.append(value)

    assert no_result("test") is None
    logger.debug.assert_called_once_with("no_result('test')")

# Generated at 2026-10-25 02:04:35.153126
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, multiplier=1):
        """Example function."""
        return value * multiplier

    result = example(3, multiplier=2)

    assert result == 6
    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."
    logger.debug.assert_has_calls(
        [
            call("example(3, multiplier=2)"),
            call("example -> 6"),
        ]
    )
    assert logger.debug.call_count == 2

    # A None return value should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def no_result(value):
        return None

    assert no_result(" value ") is None
    logger.debug.assert_called_once_with("no_result('value')")

# Generated at 2026-10-25 02:04:47.742554
# Unit test for function build_requests_session
def test_build_requests_session():from unittest.mock import Mock

import pytest
from requests.packages.urllib3.util.retry import Retry


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_with_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    try:
        assert session.get_adapter("http://").max_retries.total == retry_count
        assert session.get_adapter("https://").max_retries.total == retry_count
    finally:
        session.close()


def test_build_requests_session_with_default_retry():
    session = module_0.build_requests_session(retry=True)

    try:
        assert isinstance(session.get_adapter("http://").max_retries, Retry)
        assert isinstance(session.get_adapter("https://").max_retries, Retry)
    finally:
        session.close()


def test_build_requests_session_with_custom_retry():
    retry = Retry(total=4, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)

    try:
        assert session.get_adapter("http://").max_retries is retry
        assert session.get_adapter("https://").max_retries is retry
    finally:
        session.close()


def test_build_requests_session_without_retry():
    session = module_0.build_requests_session(retry=False)

    try:
        # The adapters installed by requests.Session use zero retries.
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_installs_raise_for_status_hook():
    session = module_0.build_requests_session(raise_for_status=True, retry=False)
    response = Mock()

    try:
        assert len(session.hooks["response"]) == 1

        session.hooks["response"][0](response)

        response.raise_for_status.assert_called_once_with()
    finally:
        session.close()


def test_build_requests_session_without_raise_for_status_hook():
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    try:
        assert session.hooks["response"] == []
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:04:50.303531
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:52.827110
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:55.347746
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:04:57.866180
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:05:00.281789
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:05:02.696295
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:05:05.111748
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:05:07.526815
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:05:14.570829
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 02:05:25.951895
# Unit test for function build_requests_session
def test_build_requests_session():
    custom_retry = Retry(total=3)
    session = module_0.build_requests_session(
        raise_for_status=True,
        retry=custom_retry,
    )

    try:
        assert isinstance(session, Session)

        # Verify the raise_for_status response hook.
        response = Mock()
        assert len(session.hooks["response"]) == 1
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Verify retry configuration for both protocols.
        for scheme in ("http://", "https://"):
            adapter = session.get_adapter(scheme)
            assert isinstance(adapter, HTTPAdapter)
            assert adapter.max_retries is custom_retry
            assert adapter.max_retries.total == 3
    finally:
        session.close()


@pytest.mark.parametrize("retry_count", [0, 1, 5])
def test_build_requests_session_with_integer_retry(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    try:
        adapter = session.get_adapter("https://")

        # retry=0 disables custom retry configuration due to `if retry`.
        expected_total = 0 if retry_count == 0 else retry_count
        assert adapter.max_retries.total == expected_total
    finally:
        session.close()


def test_build_requests_session_without_raise_for_status_hook():
    session = module_0.build_requests_session(raise_for_status=False)

    try:
        assert session.hooks["response"] == []
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:05:31.774226
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    logger.debug.assert_has_calls(
        [
            call("add(2, increment=3)"),
            call("add -> 5"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:05:43.557746
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    with module_0.build_requests_session() as session:
        assert len(session.hooks["response"]) == 1
        assert isinstance(session.adapters["http://"].max_retries, Retry)
        assert isinstance(session.adapters["https://"].max_retries, Retry)

        # Verify the response hook calls raise_for_status()
        response = Response()
        response.status_code = 500
        response.url = "https://example.com"

        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

    # Disable raise_for_status and retries
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0

    # Integer retry count
    with module_0.build_requests_session(retry=3) as session:
        assert session.adapters["http://"].max_retries.total == 3
        assert session.adapters["https://"].max_retries.total == 3

    # Explicit Retry instance
    retry_config = Retry(total=5)
    with module_0.build_requests_session(retry=retry_config) as session:
        assert session.adapters["http://"].max_retries is retry_config
        assert session.adapters["https://"].max_retries is retry_config

    # Invalid retry configuration
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:05:53.290390
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def repeat(value, multiplier=1):
        return value * multiplier

    result = repeat("abc", multiplier=2)

    assert result == "abcabc"
    assert repeat.__name__ == "repeat"
    assert logger.debug.call_args_list == [
        call("repeat('abc', multiplier=2)"),
        call("repeat -> abcabc"),
    ]

# Generated at 2026-10-25 02:06:03.038863
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, count=1):
        """Example function."""
        return count * 2

    result = example("  hello  ", count=3)

    assert result == 6
    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."
    assert logger.debug.call_args_list == [
        call("example('hello', count=3)"),
        call("example -> 6"),
    ]

# Generated at 2026-10-25 02:06:13.349354
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def repeat(value, count=1):
        received_arguments.append((value, count))
        return value * count

    result = repeat(" test ", count=2)

    assert result == " test  test "
    assert received_arguments == [(" test ", 2)]
    assert repeat.__name__ == "repeat"

    assert logger.debug.call_args_list == [
        call("repeat('test', count=2)"),
        call("repeat ->  test  test "),
    ]

# Generated at 2026-10-25 02:06:23.281707
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    function_body = Mock(return_value="done")

    def target(value, option=None):
        return function_body(value, option=option)

    decorated = LoggedFunction(logger)(target)

    result = decorated("  input  ", option=" selected ")

    assert result == "done"
    function_body.assert_called_once_with("  input  ", option=" selected ")
    assert logger.debug.call_args_list == [
        call("target('input', option='selected')"),
        call("target -> done"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert decorated.__name__ == "target"

# Generated at 2026-10-25 02:06:34.453845
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    wrapped_function = Mock(return_value="completed")

    @LoggedFunction(logger)
    def example(value, count=None):
        return wrapped_function(value, count=count)

    result = example("  test  ", count=3)

    assert result == "completed"
    assert example.__name__ == "example"
    wrapped_function.assert_called_once_with("  test  ", count=3)
    assert logger.debug.call_args_list == [
        call("example('test', count=3)"),
        call("example -> completed"),
    ]

# Generated at 2026-10-25 02:06:44.789383
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    for scheme in ("http://", "https://"):
        assert isinstance(session.adapters[scheme].max_retries, Retry)


def test_build_requests_session_without_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_build_requests_session_with_retry_count():
    session = module_0.build_requests_session(retry=3)

    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=4, backoff_factor=0.5)

    session = module_0.build_requests_session(retry=retry)

    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    # These are the default adapters installed by requests.Session.
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0


def test_build_requests_session_with_invalid_retry():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:06:54.924000
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, multiplier=1):
        return value * multiplier

    result = example(3, multiplier=4)

    assert result == 12
    logger.debug.assert_has_calls(
        [
            call("example(3, multiplier=4)"),
            call("example -> 12"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:07:05.031416
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, *, enabled=False):
        received_arguments.append((value, enabled))
        return "result"

    result = example(" value ", enabled=True)

    assert result == "result"
    assert received_arguments == [(" value ", True)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('value', enabled=True)"),
        call("example -> result"),
    ]

# Generated at 2026-10-25 02:07:20.319471
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def sample_function(text, count=1):
        return count * 2

    result = sample_function("  hello  ", count=3)

    assert result == 6
    assert sample_function.__name__ == "sample_function"
    assert logger.debug.call_args_list == [
        call("sample_function('hello', count=3)"),
        call("sample_function -> 6"),
    ]

# Generated at 2026-10-25 02:07:29.999709
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        """Add an increment to a value."""
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add an increment to a value."
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 02:07:46.517795
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Mock()
    response.raise_for_status.return_value = None
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")

    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    assert session.get_adapter("https://example.com").max_retries.total == 3

    # Explicit Retry instance
    retry_config = Retry(total=5)
    session = module_0.build_requests_session(retry=retry_config)

    assert (
        session.get_adapter("http://example.com").max_retries
        is retry_config
    )
    assert (
        session.get_adapter("https://example.com").max_retries
        is retry_config
    )

    # Disabled status hook and retries
    session = module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks["response"] == []
    assert session.get_adapter("http://example.com").max_retries.total == 0
    assert session.get_adapter("https://example.com").max_retries.total == 0

    # Invalid retry configuration
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry=object())

# Generated at 2026-10-25 02:07:57.514723
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def sample_function(text, number, *, enabled=False):
        """Sample documentation."""
        received_arguments.append((text, number, enabled))
        return number + 1 if enabled else number

    result = sample_function("  value  ", 4, enabled=True)

    assert result == 5
    assert received_arguments == [("  value  ", 4, True)]
    assert sample_function.__name__ == "sample_function"
    assert sample_function.__doc__ == "Sample documentation."

    assert logger.debug.call_args_list == [
        call("sample_function('value', 4, enabled=True)"),
        call("sample_function -> 5"),
    ]

# Generated at 2026-10-25 02:08:15.104101
# Unit test for function build_requests_session
def test_build_requests_session():
    sessions = []

    try:
        # Default configuration installs the status hook and retry adapters.
        session = module_0.build_requests_session()
        sessions.append(session)

        assert isinstance(session, Session)
        assert len(session.hooks["response"]) == 1

        response = Response()
        response.status_code = 400
        response.url = "https://example.com"
        response.reason = "Bad Request"

        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

        http_adapter = session.get_adapter("http://")
        https_adapter = session.get_adapter("https://")

        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total

        # An integer configures the total retry count.
        session = module_0.build_requests_session(retry=3)
        sessions.append(session)

        assert session.get_adapter("https://").max_retries.total == 3

        # A Retry instance is used directly.
        retry = Retry(total=5, backoff_factor=0.5)
        session = module_0.build_requests_session(retry=retry)
        sessions.append(session)

        assert session.get_adapter("http://").max_retries is retry
        assert session.get_adapter("https://").max_retries is retry

        # Retry and status handling can be disabled.
        session = module_0.build_requests_session(raise_for_status=False, retry=False)
        sessions.append(session)

        assert session.hooks["response"] == []
        assert session.get_adapter("https://").max_retries.total == 0

        # Unsupported retry values are rejected.
        with pytest.raises(
            ValueError,
            match="retry should be a bool, int or Retry instance",
        ):
            module_0.build_requests_session(retry="invalid")

    finally:
        for session in sessions:
            session.close()

# Generated at 2026-10-25 02:08:27.613443
# Unit test for function build_requests_session
def test_build_requests_session():
    sessions = []

    try:
        # Default configuration installs the status hook and retry adapters.
        session = module_0.build_requests_session()
        sessions.append(session)

        assert len(session.hooks["response"]) == 1
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        for prefix in ("http://", "https://"):
            adapter = session.get_adapter(prefix)
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == Retry().total

        # Disabling raise_for_status leaves the response hooks empty.
        session = module_0.build_requests_session(raise_for_status=False)
        sessions.append(session)
        assert session.hooks["response"] == []

        # An integer configures the total retry count.
        session = module_0.build_requests_session(retry=3)
        sessions.append(session)
        assert session.get_adapter("http://").max_retries.total == 3
        assert session.get_adapter("https://").max_retries.total == 3

        # A supplied Retry instance is used by both adapters.
        retry_config = Retry(total=5, backoff_factor=0.5)
        session = module_0.build_requests_session(retry=retry_config)
        sessions.append(session)
        assert session.get_adapter("http://").max_retries is retry_config
        assert session.get_adapter("https://").max_retries is retry_config

        # False disables custom retry configuration. Requests' default
        # adapters use zero retries.
        session = module_0.build_requests_session(retry=False)
        sessions.append(session)
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0

        # Unsupported truthy values are rejected.
        with pytest.raises(
            ValueError,
            match="retry should be a bool, int or Retry instance",
        ):
            module_0.build_requests_session(retry="invalid")

    finally:
        for session in sessions:
            session.close()

# Generated at 2026-10-25 02:08:37.369249
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def multiply(value, factor=1):
        return value * factor

    result = multiply(4, factor=3)

    assert result == 12
    assert multiply.__name__ == "multiply"
    assert logger.debug.call_args_list == [
        call("multiply(4, factor=3)"),
        call("multiply -> 12"),
    ]

# Generated at 2026-10-25 02:08:47.155181
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_spy = Mock(return_value="done")

    def example(value, count=None):
        return function_spy(value, count=count)

    decorated = LoggedFunction(logger)(example)

    result = decorated("  test value  ", count=3)

    assert result == "done"
    function_spy.assert_called_once_with("  test value  ", count=3)
    assert decorated.__name__ == example.__name__

    logger.debug.assert_has_calls(
        [
            call("example('test value', count=3)"),
            call("example -> done"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:08:58.019691
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, *, count=1):
        received_arguments.append((value, count))
        return 42

    result = example("  test  ", count=3)

    assert result == 42
    assert received_arguments == [("  test  ", 3)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('test', count=3)"),
        call("example -> 42"),
    ]

# Generated at 2026-10-25 02:09:00.424895
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:03.024036
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:05.438960
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:07.854731
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:10.274244
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:12.962037
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:15.377050
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:17.792202
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:20.207152
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:09:28.217392
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def repeat(text, count=1):
        """Repeat the supplied text."""
        return text.strip() * count

    result = repeat(" hello ", count=2)

    assert result == "hellohello"
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat the supplied text."
    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat -> hellohello"),
    ]

# Generated at 2026-10-25 02:09:39.000143
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()

    @LoggedFunction(logger)
    def repeat(value, count=1):
        """Repeat a value."""
        return value.strip() * count

    result = repeat(" hello ", count=2)

    assert result == "hellohello"
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat a value."
    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat -> hellohello"),
    ]

    # A None result should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def do_nothing(value):
        return None

    assert do_nothing(" value ") is None
    logger.debug.assert_called_once_with("do_nothing('value')")

# Generated at 2026-10-25 02:09:48.082871
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, count, enabled=False):
        received_arguments.append((value, count, enabled))
        return "completed"

    result = example("  test  ", 3, enabled=True)

    assert result == "completed"
    assert received_arguments == [("  test  ", 3, True)]
    assert logger.debug.call_args_list == [
        call("example('test', 3, enabled=True)"),
        call("example -> completed"),
    ]

    # functools.wraps should preserve the wrapped function's metadata.
    assert example.__name__ == "example"

# Generated at 2026-10-25 02:09:57.201272
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocation_count = 0

    def sample_function(value, multiplier=1):
        nonlocal invocation_count
        invocation_count += 1
        return len(value) * multiplier

    decorated_function = LoggedFunction(logger)(sample_function)

    result = decorated_function(" test ", multiplier=2)

    assert result == 12
    assert invocation_count == 1

    # functools.wraps should preserve the wrapped function's metadata.
    assert decorated_function.__name__ == "sample_function"
    assert decorated_function.__wrapped__ is sample_function

    assert logger.debug.call_args_list == [
        call("sample_function('test', multiplier=2)"),
        call("sample_function -> 12"),
    ]

# Generated at 2026-10-25 02:10:06.198730
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    wrapped_function = Mock(return_value="success")

    @LoggedFunction(logger)
    def example(value, count=0):
        return wrapped_function(value, count=count)

    result = example("  test  ", count=2)

    assert result == "success"
    wrapped_function.assert_called_once_with("  test  ", count=2)
    assert logger.debug.call_args_list == [
        call("example('test', count=2)"),
        call("example -> success"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert example.__name__ == "example"

# Generated at 2026-10-25 02:10:08.617456
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:10:11.152929
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:10:13.567865
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:10:15.983651
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:10:18.583716
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:10:21.004324
# Unit test for method __call__ of class LoggedFunction