

# Generated at 2022-06-14 12:31:07.119123
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()


# Generated at 2022-06-14 12:31:08.397447
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    pass

# Generated at 2022-06-14 12:31:12.902734
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()
    gen_log.debug("test message")
    assert True

# Generated at 2022-06-14 12:31:25.154116
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    from io import StringIO
    from tornado.log import LogFormatter
    log_output = StringIO()
    formatter = LogFormatter(color=False)
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(log_output)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Generated at 2022-06-14 12:31:34.524358
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    if True:
        record = logging.LogRecord('test', 'INFO', ('test/test.py', 1, 'test', 'test.py'), 1, 'test', (), None, None)
        logformatter = LogFormatter()
        ret = logformatter.format(record)
        assert ret == '[I 01010000 test:1] test'
    if True:
        record = logging.LogRecord('test', 'INFO', ('test/test.py', 1, 'test', 'test.py'), 1, 'test', (), 'test', None)
        logformatter = LogFormatter()
        ret = logformatter.format(record)
        assert ret == '[I 01010000 test:1] test\n    test'



# Generated at 2022-06-14 12:31:43.228898
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert isinstance(f, logging.Formatter)
    assert f._colors.keys() == {10, 20, 30, 40, 50}
    assert f._fmt == LogFormatter.DEFAULT_FORMAT
    assert f._normal == f._colors[30]
    f = LogFormatter(fmt="%(message)s", datefmt="%Y-%m-%d")
    assert f._fmt == "%(message)s"
    assert f.datefmt == "%Y-%m-%d"



# Generated at 2022-06-14 12:31:55.978080
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.parse_config_file(filename="tornado_test.conf")
    tornado.options.parse_command_line()
    enable_pretty_logging()
    gen_log.info('tornado.options.logging="%s"', tornado.options.options.logging)
    gen_log.info('tornado.options.log_file_prefix="%s"', tornado.options.options.log_file_prefix)
    gen_log.info('tornado.options.log_rotate_mode="%s"', tornado.options.options.log_rotate_mode)
    gen_log.info('tornado.options.log_file_max_size="%s"', tornado.options.options.log_file_max_size)

# Generated at 2022-06-14 12:32:07.306152
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    LogFormatter_format_fail=False 
    try:
        import tornado.log
        import logging
        import time
        logger = logging.getLogger("test_logging")
        for i in range(1,5):
            logger.debug("test logging")
            logger.info("test logging")
            logger.warning("test logging")
            logger.critical("test logging")
            logger.error("test logging")
            time.sleep(1)
    except Exception as ex:
        LogFormatter_format_fail=True
        print("Exception in test_LogFormatter_format",ex)

    assert LogFormatter_format_fail == False


# Generated at 2022-06-14 12:32:09.270346
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=True)
    formatter  # type: ignore



# Generated at 2022-06-14 12:32:15.998817
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    l = LogFormatter()
    l = LogFormatter(fmt="%(message)s")
    l = LogFormatter(datefmt=None)
    l = LogFormatter(color=False)
    l = LogFormatter(colors={1: 3, 2: 1})



# Generated at 2022-06-14 12:32:27.432883
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    """Unit test for function enable_pretty_logging
    """
    import os, tornado.options
    os.environ["TORNADO_NODE_ENV"] = "test"
    tornado.options.parse_config_file(None)
    enable_pretty_logging()



# Generated at 2022-06-14 12:32:32.360998
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    record = logging.LogRecord(
        name="tornado.general",
        level=logging.INFO,
        pathname="/home/guoxiao/miniconda3/envs/grass/lib/python3.6/site-packages/tornado/log.py",
        lineno=48,
        msg="264",
        args=None,
        exc_info=None,
    )

# Generated at 2022-06-14 12:32:45.083959
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.testing
    import tornado.options

    def test_function():
        tornado.options.define("logging", type=str, help="logging level")
        tornado.options.define("log_to_stderr", type=bool, help="log to stderr")
        tornado.options.define("log_file_prefix", type=str, help="log file prefix")
        tornado.options.define(
            "log_rotate_mode",
            default="time",
            type=str,
            help="log rotate mode",
        )
        tornado.options.define(
            "log_rotate_when", default="S", type=str, help="log rotate when"
        )

# Generated at 2022-06-14 12:32:57.365234
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter(
        fmt='%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s',
        datefmt='%y%m%d %H:%M:%S',
        style='%',
        color=True,
        colors={
            logging.DEBUG: 4,  # Blue
            logging.INFO: 2,  # Green
            logging.WARNING: 3,  # Yellow
            logging.ERROR: 1,  # Red
            logging.CRITICAL: 5,  # Magenta
        }
    )
    # END LogFormatter.__init__
    # BEGIN LogFormatter.format

