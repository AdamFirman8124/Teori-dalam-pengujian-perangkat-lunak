

# Generated at 2022-06-14 13:27:59.171156
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from unittest import mock
    except ImportError:
        import mock  # noqa

    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    def test_func(pbar):
        logging.info("info")
        logging.warning("warning")

    with mock.patch('tqdm.contrib.logging._TqdmLoggingHandler') as mock_class:
        tqdm_logging_redirect(range(10), miniters=10)
        assert mock_class.call_count == 1, \
            ("_TqdmLoggingHandler should only be called when "\
             "tqdm_logging_redirect is used.")


# Generated at 2022-06-14 13:28:08.462987
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm as tqdm_std
    from ..std import mock
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        LOG = logging.getLogger(__name__)
        with mock.patch('sys.stderr', new_callable=mock.StringIO) as mock_stderr:
            for i in range(5):
                LOG.info("test_logging_redirect_tqdm")
        output_string = " ".join(mock_stderr.getvalue().split())
        assert len(
            list(filter(
                lambda x: x == "test_logging_redirect_tqdm", output_string.split()))) == 5
        assert len(output_string.split()) == 5

    # test log

# Generated at 2022-06-14 13:28:15.023054
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Test function for logging_redirect_tqdm"""
    # logging.basicConfig(level=logging.INFO)
    # Clean up
    logger = logging.getLogger('tqdm.std.__main__')
    for handler in logger.handlers:
        logger.removeHandler(handler)
    # Explicitly add StreamHandler so that output points to stderr
    logger.addHandler(logging.StreamHandler())

    # At the moment, this is basically just a syntax check
    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                logger.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:21.991931
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import tempfile
    import time
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with tempfile.TemporaryFile() as f:
        with logging_redirect_tqdm(loggers=[LOG]):
            for i in range(9):
                if i == 4:
                    LOG.info("hahahahahahahahahahahahahahahahahaha")
                time.sleep(0.1)  # simulate work


# Generated at 2022-06-14 13:28:33.086037
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    if sys.version_info >= (3, 0):
        from io import TextIOWrapper  # pylint: disable=no-name-in-module
    else:
        TextIOWrapper = object
    import logging
    old_logger_handlers = logging.root.handlers
    logging.root.handlers = []

# Generated at 2022-06-14 13:28:38.218781
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(total=9) as pbar:
        for i in range(9):
            pbar.update()
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
    assert pbar.n == 9



# Generated at 2022-06-14 13:28:43.216050
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import trange
    import logging

    LOG = logging.getLogger('test_logging_redirect_tqdm')
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm(loggers=[LOG]):
        for _ in trange(9):
            LOG.info('console logging redirected to `tqdm.write()`')



# Generated at 2022-06-14 13:28:48.776802
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    with tqdm_logging_redirect(total=9, desc='test_tqdm_logging_redirect'):
        for i in trange(9):
            if i == 4:
                LOG = logging.getLogger(__name__)
                LOG.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:28:56.093914
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm, trange

    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        for _ in trange(9):
            logging.info('this is a test\n')
        for _ in trange(9):
            try:
                raise RuntimeError
            except RuntimeError:
                logging.error('this is an error\n', exc_info=True)

    with logging_redirect_tqdm(loggers=[logging.getLogger('test')],
                               tqdm_class=tqdm):
        for _ in trange(9):
            logging.info('another test\n')

    print('finished logging_redirect_tqdm test')



# Generated at 2022-06-14 13:29:00.756771
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    log = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(8):
            if i == 4:
                log.info("this should be printed on the console")
                log.debug("this should not be printed on the console")



# Generated at 2022-06-14 13:29:13.750739
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        LOG.info('Logging redirected to `tqdm.write()`')
    return True



# Generated at 2022-06-14 13:29:21.330403
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    # ---
    try:
        import colorama
        colorama.init()
        color = {
            'DEBUG': colorama.Fore.BLUE,
            'INFO': '',
            'WARNING': colorama.Fore.YELLOW,
            'ERROR': colorama.Fore.RED,
            'CRITICAL': colorama.Back.RED}
    except ImportError:
        color = {'DEBUG': '', 'INFO': '', 'WARNING': '', 'ERROR': '',
                 'CRITICAL': ''}
        pass
    # ---
    fmt = color['INFO'] + '%(msg)s' + colorama.Style.RESET_ALL
    logging.basicConfig(level=logging.INFO, format=fmt)
    # ---

# Generated at 2022-06-14 13:29:24.947611
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    try:
        with tqdm_logging_redirect(total=9, tqdm_class=tqdm) as pbar:
            for _i in pbar:
                pass
    except Exception:
        pass

# Generated at 2022-06-14 13:29:31.695193
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class CustomTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):
            self.write_output = kwargs.pop("write_output", None)
            self.file = kwargs.pop("file", None)
            super(CustomTqdm, self).__init__(*args, **kwargs)

        def write(self, *args, **kwargs):
            self.write_output = args[0]
            self.file = args[1]

    logger = logging.getLogger(__name__)
    custom_tqdm = CustomTqdm(write_output="", file=None)
    handler = _TqdmLoggingHandler(tqdm_class=custom_tqdm)
    logger.addHandler(handler)

# Generated at 2022-06-14 13:29:40.775754
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Tests logging_redirect_tqdm.
    """
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



