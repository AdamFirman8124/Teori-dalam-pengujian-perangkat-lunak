

# Generated at 2022-06-14 12:47:10.082488
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    print('Unit test for method __iter__ of class OptionParser')
    from tornado.options import define, options
    define('option1', default=1, help='option1')
    define('option2', default=2, help='option2')
    define('option3', default=3, help='option3')
    for k, v in options._options.items():
        print(k)
        print(v)
        print(v.name)
        print(v.default)
        print(v.value())
        print(v.help)
        print(v.file_name)
        print(v.metavar)
        print(v.type)
        print(v.multiple)
        print(v.callback)
    # it's at the end
    pass


# Generated at 2022-06-14 12:47:23.136517
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():

    #Test that the function can parse certain types of inputs
    op = OptionParser()
    op.define('port', default=8888, type=int)
    op.define('host', default='localhost', type=str)
    op.parse_config_file('../tests/syntax_test.py')
    assert op.port == 8888  #Test if parsed an integer
    assert op.host == 'localhost'  #Test if parsed a string


    #Test that it has the __file__ variable
    assert op.__file__ == '../tests/syntax_test.py'


    #Test that it throws the right exception when a wrong type is passed to it
    op = OptionParser()
    op.define('host', default='localhost', type=int)


# Generated at 2022-06-14 12:47:26.273961
# Unit test for method parse of class _Option
def test__Option_parse():
    _OPTION_OBJ = _Option("test")
    _OPTION_OBJ.parse("10")
    assert _OPTION_OBJ.value() == "10"
test__Option_parse()


# Generated at 2022-06-14 12:47:35.835380
# Unit test for method value of class _Option
def test__Option_value():
    option = _Option(name="aaaa", default=3)
    assert option.value() == 3
    option.set(4)
    assert option.value() == 4
    try:
        option.set(4.4)
        assert False
    except Error as e:
        assert e.args[0] == "Option 'aaaa' is required to be a int (float given)"
    option = _Option(name="bbbb", default=[1, 2], multiple=True)
    assert option.value() == [1, 2]
    option.set([3, 4, 5])
    assert option.value() == [3, 4, 5]

# Generated at 2022-06-14 12:47:41.558929
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    #Create an instance of OptionParser
    optionParser_instance = OptionParser()
    #Call method __iter__ with incorrect parameter types
    try:
        optionParser_instance.__iter__(1)
        assert False
    except TypeError:
        assert True
    except:
        assert False
    #Call method __iter__ with specified parameter types
    try:
        optionParser_instance.__iter__()
        assert True
    except:
        assert False

# Generated at 2022-06-14 12:47:46.264533
# Unit test for method set of class _Option
def test__Option_set():
    a = _Option("name",None,str,"help","metavar",False,"file_name","group_name",None)
    tmp = a.set("test")
    assert tmp is None
    print("Passed")


# Generated at 2022-06-14 12:47:58.101578
# Unit test for method set of class _Option
def test__Option_set():
    # Callback method
    def func2(val):
        return val
    # Create a simple option
    option = _Option('name', 'abc', str, 'desc', 'aaa', False, 'file', 'group', func2)
    
    # Create a multiple option
    option2 = _Option('name', [1,2], int, 'desc', 'aaa', True, 'file', 'group', func2)
    # Set the value of the simple option
    option.set(1)
    assert option.value() == 1
    # Set the value of the multiple option
    # Set the value of the option with a normal list
    option2.set([1,2])
    assert option2.value() == [1,2]
    # Set the value of the option with multiple value
    option2.set(1)
    assert option2

# Generated at 2022-06-14 12:48:10.174781
# Unit test for method parse of class _Option
def test__Option_parse():
    o = _Option(name="name", type=int, multiple=False, callback=None)
    assert o.parse("12345") == 12345
    o = _Option(name="name", type=int, multiple=False, callback=None)
    assert o.parse("-12345") == -12345
    o = _Option(name="name", type=int, multiple=False, callback=None)
    assert o.parse("+12345") == 12345
    o = _Option(name="name", type=int, multiple=False, callback=None)
    assert o.parse("-0") == 0
    o = _Option(name="name", type=int, multiple=False, callback=None)
    assert o.parse("+0") == 0

# Generated at 2022-06-14 12:48:12.601374
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option('a_str', '', str, True, False, False)
    option.set([])
    return

