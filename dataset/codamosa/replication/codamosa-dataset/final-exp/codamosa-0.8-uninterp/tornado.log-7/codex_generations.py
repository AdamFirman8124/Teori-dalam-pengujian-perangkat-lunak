

# Generated at 2022-06-14 12:31:16.708706
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()[0].__class__ == logging.Formatter

# Generated at 2022-06-14 12:31:26.790882
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.web
    import tornado.ioloop
    import tornado.autoreload
    import tornado.httpserver

    class PrintHandler(tornado.web.RequestHandler):
        def get(self, line):
            print(line)
            self.write("see stdout")

    if __name__ == "__main__":
        tornado.options.define("port", default=8888, help="run on the given port", type=int)
        tornado.options.define("logging", default="debug", help="logging level")
        tornado.options.define("log_file_prefix", default="log.", help="log filename")
        tornado.options.define("log_rotate_mode", default="time", help="log rotate mode")

# Generated at 2022-06-14 12:31:28.281432
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():pass



# Generated at 2022-06-14 12:31:36.464264
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter()
    import datetime
    record = logging.LogRecord(
        "tornado.access", logging.INFO, "logger/__init__.py", 156,
        "GET /api/v1/labels/images/1 HTTP/1.1", None, None
    )
    new_record = lf.format(record)
    assert new_record.startswith("[I ")
    assert new_record.endswith("] GET /api/v1/labels/images/1 HTTP/1.1")
    assert datetime.datetime.now().strftime("%y%m%d %H:%M:%S") in new_record
    assert "logger/__init__.py:156" in new_record
    # Use __class__._method
    lf1

# Generated at 2022-06-14 12:31:38.274883
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:46.874399
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        import tornado.options
        import tornado.log
        import mock

        options = tornado.options.options
        tornado.options.options.logging = 'INFO'
        tornado.options.options.log_file_prefix = './log/application.log'
        tornado.options.options.log_rotate_mode = 'size'
        tornado.options.options.log_file_max_size = 1024 * 1024 * 1024
        tornado.options.options.log_file_num_backups = 5
        tornado.options.options.log_to_stderr = True

        tornado.log.enable_pretty_logging()
        gen_log.info("Success")
        assert True
    except Exception:
        assert False

# Generated at 2022-06-14 12:31:55.190339
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    class TestCase(unittest.TestCase):
        def test_format(self):
            formatter = LogFormatter()
            record = logging.LogRecord(
                name='tornado.application',
                level=logging.INFO,
                pathname='/Users/Shared/anaconda3/lib/python3.6/site-packages/tornado/web.py',
                lineno=3035,
                msg='200 GET / (127.0.0.1) 2.17ms',
                args=(),
                exc_info=None
            )
            message = formatter.format(record)
            self.assertEqual(message, '[I 20190217 12:17:03 web:3035] 200 GET / (127.0.0.1) 2.17ms')
    unittest

# Generated at 2022-06-14 12:31:56.370367
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()



# Generated at 2022-06-14 12:32:07.717556
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # check default values
    log_formatter = LogFormatter()
    assert log_formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert log_formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert log_formatter._normal == ""
    assert log_formatter._colors == {}

    # check constructor args
    fmt = "%(level)s %(message)s"
    datefmt = "%Y"
    log_formatter = LogFormatter(fmt, datefmt)
    assert log_formatter.datefmt == datefmt
    assert log_formatter._fmt == fmt



# Generated at 2022-06-14 12:32:16.058796
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    def demo_LogFormatter_format():
        try:
            logging.debug('This is a debug message')
        except NameError:
            print('NameError raised')
        # logging.warning('This is a warning message')
        # logging.error('This is an error message')
        # logging.critical('This is a critical error message')

    if __name__ == '__main__':
        demo_LogFormatter_format()


# Generated at 2022-06-14 12:32:29.795459
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=False, fmt="%(color)s%(levelname)s%(end_color)s %(message)s")  # noqa: E501
    assert formatter is not None



