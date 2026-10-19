

# Generated at 2022-06-14 12:31:16.709427
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert _stderr_supports_color()

    if colorama:
        colorama.init()

    class Options(object):
        log_file_prefix = None
        log_file_max_size = 500
        log_file_num_backups = 5
        log_rotate_mode = "time"
        log_rotate_when = "S"
        log_rotate_interval = 1
        log_to_stderr = False
        logging = "info"

    try:
        enable_pretty_logging(Options())
        logging.info("test")
    finally:
        logging.error("test")
        logging.getLogger().handlers = []
        if colorama:
            colorama.deinit()

# Generated at 2022-06-14 12:31:26.829700
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    class TestOptions:
        log_file_prefix = "/tmp/test.log"
        log_rotate_mode = "time"
        log_rotate_when = "D"
        log_rotate_interval = 1
        log_file_num_backups = 5
        logging = "ERROR"
        log_to_stderr = False
    tornado.options.options = TestOptions()
    enable_pretty_logging(tornado.options.options, gen_log)
    log_record = logging.LogRecord("tornado", logging.INFO, "./test_logging.py", 10, "test", None, None)
    gen_log.setLevel(logging.INFO)
    gen_log.handlers[0].setFormatter(LogFormatter())

# Generated at 2022-06-14 12:31:30.256395
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging(): # Unit test for function enable_pretty_logging
    enable_pretty_logging()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 12:31:33.600826
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # type: () -> None
    """
    format of LogFormatter
    :return:
    """
    l = LogFormatter(color=False)
    assert isinstance(l, LogFormatter)

# Generated at 2022-06-14 12:31:34.875450
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    LogFormatter()



# Generated at 2022-06-14 12:31:45.835740
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    def f():
        raise ValueError

    import tornado.options
    import tornado.log

    class Options(object):

        logging = "debug"
        log_rotate_mode = "size"
        log_rotate_when = "midnight"
        log_rotate_interval = 1
        log_file_num_backups = 5
        log_file_prefix = "prefix"
        log_file_max_size = 1024 * 1024 * 100
        log_to_stderr = True
        test_mode = True

    tornado.options.define("logging", lambda: None)
    tornado.options.define("log_to_stderr", lambda: False)
    tornado.options.define("log_file_prefix", lambda: None)
    tornado.options.define("log_rotate_mode", lambda: None)

# Generated at 2022-06-14 12:31:54.798823
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.log import LogFormatter
    class FakeLogRecord:
        def __init__(self, level, message, exc_info=None):
            self.levelno = level
            self.exc_info = exc_info
            self.message = message
            self.__dict__ = {}

    class FakeExcInfo:
        def __init__(self, name):
            self.name = name
            self.exc_info = self
            self.__dict__ = {}

    expected = '{"Error": "An error"}'
    def _test_format(kwargs, level, message, exc_info):
        log_formatter = LogFormatter(**kwargs)
        fake_log_record = FakeLogRecord(level, message, exc_info)
        result = log_formatter.format(fake_log_record)
       

# Generated at 2022-06-14 12:32:01.840295
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    if __name__ == "__main__":
        import tornado.options
        tornado.options.define("--logging", default="none", help="")
        tornado.options.define("--log_file_prefix", default="", help="")
        tornado.options.define("--log_to_stderr", default=False, help="")
        tornado.options.define("--log_rotate_mode", default="", help="")
        tornado.options.define("--log_file_max_size", default="", help="")
        tornado.options.define("--log_file_num_backups", default="", help="")
        tornado.options.define("--log_rotate_when", default="", help="")
        tornado.options.define("--log_rotate_interval", default="", help="")


# Generated at 2022-06-14 12:32:06.770048
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert isinstance(lf._fmt, str)
    assert isinstance(lf.datefmt, str)
    assert isinstance(lf._colors, dict)
    assert isinstance(lf._normal, str)



# Generated at 2022-06-14 12:32:12.339631
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.makeLogRecord({"name": "tornado.general", "msg": "test"})
    assert formatter.format(record) == '[I 180918 16:39:40 <unknown>:<unknown>] test'
    record = logging.makeLogRecord({"name": "tornado.general", "msg": "test", "exc_info": "error"})
    assert formatter.format(record) == '[I 180918 16:39:41 <unknown>:<unknown>] test\n    error'


