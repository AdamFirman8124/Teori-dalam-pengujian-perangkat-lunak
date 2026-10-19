

# Generated at 2022-06-14 12:31:04.742788
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Note: this test is necessarily trivial, because application code
    # can only call the public methods, and LogFormatter is just a
    # wrapper around logging.Formatter, so the interesting work is
    # done in the logging module.
    log_record = logging.LogRecord("x", "DEBUG", "x", "x", "x", "x", "x")
    log_record.msg = "x"
    log_record.args = ("x",)
    log_record.exc_info = ("x", "x", "x")
    log_record.exc_text = "x\n"
    lf = LogFormatter()
    output = lf.format(log_record)

# Generated at 2022-06-14 12:31:13.306105
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado
    tornado.options.options = tornado.options.parse_command_line("--logging=NONE")
    tornado.options.options = tornado.options.parse_command_line("--logging=DEBUG")
    tornado.options.options = tornado.options.parse_command_line("--logging=INFO")
    tornado.options.options = tornado.options.parse_command_line("--logging=WARN")
    tornado.options.options = tornado.options.parse_command_line("--logging=ERROR")
    tornado.options.options = tornado.options.parse_command_line("--logging=CRITICAL")
    tornado.options.options = tornado.options.parse_command_line("--logging=NONE") # Do nothing

test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:23.470022
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = '%(color)s%(levelname)s%(end_color)s %(message)s'
    f = LogFormatter(fmt)
    record = logging.makeLogRecord({'msg': 'a msg', 'levelname': 'INFO'})
    assert f.format(record) == '\x1b[0;32mINFO\x1b[0m a msg'
    record = logging.makeLogRecord({'msg': 'a msg', 'levelname': 'DEBUG'})
    assert f.format(record) == '\x1b[0;34mDEBUG\x1b[0m a msg'



# Generated at 2022-06-14 12:31:33.349958
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    assert formatter.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert formatter._colors
    assert formatter._normal
    assert formatter._fmt == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"

test_LogFormatter()

# Generated at 2022-06-14 12:31:44.460937
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._colors == LogFormatter.DEFAULT_COLORS
    assert len(LogFormatter(color=False)._colors) == 0
    assert LogFormatter(
        color=False, colors={logging.DEBUG: 9}
    )._colors == {}  # type: ignore
    assert LogFormatter(color=True, colors={logging.DEBUG: 9})._colors[
        logging.DEBUG
    ] == "\033[2;39m"
    test_dict = {
        logging.ERROR: 1,
        logging.CRITICAL: 2,
        logging.WARNING: 3,
        logging.INFO: 4,
        logging.DEBUG: 5,
    }
    assert LogFormatter(color=True, colors=test_dict)._colors == test_dict

_default_log_handler

# Generated at 2022-06-14 12:31:56.823261
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import os
    import sys
    import shutil

    def write_file(filename: str, contents: str) -> None:
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, "w") as f:
            f.write(contents)
    # Test that options.logging overrides logging.getLevelName()
    tornado.options.parse_command_line(
        ["progname", "--logging=debug"]
    )
    root_logger = logging.getLogger()
    assert root_logger.getEffectiveLevel() == logging.DEBUG

    # Test that logging.getLevelName() overrides options.logging

# Generated at 2022-06-14 12:32:09.173548
# Unit test for constructor of class LogFormatter
def test_LogFormatter():

    # default arguments
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    # create formatter
    formatter = LogFormatter()
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)

    logger.error("this is error message")
    logger.debug("this is debug message")

    # set color = False
    logging.basicConfig(level = logging.DEBUG)
    formatter = LogFormatter(color = False)
    handler.setFormatter(formatter)
    logger.debug("this is debug message,without color")

    # set fmt

# Generated at 2022-06-14 12:32:16.670429
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options
    options.logging="debug"
    options.log_file_prefix="test"
    options.log_rotate_mode="size"
    options.log_file_max_size=10
    options.log_file_num_backups=3
    options.log_to_stderr=None
    enable_pretty_logging()