# Generated at 2022-06-14 12:32:42.081298
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter()
    class MockRecord:
        __dict__ = {"getMessage":lambda :"me", "__dict__":{}, "levelno":1, "asctime":"asctime",
            "color":"color", "end_color":"end_color", "exc_info":None, "exc_text":None}
    r = MockRecord()
    # test normal
    r.__dict__["getMessage"] = lambda :"this is a message"
    assert lf.format(r) == "[I asctime :0] this is a message"
    # test with exception
    r.__dict__["exc_info"] = (ValueError, "test exception")
    r.__dict__["exc_text"] = "this is an exception"

# Generated at 2022-06-14 12:32:45.038632
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # Just make sure we can create one.
    formatter = LogFormatter()
    formatter(logging.LogRecord("test", logging.INFO, __file__, 10, "", None, None))



# Generated at 2022-06-14 12:32:49.335600
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter._fmt, str)
    assert isinstance(formatter._colors, dict)
    assert formatter._normal == ""


# Generated at 2022-06-14 12:32:56.546995
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: ignore
    formatter = logging.Formatter(
        fmt='%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s',
        datefmt='%y%m%d %H:%M:%S')
    assert isinstance(formatter, logging.Formatter)
    assert isinstance(formatter, LogFormatter)



# Generated at 2022-06-14 12:33:00.435969
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    tornado.options.parse_command_line()
    enable_pretty_logging()
    logger = logging.getLogger()
    ts = logger.handlers
    for x in ts:
        print(x)
test_enable_pretty_logging()

# Generated at 2022-06-14 12:33:08.903715
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf.datefmt == lf.DEFAULT_DATE_FORMAT
    assert lf._colors == lf.DEFAULT_COLORS
    assert lf._normal == ""

    lf = LogFormatter(None, None, None, False)
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf.datefmt == lf.DEFAULT_DATE_FORMAT
    assert lf._colors == lf.DEFAULT_COLORS
    assert lf._normal == ""

    lf = LogFormatter(color=False)
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf.datefmt == lf.DEFAULT_

# Generated at 2022-06-14 12:33:09.959465
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert enable_pretty_logging() is None

# Generated at 2022-06-14 12:33:21.345352
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    tornado.options.options.logging = 'debug'
    tornado.enable_pretty_logging()
    tornado.log.app_log.debug('test')
    with open('./tornado.application.log') as fp:
        lines = fp.readlines()
        assert len(lines) == 1
        assert 'test' in lines[0]
    tornado.log.gen_log.info('test')
    with open('./tornado.general.log') as fp:
        lines = fp.readlines()
        assert len(lines) == 1
        assert 'test' in lines[0]
    tornado.log.access_log.error('test')

# Generated at 2022-06-14 12:33:30.391049
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    from io import StringIO
    from tornado.log import app_log

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(LogFormatter())

    app_log.addHandler(handler)
    app_log.critical('critical test')
    app_log.error('error test')
    app_log.warning('warning test')
    app_log.info('info test')
    app_log.debug('debug test')
    app_log.removeHandler(handler)



# Generated at 2022-06-14 12:33:51.859014
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:52.819401
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:54.221671
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()


# Generated at 2022-06-14 12:34:00.526236
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.logging="DEBUG"
    options.log_file_prefix="logs"
    options.log_file_max_size=1
    options.log_file_num_backups = 1
    options.log_rotate_mode = "size"
    options.log_rotate_when="midnight"
    options.log_rotate_interval=1
    options.log_to_stderr = True
    enable_pretty_logging()
    gen_log.info("aa")