# Generated at 2022-06-14 12:32:25.121548
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # untested
    formatter = LogFormatter()


# Generated at 2022-06-14 12:32:33.782886
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # noqa: F811
    logger = logging.getLogger("demo")
    logger.setLevel(logging.DEBUG)
    # test if the format is default
    if LogFormatter.DEFAULT_FORMAT != "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s":  # noqa: E501
        raise Exception(
            "Test failed in class LogFormatter: expected Default_Format to be %(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s, actual: %s",
            LogFormatter.DEFAULT_FORMAT,
        )

# Generated at 2022-06-14 12:32:37.453701
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 12:32:47.289931
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # pylint: disable=missing-docstring
    formatter = LogFormatter(color=True, fmt='%(color)s%(levelname)s%(end_color)s %(message)s')
    class Record(object):  # pylint: disable=missing-docstring
        __getattr__ = lambda s, k: logging.NOTSET  # type: ignore
        levelno = logging.CRITICAL
        def getMessage(self) -> str:  # pylint: disable=missing-docstring
            return "hello"
    record = Record()  # type: Any
    formatted = formatter.format(record)
    assert formatted == "\x1b[1mCRITICAL\x1b[0m hello"



# Generated at 2022-06-14 12:32:49.815326
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.parse_command_line()
    enable_pretty_logging(logger = gen_log)

# Generated at 2022-06-14 12:32:55.486948
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    colors = {logging.WARNING: 3}
    formatter = LogFormatter(fmt="%(levelname)s %(message)s", colors=colors)
    assert formatter._colors[logging.WARNING] == "\033[2;3%dm" % colors[logging.WARNING]
    assert formatter._normal == "\033[0m"


# Generated at 2022-06-14 12:33:06.847628
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    # Parse commandline
    tornado.options.parse_command_line(["-logging=warning"])
    tornado.log.enable_pretty_logging()
    # Parse config file
    tornado.options.parse_config_file("tests/simple_options.py")
    tornado.log.enable_pretty_logging()

# Generated at 2022-06-14 12:33:07.822912
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    print(formatter)


# Generated at 2022-06-14 12:33:11.549739
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging='info'
    tornado.options.options.log_to_stderr=True
    tornado.options.options.log_rotate_mode='size'
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:23.191525
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import typing
    import logging
    import tornado.log 

    if(
        not isinstance(tornado.log.LogFormatter.DEFAULT_FORMAT, str) or
        not isinstance(tornado.log.LogFormatter.DEFAULT_DATE_FORMAT, str) or
        not isinstance(tornado.log.LogFormatter.DEFAULT_COLORS, typing.Dict)
    ):
        raise Exception("LogFormatter has wrong type")

    test_log = logging.getLogger("test_log")
    test_log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

# Generated at 2022-06-14 12:33:43.030949
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    f = LogFormatter(fmt=fmt)
    # The default colors are from logging.StreamHandler().level_map
    assert f._colors[logging.DEBUG] == "\x1b[0;32m"  # green
    assert f._colors[logging.INFO] == "\x1b[0;36m"  # cyan
    assert f._colors[logging.WARNING] == "\x1b[0;33m"  # yellow
    assert f._colors[logging.ERROR] == "\x1b[0;31m"  # red
    assert f._colors[logging.CRITICAL] == "\x1b[0;35m"  # pink


# Generated at 2022-06-14 12:33:55.569565
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    import os

    class LogFormatterTest(unittest.TestCase):
        def test_LogFormatter(self):
            fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
            datefmt = "%Y-%m-%d %H:%M:%S"
            style = "%"
            color = True
            colors = {
                        logging.DEBUG: 4,  # Blue
                        logging.INFO: 2,  # Green
                        logging.WARNING: 3,  # Yellow
                        logging.ERROR: 1,  # Red
                        logging.CRITICAL: 5,  # Magenta
                    }

            LogFormatter

