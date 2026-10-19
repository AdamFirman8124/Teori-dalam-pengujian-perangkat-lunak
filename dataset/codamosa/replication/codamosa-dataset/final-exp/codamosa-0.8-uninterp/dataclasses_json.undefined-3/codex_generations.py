

# Generated at 2022-06-13 19:20:49.838417
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class TestClass:
        a: int
        b: int = 0
        c: int = 0

        def __init__(self, a: int, b: int, c: int = 0):
            self.a = a
            self.b = b
            self.c = c

    cls = TestClass
    init_function = _IgnoreUndefinedParameters.create_init(cls)
    # noinspection PyTypeChecker
    init_function(cls, 1, 2, 3, e=5)
    assert cls.a == 1
    assert cls.b == 2
    assert cls.c == 3

# Generated at 2022-06-13 19:20:58.633955
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass
    class Test:
        a: int
        b: int
        c: int
        d: int

        def __init__(self, a, b, c, d):
            pass

    init = _IgnoreUndefinedParameters.create_init(Test)
    assert init.__name__ == "__init__"

    t = Test(a="", b="", c="", d="")
    assert inspect.signature(t.__init__) == inspect.signature(init)

# Generated at 2022-06-13 19:21:02.093615
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # noinspection PyMissingOrEmptyDocstring

    class Test:
        def __init__(self, test_parameter, ignore, **_) -> None:
            pass

    obj = Test(test_parameter=1, ignore=2)
    assert obj is not None  # to make sure it's called



# Generated at 2022-06-13 19:21:09.138935
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # define some fixture data:
    class_definition = dataclasses.make_dataclass("MyClass",
                                                  [("name", str),
                                                   ("age", int),
                                                   ("height", int)])
    kwargs = {"name": "John", "age": 23, "height": 182, "extra": "value"}
    # define a mock object for the method under test:
    mock_init = _IgnoreUndefinedParameters.create_init(class_definition)

    # act
    mock_init(class_definition, **kwargs)

    # assert
    assert True



# Generated at 2022-06-13 19:21:16.403685
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass
    from dataclasses_json import config

    @dataclass
    class Test:
        test: str = "test"

        @classmethod
        def new(cls, **kwargs) -> "Test":
            return cls(**config.undefined.RAISE.handle_from_dict(cls, kwargs))

    assert Test.new(test="test") == Test(test="test")

    try:
        Test.new(test="test", invalid="test")
        assert False
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:21:24.670248
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Testclass:
        def __init__(self, param1: str, param2: int):
            pass

    instance1 = Testclass(param1="foo", param2=1)

    undefined_action = _RaiseUndefinedParameters()
    parameter_dict = dataclasses.asdict(instance1)
    result = undefined_action.handle_from_dict(Testclass, parameter_dict)
    assert result["param1"] == "foo"
    assert result["param2"] == 1
    try:
        undefined_action.handle_from_dict(Testclass, {"param1": "foo",
                                                      "param2": 1,
                                                      "unknown": "hey"})
    except UndefinedParameterError as e:
        print(e)



# Generated at 2022-06-13 19:21:33.010596
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class TestClass(object):
        def __init__(self, known_parameter: Any, **kwargs: Any) -> None:
            pass

    test_init_params = {"this_parameter_is_not_defined": "test"}
    test_result = _IgnoreUndefinedParameters.handle_from_dict(
        cls=TestClass, kvs=test_init_params)
    assert len(test_result) == 0



# Generated at 2022-06-13 19:21:37.045480
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = _CatchAllUndefinedParameters()
    assert obj.handle_to_dict(obj, kvs={"a": 1, "b": 2, "c": 3}) == \
           {"a": 1, "b": 2, "c": 3}



# Generated at 2022-06-13 19:21:42.337660
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class ClassWithCatchAll:
        catch_all: CatchAll = None


# Generated at 2022-06-13 19:21:55.404303
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Dummy:
        catch_all: Optional[CatchAllVar] = None
        field_1: int = 1
        field_2: str = "Test"

    class InvalidDummy(Dummy):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    class ValidDummy(Dummy):
        def __init__(self, **kwargs):
            super(__class__, self).__init__(**kwargs)

    for klass in [InvalidDummy, ValidDummy]:
        klass = _IgnoreUndefinedParameters.create_init(klass)


