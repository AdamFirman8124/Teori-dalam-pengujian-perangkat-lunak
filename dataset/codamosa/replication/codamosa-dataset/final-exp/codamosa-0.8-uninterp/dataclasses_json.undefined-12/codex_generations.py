

# Generated at 2022-06-13 19:20:40.903038
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    TestClass = dataclasses.make_dataclass("TestClass", [
        ("a", int),
        ("b", int),
        ("c", int),
        ("d", int),
        ("e", int),
    ])

    def _run_test(action: _UndefinedParameterAction,
                  kvs: Dict[str, Any]) -> Dict[str, Any]:
        return action.handle_from_dict(cls=TestClass, kvs=kvs)

    assert _run_test(_IgnoreUndefinedParameters,
                     kvs={"a": 1, "b": 2, "c": 3, "e": 5, "f": 6}) == {
                           "a": 1, "b": 2, "c": 3, "e": 5}

# Generated at 2022-06-13 19:20:48.008453
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import dataclasses

    class MyClass:
        def __init__(self, param: bool):
            pass

    my_dict = {"param": "test"}

    try:
        # noinspection PyUnresolvedReferences
        _CatchAllUndefinedParameters._CatchAllUndefinedParameters.create_init(
            MyClass)(MyClass, **my_dict)
    except TypeError as te:
        assert type(te) == TypeError

# Generated at 2022-06-13 19:20:50.763026
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class DummyClass:
        pass

    dummy_class = DummyClass()
    assert _IgnoreUndefinedParameters.handle_dump(dummy_class) == {}

# Generated at 2022-06-13 19:21:01.426928
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    handle_from_dict = _IgnoreUndefinedParameters.handle_from_dict
    assert handle_from_dict(cls=int, kvs={}) == {}
    assert handle_from_dict(cls=int, kvs="abc") == {}
    assert handle_from_dict(cls=int, kvs=1) == {"x": 1}
    assert handle_from_dict(cls=int, kvs={"x": 1, "y": 2}) == {"x": 1}

    class Example:
        def __init__(self, x, y):
            pass

    assert handle_from_dict(cls=Example,
                            kvs={"x": 1, "y": 2, "z": 3}) == {"x": 1, "y": 2}

# Generated at 2022-06-13 19:21:06.436580
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        required_field: int

    kvs = {
        "required_field": 42,
        "undefined_field": 0
    }

    initial = _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert initial == {"required_field": 42}



# Generated at 2022-06-13 19:21:07.723417
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:21:11.987296
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = Undefined.INCLUDE._value_
    assert obj.handle_dump(obj) == {}
    obj = Undefined.RAISE._value_
    assert obj.handle_dump(obj) == {}
    obj = Undefined.EXCLUDE._value_
    assert obj.handle_dump(obj) == {}

# Generated at 2022-06-13 19:21:21.085028
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class SimpleClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class UnknownClass(_RaiseUndefinedParameters):
        pass

    class UnknownClassWithFields(_RaiseUndefinedParameters):
        x: float
        y: str

    with pytest.raises(UndefinedParameterError):
        UnknownClass.handle_from_dict(SimpleClass, {"a": 1, "b": 2})

    assert UnknownClass.handle_from_dict(SimpleClass, {"x": 1, "y": 2}) == {
        "x": 1,
        "y": 2
    }

# Generated at 2022-06-13 19:21:33.590967
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # Test method
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str
    # Test cases
    input_1 = {"a": 1, "b": "test"}
    output_1 = {"a": 1, "b": "test"}

    input_2 = {"a": 1, "b": "test", "c": 3}

    input_3 = {"a": 1, "c": 3}

    # Do test cases
    assert _RaiseUndefinedParameters.handle_from_dict(TestClass, input_1) == output_1
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, input_2)
        assert False
    except UndefinedParameterError:
        assert True

# Generated at 2022-06-13 19:21:37.949942
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError()
    except UndefinedParameterError as e:
        assert str(e) == "UndefinedParameterError"

    try:
        raise UndefinedParameterError("some message")
    except UndefinedParameterError as e:
        assert str(e) == "some message"

# Generated at 2022-06-13 19:21:56.885287
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass():
        pass
    given_params = {"somearg": "someargval", "someotherarg": "someotherargval"}
    given_class = TestClass
    assert _UndefinedParameterAction.handle_from_dict(given_class,
                                                      given_params) == {}
    assert _RaiseUndefinedParameters.handle_from_dict(given_class,
                                                      given_params) == {}



