

# Generated at 2022-06-13 19:20:40.996540
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class _CatchAllTest:
        def __init__(self, catch_all: Optional[CatchAllVar] = None):
            self.catch_all = catch_all

    catch_all = dict(a=1, b=2, c=3)
    obj = _CatchAllTest(catch_all)
    kvs = _CatchAllUndefinedParameters.handle_to_dict(obj, dict())

    assert dict(a=1, b=2, c=3) == kvs

# Generated at 2022-06-13 19:20:49.838092
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from dataclasses_json.undefined import Undefined

    @dataclass_json(undefined=Undefined.EXCLUDE)
    @dataclass
    class A:
        x: int
        y: int

    input_dict = {"x": 1, "y": 2, "z": 3}
    a = A.from_dict(input_dict)
    json_dict = a.to_dict()
    assert input_dict == json_dict

# Generated at 2022-06-13 19:21:01.346342
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class Sample:
        a: str
        b: str = "b"
        c: Optional[CatchAllVar]


# Generated at 2022-06-13 19:21:10.432365
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    defined_parameters = {
        "foo": 2
    }
    num_undefined_parameters = 4
    num_parameters_in_init = len(defined_parameters) + num_undefined_parameters

    class _TestClass:
        def __init__(self, foo: int, bar: str, baz: Tuple[str, int],
                     **undefined_parameters):
            pass

        def foo(self) -> int:
            return self.foo

        def bar(self) -> str:
            return self.bar

        def baz(self) -> Tuple[str, int]:
            return self.baz

    num_args = 3
    num_kwargs = 3
    num_positional_takeable = num_parameters_in_init - num_args - num_kwargs

    #

# Generated at 2022-06-13 19:21:20.296620
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    catch_all_field = Field(
        name="catch_all",  # type: ignore
        type=Optional[CatchAllVar],
        default=None,
        init=True,
        default_factory=dict
    )
    assert _CatchAllUndefinedParameters.handle_from_dict(
        cls=type("L", (object,), {
            "__annotations__": {"catch_all": Optional[CatchAllVar]},
            "catch_all": Field(
                name="catch_all",
                type=Optional[CatchAllVar],
                default=None,
                init=True,
                default_factory=dict
            )
        }),
        kvs={}) == {"catch_all": {}}

# Generated at 2022-06-13 19:21:27.218370
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    Dummy = dataclasses.make_dataclass("Dummy", [("x", int)])
    assert _CatchAllUndefinedParameters.handle_from_dict(Dummy, {"x": 1}) \
           == {"x": 1}

    CatchAllDummy = dataclasses.make_dataclass("CatchAllDummy",
                                               [("x", int),
                                                ("y", Optional[CatchAll])])
    assert _CatchAllUndefinedParameters.handle_from_dict(CatchAllDummy,
                                                         {"x": 1}) \
           == {"x": 1, "y": {}}

# Generated at 2022-06-13 19:21:39.044857
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Test:
        x: str
        y: str
        z: str
        ignore: UnknownParameters = dataclasses.field(
            default_factory=dict)

    obj = Test(x="x", y="y", z="z", ignore={"a": "a", "b": "b"})
    kvs = {"x": obj.x, "y": obj.y, "z": obj.z, "ignore": obj.ignore}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    expected = {"x": "x", "y": "y", "z": "z", "a": "a", "b": "b"}
    assert result == expected