# Generated at 2022-06-14 12:34:03.117664
# Unit test for function define_logging_options
def test_define_logging_options():
    import tornado.options
    def test_define_logging_options():
        options = tornado.options.options
        options.define(
            "logging",
            default="info",
            help=(
                "Set the Python log level. If 'none', tornado won't touch the "
                "logging configuration."
            ),
            metavar="debug|info|warning|error|none",
        )
        # options.add_parse_callback(lambda: enable_pretty_logging(options))
        # options.logging = 'debug'
        # options.log_to_stderr = True
        # options.log_file_prefix = '/home/ubuntu/tornado_log'
        # options.log_file_max_size = 100000
        # options.log_file_num_backups = 5
        # options.

# Generated at 2022-06-14 12:34:08.633123
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig()
    logging.getLogger().handlers = []
    enable_pretty_logging()
    logger = logging.getLogger()
    assert logger.getEffectiveLevel() == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:11.377285
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = None
    enable_pretty_logging(options)

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:24.596830
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._fmt == LogFormatter.DEFAULT_FORMAT
    assert LogFormatter()._colors == LogFormatter.DEFAULT_COLORS
    assert LogFormatter().datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert LogFormatter(
        fmt="%(asctime)s %(message)s", datefmt="%Y-%m-%d", color=False
    )._fmt == "%(asctime)s %(message)s"
    assert LogFormatter(color=False)._colors == {}
    assert LogFormatter(color=False).datefmt == LogFormatter.DEFAULT_DATE_FORMAT

# Generated at 2022-06-14 12:34:33.940512
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    assert formatter.format("")==""
    assert formatter.format("abc\nabc")=="abc\n    abc"
    assert (formatter.format("[DEBUG 20170101 00:01:02 abc:123] msg") ==
        "[DEBUG 20170101 00:01:02 abc:123] msg")
    assert (formatter.format("[DEBUG 20170101 00:01:02 abc:123] msg\nexc_msg") 
        =="[DEBUG 20170101 00:01:02 abc:123] msg\n    exc_msg")



# Generated at 2022-06-14 12:34:40.703089
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        args = ["--logging=none"]
        options = parse_command_line(args, application=Application)
        assert options.logging.lower() == "none"
    except:
        pass
    try:
        options = parse_command_line(
            ["--logging=debug", "--log_file_prefix=test_enable_pretty_logging.log", '--log_file_max_size=1',
             '--log_file_num_backups=2'], application=Application)
        assert options.log_file_prefix == "test_enable_pretty_logging.log"
    except:
        pass


# Register our custom logger class with logging.getLogger.
# Loggers that don't specify a custom class will use this.
logging.setLoggerClass(LogFormatter)


# Generated at 2022-06-14 12:34:50.111044
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class LogRecord:
        pass

    record = LogRecord()
    record.__dict__ = dict(
        levelno=logging.DEBUG,
        asctime="[TEST]",
        pathname="foo.py",
        filename="foo.py",
        lineno=123,
        funcName="bar",
        module="foo",
        levelname="DEBUG",
        message="hello world",
    )

    # This is pretty ugly, but it's the only way to configure a log
    # Formatter "from the outside"
    record.processName = "foo"

    # Dummy datefmt
    datefmt = "BAD_DATEFMT"

    # Base test
    formatter = LogFormatter(datefmt=datefmt)
    assert isinstance(formatter.datefmt, str) 

# Generated at 2022-06-14 12:35:00.079666
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    datefmt = "%y%m%d %H:%M:%S"
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    record = LogFormatter(fmt, datefmt, color, colors)
    record.format()


# Generated at 2022-06-14 12:35:23.720859
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado.options

    logger = logging.getLogger()
    tornado.options.options.logging = "debug"
    enable_pretty_logging()
    logger.debug("testing")
    logger.info("testing")
    logger.warning("testing")
    logger.error("testing")
    logger.critical("testing")
    tornado.options.options.logging = "none"
    enable_pretty_logging()
    logger.debug("testing")
    logger.info("testing")
    logger.warning("testing")
    logger.error("testing")
    logger.critical("testing")

# Generated at 2022-06-14 12:35:34.398658
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    filename = __file__
    if filename.endswith(".pyc") or filename.endswith(".pyo"):
        filename = filename[:-1]
        # with open(filename, 'rb') as f:
        #     contents = f.read()
    fp = open(filename, 'r')
    contents = fp.read()
    fp.close()

    log_formatter = LogFormatter()
    assert log_formatter.DEFAULT_COLORS == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    assert isinstance(log_formatter._colors, dict)

