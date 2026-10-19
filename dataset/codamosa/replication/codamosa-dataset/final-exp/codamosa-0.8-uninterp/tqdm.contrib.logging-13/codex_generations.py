

# Generated at 2022-06-14 13:27:46.373928
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import re
    import sys
    from time import time
    from unittest import TestCase
    from ..tdqm import tqdm

    origin_stdout = sys.stdout
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = [logging.StreamHandler(sys.stdout)]
    assert len(logger.handlers) == 1

    tqdm_stdout = ''

    class TestLoggingRedirectTqdm(TestCase):
        def setUp(self):
            nonlocal tqdm_stdout
            tqdm_stdout = ''
            sys.stdout = TestLoggingRedirectTqdm.TqdmStream()

        def tearDown(self):
            sys.stdout = origin_stdout

# Generated at 2022-06-14 13:27:54.611774
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    log_format = '%(levelname)s:%(filename)s:%(lineno)d:%(funcName)s:%(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)

    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored



# Generated at 2022-06-14 13:28:03.179805
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.utils import _range
    import logging
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)  # Fix Python 2.7.6

    with logging_redirect_tqdm() as pbar, \
            tqdm_logging_redirect(list(range(9))) as pbar2:
        for i in _range(9):
            logging.info("example log message: {}".format(i))
            assert next(pbar) == i  # pylint: disable=stop-iteration-return
            assert next(pbar2) == i  # pylint: disable=stop-iteration-return

# Generated at 2022-06-14 13:28:13.329409
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger("tqdm.contrib")

    # Check that logging_redirect_tqdm() works
    with logging_redirect_tqdm():
        for i in trange(5):
            log.info("console logging redirected to `tqdm.write()`")
        log.info("done redirecting")
    log.info("restored handlers")

    # Check that logging_redirect_tqdm() restores the original logger's handlers correctly
    assert all(
        orig_handler in logging.root.handlers
        for orig_handler in logging._handlers.values())

# Generated at 2022-06-14 13:28:23.798514
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import threading
    import logging
    LOG = logging.getLogger(__name__)
    # Unit test for function logging_redirect_tqdm
    with logging_redirect_tqdm():
        for i in std_tqdm(range(4)):
            if i == 2:
                LOG.info('console logging redirected to `tqdm.write()`')
    # with logging_redirect_tqdm():
    #     for i in std_tqdm(range(4)):
    #         if i == 2:
    #             LOG.info('console logging redirected to `tqdm.write()`')
    #     LOG.info('test')
    #     LOG.info('test2')
    #     # test: showing output
    #     for i in std_tqdm(range(4)

# Generated at 2022-06-14 13:28:32.087325
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tnrange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
                tqdm_class=tnrange,
                desc="console logging redirected to `tqdm.write()`",
                total=1e99):
            LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:28:36.202368
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        with tqdm_logging_redirect(total=9, desc='Unit test'):
            print(42)
    except SystemExit as e:
        raise
    except:  # noqa pylint: disable=bare-except
        assert False, "tqdm_logging_redirect failed"

# Generated at 2022-06-14 13:28:39.691724
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from io import StringIO
    from tqdm import trange

    LOG = logging.getLogger(__name__)
    logger_level = LOG.getEffectiveLevel()

    # Test basic logging
    capture_stream = StringIO()
    logger_handlers = LOG.handlers[:]
    try:
        with logging_redirect_tqdm():
            for i in trange(2):
                LOG.info("hello, world")
        captured_output = capture_stream.getvalue()
    finally:
        LOG.handlers = logger_handlers
    assert captured_output == 'hello, world\r\nhello, world\r\n'

    # Test logger filters (e.g. the default INFO level filter)
    capture_stream = StringIO()
    logger_handlers = LOG.handlers[:]

# Generated at 2022-06-14 13:28:44.949118
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import io

    logger = logging.getLogger()
    handler = logging.StreamHandler(io.StringIO())
    logger.addHandler(handler)

    with tqdm_logging_redirect(total=5) as pbar:
        for i in range(5):
            logging.info('test')
            pbar.update()

    assert 'test\n'*5 in handler.stream.getvalue()

# Generated at 2022-06-14 13:28:51.047094
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


# Generated at 2022-06-14 13:29:00.359332
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import tqdm as auto_tqdm
    from tqdm import trange

    with tqdm_logging_redirect(tqdm_class=auto_tqdm):
        for _ in trange(10):
            logging.info(
                "This should be redirected to `tqdm.write()` "
                "and should also appear in the progress bar")

