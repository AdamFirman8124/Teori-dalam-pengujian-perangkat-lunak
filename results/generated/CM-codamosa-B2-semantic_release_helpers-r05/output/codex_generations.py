

# Generated at 2026-10-25 04:19:36.252656
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    import logging

    logger = logging.getLogger("test_logger")

    # Test 1: Constructor stores the logger instance
    logged_func = LoggedFunction(logger)
    assert logged_func.logger is logger

    # Test 2: Constructor accepts any logger-like object
    class FakeLogger:
        def debug(self, msg):
            pass

    fake = FakeLogger()
    logged_func2 = LoggedFunction(fake)
    assert logged_func2.logger is fake

    # Test 3: Constructor requires exactly one argument
    try:
        LoggedFunction()  # type: ignore
        assert False, "Expected TypeError for missing logger argument"
    except TypeError:
        pass

    print("All LoggedFunction constructor tests passed!")

# Generated at 2026-10-25 04:19:38.775635
# Unit test for function format_arg

# Generated at 2026-10-25 04:19:41.190307
# Unit test for function format_arg

# Generated at 2026-10-25 04:19:43.606750
# Unit test for function format_arg

# Generated at 2026-10-25 04:19:46.020160
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:19:48.435294
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:19:50.849975
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:19:53.264645
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 04:19:55.681567
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 04:19:58.095995
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 04:20:00.511426
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:07.804079
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:16.904910
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:30.526769
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def repeat(value, count=1):
        invocations.append((value, count))
        return value.strip() * count

    result = repeat(" hello ", count=2)

    assert result == "hellohello"
    assert invocations == [(" hello ", 2)]
    assert repeat.__name__ == "repeat"

    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat -> hellohello"),
    ]

# Generated at 2026-10-25 04:20:33.393588
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:35.921280
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:38.337160
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:40.752470
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:20:43.166947
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:20:45.581729
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:20:47.996224
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:50.412211
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:52.826470
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:20:55.242446
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:20:57.659084
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:21:00.075959
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:21:02.658499
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:21:05.073752
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:21:06.546534
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session(raise_for_status=True, retry=2)

# Generated at 2026-10-25 04:21:16.312614
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def example(name, count=0):
        """Example function."""
        invocations.append((name, count))
        return count + 1

    result = example(" alice ", count=2)

    assert result == 3
    assert invocations == [(" alice ", 2)]

    logger.debug.assert_has_calls(
        [
            call("example('alice', count=2)"),
            call("example -> 3"),
        ]
    )
    assert logger.debug.call_count == 2

    # functools.wraps should preserve function metadata.
    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."

# Generated at 2026-10-25 04:21:30.741715
# Unit test for function build_requests_session
def test_build_requests_session():
    with module_0.build_requests_session() as session:
        assert isinstance(session, Session)

        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        assert isinstance(http_adapter.max_retries, Retry)
        assert isinstance(https_adapter.max_retries, Retry)

        # Verify the raise_for_status response hook.
        response = Response()
        response.status_code = 500
        response.url = "https://example.com"

        with pytest.raises(HTTPError):
            session.hooks["response"][0](response)


def test_build_requests_session_with_retry_count():
    with module_0.build_requests_session(retry=3) as session:
        assert session.get_adapter("http://example.com").max_retries.total == 3
        assert session.get_adapter("https://example.com").max_retries.total == 3


def test_build_requests_session_with_retry_instance():
    retry = Retry(total=4)

    with module_0.build_requests_session(retry=retry) as session:
        assert session.get_adapter("https://example.com").max_retries is retry


def test_build_requests_session_without_status_hook():
    with module_0.build_requests_session(raise_for_status=False) as session:
        assert session.hooks["response"] == []


def test_build_requests_session_rejects_invalid_retry():
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 04:21:35.240596
# Unit test for function format_arg
def test_format_arg():
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello world  ") == "'hello world'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(3.14) == "3.14"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 04:21:39.872584
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

# Generated at 2026-10-25 04:21:54.707373
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    implementation = Mock(return_value={"ok": True})

    def example(value, count=0):
        return implementation(value, count=count)

    logged_example = LoggedFunction(logger).__call__(example)

    result = logged_example("  test value  ", count=2)

    assert result == {"ok": True}
    assert logged_example.__name__ == "example"
    implementation.assert_called_once_with("  test value  ", count=2)
    assert logger.debug.call_args_list == [
        call("example('test value', count=2)"),
        call("example -> {'ok': True}"),
    ]