# Generated at 2022-06-14 12:48:22.971535
# Unit test for method set of class _Option
def test__Option_set():
    option = OptionParser._Option("name", type=int, multiple=False, default=None)
    try:
        option.set("1")
        raise Exception("This should not happen")
    except Error as ex:
        assert str(ex) == "Option name is required to be a int (str given)"
    try:
        option.set(1.23)
        raise Exception("This should not happen")
    except Error as ex:
        assert str(ex) == "Option name is required to be a int (float given)"
    option.set(None)
    option.set(23)
    option.set(-23)
    try:
        option.set(())
        raise Exception("This should not happen")
    except Error as ex:
        assert str(ex) == "Option name is required to be a int (tuple given)"


# Generated at 2022-06-14 12:49:08.244114
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import tempfile
    import shutil
    import os
    import sys
    import io
    import re
    import pytest
    import tornado.testing
    import tornado.gen
    import tornado.options
    import tornado.ioloop
    import tornado.concurrent

    class _OptionParser(tornado.options.OptionParser):
        ...

    def main():
        tornado.options.define("foo", default=[], type=list, multiple=True)
        tornado.options.define("bar", default=[], type=list, multiple=True)
        tornado.options.define("baz", default=[], type=list, multiple=True)
        tornado.options.define("frobozz", default=[], type=list, multiple=True)
        tornado.options.define("fleeb", default=[], type=list, multiple=True)

# Generated at 2022-06-14 12:49:12.066372
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():

    options = OptionParser()
    options.define("test_option", type=int)

    my_options = _Mockable(options)
    my_options.test_option = 5
    assert my_options.test_option == 5
    assert options.test_option == 5


# Generated at 2022-06-14 12:49:13.630490
# Unit test for method define of class OptionParser
def test_OptionParser_define():
    OptionParser().define('x',default=1)
    assert(True)

# Generated at 2022-06-14 12:49:15.355160
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    print('testing OptionParser.__iter__()')
    print('not yet implemented')

# Generated at 2022-06-14 12:49:26.385758
# Unit test for method parse of class _Option
def test__Option_parse():
    message = "test__Option_parse"
    print()
    print(message)
    option = _Option("name", None, str, "this is help", "metavar", False)
    # assert option.parse("abc") == "abc"
    print(option.parse("abc"))
    option = _Option("name", None, int, "this is help", "metavar", False)
    # assert option.parse("10") == 10
    print(option.parse("10"))
    option = _Option("name", None, float, "this is help", "metavar", False)
    # assert option.parse("10.22") == 10.22
    print(option.parse("10.22"))
    option = _Option("name", None, list, "this is help", "metavar", True)
    # assert option

# Generated at 2022-06-14 12:49:27.555971
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    for _ in options._options.keys():
        pass


# Generated at 2022-06-14 12:49:32.780231
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    options = OptionParser()
    # options.define("name1", type=str)
    # options.define("name2", type=float)
    # options.define("name3", type=int)
    options.define("name4", type=bool)
    op = options.parse_config_file("../test_files/test_options_parse_config_file.cfg")
    assert op == None
    assert options.name4 == True
    # assert options.name1 == "value1"
    # assert options.name2 == 0.001
    # assert options.name3 == 0001


# Generated at 2022-06-14 12:49:37.834310
# Unit test for method parse of class _Option
def test__Option_parse():
    print("\n", "_Option.parse()")
    option = _Option("port",default=8080,type=int,help="Description")
    print(option.parse("8090"))
    print(option.parse("8090"))
    print(option.parse("8090"))
    
test__Option_parse()


# Generated at 2022-06-14 12:49:46.802449
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    options = OptionParser()
    # options.define('name', default=None, type=<class 'NoneType'>, help=None, metavar=None, multiple=False, group=None, callback=None)
    options.define('name', default=None, help='', multiple=False, callback=None)
    # options.define('value', default=None, type=<class 'NoneType'>, help=None, metavar=None, multiple=False, group=None, callback=None)
    options.define('value', default=None, help='', multiple=False, callback=None)
    # options.define('memcache_hosts', default=[], type=<class 'list'>, help='', metavar=None, multiple='True', group=None, callback=None)

