

# Generated at 2022-06-14 06:25:15.526433
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    logger.info("This should not appear")
    with logger_level(logger, logging.WARNING):
        logger.debug("This should not appear")
        logger.info("This should not appear")
        logger.warning("This should appear")
        assert logger.isEnabledFor(logging.WARNING)
    logger.info("This should appear")
    logger.debug("This should not appear")
    assert not logger.isEnabledFor(logging.DEBUG)

# Generated at 2022-06-14 06:25:22.038691
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

    with logger_level(log, logging.DEBUG):
        assert log.debug("hello") is None  #sanity check, log.debug should return None
        assert log.getEffectiveLevel() == logging.DEBUG

    # verify that logger level has been reset after logging.DEBUG context block
    assert log.getEffectiveLevel() == logging.INFO

# Generated at 2022-06-14 06:25:25.588548
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.WARN):
        assert logger.level == logging.WARN
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:25:32.271373
# Unit test for function get_config
def test_get_config():
    config1 = '{"version": 1}\n'
    config2 = 'version: 1\n'
    config3 = 'version: 1'
    config4 = '{"version": 1}'
    default_config = dict(version=1)

    # string, default
    assert get_config(config1, default=default_config) == default_config
    # string, yaml, default
    assert get_config(config2, default=default_config) == default_config
    # string, yaml
    assert get_config(config2) == dict(version=1)
    # string, json
    assert get_config(config4) == dict(version=1)
    # string, bare
    with pytest.raises(ValueError):
        get_config(config3)
    # dict

# Generated at 2022-06-14 06:25:41.493499
# Unit test for function logger_level
def test_logger_level():
    import json
    import tempfile


# Generated at 2022-06-14 06:25:50.152655
# Unit test for function logger_level
def test_logger_level():
    import logging
    import contextlib
    import time

# Generated at 2022-06-14 06:25:57.298300
# Unit test for function logger_level
def test_logger_level():
    level = 10
    logger = get_logger()
    with logger_level(logger, level):  # change logger level to 10.
        assert logger.level == level    # This should never fail, if it does there's a bug here.
    assert logger.level != level       # Should be back to the default value.


# Generated at 2022-06-14 06:26:06.029844
# Unit test for function get_config
def test_get_config():
    # test this function of different configuration
    config = get_config(default = DEFAULT_CONFIG)
    assert config == DEFAULT_CONFIG
    config = get_config(default = {"version": 1}, env_var = "LOGGING")
    assert config == {"version": 1}
    config = get_config(config = {"version": 2}, env_var = "LOGGING")
    assert config == {"version": 2}
    config = get_config(config = '{"version": 3}', env_var = "LOGGING")
    assert config == {"version": 3}
    config = get_config(config = 'version: 4', env_var = "LOGGING")
    assert config == {"version": 4}

# Generated at 2022-06-14 06:26:11.986728
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug('Run in DEBUG')
        logger.info('Run in DEBUG')
        logger.warn('Run in DEBUG')
        logger.error('Run in DEBUG')
        logger.critical('Run in DEBUG')
    logger.debug('Do not run')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:26:18.340414
# Unit test for function configure
def test_configure():
    import requests
    configure()
    log = logging.getLogger('test')
    log.info('test')
    log.debug('test')

    # Test that requests is filtered properly
    requests.get('http://www.google.com')


if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:26:27.803685
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.critical('critical message')
        logger.error('error message')
        logger.warning('warning message')
        logger.info('info message')
        logger.debug('debug message')



# Generated at 2022-06-14 06:26:41.279176
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    # Create a temporary file
    fd, path = tempfile.mkstemp()
    fp = open(path, 'rb+')

    # Initialize logger
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    # Create a handler for the logger
    handler = logging.StreamHandler(fp)
    logger.addHandler(handler)

    # Write something into the logger
    with logger_level(logger, logging.ERROR):
        logger.log(logging.ERROR, "Error message")
        logger.log(logging.DEBUG, "Debug message")
        logger.log(logging.INFO, "Info message")

    # Check if the file is empty
    fp.seek(0)
    # Should be empty

# Generated at 2022-06-14 06:26:45.131144
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.ERROR):
        try:
            log.debug("This should not be logged")
            assert False
        except Exception:
            assert True
        log.error("This should be logged")

