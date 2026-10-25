

# Generated at 2026-10-24 07:20:33.626530
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:36.042296
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:38.456900
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:40.868474
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:20:43.286126
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:20:45.698795
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:20:48.112709
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:50.529208
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:52.944587
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:20:55.361313
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:20:57.776291
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:00.191982
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:02.604567
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:21:05.017530
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:21:07.448450
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 07:21:09.849683
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:12.263925
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:14.679060
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:17.092096
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:19.507641
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:21.922185
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:24.334074
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:26.749353
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:29.181949
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:21:31.596931
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:21:34.014794
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:21:36.625550
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session()

# Generated at 2026-10-24 07:21:37.949285
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

# Generated at 2026-10-24 07:21:39.263912
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

# Generated at 2026-10-24 07:21:40.626607
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

# Generated at 2026-10-24 07:21:41.943026
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

# Generated at 2026-10-24 07:21:43.255124
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

# Generated at 2026-10-24 07:21:44.561791
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

# Generated at 2026-10-24 07:21:45.951884
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

# Generated at 2026-10-24 07:21:47.262631
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

# Generated at 2026-10-24 07:21:48.611798
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

# Generated at 2026-10-24 07:21:49.916084
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

# Generated at 2026-10-24 07:21:51.255057
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

# Generated at 2026-10-24 07:21:52.581588
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

# Generated at 2026-10-24 07:21:54.693176
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

# Generated at 2026-10-24 07:21:56.001827
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

# Generated at 2026-10-24 07:21:57.375725
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

# Generated at 2026-10-24 07:21:58.731555
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

# Generated at 2026-10-24 07:22:01.243313
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:03.796706
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:06.433298
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:08.849131
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:11.266830
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:13.890633
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:16.309170
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:18.724831
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:21.138178
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:23.555891
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:25.968880
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:28.390043
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:30.803898
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:33.216961
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:35.635167
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:22:38.045861
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:40.457880
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:42.869845
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:22:45.282238
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:16.948297
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest import mock


# Generated at 2026-10-24 07:23:19.363534
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:21.775394
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:24.190166
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:26.608274
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:29.023271
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:31.439902
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:33.852389
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:23:36.268138
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:23:38.683243
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:23:41.266354
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:43.677388
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:46.091173
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:48.505054
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:50.923381
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:53.336501
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:23:55.749822
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:23:58.164697
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:00.580683
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:02.994920
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:05.407951
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:07.823428
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:10.237198
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:12.654415
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:15.068569
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:17.482991
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:19.896539
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:22.312412
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:24.730920
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:27.141906
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:29.555984
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:31.970077
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:34.387228
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:36.800803
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:24:39.214290
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:41.628604
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:44.045110
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:24:45.419289
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

# Generated at 2026-10-24 07:24:46.748034
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

# Generated at 2026-10-24 07:24:48.067010
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

# Generated at 2026-10-24 07:24:49.398002
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

# Generated at 2026-10-24 07:24:50.730794
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

# Generated at 2026-10-24 07:24:52.057114
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

# Generated at 2026-10-24 07:24:53.361945
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

# Generated at 2026-10-24 07:24:54.667372
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

# Generated at 2026-10-24 07:24:55.981658
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

# Generated at 2026-10-24 07:24:57.283137
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

# Generated at 2026-10-24 07:24:58.601648
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

# Generated at 2026-10-24 07:25:00.502247
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

# Generated at 2026-10-24 07:25:01.836334
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

# Generated at 2026-10-24 07:25:03.148239
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

# Generated at 2026-10-24 07:25:05.655839
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:08.067639
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:10.484590
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:12.901950
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:15.425065
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:17.842079
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:20.259303
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:22.676389
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:25.094506
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:27.504659
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:29.920534
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:32.338227
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:34.752251
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:37.167646
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:39.583134
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:42.000293
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:44.417765
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:46.832254
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:25:49.250814
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:51.666157
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:54.082636
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:25:58.621828
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:01.265530
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 07:26:02.548927
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

# Generated at 2026-10-24 07:26:03.878928
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

# Generated at 2026-10-24 07:26:05.207306
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

# Generated at 2026-10-24 07:26:06.557334
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

# Generated at 2026-10-24 07:26:07.826548
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

# Generated at 2026-10-24 07:26:09.224939
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

# Generated at 2026-10-24 07:26:10.537356
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

# Generated at 2026-10-24 07:26:11.857112
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

# Generated at 2026-10-24 07:26:13.179510
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

# Generated at 2026-10-24 07:26:18.276594
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

# Generated at 2026-10-24 07:26:19.581999
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

# Generated at 2026-10-24 07:26:22.099184
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:24.514822
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:26.927715
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:29.344472
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:26:31.759749
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:26:34.174911
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:26:36.590932
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:39.003907
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:41.422174
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:43.838954
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:46.257227
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:48.676129
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:51.086485
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:53.501104
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:55.915586
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:26:58.331349
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:00.745107
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:03.159122
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:05.573360
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:08.166877
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():import logging


# Generated at 2026-10-24 07:27:09.491484
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

# Generated at 2026-10-24 07:27:17.166367
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

# Generated at 2026-10-24 07:27:18.490757
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

# Generated at 2026-10-24 07:27:19.795271
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

# Generated at 2026-10-24 07:27:21.106200
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

# Generated at 2026-10-24 07:27:22.433164
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

# Generated at 2026-10-24 07:27:23.783829
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

# Generated at 2026-10-24 07:27:25.104069
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

# Generated at 2026-10-24 07:27:26.423399
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

# Generated at 2026-10-24 07:27:27.732734
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

# Generated at 2026-10-24 07:27:29.059064
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

# Generated at 2026-10-24 07:27:52.087762
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:54.509627
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:56.927815
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:27:59.347386
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:01.768411
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:04.190445
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:07.189642
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:09.618327
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:12.037564
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:14.452948
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:16.864532
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:19.275313
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:21.688284
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:24.104824
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:26.517136
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:28.935980
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:28:31.350065
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:28:33.765820
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:28:36.184519
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:38.601624
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:41.018031
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:43.434955
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:45.854106
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:48.274671
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:50.691135
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:53.107222
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:55.530167
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:28:57.937105
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:00.353727
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:02.769979
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:37.061038
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:39.475826
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:41.891403
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:44.303870
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:46.715511
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:49.130693
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:29:51.546497
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:53.961983
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:56.374928
# Unit test for function build_requests_session

# Generated at 2026-10-24 07:29:58.789432
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:01.202515
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:03.621274
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:06.031776
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:08.445697
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:10.862184
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:13.277449
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:15.693672
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:18.108552
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:20.522765
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:22.937999
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:25.351494
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:27.805780
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:30.181601
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 07:30:32.595522
# Unit test for method __call__ of class LoggedFunction