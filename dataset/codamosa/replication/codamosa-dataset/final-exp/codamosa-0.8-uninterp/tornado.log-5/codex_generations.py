

# Generated at 2022-06-14 12:31:16.615266
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.log_rotate_mode = "size"
    options.log_file_prefix = "test_tornado"
    options.log_file_max_size = 100
    options.log_file_num_backups = 10
    enable_pretty_logging(options)
    gen_log.debug("Testing Debug")
    gen_log.info("Testing Info")
    gen_log.warning("Testing Warning")
    gen_log.error("Testing Error")
    gen_log.critical("Testing Critical")
if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:26.751739
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.testing import AsyncTestCase
    from tornado.log import enable_pretty_logging

    enable_pretty_logging()

    class LogFormatterTest(AsyncTestCase):

        def test_stderr_supports_color(self):
            assert _stderr_supports_color()

        def test_safe_unicode(self):
            assert _safe_unicode(b'foo') == 'foo'
            assert _safe_unicode(u'foo') == u'foo'


# Generated at 2022-06-14 12:31:35.883334
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import datetime
    import pytz
    date = datetime.datetime(2013, 10, 19, 18, 12, 6, 801954)
    date = date.replace(tzinfo=pytz.timezone("America/New_York"))
    record = logging.LogRecord(
        name="tornado.test_utils",
        level=logging.INFO,
        pathname="/test/test_utils.py",
        lineno=1337,
        msg="test message",
        args=None,
        exc_info=None,
        func=None,
    )
    record.created = date.timestamp()
    record.msecs = int(record.created % 1000)
    record.process = 42
    record.thread = 43
    formatter = LogFormatter()
    actual = formatter.format(record)

# Generated at 2022-06-14 12:31:37.391334
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:47.130744
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # test case
    import random
    from tornado.log import gen_log
    from tornado.util import ObjectDict
    randomvalue = random.randrange(0, 40)
    # the type of record is ObjectDict
    record = ObjectDict(
        levelno = randomvalue,
        # message = 'aaa',
        exc_info = None,
        exc_text = "",
        asctime = None,
        msg = 'msg',
        args = None,
        levelname = 'level'
    )
    record.name = 'entry'
    record.lineno = randomvalue
    record.module = 'module'
    record.funcName = 'func'
    record.created = randomvalue

    # testing
    a = LogFormatter()
    result = a.format(record)
    gen_log.info

# Generated at 2022-06-14 12:31:52.344620
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter._colors == {}
    assert formatter._normal == ""


# Following two classes are copy & paste from python logging module
# and modified by adding name & module parameters to findCaller()
# These are not available in python 2.6 and 3.2


# Generated at 2022-06-14 12:31:53.430043
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log = LogFormatter()



# Generated at 2022-06-14 12:31:54.782594
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: ignore
    assert LogFormatter()._normal == ''


# Generated at 2022-06-14 12:31:56.112137
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()



# Generated at 2022-06-14 12:31:58.471663
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    t = LogFormatter()
    t.format()



# Generated at 2022-06-14 12:32:31.359780
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    """This function test for function enable_pretty_logging
    """
    import tornado.options

    class TestOptions(tornado.options.OptionParser):
        logging = "none"

        log_file_prefix = "D:\\test"

        log_rotate_mode = "size"

        log_file_max_size = 1

        log_file_num_backups = 1

        log_rotate_when = None

        log_rotate_interval = None

        log_to_stderr = True

    options = TestOptions()
    enable_pretty_logging(options)
    assert options is not None
    options.logging = "debug"
    enable_pretty_logging(options)
    assert options is not None
    options.logging = "info"
    enable_pretty_logging(options)


# Generated at 2022-06-14 12:32:42.242301
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, LogFormatter)
    assert isinstance(formatter._colors, dict)
    assert isinstance(formatter._colors.get(logging.DEBUG), str)
    assert isinstance(formatter._colors.get(logging.INFO), str)
    assert isinstance(formatter._colors.get(logging.WARNING), str)
    assert isinstance(formatter._colors.get(logging.ERROR), str)
    assert isinstance(formatter._colors.get(logging.CRITICAL), str)
    assert isinstance(formatter._normal, str)



# Generated at 2022-06-14 12:32:43.292360
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:32:52.453177
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # https://github.com/tornadoweb/tornado/issues/2351
    # Simulates behavior of calling init() directly
    # (which is not normally needed)
    fmt = LogFormatter()
    assert fmt.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501