# Generated at 2022-06-14 06:26:48.836448
# Unit test for function logger_level
def test_logger_level():
    # TODO: test with real logger object
    logger = logging
    level = 20
    logger.level = 25
    assert(logger.level != level)
    with logger_level(logger, level):
        assert(logger.level == level)
    assert(logger.level != level)



# Generated at 2022-06-14 06:26:57.530672
# Unit test for function configure
def test_configure():
    import tempfile

    # create a temporary file in the system for testing
    fd, path = tempfile.mkstemp()


# Generated at 2022-06-14 06:27:08.921366
# Unit test for function logger_level
def test_logger_level():
    """
    This unit test will create the logger, set the level to DEBUG, print message and
    then set the level back to INFO. This test will ensure that the message will
    only be printed when its DEBUG.
    """
    my_logger = getLogger()
    my_logger.setLevel(logging.INFO)
    with logger_level(my_logger, logging.DEBUG):
        my_logger.debug("This is DEBUG message")
    my_logger.info("This is INFO message")
    return


__all__ = [
    "get_logger",
    "getLogger",
    "configure",
    "get_config",
    "logger_level",  # Test purpose
]

# Generated at 2022-06-14 06:27:20.374488
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')

    # Test the parent logger level gets propaged
    with logger_level(logger, logging.INFO):
        log = getLogger('test_logger_level.child')
        assert log.level == logging.INFO

    # Test the initial log level gets reset same as parent
    with logger_level(logger, logging.WARN):
        log = getLogger('test_logger_level.child')
        assert log.level == logging.WARN
        with logger_level(log, logging.INFO):
            assert log.level == logging.INFO
        assert log.level == logging.WARN
    assert log.level == logging.INFO

    # Test the initial log level gets reset same as child
    with logger_level(log, logging.WARN):
        assert log.level == logging.WARN

# Generated at 2022-06-14 06:27:23.509205
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    log.info('This output is to be expected.')
    with logger_level(log, logging.DEBUG):
        log.debug('This output is also to be expected')
    log.debug('This will not be printed because of DEBUG level set in the context manager above')

# Generated at 2022-06-14 06:27:29.618830
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.CRITICAL) as l:
        assert(l.level == logging.CRITICAL)
        assert(log.level == logging.CRITICAL)
    assert(log.level == logging.DEBUG)


# Generated at 2022-06-14 06:27:33.595394
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('This is a debug message')
    with logger_level(logger, logging.INFO):
        logger.debug('This is a debug message')



# Generated at 2022-06-14 06:27:39.495727
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.CRITICAL):
        log.debug("This will be ignored")
        log.critical("This will work.")

    log.debug("This will work.")

# Generated at 2022-06-14 06:27:48.576441
# Unit test for function logger_level
def test_logger_level():
    """Test the logger_level function."""
    import sys
    import StringIO
    import logging

    my_logger = logging.getLogger('logger_level_test')
    my_logger.setLevel(logging.ERROR)
    my_handler = logging.StreamHandler(sys.stdout)
    my_handler.setLevel(logging.ERROR)
    my_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    my_handler.setFormatter(my_formatter)
    my_logger.addHandler(my_handler)

    # Test that a log message at level ERROR is logged
    my_logger.error("error message")
    output = my_handler.stream.getvalue()

# Generated at 2022-06-14 06:27:54.889244
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.CRITICAL):
        logger.debug('This is a DEBUG message.')
        assert logger.level == logging.CRITICAL
    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:28:01.878514
# Unit test for function logger_level
def test_logger_level():
    configured = False
    log = get_logger()
    if log.getEffectiveLevel() == logging.DEBUG:
        configured = True

    with logger_level(log, logging.INFO):
        assert log.getEffectiveLevel() == logging.INFO

    if configured:
        assert log.getEffectiveLevel() == logging.DEBUG
    else:
        assert log.getEffectiveLevel() == logging.WARNING
        log.setLevel(logging.DEBUG)

# Generated at 2022-06-14 06:28:04.079493
# Unit test for function get_config
def test_get_config():
    assert get_config(default=DEFAULT_CONFIG) == DEFAULT_CONFIG


# Generated at 2022-06-14 06:28:08.501166
# Unit test for function configure
def test_configure():
    configure()
    logger = logging.getLogger('test_logger')
    logger.info('test_logger')

if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:28:16.511286
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    with logger_level(log, logging.INFO):
        log.critical('critical message')
        log.info('info message')
        log.debug('debug message')
        log.warning('warning message')
        log.log(logging.INFO, 'logging.INFO message')
        log.log(logging.DEBUG, 'logging.DEBUG message')

