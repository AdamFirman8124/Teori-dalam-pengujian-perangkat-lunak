

# Generated at 2022-06-14 06:25:19.436940
# Unit test for function get_config
def test_get_config():
    """Test get_config function."""
    print("Testing get_config function...")

    # Test bare config

# Generated at 2022-06-14 06:25:29.933219
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    # INFO
    try:
        logger.info('info')
    except Exception:
        raise ValueError('info not allowed')
    # WARNING
    try:
        logger.warning('warning')
    except Exception:
        raise ValueError('warning not allowed')
    # ERROR
    try:
        logger.error('error')
    except Exception:
        raise ValueError('error not allowed')
    # DEBUG
    try:
        logger.debug('debug')
    except Exception:
        raise ValueError('debug not allowed')

    with logger_level(logger, logging.ERROR):
        # INFO
        try:
            logger.info('info')
            raise ValueError('info should not be allowed')
        except Exception:
            pass
        # WARNING

# Generated at 2022-06-14 06:25:36.641135
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    def test():
        logger.error("Error logging")
        logger.debug("Debug logging")
    with logger_level(logger, logging.ERROR):
        test()
    with logger_level(logger, logging.DEBUG):
        test()
    try:
        logger.setLevel("ERROR")
    except:
        with logger_level(logger, logging.ERROR):
            test()
    try:
        logger.setLevel("DEBUG")
    except:
        with logger_level(logger, logging.DEBUG):
            test()

# Generated at 2022-06-14 06:25:48.030396
# Unit test for function configure
def test_configure():

    import json
    import yaml
    import itertools
    import logging

    log = logging.getLogger()
    log.setLevel(logging.CRITICAL)


# Generated at 2022-06-14 06:25:57.950694
# Unit test for function get_config
def test_get_config():
    # test_config = {
    #     'handlers': {
    #         'console': {
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'colored',
    #             'level': logging.DEBUG,
    #         },
    #     },
    #     'root': {
    #         'handlers': ['console'],
    #         'level': logging.DEBUG,
    #     },
    #     'loggers': {
    #         'test': {
    #             'handlers': ['console'],
    #             'level': logging.DEBUG,
    #         },
    #     },
    # }

    config = get_config(None, None, DEFAULT_CONFIG)
    assert config is not None
    assert config['handlers'] is not None

# Generated at 2022-06-14 06:26:05.603788
# Unit test for function logger_level
def test_logger_level():
    def get_fake_logger():
        return logging.getLogger(__name__ + "-" + inspect.stack()[1][3])

    logger = get_fake_logger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Initial debug logging")
    logger.info("Initial info logging")
    with logger_level(logger, logging.INFO):
        logger.debug("Error: debug logging with INFO level")
        logger.info("OK: info logging with INFO level")
    logger.debug("OK: debug logging after context manager")
    logger.info("Initial info logging")


# Generated at 2022-06-14 06:26:15.526861
# Unit test for function logger_level

# Generated at 2022-06-14 06:26:24.524063
# Unit test for function configure
def test_configure():
    """Unit test for function configure"""
    import json

    configure()

    logger = logging.getLogger()
    logger.debug("This should appear")

    # Check logging is not configured
    configure(logging.NOTSET)
    logger.debug("This should not appear")

    # Check logging is configured with a json file
    configure(json.dumps(DEFAULT_CONFIG))
    logger.debug("This should appear")

    # Check logging is configured with a name env var
    configure(env_var=__name__.upper())
    logger.debug("This should appear")

if __name__ == "__main__":
    test_configure()

# Generated at 2022-06-14 06:26:38.433572
# Unit test for function logger_level
def test_logger_level():
    from bg_utils.mock import patch
    import logging.config


# Generated at 2022-06-14 06:26:42.062590
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
    assert log.level == logging.DEBUG

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:56.604259
# Unit test for function logger_level
def test_logger_level():
    import sys
    from io import StringIO
    log = logging.getLogger("test")
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    log.debug("debug")
    # expect debug message printed
    log.info("info")
    # expect info message printed
    log.warning("warning")
    # expect warning message printed
    with logger_level(log, logging.ERROR):
        log.debug("debug")
        # expect nothing printed
        log.info("info")
        # expect nothing printed
        log.warning("warning")
        # expect nothing printed
        log.error("error")
        # expect error message printed
    log.warning("warning")
    # expect warning message printed again
    sys.stdout = StringIO()

