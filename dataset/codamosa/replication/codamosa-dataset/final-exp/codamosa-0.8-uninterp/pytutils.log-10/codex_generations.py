

# Generated at 2022-06-14 06:25:15.214959
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO) as log:
        logger.info("I'm logging at INFO")
        logger.debug("I'm logging at DEBUG")
        assert logger.level == logging.INFO

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:21.680812
# Unit test for function logger_level
def test_logger_level():
    assert get_logger().level is not logging.DEBUG
    with logger_level(get_logger(), logging.DEBUG):
        assert get_logger().level == logging.DEBUG

    with logger_level(get_logger(), logging.ERROR):
        assert get_logger().level == logging.ERROR
    assert get_logger().level is not logging.ERROR



# Generated at 2022-06-14 06:25:25.688776
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    try:
        with logger_level(logger, logging.DEBUG):
            logger.debug('Test logger level')
    except Exception as e:
        print("test_logger_level exception: %s" % e)

# Generated at 2022-06-14 06:25:28.364900
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.WARN):
        assert log.level == logging.WARN
    assert log.level == logging.INFO

# Generated at 2022-06-14 06:25:38.736778
# Unit test for function get_config
def test_get_config():
    # Test config is a dict
    config = get_config(dict(a='b'))
    assert config == {'a': 'b'}

    # Test config is a dict and dict hasn't formatting
    config = get_config(dict(a='b', c=1))
    assert config == {'a': 'b', 'c': 1}

    # Test config is a JSON
    config = get_config(json.dumps({'a': 'b', 'c': 1}))
    assert config == {'a': 'b', 'c': 1}

    # Test config is a YAML
    config = get_config('a: b\nc: 1')
    assert config == {'a': 'b', 'c': 1}

    # Test config is a dict that has formatting

# Generated at 2022-06-14 06:25:41.947347
# Unit test for function logger_level
def test_logger_level():
    import time

    logger = get_logger('test')

    logger.setLevel(logging.INFO)
    logger.info('test')

    with logger_level(logger, logging.DEBUG):
        logger.debug('test')

    logger.info('test')


# Generated at 2022-06-14 06:25:48.080976
# Unit test for function logger_level
def test_logger_level():
    test_level = logging.INFO;
    log = get_logger("canprog.test_logger_level")
    logger_level_to_print = get_logger("canprog.logger_level_to_print")

    logger_level_to_print.debug("This should not be printed")
    logger_level_to_print.warn("This should not be printed")

    with logger_level(logger_level_to_print, test_level):
        logger_level_to_print.debug("This should be printed")
        logger_level_to_print.info("This should be printed")
        logger_level_to_print.warn("This should be printed")

    logger_level_to_print.debug("This should not be printed")

# Generated at 2022-06-14 06:25:55.599265
# Unit test for function logger_level
def test_logger_level():
    from unittest import TestCase
    from logging import DEBUG, INFO

    class TestLogger(object):
        def __init__(self):
            self.level = INFO
            self.called = []

        def debug(self, *args):
            self.called.append(args)

    class TestLoggerLevel(TestCase):
        def test_it(self):
            logger = TestLogger()
            with logger_level(logger, DEBUG):
                logger.debug('foo')
            logger.debug('bar')
            self.assertEqual(['foo', 'bar'], logger.called)

    # test_it()

# Generated at 2022-06-14 06:26:01.401369
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')
    with logger_level(log, logging.DEBUG):
        log.info('debug level info')
        log.debug('debug level debug')
    log.info('info')
    log.debug('debug')

# vim: et:sw=4:syntax=python:ts=4:

# Generated at 2022-06-14 06:26:05.796554
# Unit test for function logger_level
def test_logger_level():
    # Test logger_level function
    logger = logging.getLogger('logger_level')
    configure()
    with logger_level(logger, logging.DEBUG):
        # Test if logger level is set correctly within context
        assert logger.level == logging.DEBUG
        logger.info('test_logger_level')
    # Test if logger level is reset correctly after context
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:26:18.410446
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger('test')
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(console)
    logger.debug('Should not show up')

    # this will be suppressed
    with logger_level(logger, logging.DEBUG):
        logger.debug('Should show up')

    # this will be suppressed again
    logger.debug('Should not show up')

