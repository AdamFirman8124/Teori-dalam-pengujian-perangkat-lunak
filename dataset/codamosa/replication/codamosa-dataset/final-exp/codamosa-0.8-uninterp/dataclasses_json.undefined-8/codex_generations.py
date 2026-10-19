

# Generated at 2022-06-13 19:20:36.771497
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}


# Generated at 2022-06-13 19:20:49.461370
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class MyClass:
        foo: str
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict, metadata=dict(undefined=Undefined.RAISE))

    example_input = dict(foo="bar", this_is_unknown=1)

    known_parameters_out, unknown_parameters_out = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=MyClass, kvs=example_input)

    assert known_parameters_out == dict(foo="bar")
    assert unknown_parameters_out == dict(this_is_unknown=1)


# Generated at 2022-06-13 19:20:56.736778
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class C:
        def __init__(self, a, b=1, c=2, d=3):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    init_func = _IgnoreUndefinedParameters.create_init(C)

    assert init_func(C(), 1) == C(1)
    assert init_func(C(), 1, 2) == C(1, b=2)
    assert init_func(C(), 1, 2, 3, 4) == C(1, b=2, c=3, d=4)
    assert init_func(C(), 1, 2, 3, 4, 5) == C(1, b=2, c=3, d=4)

# Generated at 2022-06-13 19:21:01.503128
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class ExampleClass:
        @dataclasses.dataclass
        class _ExampleClass:
            foo: str
            bar: str

        def __init__(self, foo: str, bar: str):
            self.foo: str = foo
            self.bar: str = bar

    # Test Raise
    action = Undefined.RAISE
    class_ = ExampleClass._ExampleClass
    kvs = {"foo": "spam", "bar": "eggs", "baz": "undefined"}
    with pytest.raises(UndefinedParameterError):
        action.value.handle_from_dict(cls=class_, kvs=kvs)

    # Test Ignore
    action = Undefined.EXCLUDE
    class_ = ExampleClass._ExampleClass

# Generated at 2022-06-13 19:21:10.610521
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    global_state = {}

    def get_global_state() -> Dict[str, Any]:
        return global_state

    def init_class(*, defined_parameter: int,
                   **kwargs) -> None:
        global_state.update(kwargs)

    # No extra parameters given
    args = dict(defined_parameter=42)
    expected_unknown_parameters = dict()
    kwargs = _IgnoreUndefinedParameters.handle_from_dict(
        init_class, args)
    assert kwargs == dict(defined_parameter=42)
    get_global_state() == expected_unknown_parameters

    # One more parameter given
    given_parameters = dict(defined_parameter=42, hello="world")

# Generated at 2022-06-13 19:21:17.167171
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        data: str

        def __init__(self, data: str):
            self.data = data

    test_instance = TestClass("Test")
    assert _RaiseUndefinedParameters.handle_from_dict(
        TestClass, {"data": "foo", "other": "bar"}
    ) == {"data": "foo"}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(
            TestClass, {"other": "bar"}
        )



# Generated at 2022-06-13 19:21:24.527720
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from typing import Dict
    from dataclasses_json.core import _CatchAllUndefinedParameters, _undefined

    class A:
        def __init__(self, _undefined: Dict[str, Any] = {}):
            self._undefined = _undefined

    x = A()
    assert _CatchAllUndefinedParameters.handle_to_dict(A,
                                                       {"_undefined": 1}) \
           == {"_undefined": {}}
    assert _CatchAllUndefinedParameters.handle_to_dict(A,
                                                       {"_undefined": {},
                                                        "a": 1}) \
           == {"a": 1}



# Generated at 2022-06-13 19:21:37.493004
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import copy

    class MyClass:
        def __init__(self, param_1: str, param_2: int, *,
                     param_3: str = "default string",
                     catch_all: Optional[CatchAllVar] = None):
            pass

    original_init = MyClass.__init__
    ignore_init = _CatchAllUndefinedParameters.create_init(MyClass)
    assert original_init is not ignore_init
    assert original_init.__name__ == ignore_init.__name__
    assert original_init.__doc__ == ignore_init.__doc__
    assert copy.copy(
        original_init.__annotations__) == copy.copy(ignore_init.__annotations__)