# Generated at 2022-06-14 06:27:01.045067
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("Success")
        try:
            log.critical("Shouldn't be able to see this")
            return False
        except:
            return True

# Generated at 2022-06-14 06:27:12.718145
# Unit test for function logger_level
def test_logger_level():
    """ test function logger_level() """

    log = get_logger()

    with logger_level(log, logging.DEBUG):
        log.info("This should be visible")

    log.warning("This should also be visible")

    with logger_level(log, logging.ERROR):
        log.debug("This should be supressed")
        log.info("This should be supressed")
        log.warning("This should be supressed")
        log.error("This should be visible")
        log.critical("This should be visible")

    log.debug("This should be supressed")
    log.info("This should be supressed")
    log.warning("This should be supressed")


# Generated at 2022-06-14 06:27:16.644277
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    log.info('test_logger_level')
    with logger_level(log, logging.DEBUG):
        log.debug('should appear')
    log.debug('should not appear')



# Generated at 2022-06-14 06:27:24.098535
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    log = get_logger(__name__)
    log.debug("Should not appear")
    with logger_level(log, logging.DEBUG):
        log.debug("Should appear")
        with logger_level(log, logging.INFO):
            log.debug("Should not appear")
        log.debug("Should appear")
    log.debug("Should not appear")


# Generated at 2022-06-14 06:27:35.415822
# Unit test for function get_config
def test_get_config():
    logging_config = dict(
        version=1,
        disable_existing_loggers=False,
        handlers={
            'console': {
                'class': 'logging.StreamHandler',
                'level': logging.DEBUG,
            },
        },
        loggers={
            'requests': dict(level=logging.INFO),
        },
    )

    import json
    import yaml

    config = get_config(json.dumps(logging_config))
    assert isinstance(config, dict)
    assert config == logging_config

    config = get_config(yaml.dump(logging_config))
    assert isinstance(config, dict)
    assert config == logging_config

    config = get_config(logging_config)
    assert isinstance(config, dict)
    assert config == logging_config

# Generated at 2022-06-14 06:27:47.094836
# Unit test for function get_config

# Generated at 2022-06-14 06:27:52.745235
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test')
    with logger_level(log, logging.INFO):
        log.info("info message")
        log.error("error message")
    log.error("error message")
    log.info("info message")
    log.debug("debug message")

# Generated at 2022-06-14 06:27:54.766574
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug("This is unit test for function logger_level")
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:28:03.958501
# Unit test for function get_config
def test_get_config():
    """ Doesn't work with ' json.loads("{!r}".format(DEFAULT_CONFIG)) '"""
    import json
    import yaml
    try:
        d = json.loads("{!r}".format(DEFAULT_CONFIG))
    except ValueError as e:
        try:
            d = yaml.load("{!r}".format(DEFAULT_CONFIG))
        except ValueError as e:
            raise ValueError("Could not parse logging config as bare, json, or yaml: {!r}".format(DEFAULT_CONFIG))
    assert get_config(DEFAULT_CONFIG) == d


# Generated at 2022-06-14 06:28:22.287138
# Unit test for function logger_level
def test_logger_level():
    import pytest
    from StringIO import StringIO

    stream = StringIO()
    logger = logging.getLogger("test")
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    assert logger.level == logging.NOTSET

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.error("test")
        assert "test" not in stream.getvalue()
        logger.warn("test")
        assert "test" not in stream.getvalue()
        logger.info("test")
        assert "test" in stream.getvalue()
        logger.debug("test")
        assert "test" in stream.getvalue()

    # restore original
    assert logger.level == logging.NOTSET

# Generated at 2022-06-14 06:28:31.673323
# Unit test for function logger_level
def test_logger_level():
    """Test that a logger level will be changed in a context block."""
    import logging
    import sys

    logger = logging.getLogger('test_logger_level')
    logger.handlers = []
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.CRITICAL)
    with logger_level(logger, logging.DEBUG):
        logger.debug('You should see me.')
    logger.debug('You should not see me.')



