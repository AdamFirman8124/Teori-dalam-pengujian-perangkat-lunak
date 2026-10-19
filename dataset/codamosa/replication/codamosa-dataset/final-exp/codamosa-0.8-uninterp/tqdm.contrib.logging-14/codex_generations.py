

# Generated at 2022-06-14 13:27:57.590377
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .miscs import _range
    import logging

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.info("console logging redirected to `tqdm.write()`")

    # with logging_redirect_tqdm() as logger:

# Generated at 2022-06-14 13:28:07.135306
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import logging
    import sys
    import os

    # open temp file
    fd, fname = tempfile.mkstemp()

    # with _TqdmLoggingHandler
    handler = _TqdmLoggingHandler()
    # set stream to temp file
    handler.stream = _open_file_stream(fname)
    # get file descriptor of tempfile
    fd = _get_file_descriptor_from_stream(handler.stream)
    # get logger object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    # create log record
    record = logging.makeLogRecord(
        {'levelno': logging.INFO, 'msg': 'test'})   # noqa
    # write record to temp file
    handler.emit

# Generated at 2022-06-14 13:28:14.772892
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None

    import io
    stream = io.StringIO()
    logger = logging.getLogger()
    logger.handlers = []
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # without context
    logger.info('x')
    assert stream.getvalue() == 'x\n'
    stream.truncate(0)  # reset stream
    assert stream.getvalue() == ''

    # with context, but not tqdm
    with logging_redirect_tqdm():
        logger.info('x')
    assert stream.getvalue() == 'x\n'
    stream.trunc

# Generated at 2022-06-14 13:28:24.506560
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    from tqdm import tqdm
    import logging
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    assert logging.getLogger().handlers == []
    dummy_output = StringIO()
    original_stream = sys.stderr
    sys.stderr = dummy_output

# Generated at 2022-06-14 13:28:28.078410
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with tqdm_logging_redirect(total=3) as pbar:
        for _ in range(3):
            pbar.update()


# Compatibility with python2 logging module that doesn't have effectiveLevel

# Generated at 2022-06-14 13:28:37.217152
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # Simple unit test for tqdm_logging_redirect
    import tqdm
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    with tqdm_logging_redirect(
        total=100,
        desc="Logged progress",
        logger=logger
    ) as pbar:
        for _ in range(100):
            logger.info("this is a test")
            pbar.update(1)
    print(pbar)
    assert pbar.n == 100
    assert pbar.total == 100

if __name__ == "__main__":
    # test_tqdm_logging_redirect()
    pass

# Generated at 2022-06-14 13:28:42.549874
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(
            loggers=[LOG],
            total=5
    ) as pbar:
        for i in range(5):
            time.sleep(1)
            pbar.update()
            LOG.info("logged to tqdm")

# Generated at 2022-06-14 13:28:50.008251
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # Create a console handler for loggers
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))
    # Create root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(ch)
    root_logger.info('before logging redirect')
    with logging_redirect_tqdm():
        root_logger.info('during logging redirect')
    root_logger.info('after logging redirect')



# Generated at 2022-06-14 13:28:57.194939
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    class TqdmLoggingHandler(_TqdmLoggingHandler):
        def __init__(self):
            super(TqdmLoggingHandler, self).__init__(tqdm_class=TqdmClass)
            self.stream = FakeStream()

    class FakeStream(object):
        def write(self, str):
            return

    class TqdmClass(object):
        def write(self, str):
            return

    handler = TqdmLoggingHandler()
    msg = 'test'
    record = logging.LogRecord(
        name='name', level=logging.INFO, pathname='path', lineno=0,
        msg=msg, args=None, exc_info=None)

    handler.emit(record)
    assert handler.stream.str == msg + '\n'

# Generated at 2022-06-14 13:29:01.059654
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        import logging
        from tqdm import trange
        log = logging.getLogger(__name__)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    log.info("console logging redirected to `tqdm.write()`")
    except ImportError:
        pass

# Generated at 2022-06-14 13:29:14.341400
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)
    with logging_redirect_tqdm():
        LOG.info("This is a test")

