

# Generated at 2022-06-13 19:20:54.821033
# Unit test for function build_schema
def test_build_schema():
    # TODO fix test
    import dataclasses
    @dataclasses.dataclass
    class B:
        x: int = 10
        y: str = "abc"

    @dataclasses.dataclass
    class A:
        z: int = 100
        b: typing.List[B] = None
        c: typing.List[B] = dataclasses.field(default_factory=list)

    schema = build_schema(A, None, True, False)
    a = A()
    j = schema().dump(a)
    assert j == {"z": 100, "b": None, "c": []}



# Generated at 2022-06-13 19:21:02.781209
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from pytest import raises

    from dataclasses_json.core import JsonMixin

    @dataclass
    class DC1(JsonMixin):
        s: str
        i: int
        o: typing.Optional[int]
        l: typing.List[int]

    d = schema(DC1, JsonMixin, True)
    assert d['s'].type == str
    assert d['i'].type == int
    assert d['o'].allow_none is True
    assert d['l'].type == typing.List[int]

    with raises(NotImplementedError):
        SchemaF[DC1]()



# Generated at 2022-06-13 19:21:12.510346
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    Encoded = typing.Dict[str, typing.Any]
    OneOrMulti = typing.Union[typing.List[int], int]  # noqa: F821
    OneOrMultiEncoded = typing.Union[typing.List[Encoded], Encoded]
    s = SchemaF[int].load([1, 2])
    assert typing.get_type_hints(SchemaF.load) == typing.get_type_hints(
        lambda self: self)
    assert isinstance(s, list)
    s = SchemaF[int].load(1)
    assert isinstance(s, int)
    s = SchemaF[int].loads(b'[1, 2]')

# Generated at 2022-06-13 19:21:14.835844
# Unit test for function schema
def test_schema():
    class Test:
        pass

    class Test1(Test, Schema):
        pass



# Generated at 2022-06-13 19:21:23.563909
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class DummyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class DummyClassSchema(SchemaF[DummyClass]):
        a = fields.Int()
        b = fields.Str()

        @post_load
        def to_obj(self, data):
            return DummyClass(**data)

    sc = DummyClassSchema()
    res = sc.loads(b'not valid json', many=False)
    # mypy tells us that it is not a DummyClass. And it is correct.
    # Workaround is to do this check
    isinstance(res, DummyClass)

# Generated at 2022-06-13 19:21:28.623721
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class TestSchema(SchemaF[A], Schema):
        x: str

    data = [{"x": "foo"}, {"x": "bar"}]
    assert TestSchema(many=True).dump(data) == data



# Generated at 2022-06-13 19:21:34.223509
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    """
    It should be possible to use class SchemaF as an instance.
    """
    class SimpleSchema(SchemaF[int]):
        pass

    schema = SimpleSchema()
    result = schema.dump(12)
    assert isinstance(result, dict)


# Generated at 2022-06-13 19:21:42.925099
# Unit test for function build_type
def test_build_type():
    class MM(object):
        @classmethod
        def Schema(cls):
            return cls

    class MM2(object):
        @classmethod
        def Schema(cls):
            return cls

    class Mixin(object):
        pass

    class Mixin2(object):
        pass

    @dataclasses.dataclass
    class A(Mixin):
        foo: int

    @dataclasses.dataclass
    class B(Mixin2):
        bar: str

    type_ = typing.Optional[int]
    options = {}
    mixin = Mixin
    field = dataclasses.Field(typing.Optional[int], default=1, init=True,
                              repr=True, hash=None, compare=True,
                              metadata={})

# Generated at 2022-06-13 19:21:55.882299
# Unit test for function build_type
def test_build_type():
    union_type = typing.Union[int, float]
    int_type = build_type(int, {}, 'mixin', 'field', 'cls')
    str_type = build_type(str, {}, 'mixin', 'field', 'cls')
    optional_type = build_type(typing.Optional[int], {}, 'mixin', 'field', 'cls')
    union_type = build_type(union_type, {}, 'mixin', 'field', 'cls')

    assert int_type == fields.Int({})
    assert str_type == fields.Str({})
    assert optional_type == fields.Integer({'allow_none': True})
    assert union_type == _UnionField({int: fields.Int({}), float: fields.Float({})}, 'cls', 'field', {})


