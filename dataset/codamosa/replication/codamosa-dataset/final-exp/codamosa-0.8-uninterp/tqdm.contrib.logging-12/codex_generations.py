

# Generated at 2022-06-14 13:27:58.571123
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from io import StringIO
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    log = logging.getLogger(__name__)
    stream = StringIO()
    logger_handlers = log.handlers
    try:
        LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
        logging.basicConfig(stream=stream, level=logging.INFO, format=LOG_FORMAT)
        with logging_redirect_tqdm():
            with tqdm(total=1, file=sys.stdout) as pbar:
                for _ in range(3):
                    log.info('1')
                    pbar.update(1)
    finally:
        log.hand

# Generated at 2022-06-14 13:28:07.947890
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import pytest

    class TqdmStub(std_tqdm):
        def __init__(self):
            self.fd = sys.stdout

        def write(self, message):
            self.fd.write(message)

    # Capture output of sys.stdout
    fd = sys.stdout
    sys.stdout = open('test.txt', 'w')

    # Set up logging message
    message = 'Test logging\n'
    log_record = logging.LogRecord(
        name='tqdm',
        level=logging.INFO,
        pathname='',
        lineno=0,
        msg=message,
        args=None,
        exc_info=None)

    # Create a TqdmLoggingHandler with TqdmStub
    tqdm_handler = _Tqdm

# Generated at 2022-06-14 13:28:15.305691
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    for tqdm_module in (std_tqdm,):
        log = logging.getLogger()
        log.handlers = []
        log.setLevel(logging.INFO)
        handlers_list = [h.__class__.__name__ for h in log.handlers]
        assert handlers_list == ['NullHandler']
        with logging_redirect_tqdm(tqdm_class=tqdm_module):
            log.info('logging redirected to {}.write'.format(tqdm_module.__name__))
            handlers_list = [h.__class__.__name__ for h in log.handlers]
            assert '_TqdmLoggingHandler' in handlers_list

# Generated at 2022-06-14 13:28:22.800387
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
                total=9,
                desc='console logging redirected to `tqdm.write()`'):
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:28:33.290683
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import os
    import tempfile
    from tqdm import trange


# Generated at 2022-06-14 13:28:41.795973
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    def test_logging_redirect_tqdm(tqdm_class, loggers):
        import logging
        import six
        with tqdm_class(leave=False) as pbar:
            with logging_redirect_tqdm(loggers=loggers, tqdm_class=tqdm_class):
                for i in range(4):
                    if i == 3:
                        logging.info("console logging redirected to `tqdm.write()`")
                        pbar.update(pbar.total - pbar.n)
                    else:
                        pbar.update()


# Generated at 2022-06-14 13:28:48.058215
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange

    logging.basicConfig(level=logging.INFO)
    loggers = [logging.root]

    with tqdm_logging_redirect(loggers) as pbar:
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:28:51.328193
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with logging_redirect_tqdm():
        logger = logging.getLogger(__name__)
        with tqdm_logging_redirect(desc=__name__):
            for i in range(3):
                logger.info(i)

# Generated at 2022-06-14 13:28:55.506898
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    def invoke_emit(self, record):
        # type: (_TqdmLoggingHandler, logging.LogRecord) -> None
        self.emit(record)
    invoke_emit(_TqdmLoggingHandler(tqdm_class=std_tqdm), logging.LogRecord(
        name='test', lvl=40, pathname='', lineno=0, msg='msg',
        args=(), exc_info=None))

# Generated at 2022-06-14 13:29:02.903545
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """ Test the method _TqdmLoggingHandler.emit with a fake record.
        It is hard to run this test with a real record.
    """
    class FakeRecord(object):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return self.msg

    class FakeTqdm(object):
        @staticmethod
        def write(*args, **kwargs):
            pass

    record = FakeRecord("This is a fake record.")

    # Test the method emit without exeption
    handler = _TqdmLoggingHandler(FakeTqdm)
    handler.emit(record)

    # Test the method emit with a KeyboarInterrupt
    def raise_keyboard_interrupt(*args, **kwargs):
        raise KeyboardInterrupt
    handler = _

