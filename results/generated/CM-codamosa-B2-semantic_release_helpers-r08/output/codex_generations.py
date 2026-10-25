

# Generated at 2026-10-24 14:28:26.072288
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:28:28.484508
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:28:30.898258
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:28:33.312965
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:35.725290
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:38.137406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:40.550447
# Unit test for function format_arg

# Generated at 2026-10-24 14:28:42.962948
# Unit test for function format_arg

# Generated at 2026-10-24 14:28:45.769924
# Unit test for function format_arg

# Generated at 2026-10-24 14:28:48.183009
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:50.595593
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:53.008579
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:28:55.423377
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:28:57.836234
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:29:00.248710
# Unit test for constructor of class LoggedFunction

# Generated at 2026-10-24 14:29:02.661484
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:05.072570
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:07.485585
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:09.897891
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:12.310250
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:14.723409
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:17.134957
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:19.547158
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:21.959506
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:24.372150
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:26.785168
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:29.200690
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:31.609595
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:29:34.021901
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:29:36.434933
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:29:38.849840
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:41.263545
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:43.676966
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:29:46.090012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:29:48.502238
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:29:56.246296
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:06.239955
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:30:15.044963
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:30:17.460088
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:19.872874
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:22.446977
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:24.857737
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:27.270752
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:29.682229
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:32.261387
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:34.676196
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:37.094133
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:39.505081
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:41.922375
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:44.332533
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:46.745147
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:49.157979
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:51.571636
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:30:53.984421
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:56.397569
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:30:58.812021
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:01.227535
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:03.641860
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:06.052254
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:08.465591
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:10.879307
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:21.400344
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:22.715079
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:24.369650
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:31:25.816277
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:27.237256
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:28.547037
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:29.863068
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:31.230396
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:32.553583
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:31:33.861625
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:31:35.293295
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:36.658958
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:38.002983
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:31:40.509989
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:43.017335
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:45.437459
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:47.855348
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:50.416321
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:52.830472
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:55.243151
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:31:57.656661
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:00.069354
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:02.482369
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:04.895943
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:07.309033
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:09.722035
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:12.134597
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:14.548112
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:32:26.643972
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import Mock

    # Test: arguments and return value are logged, function metadata preserved

# Generated at 2026-10-24 14:32:27.971043
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:29.301951
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:32:30.929657
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:32.254383
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:33.562476
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:34.884919
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:36.562442
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:37.884906
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:39.215897
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = MagicMock()
    log = LoggedFunction(logger)

    @log
    def add(a, b=0):
        """add doc"""
        return a + b

    assert add(1, b=2) == 3

    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["add(1, b=2)", "add -> 3"]

    # None return value is not logged
    logger.reset_mock()

    @log
    def nothing(x):
        return None

    assert nothing("  spaced  ") is None
    calls = [c.args[0] for c in logger.debug.call_args_list]
    assert calls == ["nothing('spaced')"]

    # functools.wraps metadata preserved
    assert add.__name__ == "add"
    assert add.__doc__ == "add doc"

# Generated at 2026-10-24 14:32:40.551857
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Default: raise_for_status hook installed, default retries enabled
    session = module_0.build_requests_session()
    assert isinstance(session, Session)
    assert "response" in session.hooks
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    # raise_for_status=False: no hooks installed
    session = module_0.build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks

    # retry=False: no custom adapter mounted, default adapter has no retries
    session = module_0.build_requests_session(retry=False)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 0

    # retry as int: Retry configured with that total
    session = module_0.build_requests_session(retry=5)
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

    # retry as Retry instance: used as-is
    custom_retry = Retry(total=3, backoff_factor=0.5)
    session = module_0.build_requests_session(retry=custom_retry)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries is custom_retry

    # Invalid retry type raises ValueError
    try:
        module_0.build_requests_session(retry="yes")
        assert False, "expected ValueError"
    except ValueError:
        pass

# Generated at 2026-10-24 14:32:42.966585
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:45.380004
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:48.033650
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:50.446326
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:52.861719
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:55.273282
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:32:57.685933
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:00.103396
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:02.520017
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:04.935082
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:07.347285
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:09.762996
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:12.342694
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:14.755578
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:17.168358
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:19.579440
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:21.993650
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:24.407164
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:26.818602
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:29.230847
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:31.642696
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:34.054874
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:36.467727
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:38.880277
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:41.293167
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:43.706243
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:46.117839
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:48.529672
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:50.942524
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:53.354393
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:33:55.766075
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:33:58.178492
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:34:00.590876
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:34:03.003650
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:34:05.416259
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:34:07.827354
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:34:10.238397
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:12.649160
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:15.062003
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:17.478251
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:19.893448
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:22.307558
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:24.719143
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:27.131012
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:29.543348
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:31.957444
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:34.371075
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:36.783102
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:39.195287
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:41.608794
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:44.022223
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:46.435015
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:48.849366
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:51.263169
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:53.679080
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:56.089720
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:34:58.534267
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:00.913550
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:03.325900
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:05.738558
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:08.151591
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:10.565041
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:12.978740
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:15.392511
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:17.805663
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:20.222935
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:22.631390
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:25.043843
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:27.457303
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:29.870539
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:32.285257
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:34.701518
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:37.114311
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:39.531130
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:41.946400
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:44.970934
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:47.389109
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:49.800515
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:52.212363
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:54.623289
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:57.036231
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:35:59.448281
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:01.861672
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:04.273187
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:06.686047
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:09.098389
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:11.511179
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:13.923669
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:16.336740
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:18.750174
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:21.162406
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:23.575738
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:25.988950
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:28.401564
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:30.814684
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:33.229601
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:35.642252
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:38.055644
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:40.480112
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:42.892774
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:45.305734
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:47.719895
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:36:50.132778
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:36:52.545820
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:36:54.958890
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:36:59.452570
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:01.865674
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:04.277984
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:06.695580
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:37:09.112045
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:37:11.523378
# Unit test for function build_requests_session

# Generated at 2026-10-24 14:37:13.939638
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:16.352505
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:18.764375
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:21.177831
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:23.590781
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:26.003394
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:37:48.739950
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:38:04.859181
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock

# Generated at 2026-10-24 14:38:29.230922
# Unit test for method __call__ of class LoggedFunction

# Generated at 2026-10-24 14:38:30.666642
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():from unittest.mock import MagicMock