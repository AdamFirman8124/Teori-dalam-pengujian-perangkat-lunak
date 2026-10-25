

# Generated at 2026-10-25 02:28:38.785832
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:28:41.199857
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:28:43.614986
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:28:50.563919
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import MagicMock

    logger = MagicMock(spec=logging.Logger)
    logged = LoggedFunction(logger)

    # Case 1: positional and keyword arguments, non-None return value
    @logged
    def add(a, b=0):
        return a + b

    result = add(2, b=3)
    assert result == 5
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    second_call = logger.debug.call_args_list[1][0][0]
    assert first_call == "add('2', b='3')"
    assert second_call == "add -> 5"

    # Case 2: string arguments are quoted and stripped
    logger.reset_mock()

    @logged
    def greet(name):
        return f"Hello, {name}!"

    result = greet("  world ")
    assert result == "Hello,  world !"
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world')"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == "greet -> Hello,  world !"

    # Case 3: function returns None -> only entry logged, no result log
    logger.reset_mock()

    @logged
    def do_nothing():
        return None

    result = do_nothing()
    assert result is None
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0][0][0] == "do_nothing()"

    # Case 4: functools.wraps preserves function metadata
    @logged
    def documented():
        """Docstring."""
        return 1

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "Docstring."

    # Case 5: generator return value is logged as-is (not consumed)
    logger.reset_mock()

    @logged
    def gen():
        yield 1
        yield 2

    g = gen()
    assert hasattr(g, "__next__")
    assert logger.debug.call_args_list[1][0][0].startswith("gen -> <generator object")

# Generated at 2026-10-25 02:28:59.681539
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def sample_function(value, increment=0):
        # Ensure the decorator passes arguments through unchanged.
        assert value == "  example  "
        return len(value) + increment

    decorated = LoggedFunction(logger)(sample_function)

    result = decorated("  example  ", increment=2)

    assert result == 13
    assert decorated.__name__ == "sample_function"
    logger.debug.assert_has_calls(
        [
            call("sample_function('example', increment=2)"),
            call("sample_function -> 13"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:29:04.223689
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 02:29:10.237618
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 02:29:17.790073
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b=0):
        return a + b

    result = add(2, b=3)

    assert result == 5
    assert add.__name__ == "add"
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 02:29:30.093129
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    with module_0.build_requests_session() as session:
        assert len(session.hooks["response"]) == 1

        response = Response()
        response.status_code = 500
        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

        for scheme in ("http://", "https://"):
            adapter = session.get_adapter(scheme)
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)

    # Disable raise_for_status and retry configuration
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []

        # Requests' default adapters perform zero retries.
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0

    # Integer retry count
    with module_0.build_requests_session(retry=3) as session:
        assert session.get_adapter("http://").max_retries.total == 3
        assert session.get_adapter("https://").max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5)
    with module_0.build_requests_session(retry=retry) as session:
        assert session.get_adapter("http://").max_retries is retry
        assert session.get_adapter("https://").max_retries is retry

    # Invalid retry value
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:29:32.616151
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:35.140761
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:37.558215
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:39.974242
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:29:42.390074
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:29:45.024698
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:29:47.439810
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:49.857484
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:52.272605
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:54.688984
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:57.109066
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:29:59.538103
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:30:10.744926
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    received_arguments = {}

    @LoggedFunction(logger)
    def example(text, count, enabled=False):
        received_arguments.update(
            text=text,
            count=count,
            enabled=enabled,
        )
        return "completed"

    result = example("  hello  ", 3, enabled=True)

    assert result == "completed"
    assert received_arguments == {
        "text": "  hello  ",
        "count": 3,
        "enabled": True,
    }
    assert example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('hello', 3, enabled=True)"),
        call("example -> completed"),
    ]

    # A None result should not produce a result log entry.
    logger.reset_mock()

    @LoggedFunction(logger)
    def returns_none():
        return None

    assert returns_none() is None
    logger.debug.assert_called_once_with("returns_none()")

