

# Generated at 2022-06-14 06:25:16.625304
# Unit test for function logger_level
def test_logger_level():
    init_level = logging.DEBUG
    logger = get_logger(__name__)
    assert logger.level == init_level

    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
        logger.debug('This will be ignored')
    assert logger.level == init_level

# Generated at 2022-06-14 06:25:21.320471
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test_logger_level')

    with logger_level(log, logging.DEBUG):
        log.debug('Your level is DEBUG!')
        log.info('Your level is DEBUG!')
        log.warning('Your level is DEBUG!')
        log.error('Your level is DEBUG!')
        log.critical('Your level is DEBUG!')

    log.error('Your level is NOT DEBUG!')



# Generated at 2022-06-14 06:25:24.982687
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    try:
        with logger_level(logger, logging.DEBUG):
            logger.debug('debug message')
            logger.info('info message')
    except AttributeError:
        return False
    return True

# Generated at 2022-06-14 06:25:32.070804
# Unit test for function logger_level
def test_logger_level():
    import sys
    import io
    import unittest

    message = "test"

    class LoggerLevelTestCase(unittest.TestCase):
        def test_logger_level_info(self):
            stdout = sys.stdout
            sys.stdout = io.StringIO()
            with logger_level(getLogger(), logging.INFO):
                getLogger().debug(message)
            stdout_str = sys.stdout.getvalue()
            sys.stdout = stdout
            self.assertEqual("", stdout_str)

        def test_logger_level_debug(self):
            stdout = sys.stdout
            sys.stdout = io.StringIO()
            with logger_level(getLogger(), logging.DEBUG):
                getLogger().debug(message)
            stdout_

# Generated at 2022-06-14 06:25:39.812325
# Unit test for function logger_level
def test_logger_level():
    from tests.test_logging import StreamRecorder
    logger = logging.getLogger('test')
    with StreamRecorder() as stream:
        with logger_level(logger, logging.DEBUG):
            logger.debug('debug')
            logger.info('info')
            logger.warn('warn')
            logger.error('error')
    assert stream.lines == ['debug', 'info', 'warn', 'error']

# Generated at 2022-06-14 06:25:47.792840
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")

    assert logger.getEffectiveLevel() == logging.INFO
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")

if __name__ == '__main__':
    configure()
    test_logger_level()

# Generated at 2022-06-14 06:25:57.860575
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class LoggerLevelTest(unittest.TestCase):
        # pylint: disable=R0904
        def test_logger_level(self):
            logger = get_logger()
            self.assertEqual(logger.level, 10)
            with logger_level(logger, logging.DEBUG):
                self.assertEqual(logger.level, 10)
                with logger_level(logger, logging.INFO):
                    self.assertEqual(logger.level, 10)
                self.assertEqual(logger.level, 10)
            self.assertEqual(logger.level, 10)

    unittest.main()



# Generated at 2022-06-14 06:26:07.558780
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')
    with logger_level(logger, logging.INFO):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

# Generated at 2022-06-14 06:26:16.397304
# Unit test for function get_config
def test_get_config():
    cfg = get_config(default=DEFAULT_CONFIG)
    expected = dict(DEFAULT_CONFIG)
    if _PyInfo.PY2:
        # py2 json converted unicode keys to str
        for k in expected:
            if isinstance(k, unicode):
                expected[str(k)] = expected[k]
    assert cfg == expected

    cfg = get_config(
        default=DEFAULT_CONFIG, config='{"version":2}'
    )
    expected = dict(DEFAULT_CONFIG)
    expected['version'] = 2
    if _PyInfo.PY2:
        # py2 json converted unicode keys to str
        for k in expected:
            if isinstance(k, unicode):
                expected[str(k)] = expected[k]

# Generated at 2022-06-14 06:26:25.360568
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        logger.debug('This should be logged.')
    logger.debug('This should NOT be logged.')

# def get_logger(name=None):
#     if not name:
#         name = _namespace_from_calling_context()

#     return logging.getLogger(name)


