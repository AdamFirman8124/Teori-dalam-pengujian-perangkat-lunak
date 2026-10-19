

# Generated at 2022-06-13 19:20:41.999469
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("test")

# Generated at 2022-06-13 19:20:53.155974
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass
    from typing import List

    @dataclass
    class TestClass:
        a: int
        b: float = 5.0
        c: List[int] = dataclasses.field(default_factory=list)
        d: str = "Hello World"
        e: CatchAll = dataclasses.field(default_factory=dict)

        def __init__(self, a, b=5.0, c=None, d="Hello World", e=None):
            # Marshmallow will call `__init__` directly, so we need to call
            # `super()` ourselves to avoid an infinite loop.
            self.a = a
            self.b = b
            self.c = c if c is not None else []
            self.d = d

# Generated at 2022-06-13 19:20:58.708868
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    """
    Tests for the handle_from_dict method in class
    _CatchAllUndefinedParameters
    """
    # noinspection PyProtectedMember
    class A:
        __parameters__ = dataclasses.dataclass(
            frozen=True,
            eq=False,
            order=False,
            unsafe_hash=True,
            init=False,
            repr=False,
            kw_only=True,
            # type: ignore
            undefined=_CatchAllUndefinedParameters
        )

        catch_all: CatchAll
        a: int = 1
        b: int = dataclasses.field(default=2)
        c: int = dataclasses.field(default_factory=lambda: 3)


# Generated at 2022-06-13 19:21:02.610692
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Example:
        foo: int
        bar: int
        ca: CatchAll

        def __init__(self, foo: int, bar: int, ca: CatchAll):
            self.foo = foo
            self.bar = bar
            self.ca = ca


    given_dict = dict(foo=3,
                      bar=2,
                      _UNKNOWN1=4,
                      _UNKNOWN2=5)
    expected_dict = dict(foo=3, bar=2)
    actual_dict = _CatchAllUndefinedParameters.handle_to_dict(Example,
                                                              given_dict)
    assert actual_dict == expected_dict



# Generated at 2022-06-13 19:21:04.734013
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test msg")
    except ValidationError as e:
        assert str(e) == "test msg"

# Generated at 2022-06-13 19:21:05.673654
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    pass


# Generated at 2022-06-13 19:21:14.769039
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    from dataclasses_json.utils import CatchAllVar
    from dataclasses import dataclass

    @dataclass
    class TestDto:
        one: int
        two: int = 5
        three: Optional[CatchAllVar]

    test_dto = TestDto(1, 44)
    result = _CatchAllUndefinedParameters.handle_dump(test_dto)
    assert isinstance(result, dict)
    assert len(result) == 0

    test_dto = TestDto(1, 44, {'x': 111, 'y': 222})
    result = _CatchAllUndefinedParameters.handle_dump(test_dto)
    assert isinstance(result, dict)
    assert result == {'x': 111, 'y': 222}

# Generated at 2022-06-13 19:21:15.964905
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump({}) == {}


# Generated at 2022-06-13 19:21:24.576517
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        _UNDEFINED: CatchAll = None

        def __init__(self, defined: str, undefined: CatchAll = None):
            self.defined = defined
            self.undefined = undefined

    test_object = TestClass("defined")
    assert {} == _CatchAllUndefinedParameters.handle_to_dict(test_object, {})

    test_object = TestClass("defined")
    test_object._UNDEFINED = {}
    assert {} == _CatchAllUndefinedParameters.handle_to_dict(test_object, {})

    test_object = TestClass("defined")
    test_object._UNDEFINED = {"a": 1}
    assert {"a": 1} == _CatchAllUndefinedParameters.handle_to_dict(test_object,
                                                                    {})

   

