

# Generated at 2026-10-25 09:40:42.811303
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = logging.getLogger("test_LoggedFunction")
    logged = LoggedFunction(logger)

    assert isinstance(logged, LoggedFunction)
    assert logged.logger is logger

# Generated at 2026-10-25 09:40:44.345802
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = logging.getLogger("test_LoggedFunction")
    logged = LoggedFunction(logger)

    assert isinstance(logged, LoggedFunction)
    assert logged.logger is logger

# Generated at 2026-10-25 09:40:45.779013
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = logging.getLogger("test_LoggedFunction")
    logged = LoggedFunction(logger)

    assert isinstance(logged, LoggedFunction)
    assert logged.logger is logger

# Generated at 2026-10-25 09:40:50.285492
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    from unittest.mock import patch

    # 1. Default session (raise_for_status=True, retry=True)
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # 2. raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}
    assert "response" not in session.hooks

    # 3. retry=False -> no adapter customization, default max_retries
    session = module_0.build_requests_session(retry=False)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter.max_retries.total == 0

    # 4. retry=True -> default Retry configuration mounted on both prefixes
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter.max_retries, Retry)
    assert isinstance(https_adapter.max_retries, Retry)
    assert http_adapter is https_adapter

    # 5. retry as integer -> Retry with total set to that integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # 6. retry as Retry instance -> the same configuration is used
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry
    assert adapter.max_retries.total == 3
    assert adapter.max_retries.backoff_factor == 0.5

    # 7. Invalid retry type -> ValueError
    try:
        module_0.build_requests_session(retry="not-a-retry")
        raised = False
    except ValueError:
        raised = True
    assert raised, "expected ValueError for invalid retry type"

    # 8. raise_for_status hook actually raises on 4xx/5xx responses
    class FakeResponse:
        status_code = 500
        reason = "Internal Server Error"

        def raise_for_status(self):
            raise Exception("HTTP 500")

    hook_response = FakeResponse()
    try:
        for hook in session.hooks.get("response", []):
            hook(hook_response)
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    # session here was built with raise_for_status=True via retry=custom_retry path
    # rebuild explicitly to make the check unambiguous
    session = module_0.build_requests_session(raise_for_status=True)
    try:
        for hook in session.hooks["response"]:
            hook(FakeResponse())
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    assert raised, "expected raise_for_status hook to raise on 500"

    # 9. Hook does nothing on a successful response
    class FakeOKResponse:
        status_code = 200

        def raise_for_status(self):
            return None

    for hook in session.hooks["response"]:
        assert hook(FakeOKResponse()) is None

# Generated at 2026-10-25 09:40:52.927827
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 09:40:55.593829
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 09:40:58.358507
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 09:41:01.243863
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:03.956912
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:06.369968
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:08.786276
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:11.202072
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:13.619487
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:41:16.034154
# Unit test for function format_arg

# Generated at 2026-10-25 09:41:18.448270
# Unit test for function format_arg

# Generated at 2026-10-25 09:41:25.923636
# Unit test for function format_arg
def test_format_arg():assert module_0.format_arg("hello") == "'hello'"

# Generated at 2026-10-25 09:41:35.342348
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    from unittest.mock import patch

    # 1. Default session (raise_for_status=True, retry=True)
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # 2. raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}
    assert "response" not in session.hooks

    # 3. retry=False -> no adapter customization, default max_retries
    session = module_0.build_requests_session(retry=False)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter.max_retries.total == 0

    # 4. retry=True -> default Retry configuration mounted on both prefixes
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter.max_retries, Retry)
    assert isinstance(https_adapter.max_retries, Retry)
    assert http_adapter is https_adapter

    # 5. retry as integer -> Retry with total set to that integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # 6. retry as Retry instance -> the same configuration is used
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry
    assert adapter.max_retries.total == 3
    assert adapter.max_retries.backoff_factor == 0.5

    # 7. Invalid retry type -> ValueError
    try:
        module_0.build_requests_session(retry="not-a-retry")
        raised = False
    except ValueError:
        raised = True
    assert raised, "expected ValueError for invalid retry type"

    # 8. raise_for_status hook actually raises on 4xx/5xx responses
    class FakeResponse:
        status_code = 500
        reason = "Internal Server Error"

        def raise_for_status(self):
            raise Exception("HTTP 500")

    hook_response = FakeResponse()
    try:
        for hook in session.hooks.get("response", []):
            hook(hook_response)
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    # session here was built with raise_for_status=True via retry=custom_retry path
    # rebuild explicitly to make the check unambiguous
    session = module_0.build_requests_session(raise_for_status=True)
    try:
        for hook in session.hooks["response"]:
            hook(FakeResponse())
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    assert raised, "expected raise_for_status hook to raise on 500"

    # 9. Hook does nothing on a successful response
    class FakeOKResponse:
        status_code = 200

        def raise_for_status(self):
            return None

    for hook in session.hooks["response"]:
        assert hook(FakeOKResponse()) is None