# def configure_logging(
#         name=None,
#         log_config=None,
#         level=logging.DEBUG,
#         format=None,
#         datefmt='%H:%M:%S',
#         handlers=None,
#     ):
#     """Configure a logger."""
#     if name is None:
#         name =

# Generated at 2022-06-14 06:26:38.846743
# Unit test for function logger_level
def test_logger_level():
    import time

    class MockLogger(object):
        def debug(self, msg):
            self.logged.append(msg)
        def __init__(self):
            self.logged = []
        def setLevel(self, level):
            self.level = level
        def level(self):
            return self.level

    log = MockLogger()
    log.setLevel(logging.WARNING)
    with logger_level(log, logging.INFO):
        log.debug('this should be logged')
    assert log.level == logging.WARNING
    assert log.logged == ['this should be logged']



# Generated at 2022-06-14 06:26:45.912306
# Unit test for function logger_level
def test_logger_level():
    import re
    import sys
    logger = get_logger(__name__)
    try:
        with logger_level(logger, logging.CRITICAL):
            logger.error("test error")
    except Exception as exc:
        print(str(exc))
    else:
        assert False, "Expected exception to be raised"

    logger = get_logger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.error("test error")

# Generated at 2022-06-14 06:26:54.300730
# Unit test for function get_config
def test_get_config():
    config = get_config('{"version": 1}', default=None)
    assert isinstance(config, dict)
    assert config["version"] == 1
    config = get_config('{"version": 1}')
    assert isinstance(config, dict)
    assert config["version"] == 1
    config = get_config(default={'version': 1})
    assert isinstance(config, dict)
    assert config["version"] == 1
    config = get_config('{"version": 1}', 'LOGGING', {'version': 1})
    assert isinstance(config, dict)
    assert config["version"] == 1
    config = get_config('{"version": 1}', 'LOGGING', None)
    assert isinstance(config, dict)
    assert config["version"] == 1

# Generated at 2022-06-14 06:27:05.273949
# Unit test for function logger_level
def test_logger_level():
    log_warning = get_logger(__name__)
    log_debug = get_logger(__name__)
    with logger_level(log_warning, logging.INFO):
        print("logging level =",log_warning.level)
        log_warning.debug("Logging level is DEBUG")
        log_warning.info("Logging level is INFO")
        log_warning.warning("Logging level is WARNING")
        print("logging level =",log_warning.level)
    with logger_level(log_debug, logging.DEBUG):
        print("logging level =",log_debug.level)
        log_debug.debug("Logging level is DEBUG")
        log_debug.info("Logging level is INFO")
        log_debug.warning("Logging level is WARNING")

# Generated at 2022-06-14 06:27:14.634559
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    configure()

    with logger_level(log, logging.DEBUG):
        log.debug('debug1')
        log.debug('debug2')

    with logger_level(log, logging.INFO):
        log.debug('debug3')
        log.info('info')


if __name__ == "__main__":

    log = logging.getLogger(__name__)
    configure()
    log.debug('debug')
    log.info('info')

    test_logger_level()

# Generated at 2022-06-14 06:27:17.592696
# Unit test for function configure
def test_configure():
    configure(DEFAULT_CONFIG)
    assert logging.getLogger(__name__).level == logging.DEBUG


# Generated at 2022-06-14 06:27:27.467685
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test_logger_level')
    original_level = log.level

    def test_level(level):
        with logger_level(log, level):
            assert log.isEnabledFor(level)

    test_level(logging.DEBUG)
    test_level(logging.INFO)
    test_level(logging.WARNING)
    test_level(logging.ERROR)
    test_level(logging.CRITICAL)

    assert original_level == log.level


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:27:34.760648
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.WARNING):
        logger.debug('testing...')
        logger.info('testing...')
        logger.warning('testing...')
        logger.error('testing...')
        logger.critical('testing...')
    logger.debug('testing...')
    logger.info('testing...')
    logger.warning('testing...')
    logger.error('testing...')
    logger.critical('testing...')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:27:36.720016
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    assert log.level == logging.DEBUG
    
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:27:44.422891
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger('LevelTest')
    l.level = logging.INFO
    with logger_level(l, logging.DEBUG):
        l.info('this should be printed')
        l.debug('this should be printed too')
        with logger_level(l, logging.INFO):
            l.info('this should be printed again')
            l.debug('this should be suppressed')
        l.debug('this should be printed')
    l.debug('this should not be printed')