# Generated at 2022-06-14 12:33:02.367941
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class Record(object):
        __slots__ = ("message", "asctime", "color", "end_color", "levelno",
                     "exc_info", "exc_text", "__dict__")
        def __init__(self, message: str = "") -> None:
            self.message = message
            self.asctime = ""
            self.color = ""
            self.end_color = ""
            self.levelno = 0
            self.exc_info = None  # type: Optional[Exception]
            self.exc_text = ""

    r = Record()
    assert LogFormatter().format(r) == "    "
    r.message = "Test Message"
    assert LogFormatter().format(r) == "    Test Message"



# Generated at 2022-06-14 12:33:03.983733
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter().datefmt == LogFormatter.DEFAULT_DATE_FORMAT



# Generated at 2022-06-14 12:33:07.677392
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    tornado.options.options.log_to_stderr = None
    tornado.options.options.logging = "none"
    tornado.log.enable_pretty_logging()
    tornado.options.options.logging = "none"
    tornado.options.options.log_to_stderr = True
    tornado.log.enable_pretty_logging()

# Generated at 2022-06-14 12:33:13.635708
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # This is not a real unit test; it only ensures that the constructor
    # doesn't raise an exception.
    formatter = LogFormatter()
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter._colors == {}
    assert formatter._normal == ""
    assert formatter.format(logging.makeLogRecord(dict(msg="test"))) == "test"


# Generated at 2022-06-14 12:33:14.692042
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:21.432614
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class Record(object):
        pass
    record = Record()
    assert isinstance(record, object)
    record.asctime = "123"
    record.levelno = 0
    record.message = "test"
    assert isinstance(record.message, basestring_type)
    log_formatter = LogFormatter()
    res = log_formatter.format(record)
    assert isinstance(res, str)

# Generated at 2022-06-14 12:33:30.718599
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()


# Generated at 2022-06-14 12:33:36.405418
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.parse_command_line('--logging=none')
    enable_pretty_logging(tornado.options.options)
    assert tornado.options.options.logging.lower() == "none"
    tornado.options.parse_command_line('--logging=debug')
    enable_pretty_logging(tornado.options.options)
    assert tornado.options.options.logging.lower() == "debug"

# Generated at 2022-06-14 12:33:44.162677
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.options import define, options
    import os
    import time

    test_file_name = 'log_test.log'
    test_file_name2 = 'log_test2.log'
    define("log_file_prefix", test_file_name)
    define("log_rotate_mode", "size")
    define("log_file_max_size", 100)
    define("log_file_num_backups", 3)
    define("log_to_stderr", False)
    define("logging", "info")

    tornado.options.parse_command_line()

# Generated at 2022-06-14 12:33:56.608948
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    log_file_prefix = 'tmp/log/tmp.log'
    import tornado.options
    import os
    import time
    def _empty_file():
        with open(log_file_prefix, 'w'):
            pass
    _empty_file()
    log = logging.getLogger('test_logger')
    tornado.options._options = {
        'logging':'DEBUG',
        'log_file_prefix':log_file_prefix,
        'log_file_max_size':1024,
        'log_file_num_backups':3,
        'log_rotate_mode':'size',
        'log_rotate_when':'H',
        'log_rotate_interval':1,
        'log_to_stderr':1,
    }
    enable_pretty_

# Generated at 2022-06-14 12:33:58.957926
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()

# Generated at 2022-06-14 12:34:05.935371
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    stream = logging.StreamHandler()
    formatter = LogFormatter()
    stream.setFormatter(formatter)

_log_color = {
    logging.DEBUG: "\033[00;32m",  # GREEN
    logging.INFO: "\033[00;36m",  # CYAN
    logging.WARNING: "\033[01;33m",  # BOLD YELLOW
    logging.ERROR: "\033[01;31m",  # BOLD RED
    logging.CRITICAL: "\033[01;31m",  # BOLD RED
}



# Generated at 2022-06-14 12:34:09.372815
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    record = logging.LogRecord(
        "tornado.test", logging.DEBUG, "foo.py", 123, "test test", (), None
    )
    # just make sure we can get through it without an exception
    formatter.format(record)



# Generated at 2022-06-14 12:34:13.731620
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    datefmt: Optional[str] = None
    style: Optional[str] = None
    color: Optional[bool] = None
    colors: Optional[Dict[int, int]] = None
    LogFormatter(datefmt, style, color, colors)