# Generated at 2022-06-14 12:32:25.618034
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: ()-> None
    assert issubclass(LogFormatter, logging.Formatter)
    f = LogFormatter() # type: ignore
    f.format(logging.LogRecord("c", logging.INFO, "f", 1, "hello", (),"", None))
    f = LogFormatter(datefmt="%Y-%m-%d %H:%M:%S") # type: ignore
    f.format(logging.LogRecord("c", logging.INFO, "f", 1, "hello", (),"", None))
    assert f._normal
    f = LogFormatter(colors={1: 6}) # type: ignore
    f.format(logging.LogRecord("c", logging.INFO, "f", 1, "hello", (),"", None))
    assert f._normal
    assert f._colors

# Generated at 2022-06-14 12:32:34.155203
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options['logging'] = 'debug'
    tornado.options.options['log_file_prefix'] = 'tornado.log'
    tornado.options.options['log_rotate_mode'] = 'size'
    tornado.options.options['log_file_max_size'] = 1024
    tornado.options.options['log_file_num_backups'] = 10
    tornado.options.options['log_to_stderr'] = True
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    enable_pretty_logging(tornado.options.options, logger)
    tornado.options.options = dict()
    if False: # pylint: disable=using-constant-test
        print(logger)
test_enable_pretty_logging

# Generated at 2022-06-14 12:32:59.268020
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log = logging.getLogger('test')
    # want error, critical, warning to be red
    # want info, debug to be green
    # want other levels to be yellow

    class GoodException(Exception):
        pass

    class BadException(Exception):
        def __str__(self):
            return 'I have a\nnewline'

    class UnicodeException(Exception):
        def __str__(self):
            return '\xe9'

    class BrokenReprException(Exception):
        def __str__(self):
            return object()

    log.handlers = [logging.StreamHandler(sys.stdout)]
    log.error("error: no exception", exc_info=False)
    log.critical("critical: no exception", exc_info=False)

# Generated at 2022-06-14 12:33:10.791830
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import unittest
    from tornado.options import define, options

    define("log_file_prefix", type=str, default='tornado.log')
    define("log_rotate_mode", type=str, default='size')
    define("log_file_max_size", type=int, default=1024)
    define("log_file_num_backups", type=int, default=10)
    define("log_rotate_when", type=str, default='h')
    define("log_rotate_interval", type=int, default=1)
    define("logging", type=str, default='info')
    define("log_to_stderr", type=bool, default=False)

    enable_pretty_logging()


# Generated at 2022-06-14 12:33:22.058668
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.options import define, options
    from logging import INFO, DEBUG, NOTSET, ERROR

    define("logging", default="none", help="Which logging level to use.", type=str)
    define("log_file_prefix", default=None, help="Where to log to.", type=str)
    define("log_file_max_size", default=100, help="Maximum size of log files before rollover", type=int)
    define("log_file_num_backups", default=10, help="Number of log files to keep", type=int)
    define("log_rotate_mode", default="size", help="When to rotate logs", type=str)
    define("log_rotate_when", default="midnight", help="When to rotate logs", type=str)

# Generated at 2022-06-14 12:33:28.293982
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger("unittest")
    enable_pretty_logging(None, logger)
    logger.setLevel("DEBUG")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.fatal("fatal")



# Generated at 2022-06-14 12:33:34.397099
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    formatter = LogFormatter()
    formatter.format(logging.LogRecord(
        "tornado.test", logging.INFO, "", 99, "foo", None, None))
    formatter = LogFormatter(color=False)
    formatter.format(logging.LogRecord(
        "tornado.test", logging.INFO, "", 99, "foo", None, None))



# Generated at 2022-06-14 12:33:43.488818
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    log_formatter = LogFormatter(color=False)
    assert log_formatter is not None  # silence pyflakes
    log_formatter = LogFormatter(color=True)
    assert log_formatter is not None  # silence pyflakes
    log_formatter = LogFormatter(color=True, colors={})
    assert log_formatter is not None  # silence pyflakes
    fmt = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
    log_formatter = LogFormatter(fmt=fmt)
    assert log_formatter is not None  # silence pyflakes

# Generated at 2022-06-14 12:33:51.857697
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()
    LogFormatter(datefmt="%H:%M:%S")
    LogFormatter(fmt="%(color)s%(message)s")
    LogFormatter(fmt="%(color)s%(message)s", datefmt="%H:%M:%S")

