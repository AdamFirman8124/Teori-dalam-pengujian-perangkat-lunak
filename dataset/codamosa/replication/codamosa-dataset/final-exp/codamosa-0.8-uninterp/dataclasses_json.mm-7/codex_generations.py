

# Generated at 2022-06-13 19:20:41.356886
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()


# Generated at 2022-06-13 19:20:44.366698
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert SchemaF[int].dumps(0) == '0'
    assert SchemaF[int].dumps([0, 0]) == '[0, 0]'


# Generated at 2022-06-13 19:20:59.658685
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass, field

    @dataclass
    class Test:
        num: int = 1
        str_: str = field(default='hello')

    assert issubclass(build_schema(Test, object, True, False), Schema)
    assert build_schema(Test, object, True, False).Meta.fields == ('num', 'str_')
    assert hasattr(build_schema(Test, object, True, False), 'make_test')
    assert hasattr(build_schema(Test, object, True, False), 'dumps')
    assert hasattr(build_schema(Test, object, True, False), 'dump')
    assert hasattr(build_schema(Test, object, True, False), 'num')

# Generated at 2022-06-13 19:21:11.802869
# Unit test for function build_schema
def test_build_schema():
    from .types import Complex
    from .types import Simple
    import typing
    from datetime import datetime
    from dataclasses_json.types import TEncoded
    from typing import List

    @dataclass_json
    @dataclass
    class SimpleWithArray:
        name: str
        arr: typing.List[str]
    test_obj = Simple(name="John",
                    number=123,
                    bools=True,
                    datetime=datetime.now())
    test_obj_dict = {'name': 'John',
                    'number': 123,
                    'bools': True,
                    'datetime': test_obj.datetime.isoformat()}

# Generated at 2022-06-13 19:21:18.592011
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    # This is a very simple test.
    # More elaborate tests are in tests_dataclasses.test_dataclass_json_schema_load
    @dataclasses.dataclass
    class TestObj:
        test: str

    s = SchemaF[TestObj](strict=True)
    assert s.loads('{"test": "test"}') == TestObj(test='test')



# Generated at 2022-06-13 19:21:26.052134
# Unit test for function build_type
def test_build_type():

    # Test for when type_ is origin
    type_ = typing.Dict
    options = {}
    mixin = dataclasses.dataclass
    field = field = dc_fields(dict)[0]
    cls = Enum

    inner = build_type(type_, options, mixin, field, cls)
    assert(inner(typing.Dict, options) == fields.Dict())

    # This is the case where the origin is a union in which each member is a dataclass
    type_ = typing.Union[A, B]
    type_.__args__ = [A, B]

    options = {}
    mixin = dataclasses.dataclass
    field = field = dc_fields(dict)[0]
    cls = Enum


# Generated at 2022-06-13 19:21:26.835250
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    pass



# Generated at 2022-06-13 19:21:39.130569
# Unit test for function build_type
def test_build_type():
    assert isinstance(build_type(int, {}, object, object, object), fields.Int)
    assert isinstance(build_type(float, {}, object, object, object), fields.Float)
    assert isinstance(build_type(str, {}, object, object, object), fields.Str)
    assert isinstance(build_type(bool, {}, object, object, object), fields.Bool)
    assert isinstance(build_type(UUID, {}, object, object, object), fields.UUID)
    assert isinstance(build_type(dict, {}, object, object, object), fields.Dict)
    assert isinstance(build_type(list, {}, object, object, object), fields.List)
    assert isinstance(build_type(datetime, {}, object, object, object), _TimestampField)
   

# Generated at 2022-06-13 19:21:43.485697
# Unit test for function build_type
def test_build_type():
    # test build type
    assert isinstance(build_type(int, {}, {}, {}, {})(int, {}), fields.Int)
    assert isinstance(build_type(str, {}, {}, {}, {})(str, {}), fields.Str)
    assert isinstance(build_type(list, {}, {}, {}, {})(list, {}),
                      fields.List)
    assert isinstance(
        build_type(typing.List, {}, {}, {}, {})(list, {}), fields.List)
    assert isinstance(build_type(dict, {}, {}, {}, {})(dict, {}),
                      fields.Dict)



# Generated at 2022-06-13 19:21:49.108993
# Unit test for function build_schema
def test_build_schema():
    class NoopSchema(Schema):
        pass

    class MyMixin(NoopSchema):
        pass

    @dataclass_json(mm_schema=NoopSchema)
    @dataclass
    class MyDc:
        x: int
        y: int
        d: dict = field(dataclass_json=dataclasses_json.config(
            mm_field=fields.Dict))

    s = build_schema(MyDc, MyMixin, False, False)


