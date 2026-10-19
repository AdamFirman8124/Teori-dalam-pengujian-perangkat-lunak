

# Generated at 2022-06-14 12:46:42.861069
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # type: () -> None
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import Application, RequestHandler
    from tornado.httpserver import HTTPServer
    from tornado.httputil import url_concat
    from tornado.ioloop import IOLoop
    import logging
    import unittest

    # define("port", default=8888, help="port")
    # define("name", default="Zhang Song", help="name")

    class TestHandler(RequestHandler):
        def get(self):
            self.write("name: " + options.name)

    class TestApp(Application):
        def __init__(self):
            handlers = [("/", TestHandler)]
            Application.__init__(self, handlers, **options.group_dict("application"))


# Generated at 2022-06-14 12:46:46.114776
# Unit test for method set of class _Option
def test__Option_set():
    # Test with no initialization
    option = _Option()
    option.set(option)
    # Test with parameters
    option = _Option()
    option.set(option)

# Generated at 2022-06-14 12:46:56.109733
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    
    # Create a temporary directory and inject it into option
    import tempfile
    test_dir = tempfile.TemporaryDirectory()
    test_dir.cleanup() # Let's make sure the directory is removed after testing
    parser = OptionParser()
    # parser.define('data_path', default='./data/')
    parser.define('data_path', default='{}'.format(test_dir.name))

    # Create a temporary configuration file and inject option into it
    # test_obj_path = tempfile.mktemp(prefix='test_OptionParser_parse_config_file')
    test_obj_path = os.path.join(test_dir.name, "test_OptionParser_parse_config_file.cfg")

# Generated at 2022-06-14 12:47:08.525020
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import tempfile
    from tornado.testing import get_unused_port, bind_unused_port
    from tornado.httpserver import HTTPServer
    import tornado.web
    import unittest
    import _pytest


    class HelloHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello")


    def run_app(app):
        # tornado.web.httpserver.HTTPServer
        server = HTTPServer(app)
        # /usr/lib/python3.8/socketserver.py::BaseServer::__init__
        #   -> /usr/lib/python3.8/socketserver.py::BaseServer::bind
        #      -> /usr/lib/python3.8/socketserver.py::TCPServer::server_bind
        #

# Generated at 2022-06-14 12:47:20.945763
# Unit test for method parse of class _Option
def test__Option_parse():
    opt = _Option("name", None, type=str, help="", metavar=None, multiple=False,
                file_name=None, group_name=None, callback=None)
    v = opt.parse("str")
    assert v == "str"
    v = opt.parse("None")
    assert v == "None"

    opt = _Option("name", None, type=int, help="", metavar=None, multiple=False,
                file_name=None, group_name=None, callback=None)
    v = opt.parse("10")
    assert v == 10
    v = opt.parse("None")
    assert v == 10


# Generated at 2022-06-14 12:47:28.119293
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Setup
    options = OptionParser()
    options.define('name', type=str, default='')
    # Exercise
    config_file_name = "config_file.py"
    config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), config_file_name)
    options.parse_config_file(config_file_path)
    # Verify
    assert options.name == 'config_file'


@pytest.mark.concurrent
async def test_OptionParser_parse_config_file_async():
    # Setup
    options = OptionParser()
    options.define('name', type=str, default='')
    # Exercise
    config_file_name = "config_file.py"
    config_file_path

# Generated at 2022-06-14 12:47:32.022817
# Unit test for method set of class _Option
def test__Option_set():
    # Create an object of class _Option
    _option = _Option('name', type=int, multiple=True)
    _option.set('1')
    assert _option.value() == '1'
    _option.set('test')
    assert _option.value() == 'test'


# Generated at 2022-06-14 12:47:33.162034
# Unit test for method define of class OptionParser
def test_OptionParser_define():
    pass




# Generated at 2022-06-14 12:47:38.110936
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    """ Unit test for method OptionParser.__iter__ """
    # get a options.OptionParser instance
    parser = options.OptionParser()
    # set some attributes
    parser.options = {'a': 'A'}
    # get the corresponding iterator
    it = iter(parser)
    # the iterator should be an iterator
    assert isinstance(it, Iterator)

