

# Generated at 2022-06-14 06:25:17.025711
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test')
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
        with logger_level(logger, logging.INFO):
            assert logger.level == logging.INFO
        assert logger.level == logging.ERROR


# For backwards compatibility with the "old" logging set-up, use root logger:
_ROOT_LOGGER = get_logger()



# Generated at 2022-06-14 06:25:28.264444
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    log = get_logger()
    buf = logging.handlers.MemoryHandler(100, target=sys.stderr)
    log.handlers=[buf]
    log.info("Before setting")
    with logger_level(log, logging.DEBUG):
        log.debug("Hello World!")
        log.debug("More!")
        log.info("Inside")
    log.info("After setting")
    assert (b"Before setting" in buf.buffer[0].getMessage())
    assert (b"Hello World!" in buf.buffer[1].getMessage())
    assert (b"More!" in buf.buffer[2].getMessage())
    assert (b"Inside" in buf.buffer[3].getMessage())
    assert (b"After setting" in buf.buffer[4].getMessage())



# Generated at 2022-06-14 06:25:38.697174
# Unit test for function get_config
def test_get_config():
    assert get_config(config='{"a": 1}')['a'] == 1
    assert get_config(config={'a': 1})['a'] == 1
    # assert get_config(config=b'{"a": 1}')['a'] == 1
    assert get_config(config='{"a": true}')['a']
    # assert get_config(config=b'{"a": true}')['a']
    assert get_config(config={'a': True})['a']
    # get_config(config=[]) is None  # TypeError
    # get_config(config=None) is None  # ValueError
    assert get_config(config='{"a": 1}')['a'] == 1
    assert get_config(config='a: 1')['a'] == 1

# Generated at 2022-06-14 06:25:45.216786
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
        logger.debug('this should not be displayed')
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
        logger.debug('this should be displayed')

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:25:52.368398
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG) as l:
        assert l.level == logging.DEBUG
        with logger_level(logger, logging.ERROR) as l:
            assert l.level == logging.ERROR
            with logger_level(logger, logging.DEBUG) as l:
                assert l.level == logging.DEBUG
        assert l.level == logging.DEBUG
    assert logger.level == logging.WARNING

# Generated at 2022-06-14 06:26:02.012101
# Unit test for function logger_level
def test_logger_level():
    import time
    logger = getLogger()
    count = 0
    with logger_level(logger, logging.INFO):
        assert logger.isEnabledFor(level=logging.INFO)
        logger.debug("this should not show")
        for x in range(5):
            logger.info("hello hello!!")
            count += 1
            time.sleep(0.1)

    assert logger.isEnabledFor(level=logging.DEBUG)
    assert count == 5

test_logger_level()



# Generated at 2022-06-14 06:26:06.519035
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug('test')
    assert log.level == logging.DEBUG

    with logger_level(log, logging.CRITICAL):
        log.debug('test2')
        assert log.level == logging.CRITICAL

    log.debug('test3')
    assert log.level == logging.DEBUG
test_logger_level()



# Generated at 2022-06-14 06:26:12.158495
# Unit test for function get_config

# Generated at 2022-06-14 06:26:20.728652
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)

    log.info('First info message')
    log.error('First error message')

    with logger_level(log, level=logging.ERROR):
        assert log.level == logging.ERROR
        log.info('Second info message')
        log.error('Second error message')

    assert log.level == logging.NOTSET
    log.info('Third info message')
    log.error('Third error message')

# Generated at 2022-06-14 06:26:22.406046
# Unit test for function configure
def test_configure():
    assert(logging.getLogger('requests').getEffectiveLevel() is logging.INFO)


# Generated at 2022-06-14 06:26:39.126464
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    assert log.level == logging.DEBUG, 'Logger level should be DEBUG'
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO, 'Logger level should be INFO'
    assert log.level == logging.DEBUG, 'Logger level should be DEBUG'


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    test_log

# Generated at 2022-06-14 06:26:52.899476
# Unit test for function get_config
def test_get_config():
    import logging
    import os

    assert logging.DEBUG == get_config(default=logging.DEBUG)
    assert logging.INFO == get_config(env_var="NOT_THERE", default=logging.INFO)
    assert logging.INFO == get_config(env_var="NOT_THERE", default=logging.INFO)

    # Test json config

