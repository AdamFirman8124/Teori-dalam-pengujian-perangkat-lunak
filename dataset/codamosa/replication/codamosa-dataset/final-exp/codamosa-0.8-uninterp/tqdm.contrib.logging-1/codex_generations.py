

# Generated at 2022-06-14 13:27:49.448217
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():

    import logging
    from tqdm import tqdm, trange

    LOG = logging.getLogger(__name__)

    # Test for the basic "logging redirect"
    with tqdm_logging_redirect():
        for i in trange(5):
            if i == 1:
                LOG.info("console logging redirected to `tqdm.write()`")

    # Test for the "logging redirect" with custom loggers
    with tqdm_logging_redirect(loggers=[LOG]):
        for i in trange(5):
            if i == 1:
                LOG.info("console logging redirected to `tqdm.write()`")

    # Test for the "logging redirect" with custom parameters

# Generated at 2022-06-14 13:27:58.697473
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import io
    import logging
    import sys
    import re
    from contextlib import redirect_stdout

    from ..concurrent import thread_map
    from ..std import tqdm as std_tqdm

    from .test_logging import log_run_and_check
    from .test_multiprocessing import get_system_error_codes
    from .test_multiprocessing import _try_multiprocess_run as try_multiprocess_run

    # Examples of logs that should be redirected

# Generated at 2022-06-14 13:28:08.059589
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: (...) -> None
    from unittest import TestCase

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    tqdm_handler = _TqdmLoggingHandler()
    stream_mock = patch.object(tqdm_handler, 'stream', autospec=True).start()
    tqdm_mock = patch('tqdm.contrib.logging._tqdm').start()

    test_cases = [
        (Exception, False),
        (KeyboardInterrupt, True),
        (SystemExit, True),
    ]
    for exception_type, should_raise in test_cases:
        with TestCase.assertRaises(TestCase, exception_type if should_raise else None):
            tqdm_mock.write.side

# Generated at 2022-06-14 13:28:14.148712
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from ..std import StringIO

    # Setup fake stream and logging handlers
    fake_stream = StringIO()
    logger = logging.getLogger(__name__)
    logger.addHandler(_TqdmLoggingHandler())
    logger.setLevel(logging.DEBUG)

    # Setup logger configuration
    logging.basicConfig(level=logging.DEBUG, stream=fake_stream)

    # Call emit
    logger.debug('Test')

    # Assert that expected text is present
    assert 'Test' in fake_stream.getvalue()
    assert 'DEBUG' in fake_stream.getvalue()



# Generated at 2022-06-14 13:28:21.189972
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from .main import tqdm
    with tqdm_logging_redirect(tqdm_class=tqdm) as pbar:
        assert pbar._instances.get(sys.stderr, pbar) == pbar
        logging.info('logging redirected to `tqdm.write()`')
        assert pbar._instances.get(sys.stderr, pbar) == pbar
        assert pbar.n == 1

# Generated at 2022-06-14 13:28:32.368527
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    class TqdmMock(std_tqdm):
        def __init__(self, *args, **kwargs):
            super(TqdmMock, self).__init__(*args, **kwargs)
            self.write_to = []
            self.called = 0

        def write(self, s):
            self.called += 1
            self.write_to.append(s)

    with tqdm_logging_redirect(loggers=[logger], tqdm_class=TqdmMock) as pbar:
        assert isinstance(pbar, TqdmMock)
        assert (not pbar.called)

        logger.info("Hello world")

# Generated at 2022-06-14 13:28:41.166095
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import trange
    from tqdm import tqdm
    import logging
    import six
    import sys
    import time

    class MyConsoleHandler(logging.StreamHandler):
        def __init__(self):
            super(MyConsoleHandler, self).__init__()
            self.buffer = ''  # type: Optional[str]

        def emit(self, record):
            self.buffer = self.format(record)
            super(MyConsoleHandler, self).emit(record)

        def flush(self):
            """Flush buffer"""
            # It seems we need to flush this specific handler
            # and not ``logging.flush()``. See issue #536.
            self.buffer = None
            sys.stdout.flush()


