

# Generated at 2022-06-14 06:25:14.273985
# Unit test for function logger_level
def test_logger_level():
    output = io.StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(output)
    logger.addHandler(handler)
    with logger_level(logger, logging.DEBUG):
        logger.debug('foo')
    handler.flush()
    assert 'foo' in output.getvalue()
    output.close()



# Generated at 2022-06-14 06:25:22.170624
# Unit test for function logger_level
def test_logger_level():
    import sys
    from cStringIO import StringIO

    teststring = 'Test string'
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        logger = getLogger()
        logger.setLevel(logging.CRITICAL)

        logger.info(teststring)
        assert teststring not in out.getvalue()

        with logger_level(logger, logging.DEBUG):
            logger.info(teststring)
            assert teststring in out.getvalue()

        out.close()
    finally:
        sys.stdout = saved_stdout

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:31.037247
# Unit test for function get_config
def test_get_config():
    import datetime

    # Bare
    assert get_config(default={'test': 'hi'}) == {'test': 'hi'}

    # JSON
    assert get_config(
        default='{"test": "hi"}'
    ) == {'test': 'hi'}

    # YAML
    assert get_config(
        default='test: hi \\n date: %s' % datetime.datetime.now()
    ) == {'test': 'hi', 'date': datetime.datetime.now()}

    assert get_config(default='{"test": "hi"}') == {'test': 'hi'}


# Generated at 2022-06-14 06:25:38.708393
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)
    logger.debug('test_debug')
    logger.info('test_info')
    with logger_level(logger,logging.DEBUG):
        logger.debug('within context')
    logger.info('test_info_outside_context')

if __name__ == '__main__':
    sys.exit(test_logger_level())

# Generated at 2022-06-14 06:25:42.137484
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, logging.INFO) as l:
        assert l is None
        assert logger.level == logging.INFO
    assert logger.level != logging.INFO

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:25:46.320788
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)

    logger.info("This should be printed")
    with logger_level(logger, logging.ERROR):
        logger.info("This should be supressed")
        logger.error("This should be printed")
    logger.info("This should be printed")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test_logger_level()

# Generated at 2022-06-14 06:25:56.683061
# Unit test for function logger_level
def test_logger_level():
    # Test logger_level context manager with a few level values
    for test_level in (logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG):
        # Temporary file location for a logger's output
        fd, tmp_filename = tempfile.mkstemp()
        # Create the logger
        with open(tmp_filename, 'w') as f:
            logger = logging.getLogger("test_logger_level")
            logger.propagate = False
            logger.setLevel(logging.NOTSET)
            handler = logging.FileHandler(tmp_filename)
            handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
            logger.addHandler(handler)

            # Use the logger with level INF0

# Generated at 2022-06-14 06:26:01.906993
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.ERROR):
        assert l.level == logging.ERROR
    assert l.level == logging.DEBUG
    with logger_level(l, logging.INFO):
        assert l.level == logging.INFO
        raise ValueError
    assert l.level == logging.DEBUG

test_logger_level()

# Generated at 2022-06-14 06:26:10.759220
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.ERROR):
        pass
    with logger_level(logger, logging.INFO):
        logger.debug('test')
        logger.info('test')
        logger.warning('test')
        logger.error('test')
    with logger_level(logger, logging.DEBUG):
        logger.debug('test')
        logger.info('test')
        logger.warning('test')
        logger.error('test')


if __name__ == '__main__':
    configure()
    test_logger_level()

# Generated at 2022-06-14 06:26:17.251357
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    with logger_level(logger, logging.CRITICAL):
        logger.info('this should not get logged')

    logger.info('this should get logged')


getLoggerLevel = logger_level



# Generated at 2022-06-14 06:26:25.156421
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.debug("debug")
        logger.info("info")

        with logger_level(logger, logging.ERROR):
            assert logger.level == logging.ERROR
            logger.debug("debug")
            logger.error("error")

# Generated at 2022-06-14 06:26:32.864770
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()

    # Test that logger_level is working
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level != logging.DEBUG

    # Test that logger_level raises an exception if exception occurs
    with logger_level(logger, logging.DEBUG):
        raise Exception
    assert logger.level != logging.DEBUG


