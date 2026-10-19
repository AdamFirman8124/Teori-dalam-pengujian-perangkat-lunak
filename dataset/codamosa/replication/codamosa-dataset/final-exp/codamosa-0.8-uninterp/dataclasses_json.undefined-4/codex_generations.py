

# Generated at 2022-06-13 19:20:51.885779
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class MyClass:
        a: int
        b: int
        c: int
        d: int
        e: int

        def __init__(self, *, a, b=5, c=5, **kwargs) -> None:
            self.a = a
            self.b = b
            self.c = c
            self.d = kwargs.get("d", 5)
            self.e = kwargs.get("e", 5)

    generated_init = _IgnoreUndefinedParameters.create_init(MyClass)
    old_init = MyClass.__init__
    MyClass.__init__ = generated_init
    obj = MyClass(a=1, b=2, c=3, d=4, e=5)

# Generated at 2022-06-13 19:21:01.586126
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int
        c: CatchAll = dataclasses.field(default=dict())

    def check_result(given, expected):
        result = _CatchAllUndefinedParameters.handle_from_dict(
            cls=TestClass, kvs=given)
        assert result == expected

    check_result({}, {"a": 0, "b": 0, "c": {}})
    check_result({"a": 1, "b": 2}, {"a": 1, "b": 2, "c": {}})
    check_result({"a": 1, "b": 2, "d": 3}, {"a": 1, "b": 2, "c": {"d": 3}})

# Generated at 2022-06-13 19:21:10.680340
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class M(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def to_dict(self) -> Dict[Any, Any]:
            pass

    class Mock1(M):
        @classmethod
        def from_dict(cls, kvs: Dict[Any, Any]) -> "Mock1":
            args = kvs.copy()
            args["catch_all_field"] = "expected_value"
            return cls(**args)

        def __init__(self, **kwargs):
            self.catch_all_field = kwargs.pop("catch_all_field")

        def to_dict(self):
            kvs = {"a": "b", "c": "d"}
            kvs.update(self.catch_all_field)
            return kvs


# Generated at 2022-06-13 19:21:20.544031
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class TestClass:
        def __init__(self, known_parameter, catch_all: Optional[CatchAllVar]):
            self.known_parameter = known_parameter
            self.catch_all = catch_all

    obj = TestClass(known_parameter="the_parameter",
                    catch_all={"some_key": "some_value"})

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, {"asdf": 1})
    assert result == {"asdf": 1}

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, {"asdf": 1,
                                                               "known_parameter": "the_parameter"})
    assert result == {"asdf": 1, "known_parameter": "the_parameter"}



# Generated at 2022-06-13 19:21:23.693190
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class _TestClass:
        def __init__(self, known_parameter: int):
            self.known_parameter = known_parameter

    kvs = {
        "known_parameter": 1,
        "unknown_parameter": True
    }

    known_kvs = \
        _IgnoreUndefinedParameters.handle_from_dict(_TestClass, kvs)
    assert known_kvs == {
        "known_parameter": 1
    }



# Generated at 2022-06-13 19:21:26.038283
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    exception = UndefinedParameterError("Test")
    assert exception.title == "Test"

# Generated at 2022-06-13 19:21:38.656932
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class ExampleClass:
        field: int

        def __init__(self, field: int):
            self.field = field


    @dataclasses.dataclass
    class ExampleClassWithCatchAll:
        field: int
        catch_all: CatchAll = None

        def __init__(self, field: int, catch_all: CatchAll = None):
            self.field = field
            self.catch_all = catch_all


    @dataclasses.dataclass
    class ExampleClassWithoutDefault:
        field: int
        catch_all: CatchAll

        def __init__(self, field: int, catch_all: CatchAll = None):
            self.field = field
            self.catch_all = catch_all



# Generated at 2022-06-13 19:21:45.724323
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    import marshmallow
    class SomeClass(metaclass=dataclasses.dataclass):
        a: int
        b: int
        c: str = "Someclass"

    @dataclasses.dataclass
    class SomeDerivedClass(SomeClass):
        d: Any = marshmallow.missing

    defined_parameters = {"a": 5, "b": 7}
    extra_parameters = {"x": -5}
    full_parameters = {**defined_parameters, **extra_parameters}

    try:
        _RaiseUndefinedParameters.handle_from_dict(SomeClass,
                                                   defined_parameters)
    except UndefinedParameterError:
        raise AssertionError(
            "Exception raised even though parameters are correct")


