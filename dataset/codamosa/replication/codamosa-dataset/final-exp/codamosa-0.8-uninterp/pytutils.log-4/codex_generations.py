

# Generated at 2022-06-14 06:25:20.045909
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    from StringIO import StringIO

    logger = logging.getLogger(__name__)

    # Default logging level should be warning
    logger.debug('This should not be written')
    old_stdout = sys.stderr
    sys.stderr = StringIO()
    try:
        logger.warning('This should be written')
        logger.error('This should be written')
        assert sys.stderr.getvalue().count('This should be written') == 2
    finally:
        sys.stderr = old_stdout

    # Test that logger level is set to DEBUG within context
    logger.debug('This should not be written')
    old_stdout = sys.stderr
    sys.stderr = StringIO()

# Generated at 2022-06-14 06:25:28.264222
# Unit test for function logger_level
def test_logger_level():
    # Setup logger
    log = logging.getLogger(__name__ + 'test')
    log.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    log.addHandler(stream_handler)

    # Test logger_level
    with logger_level(log, logging.DEBUG):
        log.debug('test')

    try:
        log.debug('test')
    except:
        pass
    else:
        raise AssertionError('expected logger_level to not log')

    return True

# Generated at 2022-06-14 06:25:32.033340
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger=logger, level=logging.DEBUG):
        logger.info("DEBUG MODE")
    logger.info("NORMAL MODE")

# Generated at 2022-06-14 06:25:42.750192
# Unit test for function logger_level
def test_logger_level():
    import sys
    import logging
    import inspect
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format="%(asctime)s %(levelname)s: %(message)s")
    testlogger = logging.getLogger('test')
    testlogger.debug('debug message')
    with logger_level(testlogger, logging.INFO):
        testlogger.debug('debug message')
        testlogger.info('info message')
    testlogger.debug('debug message')
    testlogger.info('info message')



# Generated at 2022-06-14 06:25:50.653431
# Unit test for function logger_level
def test_logger_level():
    from logging import Logger
    from logging import StreamHandler
    from logging import NullHandler
    import os


    class CaptureHandler(StreamHandler):
        def __init__(self, *args, **kwargs):
            super(CaptureHandler, self).__init__(*args, **kwargs)
            self.level = None
            self.msgs = []

        def emit(self, record):
            self.msgs.append(self.format(record))

        def reset(self):
            self.level = None
            self.msgs = []

    logger = Logger('logger.test', level=logging.DEBUG)
    logger.handlers = [NullHandler()]
    handler = CaptureHandler()
    logger.addHandler(handler)

    # Basic sanity test for logger_level

# Generated at 2022-06-14 06:25:55.374126
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')

    with logger_level(logger, logging.WARNING):
        logger.setLevel(logging.WARNING)
        logger.info("This should not be printed")

    with logger_level(logger, logging.INFO):
        logger.setLevel(logging.INFO)
        logger.info("This should be printed")

# Generated at 2022-06-14 06:26:05.859257
# Unit test for function configure
def test_configure():
    import io
    import sys

    # emulate the stdout
    io_out = io.StringIO()
    sys.stdout = io_out

    log = logging.getLogger(__name__)

    configure()
    assert log.level == logging.DEBUG

    log.info('test')

# Generated at 2022-06-14 06:26:08.413824
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.debug('should not appear')
    logger.debug('should appear')

# Generated at 2022-06-14 06:26:16.483079
# Unit test for function get_config
def test_get_config():
    config = get_config(config=DEFAULT_CONFIG)
    assert config == DEFAULT_CONFIG


if __name__ == "__main__":
    import os
    import doctest

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    os.environ['LOGGING'] = str(DEFAULT_CONFIG)
    doctest.testmod()

# Generated at 2022-06-14 06:26:25.399153
# Unit test for function get_config

# Generated at 2022-06-14 06:26:37.759438
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.config
    import pprint

    logging.basicConfig()

    log = logging.getLogger("test")

    with logger_level(log, logging.INFO):
        log.debug("Should not see")
        log.info("This will be seen")

    log.debug("And this will")