# Generated at 2022-06-14 13:29:09.486879
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class NewTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):
            super(NewTqdm, self).__init__(*args, **kwargs)
            self.messages = []  # type: List[str]

        def write(self, message):
            super(NewTqdm, self).write(message)
            self.messages.append(message)

    LOG = logging.getLogger(__name__)


# Generated at 2022-06-14 13:29:18.172807
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests_tqdm import with_bar, discretize

    pyver = '%s.%s' % (sys.version_info[0], sys.version_info[1])
    logfile = 'test_outputs/logging_redirect_tqdm-' + pyver + '.log'

    import logging
    import tqdm
    with open(logfile, 'w') as f:
        LOG = logging.getLogger(__name__)
        LOG.addHandler(logging.StreamHandler(f))
        with tqdm.tqdm(range(3)) as pbar:
            with logging_redirect_tqdm([LOG], tqdm_class=tqdm.tqdm):
                with with_bar(pbar):
                    LOG.info("intercepted")
                LOG.info

# Generated at 2022-06-14 13:29:27.959711
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Tests the method emit from class _TqdmLoggingHandler.
    """
    from io import StringIO
    from contextlib import contextmanager
    from . import _TqdmLoggingHandler

    # Arrange
    logHandler = _TqdmLoggingHandler(std_tqdm)
    logHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logHandler.setLevel(logging.DEBUG)
    records = []
    record = logging.LogRecord('testLogger', logging.DEBUG, '', 0, 'testMessage', None, None)
    records.append(record)
    record = logging.LogRecord('testLogger', logging.INFO, '', 0, 'testMessage', None, None)

# Generated at 2022-06-14 13:29:36.801042
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    # from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored



# Generated at 2022-06-14 13:29:39.116362
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Unit test for method emit of class _TqdmLoggingHandler.
    """
    log_record = logging.LogRecord(
        'test__TqdmLoggingHandler_emit',
        logging.DEBUG, '', 0, "test", None, None
    )
    handler = _TqdmLoggingHandler()
    handler.emit(log_record)

# Generated at 2022-06-14 13:29:43.326417
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    handler = _TqdmLoggingHandler(std_tqdm)
    rc = logging.LogRecord(
        name='unit_test', level=20,
        pathname='path', lineno=123,
        msg='foo', args=None, exc_info=None)
    handler.emit(rc)
    assert handler.stream.getvalue() == 'foo\n'

# Generated at 2022-06-14 13:29:47.005039
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    LOG = logging.getLogger(__name__)
    LOG.info("logging info")
    with tqdm_logging_redirect(total=1):
        LOG.info("logging info")

