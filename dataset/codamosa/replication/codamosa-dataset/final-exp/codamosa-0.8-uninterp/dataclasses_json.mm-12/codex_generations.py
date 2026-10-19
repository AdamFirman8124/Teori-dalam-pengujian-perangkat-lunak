

# Generated at 2022-06-13 19:20:46.211110
# Unit test for function schema
def test_schema():
    DC = dataclasses.dataclass
    @dataclasses.dataclass
    class A:
        a: int

    assert schema(A, int, {}) == {'a': fields.Int()}
    assert schema(A, int, {'a': {'mm_field': fields.Int()}}) == {'a': fields.Int()}



# Generated at 2022-06-13 19:20:53.713847
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow import Schema, fields
    from marshmallow import ValidationError
    d = {}  # type: typing.Dict
    def loads_func(d: typing.Any, *args, **kwargs):
        if isinstance(d, bytes):
            return True
        else:
            return False
    SchemaF.loads = loads_func
    d = {'a': 42, 'b': [1,2,3]}
    s = SchemaF()
    r = s.loads(d, many=True)
    r = s.loads(d, many=False)


# Generated at 2022-06-13 19:20:56.284654
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    s = SchemaF()
    obj = s.load([{}, {}])


# Generated at 2022-06-13 19:21:04.066180
# Unit test for function build_type
def test_build_type():

    # TODO marshmallow_enum isn't installed in travis, so ignore tests that depend on it
    # TODO To run this test, first '$ pip install marshmallow_enum'
    try:
        from marshmallow_enum import EnumField
    except:
        return

    from dataclasses import dataclass
    from enum import Enum
    from typing import List, Dict, Optional, Set, FrozenSet, \
        Tuple, Literal, NewType, Union, Set

    from marshmallow import ValidationError

    class A(Enum):
        A = 12
        B = 17

    class B(A):
        C = 42

    @dataclass
    class Embedded:
        a: int

    @dataclass
    class Example:
        i: int
        s: str
        d: dict
        d2

# Generated at 2022-06-13 19:21:14.330797
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class A(typing.NamedTuple):
        x: str

    schemaf = SchemaF[A]()
    assert schemaf.load([{'x': 'y'}]) == [A(x='y')]
    assert schemaf.loads('[{"x": "y"}]') == [A(x='y')]
    assert schemaf.load({'x': 'y'}) == A(x='y')
    assert schemaf.loads('{"x": "y"}') == A(x='y')

# Generated at 2022-06-13 19:21:23.385257
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import Schema, fields

    class S(SchemaF[int]):
        i = fields.Int()

    s = S()
    data = s.dumps([1, 2, 3])
    assert data == '[{"i": 1}, {"i": 2}, {"i": 3}]'

    data = s.dumps(1)
    assert data == '{"i": 1}'


# Generated at 2022-06-13 19:21:32.626506
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Foo:
        a: int
        b: str = "hello"

    body = build_schema(Foo, None, False, False)
    assert body.Meta.fields == ('a', 'b')
    assert body.__name__ == 'FooSchema'
    assert isinstance(body.dump(Foo(1)), dict)
    assert body.dump(Foo(1)) == {'a': 1, 'b': 'hello'}



# Generated at 2022-06-13 19:21:38.568138
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    assert issubclass(SchemaF, Schema)
    assert issubclass(SchemaF[str], Schema[str])
    assert issubclass(SchemaF[str], SchemaF)
    assert not issubclass(SchemaF, SchemaF)
    assert not issubclass(SchemaF[str], SchemaF[str])

# Generated at 2022-06-13 19:21:43.982422
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import ValidationError
    from marshmallow_enum import EnumField
    from dataclasses_json import DataClassJsonMixin
    from enum import Enum
    from marshmallow import Schema, fields, post_load
    from datetime import datetime
    import typing

    @typing.overload
    def _post_load(self, data: typing.Dict[str, typing.Any], **kwargs) -> 'Book':
        ...

    @typing.overload
    def _post_load(self, data: typing.Dict[str, typing.Any], **kwargs) -> typing.List['Book']:
        ...


# Generated at 2022-06-13 19:21:47.860706
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
  s = typing.cast(SchemaF[int], SchemaF)
  assert s.loads([{'__type': 'int'}]) == [0]