# Generated at 2022-06-14 06:26:46.828494
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.ERROR):
        log.info('info outside of context')
        log.error('error outside of context')

    log.info('info outside of context')
    log.error('error outside of context')
    with logger_level(log, logging.INFO):
        log.info('info inside of context')
        log.error('error inside of context')

    log.info('info outside of context')
    log.error('error outside of context')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:53.719680
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        assert logger.getEffectiveLevel() == logging.DEBUG
    logger.info('info message')
    assert logger.getEffectiveLevel() == logging.DEBUG
    with logger_level(logger, logging.ERROR):
        logger.info('warning message')
        assert logger.getEffectiveLevel() == logging.ERROR
    assert logger.getEffectiveLevel() == logging.DEBUG
    logger.info('info message')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:58.194930
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    initial_level = level = logging.INFO
    with logger_level(log, level):
        assert level == log.level
    assert initial_level == log.level

# Generated at 2022-06-14 06:27:11.827039
# Unit test for function configure
def test_configure():
    import tempfile
    import os

    # Create a temporary file
    fd, fn = tempfile.mkstemp()
    # Write the content

# Generated at 2022-06-14 06:27:15.168316
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
        logger.info('Test INFO')
    assert logger.level == logging.INFO



# Generated at 2022-06-14 06:27:20.642972
# Unit test for function configure
def test_configure():
    _CONFIGURED.pop()

    logging.getLogger(__name__).propagate = True
    log = logging.getLogger(__name__)
    log.info('test')
    log.error('test')
    log.warning('test')
    log.debug('test')



# Generated at 2022-06-14 06:27:32.931838
# Unit test for function get_config
def test_get_config():

    print("Test get_config")

    # get_config(config=None, env_var=None, default=None)

    # given
    cfg = get_config(given='{"version": 1, "formatters": {"simple": {"format":"%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s", "datefmt": "%Y-%m-%d %H:%M:%S"}}}', env_var=None, default=None)
    print(cfg)
    assert cfg is not None

    # env_var
    # TODO: Find a way to set environment variables
    # cfg =

# Generated at 2022-06-14 06:27:41.032262
# Unit test for function configure
def test_configure():
    import io
    import logging

    from contextlib import redirect_stderr, redirect_stdout

    # Simulate logging config
    # TODO: Use a mock object instead.
    capture = io.StringIO()
    with redirect_stderr(capture), redirect_stdout(capture):
        configure()
        logging.info('Test logging config')
    assert 'Test logging config' in capture.getvalue()

# Generated at 2022-06-14 06:27:44.039563
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug("Hi")
    logger.info("Bye")

# Generated at 2022-06-14 06:28:02.913263
# Unit test for function get_config
def test_get_config():
    # no config
    assert get_config() is None

    # bare config
    assert get_config(default={'a': 1}) == {'a': 1}

    # non-bare config
    assert get_config(config='{"b": 2}') == {'b': 2}
    assert get_config(config='{"c": 3}') == {'c': 3}
    assert get_config(config='{"d": 4}') == {'d': 4}

    # config via env var
    import os
    os.environ["E"] = '{"e": 5}'
    assert get_config(env_var="E") == {'e': 5}
    os.environ.pop("E")

    # get config via env var but default config is used

# Generated at 2022-06-14 06:28:13.131414
# Unit test for function logger_level
def test_logger_level():
    """ Test logger_level context manager """
    logger = get_logger('test')

    # Turn logging off
    with logger_level(logger, logging.CRITICAL):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')

    # Turn logging back on
    with logger_level(logger, logging.INFO):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')


# Generated at 2022-06-14 06:28:18.567783
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()

    # Set logger level to DEBUG
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG

    # Verify that the logger level is reset back to NOTSET
    assert log.level == logging.NOTSET


# Generated at 2022-06-14 06:28:28.414890
# Unit test for function get_config
def test_get_config():
    # test json
    config = get_config(config='{"version": 1}')
    assert config == {"version": 1}
    # test yaml
    config = get_config(config="""
    version: 1
    """)
    assert config == {"version": 1}
    # test environemt variables
    os.environ['LOGGING'] = json.dumps({"version": 1})
    config = get_config(env_var='LOGGING')
    assert config == {"version": 1}
    # test default
    config = get_config(default={"version": 1})
    assert config == {"version": 1}
    # test given
    config = get_config(config={"version": 1})
    assert config == {"version": 1}



