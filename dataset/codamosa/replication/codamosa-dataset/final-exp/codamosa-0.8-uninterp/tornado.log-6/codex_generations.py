

# Generated at 2022-06-14 12:30:58.835070
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:10.348979
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    n = LogFormatter.DEFAULT_FORMAT
    assert '%(color)' in n
    assert '%(end_color)' in n
    assert '%(levelname)' in n
    assert '%(asctime)' in n
    assert '%(module)' in n
    assert '%(lineno)' in n
    assert '%(message)' in n
    print('test_LogFormatter_format(): ok')

test_LogFormatter_format()

# A handy short alias
_log_color = LogFormatter.__dict__["_colors"]  # type: ignore

# Format strings for use with the logging module.
# Some of these will be overridden by config options.
# Don't use these directly; instead use `gen_log.info()`, etc.


# Generated at 2022-06-14 12:31:22.518398
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s"
    datefmt = "%y%m%d %H:%M:%S"
    test_log = LogFormatter(fmt, datefmt)
    record = logging.LogRecord(level=1, filename="filename", lineno=12, msg="test_msg")
    record.__setattr__("funcName", "test_func")
    record.__setattr__("created", 1508912116.577042)
    record.__setattr__("msecs", 176.0)
    res = test_log.format(record)  # type: ignore
    # assert res == "[I yyyy-mm-dd H:M:S filename:12

# Generated at 2022-06-14 12:31:29.142618
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    msg = "foooo"
    logger = logging.getLogger()
    log = LogFormatter()
    assert log.format(logger.makeRecord(name=name, level=0, fn="", lno=0, msg=msg, args=(), exc_info=None, func=None)) == "[D 0 message]"  # noqa: E501

# Generated at 2022-06-14 12:31:35.336263
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # set up
    color_enabled = _stderr_supports_color()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    record = logging.LogRecord(
        name="tornado.access",
        level=logging.INFO,
        pathname="",
        lineno=0,
        msg="adfafdasdf",
        args=(),
        exc_info=None,
    )
    fmt = LogFormatter().format(record)
    # test
    assert "Delegate" in fmt

# Generated at 2022-06-14 12:31:42.637457
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Create a mock LogRecord object
    record = logging.LogRecord('message', 'INFO', 'module', 1, 
                               'logged message', None, None, None)
    # Create a LogFormatter object
    lf = LogFormatter()
    
    assert lf.format(record) == '[I %s module:1] logged messa' % lf.formatTime(record, lf.datefmt)

 

# Generated at 2022-06-14 12:31:54.258692
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    args = "--log_to_stderr --log_rotate_mode=size --log_file_max_size=1024 --log_file_num_backups=10 --logging=debug".split()
    # print(args)
    tornado.options.parse_command_line(args)
    # print(tornado.options.options)
    enable_pretty_logging()
    # Use tornado log format for test
    for i in range(100):
        logging.debug(i)
        logging.info(i)
        logging.warn(i)
        logging.error(i)
        logging.critical(i)
if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:56.662587
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Assert function call
    if __name__ == "__main__":
        enable_pretty_logging()

# Generated at 2022-06-14 12:32:01.000355
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    enable_pretty_logging(logger=logger)
    assert logger.handlers
    for handler in logger.handlers:
        assert len(handler.formatter._fmt) > 10

# Generated at 2022-06-14 12:32:11.641252
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from inspect import isfunction, getargspec
    import datetime

    print("run test_LogFormatter_format()")
    log_formatter_format = LogFormatter.format
    argspec = getargspec(log_formatter_format)
    assert isfunction(log_formatter_format)
    for arg_name in argspec.args:
        assert arg_name in ('self', 'record')
    default_arg_names = argspec.args[-len(argspec.defaults):]
    assert default_arg_names == tuple()
    assert argspec.varargs == None
    assert argspec.keywords == None
    assert argspec.defaults == tuple()
    assert argspec.kwonlyargs == tuple()
    assert argspec.kwonlydefaults == None
    # Test the color support
    log_formatter

