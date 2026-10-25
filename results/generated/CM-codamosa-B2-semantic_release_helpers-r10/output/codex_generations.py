

# Generated at 2026-10-25 00:05:17.648045
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session(raise_for_status=True, retry=3)

    assert isinstance(session.adapters["http://"], HTTPAdapter)
    assert isinstance(session.adapters["https://"], HTTPAdapter)
    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3

    response = Response()
    response.status_code = 500

    with pytest.raises(HTTPError):
        session.hooks["response"][0](response)


def test_build_requests_session_without_status_hook():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:05:23.904255
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"

# Generated at 2026-10-25 00:05:35.787607
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    assert isinstance(session, Session)

    # Both protocols should use an adapter configured with the default Retry.
    expected_retries = Retry().total
    for protocol in ("http://", "https://"):
        adapter = session.get_adapter(protocol)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == expected_retries

    # The response hook should invoke raise_for_status.
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    session.close()


def test_build_requests_session_without_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []

    session.close()


@pytest.mark.parametrize("retry_count", [0, 1, 3])
def test_build_requests_session_with_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    for protocol in ("http://", "https://"):
        adapter = session.get_adapter(protocol)
        assert adapter.max_retries.total == retry_count

    session.close()


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=4, backoff_factor=0.5)

    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    session.close()


def test_build_requests_session_without_retry():
    session = module_0.build_requests_session(retry=False)

    # These are the default adapters installed by requests.Session.
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    session.close()


def test_build_requests_session_rejects_invalid_retry():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:05:40.570549
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg(" hello ") == "'hello'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"

# Generated at 2026-10-25 00:05:49.693286
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    decorator = LoggedFunction(logger)

    assert decorator.logger is logger

# Generated at 2026-10-25 00:05:51.042030
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():import logging

logger = logging.getLogger("test_logger")
decorator = LoggedFunction(logger)
assert decorator.logger is logger
assert callable(decorator)

# Generated at 2026-10-25 00:06:03.192897
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    implementation = Mock(return_value=5)

    def sample(value, increment=0):
        return implementation(value, increment=increment)

    wrapped = LoggedFunction(logger)(sample)

    result = wrapped(2, increment=3)

    assert result == 5
    assert wrapped.__name__ == "sample"
    implementation.assert_called_once_with(2, increment=3)
    assert logger.debug.call_args_list == [
        call("sample(2, increment=3)"),
        call("sample -> 5"),
    ]

