

# Generated at 2022-06-14 13:27:50.134397
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

# Generated at 2022-06-14 13:27:56.368509
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from tqdm.std import tqdm

        with tqdm_logging_redirect(
            total=100,
            # loggers=[logging.root],
            # tqdm_class=tqdm
        ) as pbar:
            for i in range(100):
                if i == 50:
                    logging.info("console logging redirected to `tqdm.write()`")
                pbar.update()
        assert isinstance(pbar, tqdm)
    except ImportError:
        pass

# Generated at 2022-06-14 13:28:01.279344
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import os
    import subprocess
    import tempfile
    from tqdm import tqdm

    test_dir = os.path.join(tempfile.gettempdir(), "test_tqdm_logging_redirect_tqdm")
    try:
        os.makedirs(test_dir)
    except OSError:
        pass
    # flake8: noqa

# Generated at 2022-06-14 13:28:09.764698
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import os
    import sys

    if sys.version_info < (3, 0):
        str_ = unicode  # noqa
    else:
        str_ = str

    with open("test.log", "w") as handler:
        logging.basicConfig(level=logging.DEBUG, stream=handler)
        with tqdm_logging_redirect(total=8, file=sys.stdout,
                                   tqdm_class=std_tqdm) as progress:
            progress.print("abcde\n")
            logging.info("test 1")
            progress.print("fghij\n")
            logging.info("test 2")
            progress.print("klmno\n")
            logging.info("test 3")

# Generated at 2022-06-14 13:28:14.536837
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm
    from .tests_tqdm import with_prog_bar

    with with_prog_bar('test_logging_redirect_tqdm') as pbar:
        with logging_redirect_tqdm():
            for i in trange(10, desc='test_logging_redirect_tqdm',
                            file=pbar.write):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:28:24.475013
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch  # py3
    except ImportError:
        from mock import patch  # py2

    from .test_tqdm import pretest_posttest, closing

    @closing(tqdm_instance=False)
    def _inner_test():
        logger = logging.getLogger()

        stream = sys.stdout
        original_handler = logging.StreamHandler(stream=stream)
        original_handler.setFormatter(logging.Formatter('%(message)s'))
        logger.handlers = [original_handler]

        level = logger.level
        logger.setLevel(logging.INFO)


# Generated at 2022-06-14 13:28:34.964298
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from io import StringIO
    import logging
    from tqdm import tqdm

    log = logging.getLogger(__name__)

    for _ in logging_redirect_tqdm():
        log.info('This should not be printed.')
        log.handlers[0].stream = StringIO()
        log.info('This should not be printed either.')

    assert 'This should not be printed' not in log.handlers[0].stream.getvalue()
    assert 'This should not be printed either' in log.handlers[0].stream.getvalue()

    for _ in logging_redirect_tqdm(tqdm_class=tqdm):
        log.info('This should not be printed.')
        log.handlers[0].stream = StringIO()

# Generated at 2022-06-14 13:28:41.066547
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def test_redirect(redirect=True):
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")

    print("--- logging -> stdout/stderr ---")
    test_redirect()

    print("--- logging -> tqdm ---")
    if redirect:
        with logging_redirect_tqdm():
            test_redirect()



# Generated at 2022-06-14 13:28:45.726692
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:28:54.684910
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    from tqdm import trange

    class TestLoggingRedirectTqdm(unittest.TestCase):

        def test_logging_redirect_tqdm(self):
            import logging
            from tqdm import trange
            from tqdm.contrib.logging import logging_redirect_tqdm

            LOG = logging.getLogger(__name__)

            if __name__ == '__main__':

                logging_redirect_tqdm_called = False

                logging.basicConfig(level=logging.INFO)
                with logging_redirect_tqdm():
                    logging_redirect_tqdm_called = True

# Generated at 2022-06-14 13:29:06.812461
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(asctime)s] %(module)s.%(funcName)s %(lineno)d\n%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logging.info('first logging info')
    with logging_redirect_tqdm():
        logging.info('second logging info')
    logging.info('third logging info')

# Generated at 2022-06-14 13:29:15.776017
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    try:
        import mock
    except ImportError:
        import unittest.mock as mock

    with mock.patch("sys.stdout") as mock_stdout, \
            mock.patch("sys.stderr") as mock_stderr, \
            mock.patch("sys.excepthook") as mock_excepthook:
        with logging_redirect_tqdm():
            logging.exception("exception")
            logging.error("error")
            logging.warning("warning")
            logging.info("info")
            logging.debug("debug")

        assert mock_stdout.method_calls == [
            ('write', ('error',)), ('flush', ())]