# Generated at 2026-10-25 09:41:57.460597
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

# Generated at 2026-10-25 09:42:18.860912
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:42:21.731501
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:42:23.120086
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 09:42:46.406457
# Unit test for function format_arg
def test_format_arg():
    # str: quoted and stripped
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("  hello world  ") == "'hello world'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg("   ") == "''"

    # non-str: str(value)
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(0) == "0"
    assert module_0.format_arg(-1.5) == "-1.5"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 09:42:47.731348
# Unit test for function format_arg
def test_format_arg():
    # str: quoted and stripped
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("  hello world  ") == "'hello world'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg("   ") == "''"

    # non-str: str(value)
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(0) == "0"
    assert module_0.format_arg(-1.5) == "-1.5"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 09:42:52.654288
# Unit test for function format_arg
def test_format_arg():
    # str: quoted and stripped
    assert module_0.format_arg("hello") == "'hello'"
    assert module_0.format_arg("  hello  ") == "'hello'"
    assert module_0.format_arg("  hello world  ") == "'hello world'"
    assert module_0.format_arg("") == "''"
    assert module_0.format_arg("   ") == "''"

    # non-str: str(value)
    assert module_0.format_arg(42) == "42"
    assert module_0.format_arg(0) == "0"
    assert module_0.format_arg(-1.5) == "-1.5"
    assert module_0.format_arg(True) == "True"
    assert module_0.format_arg(None) == "None"
    assert module_0.format_arg([1, 2]) == "[1, 2]"

# Generated at 2026-10-25 09:42:55.069493
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:42:57.484632
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:00.132860
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:02.897518
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:05.312152
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:07.729164
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:10.140873
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:12.557874
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:14.975351
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:17.390498
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:20.090978
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:22.515656
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:24.927797
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:27.345637
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:29.761457
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:32.178314
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:34.594041
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:37.010893
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:39.428460
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:41.850192
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:44.264662
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:43:46.678536
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:49.091903
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:51.509331
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:53.922646
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:56.336087
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:43:58.750688
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:01.169457
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:03.582096
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:06.102730
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:08.489126
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:10.904343
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:13.323414
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:15.740322
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:18.152414
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:20.567773
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:22.984472
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:25.401151
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:27.818194
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:30.231941
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:32.645875
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:35.063329
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:37.480608
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:39.899397
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:42.312214
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:44.730586
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:47.147038
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:49.564662
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:44:51.984121
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:54.395603
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:56.812196
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:44:59.226925
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:01.644194
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:04.061275
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:06.473399
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:08.889613
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:11.303037
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:13.722081
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:16.139537
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:18.551014
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:20.970260
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:23.386487
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:25.805403
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:45:28.621779
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    from unittest.mock import patch

    # 1. Default session (raise_for_status=True, retry=True)
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # 2. raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}
    assert "response" not in session.hooks

    # 3. retry=False -> no adapter customization, default max_retries
    session = module_0.build_requests_session(retry=False)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter.max_retries.total == 0

    # 4. retry=True -> default Retry configuration mounted on both prefixes
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter.max_retries, Retry)
    assert isinstance(https_adapter.max_retries, Retry)
    assert http_adapter is https_adapter

    # 5. retry as integer -> Retry with total set to that integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # 6. retry as Retry instance -> the same configuration is used
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry
    assert adapter.max_retries.total == 3
    assert adapter.max_retries.backoff_factor == 0.5

    # 7. Invalid retry type -> ValueError
    try:
        module_0.build_requests_session(retry="not-a-retry")
        raised = False
    except ValueError:
        raised = True
    assert raised, "expected ValueError for invalid retry type"

    # 8. raise_for_status hook actually raises on 4xx/5xx responses
    class FakeResponse:
        status_code = 500
        reason = "Internal Server Error"

        def raise_for_status(self):
            raise Exception("HTTP 500")

    hook_response = FakeResponse()
    try:
        for hook in session.hooks.get("response", []):
            hook(hook_response)
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    # session here was built with raise_for_status=True via retry=custom_retry path
    # rebuild explicitly to make the check unambiguous
    session = module_0.build_requests_session(raise_for_status=True)
    try:
        for hook in session.hooks["response"]:
            hook(FakeResponse())
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    assert raised, "expected raise_for_status hook to raise on 500"

    # 9. Hook does nothing on a successful response
    class FakeOKResponse:
        status_code = 200

        def raise_for_status(self):
            return None

    for hook in session.hooks["response"]:
        assert hook(FakeOKResponse()) is None