test_logger_level()

# Generated at 2022-06-14 06:27:51.519893
# Unit test for function configure
def test_configure():
    configure()
    logging.getLogger(__name__).info('test_configure')



# Generated at 2022-06-14 06:28:03.074056
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys

    test_logger = logging.getLogger('logger_level_test')

    # Test basic function
    with logger_level(test_logger, logging.DEBUG):
        test_logger.debug('Test')
    test_logger.debug('Test2')

    # Test if context manager works properly
    with logger_level(test_logger, logging.ERROR):
        test_logger.debug('Test')
        with logger_level(test_logger, logging.INFO):
            test_logger.info('Test2')
            with logger_level(test_logger, logging.WARNING):
                test_logger.warning('Test3')
            test_logger.info('Test2')
        test_logger.debug('Test')

# Generated at 2022-06-14 06:28:09.835144
# Unit test for function logger_level
def test_logger_level():
    # Check that the logging level is set correctly
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

# End of unit test for function logger_level


# Generated at 2022-06-14 06:28:22.217722
# Unit test for function logger_level
def test_logger_level():
    from collections import namedtuple
    from .formatter import LogRecord
    import io
    import pytest
    import logging

    log_record = namedtuple('LogRecord', 'levelname msg')
    tmp_string_io = io.StringIO()
    logger = logging.getLogger('test')
    handler = logging.StreamHandler(tmp_string_io)
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    # Level of the logger is INFO.
    logger.debug('debug')
    logger.info('info')
    logger.error('error')
    assert tmp_string_io.getvalue() == 'info\nerror\n'

    with logger_level(logger, logging.DEBUG):
        # Level of the logger is now DEBUG.
        logger.debug('debug')
        logger

# Generated at 2022-06-14 06:28:26.784295
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.ERROR):
        logger.warning('test message')
    logger.warning('test message')

# Generated at 2022-06-14 06:28:31.438693
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.info('info should not be called')

    log.debug('debug should not be called')
    log.info('info')



# Generated at 2022-06-14 06:28:40.376974
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger("logger_level_test")
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        assert logger.isEnabledFor(logging.INFO)
        assert not logger.isEnabledFor(logging.DEBUG)
    assert not logger.isEnabledFor(logging.INFO)
    assert logger.isEnabledFor(logging.DEBUG)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:28:45.068691
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger('logging_setup'), logging.DEBUG):
        get_logger('logging_setup').debug("This is a test to see if logger_level works.")

# Generated at 2022-06-14 06:28:50.541665
# Unit test for function logger_level
def test_logger_level():
    import uuid
    import queue
    import logging.handlers

    root_logger = logging.getLogger()

    mem_handler = logging.handlers.QueueHandler(queue.Queue())
    root_logger.addHandler(mem_handler)

    log = getLogger('test_logger_level')
    log.setLevel(logging.DEBUG)
    log.debug('Hey there!')

    with logger_level(log, logging.INFO):
        log.debug('should not be called')

    root_logger.removeHandler(mem_handler)


# Generated at 2022-06-14 06:29:02.332913
# Unit test for function get_config

# Generated at 2022-06-14 06:29:19.061061
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.ERROR):
        logger.setLevel(logging.ERROR)
        assert logger.level == logging.ERROR
        assert logger.getEffectiveLevel() == logging.ERROR
        logger.error('test message')

    logger.setLevel(logging.DEBUG)
    assert logger.level == logging.DEBUG
    assert logger.getEffectiveLevel() == logging.DEBUG
    logger.error('test message')



# Generated at 2022-06-14 06:29:22.033187
# Unit test for function configure
def test_configure():
    logger = logging.getLogger(__name__)
    configure()
    logger.info('test')