# Generated at 2022-06-13 19:22:15.766581
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class Test(_UndefinedParameterAction):
        a: int
        b: float

        # classmethod because python doesn't allow staticmethods
        # in the body of a class
        @classmethod
        def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
            return super().handle_from_dict(cls, kvs)

    # Test combination of parameters
    dictionary_with_both = {"a": 4, "b": 4.5}
    dictionary_with_one = {"a": 4}
    dictionary_with_none = {}

    assert Test.handle_from_dict(Test, dictionary_with_both) == {
        'a': 4, 'b': 4.5}

# Generated at 2022-06-13 19:22:22.133872
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class SimpleExample:
        def __init__(self, a: int, b: int):
            pass

    kvs = {"a": 1, "b": 2}
    parameters = _RaiseUndefinedParameters.handle_from_dict(
        cls=SimpleExample, kvs=kvs)
    assert parameters == kvs

    kvs = {"a": 1, "b": 2, "c": 3}
    caught_error = False
    try:
        _RaiseUndefinedParameters.handle_from_dict(
            cls=SimpleExample, kvs=kvs)
    except UndefinedParameterError:
        caught_error = True
    assert caught_error



# Generated at 2022-06-13 19:22:28.233696
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    res = _UndefinedParameterAction.handle_dump(None)
    assert res == {}

# Generated at 2022-06-13 19:22:31.958165
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError(message="test_message")
    except UndefinedParameterError as err:
        assert isinstance(err.messages, list)
        assert "test_message" in err.messages
    else:
        raise AssertionError

# Generated at 2022-06-13 19:22:43.663090
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import random
    from dataclasses import dataclass


    def random_ordered_dict() -> Dict[str, Any]:
        number_of_items = random.randint(1, 21)
        kvs = {f"ARG{i}": i for i in range(number_of_items)}
        return kvs


    @dataclass
    class TestClass:
        field1: int
        field2: int
        field3: int
        field4: int

        def __init__(self, field1, field2, field3, field4):
            self.field1 = field1
            self.field2 = field2
            self.field3 = field3
            self.field4 = field4


    def test_init(cls, *args, **kwargs):
        init = _IgnoreUnd

# Generated at 2022-06-13 19:22:51.056603
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import dataclasses

    import pytest
    @dataclasses.dataclass
    class Example:
        a: int
        b: int
        c: int

    obj = Example(a=1, b=2, c=3)
    catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(obj)

# Generated at 2022-06-13 19:23:01.561584
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # base case:

    class _MockObject:
        def __init__(self, param1: str, param2: str, param3: str,
                     param4: CatchAll = {}) -> None:
            pass

    mock_init = _UndefinedParameterAction.create_init(_MockObject)
    # noinspection PyTypeChecker
    mock_object = _MockObject(param1="test1", param2="test2", param3="test3",
                              param5="test5")
    assert isinstance(mock_object, _MockObject)
    assert inspect.signature(mock_object.__init__) == inspect.signature(
        mock_init)

    # example case:


# Generated at 2022-06-13 19:23:02.678837
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(obj=None) == {}

# Generated at 2022-06-13 19:23:09.012222
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import pytest
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: float
        c: str
        d: bool
        e: Optional[CatchAll] = None

        def __init__(self, a, b, c, d=False, e=None):
            pass

    init = _CatchAllUndefinedParameters.create_init(A)
    assert init.__name__ == "A__init__"
    a = A(1, 2, "3")
    a_with_catch_all = A(a_param=1, b=2, c="3",
                         e={"e_param": "asdf",
                            "e_param_2": 1})

# Generated at 2022-06-13 19:23:19.744923
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Foo:
        known: Optional[str] = None
        _undefined: Optional[CatchAllVar] = None

    foo = Foo(known="known")
    kvs = {'known': 'known', '_undefined': {}}
    kvs = _CatchAllUndefinedParameters.handle_to_dict(foo, kvs)
    assert kvs == {'known': 'known'}

    foo = Foo(known="known", _undefined={"unknown": None})
    kvs = {'known': 'known', '_undefined': {'unknown': None}}
    kvs = _CatchAllUndefinedParameters.handle_to_dict(foo, kvs)
    assert kvs == {'known': 'known', 'unknown': None}



