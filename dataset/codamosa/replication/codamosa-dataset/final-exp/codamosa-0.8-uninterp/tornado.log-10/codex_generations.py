

# Generated at 2022-06-14 12:31:15.663433
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Test to make sure that the logging is enabled.
    import tornado.options
    import tornado.options
    options = tornado.options.options
    options.define("log_to_stderr", type=bool, default=True)
    options.define("log_file_prefix", type=str, default=None)
    options.logging = 'debug'
    # Log something so that it is printed on the screen
    gen_log.warning('Tornado logging test')

# Generated at 2022-06-14 12:31:24.612648
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # NOTE: tornado.log is global...
    tornado.log.enable_pretty_logging()
    assert tornado.log.access_log.level == logging.INFO
    assert tornado.log.app_log.level == logging.INFO
    assert tornado.log.gen_log.level == logging.INFO
    assert tornado.log.access_log.handlers == tornado.log.app_log.handlers
    assert tornado.log.access_log.handlers == tornado.log.gen_log.handlers
    assert tornado.log.app_log.handlers == tornado.log.gen_log.handlers
    assert tornado.log.access_log.handlers



# Generated at 2022-06-14 12:31:34.773578
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    log_formatter = LogFormatter()
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)
    logger.info('string msg')
    logger.info('unicode_msg 编码'.encode('utf-8'))
    logger.info('non_unicode_msg 编码'.decode('utf-8'))
    logger.info(bytearray('unicode_msg 编码'.encode('utf-8')))

# Generated at 2022-06-14 12:31:45.762263
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    stream = sys.stderr
    level = logging.DEBUG
    fmt = "[%(levelname)s %(asctime)s] %(message)s"
    datefmt = "%y%m%d %H:%M:%S"

    formatter = LogFormatter(fmt=fmt, datefmt=datefmt)
    logrecord = logging.LogRecord(
        name="tornado.general",
        level=level,
        pathname=__file__,
        lineno=5,
        msg="To be logged",
        args=(),
        exc_info=None,
        func=None,
    )
    msg = formatter.format(logrecord)
    assert msg == "[DEBUG %s] To be logged" % logrecord.asctime, "It's not correct!"


# Generated at 2022-06-14 12:31:54.294982
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # noqa: F811
    try:
        logging.StreamHandler().createLock()
    except NotImplementedError:
        log_handler = logging.handlers.DummyHandler()
    else:
        log_handler = logging.StreamHandler()
    formatter = LogFormatter()
    log_handler.setFormatter(formatter)
    gen_log.addHandler(log_handler)
    gen_log.setLevel(logging.DEBUG)
    gen_log.debug("test debug")
    gen_log.info("test info")
    gen_log.warning("test warning")
    gen_log.error("test error")
    gen_log.critical("test critical")
    gen_log.removeHandler(log_handler)


# Generated at 2022-06-14 12:31:55.422699
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:32:08.959466
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # setUp
    # set tornado option
    import tornado.options
    tornado.options.options.logging = None
    # function under test
    enable_pretty_logging(tornado.options.options)
    # assert
    assert(tornado.options.options.logging == None)
    assert(logging.getLogger().level == logging.NOTSET)
    # setUp
    # set tornado option
    import tornado.options
    tornado.options.options.logging = "debug"
    logging.getLogger().handlers.clear()
    # function under test
    enable_pretty_logging(tornado.options.options)
    # assert
    assert(tornado.options.options.logging == "debug")
    assert(logging.getLogger().level == logging.DEBUG)
    # setUp
   

# Generated at 2022-06-14 12:32:13.705465
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logging.basicConfig(level=logging.DEBUG)
    formatter = LogFormatter()
    formatter.format(logging.LogRecord(
        'test_LogFormatter_format', logging.DEBUG, '', 1, 'message', (), None))

# Generated at 2022-06-14 12:32:19.097598
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = parse_config_file("./log.cfg")
    enable_pretty_logging(options)

# Read the configuration file
test_enable_pretty_logging()

gen_log.info("Tornado server starting...")
app_log.warning("Tornado application starting...")

# Generated at 2022-06-14 12:32:28.150428
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # noqa: F811
    access_log = logging.getLogger("tornado.access")
    access_log.propagate = 0
    access_log.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = LogFormatter()
    handler.setFormatter(formatter)
    access_log.addHandler(handler)
    access_log.info("test")
    access_log.removeHandler(handler)
    access_log.handlers = [handler]
    access_log.info("test")
    access_log.removeHandler(handler)



