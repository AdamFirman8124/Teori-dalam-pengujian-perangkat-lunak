

# Generated at 2022-06-14 06:25:17.114626
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug("test")
    assert log.level == logging.DEBUG
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        log.info("test")
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:25:22.174697
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug('message')
    with logger_level(log, logging.INFO):
        log.debug('should not print')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:27.765947
# Unit test for function get_config
def test_get_config():
    config = get_config(given="{'foo': 'bar'}")
    assert config == {'foo': 'bar'}


if __name__ == '__main__':
    import doctest
    import os

    if os.environ.get('TEST_LOGGING'):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s|%(levelname)s|%(name)s:%(funcName)s:%(lineno)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

    doctest.testmod()

# Generated at 2022-06-14 06:25:35.562412
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    assert log.level == logging.WARNING
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.info('info')
        log.warning('warning')
        log.error('error')
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')

# Generated at 2022-06-14 06:25:42.872214
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()
    log = getLogger()

    with logger_level(log, logging.INFO):
        assert(log.isEnabledFor(logging.INFO))
        with logger_level(log, logging.CRITICAL):
            assert(log.isEnabledFor(logging.CRITICAL))
        assert(log.isEnabledFor(logging.INFO))
    assert(log.isEnabledFor(logging.DEBUG))



# Generated at 2022-06-14 06:25:46.750235
# Unit test for function logger_level
def test_logger_level():
    import time
    import logging

    log = logging.getLogger(__name__)
    configure()

    with logger_level(log, logging.DEBUG):
        log.debug("1")
        time.sleep(0.1)
        log.debug("2")
    time.sleep(0.1)
    log.debug("3")


if __name__ == "__main__":
    import pytest
    pytest.main(__file__)

# Generated at 2022-06-14 06:25:54.097323
# Unit test for function get_config
def test_get_config():
    # Test the case of empty config
    assert get_config() is None
    # Test the case where config is set to a non-empty string
    assert get_config('1') == 1
    # Test the case where config is set as a json string
    assert get_config('{"a":"1"}') == {'a': '1'}
    # Test the case where config is set as a yaml string
    assert get_config('a: 1') == {'a': 1}

# Generated at 2022-06-14 06:26:04.770348
# Unit test for function logger_level
def test_logger_level():
    # Test
    logger_test = get_logger()

    # Check that log level is below the max value
    assert logger_test.level < sys.maxsize

    # Set the log level to the max value
    logger_test.level = sys.maxsize
    # Check that the log level has been modified
    assert logger_test.level == sys.maxsize

    # Set the new log level to logging.DEBUG
    with logger_level(logger_test, logging.DEBUG):
        assert logger_test.level == logging.DEBUG

    # Check that the log level has been restored to sys.maxsize
    assert logger_test.level == sys.maxsize


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:26:14.655481
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.INFO):
        logger.debug("[test_logger_level] This shouldn't appear")
        logger.info("[test_logger_level] This *should* appear")
        logger.warning("[test_logger_level] This *should* appear")
        logger.error("[test_logger_level] This *should* appear")
    logger.debug("[test_logger_level] This *should* appear")



# Generated at 2022-06-14 06:26:23.683719
# Unit test for function logger_level
def test_logger_level():
    # We need to actually test that the level was set, so we'll use the
    # default logger to do this. We don't care about changing the level
    # of the default logger, but we do want to make sure we change the level
    # in the with block.
    logger = get_logger()
    level_before = logger.level
    with logger_level(logger, logging.INFO):
        assert logger.level != level_before
    assert logger.level == level_before

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:39.351138
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    logger.level = logging.DEBUG
    assert logger.isEnabledFor(logging.DEBUG)
    with logger_level(logger, logging.WARN):
        assert not logger.isEnabledFor(logging.DEBUG)
    assert logger.isEnabledFor(logging.DEBUG)

if __name__ == '__main__':
    get_logger().info('test')

    get_logger('foo').info('test')

    get_logger('foo.bar').info('test')

    get_logger('foo.bar').error('test')

    get_logger('foo.bar').debug('test')

    get_logger('foo.bar').warning('test')

    test_logger_level()