# Generated at 2022-06-14 06:29:33.585036
# Unit test for function logger_level
def test_logger_level():
    import contextlib
    import logging
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    with logger_level(logger, logging.DEBUG):
        logger.debug('Hello, debug')
        logger.info('Hello, info')
        logger.warning('Hello, warning')
        logger.error('Hello, error')

    logger.debug('Hello, debug')
    logger.info('Hello, info')

# Generated at 2022-06-14 06:29:37.997818
# Unit test for function logger_level
def test_logger_level():
    import logging
    
    logger = logging.getLogger(__name__)
    
    with logger_level(logger, logging.DEBUG):
        logger.debug('Hello, world!')
    print(logger.level)

# if __name__ == '__main__':
#     test_logger_level()

# Generated at 2022-06-14 06:29:46.230778
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    from contextlib import ExitStack

    with ExitStack() as stack:
        logger = stack.enter_context(get_logger())
        logger.setLevel(logging.WARN)
        with stack.enter_context(logger_level(logger, logging.DEBUG)):
            logger.debug('hello world')
        with stack.enter_context(logger_level(logger, logging.DEBUG)):
            logger.info('hello world')

test_logger_level()

# Generated at 2022-06-14 06:29:50.489630
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    assert log.level == logging.DEBUG
    with logger_level(log, logging.ERROR):
        assert log.level == logging.ERROR
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:29:53.895529
# Unit test for function configure
def test_configure():
    logger = get_logger(__name__)
    assert logger.name == __name__


# Generated at 2022-06-14 06:29:57.349778
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.info('Hello')
    logger.info('Goodbye')

# Generated at 2022-06-14 06:30:00.839624
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.INFO):
        log.debug('show me not')
        log.info('show me')
    log.debug('show me not')

