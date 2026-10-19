

# Generated at 2022-06-14 12:30:59.727423
# Unit test for function define_logging_options
def test_define_logging_options():
    import tornado.options
    options = tornado.options.options
    define_logging_options(options)
    tornado.options.parse_command_line()

# Generated at 2022-06-14 12:31:05.741405
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import unittest
    import logging
    import uuid
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("test")
    from unittest import mock
    from tornado.log import LogFormatter
    mock_log = logging.getLogger("test_log")
    mock_log.setLevel(logging.ERROR)
    mock_log.handlers = []
    mock_handler = mock.Mock()
    mock_handler.setFormatter = mock.Mock()
    mock_handler.setLevel = mock.Mock()
    mock_log.addHandler = mock.Mock()
    mock_log.addHandler.return_value = mock_handler
    message = str(uuid.uuid4())
    mock_record = mock.Mock()
    mock

# Generated at 2022-06-14 12:31:14.688549
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    channel = logging.StreamHandler()
    channel.setFormatter(LogFormatter())
    logger.addHandler(channel)

# Generated at 2022-06-14 12:31:25.446562
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.log import access_log, app_log, gen_log
    assert access_log.handlers
    assert app_log.handlers
    assert gen_log.handlers

    for logger in [access_log, app_log, gen_log]:
        for handler in logger.handlers:
            assert isinstance(handler, logging.StreamHandler)
            assert isinstance(handler.formatter, LogFormatter)

# class LogFormatterTest(unittest.TestCase):
#     def test_format(self):
#         fmt = LogFormatter(color=False)
#         record = logging.LogRecord("foo", logging.INFO, "/fakepath/fake.py",
#                                    42, "test_format", {}, None)
#         record.message = "test %s"
#         record.args = ("unic

# Generated at 2022-06-14 12:31:31.408981
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter()
    assert isinstance(log_formatter, LogFormatter)
    assert log_formatter._fmt == '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
    assert log_formatter.datefmt == '%y%m%d %H:%M:%S'



# Generated at 2022-06-14 12:31:43.093219
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import time
    import logging
    import tornado.log

    logger_name = 'test_logger'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = tornado.log.LogFormatter()
    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')



# Generated at 2022-06-14 12:31:47.791633
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert f is not None

if __name__ == "__main__":
    test_LogFormatter()

# Generated at 2022-06-14 12:31:57.602132
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    import logging.handlers
    import time
    # create logger
    logger = logging.getLogger("simple_example")
    logger.setLevel(logging.INFO)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    # create formatter
    formatter = LogFormatter(
        fmt="%(color)s%(levelname)s %(name)s %(asctime)s%(end_color)s %(message)s",
        datefmt="[%d/%b/%Y %H:%M:%S %z]",
    )
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    # 'application' code

# Generated at 2022-06-14 12:32:04.144795
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.log import LogFormatter
    import logging
    import os
    import sys

    f = LogFormatter(fmt="%(message)s")
    record = logging.LogRecord("test", logging.warning, os.path.abspath(__file__), 75, 
                                "the message", {}, None)
    s = f.format(record)
    assert s == "the message"


# Generated at 2022-06-14 12:32:11.163281
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(color)s%(levelname)1.1s\t%(filename)s:%(lineno)d%(end_color)s %(message)s",
        datefmt="%H:%M:%S",
    )
    root = logging.getLogger()
    for handler in root.handlers:
        assert isinstance(handler, logging.StreamHandler)
        assert isinstance(handler.formatter, LogFormatter)



# Generated at 2022-06-14 12:32:25.937128
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    f = LogFormatter(fmt)
    # This ought to throw a KeyError
    # noinspection PyStatementEffect
    f.format(logging.makeLogRecord({"msg": "foo"}))



# Generated at 2022-06-14 12:32:34.395716
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    class TestOptions(tornado.options.Options):
        def __init__(self):
            super(TestOptions, self).__init__()
            self.__dict__ = {
                'logging': 'info',
                'log_file_prefix': '/tmp/test_logging',
                'log_rotate_mode': 'size',
                'log_file_max_size': 10,
                'log_file_num_backups': 1,
                'log_rotate_when': 'midnight',
                'log_rotate_interval': 1,
                'log_to_stderr': False,
            }

    enable_pretty_logging(TestOptions())