# Generated at 2022-06-14 13:29:19.394204
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)
    with tqdm_logging_redirect(loggers=[LOG, logging.root]) as pbar:
        test_list = [1,2,3,4,5]
        for i in pbar(test_list):
            if i == 2:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:29:23.791913
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(desc="test_tqdm_logging_redirect", logger="test") as pbar:
        logging.getLogger('test').info('hello')
    pbar.close()

# Generated at 2022-06-14 13:29:28.268280
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm.
    """
    logging.basicConfig(level=logging.INFO)

    from tqdm.contrib.logging import logging_redirect_tqdm
    with logging_redirect_tqdm():
        logging.info('this is a test message')

    import tqdm
    tqdm.tqdm.write('this is a test message')



# Generated at 2022-06-14 13:29:36.003628
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Unit test for function tqdm_logging_redirect.
    """
    import logging
    import tqdm
    with tqdm_logging_redirect(loggers=[logging.root], tqdm_class=tqdm,
                               total=10):
        for i in range(10):
            if i == 4:
                logging.info('console logging redirected to `tqdm.write()`')

# Generated at 2022-06-14 13:29:41.745416
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    try:
        from unittest import mock
    except ImportError:  # pragma: no cover
        import mock
    with mock.patch('tqdm.std.tqdm.write') as mwrite:
        with logging_redirect_tqdm(loggers=[logging.getLogger('example')]):
            logging.getLogger('example').warning('test')
        assert mwrite.call_args[0][0] == 'test\n'

# Generated at 2022-06-14 13:29:46.324336
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logging.basicConfig(level=logging.INFO)
    for logger in [logging.root, logging.getLogger(__name__)]:
        with logging_redirect_tqdm():
            for _ in std_tqdm(range(9)):
                logger.info('Test message')



# Generated at 2022-06-14 13:29:57.437419
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    try:
        from unittest import mock
    except ImportError:
        import mock
    from .helper import TestCase
    from .wrappers import _tqdm

    with TestCase(tqdm_class=_tqdm, desc='test_tqdm_logging_redirect'):
        tqdm_kwargs = {'miniters': 0, 'mininterval': 0, 'ascii': True, 'disable': False}
        with mock.patch('logging.handlers.MemoryHandler.emit') as mock_emit:
            with tqdm_logging_redirect('test_logging_redirect', **tqdm_kwargs):
                logger = logging.getLogger()
                logger.info('hello')
                logger.error('world')

# Generated at 2022-06-14 13:30:04.186708
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for _ in trange(9):
                if _ == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored



# Generated at 2022-06-14 13:30:11.407545
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    import unittest
    import io
    import sys
    from tqdm.contrib import logging as logging_contrib

    orig_stdout = sys.stdout

# Generated at 2022-06-14 13:30:37.880041
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    message = "console logging redirected to `tqdm.write()`"

    logging.basicConfig(level=logging.INFO)
    try:
        with tqdm_logging_redirect() as pbar:
            assert pbar.__class__.__name__ == "tqdm"
            assert len(pbar) == 0
            LOG = logging.getLogger(__name__)
            LOG.info(message)
            pbar.update()
            assert len(pbar) == 1
            assert pbar.format_dict["desc"] == message
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:30:45.230850
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    loggers = [logging.root]
    original_handlers_list = [logger.handlers for logger in loggers]
    for logger in loggers:
        tqdm_handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
        orig_handler = _get_first_found_console_logging_handler(logger.handlers)
        orig_handler.setFormatter(orig_handler.formatter)
        orig_handler.stream = orig_handler.stream
        logger.handlers = [
            handler for handler in logger.handlers
            if not _is_console_logging_handler(handler)] + [tqdm_handler]
    for logger, original_handlers in zip(loggers, original_handlers_list):
        logger.handlers = original_handlers


# Generated at 2022-06-14 13:30:55.247951
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import StringIO
    import logging
    # import pdb; pdb.set_trace()
    output_file = StringIO.StringIO()
    logging.basicConfig(level=logging.DEBUG, stream=output_file)
    logger = logging.getLogger(__name__)
    with tqdm_logging_redirect(desc='test', ascii=True, total=2) as pbar:
        pbar.write("hello from tqdm")
        logger.info("hello from logging")
    output = output_file.getvalue()
    assert output == "test:   1%|                                                  | 1/2 [00:00<?, ?it/s]hello from logging\n"


