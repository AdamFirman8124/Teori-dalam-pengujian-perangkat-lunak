

# Generated at 2022-06-13 19:20:48.937232
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class SomeClass:
        a: str
        b: int
    parameters = {
        "a": "some string",
        "b": 42,
        "c": "additional parameter"
    }
    try:
        _RaiseUndefinedParameters.handle_from_dict(cls=SomeClass, kvs=parameters)
        assert False, "UndefinedParameterError should have been raised"
    except UndefinedParameterError as err:
        assert err.messages["input"]["c"] == "Received undefined initialization arguments {'c': 'additional parameter'}"



# Generated at 2022-06-13 19:20:54.324705
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass
    from dataclasses_json import config
    import pytest

    @dataclass
    class TestClassFromDict:
        foo: int = 42

        def __init__(self, **kwargs) -> None:
            super().__init__()
            self.__dict__.update(kwargs)

    def test(input_dict: Dict[str, Any], expected_output: Dict[str, Any]):
        input_dict_copy = input_dict.copy()
        result = _CatchAllUndefinedParameters.handle_from_dict(
            TestClassFromDict, input_dict_copy)
        assert result == expected_output
        assert input_dict_copy == input_dict

    test({}, {'foo': 42})

# Generated at 2022-06-13 19:21:01.590961
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    undefined = Undefined.EXCLUDE

    @dataclasses.dataclass(undefined=undefined)
    class Foo:
        a: int
        b: str

    foo = Foo(a=1, b="2")
    assert foo.a == 1
    assert foo.b == "2"

    try:
        Foo(a=1, b="2", c=3)
        assert False
    except TypeError:
        assert True

    try:
        Foo(a=1, b="2", c=3, d=4)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 19:21:05.895553
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class Test:
        def __init__(self, a, b, c=0, *, d: CatchAll = None):
            pass

    TestInit = _CatchAllUndefinedParameters.create_init(Test)

    assert TestInit is not Test.__init__
    assert TestInit is not _CatchAllUndefinedParameters.create_init(Test)

# Generated at 2022-06-13 19:21:15.323252
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import sys

    import pytest

    @functools.lru_cache(maxsize=None)
    def _create_init_test_class(parameters):
        class _TestClass:
            def __init__(self, *args, **kwargs):
                ...

        _TestClass.__init__ = parameters["init"]
        return _TestClass

    @pytest.mark.parametrize("raise_error", [
        False,
        True
    ])
    def test_invalid_input(raise_error):
        # We need to create an empty class of which we can create
        # a dataclass
        class _TestClass:
            def __init__(self, *args, **kwargs):
                ...


# Generated at 2022-06-13 19:21:24.069877
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json.utils import CatchAll
    from dataclasses import dataclass, fields
    from typing import Optional


    @dataclass
    class AlwaysCatchAll:
        always_catch_all: Optional[CatchAll] = None
        k: str = "value"
        j: int = 10

    # When no undefined parameters are given,
    # the default value for always_catch_all is set
    class_fields = fields(AlwaysCatchAll)
    d = _CatchAllUndefinedParameters.handle_from_dict(
        AlwaysCatchAll, {})
    assert d == {class_fields[0].name: {}, class_fields[1].name: "value",
                 class_fields[2].name: 10}

    # When undefined parameters are given,
    # the default value for always_catch

# Generated at 2022-06-13 19:21:25.453855
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError.__init__()

# Generated at 2022-06-13 19:21:38.259872
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class TestClass_1:
        def __init__(self, field_1: str, field_2: str,
                     unknown_1: str, unknown_2: str):
            self.field_1 = field_1
            self.field_2 = field_2

    class TestClass_2(TestClass_1):
        def __init__(self, field_1: str, field_2: str,
                     unknown_1: str, unknown_2: str,
                     **unknown):
            super().__init__(field_1=field_1, field_2=field_2,
                             unknown_1=unknown_1, unknown_2=unknown_2)

    test_object_1 = TestClass_1("field_1", "field_2", "unknown_1", "unknown_2")
    test_object_2

# Generated at 2022-06-13 19:21:41.986240
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import typing

    class Foo:
        def __init__(self, a, b, c):
            pass

    init = _IgnoreUndefinedParameters.create_init(Foo)()
    assert typing.get_type_hints(init) == {'self': Foo,
                                           'a': Any,
                                           'b': Any,
                                           'c': CatchAllVar}
    foo = init(1, 2, 3, d=4, e=5)
    assert isinstance(foo, Foo)