# Generated at 2022-06-14 13:29:18.184587
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): # pragma: no cover
    logging.info("hello world")
    with logging_redirect_tqdm():
        for i in range(10):
            logging.info("i = {}".format(i))

# Generated at 2022-06-14 13:29:23.635116
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    loggers = [logging.root]
    with tqdm_logging_redirect(loggers=loggers) as pbar:
        logger = logging.getLogger(__name__)
        logger.info('Test info logging')



# Generated at 2022-06-14 13:29:27.278964
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests_tqdm import pretest_posttest  # pylint: disable=unused-import
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        logging.info("progress bar")
        logging.info("another message")
        logging.info("another message")



# Generated at 2022-06-14 13:29:39.240025
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Test exceptions in method emit of class _TqdmLoggingHandler
    """
    # Define a class that raises exception with method write
    class ScaryTqdm():  # pylint: disable=too-few-public-methods
        """
        A Tqdm class that raises exceptions with method .write()
        """
        @staticmethod
        def write(*args, **kwargs):  # pylint: disable=unused-argument
            """
            Write arguments to stdout and raise exception
            """
            sys.stdout.write(*args)
            raise KeyboardInterrupt

    tqdm_handler = _TqdmLoggingHandler(tqdm_class=ScaryTqdm)
    try:
        tqdm_handler.emit('a message')
    except KeyboardInterrupt:
        pass
   

# Generated at 2022-06-14 13:29:49.326166
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests import TestCase, _range

    class TestProgress(TestCase):
        # pylint: disable=invalid-name

        def test_logging_redirect_tqdm(self):
            from .tests import closing, captured_stdout

            def parse_progressbar(s):
                # type: (str) -> int
                i = s.rfind('100%|')
                if i < 0:
                    raise AssertionError(s)
                i = s[i:].rfind('%')
                if i < 0:
                    raise AssertionError(s)
                return int(s[i - 3:i])


# Generated at 2022-06-14 13:29:59.074002
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect, logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(desc="redirected"):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    with logging_redirect_tqdm():
        for i in trange(9, desc="redirected"):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:30:06.967158
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class MyTqdm(std_tqdm):
        write_str = None  # type: Optional[str]

        def write(self, s, file=None):
            MyTqdm.write_str = s

    class MyHandler(_TqdmLoggingHandler):
        def __init__(self):
            super(MyHandler, self).__init__()
            self.tqdm_class = MyTqdm
            self.stream = sys.stdout

    handler = MyHandler()
    handler.emit(logging.LogRecord('foo', 0, __file__, 1, 'bar', None, None))
    assert MyTqdm.write_str == 'bar\n'



# Generated at 2022-06-14 13:30:12.084860
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console = _TqdmLoggingHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(console)
    logger.debug("debug")
    logger.info("info")
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")

# Generated at 2022-06-14 13:30:32.250819
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    log = logging.getLogger(__name__)

    # Test messages
    msg = "Testing that this message gets printed"
    log.debug(msg)
    log.info(msg)
    log.warning(msg)
    log.error(msg)
    log.critical(msg)

    for verbosity in [0, 1]:
        if verbosity == 0:
            # Redirect to tqdm.write()
            with logging_redirect_tqdm():
                pass
        else:
            assert 1 == 0

        # Test messages
        log.debug(msg)
        log.info(msg)
        log.warning(msg)
        log.error(msg)
        log.critical(msg)

    # Test that the redirection is reset after exit of context
    log.debug(msg)
   

# Generated at 2022-06-14 13:30:34.445854
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # make sure it can be imported without logging

    def do_test():
        # type: (...) -> None
        from .tests import _test_logging_redirect_tqdm
        _test_logging_redirect_tqdm()
    try:
        do_test()
    except ImportError:
        # logging is not installed
        pass

# Generated at 2022-06-14 13:30:39.376705
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.autonotebook import tqdm, tgrange

    # loghandler = tqdm_logging.TqdmLoggingHandler()
    # loghandler.setLevel(logging.INFO)
    # logger.addHandler(loghandler)

    for i in tgrange(9):
        if i == 4:
            logging.info("console logging redirected to `tqdm.write()`")
        assert i

# Generated at 2022-06-14 13:30:46.293123
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from ...tests import GITHUB_ACTIONS

    try:
        with logging_redirect_tqdm():
            raise NotImplementedError
    except NotImplementedError:
        pass
    else:
        raise ValueError

    import logging
    LOG = logging.getLogger('test_tqdmlogging')
    LOG.setLevel(logging.INFO)
    LOG.propagate = False
    LOG.handlers = []

    with tqdm_logging_redirect() as pbar:
        assert isinstance(pbar, std_tqdm)
        LOG.info("redirected console logging to `tqdm.write()`")
        pbar.update()
        pbar.write("some tqdm message")


# Generated at 2022-06-14 13:30:55.211783
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import io
    import sys
    import logging
    import tqdm
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    sys.stdout = io.StringIO()
    with tqdm_logging_redirect(
        # tqdm=tqdm.tqdm,  # type: ignore
        total=100,
    ):
        for i in range(100):
            log.info("test_tqdm_logging_redirect")
    sys.stdout = sys.__stdout__
    assert str(sys.stdout.getvalue()).count("test_tqdm_logging_redirect") == 100

# Generated at 2022-06-14 13:30:57.822530
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect():
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:31:04.486480
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    loggers = [logging.root]
    with tqdm_logging_redirect(loggers=loggers, tqdm_class=tqdm) as pbar:
        for i in range(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
                break


# Generated at 2022-06-14 13:31:16.241991
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import os
    import tqdm.contrib
    import tqdm.contrib.test

    # Suppress all logging from other than this test
    tqdm.contrib.test._suppress_logging()

    # Prepare for log messages
    file_prefix = '.' + os.path.basename(__file__) + '-' + 'test__TqdmLoggingHandler_emit'
    file_name = file_prefix + '.log'
    path = os.path.join(tqdm.contrib.test._get_tmp_dir(), file_name)
    tqdm.contrib.test._remove_files_with_prefix(file_prefix)

# Generated at 2022-06-14 13:31:26.908260
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm
    """
    import logging
    from . import tqdm_notebook as tn

    # test tqdm_class
    log1 = logging.getLogger(__name__)
    _log_messages(log1, "normal")
    with logging_redirect_tqdm(tqdm_class=tn.tqdm_notebook):
        _log_messages(log1, "notebook")
    _log_messages(log1, "normal")

    # test loggers
    log2 = logging.getLogger(__name__)
    log3 = logging.getLogger(__name__ + "2")
    log4 = logging.getLogger(__name__ + "2")