# Generated at 2022-06-13 19:21:40.572982
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Test for _UndefinedParameterAction.handle_dump
    """
    assert _UndefinedParameterAction.handle_dump(None) == {}



# Generated at 2022-06-13 19:21:41.409465
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    ...

# Generated at 2022-06-13 19:21:49.910144
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class BooleanExample:
        x: int
        y: int

    assert \
        {'x': 1, 'y': 2} == \
        _RaiseUndefinedParameters.handle_from_dict(
            BooleanExample, {'x': 1, 'y': 2})

    try:
        _RaiseUndefinedParameters.handle_from_dict(
            BooleanExample, {'x': 1, 'y': 2, 'z': 3})
        assert False
    except UndefinedParameterError:
        assert True



# Generated at 2022-06-13 19:22:08.236189
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, t: int, b: int, p3):
            self.t = t
            self.b = b
            self.p3 = p3

        def __eq__(self, other):
            return isinstance(other, TestClass) and \
                   self.t == other.t and self.b == other.b

    kvs = {'t': 1, 'b': 2, 'not_part_of_class': 3}
    result = _CatchAllUndefinedParameters.handle_to_dict(TestClass, kvs)
    assert result == {'t': 1, 'b': 2}

    instance = TestClass(t=1, b=2, p3=3)
    kvs = _CatchAllUndefinedParameters.handle_dump(instance)
    assert k

# Generated at 2022-06-13 19:22:16.325876
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class TestClass1:
        def __init__(self, known_parameter):
            pass

    class TestClass2:
        def __init__(self, known_parameter):
            pass

    class TestClass3:
        def __init__(self, known_parameter):
            pass

    class TestClass4:
        def __init__(self, known_parameter):
            pass

    class TestClass5:
        def __init__(self, known_parameter):
            pass

    class TestClass6:
        def __init__(self, known_parameter):
            pass

    class TestClass7:
        def __init__(self, known_parameter):
            pass

    kv_pairs1 = {'known_parameter': 123}

# Generated at 2022-06-13 19:22:20.340545
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class _TestClass:
        pass

    t = _TestClass()
    t.CatchAll = {"x": "y"}
    result = _CatchAllUndefinedParameters.handle_to_dict(t,
                                                         {"greek": "alpha"})
    assert result["greek"] == "alpha"
    assert result["x"] == "y"
    assert len(result) == 2

# Generated at 2022-06-13 19:22:25.862046
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class ClassWithCatchAll:
        def __init__(self, a,
                     b: CatchAll = None):
            self.a = a
            self.b = b

    class ClassWithoutCatchAll:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    # Expected results
    expect_dict_from_dict_class_with_catch_all = {'a': 1, 'b': {
        'c': 3, 'd': 4}}
    expect_dict_from_dict_class_without_catch_all = {'a': 1}

    # Test from_dict on class with catch-all
    kvs_from_dict_class_with_catch_all = {'a': 1, 'c': 3, 'd': 4}
    result_from

# Generated at 2022-06-13 19:22:36.222558
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json import DataclassJsonMixin

    class MyClass(DataclassJsonMixin):
        @classmethod
        def from_dict(cls, kvs: Dict[Any, Any]):
            known = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
            return MyClass(**known)

        def __init__(self, my_param: Optional[int] = None,
                     **kwargs: CatchAllVar):
            self.my_param = my_param
            self.kwargs = kwargs

    catch_all = _CatchAllUndefinedParameters._get_catch_all_field(MyClass)
    assert catch_all.name == "kwargs"
    assert catch_all.type == Optional[CatchAllVar]

    v = MyClass

# Generated at 2022-06-13 19:22:40.091751
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    unique_error_msg = "unique error message"
    try:
        raise UndefinedParameterError(unique_error_msg)
    except UndefinedParameterError as e:
        assert e.args[0] == unique_error_msg

# Generated at 2022-06-13 19:22:49.423812
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class Dummy:
        pass

    @dataclasses.dataclass
    class TestData:
        a: str
        b: Optional[str] = dataclasses.field(default=None)
        c: Optional[str] = dataclasses.field(default="x")
        d: CatchAll = dataclasses.field(default_factory=dict)

        def __init__(self, **kwargs):
            unknown = _CatchAllUndefinedParameters.handle_from_dict(self,
                                                                    kwargs)
            super().__init__(**unknown)

    # Test 1: no catch-all, no unknown parameters
    test = TestData(a="a")
    assert test.a == "a"
    assert test.b is None
    assert test.c == "x"
    assert test.d

# Generated at 2022-06-13 19:23:00.010373
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import pytest
    from marshmallow import fields
    from marshmallow.validate import Range

    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str = "a"
        c: Any = None
        d: Optional[str] = None

    def test_init(self, *, a: int, b: str, c: Any, d: Optional[str]):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    TestClass.__init__ = test_init

    args = [1, 2, 3, 4]

# Generated at 2022-06-13 19:23:06.596418
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        defined: int
        optional: Optional[int]
        catch_all: Optional[CatchAllVar] = None

    TestClass._init_ = _CatchAllUndefinedParameters.create_init(TestClass)

    TestClass(defined=1)
    TestClass(defined=1, other_defined=2)
    TestClass(defined=1, catch_all={})
    TestClass(defined=1, other_defined=2, catch_all={})
    TestClass(defined=1, other_defined=2, catch_all={})
    try:
        TestClass(defined=1, catch_all={'defined': 2})
        assert False, 'Should have raised'
    except UndefinedParameterError:
        pass

# Generated at 2022-06-13 19:23:11.001177
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    obj = CatchAllClass(**{"defined": "defined", "undefined": "undefined"})
    assert _CatchAllUndefinedParameters.handle_dump(obj) == {"undefined": "undefined"}



# Generated at 2022-06-13 19:23:45.710954
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, b: str, _catchall: Optional[CatchAllVar]):
            self.b = b
            self.other = _catchall

    a = A("testb", {"test": "test"})
    kvs = {"b": "testb", "_catchall": {"test": "test"}}
    result = _CatchAllUndefinedParameters.handle_to_dict(a, kvs)
    assert isinstance(result, dict)
    assert result == {"b": "testb", "test": "test"}



# Generated at 2022-06-13 19:23:48.629074
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class IgnoreUndefinedParametersTestClass:
        pass
    v = {'name': 'foo', '_UNKNOWN0': 1, '_UNKNOWN1': 2}
    obj = IgnoreUndefinedParametersTestClass()

    assert _UndefinedParameterAction.handle_to_dict(obj, v) == v


# Generated at 2022-06-13 19:23:55.545249
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():

    kvs = {"a": 1,
           "b": 2,
           "c": 3,
           "d": 4,
           "e": 5,
           "f": 6}

    class TestClass():
        a: int = None
        b: int = None

        @classmethod
        def init(cls, *args, **kws):
            cls(*args, **kws)

    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {"a": 1, "b": 2}



# Generated at 2022-06-13 19:23:59.528825
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str = ""
        c: Optional[CatchAllVar] = None

        def __init__(self, a: int, b: str = "",
                     c: Optional[CatchAllVar] = None):
            pass

    init = _CatchAllUndefinedParameters.create_init(TestClass)
    _ = TestClass(1, "b", {})
    _ = TestClass(1, "b", _UNKNOWN7="u", c={"d": "e"})

# Generated at 2022-06-13 19:24:11.058567
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestEntity:
        def __init__(self, int_field: int, catch_all: CatchAll):
            self.int_field = int_field
            self.catch_all = catch_all

        def __eq__(self, other):
            return self.int_field == other.int_field and self.catch_all == other.catch_all

    parameter_dict = {"int_field": 1, "nothing_defined": "value"}
    expected = TestEntity(1, parameter_dict)

    actual_dict = parameter_dict.copy()
    actual_dict.update(expected.catch_all)

    actual = TestEntity(**parameter_dict)
    actual_dict = _CatchAllUndefinedParameters.handle_to_dict(
        expected, actual_dict)

    expected_dict = actual_dict.copy()

# Generated at 2022-06-13 19:24:16.392712
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, a):
            self.a = a

    parameters = {"a": 1, "b": 2, "c": 3}
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        Foo, parameters)
    assert len(unknown) == 2, f"This should be two: {unknown}"
    assert len(known) == 1, f"This should be one: {known}"
    # This should not raise an error
    _IgnoreUndefinedParameters.handle_from_dict(Foo, parameters)



# Generated at 2022-06-13 19:24:26.577430
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class _MockSchema:
        pass

    schema = _MockSchema()
    schema.dump_unknown = 'never'
    undefined_parameter_handler = _IgnoreUndefinedParameters

    # Expected behavior for INCLUDE
    field_names = ["name", "age", "catch_all"]
    class_fields = [Field(name=name, type=Optional[CatchAll]) for name in
                    field_names]
    assert undefined_parameter_handler.handle_to_dict(
        class_fields, {"age": 18, "catch_all": {"eyes": "blue"}}) == {
               "age": 18}
    assert undefined_parameter_handler.handle_dump(
        class_fields) == {
               "catch_all": {}}
    assert undefined_parameter_handler.handle_to_

# Generated at 2022-06-13 19:24:36.398659
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json.utils import CatchAllVar


    @dataclasses.dataclass(frozen=True)
    class FrozenCatchAll:
        _unknown: CatchAllVar = dataclasses.field(default_factory=dict)


    @dataclasses.dataclass
    class MutableCatchAll:
        _unknown: CatchAllVar = None


    FrozenCatchAll_expected = {'_unknown': {}}
    FrozenCatchAll_test_data = [
        dict(),
        dict(_unknown={}),
        dict(_unknown={'foo': 'bar'}),
        dict(foo='bar', _unknown={'baz': 'qux'})
    ]
    MutableCatchAll_expected = {'_unknown': {'foo': 'bar'}}
    MutableCatchAll_

# Generated at 2022-06-13 19:24:46.416801
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from typing import Optional


    @functools.wraps(_IgnoreUndefinedParameters.create_init)
    def create_init_ignore(*args, **kwargs) -> Callable:
        return _IgnoreUndefinedParameters.create_init(*args, **kwargs)


    @functools.wraps(_CatchAllUndefinedParameters.create_init)
    def create_init_catch_all(*args, **kwargs) -> Callable:
        return _CatchAllUndefinedParameters.create_init(*args, **kwargs)


    class TestIgnore:
        def __init__(self, a: int, b: str, c: Optional[str] = None,
                     d: Optional[str] = None):
            self.a = a
            self.b = b
            self.c = c

# Generated at 2022-06-13 19:24:56.684289
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import typing

    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int
        c: typing.Optional[CatchAllVar]

    known_given_parameters, unknown_given_parameters = \
        _CatchAllUndefinedParameters.handle_from_dict(
            TestClass, {'a': 3, 'b': 2, 'c': {'d': 1, 'e': 2}})
    assert known_given_parameters == {'a': 3, 'b': 2, 'c': {'d': 1, 'e': 2}}
    assert unknown_given_parameters == {}

# Generated at 2022-06-13 19:25:50.855183
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    default_value = {}
    for action_cls in (Undefined.INCLUDE.value, Undefined.EXCLUDE.value,
                       Undefined.RAISE.value):
        assert action_cls.handle_dump(cls=None) == default_value

# Generated at 2022-06-13 19:26:00.223268
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Test that the created init method behaves in the same way as the original
    __init__ method, but ignores all additional parameters that are not
    defined in the dataclass.
    """

    # Define a dummy dataclass to test the init
    @dataclasses.dataclass
    class DummyClass:
        a: int
        b: int

        def __init__(self, a: int, b: int):
            self.a, self.b = a, b

    dummy = DummyClass(10, 20)
    dummy_dict = dataclasses.asdict(dummy)
    assert dummy_dict == {'a': 10, 'b': 20}, "dummy_dict must match."

    # Make a copy with fake init and check if it creates a copy of dummy_dict
    IgnoredDummyClass = _