# Generated at 2022-06-14 13:28:44.672080
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:53.888499
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import os
    import tempfile
    try:
        from tqdm import tqdm
        from tqdm.contrib.logging import logging_redirect_tqdm  # NOQA
    except ImportError:
        return
    try:
        from unittest.mock import patch  # NOQA
    except ImportError:
        from mock import patch  # NOQA
    _ = patch("tqdm.tqdm.tqdm")
    with tempfile.TemporaryFile("w+") as f:
        with logging_redirect_tqdm([logging.root], stream=f):
            logging.error("foo")
            logging.info("bar")
            logging.info("baz")
        f.seek(0)
        out = f.read()

# Generated at 2022-06-14 13:29:01.897632
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    import logging, sys

    tmp_io = StringIO()
    tmp_logger = logging.getLogger(__name__)
    tmp_logger.setLevel(logging.INFO)
    tmp_handler = _TqdmLoggingHandler()
    tmp_handler.stream = tmp_io
    tmp_logger.addHandler(tmp_handler)

    # Test raising exception and calling handleError
    # We are no longer allowed to catch bare `except`
    # see https://github.com/tqdm/tqdm/issues/800
    # assert raises(KeyboardInterrupt, tmp_handler.emit, logging.makeLogRecord({'msg': "test"}))
    # assert raises(SystemExit, tmp_handler.emit, logging.makeLogRecord({'msg': "test"}))
   

# Generated at 2022-06-14 13:29:13.867605
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:29:18.243490
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from .main import tqdm
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(total=1) as pbar:
        logging.info("test")
    assert pbar.n == 1  # make sure the unit test can be executed twice


# Fixture for testing 3rd-party libs' logging behavior with `tqdm_notebook`

# Generated at 2022-06-14 13:29:24.572093
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm, tqdm_logging_redirect

    # test logger
    logging.basicConfig(level=logging.INFO)

    # test logging_redirect_tqdm()
    with logging_redirect_tqdm():
        for i in range(5):
            logging.info("test1")
            if i == 2:
                logging.info("test2")
    # logging restored

    # test tqdm_logging_redirect()
    with tqdm_logging_redirect():
        for i in range(5):
            logging.info("test3")
            if i == 2:
                logging.info("test4")
    # logging restored

# Generated at 2022-06-14 13:29:27.574444
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    LOG = logging.getLogger(__name__)
    LOG.info("this is logging message")
    with logging_redirect_tqdm(loggers=[LOG]):
        LOG.info("this would be logged to tqdm.write()")
    LOG.info("this is logging message")


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:29:38.531522
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from unittest import mock

