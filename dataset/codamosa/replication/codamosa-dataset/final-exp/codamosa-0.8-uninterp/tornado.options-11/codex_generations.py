

# Generated at 2022-06-14 12:46:21.083562
# Unit test for method set of class _Option
def test__Option_set():
    from tornado.options import _Option
    option=_Option()
    assert option is not None

# Generated at 2022-06-14 12:46:26.968863
# Unit test for method parse of class _Option
def test__Option_parse():
    from datetime import datetime
    from datetime import timedelta   
    # test case for parse type int
    test_option = _Option("test_option",1,int,"test option",'metavar',False,'file_name',group_name=None,callback=None)
    assert test_option.parse("5") == 5,"int test fail"
    # test case for parse type float
    test_option = _Option("test_option",1.0,float,"test option",'metavar',False,'file_name',group_name=None,callback=None)
    assert test_option.parse("5.5") == 5.5,"float test fail"
    # test case for parse type str

# Generated at 2022-06-14 12:46:37.509025
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    import unittest
import time

# Generated at 2022-06-14 12:46:50.950191
# Unit test for method value of class _Option
def test__Option_value():
    op = _Option(
        name="name",
        default=None,
        type=int,
        help=None,
        metavar=None,
        multiple=False,
        file_name=None,
        group_name=None,
        callback=None,
    )
    actual = op.value()
    expected = None
    assert actual == expected
    
    op._value = 1
    actual = op.value()
    expected = 1
    assert actual == expected
    
    op = _Option(
        name="name",
        default=[],
        type=int,
        help=None,
        metavar=None,
        multiple=True,
        file_name=None,
        group_name=None,
        callback=None,
    )

# Generated at 2022-06-14 12:46:54.219023
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    class Foo(object):
        pass
    foo = Foo()
    with mock.patch.object(foo, 'bar', 'baz'):
        assert foo.bar == 'baz'
    assert not hasattr(foo, 'bar')

# Generated at 2022-06-14 12:47:07.058013
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # Test that the correct options are yielded by __iter__
    op = OptionParser()
    # Test that the correct options are yielded by __iter__
    op = OptionParser()
    op.define("str_opt", default="foo")
    op.define("int_opt", default=3, type=int)
    op.define("bool_opt", default=True, type=bool)
    op.define("float_opt", default=3.14, type=float)
    op_options = dict()
    for o in op:
        op_options[o.name] = o
    assert op_options.keys() == {'str_opt', 'int_opt', 'bool_opt', 'float_opt'}

# Generated at 2022-06-14 12:47:18.656255
# Unit test for method set of class _Option
def test__Option_set():
    import tornado.options
    import copy

# Generated at 2022-06-14 12:47:29.466478
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import tempfile
    from tornado.options import OptionParser, options
    from tornado.testing import AsyncTestCase, gen_test

    parser = OptionParser()
    parser.define("x", type=int)
    parser.define("y", type=float)
    parser.define("z", type=str)

    def check_values(x, y, z):
        assert options.x == x
        assert options.y == y
        assert options.z == z

    @gen_test
    def test_config_file():
        with tempfile.NamedTemporaryFile("wb", delete=False) as f:
            config_file = f.name

# Generated at 2022-06-14 12:47:39.246188
# Unit test for method __setattr__ of class OptionParser

# Generated at 2022-06-14 12:47:52.292740
# Unit test for method set of class _Option
def test__Option_set():
    print("Testing _Option.set(self, value)")
    o = _Option("name", default = None, type = None, help = None, metavar = None, multiple = False, file_name = None, group_name = None, callback = None)
    try:
        print("\tTesting with value = None")
        o.set(value = None)
        print("\tIt works!")
    except Exception as e:
        print("\tFails: {}".format(e))
    try:
        print("\tTesting with value = ")
        o.set(value = 1)
        print("\tIt works!")
    except Exception as e:
        print("\tFails: {}".format(e))

# Generated at 2022-06-14 12:48:14.802171
# Unit test for method parse of class _Option

