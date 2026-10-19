

# Generated at 2022-06-13 19:20:52.351906
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json.undefined import CatchAllVar


    class TestClass:
        field1: int
        field2: str


    class TestClass2:
        field1: int
        field2: str = dataclasses.field(default="default value")
        field3: Optional[CatchAllVar] = None


    class TestClass3:
        field1: int
        field2: str = dataclasses.field(default_factory=str)
        field3: Optional[CatchAllVar] = None


    # noinspection PyUnusedLocal
    class TestClass4:
        field1: int
        field2: str = dataclasses.field(default_factory=lambda: "some value")
        field3: Optional[CatchAllVar] = None


    # noinspection PyUnused

# Generated at 2022-06-13 19:21:01.845032
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass
    from dataclasses_json.undefined import _CatchAllUndefinedParameters

    @dataclass
    class Dummy:
        a: int
        b: int
        undefined: Optional[CatchAllVar]

    assert _CatchAllUndefinedParameters.handle_to_dict(
        Dummy(a=1, b=2, undefined={}), {"a": 1, "b": 2, "undefined": {}}) == {
        "a": 1, "b": 2}
    assert _CatchAllUndefinedParameters.handle_to_dict(
        Dummy(a=1, b=2, undefined=None), {"a": 1, "b": 2}) == {
        "a": 1, "b": 2}
    assert _CatchAllUndefinedParameters.handle_to_