# Generated at 2022-06-14 12:32:45.686375
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._normal == ""
    assert LogFormatter()._colors == {}
    assert LogFormatter()._fmt == LogFormatter.DEFAULT_FORMAT
    assert LogFormatter().datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert LogFormatter(
        fmt="%(message)s", datefmt="%Y%m%d %H:%M:%S"
    )._fmt == "%(message)s"
    assert LogFormatter(
        fmt="%(message)s", datefmt="%Y%m%d %H:%M:%S"
    ).datefmt == "%Y%m%d %H:%M:%S"
    assert LogFormatter(color=False)._colors == {}

# Generated at 2022-06-14 12:32:54.988955
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # Check that the constructor has been updated correctly for the
    # logging.Formatter signature.
    LogFormatter(None)

    # Check that the basic functionality is there.
    formatter = LogFormatter()
    record = logging.LogRecord(
        "name", logging.INFO, "/path/to/file.py", 123, "msg", args=(), exc_info=None
    )
    result = formatter.format(record)
    assert isinstance(result, str)
    assert result.startswith('[I ')
    assert result.endswith('] msg')



# Generated at 2022-06-14 12:33:01.560944
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.options import options, parse_config_file, parse_command_line

    parse_command_line(['tornado', '--logging=info'])
    log = logging.getLogger("test_LogFormatter")
    log.debug("test")
    expected = "[D 100101 01:23:45 test_LogFormatter:0] test"
    import os
    os.unlink(options.log_file_prefix + "-debug.log")


# Generated at 2022-06-14 12:33:09.854125
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test

    class LoggingTestCase(AsyncTestCase):
        def setUp(self):
            super(LoggingTestCase, self).setUp()
            self.port = bind_unused_port()[1]
            self.io_loop.add_callback(self.stop)
            self.io_loop.start()
            self.io_loop.stop()

    @gen_test
    def test_log_file_prefix(self):
        options = tornado.options.options
        options.logging = "debug"
        options.log_file_prefix = self.get_temp_file("log")
        options.log_file_max_size = 100
        options.log_file_num_backups = 1


# Generated at 2022-06-14 12:33:10.974331
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
  fmt = LogFormatter()


# Generated at 2022-06-14 12:33:12.479244
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    LogFormatter(color=False)


# Generated at 2022-06-14 12:33:23.935897
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()

# Setup color if we are in a tty and curses is installed
if (
    _stderr_supports_color()
    and curses is not None
    and logging.getLogger().handlers
    and not logging.getLogger().handlers[0].stream.isatty()
):
    # The curses module is only used to determine if the terminal supports
    # color; we do not need the enhanced functionality provided by the
    # curses.wrapper function.
    curses.setupterm()

