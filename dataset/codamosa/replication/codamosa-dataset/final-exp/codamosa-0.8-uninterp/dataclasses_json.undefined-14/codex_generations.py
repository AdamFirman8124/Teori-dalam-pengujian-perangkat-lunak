

# Generated at 2022-06-13 19:20:44.723911
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Cls:
        a: str
        b: str
        c: str
        d: str
        e: str

        def __init__(self, a: str, b: str, c: str, d: str, e: str):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

    custom_obj_init = _IgnoreUndefinedParameters.create_init(Cls)

    @dataclasses.dataclass
    class Cls2:
        a: str
        b: str
        c: str
        d: str
        e: str


# Generated at 2022-06-13 19:20:53.119549
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class TestClass:
        catchall: CatchAll = dataclasses.field(default=CatchAllVar())

    object_ = TestClass(catchall={"a": 1, "b": 2})
    dump = _CatchAllUndefinedParameters.handle_dump(object_)

    print(dump)
    assert dump == {"a": 1, "b": 2}


if __name__ == "__main__":
    # Unit test for method _handle_dump of class _CatchAllUndefinedParameters
    test__CatchAllUndefinedParameters_handle_dump()

# Generated at 2022-06-13 19:21:02.536601
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import dataclasses
    import dataclasses_json
    import inspect

    @dataclasses.dataclass
    class ExampleKWOnly:
        name: str
        age: int

        def __init__(self, name, age):
            self.name = name
            self.age = age

    @dataclasses.dataclass
    class ExampleWithCatchAll:
        name: str
        age: int
        undefined_parameters: dataclasses_json.CatchAll

        def __init__(self, name, age, undefined_parameters):
            self.name = name
            self.age = age
            self.undefined_parameters = undefined_parameters

    # assert that the signature of the new init is the same as before
    original = ExampleKWOnly.__init__
    modified = _CatchAll

# Generated at 2022-06-13 19:21:08.184336
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from typing import Literal

    class A:
        def __init__(self, foo: Literal[1], bar: str = "test"):
            pass

    # A(1, "test") should work
    _IgnoreUndefinedParameters.create_init(A)()
    # A(1, "test", undefined_parameter=3) should raise error
    with pytest.raises(TypeError):
        _IgnoreUndefinedParameters.create_init(A)()

# Generated at 2022-06-13 19:21:14.169191
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Foo:
        def __init__(self, a: int = 0, b: int = 1):
            pass

    # noinspection PyTypeChecker
    modified_init = _IgnoreUndefinedParameters.create_init(Foo)
    assert modified_init(None, 1, b=2, _active_code=3) is None
    assert modified_init(None, 1, b=2, _active_code=3, _undefined_parameter=4) \
           is None

# Generated at 2022-06-13 19:21:23.095390
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass(init=False)
    class Dummy:
        def __init__(self, a: str = "default_a", b: str = "default_b",
                     *, _UNKNOWN=dataclasses_json.CatchAllVar()):
            self.a = a
            self.b = b
            self._UNKNOWN = _UNKNOWN

    @dataclasses.dataclass(init=False)
    class Dummy2:
        def __init__(self, a: str = "default_a", b: str = "default_b",
                     _UNKNOWN=dataclasses_json.CatchAllVar()):
            self.a = a
            self.b = b
            self._UNKNOWN = _UNKNOWN


# Generated at 2022-06-13 19:21:32.799444
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    from dataclasses_json.schema import Schema
    from typing import Optional


    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str
        catch_all: Optional[CatchAll] = None


    schema = Schema(unknown=Undefined.EXCLUDE)
    instance = TestClass(a=0, b="b")
    dump = schema.dump(instance)
    assert dump == {"a": 0, "b": "b"}



# Generated at 2022-06-13 19:21:39.046012
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class MyClass():

        def __init__(self, foo, bar, baz):
            self.foo = foo
            self.bar = bar
            self.baz = baz

    expected = MyClass(foo=1, bar=2, baz=3)
    class_init = _IgnoreUndefinedParameters.create_init(MyClass)
    result = class_init(self=None, foo=1, bar=2, baz=3)
    assert result == expected