# Generated at 2022-06-14 06:26:52.962086
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    with logger_level(logger, logging.WARNING):
        logger.debug('This message should not be logged')
        logger.info('This message should not be logged')
        logger.warning('This message should be logged')
        logger.error('This message should be logged')
        logger.critical('This message should be logged')

    logger.debug('This message should be logged')
    logger.info('This message should be logged')
    logger.warning('This message should be logged')
    logger.error('This message should be logged')
    logger.critical('This message should be logged')

    with logger_level(logger, logging.FATAL):
        logger.debug('This message should not be logged')
        logger.info('This message should not be logged')
        logger.warning('This message should not be logged')

# Generated at 2022-06-14 06:26:57.449521
# Unit test for function configure
def test_configure():
    import logging.config
    configure()
    log = get_logger()
    assert isinstance(log, logging.Logger)
    assert isinstance(log.handlers[0], logging.StreamHandler)



# Generated at 2022-06-14 06:27:00.660700
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.info('foo')
    log.info('bar')


# Generated at 2022-06-14 06:27:04.509171
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(name=__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('a debug message')
    logger.error('an error message')



# Generated at 2022-06-14 06:27:08.352485
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger('logger_level_test'), logging.INFO):
        assert logging.getLogger('logger_level_test').level == logging.INFO


# Generated at 2022-06-14 06:27:20.335520
# Unit test for function logger_level
def test_logger_level():
    # building fake logging
    class Record(object):
        def __init__(self):
            self.levelname = None
            self.name = None
            self.message = None
    class Logger(object):
        def __init__(self, level, *channels):
            self.level = level
            self.channels = channels
        def __call__(self, *channels):
            return Logger(self.level, *channels)
        def _log(self, level, **kwargs):
            record = Record()
            record.levelname = kwargs.get('levelname', None)
            record.name = kwargs.get('name', None)
            record.message = kwargs.get('message', None)
            for c in self.channels:
                c._log(record)

# Generated at 2022-06-14 06:27:32.815462
# Unit test for function logger_level

# Generated at 2022-06-14 06:27:37.522435
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.info("test_logger_level")