# Generated at 2022-06-14 06:28:35.913934
# Unit test for function get_config
def test_get_config():
    # Test for valid config
    _LOGGING_CONFIG = {
        'disable_existing_loggers': False,
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': '[%(asctime)s] [%(name)s/%(process)d] %(message)s',
                'datefmt': '%H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': logging.DEBUG,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': logging.DEBUG,
        },
    }
    # Test both json string

# Generated at 2022-06-14 06:28:43.166571
# Unit test for function logger_level
def test_logger_level():
    from io import TextIOWrapper
    from io import StringIO
    from contextlib import redirect_stdout

    logger = get_logger()
    logger.setLevel(logging.WARNING)  # set logger level to WARNING
    f = StringIO()
    out = TextIOWrapper(f, sys.stdout.encoding)

    logger.debug('before')
    with redirect_stdout(out):
        with logger_level(logger, logging.DEBUG):
            logger.debug('during')
            logger.warning('during')
            logger.error('during')
    logger.debug('after')

    assert f"before\nduring\nduring\nduring\nafter" == f.getvalue().strip()

# Generated at 2022-06-14 06:28:55.004129
# Unit test for function logger_level
def test_logger_level():
    import json
    import logging
    import datetime

    dt = 'datetime' # for py2.7

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)


# Generated at 2022-06-14 06:28:58.836666
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:29:09.085375
# Unit test for function get_config
def test_get_config():
    # test config value = None
    config = None
    env_var = 'LOGGING'
    default = DEFAULT_CONFIG

    try:
        get_config(config, env_var, default)
    except ValueError:
        pass

    # test config value = None, env_var = None, default = None
    try:
        get_config(config, env_var=None, default=None)
    except ValueError:
        pass

    # test config value = None, env_var = None, default = 'logger.config'
    try:
        get_config(config, env_var=None, default='logger.config')
    except ValueError:
        pass

    # test config value = None, env_var = 'LOGGING', default = None

# Generated at 2022-06-14 06:29:17.749313
# Unit test for function get_config
def test_get_config():
    config = '{"a": "b"}'
    expected = {"a": "b"}
    assert get_config(config) == expected

    config = '{"a": "b"}'
    expected = {"a": "b"}
    assert get_config(config) == expected

    config = '{"a": "b"}'
    expected = {"a": "b"}
    assert get_config(config) == expected

    print('test_get_config passed.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    test_get_config()

# Generated at 2022-06-14 06:29:34.085566
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test_logger_level')
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    with logger_level(log, logging.DEBUG):
        log.debug('test')
    assert(log.level == logging.INFO)

# Generated at 2022-06-14 06:29:36.426763
# Unit test for function configure
def test_configure():
    logging.setLoggerClass(DummyLoggerClass)
    import json
    configure(config=json.dumps(DEFAULT_CONFIG))



# Generated at 2022-06-14 06:29:44.870155
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        log.debug("This is a debug message which should be printed")
        log.info("This is an info message which should be printed")
        log.warning("This is a warning message which should be printed")
        log.error("This is an error message which should be printed")
        log.critical("This is a critical message which should be printed")
    log.debug("This is a debug message which should NOT be printed")

# Generated at 2022-06-14 06:29:54.804628
# Unit test for function logger_level
def test_logger_level():
    level_test = logging.getLogger("test.test_logger_level")
    with logger_level(level_test, logging.CRITICAL):
        level_test.debug("Should not print")
        level_test.info("Should not print")
        level_test.warning("Should not print")
        level_test.error("Should not print")
        level_test.critical("Should print")

    level_test.debug("Should print")
    level_test.info("Should print")
    level_test.warning("Should print")
    level_test.error("Should print")
    level_test.critical("Should print")

# Generated at 2022-06-14 06:30:00.563136
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.ERROR):
        log.debug("Error message ignored.")
        log.info("Info message ignored.")
        log.error("ERROR message displayed")
    log.debug("Debug message displayed.")
    log.info("Info message displayed.")