# Generated at 2022-06-13 19:21:40.610221
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    _CatchAllUndefinedParameters.handle_to_dict(None, {"a": 1, "b": 2}) == {"a": 1, "b": 2}

# Generated at 2022-06-13 19:21:53.708179
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from datetime import date
    from dataclasses import dataclass, field

    @dataclass
    class A:
        a: int = 5
        b: str = "a"
        unknown = CatchAll

    a = A.from_dict({"a": 1, "unknown": 3})
    assert a.a == 1
    assert a.b == "a"
    assert a.unknown == 3

    a = A.from_dict({"b": "aa", "unknown": 3})
    assert a.a == 5
    assert a.b == "aa"
    assert a.unknown == 3

    a = A.from_dict({"a": 1, "b": "aa", "unknown": 3})
    assert a.a == 1
    assert a.b == "aa"
    assert a.unknown == 3

    a

# Generated at 2022-06-13 19:22:17.173531
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class Dc:
        a: int
        b: str
        ignore: _UndefinedParameterAction = _IgnoreUndefinedParameters
        catch_all: CatchAll = dataclasses.field(
            default_factory=dict,
            metadata={"marshmallow_field": {"load_from": "*"}}
        )

    assert len(fields(Dc)) == 4

    dc = Dc(a=1, b="b", c='c')
    assert dc.a == 1
    assert dc.b == "b"
    assert dc.catch_all == {"c": 'c'}
    assert dc.c is not None
    assert Dc.catch_all.type == Optional[CatchAll]


# Generated at 2022-06-13 19:22:24.666729
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # Given
    class Eut:
        def __init__(self, a, b=None):
            self.a = a
            self.b = b

        @classmethod
        def handle_from_dict(cls, kvs: Dict[str, Any]) -> Dict[str, Any]:
            return _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)

    expected_a = "param_a"
    expected_b = "param_b"
    expected_c = "param_c"
    expected_s = "param_s"
    expected_v = "param_v"

    kvs_a: Dict = {"a": expected_a}
    kvs_ab: Dict = {"a": expected_a, "b": expected_b}

# Generated at 2022-06-13 19:22:31.825843
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Foo:
        a: int
        b: str
        c: Optional[CatchAllVar]

    f = Foo(1, "a", {"extra1": 1, "extra2": 2})
    assert f.a == 1
    assert f.b == "a"
    assert f.c == {"extra1": 1, "extra2": 2}

# Generated at 2022-06-13 19:22:32.603284
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    pass

# Generated at 2022-06-13 19:22:44.203281
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from enum import Enum

    import dataclasses
    import pytest
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int

    @dataclass
    class B:
        b: int
        c: float

    @dataclass
    class C:
        d: float
        e: int

    @dataclass
    class D:
        f: float

        class Undefined(Enum):
            RAISE = 1


# Generated at 2022-06-13 19:22:44.804911
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    pass

# Generated at 2022-06-13 19:22:46.406461
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    assert _RaiseUndefinedParameters.handle_from_dict(
        cls=None,
        kvs={'x': 23, 'y': 42}) == {'x': 23, 'y': 42}



# Generated at 2022-06-13 19:22:54.112934
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Foo:
        def __init__(self, a: int, b: str):
            pass

    class Bar:
        def __init__(self, a: int, b: str, *, c: int = 10):
            pass

    # Only known parameters given
    kvs = {
        "a": 5,
        "b": "foo"
    }
    assert _UndefinedParameterAction.handle_from_dict(Foo, kvs) == kvs
    assert _UndefinedParameterAction.handle_from_dict(Bar, kvs) == kvs

    # Known parameters and one unknown
    kvs = {
        "a": 5,
        "b": "foo",
        "c": 20,
        "d": "foo",
        "e": "bar"
    }

# Generated at 2022-06-13 19:23:02.131804
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Foo:
        required_arg: int

        def __init__(self, required_arg: int,
                     # CatchAll:
                     optional_dict: Optional[Dict[str, Any]] = None):
            self.required_arg = required_arg
            self.optional_dict = optional_dict

    obj = Foo(1)
    init = _CatchAllUndefinedParameters.create_init(obj)
    init(obj, optional_dict={"x": [1, 2, 3]})
    assert obj.optional_dict == {"x": [1, 2, 3]}