# Generated at 2022-06-14 12:34:08.528259
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options as options
    import logging as logging
    import logging.handlers as handlers
    logger = options.options.logging
    logger = options.options.log_file_prefix
    logger = options.options.log_rotate_mode
    logger = options.options.log_file_max_size
    logger = options.options.log_file_num_backups
    logger = options.options.log_rotate_when
    logger = options.options.log_rotate_interval
    handler = handlers.RotatingFileHandler
    handler = handlers.TimedRotatingFileHandler
    channel = logging.StreamHandler()
    channel = LogFormatter()
    channel.setFormatter(LogFormatter())
    logger.addHandler(channel)

# Generated at 2022-06-14 12:34:21.605058
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Verify that it handles a record with a message (str) and no exception
    # information, a record with a message (str) and exception information, and
    # a record with no message and exception information.
    _stderr_supports_color()
    formatter = LogFormatter()
    record_no_exception = logging.LogRecord(
        "foo", logging.DEBUG, None, None, "bar", None, None
    )
    record_with_exception = logging.LogRecord(
        "foo", logging.DEBUG, None, None, "bar", None, None
    )
    record_with_exception.exc_info = (ZeroDivisionError, ZeroDivisionError("zero"), None)
    record_no_message = logging.LogRecord("foo", logging.DEBUG, None, None, None, None, None)
   

