

# Generated at 2022-06-14 12:31:01.798724
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    options = tornado.options.options
    options.log_to_stderr = True
    options.logging = "debug"
    options.log_rotate_mode = "size"
    options.log_file_prefix = "/tmp/test"
    options.log_file_num_backups = 10
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:31:02.896393
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:31:11.979580
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    LogFormatter  # silence pyflakes
    import io
    import logging

    logger = logging.getLogger("tornado.test")

    def test_formatter(fmt: str) -> None:
        out = io.StringIO()
        handler = logging.StreamHandler(out)
        handler.setFormatter(LogFormatter(fmt=fmt))
        logger.addHandler(handler)
        logger.propagate = False
        logger.info("test %d %s", 123, u"abc\u1234")
        logger.removeHandler(handler)
        return out.getvalue()

    assert (
        test_formatter("%(message)s")
        == u"[I] test 123 abc\u1234\n[I] test 123 abc\u1234\n"
    )
    assert test_

# Generated at 2022-06-14 12:31:18.317970
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.root.setLevel(logging.NOTSET)
    formatter = LogFormatter()
    assert formatter
    assert formatter._colors == LogFormatter.DEFAULT_COLORS

# Backwards compatability

# Generated at 2022-06-14 12:31:28.073546
# Unit test for constructor of class LogFormatter
def test_LogFormatter(): # pragma: no cover
    import unittest
    

# Generated at 2022-06-14 12:31:30.882092
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._colors[logging.WARNING] == "\033[2;33m"
    assert LogFormatter(color=False)._colors[logging.WARNING] == ""



# Generated at 2022-06-14 12:31:32.249899
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:31:34.828938
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    options = None
    logger = None
    enable_pretty_logging(options,logger)


if __name__=="__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:38.553212
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter(color=True)
    LogFormatter(color=True, colors={logging.DEBUG:1})


# Generated at 2022-06-14 12:31:44.090140
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter._fmt, str)
    assert formatter._colors == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    assert isinstance(formatter._normal, str)



# Generated at 2022-06-14 12:32:17.734536
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    class Object(object):
        pass
    record = Object()
    record.message = 'Some message'
    record.levelno = logging.WARNING
    result = formatter.format(record)
    assert result is not None
    record.message = "Some message\nSome message"
    result = formatter.format(record)
    assert result is not None
    record.message = "Some message\n"
    result = formatter.format(record)
    assert result is not None


# Generated at 2022-06-14 12:32:22.903669
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # No environment set
    # LogFormatter()
    # colorama is not installed
    LogFormatter(color=True, colors={}, style='')
    # class colorama.Win32 has not initialized
    LogFormatter(style='')
    LogFormatter(style='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s')



# Generated at 2022-06-14 12:32:28.948645
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options
    define("logging", default=None, help="log config file")
    options.logging = "debug"
    enable_pretty_logging(options)
    gen_log.debug("debug")
    gen_log.info("info")
    gen_log.warning("warning")
    gen_log.error("error")
test_enable_pretty_logging()

# Generated at 2022-06-14 12:32:35.915464
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import tornado.options
    # The following is based on the same test in tornado.options
    # and modified to work with this LogFormatter class.
    test_opt_str = """
    --logging=debug
    --log_file_prefix=tornado_test
    --log_to_stderr=true
    --log_file_max_size=1
    """
    tornado.options.parse_command_line(test_opt_str.split())
    tornado.options.options.log_to_stderr = True
    tornado.options.options.log_file_max_size = 1
    tornado.options.options.log_file_num_backups = 0

# Generated at 2022-06-14 12:32:47.409625
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():  # noqa: E302
    import tornado.options
    from tornado.log import enable_pretty_logging
    from tornado.options import parse_command_line, options

    # Use delete module to ensure that each test is in a clean env
    sys.modules.pop('tornado.options', None)

    args = ['--logging=debug']
    parse_command_line(args)
    enable_pretty_logging(options=options)
    import logging
    logger = logging.getLogger()
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1

    args = ['--logging=warn']
    parse_command_line(args)
    enable_pretty_logging(options=options)
    assert logger.level == logging.WARN
    assert len(logger.handlers) == 1