if __name__ == '__main__':
    # this script will be run as a module
    test_enable_

# Generated at 2022-06-14 12:32:41.624664
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    g = f.format(logging.__dict__['LogRecord']('tornado.access', logging.INFO, 'FILE_NAME', 22, 'MESSAGE', (), 'func', 'args', None, 'newlines_replacement', 'thread_name', None))
    assert isinstance(g, str)
    assert g == "[I 22222222 FILE_NAME:22] MESSAGE"

# Generated at 2022-06-14 12:32:51.485587
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    mylogger = logging.getLogger()
    mylogger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

# Generated at 2022-06-14 12:32:55.526902
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = log.getLogger("foo")
    logger.setLevel(log.DEBUG)
    logger.addHandler(log.StreamHandler())
    logger.warn("foo %s", "bar")
    assert True
    # TODO: write this test
    pass


# Generated at 2022-06-14 12:33:06.847823
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_formatter = LogFormatter()
    class Record(object):
        def __init__(self, levelno: int, message: str) -> None:
            self.levelno = levelno
            self.message = message
            self.asctime = ""
            self.color = ""
            self.end_color = ""
            self.exc_text = ""
            self.exc_info = None
    record1 = Record(logging.INFO, "message1")
    record2 = Record(logging.WARNING, "message2")
    record3 = Record(logging.ERROR, "message3")
    record4 = Record(logging.CRITICAL, "message4")
    assert log_formatter.format(record1) == "\n    [I  message1]"
    assert log_formatter.format(record2)

# Generated at 2022-06-14 12:33:18.485800
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    f = LogFormatter()
    record = lambda **kwargs: dict(__dict__=kwargs)
    assert f.format(record(message="foo")) == "foo"
    f = LogFormatter(color=False)
    assert f.format(record(message="foo")) == "foo"
    assert f.format(record(message="foo", levelno=logging.DEBUG)) == "foo"
    assert f.format(record(message=u"foo")) == u"foo"
    assert f.format(record(message=b"foo")) == "foo"
    assert f.format(record(message=b"foo\xe9")) == "foo\xe9"
    assert f.format(record(message=u"foo\xe9")) == u"foo\xe9"

# Generated at 2022-06-14 12:33:19.670737
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()  # type: ignore


# Generated at 2022-06-14 12:33:23.138884
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter.DEFAULT_FORMAT == formatter._fmt
    assert formatter.DEFAULT_DATE_FORMAT == formatter._datefmt



# Generated at 2022-06-14 12:33:23.714160
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass



# Generated at 2022-06-14 12:33:34.103522
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    options = {'logging': 'none'}
    LogFormatter(options)

# Generated at 2022-06-14 12:33:42.839625
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.testing import AsyncTestCase, gen_test
    formatter = LogFormatter()
    import logging
    record = logging.LogRecord("tornado.application", logging.WARN, msg="this is a test",
            args=[], exc_info=None, func='_stderr_supports_color', sinfo='', lno=0)
    s = formatter.format(record)
    assert s == '[W   20190123 16:46:21 _stderr_supports_color:0] this is a test'
    record = logging.LogRecord("tornado.application", logging.ERROR, msg="this is a test",
            args=[], exc_info=None, func='_stderr_supports_color', sinfo='', lno=0)
    s = formatter.format(record)

# Generated at 2022-06-14 12:33:50.685953
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    class Options(object):
        log_to_stderr = True
        logging = "debug"
        log_rotate_mode = "size"
        log_file_prefix = "test_log_file_prefix"
        log_file_max_size = 1024
        log_file_num_backups = 2
        log_rotate_when = "S"
        log_rotate_interval = 1

    options = Options()
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:34:00.526526
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # The function is based on the one in the tornado source code, but it
    # removes some code that cannot be run in a unit test (uses colorama)
    # and it does not have the html support
    from tornado import stack_context
    import tornado.options
    import tornado.ioloop
    from tornado.log import app_log
    from tornado.util import ObjectDict
    import contextlib

    class DummyHandler(object):
        def __init__(self):
            self.formatter = LogFormatter()
            self.emitted = []  # type: List[str]

        def emit(self, record):
            # type: (Any) -> None
            self.emitted.append(self.formatter.format(record))