# Generated at 2022-06-13 19:22:03.218046
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField() is not None

DateTimeField = _TimestampField


# Generated at 2022-06-13 19:22:06.708446
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import fields
    from marshmallow import Schema

    from typing import List
    from typing import TypeVar

    A = TypeVar('A')

    class Foo(SchemaF[A]):
        pass


# Generated at 2022-06-13 19:22:14.288175
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    class MyClass:
        def __init__(self):
            self.ts = datetime.now()
    field = _TimestampField()
    # The timestamp is a float
    assert field.get_value(MyClass()) == field._serialize(field.get_value(MyClass()), None, MyClass())
    # The timestamp is equal to the value
    assert field.get_value(MyClass()) == field._deserialize(field.get_value(MyClass()), None, MyClass())


# Generated at 2022-06-13 19:22:16.522610
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema

    class FooSchema(Schema):
        pass

    class Foo():
        pass


# Generated at 2022-06-13 19:22:20.264876
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime(2019, 7, 16, 8, 28, 7), None, None, None) == 1563314687
    assert _TimestampField(required=False)._serialize(None, None, None, None) is None
    assert _TimestampField(required=False)._deserialize(None, None, None, None) is None



# Generated at 2022-06-13 19:22:23.858681
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    value = datetime.now()
    assert field._serialize(value, None, None) == value.isoformat()
    assert field._deserialize(value.isoformat(), None, None) == value.replace(tzinfo=None)



# Generated at 2022-06-13 19:22:29.064593
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    schema = get_schema(TestClass)
    json = schema.dumps(TestClass('a', 1, 2.1))
    assert isinstance(json, str)



# Generated at 2022-06-13 19:22:37.996815
# Unit test for function schema
def test_schema():
    from typing import Union
    
    import marshmallow as mm
    from marshmallow import fields
    from dataclasses import field
    
    @dataclasses.dataclass
    class A:
        x: mm.fields.Number
    
    @dataclasses.dataclass
    class B:
        x: int
        y: Union[str, int]
        z: Union[mm.fields.Number, mm.fields.List]
    
    assert schema(A, None, False) == {'x': mm.fields.Number()}
    assert schema(B, None, False) == {'x': fields.Int(), 'y': fields.Field(), 'z': fields.Field()}

# Generated at 2022-06-13 19:22:46.787549
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class Foo:
        pass

    class FooSchema(SchemaF[Foo]):
        pass

    assert isinstance(FooSchema().dumps([]), str)
    assert isinstance(FooSchema().dumps([Foo()]), str)
    assert isinstance(FooSchema().dumps(Foo()), str)

# Generated at 2022-06-13 19:22:52.223991
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # Success
    class TestSchema(SchemaF[A]):
        one = fields.Str()
    assert TestSchema().dump({'one': 'success'}) == {'one': 'success'}
    try:
        TestSchema().dump([])  # type: ignore
    except MarshmallowError as e:
        assert str(e) == 'Invalid input type.'

# Generated at 2022-06-13 19:23:19.562572
# Unit test for function schema
def test_schema():
    # case 1: no mixin
    class Product:
        def __init__(self, pid, name, list_price):
            self.pid = pid
            self.name = name
            self.list_price = list_price

    _schema = schema(Product, None, False)
    assert _schema == {}

    # case 2:
    class Product1(dataclasses_json.DataClassJsonMixin):
        def __init__(self, pid, name, list_price):
            self.pid = pid
            self.name = name
            self.list_price = list_price

    _schema = schema(Product1, None, False)

# Generated at 2022-06-13 19:23:25.537823
# Unit test for function schema
def test_schema():
    assert schema({}, 3) == {}
    assert schema({"name": {"dataclasses_json": {"mm_field": 3}}}, 3) == {"name": 3}
    assert schema({"name": {"dataclasses_json": {"mm_field": 3}}}, 4) == {"name": 3}
    assert schema({"name": {"dataclasses_json": {"mm_field": None}}}, 3) == {"name": 3}
    assert schema({"name": {"dataclasses_json": {"mm_field": 5}}}, 3) == {"name": 5}
test_schema()