# Generated at 2026-10-25 02:30:18.854716
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
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 02:30:27.642901
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    function_calls = []

    @LoggedFunction(logger)
    def example(name, count=0):
        function_calls.append((name, count))
        return count + 1

    result = example("  Alice  ", count=2)

    assert result == 3
    assert function_calls == [("  Alice  ", 2)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('Alice', count=2)"),
        call("example -> 3"),
    ]

# Generated at 2026-10-25 02:30:36.036002
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def repeat(value, count=1):
        """Repeat a string."""
        return value.strip() * count

    result = repeat(" hello ", count=2)

    assert result == "hellohello"
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat a string."
    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat -> hellohello"),
    ]

# Generated at 2026-10-25 02:30:38.631802
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:41.049947
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:43.462890
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:45.877305
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:48.291567
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:50.706777
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:53.121419
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:55.535821
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:30:57.951111
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:31:00.369047
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:31:02.780455
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:31:05.194654
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:31:07.608901
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:10.024705
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:12.440046
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:14.853820
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:17.268936
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:19.682577
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:22.096951
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:24.512563
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:26.928686
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:29.347691
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:31.765625
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:34.184403
# Unit test for function build_requests_session

# Generated at 2026-10-25 02:31:36.776407
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import MagicMock

    logger = MagicMock(spec=logging.Logger)
    logged = LoggedFunction(logger)

    # Case 1: positional and keyword arguments, non-None return value
    @logged
    def add(a, b=0):
        return a + b

    result = add(2, b=3)
    assert result == 5
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    second_call = logger.debug.call_args_list[1][0][0]
    assert first_call == "add('2', b='3')"
    assert second_call == "add -> 5"

    # Case 2: string arguments are quoted and stripped
    logger.reset_mock()

    @logged
    def greet(name):
        return f"Hello, {name}!"

    result = greet("  world ")
    assert result == "Hello,  world !"
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world')"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == "greet -> Hello,  world !"

    # Case 3: function returns None -> only entry logged, no result log
    logger.reset_mock()

    @logged
    def do_nothing():
        return None

    result = do_nothing()
    assert result is None
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0][0][0] == "do_nothing()"

    # Case 4: functools.wraps preserves function metadata
    @logged
    def documented():
        """Docstring."""
        return 1

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "Docstring."

    # Case 5: generator return value is logged as-is (not consumed)
    logger.reset_mock()

    @logged
    def gen():
        yield 1
        yield 2

    g = gen()
    assert hasattr(g, "__next__")
    assert logger.debug.call_args_list[1][0][0].startswith("gen -> <generator object")

# Generated at 2026-10-25 02:31:53.629360
# Unit test for function build_requests_session
def test_build_requests_session():
    retry_config = Retry(total=3)

    with module_0.build_requests_session(
        raise_for_status=True,
        retry=retry_config,
    ) as session:
        assert isinstance(session, Session)

        # Both protocols use the configured retry adapter.
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]

        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert http_adapter.max_retries is retry_config

        # The response hook calls raise_for_status.
        assert len(session.hooks["response"]) == 1

        response = Mock()
        session.hooks["response"][0](response)

        response.raise_for_status.assert_called_once_with()

# Generated at 2026-10-25 02:32:02.453500
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, count=1):
        """Example function."""
        received_arguments.append((value, count))
        return "completed"

    result = example("  input  ", count=2)

    assert result == "completed"
    assert received_arguments == [("  input  ", 2)]

    logger.debug.assert_has_calls(
        [
            call("example('input', count=2)"),
            call("example -> completed"),
        ]
    )
    assert logger.debug.call_count == 2

    # functools.wraps should preserve the decorated function's metadata.
    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."

