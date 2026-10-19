

# Generated at 2022-06-13 19:20:42.958879
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert SchemaF.load(None, None) == None # type: ignore

# Generated at 2022-06-13 19:20:45.814936
# Unit test for constructor of class _IsoField
def test__IsoField():
    v = _IsoField()
    assert(v.default_error_messages["required"] == "Missing data for required field.")


# Generated at 2022-06-13 19:20:54.992542
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from datetime import timezone as tz
    import dataclasses_json

    @dataclass
    class Coordinate:
        x: int
        y: int

    @dataclass
    class Foo:
        foo: int
        bar: Coordinate = dataclasses.field(metadata={'dataclasses_json': {'mm_field': fields.Int()}})

    @dataclasses_json.dataclass_json
    class Bar:
        foo: int
        bar: Coordinate

    assert schema(Bar, dataclasses_json.ABCExtendedJSONEncoder, False) == {
        'foo': fields.Int(),
        'bar': fields.Nested(schema(Coordinate, dataclasses_json.ABCExtendedJSONEncoder, False))
    }

# Generated at 2022-06-13 19:20:57.527795
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    
    @dataclass
    class Test:
        foo: str
        bar: int = field(metadata = {'dataclasses_json':{'mm_field': 'foo'}})
    
    assert issubclass(build_schema(Test, None, True, False), Schema)


# Generated at 2022-06-13 19:21:04.726577
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import typing
    import dataclasses_json
    import marshmallow

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class T1(object):
        a: typing.List[int]

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class T2(object):
        a: typing.List[str]

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class T3(object):
        a: typing.List[T2]

    def test_0():
        t1: T1 = T1([1, 2, 3])
        schema: SchemaF[T1] = dataclasses_json.Schema.from_type(T1)

# Generated at 2022-06-13 19:21:17.596410
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass
    class A:
        a: int

    @dataclass
    class B:
        b: int

    def test(schema: SchemaF[typing.Union[A, B]], data: typing.Union[list, dict, A, B]):
        return schema.load(data)

    assert test(
        SchemaF[typing.Union[A, B]](strict=True),
        [
            {"a": 1},
            {"b": 1}
        ]
    ) == [
        A(a=1),
        B(b=1)
    ]

    """
    https://github.com/TezRomacH/dataclasses_json/pull/107
    """

# Generated at 2022-06-13 19:21:23.863829
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclasses.dataclass
    class Dc:
        a: typing.Optional[int] = dataclasses.field(
            default=None,
            metadata={'mm_field': fields.Str()}
        )

    schema = SchemaF[Dc]()
    s = schema.dump(Dc(a=None))
    assert s == {'a': 'None'}
    s = schema.dump([Dc(a=None)])
    assert s == [{'a': 'None'}]



# Generated at 2022-06-13 19:21:37.188818
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class InputType(typing.Generic[A]):
        pass

    schema_f = SchemaF.__getitem__(InputType, A)  #type: ignore
    assert isinstance(schema_f, SchemaF)  # type: ignore

    class UserSchema(SchemaF[InputType]):
        def __init__(self, schema, *args, **kwargs):
            """
            Raises exception because this class should not be inherited.
            This class is helper only.
            """

            super().__init__(*args, **kwargs)
            self.schema = schema

        @post_load
        def make_object(self, data):
            return self.schema.load(data)

    class UserLoad:
        def load(self, data):
            return InputType(data)

    UserSche

# Generated at 2022-06-13 19:21:41.255474
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert SchemaF.loads(  # type: ignore
        '', many=False, partial=None, unknown=None, **dict()) == NotImplementedError  # type: ignore
    assert SchemaF.loads(  # type: ignore
        b'', many=False, partial=None, unknown=None, **dict()) == NotImplementedError  # type: ignore
    assert SchemaF.loads(  # type: ignore
        bytearray(), many=False, partial=None, unknown=None, **dict()) == NotImplementedError  # type: ignore


# Generated at 2022-06-13 19:21:44.353849
# Unit test for constructor of class _IsoField
def test__IsoField():
    try:
        _IsoField()
    except Exception as e:
        sys.stdout.write("Exception in _IsoField() with message: " + str(e) + "\n")
        raise


