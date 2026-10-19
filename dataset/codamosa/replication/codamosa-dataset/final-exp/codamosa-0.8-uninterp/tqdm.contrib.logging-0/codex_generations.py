

# Generated at 2022-06-14 13:27:46.027936
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class TqdmLoggingHandlerTest:

        def emit(self, record):
            self.msg = record.msg
            self.args = record.args

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    handler = _TqdmLoggingHandler(tqdm_class=TqdmLoggingHandlerTest)
    logger.handlers = [handler]
    logger.info("test message {}".format(1))
    assert handler.msg == "test message 1"
    assert handler.args == ()

    # Cause an exception with args
    logger.info("test message {}", 1)
    assert handler.msg == "test message %s"
    assert handler.args == (1,)

# Generated at 2022-06-14 13:27:54.655321
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    import tqdm

    def mock_sleep(sec):
        time.sleep(sec / 10)

    loggers = [logging.getLogger(__name__)]
    print('loggers = %s' % loggers)

    with tqdm_logging_redirect(total=100,
                               logger=loggers,
                               desc='test_tqdm_logging_redirect'):
        for i in range(100):
            mock_sleep(1)
            logging.info('i = %d' % i)


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:28:00.519109
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pylint: disable=redefined-outer-name
    from ..std import tqdm
    LOG = logging.getLogger(__name__)
    loggers = [LOG]
    with logging_redirect_tqdm(loggers=loggers):
        for _ in tqdm(range(9), desc='logging'):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:28:08.676730
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """
    Test that logging is redirected to tqdm.
    """
    import logging
    import sys
    import traceback
    logging.basicConfig(level=logging.INFO)
    try:
        with tqdm_logging_redirect(desc="logging to tqdm") as pbar:
            logging.info("console logging redirected to `tqdm.write()`")
            assert pbar.total == 1
            assert pbar.n == 1
    except SystemExit:
        raise
    except BaseException:
        print('An error occured:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise AssertionError('Unexpected error')

# Generated at 2022-06-14 13:28:13.021986
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import tqdm

    # TODO: fix this
    logging.basicConfig(level=logging.INFO)

    with tqdm_logging_redirect(unit="B") as pbar:
        pbar.update(1048576)
        logging.info("test")
        logging.warning("test")
        pbar.update(2048)



# Generated at 2022-06-14 13:28:18.258008
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logger = logging.getLogger('tqdm')
    logger.setLevel(logging.INFO)
    with tqdm_logging_redirect() as pbar:
        logger.info('Test message')
        assert 'Test message\n' == pbar.write.call_args[0][0]

# Generated at 2022-06-14 13:28:26.134633
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    assert logging.root.handlers[0].stream == sys.stderr
    with logging_redirect_tqdm():
        logging.info('1st log')
        assert logging.root.handlers[0].stream == sys.stderr
        with tqdm_logging_redirect(total=3, unit='it', file=sys.stderr, unit_scale=True):
            logging.info('2nd log')
            with logging_redirect_tqdm():
                logging.info('3rd log')
            logging.info('4th log')
        assert logging.root.handlers[0].stream == sys.stderr
        logging.info('5th log')

# Generated at 2022-06-14 13:28:33.127842
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    This function tests logging_redirect_tqdm() function.
    """
    from tqdm.contrib.logging import logging_redirect_tqdm
    import logging
    import sys

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    with logging_redirect_tqdm():
        logger.info("redirected console logs to tqdm!")
    sys.stdout.write("\n")



# Generated at 2022-06-14 13:28:41.671871
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import (
        tqdm_logging_redirect, _is_console_logging_handler)

    logging.basicConfig(level=logging.INFO)

    loggers = [logging.getLogger(__name__)]
    with tqdm_logging_redirect(total=9):
        for i in trange(9):
            if i == 4:
                logging.info("Console logging redirected to tqdm logger")
    loggers = [logging.getLogger(__name__)]
    assert any(_is_console_logging_handler(handler) for handler in loggers)
    loggers = [logging.getLogger(__name__)]

# Generated at 2022-06-14 13:28:51.288083
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from tqdm.auto import tqdm
    except ImportError:
        from tqdm import tqdm

    import logging
    from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-14 13:29:04.478777
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.cli import Tqdm

    logger = Tqdm.get_logger()
    logger.propagate = False
    handler_orig = Tqdm.get_logging_handler()
    logger.addHandler(handler_orig)
    log_records = logger.handlers[0].records

    # make the test deterministic
    Tqdm.reset_state_inst()

    class MyTqdm(std_tqdm):
        @classmethod
        def get_logger(cls):
            return logger

    with MyTqdm(ascii=True, disable=False, desc='desc text', ncols=10,
                total=100, bar_format='{l_bar}{bar}|') as pbar:
        assert pbar.leave
        assert not pbar.disable
       

# Generated at 2022-06-14 13:29:13.751020
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from unittest import TestCase

    from .test_std import MockStream, captured_stdout
    from .tqdm import trange

    class TestLoggingRedirectTqdm(TestCase):
        def setUp(self):
            # type: () -> None
            self.logger = logging.getLogger('TestLoggingRedirectTqdm')
            self.logger.setLevel(logging.INFO)
            self.handler = logging.StreamHandler()
            self.handler.setLevel(logging.INFO)
            self.formatter = logging.Formatter('%(levelname)s - %(message)s')
            self.handler.setFormatter(self.formatter)
            self.logger.addHandler(self.handler)


# Generated at 2022-06-14 13:29:21.329221
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():

    original_stdout = sys.stdout

    sys.stdout = open('/tmp/test.txt', 'w')

    logging.root.handlers.remove(_get_first_found_console_logging_handler(logging.root.handlers))
    logging.root.addHandler(_TqdmLoggingHandler())
    logging.root.setLevel(logging.INFO)

    # Simulate some logging
    logging.info('Started')
    logging.info('Went to the store')
    logging.info('Done with program')
    logging.info('Exiting')

    # Reset original stdout
    sys.stdout.close()
    sys.stdout = original_stdout

    # Assert logging is correct
    expected_log = b'Started\n' + b'Went to the store\n' + b

# Generated at 2022-06-14 13:29:27.129381
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:29:36.891441
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test logging_redirect_tqdm function.
    """
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")


if __name__ == '__main__':
    # Testing logging_redirect_tqdm function
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:29:41.322711
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None

    import unittest
    from unittest.mock import MagicMock

    class _TqdmLoggingHandlerTest(unittest.TestCase):
        def setUp(self):
            self.tqdm_cls = MagicMock()
            self.handler = _TqdmLoggingHandler(self.tqdm_cls)
            self.msg = 'test message'
            self.record = MagicMock()
            self.record.msg = self.msg
            self.record.levelname = 'INFO'
            self.record.exc_info = None
            self.record.exc_text = None

        def test_emit(self):
            # make sure emit() doesn't raise an error
            self.handler.emit(self.record)

            self.tqdm_

# Generated at 2022-06-14 13:29:51.974612
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys
    sys.argv = [__file__]

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('test logging')
    logger.info('test redirect tqdm')

    with tqdm_logging_redirect(desc='test logging', logger=logger):
        logger.info('test redirect tqdm')

# Generated at 2022-06-14 13:29:57.115455
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import time

    import pytest

    orig_handlers = logging.getLogger().handlers
    with tqdm_logging_redirect():
        time.sleep(0.1)
    assert orig_handlers == logging.getLogger().handlers


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:30:06.356013
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm
    from io import StringIO
    from os import devnull
    from sys import platform
    import logging
    import tempfile
    import unittest

    @contextmanager
    def redirect_stdout(stream):
        old_stdout = sys.stdout
        sys.stdout = stream
        try:
            yield
        finally:
            sys.stdout = old_stdout

    class TestLoggingRedirectTqdm(unittest.TestCase):
        def setUp(self):
            # set up tqdm
            self.tqdm = tempfile.TemporaryFile(mode='w+')
            self.tqdm_real = sys.stdout
            sys.stdout = self.tqdm

            # set up logging

# Generated at 2022-06-14 13:30:10.336494
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        LOG.info("redirected to tqdm.write")
    LOG.info("back to regular logging")

# Generated at 2022-06-14 13:30:31.153842
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from tqdm import tqdm

    import logging
    from logging import getLogger, StreamHandler, basicConfig, INFO

    class MockTqdmStream(list):
        """Mock `tqdm.write()` to a list instead of sys.stderr"""
        def __init__(self):
            super(MockTqdmStream, self).__init__()

        def write(self, s):
            self.append(s)
    
    def get_logger_with_mock_tqdm_stream():
        logger = getLogger()
        mock_tqdm_stream = MockTqdmStream()
        handler = _TqdmLoggingHandler(tqdm_class=tqdm)
        handler.stream = mock_tqdm_stream
        logger.addHandler(handler)
        return

# Generated at 2022-06-14 13:30:40.315938
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm_notebook

    loggers = [logging.getLogger('test_logging_redirect_tqdm')]

    LOG = loggers[0]
    LOG.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    LOG.addHandler(ch)


# Generated at 2022-06-14 13:30:50.035356
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging

    LOG = logging.getLogger(__name__)

    logger_handlers = LOG.handlers
    LOG.info("Test line 1")
    with logging_redirect_tqdm(loggers=None):
        LOG.info("Test line 2")
        with logging_redirect_tqdm(loggers=[LOG]):
            LOG.info("Test line 3")
        LOG.info("Test line 4")
    LOG.info("Test line 5")
    assert logger_handlers == LOG.handlers
    print("Test passed")
# Test for function tqdm_logging_redirect

# Generated at 2022-06-14 13:30:57.913932
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import trange
    from time import sleep

    log = logging.getLogger('test_logging_redirect_tqdm')

    # default logger
    with logging_redirect_tqdm() as _:
        for _ in trange(5):
            sleep(0.05)
            log.info('default logger only')

    # specified logger
    logger = logging.getLogger('test_logging_redirect_tqdm')
    with logging_redirect_tqdm(loggers=[logger]) as _:
        for _ in trange(5):
            sleep(0.05)
            logger.info('specified logger only')

    # specified loggers
    logger = logging.getLogger('test_logging_redirect_tqdm')
    root = logging.getLogger

# Generated at 2022-06-14 13:31:06.999401
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import io
    import logging    # noqa
    from tqdm.std import tqdm as std_tqdm    # noqa

    # Create a test logger.
    LOG = logging.getLogger(__name__)

    # Set the logging level.
    LOG.setLevel(logging.DEBUG)

    # Redirect stdout to StringIO.
    buffer = io.StringIO()
    sys.stdout = buffer

    # Now create a handler that will write to stdout.
    stream_handler = logging.StreamHandler(sys.stdout)

    # Add the stream handler.
    LOG.addHandler(stream_handler)

    # Log the error message.

# Generated at 2022-06-14 13:31:10.742935
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    with tqdm_logging_redirect():
        log.info("a")

# Generated at 2022-06-14 13:31:15.406739
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Test whether the logging_redirect_tqdm works as expected.
    """
    import logging
    log = logging.getLogger(__name__)
    log.debug("First message")
    with logging_redirect_tqdm():
        log.debug("Second message")



# Generated at 2022-06-14 13:31:23.511756
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pylint: disable=unused-argument
    """Test the logging_redirect_tqdm function"""
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
        LOG.info("console restored")

# Generated at 2022-06-14 13:31:29.982798
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # Get logger object
    log = logging.getLogger('test')

    # Log something
    log.info('Logging something')  # Prints to stdout/err

    # Redirect logging to tqdm
    with logging_redirect_tqdm():
        # Log something
        log.info('Logging something')  # Prints to `tqdm.write()`

    # Logging is restored and prints to stdout/err again
    log.info('Logging something')



# Generated at 2022-06-14 13:31:37.410754
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Unit test for logging_redirect_tqdm()."""
    log_msg = "console logging redirected to `tqdm.write()`"

    def _test(logger):
        logger.setLevel(logging.INFO)
        logging_handler = _is_console_logging_handler(logger.handlers[0])
        with logging_redirect_tqdm():
            logger.info(log_msg)
        # logging restored
        return _is_console_logging_handler(logger.handlers[0]) == logging_handler

    assert _test(logging.getLogger("root_loger"))
    assert _test(logging.getLogger("other_loger"))

# Generated at 2022-06-14 13:32:03.608713
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import multiprocessing
    import socket
    import time

    def log(logger, i=0):
        # type: (logging.Logger, int) -> None
        logger.info('log %d' % i)
        logger.debug('debug %d' % i)
        logger.critical('critical %d' % i)
        logger.error('error %d' % i)
        logger.warning('warning %d' % i)

    def log_subprocess(logger, i=0):
        # type: (logging.Logger, int) -> None
        logger.info('subprocess %d' % i)


# Generated at 2022-06-14 13:32:09.003749
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
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


# Generated at 2022-06-14 13:32:12.099496
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from kill_ring import kill

    logger = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                logger.info('console logging redirected to `tqdm.write()`')
    # logging restored
    kill()

# Generated at 2022-06-14 13:32:20.096662
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.auto import tqdm
    from tqdm.contrib import logging as tqdm_logging
    import logging

    log = logging.getLogger(__name__)
    with tqdm_logging_redirect(desc='test tqdm_logging_redirect', tqdm=tqdm,
                               loggers=[log], leave=False) as pbar:
        for i in pbar:
            if i == 2:
                log.info('2222')
            elif i == 5:
                log.info('555555')
            elif i == 9:
                log.info('9999999999')


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:32:30.980553
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    import mock

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with mock.patch.object(tqdm, "write") as mock_write:
            with logging_redirect_tqdm():
                for i in tqdm(range(9)):
                    if i == 4:
                        LOG.info("console logging redirected to `tqdm.write()`")
            assert mock_write.call_count == 1
            mock_write.assert_called_with("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:32:40.093859
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    log_str = "test log"
    tqdm_handler = _TqdmLoggingHandler()
    try:  # Python 2
        from cStringIO import StringIO
    except ImportError:  # Python 3
        from io import StringIO
    stdout = sys.stdout
    sys.stdout = StringIO()
    tqdm_handler.emit(logging.LogRecord('name', 'WARN', 'pathname', 1, log_str, None, None))
    assert sys.stdout.getvalue() == log_str + '\n'
    sys.stdout = stdout

# Generated at 2022-06-14 13:32:45.012468
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import tqdm

    log_level = logging.INFO
    logger = logging.getLogger(__name__ + '.test__TqdmLoggingHandler_emit')
    logger.setLevel(log_level)

    try:
        handler = _TqdmLoggingHandler()
        logger.addHandler(handler)
        
        # test logging a simple string
        message = 'simple info string'
        logger.info(message)

        # test logging an object which can be converted to a string by str()
        message = tqdm.tqdm(range(10))
        logger.info(message)
    finally:
        logger.removeHandler(handler)

if __name__ == '__main__':
    test__TqdmLoggingHandler_emit()

# Generated at 2022-06-14 13:32:50.571118
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:32:54.972002
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:32:59.307193
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with tqdm_logging_redirect(total=10, unit='B') as pbar:
        for i in range(10):
            pbar.update(i)