# Generated at 2022-06-13 19:23:56.003630
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestCatcher:
        field: str

    @dataclasses.dataclass
    class TestCatchAll:
        field: str = "default"
        catch_all: CatchAll = None

    # Test with no undefined parameters
    assert TestCatcher == _CatchAllUndefinedParameters.handle_from_dict(
        cls=TestCatcher, kvs={"field": "hello"})

    # Test with no undefined parameters with defaults
    assert TestCatchAll == _CatchAllUndefinedParameters.handle_from_dict(
        cls=TestCatchAll, kvs={"field": "hello"})

    # Test with one undefined parameter
    assert {
               "field": "hello",
               "catch_all": {"catchall_field": "hello"}
           } == _

# Generated at 2022-06-13 19:24:12.157415
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass():
        def __init__(self, x, y=None):
            self.x = x
            self.y = y

    kvs = {"x": 1, "y": 2}
    new_kvs = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=TestClass, kvs=kvs
    )
    assert new_kvs == ({"x": 1, "y": 2}, {})

    kvs = {"x": 1, "y": 2, "z": 3}
    new_kvs = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=TestClass, kvs=kvs
    )
    assert new_kvs == ({"x": 1, "y": 2}, {"z": 3})


# Generated at 2022-06-13 19:24:13.649321
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:24:20.425999
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():

    kv_dict = {'a': 1, 'b': 2, 'c': 3}

    assert _IgnoreUndefinedParameters.handle_from_dict(object, {'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _IgnoreUndefinedParameters.handle_from_dict(object, kv_dict) == {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-13 19:24:29.480290
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import datetime
    import unittest.mock

    class Dataclass(metaclass=dataclasses.dataclass):
        a: int = 1
        b: str = "b"
        c: datetime.time = datetime.time(12)

    class DataclassWithCatchAll(metaclass=dataclasses.dataclass):
        a: int = 1
        b: str = "b"
        c: datetime.time = datetime.time(12)
        catch_all: CatchAll = None

    data_1 = Dataclass(
        a=1, b="b", c=datetime.time(12),
        _UNKNOWN0="some other arg")

# Generated at 2022-06-13 19:24:38.454658
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    """
    Test the function that handles undefined parameters for the
    case where a Catch-All dictionary is provided.

    :return:
    """
    @dataclasses.dataclass
    class TestClass:
        foo: int
        bar: Optional[str]
        unknown: Optional[CatchAllVar]

    no_unknown = TestClass(foo=5, bar="bla", unknown=None)
    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                         dataclasses.asdict(
                                                             no_unknown)) == {
               "foo": 5, "bar": "bla", "unknown": {}}

    a_unknown = TestClass(foo=5, bar="bla", unknown={"a": "a"})
    assert _CatchAllUndefinedParameters.handle_from_dict

# Generated at 2022-06-13 19:24:47.548902
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # case: correct input

    # noinspection PyPep8Naming
    class TestClassA:
        def __init__(self, a: int, b: str, *, c: int, d: str, e: int = 1,
                     f: str = "", g: int, h: str):
            pass

    new_init = _IgnoreUndefinedParameters.create_init(TestClassA)
    assert new_init(TestClassA, 1, "foo", c=2, d="bar", g=3, h="baz") \
        is TestClassA(1, "foo", c=2, d="bar", e=1, f="", g=3, h="baz")

    # case: too many normal arguments
    #   -> result of this should be a TypeError


# Generated at 2022-06-13 19:24:57.694709
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import marshmallow as mm

    class Schema1(mm.Schema):
        a = mm.fields.Int(required=True)

    class Schema2(mm.Schema):
        a = mm.fields.Int(required=True)
        b = mm.fields.Int(required=True)

    class TestClass:
        def __init__(self, a, b=20):
            self.a = a
            self.b = b

        def __repr__(self):
            return f'<{self.__class__.__name__}(a={self.a}, b={self.b})>'

    class TestClass2:
        def __init__(self, a, b=20):
            self.a = a
            self.b = b

        def __repr__(self):
            return f

# Generated at 2022-06-13 19:25:03.716043
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from typing import Any, Dict, TypeVar

    T = TypeVar("T", bound="_Test")

    class _Test:
        attr: str
        _undefined_parameter_action = _UndefinedParameterAction

        def __init__(self, attr: str) -> None:
            self.attr = attr

    _Test.__init__ = _UndefinedParameterAction.create_init(_Test)

    assert _Test("test").attr == "test"
    with pytest.raises(TypeError):
        _Test()



# Generated at 2022-06-13 19:25:10.616330
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclass
    class _TestClass:
        catch_all: CatchAll = dataclasses.field(
            default_factory=dict)

    simple_test_dict = {"catch_all": "test"}
    known_test_dict, unknown_test_dict = \
        _CatchAllUndefinedParameters.handle_from_dict(
            _TestClass, simple_test_dict)
    assert known_test_dict == simple_test_dict
    assert unknown_test_dict == {}

    replace_default_dict = {"catch_all": {"existing": "test"}}
    known_replace_default_dict, unknown_replace_default_dict = \
        _CatchAllUndefinedParameters.handle_from_dict(
            _TestClass, replace_default_dict)
    assert known_replace_default_dict == replace_

# Generated at 2022-06-13 19:26:09.168527
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class MyClass:
        def __init__(self, a: int, b: int):
            pass

    test_parameters = dict(a=-1, b=2, c=3)

    output = _IgnoreUndefinedParameters.handle_from_dict(MyClass,
                                                         test_parameters)
    assert output == dict(a=-1, b=2)

# Generated at 2022-06-13 19:26:16.650525
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.utils import CatchAllVar


    @dataclasses.dataclass
    class TestClass:
        catch_all: Optional[CatchAllVar] = None
        field1: str
        field2: str


    tc = TestClass(**{'field1': 'hello', 'field2': 'world', 'field3': 'hi'})
    dump = tc.__dict__.copy()
    dump = _CatchAllUndefinedParameters.handle_to_dict(tc, dump)
    assert(dump['catch_all'] == {"field3": "hi"})


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 19:26:22.323395
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class TestClass:
        def __init__(self, a, b, c=None, d=None, e=None):
            pass

    # noinspection PyTypeChecker
    init = _IgnoreUndefinedParameters.create_init(TestClass)
    init(TestClass, 1, 2, 3, 4, 5, e=6, g=7)

# Generated at 2022-06-13 19:26:23.323893
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("Test")

# Generated at 2022-06-13 19:26:26.750359
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class ParameterTestClass:
        def __init__(self, first_name: str):
            self.first_name = first_name

    instance = ParameterTestClass("Basti")

    fields = _UndefinedParameterAction.handle_dump(instance)
    assert fields == {}

# Generated at 2022-06-13 19:26:37.468901
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestCls:
        def __init__(self, arg1: str, arg2: int = 1, arg3: str = "3",
                     arg4: int = 4):
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = arg3
            self.arg4 = arg4

    kvs = {"arg1": "1", "arg2": 2, "arg3": "3", "arg5": 5}
    result = _RaiseUndefinedParameters.handle_from_dict(TestCls, kvs)
    expected = {"arg1": "1", "arg2": 2, "arg3": "3", "arg4": 4}
    assert result == expected
    assert len(result) == len(expected)


# Generated at 2022-06-13 19:26:47.774407
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Test(metaclass=abc.ABCMeta):
        def __init__(self, a, b):
            pass
    assert isinstance(Test, abc.ABCMeta)
    assert isinstance(Test, abc.ABC)
    known, unknown = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=Test, kvs={"a": 1, "b": 2, "c": 3})
    assert known == {"a": 1, "b": 2}
    assert unknown == {"c": 3}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(cls=Test, kvs=known)

    assert _IgnoreUndefinedParameters.handle_from_dict(cls=Test, kvs=known) == known

