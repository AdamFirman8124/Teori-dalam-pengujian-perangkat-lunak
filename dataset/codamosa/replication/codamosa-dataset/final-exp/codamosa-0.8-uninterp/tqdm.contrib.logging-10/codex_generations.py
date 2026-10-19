

# Generated at 2022-06-14 13:27:49.050491
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm
    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        for _ in trange(9):
            if _ == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    with logging_redirect_tqdm():
        for _ in trange(9):
            if _ == 4:
                LOG.warning("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:27:58.417338
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    from StringIO import StringIO
    from tqdm import tqdm
    from tqdm.utils import _term_move_up

    tqdm_inst = tqdm(desc='test')
    log_handler = _TqdmLoggingHandler(tqdm_class=tqdm)
    log_handler.stream = StringIO()
    log_handler.stream.isatty = lambda: True
    log_handler.terminal = sys.stdout
    log_handler.formatter = logging.Formatter('%(message)s')
    record = logging.LogRecord("TEST", logging.INFO,
                               "test.py", 0, "message", None, None)
    log_handler.emit(record)
    assert log_handler.stream.getvalue() == 'message\n'

# Generated at 2022-06-14 13:28:07.785567
# Unit test for function tqdm_logging_redirect

# Generated at 2022-06-14 13:28:15.192650
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Method `emit` of class `_TqdmLoggingHandler` must redirect console
    logging to `tqdm.write()` and leave unaffected other logging handlers.
    """
    import os
    import tempfile
    from cStringIO import StringIO

    # save the previous value of logger handlers (if any)
    logger = logging.getLogger(__name__)
    prev_handlers = logger.handlers
    logger.handlers = []

    def _get_stdout_and_restore_handlers():
        """
        For python 2 compatibility
        """
        try:
            return sys.stdout.getvalue()
        finally:
            # restore the previous value of logger handlers
            # (if any)
            logger.handlers = prev_handlers


# Generated at 2022-06-14 13:28:23.345105
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    # Create a logger
    LOGGER = logging.getLogger()

    # Create a handler
    handler = _TqdmLoggingHandler()

    # Set the logger level to debug, so that all messages are processed.
    LOGGER.setLevel(logging.DEBUG)

    # Add the handler to the logger
    LOGGER.addHandler(handler)

    # Log some messages
    LOGGER.debug("debug message")
    LOGGER.info("info message")
    LOGGER.warning("warning message")
    LOGGER.error("error message")
    LOGGER.critical("critical message")

    # Remove the handler
    LOGGER.removeHandler(handler)

# Generated at 2022-06-14 13:28:25.936646
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    handler = _TqdmLoggingHandler()
    # handler.tqdm_class = tqdm
    handler.emit('test')



# Generated at 2022-06-14 13:28:33.332300
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    # type: () -> None
    """
    Test case for @logging_redirect_tqdm.
    """
    import tqdm
    import logging

    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(unit='B', file=sys.stdout):
        for i in range(20):
            if i == 9:
                LOG.info("console logging redirected to `tqdm.write()`")

if __name__ == '__main__':
    test_logging_redirect_tqdm()

# Generated at 2022-06-14 13:28:39.019020
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    import io
    import logging
    from tqdm.contrib.logging import _TqdmLoggingHandler

    stream = io.StringIO()
    handler = _TqdmLoggingHandler()
    handler.stream = stream

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    logger.info("test")
    assert stream.getvalue() == "test\n"


# Generated at 2022-06-14 13:28:42.079788
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    with std_tqdm(total=10) as pbar:
        with logging_redirect_tqdm():
            pbar.update(1)
            logging.info("TEST: yo!")
            pbar.update(1)

# Generated at 2022-06-14 13:28:51.405340
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(total=9, desc='test_tqdm_logging_redirect'):
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
                    time.sleep(0.25)
        # logging restored


if __name__ == '__main__':
    test_tqdm_logging_redirect()