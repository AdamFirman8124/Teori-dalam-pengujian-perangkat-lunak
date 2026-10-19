

# Generated at 2022-06-14 12:31:03.757538
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tempfile
    import random
    import os
    from tornado.options import define, options
    define("logging", default="debug")
    define("log_file_prefix", type=str, default=tempfile.mktemp())
    define("log_rotate_mode", type=str, default="size")
    define("log_file_max_size", type=int, default=1000)
    define("log_file_num_backups", type=int, default=1)
    define("log_rotate_when", type=str, default="S")
    define("log_rotate_interval", type=int, default=1)
    define("log_to_stderr", type=bool, default=False)
    enable_pretty_logging()
    # logging.info("test")
    # assert os.path

# Generated at 2022-06-14 12:31:12.660918
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    import logging

    # test that the LogFormatter constructor works with the signature
    # used by argparse and config files.
    # Note that a LogFormatter object is initialized automatically
    # when the tornado.options module is imported
    logging.basicConfig(
        level=logging.DEBUG, format="%(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    lf = LogFormatter(fmt="%(color)s%(levelname)s: %(message)s")
    logging.debug("test")


# Copied from the stdlib since Tornado is compatible with older versions.
# The logging module does not use the new style formatting by default
# (since in some cases it can be slower) so we have to explicitly ask for it.


# Generated at 2022-06-14 12:31:25.104896
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import logging.handlers
    import logging.config

    logger = logging.getLogger()
    CONFIGS = [
        {
            "logging": "info",
            "log_file_prefix": "tornado.log",
            "log_rotate_mode": "time",
            "log_rotate_when": "D",
            "log_rotate_interval": 1,
            "log_file_num_backups": 15,
        },
        {
            "logging": "warning",
            "log_file_prefix": "tornado.log",
            "log_rotate_mode": "size",
            "log_file_max_size": 10,
            "log_file_num_backups": 15,
        },
    ]

# Generated at 2022-06-14 12:31:35.181600
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = 'none'
    assert enable_pretty_logging() is None
    tornado.options.options.logging = 'info'
    tornado.options.options.log_to_stderr = None
    tornado.options.options.log_file_prefix = None
    tornado.options.options.log_file_num_backups = None
    tornado.options.options.log_file_max_size = None
    tornado.options.options.log_rotate_when = None
    tornado.options.options.log_rotate_interval = None
    tornado.options.options.log_rotate_mode = None
    logger = cast(Any, logging.getLogger())
    logger.setLevel(logging.INFO)
    assert enable_pretty_logging() is None

# Generated at 2022-06-14 12:31:40.965979
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    f = LogFormatter()
    assert isinstance(f, logging.Formatter)
    assert f is not None
    assert f._fmt == f.DEFAULT_FORMAT
    assert f._colors == f.DEFAULT_COLORS
    assert f._normal != ""



# Generated at 2022-06-14 12:31:43.752006
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.makeLogRecord({})
    record.levelno = logging.DEBUG
    record.message = "TEST"
    print(formatter.format(record))


# Generated at 2022-06-14 12:31:56.416564
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    class Options(object):
        def __init__(self):
            self.logging = "debug"
            self.log_file_prefix = None
            self.log_to_stderr = True
            self.log_rotate_mode = "size"
            self.log_rotate_when = ""
            self.log_rotate_interval = None
            self.log_file_max_size = None
            self.log_file_num_backups = None

    logging.disable(logging.CRITICAL)
    enable_pretty_logging(Options())
    logging.info("Testing logging")
    tornado.options.enable_pretty_logging()
    logging.info("Testing logging")
    logging.disable(logging.NOTSET)

# Generated at 2022-06-14 12:31:58.172043
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert enable_pretty_logging

# Generated at 2022-06-14 12:32:09.976665
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import tornado
    import logging
    import StringIO
    formatter = LogFormatter()
    logger = logging.getLogger("tornado.general")
    handler = logging.StreamHandler(StringIO.StringIO())
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Test basic logging.
    logger.info("Hello")
    s = handler.stream
    assert s.getvalue().endswith("Hello\n")

    # Test message containing unicode.
    logger.info("\u2713")
    assert s.getvalue().endswith("\xe2\x9c\x93\n")

    # Test message containing utf8 bytestring.
    logger.info(u"\u2713".encode("utf-8"))

# Generated at 2022-06-14 12:32:21.921184
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import datetime
    datetime_instance = datetime.datetime.now()
    record = logging.LogRecord('name_of_logger', logging.WARNING, '/aaa/bbb.py', 19, 'Message', args=[], exc_info=None, stack_info=None)
    record.__dict__['asctime'] = datetime_instance
    record.__dict__['message'] = 'message'
    record.__dict__['color'] = 'color'
    record.__dict__['end_color'] = 'end_color'
    record.__dict__['exc_text'] = 'exc_text'

    lf = LogFormatter()

# Generated at 2022-06-14 12:32:45.095578
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log

    def test_opts() -> None:
        """Test the deprecated ``enable_pretty_logging`` function."""
        tornado.options.define("logging", default="debug", help="log level")
        tornado.options.define("log_to_stderr", type=bool, help="stdout logging")
        tornado.options.define("log_file_prefix", type=str, help="log file")
        tornado.options.define("log_rotate_mode", type=str, help="rotate log mode")
        tornado.options.define("log_file_num_backups", type=int, help="rotate file num")
        tornado.options.define("log_file_max_size", type=int, help="rotate max size")

# Generated at 2022-06-14 12:32:56.715856
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_formatter=LogFormatter(
        fmt = LogFormatter.DEFAULT_FORMAT,
        datefmt = LogFormatter.DEFAULT_DATE_FORMAT,
        style = "%",
        color = True,
        colors = LogFormatter.DEFAULT_COLORS,
    )
    record = logging.LogRecord("name","levelno","pathname","lineno","msg","args","exc_info",
                               func="func")
    record.levelno = logging.DEBUG
    assert log_formatter.format(record) == "[D 20190120 20:40:42 pathname:999]  msg"
    assert log_formatter.format(record) != "[DEBUG 20190120 20:40:42 pathname:999]  msg"



# Generated at 2022-06-14 12:32:57.692067
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:00.439350
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = None
    enable_pretty_logging()
    tornado.options.options.logging = "not None"
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:02.095073
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # This ia a dummy test. The actual test is in ioloop_test.py
    pass

# Generated at 2022-06-14 12:33:10.229954
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import tornado.log
    import datetime
    formatter = tornado.log.LogFormatter(color=True)
    test_record = {"asctime":datetime.datetime(2019, 1, 18, 18, 19, 21, 711000), "levelno":20,  "args":(), "name":"tornado.general","message":"1234567890"}
    str = formatter.format(test_record)
    assert str == "[I 20190118 18:19:21 tornado.log:13] 1234567890"

    test_record = {"asctime":datetime.datetime(2019, 1, 18, 18, 19, 21, 711000), "levelno":20,  "args":(), "name":"tornado.general","message":"1234567890","exc_info":True,"exc_text":"cat"}
    str

# Generated at 2022-06-14 12:33:21.475119
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from datetime import datetime
    from io import StringIO
    import sys
    import os
    import logging
    import unittest

    # Redirect the stdout and stderr to a StringIO
    f = StringIO()
    sys.stdout = f

    datefmt = "%Y/%m/%d %H:%M:%S"
    logger = logging.getLogger(os.environ["LOGGING_NAME"])
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = LogFormatter(datefmt=datefmt)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info("test logging")
    output = f.getvalue()

# Generated at 2022-06-14 12:33:26.089944
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    class Record:
        __dict__ = {'name': 'test', 'levelno': 1, 'args': (1,2), 'msg': 'test'}
    record = Record()
    print(formatter.format(record))


# Generated at 2022-06-14 12:33:31.320699
# Unit test for method format of class LogFormatter
def test_LogFormatter_format(): 
    # Method attributes of class LogFormatter
    fmt = "a%(message)s" + "%(color)sb%(end_color)s"
    datefmt = "[%Y%m%d %H:%M:%S]"
    style = "%"
    color = True
    colors = {
        1: 4,  # Blue
        2: 2,  # Green
        3: 3,  # Yellow
        4: 1,  # Red
        5: 5,  # Magenta
    }
    
    # Instance attributes of class LogFormatter
    logF = LogFormatter(fmt, datefmt, style, color, colors)

# Generated at 2022-06-14 12:33:32.718517
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(None,logging.getLogger())

# Generated at 2022-06-14 12:33:59.263623
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.define("log_file_prefix", default="log.txt")
    tornado.options.define("log_rotate_mode", default="size")
    tornado.options.define("log_file_max_size", default=10000)
    tornado.options.define("log_file_num_backups", default=2)
    tornado.options.define("log_rotate_when", default="S")
    tornado.options.define("log_rotate_interval", default=10)

# Generated at 2022-06-14 12:34:03.687625
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    format = '%(levelname)s %(message)s'
    formatter = LogFormatter(fmt=format)
    record = logging.LogRecord("tornado.access", logging.INFO, None, 0, "test", None, None)
    assert isinstance(formatter.format(record), basestring_type)



# Generated at 2022-06-14 12:34:06.457601
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    instance = LogFormatter()
    assert isinstance(instance.format(logging.LogRecord("name", logging.DEBUG, "pathname", 0, "msg", args, None)), str)



# Generated at 2022-06-14 12:34:19.033411
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    import logging
    import io
    import io
    import sys
    from io import StringIO
    from logging import StreamHandler
    from tornado.log import LogFormatter
    from typing import Dict, Any, cast, Optional
    from logging import LogRecord
    from tornado.log import access_log as tornado_access_log
    from logging import getLogger as logging_getLogger
    from typing import Dict, Any, cast, Optional
    from tornado.escape import _unicode
    from tornado.util import unicode_type, basestring_type
    import logging
    import logging.handlers
    import sys
    from tornado.escape import _unicode
    from tornado.util import unicode_type, basestring_type

# Generated at 2022-06-14 12:34:20.243098
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    return



# Generated at 2022-06-14 12:34:24.589442
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import sys
    from logging.config import dictConfig

    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO

    log_config = dict(
        version=1,
        disable_existing_loggers=False,
        formatters={
            "colored": {
                "()": LogFormatter,
                "format": "%(color)s%(levelname)1.1s %(message)s%(end_color)s",
            }
        },
        handlers={
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "colored",
                "stream": "ext://sys.stdout",
            }
        },
        root={"handlers": ["console"]},
    )

    old_std

