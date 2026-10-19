

# Generated at 2022-06-14 06:25:13.502893
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.info('Before')
    with logger_level(logger, 10):
        logger.info('Within')
    logger.info('After')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:25:16.014929
# Unit test for function configure
def test_configure():
    configure()
    log = get_logger(__name__)
    log.info('configure test')
    assert log.isEnabledFor(logging.INFO)



# Generated at 2022-06-14 06:25:23.916221
# Unit test for function get_config
def test_get_config():
    dict_config = dict(a=1, b=2)
    json_config = '{"a":1,"b":2}'
    yaml_config = "a: 1\nb: 2\n"

    assert get_config(dict_config) == dict_config
    assert get_config(json_config) == dict_config
    assert get_config(yaml_config) == dict_config
    assert get_config(None) is None



# Generated at 2022-06-14 06:25:28.183613
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    with logger_level(logger, logging.INFO):
        logger.setLevel(logging.DEBUG)
        logger.info('During INFO')
    logger.info('After INFO')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:33.151139
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')
    with logger_level(log, logging.ERROR):
        log.debug('Debug message')
        log.info('Info message')
        log.warning('Warning message')
        log.error('Error message')
        log.critical('Critical message')


# Generated at 2022-06-14 06:25:39.077884
# Unit test for function get_config
def test_get_config():
    assert get_config(default=DEFAULT_CONFIG) == DEFAULT_CONFIG


if __name__ == "__main__":
    import doctest

    doctest.testmod(
        name="logger",
        globs=dict(get_logger=get_logger, configure=configure, get_config=get_config),
    )

# Generated at 2022-06-14 06:25:44.033779
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    try:
        with logger_level(logger, logging.DEBUG):
            logger.info('initial info message')
            raise Exception('test')
    except:
        pass
    logger.debug('subsequent debug message')
    with logger_level(logger, logging.INFO):
        logger.debug('subsequent debug message 2')


# from github.com/dm03514/python-log-in-the-dark

# Generated at 2022-06-14 06:25:51.850039
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        logger.debug('this should log')
    logger.debug('this should not log')
    with logger_level(logger, logging.DEBUG):
        with logger_level(logger, logging.INFO):
            logger.debug('this should not log')
            logger.info('this should log')
        logger.debug('this should log')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:59.133219
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARN):
        logger.info("This WARN message is not output")
        logger.warn("This is an output WARN message")
    logger.info("This is an output INFO message")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:26:02.396797
# Unit test for function logger_level
def test_logger_level():
    log = Logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('debug message')
    log.info('info message') #will not be printed

# Generated at 2022-06-14 06:26:14.714720
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("test_logger_level")
    assert(logger.level == logging.DEBUG)
    assert(logging.getLevelName(logger.level) == "DEBUG")
    assert(logging.getLevelName(logging.INFO) == "INFO")
    logging.log(logging.INFO, "normal message")
    assert(logging.getLevelName(logging.WARNING) == "WARNING")
    logging.log(logging.WARNING, "normal message")
    with logger_level(logger, logging.INFO):
        logger.critical("critical message")
        assert(logger.level == logging.INFO)
    assert(logger.level == logging.DEBUG)

# Generated at 2022-06-14 06:26:18.480115
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    with logger_level(logger, logging.NOTSET):
        assert logger.level == logging.NOTSET
    assert logger.level != logging.NOTSET

# Generated at 2022-06-14 06:26:23.578492
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger("some_logger")
    print("Current level: {}".format(l.getEffectiveLevel()))
    with logger_level(l, logging.DEBUG):
        print("Level: {}".format(l.getEffectiveLevel()))
    print("Level: {}".format(l.getEffectiveLevel()))

# Generated at 2022-06-14 06:26:29.083387
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.WARNING):
        logger.info('This should be ignored')
    logger.info('This should be printed')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:26:34.276171
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__+'.test_logger_level')

    logger.debug('before context')
    with logger_level(logger, logging.INFO):
        logger.debug('in context')
    logger.debug('after context')



# Generated at 2022-06-14 06:26:40.273392
# Unit test for function logger_level
def test_logger_level():
    """ 
        >>> import logging
        >>> logger = logging.getLogger('test')
        >>> logger.level = logging.INFO
        >>> with logger_level(logger, logging.ERROR):
        ...     logger.warning('test')
        >>> logger.critical('test')
        CRITICAL:test:test
    """