# Generated at 2022-06-14 06:26:43.610809
# Unit test for function logger_level
def test_logger_level():
    class StringStreamHandler(logging.Handler):
        def emit(self, record):
            s = self.format(record)
            self.stream.write(s)

    log = get_logger()

    str_handler = StringStreamHandler()
    str_handler.setLevel(logging.INFO)
    str_handler.setFormatter(logging.Formatter('%(message)s'))

    log.setLevel(logging.INFO)

    log.addHandler(str_handler)

    logger_level_scope = logger_level(log, logging.WARNING)

    log.info('this should not be seen')

    with logger_level_scope:
        log.info('this should be seen')

    output = str_handler.stream.getvalue()

    assert output == 'this should be seen'

# Generated at 2022-06-14 06:26:47.342641
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    initial_level = logger.level
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == initial_level

# Generated at 2022-06-14 06:26:51.115952
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()
    with logger_level(logger, logging.DEBUG):
        logger.debug('Debug message')
    logger.info('Info message')

# vim: et:sw=4:syntax=python:ts=4:

# Generated at 2022-06-14 06:26:52.731638
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG



# Generated at 2022-06-14 06:27:04.537269
# Unit test for function logger_level
def test_logger_level():
    # logger_level must be importable as gingertel.logging.logger_level
    from gingertel.logging import logger_level
    import logging
    # Raise exception if logger_level is not a context manager
    with logger_level:
        raise Exception('logger_level must be a context manager')
    with logger_level(logging.getLogger(), logging.CRITICAL):
        # CRITICAL level should not print DEBUG level logs
        logger = logging.getLogger()
        logger.debug('This log must not be printed')
    with logger_level(logging.getLogger(), logging.DEBUG):
        # DEBUG level should print DEBUG level logs
        logger = logging.getLogger()
        logger.debug('This log must be printed')
    # logger_level must be able to restore the original logger level
   

# Generated at 2022-06-14 06:27:14.634603
# Unit test for function get_config
def test_get_config():
    from tempfile import NamedTemporaryFile
    import json

    config = dict(key1='value1', key2='value2')

    with NamedTemporaryFile(mode='w+') as fp:
        json.dump(config, fp)
        fp.flush()
        output = get_config(fp.name)
        assert output == config

    with NamedTemporaryFile(mode='w+') as fp:
        yaml.dump(config, fp)
        fp.flush()
        output = get_config(fp.name)
        assert output == config



# Generated at 2022-06-14 06:27:19.470679
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.INFO):
        logger.info("INFO message")

    with logger_level(logger, logging.WARNING):
        logger.warning("WARNING message")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:27:21.916442
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        assert logger.level is logging.INFO

    assert logger.level is logging.DEBUG


# Generated at 2022-06-14 06:27:31.804443
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info('default verbosity')
    with logger_level(log, logging.DEBUG):
        assert log.getEffectiveLevel() <= logging.DEBUG
        log.debug('debug verbosity')
    assert log.getEffectiveLevel() <= logging.INFO



# Generated at 2022-06-14 06:27:38.583364
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    configure()
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.debug('foo')
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:27:42.639625
# Unit test for function logger_level
def test_logger_level():
    import logging

    root = logging.getLogger()
    configure()
    with logger_level(root, logging.CRITICAL):
        assert root.level == logging.CRITICAL
    assert root.level == logging.DEBUG


# Generated at 2022-06-14 06:27:50.642824
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()
    # logger_level is part of a context manager, so it is only
    # tested for that case
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
    assert logger.isEnabledFor(logging.INFO)

    with logger_level(logger, logging.INFO):
        assert not logger.isEnabledFor(logging.DEBUG)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:27:52.528126
# Unit test for function get_config
def test_get_config():
    config = get_config(env_var='logging')


# Generated at 2022-06-14 06:27:57.269198
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        logger.debug('This is a DEBUG messaage')
        logger.info('This is an INFO message')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:02.493086
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    with logger_level(log, logging.DEBUG):
        log.debug('test')
    log.info('test')
    log.debug('test')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:14.940732
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
    # output: warning message
    #         error message
    #         critical message

    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')
        # output: debug message
        #         info message
        #         warning message
        #         error message
        #         critical message

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')


