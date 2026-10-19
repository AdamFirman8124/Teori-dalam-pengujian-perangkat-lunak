

# Generated at 2022-06-13 19:20:51.928891
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json import dataclass, Undefined

    @dataclass
    class MyClass:
        a: int
        b: str
        c: Optional[CatchAllVar] = Undefined.INCLUDE

    assert _CatchAllUndefinedParameters.handle_from_dict(
        MyClass, {"a": 1, "b": "b"}) == {"a": 1, "b": "b", "c": {}}

    # Test with catch-all field which is already set
    assert _CatchAllUndefinedParameters.handle_from_dict(
        MyClass, {"a": 1, "b": "b", "c": {}}) == {"a": 1, "b": "b", "c": {}}


# Generated at 2022-06-13 19:20:55.841514
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class MyData:
        a: str
        b: str
        def __init__(self, a: str, b: str):
            pass

    init_method = _CatchAllUndefinedParameters.create_init(MyData)
    # noinspection PyCallingNonCallable
    init_method(MyData(1, 2), "string", "another_string")
    init_method(MyData("string", "another_string"), "string", "another_string")
    init_method(MyData("string", "another_string"), 1, 2)

# Generated at 2022-06-13 19:21:03.809352
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # noinspection PyProtectedMember
    class Test(metaclass=dataclasses.dataclass):
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    # Test 1: no parameters given, default factory run
    result1 = _CatchAllUndefinedParameters.handle_from_dict(Test, {})
    assert result1["catch_all"] == {}

    # Test 2: no parameters given, default factory run, field exists
    result2 = _CatchAllUndefinedParameters.handle_from_dict(Test,
                                                            {"catch_all": {}})
    assert result2["catch_all"] == {}

    # Test 3: no parameters given, default factory run, field supplied with
    # same value

# Generated at 2022-06-13 19:21:10.638758
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class TestClass:
        name = "test"
        catch_all: CatchAll = CatchAll

    def handle_to_dict(obj, kvs: Dict) -> Dict:
        return kvs


    def handle_dump(obj) -> Dict:
        return {}


    def handle_from_dict(cls, kvs: Dict) -> Dict:
        return kvs


    t = TestClass()
    assert handle_to_dict(obj=t, kvs={"name": "test", "catch_all": {}}) \
           == {"name": "test"}

# Generated at 2022-06-13 19:21:18.847993
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import pytest

    @dataclasses.dataclass
    class _Test:
        a: str
        b: int
        c: str

    # Check that the init signature matches the original signature
    assert _IgnoreUndefinedParameters.create_init(_Test) \
                                                .__signature__ == _Test.__init__
    # Check that invalid input leads to error
    with pytest.raises(TypeError):
        _Test(5, 1)
    # Check that valid input is accepted
    _Test("a", 5)
    # Check that undefined parameters are ignored
    _Test("a", 2, 3, "b")



# Generated at 2022-06-13 19:21:23.644730
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestClassSimpleCatchAll:
        def __init__(self, *, a: int, b: Optional[CatchAllVar] = None) -> None:
            self.a = a
            self.b = b

    class TestClassCatchAllWithDefault:
        def __init__(self, *,
                     a: int,
                     b: Optional[CatchAllVar] = {1, 2, 3},
                     c: int = 4) -> None:
            self.a = a
            self.b = b
            self.c = c

    kvs = {"a": 1, "b": {4, 5, 6}}
    assert _CatchAllUndefinedParameters.handle_from_dict(TestClassSimpleCatchAll,
                                                         kvs) == kvs


# Generated at 2022-06-13 19:21:35.754755
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    # GIVEN
    class TestClass:
        def __init__(self, catch_all: Optional[CatchAllVar]):
            self.catch_all = catch_all

    from dataclasses_json.config import ValidationMixin
    from marshmallow import Schema as MarshmallowSchema


    class TestSchema(ValidationMixin, MarshmallowSchema):
        class Meta:
            validation_undefined = Undefined.INCLUDE


    # WHEN
    schema = TestSchema()
    obj = TestClass(catch_all={'a':2})
    dump = schema.dumps(obj)

    # THEN
    assert dump == '{"catch_all":{"a":2}}'

