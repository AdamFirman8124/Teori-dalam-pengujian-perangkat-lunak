

# Generated at 2022-06-14 06:25:19.741153
# Unit test for function logger_level
def test_logger_level():
    # Set up logger
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)

    # Add handler
    fh = logging.FileHandler("level.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Test context manager
    with logger_level(logger, logging.INFO):
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.exception("exception")
        logger.critical("critical")
    logger.debug("debug")
    logger.info("info")

# Generated at 2022-06-14 06:25:30.080217
# Unit test for function logger_level
def test_logger_level():
    """
    >>> from io import StringIO
    >>> from contextlib import contextmanager
    >>> @contextmanager
    ... def capture_stream(stream):
    ...     out, stream.stream = stream.stream, StringIO()
    ...     try:
    ...         yield stream.stream
    ...     finally:
    ...         stream.stream = out
    >>> l = getLogger()
    >>> with capture_stream(l) as s:
    ...     with logger_level(l, logging.INFO):
    ...         l.debug("this should not print")
    ...     with logger_level(l, logging.DEBUG):
    ...         l.debug("this should print")
    >>> "this should print" in s.getvalue()
    True
    >>> "this should not print" in s.getvalue()
    False
    """
    pass

# Generated at 2022-06-14 06:25:34.813344
# Unit test for function configure
def test_configure():

    configure()
    log = logging.getLogger('test_configure')
    with logger_level(log, logging.DEBUG):
        log.info("test_configure")


# Generated at 2022-06-14 06:25:47.098096
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure(default=dict(
        version=1,
        disable_existing_loggers=False,
        handlers={
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': logging.DEBUG,
            },
        },
        root=dict(handlers=['console'], level=logging.DEBUG),
        loggers={
            'requests': dict(level=logging.INFO),
        },
    ))
    logger.info('test')
    logger.debug('test-debug')

    with logger_level(logger, level=logging.DEBUG):
        logger.debug('test-debug')
        logger.info('test')

    logger.debug('test-debug')

# Generated at 2022-06-14 06:25:51.762433
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()
    assert logger_level is not None
    assert log is not None
    with logger_level(log, logging.WARN):
        log.debug("this message should not appear")
        log.warn("a warning message")


# Generated at 2022-06-14 06:25:58.495556
# Unit test for function logger_level
def test_logger_level():
    loggerlogger = get_logger('test_logger_level')
    with logger_level(loggerlogger, logging.INFO):
        loggerlogger.debug('This should not be seen. %s', 'or this')
        loggerlogger.info('This should be seen. %s', 'and this')



# Generated at 2022-06-14 06:26:04.450828
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logging')
    with logger_level(log, logging.INFO):
        for level in (log.debug('test message 1, should be hidden'),
                      log.info('test message 2, should be visible')):
            assert not level
    for level in (log.debug('test message 3, should be visible'),
                  log.info('test message 4, should be visible')):
        assert level


# Generated at 2022-06-14 06:26:08.624831
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    
    # This will fail without the context manager
    with logger_level(log, logging.CRITICAL):
        log.debug("Debug message should not print")

# Generated at 2022-06-14 06:26:14.285762
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    assert l.level == logging.DEBUG
    with logger_level(l, logging.WARNING) as ctx:
        assert l.level == logging.WARNING
        l.debug("testing")
    assert l.level == logging.DEBUG

# Generated at 2022-06-14 06:26:19.683857
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
        logger.debug('debug test')
    assert logger.call_count == 1
    assert logger.level == logging.INFO

# Generated at 2022-06-14 06:26:36.466456
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('foo')

    # Test logger_level function.
    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.info('info')
        log.warning('warning')
        log.error('error')
        log.critical('critical')
    with logger_level(log, logging.ERROR):
        log.debug('debug')
        log.info('info')
        log.warning('warning')
        log.error('error')
        log.critical('critical')

    log.setLevel(logging.INFO)

    log.debug('debug...')
    log.info('info..')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:39.048215
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, 100):
        assert logger.level == 100
    assert logger.level != 100

# Generated at 2022-06-14 06:26:43.190257
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARNING):
        logger.debug("should be a no-op")
    logger.debug("debugging again")

