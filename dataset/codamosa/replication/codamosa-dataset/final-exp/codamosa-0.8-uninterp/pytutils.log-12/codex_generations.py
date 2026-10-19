

# Generated at 2022-06-14 06:25:14.149802
# Unit test for function configure
def test_configure():
    _CONFIGURED[:] = []
    configure()
    log = getLogger(__name__)
    log.info('test')


# Generated at 2022-06-14 06:25:18.405022
# Unit test for function logger_level
def test_logger_level():
    """
    >>> import logging
    >>> log = logging.getLogger('test_logger_level')
    >>> with logger_level(log, logging.CRITICAL):
    ...     log.debug('not seen')
    ...     log.error('seen')
    """
    pass

# Generated at 2022-06-14 06:25:21.516603
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.INFO):
        log.debug('Should be ignored')
    log.debug('Restored')

# Generated at 2022-06-14 06:25:23.101309
# Unit test for function configure
def test_configure():
    log = get_logger()
    log.debug('test')



# Generated at 2022-06-14 06:25:30.346388
# Unit test for function logger_level
def test_logger_level():
    import logging
    log = logging.getLogger('test')
    log.addHandler(logging.StreamHandler())
    log.setLevel(150)

    with logger_level(log, logging.DEBUG):
        log.debug("debug logging at debug level")
        log.warning("warning logging at debug level")
        log.error("error logging at debug level")

    log.debug("debug logging at 150 level")
    log.warning("warning logging at 150 level")
    log.error("error logging at 150 level")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:25:42.628126
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('test')
    initial = log.level
    try:
        with logger_level(log, logging.DEBUG):
            log.debug('some debug message')
            log.info('some info message')
            assert True
    finally:
        log.level = initial

    log.info('and an info message')
    log.debug('and a debug message')
    assert True

    try:
        logger_level(log, logging.DEBUG)
        log.debug('some debug message')
        log.info('some info message')
        assert False
    except:
        assert True

    try:
        logger_level(log, initial)
        assert True
    except:
        assert False



# Generated at 2022-06-14 06:25:45.078675
# Unit test for function logger_level
def test_logger_level():
    log = getLogger('test_logger_level')
    with logger_level(log, logging.DEBUG):
        log.info('test_logger_level')



# Generated at 2022-06-14 06:25:48.912435
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.WARN):
        log.info('Will not print')
    log.info('Will print')



# Generated at 2022-06-14 06:25:51.974163
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 06:25:54.948554
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger("test_logger_level")
    with logger_level(logger, logging.ERROR):
        logger.debug("shoud not see this")
        logger.error("should see this")

# Generated at 2022-06-14 06:26:05.112852
# Unit test for function get_config
def test_get_config():
    test_config = {'test': 'test'}
    assert get_config(test_config) == get_config(json.dumps(test_config)) == get_config(yaml.safe_dump(test_config))
    assert get_config(yaml.safe_dump(test_config)) == yaml.load(yaml.safe_dump(test_config))
    assert get_config() == DEFAULT_CONFIG

if __name__ == '__main__':
    import nose
    nose.main()

# Generated at 2022-06-14 06:26:07.436847
# Unit test for function get_config
def test_get_config():
    assert get_config({"a": "b"}) == {"a": "b"}


# Generated at 2022-06-14 06:26:16.323338
# Unit test for function logger_level
def test_logger_level():
    from contextlib import redirect_stdout
    import io
    import sys

    orig_stdout = sys.stdout
    fake_stdout = io.StringIO()
    with redirect_stdout(fake_stdout):
        log = get_logger()
        log.error('this should not print')
        with logger_level(log, logging.ERROR):
            log.error('this should print')
            with logger_level(log, logging.INFO):
                log.info('this should print')
            log.info('this should not print')

    fake_stdout.seek(0)
    output = fake_stdout.read()
    print(output)
    assert 'should print' in output
    assert 'should not print' not in output
    sys.stdout = orig_stdout



