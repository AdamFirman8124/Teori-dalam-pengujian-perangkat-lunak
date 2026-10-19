

# Generated at 2022-06-14 13:27:43.895026
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logging.basicConfig(level=logging.INFO)
    try:
        with tqdm_logging_redirect(
            bar_format='{desc}{percentage:3.0f}%', desc='Redirecting...'
        ) as pbar:
            for i in range(9):
                if i == 4:
                    logging.info('console logging redirected to tqdm.write()')
                if i == 8:
                    pbar.set_description('Done')
    except (KeyboardInterrupt, SystemExit):
        raise



# Generated at 2022-06-14 13:27:48.961736
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import sys
    log_output = io.StringIO()
    test_message = 'This is a test message'

    hdlr = _TqdmLoggingHandler()
    hdlr.stream = io.TextIOWrapper(log_output, sys.stdout.encoding)

    hdlr.emit(logging.LogRecord(name='test', level=10, pathname='', lineno=0,
                                msg=test_message, args=None, exc_info=None))

    assert log_output.getvalue() == test_message

# Generated at 2022-06-14 13:27:55.399563
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.root.handlers = []
    from .test_std import TestManyConsoleStreams
    logging.basicConfig(level=logging.DEBUG)
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        LOG.info("info")
        LOG.error("error")
        for s in TestManyConsoleStreams.test_log_write(LOG):
            assert s == 'error'
    assert [h.__class__.__name__ for h in logging.root.handlers] == ['StreamHandler']

# Generated at 2022-06-14 13:27:57.855932
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # Running method emit of class _TqdmLoggingHandler
    handler = _TqdmLoggingHandler()
    record = logging.LogRecord("", "", "", "", "", "", "")
    handler.emit(record)

# Generated at 2022-06-14 13:28:03.821174
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tqdm_test_cases import TestCaseWithLogging

    log = logging.getLogger()
    assert not log.handlers

    with logging_redirect_tqdm():
        assert log.handlers
        log.warning('test_logging_redirect_tqdm output')

        with TestCaseWithLogging():
            assert log.handlers

            log.info('test_logging_redirect_tqdm output 2')

    assert not log.handlers

# Generated at 2022-06-14 13:28:08.096747
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    with tqdm_logging_redirect(ascii=True, loggers=[]) as pbar:
        raise ValueError()


# Generated at 2022-06-14 13:28:15.373816
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    try:
        from typing import List  # noqa
    except ImportError:
        pass
    from time import sleep
    from random import randrange
    import logging
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    def main():
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(tqdm=tqdm, loggers=[LOG],
                                   desc="logging redirected to `tqdm.write()`") \
                as pbar:
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("test")
                sleep(randrange(1, 3)/10)
                pbar.update()
        # logging restored


# Generated at 2022-06-14 13:28:21.556689
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    LOG.info("console logging redirected to `tqdm.write()`")

    with tqdm_logging_redirect() as pbar:
        pbar.update()

    LOG.info("console logging restored")


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:28:25.164331
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Test logging_redirect_tqdm."""
    import logging
    logger = logging.getLogger()
    logger.setLevel('INFO')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    with logging_redirect_tqdm():
        logging.info("test1")
    logging.info("test2")

# Generated at 2022-06-14 13:28:29.835836
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in std_tqdm.trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:28:40.469731
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    # Default configuration
    logger = logging.getLogger('test__TqdmLoggingHandler_emit')
    logger.setLevel(logging.INFO)
    tqdmHandler = _TqdmLoggingHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    tqdmHandler.setFormatter(formatter)
    logger.addHandler(tqdmHandler)
    logger.info('info logging')



# Generated at 2022-06-14 13:28:50.162603
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from logging.handlers import RotatingFileHandler
    from random import shuffle
    from .utils import formatted_range

    log_file = 'log.txt'
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-5.5s]  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    logger.handlers = []
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    file_handler = RotatingFileHandler(log_file, mode='a', maxBytes=10, backupCount=1)

# Generated at 2022-06-14 13:28:57.298821
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    log_file = './log_tqdm_logging_redirect.log'
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     datefmt='%Y-%m-%d %H:%M:%S')
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    with tqdm_logging_redirect(total=10, desc="test") as pbar:
        for i in range(10):
            pbar.update(1)
            logger.info

# Generated at 2022-06-14 13:29:02.341748
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    def f():
        for i in trange(3):
            logging.info("hello {}".format(i))
            yield i

    LOGGING_HANDLERS_SAVE = logging.root.handlers

    try:
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            list(f())
    finally:
        logging.root.handlers = LOGGING_HANDLERS_SAVE



# Generated at 2022-06-14 13:29:11.318410
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Basic test for context manager logging_redirect_tqdm.

    It does not check whether output is actually redirected to
    tqdm.write(). This can be tested manually e.g. with `-s` flag.

    """
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(2):
                if i == 0:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