# Generated at 2022-06-13 19:21:57.810590
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    obj = object()
    kvs = {"a": 1, "b": 2}

    # Test if nothing happens if no method _get_catch_all_field is implemented
    assert _UndefinedParameterAction.handle_to_dict(obj, kvs) == kvs

    # Test if nothing happens if no parameters are contained in the output dictionary
    assert _CatchAllUndefinedParameters.handle_to_dict(obj, kvs) == kvs

    # Test if an dict contained in the output dictionary is handled correctly
    undefined_parameters = {"a": 1, "b": 2}
    kvs = {"c": 3, "d": 4, "CATCH_ALL": undefined_parameters}
    expected_dict = {"a": 1, "b": 2, "c": 3, "d": 4,}
    assert _CatchAllUndefinedParameters

# Generated at 2022-06-13 19:22:05.825428
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    kvs = {"a": 1, "b": 2, "c": {"ca": 1}}
    expected_return = {"a": 1, "b": 2}
    returned = _CatchAllUndefinedParameters.handle_to_dict(obj=None, kvs=kvs)
    assert kvs == returned  # This operation is in-place. The original dict must be unchanged.
    assert returned == expected_return



# Generated at 2022-06-13 19:22:18.711348
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("argument")

# Generated at 2022-06-13 19:22:25.903126
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import sys
    import typing
    import dataclasses

    def _test(method_to_test,
              input_dict: dict,
              expected_dict: dict,
              expected_error=None):
        test_class = _CatchAllUndefinedParameters
        obj = dataclasses.dataclass(
            factory=True)(**test_class._get_test_class_parameters())

        init_func = method_to_test(obj)

        class TestClass:
            pass

        # noinspection PyUnusedLocal

# Generated at 2022-06-13 19:22:33.987185
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Test:

        def __init__(self, my_field: Optional[CatchAllVar] = {}):
            self._my_field = my_field

        @property
        def my_field(self) -> Optional[CatchAllVar]:
            return self._my_field

    test = Test()
    assert _UndefinedParameterAction.handle_to_dict(test,
                                                     {"field": "field"}) ==\
           {"field": "field"}
    assert _UndefinedParameterAction.handle_to_dict(test,
                                                     {"my_field": "field"}) == {}

# Generated at 2022-06-13 19:22:45.145628
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        value: str
        ignore: Optional[CatchAllVar] = dataclasses.field(default=None,
                                                          metadata={
                                                              "undefined": Undefined.INCLUDE})

    instance = TestClass._CatchAllUndefinedParameters.create_init(TestClass)(
        "self", value="a", _UNKNOWN0="b")
    assert instance.value == "a"
    assert instance.ignore == {"_UNKNOWN0": "b"}

    instance = TestClass._CatchAllUndefinedParameters.create_init(TestClass)(
        "self", value="b", ignore={"c": "d"}, _UNKNOWN0="e")
    assert instance.value == "b"

# Generated at 2022-06-13 19:22:51.392349
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import dataclasses
    import inspect

    def create_class(**kwargs):
        @dataclasses.dataclass(**kwargs)
        class TestClass:
            a: int = None
            c: Optional[CatchAll] = None

            def __init__(self, a: int, b: int, c: Optional[CatchAll] = None):
                self.a = a
                self.b = b
                self.c = c

        return TestClass


    TestClass = create_class(frozen=False)

    def assert_init_sig_is_equal(init1, init2):
        sig1 = inspect.signature(init1)
        sig2 = inspect.signature(init2)
        assert sig1 == sig2, \
            "Signatures did not match:\n" \
           

# Generated at 2022-06-13 19:22:59.656579
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from dataclasses_json.utils import CatchAllVar

    class _TestClass:
        catch_all: CatchAllVar

    test_instance = _TestClass()
    expected = {"hello": "world"}
    setattr(test_instance, "catch_all", {"hello": "world", "foo": "bar"})
    kvs_without_catch_all = {"foo": "bar"}
    dict_without_catch_all = _CatchAllUndefinedParameters \
        .handle_to_dict(test_instance, kvs_without_catch_all)
    assert dict_without_catch_all == expected



# Generated at 2022-06-13 19:23:01.601768
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    obj = object()
    result = _UndefinedParameterAction.handle_dump(obj)
    assert isinstance(result, dict)



# Generated at 2022-06-13 19:23:12.990941
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    """
    Method __RaiseUndefinedParameters.handle_from_dict
    """
    from random import Random
    random = Random(0)
    for _ in range(1000):
        num_fields_class_under_test = random.randint(1, 5)
        fields_class_under_test = [random.choice(["a", "b", "c", "d", "e",
                                                  "f", "g", "h"]) for _ in
                                   range(num_fields_class_under_test)]

        # noinspection PyTypeChecker
        class ClassUnderTest(metaclass=dataclasses.make_dataclass):
            """
            Dataclass used for testing
            """
            a = dataclasses.field(init=False)
            b = dataclasses.field(init=False)

