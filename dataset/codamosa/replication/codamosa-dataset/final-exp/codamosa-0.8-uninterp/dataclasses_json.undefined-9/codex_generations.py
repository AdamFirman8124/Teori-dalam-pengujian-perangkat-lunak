

# Generated at 2022-06-13 19:20:46.959157
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class DummyClass:
        val: int
        num: int

    mock_cls = DummyClass
    mock_kvs = {"val": 42, "num": -42, "undefined": "parameter"}
    expected_defined_kvs = {"val": 42, "num": -42}
    known_given_parameters, unknown_given_parameters = \
        _IgnoreUndefinedParameters.handle_from_dict(mock_cls, mock_kvs)
    assert known_given_parameters == expected_defined_kvs
    assert len(unknown_given_parameters) == 0



# Generated at 2022-06-13 19:20:55.515984
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # noinspection PyProtectedMember
    from dataclasses import dataclass, MISSING

    @dataclass
    class Example:
        one: int
        two: str = ""
        three: str = dataclasses.field(default=MISSING)
        undefined_parameters: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)

    example_dict = {
        "one": 1,
        "two": "two",
        "three": "three",
        "four": "four",
        "undefined_parameters": None
    }
    expected_res = {
        "one": 1,
        "two": "two",
        "three": "three",
        "undefined_parameters": {"four": "four"}
    }
    assert _CatchAll

# Generated at 2022-06-13 19:20:59.826266
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class SomeClass:
        def __init__(self, defined_param: str,
                     # type: ignore
                     undefined_param: CatchAll = None):
            self.defined_param = defined_param
            self.undefined_param = undefined_param

    some_obj = SomeClass(defined_param="a",
                         # type: ignore
                         undefined_param={"b": "c", "d": "e"})
    dump = some_obj.__dict__
    dump = _CatchAllUndefinedParameters.handle_to_dict(obj=some_obj,
                                                       kvs=dump)
    assert dump == {"defined_param": "a", "b": "c", "d": "e"}



# Generated at 2022-06-13 19:21:02.561837
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert _UndefinedParameterAction.handle_to_dict({},{}) == {}
    assert _UndefinedParameterAction.handle_to_dict({},{'a':1}) == {'a':1}

# Generated at 2022-06-13 19:21:08.184952
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        a: Any
        b: Any

    class_test_a = TestClass(None, None)
    parameters = {"a": 1}

    try:
        _RaiseUndefinedParameters \
            .handle_from_dict(class_test_a, parameters)
        raise AssertionError("Expected to raise UndefinedParameterError")
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:21:17.087401
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str

    known_params, unknown_params = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            TestClass, {"a": 1, "c": "c"})
    assert known_params == {"a": 1}
    assert unknown_params == {"c": "c"}

    known_params, unknown_params = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            TestClass, {"a": 1, "b": "b", "c": "c"})
    assert known_params == {"a": 1, "b": "b"}
    assert unknown_params == {"c": "c"}



# Generated at 2022-06-13 19:21:25.433977
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # noinspection PyShadowingBuiltins
    class TestClass:
        x: int
        y: Any = CatchAll

        def __init__(self, x: int, y: Any):
            self.x = x
            self.y = y

    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                         dict(x=1, y={"a": 5})) \
           == dict(x=1, y=dict(a=5))
    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                         dict(x=1)) \
           == dict(x=1, y={})

# Generated at 2022-06-13 19:21:32.422443
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    @dataclasses.dataclass
    class CatchAllTest:
        val: int
        extra: CatchAll

    d = CatchAllTest(1, {"a": "b"})
    assert _UndefinedParameterAction.handle_to_dict(d, {'val': 1, 'a': 'b'}) == {'val': 1}

# Generated at 2022-06-13 19:21:34.814929
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("Hi")
    except UndefinedParameterError as err:
        assert err.args[0] == "Hi"

