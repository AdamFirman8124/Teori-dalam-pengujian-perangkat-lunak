

# Generated at 2022-06-14 12:31:03.718061
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert isinstance(lf, logging.Formatter)

# Generated at 2022-06-14 12:31:06.971954
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = gen_log
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    logger.warning('Test Message')
    logger.error('Error Message')
# Unit testing for class LogFormatter

# Generated at 2022-06-14 12:31:14.213538
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class _MockRecord(object):
        __slots__ = ("levelno", "message", "asctime", "color", "end_color")

        def __init__(self, levelno: int) -> None:
            self.levelno = levelno
            self.message = "test_message"
            self.asctime = "test_asctime"
            self.color = "test_color"
            self.end_color = "test_end_color"

    log_formatter = LogFormatter()
    record = _MockRecord(logging.DEBUG)
    log_formatter.format(record)
    assert record.message == "test_message"



# Generated at 2022-06-14 12:31:25.286436
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    #logging levelno is a tuple of logging level like this,
    #see: https://docs.python.org/3.5/library/logging.html#logging-levels
    #CRITICAL = 50
    #FATAL = CRITICAL
    #ERROR = 40
    #WARNING = 30
    #WARN = WARNING
    #INFO = 20
    #DEBUG = 10
    #NOTSET = 0
    formatter = LogFormatter()
    logging.getLogger("tornado.general").setLevel(logging.DEBUG)
    gen_log = logging.getLogger("tornado.general")
    gen_log.debug("debug message: %s%s",
                  "debug", ", not you")
    gen_log.info("info message: %s%s",
                 "info", ", just do it")
    gen

# Generated at 2022-06-14 12:31:26.822317
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
  pass
from tornado.testing import AsyncTestCase, gen_test

# Generated at 2022-06-14 12:31:35.947052
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import sys
    import logging
    logger = logging.getLogger('test_LogFormatter_format')  
    logger.setLevel(logging.DEBUG)  

    stream_handler = logging.StreamHandler(sys.stdout)
    # stream_handler.setLevel(logging.DEBUG)  
    formatter = LogFormatter(color=True, datefmt='%Y-%m-%d %H:%M:%S', fmt='%(color)s%(asctime)s [%(levelname)s] %(end_color)s %(message)s')
    stream_handler.setFormatter(formatter)  

    logger.addHandler(stream_handler)  

    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')

# Generated at 2022-06-14 12:31:43.754224
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from unittest import mock
    from tornado.options import options

    options.logging = 'None'
    with mock.patch('tornado.log.logging') as mocked_logging:
        enable_pretty_logging()
        mocked_logging.fatal.assert_not_called()

    options.logging = 'info'
    with mock.patch('tornado.log.logging') as mocked_logging:
        enable_pretty_logging()
        mocked_logging.basicConfig.assert_called_once_with(level=20)

    options.logging = 'debug'
    with mock.patch('tornado.log.logging') as mocked_logging:
        enable_pretty_logging()
        mocked_logging.basicConfig.assert_called_once_with(level=10)


# Generated at 2022-06-14 12:31:56.417207
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'  # noqa: E501
    datefmt = '%y%m%d %H:%M:%S'
    style = '%'
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    f = LogFormatter(fmt,datefmt,style,color,colors)

# Generated at 2022-06-14 12:31:58.171814
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:32:00.455499
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = LogFormatter()._fmt
    msg = "%s" % ("hello world")
    fmt % {"message": msg}

# Generated at 2022-06-14 12:32:19.371291
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Given
    message = "This is a test"
    record = logging.LogRecord(
        name=None, level=logging.DEBUG, pathname=None, lineno=None,
        msg=message, args=None, exc_info=None, func=None
    )
    expected = "[D " + LogFormatter.DEFAULT_DATE_FORMAT + " None:None] " + message # noqa: E501
    formatter = LogFormatter()

    # When
    result = formatter.format(record)

    # Then
    assert(expected == result)


# Generated at 2022-06-14 12:32:20.531288
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:32:24.371880
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.log import app_log, access_log, gen_log
    app_log.error("hello")
    access_log.error("hello")
    gen_log.error("hello")

# Generated at 2022-06-14 12:32:31.736297
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import os
    import sys
    import logging
    import unittest

    level = logging.DEBUG
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(LogFormatter())
    logger.addHandler(ch)
    logger.debug('This is a logger text')
    logger.error('This is a error message')
    logger.info('This is a info message')
    logger.warning('This is a warning message')
    logger.critical('This is a critical message')