# Generated at 2022-06-14 12:32:59.215455
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

if __name__ == "__main__":
    test_enable_pretty_logging()

# Generated at 2022-06-14 12:33:03.855008
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logger=logging.getLogger("tornado.application.test")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(stream=None))
    formatter = LogFormatter()
    logger.error('Error')
    logger.warning('Warning')
    logger.info('Info')
    logger.debug('Debug')
    logger.critical('Critical')


# Generated at 2022-06-14 12:33:09.706497
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    from tornado.options import options
    from tornado.options import define
    from io import StringIO
    io = StringIO()
    define("log_file_max_size", 100)
    define("log_file_num_backups", None)
    options.log_to_stderr = True
    options.log_file_prefix = 'prefix'
    options.log_file_prefix = io
    basicConfig()


# Generated at 2022-06-14 12:33:15.446304
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.options.log_file_prefix = "test.log"
    try:
        enable_pretty_logging()
        logging.info("test")
        assert open("test.log").read().strip().endswith("test")
    finally:
        import os

        os.unlink("test.log")
        logging.getLogger().handlers = []



# Generated at 2022-06-14 12:33:16.402031
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    pass

# Generated at 2022-06-14 12:33:28.896545
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    from tornado.options import parse_config_file
    from tornado.options import define, options
    from tornado.log import access_log, gen_log, app_log
    import os
    import sys
    import random
    import logging
    import re
    import io

    file_path = os.path.join(os.path.dirname(__file__), 'test_logging.conf')
    # test parse_config_file
    parse_config_file(file_path)
    assert options.logging == 'debug'
    assert options.log_rotate_mode == 'size'
    assert options.log_to_stderr is False
    assert options.log_file_prefix == 'test.log'
    # test enable_pretty_logging
    enable_pretty_logging()
    # test LogFormatter.format

# Generated at 2022-06-14 12:33:44.391902
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.parse_command_line([])
    enable_pretty_logging()
    assert True

# Generated at 2022-06-14 12:33:56.822508
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options = tornado.options.define(
        "log_to_stderr",
        default=None,
        help=("Send log output to stderr (colorized if possible). " "By default use stderr if --log_file_prefix is not set and no other logging is configured."),  # noqa: E501
        type=bool,
    )
    tornado.options.options = tornado.options.define(
        "log_file_prefix",
        default=None,
        metavar="PATH",
        help=("Path prefix for log files. " "Note that if you are running multiple tornado processes, log_file_prefix must be different for each of them (e.g. include the port number)."),  # noqa: E501
    )

# Generated at 2022-06-14 12:34:03.503010
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    logging.basicConfig(level=logging.DEBUG)
    record = logging.LogRecord(
        name="tornado.application",
        level=logging.INFO,
        pathname="somepath",
        lineno=1,
        msg="hi",
        args=None,
        exc_info=None,
    )
    logger = logging.getLogger("tornado.application")
    logger.debug(record)



# Generated at 2022-06-14 12:34:06.451160
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)
    assert formatter._fmt == LogFormatter.DEFAULT_FORMAT
    assert formatter._colors == LogFormatter.DEFAULT_COLORS



# Generated at 2022-06-14 12:34:10.016297
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    x = LogFormatter()
    assert x is not None
    LogFormatter(fmt="foo")
    LogFormatter(datefmt="foo")
    LogFormatter(color=False)
    LogFormatter(color=True)
    LogFormatter(colors={})
    LogFormatter(colors={1: 2})

# Generated at 2022-06-14 12:34:23.139770
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    pass
    # NOTE: Disabled since we don't have a mock curses object to avoid
    # hitting the filesystem.

# Generated at 2022-06-14 12:34:32.432050
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter(color=False)

    # Add sample record.
    record = logging.LogRecord(
        name="tornado.test",
        level=logging.INFO,
        pathname="/path/dummy",
        lineno=37,
        msg="test message",
        args=(),
        exc_info=None)

    # Format.
    formatter.format(record)
    assert record.message == "test message"
    assert record.color == ""
    assert record.end_color == ""
    assert record.asctime == "000000 00:00:00"

    # Test string format.
    formatter = LogFormatter(
        fmt='%(color)s%(asctime)s - %(message)s%(end_color)s')
    formatter.format(record)


# Generated at 2022-06-14 12:34:33.873712
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    enable_pretty_logging()