# Generated at 2022-06-14 12:33:31.580710
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Unit test for LogFormatter class.
    """
    LogFormatter()
    LogFormatter(color=False)
    LogFormatter(color=True)
    LogFormatter(color=True, fmt="%(message)s", datefmt="%H:%M", style="{")
    LogFormatter(color=True, fmt="%(message)s", datefmt="%H:%M", style="{")

# Generated at 2022-06-14 12:33:33.916014
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert log_formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert log_formatter._colors == LogFormatter.DEFAULT_COLORS
    assert log_formatter._normal == ""



# Generated at 2022-06-14 12:33:39.230186
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = Options()
    options.logging = "info"
    options.log_file_prefix = "tornado.txt"
    options.log_file_max_size = 1024
    options.log_file_num_backups = 2
    options.log_to_stderr = True
    options.log_rotate_mode = "size"
    options.log_rotate_when = "W0"
    options.log_rotate_interval = 1
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:33:56.990645
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import logging
    import logging.handlers
    import sys

    root = logging.getLogger()

    record = logging.makeLogRecord({'args': (), 'exc_info': None, 'func': None, 'created': 1424682711.18, 'filename': '', 'exc_text': None, 'pathname': '', 'module': None, 'msecs': 181.8, 'levelname': 'ERROR', 'lineno': None, 'threadName': 'MainThread', 'name': 'tornado.general', 'msg': 'blah', 'levelno': 40, 'process': 15368})
    formatter = LogFormatter()
    stream = sys.stdout
    formatter.formatTime(record)
    formatter.formatTime(record, '%Y')
    formatter.formatMessage(record)
    formatter.format

# Generated at 2022-06-14 12:34:00.532014
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():

    enable_pretty_logging()


__all__ = ("gen_log", "app_log", "access_log", "LogFormatter", "enable_pretty_logging")

# Generated at 2022-06-14 12:34:01.908109
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt is not None



# Generated at 2022-06-14 12:34:03.273301
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter(datefmt="%H:%M")



# Generated at 2022-06-14 12:34:05.009260
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logformatter = LogFormatter()
    assert isinstance(logformatter, logging.Formatter)

# Generated at 2022-06-14 12:34:12.027495
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    class MockRecord(object):
        def __init__(self, message, levelno) -> None:
            self.message = message
            self.levelno = levelno
            self.exc_info = ()  # type: Optional[Any]
            self.exc_text = ""  # type: str
    format_record = LogFormatter().format
    assert format_record(MockRecord(b'b"xyz"', logging.INFO)) == '[I 140707 11:10:09 -] b"xyz"'
    assert format_record(MockRecord(b'b"xyz"', logging.DEBUG)) == '[D 140707 11:10:09 -] b"xyz"'

# Generated at 2022-06-14 12:34:25.311877
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import unittest

    # Simple unit test for injection by constructor
    class TestLogFormatter(unittest.TestCase):
        def setUp(self) -> None:
            self.log_formatter = LogFormatter(
                fmt="%(color)s%(levelname)s %(message)s%(end_color)s",
                colors={
                    logging.WARNING: 41,  # Red background
                    logging.ERROR: 42,  # Green background
                    logging.CRITICAL: 43,  # Yellow background
                },
            )

        def test_custom_colors(self) -> None:
            record = logging.makeLogRecord({"levelno": logging.WARNING})
            # pylint: disable=protected-access

# Generated at 2022-06-14 12:34:29.521096
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    def my_func():
        import tornado.options

        options = tornado.options.options
        options.logging = "info"
        enable_pretty_logging(options)
        logger = logging.getLogger("tornado.access")
        logger.info("booday")

    my_func()

# Generated at 2022-06-14 12:34:43.344204
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    expected_formatted = "[C\\n 160612 20:38:14 test_logging:16] \\n    message"
    record = logging.makeLogRecord(dict(msg="message", created=1465825094))
    record.name = "test_logging"
    record.module = "test_logging"
    record.funcName = "test_LogFormatter"
    record.lineno = 16
    record.levelno = logging.CRITICAL
    record.exc_info = (None, None, None)
    record.exc_text = None
    assert LogFormatter(
        fmt="[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]\\n    %(message)s"
    ).format(record) == expected_formatted

# Generated at 2022-06-14 12:34:44.439211
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    pass



# Generated at 2022-06-14 12:34:52.805871
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    enable_pretty_logging('foo.log')

# Generated at 2022-06-14 12:34:54.297684
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # fmt: off
    enable_pretty_logging()
    # fmt: on

# Generated at 2022-06-14 12:35:04.002895
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_config_file
    from io import StringIO
    import os
    buf = StringIO()
    define("log_file_prefix", type=str, default=None)
    define("logging", type=str, default=None)
    define("log_rotate_mode", type=str, default=None)
    define("log_file_num_backups", type=int, default=None)
    define("log_file_max_size", type=int, default=None)
    define("log_rotate_when", type=str, default=None)
    define("log_rotate_interval", type=int, default=None)
    define("log_to_stderr", type=bool, default=None)

# Generated at 2022-06-14 12:35:15.649947
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log

    import tornado.testing

    tornado.testing.gen_test(test_enable_pretty_logging)
    # Set logging options
    class LoggingOptions(object):
        def __init__(self) -> None:
            self.logging = "DEBUG"
            self.log_file_prefix = "test_log"
            self.log_file_max_size = 10485760
            self.log_file_num_backups = 5
            self.log_to_stderr = True

    logging_options = LoggingOptions()
    # Set options
    tornado.log.enable_pretty_logging(options=logging_options)
    # Get the current logger
    logger = logging.getLogger()
    # Check if the current logger is enabled

# Generated at 2022-06-14 12:35:22.831349
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    msg = LogFormatter()
    msg.format("[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s")
    msg.formatTime("[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s", "%y%m%d %H:%M:%S")
    msg.formatException("[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s")


# Generated at 2022-06-14 12:35:30.017756
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.logging = "debug"
    options.log_file_prefix = "test.log"
    options.log_rotate_mode = "time"
    options.log_rotate_when = "D"
    options.log_rotate_interval = 1
    options.log_file_num_backups = 5
    logger = logging.getLogger()
    enable_pretty_logging(options, logger)

# Generated at 2022-06-14 12:35:33.499658
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    assert LogFormatter().format(logging.LogRecord("name", logging.DEBUG, "file.py", 100, "message", args=(), exc_info=None)) == "[D 100200 file.py:100] message"  # noqa: E501


# Generated at 2022-06-14 12:35:35.260214
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # It must be callable
    assert callable(LogFormatter.format)


# Generated at 2022-06-14 12:35:36.169870
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf



# Generated at 2022-06-14 12:35:43.771387
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    import logging
    import logging.handlers
    from tornado.log import LogFormatter, Logger
    #TODO
    #class LogFormatterTest(unittest.TestCase):
    #    def setUp(self):
    #        self.log_handler = logging.handlers.MemoryHandler(100)
    #        self.formatter = LogFormatter()
    #        self.log_handler.setFormatter(self.formatter)
    #        self.formatter.format(logging.getLogger().makeRecord('test-logger', logging.DEBUG, 'test_func', 23, 'test_message', None, None))
    #        self.log_handler.flush()
    #        self.log_record = self.log_handler.buffer[0]
    #        self.formatter

# Generated at 2022-06-14 12:36:06.001874
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado
    tornado.options.parse_command_line()
    logger = logging.getLogger()
    options = tornado.options.options
    options.logging = "debug"
    options.log_file_prefix = "log/tornado"
    options.log_rotate_mode = "size"
    options.log_file_max_size = 10000000
    options.log_file_num_backups = 10
    options.log_to_stderr = False
    enable_pretty_logging(options,logger)


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:14.032444
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    """Test case for LogFormatter."""
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    if _stderr_supports_color():
        formatter = LogFormatter()
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # test that the terminal's reset sequence is called.
        handler.flush = lambda: False
        handler.acquire = lambda: False
        handler.release = lambda: False
        handler.reset = lambda: log.error("reset")
        log.addHandler(handler)

        log.debug("test debug")
        log.warning("test warning")
        log.success("test success")
        log.error("test error")
        log.critical("test critical")



# Generated at 2022-06-14 12:36:25.496247
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    system = LogFormatter.DEFAULT_FORMAT
    fmt = "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s"
    assert system == fmt
    datefmt = "%y%m%d %H:%M:%S"
    assert system == fmt
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    formatter = LogFormatter(fmt, datefmt, "%", color, colors)
    assert formatter.datefmt == datefmt

# Generated at 2022-06-14 12:36:29.206298
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fm = LogFormatter(datefmt='%Y-%m-%d %H:%M:%S', color=True)
    assert fm



# Generated at 2022-06-14 12:36:32.822411
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig()
    enable_pretty_logging()
    logging.info("Hello")
    logging.error("Hello")
    logging.warning("Hello")
if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:36.987417
# Unit test for function define_logging_options
def test_define_logging_options():
    # Unit test for define_logging_options

    # pylint: disable=missing-docstring
    import tornado.options
    import logging
    import random
    import logging.handlers

    tornado.options.define("logging", default="info")
    tornado.options.define("log_file_prefix", default="")
    tornado.options.define("log_file_max_size", default=100 * 1000 * 1000)  # type: ignore
    tornado.options.define("log_file_num_backups", default=10)  # type: ignore
    tornado.options.define("log_rotate_mode", default="size", type=str)  # type: ignore
    tornado.options.define("log_rotate_when", default="midnight", type=str)  # type: ignore

# Generated at 2022-06-14 12:36:38.640944
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert isinstance(LogFormatter(), LogFormatter)


# Generated at 2022-06-14 12:36:44.197230
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.define("logging", default=None)
    tornado.options.define("log_file_prefix", default="None")
    options = tornado.options.options
    logger = logging.getLogger()
    enable_pretty_logging(options, logger)
    return None


# Generated at 2022-06-14 12:36:48.575081
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado.options
    import tornado.log
    tornado.options.define("log_file_prefix", "./log/test.log")
    tornado.options.options.logging = 'info'
    tornado.options.options.log_rotate_mode = "size"
    tornado.options.options.log_file_max_size = 5242880
    tornado.options.options.log_file_num_backups = 5
    tornado.options.options.log_rotate_when = "S"
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_to_stderr = True
    # tornado.log.enable_pretty_logging(tornado.options.options)
    # logging.info("first info log")
    # logging.info("second

# Generated at 2022-06-14 12:37:00.591366
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    def test_colorama(colors: Dict[int, int] = LogFormatter.DEFAULT_COLORS) -> None:
        import logging
        import logging.handlers

        class TestLogFormatter(LogFormatter):
            pass

        logging.raiseExceptions = False
        formatter = TestLogFormatter(color=True, colors=colors)
        log_msg = "colorama test message"
        log_record = logging.LogRecord("colorama.test", logging.ERROR, "", 0, log_msg, None, None)  # noqa: E501
        colored_log_msg = formatter.format(log_record)

        assert colored_log_msg == "\033[2;31m%s\033[0m" % log_msg

        # Check if color is not enabled when stderr is not a tty

# Generated at 2022-06-14 12:37:40.441822
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.root.setLevel(logging.INFO)
    logger = logging.getLogger()

    # Clear handlers
    del logger.handlers[:]
    assert not logger.handlers

    # Set handler for test
    handler = logging.StreamHandler(sys.stderr)
    formatter = LogFormatter(color=False)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("test_LogFormatter - First message")

    # Change datefmt and fmt
    formatter.datefmt = "%Y"
    formatter.fmt = "%(color)s%(levelname)s:%(name)s:%(message)s:%(end_color)s"
    logger.info("test_LogFormatter - Second message")

    # Exception log

# Generated at 2022-06-14 12:37:52.015892
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter._colors == LogFormatter.DEFAULT_COLORS
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT

    formatter2 = LogFormatter(
        color=True,
        fmt="%(asctime)s",
        datefmt="%H:%M:%S",
        colors={
            logging.DEBUG: 7,
            logging.INFO: 6,
            logging.WARNING: 8,
            logging.ERROR: 9,
            logging.CRITICAL: 10,
        },
    )
    assert formatter2.datefmt == "%H:%M:%S"

# Generated at 2022-06-14 12:38:02.349936
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from sys import stdout
    from tornado.options import define, options, parse_command_line
    define("logging", default="debug", help="log level")
    define("log_file_prefix", default="x", help="log file")
    parse_command_line(["--logging=debug", "--log_file_prefix=x"])

    assert LogFormatter()._normal == ''

    # fmt: off
    curses.setupterm(1, 1)  # type: ignore
    curses.tigetstr('setaf')  # type: ignore
    # fmt: on
    args = dict(fmt="%(color)s%(levelname)s%(end_color)s %(message)s")
    formatter = LogFormatter(**args)
    assert formatter._normal != ''

# Generated at 2022-06-14 12:38:08.584963
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter
    formatter.format("ok")  # type: ignore
    formatter.format("ok")  # type: ignore
    formatter.format("ok")  # type: ignore
    formatter.format("ok")  # type: ignore
    formatter.format("ok")  # type: ignore
    LogFormatter.format("ok")  # type: ignore



# Generated at 2022-06-14 12:38:13.906613
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    record = logging.LogRecord("foo", "INFO", None, None, "bar", {}, None)
    f.format(record)  # no error should happen

# Format string for logging the data from request.headers and cookies
# (selected lines only, to avoid huge log files)
REQUEST_LOG_FORMAT = """remote_ip=%s; %s %s %s
       headers=%s
       cookies=%s
