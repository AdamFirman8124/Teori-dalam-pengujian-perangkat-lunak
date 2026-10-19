

# Generated at 2022-06-14 12:31:00.292857
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    pass



# Generated at 2022-06-14 12:31:09.740713
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    style = "%"
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    lf = LogFormatter(fmt,datefmt,style,True,colors)
    assert lf is not None



# Generated at 2022-06-14 12:31:10.662396
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:12.498563
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        enable_pretty_logging()
    except Exception as e:
        print(e)
test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:24.945241
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    f = LogFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.DEBUG,
        pathname="/path/test.py",
        lineno=100,
        msg="this is test",
        args=None,
        exc_info=None,
    )
    record1 = logging.LogRecord(
        name="test1",
        level=logging.INFO,
        pathname="/path/test1.py",
        lineno=100,
        msg="this is test 1",
        args=None,
        exc_info=None,
    )

# Generated at 2022-06-14 12:31:30.070215
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.enable_pretty_logging(options)
    assert tornado.options.options.logging is None
    assert tornado.options.options.log_file_prefix is None
    assert tornado.options.options.log_file_max_size is None
    assert tornado.options.options.log_file_num_backups is None
    assert tornado.options.options.log_rotate_when is None
    assert tornado.options.options.log_rotate_interval is None
    assert tornado.options.options.log_rotate_mode is None
    assert tornado.options.options.log_to_stderr is None

# Generated at 2022-06-14 12:31:33.871242
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    stdout_stream_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_log_formatter = LogFormatter()
    stdout_stream_handler.setFormatter(stdout_log_formatter)



# Generated at 2022-06-14 12:31:34.785157
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # TODO
    pass



# Generated at 2022-06-14 12:31:38.509358
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    assert LogFormatter().format(logging.makeLogRecord({'msg': 'test'})) == '[INFO  0000000000 :    ] test'



# Generated at 2022-06-14 12:31:47.953303
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    def formatted_test(data,result):
        data = data.replace("\\n","\n")
        result = result.replace("\\n","\n")
        formatter = LogFormatter()
        record = logging.LogRecord(
        name=None, level=logging.ERROR, pathname=None, lineno=0,
        msg=data, args=None, exc_info=None)
        got = formatter.format(record)
        return got == result
    d = {'data':"Test \n Log \n Multiline \n Error","result":"[E 0 1970-01-01 00:00:00 (0:0)]: Test \n    Log \n    Multiline \n    Error"}
    assert formatted_test(d['data'],d['result'])

# Generated at 2022-06-14 12:32:00.454546
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig()
    root = logging.getLogger()
    stream = logging.StreamHandler()
    stream.setFormatter(LogFormatter())
    root.addHandler(stream)
    root.warning('test')


# Generated at 2022-06-14 12:32:03.315428
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._normal == "\033[0m"


# Generated at 2022-06-14 12:32:12.707688
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging

    logging.basicConfig(level=logging.DEBUG)
    tornado.options.define("logging", type=str, default="severe")
    tornado.options.define("log_file_prefix", type=str, default="")
    tornado.options.define("log_rotate_mode", type=str, default="size")
    tornado.options.define("log_file_max_size", type=int, default=1024)
    tornado.options.define("log_file_num_backups", type=int, default=0)
    tornado.options.define("log_rotate_when", type=str, default="S")
    tornado.options.define("log_rotate_interval", type=int, default=1)

# Generated at 2022-06-14 12:32:23.443934
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # This is a unit test of the format method in the LogFormatter class
    import os
    import logging
    import time
    log_time_string = time.strftime('%y%m%d %H:%M:%S')
    log_file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tornado', 'log.txt')
    if os.path.exists(log_file_name):
        os.remove(log_file_name)
    # Set the default logging level to debug
    logging.getLogger().setLevel(logging.DEBUG)
    # Create a logger for the LogFormatter class
    logger = logging.getLogger('tornado.test.LogFormatter')
    # Create a file handler and add that to the logger
    f