# Generated at 2022-06-14 06:30:13.323063
# Unit test for function configure
def test_configure():
    """
    >>> import logging
    >>> log = logging.getLogger('log_config_test')
    >>> configure()
    >>> assert log.getEffectiveLevel() == logging.DEBUG
    >>> configure(default=dict(root=dict(level='WARNING')))
    >>> assert log.getEffectiveLevel() == logging.WARNING
    >>> configure(default=dict(root=dict(level='DEBUG')))
    >>> assert log.getEffectiveLevel() == logging.DEBUG
    >>> configure(default=dict(root=dict(level='ERROR')))
    >>> assert log.getEffectiveLevel() == logging.ERROR
    >>> configure()
    >>> assert log.getEffectiveLevel() == logging.DEBUG
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:30:23.284493
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.ERROR):
        logger.error("logger level is ERROR")
        logger.debug("logger level is ERROR")
    logger.debug("logger level is %d", logger.level)



# Generated at 2022-06-14 06:30:34.960759
# Unit test for function get_config

# Generated at 2022-06-14 06:30:49.335662
# Unit test for function logger_level
def test_logger_level():
    import tempfile


# Generated at 2022-06-14 06:30:54.086080
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.debug('This should not show up')
        log.error('This should show up')
    log.info('This should show up')


# Generated at 2022-06-14 06:31:05.096738
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger("test_logger_level")
    assert logger.level == logging.getLevelName("DEBUG")
    with logger_level(logger, logging.getLevelName("INFO")):
        assert logger.level == logging.getLevelName("INFO")
    assert logger.level == logging.getLevelName("DEBUG")
    with logger_level(logger, logging.getLevelName("WARNING")):
        assert logger.level == logging.getLevelName("WARNING")
    assert logger.level == logging.getLevelName("DEBUG")
    with logger_level(logger, logging.getLevelName("ERROR")):
        assert logger.level == logging.getLevelName("ERROR")
    assert logger.level == logging.getLevelName("DEBUG")

# Generated at 2022-06-14 06:31:16.158605
# Unit test for function get_config
def test_get_config():
    from collections import OrderedDict

    # Test config with hand crafted dict
    config = get_config(default={'test': '1'})
    assert config['test'] == '1'

    # Test config with hand crafted dict which is ordered
    config = get_config(
        default=OrderedDict([
            ('version', '1'),
            ('test', '1'),
            ]))

    assert config['test'] == '1'
    assert config['version'] == '1'

    # Test config with hand crafted dict as JSON string
    config_json = '{"test": "1"}'
    config = get_config(default=config_json)
    assert config['test'] == '1'

    # Test config with hand crafted dict as YAML string
    config_yaml = 'test: 1'
    config = get_

# Generated at 2022-06-14 06:31:20.739874
# Unit test for function logger_level
def test_logger_level():
    """Test function logger_level"""
    # Setup
    logger = get_logger()

    # Test
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level != logging.DEBUG
    

# Generated at 2022-06-14 06:31:25.315195
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    assert logger.level == logging.NOTSET
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.NOTSET


# Generated at 2022-06-14 06:31:31.319090
# Unit test for function logger_level
def test_logger_level():
    """
    >>> logger = get_logger()
    >>> with logger_level(logger, logging.ERROR):
    ...     logger.debug('You should never see this')
    ...     logger.error('You should see this')
    ...     logger.info('You should never see this')
    ...     logger.warning('You should never see this')
    """

# Generated at 2022-06-14 06:31:39.745026
# Unit test for function logger_level
def test_logger_level():
    import unittest
    from logging import DEBUG
    from contextlib import redirect_stdout

    class TestLoggerLevel(unittest.TestCase):
        def test_logger_level(self):
            # Setup
            logger = getLogger('test')
            logger.addHandler(logging.NullHandler())
            logger.setLevel(DEBUG)
            with redirect_stdout(sys.stdout):
                # Test
                with logger_level(logger, logging.INFO):
                    logger.debug('test')
                    logger.info('test2')
                with logger_level(logger, logging.DEBUG):
                    logger.debug('test3')
                    logger.info('test4')

    unittest.main()

# Generated at 2022-06-14 06:31:57.242263
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    # Set the logger level to ERROR
    assert log.isEnabledFor(logging.DEBUG) == True , 'The logger level should be DEBUG'
    with logger_level(log, logging.DEBUG) as debug_log:
        # Check that logger level changed to DEBUG within the context block
        assert log.isEnabledFor(logging.ERROR) == False, 'The logger level should be ERROR'
    # Check that logger level is restored to ERROR outside the context block
    assert log.isEnabledFor(logging.DEBUG) == True , 'The logger level should be DEBUG'

# Generated at 2022-06-14 06:32:08.347425
# Unit test for function get_config

# Generated at 2022-06-14 06:32:12.563471
# Unit test for function logger_level
def test_logger_level():
    import logging
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.info('before')
    with logger_level(log, logging.DEBUG):
        log.debug('in middle')
    log.info('after')


# Generated at 2022-06-14 06:32:26.956890
# Unit test for function logger_level
def test_logger_level():
    # Create a fake logger
    logger = logging.Logger("test_logger")
    # Attach a fake logger to the fake logger, that just adds to a list
    logger.log = lambda level, msg: logger.logged.append((level, msg))
    logger.logged = []
    # Run the logger with a captured output
    with logger_level(logger, logging.DEBUG):
        logger.debug("foo")
    # Check the result
    assert logger.logged == [(logging.DEBUG, "foo")]
    # Check that we haven't messed up the logging state
    assert logger.level == logging.NOTSET
    # Do the same again, but with a higher level
    # (This used to fail, hence the test)
    with logger_level(logger, logging.ERROR):
        logger.error("foo")
       

# Generated at 2022-06-14 06:32:38.621475
# Unit test for function logger_level
def test_logger_level():
    """Should set and reset logger levels with contextmanager."""
    import logging

    logger = logging.getLogger(__name__)
    assert logger.level == logging.NOTSET, "Default logger level should be NOTSET."

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG, "Temporary logger level should be DEBUG."

    assert logger.level == logging.NOTSET, "Logger level should be reset to NOTSET."


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    print("Passed doctest.")

# Generated at 2022-06-14 06:32:47.144493
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    assert log.level == 10

    with logger_level(log, 0):
        try:
            # This should log a message
            log.warning('If this was logged, then logger_level works')
        except Exception as err:
            # If something went wrong, log it
            log.error('logger_level test failed: %s' % err)
            raise err

# Generated at 2022-06-14 06:32:57.073805
# Unit test for function logger_level
def test_logger_level():
    """Test logger level change within context manager.
    """
    # Make sure no logging is present.
    logger = getLogger()
    with logger_level(logger, logging.CRITICAL):
        logger.debug("This will not be logged")

    # Test level change
    logger = getLogger()
    logger.setLevel(logging.CRITICAL)
    with logger_level(logger, logging.DEBUG):
        logger.debug("This will be logged")

# Generated at 2022-06-14 06:33:01.721384
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    logger.setLevel(logging.INFO)
    logger.info("Test before setting level")
    with logger_level(logger, logging.WARNING):
        logger.info("Test after setting level")
    logger.info("Test after returning from context")

# Generated at 2022-06-14 06:33:09.378052
# Unit test for function logger_level
def test_logger_level():
    import logging
    import contextlib

    my_logger = logging.getLogger('my_logger')
    my_logger.setLevel(logging.INFO)

    with logger_level(my_logger, logging.DEBUG):
        assert my_logger.level == logging.DEBUG
    assert my_logger.level == logging.INFO

    with contextlib.closing(logger_level(my_logger, logging.DEBUG)) as cm:
        assert cm.__exit__() is None
    assert my_logger.level == logging.INFO

# Generated at 2022-06-14 06:33:21.201757
# Unit test for function get_config

# Generated at 2022-06-14 06:33:46.828263
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("test_logger_level")
    with logger_level(logger, logging.INFO):
        logger.debug("logger_level DEBUG: not shown")
        logger.info("logger_level INFO: shown")
    logger.debug("logger_level DEBUG: shown")
    logger.info("logger_level INFO: shown")

if __name__ == '__main__':
    test_logger_level()
    print("Done.")

# Generated at 2022-06-14 06:33:55.252851
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    log.debug('This is a debug message')
    with logger_level(log, logging.INFO):
        log.debug('This is a debug message')
        log.info('This is a info message')
    log.debug('This is a debug message')

# pytest doesn't support unittest.main(). So, I add this code to make it possible.
if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:33:58.633361
# Unit test for function configure
def test_configure():
    configure()
    log = logging.getLogger(__name__)
    log.debug('test')
    log.info('test')



# Generated at 2022-06-14 06:34:04.227560
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.INFO):
        log.info('test')
    assert(log.level == logging.DEBUG)
    log.info('test')


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:34:07.815732
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    level = logging.DEBUG
    with logger_level(logger, level):
        assert logger.level == level
    assert logger.level != level

# Generated at 2022-06-14 06:34:10.591000
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARNING):
        logger.info("info message shouldn't be shown")
        logger.warning("warning message should be shown")

# Generated at 2022-06-14 06:34:22.714703
# Unit test for function logger_level
def test_logger_level():
    # Logger should not be configured here
    import logging.config
    import logging.handlers
    try:
        logging.config.fileConfig("logging.conf")
    except BaseException:
        pass
    # Nothing should be printed here
    logger = logging.getLogger("test_logger_level")
    logger.info("logging.INFO")
    logger.debug("logging.DEBUG")
    with logger_level(logger, logging.INFO):
        logger.debug("logging.DEBUG")
    logger.debug("logging.DEBUG")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:29.438662
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('Before logger_level')
    with logger_level(logger, logging.NOTSET):
        logger.info('Should not be visible')
        with logger_level(logger, logging.DEBUG):
            logger.info('Should be visible')
    logger.info('After')
    # End unit test

# Generated at 2022-06-14 06:34:37.771280
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        assert log.isEnabledFor(logging.DEBUG)
    assert not log.isEnabledFor(logging.DEBUG)
    with logger_level(log, logging.DEBUG):
        pass
    assert not log.isEnabledFor(logging.DEBUG)
    with logger_level(log, logging.DEBUG):
        raise Exception('lol')
    # the exception here is re-raised.



# Generated at 2022-06-14 06:34:42.781344
# Unit test for function configure
def test_configure():
    import logging
    import os
    import time

    os.environ["LOGGING"] = json.dumps(config)

    configure()
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.info("Simple logger test")
        logger.info("Simple logger test in name-spaced logger")