# Generated at 2022-06-13 19:22:04.156026
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import json
    from dataclasses import dataclass
    @dataclass
    class User:
        name: str = 'John Doe'
        email: str = 'jdoe@example.com'
        website: typing.Optional[str] = None

    class UserSchema(SchemaF[User]):
        name = fields.String()
        email = fields.Email()
        website = fields.Url(allow_none=True)

    user_schema = UserSchema()
    user, errors = user_schema.load({
        'email': 'foo@bar.com',
        'website': 'example.com',
        'unknown_field': 'this field is not defined on User'
    })

# Generated at 2022-06-13 19:22:12.616212
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():

    class Foo(typing.NamedTuple):
        a: int
        b: str

    class Bar(typing.NamedTuple):
        a: int
        b: str

    class MySchema(SchemaF[Foo]):
        a = fields.Int()
        b = fields.Str()

    class MySchema2(SchemaF[typing.Any]):
        a = fields.Int()
        b = fields.Str()

    assert MySchema().dump(Foo(a=1, b="test")) == {"a": 1, "b": "test"}

# Generated at 2022-06-13 19:22:19.676613
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import marshmallow_enum as me
    from typing import List, Dict, Union, Optional, Any, Tuple, Set, FrozenSet

    @dataclass
    class User:
        id: int
        name: str
        opt_name: Optional[str]

    @dataclass
    class Article:
        id: int
        title: str
        published: datetime
        user: User

    UserSchema = _user_overrides_or_exts(User)
    ArticleSchema = _user_overrides_or_exts(Article)

    assert UserSchema['name'].mm_field == fields.Str
    assert UserSchema['opt_name'].mm_field == fields.Str(allow_none=True)
    assert ArticleSchema['user'].mm_

# Generated at 2022-06-13 19:22:24.210574
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    l = [A]  # type: ignore
    SchemaF[A].dump(l, many=True)
    SchemaF[A].dump(l, many=False)
    SchemaF[A].dumps(l, many=True)
    SchemaF[A].dumps(l, many=False)


# Generated at 2022-06-13 19:22:35.588672
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    @dataclass_json
    @dataclass
    class B:
        b: typing.List[int] = []
    @dataclass_json
    @dataclass
    class A:
        a: typing.List[B] = []
    s = schema(A, None, False)
    assert s['a'].container is fields.List
    assert s['a']._nested.container is fields.List
    assert s['a']._nested._nested.__class__ is fields.Int
    assert s['a']._nested._nested.__class__ is fields.Int




# Generated at 2022-06-13 19:22:50.066450
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._deserialize(None, None, None) is None
    #_TimestampField()._deserialize(None, None, None, required=True)
    with pytest.raises(ValidationError):
        _TimestampField()._deserialize(None, None, None, required=True)
    assert _TimestampField()._serialize(None, None, None) is None
    #_TimestampField()._serialize(None, None, None, required=True)
    with pytest.raises(ValidationError):
        _TimestampField()._serialize(None, None, None, required=True)
    assert _TimestampField()._serialize(datetime.now(), None, None) > 1000000000  # int



# Generated at 2022-06-13 19:22:58.639051
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin
    @dataclass(init=False)
    class A(DataClassJsonMixin):
        a: int

    @dataclass(init=False)
    class B(DataClassJsonMixin):
        b: A
    type(schema(A, DataClassJsonMixin, False)) == dict
    type(schema(B, DataClassJsonMixin, False)) == dict
    assert len(schema(A, DataClassJsonMixin, False)) == 1
    assert len(schema(B, DataClassJsonMixin, False)) == 1
    assert schema(A, DataClassJsonMixin, False)['a'] == fields.Int

# Generated at 2022-06-13 19:23:05.891723
# Unit test for function build_type

# Generated at 2022-06-13 19:23:17.910019
# Unit test for function build_schema
def test_build_schema():
    from typing_extensions import TypedDict
    from datetime import datetime, date, time
    import numbers
    from dataclasses import dataclass


    class User(TypedDict):
        name: str
        age: int


    @dataclass
    class Root:
        user: User


    @dataclass
    class Root2:
        user: typing.Optional[User]
        name: str


    @dataclass
    class Intable:
        # TODO This case is not supported, because mm doesn't check if something is an intable
        number: numbers.Integral


    @dataclass
    class Floatable:
        number: numbers.Real