# Generated at 2022-06-14 06:28:18.887723
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.NOTSET


# Generated at 2022-06-14 06:28:24.110495
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    configure()
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.debug('debug log')
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
        logger.debug('debug log')



# Generated at 2022-06-14 06:28:35.252524
# Unit test for function logger_level
def test_logger_level():
    from datetime import datetime

    import sys, io
    out = io.StringIO()
    sys.stdout = out

    logger_level(logging.getLogger(__name__), logging.WARNING)
    log = get_logger(__name__)
    initial_logger_level = logging.getLogger(__name__).level
    log.info('Initial logger level is %s'%initial_logger_level)
    log.info('test_logger_level_info_msg')
    log.debug('test_logger_level_debug_msg')
    log.warning('test_logger_level_warning_msg')
    log.error('test_logger_level_error_msg')
    log.critical('test_logger_level_critical_msg')


# Generated at 2022-06-14 06:28:40.434917
# Unit test for function logger_level
def test_logger_level():
    root_logger = logging.getLogger()
    root_logger.setLevel(1)
    with logger_level(root_logger, logging.DEBUG):
        assert root_logger.level == logging.DEBUG
        root_logger.debug('test')
    assert root_logger.level == 1



# Generated at 2022-06-14 06:28:53.956017
# Unit test for function get_config
def test_get_config():
    # Testing if given a bare string value
    cfg = get_config(config='DEBUG', env_var=None, default=None)
    assert cfg == 'DEBUG', "Config value should be DEBUG, but got: {}".format(cfg)

    # Testing if given a JSON string value
    cfg = get_config(config='{"a": 1, "b": "2"}', env_var=None, default=None)
    assert cfg == {"a": 1, "b": "2"}, "Config value should be {'a': 1, 'b': '2'}, but got: {}".format(cfg)

    # Testing if given YAML string value
    cfg = get_config(config="a: 1\nb: 2\n", env_var=None, default=None)

# Generated at 2022-06-14 06:28:59.083444
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('test_debug')
        logger.info('test_info')

    with logger_level(logger, logging.INFO):
        logger.debug('test_debug')
        logger.info('test_info')

# Generated at 2022-06-14 06:29:02.742311
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.INFO):
        logger.debug('foo')
        logger.info('bar')

# Generated at 2022-06-14 06:29:06.493832
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, 20):
        log.warning("with test")
    log.critical("not with test")


# Generated at 2022-06-14 06:29:15.063060
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test_logr.logger_level')
    with logger_level(log, logging.DEBUG):
        log.debug('logging at debug level')
        log.info('logging at info level')
        log.warning('logging at warning level')
        log.error('logging at error level')
        log.critical('logging at critical level')
    # Next test should pass after the with block
    log.debug('Still logging at debug level', logging.WARNING)

test_logger_level()

# Generated at 2022-06-14 06:29:22.095938
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.CRITICAL):
        assert log.getEffectiveLevel() == logging.CRITICAL
    assert log.getEffectiveLevel() == logging.DEBUG

if __name__ == '__main__':
    configure()
    log = get_logger()
    log.info('info')
    log.debug('debug')
    log.error('error')
    log.warn('warn')

# Generated at 2022-06-14 06:29:29.711498
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    from logtime import logger_level

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    log.addHandler(handler)

    with logger_level(log, logging.DEBUG):
        log.debug('this will print')
        log.info('this will print')
        log.warning('this will print')

    log.info('this will NOT print')

# Generated at 2022-06-14 06:29:37.595318
# Unit test for function logger_level
def test_logger_level():
    """Unit test for function logger_level"""
    import time
    import logging
    logger = logging.getLogger('testing_logger_level')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    with logger_level(logger, logging.DEBUG):
        logger.info('info message 1')
        time.sleep(0.1)
        logger.info('info message 2')
        time.sleep(0.1)
        logger.info('info message 3')
        time.sleep(0.1)



# Generated at 2022-06-14 06:29:52.584744
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('test_logger_level: This should be set to DEBUG')
        logger.info('test_logger_level: This should be set to DEBUG')
    logger.info('test_logger_level: This should be set to INFO')
    logger.debug('test_logger_level: This should be set to DEBUG')



