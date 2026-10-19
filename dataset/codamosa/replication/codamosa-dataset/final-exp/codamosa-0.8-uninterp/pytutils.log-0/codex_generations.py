

# Generated at 2022-06-14 06:25:11.870514
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.info('info')
        logger.debug('debug')

    logger.info('info')
    # logger.debug('debug')   # disabled



# Generated at 2022-06-14 06:25:21.765419
# Unit test for function get_config
def test_get_config():
    os.environ["LOGGING"] = None

    # Testing for bare string input
    config = get_config('DEBUG', None, None)
    assert config == 'DEBUG'

    # Testing for `JSON` input
    config = get_config('{"KEY": "VALUE"}', None, None)
    assert config == {'KEY': 'VALUE'}

    # Testing for `YAML` input
    config = get_config('KEY: VALUE', None, None)
    assert config == {'KEY': 'VALUE'}

    # Testing for `env_var` input
    os.environ["LOGGING"] = 'DEBUG'
    config = get_config(None, 'LOGGING', None)
    assert config == 'DEBUG'

    # Testing for `default` input
    os.environ["LOGGING"] = None
   

# Generated at 2022-06-14 06:25:24.982644
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.NOTSET



# Generated at 2022-06-14 06:25:28.649371
# Unit test for function logger_level
def test_logger_level():
    """
    >>> from .log import getLogger
    >>> l = getLogger()
    >>> l.setLevel('ERROR')
    >>> l.error('Unit test for logger_level (expect error)')
    >>> with logger_level(l, 'INFO'):
    ...     l.info('Unit test for logger_level (expect info)')
    >>> l.info('Unit test for logger_level (expect to be ignored)')
    """
    pass


# Generated at 2022-06-14 06:25:32.642952
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
    assert logger.level == logging.DEBUG
    logger.info('test')