# Generated at 2022-06-14 06:28:19.652594
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.DEBUG) as level:
        log.debug('hello')
    log.debug('world')



# Generated at 2022-06-14 06:28:25.113958
# Unit test for function get_config
def test_get_config():
    # Test for bare config
    config = get_config(
        'level=DEBUG\nhandlers=console\nloggers=root\nroot.level=DEBUG')
    assert config == {'level': 'DEBUG',
                      'handlers': 'console',
                      'loggers': 'root',
                      'root.level': 'DEBUG'}

    # Test for json config
    config = get_config(
        '{"level": "DEBUG", "handlers": "console", "loggers": "root", "root.level": "DEBUG"}')
    assert config == {'level': 'DEBUG',
                      'handlers': 'console',
                      'loggers': 'root',
                      'root.level': 'DEBUG'}

    # Test for yaml config

# Generated at 2022-06-14 06:28:33.357762
# Unit test for function logger_level
def test_logger_level():
    import logging
    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger("test")
    with logger_level(logger, logging.INFO):
        logger.warn("The logging level of this logger should be INFO.")
    logger.warn("The logging level of this logger should be WARN.")
    logger.setLevel(logging.INFO)
    logger.warn("The logging level of this logger should be INFO.")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:28:43.332704
# Unit test for function logger_level
def test_logger_level():
    log = logbook.Logger("name")
    with logger_level(log, logbook.CRITICAL):
        f = logbook.FileHandler("haha")
        with logger_level(f, logbook.DEBUG):
            log.debug("1")
            log.info("2")
            log.error("3")
        with logger_level(f, logbook.INFO):
            log.debug("4")
            log.info("5")
            log.error("6")
        log.debug("7")
        log.info("8")
        log.error("9")

# Generated at 2022-06-14 06:28:50.445299
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)

    # provided logger should be used.
    assert log.level == logging.NOTSET
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG

    # get_logger should be used if no logger is provided.
    assert log.level == logging.NOTSET
    with logger_level(logging.DEBUG):
        assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:28:53.825936
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.INFO):
        assert l.level == logging.INFO

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:58.932112
# Unit test for function logger_level
def test_logger_level():
    log_test = getLogger("test_logger_level")
    with logger_level(log_test, logging.INFO):
        assert log_test.level == logging.INFO
        log_test.error("test")

    assert log_test.level == logging.DEBUG
    log_test.error("test")  # will fail



# Generated at 2022-06-14 06:29:03.829863
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("logger_level")
    logger.info("Start test")
    with logger_level(logger, logging.DEBUG):
        logger.debug("This debug message is within context block")
    logger.debug("This debug message is outside context block")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:29:16.474683
# Unit test for function logger_level

# Generated at 2022-06-14 06:29:19.186183
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.CRITICAL):
        log.warn("This should not be printed.")
    log.warn("This should be printed.")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:29:24.500094
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.INFO):
        logging.debug('This SHOULD NOT be seen.')
        logging.info('This should be seen.')
        logging.warning('This should be seen.')
        logging.critical('This should be seen.')

# Generated at 2022-06-14 06:29:31.981568
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(), logging.DEBUG):
        get_logger().debug("Should log")
    get_logger().debug("Should not log")
    with logger_level(get_logger(), logging.DEBUG):
        with logger_level(get_logger(), logging.WARNING):
            get_logger().debug("Should not log")
        get_logger().debug("Should log")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:29:42.206401
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    import logging

    # test given config

# Generated at 2022-06-14 06:29:59.233005
# Unit test for function logger_level
def test_logger_level():
    import sys
    import StringIO
    import logging

    # Setup fake logging stream
    _old_stdout = sys.stdout
    try:
        _fake_stdout = StringIO.StringIO()
        sys.stdout = _fake_stdout
        logging.basicConfig(stream=_fake_stdout, level=logging.DEBUG)
        log = logging.getLogger('test')
        # logger_level will set level to INFO
        with logger_level(log, logging.INFO):
            log.warn('test warn')
            log.error('test error')
            log.info('test info')
            log.debug('test debug')

        assert _fake_stdout.getvalue() == 'test error\n' + 'test info\n'
    finally:
        sys.stdout = _old_stdout