# Generated at 2022-06-13 19:21:37.538550
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test message")
    except UndefinedParameterError as e:
        assert str(e) == "test message"



# Generated at 2022-06-13 19:22:02.352945
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Test:
        a: int
        b: int

    action = _RaiseUndefinedParameters()
    exception = None
    try:
        Test(**action.handle_from_dict(Test, {"a": 1, "b": 2, "c": 3}))
    except UndefinedParameterError as e:
        exception = e
    assert str(e) == "Received undefined initialization arguments {'c': 3}"


# Generated at 2022-06-13 19:22:11.430117
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class TestClass:
        pass

    TestClass.__init__ = lambda *args: None  # type: ignore

    class _TestableAction(_UndefinedParameterAction):
        @staticmethod
        def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            return kvs

    action = _TestableAction()

    test_class_init_before = TestClass.__init__
    TestClass.__init__ = action.create_init(TestClass)
    assert TestClass.__init__ is not test_class_init_before
    assert TestClass.__init__.__name__ == "_ignore_init"


# Unit tests for method __separate_defined_undefined_kvs of class _UndefinedParameterAction

# Generated at 2022-06-13 19:22:17.561024
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from .test_schema import test_schema
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        foo: int
        bar: str
        arec: dict
        # We do not have to define the any field here

    tc = TestClass(6, "hello", {"a": "b"}, any={"c": "d"})
    d = dataclasses_json.dataclass_to_dict(test_schema, tc,
                                           encode_letter_case_types=dict)
    assert d == {"foo": 6, "bar": "hello", "a": "b", "c": "d"}

# Generated at 2022-06-13 19:22:25.006937
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class TestOne(object):

        def __init__(self, *args, **kwargs):
            pass

    @dataclass
    class TestTwo(object):

        arg_one: int
        arg_two: int

        def __init__(self, arg_one, arg_two):
            pass

    @dataclass
    class TestThree(object):

        arg_one: int
        arg_two: int

        def __init__(self, arg_one, arg_two, *args, **kwargs):
            pass

    @dataclass
    class TestFour(object):

        arg_one: int
        arg_two: int

        def __init__(self, arg_one, arg_two=1):
            pass

    assert Test

# Generated at 2022-06-13 19:22:33.529095
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass(metaclass=dataclasses.dataclass):
        a: int = 1
        b: str = "hey"
        c: float = 3.14

    tc = dataclasses.dataclass(TestClass,
                               _UNDEFINED_PARAMETER_ACTION=_RaiseUndefinedParameters)
    test = tc(a=2, b="hallo", c=3.,
              _UNKNOWN0=1)
    assert test.a == 2
    assert test.b == "hallo"
    assert test.c == 3.



# Generated at 2022-06-13 19:22:44.793415
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class UndefinedParametersClass:
        def __init__(self, defined_parameter):
            self.defined_parameter = defined_parameter

    from_dict_method = _RaiseUndefinedParameters.handle_from_dict
    defined_parameter = "defined"
    undefined_parameter = "undefined"
    good_dict = {
        "defined_parameter": defined_parameter
    }
    bad_dict = {
        "defined_parameter": defined_parameter,
        "undefined_parameter": undefined_parameter
    }
    test_result_good = from_dict_method(UndefinedParametersClass, good_dict)
    assert test_result_good == good_dict
    test_result_bad = from_dict_method(UndefinedParametersClass, bad_dict)
    assert test_result_bad

# Generated at 2022-06-13 19:22:51.285468
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import pytest
    from dataclasses import dataclass
    from typing import Optional, Union

    @dataclass
    class Dataclass(object):
        normal_parameter: int

        def __init__(self, normal_parameter, undefined_parameter):
            self.normal_parameter = normal_parameter
            self.undefined_parameter = undefined_parameter

    d = Dataclass(normal_parameter=1, undefined_parameter=3)
    new_init = _IgnoreUndefinedParameters.create_init(d)
    instance = new_init(d, normal_parameter=2, undefined_parameter=4)
    assert instance.normal_parameter == 2
    assert instance.undefined_parameter != 4



