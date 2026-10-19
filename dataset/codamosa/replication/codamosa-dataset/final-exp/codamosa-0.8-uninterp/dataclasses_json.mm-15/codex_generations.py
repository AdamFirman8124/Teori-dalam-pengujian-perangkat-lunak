

# Generated at 2022-06-13 19:20:42.379852
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class UserSchema(SchemaF): ...
    UserSchema().dumps([], many=True)


# Generated at 2022-06-13 19:20:53.393396
# Unit test for function schema
def test_schema():
    from dataclasses_json.api import dataclass_json
    from datetime import datetime, timedelta
    from enum import Enum
    import uuid
    @dataclass_json
    @dataclass
    class MyData:
        name: str
        age: int = 42
        data: typing.Optional[str] = None
        mail: typing.Optional[str] = ""
        height: typing.Optional[float] = 1.7
        date: typing.Optional[datetime] = datetime.now()
        uuid_: uuid.UUID = uuid.uuid4()

    @dataclass_json
    @dataclass
    class MyData2(MyData):
        name: typing.Optional[str]


# Generated at 2022-06-13 19:21:02.690757
# Unit test for function build_type
def test_build_type():
    assert build_type(int, {}, int, 1, None) == fields.Int
    assert build_type(list, {}, int, 1, None) == fields.List
    assert build_type(typing.List[int], {}, int, 1, None) == fields.List[int]
    assert build_type(typing.Void, {}, int, 1, None) == fields.Raw
    assert build_type(typing.Optional[int], {}, int, 1, None) == fields.Int
    assert build_type(typing.Union[int, None], {}, int, 1, None) == fields.Int
    assert build_type(typing.Union[int, str], {}, int, 1, None) == fields.Int
    assert build_type(typing.Type[int], {}, int, 1, None)

# Generated at 2022-06-13 19:21:08.977147
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclass_json
    @dataclass
    class DC:
        a: int

    sf = SchemaF[DC]()

    @dataclass_json
    @dataclass
    class DCOuter:
        a: typing.List[DC]

    sf_outer = SchemaF[DCOuter]()

    dc = DC(10)
    assert sf.dump(dc) == {'a': 10}
    assert sf.dump([dc]) == [{'a': 10}]



# Generated at 2022-06-13 19:21:18.847589
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # type: () -> None
    class Foo:
        pass

    @dataclasses_json.dataclass_json(unknown=dataclasses_json.UNDEFINED)
    class Bar:
        foo: str
        bar: typing.Optional[int] = None
        bar_none: typing.Optional[int] = None
        baz: typing.Optional[Foo] = None

    xs = [Bar(foo='foo', bar=1, bar_none=None),
          Bar(foo='foo', bar=2)]
    ys = [Bar(foo='foo', bar=1, bar_none=None),
          Bar(foo='foo', bar=2)]


# Generated at 2022-06-13 19:21:21.977141
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class TestData(typing.NamedTuple):
        b: int

    class TestDataSchema(SchemaF[TestData]):
        b = fields.Integer()

    dump = TestDataSchema().dumps(TestData(1))

    assert dump == '{"b": 1}'



# Generated at 2022-06-13 19:21:28.973093
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class OneSchema(SchemaF[List[int]]):  # type: ignore
        pass

    class TwoSchema(SchemaF[int]):  # type: ignore
        pass

    SCHEMA = OneSchema()
    assert SCHEMA.dumps(obj=[], many=False) == '[]'
    assert SCHEMA.dumps(obj=[], many=True) == '[]'
    assert SCHEMA.dumps(obj=[1, 2], many=False) == '[]'
    assert SCHEMA.dumps(obj=[1, 2], many=True) == '[1, 2]'
    SCHEMA = TwoSchema()
    assert SCHEMA.dumps(obj=1, many=True) == '1'
    assert SCHEMA.dumps(obj=1, many=False) == '1'

