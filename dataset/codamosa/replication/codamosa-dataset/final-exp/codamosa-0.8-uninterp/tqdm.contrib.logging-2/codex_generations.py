

# Generated at 2022-06-14 13:27:46.373945
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    def _get_formatted_msg(record):
        msg = _TqdmLoggingHandler().format(record)
        return msg

    level = logging.DEBUG
    record = logging.LogRecord(
        name='name', level=level, pathname='pathname', lineno=1, msg='msg',
        args=(), exc_info=None)

    assert 'msg' in _get_formatted_msg(record)

    record.levelname = logging.getLevelName(level)
    record.msg = '%s'
    assert 'msg' in _get_formatted_msg(record)

    record.msg = '%(msg)s'
    assert 'msg' in _get_formatted_msg(record)

    record.msg = '%(long_arg)s'
    assert 'long_arg' not in record

# Generated at 2022-06-14 13:27:56.175064
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Tests function tqdm_logging_redirect.
    """
    # set up tqdm_logging_redirect arguments
    tqdm_kwargs = {'total': 1,
                   'position': 1,
                   'desc': 'redirecting',
                   'loggers': [logging.getLogger()]}
    logging_redirect_tqdm_args = [tqdm_kwargs['loggers']]
    logging_redirect_tqdm_kwargs = dict()
    tqdm_logging_redirect_args = []
    tqdm_logging_redirect_kwargs = tqdm_kwargs

    # check for desired output with tqdm_logging_redirect

# Generated at 2022-06-14 13:28:01.149143
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Unit test to ensure that logging_redirect_tqdm() operates as expected
    """
    import logging
    from _tqdm import tqdm

    # create test logger that we can mess with
    LOG = logging.getLogger(__name__)

    # create dummy handler that won't do anything with the logs
    class DummyHandler(logging.NullHandler):
        def emit(self, record):
            pass

    # set up basic logger properties
    logging.basicConfig(level=logging.INFO, handlers=[DummyHandler()])

    # ensure that it has the tqdm handler, but not the stream handler
    assert len(LOG.handlers) == 1
    assert isinstance(LOG.handlers[0], DummyHandler)

    # first use-case: as context manager with

# Generated at 2022-06-14 13:28:09.712340
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    try:
        from unittest import mock
    except ImportError:
        import mock

    import io
    import logging
    import sys

    with mock.patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
        handler = _TqdmLoggingHandler()
        logger = logging.getLogger('logger')
        logger.addHandler(handler)

        logger.critical('critical')
        assert mock_stderr.getvalue() == 'critical\n'

        logger.error('error')
        assert mock_stderr.getvalue() == 'critical\nerror\n'

        logger.warning('warning')
        assert mock_stderr.getvalue() == \
            'critical\nerror\nwarning\n'

        logger.info('info')
        assert mock

# Generated at 2022-06-14 13:28:14.441616
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    from .std import tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(tqdm=tqdm) as pbar:
            for i in pbar:
                LOG.info("console logging redirected to tqdm.write()")
                time.sleep(0.2)
                if i >= 10:
                    break

# Generated at 2022-06-14 13:28:18.680420
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # pylint: disable=missing-docstring
    import logging
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect():
        LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:25.968145
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import unittest

    # Create message and set the level
    message = "test_message"
    level = logging.DEBUG

    # Create the handler, a stream, a logger and a record
    handler = _TqdmLoggingHandler()
    stream = io.StringIO()
    logger = logging.Logger("dummy_logger")
    logger.setLevel(level)
    logger.addHandler(handler)
    handler.setLevel(level)
    record = logger.makeRecord(logger.name, level, "", 0, message, None, None)

    # Write the message in the stream
    handler.emit(record)
    stream.seek(0)
    line = stream.readline()
    assert message in line

# Generated at 2022-06-14 13:28:31.959205
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    loggers = [logging.root]
    tqdm_class, loggers, tqdm_kwargs = std_tqdm, loggers, {}
    with tqdm_logging_redirect(tqdm_class=tqdm_class, loggers=loggers, **tqdm_kwargs) as _:
        logging.warning("warning #1")
        logging.warning("warning #2")

# Generated at 2022-06-14 13:28:40.818126
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    class TestTqdm(object):
        def __init__(self, *args, **kwargs):
            self.iterable = args[0]
            self.desc = kwargs.get('desc', '')
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def __iter__(self):
            return self
        def __next__(self):
            if self.iterable == 0:
                raise StopIteration
            self.iterable -= 1
            return None
        next = __next__

    # Create a Logger
    logger = logging.getLogger('TEST')

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')

    # Create formatters and