# Generated at 2022-06-13 19:26:09.059376
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Test:
        def __init__(self, a: int, b: int, c: int,
                     d: CatchAllVar = None):
            print(a)
            print(b)
            print(c)
            print(d)

    init_without_catch_all_field = Test.__init__
    init_with_catch_all_field = _CatchAllUndefinedParameters.create_init(
        Test)

    # Check that all parameters are passed when no undefined parameters are
    # supplied
    b = 1
    c = 2
    init_with_catch_all_field(Test, 0, b=b, c=c)
    init_without_catch_all_field(Test, 0, b=b, c=c)

    # Check that undefined parameters are taken into account for parameter
    # count
   

# Generated at 2022-06-13 19:26:17.278173
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import dataclasses
    import pytest

    @dataclasses.dataclass
    class InvalidCatchAll:
        defined: str
        non_default_given: Optional[str] = dataclasses.field(
            default=None)
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default={"some_key": "some_value"})

    @dataclasses.dataclass
    class ValidCatchAll:
        defined: str
        non_default_given: Optional[str] = dataclasses.field(
            default=None)
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default=None)

    @dataclasses.dataclass
    class ValidCatchAllWithDefaultFactory:
        defined: str
        non_default_

# Generated at 2022-06-13 19:26:26.896973
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Test:
        @dataclasses.dataclass
        class Test:
            foo: int
            bar: int
            baz: Optional[CatchAll] = None

    test = Test.Test(1, 2, {"bla": 1, "blub": 2})
    expected = {
        "foo": 1,
        "bar": 2,
        "bla": 1,
        "blub": 2
    }
    actual = _CatchAllUndefinedParameters.handle_to_dict(test, {
        "foo": 1,
        "bar": 2,
        "baz": {"bla": 1, "blub": 2}
    })
    assert actual == expected



