

# Generated at 2026-10-24 05:53:50.413601
# Unit test for function format_arg
def test_format_arg():
    # Strings are stripped and wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  padded  ") == "'padded'"
    assert module_0.format_arg("") == "''"

    # Non-strings are passed through str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg([1, "a"]) == "[1, 'a']"
    assert module_0.format_arg({"k": 1}) == "{'k': 1}"

# Generated at 2026-10-24 05:54:04.126803
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

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)
    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry

    # Disabled options
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0

    # Invalid retry type
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:54:05.528206
# Unit test for function format_arg
def test_format_arg():
    # Strings are stripped and wrapped in single quotes
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  padded  ") == "'padded'"
    assert module_0.format_arg("") == "''"

    # Non-strings are passed through str()
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg([1, "a"]) == "[1, 'a']"
    assert module_0.format_arg({"k": 1}) == "{'k': 1}"

# Generated at 2026-10-24 05:54:11.579279
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-24 05:54:14.141143
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 05:54:17.815990
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():logger = object()

# Generated at 2026-10-24 05:54:23.165564
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-24 05:54:27.036381
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():logger = object()

# Generated at 2026-10-24 05:54:39.527611
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:54:40.958903
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:54:54.068498
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration installs the status hook and retry adapters.
    session = module_0.build_requests_session()

    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    assert isinstance(session.get_adapter("http://").max_retries, Retry)
    assert isinstance(session.get_adapter("https://").max_retries, Retry)

    response = Response()
    response.status_code = 500
    response.url = "https://example.com/test"

    with pytest.raises(HTTPError):
        session.hooks["response"][0](response)

    session.close()

    # An integer configures the total retry count.
    session = module_0.build_requests_session(raise_for_status=False, retry=3)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    session.close()

    # A supplied Retry instance is used directly.
    retry_config = Retry(total=5, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config

    session.close()

    # Unsupported retry configurations are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:55:06.871223
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    http_adapter = session.get_adapter("http://")
    https_adapter = session.get_adapter("https://")

    assert http_adapter is https_adapter
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(http_adapter.max_retries, Retry)

    # Explicit retry count
    retry_session = module_0.build_requests_session(retry=3)
    assert retry_session.get_adapter("https://").max_retries.total == 3

    # Supplied Retry instance
    retry = Retry(total=5)
    custom_session = module_0.build_requests_session(retry=retry)
    assert custom_session.get_adapter("https://").max_retries is retry

    # Disabled options
    disabled_session = module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    )
    assert disabled_session.hooks["response"] == []
    assert disabled_session.get_adapter("https://").max_retries.total == 0

    # Invalid retry configuration
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:55:08.199083
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:09.513411
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:21.919834
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    with module_0.build_requests_session() as session:
        assert isinstance(session, Session)
        assert len(session.hooks["response"]) == 1

        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        for scheme in ("http://", "https://"):
            adapter = session.get_adapter(scheme)
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)

    # Explicit retry count
    with module_0.build_requests_session(retry=3) as session:
        assert session.get_adapter("http://").max_retries.total == 3
        assert session.get_adapter("https://").max_retries.total == 3

    # Custom Retry instance
    custom_retry = Retry(total=5, backoff_factor=0.5)
    with module_0.build_requests_session(retry=custom_retry) as session:
        assert session.get_adapter("http://").max_retries is custom_retry
        assert session.get_adapter("https://").max_retries is custom_retry

    # Retries and raise-for-status hook disabled
    with module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    ) as session:
        assert session.hooks["response"] == []
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0

    # Invalid retry configuration
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:55:23.353346
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:35.746520
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    assert isinstance(session.get_adapter("http://").max_retries, Retry)
    assert isinstance(session.get_adapter("https://").max_retries, Retry)
    session.close()

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
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
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:55:37.081912
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:38.510964
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:40.010303
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:41.405440
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:42.755474
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:44.145278
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:45.580492
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:47.006663
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:55:48.441703
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:02.477618
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

    expected_total = Retry().total
    assert session.get_adapter("http://").max_retries.total == expected_total
    assert session.get_adapter("https://").max_retries.total == expected_total

    # Disable raise_for_status hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Configure retries using an existing Retry instance
    retry_config = Retry(total=5, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config

    # Reject unsupported retry values
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:56:03.854658
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:05.165114
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:06.567383
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:07.998815
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:22.848298
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

    for scheme in ("http://", "https://"):
        adapter = session.get_adapter(scheme)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Configure retries using an existing Retry instance
    retry_config = Retry(total=5, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config

    # Reject unsupported retry values
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:56:24.282371
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:25.698080
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:27.148553
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:28.582539
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:44.263644
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

    # Disable the response hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=3)

    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["https://"].max_retries.total == 3

    # Configure retries using an existing Retry instance
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.adapters["http://"].max_retries is retry
    assert session.adapters["https://"].max_retries is retry

    # Reject unsupported retry values
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:56:45.593831
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:56:46.911176
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:07.818527
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration installs the status hook and retry adapters.
    with module_0.build_requests_session() as session:
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        http_adapter = session.get_adapter("http://")
        https_adapter = session.get_adapter("https://")

        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert http_adapter.max_retries.total == Retry().total

    # An integer configures the total retry count.
    with module_0.build_requests_session(retry=3) as session:
        assert session.get_adapter("https://").max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry = Retry(total=5, backoff_factor=0.5)
    with module_0.build_requests_session(retry=retry) as session:
        assert session.get_adapter("http://").max_retries is retry
        assert session.get_adapter("https://").max_retries is retry

    # Both optional behaviors can be disabled.
    with module_0.build_requests_session(raise_for_status=False, retry=False) as session:
        assert session.hooks["response"] == []
        assert session.get_adapter("https://").max_retries.total == 0

    # Unsupported retry values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:57:09.380882
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:10.691845
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:24.187903
# Unit test for function build_requests_session
def test_build_requests_session():
    retry_config = Retry(total=3)
    session = module_0.build_requests_session(
        raise_for_status=True,
        retry=retry_config,
    )

    try:
        assert isinstance(session, Session)

        # Verify the raise_for_status response hook.
        assert len(session.hooks["response"]) == 1
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Verify retry adapters are mounted for HTTP and HTTPS.
        for scheme in ("http://", "https://"):
            adapter = session.get_adapter(scheme)
            assert isinstance(adapter, HTTPAdapter)
            assert adapter.max_retries is retry_config
            assert adapter.max_retries.total == 3
    finally:
        session.close()


@pytest.mark.parametrize(
    ("retry_value", "expected_total"),
    [
        (True, Retry.DEFAULT),
        (2, 2),
    ],
)
def test_build_requests_session_retry_configuration(retry_value, expected_total):
    session = module_0.build_requests_session(retry=retry_value)

    try:
        assert session.get_adapter("http://").max_retries.total == expected_total
        assert session.get_adapter("https://").max_retries.total == expected_total
    finally:
        session.close()


def test_build_requests_session_without_status_hook_or_retries():
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    try:
        assert session.hooks["response"] == []

        # Requests' standard adapters remain mounted, with retries disabled.
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:57:38.150523
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    # raise_for_status hook is installed and invoked.
    assert len(session.hooks["response"]) == 1
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Retry-enabled adapters are mounted for HTTP and HTTPS.
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")

    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)

    session.close()


def test_build_requests_session_without_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []

    session.close()


def test_build_requests_session_with_integer_retry_count():
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("https://example.com").max_retries.total == 3

    session.close()


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("https://example.com").max_retries is retry

    session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:57:39.479745
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:40.877165
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:42.190169
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:43.495221
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:57:45.329272
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:04.665892
# Unit test for function build_requests_session
def test_build_requests_session():import pytest
from unittest.mock import Mock


def test_build_requests_session_defaults():
    session = module_0.build_requests_session()

    assert isinstance(session, Session)

    # The response hook should call raise_for_status.
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Both protocols should use the configured retry adapter.
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")

    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)