if __name__ == '__main__':
    test_log

# Generated at 2022-06-14 13:29:15.913155
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    with logging_redirect_tqdm():
        for i in tqdm(range(5), "logging redirected:"):
            if i == 2:
                logging.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:29:25.867526
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        # pylint: disable=redefined-outer-name
        import logging
        from tqdm import tqdm_notebook
        from tqdm.contrib.logging import tqdm_logging_redirect
        from unittest.mock import patch
    except ImportError:  # pragma: no cover
        return
    logger = logging.getLogger('test_tqdm_logging_redirect')
    logger.setLevel(logging.DEBUG)
    # Remove existing handlers
    for handler in logger.handlers:
        logger.removeHandler(handler)
    log_messages = []

# Generated at 2022-06-14 13:29:37.797813
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from .std import tqdm, tqdm_notebook
    from .logging import tqdm_logging_redirect
    from .std import HTMLReport

    LOG = logging.getLogger(__name__)

    # Run this as
    # import tqdm; tqdm.contrib.test(tqdm.contrib.logging.test_tqdm_logging_redirect)
    tqdm.test_cli([])
    tqdm_notebook.test_notebook()

    # tqdm output

# Generated at 2022-06-14 13:29:44.629664
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch
        patch_ = patch
    except ImportError:
        from mock import patch
        patch_ = patch

    with patch_('sys.stdout', new=std_tqdm.io.StringIO()) as p:
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            LOG = logging.getLogger(__name__)
            LOG.info('hello world')
        assert p.getvalue() == 'hello world\n'

    with patch_('sys.stdout', new=std_tqdm.io.StringIO()) as p:
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            LOG = logging.getLogger(__name__)
            LOG

# Generated at 2022-06-14 13:29:55.973692
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch
        mock_write = patch('tqdm.contrib.logging._TqdmLoggingHandler.write')  # type: ignore
        mock_emit = patch('tqdm.contrib.logging._TqdmLoggingHandler.emit')  # type: ignore
    except ImportError:
        from mock import patch
        mock_write = patch('tqdm.contrib.logging._TqdmLoggingHandler.write')
        mock_emit = patch('tqdm.contrib.logging._TqdmLoggingHandler.emit')
    import logging
    with logging_redirect_tqdm():
        logging.warning('test_1')
        logging.warning('test_2')

# Generated at 2022-06-14 13:30:09.389385
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm

    logging.disable(logging.CRITICAL)

    loggers = [logging.getLogger(__name__),
               logging.getLogger('tqdm'),
               logging.root]
    for i in range(3):
        logging.getLogger(__name__).handlers = []
        logging.getLogger('tqdm').handlers = []
        logging.root.handlers = []

    # Test 1: no logging handlers
    with tqdm_logging_redirect(total=10, desc='test', ascii=True) as pbar:
        for _ in range(10):
            pbar.update()
    assert len(logging.getLogger(__name__).handlers) == 0

# Generated at 2022-06-14 13:30:18.051677
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tqdm_test_case import _TestTqdmIO, _test_instance

    with tqdm_logging_redirect(total=4) as pbar:
        LOG = logging.getLogger(__name__)
        for i in range(4):
            if i == 2:
                LOG.info("console logging redirected to `tqdm.write()`")
            pbar.update()

    class DummyFileLike(object):
        @staticmethod
        def write(s):
            pass

    dout = DummyFileLike()

    def dummy_log(msg, level="ERROR"):
        # type: (str, str) -> None
        with tqdm_logging_redirect(loggers=[logging.root], file=dout, level=level):
            LOG = logging.getLogger

# Generated at 2022-06-14 13:30:26.187723
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored



# Generated at 2022-06-14 13:30:33.628722
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    from .tqdm import tqdm
    from ..std import time

    LOG = logging.getLogger(__name__)

    for tqdm_class in [tqdm, std_tqdm]:
        with tqdm_logging_redirect(total=9, tqdm_class=tqdm_class,
                                   loggers=[LOG], desc='tqdm_logging_redirect'):
            for i in range(9):
                time.sleep(.1)
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                LOG.debug("DEBUG LOG: {}".format(i))

# Generated at 2022-06-14 13:30:37.225829
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    loggers = [logging.root]
    original_handlers_list = [logger.handlers for logger in loggers]
    with tqdm_logging_redirect() as pbar:
        assert isinstance(pbar, std_tqdm)
    # logging restored

# Generated at 2022-06-14 13:30:44.758385
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None

    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    def tqdm_test():
        # type: () -> None
        with logging_redirect_tqdm():
            for i in trange(10):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

    # Chunked file-like wrapper (for testing)
    class FileWrapper(object):
        def __init__(self, f, chunksize):
            # type: (Any, int) -> None
            self.f = f  # type: Any
            self.chunksize = chunksize


# Generated at 2022-06-14 13:30:52.742817
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    # Test root logger
    with logging_redirect_tqdm():
        logging.info("test logging1")
        logging.warning("test logging2")
    # Test defined logger
    test_logger = logging.getLogger("Test")
    test_logger.setLevel(logging.INFO)
    with logging_redirect_tqdm([test_logger]):
        test_logger.info("test logging1")
        test_logger.warning("test logging2")



# Generated at 2022-06-14 13:30:59.581409
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import sys
    import logging
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    logger.info("tqdm_loggin_redirect test 1")
    with tqdm_logging_redirect(total=3) as pbar:
        for i in range(1, 4):
            pbar.write(i)
            pbar.update(1)
    logger.info("tqdm_loggin_redirect test 2")
    with tqdm_logging_redirect(total=3, file=sys.stdout, desc='testing...') as pbar:
        for i in range(1, 4):
            pbar.write(i)
            pbar.update(1)

if __name__ == '__main__':
    test_tqdm_

# Generated at 2022-06-14 13:31:04.395567
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(desc="console logging redirected to `tqdm.write()`"):
        for _ in trange(9):
            LOG.info("info msg")



# Generated at 2022-06-14 13:31:16.242052
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    loggers = [logger]
    tqdm_class = std_tqdm

    def test(
        tqdm_class=tqdm_class,
        loggers=loggers
    ):
        # type: (...) -> None
        with tqdm_logging_redirect(
            loggers=loggers,
            tqdm_class=tqdm_class,
        ):
            logger.debug('test_debug')
            logger.info('test_info')
            logger.warning('test_warning')
            logger.error('test_error')
            logger.critical('test_critical')

    test()

# Generated at 2022-06-14 13:31:35.152944
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """Ensure that the tqdm_logging_redirect() is functional."""
    # Clearing the loggers
    logging.root.handlers = []
    # Creating a logger
    logger = logging.getLogger('test_tqdm_logging_redirect')
    logging.basicConfig(level=logging.INFO)
    original_handlers = logger.handlers
    # Checking the logger with default tqdm
    with tqdm_logging_redirect() as pbar:
        logger.info("Testing tqdm_logging_redirect()")
        pass
    assert pbar.n == 1
    # Checking the logger with a different logger
    logger = logging.getLogger('different_logger')

# Generated at 2022-06-14 13:31:46.734184
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging as lg
    import os
    import tempfile
    LOG = lg.getLogger('test')

    # test: log file created and written to
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmpl:
        tmpl.close()
        handler = lg.FileHandler(tmpl.name)
        LOG.addHandler(handler)
        with tqdm_logging_redirect(total=10, desc="test",
                                   loggers=[LOG]) as pbar:
            LOG.info("test")
            LOG.info("test")
            LOG.info("test")
            LOG.info("test")
            for i in range(10):
                pbar.update()
        LOG.removeHandler(handler)

# Generated at 2022-06-14 13:31:52.306107
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from tqdm.auto import tqdm as tqdm_auto
    except:
        return
    with tqdm_logging_redirect(tqdm_class=tqdm_auto) as pbar:
        pbar.update(1)
        # Uncomment the following line to see it fail
        #pbar.write('hi')

# Generated at 2022-06-14 13:31:57.911073
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(total=9):
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    # logging restored
    LOG.info("console logging restored")