# Generated at 2022-06-14 12:32:30.570038
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    a = LogFormatter(datefmt='%y%m%d %H:%M:%S')
    class Record:
        def __init__(self):
            self.msg = "test_message"
            self.levelname = "test_levelname"
            self.levelno = 5
            self.pathname = "test_pathname"
            self.filename = "test_filename"
            self.module = "test_module"
            self.lineno = 10
            self.funcname = "test_funcname"
            self.created = 25

    class TestException:
        def __str__(self):
            return "test_exception"

    r = Record()
    r.exc_info = ()  # type: ignore
    r.exc_text = "test_exc_text"
    r.msg

# Generated at 2022-06-14 12:32:42.527110
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
    datefmt = '%y%m%d %H:%M:%S'
    style = '%'
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    formatter = LogFormatter(fmt, datefmt, style, color, colors)


# Generated at 2022-06-14 12:32:52.403248
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lfm = LogFormatter()
    record = object()
    record.__dict__ = {}
    record.__dict__['message'] = 'message'
    record.__dict__['asctime'] = 'asctime'
    record.__dict__['color'] = 'color'
    record.__dict__['end_color'] = 'end_color'
    record.__dict__['exc_info'] = None
    record.__dict__['exc_text'] = None
    lfm.format(record)


# Generated at 2022-06-14 12:33:03.959269
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(level=logging.DEBUG)
    log_msg = "log_msg"
    app_log.debug(log_msg)
    assert app_log.handlers[0].formatters[0]._fmt == "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s", "Constructor of LogFormatter failed on fmt argument."
    assert app_log.handlers[0].formatters[0].datefmt == "%y%m%d %H:%M:%S", "Constructor of LogFormatter failed on datefmt argument."
    assert app_log.handlers[0].formatters[0]._normal == "", "Constructor of LogFormatter failed on color argument."

# Generated at 2022-06-14 12:33:08.942068
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class FakeRecord(object):
        pass
    log_record = FakeRecord()
    log_record.__dict__ = {"message": "Hello World!"}
    formatter = LogFormatter()
    s = formatter.format(log_record)
    assert s == "[I 170302 12:00:00 <string>:0] Hello World!\n    "



# Generated at 2022-06-14 12:33:12.833451
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter(color=True)
    record = logging.LogRecord(
        name='',
        level=logging.INFO,
        pathname='',
        lineno=0,
        msg="",
        args=[],
        exc_info=None
    )
    result = formatter.format(record)
    print(result)
# test_LogFormatter_format()


# Generated at 2022-06-14 12:33:24.392561
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tempfile
    import time
    import os.path
    import logging.handlers
    import os

    # write a bunch of log lines, rotating between 5 and 6 files
    for i in range(1000):
        tornado.options.options.log_file_prefix = tempfile.mktemp()
        tornado.options.options.log_to_stderr = False
        tornado.options.options.logging = "debug"
        tornado.options.options.log_rotate_mode = "size"
        tornado.options.options.log_file_max_size = 2000
        tornado.options.options.log_file_num_backups = 5
        enable_pretty_logging()
        logging.info("test %d", i)
        time.sleep(0.01)


# Generated at 2022-06-14 12:33:26.041948
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()
    # You could add other test cases here...



# Generated at 2022-06-14 12:33:29.186198
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(None, None)

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:33:35.541210
# Unit test for function define_logging_options
def test_define_logging_options():
    import tornado.options
    options = tornado.options.options
    tornado.options.define_logging_options(options)
   
    options.parse_config_file('config')
    print(options.parse_config_file('config'))
    print(options.logging)
    print(options.log_file_prefix)
    print(options.log_to_stderr)
    print(options.log_file_max_size)
    print(options.log_file_num_backups)
    print(options.log_rotate_when)
    print(options.log_rotate_mode)
    print(options.log_rotate_interval)
    print(options.enable_pretty_logging)
if __name__ == '__main__':
    test_define_logging_options()

