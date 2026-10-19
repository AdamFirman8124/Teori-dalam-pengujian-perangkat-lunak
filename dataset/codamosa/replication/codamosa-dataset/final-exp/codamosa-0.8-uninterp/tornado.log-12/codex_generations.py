

# Generated at 2022-06-14 12:31:24.944970
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import io
    import sys
    import tempfile

    # We want to do this as early as possible, otherwise some things
    # (like unpickling from a database) may cause the global state to
    # be changed by something like colorama.
    sys.stdout = tempfile.TemporaryFile()
    sys.stderr = tempfile.TemporaryFile()

    # On windows, colorama gets in the way of our test
    colorama = None
    if sys.platform == "win32":
        try:
            import colorama
        except ImportError:
            pass

# Generated at 2022-06-14 12:31:27.798406
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass

if __name__=="__main__":
    test_LogFormatter_format()

# Generated at 2022-06-14 12:31:34.196314
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.logging = 'debug'
    options.log_file_prefix = 'mylog.txt'
    options.log_rotate_mode = 'time'
    options.log_rotate_when = 'h'
    options.log_rotate_interval = 1
    options.log_file_num_backups = 2
    options.log_to_stderr = True
    enable_pretty_logging(options)

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:36.969184
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger("test")
    enable_pretty_logging(None, logger)

# Generated at 2022-06-14 12:31:47.023159
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    logger.setLevel(100)
    if len(logger.handlers) > 0:
        logger.removeHandler(logger.handlers[0])

    class Options:
        logging = "none"
        log_file_prefix = None
        log_to_stderr = True
        def __init__(self):
            pass
    options = Options()
    enable_pretty_logging(options,logger)
    assert len(logger.handlers) == 0

    class Options:
        logging = "info"
        log_file_prefix = None
        log_to_stderr = True
        def __init__(self):
            pass
    options = Options()
    enable_pretty_logging(options,logger)
    assert len(logger.handlers)

# Generated at 2022-06-14 12:31:53.411216
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # This is the default value
    assert LogFormatter()._fmt == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501

    class MyFormatter(LogFormatter):
        DEFAULT_FORMAT = "%(asctime)s %(message)s"

    assert MyFormatter()._fmt == "%(asctime)s %(message)s"



# Generated at 2022-06-14 12:32:05.240314
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    tornado.options.define('log_rotate_interval', 1)
    tornado.options.define('log_file_num_backups', 1)
    tornado.log.enable_pretty_logging(options=tornado.options.options)
    # test_logging_set_level
    def test_logging_set_level():
        import tornado.log
        tornado.log.enable_pretty_logging(options=tornado.options.options)
        tornado.log.app_log.setLevel(50)
        tornado.log.app_log.warning('test_logging_set_level')

    # test_logging_handlers_remove
    def test_logging_handlers_remove():
        import tornado.log
        tornado.log.enable_pretty_log

# Generated at 2022-06-14 12:32:09.500994
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter._colors == {}
    assert formatter._normal == ""
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT



# Generated at 2022-06-14 12:32:13.852861
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    def test(color: bool) -> None:
        formatter = LogFormatter(color=color)
        assert formatter is not None

    test(True)
    test(False)



# Generated at 2022-06-14 12:32:23.332486
# Unit test for function define_logging_options
def test_define_logging_options():
    from tornado.options import define, parse_command_line
    define('log_rotate_mode', type=str, default="size",
           help="The mode of rotating files(time or size)")
    define('log_rotate_when', type=str, default="midnight",
           help="specify the type of TimedRotatingFileHandler interval "
                "other options:('S', 'M', 'H', 'D', 'W0'-'W6')")
    define('log_rotate_interval', type=int, default=1, help="The interval value of timed rotating")
    parse_command_line()
    define_logging_options()
    enable_pretty_logging()


# Generated at 2022-06-14 12:32:40.456376
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    A = LogFormatter() # type: ignore
    B = LogFormatter() # type: ignore
    assert A != B

# Because of the way we match names to arguments, this must be a function
# rather than a class method.

# Generated at 2022-06-14 12:32:50.718217
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=False)
    assert formatter._colors == {}
    assert formatter._normal == ""
    assert isinstance(formatter, logging.Formatter)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        LogFormatter(colors={logging.DEBUG: 4})
        assert len(w) == 0

    # Test bad type for 'colors' argument
    with pytest.raises(AssertionError):
        LogFormatter(colors={4: 'nope'})
    # Test key not int
    with pytest.raises(AssertionError):
        LogFormatter(colors={'oh': 4})
    # Test value not int
    with pytest.raises(AssertionError):
        LogFormatter

