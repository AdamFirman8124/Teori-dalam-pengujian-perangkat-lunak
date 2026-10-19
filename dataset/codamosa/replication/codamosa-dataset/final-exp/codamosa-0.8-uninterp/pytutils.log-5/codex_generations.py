

# Generated at 2022-06-14 06:25:14.212223
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger('test_logger_level')
    >>> with logger_level(log, logging.DEBUG):
    ...    with logger_level(log, logging.INFO):
    ...        log.debug('test')
    ...
    >>>
    """



# Generated at 2022-06-14 06:25:22.817572
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    logger = logging.getLogger('test')

    def log(level, msg):
        logger.log(level, msg)

    with logger_level(logger, logging.DEBUG):
        log(logging.CRITICAL, "critical")
        log(logging.ERROR, "error")
        log(logging.WARN, "warn")
        log(logging.INFO, "info")
        log(logging.DEBUG, "debug")

    assert logger.level == logging.INFO
    with logger_level(logger, logging.INFO):
        log(logging.CRITICAL, "critical")
        log(logging.ERROR, "error")
        log(logging.WARN, "warn")
        log(logging.INFO, "info")

# Generated at 2022-06-14 06:25:28.988620
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    err = StringIO()
    # Change to a known level and try again
    old_level = log.level
    old_handler = log.handlers[0]
    log.level = logging.DEBUG
    try:
        # Set the logging level to a known level.
        with logger_level(log, logging.DEBUG):
            assert log.level == logging.DEBUG
            log.handlers = [logging.StreamHandler(err)]
            log.debug("Debug output")
            log.info("Info output")
            log.error("Error output")
            log.critical("Critical output")
            for line in err.getvalue().strip().splitlines():
                assert line.endswith("output")
    finally:
        log.level = old_level
        log.handlers = old_handler

# Generated at 2022-06-14 06:25:39.055635
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__ + ".test_logger_level")
    initial_level = logger.level

    # Test for a logger level of DEBUG
    try:
        with logger_level(logger, logging.DEBUG):
            assert logger.level == logging.DEBUG
            logger.debug("A debug log")
    except AssertionError:
        raise AssertionError("logger_level() was not able to set the the logger level to DEBUG.")

    # Test for a logger level of DEBUG
    try:
        with logger_level(logger, logging.INFO):
            assert logger.level == logging.INFO
            logger.info("An info log")
    except AssertionError:
        raise AssertionError("logger_level() was not able to set the the logger level to INFO.")

    # Test that the logger level gets

# Generated at 2022-06-14 06:25:49.092157
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import StringIO
    import logging

    class StringHandler(logging.StreamHandler):
        def __init__(self):
            logging.StreamHandler.__init__(self, StringIO.StringIO())
        @property
        def contents(self):
            return self.stream.getvalue()

    class TestLoggerLevel(unittest.TestCase):
        def test_level(self):
            logger = logging.getLogger('test_level')
            logger.addHandler(StringHandler())
            logger.setLevel(logging.WARN)
            with logger_level(logger, logging.INFO):
                logger.debug('This should not show up')
                logger.info('This should be shown')

            self.assertNotIn('This should not show up', logger.handlers[0].contents)
            self

# Generated at 2022-06-14 06:25:53.139211
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level != logging.DEBUG
    logger.handlers.clear()


# Generated at 2022-06-14 06:26:02.069135
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)

    # This log statement should be suppressed
    logger.log(logging.DEBUG, "Before the context manager")

    level = logging.DEBUG

    with logger_level(logger, level):
        logger.log(logging.DEBUG, "Within the context manager")

    # This log statement should be suppressed
    logger.log(logging.DEBUG, "After the context manager")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:13.125939
# Unit test for function configure
def test_configure():
    import tempfile, os, logging

    logger = logging.getLogger(__name__ + '.test_configure')
    tmpdir = tempfile.gettempdir()

    assert not logger.handlers, "logger shouldn't have any handlers yet"
    configure()
    assert logger.handlers, "logger should now have handlers"

    old_handlers = logger.handlers
    file_handler = logging.FileHandler(os.path.join(tmpdir, 'logging.config.test.log'))
    logger.addHandler(file_handler)
    assert old_handlers != logger.handlers, "logger should now have a FileHandler"

    configure(default={})
    assert logger.handlers == [], "logger should have no handlers"

    logger.addHandler(file_handler)

# Generated at 2022-06-14 06:26:17.926565
# Unit test for function get_config
def test_get_config():
    assert get_config(dict()) == dict()
    assert get_config(True) == True
    assert get_config('{"a": 1}') == {"a": 1}
    assert get_config('a: 1') == {"a": 1}

# Generated at 2022-06-14 06:26:26.511790
# Unit test for function configure

# Generated at 2022-06-14 06:26:40.567657
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.handlers = [logging.StreamHandler(sys.stdout)]

    # To test logger_level, we set logger's level to logging.WARN
    # and verify that the messages up to level-WARN are not being logged.
    # logging.INFO and logging.DEBUG messages should be logged.
    logger.setLevel(logging.WARN)
    with logger_level(logger, logging.DEBUG):
        logger.info("Testing logger_level")
        logger.debug("This should be logged")

    # This should not be logged
    logger.info("Testing logger_level - part 2")



# Generated at 2022-06-14 06:26:53.517991
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os

# Generated at 2022-06-14 06:27:04.984890
# Unit test for function logger_level
def test_logger_level():
    import tempfile


# Generated at 2022-06-14 06:27:08.795214
# Unit test for function logger_level
def test_logger_level():

    logger = get_logger()

    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:27:13.516008
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.info('info message')
        logger.debug('debug message')
    logger.info('info message')
    assert logger.level == logging.NOTSET

# Generated at 2022-06-14 06:27:27.344351
# Unit test for function logger_level
def test_logger_level():
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(message)s',
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': logging.DEBUG,
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': logging.DEBUG,
                'propagate': False,
            },
        },
    })
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.INFO):
        assert logger.getEffectiveLevel() == logging.INFO

# Generated at 2022-06-14 06:27:30.963631
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG


# For backwards compatibility

# Generated at 2022-06-14 06:27:34.884385
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug("hello world!")
        log.info("hello world!")
        log.warning("hello world!")
        log.error("hello world!")
        log.critical("hello world!")


# Generated at 2022-06-14 06:27:38.462910
# Unit test for function get_config
def test_get_config():
    import json
    json_config = json.dumps({'a': 'b'})
    assert get_config(json_config) == {'a': 'b'}



# Generated at 2022-06-14 06:27:48.217618
# Unit test for function get_config
def test_get_config():
    import json


# Generated at 2022-06-14 06:27:56.820512
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)

# Generated at 2022-06-14 06:28:04.343492
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger("logger_level")
    try:
        with logger_level(logger, logging.NOTSET):
            raise Exception("Exception thrown at logger level NOTSET")
    except:
        pass

    with logger_level(logger, logging.DEBUG):
        logger.debug("This is shown with logger at DEBUG")
        logger.info("This is shown with logger at DEBUG")

    with logger_level(logger, logging.INFO):
        logger.debug("This is not shown with logger at INFO")
        logger.info("This is shown with logger at INFO")

# Generated at 2022-06-14 06:28:12.127238
# Unit test for function logger_level
def test_logger_level():
    # logger instance
    logger = getLogger(__name__)
    # logger level = <Logger __main__ (DEBUG)>
    # level into the context = 50 (CRITICAL)
    with logger_level(logger, level=50):
        # logger level = <Logger __main__ (CRITICAL)>
        logger.debug("logger should have level changed to CRITICAL")
    # logger level = <Logger __main__ (DEBUG)>
    logger.debug("logger should have returned to DEBUG")

# Generated at 2022-06-14 06:28:23.568035
# Unit test for function get_config
def test_get_config():
    """Test get_config function properly gets the logging configuration dict
    """
    import json
    import yaml
    default_config = '{"root": {"level": "DEBUG"}}'
    json_config = '{"root": {"level": "INFO"}}'
    yaml_config = 'root:\n  level: INFO'

    # Check that config is used as is when provided
    assert get_config(config={'root': {'level': 'INFO'}}) == \
           {'root': {'level': 'INFO'}}
    # Check that config returns the default config when it is a string
    assert get_config(config=default_config, default=DEFAULT_CONFIG) == \
           json.loads(default_config)
    # Check that config returns the value of the env_var when it is a string
    assert get_config

# Generated at 2022-06-14 06:28:35.080746
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger(__name__)
    >>> with logger_level(log, logging.DEBUG):
    ...     log.debug('DEBUG log')
    ...     log.info('INFO log')
    DEBUG - test_logger_level - DEBUG log
    INFO - test_logger_level - INFO log
    >>> log.info('INFO log') #doctest:+IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    AttributeError: 'NoneType' object has no attribute 'write'
    >>> log.setLevel(logging.INFO)
    >>> log.info('INFO log')
    INFO - test_logger_level - INFO log
    """


