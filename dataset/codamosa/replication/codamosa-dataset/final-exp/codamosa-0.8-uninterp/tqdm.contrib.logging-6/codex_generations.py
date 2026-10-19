

# Generated at 2022-06-14 13:27:57.634926
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(total=9, loggers=[LOG]):
            for i in range(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:04.382138
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  # pragma: no cover
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info('console logging redirected to `tqdm.write()`')
        # logging restored

# Generated at 2022-06-14 13:28:09.125763
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    import time
    import logging
    from tqdm import trange
    log = logging.getLogger()
    try:
        with logging_redirect_tqdm():
            for i in trange(9):
                time.sleep(0.1)
                if i == 4:
                    log.warning("console logging redirected to `tqdm.write()`")
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:28:15.873323
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from tqdm._utils import _term_move_up
    from .test_redirect_std_streams import memory_stream

    stream = memory_stream()
    logger = logging.getLogger()

    # Print "...", but don't overwrite the next line
    std_tqdm.write('...')
    print('\r', file=stream)

    with logging_redirect_tqdm(loggers=[logger], tqdm_class=std_tqdm):
        # Should NOT overwrite the next line
        logger.warning('...')
        print('\r', file=stream)

        # Should overwrite the "..."
        logger.warning('.')
        print('\r', file=stream)
        # Should NOT overwrite the "..."
        std_tqdm.write('.')

# Generated at 2022-06-14 13:28:20.871503
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():
    """
    Test _TqdmLoggingHandler writer function.
    """
    import logging
    import sys

    class _TqdmLoggingHandler(logging.StreamHandler):
        def __init__(
            self,
            tqdm_class=std_tqdm  # type: Type[std_tqdm]
        ):
            super(_TqdmLoggingHandler, self).__init__()
            self.tqdm_class = tqdm_class

        def emit(self, record):
            try:
                msg = self.format(record)
                self.tqdm_class.write(msg, file=self.stream)
                self.flush()
            except (KeyboardInterrupt, SystemExit):
                raise

# Generated at 2022-06-14 13:28:25.842923
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Tests for function logging_redirect_tqdm.
    """
    import logging

    log = logging.getLogger(__name__)
    log.info("hey")
    with logging_redirect_tqdm():
        log.info("hey")



# Generated at 2022-06-14 13:28:36.084888
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import os
    import inspect
    import logging
    filename = inspect.getfile(inspect.currentframe())
    dirpath = os.path.dirname(os.path.abspath(filename))
    logfile = os.path.join(dirpath, 'test_tqdm_logging_redirect.txt')
    if os.path.exists(logfile):
        os.remove(logfile)
    logging.basicConfig(filename=logfile, level=logging.INFO)

# Generated at 2022-06-14 13:28:43.315637
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from .tests import tests
    import logging

    # Get the stdout from the console
    console_stdout = sys.stdout

    # Change sys.stdout to a temporary stringIO object
    sys.stdout = tests.get_temp_stringIO()

    # Get the example module
    example_module = tests.get_example_module()

    # Add logging to the example module
    example_module.tqdm_example_add_logging()

    # Import the example module
    example = tests.import_module(example_module.__file__)

    # Get the stdout from the logger
    logger_stdout = sys.stdout

    # Redirect logging to tqdm
    with tqdm_logging_redirect(total=10, loggers=[logging.root]):

        # Run the example
        example

# Generated at 2022-06-14 13:28:50.485754
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    try:
        from .test_tqdm import pretest_posttest  # NOQA
    except ImportError:
        return
    log = logging.getLogger(__name__)
    log_level = logging.INFO
    logging.basicConfig(level=log_level)
    with pretest_posttest():
        with logging_redirect_tqdm():
            for i in std_tqdm(range(9), desc="bar", ncols=90):
                if i == 4:
                    log.info("console logging redirected to `tqdm.write()`")

# Generated at 2022-06-14 13:28:55.472907
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .deprecation import _tqdm_deprecated
    handler_list = []
    _tqdm_deprecated(handler_list)
    logging.basicConfig(level=logging.INFO)
    with logging_redirect_tqdm():
        logging.info('test')
        assert handler_list == [
            'tqdm_contrib.tqdm_deprecated.logging_redirect_tqdm is deprecated '
            '(use tqdm.contrib.logging instead)']

# Generated at 2022-06-14 13:29:09.567630
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from .tst import tst
    from . import __version__
    import logging

    with tst():
        logging.info("root")
        test_handler = logging.StreamHandler()
        test_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logging.root.addHandler(test_handler)
        with logging_redirect_tqdm():
            logging.info("tqdm write")
            logging.info("tqdm write")

# Generated at 2022-06-14 13:29:17.987218
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import sys
    import os

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    tqdm_logging_redirect(
        pbar_kwargs={'file': sys.stdout},
        tqdm_class=std_tqdm,
        loggers=[LOG],
    )
    LOG.info("console logging redirected to `tqdm.write()`")
    tqdm_logging_redirect(
        pbar_kwargs={'file': sys.stderr},
        tqdm_class=std_tqdm,
        loggers=[LOG],
    )
    LOG.info("console logging redirected to `tqdm.write()`")



# Generated at 2022-06-14 13:29:27.959294
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    tqdm.contrib.logging - Redirect logging to tqdm

    Make sure logging messages are displayed on the tqdm progress bar
    """
    from tqdm import tqdm
    import logging
    import time

    LOG = logging.getLogger(__name__)
    with logging_redirect_tqdm():
        pbar = tqdm(total=10)
        try:
            for _ in range(10):
                pbar.update()
                LOG.info("console logging redirected to `tqdm.write()`")
                time.sleep(0.05)
        except KeyboardInterrupt:
            raise SystemExit("aborted")
        except:  # noqa pylint: disable=bare-except
            LOG.error("An error happened!")
            time.sleep(0.05)

# Generated at 2022-06-14 13:29:39.944323
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    from ..std import tqdm
    from ..utils import SafeRegex
    from .tests import pretest_posttest, _range

    pretest_posttest()

    with logging_redirect_tqdm():
        for i in _range(3):
            logging.critical('critical')
            logging.error('error')
            logging.warning('warning')
            logging.info('info')
            logging.debug('debug')

    print('')
    with tqdm_logging_redirect():
        for i in _range(3):
            logging.warning('warning')
            logging.info('info')
            logging.debug('debug')

    print('')

# Generated at 2022-06-14 13:29:46.126979
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging
    import time

    logging.basicConfig(level=logging.INFO)

    tqdm_logging_redirect(total=5, leave=False, disable=False,
                          loggers=[logging.getLogger(__name__)])
    LOG = logging.getLogger(__name__)
    LOG.info("hello")
    LOG.info("world")
    for i in range(5):
        time.sleep(0.1)



# Generated at 2022-06-14 13:29:57.318482
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    import logging

    # Default
    with tqdm_logging_redirect() as pbar:
        assert(pbar == std_tqdm.tqdm(disable=std_tqdm.DISABLE))

    # Change tqdm_class
    with tqdm_logging_redirect(tqdm_class=std_tqdm.tqdm_gui) as pbar:
        assert(pbar == std_tqdm.tqdm_gui(disable=std_tqdm.DISABLE))

    # Change loggers
    with tqdm_logging_redirect(loggers=[logging.getLogger('test')]) as pbar:
        assert(pbar == std_tqdm.tqdm(disable=std_tqdm.DISABLE))

    # Change loggers, tq

# Generated at 2022-06-14 13:29:59.443969
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():
    from tqdm.contrib import test
    test.test_tqdm_logging_redirect(tqdm_logging_redirect)

# Generated at 2022-06-14 13:30:03.557024
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    logger = logging.getLogger(__name__)
    logger.info("logging before redirect")
    with logging_redirect_tqdm():
        logger.info("logging after redirect")
        logger.info("this should appear in tqdm")
    logger.info("logging after restore")



# Generated at 2022-06-14 13:30:09.861197
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():
    """
    Example with logging_redirect_tqdm:
    """
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



# Generated at 2022-06-14 13:30:15.296880
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