# Generated at 2022-06-13 19:21:44.027852
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError()
    except UndefinedParameterError:
        pass



# Generated at 2022-06-13 19:22:03.998726
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    input_parameters = ["one", "two", "three"]
    expected_results = input_parameters

    class Tester:
        def __init__(self, one, two, three):
            self.one = one
            self.two = two
            self.three = three

    for input_parameters in [
        input_parameters,  # test exact match
        ["one", "two", "three", "four"],  # test additional parameter
        ["one", "two"],  # test missing parameter
    ]:
        received_result = _RaiseUndefinedParameters.handle_from_dict(
            cls=Tester, kvs=dict(zip(input_parameters, expected_results)))
        assert received_result == dict(zip(input_parameters, expected_results))



# Generated at 2022-06-13 19:22:12.616608
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from tests.classes import A, B

    test_kvs = dict(x=1, y=2)
    known_kvs = dict(x=1, y=2)
    unknown_kvs = dict()
    assert _RaiseUndefinedParameters.handle_from_dict(A, test_kvs) == known_kvs

    test_kvs = dict(x=1, y=2, z=3)
    known_kvs = dict(x=1, y=2)
    unknown_kvs = dict(z=3)
    assert _RaiseUndefinedParameters.handle_from_dict(
        A, test_kvs) == known_kvs

    given_kvs = dict()
    assert _RaiseUndefinedParameters.handle_from_dict(
        A, given_kvs) == given_k

# Generated at 2022-06-13 19:22:22.443812
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    def test_function(self, a=1, b=2, c=3, *, d=4, e=5, **kwargs):
        print(locals())

    init = _IgnoreUndefinedParameters.create_init(test_function)
    init(None, 0, 1, 2, 3, 4, 5, 6, e=6, c=6, f=6, g=6)
    init(None, 0, 1, 2, 3, 4, 5, 6)

# Generated at 2022-06-13 19:22:31.384014
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        a: int
        b: float

    test_class = TestClass
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(test_class,
                                                   {'a': 1, 'b': 1.0,
                                                    'c': 'c'})



# Generated at 2022-06-13 19:22:41.045526
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Foo:
        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b


    kvs = {"a": 3, "b": 1, "c": 2}
    received = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    assert received == {"a": 3, "b": 1}

    kvs = {"a": 3, "b": 1}
    received = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    assert received == {"a": 3, "b": 1}



# Generated at 2022-06-13 19:22:49.829926
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, a, b, c, d=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    test = TestClass(a=1, b=2, c=3, d=4)

    kvs = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
    }
    res = _IgnoreUndefinedParameters.handle_to_dict(test, kvs)
    assert res == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
    }


# Generated at 2022-06-13 19:23:00.492761
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        a: int
        b: int

        def __init__(self, a: int = 0, b: int = 0):
            self.a = a
            self.b = b

    test_obj = TestClass()
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                        {"a": 1})
    assert result == {"a": 1}

    test_obj = TestClass()
    assert test_obj.a == 0
    assert test_obj.b == 0

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass,
                                                   {"a": 1, "c": 3})

    assert test_obj.a == 0
    assert test_obj.b == 0


# Generated at 2022-06-13 19:23:05.902877
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass:
        def __init__(self, name: str, value: int):
            self.name = name
            self.value = value

    kvs: Dict[str, Any] = {"name": "Fred", "value": 1, "color": "red"}
    known, unknown = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=TestClass, kvs=kvs)
    assert known == {"name": "Fred", "value": 1}
    assert unknown == {"color": "red"}



# Generated at 2022-06-13 19:23:14.299146
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    init = _CatchAllUndefinedParameters.create_init(
        SampleClassWithCatchAll)
    instance = init(a="a", b="b", c="c", defined_parameter="parameter",
                    catch_all={"b": "b"})
    assert instance.a == "a"
    assert instance.b == "b"
    assert instance.c == "c"
    assert instance.defined_parameter == "parameter"
    assert instance.catch_all == {"b": "b"}



# Generated at 2022-06-13 19:23:21.219787
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    @dataclasses.dataclass
    class Simple:
        field_1: str
        field_2: Any

    input = Simple(field_1="a", field_2={1: 2})
    output = _UndefinedParameterAction.handle_to_dict(input, {"field_1": "a",
                                                               "field_2": {1: 2}})
    assert len(output) == 2
    assert output["field_1"] == "a"
    assert output["field_2"] == {1: 2}