# Generated at 2026-10-25 02:32:12.506774
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()

    def sample(value, increment=0):
        """Sample function."""
        return value + increment

    logged_sample = LoggedFunction(logger)(sample)

    result = logged_sample(2, increment=3)

    assert result == 5
    assert logged_sample.__name__ == "sample"
    assert logged_sample.__doc__ == "Sample function."
    logger.debug.assert_has_calls(
        [
            call("sample(2, increment=3)"),
            call("sample -> 5"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:32:29.600466
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration installs retries and raise_for_status hook.
    with module_0.build_requests_session() as session:
        assert len(session.hooks["response"]) == 1

        response = Response()
        response.status_code = 500
        response.url = "https://example.com"

        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

        assert isinstance(session.adapters["http://"].max_retries, Retry)
        assert isinstance(session.adapters["https://"].max_retries, Retry)

    # Integer retry configuration is used as the total retry count.
    with module_0.build_requests_session(retry=3) as session:
        assert session.adapters["http://"].max_retries.total == 3
        assert session.adapters["https://"].max_retries.total == 3

    # A supplied Retry instance is preserved.
    configured_retry = Retry(total=5)
    with module_0.build_requests_session(retry=configured_retry) as session:
        assert session.adapters["http://"].max_retries is configured_retry
        assert session.adapters["https://"].max_retries is configured_retry

    # Both optional features can be disabled.
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0

    # Unsupported truthy retry values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:32:32.137780
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:34.553002
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:36.983853
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:39.398451
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:41.814223
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:44.231296
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 02:32:47.109402
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import MagicMock

    logger = MagicMock(spec=logging.Logger)
    logged = LoggedFunction(logger)

    # Case 1: positional and keyword arguments, non-None return value
    @logged
    def add(a, b=0):
        return a + b

    result = add(2, b=3)
    assert result == 5
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    second_call = logger.debug.call_args_list[1][0][0]
    assert first_call == "add('2', b='3')"
    assert second_call == "add -> 5"

    # Case 2: string arguments are quoted and stripped
    logger.reset_mock()

    @logged
    def greet(name):
        return f"Hello, {name}!"

    result = greet("  world ")
    assert result == "Hello,  world !"
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world')"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == "greet -> Hello,  world !"

    # Case 3: function returns None -> only entry logged, no result log
    logger.reset_mock()

    @logged
    def do_nothing():
        return None

    result = do_nothing()
    assert result is None
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0][0][0] == "do_nothing()"

    # Case 4: functools.wraps preserves function metadata
    @logged
    def documented():
        """Docstring."""
        return 1

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "Docstring."

    # Case 5: generator return value is logged as-is (not consumed)
    logger.reset_mock()

    @logged
    def gen():
        yield 1
        yield 2

    g = gen()
    assert hasattr(g, "__next__")
    assert logger.debug.call_args_list[1][0][0].startswith("gen -> <generator object")

# Generated at 2026-10-25 02:32:55.813606
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()

    @LoggedFunction(logger)
    def example(value, multiplier=1):
        return value * multiplier

    result = example(3, multiplier=2)

    assert result == 6
    logger.debug.assert_has_calls(
        [
            call("example(3, multiplier=2)"),
            call("example -> 6"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:33:07.086747
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import Mock

    import pytest

    # Default configuration installs the status hook and retry adapters.
    session = module_0.build_requests_session()

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    assert isinstance(session.adapters["http://"].max_retries, Retry)
    assert isinstance(session.adapters["https://"].max_retries, Retry)

    # Status checking can be disabled.
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks["response"] == []

    # Integer retry counts are applied to both adapters.
    session = module_0.build_requests_session(retry=3)
    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)
    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry

    # Disabling retries leaves the Session's default adapters in place.
    session = module_0.build_requests_session(retry=False)
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0

    # Unsupported truthy retry values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:33:22.614708
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def multiply(value, factor=1):
        received_arguments.append((value, factor))
        return value * factor

    result = multiply(3, factor=4)

    assert result == 12
    assert received_arguments == [(3, 4)]
    assert multiply.__name__ == "multiply"
    assert logger.debug.call_args_list == [
        call("multiply(3, factor=4)"),
        call("multiply -> 12"),
    ]

    # A None return value should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def record(value):
        received_arguments.append(value)

    result = record(" value ")

    assert result is None
    assert received_arguments[-1] == " value "
    logger.debug.assert_called_once_with("record('value')")

# Generated at 2026-10-25 02:33:32.166349
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def example(value, count=1):
        invocations.append((value, count))
        return "completed"

    result = example("  hello  ", count=2)

    assert result == "completed"
    assert invocations == [("  hello  ", 2)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('hello', count=2)"),
        call("example -> completed"),
    ]

# Generated at 2026-10-25 02:33:43.738764
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1
    assert isinstance(session.adapters["http://"], HTTPAdapter)
    assert isinstance(session.adapters["https://"], HTTPAdapter)
    assert isinstance(session.adapters["http://"].max_retries, Retry)

    # Verify the response hook calls raise_for_status()
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()
    session.close()

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3
    session.close()

    # Explicit Retry instance
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)
    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry
    session.close()

    # Disabled status hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0
    session.close()

    # Invalid retry value
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:33:52.660696
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received = {}

    def sample_function(value, count=1):
        received["arguments"] = (value, count)
        return value * count

    decorated = LoggedFunction(logger)(sample_function)

    result = decorated("  test  ", count=2)

    assert result == "  test    test  "
    assert received["arguments"] == ("  test  ", 2)
    assert decorated.__name__ == "sample_function"

    assert logger.debug.call_args_list == [
        call("sample_function('test', count=2)"),
        call("sample_function ->   test    test  "),
    ]

# Generated at 2026-10-25 02:33:59.200631
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_calls = []

    @LoggedFunction(logger)
    def add(a, b=0):
        function_calls.append((a, b))
        return a + b

    result = add(2, b=3)

    assert result == 5
    assert function_calls == [(2, 3)]
    assert add.__name__ == "add"
    assert logger.debug.call_args_list == [
        call("add(2, b=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 02:34:07.090261
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, increment=0):
        return len(value) + increment

    result = example(" test ", increment=2)

    assert result == 8
    assert example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('test', increment=2)"),
        call("example -> 8"),
    ]

# Generated at 2026-10-25 02:34:17.224140
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def sample_function(value, count=0):
        received_arguments.append((value, count))
        return count + 1

    decorated_function = LoggedFunction(logger)(sample_function)

    result = decorated_function("  example  ", count=2)

    assert result == 3
    assert received_arguments == [("  example  ", 2)]
    assert decorated_function.__name__ == "sample_function"
    assert logger.debug.call_args_list == [
        call("sample_function('example', count=2)"),
        call("sample_function -> 3"),
    ]

# Generated at 2026-10-25 02:34:27.261514
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_args = []

    def example(value, increment=0):
        received_args.append((value, increment))
        return 10 + increment

    decorated = LoggedFunction(logger)(example)

    result = decorated(" hello ", increment=2)

    assert result == 12
    assert received_args == [(" hello ", 2)]
    assert decorated.__name__ == "example"
    logger.debug.assert_has_calls(
        [
            call("example('hello', increment=2)"),
            call("example -> 12"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:34:41.901484
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def example(value, count=0):
        received_arguments.append((value, count))
        return "done"

    decorated = LoggedFunction(logger)(example)

    result = decorated("  hello  ", count=2)

    assert result == "done"
    assert received_arguments == [("  hello  ", 2)]
    assert decorated.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('hello', count=2)"),
        call("example -> done"),
    ]

# Generated at 2026-10-25 02:35:05.249788
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    # Verify that the response hook invokes raise_for_status().
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Both protocols should use the configured retry adapter.
    http_adapter = session.adapters["http://"]
    https_adapter = session.adapters["https://"]

    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)


def test_build_requests_session_without_raise_for_status_hook():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0


def test_build_requests_session_with_retry_count():
    session = module_0.build_requests_session(retry=3)

    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=5, backoff_factor=0.5)

    session = module_0.build_requests_session(retry=retry)

    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry


@pytest.mark.parametrize("invalid_retry", ["invalid", object(), [1, 2]])
def test_build_requests_session_rejects_invalid_retry(invalid_retry):
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry=invalid_retry)

# Generated at 2026-10-25 02:35:16.796652
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()
    try:
        assert isinstance(session, Session)

        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert http_adapter is https_adapter
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(http_adapter.max_retries, Retry)
    finally:
        session.close()

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    try:
        assert session.hooks["response"] == []
        assert session.get_adapter("http://example.com").max_retries.total == 0
        assert session.get_adapter("https://example.com").max_retries.total == 0
    finally:
        session.close()

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    try:
        assert session.get_adapter("https://example.com").max_retries.total == 3
    finally:
        session.close()

    # Explicit Retry instance
    retry_config = Retry(total=5, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_config)
    try:
        adapter = session.get_adapter("https://example.com")
        assert adapter.max_retries is retry_config
    finally:
        session.close()

    # Invalid retry configuration
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:35:26.244763
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def example(value, count=1):
        received_arguments.append((value, count))
        return 42

    logged_example = LoggedFunction(logger)(example)

    result = logged_example("  hello  ", count=2)

    assert result == 42
    assert received_arguments == [("  hello  ", 2)]
    assert logged_example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('hello', count=2)"),
        call("example -> 42"),
    ]

# Generated at 2026-10-25 02:35:38.118257
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1
    assert session.get_adapter("http://").max_retries.total == Retry().total
    assert session.get_adapter("https://").max_retries.total == Retry().total

    # Verify the response hook calls raise_for_status
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Integer retry count
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    # Unsupported retry value
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:35:40.677137
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import MagicMock

    logger = MagicMock(spec=logging.Logger)
    logged = LoggedFunction(logger)

    # Case 1: positional and keyword arguments, non-None return value
    @logged
    def add(a, b=0):
        return a + b

    result = add(2, b=3)
    assert result == 5
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    second_call = logger.debug.call_args_list[1][0][0]
    assert first_call == "add('2', b='3')"
    assert second_call == "add -> 5"

    # Case 2: string arguments are quoted and stripped
    logger.reset_mock()

    @logged
    def greet(name):
        return f"Hello, {name}!"

    result = greet("  world ")
    assert result == "Hello,  world !"
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world')"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == "greet -> Hello,  world !"

    # Case 3: function returns None -> only entry logged, no result log
    logger.reset_mock()

    @logged
    def do_nothing():
        return None

    result = do_nothing()
    assert result is None
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0][0][0] == "do_nothing()"

    # Case 4: functools.wraps preserves function metadata
    @logged
    def documented():
        """Docstring."""
        return 1

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "Docstring."

    # Case 5: generator return value is logged as-is (not consumed)
    logger.reset_mock()

    @logged
    def gen():
        yield 1
        yield 2

    g = gen()
    assert hasattr(g, "__next__")
    assert logger.debug.call_args_list[1][0][0].startswith("gen -> <generator object")