# Generated at 2022-06-14 13:28:46.900502
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """Unit test for function tqdm_logging_redirect"""
    import pytest
    import logging

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)

    with tqdm_logging_redirect(total=9):
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:29:03.406588
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from tqdm.auto import tqdm

    class _MockTqdmWrite(object):
        def __init__(self):
            self.written = []

        def write(self, string, file=None):
            self.written.append(string)

    class _MockFile(object):
        def __init__(self):
            self.written = []

        def write(self, string):
            self.written.append(string)

        def isatty(self):
            return True


# Generated at 2022-06-14 13:29:10.053835
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG)
        with tqdm_logging_redirect() as pbar:
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                pbar.update()



# Generated at 2022-06-14 13:29:17.108631
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    tqdm_logging_redirect(range(10))
    # The following should work but apparently logging.basicConfig doesn't work
    # correctly when it is called multiple times.
    # logging.basicConfig(level=logging.INFO, format='%(message)s')
    # with tqdm_logging_redirect(range(10), loggers=[logging.getLogger(__name__)]) as mybar:
    #     logger = logging.getLogger(__name__)
    #     for i in mybar:
    #         if i==1:
    #             logger.info("tqdm_logging_redirect works!")

# Generated at 2022-06-14 13:29:26.558104
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """Test tqdm_logging_redirect."""
    import logging
    import tqdm
    loggers = [logging.root]
    with tqdm_logging_redirect(desc='mybar',
                               total=100,
                               loggers=loggers,
                               tqdm_class=tqdm) as pbar:
        pbar.update(50)
        logging.info('Test info')
        assert pbar.n == 50
        pbar.update(pbar.total - pbar.n)
        assert pbar.n == 100
    logging.info('Test info')
    assert pbar.n == 100
    assert pbar.closed, "pbar should be closed"

# Generated at 2022-06-14 13:29:32.433661
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    LOG = logging.getLogger("test_logging_redirect_tqdm")
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in std_tqdm(range(9)):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    return

# Generated at 2022-06-14 13:29:42.431979
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import logging
    import sys
    
    def test_method_emit(self):
        '''
        method emit
        '''
        _TqdmLoggingHandler.emit(self, record)

    global tqdm_write
    
    def write_in_tqdm(x, y):
        tqdm_write.write(x)
    
    tqdm_write = io.BytesIO()
    tqdm_write.write = write_in_tqdm
    stdout_ = sys.stdout
    sys.stdout = tqdm_write
    _TqdmLoggingHandler_inherit = type('_TqdmLoggingHandler_inherit', (_TqdmLoggingHandler,), {'emit' : test_method_emit})

# Generated at 2022-06-14 13:29:54.441024
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Unit test for function logging_redirect_tqdm.
    """
    logging.basicConfig(level=logging.DEBUG)

    # A fake code for usage of function logging_redirect_tqdm
    with tqdm_logging_redirect():
        logging.debug("this message is hidden")
        logging.info("this message is redirected to tqdm.write()")

        with std_tqdm() as pbar:
            for i in pbar:
                logging.info("iteration {0}".format(i))
                if i > 10:
                    break

    # * Everything * should be normal

    # Check if the message is logged
    assert logging.getLogger().hasHandlers()

    # Directly log the message

# Generated at 2022-06-14 13:29:59.197305
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    with logging_redirect_tqdm():
        for i in tqdm(range(9)):
            if i == 4:
                logging.info('console logging redirected to `tqdm.write()`')


# Generated at 2022-06-14 13:30:06.795069
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    """Test function."""
    import logging
    try:
        from tqdm import trange
        from tqdm.contrib.logging import logging_redirect_tqdm
    except ImportError as e:
        print(e)
        return

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:30:14.072101
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    for tqdm_class in [std_tqdm, tqdm]:
        with tqdm_logging_redirect(loggers=[logging.getLogger('tqdm')],
                                   tqdm_class=tqdm_class,
                                   desc='test_tqdm_logging_redirect') as pbar:
            pbar.update(5)
        assert pbar.n == 5
        assert 'tqdm' in logging.getLogger().handlers[0].formatter._fmt
        assert 'RuntimeWarning' in str(pbar)

# Generated at 2022-06-14 13:30:32.353226
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    try:
        from tqdm import trange
    except ImportError:
        pass  # pragma: no cover (pip install tqdm)
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored


# Generated at 2022-06-14 13:30:41.109281
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Test for `logging_redirect_tqdm` function.

    Note: it is not possible to test for the logging output directly, as
    `StreamHandler` is not set up. Only indirectly by checking if it is
    removed and not restored.
    """
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    assert len(LOG.handlers) == 1
    assert isinstance(LOG.handlers[0], logging.StreamHandler)

    with logging_redirect_tqdm():
        assert len(LOG.handlers) == 1

