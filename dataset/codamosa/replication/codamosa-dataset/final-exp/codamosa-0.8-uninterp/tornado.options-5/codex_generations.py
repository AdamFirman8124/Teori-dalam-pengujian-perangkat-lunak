

# Generated at 2022-06-14 12:46:25.791702
# Unit test for method parse of class _Option
def test__Option_parse():
    option = _Option('name', default=None, type=str, help=None, multiple=False, file_name=None, group_name=None, callback=None)
    assert option.parse(value='1') == '1'


# Generated at 2022-06-14 12:46:30.401177
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    from unittest.mock import patch
    from tornado.options import OptionParser, _Mockable
    import sys
    import os

    options = OptionParser()

    options.define("name", default="default", help="", type=str)
    # Use _Mockable in order to use the mock.patch()
    mockable = _Mockable(options)
    with patch.object(mockable, 'name', "mock"):
        assert options.name == "mock"
        mockable.name = "test"
        assert options.name == "test"
    assert options.name == "default"



# Generated at 2022-06-14 12:46:32.567445
# Unit test for method set of class _Option
def test__Option_set():
    __option = _Option('port', 80, int, 'port', 'PORT', False, 'file_name', 'group_name')
    __option.set(80)


# Generated at 2022-06-14 12:46:39.086528
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    optparser = OptionParser()
    optparser.define('name', default='name', help='name lixiaohui', multiple=True)
    
    optparser.define('password', default='password', help='password lixiaohui', multiple=False)
    
    # optparser._options: Dict[str, _Option]
    # _Option object will automatically be converted to _Option object when iterating
    for option in optparser:
        assert option.description() == 'name lixiaohui'
        break

# Generated at 2022-06-14 12:46:51.777411
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    import sys
    import io
    import unittest
    from tornado.options import OptionParser

    class _MockableTestCase(unittest.TestCase):
        def setUp(self):
            # setup the context of the testcase
            self.options = OptionParser()
            self.options.define('name', type=str, group='testcase')
            self.mockable_obj = _Mockable(self.options)

        def tearDown(self):
            # release the resource
            self.options = None
            self.mockable_obj = None

        def test__setattr__(self):
            # prepare the test context
            name = 'test_name'
            value = 'test_value'
            # the test code
            self.mockable_obj.__setattr__(name, value)
           

# Generated at 2022-06-14 12:46:54.136932
# Unit test for method parse of class _Option
def test__Option_parse():
    # Initialize option and test parse
    option = options._Option("name", type=str)
    assert option.parse("value") == "value"



# Generated at 2022-06-14 12:46:56.262632
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # OptionParser(self)
    option_parser_instance = OptionParser()


# Generated at 2022-06-14 12:46:57.786406
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    pass


# Generated at 2022-06-14 12:47:09.095710
# Unit test for method parse of class _Option
def test__Option_parse():
    """
    _Option.parse test
    """
    from datetimetest import _datetime_example

    # 有缺省时间值的配置变量
    option = _Option(name='name', default=_datetime_example, type=datetime.datetime, help='help')

    # 在单个配置变量处理时调用parse
    option.parse('2015-04-01 12:30:00')
    assert option.value() == _datetime_example

    # 在多个配置变量处理时调用parse
    option.multiple = True

# Generated at 2022-06-14 12:47:14.389738
# Unit test for method set of class _Option
def test__Option_set():
    Option = _Option('option', type = int, default = 10)
    Option.set(20)
    assert Option.value() == 20
    assert Option._value == 20
    try:
        Option.set(10.5)
    except Exception as e:
        assert isinstance(e, Error)


# Generated at 2022-06-14 12:47:50.893235
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    options = _Mockable(None)
    setattr(options, 'name', 'value')
    assert options._originals['name'] == 'value'


# Generated at 2022-06-14 12:47:53.169043
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    # Check the OptionParser method group_dict
    '''
    Check the OptionParser method group_dict
    '''
    parser = OptionParser()
    parser.define('name', type=str, help='', metavar='', multiple=False, group='name', callback=None)
    result = parser.group_dict('name')
    assert isinstance(result, dict) and result == {}, "Test failed."