# Generated at 2022-06-13 19:21:43.881524
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    """
    Assert that we can initialize dataclasses with undefined parameters
    """
    from dataclasses import dataclass

    @dataclass
    class TestCase:
        name: str
        value: int

        def __init__(self, *args, **kwargs):
            pass

    @dataclass
    class TestClass:
        a: int
        b: str
        c: str
        test_cases: List[TestCase] = dataclasses.field(default_factory=list)
        all_other_parameters: Optional[CatchAllVar] = None

        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 19:21:56.836170
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from typing import List

    from dataclasses import dataclass

    import pytest

    @dataclass
    class Bean:
        a: int
        b: int = 12
        c: Optional[str] = None
        d: List[str] = dataclasses.field(default_factory=list)
        e: CatchAll = None

    @dataclass
    class Bean2:
        a: int
        b: int = 12
        c: Optional[str] = None
        d: List[str] = dataclasses.field(default_factory=list)
        e: CatchAll = {"hallo": "welt"}

    @dataclass
    class Bean3:
        a: int
        b: int = 12
        c: Optional[str] = None
        d: List[str] = datac

# Generated at 2022-06-13 19:22:04.729359
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():

    class TestClass1:
        def __init__(self, a: str, b: int):
            self.a: str = a
            self.b: int = b

    class TestClass2:
        def __init__(self, a: str, b: int, c: str):
            self.a: str = a
            self.b: int = b
            self.c: str = c

    class TestClass3:
        def __init__(self, a: str, b: int, c: Optional[str]):
            self.a: str = a
            self.b: int = b
            self.c: Optional[str] = c

    class TestClass4:
        def __init__(self, a: str, b: int, c: str, d: str):
            self.a: str = a


# Generated at 2022-06-13 19:22:23.728169
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    from dataclasses import dataclass

    @dataclass
    class Foo(object):
        catch_all_field: CatchAll = dataclasses.field(
            default_factory=dict)

    @dataclass
    class Bar(object):
        defined1: str
        defined2: str

    class Baz(object):
        def __init__(self, defined1, defined2):
            self.defined1 = defined1
            self.defined2 = defined2

    foo = Foo(catch_all_field={"key1": "value1", "key2": "value2"})
    bar = Bar(defined1="value1", defined2="value2")
    baz = Baz(defined1="value1", defined2="value2")

# Generated at 2022-06-13 19:22:28.649644
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class Test:
        pass

    assert _UndefinedParameterAction.handle_dump(obj=Test) == {}



# Generated at 2022-06-13 19:22:37.511008
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass(
        init=_CatchAllUndefinedParameters.create_init,
        frozen=False)
    class TestDataClass:
        a: int
        b: int
        c: str
        d: int = dataclasses.field(default=5)
        e: int = dataclasses.field(default=1)
        # noinspection PyTypeChecker
        f: CatchAll = dataclasses.field(default_factory=dict)

    dataclass = TestDataClass(1, 2, "3", f={"g": 4})
    # Check default parameters
    assert dataclass.d == 5
    assert dataclass.e == 1
    # Check given parameters
    assert dataclass.a == 1
    assert dataclass.b == 2

# Generated at 2022-06-13 19:22:43.693864
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    simple_known = {"a": 1, "b": 2}
    simple_unknown = {"c": 3}
    simple_input = {**simple_known, **simple_unknown}

    assert _UndefinedParameterAction \
               ._separate_defined_undefined_kvs(
            cls=None,
            kvs=simple_input) == (simple_known, simple_unknown)

    # Advanced use case:
    # CatchAll is the catch-all parameter,
    # "d" is a user-defined parameter, which must not be included in CatchAll
    @dataclasses.dataclass
    class AdvancedDC:
        a: int
        Catch_All: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)