# Generated at 2022-06-14 12:47:49.712877
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # This file is used by test_logging_config_file
    with open("test_logging_config_file.conf", "w") as f:
        f.write("""
logging_level = 40
""")
    logging_level = define("logging_level", 1, int)
    options.parse_config_file("test_logging_config_file.conf", final=False)
    assert logging_level.value == 40
    logging_level.value = 100
    assert logging_level.value == 100
    os.remove("test_logging_config_file.conf")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 12:48:09.211127
# Unit test for method parse of class _Option
def test__Option_parse():
    def set_options(**kwargs: Any) -> None:
        for name, value in kwargs.items():
            setattr(options, name, value)

    def set_default_options() -> None:
        set_options(
            port=80,
            mysql_host="mydb.example.com:3306",
            memcache_hosts=["cache1.example.com:11011",
                            "cache2.example.com:11011"],
        )

    def check_options(error: Optional[str], **kwargs: Any) -> None:
        if error:
            with pytest.raises(Error) as e:
                set_options(**kwargs)
            assert str(e.value) == error
        else:
            set_options(**kwargs)

# Generated at 2022-06-14 12:48:17.396880
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    # OptionParser.group_dict(group)

    # The names and values of options in a group.
    from tornado.options import define, parse_command_line, options
    define('template_path', group='application')
    define('static_path', group='application')
    parse_command_line()
    assert options.group_dict('application') == {}
    options.template_path = '/app/templates'
    options.static_path = '/app/static'
    assert options.group_dict('application') == {
        'template_path': '/app/templates',
        'static_path': '/app/static',
    }


# Generated at 2022-06-14 12:48:21.639618
# Unit test for method set of class _Option
def test__Option_set():
    def callback(value):
        pass
    option = _Option('name',
                     default=None,
                     type=None,
                     help=None,
                     metavar=None,
                     multiple=False,
                     file_name=None,
                     group_name=None,
                     callback=callback)
    option.set("x")


# Generated at 2022-06-14 12:48:35.279379
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():

    # The type of args is List[str]
    args = None
    # The type of final is bool
    final = True
    # The type of x_rest is List[str]
    x_rest = None

    # Line: 7 ->    def parse_command_line(self, args: Optional[List[str]] = None, final: bool = True) -> List[str]:

    # Line: 8 ->        if args is None:
    if args is None:

        # Line: 9 ->            args = sys.argv
        args = sys.argv
    # Line: 12 ->        remaining = []  # type: List[str]
    remaining = []  # type: List[str]
    # Line: 13 ->        for i in range(1, len(args)):

# Generated at 2022-06-14 12:48:36.570899
# Unit test for method define of class OptionParser
def test_OptionParser_define():
    parser = OptionParser()

# Generated at 2022-06-14 12:48:46.173480
# Unit test for method parse of class _Option
def test__Option_parse():
    o = _Option('name', type=basestring_type)
    assert o.parse('value') == 'value'
    o = _Option('number', type=int)
    assert o.parse('1') == 1
    assert o.parse('0') == 0
    assert o.parse('-1') == -1
    o = _Option('float', type=float)
    assert o.parse('0') == 0.0
    assert o.parse('0.0') == 0.0
    assert o.parse('0.1') == 0.1
    assert o.parse('-0.1') == -0.1
    o = _Option('bool', type=bool)
    assert o.parse('true') == True
    assert o.parse('True') == True
    assert o.parse('False') == False

# Generated at 2022-06-14 12:48:51.812330
# Unit test for method parse of class _Option
def test__Option_parse():
    _Option_parse_func = _Option.parse
    if isinstance(
            _Option_parse_func, (staticmethod, classmethod)
        ):
        _Option_parse_func = _Option_parse_func.__func__
    assert _Option_parse_func.__defaults__ is None
    assert _Option_parse_func.__code__.co_argcount == 2
    assert _Option_parse_func.__code__.co_varnames[
        : _Option_parse_func.__code__.co_argcount
    ] == ("self", "value")



# Generated at 2022-06-14 12:48:53.389551
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    print(OptionParser().parse_command_line(["--key1", "value1", "--key2", "value2", "--key3", "value3"]))

# Generated at 2022-06-14 12:49:06.199582
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    parser = options.OptionParser()
    parser.define("name", default="Group1", type=str, help="help", metavar="Metavar", multiple=False, group="Group1")
    parser.define("name", default="Group2", type=str, help="help", metavar="Metavar", multiple=False, group="Group2")
    parser.define("name", default="Group1", type=str, help="help", metavar="Metavar", multiple=False, group="Group1")
    parser.define("name", default="Group2", type=str, help="help", metavar="Metavar", multiple=False, group="Group2")
    parser.define("name", default="", type=str, help="help", metavar="Metavar", multiple=False, group="") # group is not specified