# Generated at 2022-06-14 12:33:01.746752
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    import logging.config

    import tornado.log
    import tornado.options
    import tornado.platform.asyncio
    import tornado.platform.twisted

    import unittest
    import unittest.mock

    @staticmethod
    def remove_log_handler(logger: Optional[logging.Logger], handler: logging.Handler) -> None:
        if logger is not None:
            handlers = logger.handlers
            for _handler in handlers:
                if _handler is handler:
                    handlers.remove(_handler)

    class TestLogFormatter(unittest.TestCase):
        def setUp(self):
            # Can't use the global config files to avoid messing up the tests
            # that rely on them.
            self.root_logger = logging.getLogger()

# Generated at 2022-06-14 12:33:04.023044
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    dates = LogFormatter(datefmt='datefmt')
    dt = dates.formatTime(None, None)
    assert dt == dates.datefmt

# Generated at 2022-06-14 12:33:06.675524
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    record = logging.LogRecord('tornado.general', logging.DEBUG, '/foo.py', 5,
                               'hello %s', ('world',), None, None)
    message = formatter.format(record)
    assert isinstance(message, str)

_default_log_handler = None  # type: Optional[logging.Handler]


# Generated at 2022-06-14 12:33:17.613661
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    def _test_LogFormatter_format_1(obj, log_record, log_msg):
        obj.format(log_record)
        output = log_record.message + '\n' + log_record.exc_text
        assert log_msg == output

    _test_LogFormatter_format_1(LogFormatter(datefmt='%Y-%m-%d %H:%M:%S'), logging.LogRecord('test', logging.DEBUG, '/home/dumbhippo/code/hippo-web/tornado/testing/test_tornado.py', 10, 'test log message\nsecond line', args=None, exc_info=None, func=None), "test log message\nsecond line")
_test_LogFormatter_format()


# Generated at 2022-06-14 12:33:24.691712
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Create a string for logging
    first_str = "first string for logging"
    # Create a LogRecord object with message as first_str and set levelno to INFO
    record = logging.LogRecord(
        "tornado.access", logging.INFO, "/", 21, first_str, {}, None)
    # Create a LogFormatter object with style string, color and date format
    str_style = "%"
    bool_color = True
    str_date_format = "%y%m%d %H:%M:%S"
    myFormatter = LogFormatter(str_style, str_date_format, bool_color)
    # Call format method with record object to get the formatted string
    result_str = myFormatter.format(record)
    assert first_str and record.message in result_str



# Generated at 2022-06-14 12:33:36.206534
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class _Record(object):
        def __init__(self, level, message):
            self.levelno = level
            self.getMessage = lambda: message
            self.exc_info = None
            self.exc_text = None

    formatter = LogFormatter()
    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR]:
        record = _Record(level, basestring_type("hello"))
        assert formatter.format(record)
        assert isinstance(formatter.format(record), unicode_type)
        assert formatter.format(_Record(level, b"hello"))
        assert formatter.format(_Record(level, u"hello"))
        assert formatter.format(_Record(level, u"\u1234"))

# Generated at 2022-06-14 12:33:40.357202
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    testing = LogFormatter(datefmt="%y%m%d %H:%M:%S")
    assert testing.datefmt == "%y%m%d %H:%M:%S"
    assert testing._fmt == testing.DEFAULT_FORMAT
    assert testing._colors == {}
    assert testing._normal == ""



# Generated at 2022-06-14 12:33:43.326448
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    tornado.options.parse_command_line(args=['--logging=none'])
    enable_pretty_logging(logger = app_log)
    app_log.info('testing %s', 'logging')

# Generated at 2022-06-14 12:34:30.017553
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    print("\nNow in function test_enable_pretty_logging()")
    import tornado.options
    tornado.options.parse_command_line(["--logging=debug"])
    enable_pretty_logging()
    # print(type(access_log)) <class 'logging.Logger'>
    access_log.debug("access")
    app_log.debug("app")
    gen_log.debug("gen")
    gen_log.error("error")


# Generated at 2022-06-14 12:34:43.518993
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    options = tornado.options
    options.logging = 'none'
    assert logger.handlers == []
    enable_pretty_logging(options)
    assert logger.handlers == []
    options.logging = "info"
    options.log_file_prefix = 'test'
    options.log_rotate_mode = 'size'
    options.log_file_max_size = 5
    options.log_file_num_backups = 1
    enable_pretty_logging(options)
    assert len(logger.handlers) == 1
    assert type(logger.handlers[0]) == logging.handlers.RotatingFileHandler
    assert logger.handlers[0].maxBytes == 5
    assert logger.handlers[0].backupCount == 1
    assert logger

# Generated at 2022-06-14 12:34:44.798263
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:34:46.072415
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    LogFormatter().format('test')
    LogFormatter().format()