# Generated at 2022-06-14 13:29:47.113625
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging

    with tqdm_logging_redirect(
            ['Iteration ' + str(i) for i in range(5)],
            total=5
        ) as pbar:
        LOG = logging.getLogger(__name__)
        LOG.info("console logging redirected to `tqdm.write()`")
        # `pbar` is the progress bar
        for item in pbar:
            pbar.write(item)

# Generated at 2022-06-14 13:29:54.542359
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm

    log = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                log.info("console logging redirected to `tqdm.write()`")

    for i in range(9):
        if i == 4:
            log.info("console logging restored")

# Generated at 2022-06-14 13:29:58.909011
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    try:
        from unittest import mock
    except ImportError:
        import mock
    m = mock.mock_open()
    with mock.patch('builtins.open', m, create=True) as _:
        with tqdm_logging_redirect(ncols=100, mininterval=0.1,
                                   unit_scale=True, unit='B',
                                   file=open('/dev/null', 'w+')):
            pass

# Generated at 2022-06-14 13:30:02.406616
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from .test_tqdm import closing, pretest_posttest
    with closing(pretest_posttest()):
        with logging_redirect_tqdm():
            logging.info("test message")
        # logging restored



# Generated at 2022-06-14 13:30:10.386777
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    original_stdout = sys.stdout
    sys.stdout = None

    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect
    LOG = logging.getLogger(__name__)

    logging.basicConfig(
        format='%(asctime)s %(message)s', level=logging.INFO)

    with tqdm_logging_redirect(total=100) as pbar:
        assert pbar.total == 100
        for _ in trange(9):
            assert pbar.n == _
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    assert pbar.n == 9
    assert pbar.total == 100

    sys.stdout = original

# Generated at 2022-06-14 13:30:25.334535
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:30:32.502015
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


if __name__ == "__main__":
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:30:40.234494
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm
    LOG = logging.getLogger(__name__)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        logging.info("logging restored")
        # Result:
        #   console logging redirected to `tqdm.write()`
        #   logging restored (not redirected to `tqdm.write()`)


# Generated at 2022-06-14 13:30:44.650311
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    with tqdm_logging_redirect() as pbar:
        assert pbar == tqdm
        with logging_redirect_tqdm():
            logging.info("tqdm logging redirection activated")
        # logging restored

# Generated at 2022-06-14 13:30:54.855981
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    # Setup logging handlers
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Run the actual test
    expected = ["test message1", "...", "test message2", "...\n"]
    logger.info("test message1")
    with tqdm_logging_redirect(loggers=[logger], total=3) as pbar:
        pbar.set_description("...")
        logger.info("test message2")
        pbar.update(1)