# Generated at 2022-06-14 06:28:43.268677
# Unit test for function logger_level
def test_logger_level():
    import sys
    import StringIO
    import logging

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    str = StringIO.StringIO()
    h = logging.StreamHandler(str)
    log.addHandler(h)

    with logger_level(log, logging.CRITICAL):
        log.debug('debug log')
        log.info('info log')
        log.critical('critical log')
        assert str.getvalue() == 'CRITICAL:root:critical log \n'
    # logger level is back to DEBUG
    log.debug('debug log')
    log.info('info log')
    log.warning('warning log')
    log.critical('critical log')

# Generated at 2022-06-14 06:28:46.489791
# Unit test for function configure
def test_configure():
    logger = get_logger('test_configure')
    logger.debug('test_configure')
    assert logger.getEffectiveLevel() == logging.DEBUG



# Generated at 2022-06-14 06:28:56.697817
# Unit test for function logger_level
def test_logger_level():
    # Get logger
    logger = get_logger()
    # Create a stream handler to capture the log stream
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    # Test with stream handler
    logger.addHandler(stream_handler)
    # Check logger is at DEBUG level
    assert logger.level == logging.DEBUG
    # Capture log messages
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    # Test logger_level function
    with logger_level(logger, logging.ERROR):
        logger.info('test')
        # Assert that the log stream did not contain the log message
        assert stream.getvalue() == ''
    # Assert that the log stream did contain the error log message

