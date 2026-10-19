

# Generated at 2022-06-13 19:20:51.888093
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class Example:
        def __init__(self, a: int, b: int = 0):
            pass

    assert _UndefinedParameterAction.handle_from_dict(cls=Example,
                                                      kvs={"a": 1,
                                                           "b": 0}) == {"a": 1,
                                                                       "b": 0}
    assert _UndefinedParameterAction.handle_from_dict(cls=Example,
                                                      kvs={"a": 1,
                                                           "b": 2}) == {"a": 1,
                                                                       "b": 2}
    assert _UndefinedParameterAction.handle_from_dict(cls=Example,
                                                      kvs={"a": 1}) == {"a": 1,
                                                                        "b": 0}



# Generated at 2022-06-13 19:20:57.144601
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    original_init = __IgnoreUndefinedParametersInit
    num_params = len(inspect.signature(original_init).parameters)
    if num_params <= 1:
        return
    num_args_takeable = num_params - 1  # don't count self

    @dataclasses.dataclass(undefined=IgnoreUndefinedParameters)
    class A:
        def __init__(self, *args, **kwargs):
            pass

    @dataclasses.dataclass(undefined=IgnoreUndefinedParameters)
    class B:
        def __init__(self, *args, **kwargs):
            pass

    a = A(1, *range(num_args_takeable))

    @dataclasses.dataclass(undefined=IgnoreUndefinedParameters)
    class C:
        c

# Generated at 2022-06-13 19:21:04.529058
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    from dataclasses import dataclass

    @dataclass
    class Example:
        a: str
        b: str = 'b'

    params = {
        'a': 'a'
    }

    obj = Example(**params)

    dumped_kvs_action1 = _UndefinedParameterAction.handle_dump(obj)
    assert dumped_kvs_action1 == {}

    dumped_kvs_action2 = _RaiseUndefinedParameters.handle_dump(obj)
    assert dumped_kvs_action2 == {}

    dumped_kvs_action3 = _IgnoreUndefinedParameters.handle_dump(obj)
    assert dumped_kvs_action3 == {}

    dumped_kvs_action4 = _CatchAllUndefinedParameters.handle_dump(obj)
    assert dumped_kvs_action4 == {}

# Generated at 2022-06-13 19:21:14.051789
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class TestClass:
        a: int
        undefined_parameter: int

        def __init__(self, a, undefined_parameter):
            self.a = a
            self.undefined_parameter = undefined_parameter

    obj_to_test = TestClass(1, 2)
    init_method = _IgnoreUndefinedParameters.create_init(obj=obj_to_test)
    expected_a = 1
    expected_undefined_parameter = None
    init_method(obj_to_test, *(1,), undefined_parameter=2,
                undefined_parameter_2=3)
    assert expected_a == obj_to_test.a
    assert expected_undefined_parameter == obj_to_test.undefined_parameter


# Unit test

# Generated at 2022-06-13 19:21:22.985899
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        pass

    TestClass.__init__ = lambda self: None
    TestClass.__init__.__signature__ = inspect.Signature([])
    TestClass.__init__.__annotations__ = {}

    class_fields = fields(TestClass)
    known, _ = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=TestClass, kvs={})
    assert known == {}

    kvs = {"a": "b"}
    _, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=TestClass, kvs=kvs)
    assert unknown == {"a": "b"}