# Generated at 2022-06-14 06:26:53.517989
# Unit test for function get_config
def test_get_config():
    config = get_config(env_var=None, default=DEFAULT_CONFIG)
    assert(get_config() == get_config(env_var=None, default=DEFAULT_CONFIG))
    logging_dict = json.loads(os.environ['LOGGING'])
    assert(get_config(env_var='LOGGING') == get_config(env_var=None, default=logging_dict))
    assert(get_config(config={'test':'test'}) == {'test':'test'})


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:27:04.985195
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    from logging.config import DictConfigurator

    json_config = '{"loggers": {"my.module": {"level": "DEBUG"}}}'
    yaml_config = yaml.dump(json.loads(json_config))

    config = get_config(config=json_config)
    assert json.dumps(config) == json_config
    c = DictConfigurator()
    c.configure(config)
    assert c.loggers['my.module']['level'] == 'DEBUG'

    config = get_config(config=yaml_config)
    assert json.dumps(config) == json_config
    c = DictConfigurator()
    c.configure(config)
    assert c.loggers['my.module']['level'] == 'DEBUG'

# Generated at 2022-06-14 06:27:10.558211
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger("test_logger_level")
    with logger_level(log, logging.DEBUG):
        assert log.getEffectiveLevel() == logging.DEBUG
    assert log.getEffectiveLevel() == logging.NOTSET


# Generated at 2022-06-14 06:27:18.094623
# Unit test for function logger_level
def test_logger_level():
    configure()
    logger = getLogger()
    try:
        with logger_level(logger, logging.CRITICAL):
            assert logger.level==logging.CRITICAL
            logger.debug("This doesn't make it to console")
            logger.error("This does make it to console")
        assert logger.level==logging.DEBUG
        logger.debug("This DOES make it to console")
    except Exception as e:
        print("There was an exception in the test:", e)
    finally:
        pass

# Generated at 2022-06-14 06:27:25.457800
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__ + '.test_logger_level')
    logger.level = logging.INFO

    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
        assert not logger.isEnabledFor(logging.INFO)

    assert not logger.isEnabledFor(logging.DEBUG)
    assert logger.isEnabledFor(logging.INFO)



# Generated at 2022-06-14 06:27:32.914962
# Unit test for function logger_level
def test_logger_level():
    import io
    import logging
    import unittest
    logger = logging.getLogger("test_logger_level")
    buf = io.StringIO()
    hdlr = logging.StreamHandler(buf)
    logger.addHandler(hdlr)
    logger.setLevel(logging.CRITICAL)
    with logger_level(logger,logging.DEBUG):
        assert(logger.level == logging.DEBUG)
    assert(logger.level == logging.CRITICAL)



# Generated at 2022-06-14 06:27:43.422047
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    assert log.level == logging.DEBUG
    with logger_level(log, logging.WARNING):
        assert log.level == logging.WARNING
    assert log.level == logging.DEBUG

# DEPROGATED. Code that switches on level is a code smell.
# def test_level_switch_warnings():
#     log = getLogger(__name__)
#     with logger_level(log, logging.WARNING):
#         if log.level() < logging.ERROR:
#             log.warn("Should be able to see this")

# Generated at 2022-06-14 06:27:54.153061
# Unit test for function logger_level
def test_logger_level():
    l = getLogger('test_logger_level')

    # default
    assert l.isEnabledFor(logging.INFO)

    with logger_level(l, logging.DEBUG):
        assert l.isEnabledFor(logging.DEBUG)

    assert l.isEnabledFor(logging.INFO)

# Generated at 2022-06-14 06:27:59.799592
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    import socket
    with logger_level(logger, logging.ERROR):
        with logger_level(logger, logging.DEBUG):
            assert logger.level == logging.DEBUG
            logger.debug("This is a debug message")
        assert logger.level == logging.DEBUG
    assert logger.level == logging.ERROR

# Generated at 2022-06-14 06:28:03.739596
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.NOTSET


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:28:08.959052
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    new_level = logging.INFO
    with logger_level(logger, new_level) as ctx:
        assert logger.level == new_level
    assert logger.level != new_level

# Generated at 2022-06-14 06:28:14.181821
# Unit test for function configure
def test_configure():
    logger = configure()
    logger = logging.getLogger('test')
    logger.debug('Test debug')
    logger.info('Test info')
    logger.warning('Test warning')
    logger.error('Test error')
    logger.critical('Test critical')


# Generated at 2022-06-14 06:28:19.594649
# Unit test for function logger_level
def test_logger_level():
    global log
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.DEBUG('debugging')
        log.INFO('info')
        log.WARNING('warning')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:24.407421
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        logger.debug("test level DEBUG")
    logger.info("test level INFO")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:36.508092