# Generated at 2022-06-14 13:29:56.015026
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm; tqdm_std = tqdm
    import logging
    import time

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm_std(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                    time.sleep(0.1)
        # logging restored
        LOG.info("logging back to console")

# Generated at 2022-06-14 13:30:04.744352
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    '''
    Unit test function to test function tqdm_logging_redirect
    '''
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:30:19.307067
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.autonotebook import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

#
# if __name__ == '__main__':
#     test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:30:27.600315
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # pylint: disable=missing-docstring
    import tqdm
    import logging
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect():
        logging.info("hello")
    with tqdm_logging_redirect(desc='my tqdm', unit='B', unit_scale=True,
                               unit_divisor=1024, miniters=1,
                               disable=True, bar_format='{r_bar}'):
        logging.info("hello")
    # pylint: enable=missing-docstring

# Generated at 2022-06-14 13:30:35.319588
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    with tqdm_logging_redirect(
            total=5,
            desc="tqdm logging redirect",
            logger=logger
            ) as pbar:
        for _ in range(5):
            pbar.update()
            logger.info('hello world!')

    with tqdm_logging_redirect(
            total=5,
            desc="tqdm logging redirect",
            logger=logger,
            disable=True
            ) as pbar:
        for _ in range(5):
            pbar

# Generated at 2022-06-14 13:30:43.390272
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import tempfile
    import os
    import random

    # writing and reading through a temporary file
    # this avoids log-spamming the test process output
    with tempfile.TemporaryFile() as f:
        with redirect_stdout(f):
            LOG = logging.getLogger(__name__)

            logging.basicConfig(level=logging.INFO)
            with tqdm_logging_redirect(total=10, desc="Custom description",
                                       logger=LOG) as pbar:
                for i in range(10):
                    LOG.info(i)
                    pbar.update(1)

            f.seek(0)
            output_list = f.readlines()
            assert len(output_list) == 12

# Generated at 2022-06-14 13:30:50.904816
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import sys
    from tqdm._utils import _term_move_up
    from tqdm.std import tqdm

    logger = logging.getLogger('logging')
    logger.setLevel(logging.INFO)
    logger_handler = _TqdmLoggingHandler(tqdm_class=tqdm)

    log_text = 'hello'
    logger.info(log_text)
    assert _term_move_up() + log_text + '\n' == logger_handler.stream.getvalue()



# Generated at 2022-06-14 13:30:56.518710
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None

    import logging
    try:
        import tqdm
    except ImportError:
        print("tqdm not found!")
        return

    # logging.basicConfig(level=logging.DEBUG)
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(total=9) as pbar:
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
            pbar.update()

# Generated at 2022-06-14 13:31:04.744336
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from tqdm.tests import pretest_posttest  #
    except ImportError:
        return
    from tqdm.contrib.logging import tqdm_logging_redirect

    @pretest_posttest
    def _():
        # Initialize Logger
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(leave=False) as pbar:
            for i in range(3):
                logging.info('Logging to tqdm')
                pbar.set_description('tqdm')
                pbar.update()
    _()

# Generated at 2022-06-14 13:31:11.165413
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import tqdm
    import logging
    LOG = logging.getLogger(__name__)
    with tqdm() as pbar:
        with logging_redirect_tqdm(loggers=[LOG]):
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:31:16.370457
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    with logging_redirect_tqdm():
        try:
            for i in trange(9):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")
        except:
            pass
        # logging restored


# Generated at 2022-06-14 13:31:20.072825
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        log.info(u"hello, this is tqdm speaking")
        log.warning(u"already done, or what?")

# Generated at 2022-06-14 13:31:49.062996
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.tests import _range
    import logging
    from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
    loggers = [logging.getLogger(__name__), logging.getLogger('tqdm')]

    def logprint(*args):
        print(*args)
    logging.basicConfig(
        level=DEBUG, format='%(levelname)s: %(message)s',
        datefmt='%H:%M:%S', stream=logprint)

    # Test no log
    with tqdm_logging_redirect(total=8, loggers=loggers) as pbar:
        for _ in _range(8):
            pbar.update()

    # Test only INFO log

# Generated at 2022-06-14 13:31:58.813460
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import io
    import logging

    from ..std import tqdm_notebook as tqdm_n

    outs = io.StringIO()
    handler = logging.StreamHandler(outs)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    with tqdm_logging_redirect(range(5), loggers=[logger], tqdm_class=tqdm_n) as pbar:
        for i in pbar:
            logger.info('msg %d', i)

# Generated at 2022-06-14 13:32:07.381368
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    logger = logging.getLogger(__name__)
    logger.info('This is a test')
    logger.warning('This is a test')
    logger.error('This is a test')
    logger.critical('This is a test')

    try:
        with logging_redirect_tqdm():
            logger.info('This is a test')
            logger.warning('This is a test')
            logger.error('This is a test')
            logger.critical('This is a test')
    except AssertionError:
        assert False
        # TODO: find out why the above lines throw an AssertionError

# Generated at 2022-06-14 13:32:14.394585
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():

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


if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:32:24.615828
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # Test 1
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        for i in range(10):
            if i == 9:
                LOG.info("console logging redirected to `tqdm.write()`")
    # Test 2
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        with logging_redirecting_tqdm():
            for i in range(10):
                if i == 9:
                    LOG.info("console logging redirected to `tqdm.write()`")
    # Test 3
    logging.basicConfig(level=logging.INFO)
   

# Generated at 2022-06-14 13:32:32.928014
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+') as output_file:
        logging.basicConfig(
            level=logging.DEBUG,
            filename=output_file.name,
            filemode='w'
        )
        with tqdm_logging_redirect(
                logging.root,
                bar_format='{l_bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]',
                file=output_file
        ) as t:
            t.set_description('Testing with file redirect')
            for i in range(10):
                logging.debug('message %d', i)
                t.update(1)

# Generated at 2022-06-14 13:32:41.913220
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    import tqdm
    import time
    import sys

    # Logger
    log = logging.getLogger('__main__')
    log.setLevel(logging.INFO)
    
    # Message in loop
    n = 10
    while n > 0:
        n -= 1
        with tqdm_logging_redirect(
            desc="Loop",
            total=100,
            smoothing=0,
        ):
            time.sleep(0.1)
            log.info("Message")

    # New line
    print()



# Generated at 2022-06-14 13:32:50.869166
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm, tqdm_gui
    #from tqdm.contrib import logging_redirect_tqdm

    loggers = [logging.getLogger(__name__)]
    with tqdm_logging_redirect(
        total=10, file=sys.stderr, desc='this is a test', ncols=80,
        loggers=loggers, tqdm_class=tqdm_gui
    ) as pbar:
        logging.info('hello world')
        for i in range(10):
            pbar.update()
    logging.info('back to normal')

# Generated at 2022-06-14 13:32:55.827509
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:33:04.973572
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.autonotebook import tqdm
    from tqdm.autonotebook import trange
    from random import random
    from sys import stderr
    from time import sleep

    loops = 5
    log = logging.getLogger('test_logging_redirect_tqdm')

    for loop in trange(loops,
                       desc='redirect_test_test',
                       leave=True,
                       file=stderr):
        log.info('logging test')
        sleep(random() / 100.0)

    with logging_redirect_tqdm():
        for loop in trange(loops, desc='redirect_test', leave=True,
                           file=stderr):
            log.info('logging test')
            sleep(random() / 100.0)


# Generated at 2022-06-14 13:33:42.707287
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    handler = _TqdmLoggingHandler()
    record = logging.LogRecord(
        'name', logging.DEBUG, '/tmp/pytest-of-test/pytes22/test_advanced4.py',
        13, 'message', (), None)
    handler.emit(record)

# Generated at 2022-06-14 13:33:49.741357
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class DummyTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):
            super(DummyTqdm, self).__init__(*args, **kwargs)
            self.write = lambda *args, **kwargs: args
            self.flush = lambda *args, **kwargs: self

    dummy_tqdm = DummyTqdm(
        desc='desc',
        file=None,
    )

    tqdm_handler = _TqdmLoggingHandler(tqdm_class=DummyTqdm)
    tqdm_handler.tqdm_class = dummy_tqdm
    tqdm_handler.stream = None
    format_old = logging.Formatter()
    tqdm_handler.level = 1