# Generated at 2022-06-14 12:49:09.386407
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # test for function parse_config_file() of class OptionParser in file args.py
    from tornado.httputil import HTTPServerRequest
    
    
    
    
    
    
    
    
    
    
    pass

# Generated at 2022-06-14 12:49:23.555839
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    define("name")
    define("age", type=int)
    values = dict(name="Aaron", age=30)
    parser = OptionParser()
    parser.parse_command_line(
        ["prog", "--name=%(name)s" % values, "--age=%(age)d" % values]
    )
    assert list(parser) == ["name", "age"]



# Generated at 2022-06-14 12:49:30.297502
# Unit test for method parse of class _Option
def test__Option_parse():
    option = _Option('name',default='string',type=str,help='help')
    assert option.parse('hello') == 'hello'
    option = _Option('name',default='2018-12-30 10:30:00',type=datetime.datetime,help='help')
    assert option.parse('hello') == 'hello'



# Generated at 2022-06-14 12:49:36.262270
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    cfg_file = 'tests/test_parse_config_file/config.cfg'
    _dict_1 = {
        '__file__': 'tests/test_parse_config_file/config.cfg',
        'host': ['0.0.0.0'],
        'port': ['8009'],
        'debug': [True],
        'min_chunk_size': ['131072'],
        'max_chunk_size': ['1048576'],
        'max_body_size': ['1048576'],
        'ssl_options': [None]
    }
    parser = OptionParser()
    parser.define('host', type=list, multiple=True)
    parser.define('port', type=int, multiple=False)
    parser.define('debug', type=bool, multiple=False)

# Generated at 2022-06-14 12:49:39.687435
# Unit test for method parse of class _Option
def test__Option_parse():
    value = 'a'
    obj = _Option('name',type=datetime.datetime,help='help',metavar='metavar')
    result = obj.parse(value)
    expected_result = 'a'
    assert result == expected_result


# Generated at 2022-06-14 12:49:46.770709
# Unit test for method set of class _Option
def test__Option_set():
    # form the arguments
    # Check if the method set works the same way as an actual method of the object 
    # created in the target program.
    
    
    name=''
    default = None
    type = None
    help=''
    metavar=''
    multiple = False
    file_name = None
    group_name = None
    callback = None
    # create a option object
    options = _Option(name,default,type,help,metavar,multiple,file_name,group_name,callback)
    
    
    
    
    if options()== 0:
        print('Pass')
    else:
        print('Fail')

# Generated at 2022-06-14 12:49:55.475395
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    OptionParser.parse_config_file(OPTIONS_FILE)
    assert(isinstance(options.port, int))
    assert(options.port == 80)
    assert(isinstance(options.mysql_host, str))
    assert(options.mysql_host == 'mydb.example.com:3306')
    assert(isinstance(options.memcache_hosts, list))
    assert(options.memcache_hosts == \
            ['cache1.example.com:11011', 'cache2.example.com:11011'])
    assert(options.ioloop_time_monotonic == False)
    assert(options.ioloop_time_monotonic == False)
    assert(options.supervisor_datetime == datetime.datetime(2014, 2, 1, 16, 47))

# Generated at 2022-06-14 12:50:06.903148
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import unittest
    import io
    from tornado.options import options
    from tornado.options import OptionParser
    from tornado.options import Error
    from tornado.options import define
    from tornado.options import is_ascii
    from tornado.options import _CONFIG_DEFAULTS
    from tornado.options import _parse_config_file
    from tornado.options import _import_config_file
    from tornado.options import _CONFIG_DEFAULTS
    from tornado.options import _CONFIG_DEFAULTS

    class TestOptionParserParseConfigFile(unittest.TestCase):
        def setUp(self):
            self.parser = OptionParser()


# Generated at 2022-06-14 12:50:12.526533
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Config file containing multiple options
    yaml_test_multiple = """
    config_file_multiple:
        port: 80
        mysql_host: "mydb.example.com:3306"
        memcache_hosts: ['cache1.example.com:11011']
        """
    # Parser for the above config file
    option_parser_config_multiple = OptionParser()
    option_parser_config_multiple.define('port', type=int, default=80)
    option_parser_config_multiple.define('mysql_host', type=str, default="")
    option_parser_config_multiple.define("memcache_hosts", type=str,default="'['",multiple=True)

    # Config file containing one option