def test_build_requests_session_without_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    assert session.get_adapter("http://example.com").max_retries.total == 0
    assert session.get_adapter("https://example.com").max_retries.total == 0


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_with_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    assert (
        session.get_adapter("http://example.com").max_retries.total == retry_count
    )
    assert (
        session.get_adapter("https://example.com").max_retries.total == retry_count
    )


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=4, backoff_factor=0.5)

    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("http://example.com").max_retries is retry
    assert session.get_adapter("https://example.com").max_retries is retry


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:58:06.375990
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:18.001142
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1
    assert isinstance(session.get_adapter("http://").max_retries, Retry)
    assert isinstance(session.get_adapter("https://").max_retries, Retry)

    # Verify the response hook calls raise_for_status()
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Disable the response hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=5)

    assert session.get_adapter("http://").max_retries.total == 5
    assert session.get_adapter("https://").max_retries.total == 5

    # Configure retries using an existing Retry instance
    retry_config = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config

    # Reject unsupported retry values
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:58:30.030517
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import MagicMock

    # Create a mock logger
    logger = MagicMock(spec=logging.Logger)

    # Create the decorator and apply it to a test function
    logged_function_decorator = LoggedFunction(logger)

    @logged_function_decorator
    def add_numbers(a, b, separator="-"):
        return f"{a}{separator}{b}"

    # Reset mock to isolate the call we're testing
    logger.reset_mock()

    # Call the decorated function with args and kwargs
    result = add_numbers("hello", "world", separator=":")

    # Verify the function's return value is passed through unchanged
    assert result == "hello:world"

    # The logger should have been called exactly twice (args + result)
    assert logger.debug.call_count == 2

    # First debug call: logs function name and arguments
    first_call_args = logger.debug.call_args_list[0][0][0]
    assert "add_numbers" in first_call_args
    assert "'hello'" in first_call_args
    assert "'world'" in first_call_args
    assert "separator=':'" in first_call_args

    # Second debug call: logs the return value
    second_call_args = logger.debug.call_args_list[1][0][0]
    assert "add_numbers -> hello:world" in second_call_args

    # Test with a function that returns None (result should not be logged)
    @logged_function_decorator
    def returns_none(x):
        return None

    logger.reset_mock()
    none_result = returns_none(42)

    assert none_result is None
    # Only one debug call: arguments logged, but None result is not logged
    assert logger.debug.call_count == 1
    assert "returns_none" in logger.debug.call_args_list[0][0][0]
    assert "42" in logger.debug.call_args_list[0][0][0]

    # Test with a function that has no arguments and no return value
    @logged_function_decorator
    def no_args():
        pass

    logger.reset_mock()
    no_args()

    assert logger.debug.call_count == 1
    assert "no_args()" in logger.debug.call_args_list[0][0][0]

    # Test that functools.wraps preserves function metadata
    assert add_numbers.__name__ == "add_numbers"
    assert returns_none.__name__ == "returns_none"
    assert no_args.__name__ == "no_args"