# Generated at 2022-06-14 12:34:27.035537
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from logging import basicConfig, DEBUG, StreamHandler
    from tornado.options import parse_command_line
    from tornado.platform.auto import set_close_exec
    import io

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import socket
    import time

    class _TestHandler(StreamHandler):
        def __init__(self, stream, *args, **kwargs):
            self.stream = stream
            StreamHandler.__init__(self, *args, **kwargs)

        def flush(self):
            self.stream.seek(0)
            lines = self.stream.readlines()
            self.stream.seek(0)
            self.stream.truncate()
            return lines


# Generated at 2022-06-14 12:34:38.979246
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log = logging.getLogger("tornado.test")
    LogFormatter()
    LogFormatter(color=True)
    LogFormatter(color=True, datefmt="%Y-%m-%d %H:%M:%S")
    LogFormatter(color=True, fmt="%(color)s%(message)s%(end_color)s")
    LogFormatter(color=True, fmt="%(color)s%(asctime)s%(end_color)s %(message)s")
    LogFormatter(color=True, fmt="%(message)s")
    LogFormatter(color=True, fmt="%(asctime)s %(message)s")


# Generated at 2022-06-14 12:34:57.376655
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from argparse import Namespace
    from tornado.options import options
    options.logging = 'none'
    enable_pretty_logging()
    assert not gen_log.handlers

    options.logging = 'debug'
    options.log_file_prefix = 'test.log'
    options.log_rotate_mode = 'size'
    options.log_file_num_backups = 10
    options.log_file_max_size = 1024
    options.log_to_stderr = False
    enable_pretty_logging()
    assert len(gen_log.handlers) == 1

    options.log_to_stderr = True
    options.log_rotate_mode = 'time'
    options.log_rotate_when = 'D'

# Generated at 2022-06-14 12:35:02.176057
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()

    # test _fmt
    assert fmt._fmt == LogFormatter.DEFAULT_FORMAT

    fmt = LogFormatter(fmt='A%(color)s%(module)s%(end_color)sA')
    assert fmt._fmt == 'A%(color)s%(module)s%(end_color)sA'

    fmt = LogFormatter(fmt='A%(color)s%(module)sB%(end_color)sA')
    assert fmt._fmt == 'A%(color)s%(module)sB%(end_color)sA'

    # test datefmt
    assert fmt.datefmt == LogFormatter.DEFAULT_DATE_FORMAT

    fmt = LogFormatter(datefmt='A')
    assert fmt

# Generated at 2022-06-14 12:35:10.251419
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    formatter = LogFormatter()
    stream.setFormatter(formatter)
    logger.addHandler(stream)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")



# Generated at 2022-06-14 12:35:17.144817
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class _TestRecord(object):
        def __init__(self, levelno, msg):
            self.levelno = levelno
            self.msg = msg

        def getMessage(self):
            return self.msg

    formatter = LogFormatter()
    assert formatter.format(_TestRecord(logging.INFO, "test")) == (
        "[I {0} gen_log:1] test".format(formatter.datefmt)
    )



# Generated at 2022-06-14 12:35:22.235045
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from typing import Any, Dict, Union
    from logging import LogRecord
    class mylogrecord(LogRecord):
        def __init__(self, x: Union[Any, Dict]) -> None:
            self.__dict__.update(x)
    log = LogFormatter()
    print(log.format(mylogrecord({'levelno':40, 'levelname':'test', 'module':'test1', 'lineno':123})))


# Generated at 2022-06-14 12:35:28.836638
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():

    obj = LogFormatter()
    options = {'logging': 'none', 'log_file_prefix': '',
               'log_rotate_mode': '', 'log_file_max_size': '',
               'log_file_num_backups': '', 'log_rotate_when': '',
               'log_rotate_interval': '', 'log_to_stderr': ''}
    enable_pretty_logging(options)
    print(obj)

# Generated at 2022-06-14 12:35:36.751537
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    class test:
        logging = "debug"
        log_file_prefix = "./options.log"
        log_rotate_mode = "size"
        log_file_max_size = 100
        log_file_num_backups = 3
        log_to_stderr = True
    options = test()
    enable_pretty_logging(options)
    logger = logging.getLogger()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

# Generated at 2022-06-14 12:35:40.282321
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert log_formatter._fmt == LogFormatter.DEFAULT_FORMAT
    log_formatter = LogFormatter(fmt="%(message)s", datefmt="%Y")
    assert log_formatter._fmt == "%(message)s"



# Generated at 2022-06-14 12:35:50.609685
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import unittest
    import re
    import os

    class TestLogFormatter(unittest.TestCase):
        def test_constructor(self):
            # Test that we are able to set the fmt and datefmt arguments
            formatter = LogFormatter(datefmt="%d %H:%M:%S", fmt="%(message)s")
            log_record = logging.LogRecord(
                "name", logging.INFO, "/path/to/file.py", 123, "message", None, None
            )
            self.assertEqual(formatter.format(log_record), "message")

    # If run from the command line, run the tests
    if __name__ == "__main__":
        unittest.main()



