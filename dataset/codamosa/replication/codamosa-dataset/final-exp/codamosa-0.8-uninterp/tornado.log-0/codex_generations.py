

# Generated at 2022-06-14 12:31:12.234068
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_format = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
    fmt = LogFormatter(log_format)
    import time

    class Record(object):
        __slots__ = [
            "levelname",
            "asctime",
            "module",
            "lineno",
            "message",
            "exc_text",
            "exc_info",
        ]

    record = Record()
    record.levelname = "INFO"
    record.asctime = time.strftime('%H:%M:%S')
    record.module = "test"
    record.lineno = 1
    record.message = "A test message."
    record.exc_text = ""
    record.exc_

# Generated at 2022-06-14 12:31:18.841915
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter(fmt="%(asctime)s %(message)s")
    assert lf.format(logging.LogRecord(
        None, None, None, None, "test", None, None)) == \
        'None test'

# Generated at 2022-06-14 12:31:19.469742
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass


# Generated at 2022-06-14 12:31:20.016741
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:28.416249
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    record={'level': 30, 'created': 1430563146880,
            'thread': 140128755859456, 'process': 140128755859456,
            'args': (), 'msg': 'Test', 'module': 'tornado.log',
            'threadName': 'MainThread', 'filename': 'log.py',
            'pathname': '/home/linyuhang/tornado/tornado/log.py', 'lineno': 286,
            'funcName': 'format', 'levelname': 'WARNING',
            'exc_info': None, 'exc_text': None, 'stack_info': None,
            'message': 'Test'}
    log=LogFormatter()
    log.format(record)



# Generated at 2022-06-14 12:31:31.213358
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = 'debug'
    enable_pretty_logging()
    assert logging.getLogger().getEffectiveLevel() == logging.DEBUG


# Generated at 2022-06-14 12:31:38.737464
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from typing import cast

    fmt = '%(color)s[%(levelname)s]%(end_color)s %(message)s'

    lf = LogFormatter(fmt, color=True)
    lf = cast(LogFormatter, lf)

    print(lf.format(logging.LogRecord('tornado.general', logging.DEBUG, '', 0, "Some message", None, None)))