# Generated at 2022-06-14 13:29:20.918203
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import trange
    from logging import root, getLogger, INFO, StreamHandler, Formatter
    try:
        from io import StringIO
    except ImportError:
        from six import StringIO

    tqdm_out = StringIO()
    logging_out = StringIO()
    log_handler = StreamHandler(logging_out)
    log_handler.setFormatter(Formatter('[%(levelname)s] %(message)s'))
    root.handlers = [log_handler]

    with trange(3) as pbar:
        with logging_redirect_tqdm() as tqdm_handler:
            pbar.set_postfix_str('[test]')
            getLogger().setLevel(INFO)
            getLogger().info('test')
    assert tqdm_

# Generated at 2022-06-14 13:29:29.265044
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import tempfile
    lf = tempfile.TemporaryFile()  # type: ignore
    n = 9
    with tqdm_logging_redirect(
            iterable=range(n),
            loggers=[logging.root],  # default
            tqdm_class=std_tqdm,
            file=lf) as pbar:
        for i in pbar:
            if i == 5:
                LOG = logging.getLogger(__name__)
                LOG.info("console logging redirected to `tqdm.write()`")
            elif i == 3:
                logging.info("console logging redirected to `tqdm.write()`")
                # bad: logging stream will be redirected to tqdm.write()
                pass

# Generated at 2022-06-14 13:29:40.845720
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys

    def test_func(arg):
        LOG.debug("debug")
        LOG.info("info")
        LOG.warning("warning")
        LOG.error("error")
        LOG.critical("critical")

    loggers = [logging.getLogger(__name__)]

    test_value = "test_value"
    with tqdm_logging_redirect(loggers=loggers) as pbar:
        pbar.update(1)
        test_func(test_value)
        pbar.update(1)

    assert pbar.n == 2
    assert next(pbar.log_values).message == "info"
    assert next(pbar.log_values).message == "warning"
    assert next(pbar.log_values).message == "error"
    assert next

# Generated at 2022-06-14 13:29:46.539157
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from io import StringIO
    import logging

    # Set logger output to a string and also flush stdout
    with open(StringIO, 'w', encoding='utf-8') as sys.stdout:
        with logging_redirect_tqdm():
            logger = logging.getLogger("logging_redirect_tqdm")
            logger.debug("hello")
            logger.info("world")

# Generated at 2022-06-14 13:29:50.173101
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:29:57.396831
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

# Generated at 2022-06-14 13:30:06.627073
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.contrib.logging import tqdm_logging_redirect, logging_redirect_tqdm
    from tqdm.tests.gui import pretest_posttest_test  # Do not remove, context manager
    from tqdm.tests.gui import _capture_output  # Do not remove, context manager
    with _capture_output() as captured:
        logger = logging.getLogger('logger_one')
        LOG_MSG = 'some custom logging msg'
        logger.setLevel(logging.INFO)
        with pretest_posttest_test(captured, leave=False):
            with tqdm_logging_redirect(leave=True, loggers=[logger]) as pbar:
                pbar.update()
                logger.info(LOG_MSG)
        assert LOG

# Generated at 2022-06-14 13:30:16.095684
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from contextlib import redirect_stdout
    import logging
    from io import StringIO
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    logging.basicConfig(level=logging.INFO)
    foo_logger = logging.getLogger('foo')
    LOG = logging.getLogger(__name__)
    # method 1
    with StringIO() as s, redirect_stdout(s):
        with logging_redirect_tqdm(loggers=[foo_logger, LOG]):
            for i in tqdm(range(5)):
                if i == 3:
                    foo_logger.info('this is')
                    LOG.info('console logging redirected to `tqdm.write()`')

# Generated at 2022-06-14 13:30:22.898658
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

# Generated at 2022-06-14 13:30:32.648375
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    def _test_func(stream):
        # type: (TextIO) -> None
        logging.info('this is a test log')

    _test_func_stdout = _test_func
    _test_func_stderr = _test_func

    loggers = [logging.getLogger('test_tqdm_logging_redirect')]
    with logging_redirect_tqdm(loggers=loggers):
        _test_func_stdout(sys.stdout)
        _test_func_stderr(sys.stderr)

    # Unit test for function logging_redirect_tqdm
    def _test_func(stream):
        # type: (TextIO) -> None
        logging.info('this is a test log')

    _test_func