# Generated at 2022-06-14 12:34:41.772212
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    class DummyLogRecord:
        def __init__(self, level: int, msg: str) -> None:
            self.levelno = level
            self.msg = msg

        def exc_text(self) -> Optional[str]:
            return None

        def exc_info(self) -> None:
            return
    r = DummyLogRecord(1, "message")
    lf = LogFormatter(_stderr_supports_color())
    assert lf.format(r)



# Generated at 2022-06-14 12:34:50.667990
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
    log_datefmt = "%Y-%m-%d %H:%M:%S"
    log_style = "%"
    log_color = True
    log_colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 5,  # Magenta
    }

    # Test that you can init with all args

# Generated at 2022-06-14 12:35:19.878238
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter(datefmt = "test") is not None


# Generated at 2022-06-14 12:35:26.703975
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options

    tornado.options.options.log_rotate_mode = "size"
    tornado.options.options.log_file_max_size = 1024
    tornado.options.options.log_file_num_backups = 5
    tornado.options.options.log_to_stderr = True
    logging.basicConfig(level=logging.DEBUG)
    enable_pretty_logging(tornado.options.options)
    for i in range(10):
        logging.info(i)



# Generated at 2022-06-14 12:35:27.314097
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

# Generated at 2022-06-14 12:35:30.841615
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert hasattr(formatter, '_fmt')
    assert hasattr(formatter, '_colors')
    assert hasattr(formatter, '_normal')


# Generated at 2022-06-14 12:35:40.112170
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    """test_enable_pretty_logging"""
    import tornado.options

    options = tornado.options.options
    if options.logging is None or options.logging.lower() == "none":
        return
    if logger is None:
        logger = logging.getLogger()
    logger.setLevel(getattr(logging, options.logging.upper()))
    if options.log_file_prefix:
        rotate_mode = options.log_rotate_mode
        if rotate_mode == "size":
            channel = logging.handlers.RotatingFileHandler(
                filename=options.log_file_prefix,
                maxBytes=options.log_file_max_size,
                backupCount=options.log_file_num_backups,
                encoding="utf-8",
            )  # type: logging.Handler


# Generated at 2022-06-14 12:35:43.775225
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    tornado.options.options.log_file_prefix = '../logs/tornado.log'
    enable_pretty_logging()
# test_enable_pretty_logging()

# Generated at 2022-06-14 12:35:54.537672
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options
    import tornado.log
    import os
    import shutil
    import tempfile
    import time

    def test_log_file_prefix():
        tmpdir = tempfile.mkdtemp()
        try:
            log_file_prefix = os.path.join(tmpdir, "test_log")
            tornado.options.parse_command_line(
                ["dummy_arg", "--log_file_prefix=" + log_file_prefix]
            )
            tornado.log.enable_pretty_logging()
            tornado.log.info("test")
            assert os.path.exists(log_file_prefix)
            assert open(log_file_prefix).read().endswith(" - INFO - test\n")
        finally:
            shutil.rmtree(tmpdir)


# Generated at 2022-06-14 12:36:01.052230
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    import tornado.options
    import optparse
    parser = optparse.OptionParser()
    parser.add_option(
        "--logging", default="info", help="Logging verbosity, 0-50 (default: %default)"
    )
    tornado.options.parse_command_line([], None, parser)
    formatter = LogFormatter()
    assert formatter != None

# Generated at 2022-06-14 12:36:03.389420
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    msg = LogFormatter()
    assert msg.datefmt == "%Y-%m-%d %H:%M:%S"


# Generated at 2022-06-14 12:36:09.747107
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert f._colors == {
        logging.DEBUG: "\x1b[2;37m",
        logging.INFO: "\x1b[2;32m",
        logging.WARNING: "\x1b[2;33m",
        logging.ERROR: "\x1b[2;31m",
        logging.CRITICAL: "\x1b[2;35m",
    }
    assert f._normal == "\x1b[0m"



# Generated at 2022-06-14 12:37:06.382583
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    assert LogFormatter() is not None



# Generated at 2022-06-14 12:37:11.230207
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    """Test for function enable_pretty_logging"""
    logging.info("test for function enable_pretty_logging")
    enable_pretty_logging()


__test__ = {"test_enable_pretty_logging": test_enable_pretty_logging}

# Generated at 2022-06-14 12:37:21.231449
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    fmt = "%(name)s"
    datefmt = "%H:%H"
    style = "%"
    color = True
    colors = {
        0:0,
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
    }
    formatter = LogFormatter(fmt, datefmt, style, color, colors)
    assert formatter._colors == colors
    assert formatter._normal == "\033[0m"
    assert formatter._fmt == fmt