# Generated at 2022-06-13 19:23:21.880485
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():
    @dataclasses_json.dataclass_json(undefined=Undefined.INCLUDE)  # type: ignore
    class Test:
        a: int = dataclasses.field(metadata={"default_value": 3})
        b: str
        _catch_all= dataclasses.field(default_factory=dict,
                                      metadata={
                                          "marshmallow_field":
                                              dataclasses_json.fields.CatchAll})

    t = Test(3, b="foo", c="bar")
    assert t._catch_all == {'c': 'bar'}
    assert t == Test(3, b="foo", _catch_all={'c': 'bar'})

# Generated at 2022-06-13 19:23:29.419290
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, a, _UNKNOWN0=None):
            self.a = a
            self._UNKNOWN0 = _UNKNOWN0

    obj = A(a="a", b="b")
    kvs = {'b': 'b', 'a': 'a', '_UNKNOWN0': {'b': 'b'}}
    output = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    expected = {'b': 'b', 'a': 'a'}
    assert output == expected

# Generated at 2022-06-13 19:24:02.351809
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class ClassWithKwargs:
        def __init__(self, a: int, b: int, **kwargs):
            pass

    assert isinstance(_UndefinedParameterAction.create_init(
        ClassWithKwargs)(ClassWithKwargs), ClassWithKwargs)



# Generated at 2022-06-13 19:24:16.236502
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    # Simple function with no parameters
    def f0():
        pass

    assert f0.__code__.co_argcount == 0
    assert inspect.signature(f0).parameters == {}
    assert _UndefinedParameterAction.handle_dump(f0) == {}

    # Simple function with ignored undefined parameter
    def f1(*, x: int = 1):
        pass

    assert f1.__code__.co_argcount == 0
    assert inspect.signature(f1).parameters == {"x": 1}
    assert _UndefinedParameterAction.handle_dump(f1) == {}

    # Simple function with catch-all
    def f2(*, x: int = 1, _CatchAll=CatchAll.INCLUDE):
        pass

    assert f1.__code__.co_argcount == 0


# Generated at 2022-06-13 19:24:26.395918
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass(object):
        @dataclasses.dataclass
        class TestClassInner(object):
            f1: str
            f2: bool

        f1: str
        f2: bool
        f3: TestClassInner
        f4: Optional[str] = dataclasses.field(default=None)
        f5: Optional[TestClassInner] = dataclasses.field(default=None)


# Generated at 2022-06-13 19:24:36.211479
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class MyClass:
        defined_field: str

        catch_all: CatchAll = None

    # case 1: no undefined parameters
    my_dict = {"defined_field": "defined_string"}
    defined, undefined = _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
        MyClass, my_dict)
    received_parameters = \
        _CatchAllUndefinedParameters.handle_from_dict(MyClass, my_dict)
    assert received_parameters == my_dict

    # case 2: undefined parameters. No catch-all field given
    my_dict = {"defined_field": "defined_string",
               "undefined_field1": 1,
               "undefined_field2": "foo"}
    defined, undefined = _CatchAllUndefined

# Generated at 2022-06-13 19:24:42.580955
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class TestClass:
        def __init__(self, a, **options):
            self.a = a
            self.options = options
        #test = classmethod(test)

    assert _CatchAllUndefinedParameters.handle_to_dict(obj=TestClass,
                                                       kvs={'a': 1,
                                                            'options': {}}) == {}


if __name__ == '__main__':
    raise RuntimeError()

# Generated at 2022-06-13 19:24:53.519710
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    for handle_from_dict, expected_output in [(
            _UndefinedParameterAction.handle_from_dict,
            {'name': 'test', 'age': 3}
    ), (
            _IgnoreUndefinedParameters.handle_from_dict,
            {'name': 'test', 'age': 3}
    ), (
            _RaiseUndefinedParameters.handle_from_dict,
            {'name': 'test', 'age': 3}
    )]:
        assert handle_from_dict(TestClass, {'name': 'test', 'age': 3}) == expected_output

# Generated at 2022-06-13 19:25:02.216462
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int
        c: int

    test_cases = [
        # empty dict
        (dict(), dict()),
        # empty dict with args
        (dict(), dict(a=1, b=2, c=3)),
        # non-empty dict
        (dict(a=1, b=2, c=3), dict()),
        # non-empty dict with args
        (dict(a=1, b=2, c=3), dict(a=1, b=2, c=3)),
    ]

    for kvs, args in test_cases:
        result = _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs,
                                                            **args)
        assert args == result


