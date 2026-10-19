

# Generated at 2022-06-14 06:25:11.743529
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        # log.debug('debug')
        log.info('info')


# Generated at 2022-06-14 06:25:21.702270
# Unit test for function logger_level
def test_logger_level():
    # Reset the logging configuration to an empty config
    logging.config.dictConfig(DEFAULT_CONFIG)

    # Set up a logger to log at DEBUG
    logger = get_logger(__name__)

    # Set up a handler to capture the log records and verify them
    handler = logging.NullHandler()
    logger.addHandler(handler)

    # Verify that a log at INFO does not go through the handler
    with logger_level(logger, logging.INFO):
        logger.info("Test")
        assert len(handler.records) == 0

    # Verify that a log at DEBUG does go through the handler
    with logger_level(logger, logging.DEBUG):
        logger.info("Test")
        assert len(handler.records) == 1
        assert handler.records[-1].levelname == "INFO"


# Generated at 2022-06-14 06:25:27.960226
# Unit test for function logger_level
def test_logger_level():
    import time
    import random
    import logging
    import multiprocessing
    import threading

    def _test_level(logger, level, record_count):
        with logger_level(logger, level):
            for i in range(record_count):
                logger.debug("This is a debug message %d", i)
                logger.info("This is an info message %d", i)
                logger.warning("This is a warning message %d", i)
                logger.error("This is an error message %d", i)
                logger.critical("This is a critical message %d", i)
                time.sleep(random.random())
        return i


    def _worker_func(q, name, level, record_count):
        logger = get_logger(name)

# Generated at 2022-06-14 06:25:33.780528
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARN):
        assert logger.level == logging.WARN
        logger.debug('logger.debug')
        logger.info('logger.info')
    assert logger.level == logging.DEBUG
    logger.debug('logger.debug')
    logger.info('logger.info')



# Generated at 2022-06-14 06:25:46.377623
# Unit test for function logger_level
def test_logger_level():
    import logging
    import sys


# Generated at 2022-06-14 06:25:56.709713
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.info("before setting loglevel")
    with logger_level(logger, logging.INFO):
        logger.debug("debug enabled")
        with logger_level(logger, logging.DEBUG):
            logger.debug("debug enabled")
        logger.debug("debug disabled")

if __name__ == '__main__':
    # Only run when this module is run directly, not when it's imported
    test_logger_level()

try:
    import json
except ImportError:
    import simplejson as json

try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except ImportError:
    from urllib3.exceptions import InsecureRequestWarning

import requests

requests.packages.urllib3.disable_warn

# Generated at 2022-06-14 06:26:02.941172
# Unit test for function logger_level
def test_logger_level():
    log = getLogger(__name__)
    log.setLevel(logging.INFO)
    log.info("Logging at INFO level")
    with logger_level(log, logging.DEBUG):
        log.info("Logging at DEBUG level")
    log.info("Logging back at INFO level")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:11.246046
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)

    test_msg = 'TEST'

    logger.info(test_msg) # This should appear
    with logger_level(logger, logging.CRITICAL):
        logger.info(test_msg)  # This should not!
    logger.info(test_msg) # This should again




# Unit tests for function configure
if __name__ == "__main__":
    test_logger_level()

# Generated at 2022-06-14 06:26:17.723109
# Unit test for function logger_level
def test_logger_level():
    test_logger = logging.getLogger('test_logger_level')
    with logger_level(test_logger, 0):
        # DoLogging
        test_logger.debug('Test logger level')
    # DoLogging
    test_logger.debug('Test logger level')

# Generated at 2022-06-14 06:26:19.683736
# Unit test for function configure
def test_configure():
    import logging
    configure()
    logging.debug('test debug')


# Generated at 2022-06-14 06:26:30.482614
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.debug('test message')
        assert logger.level == logging.DEBUG
    logger.debug('should not be displayed')

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:26:34.277118
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger("test.logger")
    logger.debug("First")
    with logger_level(logger, logging.DEBUG):
        logger.debug("Debug")
    logger.debug("First")

