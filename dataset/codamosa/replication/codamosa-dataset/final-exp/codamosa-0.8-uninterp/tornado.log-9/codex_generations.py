

# Generated at 2022-06-14 12:31:07.282816
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = Object()
    record.message = 'Test message'
    record.asctime = '2020'
    record.levelno = logging.INFO
    timestamp = formatter.formatTime(record, formatter.datefmt)
    assert timestamp == '20200626 14:11:51'
    assert formatter.format(record) == '[I 2020 0626 14:11:51 None:None] Test message'  # noqa: E501


# Generated at 2022-06-14 12:31:10.337271
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    enable_pretty_logging(options=None)
    enable_pretty_logging(logger=None)
    enable_pretty_logging(options=False, logger=False)
test_enable_pretty_logging()

# Generated at 2022-06-14 12:31:13.472221
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class FakeLogRecord:
        message = "test"
        asctime = "fake"
        levelno = 10

    logger = LogFormatter()
    assert logger.format(FakeLogRecord()) == "[L fake test] "

# -----------------------------------------------------------------------------
# Logger object class
# -----------------------------------------------------------------------------



# Generated at 2022-06-14 12:31:15.007581
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass

# Generated at 2022-06-14 12:31:25.719852
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import time
    import logging
    import os
    import log

    # Create logger
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    # Create file handler which logs even debug messages
    os.makedirs('log', exist_ok=True)
    fh = logging.handlers.TimedRotatingFileHandler('log/test.log', when='M', interval=1)
    fh.setLevel(logging.DEBUG)
    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # Create formatter
    formatter = log.LogFormatter()
    # Add the formatter to the handlers
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
   

# Generated at 2022-06-14 12:31:36.168791
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import OptionParser, options
    parser = OptionParser()
    parser.add_option('--logging', default='info')
    parser.add_option('--logging_level', default='info')
    parser.add_option('--log_to_stderr', default=False)
    parser.add_option('--log_file_prefix', default='/tmp/tornado.log')
    parser.add_option('--log_file_num_backups', default=10)
    parser.add_option('--log_file_max_size', default=1024 * 1024 * 2)
    parser.add_option('--log_rotate_mode', default='size')
    parser.add_option('--log_rotate_when', default='MIDNIGHT')

# Generated at 2022-06-14 12:31:39.221494
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # check that a LogFormatter with datefmt but without fmt
    # gives an error
    with pytest.raises(TypeError):
        LogFormatter(datefmt='%Y-%m-%d')



# Generated at 2022-06-14 12:31:43.542232
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    lf = LogFormatter()
    lf.__init__()
    print(help(lf.format))  # 打印该方法的帮助信息
    print(lf.format(record='Tornado.logger'))  # 测试方法



# Generated at 2022-06-14 12:31:50.356674
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt_obj = LogFormatter()
    record = logging.LogRecord('name', 'level', pathname='/pathname', lineno=101, msg='msg', args=tuple(), exc_info=None)
    out = fmt_obj.format(record)
    expected = '[level pathname:101] msg'
    assert out == expected


# Generated at 2022-06-14 12:31:59.303804
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.platform.auto
    from tornado.options import define, options
    tornado.platform.auto.set_close_exec(False)
    tornado.platform.auto.set_inheritable(False)
    tornado.platform.auto.set_nonblocking(False)
    define("logging", default="debug")
    define("log_rotate_mode", default="time")
    define("log_rotate_when", default="h")
    define("log_rotate_interval", default=1)
    define("log_file_prefix", default="<stdout>")
    define("log_file_max_size", default=100)
    define("log_file_num_backups", default=10)
    define("log_to_stderr", False)
    tornado.options.parse_

# Generated at 2022-06-14 12:32:16.435580
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()  # type: ignore
    return formatter


# Generated at 2022-06-14 12:32:21.627322
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter._colors == {}
    assert formatter._normal == ""

    formatter = LogFormatter(color=False)
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter._colors == {}
    assert formatter._normal == ""