# Aliases for common levels
# Use these instead of logging.INFO/WARNING/etc.
INFO = logging.INFO
WARNING = logging.WARNING
DEBUG = logging.DEBUG
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

# Generated at 2022-06-14 06:26:44.409721
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()

    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:26:56.306681
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys

    l = logging.getLogger(__name__)
    l.setLevel(logging.DEBUG)

    def get_log_level():
        return l.getEffectiveLevel()

    def set_log_level(lvl):
        l.setLevel(lvl)

    # Test default log level
    assert get_log_level() == 10, 'default log level is not DEBUG but is %s' % get_log_level()

    # Test setting log level inside with statement
    with logger_level(l, logging.ERROR):
        assert get_log_level() == 40, 'log level is not ERROR but is %s' % get_log_level()

    # Test that logging level is unchanged outside logger_level block
    assert get_log_level() == 10, 'log level is not DEBUG but is %s'

# Generated at 2022-06-14 06:27:00.408379
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger() # getLogger is an alias of get_logger function
    with logger_level(logger, logging.DEBUG):
        logger.debug('a')



# Generated at 2022-06-14 06:27:03.202024
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.WARNING):
        log.info("info")
        log.warning("warning")

# Generated at 2022-06-14 06:27:13.018440
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.info("level=info")
        logger.debug("level=debug")
    logger.debug("level=debug")
    logger.info("level=info")



# Generated at 2022-06-14 06:27:27.220652
# Unit test for function get_config

# Generated at 2022-06-14 06:27:36.112311
# Unit test for function logger_level
def test_logger_level():
    import io

    with io.StringIO() as stream:
        log = get_logger()
        handler = logging.StreamHandler(stream)
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)

        log.debug("level: %s before context manager", log.level)
        with logger_level(log, logging.CRITICAL):
            log.debug("level: %s inside context manager", log.level)
        log.debug("level: %s after context manager", log.level)

        assert stream.getvalue() == "\x1b[90mlevel: 10 before context manager\x1b[0m\n\x1b[90mlevel: 50 after context manager\x1b[0m\n"

test_logger_level()

# Generated at 2022-06-14 06:27:47.307448
# Unit test for function logger_level
def test_logger_level():
    import sys
    logger = get_logger()
    # Create a file-like string to capture output
    codeOut = io.StringIO()
    codeErr = io.StringIO()
    sys.stdout = codeOut
    sys.stderr = codeErr
    logger.info("Before change")
    logger.setLevel(logging.WARNING)
    with logger_level(logger, logging.DEBUG):
        logger.info("Inside change")
    logger.info("After change")
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    output = codeOut.getvalue()
    codeOut.close()
    codeErr.close()
    assert("Inside change" in output)
    assert("After change" not in output)

# Generated at 2022-06-14 06:27:53.997010
# Unit test for function logger_level
def test_logger_level():

    log = get_logger(__name__)

    # Ensure we can log at debug
    assert log.isEnabledFor(logging.DEBUG) is True

    # Check that we can't log with a higher threshold
    with logger_level(log, level=logging.WARN):
        assert log.isEnabledFor(logging.DEBUG) is False

# Generated at 2022-06-14 06:28:04.673526
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    initial = logger.level

    print('Initial %s' % logger.level)
    # Test warning
    logger_warning = logger_level(logger, logging.WARNING)
    logger_warning.__enter__()

    print('Warning %s' % logger.level)
    assert logger.level == logging.WARNING
    logger_warning.__exit__()

    # Test debug
    logger_debug = logger_level(logger, logging.DEBUG)
    logger_debug.__enter__()

    print('Debug %s' % logger.level)
    assert logger.level == logging.DEBUG
    logger_debug.__exit__()

    # Test initial
    print('Final %s' % logger.level)

    assert initial == logger.level

if __name__ == '__main__':
    test

# Generated at 2022-06-14 06:28:18.388428
# Unit test for function get_config

# Generated at 2022-06-14 06:28:22.034430
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.setLevel(logging.ERROR)
    with logger_level(logger, logging.DEBUG):
        logger.debug('This should be logged')

    logger.debug('This should not be logged')