# Generated at 2022-06-13 19:21:36.563382
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class Foo:
        def __init__(self, a: int = 0, b: int = 1,
                     c: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c

    foo = Foo()
    expected = {'a': 0, 'b': 1}
    result = _UndefinedParameterAction.handle_to_dict(foo, {'a': 0, 'b': 1})
    assert result == expected

    foo = Foo(a=52, b=4, c={'foo': 1, 'bar': 'frob'})
    expected = {'a': 52, 'b': 4, 'foo': 1, 'bar': 'frob'}

# Generated at 2022-06-13 19:21:40.509483
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError(errs=[
            dict(field="a", message="b"),
            dict(field="c", message="d")])
    except ValidationError as err:
        assert isinstance(err, UndefinedParameterError)
        assert err.messages == dict(a="b", c="d")

# Generated at 2022-06-13 19:21:47.806511
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class Foo:
        def __init__(self, catch_all: Optional[CatchAllVar] = None):
            self.catch_all = catch_all

    kvs = {"hello": "world", "foo": "bar"}
    foo = Foo(catch_all=kvs)
    assert _CatchAllUndefinedParameters.handle_to_dict(foo, kvs) == {"hello": "world"}

# Generated at 2022-06-13 19:21:51.609895
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    # Arrange
    class TestClass:
        def __init__(self, *args):
            print(args)

    # Act
    init = _IgnoreUndefinedParameters.create_init(TestClass)
    init(TestClass)

# Generated at 2022-06-13 19:22:01.575627
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class SimpleClass:
        field1: str
        field2: str

    @dataclass(undefined=Undefined.RAISE)
    class SimpleClassA:
        field1: str
        field2: str

    @dataclass(undefined=Undefined.RAISE)
    class SimpleClassB:
        field1: str
        field2: str

    @dataclass(undefined=Undefined.RAISE)
    class SimpleClassC:
        field1: str
        field2: str
        catch_all: CatchAll = None

    @dataclass(undefined=Undefined.RAISE)
    class SimpleClassD:
        field1: str
        field2: str
        catch_all: CatchAll = None


# Generated at 2022-06-13 19:22:20.121469
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    """
    Tests that the _IgnoreUndefinedParameters._create_init method returns
    a function that discards unknown parameters
    """

    @dataclasses.dataclass(undefined=Undefined.EXCLUDE)
    class Foo:
        foo: int
        bar: int = dataclasses.field(default=0)

        def __init__(self, foo: int, bar: int = 0) -> None:
            self.foo = foo
            self.bar = bar

    for i in range(3):
        for j in range(3):
            x = Foo(foo=i, bar=j, baz=3)
            assert x.foo == i
            assert x.bar == j

# Generated at 2022-06-13 19:22:26.742283
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a: int, b: float = 0.0, catch_all: CatchAll = None):
            self.a = a
            self.b = b
            self.catch_all = catch_all

    kvs = {'a': 1, 'b': 1.0, 'c': 1.0}
    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {'a': 1, 'b': 1.0, 'catch_all': {'c': 1.0}}

    kvs = {'a': 1, 'c': 1.0}
    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, kvs)

# Generated at 2022-06-13 19:22:30.042086
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump({}) == {}
    # Test that the method does not mutate the object
    assert _UndefinedParameterAction.handle_dump({"a": 3}) == {}



# Generated at 2022-06-13 19:22:42.175881
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    def _test_case(cls, expected_output):
        init = _CatchAllUndefinedParameters.create_init(cls)
        try:
            init(cls=cls, *expected_output)
        except UndefinedParameterError:
            # Expected
            return

        raise RuntimeError("Expected UndefinedParameterError")

    @dataclasses.dataclass
    class _ClassA:
        a: str
        b: int

    init = _CatchAllUndefinedParameters.create_init(_ClassA)
    init(_ClassA, "", 1)
    with pytest.raises(UndefinedParameterError):
        init(_ClassA, "", 1, undefined="")

    @dataclasses.dataclass
    class _ClassB:
        a: str
        b: int

