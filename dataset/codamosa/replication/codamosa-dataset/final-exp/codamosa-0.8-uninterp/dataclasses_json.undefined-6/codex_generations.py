

# Generated at 2022-06-13 19:20:53.554360
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.core import Dataclass

    @Dataclass(undefined=Undefined.INCLUDE)
    class A:
        a: str
        b: int
        c: Optional[CatchAllVar]

    a = A("a", 1, {"d": "d", "e": 2})
    class_fields = fields(A)
    kvs = {f.name: getattr(a, f.name) for f in class_fields}
    kvs = _CatchAllUndefinedParameters.handle_to_dict(a, kvs)
    assert {"a": "a", "b": 1, "d": "d", "e": 2} == kvs

# Generated at 2022-06-13 19:20:59.376049
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class _TestClass:

        def __init__(self, x, *, catchall: CatchAll = None):
            self.x = x
            self.catchall = catchall

    x = _TestClass(x=1, catchall=dict(hello="world"))
    assert _UndefinedParameterAction.handle_to_dict(obj=x, kvs=x.__dict__) == dict(x=1, hello="world")



# Generated at 2022-06-13 19:21:08.977164
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():  # type: () -> None
    import inspect

    @dataclasses.dataclass
    class Foo:
        a: Any
        b: Any

        def __init__(self, *args, **kwargs):
            pass

    def init_to_dict(obj):
        return inspect.signature(obj.__init__).parameters.keys()

    @dataclasses.dataclass
    class Bar:
        a: Any
        b: Any

        def __init__(self, a, b, **kwargs):
            pass

    assert "self" in init_to_dict(Foo)
    assert "self" in init_to_dict(Bar)

    new_init = _IgnoreUndefinedParameters.create_init(Foo)
    assert init_to_dict(new_init) == {"self"}

   

# Generated at 2022-06-13 19:21:18.847484
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class Test:
        def __init__(self, a: int, b: int, c: int,
                     catch_all: Optional[CatchAllVar] = None):
            pass

    default = dict(d=4, e=5)
    result = _CatchAllUndefinedParameters.handle_from_dict(
        Test, {"a": 1, "b": 2, "c": 3, "catch_all": default})
    assert result == {"a": 1, "b": 2, "c": 3, "catch_all": default}

    result = _CatchAllUndefinedParameters.handle_from_dict(
        Test, {"a": 1, "b": 2, "c": 3, "catch_all": default, "d": 4, "e": 5})

# Generated at 2022-06-13 19:21:26.228335
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # Given class A with an optional field a, and a required field b.
    @dataclasses.dataclass
    class A:
        a: str = "default_a"
        b: str

        def __init__(self, *args, **kwargs):
            pass

    # When a new init is created with the method create_init and initialized
    # with an extra parameter
    new_init = _IgnoreUndefinedParameters.create_init(A)
    a = new_init(A, "some_b", a="some_a", c="some_c")

    # Then the class should initialize correctly, with parameter b and a
    # with the given value, and the extra parameter should just be discarded.
    assert a.a == "some_a"
    assert a.b == "some_b"
    assert not hasattr

# Generated at 2022-06-13 19:21:31.828881
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        pass
    except Exception:
        raise UndefinedParameterError("The error message")


# the following code avoids a mypy false-positive:
# https://github.com/python/mypy/issues/5374



# Generated at 2022-06-13 19:21:41.363530
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    def catch_all_func(unknown: Optional[CatchAll] = None) -> None:
        pass

    class Outer:
        def __init__(self, unknown: Optional[CatchAll] = None):
            self.inner = Inner(unknown=unknown)

    class Inner:
        def __init__(self, unknown: Optional[CatchAll] = None):
            self.unknown = unknown

    @dataclasses.dataclass
    class Nest:
        a: Optional[CatchAll] = None

    @dataclasses.dataclass
    class Test:
        test: CatchAll
        a: CatchAll
        b: Optional[CatchAll]
        c: Optional[CatchAll] = None

    Test._init_()
    test = Test(test={"a": 1}, a={"b": 2})

   

