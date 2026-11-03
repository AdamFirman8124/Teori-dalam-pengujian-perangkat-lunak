

# Generated at 2026-11-01 21:27:15.003777
# Unit test for function build_requests_session
def test_build_requests_session():import unittest
from unittest.mock import patch

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from mymodule import build_requests_session  # adjust import path as needed


class TestBuildRequestsSession(unittest.TestCase):
    def test_default(self):
        session = module_0.build_requests_session()
        self.assertIsInstance(session, Session)
        # raise_for_status hook installed by default
        self.assertIn("response", session.hooks)
        self.assertEqual(len(session.hooks["response"]), 1)
        # default retry adapter mounted
        adapter = session.get_adapter("http://example.com")
        self.assertIsInstance(adapter, HTTPAdapter)
        self.assertIsInstance(adapter.max_retries, Retry)
        self.assertEqual(adapter.max_retries.total, 10)  # Retry default total

    def test_raise_for_status_false(self):
        session = module_0.build_requests_session(raise_for_status=False)
        self.assertEqual(session.hooks, {})

    def test_raise_for_status_hook_raises(self):
        session = module_0.build_requests_session()
        from requests import Response

        response = Response()
        response.status_code = 500
        with self.assertRaises(Exception):
            for hook in session.hooks["response"]:
                hook(response)

    def test_retry_false(self):
        session = module_0.build_requests_session(retry=False)
        adapter = session.get_adapter("https://example.com")
        self.assertEqual(adapter.max_retries.total, 0)

    def test_retry_int(self):
        session = module_0.build_requests_session(retry=5)
        adapter = session.get_adapter("https://example.com")
        self.assertIsInstance(adapter.max_retries, Retry)
        self.assertEqual(adapter.max_retries.total, 5)

    def test_retry_instance(self):
        retry = Retry(total=3, backoff_factor=0.5)
        session = module_0.build_requests_session(retry=retry)
        adapter = session.get_adapter("https://example.com")
        self.assertIs(adapter.max_retries, retry)
        self.assertEqual(adapter.max_retries.total, 3)
        self.assertEqual(adapter.max_retries.backoff_factor, 0.5)

    def test_http_and_https_mounted(self):
        session = module_0.build_requests_session()
        self.assertIsInstance(session.get_adapter("http://example.com"), HTTPAdapter)
        self.assertIsInstance(session.get_adapter("https://example.com"), HTTPAdapter)

    def test_invalid_retry_raises_value_error(self):
        with self.assertRaises(ValueError):
            module_0.build_requests_session(retry="invalid")

    def test_hooks_raise_for_status_callable(self):
        session = module_0.build_requests_session(raise_for_status=True)
        hook = session.hooks["response"][0]
        from requests import Response

        response = Response()
        response.status_code = 200
        # Should not raise for a successful response
        hook(response)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 21:27:52.992977
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Test LoggedFunction constructor stores the provided logger."""
    import logging
    from unittest.mock import MagicMock

    # Test with a standard logging.Logger instance
    logger = logging.getLogger("test_logger")
    logged_function = LoggedFunction(logger)
    assert logged_function.logger is logger

    # Test with a mock logger object
    mock_logger = MagicMock()
    logged_function_with_mock = LoggedFunction(mock_logger)
    assert logged_function_with_mock.logger is mock_logger

    # Ensure different instances hold their own logger reference
    another_logged_function = LoggedFunction(logging.getLogger("another_logger"))
    assert another_logged_function.logger is not logged_function.logger

# Generated at 2026-11-01 21:28:21.870125
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Test LoggedFunction constructor stores the logger."""
    import logging

    # Test with a standard logger instance
    logger = logging.getLogger("test_logger")
    logged_func = LoggedFunction(logger)
    assert logged_func.logger is logger

    # Test with a mock logger
    mock_logger = object()
    logged_func2 = LoggedFunction(mock_logger)
    assert logged_func2.logger is mock_logger

    # Test with None
    logged_func3 = LoggedFunction(None)
    assert logged_func3.logger is None

    # Test that constructor requires a logger argument
    try:
        LoggedFunction()  # type: ignore
        assert False, "Expected TypeError for missing logger argument"
    except TypeError:
        pass

