

# Generated at 2022-06-13 19:20:42.485195
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    kvs = {"a": 1, "b": 2}
    handled_kvs = _UndefinedParameterAction.handle_to_dict(
        cls="", kvs=kvs)
    assert handled_kvs is kvs

# Generated at 2022-06-13 19:20:53.156052
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass

    @dataclass
    class Test(object):
        a: Optional[CatchAllVar]

    test_dict = {
        "a": {
            1: 2,
            3: 4
        },
        4: 5
    }

    expected_result = {1: 2, 3: 4, 4: 5}
    assert expected_result == \
           _CatchAllUndefinedParameters.handle_to_dict(Test, test_dict)

    test_dict = {
        "a": 123,
        4: 5
    }

    expected_result = {4: 5}
    assert expected_result == \
           _CatchAllUndefinedParameters.handle_to_dict(Test, test_dict)



# Generated at 2022-06-13 19:20:53.970377
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    err = UndefinedParameterError()
    assert str(err) == "UndefinedParameterError"

# Generated at 2022-06-13 19:20:59.023735
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses.dataclass
    class Test:
        catch_all: Optional[CatchAllVar] = None

    t = Test()
    assert _CatchAllUndefinedParameters.handle_dump(t) == {}
    setattr(t, "catch_all", {"a": 1})
    assert _CatchAllUndefinedParameters.handle_dump(t) == {"a": 1}

# Generated at 2022-06-13 19:21:02.416835
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert _UndefinedParameterAction.handle_to_dict(None, {}) == {}
    assert _UndefinedParameterAction.handle_to_dict(None, {"a": 1}) == {"a": 1}



# Generated at 2022-06-13 19:21:11.093305
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class A:
        a: int
        b: int
        c: int = 3
        _: dict = dataclasses.field(default_factory=dict)

    input_params = {
        "a": 1,
        "b": 2,
        "_": {"foo": "bar",
              "bar": "baz"}
    }
    expected_params = {
        "a": 1,
        "b": 2,
        "c": 3,
        "_": {"foo": "bar",
              "bar": "baz"}
    }
    output_params = \
        _CatchAllUndefinedParameters.handle_from_dict(A, input_params)

    assert expected_params == output_params



# Generated at 2022-06-13 19:21:13.065176
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    err = UndefinedParameterError()
    assert err.field_names == []

# Generated at 2022-06-13 19:21:22.081849
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __eq__(self, other):
            return self.a == other.a and self.b == other.b

    catch_all_init = _CatchAllUndefinedParameters.create_init(TestClass)
    test_class1 = TestClass(a=1, b="hello")
    test_class2 = TestClass(1, "hello")
    test_class3 = TestClass(a=1, b="hello", c=3)
    test_class4 = TestClass(1, "hello", c=3)
    test_class5 = TestClass(1, "hello", d=4)
   

# Generated at 2022-06-13 19:21:35.809826
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass(undefined=Undefined.INCLUDE)
    class DataclassWithCatchAll:
        a: int = dataclasses.field(default=0)
        b: int = dataclasses.field(default=0)
        c: Optional[CatchAll] = dataclasses.field(default=None)

        def __str__(self):
            return f"DataclassWithCatchAll(a: {self.a}, b: {self.b}, " \
                   f"c: {self.c})"

    kvs = {}
    kvs["a"] = 1
    kvs["b"] = 2
    kvs["c"] = 3
    kvs["d"] = 4
    kvs["e"] = 5
    res = _CatchAllUndefinedParameters.handle

# Generated at 2022-06-13 19:21:38.700243
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    test_dict = {"a": "b"}
    assert _UndefinedParameterAction.handle_dump(obj=1) == {}, \
        type(_UndefinedParameterAction.handle_dump(obj=1))

# Generated at 2022-06-13 19:22:00.759340
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import marshmallow
    from typing import Optional

    class TestObj:
        def __init__(self, a: str, b: int, c: Optional[CatchAllVar]):
            pass

    @dataclasses.dataclass
    class TestObj2:
        a: str
        b: int

    for cls in [TestObj, TestObj2]:
        init = _IgnoreUndefinedParameters.create_init(cls)
        init(cls, "a", 1, "d")
        init(cls, "a", 1, "d", "e")



# Generated at 2022-06-13 19:22:07.902888
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class TestClass:
        def __init__(self):
            self.a = 42
        a: int
    test_obj = TestClass()
    @functools.wraps(test_obj.__init__)
    def new_init(self):
        self.a = None
    test_obj.__init__ = new_init
    _UndefinedParameterAction.create_init(test_obj)()
    assert test_obj.a == 42