# Generated at 2022-06-14 13:31:32.054778
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import loading_bar

    def bar():
        with tqdm_logging_redirect(tqdm_class=loading_bar):
            import logging
            LOG = logging.getLogger(__name__)
            LOG.info("Test logging redirection to loading bar")

    # Redirect stdout to stderr for pytest
    sys.stdout = sys.stderr
    bar()

# Generated at 2022-06-14 13:32:09.394810
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Unit test for function logging_redirect_tqdm
    """
    try:
        # py2
        import StringIO  # type: ignore
    except ImportError:
        # py3
        from io import StringIO
    import logging

    # Create a new logger to which we can attach a handler
    logger = logging.getLogger(__name__)

    # create a handler and set its level (this could be stdout, stderr, a file, or anything else)
    log_capture_string = StringIO()
    handler = logging.StreamHandler(log_capture_string)
    handler.setLevel(logging.INFO)

    # set the default logging level of the logger (this is not needed)
    logger.setLevel(logging.INFO)

    # create a form

# Generated at 2022-06-14 13:32:14.271444
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    loggers = [logging.getLogger('logging_redirect_tqdm.test')]
    with logging_redirect_tqdm(loggers=loggers):
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:32:22.090734
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect
    result = []  # type: List[str]

    class SimpleTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):
            # type: (Any, Any) -> None
            super(SimpleTqdm, self).__init__(*args, **kwargs)
            # raise a custom exception if `set_description()` is called
            self.set_description = lambda x: 1 / 0

    def log_handler(record):
        result.append(record.getMessage())

    root_logger = logging.getLogger()
    orig_handlers = root_logger.handlers

# Generated at 2022-06-14 13:32:32.128264
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Test that the emit function of _TqdmLoggingHandler writes messages to the
    terminal and not to a file.
    """
    import io
    from tqdm import std
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    # Get output file and create a handler that writes to that file
    output_file = io.StringIO()
    handler = logging.StreamHandler(output_file)
    handler.setFormatter(logging.Formatter('%(message)s'))
    log.addHandler(handler)

    # Get output terminal and create a handler that writes to that terminal
    output_terminal = io.StringIO()
    tqdm_handler = _TqdmLoggingHandler(std.tqdm)

# Generated at 2022-06-14 13:32:42.529350
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():

    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm, tqdm_logging_redirect

    log_msg = "console logging redirected to tqdm.write()"


# Generated at 2022-06-14 13:32:53.548835
# Unit test for function logging_redirect_tqdm