# Generated at 2026-11-01 21:28:55.354566
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Test that the LoggedFunction constructor stores the logger."""
    import logging
    from unittest.mock import MagicMock

    # Test with a MagicMock logger
    mock_logger = MagicMock()
    logged = LoggedFunction(mock_logger)
    assert logged.logger is mock_logger

    # Test with a standard logger instance
    logger = logging.getLogger("test_logger")
    logged2 = LoggedFunction(logger)
    assert logged2.logger is logger
    assert isinstance(logged2, LoggedFunction)

# Generated at 2026-11-01 21:29:30.738999
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    logger = Mock()

    @LoggedFunction(logger)
    def add(a, b, *, suffix=""):
        return a + b

    # functools.wraps should preserve metadata
    assert add.__name__ == "add"

    # Call the decorated function and check result
    result = add(1, 2, suffix="x")
    assert result == 3

    # Check the call arguments were logged (strings quoted, kwargs included)
    expected_call_log = "add(1, 2, suffix='x')"
    logger.debug.assert_any_call(expected_call_log)

    # Check the result was logged
    logger.debug.assert_any_call("add -> 3")

    # Exactly two debug calls: args log and result log
    assert logger.debug.call_count == 2


def test_LoggedFunction___call__string_args():
    from unittest.mock import Mock

    logger = Mock()

    @LoggedFunction(logger)
    def greet(name):
        return f"Hello {name}"

    result = greet(" Alice ")
    assert result == "Hello  Alice "

    # Strings are stripped and wrapped in single quotes
    logger.debug.assert_any_call("greet('Alice')")
    logger.debug.assert_any_call("greet -> Hello  Alice ")


def test_LoggedFunction___call__none_result_not_logged():
    from unittest.mock import Mock

    logger = Mock()

    @LoggedFunction(logger)
    def returns_none():
        return None

    result = returns_none()
    assert result is None

    # Only the argument log should occur; None results are not logged
    logger.debug.assert_called_once_with("returns_none()")


def test_LoggedFunction___call__various_types():
    from unittest.mock import Mock

    logger = Mock()

    @LoggedFunction(logger)
    def mixed(a, b, c):
        return a

    mixed("s", 3.5, None)
    logger.debug.assert_any_call("mixed('s', 3.5, None)")

# Generated at 2026-11-01 21:29:58.845629
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # nonce:9116832d
    logger = MagicMock()

    @LoggedFunction(logger)
    def add(a, b, c=0):
        """Add numbers."""
        return a + b + c

    # functools.wraps preserves function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

    # Call the decorated function with positional and keyword args
    result = add(1, 2, c=3)
    assert result == 6

    # Arguments are logged before the call (ints are not quoted)
    logger.debug.assert_any_call("add(1, 2, c=3)")
    # Non-None return value is logged after the call
    logger.debug.assert_any_call("add -> 6")
    assert logger.debug.call_count == 2

    # String args are stripped and wrapped in single quotes
    logger2 = MagicMock()

    @LoggedFunction(logger2)
    def greet(name):
        return None

    assert greet(" world ") is None
    # None result must not be logged
    logger2.debug.assert_called_once_with("greet('world')")

    # Non-string args use str()
    logger3 = MagicMock()

    @LoggedFunction(logger3)
    def process(items):
        return len(items)

    assert process([1, 2]) == 2
    logger3.debug.assert_any_call("process([1, 2])")
    logger3.debug.assert_any_call("process -> 2")
    assert logger3.debug.call_count == 2

    # Exceptions propagate and no result is logged
    logger4 = MagicMock()

    @LoggedFunction(logger4)
    def boom():
        raise ValueError("boom")

    try:
        boom()
        raised = False
    except ValueError:
        raised = True
    assert raised
    # Only the call was logged, not a result
    logger4.debug.assert_called_once_with("boom()")

# Generated at 2026-11-01 21:30:27.694545
# Unit test for function format_arg
def test_format_arg():
    # Plain string is wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"

    # String with surrounding whitespace is stripped
    assert module_0.format_arg("  hello  ") == "'hello'"

    # Empty string becomes quoted empty string
    assert module_0.format_arg("") == "''"

    # Integer is converted to its string representation
    assert module_0.format_arg(42) == "42"

    # Negative integer
    assert module_0.format_arg(-7) == "-7"

    # Float
    assert module_0.format_arg(3.14) == "3.14"

    # Boolean
    assert module_0.format_arg(True) == "True"

    # None
    assert module_0.format_arg(None) == "None"

    # List
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"

    # Dictionary
    assert module_0.format_arg({"a": 1}) == "{'a': 1}"

    # String containing quotes is preserved as-is (only wrapped)
    assert module_0.format_arg("it's") == "'it's'"

    # Multiline-type whitespace inside is kept, only edges stripped
    assert module_0.format_arg("  a b  ") == "'a b'"

# Generated at 2026-11-01 21:31:02.853116
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Create a mock logger
    mock_logger = MagicMock()

    # Create the decorator instance
    logged_function = LoggedFunction(mock_logger)

    # Decorate a test function
    @logged_function
    def add(a, b, c=0):
        """Add numbers."""
        return a + b + c

    # Verify functools.wraps preserved metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

    # Call the decorated function with positional and keyword args
    result = add(1, 2, c=3)
    assert result == 6

    # Verify debug was called twice: once for input, once for output
    assert mock_logger.debug.call_count == 2

    # Check the input log message
    first_call = mock_logger.debug.call_args_list[0][0][0]
    assert first_call == "add(1, 2, c=3)"

    # Check the result log message
    second_call = mock_logger.debug.call_args_list[1][0][0]
    assert second_call == "add -> 6"


def test_LoggedFunction___call__string_args():
    # String args should be quoted and stripped
    mock_logger = MagicMock()
    logged_function = LoggedFunction(mock_logger)

    @logged_function
    def greet(name):
        return f"Hello {name}"

    result = greet("  world  ")
    assert result == "Hello   world  "

    first_call = mock_logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world')"

    second_call = mock_logger.debug.call_args_list[1][0][0]
    assert second_call == "greet -> Hello   world  "


def test_LoggedFunction___call__none_result_not_logged():
    # If the function returns None, only the input should be logged
    mock_logger = MagicMock()
    logged_function = LoggedFunction(mock_logger)

    @logged_function
    def do_nothing():
        pass

    result = do_nothing()
    assert result is None

    # Only the call input was logged, not the result
    assert mock_logger.debug.call_count == 1
    first_call = mock_logger.debug.call_args_list[0][0][0]
    assert first_call == "do_nothing()"


def test_LoggedFunction___call__no_args():
    # Function with no arguments
    mock_logger = MagicMock()
    logged_function = LoggedFunction(mock_logger)

    @logged_function
    def noop():
        return 42

    assert noop() == 42
    assert mock_logger.debug.call_count == 2
    assert mock_logger.debug.call_args_list[0][0][0] == "noop()"
    assert mock_logger.debug.call_args_list[1][0][0] == "noop -> 42"


def test_LoggedFunction___call__propagates_exceptions():
    # Exceptions from the wrapped function should propagate (and no result logged)
    mock_logger = MagicMock()
    logged_function = LoggedFunction(mock_logger)

    @logged_function
    def boom():
        raise RuntimeError("boom")

    try:
        boom()
        assert False, "Expected RuntimeError"
    except RuntimeError:
        pass

    # Only the input log happened; result was never logged
    assert mock_logger.debug.call_count == 1

# Generated at 2026-11-01 21:32:07.680154
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration: raise_for_status hook installed, retry enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # Retry adapter mounted for both http and https
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(https_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)

    # The installed hook should call raise_for_status on the response
    mock_response = Mock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once()

    # raise_for_status disabled: no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks.get("response", []) == []

    # retry disabled: default adapter used (no retries)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0

    # retry as integer: Retry configured with that total
    session = module_0.build_requests_session(retry=3)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 3

    # retry as a Retry instance: instance is used directly
    retry = Retry(total=5, backoff_factor=0.2)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is retry

    # invalid retry value raises ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-11-01 21:33:19.549348
# Unit test for function build_requests_session
def test_build_requests_session():
    # nonce:cd83b4d9
    class FakeResponse:
        def __init__(self):
            self.raise_status_called = False

        def raise_for_status(self):
            self.raise_status_called = True

    # Default construction returns a Session
    session = module_0.build_requests_session()
    assert isinstance(session, Session)

    # A raise_for_status hook is installed by default and behaves correctly
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    fake_response = FakeResponse()
    session.hooks["response"][0](fake_response)
    assert fake_response.raise_status_called

    # With raise_for_status=False no hook should be installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    for event_hooks in session.hooks.values():
        assert not event_hooks

    # retry=True installs a default Retry configuration
    session = module_0.build_requests_session(retry=True)
    adapter = session.get_adapter("http://example.com/")
    assert isinstance(adapter.max_retries, Retry)

    # retry as an integer sets the total number of retries
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com/")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as a Retry instance is used as-is
    retry_instance = Retry(total=7, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_instance)
    adapter = session.get_adapter("http://example.com/")
    assert adapter.max_retries is retry_instance

    # The same adapter is mounted for both http and https
    session = module_0.build_requests_session(retry=3)
    assert (
        session.get_adapter("http://example.com/")
        is session.get_adapter("https://example.com/")
    )

    # retry=False leaves the default (non-Retry) adapters in place
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com/")
    assert isinstance(adapter.max_retries, int)

    # An invalid retry argument raises ValueError
    raised = False
    try:
        module_0.build_requests_session(retry="not-a-retry")
    except ValueError:
        raised = True
    assert raised

# Generated at 2026-11-01 21:34:19.350814
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration: raise_for_status enabled, default retry
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # Retry adapter mounted for both http and https with default Retry
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(https_adapter, HTTPAdapter)
    assert http_adapter.max_retries.total == Retry().total
    assert https_adapter.max_retries.total == Retry().total

    # raise_for_status disabled: no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert session.hooks["response"] == []

    # retry disabled: default adapter with zero retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries.total == 0

    # retry as integer: Retry with given total count
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 5

    # retry as Retry instance: instance is used directly
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is retry

    # invalid retry value raises ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-11-01 21:35:14.854952
# Unit test for function build_requests_session
def test_build_requests_session():import pytest
from unittest.mock import MagicMock, patch
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from mymodule import build_requests_session  # adjust import to your module


def test_build_requests_session_defaults():
    """Default call should return a Session with raise_for_status hook and default Retry."""
    session = module_0.build_requests_session()
    assert isinstance(session, Session)

    # raise_for_status hook installed
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # Default retry adapter mounted on http and https
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == Retry().total

    assert session.get_adapter("https://example.com") is adapter


def test_build_requests_session_raise_for_status_hook():
    """The installed response hook should call raise_for_status."""
    session = module_0.build_requests_session(raise_for_status=True)
    hook = session.hooks["response"][0]

    mock_response = MagicMock()
    hook(mock_response)
    mock_response.raise_for_status.assert_called_once()


def test_build_requests_session_no_raise_for_status():
    """When raise_for_status=False, no hooks should be installed."""
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}
    assert "response" not in session.hooks


def test_build_requests_session_retry_false():
    """When retry=False, no retry adapter should be mounted."""
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == 0  # default HTTPAdapter has no retries


def test_build_requests_session_retry_int():
    """When retry is an int, Retry should be configured with that total."""
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5


def test_build_requests_session_retry_zero():
    """retry=0 is falsy, so no retry adapter is mounted."""
    session = module_0.build_requests_session(retry=0)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries == 0


def test_build_requests_session_retry_instance():
    """When a Retry instance is passed, it should be used directly."""
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is retry


def test_build_requests_session_invalid_retry_raises():
    """Passing an unsupported type for retry should raise ValueError."""
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        module_0.build_requests_session(retry="not valid")

    with pytest.raises(ValueError):
        module_0.build_requests_session(retry=1.5)

    with pytest.raises(ValueError):
        module_0.build_requests_session(retry=["a", "b"])


def test_build_requests_session_mounts_adapter_on_both_schemes():
    """The same adapter should be mounted for both http:// and https://."""
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter is https_adapter
    assert isinstance(http_adapter, HTTPAdapter)