# Generated at 2022-06-14 06:27:42.076331
# Unit test for function get_config
def test_get_config():
    """
    >>> cfg = get_config(default={"level": "DEBUG"})
    >>> assert cfg['level'] == 'DEBUG'
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:27:48.521800
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger(), 'DEBUG'):
        assert getLogger().level == logging.DEBUG
    assert getLogger().level != logging.DEBUG



# Generated at 2022-06-14 06:28:01.180031
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    # Get a logger
    logger = get_logger('test_logger_level')

    # Check for a log and do a log
    with logger_level(logger, logging.CRITICAL):
        assert not logger.isEnabledFor(logging.DEBUG)
        assert logger.isEnabledFor(logging.CRITICAL)
        logger.critical("critical message")
        # noinspection PyMissingOrEmptyDocstring
        class Error(Exception):
            pass

        try:
            raise Error("This should not show up in the log")
        except Error:
            logger.critical("critical message", exc_info=1)


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:11.263825
# Unit test for function logger_level
def test_logger_level():
    import logging

    with logger_level(logging.getLogger(), logging.DEBUG):
        assert logging.getLogger().isEnabledFor(logging.DEBUG)
        assert not logging.getLogger().isEnabledFor(logging.INFO)

    with logger_level(logging.getLogger(), logging.INFO):
        assert not logging.getLogger().isEnabledFor(logging.DEBUG)
        assert logging.getLogger().isEnabledFor(logging.INFO)

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)

# Generated at 2022-06-14 06:28:14.835609
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test')
    with logger_level(log, logging.DEBUG):
        log.debug('test')
    log.info('test')


log_info = get_logger().info



# Generated at 2022-06-14 06:28:23.371821
# Unit test for function configure
def test_configure():
    import json

    default_config = json.dumps(DEFAULT_CONFIG)

    # Test bad config
    bad_config = 'bad config'
    with pytest.raises(ValueError):
        configure(bad_config)

    # Test passing dictionary config
    cfg = dict(version=1)
    configure(cfg)

    # Test passing json config
    cfg = default_config
    configure(cfg)

    # Test passing config file path
    with tempfile.NamedTemporaryFile('w+') as f:
        cfg = f.name
        f.write(default_config)
        f.seek(0)
        configure(cfg)

    # Test passing yaml config
    import yaml
    cfg = yaml.dump(DEFAULT_CONFIG)
    configure(cfg)



# Generated at 2022-06-14 06:28:35.812813
# Unit test for function logger_level
def test_logger_level():
    import pytest
    from pytest import approx
    from datetime import datetime
    from io import StringIO
    import time
    import sys

    import logging
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    log = logging.getLogger(__name__)

    now1 = datetime.now().timestamp()
    with logger_level(log, logging.WARNING):
        log.info(1)
        log.warning(2)
    now2 = datetime.now().timestamp()
    log.info(3)
    now3 = datetime.now().timestamp()

    assert now3 > now2
    assert now2 > now1

    # Ensure that the first info message is printed after the warning message
    # This can fail if the test runs on a slow computer, in which case we

# Generated at 2022-06-14 06:28:43.876038
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import StringIO

    class TestLoggerLevel(unittest.TestCase):
        def test_logger_level(self):
            log_output = StringIO.StringIO()
            log = getLogger(__name__)
            level = logging.INFO
            log.setLevel(level)
            ch = logging.StreamHandler(log_output)
            log.addHandler(ch)
            log.setLevel(logging.DEBUG)
            log.debug('This should be displayed')
            log.warning('This should also be displayed')
            with logger_level(log, logging.WARNING):
                log.debug('This should not be displayed')
                log.warning('This should be displayed')
            # Check that logger is back to initial level
            log.debug('This should be displayed')

# Generated at 2022-06-14 06:28:51.855166
# Unit test for function get_config
def test_get_config():
    config = get_config(config=None, env_var=None, default=None)
    assert config == {}

    config = get_config(config=None, env_var='LOGGING', default=None)
    assert config == {}

    config = get_config(
        config={"version": 1},
        env_var=None,
        default=None
    )
    assert config == {"version": 1}


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:28:56.989209
# Unit test for function logger_level
def test_logger_level():
    l = get_logger('test_logger_level')
    l.setLevel(logging.WARNING)
    l.debug('this should not be printed')
    with logger_level(l, logging.DEBUG):
        l.debug('this should be printed')
    l.debug('this should not be printed')
    

# Generated at 2022-06-14 06:29:07.820581
# Unit test for function logger_level
def test_logger_level():
    import unittest

    import logging
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()

    class TestLoggerLevel(unittest.TestCase):
        def test_no_logger_before(self):
            with logger_level(log, logging.ERROR):
                self.assertFalse(log.isEnabledFor(logging.INFO))
                self.assertTrue(log.isEnabledFor(logging.ERROR))
                self.assertFalse(log.isEnabledFor(logging.DEBUG))

            self.assertTrue(log.isEnabledFor(logging.INFO))
            self.assertFalse(log.isEnabledFor(logging.ERROR))
            self.assertFalse(log.isEnabledFor(logging.DEBUG))


# Generated at 2022-06-14 06:29:17.340953
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
    assert logger.getEffectiveLevel() == logging.DEBUG



# Generated at 2022-06-14 06:29:30.577934
# Unit test for function get_config
def test_get_config():
    # test for get_config when giving a string
    assert get_config('{"a": 3}') == {'a': 3}
    assert get_config('{"a": 3, "b": "str"}') == {'a': 3, 'b': 'str'}
    assert get_config('{"a": {"b": "c"}}') == {'a': {'b': 'c'}}

    # test for get_config when giving a dict
    assert get_config({'a': 3}) == {'a': 3}
    assert get_config({'a': 3, 'b': 'str'}) == {'a': 3, 'b': 'str'}
    assert get_config({'a': {'b': 'c'}}) == {'a': {'b': 'c'}}

    # test for get_config

# Generated at 2022-06-14 06:29:41.643879
# Unit test for function configure
def test_configure():
    import tempfile

    fd, path = tempfile.mkstemp()

# Generated at 2022-06-14 06:29:47.232700
# Unit test for function logger_level
def test_logger_level():
    # default level is INFO
    _ensure_configured()
    logger = get_logger()
    assert logger.level is logging.INFO

    # set level in context manager
    with logger_level(logger, logging.ERROR):
        assert logger.level is logging.ERROR

    # level is restored after context manager
    assert logger.level is logging.INFO


# Generated at 2022-06-14 06:29:52.366366
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.debug("Test 1")
    assert logger.isEnabledFor(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        logger.debug("Test 2")
        assert not logger.isEnabledFor(logging.DEBUG)


# Generated at 2022-06-14 06:30:05.370746
# Unit test for function get_config

# Generated at 2022-06-14 06:30:09.970747
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.WARN):
        logger.debug('this one should not show up')
        logger.warn('this one should show up')
    logger.debug('this one should show up')

# Generated at 2022-06-14 06:30:15.400212
# Unit test for function logger_level
def test_logger_level():
    conf = logging.getLoggerConfiguration()
    with logger_level(logging.getLogger(), logging.CRITICAL):
        assert logging.getLogger().level == logging.CRITICAL
    assert logging.getLogger().level == conf.get('root').get('level')



# Generated at 2022-06-14 06:30:18.951485
# Unit test for function configure
def test_configure():
    # Should not raise an exception
    configure()
    # Should not raise an exception
    configure({'loggers': {'test_configure': {'level': logging.DEBUG}}})



# Generated at 2022-06-14 06:30:28.412022
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    with logger_level(logger,logging.WARNING):
        logger.warning('WARNING-1')
        logger.error('ERROR-1')
        logger.debug('DEBUG-1')
    logger.warning('WARNING-2')
    logger.error('ERROR-2')
    logger.debug('DEBUG-2')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:30:50.088102
# Unit test for function logger_level
def test_logger_level():
    import logging.config
    import logging

    configuration={
        'version': 1,
        'formatters': {
            'standard': {'format': '%(name)s:%(message)s'}
        },
        'handlers': {
            'console': {'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': logging.DEBUG
            }
        },
        'loggers': {
            'a_logger': {'handlers': ['console'],
                'level': logging.DEBUG
            }
        }
    }
    logging.config.dictConfig(configuration)
    logger = logging.getLogger('a_logger')
    logger.debug("Initial logging level: {}".format(logger.level))


# Generated at 2022-06-14 06:31:02.870715
# Unit test for function get_config
def test_get_config():
    ''' Unit test for function get_config '''
    from pprint import pformat
    
    # Read the logging configuration file in source code directory
    logging_config_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'logging.yaml'
    )
    with open(logging_config_file, 'r') as f:
        config_file_contents = f.read()
    
    # Test bare logging config

# Generated at 2022-06-14 06:31:05.794303
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    logger.info('This line should be logged')
    with logger_level(logger, logging.DEBUG):
        logger.debug('This line should be logged')
    logger.debug('This line should not be logged')



# Generated at 2022-06-14 06:31:11.450653
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    assert logger.level == logging.NOTSET

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.NOTSET



# Generated at 2022-06-14 06:31:16.911278
# Unit test for function configure
def test_configure():
    configure()
    logger = logging.getLogger('test')
    logger.info('test')


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:31:25.681924
# Unit test for function logger_level
def test_logger_level():
    import pytest
    sio = io.StringIO()
    fmt = '%(name)s|%(levelname)s|%(message)s'
    logging.basicConfig(stream=sio, level=logging.DEBUG, format=fmt)
    log = logging.getLogger('test_logger_level')
    log.info('_test_')
    with logger_level(log, logging.ERROR):
        log.info('recursive_test_')
        with logger_level(log, logging.INFO):
            log.info('recursive_test_')
    log.info('_test_end_')
    log_contents = sio.getvalue()
    # Note that test does not properly simulate outputs of different threads.

# Generated at 2022-06-14 06:31:35.225814
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> root = logging.getLogger()
    >>> root.setLevel(logging.DEBUG)
    >>> logger = logging.getLogger('test')
    >>> logger.info('yo')
    yo
    >>> with logger_level(logger, logging.DEBUG):
    ...     logger.debug('hide me')
    ...     with logger_level(logger, logging.WARN):
    ...         logger.debug('hide me too')
    ...         logger.warn('show me')
    ...     logger.debug('show me again')
    hide me
    show me again
    """