# Generated at 2022-06-13 19:22:04.188390
# Unit test for function build_schema
def test_build_schema():
    class T(TypeVar):
        pass

    @dataclass_json
    @dataclass
    class Foo:
        value: T = 3

        def __post_init__(self):
            self.value = self.value + 1

    @dataclass_json(mm_field=fields.Int(allow_none=True))
    @dataclass
    class Foo2:
        value: typing.Optional[int]

    @dataclass_json
    @dataclass
    class Foo3:
        value: typing.NewType('Value', int)

    @dataclass_json
    @dataclass
    class Foo4:
        value: typing.NewType('Value', str)


# Generated at 2022-06-13 19:22:21.691265
# Unit test for function build_type
def test_build_type():
    import typing
    import marshmallow
    import marshmallow_enum
    import dataclasses_json
    from copy import deepcopy
    from enum import Enum
    from test.helper import is_test_enabled
    if not is_test_enabled('build_type'):
        return
    from dataclasses import dataclass, field
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class BuildTypeTest:
        x: str
        y: int = field(metadata={'mm_field': marshmallow.fields.Str})
        z: typing.Optional[typing.List[int]] = field(
            default=None, metadata={
                'mm_field': marshmallow.fields.List(
                    marshmallow.fields.Integer())})
        a: typing.M

# Generated at 2022-06-13 19:22:36.053042
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    ts = _TimestampField(default=5)
    assert ts.default == 5
    assert ts.deserialize(5) == _timestamp_to_dt_aware(5)
    assert ts.serialize(datetime(2019, 1, 1, 0, 0, 0)) == 1546300800
    assert ts._serialize(None, 1, 2, 2) is None
    with warnings.catch_warnings(record=True) as w:
        ts._serialize(None, 1, 2, 2, required=True)
    assert len(w) == 1
    assert issubclass(w[-1].category, UserWarning)
    assert "required" in str(w[-1].message)


# Generated at 2022-06-13 19:22:38.228174
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    assert field._deserialize(0) == datetime.fromtimestamp(0)
    assert field._serialize(datetime.fromtimestamp(0)) == 0


# Generated at 2022-06-13 19:22:48.428596
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from typing import List
    from marshmallow import Schema
    from marshmallow.fields import Str, Integer

    class MyTmpSchema(SchemaF[List[List[int]]]):
        name = Str()
        age = Integer()
    cls_f = MyTmpSchema()
    res = cls_f.loads('{"name": "john", "age": 20}', many=True)
    pass

    class MyTmpSchema(SchemaF[List[int]]):
        name = Str()
        age = Integer()
    cls_f = MyTmpSchema()
    res = cls_f.loads('{"name": "john", "age": 20}', many=True)
    pass

    class MyTmpSchema(SchemaF[int]):
        name = Str()

# Generated at 2022-06-13 19:22:53.657357
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclasses.dataclass
    class Foo:
        foo: str

    schema = SchemaF(fields={'foo': fields.String()})
    assert not isinstance(schema, Schema)
    assert isinstance(schema.dump(Foo('bar')), dict)
    assert isinstance(schema.dump([Foo('bar')]), list)



# Generated at 2022-06-13 19:23:03.286949
# Unit test for function build_type
def test_build_type():
    # fmt: off
    class U1(Enum):
        z = 1
    class U2(Enum):
        y = 2
    class Unit(typing.NamedTuple):
        a: int
    class Recursive:
        foo: typing.List['Recursive']
    class Recursive_Mixin_Parent(Recursive, TypedSchemaMixin):
        pass
    class Recursive_Mixin_Child(Recursive_Mixin_Parent):
        pass
    class Recursive_Child(Recursive):
        pass
    class Recursive_Mixin_Unrelated(typing.NamedTuple):
        pass
    class Recursive_Unrelated(typing.NamedTuple):
        pass
    class DC1:
        x: typing.Union[U1, U2, int]

# Generated at 2022-06-13 19:23:15.001830
# Unit test for function build_type
def test_build_type():
    @dataclass
    class Foo:
        a: int

    @dataclass
    class Bar:
        foo: Foo
    class TestClass:
        @dataclass_json
        @dataclass
        class InnerClass:
            foo: Foo

        @dataclass_json
        @dataclass
        class InnerClass2(InnerClass):
            bar: Bar

        @dataclass_json
        @dataclass
        class Class1:
            foo: InnerClass
            bar: typing.List[int]

        @dataclass_json
        @dataclass
        class Class2:
            foo: typing.Optional[InnerClass2]
            bar: typing.List[Bar]

        @dataclass_json
        @dataclass
        class Class3(Class1):
            bar: typing