# Generated at 2022-06-13 19:22:50.254600
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    # CatchAll field is called 'other_fields' and recevied parameters are:
    # 'a', 'b', 'c', and 'other_fields'
    class _Class:
        def __init__(self, a, b, c, other_fields: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.c = c
            self.other_fields = other_fields if other_fields is not None else {}

    kvs = {"a": 1, "b": "world", "c": 'test', "other_fields": {"test": 3}}
    expected = {"a": 1, "b": "world", "c": "test", "test": 3}

    assert _CatchAllUndefinedParameters.handle_to_dict(_Class, kvs) == expected


# Unit

# Generated at 2022-06-13 19:23:01.013822
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from typing import Type
    
    def _test_case(cls: Type, kvs: Dict, expected_kvs: Dict):
        from dataclasses import dataclass, field
        from dataclasses_json.undefined import _CatchAllUndefinedParameters
        from dataclasses_json.undefined import CatchAllVar

        @dataclass
        class Test:
            def __init__(self, *args, **kws) -> None:
                pass

        real_kvs = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
        assert real_kvs == expected_kvs

    def test_no_catch_all_field():
        @dataclass
        class Test:
            b: int = 1
            a: int = field(init=False)


# Generated at 2022-06-13 19:23:05.394297
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class Test:
        def __init__(self, a: int, b: int, **kwargs: Any):
            pass

    test_object = Test(1, 2, c=3)
    known, unknown = _IgnoreUndefinedParameters._separate_defined_undefined_kvs(
        test_object, {'a': 1, 'b': 2, 'c': 3})
    assert known == {'a': 1, 'b': 2}
    assert unknown == {'c': 3}


# Generated at 2022-06-13 19:23:12.306811
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    @dataclasses.dataclass
    class Test:
        a: str
        b: int

    a, b = "a", 1
    c, d = "c", "d"
    test = Test(a, b, c=c, d=d)

    assert test.a == a
    assert test.c == c
    assert test.b == b
    assert test.d == d

# Generated at 2022-06-13 19:23:17.911771
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    @dataclasses.dataclass
    class TestClass(_UndefinedParameterAction):
        pass

    def check(cls, kvs):
        assert cls._UndefinedParameterAction.handle_dump(cls, kvs) == kvs

    check(TestClass, {})
    check(TestClass, {"a": 1})
    check(TestClass, {"a": 2, "b": 3})

# Generated at 2022-06-13 19:23:25.197303
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    from dataclasses_json.undefined_parameter_policy import \
        _RaiseUndefinedParameters

    @dataclasses.dataclass
    class TestClass:
        a: int
        b: str

    input_dict = {'a': 1,
                  'b': 'b',
                  'c': 'c'}
    expected_output_dict = {
        'a': 1,
        'b': 'b'}
    try:
        output_dict = _RaiseUndefinedParameters \
            .handle_from_dict(TestClass, input_dict)
    except UndefinedParameterError:
        output_dict = None

    assert output_dict is None



# Generated at 2022-06-13 19:24:05.813762
# Unit test for method handle_from_dict of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_handle_from_dict():
    class A:
        def __init__(self, a: int, b=2, c=3):
            pass

    class B(A):
        def __init__(self, a: int, b=2, c=3):
            super().__init__(a, b, c)

    class C(A):
        def __init__(self, a: int, b=2, c=3, *args, **kwargs):
            super().__init__(a, b, c)

    class D(A):
        def __init__(self, a: int, b=2, c=3, d=42):
            super().__init__(a, b, c)

    class E(object):
        def __init__(self, a: int = 1):
            pass


# Generated at 2022-06-13 19:24:17.318987
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():
    class A:
        def __init__(self, a, b=1):
            self.a = a
            self.b = b

    a = A(1)
    r = _UndefinedParameterAction.handle_to_dict(a, kvs={"a": "1", "b": 1})
    assert r["a"] == 1

    a = A(2, 3)
    r = _UndefinedParameterAction.handle_to_dict(a, kvs={"a": "2", "b": 3})
    assert r["a"] == 2
    assert r["b"] == 3

    a = A(2, 3)
    r = _UndefinedParameterAction.handle_to_dict(a, kvs={"a": "3", "b": 3})
    assert r["a"] == 3

# Generated at 2022-06-13 19:24:19.196123
# Unit test for constructor of class UndefinedParameterError
def test_UndefinedParameterError():
    try:
        raise UndefinedParameterError("test message")
    except UndefinedParameterError:
        pass

# Generated at 2022-06-13 19:24:28.626672
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    _UndefinedParameterAction.handle_from_dict(MyClass, {})
    _UndefinedParameterAction.handle_from_dict(MyClass, {
        "foo": 42,
        "baz": "hello"
    })
    _UndefinedParameterAction.handle_from_dict(MyClass, {
        "bar": "hello",
        "baz": "hello",
        "foo": 42,
        "qux": "hello"
    })
    _UndefinedParameterAction.handle_from_dict(MyClass, {
        "foo": 42,
    })
    _UndefinedParameterAction.handle_from_dict(MyClass, {
        "foo": 42,
        "bar": "hello",
        "unknown": 42
    })

# Generated at 2022-06-13 19:24:38.184510
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    class Clazz:
        def __init__(self, hello, world, *, a=1, b=2, **catchall):
            self.hello = hello
            self.world = world
            self.a = a
            self.b = b
            self.catchall = catchall

    def test_case(input_kvs: Dict[str, Any], expected_output: Dict[str, Any]):
        output = _CatchAllUndefinedParameters.handle_from_dict(Clazz, input_kvs)
        assert expected_output == output, \
            f"{output} != {expected_output}"

    test_case({"hello": 2}, {"hello": 2, "world": None, "a": 1, "b": 2})

# Generated at 2022-06-13 19:24:44.935935
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    input_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'catch_all': {
            'd': 4,
            'e': 5
        }
    }
    expected = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    assert _CatchAllUndefinedParameters.handle_to_dict(
        None,
        input_dict
    ) == expected

# Generated at 2022-06-13 19:24:54.457226
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    import dataclasses

    @dataclasses.dataclass
    class C:
        a: int
        b: int
        c: str = "c"

        def __init__(self, a: int, b: int, c: str = "c"):
            pass

    @dataclasses.dataclass
    class D:
        a: int
        b: int
        d: int = 42
        c: str = "c"

        def __init__(self, a: int, b: int, c: str = "c", d: int = 42):
            pass

    _IgnoreUndefinedParameters.create_init(C)()
    _IgnoreUndefinedParameters.create_init(D)()