# Generated at 2022-06-13 19:26:37.537392
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from dataclasses_json._utils import CatchAllVar


    class MyClass:
        def __init__(self, x: str, y: str = "foo", z: str = "bar"):
            pass


    _IgnoreUndefinedParameters.create_init(MyClass)

    class MyClass:
        def __init__(self, x: str, *args, **kwargs):
            self.x = x


    _IgnoreUndefinedParameters.create_init(MyClass)

    class MyClass:
        def __init__(self, x: str, y: str = "foo", z: str = "bar"):
            pass


    _CatchAllUndefinedParameters.create_init(MyClass)


# Generated at 2022-06-13 19:26:45.091670
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Foo:
        def __init__(self, a, b, c=3, **kwargs):
            self.a = a
            self.b = b
            self.c = c
            self.kwargs = kwargs

    obj = Foo(1, 2, c=4, d=5)
    representation = _UndefinedParameterAction.handle_to_dict(
        obj=obj, kvs={
            "a": obj.a,
            "b": obj.b,
            "c": obj.c,
            "kwargs": {
                "d": 5
            }})
    assert representation == {"a": 1, "b": 2, "c": 4, "d": 5}

# Generated at 2022-06-13 19:26:52.322044
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # Need to be aware that some of this is tested
    # indirectly through test_undefined_parameters.py

    class Foo:
        def __init__(self, a=1, b=2, d=3, **unknown):
            pass

    init = _CatchAllUndefinedParameters.create_init(Foo)
    assert init is not Foo.__init__

    f1 = Foo()
    init(f1)

    f2 = Foo(a=5, b=5, c=5)
    init(f2)

    f3 = Foo(a=5, b=5, c=5, known=5)
    with pytest.raises(UndefinedParameterError):
        init(f3)

    class Bar:
        def __init__(self, a, b=2, **unknown):
            pass