# Generated at 2022-06-13 19:21:57.594904
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    pass

# Generated at 2022-06-13 19:22:03.933086
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Sample:
        def __init__(self, a, b, c=3):
            pass

    for kvs in [
        dict(a=1, b=2),
        dict(a=1, b=2, c=3),
        dict(a=1, b=2, c=3, d=4)
    ]:
        _RaiseUndefinedParameters.handle_from_dict(Sample, kvs)

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(Sample, dict(a=1, b=2, d=4))



# Generated at 2022-06-13 19:22:12.580512
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        field_a: str = "default"
        field_b: int
        field_c: Optional[str] = None
        field_d: CatchAll

        __undefined__: _UndefinedParameterAction = _CatchAllUndefinedParameters

        def __init__(self, *args, **kwargs):
            pass

    # noinspection PyTypeHints
    init = _CatchAllUndefinedParameters.create_init(TestClass)
    try:
        init(TestClass(), "arg_too_many")
        raise AssertionError(
            "Did not raise a TypeError for too many positional arguments.")
    except TypeError:
        pass

# Generated at 2022-06-13 19:22:23.682912
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass(init=False)
    class Dummy(object):
        catch_all: CatchAll = dataclasses.field(
            default=None, metadata={"marshmallow_field": "test"})

        def __init__(self, **kwargs):
            pass

    # noinspection PyTypeChecker
    dummy_instance = Dummy(test=dict(a=1))

    assert \
    _CatchAllUndefinedParameters.handle_dump(dummy_instance) == dict(a=1)

# Generated at 2022-06-13 19:22:28.334376
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    handle = _UndefinedParameterAction.handle_dump
    assert handle(None) == {}


# Generated at 2022-06-13 19:22:40.769279
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass(abc.ABC):
        @staticmethod
        @abc.abstractmethod
        def _handle_from_dict(cls, kvs):
            pass

    @dataclasses.dataclass
    class TestClass1(TestClass):
        a: int
        b: Optional[int] = None
        c: str

    class TestClass2(TestClass):
        a: int
        b: Optional[int] = None
        c: str


# Generated at 2022-06-13 19:22:54.176304
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # Input are given undefined parameters
    class Foo:
        def __init__(self, a: str, b: str):
            pass

    kvs = {'a': 'a', 'b': 'b', 'c': 'c'}

    try:
        _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    except UndefinedParameterError:
        pass
    else:
        raise AssertionError("Expected to throw an error.")

    # Input contains no undefined parameters
    kvs = {'a': 'a', 'b': 'b'}
    known_parameters = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    assert known_parameters == kvs



# Generated at 2022-06-13 19:23:02.443589
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # Test setup
    @dataclasses.dataclass
    class TestClass:
        field: int
        field_2: str

        def __init__(self, **kwargs):
            kwargs = _IgnoreUndefinedParameters.handle_from_dict(self.__class__,
                                                                 kwargs)
            unused_parameters = kwargs.pop(
                'catch_all', {})  # type: ignore
            for arg, val in kwargs.items():
                setattr(self, arg, val)

    # Tests
    assert _IgnoreUndefinedParameters.handle_dump(TestClass(field=1,
                                                             field_2="test")) == {}

# Generated at 2022-06-13 19:23:14.350108
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.undefined import _CatchAllUndefinedParameters

    class ExampleClass:
        def __init__(self, a: int, catch_all: Optional[CatchAllVar] = None):
            self.a = a
            self.catch_all = catch_all

    @dataclasses.dataclass
    class ExampleDataclass:
        a: int
        catch_all: Optional[CatchAllVar] = None

    a: str = "a"
    b: str = "b"
    c: str = "c"
    x: str = "x"
    y: str = "y"
    z: str = "z"

    example_class = ExampleClass(a=1,
                                 catch_all={a: 1, b: 2, c: 3})
    example_datac