# Unit test for function logger_level
def test_logger_level():
    """Verifies logger_level function sets logger level within a context block. The log level is restored to the
    original value when the context block is exited

    """
    # Need to call configure before getLogger is called
    configure()
    logger = getLogger(__name__)
    try:
        with logger_level(logger, logging.INFO):
            assert logger.getEffectiveLevel() == logging.INFO
        assert logger.getEffectiveLevel() == logging.DEBUG
    except Exception as e:
        assert False, e

if __name__ == '__main__':
    configure()
    test_logger_level()
    # pytest is not importing properly
    # import sys
    # if sys.version_info.major == 2:
    #     import unittest
    #     unittest.main(module='tests')
   

# Generated at 2022-06-14 06:28:44.402936
# Unit test for function logger_level
def test_logger_level():
    import logging
    from . import logger

    logger_name = "logger_name"
    logger.configure()
    log = logger.get_logger(logger_name)

    # with context, level set to logging.INFO
    with logger_level(log, logging.INFO):
        log.debug("logger test: pass")
        log.debug("logger test: fail")
        log.info("logger test: pass")
        log.info("logger test: fail")
        log.warning("logger test: pass")
        log.warning("logger test: fail")
    # without context, level set to logging.DEBUG
    log.debug("logger test: pass")
    log.debug("logger test: fail")
    log.info("logger test: pass")

# Generated at 2022-06-14 06:28:51.034138
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.WARNING):
        logger.info('A message in the code')
        assert not logger.handlers[0].stream.getvalue()
        logger.warning('A warning in the code')
        assert 'A warning in the code\n' in logger.handlers[0].stream.getvalue()



# Generated at 2022-06-14 06:29:01.112174
# Unit test for function logger_level
def test_logger_level():
    import time

    log = logging.getLogger(__name__)
    with logger_level(log, logging.WARNING):
        log.info('in with block')
        time.sleep(1)
        log.info('in with block')
    log.info('after with block')


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:29:04.478779
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    log.info('info from %s', __name__)
    with logger_level(log, logging.WARN):
        log.info('this message should be filtered out')
    log.info('info from %s', __name__)



# Generated at 2022-06-14 06:29:11.601126
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)

    # Should not log
    with logger_level(logger, logging.CRITICAL):
        logger.info('testing')

    # Should log
    with logger_level(logger, logging.INFO):
        logger.info('testin')


format_time = logging.Formatter.formatTime



# Generated at 2022-06-14 06:29:12.816891
# Unit test for function configure
def test_configure():
    configure()


# Generated at 2022-06-14 06:29:26.282966
# Unit test for function get_config

# Generated at 2022-06-14 06:29:36.426520
# Unit test for function logger_level
def test_logger_level():
    import sys
    import io

    log = get_logger('test_logger_level')

    with io.StringIO() as output:
        sys.stderr = output

        with logger_level(log, logging.NOTSET):
            log.debug("Out of range")

        log.warn("message")
        assert "message" in output.getvalue()

    # The logger level is reset to its initial state
    with io.StringIO() as output:
        sys.stderr = output
        log.debug("Still out of range")
        assert len(output.getvalue()) == 0

    assert log.level == logging.INFO


# Tests for get_logger()

# Generated at 2022-06-14 06:29:44.001056
# Unit test for function logger_level
def test_logger_level():
    # This test is not very good at testing, but it did help me figure
    # out how to use the context manager.
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    with logger_level(logger, logging.DEBUG):
        logger.debug("This message should appear")

    logger.debug("This message should not appear")

# Generated at 2022-06-14 06:29:57.068258
# Unit test for function logger_level
def test_logger_level():
    import logging
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    with logger_level(log, logging.CRITICAL):
        log.info('this should not show up')
        log.critical('this should show up')
    log.info('this should show up')
    log.critical('this should show up')

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    with logger_level(log, logging.CRITICAL):
        log.info('this should not show up')
        with logger_level(log, logging.INFO):
            log.info('this should show up')
        log.critical('this should show up')
    log.info('this should show up')
    log.critical('this should show up')

# Generated at 2022-06-14 06:30:03.209034
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger("test_logger_level")
    logger.setLevel(logging.INFO)

    with logger_level(logger, logging.DEBUG):
        logger.debug("This should show up")
        logger.info("This shouldn't")
    logger.info("This should show up")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:06.448532
# Unit test for function logger_level
def test_logger_level():
    """
    >>> with logger_level(logging.Logger, logging.WARNING):
    ...     1 + 1
    """