# Generated at 2022-06-14 06:26:22.697201
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(test_logger_level.__name__)
    with logger_level(log, logging.ERROR):
        log.debug('should not be printed')
        log.error('should be printed')


# Generated at 2022-06-14 06:26:25.875496
# Unit test for function configure
def test_configure():
    import logging
    configure()
    log = logging.getLogger(__name__)
    log.info('test')



# Generated at 2022-06-14 06:26:32.881783
# Unit test for function logger_level
def test_logger_level():
    from nose.tools import assert_equals
    from logging import DEBUG, INFO

    try:
        logger = getLogger()
        with logger_level(logger, DEBUG):
            with logger_level(logger, INFO):
                assert_equals(logger.level, INFO)
            assert_equals(logger.level, DEBUG)
        assert_equals(logger.level, INFO)
    finally:
        logger.level = INFO



# Generated at 2022-06-14 06:26:36.648696
# Unit test for function configure
def test_configure():
    logger = logging.getLogger("configure")
    logger.info("test")



# Generated at 2022-06-14 06:26:46.789671
# Unit test for function get_config
def test_get_config():
    cfg_string = '''
        version: 1
        formatters:
            simple:
                format: '%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s'
                datefmt: '%Y-%m-%d %H:%M:%S'
        handlers:
            console:
                class: logging.StreamHandler
                formatter: simple
                level: DEBUG
        root:
            handlers: [console]
            level: DEBUG
        loggers:
            requests:
                level: INFO
    '''

# Generated at 2022-06-14 06:26:54.968292
# Unit test for function logger_level
def test_logger_level():
    # Create a root logger
    root = logging.getLogger()
    root_initial = root.level
    root.setLevel(logging.INFO)
    
    # Create a child logger
    logger = logging.getLogger('test')
    child_level = logger.level
    logger.setLevel(logging.DEBUG)
    root.addHandler(logging.StreamHandler())
    
    assert logger.level == logging.DEBUG
    
    # Test that context block correctly changes logger level
    with logger_level(logger, logging.WARNING):
        assert logger.level == logging.WARNING
        
        # Test that setting level outside of context block doesn't affect logger within context
        logger.setLevel(logging.DEBUG)
        assert logger.level == logging.WARNING
        
        # Test that child logger gets reset to initial level when leaving context

# Generated at 2022-06-14 06:27:05.538998
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import unittest

    logger = logging.getLogger()
    _, tmp_file = tempfile.mkstemp(suffix='.log', prefix='tmp-')

    handler = logging.handlers.RotatingFileHandler(tmp_file)
    logger.addHandler(handler)

    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')

    with open(tmp_file) as f:
        lines = f.readlines()


# Generated at 2022-06-14 06:27:09.843767
# Unit test for function configure
def test_configure():
    try:
        configure()
        log = get_logger(__name__)
        log.info('test')
        assert True
    except:
        assert False


if __name__ == "__main__":
    test_configure()

# Generated at 2022-06-14 06:27:20.799364
# Unit test for function logger_level
def test_logger_level():
    config_str = """
    version: 1
    disable_existing_loggers: False
    formatters:
        simple:
            format: %(message)s
    handlers:
        console:
            class: logging.StreamHandler
            formatter: simple
            stream: ext://sys.stdout
    root:
        level: INFO
        handlers: [console]
    """
    configure(config_str)

    # Create new file "temp_log_level.txt" for storing log messages
    log_file = open("temp_log_level.log", "w")
    log_file.close()
    with open("temp_log_level.log", "a") as log_file:
        sys.stdout = log_file
        log = logging.getLogger()
        log.info("Test INFO message")