# Generated at 2022-06-14 12:50:17.722728
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    """
    **INPUT**

    * [*sys.argv*] - a list of arguments (normally, the sys.argv list)

    **OUTPUT**

    * The remaining arguments.
    """
    # 0. Normal operation
    sys.argv = ['myscript', '-d', 'opt1']
    assert options.parse_command_line() == []
    assert options.debug == True

    # 1. Unknown command line option
    sys.argv = ['myscript', '-d', 'opt1']
    try:
        options.parse_command_line(["-d", "opt1", "--nonsense", "-p", "opt2"])
    except Error as e:
        assert True
    else:
        assert False

    # 2. Command line option requires a value

# Generated at 2022-06-14 12:50:29.000303
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # From the documentation
    define("port", default=8888, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode")
    opt = options._OptionParser()
    args = opt.parse_command_line([])
    assert args == []
    # test
    assert opt.port == 8888
    assert opt.debug == False
    assert sorted(opt.group_dict()) == ["server"]
    assert opt.as_dict() == {"debug": False, "port": 8888}
    assert sorted(opt.groups()) == ["server"]
    define("name", default="bob", help="name", type=str)
    define("age", default=18, help="age", type=int)
    opt = options._OptionParser()
    args = opt.parse_command_

# Generated at 2022-06-14 12:50:56.246302
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    from tornado.options import options, define

    define('port', type=int, help="help")

    testfile = "testfile.conf"

    with open(testfile, "w") as f:
        f.write('port = 80\n')

    options.parse_config_file(testfile)

    if options.port == 80:
        print("case 1 passed")

    with open(testfile, "w") as f:
        f.write('port = -1\n')
    try:
        options.parse_config_file(testfile)
    except Error:
        print("case 2 passed")

    with open(testfile, "w") as f:
        f.write('port = "abc"\n')

# Generated at 2022-06-14 12:51:02.141195
# Unit test for method parse of class _Option
def test__Option_parse():
    Date_time = _Option('date_time', type=datetime.datetime)
    time_delta = _Option('time_delta', type=datetime.timedelta)
    bool_value = _Option('bool_value', type=bool)
    string_value = _Option('string_value', type=basestring_type)
    multiple = _Option('multiple', type=int, multiple=True)
    print(Date_time.parse('Tue Apr 17 21:50:34 2012'))
    print(time_delta.parse('1.5H'))
    print(bool_value.parse('True'))
    print(string_value.parse('string'))
    print(multiple.parse('0, 1, 2, 3'))

test__Option_parse()


# Generated at 2022-06-14 12:51:03.813936
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option('name',help="help",metavar="metavar")
    option.set(['name'])



# Generated at 2022-06-14 12:51:12.570035
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import tornado
    import os
    # tornado.options.options.hello
    with open("option.cfg", "w") as f:
        f.write("hello = 100\n")
    # tornado.options.options.hello = 100
    tornado.options.parse_config_file("option.cfg")
    hello = tornado.options.options.hello
    assert hello == 100
    os.remove("option.cfg")

    # tornado.options.options.hello
    with open("option.cfg", "w") as f:
        f.write("hello = [1,2,3]\n")
    # tornado.options.options.hello = [1,2,3]
    tornado.options.parse_config_file("option.cfg")
    hello = tornado.options.options.hello
    assert hello == [1,2,3]

# Generated at 2022-06-14 12:51:24.579891
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    
    op = OptionParser()
    # Defining a new option
    op.define('test', default = 3, multiple = True)
    
    # Create a config file
    dirpath = tempfile.mkdtemp()
    configFilePath = dirpath + '/test.conf'
    with open(configFilePath, "w") as f:
        f.write('test = 2')
    
    # Parse the config file
    op.parse_config_file(configFilePath)
    print(op.options["test"].value())
    assert(op.options["test"].value() == [2])
    
    # Clean up
    os.remove(configFilePath)
    os.rmdir(dirpath)
    
test_OptionParser_parse_config_file()

# Individual Unit tests for method parse_command

# Generated at 2022-06-14 12:51:34.970496
# Unit test for method set of class _Option
def test__Option_set():
    """Unit test for method set of class _Option"""
    import doctest
    import tornado.options
    import io
    import sys
    import unittest

    stdout = io.StringIO()  # type: Any
    sys.stdout = stdout
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(tornado.options))
    unittest.TextTestRunner(descriptions=0, verbosity=2).run(suite)
    sys.stdout = sys.__stdout__

