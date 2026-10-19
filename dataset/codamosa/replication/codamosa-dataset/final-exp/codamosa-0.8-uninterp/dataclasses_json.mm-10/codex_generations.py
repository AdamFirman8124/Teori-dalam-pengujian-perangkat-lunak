

# Generated at 2022-06-13 19:20:51.110567
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from marshmallow_dataclass import class_schema
    from dataclasses import dataclass

    @dataclass
    class Base:
        name: str

    @dataclass
    class Child(Base):
        age: int

    schema = class_schema(Child)

    assert Base(name='John') == schema.load({'name': 'John'}, many=False, partial=True)



# Generated at 2022-06-13 19:21:01.509809
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import Schema, fields

    class MySchema(Schema):
        foo = fields.Str()

    ms = MySchema()
    assert ms.dumps({'foo': 'bar'}) == '{"foo": "bar"}'

    schema: SchemaF[typing.Dict[str, str]] = MySchema()
    assert schema.dumps({'foo': 'bar'}) == '{"foo": "bar"}'
    assert schema.dumps([{'foo': 'bar'}]) == '[{"foo": "bar"}]'
    assert schema.dumps([{'foo': 'bar'}, {'foo': 'bar2'}]) == '[{"foo": "bar"}, {"foo": "bar2"}]'
    assert schema.dumps({'foo': 'bar'}) == '{"foo": "bar"}'


# Generated at 2022-06-13 19:21:10.603706
# Unit test for function build_type
def test_build_type():
    class TestCls1:
        pass

    class TestCls2:
        pass

    class TestCls3:
        pass

    @dataclass_json
    @dataclass
    class MixedIn:
        pass

    @dataclass
    class TestCls4:
        pass

    @dataclass_json
    @dataclass
    class TestCls5:
        pass

    @dataclass
    class TestCls6(MixedIn):
        pass

    @dataclass
    class TestCls7(MixedIn):
        pass

    @dataclass_json
    @dataclass
    class TestCls8(MixedIn):
        pass


# Generated at 2022-06-13 19:21:20.373295
# Unit test for function build_schema
def test_build_schema():
    from dataclasses_json.api_config import ApiConfig

    def test_output(a, d, output):
        assert a == output
        assert d == output

    class MyClass(ApiConfig):
        b: str

    a = MyClass()
    a.b = "test"
    d = MyClass.schema().load(MyClass.schema().dump(a))

    test_output(a, d, "test")



# Generated at 2022-06-13 19:21:26.842240
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    lst = [0]
    lst = SchemaF[int].dumps(lst)
    assert isinstance(lst, str)

    lst = SchemaF[int].dumps(0)
    assert isinstance(lst, str)

    lst = SchemaF[int].dumps([0], many=False)
    assert isinstance(lst, str)

    lst = SchemaF[int].dumps(0, many=False)
    assert isinstance(lst, str)

    lst = SchemaF[int].dumps(0, many=False, output_format='bla')
    assert isinstance(lst, str)

# Generated at 2022-06-13 19:21:32.265875
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    time = datetime.now()
    assert field._serialize(time, None, None) == time.isoformat()
    assert field._deserialize(time.isoformat(), None, None) == time



# Generated at 2022-06-13 19:21:41.636742
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    def f0(schem: SchemaF[A]) -> typing.Any:
        return schem.loads('{"a":1}')
    def f1(schem: SchemaF[A]) -> typing.Any:
        return schem.loads('{"a":1}', many=True)
    def f2(schem: SchemaF[A]) -> typing.Any:
        return schem.loads('{"a":1}', many=False)
    def f3(schem: SchemaF[A]) -> typing.Any:
        return schem.loads(b'{"a":1}')
    def f4(schem: SchemaF[A]) -> typing.Any:
        return schem.loads(b'{"a":1}', many=True)

# Generated at 2022-06-13 19:21:45.926616
# Unit test for function build_schema
def test_build_schema():
    import unittest
    import marshmallow as ma
    
    @dataclass
    class Test:
        field: int
    class TestSchemaMixin:
        pass

    cls = Test
    mixin = TestSchemaMixin
    infer_missing = True
    partial = False

    schema = build_schema(cls, mixin, infer_missing, partial)
    assert schema.Meta.fields == ('field',)
    assert issubclass(schema, ma.Schema)
    assert schema.make_test is not None
    assert schema.dump is not None
    assert schema.dumps is not None
    assert schema.fields["field"].__class__.__name__ == "Int"