# Generated at 2022-06-14 06:27:29.370073
# Unit test for function logger_level
def test_logger_level():
    """basic test of logger_level"""
    logger = getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.info("I'm info")
        logger.debug("I'm debug")



# Generated at 2022-06-14 06:27:34.152109
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    assert log.level is logging.DEBUG

    with logger_level(log, logging.INFO):
        assert log.level is logging.INFO

    assert log.level is logging.DEBUG

    log.info('Inside debug')
    with logger_level(log, logging.WARNING):
        log.info('Inside warning')

    log.info('Back to debug')

# Generated at 2022-06-14 06:27:39.249215
# Unit test for function logger_level
def test_logger_level():
    # Silence logger during unit test
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.debug('debugged')
        logger.info('infoed')
        logger.warning('warned')

# Generated at 2022-06-14 06:27:48.498176
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')
    # Configure the logger to log the highest level messages

# Generated at 2022-06-14 06:27:52.956313
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(__name__), logging.DEBUG):
        get_logger(__name__).debug('logger_level works!')

# Generated at 2022-06-14 06:27:59.060563
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    # If a message is logged below where the logger level is set
    # then an error will be triggered in the except block.
    try:
        with logger_level(log, logging.CRITICAL):
            log.info("will not appear in output")
    except Exception as e:
        raise Exception("logger_level test failed") from e


# Generated at 2022-06-14 06:28:00.923194
# Unit test for function configure
def test_configure():
    configure()
    log = logging.getLogger(__name__)
    log.info('test')


# Generated at 2022-06-14 06:28:06.284405
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("This should be seen.")
        log.info("This should not be seen.")
    log.info("This should be seen again.")

DEFAULT_CONFIG['loggers'][__name__] = dict(level=logging.INFO)



# Generated at 2022-06-14 06:28:11.236542
# Unit test for function logger_level
def test_logger_level():
    # Make sure we're in a context manager by setting level to something
    # different and seeing if it gets reset.
    with logger_level(getLogger(), logging.INFO):
        assert getLogger().level == logging.INFO
    assert getLogger().level == logging.DEBUG


# Generated at 2022-06-14 06:28:18.210083
# Unit test for function logger_level
def test_logger_level():
    # Test that logger_level() sets the logger level correctly to the requested level
    # within the context and restores the level correctly after exiting the context
    logger = logging.getLogger('test')
    logger.setLevel(logging.INFO)

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG

    assert logger.level == logging.INFO



# Generated at 2022-06-14 06:28:27.977963
# Unit test for function configure
def test_configure():
    assert configure(None) == configure(DEFAULT_CONFIG)


# Generated at 2022-06-14 06:28:33.080145
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

    log.setLevel(logging.DEBUG)

    log.debug("Before")

    with logger_level(log, logging.ERROR):
        log.debug("In block")
        assert log.getEffectiveLevel() == logging.ERROR

    log.debug("After")


# Generated at 2022-06-14 06:28:41.700707
# Unit test for function logger_level
def test_logger_level():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    from contextlib import contextmanager
    @contextmanager
    def assert_raises(*exc_types):
        """assert that a given block of code raises any exc_types"""
        raised = False
        try:
            yield
        except exc_types:
            raised = True
        assert raised, "Expected an exception to be raised"
    class TestLoggerLevel(unittest.TestCase):
        def test_logging_level_not_set(self):
            logger = get_logger()

# Generated at 2022-06-14 06:28:45.067689
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

# Generated at 2022-06-14 06:28:50.199977
# Unit test for function logger_level
def test_logger_level():
    log_level = logging.DEBUG
    logger = get_logger()
    logger.setLevel(logging.INFO)
    assert logger.level == logging.INFO
    with logger_level(logger, log_level):
        assert logger.level == log_level
    assert logger.level == logging.INFO