# TODO(bdarnell): use a real exception for this (tornado.exceptions
# does not exist in the backport).

# Generated at 2022-06-14 12:33:54.071515
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    assert gen_log.getEffectiveLevel() == logging.INFO

# Generated at 2022-06-14 12:33:58.897126
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    def test(color, colors, expected):
        formatter = LogFormatter(color=color, colors=colors)
        assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
        assert formatter._colors == expected

    colors = {logging.DEBUG: 4, logging.INFO: 2}
    test(True, colors, colors)
    test(False, colors, {})


# Generated at 2022-06-14 12:34:08.304791
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        #pylint: disable=wrong-import-position
        from tornado.options import options, define, parse_command_line
    except ImportError as e:
        import sys
        import traceback
        raise ImportError(
            "Unable to import tornado.options in test_pretty_logging: %s" % e
        ).with_traceback(traceback.format_tb(sys.exc_info()[2]))
    import io
    import logging
    import logging.handlers
    import time
    import unittest
    import warnings
    import os

    define("logging", default="info")
    define("log_file_prefix", default=None)
    define("simple_logging", default=False)


# Generated at 2022-06-14 12:34:28.276323
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import functools
    from tornado.testing import AsyncTestCase
    from tornado.log import app_log, access_log, gen_log
    from tornado.gen import coroutine

    level_names = {
        logging.DEBUG: "DEBUG",
        logging.INFO: "INFO",
        logging.WARNING: "WARNING",
        logging.ERROR: "ERROR",
        logging.CRITICAL: "CRITICAL",
    }

    @coroutine
    def log_once(log, level):
        logging.log(level, level_names[level])
        yield  # Allow an event loop iteration so the logs get flushed.
        log.handlers[0].close()

    class MyTestCase(AsyncTestCase):
        def async_test(self, level):
            pass


# Generated at 2022-06-14 12:34:34.113376
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(
        fmt="%(color)s%(levelname)s%(end_color)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )



# Generated at 2022-06-14 12:34:35.615418
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    return


# Generated at 2022-06-14 12:34:46.474834
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    log_formatter = LogFormatter()
    assert log_formatter._fmt == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    assert log_formatter._normal == ""
    assert log_formatter._colors == {}
    assert log_formatter.datefmt == "%y%m%d %H:%M:%S"

    # Test for creating a LogFormatter for a terminal that does not
    # support color
    log_formatter = LogFormatter(color=False)

# Generated at 2022-06-14 12:34:50.111206
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("test")
    logger.warning("test message")
    logger.warning("%s", "test message")
    logger.warning("%s", 'test message')



# Generated at 2022-06-14 12:34:56.976955
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug("test debug message")
    logger.info("test info message")
    logger.warning("test warning message")
    logger.error("test error message")
    logger.critical("test critical message")


# Generated at 2022-06-14 12:35:00.304239
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(level=logging.INFO, format=LogFormatter.DEFAULT_FORMAT)
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())

    logger.info("Hello")



# Generated at 2022-06-14 12:35:07.028018
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from nose.tools import assert_equal
    from tornado.log import LogFormatter
    from tornado.log import gen_log

    log_format = '%(color)s%(levelname)s%(end_color)s %(message)s'
    log_date_format = '%H:%M:%S'
    formatter = LogFormatter(fmt=log_format, datefmt=log_date_format)

    record = gen_log.makeRecord(
        name='tornado.general',
        level=20,
        pathname='/foo/bar/tornado/log.py',
        lineno=33,
        msg='This is a %s',
        args=('test',),
        exc_info=None,
        func=None,
        sinfo=None,
    )
    form

# Generated at 2022-06-14 12:35:16.171099
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    _stderr = sys.stderr
    sys.stderr = open('/dev/null', 'a')
    class record:
        exc_info = None
        exc_text = None
        levelno = 1
        name = None
        pathname = None
        filename = None
        module = ''
        lineno = None
        funcName = None
        created = None
        asctime = None
        message = ''
        color = None
        end_color = None
    result = LogFormatter().format(record)
    sys.stderr = _stderr
    assert result.startswith('[E')


