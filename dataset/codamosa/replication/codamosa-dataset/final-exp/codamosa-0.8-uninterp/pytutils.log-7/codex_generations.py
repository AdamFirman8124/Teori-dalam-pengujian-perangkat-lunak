

# Generated at 2022-06-14 06:25:14.024584
# Unit test for function logger_level
def test_logger_level():
    logger1 = get_logger("test_logger_level")
    logger1.setLevel(logging.INFO)

    with logger_level(logger1, logging.DEBUG):
        logger1.debug("Hello")

# Generated at 2022-06-14 06:25:17.993825
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.INFO):
        log.info("This should be logged")
    log.debug("This should not be logged.")
test_logger_level()

# Generated at 2022-06-14 06:25:22.527012
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.INFO):
        l.debug('debug')
        l.info('info')
    l.debug('debug')


# vim: et:sw=4:syntax=python:ts=4:

# Generated at 2022-06-14 06:25:31.161274
# Unit test for function get_config
def test_get_config():
    print ("Testing get_config")
    print ("Testing get_config with bare config")

# Generated at 2022-06-14 06:25:44.646261
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.CRITICAL):
        log.info('test')
        log.error('test')
        log.critical('test')

        assert log.handlers, 'handlers'
        assert len(log.handlers) == 1, 'len(handlers)'
        assert log.handlers[0], 'log.handlers[0]'

        assert isinstance(log.handlers[0], logging.StreamHandler), 'lh'
        h = log.handlers[0]

        assert isinstance(h.stream, io.TextIOBase), 'stream'

        h.stream = io.StringIO()
        h.emit(logging.LogRecord('name', logging.INFO, 'pathname', 0, 'test1', (), None))

# Generated at 2022-06-14 06:25:54.297602
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    with logger_level(logger, logging.CRITICAL):
        logger.debug('this will not be printed')
        logger.info('this will not be printed')
        logger.warning('this will not be printed')
        logger.error('this will not be printed')
        logger.critical('this will be printed')

    with logger_level(logger, logging.DEBUG):
        logger.debug('this will be printed')
        logger.info('this will be printed')
        logger.warning('this will be printed')
        logger.error('this will be printed')
        logger.critical('this will be printed')

import unittest


# Generated at 2022-06-14 06:26:05.367594
# Unit test for function logger_level
def test_logger_level():
    import logging, tempfile
    logger = logging.getLogger('test_logger_level')
    fd, tmp = tempfile.mkstemp()
    lh = logging.FileHandler(tmp)
    lh.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(lh)
    logger.setLevel(logging.DEBUG)

    logger.debug('debug')
    logger.info('info')
    logger.error('error')

    with logger_level(logger, logging.INFO):
        logger.debug('debug')
        logger.info('info')
        logger.error('error')

    logger.debug('debug')
    logger.info('info')
    logger.error('error')


# Generated at 2022-06-14 06:26:15.387349
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    import io

    from contextlib import contextmanager

    @contextmanager
    def capture_logging_stderr(logger):
        original = logger.handlers[0].stream
        captured = io.StringIO()
        try:
            logger.handlers[0].stream = captured
            yield captured
        finally:
            logger.handlers[0].stream = original

    def _is_logged(captured, expected):
        captured_value = captured.getvalue()
        expected_value = expected + '\n'
        return captured_value == expected_value

    configure(DEFAULT_CONFIG)
    logger = get_logger()

    with capture_logging_stderr(logger) as captured:
        with logger_level(logger, logging.CRITICAL):
            logger

# Generated at 2022-06-14 06:26:25.627078
# Unit test for function get_config
def test_get_config():

    config = get_config(default='{"version": 1, "formatters": {"simple": {"format":"%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s","datefmt":"%Y-%m-%d %H:%M:%S"}}}', env_var="LOGGING")

# Generated at 2022-06-14 06:26:32.216451
# Unit test for function logger_level
def test_logger_level():
    # Check ValueError
    logger = logging.getLogger(__name__)

    try:
        logger_level(logger, 'ERROR')
    except ValueError:
        pass

    logger_level(logger, logging.ERROR)
    logger_level(logger, logging.INFO)
    logger_level(logger, logging.WARNING)
    logger_level(logger, logging.DEBUG)