# Generated at 2022-06-13 19:22:53.645330
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """Check that abstract method handle_dump returns {}"""
    result = _UndefinedParameterAction.handle_dump(None)
    assert result == {}

# Generated at 2022-06-13 19:23:01.143029
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.utils import FromDict
    class Example:
        class Meta:
            unknown_parameters = Undefined.INCLUDE
        dictionary: CatchAll

        def __init__(self, **kvs):
            FromDict().make_dataclass(self.__class__, kvs)

    ex1 = Example(dictionary=dict(a=1))
    ex2 = Example(a=1)

    assert ex1.dictionary == dict(a=1)
    assert ex2.dictionary == dict()


# Generated at 2022-06-13 19:23:07.399776
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from marshmallow import ValidationError
    from typing import Dict

    from dataclasses_json import dataclass_json, config
    from dataclasses_json.utils import CatchAllVar

    @dataclass_json
    @dataclass_json
    class CatchAll:
        non_catch_all: int
        catch_all: CatchAllVar = CatchAllVar()

        @classmethod
        def _undefined_parameters_handler(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            return _CatchAllUndefinedParameters.handle_from_dict(CatchAll, kvs)

    def test_empty():
        result = CatchAll._undefined_parameters_handler({})
        assert result["non_catch_all"] == None

# Generated at 2022-06-13 19:23:34.949674
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert _UndefinedParameterAction.handle_to_dict(None, {}) == {}
    assert _UndefinedParameterAction.handle_to_dict(None, {1: 2}) == {1: 2}

# Generated at 2022-06-13 19:23:44.993035
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, _foo: int, catch_all: Optional[CatchAllVar]):
            self._foo = _foo
            self._catch_all = catch_all

    class WithUndefinedFields:
        def __init__(self, _foo: int, _catch_all: Optional[CatchAllVar]):
            self._foo = _foo
            self._catch_all = _catch_all

    # Ignore the first element, which is the class name
    orig_fields = fields(WithUndefinedFields)[1:]
    known_fields, unknown_fields = orig_fields[0], orig_fields[1]
    object_test_class = TestClass(42, {"_bar": "test"})

# Generated at 2022-06-13 19:23:49.050902
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    import dataclasses as dc


    @dc.dataclass(undefined=Undefined.RAISE)
    class TestClass:
        a: str
        b: str
        c: str


    undefinedParameters = {"a": "hi", "d": "hello"}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(
            TestClass, undefinedParameters)



# Generated at 2022-06-13 19:23:59.131438
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class Mock:
        defined: bool
        optional_with_default: Optional[str] = "abc"
        optional: Optional[str]
        catch_all: Optional[CatchAllVar]

    catch_all_undefined_parameter = _CatchAllUndefinedParameters()

    created = _CatchAllUndefinedParameters.handle_from_dict(
        cls=Mock, kvs={"defined": True, "catch_all": {"other": "value"}})
    assert created == {"defined": True, "catch_all": {"other": "value"}}

    # ignore undefined parameters

# Generated at 2022-06-13 19:24:05.204344
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        a: int = 1
        b: int = 2

    class_under_test = TestClass
    known_parameters = {"a": 3}
    return_value = _CatchAllUndefinedParameters.handle_from_dict(
        class_under_test, known_parameters)
    assert return_value == {"a": 3}



# Generated at 2022-06-13 19:24:16.604355
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # noinspection DuplicatedCode
    class _TestClass:
        def __init__(self, **kwargs):
            pass

        def _test_method(self, **kwargs):
            return _CatchAllUndefinedParameters. \
                handle_from_dict(self.__class__, kwargs)

    def _test_undefined_parameters(test_dict, expected):
        test_instance = _TestClass(**test_dict)
        actual = test_instance._test_method(**test_dict)
        assert actual == expected

    test_dict = {"a": 1, "b": 2, "catch_all": {"c": 3}}
    expected = {"a": 1, "b": 2, "catch_all": {"c": 3}}
    _test_undefined_parameters(test_dict, expected)