# Generated at 2022-06-13 19:23:43.167145
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from .example_classes import TestClassWithOptionalCatchAll
    # receive all parameters
    obj = TestClassWithOptionalCatchAll(a=1, b=2, c=dict(z=1, y=2))
    kvs = {'a': 1, 'b': 2, 'c': {'z': 1, 'y': 2}}
    assert _CatchAllUndefinedParameters.handle_to_dict(obj, kvs) == {'a': 1,
                                                                     'b': 2,
                                                                     'c': {
                                                                         'z': 1,
                                                                         'y': 2}}
    # receive known parameters
    obj = TestClassWithOptionalCatchAll(a=1, b=2)
    kvs = {'a': 1, 'b': 2, 'c': {}}
   

# Generated at 2022-06-13 19:23:43.560910
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    pass

# Generated at 2022-06-13 19:23:44.295012
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump({}) == {}

# Generated at 2022-06-13 19:23:47.797011
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    kvs = {"field1": "value1", "field2": "value2"}
    assert _UndefinedParameterAction.handle_to_dict(None, kvs) == kvs



# Generated at 2022-06-13 19:23:51.441889
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass:
        def __init__(self, field1: str, field2: str,
                     *,  # type: ignore
                     field3: str = "default_value"):
            pass

    kvs = {"field1": "value1", "field2": "value2", "field4": "value4"}

    assert _UndefinedParameterAction.handle_from_dict(TestClass, kvs) == \
           kvs



# Generated at 2022-06-13 19:23:57.239347
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class SomeClass:
        pass

    @dataclasses.dataclass
    class SomeDataclass:
        foo: str

    for obj in [SomeClass, SomeDataclass]:
        for undefined_parameters in ({}, {"some": "thing"},
                                     {"other": "stuff"}, {"some": "thing",
                                                          "other": "stuff"}):
            catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(
                obj)
            kvs = {catch_all_field.name: undefined_parameters}
            output = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
            assert output == undefined_parameters



# Generated at 2022-06-13 19:23:59.742378
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    msg = "Test"
    e = UndefinedParameterError(msg)
    assert e.messages == [msg]

# Generated at 2022-06-13 19:24:11.230668
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():

    @dataclasses.dataclass
    class TestCase:
        test_case_name: str
        params: Dict[str,
                     Any] = dataclasses.field(default_factory=lambda: {
            "x": 10, "y": 20, "z": 30})
        catch_all: CatchAll = dataclasses.field(default=None)

    @dataclasses.dataclass
    class TestCases:
        testcases: Dict[str, TestCase]

    @dataclasses.dataclass
    class Input:
        testcases: Dict[str, TestCase]
        global_x: int = dataclasses.field(default=0)
        global_y: int = dataclasses.field(default=0)


# Generated at 2022-06-13 19:24:13.251783
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()
    result = _UndefinedParameterAction.handle_dump(obj=obj)
    assert result == {}

# Generated at 2022-06-13 19:24:24.485886
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin, config

    @dataclass
    class SomeClass(DataClassJsonMixin):
        a: int
        b: str

    some_instance = SomeClass.from_dict({"a": 1, "b": "1", "c": "foobar"})
    assert some_instance.a == 1
    assert some_instance.b == "1"

    @dataclass
    class SomeClass(DataClassJsonMixin):
        a: int
        b: str
        c: int


# Generated at 2022-06-13 19:25:02.881618
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():

    @dataclasses.dataclass
    class TestObject:
        catch_all: CatchAll = dataclasses.field(
            default=None)  # type: ignore
        a: int
        b: int

    dct = {"a": 1, "b": 2, "c": 3, "_UNKNOWN0": 10}
    final_dct = _CatchAllUndefinedParameters.handle_from_dict(TestObject, dct)
    expected_dct = {"catch_all": {"_UNKNOWN0": 10}, "a": 1, "b": 2}
    assert final_dct == expected_dct

# Generated at 2022-06-13 19:25:06.714590
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Foo:
        def __init__(self):
            self._catch_all = {'foo': 'bar'}

    assert isinstance(_UndefinedParameterAction.handle_to_dict(Foo(), {}),
                      dict)
    assert len(_UndefinedParameterAction.handle_to_dict(Foo(), {})) == 0



# Generated at 2022-06-13 19:25:13.903355
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class Cls:
        def __init__(self, a: int, **_):
            assert isinstance(_, dict)

    dict_to_use = {}
    _CatchAllUndefinedParameters.handle_from_dict(Cls, dict_to_use)

    dict_to_use = {"a": 2}
    _CatchAllUndefinedParameters.handle_from_dict(Cls, dict_to_use)

    dict_to_use = {"a": 2, "_": 4}
    _CatchAllUndefinedParameters.handle_from_dict(Cls, dict_to_use)