# Generated at 2022-06-14 13:30:52.080789
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    log = logging.getLogger('error_log')
    log.setLevel(logging.DEBUG)

    with tqdm_logging_redirect() as pbar:
        pbar.write("test")
        pbar.update(1)  # pbar.n
        with logging_redirect_tqdm() as tqdm_log:
            tqdm_log.write("test in tqdm log")
            pbar.write("test in pbar")
            pbar.update(1)
            log.error("test in log")

    assert pbar.n == 2
    assert pbar.last_print_n == 4


if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:30:59.219077
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    assert LOG.handlers == [], "Handlers of logger should be empty"

    with logging_redirect_tqdm():
        LOG.info("This message should be redirected to tqdm.write()")

    assert LOG.handlers == [], "Handlers of logger should be empty"

    with logging_redirect_tqdm(loggers=[LOG]):
        LOG.info("This message should be redirected to tqdm.write()")

    assert LOG.handlers == [], "Handlers of logger should be empty"

    def test_function():
        assert LOG.handlers == [], "Handlers of logger should be empty"

        with logging_redirect_tqdm():
            LOG.info("This message should be redirected to tqdm.write()")

# Generated at 2022-06-14 13:31:07.389641
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from tqdm import trange

    class Handler(_TqdmLoggingHandler):
        """
        Inherits from _TqdmLoggingHandler to access its private members
        """
        def __init__(self, stream, tqdm_class=std_tqdm):
            super(Handler, self).__init__(tqdm_class=tqdm_class)
            self.stream = stream

    # test if report is correctly printed
    # if report is correctly printed, then it should be visible in stream
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    stream = sys.stderr
    handler = Handler(stream)
    logger.addHandler(handler)
    report = "hello world"

# Generated at 2022-06-14 13:31:18.769921
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import re
    import os
    # Test with examples/logging_test.py
    logging.basicConfig(level=logging.INFO)
    re_input = re.compile('^input\d+$')
    loggers = [logging.getLogger(m) for m in logging.Logger.manager.loggerDict
               if re_input.match(m)]
    try:
        old_loggers = [logger.handlers for logger in loggers]
        with logging_redirect_tqdm(loggers):
            from examples import logging_test
        new_loggers = [logger.handlers for logger in loggers]
    finally:
        for logger, old_logger in zip(loggers, old_loggers):
            logger.handlers = old_logger

# Generated at 2022-06-14 13:31:23.828322
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



# Generated at 2022-06-14 13:31:30.634087
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(9)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

# Generated at 2022-06-14 13:31:37.261495
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class CustomHandler(_TqdmLoggingHandler):
        def __init__(self):
            super(CustomHandler, self).__init__()
            self.msg = None
            self.err = None

        def emit(self, record):
            try:
                self.msg = super(CustomHandler, self).format(record)
            except Exception as e:
                self.err = e

    logger = logging.getLogger('Test Logger')
    ch = CustomHandler()
    logger.addHandler(ch)
    logger.error("Test Error")
    assert ch.err is None
    assert ch.msg == "Test Error"

# Generated at 2022-06-14 13:31:49.335088
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    # pylint: disable=protected-access
    import logging
    from tqdm._utils import _supports_unicode
    from .tests_tqdm import StringIO

    buffer = StringIO()
    sys.stdout = buffer

    LOG = logging.getLogger(__name__)

    if _supports_unicode:
        linebreak = '\u2029'
    else:
        linebreak = '\n'

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        LOG.info("console logging redirected")
        LOG.info("to `tqdm.write()` with custom" + linebreak + " linebreaks!")
    # logging restored
    logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:32:17.634849
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import sys
    from io import StringIO
    from tqdm import trange
    import logging
    LOG = logging.getLogger(__name__)

    sys.stderr = StringIO()
    with tqdm_logging_redirect(smoothing=.1) as pbar:
        pbar.set_postfix(ord='test')
        for _ in trange(9):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    sys.stderr = StringIO()
    with tqdm_logging_redirect():
        for _ in trange(9):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    sys.stderr = StringIO()
    orig_stder