# Generated at 2022-06-14 06:30:07.373067
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.CRITICAL):
        assert log.level == logging.CRITICAL
        log.info('This shouldnt print')
        log.critical('This should print')
    assert log.level == DEFAULT_CONFIG['root']['level']
    log.info('This should print again')



# Generated at 2022-06-14 06:30:19.121901
# Unit test for function get_config
def test_get_config():
    config = {"version": 1, "disable_existing_loggers": False, "formatters": {"simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "datefmt": "%Y-%m-%d %H:%M:%S"}}, "handlers": {"console": {"class": "logging.StreamHandler", "level": "DEBUG", "formatter": "simple", "stream": "ext://sys.stdout"}}, "loggers": {"my_module": {"level": "ERROR", "handlers": ["console"], "propagate": "no"}}}
    conf = get_config(config)
    assert conf == config


# Generated at 2022-06-14 06:30:24.460883
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.info("Should not be logged")
    logger.info("Should be logged")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:36.500167
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test')
    try:
        with logger_level(logger, logging.DEBUG):
            logger.debug("hello from logger_level")
            logger.info("hello from logger_level")
            logger.error("hello from logger_level")
    except Exception as exc:
        raise exc
    # logger should return to original level
    try:
        logger.debug("hello from logger_level")
        logger.info("hello from logger_level")
        logger.error("hello from logger_level")
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    import doctest

    doctest.testmod()


# Generated at 2022-06-14 06:30:42.248365
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    assert logger.level == logging.DEBUG, "Default log level differs from expect value"
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR, "Log level change fails"
    assert logger.level == logging.DEBUG, "log level restore fails"

# Generated at 2022-06-14 06:30:58.628074
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level == logging.INFO

# Generated at 2022-06-14 06:31:02.083071
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        logger.debug('not shown')
        logger.info('shown')
    logger.debug('shown')



# Generated at 2022-06-14 06:31:08.042469
# Unit test for function logger_level
def test_logger_level():
    from StringIO import StringIO
    from pytest import raises

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    buf = StringIO()
    h = logging.StreamHandler(buf)
    log.addHandler(h)

    with raises(Exception):
        with logger_level(log, logging.ERROR):
            log.debug("SHOULD NOT SEE THIS!")
            raise Exception("SHOULD SEE THIS!")

    log.debug("SHOULD SEE THIS!")

    assert not buf.getvalue().find("SHOULD NOT SEE THIS") >= 0
    assert buf.getvalue().find("SHOULD SEE THIS") >= 0



# Generated at 2022-06-14 06:31:19.264824
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    assert log.isEnabledFor(logging.INFO)
    with logger_level(log, logging.DEBUG):
        assert log.isEnabledFor(logging.DEBUG)
        assert log.isEnabledFor(logging.INFO)
        assert not log.isEnabledFor(logging.WARNING)
    assert log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.DEBUG)

"""
Some mocking helpers to aid in testing code that uses logging.
"""
# I don't like this much, but I can't think of a better way to do it.
# It's also nice that it is only used in tests.

# Generated at 2022-06-14 06:31:26.817067
# Unit test for function logger_level
def test_logger_level():
    print("testing logger_level")
    log = get_logger(__name__ + '.test_logger_level')
    with logger_level(log, logging.ERROR):
        assert log.isEnabledFor(logging.ERROR)
        assert not log.isEnabledFor(logging.INFO)

    assert not log.isEnabledFor(logging.ERROR)
    assert log.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:34.154254
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        print('logger level below')
        logger.debug('not printed')
    print('logger level above')
    logger.debug('printed')


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:31:40.943404
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger_level(logger, logging.ERROR) is None
    logger.warn("warning msg")
    with logger_level(logger, logging.INFO):
        logger.warn("warning msg")
    with logger_level(logger, logging.DEBUG):
        logger.info("info msg")

# Generated at 2022-06-14 06:31:45.463990
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        log.debug("Inside with block")
    log.info("Outside with block")
    eq_(log.level, logging.INFO)

# Generated at 2022-06-14 06:31:58.240007
# Unit test for function logger_level
def test_logger_level():
    """Test function logger_level."""
    import time

    class FakeLogger(object):

        def __init__(self):
            self.level = 10
            self.log = []
        def add(self, level, msg, *args):
            self.log.append(level)
        def debug(self, msg, *args):
            self.add(10, msg, *args)
        def info(self, msg, *args):
            self.add(20, msg, *args)
        def warn(self, msg, *args):
            self.add(30, msg, *args)
        def warning(self, msg, *args):
            self.warn(msg, *args)
        def error(self, msg, *args):
            self.add(40, msg, *args)

# Generated at 2022-06-14 06:32:08.459091
# Unit test for function get_config
def test_get_config():
    import json
    import yaml


# Generated at 2022-06-14 06:32:23.140444
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    level = logger.level

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == level



# Generated at 2022-06-14 06:32:35.655502
# Unit test for function get_config

# Generated at 2022-06-14 06:32:42.063113
# Unit test for function logger_level
def test_logger_level():
    import sys
    import StringIO

    class TestLogLevel(unittest.TestCase):
        def test_logger_level(self):
            stdout = sys.stdout
            out = StringIO.StringIO()
            sys.stdout = out

            logger = logging.getLogger(__name__)
            logger.info("Test 1")
            with logger_level(logger, logging.ERROR):
                logger.info("Test 2")
                logger.error("Test 3")
                self.assertTrue("Test 1" in out.getvalue())
                self.assertTrue("Test 2" not in out.getvalue())
                self.assertTrue("Test 3" in out.getvalue())
                with logger_level(logger, logging.DEBUG):
                    logger.debug("Test 4")

# Generated at 2022-06-14 06:32:48.982649
# Unit test for function configure
def test_configure():
    # configure success
    DEFAULT_CONFIG['loggers']['requests'] = dict(level=logging.INFO)
    configure()
    logging.getLogger('requests').info('test')

    # configure failure because of wrong env_var
    os.environ['LOGGING'] = 'ABC'
    try:
        configure()
        assert False, 'Should not reach here'
    except ValueError:
        pass

    # configure failure because of wrong default config
    DEFAULT_CONFIG['loggers']['requests'] = dict(level=logging.INFO)
    try:
        configure()
        assert False, 'Should not reach here'
    except ValueError:
        pass


# Generated at 2022-06-14 06:33:02.669765
# Unit test for function get_config
def test_get_config():
    logging_config_str_json = '{"handlers": {"null": {"class": "logging.NullHandler"}}}'
    logging_config_str_yaml = 'handlers: {null: {class: logging.NullHandler}}'
    logging_config_dict = {'handlers': {'null': {'class': 'logging.NullHandler'}}}
    logging_config_str = '{"handlers": "null"}'

    assert get_config(logging_config_str_json) == get_config(logging_config_dict)
    assert get_config(logging_config_str_yaml) == get_config(logging_config_dict)
    assert get_config(logging_config_str) == {'handlers': 'null'}
    assert get_config(env_var='my_logging')

# Generated at 2022-06-14 06:33:14.220973
# Unit test for function logger_level
def test_logger_level():
    import logging
    import time

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test_logger_level")

    with logger_level(log, logging.INFO):
        log.debug("This is a debug message")
        log.info("This is an info message")
        log.warn("This is a warning message")

    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warn("This is a warning message")

    with logger_level(log, logging.DEBUG):
        log.debug("This is a debug message")
        log.info("This is an info message")
        log.warn("This is a warning message")

    log.debug("This is a debug message")
    log.info("This is an info message")
    log

# Generated at 2022-06-14 06:33:19.253488
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

test_logger_level()

# Generated at 2022-06-14 06:33:25.781927
# Unit test for function logger_level
def test_logger_level():
    log1 = get_logger("hello")
    log2 = get_logger("world")
    log1.info("global")
    log2.info("global")
    with logger_level(log1, logging.CRITICAL):
        log1.info("hello")
        log2.info("world")
    log1.info("global")
    log2.info("global")

# Generated at 2022-06-14 06:33:35.807322
# Unit test for function logger_level
def test_logger_level():
    # Allow output of test to be logged.
    configure()
    log = get_logger(__name__)

    with logger_level(log, logging.DEBUG):
        log.debug('logging at level DEBUG')
        log.info('logging at level INFO')
        log.warning('logging at level WARNING')
        log.error('logging at level ERROR')
        log.critical('logging at level CRITICAL')

    log.debug('logging at level DEBUG')
    log.info('logging at level INFO')
    log.warning('logging at level WARNING')
    log.error('logging at level ERROR')
    log.critical('logging at level CRITICAL')

# Generated at 2022-06-14 06:33:43.097528
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(), logging.ERROR):
        get_logger().info('Info <== ERROR')
        with logger_level(get_logger(), logging.DEBUG):
            get_logger().debug('Debug <== DEBUG')
            get_logger().info('Info <== DEBUG')
        get_logger().info('Info <== ERROR')