# Module functions
write = std_tqdm.write
monitor_interval = std_tqdm.monitor_inter

# Generated at 2022-06-14 13:30:58.574181
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    LOG = logging.getLogger('logging_redirect_tqdm')
    with logging_redirect_tqdm():
        for i in range(9):
            if i == 4:
                LOG.info(u'hello world!')


if __name__ == "__main__":
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:31:07.185914
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm.utils import _term_move_up

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    def _test_logging_redirect_tqdm(with_format=False, err=False):
        if with_format:
            try:
                with logging_redirect_tqdm(tqdm_class=std_tqdm):
                    raise Exception()
            except Exception:
                logger.exception('test', exc_info=not err)
        else:
            logger.debug('test')
            try:
                with logging_redirect_tqdm(tqdm_class=std_tqdm):
                    raise Exception()
            except Exception:
                logger.exception(exc_info=not err)

    # print('Test logging_

# Generated at 2022-06-14 13:31:16.787245
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    def dummy_tqdm(file, **kwargs):
        # type: (str, **str) -> None
        open(file, 'a').write("Start\n")
        open(file, 'a').write("Finish\n")

    with tqdm_logging_redirect(tqdm_class=dummy_tqdm, loggers=[logging.getLogger(__name__)]) as p:
        logging.info("Test")

    with open("tqdm_logging_redirect_test.log", "r") as f:
        assert f.read() == "Start\nFinish\n"

# Generated at 2022-06-14 13:31:27.388952
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from tqdm import std_tqdm
    from io import StringIO as _StringIO
    from io import BytesIO as _BytesIO

    _tee = _BytesIO if sys.version_info[0] == 2 else _StringIO

    for io_ in (sys.stdout, sys.stderr, _tee()):
        std_tqdm.write("hello stdout")
        std_tqdm.write("hello stdout", file=io_)
        std_tqdm.write("hello stdout", file=_tee())

        log = logging.getLogger(__name__)
        log.handlers = []
        log.setLevel(logging.DEBUG)
        handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
        handler.stream = io

# Generated at 2022-06-14 13:31:30.390620
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    loggers = [logging.getLogger(__name__)]
    with logging_redirect_tqdm(loggers):
        for i in range(3):
            logging.info('hello')


# Generated at 2022-06-14 13:31:34.814491
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm import trange
    import logging

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:31:46.123247
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    log = logging.getLogger(__name__)
    log.handlers = []
    log.setLevel(logging.INFO)
    log.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    log.addHandler(stream_handler)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                log.info('console logging redirected to `tqdm.write()`')


# Generated at 2022-06-14 13:32:28.274313
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:32:35.306952
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    import logging
    # import tqdm
    # from tqdm.contrib.logging import tqdm_logging_redirect
    with tqdm_logging_redirect(loggers=[logging.root]):
        logging.info("This is a test")
    assert True


del absolute_import, contextmanager, isinstance, logging, sys, optional

# Generated at 2022-06-14 13:32:44.652778
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    LOG = logging.getLogger(__name__)

    # Logging to console
    orig_handlers = logging.root.handlers.copy()

# Generated at 2022-06-14 13:32:53.924642
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import tqdm

    with tqdm_logging_redirect(desc='test_tqdm_logging_redirect',
                               total=1, unit='i',
                               leave=True) as pbar:
        assert pbar is not None
    # Also test loggers ..
    with tqdm.trange(2) as pbar:
        with tqdm_logging_redirect(loggers=[logging.getLogger(__name__)],
                                   tqdm_class=pbar.__class__, # type: ignore
                                   desc='test_tqdm_logging_redirect',
                                   total=1, unit='i',
                                   leave=True) as pbar:
            assert pbar is not None

