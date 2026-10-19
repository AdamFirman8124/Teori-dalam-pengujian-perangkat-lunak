

# Generated at 2022-06-13 19:20:41.901470
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    def __init__(self, *args, **kwargs):
        pass

    _IgnoreUndefinedParameters.create_init(__init__)

# Generated at 2022-06-13 19:20:42.613186
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    pass

# Generated at 2022-06-13 19:20:52.883734
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Foo:
        a: int
        b: int

        def __init__(self, a, b):
            self.a = a
            self.b = b

    # check that no exception is raised if init does not have `self`
    @dataclasses.dataclass
    class Foo:
        a: int
        b: int

        def __init__(self, a, b):
            pass

    # check that no exception is raised if init has `self`
    Foo(1, 2)

    # check that no exception is raised if init has `self` and the number of
    # supplied arguments exceeds the number of arguments to __init__
    Foo(1, 2, 4)



# Generated at 2022-06-13 19:20:54.029386
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("test")

# Generated at 2022-06-13 19:21:03.015447
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # Test receiving a defined argument
    class TestClass:
        def __init__(self, a: int):
            self.a = a
    kvs = {"a": 1}
    expected = {"a": 1}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == expected
    # Test receiving an undefined argument
    class TestClass:
        # no further arguments
        pass
    kvs = {"a": 1}
    expected = UndefinedParameterError
    with pytest.raises(expected):
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    # Test receiving zero arguments
    class TestClass:
        def __init__(self):
            pass
    kvs = {}
    expected = {}
    result = _RaiseUndefined

# Generated at 2022-06-13 19:21:12.729851
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Test:
        def __init__(self, a: str, b: str, c: str):
            self.a = a
            self.b = b
            self.c = c

    t = Test("a", "b", "c")
    init = _IgnoreUndefinedParameters.create_init(t)

    class Test2:
        def __init__(self, a: str, b: str, c: str, d: str, e: str, f: str):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    t2 = Test2("a", "b", "c", "d", "e", "f")

# Generated at 2022-06-13 19:21:21.762767
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class A:
        def __init__(self, a: str):
            self.a = a

    @dataclasses.dataclass
    class B:
        a: str
        b: int

    assert _RaiseUndefinedParameters.handle_from_dict(obj=A,
                                                      kvs={"a": "str"}) == \
           {"a": "str"}

    assert _RaiseUndefinedParameters.handle_from_dict(obj=B,
                                                      kvs={"a": "str",
                                                           "b": 2}) == \
           {"a": "str",
            "b": 2}


# Generated at 2022-06-13 19:21:26.544520
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass()
    class TestClass:
        foo: int = 1
        bar: str = "Bar"
        baz: Optional[CatchAllVar] = None
        __undefined__ = "RAISE"

    test_class_init: Callable = \
        _CatchAllUndefinedParameters.create_init(TestClass)

    # check that the original init is not modified
    assert TestClass.__init__ == \
           dataclasses.dataclass(TestClass).__init__

    # check that the parameters are parsed correctly
    instance = test_class_init(TestClass(), foo=42, baz=dict())
    assert instance.foo == 42
    assert instance.bar == "Bar"
    assert instance.baz == dict()

    # check that parameter foo can not be overwritten

# Generated at 2022-06-13 19:21:39.045265
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from inspect import signature

    @dataclasses.dataclass
    class Klass:
        a: str
        b: str
        c: str

    kobject = Klass("a", "b", "c")
    kobject_init = kobject.__init__
    assert signature(kobject_init) == signature(
        _UndefinedParameterAction.create_init(Klass))

    # Now the hard case
    Klass_with_Ignore = dataclasses.dataclass(
        Klass,
        init=True,
        repr=True,
        eq=True,
        order=False,
        unsafe_hash=False,
        frozen=False)

# Generated at 2022-06-13 19:21:50.597278
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Whatever:
        a: int
        b: CatchAll = dataclasses.field(default=None, metadata={})

    data = {
        "a": 1,
        "c": 2,
        "b": 3
    }
    parameters = _CatchAllUndefinedParameters.handle_from_dict(Whatever, data)
    assert parameters["a"] == 1
    assert parameters["b"] == {"c": 2}

    data = {
        "a": 1,
    }
    parameters = _CatchAllUndefinedParameters.handle_from_dict(Whatever, data)
    assert parameters["a"] == 1
    assert parameters["b"] == {}

    data = {
        "a": 1,
        "c": 2
    }

