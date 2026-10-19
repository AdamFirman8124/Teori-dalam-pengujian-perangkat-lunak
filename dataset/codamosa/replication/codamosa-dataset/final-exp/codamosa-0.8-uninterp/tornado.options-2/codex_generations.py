

# Generated at 2022-06-14 12:46:54.096598
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option("hello",str,"newstring")
    try:
        option.set("oldstring")
    except Error as error:
        assert error.message == "Option 'hello' is required to be a newstring (str given)"


# Generated at 2022-06-14 12:47:06.911508
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    from tornado.options import OptionParser
    from tornado.util import exec_in
    from types import ModuleType
    import unittest.mock
    import sys
    import types
    import unittest
    class OptionsMockableTestCase(unittest.TestCase):
        def test_mock_attr(self):
            # 'name' should be mocked after the with statement
            class M(object):
                pass
            options = OptionParser()
            options.define('name', default='', type=str)
            obj = options.mockable()
            options.name = 'foo'
            self.assertEqual(options.name, 'foo')
            self.assertFalse(hasattr(obj, 'name'))

# Generated at 2022-06-14 12:47:18.241572
# Unit test for method set of class _Option
def test__Option_set():
    from tornado.options import OptionParser
    op = OptionParser()
    # initialization
    op.add_option("--port", type=int, default=8080)
    op.add_option("a", type=float, default=1.0)
    op.add_option("b", type=float, default=None, multiple=True)
    op.add_option("c", type=int, default=None, multiple=True)
    op.add_option("d", type=int, default=None, multiple=False)
    op.add_option("e", type=float, default=None, multiple=False)
    op.add_option("f", type=int, default=None, multiple=True)
    # test
    op._options["port"].set(80)

# Generated at 2022-06-14 12:47:29.170898
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # define('foo', type=str)
    # define('bar', type=int, multiple=True)
    # define('baz', type=bool)
    # define('qux', type=float)
    foo_name = 'foo'
    foo_type = str
    foo_default = None
    foo_help = None
    foo_metavar = None
    foo_multiple = False
    foo_group = None
    foo_callback = None
    foo_option = define(foo_name, foo_type, foo_default, foo_help, foo_metavar,
        foo_multiple, foo_group, foo_callback)

    bar_name = 'bar'
    bar_type = int
    bar_default = None
    bar_help = None
    bar_metavar = None
    bar_multiple = True

# Generated at 2022-06-14 12:47:39.116908
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    text_str = 'port = 80\n' + \
            'mysql_host = \'mydb.example.com:3306\'\n' + \
            'memcache_hosts = [\'cache1.example.com:11011\',\n' + \
            '              \'cache2.example.com:11011\']\n' + \
            'memcache_hosts = \'cache1.example.com:11011,cache2.example.com:11011\''
    file_path = 'test_option_config.txt'
    with open(file_path, 'w') as f:
        f.write(text_str)
    def clean():
        os.remove(file_path)

    parser = OptionParser()

# Generated at 2022-06-14 12:47:52.140478
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    from io import StringIO
    from tornado.options import define, options, OptionParser
    from tests.util import strip_python_stderr

    class FooModule(object):
        pass
    foo = FooModule()

    with NamedTemporaryFile("wt") as f:
        f.write("name = 'bar'")
        f.flush()
        define("name", default="foo")
        assert options.name == "foo"
        options.parse_config_file(f.name)
        assert options.name == "bar"

    with NamedTemporaryFile("wt") as f:
        f.write("name = 'bar'")
        f.flush()
        define("name", default="foo")
        assert options.name == "foo"
        options.parse_config_file(f.name)
        assert options

# Generated at 2022-06-14 12:48:01.293792
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    from datetime import timedelta
    from tornado.options import define, Error
    define("foo", type=float)
    define("bar", default=4, type=int)
    define("baz", default=[1, 2, 3], type=list)
    define("quux", type=timedelta)
    define("duh", default=[], multiple=True)
    define("paf", type=list, multiple=True)
    define("password", type=str, help=None, metavar="PASSWORD")
    define("server")
    options.parse_config_file("tests/options_test_data/parse_config_file_data.py")

    assert options.foo == 5.25
    assert options.bar == 12
    assert options.baz == ["1", "2", "3", "4", "5"]