# Generated at 2022-06-14 06:26:39.230741
# Unit test for function logger_level
def test_logger_level():
    # TODO: Test that this is actually logging
    logger = get_logger(__name__)
    logger.debug('basic debug')

    with logger_level(logger, logging.INFO):
        logger.debug('suppressed debug')

    logger.debug('restored debug')

# Generated at 2022-06-14 06:26:52.899306
# Unit test for function get_config
def test_get_config():
    # Test case
    import json
    import yaml


# Generated at 2022-06-14 06:27:03.430228
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    from contextlib import contextmanager
    from io import StringIO
    
    def get_logger():
        '''
        Return a logger that writes to string
        '''
        logging.basicConfig(stream=StringIO())
        return logging.getLogger(__name__)

    logger = get_logger()

    with logger_level(logger, logging.DEBUG):
        assert(logger.level == logging.DEBUG)
        logger.debug('test')
        assert(logger.level == logging.DEBUG)

    assert(logger.level == logging.WARNING)
    # logger.handlers[0].stream.getvalue() should return 'test\n'

# Generated at 2022-06-14 06:27:08.292817
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()

    with logger_level(log, logging.INFO):
        log.debug('Inside context')
    log.debug('Outside context')

    output = sys.stdout.getvalue().strip()
    assert output == 'Outside context'