# Generated at 2022-06-13 19:23:22.849739
# Unit test for function build_schema
def test_build_schema():
    class Test(object):
        def __init__(self, value):
            self._value = value

        def __eq__(self, other):
            return isinstance(other, Test) and other._value == self._value

    @dataclass
    class TestDC(object):
        test: Test
        foo: str

    TestDC.schema().dump(TestDC(Test(1), 'foo'))

# Generated at 2022-06-13 19:23:46.202892
# Unit test for function schema
def test_schema():
    from .dataclasses import dataclass_json
    from dataclasses import dataclass

    @dataclass_json
    @dataclass
    class User:
        id: str
        name: str
        email: str = None
        password: str = None

    @dataclass_json
    @dataclass
    class User2:
        id: int
        name: str
        email: str = None
        password: str = None
        secret: str = None
        user: typing.Union[str, User]

    @dataclass_json
    @dataclass
    class TheNumber:
        number: typing.Union[int, float]

    @dataclass_json
    @dataclass
    class TheDate:
        date: datetime


# Generated at 2022-06-13 19:23:53.811279
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():  # type: ignore
    from dataclasses import dataclass

    @dataclass
    class Test:
        a: typing.List[int]

    import json

    schema = SchemaF[Test]()
    res = schema.dumps(Test(a=[1,2,3]), many=False)
    assert json.loads(res) == {'a': [1,2,3]}
    res = schema.dumps([Test(a=[1,2,3]), Test(a=[3,4,5])], many=True)
    assert json.loads(res) == [{'a': [1,2,3]}, {'a': [3,4,5]}]



# Generated at 2022-06-13 19:24:00.632027
# Unit test for constructor of class _IsoField
def test__IsoField():
    string_ = "2019-03-13T13:00:00"
    iso_field = _IsoField()
    iso_field.deserialize(string_)
    assert iso_field._deserialize(string_, "", "") == "2019-03-13 13:00:00"
    iso_field.serialize(string_)
    assert iso_field._serialize(string_, "", "") == "2019-03-13 13:00:00"



# Generated at 2022-06-13 19:24:05.598240
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Test:
        a: str = field(metadata={'dataclasses_json': {'letter_case': lambda x: x.upper()}})
        b: int = field(metadata={'dataclasses_json': {'letter_case': lambda x: x.lower()}})
    TestSchema = build_schema(Test, dataclass_json.DataClassJsonMixin, False, False)
    assert TestSchema.fields == ('A', 'B')
    assert len(TestSchema.__dict__) == 4
    assert 'A' in TestSchema.__dict__
    assert 'B' in TestSchema.__dict__
    assert TestSchema.A.attribute == 'a'
    assert TestSchema.B.attribute == 'b'


# Generated at 2022-06-13 19:24:17.133621
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass, field
    from typing import List, Optional

    from dataclasses_json import DataClassJsonMixin, dataclass_json, config

    @dataclass_json
    @dataclass
    class SomeClass(DataClassJsonMixin):
        name: str
        age: int = field(metadata={"dataclasses_json": {"marshmallow_field": fields.Float()}})
        some_id: Optional[int] = None
        some_lambda: List[str] = field(default_factory=lambda: [])

    schm = build_schema(SomeClass, DataClassJsonMixin, False, True)
    assert str(schm) is not None
    # assert issubclass(schm, Schema)

# Generated at 2022-06-13 19:24:20.925506
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A():
        a = 1
    s = SchemaF[A]()
    s.load([{'a': 1}, {'a': 1}])
    s.load({'a': 1}, many=False)
    s.load({'a': 1})
    s.load([{'a': 1}, {'a': 1}], many=False)

# Generated at 2022-06-13 19:24:29.835509
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses_json.mm import SchemaF
    from dataclasses import dataclass
    from typing import List

    @dataclass
    class User:
        user_id: int
        name: str

    @dataclass
    class Post:
        post_id: int
        user_id: int
        title: str
        content: str

    # Define serializers
    class UserSchema(SchemaF[User]):
        user_id = fields.Int()
        name = fields.Str()

    class PostSchema(SchemaF[Post]):
        post_id = fields.Int()
        user_id = fields.Int()
        title = fields.Str()
        content = fields.Str()


# Generated at 2022-06-13 19:24:40.850558
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class AType(SchemaF):
        a: str
        b: int
    assert AType.loads('{"a": "hello", "b": 5}') == AType(a="hello", b=5)



# Generated at 2022-06-13 19:24:48.904183
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str

    @dataclass
    class PersonList:
        people: typing.List[Person]

    class PersonSchema(SchemaF[Person]):
        name = fields.Str(required=True)

        @post_load
        def make(self, data, **kwargs):
            return Person(**data)

    class PersonListSchema(SchemaF[PersonList]):
        people = fields.Nested(PersonSchema, many=True, required=True)

        @post_load
        def make(self, data, **kwargs):
            return PersonList(**data)

    p_list_schema = PersonListSchema()

# Generated at 2022-06-13 19:24:58.702699
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow import SchemaF
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int

    class PersonSchema(SchemaF[Person]):
        name = fields.String()
        age = fields.Integer()

        @post_load
        def make_person(self, data, many, **kwargs):
            return Person(**data)

    data, err = PersonSchema().loads(None, many=True)
    data, err = PersonSchema().loads(None, many=False)

    d: typing.List[Person] = PersonSchema().loads(None, many=True)
    d: Person = PersonSchema().loads(None, many=False)

    PersonSchema().loads(None, many=False)

# Generated at 2022-06-13 19:25:12.434438
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert SchemaF[C].load([C().to_json()]) == [C()]


# Generated at 2022-06-13 19:25:20.190294
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from marshmallow import Schema, fields, post_load

    class UserSchema(SchemaF[User]):
        name = fields.Str()
        email = fields.Email()
        created_at = fields.DateTime()

        @post_load
        def make_object(self, data):
            return User(**data)

    json_data = {'name': 'Monty', 'email': 'monty@python.org',
                 'created_at': '2014-08-11T05:26:03.869245'}
    assert isinstance(json_data, dict), repr(json_data)
    data, errors = UserSchema().load(json_data)
    assert isinstance(data, User), repr(data)
    assert isinstance(errors, dict), repr(errors)

# Generated at 2022-06-13 19:25:20.743353
# Unit test for function build_schema
def test_build_schema():
    pass

# Generated at 2022-06-13 19:25:36.915930
# Unit test for function build_type

# Generated at 2022-06-13 19:25:48.356937
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class User:
        pass

    class UserSchema(SchemaF[User]):
        pass

    schema = UserSchema()
    assert isinstance(schema.dumps(User()), str)
    assert isinstance(schema.dumps([User()]), str)

    class User2:
        pass

    class User3:
        pass

    class User4:
        pass

    class User5:
        pass

    class UserSchema2(SchemaF[typing.Union[User2, User3]]):
        pass

    schema2 = UserSchema2()
    assert isinstance(schema2.dumps(User2()), str)
    assert isinstance(schema2.dumps(User3()), str)
    assert isinstance(schema2.dumps([User2()]), str)

# Generated at 2022-06-13 19:25:58.349559
# Unit test for function build_type
def test_build_type():
    assert not _is_optional(float)
    assert _is_optional(typing.Optional[float])
    assert _is_optional(typing.Union[type(None), float])
    assert not _is_optional(typing.List[float])
    assert _is_optional(typing.Optional[typing.List[float]])

    assert not _is_collection(float)
    assert not _is_collection(typing.Optional[float])
    assert not _is_collection(typing.Union[type(None), float])
    assert _is_collection(typing.List[float])
    assert _is_collection(typing.Optional[typing.List[float]])

    assert not _is_new_type(float)
    assert _is_new_type(typing.Optional[float])
    assert _is

# Generated at 2022-06-13 19:26:04.906225
# Unit test for function build_type
def test_build_type():
    from typing import TypeVar
    T = TypeVar('T')
    assert build_type(typing.Optional[int], {}, object, None, object) == \
        fields.Int(allow_none=True)
    assert build_type(typing.Optional[typing.List[T]], {}, object, None, object) \
        == fields.List(allow_none=True)
    assert build_type(typing.List[int], {}, object, None, object) == fields.List



# Generated at 2022-06-13 19:26:11.703039
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger a warning.
        SchemaF.load  # pylint: disable=pointless-statement
        # Verify some things
        assert len(w) == 1
        assert not isinstance(w[-1].message, DeprecationWarning)
        assert issubclass(w[-1].category, RuntimeWarning)
        assert "This class is helper only." in str(w[-1].message)
        assert "SchemaF.load" in str(w[-1].message)