# Generated at 2022-06-14 13:33:59.696341
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .test_utils import is_module_in_pythonpath

    if not is_module_in_pythonpath("logging"):
        return
    import logging
    from tqdm import tqdm

    def test_tqdm_logging_redirect_unit(tqdm_class=std_tqdm):
        # type: (Type[tqdm]) -> None
        """Unit tests"""
        with tqdm_logging_redirect(total=100, tqdm_class=tqdm_class) as pbar:
            assert pbar.n == 0
            logging.info("logging class: %s", tqdm_class)
            pbar.update()
            assert pbar.n == 1
            logging.info("EOL")
    test_tqdm_logging_redirect_unit

# Generated at 2022-06-14 13:34:10.843898
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import TestTqdm
    import logging

    for tqdm_class in TestTqdm:
        with TestTqdm._catch_stdout() as s:
            with tqdm_logging_redirect(tqdm_class=tqdm_class,
                                       total=20, loggers=[logging.root],
                                       desc='foo') as pbar:
                logging.info('bar')
                for _ in pbar:
                    pbar.update()
                    if pbar.n == 10:
                        logging.info('stdout')
                        print('stdout')
                    if pbar.n == 15:
                        logging.info('stderr')
                        print('stderr', file=sys.stderr)
                    if pbar.n == 17:
                        break

# Generated at 2022-06-14 13:34:15.312695
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(
        total=9, unit="cats", desc="Downloading", leave=False):
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:34:18.631638
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    log = logging.getLogger('log')
    with logging_redirect_tqdm():
        for i in trange(5):
            log.info(i)
    logging.shutdown()

# Generated at 2022-06-14 13:34:23.828112
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    tlh = _TqdmLoggingHandler()
    tlh.stream = sys.stderr
    record = logging.LogRecord(
        name='test', level=0, pathname='/weird/path', lineno=0, msg='test',
        args=(), exc_info=None)
    record.msg += '\n'
    tlh.emit(record)

# Generated at 2022-06-14 13:34:27.007810
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    for i in range(0, 1):
        logger.info(i)

    logging.basicConfig(level=logging.INFO)
    # If the method emit is implemented correctly, there would be no
    # error generated.
    with logging_redirect_tqdm():
        for i in range(1, 11):
            logger.info(i)