# Generated at 2022-06-14 06:26:25.319207
# Unit test for function logger_level
def test_logger_level():
    strIO = StringIO()
    streamHandler = logging.StreamHandler(strIO)
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s'))

    logger = logging.getLogger('logger_level')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(streamHandler)

    logger.debug('first')
    logger.info('second')

    with logger_level(logger, logging.INFO):
        logger.debug('third')
        logger.info('forth')

    logger.debug('fifth')
    logger.info('sixth')


# Generated at 2022-06-14 06:26:30.956142
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    with logger_level(log, logging.INFO):
        log.debug('You should not see this')
        log.info('This will be visible')
    log.debug('And now you should see this')


# Generated at 2022-06-14 06:26:42.605483
# Unit test for function get_config
def test_get_config():
    import json
    import yaml

    cfg1 = dict(
        root = dict(level = 'DEBUG'),
        loggers = dict(
            requests = dict(level = 'INFO')
        )
    )
    

# Generated at 2022-06-14 06:26:48.682785
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger(__name__)
    configure()
    with logger_level(l, logging.DEBUG):
        l.debug(__name__)
    l.log(logging.INFO, __name__)  # should not print
    with logger_level(l, logging.INFO):
        l.debug(__name__)
        l.info(__name__)
    l.log(logging.DEBUG, __name__)  # should not print



# Generated at 2022-06-14 06:26:50.465379
# Unit test for function configure
def test_configure():
    logging.getLogger('__main__').info('test')

# Generated at 2022-06-14 06:26:56.169133
# Unit test for function logger_level
def test_logger_level():
    lvl = logging.DEBUG
    log = get_logger('test_logger_level')
    with logger_level(log, lvl):
        log.warn('This is a test of %s. It should print, and print at level %s', 'logger_level', lvl)
    log.warn('This is a test of %s. It should not print', 'logger_level')


# Generated at 2022-06-14 06:27:09.475174
# Unit test for function get_config
def test_get_config():
    from collections import OrderedDict
    import json

    assert get_config(None, None, None) is None

    cfg = get_config(None, None, OrderedDict([
        ('foo', OrderedDict([('bar', 'baz')])),
    ]))
    assert cfg == OrderedDict([
        ('foo', OrderedDict([('bar', 'baz')])),
    ])

    cfg = get_config(None, None, json.dumps({
        'foo': {'bar': 'baz'},
    }))
    assert cfg == {
        'foo': {'bar': 'baz'},
    }

    cfg = get_config(None, None, 'foo: bar: baz')

# Generated at 2022-06-14 06:27:16.743827
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger')
    with logger_level(logger, logging.WARNING):
        logger.info('test_logger_level')
    logger.info('test_logger_level')


# Generated at 2022-06-14 06:27:29.985137
# Unit test for function logger_level
def test_logger_level():
    import uuid
    from subprocess import *
    from tempfile import NamedTemporaryFile

    tmp = NamedTemporaryFile(prefix='test_logger_level', delete=False)
    tmpname = tmp.name
    tmp.close()

    conf = {}
    conf['version'] = 1
    conf['disable_existing_loggers'] = False

    conf['formatters'] = {}

# Generated at 2022-06-14 06:27:33.074595
# Unit test for function logger_level
def test_logger_level():
    import threading
    log = get_logger()
    threading.current_thread().name = 'main'
    with logger_level(log, logging.DEBUG):
        log.debug("log test")

# Generated at 2022-06-14 06:27:39.309404
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test')
    with logger_level(logger, logging.CRITICAL):
        assert logger.getEffectiveLevel() == logging.CRITICAL
        logger.info('test')

    assert logger.getEffectiveLevel() == logging.NOTSET
    logger.info('test')