# Generated at 2026-10-25 04:21:57.134803
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:21:59.554143
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:22:01.970971
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:22:04.384758
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:06.798949
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:09.214127
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:11.628071
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:14.042454
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:22.037409
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:22:30.743432
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_calls = []

    @LoggedFunction(logger)
    def repeat(value, count=1):
        function_calls.append((value, count))
        return value * count

    result = repeat(" hello ", count=2)

    assert result == " hello  hello "
    assert function_calls == [(" hello ", 2)]
    assert repeat.__name__ == "repeat"

    assert logger.debug.call_args_list == [
        call("repeat('hello', count=2)"),
        call("repeat ->  hello  hello "),
    ]

# Generated at 2026-10-25 04:22:40.558409
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_spy = Mock(return_value=5)

    @LoggedFunction(logger)
    def add(value, increment=0):
        return function_spy(value, increment=increment)

    result = add(2, increment=3)

    assert result == 5
    assert add.__name__ == "add"  # functools.wraps preserves metadata
    function_spy.assert_called_once_with(2, increment=3)
    assert logger.debug.call_args_list == [
        call("add(2, increment=3)"),
        call("add -> 5"),
    ]

# Generated at 2026-10-25 04:22:57.265259
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import Mock

    # Default configuration
    session = module_0.build_requests_session()
    try:
        assert isinstance(session, Session)

        http_retries = session.get_adapter("http://").max_retries
        https_retries = session.get_adapter("https://").max_retries
        assert isinstance(http_retries, Retry)
        assert isinstance(https_retries, Retry)

        # Verify the raise_for_status response hook
        response = Mock()
        assert len(session.hooks["response"]) == 1
        session.hooks["response"][0](response)
        response.raise_for_status.assert_called_once_with()
    finally:
        session.close()

    # Disable raise_for_status and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    try:
        assert session.hooks["response"] == []

        # Requests' standard adapters use zero retries by default.
        assert session.get_adapter("http://").max_retries.total == 0
        assert session.get_adapter("https://").max_retries.total == 0
    finally:
        session.close()

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    try:
        assert session.get_adapter("http://").max_retries.total == 3
        assert session.get_adapter("https://").max_retries.total == 3
    finally:
        session.close()

    # Explicit Retry instance
    configured_retry = Retry(
        total=5,
        connect=2,
        status=3,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    session = module_0.build_requests_session(retry=configured_retry)
    try:
        assert session.get_adapter("http://").max_retries is configured_retry
        assert session.get_adapter("https://").max_retries is configured_retry
    finally:
        session.close()

    # Invalid retry configuration
    try:
        module_0.build_requests_session(retry="invalid")
    except ValueError as exc:
        assert str(exc) == "retry should be a bool, int or Retry instance."
    else:
        raise AssertionError("Expected ValueError for an invalid retry value")

# Generated at 2026-10-25 04:22:59.793406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:23:02.208277
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:23:04.622597
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:23:07.038920
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:23:09.452892
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:23:11.868602
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:23:14.283460
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:23:20.687501
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock


# Generated at 2026-10-25 04:23:28.087783
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
    logger.debug.assert_has_calls(
        [
            call("add(2, increment=3)"),
            call("add -> 5"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 04:23:38.006175
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def sample(value, increment=0):
        """Sample function."""
        return len(value.strip()) + increment

    result = sample("  abc  ", increment=2)

    assert result == 5
    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Sample function."
    assert logger.debug.call_args_list == [
        call("sample('abc', increment=2)"),
        call("sample -> 5"),
    ]

    # A None return value should not produce a result log.
    logger.reset_mock()

    @LoggedFunction(logger)
    def no_result():
        return None

    assert no_result() is None
    logger.debug.assert_called_once_with("no_result()")

# Generated at 2026-10-25 04:23:49.693705
# Unit test for function build_requests_session
def test_build_requests_session():
    # Default configuration
    session = module_0.build_requests_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1
    assert isinstance(session.get_adapter("http://"), HTTPAdapter)
    assert isinstance(session.get_adapter("https://"), HTTPAdapter)
    assert isinstance(session.get_adapter("http://").max_retries, Retry)

    # Verify the response hook invokes raise_for_status()
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Integer retry count
    session = module_0.build_requests_session(retry=3)
    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Explicit Retry instance
    retry = Retry(total=5, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=retry)
    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry

    # Disabled status hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)
    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Invalid retry value
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 04:23:59.832578
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received_arguments = []

    def example(value, count=1):
        received_arguments.append((value, count))
        return "result"

    decorated = LoggedFunction(logger)(example)

    result = decorated("  hello  ", count=2)

    assert result == "result"
    assert received_arguments == [("  hello  ", 2)]
    assert decorated.__name__ == "example"
    logger.debug.assert_has_calls(
        [
            call("example('hello', count=2)"),
            call("example -> result"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 04:24:02.253890
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:04.678471
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:07.093295
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:09.507363
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:11.938730
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:14.351773
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:16.767317
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:19.183720
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:21.598760
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:24.015291
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:26.433488
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:28.847173
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:24:31.264302
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:33.683908
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:36.099163
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:38.515658
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:40.932675
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:43.345858
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:45.767810
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:48.179900
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:50.599291
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:53.013576
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:55.427617
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:24:57.843377
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:00.258508
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:02.673276
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:05.088061
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:07.503556
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:09.918338
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:12.334884
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:14.750154
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:17.165285
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:25:24.471714
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 04:25:34.961669
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def example(value, enabled=False):
        invocations.append((value, enabled))
        return "result"

    result = example("  value  ", enabled=True)

    assert result == "result"
    assert invocations == [("  value  ", True)]
    assert example.__name__ == "example"

    assert logger.debug.call_args_list == [
        call("example('value', enabled=True)"),
        call("example -> result"),
    ]

# Generated at 2026-10-25 04:25:44.485418
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(left, right, *, offset=0):
        return left + right + offset

    result = add(2, 3, offset=4)

    assert result == 9
    assert add.__name__ == "add"
    logger.debug.assert_has_calls(
        [
            call("add(2, 3, offset=4)"),
            call("add -> 9"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 04:25:56.466735
# Unit test for function build_requests_session
def test_build_requests_session():
    retry_config = Retry(total=3)

    session = module_0.build_requests_session(
        raise_for_status=True,
        retry=retry_config,
    )

    assert isinstance(session, Session)

    # Both protocols use the configured retry policy.
    http_adapter = session.get_adapter("http://")
    https_adapter = session.get_adapter("https://")

    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert http_adapter.max_retries is retry_config

    # The response hook invokes raise_for_status.
    response = Mock()
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_accepts_integer_retry_count(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    assert session.get_adapter("https://").max_retries.total == retry_count


def test_build_requests_session_without_raise_for_status_hook():
    session = module_0.build_requests_session(raise_for_status=False)

    assert session.hooks.get("response", []) == []


def test_build_requests_session_without_retries():
    session = module_0.build_requests_session(retry=False)

    # Requests' standard adapter has retries disabled by default.
    assert session.get_adapter("https://").max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry_value():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 04:26:06.506667
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def add(value, increment=0):
        return value + increment

    result = add(2, increment=3)

    assert result == 5
    logger.debug.assert_has_calls(
        [
            call("add(2, increment=3)"),
            call("add -> 5"),
        ]
    )
    assert logger.debug.call_count == 2

    # functools.wraps should preserve the decorated function's metadata.
    assert add.__name__ == "add"

# Generated at 2026-10-25 04:26:17.663528
# Unit test for function build_requests_session
def test_build_requests_session():
    sessions = []

    try:
        # Custom Retry instance is installed for both HTTP and HTTPS.
        retry = Retry(total=3)
        session = module_0.build_requests_session(raise_for_status=True, retry=retry)
        sessions.append(session)

        assert session.adapters["http://"].max_retries is retry
        assert session.adapters["https://"].max_retries is retry

        # The response hook invokes raise_for_status.
        response = Mock()
        for hook in session.hooks["response"]:
            hook(response)

        response.raise_for_status.assert_called_once_with()

        # An integer creates a Retry object with the requested total.
        session_with_count = module_0.build_requests_session(retry=5)
        sessions.append(session_with_count)

        assert session_with_count.adapters["http://"].max_retries.total == 5
        assert session_with_count.adapters["https://"].max_retries.total == 5

        # Retry and status checking can both be disabled.
        session_without_options = module_0.build_requests_session(
            raise_for_status=False,
            retry=False,
        )
        sessions.append(session_without_options)

        assert session_without_options.hooks["response"] == []
        assert session_without_options.adapters["http://"].max_retries.total == 0
        assert session_without_options.adapters["https://"].max_retries.total == 0

        # Unsupported retry configurations are rejected.
        with pytest.raises(
            ValueError,
            match="retry should be a bool, int or Retry instance",
        ):
            module_0.build_requests_session(retry="invalid")

    finally:
        for created_session in sessions:
            created_session.close()

# Generated at 2026-10-25 04:26:20.079863
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:26:28.209463
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:26:33.272311
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:26:44.209550
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    @LoggedFunction(logger)
    def multiply(value, multiplier=1):
        """Multiply two values."""
        return value * multiplier

    result = multiply(3, multiplier=4)

    assert result == 12
    assert logger.debug.call_args_list == [
        call("multiply(3, multiplier=4)"),
        call("multiply -> 12"),
    ]

    # functools.wraps should preserve the decorated function's metadata.
    assert multiply.__name__ == "multiply"
    assert multiply.__doc__ == "Multiply two values."

# Generated at 2026-10-25 04:26:56.063248
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    from unittest.mock import Mock

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

    # Disable status hook and retries
    session = module_0.build_requests_session(raise_for_status=False, retry=False)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0

    # Configure retries using an integer
    session = module_0.build_requests_session(retry=3)

    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3

    # Configure retries using an existing Retry instance
    retry_config = Retry(total=5)
    session = module_0.build_requests_session(retry=retry_config)

    assert session.get_adapter("http://").max_retries is retry_config
    assert session.get_adapter("https://").max_retries is retry_config

    # Reject unsupported retry values
    with pytest.raises(
        ValueError, match="retry should be a bool, int or Retry instance"
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 04:26:58.480017
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:00.894339
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:03.308787
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:05.723218
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:08.138846
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:10.553306
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:12.967735
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:27:15.383470
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:27:17.804458
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:27:20.223673
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:22.637118
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:25.051624
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:27.467166
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:29.882322
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:32.296928
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:34.714821
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:41.837224
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:27:47.876371
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock


# Generated at 2026-10-25 04:27:58.322196
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

    logger.reset_mock()

    @LoggedFunction(logger)
    def no_result(value):
        return None

    assert no_result("  test  ") is None
    logger.debug.assert_called_once_with("no_result('test')")

# Generated at 2026-10-25 04:28:08.874349
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    function_mock = Mock()

    @LoggedFunction(logger)
    def example(name, count=1):
        function_mock(name, count)
        return 42

    result = example("  Alice  ", count=2)

    assert result == 42
    assert example.__name__ == "example"
    function_mock.assert_called_once_with("  Alice  ", 2)
    logger.debug.assert_has_calls(
        [
            call("example('Alice', count=2)"),
            call("example -> 42"),
        ]
    )
    assert logger.debug.call_count == 2

# Generated at 2026-10-25 04:28:11.290758
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:13.852683
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:16.268771
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:18.683925
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:21.101998
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:23.675110
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:26.091835
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:28:28.508562
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:28:30.924324
# Unit test for function build_requests_session

# Generated at 2026-10-25 04:28:33.341213
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:35.753319
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:43.064407
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:28:53.710881
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    received = []

    @LoggedFunction(logger)
    def add(left, right=0):
        """Add two values."""
        received.append((left, right))
        return left + right

    result = add(1, right=2)

    assert result == 3
    assert received == [(1, 2)]

    logger.debug.assert_has_calls(
        [
            call("add(1, right=2)"),
            call("add -> 3"),
        ]
    )
    assert logger.debug.call_count == 2

    # functools.wraps should preserve the decorated function's metadata.
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two values."

# Generated at 2026-10-25 04:29:02.527350
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    received_arguments = []

    @LoggedFunction(logger)
    def example(value, count, enabled=False):
        received_arguments.append((value, count, enabled))
        return "completed"

    result = example("  test  ", 3, enabled=True)

    assert result == "completed"
    assert received_arguments == [("  test  ", 3, True)]
    assert example.__name__ == "example"
    assert logger.debug.call_args_list == [
        call("example('test', 3, enabled=True)"),
        call("example -> completed"),
    ]

# Generated at 2026-10-25 04:29:20.961777
# Unit test for function build_requests_session
def test_build_requests_session():
    retry_policy = Retry(total=3)

    session = module_0.build_requests_session(
        raise_for_status=True,
        retry=retry_policy,
    )

    assert isinstance(session, Session)

    # Verify the response hook calls raise_for_status().
    response = Mock()
    assert len(session.hooks["response"]) == 1
    session.hooks["response"][0](response)
    response.raise_for_status.assert_called_once_with()

    # Verify both protocols use the configured retry policy.
    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries is retry_policy


@pytest.mark.parametrize("retry_count", [1, 3, 5])
def test_build_requests_session_with_integer_retry(retry_count):
    session = module_0.build_requests_session(retry=retry_count)

    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert adapter.max_retries.total == retry_count


def test_build_requests_session_with_default_retry():
    session = module_0.build_requests_session(retry=True)

    expected_total = Retry().total
    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == expected_total


def test_build_requests_session_without_retry_or_status_hook():
    session = module_0.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks["response"] == []

    # Requests' default adapters have retries disabled.
    for url in ("http://example.com", "https://example.com"):
        assert session.get_adapter(url).max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry():
    with pytest.raises(
        ValueError,
        match="retry should be a bool, int or Retry instance",
    ):
        module_0.build_requests_session(retry="invalid")

# Generated at 2026-10-25 04:29:23.376893
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:29:25.789019
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:29:28.216110
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:29:30.639637
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:29:33.053717
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 04:29:35.471319
# Unit test for method __call__ of class LoggedFunction