# Generated at 2022-06-14 06:28:57.562123
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.WARN):
        log.info("This log will go to console, because it is WARNING level.")
        log.warning("This log will go to console, because it is WARNING level.")
        log.error("This log will go to console, because it is WARNING level.")
    log.info("This log will go to console, because it is INFO level.")
    log.warning("This log will go to console, because it is INFO level.")


# Generated at 2022-06-14 06:29:08.338972
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    with logger_level(logger, logging.CRITICAL):
        logger.debug('This one is not logged!')
        logger.critical('We are in critical mode!')

    logger.debug('XXXXXXXXXXXXXXXXXX')
    logger.info('We are in normal mode!')
    logger.critical('We are in normal mode!')


if __name__ == '__main__':
    test_logger_level()


# Generated at 2022-06-14 06:29:12.331731
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.info("hello")
        log.debug("there")
        log.error("you")

# Generated at 2022-06-14 06:29:18.569112
# Unit test for function get_config
def test_get_config():
    cfg = get_config(config=DEFAULT_CONFIG)
    assert cfg == DEFAULT_CONFIG

    cfg = get_config(env_var='_LOGGING', default=DEFAULT_CONFIG)
    assert cfg == DEFAULT_CONFIG

    get_config()

# Generated at 2022-06-14 06:29:31.171669
# Unit test for function get_config
def test_get_config():
    # Test if given and config are None
    try:
        get_config()
    except ValueError as e:
        assert 'Invalid logging config:' in str(e)

    # Test if given is str
    cfg = get_config(given='{}')
    assert cfg == {}
    cfg = get_config(given='{1:2}')
    assert cfg == {1: 2}
    cfg = get_config(given='{"1": 2}')
    assert cfg == {'1': 2}
    # Invalid
    try:
        get_config(given='{')
    except ValueError as e:
        assert 'Could not parse logging config as bare, json, or yaml' in str(e)

    # Test if given is dict
    cfg = get_config(given={})
    assert cf

# Generated at 2022-06-14 06:29:54.129819
# Unit test for function logger_level
def test_logger_level():
    from unittest import mock
    import sys

    logger = mock.Mock()

    # Pretend like the logger has had a level set
    logger.level = 30

    # Arbitrary high level
    OVER_NINE_THOUSAND = 9001

    with logger_level(logger, OVER_NINE_THOUSAND):
        assert logger.level == OVER_NINE_THOUSAND

    assert logger.level == 30



# Generated at 2022-06-14 06:30:05.755480
# Unit test for function configure
def test_configure():
    logger = logging.getLogger('test_configure')

# Generated at 2022-06-14 06:30:18.896245
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Test logger level higher than initial level
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG) is True
        assert logger.isEnabledFor(logging.INFO) is True

    # Test logger level lower than initial level
    with logger_level(logger, logging.ERROR):
        assert logger.isEnabledFor(logging.INFO) is False
        assert logger.isEnabledFor(logging.ERROR) is True


# XXX: This is a quick hack to add a handler to an existing logging configuration.
#      This is probably not the best way to do this, but it works for now.

# Generated at 2022-06-14 06:30:32.064332
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    f = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 06:30:35.414800
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()

    # initial level
    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG


# Unit tests for this module

# Generated at 2022-06-14 06:30:49.370245
# Unit test for function logger_level
def test_logger_level():
    import random
    import logging

    # Create logger using get_logger func
    log = get_logger("logger_level")

    # Test 1
    with logger_level(log, logging.DEBUG):
        log.debug("Test 1")

    # Test 2
    with logger_level(log, logging.INFO):
        log.debug("Test 2")

    # Test 3
    with logger_level(log, logging.WARNING):
        log.debug("Test 3")

    # Test 4
    with logger_level(log, logging.ERROR):
        log.debug("Test 4")

    # Test 5
    with logger_level(log, random.randint(-1, 100)):
        log.debug("Test 5")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:02.313866
# Unit test for function configure
def test_configure():
    import tempfile