# Generated at 2022-06-14 12:48:01.855703
# Unit test for method parse of class _Option
def test__Option_parse():
    def callback(value: Any) -> None:
        print("callback")

    option = _Option("name", None, 'int')
    option.parse("1")

    option = _Option("name", None, 'int', callback=callback)
    option.parse("1")

    option = _Option("name", None, 'bool')
    option.parse("1")
    option.parse("0")

    option = _Option("name", None, 'bool', callback=callback)
    option.parse("1")

    option = _Option("name", None, 'timedelta')
    option.parse("1us")

    option = _Option("name", None, 'timedelta', callback=callback)
    option.parse("1min")

    option = _Option("name", None, 'datetime')

# Generated at 2022-06-14 12:48:07.540529
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Initialization
    parser = OptionParser(None, None)

    config = {"__file__": os.path.abspath("./test/test_config_file.py")}

    # Syntax error
    with open("./test/test_config_file.py", "rb") as f:
        with pytest.raises(SyntaxError):
            exec_in(native_str(f.read()), config, config)
    # parse_config_file
    with open("./test/test_config_file.py", "rb") as f:
        assert parser.parse_config_file("./test/test_config_file.py") is None

# Generated at 2022-06-14 12:48:08.933264
# Unit test for method set of class _Option
def test__Option_set():
    # pass
    pass


# Generated at 2022-06-14 12:48:11.223275
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    import mock
    from tornado.options import OptionParser, Error

    # OptionParser.__iter__() -> iterator of (key, value) pairs

    result = OptionParser()._options
    expected = {}

    assert result == expected


# Generated at 2022-06-14 12:48:13.466355
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
  r = 'a'
  obj = OptionParser()
  res = obj.__iter__()
  return res

# Generated at 2022-06-14 12:48:22.417096
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    out = []
    class Options:
        pass
    options = Options()
    
    op = OptionParser()
    op.define("name", default="world", callback=lambda s: out.append(s))
    op.define("number", type=int, default=123)

    op.parse_config_file("tests/options.cfg")
    assert options.name == "world"
    assert out == ["Bob"]
    assert options.number == 123

    op.parse_config_file("tests/options2.cfg")
    assert options.name == "Zaphod"
    assert out == ["Bob", "Zaphod"]
    assert options.number == 1024


# Generated at 2022-06-14 12:48:35.992449
# Unit test for method group_dict of class OptionParser

# Generated at 2022-06-14 12:48:39.385703
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    options = OptionParser()
    options.define('name', default='John Doe')
    mock = _Mockable(options)
    setattr(mock, 'name', 'Jane Doe')
    assert options.name == 'Jane Doe'

test__Mockable___setattr__()



# Generated at 2022-06-14 12:49:06.866397
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
  parser = OptionParser()
  parser.define("a", type=int)
  parser.define("b", type=float, default=0.5)
  parser.parse_config_file("Example1.txt")
  assert parser.a == 3
  assert parser.b == 11.0
  parser.parse_config_file("Example2.txt")
  assert parser.a == 20
  assert parser.b == 4.2
# Test for method parse_config_file of class OptionParser
# Test for our own example code.
from tornado.testing import AsyncTestCase, gen_test
from tornado.ioloop import IOLoop
from tornado.options import options

# Generated at 2022-06-14 12:49:10.553483
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    parser = OptionParser()
    parser.define("x", default=1, type=int)
    parser.define("y", default=2, type=str)
    assert len(list(parser)) == 2
    assert list(parser)[1].name == "y"


# Generated at 2022-06-14 12:49:11.311330
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    pass