# Generated at 2022-06-13 19:21:10.888045
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Foo:
        def __init__(self,
                     a: int,
                     b: int = 10,
                     c: int = 100,
                     d: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    new_init = _CatchAllUndefinedParameters.create_init(Foo)
    foo = Foo(1, 2, 3, None)
    zero = Foo()

    # Catch all is None because no unhandled parameters received
    assert new_init(foo, 1, 2, 3) is None

    # Catch all contains one unhandled parameter
    assert new_init(foo, 1, 2, 3, e=7) == {'e': 7}

    # Catch all contains one unhandled parameter with value None
   

# Generated at 2022-06-13 19:21:20.750387
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import dataclasses

    @dataclasses.dataclass
    class TestClass:
        with_default: str = dataclasses.field(default="DEFAULT")
        no_default: int
        catch_all: Optional[CatchAllVar] = dataclasses.field(default=None)

    def test(input_dict, expected_output_dict):
        result = _CatchAllUndefinedParameters.handle_from_dict(
            obj=TestClass, kvs=input_dict)
        assert result == expected_output_dict

    test(input_dict={"no_default": 3},
         expected_output_dict={"no_default": 3, "with_default": "DEFAULT",
                               "catch_all": {}})

# Generated at 2022-06-13 19:21:21.819373
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("")
    except UndefinedParameterError as e:
        pass

# Generated at 2022-06-13 19:21:35.428975
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestCase:
        def __init__(self, a: int, b: int, c: CatchAll = None):
            pass

    kvs = {'a': 1, 'b': 2, 'c': {'foo': 'bar'}}
    expected_kvs = {'a': 1, 'b': 2, 'c': {'foo': 'bar'}}
    assert (
            _CatchAllUndefinedParameters.handle_from_dict(TestCase, kvs) ==
            expected_kvs)

    kvs = {'a': 1, 'b': 2, 'c': {'foo': 'bar'}, 'd': 'hello'}
    expected_kvs = {'a': 1, 'b': 2,
                    'c': {'foo': 'bar', 'd': 'hello'}}

# Generated at 2022-06-13 19:21:43.684666
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    """
    This function is a unit test for the method create_init of
    class _CatchAllUndefinedParameters. It does not need to be in this file.
    """
    import pytest
    from dataclasses import dataclass

    class CustomException(Exception):
        pass

    # Base class
    @dataclass
    class AbstractBaseClass:
        x: int

    # Test classes
    @dataclass
    class TestClass0(AbstractBaseClass):
        """
        Test Class 0:
        With catch-all field but no other fields.
        """
        catch_all: Optional[CatchAllVar] = None

    @dataclass
    class TestClass1(AbstractBaseClass):
        """
        Test Class 1:
        With catch-all field and one other field.
        """
        x: float  #

# Generated at 2022-06-13 19:21:48.771726
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert \
        _UndefinedParameterAction.handle_to_dict(None,
                                                 {'param1': 20}) == {'param1': 20}
    assert \
        _UndefinedParameterAction.handle_to_dict(None,{}) == {}

# Generated at 2022-06-13 19:21:56.387745
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass
    class A:
        a: Any
        b: Any
        c: Any
        d: Any

        def __init__(self, a, b, c, d):
            pass

    obj = A(1, 2, 3, 4)
    init = _IgnoreUndefinedParameters.create_init(obj)
    assert init is not obj.__init__
    assert inspect.signature(init) == inspect.signature(obj.__init__)

# Generated at 2022-06-13 19:22:00.150512
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    with pytest.raises(ValidationError, match=r"^Received undefined initialization arguments {'foo': 1}"):
        raise UndefinedParameterError('Received undefined initialization arguments {\'foo\': 1}')
    with pytest.raises(ValidationError, match=r"^No field of type dataclasses_json.CatchAll defined"):
        raise UndefinedParameterError('No field of type dataclasses_json.CatchAll defined')
    with pytest.raises(ValidationError, match=r"^Multiple catch-all fields supplied: 2."):
        raise UndefinedParameterError('Multiple catch-all fields supplied: 2.')

# Generated at 2022-06-13 19:22:17.888854
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    global _IgnoreUndefinedParameters
    _IgnoreUndefinedParameters = _UndefinedParameterAction
    global _UndefinedParameterAction
    _UndefinedParameterAction = _IgnoreUndefinedParameters
    kvs = {"a": 1, "b": 2, "c": 3}
    assert _IgnoreUndefinedParameters.handle_from_dict(None, kvs) == kvs



# Generated at 2022-06-13 19:22:25.309205
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    # class with 2 fields
    @dataclass_json
    @dataclass
    class TestClass:
        foo: str
        bar: int

    test_dict = {"foo": "abc", "bar": 1234, "baz": 4321}
    assert _UndefinedParameterAction._separate_defined_undefined_kvs(
        TestClass, test_dict) == ({"foo": "abc", "bar": 1234},
                                  {"baz": 4321})

    assert _RaiseUndefinedParameters.handle_from_dict(
        TestClass, test_dict) == {"foo": "abc", "bar": 1234}

    assert _IgnoreUndefinedParameters.handle_from_dict(
        TestClass, test_dict) == {"foo": "abc", "bar": 1234}

    # class with 1 field, Catch

# Generated at 2022-06-13 19:22:39.153039
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class _TestClass:
        catch_all: Optional[CatchAllVar] = None
        field: int = 1

    data = {"field": 2, "catch_all": {}}
    result = _CatchAllUndefinedParameters.handle_from_dict(_TestClass, data)
    assert result == {"field": 2, "catch_all": {}}

    data = {"field": 2, "catch_all": _TestClass.catch_all}
    result = _CatchAllUndefinedParameters.handle_from_dict(_TestClass, data)
    assert result == {"field": 2, "catch_all": {}}

    data = {"field": 2}
    result = _CatchAllUndefinedParameters.handle_from_dict(_TestClass, data)

# Generated at 2022-06-13 19:22:48.951861
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class _FakeClassUndefinedParameters:
        def __init__(self, p1: str, p2: int, p3: str = "p3",
                     p4: Any = CatchAll) -> None:
            pass

    class _FakeClassNoUndefinedParameters:
        def __init__(self, p1: str, p2: int, p3: str = "p3") -> None:
            pass


# Generated at 2022-06-13 19:22:59.299271
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: Optional[CatchAllVar]

    result = _CatchAllUndefinedParameters.handle_from_dict(A, {"a": 1, "b": 2})
    assert result == {"a": 1, "b": {"b": 2}}

    result = _CatchAllUndefinedParameters.handle_from_dict(A, {"a": 1, "b": []})
    assert result == {"a": 1, "b": []}

    result = _CatchAllUndefinedParameters.handle_from_dict(A, {"a": 1, "b": {}})
    assert result == {"a": 1, "b": {}}


# Generated at 2022-06-13 19:23:06.405325
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses_json.undefined import Undefined
    from dataclasses import dataclass

    @dataclass
    class Cl:
        a: str
        b: str
        undefined: Undefined = Undefined.RAISE

    kvs = {"a": "foo", "b": "bar", "c": "baz"}
    try:
        Cl.undefined.value.handle_from_dict(Cl, kvs)
        assert False
    except UndefinedParameterError:
        pass

    assert Cl.undefined.value.handle_from_dict(Cl, {"a": "foo", "b": "bar"}) \
           == {"a": "foo", "b": "bar"}



# Generated at 2022-06-13 19:23:14.680713
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    # Arrange
    klass = dataclasses.make_dataclass("TestClass", [
        ("a", int),
        ("b", CatchAll)])
    parameters = {"a": 1, "b": {"c": 1, "d": 2}}
    obj = klass(**parameters)
    # Act
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, parameters)
    # Assert
    assert result == {"a": 1, "c": 1, "d": 2}