# Generated at 2022-06-14 06:28:36.159183
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        logger.debug("test_logger_level failed")
        assert True

# Generated at 2022-06-14 06:28:40.187323
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.debug('This should be ignored')
    with logger_level(logger, logging.DEBUG):
        logger.debug('This should be logged')
    logger.debug('This should be ignored again')
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:28:45.521828
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger('test_logger_level'), logging.DEBUG):
        getLogger('test_logger_level').info('Test logger_level context manager')


# Generated at 2022-06-14 06:28:49.164601
# Unit test for function logger_level
def test_logger_level():
    log=get_logger()
    for lvl in log.level, logging.INFO, logging.DEBUG:
        with logger_level(log, lvl):
            assert log.level == lvl
    assert log.level == logging.INFO

# Generated at 2022-06-14 06:28:56.543852
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')

    with logger_level(logger, logging.DEBUG):
        logger.debug('debug log')
        logger.info('info log')
        logger.warning('warning log')
        logger.error('error log')
        logger.critical('critical log')

    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')

# Generated at 2022-06-14 06:29:03.933226
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test')
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)
    with logger_level(log, logging.CRITICAL):
        log.debug('debug message')
        log.info('info message')
        log.warn('warn message')
        log.error('error message')
        log.critical('critical message')
        assert True

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:29:12.765062
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

    with logger_level(log, logging.NOTSET):
        log.info("NotSet")
        log.debug("debug")

    with logger_level(log, logging.INFO):
        log.info("Info")
        log.debug("debug")

    with logger_level(log, logging.DEBUG):
        log.info("Debug")
        log.debug("debug")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:29:18.514394
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    level = logger.level
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
        logger.info('test')
    assert logger.level == level



# Generated at 2022-06-14 06:29:35.656942
# Unit test for function get_config
def test_get_config():
    # Test with given default config
    cfg_dict = get_config(default=DEFAULT_CONFIG)
    assert cfg_dict == DEFAULT_CONFIG

    # Test with given config as string (json or yaml)
    cfg_str = json.dumps(DEFAULT_CONFIG)
    cfg_dict = get_config(config=cfg_str)
    assert cfg_dict == DEFAULT_CONFIG

    cfg_str = yaml.dump(DEFAULT_CONFIG)
    cfg_dict = get_config(config=cfg_str)
    assert cfg_dict == DEFAULT_CONFIG

    # Test with given config as dict
    cfg_dict = get_config(config=DEFAULT_CONFIG)
    assert cfg_dict == DEFAULT_CONFIG

    # Test with given config as

# Generated at 2022-06-14 06:29:48.261345
# Unit test for function logger_level
def test_logger_level():
    logging_config = {
        "version":1,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {
                "format": "%(levelname)s %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console"],
        },
    }

# Generated at 2022-06-14 06:29:54.652451
# Unit test for function logger_level
def test_logger_level():
    # pylint: disable=missing-docstring,too-few-public-methods,invalid-name
    class Logger(object):
        def __init__(self):
            self.level = None

    def test():
        l = Logger()
        with logger_level(l, level=logging.DEBUG):
            assert l.level == logging.DEBUG
        assert l.level is None

    test()


# Generated at 2022-06-14 06:29:59.552264
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(name=__name__)
    log.setLevel(logging.DEBUG)
    log.debug('test')
    with logger_level(log, logging.INFO):
        log.debug('test')
    log.debug('test')

# Generated at 2022-06-14 06:30:02.576445
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('logger_level')

# Generated at 2022-06-14 06:30:15.856279
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    import tempfile

    log = getLogger()
    with tempfile.TemporaryFile() as log_file:
        log_handler = logging.StreamHandler(log_file)
        log_handler.setFormatter(logging.Formatter('%(message)s'))
        log.addHandler(log_handler)
        log.info('message in logger with level not DEBUG')
        with logger_level(log, logging.DEBUG):
            log.debug('message in logger with level DEBUG')
        log.info('message in logger with level not DEBUG')
        log_file.seek(0)
        log_file_contents = log_file.read()
        log_file.close()
    assert 'DEBUG' not in log_file_contents
    assert 'message in logger with level DEBUG' not in log

