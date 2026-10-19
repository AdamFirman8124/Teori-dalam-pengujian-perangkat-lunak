

# Generated at 2022-06-13 19:20:52.844002
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int

    schema = SchemaF[A]()
    a = A(a=1)
    print(schema.dump(a))


# Generated at 2022-06-13 19:20:55.268953
# Unit test for constructor of class _IsoField
def test__IsoField():
    iso_field = _IsoField()
    assert iso_field.__class__.__name__ == "IsoField"


# Generated at 2022-06-13 19:21:03.670235
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from typing import Mapping, Dict, List, Tuple, Callable, Any, Optional
    from dataclasses_json import dataclass_json
    from marshmallow import fields, Schema

    @dataclass_json
    @dataclass
    class A:
        a: int = 1

    @dataclass_json
    @dataclass
    class B:
        a: Optional[A] = None

    @dataclass_json
    @dataclass
    class Test:
        b: B = field(metadata={'dataclasses_json': {"mm_field": fields.String()}})

    # Unit test for function schema
    assert schema(Test, dataclasses_json.DataClassJsonMixin, False) == {'b': fields.String()}

# Generated at 2022-06-13 19:21:17.348717
# Unit test for function schema

# Generated at 2022-06-13 19:21:21.500976
# Unit test for function build_schema
def test_build_schema():
    data = [1, 2, 3]
    schema = build_schema(list, type(None), False, False)
    dumped = schema().dump(data, many=True)
    loaded = schema().loads(dumped)
    assert loaded == data

# Generated at 2022-06-13 19:21:25.133687
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    ts_instance = datetime(2012, 12, 12, 12, 12, 12, 122000)
    assert _TimestampField()._serialize(ts_instance,
                                        "attr",
                                        "obj",
                                        format="%Y-%m-%dT%H:%M:%S.%f%z") == 1355049332.122
    assert _TimestampField()._deserialize(ts_instance.timestamp(),
                                          "attr",
                                          "obj") == ts_instance


# Generated at 2022-06-13 19:21:37.997223
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Msg:
        hello: str = 'world'
        foo: typing.Optional[int] = None
    @dataclass
    class Foo:
        msg: Msg
        optional_msg: typing.Optional[Msg] = None
    @dataclass
    class Bar:
        foo: typing.List[Foo]
        optional_foo: typing.Optional[typing.List[Foo]] = None
    schema = build_schema(Bar, JsonMixin, False, False)

    input = Bar(foo=[Foo(msg=Msg())])
    serialized = schema(strict=True).dump(input)

# Generated at 2022-06-13 19:21:45.277695
# Unit test for function build_type
def test_build_type():
    # Fixture
    class TestClass:
        def __init__(self, a: str, b: int, c: typing.List[int]):
            self.a = a
            self.b = b
            self.c = c

    # Test
    mm_field_a = build_type(str, {}, None,
                            dc_fields(TestClass)[0], TestClass)
    mm_field_b = build_type(int, {}, None,
                            dc_fields(TestClass)[1], TestClass)
    mm_field_c = build_type(typing.List[int], {}, None,
                            dc_fields(TestClass)[2], TestClass)

    assert isinstance(mm_field_a(), fields.Str)
    assert isinstance(mm_field_b(), fields.Int)
   

# Generated at 2022-06-13 19:21:48.136997
# Unit test for constructor of class _TimestampField
def test__TimestampField(): 
    assert _TimestampField() != None

TIMESTAMP_FIELD = _TimestampField()


# Generated at 2022-06-13 19:21:51.504594
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()


if sys.version_info.minor > 6:
    _datetime_field_class = _IsoField
else:
    _datetime_field_class = _TimestampField



# Generated at 2022-06-13 19:22:11.278282
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class Aa:
        a: str


    @dataclass
    class B:
        b: int


    @dataclass
    class C:
        c: float


    @dataclass
    class D:
        d: bool


    @dataclass
    class E(Aa):
        e: int


    @dataclass
    class F:
        f: typing.List[str]


    @dataclass
    class G:
        g: typing.List[int]


    @dataclass
    class H:
        h: typing.List[float]


    @dataclass
    class I:
        i: typing.List[bool]