# Generated at 2022-06-14 06:27:03.121827
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('logger_level')
    log.info('info message')
    with logger_level(log, logging.ERROR):
        log.info('info message')

# Testscript
if __name__ == '__main__':
    configure()
    log = get_logger('test')
    log.debug('debug message')
    log.info('info message')
    log.warn('warn message')
    log.error('error message')
    log.critical('critical message')
    try:
        raise Exception('exception message')
    except Exception as e:
        log.exception(e)
    test_logger_level()

# Generated at 2022-06-14 06:27:09.965930
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    configure()
    with logger_level(logger, logging.DEBUG):
        logger.debug(1)
        with logger_level(logger, logging.INFO):
            logger.debug(2)
            logger.info(3)
        logger.debug(4)
    logger.debug(5)
    logger.info(6)



# Generated at 2022-06-14 06:27:18.179809
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.isEnabledFor(logging.DEBUG) == True
        assert log.isEnabledFor(logging.ERROR) == False

    with logger_level(log, logging.ERROR):
        assert log.isEnabledFor(logging.DEBUG) == False
        assert log.isEnabledFor(logging.ERROR) == True

    assert log.isEnabledFor(logging.DEBUG) == True
    assert log.isEnabledFor(logging.ERROR) == False

# Generated at 2022-06-14 06:27:25.776561
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('testLogger') 

# Generated at 2022-06-14 06:27:33.391771
# Unit test for function logger_level
def test_logger_level():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    f = logging.Formatter('%(levelname)s|%(name)s: %(message)s')
    h.setFormatter(f)
    logger.addHandler(h)

    with logger_level(logger, logging.INFO):
        logger.debug('Testing logger_level')
        assert True

    logger.debug('Testing logger_level')
    assert True

# Generated at 2022-06-14 06:27:39.613370
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARNING):
        assert logger.level == logging.WARNING
        logger.debug("this should not show up")
    assert logger.level == logging.DEBUG
    logger.debug("this should show up")



# Generated at 2022-06-14 06:27:49.922130
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Logging messages at DEBUG level will be ignored
    logger.debug('This is a debug message')
    assert(True)

    with logger_level(logger, logging.DEBUG):
        # Logging messages at DEBUG level will be echoed back
        logger.debug('This is a debug message with set level')
        assert(True)

# Generated at 2022-06-14 06:27:54.276868
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        logger.debug('This should not be logged')
    logger.debug('This should be logged')


# Generated at 2022-06-14 06:28:03.927231
# Unit test for function get_config
def test_get_config():
    config = {'root': {'level': 'DEBUG'}}
    assert get_config(config) == config, 'Fail to get configuration'

    config = {'root': {'level': 'DEBUG'}}
    assert get_config(json.dumps(config)) == config, 'Fail to get configuration'

    try:
        get_config(None)
    except ValueError:
        pass
    else:
        assert False, 'Should raise ValueError'


# Generated at 2022-06-14 06:28:06.321276
# Unit test for function get_config
def test_get_config():
    with open('config.yaml') as f:
        config = get_config(default=f.read())
        print(config)


# Generated at 2022-06-14 06:28:13.335292
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger('test')
    logger.setLevel(logging.INFO)
    logger.info("test message")
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG, logger.level
    assert logger.level == logging.INFO, logger.level

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:28:22.315065
# Unit test for function configure
def test_configure():
    DEFAULT_CONFIG['formatters']['simple']['format'] = '%(asctime)s| %(name)s/%(process)d-%(thread)d: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s'
    configure()
    log = logging.getLogger(__name__)
    log.info("test")
    log.debug("test")
    log.warning("test")
    log.warn("test")
    log.error("test")
    log.critical("test")
    log.fatal("test")

# Generated at 2022-06-14 06:28:24.600021
# Unit test for function configure
def test_configure():
    log = logging.getLogger('test_configure')
    configure()
    log.error('test configure')


# Generated at 2022-06-14 06:28:26.577410
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)

# Generated at 2022-06-14 06:28:29.049826
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('py_utils')
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO



# Generated at 2022-06-14 06:28:32.694780
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    level = logger.level
    with logger_level(logger, logging.DEBUG):
        assert logger.level is logging.DEBUG
    assert logger.level is level

