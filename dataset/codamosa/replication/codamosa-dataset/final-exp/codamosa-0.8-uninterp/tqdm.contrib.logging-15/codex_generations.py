

# Generated at 2022-06-14 13:27:58.417677
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from logging import getLogger, StreamHandler, Formatter, DEBUG
    import sys

    dummy_logger = getLogger("dummy")
    dummy_logger.setLevel(DEBUG)
    console_handler = StreamHandler(sys.stderr)
    console_handler.setFormatter(Formatter("%(message)s"))
    dummy_logger.addHandler(console_handler)

    new_tqdm = _TqdmLoggingHandler()
    # dummy_logger.handlers = [new_tqdm]
    dummy_logger.info("test message")
    del dummy_logger.handlers[:]

    # Check if there is no exception
    assert True



# Generated at 2022-06-14 13:28:07.784220
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from unittest import TestCase
    from io import StringIO
    import logging
    import sys
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    import six

    class LoggingRedirectTqdmTest(TestCase):
        def setUp(self):
            # create a buffer to store the tested output
            self.buf = StringIO()
            sys.stderr = self.buf

        def test_logging_redirect_tqdm(self):
            LOG = logging.getLogger(__name__)

            logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:28:12.515833
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from tqdm.contrib.logging import _TqdmLoggingHandler
    log = logging.getLogger()
    log.propagate = False
    out = StringIO()
    hdlr = _TqdmLoggingHandler(out=out)
    log.addHandler(hdlr)
    log.warning('test')
    assert "test\n" == out.getvalue()

# Generated at 2022-06-14 13:28:23.197994
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # Make sure the test doesn't generate logs in the console
    import logging
    logging.disable(logging.NOTSET)
    import os
    import sys
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 13:28:33.776164
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    import six
    import StringIO
    import sys

    # Create a temporary stream
    stream = StringIO.StringIO()

    # Instantiate a _TqdmLoggingHandler instance and tell it to use the temporary stream
    tqdm_logging_handler = _TqdmLoggingHandler()
    tqdm_logging_handler.stream = stream

    # Create a logging record with a dummy message and a dummy level
    logger = logging.Logger()
    record = logger.makeRecord('name', logging.WARNING, '/fake/file/name/on/disk', 123,
                               "logging_redirect_tqdm: warning message", (), None, None)

    # Check that the temporary stream is empty
    assert stream.getvalue() == ""
    # Call the emit method
    tqdm_logging_handler

# Generated at 2022-06-14 13:28:41.998628
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests_tqdm import pretest_posttest  # pylint: disable=redefined-outer-name
    with pretest_posttest(std_tqdm):
        with tqdm_logging_redirect(
                "test", file=sys.stderr, disable=None, mininterval=0, miniters=1,
                total=20, unit='it'
        ) as pbar:
            assert pbar.n == 0
            pbar.update(1)
            assert pbar.n == 1
            with pbar:
                assert pbar.n == 1
                pbar.update(1)
                assert pbar.n == 2
            assert pbar.n == 2
            pbar.update(2)
            assert pbar.n == 4
            pbar.close()

# Generated at 2022-06-14 13:28:51.630155
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests_tqdm import with_bar, with_logging_redirect

    @with_logging_redirect()
    def f(loggers=None, tqdm_class=std_tqdm, tqdm_redirect=True):
        # type: (...) -> Iterator[None]
        with with_bar() as pbar:
            if tqdm_redirect:
                with tqdm_logging_redirect(
                        loggers=loggers, tqdm_class=tqdm_class,
                        desc='logging_redirect_tqdm:', leave=True):
                    logging.info('testing logging_redirect_tqdm')

# Generated at 2022-06-14 13:28:58.913154
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    def fake_pbar(x, total=None, desc=None, unit=None, unit_scale=False,
                  dynamic_ncols=True, smoothing=None, bar_format=None,
                  initial=0, position=None, leave=True, postfix=None,
                  miniters=None, mininterval=0, maxinterval=10, units=None,
                  file=None, disable=False, ascii=None,
                  ncols=None, mininterval_dynamic=True, unit_divisor=1000,
                  ):
        import tqdm

