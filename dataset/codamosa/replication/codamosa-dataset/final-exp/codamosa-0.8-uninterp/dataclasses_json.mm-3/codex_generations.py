

# Generated at 2022-06-13 19:20:52.224932
# Unit test for function build_type
def test_build_type():
    from typing import Optional
    class A(int):
        pass

    assert _issubclass_safe(int, A)
    assert not _issubclass_safe(A, int)

    @dataclass_json
    @dataclass
    class B:
        a: A

    class X:
        pass

    @dataclass_json
    @dataclass
    class Y:
        x: Optional[X]
        y: Optional[X]

    @dataclass_json
    @dataclass
    class Z:
        y: Y

    class Obj:
        a: A

    a = Obj()
    assert is_dataclass(Obj)
    assert is_dataclass(a)
    assert not issubclass(A, dataclass_json)

# Generated at 2022-06-13 19:20:57.399987
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type: () -> None
    """Unittest for method dumps of class SchemaF"""
    class S(SchemaF[A]):
        def __init__(self):
            pass
    s = S()
    s.dumps(3, many=False)
    s.dumps([3], many=True)
    s.dumps(False)

# Generated at 2022-06-13 19:21:04.090427
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from typing import List
    from marshmallow import Schema, fields

    class InnerSchema(Schema):
        some_field = fields.Str()

        @post_load
        def make_object(self, data, **kwargs):
            # type: (dict, **str)->str
            return data['some_field']

    class OuterSchema(SchemaF[List[str]]):
        some_field = fields.Nested(InnerSchema, many=True)

    a = OuterSchema()
    b = a.dump(['1', '2'])
    assert b == [{'some_field': '1'}, {'some_field': '2'}]


# Generated at 2022-06-13 19:21:13.734135
# Unit test for function schema
def test_schema():

    class JsonMixin:
        @classmethod
        def schema(cls):
            return schema(cls, JsonMixin, infer_missing=True)

    @dataclass_json(mm_field=fields.Field(missing=None, allow_none=True))
    class A:
        a: typing.Optional[int]

    @dataclass_json(mm_field=fields.Field())
    class B:
        b: typing.Any

    @dataclass_json(mm_field=fields.String())
    class C:
        c: str

    @dataclass_json(mm_field=fields.DateTime(format="%Y-%m-%dT%H:%M:%S"))
    class D:
        d: datetime


# Generated at 2022-06-13 19:21:26.057716
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    # We mock the datetime.timestamp() method, so that we can test this field.
    # If the value passed to _TimestampField is a number, then we return it.
    # Else, we return an instance of datetime.
    def mock_timestamp(self):
        if type(self) == datetime:
            return self.hour
        else:
            return self

    datetime.timestamp = mock_timestamp

    # Retrieve the serialized version of a datetime object.
    ser_fld = _TimestampField().serialize(datetime(1, 1, 1, 1), "attr", "obj")
    # The serialized version of the datetime object should be the hour of the
    # object.
    assert ser_fld == 1

    # If the object passed is not a datetime, then the object itself should

# Generated at 2022-06-13 19:21:29.305346
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    pass



# Generated at 2022-06-13 19:21:34.441336
# Unit test for function build_type
def test_build_type():
    class User:
        name: str
        age: int

    user_schema = Schema.from_dataclass(User)
    assert build_type(typing.Union[str, int], {}, None, "name", User) == fields.Field()


# Generated at 2022-06-13 19:21:39.644966
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    def f(obj: typing.List[int],
          many: bool = None,
          *args, **kwargs) -> str:
        pass

    def g(obj: typing.List[int],
          many: bool = None) -> str:
        pass

    a = SchemaF.dumps
    assert f == a

    b = SchemaF.dumps
    assert g == b


# Generated at 2022-06-13 19:21:44.389979
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class A(typing.Generic[T]):
        pass

    aschema = SchemaF[A]
    # mypy error: Value of type variable "T" of "A" cannot be "int"
    a = A[int]() # type: ignore
    ares = aschema.dump(a)

    class B(typing.Generic[T]):
        pass

    bschema = SchemaF[B]
    # mypy error: Value of type variable "T" of "B" cannot be "int"
    b = B[int]() # type: ignore
    bres = bschema.dump(b)

    assert isinstance(ares, dict)
    assert isinstance(bres, dict)


