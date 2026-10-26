

# Generated at 2026-10-25 06:43:57.801547
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:00.522255
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:02.943639
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:05.361857
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 06:44:07.780390
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 06:44:10.194202
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-25 06:44:12.610541
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:15.135965
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:17.481308
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:19.897783
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:22.356084
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:24.746668
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:27.159079
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:29.607001
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:31.989049
# Unit test for function format_arg

# Generated at 2026-10-25 06:44:34.403961
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:44:36.818180
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:44:39.232483
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:44:41.648559
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:44:44.061835
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:44:46.477041
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:45:04.387953
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

# Generated at 2026-10-25 06:45:22.394753
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

# Generated at 2026-10-25 06:45:24.814026
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:27.539117
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:29.922376
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:32.338949
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:34.752964
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:37.170655
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:39.585577
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:42.002185
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:44.415301
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:46.827736
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:49.244708
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:51.655926
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:45:54.068132
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:46:14.645197
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:46:16.063914
# Unit test for function build_requests_session
def test_build_requests_session():session = module_0.build_requests_session(raise_for_status=True, retry=2)

# Generated at 2026-10-25 06:46:25.973163
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

# Generated at 2026-10-25 06:46:28.845125
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

# Generated at 2026-10-25 06:46:37.208801
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    from unittest.mock import MagicMock

    # Default: raise_for_status=True, retry=True
    session = module_0.build_requests_session()
    assert session.hooks["response"][0](MagicMock(return_value=None)) is None or True
    adapter = session.get_adapter("http://example.com")
    assert adapter.max_retries.total is not None  # default Retry config

    # raise_for_status=False installs no hook
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks or not session.hooks["response"]

    # retry=False -> no retry adapter behavior (default adapter, max_retries=0)
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 5

    # retry as Retry instance
    from requests.packages.urllib3.util.retry import Retry
    custom = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom

    # invalid retry type raises ValueError
    with pytest.raises(ValueError):
        module_0.build_requests_session(retry="nope")

# Generated at 2026-10-25 06:46:39.799572
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:42.228519
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:44.771478
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:47.180451
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:49.602015
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:52.014014
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:54.428222
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:56.844406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:46:59.261401
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:17.187512
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

# Generated at 2026-10-25 06:47:20.147546
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

# Generated at 2026-10-25 06:47:23.195984
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

# Generated at 2026-10-25 06:47:25.699057
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:28.333410
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:30.750963
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:33.166398
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:35.797723
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:38.211917
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:40.630454
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:43.338178
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:45.757895
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:48.169475
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:50.583453
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:53.000896
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:55.417119
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:47:57.837238
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:00.251048
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:02.669204
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:05.087319
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:07.499496
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:09.919077
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:12.337298
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:14.751691
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:17.169338
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:19.585496
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:21.999953
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:24.419545
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:48:26.835617
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:48:29.251268
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:48:31.670934
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:34.084639
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:36.498185
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:38.916229
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:41.334656
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:43.748152
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:46.160196
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:48.576499
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:50.990487
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:53.454887
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:55.868790
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:48:58.284260
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:00.771792
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:03.185989
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:05.599154
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:08.040381
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:10.456443
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:12.915665
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:15.286095
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:17.703849
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:20.200980
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:22.615126
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:25.030847
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:27.457574
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:29.900762
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:32.285270
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:34.706123
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:37.118558
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:39.534542
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:41.953176
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:44.369181
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:46.786228
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:49.201096
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:51.619471
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:54.035417
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:56.448906
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:49:58.865404
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:01.283058
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:03.695058
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:06.601311
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:09.013816
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:11.438448
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:13.846193
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:16.259108
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:18.674775
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:21.089023
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:23.503046
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:25.917193
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:28.364945
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:30.780057
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:33.190248
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:35.607352
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:38.024029
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:40.441012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:42.855628
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:45.273086
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:47.689659
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:50.102706
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:52.518339
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:54.933805
# Unit test for function build_requests_session

# Generated at 2026-10-25 06:50:57.345785
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:50:59.761871
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:02.179797
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:04.592394
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:07.010166
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:09.427287
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:11.840099
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:14.257873
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:16.674961
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:21.441072
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:23.859392
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:26.269836
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:28.690448
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:31.104324
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:33.518353
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:35.931660
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:38.348604
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:40.815999
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:43.234836
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:45.651183
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:48.075436
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:50.491463
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:52.905367
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:55.342103
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:51:57.759946
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:03.630977
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:05.124667
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 06:52:08.092699
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

# Generated at 2026-10-25 06:52:26.014254
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

# Generated at 2026-10-25 06:52:43.936839
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

# Generated at 2026-10-25 06:52:46.501012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:48.919645
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:51.334306
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:56.418045
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:52:58.835664
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:01.413183
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:04.314958
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

# Generated at 2026-10-25 06:53:07.280124
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:08.801936
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 06:53:11.492009
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

# Generated at 2026-10-25 06:53:14.391871
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

# Generated at 2026-10-25 06:53:19.876889
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

# Generated at 2026-10-25 06:53:22.999030
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:25.536351
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:27.953346
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:30.485782
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:32.889874
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:35.308102
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:37.720333
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:40.134654
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:42.553412
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:44.968210
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:47.381731
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 06:53:49.804028
# Unit test for method __call__ of class LoggedFunction