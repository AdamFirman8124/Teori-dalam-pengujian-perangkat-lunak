

# Generated at 2022-06-13 19:20:43.325037
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:20:53.044540
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class MyClass:
        def __init__(self, a, b=2, **undefined_parameters):
            self.a = a
            self.b = b
            self.undefined_parameters = undefined_parameters

    kvs = {"a": 1, "b": 3}
    args = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert args == {"a": 1, "b": 3}

    kvs["unknown"] = 42
    try:
        args = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
    except UndefinedParameterError:
        pass
    else:
        raise AssertionError



# Generated at 2022-06-13 19:21:02.505199
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass
    class Test:
        a: Any = dataclasses.field(default=1)
        b: Any = dataclasses.field(default=2)
        c: Any = dataclasses.field(default=3)

        def __post_init__(self):
            self.asdf = 5

    # Test that the new __init__ does not break the __post_init__
    test = Test(4, 5)
    assert test.a == 4
    assert test.b == 5
    assert test.c == 3
    assert test.asdf == 5

    bound_parameters_new_init = inspect.signature(test.__init__).bind(
        test, a=1, b=2, c=3, d=4)
    bound_parameters_new

# Generated at 2022-06-13 19:21:12.247803
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # Arrange
    kvs = {"first_name": "John", "last_name": "Doe", "place_of_birth": "Dresden"}
    _RaiseUndefinedParameters = _RaiseUndefinedParameters()

    class Person:
        def __init__(self, first_name: str, last_name: str):
            pass

    # Act
    try:
        wrong_parameters1 = _RaiseUndefinedParameters.handle_from_dict(cls=Person, kvs=kvs)
    except UndefinedParameterError:
        pass
    else:
        raise AssertionError("Expected UndefinedParameterError")

# Generated at 2022-06-13 19:21:20.669547
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class SomeClass:
        def __init__(self, foo=3, bar=2, **kwargs):
            pass
    known_given_parameters, unknown_given_parameters = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=SomeClass, kvs={"foo": 3,
                                "bar": 2,
                                "baz": 1,
                                "other": "text",
                                "_UNKNOWN1": "text"})
    assert known_given_parameters == {"foo": 3, "bar": 2}
    assert unknown_given_parameters == {"baz": 1, "other": "text",
                                        "_UNKNOWN1": "text"}



# Generated at 2022-06-13 19:21:25.623336
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a: int, b: str):
            pass

    defined_params = {"a": 1, "b": "b"}
    undefined_params = {"c": 2, "d": "d"}

    kvs_with_undef_params = {**defined_params, **undefined_params}

    try:
        _RaiseUndefinedParameters.handle_from_dict(
            cls=TestClass, kvs=kvs_with_undef_params)
    except UndefinedParameterError as e:
        e_message = str(e)
        for k, v in undefined_params.items():
            assert k in e_message
            assert str(v) in e_message
    else:
        raise AssertionError("Got no exception")

    known_params = _Ra

# Generated at 2022-06-13 19:21:30.162935
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    @dataclasses.dataclass
    class TestClass:
        one: str = "one"

    assert {} == _UndefinedParameterAction.handle_dump(TestClass())