# Generated at 2022-06-13 19:26:23.149911
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from uuid import uuid4
    from typing import List

    class TestSchema(SchemaF[List[uuid4]]):
        uuids = fields.List(fields.UUID)
        @post_load
        def make_test(self, data, **kwargs):
            return [uuid4()]
    s = TestSchema()
    obj = s.load({'uuids': ['8110b73a-7e9e-47d0-9b4f-4f7a73a09a87']})
    assert(s.__doc__ == 'Lift Schema into a type constructor')


if sys.version_info >= (3, 7):
    SchemaClass = SchemaF
else:
    class SchemaF(Schema):
        """Lift Schema into a type constructor"""

       

# Generated at 2022-06-13 19:26:26.014034
# Unit test for function build_schema
def test_build_schema():
    from dataclasses_json.exceptions import ConfigurationError
    class Mixin:
        pass
    s = build_schema(NamedTuple, Mixin, False, True)


# Generated at 2022-06-13 19:27:09.267504
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import json
    import datetime
    from typing import Optional

    from dataclasses import dataclass, field

    from dataclasses_json import DataClassJsonMixin, config
    from dataclasses_json.schema import SchemaF

    @dataclass
    class MyDataClass(DataClassJsonMixin):
        id: int
        date: Optional[datetime.datetime]
        name: str = 'default value'

    class MyDataClassSchemaF(SchemaF[MyDataClass]):
        class Meta:
            unknown = config.EXCLUDE
        id = fields.Int()
        name = fields.String()
        date = fields.DateTime()

    obj1 = MyDataClass(id=12, name='foo', date=datetime.datetime(2020, 12, 20))
    obj2

# Generated at 2022-06-13 19:27:11.088840
# Unit test for function build_type
def test_build_type():
    assert build_type(int, {}, None, None, None)



# Generated at 2022-06-13 19:27:18.749512
# Unit test for function schema
def test_schema():
    import marshmallow as mm
    import dataclasses
    import typing
    @dataclasses.dataclass
    class A:
        a: typing.Union[str, int]
        b: typing.Optional[str] = "hello"
        c: typing.List[str] = dataclasses.field(default_factory=list)
        d: typing.Dict[str, int] = dataclasses.field(default_factory=dict)
    s = schema(A, mm.Schema, True)
    assert isinstance(s['a'], _UnionField)
    assert isinstance(s['b'], fields.Str)
    assert fields.Str in s['a'].field.kwargs['oneof_schema'].values()

# Generated at 2022-06-13 19:27:25.757461
# Unit test for function build_schema
def test_build_schema():
    class A(MixinSchema):
        field2: str

    class B:
        field1: int = 0
        field3: typing.List[int] = [0, 1]
        field4: typing.Tuple[int, str]
        field5: typing.Optional[int] = None
        field6: typing.Union[int, str]

    _build_schema(cls=A, mixin=MixinSchema)
    _build_schema(cls=B)
    try:
        _build_schema(1)
    except TypeError:
        pass


if __name__ == '__main__':
    test_build_schema()

# Generated at 2022-06-13 19:27:35.524297
# Unit test for function build_type
def test_build_type():
    import unittest
    @dataclass_json
    @dataclass
    class Animal():
        zoo: str
        field_many = dataclasses.field(metadata={"mm_field": fields.Int})

    @dataclass_json
    @dataclass
    class Dog(Animal):
        name: str

    @dataclass_json
    @dataclass
    class Cat(Animal):
        age: int

    @dataclass_json
    @dataclass
    class Person:
        name: str
        location: Dog
        favourite_number: Dog
        favourite_number_optional: typing.Optional[Dog]
        pets: typing.List[Animal]
        pets_dict: typing.Dict[str, Animal]
        pets_union: typing.Union[Dog, Cat]


# Generated at 2022-06-13 19:27:45.517405
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    def t_loads(json_data: JsonData,
                many: bool = None, partial: bool = None, unknown: str = None,
                **kwargs) -> TOneOrMulti:
        return TOneOrMulti

    SchemaF.loads(test_loads)  # type: ignore



# Generated at 2022-06-13 19:27:48.922985
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    assert f._serialize(datetime.now()) is not None



# Generated at 2022-06-13 19:27:58.927833
# Unit test for function schema
def test_schema():
    import json
    import marshmallow
    import pytest
    from dataclasses import dataclass, asdict, field
    from dataclasses_json import dataclass_json, config, mm_field
    from marshmallow import fields as mm_fields

    @dataclass_json
    @dataclass
    class TestOptStr:
        a: typing.Optional[str] = field(default=None, metadata={'dataclasses_json': {
            "mm_field": mm_fields.Str(required=False)}})
        b: typing.Optional[str] = field(default=None, metadata={'dataclasses_json': {
            "mm_field": mm_fields.Str(required=False)}})