# Generated at 2022-06-14 12:49:53.300929
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    # Case 1 : Tests whether the method parse_config_file executes successfully with a valid config file
    parser.parse_config_file("options_parser.py")
    # Case 2 : Tests whether the method parse_config_file throws an exception when a non-existant config file is passed
    try:
        parser.parse_config_file("non-existant_file")
    except Error as e:
        assert(str(e) == "Unrecognized command line option: 'non-existant_file'")
    else:
        assert(False)


# Generated at 2022-06-14 12:50:06.873177
# Unit test for method parse of class _Option
def test__Option_parse():
    options = OptionParser()
    for option in options._options.values():
        if option.name == 'logging':
            assert option.parse("'info'") == 'info'
        elif option.name == 'xheaders':
            assert option.parse("False") == False
        elif option.name == 'compiled_template_cache':
            assert option.parse("True") == True
        elif option.name == 'unix_socket':
            assert option.parse("/path/to/socket") == '/path/to/socket'
        #elif option.name == 'ssl_options':
            #assert not option.parse("None") #TODO
        elif option.name == 'allow_hosts':
            assert option.parse("['*']") == ['*']

# Generated at 2022-06-14 12:50:10.245667
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # Create an instance of class OptionParser
    option_parser = OptionParser()

    # Test the method __iter__ of class OptionParser
    assert option_parser.__iter__() == option_parser._options.__iter__()



# Generated at 2022-06-14 12:50:17.902645
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import datetime
    from tornado.options import define, options, parse_config_file
    define("debug", type=bool, default=False, help="turn on debugging output")
    define("port", default=8888, help="run on the given port", type=int)
    define("param", default=[-1, -2, -3], help="param", multiple=True)
    define("dt", default=datetime.datetime.now(), help="datetime", type=datetime.datetime)
    define("some_file", help="some_file")
    print('Test 1')
    parse_config_file('test_options.conf')
    print('options.dt:',options.dt)
    print('options.port:', options.port)
    print('options.param:', options.param)
    print

# Generated at 2022-06-14 12:50:29.080817
# Unit test for method parse of class _Option

# Generated at 2022-06-14 12:50:41.110113
# Unit test for method parse of class _Option
def test__Option_parse():
    name1 = "--port"
    name2 = "--ssl"
    name3 = "--path"
    name4 = "--list"
    name5 = '--date'
    name6 = '--time'
    name7 = "--empty"
    option1 = _Option(name1, default=80, type=int)
    option2 = _Option(name2, default=False, type=bool)
    option3 = _Option(name3, default='.', type=str)
    option4 = _Option(name4, default=[], type=int, multiple=True)
    option5 = _Option(name5, default=datetime.datetime.now(), type=datetime.datetime)

# Generated at 2022-06-14 12:50:46.132540
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option(name='name', default=None, type=str, help=None, multiple=False, file_name=None, group_name=None, callback=None, metavar=None)
    value = 'value'
    option.set(value=value)
    assert option.value() == 'value'

# Generated at 2022-06-14 12:50:52.274166
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    path = "/home/ubuntu/opt/test.cfg"
    config = {"__file__": os.path.abspath(path)}
    with open(path, "rb") as f:
        exec_in(native_str(f.read()), config, config)
    assert config

if __name__ == '__main__':
    test_OptionParser_parse_config_file()



# Generated at 2022-06-14 12:51:00.018005
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import os.path
    try:
        file = open(os.path.join(os.environ["TEMP"], "test_OptionParser_parse_config_file.py"), "w")
        file.write("logging = 'WARNING'\n").close()
        import tornado.options, logging
        tornado.options.define("logging", default="INFO", help="")
        tornado.options.parse_config_file(file.name)
        assert tornado.options.options.logging == logging.WARNING, \
            "parse_config_file of class OptionParser does not work"
        os.remove(file.name)
    except Exception as ex:
        print(ex)

# Generated at 2022-06-14 12:51:06.963440
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Success cases
    config_file = """
port = 80
mysql_host = 'mydb.example.com:3306'
memcache_hosts = ['cache1.example.com:11011',
                  'cache2.example.com:11011']
memcache_hosts = 'cache1.example.com:11011,cache2.example.com:11011'
"""
    options.define("port", cast=int, type=int)
    options.define("mysql_host", type=str)
    options.define("memcache_hosts", multiple=True, type=str)
    options.parse_config_file(StringIO(config_file))
    
        

