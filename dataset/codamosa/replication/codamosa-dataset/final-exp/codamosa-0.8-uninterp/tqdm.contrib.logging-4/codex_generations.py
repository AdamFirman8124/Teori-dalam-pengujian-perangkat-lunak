

# Generated at 2022-06-14 13:27:47.028450
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    # Patch the function tqdm_logging_redirect
    with patch('tqdm.contrib.logging.tqdm_logging_redirect') as p:
        # Call the function tqdm_logging_redirect with 3 arguments
        tqdm_logging_redirect(1, 2, 3)

        # Check if the function has been called with the good arguments
        assert p.call_count == 1
        call_args, _ = p.call_args
        assert call_args == (1, 2, 3)



# Generated at 2022-06-14 13:27:52.826228
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """
    Test function tqdm_logging_redirect.
    """
    import time
    import logging
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect():
        LOG.info("console logging redirected to `tqdm.write()`")
        time.sleep(0.01)

# Generated at 2022-06-14 13:28:02.515044
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm.
    """

# Generated at 2022-06-14 13:28:10.257742
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    with patch('sys.stdout', new=None) as stdout, \
            patch('tqdm.tqdm.write') as write, \
            logging_redirect_tqdm():
        print('foo')
    assert write.called_with('foo\n')



# Generated at 2022-06-14 13:28:15.567405
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logger = logging.getLogger(__name__)
    try:
        # old logger format
        old_format = logger.handlers[0].formatter._fmt
    except IndexError:
        # new logger format
        old_format = logger.handlers[0].formatter._style._fmt
    old_handlers = logger.handlers
    with logging_redirect_tqdm() as pbar:
        for i in pbar(range(4)):
            logger.info("progress: {}".format(i))
        logger.info("done")
    assert pbar.n == 4
    assert logger.handlers == old_handlers
    assert logger.handlers[0].formatter._fmt == old_format



# Generated at 2022-06-14 13:28:20.423223
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with tqdm_logging_redirect(
        total=4, ascii=True, dynamic_ncols=True, loggers=logging.getLogger('log_a')) as pbar:
        pbar.set_description("Redirecting log_a")
        logging.getLogger('log_b').info("logging to log_b")
        logging.getLogger('log_a').info("logging to log_a")
        pbar.update()

        logging.getLogger('log_b').info("logging to log_b")
        logging.getLogger('log_a').info("logging to log_a")
        pbar.update()

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:28:21.935507
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    test_logger = logging.getLogger("tqdm_tests")
    test_logger.addHandler(_TqdmLoggingHandler(std_tqdm))
    test_logger.info("Some text to test")

# Generated at 2022-06-14 13:28:32.678092
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange
    import sys

    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # create logging record
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # check that message is being printed
    for i in trange(9):
        if i == 4:
            LOG.info("console logging redirected to `tqdm.write()`")
    assert sys.stderr.getvalue() == u'\n'.join(
        [u'[INFO] console logging redirected to `tqdm.write()`', u''])

# Generated at 2022-06-14 13:28:41.420707
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    import logging

    # Dummy function to simulate the computation
    def compute():
        logging.info("hello")
        for i in tqdm(range(10), desc="compute"):
            i

    import io
    import sys
    old_stream = sys.stdout
    sys.stdout = io.StringIO()  # capture output

    with tqdm_logging_redirect(desc="outer"):
        compute()
    sys.stdout = old_stream
    output_str = sys.stdout.getvalue()
    # Search for the logging output string
    assert ("outer: 100%|##########| 1 of 1 complete"
            in output_str)
    assert "compute: 100%|##########| 10 of 10 complete" in output_str
    assert "hello"

# Generated at 2022-06-14 13:28:51.047614
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        import unittest as ut
        import contextlib
    except ImportError:
        import unittest2 as ut
        import unittest2.util as contextlib
    import StringIO
    import logging

    class OutputTqdm(std_tqdm):
        def __init__(self, **kwargs):
            super(OutputTqdm, self).__init__(**kwargs)
            self.output = StringIO.StringIO()

        def write(self, msg, *args, **kwargs):
            self.output.write(msg)
            return super(OutputTqdm, self).write(msg, *args, **kwargs)


# Generated at 2022-06-14 13:29:01.838511
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
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
    assert True



# Generated at 2022-06-14 13:29:07.291167
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    # Unit test
    logging.basicConfig()
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm(tqdm_class=std_tqdm):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    logging.shutdown()
    return True



# Generated at 2022-06-14 13:29:16.279051
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import unittest
    import sys
    import logging
    import cStringIO

    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

    # test logging.basicConfig(level=logging.INFO)
    stdout = sys.stdout
    sys.stdout = cStringIO.StringIO()
    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
    sys.stdout = stdout

    # test no logger given (logging.root)

# Generated at 2022-06-14 13:29:20.978454
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from tqdm.auto import trange

    loggers = [logging.root]
    original_handlers_list = [logger.handlers for logger in loggers]
    with logging_redirect_tqdm():
        for i in trange(9):
            if i in [2, 5]:
                logging.info("console logging redirected to `tqdm.write()`")
    # logging restored
    assert loggers[0].handlers == original_handlers_list[0]

# Generated at 2022-06-14 13:29:29.295851
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    class CustomTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):  # pylint: disable=super-init-not-called
            self.write_called = False
            self.msg = None

        def write(self, msg):
            self.write_called = True
            self.msg = msg

    custom_tqdm = CustomTqdm()
    formatter = logging.Formatter('%(message)s')

    with logging_redirect_tqdm(tqdm_class=CustomTqdm):
        logging.getLogger('test').info('test1')

    assert custom_tqdm.write_called
    assert custom_tqdm.msg == 'test1'


# Generated at 2022-06-14 13:29:39.774411
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import pretest_posttest  # pylint: disable=wrong-import-order
    from .tests import _test_logging_redirect  # pylint: disable=wrong-import-order

    for tqdm in [std_tqdm, pretest_posttest(std_tqdm)]:
        with tqdm_logging_redirect(desc='test_logging_redirect', total=1,
                                   loggers=[logging.root], tqdm_class=tqdm) as _pbar:
            _test_logging_redirect(tqdm_class=tqdm)

test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:29:42.559297
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        LOG = logging.getLogger(__name__)
        LOG.info("test1")
    LOG.info("test2")

# Generated at 2022-06-14 13:29:54.542089
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """ Test conditional execution of logging_redirect_tqdm """
    import os
    import sys
    import contextlib
    import unittest
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    # In case of testing, the environment variable may not be set.
    os.environ['TEST_TQDM'] = '1'

    @contextlib.contextmanager
    def capture_sys_output():
        capture_out, capture_err = StringIO(), StringIO()
        current_out, current_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = capture_out, capture_err
            yield capture_out, capture_err
        finally:
            sys.stdout, sys.stderr = current_

# Generated at 2022-06-14 13:30:02.204179
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    log_str = ''

    class TestTqdm(std_tqdm):
        def write(self, s, file=None):
            global log_str  # pylint: disable=global-statement
            log_str += s

    with tqdm_logging_redirect(loggers=[LOG], tqdm_class=TestTqdm):
        LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

    assert log_str == 'INFO:__main__:console logging redirected to `tqdm.write()`\n'

# Generated at 2022-06-14 13:30:09.314493
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """
    Test tqdm_logging_redirect.
    """
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(desc="tqdm_logging_redirect") as pbar:
            for i in trange(9):
                pbar.set_description("test_tqdm_logging_redirect")
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:30:28.531855
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    # https://github.com/tqdm/tqdm/issues/629
    LOG = logging.getLogger(__name__)

    try:
        with tqdm_logging_redirect(range(10),
                                   logger_ref=LOG,
                                   loggers=[logging.getLogger(__name__)],
                                   tqdm_class=std_tqdm):
            for i in range(10):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
    finally:
        # logging restored
        assert len(LOG.handlers) == 0, 'logging handlers not restored'

# Generated at 2022-06-14 13:30:33.983372
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


# Generated at 2022-06-14 13:30:42.330711
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import sys
    from contextlib import contextmanager
    from sys import stderr
    from tqdm import tqdm

    @contextmanager
    def my_tqdm(*args, **kwargs):
        """
        A dummy tqdm class with a `__enter__` method that prints
        a message to `stderr`
        """
        errmsg = kwargs.pop('errmsg', 'Entering tqdm')
        stderr.write(errmsg)
        yield

    # We catch `tqdm` output to suppress it

# Generated at 2022-06-14 13:30:48.425022
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for _ in tqdm(range(9)):
            if _ == 4:
                LOG.info('console logging redirected to `tqdm.write()`')
    # logging restored


# Generated at 2022-06-14 13:30:53.435707
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import mock
    import tqdm.contrib.logging
    from tqdm.contrib.logging import _TqdmLoggingHandler
    from tqdm.std import tqdm
    from tqdm import std
    from sys import version_info

    # Case 1:
    # Input: m_logger.info("message"), where m_logger is a mocked Logger
    # Expectation: The message "message" is written to the tqdm.std.tqdm's file

    tqdm_std_file = tqdm.std.tqdm.__dict__["_file"]
    with mock.patch('tqdm.contrib.logging.std_tqdm.write') as m_tqdm_write:
        # create mocked loggers, records and files
        m_logger = mock

# Generated at 2022-06-14 13:30:58.345819
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    def do_sleep(sec):
        time.sleep(sec)
        LOG.info('Done sleeping...')

    with tqdm_logging_redirect(
            loggers=[logging.root],
            total=4,
            desc='Waiting',
            disable=False) as pbar:
        for _ in range(4):
            do_sleep(0.5)
            pbar.update(1)

# Generated at 2022-06-14 13:31:07.157515
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from .helpers import closing
    from .tqdm import trange
    from .autonotebook import tqdm

    logging.basicConfig(level=logging.INFO)

    with closing(tqdm(total=10)) as pbar:
        with logging_redirect_tqdm(tqdm_class=tqdm):
            for i in trange(9):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")
        assert pbar.n == 9 and pbar.total == 10
        pbar.update(1)
        assert pbar.n == 10 and pbar.total == 10


# Generated at 2022-06-14 13:31:14.343808
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
            total=10,
            unit="It",
            desc="Example",
        ):
            for i in range(10):
                if i == 4:
                    LOG.info("console logging redirected to tqdm.write()")
        # logging restored

# Generated at 2022-06-14 13:31:21.225795
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    def test_logging_redirect_tqdm():
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
    test_logging_redirect_tqdm()



# Generated at 2022-06-14 13:31:28.868770
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # setup
    tqdm_handler = _TqdmLoggingHandler(std_tqdm)
    tqdm_handler.stream = sys.stdout

    # call
    tqdm_handler.emit(logging.LogRecord('name', logging.INFO,
                                        'file', 1, 'test_message', (), None,
                                        'func'))
    # test
    assert tqdm_handler.stream.getvalue() == 'test_message\n'



# Generated at 2022-06-14 13:32:00.648892
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import pretest_posttest

    @pretest_posttest
    def unit_test_logging_redirect_tqdm(
        loggers=None,  # type: Optional[List[logging.Logger]],
        tqdm_class=std_tqdm  # type: Type[std_tqdm]
    ):
        from .tests import tqdm_cls_arg

        # Checked tqdm_logging_redirect function
        console_output = []  # type: List[str]
        # set up logger
        tqdm_handler = _TqdmLoggingHandler(tqdm_class)
        logger = logging.getLogger()
        logger.addHandler(tqdm_handler)
        logger.setLevel(logging.INFO)
        # Standard logger
       

# Generated at 2022-06-14 13:32:06.064510
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from nose.plugins.skip import SkipTest
    raise SkipTest("Not implemented")
    # # Testing with default tqdm=tqdm.std.tqdm
    # with tqdm_logging_redirect():
    #     pass
    # # Testing with custom tqdm class
    # with tqdm_logging_redirect(tqdm_class=tqdm.tqdm):
    #     pass

# Generated at 2022-06-14 13:32:08.316907
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm
    with logging_redirect_tqdm():
        logging.info("Test message")

# Generated at 2022-06-14 13:32:12.847523
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:32:17.706492
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:32:22.438205
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import logging
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(desc='Test tqdm_logging_redirect') as pbar:
        for _ in range(10):
            logging.info("Total progress: %d/10", pbar.n)
            pbar.update(1)

# Generated at 2022-06-14 13:32:31.077111
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(unit='B',
                               total=100,
                               ascii=True) as pbar:
        for _ in pbar:
            pass
        LOG.info('test INFO')
        LOG.info('test ERROR')
        LOG.info('test WARNING')
        LOG.info('test DEBUG')

        assert pbar.n == 100, "pbar.n is not 100"



# Generated at 2022-06-14 13:32:38.919951
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    import logging
    from tqdm.contrib.concurrent import ProcessPoolExecutor
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with ProcessPoolExecutor(max_workers=2) as executor:
        with logging_redirect_tqdm():
            for _ in executor.map(LOG.info, ["console logging redirected to `tqdm.write()`"]*9):
                pass

# Generated at 2022-06-14 13:32:47.527766
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import trange
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    # Dummy handler for standard output
    stringio = StringIO()  # type: StringIO

    import logging
    LOG = logging.getLogger(__name__)
    try:
        for i in trange(4):
            LOG.info("Please ignore this dummy loop")
    except AttributeError:
        pass
    if 'attach_stderr_handler' in logging.__dict__:
        logging.attach_stderr_handler()
    logging.basicConfig(level=logging.INFO, stream=stringio)

    with logging_redirect_tqdm():
        LOG.info("Redirected logging")


# Generated at 2022-06-14 13:32:56.818068
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    try:
        from logging import NullHandler  # type: ignore[attr-defined]
    except ImportError:  # pragma: no cover
        from logging import Handler  # type: ignore[attr-defined]

        class NullHandler(Handler):  # type: ignore[attr-defined]
            def emit(self, record):  # type: ignore[override]
                pass

    class TestTqdm(std_tqdm):  # type: ignore[no-redef]
        def __init__(
            self,
            *args,  # type: Any
            **kwargs
        ):
            test_records = kwargs.pop('test_records')
            super(TestTqdm, self).__init__(*args, **kwargs)
            self.test_records = list

# Generated at 2022-06-14 13:33:44.286870
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    original_handlers_list = [logging.root.handlers]
    tqdm_kwargs = {'unit': 'blocks'}
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        original_handlers_list = [logging.root.handlers]
        with tqdm_logging_redirect(total=9, **tqdm_kwargs) as pbar:
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                pbar.update()
        # logging restored
        assert original_handlers_

# Generated at 2022-06-14 13:33:53.795131
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from ..std import tqdm
    import logging
    import io

    stream = io.StringIO()
    handler = _TqdmLoggingHandler(tqdm)
    handler.stream = stream
    logging_record = logging.LogRecord(
        'name', logging.INFO, 'foo_path', 3, 'bar', [], 'baz')
    handler.emit(logging_record)
    assert stream.getvalue() == "bar\n"



# Generated at 2022-06-14 13:34:00.291237
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Test the _TqdmLoggingHandler.emit() method.

    Create a new handler, retrieve a logger and assign it to the new handler.
    Use this logger to send a record to the new handler and check that the
    associated stream has been written to.
    """
    handler = _TqdmLoggingHandler()
    logger = logging.getLogger('tqdm')
    logger.propagate = False
    logger.handlers = [handler]
    logger.error('test emit')
    assert(handler.stream.getvalue() == 'ERROR:tqdm:test emit\n')