# Generated at 2022-06-13 19:24:02.632133
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import pytest


    class TestCase:
        pass


    class TestCaseWithIgnoreUndefinedParameters(TestCase):
        def __init__(self, var1: str, var2: str, var3: str, var4: str):
            pass


    class TestCaseWithIgnoreUndefinedParametersElementary(TestCase):
        def __init__(self, a, b, c, d):
            pass



# Generated at 2022-06-13 19:24:12.637025
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class SimpleClass:
        a: str
        b: int

    kvs = {"a": "foo", "b": 1, "c": "bar"}
    kvs_expected = {"a": "foo", "b": 1}
    assert (_RaiseUndefinedParameters.handle_from_dict(
        cls=SimpleClass, kvs=kvs) == kvs_expected)

    # Should raise if undefined parameters are given
    kvs = {"a": "foo", "b": 1, "c": "bar"}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(cls=SimpleClass, kvs=kvs)



# Generated at 2022-06-13 19:24:17.234334
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("error")
    except UndefinedParameterError as error:
        assert error.messages == ["error"]
    else:
        raise ValueError("UndefinedParameterError could not be raised")



# Generated at 2022-06-13 19:24:24.763140
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    from dataclasses import dataclass, field

    from marshmallow import Schema
    from marshmallow.fields import Integer, Str

    @dataclass
    class Example:
        a: int
        b: int

        def __init__(self, a: int, b: int = 1, catch_all: Optional[CatchAllVar] = field(default_factory=dict)):
            pass

    class ExampleSchema(Schema):
        a = Integer()

        class Meta:
            unknown = Undefined.INCLUDE
            additional = ("b",)

    @dataclass
    class Example2:
        a: int
        b: int
        c: int


# Generated at 2022-06-13 19:24:27.671582
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class Foo:
        pass

    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(Foo, {"a": 1})


# Unit tests for handle_dump method of class
# _CatchAllUndefinedParameters

# Generated at 2022-06-13 19:24:28.996455
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:24:36.430327
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        x: int
        y: str

    # Test that the method raises when undefined parameters are given
    kvs = {"x": 1, "y": "2", "z": 3}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)

    # Test that defined parameters are handled correctly
    kvs = {"x": 1, "y": "2"}
    assert _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs) == kvs



# Generated at 2022-06-13 19:24:45.552449
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        known_parameter: Any
        catch_all: Optional[CatchAllVar] = None
        _undefined_parameter: _UndefinedParameterAction = \
            _CatchAllUndefinedParameters

    assert TestClass._undefined_parameter.handle_from_dict(
        TestClass, {
        "known_parameter": "value"}) == {"known_parameter": "value",
                                         "catch_all": {}}
    assert TestClass._undefined_parameter.handle_from_dict(
        TestClass, {
        "known_parameter": "value", "catch_all": {}}) == {"known_parameter":
                                                          "value", "catch_all": {}}
    assert TestClass._undefined_parameter.handle_from

# Generated at 2022-06-13 19:24:55.809608
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass(undefined=Undefined.INCLUDE)
    class Test:
        a: str
        b: Optional[CatchAllVar]

    assert Test("hello", {}) == Test("hello", {})

    # Test if CatchAllVar is written to if it is default
    assert Test("hello", CatchAll()) == Test("hello", {'a': 1, 'b': 2})

    # Test if CatchAllVar is written to if it is not default
    assert Test("hello", {}) == Test("hello", {'a': 1, 'b': 2})

    # Test if an error is raised if CatchAllVar is not a dict
    with pytest.raises(UndefinedParameterError):
        Test("hello", "hello")

    # Test if I can provide a parameter with the same

# Generated at 2022-06-13 19:25:03.728569
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    import dataclasses

    @dataclasses.dataclass
    class TestClass:
        a: str
        b: str
        c: Optional[CatchAllVar] = None

    test_class = TestClass(a="a", b="b")
    initial_dict = {"a": "a", "b": "b"}
    # Should not be affected
    output_dict = _CatchAllUndefinedParameters.handle_from_dict(
        TestClass, initial_dict)
    assert output_dict == initial_dict
    # Should be passed to catch_all
    initial_dict = {"a": "a", "b": "b", "c": "c"}
    output_dict = _CatchAllUndefinedParameters.handle_from_dict(
        TestClass, initial_dict)

