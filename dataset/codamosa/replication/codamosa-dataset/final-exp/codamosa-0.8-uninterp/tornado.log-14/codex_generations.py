

# Generated at 2022-06-14 12:31:03.794594
# Unit test for function define_logging_options
def test_define_logging_options():
    import tornado.options
    import unittest
    import os

    class LoggingTest(unittest.TestCase):
        def test_logging(self):
            old_stdout = sys.stdout
            sys.stdout = open("test.log", "w")
            define_logging_options(tornado.options.options)
            tornado.options.parse_command_line(
                [
                    "--log_file_prefix=test",
                    "--log_rotate_when=midnight",
                    "--log_rotate_interval=10",
                    "--log_file_num_backups=5",
                    "--log_file_max_size=10000",
                    "--log_rotate_mode=size",
                ]
            )
            logger = logging.getLogger()

# Generated at 2022-06-14 12:31:05.772467
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()

if __name__ == "__main__":
    test_LogFormatter()

# Generated at 2022-06-14 12:31:08.753791
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: Any -> None
    from tornado.log import LogFormatter
    from tornado.options import options
    options.log_file_prefix = "test.log"
    formatter = LogFormatter()

test_LogFormatter()


# Generated at 2022-06-14 12:31:10.417705
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)



# Generated at 2022-06-14 12:31:20.821166
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    # test for all the sizes of log messages
    for size in range(20, 1024 * 1024 * 5, 1024 * 1024):
        options = tornado.options.parse_command_line(
            ["test", "--log_rotate_mode=size", "--log_file_prefix=test-%d" % size]
        )
        enable_pretty_logging(options)

        s = "x" * size
        gen_log.warning(s)
        gen_log.error(s)
        gen_log.info(s)


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:23.124069
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import doctest
    import micromono.log
    doctest.run_docstring_examples(micromono.log.LogFormatter.format, globals())


# Generated at 2022-06-14 12:31:33.837355
# Unit test for method format of class LogFormatter