# Generated at 2022-06-14 13:29:07.598231
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm, tqdm_notebook
    from tqdm.contrib.logging import tqdm_logging_redirect

    # Redirect the output to memory
    log_stream = open('/dev/null', 'w')
    log_handler = logging.StreamHandler(log_stream)
    logging.root.addHandler(log_handler)

    # Test 1

# Generated at 2022-06-14 13:29:16.599394
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    def main():
        import logging
        import time


# Generated at 2022-06-14 13:29:27.499531
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    log = logging.getLogger(__name__)

    with tqdm_logging_redirect(desc="testing redirect",
                               loggers=[log], mininterval=0):
        for i in trange(9):
            if i == 4:
                log.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:29:39.504792
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from tqdm import std
    from tqdm.contrib.logging import _TqdmLoggingHandler
    import logging

    stream = StringIO()
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(_TqdmLoggingHandler(std.tqdm))

    log = logging.getLogger(__name__)
    log.debug("DEBUG message")
    log.info("INFO message")
    log.warning("WARN message")
    log.error("ERROR message")
    log.critical("CRITICAL message")

    output = stream.getvalue()
    assert "DEBUG message" not in output
    assert "INFO message" in output
    assert "WARN message" in output
    assert "ERROR message" in output

# Generated at 2022-06-14 13:29:49.768886
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    try:
        import tqdm
    except ImportError:
        try:
            import tqdm as tqdm
        except ImportError:
            tqdm = None  # type: ignore
    try:
        from tqdm.contrib.logging import logging_redirect_tqdm
    except ImportError:
        logging_redirect_tqdm = None  # type: ignore
    try:
        from tqdm.contrib.logging import tqdm_logging_redirect
    except ImportError:
        tqdm_logging_redirect = None  # type: ignore
    try:
        import unittest2 as unittest  # py26
    except ImportError:
        import unittest


# Generated at 2022-06-14 13:30:00.572289
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from unittest import TestCase

    class TestCaseTqdmLoggingHandler(TestCase):

        def test_emit(self):
            for tqdm_class in (std_tqdm, ):
                print("Testing {0}".format(tqdm_class))
                with tqdm_class(disable=True) as tqdm:
                    logger = logging.getLogger("test")
                    handler = _TqdmLoggingHandler(tqdm_class=tqdm_class)
                    handler.stream = tqdm.write
                    logger.addHandler(handler)
                    logger.error("Hello world!")
                    logger.info("Hello world!")
                    logger.debug("Hello world!")

    suite = TestCaseTqdmLoggingHandler()
    suite.run()



# Generated at 2022-06-14 13:30:04.584581
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        print(sys.stderr)

# Generated at 2022-06-14 13:30:11.636684
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from .test_tqdm import pretest  # pylint: disable=unused-variable
        import logging
        import multiprocessing as mp
        from tqdm import trange
    except ImportError:
        return
    logger = logging.getLogger('example_logger')
    with logging_redirect_tqdm([logger, mp.get_logger()], std_tqdm) as _:
        logger.info('redirected logging in tqdm')
        mp.get_logger().info('redirected logging in tqdm')
        with tqdm_logging_redirect(total=3, desc='x'):
            for i in trange(3):
                logger.info('in loop')
                mp.get_logger().info('in loop')

# Generated at 2022-06-14 13:30:19.459730
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import logging, tqdm
    from ..std import StringIO as cStringIO
    log = logging.getLogger('test')
    orig_log_handlers = log.handlers
    try:
        log.setLevel(logging.INFO)
        with cStringIO() as buf:
            with logging_redirect_tqdm(loggers=[log], tqdm_class=tqdm):
                for i in tqdm(range(9)):
                    if i == 4:
                        log.info("console logging redirected to tqdm.write()")
            assert "console logging" in buf.getvalue()
            assert "redirected to tqdm.write" in buf.getvalue()
    finally:
        log.handlers = orig_log_handlers