# Generated at 2022-06-13 19:25:55.251038
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    """
    Test whether the constructor of the class UndefinedParameterError gets
    called correctly.
    :return: None
    """

    UndefinedParameterError(message="Test Message")

# Generated at 2022-06-13 19:26:04.600575
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import pytest
    """
    Tests the handle_to_dict method of the class _CatchAllUndefinedParameters
    """
    class Example:
        def __init__(self, foo: str, bar: str,
                     catch_all: Optional[CatchAllVar] = None) -> None:
            self.foo = foo
            self.bar = bar
            self.catch_all = catch_all

        def to_dict(self) -> Dict[Any, Any]:
            return {
                "foo": self.foo,
                "bar": self.bar,
            }

    def run_test(given, expected):
        obj = Example("foo", "bar", catch_all=given)
        result = _CatchAllUndefinedParameters.handle_to_dict(obj, obj.to_dict())
        assert result["foo"]

# Generated at 2022-06-13 19:26:13.033568
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    """
    Unit test that ensures that the method _UndefinedParameterAction.handle_to_dict
    returns the right dictionary.
    """
    # Create test class
    @dataclasses.dataclass
    class TestClass:
        foo: int
        bar: str
        # This field is used to test whether only _UNKNOWN* tags are removed.
        # If this tag is removed, the tests will fail.
        _UNKNOWN1: bool
        _UNKNOWN2: bool

    test_obj_0 = TestClass(foo=1, bar="bar", _UNKNOWN1=True, _UNKNOWN2=False)
    test_obj_1 = TestClass(foo=1, bar="bar", _UNKNOWN1=False, _UNKNOWN2=True)


# Generated at 2022-06-13 19:26:18.506954
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    CATCH_ALL = Optional[CatchAllVar]

    @dataclasses.dataclass
    class Test(object):

        data: CATCH_ALL = dataclasses.field(default_factory=dict)

        def __init__(self, *_, **__):
            raise RuntimeError

    cls = Test()
    _CatchAllUndefinedParameters.create_init(cls)