# Generated at 2022-06-14 06:29:02.013486
# Unit test for function logger_level
def test_logger_level():
    log = getLogger("logger_level")
    with logger_level(log, "INFO"):
        log.debug("This won't show")
        log.info("Show this")
    log.debug("This will show")

# For running unit tests from command line
if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:29:07.076852
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.CRITICAL):
        assert log.getEffectiveLevel() == logging.CRITICAL
        log.info('should not show')
    assert log.getEffectiveLevel() != logging.CRITICAL

# Generated at 2022-06-14 06:29:21.900808
# Unit test for function logger_level
def test_logger_level():
    from gevent.monkey import patch_all
    patch_all()

    from gevent import socket, sleep
    from gevent.pool import Pool

    logging.basicConfig(level=logging.DEBUG)
    log = get_logger(__name__)

    def contrived_client(addr):
        import time
        s = socket.create_connection(addr)
        f = s.makefile()
        while True:
            line = f.readline()
            if not line:
                log.debug('EOF')
                break
            time.sleep(.1)
            log.debug('Writing line')
            s.send(b'from client\n')
        s.close()

    def contrived_server(listener):
        import socket
        conn, addr = listener.accept()

# Generated at 2022-06-14 06:29:27.780470
# Unit test for function logger_level
def test_logger_level():
    import logging
    import time

    log = getLogger()

    with logger_level(log, logging.DEBUG):
        log.info('a')
        log.debug('b')
        log.warn('c')

    log.info('a')
    log.debug('b')
    log.warn('c')

    time.sleep(.1)