# Generated at 2022-06-13 19:21:36.295713
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    @dataclass_json
    @dataclass
    class Car:
        name: str

    car_schema = SchemaF[Car]()
    car = Car('Fiesta')
    assert car_schema.dumps(car) == '{"name": "Fiesta"}'
    assert car_schema.dumps([car, car]) == '[{"name": "Fiesta"}, {"name": "Fiesta"}]'


# Generated at 2022-06-13 19:21:40.639170
# Unit test for function build_schema
def test_build_schema():
    class Test:
        @classmethod
        def __init_subclass__(cls, **kwargs):
            if cls.__name__ != 'Test':
                cls.schema = build_schema(cls, dataclass_json, False, False)

    @dataclass_json
    class Test1(Test):
        a = 'hi'
        b = 1
        c: str = 'bye'
        d: int = 2

    assert type(Test1.schema) == type(Test1.schema)



# Generated at 2022-06-13 19:21:53.705184
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from typing import Mapping, List, Tuple, Union, Optional, Dict

    @dataclass
    class Person:
        name: str
        age: int

    @dataclass
    class A:
        field1: Union[str, Person]
        field2: Union[str, Mapping[str, Person], List[Person]]
        field3: Optional[Tuple[int, int, int]]
        field4: Dict[str, int]
        field5: List[int]
        field6: int = field(metadata=dict(mm_field=fields.Field(required=False)))
    mixin = dataclass_json(mm_schema=False)
    dc = _decode_dataclass(A)


# Generated at 2022-06-13 19:22:13.275241
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass
    class MyClass:
        s: str
        b: bytes

    JsonData = typing.Union[str, bytes, bytearray]
    TEncoded = typing.Dict[str, typing.Any]
    TOneOrMulti = typing.Union[typing.List[A], A]
    TOneOrMultiEncoded = typing.Union[typing.List[TEncoded], TEncoded]

    class SchemaF(Schema, typing.Generic[A]):
        """Lift Schema into a type constructor"""

        def __init__(self, *args, **kwargs):
            """
            Raises exception because this class should not be inherited.
            This class is helper only.
            """

            super().__init__(*args, **kwargs)
            raise NotImplementedError()



# Generated at 2022-06-13 19:22:20.149867
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from marshmallow import fields

    @dataclass_json
    @dataclass
    class User:
        username: str
        password: str

    @dataclass_json
    @dataclass
    class Test:
        users: typing.List["User"] = None
        at: typing.Tuple[datetime, datetime] = None
        enum: typing.Union[str, int] = None
        var: typing.Any = None
        optional: typing.Optional[int] = None
        mapped: typing.Dict[int, str] = None
        special: typing.Optional[typing.List[typing.Dict[str, str]]] = None
        # we cannot write `None` as it would be interpreted as Optional

# Generated at 2022-06-13 19:22:36.017898
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class DC:
        a: int = 1
        b: int = 2
        c: Optional[Decimal]
        d: int = 1

    DataClassSchema = build_schema(DC, None, True, False)
    # we need to instantiate the schema to run the test.
    schema = DataClassSchema()
    assert len(schema.declared_fields) == 4
    assert len(schema.fields.keys()) == 4
    # We need to add the values for the fields for the `to_internal_value` method
    dc = DC(a=3, c=Decimal(2))
    internal_value = schema.to_internal_value({"a": 3, "c": 2})
    object_value = schema.to_representation(dc)

# Generated at 2022-06-13 19:22:46.899591
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import asdict, field
    from typing import List
    from dataclasses_json import dataclass_json
    from dataclasses_json.utils import is_dataclass, dc_fields
    from marshmallow import Schema, fields
    from marshmallow.validate import OneOf, Length

    # Basic cases

    @dataclass_json
    @dataclass
    class MyName:
        first: str
        last: str

    assert is_dataclass(MyName)

    J = build_schema(MyName, None, None, None)
    assert issubclass(J, Schema)
    assert len(dc_fields(J)) == 2
    assert all([isinstance(i, fields.Field) for i in J().declared_fields.values()])

    # More complex cases