# Generated at 2022-06-14 13:34:06.011667
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from pytest import raises

    loggers = [logging.getLogger(__name__)]
    with logging_redirect_tqdm(loggers=loggers) as pbar:
        pbar.write("console logging redirected to `tqdm.write()`")
    tqdm.write("logging restored")

# Generated at 2022-06-14 13:34:14.657382
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    import unittest
    from tqdm import tqdm_notebook as tqdm  # pylint: disable=unused-import
    from tqdm.contrib.logging import logging_redirect_tqdm, tqdm_logging_redirect

    class TestTqdmLoggingRedirect(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.logger = logging.getLogger(__name__)
            # cls.logger.setLevel(logging.INFO)
            # cls.logger.addHandler(logging.StreamHandler())
            # cls.logger.propagate = False

        def test_logging_redirect_tqdm(self):
            total = 5

# Generated at 2022-06-14 13:34:18.770740
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect
    LOG = logging.getLogger(__name__)
    LOG.propagate = False
    LOG.setLevel(logging.INFO)
    if __name__ == '__main__':
        with tqdm_logging_redirect(tqdm_class=tqdm) as pbar:
            for i in pbar(range(3)):
                if i == 1:
                    LOG.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:34:27.306224
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib import logging as tqdm_logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    import sys
    import io

    LOG = logging.getLogger(__name__)


# Generated at 2022-06-14 13:34:38.248460
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    old_handlers = logging.root.handlers[:]


# Generated at 2022-06-14 13:34:44.442868
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests_tqdm import with_setup, _range, pretest, posttest

    logging.basicConfig(level=logging.INFO)
    @with_setup(pretest, posttest)
    def test_with_logging():
        with logging_redirect_tqdm(loggers=[logging.root]):
            for i in _range(9):
                logging.info("test1 {}".format(i))
        # log to console again
        for i in _range(3):
            logging.info("test2 {}".format(i))
    test_with_logging()



# Generated at 2022-06-14 13:34:49.696165
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """If `logging_redirect_tqdm` doesn't crash, it's working."""
    import logging
    from tqdm import trange
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm(loggers=[LOG]):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:36:14.305791
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import time
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        logger = logging.getLogger()
        logger.info("test 0")
        logger.info("test 1")
        logger.info("test 2")
        time.sleep(0.05)
        logger.info("test 3")
        logger.info("test 4")
        logger.info("test 5")
        time.sleep(0.05)
        logger.info("test 6")
        logger.info("test 7")
        logger.info("test 8")



# Generated at 2022-06-14 13:36:19.716512
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    LOG = logging.getLogger(__name__)
    def main():
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

    if __name__ == '__main__':
        return main()


# Generated at 2022-06-14 13:36:29.170730
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    # import tqdm.std as std_tqdm

    LOG = logging.getLogger(__name__)

    # Create Formatter
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s[%(funcName)s] : %(message)s')

    # Create and add Handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    LOG.addHandler(handler)

    # Set Logging Level
    LOG.setLevel(logging.DEBUG)

    LOG.debug("Hello World!")


# Generated at 2022-06-14 13:36:37.083827
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm  # type: ignore
    from tqdm import contrib
    with tqdm(total=10, ncols=0) as pbar:
        with contrib.logging_redirect_tqdm() as pbar:
            for _ in range(5):
                pbar.update()
                # print('hello')
            logging.info('console logging redirected to `tqdm.write()`')
            for _ in range(5, 10):
                pbar.update()
                # print('world!')

# test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:36:44.168526
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    handler = _TqdmLoggingHandler()

    # Check that we capture the normal case when logging.debug("my_message")
    record = logging.LogRecord('tqdm', logging.DEBUG,
            '/home/foo/bar/baz.py', 73, 'my_message', None, None)
    handler.emit(record)
    assert handler.stream.getvalue().split('\n')[-1] == 'my_message'

    # Check that we capture the case when logging.debug("my_message", exc_info=True)
    record = logging.LogRecord('tqdm', logging.DEBUG,
            '/home/foo/bar/baz.py', 73, 'my_message', None, None)
    handler.emit(record)

# Generated at 2022-06-14 13:36:54.929472
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():

    # Setup a logger and add custom logging handler to
    # it. The logging handler will track the logs emitted
    # to the defined stream.
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    # Dummy functions to test the logger's behaviour
    def log_func():
        LOG.debug("Test DEBUG log")
        LOG.info("Test INFO log")
        LOG.warning("Test WARNING log")
        LOG.error("Test ERROR log")
        LOG.critical("Test CRITICAL log")

    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG)
        # Capture stdout stream
        import io
        from contextlib import redirect_stderr

