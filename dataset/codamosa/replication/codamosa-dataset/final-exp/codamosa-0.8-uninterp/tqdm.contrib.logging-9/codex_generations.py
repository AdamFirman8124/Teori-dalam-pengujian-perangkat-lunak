

# Generated at 2022-06-14 13:27:52.919638
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    with logging_redirect_tqdm(tqdm_class=trange):
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:27:56.174049
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import time

    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")
        time.sleep(1)


# Generated at 2022-06-14 13:27:58.686601
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:28:04.669854
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)

        with tqdm_logging_redirect(total=9) as pbar:
            for i in pbar:
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

    # logging restored

# Generated at 2022-06-14 13:28:12.081725
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Test logging_redirect_tqdm"""
    import os
    import sys
    import tempfile
    import logging

    if sys.version_info[0] < 3:
        return
    # Old version of logging
    if sys.version.startswith('3.3') and sys.version_info >= (3, 4, 0):
        return

    def get_stream_data(stream):
        stream.seek(0)
        return stream.read()

    log = logging.getLogger(__name__)
    # create a stream for tqdm.write()
    tqdm_log_stream = tempfile.TemporaryFile(mode='w')
    # create a stream for logger
    log_stream = tempfile.TemporaryFile(mode='w')
    # create a stream for

# Generated at 2022-06-14 13:28:23.078657
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():

    from io import StringIO

    class _MyTqdm(std_tqdm):
        def write(self, s, file=None, end="\n"):
            if file is None:
                file = sys.stdout
            if not (s == "" and end == "\n"):  # noqa pylint: disable=no-else-return
                file.write(s + end)
            else:
                file.write(end)

    stream_handler = _TqdmLoggingHandler(_MyTqdm)
    stream = StringIO()
    stream_handler.stream = stream

    record = logging.LogRecord(name="foo", level=1, pathname="bar", lineno=2,
                               msg="baz", args=(), exc_info=None)
    stream_handler.emit(record)

   

# Generated at 2022-06-14 13:28:31.024954
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect() as pbar:
            for i in pbar(trange(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:28:36.664652
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import io
    import logging

    handler = logging.StreamHandler(io.StringIO())
    logger = logging.getLogger("test_log_redirect")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("Test message")

    with logging_redirect_tqdm():
        logger.info("Test message")

    assert "Test message" in handler.stream.getvalue()

# Generated at 2022-06-14 13:28:43.608360
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from tqdm.std import tqdm  # pylint: disable=unused-import
    import logging
    import sys

    test_info = 'test_info'

    # Create a new stringiostream
    stringiostream = StringIO()

    # Define the _TqdmLoggingHandler
    handler = _TqdmLoggingHandler(tqdm)

    # Redirect the stdout of the _TqdmLoggingHandler to our new stringiostream
    handler.stream = stringiostream

    # Set the logging level of the handler to info
    handler.setLevel(logging.INFO)

    # Get the record of the string test_info
    record = logging.makeLogRecord({'msg': test_info, 'levelno': 20})

    # Send the record to the

# Generated at 2022-06-14 13:28:53.142188
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import sys

    for stream in ['stdout', 'stderr']:
        # [test 1] override stream manually
        with std_tqdm(
                desc='test_override', disable=True,
                file=getattr(sys, stream)) as pbar:
            tqdm_logging_redirect(tqdm_class=std_tqdm,
                                  loggers=[logging.root],
                                  tqdm_kwargs={
                                      'desc': 'test_redirect',
                                      'disable': True})
        assert pbar is None

    # [test 2] use stream from tqdm instance

# Generated at 2022-06-14 13:29:11.880653
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import os
    import logging
    import tempfile
    from tqdm.contrib.logging import logging_redirect_tqdm
    from tqdm.contrib import nanotime
    from tqdm.utils import _term_move_up
    from tqdm import trange

    with tempfile.TemporaryDirectory() as d:
        log_file = os.path.join(d, 'log')
        with open(log_file, 'w') as log_file_obj:
            log = logging.getLogger('test')
            log.setLevel(logging.DEBUG)
            log.addHandler(logging.StreamHandler())
            log.addHandler(logging.FileHandler(log_file_obj))

            log.debug('test1')

# Generated at 2022-06-14 13:29:21.202850
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # pylint: disable=missing-docstring
    class TestTqdm(object):
        buffer = b""

        @classmethod
        def write(cls, msg, file=None):
            cls.buffer += msg.encode()

        @classmethod
        def flush(cls, file=None):
            pass

    print(TestTqdm.buffer)

    handler = _TqdmLoggingHandler(tqdm_class=TestTqdm)
    assert isinstance(handler.formatter, logging.Formatter)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    log.handlers[0].emit(logging.makeLogRecord({"msg": "test"}))

# Generated at 2022-06-14 13:29:28.177988
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

# Generated at 2022-06-14 13:29:36.709047
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    def logger_setup():
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("test").setLevel(logging.INFO)
        logging.getLogger("test").info("Test")

    logger_setup()
    with logging_redirect_tqdm():
        logging.getLogger("test").info("Test")
        with tqdm_logging_redirect(ncols=75):
            logging.getLogger("test").info("Test")

    logger_setup()

# Generated at 2022-06-14 13:29:44.271167
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import tqdm
    from ..std import io as pythons_io
    from io import StringIO
    from ..std import logging as std_logging
    from ..std import time as pythons_time
    import time

# Generated at 2022-06-14 13:29:55.886650
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import tqdm, trange, tqdm_notebook, tqdm_pandas

    loggers = [logging.root, logging.getLogger('tqdm_test')]
    for tqdm_class in [tqdm, trange, tqdm_notebook, tqdm_pandas]:
        with logging_redirect_tqdm(loggers, tqdm_class):
            for logger in loggers:
                logger.info('test1')
        logger.info('test2')

    # final parentheses in tqdm_class.__name__
    with logging_redirect_tqdm(loggers, tqdm_class):
        pass
    assert logger.handlers[-1].stream == sys.stderr

# Generated at 2022-06-14 13:30:05.261071
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    logger = logging.getLogger("test_logger_to_log_file")
    logger.setLevel(logging.INFO)

    # set up logging to file
    logfile = "test_logfile_tqdm_write.log"  # pylint: disable=unused-variable
    fh = logging.FileHandler(logfile, mode="w")
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(fh)

    hdlr = _TqdmLoggingHandler()

# Generated at 2022-06-14 13:30:08.996087
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    original_handlers = logging.root.handlers

    with tqdm_logging_redirect(total=1) as pbar:
        assert pbar.n == 0
        logging.root.info("FooBar")
        assert pbar.n == 1

    assert logging.root.handlers == original_handlers

# Generated at 2022-06-14 13:30:14.857973
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():  # pragma: no cover
    class StubTqdm(std_tqdm):
        @staticmethod
        def write(s, file):
            assert s == 'message'
            assert file == sys.stdout
            print('success')

    handler = _TqdmLoggingHandler(tqdm_class=StubTqdm)
    handler.format = lambda x: 'message'
    handler.stream = sys.stdout

    handler.emit(None)


# Generated at 2022-06-14 13:30:19.761638
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import tqdm
    from .logging import logging_redirect_tqdm

    logger = logging.getLogger(__name__)

    with tqdm(range(5), leave=False, bar_format='{l_bar}') as pbar, \
            logging_redirect_tqdm(loggers=[logger], tqdm_class=tqdm):
        for i in range(5):
            if i == 4:
                logger.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:30:39.459421
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from contextlib import contextmanager

    @contextmanager
    def func(i):
        yield i

    log = logging.getLogger(__name__)
    log.propagate = False

    output = []

    def _func(i):
        return func(i)

    def add_handler():
        console_handler = logging.StreamHandler()
        log.addHandler(console_handler)
        return console_handler, None

    # test
    for i in range(3):
        old_handler, old_formatter = add_handler()
        if i == 1:
            with logging_redirect_tqdm():
                log.info(1)
                log.info(2)
                with _func(3) as f:
                    log.info(f)
        log.removeHandler(old_handler)

# Generated at 2022-06-14 13:30:48.943359
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    LOG = logging.getLogger(__name__)

    try:
        # silence stdout
        oldout = sys.stdout
        olderr = sys.stderr
        sys.stdout = sys.stderr = open('/dev/null', 'w')

        with logging_redirect_tqdm(tqdm_class=std_tqdm):
            LOG.info('console logging redirected to `tqdm.write()`')
            LOG.warning('you should not see this on stdout')
    finally:
        sys.stdout = oldout
        sys.stderr = olderr



# Generated at 2022-06-14 13:30:54.732538
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import tqdm

    LOG = logging.getLogger(__name__)

    with tqdm.std.tqdm(total=9) as progress_bar:
        # redirect console logging to `tqdm.write()`
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                progress_bar.update()
        # logging restored

# Generated at 2022-06-14 13:31:00.896693
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from .py3compat import StringIO
    import logging
    from .tqdm import trange
    with StringIO() as captured:
        with tqdm_logging_redirect(
                file=captured,
                loggers=[logging.root],
                miniters=1):
            for i in trange(3):
                logging.info('log_{}'.format(i))

# Generated at 2022-06-14 13:31:03.323665
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    log = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        log.warning('Hello tqdm!')



# Generated at 2022-06-14 13:31:07.243718
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)
    with tqdm_logging_redirect(unit='unit', total=100, smoothing=0) as pbar:
        for i in range(100):
            log.debug("test log message {}".format(i))
            pbar.update(1)

# Generated at 2022-06-14 13:31:16.065518
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        # Initialize logger
        logging.basicConfig(level=logging.INFO)
        LOG = logging.getLogger('TqdmLoggingHandler')
        # Test logger
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
    except(Exception):
        # Test failed
        raise AssertionError("logging_redirect_tqdm function failed")
    else:
        # Test succeeded
        pass


# Generated at 2022-06-14 13:31:20.606473
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with tqdm_logging_redirect(total=5, logger=logger) as pbar:
        for i in range(5):
            logger.info("foo")
            pbar.update()

# Generated at 2022-06-14 13:31:29.675616
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .testing import closing, captured_stdout
    import logging

    with closing(captured_stdout()):
        LOG = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        LOG.info("something before")
        with logging_redirect_tqdm():
            LOG.info("should be in tqdm")
        LOG.info("something after")

        # Verify that the message hasn't been written twice
        output = captured_stdout.getvalue()
        assert len([line for line in output.split('\n')
                    if line.strip() == "should be in tqdm"]) == 1

# Generated at 2022-06-14 13:31:34.372333
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect() as pbar:
        for _ in range(3):
            pbar.update()
            LOG.info('TEST')


if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:31:59.494051
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

# Generated at 2022-06-14 13:32:09.472241
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    import os
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    class Printer(object):
        def __init__(self):
            self.arr = []

        def write(self, s):
            self.arr.append(s.strip())

    with Printer() as p:
        with logging_redirect_tqdm(loggers=[LOG], tqdm_class=type(p)):
            for i in trange(3):
                LOG.info('foo')

    assert p.arr == [str(i) for i in range(1, 4)]


# Generated at 2022-06-14 13:32:12.744969
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    from tqdm import trange
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:32:16.987135
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.info("1")
    logger.info("2")
    with logging_redirect_tqdm():
        logger.info("3")
        logger.info("4")
    logger.info("5")
    logger.info("6")


# Generated at 2022-06-14 13:32:24.192467
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(loggers=[LOG]):
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:32:29.694085
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



# Generated at 2022-06-14 13:32:41.101470
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging  # pylint: disable=import-outside-toplevel
    from tqdm import trange  # pylint: disable=import-outside-toplevel
    # from tqdm.contrib.logging import (  # pylint: disable=import-outside-toplevel
    #     logging_redirect_tqdm, tqdm_logging_redirect)
    loggers = [logging.getLogger(__name__), logging.root]
    for i in trange(3, desc='outer'):
        with tqdm_logging_redirect(
                loggers=loggers,
                disable=i == 0,
                desc='inner',
                unit_scale=True,
                total=100):
            for _ in range(100):
                logging.info('info')
           

# Generated at 2022-06-14 13:32:49.014311
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    from .tests import TestCase

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger('test_logging_redirect_tqdm')

    with tqdm_logging_redirect(
            loggers=[LOG],
            total=65536,
            miniters=1024,
            desc="Redirected logging"
    ) as pbar:
        pbar.update(32)
        pbar.set_postfix(test=1)
        LOG.info('Redirected log #1')
        LOG.info('Redirected log #2')

    LOG.info('Original log #1')
    LOG.info('Original log #2')


# Generated at 2022-06-14 13:32:53.971261
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(total=10) as pbar:
        for i in range(10):
            pbar.set_postfix({'test': i})
            logging.info("test {}".format(i))
        assert pbar.n == 10



# Generated at 2022-06-14 13:33:04.825271
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)

    logging_messages = []
    console_logging_messages = []

    def hook_logging():
        # type: () -> None
        def hook(record):
            logging_messages.append(record)

        def hook_console(record):
            console_logging_messages.append(record)

        hook_console_handler = logging.StreamHandler()
        hook_console_handler.emit = hook_console
        sys.stdout.write('stdout console logging hook enabled\n')
        logging.root.addHandler(hook_console_handler)

        hook_handler = logging.StreamHandler()
        hook_handler.emit = hook
        sys.stdout.write('logging hook enabled\n')
        logging.root.addHandler(hook_handler)

# Generated at 2022-06-14 13:33:45.135955
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Basic unit test.
    """
    import logging

    with logging_redirect_tqdm():
        logging.info('Message')