# Generated at 2022-06-13 19:23:24.240524
# Unit test for function build_schema
def test_build_schema():
    data_config = dataclass_json(
        LetterCase.CAMEL,
        Metadata.default(infer_serializer=True, infer_deserializer=True),
    )

    @data_config
    @dataclass
    class ItemClass:
        string_field: str
        int_field: int
        uuid_field: uuid.UUID
        datetime_field: datetime
        decimal_field: decimal.Decimal
        bool_field: bool
        list_field: typing.List[int]
        union_field: typing.Union[int, str]
        default_field: str = "123"
        optional_field: typing.Optional[int] = None

# Generated at 2022-06-13 19:23:30.595727
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field

    @dataclass
    class _Test:
        a: int = field(metadata={'dataclasses_json': {'mm_field': fields.List(fields.Int)}})
        b: str = field(metadata={'dataclasses_json': {
            'mm_field': fields.Str(default='test', missing='test')}})
        c: str = field(metadata={'dataclasses_json': {'mm_field': fields.Str(data_key="D")}})
        d: int = field()

    import pprint

    pprint.pprint(schema(_Test, Schema, infer_missing=True))

# Generated at 2022-06-13 19:23:41.257201
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    def test() -> None:
        class PointF(typing.NamedTuple):
            x: int
            y: int

        class PointSchema(SchemaF[PointF]):
            x = fields.Int()
            y = fields.Int()

        p1 = PointF(2, 3)
        p2 = PointF(4, 5)
        pl = [p1, p2]
        schema = PointSchema()
        assert schema.dumps(p1) == '{"x": 2, "y": 3}'
        assert schema.dumps(p2) == '{"x": 4, "y": 5}'
        assert schema.dumps(pl) == '[{"x": 2, "y": 3}, {"x": 4, "y": 5}]'

# Generated at 2022-06-13 19:24:04.222099
# Unit test for function build_type
def test_build_type():
    class Bar:
        pass

    @dataclass_json
    class BarSchema(SchemaType):
        baz: str

    class Foo:
        class Bar(Enum):
            baz = 'baz'

    type_ = typing.Optional[Foo.Bar]
    options = {}
    mixin = SchemaType
    field = dc_fields(Bar)[0]
    cls = Bar
    True == _issubclass_safe(Foo.Bar, Enum)
    assert (is_union_type(type_) == False)
    assert (_is_optional(type_) == True)
    assert (_issubclass_safe(Foo.Bar, Enum) == True)
    assert (field.type == type_)
    assert (field.name == 'baz')

# Generated at 2022-06-13 19:24:15.632722
# Unit test for function schema
def test_schema():
    from dataclasses_json.core import as_dict
    from dataclasses import dataclass
    import marshmallow as mm
    import typing

    @dataclass(frozen=True)
    class EnumExample(Enum):
        VALUE_A = 'A'
        VALUE_B = 'B'

    @dataclass(frozen=True)
    class TestUnion:
        a: typing.Union[str, int]

    @dataclass(frozen=True)
    class TestInherit(TestUnion):
        b: str

    @dataclass(frozen=True)
    class TestAny:
        a: typing.Any

    @dataclass(frozen=True)
    class TestMapping:
        a: typing.Mapping[str, int]


# Generated at 2022-06-13 19:24:25.875853
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import List
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class Data:
        data: int

    class MySchema(SchemaF[Data]):
        data = fields.Integer()

    assert MySchema().dumps(Data(1)) == '{"data": 1}'
    assert MySchema().dumps(Data(1)) == MySchema().dumps(List[Data]([Data(1)]), many=True)


# Generated at 2022-06-13 19:24:35.637012
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import json
    import typing
    from marshmallow import Schema, fields
    from marshmallow.utils import missing
    from marshmallow.exceptions import ValidationError
    from dataclasses import dataclass
    
    
    
    
    
    
    
    
    
    
    @dataclass
    class Member:
        name: str
        age: int
        address: typing.Optional[str]
    
    
    
    
    
    
    
    
    
    class MemberSchema(Schema):
        name = fields.Str()
        age = fields.Int()
        address = fields.Str(default=missing)
    
        @post_load
        def make_member(self, data, **kwargs):
            return Member(**data)