# Generated at 2022-06-13 19:21:50.279263
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, a: int, b: int, c: CatchAll = None):
            self.a = a
            self.b = b
            self.c = c

    obj = TestClass(1, 2, {"d": 4})
    kvs = {"a": 1, "b": 2, "d": 4}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {"a": 1, "b": 2, "d": 4}

# Generated at 2022-06-13 19:21:55.000682
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    test_field = Field(name="test", type=int)
    result = _RaiseUndefinedParameters.handle_from_dict(cls=object,
                                                        kvs={"test": 0})
    assert result == {"test": 0}



# Generated at 2022-06-13 19:22:03.543156
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():

    @dataclasses.dataclass
    class Ball:
        x: int
        y: int
        color: str
        diameter: float = 5
        dimensions: Optional[CatchAll] = dataclasses.field(default_factory=dict)

    m = Ball(**dict(x=1, y=2, color="blue", diameter=10))
    assert m.x == 1
    assert m.y == 2
    assert m.color == "blue"
    assert m.diameter == 10
    assert m.dimensions == {}

    m = Ball(**dict(x=1, y=2, color="blue", diameter=10, volume=12))
    assert m.x == 1
    assert m.y == 2
    assert m.color == "blue"
    assert m.diameter == 10
    assert m.dim

# Generated at 2022-06-13 19:22:22.685738
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.decoder import Decoder
    from dataclasses_json.undefined import CatchAll


    @dataclasses.dataclass()
    class Foo:
        name: str
        catch_all: CatchAll = dataclasses.field(default=None)


    decoder = Decoder()
    obj = decoder.decode_dict(Foo, {"name": "test", "catch_all": {}, "test": 42})

    kvs = _CatchAllUndefinedParameters.handle_to_dict(
        obj=obj,
        kvs={"name": obj.name, "catch_all": obj.catch_all})

    assert kvs == {"name": "test", "test": 42}


# Generated at 2022-06-13 19:22:33.821462
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    import dataclasses

    @dataclasses.dataclass
    class A:
        a: str

    # No undefined parameters
    kvs = dict(a="a")
    result = _RaiseUndefinedParameters.handle_from_dict(A, kvs)
    assert result == kvs

    # Undefined extra parameter
    kvs = dict(a="a", b="b")
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(A, kvs)
    # Unit test for method handle_from_dict of class _IgnoreUndefinedParameters


# Generated at 2022-06-13 19:22:45.056325
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # noinspection PyUnusedLocal
    class TestClass:
        def __init__(self, a: Any, b: Any, c: Any, catch_all: CatchAll = None):
            ...


# Generated at 2022-06-13 19:22:46.016825
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    error = UndefinedParameterError("Test")
    assert error is not None

# Generated at 2022-06-13 19:22:53.010729
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass
    from dataclasses_json import config

    @dataclass
    class A:
        a: str
        b: int
        other: dataclasses_json.CatchAll = dict()

    A = config(undefined=Undefined.INCLUDE).patch_from_dict(
        A)
    a = A("a", b=1)
    assert a.a == "a"
    assert a.b == 1
    assert a.other == dict()

    A = config(undefined=Undefined.EXCLUDE).patch_from_dict(
        A)
    a = A("a", b=1)
    assert a.a == "a"
    assert a.b == 1
    assert a.other == dict()

# Generated at 2022-06-13 19:23:00.097577
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Test:
        d: Dict
        c: CatchAll

        def __init__(self, d: Dict, c: CatchAll = None):
            self.d = d
            self.c = c

    t = Test({"a": 1}, {"b": 2})
    result = _CatchAllUndefinedParameters.handle_to_dict(t, t.__dict__)
    expected = {"a": 1, "b": 2}
    assert result == expected

# Generated at 2022-06-13 19:23:01.942334
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError(
            "example error")
    except UndefinedParameterError as error:
        assert error.messages == ["example error"]
        assert error.fields == []

# Generated at 2022-06-13 19:23:13.783820
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        a: int
        b: str
        c: float = 1.0

        def __init__(self, a: int, b: str, c: float = 1.0):
            self.a = a
            self.b = b
            self.c = c

    new_init = _IgnoreUndefinedParameters.create_init(MyClass)

    @dataclass
    class MyClass:
        a: int
        b: str
        c: float = 1.0

        def __init__(self, a: int, b: str, c: float = 1.0):
            self.a = a
            self.b = b
            self.c = c