# Generated at 2022-06-13 19:22:12.430327
# Unit test for constructor of class _TimestampField
def test__TimestampField():
  assert isinstance(_TimestampField(), fields.Field)


# Generated at 2022-06-13 19:22:29.035857
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class MyData:
        an_int: int = 1
        a_float: float = 1.1
        a_string: str = "my string"
        a_bool: bool = True
        a_dict: typing.Dict[str, int] = dataclasses.field(
            default_factory=lambda: {'a': 1})
        a_list: typing.List[int] = dataclasses.field(default_factory=lambda: [
            1, 2, 3])
        an_optional_float: typing.Optional[float] = None
        a_tuple: typing.Tuple[int, str] = (1, "a")
        a_nested: typing.Any = dataclasses.field(
            default_factory=lambda: MyData())
        an_enum: My

# Generated at 2022-06-13 19:22:41.154130
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import typing

    import marshmallow
    import marshmallow.fields
    import marshmallow_dataclass

    class SampleSchema(marshmallow_dataclass.Schema):
        foo: str = marshmallow.fields.String()

    s = SampleSchema()
    dumped_obj = s.dump(SampleSchema(foo="bar"))
    assert isinstance(dumped_obj, dict)
    assert "foo" in dumped_obj
    assert dumped_obj["foo"] == "bar"

    dumped_list_of_obj = s.dump([SampleSchema(foo="bar"), SampleSchema(foo="baz")], many=True)
    assert isinstance(dumped_list_of_obj, typing.List)
    assert len(dumped_list_of_obj) == 2

# Generated at 2022-06-13 19:22:44.910962
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import List
    from marshmallow import Schema, fields
    from marshmallow_dataclass import dataclass
    @dataclass
    class Foo:
        name = 'Foo'
    FooSchema = SchemaF[Foo]({'name': fields.Str()})
    assert FooSchema.dumps(Foo()) == '{"name": "Foo"}'
    assert FooSchema.dumps(List[Foo([])]) == '[{"name": "Foo"}]'


# Generated at 2022-06-13 19:22:54.142482
# Unit test for function build_type
def test_build_type():
    import marshmallow
    @dataclass
    class TestClass:
        pass
    class TestClass2():
        pass
    class TypeMappingTest:
        pass
    class EnumTest(Enum):
        TEST_VAL1 = "test"
        TEST_VAL2 = "test2"
    class TestSchema(Schema):
        pass
    test_dict = {'a':1, 'b':2}
    test_tuple = (1,2,3)
    custom_type = typing.NewType("CustomType", TestClass)
    custom_nonetype = typing.NewType("CustomType", None)

    type_schema = build_type(TestClass, {}, None, None, TestClass)
    assert isinstance(type_schema, marshmallow.fields.Nested)

# Generated at 2022-06-13 19:22:56.729308
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    field.deserialize(value='2020-01-01T00:00:00')



# Generated at 2022-06-13 19:22:59.657355
# Unit test for constructor of class _IsoField
def test__IsoField():
    try:
        _IsoField()._deserialize("2020-06-05T23:56:50.146426")
    except:
        assert False
    assert True
test__IsoField()


# Generated at 2022-06-13 19:23:09.519448
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    import marshmallow.fields as f

    schema = build_schema(cls, None, True, False)
    assert issubclass(schema, Schema)
    assert len(schema.__fields__) == len(dc_fields(cls))
    assert schema.__dict__["make_dataclass_schema_test"].__name__ == "make_dataclass_schema_test"

    # Meta
    assert issubclass(schema.Meta, type("", (), {}))
    assert schema.Meta.fields == (field.name for field in dc_fields(cls))
    assert len(schema.Meta.fields) == len(dc_fields(cls))
    assert schema.Meta.__name__ == "Meta"

    # make_instance has @post_