# Generated at 2022-06-14 06:30:18.181021
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    with logger_level(logger, logging.DEBUG):
        logger.debug("Debug level logging to be visible")
        logger.info("Info level logging to be visible")

    with logger_level(logger, logging.INFO):
        logger.debug("Debug level logging to be hidden")
        logger.info("Info level logging to be visible")


# Generated at 2022-06-14 06:30:30.930309
# Unit test for function logger_level
def test_logger_level():
    import sys
    logger = logging.getLogger()
    assert logger.level == logging.WARNING
    # On Python 2.7, logger.level is an integer, on Python 3 it's a string.
    if sys.version_info[0] == 3:
        assert (logger.getEffectiveLevel() == 'WARNING')
    else:
        assert (logger.getEffectiveLevel() == 30)

    with logger_level(logger, logging.DEBUG):
        assert (logger.getEffectiveLevel() == 10)
    assert (logger.getEffectiveLevel() == 30)

    assert (get_logger() == logger)
    assert (get_logger('test') == get_logger('test'))
    assert (get_logger('test').level == 30)

# Generated at 2022-06-14 06:30:33.162836
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('test')



# Generated at 2022-06-14 06:30:37.628620
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    logger.debug('Not_displayed_when_level_is_WARNING')

    with logger_level(logger, logging.WARNING):
        logger.debug('Not_displayed_when_level_is_WARNING')



# Generated at 2022-06-14 06:30:41.774563
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()

    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:30:53.662676
# Unit test for function get_config
def test_get_config():
    config = get_config(config="""
        version: 1
        disable_existing_loggers: False

        formatters:
            simple:
                format: '%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s'
                datefmt: '%Y-%m-%d %H:%M:%S'

        handlers:
            console:
                class: logging.StreamHandler
                formatter: simple
                level: DEBUG

        loggers:
            root:
                level: DEBUG
                handlers: [console]
    """, env_var=None, default=None)
    assert config

# Generated at 2022-06-14 06:30:56.441923
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.info("logger_level test")

# Generated at 2022-06-14 06:31:00.891536
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.Logger("test")
    level = logging.DEBUG
    with logger_level(logger, level):
        assert logger.getEffectiveLevel() == level

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:31:05.734801
# Unit test for function get_config
def test_get_config():
    config = get_config(default=DEFAULT_CONFIG)
    assert DEFAULT_CONFIG == config

    config = get_config(config='{"version": 1}', default=DEFAULT_CONFIG)
    assert config == {'version': 1}

    config = get_config(config='version: 1', default=DEFAULT_CONFIG)
    assert config == {'version': 1}



# Generated at 2022-06-14 06:31:11.319150
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:31:24.617203
# Unit test for function logger_level
def test_logger_level():
    import unittest
    import io
    import contextlib
    logger = getLogger('mock')
    logger.level = 0
    logger.addHandler(logging.StreamHandler())

    class TestLoggerLevel(unittest.TestCase):
        def test_logger_level_inside_context_block(self):
            with contextlib.redirect_stdout(io.StringIO()):
                with logger_level(logger, logging.INFO):
                    logger.debug('debug message')
                    logger.info('info message')
            self.assertEqual(logger.level, 0, 'The logger level should be override')

    try:
        unittest.main()
    except SystemExit as inst:
        return inst.code



# Generated at 2022-06-14 06:31:32.789330
# Unit test for function get_config
def test_get_config():
    try:
        get_config(None, None, None)
        assert False, "config: None should raise Exception"
    except ValueError:
        pass

    try:
        get_config(None, 'LOGGING', None)
        assert False, "config: None should raise Exception"
    except ValueError:
        pass

    try:
        get_config(None, None, 'random')
        assert False, "config: random should raise Exception"
    except ValueError:
        pass



# Generated at 2022-06-14 06:31:43.463616
# Unit test for function logger_level
def test_logger_level():
    # setup logger
    logger = logging.getLogger('test_logger_level')
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    # custom level
    logger.setLevel(5)

    with logger_level(logger, 10):
        try:
            logger.log(5, '1')
        except Exception as e:
            raise e

    with logger_level(logger, 5):
        try:
            logger.log(5, '2')
        except Exception as e:
            raise e

    try:
        logger.log(5, '3')
    except Exception as e:
        raise e

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:31:51.023078
# Unit test for function logger_level
def test_logger_level():
    import logging
    assert logging.getLogger('test_logger_level').level == logging.NOTSET
    with logger_level(logging.getLogger('test_logger_level'), logging.DEBUG):
        assert logging.getLogger('test_logger_level').level == logging.DEBUG
    assert logging.getLogger('test_logger_level').level == logging.NOTSET