# Generated at 2022-06-14 06:28:40.221708
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('testing')
    logger.info("Testing if logger_level works")
    try:
        with logger_level(logger, logging.INFO):
            logger.info("Logger level is set to INFO")
    except:
        logger.info("Expected failure here")

if __name__ == '__main__':
    import logging
    import logging.config
    import logging_config_helper
    # configure()
    test_logger_level()
    logger = getLogger('test')
    logger.info('test')
    logger.info('test2')
    logger.info('test2')

# Generated at 2022-06-14 06:28:46.985801
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug("This should be printed by the logger")
    logger.debug("This should not be printed by the logger")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:53.537031
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    with logger_level(logger, logging.INFO):
        assert logger.getEffectiveLevel() == logging.INFO
    assert logger.getEffectiveLevel() != logging.INFO

# Generated at 2022-06-14 06:29:04.176807
# Unit test for function logger_level

# Generated at 2022-06-14 06:29:16.939626
# Unit test for function logger_level
def test_logger_level():
    logging.circular.capture()
    log = getLogger('test_logger_level')
    with logger_level(log, logging.DEBUG):
        log.debug('this is a debug message')
        log.info('this is an info message')
        log.warning('this is a warning message')
        log.error('this is an error message')
        log.critical('this is a critical message')
    log.debug('this is a debug message')
    log.info('this is an info message')
    log.warning('this is a warning message')
    log.error('this is an error message')
    log.critical('this is a critical message')

# Generated at 2022-06-14 06:29:22.582396
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        assert log.isEnabledFor(logging.ERROR)
        assert not log.isEnabledFor(logging.INFO)
    assert log.isEnabledFor(logging.INFO)
    assert not log.isEnabledFor(logging.ERROR)

test_logger_level()

# Generated at 2022-06-14 06:29:27.466656
# Unit test for function logger_level
def test_logger_level():
    """Basic tests for function logger_level"""
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.info('test info')
    with logger_level(log, logging.DEBUG):
        log.debug('test debug')
    log.info('test info continued')
    assert True



# Generated at 2022-06-14 06:29:39.363285
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.config
    import sys

    def get_logger(name=None):
        config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'simple': {
                    'format': '%(levelname)s %(name)s:%(lineno)d:%(message)s',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple',
                    'stream': sys.stderr,
                    'level': logging.DEBUG,
                },
            },
            'root': {
                'handlers': ['console'],
                'level': logging.DEBUG,
            },
        }

# Generated at 2022-06-14 06:29:45.193156
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__ + '.test_logger_level')
    with logger_level(logger, logging.INFO):
        logger.debug('huh?')
    logger.debug('yay!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test_logger_level()

# Generated at 2022-06-14 06:29:53.440020
# Unit test for function logger_level
def test_logger_level():
    """Unit test for function logger_level."""
    import contextlib
    import sys

    with contextlib.redirect_stdout(sys.stdout):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)        
        logger.info('test')
        #with logger_level(logger, logging.DEBUG):
        #    logger.debug('test')
        #logger.info('test')
        logger.setLevel(logging.DEBUG)

# Generated at 2022-06-14 06:30:00.449461
# Unit test for function configure
def test_configure():
    import logging
    import sys
    
    test_handler = logging.StreamHandler(sys.stdout)
    test_logger = logging.getLogger()
    test_logger.addHandler(test_handler)
    
    configure()
    
    #test_logger.warning('test')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:30:13.423975
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    logger = logging.getLogger("test")
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: '
        '%(message)s @%(funcName)s:%(lineno)d #%(levelname)s'
    )
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.ERROR)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    with logger_level(logger, logging.DEBUG):
        logger.critical("critical msg")
        logger.debug("last msg")
    logger

# Generated at 2022-06-14 06:30:21.932204
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, 10):
        assert log.level == 10
    assert log.level != 10
    with logger_level(log, 10):
        assert log.level == 10
    assert log.level != 10

# Generated at 2022-06-14 06:30:26.389865
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:30:28.664543
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug("Hello")