# Generated at 2022-06-14 06:25:38.381942
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger()
    >>> with logger_level(log, logging.CRITICAL):
    ...     log.debug('boo')
    ...     log.info('bah')
    ...     log.error('bam')
    >>> log.error('finished')

    """
    pass



# Generated at 2022-06-14 06:25:45.330080
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
        assert not logger.isEnabledFor(logging.INFO)

    assert not logger.isEnabledFor(logging.DEBUG)
    assert not logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:50.424187
# Unit test for function configure
def test_configure():
    try:
        logging.basicConfig()
    except:
        logger = logging.getLogger('test_configure')
        logger.critical('Error configuring logger')
        raise
    else:
        logger = logging.getLogger('test_configure')
        logger.info('Default logger was configured properly')


# Generated at 2022-06-14 06:25:56.644635
# Unit test for function logger_level
def test_logger_level():
    import sys
    logger = logging.getLogger('test_logger_level')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)

    logger.info('test')
    with logger_level(logger, logging.DEBUG):
        logger.info('test')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:03.949612
# Unit test for function get_config
def test_get_config():
    assert get_config(config=None) == DEFAULT_CONFIG
    assert get_config(config=None, default=None) == {}
    assert get_config(config=None, env_var='LOGGING') == DEFAULT_CONFIG
    assert get_config(config='{"root": {"level": "WARNING"}}') == {"root": {"level": "WARNING"}}

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

# Generated at 2022-06-14 06:26:09.860052
# Unit test for function configure
def test_configure():
    _CONFIGURED.clear()
    log = get_logger()
    log.info('test')
    assert len(_CONFIGURED) == 1
    log.info('test')

# Generated at 2022-06-14 06:26:16.199623
# Unit test for function logger_level
def test_logger_level():
    import time

    log = get_logger()
    start_time = time.time()
    # The following should not print anything
    with logger_level(log, logging.ERROR):
        for i in range(10):
            log.info('Should not print this')
    log.info('This should print')
    end_time = time.time()

    assert(end_time - start_time < 0.2)

if __name__ == '__main__':
    print(getLogger('test'))

    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:26:20.926496
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger(), logging.DEBUG):
        logger = getLogger()
        assert logger.level == logging.DEBUG, \
            'Incorrect level for logger with context logger_level'


_broken_pipe = None



# Generated at 2022-06-14 06:26:27.412998
# Unit test for function get_config
def test_get_config():
    # test for non-existent file and None config
    try:
        config = get_config(config='doesnotexist.conf')
        assert False, "Should not reach here"
    except ValueError:
        assert True

    # test for config='some.yml'
    config = get_config(config='logger/tests/some.yml')
    assert isinstance(config, dict)
    assert set(config.keys()) == {'version', 'disable_existing_loggers',
                                  'handlers', 'root', 'formatters'}

    # test for config='some.json'
    config = get_config(config='logger/tests/some.json')
    assert isinstance(config, dict)

# Generated at 2022-06-14 06:26:40.296502
# Unit test for function logger_level
def test_logger_level():
    # Configure a simple logger for the time being
    configure(dict(
        version=1,
        disable_existing_loggers=False,
        handlers={
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'level': logging.DEBUG,
            },
        },
        formatters={
            'simple': {
                'format': '%(asctime)s| %(message)s',
            },
        },
        root=dict(handlers=['console'], level=logging.DEBUG),
        loggers={
            'requests': dict(level=logging.INFO),
        },
    ))

    # Get the root logger
    logger = get_logger()

    # Set it to DEBUG and log something, pass in a function to logger_level that

# Generated at 2022-06-14 06:26:50.589434
# Unit test for function logger_level
def test_logger_level():
    # Set up a logger
    logger = logging.getLogger('test')
    configure()

    # Set the minimum level to print
    logger.level = logging.WARNING

    # In the context of the logger level being set to DEBUG,
    # we can see messages with level DEBUG
    with logger_level(logger, logging.DEBUG):
        logger.debug('Message 1')
    # Outside the context, we cannot see messages with level DEBUG
    logger.debug('Message 2')

    # Verify that the logger level was restored
    assert logger.level == logging.WARNING, \
        "logger_level did not restore original logger level"

    # Verify that only the first message was printed
    with CaptureStdout() as capture:
        logger.debug('Message 3')

# Generated at 2022-06-14 06:26:57.364177
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    file_path = os.path.join(tempfile.gettempdir(), 'test.log')
    logging.basicConfig(level=logging.DEBUG, filename=file_path)
    f = open(file_path, 'r')
    if f.read():
        pytest.fail('The log is not blank!')
    f.close()

    logger = get_logger()
    logger.error('This is the error message.')
    logger.info('This is the info message.')
    f = open(file_path, 'r')
    output = f.read()
    assert 'This is the error message.' in output
    assert 'This is the info message.' not in output
    f.close()

    f = open(file_path, 'w')

# Generated at 2022-06-14 06:27:01.098851
# Unit test for function get_config
def test_get_config():
    try:
        logging.getLogger()
    except ValueError:
        pass
    else:
        assert(False)

    logging.getLogger(__name__)
    assert(True)

# Generated at 2022-06-14 06:27:03.929110
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(__name__), logging.DEBUG):
        get_logger(__name__).debug('test')



# Generated at 2022-06-14 06:27:15.107353
# Unit test for function logger_level
def test_logger_level():
    from io import StringIO
    from logging import DEBUG, INFO, ERROR

    out = StringIO()

    logger = getLogger(__name__)
    root_logger = getLogger()
    original_level = root_logger.level

    root_logger.setLevel(ERROR)
    logger.setLevel(DEBUG)

    handler = logging.StreamHandler(out)
    handler.setLevel(DEBUG)
    logger.addHandler(handler)

    logger.debug('debug')
    assert out.getvalue() == ''

    with logger_level(logger, INFO):
        logger.debug('debug')
        assert out.getvalue() == ''
        logger.info('info')
        assert out.getvalue() == 'info\n'

    logger.debug('debug')

# Generated at 2022-06-14 06:27:21.033729
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level != logging.INFO



# Generated at 2022-06-14 06:27:24.815285
# Unit test for function logger_level
def test_logger_level():
    import logging
    log = logging.getLogger("test_logger_level")
    logger_level(log, logging.INFO)
    log.info("Hello")
    log.warning("Goodbye")



# Generated at 2022-06-14 06:27:29.375337
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('logger_level_test')
    with logger_level(logger, logging.INFO):
        logger.debug('test_logger_level failed')
    logger.debug('test_logger_level succeeded')

# Generated at 2022-06-14 06:27:34.474148
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.INFO):
        log.debug("Log level should be INFO right now, but you won't see this message")
        log.info("This should be visible")
    log.debug("Log level should be DEBUG again")
    log.debug("This should be visible again")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:27:40.278822
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = getLogger()
    >>> log.info('test')
    >>> with logger_level(log, logging.CRITICAL):
    ...     log.info('test')
    """
    pass