# Generated at 2022-06-13 19:23:14.043253
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    """
    Test method _CatchAllUndefinedParameter.handle_from_dict.
    """
    # Test different types of field defaults:
    # (1) no default
    # (2) value default
    # (3) callable default

    class Defaulted:
        def __init__(self, catch_all: Optional[CatchAllVar] = {}):
            self.catch_all = catch_all

    defaulted = Defaulted()
    params = _CatchAllUndefinedParameters.handle_from_dict(Defaulted, {"p": 1})
    assert params == {"catch_all": {"p": 1}}
    defaulted = Defaulted(catch_all=defaulted.catch_all)


# Generated at 2022-06-13 19:23:45.099433
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    class TestClass:
        pass

    test_object = TestClass()
    result = _CatchAllUndefinedParameters.handle_dump(test_object)
    assert result == {}

# Generated at 2022-06-13 19:23:47.197182
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    e = UndefinedParameterError("Error!")
    assert e


# Generated at 2022-06-13 19:23:55.005356
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        _catch_all: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict
        )

        def __init__(self, a: int, **kwargs: int):
            self.a = a

    defined_input = dict(a=1)
    expected = dict(a=1, _catch_all={})
    _CatchAllUndefinedParameters.handle_from_dict(cls=TestClass,
                                                  kvs=defined_input)
    assert expected == defined_input

    undefined_input = dict(a=1, b=2)
    expected = dict(a=1, _catch_all=dict(b=2))

# Generated at 2022-06-13 19:24:10.428726
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import dataclasses
    import dataclasses_json

    @dataclasses.dataclass
    class _Test:
        a: str
        b: int

        @dataclasses_json.dataclass_json(undefined=Undefined.EXCLUDE)
        class _Test2:
            a: str
            b: int

    _, kwargs = _UndefinedParameterAction.create_init(_Test)(
        _Test("a", 1), "b", 2, c=3)
    assert kwargs == {"a": "a", "b": 1}

    _, kwargs = _UndefinedParameterAction.create_init(_Test)(
        _Test("a", 1), "b")
    assert kwargs == {"a": "a"}



# Generated at 2022-06-13 19:24:16.348153
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            assert False

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(
            TestClass, kvs={"a": "value a", "b": "value b", "c": "value c"})



# Generated at 2022-06-13 19:24:26.523348
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, a: int, b: int, c: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            if c is not None:
                if isinstance(c, dict):
                    self.c = c.copy()
                else:
                    raise UndefinedParameterError(
                        f"Catch all parameter must be a dictionary. "
                        f"Received {c}")
            else:
                self.c = c
    a = A(3,4)
    d = _CatchAllUndefinedParameters.handle_to_dict(a, {"a": 3, "b": 4})
    assert d == {}
    a = A(3, 4, {"x": 7})
    d = _CatchAllUndefinedParameters.handle_to_

# Generated at 2022-06-13 19:24:36.358430
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class Bla:
        def __init__(self, a: int, b: int):
            pass

    assert Bla.__init__ == Bla(1, 2).__init__
    assert Bla.__init__ != _UndefinedParameterAction.create_init(Bla)(1, 2)

    class Bla:
        def __init__(self, a: int, b: int, c: int = 2):
            pass

    assert Bla.__init__ == Bla(1, 2).__init__
    assert Bla.__init__ != _UndefinedParameterAction.create_init(Bla)(1)

    class Bla:
        def __init__(self, a: int, b: int, c: int = None):
            pass

    assert Bla.__init__ == _UndefinedParameterAction.create_

# Generated at 2022-06-13 19:24:46.378560
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    """
    Verify that create_init returns an __init__ function that discards
    accordingly
    :return:
    """
    import sys

    # If a lambda is assigned to a variable, then it can be imported

    # noinspection PyUnusedLocal
    def f(self, a: int, b: int, c: int) -> None:
        pass

    def g(self, a: int, b: int, c: int) -> None:
        pass

    def h(self, a: int = 1, b: int = 2, c: int = 3) -> None:
        pass

    def i(self, a: int, b: int = 2, c: int = 3) -> None:
        pass