# Generated at 2022-06-14 06:26:38.961271
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger('test')
    log.setLevel(logging.CRITICAL)
    assert log.level == logging.CRITICAL
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level == logging.CRITICAL

# Generated at 2022-06-14 06:26:43.561994
# Unit test for function logger_level
def test_logger_level():
    log = getLogger()

    with logger_level(log, logging.CRITICAL):
        log.info('OOPS!')
        log.debug('X')

    log.info('ok')

# Generated at 2022-06-14 06:26:48.291191
# Unit test for function logger_level
def test_logger_level():
    # Test logger_level with DEBUG level
    logger = get_logger(__name__)
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG

test_logger_level()

# Generated at 2022-06-14 06:26:52.651183
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.WARN):
        logger.info("This should not be seen")
        logger.warn("This should be seen")
    logger.debug("This should also be seen")


# Generated at 2022-06-14 06:26:58.540614
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.DEBUG)
    with logger_level(logger, logging.ERROR):
        logger.debug("debug message should not be output")
        logger.error("error message should be output")
    logger.debug("debug message should be output")

# Generated at 2022-06-14 06:27:05.897021
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = get_logger(__name__)
    >>> with logger_level(log, logging.INFO):
    ...     log.info("This is at level INFO")
    ...     log.debug("This is at level DEBUG, but not printed")
    >>> log.info("Back to initial level")
    ... 
    """

if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:27:12.918146
# Unit test for function logger_level
def test_logger_level():
    logger = getLogger(__name__)

    # Test that logger_level is working
    with logger_level(logger, logging.DEBUG):
        assert logger.getEffectiveLevel() == logging.DEBUG
        logger.debug("Starting logger level test")
    assert logger.getEffectiveLevel() == logging.NOTSET
    logger.debug("Ending logger level test")

# Generated at 2022-06-14 06:27:21.647719
# Unit test for function logger_level
def test_logger_level():
    logging.getLogger().handlers[0].setLevel(logging.ERROR)
    logger = get_logger()
    # Not equal to handler level
    assert logger.level != logging.ERROR
    # Set logger level to logging.ERROR inside the context
    with logger_level(logger, logging.ERROR):
        # Equal to handler level
        assert logger.level == logging.ERROR
    # Not equal to handler level
    assert logger.level != logging.ERROR

# Generated at 2022-06-14 06:27:33.038269
# Unit test for function logger_level
def test_logger_level():
    l = logging.getLogger()
    logger_level(l, logging.WARNING)
    assert l.level == logging.WARNING

# Make the module importable in python2
sys.modules[__name__] = sys.modules[__name__ + str(sys.version_info[0])]

# Generated at 2022-06-14 06:27:46.369519
# Unit test for function logger_level
def test_logger_level():
    import logging

    log = logging.getLogger(__name__)

    # test it works
    with logger_level(log, logging.DEBUG):
        log.debug('debug msg')
        log.info('info msg')
        log.warn('warn msg')
        log.error('error msg')
        log.critical('critical msg')

    # test it doesn't work
    with logger_level(log, logging.ERROR):
        log.debug('debug msg')
        log.info('info msg')
        log.warn('warn msg')
        log.error('error msg')
        log.critical('critical msg')
        assert True



# Generated at 2022-06-14 06:27:54.357772
# Unit test for function get_config

# Generated at 2022-06-14 06:27:59.970700
# Unit test for function logger_level
def test_logger_level():
    import logging
    logger = logging.getLogger(__name__)
    with logger_level(logger, logging.DEBUG):
        logger.info('debugging')
        with logger_level(logger, logging.INFO):
            logger.info('debugging again')
        logger.info('debugging')
    logger.info('not debugging')

# Generated at 2022-06-14 06:28:05.989175
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    logger.setLevel(logging.INFO)

    with logger_level(logger, logging.CRITICAL):
        assert logger.level == logging.CRITICAL
        logger.debug('this should not appear in logs')
        logger.critical('this should appear in logs')
    assert logger.level == logging.INFO
    logger.debug('this should appear in logs')



# Generated at 2022-06-14 06:28:19.545494
# Unit test for function get_config
def test_get_config():
    config = get_config(config=None, env_var=None, default=None)
    assert config is None
    config = get_config(config=None, env_var='LOGGING', default=None)
    assert config is None
    config = get_config(config='foo', env_var=None, default=None)
    assert config == 'foo'
    config = get_config(config='foo', env_var='LOGGING', default=None)
    assert config == 'foo'
    config = get_config(config='', env_var='LOGGING', default=None)
    assert config == ''
    config = get_config(config=None, env_var=None, default=DEFAULT_CONFIG)
    assert config == DEFAULT_CONFIG

    with pytest.raises(ValueError):
        config

# Generated at 2022-06-14 06:28:29.665880
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    logger.debug("test_debug")
    logger.info("test_info")
    with logger_level(logger, logging.INFO):
        logger.debug("test_debug")
        logger.info("test_info")
    logger.debug("test_debug")


# Generated at 2022-06-14 06:28:30.911747
# Unit test for function configure
def test_configure():
    configure(default=DEFAULT_CONFIG)
    logger = get_logger()
    logger.info('test')

# Generated at 2022-06-14 06:28:38.066051
# Unit test for function logger_level
def test_logger_level():
    my_logger = get_logger(__name__)
    my_logger.debug('starts at level DEBUG')
    with logger_level(my_logger, logging.INFO):
        my_logger.debug('no log for INFO')
        my_logger.info('logging at INFO level')
    my_logger.debug('resuming at level DEBUG')



# Generated at 2022-06-14 06:28:45.706442
# Unit test for function get_config
def test_get_config():
    # json config
    json_cfg = '{"version": 1, "root": { "level": "DEBUG", "handlers": ["console"] } }'
    assert get_config(json_cfg) == {"version": 1, "root": { "level": "DEBUG", "handlers": ["console"] }}
    # yaml config
    yaml_cfg = """version: 1
                  root:
                    level: DEBUG
                    handlers: ["console"]"""
    assert get_config(yaml_cfg) == {"version": 1, "root": { "level": "DEBUG", "handlers": ["console"] }}

# Generated at 2022-06-14 06:29:04.287751
# Unit test for function logger_level

# Generated at 2022-06-14 06:29:16.956494
# Unit test for function get_config
def test_get_config():
    # Case1: the input config is bare string
    config = 'LOGGING=root:DEBUG'

    cfg = get_config(config)

    assert(cfg['handlers']['console']['level'] == 10)

    # Case2: the input config is json string
    config = """{"handlers": {"console": {"class": "logging.StreamHandler", "formatter": "colored", "level": 10}}}"""

    cfg = get_config(config)

    assert(cfg['handlers']['console']['level'] == 10)

    # Case3: the input config is yaml string
    config = """