# Generated at 2022-06-14 12:37:30.043835
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import logging
    from tornado import logging
    from tornado import options
    from tornado import escape
    from tornado.util import unicode_type
    from typing import Any, Optional, List

    options.log_file_prefix = options.log_rotate_mode = 'size'
    options.log_file_max_size = options.log_file_num_backups = 50
    options.log_rotate_when = options.log_rotate_interval = 'time'
    options.logging = 'none'
    options.log_to_stderr = None
    options.log_file_prefix = None
    options.log_rotate_mode = None
    options.log_file_max_size = None
    options.log_file_num_backups = None
    options.log_rotate_when = None
   

# Generated at 2022-06-14 12:37:31.698706
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    assert True
test_enable_pretty_logging()

# Generated at 2022-06-14 12:37:32.525403
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
  assert enable_pretty_logging() == None

# Generated at 2022-06-14 12:37:43.987784
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    import tornado.options  # type: ignore

    tornado.options.define(
        "logging", default="none", help="Set the Python log level", type=str,
    )
    tornado.options.define(
        "log_file_prefix",
        default=None,
        metavar="PATH",
        type=str,
        help="Path prefix for log files. "
        + "Note that if you are running multiple tornado processes, "
        + "log_file_prefix must be different for each of them (e.g. "
        + "include the port number)",
    )

# Generated at 2022-06-14 12:37:45.928807
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    # type: () -> None
    t = LogFormatter()
    assert isinstance(t, LogFormatter)


# Generated at 2022-06-14 12:37:47.681449
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    formatter = LogFormatter()
    assert isinstance(formatter, logging.Formatter)



# Generated at 2022-06-14 12:37:50.261925
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    logging.basicConfig()
    enable_pretty_logging()
    logger = logging.getLogger()
    logger.info('test')

# Generated at 2022-06-14 12:39:59.798621
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    record = logging.LogRecord('1','2','3','4','5','{}','7','8','9','10', '11')
    record.levelno = 10
    LogFormatter().format(record)


# Generated at 2022-06-14 12:40:02.649700
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    TestLogFormatter = LogFormatter("%(message)s")
    TestLogFormatter.format(logging.LogRecord("", 20, None, None, "test message", None, None))
    assert True

# Generated at 2022-06-14 12:40:14.208690
# Unit test for method format of class LogFormatter
def test_LogFormatter_format():
    class record(object):
        __slots__ = ["logger", "name", "levelno", "levelname", "pathname", "filename", "module", "lineno", "funcName", "created", "asctime", "msecs", "relativeCreated", "thread", "threadName", "processName", "process", "message", "color", "end_color", "args", "exc_info", "exc_text"]
        def __init__(self, **args):
            for key in args:
                setattr(self, key, args[key])
    formatter = LogFormatter()
    assert formatter.format(record(message = "test")) == "[I 00000000 root:0] test"
# End of method test of class LogFormatter


# Generated at 2022-06-14 12:40:15.971278
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    LogFormatter()

if __name__ == "__main__":
    test_LogFormatter()

# Generated at 2022-06-14 12:40:23.351446
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_format = LogFormatter()
    # The only thing that can raise an exception is the fmt kwarg
    log_format = LogFormatter(fmt="%(message)s")
    # non-existent field raises a KeyError exception
    try:
        log_format = LogFormatter(fmt="%(non_existent)s")
    except KeyError:
        pass
    # test the optional arguments
    log_format = LogFormatter(
        fmt="%(message)s", datefmt="%Y-%m-%d %H:%M:%S", style="%", color=False
    )



# Generated at 2022-06-14 12:40:26.511820
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    log_formatter = LogFormatter(color=True)  # type: ignore
    assert isinstance(log_formatter, LogFormatter)


# override log functions

# Generated at 2022-06-14 12:40:28.279830
# Unit test for constructor of class LogFormatter
def test_LogFormatter():
    f = LogFormatter()
    assert f



# Generated at 2022-06-14 12:40:39.266118
# Unit test for function enable_pretty_logging
def test_enable_pretty_logging():
    # Bascially the same test as
    #   https://github.com/tornadoweb/tornado/blob/master/tornado/test/util_test.py#L947-L958
    import tornado.options
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    enable_pretty_logging(options = tornado.options.Options, logger = logger)
    tornado.options.define("log_file_prefix", type = str, default = "")
    tornado.options.define("log_rotate_mode", type = str, default = "time")
    tornado.options.define("log_file_num_backups", type = int, default = 5)
    tornado.options.define("log_rotate_when", type = str, default = "D")
    tornado.options