# Generated at 2022-06-13 19:22:44.936666
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # prepare
    kvs = {"a": 1, "b": 2}
    _RaiseUndefinedParameters.handle_from_dict(object, kvs)

# Generated at 2022-06-13 19:22:50.546741
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    from dataclasses_json.api import DataclassJSON
    # noinspection PyTypeChecker
    dataclass_json = DataclassJSON(
        unknown_parameter_policy=Undefined.EXCLUDE)

    @dataclass_json
    @dataclasses.dataclass
    class _TestClass:
        foo: int
        baz: int
        bat: str = dataclasses.field(default="bat")

    kvs = {"foo": 1, "baz": 2, "test": 3}
    kvs_ = {"foo": 1, "baz": 2}
    _IgnoreUndefinedParameters.handle_from_dict(_TestClass, kvs) == kvs_

    kvs = {"foo": 1, "baz": 2, "bat": "foo"}

# Generated at 2022-06-13 19:23:01.272629
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class DummyClass:
        def __init__(self, defined_parameters, undefined_parameters=None):
            self.defined_parameters = defined_parameters
            self.undefined_parameters = undefined_parameters


# Generated at 2022-06-13 19:23:07.469144
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    #
    # Test with of defined parameters
    #
    from dataclasses import dataclass


    @dataclass
    class A:
        a: int


    a = A(a=1)
    kvs = {"a": 1}
    defined, undefined = _UndefinedParameterAction._separate_defined_undefined_kvs(
        A, kvs)
    known = _RaiseUndefinedParameters.handle_from_dict(A, kvs)
    assert len(known) == 1
    assert len(kvs) == 1
    assert len(defined) == 1
    assert len(undefined) == 0
    assert known == kvs
    assert a == A(a=1)

    #
    # Test with a single undefined parameter
    #

# Generated at 2022-06-13 19:23:12.520965
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class MyClass:
        pass

    parameters = {"p1": "v1", "p2": "v2"}
    returned_parameters = _RaiseUndefinedParameters.handle_from_dict(
        MyClass, parameters)
    assert parameters == returned_parameters


# Generated at 2022-06-13 19:23:22.202741
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, foo: int, bar: int):
            self.foo = foo
            self.bar = bar

    assert _IgnoreUndefinedParameters.handle_from_dict(
        Foo, {}) == {}
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Foo, {"foo": 1, "bar": -1}) == {"foo": 1, "bar": -1}
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Foo, {"baz": 1, "foo": 1, "bar": -1}) == {"foo": 1, "bar": -1}
    assert _IgnoreUndefinedParameters.handle_from_dict(
        Foo, {"baz": 1}) == {}


# Generated at 2022-06-13 19:24:01.764250
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Test(abc.ABC):

        @staticmethod
        @abc.abstractmethod
        def handle_to_dict(obj, kvs: Dict[Any, Any]) -> Dict[Any, Any]:
            """
            Return the parameters that will be written to the output dict
            """
            pass

    undef_params_class = _UndefinedParameterAction()
    expected_params = {"key1": "value1", "key2": "value2"}
    actual_params = undef_params_class.handle_to_dict(obj=None, kvs=expected_params)
    assert expected_params == actual_params



# Generated at 2022-06-13 19:24:12.876739
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class _TestClass:
        p1: str = ""

    # Assert valid input
    assert _UndefinedParameterAction.handle_from_dict(_TestClass,
                                                      {"p1": "test1"}) == \
           {"p1": "test1"}
    assert _UndefinedParameterAction.handle_from_dict(_TestClass,
                                                      {"p1": "test1",
                                                       "p2": "test2"}) == \
           {"p1": "test1"}

    # Assert invalid input

# Generated at 2022-06-13 19:24:18.777248
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    test_class = dataclasses.dataclass(frozen=True)(
        float, int,
        undefined_parameter_action=_RaiseUndefinedParameters)

    with pytest.raises(UndefinedParameterError):
        _ = test_class(1.0, 1, undefined_parameter1=1,
                       undefined_parameter2=1)