# Generated at 2022-06-14 13:31:00.978476
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    import threading
    import queue
    import tqdm
    tqdm.tqdm = tqdm.std.tqdm
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    sample_text = 'Message from thread'
    test_queue = queue.Queue()
    # Start a thread to log and send
    # the last logged message through the queue
    def logger_thrd():
        with tqdm_logging_redirect(desc='Testing logging', unit='messages', unit_scale=True):
            for i in tqdm.trange(5):
                LOG.info(sample_text+' '+str(i))
                time.sleep(1)

# Generated at 2022-06-14 13:31:06.103834
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    loggers = [logging.getLogger('test_tqdm_logging_redirect')]
    with tqdm_logging_redirect(loggers=loggers) as t:
        for i in range(5):
            t.update(1)
            logging.info('hello world')


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-14 13:31:17.533280
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    try:
        from StringIO import StringIO  # Python 2
    except ImportError:
        from io import StringIO  # Python 3
    assert(sys.version_info >= (2, 7))
    assert(sys.version_info < (3, 0))
    sys.stdout = StringIO()
    sys.stderr = StringIO()

# Generated at 2022-06-14 13:31:19.253673
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        LOG.info("This is a test message")
        LOG.error("This is another test message")

# Generated at 2022-06-14 13:31:23.717672
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import sys
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    handler = _TqdmLoggingHandler()
    handler.setFormatter(logging.Formatter('%(message)s'))
    handler.stream = sys.stdout
    log.addHandler(handler)
    log.info('hello world!')
    log.info('hello world!')
    log.info('hello world!')



# Generated at 2022-06-14 13:32:04.042603
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    from tqdm.auto import tqdm

    stream = StringIO()
    handler = _TqdmLoggingHandler(tqdm)
    handler.stream = stream
    record = logging.LogRecord('logger', logging.INFO, 'path', 1, 'message', [], None)
    handler.emit(record)
    assert stream.getvalue() == 'message\n'

