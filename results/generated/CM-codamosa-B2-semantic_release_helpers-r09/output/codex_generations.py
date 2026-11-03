

# Generated at 2026-11-01 21:51:42.922381
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default arguments: raise_for_status hook installed, default Retry adapter mounted
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == Retry().total
    # Same adapter instance mounted for both http and https
    assert session.get_adapter("http://example.com") is adapter

    # The installed hook should call raise_for_status on the response
    mock_response = MagicMock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # raise_for_status=False -> no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks["response"] == []

    # retry=False -> no retry adapter mounted (default adapter, no retries)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0

    # retry as int -> Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance -> used as-is
    custom_retry = Retry(total=3, backoff_factor=0.1)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type -> ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="not a valid retry")

# Generated at 2026-11-01 21:52:00.837085
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Unit test for constructor of class LoggedFunction."""
    from unittest.mock import MagicMock

    logger = MagicMock()

    # Test constructor sets logger attribute
    logged_function = LoggedFunction(logger)
    assert logged_function.logger is logger

    # Test with different logger instances
    another_logger = MagicMock()
    another_logged_function = LoggedFunction(another_logger)
    assert another_logged_function.logger is another_logger

    # Each instance holds its own logger reference
    assert logged_function.logger is not another_logged_function.logger

# Generated at 2026-11-01 21:52:21.257977
# Unit test for function format_arg
def test_format_arg():
    # Strings are wrapped in single quotes and stripped
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  padded  ") == "'padded'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg("no trailing space\n") == "'no trailing space'"

    # Non-string values are converted via str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(-7) == "-7"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"
    assert module_0.format_arg((1, 2)) == "(1, 2)"
    assert module_0.format_arg({"key": "value"}) == "{'key': 'value'}"

# Generated at 2026-11-01 21:52:40.875479
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = MagicMock()
    logged_function = LoggedFunction(logger)
    assert logged_function.logger is logger

# Generated at 2026-11-01 21:53:27.371775
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():from unittest.mock import Mock


# Generated at 2026-11-01 21:54:06.238852
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = "test_logger"
    logged_function = LoggedFunction(logger)
    assert logged_function.logger == logger

# Generated at 2026-11-01 21:55:00.657535
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    logger = Mock()
    logged_function = LoggedFunction(logger)

    @logged_function
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    # functools.wraps preserves function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

    # Return value is passed through unchanged
    assert add(1, b=2) == 3

    # Both invocation and result are logged
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, b=2)")
    logger.debug.assert_any_call("add -> 3")

    # String arguments are wrapped in single quotes
    logger.reset_mock()

    @logged_function
    def concat(left, right):
        return left + right

    assert concat("foo", "bar") == "foobar"
    logger.debug.assert_any_call("concat('foo', 'bar')")
    logger.debug.assert_any_call("concat -> foobar")

    # A None result is not logged
    logger.reset_mock()

    @logged_function
    def noop():
        pass

    assert noop() is None
    assert logger.debug.call_count == 1
    logger.debug.assert_called_once_with("noop()")

# Generated at 2026-11-01 21:55:47.979311
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()

    @LoggedFunction(logger)
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    # Decorated function returns the wrapped function's result
    result = add(1, b=2)
    assert result == 3

    # functools.wraps preserves the wrapped function's metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

    # Arguments logged before the call, result logged after
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, b=2)")
    logger.debug.assert_any_call("add -> 3")


def test_LoggedFunction___call__string_args_formatted():
    logger = MagicMock()

    @LoggedFunction(logger)
    def greet(name):
        return "hi " + name

    result = greet("  bob ")
    assert result == "hi   bob "

    # Strings are stripped and quoted by format_arg
    logger.debug.assert_any_call("greet('bob')")
    logger.debug.assert_any_call("greet -> hi   bob ")


def test_LoggedFunction___call__none_result_not_logged():
    logger = MagicMock()

    @LoggedFunction(logger)
    def nothing():
        pass

    assert nothing() is None

    # None results are not logged, only the call itself
    logger.debug.assert_called_once_with("nothing()")


def test_LoggedFunction___call__positional_and_mixed_args():
    logger = MagicMock()

    @LoggedFunction(logger)
    def combine(x, y, sep="-"):
        return sep.join([str(x), str(y)])

    result = combine(1, 2, sep=":")
    assert result == "1:2"

    logger.debug.assert_any_call("combine(1, 2, sep=':')")
    logger.debug.assert_any_call("combine -> 1:2")

# Generated at 2026-11-01 21:56:33.009489
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration: raise_for_status hook installed, default Retry mounted
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == Retry().total
    # Same adapter mounted for both http and https
    assert session.get_adapter("https://example.com") is adapter

    # The installed hook invokes raise_for_status on error responses
    response = requests.Response()
    response.status_code = 500
    with pytest.raises(requests.HTTPError):
        session.hooks["response"][0](response)

    # raise_for_status=False: no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks.get("response") in ([], None)

    # retry=False: adapters remain default (no retries)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with given total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: instance is used directly
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is retry

    # Invalid retry type raises ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="not valid")

# Generated at 2026-11-01 21:57:13.161232
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default construction returns a configured Session
    session = module_0.build_requests_session()
    assert isinstance(session, Session)

    # raise_for_status hook is installed by default and invokes raise_for_status
    hook_calls = []

    class FakeResponse:
        def raise_for_status(self):
            hook_calls.append(True)

    hooks = session.hooks["response"]
    assert len(hooks) == 1
    hooks[0](FakeResponse())
    assert hook_calls == [True]

    # Retry-enabled adapter is mounted on both http and https by default
    adapter_http = session.get_adapter("http://example.com/")
    adapter_https = session.get_adapter("https://example.com/")
    assert isinstance(adapter_http, HTTPAdapter)
    assert adapter_http is adapter_https
    assert adapter_http.max_retries.total == Retry().total

    # raise_for_status=False leaves hooks untouched (no raise_for_status hook)
    session = module_0.build_requests_session(raise_for_status=False)
    assert len(session.hooks.get("response", [])) == 0

    # retry=False means the default (zero-retry) adapters remain
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("http://example.com/")
    assert adapter.max_retries.total == 0

    # retry as an int sets the total retry count
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com/")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 5

    # retry as a Retry instance is passed through unchanged
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("http://example.com/")
    assert adapter.max_retries is retry

    # An invalid retry value raises ValueError
    try:
        module_0.build_requests_session(retry="lots")
        raised = False
    except ValueError:
        raised = True
    assert raised

# Generated at 2026-11-01 21:57:51.520683
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Setup a mock logger
    logger = Mock()

    # Create the decorator
    decorator = LoggedFunction(logger)

    # Decorate a function with positional and keyword arguments
    @decorator
    def add(a, b, c=0):
        """Add numbers."""
        return a + b + c

    # Verify functools.wraps preserved function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

    # Call the decorated function
    result = add(1, " two", c=3.5)
    assert result == "1 two3.5" or result == 1 + 3.5  # sanity: function executed

    # Verify the arguments were logged before the call
    first_call = logger.debug.call_args_list[0][0][0]
    assert "add(1, ' two', c=3.5)" == first_call

    # Verify the result was logged after the call
    second_call = logger.debug.call_args_list[1][0][0]
    assert "add -> " in second_call

    # Verify a function returning None does not log a result
    @LoggedFunction(logger)
    def returns_none(x):
        return None

    debug_count_before = logger.debug.call_count
    assert returns_none(5) is None
    # Only the argument log call should have occurred, no result log
    assert logger.debug.call_count == debug_count_before + 1
    last_call = logger.debug.call_args_list[-1][0][0]
    assert "returns_none(5)" == last_call

    # Verify string args are quoted and stripped
    @LoggedFunction(logger)
    def greet(name):
        return name

    greet("  bob  ")
    expected_args_call = logger.debug.call_args_list[-2][0][0]
    assert "greet('bob')" == expected_args_call

# Generated at 2026-11-01 21:58:42.052829
# Unit test for function build_requests_session
def test_build_requests_session():import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from mymodule import build_requests_session  # adjust import as needed


def test_build_requests_session_defaults():
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    # raise_for_status hook installed by default
    assert "response" in session.hooks
    assert callable(session.hooks["response"][0])
    # default retry adapter mounted on http and https
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == Retry().total
    assert session.get_adapter("https://example.com") is adapter


def test_build_requests_session_no_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert session.hooks == {}


def test_build_requests_session_no_retry():
    session = module_0.build_requests_session(retry=False)
    assert isinstance(session, Session)
    # default adapters mounted, not ours
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert not adapter.max_retries.total


def test_build_requests_session_retry_int():
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 5


def test_build_requests_session_retry_zero_int():
    session = module_0.build_requests_session(retry=0)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0


def test_build_requests_session_retry_instance():
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries is retry


def test_build_requests_session_invalid_retry_type():
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="invalid")


def test_build_requests_session_hook_raises_for_status():
    session = module_0.build_requests_session()
    import responses  # optional; fallback to manual test below if unavailable

    responses.add(
        responses.GET,
        "http://example.com/fail",
        status=500,
    )
    with pytest.raises(Exception):
        session.get("http://example.com/fail")

# Generated at 2026-11-01 21:59:29.871390
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def add(a, b, c=0):
        """Add numbers."""
        return a + b + c

    # functools.wraps preserves function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

    # Return value is passed through unchanged
    assert add(1, 2, c=3) == 6

    # Input arguments and result are both logged
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")


def test_LoggedFunction___call__string_args_are_quoted_and_stripped():
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def greet(name, greeting="Hello"):
        return f"{greeting} {name}"

    result = greet("  Bob ", greeting="Hi")
    assert result == "Hi   Bob "  # original (unstripped) value is used in the call

    # Logged strings are stripped and wrapped in single quotes
    logger.debug.assert_any_call("greet('Bob', greeting='Hi')")
    logger.debug.assert_any_call("greet -> Hi   Bob ")


def test_LoggedFunction___call__none_result_not_logged():
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def nothing():
        pass

    assert nothing() is None

    # Only the input-arguments debug call happens; None result is not logged
    assert logger.debug.call_count == 1
    logger.debug.assert_called_once_with("nothing()")


def test_LoggedFunction___call__no_args():
    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def constant():
        return 42

    assert constant() == 42
    logger.debug.assert_any_call("constant()")
    logger.debug.assert_any_call("constant -> 42")
    assert logger.debug.call_count == 2

# Generated at 2026-11-01 22:00:09.709122
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default arguments: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # Mounted adapter should use a default Retry config (total=10)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 10

    # The installed hook should invoke raise_for_status on the response
    mock_response = mock.Mock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once()

    # raise_for_status=False: no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert session.hooks == {"response": []}

    # retry=False: no retry adapter mounted (default max_retries is 0)
    session = module_0.build_requests_session(retry=False)
    assert isinstance(session, Session)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with the given total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: instance is passed through unchanged
    retry_instance = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_instance)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is retry_instance

    # Invalid retry type should raise ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="invalid")

    with pytest.raises(ValueError):
        module_0.build_requests_session(retry=1.5)

# Generated at 2026-11-01 22:00:56.118235
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()

    @LoggedFunction(logger)
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    result = add(1, b=2)

    # Result is returned unchanged
    assert result == 3

    # Function name and arguments are logged before the call
    logger.debug.assert_any_call("add(1, b=2)")

    # Return value is logged after the call
    logger.debug.assert_any_call("add -> 3")

    # Exactly two debug calls were made
    assert logger.debug.call_count == 2

    # functools.wraps preserves function metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."


def test_LoggedFunction___call__string_args():
    logger = MagicMock()

    @LoggedFunction(logger)
    def greet(name):
        return "hello " + name

    assert greet("world") == "hello world"
    # Strings are quoted in the log output
    logger.debug.assert_any_call("greet('world')")
    logger.debug.assert_any_call("greet -> hello world")


def test_LoggedFunction___call__none_result_not_logged():
    logger = MagicMock()

    @LoggedFunction(logger)
    def do_nothing():
        pass

    assert do_nothing() is None
    # Only the invocation is logged; None results are not logged
    logger.debug.assert_called_once_with("do_nothing()")