@patch("mymodule.Retry")  # adjust to your module path
def test_build_requests_session_retry_true_uses_default_retry(mock_retry_cls):
    """When retry=True, Retry() should be constructed with no arguments."""
    mock_retry_instance = MagicMock()
    mock_retry_cls.return_value = mock_retry_instance

    session = module_0.build_requests_session(retry=True)

    mock_retry_cls.assert_called_once_with()
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is mock_retry_instance

# Generated at 2026-11-01 21:35:46.104388
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
# nonce:5d4e220b
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def sample_function(a, b=None):
        """Sample docstring."""
        return f"{a}-{b}"

    # functools.wraps preserves the original function's metadata
    assert sample_function.__name__ == "sample_function"
    assert sample_function.__doc__ == "Sample docstring."

    # Call with positional and keyword arguments
    result = sample_function("hello", b=42)
    assert result == "hello-42"

    # Arguments are logged before the call, result logged after
    assert logger.debug.call_args_list == [
        (("sample_function('hello', b=42)",), {}),
        (("sample_function -> hello-42",), {}),
    ]

    # Multiple positional args; strings are quoted, others use str()
    @decorator
    def multi(a, b, c):
        return (a, b, c)

    assert multi(1, "two", 3) == (1, "two", 3)
    logger.debug.assert_any_call("multi(1, 'two', 3)")
    logger.debug.assert_any_call("multi -> (1, 'two', 3)")

    # Function returning None: only the arguments are logged, not the result
    @decorator
    def none_function(x):
        return None

    assert none_function(5) is None
    assert logger.debug.call_count == 5
    assert logger.debug.call_args_list[-1] == (("none_function(5)",), {})