# Generated at 2022-06-13 19:25:02.028180
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    import datetime
    from dataclasses_json.core import todict
    from typing import List

    @dataclasses.dataclass
    class Foo:
        normal_field: int
        catch_all: CatchAll

    @dataclasses.dataclass
    class DictTest:
        normal_field: int
        catch_all: CatchAll
        __dataclasses_json__ = {
            "unknown": Undefined.INCLUDE
        }

    @dataclasses.dataclass
    class ListTest:
        normal_field: int
        catch_all: CatchAll
        __dataclasses_json__ = {
            "unknown": Undefined.INCLUDE
        }

    @dataclasses.dataclass
    class DateTimeTest:
        normal_field: datetime.datetime
        catch

# Generated at 2022-06-13 19:25:06.638136
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Test(_IgnoreUndefinedParameters):

        def __init__(self, a: int, b: int, c: int):
            pass

    orig_func = Test.__init__
    Test.__init__ = _IgnoreUndefinedParameters.create_init(Test)
    test = Test(1, 2, 3)
    assert test
    Test.__init__ = orig_func



# Generated at 2022-06-13 19:25:13.823863
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    from .utils import CatchAllVar


    @dataclasses.dataclass
    class A(object):
        x: str
        y: int
        z: Optional[CatchAllVar]


    a = A("foo", 42, {"a": 3, "b": "hello"})
    kvs = {"x": "a", "y": 1, "z": "b"}
    assert _CatchAllUndefinedParameters.handle_to_dict(a, kvs) == {
        "x": "a", "y": 1,
        "a": 3, "b": "hello"}



# Generated at 2022-06-13 19:26:09.315456
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    class _UndefinedParameterActionImpl(_UndefinedParameterAction):
        pass

    d = _UndefinedParameterActionImpl.handle_dump(obj=None)
    assert d == {}

# Generated at 2022-06-13 19:26:14.953208
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():
    class A:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b
            self.__dict__["c"] = "foo"
            self.__dict__["d"] = "bar"
    a = A(1, "b")
    kvs = _CatchAllUndefinedParameters.handle_to_dict(A, a.__dict__)
    assert(kvs == {"a":1,"b":"b","c":"foo","d":"bar"})

# Generated at 2022-06-13 19:26:20.261693
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    ignored_state = \
        _IgnoreUndefinedParameters.create_init(_UndefinedParameterAction)()
    caught_all_state = _CatchAllUndefinedParameters.create_init(
        _UndefinedParameterAction)()
    assert str(ignored_state) == "UndefinedParameterAction()"
    assert str(caught_all_state) == "UndefinedParameterAction()"

# Generated at 2022-06-13 19:26:29.167528
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class Foo:
        a: int
        b: int
        c: int

        @classmethod
        def handle_undefined(cls, undefined):
            return {**undefined,
                    "c": 99}

    @dataclasses.dataclass
    class Foo2:
        d: int
        e: int

    @dataclasses.dataclass
    class Foo3:
        d: int
        e: int

    @dataclasses.dataclass
    class Bar:
        a: int
        b: int
        foo: Foo = dataclasses.field(metadata=dict(
            mapper={"undefined": "EXCLUDE"}))

# Generated at 2022-06-13 19:26:40.048158
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    """
    Test that _CatchAllUndefinedParameters.create_init returns the correct
    init function.
    """
    from test.test_utils import TestDataclassCatchAll
    init = _CatchAllUndefinedParameters.create_init(TestDataclassCatchAll)
    init_signature = inspect.signature(init)

# Generated at 2022-06-13 19:26:47.199911
# Unit test for method handle_from_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_from_dict():
    class TestClass:
        def __init__(self, field_a, field_b="Some default"):
            self.field_a = field_a
            self.field_b = field_b

    kvs = dict(field_a="A", field_c="B")

    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(
        cls=TestClass, kvs=kvs)
    assert dict(field_a="A") == known
    assert dict(field_c="B") == unknown

# Generated at 2022-06-13 19:26:53.835589
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():
    import inspect

    @dataclasses.dataclass
    class Foo:
        x: int
        y: str
        z: float
        catch: CatchAllVar = dataclasses.field(
            default=dataclasses.MISSING,
            metadata={'marshmallow_field': CatchAllVar(Any)}
        )

        undef: Undefined.INCLUDE

    f1 = Foo(1, '2', 3.3)
    f2 = Foo(1, '2', 3.3, a='A', b='B')
    f3 = Foo(1, '2', 3.3, a='A', b='B', catch={'c': 'C'})
    f4 = Foo(1, '2', 3.3, a='A', b='B', c='C', d='D')
    f