# Generated at 2022-06-14 12:32:54.852187
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # pragma: no cover
    log = logging.getLogger()
    log.level = logging.INFO
    log.addHandler(
        logging.StreamHandler(stream=sys.stderr)
    )  # type: ignore[arg-type]

    log.debug("this is DEBUG")
    log.info("this is INFO")
    log.warning("this is WARNING")
    log.error("this is ERROR")
    log.critical("this is CRITICAL")

# Generated at 2022-06-14 12:33:00.210751
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.log_file_prefix = '/tmp/tornado_log'
    options.log_rotate_mode = "size"
    options.log_file_max_size = 10240000
    options.log_file_num_backups = 1000
    enable_pretty_logging(options)

# Generated at 2022-06-14 12:33:08.372874
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import logging, logging.handlers
    lf = LogFormatter()
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._colors == {}
    assert lf._normal == ""

    lf = LogFormatter({1: 1})
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._colors == {}
    assert lf._normal == ""

    lf = LogFormatter(color=False)
    assert lf._fmt == lf.DEFAULT_FORMAT
    assert lf._colors == {}
    assert lf._normal == ""

    lf = LogFormatter(color=True)
    assert lf._fmt == lf.DEFAULT_FORMAT

# Generated at 2022-06-14 12:33:19.812540
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: () -> None
    assert LogFormatter()._normal == ""
    assert LogFormatter(color=False)._normal == ""
    assert LogFormatter()._colors == LogFormatter.DEFAULT_COLORS

    fmt = LogFormatter()._fmt = "%(message)s %(levelname)s"
    record = logging.LogRecord(
        "name", logging.ERROR, "/path/to/file.py", 42, "this is a message", None, None
    )
    expected = "%s ERROR" % record.message
    assert LogFormatter().format(record) == expected
    assert LogFormatter(color=False).format(record) == expected

    class Colored(object):
        def __init__(self) -> None:
            self.levelno = 42


# Generated at 2022-06-14 12:33:21.399935
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: () -> None
    lf = LogFormatter()
    assert lf._normal == ""


# Generated at 2022-06-14 12:33:40.320437
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger = logging.getLogger("tornado.general")
    formatter = LogFormatter()
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.warning("warning")
    

# Generated at 2022-06-14 12:33:41.609179
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()


# Generated at 2022-06-14 12:33:53.777754
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
    datefmt = '%y%m%d %H:%M:%S'
    style = '%'
    color = False
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    logger = LogFormatter(fmt=fmt, datefmt=datefmt, style=style, color=color, colors=colors)

# Generated at 2022-06-14 12:34:02.124095
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_formatter = LogFormatter()
    import logging
    # INFO: root: This is a test
    record = logging.makeLogRecord({"msg": "This is a test", "levelname": "INFO"})
    r = log_formatter.format(record)
    assert '[I' in r
    assert '[INFO' not in r
    assert 'This is a test' in r
    # INFO: root: This is a test with a new line
    record = logging.makeLogRecord(
        {"msg": "This is a test with a new line\n", "levelname": "INFO"}
    )
    r = log_formatter.format(record)
    assert '[I' in r
    assert '[INFO' not in r
    assert 'This is a test with a new line' in r
    assert '    ' in r


# Generated at 2022-06-14 12:34:10.288751
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    options = tornado.options.options
    options.logging = "info"
    options.log_file_prefix = "LoggingTest"
    options.log_file_max_size = 1024
    options.log_file_num_backups = 10
    options.log_rotate_mode = "size"
    options.log_rotate_when = "S"
    options.log_rotate_interval = 1
    options.log_to_stderr = False
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, options.logging.upper()))
    print(logger.handlers)
    enable_pretty_logging(options,logger)
    print(logger.handlers)

# Generated at 2022-06-14 12:34:22.365086
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import os
    import time
    from tornado.log import enable_pretty_logging

    tornado.options.parse_command_line(
        ['--logging=debug',
         '--log_file_prefix=log/'+ 'test_enable_pretty_logging' +str(time.time()) + '.txt',
         '--log_rotate_mode=size',
         '--log_rotate_when=S',
         '--log_rotate_interval=2',
         '--log_file_num_backups=3',
         '--log_file_max_size=10240',
         '--log_to_stderr=true'])
    enable_pretty_logging()