# Generated at 2026-10-24 05:58:45.716947
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    for scheme in ("http://", "https://"):
        adapter = session.get_adapter(scheme)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)

    # Explicit retry count
    session = module_0.build_requests_session(retry=3)
    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Supplied Retry instance
    retry_policy = Retry(total=5)
    session = module_0.build_requests_session(retry=retry_policy)
    assert session.get_adapter("http://").max_retries is retry_policy
    assert session.get_adapter("https://").max_retries is retry_policy

    # Disabled status hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Invalid retry configuration
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:58:47.046828
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:48.564764
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:50.106099
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:51.412125
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:53.941002
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:55.269837
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:56.573533
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:57.889430
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:58:59.300162
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:59:13.768172
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session(retry=3)

    assert isinstance(session, Session)

    # Verify the raise_for_status response hook is installed.
    response = Response()
    response.status_code = 500
    response.url = "https://example.com/test"

    with pytest.raises(HTTPError):
        session.hooks["response"][0](response)

    # Verify retry adapters are mounted for HTTP and HTTPS.
    http_adapter = session.get_adapter("http://")
    https_adapter = session.get_adapter("https://")

    assert http_adapter.max_retries.total == 3
    assert https_adapter.max_retries.total == 3


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)

    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry


def test_build_requests_session_without_retry_or_status_hook():
    session = module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:59:15.392966
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:59:28.194061
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    try:
        assert isinstance(session, Session)

        http_adapter = session.get_adapter("http://")
        https_adapter = session.get_adapter("https://")

        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)

        # Verify the raise_for_status response hook
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()
    finally:
        session.close()

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    try:
        assert session.hooks["response"] == []
    finally:
        session.close()

    # Configure retry count
    session = module_0.build_requests_session(retry=5)

    try:
        assert session.get_adapter("https://").max_retries.total == 5
    finally:
        session.close()

    # Use a provided Retry instance
    retry_configuration = Retry(total=7)
    session = module_0.build_requests_session(retry=retry_configuration)

    try:
        assert session.get_adapter("https://").max_retries is retry_configuration
    finally:
        session.close()

    # Reject unsupported retry values
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:59:29.522026
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:59:41.709669
# Unit test for function build_requests_session
def test_build_requests_session():
    retry = Retry(total=3)

    session = module_0.build_requests_session(raise_for_status=True, retry=retry)

    assert isinstance(session, Session)
    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    session.close()