# Generated at 2022-06-13 19:23:31.690433
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():  # type: ignore
    class FooSchema(SchemaF[A]):
        pass

    @dataclass
    class A:
        age: int
    as_ = [A(age=1), A(age=2)]
    schema = FooSchema()
    result = schema.dump(as_)  # type: ignore
    assert result == [{'age': 1}, {'age': 2}]

    result = schema.dump(as_, many=True)  # type: ignore
    assert result == [{'age': 1}, {'age': 2}]

    a = A(age=1)
    result = schema.dump(a)  # type: ignore
    assert result == {'age': 1}

    result = schema.dump(a, many=False)  # type: ignore

# Generated at 2022-06-13 19:23:33.123723
# Unit test for constructor of class _IsoField
def test__IsoField():
    i = _IsoField()
    return i


# Generated at 2022-06-13 19:23:43.121488
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from typing import List, Mapping, Dict
    from marshmallow import Schema, fields
    import dataclasses
    class MySchema(Schema, typing.Generic[A]):
        pass
    @dataclasses.dataclass
    class Bar:
        bar: str
        bar2: int
    @dataclasses.dataclass
    class Foo:
        i: int
        s: str
        e: Bar

    class DataClassSchema(MySchema[Foo]):
        i = fields.Int()
        s = fields.String()
        e = fields.Nested('DataClassSchema')

    foo1 = Foo(i=42, s="string", e=Bar(bar="barstring", bar2=2))
    dc_schema = DataClassSchema()

# Generated at 2022-06-13 19:23:46.078783
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class Person:
        name: str
        age: Optional[int] = None

    s = schema(Person, None, False)
    assert type(s['age']) is _TimestampField
    assert s['name'].required == False
    assert s['age'].required == False
    assert s['name'].default is None
    assert s['age'].default is None
    #assert type(s['age']) == TimestampField



# Generated at 2022-06-13 19:23:51.234240
# Unit test for function build_type
def test_build_type():
    class Mixin:
        @classmethod
        def schema(cls):
            return cls()

    class A:
        pass

    class B(A):
        pass


# Generated at 2022-06-13 19:23:51.949794
# Unit test for function build_type
def test_build_type():
    assert False
    return
    assert True

# Generated at 2022-06-13 19:24:03.975792
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import marshmallow
    class Mixin:
        pass

    @dataclass
    class Embedded:
        val: int

    @dataclass
    class C(Mixin):
        i: int
        f: float
        s: str
        u: typing.Optional[UUID]
        embedded: Embedded
        f_default: float = 3.14
        f_factory: float = fields.Field(default_factory=lambda: 3.14)

        class Config:
            infer_missing = True


# Generated at 2022-06-13 19:24:05.811368
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    schema = SchemaF()
    assert '2' == schema.dump(2)


# Generated at 2022-06-13 19:25:00.320053
# Unit test for function build_schema
def test_build_schema():
    import dataclasses_json
    import dataclasses
    import marshmallow
    class UserSchema():
        def Meta(self):
            pass
        def make_user(self,kvs,**kwargs):
            pass
        def dumps(self):
            pass
        def dump(self):
            pass
        username = fields.Str()
        email = fields.Str()
        age = fields.Int()

    class User:
        def __init__(self,name,email,age):
            self.name = name
            self.email = email
            self.age = age

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class User:
        username: str
        email: str
        age: int


# Generated at 2022-06-13 19:25:01.497852
# Unit test for function build_type
def test_build_type():
    assert build_type(str, {}, None, None, None)

# Generated at 2022-06-13 19:25:03.458964
# Unit test for function schema
def test_schema():
    assert schema(list,list,True) ==  {'append':fields.Function}
    assert schema(bool,bool,True) == {}
    assert schema(dict,dict,True) == {}

# Generated at 2022-06-13 19:25:08.217045
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow import Schema, fields
    class S(Schema):
        data = fields.Dict()
    schema = SchemaF[typing.Dict[str, str]](S)
    result = schema.loads('{"data": "test"}')
    assert result == {"data": "test"}
    assert isinstance(result, dict)


# Generated at 2022-06-13 19:25:08.817032
# Unit test for function build_schema
def test_build_schema():
    pass

# Generated at 2022-06-13 19:25:17.346552
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from typing import List
    from marshmallow import fields
    from marshmallow.schema import Schema
    class Foo(Schema):
        a: int
        b: str
        c: List[int]
    FooF = SchemaF[Foo]
    assert issubclass(FooF, Schema)
    assert FooF.dump([{"b":"a", "a": 1, "c": [1, 2, 3]}, {"b":"a", "a": 1, "c": [1, 2, 3]}], many=True) == [{"b":"a", "a": 1, "c": [1, 2, 3]}, {"b":"a", "a": 1, "c": [1, 2, 3]}]