# Generated at 2022-06-14 13:32:08.929787
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .test_tqdm import pretest_posttest  # pylint: disable=import-outside-toplevel

    @pretest_posttest
    def test_func(loggers):
        import logging
        import tqdm
        from tqdm import tqdm

        LOG = logging.getLogger(__name__)

        if __name__ == '__main__':
            logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:32:14.948073
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for _ in trange(9):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored


# Generated at 2022-06-14 13:32:22.089586
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    loggers = [logging.root]
    tqdm_class = std_tqdm
    count = 200
    tf = True
    with std_tqdm(total=count, file=sys.stderr, desc='tqdm_logging_redirect') as pbar:
        with logging_redirect_tqdm(
                loggers=loggers, tqdm_class=tqdm_class):
            logging.warning('abc')
            logging.warning('abc')
            for i in range(count):
                pbar.update()
                logging.warning('abc')
                logging.warning('abc')
                logging.warning('abc')
                logging.warning('abc')
                logging.warning('abc')
    assert(tf)

# Generated at 2022-06-14 13:32:30.393593
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import tqdm.auto as tqdm_auto
    import logging
    import sys
    sys.stderr = sys.stdout
    t = _TqdmLoggingHandler(tqdm_class=tqdm_auto.tqdm)
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    root.addHandler(t)
    logging.debug('test 1')
    logging.debug('test 2')
    logging.debug('test 3')
    root.removeHandler(root.handlers[-1])

# Generated at 2022-06-14 13:32:40.562199
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Coverage testing"""
    import tqdm
    import logging

    with tqdm.std.tqdm(
            total=5,
            desc='Running custom logging test',
            ncols=100,
            dynamic_ncols=True,
            unit='bits') as pbar:
        with logging_redirect_tqdm():
            for _ in range(5):
                logging.info('console logging redirected to `tqdm.write()`')
                pbar.update(1)
                logging.info('console logging redirected to `tqdm.write()`')
                pbar.update(1)

    logging.error('console logging restored')

# Generated at 2022-06-14 13:32:48.592799
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """Test tqdm_logging_redirect"""
    import sys
    import logging
    from ..std import tqdm
    from ..std import tqdm_gui
    from ..std import tqdm_notebook
    from ..utils import _range

    for tqdm_class in [tqdm, tqdm_gui, tqdm_notebook]:
        with tqdm_logging_redirect(total=9,
                                   tqdm_class=tqdm_class) as logpbar:
            for _ in _range(9):
                logging.info("redirected")

# Generated at 2022-06-14 13:33:06.282788
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Test function logging_redirect_tqdm"""
    import logging
    import tqdm
    from tqdm._utils import _term_move_up

    # test normal case
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in tqdm.trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    # test if detaching and restoring works
    # test normal case
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        try:
            tqdm.tqdm.write('foo')
            LOG.info('bar')
        finally:
            logging_redirect_tqdm.detach()
    #

# Generated at 2022-06-14 13:33:13.124775
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .utils import closing

    log = logging.getLogger('test')
    log.addHandler(logging.NullHandler())
    log.propagate = False

    log.info('should NOT be displayed with logging_redirect_tqdm')

    with closing(StringIO()) as our_file:
        log.handlers = [logging.StreamHandler(our_file)]
        with tqdm.utils.capture_output() as captured_output:
            log.info('should be displayed')

    assert captured_output.getvalue() == ''

    with closing(StringIO()) as our_file:
        log.handlers = [logging.StreamHandler(our_file)]

# Generated at 2022-06-14 13:33:20.132194
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # pylint: disable=anomalous-backslash-in-string
    import logging
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(unit='bars',
                               desc='logging redirected to `tqdm.write()`',
                               total=9) as pbar:
        for i in range(9):
            pbar.update()
            if i == 4:
                LOG = logging.getLogger(__name__)
                LOG.info("console logging redirected to `tqdm.write()`")
    # pylint: enable=anomalous-backslash-in-string



# Generated at 2022-06-14 13:33:30.480287
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)

    class testing_adapter(logging.LoggerAdapter):
        def process(self, msg, kwargs):
            # type: (...) -> str
            return msg

    with tqdm_logging_redirect(
        testing_adapter(LOG, {}),
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        total=1024,
        ncols=80,
        disable=False,
        file=sys.stderr
    ) as pbar:
        # testing all attribtues of pbar
        assert pbar.__repr__() != ''
        pbar.update(10)
        pbar.n
        pbar.miniters
        pbar.maxinterval