# Generated at 2022-06-14 13:32:28.933647
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    for tqdm_class in [std_tqdm, std_tqdm.tqdm]:  # type: Type[std_tqdm]
        with tqdm_logging_redirect(
            range(4), tqdm=tqdm_class, ascii=True, dynamic_ncols=True,
            file=sys.stdout, loggers=[logging.root]
        ) as pbar:
            assert pbar.n == 4
            assert len(pbar) == 4
            assert pbar.ascii
            assert pbar.file is sys.stdout
            assert pbar.logging_redirected

        # exit automatically after the context
        assert pbar.n == 4
        assert len(pbar) == 4
        assert pbar.ascii
        assert pbar.file

# Generated at 2022-06-14 13:32:34.794459
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm as std_tqdm

    with logging_redirect_tqdm():
        logging.info("This is a test")
        std_tqdm.write("This is also a test")

    logging.info("This should not be printed")
    std_tqdm.write("This should be printed")


# Generated at 2022-06-14 13:32:37.832428
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm._utils import _term_move_up
    with logging_redirect_tqdm():
        for _ in range(2):
            logging.error("error")
        for _ in range(2):
            logging.warning("warning")
        for _ in range(2):
            logging.info("info")
        for _ in range(2):
            logging.debug("debug")
    # Should not throw any errors
    assert True