# Generated at 2022-06-14 13:29:42.280983
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Test the function logging_redirect_tqdm
    """
    loggers = [logging.root]
    with logging_redirect_tqdm(loggers=loggers):
        for i in range(10):
            logging.info(str(i))


# Generated at 2022-06-14 13:29:49.635347
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm() as pbar:
        for i in pbar(range(9)):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored



# Generated at 2022-06-14 13:29:57.738733
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.test_utils import closing_test

    LOG = logging.getLogger(__name__)

    def test():
        logging.basicConfig(level=logging.INFO)

        with closing_test():
            with tqdm_logging_redirect():  # default: tqdm=tqdm, loggers=logging.root
                for i in trange(9):
                    if i == 4:
                        LOG.info("console logging redirected to `tqdm.write()`")

    test()

# Generated at 2022-06-14 13:30:06.901750
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging_output = ""

    class MockLoggingHandler(logging.Handler):
        def emit(self, record):
            nonlocal logging_output
            logging_output += self.format(record) + "\n"

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.addHandler(MockLoggingHandler())

    with tqdm_logging_redirect(desc="tqdm_logging_redirect test", total=10) as pbar:
        pbar.set_description("progress")
        assert logging_output == ""
        logger.info("info")
        assert logging_output == "info\n"
        logger.warning("warning")
        assert logging_output == "info\nwarning\n"



# Generated at 2022-06-14 13:30:16.349875
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from .tests_helper import closing, StringIO
    class TestTqdm(object):
        def __init__(self, *args, **kwargs):
            pass

        def write(self, msg, file):
            file.write(msg)
            file.write('\n')

    tqdm_logging_handler = _TqdmLoggingHandler(tqdm_class=TestTqdm)
    tqdm_logging_handler.stream = StringIO()
    with closing(tqdm_logging_handler):
        tqdm_logging_handler.emit(logging.LogRecord(
            name="default", level=logging.INFO, pathname=".", lineno=1, msg="Test",
            args=(), exc_info=None))
    assert tqdm_logging_handler.stream

# Generated at 2022-06-14 13:30:33.896318
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """Unit test method of class _TqdmLoggingHandler"""
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    _handler = _TqdmLoggingHandler()
    _handler.flush = mock.Mock()
    _handler.stream = mock.Mock()
    _handler.tqdm_class.write = mock.Mock()
    _handler.handleError = mock.Mock()
    _handler.format = mock.Mock()

    # testing exception logging.raiseExceptions = True
    with mock.patch('logging.raiseExceptions', True):
        record = mock.Mock()
        _handler.format.return_value = "hello"
        _handler.emit(record)
        _handler.tqdm_class.write.assert_called_once

# Generated at 2022-06-14 13:30:42.258613
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        fake_pbar = Mock()

        def fake_pbar_update():
            pass

        fake_pbar.update = fake_pbar_update

# Generated at 2022-06-14 13:30:45.889886
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:30:52.969596
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    log = logging.getLogger(__name__)
    with logging_redirect_tqdm() as l:
        log.debug("test 1")
        log.info("test 2")
        log.warning("test 3")
        log.error("test 4")
        log.critical("test 5")
    assert l == [], "logging_redirect_tqdm() produces no physical output"

# Generated at 2022-06-14 13:30:57.275353
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        logging.root.handlers[:] = []
        logger = logging.getLogger('logging_redirect_tqdm_test')
        with logging_redirect_tqdm([logger]):
            logger.info('this is a test')
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:31:02.753936
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():  # pylint: disable=missing-docstring
    logging.root.handlers = []
    logger = logging.getLogger('test_logger')
    logger.handlers = []
    try:
        logger.setLevel(logging.INFO)
        with tqdm_logging_redirect():
            logger.info('unit test')
    finally:
        logger.handlers = []

# Generated at 2022-06-14 13:31:13.871759
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Test for function logging_redirect_tqdm.
    """
    # Setup logging
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.INFO)
    sh.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(sh)

    # Check function
    tqdm_handler = _TqdmLoggingHandler(std_tqdm)
    tqdm_handler.setFormatter(sh.formatter)
    tqdm_handler.stream = sh.stream

# Generated at 2022-06-14 13:31:18.344514
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import sys
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        LOG.info('testing logging_redirect_tqdm')



# Generated at 2022-06-14 13:31:25.299380
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import std_tqdm

    log = logging.getLogger(__name__)
    std_tqdm.write("console output restored")
    with logging_redirect_tqdm(loggers=[log]):
        std_tqdm.write("console output redirected to tqdm.write()")
        log.info("console output redirected to tqdm.write()")
        log.error("console output redirected to tqdm.write()")

# Generated at 2022-06-14 13:31:31.608797
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    logging.basicConfig(level=logging.DEBUG)
    test_log = logging.getLogger(__name__ + ".test__TqdmLoggingHandler_emit")
    test_log.handlers = [_TqdmLoggingHandler()]
    test_log.debug('Debug message')
    test_log.info('Info message')
    test_log.warning('Warning message')
    test_log.error('Error message')
    test_log.critical('Critical message')



# Generated at 2022-06-14 13:31:54.668912
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from io import StringIO

    test_string = 'TEST'

    orig_stderr = sys.stderr
    sys.stderr = StringIO()