# Alias for historical reasons.
with_log_level = logger_level



# Generated at 2022-06-14 06:27:44.569978
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    try:
        with logger_level(logger, logging.WARN):
            logger.debug("Should not print")
            logger.warn("Should print")
    except:
        raise AssertionError("logger level context manager failed")

# Generated at 2022-06-14 06:27:50.044403
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = getLogger('test')
    >>> with logger_level(log, logging.DEBUG):
    ...     log.info('info message should appear')
    ...     log.debug('debug message should appear')
    ...
    >>> with logger_level(log, logging.INFO):
    ...     log.info('info message should appear')
    ...     log.debug('debug message should not appear')
    """


# Generated at 2022-06-14 06:27:55.534482
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('logging_ext')

    with logger_level(logger, logging.DEBUG):
        logger.debug('visibly debug')
        logger.info('hidden info')

    logger.warning('visible warning')
    logger.info('still hidden')

# Generated at 2022-06-14 06:27:59.522782
# Unit test for function logger_level
def test_logger_level():
    log = get_logger("test_logger_level")
    log.info("before")
    with logger_level(log, logging.INFO):
        log.info("inside")
    log.info("after")



# Generated at 2022-06-14 06:28:04.130626
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test-logger-level')
    # logger.setLevel(logging.DEBUG)
    assert logger.level == logging.NOTSET
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.NOTSET



# Generated at 2022-06-14 06:28:18.969219
# Unit test for function logger_level
def test_logger_level():
    def test_func():
        log = get_logger()
        log.setLevel(logging.ERROR)
        log.debug('Test debug message')
        log.info('Test info message')
        log.warning('Test warning message')
        log.error('Test error message')
        return None
    test_func()
    log = get_logger()
    log.setLevel(logging.DEBUG)
    with logger_level(log, logging.INFO):
        test_func()
    test_func()
    with logger_level(log, logging.DEBUG):
        test_func()


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:29.156233
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("ok")
        assert log.isEnabledFor(logging.DEBUG)
        assert log.isEnabledFor(logging.INFO)
        assert log.isEnabledFor(logging.NOTSET)
    assert not log.isEnabledFor(logging.DEBUG)
    assert not log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.NOTSET)

    def show(log):
        s = '{name} log level: {level}'.format(name=log.name, level=log.level)
        print(s)
        log.info(s)

    log2 = get_logger('test_logger_level')
    show(log2)

# Generated at 2022-06-14 06:28:34.971074
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.INFO


if __name__ == "__main__":
    configure()
    log = get_logger()
    log.debug('Hello, world!')
    log.debug('Hello, world!')

# Generated at 2022-06-14 06:28:38.349341
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger()
    with logger_level(log, logging.ERROR):
        log.info('Logging should be disabled')
    log.info('Logging should work again')


# Generated at 2022-06-14 06:28:38.907504
# Unit test for function configure
def test_configure():
    configure()

# Generated at 2022-06-14 06:28:46.300047
# Unit test for function logger_level
def test_logger_level():
    old_level = logging.getLogger().level
    logger = get_logger()


# Generated at 2022-06-14 06:28:51.864092
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger("test_logger_level")
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:28:55.344010
# Unit test for function logger_level
def test_logger_level():
    # log.debug('test')
    # log.info('test')
    with logger_level(log, logging.WARN):
        log.debug('test')
        log.info('test')
    log.debug('test')



# Generated at 2022-06-14 06:29:04.397336
# Unit test for function logger_level
def test_logger_level():
    import sys
    import pytest
    import io

    log = getLogger()

    # Test that the logger isn't already at debug level
    log.debug('test')
    with pytest.raises(AssertionError):
        io.StringIO().getvalue() == 'test'

    # Test with debug level
    with logger_level(log, logging.DEBUG):
        log.debug('test')
        assert io.StringIO().getvalue() == 'test'

    # Test that logger is at INFO level
    with logger_level(log, logging.INFO):
        log.debug('test')
        with pytest.raises(AssertionError):
            io.StringIO().getvalue() == 'test'

# Generated at 2022-06-14 06:29:11.088420
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    # Make sure that by default the logger is at info level
    log.info("Test1")
    with logger_level(log, logging.WARNING):
        log.info("Test2")
        log.warning("Test3")
    log.info("Test4")


# Generated at 2022-06-14 06:29:26.715602
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    config = get_config()
    cfg_json = json.dumps(config)
    cfg_yaml = yaml.dump(config)
    cfg = get_config(cfg_json)
    assert len(cfg) == len(config)
    cfg = get_config(cfg_yaml)
    assert len(cfg) == len(config)

    config1 = dict(a=1)
    cfg_json_1 = json.dumps(config1)
    cfg_yaml_1 = yaml.dump(config1)
    cfg = get_config(cfg_json_1)
    assert len(cfg) == len(config1)
    cfg = get_config(cfg_yaml_1)
    assert len(cfg) == len(config1)

# Generated at 2022-06-14 06:29:30.376751
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.DEBUG):
        logging.debug('test')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:29:36.530957
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    logger.info('test_logger_level: info')
    with logger_level(logger, logging.CRITICAL):
        logger.info('test_logger_level: info under critical should not be logged')
        logger.critical('test_logger_level: critical under critical')
    logger.info('test_logger_level: info')



# Generated at 2022-06-14 06:29:43.561667
# Unit test for function logger_level
def test_logger_level():
    configure()
    logger = get_logger('test_logger_level')
    logger.setLevel(logging.INFO)
    assert logger.level == logging.INFO
    try:
        with logger_level(logger, logging.CRITICAL):
            assert logger.level == logging.CRITICAL
    finally:
        assert logger.level == logging.INFO

# Generated at 2022-06-14 06:29:46.787622
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.DEBUG):
        assert l.level == logging.DEBUG

    assert l.level != logging.DEBUG



# Generated at 2022-06-14 06:29:51.431578
# Unit test for function logger_level
def test_logger_level():
    l = get_logger(__name__)

    with logger_level(l, logging.CRITICAL):
        l.debug("I won't be displayed")
        l.info("I won't be displayed")
        l.error("I will be displayed")

# Generated at 2022-06-14 06:30:03.746121
# Unit test for function logger_level
def test_logger_level():
    logger_info = get_logger(__name__)
    logger_debug = get_logger(__name__)
    # info is default level
    assert logger_info.level == 20
    assert logger_debug.level == 20
    # info should be 20, debug should be 10
    with logger_level(logger_info, 10):
        assert logger_info.level == 10
        assert logger_debug.level == 10
    # info should be 20, debug should also be 20
    with logger_level(logger_debug, 10):
        assert logger_info.level == 20
        assert logger_debug.level == 10
    assert logger_info.level == 20
    assert logger_debug.level == 20

# Generated at 2022-06-14 06:30:09.663814
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level = logging.DEBUG)
    log = logging.getLogger(__name__)

    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        log.debug('Hello Logger!')

    assert log.level == logging.DEBUG
    log.debug('Hello Logger!')



# Generated at 2022-06-14 06:30:12.959170
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test')
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:30:23.308280
# Unit test for function get_config
def test_get_config():
    config_dict = {'version': 1, 'formatters': {'simple': {'format': '%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}}, 'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'simple', 'level': 'DEBUG'}}, 'root': {'level': 'DEBUG', 'handlers': ['console']}, 'loggers': {'requests': {'level': 'INFO'}}}

# Generated at 2022-06-14 06:30:31.866936
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    assert log.getEffectiveLevel() == logging.INFO
    with logger_level(log, logging.DEBUG):
        assert log.getEffectiveLevel() == logging.DEBUG
    assert log.getEffectiveLevel() == logging.INFO

# Generated at 2022-06-14 06:30:38.430159
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.info('level=info, DEBUG (expected)')
        logger.warning('level=warning, DEBUG (expected)')
        logger.error('level=error, DEBUG (expected)')
    logger.info('level=info, INFO (expected)')
    logger.warning('level=warning, INFO (expected)')
    logger.error('level=error, INFO (expected)')

# Unit tests for function get_config

# Generated at 2022-06-14 06:30:47.945001
# Unit test for function logger_level
def test_logger_level():
    """Test to see if a logging.DEBUG message is not shown with logging level set to INFO"""
    import random
    import string
    test_logger = logging.getLogger('logger_level_test')
    configure()
    test_logger.setLevel(logging.INFO)
    test_logger.info('info message')
    test_logger.debug('debug message')
    with logger_level(test_logger, logging.DEBUG):
        test_logger.debug('debug message')


# Generated at 2022-06-14 06:31:00.791321
# Unit test for function get_config
def test_get_config():
    json_string = '{"version": 1, "disable_existing_loggers": false, "formatters": {"colored": {"()": "colorlog.ColoredFormatter", "format": "%(bg_black)s%(log_color)s[%(asctime)s] [%(name)s/%(process)d] %(message)s %(blue)s@%(funcName)s:%(lineno)d #%(levelname)s%(reset)s", "datefmt": "%H:%M:%S"}}, "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "colored", "level": 10}}, "root": {"handlers": ["console"], "level": 10}, "loggers": {"requests": {"level": 20}}}'

# Generated at 2022-06-14 06:31:04.989625
# Unit test for function logger_level
def test_logger_level():
    from .logging_setup import get_logger
    logger = get_logger()
    with logger_level(logger, logging.WARNING):
        logger.info('this should not show up')
        logger.warning('this should show up')
    logger.info('this should show up')
    logger.warning('this should show up')

# Generated at 2022-06-14 06:31:10.775469
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test.logger_level')
    assert logger.level == logging.NOTSET
    with logger_level(logger, logging.WARN):
        assert logger.level == logging.WARN
        with logger_level(logger, logging.INFO):
            assert logger.level == logging.INFO
        assert logger.level == logging.WARN
    assert logger.level == logging.NOTSET



# Generated at 2022-06-14 06:31:14.871354
# Unit test for function configure
def test_configure():
    with logger_level(logging.getLogger(), logging.CRITICAL):
        configure()
        log = logging.getLogger(__name__)
        log.info('test_configure')

# Generated at 2022-06-14 06:31:20.707162
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARNING):
        for level in (logging.DEBUG, logging.INFO):
            assert logger.isEnabledFor(level) == False
        for level in (logging.WARNING, logging.ERROR, logging.CRITICAL):
            assert logger.isEnabledFor(level) == True



# Generated at 2022-06-14 06:31:33.647726
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import time

    # Create the logger
    logger = logging.getLogger()
    configure()

    # Create a temp file that we'll log to
    fd, path = tempfile.mkstemp(suffix=".log")
    f = os.fdopen(fd, 'w')
    f.close()

    # Configure the root logger to log to our file.
    logger.handlers[0].stream = open(path, 'w')

    # Log something at the default DEBUG level
    logger.info("Hello World")

    # Open the file to read what we just logged
    with open(path, 'r') as fh:
        logs = fh.readlines()
        assert len(logs) == 1

    # The above logged our message because the logger was at DEBUG level
    # Now change the level

# Generated at 2022-06-14 06:31:41.904817
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.ERROR):
        logger.info('this message should not be printed')
        logger.debug('this message should not be printed')
        logger.error('this message should be printed')
    logger.info('this message should be printed')
    logger.debug('this message should be printed')
    logger.error('this message should be printed')
    assert True

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:31:55.312263
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    original_level = logger.level
    try:
        with logger_level(logger, logging.ERROR):
            logger.error('this should be visible')
            logger.warning('this should not be visible')
            with logger_level(logger, logging.WARNING):
                logger.error('this should be visible, still')
                logger.warning('this should be visible, too')
        logger.error('this should be visible, too')
    finally:
        logger.level = original_level



# Generated at 2022-06-14 06:32:01.466979
# Unit test for function logger_level
def test_logger_level():
    print("\nTesting function logger_level")
    import logging
    import logging.config
    import sys
    import os
    import tempfile
    import subprocess
    import json
    import traceback
    import time
    logger = logging.getLogger()
    print("logger level is %s"%logger.level)
    with logger_level(logger, logging.INFO):
        print("logger level is %s"%logger.level)
    print("logger level is %s"%logger.level)

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:32:03.445423
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.DEBUG):
        pass

# Generated at 2022-06-14 06:32:08.687434
# Unit test for function logger_level
def test_logger_level():
    from io import StringIO
    from contextlib import redirect_stdout

    log = get_logger('test_dummy')
    log.info('Testing logger_level')
    log.warning('This is a warning')
    log.info('This is an info message')

    with redirect_stdout(StringIO()) as stdout:
        with logger_level(log, logging.WARNING):
            log.info('Testing logger_level')
            log.warning('This is a warning')
            log.info('This is an info message')
    output = stdout.getvalue()

    assert output.count('INFO:test_dummy:This is an info message') == 1, "Invalid logger_level behavior"
    assert output.count('WARNING:test_dummy:This is a warning') == 2, "Invalid logger_level behavior"

# Generated at 2022-06-14 06:32:12.456587
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.info('This should NOT show up in the log')
        log.debug('This should show up in the log')
    log.info('This should show up in the log')

# Generated at 2022-06-14 06:32:15.066160
# Unit test for function get_config
def test_get_config():
    assert get_config() == DEFAULT_CONFIG



# Generated at 2022-06-14 06:32:18.283021
# Unit test for function get_config
def test_get_config():
    print(get_config(json.dumps(DEFAULT_CONFIG), None, None))


if __name__ == '__main__':
    test_get_config()

# Generated at 2022-06-14 06:32:26.621873
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    with logger_level(logging.getLogger('test_logger_level'), logging.CRITICAL):
        logger = logging.getLogger('test_logger_level')
        logger.warning("Hello") # this message should not be printed
        assert logger.isEnabledFor(logging.WARNING) == False
        assert logger.isEnabledFor(logging.CRITICAL) == True


# Generated at 2022-06-14 06:32:32.062302
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> log = logging.getLogger('test')
    >>> with logger_level(log, logging.INFO):
    ...     print(log.level)
    INFO
    """
    pass