# Generated at 2022-06-13 19:22:08.260060
# Unit test for function build_schema
def test_build_schema():
    import marshmallow
    from dataclasses import dataclass
    class A:
        pass
    @dataclass
    class B:
        number: int = 1
    
    schema = build_schema(A, A, False, False)
    try:
        schema.load({"number": 1})
    except marshmallow.exceptions.ValidationError:
        pass
    else:
        assert False
    x = build_schema(B, B, False, False)
    assert isinstance(x.load({"number": 1}), B)
    assert x.load({"number": "1"}).number == 1


# Generated at 2022-06-13 19:22:17.631410
# Unit test for constructor of class _IsoField
def test__IsoField():
    assert _IsoField()._deserialize("2019-06-01T00:00:00") == datetime(2019, 6, 1)
    assert _IsoField()._serialize(datetime(2019, 6, 1)) == "2019-06-01T00:00:00"

if sys.version_info >= (3, 7):
    from datetime import timezone
    from datetime import time
    from datetime import date

    class _DateField(fields.Field):
        def _serialize(self, value, attr, obj, **kwargs):
            if value is not None:
                return value.isoformat()
            else:
                if not self.required:
                    return None
                else:
                    raise ValidationError(self.default_error_messages["required"])


# Generated at 2022-06-13 19:22:23.948423
# Unit test for function build_schema
def test_build_schema():
    class C(metaclass=Config):
        pass

    class D:
        def __init__(self, a: int = 3, b: int = 4):
            self.a = a
            self.b = b

    class B:
        a: int = 3

    class A(metaclass=Config):
        a: typing.Optional[str] = None
        b: typing.Optional[str] = None

    class A1(metaclass=Config):
        a: typing.Optional[str] = None
        b: typing.Optional[str] = None

        def __init__(self, x: int = 1, y: int = 2):
            self.x = x
            self.y = y


# Generated at 2022-06-13 19:22:33.160484
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    def test(json_data: JsonData, many: bool = None, partial: bool = None,
             unknown: str = None, **kwargs) -> TOneOrMulti:
        return SchemaF.loads(json_data,
                             many=many, partial=partial, unknown=unknown,
                             **kwargs)

# Generated at 2022-06-13 19:22:34.806493
# Unit test for function schema
def test_schema():
    assert schema(int, None, None) == {}



# Generated at 2022-06-13 19:22:45.838894
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import List
    from marshmallow import validate
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin
    from dataclasses_json.schema import Schema, SchemaF

    @dataclass
    class Foo(DataClassJsonMixin):
        foo: str
        bar: str
        baz: List[str] = None

    m = Schema(
        {
            'foo': fields.Str(
                required=True, validate=validate.Length(max=10)),
            'bar': fields.Str(
                required=True, validate=validate.Length(max=10)),
            'baz': fields.List(fields.Str(), required=False),
        }
    )

# Generated at 2022-06-13 19:22:55.475502
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow import fields
    from marshmallow import Schema
    from marshmallow import post_load
    from dataclasses import dataclass
    from typing import Dict
    import dataclasses_json

    class MyDict(dict):
        pass

    @dataclass
    class MyDataClass:
        foo: str
        bar: int
        baz: MyDict

        @post_load
        def make(self, data: Dict, **kwargs) -> 'MyDataClass':
            return MyDataClass(**data)

    class MySchemaF(SchemaF[MyDataClass]):
        foo = fields.String()
        bar = fields.Integer()
        baz = dataclasses_json.DataClassJsonMixin.from_dict(MyDict)


# Generated at 2022-06-13 19:23:03.244392
# Unit test for function schema
def test_schema():
    @dataclasses.dataclass
    class A:
        b: str

    @dataclasses_json.dataclass_json
    class B:
        a: typing.List[A]
        c: datetime

    # TODO check if the metadata can be added back to the class
    # see test_schema

    class Test1(dataclasses_json.DataClassJsonMixin):
        b: int

    _schema = schema(Test1, Test1, True)
    assert _schema['b'] is fields.Int

    class Test2(dataclasses_json.DataClassJsonMixin):
        b: typing.Optional[int]

    _schema = schema(Test2, Test2, True)
    assert _schema['b'] is fields.Int


# Generated at 2022-06-13 19:23:06.275610
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import Schema, fields

    class Person(SchemaF[A]):
        name = fields.Str()

    obj = Person(many=False)
    obj.dump(obj)