# Generated at 2022-06-14 12:34:26.206829
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Backwards compatibility for applications not using any logging
# configuration

# Generated at 2022-06-14 12:34:30.052853
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.LogRecord("test", logging.INFO, "filename", "lineno", "msg", None, None)
    res = formatter.format(record)


# Class for convenient logging of user-visible messages

# Generated at 2022-06-14 12:34:38.514249
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    f = LogFormatter()
    class r():
        def __init__(self,msg,levelno):
            self.msg = str(msg)
            self.levelno = int(levelno)
        def getMessage(self):
            return self.msg
    assert f.format(r("hello",1)) == "[ E . . . . . . . . . . . ] hello"



# Generated at 2022-06-14 12:34:39.980533
# Unit test for constructor of class LogFormatter
def test_LogFormatter():

    formatter = LogFormatter()
    assert formatter

    assert formatter._colors

    assert formatter._normal

# Generated at 2022-06-14 12:35:28.741263
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    TEST_LOG = {
        "message": "test msg",
        "args": "args1",
        "levelname": "DEBUG",
        "levelno": 10,
        "pathname": "c:/user/a.py",
        "filename": "a.py",
        "module": "a",
        "exc_info": "exc_info",
        "exc_text": "exc_text",
        "lineno": 123,
        "funcName": "function",
        "created": 1565791048.3626,
        "msecs": 362.6,
        "relativeCreated": 5,
        "thread": 123456,
        "threadName": "Thread-4",
        "processName": "MainProcess",
        "process": 1234,
    }