# Generated at 2022-06-13 19:21:31.591847
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Z(object):
        def __init__(self, a: str, b: str, c: str):
            pass

    try:
        _RaiseUndefinedParameters.handle_from_dict(Z, {"a": "a", "d": 4})
        assert False
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:21:56.299798
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from dataclasses import dataclass
    from typing import List
    from dataclasses_json.undefined import dataclass_json

    @dataclass
    class Person:
        """
        A class for testing how the init method is created
        """

        name: str
        age: int
        addresses: List[str]

    original_init = Person.__init__

    def _catch_all_init(self, *args, **kwargs):
        known_kwargs, unknown_kwargs = \
            _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                Person, kwargs)
        num_params_takeable = len(
            init_signature.parameters) - 1  # don't count self

# Generated at 2022-06-13 19:22:04.421770
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    _CatchAllUndefinedParameters.handle_from_dict(
        cls=CatchAllTestClass, kvs={})
    _CatchAllUndefinedParameters.handle_from_dict(
        cls=CatchAllTestClass, kvs={"x": "foo"})
    _CatchAllUndefinedParameters.handle_from_dict(
        cls=CatchAllTestClass, kvs={"x": "foo", "catch_all": {}})
    _CatchAllUndefinedParameters.handle_from_dict(
        cls=CatchAllTestClass, kvs={"x": "foo", "catch_all": {"bar": "baz"}})