# Generated at 2022-06-13 19:22:56.749786
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    @dataclass_json
    @dataclass
    class Color:
        r: int
        g: int
        b: int

    @dataclass_json
    @dataclass
    class A:
        a: typing.List[Color]

    sf = SchemaF[A].from_dataclass(A)
    x = sf.dumps([Color(r=0, g=1, b=2)])


# Generated at 2022-06-13 19:23:05.123993
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    s = SchemaF[Test](strict=True)
    f = s.loads('{"a": 1, "b": "xxx"}')
    expected = Test(a=1, b='xxx')
    assert f == expected


# Generated at 2022-06-13 19:23:17.067154
# Unit test for function build_schema
def test_build_schema():
    import pytest
    schema_keys = {'Meta', f'make_{SYSTEM.lower()}', 'dumps', 'dump'}
    schema_keys.update(schema(SYSTEM, False, False))

    def test_keys(keys):
        assert keys <= schema_keys
        for key in keys:
            assert key in schema_keys

    test_keys(set(build_schema(SYSTEM, None, True, True).__dict__.keys()))

    test_keys(set(build_schema(SYSTEM, None, True, False).__dict__.keys()))
    test_keys(set(build_schema(SYSTEM, None, False, True).__dict__.keys()))
    test_keys(set(build_schema(SYSTEM, None, False, False).__dict__.keys()))

# Generated at 2022-06-13 19:23:25.705340
# Unit test for function schema
def test_schema():
    from marshmallow import Schema, fields
    from dataclasses import dataclass, MISSING
    from dataclasses_json import dataclass_json

    @dataclass
    class A:
        test: int = 1

    @dataclass_json
    @dataclass
    class Test:
        a: A = A()

    @dataclass_json
    @dataclass
    class B:
        b: Test = Test()

    class TestSchema(Schema):
        a = fields.Nested(Test.schema())

    class TestB(Schema):
        b = fields.Nested(B.schema())

    expected = {'b': {'b': {'a': {'test': 1}}}}

    assert TestB().dump(B()) == expected



# Generated at 2022-06-13 19:23:29.110127
# Unit test for function schema
def test_schema():
    # type: () -> None
    class TestClass:
        class Schema(SchemaType):
            __dataclass_json__ = _ExtendedEncoder(schema, module=TestClass,
                                                  infer_missing=True)
            # raise MarshmallowSchemaError("My error", {})
        pass



# Generated at 2022-06-13 19:23:39.389238
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Test:
        a: int = 1
        b: str
        c: typing.Optional[int]
        d: typing.Optional[typing.Union[int, str]] = None
        e: typing.List[int]
        f: int = field(default_factory=lambda: 5)
        g: typing.Optional[typing.List[int]] = None
        h: typing.List[typing.Union[int, str]] = field(
            metadata={'dataclasses_json': {'mm_field': fields.Str()}})
        i: typing.Dict[str, typing.List[int]] = field(
            default_factory=dict)

# Generated at 2022-06-13 19:24:09.635882
# Unit test for function schema
def test_schema():
    from typing import Optional

    from dataclasses import dataclass

    from dataclasses_json.mm import Mm

    @dataclass(frozen=True)
    class Person:
        name: str
        age: int
        birthday: Optional['datetime.datetime']

    assert schema(Person, Mm, True) == {
        'name': fields.Str(),
        'age': fields.Int(),
        'birthday': _TimestampField(allow_none=True)
    }



# Generated at 2022-06-13 19:24:13.973794
# Unit test for constructor of class _IsoField
def test__IsoField():
    # json = "2020-05-04T16:47:34.690515"
    dt = datetime.fromisoformat("2020-05-04T16:47:34.690515")
    fi = _IsoField()
    print(fi.__serialize__(dt, "", None, {}))
    


# Generated at 2022-06-13 19:24:25.123527
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class Test:
        a: str
        b: int = 3
        c: typing.List[int] = field(default_factory=list)
        d: typing.Dict = field(default_factory=dict)
        e: typing.Optional[str] = None
        f: typing.Optional[str] = field(default=None)
        g: typing.Optional[str] = field(default=None, mm_field=fields.Str())
        h: typing.Optional[str] = field(mm_field=fields.Str())
        i: typing.Optional[str] = field(
            metadata={'dataclasses_json': {
                'mm_field': fields.Str()}})