# Generated at 2022-06-14 13:34:34.578743
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange

    log_str = 'console logging redirected to `tqdm.write()`'
    for logger in [logging.root, logging.getLogger(__name__)]:
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.setLevel(logging.INFO)

    for i in trange(10):
        logging.info(log_str)
    with logging_redirect_tqdm():
        for i in trange(10):
            logging.info(log_str)

# Generated at 2022-06-14 13:34:44.380706
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)  # type: logging.Logger

    # cleanup the logging environment
    logging.shutdown()
    LOG.handlers = []

    # test callback function
    def _test_cb():
        try:
            with logging_redirect_tqdm():
                for _ in trange(9):
                    # should be redirected to `tqdm.write()`
                    LOG.info("test-1")
                    LOG.info("test-2")
        except KeyboardInterrupt:
            pass
        for _ in trange(9):
            LOG.info("test-3")

    # run test
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        _test_cb()

# Generated at 2022-06-14 13:36:01.581486
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.autonotebook import tqdm as tqdm_notebook, trange
    from tqdm.storage import Storage, get_storage
    from tqdm.utils import _term_move_up
    import io
    import logging
    import sys

    # Test for same behaviour for logging.getLogger() and logging.root
    for logger in (logging.root, logging.getLogger()):
        with tqdm_logging_redirect(
                tqdm_class=tqdm_notebook,
                desc='ctxt mngr', loggers=[logger],
                bar_format='{desc}{bar}{r_bar} {n_fmt}/{total_fmt}',
                ) as pbar:
            assert pbar.desc == 'ctxt mngr'
            p

# Generated at 2022-06-14 13:36:12.049152
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from nose.tools import raises

    from .tqdm import tqdm

    # Start tests
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in tqdm(range(9), desc="test1"):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

    with tqdm_logging_redirect(total=9, desc="test2") as pbar:
        for i in range(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
            pbar.update(1)


# Generated at 2022-06-14 13:36:18.662326
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # Test logging
    try:
        import logging
        LOG = logging.getLogger(__name__)
        LOG.setLevel(logging.INFO)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        LOG.addHandler(console)
    except ImportError:
        LOG = None

    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm


# Generated at 2022-06-14 13:36:25.216027
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")
    logging.info("logging restored")

    try:
        from tqdm import tqdm
        with logging_redirect_tqdm(tqdm_class=tqdm):
            logging.info("console logging redirected to `tqdm.write()`")
    except ImportError:
        pass



# Generated at 2022-06-14 13:36:29.565555
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import time
    cnt = 0
    try:
        with tqdm_logging_redirect(total=10) as pbar:
            for i in range(10):
                cnt += 1
                if i == 4:
                    logging.info("test_tqdm_logging_redirect")
                time.sleep(0.1)
            assert cnt == 10
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-14 13:36:34.152935
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO

    capture = StringIO()
    handler = _TqdmLoggingHandler()
    handler.setFormatter(logging.Formatter('%(message)s'))
    handler.stream = capture
    hello = logging.LogRecord(
        'name', logging.INFO, 'pathname', 0, 'hello', None, None)
    handler.emit(hello)
    assert 'hello' in capture.getvalue()

# Generated at 2022-06-14 13:36:37.437343
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored



# Generated at 2022-06-14 13:36:44.315105
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    LOG = logging.getLogger('test')
    log_msgs = ['hello', 'world']
    tqdm_redirect_msgs = []

    def tqdm_write(msg):
        sys.stdout.write(msg + '\n')
        tqdm_redirect_msgs.append(msg)

    with logging_redirect_tqdm([LOG]):
        for msg in log_msgs:
            LOG.info(msg)
    assert tqdm_redirect_msgs == log_msgs

    tqdm_redirect_msgs = []
    with logging_redirect_tqdm([LOG], tqdm_class=std_tqdm.tqdm):
        for msg in log_msgs:
            LOG.info(msg)
    assert tqdm_redirect

# Generated at 2022-06-14 13:36:54.811368
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from .tqdm import tqdm

    test_logger = logging.getLogger(__name__)
    with logging_redirect_tqdm([test_logger]):
        for i in tqdm(range(10), desc='outer'):
            for j in tqdm(range(10), desc='inner'):
                test_logger.info('hello')
    assert hasattr(tqdm, '_instances')
    assert all(isinstance(h, _TqdmLoggingHandler) for h in test_logger.handlers)
    assert all(h.stream == sys.stderr for h in test_logger.handlers)
    assert all(i not in tqdm._instances for i in tqdm._instances)

# Generated at 2022-06-14 13:36:56.328247
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        logging.info("console logging redirected")