# Generated at 2022-06-13 19:21:56.387955
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    import marshmallow
    @dataclass
    class A:
        a: int
    a = build_schema(A,marshmallow.Schema,[],False)
    assert isinstance(a,marshmallow.Schema)
    assert a.Meta.fields == ("a",)
    assert a.make_a is not None
    assert a.dumps is not None
    assert a.dump is not None
    assert a.a is not None
    assert isinstance(a.a,marshmallow.fields.Integer)
    assert a.a.attribute == "a"

# Test for function build_type

# Generated at 2022-06-13 19:22:02.575985
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    @dataclass_json
    @dataclass
    class TestSchemaF:
        a: int

    obj = TestSchemaF(a=2)
    assert obj.a == 2

    obj_serialized = TestSchemaF.Schema().dumps(obj)
    assert obj_serialized == '{"a": 2}'

    obj_deserialized = TestSchemaF.Schema().loads(obj_serialized)
    assert obj_deserialized == obj



# Generated at 2022-06-13 19:22:20.644396
# Unit test for function schema
def test_schema():
    import attr
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int

    @dataclass
    class Book:
        isbn: str = attr.ib(metadata={'dataclasses_json': {'mm_field': fields.Str()}})
        title: str = attr.ib(metadata={'dataclasses_json': {'mm_field': fields.Str()}})
        year: int = attr.ib(metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        author: Person = attr.ib(metadata={'dataclasses_json': {'mm_field': fields.Nested(Person.schema())}})


# Generated at 2022-06-13 19:22:30.970819
# Unit test for function schema
def test_schema():
    import dataclasses
    import typing
    from dataclasses_json import DataClassJsonMixin
    @dataclasses.dataclass
    class SomeClass(DataClassJsonMixin):
        a: int
    assert schema(SomeClass, DataClassJsonMixin, infer_missing=True) == {'a': fields.Int()}



# Generated at 2022-06-13 19:22:38.929187
# Unit test for function build_schema
def test_build_schema():
    for dc, schema_class in [
        (TestStrategy, StrategySchema),
        (TestConfig, ConfigSchema),
        (TestRecord, RecordSchema),
        (TestHistoryEntry, HistoryEntrySchema),
        (TestInfo, InfoSchema),
        (TestStrategyMetadata, StrategyMetadataSchema),
        (TestSection, SectionSchema),
        (TestData, DataSchema),
    ]:
        assert build_schema(dc, SerializerMixin, False, False) == schema_class



# Generated at 2022-06-13 19:22:39.641182
# Unit test for function build_type
def test_build_type():
    pass



# Generated at 2022-06-13 19:22:47.518870
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():  # type: ignore
    dataclass, schema_cls = _decode_dataclass(A)
    schema = schema_cls()
    schema.dump, schema.dumps, schema.load, schema.loads

# Generated at 2022-06-13 19:22:51.897141
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    f = Fields()
    d = SchemaF[Test].dump([Test(c='c')], f)
    assert isinstance(d, list)
    d = SchemaF[Test].dump(Test(c='c'), f)
    assert isinstance(d, dict)



# Generated at 2022-06-13 19:23:02.171195
# Unit test for function schema
def test_schema():
    import marshmallow as mm
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class DC:
        i: int = 3

    @dataclass_json
    @dataclass
    class DC2:
        dc: DC
        l: typing.List[int]

    assert schema(DC2, mm.Schema, False) == {
        'dc': mm.fields.Nested(schema(DC, mm.Schema, False)),
        'l': mm.fields.List(mm.fields.Int)
    }


# Equivalent to the following dataclass_json code:
#
# @dataclass_json
# @dataclass
# class PetSchema(mm.Schema):
#     name: str = field(metadata=dict(dat

# Generated at 2022-06-13 19:23:10.270470
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class C(typing.Generic[A]):
        def dumps(self, obj: A, many: bool = None, *args, **kwargs) -> str:
            pass

    c = C()
    x: typing.List[int] = [1, 2, 3]
    c.dumps(x)
    c.dumps(1)
    x: typing.Optional[int] = None
    c.dumps(x)
    x = 1
    c.dumps(x)



# Generated at 2022-06-13 19:23:13.570377
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    if sys.version_info >= (3, 7):
        class S(SchemaF[int]): pass
        s = S()
        res: int = s.loads('{"a": 1}')



# Generated at 2022-06-13 19:23:22.283045
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class User:
        username: str
        password: str
        id: int = field(default=None)
        age: int = field(default=None, metadata={'foo': 'bar'})
        int_type: typing.Optional[int] = field(default=None)

    schema = build_schema(User, None, False, False)
    assert len(schema.__dict__) == 6  # 5 fields plus make_user
    assert isinstance(schema.__dict__["username"], fields.Str)
    assert schema.__dict__["password"].metadata == {"foo": "bar"}
    assert schema.__dict__["int_type"].allow_none is True

# Generated at 2022-06-13 19:23:52.080638
# Unit test for function build_type
def test_build_type():
    options = {}
    mixin = object
    field = object
    cls = object
    type_ = typing.List[int]

    assert isinstance(build_type(type_, options, mixin, field, cls), fields.List)
    type_ = object
    assert isinstance(build_type(type_, options, mixin, field, cls), fields.Field)



# Generated at 2022-06-13 19:23:54.884692
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    assert f._serialize(datetime.now(), None, None) == datetime.now().isoformat()
    assert f._deserialize(datetime.now().isoformat(), None, None) == datetime.fromisoformat(datetime.now().isoformat())


# Generated at 2022-06-13 19:24:06.812753
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    @dataclass
    class A:
        x: str = 'foo'
    class B(Schema):
        x = fields.Str()
    b = B(many=True)
    _ = b.load([{'x':'bar'}], many=True)
    _ = b.load({'x':'bar'}, many=False)
    _ = b.load([{'x':'bar'}])
    _ = b.load({'x':'bar'})

    _ = b.load([A()], many=True)
    _ = b.load(A(), many=False)
    _ = b.load([A()])
    _ = b.load(A())



# Generated at 2022-06-13 19:24:17.597069
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from typing import Optional


# Generated at 2022-06-13 19:24:27.450340
# Unit test for function build_type
def test_build_type():
    from .utils import jsonify
    from .core import dataclass_json, dataclass_json_config
    from uuid import uuid4
    import enum

    class Animal(enum.Enum):
        cat = "cat"
        dog = "dog"

    @dataclass_json
    class AnimalSchema(Schema):
        kind = EnumField(Animal, by_value=True)

    @dataclass_json
    @dataclass_json_config(encoder=_ExtendedEncoder)
    class Tmp:
        s: typing.Optional[str] = MISSING
        i: int = MISSING

    @dataclass_json
    @dataclass_json_config(encoder=_ExtendedEncoder)
    class Parent:
        kid: typing.Optional[Tmp] = MISSING

# Generated at 2022-06-13 19:24:37.402805
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclass
    class Dummy:
        a: str
        b: int

    schema = SchemaF[Dummy](
        type_='object',
        properties={
            'a': {'type': 'string'},
            'b': {'type': 'integer'},
        }
    )
    schema.dump({'a': 'A', 'b': 1})

    #__annotations__
    assert isinstance(SchemaF[Dummy].__annotations__, dict)
    assert issubclass(SchemaF[Dummy], Schema)
    s = SchemaF[Dummy]() # type: ignore
    s.dump({'a': 'A', 'b': 1}) # type: ignore

    #__init__

# Generated at 2022-06-13 19:24:46.989285
# Unit test for function schema
def test_schema():
    import inspect
    import marshmallow as mm
    import marshmallow.fields as mars_fields
    from typing import Optional

    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class _Test1(DataClassJsonMixin):
        def __init__(self, test1_field1: str, test1_field2: str = 'default1'):
            self.test1_field1 = test1_field1
            self.test1_field2 = test1_field2

    @dataclass
    class _Test2(DataClassJsonMixin):
        def __init__(self, test2_field1: str, test2_field2: Optional[_Test1]):
            self.test2_field1 = test2_field1
            self

# Generated at 2022-06-13 19:24:57.130387
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass
    class A:
        x: int

    @dataclass
    class B:
        x: int
        y: typing.Optional[int] = None

    class ABC(SchemaF[A]):
        x = fields.Int()

    class BCD(SchemaF[B]):
        x = fields.Int()
        y = fields.Int()

    # mm has the wrong return type annotation (dict) so we can ignore the mypy error
    # for the return type overlap
    assert ABC().load({"x":1}) == A(1)
    assert ABC().load([{"x":1}, {"x":2}]) == [A(1), A(2)]  # type: ignore[attr-defined]
    assert BCD().load({"x":1}) == B(1, None)

# Generated at 2022-06-13 19:25:03.337550
# Unit test for function build_schema
def test_build_schema():
    class Foo:
        pass

    class FooSchema(Schema):
        make_foo = post_load(lambda self, kvs: Foo())

    assert build_schema(Foo, None, False, False) == FooSchema

    class Bar(Foo):
        def __init__(self):
            pass

    class BarSchema(FooSchema):
        make_bar = post_load(lambda self, kvs: Bar())
        baz = fields.Str()

    assert build_schema(Bar, None, False, False) == BarSchema

# Generated at 2022-06-13 19:25:08.443657
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    schema = SchemaF[str](unknown='none')
    a = schema.loads('"test"')
    assert a == "test"
    a = schema.loads(b'"test"')
    assert a == "test"
    a = schema.loads(b'"test"', many=True)
    assert a == ["test"]
    a = schema.loads('["test"]')
    assert a == ["test"]
# type: ignore


if sys.version_info < (3, 7):
    SchemaF = Schema



# Generated at 2022-06-13 19:26:07.077317
# Unit test for function schema
def test_schema():
    class SchemaTestClass:
        def __init__(self):
            self.mapping = {'a': 1}
            self.list = [1, 2, 3, 4]
            self.tuple = (1, 2, 3, 4)
            self.dict = {'a': 1, 'b': 2}
            self.str = 'a'
            self.int = 1
            self.float = 1.2
            self.bool = False
            self.datetime = datetime.now()
            self.uuid = UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')
            self.decimal = Decimal(2)
            self.callable = lambda x: x
            self.any = None
            self.dict_var = {}
            self

# Generated at 2022-06-13 19:26:15.318272
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json, DataClassJsonMixin
    from marshmallow import fields
    from marshmallow_enum import EnumField
    from enum import Enum


    @dataclass_json
    @dataclass
    class Test(DataClassJsonMixin):
        a: int
        b: 'Test2'
        c: List[int]
        e: 'Test3'
        f: typing.Union[float, None]
        g: typing.Optional[DataClassJsonMixin] = 'default value'
        h: typing.Optional[DataClassJsonMixin] = None



# Generated at 2022-06-13 19:26:23.589547
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert SchemaF[int].loads('1') == 1
    assert SchemaF[int].loads('1', many=False) == 1
    assert SchemaF[int].loads(b'1') == 1
    assert SchemaF[int].loads(b'1', many=False) == 1
    assert SchemaF[int].loads([b'1', b'2']) == [1, 2]
    assert SchemaF[int].loads([b'1', b'2'], many=True) == [1, 2]


T = typing.TypeVar('T')



# Generated at 2022-06-13 19:26:28.797211
# Unit test for function build_type
def test_build_type():
    from .dataclasses import dataclass_json
    from dataclasses import dataclass
    from typing import Type, List, Union

    @dataclass
    class A:
        a: Union[int, float] = 1

    @dataclass_json(mm_field=fields.Integer(allow_none=False))
    @dataclass
    class B:
        a: Union[int, float] = 1

    @dataclass
    class C:
        a: List[Union[int, Union[int, float]]] = 1

    assert isinstance(build_type(A, {}, dataclass_json.NewType, dc_fields(B)[0], B), fields.Integer)

# Generated at 2022-06-13 19:26:33.439053
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class TestClass(typing.Generic[A]):
        def method(self, schema: SchemaF[A]) -> \
                typing.Callable[[TOneOrMultiEncoded, bool, bool, str], TOneOrMulti]:
            return SchemaF[A].load



# Generated at 2022-06-13 19:26:40.677335
# Unit test for function build_type
def test_build_type():
    import marshmallow.fields
    @dataclass_json
    @dataclass
    class Test:
        pass

    assert isinstance(build_type(int, {}, None, '', Test)(int, {}), fields.Int)
    assert isinstance(
        build_type(typing.Optional[int], {}, None, '', Test)(typing.Optional[int], {}),
        fields.Int)



# Generated at 2022-06-13 19:26:49.802094
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class D1(typing.Generic[A]):
        def __init__(self, d: A):
            self.d = d

    class S(SchemaF[D1[str]]):
        pass

    s = S()
    d = D1('Hi')
    res = s.dump(d)
    assert res == {'d': 'Hi'}  # type: ignore

    res = s.dumps(d)
    assert res == '{"d": "Hi"}'

    res = s.dump([d, d])
    assert res == [{'d': 'Hi'}, {'d': 'Hi'}]  # type: ignore

    res = s.dumps([d, d])
    assert res == '[{"d": "Hi"}, {"d": "Hi"}]'


# Generated at 2022-06-13 19:26:53.424957
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime.now(), 'attr', {}) == datetime.now().timestamp()
    assert _TimestampField()._deserialize(datetime.now().timestamp(), 'attr', {}) == datetime.now()