@pytest.mark.parametrize(
    ("retry_value", "expected_total"),
    [
        (True, Retry().total),
        (2, 2),
    ],
)
def test_build_requests_session_retry_configuration(retry_value, expected_total):
    session = module_0.build_requests_session(retry=retry_value)

    assert session.get_adapter("http://").max_retries.total == expected_total
    assert session.get_adapter("https://").max_retries.total == expected_total

    session.close()


def test_build_requests_session_without_status_hook_or_retries():
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    session.close()


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 05:59:45.945886
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 05:59:58.709568
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert isinstance(session.adapters["http://"], HTTPAdapter)
    assert session.adapters["http://"] is session.adapters["https://"]
    assert isinstance(session.adapters["http://"].max_retries, Retry)

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()


def test_build_requests_session_without_raise_for_status():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    # These are the default adapters installed by requests.Session.
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


def test_build_requests_session_rejects_invalid_retry():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 06:00:00.140656
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:01.487825
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:02.907132
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:04.245064
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:05.638459
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:18.574534
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration enables status checking and retries.
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    for scheme in ("http://", "https://"):
        adapter = session.get_adapter(scheme)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)

    # An integer configures the total retry count.
    session = module_0.build_requests_session(retry=3)
    assert session.get_adapter("https://").max_retries.total == 3

    # A supplied Retry instance is used directly.
    retry = Retry(total=5)
    session = module_0.build_requests_session(retry=retry)
    assert session.get_adapter("https://").max_retries is retry

    # Both optional features can be disabled.
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.get_adapter("https://").max_retries.total == 0

    # Unsupported retry values are rejected.
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 06:00:20.989797
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:00:27.383501
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 06:00:28.741727
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:38.424030
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:39.730910
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:41.060084
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:42.379437
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:43.686153
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:45.095587
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:46.443165
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:47.963047
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:49.395499
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:00:50.702451
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b, c=0):
        return a + b + c

    result = add(1, 2, c=3)

    # return value passes through unchanged
    assert result == 6

    # one debug call for the call, one for the result
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("add(1, 2, c=3)")
    logger.debug.assert_any_call("add -> 6")

    # functools.wraps preserves metadata
    assert add.__name__ == "add"


def test_LoggedFunction___call___strips_strings_and_skips_none_result():
    logger = MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None

    # strings are stripped by format_arg; None result is not logged
    logger.debug.assert_called_once_with("noop('hi')")

# Generated at 2026-10-24 06:01:06.339135
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:08.835787
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:11.251196
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:13.750429
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:16.160760
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:18.574268
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:21.145315
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:23.561118
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:25.974015
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:28.388810
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:30.803915
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:33.220035
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:35.636840
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:38.052926
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:40.468125
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:01:42.882300
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:45.299332
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:47.713783
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:50.128893
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:52.546047
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:54.958647
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:57.373907
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:01:59.786591
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:02.200036
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:04.617466
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:07.030686
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:09.448013
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:11.860842
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:14.275746
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:02:16.691527
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:04.430029
# Unit test for function build_requests_session
def test_build_requests_session():
    session = module_0.build_requests_session()

    try:
        assert isinstance(session, Session)

        # Verify the raise-for-status response hook.
        assert len(session.hooks["response"]) == 1
        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        # Verify retry-enabled adapters are mounted for HTTP and HTTPS.
        http_adapter = session.get_adapter("http://")
        https_adapter = session.get_adapter("https://")

        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
    finally:
        session.close()

# Generated at 2026-10-24 06:03:06.933127
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:09.348891
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:11.857332
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:14.274287
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:16.689391
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:19.105312
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:21.520157
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:23.935618
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:26.349055
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:28.763491
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:31.176991
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:33.594121
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:36.007609
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:38.421632
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:40.834999
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:43.248714
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:45.673596
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:03:48.077521
# Unit test for method __call__ of class LoggedFunction