if __name__ == "__main__":
    import doctest

    doctest.testmod

# Generated at 2022-06-13 19:21:42.797866
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class X:
        a: str
        b: int
        c: int = dataclasses.field(default=3)
        catch_all: Optional[CatchAllVar] = None

    assert X(a="a", b=2).catch_all == {}

    # Input is empty:
    assert _CatchAllUndefinedParameters.handle_from_dict(
        X, {}) == {"a": None, "b": None, "c": 3, "catch_all": {}}
    assert _CatchAllUndefinedParameters.handle_from_dict(
        X, {"a": "a"}) == {"a": "a", "b": None, "c": 3, "catch_all": {}}

# Generated at 2022-06-13 19:21:55.756061
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Tests whether create_init method of class _IgnoreUndefinedParameters
    ignores all but the first n arguments and all but the first n keyword
    arguments.
    """


    class TestClass:
        def __init__(self, a: str, b: str, c: str, d: str, e: str, f: str):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f


    initialization_params = ["a", "b", "c", "d", "e", "f"]
    init_kwargs = dict()
    for i in range(len(initialization_params)):
        initialisation_param = initialization_params[i]

# Generated at 2022-06-13 19:22:16.210012
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class A:
        def __init__(self, foo: str, bar: str, baz: str):
            self.foo = foo
            self.bar = bar
            self.baz = baz

    a = A("foo", "bar", "baz")

    expected = {"foo": "foo", "bar": "bar", "baz": "baz"}
    result = _UndefinedParameterAction.handle_to_dict(obj=A, kvs=expected)
    assert result == expected

    result = _IgnoreUndefinedParameters.handle_to_dict(a=a, kvs=expected)
    assert result == expected



# Generated at 2022-06-13 19:22:18.364100
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Unit test for method handle_dump of class _UndefinedParameterAction
    """
    test_object = _UndefinedParameterAction()
    dump = test_object.handle_dump(1)
    assert dump == {}

# Generated at 2022-06-13 19:22:24.172694
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        x: int
        y: int

    def _test_function(**kwargs):
        return _RaiseUndefinedParameters.handle_from_dict(
            TestClass, kwargs)

    assert _test_function(x=1, y=2) == dict(x=1, y=2)
    assert _test_function(x=3, y=4, z=5) == dict(x=3, y=4)

    with pytest.raises(UndefinedParameterError):
        _test_function(z=5)



# Generated at 2022-06-13 19:22:36.122673
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from unittest.mock import Mock, patch
    from marshmallow import Schema

    class MyClass:
        def __init__(self, known1: str, known2: int,
                     catch_all: Optional[CatchAllVar] = None):
            self.known1 = known1
            self.known2 = known2
            self.catch_all = catch_all
            self.tracked_call = Mock()

        __init__.__signature__ = inspect.signature(__init__)

        def __eq__(self, other):
            if isinstance(other, MyClass):
                return self.known1 == other.known1 and \
                       self.known2 == other.known2 and \
                       self.catch_all == other.catch_all
            else:
                return False


# Generated at 2022-06-13 19:22:46.939338
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    from marshmallow import Schema, fields
    from dataclasses_json.utils import CatchAllVar

    @dataclasses.dataclass
    class _Test(_UndefinedParameterAction):
        a: str
        b: str
        UNKNOWN: CatchAllVar = dataclasses.field()

        @property
        def _undefined(self):
            return self.UNKNOWN

        def _set_undefined(self, parameters: dict) -> None:
            self.UNKNOWN.update(parameters)

    test_object = _Test("a", "b", {"c": 1, "d": "e"})
    test_object.UNKNOWN.update({"f": 2})
    kvs = {"a": "a", "b": "b", "c": 1, "d": "e", "f": 2}
    assert test_

# Generated at 2022-06-13 19:22:49.360963
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = dataclasses.dataclass()(foo=1)
    method_under_test = _UndefinedParameterAction.handle_dump
    assert method_under_test(obj) == {}
    assert method_under_test(obj=1) == {}