# Generated at 2022-06-13 19:26:26.711603
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Test that the create_init method of _IgnoreUndefinedParameters
    works as expected.
    """

    class TestClass:
        def __init__(self,
                     a: str,
                     b: int,
                     c: bool,
                     d: int = 6,
                     e: str = "bla") -> None:
            pass

    obj = TestClass
    _IgnoreUndefinedParameters.create_init(obj)
    t = TestClass("a", 1, True, 3, "x")
    assert t.__init__ is _IgnoreUndefinedParameters.create_init(obj)


# Generated at 2022-06-13 19:26:37.470328
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    class _TestClass:
        def __init__(self, a: str, b: str,
                     c: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c

    test_case = _TestClass("a", "b")
    init_function = test_case.__init__
    init_function_catch_all = _CatchAllUndefinedParameters.create_init(
        test_case)
    expected_result = {"a": "a", "b": "b", "c": {}}

    argspec_init = inspect.getfullargspec(init_function)
    argspec_catch_all_init = inspect.getfullargspec(init_function_catch_all)
    assert argspec_init.args == argspec_catch_all_init

# Generated at 2022-06-13 19:26:45.702897
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class CatchAllDataclass:
        foo: int
        bar: str
        catch_all: CatchAll

    dataclass = CatchAllDataclass(foo=1, bar="qux", catch_all={"test": True})

    kvs = {"foo": 1, "bar": "qux", "catch_all": {"test": True}}
    kvs_without_catch_all = {"foo": 1, "bar": "qux"}
    assert _CatchAllUndefinedParameters \
               .handle_to_dict(dataclass, kvs) == kvs_without_catch_all



# Generated at 2022-06-13 19:26:47.987851
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("some error")
    except UndefinedParameterError as e:
        assert(str(e) == "some error")

# Generated at 2022-06-13 19:26:56.837277
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class _TestClass1:
        defined: int
        field_without_default: float

        def __init__(self, defined: int, field_without_default: float,
                     catch_all: Optional[CatchAllVar] = None):
            self.defined = defined
            self.field_without_default = field_without_default
            self.catch_all = catch_all

    init = _CatchAllUndefinedParameters.create_init(_TestClass1)

    # expected_parameters = {"defined": 1, "field_without_default": 0.0}
    test_output = init(None, 1, 0.0)
    assert isinstance(test_output, _TestClass1)
    assert test_output.defined == 1

# Generated at 2022-06-13 19:27:06.308125
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    @dataclasses.dataclass
    class TestClass:
        """
        Test class
        """
        a: int
        b: str

    test_cls = TestClass(a=1, b="a")
    cls = type(test_cls)
    _UndefinedParameterAction.create_init(cls)(test_cls, 3, "c")
    assert cls(a=3, b="c") == test_cls

    # Test when fields are not given by keyword
    @dataclasses.dataclass
    class TestClassUnordered:
        """
        Test class that cannot be given by keyword
        """
        a: int
        b: str

    unordered_cls = type(TestClassUnordered(a=1, b="a"))

# Generated at 2022-06-13 19:29:16.458697
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    pass

# Generated at 2022-06-13 19:29:25.796575
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    error = UndefinedParameterError(
        message="Failed to handle undefined parameters.",
        field_names=["field1", "field2", "field3"],
        fields={"field1": {"data": "data1"}, "field2": {"data": "data2"}},
        data={"key1": "value1", "key2": "value2"}
    )
    assert error.message == "Failed to handle undefined parameters."
    assert error.field_names == ["field1", "field2", "field3"]
    assert error.fields == {"field1": {"data": "data1"}, "field2": {"data": "data2"}}
    assert error.data == {"key1": "value1", "key2": "value2", "messages": []}

# Generated at 2022-06-13 19:29:35.022635
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    def __init__(self, a: int, b: int, c: int, d: int, e: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    class TestClass:
        __init__ = __init__

    new_init = _UndefinedParameterAction.create_init(obj=TestClass)
    obj = new_init()

    assert obj is not None



# Generated at 2022-06-13 19:29:39.015657
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    assert _UndefinedParameterAction.handle_to_dict({}, {}) == {}
    assert _UndefinedParameterAction.handle_to_dict({}, {"test": 1}) == {"test": 1}



# Generated at 2022-06-13 19:29:47.631174
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # The code here works, the issue is that mypy thinks the initialization is
    # wrong:
    # https://github.com/python/mypy/issues/6910
    @dataclasses.dataclass
    class Point:
        x: int
        y: int
        catch_all: Optional[CatchAllVar] = dataclasses.field(
            default=CatchAllVar())

    point = Point(x=1, y=2, catch_all={"color": "red", "z": 3})
    from pprint import pprint

    pprint(dataclasses.asdict(point))
    pprint(point.catch_all)

# Generated at 2022-06-13 19:29:58.668333
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Test:
        def __init__(self, a=1, b=2, c=3):
            self.a = a
            self.b = b
            self.c = c

        def to_dict(self):
            kvs = {"a": self.a, "b": self.b, "c": self.c}
            return _CatchAllUndefinedParameters.handle_to_dict(self, kvs)

    assert Test().to_dict() == {"a": 1, "b": 2, "c": 3}
    assert Test(a=4).to_dict() == {"a": 4, "b": 2, "c": 3}
    assert Test(a=4).to_dict() == {"a": 4, "b": 2, "c": 3}

# Generated at 2022-06-13 19:30:03.536323
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class TestClass:
        a: int

    input = dict(a=1, b=2)
    expected = dict(a=1)
    actual = _RaiseUndefinedParameters.handle_from_dict(TestClass, input)

    assert expected == actual



# Generated at 2022-06-13 19:30:08.113582
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    # type: () -> None
    class A(object):
        def __init__(self, a, b, c=1, d=2):
            pass

    new_init = _CatchAllUndefinedParameters.create_init(A)
    a = A('a', 'b')

    # Should ignore any unknown parameters
    new_init(a, 'c', 'd', x=3, y=4)

# Generated at 2022-06-13 19:30:09.143775
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}

# Generated at 2022-06-13 19:30:18.848299
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class Foo:
        a: Any
        b: Any
        c: Any = 0

    kvs = {"a": 3, "b": 2, "d": 4}

    result = _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)

    expected_result = {"a": 3, "b": 2}
    assert result == expected_result, "The action RaiseUndefinedParameters " \
                                      "did not work as expected."
    # UndefinedParameterError raised here
    try:
        _RaiseUndefinedParameters.handle_from_dict(Foo, kvs)
    except UndefinedParameterError:
        pass
    else:
        assert False, "Expected UndefinedParameterError to be raised."