# Generated at 2026-10-25 02:35:57.619266
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration enables status checking and retries.
    session = module_0.build_requests_session()
    try:
        assert isinstance(session, Session)

        response = Mock()
        assert len(session.hooks["response"]) == 1
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == Retry().total
    finally:
        session.close()

    # Both features can be disabled.
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    try:
        assert session.hooks["response"] == []
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0
    finally:
        session.close()

    # An integer configures the total retry count.
    session = module_0.build_requests_session(retry=5)
    try:
        assert session.adapters["http://"].max_retries.total == 5
        assert session.adapters["https://"].max_retries.total == 5
    finally:
        session.close()

    # A supplied Retry instance is used by both adapters.
    retry = Retry(total=3)
    session = module_0.build_requests_session(retry=retry)
    try:
        assert session.adapters["http://"].max_retries is retry
        assert session.adapters["https://"].max_retries is retry
    finally:
        session.close()

    # Truthy unsupported retry values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:36:09.148489
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1
    assert isinstance(session.get_adapter("http://").max_retries, Retry)
    assert isinstance(session.get_adapter("https://").max_retries, Retry)

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()
    session.close()

    # Disable the response hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    # Session's standard adapters use zero retries.
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0
    session.close()

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3
    session.close()

    # Configure retries using an existing Retry instance
    retry_config = Retry(total=5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config
    session.close()

    # Reject unsupported retry values
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:36:27.259772
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration enables status checking and retries.
    with module_0.build_requests_session() as session:
        assert len(session.hooks["response"]) == 1

        response = Response()
        response.status_code = 204
        session.hooks["response"][0](response)

        response.status_code = 500
        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)

        http_adapter = session.get_adapter("http://")
        https_adapter = session.get_adapter("https://")

        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total

    # Hooks and configured retries can be disabled.
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0

    # An integer configures the total retry count.
    with module_0.build_requests_session(retry=3) as session:
        assert session.get_adapter("http://").max_retries.total == 3
        assert session.get_adapter("https://").max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry_config = Retry(total=7)
    with module_0.build_requests_session(retry=retry_config) as session:
        assert session.get_adapter("http://").max_retries is retry_config
        assert session.get_adapter("https://").max_retries is retry_config

    # Unsupported truthy values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 02:36:37.704969
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(number, text, enabled=False):
        received_arguments.append((number, text, enabled))
        return "completed"

    result = example(42, "  hello  ", enabled=True)

    assert result == "completed"
    assert received_arguments == [(42, "  hello  ", True)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example(42, 'hello', enabled=True)"),
        call("example -> completed"),
    ]