# Generated at 2022-06-14 12:48:02.460892
# Unit test for method parse of class _Option
def test__Option_parse():
    pass
    # TODO Add tests

# Generated at 2022-06-14 12:48:13.685872
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    import unittest
    import unittest.mock
    class _MockableTest(unittest.TestCase):
        def test___setattr__2(self):
            from tornado.options import _Mockable
            from tornado.options import OptionParser
            options = OptionParser()
            mockable = _Mockable(options)
            with unittest.mock.patch.object(mockable, 'name', value):
                assert options.name == value
        def test___setattr__1(self):
            from tornado.options import _Mockable
            from tornado.options import OptionParser
            options = OptionParser()
            mockable = _Mockable(options)
            with unittest.mock.patch.object(mockable, 'name', value):
                assert options.name == value

# Generated at 2022-06-14 12:48:15.568790
# Unit test for method print_help of class OptionParser
def test_OptionParser_print_help():
    parser = OptionParser()
    parser.print_help()

# Generated at 2022-06-14 12:48:34.421952
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option(name="name", type=basestring_type, default=None)
    assert option.value() == None
    option.set(None)
    assert option.value() == None
    option.set("value")
    assert option.value() == "value"



# Generated at 2022-06-14 12:48:38.726271
# Unit test for method __setattr__ of class OptionParser
def test_OptionParser___setattr__():
    import tornado.options
    instance = tornado.options.OptionParser()
    object = object()
    name = '_OptionParser__options'
    instance.__setattr__(name, object)
    assert instance._OptionParser__options == object