# Generated at 2022-06-14 12:31:48.462238
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Test tornado.log.LogFormatter()"""
    formatter = LogFormatter()
    assert hasattr(formatter, "_fmt")
    assert hasattr(formatter, "_colors")
    assert hasattr(formatter, "_normal")
    assert formatter._colors[logging.DEBUG] == "\x1b[2;34m"
    assert formatter._colors[logging.INFO] == "\x1b[2;32m"
    assert formatter._colors[logging.WARNING] == "\x1b[2;33m"
    assert formatter._colors[logging.ERROR] == "\x1b[2;31m"
    assert formatter._colors[logging.CRITICAL] == "\x1b[2;35m"

# Generated at 2022-06-14 12:31:55.423030
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    formatter.use_color = True
    msg = "Test line"
    record = logging.LogRecord("tornado.general", logging.INFO, "/tmp", 0, msg, None, None)
    result = formatter.format(record)
    expected = '\x1b[0;32;49m[I ' + time.strftime("%y%m%d %H:%M:%S") + ' <string>:0]\x1b[0m Test line'
    assert result == expected



# Generated at 2022-06-14 12:32:03.951691
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=True)
    assert formatter

# I don't like the logging module's built-in buffering because you lose
# logs when the process dies.  So here's a simple replacement that just
# stores everything in a list:

_log_buffer = []  # type: Optional[List[Tuple[int, str, Any]]]
_log_buffer_lock = None  # type: Any



# Generated at 2022-06-14 12:32:15.474332
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:32:20.494834
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=False)
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("tornado")
    logger.warning("test")
    assert formatter.format(logging.LogRecord("tornado", logging.DEBUG, "test", 1, "test", None, None)) == "[DEBUG 0001 test] test"


# Generated at 2022-06-14 12:32:31.248652
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter(
        fmt='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%y%m%d %H:%M:%S',
        color=True,
        colors={
            logging.DEBUG: 4,
            logging.INFO: 2,
            logging.WARNING: 3,
            logging.ERROR: 1,
            logging.CRITICAL: 5
        }
    )

# Generated at 2022-06-14 12:32:44.107292
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define
    define('logging', default='WARNING', type=str)
    define('log_file_prefix', default='../run/test.log', type=str)
    define('log_file_max_size', default='10000', type=int)
    define('log_file_num_backups', default=5, type=int)
    define('log_rotate_mode', default='time', type=str)
    define('log_rotate_when', default='W0', type=str)
    define('log_rotate_interval', default=1, type=int)
    define('log_to_stderr', default=False, type=bool)
    enable_pretty_logging()
    gen_log.debug('Debug message')
    gen_log.info('Info message')
    gen

# Generated at 2022-06-14 12:32:56.963355
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # type () -> None
    import tornado.options
    import logging
    import os

    def _dump_log(filename: str) -> None:
        with open(filename, "rt") as f:
            for line in f:
                print(line.rstrip())

    def _cleanup(filename: str) -> None:
        if os.path.exists(filename):
            os.remove(filename)

    # Log file prefix explicitly specified

# Generated at 2022-06-14 12:32:57.494541
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass



# Generated at 2022-06-14 12:33:02.051278
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    import logging
    logRecord = logging.LogRecord("test",logging.INFO,"","1","test","()","()",
        "test_LogFormatter_format")
    logRecord.exc_info = "()"
    logRecord.exc_text = "()"
    print(formatter.format(logRecord))
    assert(True)



# Generated at 2022-06-14 12:33:02.976253
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()  # Should not raise error

# Generated at 2022-06-14 12:33:14.158111
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.log import app_log
    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test
    from tornado.httpclient import AsyncHTTPClient
    import functools
    import logging


    class P(tornado.web.RequestHandler):
        def get(self):
            app_log.info("P")
            self.write("P")

    http_server = tornado.httpserver.HTTPServer(tornado.web.Application([("/", P)]))
    http_server.listen(8888)
    @gen_test
    async def main():
        response = await AsyncHTTPClient().fetch("http://localhost:8888")
        assert response.body == b"P"

    logging.basicConfig(level=logging.DEBUG)

# Generated at 2022-06-14 12:33:21.979515
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Make sure that Formatter.format() handles unicode.
    # It no longer raises UnicodeDecodeError exceptions since we moved to
    # safe_str() in all loggers and formatters.
    import unittest
    import logging

    class _TestFormatter(LogFormatter):
        def __init__(self, *args, **kwargs):
            LogFormatter.__init__(self, *args, **kwargs)
            # In python 2, logging.Formatter.format() internal calls
            # str() on the resulting message. Use this variable to set
            # the return value of the inserted str() call.
            self._str = "TEST UNICODE"

        def format(self, record):
            return self._str


# Generated at 2022-06-14 12:33:56.339859
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    f = LogFormatter(fmt=fmt)
    assert f._fmt == fmt
    assert f._colors[logging.DEBUG] == "\033[2;34m"
    assert f._normal == "\033[0m"

# Global logger object
logger = gen_log



# Generated at 2022-06-14 12:34:07.485631
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    s = '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19'
    color = True

# Generated at 2022-06-14 12:34:10.438169
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert _stderr_supports_color()
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)


# Generated at 2022-06-14 12:34:13.604049
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logFormatter = LogFormatter(fmt='%(asctime)s %(lineno)d %(levelname)s %(message)s')


# Shortcut for tornado.options.options.logging

# Generated at 2022-06-14 12:34:26.938904
# Unit test for function define_logging_options
def test_define_logging_options():
    from tornado.options import define, options, parse_command_line
    define("foo")
    define("bar")
    define("baz")
    options.logging = "debug"
    options.log_to_stderr = True
    define_logging_options()
    options.log_file_prefix = options.bar = "/xyzzy"
    options.log_file_max_size = 100 * 1000 * 1000
    options.log_file_num_backups = 10
    options.log_rotate_when = "midnight"
    options.log_rotate_interval = 1
    options.log_rotate_mode = "size"
    parse_command_line()
    assert options.log_to_stderr
    assert options.log_file_prefix == "/xyzzy"
    assert options.log_

# Generated at 2022-06-14 12:34:40.307015
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.addLevelName(1, "TESTLEVEL")

    class TestHandler(logging.Handler):
        def __init__(self, levelname: str) -> None:
            super().__init__(logging.NOTSET)
            self.levelname = levelname

        def handle(self, record: Any) -> None:
            assert record.levelname == self.levelname
            assert record.name == "test"
            assert record.msg == "test message"
            self.levelname = "handled"

    TestHandler.test_class = True  # skip test on this class
    test_handler = TestHandler("TESTLEVEL")
    logging.getLogger().addHandler(test_handler)

    enable_pretty_logging()
    app_log.info("test message")

# Generated at 2022-06-14 12:34:41.680498
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(options=None, logger=None)
    return

# Generated at 2022-06-14 12:34:47.203401
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logfm = LogFormatter()
    assert logfm._fmt == LogFormatter.DEFAULT_FORMAT
    logfm = LogFormatter(fmt="test")
    assert logfm._fmt == "test"
    assert logfm.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    logfm = LogFormatter(fmt="test", datefmt="test")
    assert logfm.datefmt == "test"


# Generated at 2022-06-14 12:34:55.004995
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(
        LogFormatter(fmt="%(color)s%(levelname)s%(end_color)s %(message)s")
    )
    logger.addHandler(handler)
    logger.debug("example debug message")
    logger.info("example info message")
    logger.warning("example warning message")
    logger.error("example error message")
    logger.critical("example critical message")


# Generated at 2022-06-14 12:35:00.028234
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Don't print messages to stderr.
    logging.getLogger().handlers = []
    import tornado.options
    tornado.options.parse_config_file("test/options_test_logging.conf")
    logging.info("foo")
test_enable_pretty_logging.no_tornado = True

# Generated at 2022-06-14 12:35:55.831392
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logFmt = LogFormatter()
    logName = logging.getLogger()
    logName.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    logName.addHandler(console)
    logName.info("This is a test log message.")
    print(logFmt.format(logName))



# Generated at 2022-06-14 12:36:07.004676
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options = tornado.options.define("name", default="", help="", type=str)
    tornado.options.options().name = "test"
    tornado.options.options.logging = "test"
    tornado.options.options.logging.upper = lambda x: "DEBUG"
    tornado.options.options.log_file_prefix = "test_file"
    tornado.options.options.log_rotate_mode = "size"
    tornado.options.options.log_file_max_size = 100
    tornado.options.options.log_file_num_backups = 10
    tornado.options.options.log_rotate_when = "S"
    tornado.options.options.log_rotate_interval = 10
    tornado.options.options.log_to_stderr

# Generated at 2022-06-14 12:36:09.032911
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    enable_pretty_logging(logger=logger)
    logger.info("test")

# Generated at 2022-06-14 12:36:14.185871
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter(color=True)
    assert isinstance(fmt, logging.Formatter)
    assert isinstance(fmt._fmt, str)
    assert isinstance(fmt._colors, dict)
    assert isinstance(fmt.datefmt, str)
    assert isinstance(fmt._normal, str)



# Generated at 2022-06-14 12:36:16.010512
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = None
    logger = None
    enable_pretty_logging(options, logger)

# Generated at 2022-06-14 12:36:21.182823
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = "none"
    enable_pretty_logging()

    tornado.options.options.logging = "debug"
    enable_pretty_logging()
    enable_pretty_logging()
    enable_pretty_logging()
    enable_pretty_logging()


# Generated at 2022-06-14 12:36:22.093406
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()


# Generated at 2022-06-14 12:36:33.839999
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.platform.asyncio import AsyncIOMainLoop

    class TestHandler(logging.Handler):
        def __init__(self):
            super(TestHandler, self).__init__()
            self.records = []  # type: list

        def emit(self, record):
            self.records.append(record)

    def get_formatted_records(fmt: str, color: bool = True) -> list:
        logger = logging.getLogger("test_tornado")
        logger.handlers = []
        logger.addHandler(TestHandler())
        logger.setLevel(logging.INFO)
        formatter = LogFormatter(color=color, fmt=fmt)

# Generated at 2022-06-14 12:36:47.100238
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class MockLogRecord(object):  # type: ignore
        levelname = 'DEBUG'
        module = 'test'
        lineno = 1
        created = 1502309492.889248
        msecs = 889.2477831363678
        asctime = "2017-08-08 11:31:32"
        levelno = logging.DEBUG
        exc_info = None  # type: Optional[Any]
        exc_text = None  # type: Optional[str]
        message = ''  # type: str
        color = ''  # type: str
        end_color = ''  # type: str
        def __init__(self, msg):
            self.message = msg
        def __getitem__(self, key):
            return getattr(self, key)
        def getMessage(self):
            return self

# Generated at 2022-06-14 12:36:53.191434
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()
    assert LogFormatter(fmt="%(asctime)s", datefmt="%d/%m/%Y %H:%M:%S")
    assert LogFormatter(fmt="%(asctime)s", color=False)
    assert (
        LogFormatter(fmt="%(asctime)s", color=False, colors={logging.DEBUG: 2})
    )



# Generated at 2022-06-14 12:37:53.649735
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import time
    options = tornado.options.options
    options.logging = "INFO"
    options.log_file_prefix = "log/hello.log"
    options.log_rotate_mode = "size"
    options.log_file_max_size = 100
    options.log_file_num_backups = 2
    enable_pretty_logging(options)
    for i in range(10):
        gen_log.info(f"hello world {i}")
    time.sleep(1)


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:57.006646
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = LogFormatter()
    record = logging.LogRecord(
        "tornado.access",
        logging.INFO,
        None,
        0,
        "test message",
        None,
        None,
    )
    assert fmt.format(record) == "[I 171110 12:06:19 -  ] test message"

# Generated at 2022-06-14 12:38:09.043784
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line
    define("logging", default=None, help="logging level", type=str)
    define(
        "log_to_stderr",
        default=None,
        help="Send log output to stderr (colorized if possible). "
        "By default use stderr if --log_file_prefix is not set and "
        "no other logging is configured.",
        type=bool,
    )
    define("log_file_prefix", default=None, help="Path prefix for log files", type=str)

# Generated at 2022-06-14 12:38:15.871081
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # LogFormatter()
    log_formatter = LogFormatter()
    assert log_formatter.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    assert log_formatter.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert log_formatter.DEFAULT_COLORS == {logging.DEBUG: 4, logging.INFO: 2, logging.WARNING: 3, logging.ERROR: 1, logging.CRITICAL: 5}  # noqa: E501



# Generated at 2022-06-14 12:38:27.452741
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.logging = "debug" # should set logger.level
    tornado.options.options.log_file_prefix = "test"
    tornado.options.options.log_rotate_mode = "size"
    tornado.options.options.log_file_max_size = 100
    tornado.options.options.log_file_num_backups = 5
    tornado.options.options.log_rotate_when = "D"
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_to_stderr = False
    enable_pretty_logging()
    assert logging.getLogger().level == logging.DEBUG
    assert isinstance(logging.getLogger().handlers[0], logging.handlers.RotatingFileHandler) 

# Generated at 2022-06-14 12:38:34.893906
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger()
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    fmter = LogFormatter(fmt=fmt)
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(fmter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    logger.info("test")
    logger.critical("test")



# Generated at 2022-06-14 12:38:36.760059
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    _stderr_supports_color()
    enable_pretty_logging(None, None)

# Generated at 2022-06-14 12:38:38.437549
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()
    LogFormatter(color=False)
    LogFormatter(color=True)



# Generated at 2022-06-14 12:38:48.230082
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(level=logging.DEBUG, format="--- %(message)s")
    color_formatter = LogFormatter()

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.handlers[0].setFormatter(color_formatter)

    logger.critical("critical")
    logger.error("error")
    logger.warning("warning")
    logger.info("info")
    logger.debug("debug")

if __name__ == '__main__':
    test_LogFormatter()



# Generated at 2022-06-14 12:38:52.789921
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # the log_function has no effect
    log = logging.LogRecord("", "", "", 0, "Hello, world!", None, None)
    logf = LogFormatter()
    assert logf.format(log) == "[I 000508 01:12:21 test_logging.py:77] Hello, world!"