# Generated at 2022-06-13 19:23:14.569094
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    with pytest.raises(UndefinedParameterError):
        raise UndefinedParameterError()

# Generated at 2022-06-13 19:23:16.087289
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:23:43.463803
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump('') == {}

# Generated at 2022-06-13 19:23:48.361072
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # test with empty dict
    kvs = {}
    undefined = _UndefinedParameterAction.handle_to_dict(object, kvs)
    assert undefined is kvs

    # test with non-empty dict
    kvs = {'a': 1, 'b': 2}
    undefined = _UndefinedParameterAction.handle_to_dict(object, kvs)
    assert undefined is kvs



# Generated at 2022-06-13 19:23:50.501858
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    def test_func(self, *args, **kwargs):
        print("Test")

    init = _CatchAllUndefinedParameters.create_init(test_func)
    init("")

# Generated at 2022-06-13 19:23:57.267766
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        catch_all: CatchAllVar = dataclasses.field(
            default_factory=lambda: CatchAllVar({}))

        def __init__(self, *args, **kwargs):
            assert False

    init = _CatchAllUndefinedParameters.create_init(TestClass)

    try:
        init(1, 2, 3)
        assert False
    except TypeError:
        pass

    try:
        init(1, 2, 3, **{"catchall": CatchAllVar({})})
        assert False
    except TypeError:
        pass

    obj = init(1, 2, 3, **{"catch_all": CatchAllVar({})})
    assert obj.catch_all == CatchAllVar({})


# Generated at 2022-06-13 19:24:03.975304
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    dict_to_test = {'test': 'test', 'test2': 'test2', Undefined.EXCLUDE: 'test3'}

    handle_to_dict = Undefined.EXCLUDE.value.handle_to_dict(Dict[Any, Any], dict_to_test)
    handle_to_dict.pop(Undefined.EXCLUDE.name, None)

    assert dict_to_test == handle_to_dict

# Generated at 2022-06-13 19:24:15.326302
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class A:
        a: str
        b: str = "default"
        c: str = dataclasses.field(default_factory=lambda: "factory")

        _undefined_parameters: Optional[CatchAllVar] = \
            dataclasses.field(default_factory=dict)

    undefined_parameters_field = _CatchAllUndefinedParameters._get_catch_all_field(
        A)

    # initialization with CatchAll field
    kvs = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
    result = _CatchAllUndefinedParameters.handle_from_dict(A, kvs)

# Generated at 2022-06-13 19:24:20.990054
# Unit test for method handle_from_dict of class _UndefinedParameterAction

# Generated at 2022-06-13 19:24:29.871189
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    """
    Test the behavior of handle_from_dict() of _RaiseUndefinedParameters.
    """
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        """
        Test class for raising UndefinedParameterError.
        """
        a: int
        b: str = "B"

    # Get known_given_parameters, unknown_given_parameters.
    ret = _RaiseUndefinedParameters.handle_from_dict(kvs={"a": 1, "b": "D",
                                                          "c": 1.0},
                                                     cls=TestClass)
    known_given_parameters = ret

    # Only known_given_parameters are returned.
    assert len(known_given_parameters) == 2

# Generated at 2022-06-13 19:24:40.937536
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class TestClass:

        a: int
        b: str

        def __init__(self, **kwargs):
            self.a = kwargs["a"]
            self.b = kwargs["b"]

    # Test with positional arguments
    @dataclass
    class TestClass:
        a: int
        b: str
        c: Any

        def __init__(self, a: int, b: str, c: CatchAll):
            self.a = a
            self.b = b
            self.c = c


    modified_init = _IgnoreUndefinedParameters.create_init(obj=TestClass)
    TestClassWithCatchAll(1, 2, 3)