# Generated at 2026-10-25 00:06:13.093840
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def greet(name, punctuation="!"):
        invocations.append((name, punctuation))
        return f"Hello, {name.strip()}{punctuation}"

    result = greet(" Alice ", punctuation="?")

    assert result == "Hello, Alice?"
    assert invocations == [(" Alice ", "?")]
    assert greet.__name__ == "greet"
    logger.debug.assert_has_calls(
        [
            call("greet('Alice', punctuation='?')"),
            call("greet -> Hello, Alice?"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:06:15.826546
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:18.248154
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:20.678919
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:23.098062
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:25.517197
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:27.943188
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:30.367774
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:32.796204
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:35.220951
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:06:37.646008
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:03.956004
# Unit test for function build_requests_session
def test_build_requests_session():from requests import Response

# Generated at 2026-10-25 00:07:13.405782
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b, multiplier=1):
        """Add two values and apply a multiplier."""
        return (a + b) * multiplier

    result = add(2, 3, multiplier=4)

    assert result == 20
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two values and apply a multiplier."
    assert logger.debug.call_args_list == [
        call("add(2, 3, multiplier=4)"),
        call("add -> 20"),
    ]

    # A None result should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def do_nothing(value):
        return None

    assert do_nothing("  test  ") is None
    logger.debug.assert_called_once_with("do_nothing('test')")

# Generated at 2026-10-25 00:07:15.837015
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:18.599359
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:21.037169
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:23.461552
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:07:25.883280
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:07:28.301274
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:07:30.722482
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:33.146120
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:35.730046
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:38.149104
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:40.564526
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:42.986261
# Unit test for function build_requests_session

# Generated at 2026-10-25 00:07:45.403199
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:07:47.822431
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:07:50.242640
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:09.667628
# Unit test for function build_requests_session
def test_build_requests_session():sessions = []

# Generated at 2026-10-25 00:08:17.361486
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    assert add.__name__ == "add"
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 00:08:28.964122
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def sample(value, amount=0):
        """Sample function."""
        received_arguments.append((value, amount))
        return "done"

    result = sample("  hello  ", amount=2)

    assert result == "done"
    assert received_arguments == [("  hello  ", 2)]
    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Sample function."
    assert logger.debug.call_args_list == [
        call("sample('hello', amount=2)"),
        call("sample -> done"),
    ]

    # A None return value should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def no_result():
        return None

    assert no_result() is None
    logger.debug.assert_called_once_with("no_result()")

# Generated at 2026-10-25 00:08:38.264237
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def multiply(number, text, *, factor=1):
        """Example decorated function."""
        return number * factor

    result = multiply(2, "  example  ", factor=3)

    assert result == 6
    assert multiply.__name__ == "multiply"
    assert multiply.__doc__ == "Example decorated function."
    assert logger.debug.call_args_list == [
        call("multiply(2, 'example', factor=3)"),
        call("multiply -> 6"),
    ]

# Generated at 2026-10-25 00:08:40.802071
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:43.440326
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:45.866919
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:48.448710
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:50.969529
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:53.388392
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:08:55.804664
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:02.453406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:03.786248
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 00:09:13.899124
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocations = []

    def greet(name, punctuation="!"):
        invocations.append((name, punctuation))
        return f"Hello, {name.strip()}{punctuation.strip()}"

    logged_greet = LoggedFunction(logger)(greet)

    result = logged_greet(" Alice ", punctuation=" ! ")

    assert result == "Hello, Alice!"
    assert invocations == [(" Alice ", " ! ")]
    assert logged_greet.__name__ == "greet"
    assert logger.debug.call_args_list == [
        call("greet('Alice', punctuation='!')"),
        call("greet -> Hello, Alice!"),
    ]

# Generated at 2026-10-25 00:09:25.211355
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(x, y=0):
        """Add two numbers."""
        return x + y

    result = add(2, y=3)

    assert result == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."
    logger.debug.assert_has_calls(
        [
            call("add(2, y=3)"),
            call("add -> 5"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:09:43.050168
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import Mock

    import pytest

    # Default configuration enables status checking and retries.
    with module_0.build_requests_session() as session:
        response = Mock()
        assert len(session.hooks["response"]) == 1

        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        expected_total = Retry().total
        for prefix in ("http://", "https://"):
            adapter = session.get_adapter(prefix)
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == expected_total

    # An integer configures the total retry count.
    with module_0.build_requests_session(retry=3) as session:
        for prefix in ("http://", "https://"):
            assert session.get_adapter(prefix).max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry_config = Retry(total=5, backoff_factor=0.25)
    with module_0.build_requests_session(retry=retry_config) as session:
        for prefix in ("http://", "https://"):
            assert session.get_adapter(prefix).max_retries is retry_config

    # Both optional behaviors can be disabled.
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []
        for prefix in ("http://", "https://"):
            assert session.get_adapter(prefix).max_retries.total == 0

    # Unsupported retry configurations are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:09:45.469994
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:47.893170
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:50.320118
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:52.733761
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:55.149672
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:57.565528
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:09:59.981444
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:02.396744
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:04.812573
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:07.228660
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:09.643995
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:16.231517
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 00:10:25.173466
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, multiplier=1):
        return len(value) * multiplier

    result = example(" test ", multiplier=2)

    assert result == 12
    assert example.__name__ == "example"
    logger.debug.assert_has_calls(
        [
            call("example('test', multiplier=2)"),
            call("example -> 12"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:10:35.449782
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    result = add(2, b=3)

    assert result == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 00:10:46.138271
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def repeat(value, *, count=1):
        """Repeat a value."""
        return value.strip() * count

    result = repeat(" test ", count=2)

    assert result == "testtest"
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat a value."
    assert logger.debug.call_args_list == [
        call("repeat('test', count=2)"),
        call("repeat -> testtest"),
    ]

    logger.reset_mock()

    @decorator
    def returns_none():
        return None

    assert returns_none() is None
    logger.debug.assert_called_once_with("returns_none()")

# Generated at 2026-10-25 00:10:56.818069
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    implementation = Mock(return_value="result")

    def example(value, count=0):
        return implementation(value, count=count)

    logged_example = LoggedFunction(logger)(example)

    result = logged_example("  hello  ", count=2)

    assert result == "result"
    implementation.assert_called_once_with("  hello  ", count=2)
    assert logger.debug.call_args_list == [
        call("example('hello', count=2)"),
        call("example -> result"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert logged_example.__name__ == "example"

# Generated at 2026-10-25 00:11:08.048337
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(number, text="default"):
        return f"{number}: {text}"

    result = example(42, text=" hello ")

    assert result == "42:  hello "
    assert example.__name__ == "example"
    logger.debug.assert_has_calls(
        [
            call("example(42, text='hello')"),
            call("example -> 42:  hello "),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:11:22.608479
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    try:
        assert isinstance(session, Session)

        # Verify raise_for_status response hook.
        assert len(session.hooks["response"]) == 1
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Verify retry adapters are mounted for HTTP and HTTPS.
        for url in ("http://example.com", "https://example.com"):
            adapter = session.get_adapter(url)
            assert isinstance(adapter.max_retries, Retry)
    finally:
        session.close()


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_with_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    try:
        assert session.get_adapter("http://").max_retries.total == retry_count
        assert session.get_adapter("https://").max_retries.total == retry_count
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


def test_build_requests_session_without_status_hook_or_retries():
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    try:
        assert session.hooks["response"] == []
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:11:33.572736
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    with module_0.build_requests_session() as session:
        assert "http://" in session.adapters
        assert "https://" in session.adapters

        for scheme in ("http://", "https://"):
            assert isinstance(session.adapters[scheme].max_retries, Retry)

        # Verify that the response hook calls raise_for_status()
        response = Response()
        response.status_code = 500
        response.url = "https://example.com"

        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

    # Disable raise_for_status and retries
    with module_0.build_requests_session(
        raise_for_status=False, retry=False
    ) as session:
        assert session.hooks["response"] == []
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0

    # Integer retry count
    with module_0.build_requests_session(retry=3) as session:
        assert session.adapters["http://"].max_retries.total == 3
        assert session.adapters["https://"].max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5)
    with module_0.build_requests_session(retry=retry) as session:
        assert session.adapters["http://"].max_retries is retry
        assert session.adapters["https://"].max_retries is retry

    # Invalid retry value
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:11:45.351090
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()
    try:
        assert isinstance(session, Session)

        # A raise_for_status response hook is installed.
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Retry-enabled adapters are mounted for both protocols.
        assert isinstance(session.adapters["http://"].max_retries, Retry)
        assert isinstance(session.adapters["https://"].max_retries, Retry)
    finally:
        session.close()


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_with_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)
    try:
        assert session.adapters["http://"].max_retries.total == retry_count
        assert session.adapters["https://"].max_retries.total == retry_count
    finally:
        session.close()


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=4, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    try:
        assert session.adapters["http://"].max_retries is retry
        assert session.adapters["https://"].max_retries is retry
    finally:
        session.close()


def test_build_requests_session_without_retry_or_status_hook():
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    try:
        assert session.hooks["response"] == []

        # Default requests adapters disable retries.
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:11:55.889891
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def add(a, b=0):
        """Add two numbers."""
        return a + b

    logged_add = LoggedFunction(logger)(add)

    result = logged_add(2, b=3)

    assert result == 5
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert logged_add.__name__ == "add"
    assert logged_add.__doc__ == "Add two numbers."
    assert logged_add.__wrapped__ is add

# Generated at 2026-10-25 00:12:09.310746
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b=0):
        return a + b

    result = add(2, b=3)

    assert result == 5
    assert add.__name__ == "add"  # functools.wraps preserves metadata
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 00:12:20.472563
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    implementation = Mock(return_value="done")

    @LoggedFunction(logger)
    def example(value, count, enabled=False):
        return implementation(value, count, enabled=enabled)

    result = example("  test  ", 3, enabled=True)

    assert result == "done"
    implementation.assert_called_once_with("  test  ", 3, enabled=True)
    assert logger.debug.call_args_list == [
        call("example('test', 3, enabled=True)"),
        call("example -> done"),
    ]

# Generated at 2026-10-25 00:12:30.919148
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class StubLogger:
        def __init__(self):
            self.messages = []

        def debug(self, message):
            self.messages.append(message)

    logger = StubLogger()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, count, enabled=False):
        received_arguments.append((value, count, enabled))
        return "completed"

    result = example("  hello  ", 2, enabled=True)

    assert result == "completed"
    assert received_arguments == [("  hello  ", 2, True)]
    assert logger.messages == [
        "example('hello', 2, enabled=True)",
        "example -> completed",
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert example.__name__ == "example"

# Generated at 2026-10-25 00:12:41.157777
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def sample_function(value, multiplier=1):
        return len(value) * multiplier

    decorated = LoggedFunction(logger)(sample_function)

    result = decorated(" test ", multiplier=2)

    assert result == 12
    assert decorated.__name__ == sample_function.__name__
    assert decorated.__doc__ == sample_function.__doc__
    logger.debug.assert_has_calls(
        [
            call("sample_function('test', multiplier=2)"),
            call("sample_function -> 12"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:12:50.781636
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

# Generated at 2026-10-25 00:13:02.252985
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    received = {}

    def sample(value, multiplier=1):
        received["arguments"] = (value, multiplier)
        return value.strip() * multiplier

    wrapped = LoggedFunction(logger)(sample)

    result = wrapped(" hello ", multiplier=2)

    assert result == "hellohello"
    assert received["arguments"] == (" hello ", 2)

    logger.debug.assert_has_calls(
        [
            call("sample('hello', multiplier=2)"),
            call("sample -> hellohello"),
        ]
    )
    assert logger.debug.call_count == 2

    # functools.wraps should preserve the decorated function's metadata.
    assert wrapped.__name__ == "sample"

# Generated at 2026-10-25 00:13:14.429824
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def example(value, repeat=1):
        """Example function."""
        return value * repeat

    logged_example = LoggedFunction(logger)(example)

    result = logged_example("  hello  ", repeat=2)

    assert result == "  hello    hello  "
    assert logged_example.__name__ == "example"
    assert logged_example.__doc__ == "Example function."

    assert logger.debug.call_args_list == [
        call("example('hello', repeat=2)"),
        call("example ->   hello    hello  "),
    ]

# Generated at 2026-10-25 00:13:25.910189
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    response = Mock()
    for hook in session.hooks["response"]:
        hook(response)

    response.raise_for_status.assert_called_once_with()

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)

    # Retry count supplied as an integer
    session = module_0.build_requests_session(retry=3)
    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)
    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    # Disabled response hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Invalid retry argument
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:13:35.010839
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    result = add(2, b=3)

    assert result == 5
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

    # Verify functools.wraps preserves function metadata.
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

# Generated at 2026-10-25 00:13:44.137901
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def sample_function(value, multiplier=1):
        """Sample docstring."""
        return len(value) * multiplier

    result = sample_function(" test ", multiplier=2)

    assert result == 12
    assert logger.debug.call_args_list == [
        call("sample_function('test', multiplier=2)"),
        call("sample_function -> 12"),
    ]

    # Verify functools.wraps preserves the decorated function's metadata.
    assert sample_function.__name__ == "sample_function"
    assert sample_function.__doc__ == "Sample docstring."

# Generated at 2026-10-25 00:13:54.685049
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def greet(name, punctuation="!"):
        return f"Hello, {name.strip()}{punctuation}"

    result = greet(" Alice ", punctuation="?")

    assert result == "Hello, Alice?"
    assert greet.__name__ == "greet"
    logger.debug.assert_has_calls(
        [
            call("greet('Alice', punctuation='?')"),
            call("greet -> Hello, Alice?"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 00:14:03.078228
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        """Add two values."""
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two values."
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

    logger.reset_mock()

    @LoggedFunction(logger)
    def do_nothing(value):
        return None

    assert do_nothing(" test ") is None
    logger.debug.assert_called_once_with("do_nothing('test')")

# Generated at 2026-10-25 00:14:17.822604
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration installs a response hook and retry adapters.
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Response()
    response.status_code = 500
    response.url = "https://example.com"

    with pytest.raises(HTTPError):
        session.hooks["response"][0](response)

    http_adapter = session.get_adapter("http://")
    https_adapter = session.get_adapter("https://")

    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)

    # Both optional features can be disabled.
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # An integer configures the total retry count.
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    # Unsupported retry values are rejected.
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 00:14:27.766727
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

# Generated at 2026-10-25 00:14:36.459193
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def sample_function(value, multiplier=1):
        return value * multiplier

    result = sample_function(3, multiplier=2)

    assert result == 6
    assert sample_function.__name__ == "sample_function"
    assert logger.debug.call_args_list == [
        call("sample_function(3, multiplier=2)"),
        call("sample_function -> 6"),
    ]

# Generated at 2026-10-25 00:14:49.977019
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    implementation = Mock(return_value=5)

    @LoggedFunction(logger)
    def add(a, b=0):
        """Add two values."""
        return implementation(a, b=b)

    result = add(2, b=3)

    assert result == 5
    implementation.assert_called_once_with(2, b=3)
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two values."

    # A None return value should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def do_nothing(value):
        return None

    assert do_nothing(" value ") is None
    logger.debug.assert_called_once_with("do_nothing('value')")

# Generated at 2026-10-25 00:14:59.409382
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(text, count=1):
        received_arguments.append((text, count))
        return count * 2

    result = example("  value  ", count=3)

    assert result == 6
    assert received_arguments == [("  value  ", 3)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('value', count=3)"),
        call("example -> 6"),
    ]