# Generated at 2022-06-14 06:31:40.657605
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("test_logger_level")
    with logger_level(logger, logging.DEBUG):
        logger.debug("debug log")
        logger.info("info log")
    logger.debug("debug log")

# Generated at 2022-06-14 06:31:49.076115
# Unit test for function logger_level
def test_logger_level():
    import mock
    import sys
    import io

    logger = get_logger()
    with mock.patch.object(sys.stdout, "write") as mock_stdout_write:
        with logger_level(logger, logging.DEBUG):
            logger.debug("test_debug")
            logger.info("test_info")
        logger.info("test_info_noc")

    assert mock_stdout_write.called



# Generated at 2022-06-14 06:31:53.672312
# Unit test for function logger_level
def test_logger_level():

    # setup
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logger = logging.getLogger(__name__)

    # test
    with logger_level(logger, logging.CRITICAL):
        logger.debug("debug message")  # should be silent
        logger.info("info message")    # should be silent
        logger.critical("critical message") # should not be silent

    # teardown
    del logging.Logger.manager.loggerDict[__name__]


# Generated at 2022-06-14 06:32:14.494066
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger()
    with logger_level(l, logging.CRITICAL):
        assert l.level == logging.CRITICAL
    assert l.level == logging.NOTSET

# Generated at 2022-06-14 06:32:20.822617
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.critical('critical')
        logger.error('error')
        logger.warning('warning')
        logger.info('info')
        logger.debug('debug')