# Generated at 2022-06-14 06:31:07.280591
# Unit test for function logger_level
def test_logger_level():
    # get current logger level
    old_level = logging.getLogger().getEffectiveLevel()

    # check that the logger level is changed in the context block
    with logger_level(logging.getLogger(), logging.INFO):
        assert logging.getLogger().getEffectiveLevel() == logging.INFO

    # check that the logger level is reset outside the context block
    assert logging.getLogger().getEffectiveLevel() == old_level


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:31:11.957263
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger('test_logger_level')
    with logger_level(logging.getLogger('test_logger_level'), logging.DEBUG):
        l.debug('debug')
        l.info('info')

# Generated at 2022-06-14 06:31:19.709309
# Unit test for function logger_level
def test_logger_level():
    import time
    import random
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Info message 1")
    logger.debug("Debug message 1")

    with logger_level(logger, logging.DEBUG):
        logger.info("Info message 2")
        logger.debug("Debug message 2")

    logger.info("Info message 3")
    logger.debug("Debug message 3")


# Generated at 2022-06-14 06:31:41.621920
# Unit test for function logger_level
def test_logger_level():
    """Test logger_level function for validity."""
    logger = get_logger(__name__)
    logger.debug('This debug message should be displayed.')
    with logger_level(logger, logging.ERROR):
        logger.debug('This debug message should not be displayed.')


# getLogger = get_logger

# Generated at 2022-06-14 06:31:53.894858
# Unit test for function get_config
def test_get_config():
    env_var='123'
    test_default={'key':'value'}
    test_config={'key':'value', 'key2':'value2'}
    input_config=None
    output_config=get_config(input_config, env_var, test_default)
    assert output_config == test_default

    input_config=test_config
    output_config=get_config(input_config, env_var, test_default)
    assert output_config == test_config

    input_config=None
    output_config=get_config(input_config, env_var, test_default)
    assert output_config == test_default

# Generated at 2022-06-14 06:32:02.215310
# Unit test for function get_config
def test_get_config():
    from yaml import load as yaml_load


# Generated at 2022-06-14 06:32:10.097852
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    assert logger.level == 10  # default level is not 0, but 10
    with logger_level(logger, 0):
        assert logger.level == 0
        logger.debug("This should not show up")
        logger.info("This should show up")
        logger.warning("This should show up too")
    assert logger.level == 10
    logger.info("This should definitely show up")
    logger.debug("This should not show up")



# Generated at 2022-06-14 06:32:18.531784
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    with logger_level(logger, logging.DEBUG):
        logger_level(logger, logging.WARNING)
    with logger_level(logger, logging.WARNING):
        logger_level(logger, logging.INFO)
    with logger_level(logger, logging.INFO):
        logger_level(logger, logging.DEBUG)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:32:27.403215
# Unit test for function logger_level
def test_logger_level():
    from logging import CRITICAL, DEBUG, INFO
    log = get_logger(__name__)
    test_log = "Logger_level"

    with logger_level(log, INFO):
        log.warning(test_log) # This line should be not shown

    with logger_level(log, CRITICAL):
        log.info(test_log) # This line should be shown

    with logger_level(log, DEBUG):
        log.info(test_log) # This line should be shown

# Generated at 2022-06-14 06:32:30.471464
# Unit test for function logger_level
def test_logger_level():
    """
    >>> logger_level(logging.getLogger(__name__), logging.DEBUG)
    """

# Generated at 2022-06-14 06:32:45.766850
# Unit test for function configure
def test_configure():
    import tempfile
    import json

    with tempfile.NamedTemporaryFile() as config_file:
        config_file.write(json.dumps({
            'version': 1,
            'formatters': {
                'simple': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'simple',
                },
            },
            'loggers': {
                __name__: {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                    'propagate': False,
                },
            },
        }))
        config_

# Generated at 2022-06-14 06:32:49.151109
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert (logger.isEnabledFor(logging.DEBUG))
        logger.debug("Debug log")
        logger.info("Info log")
    assert (not logger.isEnabledFor(logging.DEBUG))


