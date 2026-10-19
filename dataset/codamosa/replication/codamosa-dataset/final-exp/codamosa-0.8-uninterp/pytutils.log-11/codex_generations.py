

# Generated at 2022-06-14 06:25:15.566763
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)

    # initial level of logger is 'WARN'
    logger.info('logger should not print this')
    logger.warning('logger should print this')
    with logger_level(logger, logging.INFO):
        logger.info('logger should print this now')
        logger.warning('logger should print this now')
    logger.info('logger should not print this')
    logger.warning('logger should print this')


# Generated at 2022-06-14 06:25:20.153706
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug('debug message')
    log.info('info message')
    with logger_level(log, logging.INFO):
        log.debug('debug message')
        log.info('info message')
    log.debug('debug message')
    log.info('info message')


# Generated at 2022-06-14 06:25:25.538700
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger("logger_level")
    configure()
    log.info("TEST 1")
    with logger_level(log, logging.DEBUG):
        log.info("TEST 2")
        with logger_level(log, logging.WARNING):
            log.info("TEST 3")
        log.info("TEST 4")
    log.info("TEST 5")

# Generated at 2022-06-14 06:25:28.557440
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig()
    logger = logging.getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level != logging.DEBUG

# Generated at 2022-06-14 06:25:32.966874
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__ + '.test')
    logger.error('test error')
    with logger_level(logger, logging.DEBUG):
        logger.debug('test debug')
        logger.info('test info')
    logger.error('test error')

# Generated at 2022-06-14 06:25:40.912937
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()

    with logger_level(l, logging.WARNING):
        l.debug('blah')
        l.info('blah')
        l.warning('blah')  # Should show up
        l.error('blah')
        l.critical('blah')

    l.debug('blah')
    l.info('blah')
    l.warning('blah')
    l.error('blah')
    l.critical('blah')

# Generated at 2022-06-14 06:25:49.925598
# Unit test for function get_config
def test_get_config():
    import json
    # config=None env_var=None default=None
    cfg = get_config()
    assert cfg == DEFAULT_CONFIG

    # config=None env_var='LOGGING' default=DEFAULT_CONFIG
    os.environ['LOGGING'] = json.dumps({})
    cfg = get_config(env_var='LOGGING')
    assert cfg == {}

    # config=None env_var='LOGGING' default=DEFAULT_CONFIG
    os.environ['LOGGING'] = json.dumps({'loggers':{'requests':{'level':logging.DEBUG}}})
    cfg = get_config(env_var='LOGGING')
    assert cfg['loggers']['requests']['level'] == logging.DEBUG

    #

# Generated at 2022-06-14 06:25:55.182298
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    for lvl in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        logger.warning("Logger level = " + lvl)
        with logger_level(logger, logging.__dict__[lvl]):
            logger.warning("Inner logger level = " + lvl)


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:59.004895
# Unit test for function logger_level
def test_logger_level():

    log = get_logger()
    with logger_level(log, logging.INFO):
        assert log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.INFO)

# Generated at 2022-06-14 06:26:07.156840
# Unit test for function logger_level
def test_logger_level():
    """
    >>> test_logger_level()
    INFO - test_logger_level - info
    WARNING - test_logger_level - warning
    ERROR - test_logger_level - error
    """
    import logging
    logger = logging.getLogger('test_logger_level')
    logger.setLevel(logging.DEBUG)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    with logger_level(logger, logging.INFO):
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

# Generated at 2022-06-14 06:26:24.683368
# Unit test for function logger_level
def test_logger_level():
    import mock

    logging.config.dictConfig({'loggers': {'test': {'level': 'INFO'}}})
    l = logging.getLogger('test')
    l._log = mock.MagicMock()

    l.info('info1')
    assert l._log.call_args[0][0] == logging.INFO
    l.debug('debug1')
    assert l._log.call_args is None

    with logger_level(l, logging.DEBUG):
        l.info('info2')
        assert l._log.call_args[0][0] == logging.INFO
        l.debug('debug2')
        assert l._log.call_args[0][0] == logging.DEBUG

    l.info('info3')
    assert l._log.call_args[0][0] == logging.INFO