# Generated at 2022-06-13 19:22:58.068168
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        x: int
        y: int
        z: int = _IgnoreUndefinedParameters.UNWRITTEN_FIELD
        _UNDEFINED = Undefined.INCLUDE

    kvs = {"x": 1, "y": 2, "z": 3, "_not_used": "something", "_another": 4}
    defined_parameters = _IgnoreUndefinedParameters.handle_from_dict(
        cls=TestClass,
        kvs=kvs)
    assert defined_parameters == {"x": 1, "y": 2, "z": 3}



# Generated at 2022-06-13 19:23:02.752658
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        foo: int
        bar: int
        undefined: int = _RaiseUndefinedParameters.handle_from_dict(
            MyClass, dict(foo=1, bar=2, foo=3))

    obj = MyClass(1, 2)
    assert obj.foo == 1
    assert obj.bar == 2



# Generated at 2022-06-13 19:23:09.064159
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # Case where nothing is specified

    class TestNoDefault(metaclass=CatchAllUndefinedParameters):
        a: int
        b: str
        c: CatchAllVar

    no_default_res = _CatchAllUndefinedParameters.handle_from_dict(
        TestNoDefault, {"a": 1, "b": "hello"})

    assert no_default_res == {"a": 1, "b": "hello", "c": {}}

    # Case where parameter is specified before as a value
    class TestDefault(metaclass=CatchAllUndefinedParameters):
        a: int
        b: str
        c: CatchAllVar = {"c": "hello"}

    default_res = _CatchAllUndefinedParameters.handle_from_dict(
        TestDefault, {"a": 1, "b": "hello"})

   

# Generated at 2022-06-13 19:23:14.906920
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    catch_all_field = Field(name="catch_all", type=Optional[CatchAllVar])

    unknown_kvs = {"unknown": 1, "unknown2": 2}
    known_kvs = {"a": 1, "b": 2}
    kvs = {**unknown_kvs, **known_kvs}

    expected = {**unknown_kvs, **known_kvs, "catch_all": unknown_kvs}
    result = _CatchAllUndefinedParameters.handle_from_dict(
        cls=CatchAllVar, catch_all_field=catch_all_field, kvs=kvs)
    assert result == expected

    # test default value
    default_value = 1

# Generated at 2022-06-13 19:23:58.015047
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from typing import TypeVar
    from dataclasses import dataclass

    T = TypeVar('T', bound='A')

    @dataclass(unsafe_hash=True)
    class A:
        b: str
        c: Optional[CatchAllVar] = None

        def __init__(self, **kwargs: Any) -> None:
            super().__init__()

    assert _CatchAllUndefinedParameters.handle_from_dict(A, {
        "b": "B",
        "c": {"d": "D"}
    }) == {'b': 'B', 'c': {'d': 'D'}}


# Generated at 2022-06-13 19:24:09.635815
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class A:
        def __init__(self, a: Optional[CatchAllVar] = None):
            self.a = a

    c = A()
    assert c.a is None
    c = A(a={'b': 5})
    assert c.a == {'b': 5}

    c = _CatchAllUndefinedParameters.handle_from_dict(A, {'a': {'a': 1}, 'b': 5})
    assert isinstance(c['a'], dict)
    assert c['a'] == {'a': 1, 'b': 5}

    c = _CatchAllUndefinedParameters.handle_from_dict(A, {'b': 5})
    assert isinstance(c['a'], dict)
    assert c['a'] == {'b': 5}

    c = _Catch

# Generated at 2022-06-13 19:24:10.316126
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    exception = UndefinedParameterError("error")
    assert str(exception) == "error"

# Generated at 2022-06-13 19:24:21.250456
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    from dataclasses import dataclass
    from dataclasses_json import config

    @dataclass
    class MyClass:
        a: int = 1
        catch_all: CatchAll = field(metadata=config(undefined=Undefined.INCLUDE))
        b: int = 2
        c: int = 3

    instance = MyClass({"does_not_exist": 3})

    # Check that all undefined fields have been set to the catch_all field
    assert getattr(instance, "a") == 1
    assert getattr(instance, "catch_all").get("a") is None
    assert getattr(instance, "catch_all").get("b") == 2
    assert getattr(instance, "catch_all").get("c") == 3