# Generated at 2022-06-14 12:34:29.346506
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = LogFormatter(
        fmt='%(color)s%(asctime)s [%(levelname)s] %(message)s%(end_color)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('test message')


# Generated at 2022-06-14 12:34:43.297448
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    if not _stderr_supports_color():
        return

    class MockLogRecord:
        levelno = logging.INFO
        exc_info = None
        exc_text = None

    def test(msg, record):
        try:
            record.message = msg
            if isinstance(msg, bytes):
                raise AssertionError("msg should be unicode")
            if not isinstance(record.message, basestring_type):
                raise AssertionError("message must be a string")
        except Exception as e:
            record.message = "Bad message (%r): %r" % (e, record.__dict__)

    formatter = LogFormatter()

    record = MockLogRecord()
    record.__dict__["message"] = "Test"
    formatter.format(record)

# Generated at 2022-06-14 12:34:45.084804
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt is not None


# Generated at 2022-06-14 12:34:52.382207
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logFormatter = LogFormatter()
    logFormatter.format(logging.getLogger().makeRecord(None, logging.INFO, "msg", None, None, None, None, None))
    logFormatter.datefmt = None
    logFormatter.format(logging.getLogger().makeRecord(None, logging.INFO, "msg", None, None, None, None, None))
    logFormatter.datefmt = 13
    logFormatter.format(logging.getLogger().makeRecord(None, logging.INFO, "msg", None, None, None, None, None))



# Generated at 2022-06-14 12:35:41.352195
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.getLogger().handlers = []
    import tornado.options
    import tornado.log
    import sys

    tornado.log.enable_pretty_logging()
    tornado.options.parse_command_line(["--logging=none"])
    assert not logging.getLogger().handlers

    tornado.log.enable_pretty_logging()
    tornado.options.parse_command_line(["--logging=debug"])
    assert isinstance(logging.getLogger().handlers[0], logging.StreamHandler)

    tornado.log.enable_pretty_logging()
    tornado.options.parse_command_line(["--log_to_stderr=true"])
    assert isinstance(logging.getLogger().handlers[0], logging.StreamHandler)

    tornado.log.enable_pretty_

# Generated at 2022-06-14 12:35:43.827753
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log = LogFormatter()
    record = logging.makeLogRecord({})
    print(log.format(record))

test_LogFormatter_format()

# Generated at 2022-06-14 12:35:47.944336
# Unit test for function define_logging_options
def test_define_logging_options():
    # action 1
    import tornado.options
    options = tornado.options.OptionParser()
    define_logging_options(options)
    options.parse_command_line(args=["--log_to_stderr=1"])
    options.parse_config_file(config_file = 'logging_config.conf')
    enable_pretty_logging(options)
    # action 2
    access_log.info("access log message")
    # action 3
    access_log.info("access log message")
    # action 4
    access_log.info("access log message")
    # action 5
    access_log.info("access log message")
    # action 6
    access_log.info("access log message")
    app_log.info("app log message")
    gen_log.info("gen log message")

# Generated at 2022-06-14 12:36:00.489559
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class _TestRecord(object):
        def __init__(
            self,
            levelno,
            msg,
            args,
            exc_info,
            func=None,
            stack_info=None,
        ):
            self.levelno = levelno
            self.msg = msg
            self.args = args
            self.exc_info = exc_info
            self.func = func
            self.stack_info = stack_info

        def getMessage(self):
            return self.msg

    lf = LogFormatter()
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._datefmt == lf.DEFAULT_DATE_FORMAT
    assert lf._colors == lf.DEFAULT_COLORS


# Generated at 2022-06-14 12:36:10.280009
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # pylint: disable=unused-argument
    def options_func(options):
        options.define("logging", default="debug", help="debug, info, warning, error, none")
        options.define("log_file_prefix", default="tornado.log", help="file name of log file")
        options.define("log_file_num_backups", default=10, help="number of backups log files to keep")
        options.define("log_rotate_when", default="midnight", help="when to rotate log files")
        options.define("log_rotate_interval", default=1, help="how many backups to keep")
        options.define("log_rotate_mode", default="size", help="size, time")

# Generated at 2022-06-14 12:36:21.795884
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class FakeOption:
        def __init__(self, logging, log_file_prefix, log_rotate_mode,
                     log_file_max_size, log_file_num_backups,
                     log_rotate_when, log_rotate_interval, log_to_stderr):
            self.logging = logging
            self.log_file_prefix = log_file_prefix
            self.log_rotate_mode = log_rotate_mode
            self.log_file_max_size = log_file_max_size
            self.log_file_num_backups = log_file_num_backups
            self.log_rotate_when = log_rotate_when
            self.log_rotate_interval = log_rotate_interval
            self.log_to_stder

# Generated at 2022-06-14 12:36:33.538671
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log

    import logging
    import logging.handlers
    import io
    import sys
    import warnings

    logging.getLogger().handlers = []
    # Test basic functionality
    tornado.options.parse_command_line(["--logging=debug"])
    tornado.log.enable_pretty_logging()
    tornado.log.gen_log.info("test")
    assert "test" in sys.stderr.getvalue()
    sys.stderr = io.StringIO()

    # Test json formatting
    tornado.options.parse_command_line(["--logging=debug", "--log_json=1"])
    tornado.log.enable_pretty_logging()
    tornado.log.gen_log.info("{test}")

# Generated at 2022-06-14 12:36:34.502674
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:36:43.034805
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging('none')
    try:
        enable_pretty_logging('DEBUG')
        enable_pretty_logging('debug',logging.getLogger())
    except Exception as e:
        #print(str(e))
        pass
    try:
        enable_pretty_logging('DEBUG','none')
    except Exception as e:
        #print(str(e))
        pass
test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:53.725337
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    my_log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    my_log_date_format = "%y%m%d %H:%M:%S"
    my_log_color = True

# Generated at 2022-06-14 12:38:01.699366
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()

    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._colors == {}
    assert lf._normal == ""
    assert lf._style == "%"
    assert lf.usesTime()
    assert lf.datefmt == lf.DEFAULT_DATE_FORMAT

    fmt = "the answer is %(answer)s"
    lf2 = LogFormatter(fmt)
    assert lf2._fmt == fmt
    assert lf2._colors is lf2._colors
    assert lf2._normal is lf2._normal
    assert lf2._style == "%"
    assert lf2.usesTime()
    assert lf2.datefmt == lf2.DEFAULT_DATE_FORMAT

    l

# Generated at 2022-06-14 12:38:02.708270
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()


# Generated at 2022-06-14 12:38:04.387191
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert isinstance(log_formatter, LogFormatter)



# Generated at 2022-06-14 12:38:12.879215
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    # Create a mock record to test it out
    class MockRecord:
        def __init__(self, name, levelno, msg):
            self.name = name
            self.levelno = levelno
            self.msg = msg
            self.exc_info = self.exc_text = None

        def getMessage(self) -> str:
            return self.msg

    assert (
        f.format(MockRecord("name", logging.INFO, "foo"))
        == "[I %(asctime)s name:%(lineno)d] foo"
    )



# Generated at 2022-06-14 12:38:14.166244
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert(log_formatter)

# Generated at 2022-06-14 12:38:16.179324
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # Check that the constructor doesn't raise exceptions
    LogFormatter()


# Generated at 2022-06-14 12:38:16.799420
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():pass

# Generated at 2022-06-14 12:38:22.955120
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    logger = logging.Logger("tornado.test")
    logger.propagate = False
    logger.addHandler(logging.StreamHandler())

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")



# Generated at 2022-06-14 12:38:29.109593
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    class opt():
        logging = "debug"
        log_file_prefix = None
        log_rotate_mode = "time"
        log_rotate_when = "D"
        log_rotate_interval = 1
        log_file_num_backups = 5
        log_to_stderr = None
    options = opt()
    enable_pretty_logging(options)


# Generated at 2022-06-14 12:38:35.110446
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    def test_LogFormatter_empty():
        x = LogFormatter()
        assert x != None

    def test_LogFormatter_with_colorama():
        old_stderr = sys.stderr
        sys.stderr = colorama.initialise.wrapped_stderr
        colorama.init()
        try:
            if not _stderr_supports_color():
                assert False
        finally:
            sys.stderr = old_stderr
            colorama.deinit()

    test_LogFormatter_empty()
    test_LogFormatter_with_colorama()



# Generated at 2022-06-14 12:40:15.607419
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    logger = logging.getLogger()
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(LogFormatter(log_format))
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
    logger.info("test")
    logger.error("test")



# Generated at 2022-06-14 12:40:22.734208
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    m = {"__name__": "__main__"}
    logFormatter = LogFormatter(style="%", color=True, colors={})
    logger = logging.getLogger("test.logger")
    logger.info("This is a test")
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logFormatter)
    logger.addHandler(streamHandler)

