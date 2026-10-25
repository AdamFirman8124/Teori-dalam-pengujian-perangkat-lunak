

# Generated at 2026-10-24 06:31:23.833326
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:26.249328
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:28.664815
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:31.080566
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:33.494128
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:35.909012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:31:41.229101
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-24 06:31:45.528047
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():logger = object()

# Generated at 2026-10-24 06:31:46.833159
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

# Generated at 2026-10-24 06:31:51.348231
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = Mock()

    logged_function = LoggedFunction(logger)

    assert logged_function.logger is logger

# Generated at 2026-10-24 06:31:55.604630
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():logger = object()

# Generated at 2026-10-24 06:31:56.928838
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

# Generated at 2026-10-24 06:32:15.536204
# Unit test for function build_requests_session
def test_build_requests_session():
    sessions = []

    try:
        # Default configuration
        session = module_0.build_requests_session()
        sessions.append(session)

        assert isinstance(session, Session)
        assert len(session.hooks["response"]) == 1

        response = Mock()
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()

        expected_default_retries = Retry().total
        assert session.get_adapter("http://").max_retries.total == expected_default_retries
        assert session.get_adapter("https://").max_retries.total == expected_default_retries

        # Explicit retry count
        session_with_count = module_0.build_requests_session(retry=3)
        sessions.append(session_with_count)

        assert session_with_count.get_adapter("http://").max_retries.total == 3
        assert session_with_count.get_adapter("https://").max_retries.total == 3

        # Supplied Retry instance
        retry_config = Retry(total=5, backoff_factor=0.5)
        session_with_config = module_0.build_requests_session(retry=retry_config)
        sessions.append(session_with_config)

        assert session_with_config.get_adapter("http://").max_retries is retry_config
        assert session_with_config.get_adapter("https://").max_retries is retry_config

        # Disabled status hook and retries
        session_without_features = module_0.build_requests_session(
            raise_for_status=False,
            retry=False,
        )
        sessions.append(session_without_features)

        assert session_without_features.hooks["response"] == []
        assert session_without_features.get_adapter("http://").max_retries.total == 0
        assert session_without_features.get_adapter("https://").max_retries.total == 0

        # Invalid retry configuration
        with pytest.raises(
            ValueError,
            match="retry should be a bool, int or Retry instance",
        ):
            module_0.build_requests_session(retry="invalid")

    finally:
        for created_session in sessions:
            created_session.close()

# Generated at 2026-10-24 06:32:17.151732
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

# Generated at 2026-10-24 06:32:29.774709
# Unit test for function build_requests_session
def test_build_requests_session():
    retry_config = Retry(total=3)

    session = module_0.build_requests_session(
        raise_for_status=True,
        retry=retry_config,
    )

    assert isinstance(session, Session)

    # Verify raise_for_status response hook.
    assert len(session.hooks["response"]) == 1

    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Verify retry configuration for both protocols.
    assert session.adapters["http://"].max_retries is retry_config
    assert session.adapters["https://"].max_retries is retry_config


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_accepts_integer_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    assert session.adapters["http://"].max_retries.total == retry_count
    assert session.adapters["https://"].max_retries.total == retry_count


def test_build_requests_session_without_status_hook_or_retries():
    session = module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks["response"] == []

    # Requests installs default adapters whose retry total is zero.
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 06:32:31.081944
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

# Generated at 2026-10-24 06:32:32.398104
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

# Generated at 2026-10-24 06:32:44.595404
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert isinstance(session.adapters["http://"].max_retries, Retry)
    assert isinstance(session.adapters["https://"].max_retries, Retry)

    # Verify the raise_for_status response hook
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Disable raise_for_status and retries
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
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-24 06:32:45.943918
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

# Generated at 2026-10-24 06:32:54.733863
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:32:56.043589
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:32:57.365795
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

# Generated at 2026-10-24 06:32:58.678322
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

# Generated at 2026-10-24 06:32:59.981764
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

# Generated at 2026-10-24 06:33:01.310282
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:33:02.638410
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

# Generated at 2026-10-24 06:33:03.955396
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

# Generated at 2026-10-24 06:33:05.281224
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

# Generated at 2026-10-24 06:33:06.607017
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

# Generated at 2026-10-24 06:33:07.901883
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

# Generated at 2026-10-24 06:33:09.217223
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:33:10.523198
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

# Generated at 2026-10-24 06:33:11.831914
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

# Generated at 2026-10-24 06:33:13.136805
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

# Generated at 2026-10-24 06:33:14.434448
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

# Generated at 2026-10-24 06:33:15.757600
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

# Generated at 2026-10-24 06:33:17.064309
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

# Generated at 2026-10-24 06:33:19.493873
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:21.903995
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:24.445350
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:26.862899
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:29.276163
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:31.693570
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:34.108002
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:36.526115
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:38.942968
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:33:41.519269
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

# Generated at 2026-10-24 06:33:42.900197
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

# Generated at 2026-10-24 06:33:44.201257
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

# Generated at 2026-10-24 06:34:05.187862
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:34:27.919256
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session()

# Generated at 2026-10-24 06:34:29.220802
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

# Generated at 2026-10-24 06:34:30.529397
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

# Generated at 2026-10-24 06:34:31.838136
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