# Generated at 2022-06-13 19:27:04.709471
# Unit test for function build_type
def test_build_type():
    from dataclasses_json import dataclass_json
    from enum import Enum
    from typing import Dict, List

    @dataclass_json
    @dataclass_json
    class MyClass:
        pass

    class MyEnum(Enum):
        A = 1
        B = 2

    cc = MyClass()
    c = build_type(MyClass, {}, dataclass_json,
                   dc_fields(MyClass)[0], MyClass)
    assert str(c.__class__) == "<class 'marshmallow.fields.Nested'>"

    e = build_type(MyEnum, {}, dataclass_json,
                   dc_fields(MyClass)[1], MyClass)

# Generated at 2022-06-13 19:27:11.675096
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    JsonString = str
    JSON_DATA: JsonString
    JSON_DATA = ""
    JSON_DATA = ""

# Generated at 2022-06-13 19:29:27.944285
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    assert field.description == "datetime.datetime"


# Generated at 2022-06-13 19:29:37.749858
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass
    class A:
        b: float = None

    @dataclass_json
    @dataclass
    class Z(A):
        a: typing.Dict[str, bool] = None
        b: str = 'a'
        c: typing.Optional[int] = None
        d: typing.List[str] = None

    assert schema(Z, {}, False)['b'] == fields.Str()