# Generated at 2022-06-14 12:51:45.007056
# Unit test for method parse of class _Option
def test__Option_parse():
    option = _Option(
        name="name",
        default=None,
        type=datetime.datetime,
        help=None,
        metavar=None,
        multiple=False,
        file_name=None,
        group_name=None,
        callback=None
    )
    assert option.parse("now") == datetime.datetime.now()
    assert option.parse("2016-05-11 11:05:10") == datetime.datetime.strptime("2016-05-11 11:05:10", "%Y-%m-%d %H:%M:%S")


# Generated at 2022-06-14 12:51:54.426819
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    # print(">>>test_OptionParser_parse_command_line")

    # Create test instance of class OptionParser
    option_parser = OptionParser()

    # Define test option 'option_0'
    # - Type = bool
    # - Multiple = False
    option_parser.define(
        "option_0",
        default=False,
        type=bool,
        help="Option description",
        metavar="[True|False]",
        multiple=False,
        group="group_0",
        callback=None,
    )

    # Define test option 'option_1'
    # - Type = bool
    # - Multiple = False

# Generated at 2022-06-14 12:52:02.127095
# Unit test for method parse of class _Option
def test__Option_parse():
    assert _Option("a", type = int, multiple = False).parse("0") == 0
    assert _Option("a", type = int, multiple = True).parse("1,2,3") == [1,2,3]
    assert _Option("a", type = int, multiple = True).parse("0:3") == [0,1,2,3]
    assert _Option("a", type = int, multiple = True).parse("1") == [1]
    assert _Option("a", type = datetime.datetime, multiple = False).parse("2019-02-01 01:01:01") == datetime.datetime(2019,2,1,1,1,1)

# Generated at 2022-06-14 12:52:06.941509
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    from tornado_options import define, options

    define("name", group='group', default="Bob", help="help")
    options.parse_config_file('/Users/wangqiushi/workspace/tornado_app/app/options.conf')
    
    assert options.name == "Tom"
    assert options.group.name == "Tom"

# Generated at 2022-06-14 12:52:28.783349
# Unit test for method set of class _Option
def test__Option_set():
    """
    method set of class _Option
    """
    from tornado.options import _Option
    from tornado.options import Error

# Generated at 2022-06-14 12:52:39.776236
# Unit test for method parse of class _Option
def test__Option_parse():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.httpserver import HTTPServer

    class HomeHandler(RequestHandler):
        def post(self):
            val = parse_argument(self.request.body.decode(), 'start_date', str)
            self.set_header('Content-Type', 'text/plain')
            self.write(val)

    class Test(AsyncTestCase):
        def setUp(self):
            super(Test, self).setUp()
            # create an instance of the _Option class (the class to be tested here)

# Generated at 2022-06-14 12:52:47.559897
# Unit test for method parse of class _Option
def test__Option_parse():
    _option = _Option(
        'mock_name', default=None, type=str, help=None, metavar=None, multiple=True, file_name=None, group_name=None, callback=None
    )
    _option.parse('10:11')
    assert _option.value() == [10, 11]
    _option.parse('10')
    assert _option.value() == [10]
    _option.parse('10.4')
    assert _option.value() == [10.4]
    _option.parse('a')
    assert _option.value() == ['a']
    _option.parse('True')
    assert _option.value() == [True]
    _option.parse('False')
    assert _option.value() == [False]

# Generated at 2022-06-14 12:52:56.026104
# Unit test for method parse of class _Option
def test__Option_parse():
    from datetime import datetime
    seconds_in_a_day = 86400
    # from tornado import options
    # from tornado import options
    # from tornado import options
    # from tornado import options
    # from tornado import options
    options = OptionParser()
    print("-------------------------")
    print("Testing _Option.parse():")
    print("-------------------------")
    print()
    print("Test when the option is of type datetime.datetime:")
    print("----------------------------------")
    option = _Option("name", type=datetime.datetime)
    assert option.parse("2019-01-01T00:00:00") == datetime(2019, 1, 1, 0, 0, 0)