# Generated at 2022-06-14 06:34:09.634009
# Unit test for function get_config
def test_get_config():
    # Test with bare
    cfg = get_config(
        config='[handlers][console][class] = logging.StreamHandler',
        env_var='LOGGING',
        default=None,
    )
    assert(isinstance(cfg, dict))
    # Test with json
    import json

# Generated at 2022-06-14 06:34:14.585351
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.error("Test on logger_level")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:18.661141
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger()
    assert log.level > logging.DEBUG
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level > logging.DEBUG

# Generated at 2022-06-14 06:34:22.129719
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:34:30.017376
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    # TODO: Test if this works in py2.6, 2.6 has no assertIn
    with logger_level(logger, logging.DEBUG):
        logger.debug("test_debug")
        assert "test_debug" in str(logger)
    with logger_level(logger, logging.INFO):
        logger.debug("test_debug")
        assert "test_debug" not in str(logger)



# Generated at 2022-06-14 06:34:40.965296
# Unit test for function logger_level
def test_logger_level():
    from contextlib import contextmanager
    import unittest

    class TestLoggerLevel(unittest.TestCase):
        def test_it(self):
            @contextmanager
            def logger_level(logger, level):
                initial = logger.level
                logger.level = level
                try:
                    yield
                    self.assertEqual(logger.level, level)
                finally:
                    logger.level = initial

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            with logger_level(logger, logging.DEBUG):
                logger.debug("Hello")
            self.assertEqual(logger.level, logging.INFO)

