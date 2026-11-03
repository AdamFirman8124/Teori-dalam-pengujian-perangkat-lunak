

# Generated at 2026-11-02 23:33:05.467276
# Unit test for function format_arg
def test_format_arg():
    # String values are wrapped in single quotes and stripped
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  spaced  ") == "'spaced'"
    assert module_0.format_arg("") == "''"

    # Non-string values are converted with str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(-1) == "-1"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"
    assert module_0.format_arg({"a": 1}) == "{'a': 1}"
    assert module_0.format_arg((1, 2)) == "(1, 2)"

# Generated at 2026-11-02 23:34:10.108581
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    from unittest.mock import MagicMock

    # Default configuration: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    assert set(session.adapters) == {"http://", "https://"}
    for adapter in session.adapters.values():
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == 10  # Retry() default total

    # The installed hook should call raise_for_status on the response
    mock_response = MagicMock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # raise_for_status=False -> no hook installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks["response"] == []

    # retry=False -> default adapters kept (no retries configured)
    session = module_0.build_requests_session(retry=False)
    assert "response" in session.hooks
    assert set(session.adapters) == {"http://", "https://"}
    for adapter in session.adapters.values():
        assert adapter.max_retries.total == 0

    # retry as int -> Retry with that total
    session = module_0.build_requests_session(retry=5)
    for adapter in session.adapters.values():
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == 5

    # retry as Retry instance -> same instance used on both adapters
    retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    for adapter in session.adapters.values():
        assert adapter.max_retries is retry

    # Invalid retry type -> ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="not a retry")

# Generated at 2026-11-02 23:35:43.529814
# Unit test for function format_arg
def test_format_arg():
    # Strings are stripped and wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  spaced  ") == "'spaced'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg("  ") == "''"

    # Non-string values are converted with str()
    assert module_0.format_arg(123) == "123"
    assert module_0.format_arg(-1) == "-1"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(False) == "False"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2, 3]) == "[1, 2, 3]"
    assert module_0.format_arg({"a": 1}) == "{'a': 1}"
    assert module_0.format_arg((1, 2)) == "(1, 2)"

    # Type distinction: str subclass vs other types
    class MyStr(str):
        pass

    assert module_0.format_arg(MyStr("  subclass  ")) == "'subclass'"

# Generated at 2026-11-02 23:38:31.097557
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = MagicMock()
    logged_function = LoggedFunction(logger)
    assert logged_function.logger == logger

# Generated at 2026-11-02 23:40:20.949136
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():import logging

# Generated at 2026-11-02 23:41:41.083208
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    """Test that the LoggedFunction constructor stores the logger."""
    # Test with a mock logger
    mock_logger = Mock()
    logged_function = LoggedFunction(mock_logger)
    assert logged_function.logger is mock_logger

    # Test with a standard library logger
    import logging
    logger = logging.getLogger("test_logger")
    logged_function = LoggedFunction(logger)
    assert logged_function.logger is logger
    assert logged_function.logger.name == "test_logger"

    # Test with a Mock-based logger (alternative approach)
    logger = Mock()
    logged_function = LoggedFunction(logger)
    assert isinstance(logged_function, LoggedFunction)
    assert logged_function.logger == logger