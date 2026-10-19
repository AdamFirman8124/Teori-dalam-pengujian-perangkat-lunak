

# Generated at 2022-06-13 19:20:51.893394
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class UserSchema(SchemaF[User]):
        pass

    u = User(name='Anton', job=Job(title='Senior Developer', years=10), friends=[User('Ivan', Job(title='Junior Developer', years=2)), User('Sergey', Job(title='Senior Developer', years=5))])
    user_data = {"name": "Anton", "job": {"title": "Senior Developer", "years": 10}, "friends": [{"name": "Ivan", "job": {"title": "Junior Developer", "years": 2}}, {"name": "Sergey", "job": {"title": "Senior Developer", "years": 5}}]}

# Generated at 2022-06-13 19:20:53.119904
# Unit test for function schema
def test_schema():
    # TODO: add test for schema function
    pass



# Generated at 2022-06-13 19:21:00.416324
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass_json
    @dataclass
    class Product(object):
        id: int
        name: str
        desc: str = None

    class ProductSchema(SchemaF[Product]):  # type: ignore
        id = fields.Int()
        name = fields.Str()
        desc = fields.Str()

    product_data = {'id': 1, 'name': 'Foo'}
    schema = ProductSchema()
    product = schema.load(product_data)
    assert product == Product(**product_data)


# Generated at 2022-06-13 19:21:12.390744
# Unit test for function build_schema
def test_build_schema():
    '''
    Unit test for build_schema
    '''

    class Meta:
        fields = ('one', 'two', 'three', 'four', 'five')

    @dataclass_json
    @dataclass
    class A:
        one: str
        two: int
        three: bool
        four: typing.List[str]
        five: typing.Dict[str, Any]

    @dataclass_json
    @dataclass
    class B(A):
        six: str

    assert build_schema(A, None, False, False) == type('Meta',
                                                       (),
                                                       {
                                                           'fields': (
                                                           'one', 'two',
                                                           'three',
                                                           'four', 'five')}
                                                       )

# Generated at 2022-06-13 19:21:21.076014
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    class PersonSchema(SchemaF[Person]):
        name = fields.Str()
        age = fields.Int()
        @post_load
        def make_person(self, data, **kwargs):
            return Person(**data)
    person = Person('John', 30)
    data = PersonSchema().dump(person)
    assert data == {
        'name': 'John',
        'age': 30
    }

# Generated at 2022-06-13 19:21:26.464868
# Unit test for function build_schema
def test_build_schema():
    class A:
        x: int

    class D(A):
        y: int

    s = build_schema(A, {}, False, False)
    assert s.dump(D(1, 2)) == dict(x=1)  # type: ignore

    assert s.loads('{"x":1}', partial=False) == D(x=1)
    assert s.loads('{"x":1}', partial=True) == D(x=1)


# Generated at 2022-06-13 19:21:39.001579
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from datetime import datetime
    import typing

    @dataclass
    class User:
        username: str
        password: str
        last_login: typing.Optional[datetime] = None

    @dataclass
    class User2:
        username: str
        password: str
        last_login: typing.Optional[datetime] = None
    result = schema(User, User, False)
    assert 'username' in result
    assert 'password' in result
    assert 'last_login' in result
    assert result['last_login'].allow_none
    assert result['last_login'].required
    assert result['last_login'].default == None

    result2 = schema(User2, User2, True)
    assert result2['last_login'].default == None


# Generated at 2022-06-13 19:21:45.985344
# Unit test for function schema
def test_schema():
    from typing import Optional, List, Union, Dict, Any, Tuple
    from marshmallow import fields
    from marshmallow_enum import EnumField as MaEnumField
    from marshmallow.exceptions import ValidationError

    from dataclasses import dataclass
    import json

    class LetterCase:
        snake = staticmethod(lambda s: '_'.join(s.split()).lower())

    @dataclass
    class User:
        name: str
        email: str

    @dataclass
    class Address:
        city: str
        street: str

    class Gender(Enum):
        male = 0
        female = 1

    @dataclass
    class Cat:
        name: str
        age: int
        sex: Gender
        color: Optional[str]


# Generated at 2022-06-13 19:21:56.879259
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class A:
        x: int
        y: str = 'abc'

    class B(MixinJSONSchema):
        def get_schema(self):
            return build_schema(cls=A,
                                mixin=MixinJSONSchema,
                                infer_missing=False,
                                partial=False)

    b = B()
    schema_ = b.get_schema()
    a_ = A(x=1)
    a_dumped = schema_.dump(a_)
    a_loaded = schema_.load(a_dumped)
    assert a_.x == a_loaded.x
    assert a_.y == a_loaded.y



# Generated at 2022-06-13 19:21:59.870741
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type:() -> None
    class Test(SchemaF[A]):
        pass
    # type: ignore
    res = Test().dumps("test")
    assert res == "test"



# Generated at 2022-06-13 19:22:28.290894
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from dataclasses_json.api import load, from_dict
    from typing import Dict

    class Foo:
        ...

    class FooSchema(SchemaF[Foo]):
        class Meta:
            ...

        @post_load
        def make_foo(self, dct: Dict[str, typing.Any]) -> Foo:
            return from_dict(Foo, dct)

    schema = FooSchema()
    assert isinstance(schema.load({"bar": 1}), Foo)
    assert isinstance(schema.loads('{"bar": 1}'), Foo)
    assert isinstance(load(schema, {"bar": 1}), Foo)


# Generated at 2022-06-13 19:22:37.324128
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from typing import Optional, List, NamedTuple
    from marshmallow import fields
    from marshmallow.exceptions import ValidationError
    from marshmallow_enum import EnumField

    class MyEnum(Enum):
        First = 0
        Second = 1

    @dataclass_json(unknown='EXCLUDE')
    @dataclass
    class TestUnion:
        key: Optional[MyEnum]
        inner: List[int]

    @dataclass_json(unknown='EXCLUDE')
    @dataclass
    class TestField:
        key: int


# Generated at 2022-06-13 19:22:38.695238
# Unit test for constructor of class _IsoField
def test__IsoField():
    assert _IsoField(required=True)


# Generated at 2022-06-13 19:22:48.759343
# Unit test for function schema
def test_schema():
    # TODO fix unit test
    if False:
        import sys
        import os
        # insert at 1, 0 is the script path (or '' in REPL)
        sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', '..'))
        import dataclasses_json
        from dataclasses import dataclass

        @dataclass
        class Test1:
            f1: str
            f2: int = 1

        class Mixin:
            pass

        assert(schema(Test1, Mixin, infer_missing=True) == {
            'f1': fields.Str,
            'f2': fields.Int(missing=1, allow_none=True)
        })


# Generated at 2022-06-13 19:22:59.028927
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Person:
        name: Optional[str]
        age: Optional[int]
        gender: str
    
    @dataclass
    class Animal:
        name: str
    
    class Mixin:
        @staticmethod
        def animal_name(obj):
            return obj.name
    
    @dataclass_json(mixins=[Mixin])
    class Person:
        name: Optional[str]
        age: Optional[int]
        gender: str
    
    class Mixin:
        @staticmethod
        def animal_name(obj):
            return obj.name
    
    @dataclass_json(mixins=[Mixin])
    class Person:
        name: Optional[str]
        age: Optional[int]
        gender: str
    

# Generated at 2022-06-13 19:23:05.948710
# Unit test for function build_type
def test_build_type():
    UnknownType = typing.TypeVar('UnknownType')
    class SomeClass: pass
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(D): pass

    class MyEnum(Enum):
        a = 1
        b = 2

    class UnknownClass(metaclass=typing.GenericMeta):
        pass

    assert isinstance(build_type(UnknownType, {}, None, None, None), fields.Field)

    assert isinstance(build_type(typing.List[UnknownType], {}, None, None, None), fields.List)
    assert isinstance(build_type(list, {}, None, None, None), fields.List)

# Generated at 2022-06-13 19:23:14.729749
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert isinstance(SchemaF.load(SchemaF, {}), A)
    assert isinstance(SchemaF.load(SchemaF, {}, many=None), A)
    assert isinstance(SchemaF.load(SchemaF, [], many=True), typing.List[A])
    assert isinstance(SchemaF.load(SchemaF, [], many=None), typing.List[A])
    assert isinstance(SchemaF.load(SchemaF, [], many=False), A)

# Generated at 2022-06-13 19:23:17.770086
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime.now())
    assert not _TimestampField()._deserialize(None)
    assert _TimestampField()._deserialize(1579306653)


# Generated at 2022-06-13 19:23:20.431094
# Unit test for function build_schema
def test_build_schema():
    import typing
    class Empty:pass
    assert not _issubclass_safe(Empty, Empty)
    assert _issubclass_safe(Empty, typing.Mapping)


# Generated at 2022-06-13 19:23:25.059022
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # type: () -> None
    class A(SchemaF):
        val = fields.Int()

    assert A().load({'val': 10}) == A(val=10)
    assert A().load([{'val': 10}, {'val': 20}], many=True) == [A(val=10), A(val=20)]



# Generated at 2022-06-13 19:23:42.254576
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime.now(), "attr", "obj")
    assert _TimestampField()._deserialize(1, "attr", "data")



# Generated at 2022-06-13 19:23:49.600484
# Unit test for function build_schema
def test_build_schema():
    @dataclass()
    class A:
        first: int
        second: str = 'default'

    v1 = {'first': 1, 'second': 'second'}
    v2 = {'first': 1, 'second': 'default'}
    v3 = {'first': 'something', 'second': 'second'}
    v4 = {'first': 1, 'second': 1}

    a = A(**v1)
    schema = build_schema(A, None, False, False)
    _s = schema()
    a_s = _s.load(v1)
    a_s2 = _s.load(v2)
    a_s3 = _s.load(v3)
    a_s4 = _s.load(v4)
    assert (a == a_s)

# Generated at 2022-06-13 19:23:54.333836
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    # type: () -> None
    class Data(typing.TypedDict):
        value: int

    encoder = Encoder()

    schema = encoder.schema(Data)()
    res = schema.loads(b'{"value": 5}')  # type: ignore
    assert isinstance(res, Data)
    assert res['value'] == 5

    schema = encoder.schema(typing.List[Data])()
    res = schema.loads(b'[{"value": 5}]')  # type: ignore
    assert isinstance(res, list)
    assert len(res) == 1
    assert type(res[0]) == Data
    assert res[0]['value'] == 5

    data = Data(value=5)
    schema = encoder.schema(Data)()
    res = schema.loads

# Generated at 2022-06-13 19:24:05.669061
# Unit test for function schema
def test_schema():
    import pytest
    from dataclasses_json import DataClassJsonMixin, dataclass_json
    from dataclasses import dataclass
    from dataclasses_json.utils import _is_supported_generic

    @dataclass
    class Foo(DataClassJsonMixin):
        a: int
        b: float
        c: str

    @dataclass_json()
    class Bar:
        a: int
        b: float
        c: str

    assert schema(Bar, DataClassJsonMixin, False) == {'a': fields.Int(), 'b': fields.Float(), 'c': fields.Str()}
    assert schema(Bar, DataClassJsonMixin, True) == {'a': fields.Int(), 'b': fields.Float(), 'c': fields.Str()}
    

# Generated at 2022-06-13 19:24:17.184316
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class A:
        a: int
    @dataclass_json
    @dataclass
    class B:
        a: int
        b: typing.Optional[A]
    @dataclass_json
    @dataclass
    class C:
        a: int
        b: typing.Optional[B]
    @dataclass_json
    @dataclass
    class D:
        a: int
        b: typing.Optional[C]
    @dataclass_json
    @dataclass
    class E:
        a: int
        b: typing.Optional[D]
    @dataclass_json
    @dataclass
    class F:
        a: int
        b: typing.Optional[E]


# Generated at 2022-06-13 19:24:23.273366
# Unit test for function build_type
def test_build_type():
    import dataclasses
    import typing

    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        address: typing.Optional[str]

    @dataclasses.dataclass
    class DC:
        person: typing.List[Person]
        data: typing.Optional[typing.Dict[str, typing.Union[int, float]]]

    DC.schema()



# Generated at 2022-06-13 19:24:27.052648
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class TestSchemaF(SchemaF[A]):
        pass

    TestSchemaF().dump(['a', 'b'])
    TestSchemaF().dump('a')

    with pytest.raises(NotImplementedError):
        TestSchemaF()



# Generated at 2022-06-13 19:24:33.063209
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    jsonStr = '[{"id":1,"name":"peter"}]'
    data = [{"id": 1, "name": "peter"}]
    assert SchemaF.loads(jsonStr) == data
    assert SchemaF.loads(b'[{"id":1,"name":"peter"}]') == data
    assert SchemaF.loads(bytearray(b'[{"id":1,"name":"peter"}]')) == data
    assert SchemaF.loads(data=jsonStr) == data
    assert SchemaF.loads(data=b'[{"id":1,"name":"peter"}]') == data
    assert SchemaF.loads(data=bytearray(b'[{"id":1,"name":"peter"}]')) == data


# Generated at 2022-06-13 19:24:34.866885
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField() is not None


# Generated at 2022-06-13 19:24:36.628756
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    _TimestampField()



# Generated at 2022-06-13 19:25:00.791430
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    raw_value = 1615827551.043
    value = _timestamp_to_dt_aware(raw_value)
    field = _TimestampField()
    assert field._serialize(value, None, None) == raw_value
    assert field._deserialize(raw_value, None, None) == value



# Generated at 2022-06-13 19:25:04.546924
# Unit test for function build_type
def test_build_type():
    options = {}
    mixin = typing.Any
    field = typing.Any
    cls = typing.Any
    type_ = typing.Any
    build_type(type_, options, mixin, field, cls)


# Generated at 2022-06-13 19:25:10.299054
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import marshmallow as mm
    @mm.post_load
    def mk(data):
        return data['id']
    class A(mm.Schema):
        id = mm.Int(data_key='id')
    class B(mm.Schema):
        id = mm.Int(data_key='id')
    class S(SchemaF[typing.Union[A, B]]):
        a = mm.Nested(A)
        b = mm.Nested(B)
        class Meta:
            unknown = EXCLUDE
    A.__name__
    d = S.loads('{"a": {"id": 2}}')
    assert d == 2

# Generated at 2022-06-13 19:25:18.037422
# Unit test for method load of class SchemaF
def test_SchemaF_load():
  data = {'a': '3'}
  # assert SchemaF[int]() // TypeError: SchemaF cannot be instantiated
  assert SchemaF[int].load(data, many=False) == 3

# Generated at 2022-06-13 19:25:24.381467
# Unit test for function build_schema
def test_build_schema():
    schema = build_schema(MixinA,MixinA, True, False)
    assert schema.__name__ == 'MixinASchema'
    assert issubclass(schema, Schema)
    assert hasattr(schema,'make_mixina')



# Generated at 2022-06-13 19:25:37.942725
# Unit test for function build_type
def test_build_type():
    from typing import Optional
    from dataclasses import dataclass

    @dataclass
    class Dummy:
        foo: Optional[str]

    _decode_dataclass(Dummy)
    assert build_type(Dummy, {}, object, dc_fields(Dummy)[0], Dummy)(Dummy, {}) == fields.Nested(Dummy.schema(),{})
    assert build_type(type(None), {}, object, dc_fields(Dummy)[0], Dummy)(type(None), {}) == fields.Field(**{})
    assert build_type(Optional[str], {}, object, dc_fields(Dummy)[0], Dummy)(Optional[str], {}) == fields.String(**{})

# Generated at 2022-06-13 19:25:48.863448
# Unit test for function schema
def test_schema():
    class C(Enum):
        A = 1
        B = 2
    class A:
        @dataclass_json(mm_field=fields.List(fields.Str()))
        class Person:
            name: str
        @dataclass_json(mm_field=fields.Str())
        class Page:
            name: str
            num: int
        @dataclass_json(mm_field=EnumField(enum=C))
        class Color:
            c: C
        @dataclass_json(mm_field=fields.Raw, letter_case=camelize)
        class Poem:
            title: str
            author: Person
            pages: List[Page]
            about: Optional[Dict[str, Any]] = {}
            color: Optional[Color] = None
            pi: float = 3.

# Generated at 2022-06-13 19:25:58.598947
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class A:
        a: int

    assert "a" in schema(A, None, False)

    @dataclass_json
    @dataclass
    class B:
        a: typing.Any

    assert "a" in schema(B, None, False)

    @dataclass_json
    @dataclass
    class C:
        a: typing.List

    assert "a" in schema(C, None, False)

    @dataclass_json
    @dataclass
    class D:
        a: typing.Tuple

    assert "a" in schema(D, None, False)


# Generated at 2022-06-13 19:26:07.518019
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class TestCase1:
        a: int = field(default_factory=lambda: 1)

    @dataclass_json
    @dataclass
    class TestCase2:
        a: int = field(default=1, metadata={'dataclasses_json': {'mm_field': fields.Int()}})

    assert isinstance(build_schema(TestCase1, type, True, False)().Meta.fields, tuple)
    assert len(build_schema(TestCase1, type, True, False)().Meta.fields) == 0
    assert isinstance(build_schema(TestCase2, type, True, False)().Meta.fields, tuple)
    assert len(build_schema(TestCase2, type, True, False)().Meta.fields)

# Generated at 2022-06-13 19:26:11.629200
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert isinstance(SchemaF[int].loads(b'1'), int)
    class MyClass(typing.NamedTuple):
        a: int
    assert isinstance(SchemaF[MyClass].loads(b'{"a": 1}'), MyClass)
    assert isinstance(SchemaF[typing.List[int]].loads(b'[1]'), typing.List[int])

# Generated at 2022-06-13 19:27:06.767663
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Pet:
        name: str

    @dataclass_json
    @dataclass
    class Person:
        name: str
        age: int
        pets: List[Pet]

    assert build_schema(Person, None, False, False) == PersonSchema

    @dataclass_json
    @dataclass
    class User:
        name: str = field()

    @dataclass_json
    @dataclass
    class Company:
        name: str
        users: List[User]

    assert build_schema(Company, None, False, False) == CompanySchema



# Generated at 2022-06-13 19:27:16.583079
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import marshmallow as mm

    class Foo(mm.Schema):
        foo = mm.fields.String(required=True)

    data = {'foo': 'bar'}
    dumped = mm.Schema.dump(Foo(), data)

    foo: str = SchemaF(Foo()).loads(mm.Schema.dumps(Foo(), data))
    foo: str = SchemaF(Foo()).loads(dumped)

    foos: typing.List[Foo] = SchemaF(Foo()).loads(mm.Schema.dumps(Foo(), [data, data, data]))
    foos: typing.List[Foo] = SchemaF(Foo()).loads(mm.Schema.dump(Foo(), [data, data, data], many=True))



# Generated at 2022-06-13 19:27:23.983174
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class MySchema(SchemaF[int]):
        pass

    class MySchema2(SchemaF[str]):
        pass

    obj = [{'a': 1}]
    obj2 = [1, 2]
    
    my_schema = MySchema()
    my_schema2 = MySchema2()
    
    dts = my_schema.load(obj)
    assert dts == [1]
    dts2 = my_schema.load(obj2)
    assert dts2 == [1, 2]



# Generated at 2022-06-13 19:27:25.360776
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    return SchemaF[int].dumps(0, many=False)

# Generated at 2022-06-13 19:27:29.568090
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert SchemaF[str].dumps("a") == "\"a\""  # type: ignore
    assert SchemaF[str].dumps("a", many=True) == "[\"a\"]"  # type: ignore



# Generated at 2022-06-13 19:27:37.390152
# Unit test for function build_schema
def test_build_schema():
    schema = build_schema(User, mixin=None, infer_missing=True, partial=False)
    assert schema.__name__ == 'UserSchema'
    assert len(schema.__dict__) == 5
    assert 'Meta' in schema.__dict__
    assert 'make_user' in schema.__dict__
    assert 'name' in schema.__dict__
    assert 'email' in schema.__dict__
    assert 'age' in schema.__dict__
    assert 'Meta' in schema.__dict__
    assert schema.Meta.__name__ == 'Meta'
    assert getattr(schema.Meta, 'fields') == ('name', 'email', 'age')
    assert getattr(schema, 'name') == fields.Str()
    assert getattr(schema, 'email') == fields.Email()

# Generated at 2022-06-13 19:27:48.068981
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Test1(SchemaF):
        pass

    class Test2(Test1):
        pass



# Generated at 2022-06-13 19:27:58.326971
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    _ = SchemaF[int].dump([1, 2])
    _ = SchemaF[int].dump(1)
    _ = SchemaF[int].dump([1, 2], many=False)
    _ = SchemaF[int].dump(1, many=False)
    _ = SchemaF[int].dump([1, 2], many=True)
    _ = SchemaF[int].dump(1, many=True)
    _ = SchemaF[int].dump([1, 2], many=False) # type: ignore
    _ = SchemaF[int].dump(1, many=True)  # type: ignore



# Generated at 2022-06-13 19:28:06.817981
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from typing import List
    from marshmallow import Schema, fields
    from dataclasses_json.schema import SchemaF

    class A(object):
        def __init__(self, a: str, b: int):
            self.a = a
            self.b = b
        @staticmethod
        def from_json(data: str) -> 'A':
            res = A.__new__(A)
            setattr(res, 'a', data)
            setattr(res, 'b', 42)
            return res
    class A2(object):
        def __init__(self, a: str, b: int):
            self.a = a
            self.b = b

# Generated at 2022-06-13 19:28:19.769918
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import marshmallow_dataclass
    schema = marshmallow_dataclass.class_schema(SchemaF.schema_cls)
    json_data = '{"optional": "value"}'
    a = schema.loads(json_data)
    assert isinstance(a, SchemaF.schema_cls)
    assert a.optional == "value"