# Generated at 2026-11-01 21:36:24.637373
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()

    @LoggedFunction(logger)
    def add(a, b, c=0):
        """Add three numbers."""
        return a + b + c

    # functools.wraps preserves function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add three numbers."

    # Positional arguments are logged on entry and the result on exit
    assert add(1, 2) == 3
    logger.debug.assert_any_call("add(1, 2)")
    logger.debug.assert_any_call("add -> 3")
    assert logger.debug.call_count == 2

    # Keyword arguments appear in the entry log
    logger.reset_mock()
    assert add(1, b=2, c=4) == 7
    logger.debug.assert_any_call("add(1, b=2, c=4)")
    logger.debug.assert_any_call("add -> 7")
    assert logger.debug.call_count == 2

    # Strings are quoted and stripped in the log output only
    logger.reset_mock()

    @LoggedFunction(logger)
    def greet(name, punctuation="!"):
        return "Hi %s%s" % (name, punctuation)

    assert greet(" bob ", punctuation="?") == "Hi  bob ?"
    logger.debug.assert_any_call("greet('bob', punctuation='?')")
    logger.debug.assert_any_call("greet -> Hi  bob ?")

    # A function with no args returning None logs only the entry line
    logger.reset_mock()

    @LoggedFunction(logger)
    def noop():
        return None

    assert noop() is None
    logger.debug.assert_called_once_with("noop()")

    # Falsy (but not None) results are still logged
    logger.reset_mock()

    @LoggedFunction(logger)
    def zero():
        return 0

    assert zero() == 0
    logger.debug.assert_any_call("zero()")
    logger.debug.assert_any_call("zero -> 0")

    # Exceptions propagate and no result line is logged
    logger.reset_mock()

    @LoggedFunction(logger)
    def boom():
        raise ValueError("boom")

    raised = False
    try:
        boom()
    except ValueError:
        raised = True
    assert raised
    logger.debug.assert_called_once_with("boom()")

# Generated at 2026-11-01 21:36:55.410313
# Unit test for function format_arg
def test_format_arg():
    # Strings are wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"

    # Strings are stripped of surrounding whitespace
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("\tfoo\n") == "'foo'"

    # Empty string
    assert module_0.format_arg("") == "''"

    # Non-string values are converted with str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(-1) == "-1"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(False) == "False"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"
    assert module_0.format_arg((1, 2)) == "(1, 2)"
    assert module_0.format_arg({"a": 1}) == "{'a': 1}"