# Generated at 2022-06-14 06:30:01.921335
# Unit test for function logger_level
def test_logger_level():
    import time
    logger = get_logger()
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
        # This sleep is necessary for the logger to initialize the logger_level inside the with statement.
        # Otherwise, the level does not change in time and the message is logged.
        time.sleep(0.1)
        logger.debug('This message should not be logged.')
    assert logger.level == logging.DEBUG
    logger.debug('This message should be logged.')

# Generated at 2022-06-14 06:30:07.157203
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.WARN):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.debug('Should be suppressed')
        logger.warn('Should NOT be suppressed')

# Generated at 2022-06-14 06:30:20.159501
# Unit test for function get_config
def test_get_config():
    import json


# Generated at 2022-06-14 06:30:28.790890
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger_level')
    with logger_level(logger, logging.DEBUG):
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



# Generated at 2022-06-14 06:30:35.795831
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    # Only ERROR logs will be shown.
    with logger_level(logger, logging.ERROR):
        logger.debug("Debug log is not shown")
        logger.info("Info log is not shown")
        logger.error("Error log is shown")
    # Log all
    logger.debug("Debug log is shown")
    logger.info("Info log is shown")
    logger.error("Error log is shown")




# Generated at 2022-06-14 06:30:42.479952
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    assert logger.level == logging.NOTSET

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG

    assert logger.level == logging.NOTSET

# When run directly (not imported) run unit test
if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:52.255777
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(__name__), logging.CRITICAL):
        assert get_logger(__name__).isEnabledFor(logging.CRITICAL)
        assert not get_logger(__name__).isEnabledFor(logging.WARNING)
        assert not get_logger(__name__).isEnabledFor(logging.INFO)
        assert not get_logger(__name__).isEnabledFor(logging.DEBUG)

    assert get_logger(__name__).isEnabledFor(logging.DEBUG)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:31:03.968755
# Unit test for function logger_level
def test_logger_level():
    l = get_logger("test_logger_level")
    l.debug("Test nothing ")
    with logger_level(l, logging.DEBUG):
        l.debug("Test debug ")
        with logger_level(l, logging.INFO):
            l.info("Test info ")
            with logger_level(l, logging.WARNING):
                l.warning("Test warning ")
                with logger_level(l, logging.ERROR):
                    l.error("Test error ")
                    with logger_level(l, logging.CRITICAL):
                        l.critical("Test critical ")
    # l.setLevel(logging.INFO)
    l.debug("Test nothing ")
    with logger_level(l, logging.DEBUG):
        l.debug("Test debug ")

# Generated at 2022-06-14 06:31:12.067160
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("debug")
    with logger_level(log, logging.INFO):
        log.info("info")
    with logger_level(log, logging.WARNING):
        log.warn("warning")
    with logger_level(log, logging.ERROR):
        log.error("error")
    with logger_level(log, logging.CRITICAL):
        log.critical("critical")



# Generated at 2022-06-14 06:31:28.565250
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.root, logging.INFO):
        log = getLogger(__name__)
        log.debug("debug stash")
        log.info("info stash")
        log.warning("warning stash")
        log.error("error stash")
        log.critical("critical stash")

        output = ''.join(sys.stderr)

        assert "debug stash" not in output
        assert "info stash" in output
        assert "warning stash" in output
        assert "error stash" in output
        assert "critical stash" in output



# Generated at 2022-06-14 06:31:37.571487
# Unit test for function logger_level
def test_logger_level():
    # Assert that the initial logger level is NOT 'DEBUG'
    assert get_logger().level != logging.DEBUG
    with logger_level(get_logger(), logging.DEBUG):
        # Assert that the logger level is now 'DEBUG' within the context block
        assert get_logger().level == logging.DEBUG
        # Assert that the logger level is NOT 'DEBUG' outside of the context block
    assert get_logger().level != logging.DEBUG