# Generated at 2022-06-13 19:24:28.329457
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Test:
        def __init__(self, a: int, b: str = "DEFAULT", c: int = 0,
                     _undefined: CatchAll = None):
            self.a = a
            self.b = b
            self.c = c
            self._undefined = _undefined

    cls = Test(1, "RECEIVED_DEFAULT", _undefined={"X": 1})
    init = _CatchAllUndefinedParameters.create_init(cls)

    # Wrong default
    with pytest.raises(UndefinedParameterError) as e:
        Test(1, _undefined={1, 2})
    assert "CatchAll" in e.value.messages

# Generated at 2022-06-13 19:24:37.986295
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from typing import Optional, List
    import dataclasses
    import json
    import pytest
    from marshmallow import fields, Schema
    from dataclasses_json import dataclass_json, config
    from dataclasses_json import Undefined, CatchAll
    import sys

    class _PersonSchema(Schema):
        first_name = fields.Str()
        last_name = fields.Str()
        age = fields.Integer()
        nationalities = fields.List(fields.String())

    @dataclass_json(undefined=Undefined.INCLUDE)
    class Person:
        first_name: str
        last_name: str
        age: int
        nationalities: List[str] = dataclasses.field(default_factory=list)
        _undefined: CatchAll = dataclasses.field

# Generated at 2022-06-13 19:24:45.765368
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class A:
        pass

    kvs: Dict[Any, Any] = {"a": 1, "b": 2, "c": 3}
    expected = {"a": 1, "b": 2}
    result = _RaiseUndefinedParameters.handle_from_dict(A, kvs)
    assert result == expected

    try:
        test_kvs = kvs
        test_kvs["undefined"] = 4
        _RaiseUndefinedParameters.handle_from_dict(A, test_kvs)
    except UndefinedParameterError:
        pass
    else:
        raise Exception("Expected UndefinedParameterError")



# Generated at 2022-06-13 19:24:46.327841
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    pass

# Generated at 2022-06-13 19:24:56.597569
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class A:
        a: int
        b: int = 1
        c: Optional[CatchAllVar] = dataclasses.field(default_factory=dict)

    @dataclasses.dataclass
    class B:
        a: CatchAllVar

    @dataclasses.dataclass
    class C:
        a: Any

    @dataclasses.dataclass
    class D:
        a: int
        b: int
        c: Optional[CatchAllVar]

    c_instance = C(a=None)

    for clazz in [A, B, D]:
        for undefined in Undefined:
            _CatchAllUndefinedParameters._set_undefined_parameter_action(
                clazz, undefined)

# Generated at 2022-06-13 19:25:00.588538
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    input = {"alpha": "a", Undefined.INCLUDE.value._SentinelNoDefault: {"bravo": "b"}}
    expected = {"alpha": "a", "bravo": "b"}
    output = Undefined.INCLUDE.value.handle_to_dict(None, input)
    assert output == expected

# Generated at 2022-06-13 19:25:09.126806
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    import pytest

    @dataclasses.dataclass
    class DataClass:
        a: int
        b: str

    data_class_initialization_data = {"a": 1, "b": "2"}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters \
            .handle_from_dict(cls=DataClass,
                              kvs={"a": 1, "b": "2", "c": 3})

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters \
            .handle_from_dict(cls=DataClass,
                              kvs={"a": 1, "b": "2", "c": 3})


# Generated at 2022-06-13 19:26:09.172023
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin, config

    @dataclass
    class MyDataClass(DataClassJsonMixin):
        a: str
        b: str = field(default="b_default")
        c: str = field(default_factory=lambda: "c_default")
        catch_all: CatchAll = field(default=None)

    expected_dict = {"a": "a1", "b": "b1", "c": "c1", "d": "d1", "e": "e1"}

    def test_combination(given_params: dict, expected: dict,
                         expected_catch_all: dict):
        example = MyDataClass(**given_params)
        assert vars(example) == expected