# Generated at 2022-06-14 12:34:53.633237
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    if not tornado.options.options.log_file_prefix:
        tornado.options.define("log_file_prefix", type=str, default=None)
    if not tornado.options.options.log_rotate_mode:
        tornado.options.define("log_rotate_mode", type=str, default="size")
    if not tornado.options.options.log_file_max_size:
        tornado.options.define("log_file_max_size", type=int, default=104857600)
    if not tornado.options.options.log_file_num_backups:
        tornado.options.define("log_file_num_backups", type=int, default=5)

# Generated at 2022-06-14 12:35:03.646984
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line

    # logging is None:
    define("logging", type=str, default=None)
    parse_command_line(args=[])
    enable_pretty_logging()
    # logging is 'none':
    define("logging", type=str, default="none")
    parse_command_line(args=[])
    enable_pretty_logging()
    # logging is anything else:
    define("logging", type=str, default="info")
    define("log_file_prefix", type=str, default="/var/tmp/tornado_test.log")
    parse_command_line(args=[])
    enable_pretty_logging()
    # log_to_stderr is False:
    options.log_to_stderr = False
    enable

# Generated at 2022-06-14 12:35:15.296879
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import doctest
    import tempfile
    import time

    try:
        import unittest2 as unittest  # type: ignore
    except ImportError:
        import unittest  # type: ignore

    @unittest.skipIf(colorama is None, "no colorama module")
    class LogFormatterColoramaInitTest(unittest.TestCase):
        def test_colorama_init(self):
            from tornado.log import LogFormatter

            colorama.init()
            try:
                f = LogFormatter()
                self.assertTrue(f is not None)
            finally:
                colorama.deinit()

    # Change log level of tornado.access to avoid unneded logs
    access_log.setLevel(logging.ERROR)


# Generated at 2022-06-14 12:35:22.869960
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # fmt: off
    assert LogFormatter(
        fmt="%(color)s%(asctime)s%(end_color)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        colors={
            logging.DEBUG: 4,
            logging.INFO: 2,
            logging.WARNING: 3,
            logging.ERROR: 1,
            logging.CRITICAL: 5,
        },
    )._fmt == "%(color)s%(asctime)s%(end_color)s [%(levelname)s] %(message)s"
    # fmt: on



# Generated at 2022-06-14 12:35:31.245966
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # create a log record
    record = logging.LogRecord(
        "tornado.access",
        logging.INFO,
        "D:\\A\\tornado-4.4.1\\tornado\\log.py",
        48,
        "A",
        (None, None, None),
        None,
    )
    # create a log formatter
    formatter = LogFormatter()
    # run the actual method
    formatter.format(record)
    # assert the result
    assert record.asctime[12:] == "00:00:00"


# Generated at 2022-06-14 12:35:35.805769
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # mock the options
    class Options():

        def __init__(self, logging = "none", log_file_prefix = "test_enable_pretty_logging.log", log_rotate_mode = "size", log_file_max_size = 123456, log_file_num_backups = 6, log_to_stderr = True):
            self.logging = logging
            self.log_file_prefix = log_file_prefix
            self.log_rotate_mode = log_rotate_mode
            self.log_file_max_size = log_file_max_size
            self.log_file_num_backups = log_file_num_backups
            self.log_to_stderr = log_to_stderr
    test_options = Options()
    test_logger = logging

# Generated at 2022-06-14 12:36:00.471827
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    print(enable_pretty_logging())

# Generated at 2022-06-14 12:36:03.549578
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    logger = logging.getLogger()
    logger.error('test')

if __name__=="__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:36:12.338366
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import logging

    log = logging.getLogger("test")
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    log.addHandler(handler)

    # Exercise the color handling
    if _stderr_supports_color():
        import curses

    handler.setFormatter(LogFormatter())
    log.debug("test debug")
    log.info("test info")
    log.warn("test warn")
    log.warning("test warn")
    log.error("test error")
    log.critical("test critical")

    # Exercise the format handling
    fmt = "%(msecs)d %(message)s %(name)s"
    handler.setFormatter(LogFormatter(fmt=fmt))
    log.debug("test debug")

    # Excercise the str

# Generated at 2022-06-14 12:36:21.697667
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logFormatter = LogFormatter()
    assert isinstance(logFormatter, LogFormatter)
    assert isinstance(logFormatter._colors, dict)
    assert isinstance(logFormatter.DEFAULT_COLORS, dict)
    assert isinstance(logFormatter.DEFAULT_FORMAT, str)
    assert isinstance(logFormatter.DEFAULT_DATE_FORMAT, str)
    assert logFormatter._normal == ""
    assert logFormatter.datefmt == logFormatter.DEFAULT_DATE_FORMAT
    assert logFormatter._fmt == logFormatter.DEFAULT_FORMAT


# Generated at 2022-06-14 12:36:29.726773
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert f.DEFAULT_COLORS[logging.CRITICAL] == 5
    assert f.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert f.DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501