# Generated at 2022-06-14 12:32:44.675498
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from datetime import datetime
    import logging, sys

    class Record(object):
        def __init__(self):
            self.levelno = logging.DEBUG # type: int
            self.levelname = 'DEBUG' # type: str
            self.module = 'test_LogFormatter_format' # type: str
            self.lineno = sys._getframe().f_lineno + 1 # type: int
            self.name = 'tornado.test' # type: str
            self.message = 'message' # type: str
            self.exc_info = None # type: Any
            self.exc_text = None # type: Any
        def getMessage(self):
            return self.message
    record = Record()
    formatter = LogFormatter()

# Generated at 2022-06-14 12:32:57.323500
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.define("log_file_prefix", type=str)
    tornado.options.define("log_file_max_size", type=int)
    tornado.options.define("log_file_num_backups", type=int)
    tornado.options.define("log_rotate_mode", type=str)
    tornado.options.define("log_rotate_when", type=str)
    tornado.options.define("log_rotate_interval", type=int)
    tornado.options.define("log_to_stderr", type=bool)
    tornado.options.define("logging", type=str)
    options = tornado.options.options
    options.log_file_prefix="log_file_prefix"
    options.log_file_max_size=1024

# Generated at 2022-06-14 12:33:04.614252
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.log_file_prefix= "test.log"
    tornado.options.options.log_file_max_size = 1000
    tornado.options.options.log_file_num_backups = 10
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_rotate_when = "D"
    tornado.options.options.log_rotate_interval = 3
    tornado.options.options.logging = "debug"
    tornado.options.options.log_to_stderr = True
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:07.495207
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lF = LogFormatter()
    record = logging.LogRecord("general", 1, "", 0, "message", None, None)
    result = lF.format(record)
    print(result)    