# Generated at 2022-06-13 19:24:35.092632
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from marshmallow import fields

    @dataclass
    class A:
        pass

    @dataclass
    class B:
        pass

    @dataclass
    class C:
        pass

    @dataclass
    class D:
        pass

    class E(Enum):
        a = 1
        b = 2
        c = 3

    assert build_type(A, {}, None, None, None) == fields.Field
    assert build_type(typing.List[A], {}, None, None, None) == fields.Field
    assert build_type(typing.Union[A, B, C], {}, None, None, None) == fields.Field

# Generated at 2022-06-13 19:24:46.037874
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import pytest
    @dataclass
    class Foo:
        a: str
        b: int

    @dataclass
    class Bar:
        foo: Foo
        c: float

    @dataclass
    class Baz:
        bar: Bar
        d: typing.Optional[int] = None

    opt = {'d': fields.Int(allow_none=True, missing=None, default=None)}
    result = schema(Baz, {}, False)

# Generated at 2022-06-13 19:24:50.119912
# Unit test for constructor of class _IsoField
def test__IsoField():
    assert _IsoField()._deserialize('2020-04-06T20:38:07.776829') == datetime(2020, 4, 6, 20, 38, 7, 776829)
    assert _IsoField()._deserialize(None) == None


# Generated at 2022-06-13 19:24:51.049519
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    pass



# Generated at 2022-06-13 19:25:00.477894
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    obj: typing.List[str] = []  # NOQA


# Generated at 2022-06-13 19:25:08.223353
# Unit test for function build_type
def test_build_type():
    from typing import Optional, Union, List, Dict, Tuple, Any, Callable
    from marshmallow import Schema
    from marshmallow.fields import Mapping, List, Dict, Tuple, Function, Raw, Str, Int, Float, Bool, Dict, Field
    from marshmallow_enum import EnumField
    from dataclasses_json import dataclass_json
    from .fixtures import ADTExampleEnum

    @dataclass_json
    class EnumExample(ADTExampleEnum):
        pass

    @dataclass_json
    class NestedExample:
        foo: str

    @dataclass_json
    class UnionExample:
        bar: Union[NestedExample, str]


# Generated at 2022-06-13 19:25:16.832763
# Unit test for function schema
def test_schema():
    import pytest
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin, config

    @dataclass
    class MyType(DataClassJsonMixin):
        default: int = field(default=42)

    @dataclass
    class MyTypeWithDefaultFactory(DataClassJsonMixin):
        default_factory: int = field(default_factory=lambda: 999)

    @dataclass
    class MyTypeUnion(DataClassJsonMixin):
        union: typing.Union[int, None] = None

    @dataclass
    class MyTypeWithDefaultFactoryUnion(DataClassJsonMixin):
        default_factory: typing.Union[int, None] = field(default_factory=lambda: 999)


# Generated at 2022-06-13 19:26:12.070584
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import fields, Schema

    class Output(object):
        def __init__(self, a: int):
            self.a = a
            
        def __eq__(self, other):
            return self.a == other.a

    class MySchema(Schema):
        a = fields.Int()

    MySchemaF = SchemaF[Output]
    my_schema = MySchemaF(cls=MySchema)
    assert my_schema.dump([Output(2), Output(3)]) == [{"a": 2}, {"a": 3}]
    assert my_schema.dump(Output(2)) == {"a": 2}
    assert my_schema.dump(Output(2), many = False) == {"a": 2}

# Generated at 2022-06-13 19:26:17.925264
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    ts = _TimestampField()
    try:
        datetime.fromtimestamp(ts._serialize(datetime.now(), "test", None))
    except (TypeError, OSError):
        assert False
    assert ts._serialize(None, "test", None) is None
    try:
        datetime.fromtimestamp(ts._serialize(datetime.now(), "test", None))
    except (TypeError, OSError):
        assert False
    try:
        ts._serialize(datetime.now(), "test", None, required=True)
        assert False
    except ValidationError:
        pass