# Generated at 2022-06-13 19:25:15.616769
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from tests.test_classes.fixtures import DetailedFather, SimpleFather

# Generated at 2022-06-13 19:25:31.879411
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass()
    class A:
        a: int
        b: int

    @dataclasses.dataclass()
    class B:
        a: int
        b: int

    @dataclasses.dataclass
    class C:
        a: int
        catch_all: Optional[CatchAllVar] = None
        b: int

    @dataclasses.dataclass
    class D:
        a: int
        catch_all: Optional[CatchAllVar] = None
        b: int

    @dataclasses.dataclass
    class E:
        a: int
        catch_all: Optional[CatchAllVar] = None
        b: int

    @dataclasses.dataclass
    class F:
        a: int

# Generated at 2022-06-13 19:25:39.626343
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        a: int
        b: int
        c: CatchAll

        def __init__(self, a, b, *, c=None):
            self.a = a
            self.b = b
            self.c = c

    init = \
        _UndefinedParameterAction._separate_defined_undefined_kvs.__get__(
            obj=MyClass)

    assert init == MyClass.__init__

    init = Undefined.INCLUDE.value.create_init(MyClass)(MyClass)
    assert inspect.signature(init) == inspect.signature(MyClass.__init__)
    x = init(1, 2)
    assert x.a == 1
    assert x.b == 2

# Generated at 2022-06-13 19:25:49.584722
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass(frozen=True)
    class _TestClass(metaclass=abc.ABCMeta):
        a: Any
        b: str
        c: int
        d: float
        e: bool

    kvs: Dict[str, Any]

    # Adds all params, no undefined params
    kvs = {"a": 5, "b": "5", "c": 5, "d": 5.5, "e": True}
    received = _CatchAllUndefinedParameters.handle_from_dict(
        cls=_TestClass, kvs=kvs)
    expected_copy_kvs = kvs.copy()
    expected = expected_copy_kvs
    assert received == expected

    # Adds all params for this param, no undefined params

# Generated at 2022-06-13 19:25:57.543124
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    from marshmallow import fields
    from marshmallow.exceptions import ValidationError
    from marshmallow.validate import OneOf
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin, config

    @dataclass
    class Test(DataClassJsonMixin):
        x: int = 1
        y: int = 2

        class Config(config.Config):
            unknown_parameters = Undefined.INCLUDE

    test = Test(x=2, to_dict_test=1)
    kvs = test.to_dict()

    assert kvs == {'x': 2, 'y': 2}

# Generated at 2022-06-13 19:26:04.267669
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    known_input = {"foo": "Foo", "other_field": 42,
                   "catch_all": {"I am": "unknown"}}
    result = {"foo": "Foo", "other_field": 42}
    assert _CatchAllUndefinedParameters.handle_to_dict(None,
                                                       known_input) == result
    assert _RaiseUndefinedParameters.handle_to_dict(None,
                                                    known_input) == result
    assert _IgnoreUndefinedParameters.handle_to_dict(None,
                                                     known_input) == result



# Generated at 2022-06-13 19:26:12.720262
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class _TestClass:
        def __init__(self, x, y=None, z=None, catch_all=None):
            self.x = x
            self.y = y
            self.z = z
            self.catch_all = catch_all


    _TestClass_catch_all = _CatchAllUndefinedParameters \
        .create_init(_TestClass)

    test_instance = _TestClass_catch_all(1, 2, 3, a=4, b=5)

    assert test_instance.x == 1
    assert test_instance.y == 2
    assert test_instance.z == 3
    assert test_instance.catch_all == {"a": 4, "b": 5}

    test_instance_2 = _TestClass_catch_all(3, catch_all={})
    assert test_

# Generated at 2022-06-13 19:27:31.242009
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.__y = 3

        @property
        def y(self):
            return self.__y

    t = TestClass(1, 2)
    assert hasattr(t, "y")
    assert not hasattr(t, "z")

    received_parameters = {
        "a": 3,
        "x": "ignore1"
    }

    known_given_parameters, unknown_given_parameters = \
        _IgnoreUndefinedParameters.handle_from_dict(TestClass,
                                                     received_parameters)

    assert known_given_parameters == {"a": 3}
    assert unknown_given_parameters == {"x": "ignore1"}

    # Unit