# Generated at 2022-06-13 19:24:23.111456
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        a: int
        b: str
        c: Optional[CatchAllVar]

        def __init__(self, a: int, b: str, c: Optional[CatchAllVar] = None):
            print("TEST")


    new_init = _CatchAllUndefinedParameters.create_init(TestClass)
    new_init(None, 1, "b", "c")

# Generated at 2022-06-13 19:24:31.988004
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class MyClass:
        def __init__(self, a: int, b: int, c: int, d: int):
            pass

    my_class = MyClass(1, 2, 3, 4)
    init_function = my_class.__init__

    original_num_args = len(inspect.signature(init_function).parameters) - 1
    num_params_given = 3
    num_args_takeable = original_num_args - num_params_given

    def side_effect(_, *args, **kwargs):
        assert len(args) == num_args_takeable
        assert len(kwargs) == num_params_given
        assert kwargs['b'] == 2
        assert kwargs['c'] == 3
        assert kwargs['d'] == 4
        return

    patched

# Generated at 2022-06-13 19:24:40.104459
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, x: str, y: str, z: str,
                     **kwargs: Dict[str, str]):
            self.x = x
            self.y = y
            self.z = z
            self.kwargs = kwargs

        def __eq__(self, other):
            if not isinstance(other, A):
                return NotImplementedError

            return all(
                (getattr(self, name) == getattr(other, name) for name in
                 ('x', 'y', 'z', 'kwargs')))

    class A:
        def __init__(self, x: str, y: str, z: str,
                     **kwargs: CatchAll):
            self.x = x
            self.y = y
            self.z = z


# Generated at 2022-06-13 19:24:48.600399
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class C:
        a: int
        b: int
        c: int
        d: Optional[CatchAllVar] = None

    c = C(a=10, b=20, c=30, d={"x": "bla", "y": "blub"}, e=15, f=20)
    assert c.a == 10
    assert c.b == 20
    assert c.c == 30
    assert c.d == {"x": "bla", "y": "blub", "e": 15, "f": 20}

    c = C(a=10, b=20, c=30, e=15, f=20)
    assert c.a == 10
    assert c.b == 20
    assert c.c == 30

# Generated at 2022-06-13 19:25:40.383690
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class A:
        a: int
        b: str
        c: int = 0
        cc: int = dataclasses.field(default=0)
        d: str = "test"
        ccc: str = dataclasses.field(default="test")
        e: Optional[str] = None
        dd: Optional[str] = dataclasses.field(default=None)
        catch_all: CatchAll = dataclasses.field(
            default_factory=dict)

    init = _CatchAllUndefinedParameters.create_init(A)
    assert init is not A.__init__
    a = A(None, None, None, None, None, None, None)
    assert a.a == 0
    assert a.b == ""
    assert a.c == 0

# Generated at 2022-06-13 19:25:47.299917
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class C:
        def __init__(self, a, b, c):
            pass
    input_class = C(a=1, b=2, c=3)
    input_kvs = {"a": 10, "b": 20, "c": 30}
    output_kvs = _UndefinedParameterAction.handle_to_dict(input_class,
                                                          input_kvs)
    assert output_kvs == input_kvs



# Generated at 2022-06-13 19:25:53.661050
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Example:
        def __init__(self):
            self.a = 1
            self.b = 2

        def to_dict(self):
            return {'b': 3, 'c': 4}

    assert _UndefinedParameterAction.handle_to_dict(Example(),
                                                    {'a': 1, 'b': 3, 'c': 4}) \
           == {'a': 1, 'b': 3, 'c': 4}