# Generated at 2022-06-13 19:24:48.932533
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import dataclasses
    from enum import Enum
    from typing import List
    from unittest.mock import Mock, patch

    from dataclasses_json import dataclass_json

    class Dummy(Enum):
        DUMMY = 1

    class DummyUndefinedParameterAction(_UndefinedParameterAction):
        @staticmethod
        def handle_from_dict(cls, kvs: Dict[str, Any]) -> Dict[str, Any]:
            return kvs

        @staticmethod
        def handle_to_dict(obj, kvs: Dict[str, Any]) -> Dict[str, Any]:
            return kvs


# Generated at 2022-06-13 19:25:45.526693
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    # Arrange
    class TestClass:
        pass

    kvs = {
        'y': 1,
        'a': 4,
        'b': 17,
        'z': 9
    }
    expected = kvs

    # Act
    actual = _UndefinedParameterAction.handle_to_dict(TestClass, kvs)

    # Assert
    assert actual == expected

# Generated at 2022-06-13 19:25:47.748220
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("Unit test")
    except UndefinedParameterError as error:
        assert error.args[0] == "Unit test"

# Generated at 2022-06-13 19:25:55.999525
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Test:
        a: int = 1
        b: int = 2
        c: Optional[CatchAllVar] = dataclasses.field(default_factory=dict)

    foo = Test.__new__(Test)
    kvs = {"a": 5, "b": 7, "d": 3, "e": 4}

    _CatchAllUndefinedParameters.handle_from_dict(Test, kvs)
    foo.__init__(**kvs)

    assert foo.a == 5
    assert foo.b == 7
    assert foo.c == {"d": 3, "e": 4}

# Generated at 2022-06-13 19:25:57.373836
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(object()) == {}

# Generated at 2022-06-13 19:26:06.228317
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, a: int, b: int):
            pass

    @dataclasses.dataclass
    class Bar:
        a: int
        b: int

    for cls in [Foo, Bar]:
        for kvs in [{"a": 42, "b": 43}, {"b": 43}, {"a": 42}]:
            result = _IgnoreUndefinedParameters.handle_from_dict(cls, kvs)
            assert result == {"a": 42, "b": 43}

        try:
            result = _IgnoreUndefinedParameters.handle_from_dict(cls,
                                                                 {"c": 42})
            assert result == {"a": 42, "b": 43}
        except ValidationError:
            pass



# Generated at 2022-06-13 19:26:17.305870
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from typing import List

    @dataclasses.dataclass
    class TestClassOne:
        l: list
        cap: str
        catch_all: Optional[CatchAll]

    obj = TestClassOne([], "hello", None)
    init = _CatchAllUndefinedParameters.create_init(obj)
    assert init(obj, [1, 2], "hallo") == TestClassOne.__init__(
        obj, l=[1, 2],
        cap="hallo",
        catch_all={})

    @dataclasses.dataclass
    class TestClassTwo:
        l: list
        cap: str

    obj = TestClassTwo([], "hello")
    init = _IgnoreUndefinedParameters.create_init(obj)

# Generated at 2022-06-13 19:26:23.059089
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class TestClass:
        a: int
        b: str

    kvs = {"a": 1, "b": "b", "c": "c"}
    result = _IgnoreUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {"a": 1, "b": "b"}



# Generated at 2022-06-13 19:26:30.435488
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters

# Generated at 2022-06-13 19:26:35.788603
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class A:
        x: str

    @dataclasses.dataclass
    class B:
        x: str

        def __init__(self, x: str, undefined: CatchAll = None):
            super().__init__(x=x)

    _UndefinedParameterAction.create_init(A)
    _UndefinedParameterAction.create_init(B)

# Generated at 2022-06-13 19:26:42.190613
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class TestClass:
        # noinspection PyTypeChecker
        def __init__(self, catch_all: CatchAll = None):
            self.catch_all = catch_all

    # noinspection PyTypeChecker
    obj = TestClass(
        {1: 2})
    assert obj.catch_all == {1: 2}
    assert _UndefinedParameterAction.handle_dump(obj) == {1: 2}