# Generated at 2022-06-13 19:23:20.121693
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    @dataclasses.dataclass
    class Point:
        x: float = dataclasses.field(metadata={'mm': {'required': False}})
        y: float = dataclasses.field(metadata={'mm': {'required': False}})

    # type: typing.List[Point]
    points = [Point(x=1, y=2)]
    # type: Point
    point = Point(x=1, y=2)
    # type: typing.Union[typing.List[Point], Point]
    point_or_points = [Point(x=1, y=2)]
    # type: typing.Union[typing.List[Point], Point]
    point_or_points = Point(x=1, y=2)
    # type: typing.List[T

# Generated at 2022-06-13 19:23:42.785019
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class T(typing.NamedTuple):
        x: int

    class SchemaF_test(SchemaF[T]):
        x = fields.Int()

    s = SchemaF_test()
    a = s.load({'x': 1})
    assert isinstance(a, T)



# Generated at 2022-06-13 19:23:50.010618
# Unit test for function build_schema
def test_build_schema():
    """
    Schema is the main class of the module. It is used to serialize and deserialize dataclass objects.
    The build_schema function is called every time a dataclass object is defined.
    :return: None
    """

    class Mixin:
        pass

    # Test case: test build_schema with dictionary
    @dataclass_json
    @dataclass
    class TestDict:
        d: dict

    # Expected
    assert not (TestDict.schema().Meta.fields == ('d',))

    # Test case: test build_schema with string
    @dataclass_json
    @dataclass
    class TestString:
        str: str

    # Expected
    assert TestString.schema().Meta.fields == ('str',)

    # Test case: test build

# Generated at 2022-06-13 19:23:51.128498
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    field.required = False


# Generated at 2022-06-13 19:23:53.131261
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    def _check(obj: A, many: bool) -> TOneOrMultiEncoded:
        return SchemaF[A]().dumps(obj, many)



# Generated at 2022-06-13 19:24:04.933480
# Unit test for function schema
def test_schema():
    class Test:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    from dataclasses_json import dataclass_json, mm_field

    @dataclass_json
    @dataclass
    class Test1:
        name: str
        age: int = mm_field(default=10)
        d: datetime = mm_field(mm_field=_TimestampField)
        u: UUID = mm_field(mm_field=fields.UUID())

    t = Test1('name', 20, datetime.now(), UUID('00000000-0000-0000-0000-000000000000'))
    s = Test1.schema().dump(t)
    assert s.get('d') is not None
    assert s.get('u') is not None

   

# Generated at 2022-06-13 19:24:17.095087
# Unit test for function schema
def test_schema():
    import types
    import inspect
    import dataclasses_json
    import decimal
    @dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
    class A:
        a0: str = "a0"
        a1: typing.Tuple[str, str] = ("a11", "a12")
        a2: typing.List[str] = ["a2", "a3"]
        a3: typing.Dict = {"a3": "a3"}
        a4: typing.MutableMapping = {"a4": "a4"}
        a5: datetime = datetime.now()
        a6: datetime.time = datetime.now().time()
        a7: decimal.Decimal = decimal.Decimal("123456.789")


# Generated at 2022-06-13 19:24:27.093674
# Unit test for function schema
def test_schema():
    import pytest
    from dataclasses_json import dataclass_json, mm_field


    @dataclass_json
    class Foo:
        x: int
        y: str

        @mm_field(fields.Str())
        def z(self) -> str:
            return str(self.x)


    schema = schema(Foo, None, True)
    assert isinstance(schema['x'], fields.Int)
    assert isinstance(schema['y'], fields.Str)
    assert isinstance(schema['z'], fields.Str)


    @dataclass_json
    class Bar:
        f: typing.Optional[Foo]


    schema = schema(Bar, None, True)
    assert isinstance(schema['f'], fields.Nested)

# Generated at 2022-06-13 19:24:36.876090
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    if sys.version_info < (3, 7) or sys.version_info >= (3, 9):
        return
    import marshmallow.utils
    import marshmallow.exceptions

    class Foo:
        pass

    class FooSchema(SchemaF[Foo]):
        bar = fields.Int()

    class FooListSchema(SchemaF[typing.List[Foo]]):
        bar = fields.List(fields.Int())

    @_handle_undefined_parameters_safe
    def test(obj) -> typing.List[Foo]:
        return [Foo()]

    test(FooSchema.dumps(Foo()))
    test(FooSchema().dumps(Foo()))

    test(FooListSchema.dumps([Foo()]))