# Generated at 2022-06-14 13:33:51.349697
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():

    import logging

    # Create a logger
    LOG = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    r_handler = logging.handlers.RotatingFileHandler('foo.log', 'a', 1e6, 10)
    c_handler.setLevel(logging.DEBUG)
    r_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    r_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    r_handler.set

# Generated at 2022-06-14 13:34:00.265221
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import unittest
    import io
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    class TestTqdmLoggingRedirect(unittest.TestCase):

        def test_tqdm_logging_redirect(self):

            with io.StringIO() as my_stdout:
                sys.stdout = my_stdout

                with tqdm_logging_redirect() as pbar:
                    for i in trange(4):
                        if i == 2:
                            LOG.info("console logging redirected to `tqdm.write()`")

                sys.stdout = sys.__stdout__


# Generated at 2022-06-14 13:34:11.226777
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    pytest = pytest_import_error()  # type: ignore
    import logging
    from tqdm.std import tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

    c = [0]
    def mock_write(s):
        # type: (str) -> None
        c[0] += 1

    tqdm.write = mock_write

# Generated at 2022-06-14 13:34:20.452090
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class Tqdm(std_tqdm):
        """class Tqdm, to be used in the test_emit_handler
        """
        last_msg = ""
        last_file = ""

        @classmethod
        def write(cls, msg, file):
            cls.last_msg = msg
            cls.last_file = file

    handler = _TqdmLoggingHandler(Tqdm)
    handler.stream = sys.stderr

    record = logging.LogRecord(level=1, msg="hello", pathname="", lineno=0,
                               name="", exc_info=None, func="")
    handler.emit(record)
    assert Tqdm.last_msg == "hello"
    assert Tqdm.last_file == sys.stderr