# Generated at 2022-06-14 12:48:47.433782
# Unit test for method set of class _Option
def test__Option_set():
    _o = _Option('_o', default=None, type=None, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
    assert _o.value() == None
    _o.multiple = True
    _o.set([None])
    _o.multiple = False
    _o.set(None)
    assert _o.value() == None
    with pytest.raises(Error, match="must not be None"):
        _o = _Option('_o', default=None, type=None, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
        _o.set(None)

# Generated at 2022-06-14 12:48:54.001723
# Unit test for method print_help of class OptionParser
def test_OptionParser_print_help():
    import sys
    import StringIO
    sys.stdout = StringIO.StringIO()
    from tornado.options import options, define
    define("foo", type=str, help="FOO")
    define("bar", type=bool, help="BAR")
    define("baz", type=str, default="noone", help="BAZ")
    options.parse_config_file("config.py")
    options.print_help()
    print(sys.stdout.getvalue())
    assert sys.stdout.getvalue() == """Usage: test_OptionParser_print_help.py [OPTIONS]\n\nOptions:\n\n  --foo=METAVAR   FOO\n  --bar           BAR\n  --baz=METAVAR   BAZ (default noone)\n\n"""
    
# Unit

# Generated at 2022-06-14 12:48:59.392049
# Unit test for method set of class _Option
def test__Option_set():
    x = _Option('x', type=int)
    x.set('1')
    assert x.value() == 1
    x.set('2')
    assert x.value() == 2
    try:
        x.set('a')
    except Error:
        pass


# Generated at 2022-06-14 12:49:05.737913
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    options = Options()
    options.define("name", default=None, type=str)
    
    # Test for correct results
    options.parse_command_line(["--name=arg1"])
    assert options.name == "arg1"

    # Test for incorrect results
    options.parse_command_line(["--name_arg1"])
    assert options.name == "arg1"   

# Generated at 2022-06-14 12:49:09.444193
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    build_path = os.path.join(os.path.dirname(__file__), "sample.cfg")
    parser.parse_config_file(build_path, final=False)
    assert parser.options.application == {}



# Generated at 2022-06-14 12:49:16.829032
# Unit test for method set of class _Option
def test__Option_set():
    # Test for _Option.set
    for test_num,(test_case1, test_case2, test_case3, test_case4, test_case5, test_case6, test_case7, test_case8, test_case9, test_case10, test_case11, test_case12, test_case13) in enumerate(itertools.product(
            [False],
            [False],
            [False],
            [None],
            [None],
            [None],
            [None],
            [None],
            [None],
            [False],
            [True],
            [True],
            [True],
        )):
        print("test__Option_set", test_num)
        # setup

# Generated at 2022-06-14 12:49:25.451942
# Unit test for method parse of class _Option
def test__Option_parse():
    class Option1(_Option):
        def __init__(self, name, default, type, help, metavar, multiple, file_name, group_name, callback):
            super(Option1,self).__init__(name, default, type, help, metavar, multiple, file_name, group_name, callback)
            
        def parse(self, value: str) -> Any:
            return 1
    o = Option1('name', None, None, None, None, False, None, None , None)
    rlt = o.parse('value')
    assert rlt == 1


# Generated at 2022-06-14 12:49:37.788948
# Unit test for method parse of class _Option
def test__Option_parse():
    if __name__ == '__main__':
        option_a = _Option("a", default=None, type=int, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
        # for type = int
        assert option_a.parse("1") == 1
        option_b = _Option("b", default=None, type=int, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
        # for type = int
        assert option_b.parse("1") == 1
        assert option_b.parse("2") == 2


# Generated at 2022-06-14 12:51:05.522890
# Unit test for method parse of class _Option
def test__Option_parse():
    import doctest
    from tornado.options import _Option
    print(_Option.__init__.__doc__)
    print(_Option.parse.__doc__)
    doctest.run_docstring_examples(_Option.parse, globals())


# Generated at 2022-06-14 12:51:18.085925
# Unit test for method parse of class _Option
def test__Option_parse():
    args = "jojo,jojo"
    o = _Option(name = "jojo", default = None, type = list, help = None, metavar = None, multiple = True, file_name = None, group_name = None, callback = None)
    output = ['jojo', 'jojo']
    assert o.parse(args) == output, "The output should be 'jojo,jojo'"
    
    args = "jojo:jojo"
    output = [1, 0]
    assert o.parse(args) == output, "The output should be 'jojo:jojo'"
    
    args = "jojo:jojo"

# Generated at 2022-06-14 12:51:21.053704
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option(name='test', multiple=True)
    #option.set(['test'])
    option.set([None, 'test', None])


# Generated at 2022-06-14 12:51:25.285672
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    options.define('port', type=int, help='port to listen on', default=8000)
    options.define('mysql_host', type=str, help='mysql host')
    options.define('memcache_hosts', type=str, multiple=True, help='memcache hosts')
    print(options.as_dict())
    options.parse_config_file('options_config.py')
    print(options.as_dict())
    assert True


# Generated at 2022-06-14 12:51:31.891465
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    if sys.version_info[:2] == (2, 7):
        import mock
        with mock.patch.object(
            Options, "__setattr__", side_effect=Options.__setattr__
        ):
            opt = Options()
            opt.define("name", default="foo")
            opt.parse_config_file(
                os.path.join(os.path.dirname(__file__), "options_test_config.py")
            )
            assert opt.name == "bar"

# Generated at 2022-06-14 12:51:33.551507
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    pass



# Generated at 2022-06-14 12:51:45.476836
# Unit test for method parse of class _Option
def test__Option_parse():
    op = _Option("foo", help=None, metavar=None, callback=None)
    assert op.parse("1") == 1
    assert op.parse("2") == 2, "integer only parse once"

    op = _Option("foo", type=str, default=None, help=None, metavar=None, callback=None)
    assert op.parse("'bar'") == "'bar'"
    
    op = _Option("foo", type=datetime.timedelta, default=None, help=None, metavar=None, callback=None)
    assert op.parse("1s") == datetime.timedelta(seconds=1)
    assert op.parse("1sec") == datetime.timedelta(seconds=1)

# Generated at 2022-06-14 12:51:49.695431
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option('port', 80, int, 'port number', group_name='', file_name='config.py')
    option.set(80)
    assert option.value() == 80

    option.set(list([1, 2, 3]))
    assert option.value() == [1, 2, 3]


# Generated at 2022-06-14 12:51:59.662463
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    options = OptionParser()
    with pytest.raises(AttributeError):
        options._parse_callbacks
    with pytest.raises(AttributeError):
        options._options
    with pytest.raises(AttributeError):
        options._normalize_name
    options.mockable()
    options.print_help()
    options.group_dict(group="")
    options.as_dict()
    options.define(name="name", default=None, type=None, help=None, metavar=None, multiple=False, group=None, callback=None)
    options.parse_config_file(path="")
    options.add_parse_callback(callback=None)
    options.run_parse_callbacks()
    options.parse_command_line(args=None, final=True)
    options.groups

# Generated at 2022-06-14 12:52:10.547139
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Arrange
    parser = OptionParser()
    parser.define("string_value", str)
    parser.define("float_value", float)
    parser.define("int_value", int)
    parser.define("bool_value", bool)

    with tempfile.NamedTemporaryFile(mode="w+") as f:
        f.write(textwrap.dedent(
            """
            float_value = 1.5
            int_value = 1
            bool_value = true
            string_value = "abc"
            """
        ))
        f.flush()
        
        # Act
        parser.parse_config_file(f.name)

        # Assert
        assert parser.float_value == 1.5
        assert parser.int_value == 1
        assert parser.bool_value
        assert parser.string

# Generated at 2022-06-14 12:55:24.625610
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    parser.define("arg1", type=str, required=True)
    parser.define("arg2", type=int, required=True)
    parser.define("arg3", type=float, required=True)
    parser.define("arg4", type=bool, required=True)
    parser.define("arg5", type=list, required=True)
    parser.define("arg6", type=dict, required=True)
    filename = os.path.abspath("test/test_options.py")
    parser.parse_config_file(filename)
    assert parser.arg1 == "test_arg1"
    assert parser.arg2 == 2
    assert parser.arg3 == 3.0
    assert parser.arg4 == True
    assert parser.arg5 == [11, 22, 33]


# Generated at 2022-06-14 12:55:25.145606
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    pass



# Generated at 2022-06-14 12:55:37.419336
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    results = []
    with open("myconfig.conf","w") as f:
        f.write("port = 80\n")
        f.write("mysql_host = 'mydb.example.com:3306'\n")
        f.write("mysql_host = 'cache1.example.com:11011'\n")
        f.write("mysql_host = 'cache2.example.com:11011'\n")
    path = os.path.abspath(os.path.join(os.getcwd(), "myconfig.conf"))
    define("port", type=type(5))
    define("mysql_host",type=type('a'))
    try:
        parse_config_file(path)
    except Error as e:
        results.append(str(e))

# Generated at 2022-06-14 12:55:44.561651
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():

    class DummyOptionParser(OptionParser):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name = ""
            self.default = ""

        def set(self, value):
            self.name = value

        def parse(self, value):
            self.default = value

    # Create a dummy OptionParser object and set some options.
    optionparser = DummyOptionParser()
    optionparser.define(
        "port", type=int, default=80, help="server port", group="server"
    )
    optionparser.define(
        "mysql_host", default="mydb.example.com:3306", help="mysql host", group="db"
    )

# Generated at 2022-06-14 12:55:52.155725
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    parser = OptionParser()
    define = parser.define

    define('name', type=str, help='help message', default='John')

    assert len(parser._options) == 1
    it = iter(parser)

    # Next method of OptionParser iterator returns an Option object
    assert next(it).name == 'name'

    # OptionParser iterator stops when no more elements available
    with pytest.raises(StopIteration):
        next(it)


# Generated at 2022-06-14 12:55:55.472191
# Unit test for method parse of class _Option
def test__Option_parse():
    import datetime
    op = _Option(name='', default=None, type=datetime.timedelta, help=None, metavar=None, multiple=True, file_name=None, group_name=None)
    result = op.parse("  5  minutes  ")
    assert 300.0 == result.total_seconds()