# Generated at 2022-06-13 19:24:46.709727
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from typing import List, Union

    from dataclasses_json.api import from_dict, from_json

    @dataclass
    class A:
        a: List[int]
        b: int = 0
        c: str = 'test'

    s = build_schema(A,None,False)
    x = A([1, 2, 3], c='test')
    d = s().dump(x)
    print(d)
    assert d=={'a': [1, 2, 3], 'b': 0, 'c': 'test'}
    x2 = s().loads(d)
    print(s().load(d))
    assert x2 == {'a': [1, 2, 3], 'b': 0, 'c': 'test'}


# Unit

# Generated at 2022-06-13 19:24:49.089781
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    tsf = _TimestampField()
    assert isinstance(tsf, fields._UnicodeField) is True


# Generated at 2022-06-13 19:25:14.390972
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import marshmallow as ma

    class MySchema(SchemaF[int]):
        x = ma.fields.Int()

    def f(xs:TOneOrMultiEncoded):
        return MySchema().loads(xs)

    f([{'x': 1}])
    xs = [1]  # type: TOneOrMultiEncoded
    f(xs)

# Generated at 2022-06-13 19:25:21.069483
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import marshmallow
    import marshmallow_enum
    import marshmallow.exceptions
    import marshmallow_dataclass
    class _EnumField(marshmallow_enum.EnumField):
        __qualname__ = '_EnumField'
        pass
    if sys.version_info < (3, 7):
        _MISSING = marshmallow_dataclass._MISSING  # type: ignore
        def _is_dataclass(obj):  # type: ignore
            return marshmallow_dataclass._is_dataclass(obj)

# Generated at 2022-06-13 19:25:37.023638
# Unit test for function schema
def test_schema():
    import marshmallow
    assert marshmallow.fields.Dict == type(schema({}, None, False)['d'])
    assert marshmallow.fields.UUID == type(schema({}, None, False)['u'])
    assert marshmallow.fields.Int == type(schema({}, None, False)['i'])
    assert marshmallow.fields.List == type(schema({}, None, False)['l'])
    assert marshmallow.fields.Tuple == type(schema({}, None, False)['c'])
    assert marshmallow.fields.Field == type(schema({}, None, False)['f'])
    assert marshmallow.fields.Field == type(schema({}, None, False)['C'])
    assert marshmallow.fields.Raw == type(schema({}, None, False)['A'])

# Generated at 2022-06-13 19:25:48.430170
# Unit test for function build_schema
def test_build_schema():
  from dataclasses import dataclass
  from dataclasses_json.api import DataClassJsonMixin
  from unittest import TestCase
  from marshmallow import fields as mm_fields, Schema as mm_Schema
  from marshmallow_annotations.ext.marshmallow.fields import EnumField
  import marshmallow_annotations.ext.marshmallow as mm
  import marshmallow as marshmallow_schemas
  import marshmallow_annotations.ext.marshmallow.schema as _marshmallow_schema
  import marshmallow_annotations.ext.marshmallow.validate as _marshmallow_validate

  def field_for_validations(validations):
    return mm_fields.Field(validate=validations)


# Generated at 2022-06-13 19:25:54.210017
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    dt = datetime(2012, 10, 2, 15, 43, 56, 123456)
    assert field._serialize(dt, None, None, None) == "2012-10-02T15:43:56.123456"
    assert field._deserialize("2012-10-02T15:43:56.123456", None, None) == dt