# Generated at 2022-06-14 13:34:28.063820
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from .utils import _range
    from .std import tqdm as std_tqdm
    from .std import tnrange as std_tnrange
    from .std import trange as std_trange
    from .std import tqdm_gui as std_tqdm_gui
    from .std import tqdm_notebook as std_tqdm_notebook
    from .std import tgrange as std_tgrange
    from .std import tqdm_pandas as std_tqdm_pandas
    from .std import tdqm as std_tdqm

    # check tqdm_class=std_tqdm
    std_tqdm.write = None
    logger = logging.getLogger(__name__)

# Generated at 2022-06-14 13:34:38.680492
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # Issue https://github.com/tqdm/tqdm/issues/353
    from io import StringIO
    from tqdm import tqdm_notebook
    from .tqdmbase import tqdm as tqdm_console
    for tqdm_class in [tqdm_console, tqdm_notebook]:
        for dest in [StringIO(), sys.stdout]:
            handler = _TqdmLoggingHandler(tqdm_class=tqdm_class)
            handler.stream = dest
            handler.setFormatter(logging.Formatter())
            assert handler.stream == dest
            handler.emit(logging.LogRecord('test', logging.INFO, 'test.py',
                                           'test', 'test', None, None))

# Generated at 2022-06-14 13:34:42.319973
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    import logging
    import sys

    with tqdm_logging_redirect() as pbar:
        for i in range(3):
            pbar.update()
            logging.info("Hello" + str(i))
        if sys.version_info[0] >= 3:
            assert 'Hello' in pbar.writelines[0]
        else:
            assert 'Hello' in pbar.write_buf.getvalue()
            assert 'Hello' in pbar.write_buf.buf