# Generated at 2022-06-14 13:37:00.507387
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from tqdm import trange
    except ImportError:
        return None

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
    # logging restored
    logging.info("INFO message written after the end of the context manager.")

# Generated at 2022-06-14 13:37:10.148866
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Test redirection of logging to tqdm.write().
    """
    import logging
    from tqdm import tqdm

    # Logging setup
    logging.basicConfig(level=logging.DEBUG)

    # In-function logging
    def debug_logging():
        # type: () -> None
        LOG = logging.getLogger(__name__)
        for i in range(9):
            LOG.debug(i)
            LOG.info(i)
            LOG.warning(i)
            LOG.error(i)
            LOG.critical(i)

    # Without redirect
    debug_logging() # DEBUG, INFO, WARNING, ERROR, CRITICAL


    # With redirect
    with tqdm_logging_redirect(bar_format='{desc}'):
        debug_logging()



# Generated at 2022-06-14 13:37:18.817939
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .utils import TestHandler
    from .std import trange

    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    test_handler = TestHandler()
    log.addHandler(test_handler)

    with logging_redirect_tqdm(tqdm_class=std_tqdm) as pbar:
        for _ in trange(9):
            log.info("console logging redirected to `tqdm.write()`")

    assert test_handler.entries == []
    assert pbar._dynamic_console.ncols == 120

# Generated at 2022-06-14 13:37:26.007593
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from tqdm.std import tqdm
    handler = _TqdmLoggingHandler()
    with tqdm(total=5, file=sys.stdout) as pbar:
        record = logging.LogRecord("test_logger", logging.INFO, '/test/path.py', 40, 'This is a test log record.', [], None)
        handler.tqdm_class = pbar.__class__
        handler.stream = pbar.fp
        handler.emit(record)
        assert pbar.n == 5
        assert pbar.last_print_n == 5
        assert pbar.last_print_t == 0.0
        assert pbar.total == 5