# Generated at 2022-06-14 12:33:09.655290
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Run doctest on LogFormatter.__init__()."""
    _ = LogFormatter()



# Generated at 2022-06-14 12:33:12.430649
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    print(formatter._fmt)
    print(formatter._colors)
    print(formatter._normal)


# Generated at 2022-06-14 12:33:22.827298
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    assert True


# Generated at 2022-06-14 12:33:34.709000
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    """test_LogFormatter_format.py
    ================================================

    This demonstrates how to write a unit test using the ``unittest``
    module. It tests that the ``format()`` method of the ``LogFormatter``
    class works as expected.
    """

    import unittest
    import tempfile
    import shutil
    import time
    import logging
    import os
    import re

    import tornado

    this_dir = os.path.dirname(__file__)
    test_dir = os.path.join(this_dir, "data", "test_LogFormatter_format")
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp(dir=test_dir)

   

# Generated at 2022-06-14 12:33:43.212234
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class TestLogFormatter(LogFormatter):
        pass

    t = TestLogFormatter()
    assert t.DEFAULT_FORMAT == LogFormatter.DEFAULT_FORMAT
    assert t.DEFAULT_DATE_FORMAT == LogFormatter.DEFAULT_DATE_FORMAT

    # test for ctor arg: fmt
    tf = TestLogFormatter(fmt='%(asctime)s %(message)s')
    r = logging.LogRecord("name", logging.DEBUG, "pathname", 1, "msg", (), None)
    assert tf.format(r) == "%s %s" % (r.asctime, r.message)

    # test for ctor arg: datefmt

# Generated at 2022-06-14 12:33:55.745478
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.define(
        "logging",
        default="none",
        help=("Set the Python log level. If 'none', tornado won't touch the " "logging setup."),
    )
    tornado.options.define(
        "log_to_stderr",
        type=bool,
        default=None,
        help=("Send log output to stderr (colorized if possible). " "By default use stderr if --log_file_prefix is not set and " "no other logging is configured."),
    )

# Generated at 2022-06-14 12:34:07.441896
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    f = LogFormatter(fmt='%(color)s%(asctime)s%(end_color)s - %(message)s')
    r = logging.LogRecord('name', logging.DEBUG, 'pathname.py', 10,
                          'msg', None, None)
    # Then
    assert f.format(r) == '%(color)s%(asctime)s%(end_color)s - %(message)s'
    # When
    f.datefmt = '%y%m%d %H:%M:%S'
    # Then
    assert f.format(r) == '%(color)s%(asctime)s%(end_color)s - %(message)s'
    # When

# Generated at 2022-06-14 12:34:11.086914
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert type(formatter.DEFAULT_FORMAT) == str
    assert type(formatter.DEFAULT_DATE_FORMAT) == str
    assert type(formatter.DEFAULT_COLORS) == dict
    assert type(formatter._fmt) == str
    assert type(formatter._colors) == dict
    assert type(formatter._normal) == str


# Generated at 2022-06-14 12:34:24.294762
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import sys
    import logging
    import tornado.options
    import tornado.log
    class DummyOptions(object):
        pass
    # Set up some dummy options
    options = DummyOptions()
    options.logging = "DEBUG"
    options.log_to_stderr = True
    options.log_file_prefix = None
    options.log_rotate_mode = "size"
    options.log_rotate_when = "S"
    options.log_rotate_interval = 1
    options.log_file_max_size = 1000
    options.log_file_num_backups = 1
    logger = logging.getLogger()
    # Check that a channel has been added to the logger
    channel_num_before = len(logger.handlers)
    tornado.log.enable_pretty_log

# Generated at 2022-06-14 12:34:32.557999
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    log_format = "%(asctime)s [%(levelname)-8s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = LogFormatter(fmt=log_format, datefmt=date_format)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")


# Generated at 2022-06-14 12:34:33.939905
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt


# Generated at 2022-06-14 12:34:35.857607
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    rotat

# Generated at 2022-06-14 12:35:01.767966
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # noqa: F811
    LogFormatter()



# Generated at 2022-06-14 12:35:14.050447
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado.log

    LOG_FILE_PREFIX = '/tmp/tornado.log'
    LOG_ROTATE_MODE = 'time'
    LOG_ROTATE_WHEN = 'S'
    LOG_ROTATE_INTERVAL = 1
    LOG_FILE_NUM_BACKUPS = 100
    logging.basicConfig()
    logger = logging.getLogger()

    tornado.log.enable_pretty_logging(options=tornado.options.options, logger=logger)

    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)

    tornado.options.options.logging = 'debug'
    tornado.options.options.log_file_prefix = LOG_FILE_PREF

# Generated at 2022-06-14 12:35:15.387535
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.enable_pretty_logging()

# Generated at 2022-06-14 12:35:24.019703
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class Options:
        def __init__(self):
            self.logging = 'test'
            self.log_file_prefix = 'test'
            self.log_rotate_mode = 'time'
            self.log_file_num_backups = 2
            self.log_rotate_when = 'H'
            self.log_rotate_interval = 2
            self.log_to_stderr = True

    options = Options()
    logger = logging.getLogger()
    enable_pretty_logging(options, logger)
    logger.info("The log works")
    assert logger.handlers[0].level == logging.INFO
    logger.error("The log works")
    assert logger.handlers[0].level == logging.ERROR
    logger.warning("The log works")
    assert logger.hand

# Generated at 2022-06-14 12:35:26.238572
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = lambda : None
    options.logging = False

    gen_log.info('test_enable_pretty_logging')


# Generated at 2022-06-14 12:35:32.239775
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger("test_log")
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(10)
    logger.error("TestError")
    logger.debug("TestDebug")
    logger.warning("TestWarning")
    logger.info("TestInfo")
    logger.critical("TestCritical")

test_LogFormatter_format()

# Generated at 2022-06-14 12:35:37.575378
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    l = LogFormatter()
    l = LogFormatter(fmt="%(levelname)s %(message)s")
    l = LogFormatter(datefmt="%y %m %d %H:%M:%S")
    l = LogFormatter(color=False, colors={})
    l = LogFormatter(style="{")
    l = LogFormatter(style="{", color=False)



# Generated at 2022-06-14 12:35:43.879024
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define
    define("logging", default="none")
    enable_pretty_logging()
    assert logging.getLogger().level == logging.NOTSET
    define("logging", default="info")
    enable_pretty_logging()
    assert logging.getLogger().level == logging.INFO

# Generated at 2022-06-14 12:35:54.675420
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    fmt = LogFormatter()
    if fmt.datefmt != LogFormatter.DEFAULT_DATE_FORMAT:
        raise Exception(
            "LogFormatter.datefmt: expected="
            + LogFormatter.DEFAULT_DATE_FORMAT
            + ", actual="
            + fmt.datefmt
        )
    if fmt._fmt != LogFormatter.DEFAULT_FORMAT:
        raise Exception(
            "LogFormatter._fmt: expected="
            + LogFormatter.DEFAULT_FORMAT
            + ", actual="
            + fmt._fmt
        )

# Generated at 2022-06-14 12:35:58.985130
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    obj = logging.LogRecord('myname', logging.DEBUG, '/path/file', 123, 'a', None, None)
    formatter = LogFormatter()
    assert formatter.format(obj)


# Generated at 2022-06-14 12:36:32.461892
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()
    LogFormatter(color=False)
    LogFormatter(color=True)


# Generated at 2022-06-14 12:36:33.374877
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    pass



# Generated at 2022-06-14 12:36:40.770970
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Import tornado.options after setting the environment variable
    # to avoid parsing the command line
    import os
    import tornado.options
    os.environ["TORNADO_LOGGING"] = "debug"
    tornado.options.parse_command_line()
    assert tornado.options.options.logging == "debug"
    enable_pretty_logging()
    assert tornado.options.options.logging == "debug"

# Generated at 2022-06-14 12:36:42.775069
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt is not None


# Generated at 2022-06-14 12:36:53.544011
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import io
    import logging
    import logging.config
    import logging.handlers

    log_config = dict(
        version = 1,
        formatters = {
            'tornado': {
                '()': 'tornado.log.LogFormatter',
                'color': True
            }
        },
        handlers = {
            'test': {
                'class': 'logging.StreamHandler',
                'formatter': 'tornado',
                'stream': 'ext://sys.stdout'
            }
        },
        root = {
            'handlers': ['test'],
            'level': 'INFO',
        },
    )

    if colorama:
        colorama.init()

    logger = logging.getLogger("tornado")
    old_loggers = list(logger.handlers)

# Generated at 2022-06-14 12:36:59.227773
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # options is None
    enable_pretty_logging()

    # options is not None
    import tornado.options
    tornado.options.options.logging = "none"
    enable_pretty_logging()

    # logger is None
    tornado.options.options.logging = None
    enable_pretty_logging()

# Generated at 2022-06-14 12:37:06.271921
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(
        fmt='%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s',  # noqa: E501
        datefmt='%y%m%d %H:%M:%S',
        style='%',
        color=True,
        colors={
            logging.DEBUG: 4,  # Blue
            logging.INFO: 2,  # Green
            logging.WARNING: 3,  # Yellow
            logging.ERROR: 1,  # Red
            logging.CRITICAL: 5,  # Magenta
        },
    )

_default_log_handler = None  # type: Optional[logging.Handler]



# Generated at 2022-06-14 12:37:10.709464
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter("%(message)s")
    assert f.format(logging.LogRecord("name", logging.INFO, "path", 1, "hello", (), None, None, "func")) == "hello"

# Generated at 2022-06-14 12:37:11.343449
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert 1 == 1

# Generated at 2022-06-14 12:37:13.873828
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(options=None)
    enable_pretty_logging(options=None, logger=None)

# Generated at 2022-06-14 12:38:27.684739
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    time = "161117 12:54:01"
    fmt = LogFormatter()._fmt
    color = LogFormatter()._normal

    assert "\033[2;3" in LogFormatter(color=True)._colors[20]
    assert curses.tigetstr("sgr0") in LogFormatter(color=True)._normal

    assert time in LogFormatter().formatTime(None)

    msg = "INFO " + time + " " + sys.argv[0] + ":1234] example_message"
    assert msg == LogFormatter().format(
        logging.LogRecord(
            "tornado.general", logging.INFO, "", 1234, msg, (), None
        )
    )


# Generated at 2022-06-14 12:38:36.280367
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
  color = True;
  fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
  datefmt = "%y%m%d %H:%M:%S"
  style = "%";
  colors = LogFormatter.DEFAULT_COLORS
  formatter = LogFormatter(color=color, fmt=fmt, datefmt=datefmt, style=style, colors=colors)



# Generated at 2022-06-14 12:38:37.314954
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert enable_pretty_logging is None

# Generated at 2022-06-14 12:38:37.938779
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:38:41.477248
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter


# Generated at 2022-06-14 12:38:42.799384
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._colors == {}



# Generated at 2022-06-14 12:38:46.598865
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        enable_pretty_logging()
    except Exception as e:
        print("function enable_pretty_logging has error:", e)

if __name__ == '__main__':
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:55.190817
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    class TestOption(tornado.options.OptionParser, object):
        def __init__(self) -> None:
            super(TestOption, self).__init__()
            self.log_file_prefix = None
            self.log_rotate_mode = "size"
            self.log_file_max_size = 100
            self.log_file_num_backups = 10
            self.logging = "debug"
            self.log_to_stderr = None

    class TestLogRotateTime(TestOption):
        def __init__(self) -> None:
            super(TestLogRotateTime, self).__init__()
            self.log_rotate_mode = "time"


# Generated at 2022-06-14 12:38:57.733527
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    enable_pretty_logging(None,logger)
    assert logger.handlers

# Generated at 2022-06-14 12:39:06.557307
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter(
        fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s",
        datefmt="%y%m%d %H:%M:%S",
        color=True,
        colors={
            logging.DEBUG: 4,
            logging.INFO: 2,
            logging.WARNING: 3,
            logging.ERROR: 1,
            logging.CRITICAL: 5,
        }
    )