# Generated at 2022-06-13 19:22:15.957029
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # type: () -> None
    def _dummy_init(self, a, b, catch_all=None):
        # type: (int, int, Dict[Any, Any]) -> None
        pass

    def _dummy_init_with_default(self, a, b, catch_all=None):
        # type: (int, int, Dict[Any, Any]) -> None
        pass

    def _dummy_init_with_default_factory(self, a, b, catch_all=None):
        # type: (int, int, Dict[Any, Any]) -> None
        pass


# Generated at 2022-06-13 19:22:21.742727
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # noinspection PyAttributeOutsideInit
    class A:
        def __init__(self, a=None, b=None):
            self.a = a
            self.b = b

        def __attrs_post_init__(self):
            pass

    with pytest.raises(UndefinedParameterError, match="udp") as e:
        _RaiseUndefinedParameters.handle_from_dict(cls=A, kvs={"foo": 42})
    assert "udp" in e.value.args[0] and "foo" in e.value.args[0]



# Generated at 2022-06-13 19:22:33.737558
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class TestClass:
        field1: str
        field2: int

        def __init__(self, field1, field2, field3):
            self.field1 = field1
            self.field2 = field2

        def returns_field1(self):
            return self.field1

    obj = TestClass("value1", 42, 23)
    assert obj.field2 == 42
    assert obj.returns_field1() == "value1"
    assert obj.__init__.__name__ == "__init__"

# Generated at 2022-06-13 19:22:36.033172
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError(
            'UndefinedParameterError raises an exception')
    except ValidationError as error:
        print(error)

# Generated at 2022-06-13 19:22:51.033839
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    """
    Tests that _IgnoreUndefinedParameters handles undefined parameters as
    expected.
    """
    from dataclasses import dataclass

    @dataclass
    class A:

        def __init__(self, a: str, b: int, c: float = None):
            pass    


# Generated at 2022-06-13 19:22:52.518643
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump("hi") == {}



# Generated at 2022-06-13 19:23:02.052527
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:

        def __init__(self, catch_all: CatchAll = None, **kwargs):
            self.catch_all = catch_all

    obj = TestClass(a=1, b=2, c=3, catch_all={"d": 4, "e": 5})
    kvs = {"a": 1, "b": 2, "c": 3, "catch_all": {"d": 4, "e": 5}}
    expected_result = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

    result = _CatchAllUndefinedParameters.handle_to_dict(obj=obj, kvs=kvs)

    assert result == expected_result

# Generated at 2022-06-13 19:23:02.653626
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError()

# Generated at 2022-06-13 19:23:25.046057
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    dummy_object = object()
    class ClassWithCatchAll:
        foo: str
        bar: str
        # noinspection PyMissingConstructor,PyTypeChecker
        def __init__(self, foo: str, bar: str, catch_all: Optional[CatchAll]):
            self.foo, self.bar, self.catch_all = foo, bar, catch_all

    class ClassWithoutCatchAll:
        foo: str
        bar: str
        # noinspection PyMissingConstructor,PyTypeChecker
        def __init__(self, foo: str, bar: str):
            self.foo, self.bar = foo, bar


# Generated at 2022-06-13 19:23:29.046588
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # noinspection PyUnresolvedReferences
    if _UndefinedParameterAction.handle_dump.__module__ != \
            _UndefinedParameterAction.__module__:
        raise AssertionError("UndefinedParameterAction._handle_dump() "
                             "needs to be defined in class scope")

# Generated at 2022-06-13 19:23:34.215816
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    class TestClass:
        def __init__(self, a, b, c: CatchAll=None, d=5) -> None:
            pass

    dump_result = _CatchAllUndefinedParameters.handle_dump(TestClass)
    assert isinstance(dump_result, dict)
    assert len(dump_result) == 0
# end of unit test for method handle_dump of class _CatchAllUndefinedParameters