# Generated at 2022-06-14 06:27:47.788507
# Unit test for function logger_level
def test_logger_level():
    from contextlib import redirect_stdout
    from io import StringIO
    log = get_logger()
    f = StringIO()
    with redirect_stdout(f):
        with logger_level(log, logging.CRITICAL):
            log.debug("Not going to appear in output!")
            print("But this will!")
        log.debug("Okay, this will appear in output.")
    output = f.getvalue()
    assert "Not going to appear in output!" not in output
    assert "But this will!" in output
    assert "Okay, this will appear in output." in output

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:27:56.430038
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    try:
        with logger_level(logger, logging.DEBUG):
            logger.debug('this is a DEBUG message')
        logger.critical('this is a CRITICAL message')
    except:
        logger.exception('test_logger_level failed')
        raise

# End of unit test for function logger_level

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:28:00.788644
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    configure()
    with logger_level(log, logging.DEBUG):
        assert log.isEnabledFor(logging.DEBUG)

    assert log.getEffectiveLevel() == logging.INFO

# Generated at 2022-06-14 06:28:04.254535
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    log.warning('Before')
    with logger_level(log, logging.ERROR):
        log.warning('Should not show up')
        log.error('Should show up')
    log.warning('Should show up again')


# Generated at 2022-06-14 06:28:08.814742
# Unit test for function logger_level
def test_logger_level():
    log = get_logger('logger_level')
    with logger_level(log, logging.ERROR):
        log.error("We should see this")
        log.debug("We should not see this")
    log.debug("We should see this")

# Generated at 2022-06-14 06:28:21.676725
# Unit test for function get_config
def test_get_config():
    # Test 1: Config is a string that looks like a dict
    config = '{"version": 1, "level": "DEBUG", "loggers": {"requests": {"level": "INFO"}}}'
    result = get_config("config", "LOGGING", None)
    assert result == {'version': 1, 'level': 'DEBUG', 'loggers': {'requests': {'level': 'INFO'}}}

    # Test 2: Config is a string that looks like a list
    config = "[1, 2, 3, 4]"
    result = get_config("config", "LOGGING", None)
    assert result == [1, 2, 3, 4]

    # Test 3: Config is a dict
    config = {'version': 1, 'level': 'DEBUG', 'loggers': {'requests': {'level': 'INFO'}}}

# Generated at 2022-06-14 06:28:37.065171
# Unit test for function get_config
def test_get_config():
    import json
    import yaml

    # Test bare config
    default_bare_cfg = DEFAULT_CONFIG

# Generated at 2022-06-14 06:28:43.242597
# Unit test for function logger_level
def test_logger_level():
    from contextlib import closing
    from . import logger

    with closing(logger.LoggerStdout()) as stderr_buffer:
        with logger_level(logger.get_logger(), logger.DEBUG):
            logger.get_logger().debug("This message won't print")
            logger.get_logger().info("This message will print")

    assert "This message will print" in stderr_buffer.contents()


# Generated at 2022-06-14 06:28:50.577865
# Unit test for function logger_level
def test_logger_level():
    import logging
    logging.basicConfig(format='%(message)s')
    main_logger = logging.getLogger(__name__)
    main_logger.setLevel(logging.DEBUG)
    main_logger.debug('main_debug')
    main_logger.info('main_info')
    main_logger.warning('main_warning')
    with logger_level(main_logger, logging.WARNING):
        main_logger.debug('main_debug')
        main_logger.info('main_info')
        main_logger.warning('main_warning')
    main_logger.debug('main_debug')
    main_logger.info('main_info')
    main_logger.warning('main_warning')

# __all__ = [
#     'DEFAULT_CON

# Generated at 2022-06-14 06:29:02.372449
# Unit test for function logger_level
def test_logger_level():
    import os
    import tempfile

    from . import _PyInfo

    logger = get_logger()

    with tempfile.NamedTemporaryFile(mode='w+') as tf:
        with logger_level(logger, 100):
            logger.info('aaa')

        with logger_level(logger, logging.INFO):
            logger.info('bbb')
            logger.error('ccc')

        logger.info('ddd')

        tf.flush()
        with open(tf.name) as f:
            contents = f.read()

        if _PyInfo.PY2:
            assert contents == 'INFO:test_logger:bbb\nERROR:test_logger:ccc\nINFO:test_logger:ddd\n'