# Generated at 2022-06-14 12:32:31.850369
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Unit test for LogFormatter.

    To run this test, execute the following command:

        python -m tornado.log
    """
    d = dict(
        color=True,
        fmt="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        colors={logging.DEBUG: 2, logging.INFO: 3, logging.WARNING: 4},
    )
    lf = LogFormatter(**d)
    assert lf._fmt == "%(color)s%(asctime)s %(message)s%(end_color)s"
    assert lf._colors[logging.DEBUG] == "\033[2;3;32m"

# Generated at 2022-06-14 12:32:44.809891
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    fmt = LogFormatter()
    class Record(object):
        pass
    record = Record()
    record.message = "1"
    record.asctime = "2"
    record.color = "3"
    record.end_color = "4"
    record.__dict__ = {
        "message": "1", 
        "asctime": "2", 
        "color": "3", 
        "end_color": "4"
    }
    assert fmt._fmt == "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501

# Generated at 2022-06-14 12:32:49.675863
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    tf = LogFormatter()
    assert tf.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    tf = LogFormatter(datefmt='%Y-%m-%d %H:%M:%S')
    assert tf.datefmt == '%Y-%m-%d %H:%M:%S'


# Generated at 2022-06-14 12:32:51.003014
# Unit test for function define_logging_options
def test_define_logging_options():
    assert define_logging_options != None


# Generated at 2022-06-14 12:32:53.710303
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    log_formatter = LogFormatter()
    output = log_formatter.format("test")
    assert output == "test"



# Generated at 2022-06-14 12:32:56.926222
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    print(LogFormatter())  # noqa: T001



# Generated at 2022-06-14 12:33:03.897430
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import logging
    import logging.handlers
    import os

    if not os.path.isdir("test"):
        os.mkdir("test")
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler("test/test.log", maxBytes=1024)
    handler.setLevel(logging.DEBUG)
    formatter = LogFormatter(color=False)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug("test messsage")



# Generated at 2022-06-14 12:33:11.225249
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.propagate = False
    logging.addLevelName(5, "SPAM")
    logging.Logger.spam = lambda inst, msg, *args: inst.log(5, msg, *args)

    enable_pretty_logging()

    gen_log.info("info")
    gen_log.debug("debug")
    gen_log.warning("warning")
    gen_log.error("error")
    try:
        raise Exception("test exception")
    except Exception:
        gen_log.exception("exception")
    try:
        raise Exception("Unicode \xe9")
    except Exception:
        gen_log.exception("Unicode exception")
    gen_log.spam("spam")

# Generated at 2022-06-14 12:33:36.885313
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # It should work fine with no options.
    enable_pretty_logging()
    # But the option parsing should work too.
    import tornado.options
    tornado.options.define('log_to_stderr', True)
    tornado.options.define('log_file_prefix', 'test')
    # It should be no problem to set log_rotate_mode to 'time' or 'size'
    tornado.options.define('log_rotate_mode', 'time')
    tornado.options.define('log_rotate_when', 'S')
    tornado.options.define('log_rotate_interval', 1)
    tornado.options.define('log_file_num_backups', 5)
    tornado.options.define('log_file_max_size', 10)
    tornado.options.parse_command_line()


# Generated at 2022-06-14 12:33:39.570320
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    msg = "some message"
    t = logging.LogRecord("name", logging.DEBUG, None, None, msg, None, None)
    assert formatter.format(t)



# Generated at 2022-06-14 12:33:48.274658
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    l = LogFormatter()
    l = LogFormatter(color=False)
    l = LogFormatter(colors={})
    l = LogFormatter(datefmt="")
    l = LogFormatter(fmt="[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s")  # noqa: E501
    l = LogFormatter(style="%")



# Generated at 2022-06-14 12:33:58.483637
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    def test_rotate_mode_is_time():
        import tornado.options
        import tornado.options
        import logging

        class Options(object):
            log_file_prefix = "test"
            log_file_num_backups = 30
            log_rotate_mode = "time"
            log_rotate_when = "D"
            log_rotate_interval = 1

        options = Options()
        enable_pretty_logging(options)
        logger = logging.getLogger()
        for handler in logger.handlers:
            if isinstance(handler, logging.handlers.TimedRotatingFileHandler):
                logging.info("test")
                # The log file should be created successfully.
    test_rotate_mode_is_time()


# Generated at 2022-06-14 12:34:03.410754
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s %(asctime)s] %(message)s')
    enable_pretty_logging()
    app_log.debug('hello')
    app_log.info('info')

if __name__ == '__main__':
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:34:11.263736
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    # test attibutes
    assert formatter.datefmt == LogFormatter.DEFAULT_DATE_FORMAT
    assert formatter._normal == colorama.Style.RESET_ALL if colorama else "\033[0m"

# Generated at 2022-06-14 12:34:17.037376
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class Mock(object):
        pass
    record=Mock()
    record.message="Warning"
    record.levelno=30
    record.exc_info="exception"
    record.__dict__={}
    assert(LogFormatter().format(record)=="[W 0128 16:04:38:  :] Warning")


# Generated at 2022-06-14 12:34:21.372077
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class Record:
        def __init__(self,message,levelno,exc_info,exc_text):
            self.message = message
            self.levelno = levelno
            self.exc_info = exc_info
            self.exc_text = exc_text

    def test_log_formatter():
        log_formatter = LogFormatter()
        record = Record('message1',11,True,'exc_text')
        assert log_formatter.format(record) == '[D 000101 tornado.general:0] message1'

        record = Record(['message2'],11,True,'exc_text')
        assert log_formatter.format(record) == '[D 000101 tornado.general:0] Bad message (%r): %r'

        record = Record(5,11,True,'exc_text')

# Generated at 2022-06-14 12:34:28.784568
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    formatter = LogFormatter()
    record = logging.LogRecord(
            name = 'tornado.access',
            level = logging.DEBUG ,
            pathname = None,
            lineno = 0,
            msg = 'Test',
            args = None,
            exc_info = None,
        )
    result = formatter.format(record)
    # print(result)
    assert result == '[D %s tornado.access:%d] Test' % (record.asctime, record.lineno)


# Generated at 2022-06-14 12:34:35.732809
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = LogFormatter()
    assert fmt.DEFAULT_FORMAT == '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'  # noqa: E501
    assert fmt.DEFAULT_DATE_FORMAT == '%y%m%d %H:%M:%S'
    assert fmt.DEFAULT_COLORS == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
    # TODO: use mock object to test if is called properly

# Generated at 2022-06-14 12:35:02.184403
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass

# Generated at 2022-06-14 12:35:12.037080
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    def helper(formatter):
        record = logging.LogRecord("name", "INFO", "", 1, "--msg--", None, None)
        res = formatter.format(record)
        assert res == "[I --msg--]\n"

        record.exc_text = "--exc--"
        res = formatter.format(record)
        assert res == "[I --msg--]\n    --exc--\n"

        record.exc_info = None
        res = formatter.format(record)
        assert res == "[I --msg--]\n    --exc--\n"

    helper(LogFormatter())



# Generated at 2022-06-14 12:35:21.996565
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    import time
    import datetime
    f = LogFormatter(
        '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s',
        '%m/%d/%Y %H:%M:%S',
        '%',
        True,
        {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
        }
    )

# Generated at 2022-06-14 12:35:25.706477
# Unit test for constructor of class LogFormatter
def test_LogFormatter():  # pragma: nocover
    from tornado.log import LogFormatter
    LogFormatter(fmt="%(color)s%(levelname)s%(end_color)s %(message)s")



# Generated at 2022-06-14 12:35:36.155751
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    import tornado.options
    from tornado.options import define, options
    define('logging', default='warning', help='logging level')
    define('log_file_prefix', default='/tmp/tornado.log', help='log file prefix')
    define('log_rotate_mode', default='size', help='log rotate mode')

    define('log_file_max_size', default='100', help='log file max size')
    define('log_file_num_backups', default='5', help='log file backups number')

    define('log_to_stderr', default='True', help='log to stderr')

    define('log_rotate_when', default='d', help='log rotate when')
    define('log_rotate_interval', default='1', help='log rotate interval')

   

# Generated at 2022-06-14 12:35:42.385404
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    non_string_keys = {1: 1, 2: 2}
    assert isinstance(non_string_keys, dict)
    fmter = LogFormatter()
    record = logging.LogRecord("tornado", logging.ERROR,
                               "test_file.py", 1,
                               _unicode('message'),
                               ('arg0', 'arg1'),
                               exc_info=('type', 'value', 'traceback'),
                               func='f')
    record.__dict__.update(non_string_keys)
    formatted = fmter.format(record)
    print(formatted)


# Generated at 2022-06-14 12:35:53.400152
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    """Test log formatter.
    """
    from dataclasses import dataclass
    from datetime import datetime
    from typing import Dict
    import unittest
    import logging

    class Record(object):
        def __init__(self, message: str = '', levelno: int = 10, exc_info: None = None) -> None:
            self.__dict__: Dict[str, Any] = {}
            self.message = message
            self.levelno = levelno
            self.exc_info = exc_info
            self.exc_text = None

        def getMessage(self) -> str:
            return self.message

    @dataclass
    class Datetime(object):
        year: int = 2020
        month: int = 1
        day: int = 1


# Generated at 2022-06-14 12:35:54.132705
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:35:59.675046
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    import logging 
    from tornado.log import enable_pretty_logging

    logger = logging.getLogger()
    tornado.log.enable_pretty_logging()
    logger.setLevel(logging.INFO)
    logger.info('this is a tornado log test')

# Generated at 2022-06-14 12:36:09.709413
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
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
    lf = LogFormatter(format, datefmt, style, color, colors)
    assert format == lf._fmt
    assert color == (lf._colors != {})

# Generated at 2022-06-14 12:37:03.556426
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:37:09.504407
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    logger = logging.getLogger()
    formatter = LogFormatter()
    logger.setLevel(logging.INFO)
    stream = logging.StreamHandler()
    stream.setLevel(logging.INFO)
    stream.setFormatter(formatter)
    logger.addHandler(stream)
    logger.info("test1")


# Generated at 2022-06-14 12:37:18.804242
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from logging import StreamHandler

    h = StreamHandler()
    h.setFormatter(LogFormatter())

    # Test the format() method
    h.emit(logging.makeLogRecord({"msg": "A"}))
    h.emit(logging.makeLogRecord({"msg": "B" * 50}))
    h.emit(logging.makeLogRecord({"msg": "C", "exc_info": Exception("foo")}))

    # test invalid input
    h.emit(logging.makeLogRecord({"msg": b"D\xc3"}))



# Generated at 2022-06-14 12:37:28.081672
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    try:
        del logging.Logger.manager.loggerDict["tornado.access"]
        logging.getLogger("tornado.access").propagate = False
    except KeyError:
        pass
    fmt = LogFormatter()
    log = logging.getLogger("tornado.access")
    log.handle = logging.StreamHandler(sys.stdout)
    log.addHandler(log.handle)
    log.setLevel(logging.DEBUG)
    log.critical("critical")
    log.error("error")
    log.warning("warning")
    log.info("info")
    log.debug("debug")
    logging.shutdown()


# Set up color if we are in a tty and curses is installed

# Generated at 2022-06-14 12:37:40.031603
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    x = LogFormatter()
    assert x.DEFAULT_FORMAT == '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'  # noqa: E501
    assert x.DEFAULT_DATE_FORMAT == '%y%m%d %H:%M:%S'
    assert x.DEFAULT_COLORS == {logging.DEBUG: 4, logging.INFO: 2, logging.WARNING: 3, logging.ERROR: 1, logging.CRITICAL: 5}  # noqa: E501

# Generated at 2022-06-14 12:37:44.081413
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    test_record = logging.LogRecord('name', logging.ERROR, '/home/user/a', 7, 'msg', None, None)
    formatter = LogFormatter()
    formatter.format(test_record)


# Generated at 2022-06-14 12:37:54.669836
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import json
    import tornado.options

    tornado.options.enable_pretty_logging()
    tornado.options.parse_command_line()
    gen_log.info("test")
    gen_log.warning("test")
    gen_log.error("test")

# Generated at 2022-06-14 12:37:58.983037
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    """Test constructor of class LogFormatter."""
    assert LogFormatter()
    assert LogFormatter(color=False)
    assert LogFormatter(fmt="LogFormatter")
    assert LogFormatter(datefmt="LogFormatter")
    assert LogFormatter(style="LogFormatter")
    assert LogFormatter(colors={"LogFormatter": "LogFormatter"})


# Generated at 2022-06-14 12:38:02.574860
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter(fmt="%(color)s%(message)s%(end_color)s")


# Generated at 2022-06-14 12:38:11.713721
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    from io import StringIO
    from tornado.log import gen_log
    opts = tornado.options.Options()
    opts.parse_config_file('options.py')
    #opts.parse_command_line(['test.log'])
    #opts.parse_command_line(['--logging=error', '--log-file-prefix=test.log'])
    tornado.options.enable_pretty_logging(opts)

    gen_log.error("Test")
    #ff1 = open('test.log', 'r')
    #assert ff1.readline().startswith("[E")

# Generated at 2022-06-14 12:40:15.925611
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter().DEFAULT_COLORS == {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }
# end of unit test



# Generated at 2022-06-14 12:40:24.599235
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    import tornado.testing
    import unittest

    # enable_pretty_logging should set the log level, add a rotating
    # file handler, and add a stderr handler.
    # We could test the log output, but this is enough for coverage.
    def setUpModule() -> None:
        tornado.options.enable_pretty_logging(options=tornado.options.options)

    @tornado.testing.gen_test
    def test_enable_pretty_logging() -> None:
        tornado.log.gen_log.info("test")

    class TestOptions(tornado.options.OptionParser):
        def __init__(self) -> None:
            super(TestOptions, self).__init__()

# Generated at 2022-06-14 12:40:36.966872
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    print("\n--- Method format of class LogFormatter")
    import sys
    import logging
    import logging.handlers
    # logging.basicConfig(filename='some.log',level=logging.DEBUG)
    # fmt = "%(color)s[%(levelname)s %(asctime)s %(module)s:%(lineno)d]$(end_color)s %(message)s"
    fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
    import datetime
    datefmt = "%H:%M:%S"