# Generated at 2022-06-13 19:23:13.452897
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class A:
        x: int = 1
        y: int
        z: int = 2
    DataClassSchema = build_schema(A, object, True, None)
    result = DataClassSchema().dump(A(2))
    assert result =={'x': 1, 'y': 2, 'z': 2}


# Generated at 2022-06-13 19:23:44.163333
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class MySchema(SchemaF[A]):
        pass

    MySchema().load([A()])

# Generated at 2022-06-13 19:23:45.554200
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert SchemaF[int].dumps([1, 2, 3]) == '[1, 2, 3]'
    assert SchemaF[int].dumps(1) == '1'



# Generated at 2022-06-13 19:23:49.582041
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class Foo:
        def __init__(self) -> None:
            self.bar = "test"

    class FooSchemaF(SchemaF[Foo]):
        pass

    foo = Foo()
    foo_schema = FooSchemaF()
    res = foo_schema.dumps(foo)
    assert res == '{"bar": "test"}'

    res = foo_schema.dumps([foo, foo])
    assert res == '[{"bar": "test"}, {"bar": "test"}]'



# Generated at 2022-06-13 19:23:56.604651
# Unit test for function schema
def test_schema():
    from marshmallow.fields import Field
    from dataclasses_json.mm import schema
    from dataclasses_json import dataclass_json
    @dataclass_json
    @dataclass
    class A:
        x: str
        y: int
        z: typing.List[int]
        a: typing.Optional[int]
    schema(A, 'test_schema', False)
    x = A.schema()

# Generated at 2022-06-13 19:24:05.594593
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    dt = datetime.fromisoformat('2019-10-14T00:59:31.807775')
    assert f._serialize(dt, None, None) == '2019-10-14T00:59:31.807775'
    assert f._deserialize('2019-10-14T00:59:31.807775', None, None) == dt


# Generated at 2022-06-13 19:24:17.014110
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():  # type: ignore
    import json
    from dataclasses import dataclass, field
    from dataclasses_json.api import Schema, config

    @dataclass
    class MyDataClass(object):
        x: int
        y: str

    schema = Schema(MyDataClass)

    serialized = schema.dumps([
        MyDataClass(0, 'a'), MyDataClass(1, 'b'), MyDataClass(2, 'c')
    ])

    assert isinstance(serialized, str)

    deserialized = schema.loads(serialized)

    assert isinstance(deserialized, list)

    for x in deserialized:
        assert isinstance(x, MyDataClass)
        assert x.x == 1
        assert x.y == 'b'

    # Unit test for method loads of class Sche

# Generated at 2022-06-13 19:24:24.737443
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass

    @dataclass
    class Example:
        a: int = 1
        b: str = 'b'
        c: typing.Optional[int] = None
        d: typing.Optional[typing.Union[int, str]] = '1'
        e: typing.Optional[typing.Union[int, str, UUID]] = '1'
        f: typing.Optional[typing.Union[int, str, UUID]] = '123e4567-e89b-12d3-a456-426655440000'
        g: typing.Optional[typing.Union[int, str]] = 2
        h: typing.Optional[typing.Union[int, str]] = '2'
        i: typing.Optional[typing.Union[int, str]] = 3
        j

# Generated at 2022-06-13 19:24:34.507293
# Unit test for function schema
def test_schema():
    from marshmallow import fields as mm_fields
    import dataclasses
    import pytest

    # noinspection PyUnresolvedReferences
    with pytest.raises(NotImplementedError, match='Lift Schema into a type constructor'):
        SchemaF[int]()

    class SomeSchemaClass(SchemaType):
        @typing.overload
        def dump(self, obj: typing.List[int], many: bool = None) -> typing.List[int]:  # type: ignore
            pass

        @typing.overload
        def dump(self, obj: int, many: bool = None) -> int:
            pass


# Generated at 2022-06-13 19:24:45.446458
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from typing import List, Optional
    from marshmallow import fields
    from dataclasses_json import dataclass_json
    import pytest

    @dataclass_json
    @dataclass
    class MyList:
        value: List

    @dataclass_json
    @dataclass
    class Nested:
        mylist: MyList

    @dataclass_json
    @dataclass
    class Root:
        nested: Nested

    @dataclass_json
    @dataclass
    class Point:
        x: float
        y: float

    @dataclass_json
    @dataclass
    class Polygon:
        points: List[Point]

    @dataclass_json
    @dataclass
    class Shape:
        points