# Generated at 2022-06-14 12:49:17.963140
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # init options and arguments
    optionparser = OptionParser()
    optionparser.define('s', type=str, help='s is a str')
    optionparser.define('i', type=int, help='i is a int')
    optionparser.define('f', type=float, help='f is a float')
    optionparser.define('b', type=bool, help='b is a bool')
    parser_args = []
    # _parse_config_file(path, final=True)
    # path is str
    # path is valid
    # path is valid and final is Ture
    optionparser.parse_config_file("test_optionparser_parse_config_file.py")
    assert optionparser.s == "this is a str"
    assert optionparser.i == 1024
    assert optionparser.f == 3.14


# Generated at 2022-06-14 12:49:20.604602
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    parser = OptionParser()
    with pytest.raises(Error):
        parser.parse_command_line([""])

    parser.define("name", default="default")
    assert parser.name == "default"

    parser.parse_command_line(["--name=command"])
    assert parser.name == "command"



# Generated at 2022-06-14 12:49:23.279009
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    d = {'x': 'y'}
    o = OptionParser()
    o._options = d
    assert o.__iter__()  == d.__iter__()

# Generated at 2022-06-14 12:49:31.017891
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    parser = OptionParser()
    parser.define("foo", "bar")
    assert parser.parse_command_line(["--foo", "baz"]) == []
    assert parser.foo == "baz"
    assert parser.parse_command_line(["--foo=quux", "--foo=spam"]) == []
    assert parser.foo == "spam"
    assert parser.parse_command_line([
        "--foo=spam", "--foo", "quux", "--foo=spam", "--foo=quux"
    ]) == []
    assert parser.foo == "quux"
    assert parser.parse_command_line(["--foo", "--foo=1"]) == []
    assert parser.foo == "--foo=1"
    return



# Generated at 2022-06-14 12:49:33.359504
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    test_parser = _OptionParser()
    test_parser.define('name', default='', help='some help')
    test_parser.parse_config_file('test.ini', final=True)
    assert test_parser.name == 'test_name'

# Generated at 2022-06-14 12:49:36.750482
# Unit test for method set of class _Option
def test__Option_set():
    _Option_instance2_ = _Option("name",type=str,default=None)
    _Option_instance2_.set('abc')
    assert _Option_instance2_.value() == 'abc'


# Generated at 2022-06-14 12:49:43.315235
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    p = OptionParser()
    p.add_parse_callback(lambda _: print("Hello!"))
    p.define("name", default="foo", type=str, help="name", metavar="NAME", multiple=False, group="application")
    p.parse_command_line(["test", "--name"])
    assert p.options["name"] == "foo"
    # p.run_parse_callbacks()

# Generated at 2022-06-14 12:50:01.025644
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    from io import StringIO
    from unittest import mock, TestCase
    from tornado.options import define, options, parse_command_line

    def _test(group, expected):
        # type: (str, Dict[str, Any]) -> None
        actual = options.group_dict(group)
        assert actual == expected, (actual, expected)

    class TestCase(TestCase):
        def setUp(self):
            # type: () -> None
            self.io = StringIO()
            self.mock = mock.patch("sys.stdout", self.io)
            self.mock.start()
            parse_command_line([])
            define("a", group="foo")
            define("b", group="bar")
            define("c", 1, group="foo")

# Generated at 2022-06-14 12:50:11.323272
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    grp1 = 'group1'
    grp2 = 'group2'
    define('name', type=str, group=grp1)
    define('age', type=int, group=grp2)
    define('dob', type= datetime.date, group=grp2)
    
    parse_command_line()
    
    group_dict_grp1 = options.group_dict(grp1)
    group_dict_grp2 = options.group_dict(grp2)
    
    assert len(group_dict_grp1) == 1
    assert len(group_dict_grp2) == 2
    
    assert 'name' in group_dict_grp1
    assert 'age' in group_dict_grp2
    assert 'dob' in group_dict_grp

# Generated at 2022-06-14 12:50:14.633128
# Unit test for method set of class _Option
def test__Option_set():
    from .options import _Option
    my_option = _Option("test", type=int)
    # Test for normal value
    my_option.set(5)
    assert my_option.value() == 5
    # Test for negative value
    my_option.set(-5)
    assert my_option.value() == -5
    # Test for type error
    with pytest.raises(tornado.options.Error):
        my_option.set("5")