# Generated at 2022-06-14 06:30:06.393712
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()

    logger.setLevel(logging.INFO)
    assert logger.level == logging.INFO

    with logger_level(logger, logging.DEBUG):
        logger.debug('should log')
        logger.info('should log')
        assert logger.level == logging.DEBUG

    logger.debug('should not log')
    assert logger.level == logging.INFO

# Generated at 2022-06-14 06:30:11.917821
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('some_logger')
    with logger_level(log, logging.CRITICAL):
        log.info('this text will not appear')
        log.critical('this text will appear')
    log.info('this text should reappear')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:19.328718
# Unit test for function logger_level
def test_logger_level():
    """
    >>> test_logger_level()
    INFO hello
    """
    configure()
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        logger.debug('hello')
        logger.info('hello')
        # logger.debug('hello')


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:30:24.195357
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        logger.info('logger_level worked')
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:30:36.291000
# Unit test for function configure

# Generated at 2022-06-14 06:30:42.071849
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    # default logging level is WARNING
    log.info('testing')

    with logger_level(logger=log, level=logging.INFO):
        log.info('testing')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:48.564387
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger('demo')
    logger.setLevel(logging.DEBUG)
    logger.debug('logging at level DEBUG')
    with logger_level(logger, logging.WARN):
        logger.debug('THIS IS NOT LOGGED')
        logger.warn('this is logged')


# Generated at 2022-06-14 06:31:01.363823
# Unit test for function get_config
def test_get_config():
    print("Test get_config")
    cfg = get_config(config={})
    assert cfg == {}
    cfg = get_config(config='{"name":"value"}')
    assert cfg == {"name": "value"}
    cfg = get_config(config='name:value')
    assert cfg == {"name": "value"}
    os.environ["LOGGING"] = '{"name":"value"}'
    cfg = get_config(env_var='LOGGING')
    assert cfg == {"name": "value"}
    os.environ["LOGGING"] = 'name:value'
    try:
        cfg = get_config(env_var='LOGGING')
        assert cfg == {"name": "value"}
    except Exception:
        import traceback
        traceback.print_exc

# Generated at 2022-06-14 06:31:06.459350
# Unit test for function logger_level
def test_logger_level():
    from logging import DEBUG, INFO

    logger = get_logger()

    # When logger level is INFO
    with logger_level(logger, INFO):
        logger.debug('Should not be logged.')
        logger.error('Should be logged.')

    # When logger level is DEBUG
    with logger_level(logger, DEBUG):
        logger.debug('Should be logged.')
        logger.error('Should be logged.')


# Utility function to log parameter values at entry and exit of a function

# Generated at 2022-06-14 06:31:13.652455
# Unit test for function logger_level
def test_logger_level():
    class FakeLogger(object):
        level = None
        def setLevel(self, level):
            self.level = level

    logger = Fa

# Generated at 2022-06-14 06:31:22.947423
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    assert(log.getEffectiveLevel() == logging.DEBUG)
    with logger_level(log, logging.INFO):
        assert(log.getEffectiveLevel() == logging.INFO)
    assert(log.getEffectiveLevel() == logging.DEBUG)


# Deprecated alias
with_logger_level = logger_level

__all__ = [
    'getLogger',
    'configure',
    'get_config',
    'logger_level',
    'with_logger_level',
]

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:25.977556
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level != logging.DEBUG

# Generated at 2022-06-14 06:31:32.019078
# Unit test for function configure
def test_configure():
    import json

    config = get_config(default=DEFAULT_CONFIG)
    config = json.dumps(config)
    configure(config=config)
    assert logging.getLogger('test_configure').getEffectiveLevel() == logging.DEBUG


if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:31:40.627207
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger()
    configure()
    
    # Should raise nothing
    try:
        with logger_level(log, logging.DEBUG):
            log.debug("test")
    except:
        assert False
    
    # Should raise error
    try:
        with logger_level(log, logging.CRITICAL):
            log.debug("test")
            assert False
    except:
        assert True
    
    # Should raise error
    try:
        with logger_level(log, logging.CRITICAL):
            log.critical("test")
            assert False
    except:
        assert True
    
    # Should raise error

# Generated at 2022-06-14 06:31:49.016082
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('test')
        log.info('test')
    with logger_level(log, logging.WARNING):
        log.warning('test')
        log.info('test')
    try:
        with logger_level(log, logging.CRITICAL):
            raise RuntimeError('test')
    except RuntimeError:
        pass

# Generated at 2022-06-14 06:31:57.301359
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level != logging.DEBUG