# Generated at 2022-06-14 12:34:04.854795
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter._colors == LogFormatter.DEFAULT_COLORS
    assert formatter._normal == ""


# Generated at 2022-06-14 12:34:05.761118
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()



# Generated at 2022-06-14 12:34:08.963452
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    import logging

    with tornado.log.enable_pretty_logging():
        logging.info("test1")
        tornado.options.options.log_to_stderr = False
    logging.info("test2")

# Generated at 2022-06-14 12:34:15.326354
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, LogFormatter)
    assert formatter._normal == ""
    assert formatter._colors == {}
    assert formatter.DEFAULT_DATE_FORMAT == "%y%m%d %H:%M:%S"
    assert formatter.datefmt == formatter.DEFAULT_DATE_FORMAT


# Generated at 2022-06-14 12:34:26.205270
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.escape import json_decode, json_encode
    from tornado.options import define, options, parse_command_line
    import tornado.platform.asyncio
    from tornado.web import RequestHandler, Application, asynchronous
    from tornado.httpclient import AsyncHTTPClient
    import time
    import os
    import logging
    import datetime
    import inspect
    import asyncio
    import signal
    import json
    import sys
    
    gen_log.info('test logging')

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:32.079664
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert isinstance(lf._fmt, str)
    assert isinstance(lf._normal, str)
    assert isinstance(lf._colors, dict)

    lf = LogFormatter(
        fmt="test",
        datefmt="test",
        style="test",
        color=True,
        colors={"test": 1},
    )
    assert isinstance(lf._fmt, str)
    assert isinstance(lf._normal, str)
    assert isinstance(lf._colors, dict)



# Generated at 2022-06-14 12:35:12.405138
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import sys
    import mock
    import time
    import datetime
    try:
        time.monotonic = time.monotonic
    except AttributeError:
        # Python 2
        time.monotonic = lambda: datetime.datetime.now()

    out = mock.Mock()
    # Unit tests with logging.handlers.MemoryHandler
    # http://docs.python.org/2/library/logging.handlers.html#logging.handlers.MemoryHandler
    handler = logging.handlers.MemoryHandler(100, target=out)
    handler.setFormatter(LogFormatter())
    # Check if we have colors
    if 'color' in handler.format(logging.makeLogRecord({})).lower():
        color = True
    else:
        color = False

    # Check the message format
   

# Generated at 2022-06-14 12:35:16.397386
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        #Test if the following function will raise a exception
        #If raise a exception, the accuracy is False
        enable_pretty_logging()
        accuracy = True
    except:
        accuracy = False
    XCTAssertTrue(accuracy)

# Generated at 2022-06-14 12:35:19.855560
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options
    define("logging", default="debug")
    options.parse_command_line()
    logger = logging.getLogger()
    enable_pretty_logging()
    # Should not raise exception
    logger.debug("test_log")

# Generated at 2022-06-14 12:35:21.436532
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    _stderr_supports_color()

default_log_formatter = LogFormatter()



# Generated at 2022-06-14 12:35:24.331781
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert isinstance(f, LogFormatter)

# Unit test _stderr_supports_color

# Generated at 2022-06-14 12:35:25.798150
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    pass

# Generated at 2022-06-14 12:35:35.214148
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Setup
    fmt = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
    log = logging.getLogger("tornado.access")
    log.setLevel(logging.DEBUG)
    log.handlers = []
    log.addHandler(logging.StreamHandler(sys.stdout))
    formatter = LogFormatter()
    log.handlers[0].setFormatter(formatter)

    # Execute
    log.info("This is a test for function 'format' of class LogFormatter")

    # Verify
    assert True



# Generated at 2022-06-14 12:35:38.385120
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # pragma: no cover
    fm = LogFormatter()
    res = fm.format(logging.LogRecord("tornado.general", logging.INFO, __file__, 1, "tornado.test", (), None))
    print(res)
    assert res == "[I"