# Generated at 2022-06-13 19:29:48.273727
# Unit test for function schema
def test_schema():
    import marshmallow
    assert schema(A) == {
        'foo': marshmallow.fields.Str(
            data_key='foo', default='bar')
    }
    assert schema(B) == {
        'foo': marshmallow.fields.Str(
            data_key='foo', default='bar')
    }
    assert schema(C) == {
        'foo': marshmallow.fields.Str(
            data_key='foo', default='bar'),
        'foo_camel_case': marshmallow.fields.Str(
            data_key='fooCamelCase', default='baz')
    }


# Generated at 2022-06-13 19:29:53.223498
# Unit test for function build_schema
def test_build_schema():
    from unittest import mock
    from marshmallow import schema
    
    @dataclass
    class TestDataClassBuildSchema:
        a: int = 5
        b: str = 'hello'
        c: Optional[float] = None

    DataClassSchema=build_schema(TestDataClassBuildSchema,'', False, False)

    assert issubclass(DataClassSchema, schema.Schema)
    assert DataClassSchema.__name__ == 'TestDataClassBuildSchemaSchema'
    assert not issubclass(DataClassSchema, schema.SchemaABC)
    assert DataClassSchema.opts.fields == ('a', 'b', 'c')
    assert DataClassSchema.opts.render_module is None
    assert isinstance(DataClassSchema.a, schema.fields.Integer)
   