# Generated at 2022-06-14 12:32:27.814540
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    mylog = LogFormatter(datefmt="%m-%d %H:%M:%S", fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s") # noqa: E501



# Generated at 2022-06-14 12:32:33.173567
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    #Should not be called
    raise Exception
    #message = "message1"
    #assert isinstance(message, basestring_type)  # guaranteed by logging
    #print("message={},type={},isinstance={}".format(message,type(message),isinstance(message, basestring_type)))
    #print(sys.getdefaultencoding())
    #print(sys.getfilesystemencoding())
#test_LogFormatter_format()



# Generated at 2022-06-14 12:32:37.192229
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    logger.addHandler(logging.StreamHandler())
    logger.info("test")

# Generated at 2022-06-14 12:32:39.844931
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    obj = LogFormatter()
    assert obj is not None
    del obj

if __name__ == "__main__":
    test_LogFormatter()

# Generated at 2022-06-14 12:32:50.235952
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import logging.handlers
    tornado.options.options.logging = "DEBUG"
    tornado.options.options.log_file_prefix = None
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_rotate_when = "D"
    tornado.options.options.log_rotate_interval = 30
    tornado.options.options.log_file_num_backups = 3
    tornado.options.options.log_to_stderr = None
    logger = logging.getLogger()
    for i in range(len(logger.handlers)):
        logger.removeHandler(logger.handlers[0])
    enable_pretty_logging()
    logger.error("test error")

# Generated at 2022-06-14 12:32:59.946343
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    root_logger = logging.getLogger()
    root_logger.handlers = []
    root_logger.setLevel(logging.DEBUG) 
    enable_pretty_logging()
    print(root_logger.handlers[0].stream.__class__)
    assert(root_logger.handlers[0].stream.__class__==logging.StreamHandler)
    enable_pretty_logging(None,root_logger)
    assert(root_logger.handlers[1].stream.__class__==logging.StreamHandler)
    #for handler in root_logger.handlers:
    #    handler.close()

# Generated at 2022-06-14 12:33:19.631581
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    record_info = logging.LogRecord("Log-1", "INFO", "", 1, "Dummy Log formatter message", None, None)
    log_fmt = LogFormatter()
    message = log_fmt.format(record_info)
    assert len(message) > 0

# Generated at 2022-06-14 12:33:32.069763
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class MockOptions():
        def __init__(self):
            self.log_file_prefix = ''
            self.log_rotate_mode = ''
            self.log_file_max_size = ''
            self.log_file_num_backups = ''
            self.log_rotate_when = ''
            self.log_rotate_interval = ''

    MockOptions.logging = 'info'
    enable_pretty_logging(MockOptions())
    MockOptions.logging = 'warning'
    enable_pretty_logging(MockOptions())
    MockOptions.logging = 'error'
    enable_pretty_logging(MockOptions())
    MockOptions.logging = 'debug'
    enable_pretty_logging(MockOptions())
    MockOptions.logging = 'none'
    enable

# Generated at 2022-06-14 12:33:41.396061
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.ioloop
    import time
    import sys
    import threading
    import logging
    import tornado.web
    import tornado.websocket
    import tornado.httpserver

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    class Application(tornado.web.Application):
        def __init__(self):
            handlers = [
                (r"/", MainHandler),
            ]

# Generated at 2022-06-14 12:33:42.306102
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:33:54.815319
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.setLoggerClass(Logger)
    logger = logging.getLogger()
    enable_pretty_logging({'logging' : '', 'log_to_stderr' : False})
    assert(len(logger.handlers) == 1)
    enable_pretty_logging({'logging' : '', 'log_to_stderr' : True})
    assert(len(logger.handlers) == 1)
    enable_pretty_logging({'logging' : '', 'log_file_prefix' : ''})
    assert(len(logger.handlers) == 2)
    enable_pretty_logging({'logging' : '', 'noconfig' : False})
    assert(len(logger.handlers) == 1)

# Generated at 2022-06-14 12:33:59.759054
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger("logging_test")
    handler = logging.StreamHandler(sys.stderr)
    log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]" \
                 "%(end_color)s %(message)s"
    date_format = "%m,%d/%Y %H:%M:%S"
    formatter = LogFormatter(color=True, fmt=log_format, datefmt=date_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    try:
        logger.info("test info")
    except Exception as e:
        print(e)

test_Log

# Generated at 2022-06-14 12:34:00.565108
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert enable_pretty_logging() is None

# Generated at 2022-06-14 12:34:04.659791
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        import tornado.options
        options = tornado.options.options
        options.logging = ""
        options.log_file_prefix = ""
        options.log_file_max_size = 0
        options.log_file_num_backups = 0
        options.log_to_stderr = 0
        enable_pretty_logging()
        assert True
    except ValueError:
        assert False

# Generated at 2022-06-14 12:34:07.353344
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    enable_pretty_logging(options = "options")
    enable_pretty_logging(logger = "logger")

test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:13.147462
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import logging.handlers
    tornado.options.options = tornado.options.Options()
    tornado.options.options.logging = "DEBUG"
    tornado.options.options.log_file_prefix = "a"
    tornado.options.options.log_rotate_mode = "size"
    tornado.options.options.log_file_max_size = "b"
    tornado.options.options.log_file_num_backups = "c"
    tornado.options.options.log_rotate_when = "D"
    tornado.options.options.log_rotate_interval = "e"
    tornado.options.options.log_to_stderr = "false"
    logger = logging.getLogger()
    enable_pretty_logging()
    return logger.hand

# Generated at 2022-06-14 12:34:51.601418
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    import time
    import unittest

    class Record(object):
        __slots__ = "created", "levelno", "msg"

        def __init__(self, levelno, msg):
            self.created = time.time()
            self.levelno = levelno
            self.msg = msg

    def setUpModule():
        global unittest
        try:
            import unittest2 as unittest
        except ImportError:
            pass

    class LogFormatterTest(unittest.TestCase):
        def setUp(self):
            self.formatter = LogFormatter()

        def test_format(self):
            def test(levelno, msg, should_eq):
                record = Record(levelno, msg)
                eq = unittest.TestCase.assertEqual
                eq

# Generated at 2022-06-14 12:34:53.022883
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()


test_enable_pretty_logging()

# Generated at 2022-06-14 12:35:03.242052
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import sys
    import tornado.options

    class MockedOptions(object):
        def __init__(self):
            self.logging = "debug"
            self.log_file_prefix = "/tmp/logs/tornado.log"
            self.log_file_num_backups = 100
            self.log_file_max_size = 1000
            self.log_rotate_mode = "size"
            self.log_to_stderr = True
            self.logging = "debug"
            self.log_rotate_when = "M"
            self.log_rotate_interval = 1000

        def __setattr__(self, a, v):
            return None

        def __getattr__(self, a):
            return None

    old_stdout = sys.stdout
    old_st

# Generated at 2022-06-14 12:35:05.609675
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter(color=False)
    assert not hasattr(fmt, "_colors")
    assert fmt._normal == ""



# Generated at 2022-06-14 12:35:14.588668
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf._fmt == LogFormatter.DEFAULT_FORMAT
    assert lf._colors == LogFormatter.DEFAULT_COLORS
    assert lf._normal == ""

    lf = LogFormatter('%(message)s', "%y%m%d %H:%M:%S", "%", True, {logging.DEBUG: 4})
    assert lf._fmt == "%(message)s"
    assert lf._colors == {logging.DEBUG: 4}
    assert lf._normal == ""



# Generated at 2022-06-14 12:35:21.634505
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class Record:
        __dict__ = dict(
            message='message',
            levelno=1,
            asctime='asctime',
            exc_info=(),
            exc_text='exc_text'
        )
        def getMessage(self):
            return self.message

    formatter = LogFormatter()
    formatter._colors = {1: 'color'}
    formatter._normal = 'normal'
    formatted = formatter.format(Record())
    assert(formatted == 'color[L asctime : 0]normal message\n    exc_text')



# Generated at 2022-06-14 12:35:33.169446
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado
    tornado.options.logging = 'debug'
    tornado.options.log_file_prefix = 'debug.log'
    tornado.options.log_rotate_mode = 'size'
    tornado.options.log_file_max_size = 1024
    tornado.options.log_file_num_backups = 5
    tornado.options.log_to_stderr = True
    tornado.options.log_rotate_when = 'S'
    tornado.options.log_rotate_interval = 1
    enable_pretty_logging()
    logger = logging.getLogger()
    logger.debug("test message")
    logger.info("test message")
    logger.warning("test message")
    logger.error("test message")
    logger.critical("test message")


# Generated at 2022-06-14 12:35:41.684940
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.log
    import tornado.options
    import logging

    # color_enabled tests.
    # "logging.INFO" is equivalent to tornado.options.options.logging.
    tornado.options.options.logging = "info"
    # "isatty" is the only thing the logging module checks to see if we can use
    # colors.
    sys.stderr.isatty = lambda: True
    # We should have color support if we're a tty.
    assert tornado.log.enable_pretty_logging()
    # If we disable colors, we shouldn't have color.
    tornado.options.options.log_color = False
    assert not tornado.log.enable_pretty_logging()
    # If we're not a tty, we shouldn't have color.
    sys.stderr.isatty

# Generated at 2022-06-14 12:35:52.578162
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(logging="none")
    enable_pretty_logging(logging="error")
    enable_pretty_logging(logging="warning")
    enable_pretty_logging(logging="info")
    enable_pretty_logging(logging="debug")

    enable_pretty_logging(logging="error", log_to_stderr=True)
    enable_pretty_logging(logging="error", log_to_stderr=False)
    enable_pretty_logging(logging="error", log_to_stderr=None)
    enable_pretty_logging(logging="error", log_to_stderr=False, log_file_prefix=".")

# Generated at 2022-06-14 12:35:59.441549
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LF = LogFormatter(fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s")
    assert LF.formatTime(logging.LogRecord(level=1, pathname=__file__, lineno=100, msg="hello")) == '100'


# Generated at 2022-06-14 12:37:00.223623
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:37:04.312215
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert log_formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    log_formatter = LogFormatter(fmt="%(message)s", datefmt="%Y-%m-%d")
    assert log_formatter.datefmt == "%Y-%m-%d"



# Generated at 2022-06-14 12:37:12.404371
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class MyLogFormatter(LogFormatter):
        def __init__(self) -> None:
            super().__init__(
                fmt=MyLogFormatter.DEFAULT_FORMAT,
                datefmt=MyLogFormatter.DEFAULT_DATE_FORMAT,
                color=False,
                colors=MyLogFormatter.DEFAULT_COLORS,
            )
    assert isinstance(MyLogFormatter(), LogFormatter)

# Shortcuts for writing to the logging streams

# Generated at 2022-06-14 12:37:21.235496
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    test_logger = logging.getLogger('test_logger')
    test_logger.setLevel(logging.DEBUG)
    test_formatter = LogFormatter()
    test_handler = logging.StreamHandler()
    test_handler.setFormatter(test_formatter)
    test_logger.addHandler(test_handler)
    test_logger.warning("\nWARNING_MSG")
    test_logger.error("\nERROR_MSG")
    test_logger.info("\nINFO_MSG")


# Generated at 2022-06-14 12:37:30.449790
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Test that constructor of class LogFormatter works"""
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
    }  # type: Dict[int, int]


# Generated at 2022-06-14 12:37:36.892763
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Unit test for constructor of class LogFormatter"""
    log_formatter = LogFormatter(color=False, colors={1: 1})
    assert isinstance(log_formatter, LogFormatter)
    assert log_formatter._normal == ""
    assert log_formatter._colors == {1: ""}
    assert log_formatter._fmt == log_formatter.DEFAULT_FORMAT



# Generated at 2022-06-14 12:37:45.102951
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter(fmt='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s')
    formatter.datefmt = "%y%m%d %H:%M:%S"
    formatter.format({
        'levelname': 'INFO',
        'asctime': '120102 00:00:00',
        'module': 'module',
        'lineno': 42,
        'message': 'message',
        })

test_LogFormatter_format()



# Generated at 2022-06-14 12:37:49.707780
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()
    LogFormatter(datefmt='%Y-%m-%d')  # type: ignore

# A subclass of LogFormatter that allows color schemes other than the
# default tornado colors.  This should only be used by other
# framework-level code; applications should use the customLogging
# context manager below.

# Generated at 2022-06-14 12:37:54.775682
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    logFormatter = LogFormatter()
    assert isinstance(logFormatter._fmt, str)
    assert isinstance(logFormatter._colors, dict)
    assert isinstance(logFormatter._normal, str)
    assert isinstance(logFormatter.datefmt, str)


# Generated at 2022-06-14 12:38:00.990425
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import sys
    tornado.options.options.logging = "info"
    tornado.options.options.log_file_prefix = "t_basic.log"
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_rotate_when = "midnight"
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_file_num_backups = 5
    tornado.options.options.log_to_stderr = False
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if True:
        rotate_mode = "time"