# Generated at 2022-06-14 12:34:29.098677
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._colors == {
        logging.WARNING: '\x1b[0;33m',
        logging.ERROR: '\x1b[0;31m',
        logging.CRITICAL: '\x1b[1;35m',
        logging.DEBUG: '\x1b[0;34m',
        logging.INFO: '\x1b[0;32m'
    }



# Generated at 2022-06-14 12:34:37.892628
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = '[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s'
    datefmt = '%y%m%d %H:%M:%S'
    formatter = LogFormatter(fmt, datefmt)
    assert formatter._fmt == fmt
    assert formatter.datefmt == datefmt


# Generated at 2022-06-14 12:34:47.689843
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    time_format = "%y%m%d %H:%M:%S"
    style = "%"
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    log_formatter = LogFormatter(log_format, time_format, style, color, colors)

# Generated at 2022-06-14 12:34:54.438531
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter._colors == LogFormatter.DEFAULT_COLORS
    assert formatter._normal == ""

    # Color support on Windows versions that do not support ANSI color codes is
    # enabled by use of the colorama library. Applications that wish to use
    # this must first initialize colorama with a call to colorama.init.
    # See the colorama documentation for details.
    colorama.init()
    formatter = LogFormatter()
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter

# Generated at 2022-06-14 12:35:11.571892
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    enable_pretty_logging(tornado.options.options)

# Generated at 2022-06-14 12:35:16.664243
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    assert LogFormatter().format(logging.LogRecord("asdsd", "sdfsdfsdfsdfsdf", "sdfsdfsdfsdfsdf", 1, 1, {}, 1, 1)) == '[sdfsdfsdfsdfsdf asdsd:1]  %(message)s\n    '

# Generated at 2022-06-14 12:35:24.839197
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log  # noqa
    tornado.options.options.logging = "info"
    tornado.options.options.log_file_prefix = "test.log"
    tornado.options.options.log_file_max_size = 1024 * 1024 * 1024
    tornado.options.options.log_file_num_backups = 4
    tornado.options.options.log_rotate_mode = "time"  # time/size
    tornado.options.options.log_rotate_when = 'S'
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_to_stderr = True

    gen_log.info("test_enable_pretty_logging")
    app_log.warning("test_enable_pretty_logging")
    app

# Generated at 2022-06-14 12:35:28.184874
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    enable_pretty_logging(options = {'logger': "logger"})
    enable_pretty_logging(logger = logging.getLogger())

test_enable_pretty_logging()

# Generated at 2022-06-14 12:35:38.368486
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import io
    import unittest
    import logging

    # Create a file-like object to capture stdout output
    buf = io.StringIO()

    class LogHandler(logging.Handler):
        def emit(self, record: Any) -> None:
            buf.write(self.format(record))

    handler = LogHandler()
    handler.setFormatter(LogFormatter())
    logger = logging.getLogger("test")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.critical("Test Critical")
    logger.error("Test Error")
    logger.warning("Test Warning")
    logger.info("Test Info")
    logger.debug("Test Debug")
    result = buf.getvalue()

# Generated at 2022-06-14 12:35:50.434899
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    # __init__() is called in parse_command_line(),
    # which is called at the end of tornado/options.py
    from tornado.testing import AsyncTestCase, LogTrapTestCase

    class Test(AsyncTestCase, LogTrapTestCase):
        def test_formatter(self):
            gen_log.info("hello")
            self.assertLogged("hello")
            gen_log.info("a\u1234")
            self.assertLogged("a\\xe1\\x88\\xb4")
            gen_log.info(b"a\xe1\x88\xb4")
            self.assertLogged("a\\xe1\\x88\\xb4")
            try:
                1 / 0
            except ZeroDivisionError:
                gen_log.error("exception", exc_info=True)

# Generated at 2022-06-14 12:35:52.298828
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

test_enable_pretty_logging()

# Generated at 2022-06-14 12:35:54.631008
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    LogFormatter()