# Generated at 2022-06-14 13:33:03.143511
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.INFO)

    # Test tqdm_logging_redirect
    with tqdm_logging_redirect(total=9) as pbar1:
        for i in pbar1:
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

    # Restore logging
    LOG.setLevel(logging.NOTSET)


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:11.850148
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm
    from tqdm._utils import _term_move_up

    logger = logging.getLogger(__name__)
    test_string = "console logging redirected to `tqdm.write()`"

    def test(logger, string, tqdm_class=tqdm):
        """Simple console logging redirection test."""
        with logging_redirect_tqdm([logger], tqdm_class):
            for i in tqdm(range(50)):
                if i == 4:
                    logger.info(string)
        logging.info('=' * len(string))

    test(logger, test_string)
    test(logging.root, test_string)

    # test `_TqdmLoggingHandler.emit()` exception catching


# Generated at 2022-06-14 13:33:20.224154
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    def assert_logs(count, tqdm_class=tqdm):
        assert tqdm_class.write.call_count == count

    class FakeProgressBar(tqdm):
        def __init__(self):
            self.call_count = 0

        def update(self, n):
            self.call_count += n

    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    with tqdm_logging_redirect(level=logging.INFO,
                               tqdm_class=FakeProgressBar) as pbar:
        assert isinstance(pbar, FakeProgressBar)

# Generated at 2022-06-14 13:33:26.556734
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    def do_work():
        LOG.info("Redirected!")

    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        for _ in trange(9):
            do_work()



# Generated at 2022-06-14 13:33:31.703238
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import io

    out = io.StringIO("")
    logging.basicConfig(level=logging.INFO, stream=out)
    with tqdm_logging_redirect():
        logging.info("test")
    assert out.getvalue().strip() == "test"
    out.close()


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:33:36.268982
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    try:
        with tqdm_logging_redirect():
            for i in trange(3):
                if i == 1:
                    LOG.info("console logging redirected to `tqdm.write()`")
    except (StopIteration, RuntimeError):
        pass

# Generated at 2022-06-14 13:34:19.252823
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: () -> None
    tqdm_class = std_tqdm
    # prepare the `tqdm` object
    tqdm_obj = tqdm_class()

    tqdm_obj.write = lambda s: None
    tqdm_obj.flush = lambda: None

    # prepare the `logging.StreamHandler` object
    logging_handler_obj = _TqdmLoggingHandler(tqdm_class)

    logging_handler_obj.tqdm_class = tqdm_class
    logging_handler_obj.stream = tqdm_obj

    # prepare the `logging.LogRecord` object

# Generated at 2022-06-14 13:34:24.721735
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    with tqdm_logging_redirect(desc='test', total=9,
                               loggers=[logging.getLogger(__name__)]) as pbar:
        for i in range(9):
            if i == 4:
                logging.getLogger(__name__).info("console logging redirected to `tqdm.write()`")


if __name__ == "__main__":
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:34:31.020235
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # type: () -> None

    def test_emit(test_stream, test_logger):
        # type: (IO[str], logging.Logger) -> None
        """ Test method emit of class _TqdmLoggingHandler.
        """
        test_tqdm = test_stream.write
        test_tqdm_flush = test_stream.flush
        test_handler = _TqdmLoggingHandler(tqdm_class=test_tqdm)
        test_handler.stream = test_stream
        test_handler_format = test_handler.format
        test_record = logging.LogRecord(
            name='mylogger', level=logging.INFO, pathname='None', lineno=1,
            msg='myLogRecord', args=None, exc_info=None)
        test_handler_em

# Generated at 2022-06-14 13:34:39.029173
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange, tnrange

    log = logging.getLogger(__name__)

    for logger in [logging.root, log]:
        with logging_redirect_tqdm([logger]):
            for i in trange(6):
                if i == 4:
                    log.info("console logging redirected to `tqdm.write()`")
        for i in tnrange(0, 6):
            if i == 4:
                log.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:34:46.184358
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    r"""Test that the logging_redirect_tqdm() function works correctly."""
    # Tests are located in the logging_redirect_tqdm function
    # because the function's context manager temporarily modifies
    # logging.root.handlers and this would interfere with the
    # tests of the unit tests if they were in separate functions.

    # TODO : use a different logger than logging.root for tests
    import os
    import tempfile
    import logging
    from contextlib import redirect_stdout
    from io import StringIO

    # script set-up
    LogPath = tempfile.mkstemp("log")[1]
    logger = logging.getLogger("")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(LogPath)
    logger.addHandler(file_handler)
   

# Generated at 2022-06-14 13:34:48.430435
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm():
        LOG.info("test")