# Generated at 2022-06-14 13:32:46.214883
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm
    """
    import logging
    import tempfile

    from tqdm import trange

    # test multiple loggers
    root_logger = logging.getLogger()
    custom_logger1 = logging.getLogger('logger1')
    custom_logger2 = logging.getLogger('logger2')
    custom_logger3 = logging.getLogger('logger3')

    msg1 = 'logger1 message'
    msg2 = 'logger2 message'
    msg3 = 'logger3 message'


# Generated at 2022-06-14 13:32:55.495756
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange, tqdm

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

    with tqdm_logging_redirect('hello', bar_format='{l_bar}') as pbar:
        for i in range(8):
            if i == 3:
                LOG.info('console logging redirected to `pbar.write()`')
            pbar.update()


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:33:01.513002
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect():
        LOG.info("console logging redirected to `tqdm.write()`")
    LOG.info("logging restored")

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:08.561773
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import warnings
    try:
        from tqdm.contrib.logging import tqdm_logging_redirect
    except Exception as e:
        warnings.warn("contrib.logging can't be imported: " + str(e))
        return
    logging.basicConfig(level=logging.INFO)
    for i in tqdm_logging_redirect(unit="B", total=100 * 1024 * 1024,
                                   desc="Downloading"):
        logging.info(str(i))



# Generated at 2022-06-14 13:33:18.034138
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    class _TestLoggingRedirectTqdm(std_tqdm):
        def __init__(self, *args, **kwargs):
            super(_TestLoggingRedirectTqdm, self).__init__(*args, **kwargs)
            self.log_messages = []  # type: List[str]
        def write(self, msg, file=sys.stdout):
            self.log_messages.append(msg)

    with tqdm_logging_redirect(
            total=10,
            tqdm_class=_TestLoggingRedirectTqdm) as pbar:
        logging.info('logged message 1')
        pbar.update(1)
        logging.info('logged message 2')
        pbar.update(1)

    assert len

# Generated at 2022-06-14 13:33:28.017708
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys

    def my_class(*args, **kwargs):
        return std_tqdm(*args, **kwargs)

    # only stdout
    with tqdm_logging_redirect(tqdm_class=my_class, disable=True) as pbar:
        assert sys.stdout is not pbar.fp
        pbar.write('test')

    # only stderr
    with tqdm_logging_redirect(tqdm_class=my_class, file=sys.stderr, disable=True) as pbar:
        assert sys.stderr is not pbar.fp
        pbar.write('test')

    class MyStream:

        def __init__(self):
            self.data = ''

        def write(self, x):
            self.data

# Generated at 2022-06-14 13:34:37.820977
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .utils import setup_loggers
    from .utils import test_logging_redirect_tqdm as utils_test_logging_redirect_tqdm
    from .utils import _range, A
    from .utils import _test_pre_post_reset_post_finalizer_context_manager

    loggers = setup_loggers(
        'tqdm.contrib.logging.test_logging_redirect_tqdm.loggers')
    # test tqdm.write(msg, file=sys.stderr)
    with tqdm_logging_redirect(
            logger=loggers,
            tqdm_class=A,
            file=sys.stderr,
    ) as pbar:
        pbar.updates = []
        utils_test_logging_red

# Generated at 2022-06-14 13:34:43.990708
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from io import StringIO
    import logging
    import sys

    stdout = sys.stdout
    sys.stdout = StringIO()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = _TqdmLoggingHandler()
    handler.emit('Hello World')

    # Assert if write method is called
    sys.stdout.seek(0)  # For reading from the beginning of the StringIO object
    assert sys.stdout.read() == 'Hello World\n'

    sys.stdout = stdout

# Generated at 2022-06-14 13:34:46.294562
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        logging.info("console logging redirected to `tqdm.write()`")
    # logging restored
    logging.info("console logging restored")


# Generated at 2022-06-14 13:34:56.356129
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        import logging
        from tqdm import trange
    except ImportError:
        return True
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)
    # loggers = [LOG, logging.getLogger()]

    logging.basicConfig(level=logging.INFO)

    with logging_redirect_tqdm() as pbar:
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    for i in trange(9):
        if i == 4:
            LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:35:02.275570
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    logging.basicConfig(level=logging.INFO)

    with tqdm_logging_redirect(tqdm_class=tqdm):
        for i in tqdm(range(9)):
            if i == 4:
                logging.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:35:11.345090
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import tqdm
    import logging


# Generated at 2022-06-14 13:35:20.395205
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    # stdout
    with logging_redirect_tqdm():
        LOG.info('first')
        LOG.info('second')

    # stdout, stderr
    with logging_redirect_tqdm():
        LOG.info('third')
        LOG.error('fourth')

    # stdout, stderr, file
    with logging_redirect_tqdm():
        LOG.info('fifth')
        LOG.error('sixth')
        LOG.info('seventh')
        LOG.critical('eighth')

# Generated at 2022-06-14 13:35:27.467235
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm.contrib.logging import logging_redirect_tqdm
    with logging_redirect_tqdm([logging.getLogger()]):
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")
        logging.info("logging_redirect_tqdm")



# Generated at 2022-06-14 13:35:33.142826
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


# Generated at 2022-06-14 13:35:43.510066
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        # Python 2
        import cStringIO as io
    except ImportError:
        # Python 3
        import io
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        # Redirect output to a buffer
        output = io.StringIO()
        with trange(9, file=output) as t:
            with logging_redirect_tqdm(tqdm_class=t.__class__):
                for i in t:
                    if i == 4:
                        LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
        assert output.getvalue().count('console logging redirected') == 1
        assert output

# Generated at 2022-06-14 13:37:10.662782
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm
    try:
        from unittest.mock import Mock, patch
    except ImportError:
        from mock import Mock, patch
    LOG = logging.getLogger('test')
    logging.basicConfig(level=logging.INFO)  # for `logging.getLogger('test')`
    mock_stdout = Mock()
    with patch('sys.stdout', mock_stdout):
        with logging_redirect_tqdm():
            for _ in trange(5):
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:37:18.566005
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    with tqdm_logging_redirect(total=10) as pbar:
        logger = logging.getLogger()
        assert len(logger.handlers) == 1
        assert isinstance(logger.handlers[0], _TqdmLoggingHandler)
        pbar.update(1)
        logger.info('test')
        pbar.update(1)
    assert len(logger.handlers) == 0

if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:37:26.095459
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    LOG.handlers = []
    LOG.disabled = False
    LOG.propagate = True

    with tqdm_logging_redirect(total=5, disable=True):
        for i in trange(5):
            LOG.info("this is info msg [%d]:", i)
            LOG.error("this is error msg [%d]:", i)
            LOG.warning("this is warning msg [%d]:", i)
            LOG.critical("this is critical msg [%d]:", i)



# Generated at 2022-06-14 13:37:30.892668
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)
    # LOG.setLevel(logging.DEBUG)
    LOG.addHandler(logging.StreamHandler())

    LOG.info('Original logging output')
    try:
        with logging_redirect_tqdm():
            LOG.info('Output redirected to `tqdm.write()`')
            raise RuntimeError('Intentional Error')
    except RuntimeError:
        pass

    LOG.info('Original logging output')


if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:37:38.058523
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from pytest import raises
    import logging

    with tqdm_logging_redirect() as pbar:
        assert isinstance(pbar, std_tqdm)
        try:
            print("Test")  # Should not print
        except AttributeError:
            pass
        else:
            raise ValueError("Test failed!")

        logger = logging.getLogger(__name__)
        logger.info("Test")


if __name__ == "__main__":
    test_tqdm_logging_redirect()