# Generated at 2022-06-14 06:27:14.345153
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> logger = logging.getLogger('test')
    >>> logger.setLevel(logging.INFO)
    >>> logger.info('info')
    >>> with logger_level(logger, logging.DEBUG):
    ...     logger.debug('debug')
    >>> logger.info('info')
    """



# Generated at 2022-06-14 06:27:20.389380
# Unit test for function logger_level
def test_logger_level():
    """
    Test logger_level context manager
    """
    log = getLogger()
    log.setLevel(logging.INFO)
    with logger_level(log, logging.DEBUG):
        log.debug("debug01")
        log.info("info01")
    log.debug("debug02")
    log.info("info02")

# Generated at 2022-06-14 06:27:27.819555
# Unit test for function get_config
def test_get_config():
    # Plain string
    cfg = 'asdf'
    assert get_config(cfg) == 'asdf'

    # JSON string
    assert get_config('{"asdf": "asdf"}') == {"asdf": "asdf"}

    # YAML string
    assert get_config('asdf: asdf') == {"asdf": "asdf"}


if __name__ == '__main__':
    import sys

    def _main():
        configure()

        log = get_logger()

        level = sys.argv[1] if len(sys.argv) >= 2 else "info"

        if level == "critical":
            log.critical("critical")
        if level == "error":
            log.error("error")
        if level == "warning":
            log.warning("warning")

# Generated at 2022-06-14 06:27:32.131632
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger.level is NOTSET

    with logger_level(logger, logging.INFO):
        assert logger.level is logging.INFO

    assert logger.level is NOTSET



# Generated at 2022-06-14 06:27:45.374555
# Unit test for function logger_level
def test_logger_level():
    import logging
    import time
    import multiprocessing
    import Queue

    # Get logger
    logger = get_logger(__name__ + ".logger_level_test")

    # Make a queue to receive logging messages
    received = multiprocessing.Queue()
    output = Queue.Queue()

    # Make a handler to push log messages to the queue
    class QueueHandler(logging.Handler):
        def emit(self, record):
            output.put(record)

    # Add the queue handler to the logger
    logger.addHandler(QueueHandler())

    # Set the logger's level to DEBUG
    logger.setLevel(logging.DEBUG)

    # Log a debug message
    logger.debug("before")

    # With the logger at debug, time.sleep should yield a logged message

# Generated at 2022-06-14 06:27:50.730798
# Unit test for function logger_level
def test_logger_level():
    """Test logger_level context manager

    >>> log = get_logger()
    >>> with logger_level(log, logging.DEBUG):
    ...     log.debug('This is DEBUG level log')
    ...     log.info('This is INFO level log')

    >>> with logger_level(log, logging.INFO):
    ...     log.debug('This is DEBUG level log')
    ...     log.info('This is INFO level log')
    """
    pass



# Generated at 2022-06-14 06:28:00.901731
# Unit test for function logger_level
def test_logger_level():
    """
    >>> with logger_level(getLogger(), logging.INFO):
    ...     getLogger().error('oops')
    ...     getLogger().warning('uh oh')
    ...     getLogger().info('meh')
    ...     getLogger().debug('yadda yadda')
    oops
    uh oh
    meh
    """



# Generated at 2022-06-14 06:28:11.748051
# Unit test for function configure
def test_configure():
    import json
    import logging
    import os
    import sys
    import tempfile

    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
        f.write(json.dumps(DEFAULT_CONFIG))

    try:
        os.environ['LOGGING'] = f.name

        configure()

        logger = get_logger()

        for msg in (
            'test',
            'test2',
        ):
            logger.info(msg)
            logger.warn(msg)
            logger.debug(msg)
    finally:
        os.unlink(f.name)
        del os.environ['LOGGING']



# Generated at 2022-06-14 06:28:18.205007
# Unit test for function configure
def test_configure():
    logger = logging.getLogger('dummy')
    logger.setLevel(logging.WARNING)
    # logging.warning('dummy config')

    configure()
    logger.debug('dummy debug config')
    logger.info('dummy info config')


if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:28:21.416027
# Unit test for function configure
def test_configure():
    configure()
    logger = get_logger()
    logger.info('test_configure')
    logger.debug('test_configure')
    logger.error('test_configure')


# Generated at 2022-06-14 06:28:35.129665
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.CRITICAL + 1)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    with logger_level(logger, logging.DEBUG):
        logger.debug("This message should be logged")
    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
        logger.warning("This message should be logged")
    assert logger.getEffectiveLevel() == logging.WARNING
    assert logger.level == logging.WARNING
    with logger_level(logger, logging.CRITICAL + 1):
        logger.debug("This message should not be logged")
    with logger_level(logger, logging.CRITICAL + 1):
        assert logger.getEffectiveLevel() == logging.CRITICAL + 1
       

# Generated at 2022-06-14 06:28:42.187579
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger("test_logger_level")
    logger.setLevel(logging.DEBUG)

    assert logger.getEffectiveLevel() == 10, "Default log level is not DEBUG."

    logger.debug("test_debug")
    logger.info("test_info")

    with logger_level(logger, logging.INFO):
        assert logger.getEffectiveLevel() == 20, "Log level is not INFO."
        logger.debug("should_not_appear")
        logger.info("test_info2")
    assert logger.getEffectiveLevel() == 10, "Log level is not reset to DEBUG."

    logger.debug("test_debug2")
    logger.info("test_info3")

# Generated at 2022-06-14 06:28:54.735836
# Unit test for function configure
def test_configure():
    log = get_logger(__name__)
    print(log.level)
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:28:59.332256
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.CRITICAL):
        log.info("This shouldn't be printed")
        log.critical("Crital!!!")
        log.error("This too should not be printed.")
    log.info("This should be printed")
    log.error("This too")

# Generated at 2022-06-14 06:29:03.030093
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.info('info')
        
    log.debug('debug')
    log.info('info')


# Generated at 2022-06-14 06:29:16.032495
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import io

    class MyTest(unittest.TestCase):
        def test_logger_level(self):
            import logging
            import os

            logger = logging.getLogger(__name__)

            def check_logger(level, msg):
                with logger_level(logger, level):
                    logger.debug('debug')
                    logger.info('info')
                    logger.error('error')

                with io.StringIO() as buf:
                    handler = logging.StreamHandler(buf)
                    logger.addHandler(handler)

                    with logger_level(logger, level):
                        logger.debug('debug')
                        logger.info('info')
                        logger.error('error')

                    logger.handlers.remove(handler)
                    out = buf.getvalue().strip()
                    self.assertE

# Generated at 2022-06-14 06:29:36.633772
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logger_level')
    level = log.getEffectiveLevel()

    # check at INFO level
    log.setLevel(logging.INFO)
    log.debug('should not see this')
    with logger_level(log, logging.DEBUG):
        log.debug('should see DEBUG msg')
    log.debug('should not see this')
    assert log.getEffectiveLevel() == level

    # check at DEBUG level
    log.setLevel(logging.DEBUG)
    log.debug('should see DEBUG msg')
    with logger_level(log, logging.INFO):
        log.debug('should not see DEBUG msg')
    log.debug('should see DEBUG msg')
    assert log.getEffectiveLevel() == level

    # check default level
    log.setLevel(logging.DEBUG)
    log

# Generated at 2022-06-14 06:29:49.087121
# Unit test for function logger_level
def test_logger_level():
    import logging
    import time

    # Configure a logger

# Generated at 2022-06-14 06:29:51.074947
# Unit test for function configure
def test_configure():
    with logger_level(get_logger(), logging.DEBUG):
        configure()
        log = get_logger()

    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:30:04.757377
# Unit test for function get_config
def test_get_config():
    assert get_config('{"a": "b"}') == {"a": "b"}
    assert get_config("a: b") == {"a": "b"}
    assert get_config("a: b", default={'c': 'd'}) == {"a": "b"}
    assert get_config("a: b", default={'c': 'd'}, env_var=None) == {"a": "b"}
    assert get_config("a: b", env_var='LOGGING', default={'c': 'd'}) == {"a": "b"}
    assert get_config("a: b", env_var=None, default={'c': 'd'}) == {"a": "b"}
    assert get_config(None, env_var=None, default={'c': 'd'}) == {'c': 'd'}

# Generated at 2022-06-14 06:30:08.159377
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        assert logger.getEffectiveLevel() == logging.INFO
    assert logger.getEffectiveLevel() == logging.DEBUG


# Generated at 2022-06-14 06:30:20.930680
# Unit test for function logger_level
def test_logger_level():
    # Test logger_level(logger, level) function with log level DEBUG
    logger_test = get_logger()
    logger_test.debug("Test log message - DEBUG")
    with logger_level(logger_test, logging.DEBUG):
        logger_test.debug("Test log message - DEBUG")
    logger_test.debug("Test log message - DEBUG")

    # Test logger_level(logger, level) function with log level INFO
    logger_test = get_logger()
    logger_test.info("Test log message - INFO")
    with logger_level(logger_test, logging.INFO):
        logger_test.info("Test log message - INFO")
    logger_test.info("Test log message - INFO")

    # Test logger_level(logger, level) function with log level WARNING
    logger_test = get_

# Generated at 2022-06-14 06:30:26.521530
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    assert logger.level == logging.INFO

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG

    assert logger.level == logging.INFO

# Generated at 2022-06-14 06:30:38.579451
# Unit test for function get_config
def test_get_config():
    cfg = get_config()
    assert cfg
    assert not isinstance(cfg, _PyInfo.string_types)

    cfg = get_config('{"a": 1}')
    assert cfg
    assert not isinstance(cfg, _PyInfo.string_types)
    assert "a" in cfg

    cfg = get_config('a: 1', default='{"b": 2}')
    assert cfg
    assert not isinstance(cfg, _PyInfo.string_types)
    assert "b" in cfg

    os.environ['A_B'] = '3'
    cfg = get_config(env_var='A_B')
    assert cfg
    assert isinstance(cfg, _PyInfo.string_types)
    assert cfg == '3'




# Generated at 2022-06-14 06:30:46.596956
# Unit test for function logger_level
def test_logger_level():
    # reset state
    logging.basicConfig(level=logging.NOTSET)
    logger = get_logger(__name__)
    # test state
    assert logger.level == logging.NOTSET
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.NOTSET


__all__ = ['get_logger']

# Generated at 2022-06-14 06:30:49.168590
# Unit test for function configure
def test_configure():
    configure()

    logger = logging.getLogger(__name__)
    logger.info('test_configure')



# Generated at 2022-06-14 06:31:01.916781
# Unit test for function get_config
def test_get_config():
    logging.basicConfig(filename='test_logging.log', level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logger.info('test')
    assert 1 == 1

# Generated at 2022-06-14 06:31:05.641718
# Unit test for function logger_level
def test_logger_level():
    l = get_logger(__name__)
    with logger_level(l, logging.DEBUG):
        l.debug('debugging')
    l.info('info')
    l.warning('warning')
    l.error('error')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:31:19.709147
# Unit test for function logger_level
def test_logger_level():
    def test_f():
        log = getLogger("test_logger_level")
        log.setLevel(logging.ERROR)
        with logger_level(log, logging.DEBUG):
            log.debug("logger_level works")
        log.debug("logger_level fails outside context")

    import io
    import sys

    # Capture print output to a string
    old_stdout = sys.stdout
    try:
        sys.stdout = mystdout = io.StringIO()
        test_f()
        assert mystdout.getvalue() == \
            "logger_level works\n", "logger_level failure"
    finally:
        sys.stdout = old_stdout


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:31:25.074393
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()

    initial = logger.level

    logger.info('initial: %s' % logger.level)
    with logger_level(logger, 30):
        logger.info('inner: %s' % logger.level)
    logger.info('after: %s' % logger.level)

    assert logger.level == initial

# Generated at 2022-06-14 06:31:30.560745
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR

    # Check if logger has been restored to default level
    assert logger.level == logging.DEBUG


_LOGGER_CONTEXT_MAP = {}



# Generated at 2022-06-14 06:31:33.490583
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:31:39.786923
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('Test log')
    log.debug('Test log2')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:42.490771
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.FATAL) as logger:
        assert logger.level == logging.FATAL
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:31:50.517664
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    log.info('logger level BEFORE: %s' % log.level)
    with logger_level(log, logging.DEBUG):
        log.debug('Debug message')
        log.info('Info message')
    log.info('logger level AFTER: %s' % log.level)

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:57.237703
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> log = getLogger(__name__)
    >>> configure()
    >>> with logger_level(log, logging.CRITICAL):
    ...     log.debug('should not log: %s', 1)
    >>> with logger_level(log, logging.DEBUG):
    ...     log.debug('should log: %s', 1)
    """