# Generated at 2022-06-13 19:21:40.763618
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # noinspection PyProtectedMember,PyUnresolvedReferences
    class _TestCls:
        def __init__(self, a, b="b", *, c="c", d: Optional[CatchAllVar] = None,
                     e=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

        def __eq__(self, other):
            return (self.a == other.a and
                    self.b == other.b and
                    self.c == other.c and
                    self.e == other.e and
                    self.d == other.d)

    # noinspection PyProtectedMember,PyUnresolvedReferences

# Generated at 2022-06-13 19:21:53.705441
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # In the first two tests we test that parameters not in the dataclass are
    # filtered out.
    # The first test is when the unexpected parameters
    # are given as keyword arguments.
    @dataclasses.dataclass(frozen=True)
    class Klazz:
        foo: int
    params = {'foo': 1, 'bar': 2}
    result = _UndefinedParameterAction.handle_from_dict(Klazz, params)
    assert result == {'foo': 1}
    # The second test is when the unexpected parameters
    # are given as positional arguments.
    @dataclasses.dataclass(frozen=True)
    class Klazz:
        foo: int
    params = {'foo': 1, 'bar': 2}

# Generated at 2022-06-13 19:21:59.412618
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        pass

    arguments_that_should_not_change = dict(a=1, b=2, c=3)
    result = _UndefinedParameterAction.handle_from_dict(TestClass,
                                                        arguments_that_should_not_change)
    assert arguments_that_should_not_change is result, \
        "Should return the dict that was given as argument"



# Generated at 2022-06-13 19:22:28.702767
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from .utils import class_schema
    from .utils import json
    import pytest

    @class_schema(undefined=Undefined.EXCLUDE)
    class MyClass:
        a: int
        b: int
        c: Optional[int]

    o1 = MyClass(a=1, b=2, c=3)
    o2 = MyClass(a=4, b=5)

    class Outer:
        myclass: MyClass = MyClass(a=1, b=2, c=3)

    outer = Outer()
    outer_json = json.dumps(outer)
    outer2 = json.loads(outer_json, Outer)

    assert o1.a == 1
    assert o1.b == 2
    assert o1.c == 3
    assert o2.a == 4


# Generated at 2022-06-13 19:22:29.331790
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    pass

# Generated at 2022-06-13 19:22:36.189256
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    class T:
        a: int
        b: str
        undefined_parameters: Optional[CatchAllVar] = \
            dataclasses.field(default=None)

    t1 = T(a=3, b="string")
    assert _CatchAllUndefinedParameters.handle_dump(t1) == {}
    t2 = T(a=3, b="string", undefined_parameters={
        "key": 3
    })
    assert _CatchAllUndefinedParameters.handle_dump(t2) == {
        "key": 3
    }



# Generated at 2022-06-13 19:22:47.018281
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class B:
        def __init__(self, b: str, c: Optional[CatchAllVar] = None) -> None:
            self.b = b
            self.c = c

    class A:
        def __init__(self, a: str, b: B, c: int = 0) -> None:
            self.a: str
            self.b: B
            self.c: int
            self.a = a
            self.b = b
            self.c = c

    data = {
        "a": "A",
        "b": {"b": "b", "c": {'d': 'd'}},
        "c": 1,
        "d": 2,
    }
    a = A("A", B("b", {'d': 'd'}), 1)

# Generated at 2022-06-13 19:22:52.771931
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass

    @dataclass(undefined=Undefined.INCLUDE)
    class TestClass:
        name: str
        catch_all: Optional[CatchAllVar]

    from dataclasses_json.config import letter_case
    obj = TestClass(name="asdf", throw_away="foo")
    # check that the default behavior of letter_case is not affected
    assert {letter_case.LOWER.value(obj.name): letter_case.LOWER.value(
        obj.name)} == {
                   obj.name: obj.name}
    # check that the field is still there
    assert obj.catch_all == {"throw_away": "foo"}

# Generated at 2022-06-13 19:22:56.051687
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test message")
    except UndefinedParameterError as err:
        assert err.message == "Unable to serialize data. Errors: test message"

# Generated at 2022-06-13 19:23:03.558554
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class DummyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    dummy_obj = DummyClass(3, 4)

    created_init = _CatchAllUndefinedParameters.create_init(dummy_obj)
    dummy_obj2 = created_init(None, 5, 6, 7)
    assert dummy_obj2.a == 5
    assert dummy_obj2.b == 6
    assert created_init.__name__ == dummy_obj.__init__.__name__


if __name__ == "__main__":
    test__CatchAllUndefinedParameters_create_init()

# Generated at 2022-06-13 19:23:15.214077
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import marshmallow
    import marshmallow_enum
    import enum

    class Foo:
        class Bar(enum.Enum):
            a = 1
            b = 2

        @dataclasses.dataclass
        class Baz:
            x: int

        def __init__(self, catch_all: CatchAll = None):
            self.catch_all = catch_all

    class _Schema(marshmallow.Schema):
        foo = marshmallow_enum.EnumField(Foo.Bar)
        baz = marshmallow.Nested(marshmallow.Schema.from_dataclass(Foo.Baz))

    schema = _Schema()
    obj = schema.load({"foo": Foo.Bar.b, "baz": {"x": 42},
                       "_UNKNOWN0": "test"})

    out

# Generated at 2022-06-13 19:23:16.258143
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    err = UndefinedParameterError("test")

# Generated at 2022-06-13 19:23:20.698515
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class _TestClass():
        def __init__(self, *, a: int, b: Optional[str]):
            self.a = a
            self.b = b

    obj = _TestClass()
    init = _UndefinedParameterAction.create_init(obj)
    assert init.__name__ == "__init__"



# Generated at 2022-06-13 19:23:51.782700
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    """
    Test the method handle_dump that is the same for all inherited classes.
    """
    class DummyClass:
        pass

    assert _UndefinedParameterAction.handle_dump(DummyClass) == {}


# Unit tests for _UndefinedParameterAction

# Generated at 2022-06-13 19:23:54.579928
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class TestClass:
        def __init__(self):
            pass
    assert(_UndefinedParameterAction.handle_dump(TestClass()) == {})

# Generated at 2022-06-13 19:23:59.597815
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        x: int
        y: int

    testobj = TestClass(x=2, y=3)
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                        testobj.__dict__)
    assert result == {"x": 2, "y": 3}