# Generated at 2026-10-25 09:45:31.348715
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    from unittest.mock import patch

    # 1. Default session (raise_for_status=True, retry=True)
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # 2. raise_for_status=False -> no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert session.hooks == {}
    assert "response" not in session.hooks

    # 3. retry=False -> no adapter customization, default max_retries
    session = module_0.build_requests_session(retry=False)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert http_adapter.max_retries.total == 0

    # 4. retry=True -> default Retry configuration mounted on both prefixes
    session = module_0.build_requests_session(retry=True)
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter.max_retries, Retry)
    assert isinstance(https_adapter.max_retries, Retry)
    assert http_adapter is https_adapter

    # 5. retry as integer -> Retry with total set to that integer
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # 6. retry as Retry instance -> the same configuration is used
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry
    assert adapter.max_retries.total == 3
    assert adapter.max_retries.backoff_factor == 0.5

    # 7. Invalid retry type -> ValueError
    try:
        module_0.build_requests_session(retry="not-a-retry")
        raised = False
    except ValueError:
        raised = True
    assert raised, "expected ValueError for invalid retry type"

    # 8. raise_for_status hook actually raises on 4xx/5xx responses
    class FakeResponse:
        status_code = 500
        reason = "Internal Server Error"

        def raise_for_status(self):
            raise Exception("HTTP 500")

    hook_response = FakeResponse()
    try:
        for hook in session.hooks.get("response", []):
            hook(hook_response)
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    # session here was built with raise_for_status=True via retry=custom_retry path
    # rebuild explicitly to make the check unambiguous
    session = module_0.build_requests_session(raise_for_status=True)
    try:
        for hook in session.hooks["response"]:
            hook(FakeResponse())
        raised = False
    except Exception as e:
        raised = True
        assert "HTTP 500" in str(e)
    assert raised, "expected raise_for_status hook to raise on 500"

    # 9. Hook does nothing on a successful response
    class FakeOKResponse:
        status_code = 200

        def raise_for_status(self):
            return None

    for hook in session.hooks["response"]:
        assert hook(FakeOKResponse()) is None

# Generated at 2026-10-25 09:46:00.868754
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

# Generated at 2026-10-25 09:46:03.284735
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:46:05.884945
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:46:08.299089
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:46:10.713549
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:13.139010
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:15.547354
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:17.960690
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:20.374640
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:22.789410
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:25.207498
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:27.621174
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:46:44.577581
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session(raise_for_status=True, retry=2)


# Generated at 2026-10-25 09:46:48.014770
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

# Generated at 2026-10-25 09:47:08.142955
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

# Generated at 2026-10-25 09:47:10.813211
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:13.232143
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:15.649855
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:18.093418
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:20.508453
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:22.922707
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:25.336103
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:27.749934
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:30.163553
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:32.577232
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:34.991003
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:37.403406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:39.819890
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:42.272255
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:44.687166
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:47.100670
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:47:49.512401
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:47:51.926791
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:47:54.347649
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:56.758481
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:47:59.174122
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:01.588258
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:04.002955
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:06.417953
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:08.828879
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:11.243593
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:13.659995
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:16.074955
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:18.484849
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:20.904098
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:38.869060
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:48:40.334453
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 09:49:00.580193
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

# Generated at 2026-10-25 09:49:03.323121
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:05.737321
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:08.152358
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:10.569905
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:13.260346
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:15.919663
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:18.334194
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:20.748272
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:23.399033
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:25.814153
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:49:28.227698
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:49:30.642920
# Unit test for function build_requests_session

# Generated at 2026-10-25 09:49:33.302990
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:35.721116
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:38.134206
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:40.548226
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:42.963157
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:45.376806
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:47.795203
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:50.232320
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:52.645160
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:55.058722
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:57.475593
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:49:59.892147
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:50:02.305099
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:50:04.719764
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:50:07.133242
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 09:50:40.315475
# Unit test for method __call__ of class LoggedFunction