# Generated at 2022-06-14 06:32:15.027241
# Unit test for function get_config
def test_get_config():
    assert get_config(default=DEFAULT_CONFIG) == DEFAULT_CONFIG
    assert get_config(env_var=None) == None
    assert get_config('{"version": "1"}', env_var=None) == {"version": "1"}
    assert get_config('{"version": "1"}', env_var="LOGGING") == {"version": "1"}
    assert get_config({"version": "1"}, env_var="LOGGING") == {"version": "1"}
    assert get_config(["version", "1"], env_var=None) == ["version", "1"]
    assert get_config('version: 1', env_var=None) == {'version': 1}
    assert get_config(None, env_var=None) == None

# Generated at 2022-06-14 06:32:28.135466
# Unit test for function get_config
def test_get_config():
    assert get_config(given=None) == DEFAULT_CONFIG
    assert get_config(given=None, default=None) == None
    logging_config = {
        "handlers": {"console": {"formatter": "colored"}},
        "formatters": {"colored": {"format": "test"}}
    }
    assert get_config(given=logging_config) == logging_config
    logging_config_yaml = """
    handlers:
        console:
            formatter: colored
    formatters:
        colored:
            format: test
    """
    assert get_config(given=logging_config_yaml) == logging_config

# Generated at 2022-06-14 06:32:32.797956
# Unit test for function configure
def test_configure():
    configure(DEFAULT_CONFIG)
    log = logging.getLogger(__name__)
    log.info('test')