# Generated at 2022-06-14 12:48:19.575621
# Unit test for method value of class _Option
def test__Option_value():
    opt = _Option("name", metavar="name", help="help",
                  group_name="group_name", type=str, default="", multiple=True,
                  callback=lambda x: [print(x)], file_name="hello_world.py")
    print(opt.value())


# Generated at 2022-06-14 12:48:22.230676
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    o = options = OptionParser()

    m = _Mockable(o)
    m.__setattr__("name", True)
    assert options.name
    assert m.name



# Generated at 2022-06-14 12:48:35.830819
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    result = OptionParser.parse_command_line(OptionParser, ["--database=mysql://user:pass@proximus.modulusmongo.net:27017/I7wixeqa"])
    
    assert result == []
    
    options = OptionParser()
    result = options.parse_command_line(["--database", "mysql://user:pass@proximus.modulusmongo.net:27017/I7wixeqa"])
    assert len(result) == 0
    assert options.database == "mysql://user:pass@proximus.modulusmongo.net:27017/I7wixeqa"
    
    options = OptionParser()
    result = options.parse_command_line(["--help"])
    options.print_help()
    assert len(result) == 0

# Generated at 2022-06-14 12:48:36.947387
# Unit test for method __setattr__ of class OptionParser
def test_OptionParser___setattr__():
    # all doc tests are in
    pass
    # OptionParser._normalize_name

# Generated at 2022-06-14 12:48:46.390190
# Unit test for method parse of class _Option
def test__Option_parse():
    try:
        option = _Option("option")
    except ValueError as e:
        print("Error: %s" % e)
    try:
        option = _Option("option", type=datetime.datetime)
    except ValueError as e:
        print("Error: %s" % e)
    try:
        option = _Option("option", type=datetime.datetime, help="one help")
    except ValueError as e:
        print("Error: %s" % e)
    try:
        option = _Option("option", type=datetime.datetime, help="two help")
    except ValueError as e:
        print("Error: %s" % e)

# Generated at 2022-06-14 12:48:47.639697
# Unit test for method __setattr__ of class OptionParser
def test_OptionParser___setattr__():
    obj = OptionParser()
    with pytest.raises(AttributeError):
        obj.foo = 'bar'



# Generated at 2022-06-14 12:48:54.124646
# Unit test for method parse of class _Option
def test__Option_parse():
    opt = _Option(
        "name",
        datetime.datetime,
        default=None,
        type=datetime.datetime,
        help=None,
        metavar=None,
        multiple=False,
        file_name=None,
        group_name=None,
        callback=None,
    )
    dt = opt.parse("2015-01-01")
    assert dt.year == 2015 and dt.month == 1 and dt.day == 1
    
    opt.multiple = True
    dt = opt.parse("2015-01-01,2015-01-05")
    assert dt == [datetime.datetime(2015, 1, 1, 0, 0), datetime.datetime(2015, 1, 5, 0, 0)]
    
    opt.type = datetime.tim

# Generated at 2022-06-14 12:49:04.075783
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    import pytest

    # Mock attribute self.groups
    OptionParser.groups = mock_attribute(name=None)

    # Mock attribute self._options
    OptionParser._options = mock_attribute(name=None)

    # Mock attribute self._options[name]
    OptionParser._options[name] = mock_attribute(name=None)

    # Mock attribute self._options[name].name
    OptionParser._options[name].name = mock_attribute(name=None)

    with pytest.raises(Error):
        options = OptionParser()
        all = options.__iter__()
        next = all.__next__()


# Generated at 2022-06-14 12:49:11.738432
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # It should return the option iterator
    op = OptionParser()
    op.define('name', help='my name', group='my group')
    op.define('name', help='my name', group='my group')
    op.define('age', default=10, help='your age', group='your group')
    it = op.__iter__()
    # It should return the option iterator
    assert isinstance(it, types.GeneratorType)
    # It should return the option iterator
    names = list(op)
    assert 'name' in names
    assert 'age' in names