# Generated at 2022-06-13 19:24:45.160080
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    @dataclasses.dataclass
    class A:
        a: str

    class S(SchemaF[A]):
        a = fields.Str()

    s = S()
    res = s.dump(A('foo'))
    assert res == {'a': 'foo'}
    assert isinstance(res, dict)
    res = s.dump([A('foo'), A('bar')])
    assert res == [{'a': 'foo'}, {'a': 'bar'}]
    assert isinstance(res, list)
    with pytest.raises(NotImplementedError):
        s.dump(A('foo'), many=True)


# Generated at 2022-06-13 19:24:53.650849
# Unit test for function schema
def test_schema():
    import marshmallow as mm
    from dataclasses import dataclass

    @mm.post_load
    def make_stuff(self, data, **kwargs):
        from dataclasses_json.core import _decode_dataclass
        return _decode_dataclass(self.test_dt, data)

    @dataclass
    class Example:
        x: float

    class TestSchema(mm.Schema):
        class Meta:
            unknown = mm.EXCLUDE

    encoded = TestSchema().dump(Example(1.1))
    assert encoded == {'x': 1.1}



# Generated at 2022-06-13 19:24:57.867127
# Unit test for function schema
def test_schema():
    from marshmallow_dataclass import class_schema
    assert (schema(class_schema,class_schema,True) == {'id': fields.Int(missing=None), 'name': fields.Str(default='', missing=''), 'email': fields.Str(default='', missing='')})
    return 0



# Generated at 2022-06-13 19:24:59.140980
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    field.deserialize("2017-11-12T15:07")



# Generated at 2022-06-13 19:25:08.434506
# Unit test for function schema
def test_schema():
    import sys
    import os

    root_dir = os.path.abspath(os.path.dirname(__file__))
    for i in range(2):
        root_dir = os.path.dirname(root_dir)
    sys.path.append(root_dir)
    from tests.utils import get_instance, check
    from dataclasses_json.mm import MMEncoder
    class MSchema(Schema):
        def handle_error(self, error, data):
            pass

    class Base(MMEncoder):
        @classmethod
        def schema(cls):
            return MSchema

    # test simple
    class A(Base):
        a: int

    cls = A
    inst = get_instance(cls, 0)
    validate_func = check(inst)


# Generated at 2022-06-13 19:25:17.220417
# Unit test for function schema
def test_schema():
    import marshmallow as mm

    @dataclass_json
    @dataclass
    class DataSchemaMixin:
        schema_: mm.Schema

        @classmethod
        def schema(cls):
            return cls.schema_

    @dataclass_json(mix_with=DataSchemaMixin)
    @dataclass
    class Test:
        a: int = 1

        @classmethod
        def schema(cls):
            return cls.schema_

    try:
        import pytest
        pytest.fail("Test should have thrown an exception because"
                    " the class doesn't inherit from DataSchemaMixin")
    except TypeError:
        pass


# Generated at 2022-06-13 19:25:37.057640
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type: () -> None
    class Foo(typing.Protocol):
        foo: int

    class FooSchema(SchemaF[Foo]):
        foo = fields.Int()

    class Bar:
        def __init__(self) -> None:
            self.foo = 42

    BarSchema = FooSchema.inherit(Bar)
    bar = Bar()
    bar_schema = BarSchema()
    bar_schema.dumps(bar)
    # foo = 42

    class FooBar:
        def __init__(self, bar: int) -> None:
            self.bar = bar

        @property
        def foo(self) -> int:
            return self.bar

    BarFooSchema = FooSchema.inherit(FooBar)

# Generated at 2022-06-13 19:25:48.434419
# Unit test for function build_type
def test_build_type():
    # import typing

    # from enum import Enum, auto, unique
    # from dataclasses import dataclass, field
    # from dataclasses_json import dataclass_json
    # from marshmallow import Schema, fields as mm_fields, post_load
    # import pytest
    # from marshmallow_enum import EnumField

    # from dataclasses_json.marshmallow_ import _TimestampField
    # from dataclasses_json.marshmallow_ import _UnionField

    # from .common import assert_equal

    class MMMixin():
        """Mixin class for marshmallow dataclasses.

        https://marshmallow.readthedocs.io/en/stable/extending.html#declaring-a-custom-field-for-a-nested-object
        """