# Generated at 2022-06-13 19:26:53.807529
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    dict1 = {'1': 1, '2': 2}
    dict2 = {'3': 3}
    dict_combined = {**dict1, **dict2}
    assert _UndefinedParameterAction.handle_to_dict(obj=None, kvs=dict1
                                                    ) == dict1
    assert _UndefinedParameterAction.handle_to_dict(obj=None, kvs=
    {**dict1, **dict2}) == dict_combined



# Generated at 2022-06-13 19:26:59.894555
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():

    @dataclasses.dataclass(frozen=True)
    class ClassWithCatchAll:
        field1: int
        field2: float
        _undefined: Optional[CatchAllVar] = dataclasses.field(
            # TODO: We have to pass an instance for mypy to infer the type.
            # Once mypy supports PEP 563 this can be fixed.
            metadata={"marshmallow_field": dataclasses_json.CatchAll})

    kvs = {"field1": 1, "field2": 1., "field3": 1}
    ClassWithCatchAll._CatchAllUndefinedParameters._get_catch_all_field(
        ClassWithCatchAll)

# Generated at 2022-06-13 19:27:06.056593
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class _TestClass:
        def __init__(self, param1, param2):
            pass

    try:
        _UndefinedParameterAction.handle_from_dict(
            _TestClass,
            {
                "param1": 1,
                "param2": 2,
                "param3": 3,
            }
        )
    except Exception as e:
        assert type(e) == NotImplementedError
    else:
        raise AssertionError("Expected exception to be raised")