# Generated at 2022-06-13 19:21:57.313542
# Unit test for function build_type
def test_build_type():
  class A:
    pass

  class B:
    pass

  class C(A, B):
    pass

  class D(datetime):
    pass

  assert build_type(int, {}, C, "test", C) == fields.Int
  assert build_type(float, {}, C, "test", C) == fields.Float
  assert build_type(typing.Dict, {}, C, "test", C) == fields.Dict
  assert build_type(C, {}, C, "test", C) == fields.Field
  assert build_type(A, {}, C, "test", C) == fields.Field
  assert build_type(B, {}, C, "test", C) == fields.Field
  assert build_type(D, {}, C, "test", C) == fields.Field




# Generated at 2022-06-13 19:22:23.441291
# Unit test for function build_schema
def test_build_schema():
    class Test1(metaclass=dataclass):
        test: str


# Generated at 2022-06-13 19:22:31.386386
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime.now(), None, None) is not None
    assert _TimestampField()._deserialize(None, None, None) is None
    assert _TimestampField()._deserialize(123, None, None) is not None
    assert _TimestampField()._deserialize(123.0, None, None) is not None


# Generated at 2022-06-13 19:22:35.574001
# Unit test for constructor of class _IsoField
def test__IsoField():
    assert _IsoField()._deserialize(
        '2019-07-17T20:52:14.684089', 'attr', 'data') == datetime(2019, 7, 17, 20, 52, 14, 684089)



# Generated at 2022-06-13 19:22:46.520954
# Unit test for function schema
def test_schema():
    from dataclasses_json.annotations import mm_field
    import marshmallow
    from dataclasses import dataclass
    from typing import Optional, Dict
    from dataclasses_json.core import _is_optional, _get_type_origin

    @dataclass
    class A(mm.Schema):
        a: int = mm_field(missing=None, allow_none=True)
        b: Optional[str] = mm_field(missing=None, allow_none=True)
        c: Optional[str] = mm_field(missing=None, allow_none=True)
        d: Optional[str] = mm_field(missing=None, allow_none=True)
        e: Optional[str] = mm_field(missing=None, allow_none=True)

# Generated at 2022-06-13 19:22:53.827740
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    f = _TimestampField()
    assert f._serialize(datetime.now(), "a", None)
    assert f._deserialize(None, "a", None) is None
    try:
        f._serialize(None, "a", None)
        raise AssertionError("Should raise ValidationError")
    except ValidationError:
        pass
    try:
        f._deserialize(None, "a", None, required=True)
        raise AssertionError("Should raise ValidationError")
    except ValidationError:
        pass



# Generated at 2022-06-13 19:23:00.580455
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # Setup
    class PersonSchema(SchemaF[dataclasses.dataclass.Person]):
        pass
    # Test
    PersonSchema().dump([dataclasses.dataclass.Person("person", 30, 30.2)])
    PersonSchema(many=True).dumps([dataclasses.dataclass.Person("person", 30, 30.2)])
    PersonSchema().dumps(dataclasses.dataclass.Person("person", 30, 30.2))

# Generated at 2022-06-13 19:23:11.357539
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    import typing
    @dataclass
    class A:
        name : str
        name2 : str = 'def'
    @dataclass
    class B:
        name : str = 'def'
        name2 : str = 'def2'
    @dataclass
    class C:
        name : str = 'def'
        name2 : typing.List[str] = 'def2'
    @dataclass
    class D:
        name : str = 'def'
        name2 : typing.Union[int, str] = 'def2'
    @dataclass
    class F:
        name : str = 'def'
        name2 : typing.Optional[int] = None
        name3 : typing.Optional[C] = None

# Generated at 2022-06-13 19:23:19.468994
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class User:
        def __init__(self, id: int, name: str):
            self.id = id
            self.name = name

    class UserSchema(SchemaF[User]):
        id = fields.Int()
        name = fields.Str()

        @post_load
        def create_user(self, data, **kwargs):
            return User(**data)

    schema = UserSchema()
    user = schema.load({'id': 1, 'name': 'nick'})
    assert user.id == 1
    assert user.name == 'nick'



# Generated at 2022-06-13 19:23:21.896850
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert SchemaF.load


# Generated at 2022-06-13 19:23:25.976645
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Person:
        name: str = 'John Doe'
        age: int = 0

    assert 'name' in build_schema(Person, dataclass_json(), True, False).__dict__