# Generated at 2026-10-25 02:36:50.196748
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def repeat(value, count=1):
        """Repeat a stripped string."""
        return value.strip() * count

    result = repeat(" hello ", count=2)

    assert result == "hellohello"
    assert repeat.__name__ == "repeat"
    assert repeat.__doc__ == "Repeat a stripped string."
    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat -> hellohello"),
    ]

# Generated at 2026-10-25 02:36:59.527811
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    wrapped_function = Mock(return_value="success")

    @LoggedFunction(logger)
    def example(name, count=1):
        return wrapped_function(name, count=count)

    result = example("Alice", count=2)

    assert result == "success"
    wrapped_function.assert_called_once_with("Alice", count=2)
    assert logger.debug.call_args_list == [
        call("example('Alice', count=2)"),
        call("example -> success"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert example.__name__ == "example"

# Generated at 2026-10-25 02:37:09.153629
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_call = Mock(return_value={"success": True})

    @LoggedFunction(logger)
    def example(name, count=0):
        return function_call(name, count=count)

    result = example(" Alice ", count=2)

    assert result == {"success": True}
    function_call.assert_called_once_with(" Alice ", count=2)
    assert logger.debug.call_args_list == [
        call("example('Alice', count=2)"),
        call("example -> {'success': True}"),
    ]

    # functools.wraps should preserve the wrapped function's metadata.
    assert example.__name__ == "example"

# Generated at 2026-10-25 02:37:18.679809
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def sample(value, count=1):
        """Sample function."""
        received_arguments.append((value, count))
        return "completed"

    decorated = LoggedFunction(logger)(sample)

    result = decorated("  value  ", count=2)

    assert result == "completed"
    assert received_arguments == [("  value  ", 2)]

    # functools.wraps preserves the decorated function's metadata.
    assert decorated.__name__ == "sample"
    assert decorated.__doc__ == "Sample function."

    assert logger.debug.call_args_list == [
        call("sample('value', count=2)"),
        call("sample -> completed"),
    ]

# Generated at 2026-10-25 02:37:25.874396
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        """Add increment to value."""
        return value + increment

    result = add(3, increment=4)

    assert result == 7
    assert add.__name__ == "add"
    assert add.__doc__ == "Add increment to value."
    assert logger.debug.call_args_list == [
        call("add(3, increment=4)"),
        call("add -> 7"),
    ]

# Generated at 2026-10-25 02:37:35.469566
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, count=0):
        received_arguments.append((value, count))
        return count + 1

    result = example("  hello  ", count=2)

    assert result == 3
    assert received_arguments == [("  hello  ", 2)]
    assert example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('hello', count=2)"),
        call("example -> 3"),
    ]