# Generated at 2022-06-14 12:33:55.660808
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.options
    from tornado.options import options
    from tornado.options import options
    from tornado.options import options

    tornado.options.options = options
    tornado.options.options = options
    tornado.options.options = options

    if options.logging is None or options.logging.lower() == "none":
        return
    if logger is None:
        logger = logging.getLogger()
    logger.setLevel(getattr(logging, options.logging.upper()))
    if options.log_file_prefix:
        rotate_mode = options.log_rotate_mode

# Generated at 2022-06-14 12:33:58.979661
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    "Unit Test for LogFormatter"
    # Test format error
    try:
        LogFormatter(fmt="Foo %(not-exists)s")
    except KeyError:
        pass
    else:
        raise Exception("Test for log format error failed")



# Generated at 2022-06-14 12:34:00.021100
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:34:08.564345
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()

# Override the default logging classes in the logging package
logging.Logger.manager.loggerClass = Logger
logging.setLoggerClass(Logger)  # type: ignore

# Set up a logger with our application log formatter
_default_logger = logging.getLogger()
for handler in _default_logger.handlers:
    if isinstance(handler, logging.StreamHandler):
        _default_logger.removeHandler(handler)
        break
_default_handler = logging.StreamHandler()
_default_handler.setFormatter(LogFormatter())
_default_logger.addHandler(_default_handler)
_default_logger.setLevel(logging.INFO)



# Generated at 2022-06-14 12:34:21.675705
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import options, define

    class OptionMixin(object):
        def __init__(self, **kwargs):
            self.values = {}
            self.default_values = {}
            for k, v in kwargs.items():
                self.__dict__[k] = v
                self.values[k] = v
                define(k, v)

        def __getattr__(self, name):
            return self.values[name]

    options.logging = "info"
    options.log_to_stderr = True
    options.log_rotate_mode = "time"
    options.log_file_prefix = "test.log"
    options.log_rotate_when = "S"
    options.log_rotate_interval = 1
    options.log_file_num

# Generated at 2022-06-14 12:34:24.485362
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:26.094177
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(options=None,logger=None)



# Generated at 2022-06-14 12:34:34.014632
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # type: () -> None
    def test(
        fmt,  # type: str
        datefmt,  # type: Optional[str]
        level,  # type: int
        msg,  # type: str
        exc_info,  # type: Optional[str]
        result,  # type: str
    ):
        # type: (...) -> None
        formatter = LogFormatter(fmt, datefmt)
        record = logging.LogRecord("tornado.general", level, "/fake/path/file", 1, msg, None, None, None)  # noqa: E501
        if exc_info is not None:
            record.exc_info = exc_info
        assert formatter.format(record) == result


# Generated at 2022-06-14 12:34:41.121271
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    fmt = LogFormatter(color=False, fmt='%(asctime)s')
    test_record = logging.LogRecord(
        name="foo",
        level=logging.DEBUG,
        pathname="/foo/bar.py",
        lineno=123,
        msg="hello",
        args=None,
        exc_info=None,
    )
    fmt.format(test_record)



# Generated at 2022-06-14 12:34:42.794110
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf is not None


# Generated at 2022-06-14 12:35:01.267877
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    import logging.handlers
    from tornado.log import LogFormatter
    from io import StringIO

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(LogFormatter())
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.DEBUG)

    logging.info("Hello, world!")
    logging.warning("Hello, world!")
    logging.error("Hello, world!")
    logging.info("Hello, %s!", "world")

    logging.info("Goodbye, world!")
    logging.info("Testing %r", 123)

    try:
        raise ValueError("some error")
    except ValueError:
        logging.exception("Got an error")

    logging.root.removeHandler(handler)
    log_data

# Generated at 2022-06-14 12:35:02.070297
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()


# Generated at 2022-06-14 12:35:08.937512
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger("tornado.test")
    formatter = LogFormatter()
    logger.handlers[0].setFormatter(formatter)
    logger.error("test error message")
    assert logger.handlers[0].stream.getvalue() == "[E 20000101 16:00:00 test:0] test error message\n"  # noqa: E501