# Generated at 2022-06-14 13:31:59.660584
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Example usecase"""
    import logging
    from tqdm import trange
    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored



# Generated at 2022-06-14 13:32:06.308526
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(
        [1, 2, 3],
        total=3,
        file=sys.stdout,
        loggers=[logging.getLogger('test_tqdm_logging_redirect')]
    ) as pbar:
        for _ in range(3):
            logging.info("test")
            pbar.update()



# Generated at 2022-06-14 13:32:15.027408
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: () -> None
    """
    Test that the _TqdmLoggingHandler emits the record using tqdm.write.
    """
    import sys
    import io
    import unittest
    import logging

    # use a StreamHandler as mock object to intercept the output of tqdm.write
    handler = logging.StreamHandler(sys.stdout)
    dummy_logger = logging.getLogger(__name__)
    dummy_logger.addHandler(handler)
    dummy_logger.setLevel(logging.DEBUG)

    # the record to be logged
    record = logging.LogRecord(
        name="test_logger", level=logging.INFO,
        fn="test.py", lno=23, msg="TEST", args=None, exc_info=False)

    # set stdout to

# Generated at 2022-06-14 13:32:21.641353
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from io import StringIO
    import logging
    from tqdm.contrib import logging_redirect_tqdm

    log = logging.getLogger()
    log.setLevel(logging.INFO)
    _stream = StringIO()
    hdl = logging.StreamHandler(_stream)
    hdl.setFormatter(logging.Formatter('%(message)s'))  # nosec
    log.handlers = [hdl]
    with logging_redirect_tqdm():
        log.info('hello')
    assert _stream.getvalue() == 'hello\n'



# Generated at 2022-06-14 13:32:29.775536
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    import logging
    from tqdm import trange
    from . import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored



# Generated at 2022-06-14 13:32:41.181196
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    LOG = logging.getLogger(__name__)

    LOG.debug("debug")
    assert(len(LOG.handlers) == 1)
    assert(logging.root.handlers[0].stream == sys.stderr)

    with tqdm_logging_redirect(total=100) as pbar:
        LOG.debug("debug")
        assert(len(LOG.handlers) == 1)
        # assert(logging.root.handlers[0].stream == pbar)
        LOG.info("info")
        LOG.error("error")
        LOG.critical("critical")

    # Test that logging is correctly restored
    assert(len(LOG.handlers) == 1)

# Generated at 2022-06-14 13:32:47.675392
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .main import FakeTqdm

    loggers = [logging.getLogger('tqdm')]
    with logging_redirect_tqdm(loggers):
        loggers[0].warning('THIS IS A TEST MESSAGE')
    assert not FakeTqdm.write_set.isdisjoint(['THIS IS A TEST MESSAGE'])



# Generated at 2022-06-14 13:32:54.364907
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    try:
        from tests_tqdm.utils import closing, _progbar
    except ImportError:
        return

    with closing(open('test.txt', 'w')) as out:
        with _progbar(100, file=out,
                      loggers=[logging.getLogger()]) as progress:
            progress.update(10)
        assert '\r10/100' in out.read()


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:02.579855
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # Suppress logging.warning messages
    def fxn():
        _test_logging_redirect()
    import warnings
    from unittest.mock import patch
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with patch('logging.warning') as mock_warn:
            fxn()
    # Verify logging redirected to `tqdm.write()`
    assert mock_warn.call_args[0][0] == "console logging redirected to `tqdm.write()`"



# Generated at 2022-06-14 13:33:37.177121
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from ..utils import _supports_unicode
    from .. import tgrange, tnrange
    from ..std import tqdm as std_tqdm

    if not _supports_unicode:
        return

    def _test_logging_redirect_tqdm(
        tqdm_class=std_tqdm,  # type: Type
        loggers=None  # type: List[logging.Logger]
    ):
        if loggers is None:
            loggers = [logging.root]

# Generated at 2022-06-14 13:33:40.690129
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:33:48.524843
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    LOG = logging.getLogger(__name__)
    # Clear all logging handlers from root logger
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    assert root_logger.handlers == []

    # Create a console handler for root logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Assert console handler is found

# Generated at 2022-06-14 13:33:55.819467
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    from .gui import tqdm
    from .std import tqdm as std_tqdm
    import logging
    tqdms = [tqdm, std_tqdm]
    for tqdm_class in tqdms:
        with tqdm_logging_redirect(
                total=1, tqdm_class=tqdm_class) as pbar:
            pbar.update(1)
        assert pbar.n == 1  # type: ignore

# Generated at 2022-06-14 13:33:57.448530
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():

    # import logging
    logging_redirect_tqdm()

# Generated at 2022-06-14 13:34:07.980815
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    def patched_tqdm_write(message, file):
        assert message == 'message'
        assert file == sys.stderr

    log = logging.getLogger('test_logging_redirect_tqdm')

    handler = logging.StreamHandler(stream=sys.stderr)
    log.addHandler(handler)

    log.info('message')
    with patch("tqdm.contrib.logging._TqdmLoggingHandler.write",
               side_effect=patched_tqdm_write):
        with logging_redirect_tqdm():
            log.info('message')
        log.info('message')



# Generated at 2022-06-14 13:34:12.040300
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with tqdm_logging_redirect() as tqdm_redirect:
        tqdm_redirect.write("A message")
    with tqdm_logging_redirect(ncols=100) as tqdm_redirect:
        tqdm_redirect.write("A message")



# Generated at 2022-06-14 13:34:20.074396
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import tqdm

    def my_print(x):  # pragma: no cover
        print(x)

    with logging_redirect_tqdm():
        my_print('First print')
        logging.basicConfig(level=logging.INFO)
        logging.info('Basic logging')
        with tqdm(range(3), desc="foo", leave=False) as t:
            for i in t:
                if i == 1:
                    my_print('Second print')
                    logging.info('With tqdm')
        my_print('Third print')
        logging.info('No tqdm')
        logging.info('No tqdm')

# Generated at 2022-06-14 13:34:27.817408
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from time import sleep

    # reset global state
    std_tqdm.set_lock(False)
    std_tqdm.set_lock(True)
    std_tqdm.disable = False

    log = logging.getLogger(__name__)
    log.handlers.clear()
    log.setLevel(logging.INFO)

    with tqdm_logging_redirect():
        log.info('some info')
        log.debug('some debug')  # not written
        log.info('some info')
        with tqdm_logging_redirect(loggers=[log]):
            log.info('some info')
        log.info('some info')
        sleep(0.5)  # force-flush

    assert log.hasHandlers()

# Generated at 2022-06-14 13:34:32.517838
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logger.info('middle')
        logger.warning('final')

# Generated at 2022-06-14 13:35:30.872849
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
                iterable=[i for i in range(9)],
                desc="console logging redirected to `tqdm.write()`",
        ) as pbar:
            for i in pbar:
                if i in {3, 6}:
                    LOG.info("{:d}".format(i))

# Generated at 2022-06-14 13:35:38.017845
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    def zprint(msg):
        print(msg, flush=True)  # logging.info(msg)

    def zlogger(msg):
        log.info(msg)

    log = logging.getLogger(__name__)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
        for i in range(9):
            if i == 4:
                zlogger("this should print with tqdm")
            zprint("this should print with logging.info")



# Generated at 2022-06-14 13:35:43.281776
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import logging
    from tqdm import trange
    with tqdm_logging_redirect(total=9, desc='tqdm'):
        for i in trange(9):
            if i == 4:
                LOG = logging.getLogger(__name__)
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:35:48.824832
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm
    """
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:35:57.289277
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # Setup
    tqdm_handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    tqdm_stdout = "This is stdout\n"
    tqdm_stderr = "This is stderr\n"

    # Test