# Generated at 2022-06-14 13:30:52.772561
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:30:56.674078
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    with tqdm_logging_redirect(total=9,
                               unit='i',
                               unit_scale=True,
                               unit_divisor=1024) as pbar:
        logging.info('console logging redirected to `tqdm.write()`')
    print('logging outside pbar')
    try:
        with tqdm_logging_redirect(total=9,
                                   unit='i',
                                   unit_scale=True,
                                   unit_divisor=1024) as pbar:
            logging.info('console logging redirected to `tqdm.write()`')
            raise Exception('raise exception')
    except Exception as e:
        print('It is split by error:')

# Generated at 2022-06-14 13:31:01.007178
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """Unit test for function tqdm_logging_redirect"""
    with tqdm_logging_redirect(total=9, desc='test') as pbar:
        if pbar.n == 4:
            logging.info('console logging redirected to `tqdm.write()`')

# Generated at 2022-06-14 13:31:05.874990
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(total=100) as pbar:
        for _ in range(100):
            pbar.update()
            LOG = logging.getLogger(__name__)
            if _ == 34:
                LOG.info("console logging redirected to `tqdm.write()`")
                break
    for _ in range(66):
        pbar.update()

# Generated at 2022-06-14 13:31:17.444027
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from itertools import product
    import logging
    from tqdm import tqdm
    import pytest

    LOG = logging.getLogger(__name__)
    messages = ["hello", "world", "!"]

    def bar(*args, **kwargs):
        try:
            for msg in messages:
                LOG.info(msg)
                yield  # type: ignore
        finally:
            for msg in messages:
                LOG.info(msg)

    logger_lists = (logging.Logger.manager.loggerDict.values(), [])
    progress_bars = (tqdm, tqdm(desc="logging_redirect_tqdm()"), bar)


# Generated at 2022-06-14 13:31:26.574889
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Test tqdm_logging_redirect()
    """
    import os
    import logging
    import sys
    from contextlib import contextmanager
    from functools import partial

    @contextmanager
    def no_stdout():
        # type: () -> Iterator[None]
        stdout = sys.stdout
        try:
            sys.stdout = open(os.devnull, 'w')
            yield
        finally:
            sys.stdout.close()
            sys.stdout = stdout

    with no_stdout():
        with tqdm_logging_redirect(total=5):
            logging.info('lol')
      

# Generated at 2022-06-14 13:31:29.897833
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    with tqdm_logging_redirect(desc='testing') as pbar:
        for i in range(3):
            logging.info('msg %d' % i)
            pbar.update()



# Generated at 2022-06-14 13:31:38.134936
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .test_tqdm import pretest_posttest_testsuite
    from ..utils import _range
    from ..std import tqdm
    from ..std import logging as std_logging
    from ..std import sys as std_sys

    class _TestLoggingFormatter(std_logging.Formatter):
        def formatMessage(self, record):
            return record.getMessage()

    def test(loggers):
        with tqdm_logging_redirect(*_range(9), loggers=loggers,
                                   unit='t', desc='tqdm logging redirection') as pbar:
            assert isinstance(pbar, std_tqdm.tqdm)
            std_logging.info("console logging redirected to `tqdm.write()`")

    test([logging.root])
    test

# Generated at 2022-06-14 13:31:44.249009
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    return
    from .tests import test_logging_redirect_tqdm
    test_logging_redirect_tqdm.test_logging_redirect_tqdm(
        _TqdmLoggingHandler, _is_console_logging_handler,
        _get_first_found_console_logging_handler, logging_redirect_tqdm
    )

# Generated at 2022-06-14 13:31:54.888441
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm

    from .test_redirect_std_tqdm import FakeTqdmType
    from .test_redirect_std_tqdm import DummyFile

    warnings_shown = []

    def import_fake_tqdm():
        # type: () -> None
        """
        This function is called indirectly by monkeypatching the import system
        to replace tqdm with our FakeTqdmType (which is a tqdm.tqdm
        subclass).
        """
        # noinspection PyUnresolvedReferences
        from .test_redirect_std_tqdm import FakeTqdmType
        # noinspection PyUnresolvedReferences
        from .test_redirect_std_tqdm import warnings_shown