# Generated at 2022-06-14 12:49:24.680605
# Unit test for method parse of class _Option
def test__Option_parse():
    # initialize option
    option = _Option("var_name", default="my_default_value", type=str,
                     help="some help string", metavar="some_metavar", multiple=False,
                     file_name="some_file_name", group_name="some_group_name", callback=None,)
    print("value before parsing: ", option.value())
    # test parse
    option.parse("new_value")
    print("value after parsing: ", option.value())


# Generated at 2022-06-14 12:49:31.993257
# Unit test for method parse of class _Option
def test__Option_parse():
    print("\n ***************** Unit test for method parse of class _Option ***************** ")
    # Test whether the method parse of _Option can parse correctly
    # test on the int type
    # 1. test on the type of int
    option1 = _Option('test_option',None,int,None,None,False,None,None,None)
    assert option1.parse("2") == 2
    # 2.test on the type of multiple
    option5 = _Option('test_option',None,int,None,None,True,None,None,None)
    assert option5.parse("1,2,3,4") == [1,2,3,4]
    assert option5.parse("1:4") == [1,2,3,4]
    # test on the float type
    # 1. test on the type

# Generated at 2022-06-14 12:49:43.471308
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    # Test case 1
    import tempfile
    import os
    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = os.path.join(tmpdir, "test.cfg")
        with open(config_file, "w") as f:
            print("port = 80", file=f)
        options.define("port", type=int, help="port")
        options.parse_config_file(config_file)
        value = options.port
        err = 80
        assert value == err, "Expected {}, but got: {}".format(err, value)

    # Test case 2
    options.parse_config_file(config_file, final=False)
    value = options.port
    err = 80
    assert value == err, "Expected {}, but got: {}".format(err, value)

# Generated at 2022-06-14 12:49:47.618321
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    # _OptionParser.__iter__() -> generator of str
    parser = _OptionParser()
    define = parser.define
    define('foo')
    define('bar')
    define('baz')
    values = sorted(parser)
    assert values == ['bar', 'baz', 'foo']
    define('garply')
    values = sorted(parser)
    assert values == ['bar', 'baz', 'foo', 'garply']


# Generated at 2022-06-14 12:49:56.047933
# Unit test for method parse of class _Option
def test__Option_parse():
    temp = _Option("test", type=int)
    assert temp.parse("0") == 0
    temp = _Option("test", type=float)
    assert temp.parse("1") == 1.0
    temp = _Option("test", type=str)
    assert temp.parse("2") == "2"
    temp = _Option("test", type=bool)
    assert temp.parse("3") == True
    temp = _Option("test", type=datetime.timedelta)
    assert temp.parse("3w") == datetime.timedelta(weeks=3)
    temp = _Option("test", type=datetime.datetime)
    assert temp.parse("2018-07-25") == datetime.datetime(2018, 7, 25)


# Generated at 2022-06-14 12:50:00.432649
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    opt = OptionParser()
    assert isinstance(opt, OptionParser)
    try:
        next(iter(opt))
        raise Exception("Shouldn't get here")
    except StopIteration:
        pass



# Generated at 2022-06-14 12:50:10.846607
# Unit test for method __setattr__ of class OptionParser
def test_OptionParser___setattr__():
    from tornado.options import _Options
    from tornado.options import _Option
    from tornado.options import _mock
    from tornado.options import define
    from datetime import datetime
    from datetime import timedelta
    import unittest.mock
    import pytest

    assert not hasattr(_Options(), '_test')
    from tornado.log import gen_log

    _Options()._test = "value"
    assert _Options()._test == "value"
    with unittest.mock.patch.object(
        _Options().mockable(), '_test', 'different value'
    ):
        assert _Options()._test == 'different value'
    assert _Options()._test == 'value'
    with pytest.raises(AttributeError):
        _Options()._test2   # type: ignore

    test_

# Generated at 2022-06-14 12:50:14.456867
# Unit test for method value of class _Option
def test__Option_value():
    option = _Option(name = "test", default = None, type = str, help = None, metavar = None, multiple = False, file_name = None, group_name = None)
    assert option.value() == None
    option.set("test")
    assert option.value() == "test"