# Generated at 2022-06-14 12:50:18.200924
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    options = OptionParser()
    options.define("config", type=str, help="path to config file", callback = lambda path: parse_config_file(path, final=False))
    path = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "test_config.conf")
    options.parse_config_file(path, True)
    assert options.config == path
    #options.parse_config_file(path, True)


# Generated at 2022-06-14 12:50:24.174223
# Unit test for method parse of class _Option
def test__Option_parse():
    def test_parse(option, value, expected):
        return True
    option = _Option('name', default=None, type=None, help='', metavar='', multiple=None, file_name=None, group_name=None, callback=None)
    value = ""
    expected = ""
    test_parse(option, value, expected)



# Generated at 2022-06-14 12:50:36.724106
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # You can always use 'assert_equal' to check the equality of the result with expect value.
    # You can always use 'assert_true' or 'assert_false' to check the Boolean value.
    # You can always use 'assert_raises' to check raise error.
    # You can always use 'len' to get the length of the content.
    from tornado.options import Options, Error
    opt = Options()
    with open("config.txt", "w") as f:
        f.write("port = 80\n")
        f.write("mysql_host = 'mydb.example.com:3306'\n")
        f.write("memcache_hosts = ['cache1.example.com:11011','cache2.example.com:11011']\n")

# Generated at 2022-06-14 12:50:43.569431
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import unittest.mock as mock
    import os.path
    import sys
    import io

    f = io.StringIO()
    with mock.patch.object(sys, "stdout", f):
        options = OptionParser()
        options.define("option", default=False)
        options.parse_config_file("tests/options_test_file")
        assert options.option
        f.seek(0)
        assert f.read() == "true\n"


# Generated at 2022-06-14 12:50:54.898799
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import sys
    import datetime
    from tornado.options import define, options, Error, OptionParser
    define('name', default=None, type=str, help='desc')
    define('now', default=None, type=int, help='desc')
    define('date', default=None, type=datetime.datetime, help='desc')
    define('list', default=None, type=list, help='desc')
    define('bool', default=None, type=bool, group='boolean', help='desc')
    define('string', default=None, type=str, group='boolean', help='desc')
    define('float', default=None, type=float, group='float', help='desc')
    define('int', default=None, type=int, group='float', help='desc')

# Generated at 2022-06-14 12:50:57.586159
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    class Test:
        def __init__(self):
            self.args = []
        def __setattr__(self,name, value):
            self.args.append((name, value))
    option = _Mockable(Test())
    option.__setattr__("foo", "bar")
    option.__setattr__("foo", "foobar")
    assert option._originals["foo"] == "bar"
    assert option._options.args == [("foo", "bar")]


# Generated at 2022-06-14 12:50:58.532586
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    pass



# Generated at 2022-06-14 12:51:28.804713
# Unit test for method set of class _Option
def test__Option_set():
    name = "test__Option_set.testname"
    default = "test__Option_set.testdefault"
    type_ = type(default)
    help = "test__Option_set.testhelp"
    metavar = "test__Option_set.testmetavar"
    multiple = True
    file_name = "test__Option_set.testfile_name"
    group_name = "test__Option_set.testgroup_name"
    callback = None
    option = _Option(name, default, type_, help, metavar, multiple, file_name, group_name, callback)
    set_value = "test__Option_set.testset_value"
    option.set(set_value)
    assert(option._value == set_value)



# Generated at 2022-06-14 12:51:39.068845
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import sys
    import os
    from io import StringIO
    from pprint import pprint
    import unittest
    import traceback
    from tornado.options import OptionParser, Error, options
    try:
        options.parse_config_file("../test/test_options.py", final=True)
        assert options.name == "peter"
        assert options.age == 30
    except Exception as e:
        traceback.print_exc()
        print(e.__str__())