# Generated at 2022-06-13 19:29:54.277303
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    _TimestampField()


# Generated at 2022-06-13 19:30:05.600889
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    @dataclass
    class Model:
        id: str
        name: str
    class ModelSchema(SchemaF[Model], Schema):
        id = fields.Str()
        name = fields.Str()
    def test_1():
        m = Model(id='7', name='John Doe')
        s = ModelSchema()
        res1 = s.dump(m)
        assert isinstance(res1, dict)
    def test_2():
        m = Model(id='7', name='John Doe')
        s = ModelSchema()
        res1 = s.dump(m, many=False)
        assert isinstance(res1, dict)

# Generated at 2022-06-13 19:30:11.155478
# Unit test for function schema
def test_schema():
    import dataclasses_json
    import dataclasses

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class A:
        a: str
        b: int

    @dataclasses.dataclass
    class B:
        a: A

    schema(B, dataclasses_json.JsonMixin, False)



# Generated at 2022-06-13 19:30:20.366802
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from marshmallow import fields
    from marshmallow_enum import EnumField

    @dataclass
    class Person:
        first_name: str
        last_name: str
        age: int

    @dataclass
    class MySchema(Schema):
        first_name: str
        last_name: str
        age: int

    class Fruit(Enum):
        PEAR = 1
        BANANA = 2
        APPLE = 3

    @dataclass
    class MyClass:
        foo: typing.List[Person]
        bar: typing.Optional[Person]
        baz: typing.Dict[str, Person]
        flob: typing.Mapping[str, Person]
        blar: typing.List[Fruit]
        blub: typing.Optional