# Generated at 2022-06-14 06:28:33.962916
# Unit test for function get_config
def test_get_config():
    assert get_config(
        {'a': 'b'},
        'LOGGING',
        {'x': 'y', 'z': {'z1': 'z1'}},
    ) == {'a': 'b'}

    assert get_config(
        {'a': 'b'},
        'LOGGING',
        None,
    ) == {'a': 'b'}

    assert get_config(
        None,
        'LOGGING',
        {'x': 'y', 'z': {'z1': 'z1'}},
    ) == {'x': 'y', 'z': {'z1': 'z1'}}

# Generated at 2022-06-14 06:28:36.942286
# Unit test for function logger_level
def test_logger_level():
    root = getLogger()
    with logger_level(root, logging.DEBUG):
        assert root.level == logging.DEBUG
    assert root.level == logging.DEBUG

# Generated at 2022-06-14 06:28:46.489730
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.ERROR):
        logger.debug('Should not be visible')
        logger.error('Should be visible')
    logger.debug('Should be visible')

# Generated at 2022-06-14 06:28:59.236599
# Unit test for function get_config
def test_get_config():
    import sys
    import os
    import json
    import yaml
    if sys.version_info.major == 3:
        # Test the function with usage of valid json and yaml string
        assert get_config(json.dumps(DEFAULT_CONFIG)) == DEFAULT_CONFIG
        assert get_config(yaml.dump(DEFAULT_CONFIG)) == DEFAULT_CONFIG

        # Test the function with a list
        try:
            get_config([])
        except ValueError as exc:
            assert exc.args[0] == 'Invalid logging config: []'

        # Test the function with valid environment var

# Generated at 2022-06-14 06:29:00.390912
# Unit test for function configure
def test_configure():
    configure()


# Generated at 2022-06-14 06:29:03.135764
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.ERROR):
        logger.debug('This should not show up')
        logger.error('This should still show up')

# Generated at 2022-06-14 06:29:13.192741
# Unit test for function logger_level
def test_logger_level():
    # Set up logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    print('Test logger initial state: %s' % logger.level)

    # Test context manager is working
    with logger_level(logger, logging.ERROR):
        logger.info('Test logger level (should not appear)')
        print('Test logger contextual state: %s' % logger.level)

    logger.info('Test logger level (should appear)')
    print('Test logger final state: %s' % logger.level)


# Generated at 2022-06-14 06:29:20.721261
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    log.setLevel(logging.INFO)
    log.info('hello')
    assert log.level == logging.INFO

    with logger_level(log, logging.DEBUG):
        log.debug('hello')
        assert log.level == logging.DEBUG

    log.info('hello again')
    assert log.level == logging.INFO



# Generated at 2022-06-14 06:29:23.760034
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.critical('critical')
    log.critical('critical')

# Generated at 2022-06-14 06:29:29.490487
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warning message')
        logger.error('error message')
        logger.critical('critical message')
        logger.info('info message')
        logger.warn('warning message')

# Generated at 2022-06-14 06:29:34.905408
# Unit test for function get_config
def test_get_config():
    config = get_config(config='{"version": 1, "disable_existing_loggers": False, "formatters": {}, "handlers": {}, "root": {"level": "DEBUG", "handlers": []}}' , env_var='LOGGING', default=None)
    assert(config['version'] == 1)


# Generated at 2022-06-14 06:29:47.621323
# Unit test for function logger_level

# Generated at 2022-06-14 06:29:58.183581
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    log.setLevel(logging.DEBUG)
    log.info('Hello, world!')
    with logger_level(log, logging.ERROR):
        log.info('This should be suppressed.')
    log.info('Hello, world!')



# Generated at 2022-06-14 06:30:03.260328
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info('Info message')
    
    with logger_level(logger, logging.DEBUG):
        logger.debug('Debug message')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:16.215111
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    log.debug("Debug message")
    log.info("Info message")
    log.warning("Warning message")
    log.error("Error message")
    with logger_level(log, logging.DEBUG):
        log.debug("Debug message")
        log.info("Info message")
        log.warning("Warning message")
        log.error("Error message")
    with logger_level(log, logging.INFO):
        log.debug("Debug message")
        log.info("Info message")
        log.warning("Warning message")
        log.error("Error message")
    with logger_level(log, logging.WARNING):
        log.debug("Debug message")
        log.info("Info message")
        log.warning("Warning message")
        log.error("Error message")