# Generated at 2026-10-25 02:37:45.392641
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def combine(value, suffix=""):
        """Test function."""
        return f"{value.strip()}-{suffix.strip()}"

    result = combine("  alpha  ", suffix=" beta ")

    assert result == "alpha-beta"
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Test function."

    assert logger.debug.call_count == 2
    logger.debug.assert_has_calls(
        [
            call("combine('alpha', suffix='beta')"),
            call("combine -> alpha-beta"),
        ]
    )

# Generated at 2026-10-25 02:37:53.929749
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def multiply(value, multiplier=1):
        return value * multiplier

    result = multiply(3, multiplier=2)

    assert result == 6
    assert logger.debug.call_args_list == [
        call("multiply(3, multiplier=2)"),
        call("multiply -> 6"),
    ]

    # Verify functools.wraps preserved the decorated function's metadata.
    assert multiply.__name__ == "multiply"

# Generated at 2026-10-25 02:38:04.460310
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

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

    # A None return value should not produce a result log entry.
    logger.reset_mock()

    @LoggedFunction(logger)
    def do_nothing(value):
        return None

    assert do_nothing(42) is None
    logger.debug.assert_called_once_with("do_nothing(42)")

# Generated at 2026-10-25 02:38:13.409102
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def example(value, count=0):
        return f"{value}:{count}"

    decorated = LoggedFunction(logger)(example)

    result = decorated("  hello  ", count=2)

    assert result == "  hello  :2"
    assert decorated.__wrapped__ is example
    logger.debug.assert_has_calls(
        [
            call("example('hello', count=2)"),
            call("example ->   hello  :2"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:38:23.392259
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def sample(number, text, enabled=False):
        assert number == 2
        assert text == " value "
        assert enabled is True
        return 42

    decorated = LoggedFunction(logger)(sample)

    result = decorated(2, " value ", enabled=True)

    assert result == 42
    assert decorated.__name__ == "sample"
    logger.debug.assert_has_calls(
        [
            call("sample(2, 'value', enabled=True)"),
            call("sample -> 42"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 02:38:33.347094
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def sample_function(value, count=1):
        """Sample function."""
        received_arguments.append((value, count))
        return count * 2

    decorated = LoggedFunction(logger)(sample_function)

    result = decorated("  example  ", count=3)

    assert result == 6
    assert received_arguments == [("  example  ", 3)]
    assert decorated.__name__ == "sample_function"
    assert decorated.__doc__ == "Sample function."

    assert logger.debug.call_args_list == [
        call("sample_function('example', count=3)"),
        call("sample_function -> 6"),
    ]

# Generated at 2026-10-25 02:38:43.769695
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    def sample(value, increment=0):
        """Sample function."""
        return len(value) + increment

    logged_sample = LoggedFunction(logger)(sample)

    result = logged_sample(" x ", increment=2)

    assert result == 5
    assert logged_sample.__name__ == "sample"
    assert logged_sample.__doc__ == "Sample function."
    assert logger.debug.call_args_list == [
        call("sample('x', increment=2)"),
        call("sample -> 5"),
    ]