# Generated at 2022-06-13 19:24:30.065841
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Tests if _IgnoreUndefinedParameters.create_init works properly.
    """

    class Example:
        def __init__(self, a, b, c: int = 3, d: str = "d",
                     e: Optional[int] = None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

    example = Example(a=1, b=2, c=4, d="D", e=5)

    init_function = _IgnoreUndefinedParameters.create_init(Example)

    ####
    # Test 1: check if all required parameters are present
    ####
    init_function(example, a=1, b=2)
    assert example.a == 1
    assert example.b == 2
   

# Generated at 2022-06-13 19:24:37.162391
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    def get_params(**kwargs):
        return _UndefinedParameterAction.handle_from_dict(TestClass, kwargs)

    assert get_params(a=1, b=1) == {'a': 1, 'b': 1}
    try:
        get_params(a=1, c=1)
        assert False
    except UndefinedParameterError:
        assert True

# Generated at 2022-06-13 19:24:46.885726
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    def dummy_init(self, kw1="default", kw2="default"):
        pass

    class Dummy(object):
        __init__ = dummy_init

    with_defaults = _IgnoreUndefinedParameters.create_init(Dummy)
    with_defaults(Dummy(), "and", "some")

    def dummy_init_no_defaults(self, kw1, kw2):
        pass

    class DummyNoDefaults(object):
        __init__ = dummy_init_no_defaults

    without_defaults = _IgnoreUndefinedParameters.create_init(DummyNoDefaults)
    without_defaults(DummyNoDefaults(), "and", "some")


if __name__ == "__main__":
    test__IgnoreUndefinedParameters_create_init()

# Generated at 2022-06-13 19:24:57.042565
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    from dataclasses_json.api import Config
    from dataclasses_json.utils import LetterCase
    from dataclasses_json.utils import CatchAllVar
    from dataclasses_json.undefined import Undefined

    @dataclasses.dataclass(config=Config.with_undefined_parameter_behavior(
        behavior=Undefined.INCLUDE))
    class CatchAllTestClass:
        catch_all: Optional[CatchAllVar] = None
        a: int = 0

    c = CatchAllTestClass(a=1, b=2, c=3)
    expected_handle_to_dict_result = {"catch_all": {}, "a": 1}

# Generated at 2022-06-13 19:25:00.359086
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Test:
        x: int

        def __init__(self, x=1):
            self.x = x


    _RaiseUndefinedParameters.handle_from_dict(Test, {
        "y": 1,
        "x": 2
    })



# Generated at 2022-06-13 19:25:07.495839
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # normal behavior
    @dataclasses.dataclass
    class A:
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default=None,
            metadata={'marshmallow_field': dataclasses_json.CatchAllVar()})

    kvs = _CatchAllUndefinedParameters.handle_from_dict(
        A, {'something': 42, 'and_more': 'one'})
    assert kvs == {'catch_all': {'something': 42, 'and_more': 'one'}}

    # with catch-all input
    kvs = _CatchAllUndefinedParameters.handle_from_dict(
        A, {'something': 42, 'and_more': 'one',
            'catch_all': {'something_else': 42}})
    assert kvs

# Generated at 2022-06-13 19:26:27.370047
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class TestClass:
        def __init__(self, a: int, b: int, c: int, d: int, e: int) -> None:
            self.a: int = a
            self.b: int = b
            self.c: int = c
            self.d: int = d
            self.e: int = e

    class TestClass2:
        def __init__(self, a: int, b: int, c: int, d: int, e: int,
                     *args, **kwargs) -> None:
            self.a: int = a
            self.b: int = b
            self.c: int = c
            self.d: int = d
            self.e: int = e


# Generated at 2022-06-13 19:26:37.820662
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # this test uses an enum for the type undef to make sure that
    # the test is not dependent on one specific type of Undef
    # It creates an instance of the class defined inside the enum
    # and tests it's behavior.
    Undefined = Undefined("Undefined",
                          ("Undef", _UndefinedParameterAction))
    Undefined.__new__ = staticmethod(lambda _type, *args, **kwargs:
                                     _type.Undef(*args, **kwargs))
    undef = Undefined()

    class TestClass:
        x: int = 0
        y: str = ""

    d = {'x': 3, 'z': 4}  # z is undefined for TestClass
    result = undef.handle_from_dict(TestClass, d)
    assert result == {'x': 3}

    d

# Generated at 2022-06-13 19:26:48.022456
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class A:
        def __init__(self, a, b):
            pass

    class B:
        def __init__(self, a, b, c, **kwargs):
            pass

    orig_A = A.__init__
    orig_B = B.__init__

    A.__init__ = _UndefinedParameterAction.create_init(A)
    B.__init__ = _UndefinedParameterAction.create_init(B)

    # Test that arguments get passed through
    A("a", "b")
    B("a", "b", "c")
    A("a", "b", "c")
    A("a", "b", "c", "d")

    # Test that the catch-all keyword arguments are passed through
    A("a", "b", **{"key": "value"})
   

# Generated at 2022-06-13 19:26:54.452548
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Foo:
        pass

    parameters = _IgnoreUndefinedParameters.handle_from_dict(
        cls=Foo,
        kvs={"b": 1, "a": 2, "TEST": "TEST"}
    )

    assert parameters == {}

    class Foo:
        a: int
        b: int
        c: int

    parameters = _IgnoreUndefinedParameters.handle_from_dict(
        cls=Foo,
        kvs={"a": 1, "b": 2, "c": 3, "TEST": "TEST"}
    )

    assert parameters == {"a": 1, "b": 2, "c": 3}

    class Foo:
        a: int
        b: int
        c: int


# Generated at 2022-06-13 19:27:05.368445
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    from dataclasses import dataclass
    from typing import Optional

    from dataclasses_json import DataClassJsonMixin
    from dataclasses_json.api import Undefined


    @dataclass
    class TestClass(DataClassJsonMixin):
        value: int
        undefined: Undefined = Undefined.EXCLUDE

    test1 = TestClass.from_dict({"value": 1, "other": "test"})
    assert test1.value == 1

    try:
        TestClass.from_dict({"value": 1, "other": "test"},
                                   undefined=Undefined.RAISE)
        raise ValueError("Should not be reachable!")
    except UndefinedParameterError:
        pass


# Generated at 2022-06-13 19:27:07.208577
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # GIVEN
    # WHEN
    result = _UndefinedParameterAction.handle_dump()
    # THEN
    assert result == {}



# Generated at 2022-06-13 19:27:11.550377
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    class X:
        a: int
        b: Optional[CatchAllVar]

    x = X(a=1, b={"c": 2})
    assert _CatchAllUndefinedParameters.handle_dump(x) == {"c": 2}



# Generated at 2022-06-13 19:27:18.994302
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        foo: str
        bar: str
        baz: str

        def __init__(self, **kwargs):
            raise NotImplementedError("Class TestClass should not be "
                                      "instantiated during testing!")

    input_dict = dict(foo=42, bar=31, baz=15)

    # No undefined parameter
    expected_dict = dict(foo=42, bar=31, baz=15)
    output_dict = _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                             input_dict)
    assert output_dict == expected_dict

    # Single undefined parameter
    input_dict = dict(foo=42, bar=31, baz=15, qux=17)

# Generated at 2022-06-13 19:27:26.558039
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    from dataclasses_json.config import Config
    from dataclasses_json.undefined import Undefined
    from dataclasses_json.utils import CatchAll

    config = Config(
        unknown_parameter_policy=Undefined.INCLUDE)
    from ._undefined_tests import TestClass
    from ._undefined_tests import TestClassNoField
    from ._undefined_tests import TestClassTwoFields
    from ._undefined_tests import TestClassFieldAndFixture
    from ._undefined_tests import TestClassDefaultField
    from ._undefined_tests import TestClassDefaultFactoryField
    from ._undefined_tests import TestClassValidateField
    from ._undefined_tests import TestClassValidateFieldFail


# Generated at 2022-06-13 19:27:36.169615
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import dataclasses
    import dataclasses_json

    @dataclasses.dataclass
    class Person:
        name: str


    @dataclasses_json.dataclass_json(undefined=Undefined.RAISE)
    @dataclasses.dataclass
    class Other:
        name: str


    @dataclasses_json.dataclass_json(undefined=Undefined.EXCLUDE)
    @dataclasses.dataclass
    class Third:
        name: str


    assert _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=Third, kvs={"name": "Amber"}) == ({"name": "Amber"}, {})

# Generated at 2022-06-13 19:29:22.709041
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("Some message")
    except UndefinedParameterError as e:
        assert str(e) == "Some message"

# Generated at 2022-06-13 19:29:31.950062
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class X:
        _undefined = Undefined.INCLUDE
        arg1: str
        arg2: str
        arg3: Optional[CatchAllVar] = None

    def func(a: str, b: str) -> None:
        pass

    init_method = _CatchAllUndefinedParameters.create_init(X)
    assert inspect.signature(init_method) == inspect.signature(func)

# Generated at 2022-06-13 19:29:45.623951
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import dataclasses
    import dataclasses_json

    class C:
        y: int
        z: int

    @dataclasses.dataclass
    class A:
        x: int
        y: int = 3
        z: int = dataclasses.field(default=2)
        catch_all: Optional[dataclasses_json.CatchAllVar] = \
            dataclasses.field(default_factory=dict)
        child: C = dataclasses.field(default_factory=lambda: C(y=1, z=2))

    @dataclasses.dataclass
    class B:
        x: int
        catch_all: Optional[dataclasses_json.CatchAllVar] = \
            dataclasses.field(default=None)

# Generated at 2022-06-13 19:29:50.687592
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(x=None) == {}
    assert _UndefinedParameterAction.handle_dump(x=42) == {}
    assert _UndefinedParameterAction.handle_dump(x="something") == {}
    assert _UndefinedParameterAction.handle_dump(x=[]) == {}
    assert _UndefinedParameterAction.handle_dump(x={}) == {}



# Generated at 2022-06-13 19:29:51.866586
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert _UndefinedParameterAction.handle_to_dict(None, {}) == {}

# Generated at 2022-06-13 19:30:02.959337
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: Any
        b: int
        c: CatchAll = None

        def __init__(self, a: Any, b: int, c: CatchAll = None):
            self.a = a
            self.b = b
            self.c = c

    test_class = TestClass.__init__
    assert test_class.__name__ == "__init__"
    catch_all_init = _CatchAllUndefinedParameters.create_init(test_class)
    catch_all_init.__name__ == "__init__"
    assert test_class.__defaults__ == catch_all_init.__defaults__
    assert test_class.__code__ == catch_all_init.__code__

# Generated at 2022-06-13 19:30:10.814083
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    from unittest.mock import patch

    class SomeClass:
        def __init__(self, a: int, b: str, c: str, d: int):
            pass

    expected_known_parameters = {'a': 1, 'b': 'b', 'c': 'c'}
    expected_unknown_parameters = {'d': 4}
    kvs = {**expected_known_parameters, **expected_unknown_parameters}

    @patch.object(_UndefinedParameterAction, '_separate_defined_undefined_kvs')
    def check_default_action(
            mock_separate_defined_undefined_kvs,
            defined_parameters: Dict[str, Any],
            undefined_parameters: Dict[str, Any]):
        mock_separate_defined_undefined_

# Generated at 2022-06-13 19:30:14.152890
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test")
    except Exception as e:
        assert str(e) == "test"
        assert e.field_names == tuple()

# Generated at 2022-06-13 19:30:27.353761
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class DummyClass:
        field_1: int
        field_2: int

        @classmethod
        def from_dict(cls, kvs):
            return cls(**_RaiseUndefinedParameters.handle_from_dict(cls, kvs))

    with pytest.raises(UndefinedParameterError):
        DummyClass.from_dict(dict(field_1=1, field_2=2, field_3=3))

    assert DummyClass.from_dict(dict(field_1=1, field_2=2)) == DummyClass(
        1, 2)