# Generated at 2022-06-14 06:26:34.335468
# Unit test for function logger_level
def test_logger_level():
    # This line is necessary since logger_level uses get_logger which in turn uses
    # _namespace_from_calling_context which relies on inspect.stack
    __name__ = '__main__'

    logger = get_logger()

    logger.warn('Warning!')

    with logger_level(logger, logging.DEBUG):
        logger.debug('Debug should print')

    logger.debug('Debug should not print')



if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:41.635637
# Unit test for function configure
def test_configure():
    import os
    import tempfile
    import json


# Generated at 2022-06-14 06:26:44.615436
# Unit test for function get_config
def test_get_config():
    print(get_config(os.environ.get('LOGGING')))

if __name__ == '__main__':
    test_get_config()

# Generated at 2022-06-14 06:26:52.484453
# Unit test for function get_config
def test_get_config():
    # Config provided as file
    if os.environ.get('TRAVIS'):
        os.environ['LOGGING'] = 'tests/data/logging_sample.conf'
    else:
        os.environ['LOGGING'] = 'tests/data/logging_sample.json'
    assert get_config(env_var='LOGGING') == DEFAULT_CONFIG

    # Config provided as path
    os.environ['LOGGING'] = 'tests/data/logging_sample.json'
    assert get_config(env_var='LOGGING') == DEFAULT_CONFIG

    # Config provided as string
    os.environ['LOGGING'] = '{"version": 1}'
    assert get_config(env_var='LOGGING') == {'version': 1}



# Generated at 2022-06-14 06:26:59.227295
# Unit test for function logger_level
def test_logger_level():
    test_logger = get_logger('logger_level')
    test_logger.info("logger_level test")
    with logger_level(test_logger, logging.ERROR):
        test_logger.info("Shouldn't appear")
        test_logger.error("This will appear")
    test_logger.info("This will appear")

# Generated at 2022-06-14 06:27:12.936277
# Unit test for function get_config
def test_get_config():
    # Invalid config
    with pytest.raises(ValueError):
        get_config(config = None)

    # Given parameter is a str
    config = get_config(config = "{'foo': 'bar'}")
    assert config == {'foo': 'bar'}

    # Given parameter is a dict
    config = get_config(config = {'foo': 'bar'})
    assert config == {'foo': 'bar'}

    config = get_config(config = {'foo': 'bar'}, env_var = "LOGGING")
    assert config == {'foo': 'bar'}

    env_var = 'LOGGING'
    with mock.patch.dict(os.environ, {env_var: '{"foo": "bar"}'}):
        config = get_config(default = {})
       

# Generated at 2022-06-14 06:27:23.653635
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.handlers
    import sys
    logger = logging.getLogger('test')
    logger.setLevel(logging.ERROR)
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:27:29.535941
# Unit test for function logger_level
def test_logger_level():
    import logging

    l = logging.getLogger('test_logger')
    assert l.level == logging.NOTSET

    with logger_level(l, logging.DEBUG):
        assert l.level == logging.DEBUG

    assert l.level == logging.NOTSET

# Generated at 2022-06-14 06:27:34.634593
# Unit test for function get_config
def test_get_config():
    # Notice that the second argument of get_config is not used in this test.

    # Test string as config.
    cfg_str = '{"version": 1}'
    assert get_config(cfg_str) == {"version": 1}

    # Test dict as config.
    cfg_dict = {"version": 1}
    assert get_config(cfg_dict) == {"version": 1}



# Generated at 2022-06-14 06:27:44.034227
# Unit test for function configure
def test_configure():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')



# Generated at 2022-06-14 06:27:48.008365
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.INFO):
        logger.debug('Expected to see nothing')
        logger.info('Expected to see something')


# Generated at 2022-06-14 06:27:56.207440
# Unit test for function logger_level
def test_logger_level():
    """
    >>> test_logger_level()
    """
    log = getLogger(__name__)
    assert log.isEnabledFor(logging.INFO)
    assert log.isEnabledFor(logging.DEBUG)
    with logger_level(log, logging.INFO):
        assert not log.isEnabledFor(logging.DEBUG)
    assert log.isEnabledFor(logging.DEBUG)



# Generated at 2022-06-14 06:28:05.435430
# Unit test for function logger_level
def test_logger_level():
    """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
    from contextlib import contextmanager
    
    logger = logging.getLogger('test_logger_level')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    
    @contextmanager
    def logger_level(logger, level):
        """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
        initial = logger.level
        logger.level = level
        try:
            yield
        finally:
            logger.level = initial
            
    with logger_level(logger, logging.CRITICAL):
        logger.debug('should not be seen')
        logger.warn