# Generated at 2022-06-14 06:30:22.361623
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.info('a message')
        logger.debug('a message')
        with logger_level(logger, logging.ERROR):
            logger.debug('a message')
            logger.error('a message')
        logger.info('a message')
        logger.debug('a message')

# Generated at 2022-06-14 06:30:33.359604
# Unit test for function logger_level
def test_logger_level():
    configure()
    log = logging.getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug("this should not display")
        log.info("this should display")
        log.warning("this should also display")
    log.info("this should again display")
    with logger_level(log, logging.INFO):
        log.debug("this should not display again")
        log.info("this should display again")
        log.warning("this should also display again")
    log.debug("this should again not display")
    log.info("this should again display")
    log.warning("this should also display")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:30:39.291268
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    with logger_level(logger, logging.INFO):
        logger.debug('this should not be logged')
        logger.info('this should be logged')
    logger.debug('this should be logged again')
    logger.info('this should be logged again')



# Generated at 2022-06-14 06:30:51.228504
# Unit test for function logger_level
def test_logger_level():
    import StringIO
    import tempfile
    import os

    # Create a log file
    log_file = tempfile.NamedTemporaryFile(delete=False)
    log_file.close()
    os.unlink(log_file.name)

    # Create a logger
    logger = get_logger()
    logger.setLevel(logging.DEBUG)

    # Add a stream handler and a file handler to the logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file.name)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    logger.addHandler(fh)

    # Check the log contents
    logger.debug('Hello')
    logger.warning('Hello again')

    # Make sure

# Generated at 2022-06-14 06:31:13.440597
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test')
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug level')
        logger.info('info level')
        logger.warn('warn level')


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:16.002083
# Unit test for function logger_level
def test_logger_level():
    """
    Test function logger_level.
    The function logger_level must set logger level to `level` within a context
    block.
    """
    log = logging.getLogger('test_logger_level')
    log.warning("test1")
    with logger_level(log, logging.DEBUG):
        log.debug("test2")
        log.warning("test3")
    log.warning("test4")



# Generated at 2022-06-14 06:31:17.667082
# Unit test for function configure
def test_configure():
    import tempfile
    import json

    with tempfile.NamedTemporaryFile() as fp:
        json.dump(DEFAULT_CONFIG, fp, indent=2)
        fp.flush()
        configure(fp.name)


if __name__ == "__main__":
    test_configure()

# Generated at 2022-06-14 06:31:22.124840
# Unit test for function configure
def test_configure():
    configure()

    log = logging.getLogger(__name__)

    with logger_level(log, logging.CRITICAL):
        log.info('test')
    log.info('test')


if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:31:26.977448
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        logger.debug('test')



# Generated at 2022-06-14 06:31:32.461887
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.CRITICAL):
        log.critical("critical message")
        log.error("error message")
        log.warning("warning message")
        log.info("info message")
        log.debug("debug message")

# Generated at 2022-06-14 06:31:43.329662
# Unit test for function logger_level
def test_logger_level():
    import datetime
    from contextlib import contextmanager
    from io import StringIO
    from logging import getLogger, DEBUG, INFO
    from pytest import raises, warns

    @contextmanager
    def capture():
        """It's the 21st century, this should be in the stdlib.
            See https://gist.github.com/takluyver/789568"""
        oldout, olderr = sys.stdout, sys.stderr
        try:
            out = [StringIO(), StringIO()]
            sys.stdout, sys.stderr = out
            yield out
        finally:
            sys.stdout, sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()


# Generated at 2022-06-14 06:31:57.408859
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.ERROR):
        # Check logger is at level ERROR
        assert logger.level == logging.ERROR

        # Check if output is correct
        import colorlog
        colorlog.default_log_colors['DEBUG'] = 'bold_white'
        colorlog.default_log_colors['INFO'] = 'bold_yellow'
        colorlog.default_log_colors['ERROR'] = 'bold_red'
        colorlog.default_log_colors['CRITICAL'] = 'bold_red'