if __name__ == "__main__":
    test_OptionParser_parse_config_file()

# Generated at 2022-06-14 12:51:51.047976
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    parser.define("foo", type=int, default=1, help="foo")
    parser.define("bar", type=int, default=2, help="bar")
    parser.define("baz", type=int, default=3, help="baz")
    parser.parse_config_file(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "test_options_config.py",
        )
    )
    #def parse_config_file(self, path: str, final: bool = True) -> None:
    assert parser.foo == 10
    assert parser.bar == 20
    assert parser.baz == 30
    parser.define("baz", type=int, default=4, help="baz")

# Generated at 2022-06-14 12:51:59.766164
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # An option with default value `None`
    define('myoption', type=int, default=None)
    # A config file with content of `myoption = 99`
    test_config_file_path = os.path.join('options_test.conf')
    with open(test_config_file_path, 'w') as f:
        f.write('myoption = 99')
    # Parse the config file
    options.parse_config_file(test_config_file_path, final=True)
    # Test whether the option is successfully set
    assert options.myoption == 99
    # Clear the state
    options.clear()
    # Delete the test file
    os.remove(test_config_file_path)


# Note: this is a subclass of OptionParser to avoid breaking existing
# unit tests that may be relying on

# Generated at 2022-06-14 12:52:05.014476
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    def helper(path, final = True):
        opt = OptionParser()
        opt.define("port")
        opt.define("mysql_host")
        opt.define("memcache_hosts", multiple = True)
        opt.parse_config_file(path)

    return helper


# Generated at 2022-06-14 12:52:15.010091
# Unit test for method set of class _Option
def test__Option_set():
    o = _Option("name", type=int)
    o.set(1)
    o.set(2)
    assert (o.value(), o._value) == (2, 2)
    o = _Option("name", type=int)
    o.set(1)
    assert (o.value(), o._value) == (1, 1)
    o = _Option("name", type=int)
    o.set(2)
    assert (o.value(), o._value) == (2, 2)
    o = _Option("name", type=int)
    o.set(2)
    assert (o.value(), o._value) == (2, 2)
    o = _Option("name", type=int)
    o.set(2)
    o.set(2)

# Generated at 2022-06-14 12:52:17.810885
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
	print('unit test for method test__Mockable___setattr__ in class _Mockable()')
	print('TODO')



# Generated at 2022-06-14 12:52:24.714893
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    # Unit tests do not use $HOME, so override that
    with TemporaryDirectory() as tmpdir:
        os.environ["HOME"] = tmpdir
        with patch.dict(
            os.environ,
            {
                "HOME": tmpdir,
                "HOMEPATH": tmpdir,
                "USERPROFILE": tmpdir,
            },
            clear=True,
        ), patch.object(
            sys,
            "platform",
            "linux2",
        ):
            options = OptionParser()
            mockable = options.mockable()
            assert options.name == "foo"
            setattr(mockable, "name", "bar")
            assert options.name == "bar"
            delattr(mockable, "name")
            assert options.name == "foo"

# Generated at 2022-06-14 12:52:36.240119
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import io
    import os
    from tornado.options import define, options

    define('name', type=str)
    define('port', type=int)
    define('array', type=([int]))
    _, fn = mkstemp()

# Generated at 2022-06-14 12:52:47.213130
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import tempfile
    options = OptionParser()
    options.define("name", default="world", help="world", group="group", multiple=True,
                   callback=None, type=str, metavar="metavar")
    options.define("world", default="world", help="world", group="group", multiple=True,
                   callback=None, type=str, metavar="metavar")
    temp = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 12:53:24.142874
# Unit test for method parse of class _Option
def test__Option_parse():
    import doctest
    o = _Option(1)
    doctest.run_docstring_examples(o.parse, globals(), verbose=True)