# Generated at 2022-06-14 06:32:42.189833
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)

    # log messages will be visible at level >= 50
    logger.warning('message1')

    with logger_level(logger, logging.WARN) as l:
        # log messages will be visible at level >= 10
        logger.info('message2')

    # level is back to 50
    logger.warning('message3')


if __name__ == "__main__":
    print(get_logger().name)
    print(get_logger(__name__).name)

# Generated at 2022-06-14 06:32:47.812008
# Unit test for function configure
def test_configure():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.info('Test')

# Generated at 2022-06-14 06:33:02.284976
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger(__name__)
    >>> with logger_level(log, logging.ERROR):
    ...     log.info('should not print')
    ...     log.error('should print')
    ERROR:test:should print @test_logger_level:%d #ERROR
    >>> log = get_logger(__name__)
    >>> log.error('should print')
    ERROR:test:should print @test_logger_level:%d #ERROR
    >>> log.level = logging.ERROR
    >>> log.info('should not print')
    >>> log.error('should print')
    ERROR:test:should print @test_logger_level:%d #ERROR
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:33:06.066083
# Unit test for function logger_level
def test_logger_level():
    """
    >>> logging.basicConfig(level=logging.DEBUG)
    >>> log = getLogger(__name__)
    >>> log.info('x')
    x
    >>> with logger_level(log, logging.WARN):
    ...    log.info('x')
    >>> log.info('y')
    y
    """