# Generated at 2022-06-14 06:32:08.384064
# Unit test for function logger_level
def test_logger_level():
    import sys, tempfile
    log = getLogger()
    with logger_level(log, logging.DEBUG):
        log.debug('debug-level message')
        log.info('info-level message')
        log.warn('warn-level message')
        log.error('error-level message')
        log.critical('critical-level message')
    with tempfile.TemporaryFile('w+') as fh:
        handler = logging.StreamHandler(fh)
        handler.setFormatter(logging.Formatter('%(message)s'))
        log.addHandler(handler)
        log.debug('debug-level message')
        log.info('info-level message')
        log.warn('warn-level message')
        log.error('error-level message')
        log.critical('critical-level message')
        f

# Generated at 2022-06-14 06:32:14.944747
# Unit test for function get_config
def test_get_config():
    config = get_config(json.dumps(DEFAULT_CONFIG))
    assert config
    assert type(config) is dict
    config = get_config(yaml.dump(DEFAULT_CONFIG))
    assert config
    assert type(config) is dict
    config = get_config(DEFAULT_CONFIG)
    assert config
    assert type(config) is dict

    expected_exc = ValueError
    try:
        get_config()
    except expected_exc as exc:
        pass
    else:
        raise Exception('Expected get_config() to raise {}'.format(expected_exc))

# Generated at 2022-06-14 06:32:55.528040
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        logger.debug("Should not be logged")
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:33:05.900436
# Unit test for function logger_level
def test_logger_level():
    logger1 = get_logger('test_logger_level')
    # Test3 - print debug level, but not info or warning level
    with logger_level(logger1, logging.DEBUG):
        logger1.debug('test_logger_level - debug')
        logger1.info('test_logger_level - info')
        logger1.warning('test_logger_level - warning')
        logger1.error('test_logger_level - error')
        logger1.critical('test_logger_level - critical')

    # Test6 - print debug, info, and warning level, but not error or critical level
    with logger_level(logger1, logging.INFO):
        logger1.debug('test_logger_level - debug')
        logger1.info('test_logger_level - info')
        logger1

# Generated at 2022-06-14 06:33:13.729928
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.WARNING):
        logger.info("this is an info message")
        logger.debug("this is a debug message")
        logger.warning("this is a warning message")
        logger.error("this is an error message")
        logger.critical("this is a critical message")


# Generated at 2022-06-14 06:33:23.014304
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import os
    import sys
    import logging
    import logging.config
    import StringIO

    class TestLoggerLevel(unittest.TestCase):

        def setUp(self):
            self.out = StringIO.StringIO()
            self.handler = logging.StreamHandler(self.out)
            self.log = logging.getLogger(self.__class__.__name__)
            self.log.addHandler(self.handler)

            # capture original state of logging
            self.existing_logging_level = self.log.level
            self.existing_stream_level = self.handler.level
            self.existing_propagate = self.log.propagate

            # set up default settings for testing
            self.log.setLevel(logging.DEBUG)

# Generated at 2022-06-14 06:33:30.028347
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> log = logging.getLogger(__name__)
    >>> log.setLevel(logging.ERROR)
    >>> with logger_level(log, logging.INFO):
    ...    log.info('hi')
    [2017-05-22 09:41:06] [tests.test_logutil/3421] hi @test_logger_level:123 #INFO
    """
    pass


# Generated at 2022-06-14 06:33:34.237243
# Unit test for function logger_level
def test_logger_level():
    with logger_level(getLogger(), logging.WARNING):
        getLogger("test").debug("test debug")
        getLogger("test").info("test info")
        getLogger("test").warning("test warning")



# Generated at 2022-06-14 06:33:37.795004
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        assert logger.isEnabledFor(logging.INFO)

# Generated at 2022-06-14 06:33:51.083276
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import logging
    import logging.config
    from tests.utils import get_logger as get_test_logger

    logger = get_test_logger(__name__)
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

if __name__ == '__main__':
    import sys
    import doctest

# Generated at 2022-06-14 06:34:05.208575
# Unit test for function configure

# Generated at 2022-06-14 06:34:10.626448
# Unit test for function logger_level
def test_logger_level():

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARN)
    logger.warn('Logger not configured, this should not print')

    with logger_level(logger, logging.DEBUG):
        logger.debug('This should print')
        logger.warn('This should also print')

    logger.debug('This should not print')