# Generated at 2022-06-14 13:34:55.536761
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging, time
    from tqdm import trange

    logger = logging.getLogger(__name__)
    with tqdm_logging_redirect(loggers=[logger],
                               total=100, mininterval=0.01, miniters=1) as pbar:
        for k in range(10):
            logger.warning('hello {}'.format(k))
            time.sleep(0.1)
            pbar.update(10)
    assert 10 == len(pbar)



# Generated at 2022-06-14 13:35:05.184510
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect() as pbar1:
            for i in pbar1(range(10)):
                if i == 5:
                    LOG.info("console logging redirected to pbar1")

        LOG = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

# Generated at 2022-06-14 13:35:11.436673
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    import re
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

# Generated at 2022-06-14 13:35:17.696537
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Unit test for function tqdm_logging_redirect()
    """
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    with tqdm_logging_redirect():
        logger.info('logging message')
    logger.info('logging message again')



# Generated at 2022-06-14 13:36:40.534745
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # Get a logger
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect(total=1, desc="Logging redirected to tqdm.write()") as pbar:
        # Test is we get all the log messages
        LOG.info("This should not be visible")
        LOG.info("This should be visible")
        # Test if we can still use the tqdm object
        for _ in range(4):
            pbar.update()
        # Test if logging is turned off after context
        LOG.info("This should still not be visible")

if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:36:49.378748
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from unittest import mock
    except ImportError:
        import mock
    import logging
    from tqdm import trange

    def _test_loggers(loggers):
        for logger in loggers:
            assert all([not _is_console_logging_handler(han)
                        for han in logger.handlers])

    with mock.patch('tqdm.contrib.logging.std_tqdm.write') as mock_write:
        with logging_redirect_tqdm():
            _test_loggers([logging.root])
            trange(3)

# Generated at 2022-06-14 13:36:56.735893
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
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

# Generated at 2022-06-14 13:37:03.656002
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Unit test for function logging_redirect_tqdm"""
    from . import _utils
    log = logging.getLogger(__name__)  # pylint: disable=locally-disabled, invalid-name
    with logging_redirect_tqdm():
        for i in _utils.trange(9):
            if i == 4:
                log.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2022-06-14 13:37:11.965476
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """Test case for function logging_redirect_tqdm"""
    from .utils import closing, suppress_tqdm_output

    # We add a null handler to root logger to prevent logging message
    # "No handlers could be found for logger" message
    logging.root.addHandler(logging.NullHandler())

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    with suppress_tqdm_output():
        log.info("hello")

    with closing(std_tqdm(total=1, leave=False)) as t:
        with logging_redirect_tqdm():
            pbar = tqdm_logging_redirect(loggers=[log], total=1, leave=False)
            log.info("tqdm.write: hello")

# Generated at 2022-06-14 13:37:21.747460
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    logging.basicConfig()  # default level is WARNING
    with tqdm_logging_redirect() as pbar:
        logging.info("test logging")
        logging.warning("test logging")
        # assert that nothing is logged to console (pbar):
    assert pbar.last_print_n == 0
    assert pbar.total == 0

    with tqdm_logging_redirect() as pbar:
        logging.getLogger('__main__').setLevel(logging.INFO)
        logging.info("test logging")
        logging.warning("test logging")
        # assert that only INFO is logged to console (pbar):
    assert pbar.last_print_n == 1
    assert pbar.total == 1


# Generated at 2022-06-14 13:37:29.078093
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    try:
        import tqdm
    except ImportError:
        return

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
    logger.addHandler(stream_handler)


# Generated at 2022-06-14 13:37:39.810990
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import time
    import logging
    from tqdm.contrib import logging_redirect_tqdm
    tqdm_class = std_tqdm
    try:
        with tqdm_logging_redirect(total=10, bar_format="{desc}") as pbar:
            for i in range(10):
                pbar.set_description("tqdm_{}".format(i))
                time.sleep(0.1)
        with logging_redirect_tqdm(tqdm_class=tqdm_class):
            log_ = logging.getLogger(__name__)
            for i in range(10):
                log_.info("tqdm_{}".format(i))
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:37:46.449323
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in tqdm(range(10)):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored

