

# Generated at 2022-06-13 19:20:51.885790
# Unit test for function build_type
def test_build_type():
    from marshmallow import fields
    from marshmallow_enum import EnumField
    from dataclasses_json.mm_field import _UnionField

    type_ = typing.Optional[typing.List[int]]
    options = {}
    mixin = ()
    field = None
    cls = None

    result = build_type(type_, options, mixin, field, cls)
    assert isinstance(result, fields.List)

    type_ = typing.Optional[typing.List[typing.Optional[int]]]
    options = {}
    mixin = ()
    field = None
    cls = None

    result = build_type(type_, options, mixin, field, cls)
    assert isinstance(result, fields.List)


# Generated at 2022-06-13 19:20:58.590279
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    value = "2014-02-20T04:20:40"
    assert field._serialize(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"),
                            'attr', None, **kwargs) == value
    assert field._deserialize(value, 'attr', None, **kwargs) == datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")


# Generated at 2022-06-13 19:21:01.889377
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()

_SUPPORTED_FIELDS = {
    datetime: _IsoField,
    Decimal: fields.Decimal,
    UUID: fields.UUID,
}



# Generated at 2022-06-13 19:21:07.938495
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import marshmallow as ma
    import marshmallow_enum as ma_en

    @dataclass
    class Test:
        a: Test = None
        b: Test = ma.fields.Constant("test")

    t = Test()
    assert schema(Test, Test, True) == {'a': ma.fields.Constant("test")}
    assert schema(Test, Test, False) == {'a': ma.fields.Constant("test")}



# Generated at 2022-06-13 19:21:12.247018
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class ExampleClass(typing.Generic[A]):
        def __init__(self, a: A):
            self.a = a

    @dc_fields(init=True, repr=True)
    class ExampleClass2(ExampleClass[str]):
        pass

    ExampleClass2.Schema()



# Generated at 2022-06-13 19:21:22.439505
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A:
        pass

    class B(A):
        pass

    class SchemaA(SchemaF[A]):
        pass

    class SchemaB(SchemaF[B]):
        pass

    schema_a = SchemaA()
    schema_b = SchemaB()

    a_list = [A(), A()]
    a_list_encoded = [{}, {}]
    b_list = [B(), B()]
    b_list_encoded = [{}, {}]

    class C:
        pass

    c_list = [C(), C()]
    c_list_encoded = [{}, {}]

    assert schema_a.load(a_list_encoded) == a_list
    assert schema_a.load(a_list_encoded, many=False) == a

# Generated at 2022-06-13 19:21:36.025003
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class Foo:
        bar: int

    @dataclass
    class Foobar:
        foo: Foo
        foobar: str

    class FooSchema(SchemaF[Foo]):
        class Meta:
            unknown = EXCLUDE

        bar = fields.Int()

    class FoobarSchema(SchemaF[Foobar]):
        class Meta:
            unknown = EXCLUDE

        foo = bar = fields.Nested(FooSchema)

    schema = FoobarSchema()

    data = {
        'foo': {
            'bar': 42,
        },
        'foobar': 'xxx'
    }


# Generated at 2022-06-13 19:21:41.437175
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    assert field.deserialize('2019-11-02T11:36:20.158213') == datetime(2019, 11, 2, 11, 36, 20, 158213)
    assert field.deserialize('2019-11-02T11:36:20.158213+09:00') == datetime(2019, 11, 2, 11, 36, 20, 158213)
    assert field.serialize(datetime(2019, 11, 2, 11, 36, 20, 158213)) == '2019-11-02T11:36:20.158213'
    assert field.serialize(datetime(2019, 11, 2, 11, 36, 20, 158213)) == '2019-11-02T11:36:20.158213'