# Generated at 2022-06-14 13:32:11.296627
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Test function logging_redirect_tqdm

    Returns
    -------
    None
    """
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


# Generated at 2022-06-14 13:32:14.769017
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import sys

    buffer = io.StringIO()
    sys.stdout = buffer

    handler = _TqdmLoggingHandler()
    handler.write('123')
    sys.stdout = sys.__stdout__

    buffer.getvalue() == '123'

# Generated at 2022-06-14 13:32:25.288101
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .std import tqdm as std_tqdm
    import logging
    from io import StringIO
    from contextlib import contextmanager

    LOG = logging.getLogger(__name__)

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-14 13:32:30.257757
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        for _ in range(2):
            LOG.info("printing message")

# Generated at 2022-06-14 13:32:35.263868
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    with tqdm_logging_redirect(desc="Redirected logging test") as pbar:
        LOG.info("in tqdm_logging_redirect")
        pbar.update(1)

# Generated at 2022-06-14 13:32:42.295957
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from .tqdm import tqdm
    from .logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:32:47.475329
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import test

    with test("tqdm_logging_redirect"):
        from .tests.tqdm import tqdm

        with tqdm_logging_redirect(total=10) as pbar:
            for i in range(10):
                pbar.update()



# Generated at 2022-06-14 13:32:56.779286
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.auto import trange
    import logging
    from .utils import trange_iter

    class _TqdmHandler(logging.StreamHandler):

        def emit(self, record):
            try:
                msg = self.format(record)
                std_tqdm.write(msg, file=self.stream)
                self.flush()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:  # noqa pylint: disable=bare-except
                self.handleError(record)

    # sanity check
    with logging_redirect_tqdm():
        logging.info('This should be redirected to tqdm!')

    # check that tqdm is correctly restored

# Generated at 2022-06-14 13:33:03.983688
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    loggers = []
    with tqdm_logging_redirect(range(5), loggers=loggers, postfix='logging') as pbar:
        pbar.set_postfix(postfix='stdout')
        logging.info('hello')
        assert loggers[0].handlers[0].stream == pbar.file.buffer
        with tqdm_logging_redirect(range(5), loggers=loggers, postfix='nested') as _:
            pass
        print('some stdout')
        logging.info('hello again')
        assert loggers[0].handlers[0].stream == pbar.file.buffer

# Generated at 2022-06-14 13:33:51.021737
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    def log_simple():
        # type: () -> None
        LOG.info('This is an info level message.')
        LOG.warning('This is a warning level message.')
        LOG.error('This is an error level message.')

    LOG = logging.getLogger(__name__)

    # Logging at info level and above should be shown with logging_redirect_tqdm
    LOG.setLevel(logging.INFO)
    with logging_redirect_tqdm():
        log_simple()

    # Logging at warning level and above should be shown with logging_redirect_tqdm
    LOG.setLevel(logging.WARNING)
    with logging_redirect_tqdm():
        log_simple()

    # Logging at error level and above should

# Generated at 2022-06-14 13:33:57.329650
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    from tqdm import tnrange
    from tqdm.contrib.logging import tqdm_logging_redirect

    with tqdm_logging_redirect(total=7) as pbar:
        assert pbar is not None
        for _ in tnrange(7):
            logging.info('a')
        logging.info('b')

# Generated at 2022-06-14 13:34:07.822649
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """Unit test for function logging_redirect_tqdm"""
    import logging
    from contextlib import contextmanager
    from tqdm.contrib.logging import logging_redirect_tqdm
    from .tests_tqdm import captured_stdout  # pylint: disable=unused-import

    @contextmanager
    def calling_foo():
        yield


# Generated at 2022-06-14 13:34:14.276369
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    logger = logging.getLogger('example')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(console)

    logger.info('info message')

    with logging_redirect_tqdm():
        for i in range(10):
            logger.info(i)

    logger.info('info message')



# Generated at 2022-06-14 13:34:16.364470
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    with tqdm_logging_redirect() as pbar:
        assert isinstance(pbar, std_tqdm)
        assert not pbar.leave
        LOG = logging.getLogger(__name__)
        LOG.error("test")

# Generated at 2022-06-14 13:34:23.476156
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    The following lines should display the following output
        [INFO] console logging redirected to `tqdm.write()`
        100%|██████████| 9/9 [00:00<00:00, 1680.33it/s]
    """
    import logging
    from tqdm import trange
    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:34:27.257301
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    with mock.patch('tqdm.contrib.logging._TqdmLoggingHandler.emit') as mock_emit:
        with tqdm_logging_redirect() as pbar:
            logging.getLogger(__name__).info('text')
    assert mock_emit.called
    assert logging.getLogger(__name__).handlers == []
    assert pbar.desc == 'text'

# Generated at 2022-06-14 13:34:30.431834
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logger = logging.getLogger(__name__)
    with logging_redirect_tqdm([logger]):
        logger.info("test")


# Generated at 2022-06-14 13:34:39.423235
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from .misc import test_env
    with test_env() as (_, capsys):
        import logging
        LOG = logging.getLogger(__name__)
        LOG.info("test start")
        with logging_redirect_tqdm():
            LOG.info("console logging redirected to `tqdm.write()`")
        LOG.info("test end")
        captured = capsys.readouterr()
        assert captured.out == "test start\nconsole logging redirected to `tqdm.write()`\n"
        assert captured.err == ""  # noqa # pylint: disable=used-before-assignment

# Generated at 2022-06-14 13:34:46.426834
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from unittest import TestCase
    from six.moves import StringIO

    class Foo(TestCase):
        def test(self):
            out = StringIO()
            def cb(*args, **kwargs):
                out.write("callback " + str(args) + str(kwargs) + "\n")

            msg = "Hello, world!"
            record = logging.LogRecord("name", logging.INFO,
                                       "/foo/bar/baz.py", 666, msg, [], None)
            handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
            handler.emit(record)
            self.assertEqual(out.getvalue(), msg + "\n")

            handler.tqdm_class = None