_default_log_handler = None  # type: Optional[logging.Handler]



# Generated at 2022-06-14 12:36:00.755500
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=True, fmt='%(color)s%(levelname)s%(end_color)s %(message)s')
    record = logging.LogRecord('tornado.test', logging.INFO, '/some/path', 123, 'Hello there', {}, None)
    formatter.format(record)


# Generated at 2022-06-14 12:36:02.200340
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: ignore
    lf = LogFormatter()
    assert lf



# Generated at 2022-06-14 12:36:23.622827
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    # This is not a full unit test for LogFormatter, only enough to
    # ensure that the constructor returns a usable object.
    log_formatter = LogFormatter()
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.warning("This is a test.")

# Unit tests for class LogFormatter

# Generated at 2022-06-14 12:36:34.900208
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    import logging
    import sys
    record = logging.LogRecord("tornado.general", logging.INFO, "a", 1, "b", None, None)
    record.message = "c"
    record.asctime = "d"
    record.color = "e"
    record.end_color = "f"
    record.exc_info = None
    record.exc_text = ""
    result = formatter.format(record)
    assert result == """[I d a:1]  c\n    """
    record.exc_info = sys.exc_info()
    record.exc_text = "g"
    result = formatter.format(record)
    assert result == """[I d a:1]  c
    g\n    """


# Generated at 2022-06-14 12:36:37.583895
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    lf = LogFormatter()
    assert lf


# Generated at 2022-06-14 12:36:48.452454
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    datefmt = '%Y-%m-%d %H:%M:%S'
    fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    color = True
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    LogFormatter(fmt, datefmt, '%', color, colors)


# Generated at 2022-06-14 12:37:00.406515
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import define, options
    from tornado.log import app_log

    define("logging", default=None, type=str,
           help="Use " + ", ".join(app_log.name for app_log in [app_log, access_log, gen_log]) + ", or none to set the python log level")
    define("log_file_prefix", default=None, type=str,
           help="Path prefix for log files. "
                "Note that if you are running multiple tornado processes, "
                "log_file_prefix must be different for each of them (e.g. "
                "include the port number)")

# Generated at 2022-06-14 12:37:05.780224
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.options
    
    class TestOptions:
        def __init__(self):
            self.logging = "error"
            self.log_file_prefix = "tmp_file.log"
            self.log_rotate_mode = "size"
            self.log_file_max_size = 2
            self.log_file_num_backups = 1
            self.log_to_stderr = False

    options = TestOptions()
    enable_pretty_logging()

test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:18.586085
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import io

    options = tornado.options.options
    options.logging = "info"
    options.log_to_stderr = True
    options.log_file_prefix = None
    options.log_file_max_size = 100
    options.log_file_num_backups = 5
    options.log_rotate_mode = "time"
    options.log_rotate_when = "S"
    options.log_rotate_interval = 15
    enable_pretty_logging()
    gen_log.info("pretty logging is enabled")
    gen_log.info("gen_log")
    app_log.info("app_log")
    access_log.info("access_log")

# Generated at 2022-06-14 12:37:20.869473
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = LogFormatter()
    assert fmt.format('bad message( invalid syntax )') == 'Bad message ("invalid syntax"): {}'
    assert fmt.format("print('hello world')") == "print('hello world')"

# Generated at 2022-06-14 12:37:21.737470
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:37:22.815402
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert repr(LogFormatter())



# Generated at 2022-06-14 12:37:58.226908
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    try:
        import tornado.options
        import tornado.log
        try:
            tornado.log.enable_pretty_logging(
                logger=tornado.log.gen_log, options=tornado.options.options)
        except:
            tornado.log.enable_pretty_logging(logger=tornado.log.gen_log)
    except:
        pass

test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:00.278537
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging(True,'tornado')


# Generated at 2022-06-14 12:38:01.686839
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:38:03.045907
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    LogFormatter(style='%')


# Generated at 2022-06-14 12:38:13.471500
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers = []
    enable_pretty_logging()
    assert len(logger.handlers) == 1, logger.handlers