# Generated at 2022-06-14 12:50:19.799623
# Unit test for method __setattr__ of class OptionParser
def test_OptionParser___setattr__():
    parser = OptionParser(values=options)
    parser.name = "Thomas"
    assert parser.name == "Thomas"

    # __setattr__在values是None的情况下，会调用OptionParser的__setattr__方法
    parser = OptionParser()
    parser.name = "Thomas"
    assert parser.name == "Thomas"

# 由于__getattr__会调用_normalize_name，所以在这里单独测试一下_normalize_name

# Generated at 2022-06-14 12:50:30.393123
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    import unittest
    import types
    import os
    import sys
    import tempfile
    from tornado.options import OptionParser
    from tornado.options import _Mockable
    from tornado.options import Error
    from tornado.platform.auto import set_close_exec

    class TestOptions(unittest.TestCase):
        def setUp(self):
            self.options = OptionParser()
            self.mockable = _Mockable(self.options)

        def tearDown(self):
            del self.options
            del self.mockable

        def test_setattr(self):
            self.mockable.name = 'test'
            self.assertEqual(self.options.name, 'test')

        def test_delattr(self):
            self.options.name = 'test'
            self.m

# Generated at 2022-06-14 12:50:41.792500
# Unit test for method parse of class _Option

# Generated at 2022-06-14 12:50:53.007952
# Unit test for method parse of class _Option
def test__Option_parse():
    import unittest
    #from tornado.options import _Option

    class TestOption(_Option):
        UNSET = None

    option = TestOption("name")

    # Test for parameter check
    with unittest.mock.patch.object(_Option, "parse") as mock_parse:
        mock_parse.side_effect = Exception("raise an exception to test parameter check")
        with unittest.TestCase().assertRaises(Exception) as context:
            option.parse("")
        unittest.TestCase().assertTrue("raise an exception to test parameter check" in str(context.exception))
    with unittest.mock.patch.object(_Option, "parse") as mock_parse:
        mock_parse.side_effect = Exception("raise an exception to test parameter check")

# Generated at 2022-06-14 12:51:02.044872
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os, sys
    import unittest

    class OptionParserTest(unittest.TestCase):

        def setUp(self):
            self.orig_sys_path = sys.path[:]
            self.orig_working_directory = os.getcwd()
            self.tempdir = tempfile.mkdtemp()
            os.chdir(self.tempdir)
            sys.path.insert(0, self.tempdir)

        def tearDown(self):
            sys.path = self.orig_sys_path
            os.chdir(self.orig_working_directory)
            shutil.rmtree(self.tempdir)

        def test_parse_config_file(self):
            path = os.path.join(self.tempdir, 'config')

# Generated at 2022-06-14 12:51:04.879466
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    """_Mockable.__setattr__"""
    options = OptionParser()
    option = options.define("name", default=None)
    assert option.default == None
    setattr(options, "name", "test")
    assert option.default == "test"


# Generated at 2022-06-14 12:51:10.989788
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    # test_args = ['test.py', '-test', 'test']
    # test_args = ['test.py', '--test', 'test2']
    # test_args = ['test.py', '--test2']
    test_args = ['test.py', '--test3', 'hello']
    test = OptionParser()
    test.define('test')
    test.define('test2', type=bool)
    test.define('test3', default='hello world')
    test.parse_command_line(test_args)

# Generated at 2022-06-14 12:51:22.846564
# Unit test for method parse of class _Option
def test__Option_parse():
        option = _Option('db_host',
                                type=basestring_type,
                                default='',
                                help='hostname of the database',
                                metavar='HOST')
        option.parse('cassandra')
        assert option.value() == 'cassandra'
        # Test for error of setting multiple=False with value of type list
        option1 = _Option('db_host',
                                type=basestring_type,
                                default='',
                                help='hostname of the database',
                                metavar='HOST',
                                multiple=True)
        try:
            option1.set(['value1', 'value2'])
        except Exception: assert True
        else: assert False
        # Test for error of setting multiple=True with value of type string
        option1 = _

# Generated at 2022-06-14 12:51:24.836520
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    options = OptionParser()
    options.define("name", type=str, default="Bob", help="name help")
    assert "name" in options
    assert "not_in_options" not in options