# Generated at 2022-06-13 19:26:17.353822
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class A:
        a: int = 1
        b: str = "Foo"

    @dataclasses.dataclass(undefined=Undefined.RAISE)
    class B:
        a: int = 1
        b: str = "Foo"

    @dataclasses.dataclass(undefined=Undefined.INCLUDE)
    class C:
        a: int = 1
        b: str = "Foo"
        c: Optional[CatchAllVar] = None

    a = A(1, "Foo")
    a2 = A(2, "Foo")
    a3 = A(3, "Foo")
    a4 = A(4, "Foo", "extra")
    a

# Generated at 2022-06-13 19:26:27.749957
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json import dataclass, Undefined
    from dataclasses_json.utils import CatchAll
    from marshmallow import fields
    from marshmallow_dataclass import NewType

    @dataclass
    class A:
        x: Optional[CatchAll] = None
        y: int

    class A_Schema(Schema):
        x = fields.Dict()
        y = fields.Integer()

    a = A(y=1, _UNKNOWN=17, _UNKNOWN2=21)
    a_schema = A_Schema()
    print(A_Schema().dump(a))  # {'y': 1, 'x': {'_UNKNOWN': 17, '_UNKNOWN2': 21}}

# Generated at 2022-06-13 19:26:37.963549
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    """
    Test the method _UndefinedParameterAction.handle_to_dict
    """
    @dataclasses.dataclass
    class ClassForTestingUndefinedParameters:
        one: int
        two: int
        three: int = dataclasses.field(metadata=dict(
            dataclasses_json=dict(undefined=Undefined.RAISE,
                                  unknown=Undefined.INCLUDE,
                                  str_encoder=None))
        )

    assert ClassForTestingUndefinedParameters.__dict__ is not None
    field_three = ClassForTestingUndefinedParameters.__dict__["three"]
    assert field_three is not None
    undefined_parameter_action = field_three.metadata.get("dataclasses_json")[
        "undefined"].value

# Generated at 2022-06-13 19:26:48.158040
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class _TestClass:
        defined_parameter: int
        @dataclasses.dataclass
        class _NestedClass:
            nested_default: int
        nested_class: Optional["_NestedClass"] = dataclasses.field(
            default_factory=lambda: _NestedClass(nested_default=0))

        def __init__(self, defined_parameter: int,
                     undefined_parameter: CatchAll,
                     **kwargs):
            self.defined_parameter = defined_parameter
            self.undefined_parameter = undefined_parameter

    # Test that undefined_parameter is rewritten
    def test_undefined_parameter_rewritten():
        _TestClass(defined_parameter=1,
                   undefined_parameter={1: 2})



# Generated at 2022-06-13 19:26:52.887319
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Test:
        def __init__(self, param: int,
                     catch_all: Optional[CatchAllVar] = None):
            self.param = param
            self.catch_all = catch_all or {}

        def __eq__(self, other):
            if not isinstance(other, Test):
                return False
            return self.param == other.param and self.catch_all == other.catch_all

    from marshmallow import fields as marshmallow_fields

    field = Field(type(None), default=None,
                  default_factory=dict,
                  metadata={'marshmallow_field': marshmallow_fields.Dict()})

    init = \
        _CatchAllUndefinedParameters.create_init(Test)


# Generated at 2022-06-13 19:26:59.466334
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, a: int, b: int, c: int, d: int,
                     e: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

    a = A(a=1, b=2, c=3, d=4, e={'f': 5, 'g': 6})
    kvs = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': {'f': 5, 'g': 6}}
    kvs_expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5, 'g': 6}
    kvs_actual = _C

# Generated at 2022-06-13 19:27:08.070804
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, arg1: int, arg2: str):
            pass

        def __eq__(self, other):
            return isinstance(other, TestClass) and self.__dict__ == other.__dict__


    @dataclasses.dataclass
    class TestDataClass:
        arg1: int
        arg2: str


    @dataclasses.dataclass
    class TestDataClassWithUndefined:
        arg1: int
        arg2: str
        undefined_parameters: CatchAll = dataclasses.field(
            default_factory=dict)


    for cls in (TestClass, TestDataClass, TestDataClassWithUndefined):
        input_parameters = {"arg1": 1, "arg2": "2", "arg3": 3}

       