# Generated at 2022-06-14 12:35:41.992638
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    log = logging.getLogger("tornado.test")
    log.propagate = 0
    log.setLevel(logging.DEBUG)
    # TODO: May need to use a different handler for Colorama
    handler = logging.StreamHandler()
    log.addHandler(handler)

    LogFormatter().__init__(color=False)
    LogFormatter("{asctime} {levelname}: {message}").__init__(color=False)

    LogFormatter().__init__(color=True)
    LogFormatter("{asctime} {levelname}: {message}").__init__(color=True)

use_color = _stderr_supports_color()



# Generated at 2022-06-14 12:35:43.226701
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:35:49.570025
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.LogRecord(
        name='tornado.general',
        level=logging.INFO,
        pathname='/some/path/somefile.py',
        lineno=42,
        msg='some log message',
        args=(),
        exc_info=None
    )
    # Check that formatting can be done without error and returns a str
    result = formatter.format(record)
    assert isinstance(result, str)

# Generated at 2022-06-14 12:36:01.803799
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: () -> None
    import logging
    import logging.handlers
    logger = logging.getLogger('testlogger')
    logger.setLevel(logging.DEBUG)

    fh = logging.handlers.RotatingFileHandler('test.log', maxBytes=100, backupCount=1)
    fh.setLevel(logging.DEBUG)

    # test case: color=True
    fh.setFormatter(LogFormatter(color=True))
    logger.addHandler(fh)
    logger.debug('test debug message')
    logger.info('test info message')
    logger.warning('test warning message')
    logger.error('test error message')
    logger.critical('test critical message')
    fh.close()

    # test case: color=False
    logger.removeHandler(fh)
   

# Generated at 2022-06-14 12:36:02.948555
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()



# Generated at 2022-06-14 12:36:08.702890
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    message = "我喜欢大骆驼啊"
    record = logging.LogRecord(name=None, level=logging.DEBUG, pathname=None, lineno=None,
        msg=message, args=None, exc_info=None)
    formatter = LogFormatter(datefmt=None)
    formatter.format(record)
    assert record.message == message



# Generated at 2022-06-14 12:36:20.344454
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    import tornado.testing
    import yappi

    def test_logformatter_constructor():
        # type: () -> None
        # test calls to __init__ are what they are supposed to be
        f = LogFormatter()
        assert isinstance(f, logging.Formatter)
        g = LogFormatter(fmt="%(asctime)s %(message)s")
        assert isinstance(g, logging.Formatter)
        assert g._fmt == "%(asctime)s %(message)s"

    def test_logformatter_format():
        # type: () -> None
        # test calls to format are what they are supposed to be
        f = LogFormatter()

# Generated at 2022-06-14 12:36:32.167233
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line
    from tornado.log import enable_pretty_logging, app_log

    define("logging", default="info")
    enable_pretty_logging(options)
    assert app_log.getEffectiveLevel() == logging.INFO

    define("logging", default="warning")
    enable_pretty_logging(options)
    assert app_log.getEffectiveLevel() == logging.WARNING

    define("logging", default="none")
    enable_pretty_logging(options)
    assert isinstance(app_log.getEffectiveLevel(), int) and app_log.getEffectiveLevel() > logging.WARNING
    # test the log_file_prefix
    for rotate_mode in ["size", "time"]:
        define("logging", default="info")

# Generated at 2022-06-14 12:36:50.732513
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.parse_command_line()
    enable_pretty_logging()
    gen_log.info('test_enable_pretty_logging')

# Generated at 2022-06-14 12:36:57.498512
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    fmt = LogFormatter(color=True)._fmt
    stream_handler.setFormatter(LogFormatter(color=True))
    logger.addHandler(stream_handler)
    logger.info("info message")
    logger.debug("debug message")


# Generated at 2022-06-14 12:37:00.965459
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: () -> None
    with logging.NullHandler():
        # Constructor of class LogFormatter
        log_format = LogFormatter(fmt="%(color)s%(asctime)s%(end_color)s")