# Generated at 2022-06-14 06:32:27.244529
# Unit test for function logger_level
def test_logger_level():
    import pickle

    def foo():
        log = get_logger()
        with logger_level(log, logging.CRITICAL):
            pickle.dump(log, sys.stdout)
    foo()

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:32:29.652516
# Unit test for function get_config
def test_get_config():
    cfg = get_config(None, None, DEFAULT_CONFIG)

# Generated at 2022-06-14 06:32:45.005754
# Unit test for function logger_level
def test_logger_level():
    # Create a logger
    logger = get_logger('Test logger_level')

    # Set initial level
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

    # Configure level
    with logger_level(logger, logging.DEBUG):

        # Check debug level
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')

    # Check initial level
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

# Generated at 2022-06-14 06:32:50.210594
# Unit test for function logger_level
def test_logger_level():
    try:
        log = get_logger()
        wlog = get_logger('test_logger_level')

        for l in ['debug', 'info', 'warning', 'error', 'critical', 'disable']:
            with logger_level(wlog, l):
                getattr(wlog, l)('%s level works', l)
                getattr(log, l)('%s level works', l)

        log.debug('logger_level: PASSED')
    except Exception as e:
        log.exception('logger_level: FAILED')


# Generated at 2022-06-14 06:32:57.135225
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.INFO):
        assert log.isEnabledFor(logging.INFO)
        assert not log.isEnabledFor(logging.DEBUG)
    assert log.isEnabledFor(logging.DEBUG)
    assert not log.isEnabledFor(logging.INFO)



# Generated at 2022-06-14 06:33:05.663332
# Unit test for function logger_level
def test_logger_level():
    import logging
    import StringIO

    buf = StringIO.StringIO()

    # Start of captured region
    h = logging.StreamHandler(buf)
    logger = logging.getLogger("logger level test")
    logger.addHandler(h)
    logger.setLevel(logging.WARN)
    assert logger.getEffectiveLevel() == logging.WARN

    with logger_level(logger, logging.INFO):
        assert logger.getEffectiveLevel() == logging.INFO
        logger.info("Hello world")

    assert logger.getEffectiveLevel() == logging.WARN
    logger.info("Hello world")
    # End of captured region

    assert buf.getvalue() == "Hello world\n"