# Generated at 2022-06-13 19:25:58.346866
# Unit test for function build_schema
def test_build_schema():
    from tests.resources import Simple
    from tests.resources import Pet
    from tests.resources import Person

    DataClassSchema = build_schema(Simple, [], False, False)

    s = DataClassSchema()

    dump = s.dump(Simple(name='Name', value=123.4444))
    assert dump == {'name': 'Name', 'value': 123.4444}
    assert isinstance(dump, dict)

    dump = s.dumps(Simple(name='Name', value=123.4444))
    assert dump == b'{"name": "Name", "value": 123.4444}'
    assert isinstance(dump, bytes)

    load = s.load({'name': 'Name', 'value': 123.4444})
    assert load.name == 'Name'
    assert load.value == 123.44

# Generated at 2022-06-13 19:26:01.597393
# Unit test for function build_schema
def test_build_schema():
    class TestSchema:
        def __init__(self, test_field):
            self.test_field = test_field

    config = Config(default_later_case=False)
    assert build_schema(TestSchema, None, False, False) == JSONSchema



# Generated at 2022-06-13 19:26:10.645784
# Unit test for function build_type
def test_build_type():
    class EnumT(Enum):
        A = 1
        B = 2
    @dataclass_json
    @dataclass
    class T:
        pass
    @dataclass_json
    @dataclass
    class NT(T):
        pass
    @dataclass_json
    @dataclass
    class DC:
        f: NT
    @dataclass_json
    @dataclass
    class DC2:
        f: typing.Union[T, NT]

    assert isinstance(build_type(typing.List[str], {}, NT,
                                 DC.__dataclass_fields__["f"], DC), fields.List)

# Generated at 2022-06-13 19:26:14.326789
# Unit test for function schema
def test_schema():
    from typing import Optional
    from marshmallow import Schema, fields
    from dataclasses import dataclass

    @dataclass
    class Test:
        name: Optional[str]
        age: int
        # comment here will cause the type of `age` to be `object`
        # age: object

    assert schema(Test, {}, False) == {'age': fields.Int(missing=0),
                                       'name': fields.Str(missing=None,
                                                          allow_none=True)}

# schema.py ends here


# Generated at 2022-06-13 19:26:22.117360
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    # TODO: This unit test is not complete yet
    # It is simply here to make mypy happy
    class A(typing.Generic[int]):
        pass

    x = SchemaF[A]
    json_data = """{}"""
    many = True
    partial = True
    unknown = None
    kwargs = {}

    assert isinstance(x.loads(json_data, many, partial, unknown, **kwargs), A)



# Generated at 2022-06-13 19:26:29.899858
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import typing
    import json
    import marshmallow
    class PersonF(typing.Generic[str]):
        def __init__(self, name: str) -> None:
            self._name = name
        def get_name(self) -> str:
            return self._name

    class PersonSchemaF(SchemaF[PersonF]):
        class Meta:
            unknown = marshmallow.EXCLUDE
        name = marshmallow.fields.Str()
        @marshmallow.post_load
        def make_person(self, data, **kwargs) -> PersonF:
            return PersonF(**data)
    psf = PersonSchemaF()
    p = PersonF('Bob')
    assert json.dumps(psf.dump(p)) == '{"name":"Bob"}'


# Generated at 2022-06-13 19:26:31.595020
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()


# Generated at 2022-06-13 19:26:33.136960
# Unit test for function build_schema
def test_build_schema():
    # TODO
    assert True

# Generated at 2022-06-13 19:26:57.073787
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from typing import Optional
    from enum import Enum
    @dataclass
    class FieldNestedClass:
        field_a: str

    @dataclass
    class FieldNestedClass2:
        field_a: str

    @dataclass
    class FieldTest:
        field_a: FieldNestedClass = FieldNestedClass("field_a_value")
        field_b: str = "field_b_value"
        field_c: Optional[str] = "field_c_value"
        field_d: Optional[FieldNestedClass] = FieldNestedClass(
            "field_d_value")
        field_e: Optional[FieldNestedClass2] = FieldNestedClass2(
            "field_e_value")

# Generated at 2022-06-13 19:27:06.482098
# Unit test for function build_schema
def test_build_schema():
    import tests.test_base as test_base
    # First test
    class Temp:
        a: int
        b: str

    @dataclass_json
    @dataclass
    class Temp1(Temp):
        c: int = 10

    @dataclass_json
    @dataclass
    class Temp2(Temp1):
        d: typing.List[int]

    # We need to create circular imports, so requires will be checked
    from tests.test_base import Temp1, Temp2
    test_base.Temp1 = Temp1
    test_base.Temp2 = Temp2

    assert build_schema(Temp1, dataclass_json.dataclass_json(), True, False)
    assert build_schema(Temp2, dataclass_json.dataclass_json(), True, False)