# Generated at 2022-06-14 13:33:33.795684
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    with tqdm_logging_redirect(
            total=100, desc='test_tqdm_logging_redirect') as pbar:
        for _ in range(100):
            pbar.update()
            logging.info('test')

# Generated at 2022-06-14 13:33:42.832090
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def capture_std_stream(std_stream):
        # type: (StringIO) -> Iterator[None]  # NOQA
        """
        Captures the std_stream (stdout or stderr).
        """
        original = std_stream.getvalue()
        std_stream.seek(0)
        std_stream.truncate()
        try:
            yield std_stream
        finally:
            std_stream.seek(0)
            std_stream.truncate()
            std_stream.write(original)

    with capture_std_stream(StringIO()) as output:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # create console handler and set level

# Generated at 2022-06-14 13:33:48.024996
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from . import tqdm
    from .utils import _range

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect() as pbar:
            for i in _range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                pbar.update(1)
        # logging restored


# Generated at 2022-06-14 13:33:58.498364
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    try:
        import pytest
        from io import StringIO
    except ImportError:
        return

    @contextmanager  # type: ignore
    def captured_output():
        """Captured stdout and stderr from logging."""
        old_out, old_err = sys.stdout, sys.stderr
        try:
            out = [StringIO(), StringIO()]
            sys.stdout, sys.stderr = out
            yield out
        finally:
            sys.stdout, sys.stderr = old_out, old_err
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()


# Generated at 2022-06-14 13:34:06.249364
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


# Generated at 2022-06-14 13:34:14.842202
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from io import StringIO
    from contextlib import redirect_stdout
    from ..std import tqdm as std_tqdm
    import logging

    test_logger = logging.getLogger(__name__)
    test_logger.setLevel(logging.DEBUG)

    with StringIO() as buffer, redirect_stdout(buffer):
        with logging_redirect_tqdm():
            test_logger.debug('Test tqdm logging redirect')
    assert 'Test tqdm logging redirect' in buffer.getvalue()

    with StringIO() as buffer, redirect_stdout(buffer):
        with logging_redirect_tqdm(tqdm_class=std_tqdm):
            test_logger.debug('Test tqdm_class')
    assert 'Test tqdm_class' in buffer.get

# Generated at 2022-06-14 13:34:31.318392
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        # suppress print statement in std_tqdm
        sys.stdout = open(os.devnull, 'w')

        with tqdm_logging_redirect(total=5) as pr:
            pr.update()
            pr.update()
            raise AssertionError
    except AssertionError:
        pass

# Generated at 2022-06-14 13:34:41.570109
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests_tqdm import with_unit_option, with_unit_environment
    from .tests_tqdm import closing
    import datetime
    import logging
    import time
    try:
        import __main__
        assert __main__.__file__  # only set if standalone script
    except:  # noqa pylint: disable=bare-except
        __main__ = None
    LOG = logging.getLogger(__name__ + '.test_logging_redirect_tqdm')


# Generated at 2022-06-14 13:34:44.564416
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in std_tqdm(range(9)):
            if i == 4:
                logging.info('console logging redirected to "tqdm.write()"')



# Generated at 2022-06-14 13:34:50.188571
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tests import TestCase  # pylint: disable=unused-variable
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:35:01.083803
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """
    Test the context manager tqdm_logging_redirect
    """
    # import necessary modules
    import logging
    from tqdm import trange

    # Initialize logging
    logging.basicConfig(level=logging.INFO)

    # Define a list of loggers
    loggers = [logging.root]

    # Make sure that nothing is \n
    assert std_tqdm.write('') == '\n'

    # Make sure that we are redirecting the logging to std_tqdm.write