# Generated at 2022-06-14 13:33:01.227301
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    logging.basicConfig(level=logging.INFO)
    # tqdm.monitor_interval = 0  # workaround for ipython

    with tqdm_logging_redirect(total=9) as pbar:
        for i in pbar:
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:33:04.943499
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    with tqdm_logging_redirect(desc="Test"):
        logging.warning("test")
        logging.info("test2")



# Generated at 2022-06-14 13:33:09.651605
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .main import tqdm

    logging.basicConfig(level=logging.INFO)
    with tqdm.contrib.logging.logging_redirect_tqdm():
        for i in tqdm.trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:33:15.807500
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests import SimpleLoggingTestCase

    test_msg = "test_msg"
    test_logger = logging.getLogger(__name__)

    class TestCase(SimpleLoggingTestCase):
        def test_logger_handler(self):
            with logging_redirect_tqdm():
                test_logger.info(test_msg)
                self.assertEqual(self.get_log_content(), test_msg + '\n')

    TestCase().run()

# Generated at 2022-06-14 13:33:55.953450
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    from tqdm import tqdm, trange

    with tqdm_logging_redirect():
        for i in trange(9):
            if i == 4:
                logging.info('console logging redirected to tqdm.write()')

# Generated at 2022-06-14 13:34:02.525820
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    logging.basicConfig(level=logging.INFO)
    if sys.version_info >= (3, 5):  # pragma: py3
        from ipywidgets import IntProgress
        from tqdm import tqdm
        from tqdm import tqdm_notebook
        from tqdm.contrib import ipywidgets
        from tqdm.contrib.concurrent import thread_map

        with logging_redirect_tqdm(tqdm_class=tqdm):
            logging.info('Testing `with logging_redirect_tqdm():`')

        with tqdm_notebook(desc='Testing tqdm_notebook') as pbar:
            pbar.update(1)