# Generated at 2022-06-13 19:22:12.202301
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Example:
        def __init__(self, a, b, cat: Optional[CatchAllVar] = {}):
            self.a = a
            self.b = b
            self.cat = cat

    example = Example(a=1, b=2, cat={1: "cat"})
    assert example.a == 1
    assert example.b == 2
    assert example.cat == {1: "cat"}

    example = Example(a=1, b=2)
    assert example.a == 1
    assert example.b == 2
    assert example.cat == {}

    class Example2:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    with pytest.raises(ValueError):
        _UndefinedParameterAction.create_init(Example2)

# Generated at 2022-06-13 19:22:20.560558
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class _TestClass:
        defined_parameter: int
        undefined_parameter_1: int
        undefined_parameter_2: int

        def __init__(self, defined_parameter: int, *,
                     undefined_parameter_1: int,
                     undefined_parameter_2: int):
            self.defined_parameter = defined_parameter
            self.undefined_parameter_1 = undefined_parameter_1
            self.undefined_parameter_2 = undefined_parameter_2


# Generated at 2022-06-13 19:22:23.897965
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    try:
        _RaiseUndefinedParameters.handle_from_dict(
            dataclasses.make_dataclass("Foo", [("y", int)]), {"x": 5})
        raise AssertionError("Did not raise")
    except UndefinedParameterError:
        pass

# Generated at 2022-06-13 19:22:33.486036
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        param1: int
        param2: int

    kvs: Dict[str, Any] = {'param1': 1, 'param2': 2, 'param3': 3}
    assert _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs) == \
           {'param1': 1, 'param2': 2}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)


# Generated at 2022-06-13 19:22:44.794024
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestClass:
        user_dict = CatchAll
        t = 5

    # noinspection PyTypeChecker
    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                           {"t": 5,
                                                            "user_dict": {
                                                                "x": 2, "y": 3}})
    assert result["t"] == 5
    assert result["user_dict"]["x"] == 2
    assert result["user_dict"]["y"] == 3

    # noinspection PyTypeChecker

# Generated at 2022-06-13 19:22:46.056306
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump({}) == {}
    assert _UndefinedParameterAction.handle_dump(None) == {}


# Generated at 2022-06-13 19:22:53.111842
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class _TestClass:
        def __init__(self,
                     _arg2: str,
                     _arg3: dict,
                     _arg4: int,
                     _arg5: float,
                     _arg6: bool,
                     _arg7: str,
                     _arg8: int,
                     _arg9: float,
                     _arg10: bool,
                     _arg11: str,
                     _arg12: int,
                     _arg13: float,
                     _arg14: bool,
                     _arg15: str,
                     _arg16: int,
                     _arg17: float,
                     _arg18: bool,
                     catch_all: Optional[CatchAllVar] = None,
                     ):
            pass

    @dataclasses.dataclass
    class TestClass:
        _arg2: str
        _

# Generated at 2022-06-13 19:22:56.339849
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    data = {"a": 1, "b": 2}
    result = _UndefinedParameterAction.handle_to_dict(None, data)
    assert data == result