# Generated at 2022-06-14 12:53:07.593723
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    """
    Ensure that the method parse_config_file works as expected, by parsing the config file
    we have saved in the module, and ensuring that the options we have set in the config file
    are indeed stored in the options.options dictionary of the OptionParser class.
    The config file contains Python code that will be executed (so it is **not safe** to
    use untrusted config files).
    Anything in the global namespace that matches a defined option will be used to set
    that option's value.
    """
    global parsed_config

    if not parsed_config:
        # Parse the config file on module load
        # It's possible that the config file is not available yet at this point
        try:
            options.parse_config_file("config_file")
        except:
            pass
        parsed_config = True

    # Check that the options we

# Generated at 2022-06-14 12:53:17.664890
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    from tornado.options import OptionParser
    from tornado.log import enable_pretty_logging
    path = '/home/ubuntu/tornado_study_note/tornado_study_code/test_config_file.py'
    OptionParser().parse_config_file(path)
    # enable_pretty_logging()
    # 从我的理解来说, 执行此方法的作用是实现执行path指定的文件的内容, 而这个文件中的内容由define(name, default, type, help, metavar)方法定义
    # 其中参数name将作为别名, 参

# Generated at 2022-06-14 12:53:25.960140
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    path = "~/dev/tornado/tornado/test/options_test.conf"
    try:
        parse_config_file(path)
        assert options.port == 80
        assert options.mysql_host == "mydb.example.com:3306"
        assert options.memcache_hosts == ["cache1.example.com:11011", "cache2.example.com:11011"]
    except:
        assert False
# Exercise: Write unit test for method parse_command_line of class OptionParser
# Exercise: Write unit test for method print_help of class OptionParser
# Exercise: Write unit test for method define of class OptionParser
# Exercise: Write unit test for method add_parse_callback of class OptionParser
# Exercise: Write unit test for method run_parse_callbacks of class OptionParser
# Exercise: Write unit test for

# Generated at 2022-06-14 12:53:37.783957
# Unit test for method set of class _Option
def test__Option_set():
    import mock
    from types import GeneratorType
    from tornado.concurrent import Future
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import Application, RequestHandler, url
    from tornado.websocket import WebSocketHandler
    # CASE1: test with options.logging=None and options.log_level=None
    options = mock.Mock()
    options.logging = None
    options.log_level = None
    assert set(options) == set(dir(options)), '#case1: test with options.logging=None and options.log_level=None'
    # CASE2: test with options.logging="none" and options.log_level=None
    options = mock.Mock()
    options.logging = "none"
    options.log_level = None
    assert set

# Generated at 2022-06-14 12:53:47.950830
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    opts = OptionParser()
    opts.define('opt1', type=str)
    opts.define('opt2', type=str)
    opts.define('opt3', type=str)

    objs = [FakeObject(name='opt1'), FakeObject(name='opt2'), FakeObject(name='opt3')]
    opts.parse_config_file = Mock(side_effect = objs)
    opts.run_parse_callbacks = Mock()
    opts.parse_config_file('/fake/path', final=True)
    assert opts.parse_config_file.call_args[0][0] == '/fake/path'
    assert opts.parse_config_file.call_args[1] == {'final': True}
    opts.run_parse_callbacks.assert_

# Generated at 2022-06-14 12:53:55.281651
# Unit test for method parse of class _Option
def test__Option_parse():
    # Tested function in Options
    # Tested function in Options
    option_types = [
        (1, int),
        (1.1, float),
    ]
    option_values = [
        ('1', 1),
        ('1.1', 1.1),
        (str(1), 1),
        (str(1.1), 1.1),
    ]
    for i,j in option_values:
        assert _Option.parse(i,j) == j



# Generated at 2022-06-14 12:54:36.134513
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    options = OptionParser()
    options.define('config_file', type=str, callback=test_callback)
    _ = options.parse_command_line(['my_app.py', '--config_file=my_app.cfg'])
    assert _ == []
    assert options.config_file == 'my_app.cfg'
    
    options = OptionParser()
    options.define('config_file', type=str, callback=test_callback)
    _ = options.parse_command_line(['my_app.py', '--config_file', 'my_app.cfg'])
    assert _ == []
    assert options.config_file == 'my_app.cfg'
    
    options = OptionParser()
    options.define('config_file', type=str, callback=test_callback)