# Generated at 2022-06-14 13:34:12.349503
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Unit test for function `logging_redirect_tqdm`"""
    from time import time, sleep
    from nose.tools import eq_, assert_raises

    loggers = [logging.getLogger('_tqdm_logger_')]

    class MockLoggingHandler(logging.StreamHandler):

        def __init__(self, *args, **kwargs):
            super(MockLoggingHandler, self).__init__(*args, **kwargs)
            self.buffer = ''

        def emit(self, record):
            self.buffer += self.format(record)

    # Temporary set up logging
    tqdm.write = None
    parent = logging.getLogger('_tqdm_parent_')
    parent.setLevel(logging.INFO)
    parent.propagate = False
   

# Generated at 2022-06-14 13:34:21.842994
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    log = logging.getLogger(__name__)
    log.addHandler(logging.NullHandler())

    log.info('1: should not be in stdout')
    for i in trange(9):
        log.info('2a: should be in stdout. ' + str(i))
    for i in trange(9):
        log.info('2b: should NOT be in stdout. ' + str(i))
    with logging_redirect_tqdm():
        log.info('3: should be in stdout')
        for i in trange(9):
            log.info('4a: should be in stdout. ' + str(i))

# Generated at 2022-06-14 13:34:27.378461
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    log = logging.getLogger(__name__)
    expected = []
    with tqdm_logging_redirect(total=3, position=0) as pbar:
        with logging_redirect_tqdm():
            log.info('test0')
            expected.append('test0')
            pbar.set_description('test')
            expected.append('test')
            log.info('test1')
            expected.append('test1')
            pbar.set_description('test1')
            expected.append('test1')
            log.info('test2')
            expected.append('test2')
    assert 'test0test1test2test' == pbar.desc


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:34:31.726424
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # pylint: disable=protected-access
    tqdm_handler = _TqdmLoggingHandler()
    logger = logging.getLogger(__name__)
    logger.handlers = [tqdm_handler]
    logger.info("hello world")
    # pylint: enable=protected-access

# Generated at 2022-06-14 13:34:34.503926
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    LOG = logging.getLogger('test_logging_redirect_tqdm')
    with logging_redirect_tqdm([LOG]):
        LOG.info('logging redirected to `tqdm.write()`')

# Generated at 2022-06-14 13:34:43.786505
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():

    import logging
    from tqdm import trange

    # set default logger
    logger = logging.getLogger('tqdm_logging_redirect')

    for i in trange(15):
        logger.info("logging_redirect: %d" % i)

    with tqdm_logging_redirect(logging.INFO, logger=logger):
        for i in trange(15):
            logger.info("tqdm_logging_redirect: %d" % i)

    for i in trange(15):
        logger.info("logging_redirect: %d" % i)


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:34:52.656449
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import io
    import os
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)
    original_stdout_fd = sys.stdout.fileno()

    # `StringIO` used to capture `sys.stdout.write` calls.
    captured_output = io.StringIO()

    sys.stdout = captured_output

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

    # Set environment variable `

# Generated at 2022-06-14 13:34:54.595108
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    pass

if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:36:21.054028
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect(total=3) as pbar:
        for i in range(3):
            pbar.update()
            if i == 1:  # Test logging redirection
                LOG.info('Test logging redirection %s' % i)
                LOG.warning('Test logging redirection %s' % i)
            if i == 2:  # Test logging redirection (without newline)
                LOG.info('Test logging redirection %s' % i)
    with tqdm_logging_redirect(
            total=3,
            desc='TESTING',
            leave=False) as pbar:
        for i in range(3):
            pbar.update

# Generated at 2022-06-14 13:36:23.337596
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .test import test_logging_redirect_tqdm
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:36:28.377474
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    with tqdm_logging_redirect(
            tqdm_class=tqdm, total=3, desc='tqdm_logging_redirect'
    ) as pbar:
        for _ in pbar:
            LOG = logging.getLogger(__name__)
            LOG.info('logging redirect to "tqdm.write()"')
    # logging restored

# Generated at 2022-06-14 13:36:35.451703
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)
    log_str = []

    LOG.addHandler(logging.StreamHandler(sys.stdout))
    LOG.setLevel(logging.INFO)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in range(3):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

                log_str.append(sys.stdout)
        # logging restored

        assert isinstance(log_str[0], _TqdmLoggingHandler)



# Generated at 2022-06-14 13:36:37.451972
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in range(9):
            logging.info(i)

# Generated at 2022-06-14 13:36:44.343982
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    logger = logging.getLogger()

    assert(not logger.handlers)

    # testing basic
    with logging_redirect_tqdm():
        logger.warning("test")
        logger.error("test")

    with logging_redirect_tqdm():
        with tqdm_logging_redirect():
            pass

    # testing custom logger
    custom_logger = logging.getLogger(__name__)
    with logging_redirect_tqdm(loggers=[custom_logger]):
        custom_logger.warning("test")
        custom_logger.error("test")

    assert(not logger.handlers)
    if custom_logger.handlers:
        custom_logger.handlers = []

# Generated at 2022-06-14 13:36:55.154646
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from .test_utils import UnitTest
    from .test_utils import get_empty_file
    from .test_utils import get_file_info

    tqdm_logging_handler = _TqdmLoggingHandler()

    # get empty file and current size
    file_empty, size_empty = get_empty_file()

    # set empty file to the output stream
    tqdm_logging_handler.stream = file_empty

    # define a record
    record_info = logging.LogRecord('test_name', 'INFO', '/test/path',
                                    2, 'test_message', (), None)

    # call emit method
    tqdm_logging_handler.emit(record_info)

    # get the current size of file
    _, size_info = get_file_info(file_empty)



# Generated at 2022-06-14 13:37:05.610342
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None

    import logging
    import sys

    try:
        from StringIO import StringIO
        stringio_available = True
    except ImportError:
        stringio_available = False

    try:
        from io import StringIO
        stringio_available = True
    except ImportError:
        pass

    if not stringio_available:
        raise ImportError('Please install `StringIO`/`io` package.')

    def get_log(logger):
        # type: (logging.Logger) -> str
        log_stream = StringIO()
        handler = logging.StreamHandler(log_stream)
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return log_

# Generated at 2022-06-14 13:37:13.493619
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from tqdm import tqdm
    except ImportError:
        tqdm = std_tqdm
    try:
        from tqdm._tqdm_gui import tqdm_gui
    except (ImportError, RuntimeError):
        tqdm_gui = tqdm
    with tqdm_logging_redirect(total=5) as pbar:
        for i in range(5):
            pbar.update()
        logging.info("test")
    with tqdm_logging_redirect(total=5, loggers=[logging.getLogger("foo")]) as pbar:
        for i in range(5):
            pbar.update()

# Generated at 2022-06-14 13:37:19.075820
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from io import StringIO  # Python 3
    except ImportError:
        from cStringIO import StringIO  # Python 2

    # Set up logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Set up stream for redirecting stdout
    stdout = sys.stdout
    out = StringIO()
    sys.stdout = out
    with logging_redirect_tqdm():
        logger.info('This should go to tqdm.write()')
        logger.info('This should also go to tqdm.write()')
    out.seek(0)
    results = out.read().strip().split('\n')
    sys.stdout = stdout