# Generated at 2022-06-14 13:36:16.683305
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from StringIO import StringIO
    from logging import LogRecord
    from inspect import currentframe
    import os

    # initialize
    orig_stdout = sys.stdout
    stdout_redirect = StringIO()
    sys.stdout = stdout_redirect

    # create
    parent_frame = currentframe().f_back
    log_filename = parent_frame.f_code.co_filename
    log_lineno = parent_frame.f_lineno
    log_msg = "log message at line %d of file %s" % (log_lineno, log_filename)
    log_record = LogRecord('name', 10, log_filename, log_lineno,
                           log_msg, [], None)

    # test
    handler = _TqdmLoggingHandler()

# Generated at 2022-06-14 13:36:26.071996
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from contextlib import closing
    from tqdm._utils import _term_move_up

    from .helpers import closing_if_not

    with closing(closing_if_not(std_tqdm(range(3), leave=False),
                                std_tqdm.disable)) as q:
        with tqdm_logging_redirect(total=3, tqdm_class=q.__class__) as pbar:
            logging.info("foo")
            pbar.update(1)
            logging.info("bar")
            pbar.update(2)

    assert _term_move_up() + _term_move_up() + _term_move_up() + _term_move_up()
    print("foo")
    print("bar")

# Generated at 2022-06-14 13:36:34.117719
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    import logging
    LOG = logging.getLogger(__name__)

    def _test(log_class):
        with logging_redirect_tqdm():
            log_class(
                "console logging redirected to `tqdm.write()`",
                level=logging.INFO)  # pylint: disable=unexpected-keyword-arg

    try:
        # Python 2
        from StringIO import StringIO
    except ImportError:
        # Python 3
        from io import StringIO
    with StringIO() as stream:
        for log_class in (logging.debug, logging.info, logging.warning,
                          logging.error, logging.critical):
            _test(log_class)
            assert stream.getvalue().strip() == ""

# Generated at 2022-06-14 13:36:40.930447
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import tqdm
    from tqdm._utils import _range

    with tqdm_logging_redirect(range(45),
                               logger=logging.getLogger(__name__),
                               tqdm_class=tqdm,
                               desc="Example") as pbar:
        for i in pbar:
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")
                pbar.set_postfix(i=i)


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:36:44.249205
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tqdm import tqdm
    import logging
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        for i in tqdm(range(9)):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")


# Generated at 2022-06-14 13:36:55.042683
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import os
    import sys
    import logging
    import time
    import tempfile

    _test_out = b''

    def test_logging_redirect():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        logger.stream_handler = logging.StreamHandler()
        logger.stream_handler.stream = sys.stdout
        logger.addHandler(logger.stream_handler)
        logger.debug('test_logging_redirect 1')
        logger.debug('test_logging_redirect 2')

        global _test_out
        with tempfile.TemporaryFile(mode='w+b') as f:
            sys.stdout = f
            assert [handler.stream for handler in logger.handlers] == [f]


# Generated at 2022-06-14 13:37:00.990690
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm(loggers=[LOG]):
        LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored
    return



# Generated at 2022-06-14 13:37:10.586720
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.utils import _term_move_up
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


# Generated at 2022-06-14 13:37:17.654666
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    log_to_cons_log_to_file()
    log_to_file_log_to_cons()
    log_to_cons_log_to_cons()
    log_to_file_log_to_file()
    log_to_cons()
    log_to_file()

    log_to_cons_log_to_cons_log_to_file()
    log_to_cons_log_to_file_log_to_file()



# Generated at 2022-06-14 13:37:26.054231
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Test function logging_redirect_tqdm
    """
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm
    try:
        from io import StringIO
    except ImportError:
        from io import BytesIO as StringIO

    import sys

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)

        # regular output
        with StringIO() as str_buffer:
            sys.stdout = str_buffer
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
            str_buffer.seek(0)
            assert str