# Generated at 2022-06-14 12:51:31.509834
# Unit test for method value of class _Option
def test__Option_value():
    option = _Option(name='name', default=None, type=datetime.datetime, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
    # if no value has been set before,default value is returned
    assert option.value() is None
    # test case when value is set
    default=datetime.datetime.now()
    option.set(default)
    assert option.value() is default


# Generated at 2022-06-14 12:51:34.549688
# Unit test for method set of class _Option
def test__Option_set():
    option = _Option(name = 'name', default = None, type = int, help = '', metavar = None, multiple = False, file_name = None, group_name = None, callback = None)
    value = 6
    assert option.set(value) == None
    assert option._value == value
    value = '6'
    assert option.set(value) == None
    assert option._value == int(value)



# Generated at 2022-06-14 12:51:40.827082
# Unit test for method parse_command_line of class OptionParser
def test_OptionParser_parse_command_line():
    _OptionParser_instance_0= _OptionParser()
    assert isinstance(_OptionParser_instance_0, _OptionParser)
    # Call the method
    try:
        _OptionParser_ret_0 = _OptionParser_instance_0.parse_command_line(args=None, final=True)
    except: #catch *all* exceptions
        _OptionParser_ret_0 = False
    return _OptionParser_ret_0


# Generated at 2022-06-14 12:51:59.425297
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    import os
    import tempfile

    @gen.coroutine
    @gen_test
    def test_parse_config_file():
        cfg = """
foo = 5
bar = 'hello'
baz = "hello"
qux = []
quux = {}
corge = 3.14
grault = True
garply = None
waldo = datetime.timedelta(1)
fred = datetime.datetime(2012, 1, 2, 3, 4, 5)
"""

        with tempfile.NamedTemporaryFile(suffix='.py') as f:
            f.write(cfg.encode('utf-8'))
            f.flush()
            options.parse_config_file(f.name)
        assert options.foo == 5
        assert options.bar == 'hello'
        assert options.b

# Generated at 2022-06-14 12:52:10.266907
# Unit test for method group_dict of class OptionParser
def test_OptionParser_group_dict():
    parser = OptionParser()
    parser.define("port", type=int, default=8888, group="application")
    parser.define("logging", default="debug", group="application")
    parser.define("log_file_prefix", default="tornado.log", group="application")
    parser.define("base_url", default=None, group="application")
    parser.define("debug", type=bool, default=False, group="application")
    parser.define("send_email", type=bool, default=False, group="application")
    parser.define("address", type=str, default="0.0.0.0", group="application")
    parser.define("locale_path", type=str, default="locale", group="application")

# Generated at 2022-06-14 12:52:20.020858
# Unit test for method set of class _Option
def test__Option_set():
    import unittest
    # Assumption:
    # If a subclass determines a new attribute,
    # we can safely assume that it is an AttributeError.
    # This is because of the handling in _parse_command_line.
    # There is always one of the following:
    # - a class is defined
    # - a function is defined
    # - an inner class is defined
    # - the class is the type.
    try:
        from unittest.mock import patch
        from unittest.mock import Mock
    except ImportError:
        from mock import patch
        from mock import Mock

    class OptionParserSubclass(OptionParser):

        def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)

# Generated at 2022-06-14 12:52:25.227587
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    option = OptionParser()
    m = _Mockable(option)
    m.name = 'hello'
    assert option.name == 'hello', 'setattr fail'
    m.name = 'world'
    assert option.name == 'world', 'multi setattr fail'
    m.name = 'test'
    assert option.name == 'test', 'override setattr fail'
    del m.name
    assert option.name == 'hello', 'delattr fail'



# Generated at 2022-06-14 12:52:31.270478
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    # 1. Create a non-empty OptionParser instance
    op = OptionParser()
    op.define("test", default=False)
    # 2. Create a _Mockable wrapper
    m = _Mockable(op)
    # 3. Set the value of the already present option
    m.test = True
    # 4. Check that the value is changed
    assert op.test == True