# Generated at 2022-06-14 12:53:34.006369
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    with patch.object(sys, 'argv', ['prog', '--foo', '1', '--bar', '2']):
        define('foo', type=int, group='group1')
        define('bar', type=int, group='group2')
        define('baz', type=int)
        parse_command_line()
        assert options.group_dict('group1') == {'foo': 1}
        assert options.group_dict('group2') == {'bar': 2}
        assert options.group_dict('unknown') == {}
        assert options.group_dict(None) == {'foo': 1, 'bar': 2, 'baz': None}


# Generated at 2022-06-14 12:53:44.318897
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    def get_options():
        class A:
            debug = 0

        class B:
            a = A()
            host = 'localhost'
            port = 8080
            path = './'
            mysql_host = None
            memcache_hosts = []

        return B()
    options = get_options()
    OptionParser().parse_config_file(path=os.path.join(root_path, 'test_data/options.cfg'), final=True)
    field_names = [field for field in dir(options) if not callable(getattr(options, field)) and not field.startswith("__")]
    for field_name in field_names:
        assert getattr(options, field_name) is getattr(get_options(), field_name)


# Generated at 2022-06-14 12:53:45.753214
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    assert _Mockable.__setattr__.__doc__ is not None


# Generated at 2022-06-14 12:53:46.705817
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    assert True

# Generated at 2022-06-14 12:53:57.043249
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    # sample parse_command_line: command line invalid
    import sys
    from tornado.options import OptionParser
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.httputil import HTTPHeaders
    from tornado.http1connection import HTTP1ServerConnection
    from tornado.tcpserver import TCPServer
    from tornado.httpserver import HTTPServer
    from tornado.escape import to_unicode, utf8
    from tornado.httputil import _parse_header
    import unittest.mock as mock
    def test_parse_command_line():
        options = OptionParser()
        options.define("a", type=int)
        options.define("b", type=str)

# Generated at 2022-06-14 12:54:06.922756
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    import sys
    from numpy.testing import assert_raises
    # test when sys.argv is empty
    sys.argv = []
    # TODO: how to test the exit system call
    #assert_raises(SystemExit, options.parse_command_line)
    # test when the option name cannot be found in the _options
    sys.argv = ["--name=value"]
    parser = OptionParser()
    assert_raises(Error, parser.parse_command_line)
    # test when the option name is found in _options
    parser.define("name", default="default")
    parser.parse_command_line()
    assert parser.name == "value"
    # test when the option type is not bool and option value is not given
    parser.define("port", type=int)

# Generated at 2022-06-14 12:54:17.100827
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    from unittest.mock import patch
    parser = OptionParser()
    parser.define("name", type=str, help="Name", multiple=True)
    parser.define("age", type=int, help="Age")

    parser.parse_command_line(['--name=Bart,Lisa', '--age=8'])

    mockable = parser.mockable()
    assert mockable.name == ['Bart', 'Lisa']

    with patch.object(mockable, 'name', ['Maggie', 'Homer']):
        assert parser.name == ['Maggie', 'Homer']

    with patch.object(mockable, 'name', 'Homer'):
        assert parser.name == 'Homer'

    assert parser.name == ['Bart', 'Lisa']


# Generated at 2022-06-14 12:54:24.675899
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    parser = OptionParser()
    path = ''
    final = True
    with pytest.raises(Error) as excinfo:
        parser.parse_config_file(path, final)
    print(excinfo)
    assert str(excinfo.value) == "Config file not found: ''"
    path = './not_existed_config_file.ini'
    with pytest.raises(Error) as excinfo:
        parser.parse_config_file(path, final)
    print(excinfo)
    assert str(excinfo.value) == "Config file not found: './not_existed_config_file.ini'"

    path = './not_existed_config_file.ini'

# Generated at 2022-06-14 12:54:30.882028
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    opts = OptionParser()
    opts.define("name", type=str, default="zhang", help='username')
    opts.define("age", default=22, help='age of the user')
    opts.parse_config_file('/Users/zhang/study/python/tornado/options_config.conf')
    print(opts.name) # zhaoliu
    print(opts.age) # 22