# Generated at 2022-06-13 19:26:04.438499
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import dataclasses
    import typing as tp


    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int
        N: tp.Optional[int] = dataclasses.field(default=None)
        catch: tp.Optional[CatchAllVar] = dataclasses.field(default=None)


    def test_case_1():
        d: Dict = {"a": 1, "b": 2, "c": 3, "d": 4, "catch": {}}
        expected = {"a": 1, "b": 2, "catch": {"c": 3, "d": 4}}
        assert _CatchAllUndefinedParameters.handle_from_dict(TestClass, d) == \
               expected



# Generated at 2022-06-13 19:26:07.526395
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    d = {"defined": 1, dataclasses_json.CatchAllVar(): {"undefined": 2}}
    expected = {"defined": 1, "undefined": 2}
    assert _CatchAllUndefinedParameters.handle_to_dict(None, d) == expected

# Generated at 2022-06-13 19:26:15.869885
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass()
    class CatchAllSample:
        given_parameter: str
        catch_all: Optional[CatchAllVar] = None

    # case 1
    input_dict = {"given_parameter": "bla"}
    result = _CatchAllUndefinedParameters.handle_from_dict(CatchAllSample,
                                                           input_dict)
    assert result == input_dict
    assert not isinstance(result["catch_all"], dict)

    # case 2
    input_dict = {"given_parameter": "bla", "catch_all": {"field1": "value1"}}
    result = _CatchAllUndefinedParameters.handle_from_dict(CatchAllSample,
                                                           input_dict)
    assert result == input_dict

# Generated at 2022-06-13 19:26:25.648521
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Foo:
        @classmethod
        def __init__(cls, **kwargs):
            pass

    @dataclasses.dataclass
    class Bar:
        x: int
        y: int

    foo = Foo(y=1)
    print(
        _UndefinedParameterAction.handle_to_dict(foo, dict(x=1, y=2, z=3)))

    # test for a dataclass
    bar = Bar(x=1, y=2, z=3)
    assert _UndefinedParameterAction.handle_to_dict(bar, dict(x=1, y=2, z=3)) == dict(
        x=1, y=2)



# Generated at 2022-06-13 19:26:27.385048
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("test message")

# Generated at 2022-06-13 19:26:32.166298
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    from tests.fixtures import Point
    test_args = {"x": 1, "y": 2, "z": 3}
    assert _UndefinedParameterAction.handle_from_dict(Point,test_args) == {"x": 1, "y": 2}

# Generated at 2022-06-13 19:26:32.915517
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    pass

# Generated at 2022-06-13 19:28:27.088713
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: str
        c: Optional[CatchAllVar] = None

        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c

    undefined_parameters_obj = \
        _CatchAllUndefinedParameters._get_catch_all_field(A)
    assert undefined_parameters_obj.name == "c"

    obj = A(1, "a")
    assert obj.a == 1
    assert obj.b == "a"
    assert obj.c is None

    obj = A(1, "a", c="c")
    assert obj.a == 1
    assert obj.b == "a"

# Generated at 2022-06-13 19:28:30.736583
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # Given
    import dataclasses

    @dataclasses.dataclass
    class SomeClass:
        a: int
        b: str

        def __init__(self, **kwargs):
            super().__init__()

    # Should
    class_object = SomeClass(**{"a": 1, "b": "test"})
    assert class_object.a == 1
    assert class_object.b == "test"


# Generated at 2022-06-13 19:28:37.475745
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    def _create_test_class(number_of_kwargs, number_of_positional_args):

        class TestClass:
            def __init__(self, *args, **kwargs):
                assert len(args) == number_of_positional_args
                assert len(kwargs) == number_of_kwargs

        return TestClass

    class Helper:
        def __init__(self, new_init):
            self.new_init = new_init

    def test_input(number_of_kwargs, number_of_positional_args):
        kwargs = {f"field{i}": 1.2 for i in range(number_of_kwargs)}
        positional_args = list(range(number_of_positional_args))