# Generated at 2022-06-14 06:29:34.114561
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    level_to_test = logging.INFO
    with logger_level(logger, level_to_test):
        assert logger.level == level_to_test


"""

A sample script to execute tests and view output:

import logging
import log

log.configure()

logger = log.get_logger()

logger.info('info')
logger.debug('debug')
logger.warning('warning')
"""

# Generated at 2022-06-14 06:29:37.865386
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.CRITICAL):
        log.debug("Message")
        log.warning("Message")
        assert log.level == logging.CRITICAL

# Generated at 2022-06-14 06:29:44.384991
# Unit test for function logger_level
def test_logger_level():
    import logging
    import coloredlogs

    logger = logging.getLogger('test_logger_level')

    with logger_level(logger, logging.INFO):
        logger.debug('This has to be suppressed')
        logger.info('This has to be shown')
    # Info message has to be shown
    logger.debug('This has to be suppressed as well')
    return



# Generated at 2022-06-14 06:29:50.654895
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.debug('debug')
        log.info('info')
        log.warning('warning')
        log.error('error')
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')

# Generated at 2022-06-14 06:29:59.264789
# Unit test for function logger_level
def test_logger_level():
    import logging

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    with logger_level(log, logging.WARNING):
        log.info('this is a test')
        log.warning('this is a warning')
    log.info("this is a info")
    log.debug("this is a debug")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:06.832982
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    assert(logger.level == logging.DEBUG)

    with logger_level(logger, logging.ERROR):
        assert(logger.level == logging.ERROR)

    assert(logger.level == logging.DEBUG)


if __name__ == '__main__':
    import doctest
    import sys
    import os
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-14 06:30:18.066967
# Unit test for function logger_level
def test_logger_level():
    from logging import INFO
    from io import StringIO
    import sys
    import unittest

    logger = logging.getLogger(__name__)
    logger.setLevel(INFO)
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    logger.info("Before switch to CRITICAL level")

    with logger_level(logger, logging.CRITICAL):
        logger.info("This INFO message is not logged")

    logger.info("Back to INFO level")

    output = stream.getvalue().strip()
    expected = "Before switch to CRITICAL level"
    assert output == expected



# Generated at 2022-06-14 06:30:26.521290
# Unit test for function get_config
def test_get_config():
    import json
    import yaml

    json_cfg = json.dumps(DEFAULT_CONFIG)
    yaml_cfg = yaml.dump(DEFAULT_CONFIG)

    # json as string
    assert get_config(json_cfg) == DEFAULT_CONFIG
    # yaml as string
    assert get_config(yaml_cfg) == DEFAULT_CONFIG
    # dict
    assert get_config(DEFAULT_CONFIG) == DEFAULT_CONFIG



# Generated at 2022-06-14 06:30:50.775268
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('test debug')
        assert logger.isEnabledFor(level=logging.DEBUG)

    with logger_level(logger, logging.ERROR):
        logger.debug('test error')
        assert not logger.isEnabledFor(level=logging.DEBUG)


if __name__ == '__main__':
    configure()
    test_logger_level()
    logging.getLogger('test').debug('test debug')
    logging.getLogger('test').info('test info')

# Generated at 2022-06-14 06:31:00.407741
# Unit test for function get_config
def test_get_config():
    config = get_config(default=DEFAULT_CONFIG)
    assert isinstance(config, dict)
    config = get_config(config=json.dumps(DEFAULT_CONFIG))
    assert isinstance(config, dict)
    config = get_config(config=yaml.dump(DEFAULT_CONFIG))
    assert isinstance(config, dict)
    config = get_config(config='{"version": 1}')
    assert isinstance(config, dict)

    with pytest.raises(ValueError):
        config = get_config(config=None, default=None)