# Generated at 2022-06-13 19:23:19.008130
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    kvs = {"first": 1, "second": 2}
    @dataclasses.dataclass
    class MyClass:
        first: int

    new_kvs = _UndefinedParameterAction.handle_from_dict(MyClass, kvs)
    assert new_kvs == {"first": 1}



# Generated at 2022-06-13 19:23:25.091615
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class A:
        def __init__(self, a):
            self.a = a

    a = A(a="a")
    result = _RaiseUndefinedParameters.handle_from_dict(A, {"a": "a",
                                                             "b": "b"})
    assert result == {"a": "a"}

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(A, {"b": "b"})


# Unit tests for method handle_from_dict of class _IgnoreUndefinedParameters

# Generated at 2022-06-13 19:23:29.729851
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses import dataclass

    @dataclass
    class Test:
        a: int
        b: str
        c: CatchAll

    t = Test(1, "a", {"b": 1, "c": 2})
    assert t.to_dict() == {"a": 1, "b": "a", "b": 1, "c": 2}

# Generated at 2022-06-13 19:24:01.540368
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    a = _UndefinedParameterAction.__new__(_UndefinedParameterAction)
    assert a.handle_to_dict({}, {}) == {}



# Generated at 2022-06-13 19:24:15.957659
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class MyClass:
        a: int
        b: int = 1
        c: int = 2
        d: CatchAll = None

        @classmethod
        def _undefined_parameter_action(cls) -> _UndefinedParameterAction:
            return _CatchAllUndefinedParameters

        def __init__(self, **kwargs):
            pass

    _ = MyClass._undefined_parameter_action()
    params = {"a": 3, "c": 4, "e": 5}
    try:
        MyClass.__init__(MyClass, **params)
    except TypeError as e:
        assert "got an unexpected keyword argument 'e'" in str(e)
    params = {"a": 3, "c": 4}
    MyClass(**params)

# Generated at 2022-06-13 19:24:22.862610
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a: str, b: str, c: str):
            pass

    with pytest.raises(UndefinedParameterError) as err:
        _RaiseUndefinedParameters.handle_from_dict(
            cls=TestClass, kvs={"a": "a", "b": "b", "c": "c", "d": "d"})

    assert str(err.value) == "Received undefined initialization arguments {'d': 'd'}"



# Generated at 2022-06-13 19:24:30.939748
# Unit test for method create_init of class _UndefinedParameterAction

# Generated at 2022-06-13 19:24:39.095443
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class Simple(object):
        a: int
        b: int = 4

        def __init__(self, *,
                     _undefined_parameters_action=_CatchAllUndefinedParameters,
                     **kwargs):
            self._undefined_parameters_action = \
                _undefined_parameters_action

            super().__init__(**kwargs)

        def __setattr__(self, key, value):
            if key == "_undefined_parameters_action":
                return super().__setattr__(key, value)
            else:
                return setattr(self, key, value)

        def to_dict(self) -> Dict[str, Any]:
            kvs = dataclasses.asdict(self)

# Generated at 2022-06-13 19:24:49.535043
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class TestCase:
        def __init__(self, variable_1, variable_2: int, variable_3: str,
                     variable_4: float = 3.0, variable_5: float = 4.0,
                     catch_all: Optional[CatchAllVar] = None):
            pass

    try:
        TestCase(1, 2, "3", variable_4=4.0, variable_5=5.0,
                 catch_all={"something": "else"})
    except Exception: # Something went wrong!
        assert False

    try:
        TestCase(1, 2, "3", variable_4=4.0, variable_5=5.0, something="else")
    except TypeError:
        assert True # Everything is all right


# Generated at 2022-06-13 19:24:52.340480
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump({}) == {}
    assert _UndefinedParameterAction.handle_dump(None) == {}
    assert _UndefinedParameterAction.handle_dump(["foo"]) == {}