# Generated at 2022-06-13 19:28:07.273994
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from typing import Optional, List

    from marshmallow import Schema, fields


    @dataclass
    class Sub:
        name: str


    @dataclass
    class Foo:
        name: str
        sub: Optional[Sub]


    @dataclass
    class Bar:
        name: str


    @dataclass
    class Root:
        name: str
        foo: Foo
        bar: Optional[Bar]
        subs: List[Sub]


    schema = schema(Root, Schema, False)
    assert type(schema['foo']) == fields.Nested
    assert type(schema['subs']) == fields.List
    assert type(schema['bar']) == fields.Nested  # Bar does not inherit from schema

# Generated at 2022-06-13 19:28:14.199845
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import marshmallow as mm
    data = [{'s': 'a', 'i': 1}]
    schema = mm.Schema.from_dict(data)
    obj = schema.loads(schema.dumps(data))
    assert obj == data



# Generated at 2022-06-13 19:29:19.780087
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class Foo:
        pass

    class Bar:
        pass

    class Schema1(SchemaF[Foo]):
        pass

    class Schema2(SchemaF[Bar]):
        pass

    foo = Foo()
    out = Schema1().dump(foo)
    out = Schema1().dump([foo])
    out = Schema2().dump(foo)  # type: ignore
    out = Schema2().dump([foo])  # type: ignore


# Generated at 2022-06-13 19:29:22.549481
# Unit test for function build_type
def test_build_type():
    assert build_type(typing.Optional[int], {}, None, None, None) == TYPES[typing.Optional[int]]



# Generated at 2022-06-13 19:29:24.077037
# Unit test for function build_schema
def test_build_schema():
    assert isinstance(build_schema(User, None, False, False), type)
    assert issubclass(build_schema(User, None, False, False), Schema)


# Generated at 2022-06-13 19:29:37.733628
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class _SchemaF(SchemaF[A]):
        pass
    s = _SchemaF()
    result = s.dumps(1, many=None)
    assert result == '1'



# Generated at 2022-06-13 19:29:39.718653
# Unit test for function build_schema
def test_build_schema():
    class Dummy:
        pass

    # Test that it generates the same result as Marshmallow 3.2.2
    # The order of the fields is not guaranteed, but only equality matters
    assert build_schema(A, None, False, False) == build_schema(Dummy, None, False, False)

# Generated at 2022-06-13 19:29:49.042071
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, Field
    from dataclasses_json.api import mm_field

    t1 = typing.List[int]
    t2 = typing.List[typing.Optional[typing.Union[int, str]]]
    t3 = typing.Optional[typing.Union[int, str]]
    t4 = typing.Union[int, str, None]

    @dataclass
    class Data:
        a: t1 = mm_field(allow_none=False)
        b: t2 = mm_field(allow_none=True)
        c: t3 = mm_field(allow_none=True)
        d: t4 = mm_field(allow_none=True)

    from dataclasses_json.api import Schema
    from marshmallow import fields

# Generated at 2022-06-13 19:29:50.237634
# Unit test for function build_type
def test_build_type():
    build_type(A, {}, None, None, None)


# Generated at 2022-06-13 19:29:51.462683
# Unit test for function schema
def test_schema():
    assert schema.__name__ == 'schema'


# Generated at 2022-06-13 19:29:59.777709
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    """Test if the SchemaF method dump works properly"""
    class Example(object):
        a: int = 0
    s = SchemaF[Example]()
    o = Example()
    o.a = 1
    res2 = s.dump(o)
    assert res2['a'] == 1
    res1 = s.dump(o, many=True)
    assert res1[0]['a'] == 1
    res = s.dump([o])
    assert res[0]['a'] == 1



# Generated at 2022-06-13 19:30:06.360840
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from marshmallow import fields
    from dataclasses_json.mm_base import MMBase
    @dataclass
    class Coords(MMBase):
        lat: float
        lon: float
    @dataclass
    class City(MMBase):
        name: str
        population: int
        coords: Coords
    s = schema(City, MMBase, True)
    assert s['coords'].__class__ == fields.Nested