# Generated at 2022-06-14 12:35:17.103401
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()


# Generated at 2022-06-14 12:35:31.245689
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
    enable_pretty_logging()
    access_log.debug('A debug message')

# BasicConfig only for unit test

# Generated at 2022-06-14 12:35:31.942336
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:35:32.918367
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    tornado.options.get_options()

# Generated at 2022-06-14 12:35:39.503631
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Enable_pretty_logging: Given the configuration, this function ensures that the entire functionality of logging is specified 
    import sys as sys
    import tornado.options as o
    o.define("logging", default="none")
    o.define("log_to_stderr", default=True)
    sys.argv = ["def __init__"]
    o.parse_command_line()
    sys.argv.pop()
    logging.info("this is a test")
    logging.warning("this is a warning test")
    logging.error("this is a error test")

# Generated at 2022-06-14 12:35:50.829514
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # Dummy class used for testing
    class DummyRecord:
        pass

    test_record = DummyRecord()
    test_record.levelno = 100
    test_record.msg = "Test Message"
    test_record.asctime = "2019-01-01 10:10:10,000"

    test_colors = {100: 1, 200: 2}
    test_formatter = LogFormatter(
        fmt="[%(levelname)1.1s %(asctime)s] %(message)s",
        datefmt="%y%m%d %H:%M:%S",
        color=True,
        colors=test_colors,
    )
    test_output = test_formatter.format(test_record)

# Generated at 2022-06-14 12:36:03.260316
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = Dict[str, Any]()
    options['logging'] = 'debug'
    #log_file_prefix = '/tornado-4.5.1/tornado/log/log_file.log'
    options['log_file_prefix'] = '/log_file.log'
    options['log_rotate_mode'] = 'size'
    options['log_file_max_size'] = 1024
    options['log_file_num_backups'] = 20
    options['log_to_stderr'] = True
    options['log_rotate_when'] = 'D'
    options['log_rotate_interval'] = 90

    enable_pretty_logging(options)
    #print(logging.options)
    logger = logging.getLogger()
    #logger.setLevel(getattr

# Generated at 2022-06-14 12:36:12.175034
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # pragma: no cover
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)
    assert formatter._colors == LogFormatter.DEFAULT_COLORS
    assert formatter._normal == ""

    colors = { logging.DEBUG: 1 }
    formatter = LogFormatter(colors=colors)
    assert formatter._colors == colors
    assert formatter._normal == ""

    formatter = LogFormatter(color=False)
    assert formatter._colors == {}
    assert formatter._normal == ""

    formatter = LogFormatter(color=True)
    assert formatter._colors == {}
    assert formatter._normal == ""

    formatter = LogFormatter(color=False, colors={})
    assert formatter._colors == {}

# Generated at 2022-06-14 12:36:17.271029
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    record = logging.makeLogRecord({"msg": "some message"})
    assert formatter.format(record) == "[I 083100 43 log_test:4] some message"
    assert formatter.format(record)