# Generated at 2022-06-14 13:36:02.458509
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: () -> None
    """
    Unit test for method `emit` of class `_TqdmLoggingHandler`.
    """
    # local import to avoid circular import
    from ..std import tqdm

    LOG = logging.getLogger('test_logger')
    orig_handlers = LOG.handlers
    try:
        LOG.info('Hello world')  # let's keep the original format
        assert not tqdm.write.called
        handler = _TqdmLoggingHandler()
        handler.setLevel(logging.INFO)
        LOG.addHandler(handler)
        LOG.info('Hello world')
        assert tqdm.write.called
    finally:
        LOG.handlers = orig_handlers

# Generated at 2022-06-14 13:36:04.628796
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:36:10.572508
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with tqdm_logging_redirect(desc='Test', total=9, file=None) as pbar:
        for i in range(9):
            if i == 4:
                print('console logging redirected to `tqdm.write()`')
    assert pbar.n == 9
    assert pbar.last_print_n == 1


_logging_context_redirect = tqdm_logging_redirect

# Generated at 2022-06-14 13:36:17.798274
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import unittest
    import io
    import logging
    import tqdm

    class MyTestCase(unittest.TestCase):
        def test_something(self):
            with io.StringIO() as buff:
                with tqdm_logging_redirect(
                    file=buff, mininterval=0, miniters=1,
                ):
                    logging.warning("hello world!")
                self.assertTrue("hello world" in buff.getvalue())


# Generated at 2022-06-14 13:36:27.356801
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Test the context manager to redirect logging to tqdm.

    Note that the redirection actually takes place only the first time that a
    logging function is called while in the context manager.
    """
    import logging
    from tqdm import trange
    from .logging import tqdm_logging_redirect as tlr

    # Create a logger and define a simple logging handler
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)
    LOG.addHandler(logging.NullHandler())

    # Create a second logger to test that logger=loggers is optional
    LOG2 = logging.getLogger('tqdm.contrib.logging.logging_redirect_tqdm')
    LOG2.setLevel(logging.DEBUG)