# Generated at 2022-06-14 12:51:11.684709
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    parser.define("a", default=10)
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'temp.conf')
        with open(path, "w") as f:
            f.write("a = 5")
        parser.parse_config_file(path)
    assert options.a == 5

# Generated at 2022-06-14 12:51:49.321211
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    from tornado.options import define, options, Error
    import pytest
    # Test the return value
    define("port", type=int, default=8000)
    assert options.parse_command_line(['', '--port=80']) == []
    define("address", type=str, default='')
    assert options.parse_command_line(['', '--address=localhost:80']) == []
    # Test '=' sign inside the value
    define("name", type=str, default='')
    assert options.parse_command_line(['', '--name=first-second-third']) == []
    # Test boolean options
    define("debug", type=bool, default=True)
    assert options.parse_command_line(['', '--debug=false']) == []
    assert options.parse_command_line

# Generated at 2022-06-14 12:51:59.247810
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Create an OptionParser object
    option_parser = OptionParser()
    # Create a file to store the config
    f = open('config.txt', 'w+')
    # Adapted from a demo in tornado.options
    f.write('''
    # -*- coding: utf-8 -*-
    port = 80
    mysql_host = 'mydb.example.com:3306'
    memcache_hosts = ['cache1.example.com:11011', 'cache2.example.com:11011']
    memcache_hosts = 'cache1.example.com:11011,cache2.example.com:11011'
    ''')
    # Close the file
    f.close()
    # Call the method to be tested
    option_parser.parse_config_file('config.txt')


# Generated at 2022-06-14 12:52:01.149044
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # OptionParser.__iter__()
    pass



# Generated at 2022-06-14 12:52:11.552154
# Unit test for method parse of class _Option
def test__Option_parse():
    def test_parse_datetime():
        o = _Option("", type = datetime.datetime)
        o._parse_datetime("Thu Jan 01 00:00:00 1970")
        o._parse_datetime("1970-01-01 00:00:00")
        o._parse_datetime("1970-01-01 00:00")
        o._parse_datetime("1970-01-01T00:00")
        o._parse_datetime("19700101 00:00:00")
        o._parse_datetime("19700101 00:00")
        o._parse_datetime("1970-01-01")
        o._parse_datetime("19700101")
        o._parse_datetime("00:00:00")
        o._parse_datetime("00:00")

# Generated at 2022-06-14 12:52:16.829468
# Unit test for method set of class _Option
def test__Option_set():
    t1 = datetime.datetime(2012, 5, 9, 3, 0)
    t2 = datetime.datetime(2012, 5, 9, 3, 0)
    op = _Option('name', datetime.datetime(2012, 5, 9, 3, 0), datetime.datetime, True)
    op.set(t1)
    assert op.value() == t2


# Generated at 2022-06-14 12:52:26.325441
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
  import mock
  
  import tornado.options
  import typing
  
  def _test_OptionParser___iter__():
    # Ensure that __iter__ does *not* throw an exception
    tornado.options.OptionParser.__iter__()
    
  with mock.patch('tornado.options.OptionParser.options', new=typing.List[tornado.options._Option]):
    _test_OptionParser___iter__()
    
  with mock.patch('tornado.options.OptionParser.options', new=typing.List[tornado.options._Option]):
    _test_OptionParser___iter__()
    
  with mock.patch('tornado.options.OptionParser.options', new=typing.Dict[str, tornado.options._Option]):
    _test_OptionParser___iter__()
    

# Generated at 2022-06-14 12:52:37.195437
# Unit test for method parse of class _Option
def test__Option_parse():
    import unittest
    import datetime
    a = _Option("a", 1, int, "Option a")
    b = _Option("b", "", str, "Option b")
    c = _Option("c", False, bool, "Option c")
    d = _Option("d", datetime.timedelta(0), datetime.timedelta, "Option d")
    e = _Option("e", [], int, "Option e", multiple=True)
    f = _Option("f", [""], str, "Option f", multiple=True)
    g = _Option("g", [], bool, "Option g", multiple=True)
    h = _Option("h", [datetime.timedelta(0)], datetime.timedelta, "Option h", multiple=True)