"""



# Generated at 2022-06-14 12:38:23.329120
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    with mock.patch("tornado.options.options") as options:
        options.logging = True
        logger = mock.Mock()
        enable_pretty_logging(options, logger)
        assert logger.setLevel.called
        assert logger.addHandler.called
        assert logger.addHandler.call_args[0][0].__class__.__name__ == "RotatingFileHandler"
    with mock.patch("tornado.options.options") as options:
        options.logging = 'test'
        enable_pretty_logging(options)
        enable_pretty_logging()

# Generated at 2022-06-14 12:38:26.901604
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging('none')
    assert(True)

# Generated at 2022-06-14 12:38:28.448915
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(options = None, logger = None)

# Generated at 2022-06-14 12:38:30.663365
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    access_log.info("hello world")

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:38.307688
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line

    define("log_file_prefix", type=str)
    define("log_to_stderr", type=bool)
    define("logging", type=str)
    # Fake parse_command_line
    options.log_file_prefix = "./log/Log.log"
    options.log_to_stderr = True
    options.logging = "debug"
    enable_pretty_logging(options=options)

# Generated at 2022-06-14 12:40:32.742597
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.log import LogFormatter
    log_formatter = LogFormatter(True, True)
    assert isinstance(log_formatter._fmt, str)
    assert isinstance(log_formatter._colors, dict)
    assert isinstance(log_formatter._normal, str)
    assert isinstance(log_formatter.datefmt, str)


# Generated at 2022-06-14 12:40:37.351418
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter(
        fmt="%(levelno) %(a) %(b) %(c) %(d) %(e) %(f) %(g) %(h) %(i) %(j) %(k) %(l) %(m) %(n) %(o) %(p) %(q) %(r) %(s) %(t)"
    )
    rec = logging.LogRecord("name", "info", __file__, 1, "", [], None)
    rec.a = 123
    rec.b = "asdf"
    rec.c = ["asdf"]
    rec.d = {"asdf": 123}
    rec.e = {"asdf": "asdf"}
    rec.f = (1, 2, 3)