# Generated at 2022-06-14 06:30:27.199668
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    # Check if logger level is DEBUG as it should be
    assert logger.level == logging.DEBUG
    # Change logger level to INFO to make sure it returns to initial level
    with logger_level(logger, logging.INFO):
        pass
    assert logger.level == logging.DEBUG
    # Make sure logger level is INFO 
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    # Make sure logger level is DEBUG and it has returned to initial level after context
    assert logger.level == logging.DEBUG

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:30.326744
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.info( "hello, world" )



# Generated at 2022-06-14 06:30:40.090919
# Unit test for function get_config
def test_get_config():
    # No input config
    assert get_config() == DEFAULT_CONFIG
    # Test with a config as yaml string

# Generated at 2022-06-14 06:30:49.169116
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)

    message = 'some message that must be logged'
    logger.warning(message)

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.warning(message)

    assert logger.level == logging.DEBUG
    logger.warning(message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:30:55.875433
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    # Check default level
    assert logger.level == logging.DEBUG
    # Change the level of the logger
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    # Check if logger has reverted to the original level when exiting the context block
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:31:03.920701
# Unit test for function get_config
def test_get_config():
    from loggician.loggician import get_config

    assert get_config(None) == DEFAULT_CONFIG

    assert get_config({'a': 'a'}) == {'a': 'a'}

    assert get_config('') == {}

    import json

    assert get_config(json.dumps({'a': 'a'})) == {'a': 'a'}

    import yaml

    assert get_config(yaml.dump({'a': 'a'})) == {'a': 'a'}


# Generated at 2022-06-14 06:31:09.715080
# Unit test for function logger_level
def test_logger_level():
    from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
    log = logging.getLogger(__name__ + ".test_logger_level")
    log.setLevel(INFO)
    log.debug("log.level=%s", INFO)
    with logger_level(log, DEBUG):
        log.debug("log.level=%s (inside)", DEBUG)
        with logger_level(log, ERROR):
            log.debug("log.level=%s (inside)", ERROR)
        log.debug("log.level=%s (inside)", ERROR)
    log.debug("log.level=%s", INFO)


__all__ = ['getLogger', 'get_logger', 'configure',
           'get_config', 'logger_level']

# Generated at 2022-06-14 06:31:19.975657
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.setLevel(logging.DEBUG)

    with logger_level(logger, logging.INFO):
        assert logger.isEnabledFor(logging.INFO) is True
        assert logger.isEnabledFor(logging.DEBUG) is False

    assert logger.isEnabledFor(logging.INFO) is False
    assert logger.isEnabledFor(logging.DEBUG) is True

# Generated at 2022-06-14 06:31:26.703290
# Unit test for function get_config
def test_get_config():
    """Unit test for function get_config"""
    # Default configuration
    assert get_config() == DEFAULT_CONFIG

    # From env variable
    with patch.object(os, 'environ', {'LOGGING': '{"loggers": {"a": 1}, "root": {"level": "INFO"}}'}):
        assert get_config() == {'loggers': {'a': 1}, 'root': {'level': 'INFO'}}

# Generated at 2022-06-14 06:31:32.293711
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig()
    log = logging.getLogger('test')
    assert log.getEffectiveLevel() == logging.DEBUG
    log.debug('before')
    with logger_level(log, logging.INFO):
        log.debug('inside')
    log.debug('after')



# Generated at 2022-06-14 06:31:42.483469
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        log.debug('a debug message')
        assert not log.isEnabledFor(logging.DEBUG)

    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('a debug message')
        assert log.isEnabledFor(logging.DEBUG)

    assert log.level == logging.NOTSET
    assert log.getEffectiveLevel() == logging.NOTSET
    log.debug('a debug message')
    assert log.isEnabledFor(logging.DEBUG)



# Generated at 2022-06-14 06:31:49.506385
# Unit test for function logger_level
def test_logger_level():

    log = get_logger()

    # There are no handlers set up for the test, so we need to manually log an
    # entry to see if it's working
    message = 'this should be logged'
    with logger_level(log, logging.DEBUG):
        log.debug(message)

    assert message in log.handlers[0].stream.getvalue()

# Generated at 2022-06-14 06:31:56.782408
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    logger = logging.getLogger(__name__ + 'test_logger_level')
    with logger_level(logger, logging.CRITICAL):
        logger.debug('debug')
        logger.error('error')
        logger.critical('critical')

    logger.debug('debug should be printed')
    logger.error('error should be printed')
    logger.critical('critical should be printed')



# Generated at 2022-06-14 06:31:59.473238
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.CRITICAL):
        log.setLevel(logging.INFO)
        assert log.level == logging.INFO
    assert log.level == logging.CRITICAL