# Generated at 2022-06-13 19:25:33.853640
# Unit test for function schema
def test_schema():
    import typing
    import dataclasses

    @dataclasses.dataclass
    class DC1:
        a: typing.Optional[int] = dataclasses.field(metadata=dataclasses.field(
            mm_field=fields.Int()))
        b: typing.Optional[int] = dataclasses.field(default=2)
        c: typing.Optional[int] = dataclasses.field(default=3)


    @dataclasses.dataclass
    class DC2:
        d: typing.Optional[int]
        e: typing.Optional[DC1] = dataclasses.field(default=DC1())


    from dataclasses_json import dataclass_json
    from dataclasses_json.schema import schema



# Generated at 2022-06-13 19:25:36.490144
# Unit test for constructor of class _IsoField
def test__IsoField():
    from datetime import datetime
    dt = datetime.now()
    value = dt.isoformat()
    f = _IsoField()
    f._deserialize(value)
# End of Unit test for constructor of class _IsoField



# Generated at 2022-06-13 19:25:37.610470
# Unit test for function schema
def test_schema():
    assert schema({}, {}, infer_missing=True) == {}, 'schema should return an empty dict'


# Generated at 2022-06-13 19:25:48.591758
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # type: () -> None
    @dataclasses.dataclass
    class A:
        b: int

    s = SchemaF.of(A)
    x = s.load({'b': 1})  # type: ignore
    assert isinstance(x, A)


# Generated at 2022-06-13 19:27:25.537787
# Unit test for function schema
def test_schema():
    from typing import List

    from dataclasses import dataclass

    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class Marsh():
        a: str
        b: List[int]
        c: bool = True
        d: Decimal = Decimal(1)
        e: datetime


# Generated at 2022-06-13 19:27:26.485631
# Unit test for function build_schema
def test_build_schema():
    # TODO
    pass

# Generated at 2022-06-13 19:27:36.139105
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    @dataclass_json
    @dataclass
    class SchemaF_test_loads(object):
        float_field: float

    s = SchemaF[SchemaF_test_loads].Schema(strict=True)
    e = s.loads('{"float_field":1.1}', many=False)
    assert e.float_field == 1.1

    es = s.loads('[{"float_field":1.1},{"float_field":1.1}]', many=True)
    assert not isinstance(es, SchemaF_test_loads)
    assert isinstance(es, list)
    assert len(es) == 2
    assert isinstance(es[0], SchemaF_test_loads)
    assert isinstance(es[1], SchemaF_test_loads)
    assert es

# Generated at 2022-06-13 19:27:40.834886
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    @dataclass
    class User:
        name: str = 'a'
    assert schema(User, None, False) == {'name': fields.Field(default='a', load_from='name', missing=fields.missing)}

test_schema()


# Generated at 2022-06-13 19:27:47.849541
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Person:
        name: str

    schema = build_schema(Person, {}, True, False)
    print(schema.__name__)
    print(schema.Meta.fields)
    print(schema.make_person)

test_build_schema()
 

# Generated at 2022-06-13 19:27:48.577512
# Unit test for function build_type
def test_build_type():
    pass



# Generated at 2022-06-13 19:27:56.392468
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Foo:
        foo: str
        bar: int

        @property
        def baz(self) -> str:
            return "bla bla"

    assert isinstance(build_schema(cls=Foo, mixin=Schema, infer_missing=True,
                                   partial=False),
                      type(SchemaF[Foo]))

# Generated at 2022-06-13 19:28:04.595175
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    dc = typing.Dict[str, int]
    ndc = typing.List[int]
    SchemaF[dc].loads(data={"a": 1, "b": 2}, many=False)
    SchemaF[ndc].loads(data=[1,2,3], many=True)

# Generated at 2022-06-13 19:28:19.326225
# Unit test for function build_schema
def test_build_schema():
    import marshmallow
    mixin = BasicMappingMixin
    infer_missing = global_config.infer_missing
    partial = global_config.strict_json

# Generated at 2022-06-13 19:28:27.803157
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class S1(SchemaF):
        pass

    s = S1()
    s.loads([{}, {}])
    assert isinstance(s.loads('[{"a": 1}]'), list)
    assert isinstance(s.loads([{}], many=False), dict)


if sys.version_info >= (3, 7):
    class BaseSchemaF(SchemaF[A]):
        """Lift Schema into a type constructor"""

        def __init__(self, *args, **kwargs):
            """
            Raises exception because this class should not be inherited.
            This class is helper only.
            """

            super().__init__(*args, **kwargs)
            raise NotImplementedError()

else:
    BaseSchemaF = Schema