# Generated at 2022-06-13 19:24:51.588121
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class A:
        def __init__(self, a: int, b: int, c: int):
            pass

    cls = A
    init_callable = _UndefinedParameterAction.create_init(cls)
    assert init_callable(None, 1, 2, 3) == None



# Generated at 2022-06-13 19:25:00.948725
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        f1: str
        f2: str
        def __init__(self, f1, f2):
            self.f1 = f1
            self.f2 = f2

    init_method = _CatchAllUndefinedParameters.create_init(TestClass)

    # Test how the function deals with undefined parameters
    instance = init_method(TestClass, "a", "b", f1="c", f2="d",
                           e="e")
    assert instance.f1 == "a"
    assert instance.f2 == "b"

    # Test how the function deals with too many defined parameters
    instance = init_method(TestClass, "a", "b", "c", "d", "e")
    assert instance.f1 == "a"


# Generated at 2022-06-13 19:26:02.131690
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass(frozen=True)
    class TestClass:
        a: int
        b: str

    assert _UndefinedParameterAction.handle_from_dict(TestClass,
                                                      dict(a=1, b="v")) == dict(
        a=1, b="v")
    undefined_parameter_actions = [
        Undefined.INCLUDE, Undefined.EXCLUDE, Undefined.RAISE]
    undefined_parameter_actions = [action.value for action in
                                   undefined_parameter_actions]

    for undefined_parameter_action in undefined_parameter_actions:
        for unknown_parameter_count in range(0, 3):
            for known_parameter_count in range(0, 3):
                kvs = dict(a=1)  # The

# Generated at 2022-06-13 19:26:03.993968
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    _UndefinedParameterAction.handle_to_dict(None, {})

# Generated at 2022-06-13 19:26:09.045186
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    import dataclasses

    @dataclasses.dataclass
    class TestClass:
        field: str

    test_instance = TestClass("hello")

    assert _RaiseUndefinedParameters.handle_from_dict(
        TestClass, {"field": "hello"}) == {"field": "hello"}

    kvs = {"field": "hello", "not_a_field": "world"}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
        assert False
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:26:17.245240
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class DataClass(object):
        a: int
        b: int
        c: int

    def assert_dict_equal(d1, d2):
        assert {k: v for k, v in d1.items()} == {k: v for k, v in d2.items()}

    obj = DataClass(a=1, b=2, c=3)

    assert_dict_equal(
        _UndefinedParameterAction.handle_to_dict(obj, {"a": 1, "b": 2, "c": 3}),
        {"a": 1, "b": 2, "c": 3}
    )

# Generated at 2022-06-13 19:26:26.897740
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass
    from dataclasses_json.utils import CatchAllVar

    data = {"foo": "bar", "name": "Baz", "_UNKNOWN0": "banana"}

    @dataclass
    class TestClass:
        name: str
        catch_all: Optional[CatchAllVar] = None

        def __init__(self, name: str, catch_all: Optional[CatchAllVar] = None):
            self.name = name
            self.catch_all = catch_all

    result = TestClass(**data)
    expected = TestClass("Baz", catch_all={"_UNKNOWN0": "banana"})

    assert result == expected

# Generated at 2022-06-13 19:26:36.380878
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class C:
        def __init__(self, a: int, b: int):
            pass


    assert _UndefinedParameterAction.handle_from_dict(C, {"a": 1}) == {"a": 1}
    assert _UndefinedParameterAction.handle_from_dict(C, {"a": 1, "b": 1}) == {
        "a": 1,
        "b": 1}
    assert _UndefinedParameterAction.handle_from_dict(C, {"a": 1, "c": 1}) == {
        "a": 1}
    assert _UndefinedParameterAction.handle_from_dict(C, {"c": 1}) == {}



# Generated at 2022-06-13 19:26:46.173592
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a: int, b: str):
            pass

    kvs = {"a": 1, "b": "str", "c": True}
    known_given_parameters, unknown_given_parameters = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=TestClass, kvs=kvs)
    assert {"a": 1, "b": "str"} == known_given_parameters
    assert {"c": True} == unknown_given_parameters
    assert _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs) == {
        "a": 1, "b": "str"}