# Generated at 2022-06-14 06:31:58.239626
# Unit test for function logger_level
def test_logger_level():
    import logging
    logging.getLogger(__name__).setLevel(logging.WARN)
    log1 = logging.getLogger(__name__)

    log1.debug('should not be displayed')

    with logger_level(logger=log1, level=logging.DEBUG):
        log1.debug('should be displayed')

    log1.debug('should not be displayed')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:32:08.458834
# Unit test for function logger_level
def test_logger_level():
    # Given
    logger = getLogger(__name__)

    # When
    with logger_level(logger, logging.INFO):
        # Then
        logger.error('This is an error which should be hidden')
        logger.info('This is an info which should be shown')

    # When
    with logger_level(logger, logging.CRITICAL):
        # Then
        logger.error('This is an error which still be shown')
        logger.info('This is an info which should be hidden')

    with logger_level(logger, logging.DEBUG):
        # Then
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.error('This is an error message')


if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:32:12.964315
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    logger.setLevel(logging.WARN)
    # normal log
    logger.info('Info level log')
    # check if the log is displayed or not
    assert not logger.handlers[0].stream.getvalue()
    with logger_level(logger, logging.INFO):
        logger.info('Info level log')
        logger.warn('Warning level log')
    # This log should be displayed because the previous context
    # set the level of the logger to logging.INFO
    assert logger.handlers[0].stream.getvalue().strip()

# Generated at 2022-06-14 06:32:21.234790
# Unit test for function logger_level
def test_logger_level():
    import sys
    _log = getLogger()
    with logger_level(_log, logging.CRITICAL):
        _log.debug("debug msg")
        _log.info("info msg")
        _log.warning("warning msg")
    _log.error("error msg")
    _log.critical("critical msg")
    assert sys.stdout.getvalue() == "error msg\ncritical msg\n"

# End unit test


# Generated at 2022-06-14 06:32:24.052788
# Unit test for function get_config
def test_get_config():
    import json
    config = json.dumps(DEFAULT_CONFIG)
    assert config == get_config(config)

# Generated at 2022-06-14 06:32:36.540899
# Unit test for function configure
def test_configure():
    configure()

    # Setup
    logging.basicConfig()
    log = logging.getLogger(__name__)
    test_logger_handlers = log.handlers
    test_logger_level = log.level
    test_root_logger_handlers = logging.getLogger().handlers
    test_root_logger_level = logging.getLogger().level
    test_root_logger_propagate = logging.getLogger().propagate

    configure()
    assert log.handlers == test_logger_handlers
    assert log.level == test_logger_level
    assert logging.getLogger().handlers == test_root_logger_handlers
    assert logging.getLogger().level == test_root_logger_level
    assert logging.getLogger().propagate == test_root

# Generated at 2022-06-14 06:32:51.189934
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    with tempfile.NamedTemporaryFile(mode = 'w') as f:
        logger = logging.getLogger()
        h = logging.StreamHandler(f)
        h.setLevel(logging.INFO)
        logger.addHandler(h)
        logger.setLevel(logging.DEBUG)
        logger.info('hi')
        assert 'hi' in f.read()
        with logger_level(logger, logging.ERROR):
            logger.info('hi')
            assert 'hi' not in f.read()
            logger.error('hi')
            assert 'hi' in f.read()
            logger.exception('hi')
            assert 'hi' in f.read()
        logger.info('hi')
        assert 'hi' in f.read()

# Generated at 2022-06-14 06:32:57.074793
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    log.debug("Testing debug level before")
    with logger_level(log, logging.DEBUG):
        log.debug("Testing debug level within context, should be enabled")
    log.debug("Testing debug level after, should be disabled")

# Generated at 2022-06-14 06:33:08.687624
# Unit test for function logger_level
def test_logger_level():
    rootlogger = logging.getLogger()
    with logger_level(rootlogger, logging.DEBUG):
        assert rootlogger.isEnabledFor(logging.DEBUG)
    with logger_level(rootlogger, logging.ERROR):
        assert not rootlogger.isEnabledFor(logging.DEBUG)
        assert rootlogger.isEnabledFor(logging.ERROR)
    with logger_level(rootlogger, logging.DEBUG):
        assert rootlogger.isEnabledFor(logging.DEBUG)
        assert not rootlogger.isEnabledFor(logging.ERROR)
        assert rootlogger.isEnabledFor(logging.INFO)
        assert rootlogger.isEnabledFor(logging.WARNING)



