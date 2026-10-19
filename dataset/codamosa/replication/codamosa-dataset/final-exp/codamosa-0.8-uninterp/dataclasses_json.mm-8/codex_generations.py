

# Generated at 2022-06-13 19:20:52.641493
# Unit test for function build_type
def test_build_type(): # type: ignore
    import uuid
    from typing import Optional
    from marshmallow.validate import Equal
    from marshmallow.validate import OneOf
    from datetime import time
    from marshmallow.fields import Nested, Field

    assert isinstance(
        build_type(
            uuid.UUID, {}, None, None, None), fields.UUID)

    assert isinstance(
        build_type(
            datetime, {}, None, None, None), _TimestampField)

    assert isinstance(
        build_type(
            typing.Tuple, {}, None, None, None),
        fields.Tuple)

    assert isinstance(
        build_type(
            typing.List, {}, None, None, None),
        fields.List)


# Generated at 2022-06-13 19:20:55.361783
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    data = [{'__type': 'T', 'value': 1}]
    SchemaF[T].load(data)[0].value == 1

# Generated at 2022-06-13 19:21:00.328743
# Unit test for function build_schema
def test_build_schema():
    from dataclasses_json.core import make_encoder, make_decoder, \
        make_schema, make_encoder_with_schema, make_decoder_with_schema, global_config
    from dataclasses_json.test_utils import is_encoder, is_decoder, is_schema, \
        is_json_decoder, is_json_encoder, is_json_decoder_with_schema, \
        is_json_encoder_with_schema

    class DataClass:
        pass

    '''
    @Schema.from_dict
    @dataclass
    class DataClass:
        f1: int
        f2: str = 'abc'
    '''
    assert is_schema(make_schema(DataClass))

    assert is_encoder

# Generated at 2022-06-13 19:21:01.268301
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()



# Generated at 2022-06-13 19:21:10.349400
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    class User(typing.NamedTuple):
        id: int
        name: str

    class UserSchema(SchemaF[User]):
        id = fields.Int(required=True)
        name = fields.String(required=True)

    u, u2 = User(1, "Max"), User(2, "John")
    assert UserSchema().dump(u) == {'id': 1, 'name': "Max"}
    assert UserSchema().dump(u, many=False) == {'id': 1, 'name': "Max"}
    assert UserSchema().dump([u, u2]) == [{'id': 1, 'name': "Max"}, {'id': 2, 'name': "John"}]

# Generated at 2022-06-13 19:21:20.215692
# Unit test for function build_type
def test_build_type():
    import typing
    import marshmallow_dataclass as md
    from marshmallow import Schema, fields
    from dataclasses import dataclass, field

    @dataclass
    class MyData:
        a: int = 1
    @dataclass
    class MyDataSchema(Schema):
        a = fields.Int()
    
    class MyEnum(Enum):
        A = 3
        B = 4

    @dataclass
    class MyData2:
        a: typing.List[MyData]
        b: typing.List[dict]
        e: typing.Dict[int, typing.List[int]]
        f: typing.SupportVar[MyData]

    @dataclass
    class MyData3:
        options: typing.Dict[str, str]


# Generated at 2022-06-13 19:21:26.278810
# Unit test for function schema
def test_schema():
    class Param(Schema):
        parameter_name: str
        parameter_type: typing.Union[str, list]
        value: typing.Union[int, dict, str]
        notes: typing.Optional[str]
        default_value: typing.Optional[bool] = None

    assert (schema(Param, object, False) == {
        'parameter_name': fields.Str(),
        'parameter_type': fields.Field(),
        'value': fields.Field(),
        'notes': fields.Field(allow_none=True, missing=None),
        'default_value': fields.Field(allow_none=True, missing=None)
    })



# Generated at 2022-06-13 19:21:38.830647
# Unit test for function build_type
def test_build_type():
    from marshmallow import fields, Schema
    from dataclasses import dataclass
    from dataclasses_json.annotations import _type_from_annotation
    from dataclasses_json import DataClassJsonMixin
    import typing
    @dataclass
    class Test(DataClassJsonMixin):
        test: typing.List[str]

    @dataclass
    class Test2(DataClassJsonMixin):
        test: typing.List[Test]

    t1 = Test2(test=[Test(test=['a','b','c'])])
    result = build_type(t1.test[0].test[0].__class__, {}, DataClassJsonMixin,
        _type_from_annotation(Test2.test), Test2)
    assert isinstance(result, fields.String)

# Generated at 2022-06-13 19:21:43.340367
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import marshmallow
    import marshmallow_dataclass
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class User:
        name: str
        age: int

    schema = SchemaF[User]({'name': fields.Str(), 'age': fields.Int()})
    user = User('Test1', 20)
    encoded = schema.dump(user)
    decoded = schema.load(encoded)
    assert decoded == user
    encoded = schema.loads(marshmallow.json.dumps(encoded))
    decoded = schema.load(encoded)
    assert decoded == user



# Generated at 2022-06-13 19:21:44.352100
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    pass


# Generated at 2022-06-13 19:22:08.654189
# Unit test for function build_type
def test_build_type():
    """ Assert that build_type returns proper fields based on type."""
    assert str(build_type(str, {})) == "<class 'str'>"
    assert str(build_type(int, {})) == "<class 'int'>"
    assert str(build_type(float, {})) == "<class 'float'>"
    assert str(build_type(bool, {})) == "<class 'bool'>"
    assert str(build_type(dict, {})) == "<class 'dict'>"
    assert str(build_type(list, {})) == "<class 'list'>"
    assert str(build_type(uuid.uuid4, {})) == "<class 'uuid.UUID'>"
    assert str(build_type(schema.Integer, {})) == "<class 'marshmallow.fields.Integer'>"

# Generated at 2022-06-13 19:22:16.433521
# Unit test for constructor of class _IsoField
def test__IsoField(): # pylint: disable=unused-argument
    class Foo:
        def __init__(self, dt):
            self.dt = dt
    class Bar:
        def __init__(self, dt=None):
            self.dt = dt
    a = Foo(dt=datetime.now())
    b = Bar(dt=datetime.now())
    c = Foo(dt=None)
    d = Bar(dt=None)
    assert _IsoField().serialize(a) == a.dt.isoformat()
    assert _IsoField().serialize(b) == b.dt.isoformat()
    assert _IsoField().serialize(c) is None
    assert _IsoField().serialize(d) is None



# Generated at 2022-06-13 19:22:20.227706
# Unit test for constructor of class _IsoField
def test__IsoField():
    test_val = None
    test_attr = 'attr'
    test_obj = None
    test_kwargs = {}
    test_field = _IsoField()
    if test_field._serialize(test_val, test_attr, test_obj, **test_kwargs) is None:
        return
    else:
        return
                                                                      

# Generated at 2022-06-13 19:22:21.847467
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    if f is None:
        # if the constructor returns None, it means that the test has failed
        assert False


# Generated at 2022-06-13 19:22:36.088670
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    json_data = b"[1, 2, 3]"
    dt = SchemaF().loads(json_data, many=True, variant_value=1, variant_name='abcd')
    assert dt == [1, 2, 3]
    dt = SchemaF().loads(json_data, variant_value=1, variant_name='abcd')
    assert dt == [1, 2, 3]

# Generated at 2022-06-13 19:22:44.522919
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import Schema
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class _A:
        a: int

    class _Schema(_SchemaF[TypeVar('_B')]):
        pass

    _SA = _Schema.from_dataclass(_A)
    assert _SA.dumps(None) is None
    _SA.dumps(None)



# Generated at 2022-06-13 19:22:51.552517
# Unit test for function build_schema
def test_build_schema():
    from .mixins import from_json
    from .fields import from_json_inherit

    @from_json
    @dataclass
    class A:
        x: int
        y: typing.Optional[float]
        z: str = "zzz"
        zz: str = field(default_factory=lambda: "zzzz")

    @dataclass
    class B(A, dataclass_json=from_json_inherit):
        u: int
        v: typing.Optional[float]

        @property
        def w(self):
            return self.u

        @w.setter
        def w(self, value):
            self.u = value

        @w.deleter
        def w(self):
            del self.u


# Generated at 2022-06-13 19:22:58.744649
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Bar:
        bar: int
        bar2: str

    @dataclass
    class Foo(JSONDataclassMixin):
        foo: int
        bar: Bar
        fo3: str = 3

    class FooSchema(Schema):
        foo = fields.Int()
        bar = fields.Nested(BarSchema)
        fo3 = fields.Int()

    assert build_schema(Foo, JSONDataclassMixin, False) == FooSchema



# Generated at 2022-06-13 19:23:06.683154
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Test:
        pass

    Test().__module__ = None

    TestSchema = build_schema(Test, EmptyMixin, False, False)

    assert TestSchema().fields.keys() == dict()

    @dataclass
    class Test:
        i: int

    Test().__module__ = None

    TestSchema = build_schema(Test, EmptyMixin, False, False)

    assert TestSchema().dump(Test(1)).keys() == {"i"}

    @dataclass
    class Test:
        i: int

    Test().__module__ = None

    TestSchema = build_schema(Test, EmptyMixin, True, False)

    assert TestSchema().dump(Test(1)).keys() == {"i"}

