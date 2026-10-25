

# Generated at 2026-10-24 07:33:43.358155
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

# Generated at 2026-10-24 07:33:44.678780
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

# Generated at 2026-10-24 07:33:46.041682
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

# Generated at 2026-10-24 07:33:48.462667
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:33:51.110283
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:33:53.661908
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:33:56.074340
# Unit test for function format_arg

# Generated at 2026-10-24 07:33:58.488877
# Unit test for function format_arg

# Generated at 2026-10-24 07:34:00.906242
# Unit test for function format_arg

# Generated at 2026-10-24 07:34:03.326243
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:05.739751
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:08.152972
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:09.541739
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

# Generated at 2026-10-24 07:34:10.868652
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

# Generated at 2026-10-24 07:34:12.189037
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

# Generated at 2026-10-24 07:34:13.489661
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

# Generated at 2026-10-24 07:34:14.793631
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

# Generated at 2026-10-24 07:34:16.103129
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

# Generated at 2026-10-24 07:34:17.468295
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

# Generated at 2026-10-24 07:34:18.780826
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

# Generated at 2026-10-24 07:34:20.113795
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

# Generated at 2026-10-24 07:34:21.429178
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

# Generated at 2026-10-24 07:34:22.795722
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

# Generated at 2026-10-24 07:34:24.107339
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

# Generated at 2026-10-24 07:34:25.566843
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

# Generated at 2026-10-24 07:34:26.878694
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

# Generated at 2026-10-24 07:34:28.265872
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

# Generated at 2026-10-24 07:34:30.761991
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:33.288198
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:35.911748
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:38.329211
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:40.742317
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:43.337990
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:34:45.752831
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:48.170481
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:50.582836
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:52.997495
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:55.409728
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:34:57.825169
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:00.241838
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:02.655749
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:05.388283
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:07.796128
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:35:10.214502
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:35:12.626777
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:35:15.040885
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:17.466114
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:19.878661
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:21.337275
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

# Generated at 2026-10-24 07:35:22.791984
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

# Generated at 2026-10-24 07:35:24.100519
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

# Generated at 2026-10-24 07:35:25.507856
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

# Generated at 2026-10-24 07:35:26.822824
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

# Generated at 2026-10-24 07:35:28.229364
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

# Generated at 2026-10-24 07:35:29.533001
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

# Generated at 2026-10-24 07:35:31.713072
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

# Generated at 2026-10-24 07:35:33.026772
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

# Generated at 2026-10-24 07:35:34.347465
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

# Generated at 2026-10-24 07:35:35.669753
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

# Generated at 2026-10-24 07:35:36.976579
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

# Generated at 2026-10-24 07:35:38.293128
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

# Generated at 2026-10-24 07:35:39.613799
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

# Generated at 2026-10-24 07:35:40.917257
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

# Generated at 2026-10-24 07:35:43.335122
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:45.747790
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:48.165512
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:50.654269
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:53.072175
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:55.670623
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:35:58.318256
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:00.734360
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:03.147828
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:05.565622
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:07.980682
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:10.396450
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:12.807062
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:15.231144
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:17.659829
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:20.062874
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:22.476486
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:24.895617
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:27.314565
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:36:29.977632
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session()

# Generated at 2026-10-24 07:36:31.283132
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

# Generated at 2026-10-24 07:36:32.597963
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

# Generated at 2026-10-24 07:36:33.921010
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

# Generated at 2026-10-24 07:36:35.248878
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

# Generated at 2026-10-24 07:36:36.579756
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

# Generated at 2026-10-24 07:36:37.985793
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

# Generated at 2026-10-24 07:36:39.301586
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

# Generated at 2026-10-24 07:36:40.631525
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

# Generated at 2026-10-24 07:36:41.930121
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

# Generated at 2026-10-24 07:36:43.285103
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

# Generated at 2026-10-24 07:36:44.591208
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

# Generated at 2026-10-24 07:36:45.897737
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

# Generated at 2026-10-24 07:36:47.210763
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

# Generated at 2026-10-24 07:36:48.719156
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