# Generated at 2022-06-13 19:28:47.305399
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass, field
    from enum import Enum

    from dataclasses_json import config, Undefined, dataclass_json

    class Undefined(Enum):
        """
        Choose the behavior what happens when an undefined parameter is
        encountered during class initialization.
        """
        INCLUDE = _CatchAllUndefinedParameters
        RAISE = _RaiseUndefinedParameters
        EXCLUDE = _IgnoreUndefinedParameters

    @dataclass_json
    @dataclass(undefined=Undefined.INCLUDE)
    class Greeting:
        """
        A greeting.
        """
        type: str = field(metadata=config(field_name="type"))
        message: str = field(metadata=config(field_name="message"))

# Generated at 2022-06-13 19:28:52.705945
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # noinspection PyUnresolvedReferences
    @dataclasses.dataclass(init=False)
    class A:
        x: int
        y: int
        ca: CatchAll

    a = A(x=1, y=1, ca=dict(a=1, b=2))
    assert (a.x, a.y, a.ca) == (1, 1, {"a": 1, "b": 2})


# Generated at 2022-06-13 19:28:58.802282
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    """
    This test ensures that the method handle_to_dict of class
    _UndefinedParameterAction is defined
    for all members of the Enum Undefined.
    """
    for undefined_parameter_behavior in Undefined:
        assert getattr(undefined_parameter_behavior.value,
                       "handle_to_dict") is not None

# Generated at 2022-06-13 19:29:00.448921
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:29:08.546659
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class A:
        def __init__(self, *, a: int, b: int, **kwargs):
            pass

    class B:
        def __init__(self, *, a: int, b: int, c: int, **kwargs):
            pass

    class C:
        def __init__(self, *args, **kwargs):
            pass

    assert _IgnoreUndefinedParameters.create_init(A)(A, a=1, b=2, c=3)
    assert _IgnoreUndefinedParameters.create_init(B)(B, a=1, b=2, c=3)
    assert _IgnoreUndefinedParameters.create_init(
        C)(C, a=1, b=2, c=3, d=4, e=5, f=6, g=7)




# Generated at 2022-06-13 19:29:23.049710
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass
    from marshmallow import fields as ma_fields

    @dataclass
    class TestClass:
        initial: str
        known: int
        additional_1: str
        additional_2: int
        undefined: CatchAll = None

    test_class_dict = {
        "initial": "test_value",
        "known": 123,
        "additional_1": "test_additional_1",
        "unknown_1": "test_unknown_1",
        "unknown_2": 123,
        "additional_2": "test_additional_2"
    }

# Generated at 2022-06-13 19:29:26.314737
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    with pytest.raises(UndefinedParameterError):
        raise UndefinedParameterError("test")

# Generated at 2022-06-13 19:29:40.589525
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # Need mock dataclass and fields of type CatchAll to properly test this
    # method.
    # The fields are not correctly identified by mypy as CatchAll, so have to
    # use type ignore.
    from unittest.mock import Mock, MagicMock

    class DataClass(object):
        def __init__(self, cls_field, catch_all_field):
            self.cls_field = cls_field
            self.catch_all_field = catch_all_field

        def __eq__(self, other):
            return self.cls_field == other.cls_field and \
                   self.catch_all_field == other.catch_all_field

        def __hash__(self):
            return hash(self.cls_field) + hash(self.catch_all_field)

   

# Generated at 2022-06-13 19:29:50.194227
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class ExampleClass:
        a: int
        b: int
        c: str
        d: Optional[str] = None
        unknown: CatchAll = None

        def __init__(self, a, b, c, d=None, unknown=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.unknown = unknown


    example_class = ExampleClass(a=1, b=2, c="unit testing", d="unit",
                                 unknown={"test": "pass"})
    assert example_class.a == 1
    assert example_class.b == 2
    assert example_class.c == "unit testing"
    assert example_class.d == "unit"

# Generated at 2022-06-13 19:30:00.866821
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # ----------------------------------
    # utility functions

    def get_init_signature(cls) -> inspect.Signature:
        return inspect.signature(getattr(cls, "__init__", None))

    def get_num_init_params(cls) -> int:
        return len(get_init_signature(cls).parameters)

    def create_class(class_name: str, *args, **defaults):
        return type(class_name, (object,), {
            "__init__": lambda self, *args, **kwargs: None,
            **defaults,
        })