# Generated at 2022-06-14 12:36:03.022315
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    f = LogFormatter(fmt)
    r = logging.makeLogRecord({"msg": "test", "levelname": "INFO"})
    s = f.format(r)
    assert s == "\033[0;32m%(levelname)s\033[0m %(message)s"
    f = LogFormatter(fmt, color=False)
    s = f.format(r)
    assert s == "%(levelname)s %(message)s"
    f = LogFormatter(fmt, colors={})
    s = f.format(r)
    assert s == "\033[0;32m%(levelname)s\033[0m %(message)s"
    f

# Generated at 2022-06-14 12:36:20.200994
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:36:31.979693
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    def test(colors: Optional[Dict[int, int]] = None) -> LogFormatter:
        if colors is None:
            colors = LogFormatter.DEFAULT_COLORS
        return LogFormatter(color=False, colors=colors)

    with_colors = test()
    assert with_colors._normal == ""
    assert with_colors._colors == {}

    no_colors = test(colors={})
    assert no_colors._normal == ""
    assert no_colors._colors == {}

    # Check that the color codes are getting set correctly
    curses_colors = test(colors={logging.DEBUG: 4})
    assert curses_colors._colors[logging.DEBUG] == curses.tigetstr("setaf")(4)



# Generated at 2022-06-14 12:36:44.199163
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Verifies that the output messages of class LogFormatter are identical
    # in content and format
    # to the result of the default format() method

    # Create a LogFormatter instance
    formatter = LogFormatter()

    # Create a LogRecord instance
    record = logging.LogRecord(
        name='name', level=logging.INFO, pathname='pathname', lineno=1, msg='msg', args=(), exc_info=None
    )

    # Call the method under test
    output1 = formatter.format(record)

    # Call the default format() method on the same LogRecord instance
    output2 = logging.Formatter().format(record)

    # Compare the two outputs
    assert output1 == output2


# Generated at 2022-06-14 12:36:55.464450
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter: Optional[LogFormatter] = None

# Generated at 2022-06-14 12:37:04.957141
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import unittest

    class TestLogFormatter(unittest.TestCase):
        def test_two_args(self):
            formatter = LogFormatter("%(color)s%(levelname)-8s%(end_color)s %(message)s")
            self.assertIn("%", formatter._fmt)
            self.assertIn("%(color)s", formatter._fmt)
            self.assertIn("%(levelname)-8s", formatter._fmt)
            self.assertIn("%(end_color)s", formatter._fmt)
            self.assertIn("%(message)s", formatter._fmt)


# Generated at 2022-06-14 12:37:16.147884
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options
    options.logging = 'debug'
    options.log_to_stderr = True
    options.log_file_prefix = False
    enable_pretty_logging(options)
    assert logging.getLogger().level == logging.DEBUG
    assert logging.getLogger().handlers
    assert logging.getLogger().handlers[0].formatter.datefmt == '%Y-%m-%d %H:%M:%S'
    logging.getLogger().handlers.clear()

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:26.282969
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import logging.handlers
    tornado.options.options.logging = "debug"
    tornado.options.options.log_file_prefix = r"D:\Temp\test.log"
    tornado.options.options.log_to_stderr = False
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_rotate_when = 'D'
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_file_num_backups = 10
    tornado.options.options.log_file_max_size = 1024
    #logger = logging.getLogger()
    #logger.setLevel('DEBUG')
    enable_pretty_logging()
    #tornado.options.

# Generated at 2022-06-14 12:37:37.982186
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    import tornado.log
    options.define("logging", "info", help="logging level", type=str)
    options.define("log_file_prefix", "blue-log", help="log file", type=str)
    options.define("log_rotate_mode", "time", help="log rotate mode", type=str)
    options.define("log_rotate_when", "S", help="log rotate time", type=str)
    options.define("log_rotate_interval", 1, help="log rotate interval", type=int)
    options.define("log_file_num_backups", 1, help="log file num backups", type=int)
    options.parse_command_line()
    tornado.log.enable_pretty_logging(options)

# Generated at 2022-06-14 12:37:44.602220
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    f = LogFormatter()
    assert f.format(logging.INFO, "Hello world")
    assert f.format(logging.WARNING, "Hello world")
    assert f.format(logging.ERROR, "Hello world")
    assert f.format(logging.CRITICAL, "Hello world")
    assert f.format(logging.INFO, "Hello world\n")
    assert f.format(logging.INFO, "Hello world\nHello world")