# Generated at 2022-06-13 19:24:11.106801
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Because of the __init__ override, mypy complains that the init
    signature is not recognized.
    This test ensures that the init signature is still the same!
    """
    from typing import Tuple

    from dataclasses import dataclass

    @dataclass
    class TestClass:

        def __init__(self, a: int, b: int, c: int, d: Optional[CatchAllVar]):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    func = _IgnoreUndefinedParameters.create_init(TestClass)
    assert func(TestClass, 1, 2, 3, a=4, b=5, c=6)

# Generated at 2022-06-13 19:24:14.107452
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class TestClass:
        undefined: CatchAll = None

    assert _CatchAllUndefinedParameters.handle_to_dict(TestClass,
                                                       {"undefined": {
                                                           "foo": "bar"}}) == {"foo": "bar"}

# Generated at 2022-06-13 19:24:18.138437
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import dataclasses
    import dataclasses_json

    @dataclasses.dataclass
    class Dummy:
        a: int
        b: int
        c: int

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    dummy = Dummy(1, 2, 3)
    expect = {'a': 1, 'b': 2, 'c': 3}
    assert vars(dummy) == expect



# Generated at 2022-06-13 19:24:19.656340
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:24:27.370059
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError()
    UndefinedParameterError(valid_data={"foo": 1}, errors={"bar": "baz"})
    UndefinedParameterError(valid_data={"foo": 1},
                            errors={"bar": "baz"},
                            fields_schema={'foo': 'This is a schema for foo'},
                            messages={'bar': 'whee'})
    UndefinedParameterError(valid_data={"foo": 1},
                            errors={"bar": "baz"},
                            data={'foo': 'This is a schema for foo'},
                            messages={'bar': 'whee'})

# Generated at 2022-06-13 19:24:37.094571
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestObject:
        a: int
        b: int
        c: int
        d: Optional[CatchAllVar]

        def __init__(self, a_in: int, b_in: int = 3, c_in: int = 4,
                     **kwargs) -> None:
            self.a: int = a_in
            self.b: int = b_in
            self.c: int = c_in

    kwargs = {'a': 1, 'd': {'c': 5}}
    o = TestObject(**kwargs)
    assert o.a == 1
    assert o.b == 3
    assert o.c == 5
    assert o.d == {}


# Generated at 2022-06-13 19:24:38.780587
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    msg = "foo"
    UndefinedParameterError(msg)

# Generated at 2022-06-13 19:25:32.821574
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class A:
        def __init__(self, a, b, c=None):
            pass

    class B(A):
        def __init__(self, d, b, c=None, i=3):
            super().__init__(b, c)

    class C(B):
        pass


    def test_catch_all_init(obj):
        init = _CatchAllUndefinedParameters.create_init(obj)
        for i in range(1, 5):
            init(obj, *(i for i in range(i)), **{})


    test_catch_all_init(A)
    test_catch_all_init(B)
    test_catch_all_init(C)

# Generated at 2022-06-13 19:25:37.983037
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    import dataclasses

    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str

    known_parameters, unknown_parameters = \
        _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                   {'a': 2, 'b': '123'})

    assert unknown_parameters == {}



# Generated at 2022-06-13 19:25:41.660296
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    dump_obj = _UndefinedParameterAction()
    assert dump_obj.handle_dump(obj=None) == {}
    assert dump_obj.handle_dump(obj="test_obj") == {}



# Generated at 2022-06-13 19:25:45.128975
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    # type: () -> None
    with pytest.raises(UndefinedParameterError):
        raise UndefinedParameterError(
            f"Testing that {UndefinedParameterError.__name__} can be raised.")

# Generated at 2022-06-13 19:25:49.331828
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass(unsafe_hash=True)
    class Test:
        a: int = 5
        b: str = "test"

        def __init__(self, a: int, b: str, c: int):
            pass

    i = _IgnoreUndefinedParameters.create_init(Test)
    assert i("test") is None

# Generated at 2022-06-13 19:25:59.038728
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import dataclasses
    from dataclasses_json.undefined import _IgnoreUndefinedParameters

    @dataclasses.dataclass
    class X:
        a: int
        b: str
        c: int

    def _assert_init(x, a, b, c=None):
        """
        Helper to test that the init function has the correct signature and
        it can be called with the parameters (including defaults).
        """
        assert inspect.signature(x.__init__).parameters.keys() == \
               {"self", "a", "b", "c"}

        # Can call with defaults
        x.__init__()

        # Can not call with more parameters
        tried = False
        try:
            x.__init__(1, "1", 1, 1)
        except TypeError:
            tried

# Generated at 2022-06-13 19:26:04.509465
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    input_dict = {"_UNKNOWN2": 3, "_UNKNOWN0": 1, "_UNKNOWN1": 2}
    ref_result = {"_UNKNOWN0": 1, "_UNKNOWN1": 2, "_UNKNOWN2": 3}

    class Test:
        a: int

    result = _CatchAllUndefinedParameters.handle_to_dict(Test(), input_dict)
    assert ref_result == result

# Generated at 2022-06-13 19:26:09.387826
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class CatchAllTest:
        a: int
        b: int = 5
        c: CatchAll = None

    test_dict = {"a": 2, "b": 3, "c": {"d": 4}}
    result = _CatchAllUndefinedParameters.handle_from_dict(CatchAllTest,
                                                           test_dict)
    assert result == {"a": 2, "b": 3, "c": {"d": 4}}

# Generated at 2022-06-13 19:26:17.507570
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Foo:
        a: str
        b: int
        c: Optional[CatchAllVar] = dataclasses.field(
            default=None)  # type: ignore

    @dataclasses.dataclass
    class Bar(Foo):
        a: str
        b: int
        c: Optional[CatchAllVar] = dataclasses.field(
            default=None)  # type: ignore
        d: str

    assert _CatchAllUndefinedParameters.create_init(Foo)(Foo, "foo", 1)
    assert _CatchAllUndefinedParameters.create_init(Bar)(Bar, "bar", 2, "baz")

    # Default is dict, so we don't need to pass a parameter
    assert _CatchAllUndefinedParameters.create_init

# Generated at 2022-06-13 19:26:23.236091
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json.utils import CatchAll
    from dataclasses import dataclass

    @dataclass
    class User:
        id: str
        unknown: CatchAll = None

    instance = User(**{"id": "", "unknown": {"test": 1}})
    assert instance.unknown == {"test": 1}



# Generated at 2022-06-13 19:28:20.923258
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    def assert_correct_parameter_output(cls,
                                        kvs: Dict[str, Any],
                                        expected_kvs: Dict[str, Any]):
        result = _UndefinedParameterAction.handle_from_dict(cls, kvs)
        assert result == expected_kvs

    # noinspection PyUnresolvedReferences
    from dataclasses_json.tests._test_utils import _TestClass

    # noinspection PyUnresolvedReferences
    from dataclasses_json.tests._test_utils import \
        _TestClassWithCatchAllField


# Generated at 2022-06-13 19:28:25.378890
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():

    class A:
        def __init__(self, a: int, b: float = 3.4):
            self.a = a
            self.b = b

    a = A(3)
    assert a.a == 3
    assert a.b == 3.4

    with pytest.raises(UndefinedParameterError):
        _ = A(4, b=4.2, c="c")

# Generated at 2022-06-13 19:28:33.250409
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from datetime import date
    from typing import List

    from dataclasses import dataclass
    from dataclasses_json.config import Config

    @dataclass
    class User:
        name: str
        dear: str = "Dear"
        age: int = 0
        birth_date: date = dataclasses.field(default=date(1900, 1, 1))
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default=dataclasses.field(default_factory=dict))

    config = Config.define(
        ignore_unknown_key=True,
        undefined=Undefined.INCLUDE,
        letter_case=LetterCase.CAMEL
    )


# Generated at 2022-06-13 19:28:38.416411
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Foo:
        i: int
        name: str
        undefined_parameters: Optional[CatchAllVar] = dataclasses.field(
            default=None)


    f = Foo(i=2, name="foo", undefined_parameters={
        "bar": "blub",
        "baz": "bump"
    })

    # Test that CatchAll is not written to the output

# Generated at 2022-06-13 19:28:48.941134
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class A:
        def __init__(self, a, b, c=1, d=2):
            pass


    init_signature = inspect.signature(A.__init__)

    num_params_takeable = len(init_signature.parameters) - 1
    num_args_takeable = num_params_takeable - 3

    a, b, c, d = 1, 2, 3, 4

    args = (a, b,)
    kwargs = {"c": c, "d": d}
    args = args + (1,) * (num_args_takeable - len(args))
    bound_parameters = init_signature.bind(*args, **kwargs)

    bound_parameters.apply_defaults()

    arguments = bound_parameters.arguments

# Generated at 2022-06-13 19:29:02.643604
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from dataclasses import dataclass
    import inspect

    @dataclass
    class TestClass:
        a: str
        b: int = 5
        c: bool = True
        d: int
        e: str

        def __init__(self, a: str, b: int, c: bool, d: int, e: str,
                     f: float = 1.0):
            pass

    catch_all_parameter_action = _UndefinedParameterAction()
    new_init = catch_all_parameter_action.create_init(TestClass)

    assert new_init(TestClass("a", 5, True, 6, "e", 1.0)) == \
           TestClass("a", 5, True, 6, "e", 1.0)

# Generated at 2022-06-13 19:29:10.549038
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Mock:
        def __init__(self, catch_all: Optional[CatchAllVar] = None):
            self.catch_all = catch_all

        def __eq__(self, other):
            return self.catch_all == other.catch_all

    mock = Mock({"a": 1})
    base = {"a": 1}
    assert {'a': 1} == _CatchAllUndefinedParameters.handle_to_dict(mock, base)

    mock = Mock({"b": 2})
    assert {**base, **{"b": 2}} == _CatchAllUndefinedParameters.handle_to_dict(mock, base)

    mock2 = Mock({"a": 2})
    assert {'a': 2} == _CatchAllUndefinedParameters.handle_to_dict(mock2, base)

# Generated at 2022-06-13 19:29:16.196780
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class A:
        def __init__(self, a: int, b: int, c: int):
            self.a = a
            self.b = b
            self.c = c

    f = _IgnoreUndefinedParameters.create_init(A)
    f(A, 1, 2, 3, d=4)

# Generated at 2022-06-13 19:29:24.226649
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    def _create_class(field_cls):
        @dataclasses.dataclass
        class _TestClass:
            a: int
            b: float
            c: str
            ca: field_cls

        return _TestClass

    TestClass = _create_class(CatchAll)

    kvs = {"a": 1, "b": 1.0, "c": "1", "ca": {"d": 2}}
    expected_initial_params = kvs
    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == expected_initial_params

    kvs = {"a": 1, "b": 1.0, "c": "1", "d": 2}

# Generated at 2022-06-13 19:29:25.926553
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("")