# Generated at 2022-06-14 12:35:38.810164
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    obj = LogFormatter()
    assert isinstance(obj, logging.Formatter)
    assert obj._fmt == obj.DEFAULT_FORMAT
    assert obj._colors == {}
    assert obj._normal == ""

    obj2 = LogFormatter(fmt="%(levelno)s")
    assert obj2._fmt == "%(levelno)s"

    # colors
    colors = {
        logging.CRITICAL: 5,  # Magenta
        logging.ERROR: 1,  # Red
        logging.WARNING: 3,  # Yellow
        logging.INFO: 2,  # Green
        logging.DEBUG: 4,  # Blue
    }
    obj3 = LogFormatter(color=True, colors=colors)
    assert obj3._colors == obj3._normal == ""


# Generated at 2022-06-14 12:35:50.653910
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import io
    import logging
    import re
    import sys
    import unittest
    import warnings

    from tornado.log import LogFormatter, app_log

    def cleanup_environment_variables():
        # Reset all environment variables that may be used by logging,
        # and restore them to their original values at the end.
        original_values = {}
        for key in ("LOG_FILE_PREFIX", "LOG_TO_STDERR", "LOG_ROTATE_MODE"):
            original_values[key] = os.environ.pop(key, None)
        for key in ("LOG_FILE_MAX_SIZE", "LOG_FILE_NUM_BACKUPS", "LOG_ROTATE_WHEN"):
            original_values[key] = os.environ.pop(key, None)