# Generated at 2022-06-14 12:37:55.249432
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class MockOptions(object):
        logging = "DEBUG"
        log_file_prefix = "test.log"
        log_rotate_mode = "size"
        log_file_max_size = 1000
        log_file_num_backups = 5
        log_rotate_when = "S"
        log_rotate_interval = 1
        log_to_stderr = True

    import logging
    import logging.config
    import logging.handlers
    from tornado.log import enable_pretty_logging
    from tornado.log import LogFormatter

    logger = logging.getLogger("test")
    assert len(logger.handlers) == 0

    options = MockOptions()
    enable_pretty_logging(options, logger)
    assert len(logger.handlers) == 1
    handlers = logger

# Generated at 2022-06-14 12:38:35.616379
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options
    define("logging", default=None, type=str)
    define("log_rotate_mode", default="time", type=str)
    define("log_to_stderr", default=None, type=bool)
    define("log_file_prefix", default=None, type=str)
    define("log_file_max_size", default=None, type=int)
    define("log_rotate_when", default=None, type=str)
    define("log_file_num_backups", default=None, type=int)
    define("log_rotate_interval", default=None, type=int)
    enable_pretty_logging(options)


if __name__ == "__main__":

    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:44.094418
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import io
    import logging
    import tornado.options
    import unittest

    logging.getLogger("tornado.test").handlers = []
    tornado.options.define("logging", default="none")
    enable_pretty_logging()
    logging.getLogger("tornado.test").info("info")
    self.assertEqual(logging.getLogger("tornado.test").handlers, [])
    tornado.options.define("logging", default="debug")
    tornado.options.options.logging = "debug"
    enable_pretty_logging()
    logging.getLogger("tornado.test").info("info")
    self.assertEqual(len(logging.getLogger("tornado.test").handlers), 1)
    out = io.StringIO()
    logging.getLog

# Generated at 2022-06-14 12:38:54.145941
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # test for the default case:
    # color support and sys.stderr.isatty()
    log_formatter = LogFormatter()
    assert log_formatter._colors
    assert log_formatter._normal

    # test for the case when there is no color support
    # but it is specified in the constructor
    log_formatter = LogFormatter(color=False)
    assert not log_formatter._colors
    assert not log_formatter._normal

    # test for the case when there is no color support
    # and it is not specified in the constructor
    log_formatter = LogFormatter(color=None)
    assert not log_formatter._colors
    assert not log_formatter._normal

    # test for the case when there is color support
    # and it is specified in the constructor
    log_

# Generated at 2022-06-14 12:39:06.798632
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    for handlers in logger.handlers:
        logger.removeHandler(handlers)
    options = type("options", (object,), {"logging": "warn", "log_to_stderr": False})()
    enable_pretty_logging(options)
    assert len(logger.handlers) == 0
    options = type("options", (object,), {"logging": "warn", "log_to_stderr": True})()
    enable_pretty_logging(options)
    assert len(logger.handlers) == 1
    options = type("options", (object,), {"logging": "warn", "log_to_stderr": None})()
    enable_pretty_logging(options)
    assert len(logger.handlers) == 1


# Generated at 2022-06-14 12:39:08.115015
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = Options()
    enable_pretty_logging(options)



# Generated at 2022-06-14 12:39:13.720743
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logf = LogFormatter()
    assert logf
    assert logf.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert logf._colors == LogFormatter.DEFAULT_COLORS
    assert logf._normal == ""
    assert logf._fmt == LogFormatter.DEFAULT_FORMAT


# Generated at 2022-06-14 12:39:14.641826
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
  #TODO
  pass

# Generated at 2022-06-14 12:39:21.691477
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(  # noqa
        fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s",
        datefmt="%y%m%d %H:%M:%S",
        style="%",
        color=True,
        colors={
            logging.DEBUG: 4,  # Blue
            logging.INFO: 2,  # Green
            logging.WARNING: 3,  # Yellow
            logging.ERROR: 1,  # Red
            logging.CRITICAL: 5,  # Magenta
        },
    )


# Generated at 2022-06-14 12:39:26.219078
# Unit test for function define_logging_options
def test_define_logging_options():
    from tornado.options import define, options, print_help

    define_logging_options()

    # print help information
    print_help()

if __name__ == "__main__":
    test_define_logging_options()

# Generated at 2022-06-14 12:39:36.180055
# Unit test for function enable_pretty_logging