# Generated at 2022-06-13 19:26:04.648533
# Unit test for function build_schema
def test_build_schema():
    import typing
    import marshmallow as ma
    # ------------------ Test the class function ------------------
    # Test for the empty schema
    @dataclass_json
    @dataclass
    class TestDataClassEmptySchema:
        # Test for the empty Schema
        pass

    temp_schema = build_schema(TestDataClassEmptySchema, mixin=None, infer_missing=False, partial=False)
    assert temp_schema.Meta.fields == tuple()
    # Test for the empty Schema with 'json_module'
    temp_schema = build_schema(TestDataClassEmptySchema, mixin=None, infer_missing=False, partial=False)
    assert temp_schema.Meta.render_module == global_config.json_module

    # ------------------ Test the field function ------------------
    # Test for

# Generated at 2022-06-13 19:26:12.436650
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class SchemaEx(SchemaF):
        pass
    list_data = [{'a': 1, 'b': 2}]
    dict_data = {'a': 1, 'b': 2}
    schema = SchemaEx()
    assert schema.load(list_data) == list_data
    assert schema.load(dict_data) == dict_data
    assert schema.load([]) == []
    assert schema.load({}) == {}
    schema = SchemaEx(unknown=EXCLUDE)
    assert schema.load(list_data) == list_data
    assert schema.load(dict_data) == dict_data
    assert schema.load([]) == []
    assert schema.load({}) == {}


# Generated at 2022-06-13 19:26:23.721436
# Unit test for function build_type
def test_build_type():
    from marshmallow import fields
    from marshmallow import Schema
    from typing import List
    from dataclasses_json.schema import Schema

    from dataclasses import dataclass
    from dataclasses_json.schema import Schema

    @dataclass
    class Nested(Schema):
        a: int = 1

    @dataclass
    class Klass(Schema):
        nested: Nested
        lst: List[int]

    @dataclass
    class Klass2(Schema):
        a: typing.Union[int, str]

    def build_type(type_, options, mixin, field, cls):
        def inner(type_, options):
            while True:
                if not _is_new_type(type_):
                    break

                type_ = type_.__super

# Generated at 2022-06-13 19:26:30.789419
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Foo:
        pass

    c = SchemaF.loads([], cls=Foo)
    c = SchemaF.loads([], cls=Foo, many=True)
    c = SchemaF.loads('', cls=Foo)
    c = SchemaF.loads('', cls=Foo, many=False)
    c = SchemaF.loads(b'', cls=Foo)
    c = SchemaF.loads(b'', cls=Foo, many=True)


# Generated at 2022-06-13 19:26:42.321887
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Foo:
        name: str

    class FooSchema(Schema):
        class Meta:
            fields = ('name',)

    def make_foo(self, kvs, **kwargs):
        return _decode_dataclass(Foo, kvs, partial=True)

    FooSchema.make_foo = make_foo
    assert FooSchema.schema == {'name': fields.Str()}
    assert inspect.getmembers(FooSchema, predicate=inspect.isfunction) == [('make_foo', make_foo)]
    assert FooSchema.Meta.fields == ('name',)


# Generated at 2022-06-13 19:27:33.160218
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin, dataclass_json

    @dataclass_json
    @dataclass
    class Child(DataClassJsonMixin):
        d: float = 2.0

    @dataclass_json
    @dataclass
    class Parent(DataClassJsonMixin):
        a: int
        b: float = 2.0
        c: str
        e: Child

    assert(schema(Child, DataClassJsonMixin, infer_missing=True) == {'d': fields.Float(allow_none=True, missing=2.0)})

# Generated at 2022-06-13 19:27:43.764776
# Unit test for function build_schema
def test_build_schema():
    import unittest
    import json

    from dataclasses import dataclass
    from marshmallow import Schema as MSchema
    from marshmallow import fields as mfields
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class MyDataClass(DataClassJsonMixin):
        a: int
        b: str
        c: float = 1.1
        d: typing.List[int] = None
        e: typing.Optional[int] = None
        f: typing.Optional[typing.List[int]] = None
        g: typing.Optional[typing.List[typing.List[int]]] = None
        h: typing.Optional[typing.Union[str, int]] = None
        i: typing.Optional[typing.Union[str, int, None]] = 1