# Generated at 2022-06-14 13:30:30.464439
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    import tqdm
    import __builtin__
    import io

    # Setup the environment
    stdout_buffer = io.BytesIO()
    stderr_buffer = io.BytesIO()
    tqdm.tqdm = std_tqdm
    tqdm.std.tqdm.write = std_tqdm.write
    tqdm_handler = _TqdmLoggingHandler()
    dummy_logger = logging.getLogger('dummy_logger')
    dummy_logger.setLevel(logging.INFO)
    dummy_logger.addHandler(tqdm_handler)
    tqdm_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    temp_stdout = sys.stdout
   

# Generated at 2022-06-14 13:30:39.848892
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging

    class TqdmDummy(object):
        def __init__(self, *args, **kwargs):
            pass

        def write(self, *args, **kwargs):
            self.write_args = args
            self.write_kwargs = kwargs

        def flush(self, *args, **kwargs):
            self.flush_args = args
            self.flush_kwargs = kwargs

    record = logging.LogRecord(
        'test', logging.DEBUG, None, None, 'test_record_message', (), None, None)

    handler = _TqdmLoggingHandler(tqdm_class=TqdmDummy)
    handler.emit(record)

    assert 'test_record_message' == handler.tqdm_class.write_args[0]
    assert handler

# Generated at 2022-06-14 13:30:48.247752
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    from tqdm.contrib import log_and_tqdm

    LOG = logging.getLogger(__name__)

    def test_fn():
        for i in log_and_tqdm(range(9)):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        assert 'console logging redirected to `tqdm.write()`' in tqdm.write.get_instances()[0]._instances[0]._total['desc']

    test_fn()

# Generated at 2022-06-14 13:31:07.575976
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    # Prepare logging output
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s:%(message)s")
    # create console handler and set level to debug
    # ch = logging.StreamHandler(sys.stdout)
    # ch.setLevel(logging.DEBUG)
    # add formatter to ch
    # ch.setFormatter(formatter)
    # add ch to logger
    # LOG.addHandler(ch)

    with tqdm_logging_redirect() as pbar:
        LOG.info("This message should appear only in tqdm")
        with tqdm_logging_redirect():
            LOG.info("This message should appear only in tqdm")

# Generated at 2022-06-14 13:31:12.677363
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm() as pbar:
        for _ in xrange(2):
            logging.info("Test for logging_redirect_tqdm")
    logging.info("logging redirect removed")



# Generated at 2022-06-14 13:31:18.090932
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        import logging
        import tqdm
    except ImportError:
        return
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect():
        for i in tqdm.trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:31:23.073368
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    from tqdm import trange
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect() as pbar:
        for i in trange(9):
            pbar.update()
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
                # logging restored

# Generated at 2022-06-14 13:31:27.120362
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    log = logging.getLogger(__name__)
    with logging_redirect_tqdm(loggers=[log]) as redirect:
        log.info('tqdm')
        log.info('logging')
        log.info('redirect')
        log.info('tqdm')
    # Outside of logging_redirect_tqdm context
    log.info('logging')



# Generated at 2022-06-14 13:31:36.233648
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests import TestCase
    from tqdm import trange  # pylint: disable=unused-variable

    class Test(TestCase):
        def test_logging_redirect_tqdm(self):
            import logging
            LOG = logging.getLogger(__name__)

            with self.capture_output() as (out, err):
                logging.basicConfig(level=logging.INFO)
                with logging_redirect_tqdm():
                    for _ in trange(9):
                        if _ == 4:
                            LOG.info("console logging redirected to `tqdm.write()`")
            self.assertEqual(err.getvalue(), 'console logging redirected to `tqdm.write()`\n')
            self.assertNotEqual(out.getvalue(), '')