# Generated at 2022-06-14 12:35:14.344608
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = LogFormatter(fmt=log_format)
    assert formatter._fmt == log_format
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT


# Generated at 2022-06-14 12:35:16.092002
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=True)
    assert formatter is not None



# Generated at 2022-06-14 12:35:24.439678
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        enable_pretty_logging()
    except ValueError:
        pass
    else:
        raise AssertionError("ValeError not raised when expected")
    try:
        enable_pretty_logging(options={"log_rotate_mode": "size"})
    except ValueError:
        pass
    else:
        raise AssertionError("ValeError not raised when expected")



# Generated at 2022-06-14 12:35:35.128458
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado import gen

    # Pretty much copied from test_logging in the standard library
    formatter = LogFormatter()

    class MyLogRecord(object):
        def __init__(self, msg, a, b):
            self.msg = msg
            self.args = (a, b)
            self.levelno = logging.DEBUG

    def _test_formatter(msg, args, expected):
        record = MyLogRecord(msg, *args)
        formatter.format(record)
        actual = record.message
        assert actual == expected, (
            "%r != %r (%r, %r)" % (actual, expected, msg, args)
        )

    _test_formatter("%s %s", ("foo", "bar"), "foo bar")
    _test_formatter("no args", (), "no args")


# Generated at 2022-06-14 12:35:43.052631
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Unit tests for constructor of class LogFormatter"""

    import os
    import tempfile

    def get_colorama_init_stderr() -> Optional[Any]:
        if not colorama:
            return None
        else:
            return getattr(colorama, "_orig_stderr", None)

    # No colorama
    orig_colorama_stderr = get_colorama_init_stderr()
    LogFormatter()
    assert orig_colorama_stderr == get_colorama_init_stderr()

    # Colorama but no stderr
    orig_colorama_stderr = get_colorama_init_stderr()
    colorama.init()
    assert orig_colorama_stderr != get_colorama_init_stderr()
    assert _stderr

# Generated at 2022-06-14 12:35:49.217233
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import logging
    logFormatter = LogFormatter()

    aRecord = logging.LogRecord(
        name='',
        level=logging.INFO,
        pathname='',
        lineno=0,
        msg='',
        args=(),
        exc_info=None
    )


# Generated at 2022-06-14 12:36:01.404487
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import tornado
    import time
    import tornado.log
    import tornado.httpserver
    import tornado.options
    import tornado.ioloop
    import tornado.web
    import logging
    import logging.config
    import tempfile
    import os
    import unittest

    class LogFormatterTest(unittest.TestCase):
        def test_inheritance(self):
            self.assertIsInstance(tornado.log.LogFormatter(), logging.Formatter)

        def test_format(self):
            formatter = tornado.log.LogFormatter(color=False)
            record = logging.LogRecord(
                name="tornado.general", level=logging.INFO, pathname="fakepath", lineno=2, msg="test", args=None, exc_info=None
            )
            ts = time.gmtime()

# Generated at 2022-06-14 12:36:25.573987
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logFormatter = LogFormatter('')

# Install a log formatter if we don't have one yet.  If we already have
# a formatter, do not install new one.
if not app_log.handlers:
    app_log.propagate = False
    app_log.addHandler(logging.StreamHandler())
    app_log.setLevel(logging.INFO)
if not gen_log.handlers:
    gen_log.propagate = False
    gen_log.addHandler(logging.StreamHandler())
    gen_log.setLevel(logging.INFO)



# Generated at 2022-06-14 12:36:27.312946
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:36:31.052404
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.logging = "warning"
    options.log_file_prefix = "testlog"
    options.log_to_stderr = True
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:36:33.863302
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    LogFormatter_obj = LogFormatter()
    if LogFormatter_obj.format(logging.LogRecord):
        pass
    print('Test of LogFormatter format() method successful')


# Generated at 2022-06-14 12:36:39.214066
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(fmt="%(color)s %(asctime)s %(levelname)s%(end_color)s %(message)s",
                 datefmt="%y%m%d %H:%M:%S", style='%')


# Generated at 2022-06-14 12:36:48.844593
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options


# Generated at 2022-06-14 12:36:57.600309
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import tornado.options
    from tornado.log import enable_pretty_logging, gen_log

    try:
        tornado.options.parse_command_line([])
        assert False, "should not reach here"
    except SystemExit as e:
        assert e.code == 2

    try:
        tornado.options.parse_command_line(["--logging=none"])
    except SystemExit:
        assert False, "should not reach here"

    enable_pretty_logging()
    gen_log.info("LogFormatter test message")



# Generated at 2022-06-14 12:36:59.952714
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter(color=False)
    assert LogFormatter(color=True)

_default_logging_configured = False



# Generated at 2022-06-14 12:37:00.919093
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter() is not None


# Generated at 2022-06-14 12:37:13.874088
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import io
    import unittest

    _stderr_supports_color = True

    class TestLogFormatter(unittest.TestCase):
        def setUp(self) -> None:
            self.stream = io.StringIO()
            self.handler = logging.StreamHandler(self.stream)
            self.logger = logging.getLogger("tornado.test")
            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.DEBUG)
            self.log_formatter = LogFormatter()

        def tearDown(self) -> None:
            self.stream.close()

        def test_default_format(self) -> None:
            # Test the default formatter
            self.handler.setFormatter(self.log_formatter)

# Generated at 2022-06-14 12:37:47.223498
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()  # type: LogFormatter
    assert fmt._fmt == LogFormatter.DEFAULT_FORMAT
    dt = LogFormatter.DEFAULT_DATE_FORMAT
    assert fmt.datefmt == dt
    assert fmt._colors == LogFormatter.DEFAULT_COLORS

    fmt = LogFormatter(color=False)  # type: LogFormatter
    assert fmt._fmt == LogFormatter.DEFAULT_FORMAT
    assert fmt.datefmt == dt
    assert fmt._colors == LogFormatter.DEFAULT_COLORS
    assert fmt._normal == ""

    fmt = LogFormatter(color=True)  # type: LogFormatter
    assert fmt._fmt == LogFormatter.DEFAULT_FORMAT
    assert fmt.datefmt == dt
    assert fmt

# Generated at 2022-06-14 12:37:50.473180
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    print('test_enable_pretty_logging')

# Test the main function

if __name__ == '__main__':
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:53.890631
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert colorama is not None
    log = LogFormatter("%(message)s", "%y%m%d %H:%M:%S")
    assert log._fmt == "%(message)s"


# Generated at 2022-06-14 12:37:54.268921
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass


# Generated at 2022-06-14 12:38:00.305425
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado.options
    """
        enable_pretty_logging() and enable_pretty_logging(options=None)
        are the same.
    """
    options = tornado.options.options
    logging.warning("Warning test")
    enable_pretty_logging()
    logging.critical("Critical test")
    enable_pretty_logging(options=None)
    logging.error("Error test")
    logging.log(10, "Test <10")
    logging.log(20, "Test 20")
    logging.info("Info test")
    logging.debug("Debug test")
    logging.getLogger("test_logger").info("Test test_logger")

# test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:02.114354
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()



# Generated at 2022-06-14 12:38:07.016212
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._colors == lf.DEFAULT_COLORS
    assert lf._normal == ''
    assert lf.datefmt == lf.DEFAULT_DATE_FORMAT



# Generated at 2022-06-14 12:38:15.316348
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from tornado.log import gen_log
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.web import RequestHandler

    class Handler(RequestHandler):
        def get(self):
            gen_log.info({"this is the message": "I want to test"})

    gen_log.handlers = []
    gen_log.setLevel(logging.DEBUG)

    app = Handler
    self.http_client.fetch(self.get_url("/"), self.stop)
    response = self.wait()
    self.assertEqual(response.code, 200)

    gen_log.handlers = []
    gen_log.setLevel(logging.DEBUG)
    gen_log.handlers = []

# Generated at 2022-06-14 12:38:18.519519
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert isinstance(formatter._colors, dict)



# Generated at 2022-06-14 12:38:20.594352
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:39:13.677365
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._normal == ''
    assert formatter._colors == {}

    formatter = LogFormatter(color=False)
    assert formatter._normal == ""
    assert formatter._colors == {}

    formatter = LogFormatter(color=True)
    assert formatter._normal == ""
    assert formatter._colors == {}

    formatter = LogFormatter(colors={99:1})
    assert formatter._normal == ""
    assert formatter._colors == {99:1}


# Generated at 2022-06-14 12:39:16.610615
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    d = dict(asctime='asctime', levelname='levelname', lineno=1, message='msg')
    assert 'msg' in f.format(d)
    d['levelname'] = 'debug'
    assert 'debug' in f.format(d)



# Generated at 2022-06-14 12:39:21.571153
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig()
    enable_pretty_logging()
    gen_log.debug('haha')
    gen_log.debug('hello')
    gen_log.info('haha')
    gen_log.info('hello')
    gen_log.warning('haha')
    gen_log.warning('hello')
    gen_log.error('haha')
    gen_log.error('hello')
    gen_log.critical('haha')
    gen_log.critical('hello')

# Generated at 2022-06-14 12:39:32.389709
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    err_msg = "The value of log_rotate_mode option should be size or time, not none."
    now = datetime.datetime.now()
    # Creates a temp file
    fd, tmp = tempfile.mkstemp()
    os.close(fd)
    with mock.patch("tornado.options.options", new=mock.Mock()) as options:
        options.logging = "E"
        options.log_file_prefix = tmp
        options.log_file_max_size = 1
        options.log_file_num_backups = 1
        options.log_to_stderr = None
        options.log_rotate_mode = "size"
        enable_pretty_logging()
        app_log.error("test")

# Generated at 2022-06-14 12:39:37.786752
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    name = LogFormatter.__name__
    f = LogFormatter()
    s = f.format(logging.LogRecord(name, 10, "/", 1, "msg", None, None))
    assert s.startswith("[I "), s
    assert s.endswith("] msg")
    if colorama:
        try:
            colorama.init()
        except Exception:
            pass
    if curses:
        try:
            curses.setupterm()
        except Exception:
            pass
    if not _stderr_supports_color():
        f = LogFormatter(color=True)
        s = f.format(logging.LogRecord(name, 10, "/", 1, "msg", None, None))

# Generated at 2022-06-14 12:39:38.386638
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert True

# Generated at 2022-06-14 12:39:44.593865
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # Setup
    fmt = "fmt"
    datefmt = "datefmt"
    style = "%"
    color = True
    colors = {"colors": 2}
    log_formatter = LogFormatter(
        fmt,
        datefmt,
        style,
        color,
        colors,
    )
    assert isinstance(log_formatter, LogFormatter)
    # Exercise
    record = logging.LogRecord("name", logging.INFO, "pathname", 1, "msg", {}, None)
    result = log_formatter.format(record)
    # Verify
    assert isinstance(result, str)
    assert result == "[I datefmt name:1] msg"


# Generated at 2022-06-14 12:39:54.288009
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado import testing
    from tornado import options
    from tornado import ioloop

    class TestLogFormatter(testing.AsyncTestCase):
        def setUp(self):
            super(TestLogFormatter, self).setUp()

            options.define('logging', 'none')
            options.options.log_to_stderr = True
            options.parse_command_line([])

            self.logger = logging.getLogger('TEST')
            self.stream = io.StringIO()
            self.handler = logging.StreamHandler(self.stream)
            self.handler.setFormatter(LogFormatter())
            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.INFO)

        def tearDown(self):
            super(TestLogFormatter, self).tear

# Generated at 2022-06-14 12:39:59.060427
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """
    >>> fmt = logging.Formatter()
    >>> fmt._style._fmt = '%(color)s%(levelname)s %(message)s%(end_color)s'
    """
    pass



# Generated at 2022-06-14 12:40:00.788811
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import parse_command_line
    parse_command_line()
    enable_pretty_logging()