# Generated at 2022-06-13 19:27:38.438508
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    def _get_kvs(obj):
        return {"parameter_a": "a", "parameter_b": "b", "parameter_c": "c",
                "catch_all_field": {"field_x": "x", "field_y": "y"}}

    class TestClass:
        def __init__(self, parameter_a, parameter_b, parameter_c,  # noqa: A003
                     catch_all_field: Optional[CatchAllVar] = None):
            self.parameter_a = parameter_a
            self.parameter_b = parameter_b
            self.parameter_c = parameter_c
            self.catch_all_field = catch_all_field

    kvs = _get_kvs(obj=TestClass)

# Generated at 2022-06-13 19:27:45.885509
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: int
        c: str
        d: float
        e: dict
        unused: Optional[CatchAllVar] = dataclasses.field(default=None)

        def __init__(self, b: int, c: str, d: float, e: dict,
                     **kwargs):
            self.b = b
            self.c = c
            self.d = d
            self.e = e

    init = _CatchAllUndefinedParameters.create_init(TestClass)
    init(TestClass, 1, 2, 3, d=3.3, f=3)

# Generated at 2022-06-13 19:27:58.398924
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class DummyClass:
        pass

    @dataclasses.dataclass
    class TestClass:
        field_a: str
        field_b: str

    x = "hello"
    y = "world"
    kvs = {"field_a": x}
    kvs_expected = {"field_a": x}

    assert kvs_expected == _RaiseUndefinedParameters.handle_from_dict(
        TestClass, kvs)

    kvs = {"field_a": x, "field_b": y}
    kvs_expected = {"field_a": x, "field_b": y}

    assert kvs_expected == _RaiseUndefinedParameters.handle_from_dict(
        TestClass, kvs)


# Generated at 2022-06-13 19:27:59.142861
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    pass
    # TODO

# Generated at 2022-06-13 19:28:00.166777
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("message")

# Generated at 2022-06-13 19:28:07.886488
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from marshmallow import Schema, fields

    from marshmallow.exceptions import ValidationError
    from marshmallow.validate import OneOf
    from dataclasses import dataclass

    class BaseType(Enum):
        FOO = "FOO"
        BAR = "BAR"
        BAZ = "BAZ"

    @dataclass
    class Bar():
        foo: BaseType

    @dataclass
    class Baz():
        foo: BaseType = BaseType.FOO

    class BarSchema(Schema):
        foo = fields.EnumField(Baz.foo)

    schema = BarSchema()

    class BazSchema(Schema):
        foo = fields.EnumField(Baz.foo)

    baz_schema = BazSchema()


# Generated at 2022-06-13 19:28:19.371402
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Data:
        x: int
        y: int

    known_given_parameters, unknown_given_parameters = \
        _RaiseUndefinedParameters.handle_from_dict(
            cls=Data, kvs={'x': 5, 'a': 3})

    assert {'x': 5} == known_given_parameters
    assert {} == unknown_given_parameters

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(cls=Data, kvs={'a': 3,
                                                                  'b': 4})



# Generated at 2022-06-13 19:28:26.073911
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class DummyClass:
        def __init__(self, a: int, b: str, c: float):
            pass

    input_dict = {'a': 2, 'b': 'asdf', 'c': 2.3, 'd': True}
    known_dict, unknown_dict = _UndefinedParameterAction. \
        _separate_defined_undefined_kvs(DummyClass, input_dict)

    assert known_dict == {'a': 2, 'b': 'asdf', 'c': 2.3}
    assert unknown_dict == {'d': True}

# Generated at 2022-06-13 19:28:32.289895
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field
    from typing import Optional
    from datetime import datetime

    @dataclass
    class Test:
        a: int = 1
        b: int = 2
        c: int = field(
            default_factory=lambda: 2)
        d: int = field(
            default_factory=lambda: 3)
        e: Optional[str] = field(default="test")
        catch_all: Optional[CatchAllVar] = \
            field(default_factory=dict)

    # Test no keyword arguments
    _, _, _, _, _, catch_all = Test.__init__(1, 1, 1, 1, 1, catch_all=0)
    assert catch_all == {}

    # Test no arguments
    _, _, _, _, _