# Generated at 2022-06-13 19:26:57.099924
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():
    class Test:
        def __init__(self, a):
            self.a = a


    obj = Test(1)
    init = _IgnoreUndefinedParameters.create_init(obj)
    obj = init(1)
    assert obj.a == 1
    obj = init(1, a=2)
    assert obj.a == 1

# Generated at 2022-06-13 19:27:06.544499
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    @dataclasses.dataclass
    class DummyClass:
        x: int = 1
        _UNDEFINED: Optional[CatchAllVar] = None

    assert _CatchAllUndefinedParameters.handle_from_dict(
        DummyClass, dict(x=2, y=3)) == dict(x=2, _UNDEFINED=dict(y=3))
    assert _CatchAllUndefinedParameters.handle_from_dict(
        DummyClass, dict(x=2, _UNDEFINED=dict(y=3))) == dict(x=2,
                                                             _UNDEFINED=dict(
                                                                 y=3))

# Generated at 2022-06-13 19:27:07.981627
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump():
    assert _UndefinedParameterAction.handle_dump('my_obj') == {}

# Generated at 2022-06-13 19:29:28.638409
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        a: str = "a"
        b: str = "b"
        c: Optional[CatchAllVar] = None

    parameters = {"a": "a", "b": "b"}
    result = _CatchAllUndefinedParameters.handle_from_dict(MyClass, parameters)
    assert result == {"a": "a", "b": "b", "c": {}}

    parameters = {"a": "a", "b": "b", "c": {}}
    result = _CatchAllUndefinedParameters.handle_from_dict(MyClass, parameters)
    assert result == {"a": "a", "b": "b", "c": {}}


# Generated at 2022-06-13 19:29:42.510384
# Unit test for method handle_from_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_from_dict():
    """
    Tests if _CatchAllUndefinedParameters.handle_from_dict works as expected
    """

    # Not matter in which order the fields are defined
    @dataclasses.dataclass(
        init=False)
    class TestDataclass:
        catchall: Optional[CatchAllVar]
        a: int
        b: int

        def __init__(self, a: int, b: int, catchall: Optional[CatchAllVar]):
            self.a = a
            self.b = b
            self.catchall = catchall

    # No undefined parameters, field catchall is present
    expected_output = {
        "a": 1,
        "b": 2,
        "catchall": {}

    }

# Generated at 2022-06-13 19:29:48.823943
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    """
    Unit test for method create_init of class _UndefinedParameterAction
    """
    @dataclasses.dataclass()
    class TestClass:
        a: int = 0
        b: int = 0
        _undefined: CatchAll = None

        def __init__(self, a: int, b: int=0, **kwargs):  # type: ignore
            self.c = 1


    init = _UndefinedParameterAction.create_init(TestClass)
    obj = init(None, 0, 1, c=1)
    assert isinstance(obj, TestClass)

# Generated at 2022-06-13 19:29:59.320778
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    class TestClass:

        def __init__(self, param1: str, catch_all: CatchAll = None):
            self.param1 = param1
            self.set_catch_all(catch_all)

        def set_catch_all(self, catch_all):
            if catch_all is None:
                catch_all = {}
            self.catch_all = catch_all

    init_catch_all = _CatchAllUndefinedParameters.create_init(TestClass)
    init_ignore = _IgnoreUndefinedParameters.create_init(TestClass)
    init_raise = _RaiseUndefinedParameters.create_init(TestClass)


# Generated at 2022-06-13 19:30:08.707666
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    from dataclasses import dataclass
    from typing import List
    from dataclasses_json.api import Config

    @dataclass
    class TestClass1:
        a: str
        b: int
        c: str
        d: int
        e: float = dataclasses.field(default=1.0)

        def __init__(self, a: str, b: int, e: float, **kwargs):
            self.a = a
            self.b = b
            self.e = e


# Generated at 2022-06-13 19:30:17.171705
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():
    import dataclasses
    import dataclasses_json

    @dataclasses.dataclass
    class TestClass:
        a: int = 0
        b: int = 0
        ignore_kwargs: bool = dataclasses_json.config.undefined.EXCLUDE

        def __init__(self, a, b):
            self.a = a
            self.b = b

    tc = TestClass(1, 2)
    assert TestClass.__init__ != tc.__init__
    assert TestClass.__init__(tc, 3) != tc.__init__(3)