# Generated at 2022-06-13 19:29:28.598943
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass()
    class Test:
        attr1: int
        attr2: int
        _catch_all_field: Optional[CatchAllVar] = dataclasses.field(
            default=dataclasses.field(  # type: ignore
                default_factory=CatchAllVar),
            metadata={"marshmallow_field": dataclasses_json.fields.CatchAll})

    tc = Test(1, 2)
    kvs = {"attr1": 1, "_UNKNOWN3": 3}
    expected = {"attr1": 1, "_catch_all_field": {"_UNKNOWN3": 3}}
    result = _CatchAllUndefinedParameters.handle_from_dict(Test, kvs)
    assert expected == result



# Generated at 2022-06-13 19:29:40.790171
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from typing import Dict


    class Foo:
        def __init__(self, known: int = 0, unknown: int = 1) -> None:
            self.known = known
            self.unknown = unknown


    kvs: Dict[str, int] = {"known": 1}
    known = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    assert known == {"known": 1}

    with pytest.raises(UndefinedParameterError):
        kvs = {"known": 1, "unknown": 1}
        known = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)



# Generated at 2022-06-13 19:29:50.283240
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import json
    from dataclasses_json.api import load, dump
    from dataclasses_json.undefined import Undefined

    @dataclasses.dataclass
    class _TestClass:
        value: int
        value2: int
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)

    # Initialize an instance with one defined parameter and one undefined
    obj = load(_TestClass, {"value": 1,
                            "value2": 2,
                            "hello": "world"})
    # This should not throw an error
    dump(obj)
    # obj.hello should be gone (but we cannot check this)

# Generated at 2022-06-13 19:29:52.480454
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    with pytest.raises(UndefinedParameterError,
                       match="This is a test error message"):
        raise UndefinedParameterError("This is a test error message")



# Generated at 2022-06-13 19:29:53.992285
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:30:03.786306
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class ExampleClass:
        def __init__(self, field1, field2):
            pass


    # Test 1
    expected = {"field1": "test", "field2": True}
    res = _UndefinedParameterAction.handle_from_dict(
        cls=ExampleClass, kvs=expected)
    assert res == expected

    # Test 2
    expected = {"field1": "test"}
    unexpected = {"field3": "unexpected"}
    res = _UndefinedParameterAction.handle_from_dict(
        cls=ExampleClass, kvs={**expected, **unexpected})
    assert res == expected, "We shouldn't find unexpected fields in the result"



# Generated at 2022-06-13 19:30:11.369574
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # Set up
    original_init = lambda test_self, x, y, z, _=None: x + y * z

    class TestClass:
        x: int = 1
        y: int = 2
        z: int = 3

        def __init__(self, x, y, z, _=None):
            self.x = x
            self.y = y
            self.z = z
            self._ = _

        def __repr__(self):
            return f"{TestClass.__name__}(x={self.x}, y={self.y}, z={self.z}, " \
                   f"_={self._})"

    test_class = TestClass(1, 2, 3)


# Generated at 2022-06-13 19:30:20.392652
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import sys

    class SubTestClass(Undefined):
        """
        Testclass for the method handle_to_dict of class
        _CatchAllUndefinedParameters.
        """

        def __init__(self, x: str, y: int = 3,
                     z: Optional[CatchAllVar] = None):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"SubTestClass({self.x}, {self.y}, {self.z})"

    sys._getframe().f_locals['SubTestClass'] = SubTestClass
    for case in (Undefined.INCLUDE, Undefined.RAISE, Undefined.EXCLUDE):
        print(f"\n{case}")
        # noinspection PyTypeChecker
        test = Sub