# Generated at 2022-06-14 06:33:10.854976
# Unit test for function logger_level
def test_logger_level():
    logger_test = getlogger("test")
    with logger_level(logger_test, logging.DEBUG):
        logger_test.debug("test")
    logger_test.debug("test")
    assert True



# Generated at 2022-06-14 06:33:19.103601
# Unit test for function logger_level
def test_logger_level():
    # This is a silly test.
    logger = get_logger()
    logger.warning("Warning before level change")
    logger.debug("Debug before level change")
    with logger_level(logger, logging.DEBUG):
        logger.debug("Debug after level change")
        logger.warning("Warning after level change")
    logger.debug("Debug after level change back")
    logger.warning("Warning after level change back")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:33:46.314831
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    # The test will pass if the log message is written
    with logger_level(logger, logging.DEBUG):
        logger.info('test logger_level')

    # The test will fail if the log message is written
    with logger_level(logger, logging.INFO):
        logger.debug('test logger_level')


# This is used by log.py and called from the root.
# It should be called only once and will be called before
# any other logging is used.
# It is not meant to be called from client code.

# Generated at 2022-06-14 06:33:56.593188
# Unit test for function get_config
def test_get_config():

    # get_config(given=None, env_var=None, default=None):
    assert get_config() is None

    # get_config(given=None, env_var=None, default=None):
    assert get_config(default=dict(a=1)) == {'a': 1}

    # get_config(given=None, env_var=None, default=None):
    os.environ['LOGGING'] = json.dumps({'a': 2})
    assert get_config(env_var='LOGGING') == {'a': 2}

    # get_config(given=None, env_var=None, default=None):
    os.environ['LOGGING'] = '{"a": 3}'
    assert get_config(env_var='LOGGING') == {'a': 3}

# Generated at 2022-06-14 06:34:01.517717
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.ERROR):
        logger.info('this should not be logged')
    logger.debug('this should be logged')

if __name__ == '__main__':
    # Run unit tests
    test_logger_level()

# Generated at 2022-06-14 06:34:06.051966
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger(__name__)
    level = logger.level

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG

    assert logger.level == level

# Generated at 2022-06-14 06:34:08.301878
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.DEBUG):
        logging.debug('test')

# Generated at 2022-06-14 06:34:12.012001
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, logging.NOTSET):
        logger.debug('debug')
        logger.info('info')
    with logger_level(logger, logging.ERROR):
        logger.debug('debug')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug')
        logger.info('info')

# Generated at 2022-06-14 06:34:17.898175
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger("Test logger_level")
    logger.setLevel(logging.DEBUG)
    with logger_level(logger,logging.WARN):
        assert logger.level == logging.WARN
        logger.debug("logger is at level debug")

# Generated at 2022-06-14 06:34:23.515670
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.NOTSET

if __name__ == '__main__':
    import nose

    nose.runmodule()

# Generated at 2022-06-14 06:34:33.093624
# Unit test for function get_config
def test_get_config():
    import copy
    import logging.config
    import yaml

    # Test defaults
    cfg = get_config()
    assert isinstance(cfg, dict)
    logging.config.dictConfig(cfg)
    logging.getLogger().info('test')

    # Test explicitly passing dict

# Generated at 2022-06-14 06:34:36.778133
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug('Test')
    with logger_level(logger, logging.INFO):
        logger.debug('Test')

# Generated at 2022-06-14 06:35:05.251054
# Unit test for function logger_level
def test_logger_level():
    from contextlib import contextmanager
    from logging import getLogger, INFO

    @contextmanager
    def is_logger_info_enabled(logger):
        initial = logger.level
        logger.level = INFO
        try:
            yield
        finally:
            logger.level = initial

    logger = getLogger()
    logger.debug('info level is off')
    with is_logger_info_enabled(logger):
        logger.debug('info level is on')
        with logger_level(logger, INFO):
            logger.debug('info level is on')
        logger.debug('info level is on')
    logger.debug('info level is off')



# Generated at 2022-06-14 06:35:08.260165
# Unit test for function configure
def test_configure():
    configure()
    logger = get_logger(__name__)
    logger.info("test_configure")