# Generated at 2022-06-14 06:31:44.709023
# Unit test for function get_config
def test_get_config():
    def assert_config(expected, given, env_var='LOGGING', default=DEFAULT_CONFIG):
        config = get_config(
            given=given,
            env_var=env_var,
            default=default
        )
        assert config == expected
        logging.config.dictConfig(config)

    assert_config(DEFAULT_CONFIG, None)
    assert_config(DEFAULT_CONFIG, DEFAULT_CONFIG)

    given_json = '{"loggers": {"test": {"level": "WARN"}}}'
    expected_json = dict(DEFAULT_CONFIG, **dict(loggers={'test': {'level': 'WARN'}}))
    assert_config(expected_json, given_json)

    given_yaml = """loggers:
  test:
    level: WARN
"""
   

# Generated at 2022-06-14 06:31:52.637787
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.INFO):
        assert log.isEnabledFor(logging.INFO)
        assert not log.isEnabledFor(logging.DEBUG)
    assert log.isEnabledFor(logging.DEBUG)

if __name__ == '__main__':
    if os.getenv('DEBUG'):
        from test_utils import call
        call(test_logger_level)

# Generated at 2022-06-14 06:31:56.438443
# Unit test for function logger_level
def test_logger_level():
    get_logger().debug('Old message should be suppressed')
    with logger_level(get_logger(), logging.DEBUG):
        get_logger().debug('New message should appear')



# Generated at 2022-06-14 06:32:01.305201
# Unit test for function logger_level
def test_logger_level():
    # Setup
    logger = get_logger('this.is.a.test')
    logger.level = logging.CRITICAL
    assert logger.level == logging.CRITICAL
    
    # Raise level to INFO
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.info('Hello from the logger.')
    
    # Reset level to CRITICAL
    assert logger.level == logging.CRITICAL
    logger.info('This is a blind test.')

# Generated at 2022-06-14 06:32:04.910488
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger()
    with logger_level(logger, logging.DEBUG):
        logger.debug('test')
    assert logger.getEffectiveLevel() == logging.DEBUG


# Generated at 2022-06-14 06:32:11.327949
# Unit test for function logger_level
def test_logger_level():
    import io
    import io
    import sys
    from contextlib import contextmanager

    with io.StringIO() as buf:
        sys.stdout = buf
        logger = getLogger()
        with logger_level(logger, logging.WARNING):
            logger.info('test')
            assert buf.getvalue() == ""
            logger.warning('test')
            assert buf.getvalue() == "test\n"

# Generated at 2022-06-14 06:32:20.213713
# Unit test for function logger_level
def test_logger_level():
    # logging has not been configured, so explicitly create a logger for this test.
    logger = logging.Logger('test_logger')
    logger.addHandler(logging.StreamHandler())
    # The logger level is not set at the beginning of the test, so the level should be 0 (NOTSET).
    assert logger.level == 0
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == 0
test_logger_level()

# Generated at 2022-06-14 06:32:26.061246
# Unit test for function logger_level
def test_logger_level():
    from unittest.mock import Mock

    logger = Mock(spec=logging.Logger)
    with logger_level(logger, logging.DEBUG):
        assert(logger.level == logging.DEBUG)
    # Level should be back to what it was.
    assert(logger.level is None)

# Generated at 2022-06-14 06:32:50.830947
# Unit test for function get_config
def test_get_config():
    from tempfile import NamedTemporaryFile

    f = NamedTemporaryFile(mode='w', delete=False)

# Generated at 2022-06-14 06:33:04.030566
# Unit test for function logger_level
def test_logger_level():
    from unittest import TestCase
    from contextlib import contextmanager
    import logging

    class TestLogger(logging.Logger):
        """ Logger that records level changes and writes them in a list """
        def __init__(self, name):
            logging.Logger.__init__(self, name)
            self.log_level = []
        def setLevel(self, level):
            self.log_level.append(level)
            logging.Logger.setLevel(self, level)

    class LoggerLevelTest(TestCase):
        """ Unittest case for function logger_level """

        def test_logger_level(self):
            logger = TestLogger("test")
            logger.setLevel(logging.ERROR)
            with logger_level(logger, logging.DEBUG):
                pass

# Generated at 2022-06-14 06:33:17.980668
# Unit test for function get_config

# Generated at 2022-06-14 06:33:25.608643
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.FATAL):
        assert logger.isEnabledFor(logging.FATAL)
        assert not logger.isEnabledFor(logging.INFO)