if __name__ == '__main__':
    log = getLogger(__name__)
    log.info('test info')
    log.debug('test debug')
    log.warning('test warning')
    log.error('test error')
    log.critical('test critical')

    test_logger_level()

# Generated at 2022-06-14 06:32:02.011444
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    with logger_level(log, logging.DEBUG) as l:
        log.debug('This should print')
        log.info('This should not print')


# simple logger shortcut

# Generated at 2022-06-14 06:32:09.554366
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)
    logger.handlers = []
    logger.addHandler(logging.StreamHandler())
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
        assert logger.isEnabledFor(logging.INFO)
    assert logger.getEffectiveLevel() == logging.WARNING
    assert not logger.isEnabledFor(logging.DEBUG)
    assert not logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:32:13.834143
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    log.setLevel(logging.WARN)
    with logger_level(log, logging.DEBUG):
        log.debug('this message should be printed')
        log.info('this message should be printed')
    log.debug('this message should not be printed')
    log.info('this message should not be printed')

# Generated at 2022-06-14 06:32:24.292442
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug')
        logger.info('info')
        logger.warn('warn')
        logger.error('error')
        logger.critical('critical')



# Generated at 2022-06-14 06:32:36.635515
# Unit test for function logger_level
def test_logger_level():
    """Tests function logger_level."""
    # set up test logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    logger.addHandler(stream)

    # case 1: INFO
    with logger_level(logger, logging.INFO):
        logger.debug('debug 1')
        logger.info('info 1')
        logger.warning('warning 1')
        logger.error('error 1')
        logger.critical('critical 1')

    # case 2: WARNING
    with logger_level(logger, logging.WARNING):
        logger.debug('debug 2')
        logger.info('info 2')
        logger.warning('warning 2')
        logger.error('error 2')
        logger

# Generated at 2022-06-14 06:32:40.429953
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.INFO):
        log.debug("Should not be logged")
        log.info("Should be logged")

if __name__ == "__main__":
    configure()
    test_logger_level()

# Generated at 2022-06-14 06:32:48.201051
# Unit test for function logger_level
def test_logger_level():
    import logging
    import os
    logger = logging.getLogger("test_logger_level")
    with logger_level(logger, logging.INFO):
        logger.debug("debug")
        logger.info("info")
        logger.warn("warn")
        logger.error("error")
        logger.critical("critical")
    with logger_level(logger, logging.DEBUG):
        logger.debug("debug")
        logger.info("info")
        logger.warn("warn")
        logger.error("error")
        logger.critical("critical")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:32:51.161032
# Unit test for function configure
def test_configure():
    configure()
    log = logging.getLogger(__name__)
    log.info('test')


# Generated at 2022-06-14 06:32:58.098072
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.CRITICAL):
        logger.warning('This should not be seen.')
        logger.critical('This should be seen.')
    logger.warning('This should be seen.')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:33:06.927607
# Unit test for function logger_level
def test_logger_level():
  from StringIO import StringIO
  import sys

  logger = logging.getLogger(__name__)

  # save stdout for later
  stdout = sys.stdout
  # create a string version of it
  sys.stdout = StringIO()


# Generated at 2022-06-14 06:33:13.192818
# Unit test for function logger_level
def test_logger_level():
    logger = getlogger('test_logger_level')

    with logger_level(logger, logging.CRITICAL):
        logger.warning('this warning should not show')
        logger.error('this error should not show')
    logger.warning('this warning should show')



# Generated at 2022-06-14 06:33:22.777711
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.DEBUG)
    # Create a logging handler to handle the DEBUG level messages
    ch = logging.NullHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    with logger_level(logger, logging.DEBUG) as l:
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')
    assert logger.level == logging.DEBUG, 'Logging level is not set to DEBUG'
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
    assert logger.level == logging

# Generated at 2022-06-14 06:33:35.372528
# Unit test for function logger_level
def test_logger_level():
    from StringIO import StringIO
    import logging
    import unittest

    class LoggerLevelTestCase(unittest.TestCase):
        def setUp(self):
            super(LoggerLevelTestCase, self).setUp()
            self.sio = StringIO()
            self.log = logging.getLogger('test_logger_level')
            self.log.addHandler(logging.StreamHandler(self.sio))

        def tearDown(self):
            super(LoggerLevelTestCase, self).tearDown()
            self.log.removeHandler('test_logger_level')
            self.log.setLevel(logging.ERROR)

        def test_logger_level(self):
            '''Test that logger level is set to the given level and then reset.'''
            # Test that logger level is set