# Generated at 2022-06-13 19:27:49.314208
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema, fields, validate, pre_load
    class Options:
        class Schema(Schema):
            id = fields.Integer(dump_to='identifier', attribute='id')
            description = fields.Str()

    class Type:
        class Schema(Schema):
            type = fields.Str()
            options = fields.Nested(Options.Schema, many=True)

    class Data:
        class Schema(Schema):
            name = fields.Str(required=True, validate=validate.Length(min=2))
            type = fields.Nested(Type.Schema, many=False)
            data = fields.Dict()

        def __init__(self, name: str, type: Type, data: dict):
            self.name = name
            self.type = type

# Generated at 2022-06-13 19:27:59.053369
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass, field
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class Model:
        name: str

    @dataclass
    class Test1:
        mm_field_default: typing.List[int] = field(metadata={'mm_field': fields.List(fields.Int())})
        mm_field_builtin: typing.List[int] = field(metadata={'mm_field': fields.List(fields.Int())})
        mm_field_newtype: typing.List[int] = field(metadata={'mm_field': fields.List(fields.Int())})
        mm_field_opt: typing.Optional[int] = field(metadata={'mm_field': fields.Int()})

# Generated at 2022-06-13 19:28:02.453256
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class A:
        x: Optional[int]
        y: str
    class B(A):
        pass
    assert build_schema(B, None, False, False)
    return True
test_build_schema()


# Generated at 2022-06-13 19:28:18.800167
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import Union, List
    from marshmallow import Schema
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        value: Union[int, List[int]]

    class MyClassSchema(SchemaF[MyClass]):
        value = fields.List(fields.Int())

    @dataclass
    class MyClass2:
        value: List[MyClass] = None

    class MyClass2Schema(SchemaF[MyClass2]):
        value = fields.List(fields.Nested(MyClassSchema), allow_none=True)

    data = MyClass2(value=[MyClass(1), MyClass([2, 3])])
    schema = MyClass2Schema()

# Generated at 2022-06-13 19:28:27.671571
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    d: typing.Dict[str, typing.Any] = {}
    SchemaF[typing.Any]().load(d)
    SchemaF[typing.Any]().load([d])

    class X(SchemaF[typing.Any]):
        a: str = fields.String()

    X().load([{'a': 'b'}])
    X().load({'a': 'b'})

    class X2(SchemaF[A]):
        a: str = fields.String()

        @post_load
        def create_obj(self, data):
            return data['a']

    d1 = X2().load({'a': 'b'})
    d2 = X2().load([{'a': 'b'}])
    assert d1 == 'b'

# Generated at 2022-06-13 19:28:33.828986
# Unit test for function build_type
def test_build_type():
    from typing import Callable, Optional, NewType
    import json

    Json = NewType('Json', dict)

    class JsonMixin:
        @classmethod
        def schema(cls):
            return Schema.from_dataclass(cls)

    @dataclass_json
    @dataclass
    class Test(JsonMixin):
        f1: Optional[int]
        f2: str
        f3: Callable[[], str]
        f4: Json

    schema = Test.schema()

    assert json.loads(schema.dump({'f1': None, 'f2': 'hello', 'f3': '', 'f4': {}}).json) == {'f1': None, 'f2': 'hello', 'f3': '', 'f4': {}}




# Generated at 2022-06-13 19:28:36.350914
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert SchemaF<int>().dumps([1, 2, 3])
    assert SchemaF<int>().dumps(1)
    assert SchemaF<int>().dumps([1, 2, 3])
    assert not SchemaF<int>().dumps([1, 2, 3])


# Generated at 2022-06-13 19:28:47.770784
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin, config

    @dataclass
    class SubClass(DataClassJsonMixin):
        a: int = 5

    @dataclass
    class ClassTest(DataClassJsonMixin):
        a: int = 1
        b: str = 'b'
        c: typing.Optional[typing.Union[int, str]] = 1
        d: typing.Union[int, SubClass]
        e: typing.List[str] = config(field_many=True)
        f: typing.Optional[typing.List[str]] = None
        g: typing.Union[int, str, None] = 1
        h: typing.Optional[CatchAllVar] = None