# Generated at 2022-06-14 13:31:48.262056
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    for tqdm_class in (std_tqdm, std_tqdm.tqdm):
        for level in ('INFO', 'WARNING', 'ERROR'):
            with tqdm_class(total=1) as pbar, logging_redirect_tqdm(tqdm_class=tqdm_class):
                record = logging.Logger('test').makeRecord('test', logging.getLevelName(level),
                                                           '', 0, 'Testing %s', (), {}, None)
                logging.getLogger('test').handle(record)  # pylint: disable=no-member
                pbar.update(1)
                assert not pbar.leave, "leave was `True`"


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:31:58.296958
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Ensure tqdm.contrib.logging works as expected.
    """
    from logging import basicConfig, getLogger, CRITICAL
    from tqdm import trange
    from tqdm.auto import tqdm

    basicConfig(level=CRITICAL)

    # This is the main test
    LOG = getLogger(__name__)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

    # Extra tests for function tqdm_logging_redirect

# Generated at 2022-06-14 13:32:02.685079
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    loggers = None
    with tqdm_logging_redirect(
            total=10, leave=False, desc="test", loggers=loggers) as pbar:
        assert pbar is not None

# Generated at 2022-06-14 13:32:08.419890
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    logging.basicConfig(format='%(asctime)-15s - %(message)s', level=logging.INFO)
    LOGGER = logging.getLogger(__name__)
    with tqdm_logging_redirect(total=5, loggers=[LOGGER]) as pbar:
        for i in range(5):
            time.sleep(0.1)
            pbar.update()
            if i == 4:
                LOGGER.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:32:40.684851
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    import logging

    class tqdm:
        def __init__(self, file=None):
            self.file = file
        def write(self, txt, file=None):
            if file:
                file.write(txt)
            else:
                self.file.write(txt)

    # create logger
    logger = logging.getLogger('Test logger')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = _TqdmLoggingHandler(tqdm)
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch


# Generated at 2022-06-14 13:32:44.223136
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging

    logger = logging.getLogger("tqdm.contrib.logging")
    logger.setLevel(logging.INFO)
    with logging_redirect_tqdm(loggers=[logger]):
        for i in range(5):
            logger.info("Hello " + str(i))

# Generated at 2022-06-14 13:32:50.990771
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in std_tqdm(range(9)):
                if i == 4:
                    logging.info("console logging redirected to `std_tqdm.write()`")
    except:  # noqa pylint: disable=bare-except
        assert False, 'Error from tqdm_logging_redirect'
    assert True, 'Success from tqdm_logging_redirect'

# Generated at 2022-06-14 13:32:57.051784
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    TQDM_CLASS = std_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored



# Generated at 2022-06-14 13:33:05.576901
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    LOG = logging.getLogger(__name__)

    def test_fn(dataset_len, epochs):
        """
        This function tests tqdm_logging_redirect with a basic logging test.
        Simply verifies that the output is as expected.
        """
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

        from tqdm import trange

        for i in trange(epochs, ncols=80, ascii=True, desc="Epoch"):
            LOG.info("Epoch: %i" % i)
            for j in range(dataset_len):
                LOG.info("Iteration %i of %i" % (j, dataset_len))

    dataset_len = 10
    epochs = 10

    import String

# Generated at 2022-06-14 13:33:13.289644
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger()

    # It should output logs to tqdm
    with tqdm_logging_redirect(loggers=[LOG]) as pbar:
        pbar.write('tqdm1')
        LOG.info('log1')
        pbar.write('tqdm2')
        LOG.info('log2')
        pbar.write('tqdm3')
        LOG.info('log3')


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:20.486813
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        _ = sys.stdout, sys.stderr
        sys.stdout = sys.__stdout__ = sys.stderr = sys.__stderr__ = StringIO()
    except AttributeError:  # not available under Windows
        pass
    try:
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")
    finally:
        try:
            sys.stdout, sys.stderr = _
        except AttributeError:  # not available under Windows
            pass

# Generated at 2022-06-14 13:33:30.522948
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    pass
#     import logging
#     import random
#     from tqdm import tqdm
#     from tqdm.contrib.logging import tqdm_logging_redirect

#     def long_process():
#         LOG = logging.getLogger(__name__)
#         for i in range(3):
#             r = random.random()
#             LOG.info('random number = {}'.format(r))
#             for _ in range(2):
#                 yield

#     if __name__ == '__main__':
#         logging.basicConfig(level=logging.INFO)
#         with tqdm_logging_redirect() as pbar:
#             for _ in pbar(long_process()):
#                 sleep(0.01)

# Generated at 2022-06-14 13:33:33.830122
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        import logging
        from tqdm import std
    except ImportError:
        return
    with logging_redirect_tqdm():
        print("1")
        logging.info("2")
        logging.warning("3")
        std.tqdm.write("4")
    print("5")

# Generated at 2022-06-14 13:33:42.871004
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import tqdm
    log = logging.getLogger()
    log.handlers = []  # remove existing handlers
    log.addHandler(logging.StreamHandler(sys.stdout))
    log.setLevel(logging.DEBUG)
    with tqdm.tqdm_logging_redirect():
        log.info('Debug with tqdm.')
    with tqdm.tqdm_logging_redirect(loggers=[log], tqdm_class=tqdm.tqdm):
        log.info('Debug with tqdm.')

# Generated at 2022-06-14 13:34:30.521183
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Tests for `tqdm_logging_redirect`
    """
    from sys import stdout
    import logging
    logging.basicConfig(level=logging.INFO)

    def log_and_print(s):
        logging.info(s)
        print(s)

    with tqdm_logging_redirect(loggers=[logging.getLogger('foo')]) as pbar:
        log_and_print('foo')

    log_and_print('bar')
    assert pbar.get_lock().locked()

    with tqdm_logging_redirect(loggers=[logging.getLogger('foo')]) as pbar:
        log_and_print('bar')