# Generated at 2022-06-14 12:36:29.302680
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create the console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter and add it to the handlers
    formatter = LogFormatter(
        fmt='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Log some messages
    logger.info('info message')
    logger.debug('debug message')
    logger.warning('warning message')

# Generated at 2022-06-14 12:36:32.594571
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter(fmt="%(message)s", color=True, colors=LogFormatter.DEFAULT_COLORS)
    assert isinstance(lf, LogFormatter)



# Generated at 2022-06-14 12:36:51.893949
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    colorama = None
    try:
        import colorama
        colorama.init()
    except:
        pass

    # test with no color
    logger = logging.getLogger("tornado.test")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    def test(formatter):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info("test info")
        if colorama:
            logger.warn("test warning")
        logger.error("test error")
        if colorama:
            logger.critical("test critical")
        logger.removeHandler(handler)

    formatter = LogFormatter()
    test(formatter)

    formatter = LogFormatter(color=False)


# Generated at 2022-06-14 12:36:52.897961
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()



# Generated at 2022-06-14 12:37:01.622140
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    # Try to use the log_file_prefix to make sure that it does exist
    tornado.options.define("log_file_prefix", default=__file__ + ".log")
    tornado.log.enable_pretty_logging()
    # Remove the log file
    import os
    os.remove(__file__ + ".log")
    # Revert the default
    tornado.options.options.log_file_prefix = None

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:03.429187
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert isinstance(lf, LogFormatter)



# Generated at 2022-06-14 12:37:04.183657
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:37:11.792791
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import time

    tornado.options.parse_config_file("test/test_options.py")    
    tornado.options.parse_command_line()
    enable_pretty_logging()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    for i in range(10):
        logger.info("test %s", i)
        time.sleep(0.1)

# Generated at 2022-06-14 12:37:23.277332
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert log_formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert log_formatter._normal == ""
    assert log_formatter._colors == {}
    assert log_formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT



# Generated at 2022-06-14 12:37:26.026905
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = {}
    enable_pretty_logging(options)

if __name__ == '__main__':
    # Unit test for function enable_pretty_logging
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:32.476456
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class options:
        log_to_stderr = False
        log_file_prefix = "/tmp/dummy.txt"
        log_file_max_size = 1024**2
        log_file_num_backups = 0
        debug = False
        log_file_prefix = "dummy.txt"
    init_log(options)
    class record:
        levelno = logging.DEBUG
        exc_info = None
        exc_text = None
        def getMessage(self) -> str:
            return "dummy msg"
    formatter = LogFormatter()
    assert formatter.format(record()) == "[D %s dummy:0] dummy msg"



# Generated at 2022-06-14 12:37:43.993236
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    datefmt = "%y%m%d %H:%M:%S"
    style = "%"
    color = True
    colors = { logging.DEBUG: 4, # Blue
        logging.INFO: 2, # Green
        logging.WARNING: 3, # Yellow
        logging.ERROR: 1, # Red
        logging.CRITICAL: 5, # Magenta
    }
    try:
        formatter = LogFormatter(fmt, datefmt, style, color, colors)
    except Exception as e:
        print("constructor of class LogFormatter failed")
        print(str(e))
        return

# Generated at 2022-06-14 12:38:11.546970
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # pylint: disable=invalid-name
    try:
        import curses
    except ImportError:
        curses = None  # type: ignore

    if curses and sys.stderr.isatty():
        for _ in range(10):
            color = str(curses.tigetstr("setaf"), "ascii")
            # for code in range(1, 10):
            code = 2
            print(f"\n{color}{code}{str(curses.tigetstr('sgr0'), 'ascii')}")
        print()

    # name, level, msg, args, kwargs, exc_info, func, extra
    # record = logging.LogRecord(
    #     name="test", level=0, pathname="", lineno=0, msg="", args=None,
   

# Generated at 2022-06-14 12:38:23.283372
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options=__import__("tornado.options")
    option=options.options
    option.logging = "info"
    option.log_file_prefix = "test.log"
    option.log_rotate_mode = "size"
    option.log_file_max_size = 1024
    option.log_file_num_backups = 3
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, option.logging.upper()))
    if option.log_file_prefix:
        rotate_mode = option.log_rotate_mode

# Generated at 2022-06-14 12:38:32.239703
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    options = tornado.options.options
    options.logging = "debug"
    options.log_file_prefix = "1.json"
    options.log_file_max_size= 1024
    options.log_file_num_backups= 1
    options.log_rotate_mode="time"
    options.log_rotate_when="midnight"
    options.log_rotate_interval=1
    options.log_to_stderr=False
    enable_pretty_logging(options,logger)

# Generated at 2022-06-14 12:38:38.660976
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.log import LogFormatter
    from tornado.util import u

    dummy_logger = logging.getLogger("Dummy")
    log_handler = logging.StreamHandler()

    log_formatter = LogFormatter(color=True)
    log_handler.setFormatter(log_formatter)
    dummy_logger.addHandler(log_handler)

    dummy_logger.info(u("Test Message"))
    dummy_logger.debug(u("Test Message"))
    dummy_logger.warning(u("Test Message"))
    dummy_logger.error(u("Test Message"))
    dummy_logger.critical(u("Test Message"))

    dummy_logger.removeHandler(log_handler)