# Unit

# Generated at 2022-06-13 19:25:09.696194
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json._enforcer import _data_class_enforcer
    from dataclasses_json import LetterCase
    NAME = "name"
    NAME2 = "name2"
    NAME_LOWER = "name_lower"

    @dataclasses.dataclass
    class TestData(_data_class_enforcer,
                   letter_case=LetterCase.CAMEL):
        catch: CatchAll = None
        name: str = "Name"

    class TestData2(_data_class_enforcer, Undefined.INCLUDE,
                    letter_case=LetterCase.CAMEL):
        catch: CatchAll = None
        name: str = "Name"

    INPUT_1 = {"name": "something else"}
    EXPECTED_OUTPUT_1 = {NAME: {}}

    INPUT_2

# Generated at 2022-06-13 19:25:16.485613
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from collections import OrderedDict
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        a: int
        b: int
        _c: int
        other: Optional[CatchAllVar] = None

    d = OrderedDict()
    d["a"] = 1
    d["b"] = 2
    d["_c"] = 3
    d["other"] = {"x": 4}
    d["y"] = 5

    cls = MyClass(a=1, b=2, _c=3, other=dict(x=4, y=5))

    assert d == _CatchAllUndefinedParameters.handle_to_dict(cls, d)

# Generated at 2022-06-13 19:25:32.795893
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # simple, one argument, no default
    class A(object):
        def __init__(self, one):
            self.one = one


    A_orig_init = A.__init__
    A.__init__ = _IgnoreUndefinedParameters.create_init(A)
    a = A(one=1, two=2)

    assert a.one == 1
    A.__init__ = A_orig_init

    # keyword argument only
    class B(object):
        def __init__(self, *args, two: int = 3):
            self.two = two


    B.__init__ = _IgnoreUndefinedParameters.create_init(B)
    b = B(one=1)

    assert b.two == 3
    B.__init__ = _IgnoreUndefinedParameters.create_

# Generated at 2022-06-13 19:26:19.649762
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump(None) == {}



# Generated at 2022-06-13 19:26:22.169623
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    UndefinedParameterError("some error message")
    UndefinedParameterError("some error message", cause="some cause")



# Generated at 2022-06-13 19:26:29.223914
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class Dummy(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def handle_dump(self) -> Dict[Any, Any]:
            pass

    class Dummy1(Dummy):
        def handle_dump(self) -> Dict[Any, Any]:
            return {}

    class Dummy2(Dummy):
        def handle_dump(self) -> Dict[Any, Any]:
            return {"a": 3}

    obj = Dummy1()
    assert _UndefinedParameterAction.handle_dump(obj) == {}
    obj = Dummy2()
    assert _UndefinedParameterAction.handle_dump(obj) == {"a": 3}



# Generated at 2022-06-13 19:26:40.077591
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    from dataclasses import dataclass

    @dataclass
    class ExampleClass:
        a: str
        b: str
        c: str

    init = _IgnoreUndefinedParameters.create_init(ExampleClass)

    obj = ExampleClass("a", "b", "c")
    init(obj, "a", "b", "c")
    assert obj.a == "a"
    assert obj.b == "b"
    assert obj.c == "c"

    obj2 = ExampleClass("a", "b", "c")
    init(obj2, "a", "b")
    assert obj2.a == "a"
    assert obj2.b == "b"
    assert obj2.c == "c"

    obj3 = ExampleClass("a", "b", "c")

# Generated at 2022-06-13 19:26:41.779235
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("Error!")
    except UndefinedParameterError:
        pass
    else:
        assert False, "UndefinedParameterError not raised"

# Generated at 2022-06-13 19:26:43.606676
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError()
    except UndefinedParameterError:
        pass

# Generated at 2022-06-13 19:26:51.403829
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class _Dummy:
        def __init__(self, x: int, y: int, z: int = -1):
            pass

        @classmethod
        def test_create_init(cls) -> Callable:
            return _IgnoreUndefinedParameters.create_init(cls)

    _Dummy.test_create_init()(2, 2)
    _Dummy.test_create_init()(2, 2, _UndefinedParameterAction._SentinelNoDefault)
    _Dummy.test_create_init()(2, 2, z=3)
    _Dummy.test_create_init()(2, 2, 3)
    _Dummy.test_create_init()(2, 2, 3, x=17)

# Generated at 2022-06-13 19:26:57.025512
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    @dataclasses.dataclass
    class TestClass:
        a_field: int
        a_catch_all: CatchAll = dataclasses.field(default_factory=dict)

    obj = TestClass(1, {"other": "field"})
    assert _CatchAllUndefinedParameters.handle_to_dict(obj=obj, kvs={
        "a_field": 1,
        "a_catch_all": {"other": "field"}
    }) == {"a_field": 1, "other": "field"}

# Generated at 2022-06-13 19:27:06.449665
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        catch_all: CatchAll = dataclasses.field(default=None)

        def __init__(self, a: Any, b: Any, *args, c: Any = None, **kwargs):
            self.a = a
            self.b = b
            self.c = c

    test_obj = TestClass(a=1, b=2, c=3)
    orig_init = TestClass.__init__
    TestClass.__init__ = _CatchAllUndefinedParameters.create_init(TestClass)

# Generated at 2022-06-13 19:27:16.424815
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, _a: int, _b: int = None,
                     _catch_all=CatchAll):
            pass

    assert {'_a': 1, '_b': None, '_catch_all': {}} == \
           _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                          {'_a': 1})
    assert {'_a': 1, '_b': None, '_catch_all': {'c': 1}} == \
           _CatchAllUndefinedParameters.handle_from_dict(TestClass,
                                                          {'_a': 1, 'c': 1})
    assert {'_a': 1, '_b': None, '_catch_all': {'c': 1}} == \
           _CatchAll

