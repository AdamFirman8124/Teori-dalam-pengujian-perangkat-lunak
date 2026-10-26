

# Generated at 2026-10-25 08:01:08.996769
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:11.446397
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:13.858917
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:16.273790
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:18.737039
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:21.183786
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:23.596776
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:26.010876
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:28.425212
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:30.840249
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:33.253604
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:35.668011
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:01:38.082207
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:40.495747
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:42.910319
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:45.324921
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:47.739061
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:50.153305
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:52.567117
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:01:54.020363
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:01:56.889360
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

# Generated at 2026-10-25 08:02:15.292310
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

# Generated at 2026-10-25 08:02:33.141132
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

# Generated at 2026-10-25 08:02:35.805619
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:38.221774
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:40.633380
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:43.046064
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:45.459535
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:47.872588
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:02:50.288396
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:02:52.699596
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:02:55.114246
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:02:57.819016
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

# Generated at 2026-10-25 08:03:15.755653
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

# Generated at 2026-10-25 08:03:40.775138
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 08:03:43.185617
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:45.598728
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:48.012058
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:50.427164
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:52.882616
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:55.291500
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:03:58.035404
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

# Generated at 2026-10-25 08:04:01.002861
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

# Generated at 2026-10-25 08:04:19.329560
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:20.763103
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:04:23.405715
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:26.041610
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:28.456739
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:30.872412
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:33.287746
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:35.701853
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:38.115969
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:40.533969
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:42.948207
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:45.362866
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:47.777864
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:50.191518
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:52.607887
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:55.022906
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:57.435841
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:04:59.853851
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:05:02.271619
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:05:04.684639
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:05:27.837261
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 08:05:45.859833
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

# Generated at 2026-10-25 08:06:03.671329
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:06:06.091937
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:06:07.627677
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:06:33.373183
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:06:34.805771
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:06:37.675413
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

# Generated at 2026-10-25 08:06:55.798875
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

# Generated at 2026-10-25 08:06:58.329595
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:00.734688
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:03.150254
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:05.563453
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:07.015331
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:07:31.741861
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():messages = []


# Generated at 2026-10-25 08:07:49.660431
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:52.192793
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:54.609307
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:57.024913
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:07:59.438942
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:01.855984
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:04.271063
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:06.686142
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:09.102920
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:11.516181
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:13.934661
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:16.352528
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:18.773987
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:21.191139
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:23.604971
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:26.018180
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:28.432060
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:30.848072
# Unit test for function build_requests_session

# Generated at 2026-10-25 08:08:33.264164
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:35.683354
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:38.097711
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:40.520873
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:42.931217
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:45.343472
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:47.762333
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:50.171838
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:52.587527
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:54.998078
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:57.422602
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:08:59.841146
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:02.257800
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:04.891116
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:06.297407
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:09:32.983962
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock, call


# Generated at 2026-10-25 08:09:35.648581
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:38.065117
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:40.481378
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:42.899371
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:45.311580
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:47.728447
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:50.142901
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:52.556717
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:54.970786
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:57.387957
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:09:59.804605
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:02.218928
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:04.633585
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:07.051146
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:09.468625
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:11.883172
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:14.297101
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:16.715382
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:19.130942
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:21.544366
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:23.961247
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:27.098141
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:29.513695
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:31.928704
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:34.344124
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:36.759975
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:39.183076
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:41.597542
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:44.362419
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-25 08:10:45.892863
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-25 08:10:48.775926
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

# Generated at 2026-10-25 08:10:51.589833
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

# Generated at 2026-10-25 08:11:09.757581
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