# Generated at 2022-06-13 19:24:48.528538
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    f = _TimestampField()
    assert f.missing == MISSING
    assert f.required == False
    assert f.error_messages == {'required': 'Missing data for required field.'}


# Generated at 2022-06-13 19:25:46.197885
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    assert field._deserialize('2020-03-22T00:00:00') == datetime(2020,3,22,0,0,0)
    assert field._deserialize('2020-01-02T01:02:03.000') == datetime(2020,1,2,1,2,3,0)


# Generated at 2022-06-13 19:25:56.448681
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass
    from marshmallow import fields
    from dataclasses_json.schema_generator import FieldResolver
    import typing

    @dataclass
    class SomeDC:
        f1: int
        f2: typing.List[int] = None

    class SomeSchema(SchemaF[SomeDC]):

        f1 = fields.Int()
        f2 = fields.List(fields.Int())

    schema = SomeSchema()
    assert schema.dump([SomeDC(1), SomeDC(2, [1, 2])]) == [
        {"f1": 1, "f2": None}, {"f1": 2, "f2": [1, 2]}
    ]

# Generated at 2022-06-13 19:26:00.223084
# Unit test for function build_schema
def test_build_schema():
    class TestSchema(BaseSchema):
        class Meta:
            fields = ('bar', 'baz')
        make_blah = post_load()(lambda *args: None)
    assert type(build_schema(None, None, None, None)) == type(TestSchema)



# Generated at 2022-06-13 19:26:07.262802
# Unit test for constructor of class _IsoField
def test__IsoField():
    from marshmallow_dataclass import class_schema
    from datetime import datetime

    # Instantiate the class _IsoField
    class TestA():
        def __init__(self):
            self.field = _IsoField()

    # Test the deserialization and serialization method
    @class_schema
    class Test(TestA):
        value: datetime

    Test().load({'value': '2020-01-15T12:00:00'}).data
    Test(value=datetime(2020, 1, 15, 12, 0, 0)).dump().data



# Generated at 2022-06-13 19:26:11.629333
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    @dataclass
    class A:
        x: int
        y: int

    class ASchema(SchemaF[A]):
        x = fields.Int()
        y = fields.Int()

    a = A(1, 2)
    assert ASchema().loads(json.dumps(a)) == a

    a = [A(1, 2)]
    assert ASchema().loads(json.dumps(a)) == a

# Generated at 2022-06-13 19:26:14.423755
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class Foo(object):
        pass
    data = '[{"__type": "Foo"}]'
    foo = SchemaF.loads(data)
    assert foo[0].__class__.__name__ == 'Foo'


# Generated at 2022-06-13 19:26:25.360556
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class Foo(typing.NamedTuple):
        a: int
        b: str

    class FooSchema(SchemaF[Foo]):
        pass

    s = dumps(FooSchema(), Foo(1, 'foo'))
    assert s == '{"a": 1, "b": "foo"}'

    s = dumps(FooSchema(many=True), [Foo(1, 'foo')])
    assert s == '[{"a": 1, "b": "foo"}]'

    s = FooSchema().dumps([Foo(1, 'foo')])
    assert s == '[{"a": 1, "b": "foo"}]'

    s = FooSchema().dumps(Foo(1, 'foo'))
    assert s == '{"a": 1, "b": "foo"}'

# Generated at 2022-06-13 19:26:33.973227
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class A:
        def __init__(self, x: typing.List[float]):
            self.x = x
    schema = SchemaF[A].from_dataclass(A)
    a = schema.loads('{"x":[1,2,3]}', many = False)
    assert isinstance(a, A)
    assert isinstance(a.x, list)
    assert isinstance(a.x[0], float)
    assert a.x[0] == 1.0


# Generated at 2022-06-13 19:26:45.788218
# Unit test for function build_schema
def test_build_schema():
    class Mixin:
        pass
    class Cls(Mixin):
        field: str
    cls = Cls
    mixin = Mixin
    infer_missing = False
    partial = False
    d = build_schema(cls=cls, mixin=mixin, infer_missing=infer_missing, partial=partial)
    assert isinstance(d, type)
    assert d.__name__ == 'ClsSchema'
    assert isinstance(d.Meta, type)
    assert d.Meta.__name__ == 'Meta'
    assert d.Meta.fields == ('field',)
    assert d.make_cls(None, **None) == None
    assert isinstance(d.dumps(None, **None), str)
    assert isinstance(d.dump(None, many=None), dict)