# Generated at 2022-06-13 19:23:18.683908
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin
    from marshmallow import Schema

    @dataclass
    class Foo(DataClassJsonMixin):
        a: str
        b: int

    class_name = Foo.__name__

    built_schema = build_schema(Foo, DataClassJsonMixin, False, False)
    assert (isinstance(built_schema, type) and issubclass(built_schema, Schema))
    assert (built_schema.__name__ == f'{class_name.capitalize()}Schema')
    assert (built_schema.Meta.fields == ('a', 'b'))
    assert (built_schema.make_foo)
    assert (built_schema.dumps)


# Generated at 2022-06-13 19:24:00.804897
# Unit test for function build_schema
def test_build_schema():
    pass



# Generated at 2022-06-13 19:24:10.437135
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    datatype = typing.TypeVar('datatype')
    class TestClass(typing.Generic[datatype]):  # noqa
        def test(self, in_obj: TOneOrMultiEncoded, many: bool = None, partial: bool = None, unknown: str = None):  # type: ignore
            # mm has the wrong return type annotation (dict) so we can ignore the mypy error
            # for the return type overlap
            SchemaF[datatype].load(in_obj, many=many, partial=partial, unknown=unknown)  # noqa
    # Unit test for method loads of class SchemaF

# Generated at 2022-06-13 19:24:12.457790
# Unit test for function build_type
def test_build_type():
    a = build_type(str, {}, None, None, None)
    assert a([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 19:24:22.467655
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    assert field._serialize(datetime.fromisoformat("2019-01-01"), None, None, None).endswith("+00:00")
    assert field._deserialize("2019-01-01T00:00:00+00:00", None, None, None).isoformat().endswith("+00:00")
    field.required = True
    assert field._serialize(None, None, None, None) is None
    assert field._deserialize(None, None, None, None) is None
    try:
        field._serialize(None, None, None, None, required=True)
        assert False
    except ValidationError:
        pass


# Generated at 2022-06-13 19:24:23.496150
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()


# Generated at 2022-06-13 19:24:31.270657
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # mypy: ignore
    @dataclass_json
    @dataclass
    class P:
        id: int = field(metadata=dict(data_key='p_id'))
        name: str = field(metadata=dict(data_key='p_name'))

    schema = SchemaF[P]()

    d = {'p_id': 123, 'p_name': 'peter_pan'}

    p: P = schema.load(d, many=False)
    assert isinstance(p, P)

    ds = [d]
    ps: typing.List[P] = schema.load(ds, many=True)
    assert isinstance(ps, list)
    assert all(isinstance(p, P) for p in ps)

    p = schema.load(ds, many=False)


# Generated at 2022-06-13 19:24:31.853556
# Unit test for method load of class SchemaF
def test_SchemaF_load(): pass  #  Because mypy cannot understand this class

# Generated at 2022-06-13 19:24:34.339002
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow.schema import Schema  # type: ignore
    g = SchemaF.dump(SchemaF[int](), [1, 2, 3])

# Generated at 2022-06-13 19:24:45.324385
# Unit test for function build_schema
def test_build_schema():
    # Test the function with a simple dataclass
    @dataclass
    class A:
        a: str
    assert isinstance(build_schema(A, None, False, False), type)
    assert 'a' in build_schema(A, None, False, False).__dict__
    assert build_schema(A, None, False, False).__dict__['a'].data_key == 'a'
    assert isinstance(build_schema(A, None, False, False).__dict__['a'], fields.Field)
    assert build_schema(A, None, False, False).Meta.fields == ('a',)

    # Test optional field
    @dataclass
    class B:
        a: str
        b: typing.Optional[str]

# Generated at 2022-06-13 19:24:52.342002
# Unit test for function schema
def test_schema():
    from pytest import fixture

    @fixture
    def cls():
        from dataclasses import dataclass, field

        from dataclasses_json.mm import SchemaMixin

        @dataclass
        class Tmp(SchemaMixin):
            var: str = field(default='something')
            var2: int

        return Tmp

    def test_schema(cls):
        schema = cls.schema()
        assert schema['var'] == fields.Str()
        assert schema['var2'] == fields.Int()



# Generated at 2022-06-13 19:25:49.557033
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Foo(typing.NamedTuple):
        a: str
        b: int

    assert SchemaF[Foo].loads('{"a": "foo", "b": 2}') == Foo('foo', 2)

    assert SchemaF[Foo].loads('[{"a": "foo", "b": 2}]') == [Foo('foo', 2)]

    assert SchemaF[typing.List[Foo]].loads('[{"a": "foo", "b": 2}]') == [Foo('foo', 2)]

    assert SchemaF[Foo].loads('{"a": "foo", "b": 2}', many=False) == Foo('foo', 2)


# Generated at 2022-06-13 19:25:59.333383
# Unit test for function schema
def test_schema():
    assert len(schema(dict, dict, False)) > 1
    assert len(schema(list, list, False)) > 1
    assert len(schema(set, set, False)) > 1
    assert len(schema(str, str, False)) > 1
    assert len(schema(int, int, False)) > 1
    assert len(schema(float, float, False)) > 1
    assert len(schema(bool, bool, False)) > 1
    assert len(schema(dict, dict, True)) > 1
    assert len(schema(list, list, True)) > 1
    assert len(schema(set, set, True)) > 1
    assert len(schema(str, str, True)) > 1
    assert len(schema(int, int, True)) > 1

# Generated at 2022-06-13 19:26:07.129830
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from unittest.mock import MagicMock

    schemaMock = MagicMock(Schema)
    d = datetime(2020, 5, 17, 6, 52, 8, 477000)
    obj = d
    dump_func = lambda obj, many: ['haha']

    schemaMock._dump = dump_func
    schema = SchemaF(schema_class=schemaMock)
    # obj: typing.List[A], many: bool = None
    assert schema.dump([obj], many=True) == ['haha']
    # obj: typing.List[A], many: bool = None
    assert schema.dump(obj, many=False) == 'haha'



# Generated at 2022-06-13 19:26:15.583346
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class _Obj1:
        def __init__(self, a: int):
            self.a = a
    class _Obj2:
        def __init__(self, b: int):
            self.b = b
    class _Obj3:
        def __init__(self, c: int):
            self.c = c
    class _ObjSchema(SchemaF[_Obj1]):
        a = fields.Int()
    class _ObjSchema2(SchemaF[_Obj2]):
        b = fields.Int()
    class _ObjSchema3(SchemaF[_Obj3]):
        c = fields.Int()

    assert SchemaF[_Obj1].load({'a': 1}) == _Obj1(a=1)
    assert SchemaF[_Obj2].load({'b': 1}) == _

# Generated at 2022-06-13 19:26:24.773865
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()

    if sys.version_info.major == 3 and sys.version_info.minor < 8:
        from datetime import date
        expected = date.today().timestamp()
        dt = datetime.fromtimestamp(expected)
        assert field.deserialize(expected) == dt
        assert field.serialize(dt) == expected
    else:
        expected = datetime(2000, 1, 1, 14, 29, 59, 999999)
        assert field.deserialize(expected.timestamp()) == expected
        assert field.serialize(expected) == expected.timestamp()



# Generated at 2022-06-13 19:26:36.839956
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Foo(typing.Generic[A], SchemaF[A]):
        pass
    assert str(Foo.loads.__annotations__['json_data']) == "typing.Union[str, bytes, bytearray]"
    assert str(Foo.loads.__annotations__['many']) == "typing.Optional[bool]"
    assert str(Foo.loads.__annotations__['partial']) == "typing.Optional[bool]"
    assert str(Foo.loads.__annotations__['unknown']) == "typing.Optional[str]"
    assert str(Foo.loads.__annotations__['return']) == "typing.Any"

# Generated at 2022-06-13 19:26:47.666755
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import SchemaFlags
    class Foo:
        pass
    class Bar:
        pass
    class FooBarSchema(SchemaF[Foo|Bar]):
        data = fields.Function(lambda instance: instance)
    value = 'bar'
    res = FooBarSchema().dump(Bar(data=value))
    assert res is not None
    assert type(res) is dict
    assert res['data'] is value

    res = FooBarSchema().dump([Bar(data=value)])
    assert res is not None
    assert type(res) is list
    assert res[0]['data'] is value

    res, errors = FooBarSchema().dump([Bar(data=value)], many=False)
    assert res is not None
    assert errors is not None
    assert type(res) is dict
   

# Generated at 2022-06-13 19:26:56.685343
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class TestSchema(SchemaF[str]):
        pass
    TestSchema().loads('test') # type: str


# Generated at 2022-06-13 19:27:03.598761
# Unit test for function build_type
def test_build_type():
    _is_new_type = False
    class Test:
        pass
    class Test2:
        pass
    type_ = Test
    options = {}
    mixin = Test2
    field = fields
    cls = object
    options['field_many'] = bool(
        _is_supported_generic(field.type) and _is_collection(
            field.type))
    assert build_type(type_, options, mixin, field, cls) == fields.Nested(type_.schema(), **options)



# Generated at 2022-06-13 19:27:11.216853
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    from marshmallow_dataclass import class_schema, add_schema
    from datetime import datetime

    # Fields for testing if _TimestampField._deserialize function works
    def test_deserialize_ts(ts):
        return _TimestampField()._deserialize(ts, None, None)

    def test_deserialize_dt(dt):
        return _TimestampField()._deserialize(dt, None, None)

    def test_serialize_ts(ts):
        return _TimestampField()._serialize(ts, None, None)

    def test_serialize_dt(dt):
        return _TimestampField()._serialize(dt, None, None)

    @add_schema
    @dataclass
    class Foo:
        ts: datetime