# Generated at 2022-06-14 12:31:44.911506
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(color=True)
    LogFormatter(color=False)
    LogFormatter(color=False,
                 fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s")  # noqa: E501
    LogFormatter(color=True,
                 fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s")  # noqa: E501


# Set up color if we are in a tty and curses is installed

# Generated at 2022-06-14 12:31:56.861233
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import os
    import tempfile
    import tornado.options

    def check_pretty_logging(
            log_file_prefix:str = None,
            log_rotate_mode:str = None,
            log_file_num_backups:str = None):
        enable_pretty_logging(logger=gen_log)
        gen_log.info("info")
        enable_pretty_logging(
            options=tornado.options.OptionParser().parse_args(
                ["--logging=debug"]),
            logger=gen_log)
        gen_log.info("debug")
        fd, log_file = tempfile.mkstemp()
        os.close(fd)

# Generated at 2022-06-14 12:32:02.886776
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import time
    import datetime
    from tornado.util import _time_format

    now = datetime.datetime.utcnow()
    t = time.mktime(now.timetuple())
    time.sleep(0.001)
    f = LogFormatter()
    output = f.formatTime(
        logging.LogRecord(
            "tornado.test", logging.INFO, None, 0, "", "", "", 0),
        _time_format(now),
    )
    assert output.startswith(str(now.year))

# Generated at 2022-06-14 12:32:33.910985
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logFormatter = LogFormatter()
    assert logFormatter is not None


# Generated at 2022-06-14 12:32:36.336023
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_formatter = LogFormatter()
    assert log_formatter.format("a") == "a"

# Generated at 2022-06-14 12:32:38.109027
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:32:48.857076
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()

    record = logging.LogRecord("name", logging.INFO, "path", 10,
                               "msg", (), None)
    record.asctime = "0000-00-00 00:00:00"
    record.color = "\x1b[2;37m"
    record.end_color = "\x1b[0m"

    # unit test without exc_info
    message = formatter.format(record)
    assert message == "\x1b[2;37m[I 0000-00-00 00:00:00 path:10]\x1b[0m msg"

    # unit test with exc_info
    record.exc_info = ("val_exc_info", "val_exc_info2")
    formatter.format(record)

# Generated at 2022-06-14 12:33:00.515197
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    import tornado.options
    import logging.config
    import logging

    logging.config.dictConfig(
        {"version": 1, "disable_existing_loggers": False, "formatters": {}}
    )
    for color in [False, True]:
        formatter = LogFormatter(color=color)
        if color:
            assert formatter._colors[logging.CRITICAL]
        else:
            assert formatter._normal == ""

    formatter = LogFormatter(color=True, colors={logging.INFO: 2})
    assert formatter._colors[logging.INFO] == "\033[2;3%dm" % 2
    assert formatter._normal == "\033[0m"

    tornado.options.options.logging = "none"
    formatter = LogFormatter

# Generated at 2022-06-14 12:33:03.229903
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.options=tornado.options.options
    options= tornado.options.options
    
if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:33:08.907457
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter(color=True, colors={logging.WARNING: 1})
    assert isinstance(lf, LogFormatter)
    assert isinstance(lf._colors, dict)
    assert lf._colors.keys() == {logging.WARNING}
    assert isinstance(lf._colors[logging.WARNING], unicode_type)
    assert lf._normal == "\033[0m"

# TODO: Set up color by default for `logging.StreamHandler` (and other
# `logging.Handler`s?).



# Generated at 2022-06-14 12:33:15.494867
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(datefmt="%Y-%m-%d %H:%M:%S", color=False)
    class record(object):
        levelno = 1
        asctime = "2017-02-01 21:23:56"
        message = "Hi, I am an error message"
    assert formatter.format(record) == "[E 2017-02-01 21:23:56 <unknown>:-1] Hi, I am an error message"


# Generated at 2022-06-14 12:33:19.763047
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert type(lf) == LogFormatter
    assert lf.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    assert lf._normal == ""



# Generated at 2022-06-14 12:33:26.705313
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    stderr_supports_color = _stderr_supports_color()
    access_log_formatter = LogFormatter(color=True)
    app_log_formatter = LogFormatter(color=False)
    gen_log_formatter, stderr_formatter = LogFormatter(), LogFormatter()
    record = logging.LogRecord("name", 1, "pathname", 1, "msg", {}, None)
    access_log_formatter.format(record)
    app_log_formatter.format(record)
    gen_log_formatter.format(record)
    stderr_formatter.format(record)
    record.levelno = logging.WARNING
    access_log_formatter.format(record)
    app_log_formatter.format(record)
    gen_log_form

# Generated at 2022-06-14 12:33:54.816801
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    # get options but do not parse_command_line
    # parse_command_line will call this function
    options = tornado.options.options
    options.log_to_stderr = True
    options.log_file_prefix = 'test.log'
    options.log_rotate_mode = 'time'
    options.log_rotate_when = 'S'
    options.log_rotate_interval = 1
    options.log_file_num_backups = 3

    enable_pretty_logging(options)

    # get logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logger.debug("1.This is a debug log")
    logger.info("2.This is a info log")

# Generated at 2022-06-14 12:34:00.710312
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import io
    tornado.options.define("log_file_prefix", default = 'logging.out')
    tornado.options.define("logging", default = 'none')
    enable_pretty_logging()
    # enable_pretty_logging()
    # tornado.options.parse_config_file(conf_file)
    # tornado.options.parse_command_line()
    # enable_pretty_logging()
    logging.error("test error")
    # print(sys.stdout)

# Generated at 2022-06-14 12:34:09.641315
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging

    options = tornado.options.parse_command_line(["--logging=debug"])

    assert options.logging.lower() == "debug"

    enable_pretty_logging(options, logging.getLogger())

    assert len(logging.getLogger().handlers) == 2

    channel = logging.handlers.RotatingFileHandler(
        filename=options.log_file_prefix,
        maxBytes=options.log_file_max_size,
        backupCount=options.log_file_num_backups,
        encoding="utf-8",
    )


# Generated at 2022-06-14 12:34:21.779490
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line
    define("logging", type=str, default="info", help=("Set the Python log level. "))
    options.log_file_prefix = "test_log"
    options.log_to_stderr = False
    options.log_rotate_mode = "time"
    options.log_rotate_when = "midnight"
    options.log_rotate_interval = 1
    options.log_file_num_backups = 10
    parse_command_line(["--log_file_prefix="])#test log file
    enable_pretty_logging()
    raise Exception("test")#test raise exception
test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:29.814232
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert not formatter._normal
    assert not formatter._colors
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT

    formatter = LogFormatter("%(message)s", "%Y-%m-%d", style="{")
    assert formatter._fmt == "%(asctime)s %(message)s"
    assert formatter.datefmt == "%Y-%m-%d"



# Generated at 2022-06-14 12:34:43.433073
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    from tornado.log import LogFormatter
    class Test(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False
            self.stream = open('test.log', 'w')
            self.handler = logging.StreamHandler(self.stream)
            self.handler.setFormatter(LogFormatter())
            self.logger.addHandler(self.handler)
        def test_format(self):
            self.logger.error('an error message')
            self.logger.warning('a warning message')
            self.logger.info('a info message')

# Generated at 2022-06-14 12:34:45.194862
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter



# Generated at 2022-06-14 12:34:52.473395
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.LogRecord(
        name="tornado.access",
        level=logging.DEBUG,
        pathname=__file__,
        lineno=38,
        msg="test message",
        args=(),
        exc_info=None,
    )
    color_formatted = formatter.format(record)
    print(color_formatted)
    assert color_formatted.split(' ')[0] == 'test'
    assert color_formatted.split(' ')[-1] == 'message'

#test_LogFormatter_format()

# TODO: deprecate these and have applications instantiate a
# RotatingFileHandler themselves

# Generated at 2022-06-14 12:35:02.878126
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.util import b

    def _test(format_, *args, **kwargs):
        formatter = LogFormatter(format_, **kwargs)
        # test constructors
        record = logging.LogRecord("dummy", 10, None, None, None, None, None)
        output = formatter.format(record)
        for a in args:
            assert a in output, repr(output)
        return output

    output = _test("%(asctime)s %(message)s")
    assert "dummy" not in output

    output = _test("%(asctime)s %(message)s", "%(message)s", datefmt="%H:%M:%S")
    assert "dummy" not in output


# Generated at 2022-06-14 12:35:05.357248
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert isinstance(f, logging.Formatter)
    assert isinstance(f._fmt, str)



# Generated at 2022-06-14 12:35:45.004097
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.log import gen_log
    from tornado.options import define, options, parse_command_line
    define("logging", None, str)
    define("log_file_prefix", None, str)
    define("log_rotate_mode", "size", str)
    define("log_rotate_when", None, str)
    define("log_rotate_interval", None, int)
    define("log_file_num_backups", None, int)
    define("log_file_max_size", None, int)
    define("log_to_stderr", None, bool)
    parse_command_line(
        ["--logging=debug", "--log_file_prefix=./src/log_file_prefix"]
    )
    enable_pretty_logging()
    gen_log.info

# Generated at 2022-06-14 12:35:56.657010
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    def test_colorama_support():
        """Colorama support is detected correctly."""
        with unittest.mock.patch("sys.stderr", io.StringIO()) as stderr:
            self.assertFalse(_stderr_supports_color())
            self.assertEqual(stderr.getvalue(), "")
        with unittest.mock.patch("sys.stderr", io.StringIO()) as stderr:
            stderr.isatty = lambda: True  # type: ignore
            self.assertFalse(_stderr_supports_color())
            self.assertEqual(stderr.getvalue(), "")

# Generated at 2022-06-14 12:36:07.803905
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Unit test for LogFormatter constructor"""
    # pylint: disable=invalid-name
    fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    datefmt = "%y%m%d %H:%M:%S"
    style = "%"
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }


# Generated at 2022-06-14 12:36:18.193707
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    """Unit tests for LogFormatter class."""
    fmt = LogFormatter()
    assert fmt.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    fmt = LogFormatter(color=False)
    fmt = LogFormatter(color=True)
    assert isinstance(fmt.format(logging.LogRecord(
        "tornado", logging.DEBUG, "foo.py", 1, "hello %s", ("world",), None)), str)
    fmt = LogFormatter(color=False)
    assert isinstance(fmt.format(logging.LogRecord(
        "tornado", logging.DEBUG, "foo.py", 1, "hello %s", ("world",), None)), str)



# Generated at 2022-06-14 12:36:30.364653
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    # Test remove all handler
    logger = logging.getLogger()
    channel = logging.StreamHandler()
    channel.setFormatter(LogFormatter())
    logger.addHandler(channel)
    enable_pretty_logging(tornado.options.options,logger)
    assert len(logger.handlers) == 0
    # Test add .log file handler
    logger = logging.getLogger()
    tornado.options.options.log_file_prefix = f"test.log"
    enable_pretty_logging(tornado.options.options,logger)
    assert len(logger.handlers) == 1
    assert logger.handlers[0].baseFilename == f"test.log"
    tornado.options.options.log_file_prefix = None
    # Test add  sys.stder

# Generated at 2022-06-14 12:36:35.794369
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    enable_pretty_logging()
    log.debug('debug message')
    log.info('info message')
    log.warning('warning message')
    log.error('error message')
    log.critical('critical message')
    

if __name__ == "__main__":
    # test_enable_pretty_logging() default log level:debug
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:39.537533
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter1 = LogFormatter()
    formatter2 = LogFormatter(fmt="%(asctime)s", datefmt="%x")



# Generated at 2022-06-14 12:36:42.918902
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(options=None)


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:51.354197
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    rec = logging.LogRecord("test", logging.INFO, None, 2, "message", {}, None)

    formatter_no_color = LogFormatter(color=False)
    formatter_color = LogFormatter(color=True)

    assert formatter_no_color.format(rec) == (
        "[I " + rec.asctime + " test:2] message"
    )
    assert formatter_color.format(rec) == (
        "[\x1b[32mI \x1b[0m" + rec.asctime + " test:2] message"
    )



# Generated at 2022-06-14 12:36:55.833193
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    print("Call function enable_pretty_logging")
    import tornado.options
    options = tornado.options.options
    options.logging = "none"
    options.log_file_prefix = ""
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:38:08.461632
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    gen_log.info("test_enable_pretty_logging")

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:11.933666
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt.format(logging.LogRecord("x", "INFO", "x.py", 100, "my message", [], None)) == "[I x.py:100] my message"



# Generated at 2022-06-14 12:38:22.062798
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    formatter = LogFormatter(fmt)
    record = logging.LogRecord(
        "tornado.test",
        logging.INFO,
        "/fake/path",
        666,
        "hello",
        None,
        None,
        "foo",
    )
    message = formatter.format(record)
    assert "hello" in message
    assert "\033[0m" in message
    assert "INFO" in message

_TO_UNICODE_TYPES = (unicode_type, type(None))  # type: Any


# Generated at 2022-06-14 12:38:33.131091
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter(color=True, fmt=LogFormatter.DEFAULT_FORMAT)
    gen_log.addHandler(logging.StreamHandler(sys.stdout))
    gen_log.setLevel("DEBUG")
    gen_log.info("test message")
    gen_log.setFormatter(fmt)

test_LogFormatter()

# LogFormatter is used by the default tornado.options parse_command_line
# and parse_config_file, but the standardized logging module API can be
# used directly via standard logging.config calls
dictConfig = logging.config.dictConfig  # type: ignore  # no such attribute

# Default application log


# Generated at 2022-06-14 12:38:43.000468
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    assert fmt.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert fmt.DEFAULT_COLORS == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }

# Generated at 2022-06-14 12:38:53.429309
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Nothing should have changed, so just print the old one.
    # print(LogFormatter.format)

    l = logging.getLogger()
    l.setLevel(logging.DEBUG)
    ll = l.handlers[0]

    msg = "This is a message."
    record = logging.LogRecord("name", logging.DEBUG, "/path/to/file.py", 42, msg, (), None)

    # Nothing should have changed, so just print the old one.
    # print(ll.format(record))

    # The message has changed, print the new one.
    # print(LogFormatter.format)

    l = logging.getLogger()
    l.setLevel(logging.INFO)
    ll = l.handlers[0]

    msg = "This is a message."
    record = logging.Log

# Generated at 2022-06-14 12:39:06.649344
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options, define
    import logging
    import os
    import sys
    import tempfile
    import unittest

    log_file = os.path.join(tempfile.gettempdir(), "tornado_test_log")
    define("log_file_prefix", log_file)

    class LogTest(unittest.TestCase):
        def setUp(self):
            # make sure we start each test with no handlers
            logger = logging.getLogger()
            for h in list(logger.handlers):
                logger.removeHandler(h)
            for h in list(gen_log.handlers):
                gen_log.removeHandler(h)

        def tearDown(self):
            for h in list(logging.getLogger().handlers):
                h.close()
                logging.get

# Generated at 2022-06-14 12:39:10.480460
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(
        fmt="%(color)s%(message)s%(end_color)s",
        datefmt="%H:%M:%S",
        style="%",
        color=True,
        colors=LogFormatter.DEFAULT_COLORS
    )
    

# Generated at 2022-06-14 12:39:15.001739
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    colored_fmt = LogFormatter(color=True)
    assert isinstance(fmt, logging.Formatter)
    assert isinstance(colored_fmt, logging.Formatter)



# Generated at 2022-06-14 12:39:20.706544
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.log import LogFormatter
    from tornado.log import access_log
    from tornado.log import app_log
    from tornado.log import gen_log
    # Note that the LogFormatter raises error when logging application logs but
    # not access or general log
    try:
        app_log.info("app_log_info")
    except:
        pass
    access_log.info("access_log_info")
    gen_log.info("gen_log_info")