# Generated at 2022-06-13 19:21:46.499723
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Test:
        data: str

    s = build_schema(Test, DataClassJsonMixin, False, True)
    assert s.Meta.fields == ('data',)
    assert s.opts.fields == ('data',)
    assert s.make_test({'data': 'test'}) == Test('test')
    serialized = s.dumps({'data': 'test'})
    assert s.load(json.loads(serialized)) == {'data': 'test'}
    assert s.dump({'data': 'test'}) == {'data': 'test'}

# Generated at 2022-06-13 19:21:58.156509
# Unit test for function build_schema
def test_build_schema():
    import pytest
    from typing import Optional
    from dataclasses import dataclass, fields as dc_fields

    from dataclasses_json.core import get_converter, _user_overrides_or_exts
    from marshmallow import fields, Schema


    @dataclass
    class Person:
        name: str
        age: int


    @dataclass
    class Teacher(Person):
        subject: str


    DataClassSchema = build_schema(Person, dataclasses_json.DataClassJsonMixin, False, False)
    assert len(DataClassSchema.__dict__) == 6
    assert DataClassSchema.__bases__ == (Schema,)
    assert DataClassSchema.Meta.fields == ("name", "age")
    assert DataClassSchema.make_person

# Generated at 2022-06-13 19:22:18.850901
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclass_json
    @dataclass
    class MyDC:
        username: str


    @dataclass_json
    @dataclass
    class MyDC2:
        username: str


    assert SchemaF[MyDC].dump(MyDC('blue')) == {'username': 'blue'}
    assert SchemaF[MyDC].dump([MyDC('blue'), MyDC('blue')]) == [{'username': 'blue'}, {'username': 'blue'}]
    assert SchemaF[MyDC2].dumps(MyDC2('blue')) == '{"username": "blue"}'
    assert SchemaF[MyDC2].dumps([MyDC2('blue')]) == '[{"username": "blue"}]'



# Generated at 2022-06-13 19:22:25.067601
# Unit test for method load of class SchemaF
def test_SchemaF_load():  # type: ignore
    class Test(typing.NamedTuple):
        a: str
        b: float

    class TestSchema(SchemaF[Test]):
        a = fields.Str()
        b = fields.Float()

    assert [Test('a', 1.0), Test('b', 2.0)] == TestSchema().load([{'a': 'a', 'b': 1.0}, {'a': 'b', 'b': 2.0}])  # type: ignore
    assert Test('a', 1.0) == TestSchema().load({'a': 'a', 'b': 1.0})  # type: ignore



# Generated at 2022-06-13 19:22:34.647691
# Unit test for function build_type
def test_build_type():
    from marshmallow import Schema, fields, ValidationError
    from dataclasses import dataclass
    from typing import Union, List
    from dataclasses_json import dataclass_json

    @dataclass
    class User:
        id: int
        name: str

    @dataclass_json(mm_field=fields.Nested(User.schema()))
    @dataclass
    class TestClass:
        user: User

    assert build_type(User, {}, dataclasses_json.DataClassJsonMixin,
                      dc_fields(TestClass)[0], TestClass) == fields.Nested(User.schema())



# Generated at 2022-06-13 19:22:45.709137
# Unit test for function build_type
def test_build_type():
    import typing
    import uuid
    from marshmallow import fields, Schema, post_load
    from marshmallow_enum import EnumField  # type: ignore
    from marshmallow.exceptions import ValidationError
    from datetime import datetime
    from dataclasses import dataclass

    from dataclasses_json.mm import SchemaType, build_type, TYPES

    @dataclass
    class _Test:
        first_name: str
        last_name: str

    class NameMixin:
        @staticmethod
        def _user_overrides_or_exts():
            return {}

        @staticmethod
        def _user_overrides_or_exts_final():
            return {}

    class _TestSchema(NameMixin, SchemaType[_Test]):
        first_name = fields

# Generated at 2022-06-13 19:22:51.140474
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    # calls _TimestampField()._serialize
    ts = 1588013814.0
    assert _TimestampField()._serialize(datetime.fromtimestamp(ts), None, None, None) == ts

    # calls _TimestampField()._deserialize
    assert _TimestampField()._deserialize(ts, None, None, None) == datetime.fromtimestamp(ts, tz=None)


# Generated at 2022-06-13 19:22:53.390522
# Unit test for function build_type
def test_build_type():
    import unittest
    # FIXME: add test
    unittest.TestCase.assertEqual(True, True)
    return True



# Generated at 2022-06-13 19:22:59.253376
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    schema = SchemaF()
    obj = [1, 2, 3]
    data = schema.dumps(obj, many=True)
    assert data == '[1, 2, 3]'
    obj = 4
    data = schema.dumps(obj, many=None)
    assert data == '4'
    data = schema.dumps(obj)
    assert data == '4'

# Generated at 2022-06-13 19:23:06.268544
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from typing import List

    from marshmallow import Schema, fields
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str

    class PersonSchema(Schema):
        name = fields.Str()

    @dataclass
    class Classroom:
        people: List[Person]

    class ClassroomSchema(SchemaF[Classroom]):
        people = fields.Nested(PersonSchema, many=True)

    room_schema = ClassroomSchema()
    room = Classroom([Person('Peter')])
    enc = room_schema.dump(room)
    assert isinstance(enc, list)
    assert enc == [{'name': 'Peter'}]



# Generated at 2022-06-13 19:23:15.582127
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from dataclasses import dataclass
    class MyEnum(Enum):
        A = 'a'
        B = 'b'
    @dataclass
    class MyData:
        enum: MyEnum = MyEnum.A
    MyDataSchema = SchemaF[MyData]
    schema = MyDataSchema()
    my_data = schema.loads('{"enum": "b"}')
    assert my_data is not None
    assert my_data.enum == MyEnum.B


# Generated at 2022-06-13 19:23:24.662095
# Unit test for function build_type
def test_build_type():
    import typing
    import marshmallow as mm
    import dataclasses

    @dataclasses.dataclass
    class Adress:
        city: str = 'Vancouver'

    @dataclasses.dataclass
    class User:
        name: str
        age: int
        updated_at: datetime = dataclasses.field(init=False)

    @dataclasses.dataclass
    class Payload(mm.Schema):
        user: User
        timestamp: float

    assert isinstance(build_type(str, {}, Schema,
                               dc_fields(Payload)[2], Payload),
                      mm.Field)

    @dataclasses.dataclass
    class Payload(mm.Schema):
        user: User
        timestamp: datetime


# Generated at 2022-06-13 19:23:46.993975
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import marshmallow
    @dataclass
    class Test:
        int: int = 3
        optional: typing.Optional[int] = None
        mapping: typing.Mapping[str, int] = {"Hello": 1, "Goodbye": 2}

    t = test_schema.__wrapped__(Test, None, False)
    assert isinstance(t["int"], marshmallow.fields.Int)
    assert isinstance(t["optional"], marshmallow.fields.Int)
    assert isinstance(t["mapping"], marshmallow.fields.Dict)



# Generated at 2022-06-13 19:23:49.257335
# Unit test for function schema
def test_schema():
    try:
        _handle_undefined_parameters_safe(schema)
        return True
    except:
        return False


# Generated at 2022-06-13 19:23:56.305928
# Unit test for function build_type
def test_build_type():
    class TestDataclass(mixin):
        one: typing.Optional[int] = 1
    class Test:
        two: TestDataclass = TestDataclass()
        three: typing.List[TestDataclass] = None
        four: typing.List[typing.Optional[TestDataclass]] = None

    options = {'missing': MISSING}
    field_of_one = dc_fields(Test)[0]
    assert isinstance(build_type(field_of_one.type, options, mixin, field_of_one, Test), fields.Int)
    options = {'missing': MISSING}
    field_of_two = dc_fields(Test)[1]

# Generated at 2022-06-13 19:23:57.828942
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A(SchemaF[A]):
        pass
    A.load(A(), many=True)

# Generated at 2022-06-13 19:24:00.189737
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert True



# Generated at 2022-06-13 19:24:10.925057
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    obj = load(data, many, partial, unknown)
    obj: TOneOrMulti
    data: TOneOrMultiEncoded
    many: bool
    partial: bool
    unknown: str

    obj = loads(json_data, many, partial, unknown)
    obj: TOneOrMulti
    json_data: JsonData
    many: bool
    partial: bool
    unknown: str

# Generated at 2022-06-13 19:24:14.908530
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class I:
        pass

    @dataclass_json
    @dataclass
    class C:
        i: I

    assert build_schema(I, None, True, False)
    assert build_schema(C, None, True, False)


# test_build_schema()

# Generated at 2022-06-13 19:24:25.258838
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    pass

    class Serializable(object):
        pass
    class Attributes(DataclassJsonMixin):
        a: int = field(default=0)
        b: str = field(default='a')
        c: int = field(default=None, repr=False)
        d: bool = field(default=True)
        e: bool = field(default=False)
        f: bool = lazy_field(lambda: True)
        g: int = field(default=None, metadata={'nan': True})
        h: Serializable = field(default=None, metadata={'cls': Serializable})
        i: Tuple[int, ...] = field(default=(1, 2, 3), metadata={'type': int})
        j: int = field(default=None, metadata={'type': int})

# Generated at 2022-06-13 19:24:28.866677
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class UserSchema(SchemaF[User]):
        name = fields.String()

    s = UserSchema()
    s.loads('[{"name":"bob"},{"name":"alice"}]')
    s.loads('{"name":"bob"}')


# Generated at 2022-06-13 19:24:33.773502
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    b = _TimestampField(required=True)
    assert b._deserialize(None, None, None) == ValidationError(b.default_error_messages["required"])
    assert b._serialize(None, None, None) == ValidationError(b.default_error_messages["required"])



# Generated at 2022-06-13 19:24:54.456312
# Unit test for function schema
def test_schema():
    class Model:
        pass
    assert list(schema(Model, None, False).keys()) == []


# class_name -> {field_name -> overrides}
_user_overrides = {}

# class_name -> {field_name -> {param_name -> param_value}}
_user_extensions = {}



# Generated at 2022-06-13 19:25:02.851767
# Unit test for function build_type
def test_build_type():
    from marshmallow import Schema, fields
    from marshmallow_enum import EnumField as EF
    from typing import Union
    import dataclasses_json as json
    import uuid
    from dataclasses import dataclass
    from enum import Enum
    class E(Enum):
        a = 1
        b = 2
    @dataclass
    class A:
        pass
    @json.dataclass_json
    class AJS(A):
        pass
    class AJS2(AJS):
        pass
    @dataclass
    class DC:
        a: str
        b: typing.List[AJS]
        c: typing.List[int]
        d: typing.Optional[int]
        e: float
        f: AJS
        g: AJS2
        h: E
        i

# Generated at 2022-06-13 19:25:08.060294
# Unit test for function build_schema
def test_build_schema():
    schema = build_schema(
        cls=User,
        mixin=mm_get_mixin(),
        infer_missing=mm_get_config().infer_missing,
        partial=mm_get_config().partial)
    assert isinstance(schema.Meta, type)
    assert len(schema.Meta.fields) == 5
    assert hasattr(schema, 'make_user')
    assert hasattr(schema, 'dumps')
    assert hasattr(schema, 'dump')



# Generated at 2022-06-13 19:25:11.358589
# Unit test for constructor of class _IsoField
def test__IsoField():
    from datetime import datetime
    from dataclasses_json.marshmallow import _IsoField
    return datetime.fromisoformat(_IsoField()._serialize(datetime(1970,1,1)))


# Generated at 2022-06-13 19:25:19.071916
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow import Schema
    from marshmallow.fields import String
    from dataclasses import dataclass
    from typing_extensions import Annotated

    T = typing.TypeVar("T", bound="AnyString")

    class AnyString(str, typing.Generic[T]):
        pass

    @dataclass(frozen=True)
    class Quest(typing.Generic[T]):
        item: Annotated[T, AnyString]
        cost: int

    @dataclass(frozen=True)
    class QuestDict(typing.Generic[T]):
        quest: Quest[T]

    @dataclass(frozen=True)
    class QuestList(typing.Generic[T]):
        quests: typing.List[Quest[T]]


# Generated at 2022-06-13 19:25:31.118612
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json


    @dataclass_json
    @dataclass
    class SchemaTest:
        z: int = None
        y: str = None
        x: float = None
    assert schema(SchemaTest, None, True) == {'z': fields.Int(allow_none=True, missing=None),
                       'y': fields.Str(allow_none=True, missing=None),
                       'x': fields.Float(allow_none=True, missing=None)}



# Generated at 2022-06-13 19:25:36.265795
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    import typing
    import marshmallow_dataclass as mmdc


    @mmdc.dataclass
    class Foo:
        foo: str
        bar: int


    @mmdc.dataclass
    class Qux:
        qux: str
        quux: typing.List[Foo]


    Sch = mmdc.SchemaF[Foo]
    Sch.load({'foo': 'a', 'bar': 1})
    Sch.load([{'foo': 'a', 'bar': 1},{'foo': 'b', 'bar': 2}])



# Generated at 2022-06-13 19:25:45.614603
# Unit test for function schema
def test_schema():
    import dataclasses, typing
    import marshmallow as mm
    @dataclasses.dataclass
    class Cat:
        name: str

    @dataclasses.dataclass
    class Dog:
        name: str

    @dataclasses.dataclass
    class Pet:
        pet: typing.Union[Cat, Dog]

    schema = schema(Pet, mm.Schema, True)
    assert isinstance(schema['pet'], _UnionField)
    assert schema['pet'].desc[Cat].__name__ == 'Schema'
    assert schema['pet'].desc[Dog].__name__ == 'Schema'

# Generated at 2022-06-13 19:25:46.731733
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()


# Generated at 2022-06-13 19:25:51.006775
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    test_value = datetime.now()
    f = _TimestampField()
    assert f._serialize(test_value, None, None) == test_value.timestamp()
    assert f._deserialize(test_value.timestamp(), None, None) == test_value


# Generated at 2022-06-13 19:26:24.691434
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from typing import List, Mapping, Union, Optional, cast
    from marshmallow import Schema, fields, validate  # type: ignore
    from marshmallow import ValidationError  # type: ignore


    class PersonSchema(SchemaF[Person]):
        name = fields.Str(validate=validate.Length(min=2), required=True)
        age = fields.Int(required=True, validate=validate.Range(min=18))
        address = fields.Nested(lambda: AddressSchema())
        friends = fields.Nested(lambda: FriendsSchema(), many=True)

    class AddressSchema(SchemaF[Address]):
        street = fields.Str()
        city = fields.Str(validate=validate.Length(min=2), required=True)


# Generated at 2022-06-13 19:26:33.438893
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import Schema
    from typing import TypeVar, Generic

    T = TypeVar('T')
    class A(Generic[T]):
        pass
    obj = A[int]()
    cls = SchemaF[A[int]]
    mm_schema = Schema()
    cls.dumps(obj)
    cls.dumps(obj, mm_schema)
    cls.dumps(obj, mm_schema, many=True)


# Generated at 2022-06-13 19:26:45.744488
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from typing import List


    class PersonSchema(Schema):
        name = fields.Str()


    class Person:
        def __init__(self, name: str):
            self.name = name


    schema = SchemaF[Person]()
    assert schema.dump([Person('me'), Person('you')]) == \
        [{'name': 'me'}, {'name': 'you'}]
    assert schema.dump(Person('me')) == {'name': 'me'}

    with pytest.raises(ValidationError):
        schema.dump([Person('me'), Person('')])

    with pytest.raises(ValidationError):
        schema.dump(Person(''))


# Unit test

# Generated at 2022-06-13 19:26:54.421504
# Unit test for function schema
def test_schema():
    import dataclasses
    import typing
    from dataclasses_json import dataclass_json, types

    @dataclass_json
    @dataclasses.dataclass
    class User:
        id: int
        name: typing.Optional[str]
        age: int = 10

    d = {
        'id': 1234,
        'name': 'somnath',
        'age': 23
    }

    schema = {
        'id': fields.Int(),
        'name': fields.Str(),
        'age': fields.Int(default=10)
    }
    u = User.schema().load(d)
    assert u == User(id=1234, name='somnath', age=23), u


# Generated at 2022-06-13 19:27:00.216530
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema

    class User(Schema):
        name = fields.Str()
        email = fields.Email()

    class UserSchemaF(SchemaF[User]):
        name = fields.Str()
        email = fields.Email()

    def func(user):
        print(type(user.dump()))

    func(User())
    func(UserSchemaF())
'''

BASE_CLASS_FOR_TYPING_GENERICS_POST_3_7_1 = '''
if sys.version_info >= (3, 7, 1):
    _Schema = Schema
else:
    class _Schema(Schema, typing.Generic[A]):
        """Lift Schema into a type constructor"""


# Generated at 2022-06-13 19:27:08.528733
# Unit test for function build_schema
def test_build_schema():

    # Check the schema for a simple dataclass
    @dataclass_json
    @dataclass
    class SimpleDataclass:
        n: int
        s: str

    dcs = build_schema(SimpleDataclass, type, True, False)
    assert dcs.__name__ == 'SimpleDataclassSchema'
    assert dcs().fields is not None
    assert dcs.Meta.fields == ('n', 's')
    assert dcs.Meta.__dict__['fields'] == ('n', 's')

    # Check the schema for a nested dataclass
    @dataclass_json
    @dataclass
    class NestedDataclassB:
        b: int

    @dataclass_json
    @dataclass
    class NestedDataclassA:
        n: int

# Generated at 2022-06-13 19:27:17.704363
# Unit test for function schema
def test_schema():
    d = datetime.now()
    p1 = dataclasses.dataclass(frozen=True)(name='V', age=20, dob=d)
    p2 = dataclasses.dataclass(frozen=True)(name='X', age=20, dob=d)
    print(p1, p2)
    assert p1 != p2

    data1 = {'name': 'V', 'age': 20, 'dob': d}
    data2 = {'name': 'X', 'age': 20, 'dob': d}
    assert data1 != data2

    class S(Schema):
        name = fields.Str()
        age = fields.Int()
        dob = _TimestampField()

    schema = S()

# Generated at 2022-06-13 19:27:26.171999
# Unit test for function build_type
def test_build_type():
    class EnumTest(Enum):
        a = 1
        b = 2

    class ABC:
        pass

    class ABC2:
        pass

    class ABC_mixin:
        pass

    class ABC2_mixin:
        pass

    @dataclass
    class ABC_dc(ABC_mixin):
        a: int
        b: str

    @dataclass_json
    @dataclass
    class ABC2_dc(ABC2_mixin):
        a: int
        b: str

    @dataclass
    class ABC_dc2(ABC_mixin):
        a: int
        b: str

    @dataclass
    class ABC_dc3(ABC_mixin):
        a: int
        b: str

    @dataclass
    class SimpleDc:
        foo

# Generated at 2022-06-13 19:27:35.885950
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from typing import Union, List, TypeVar
    from enum import Enum
    from marshmallow import fields_for_schema

    @dataclass
    class Item:
        title: str = 'item'

    T = TypeVar('T', Item, int)

    @dataclass
    class MyData:
        name: str
        age: int = 18
        items: Union[Item, List[Item]] = None
        flag: bool = False
        item: Item = Item()

    def test_schema():
        my_data = MyData(name='John', age=19, flag=True)
        # Item() is not dumped by default
        assert my_data == MyData.schema().load(MyData.schema().dump(my_data))