# Generated at 2022-06-14 12:52:41.915318
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    import random
    import time
    import logging
    import unittest
    from tornado.options import _Mockable, OptionParser
    class Mockable_setattr(unittest.TestCase):
        def setUp(self):
            logging.info("test _Mockable.__setattr__...")
            self.op = OptionParser()
            self.op.define("name")
            self.m = _Mockable(self.op)
            self.n = random.randint(1,10000)
        def tearDown(self):
            logging.info("end for test __setattr__...")
        def test__setattr__(self):
            self.m.name = self.n
            self.assertEqual(self.op.name, self.n)
    unittest.main(verbosity=2)


# Generated at 2022-06-14 12:52:45.297797
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
    a = mock.MagicMock()
    b = _Mockable(a)
    b.foo = 123
    a.__setattr__.assert_called_with('foo', 123)


# Generated at 2022-06-14 12:52:54.490653
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
   import os
   import sys
   import tempfile
   import textwrap
   import unittest
   import tornado
   try:
      import unittest.mock as mock
   except ImportError:
      import mock
   from tornado.options import Error
   from tornado.options import define
   from tornado.options import options
   from tornado.options import parse_command_line
   from tornado.options import OptionParser
   from tornado.options import _Option
   from tornado.testing import AsyncTestCase
   from tornado.testing import ExpectLog
   from tornado.testing import gen_test
   from tornado.testing import main
   from tornado.testing import SkipTest
   from tornado.testing import LogTrapTestCase
   from tornado.util import exec_in
   define('test1', type=str, default='1')

# Generated at 2022-06-14 12:52:59.091591
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    op = OptionParser()
    op.define("port", type=int, default=8888)
    op.define("log_to_stderr", type=bool, default=False)
    assert "port" in op._options
    assert op._options["port"].value() == 8888
    op.parse_config_file("/tmp/test_parse_config_file")
    assert op._options["port"].value() == 80
    assert op._options["log_to_stderr"].value() == True



# Generated at 2022-06-14 12:53:08.945000
# Unit test for method parse of class _Option
def test__Option_parse():

    print("Testing _Option_parse")
    # create a instance of class _Option
    option = _Option('test', None, basestring_type, None, None, False, None, None, None)
    # ensure type(option) = _Option
    assert type(option) == _Option
    
    # ensure option.type = basestring_type
    assert option.type == basestring_type
    # ensure option.parse('test') = 'test'
    assert option.parse('test') == 'test'

    # assert option.multiple = true
    option.multiple = True
    assert option.multiple == True
    # ensure option._value = []
    assert option._value == []
    # ensure option.parse('test') = ['test']
    assert option.parse('test') == ['test']
    
    # ensure option.

# Generated at 2022-06-14 12:54:07.905216
# Unit test for method parse of class _Option
def test__Option_parse():
    def _test_type(args, expected):
        o = _Option("--test", type=args)
        assert o.parse("1") == expected

    _test_type(None, NotImplementedError)
    _test_type(bool, True)
    _test_type(int, 1)
    _test_type(float, 1.0)
    _test_type(str, "1")
    #_test_type(datetime.datetime, NotImplementedError)
    #_test_type(datetime.timedelta, NotImplementedError)


# Generated at 2022-06-14 12:54:10.498118
# Unit test for method __setattr__ of class _Mockable
def test__Mockable___setattr__():
  m=_Mockable(OptionParser())
  assert __setattr__(m, 'x', 1) == None


# Generated at 2022-06-14 12:54:19.515167
# Unit test for method parse_config_file of class OptionParser
def test_OptionParser_parse_config_file():
    from tornado.options import OptionParser, Error, options
    import os
    import tempfile
    import unittest
    from unittest import mock

    here = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(here, "test_options.conf")
    option_names = [
        "foo",
        "bar",
        "baz",
        "biz",
        "intlist",
        "floatlist",
        "stringlist",
        "timedelta",
        "bool_true",
        "bool_false",
    ]
    foo_value = "foo"
    bar_value = "bar"
    baz_value = "baz"
    biz_value = "biz"