# Generated at 2022-06-13 19:23:38.363450
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Unit test for method handle_dump of class _UndefinedParameterAction
    """
    for action in [Undefined.INCLUDE, Undefined.EXCLUDE, Undefined.RAISE]:
        assert _UndefinedParameterAction.handle_dump(
                action) == {}

# Generated at 2022-06-13 19:23:45.283085
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from .utils import CatchAllVar
    from dataclasses import dataclass


    @dataclass
    class _MyClass:
        a: int
        b: int
        _catchall: Optional[CatchAllVar]
    obj = _MyClass(1, 2, {"c": 3, "d": 4})
    kvs = {"a": 1, "b": 2, "c": 3, "d": 4}
    new_kvs = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert new_kvs == {"a": 1, "b": 2}

# Generated at 2022-06-13 19:23:51.885752
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, foo: str, bar: int):
            self.foo = foo
            self.bar = bar

    assert _RaiseUndefinedParameters.handle_from_dict(Foo, {"foo": "foo"}) == \
           {"foo": "foo"}
    assert _RaiseUndefinedParameters.handle_from_dict(Foo, {"foo": "foo", "baz": "baz"}) == \
           {"foo": "foo", "bar": "baz"}

# Generated at 2022-06-13 19:23:54.855962
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("error message")
    except UndefinedParameterError as e:
        assert e.msg == "error message"

# Generated at 2022-06-13 19:23:58.789789
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test")
    except UndefinedParameterError as e:
        assert e.args[0] == "test"



# Generated at 2022-06-13 19:24:00.300519
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError()



# Generated at 2022-06-13 19:24:15.506651
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class C(metaclass=abc.ABCMeta):
        def __init__(self, *, foo: str, bar: int,
                     catch_all: Optional[CatchAllVar] = None):
            self.foo = foo
            self.bar = bar
            self.catch_all = catch_all

    catch_all_parameters = {
        "bar": "5",
        "foo": "3",
        "baz": "bat"
    }
    only_undefined_parameters = {
        'baz': 'bat'
    }


# Generated at 2022-06-13 19:24:51.808680
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    assert _CatchAllUndefinedParameters.handle_to_dict(None,
    {"foo": "bar", "catch_all": {"a": "b", "c": "d"}}) == {"foo": "bar", "a": "b", "c": "d"}
    assert _CatchAllUndefinedParameters.handle_to_dict(None, {"foo": "bar"}) == {"foo": "bar"}

# Generated at 2022-06-13 19:24:53.252389
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert len(_UndefinedParameterAction.handle_dump(obj=None)), 0

# Generated at 2022-06-13 19:25:02.093632
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Test:
        def __init__(self, a, catch_all=None):
            self.a = a
            self.catch_all = catch_all

    new_init = _CatchAllUndefinedParameters.create_init(Test)
    obj = Test(a=1, b=5)
    assert obj.a == 1
    assert obj.catch_all == {'b': 5}

    new_init(obj, a=2, c=6)
    assert obj.a == 2
    assert obj.catch_all == {'c': 6}

    obj = Test(a=None)
    assert obj.a is None
    assert obj.catch_all == {}
    new_init(obj, a=2, b=3, c=4)
    assert obj.a == 2
    assert obj.catch_all

# Generated at 2022-06-13 19:25:09.615022
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class Example:
        pass


# Generated at 2022-06-13 19:25:17.802106
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: str
        b: int
        c: float = dataclasses.field(repr=True)

        def __init__(self, a: str, b: int, c: float = -1.0, **kwargs):
            self.a = a
            self.b = b
            self.c = c
            self.kwargs = kwargs

    init = _IgnoreUndefinedParameters.create_init(TestClass)

    init_signature = inspect.signature(init)
    print(init_signature)

    # noinspection PyArgumentList
    test_object = TestClass(a="a", b=1, c=2.0, d=3)
    assert test_object.a == "a"
    assert test_object

# Generated at 2022-06-13 19:25:24.582196
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field

    @dataclass
    class Foo:
        a: int
        b: int = field(default=10)
        c: Optional[CatchAllVar] = field(default_factory=dict)

    init = _CatchAllUndefinedParameters.create_init(Foo)

    try:
        Foo(a=9, c=10)
        assert False, "Should have raised an error."
    except TypeError:
        pass

    f = Foo(a=1, d=12, e=13)
    assert f.a == 1
    assert f.b == 10
    assert f.c == {"d": 12, "e": 13}

    f = Foo(a=1, d=12, b=20)
    assert f.a == 1
    assert f.b

# Generated at 2022-06-13 19:25:31.958960
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Test1:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class Test2(Test1):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    test_cases = [
        (Test1, {}),
        (Test1, {"a": 0}),
        (Test1, {"b": 0}),
        (Test1, {"a": 0, "b": 0}),
        (Test2, {"a": 0, "b": 0, "c": 0}),
    ]
    for cls, kvs in test_cases:
        init_args = _RaiseUndefinedParameters.handle_from_dict(cls, kvs)
        cl

# Generated at 2022-06-13 19:25:33.837061
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    data = {1: 'one', 'one': 1, 'two': 2, 'three': 3}
    assert data == _CatchAllUndefinedParameters.handle_to_dict(None, data)

# Generated at 2022-06-13 19:25:39.718510
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass

    @dataclass
    class Foo:
        foo: str
        bar: str = "bar"
        baz: Optional[CatchAllVar] = None

    obj = Foo(foo="foo", bar="test", c=3)
    assert obj.baz == {"c":3}
    assert _CatchAllUndefinedParameters.handle_to_dict(obj, {"foo":"foo","bar":"test","c":"3"}) == {"foo":"foo", "bar":"test", "c":"3"}


    @dataclass
    class Foo:
        foo: str
        bar: str = "bar"
        baz: Optional[CatchAllVar] = None

    obj = Foo(foo="foo", bar="test", c=3)
    assert obj.baz == {"c":3}

# Generated at 2022-06-13 19:25:49.611848
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.config import config

    class TestClass:
        a: int
        kwargs: Optional[CatchAllVar] = None

    @config(undefined=Undefined.INCLUDE)
    @dataclasses.dataclass()
    class TestIncludeClass:
        a: int
        kwargs: Optional[CatchAllVar] = None

    @config(undefined=Undefined.EXCLUDE)
    @dataclasses.dataclass()
    class TestExcludeClass:
        a: int
        kwargs: Optional[CatchAllVar] = None

    test_instance = TestClass(a=123, kwargs={"b": 456, "c": 789})

# Generated at 2022-06-13 19:26:58.241082
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    error = UndefinedParameterError("foobar")
    assert error.__dict__["message"] == "foobar"

# Generated at 2022-06-13 19:27:07.235878
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():

    def _separate_defined_undefined_kvs(cls, kvs: Dict) -> \
            Tuple[KnownParameters, UnknownParameters]:
        """
        Returns a 2 dictionaries: defined and undefined parameters
        """
        class_fields = fields(cls)
        field_names = [field.name for field in class_fields]
        unknown_given_parameters = {k: v for k, v in kvs.items() if
                                    k not in field_names}
        known_given_parameters = {k: v for k, v in kvs.items() if
                                  k in field_names}
        return known_given_parameters, unknown_given_parameters

    @dataclasses.dataclass
    class tester:
        catchall: Optional[CatchAllVar] = dataclasses.field

# Generated at 2022-06-13 19:27:15.817696
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass
    class _Example:
        a: int
        b: str
        _undefined_parameters: CatchAll = None
        c: int = 1
        d: str = "d"

        def __init__(self, a: int, b: str, c: int):
            pass

    class_to_initialize = _Example
    new_init = _CatchAllUndefinedParameters.create_init(
        class_to_initialize)
    assert inspect.signature(new_init) == inspect.signature(_Example.__init__)
    assert new_init.__name__ == "_catch_all_init"

# Generated at 2022-06-13 19:27:21.664062
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import dataclasses
    from typing import Optional

    @dataclasses.dataclass(undefined=Undefined.INCLUDE)
    class BaseClass:
        _unwritten: Optional[bool]
        catch_all: Optional[CatchAllVar] = None

    assert "_unwritten" not in BaseClass(catch_all={"_unwritten": True}).dict()



# Generated at 2022-06-13 19:27:24.780732
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Example:
        def __init__(self, a, b, c):
            pass

    kvs = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert _UndefinedParameterAction.handle_from_dict(Example, kvs) == kvs



# Generated at 2022-06-13 19:27:34.818187
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class InnerClass:
        catch_all: Optional[CatchAllVar]

    @dataclasses.dataclass
    class TestClass:
        test_field: str = "test_field"
        inner_test_field: InnerClass = dataclasses.field(
            default_factory=lambda: InnerClass(catch_all={}))

    expected = {
        "test_field": "test_field",
        "inner_test_field": {
            "catch_all": {
                "already_included": "already_included",
                "new_value": "new_value"
            }
        },
    }


# Generated at 2022-06-13 19:27:36.392684
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    msg = "error message"
    UndefinedParameterError(msg)

# Generated at 2022-06-13 19:27:46.002130
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from abc import ABC, ABCMeta
    from dataclasses import dataclass
    from typing import Optional

    @dataclass(undefined=Undefined.INCLUDE)
    class A(ABC):
        name: str
        catch_all: CatchAll

    @dataclass(undefined=Undefined.RAISE)
    class B(ABC):
        name: str
        catch_all: CatchAll

    @dataclass(undefined=Undefined.EXCLUDE)
    class C(ABC):
        name: str
        catch_all: CatchAll

    def test_case(abc: ABC, handle_to_dict_func, expected: Optional[int]):
        t = type(abc)
        t.__name__ = "T%s" % str(expected)[0]
        handle_to_dict_

# Generated at 2022-06-13 19:27:54.639082
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:

        def __init__(self, a=0, b=0):
            self.a = a
            self.b = b

    assert _RaiseUndefinedParameters.handle_from_dict(
        cls=TestClass,
        kvs={"a": 1, "b": 2, "c": 3}) == {"a": 1, "b": 2}



# Generated at 2022-06-13 19:27:56.206484
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("Test")