# Generated at 2022-06-14 13:34:48.305195
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    with StringIO() as sio:
        with logging_redirect_tqdm(tqdm_class=std_tqdm) as q:
            std_tqdm.set_lock(q.get_lock())
            logger = logging.getLogger('test')
            logger.error('test')
            logger.info('test')
        assert 'test' in sio.getvalue()

    with StringIO() as sio:
        logging.basicConfig(level=logging.ERROR)

# Generated at 2022-06-14 13:34:58.424557
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import random
    import logging
    # tqdm = std_tqdm
    # loggers = None

    logger = logging.getLogger('tqdm_logging')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    with tqdm_logging_redirect(loggers=[logger, logging.root],
                               tqdm_class=std_tqdm,
                               total=100,
                               unit='foo'):
        for i in range(100):
            logger.info('Mixture of {} and text logs'.format(random.randint(0, 100)))
            std_tqdm.write('Just some text logs')


if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:36:37.352505
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO

    from ..utils import _range
    from .tests import closing
    from .tqdm_gui import tqdm

    with closing(StringIO()) as s:
        sys.stdout = s
        h = tqdm._tqdm_gui._TqdmLoggingHandler()  # pylint: disable=protected-access
        h.setLevel(0)
        for i in _range(6):
            h.emit(logging.LogRecord("", logging.INFO, "", 0, "Test record %d" % i, None, None))
            print("From test", i)

    s.seek(0)