# Generated at 2022-06-14 06:30:39.730554
# Unit test for function logger_level
def test_logger_level():
    import contextlib
    import io
    import sys
    import logging

    with contextlib.redirect_stdout(io.StringIO()) as fake_out:
        log = get_logger('test_logger_level')
        with logger_level(log, logging.DEBUG):
            log.debug("This message should be shown")
            log.info("This message should be shown")
            log.warning("This message should be shown")
            log.error("This message should be shown")
            log.critical("This message should be shown")
        log.debug("This message should NOT be shown")
        log.info("This message should NOT be shown")
        log.warning("This message should NOT be shown")
        log.error("This message should NOT be shown")
        log.critical("This message should NOT be shown")

# Generated at 2022-06-14 06:30:51.394939
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys
    import os
    import os.path
    import tempfile

# Generated at 2022-06-14 06:31:00.488360
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger(__name__)
    >>> for level in ('debug', 'info', 'warning', 'error', 'critical',):
    ...     getattr(log, level)("test")
    ...     with logger_level(log, logging.CRITICAL):
    ...         getattr(log, level)("test")
    >>> for level in ('debug', 'info', 'warning', 'error', 'critical',):
    ...     getattr(log, level)("test")
    """


# Generated at 2022-06-14 06:31:04.145010
# Unit test for function get_config
def test_get_config():
    with open('test_logging.json', 'r') as f:
        config = f.read()

    cfg = get_config(config)
    assert cfg['handlers']['console']['level'] == 20
    assert cfg['version'] == 1



# Generated at 2022-06-14 06:31:16.125608
# Unit test for function logger_level
def test_logger_level():
    #import shutil
    #shutil.rmtree(os.path.join(os.environ['TMPDIR'], 'pylib'))
    import pylib.logger
    log = pylib.logger.getLogger(__name__)
    # import pdb; pdb.set_trace()
    log.critical('critical')
    log.error('error')
    log.warning('warning')
    log.info('info')
    log.debug('debug')
    with pylib.logger.logger_level(log, logging.ERROR):
        log.critical('critical')
        log.error('error')
        log.warning('warning')
        log.info('info')
        log.debug('debug')
    log.critical('critical')
    log.error('error')
    log

# Generated at 2022-06-14 06:31:25.322879
# Unit test for function get_config

# Generated at 2022-06-14 06:31:36.062208
# Unit test for function logger_level
def test_logger_level():
    from io import StringIO

    test_log = logging.getLogger("test_logger_level")
    test_log.setLevel(logging.INFO)

    fh = logging.StreamHandler(StringIO())
    test_log.addHandler(fh)

    test_log.info("foo")
    assert(fh.stream.getvalue() == "foo\n")

    with logger_level(test_log, logging.ERROR):
        test_log.info("bar")
        assert(fh.stream.getvalue() == "foo\n")

    test_log.info("baz")
    assert(fh.stream.getvalue() == "foo\nbaz\n")

# Generated at 2022-06-14 06:31:48.950201
# Unit test for function get_config
def test_get_config():
    config = dict(key='value')
    assert get_config(config) == config
    assert get_config(json.dumps(config)) == config
    assert get_config(yaml.dump(config)) == config



# Generated at 2022-06-14 06:31:59.864875
# Unit test for function configure
def test_configure():
    cfg = DEFAULT_CONFIG
    # Check if default configuration is valid
    configure(cfg)

    # Check if it is possible to set a specific format
    format = '%(asctime)s|%(message)s'
    cfg = DEFAULT_CONFIG
    cfg['formatters']['colored']['format'] = format
    configure(cfg)
    log = logging.getLogger(__name__)
    log.info('test')

    # Check if it is possible to set a specific handler
    format = '%(asctime)s|%(message)s'
    handler = 'logging.NullHandler'
    cfg = DEFAULT_CONFIG
    cfg['formatters']['colored']['format'] = format
    cfg['handlers']['console']['class']

# Generated at 2022-06-14 06:32:09.364981
# Unit test for function configure
def test_configure():
    cwd = os.getcwd()
    json_string = '{"version":1,"disable_existing_loggers":true,"formatters":{"simple":{"format":"%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s","datefmt":"%Y-%m-%d %H:%M:%S"}},"handlers":{"console":{"class":"logging.StreamHandler","formatter": "simple","level":20}},"root":{"handlers":["console"],"level":20},"loggers":{"requests":{"level":20}}}'

    # Test configure with invalid configuration

# Generated at 2022-06-14 06:32:16.680190
# Unit test for function get_config
def test_get_config():
    # Test reading config from JSON
    cfg = get_config('{"version": 1}')
    assert cfg == dict(version=1)

    # Test reading config from YAML
    cfg = get_config('version: 1')
    assert cfg == dict(version=1)

    # Test reading config from dict
    cfg = get_config({'version': 1})
    assert cfg == dict(version=1)

    # Test failure for bad config string
    try:
        get_config('{')
        assert False, 'should not reach this line'
    except ValueError:
        pass

    # Test failure for config that is not a string
    try:
        get_config(['{']);
        assert False, 'should not reach this line'
    except ValueError:
        pass



# Generated at 2022-06-14 06:32:23.629591
# Unit test for function logger_level
def test_logger_level():
    name = 'test_logger_level'
    l = getLogger(name)
    with logger_level(l, logging.DEBUG):
        assert l.isEnabledFor(logging.DEBUG)
        assert not l.isEnabledFor(logging.INFO)

    assert not l.isEnabledFor(logging.DEBUG)



# Generated at 2022-06-14 06:32:36.169677
# Unit test for function get_config
def test_get_config():
    # test with bare config string
    config = get_config('{"version": 1}')
    assert config["version"] == 1
    # test with json config string
    config = get_config('{"version": 1}')
    assert config["version"] == 1
    # test with yaml config string
    config = get_config('version: 1')
    assert config["version"] == 1
    # test with dict config
    config = get_config({'version': 1})
    assert config["version"] == 1
    # test with invalid config
    try:
        config = get_config(1)
    except ValueError:
        pass
    # test with default config
    config = get_config(default={'version': 1})
    assert config["version"] == 1

# Unit tests for function configure

# Generated at 2022-06-14 06:32:39.257679
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug("Hello World!")

# Generated at 2022-06-14 06:32:44.112201
# Unit test for function logger_level
def test_logger_level():
    configure()
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.error("This should not be logged")
        logger.debug("This should be logged")


# Generated at 2022-06-14 06:32:49.549285
# Unit test for function logger_level
def test_logger_level():
    import logging
    import time
    import random

    logger = logging.getLogger(__name__)
    old_logger_level = logger.level
    logger.setLevel(logging.DEBUG)
    for i in range(10):
        with logger_level(logger, logging.DEBUG):
            logger.debug("With debug level")
        time.sleep(random.randint(1, 3))
        with logger_level(logger, logging.INFO):
            logger.debug("With info level")
        time.sleep(random.randint(1, 3))
    logger.setLevel(old_logger_level)



##
# Func-decorators
##

# Generated at 2022-06-14 06:33:00.612230
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)

    with logger_level(logger, logging.DEBUG):
        logger.debug("Hello")
        logger.info("Info ignored")
        logger.warning("Warning ignored")
        logger.error("Error ignored")
        logger.critical("Criticl ignored")

    with logger_level(logger, logging.CRITICAL):
        logger.debug("Debug ignored")
        logger.info("Info ignored")
        logger.warning("Warning ignored")
        logger.error("Error ignored")
        logger.critical("Criticl ignored")


# Define log_calls decorator


# Generated at 2022-06-14 06:33:20.727011
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with logger_level(logger, logging.DEBUG):
        assert logger.isEnabledFor(logging.DEBUG)
        assert logger.isEnabledFor(logging.INFO)
        assert logger.isEnabledFor(logging.WARNING)
        with logger_level(logger, logging.INFO):
            assert logger.isEnabledFor(logging.DEBUG) == False
            assert logger.isEnabledFor(logging.INFO)
            assert logger.isEnabledFor(logging.WARNING)
        assert logger.isEnabledFor(logging.DEBUG)
        assert logger.isEnabledFor(logging.INFO)
        assert logger.isEnabledFor(logging.WARNING)
    assert logger.isEnabledFor(logging.DEBUG) == False
   

# Generated at 2022-06-14 06:33:32.639734
# Unit test for function get_config
def test_get_config():
    test_config = {'blah': 'blah'}
    # Test if it returns a valid config
    assert get_config(config=test_config) == test_config
    env_var = 'TEST'
    # Test if it returns a config from env
    del os.environ[env_var]
    os.environ[env_var] = str(test_config)
    assert get_config(env_var=env_var) == test_config
    # Test if it returns a default config
    del os.environ[env_var]
    assert get_config(default=test_config) == test_config
    # Test if it returns a valid config as string
    os.environ[env_var] = str(test_config)
    assert get_config(env_var=env_var) == test_

# Generated at 2022-06-14 06:33:37.190742
# Unit test for function logger_level
def test_logger_level():
    test_logger = getLogger('test_module')
    with logger_level(test_logger, logging.INFO):
        assert test_logger.level == logging.INFO
        test_logger.info('test message')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:33:44.038139
# Unit test for function logger_level
def test_logger_level():
    testlogger = get_logger(__name__)
    with logger_level(testlogger, logging.WARNING):
        assert testlogger.getEffectiveLevel() == logging.WARNING
    assert testlogger.getEffectiveLevel() == logging.DEBUG

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:33:49.609402
# Unit test for function logger_level
def test_logger_level():
    """
    Test function logger_level
    """
    log = get_logger()
    try:
        with logger_level(log, logging.DEBUG):
            log.debug('testing')
        assert 0, 'DEBUG log should not work outside of context manager'
    except AttributeError:
        pass



# Generated at 2022-06-14 06:33:55.946829
# Unit test for function get_config
def test_get_config():
    cfg = get_config('{"a": "b"}')
    assert cfg == dict(a='b')
    cfg = get_config('{"c": "d"}')
    assert cfg == dict(c='d')
    cfg = get_config({"e": "f"})
    assert cfg == dict(e='f')
    cfg = get_config()
    assert cfg == DEFAULT_CONFIG

# Generated at 2022-06-14 06:34:05.496324
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger('test_logger')
    logger.setLevel(logging.WARNING)

    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
        assert logger.isEnabledFor(logging.DEBUG) is True
        logger.debug('debug level')

    assert logger.getEffectiveLevel() == logging.WARNING
    assert logger.isEnabledFor(logging.DEBUG) is False
    logger.debug('debug level')


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:13.543481
# Unit test for function logger_level
def test_logger_level():
    # setup logger
    cfg = DEFAULT_CONFIG.copy()
    configure(cfg)
    logger_name = 'test'

    # logging message to console
    log = get_logger(logger_name)
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')

    # logging message to console with DEBUG level
    with logger_level(log, logging.DEBUG):
        log.debug('Debug message')
        log.info('Info message')
        log.warning('Warning message')
        log.error('Error message')

    # no message should be printed
    with logger_level(log, logging.CRITICAL):
        log.debug('Debug message')
        log.info('Info message')
        log.warning('Warning message')


# Generated at 2022-06-14 06:34:16.757104
# Unit test for function logger_level
def test_logger_level():
    logger_level(get_logger(), logging.DEBUG)

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:21.740045
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("DEBUG")
        log.info("INFO")

    with logger_level(log, logging.INFO):
        log.debug("DEBUG")
        log.info("INFO")

# Generated at 2022-06-14 06:34:44.319391
# Unit test for function configure
def test_configure():
    configure()
    log = logging.getLogger(__name__)
    # return logger object
    assert isinstance(log, logging.Logger)


DEFAULT_PYTHON_LOG_PATH = '/var/log/python_%s_%s.log'
DEFAULT_PYTHON_LOG_FORMAT = '%(name)s %(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
DEFAULT_PYTHON_LOG_LEVEL = logging.INFO



# Generated at 2022-06-14 06:34:48.721210
# Unit test for function logger_level
def test_logger_level():
    import logging
    import logging.config


# Generated at 2022-06-14 06:34:56.975844
# Unit test for function logger_level
def test_logger_level():
    _ensure_configured()
    log = logging.getLogger('test_logger_level')
    with logger_level(log, logging.INFO):
        log.debug('Should NOT be printed')
        log.info('Should be printed')
    log.debug('Should NOT be printed')
    log.info('Should NOT be printed')
    log.warning('Should be printed')
    log.error('Should be printed')
    log.critical('Should be printed')



# Generated at 2022-06-14 06:34:59.479075
# Unit test for function configure
def test_configure():
    configure()
    log = logging.getLogger(__name__)
    log.info('test')

# Generated at 2022-06-14 06:35:14.021873
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    import os
    import shutil
    import time

    TMP_DIR = tempfile.gettempdir()

    logfile = os.path.join(TMP_DIR, 'test.log')