# Generated at 2022-06-13 19:27:15.892970
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int = 0

    obj = TestClass
    init_signature = inspect.signature(obj.__init__)
    num_params_takeable = len(
        init_signature.parameters) - 1  # don't count self
    num_args_takeable = num_params_takeable
    for i in range(num_args_takeable + 1):
        args = tuple(range(i))
        _IgnoreUndefinedParameters.create_init(obj)(None, *args)



# Generated at 2022-06-13 19:27:25.164861
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class MyClass():
        @property
        def unknown_parameters(self):
            return self._unknown_parameters

        def __init__(self):
            self._unknown_parameters = {}

    @dataclasses.dataclass
    class MyDataClass(MyClass):
        catch_all: CatchAll = dataclasses.field(default=None)
        _undefined_param_action = _IgnoreUndefinedParameters

    # No undefined parameters:
    obj = MyDataClass(catch_all=None)
    assert _IgnoreUndefinedParameters.handle_dump(obj) == {}

    # Define an undefined parameter
    obj._unknown_parameters = {"undefined": "value"}
    assert _IgnoreUndefinedParameters.handle_dump(obj) == {"undefined": "value"}

# Generated at 2022-06-13 19:29:48.309742
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():

    @dataclasses.dataclass
    class TestClass:
        class CatchAllUndefinedParameters:
            default_value_factory = dict

        def __init__(self, x: int, y: int, z: int = None,
                     catch_all: CatchAll = None):
            self.x = x
            self.y = y
            self.z = z

            self.catch_all = catch_all

    def _test(test_input: Dict, expected_output: Dict, test_class=TestClass):
        assert _CatchAllUndefinedParameters.handle_from_dict(test_class,
                                                             test_input) == \
               expected_output

    test_input = dict(x=1, y=2, z=3, a=4)

# Generated at 2022-06-13 19:29:58.998486
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Foo:
        a: int = 1
        b: str = "foo"
        c: str = dataclasses.field(
            default=lambda: "Do not include this parameter in the output")

        def __init__(self, a: int, b: str, c: str = "Do not include this "
                                                    "parameter in the output"):
            self.a = a
            self.b = b
            self.c = c

    init = _IgnoreUndefinedParameters.create_init(Foo)
    f = Foo(1, "foo", "bar")
    foo_with_new_init = init(f, 3, "bar")

    assert f.a == foo_with_new_init.a
    assert f.b == foo_with_new_init

# Generated at 2022-06-13 19:30:08.459852
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    try:
        class ClassWithUndefinedParameters:
            def __init__(self, x: int = None, y: int = None,
                         catch_all: Optional[CatchAllVar] = None):
                pass

        ClassWithUndefinedParameters()
        raise AssertionError("Did not raise TypeError")
    except TypeError:
        pass

    try:
        ClassWithUndefinedParameters(1, 2, 3)
        raise AssertionError("Did not raise TypeError")
    except TypeError:
        pass

    try:
        ClassWithUndefinedParameters(1, 2, catch_all={"test": 1})
        raise AssertionError("Did not raise TypeError")
    except TypeError:
        pass

    ClassWithUndefinedParameters(1, 2)

# Generated at 2022-06-13 19:30:18.585950
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        foo: str
        bar: str
        test: str = "default"

    class_fields = fields(TestClass)
    field_names = [field.name for field in class_fields]
    field_defaults = {f.name: f.default for f in class_fields}

    # noinspection PyUnusedLocal
    @dataclass_json(undefined=Undefined.EXCLUDE)
    class TestClassWithIgnoreUndefinedParameters:
        foo: str
        bar: str
        test: str = "default"

    parameters = {
        "foo": "a",
        "bar": "b",
        "test": "c"
    }
    received = _IgnoreUndefinedParameters.handle_from_dict