# Generated at 2022-06-14 06:32:06.454874
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        assert logger.isEnabledFor(logging.CRITICAL)
        logger.debug("This should not be shown")
        logger.info("This should not be shown")
        logger.warning("This should not be shown")
        logger.error("This should not be shown")
        logger.critical("CRITICAL! THE END IS NEAR!")
    assert logger.isEnabledFor(logging.DEBUG)



# Generated at 2022-06-14 06:32:11.328009
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.debug('Unit test: DEBUG level')
    with logger_level(logger, logging.ERROR):
        logger.debug('Unit test: DEBUG level')
        logger.error('Unit test: ERROR level')
    logger.debug('Unit test: DEBUG level')



# Generated at 2022-06-14 06:32:16.113728
# Unit test for function logger_level
def test_logger_level():
    configure()
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('Should work')
        log.info('Should not work')
    log.info('Should work again')

# Generated at 2022-06-14 06:32:25.894354
# Unit test for function configure
def test_configure():
    import conte

    configure(os.getenv('LOGGING'))

    log = logging.getLogger(conte.__name__)

    log.info('test_configure')

# Generated at 2022-06-14 06:32:35.070107
# Unit test for function logger_level
def test_logger_level():    
    log = getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('debug message')
    with logger_level(log, logging.INFO):
        log.info('info message')
    with logger_level(log, logging.WARNING):
        log.warning('warn message')
    with logger_level(log, logging.ERROR):
        log.error('error message')
    with logger_level(log, logging.CRITICAL):
        log.critical('critical message')
    log.debug('debug message 2')


# Generated at 2022-06-14 06:32:38.630129
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.warn("test")
        assert log.getEffectiveLevel() == logging.ERROR
        log.info("test")

    # Make sure the logger is reset
    assert log.getEffectiveLevel() == logging.DEBUG



# Generated at 2022-06-14 06:32:49.650317
# Unit test for function get_config
def test_get_config():
    from . import config

    tmp_cfg_file = '/tmp/logging.conf'
    dict_cfg = dict(DEFAULT_CONFIG)
    dict_cfg['root']['level'] = 'DEBUG'
    dict_cfg['loggers'] = {
        'requests': {'level': 'DEBUG'},
        'tornado.general': {'level': 'DEBUG'}
    }
    dict_cfg['formatters'].update({
        'verbose': {
            'format': '%(asctime)s: %(levelname)s %(message)s '
                      '[in %(pathname)s:%(lineno)d]'
        }})

# Generated at 2022-06-14 06:32:53.774613
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    level = logging.INFO

    with logger_level(logger, level):
        assert logger.level == level

    assert logger.level != level

# Generated at 2022-06-14 06:32:58.576458
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    log = get_logger()
    with logger_level(log, logging.WARNING):
        log.debug("message")
        log.warning("message")


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:33:03.015508
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug')
    logger.debug('should not see this')


# Generated at 2022-06-14 06:33:07.805910
# Unit test for function logger_level
def test_logger_level():
    import logging
    log = logging.getLogger()
    configure()
    assert log.level == logging.DEBUG
    with logger_level(log, logging.ERROR):
        assert log.level == logging.ERROR
    assert log.level == logging.DEBUG


from logging import StreamHandler, FileHandler