# Generated at 2022-06-14 06:33:20.084410
# Unit test for function configure

# Generated at 2022-06-14 06:33:28.532825
# Unit test for function logger_level
def test_logger_level():
    """
    >>> test_logger_level()
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__ + ' test_logger_level')
    check_that_logger_level_is_info(logger)
    with logger_level(logger, logging.DEBUG):
        check_that_logger_level_is_debug(logger)
    check_that_logger_level_is_info(logger)



# Generated at 2022-06-14 06:33:38.831906
# Unit test for function get_config
def test_get_config():
    assert isinstance(get_config(None, None, DEFAULT_CONFIG), dict)
    assert isinstance(get_config("""{ "formatters": { "simple": { "format": "%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s", "datefmt": "%Y-%m-%d %H:%M:%S" } } }"""), dict)

# Generated at 2022-06-14 06:33:43.181490
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, 100):
        log.error("This is error")
        log.warning("This is error")
        log.debug("This is error")



# Generated at 2022-06-14 06:33:49.460356
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    logger = logging.getLogger('test_logger')

    with logger_level(logger, logging.CRITICAL):
        logger.debug("hello")
        assert logger.isEnabledFor(logging.CRITICAL)
        assert not logger.isEnabledFor(logging.DEBUG)

    assert logger.isEnabledFor(logging.DEBUG)

# Generated at 2022-06-14 06:33:53.854361
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    log.setLevel(logging.DEBUG)
    with logger_level(log, logging.DEBUG):
        log.debug('test')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:33:57.627061
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.DEBUG):
        logging.debug("level is debug")
    logging.debug("level is info")



# Generated at 2022-06-14 06:34:12.465369
# Unit test for function logger_level

# Generated at 2022-06-14 06:34:17.409907
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:34:22.871684
# Unit test for function logger_level
def test_logger_level():
    data = [1, 2, 3, 4, 5]
    with logger_level(logger, logging.CRITICAL):
        # because this info statement is being run after the context,
        # it should be suppressed 
        logger.info('This will not be logged')
    assert len(data) == 5


# Generated at 2022-06-14 06:34:27.505555
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('logger_level_test')

    with logger_level(log, logging.DEBUG):
        log.debug('debug')

    log.info('info')
    log.error('error')


# Generated at 2022-06-14 06:34:33.045528
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('foo')
    with logger_level(log, logging.ERROR):
        assert log.level == logging.ERROR
        log.debug('sup')
        log.info('sup')
    assert log.level == logging.DEBUG
    log.debug('sup')



# Generated at 2022-06-14 06:34:36.694092
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    log.info('log before')
    with logger_level(log, logging.ERROR):
        log.info('log inner')
    log.info('log after')

# Generated at 2022-06-14 06:34:41.224048
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger.level == logging.DEBUG
    context_level = 30
    with logger_level(logger, context_level):
        assert logger.level == context_level
    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:34:45.586373
# Unit test for function configure
def test_configure():
    # TODO

    # configure()

    # configure(config=dict(foo=1))

    # configure(env_var='LOGGING')

    # configure(default=dict(foo=1))

    # configure(config=dict(foo=1), env_var='LOGGING', default=dict(bar=2))

    # configure(config=dict(foo=1), default=dict(bar=2))

    # configure(env_var='LOGGING', default=dict(bar=2))

    pass



# Generated at 2022-06-14 06:34:56.017626
# Unit test for function logger_level
def test_logger_level():
    import StringIO
    fp = StringIO.StringIO()
    logging.basicConfig(stream=fp, level=logging.DEBUG, format="%(message)s")
    log = logging.getLogger()
    log.debug("before")
    with logger_level(log, logging.WARNING):
        log.debug("during")
    log.debug("after")
    s = fp.getvalue()
    if "before" not in s:
        raise AssertionError
    if "during" in s:
        raise AssertionError
    if "after" not in s:
        raise AssertionError

# Generated at 2022-06-14 06:34:58.520698
# Unit test for function configure
def test_configure():
    assert configure()


if __name__ == '__main__':
    import doctest
    doctest.testmod()