# Generated at 2022-06-14 12:36:32.936771
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    import os

    try:
        os.remove("./tornado.log")
    except:
        pass

    tornado.options.define("logging", default="DEBUG")
    tornado.opt

# Generated at 2022-06-14 12:36:37.967412
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert isinstance(LogFormatter(color=True), LogFormatter)
    assert isinstance(LogFormatter(color=False), LogFormatter)
    assert isinstance(LogFormatter(color=None), LogFormatter)


# Generated at 2022-06-14 12:36:49.430755
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # backend _logging
    import logging
    import logging.config

    # class LogRecord
    # class Logger
    # class StreamHandler
    # class Formatter

    # class RotatingFileHandler
    # class TimedRotatingFileHandler

    # class options
    # class options:
    #     def __init__(self):
    #         self.logging = "error"
    #         self.log_file_prefix = None
    #         self.log_to_stderr = None
    #         self.log_rotate_mode = None
    #         self.log_rotate_when = None
    #         self.log_file_num_backups = None
    #         self.log_rotate_interval = None
    #         self.log_file_max_size = None
    #         self

# Generated at 2022-06-14 12:36:54.890158
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Test for tornado.log.enable_pretty_logging
    import tornado.options
    from tornado.log import gen_log

    tornado.options.define("size", default=100, help="size help")
    tornado.options.parse_command_line(["myprog.py", "--size=1024"])



# Generated at 2022-06-14 12:37:04.640900
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options, parse_command_line
    from tornado.log import app_log

    def test_enable_pretty_logging(
        options, default_logging, default_log_file_prefix, default_log_to_stderr
    ):
        app_log.propagate = True
        app_log.handlers = []

        enable_pretty_logging(options)
        assert options.log_to_stderr == default_log_to_stderr
        handlers = app_log.handlers
        assert len(handlers) == (2 if default_log_to_stderr else 1)
        assert isinstance(handlers[0], logging.handlers.RotatingFileHandler)
        assert handlers[0].baseFilename == default_log_file_prefix
        assert app_log.level

# Generated at 2022-06-14 12:38:02.392098
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():

    import tornado.options
    import logging
    import os
    
    tornado.options.define("logging", default='error', type=str)
    tornado.options.define("log_file_prefix", default=os.path.join(os.getcwd(), "log", "test.log"), type=str)
    tornado.options.define("log_to_stderr", default=True, type=bool)
    tornado.options.define("log_file_max_size", default=1024*1024*1024, type=int)
    tornado.options.define("log_file_num_backups", default=5, type=int)
    tornado.options.define("log_rotate_mode", default="time", type=str)
    tornado.options.define("log_rotate_when", default="S", type=str)
   

# Generated at 2022-06-14 12:38:05.092347
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    """Unit test for function enable_pretty_logging"""
    pass


if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:14.660446
# Unit test for method format of class LogFormatter

# Generated at 2022-06-14 12:38:24.571508
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter().DEFAULT_FORMAT == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    assert LogFormatter().DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert LogFormatter().DEFAULT_COLORS == {logging.DEBUG: 4, logging.INFO: 2, logging.WARNING: 3, logging.ERROR: 1, logging.CRITICAL: 5}  # noqa: E501



# Generated at 2022-06-14 12:38:28.838888
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = None
    logger = None
    enable_pretty_logging(options,logger)

# Generated at 2022-06-14 12:38:36.146888
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # 需要抛出异常的方式
    try:
        # record是logging的一个类属性
        formatter = LogFormatter()
        record = logging.RootLogger.makeRecord("", logging.DEBUG, "", 0, "")
        formatter.format(record)
    except Exception as e:
        print("抛出异常")

    # 不需要抛出异常的方式
    formatter = LogFormatter()
    record = logging.RootLogger.makeRecord("", logging.DEBUG, "", 0, "")
    a = formatter.format(record)
    print(a)



# Generated at 2022-06-14 12:38:37.597240
# Unit test for constructor of class LogFormatter
def test_LogFormatter(): # type: ignore
    assert LogFormatter()


# Generated at 2022-06-14 12:38:51.074772
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class fake_log(object):
        def __init__(self, name):
            self.name = name
            self.msg = None
            self.level = 0
            self.asctime = "test"

    class fake_record(object):
        def __init__(self):
            self.levelno = 0
            self.name = "test"
            self.msg = 'test message'
            self.asctime = "2019-03-03"
            self.exc_info = None
            self.exc_text = None

    def test_format(fmt: str) -> bool:
        formatter = LogFormatter(fmt)
        record = fake_record()
        record.__dict__['getMessage'] = lambda: "test message"

# Generated at 2022-06-14 12:38:52.020517
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()



# Generated at 2022-06-14 12:38:52.581803
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()