# Generated at 2022-06-14 06:33:20.667295
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    count = {'info': 0, 'verbose': 0, 'debug': 0}

    def set_counts():
        count['info'] = 0
        count['verbose'] = 0
        count['debug'] = 0

    def do_it():
        set_counts()
        logger.debug('this is a test')
        count['debug'] = 1
        logger.info('this is a test')
        count['info'] = 1
        logger.verbose('this is a test')
        count['verbose'] = 1

    # Ensure that debug level logs verbose and debug
    logger.setLevel(logging.DEBUG)
    do_it()
    assert count['info'] == 1
    assert count['verbose'] == 1
    assert count['debug'] == 1

    # Ensure that info

# Generated at 2022-06-14 06:33:29.325489
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.info("This will not be output.")
    logger.info("This will be output.")

#def test_config():

#    print(get_config('{"hello": "world"}'))
#    print(get_config('{"hello": "world"}', None, 'asdasd'))

#if __name__ == '__main__':
#    test_config()
#    test_logger_level()

# Generated at 2022-06-14 06:33:48.424340
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.CRITICAL):
        l.debug('this should be suppressed')
    with logger_level(l, logging.DEBUG):
        l.debug('this should pass')


if __name__ == '__main__':
    _ensure_configured()

    logger = logging.getLogger(__name__)
    logger.info('START')
    logger.info('START')

# Generated at 2022-06-14 06:33:54.549046
# Unit test for function logger_level
def test_logger_level():
    # Setup
    log = getLogger('test')
    log.info('This message should appear')
    with logger_level(log, logging.WARNING):
        # Execute
        log.debug('This message should not appear')
        # Verify
        assert log.level != logging.DEBUG
    # Clean up
    log.level = logging.DEBUG
    log.info('This message should appear')

# Generated at 2022-06-14 06:34:07.584146
# Unit test for function get_config
def test_get_config():
    from bunch import bunchify


# Generated at 2022-06-14 06:34:11.527330
# Unit test for function logger_level
def test_logger_level():
    from colorlog import logger
    import io
    import contextlib

    with contextlib.redirect_stdout(io.StringIO()) as output:
        with logger_level(logger, logging.DEBUG):
            logger.debug("Debugging")
    print("This should be debug")
    assert("Debugging" in output.getvalue())

# Generated at 2022-06-14 06:34:18.921913
# Unit test for function get_config
def test_get_config():
    c = get_config(config=None, env_var=None, default=None)
    assert c == DEFAULT_CONFIG
    c = get_config(config=dict(), env_var=None, default=None)
    assert c == dict()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:34:23.169912
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger()
    >>> log.setLevel(logging.INFO)

    >>> with logger_level(log, logging.DEBUG):
    ...   log.debug('test')
    """
    pass



# Generated at 2022-06-14 06:34:28.979832
# Unit test for function logger_level
def test_logger_level():
    class MockLogger(object):
        def __init__(self):
            self.level = logging.DEBUG

    mock_logger = MockLogger()
    with logger_level(mock_logger, logging.INFO):
        assert mock_logger.level == logging.INFO

    assert mock_logger.level == logging.DEBUG

# Generated at 2022-06-14 06:34:36.981692
# Unit test for function logger_level
def test_logger_level():
    # Create a logger
    logger = logging.getLogger(__name__)
    # Check that it's level is 0
    assert(logger.level == 0)
    # Temporarily set it's level to 10
    with logger_level(logger, 10):
        assert(logger.level == 10)
    # Check that it's level is 0 again at the end of the context manager
    assert(logger.level == 0)

# Generated at 2022-06-14 06:34:43.132056
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig()
    logger = logging.getLogger()
    with logger_level(logger, logging.CRITICAL):
        assert(logger.level == logging.CRITICAL)
        with logger_level(logger, logging.ERROR):
            assert(logger.level == logging.ERROR)
        assert(logger.level == logging.CRITICAL)
    assert(logger.level == logging.NOTSET)



# Generated at 2022-06-14 06:34:55.960201
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug('Hello, World.')
    log.debug('Hello, World.')


# Unfortunately, there is some complexity around this.
# To get correct information, we need to log with a custom logger,
# however, our caller may be trying to log with the root logger
# (because the caller's __name__ is "__main__", for instance).
#
# So, if we're asked for the root logger, we create a special
# logger to use, and then return the root logger.

# Note: be careful not to modify the root logger by accident.
# Tracking down problems caused by that is not fun.