# Generated at 2022-06-14 06:34:46.873610
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug('logging.DEBUG')
        log.info('logging.INFO')
        log.warn('logging.WARN')
        log.error('logging.ERROR')
    with logger_level(log, logging.INFO):
        log.debug('logging.DEBUG')
        log.info('logging.INFO')
        log.warn('logging.WARN')
        log.error('logging.ERROR')
    with logger_level(log, logging.WARN):
        log.debug('logging.DEBUG')
        log.info('logging.INFO')
        log.warn('logging.WARN')
        log.error('logging.ERROR')
    with logger_level(log, logging.ERROR):
        log

# Generated at 2022-06-14 06:34:51.807018
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger(__name__), logging.DEBUG):
        getLogger(__name__).debug("This is a test.")
    getLogger(__name__).debug("This is not a test.")



# Generated at 2022-06-14 06:34:57.988294
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')

    # Expect setting logger to ERROR to block anything below that
    with logger_level(log, logging.ERROR):
        log.info('This should not be logged')
        log.error('This should be logged')

    # Expect setting level back to INFO to unblock info messages
    log.info('This should be logged')



# Generated at 2022-06-14 06:35:07.601451
# Unit test for function get_config
def test_get_config():
    assert get_config() == DEFAULT_CONFIG

    # foo_config_file is not exists
    with pytest.raises(ValueError):
        get_config(config='foo_config_file')

    with open('foo_config_file', 'w') as config_file:
        config_file.write('foo')

    os.environ['LOGGING'] = 'foo_config_file'
    assert get_config() == 'foo'
    os.remove('foo_config_file')