# Generated at 2022-06-14 06:32:54.961581
# Unit test for function configure
def test_configure():
    import logging
    import logging.config

    configure()
    log = getLogger(__name__)
    logger_test = logging.getLogger(__name__)
    logger_test.debug('test')
    assert logger_test is log



# Generated at 2022-06-14 06:33:30.714456
# Unit test for function configure
def test_configure():
    configure()
    # configure(env_var='LOGGING_ENV_VAR')

# Generated at 2022-06-14 06:33:38.030759
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()

    for level, log_func in (
        (logging.INFO, logger.info),
        (logging.DEBUG, logger.debug),
    ):
        with logger_level(logger, level):
            assert logger.level == level
            log_func('Test')
            log_func('Test2')

    assert logger.level == logging.NOTSET

    logger.debug('Should not see')
    logger.info('Should not see')


if __name__ == '__main__':
    import nose

    nose.runmodule()

# Generated at 2022-06-14 06:33:39.785130
# Unit test for function get_config
def test_get_config():
    assert isinstance(get_config(default=DEFAULT_CONFIG), dict)

# Generated at 2022-06-14 06:33:52.426529
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()

    with logger_level(log, logging.ERROR):
        assert log.level == logging.ERROR
        log.info('test')
        log.warning('test')
        log.error('test')

    assert log.level == logging.DEBUG
    log.info('test')
    log.warning('test')
    log.error('test')



## Log to multiple loggers
#stderr_log = logging.StreamHandler()
#stderr_log.setFormatter(logging.Formatter(LOG_FORMAT))
#
#log = logging.getLogger('speech_recognition')
#log.addHandler(stderr_log)
#log.setLevel(logging.INFO)
#
#pocketsphinx_logger = logging.getLogger('pocketsphinx')


# Generated at 2022-06-14 06:33:56.756277
# Unit test for function logger_level
def test_logger_level():

    print(get_logger().debug('bottom of file'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    test_logger_level()

# Generated at 2022-06-14 06:34:07.819351
# Unit test for function logger_level
def test_logger_level():
    # Create logger
    logger = logging.getLogger("test_logger_level")
    # Set logger level to debug
    logger.setLevel(logging.DEBUG)
    # Check that logger is not configured for info level
    assert logger.isEnabledFor(logging.INFO) == False
    # Enter "context"
    with logger_level(logger, logging.INFO):
        # Check that logger is configured for info level
        assert logger.isEnabledFor(logging.INFO) == True
    # Check that logger is no longer configured for info level
    assert logger.isEnabledFor(logging.INFO) == False

# Generated at 2022-06-14 06:34:13.759143
# Unit test for function configure
def test_configure():
    import os
    import pytest
    import tempfile
    import json
    import yaml

    logger = logging.getLogger(__name__)
    str_formatter = '%(asctime)s| %(name)s/%(processName)s[%(process)d] #%(levelname)s %(message)s'

# Generated at 2022-06-14 06:34:26.030798
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    # Try bad config
    # TODO
    # Try good config

# Generated at 2022-06-14 06:34:32.566344
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('levels')
    logger.setLevel(logging.INFO)

    logger.info('test')
    assert len(logger.handlers[0].buffer) == 1

    with logger_level(logger, logging.DEBUG) as level_ctx:
        logger.debug('test')
        assert len(logger.handlers[0].buffer) == 2

    logger.debug('test')
    assert len(logger.handlers[0].buffer) == 2


# TODO Are these even useful?

# Generated at 2022-06-14 06:34:39.304034
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    # Test that the function does not give an error and actually changes log level to something other than DEBUG
    with logger_level(log, logging.WARN):
        assert log.level == logging.WARN
    assert log.level == logging.DEBUG
    assert logger_level(log, logging.ERROR) is None

if __name__ == "__main__":
    test_logger_level()