# Generated at 2022-06-13 19:23:44.550071
# Unit test for function build_schema
def test_build_schema():
    assert issubclass(build_schema(str, None, True, True), Schema)



# Generated at 2022-06-13 19:23:49.706711
# Unit test for function schema
def test_schema():
    @dataclass
    class A:
        d: fields.Decimal
        x: typing.Optional[Decimal] = 1.1
        z: fields.Raw = 'raw'
        r: typing.Optional[str] = 'r1'
        t: typing.Union[str, int] = 1
        f: typing.Callable = lambda x: x
        y: typing.Optional[typing.List[int]] = [1, 2, 3]
        u: typing.Union[int, str] = 'str'
        v: typing.Union[str, int] = 1
        e: fields.Email
        j: typing.Optional[str] = None
        q: typing.Dict[str, int] = {'key': 1}

# Generated at 2022-06-13 19:24:00.145509
# Unit test for function schema
def test_schema():
    import pytest
    from dataclasses_json.api import _SchemaDecoder

    class _JsonMixin:
        @classmethod
        def schema(cls) -> Schema:
            raise NotImplementedError()

    @_handle_undefined_parameters_safe
    class _MySchema(Schema):
        class Meta:
            unknown = EXCLUDE

    _decoder = _SchemaDecoder(decode_from_schema=True,
                              decoder_cls=_MySchema,
                              infer_missing=True)

    class T1(metaclass=_decoder.meta_from_decorated):
        a: int

        @classmethod
        def json_schema(cls):
            return schema(cls, _JsonMixin, True)

        schema

# Generated at 2022-06-13 19:24:01.717983
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    _TimestampField()
    assert _TimestampField() is not None


# Generated at 2022-06-13 19:24:05.302262
# Unit test for function build_type
def test_build_type():
    result = build_type(typing.List[typing.Dict[str, int]], {}, mixin=None, field=None, cls=None)
    assert isinstance(result, fields.List)



# Generated at 2022-06-13 19:24:06.255472
# Unit test for function build_type
def test_build_type():
    assert True

# Generated at 2022-06-13 19:24:12.059079
# Unit test for function schema
def test_schema():
    from dataclasses_json.api import dataclass_json
    from dataclasses import dataclass
    @dataclass
    class A:
        pass

    @dataclass_json
    @dataclass
    class B:
        a: A

    @dataclass_json
    @dataclass
    class C:
        b: B

    assert schema(C, dataclass_json, False) is not None



# Generated at 2022-06-13 19:24:17.013160
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        name: str

    schema = SchemaF[MyClass]()

    instance = MyClass('test')
    serialized = schema.dumps([instance])

    assert serialized == '[{"name": "test"}]'



# Generated at 2022-06-13 19:24:26.051737
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass

    @dataclass
    class User:
        id: int
        username: str
        first_name: str = 'John'
        last_name: str = 'Doe'
        is_active: bool = True

        @property
        def full_name(self):
            return f'{self.first_name} {self.last_name}'

        @property
        def is_staff(self):
            return self.username == 'admin'

    class UserSchema(SchemaType):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, strict=True, **kwargs)


# Generated at 2022-06-13 19:24:31.935349
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass

    @dataclass
    class A:
        x: str = 'str'
        y: int = 1

    S = SchemaF[A]({'x': fields.Str(), 'y': fields.Int()})
    res: TEncoded
    res = S.dump(A())
    str_type = type(res['x'])
    assert str_type == str



# Generated at 2022-06-13 19:25:01.756362
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from marshmallow_dataclass import class_schema

    @dataclass
    class A:
        a: int
        b: str = None
    # TODO This should also be a test for schema declaration, this cannot be done now, as we cannot import dataclass
    A_Schema = class_schema(A)
    assert isinstance(A_Schema().fields['a'], fields.Int)
    assert isinstance(A_Schema().fields['b'], fields.Str)
    assert 'b' in A_Schema().dump({'a': 5}).keys()
    assert A_Schema().dump({'a': 5}) == {'a': 5, 'b': None}



# Generated at 2022-06-13 19:25:07.340779
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Foo:
        pass

    class FooSchema(SchemaF[Foo]):
        pass

    assert isinstance(FooSchema.loads([], many=True), typing.List[Foo])
    assert isinstance(FooSchema.loads({}, many=True), typing.List[Foo])

    assert isinstance(FooSchema.loads({}, many=False), Foo)
    assert isinstance(FooSchema.loads('{}', many=False), Foo)