# Generated at 2022-06-14 06:33:45.930679
# Unit test for function configure
def test_configure():
    logger = get_logger()
    assert logger.level == logging.DEBUG

    logger.setLevel(logging.INFO)
    logger.info("This is a test")
    logger.warning("This is a warning")
    logger.error("This is an error")
    logger.critical("This is a critical")
    assert True

# Generated at 2022-06-14 06:33:48.164337
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    with logger_level(logger, logging.DEBUG):
        logger.debug('test')

# Generated at 2022-06-14 06:33:53.160712
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger("test")
    with logger_level(log, logging.INFO):
        log.debug("info")
        log.info("debug")
    log.debug("debug")
    log.info("info")

test_logger_level()

# Generated at 2022-06-14 06:33:58.980730
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.INFO):
        assert log.getEffectiveLevel() == logging.INFO, 'Level incorrectly set to {}'.format(log.getEffectiveLevel())
    assert log.getEffectiveLevel() != logging.INFO, 'Level not reset'



# Generated at 2022-06-14 06:34:06.864082
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)

    # Default logging level is warning
    with logger_level(log, logging.DEBUG):
        log.debug("debug")
        log.info("info")
        log.warning("warning")
        log.error("error")
        log.critical("critical")
    # Here the logger level is warning again


# Generated at 2022-06-14 06:34:13.971388
# Unit test for function logger_level
def test_logger_level():
    import StringIO
    import time
    import threading
    io = StringIO.StringIO()
    logging.basicConfig(stream=io)
    log = getLogger()
    def log_msg():
        log.info("info")
        log.debug("debug")
    # LOGGING should be disabled by default, so only info should be logged.
    log.info("pre info")
    log.debug("pre debug")
    t = threading.Thread(target=log_msg)
    t.start()
    # Give the thread time to write its log lines.
    time.sleep(0.1)
    log.info("post info")
    log.debug("post debug")
    t.join()
    io.seek(0)
    # Make sure no debug messages were logged.

# Generated at 2022-06-14 06:34:25.282553
# Unit test for function get_config
def test_get_config():
    assert get_config({"1":1}) == {"1":1}
    assert get_config("{\"1\":1}") == {"1":1}
    assert get_config("{'1':1}") == {"1":1}
    assert get_config("1: 1") == {"1":1}
    assert get_config("1: 1\n2: 2") == {"1":1, "2":2}
    assert get_config("1: 1\n2: 2", "test") == {"1":1, "2":2}
    assert get_config("1: 1\n2: 2", "test", "test") == {"1":1, "2":2}


# Generated at 2022-06-14 06:34:30.027761
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    # given a logger
    # then we set it to a new level within a context
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
    # and we leave the level unchanged
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:34:35.687747
# Unit test for function logger_level
def test_logger_level():
    import time

    logger = get_logger('x')
    logger.setLevel(logging.DEBUG)
    logger.info('foo')

    with logger_level(logger, logging.WARNING):
        logger.info('bar')
        logger.debug('baz')

    logger.info('baz')



# Generated at 2022-06-14 06:34:39.780643
# Unit test for function get_config
def test_get_config():
    test_config = get_config(None, None, "log_config.yaml")
    assert test_config
    assert test_config["formatters"]
    assert test_config["handlers"]
    assert test_config["loggers"]
    return

# Generated at 2022-06-14 06:34:51.462945
# Unit test for function logger_level
def test_logger_level():
    import logging.config
    logging.config.dictConfig(DEFAULT_CONFIG)
    l = logging.getLogger()
    assert l.level == logging.DEBUG
    with logger_level(l,logging.INFO):
        assert l.level == logging.INFO
    assert l.level == logging.DEBUG
    l.debug('hello')



# Generated at 2022-06-14 06:34:58.521358
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
        logger.debug('Should not be seen')
        logger.info('Should not be seen')
        logger.warning('Should not be seen')
        logger.error('Should not be seen')
        logger.critical('Should be seen')
    assert logger.level != logging.CRITICAL

# Generated at 2022-06-14 06:35:09.951529
# Unit test for function logger_level
def test_logger_level():
    import logging

    logging.basicConfig()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    with logger_level(logger, logging.WARNING):
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    if '--run-unittests' in sys.argv:
        test_logger_level()