# Generated at 2022-06-13 19:26:59.127726
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from .utils import to_dict
    from .core import Field
    from .api import from_dict

    @dataclasses.dataclass
    class A:
        a: int
        b: str
        c: CatchAll

    a = from_dict(A, {"a": 1, "b": "b", "d": 2, "e": "e"},
                  undefined=Undefined.INCLUDE)
    assert a.a == 1
    assert a.b == "b"
    assert a.c == {"d": 2, "e": "e"}

    b = to_dict(a, undefined=Undefined.INCLUDE)
    assert b == {"a": 1, "b": "b", "d": 2, "e": "e"}

    # Test dumping

# Generated at 2022-06-13 19:26:59.688789
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    pass

# Generated at 2022-06-13 19:29:35.356353
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class MyClass:
        def __init__(self, known):
            self.known = known

    kvs = {"known": "value"}
    returned_kvs = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert returned_kvs == kvs

    kvs = {"known": "value", "unknown": "value"}
    try:
        _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
    except UndefinedParameterError:
        return

    assert False, "Expected an exception to be raised"


# Generated at 2022-06-13 19:29:47.170694
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from typing import Optional


    class A:
        def __init__(self, a, b, c: Optional[CatchAll] = None):
            self.a = a
            self.b = b
            self.c = c


    params = _CatchAllUndefinedParameters.handle_from_dict(A,
                                                           {"a": "a", "b": "b"})
    assert params["a"] == "a"
    assert params["b"] == "b"
    assert isinstance(params["c"], dict)
    assert params["c"] == {}

    params = _CatchAllUndefinedParameters.handle_from_dict(A,
                                                           {"a": "a", "b": "b",
                                                            "c": "wrong"})
    assert params["a"] == "a"