# Generated at 2022-06-13 19:26:55.420402
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():

    class MyType:
        def __init__(self, first: str = "",
                     second: int = 0,
                     catch_all: Optional[CatchAllVar] = None):
            self.first = first
            self.second = second
            self.catch_all = catch_all

        def __eq__(self, o: object) -> bool:
            return isinstance(o, MyType) and \
                   o.first == self.first and \
                   o.second == self.second and \
                   o.catch_all == self.catch_all

    # Test _RaiseUndefinedParameters
    init_nonexisting_params = _RaiseUndefinedParameters.create_init(MyType)
    # Raises UndefinedParameterError
    # noinspection PyTypeChecker

# Generated at 2022-06-13 19:27:04.298702
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass(undecorated=True)
    class A:
        a: int
        b: int

    kvs = {"a": 1, "b": 2, "c": 3, "d": 4}
    known_given_parameters, unknown_given_parameters = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(A, kvs)
    assert known_given_parameters == {"a": 1, "b": 2}
    assert unknown_given_parameters == {"c": 3, "d": 4}

test__UndefinedParameterAction_handle_from_dict.__test__ = False

# Generated at 2022-06-13 19:27:08.261814
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    @dataclasses.dataclass
    class TestClass:
        catch_all: CatchAll

    kvs = {"a" : 1, "b" : 2}
    assert \
        _CatchAllUndefinedParameters.handle_to_dict(
            obj=TestClass, kvs=kvs) == kvs

# Generated at 2022-06-13 19:29:42.059798
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass(init=_IgnoreUndefinedParameters.create_init(
        TestClass))
    class TestClass:
        a: int
        b: int = 1


# Generated at 2022-06-13 19:29:46.471123
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    def func():
        return "func_called"
    class Test:
        def __init__(self, test: str, test2: str = "default",
                     test3: CatchAll = None):
            self.test = test
            self.test2 = test2
            self.test3 = test3
    assert hasattr(Test, "__init__")
    obj = Test("test_val", "test_val2", {"test3_key": "test3_val"})
    _dict = _CatchAllUndefinedParameters.handle_dump(obj)
    assert isinstance(_dict, dict)
    assert len(_dict) == 1
    assert "test3" in _dict
    assert _dict["test3"] == {"test3_key": "test3_val"}

    # Test with default factory

# Generated at 2022-06-13 19:29:47.903473
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    """
    Test the constructor of UndefinedParameterError.
    """
    UndefinedParameterError("Test message")

# Generated at 2022-06-13 19:29:58.910562
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from hypothesis import given
    from hypothesis.strategies import lists, dictionaries, integers, sampled_from

    @dataclass_json(undefined=Undefined.EXCLUDE)
    @dataclass
    class Foo:
        x: int
        y: int
        z: int

    @dataclass_json(undefined=Undefined.EXCLUDE)
    @dataclass
    class Bar:
        x: int
        y: int
        z: int
        t: int


# Generated at 2022-06-13 19:30:08.392462
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Test:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

    test_instance = Test(1, "2")
    assert _RaiseUndefinedParameters.handle_from_dict(Test, test_instance.__dict__) == \
           {"a": 1, "b": "2"}

    test_instance = Test(1, "2")
    assert _RaiseUndefinedParameters.handle_from_dict(Test, test_instance.__dict__) == \
           {"a": 1, "b": "2"}

    test_instance = Test(1, "2")
    assert _RaiseUndefinedParameters.handle_from_dict(Test, test_instance.__dict__) == \
           {"a": 1, "b": "2"}

   

# Generated at 2022-06-13 19:30:18.586326
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    def check(kvs_dict: Dict[Any, Any],
              catch_all_name: str) -> Tuple[Dict[Any, Any], Dict[Any, Any]]:
        return _CatchAllUndefinedParameters.handle_to_dict(None, kvs_dict), \
               {catch_all_name: kvs_dict}

    assert check({'f': 5, 'catch_all_field': {'a': 2}},
                 'catch_all_field') == ({'f': 5}, {'catch_all_field': {'a': 2}})
    assert check({'f': 5, 'catch_all_field': {'a': 2}},
                 'other_field_name') == \
           ({'f': 5, 'other_field_name': {'a': 2}}, {})