# Generated at 2022-06-14 12:37:13.871721
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # noqa: F811
    class Record(object):
        __init__ = None

    r = Record()  # type: Any
    r.__dict__ = {
        "asctime": "foo",
        "levelname": "bar",
        "lineno": "baz",
        "module": "spam",
        "message": "hello",
    }
    LogFormatter().format(r)
    assert r.message == "hello"
    r.message = b"\xe9"
    assert r.message == "\xe9"
    r.message = None
    try:
        raise ValueError()
    except ValueError:
        r.__dict__["exc_info"] = sys.exc_info()
    LogFormatter().format(r)
    assert r.message.startswith("Bad message")

# Generated at 2022-06-14 12:37:16.028642
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = logging.Formatter()
    fmt = LogFormatter()



# Generated at 2022-06-14 12:37:26.258055
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.StreamHandler()
    # Init LogFormatter with default values
    formatter = LogFormatter()
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.debug("First message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    # Init LogFormatter with fmt as DEFAULT_FORMAT without color
    formatter = LogFormatter(color=False)
    fh.setFormatter(formatter)
    logger.debug("First message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

# Generated at 2022-06-14 12:37:30.042868
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options
    options.log_file_prefix = "tornado"
    options.log_rotate_mode = "time"
    options.log_rotate_when = "D"
    options.log_rotate_interval = 1
    options.log_file_num_backups = 1
    enable_pretty_logging()

# Generated at 2022-06-14 12:37:34.956739
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # test for __init__
    logformatter = LogFormatter()
    assert logformatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert logformatter._colors == {}
    assert logformatter._normal == ""


# Generated at 2022-06-14 12:37:45.268368
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import os
    import logging


# Generated at 2022-06-14 12:37:55.798752
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter(color=False, colors={})._normal == ""
    assert LogFormatter(color=True, colors={})._normal == ""
    assert LogFormatter(color=True, colors={logging.DEBUG: None})._normal == ""
    assert LogFormatter(color=True, colors={logging.DEBUG: 1})._normal == ""
    assert LogFormatter(color=True, colors={logging.DEBUG: 1, logging.INFO: 2})._normal == ""  # noqa: E501

    assert LogFormatter(color=True)._normal == "\033[0m"
    assert LogFormatter(color=True, colors={logging.DEBUG: 1, logging.INFO: 2})._colors[logging.DEBUG] == "\033[2;3%dm"

# Generated at 2022-06-14 12:38:23.227033
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tempfile
    import tornado.options
    import logging
    import shutil
    
    def test_config_files():
        """
        config_files and parse_config_files are test in TestOptionParser
        """
        pass
    
    def test_log_file_prefix():
        log_dir = tempfile.mkdtemp()
        try:
            tornado.options.define("log_file_prefix", type=str,
                default=log_dir + "/test.log",
                help="Path prefix for log files")
            tornado.options.options.log_file_prefix = log_dir + "/test.log"
            enable_pretty_logging(tornado.options.options)
            logging.warning("This is a warning message.")
        finally:
            shutil.rmtree(log_dir)
    
   

# Generated at 2022-06-14 12:38:25.184543
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # just for type check
    formatter = LogFormatter()  # type: ignore


# Generated at 2022-06-14 12:38:31.522887
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    for handler in logger.handlers:
        logger.removeHandler(handler)
    enable_pretty_logging()
    # At the end of this, logging should be different.
    # you can't really check it (the logger argument is optional),
    # but it shows up in strace
    enable_pretty_logging(logger=logger)

# Generated at 2022-06-14 12:38:42.282028
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    import sys
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = LogFormatter()
    stream_handler = logging.StreamHandler(stream = sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.debug("hello world")
    logger.info("hello world")
    logger.warning("hello world")
    logger.error("hello world")
    logger.critical("hello world")
    # unit test result
    # [D 20191202 20:49:59 logger.py:108] hello world
    # [I 20191202 20:49:59 logger.py:109] hello world
    # [W 20191202 20:49:

# Generated at 2022-06-14 12:38:52.923606
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import os
    import tempfile
    import logging
    from tornado.util import b, bytes_type
    from tornado.options import options, define, parse_command_line

    define("flag_1", type=str, default=None, help="")
    define("flag_2", type=str, default=None, help="")
    parse_command_line()

    tmp_dir = tempfile.gettempdir()
    test_file = os.path.join(tmp_dir, "TestLogFormatter_format.txt")
    hdlr = logging.FileHandler(test_file)
    frmt = LogFormatter()
    hdlr.setFormatter(frmt)
    logger = logging.getLogger()
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    logger.info

# Generated at 2022-06-14 12:38:56.192008
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter is not None

# Generated at 2022-06-14 12:39:07.593136
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.testing import AsyncTestCase
    from tornado.options import options, define
    import os
    import logging

    define("logging", default="debug", type=str, metavar="DEBUG|INFO|WARNING|ERROR|CRITICAL|NONE", help="Set the log level")
    define(
        "log_to_stderr",
        default=None,
        type=bool,
        help="Send log output to stderr (colorized if possible). "
        "By default use stderr if --log_file_prefix is not set and "
        "console_log_handler is not set",
    )
    define(
        "log_file_prefix", default=None, type=str, help="Path prefix for log files. "
    )

# Generated at 2022-06-14 12:39:18.569299
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import datetime
    t = datetime.datetime.now()
    record = logging.makeLogRecord({
        "msg": "message",
        "args": (),
        "levelno": logging.DEBUG,
        "exc_info": None,
        "levelname": logging.DEBUG,
        "pathname": "/home/bohai/tornado/tornado",
        "filename": "tornado",
        "module": "tornado",
        "lineno": 12,
        "funcName": "test",
        "created": t.timestamp(),
        "msecs": 0.0,
        "relativeCreated": 0.0,
        "thread": 1,
        "threadName": "MainThread",
        "processName": "MainProcess"
    })
    lf = LogFormatter()
    s = lf

# Generated at 2022-06-14 12:39:30.795372
# Unit test for function define_logging_options
def test_define_logging_options():
    define_logging_options()
    print(options.logging)
test_define_logging_options()

if __name__ == "__main__":
    print(sys.argv)
    print(colorama.initialise)
    print(colorama.initialise.wrapped_stderr)
    def _get_color_by_name(name: str) -> Optional[str]:
        """Returns a tuple of Python console color codes by color name.

        Args:
            name: The color name.

        Returns:
            A tuple of Python console color codes.
        """
        if name is None or not curses:
            return None

        curses.setupterm()

        fg_color = curses.tigetstr(name) or curses.tigetstr(name + " bold")

# Generated at 2022-06-14 12:39:35.945606
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    sys.argv.append("--logging=DEBUG")
    sys.argv.append("--log_file_prefix=logs/log")
    sys.argv.append("--log_rotate_mode=time")
    sys.argv.append("--log_rotate_when=M")
    sys.argv.append("--log_rotate_interval=1")
    sys.argv.append("--log_file_num_backups=15")
    sys.argv.append("--log_to_stderr")
    from tornado.options import options, parse_command_line
    parse_command_line()
    enable_pretty_logging(options)
    app_log.setLevel(options.logging)
    gen_log.setLevel(options.logging)

# Generated at 2022-06-14 12:40:22.197718
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    formatter = LogFormatter(fmt=fmt, color=True)
    assert formatter.usesTime()
    assert formatter._fmt == fmt
    assert formatter._colors == {
        logging.DEBUG: "\033[2;34m",
        logging.INFO: "\033[2;32m",
        logging.WARNING: "\033[2;33m",
        logging.ERROR: "\033[2;31m",
        logging.CRITICAL: "\033[2;35m",
    }
    assert formatter._normal == "\033[0m"


# Generated at 2022-06-14 12:40:23.886116
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()


# Supress the 'has no effect' warning from Pylint
# pylint: disable=unused-argument

# Generated at 2022-06-14 12:40:34.038146
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.log import gen_log
    @gen_test
    def test_enable_pretty_logging():
        def test_logging_options(self):
            options.logging = "info"
            options.log_file_prefix = self.get_temp_file_name()
            options.log_file_max_size = 100
            options.log_file_num_backups = 1
            enable_pretty_logging()
            gen_log.info("test")
            self.assertIn("test", open(options.log_file_prefix).read())


# Generated at 2022-06-14 12:40:42.587680
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    assert formatter.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert formatter.DEFAULT_COLORS == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    assert _stderr_supports_color()
    assert formatter._col