# Generated at 2022-06-14 06:29:10.577336
# Unit test for function logger_level
def test_logger_level():
    with logger_level(get_logger(), logging.DEBUG):
        logger = get_logger()
        assert logger.level == logging.DEBUG
        logger.info("test")


__all__ = [
    "log",
    "configure",  # probably don't need to expose that
    "get_logger",
    "getLogger",  # for compat with logging stdlib
]


log = get_logger()

# Generated at 2022-06-14 06:29:15.529604
# Unit test for function get_config
def test_get_config():
    import pytest
    data = "Hello, World!"
    with pytest.raises(ValueError):
        get_config(config=data)
        get_config(env_var=data)

# Generated at 2022-06-14 06:29:18.415447
# Unit test for function get_config
def test_get_config():
    print(get_config())
    print(get_config(env_var="LOGGING"))
    print(get_config(default=DEFAULT_CONFIG))
    print(get_config(config=DEFAULT_CONFIG))



# Generated at 2022-06-14 06:29:31.017675
# Unit test for function logger_level
def test_logger_level():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    config = dict(version=1,
                  formatters={'default': {'format': '%(asctime)s %(levelname)s %(message)s'}},
                  handlers={'default': {'class': 'logging.StreamHandler',
                                        'formatter': 'default'},
                            'file': {'class': 'logging.FileHandler',
                                     'formatter': 'default'}
                           },
                  root={'level': 'INFO',
                        'handlers': ['default']
                       }
                 )
    logging.config.dictConfig(config)
    log = logging.getLogger(__name__)

# Generated at 2022-06-14 06:29:35.064510
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test_logger_level')
    initial = logger.level
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == initial


# Generated at 2022-06-14 06:29:43.387686
# Unit test for function get_config
def test_get_config():
    assert get_config() == DEFAULT_CONFIG
    assert get_config(default=None) == None
    assert get_config(config='{"test": "test_value"}') == {"test": "test_value"}
    assert get_config(config='{"test": "test_value"}', default=None) == {"test": "test_value"}
    assert get_config(config='{"test": "test_value"}', default=DEFAULT_CONFIG) == {"test": "test_value"}

# Generated at 2022-06-14 06:29:50.284386
# Unit test for function get_config
def test_get_config():
    config_test = "this is a test"
    config_test_yaml = "{test: 1}"

    config = get_config(config_test)
    assert config == "this is a test"

    config = get_config(config_test_yaml)
    assert config == {"test": 1}

# Generated at 2022-06-14 06:29:59.721026
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    try:
        with logger_level(log, logging.CRITICAL):
            log.debug('This should not be printed')
    except Exception:
        # Todo: improve this unit test for logger_level
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    from . import test_logger_level
    print(test_logger_level())

# Generated at 2022-06-14 06:30:12.912910
# Unit test for function configure
def test_configure():
    import logging
    import logging.handlers
    from contextlib import contextmanager
    from tempfile import NamedTemporaryFile
    import os

    logfname = '.log'

    def clear_log():
        if os.path.exists(logfname):
            os.unlink(logfname)

    def assert_log_file_contents(expected):
        with open(logfname, 'r') as logf:
            actual = logf.read()
            assert actual.startswith(expected)

    def assert_logger_config(logger, expected_level):
        level = {10: 'DEBUG', 20: 'INFO', 30: 'WARNING', 40: 'ERROR', 50: 'CRITICAL'}[expected_level]
        assert logger.level == expected_level
        assert logger.getEffectiveLevel() == expected

# Generated at 2022-06-14 06:30:22.357040
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger()
    with logger_level(logger, logging.DEBUG):
        logger.debug("This is a test for logger_level")
    with logger_level(logger, logging.INFO):
        logger.info("This is a test for logger_level")
    try:
        with logger_level(logger, logging.DEBUG):
            raise ValueError("This is a test for logger_level")
    except ValueError:
        logger.info("This is a test for logger_level")

if __name__ == '__main__':
    try:
        test_logger_level()
    except ValueError as e:
        print(e)



# Generated at 2022-06-14 06:30:34.167208
# Unit test for function configure
def test_configure():
    import tempfile


# Generated at 2022-06-14 06:30:41.774609
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig()
    logger = logging.getLogger('logger_level')
    logger.warn('first log')
    with logger_level(logger, logging.WARN):
        try:
            raise Exception('boom')
        except:
            logger.exception('exception log')
    logger.warn('last log')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:46.361738
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    assert l.level == logging.DEBUG
    with logger_level(l, logging.WARNING):
        assert l.level == logging.WARNING
    assert l.level == logging.DEBUG

# Generated at 2022-06-14 06:30:50.857654
# Unit test for function get_config
def test_get_config():
    cfg = get_config(config="{'version': 1}")
    assert(cfg == {'version': 1})

    cfg = get_config(config="version: 1\n")
    assert(cfg == {'version': 1})

    cfg = get_config(config="  version:\n  1\n")
    assert(cfg == {'version': 1})

# Generated at 2022-06-14 06:30:54.107793
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:30:59.720320
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    try:
        with logger_level(log, logging.DEBUG):
            log.critical('critical message')
            log.error('error message')
            log.warning('warning message')
            log.info('info message')
            log.debug('debug message')
    except:
        return False
    return True

# Generated at 2022-06-14 06:31:08.533193
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__+'test_logger_level')
    with logger_level(log, logging.DEBUG):
        log.debug("This should be visible")
        log.info("This should not be visible")
    log.info("This should be visible again")



# Generated at 2022-06-14 06:31:12.893843
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.DEBUG):
        logger.debug('I am inside the context block.')
    logger.debug('I am outside the context block.')

# Generated at 2022-06-14 06:31:19.041798
# Unit test for function logger_level
def test_logger_level():
    from .log import get_logger
    from .log import logger_level
    from .log import configure
    logger = get_logger()
    configure()

    with logger_level(logger, 60):
        logger.error('should be suppressed')

    with logger_level(logger, 0):
        logger.error('should be logged')


# Generated at 2022-06-14 06:31:31.630816
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig()
    testlogger = logging.getLogger('test')

    class TestObject(object):
        def __init__(self):
            self.logger = logging.getLogger('test')

        def log(self, *args):
            self.logger.debug(*args)

        def log_test(self, foo):
            with logger_level(self.logger, logging.DEBUG):
                self.log(foo, os.getpid())

    testobj = TestObject()
    testobj.log_test(1)
    testobj.log_test(2)
    testobj.log_test(3)
    assert sys.stdout.getvalue().split('\n')[-2] == 'DEBUG:test:2 <%i>' % os.getpid()
    assert sys.stdout

# Generated at 2022-06-14 06:31:35.453667
# Unit test for function logger_level
def test_logger_level():
    l = get_logger(__name__)
    with logger_level(l, logging.INFO):
        assert(l.level == logging.INFO)
        l.info('hi')
    assert(l.level == logging.DEBUG)
    l.info('hi')

# Generated at 2022-06-14 06:31:44.244158
# Unit test for function get_config
def test_get_config():
    # Testing for none of the parameters
    assert get_config() == DEFAULT_CONFIG

    # Testing for only LOGGING env var

# Generated at 2022-06-14 06:31:53.646083
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    logger.info('test_logger_level')

    with logger_level(logger, logging.DEBUG):
        logger.debug('logging.DEBUG')
        logger.info('logging.INFO')
        logger.warning('logging.WARNING')
    logger.debug('logging.DEBUG')
    logger.info('logging.INFO')
    logger.warning('logging.WARNING')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:32:02.109423
# Unit test for function logger_level
def test_logger_level():
    from nose.tools import assert_equal
    import logging
    import random
    import time

    random.seed(42)

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    # Test that behavior is preserved with no context manager
    for level in [logging.DEBUG, logging.INFO, logging.WARNING]:
        log.setLevel(level)
        log.debug("this should print")
    log.setLevel(logging.DEBUG)
    log.info("this should print")
    log.warning("this should print")

    prev_debug_msg = "this should print"

# Generated at 2022-06-14 06:32:09.331686
# Unit test for function logger_level
def test_logger_level():
    # Test Logger
    log = get_logger()

    # Test Levels
    log.setLevel(logging.WARNING)
    # Test a warning
    log.warning("Warning outside of context")

    new_level = logging.DEBUG

    with logger_level(log, new_level):
        # Test a warning
        log.warning("Warning during context")
        # Test a debug
        log.debug("Debug during context")

    # Test a warning
    log.warning("Warning outside of context")
    # Test a debug
    log.debug("Debug outside of context")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:32:16.653702
# Unit test for function get_config
def test_get_config():
        # test default (json)
        assert get_config({'a': 'b'}) == {'a': 'b'}
        assert get_config(json.dumps({'a': 'b'})) == {'a': 'b'}
        assert get_config(json.dumps({'a': 'b'})) == {'a': 'b'}
        # test yaml
        #assert get_config('a: b') == {'a': 'b'}
        #assert get_config('a: b') == {'a': 'b'}
    #    # test bare string
    #    assert get_config('foo') == 'foo'
    #    # test None
    #    assert get_config(None) is None
    #    # test env_var
    #    assert get_config(env_

# Generated at 2022-06-14 06:32:37.238999
# Unit test for function logger_level
def test_logger_level():
    import pytest
    from textwrap import dedent
    from io import StringIO
    from contextlib import redirect_stderr
    import logging

    buf = StringIO()

    logger = logging.getLogger(__name__)

    # Capture stdout with pytest
    with pytest.raises(AssertionError, match="^'foo' == 'bar'$"):
        with logger_level(logger, logging.INFO):
            with redirect_stderr(buf):
                try:
                    assert "foo" == "bar"
                except AssertionError:
                    logger.exception("error")
                    raise


# Generated at 2022-06-14 06:32:47.316488
# Unit test for function get_config
def test_get_config():
    assert DEFAULT_CONFIG == get_config('','','DEFAULT_CONFIG')

# Generated at 2022-06-14 06:32:53.706190
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger("test_logger_level")
    logger.info("Before level change")
    with logger_level(logger, logging.CRITICAL):
        logger.info("Within level change")
    logger.info("After level change")



# Generated at 2022-06-14 06:32:55.533697
# Unit test for function configure
def test_configure():
    configure(default=None)


if __name__ == '__main__':
    test_configure()

# Generated at 2022-06-14 06:33:00.428349
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    configure()
    with logger_level(log, logging.INFO):
        log.setLevel(logging.DEBUG)
        assert log.level == logging.INFO
    assert log.level == logging.DEBUG

# Generated at 2022-06-14 06:33:05.045159
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger('test_logger_level')
    with logger_level(logger, level=logging.ERROR):
        assert logger.level == logging.ERROR
        logger.info('Should never see this!')
    assert logger.level == logging.DEBUG  # If the log level is not reset to the original
    logger.info('Should see this')


# Generated at 2022-06-14 06:33:17.104819
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    # For some reason, this logger doesn't send messages to the console
    # without a dedicated handler.
    logger.addHandler(logging.StreamHandler())
    # Shouldn't log
    with logger_level(logger, logging.ERROR):
        logger.info("Shouldn't log")
    # Should log
    with logger_level(logger, logging.INFO):
        logger.info("Should log")
    # Shouldn't log
    logger.info("Shouldn't log")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:33:31.248542
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    from contextlib import closing
    from io import StringIO
    from . import get_logger

    def simple_factory(logger):
        """
        A simple factory function that will be wrapped by a context manager
        returning an object that will have its own logging functionality
        enabled.
        """
        class _Simple(object):
            def __init__(self):
                self.my_logger = logger.getChild('my_logger')

            def my_func(self):
                self.my_logger.info('Test message')

        return _Simple()

    def my_func():
        """
        A function to be decorated with the logger_level context manager.
        """
        logger.info('Test message')


# Generated at 2022-06-14 06:33:39.719959
# Unit test for function get_config

# Generated at 2022-06-14 06:33:52.404927
# Unit test for function get_config

# Generated at 2022-06-14 06:34:08.103136
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger("test_logger")
    with logger_level(logger, logging.DEBUG):
        logger.debug("test")
    with logger_level(logger, logging.WARNING):
        logger.warning("test")


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:34:11.296618
# Unit test for function logger_level
def test_logger_level():
    """
    >>> logger = logging.getLogger('test')
    >>> logger.info('before')
    >>> with logger_level(logger, logging.DEBUG):
    ...     logger.debug('debug mode')
    >>> logger.info('after')
    """
    pass



# Generated at 2022-06-14 06:34:25.283419
# Unit test for function logger_level
def test_logger_level():
    import logging
    import shutil
    import tempfile

    test_directory = tempfile.mkdtemp()
    test_log_filename = os.path.join(test_directory, 'test_log.log')

    cfg = DEFAULT_CONFIG.copy()
    cfg['root']['level'] = logging.WARNING
    cfg['handlers'].update({'test': {'class': 'logging.FileHandler', 'filename': test_log_filename, 'formatter': 'colored'}})
    cfg['root']['handlers'].append('test')
    configure(cfg)

    test_logger = get_logger('test_logger')
    test_logger.info('test_logger.info')
    test_logger.warning('test_logger.warning')

    # Test the

# Generated at 2022-06-14 06:34:35.927722
# Unit test for function logger_level
def test_logger_level():
  import logging
  import random
  LEVELS = sorted([logging.getLevelName(lvl) for lvl in logging._levelNames.values() if isinstance(lvl, int)])
  msg = "Special Message"
  logger = logging.getLogger(__name__)
  with logger_level(logger, logging.ERROR):
    for level in LEVELS:
      logger.log(level, msg)
      assert "Special Message" not in caplog.text
  random.shuffle(LEVELS)
  for level in LEVELS:
    logger.log(level, msg)
    assert "Special Message" in caplog.text

# Generated at 2022-06-14 06:34:41.228576
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    log = get_logger('test_logger_level')
    assert log.isEnabledFor(logging.INFO)
    with logger_level(log, logging.ERROR):
        assert not log.isEnabledFor(logging.INFO)
    assert log.isEnabledFor(logging.INFO)

if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:34:45.128573
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.ERROR):
        log.info('this should not print')
    log.info('but this should')



# Generated at 2022-06-14 06:34:51.519180
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.CRITICAL):
        assert logger.getEffectiveLevel() == logging.CRITICAL
    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
    assert logger.getEffectiveLevel() == logging.DEBUG  # original level



# Generated at 2022-06-14 06:35:02.065520
# Unit test for function logger_level
def test_logger_level():
    import logging
    import mock

    logger = logging.getLogger()

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    with mock.patch('logging.Logger.setLevel') as setLevel:
        with logger_level(logger, logging.INFO):
            assert setLevel.called

    with mock.patch('logging.Logger.setLevel') as setLevel:
        logger.level = logging.INFO
        with logger_level(logger, logging.INFO):
            assert not setLevel.called

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:35:04.558093
# Unit test for function configure
def test_configure():
    configure()
    log = get_logger()
    log.info('test')


# Generated at 2022-06-14 06:35:10.608431
# Unit test for function get_config
def test_get_config():
    # invalid
    with pytest.raises(ValueError):
        get_config()

    # string
    assert get_config('{"a": 1}')['a'] == 1
    assert get_config('{"a": 1')['a'] == 1
    assert get_config('{"a": 1}\n')['a'] == 1
    assert get_config('a: 1')['a'] == 1
    assert get_config('a: 1\n')['a'] == 1

    # dict
    assert get_config({'a': 1})['a'] == 1

    # None
    assert get_config(None) is None
    assert get_config(config=None, default={'a': 1})['a'] == 1