handlers:
  console:
    class: logging.StreamHandler
    formatter: colored
    level: 10
    """

    cfg = get_config(config)


# Generated at 2022-06-14 06:29:22.428855
# Unit test for function get_config
def test_get_config():
    with open("logging.yaml", 'r') as f:
        data = f.read()
    cfg = get_config(config=data, env_var=None, default=None)
    assert isinstance(cfg, dict)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(name)s#%(funcName)s:%(lineno)d[%(levelname)s] %(message)s', datefmt='%H:%M:%S')
    log = get_logger(__name__)
    log.debug('test debug')
    log.info('test info')

# Generated at 2022-06-14 06:29:26.409157
# Unit test for function logger_level
def test_logger_level():
    """
    >>> log = getLogger(__name__)
    >>> with logger_level(log, logging.DEBUG):
    ...   log.debug('test')
    ...
    DEBUG:__main__:test
    """

    pass



# Generated at 2022-06-14 06:29:38.195402
# Unit test for function logger_level
def test_logger_level():

    # create logger and set it to DEBUG, which is lower than INFO
    logger = get_logger(__name__)
    assert logger.level == logging.DEBUG

    # assert that debug calls go through, but info and warning calls do not
    with logger_level(logger, logging.INFO):
        logger.debug("This is a debug message")
        assert logger.isEnabledFor(logging.DEBUG) == False
        logger.info("This is an info message")
        assert logger.isEnabledFor(logging.INFO) == True
        logger.warning("This is a warning message")
        assert logger.isEnabledFor(logging.WARNING) == True
    assert logger.level == logging.DEBUG

    # assert that we can't log anything at CRITICAL

# Generated at 2022-06-14 06:29:49.415926
# Unit test for function logger_level
def test_logger_level():
    import unittest
    class LevelTester(unittest.TestCase):
        def test_logger_level(self):
            """
            Set logger level to `DEBUG` within a context block.
            Run the test function inside the context and ensure that
            the logger level is set back to `ERROR` on exiting the context
            """
            final_level = logging.ERROR
            logger = logging.getLogger()
            self.assertNotEqual(logger.level, final_level)
            with logger_level(logger, logging.DEBUG):
                self.assertEqual(logger.level, logging.DEBUG)
            self.assertEqual(logger.level, final_level)
    unittest.main(exit=False, argv=['not a file'])

# Generated at 2022-06-14 06:30:02.575757
# Unit test for function logger_level
def test_logger_level():
    # Create a regular logger
    import sys
    import logging
    logger = logging.getLogger("test_logger_level")
    logger.setLevel(logging.WARNING)
    # Create a console handler
    ch = logging.StreamHandler(stream=sys.stdout)
    # Create a formatter
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    # Add formatter to ch
    ch.setFormatter(formatter)
    # Add ch to logger
    logger.addHandler(ch)

    # Indicate that we're inside the context manager with a message at debug level
    with logger_level(logger, logging.DEBUG):
        logger.debug("This message is at debug level")
        assert logger.level == logging.DEBUG
        logger.info("This message is at info level")

# Generated at 2022-06-14 06:30:15.856210
# Unit test for function get_config
def test_get_config():
    import json
    import yaml
    import textwrap

    logging_config_json_str = '{"foo": "bar"}'
    logging_config_yaml_str = textwrap.dedent('''\
    foo: bar
    ''')
    logging_config_dict = {'foo': 'bar'}

    assert get_config(logging_config_json_str) == json.loads(logging_config_json_str)
    assert get_config(logging_config_yaml_str) == yaml.load(logging_config_yaml_str)
    assert get_config(logging_config_dict) == logging_config_dict
    assert get_config('') == {}
    assert get_config(None) == {}


if __name__ == '__main__':
    configure()


# Generated at 2022-06-14 06:30:19.749149
# Unit test for function logger_level
def test_logger_level():
    l = get_logger()
    with logger_level(l, logging.WARNING):
        l.debug("debug should not print")
        l.info("info should not print")
        l.warning("warning should print")



# Generated at 2022-06-14 06:30:25.787932
# Unit test for function logger_level
def test_logger_level():
    logging.basicConfig(level=logging.DEBUG)
    l = logging.getLogger('test')
    l.warning('OK')
    l.debug('No op')
    with logger_level(l, logging.DEBUG):
        l.debug('OK')
    l.debug('No op')



# Generated at 2022-06-14 06:30:36.283846
# Unit test for function configure
def test_configure():
    configure(default=DEFAULT_CONFIG)



# Generated at 2022-06-14 06:30:46.420329
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    assert logger.getEffectiveLevel() == 0
    assert logger.isEnabledFor(20) == True
    with logger_level(logger, 20):
        assert logger.isEnabledFor(20) == True
        with logger_level(logger, 30):
            assert logger.isEnabledFor(20) == False
        assert logger.isEnabledFor(20) == True
    assert logger.isEnabledFor(20) == True

_LOGGER = getLogger(__name__)



# Generated at 2022-06-14 06:30:50.660224
# Unit test for function logger_level
def test_logger_level():
    log = get_logger()
    with logger_level(log, logging.DEBUG):
        log.debug("debug")
        log.info("info")
        log.warning("warning")
        log.error("error")
        log.critical("critical")

if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:30:54.143954
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__)
    with logger_level(log, logging.DEBUG):
        log.debug("Level at DEBUG")
    log.info("Level once again at INFO")



# Generated at 2022-06-14 06:31:05.130756
# Unit test for function logger_level
def test_logger_level():
    import tempfile
    filename = tempfile.mktemp()
    with open(filename, 'w') as logfile:
        logger = logging.getLogger(__name__)
        # Initial logging level is WARNING
        logger.addHandler(logging.StreamHandler(logfile))
        logger.info("This should NOT get logged.")
        logger.warning("This should get logged.")
        with logger_level(logger, logging.INFO):
            logger.info("This should get logged.")
        logger.warning("This should get logged.")

    # Check that only the expected lines were logged.
    with open(filename, 'r') as logfile:
        loglines = logfile.readlines()
        assert len(loglines) == 2, "Wrong number of log entries"

# Generated at 2022-06-14 06:31:16.160542
# Unit test for function logger_level
def test_logger_level():
    import unittest
    class LoggerLevelTest(unittest.TestCase):
        def test_logger_level_01(self):
            logger = get_logger('test_logger_level')
            logger.setLevel(logging.INFO)

            log_level_debug_msg = []
            log_level_info_msg = []
            log_level_warning_msg = []
            log_level_error_msg = []

            # test default log level is INFO
            with logger_level(logger, logging.DEBUG):
                logger.debug("this is a DEBUG message")
                logger.info("this is an INFO message")
                logger.warning("this is a WARNING message")
                logger.error("this is an ERROR message")


# Generated at 2022-06-14 06:31:25.528257
# Unit test for function configure
def test_configure():
    import unittest
    import tempfile

    class TestConfigure(unittest.TestCase):
        def test_configure(self):
            self.assertRaises(
                ValueError, configure,
            )

            with tempfile.NamedTemporaryFile(mode='w') as f:
                cfg = {'handlers': {'console': {'level': logging.WARN}}}
                json.dump(cfg, f)
                f.flush()
                log = get_logger()
                configure(f.name)
                log.info('test')

    unittest.main(module=__name__)

# Generated at 2022-06-14 06:31:32.466444
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger("test")
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR
        logger.info("FAIL")
        logger.error("PASS")
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
        logger.info("PASS")
        logger.error("PASS")
    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:31:35.700909
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(logger, logging.INFO):
        assert (logger.level == logging.INFO)
    assert (logger.level == logging.DEBUG)

# Generated at 2022-06-14 06:31:39.054819
# Unit test for function get_config
def test_get_config():
    config = get_config(DEFAULT_CONFIG)
    assert config['version'] == 1



# Generated at 2022-06-14 06:31:54.540813
# Unit test for function logger_level
def test_logger_level():
    log = get_logger(__name__).getChild("test_logger_level")

    initial = log.level
    with logger_level(log, logging.CRITICAL):
        log.info("This should not have been logged")
        log.critical("This should have been logged")
    log.critical("This should have been logged") # Change back to initial

    assert(initial==logging.DEBUG)

# Generated at 2022-06-14 06:31:59.800689
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger()
    with logger_level(log, logging.DEBUG):
        assert log.isEnabledFor(logging.DEBUG) is True
    assert log.level == logging.DEBUG
    log.info("info level log")
    log.debug("debug level log")
    with logger_level(log, logging.INFO):
        log.info("info level log")
        log.debug("debug level log")
# End Unit test for function logger_level

# Generated at 2022-06-14 06:32:09.335729
# Unit test for function get_config
def test_get_config():
    assert get_config(default="another_value") == "another_value"
    assert get_config(default={"foo": "bar"}) == {"foo": "bar"}

    env_var = "FOO"
    os.environ[env_var] = "bar"
    assert get_config(env_var=env_var) == "bar"
    del os.environ[env_var]

    logger = get_logger(__name__)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("testing get_config, json should succeed")

# Generated at 2022-06-14 06:32:13.698336
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    configure()
    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.info('info')
    log.debug('debug')  # this should not print
    log.info('info')


if __name__ == '__main__':
    test_logger_level()

# Generated at 2022-06-14 06:32:23.085090
# Unit test for function logger_level
def test_logger_level():
    global log
    log = getLogger()
    try:
        with logger_level(log, logging.INFO):
            log.debug("This line does not print")
            log.info("This line does print")
    except:
        raise AssertionError("Expect DEBUG line to not print")
    log.debug("This line does print")

if __name__ == '__main__':
    test_logger_level()

# vim:et:sw=4:ts=4:sts=4

# Generated at 2022-06-14 06:32:34.377621
# Unit test for function logger_level
def test_logger_level():
    # Create logger
    log = get_logger(__name__)
    # Set up context manager
    cm = logger_level(log, logging.DEBUG)
    for i in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        try:
            with cm:
                log.setLevel(i)
                log.debug("---------------------")
                log.debug("This log message should work")
                log.info("This info message should work")
                log.warning("This warning message should work")
                log.error("This error message should work")
                log.critical("This critical message should work")
        except:
            return False
    return True



# Generated at 2022-06-14 06:32:40.166072
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('logger_level')
    logger.setLevel(logging.Debug)

    assert logger.level == logging.DEBUG

    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO

    assert logger.level == logging.DEBUG

# Generated at 2022-06-14 06:32:47.741626
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger()
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.INFO):
        assert logger.level == logging.INFO
    assert logger.level == logging.DEBUG
    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG



# Generated at 2022-06-14 06:33:02.288751
# Unit test for function configure
def test_configure():
    from io import StringIO
    from functools import partial
    from contextlib import contextmanager

    @contextmanager
    def redirect_stdout(callback):
        old_stdout = sys.stdout

        try:
            sys.stdout = StringIO()
            yield
            callback(sys.stdout.getvalue())
        finally:
            sys.stdout = old_stdout

    log = logging.getLogger('test')

    def cb1(stdout):
        print(stdout)
        assert stdout.startswith('\x1b[30m\x1b[42m'), 'Unexpected color format: %r' % stdout

    with redirect_stdout(cb1):
        configure()
        log.info('test')

    def cb2(stdout):
        print(stdout)


# Generated at 2022-06-14 06:33:05.870270
# Unit test for function logger_level
def test_logger_level():
    logger = logging.getLogger('test')
    init_level = logger.level

    with logger_level(logger, logging.INFO):
        assert(logger.level == logging.INFO)
        assert(init_level == logger.level)
    assert(logger.level == init_level)



# Generated at 2022-06-14 06:33:23.532040
# Unit test for function get_config
def test_get_config():
    def _test_get_config(test_given_config, test_env_var, test_default_config, expected_config):
        print("\n")
        if expected_config == None:
            print("Testing with given config: %s in environment variable: %s and default config: %s\nExpecting ValueError exception to be raised" % (test_given_config, test_env_var, test_default_config))
            try:
                # Test function and expect ValueError exception
                result = get_config(test_given_config, test_env_var, test_default_config)
            except ValueError as err:
                print("Exception as expected, Test passed")


# Generated at 2022-06-14 06:33:30.588587
# Unit test for function logger_level
def test_logger_level():
    # arrange
    with patch('logging.Logger') as LoggerMock:
        with patch('logging.getLogger') as getLoggerMock:
            with patch('logging.disable') as disableMock:
                logger = MagicMock()
                getLoggerMock.return_value = logger
                # act
                with logger_level(logger, logging.DEBUG):
                    # assert
                    assert(logger.level == logging.DEBUG)




# Generated at 2022-06-14 06:33:35.640231
# Unit test for function get_config
def test_get_config():
    assert get_config("{'version':1}") == {'version':1}
    assert get_config("%7B'version'%3A1%7D") == {'version':1}


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:33:45.233864
# Unit test for function logger_level
def test_logger_level():
    import StringIO
    import logging

    log = logging.getLogger('test')
    log.setLevel(logging.WARNING)

    io = StringIO.StringIO()
    handler = logging.StreamHandler(io)
    log.addHandler(handler)

    with logger_level(log, logging.DEBUG):
        log.debug('debug')
        log.warning('warning')

    assert io.getvalue() == 'DEBUG:test:debug\nWARNING:test:warning\n'



# Generated at 2022-06-14 06:33:49.251599
# Unit test for function logger_level
def test_logger_level():
    log = logging.getLogger(__name__)
    log.debug('Hello!')  # should print message
    with logger_level(log, logging.INFO):
        log.debug('Hello!')  # should not print message

# Generated at 2022-06-14 06:33:54.038018
# Unit test for function configure
def test_configure():
    """Tests that logging is configured by configure()"""
    configure()

    root_logger = logging.getLogger()

    assert len(root_logger.handlers) == 1
    assert root_logger.handlers[0].level == logging.DEBUG



# Generated at 2022-06-14 06:34:07.195616
# Unit test for function get_config

# Generated at 2022-06-14 06:34:13.762937
# Unit test for function logger_level
def test_logger_level():
    import logging
    import tempfile
    with tempfile.TemporaryFile() as f:
        log = logging.getLogger('test_logger_level')
        log.setLevel(logging.INFO)
        handler = logging.StreamHandler(f)
        log.addHandler(handler)
        log.debug('debug')
        f.seek(0)
        debug_msg = f.read().decode('utf-8')
        assert not debug_msg

        with logger_level(log, logging.DEBUG):
            log.debug('debug')
            f.seek(0)
            debug_msg = f.read().decode('utf-8')
            assert debug_msg

        assert log.level == logging.INFO



# Generated at 2022-06-14 06:34:26.035197
# Unit test for function get_config
def test_get_config():
    import json
    import yaml

    config_string_py2 = "{'version': 1}"
    config_string_py3 = "{\"version\": 1}"
    config_string_json = json.dumps({"version": 1})
    config_string_yaml = yaml.dump({"version": 1})
    config_dict = {"version": 1}

    assert get_config(config_string_py2) == config_dict
    assert get_config(config_string_py3) == config_dict
    assert get_config(config_string_json) == config_dict
    assert get_config(config_string_yaml) == config_dict
    assert get_config(config_dict) == config_dict


if __name__ == '__main__':
    test_get_config()

# Generated at 2022-06-14 06:34:31.129057
# Unit test for function logger_level
def test_logger_level():
    configure()
    log = getLogger()
    # first make sure that the log level is not DEBUG
    assert log.level != logging.DEBUG
    # now test the context manager to verify that the level is reset
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level != logging.DEBUG



# Generated at 2022-06-14 06:34:42.011695
# Unit test for function configure
def test_configure():
    configure()
    logging.getLogger(__name__).info('Quick brown fox jumps over the lazy dog.')


# Generated at 2022-06-14 06:34:44.272542
# Unit test for function logger_level
def test_logger_level():
    logger = get_logger(__name__)
    logger.warning('test')
    with logger_level(logger, logging.CRITICAL):
        logger.warning('test - with logger_level')
    logger.warning('test')



# Generated at 2022-06-14 06:34:49.366480
# Unit test for function get_config
def test_get_config():
    config = {}
    assert get_config() == config

    config = '{}'
    assert get_config(config=config) == json.loads(config)

    config = '{a:b}'
    assert get_config(config=config) == yaml.load(config)

# Generated at 2022-06-14 06:35:02.653376
# Unit test for function logger_level
def test_logger_level():
    # Adapted from http://stackoverflow.com/a/29993177
    import logging
    import sys
    import os

    # use sys.stdout so that the test can capture the output.
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    class Capturing(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stdout = self._stdout

    logger = logging.getLogger()
