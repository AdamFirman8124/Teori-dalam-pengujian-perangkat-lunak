

# Generated at 2026-10-25 10:29:58.601692
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

# Generated at 2026-10-25 10:30:00.034697
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = logging.getLogger("test_LoggedFunction")
    logged = LoggedFunction(logger)

    assert isinstance(logged, LoggedFunction)
    assert logged.logger is logger

# Generated at 2026-10-25 10:30:03.209776
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

# Generated at 2026-10-25 10:30:04.743522
# Unit test for constructor of class LoggedFunction
def test_LoggedFunction():
    logger = logging.getLogger("test_LoggedFunction")
    logged = LoggedFunction(logger)

    assert isinstance(logged, LoggedFunction)
    assert logged.logger is logger

# Generated at 2026-10-25 10:30:06.176369
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

# Generated at 2026-10-25 10:30:16.127110
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

# Generated at 2026-10-25 10:30:18.895766
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

# Generated at 2026-10-25 10:30:23.688544
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

# Generated at 2026-10-25 10:30:26.517298
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:28.936368
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:31.654842
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:34.217452
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:36.631676
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:39.046571
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:41.463217
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:43.880037
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:46.463835
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:49.039087
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:51.453709
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:53.865862
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:30:56.284669
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:30:58.777962
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:01.123868
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:03.539636
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:05.953847
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:08.372470
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:10.792500
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:31:13.218838
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:31:15.632186
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:31:18.056265
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:20.469112
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:22.922672
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:25.342734
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:27.767229
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:30.184219
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:32.603812
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:35.021067
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:37.438703
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:31:41.112926
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

# Generated at 2026-10-25 10:32:02.992754
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

# Generated at 2026-10-25 10:32:09.073130
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

# Generated at 2026-10-25 10:32:12.000227
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:13.564752
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 10:32:16.212384
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:32:18.640576
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:32:21.327495
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:32:23.709813
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:26.320185
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:28.732730
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:31.150779
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:33.564053
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:35.978498
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:38.729559
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:41.149235
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:43.565498
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:45.981082
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:48.399692
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:50.814486
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:53.230758
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:55.649531
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:32:58.066909
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:00.488994
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:02.903202
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:05.317729
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:07.733270
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:10.151004
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:12.565908
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:14.980871
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:17.396118
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:19.810981
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:22.229085
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:24.644208
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:27.153345
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:29.556796
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:31.972106
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:34.385503
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:36.800705
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:39.213207
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:41.626816
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:33:44.040637
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:46.458081
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:48.874023
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:51.288794
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:53.702748
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:56.117137
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:33:58.532070
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:00.949861
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:03.362149
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:05.776121
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:08.207241
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:10.621456
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:13.033970
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:15.517505
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:17.894940
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:20.309483
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:22.724742
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:25.140832
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:27.561838
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:30.008924
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:32.419458
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:34.835040
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:37.249775
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:39.669563
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:42.086570
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:44.499954
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:46.915330
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:34:49.330307
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:51.748066
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:54.169003
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:56.576346
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:34:58.991953
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:35:01.407075
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:35:03.820200
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:06.235859
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:08.650484
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:11.069572
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:13.483208
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:15.895299
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:18.308568
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:20.723228
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:23.138977
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:25.550907
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:27.966012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:30.380321
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:32.793327
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:35.210225
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:37.622469
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:40.038386
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:42.455552
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:44.870229
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:47.285376
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:35:49.699653
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:35:52.112923
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:35:54.530619
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:56.947282
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:35:59.363383
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:01.779874
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:04.194595
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:06.608673
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:09.024847
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:11.442597
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:13.854189
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:16.284239
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:22.200871
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:23.697747
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 10:36:48.305563
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:50.056221
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 10:36:52.791585
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

# Generated at 2026-10-25 10:36:55.614606
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:36:58.028272
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:00.444892
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:02.862065
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:05.275269
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:07.688309
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:10.103449
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:12.519401
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:14.937425
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:17.353934
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:37:19.766054
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:37:22.181548
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:37:48.207791
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:37:52.905068
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 10:37:57.221301
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

# Generated at 2026-10-25 10:38:00.090310
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

# Generated at 2026-10-25 10:38:04.061564
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:06.723458
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:09.409265
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:12.175479
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:38:14.590088
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:38:17.007398
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:38:19.421845
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:21.842182
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:24.257304
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:30.338502
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

# Generated at 2026-10-25 10:38:33.144811
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:34.525503
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 10:38:52.403029
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

# Generated at 2026-10-25 10:38:54.965251
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:38:57.419551
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:00.217934
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:02.642488
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:05.058955
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:07.473605
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:09.888212
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:12.305642
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:14.718138
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:17.132389
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:39:19.546763
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:39:21.963050
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:39:27.266619
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:29.680504
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:32.098922
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 10:39:34.512811
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:39:36.926798
# Unit test for function build_requests_session

# Generated at 2026-10-25 10:39:39.338956
# Unit test for function build_requests_session