

# Generated at 2022-06-14 13:28:00.222225
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    loggers = None  # type: Optional[List[logging.Logger]]
    logging.basicConfig(level=logging.INFO)  # pylint: disable=no-member
    LOG = logging.getLogger(__name__)  # pylint: disable=invalid-name
    with tqdm_logging_redirect() as pbar:
        pbar.update(1)
        LOG.warning('test warning')
        LOG.error('test error')
        pbar.update(1)



# Generated at 2022-06-14 13:28:04.847487
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    with tqdm_logging_redirect() as pbar:
        for i in range(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
            pbar.update(1)
    pass

# Generated at 2022-06-14 13:28:12.188009
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import logging
    import sys
    import traceback
    try:
        from StringIO import StringIO  # Python 2
    except ImportError:
        from io import StringIO  # Python 3

    # set up a message logger
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # set up a progress bar
    pbar_stream = io.StringIO()
    pbar_handler = _TqdmLoggingHandler()
    pbar_logger = logging.getLogger()
    pbar_logger.addHandler(pbar_handler)
    pbar_logger.setLevel(logging.INFO)
    # make sure that stream is None and will be

# Generated at 2022-06-14 13:28:19.129453
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    try:
        # noinspection PyUnresolvedReferences
        from tqdm import tqdm
        from tqdm.contrib import logging_redirect
    except ImportError:
        return

    with tqdm_logging_redirect() as pbar:
        pbar.update(1)


if __name__ == '__main__':
    test_tqdm_logging_redirect()

# Generated at 2022-06-14 13:28:26.663228
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Unit test for function logging_redirect_tqdm
    """
    try:
        import unittest
    except ImportError:
        return
    try:
        from unittest.mock import patch  # type: ignore
    except ImportError:
        from mock import patch  # type: ignore
    from .utils import TqdmHandlerTest

    class TestTqdmLoggingHandler(TqdmHandlerTest):
        """
        Unit tests for TqdmLoggingHandler
        """
        @unittest.skipIf(sys.version_info < (3, 2),
                         "assertWarns not available below Python 3.2")
        def test_write(self):
            """
            Unit test for function write
            """

# Generated at 2022-06-14 13:28:36.787136
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """Unit test for function tqdm_logging_redirect"""
    from . import tqdm
    from .std import tqdm as std_tqdm

    def _unit_test(tqdm_class, tqdm_kwargs):
        log_level = logging.INFO
        log_format = "%(name)s|%(levelname)s>  %(message)s"
        # set up logger
        logger = logging.getLogger('test.tqdm_logging_redirect')
        logger.setLevel(log_level)
        logger_handler = logging.StreamHandler()
        logger_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(logger_handler)
        # check the first line of output

# Generated at 2022-06-14 13:28:43.683585
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tqdm_std import tqdm
    from .tqdm_std import tnrange

    with tqdm_logging_redirect(
        loggers=[logging.root],
        desc='redirected to tqdm',
        total=10,
        file=sys.stdout
    ) as pbar:
        for i in tqdm(range(10)):
            if i == 5:
                logging.info('Logging to stdout redirected to tqdm')
            if i == 8:
                pbar.write('Just write something to pbar')
            if i == 9:
                with tnrange(1, desc='A tnrange') as pbar2:
                    pbar2.write('A write on pbar2')

# Generated at 2022-06-14 13:28:53.178184
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm  # pylint:disable=import-outside-toplevel
    from .utils import closing, dev_null

    @closing(dev_null(), 'w')
    def _unit_test_logging_redirect_tqdm(
        loggers=None,  # type: Optional[List[logging.Logger]]
        tqdm_class=tqdm  # type: Type[tqdm]
    ):
        # type: (...) -> Iterator[None]
        """
        Context manager redirecting console logging to `tqdm.write()`, leaving
        other logging handlers (e.g. log files) unaffected.
        """
        if loggers is None:
            loggers = [logging.root]

# Generated at 2022-06-14 13:29:01.412997
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import tempfile
    from io import BytesIO
    from tqdm.contrib.logging import _TqdmLoggingHandler
    import logging
    import re

    old_stderr, old_stdout = sys.stderr, sys.stdout
    sys.stderr = sys.stdout = BytesIO()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)

    std_tqdm = __import__("tqdm")

    # Test 1
    with tempfile.NamedTemporaryFile() as log:
        handler.stream = log
        logger.info("test1")
        log.flush()
        log.seek(0)

# Generated at 2022-06-14 13:29:04.674902
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange
    logger = logging.getLogger(__name__)
    with logging_redirect_tqdm([logger]):
        for i in trange(3):
            logger.info("testing")
    assert True

# Generated at 2022-06-14 13:29:15.572568
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    """
    Test for the `tqdm_logging_redirect' function.
    """
    from ..std import tqdm
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect():
        for i in tqdm(range(9)):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:29:22.609919
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import sys
    import logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger()
    with std_tqdm() as pbar:
        with logging_redirect_tqdm(loggers=[LOG],
                                   tqdm_class=std_tqdm):
            LOG.info("test")
            LOG.info("test")
            LOG.info("test")
            pbar.update(10)
            LOG.info("test")
            LOG.info("test")
    # Check there is no crash with capturing `stdout`/`stderr`
    #   (see https://github.com/tqdm/tqdm/issues/420)
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
   

# Generated at 2022-06-14 13:29:30.428442
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging

    class FauxTqdm(object):

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.write_str = ""

        def write(self, str, file=None):
            self.write_str += str

    loggers = []
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    loggers.append(logger)

    logger2 = logging.getLogger('other')
    logger2.setLevel(logging.INFO)
    loggers.append(logger2)

    with logging_redirect_tqdm(tqdm_class=FauxTqdm) as f:
        logger.info('test')

# Generated at 2022-06-14 13:29:39.261388
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib import logging_redirect_tqdm

    LOG = logging.getLogger('test_tqdm_logging_redirect')

    def test_func(pbar):
        for i in pbar:
            if i == 3:
                LOG.info("console logging redirected to `tqdm.write()`")

    with tqdm_logging_redirect(total=9) as pbar:
        test_func(pbar)

# Generated at 2022-06-14 13:29:49.325394
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from time import sleep
    from tqdm import tqdm
    from tqdm import trange
    from tqdm.contrib.logging import (
        logging_redirect_tqdm,
        tqdm_logging_redirect,
    )
    import logging

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)
    LOG.addHandler(logging.StreamHandler())

    with tqdm_logging_redirect(
            desc="redirected logging"
    ) as pbar:
        for i in trange(3):
            if i == 1:
                LOG.info("console logging redirected to `tqdm.write()`")
                # make sure that the log statement is recorded before
                # tqdm.write()

# Generated at 2022-06-14 13:30:00.194296
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import time
    import logging
    import tempfile
    from io import StringIO

    # Redirect stdout
    sys.stdout = StringIO()

    # Temporarily redirect stdout to a temp file
    old_stdout = sys.stdout
    fd, temp_stdout_file = tempfile.mkstemp()
    sys.stdout = open(temp_stdout_file, 'w')

    # Create a logger
    LOG = logging.getLogger('Logging test')

    # Redirect logger output to stdout
    handler = logging.StreamHandler(sys.stdout)

    # Create a logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Generated at 2022-06-14 13:30:05.179431
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    log = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in trange(9):
                if i == 4:
                    log.info("hello world")
        # logging restored

# Generated at 2022-06-14 13:30:09.635169
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    LOG = logging.getLogger(__name__)
    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)

        with tqdm_logging_redirect():
            for i in range(1):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:30:17.726867
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm import trange
    try:
        from unittest import mock
    except ImportError:
        import mock
    with mock.patch.object(std_tqdm, 'write') as mock_write:
        with tqdm_logging_redirect(total=3, leave=False) as pbar:
            for i in trange(3):
                logging.info('test')
        assert len(mock_write.call_args_list) == 3
        for call_arg in mock_write.call_args_list:
            assert 'test' in call_arg[0][0]
        mock_write.assert_has_calls(
            [mock.call('test\n')] * 3, any_order=False)

# Generated at 2022-06-14 13:30:29.946815
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    # type: () -> None
    from .test_tqdm import pretest_posttest  # noqa pylint: disable=unused-variable
    from .test_tqdm import _range  # noqa pylint: disable=unused-variable

    # fmt: off
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock  # type: ignore
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock  # type: ignore
    # fmt: on

    log_mock = Mock()
    logger = MagicMock()
    logger.handlers = [log_mock]

# Generated at 2022-06-14 13:30:52.438614
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Test the method "emit" of class _TqdmLoggingHandler
    """
    import os
    import tempfile
    import logging

    log_msg = "Test log"
    log_lvl = logging.INFO

    # create a logging handler
    hdlr = _TqdmLoggingHandler()

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    hdlr.setFormatter(formatter)

    # create logger and add the handlers to it
    logger = logging.getLogger('simple_example')
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    # create a temporary file and write the log message to it
    fd,

# Generated at 2022-06-14 13:30:56.049289
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import tqdm
    import logging
    logging.basicConfig(level=logging.DEBUG)
    foo_logger = logging.getLogger('foo')
    bar_logger = logging.getLogger('bar')
    with tqdm_logging_redirect(
        tqdm_class=tqdm.tqdm,
        total=2,
        disable=True,
        unit='',
        desc='wiggle',
        loggers=[foo_logger, bar_logger]
    ) as pbar:
        foo_logger.debug('foo')
        bar_logger.debug('bar')

    # output:
    # # foo_logger.debug('foo')
    # # bar_logger.debug('bar')
    # [00:00<?, ?wiggle/s]DEBUG:foo

# Generated at 2022-06-14 13:31:05.694316
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from ..std import logging
    from .tqdm import tqdm
    from .autonotebook import tqdm as autonotebook_tqdm

    logging.info('FIRST BEFORE')
    with tqdm_logging_redirect(
            tqdm_class=autonotebook_tqdm, total=10) as p:
        logging.info('SECOND BEFORE')
        for i in p:
            logging.info('LOOP {}'.format(i))
    logging.info('FIRST AFTER')
    with tqdm_logging_redirect(tqdm_class=tqdm, total=10) as p:
        logging.info('SECOND AFTER')
        for i in p:
            logging.info('LOOP {}'.format(i))

# Generated at 2022-06-14 13:31:12.127632
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """Unit test for function tqdm_logging_redirect"""
    from tqdm.contrib import logger
    from tqdm.auto import trange

    with tqdm_logging_redirect():
        for _ in trange(9):
            logger.info("test")


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:31:20.796155
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    msg = 'test message!'
    tqdm_emit_stream = StringIO()
    tqdm_class = std_tqdm
    handler = _TqdmLoggingHandler(tqdm_class=tqdm_class)
    handler.stream = tqdm_emit_stream
    handler.emit(msg)
    tqdm_emit_stream.seek(0)
    tqdm_emit_result = tqdm_emit_stream.read()
    assert msg + '\n' == tqdm_emit_result


# Generated at 2022-06-14 13:31:27.391760
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm
    import logging
    import sys
    import subprocess

    # tqdm_logging_redirect test
    with tqdm_logging_redirect(total=1, leave=True) as pbar:
        assert isinstance(pbar, tqdm.tqdm)
    t = tqdm(total=1)
    len_orig = len(t)
    with logging_redirect_tqdm(tqdm_class=tqdm):
        logger = logging.getLogger(__name__)
        logger.info("console logging redirected to `tqdm.write()`")
    assert len(t) == len_orig + 1

# Generated at 2022-06-14 13:31:36.441306
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    Example
    -------
    ```python
    import logging
    from tqdm import trange
    from tqdm.contrib import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
    ```
    """
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)


# Generated at 2022-06-14 13:31:42.986714
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm.contrib.logging import tqdm_logging_redirect
    LOG = logging.getLogger('tqdm')
    LOG.setLevel(logging.INFO)
    LOG.info('info before')
    with tqdm_logging_redirect():
        LOG.info('info within')
    LOG.info('info after')

# Generated at 2022-06-14 13:31:53.934930
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    from tqdm import trange

    loggers = [logging.getLogger(__name__)]

    # Original logging format
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    # Redirect console logging to `tqdm.write()`
    logging.info("DO NOT PRINT ME")
    with logging_redirect_tqdm(loggers=loggers) as lrh:
        logging.info("SHOULD PRINT ME")
        for _ in trange(3, desc="PERFECT"):
            logging.info("DO NOT PRINT ME")
            logging.debug("DO NOT PRINT ME")
        logging.info("SHOULD PRINT ME")
    logging.info("DO NOT PRINT ME")

    assert lrh.tqdm_class is std_t

# Generated at 2022-06-14 13:32:01.087262
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    """
    >>> test_tqdm_logging_redirect()
    >>> print ("test passed")
    """
    from .test_tqdm import pretest
    import logging

    pretest()

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(
                loggers=[LOG],
                total=9,
                desc='tqdm_logging_redirect',
                file=sys.stdout) as pbar:
            for i in pbar:
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

