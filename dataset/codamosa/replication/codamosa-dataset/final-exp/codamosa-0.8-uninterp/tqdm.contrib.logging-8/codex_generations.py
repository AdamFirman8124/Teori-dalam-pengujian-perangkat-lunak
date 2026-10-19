

# Generated at 2022-06-14 13:27:55.358163
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Unit tests for tqdm.logging"""
    import logging
    from tqdm import trange
    from ._utils import _range

    with _range(0) as (seq, _):

        LOG = logging.getLogger(__name__)

        with logging_redirect_tqdm():
            for _ in trange(9):
                if _ == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:27:59.151461
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():

        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:08.462162
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange
    from tqdm._utils import _term_move_up

    with open('tmp_logging_redirect_tqdm.log', 'w') as out:
        logging.basicConfig(level=logging.INFO, filename='tmp_logging_redirect_tqdm.log')
        LOG = logging.getLogger(__name__)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
    assert _term_move_up() + 'console logging redirected to `tqdm.write()`'

# Generated at 2022-06-14 13:28:15.555209
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from io import StringIO
    import logging

    # Did we print out the message that the logger was changed?
    log_msg = 'console logging redirected to `tqdm.write()`'
    # Did we print out the default message (i, 0.1)?
    default_msg = '10it [00:00, 920.20it/s]'
    # Did we print out the message given by the progress bar?
    prog_msg = '9it [00:00, 1020.02it/s]'

    # Capture stdout in a file-like object
    f = StringIO()
    sys.stdout = f

    # Set up a logger that redirects info messages to stdout
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Send a message when the logger

# Generated at 2022-06-14 13:28:24.818060
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    try:
        from unittest import mock  # py3+
    except ImportError:
        import mock  # py2

    mock_tqdm_write = mock.Mock()
    mock_tqdm_write.write = mock.Mock()

    mock_tqdm = mock.Mock()
    mock_tqdm.write = mock_tqdm_write.write

    mock_log = mock.Mock()
    mock_log.handlers = [logging.StreamHandler()]

    with mock.patch('tqdm.std.tqdm', mock_tqdm), \
            mock.patch('logging.getLogger', mock_log):
        with logging_redirect_tqdm():
            logging.getLogger().info('should be intercepted')

    assert mock_log

# Generated at 2022-06-14 13:28:35.215517
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys
    import os
    import contextlib
    from io import StringIO
    tempdir = os.path.dirname(os.path.abspath(__file__))  # pylint: disable=invalid-name
    with open('Logger.log', 'w') as f:
        f.write('')
    logger = logging.getLogger(tempdir)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.FileHandler('Logger.log')
    logger.addHandler(handler)
    @contextlib.contextmanager
    def captured_output():
        oldout = sys.stdout
        olderr = sys.stderr

# Generated at 2022-06-14 13:28:41.732387
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from ..std import tqdm as std_tqdm
    # type: ignore

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
                total=9,
                desc='testing',
                loggers=[LOG],
                tqdm_class=std_tqdm
                # type: ignore
        ):
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:46.942551
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.utils import _range
    import logging

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        for i in _range(9):  # no dealy
            if i == 4:
                LOG.info('console logging redirected to `tqdm.write()`')



# Generated at 2022-06-14 13:28:55.320591
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from ..std import tqdm as std_tqdm

    def _do_test(tqdm_class):
        LOG = logging.getLogger(__name__)
        LOG.handlers = []
        original_handlers = LOG.handlers
        with tqdm_logging_redirect(tqdm_class=tqdm_class):
            with tqdm_class(total=9) as pbar:
                for i in range(9):
                    pbar.update()
                    if i == 4:
                        LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
        assert LOG.handlers == original_handlers

    _do_test(tqdm_class=std_tqdm)

# Generated at 2022-06-14 13:29:00.891435
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from contextlib import redirect_stdout

    import logging

    from .core import tqdm

    logging.basicConfig(level=logging.INFO)
    with redirect_stdout(sys.stdout) as out:
        with logging_redirect_tqdm(tqdm_class=tqdm):
            for i in tqdm(range(9)):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:29:14.903742
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    from tqdm.contrib.logging import tqdm_logging_redirect
    with tqdm_logging_redirect() as pbar:
        for i in range(3):
            pbar.update()
    logger.debug("Testing")

# Generated at 2022-06-14 13:29:17.689693
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    handler = _TqdmLoggingHandler()
    record = logging.LogRecord('name', logging.WARNING, 'pathname', 1,
                               'message', None, None)
    handler.emit(record)
    assert True

# Generated at 2022-06-14 13:29:25.408767
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    def f(loggers=None, tqdm_class=std_tqdm):
        # type: (...) -> None
        with logging_redirect_tqdm(loggers=loggers, tqdm_class=tqdm_class):
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

    f()

# Generated at 2022-06-14 13:29:29.787511
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in std_tqdm(range(9), desc='hello'):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:29:41.177669
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import os

    LOG = logging.getLogger(__name__)

    # Clear logging handlers if any
    LOG.handlers = []

    log_fname = 'log_redirect_tqdm.log'
    # Set logging handlers as file handler and console handler
    log_file_handle = logging.FileHandler(log_fname, mode='w')
    log_console_handle = logging.StreamHandler()
    log_file_handle.setLevel(logging.INFO)
    log_console_handle.setLevel(logging.INFO)
    LOG.addHandler(log_file_handle)
    LOG.addHandler(log_console_handle)

    # Set logging format
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    log

# Generated at 2022-06-14 13:29:46.911945
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored


# Generated at 2022-06-14 13:29:55.929589
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect() as pbar:
        for _ in pbar(trange(9)):
            if pbar.n == 4:
                LOG.info("console logging redirected to `tqdm.write()`")


__all__ = ['logging_redirect_tqdm', 'tqdm_logging_redirect']

# Generated at 2022-06-14 13:30:05.297054
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from ._utils import _HandlerTestCase
    test_case = _HandlerTestCase()
    for tqdm_class in [std_tqdm, test_case.get_tqdm()]:
        with test_case.redirect_stds():
            handler = _TqdmLoggingHandler(tqdm_class=tqdm_class)
            test_case.add_handler(handler)
            test_case.log_all_logging_levels()
            captured_stdout = test_case.get_stdout_log()
            assert 'DEBUG:' not in captured_stdout
            assert 'INFO:' in captured_stdout
            assert 'WARNING:' in captured_stdout
            assert 'ERROR:' in captured_stdout
            assert 'CRITICAL:' in captured_stdout


# Generated at 2022-06-14 13:30:14.716147
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock
    loggers = [Mock() for _ in range(3)]

    with logging_redirect_tqdm(loggers=loggers):
        assert len(loggers[0].handlers) == 1
        assert len(loggers[1].handlers) == 1
        assert len(loggers[2].handlers) == 1
        assert _is_console_logging_handler(loggers[0].handlers[0])
        assert _is_console_logging_handler(loggers[1].handlers[0])
        assert _is_console_logging_handler(loggers[2].handlers[0])

    assert len(loggers[0].handlers) == 0

# Generated at 2022-06-14 13:30:21.020589
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .test_tqdm import pretest_posttest  # pylint: disable=redefined-outer-name

    logger = logging.getLogger('test-logger')
    loggers = [logger]
    tqdm_message = 'test message'

    def logging_test():
        """Unit test function for function logging_redirect_tqdm"""
        # pylint: disable=protected-access
        logger.debug(tqdm_message)
        assert std_tqdm._instances  # tqdm already used
        tqdm_instance = std_tqdm._instances[0]
        assert tqdm_instance._write_buffer_lock()  # write buffer actually used
        assert tqdm_message in tqdm_instance._write_buffer[0]

# Generated at 2022-06-14 13:30:56.586631
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from io import StringIO
    import sys
    import unittest

    class TestHandler(logging.Handler):
        """Test handler for unit testing."""

        def __init__(self, name):
            # type: (str) -> None
            super(TestHandler, self).__init__()
            self.name = name
            self.logs = StringIO()

        def emit(self, record):
            # type: (logging.LogRecord) -> None
            self.logs.write(self.format(record) + '\n')

    # Redirecting stdout to a StringIO
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    # Logger
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

# Generated at 2022-06-14 13:31:00.254895
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    with tqdm_logging_redirect():
        logging.info('some text')
    with tqdm_logging_redirect(ncols=120):
        logging.info('some text')

# Generated at 2022-06-14 13:31:07.385440
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import tempfile
    logging.basicConfig(level=logging.INFO)
    with tempfile.NamedTemporaryFile('r+') as logfile:
        fileHandler = logging.FileHandler(logfile.name)
        logging.getLogger().addHandler(fileHandler)
        with logging_redirect_tqdm():
            logging.info("console logging redirected to `tqdm.write()`")
        assert logfile.read() == ("console logging redirected to "
            "`tqdm.write()`\n")
        logging.getLogger().removeHandler(fileHandler)
    # logging restored
    assert logging.getLogger().handlers == [logging.StreamHandler(sys.stderr)]

# Generated at 2022-06-14 13:31:17.761956
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger.info('one')
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info('two')
        for i in trange(3):
            logger.info('three')
            logger.info('four')
    logger.info('five')
    assert 'two\nthree\nfour\n' == sys.stderr.getvalue()
    sys.stderr.seek(0)
    sys.stderr.truncate(0)



# Generated at 2022-06-14 13:31:22.641384
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

# Generated at 2022-06-14 13:31:30.905882
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    with tqdm.tqdm() as pbar:
        with tqdm_logging_redirect():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                    assert 'logging redirected to `tqdm.write()`' in pbar.write.buf


# Generated at 2022-06-14 13:31:36.706560
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # trange is an alias of tqdm.trange
    from tqdm import trange

    with logging_redirect_tqdm(loggers=[logging.getLogger('test')]):
        for i in trange(9):
            if i == 4:
                logging.info('console logging redirected to `tqdm.write()`')



# Generated at 2022-06-14 13:31:45.072554
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from .test_tqdm import with_test_tqdm_instance
    LOG = logging.getLogger(__name__)

    with with_test_tqdm_instance() as pbar, \
            tqdm_logging_redirect(total=7, unit='splines'):
        for i in trange(7):
            if i == 3:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:31:55.242092
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Unit test for logging_redirect_tqdm()"""
    import logging
    import sys

    # Should not display anything
    with logging_redirect_tqdm():
        logging.info('This should not be displayed.')
        logging.warning('Neither should this.')
        print('Nor this.', file=sys.stdout)
        print('Or this.', file=sys.stderr)

    # Should display messages in console
    with tqdm_logging_redirect(
            desc='Display messages in console', leave=False, total=2) as pbar:
        pbar.update()
        logging.info('This should be displayed.')
        pbar.update()
        logging.warning('This should also be displayed.')

# Generated at 2022-06-14 13:31:58.061127
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('logging_test')
    lines = []
    with tqdm(total=9) as pbar:
        with logging_redirect_tqdm() as redirect:
            for i in range(9):
                pbar.update(1)
                if i == 4:
                    log.info('console logging redirected to tqdm.write()')



# Generated at 2022-06-14 13:32:38.748570
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
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


# Generated at 2022-06-14 13:32:47.150441
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in range(2):
            LOG.info('message: %d', i)
        logger = logging.getLogger('logger1')
        logger.handlers = []
        logger.addHandler(logging.NullHandler())
        logger2 = logging.getLogger('logger2')
        logger2.handlers = []
        logger2.addHandler(logging.NullHandler())
        with logging_redirect_tqdm(loggers=[logger, logger2]):
            for i in range(2):
                logger.info('logger1: %d', i)
                logger2.info('logger2: %d', i)

# Generated at 2022-06-14 13:32:53.507210
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.autonotebook import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect
    from .tests_tqdm import pretest_posttest_testsuite, foo

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


# Generated at 2022-06-14 13:33:02.589712
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    import sys
    from io import StringIO

    # Get current stdout and stderr
    current_stdout, current_stderr = sys.stdout, sys.stderr

    # Define an example logger
    logger = logging.getLogger('tqdm')
    logger.addHandler(_TqdmLoggingHandler())
    logger.setLevel(logging.DEBUG)

    # Test emit in tqdm
    tqdm_handler = _get_first_found_console_logging_handler(logger.handlers)
    assert tqdm_handler is not None
    assert tqdm_handler.stream in (sys.stdout, sys.stderr)

    # logs should be generated in the original stdout
    logger.debug('example test')
    assert current_stdout.getvalue()

# Generated at 2022-06-14 13:33:09.519919
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    # (main)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)

        # with tqdm_logging_redirect():
        #     for i in range(9):
        #         if i == 4:
        #             LOG.info("console logging redirected to `tqdm.write()`")

        for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:33:18.845604
# Unit test for function tqdm_logging_redirect

# Generated at 2022-06-14 13:33:25.581111
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from ..std import tqdm
    import logging
    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect():
        for i in tqdm.trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:31.500585
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    def f():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        f()

# Generated at 2022-06-14 13:33:36.387577
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(logging.INFO, 0, 'logging.INFO') as t:
        for i in range(4):
            if i == 2:
                LOG.info('logging redirected to tqdm.write()')
    assert t[0] == 'logging redirected to tqdm.write()'

# Generated at 2022-06-14 13:33:45.162209
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from ..std import tqdm as std_tqdm
    from ..std import tqdm
    for tqdm_class in [std_tqdm, tqdm]:
        with tqdm_logging_redirect(
            total=3,
            loggers=[logging.getLogger(__name__)],
            tqdm_class=tqdm_class
        ) as pbar:
            pbar.set_description(repr(pbar))
            assert repr(pbar).startswith(
                '<{0}({1}, '.format(tqdm_class.__name__, pbar.n)
            )
            assert logging.getLogger(__name__).handlers[-1] is pbar.logger.handlers[-1]

# Generated at 2022-06-14 13:35:06.134843
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange, tqdm_notebook
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        with logging_redirect_tqdm([LOG], tqdm_class=tqdm_notebook):
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm_notebook.write()`")

# Generated at 2022-06-14 13:35:12.840116
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ._deprecated import tqdm_cli
    from ._deprecated import tqdm_curses
    from tqdm.auto import tqdm

    for tqdm_class in [tqdm, tqdm_curses, tqdm_cli]:
        with tqdm_class(total=3, desc='(testing)', dynamic_ncols=True) as pbar:
            assert pbar.n == 0
            with logging_redirect_tqdm():
                logging.info('info')
                logging.warn('warning')
                logging.error('error')
            assert pbar.n == 3



# Generated at 2022-06-14 13:35:23.203375
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    def test_redirect():
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
            total=9,
            desc='test',
            unit=' iterations',
            disable=True,
            mininterval=0.1,
            smoothing=1e-10
        ) as pbar:
            assert pbar._miniters == 1
            assert pbar._mininterval == 0.1
            assert pbar._smoothing == 1e-10
            assert not pbar._dynamic_miniters
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:35:32.255461
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Unit test for function logging_redirect_tqdm"""
    import logging
    import sys
    from tqdm.contrib.logging import _TqdmLoggingHandler


# Generated at 2022-06-14 13:35:34.440967
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.utils import _range
    from tqdm._tqdm_pandas import tqdm_pandas
    from tqdm.std import tqdm
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(total=5):
        for i in _range(5):
            if i == 3:
                LOG.info("Console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:35:44.692008
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import os
    # save the old stdout and stderr
    saved_stdout = os.dup(sys.stdout.fileno())
    saved_stderr = os.dup(sys.stderr.fileno())

    # make write something to stdout, and redirect it to a file
    with open('test_tqdm.log', 'w') as logf:
        os.dup2(logf.fileno(), sys.stdout.fileno())
        os.dup2(logf.fileno(), sys.stderr.fileno())

        # create a logger and set its level
        log = logging.getLogger(__name__)

        # check some logs
        log.error('test error')
        log.warning('test warning')
        log.info('test info')

# Generated at 2022-06-14 13:35:53.292469
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    from tqdm._tqdm import _instances
    from .tests_tqdm import StringIOClass
    try:
        from StringIO import StringIO  # Python 2
    except ImportError:
        from io import StringIO  # Python 3
    try:
        from unittest.mock import patch  # Python 3
    except ImportError:
        from mock import patch  # Python 2

    with patch('sys.stderr', new=StringIO()):

        with tqdm_logging_redirect(file=sys.stderr):
            logging.debug("debug")
            logging.info("info")
            logging.warning("warning")
            logging.error("error")

# Generated at 2022-06-14 13:35:58.094778
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
        # logging restored



# Generated at 2022-06-14 13:36:08.551953
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:36:10.301278
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import tqdm

    logging.basicConfig(level=logging.DEBUG)
    with logging_redirect_tqdm():
        for i in tqdm(range(3)):
            logging.warning(i)



# Generated at 2022-06-14 13:37:28.406526
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import shutil
    loggers = [logging.getLogger("tqdm_logging_redirect")]
    shutil.rmtree("/tmp/tqdm-tests")
    try:
        with tqdm_logging_redirect(total=9, desc="testing tqdm_logging_redirect", loggers=loggers):
            for i in range(9):
                if i == 4:
                    for logger in loggers:
                        logger.info("console logging redirected to `tqdm.write()`")
            assert False, "should raise an error"
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:37:34.384079
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Simple unit test for `logging_redirect_tqdm`"""
    import logging
    from tqdm import trange
    logger = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in trange(5):
            logger.info("testing")
            if i == 2:
                logger.info("intermediate message")
    logger.info("restored")

# Generated at 2022-06-14 13:37:45.494216
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    from tqdm import tqdm, trange
    from tqdm.contrib.logging import logging_redirect_tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    # tqdm_kwargs passed
    with tqdm_logging_redirect(position=2):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    # tqdm