# Generated at 2022-06-14 12:35:52.027432
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()



# Generated at 2022-06-14 12:35:55.318832
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: () -> None
    log_fmt = LogFormatter()
    # LogFormatter needs to be initialized with the default params
    # to call its methods.
    log_fmt.format()



# Generated at 2022-06-14 12:35:58.540476
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options  # type: ignore

    enable_pretty_logging()
    enable_pretty_logging(options=tornado.options.options)

# Generated at 2022-06-14 12:36:02.198043
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = LogFormatter(
        fmt="%(asctime)s"
    )
    record = logging.LogRecord(
        levelname="DEBUG",
    )
    assert fmt.format(record) == "%(asctime)s"


# Generated at 2022-06-14 12:36:03.327323
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_fmt = LogFormatter()
    type(log_fmt)._colors = ''


# Generated at 2022-06-14 12:36:13.152813
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s"
    datefmt = '%d-%b-%Y %H:%M:%S'
    style = "%"
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    logFormatter = LogFormatter(
        fmt=fmt,
        datefmt=datefmt,
        style=style,
        color=color,
        colors=colors
    )

# Generated at 2022-06-14 12:36:15.383936
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:37:03.145978
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    df = LogFormatter()
    record = logging.LogRecord(
  "test",
  logging.INFO,
  "../test.py",
  1, "Test",
  None,
  None
)
    assert df.format(record)


# Generated at 2022-06-14 12:37:07.881532
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter()
    record = logging.LogRecord(
        "tornado.general", logging.INFO, "foo.py", 42, "log message", [], None
    )
    assert lf.format(record).endswith(" log message\n")