# Generated at 2022-06-13 19:27:12.911673
# Unit test for method load of class SchemaF
def test_SchemaF_load():  # type: ignore
    from typing import NamedTuple
    from dataclasses import dataclass
    class T(NamedTuple):
        x: int
    x = T(1)
    schema = SchemaF.from_dataclass(T, unknown=EXCLUDE)
    assert schema.load({'x': 1}) == x
    s = schema.dumps(x)
    assert schema.loads(s) == x

# Generated at 2022-06-13 19:27:18.067696
# Unit test for constructor of class _IsoField
def test__IsoField():
    test = _IsoField()
    assert (test._serialize(datetime(2020, 2, 4, 18, 36, 12, 386356), "test", None) == "2020-02-04T18:36:12.386356")
    assert (test._deserialize("2020-02-04T18:36:12.386356", "test", None) == datetime(2020, 2, 4, 18, 36, 12, 386356))
    assert (test._deserialize(None, "test", None) is None)


# Generated at 2022-06-13 19:27:25.648399
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import datetime
    @dataclass
    class User:
        name: str
        created_at: datetime.datetime
    @dataclass
    class Message:
        user: User
        content: str
    assert schema(User, None, False) == {
        "name": fields.Str(data_key='name'),
        "created_at": _TimestampField(data_key='created_at')
    }
    assert schema(Message, None, False) == {
        "user": fields.Nested(schema(User, None, False), data_key='user'),
        "content": fields.Str(data_key='content')
    }



# Generated at 2022-06-13 19:27:35.490656
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    # type: () -> None
    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from dataclasses_json.utils import TypedSchemaF

    assert issubclass(SchemaF, TypedSchemaF)
    assert issubclass(SchemaF[int], TypedSchemaF)
    assert issubclass(SchemaF[int], TypedSchemaF[A])
    assert issubclass(SchemaF[int], TypedSchemaF[int])
    assert not issubclass(SchemaF[int], TypedSchemaF[str])

    class TestSchemaF(SchemaF[int]):  # type: ignore
        age = fields.Int()

    class TestSchema(Schema):
        age = fields.Int()


# Generated at 2022-06-13 19:27:37.617384
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class SchemaF_dumps(SchemaF[A]):
        pass



# Generated at 2022-06-13 19:27:44.705121
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass

    @dataclass
    class A:
        s: str = "test"
        x: int = 12

    @dataclass
    class Example:
        a: typing.List[A]

    assert schema(Example, SchemaType, False) == {
        'a': fields.List(fields.Nested(
            {'s': fields.String(missing='test', required=True),
             'x': fields.Integer(missing=12, required=True)},
            required=True))
    }



# Generated at 2022-06-13 19:27:57.047742
# Unit test for function build_schema
def test_build_schema():
    import unittest
    from datetime import datetime
    from dataclasses_json.api import load, loads


    @dataclass_json
    @dataclass
    class User(JSONMixin):
        name: str
        number: int
        date: datetime


    DATA = '{"name": "Luciano Ramalho", "date": "2020-03-03T12:00:00Z"}'

    with unittest.TestCase() as test_case:
        test_case.assertTrue(User.schema())
        user = loads(DATA, User)
        test_case.assertIsInstance(user, User)
        test_case.assertEqual(user.number, 0)  # default value

# Generated at 2022-06-13 19:28:00.405857
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class TestClass:
        foo: str
        bar: int

    DataClassSchema = build_schema(TestClass, {}, True, False)
    assert DataClassSchema.opts.fields == ('foo', 'bar')
    assert DataClassSchema.opts.render_module == global_config.json_module



# Generated at 2022-06-13 19:29:09.495860
# Unit test for function schema
def test_schema():
    import pytest
    from .common import Point, test_schema_class, test_schema_dict, test_schema_dict_types
    import dataclasses_json
    import marshmallow

    @dataclasses_json.dataclass_json
    class MyClass(marshmallow.Schema):
        point: Point
        def __post_init__(self):
            self.point = Point(points=100)
        class Meta:
            unknown = marshmallow.INCLUDE

    my_class_dict = MyClass.__dataclass_fields__

    @dataclasses_json.dataclass_json
    class MyClassWithDict(marshmallow.Schema):
        points: int
        result: Point
        def __post_init__(self):
            self.point = Point(points=100)