# Generated at 2022-06-14 12:54:41.184940
# Unit test for method set of class _Option
def test__Option_set():
    def mock_callable(value):
        print(value)
    option = _Option('name', unicode, help=unicode(), metavar=unicode(), multiple=True, file_name=unicode(), group_name=unicode(), callback=mock_callable)
    value = bool()
    # Testing
    option.set(value)

# Generated at 2022-06-14 12:54:48.624966
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    import unittest
    import options as m

    class MockableTest(unittest.TestCase):
        def test__Mockable___setattr__(self):
            m_options = MagicMock()
            m_options_originals = {}
            m_name = 'name'
            m_value = MagicMock()

            result = m._Mockable(m_options)
            result.__setattr__(m_name, m_value)
            
            self.assertEqual(m_options.__setattr__.call_args_list, [call(m_name, m_value)])
            self.assertEqual(m_options_originals, {})
            self.assertEqual(result._options, m_options)
            self.assertEqual(result._originals, {})


# Unit

# Generated at 2022-06-14 12:54:58.288800
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import unittest
    import io
    import os

    class OptionParser_TestCase(unittest.TestCase):
        def test_parse_config_file(self):
            with io.StringIO() as f:
                f.write("a = 1\n")
                f.seek(0)
                options = OptionParser()
                options.define(name="a", type=int)
                options.parse_config_file(f.name)
                self.assertEqual(options.a, 1)
                f.close()
                os.remove(f.name)
    return OptionParser_TestCase()


# Generated at 2022-06-14 12:55:03.681372
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    from tornado.options import options, define
    define("a1", type=int, group="a", default=1)
    define("a2", type=int, group="a", default=2)
    define("b", type=int, group="a", default=10)
    define("c1", type=int, group="c", default=100)
    define("c2", type=int, group="c", default=200)
    assert (options.group_dict("a")["a1"] == 1)
    assert (options.group_dict("a")["a2"] == 2)
    assert (options.group_dict("a")["b"] == 10)
    assert (options.group_dict("c")["c1"] == 100)
    assert (options.group_dict("c")["c2"] == 200)
   

# Generated at 2022-06-14 12:55:09.010784
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    # Arrange
    opt = OptionParser()

    # Act
    opt.define(name='template_path', group='application')
    opt.define(name='static_path', group='application')
    opt.parse_command_line()

    # Assert
    assert opt.group_dict('application') == {'template_path': False, 'static_path': False}



# Generated at 2022-06-14 12:55:22.031922
# Unit test for method set of class _Option
def test__Option_set():
    op = _Option(
        name='mysql_database',
        default='test', 
        type=str, 
        help=None, 
        metavar=None, 
        multiple=False, 
        file_name=None,
        group_name=None, 
        callback=None
    )
    op.set('test')

    # another case 
    op = _Option(
        name='memcache_hosts',
        default=['cache1.example.com:11011', 'cache2.example.com:11011'], 
        type=str, 
        help=None, 
        metavar=None, 
        multiple=True, 
        file_name=None,
        group_name=None, 
        callback=None
    )

# Generated at 2022-06-14 12:55:28.538614
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    t_dir = os.path.dirname(os.path.realpath(__file__))
    t_dir = os.path.join(t_dir, "test_data")
    t_dir = os.path.join(t_dir, "options.py")
    test_OP = OptionParser()
    test_OP.define("test_1", default="test_1_default", type=str, help="test_1")
    test_OP.define("test_2", default="test_2_default", type=str, help="test_2")
    test_OP.parse_config_file(path=t_dir)
    assert test_OP.test_1 == "test_1_value"
    assert test_OP.test_2 == "test_2_value"



# Generated at 2022-06-14 12:55:38.151276
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    if (not os.path.exists("my_config.py")):
        #os.chdir("..")
        os.chdir("/home/travis/build/ms-jpq/tornado/tornado")
    print(os.getcwd())
    options = OptionParser()
    options.define("port", type=int, default=8080)
    options.define("ip", default="8.8.8.8")
    options.parse_config_file("my_config.py")
    print(options.port)
    print(options.ip)

# Generated at 2022-06-14 12:55:40.191094
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    """
    Test for method parse_config_file of class OptionParser
    """
    _test_OptionParser_parse_config_file()