# Generated at 2022-06-14 06:33:15.319168
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger()
    >>> log.info('test') # doctest: +ELLIPSIS
    <...>
    >>> with logger_level(log, logging.ERROR):
    ...     log.info('...')
    >>> log.info('test') # doctest: +ELLIPSIS
    <...>
    """
    pass



# Generated at 2022-06-14 06:33:17.655678
# Unit test for function configure
def test_configure():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')


# Generated at 2022-06-14 06:33:21.387737
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)

    with logger_level(log, logging.INFO):
        log.debug('No output')
        log.info('Yes output')

    log.debug('Yes output')
    log.info('Yes output')

# Generated at 2022-06-14 06:33:23.142875
# Unit test for function configure
def test_configure():
    logging.getLogger(__name__).info('test')



# Generated at 2022-06-14 06:33:30.885599
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.info("test")
    assert log.level == logging.DEBUG
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        log.info("test")
    assert log.level == logging.DEBUG



# Generated at 2022-06-14 06:33:36.672272
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()

    logger.info('test info start')
    logger.debug('test debug start')

    with logger_level(logger, logging.DEBUG):
        logger.info('test info')
        logger.debug('test debug')

    logger.info('test info end')
    logger.debug('test debug end')



# Generated at 2022-06-14 06:33:50.933463
# Unit test for function logger_level
def test_logger_level():
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        f = os.path.join(tmpdir, 'test_logger_level.txt')
        # Configure a logger
        logging_config = {
            'version': 1,
            'handlers': {
                'report_file': {
                    'class': 'logging.FileHandler',
                    'filename': f,
                    'formatter': 'simple',
                }
            },
            'formatters': {
                'simple': {
                    'format': '%(levelname)s %(message)s'
                },
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['report_file']
            },
        }
        logging.config.dictConfig(logging_config)



# Generated at 2022-06-14 06:34:11.329955
# Unit test for function logger_level
def test_logger_level():
    from logging import disable

    disable(logging.WARNING)  # Disable all loggers by default.

    log = get_logger(__name__ + ".test_logger_level")

    # Test that log level is informational.
    assert log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.WARNING)

    # Test that we can set log level to warning, that it sets and unsets properly.
    with logger_level(log, logging.WARNING):
        assert not log.isEnabledFor(logging.INFO)
        assert log.isEnabledFor(logging.WARNING)
    assert log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.WARNING)

# Generated at 2022-06-14 06:34:25.284321
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.config


# Generated at 2022-06-14 06:34:33.454167
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
        logger.debug('test debug')
        logger.info('test info')
        logger.warning('test warning')
        logger.error('test error')

    with logger_level(logger, logging.INFO):
        logger.debug('test debug')
        logger.info('test info')
        logger.warning('test warning')
        logger.error('test error')

# Generated at 2022-06-14 06:34:40.006027
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    configure()

    with logger_level(log, logging.DEBUG):
        log.debug('this message should show up')
        log.warning('this should not show up')

    log.warning('this message should show up')
    log.debug('this should not show up')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:42.659291
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        l = get_logger()
        assert l.level == logging.INFO



# Generated at 2022-06-14 06:34:52.745113
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test_logger_level')
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler(sys.stdout))
    with logger_level(log, logging.CRITICAL):
        log.debug('Debug message')
        assert not log.handlers[0].stream.getvalue()

    log.debug('Debug message')
    assert log.handlers[0].stream.getvalue()
    log.handlers[0].stream.truncate(0)



# Generated at 2022-06-14 06:34:55.105134
# Unit test for function configure
def test_configure():
    configure()
    logger = getLogger()
    logger.info('test_configure')



# Generated at 2022-06-14 06:35:04.331449
# Unit test for function logger_level
def test_logger_level():
    print('test logger_level')
    import logging.handlers
    handler = logging.handlers.SysLogHandler(address='/dev/log')
    logger = get_logger('foobar')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info('Level=%s' % logging.getLevelName(logger.level))
    with logger_level(logger, logging.WARNING):
        logger.info('Level=%s' % logging.getLevelName(logger.level))
    logger.info('Level=%s' % logging.getLevelName(logger.level))