# Generated at 2022-06-13 19:22:12.759122
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    This test verifies that create_init handles undefined kwargs correctly.
    The following is tested:
    - If no catch-all field is present, the positional and the keyword
    parameters are left untouched.
    - If positional+keyword parameters are given but the catch-all field is not
    initialized (i.e. it is None), then the positional parameters will be filled
    as usual.
    - If more positional parameters are given than can be filled by the method,
    the positional parameters are truncated.
    - If positional parameters are given which can't be matched to a parameter
    these are considered to be undefined.
    - If a catch-all field is present, the catch-all field will be extended by
    the undefined parameters.
    """

# Generated at 2022-06-13 19:22:19.763409
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    UNDEFINED_KEY = "UNDEFINED"

    class ClassWithUndefined(dataclasses.dataclass):
        field_1: str
        field_2: str = dataclasses.field(metadata={UNDEFINED_KEY: "UNDEFINED"})

    def get_undefined_key_from_field(field: dataclasses.Field) -> Any:
        if UNDEFINED_KEY in field.metadata:
            return field.metadata[UNDEFINED_KEY]

    def get_undefined_key_from_field_name(obj, field_name: str) -> Any:
        field = dataclasses.fields(type(obj))[field_name]
        return get_undefined_key_from_field(field=field)

    def init_obj(**kwargs):
        return Class

# Generated at 2022-06-13 19:22:25.417639
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass1:
        param1: str = dataclasses.field(default="param1")
        catch_all: CatchAll = dataclasses.field(default=None)

    @dataclasses.dataclass
    class TestClass2:
        param1: str = dataclasses.field(default="param1")
        param2: int = dataclasses.field(default=2)
        catch_all: CatchAll = dataclasses.field(default=None)

    @dataclasses.dataclass
    class TestClass3:
        param1: str = dataclasses.field(default="param1")
        param2: int = dataclasses.field(default=2)
        catch_all: CatchAll = dataclasses.field(default={"a": 1})



# Generated at 2022-06-13 19:22:36.258067
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.utils import CatchAllVar
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        a: str
        b: int
        catch_all: CatchAllVar = CatchAll

        def __init__(self, a: str, b: int, catch_all: CatchAllVar = None):
            self.a = a
            self.b = b
            self.catch_all = catch_all or {}


# Generated at 2022-06-13 19:22:42.630704
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import marshmallow
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        a: int
        b: str
        c: bool
        d: float = 3.14
        e: int = 15

        def __init__(self, a: int, b: str, c: bool, d: float = 3.14,
                     e: int = 15):
            pass

    _IgnoreUndefinedParameters._separate_defined_undefined_kvs \
        = classmethod(_IgnoreUndefinedParameters._separate_defined_undefined_kvs)

# Generated at 2022-06-13 19:22:50.500122
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import marshmallow as mm

    @dataclasses.dataclass
    class Test:
        field: int

    def test_init(self, field):
        pass

    original_init = test_init
    init_signature = inspect.signature(original_init)

    @functools.wraps(original_init)
    def _ignore_init(self, field: int):
        original_init(
            self, field=field)

    ignore_init = _UndefinedParameterAction.create_init(Test)
    assert _IgnoreUndefinedParameters._separate_defined_undefined_kvs(Test,
                                                                      {}) == ({},
                                                                              {})

# Generated at 2022-06-13 19:23:01.228538
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class _Test:
        def __init__(self, a, b, c=1, d: CatchAll = None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    _test_init = _CatchAllUndefinedParameters.create_init(_Test)

    a = 5
    b = 6
    c = 7
    d = {1: 2}
    t = _Test(a, b, c, d)

    # Test if all parameters are passed
    assert t.a == a and t.b == b and t.c == c and t.d == d
    t2 = _test_init(t, a, b, c, d=d)
    assert t2.a == a and t2.b == b and t2.c == c and t

# Generated at 2022-06-13 19:23:07.446862
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    import copy

    @dataclasses.dataclass
    class TestClass:
        data1: int = 1
        data2: str = "asdf"
        data3: float = 3.14

    input_dict = {
        "data1": 2,
        "data2": "asdf",
        "data3": 6.34,
        "newdata": "newdata"
    }

    # Test without catch all parameter
    method = functools.partial(_UndefinedParameterAction.handle_from_dict,
                               cls=TestClass)
    assert method(input_dict) == {
        "data1": 2,
        "data2": "asdf",
        "data3": 6.34
    }

    # Test with catch all parameter

# Generated at 2022-06-13 19:23:41.551842
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Foo:

        def __init__(self, a: int, b: int, c: int = 5, d: int = 10):
            pass

    obj = Foo(1, 2, d=9)

    new_init = _IgnoreUndefinedParameters.create_init(Foo)
    new_init(obj, 3, 4, e=9, f=10)
    new_init(obj, 3, e=9, f=10)
    new_init(obj, 3)
    with pytest.raises(TypeError):
        new_init(obj, 3, 4, 5, e=9, f=10)

# Generated at 2022-06-13 19:23:49.049234
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class MyClass(object):
        def __init__(self, x: int, y: int, z: int=3):
            self._x = x
            self._y = y
            self._z = z

    # This should be the same as the original
    my_class_init = _UndefinedParameterAction.create_init(MyClass)
    my_object = MyClass(1, 2, z=3)
    assert my_object._x == 1
    assert my_object._y == 2
    assert my_object._z == 3

    # Now there is no z parameter
    my_object = MyClass(1, 2)
    assert my_object._x == 1
    assert my_object._y == 2
    assert my_object._z == 3

    # Now we have an additional parameter
    my_object = MyClass

# Generated at 2022-06-13 19:23:54.730196
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # pylint: disable=unused-variable
    import dataclasses


    @dataclasses.dataclass
    class _TestClass:
        a: str
        b: str
        c: str


    def _init_func(self, a: str = "a", b: str = "b", c: str = "c"):
        pass


    obj = _TestClass("a", "b", "c")
    obj.__init__ = _init_func
    # Create 3 instances of the same class,
    # one for each undefined parameter handler
    ignore_instance = _IgnoreUndefinedParameters.create_init(obj)
    raise_instance = _RaiseUndefinedParameters.create_init(obj)
    catch_all_instance = _CatchAllUndefinedParameters.create_init(obj)

    #

# Generated at 2022-06-13 19:24:04.907497
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Test:
        def __init__(self, a: int, b: int, c: int, d: Optional[CatchAllVar]):
            pass

    obj = Test(1, 2, c=3, d=None)

    old_init = obj.__init__

    _IgnoreUndefinedParameters.create_init(obj)
    obj.__init__(1, 2, d=None)

    # reset object to original state
    obj.__init__ = old_init



# Generated at 2022-06-13 19:24:17.069567
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    # given
    class _TestClass:
        def __init__(self, new: str, old: str, *,
                     catch_all: Optional[CatchAllVar] = None):
            self.new = new
            self.old = old
            self.catch_all = catch_all

        def __eq__(self, other):
            return self.new == other.new and self.old == other.old and \
                   self.catch_all == other.catch_all

    class _TestClassWithoutCatchAll:
        def __init__(self, new: str, old: str):
            self.new = new
            self.old = old

        def __eq__(self, other):
            return self.new == other.new and self.old == other.old


# Generated at 2022-06-13 19:24:24.736917
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class TestClass:
        def __init__(self, a: int, b: str, c: str) -> None:
            pass

    test_class = TestClass(a=0, b="b", c="c")

    init_with_all_parameters = _UndefinedParameterAction.create_init(
        test_class)

    init_with_no_parameters = \
        _IgnoreUndefinedParameters.create_init(test_class)

    init_with_no_parameters(test_class, a=0, b="b", c="c")
    with pytest.raises(TypeError):
        init_with_no_parameters(test_class)
    with pytest.raises(TypeError):
        init_with_no_parameters(test_class, a=0)

# Generated at 2022-06-13 19:24:34.466077
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class C:
        def __init__(self, a: str, b: int, c: int = -1):
            self.a = a
            self.b = b
            self.c = c

    @dataclasses.dataclass
    class D:
        a: str
        b: int
        c: int = -1

    @dataclasses.dataclass
    class CatchAllD:
        a: str
        b: int
        c: int = -1
        _undefined_parameters: Optional[CatchAllVar] = None

    # Test from class
    new_init = _CatchAllUndefinedParameters.create_init(C)
    a = new_init(C, 1, 2, 3)

    assert a.a == 1
    assert a.b == 2
    assert a.c

# Generated at 2022-06-13 19:24:45.068451
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class _TestClass:
        def __init__(self, a: int, b: int, c: int):
            pass

        def __eq__(self, other):
            return isinstance(other, self.__class__) and \
                self.__dict__ == other.__dict__

    test_kvs = {
        "a": 4,
        "b": 5,
        "c": 6,
    }

    expected_kvs = {
        "a": 4,
        "b": 5,
        "c": 6,
    }

    assert expected_kvs == _UndefinedParameterAction.handle_to_dict(
        _TestClass(a=4, b=5, c=6), test_kvs
    )


# Generated at 2022-06-13 19:24:50.634621
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    # setup
    class Foo:
        def __init__(self, bar):
            self.bar = bar

    # given parameters
    kvs = {"bar": "bar", "invalid": "invalid"}

    # expected parameters
    expected = {"bar": "bar"}

    # test
    actual = _IgnoreUndefinedParameters.handle_from_dict(Foo, kvs)

    # assure
    assert expected == actual

# Generated at 2022-06-13 19:24:59.458923
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class DummyClass:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    dummy = DummyClass("A", "B", "C")

    kvs = {"a": "A", "b": "B", "c": "C"}
    assert kvs == _UndefinedParameterAction.handle_to_dict(dummy, kvs)

    kvs = {"a": "A", "b": "B", "c": "C", "d": "D"}
    assert {"a": "A", "b": "B", "c": "C"} == \
           _UndefinedParameterAction.handle_to_dict(dummy, kvs)

# Generated at 2022-06-13 19:25:58.180050
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses_json.utils import Undefined

    @dataclasses.dataclass
    class TestClass:
        a: int
        b: float
        c: str

    a, b, c = 1, 1.0, "abc"
    test = TestClass(a=a, b=b, c=c)
    test_dict = dataclasses.asdict(test)
    assert test_dict == {"a": a, "b": b, "c": c}

    test_dict_undefined = {"a": a, "b": b, "c": c, "d": "d"}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                   test_dict_undefined)



# Generated at 2022-06-13 19:26:07.300431
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import inspect
    from dataclasses_json.utils import CatchAllVar

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class TestClass:
        a: int
        b: str
        c: Optional[CatchAllVar]

        def __init__(self, a: int, b: str, c: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c
            self.init_called = True

    test_class = TestClass(a=1, b="1")
    assert test_class.a == 1
    assert test_class.b == "1"
    assert test_class.c == {}
    assert test_class.init_called is True


# Generated at 2022-06-13 19:26:09.641554
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    try:
        from dataclasses import dataclass
    except ImportError:
        return
    @dataclass
    class Foo:
        a: int
        b: int
        init = _IgnoreUndefinedParameters.create_init(Foo)

    x = Foo(1, 2, c=3)


if __name__ == "__main__":
    test__IgnoreUndefinedParameters_create_init()

# Generated at 2022-06-13 19:26:17.634560
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from marshmallow.schema import BaseSchema
    from marshmallow.fields import Field
    from marshmallow.validate import ValidationError

    class SpecialField(Field):
        """
        A special field, that modifies the underlying dict during load.
        """
        def _deserialize(self, value, attr, data) -> Any:
            data.update({"special": 5})
            return value

    class SpecialSchema(BaseSchema):
        """
        This schema has a special field.
        """
        special = SpecialField()

    class SpecialClass:
        """
        This class has a special field.
        """
        def __init__(self, **kwargs):
            self.special = kwargs["special"]

        @property
        def special(self):
            return self._special


# Generated at 2022-06-13 19:26:21.641254
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    def method(self) -> Dict[str, Any]:
        return {}

    # noinspection PyTypeChecker
    assert _UndefinedParameterAction.handle_dump(obj=method) == {}

# Generated at 2022-06-13 19:26:29.395267
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    """
    Test if handle_to_dict returns a dictionary with the same keys as the
    given dictionary.
    The dictionary should not be modified
    """
    # check if the handle to dict method of the different Undefined classes
    # returns the same dictionary
    d = {"a": "b"}
    for action in Undefined:
        undefined_class: _UndefinedParameterAction = action.value
        returned_dict = undefined_class.handle_to_dict(None, d)
        assert returned_dict == d

    # Check if the dictionary is not changed
    d2 = {"a": 1, "b": "2"}
    d_copy = d2.copy()
    _UndefinedParameterAction.handle_to_dict(None, d2)
    assert d_copy == d2



# Generated at 2022-06-13 19:26:40.164665
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from marshmallow import Schema, fields

    @dataclasses.dataclass
    class Inner1:
        field1: str

    @dataclasses.dataclass
    class Inner2:
        field2: str

    @dataclasses.dataclass
    class DummyClass:
        inner1: Inner1 = dataclasses.field(default_factory=Inner1)
        inner2: Inner2 = dataclasses.field(default_factory=Inner2)
        field: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict
        )

    init_function = _CatchAllUndefinedParameters.create_init(DummyClass)

    dummy_class = DummyClass()

# Generated at 2022-06-13 19:26:49.430060
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class A:
        def __init__(self, a: int, b: int, c: int, d: int) -> None:
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    def test_case(create_init, arguments, expected_results):
        init = create_init(A)
        result = init(A(1, 2, 3, 4), **arguments)
        actual_results = {
            "a": result.a,
            "b": result.b,
            "c": result.c,
            "d": result.d,
        }
        assert actual_results == expected_results


# Generated at 2022-06-13 19:26:57.584753
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class _Container(object):
        def __init__(self, a: int, b: int, catch_all: Optional[CatchAll] = None):
            self.a = a
            self.b = b
            self.catch_all = catch_all

    res = _CatchAllUndefinedParameters.handle_from_dict(_Container,
                                                        {"a": 1, "b": 2})
    assert res["a"] == 1
    assert res["b"] == 2
    assert res["catch_all"] == {}

    res = _CatchAllUndefinedParameters.handle_from_dict(_Container,
                                                        {"a": 1, "b": 2, "c": 3})
    assert res["a"] == 1
    assert res["b"] == 2
    assert res["catch_all"] == {"c": 3}

   

# Generated at 2022-06-13 19:26:59.546733
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test message")
    except UndefinedParameterError as e:
        assert str(e) == "test message"

# Generated at 2022-06-13 19:29:17.954628
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    initial_kvs = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    result = _IgnoreUndefinedParameters.handle_from_dict(Foo, initial_kvs)
    assert result['a'] == 1
    assert result['b'] == 2
    # Exclude the undefined parameter c

# Generated at 2022-06-13 19:29:21.393764
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class DataClass:
        a: int

    assert _UndefinedParameterAction.create_init(DataClass) \
           == DataClass.__init__



# Generated at 2022-06-13 19:29:23.797838
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(
        None) == {}
    assert _UndefinedParameterAction.handle_dump(
        "") == {}


# Generated at 2022-06-13 19:29:38.674411
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import pytest

    class A(FrozenInstance):

        def __init__(self, a, b):
            self.a = a
            self.b = b

    class B(FrozenInstance):

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    class CatchAllTest(FrozenInstance):
        def __init__(self, a, b, catch_all: CatchAll = None):
            self.a = a
            self.b = b
            self.catch_all = catch_all

    def test_good_case():
        obj = CatchAllTest(a=123, b="str")

        # No catch all given
        assert obj.catch_all is None

        # Catch all given

# Generated at 2022-06-13 19:29:48.685812
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    from dataclasses_json import DataClassJsonMixin

    class TestClass(DataClassJsonMixin):
        a: str
        b: str = "b"

    test_class = TestClass("a", "b")
    kvs = {"a": "a", "b": "b"}
    assert _UndefinedParameterAction.handle_to_dict(
        test_class, kvs) == kvs

    class TestClass(DataClassJsonMixin):
        a: str
        b: str = "b"
        __dataclass_json__ = {"undefined": Undefined.EXCLUDE}

    test_class = TestClass("a", "b")
    kvs = {"a": "a"}
    assert _UndefinedParameterAction.handle_to_dict(
        test_class, kvs) == k

# Generated at 2022-06-13 19:29:53.583831
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class C:
        def __init__(self, a: int,
                     b: int,
                     c: int,
                     d: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d


    init_no_catch_all = _CatchAllUndefinedParameters.create_init(C)
    init_with_catch_all = _IgnoreUndefinedParameters.create_init(C)
    c1 = C(1, 2, 3)
    c2 = C(1, 2, 3, {})
    c3 = C(1, 2, 3, d={"c": 3})
    c4 = C(1, 2, 3, d=CatchAllVar())

# Generated at 2022-06-13 19:29:56.415222
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("me")
    except UndefinedParameterError as e:
        assert e.messages[0] == "me"
    except:
        assert False

# Generated at 2022-06-13 19:30:07.219675
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class TestClass:
        def __init__(self, a = 1, b = 2, c = 3, d = 4, e = 5):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

    obj = TestClass(a="a", b="b", c="c", d="d", e="e")
    kvs = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
    kvs_except_e = {"a": "a", "b": "b", "c": "c", "d": "d"}
    kvs_except_a = {"b": "b", "c": "c", "d": "d", "e": "e"}
   

# Generated at 2022-06-13 19:30:13.433450
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, a: int, b: int, c: int, _UNKNOWN0: CatchAll = {}):
            self.a = a
            self.b = b
            self.c = c
            self._UNKNOWN0 = _UNKNOWN0

    class TestClassSubclass(TestClass):
        def __init__(self, a: int, b: int, c: int, _UNKNOWN0: CatchAll = {}):
            super().__init__(a, b, c, _UNKNOWN0)

    class TestClassSubclass2(TestClass):
        def __init__(self, a: int, b: int, c: int, _UNKNOWN0: CatchAll = {}):
            super().__init__(a, b, c, _UNKNOWN0)

    obj1 = TestClass

# Generated at 2022-06-13 19:30:28.978452
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # noinspection PyProtectedMember
    def _test_one_case(kvs: Dict[Any, Any], expected_output: Dict[Any, Any],
                       cls: type, undefined_parameter_action,
                       message_on_failure: str) -> None:
        result = undefined_parameter_action.handle_from_dict(kvs=kvs,
                                                             cls=cls)

        assert expected_output == result, message_on_failure

    # Verify correct behavior for ignore
    undefined_parameter_action = _IgnoreUndefinedParameters