# Generated at 2022-06-13 19:25:01.616088
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class SomeClass:
        def __init__(self, a: str = "hello"):
            self.a = a

    @dataclasses.dataclass
    class SomeDataClass:
        a: str = "hello"

    @dataclasses.dataclass
    class SomeDataClassWithCatchAll(object):
        a: str = "hello"
        catch_all: CatchAll = None

        # type: (CatchAllVar, ...) -> None

    @dataclasses.dataclass
    class SomeDataClassWithCatchAllAndDefault(object):
        a: str = "hello"
        catch_all: CatchAll = {}

    # Test 1 - vanilla class

# Generated at 2022-06-13 19:25:06.082661
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    def init(self, a: int, b: int = 3, c: int = 4, **_: Any):
        pass


    class A:# type: ignore
        def __init__(self, a, b, c):
            pass


    _IgnoreUndefinedParameters.create_init(A)

    _CatchAllUndefinedParameters.create_init(A)

# Generated at 2022-06-13 19:25:15.034250
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # case 1: default = {}
    kvs = {"bla": "foo"}
    class_fields = (
        Field(name="bla", type=str, default=""),
        Field(name="_UNKNOWN", type=Optional[CatchAllVar], default={})
    )
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        class_fields, kvs)
    known = _CatchAllUndefinedParameters.handle_from_dict(class_fields,
                                                          known)
    assert known["_UNKNOWN"] == {}

    # case 2: default = {}
    kvs = {"bla": "foo", "_UNKNOWN": {}}

# Generated at 2022-06-13 19:26:18.686198
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    test_cls = dataclasses.make_dataclass("TestClass",
                                          [("test_prop", str),
                                           ("test_prop2", str),
                                           ("test_prop3", int)])

    assert _RaiseUndefinedParameters.handle_from_dict(test_cls,
                                                      {"test_prop": "value",
                                                       "test_prop2": "value2"}) == {
        "test_prop": "value", "test_prop2": "value2"}
    # Undefined parameters are not allowed, so this call must raise an error

# Generated at 2022-06-13 19:26:24.602797
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # noinspection PyUnresolvedReferences
    from tests.sample_classes import Base, ExtendedBase

    num_class_fields = len(fields(Base))
    num_class_fields_extended = len(fields(ExtendedBase))

    assert len(fields(ExtendedBase)) == num_class_fields + 1

    _IgnoreUndefinedParameters.create_init(ExtendedBase)

# Generated at 2022-06-13 19:26:36.753144
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestDC:
        a: str = "a"
        b: str = "b"
        c: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)
        d: str = "d"

    CATCH_ALL_FIELD = _CatchAllUndefinedParameters._get_catch_all_field(
        TestDC)
    assert CATCH_ALL_FIELD == dataclasses.fields(TestDC)[2]

    init = _CatchAllUndefinedParameters.create_init(TestDC)
    assert init.__name__ == "__init__"
    assert init.__doc__ == TestDC.__init__.__doc__

    init(TestDC(), "a", "b", "d")


# Generated at 2022-06-13 19:26:47.340104
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    import marshmallow
    import marshmallow_dataclass

    @dataclasses.dataclass
    class RobustPerson:
        name: str = dataclasses.field(metadata=dict(load_from="name"))
        age: int = dataclasses.field(metadata=dict(load_from="age"))
        catches: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)

    RobustPersonSchema = marshmallow_dataclass.class_schema(RobustPerson)

    person = RobustPerson(name="Alice", age=42, catches={"gender": "f"})
    dumped_person = RobustPersonSchema().dump(person)
    assert dumped_person["gender"] == "f"
    assert dumped_person["age"] == 42

# Generated at 2022-06-13 19:26:53.943220
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    TESTCLASSES = [
        """
        @dataclasses.dataclass
        class Hello:
            str1: str
            str2: str = "Aloha"
            str3: str
        """,
        """
        @dataclasses.dataclass
        class Hello:
            str1: str
            str2: str = "Aloha"
            str3: str
            def __post_init__(self):
                pass
        """,
        """
        @dataclasses.dataclass
        class Hello:
            str1: str
            str2: str = dataclasses.field(default_factory=lambda: "Aloha")
            str3: str
        """
    ]
    expected = {"str1": "Hello", "str2": "Aloha", "str3": "World"}

# Generated at 2022-06-13 19:26:55.556836
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    test_case = {
        Undefined.INCLUDE: {},
        Undefined.RAISE: {},
        Undefined.EXCLUDE: {},
    }