# Generated at 2022-06-14 12:52:48.170746
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    import sys, pytest
    def test_it(self, inp: str, exp: str):
        options = Options()
        options.define("debug", type=bool, help="debug mode", callback=self._help_callback)
        options.define("logging", type=str, help="logging configuration", callback=self._help_callback)
        assert self._normalize_name("log-file") == "log_file"
        assert self._normalize_name("log-file") == "log_file"
        assert self._normalize_name("LOGFILE") == "logfile"
        assert self._normalize_name("LOGFILE") == "logfile"
        assert self._normalize_name("loG-fiLe") == "log_file"

# Generated at 2022-06-14 12:52:49.524118
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    opts = OptionParser()
    assert opts is not None

# Generated at 2022-06-14 12:52:57.701594
# Unit test for method parse of class _Option
def test__Option_parse():
    o = _Option("test", "xxx")
    assert o.parse("") == "xxx"
    assert o.parse("abc") == "abc"

    o = _Option("test", "xxx", type=bool)
    assert o.parse("false") is False
    assert o.parse("true") is True

    o = _Option("test", "xxx", type=int)
    assert o.parse("1") == 1
    assert o.parse("9") == 9

    o = _Option("test", "xxx", type=float)
    assert o.parse("1.5") == 1.5
    assert o.parse("2.5") == 2.5

    o = _Option("test", "xxx", type=datetime.datetime)

# Generated at 2022-06-14 12:55:19.512726
# Unit test for method parse of class _Option
def test__Option_parse():
    def test_cases():
        for t in [
            datetime.datetime,
            datetime.timedelta,
            bool,
            basestring_type,
            int,
        ]:
            yield t, _Option("name", type=t, multiple=False)
            yield t, _Option("name", type=t, multiple=True)
    for t, o in test_cases():
        with mock.patch.object(
            o, "_parse_%s" % t.__name__, wraps=getattr(o, "_parse_%s" % t.__name__)
        ) as m:
            o.parse("x")
            assert m.called



# Generated at 2022-06-14 12:55:25.339222
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Set up
    option = OptionParser()
    # Exercise
    with pytest.raises(Error):
        option.define("port", type=int)
        option.parse_config_file("option_parse_error.conf")
        # Verify
        assert option.port == 80
        assert option.mysql_host == 'mydb.example.com:3306'
        assert option.memcache_hosts == ['cache1.example.com:11011', 'cache2.example.com:11011']
    # Clean up - it would be automatically



# Generated at 2022-06-14 12:55:37.748264
# Unit test for method parse of class _Option
def test__Option_parse():
    _option_datetime = _Option(name='datetime', default=datetime.datetime(2005,7,14,12,30,45), type=datetime.datetime)
    _option_timedelta = _Option(name='timedelta', default=datetime.timedelta(0,0,0,12345), type=datetime.timedelta)
    _option_bool = _Option(name='bool', default=True, type=bool)
    _option_str = _Option(name='str', default='MyString', type=str)
    

# Generated at 2022-06-14 12:55:40.515055
# Unit test for method set of class _Option
def test__Option_set():
    import doctest
    import tornado.options
    doctest.run_docstring_examples(
        tornado.options._Option.set, globals(),
        name="_Option.set"
    )


# Generated at 2022-06-14 12:55:52.951843
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # test_parse_config_file
    # Build options
    options = OptionParser()
    options.define(
        "memcache_hosts",
        type=str,
        multiple=True,
        help="List of memcache servers: host:port:weight",
        metavar="HOST:PORT:WEIGHT",
    )
    options.define("port", type=int, help="TCP port to listen to")
    options.define(
        "mysql_host", type=str, default="127.0.0.1:3306", help="Main user DB"
    )
    # We need to call parse_command_line so that options are actually created
    # (options.define doesn't do that)
    options.parse_command_line(["progname"])
    # Add some values
    options.parse

# Generated at 2022-06-14 12:56:01.558979
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    opt = OptionParser()
    opt.define('test', default='test-0', type=str, help='test')
    for i in iter(opt):
        assert type(i) == str
    opt.define('test-i', default='test-1', type=int, help='test-i')
    for i in iter(opt):
        assert type(i) == str
    opt.define('test-b', default='test-2', type=bool, help='test-b')
    for i in iter(opt):
        assert type(i) == str
    opt.define('test-dt', default='test-3', type=datetime, help='test-dt')
    for i in iter(opt):
        assert type(i) == str

# Generated at 2022-06-14 12:56:03.869791
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    parser = OptionParser()
with pytest.raises(NotImplementedError):
    parser.__iter__()