if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:32:44.055113
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()

    # test that the logger level is set within the context block, and returned to the original level outside
    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
    assert logger.level == logging.DEBUG

    # test that an exception within the context block returns the logger level properly
    try:
        with logger_level(logger, logging.CRITICAL):
            assert logger.level == logging.CRITICAL
            raise Exception()
    except Exception:
        pass
    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:32:49.345371
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    try:
        with logger_level(logger, logging.DEBUG):
            # logger is at DEBUG level within this block
            logger.debug("Level is now DEBUG")
        # outside the block, level is back to NOTSET, so no logs
        logger.debug("Level is back to NOTSET")
    except Exception as e:
        raise e
    finally:
        # always reset to NOTSET
        logger.level = logging.NOTSET

# Generated at 2022-06-14 06:33:02.995538
# Unit test for function get_config
def test_get_config():
    import json
    import yaml


# Generated at 2022-06-14 06:33:10.252312
# Unit test for function get_config
def test_get_config():
    class FakeConfig(object):
        def __init__(self, **d):
            self.__dict__.update(d)


# Generated at 2022-06-14 06:33:18.297042
# Unit test for function logger_level
def test_logger_level():
    """Unit test to verify function logger_level

    >>> import logging
    >>> logging.basicConfig()
    >>>
    >>> l = logging.getLogger("test")
    >>> l.setLevel(logging.WARNING)
    >>>
    >>> with logger_level(l, logging.DEBUG):
    ...     l.debug("hello!")
    >>>
    >>>
    >>> l.warning("Don't worry, I'm a normal logger")
    """