# Generated at 2022-06-13 19:27:40.200861
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: int = 3

    assert schema(A, {}, False) == {'a': fields.Int(), 'b': fields.Int(default=3)}



# Generated at 2022-06-13 19:28:52.434061
# Unit test for function build_schema
def test_build_schema():
    class TestSchema(Schema):
        class Meta:
             fields = ("name", "data")

        @post_load
        def make_test(self, data, **kwargs):
            return Test(**data)

    data = TestSchema(strict=True).load({"name": "name", "data": "data"})
    assert data.data == "data"
    assert data.name == "name"


# Generated at 2022-06-13 19:29:03.308041
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class DataClassTest:
        id: int = field(metadata={
            "dataclasses_json": {
                "mm_field": fields.Str()
            }
        })
        name: str

    DataClassTestSchema = build_schema(DataClassTest, None, None, None)
    item = DataClassTest(id=123, name='test')
    schema = DataClassTestSchema()
    expected_result = {'id': '123', 'name': 'test'}
    
    assert schema.dump(item) == expected_result 

test_build_schema()


# Generated at 2022-06-13 19:29:05.252403
# Unit test for function schema
def test_schema():
    assert False

_ExtendedEncoderT = typing.TypeVar('_ExtendedEncoderT')


# Generated at 2022-06-13 19:29:09.759410
# Unit test for constructor of class _IsoField
def test__IsoField():
    date = datetime.now()
    date_str = date.isoformat()
    assert _IsoField()._serialize(date, None, None) == date_str
    assert _IsoField()._deserialize(date_str, None, None) == date



# Generated at 2022-06-13 19:29:21.702651
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from typing import List
    from marshmallow import Schema, fields, ValidationError

    # Invalid union type
    class InvalidSchema(Schema, typing.Generic[A]):
        test_field = fields.Field()

    with pytest.raises(NotImplementedError):
        InvalidSchema()

    # Valid single type
    class ValidStringSchema(SchemaF[str]):
        test_field = fields.Field()

    v1 = ValidStringSchema()
    assert v1.load({"test_field": "test_value"}) == "test_value"

    # Valid list type
    class ValidListStrSchema(SchemaF[List[str]]):
        test_field = fields.Field()

    v2 = ValidListStrSchema()

# Generated at 2022-06-13 19:29:28.444097
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin, dataclass_json
    from datetime import date

    @dataclass_json
    class Person(DataClassJsonMixin):
        name: str
        age: int = field(metadata=dict(mm_field=fields.Int(default=None, default_factory=lambda: None)))
        birth_date: date = field(metadata=dict(mm_field=fields.Date(), para=1))
        cirtificate: dict = field(default_factory=dict, metadata=dict(mm_field=fields.Dict()))
        phonenumber: str
        # phonenumber1: str = field(metadata=dict(mm_field=fields.Int()))  # See if some error is thrown
        phonenumber

# Generated at 2022-06-13 19:29:38.805661
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import marshmallow.fields as mm
    import typing

    class Person(typing.Generic[str]):
        def __init__(self, name: str) -> None:
            self.name = name

    def create_schema(mm, Person):
        class PersonSchema(SchemaF[Person[str]]):  # type: ignore
            name = mm.Str()

        return PersonSchema()

    s = create_schema(mm, Person)
    p = Person("Hi")
    x = s.dump(p)
    assert x == {"name": "Hi"}



# Generated at 2022-06-13 19:29:41.816363
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    field.deserialize(datetime(2020,1,1,1,1,1).timestamp())



# Generated at 2022-06-13 19:29:50.875859
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class MySchema(SchemaF):
        pass

    assert MySchema().dumps([1,2, 3]) == "[1, 2, 3]"
    assert MySchema().dumps(obj=1) == "1"



# Generated at 2022-06-13 19:29:53.018615
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert SchemaF[int].load([{'val': 1}, {'val': 2}], many=True) == [1, 2]
    assert SchemaF[int].load({'val': 1}) == 1