# Generated at 2022-06-14 06:28:19.083286
# Unit test for function get_config
def test_get_config():
    from pprint import pprint
    from json import dumps

    tests = [
        # (key, config, expected)
        (None, '{"a":2}', dict(a=2)),
        (None, '{"a":40}', dict(a=40)),
        (None, dumps({'a': 2}), dict(a=2)),
        (None, dumps({'b': 3}), dict(b=3)),
        ('LOGGING', dict(a=2), dict(a=2)),
        ('LOGGING', dict(b=3), dict(b=3)),
    ]

    for k, c, e in tests:
        print('#'*80)
        print('\n')
        v = get_config(config=c, env_var=k)
        print(repr(k))
       

# Generated at 2022-06-14 06:28:22.238415
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("test_logger_level")
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:28:24.010751
# Unit test for function configure
def test_configure():
    configure()

# Generated at 2022-06-14 06:28:28.959339
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    log.info('test')
    logger_level(log, logging.DEBUG)
    log.info('test')
    with logger_level(log, logging.DEBUG):
        log.info('test')
    log.info('test')

# Generated at 2022-06-14 06:28:32.852906
# Unit test for function logger_level
def test_logger_level():
    """Test function logger_level.

    Side effects:
        - overrides configured logger level
    """
    def get_logger_level(logger):
        return logging._checkLevel(logger.level)
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert get_logger_level(logger) == 10
    assert get_logger_level(logger) == 30



# Generated at 2022-06-14 06:28:36.392722
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level != logging.DEBUG
    logging.debug('This should be logged, as we just set level to DEBUG...')

# Generated at 2022-06-14 06:28:48.189538
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.INFO

# Generated at 2022-06-14 06:28:52.731878
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        logger.info("hello")
        logger.debug("world")
    logger.debug("goodbye")
    logger.info("world")