# Generated at 2022-06-13 19:28:47.924479
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # noinspection PyUnusedLocal
    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class TestClassDefiningInit:
        a: int = 0
        b: int = 0

        def __init__(self, a: int, b: int) -> None:
            pass

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class TestClassNotDefiningInit:
        a: int = 0
        b: int = 0

    for cls in [TestClassDefiningInit, TestClassNotDefiningInit]:
        new_init_function = _IgnoreUndefinedParameters.create_init(cls)
        assert new_init_function.__name__ == "__init__"

# Generated at 2022-06-13 19:28:54.845751
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # type: () -> None
    """
    Test the _CatchAllUndefinedParameters._create_init function
    """
    from typing import TypeVar

    from dataclasses import dataclass

    T = TypeVar('T')
    @dataclass(undefined=Undefined.INCLUDE)
    class TestClass:
        a: int
        b: Optional[CatchAllVar] = None

        def __init__(self, a: int, b: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b

    TestClass.__init__ = _CatchAllUndefinedParameters.create_init(TestClass)

    result_expected = TestClass(1)
    result = TestClass(1)
    assert result_expected.a == result.a

# Generated at 2022-06-13 19:29:06.414148
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import pytest
    from dataclasses_json import DataClassJsonMixin, config

    @dataclasses.dataclass
    class A(DataClassJsonMixin):
        a: int
        b: int
        c: int = 1
        d: CatchAll = None

    config.undefined = Undefined.INCLUDE

    a = A(a=1, b=2, d={"e": 2})
    actual = _CatchAllUndefinedParameters.handle_to_dict(obj=A, kvs={"a": 1,
                                                                      "b": 2,
                                                                      "d": {
                                                                          "c": 3,
                                                                          "b": 4}})


# Generated at 2022-06-13 19:29:19.381240
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # Define a class with an __init__ method that has 3 parameters.
    class SampleClass:
        def __init__(self, p1, p2, p3):
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3

    # Create a new class that uses this init function.
    new_cls = _IgnoreUndefinedParameters.create_init(SampleClass)
    # Create an instance of the new class, using the new init function.
    obj = new_cls(42, "Foo", "Bar")
    # Check that the instance was created with the right values.
    assert obj.p1 == 42
    assert obj.p2 == "Foo"
    assert obj.p3 == "Bar"

    # Define another class with the same init function.

# Generated at 2022-06-13 19:29:26.558149
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        field: str

        def __init__(self, field: str):
            self.field = field

    # Test 1: Test with no unknown input parameters
    assert _IgnoreUndefinedParameters.handle_from_dict(TestClass,
                                                       {"field": "test"}) == {
               "field": "test"}

    # Test 2: Test with unknown input parameters
    assert _IgnoreUndefinedParameters.handle_from_dict(TestClass,
                                                       {"field": "test", "foo":
                                                           "bar"}) == {
               "field": "test"}



# Generated at 2022-06-13 19:29:40.858561
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        field1: int
        field2: int
        field3: int
        field4: int

        def __init__(self, field1, field2, field3, field4):
            pass

    init_method = _IgnoreUndefinedParameters.create_init(obj=TestClass)
    try:
        init_method(TestClass, 1, 2, 3, 4, 5, field5=6)
    except TypeError as e:
        assert "__init__() takes 4 positional arguments but 5 were given" \
               in str(e)
    init_method(TestClass, 1, 2, 3, 4, field5=6)
    init_method(TestClass, 1, 2, 3, 4)

# Generated at 2022-06-13 19:29:43.981398
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # noinspection PyProtectedMember
    assert _UndefinedParameterAction.create_init(
        obj=None).__name__ == object.__init__.__name__
    assert not hasattr(_UndefinedParameterAction.create_init(obj=None),
                       "__wrapped__")
    assert not hasattr(_UndefinedParameterAction.create_init(obj=None),
                       "__signature__")


# Unit tests for method handle_from_dict