# Generated at 2022-06-14 12:54:26.122813
# Unit test for method __iter__ of class OptionParser
def test_OptionParser___iter__():
    fn = _OptionParser.__iter__
    op = OptionParser()
    op.define('name', 'value', str, 'help')
    op.define('name2', 'value2', str, 'help')
    it = fn(op)
    assert it is not None
    key, value = next(it)
    assert key == 'name' and value == 'value'
    key, value = next(it)
    assert key == 'name2' and value == 'value2'

# Generated at 2022-06-14 12:54:36.769829
# Unit test for method parse of class _Option
def test__Option_parse():
    o = _Option("name", multiple=True, type=int)
    o.parse("1,2,3")
    assert o.value()[0] == 1
    assert o.value()[1] == 2
    assert o.value()[2] == 3

    o = _Option("name", multiple=True, type=int)
    o.parse("-1,0,-3")
    assert o.value()[0] == -1
    assert o.value()[1] == 0
    assert o.value()[2] == -3

    o = _Option("name", multiple=True, type=int)
    assert o.parse("1,2,3") == [1, 2, 3]

    o = _Option("name", multiple=True, type=int)

# Generated at 2022-06-14 12:54:46.785671
# Unit test for method parse of class _Option
def test__Option_parse():
    o = _Option("name", type=datetime.datetime, multiple=True)
    o.parse("2013-04-10 00:00:00")
    assert len(o.value()) == 1
    assert o.value()[0].year == 2013
    assert o.value()[0].month == 4
    assert o.value()[0].day == 10
    assert o.value()[0].hour == 0
    assert o.value()[0].minute == 0
    assert o.value()[0].second == 0
    o.parse("2013-04-10 00:00:01")
    assert len(o.value()) == 2
    assert o.value()[0].year == 2013
    assert o.value()[0].month == 4
    assert o.value()[0].day == 10
    assert o.value

# Generated at 2022-06-14 12:54:53.211400
# Unit test for method parse of class _Option
def test__Option_parse():
    option = tornado.options._Option("name", str, multiple=True)
    assert option.parse("value1") == ['value1']
    assert option.parse("value1,value2") == ['value1', 'value2']


test__Option_parse()
 

# Generated at 2022-06-14 12:55:02.136813
# Unit test for method parse of class _Option
def test__Option_parse():
    from datetime import datetime, timedelta
    from tornado.options import Error, _Option
    option=_Option(name='', type=object, multiple=False, file_name='', group_name='')
    # test bool type
    bool_option = _Option('', type=bool, multiple=False)
    assert bool_option.parse('') is True
    assert bool_option.parse('false') is False
    assert bool_option.parse('0') is False
    assert bool_option.parse('F') is False
    #test string type
    string_option = _Option('', type=str, multiple=False)
    assert string_option.parse('hello') == 'hello'
    #test datetime type
    datetime_option = _Option('', type=datetime, multiple=False)
    assert datetime_option

# Generated at 2022-06-14 12:55:11.766618
# Unit test for method set of class _Option
def test__Option_set():
    import unittest
    import copy
    import shutil
    import tempfile
    import tornado
    
    @tornado.options.define('test_set', type=int, multiple=True, help='test_set help')
    def test_set_func():
        pass

    class _OptionTest(unittest.TestCase):
        def setUp(self):
            self.options_object = tornado.options.options
            test_set_func()
            self.options_object._options['test_set'].set(self.options_object.test_set)
        def test_set_case_0(self):
            self.options_object._options['test_set'].set([222])
            self.assertEqual(self.options_object._options['test_set'].value(), [222])

# Generated at 2022-06-14 12:55:22.032208
# Unit test for method parse of class _Option
def test__Option_parse():
    _Option.__init__(name, default, type, help, metavar, multiple, file_name, group_name, callback)
    try:
        assert _Option.parse(self, value) == _Option.value
    except AssertionError:
        _Option.set(self, value)
        assert _Option._parse_datetime(self, value) == _Option._DATETIME_FORMATS
        assert _Option._parse_timedelta(self, value) == _Option._TIMEDELTA_ABBREV_DICT
        assert _Option._parse_bool(self, value) == _Option._TIMEDELTA_ABBREV_DICT
        assert _Option._parse_string(self, value) == _Option.type