# Generated at 2022-06-14 12:35:50.478009
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    import tornado.log
    import tempfile
    import os
    import stat

    logging.root.handlers[:] = []
    options = tornado.options.Options()
    tornado.log.enable_pretty_logging(options)
    assert len(logging.root.handlers) == 2
    tornado.log.enable_pretty_logging(options)
    assert len(logging.root.handlers) == 2
    options.logging = "DEBUG"
    tornado.log.enable_pretty_logging(options)
    assert len(logging.root.handlers) == 2
    options.logging = "warning"
    tornado.log.enable_pretty_logging(options)
    assert len(logging.root.handlers) == 2

# Generated at 2022-06-14 12:35:54.509617
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    old_stdout = sys.stdout
    sys.stdout = sys.__stdout__  # type: ignore
    try:
        formatter = LogFormatter()
    finally:
        sys.stdout = old_stdout



# Generated at 2022-06-14 12:36:51.609063
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.log_file_prefix = './log/test_enable_pretty_logging'
    options.log_file_max_size = 1 * 1024 * 1024 * 1024
    options.log_file_num_backups = 10
    options.log_rotate_mode = "size"
    options.log_rotate_when = "D"
    options.log_rotate_interval = 1
    options.log_to_stderr = False
    options.logging = "info"
    enable_pretty_logging()
    logger = logging.getLogger()
    logger.info('hello world')
    logger.debug('hello world')
    logger.warn('hello world')
    logger.error('hello world')
    logger.critical('hello world')