# Generated at 2022-06-13 19:25:12.105096
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    @dataclasses.dataclass
    class Person:
        name: str

    class PersonSchema(marshmallow.SchemaF[Person]):
        name = marshmallow.fields.String()

    data = Person("Peter")
    s = PersonSchema()
    r = s.dumps(data)
    assert r == '{"name": "Peter"}'



# Generated at 2022-06-13 19:25:19.944166
# Unit test for function schema
def test_schema():
    import marshmallow.fields
    import marshmallow_enum
    from dataclasses import dataclass, field
    from marshmallow import Schema
    from dataclasses_json import dataclass_json, config, DataClassJsonMixin
    from typing_inspect import is_optional_type, is_union_type

    def test_schema_creation(cls, mixin, infer_missing, expected_schema):
        assert schema(cls, mixin, infer_missing) == expected_schema

    @dataclass
    class EnumExample(str, Enum):
        ONE = 'one'
        TWO = 'two'
        THREE = 'three'

    @dataclass
    class Nested(DataClassJsonMixin):
        name: str
        age: int = 18


# Generated at 2022-06-13 19:25:25.868496
# Unit test for function schema
def test_schema():
    from marshmallow import fields
    import typing
    import dataclasses

    @dataclasses.dataclass
    class DC:
        value: int
        n: int = dataclasses.field(default=10, metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        default: int = dataclasses.field(metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        default_factory: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dataclasses_json': {'mm_field': fields.Int()}})

    assert len(schema(DC, None, False)) == 3
    assert schema(DC, None, False).get('value') is None
    assert schema(DC, None, False).get

# Generated at 2022-06-13 19:25:38.299561
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclasses.dataclass
    class A:
        x: int = dataclasses.field(metadata={'marshmallow_field': fields.Str()})

    @dataclasses.dataclass
    class B:
        y: str = dataclasses.field(metadata={'marshmallow_field': fields.Str()})

    mapper = typing.Mapping[str, typing.Type[typing.TypeVar('X')]]
    dc_to_schema = {
        A: T.Schema,
        B: T.Schema.__args__[0]
    }
    from dataclasses_json.schema import _Schema

# Generated at 2022-06-13 19:25:46.927111
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class A:
        a: str
        b: int = field(metadata={'dataclasses_json': {"mm_field": fields.Field()}})

    s = build_schema(A, dataclasses_json.DataClassJsonMixin, False, False)

    assert s.schema.fields == {'a': fields.Field(allow_none=False, missing=fields.missing), 'b': fields.Field(allow_none=False, missing=fields.missing)}
    assert s.schema.required == ['a']



# Generated at 2022-06-13 19:25:47.800347
# Unit test for constructor of class _IsoField
def test__IsoField():
    pass



# Generated at 2022-06-13 19:25:57.883313
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A(typing.Generic[A]):
        @classmethod
        def load(cls, data: TOneOrMultiEncoded,
                 many: bool = None, partial: bool = None,
                 unknown: str = None) -> TOneOrMulti:
            pass

    class B(typing.Generic[A]):
        @classmethod
        def load(cls, data: TOneOrMultiEncoded, many: bool = None,
                 partial: bool = True, unknown: str = None) -> TOneOrMulti:
            pass

    class C(typing.Generic[A]):
        @classmethod
        def load(cls, data: TOneOrMultiEncoded, many: bool = False,
                 partial: bool = None, unknown: str = None) -> TOneOrMulti:
            pass


# Generated at 2022-06-13 19:26:00.143159
# Unit test for constructor of class _IsoField
def test__IsoField():
    try:
        _IsoField()
    except NotImplementedError as e:
        assert 0, "not valid _IsoField Test 1,{}".format(e)


# Generated at 2022-06-13 19:26:51.624026
# Unit test for function schema
def test_schema():
    @dataclass_json
    @dataclass
    class C:
        x: typing.List[int]
        y: typing.Dict[str, int]
        z: typing.Union[int, str]
    # mypy error because the schema() function uses a recursive type
    # that mypy does not support, so we have to ignore the wrong return type
    C_schema: Schema = schema(C, Schema, True)  # type: ignore

    assert isinstance(C_schema['x'], fields.List)
    assert isinstance(C_schema['y'], fields.Dict)
    assert isinstance(C_schema['z'], _UnionField)
    assert C_schema['x'].container == int
    assert C_schema['y'].keys == str
    assert C_

# Generated at 2022-06-13 19:27:02.341669
# Unit test for function schema
def test_schema():
    import unittest.mock as mock
    import unittest

    class MyField(fields.Field):
        pass

    class MyMixin:
        pass

    class MySchema(SchemaType, MyMixin):
        pass

    @dataclass_json(mm_field=MyField())
    @dataclass
    class MyDC:
        a: int
        b: datetime

    schema = schema(MyDC, MyMixin, True)
    assert isinstance(schema["a"], fields.Int)
    assert isinstance(schema["b"], fields.Field)

    @dataclass_json(mm_field=MyField())
    @dataclass
    class MyDC2:
        a: typing.Optional[datetime]

    schema = schema(MyDC2, MyMixin, True)
   

# Generated at 2022-06-13 19:27:07.701054
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class A(typing.Generic[A]):
        def dumps(self, obj: typing.List[A], many: bool = None, *args,
                      **kwargs) -> str:
            pass



# Generated at 2022-06-13 19:27:13.279840
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class Test(SchemaF[str]):
        pass

    obj = 'str'
    res = Test().dumps(obj)
    assert isinstance(res, str)

    objs = ['str', 'str', 'str']
    res = Test().dumps(objs, many=True)
    assert isinstance(res, str)



# Generated at 2022-06-13 19:27:23.203365
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import is_dataclass
    import inspect
    import marshmallow as ma
    import marshmallow.fields as ma_fields
    import typing
    import unittest

    def is_not_skip_dc(dc):
        return not inspect.isclass(dc) or (inspect.isclass(dc) and is_dataclass(dc))

    def get_ma_types(fields_):
        return (dict(f.__dict__) for f in
                [type(field) for _, field in fields_.items()])

    def get_ma_type_name(fields_):
        return [f.__name__ for f in get_ma_types(fields_)]


# Generated at 2022-06-13 19:27:26.486308
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():

    schema = SchemaF[List[int]]()
    value = schema.loads('[1, 2, 3]')

    assert(value) == [1, 2, 3]


# Generated at 2022-06-13 19:27:31.691956
# Unit test for function build_type
def test_build_type():
    type_ = typing.Optional[int]
    options = {}
    mixin = mixin_for_dict_serialization_uid()
    field = dc_fields(Example1)[0]
    cls = Example1
    assert build_type(type_, options, mixin, field, cls) == fields.Int(allow_none=True)



# Generated at 2022-06-13 19:27:38.603205
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class TestSchemaSchemaF(SchemaF[int]):
        pass

    obj: typing.List[int] = [1, 2]
    schema = TestSchemaSchemaF()
    assert schema.dump(obj) == [1, 2] # type: ignore
    assert schema.dump(obj, many=True) == [1, 2] # type: ignore
    assert schema.dump(obj, many=False) == [1, 2] # type: ignore
    assert schema.dump(obj, many=None) == [1, 2] # type: ignore

    obj: int = 3
    schema = TestSchemaSchemaF()
    assert schema.dump(obj) == 3 # type: ignore
    assert schema.dump(obj, many=False) == 3 # type: ignore
    assert schema.dump(obj, many=None)

# Generated at 2022-06-13 19:27:47.004030
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from typing import Union, List, Dict
    from marshmallow import fields, Schema

    class Model(SchemaF[Model]):
        id = fields.Str()

    assert isinstance(Model.load({"id": "123"}), Model)
    assert isinstance(Model.load([{"id": "321"}], many=True), List[Model])
    assert isinstance(Model.load([{"id": "321"}]), Union[Model, List[Model]])
    assert isinstance(Model.load({}), Model)
    assert isinstance(Model.load({}, partial=True), Model)
    assert isinstance(Model.load({"foo": "bar"}, unknown="EXCLUDE"), Model)
    assert isinstance(Model.load([], many=True), List[Model])

# Generated at 2022-06-13 19:27:56.861041
# Unit test for function build_type
def test_build_type():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert build_type((int, ), {}, None, None, None)((B, ), {}) == \
           build_type((A, ), {}, None, None, None)((B, ), {})

    assert build_type((A, ), {}, None, None, None)((C, ), {}) == \
           build_type((A, ), {}, None, None, None)((B, ), {})

    assert build_type((B, ), {}, None, None, None) == \
           build_type((C, ), {}, None, None, None)