# Generated at 2022-06-13 19:29:45.828339
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses_json.utils.testing_utils import CatchAllVar

    @dataclasses.dataclass
    class TestClass:
        x: int
        y: int
        param_catchall: Optional[CatchAllVar] = dataclasses.field(
            default_factory=dict)

    test_1_input = {"x": 1, "y": 2}
    test_1_output = {"x": 1, "y": 2, "param_catchall": {}}
    result = _CatchAllUndefinedParameters.handle_from_dict(
        TestClass, kvs=test_1_input)
    assert result == test_1_output

    test_2_input = {"x": 1, "y": 2, "z": 3}

# Generated at 2022-06-13 19:29:50.379052
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Test:
        a: int

    def get_func() -> Callable:
        def func(self, a: int, b: int, c: int):
            pass

        return func
    func = get_func()

    _UndefinedParameterAction.handle_from_dict(Test, {})
    _UndefinedParameterAction.handle_from_dict(Test, {"a": 3})
    _UndefinedParameterAction.handle_from_dict(Test, {"a": 3, "b": 4})
    _UndefinedParameterAction.handle_from_dict(Test, {"a": 3, "c": 10})
    init_signature = inspect.signature(func)
    _UndefinedParameterAction.handle_from_dict(func, {})
    _UndefinedParameterAction.handle_from_dict(func, {"a": 3})


# Generated at 2022-06-13 19:29:55.927689
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class TestDc(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    _init = _UndefinedParameterAction.create_init(TestDc)
    assert _init(TestDc(1, 2, 3), a=3, b=2, c=1)
    try:
        _init(TestDc(1, 2, 3), a=3, b=2, c=1, d=5)
        raise AssertionError("expected exception")
    except Exception as e:
        assert isinstance(e, TypeError)
        assert str(e) == "__init__() got an unexpected keyword argument 'd'"


# Generated at 2022-06-13 19:30:03.950144
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    @dataclasses.dataclass
    class A:
        foo: str
        bar: str
    a = A(foo="a.foo", bar="a.bar")
    d = _UndefinedParameterAction.handle_to_dict(a, {"foo": "A.foo",
                                                     "bar": "A.bar",
                                                     "baz": "A.baz"})
    assert (d == {'foo': 'A.foo', 'bar': 'A.bar', 'baz': 'A.baz'})



# Generated at 2022-06-13 19:30:05.218669
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    message = "This is a custom error message"
    e = UndefinedParameterError(message)
    assert e.message == message
    assert e.field_names == []
    assert e.fields == {}

# Generated at 2022-06-13 19:30:15.473029
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class ClassA:
        a: int
        b: float
        c: str
        d: int

    a = ClassA(1, 0.5, "test", d=10)

    assert len(inspect.signature(ClassA.__init__).parameters) == 3
    assert a == ClassA(1, d=10)

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class ClassB:
        a: int
        b: float
        c: str
        d: int = 2

    b = ClassB(1, 0.5, "test", d=10)

    assert len(inspect.signature(ClassB.__init__).parameters)

# Generated at 2022-06-13 19:30:18.823046
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError('error')
    except UndefinedParameterError as e:
        assert e.args[0] == 'error'