# Generated at 2022-06-14 13:36:39.917227
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import TestCase
    from .tests import tqdm

    with TestCase(tqdm) as tc:
        with tc.assertStdoutSim('0%|          | 0/9 [00:00<?, ?it/s]'):
            with tqdm_logging_redirect(total=9):
                pass



# Generated at 2022-06-14 13:36:44.760568
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    from tqdm import tqdm
    from io import StringIO
    from .tqdm import TqdmDeprecationWarning

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    class TestException(Exception):
        pass

    for handler in [logging.StreamHandler(sys.stdout),
                    _TqdmLoggingHandler()]:
        logger.handlers = []
        logger.addHandler(handler)

        # Test the message is emitted
        logger.info("Test")
        assert handler.stream.getvalue() == "\nTest"

        # Test exception is not raised
        handler.handleError = lambda record: 1 / 0  # noqa: E731
        logger.error("Error")

# Generated at 2022-06-14 13:36:51.469318
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import trange
    import time
    import logging

    LOG = logging.getLogger(__name__)

    # logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in trange(9):
            time.sleep(0.1)
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored



# Generated at 2022-06-14 13:36:56.071271
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from tqdm import trange
        import logging
        LOG = logging.getLogger(__name__)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
    except ImportError:
        pass


# Generated at 2022-06-14 13:37:01.228507
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)
    with tqdm_logging_redirect(total=9):
        for _ in range(9):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:37:09.502041
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                    # sys.stdout.write("console logging redirected to `tqdm.write()`\n")
        # logging restored


# Generated at 2022-06-14 13:37:14.161836
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import time
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                time.sleep(1)

# Generated at 2022-06-14 13:37:15.701258
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    with logging_redirect_tqdm():
        logging.info('Writing to stdout via logging redirected to tqdm.write()')



# Generated at 2022-06-14 13:37:23.436304
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        LOG.info('console logging redirected to `tqdm.write()`')
    print('console logging restored')

    assert 'console logging restored' in open('logger.log').read()
    assert 'console logging redirected to `tqdm.write()`' in open('logger.log').read()