# Generated at 2022-06-14 06:33:31.297923
# Unit test for function logger_level
def test_logger_level():
    FORMAT = "%(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    log = get_logger()

    # Turn off INFO to make level test more obvious
    # with logger_level(log, logging.WARN):
    log.setLevel(logging.WARN)
    log.warn("logger level = WARN")
    log.info("logger level = WARN")
    log.error("logger level = WARN")

    # with logger_level(log, logging.ERROR):
    log.setLevel(logging.ERROR)
    log.warn("logger level = ERROR")
    log.info("logger level = ERROR")
    log.error("logger level = ERROR")

    # with logger_level(log, logging.INFO):

# Generated at 2022-06-14 06:33:39.743888
# Unit test for function configure
def test_configure():
    import ast
    import json
    import yaml

    # Test configuration dictionary
    # logging.debug('Testing logger using dictConfig')
    config = dict(
        version=1,
        root=dict(level='DEBUG'),
        loggers={
            'mylogger': dict(level='DEBUG'),
        },
    )

    configure(config)
    logger = get_logger('mylogger')
    logger.debug('test')

    # Test configuration dictionary as json
    # logging.debug('Testing logger using dictConfig in json')
    config = json.dumps(config)
    configure(config)
    logger = get_logger('mylogger')
    logger.debug('test')

    # Test configuration dictionary as yaml
    # logging.debug('Testing logger using dictConfig in yaml')

# Generated at 2022-06-14 06:34:04.690846
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()
    # Create a logger
    logger = get_logger()
    # Manually set level to INFO
    logger.level = logging.INFO
    logger.info('This message should log')
    logger.debug('This message should not log')
    with logger_level(logger, logging.DEBUG):
        logger.debug('This message should log')

# Generated at 2022-06-14 06:34:13.334469
# Unit test for function get_config
def test_get_config():
    def test_config(config, expected_cfg):
        assert get_config(config) == expected_cfg

    # Test config is a dict
    config = {"version": 1}
    expected_cfg = {"version": 1}
    test_config(config, expected_cfg)

    # Test config is a string
    config = '{"version": 1}'
    expected_cfg = {"version": 1}
    test_config(config, expected_cfg)

    # Test config is a string (json)
    config = '{"version": 1}'
    expected_cfg = {"version": 1}
    test_config(config, expected_cfg)

    # Test config is a string (yaml)
    config = 'version: 1'
    expected_cfg = {"version": 1}
    test_config(config, expected_cfg)

    #

# Generated at 2022-06-14 06:34:25.904779
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    from os import environ
    from logging import Logger, StreamHandler
    from logging.config import dictConfig as dictLoggingConfig

    def assert_has_the_same_config(expected_config, config):
        # it is possible that some values in logging.config.dictConfig()
        # will be automatically updated, such as levelname.
        # These two configs only have the same structure.
        if isinstance(expected_config, list) and isinstance(config, list):
            assert len(expected_config) == len(config)
            for k, v in enumerate(expected_config):
                assert_has_the_same_config(v, config[k])
        elif isinstance(expected_config, dict) and isinstance(config, dict):
            assert set(expected_config.keys())

# Generated at 2022-06-14 06:34:33.864130
# Unit test for function logger_level
def test_logger_level():
    global level
    logger = get_logger("test_logger_level")
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG
    logger = getLogger("test_logger_level")
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:34:44.223963
# Unit test for function get_config
def test_get_config():
    import unittest

# Generated at 2022-06-14 06:34:49.291048
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

    with logger_level(log, logging.DEBUG):
        log.info("info")
        log.debug("debug")

    log.info("info")
    log.debug("debug")



# Generated at 2022-06-14 06:35:02.610908
# Unit test for function get_config

# Generated at 2022-06-14 06:35:16.332732
# Unit test for function get_config