__all__ = ["access_log", "app_log", "gen_log", "enable_pretty_logging"]

# Shorthand for `tornado.options.options`.



# Generated at 2022-06-14 12:40:24.341993
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.LogRecord("tornado.general", logging.DEBUG, "Test", 0, "Format test", [], None)  # noqa: E501



# Generated at 2022-06-14 12:40:36.329443
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # This example shows how to embed the formatted representation of
    # a record, which has been converted to Unicode, in another
    # message.

    class SpamFilter(logging.Filter):

        def filter(self, record: Any) -> bool:
            message = record.msg
            assert isinstance(message, basestring_type)
            if "spam" in message:
                return False
            return True

    lf = LogFormatter(color=True)
    lh = logging.StreamHandler()
    lh.setFormatter(lf)
    lh.addFilter(SpamFilter())
    root_logger = logging.getLogger()
    root_logger.addHandler(lh)
    root_logger.warning("Spam spam spam spam spam spam spam spam spam spam spam")
    root_logger.warning

# Generated at 2022-06-14 12:40:38.141777
# Unit test for function define_logging_options
def test_define_logging_options():
    import tornado.options
    define_logging_options()
    opts = tornado.options.options
    assert opts.log_rotate_mode == "size"
    assert opts.log_rotate_when == "midnight"
    assert opts.log_rotate_interval == 1

# Generated at 2022-06-14 12:40:41.180161
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    record = logging.LogRecord(
        "foo", logging.DEBUG, None, 0, "message", {}, None
    )
    formatter.format(record)
    assert record.message == "message"
    assert record.asctime is not None