# Generated at 2022-06-13 19:26:27.996216
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A:
        pass
    x: typing.List[A] = SchemaF[A].load([{}], many=True)
    x = SchemaF[A].load({}, many=None)
    x = SchemaF[A].load([{}, {}], many=None)  # type: ignore[arg-type]

# Generated at 2022-06-13 19:26:38.144890
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from typing_inspect import is_class_var, get_origin

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        class DummySchema(SchemaF[dict]):
            pass
        assert len(w) == 1
        assert issubclass(w[-1].category, RuntimeWarning)
        assert "schema_class should not be inherited" in str(w[-1].message)

    class DummySerializer(SchemaF[typing.Dict[str, int]]):
        a = fields.Int()

    class DummySerializer2(SchemaF[typing.Mapping[str, int]]):
        a = fields.Int()


# Generated at 2022-06-13 19:26:48.287934
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema
    from typing import List, Any


    class InnerSchema(Schema):
        x = fields.Int

    class InnerSchema2(Schema):
        y = fields.Int

    class OuterSchema(Schema, typing.Generic[A]):
        x = fields.Int
        xy = fields.Nested(InnerSchema)
        xyz = fields.Nested('OuterSchema[List[A]]')


    @dataclass_json
    @dataclass
    class Inner:
        x: int

    @dataclass_json
    @dataclass
    class Inner2:
        y: int

    @dataclass_json
    @dataclass
    class OuterList:
        x: int
        xy: Inner
        xyz: typing.List

# Generated at 2022-06-13 19:26:56.868130
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from marshmallow import fields

    @dataclass
    class _TestDataClass:
        a: str
        b: int = 1
        c: bool = True

    @dataclass
    class _TestDataClass2:
        d: str
        e: _TestDataClass

    class _Mixin:
        @classmethod
        def schema(cls):
            return schema(cls, _Mixin, False)

    _TestDataClass.schema()
    assert _TestDataClass.schema() == {'a': fields.Str(allow_none=False),
                                       'b': fields.Int(),
                                       'c': fields.Boolean()}

    _TestDataClass2.schema()

# Generated at 2022-06-13 19:27:06.379172
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class User:
        id: int
        name: str

    @dataclass_json
    @dataclass
    class Message:
        id: int
        content: str
        sender: User
        receiver: User
        is_read: bool = False

    @dataclass_json
    @dataclass
    class TestMeta:
        pass

    DataClassSchema = build_schema(Message, TestMeta(), False, False)
    assert 'content' in DataClassSchema._declared_fields
    assert 'id' in DataClassSchema._declared_fields
    assert 'sender' in DataClassSchema._declared_fields
    assert 'receiver' in DataClassSchema._declared_fields
    assert 'is_read' in DataClassSchema

# Generated at 2022-06-13 19:27:10.165678
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from pymarsh.main import Schema  # type: ignore
    from dataclasses import dataclass


    @dataclass
    class Person:
        name: str


    class PersonSchema(SchemaF[Person]):
        name = fields.Str()


    schema = PersonSchema()
    data = {"name": "foo"}
    result = schema.load(data)
    assert result is not None
    assert result.name == "foo"



# Generated at 2022-06-13 19:27:11.549454
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    assert field is not None


# Generated at 2022-06-13 19:27:21.008988
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class t1:
        a: str

    @dataclass
    class t2:
        b: int
        c: float
        d: typing.List[int]
        e: typing.Optional[t1]
        f: typing.Optional[t2]
        g: t1

    @dataclass
    class t3:
        h: t2
        i: typing.Optional[t1]
        j: typing.Optional[t2]

    @dataclass
    class t4:
        k: typing.List[t2]
        l: typing.List[t3]

    schema = build_schema(t1, None, False, False)
    assert schema.dump(t1("a"), many=False) == {"a": "a"}