# Generated at 2022-06-13 19:23:03.215323
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Test for method create_init of class _IgnoreUndefinedParameters.
    """
    @dataclasses.dataclass()
    class TestDataClass:
        a: int
        b: str

    init_signature = inspect.signature(TestDataClass.__init__)
    ignore_init = _IgnoreUndefinedParameters.create_init(TestDataClass)
    ignore_init_signature = inspect.signature(ignore_init)
    assert (init_signature.parameters.keys() ==
            ignore_init_signature.parameters.keys())



# Generated at 2022-06-13 19:23:08.488093
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():

    class Example:
        def __init__(self, a, b, c):
            pass

    dict_1 = {"a": 1, "b": 2, "c": 3}
    assert _UndefinedParameterAction.handle_from_dict(Example, dict_1) == \
           dict_1

    dict_2 = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert _UndefinedParameterAction.handle_from_dict(Example, dict_2) == \
           dict_1

    dict_3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    assert _UndefinedParameterAction.handle_from_dict(Example, dict_3) == \
           dict_1



# Generated at 2022-06-13 19:23:43.787555
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass


    @dataclass
    class Test:
        catch_all: Optional[CatchAllVar]

        def __init__(self, **kwargs):
            return 5


    new_init = _CatchAllUndefinedParameters.create_init(cls=Test)
    assert new_init(obj=Test, *[1, 2, 3, 4], **{"catch_all": {}, "a": 5}) == 5

    @dataclass
    class Test:
        catch_all: Optional[CatchAllVar]

        def __init__(self, a: int, b: int, c: int, d: int, catch_all=None):
            return a + b + c + d


    new_init = _CatchAllUndefinedParameters.create_init(Test)
   

# Generated at 2022-06-13 19:23:49.337351
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Mock:
        catchall: CatchAll = None

    init = _CatchAllUndefinedParameters.create_init(Mock)
    mock = Mock(a=1, catchall={"b": 2})
    assert mock.a == 1
    assert mock.catchall == {"b": 2}
    mock = Mock(a=1, b=2)
    assert mock.a == 1
    assert mock.catchall == {"b": 2}

# Generated at 2022-06-13 19:23:50.386906
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:23:52.473732
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():

    _CatchAllUndefinedParameters.create_init(obj=None)

    # noinspection PyProtectedMember
    assert "CatchAll" in repr(_CatchAllUndefinedParameters)

# Generated at 2022-06-13 19:23:55.446954
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class Foo:
        a: str


    try:
        _RaiseUndefinedParameters.handle_from_dict(
            Foo, {"a": "x", "b": "y"})
    except UndefinedParameterError:
        pass
    else:
        assert False


# Generated at 2022-06-13 19:24:11.585995
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import inspect

    class Object:
        pass

    init_signature = inspect.signature(Object.__init__)
    number_of_parameters = len(init_signature.parameters) - 1

    def create_init(num_taken_parameters):
        def validate_partial_init(num_taken_parameters):
            @functools.wraps(Object.__init__)
            def partial_init(*args, **kwargs):
                known_kwargs, _ = _CatchAllUndefinedParameters \
                    ._separate_defined_undefined_kvs(Object, kwargs)
                num_args_takeable = \
                    num_taken_parameters - len(known_kwargs)

                args = args[:num_args_takeable]
                bound_parameters = init_sign

# Generated at 2022-06-13 19:24:13.377336
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    error = UndefinedParameterError("Test")
    assert error.args[0] == "Test"

# Generated at 2022-06-13 19:24:24.533688
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class _ClassWithUndefinedParameters:
        def __init__(self, a: int, b: str, _undefined: Optional[CatchAll]):
            self.a = a
            self.b = b
            self._undefined = _undefined

        @classmethod
        def from_dict(cls, **kwargs) -> '_ClassWithUndefinedParameters':
            _CatchAllUndefinedParameters.handle_from_dict(cls, kvs=kwargs)
            return cls(**kwargs)

    test_dict = {"a": 2, "b": "4", "c": "5", "d": "6"}
    test_instance = _ClassWithUndefinedParameters.from_dict(**test_dict)

# Generated at 2022-06-13 19:24:28.419470
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # We only care about the signature of the function and not its behavior
    class MyClass:
        def __init__(self, catch_all: CatchAll = None, **kwargs):
            pass

    assert _UndefinedParameterAction.create_init(MyClass) == MyClass.__init__
    assert _UndefinedParameterAction.create_init(MyClass) == MyClass.__init__

# Generated at 2022-06-13 19:24:38.050336
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    import dataclasses
    import marshmallow
    import dataclasses_json
    import enum


    class CatType(enum.Enum):
        PERSIAN = "persian"
        RUSSIAN_BLUE = "russian_blue"


    @dataclasses.dataclass()
    class Cat:
        name: str
        age: int
        type: CatType = CatType.PERSIAN
        catch_all: dataclasses_json.CatchAll = dataclasses_json.field(
            default_factory=dict)


    c = Cat("Ginger", 12)
    # Add some undefined parameters
    c.catch_all["origin"] = "Iran"
    c.catch_all["color"] = "Black"

    schema = dataclasses_json.schema(Cat)


# Generated at 2022-06-13 19:25:35.878039
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Dummy:
        # noinspection PyArgumentList
        def __init__(self, foo: int, bar: str,
                     undefined: Optional[CatchAllVar] = None):
            self.foo = foo
            self.bar = bar
            self.undefined = undefined

    obj = Dummy(foo=42, bar="bar_value", undefined={"key": "value"})
    kvs = _CatchAllUndefinedParameters.handle_to_dict(obj, {"foo": 42,
                                                             "bar": "bar_value",
                                                             "undefined":
                                                                 {"key":
                                                                      "value"}})
    expected = {"foo": 42, "bar": "bar_value", "key": "value"}
    assert kvs == expected

# Generated at 2022-06-13 19:25:37.292125
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("Test")
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:25:48.529351
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class FooBar:
        def __init__(self, foo: int = 42, bar: int = 23,
                     catch_all: Optional[CatchAllVar] = None):
            self.foo = foo
            self.bar = bar
            self.catch_all = catch_all or {}

    init = _CatchAllUndefinedParameters.create_init(FooBar)
    fb1 = FooBar(123, 456)
    fb2 = FooBar(123, 456, {"other": "arg"})
    fb3 = FooBar(123, 456, {"key1": "value1"})
    fb4 = FooBar(123, 456, {"key1": "value1", "key2": "value2"})

# Generated at 2022-06-13 19:25:56.252473
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Test(_UndefinedParameterAction):
        def __init__(self, a: int, c: int = 4):
            pass

        __init_not_decorated = (lambda self, a, c=4: None) # type: ignore

    test = Test.__init_not_decorated
    assert {"a": 2} == _UndefinedParameterAction.handle_from_dict(test,
                                                                  {"a": 2})
    with pytest.raises(UndefinedParameterError):
        _UndefinedParameterAction.handle_from_dict(test, {"a": 2, "b": 2})



# Generated at 2022-06-13 19:26:05.626540
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from marshmallow.exceptions import ValidationError
    from marshmallow.fields import Field

    class Thing:
        def __init__(self, name: str, age: int, *,
                     catch_all: Optional[CatchAllVar] = None):
            self._name = name
            self._age = age
            self._catch_all = catch_all

        @property
        def name(self) -> str:
            return self._name

        @property
        def age(self) -> int:
            return self._age

        @property
        def catch_all(self) -> Optional[CatchAllVar]:
            return self._catch_all


# Generated at 2022-06-13 19:26:12.252912
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    from dataclasses import dataclass
    from dataclasses_json import config

    @dataclass
    class TestClass:
        test1: int = 1
        test2: str = "test"

    test_class = TestClass()


# Generated at 2022-06-13 19:26:23.632209
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    def original_init(self, a, b, c=1, d=1, e=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    class TestClass:
        def __init__(self, a, b, c=1, d=1, e=1):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

    def test_init_method_baseline(obj, args, kwargs):
        original_init(obj, *args, **kwargs)


# Generated at 2022-06-13 19:26:26.136456
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    kvs = {"a": 1, "b": 2, "c": 3}
    result = _UndefinedParameterAction.handle_from_dict(kvs)
    assert result == kvs
    # The argument cls is not used, so it can be anything
    result = _UndefinedParameterAction.handle_from_dict(cls="", kvs=kvs)
    assert result == kvs

# Generated at 2022-06-13 19:26:37.137817
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class SimpleClass:
        """
        Simple class with a single field of type int
        """

        def __init__(self, my_int: int):
            self.my_int = my_int

    assert _RaiseUndefinedParameters.handle_from_dict(
        cls=SimpleClass, kvs={}) == {}

    assert _RaiseUndefinedParameters.handle_from_dict(
        cls=SimpleClass, kvs={"my_int": 5}) == {"my_int": 5}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(cls=SimpleClass,
                                                   kvs={"unknown_field": 5})

    # Multiple undefined fields
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle

# Generated at 2022-06-13 19:26:45.547540
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import marshmallow
    from dataclasses_json.utils import CatchAllVar

    def init(self, a: int, b: str, c: CatchAllVar=None):
        pass

    # noinspection PyProtectedMember
    sig = inspect.signature(init)
    catch_all_init_function = _CatchAllUndefinedParameters.create_init(
        init)

    @dataclasses.dataclass
    class SomeClass:
        a: int
        b: str
        c: Optional[CatchAllVar] = dataclasses.field(default=None)

        def __init__(self, *args, **kwargs):
            bound_parameters = sig.bind(self, *args, **kwargs)
            bound_parameters.apply_defaults()

# Generated at 2022-06-13 19:29:08.968888
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class MyTestClass:
        x: int = dataclasses.field(default=0)
        y: Optional[int]
        z: Optional[str]
        catch_all: Optional[CatchAllVar]

    assert _CatchAllUndefinedParameters.handle_from_dict(MyTestClass,
                                                         {"x": 2,
                                                          "y": 3,
                                                          "z": "a"}) == {
        "x": 2,
        "y": 3,
        "z": "a",
        "catch_all": {},
    }


# Generated at 2022-06-13 19:29:23.156344
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class _TestClass:
        catch_all: CatchAll = None

    kvs = {"a": 1, "b": 2, "c": 3}
    known_parameters, _ = \
        _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
            cls=_TestClass, kvs=kvs)
    final_parameters = \
        _CatchAllUndefinedParameters.handle_from_dict(cls=_TestClass,
                                                      kvs=known_parameters)
    assert final_parameters == {'catch_all': kvs}

    # Test default value
    @dataclasses.dataclass
    class _TestClassWithDefault:
        catch_all: CatchAll = {"some_default": 1}


# Generated at 2022-06-13 19:29:38.012523
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class _C:
        def __init__(self, x):
            self.x = x

    assert _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=_C, kvs={"x": 5}) == ({'x': 5}, {})
    assert _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=_C, kvs={"x": 5, "z": 100}) == ({'x': 5}, {'z': 100})
    assert _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=_C, kvs={"z": 100}) == ({}, {'z': 100})


# Generated at 2022-06-13 19:29:48.398183
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import pytest

    class TestClass:
        def __init__(self, catch_all: Optional[CatchAllVar] = None):
            self.catch_all = catch_all

    test_object = TestClass(catch_all={"key": 1})
    kvs = {"some_key": "some_value", "key": "mykey"}
    result = _CatchAllUndefinedParameters.handle_to_dict(test_object, kvs)
    assert result["key"] == 1
    assert result["some_key"] == "some_value"

    test_object = TestClass(catch_all={"key": 1})
    kvs = {"some_key": "some_value", "key": "mykey"}
    test_object.key = "a value"
    result = _CatchAllUndefinedParameters.handle_

# Generated at 2022-06-13 19:29:56.207700
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, field1, field2, field3):
            pass

        def __repr__(self):
            return f"{self.__class__.__name__}()"

    # dict with known and unknown parameters
    kvs = {"field1": 1, "field2": 2, "field3": 3, "field4": 4}

    # dictionary with known parameters only
    result = _IgnoreUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {"field1": 1, "field2": 2, "field3": 3}



# Generated at 2022-06-13 19:30:01.807758
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    def init(self, x: int = 2, y: int = 3):
        pass


    class TestClass:
        def __init__(self, x: int = 2, y: int = 3):
            pass


    for undefined in Undefined:
        init_function = _UndefinedParameterAction.create_init(TestClass)
        assert init_function(TestClass) == init

# Generated at 2022-06-13 19:30:03.951005
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    error = UndefinedParameterError(msg="Hello")
    assert str(error) == "Hello"


# Generated at 2022-06-13 19:30:04.872990
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # Test constructor
    UndefinedParameterError()



# Generated at 2022-06-13 19:30:12.039291
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    one_to_ten = range(1, 10)

    @dataclasses.dataclass
    class CatchAllClass:
        a: str
        b: str
        c: Optional[CatchAllVar] = None

    valid_data = {"a": "a", "b": "b"}
    data_with_valid_extra_data = {"a": "a", "b": "b", "c": {
        "a": "a", "b": "b"}}
    data_with_unknown_extra_data = {"a": "a", "b": "b", "c": {
        "d": "d", "e": "e"}}
    data_with_invalid_extra_data_type = {"a": "a", "b": "b", "c": one_to_ten}
    data_with_

# Generated at 2022-06-13 19:30:20.588928
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestClass():
        def __init__(self, foo: str, a: int, b: int, c: int,
                     catch_all: Optional[CatchAllVar] = None):
            pass

    @dataclasses.dataclass
    class TestDataclass:
        foo: str
        a: int
        b: int
        c: int
        catch_all: Optional[CatchAllVar] = None

    # -- Dataclass tests --
    kvs_dataclass = {"foo": "bar", "a": 1, "b": 2, "c": 3}

    k, u = _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
        TestDataclass, kvs_dataclass)