# Generated at 2022-06-14 12:37:19.912642
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.testing
    import logging
    import os

    class EnablePrettyLoggingTest(tornado.testing.AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.io_loop = self.setup_logging()

        def tearDown(self):
            self.io_loop.close()
            super().tearDown()

        def test_basics(self):
            self.assertEqual(
                logging.getLogger("tornado.access").level,
                logging.INFO,
            )
            self.assertEqual(logging.getLogger("tornado.application").level, logging.INFO)
            self.assertEqual(logging.getLogger("tornado.general").level, logging.INFO)

# Generated at 2022-06-14 12:37:24.144851
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    a = LogFormatter(color=True)
    assert len(a._colors) > 0


# Filters for use with Python's logging module.
# These are intended for use by application code; tornado.access and
# tornado.application provide filters specific to those loggers.


# Generated at 2022-06-14 12:37:32.170241
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.options import define, options

    logger = logging.getLogger()
    msg = "test enable_pretty_logging"
    define("log_file_prefix", "test.log")
    define("log_to_stderr", True)
    enable_pretty_logging(options, logger)

    try:
        logger.info(msg)
        logger.warning(msg)
        logger.error(msg)
        logger.critical(msg)
        assert(False)
    except AttributeError as e:
        assert(True)


# Generated at 2022-06-14 12:37:43.310395
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    #testing LogFormatter.__init__ with datefmt, colors
    import tornado.log
    formatter = tornado.log.LogFormatter(datefmt='%Y-%m-%d %H:%M:%S', colors={10:1, 20:2})
    assert formatter._fmt == "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s"
    assert formatter._colors == {10: "\x1b[2;31m", 20: "\x1b[2;32m"}
    assert formatter._normal == "\x1b[0m"
    #testing LogFormatter.__init__ with colors
    formatter = tornado.log.LogFormatter(colors={10:1, 20:2})


# Generated at 2022-06-14 12:37:46.260982
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # prepare
    record = {}
    record["getMessage"] = lambda: "message"
    record["levelno"] = logging.ERROR
    record["__dict__"] = {
        "levelname": "ERROR",
        "asctime": "asctime",
        "module": "module",
        "lineno": 123,
    }
    logf = LogFormatter(colors = {})
    # execute
    res = logf.format(record)
    # verify
    assert res == "[E asctime module:123] message"



# Generated at 2022-06-14 12:37:49.074709
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s\t%(message)s')
    logging.debug("This is a test log.")


# Generated at 2022-06-14 12:37:50.845479
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    """ method:test_LogFormatter_format
    """
    pass



# Generated at 2022-06-14 12:38:01.652070
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # First test the function with no arguments
    enable_pretty_logging()
    # Second test the function with log_to_stderr = True
    options = tornado.options.options
    options.log_to_stderr = True
    enable_pretty_logging()
    # Third test the function with log_to_stderr = None and no current logger
    options.log_to_stderr = None
    logger = logging.getLogger()
    logger.addHandler(logging.NullHandler())
    enable_pretty_logging(logger=logger)
    options.log_to_stderr = None
    logger = logging.getLogger()
    enable_pretty_logging(logger=logger)
    # Fourth test the function with log_to_stderr = False and log_file_prefix

# Generated at 2022-06-14 12:39:39.972260
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    class Record():
        pass
    record = Record()

# Generated at 2022-06-14 12:39:51.180229
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import logging


# Generated at 2022-06-14 12:39:53.279226
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter().datefmt == LogFormatter.DEFAULT_DATE_FORMAT  # type: ignore
    assert LogFormatter(color=False)._normal == ""



# Generated at 2022-06-14 12:39:57.359547
# Unit test for function define_logging_options
def test_define_logging_options():
    from tornado.options import define, options, parse_command_line, parse_config_file
    import tornado.options
    from tornado.util import b
    # Basic test that the log flag is present in the default options instance.
    #
    # We can't test the default itself (it changes depending on whether
    # there's a tty) -- use a parsing option to ensure it is present and
    # not None.
    define("log_to_stderr")
    parse_command_line()
    assert options.log_to_stderr is not None
    # Exercise the flag a bit.
    options.log_to_stderr = False
    assert not options.log_to_stderr
    options.log_to_stderr = True
    assert options.log_to_stderr
    del options.log_

# Generated at 2022-06-14 12:40:08.060933
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options = tornado.options.define("log_file_prefix", type=str, 
                                                default='', help="")
    tornado.options.options = tornado.options.define("log_rotate_mode", type=str, 
                                                default='time', help="")
    tornado.options.options = tornado.options.define("log_file_max_size", type=int, 
                                                default=1024, help="")
    tornado.options.options = tornado.options.define("log_file_num_backups", type=int, 
                                                default=8, help="")

    tornado.options.options = tornado.options.define("log_rotate_when", type=str, 
                                                default='D', help="")

# Generated at 2022-06-14 12:40:16.153645
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class Options(object):
        logging = None # type: str
        log_file_prefix = None # type: str
        log_rotate_mode = 'time' # type: str
        log_file_num_backups = None # type: int
        log_rotate_when = None # type: str
        log_rotate_interval = None # type: int
        log_to_stderr = None # type: str
    options = Options()
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:40:21.402711
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    instance = LogFormatter(datefmt='%Y-%m-%d %H:%M:%S')
    assert instance._fmt == LogFormatter.DEFAULT_FORMAT
    assert instance.datefmt == '%Y-%m-%d %H:%M:%S'

LogFormatter.test = test_LogFormatter
del test_LogFormatter



# Generated at 2022-06-14 12:40:22.846614
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options.parse_command_line()
    enable_pretty_logging(options)
    assert True

# Generated at 2022-06-14 12:40:35.169532
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    class CustomLogFormatter(LogFormatter):
        DEFAULT_DATE_FORMAT = "%y%m%d %H:%M:%S"

    # If we have colormap, the color of a message should be set
    colormap = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    # If we do not have colormap, the color should not be set
    empty_colormap = {}
    # The message can be a str
    message = "message"
    # The message can be a bytes
    message_bytes = b"message"
    # The message can

# Generated at 2022-06-14 12:40:41.406782
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class Options:
        log_file_prefix = 'test/test.log'
        log_file_max_size = '10240'
        log_file_num_backups = '5'
        log_rotate_mode = 'size'
        log_rotate_when = 'D'
        log_rotate_interval = '1'
        logging = 'DEBUG'
    options = Options()
    logging.debug("Test unit test for function enable_pretty_logging")
    enable_pretty_logging(options)