# Generated at 2022-06-14 12:37:02.805629
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import unittest
    import logging

    from tornado.log import LogFormatter

    class TestLogFormatter(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger(__name__)

        def test_LogFormatter_basic_message(self):
            log_fmt = LogFormatter()
            record = logging.LogRecord(
                "tornado.general", logging.INFO, "/path/to/log", 42, "message", None, None
            )
            msg = log_fmt.format(record).strip()
            self.assertTrue(msg.startswith('[I '), msg)
            self.assertTrue(msg.endswith(']  message'), msg)

    if __name__ == '__main__':
        unittest.main()




# Generated at 2022-06-14 12:37:03.939534
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:37:16.842646
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import logging
    options = tornado.options.options
    options.logging = "DEBUG"
    options.log_file_prefix = "./test.log"
    options.log_rotate_mode = "size"
    options.log_file_max_size = 1024
    options.log_file_num_backups = 3
    options.log_rotate_when = "S"
    options.log_rotate_interval = 5
    options.log_to_stderr = None
    logger = logging.getLogger()
    assert len(logger.handlers) == 0
    print(logger)
    enable_pretty_logging(options, logger)
    assert isinstance(logger.handlers[0], logging.handlers.RotatingFileHandler)

# Generated at 2022-06-14 12:37:19.692367
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger("tornado.application")
    logger.setLevel(logging.DEBUG)
    enable_pretty_logging(None, logger)
    logger.debug("enable_pretty_logging")

# Generated at 2022-06-14 12:37:29.370951
# Unit test for function enable_pretty_logging

# Generated at 2022-06-14 12:37:40.520431
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.log import access_log, app_log, gen_log
    for logger_obj in [access_log, app_log, gen_log]:
        logger_obj.handlers = []
        logger_obj.addHandler(logging.StreamHandler())
        logger_obj.setLevel(logging.DEBUG)

test_LogFormatter()

# Test that the constructor of LogFormatter has the expected signature.
# This makes sure that it is compatible with the signature in
# `logging.config.dictConfig`.
Dict[str, Any] = {}
try:
    cast(Dict[str, Any], LogFormatter())
except TypeError:
    raise Exception("tornado.log.LogFormatter does not accept the expected constructor arguments")

# set up color if we are in a tty and curses is installed
color = False

# Generated at 2022-06-14 12:37:52.061741
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    try:
        tornado.options.define("log_file_prefix", "./log.log", str)
        tornado.options.define("log_file_max_size", 1024, int)
        tornado.options.define("log_file_num_backups", 10, int)
        tornado.options.define("log_rotate_mode", "size", str)
        tornado.options.define("log_rotate_when", "S", str)
        tornado.options.define("log_rotate_interval", 1, int)
        tornado.options.parse_command_line()
        enable_pretty_logging(tornado.options.options)
    except Exception as e:
        print(e)
        return False

    return True

if __name__ == "__main__":
    test_enable_

# Generated at 2022-06-14 12:37:53.325733
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt

# -----------------------------------------------------------------------------
# --- Functions for use from applications
# -----------------------------------------------------------------------------



# Generated at 2022-06-14 12:38:03.623151
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class TestRecord(object):
        levelno = int
        levelname = str
        asctime = str
        module = str
        lineno = int
        message = str
        color = str
        end_color = str
        exc_info = None
        exc_text = None

    # test LogFormatter
    formatter = LogFormatter()
    out = formatter.format(
        TestRecord()
    )  # type: ignore
    out = out.replace("\n", "")
    # test format style
    assert out[0] == "%"[0]
    # test color
    # assert out[1] == "["[0]
    # test levelname
    assert out[3] == "1"[0]
    # test asctime
    assert out[5] == "2"[0]
    # test module

# Generated at 2022-06-14 12:38:50.688709
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () ->  None
    f = LogFormatter("%(foo)s %(bar)s")
    assert f.format(logging.LogRecord("a", logging.WARNING, "foo.py", 1, "msg", [], ())).strip() == "%(foo)s %(bar)s"
    # class LogFormatter is not callable



# Generated at 2022-06-14 12:38:51.440243
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:38:52.706025
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    x = LogFormatter().format('')
    print(x)


# Generated at 2022-06-14 12:38:54.769654
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:38:58.916557
# Unit test for function define_logging_options
def test_define_logging_options():
    # type: () -> None
    import tornado.options, tornado.options
    options = tornado.options.options
    tornado.options.enable_pretty_logging()
    options = tornado.options.options
    options.logging = None
    options.log_to_stderr = False
    options.log_file_prefix = None
    options.log_file_max_size = None
    tornado.options.enable_pretty_logging()
    options.logging = 'error'
    options.log_file_prefix = 'test.log'
    options.log_file_max_size = 10000
    options.log_file_num_backups = 5
    options.log_rotate_when = 'S'
    options.log_rotate_interval = 2
    options.log_rotate_mode = 'time'

# Generated at 2022-06-14 12:39:02.328635
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._fmt == formatter.DEFAULT_FORMAT
    assert formatter._colors == formatter.DEFAULT_COLORS



# Generated at 2022-06-14 12:39:09.394721
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    fmt = "%(color)s%(levelname)s%(end_color)s %(message)s"
    logging.basicConfig()
    logger = logging.getLogger()
    # check color support
    for enable_color in (True, False):
        handler = logging.StreamHandler()
        handler.setFormatter(LogFormatter(fmt=fmt, color=enable_color))
        assert handler.formatter._colors == {}
        logger.handlers = []
    # check prefix and suffix
    for color_level in range(30, 38):
        handler = logging.StreamHandler()
        handler.setFormatter(
            LogFormatter(fmt=fmt, color=True, colors={logging.INFO: color_level})
        )
        assert handler.formatter._col

# Generated at 2022-06-14 12:39:20.064565
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # Test the placeholders
    formatter = LogFormatter()
    record = logging.LogRecord(
        "tornado.test", logging.INFO, "/fake/path", 1, "message", None, None
    )
    assert "[%s] message" % record.levelname in formatter.format(record)
    records = logging.getLogger("tornado.test").makeRecord(
        "tornado.test", logging.INFO, "/fake/path", 1, "message", None, None
    )
    assert "[%s] message" % records.levelname in formatter.format(records)
    
    # Test the colors
    formatter = LogFormatter(color=True)

# Generated at 2022-06-14 12:39:29.680504
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from tornado.log import enable_pretty_logging, access_log, app_log, gen_log

    tornado.options.define("logging", default="debug")
    tornado.options.define("log_to_stderr", default=True)
    enable_pretty_logging()
    enable_pretty_logging() # test for duplicate calls

    for i in range(100):
        access_log.info("info")
        app_log.warning("warning")
        gen_log.error("error")
        
test_enable_pretty_logging()

##__________________________________________________________________||

# Generated at 2022-06-14 12:39:34.506226
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "%(color)s%(module)s%(end_color)s %(message)s"
    with LogFormatter(fmt, color=True) as f:
        r = logging.makeLogRecord({'module': 'foo'})
        r.msg = 'bar'
        assert f.format(r) == '\x1b[2;37mfoo\x1b[0m bar'