if __name__ == "__main__":
    import os
    import sys
    import tempfile

    logging.root.setLevel(logging.DEBUG)
    logging.root.handlers = []

    test_formatter = LogFormatter(color=True)
    test_formatter.format(logging.LogRecord("test", logging.WARNING, __file__, 42, "foo", None, None))
    sys.stdout.write("LogFormatter tests passed\n")

    test_enable_pretty_logging()

# Generated at 2022-06-14 12:38:20.309272
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger("tornado.test.test_log")
    logger.setLevel(logging.DEBUG)
    stderr = logging.StreamHandler()
    formatter = LogFormatter()
    stderr.setFormatter(formatter)
    logger.addHandler(stderr)
    logger.error("1")
    logger.error("2")
    logger.info("3")




# Generated at 2022-06-14 12:38:22.166598
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # TODO: Implement this unit test
    pass


# Generated at 2022-06-14 12:38:32.388803
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # check if logging crashes
    import tornado.options
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_to_stderr = True
    tornado.options.options.logging = "debug"
    tornado.options.options.log_file_prefix = "./tmp/log-1"
    tornado.options.options.log_file_num_backups = 3
    tornado.options.options.log_file_max_size = 102
    tornado.options.options.log_rotate_when = "S"
    tornado.options.options.log_rotate_interval = 1
    enable_pretty_logging()
    print('')

test_enable_pretty_logging()



# Generated at 2022-06-14 12:38:41.327311
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    import logging

    class Options:
        log_to_stderr = False
        log_file_prefix = "test.log"
        log_file_max_size = 1000000
        log_file_num_backups = 3
        log_rotate_mode = "size"
        log_rotate_when = "MIDNIGHT"
        log_rotate_interval = 1
        debug = True

    options = Options()
    tornado.log.enable_pretty_logging(options)
    logger = logging.getLogger()
    assert logger.level == logging.DEBUG


# Generated at 2022-06-14 12:38:52.225783
# Unit test for constructor of class LogFormatter

# Generated at 2022-06-14 12:40:05.948090
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.util
    import tornado.log
    import logging
    import logging.handlers
    import sys
    import curses
    import colorama



# Generated at 2022-06-14 12:40:07.272988
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    enable_pretty_logging(tornado.options.options)

# Generated at 2022-06-14 12:40:16.153432
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(datefmt='%Y', fmt="%(message)s")
    formatter = LogFormatter(datefmt='%Y', fmt="%(message)s")
    formatter = LogFormatter(datefmt='%Y', fmt="%(message)s")
    formatter = LogFormatter(fmt="%(message)s")
    formatter = LogFormatter(fmt="%(message)s")
    formatter = LogFormatter(fmt="%(message)s")
    formatter = LogFormatter()



# Generated at 2022-06-14 12:40:21.045771
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    l = LogFormatter()
    assert l
    l = LogFormatter(fmt="")
    assert l
    l = LogFormatter(datefmt="")
    assert l
    l = LogFormatter(style="")
    assert l
    l = LogFormatter(color=False)
    assert l
    l = LogFormatter(colors={})
    assert l


# Generated at 2022-06-14 12:40:25.615353
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    class FakeRecord(object):
        def __init__(self, message):
            # type: (str) -> None
            self.message = message
            self.levelno = logging.INFO

    formatter = LogFormatter()
    formatter.formatTime = lambda a, b: "foo"

    formatter.format(FakeRecord("aaa"))
    formatter.format(FakeRecord("aaa%rbbb"))
    formatter.format(FakeRecord("aaa%sbbb"))



# Generated at 2022-06-14 12:40:28.703619
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter()._normal == ""
    assert LogFormatter(color=True)._normal == "\033[0m"


# Generated at 2022-06-14 12:40:30.866366
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # type: ignore
    # pylint: disable=unused-variable
    LogFormatter()


# Generated at 2022-06-14 12:40:40.695994
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'  # noqa: E501
    datefmt = '%y%m%d %H:%M:%S'
    style = '%'
    color = True
    colors = {
        logging.DEBUG: 4,
        logging.INFO: 2,
        logging.WARNING: 3,
        logging.ERROR: 1,
        logging.CRITICAL: 5,
    }
    formatter = LogFormatter(fmt, datefmt, style, color, colors)