# Generated at 2022-06-13 19:26:55.049684
# Unit test for function build_type
def test_build_type():
    from typing import Dict, List, Optional

    from dataclasses import dataclass

    class NestedMixin:
        pass

    @dataclass
    class Nested(NestedMixin):
        foo: str

    @dataclass
    class SubNested(Nested):
        bar: str

    @dataclass
    class TestDataclass:
        foo: str
        bar: int
        nested: Nested
        l: List[int]
        dict_: Dict[str, str]
        odict: Optional[Dict[int, str]]
        union: typing.Union[int, str, Nested]
        sub_union: typing.Union[int, str, SubNested]
        nested_list: List[Nested]

    from dataclasses_json.mm_schema import JsonSche

# Generated at 2022-06-13 19:29:27.398780
# Unit test for function build_type
def test_build_type():
    import datetime

    from .dataclasses import dataclass_json
    from .schema import _SchemaType

    @dataclass_json
    @dataclass
    class Foo:
        name: str

        @classmethod
        def schema(cls):
            return _SchemaType('Foo', dataclass=cls,
                               pre_dump_one=lambda x: {'name': x.name},
                               post_load_one=lambda x: Foo(x['name']))


    @dataclass_json
    @dataclass
    class Bar:
        date: Optional[datetime.date]

    @dataclass_json
    @dataclass
    class Baz:
        lst: List[Bar]


# Generated at 2022-06-13 19:29:41.614015
# Unit test for function build_type
def test_build_type():
    class TestClass(object):
        pass
    # Test 1
    # Test a simple class with nothing special.
    the_type = type(TestClass)
    class Options(object):
        def __init__(self):
            self.field_many = False
    options = Options()
    mixin = dataclasses_json.dataclass_json()
    # We need to fake a field.
    class Field(object):
        def __init__(self):
            self.name = "TestClass"
            self.type = the_type
    field = Field()
    cls = TestClass
    check = build_type(the_type, options, mixin, field, cls)
    assert type(check) == fields.Field
    assert check.required == False
    # Test 2
    # Test a class that has a dat

# Generated at 2022-06-13 19:29:45.547018
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Person:
        name: str
        age: int
        father: typing.Optional[Person]

    schema = build_schema(Person, dataclass_json.Mapping, False, False)
    assert set(schema.Meta.fields) == {'name', 'age', 'father'}
    assert schema().make_person(
        {"name": "Eric", "age": 3, "father": {"name": "Noah", "age": 47}}) == Person(
        name="Eric", age=3, father=Person(name="Noah", age=47))



# Generated at 2022-06-13 19:29:55.210216
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class TestDump:
        a: int
        b: str
        c: Optional[TestDump]
        d: Optional[list]
        e: datetime
        f: Decimal
        g: UUID
        h: UUID = None

    TestDumpSchema = build_schema(TestDump, dataclass, False, False)

# Generated at 2022-06-13 19:30:06.322474
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        SchemaF.dumps[User, List[User]](SchemaF, None, many=False)
        assert "This class is helper only" in str(w[-1].message)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        SchemaF.dumps[User, List[User]](SchemaF, None)
        assert "This class is helper only" in str(w[-1].message)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        SchemaF.dumps[User, List[User]](SchemaF, None, many=True)

# Generated at 2022-06-13 19:30:18.213082
# Unit test for function build_type
def test_build_type():
    from marshmallow import fields
    from marshmallow_enum import EnumField
    from dataclasses_json.core import _handle_undefined_parameters_safe

    class _UnionField(fields.Field):
        def __init__(self, desc, cls, field, *args, **kwargs):
            self.desc = desc
            self.cls = cls
            self.field = field
            super().__init__(*args, **kwargs)

    class TestAncestor(object):
        def __repr__(self):
            return 'TestAncestor'

    class TestChild1(TestAncestor):
        def __repr__(self):
            return 'TestChild1'

    class TestChild2(TestAncestor):
        def __repr__(self):
            return 'TestChild2'