# Generated at 2022-06-13 19:29:57.319881
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Base:
        a: str
        b: str
        c: str

    @dataclasses.dataclass
    class MyClass(_UndefinedParameterAction, Base):
        a = dataclasses.field(default="a")
        b = dataclasses.field(default="b")
        c = dataclasses.field(default="c")

    @dataclasses.dataclass
    class MyClass1(MyClass, Base):
        pass

    @dataclasses.dataclass
    class MyClass2(MyClass, Base):
        b = dataclasses.field(metadata={"ignore_in_to_dict": False})

    @dataclasses.dataclass
    class MyClass3(MyClass, Base):
        b = dataclasses.field(metadata={"ignore_in_dump": False})

   

# Generated at 2022-06-13 19:29:59.867134
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    err = UndefinedParameterError()
    assert isinstance(err, ValidationError)

# Generated at 2022-06-13 19:30:09.045770
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import dataclasses
    import inspect
    import io
    import textwrap
    import tokenize

    # pylint: disable=unused-import
    import tokenize  # noqa

    # pylint: disable=unused-import
    import tokenize  # noqa

    # define the dataclass that we want to check
    @dataclasses.dataclass
    class Example:
        """
        This class is used to test the initialization of dataclasses
        with undefined parameters
        """

        defined_parameter: str = ""
        catch_all: Optional[CatchAllVar] = None

        def __init__(
                self, defined_parameter: str = "",
                catch_all: Optional[CatchAllVar] = None):
            pass

    # we are going to set up a test case that will call

# Generated at 2022-06-13 19:30:14.558246
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class NoCatchAll:
        def __init__(self, a=1, b=2, c=3, _UNKNOWN0=None, _UNKNOWN1=None,
                     _NOTUNKNOWN=None):
            pass

    init_ignored = _IgnoreUndefinedParameters.create_init(NoCatchAll)
    constructor_ignored = init_ignored(NoCatchAll, 1, 2, 3)
    assert constructor_ignored is None

    class CatchAll:
        def __init__(self, a=1, b=2, c=3, _UNKNOWN0=None, _UNKNOWN1=None,
                     _NOTUNKNOWN=None, **kwargs: CatchAll):
            pass

    init_ignored = _CatchAllUndefinedParameters.create_init(CatchAll)

# Generated at 2022-06-13 19:30:30.112057
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    test_class = type("TestClass", (), {
        "_dataclass_json": {
            "undefined": Undefined.INCLUDE
        }
    })

    test_init = _UndefinedParameterAction.create_init(test_class)

    @dataclasses.dataclass
    class SomeTestClass(test_class):
        catch_all: Optional[CatchAllVar]
        defined: str = "default"

        def __init__(self, defined: str, catch_all: CatchAllVar,
                     undefined_1: int,
                     undefined_2: bool):
            super().__init__()

    actual_test_class = SomeTestClass(defined="test", catch_all={},
                                      undefined_1=1, undefined_2=True)

    assert actual_test_class.defined == "test"