# Generated at 2022-06-13 19:27:00.997219
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Foo:
        def __init__(self, a, b="default_b", **kwargs: CatchAll):
            self.a = a
            self.b = b
            self.catch_all = kwargs

    assert Foo("a", "b", c=1, d=2).catch_all == {"c": 1, "d": 2}
    assert Foo("a", c=1, d=2).catch_all == {"c": 1, "d": 2}
    assert Foo("a", CatchAll()).catch_all == {}
    assert Foo("a", "b", d=2).catch_all == {"d": 2}
    assert Foo("a", d=2).catch_all == {"d": 2}
    assert Foo("a", CatchAll(), d=2).catch_all == {}

# Generated at 2022-06-13 19:27:06.519057
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    # Arrange
    expected = {
        "answer": 42,
        "hello": "world",
    }
    kvs = {
        "answer": 42,
        "world": None,
        "hello": "world",
    }

    # Act
    actual = _CatchAllUndefinedParameters.handle_to_dict(None, kvs)

    # Assert
    assert actual == expected

# Generated at 2022-06-13 19:27:16.487489
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from marshmallow.fields import Field
    from marshmallow.schema import SchemaMeta
    from marshmallow import post_dump
    import dataclasses as dc

    class MyCatchAll(CatchAllVar):
        pass


    class MySchema(metaclass=SchemaMeta):
        name = Field()
        age = Field()
        catchall = Field(CatchAll(MyCatchAll))
        name_of_cat = Field()

        @post_dump
        def add_cat_name(self, data, **_):
            data['cat_name'] = 'Tom'
            return data


    @dc.dataclass
    class Person(metaclass=SchemaMeta):
        name: str
        age: int
        catchall: MyCatchAll



# Generated at 2022-06-13 19:27:24.660482
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert \
        _IgnoreUndefinedParameters.handle_to_dict(obj=None,
            kvs={"hello": "world"}) == {"hello": "world"}
    assert \
        _RaiseUndefinedParameters.handle_to_dict(obj=None,
            kvs={"hello": "world"}) == {"hello": "world"}
    catch_all_dict = {"hello": "world"}
    assert \
        _CatchAllUndefinedParameters.handle_to_dict(obj=None, kvs={
            "hello": "world", "catch": catch_all_dict}) == {
               "hello": "world", "catch": catch_all_dict}



# Generated at 2022-06-13 19:29:51.685167
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    # Only runs when this file is run standalone, not on import.
    import pytest
    with pytest.raises(UndefinedParameterError):
        _UndefinedParameterAction.create_init(int)

# Generated at 2022-06-13 19:29:56.783267
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    # Define a class with some fields
    @dataclasses.dataclass()
    class MyClass:
        a: int
        b: str = "b"

    result = _RaiseUndefinedParameters.handle_from_dict(cls=MyClass,
                                                        kvs={"a": 1})
    assert result == {"a": 1}
    result = _RaiseUndefinedParameters.handle_from_dict(cls=MyClass,
                                                        kvs={"b": "c",
                                                             "a": 1})
    assert result == {"b": "c",
                      "a": 1}

# Generated at 2022-06-13 19:30:00.246319
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    try:
        assert _UndefinedParameterAction.create_init(None)
        assert False, "method is abstract"
    except NotImplementedError:
        assert True



# Generated at 2022-06-13 19:30:09.339676
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class AClass:
        def __init__(self, a, b, c=3, d=4, catch_all: Optional[CatchAllVar] =
        None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.catch_all = catch_all


    class BClass:
        def __init__(self, a, b, catch_all: Optional[CatchAllVar]):
            self.a = a
            self.b = b
            self.catch_all: Optional[CatchAllVar] = catch_all


    class CClass:
        def __init__(self, a, b, d, catch_all: Optional[CatchAllVar] = {}):
            self.a = a
            self.b = b
            self

# Generated at 2022-06-13 19:30:11.026305
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError(["one", "two"])
    except ValidationError as error:
        assert error.messages == ["one", "two"]

# Generated at 2022-06-13 19:30:20.284761
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    # regular case
    assert _CatchAllUndefinedParameters.handle_from_dict(
        {"a": 1}, {'a': 1, 'b': 2}
    ) == {'a': 1, '__UNDEFINED__': {'b': 2}}

    # Test when a field with the same name as the catch-all field is given an
    # input
    class TestClass:
        def __init__(self, __UNDEFINED__: Optional[CatchAllVar] = None):
            pass

    try:
        _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                      {"__UNDEFINED__": "test"})
    except UndefinedParameterError:
        assert True
    else:
        assert False

    # Test when no undefined parameters are given and no default is given to
   