test_logger_level()


# import atexit
# atexit.register(logging.shutdown)

# Generated at 2022-06-14 06:33:29.474797
# Unit test for function logger_level
def test_logger_level():
    with logger_level(logging.getLogger(), logging.INFO):
        assert logging.getLogger().getEffectiveLevel() == logging.INFO
    assert logging.getLogger().getEffectiveLevel() == 10



# Generated at 2022-06-14 06:33:35.640891
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
        logger.debug("Testing logger_level")
    assert logger.level == logging.INFO
        # assert False, "Should not get here"
    # logger.debug("Testing logger_level with assertion %r", False)

# Generated at 2022-06-14 06:33:44.633878
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
    logger.warning('warning message')
    logger.info('info message')
    logger.debug('debug message')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:33:51.981962
# Unit test for function logger_level
def test_logger_level():
    import logging

    #test if within context block
    with logger_level(logging.getLogger(),logging.INFO):
        logging.debug("debug")

    #test if level is in initialization
    with logger_level(logging.getLogger(), logging.INFO):
        logging.debug("debug")

    #test if level is restored correctly after context block
    with logger_level(logging.getLogger(), logging.DEBUG):
        logging.debug("debug")

# Generated at 2022-06-14 06:33:57.201333
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    filename = tempfile.mkstemp()[1]
    with logger_level(logging.getLogger(), logging.DEBUG) as l:
        logging.debug('test')
        assert l.level == logging.DEBUG
    os.remove(filename)

# Generated at 2022-06-14 06:34:00.329818
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, 100):
        assert logger.level == 100
    assert logger.level != 100


# Generated at 2022-06-14 06:34:24.470639
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()

    ctx = logger_level(log, logging.WARN)
    ctx.__enter__()

    log.info('test')
    log.error('test')

    ctx.__exit__(None, None, None)


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:27.496362
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert(log.level == logging.DEBUG)
    assert(log.level == logging.DEBUG)


# Generated at 2022-06-14 06:34:36.483885
# Unit test for function logger_level
def test_logger_level():
    logging.config.dictConfig(DEFAULT_CONFIG)
    log = logging.getLogger('testfunction')
    log.info('test1')
    # Make sure the above code worked
    assert len(log.handlers[0].messages['info']) == 1
    with logger_level(log, logging.CRITICAL):
        log.info('test2')
    # Make sure the inner block worked
    assert len(log.handlers[0].messages['info']) == 1


# Generated at 2022-06-14 06:34:43.723470
# Unit test for function get_config
def test_get_config():
    # Test parse config if dict
    cfg = dict(
        a=1,
        b='2'
    )
    assert get_config(cfg) == cfg

    # Test parse config if str
    cfg = '{"a": 1, "b": "2"}'
    assert get_config(cfg) == dict(
        a=1,
        b='2'
    )

    # Test parse config if str if yaml format
    cfg = """
    a: 1
    b: 2
    """
    assert get_config(cfg) == dict(
        a=1,
        b=2
    )

    # Test Exception if config not right
    cfg = '{a: 1, b: 2}'
    try:
        get_config(cfg)
    except ValueError:
        pass
   

# Generated at 2022-06-14 06:34:47.811310
# Unit test for function configure
def test_configure():
    import json

    logging.basicConfig()
    logger = get_logger()
    configure(json.dumps(DEFAULT_CONFIG))
    logger.info('test')
    assert False



# Generated at 2022-06-14 06:35:00.695926
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    assert log.level == logging.DEBUG, "log level should be DEBUG, not %s" % log.level
    log.debug("test_logger_level initial debug")
    with logger_level(log, logging.WARNING):
        log.critical("test_logger_level CRITICAL inside context")
        log.error("test_logger_level ERROR inside context")
        log.warning("test_logger_level WARNING inside context")
        log.debug("test_logger_level DEBUG inside context")
        log.info("test_logger_level INFO inside context")
    log.debug("test_logger_level debug after context")
    log.info("test_logger_level info after context")

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:35:09.338742
# Unit test for function configure
def test_configure():
    from tempfile import NamedTemporaryFile
    from os import remove