# Generated at 2022-06-14 06:29:03.732433
# Unit test for function get_config
def test_get_config():
    config = get_config(r'{"version": 1, "formatters": {"simple": {"format": "%(asctime)s| %(name)-35s %(message)s @%(funcName)s:%(lineno)d #%(levelname)s", "datefmt": "%Y-%m-%d %H:%M:%S"}}}')
    assert config == {'version': 1, 'formatters': {'simple': {'format': '%(asctime)s| %(name)-35s %(message)s @%(funcName)s:%(lineno)d #%(levelname)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}}}


if __name__ == "__main__":
    import doctest
    doctest

# Generated at 2022-06-14 06:29:05.570174
# Unit test for function get_config
def test_get_config():
    config = get_config()
    assert config['version'] == 1

# Generated at 2022-06-14 06:29:12.330577
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        log.debug('debug message')
        log.info('info message')
        log.warning('warning message')
        log.error('error message')
        log.critical('critical message')


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:29:17.680967
# Unit test for function configure
def test_configure():
    cfg = configure()
    assert cfg is not None


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    print(get_logger('test').level)

# Generated at 2022-06-14 06:29:30.578228
# Unit test for function logger_level
def test_logger_level():
    import StringIO
    import logging
    import support, sys

    # This test doesn't do a great job of testing things.
    # It needs to be reworked.  The basic idea is to
    # make sure that a particular level of data gets logged
    # when that level is set.

    # create a logger
    logger = logging.getLogger('test')
    logger.propagate = False
    stream = StringIO.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug('This is a debug log message')
    logger.info('This is an info log message')
    logger.warn('This is a warn log message')
    support.unlink(support.TESTFN)

# Generated at 2022-06-14 06:29:41.643780
# Unit test for function logger_level
def test_logger_level():
    """Unit test for function logger_level."""
    import io
    import subprocess

    with io.StringIO() as stream_handler:
        logger = logging.getLogger()
        handler = logging.StreamHandler(stream_handler)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        with logger_level(logger, logging.DEBUG):
            logger.debug('debug message')
            logger.info('info message')

        logger.info('info message')

        assert stream_handler.getvalue() == 'info message\n'

    value = subprocess.check_output(['python', '-m', 'pylog'])
    assert value.decode('utf-8').strip() == 'debug message'



# Generated at 2022-06-14 06:29:50.063509
# Unit test for function logger_level
def test_logger_level():
    import logging

    logging.basicConfig()
    logger = logging.getLogger(__name__)

    def check_log_level(level):
        return level == logger.getEffectiveLevel()

    logger.setLevel(logging.DEBUG)
    assert check_log_level(logging.DEBUG)

    with logger_level(logger, logging.INFO):
        assert check_log_level(logging.INFO)

    assert check_log_level(logging.DEBUG)


if __name__ == '__main__':
    configure()
    log = getLogger(__name__)
    log.debug('test')

    test_logger_level()

# Generated at 2022-06-14 06:30:03.483224
# Unit test for function configure
def test_configure():
    import json
    import tempfile
    logging.raiseExceptions = False
    # Test default config
    configure()
    # Test json config
    with tempfile.NamedTemporaryFile() as configfile:
        json.dump({'disable_existing_loggers': False}, configfile)
        configure(configfile.name)
    with tempfile.NamedTemporaryFile() as configfile:
        json.dump({'disable_existing_loggers': True}, configfile)
        configure(configfile.name)
    with tempfile.NamedTemporaryFile() as configfile:
        json.dump({}, configfile)
        configure(configfile.name)
    # Test invalid config
    configure({'disable_existing_loggers': 'test'})
    configure(json.dumps({'disable_existing_loggers': False}))



# Generated at 2022-06-14 06:30:30.782086
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> logging.getLogger("omni").setLevel(logging.INFO)
    >>> logger = logging.getLogger("omni.utils")
    >>> logger.setLevel(logging.ERROR)
    >>> logger.error("This must be logged")
    >>> logger.info("This must be ignored")
    >>> assert logger.level == logging.ERROR
    >>> with logger_level(logger, logging.INFO):
    ...     logger.info("This must be logged")
    ...     assert logger.level == logging.INFO
    ...
    >>> assert logger.level == logging.ERROR

    """
    pass

# Generated at 2022-06-14 06:30:40.124280
# Unit test for function logger_level
def test_logger_level():
    import time

    logger = logging.getLogger(__name__)
    logfile = 'output.log'
    handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=10, backupCount=2)
    logger.addHandler(handler)

    with logger_level(logger, logging.DEBUG):
        logger.debug('Starting: test_logger_level')

    with logger_level(logger, logging.INFO):
        logger.info('Dummy log')

    with logger_level(logger, logging.CRITICAL):
        logger.warning('This should not be logged')

    logger.info('This should be logged')

    with logger_level(logger, logging.CRITICAL):
        logger.info('This should be logged')

    with logger_level(logger, logging.DEBUG):
        logger

# Generated at 2022-06-14 06:30:42.714558
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug("debug")
        log.info("info")
        log.warning("warning")
    log.debug("debug")
    log.info("info")
    log.warning("warning")



# Generated at 2022-06-14 06:30:54.335750
# Unit test for function configure
def test_configure():
    from pytest import raises
    from io import StringIO

    logging.getLogger().handlers = []
    log = get_logger('test')
    log.info("yay")
    assert len(logging.getLogger().handlers) == 1, \
        "Logger should have 1 default handler ({})".format(len(logging.getLogger().handlers))

    log = get_logger('test2')
    log.info("yay")
    assert len(logging.getLogger().handlers) == 1, \
        "Logger should still have 1 default handler ({})".format(len(logging.getLogger().handlers))

    with raises(ValueError) as excinfo:
        configure(config=None)
    assert str(excinfo.value) == "Invalid logging config: None"

   

# Generated at 2022-06-14 06:31:05.462612
# Unit test for function get_config

# Generated at 2022-06-14 06:31:13.554895
# Unit test for function logger_level
def test_logger_level():
    """Test logger_level function: replace the logger by a Mock object."""
    from collectd_logger import logger_level
    from mock import Mock

    log = Mock()
    with logger_level(log, "INFO"):
        pass  # run the code that uses log with log level set to INFO
    log.setLevel.assert_called_with("INFO")

# test_logger_level()

# Generated at 2022-06-14 06:31:16.794590
# Unit test for function logger_level
def test_logger_level():
    # Setup
    logger = get_logger()
    # Test
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    # Teardown

# Generated at 2022-06-14 06:31:23.477959
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger()
    assert logger.level == logging.NOTSET, "Expected default level to be NOTSET"
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG, "Expected new level to be DEBUG"
    assert logger.level == logging.NOTSET, "Expected level to have restored to NOTSET"

# Generated at 2022-06-14 06:31:36.383929
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)s [%(name)s] %(message)s'
            }
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            }
        },
        'loggers': {
            'test': {
                'handlers': ['default']
            }
        }
    }

    configure(config=config)

    # test
    with logger_level(logger, logging.DEBUG):
        logger.debug('test log')
        assert logger.getEffectiveLevel() == logging.DEBUG

# Generated at 2022-06-14 06:31:40.474807
# Unit test for function get_config
def test_get_config():
    """
    :return:
    """
    config=get_config()
    assert config.get('formatters')


# Generated at 2022-06-14 06:32:04.523021
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    for initial_level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        for desired_level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            with logger_level(logger, desired_level):
                assert logger.level == desired_level
            assert logger.level == initial_level



# Generated at 2022-06-14 06:32:11.721145
# Unit test for function configure
def test_configure():
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))


# Generated at 2022-06-14 06:32:19.580344
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.DEBUG):
        logging.getLogger().debug("debug message")
    try:
        with logger_level(logging.getLogger(), logging.DEBUG):
            logging.getLogger().debug("debug message")
        raise Exception("Failed to catch exception")
    except Exception:
        pass
    finally:
        logging.basicConfig()

# Generated at 2022-06-14 06:32:25.027411
# Unit test for function logger_level
def test_logger_level():
    log=get_logger(__name__)
    log.info('before setting logger level')
    with logger_level(log, logging.WARN):
        log.debug('this should not be logged')
    log.debug('this should be logged')


# Generated at 2022-06-14 06:32:28.993193
# Unit test for function logger_level
def test_logger_level():
    from contextlib import nullcontext

    with logger_level(logging.getLogger(), logging.WARN), nullcontext():
        assert logging.getLogger().level == logging.WARN

    # Verify that logger level is set back to DEBUG after the context closes
    assert logging.getLogger().level == logging.DEBUG

# Generated at 2022-06-14 06:32:33.588855
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:32:47.779942
# Unit test for function get_config
def test_get_config():
    from .utils import capture_logging

    with capture_logging(level='DEBUG') as log:
        # test of given None
        assert get_config(config=None, env_var=None, default=None) == None
        assert get_config(config=None, env_var='LOGGING', default=DEFAULT_CONFIG) == DEFAULT_CONFIG

        # test of given dict
        assert get_config(config=DEFAULT_CONFIG, env_var='LOGGING', default=DEFAULT_CONFIG) == DEFAULT_CONFIG
        assert get_config(config=DEFAULT_CONFIG, env_var=None, default=None) == DEFAULT_CONFIG

        # test of given str

# Generated at 2022-06-14 06:33:02.285527
# Unit test for function logger_level
def test_logger_level():
    """Test the `logger_level` context manager."""
    print('\ntest_logger_level:')
    logger = getLogger('test_logger_test_logger_level')
    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
        logger.debug('I am overriden by logger_level to ERROR')
        logger.error('E, this is the one that shows up')

    assert logger.level == logging.DEBUG
    logger.info('I am [INFO] and I should show up')

if __name__ == '__main__':
    configure()
    print('\ntest_get_logger:')
    get_logger().info('testing...')

# Generated at 2022-06-14 06:33:09.854427
# Unit test for function get_config
def test_get_config():
    config = get_config(config='{"a": 1}')
    assert config == {"a": 1}

    config = get_config(config='{"a": 1}', env_var=None)
    assert config == {"a": 1}

    os.environ['LOGGING'] = '{"a": 1}'
    config = get_config(config=None, env_var='LOGGING')
    assert config == {"a": 1}
    del os.environ['LOGGING']

    config = get_config(config=None, env_var=None, default='{"a": 1}')
    assert config == {"a": 1}

    config = get_config(config=None, env_var=None, default={'a': 1})
    assert config == {"a": 1}


# Generated at 2022-06-14 06:33:17.050186
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    # If no config is provided, info messages should not be displayed
    log.info('Should not be displayed')

    # If a config is provided, debug messages should be displayed
    with logger_level(log, logging.DEBUG):
        log.debug('Should be displayed')

    # info messages should still not be displayed
    log.info('Should not be displayed')

# Generated at 2022-06-14 06:33:57.441736
# Unit test for function get_config
def test_get_config():
    assert get_config(env_var='LOGGING', default=DEFAULT_CONFIG) == DEFAULT_CONFIG

# Generated at 2022-06-14 06:34:07.093376
# Unit test for function logger_level
def test_logger_level():
    from colorlog import ColoredFormatter

    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logger = logging.getLogger('test')
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(ColoredFormatter())
    logger.addHandler(ch)
    try:
        with logger_level(logger, logging.ERROR):
            logger.debug("This message won't show")

        logger.debug("This message will show")
    except Exception as e:
        print("test_logger_level failed with: ", e)


# Generated at 2022-06-14 06:34:14.055277
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    with tempfile.TemporaryFile(mode='w+') as f:
        log = get_logger('added')
        log.propagate = False
        h = logging.StreamHandler(f)
        log.addHandler(h)

        with logger_level(log, logging.WARN):
            log.debug('debug')
            log.info('info')
            log.warn('warn')
            log.error('error')

            log.info('info')

        log.info('info')
        log.debug('debug')

        f.seek(0)
        s = f.read()

        assert 'warn' in s
        assert 'error' in s
        assert 'info' not in s
        assert 'debug' not in s
        assert 'info' in s[-20:]

# Generated at 2022-06-14 06:34:22.139030
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    logger.info('Start testing logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('This should log')
        logger.info('This should log')
        logger.warning('This should log')
        logger.error('This should log')
        logger.critical('This should log')
    logger.info('This should log')
    logger.info('End testing logger_level')


# Generated at 2022-06-14 06:34:31.565144
# Unit test for function logger_level
def test_logger_level():

    # Change level to INFO
    with logger_level(logging.getLogger('requests'), logging.INFO):
        get_logger().info("logging.INFO")
    logging.info("logging.INFO")

    # Change level to CRITICAL
    with logger_level(logging.getLogger('requests'), logging.CRITICAL):
        get_logger().info("logging.CRITICAL")
    logging.info("logging.CRITICAL")

    # Test that original level stays the same
    get_logger().info("logging.INFO")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:36.526095
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()
    with logger_level(logger, logging.INFO):
        logger.debug('debugging')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')



# Generated at 2022-06-14 06:34:44.122660
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(test_logger_level.__name__)
    with logger_level(logger, logging.INFO):
        try:
            assert logger.getEffectiveLevel() == logging.INFO
        except:
            logger.error('logger level set to {} instead of {}'.format(logger.getEffectiveLevel(), logging.INFO))
            raise
    try:
        assert logger.getEffectiveLevel() != logging.INFO
    except:
        logger.error('logger level set to {} instead of {}'.format(logger.getEffectiveLevel(), logging.INFO))
        raise



# Generated at 2022-06-14 06:34:54.807366
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.WARNING):
        logger.critical('critical')
        logger.error('error')
        logger.warning('warning')
        logger.info('info')
        logger.debug('debug')
        assert logger.isEnabledFor(logging.CRITICAL)
        assert logger.isEnabledFor(logging.ERROR)
        assert logger.isEnabledFor(logging.WARNING)
        assert not logger.isEnabledFor(logging.INFO)
        assert not logger.isEnabledFor(logging.DEBUG)


# Generated at 2022-06-14 06:34:58.734095
# Unit test for function logger_level
def test_logger_level():
    import logging

    l = logging.getLogger()
    assert l.level == logging.NOTSET

    with logger_level(l, logging.DEBUG):
        assert l.level == logging.DEBUG
    assert l.level == logging.NOTSET

# Generated at 2022-06-14 06:35:13.466380
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    logger.setLevel(logging.WARN)
    assert logger.level == logging.WARN
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.WARN

# In py3k, `inspect.currentframe` is removed. This prevents the context
# manager from working; the workaround is to copy the code from
# Python 2 to Python 3.
# See https://blog.ionelmc.ro/2015/02/09/understanding-python-mro/
# and http://stackoverflow.com/questions/2380799/python-with-statement-works-differently-in-2-5-than-2-6
# for more details.