# Generated at 2026-10-24 06:34:33.166733
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:34.480518
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

# Generated at 2026-10-24 06:34:35.796775
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

# Generated at 2026-10-24 06:34:37.108924
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

# Generated at 2026-10-24 06:34:38.410692
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

# Generated at 2026-10-24 06:34:39.722574
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

# Generated at 2026-10-24 06:34:41.026628
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

# Generated at 2026-10-24 06:34:42.344540
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

# Generated at 2026-10-24 06:34:43.647354
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

# Generated at 2026-10-24 06:34:44.952632
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

# Generated at 2026-10-24 06:34:46.262388
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

# Generated at 2026-10-24 06:34:47.679717
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:49.113700
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

# Generated at 2026-10-24 06:34:50.419621
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:51.758662
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

# Generated at 2026-10-24 06:34:53.068309
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:54.384903
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:55.703299
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

# Generated at 2026-10-24 06:34:57.025700
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

# Generated at 2026-10-24 06:34:58.345925
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:34:59.663202
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

# Generated at 2026-10-24 06:35:00.991845
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

# Generated at 2026-10-24 06:35:02.426314
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

# Generated at 2026-10-24 06:35:03.742138
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

# Generated at 2026-10-24 06:35:06.912757
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:35:09.433056
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:11.939452
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:14.358980
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:16.772055
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:19.188325
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:21.685849
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:24.105171
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:26.518349
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:28.934861
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:31.349665
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:33.764612
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:36.178801
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:38.594938
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:41.009764
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:35:43.539394
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 06:35:44.857371
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:35:46.171942
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:35:47.689487
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

# Generated at 2026-10-24 06:35:49.107305
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

# Generated at 2026-10-24 06:35:51.480832
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

# Generated at 2026-10-24 06:35:52.783068
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

# Generated at 2026-10-24 06:35:54.098499
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

# Generated at 2026-10-24 06:35:55.399639
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:35:56.705716
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

# Generated at 2026-10-24 06:35:58.014213
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

# Generated at 2026-10-24 06:35:59.318663
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

# Generated at 2026-10-24 06:36:00.646669
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

# Generated at 2026-10-24 06:36:01.967663
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

# Generated at 2026-10-24 06:36:03.320678
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

# Generated at 2026-10-24 06:36:10.909911
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:13.326034
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:15.741220
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:18.161658
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:20.570959
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:22.986542
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:25.400447
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:27.819262
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:30.231673
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:32.783476
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:36:35.201616
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:36:37.620207
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:36:40.038249
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:42.447285
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:44.867862
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:47.280137
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:49.693396
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:52.108321
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:54.526152
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:56.942638
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:36:59.358076
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:37:01.771197
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:37:04.188414
# Unit test for function build_requests_session

# Generated at 2026-10-24 06:37:07.127151
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session()

# Generated at 2026-10-24 06:37:08.439728
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

# Generated at 2026-10-24 06:37:09.766008
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

# Generated at 2026-10-24 06:37:19.504680
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

# Generated at 2026-10-24 06:37:20.826558
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

# Generated at 2026-10-24 06:37:22.145241
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:37:23.448865
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:37:24.748888
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

# Generated at 2026-10-24 06:37:26.067060
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

# Generated at 2026-10-24 06:37:27.442535
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:37:28.753493
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

# Generated at 2026-10-24 06:37:30.055680
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

# Generated at 2026-10-24 06:37:32.560822
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:37:34.979776
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:37:37.396002
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:37:57.949438
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

# Generated at 2026-10-24 06:37:59.262770
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

# Generated at 2026-10-24 06:38:00.567880
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:38:01.918304
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:38:03.214977
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:38:04.540439
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

# Generated at 2026-10-24 06:38:05.851964
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

# Generated at 2026-10-24 06:38:07.166474
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

# Generated at 2026-10-24 06:38:08.500370
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert session.get_adapter("http://example.com").max_retries.total == Retry().total

    # raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {} or "response" not in session.hooks

    # retry=False -> no retry adapter mounted
    session = module_0.build_requests_session(retry=False)
    default_adapter = session.get_adapter("https://example.com")
    assert default_adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries is custom_retry

    # retry as invalid type -> ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 06:38:09.810790
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

# Generated at 2026-10-24 06:38:53.443914
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:38:55.857537
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:38:58.273483
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:00.690012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:03.109767
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:05.527512
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:07.940117
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:10.356729
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:12.771422
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:15.185540
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:17.611291
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:20.013279
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:22.431188
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:24.843323
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:27.257298
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:29.672255
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:32.098446
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:34.511472
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:36.926580
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:39:39.732951
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 06:39:41.111293
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

# Generated at 2026-10-24 06:39:42.433492
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

# Generated at 2026-10-24 06:39:43.745896
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

# Generated at 2026-10-24 06:41:09.994121
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

# Generated at 2026-10-24 06:41:11.309125
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

# Generated at 2026-10-24 06:41:12.624604
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

# Generated at 2026-10-24 06:41:13.933339
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

# Generated at 2026-10-24 06:41:15.254122
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

# Generated at 2026-10-24 06:41:17.683789
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:41:20.085263
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:41:22.502059
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:41:25.024204
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:41:27.442077
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 06:41:29.858488
# Unit test for method __call__ of class LoggedFunction