# Generated at 2022-06-13 19:29:16.999573
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    import marshmallow as mm

    class S(mm.Schema, typing.Generic[A]):  # type: ignore
        pass

    foo = S()

    f: typing.Callable = foo.loads
    x: typing.List[int] = f('[1, 2, 3]', many=True)
    x: int = f('1', many=False)



# Generated at 2022-06-13 19:29:26.498441
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class TestSchema(SchemaF[A]):
        # schema definition
        @post_load
        def make_object(self, data, **kwargs):
            return data

    # test that it is callable
    assert TestSchema().dump({}) == {}
    assert TestSchema().dumps({}) == '{}'
    assert TestSchema().load('{}') == {}
    assert TestSchema().loads('{}') == {}



# Generated at 2022-06-13 19:29:28.640387
# Unit test for function schema

# Generated at 2022-06-13 19:29:32.958866
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class C:
        i: int

    assert isinstance(build_schema(C, None, False, False), Schema)



# Generated at 2022-06-13 19:29:46.172200
# Unit test for function build_schema
def test_build_schema():
    class WithMixin:
        pass

    # noinspection PyArgumentList
    class A(WithMixin, metaclass=dataclass_json(letter_case=LetterCase.CAMEL)):
        b: typing.Optional[B]
        c: C
        name: str = ""
        start: typing.Optional[datetime] = None
        age: int = 0
        f: typing.Union[int, str] = field(
            metadata={'dataclasses_json': {'mm_field': fields.Int(allow_none=True)}})
        g: typing.List[C] = field(default_factory=list)
        h: typing.Dict[int, C] = field(default_factory=dict)
        i: typing.Callable[[], None] = lambda: None


# Generated at 2022-06-13 19:29:55.846788
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from dataclasses import dataclass
    from marshmallow import fields
    @dataclass
    class Foo:
        name: str
    @dataclass
    class Bar:
        foo: Foo = None
    @dataclass
    class Baz:
        bar: typing.List[Bar] = None
    class FooSchema(SchemaF[Foo]):
        name = fields.String()
    class BarSchema(SchemaF[Bar]):
        foo: FooSchema
    class BazSchema(SchemaF[Baz]):
        bar: typing.List[BarSchema] = None
    # test the generic type Foo
    f = Foo('foo')
    s = FooSchema()
    assert s.dump(f) == {'name': 'foo'}

# Generated at 2022-06-13 19:30:05.402044
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class WidgetSchema(SchemaF[Widget]):
        name = fields.String(required=True, allow_none=False)
        latest_purchase_date = fields.DateTime(required=True, allow_none=False)

    @dataclass
    class Widget:
        name: str
        latest_purchase_date: datetime

    name = "sprocket"
    purchase_date = datetime.now()
    widget = Widget(name, purchase_date)

    data = WidgetSchema().dump(widget)
    assert data["name"] == name
    assert data["latest_purchase_date"] == purchase_date.isoformat()


# Generated at 2022-06-13 19:30:15.922361
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from marshmallow import validates_schema, validate, fields, ValidationError
    from dataclasses_json import dataclass_json
    from dataclasses_json.mm import Configuration

    @dataclass_json(mm_field=fields.String(validate=[validates_schema]))
    @dataclass
    class A:
        a: int

    assert schema(A, Configuration, False) == {'a': fields.String(validate=[validates_schema])}
    try:
        schema(A, Configuration, True)
    except ValidationError as e:
        assert "mm_field" in str(e)

# Generated at 2022-06-13 19:30:20.554415
# Unit test for function build_schema
def test_build_schema():
    import schemathesis  # type: ignore

    from schemathesis.specs.openapi import load  # type: ignore

    from schemathesis.specs.openapi.v3 import V3Spec  # type: ignore

    from schemathesis.specs.openapi import render  # type: ignore

    from schemathesis.results import Findings  # type: ignore

    import schemathesis  # type: ignore

    from schemathesis.specs.openapi import load  # type: ignore

    from schemathesis.specs.openapi.v3 import V3Spec  # type: ignore

    from schemathesis.specs.openapi import render  # type: ignore

    from schemathesis.results import Findings  # type: ignore
    from schemathesis import Case  # type: ignore
    from dataclasses import datac