# Generated at 2022-06-14 13:34:40.771853
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import multiprocessing
    import sys
    from ..std import StringIO
    from .tqdm_gui import tqdm_gui

    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.INFO)

    # `tqdm.contrib.logging` functionality
    buffer = StringIO()
    with tqdm_logging_redirect(
            stream=buffer,
            tqdm_class=tqdm_gui,
            loggers=[LOGGER],
    ) as pbar:
        for i in range(10):
            LOGGER.info("TQDM + Log")
            pbar.update()
            LOGGER.info("TQDM + Logs")
            pbar.update()
            if i == 5:
                pbar.close()

# Generated at 2022-06-14 13:34:47.295301
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import shutil
    from .tests_tqdm import pretest_posttest, closing, StringIO, strjoin


# Generated at 2022-06-14 13:34:53.945037
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from six import PY3
    handler = _TqdmLoggingHandler()
    if PY3:
        handler.stream = StringIO()
    else:
        handler.stream = StringIO(unicode(''))
    level = logging.WARNING
    msg = 'warning message'
    handler.emit(logging.LogRecord(level, msg, 'my_module', 0, 'line', None, None))
    assert handler.stream.getvalue().strip() == msg
    assert len(handler.stream.getvalue().strip()) == len(msg)

# Generated at 2022-06-14 13:35:03.131328
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    This function requires to be executed in main to work properly.
    Test the work of :func:`tqdm.contrib.logging.logging_redirect_tqdm`.
    """
    from tqdm import trange
    from .logging import logging_redirect_tqdm
    import logging

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:35:07.476196
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import logging as std_logging, sys

    log = std_logging.getLogger(__name__)
    with logging_redirect_tqdm():
        log.info('foo')
        log.info('bar')
    assert sys.stderr.getvalue() == 'foo\nbar\n'

# Generated at 2022-06-14 13:35:14.721441
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from tqdm import tqdm

    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    with mock.patch('sys.stdout') as stdout:
        logging_redirect_tqdm()
        logging.info('foo')
        stdout.write.assert_called_once_with('foo\n')

    try:
        from unittest import TestCase
    except ImportError:
        TestCase = object


# Generated at 2022-06-14 13:35:24.526342
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    from tqdm.contrib.logging import tqdm_logging_redirect

    with StringIO() as recorded_output:
        logger = logging.getLogger('test_tqdm_logging_redirect')
        logger.propagate = False
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        logger.debug('ignore')
        with tqdm_logging_redirect(
                loggers=[logger],
                file=recorded_output,
                miniters=1) as pbar:
            pbar.set_description("tqdm test")

# Generated at 2022-06-14 13:35:31.640480
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    # Create output for test
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)

    if __name__ == '__main__':
        with logging_redirect_tqdm():
            for i in trange(2):
                if i == 0:
                    LOG.info("console logging redirected to `tqdm.write()`")
        logging.info("console logging restored.")


# Generated at 2022-06-14 13:35:38.642290
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import os
    import logging
    from tqdm import trange
    from .logging_redirect_tqdm import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if os.environ.get('TEST_TQDM_LOGGING_REDIRECT'):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    else:
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            os.environ['TEST_TQDM_LOGGING_REDIRECT'] = '1'
            # run script with logging_redirect_tqdm()

# Generated at 2022-06-14 13:37:10.846835
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():  # pragma: no cover
    try:
        import tqdm as std_tqdm
        _TqdmLoggingHandler(tqdm_class=std_tqdm).emit(logging.LogRecord(
            'test', logging.INFO, '', 0, 'TEST', (), None))
    except:  # noqa pylint: disable=bare-except
        print("Tests skipped because you did not install `tqdm` package.")
    _TqdmLoggingHandler(tqdm_class=std_tqdm).emit(logging.LogRecord(
        'test', logging.ERROR, '', 0, 'TEST', (), None))

# Generated at 2022-06-14 13:37:21.323070
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Run logging_redirect_tqdm(loggers=loggers, tqdm_class=tqdm_class).
    """
    import logging
    from tqdm import tqdm, trange

    # Set logger
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)
    log.addHandler(logging.NullHandler())

    # Test
    with tqdm_logging_redirect(log):
        # Do not use log.debug, since it is silenced
        for _ in trange(1):
            log.info('inf')
            log.warning('wrn')
            log.error('err')
            log.critical('crt')


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:37:28.781765
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    def do_logging():
        logger = logging.getLogger('foo')
        logger.setLevel(logging.DEBUG)
        logger.info('info')
        logger.warn('warn')
        logger.error('error')

    tqdm_class = std_tqdm  # type: Type[std_tqdm]
    with tqdm_class(total=0, leave=True) as pbar:
        try:
            with logging_redirect_tqdm(loggers=[logging.getLogger('foo')],
                                       tqdm_class=tqdm_class):
                do_logging()
        except Exception:
            assert False, ("logging_redirect_tqdm() does not work as expected")

    assert tqdm_class.write.get_lock().read

# Generated at 2022-06-14 13:37:37.353129
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import os
    import tempfile
    import logging
    import time
    import numpy as np
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                time.sleep(1)



# Generated at 2022-06-14 13:37:47.917322
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: () -> None
    from io import StringIO
    from tqdm import tqdm, tqdm_notebook, tqdm_pandas

    TQDM_CLASSES = [tqdm, tqdm_notebook, tqdm_pandas]
    for tqdm_class in TQDM_CLASSES:
        stream = StringIO()
        handler = _TqdmLoggingHandler(tqdm_class=tqdm_class)
        handler.stream = stream
        record = logging.makeLogRecord({
            'msg': 'hello world', 'levelno': logging.DEBUG})

        handler.emit(record)
        handler.flush()
        assert stream.getvalue() == 'hello world\n'

        stream.seek(0)
        stream.truncate(0)
       