# Generated at 2026-10-24 07:36:51.230271
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:53.732937
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:56.145781
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:36:58.853322
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:01.269905
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:03.682622
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:06.097694
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:08.510289
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:10.925434
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:13.344267
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:15.897029
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:18.309695
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:20.732095
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:23.148230
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:25.565710
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:27.977188
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:30.394183
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:32.979028
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 07:37:34.276445
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

# Generated at 2026-10-24 07:37:35.596102
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

# Generated at 2026-10-24 07:37:36.900592
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

# Generated at 2026-10-24 07:37:38.217263
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

# Generated at 2026-10-24 07:37:39.521202
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

# Generated at 2026-10-24 07:37:41.694860
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

# Generated at 2026-10-24 07:37:43.073051
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

# Generated at 2026-10-24 07:37:44.394263
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

# Generated at 2026-10-24 07:37:45.712221
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

# Generated at 2026-10-24 07:37:47.014555
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

# Generated at 2026-10-24 07:37:48.334543
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

# Generated at 2026-10-24 07:37:49.632155
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

# Generated at 2026-10-24 07:37:51.694965
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

# Generated at 2026-10-24 07:37:54.194702
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:56.697982
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:37:59.200621
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:01.613965
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:04.029450
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:06.444839
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:11.287654
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:13.702865
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:16.119178
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:18.535693
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:38:20.953413
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:38:23.369431
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:38:25.784377
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:28.200070
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:30.612069
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:33.024933
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:35.442578
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:37.858680
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:40.275419
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:38:56.720230
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest import mock


# Generated at 2026-10-24 07:38:58.030429
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

# Generated at 2026-10-24 07:38:59.345191
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

# Generated at 2026-10-24 07:39:00.672476
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

# Generated at 2026-10-24 07:39:02.043389
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

# Generated at 2026-10-24 07:39:03.368992
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

# Generated at 2026-10-24 07:39:10.786045
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

# Generated at 2026-10-24 07:39:12.146826
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

# Generated at 2026-10-24 07:39:13.504403
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

# Generated at 2026-10-24 07:39:14.824593
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

# Generated at 2026-10-24 07:39:16.129256
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

# Generated at 2026-10-24 07:39:17.438507
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

# Generated at 2026-10-24 07:39:19.938106
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:22.449477
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:24.954915
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:27.464700
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:29.877439
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:32.293467
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:34.709802
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:37.271271
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:39.773126
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:42.188346
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:44.605094
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:39:47.023812
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:40:01.789853
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:40:04.213520
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:40:06.616525
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:40:08.188850
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

# Generated at 2026-10-24 07:40:09.515972
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

# Generated at 2026-10-24 07:40:10.843943
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

# Generated at 2026-10-24 07:40:12.214594
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

# Generated at 2026-10-24 07:40:13.619215
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

# Generated at 2026-10-24 07:40:14.936639
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

# Generated at 2026-10-24 07:40:16.589800
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

# Generated at 2026-10-24 07:40:17.894709
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

# Generated at 2026-10-24 07:40:19.202700
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

# Generated at 2026-10-24 07:40:50.482407
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

# Generated at 2026-10-24 07:40:51.789066
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

# Generated at 2026-10-24 07:40:53.096998
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

# Generated at 2026-10-24 07:40:54.421676
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

# Generated at 2026-10-24 07:40:55.727215
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

# Generated at 2026-10-24 07:40:57.056424
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

# Generated at 2026-10-24 07:40:58.376630
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

# Generated at 2026-10-24 07:40:59.699570
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

# Generated at 2026-10-24 07:41:01.008274
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

# Generated at 2026-10-24 07:41:02.332810
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

# Generated at 2026-10-24 07:42:08.604570
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

# Generated at 2026-10-24 07:42:09.918860
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

# Generated at 2026-10-24 07:42:11.301466
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

# Generated at 2026-10-24 07:42:12.615351
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

# Generated at 2026-10-24 07:42:13.922258
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

# Generated at 2026-10-24 07:42:15.223088
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

# Generated at 2026-10-24 07:42:16.589509
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

# Generated at 2026-10-24 07:42:17.947303
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

# Generated at 2026-10-24 07:42:19.243572
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

# Generated at 2026-10-24 07:42:20.561552
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