# Generated at 2022-06-14 06:31:04.900955
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()
    with logger_level(logger, logging.DEBUG):
        logger.info('An informational message')
        logger.debug('A debug message')
    logger.info('An informational message')
    logger.debug('A debug message')

# Generated at 2022-06-14 06:31:16.159478
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    # test if already at the right logging level
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG, 'logger level is wrong in the inner block'
    assert logger.level == logging.DEBUG, 'logger level is wrong after the inner block'

    # test if it resets the logging level to its original after exception
    try:
        with logger_level(logger, logging.ERROR):
            assert logger.level == logging.ERROR, 'logger level is wrong in the inner block'
            raise Exception()
    except:
        assert logger.level == logging.DEBUG, 'logger level is wrong after the inner block'

    # test if it resets the logging level to its original

# Generated at 2022-06-14 06:31:28.147183
# Unit test for function get_config
def test_get_config():
    config = get_config(config=None, env_var=None, default=DEFAULT_CONFIG)
    assert config
    
    config = get_config(
        config=None, env_var='LOGGING', default=DEFAULT_CONFIG)
    assert config

    config = get_config(config={}, env_var=None, default=DEFAULT_CONFIG)
    assert config.get('version') == 1


# Generated at 2022-06-14 06:31:38.087133
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)

    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('debug1')
        log.info('info1')
        log.warning('warning1')
        log.error('error1')
        with logger_level(log, logging.INFO):
            log.debug('debug2')
            log.info('info2')
            log.warning('warning2')
            log.error('error2')
        log.debug('debug3')
        log.info('info3')
        log.warning('warning3')
        log.error('error3')



# Generated at 2022-06-14 06:31:42.149802
# Unit test for function get_config
def test_get_config():
    # testing when config == None
    out = get_config(config = None, env_var = 'LOGGING')
    if out == DEFAULT_CONFIG:
        print("test_get_config: Pass")
    else:
        print("test_get_config: Fail")


# Generated at 2022-06-14 06:31:52.322387
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    configure()
    logger_level(log, logging.INFO)
    assert log.level == logging.INFO
    log.error("An error message")
    log.critical("A critical message")
    log.debug("A debug message")
    with logger_level(log, logging.ERROR):
        log.error("An error message")
        log.critical("A critical message")
        log.debug("A debug message")
    assert log.level == logging.INFO



# Generated at 2022-06-14 06:32:00.776370
# Unit test for function get_config
def test_get_config():
    # test if a dict type object will be returned if the dict config is given
    cfg_dict = {'a': 'b'}
    assert isinstance(get_config(given=cfg_dict), dict)
    # test if a dict type object will be returned if the dict config is given
    cfg_json = '{"a": "b"}'
    assert isinstance(get_config(given=cfg_json), dict)
    # test if a dict type object will be returned if the dict config is given
    cfg_yaml = 'a: b'
    assert isinstance(get_config(given=cfg_yaml), dict)


if __name__ == '__main__':
    test_get_config()

# Generated at 2022-06-14 06:32:07.977397
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test.logger_level.test')
    with logger_level(log, logging.WARNING):
        log.setLevel(logging.WARNING)
        log.info('Test warning')
        log.warning('Test warning inside context 1')
    log.error('Test error')
    with logger_level(log, logging.ERROR):
        log.setLevel(logging.ERROR)
        log.error('Test error inside context 2')
        log.warning('Test warning inside context 2')
        log.info('Test info inside context 2')



# Generated at 2022-06-14 06:32:47.777714
# Unit test for function get_config
def test_get_config():
    s = '{"version":1,"handlers":{"console":{"class":"logging.StreamHandler","formatter":"colored","level":10,"stream":"ext://sys.stdout"}},"loggers":{"TEST":{"level":40,"handlers":["console"],"propagate":false}},"formatters":{"colored":{"()":"colorlog.ColoredFormatter","format":"%(bg_black)s%(log_color)s[%(asctime)s] [%(name)s/%(process)d] %(message)s %(blue)s@%(funcName)s:%(lineno)d #%(levelname)s%(reset)s","datefmt":"%H:%M:%S"}}}'
    assert get_config(s) == DEFAULT_CONFIG

