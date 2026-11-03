

# Generated at 2026-11-01 19:57:16.525596
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import MagicMock

    # Default behaviour: raise_for_status hook installed, retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # The hook should call raise_for_status on the response
    mock_response = MagicMock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # retry=True (default) -> adapters mounted with a default Retry config
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)

    # raise_for_status=False -> no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False -> adapters use defaults (no retries)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == 0

    # retry as int -> Retry configured with given total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance -> used as-is
    custom_retry = Retry(total=7, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # invalid retry type -> ValueError
    try:
        module_0.build_requests_session(retry="invalid")
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError not raised for invalid retry argument")

    # retry=0 (falsy int) -> no retries configured
    session = module_0.build_requests_session(retry=0)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == 0

# Generated at 2026-11-01 19:58:24.005194
# Unit test for function format_arg
def test_format_arg():
    # Plain string is wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"

    # String with surrounding whitespace is stripped before quoting
    assert module_0.format_arg("  hello world  ") == "'hello world'"

    # Empty string becomes empty quoted string
    assert module_0.format_arg("") == "''"

    # Whitespace-only string strips to empty quoted string
    assert module_0.format_arg("   ") == "''"

    # String containing quotes is preserved as-is inside quotes
    assert module_0.format_arg("it's") == "'it's'"

    # Integer is converted via str()
    assert module_0.format_arg(42) == "42"

    # Negative integer
    assert module_0.format_arg(-7) == "-7"

    # Float
    assert module_0.format_arg(3.14) == "3.14"

    # Boolean
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(False) == "False"

    # None
    assert module_0.format_arg(None) == "None"

    # List
    assert module_0.format_arg([1, "two", 3.0]) == "[1, 'two', 3.0]"

    # Tuple
    assert module_0.format_arg((1, 2)) == "(1, 2)"

    # Dict
    assert module_0.format_arg({"a": 1}) == "{'a': 1}"

# Generated at 2026-11-01 19:59:13.197344
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == Retry().total

    # raise_for_status=False
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert "response" not in session.hooks or session.hooks.get("response") is None or len(session.hooks.get("response", [])) == 0

    # retry=False: no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    assert isinstance(session, Session)
    default_adapter = Session().get_adapter("https://example.com")
    assert session.get_adapter("https://example.com").max_retries.total == default_adapter.max_retries.total or not isinstance(
        session.get_adapter("https://example.com"), HTTPAdapter
    )

    # retry as integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=10, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries is custom_retry
    assert adapter.max_retries.total == 10

    # invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="invalid")
        assert False, "Expected ValueError for invalid retry type"
    except ValueError as e:
        assert str(e) == "retry should be a bool, int or Retry instance."

    # hooks raise_for_status behavior
    session = module_0.build_requests_session(raise_for_status=True)
    class FakeResponse:
        def raise_for_status(self):
            raise AssertionError("raise_for_status called")
    hook = session.hooks["response"][0]
    # hook is callable with a response
    assert callable(hook)

# Generated at 2026-11-01 19:59:55.714660
# Unit test for function format_arg
def test_format_arg():
    # Strings are wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"

    # Leading/trailing whitespace on strings is stripped
    assert module_0.format_arg("  padded  ") == "'padded'"

    # Internal whitespace within strings is preserved
    assert module_0.format_arg("hello world") == "'hello world'"

    # Empty string
    assert module_0.format_arg("") == "''"

    # Non-string values fall back to str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(-7) == "-7"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(False) == "False"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"
    assert module_0.format_arg({"key": "value"}) == "{'key': 'value'}"
    assert module_0.format_arg((1, 2)) == "(1, 2)"

    # Check uses type() == str, so str subclasses are only passed through str()
    class FakeString(str):
        pass

    assert module_0.format_arg(FakeString("hi")) == "hi"
# nonce:6fabcc9a

# Generated at 2026-11-01 20:02:36.527021
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Test that the LoggedFunction constructor stores the logger."""
    import logging

    # Test with a real logger instance
    logger = logging.getLogger("test_logger")
    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

    # Test with a mock logger
    mock_logger = Mock()
    logged_function = LoggedFunction(mock_logger)
    assert logged_function.logger is mock_logger

# Generated at 2026-11-01 20:03:02.027260
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test basic logging of arguments and return value
    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b, offset=0):
        return a + b + offset

    # functools.wraps preserves the function metadata
    assert add.__name__ == "add"

    result = add(1, 2, offset=3)
    assert result == 6

    # Two debug calls: one for arguments before the call, one for the result
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[0][0][0] == "add(1, 2, offset=3)"
    assert logger.debug.call_args_list[1][0][0] == "add -> 6"

    # String arguments are quoted by format_arg
    logger_str = Mock()

    @LoggedFunction(logger_str)
    def greet(name):
        return f"Hello, {name}!"

    assert greet("World") == "Hello, World!"
    assert logger_str.debug.call_args_list[0][0][0] == "greet('World')"
    assert logger_str.debug.call_args_list[1][0][0] == "greet -> Hello, World!"

    # Functions returning None should not log a result line
    logger_none = Mock()

    @LoggedFunction(logger_none)
    def do_nothing():
        pass

    assert do_nothing() is None
    assert logger_none.debug.call_count == 1

# Generated at 2026-11-01 20:03:42.269145
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    from unittest.mock import MagicMock, patch

    # Test default behavior: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    # HTTP/HTTPS adapters should have retries configured
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter.max_retries is not None
    assert isinstance(http_adapter.max_retries, Retry)
    assert https_adapter.max_retries is http_adapter.max_retries or isinstance(
        https_adapter.max_retries, Retry
    )

    # Test raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert "response" not in session.hooks or not session.hooks.get("response")

    # Test retry=False: no retry adapter mounted (default adapters)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries.total == 0

    # Test retry=True: default Retry configuration
    session = module_0.build_requests_session(retry=True)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)

    # Test retry as integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # Test retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Test invalid retry type raises ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="invalid")

    # Test that raise_for_status hook actually calls raise_for_status
    session = module_0.build_requests_session(raise_for_status=True)
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    for hook in session.hooks["response"]:
        hook(mock_response)
    mock_response.raise_for_status.assert_called_once()

# Generated at 2026-11-01 20:04:32.076723
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    # Test with positional string args - strings get stripped and quoted
    logger = Mock()
    lf = LoggedFunction(logger)

    def add(a, b):
        return a + b

    wrapped = lf(add)

    assert wrapped(1, 2) == 3
    logger.debug.assert_any_call("add(1, 2)")
    logger.debug.assert_any_call("add -> 3")

    # Test with keyword arguments
    logger.reset_mock()

    def greet(name, greeting="hello"):
        return f"{greeting} {name}"

    wrapped_greet = lf(greet)
    result = wrapped_greet("bob ", greeting="hi")
    assert result == "hi bob"
    logger.debug.assert_any_call("greet('bob', hi='hi')")

# Generated at 2026-11-01 20:04:50.369802
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock

    logger = MagicMock()

    @LoggedFunction(logger)
    def add(a, b, c=3):
        return a + b + c

    result = add(1, 2)
    assert result == 6

    # Check debug was called twice: once for input args, once for result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2)")
    logger.debug.assert_any_call("add -> 6")

    # Test with keyword arguments
    logger.reset_mock()
    result = add(1, b=2, c=4)
    assert result == 7
    logger.debug.assert_any_call("add(1, b=2, c=4)")
    logger.debug.assert_any_call("add -> 7")

    # Test with string arguments (should be quoted and stripped)
    logger.reset_mock()

    @LoggedFunction(logger)
    def greet(name):
        return f"Hello, {name}"

    greet("  World  ")
    logger.debug.assert_any_call("greet('World')")

    # Test with None return value (result should not be logged)
    logger.reset_mock()

    @LoggedFunction(logger)
    def no_return(x):
        pass

    result = no_return(5)
    assert result is None
    assert logger.debug.call_count == 1
    logger.debug.assert_called_once_with("no_return(5)")

    # Test that functools.wraps preserves metadata
    assert add.__name__ == "add"
    assert greet.__name__ == "greet"

# Generated at 2026-11-01 20:05:08.593654
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    decorator = LoggedFunction(logger)

    # Decorated function with positional args and a return value
    @decorator
    def add(a, b):
        """Add two numbers."""
        return a + b

    # functools.wraps preserves metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

    result = add(1, 2)
    assert result == 3
    logger.debug.assert_any_call("add(1, 2)")
    logger.debug.assert_any_call("add -> 3")
    assert logger.debug.call_count == 2

    # String args are quoted and stripped; kwargs are logged too
    logger.reset_mock()

    @decorator
    def greet(name, punctuation="!"):
        return f"Hello {name}{punctuation}"

    result = greet("  world  ", punctuation="?")
    assert result == "Hello   world  ?"
    logger.debug.assert_any_call("greet('world', punctuation='?')")
    logger.debug.assert_any_call("greet -> Hello   world  ?")
    assert logger.debug.call_count == 2

    # None return values are not logged
    logger.reset_mock()

    @decorator
    def nothing():
        pass

    assert nothing() is None
    logger.debug.assert_called_once_with("nothing()")

    # Non-string args are formatted with str()
    logger.reset_mock()

    @decorator
    def mixed(a, b, c):
        return None

    mixed([1, 2], {"k": 1}, 3.5)
    logger.debug.assert_called_once_with("mixed([1, 2], {'k': 1}, 3.5)")

# Generated at 2026-11-01 20:05:31.633196
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import unittest
from unittest.mock import MagicMock


class TestLoggedFunctionCall(unittest.TestCase):
    def test_logged_function_logs_args_and_result(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def add(a, b, c=0):
            return a + b + c

        result = add(1, 2, c=3)
        self.assertEqual(result, 6)
        self.assertEqual(logger.debug.call_count, 2)
        logger.debug.assert_any_call("add(1, 2, c=3)")
        logger.debug.assert_any_call("add -> 6")

    def test_logged_function_string_args_are_quoted(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def greet(name, greeting="hello"):
            return f"{greeting} {name}"

        result = greet("world")
        self.assertEqual(result, "hello world")
        logger.debug.assert_any_call("greet('world', greeting='hello')")
        logger.debug.assert_any_call("greet -> hello world")

    def test_logged_function_none_result_not_logged(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def do_nothing():
            return None

        result = do_nothing()
        self.assertIsNone(result)
        logger.debug.assert_called_once_with("do_nothing()")

    def test_logged_function_preserves_metadata(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def my_func(x):
            """Docstring here."""
            return x

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "Docstring here.")
        self.assertEqual(my_func(42), 42)

    def test_logged_function_multiple_string_kwargs(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def combine(a, b):
            return a + b

        result = combine(a="x", b="y")
        self.assertEqual(result, "xy")
        logger.debug.assert_any_call("combine(a='x', b='y')")

    def test_logged_function_exception_propagates(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def failing():
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            failing()
        # Only the entry log should have been made
        logger.debug.assert_called_once_with("failing()")

    def test_logged_function_no_args(self):
        logger = MagicMock()
        decorator = LoggedFunction(logger)

        @decorator
        def noop():
            return 1

        self.assertEqual(noop(), 1)
        logger.debug.assert_any_call("noop()")
        logger.debug.assert_any_call("noop -> 1")

# Generated at 2026-11-01 20:06:01.229891
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest import mock

    # Default call returns a Session
    session = module_0.build_requests_session()
    assert isinstance(session, Session)

    # raise_for_status=True installs a response hook that calls raise_for_status
    session = module_0.build_requests_session(raise_for_status=True)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    mock_response = mock.Mock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # raise_for_status=False leaves hooks empty
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}

    # retry=True mounts an adapter with a default Retry policy
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(http_adapter.max_retries, Retry)
    assert http_adapter.max_retries.total == Retry().total
    assert http_adapter is https_adapter

    # retry=<int> sets the total retry count
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry=<Retry instance> reuses the provided instance
    retry_policy = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_policy)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is retry_policy

    # retry=False keeps the default non-retrying adapter
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # Invalid retry argument raises ValueError
    try:
        module_0.build_requests_session(retry="invalid")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid retry argument")

# Generated at 2026-11-01 20:06:21.708511
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import unittest
from unittest.mock import MagicMock, call

# Assuming the module containing LoggedFunction is named 'mymodule'
# from mymodule import LoggedFunction


class TestLoggedFunctionCall(unittest.TestCase):
    def setUp(self):
        self.mock_logger = MagicMock()

    def test_logs_function_name_and_args(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(a, b):
            return a + b

        my_func(1, 2)

        self.mock_logger.debug.assert_any_call("my_func(1, 2)")

    def test_logs_string_args_with_quotes(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(name):
            return name

        my_func("  hello  ")

        self.mock_logger.debug.assert_any_call("my_func('hello')")

    def test_logs_kwargs(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(a, b=0):
            return a + b

        my_func(1, b=2)

        self.mock_logger.debug.assert_any_call("my_func(1, b=2)")

    def test_logs_string_kwargs_with_quotes(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(name=""):
            return name

        my_func(name="world")

        self.mock_logger.debug.assert_any_call("my_func(name='world')")

    def test_logs_result_when_not_none(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func():
            return 42

        my_func()

        self.mock_logger.debug.assert_any_call("my_func -> 42")

    def test_does_not_log_result_when_none(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func():
            return None

        my_func()

        # Only the input log should have happened (1 call)
        self.assertEqual(self.mock_logger.debug.call_count, 1)
        self.mock_logger.debug.assert_called_once_with("my_func()")

    def test_returns_function_result(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(a, b):
            return a + b

        result = my_func(2, 3)
        self.assertEqual(result, 5)

    def test_preserves_function_metadata(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func():
            """Docstring here."""

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "Docstring here.")

    def test_mixed_args_and_kwargs_logging(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(a, b, c=None):
            return a

        my_func(1, "two", c=3.5)

        self.mock_logger.debug.assert_any_call("my_func(1, 'two', c=3.5)")

    def test_exception_propagates_and_result_not_logged(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func():
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            my_func()

        # Only the input log should have happened
        self.assertEqual(self.mock_logger.debug.call_count, 1)

    def test_no_result_log_for_falsy_but_not_none(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func():
            return 0

        my_func()

        # 0 is not None, so it should be logged
        self.mock_logger.debug.assert_any_call("my_func -> 0")

    def test_debug_call_order(self):
        logged = LoggedFunction(self.mock_logger)

        @logged
        def my_func(x):
            return x * 2

        my_func(5)

        self.mock_logger.debug.assert_has_calls(
            [call("my_func(5)"), call("my_func -> 10")]
        )


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:06:46.809664
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default behaviour: raise_for_status hook installed, retries enabled
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # Retry adapter should be mounted on both http and https
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(http_adapter.max_retries, Retry)
    assert http_adapter is https_adapter


def test_build_requests_session_no_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert session.hooks == {}
    # Retries still enabled by default
    assert isinstance(session.get_adapter("http://example.com").max_retries, Retry)


def test_build_requests_session_no_retry():
    session = module_0.build_requests_session(retry=False)
    assert isinstance(session, Session)
    # Default adapters have max_retries == 0 (no Retry object configured)
    assert session.get_adapter("http://example.com").max_retries == 0
    assert session.get_adapter("https://example.com").max_retries == 0


def test_build_requests_session_retry_int():
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5


def test_build_requests_session_retry_zero():
    # retry=0 is falsy, so no adapter should be mounted
    session = module_0.build_requests_session(retry=0)
    assert session.get_adapter("http://example.com").max_retries == 0


def test_build_requests_session_retry_instance():
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry


def test_build_requests_session_invalid_retry_type():
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="not-a-valid-retry")


def test_build_requests_session_hook_raises_for_status():
    session = module_0.build_requests_session()

    class FakeResponse:
        status_code = 500

        def raise_for_status(self):
            raise Exception("raised")

    response = FakeResponse()
    with pytest.raises(Exception):
        for hook in session.hooks["response"]:
            hook(response)