# Generated at 2022-06-14 12:38:50.128857
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class MockParseOptions():
        """
        Mock functions of ParseOptions class
        """
        def __init__(self):
            self.logging = None
            self.log_file_prefix = None
            self.log_rotate_mode = "size"
            self.log_file_max_size = 100
            self.log_file_num_backups = 1000
            self.log_to_stderr = False

        def log_to_stderr(self):
            """
            mock log_to_stderr function
            """
            return self.log_to_stderr

    mock_options = MockParseOptions()
    import lib.logger as logger
    logger.enable_pretty_logging(mock_options)

# Generated at 2022-06-14 12:38:51.832266
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    assert logger.handlers == []
    enable_pretty_logging(
        options=None,
        logger=logger
    )

# Generated at 2022-06-14 12:38:53.390317
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    print(__doc__)
    # Assertion starts
    assert True
    # Assertion ends

# Generated at 2022-06-14 12:39:03.308496
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = 'warning'
    tornado.options.options.log_file_prefix = 'test.log'
    tornado.options.options.log_to_stderr  = False
    tornado.options.options.log_rotate_mode = 'size'
    tornado.options.options.log_file_max_size = 1024
    tornado.options.options.log_file_num_backups = 3
    enable_pretty_logging()
    assert logger.level() == logging.WARNING

# Generated at 2022-06-14 12:39:05.556708
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    try:
        formatter = LogFormatter(color=True)
    except Exception:
        assert False
LogFormatter()



# Generated at 2022-06-14 12:39:15.134466
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.options.logging = "debug"
    tornado.options.options.log_file_prefix = "test_log.txt"
    tornado.options.options.log_file_max_size = None
    tornado.options.options.log_file_num_backups = None
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_to_stderr = None
    tornado.options.options.log_rotate_when = "test-test"
    tornado.options.options.log_rotate_interval = "test-test"
    enable_pretty_logging()

# Generated at 2022-06-14 12:39:53.684355
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Test the constructor of class LogFormatter"""
    formatter = LogFormatter()  # type: Optional[LogFormatter]


# Generated at 2022-06-14 12:40:05.252361
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter()
    msg = "hello space: %s, %d, %d"
    record = logging.LogRecord("name", 10, "file.py", 20, msg, ["hi",10,11], {})
    assert lf.format(record)=="[I 0101 00:00:00 file:20] hello space: hi, 10, 11"
    record = logging.LogRecord("name", 20, "file.py", 20, msg, ["hi","woo"], {})
    assert lf.format(record)=="[W 0101 00:00:00 file:20] hello space: hi, woo, 0"
    record = logging.LogRecord("name", 30, "file.py", 20, msg, ["hi",11.5,12], {})

# Generated at 2022-06-14 12:40:16.698161
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    options = tornado.options.options
    options.logging = "DEBUG"
    options.log_rotate_mode = None
    options.log_file_prefix = None
    options.log_to_stderr = True
    enable_pretty_logging()

    options.logging = "debug"
    options.log_rotate_mode = None
    options.log_file_prefix = None
    options.log_to_stderr = True
    enable_pretty_logging()

    options.logging = "info"
    options.log_rotate_mode = None
    options.log_file_prefix = None
    options.log_to_stderr = True
    enable_pretty_logging()

    options.logging = "warning"
    options.log_rotate_mode

# Generated at 2022-06-14 12:40:17.249750
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:40:25.442976
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import logging.handlers
    tornado.options.options.logging =  'debug'
    tornado.options.options.log_file_prefix = './tmp/log_file'
    tornado.options.options.log_file_max_size = 100
    tornado.options.options.log_file_num_backups = 1
    tornado.options.options.log_rotate_mode = 'time'
    tornado.options.options.log_rotate_when = 'D'
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_to_stderr = False
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    enable_pretty_logging()

# Generated at 2022-06-14 12:40:34.124559
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    formatter = LogFormatter(
            fmt='[%(color)s%(levelname)s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
        )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.debug("test")





# Generated at 2022-06-14 12:40:37.207864
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging(): 
    logging.basicConfig()
    options = type('', (), {})()
    options.logging = logging.CRITICAL
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:40:37.950564
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()