# Generated at 2022-06-14 06:32:59.111132
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(stream_handler)

    with logger_level(logger, logging.DEBUG):
        logger.info("test info")
        logger.debug("test debug")
        logger.critical("test critical")
    logger.info("test info after")


if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:33:05.841149
# Unit test for function logger_level
def test_logger_level():
    import time
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug("Debug message")
    with logger_level(logger, logging.INFO):
        logger.info("Info message")
    with logger_level(logger, logging.WARNING):
        logger.warning("Warning message")
    with logger_level(logger, logging.ERROR):
        logger.error("Error message")
    time.sleep(1)
    logger.critical("Critical message")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:33:12.615853
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()

    assert logging.ERROR == log.getEffectiveLevel()

    with logger_level(log, logging.INFO):
        assert logging.INFO == log.getEffectiveLevel()

    assert logging.ERROR == log.getEffectiveLevel()

# Generated at 2022-06-14 06:33:16.132571
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger(), logging.ERROR):
        assert getLogger().getEffectiveLevel() == logging.ERROR
    assert getLogger().getEffectiveLevel() == logging.DEBUG


# Generated at 2022-06-14 06:33:24.153156
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

    # Setting level to DEBUG, expect to see DEBUG and INFO
    with logger_level(log, logging.DEBUG):
        log.debug('%s: test_logger_level', __name__)
        log.info('%s: test_logger_level', __name__)

    # Setting level to INFO, expect to see INFO and WARNING
    with logger_level(log, logging.INFO):
        log.info('%s: test_logger_level', __name__)
        log.warning('%s: test_logger_level', __name__)

    # Setting level to WARNING, expect to see WARNING and ERROR
    with logger_level(log, logging.WARNING):
        log.warning('%s: test_logger_level', __name__)

# Generated at 2022-06-14 06:33:29.474650
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(__name__), logging.DEBUG):
        logging.debug('test_logger_level')
        assert logging.getLogger(__name__).level == logging.DEBUG
    assert logging.getLogger(__name__).level != logging.DEBUG

test_logger_level()

# Generated at 2022-06-14 06:33:34.781913
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    logger_level(log, logging.WARNING)
    log.info('hi')  # Shouldn't print anything
    assert log.level == logging.WARNING
    logger_level(log, logging.INFO)
    log.info('hi')  # Should print 'hi'

# Generated at 2022-06-14 06:33:37.979762
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger("test_logger_level"), logging.CRITICAL):
        assert getLogger("test_logger_level").level == logging.CRITICAL
    assert getLogger("test_logger_level").level != logging.CRITICAL

# Generated at 2022-06-14 06:33:41.436635
# Unit test for function get_config
def test_get_config():
    config = get_config('{"version": 1, "disable_existing_loggers": false}')
    assert config == {'version': 1, 'disable_existing_loggers': False}

# Generated at 2022-06-14 06:34:56.921081
# Unit test for function logger_level
def test_logger_level():
    import time
    from logging import getLogger
    log = getLogger('test')
    msg = "Logging this message at level %s"

    for level in ('debug', 'info', 'warning', 'error', 'critical'):
        log_level = getattr(log, level)
        log_level(msg % level)

    log.debug("Debug this message")
    log.info("Info this message")
    log.warning("Warning this message")
    log.error("Error this message")
    log.critical("Critical this message")


# Generated at 2022-06-14 06:35:07.662406
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.config
    import os

    from six import StringIO

    from pytest import raises

    from logging_helpers import logger_level, configure

    log = logging.getLogger('test')

    old = os.environ.get('LOGGING')
    os.environ['LOGGING'] = '{}'
    configure()

    with logger_level(log, logging.DEBUG):
        log.debug('hi')

    with raises(ValueError):
        logger_level(log, logging.DEBUG)

    os.environ['LOGGING'] = old
    configure()