# Generated at 2022-06-14 13:35:04.062722
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange

    with tqdm_logging_redirect(total=9, mininterval=0.1, unit='test'):
        for i in trange(9):
            if i == 4:
                logging.info('tqdm logging test')

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:35:12.840377
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import os
    import shutil
    import tempfile
    import logging.handlers
    with tempfile.TemporaryDirectory() as tempdir:
        LOGFILE = os.path.join(tempdir, 'test_logfile.log')
        LOG_LEVEL = logging.DEBUG
        logging.getLogger('').setLevel(LOG_LEVEL)
        logging.basicConfig(
            stream=sys.stdout,
            format='%(levelname)-8s@%(asctime)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        with tqdm_logging_redirect(logging.getLogger('')):
            LOG.debug("test_tqdm_logging_redirect: debug")

# Generated at 2022-06-14 13:35:23.203124
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Test logging_redirect_tqdm()
    """
    import logging
    from tqdm import trange

    class DummyTqdm(std_tqdm):
        """
        Dummy tqdm class for testing
        """
        tqdm_output = None
        @staticmethod
        def write(s, file=None):
            # type: (str, Optional[FileType]) -> None
            DummyTqdm.tqdm_output = s or ""
            DummyTqdm.tqdm_output += "\n"

    LOG = logging.getLogger(__name__)

    def check_logging():
        """
        Test logging_redirect_tqdm()
        """
        global LOG  # pylint: disable=global-statement
        LOG.info("info")


# Generated at 2022-06-14 13:35:26.930577
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    log_record = logging.makeLogRecord(dict(name='test', message='test_message'))
    with tqdm_logging_redirect(level=logging.INFO):
        handler = _TqdmLoggingHandler()
        handler.emit(log_record)

# Generated at 2022-06-14 13:35:30.696116
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with logging_redirect_tqdm(loggers=logger, tqdm_class=std_tqdm):
        logger.info('test_logging_redirect_tqdm')

# Generated at 2022-06-14 13:35:55.409418
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(desc="logging tqdm") as pbar:
        for i in range(5):
            assert not pbar.disable
            logging.info("testing redirected logging")

# Generated at 2022-06-14 13:35:59.936246
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import tqdm

    logging.basicConfig(level=logging.INFO)
    with tqdm(total=9, desc='redirector') as pbar:
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    logging.info("console logging redirected to `tqdm.write()`")
                pbar.update(1)


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:36:10.819165
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    with tqdm_logging_redirect(
            total=100,
            unit='test',
            unit_divisor=1,
            unit_scale=True,
            leave=True,
            dynamic_ncols=True
    ) as pbar:
        # Create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Add formatter to ch
        ch.setFormatter(formatter)
        #

# Generated at 2022-06-14 13:36:17.907510
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from .utils import SimpleNamespace

    logger = logging.getLogger('test_logging_redirect_tqdm')
    logger.propagate = False
    # logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.NullHandler())

    # This is really really really really really really really really really really really really really really stupid
    def _test_iter():
        for n in range(100):
            yield SimpleNamespace(n=n)

    progressbar = _test_iter()

# Generated at 2022-06-14 13:36:27.475602
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """Unit test for function tqdm_logging_redirect"""
    import logging
    import time
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    log_file = './test_tqdm_logging_redirect.log'
    logging.basicConfig(
        filename=log_file,
        format='%(asctime)s %(message)s',
        level=logging.DEBUG
        )
    LOG = logging.getLogger(__name__)
    LOG.info("Step 1")
    LOG.warning("Step 2")


# Generated at 2022-06-14 13:36:32.590652
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger()

    with logging_redirect_tqdm():
        for i in trange(3):
            if i == 1:
                LOG.info("console logging redirected to `tqdm.write()`")

if __name__ == "__main__":
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:36:37.648443
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
        # logging restored



# Generated at 2022-06-14 13:36:44.506846
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Unit test for `tqdm.contrib.logging.logging_redirect_tqdm`, via:
    ```python
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
    ```
    """
    import logging
    from . import log_main
    from .log_main import test_

# Generated at 2022-06-14 13:36:49.376793
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    try:
        import tqdm
    except ImportError:
        return
    LOG = logging.getLogger()

    # Redirect logging to tqdm.write
    with logging_redirect_tqdm():
        LOG.warning("WARNING")
        LOG.error("ERROR")
        tqdm.write("tqdm write")



# Generated at 2022-06-14 13:36:58.037371
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    # Tests logging_redirect_tqdm()
    import logging
    from contextlib import redirect_stdout
    from io import StringIO
    from tqdm import trange

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    # Redirect stdout to inspect logging later
    f = StringIO()
    with redirect_stdout(f):
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        assert "console logging redirected to `tqdm.write()`\n" in f.getvalue()