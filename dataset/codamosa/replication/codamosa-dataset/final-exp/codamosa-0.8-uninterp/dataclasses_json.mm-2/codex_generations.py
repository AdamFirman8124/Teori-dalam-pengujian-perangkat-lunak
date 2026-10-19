

# Generated at 2022-06-13 19:20:40.858955
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json, config, Undefined

    @dataclass_json
    @dataclass
    class Simple:
        e: int = Undefined
        d: list = Undefined
    
    class SimpleSchema(Schema):
        e = fields.Int()
        d = fields.List(fields.Field())
    
    assert SimpleSchema().fields == schema(Simple, {}, False)
    
    @dataclass_json()
    @dataclass
    class Simple:
        e: int = Undefined
        d: list = Undefined
    
    class SimpleSchema2(Schema):
        e = fields.Int()
        d = fields.List(fields.Field())
    

# Generated at 2022-06-13 19:20:52.394453
# Unit test for function schema
def test_schema():
    class User:
        name: str
        age: int

    def load_func(val):
        return 'load_func'

    def dump_func(val):
        return 'dump_func'


# Generated at 2022-06-13 19:20:55.408491
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class Foo(SchemaF):
        pass

    assert Foo().load([{'foo': 'bar'}]) == [{'foo': 'bar'}]


# Generated at 2022-06-13 19:20:57.041589
# Unit test for function schema
def test_schema():
    assert isinstance(schema(None, None, None), dict)


# Generated at 2022-06-13 19:20:57.632432
# Unit test for function schema
def test_schema():
    pass



# Generated at 2022-06-13 19:21:02.895883
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():  # pragma: no cover
    schema = SchemaF[List[str]]()
    assert schema.loads('["a", "b"]') == ["a", "b"]
    schema = SchemaF[int]()
    assert schema.loads('2') == 2


# Generated at 2022-06-13 19:21:04.638476
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert isinstance(SchemaF[str].dumps(['a', 'b']), str)


# Generated at 2022-06-13 19:21:14.996512
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class Person:
        def __init__(self, name):
            self.name = name

    p = Person('Joe')
    class PersonSchema(SchemaF[Person]):
        name = fields.Str()

    s = PersonSchema()
    pd = s.dump(p)
    assert {'name': 'Joe'} == pd

    pl = [Person('Joe'), Person('Jane')]
    pdl = s.dump(pl)
    assert [{'name': 'Joe'}, {'name': 'Jane'}] == pdl

    assert {'name': 'Joe'} == s.dump(p)



# Generated at 2022-06-13 19:21:22.798695
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin
    from marshmallow import Schema, fields

    class Origin(DataClassJsonMixin):
        a: str
        b: int

    @dataclass
    class MyClass(Origin):
        c: Origin
        d: typing.Optional[str] = None
    schema = schema(MyClass, Origin, True)
    assert(isinstance(schema, dict))
    assert(schema['c'] == fields.Nested(Origin.schema()))
    assert(schema['d'] == fields.Str(allow_none=True, missing=None))



# Generated at 2022-06-13 19:21:29.306172
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Klass:
        a:int

    k = Klass(1)
    assert build_schema(Klass, None, True, False) is not None
    assert build_schema(Klass, None, True, False)(k) is not None
# Unit tests for function _get_required_fields_dict

# Generated at 2022-06-13 19:21:53.704076
# Unit test for function schema
def test_schema():
    import dataclasses
    from marshmallow_enum import EnumField  # type: ignore

    class Enum(Enum):
        A = 1
        B = 2

    @dataclasses.dataclass
    class A:
        hello: str
        world: int
        uuid: UUID
        missing: int = 5
        default_factory: int = dataclasses.field(default_factory=lambda: 5)
        optional: typing.Optional[str] = None
        none_with_union: typing.Optional[typing.Union[str, int]] = None
        none_without_union: typing.Optional[str] = None
        enum_field: Enum = Enum.A
        dataclass_field: typing.Optional[Enum] = None
        list_field: typing.List[str] = datac

# Generated at 2022-06-13 19:21:58.105297
# Unit test for function build_type
def test_build_type():
    from typing import Union
    from marshmallow import Schema, fields
    from marshmallow_enum import EnumField
    from marshmallow.exceptions import ValidationError
    from dataclasses import dataclass
    from enum import Enum
    from dataclasses_json.api import mm_field
    from dataclasses_json.core import Schema

    @dataclass
    class SubSchema(CoreSchema):
        f: Union[str, int] = mm_field(str)
        g: str = mm_field(str)
    #     h: str = mm_field(str)
    #     h: int = mm_field(str)

    @dataclass
    class Schema(CoreSchema):
        a: bool = mm_field(bool)
        b: str = mm_field(str)
        c

# Generated at 2022-06-13 19:22:03.217145
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Example:
        x: int = 1
        y: str = "example"

    class Mixin:
        pass

    assert isinstance(build_schema(Example, Mixin, False, False), type)

# Generated at 2022-06-13 19:22:04.390316
# Unit test for function build_type
def test_build_type():
    assert 1



# Generated at 2022-06-13 19:22:12.792431
# Unit test for function build_schema
def test_build_schema():
    class MyType:
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            if isinstance(other, MyType):
                return self.x == other.x

        def __repr__(self):
            return f"MyType({self.x!r})"

        @classmethod
        def from_json(cls, json_data):
            return cls(json_data["x"])

        def to_json(self):
            return {"x": self.x}

    @dataclass_json(mm_field=None)
    @dataclass
    class A:
        x: MyType

    def make_instance(self, kvs, **kwargs):
        return kvs

    DataClassSchema: typing.Type[SchemaType]

# Generated at 2022-06-13 19:22:17.471562
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from typing import List, Any
    from dataclasses_json.mm import Mm

    @dataclass
    class A(Mm):
        a: str
        b: int

    assert schema(A, Mm, False) == {
        'a': fields.Str(missing=MISSING, allow_none=False),
        'b': fields.Int(missing=MISSING, allow_none=False)
    }



# Generated at 2022-06-13 19:22:22.045060
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Persoon:
        naam: str
    p = Persoon(naam="John Doe")
    persistoon = build_schema(Persoon,str,False,False)
    assert persistoon(many=False).dump(p) == {'naam': 'John Doe'}
    assert persistoon(many=False).load({"naam":"John Doe"}) == p
    assert persistoon(many=True).dump([p]) == [{'naam': 'John Doe'}]
    assert persistoon(many=True).load([{'naam': 'John Doe'}]) == [p]




# Generated at 2022-06-13 19:22:27.763223
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    pass



# Generated at 2022-06-13 19:22:36.995946
# Unit test for function build_schema
def test_build_schema():
    class Foo:
        a: int
    class FooMeta:
        fields = ('a', )
        render_module = 'json'
    @post_load
    def make_instance(self, kvs, **kwargs):
        return _decode_dataclass(Foo, kvs, True)
    def dumps(self, *args, **kwargs):
        if 'cls' not in kwargs:
            kwargs['cls'] = _ExtendedEncoder
        return Schema.dumps(self, *args, **kwargs)
    def dump(self, obj, *, many=None):
        dumped = Schema.dump(self, obj, many=many)


# Generated at 2022-06-13 19:22:47.518007
# Unit test for function schema
def test_schema():
    from .mixins import SchemaMixin

    @dataclass_json
    @dataclass
    class Test(SchemaMixin):
        a: str

    @dataclass_json
    @dataclass
    class Test2(SchemaMixin):
        a: str
        b: List[int]

    @dataclass_json
    @dataclass
    class Test3(SchemaMixin):
        a: str

    @dataclass_json
    @dataclass
    class Test4(SchemaMixin):
        a: UUID

    @dataclass_json
    @dataclass
    class Test5(SchemaMixin):
        a: str

    @dataclass_json
    @dataclass
    class Test6(SchemaMixin):
        a: str


# Generated at 2022-06-13 19:23:06.059876
# Unit test for function build_schema
def test_build_schema():
    import dataclasses

    import unittest

    class TestSchema(Schema):
        age: typing.Optional[int] = fields.Int(required=False, default=None)

        @property
        def r(self):
            return self.age > 30

    class _NestedClass(typing.Generic[A]):
        a: A

    @dataclasses.dataclass
    class _Nested(typing.Generic[A]):
        a: A

    @dataclasses.dataclass
    class TestDataClass:
        age: typing.Optional[
            typing.Union[int, typing.List[int], _Nested[int], str,
                         typing.List[str], _Nested[
                             str], _NestedClass[int], _NestedClass[str]]]


# Generated at 2022-06-13 19:23:12.794703
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class Tmp(DataClassJsonMixin):
        a: str
        b: str


    assert schema(Tmp, DataClassJsonMixin, False) == {'a': fields.Str(), 'b': fields.Str()}



# Generated at 2022-06-13 19:23:20.748181
# Unit test for function build_schema
def test_build_schema():
    options, mixin = _get_default_config(None)
    cls = build_schema(C, mixin, options.infer_missing, options.partial)
    assert isinstance(cls.Meta, type)
    assert len(cls.Meta.fields)==len(dc_fields(C))
    assert issubclass(cls, Schema)
    assert hasattr(cls, "make_c")
    assert len(cls.declared_fields) == len(schema(C, mixin, options.infer_missing))
    assert hasattr(cls, "dumps")


# Generated at 2022-06-13 19:23:28.792630
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Cls:
        field_1: str
        field_2: int

    schema = build_schema(Cls, mixin=None, infer_missing=False, partial=False)
    assert isinstance(schema, type)
    assert isinstance(schema.field_1, fields.Str)
    assert isinstance(schema.field_2, fields.Int)
    assert schema.Meta.fields == ('field_1', 'field_2')



# Generated at 2022-06-13 19:23:38.981827
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from .dataclass_config import dataclass_json

    @dataclass
    class Person:
        name: str
        age: int

    @dataclass_json(letter_case=LetterCase.CAMEL)
    class A:
        b: List[str]
        c: Dict[str, str]
        d: Tuple[int, str, Person]
        e: Callable
        f: Any
        g: int = 42
        h: Optional[List[int]] = [0, 1, 2]

    s = build_schema(A, Schema, True, False)

    assert issubclass(s, Schema)
    assert s.Meta.fields == ('b', 'c', 'd', 'e', 'f', 'g', 'h')


# Generated at 2022-06-13 19:23:47.495509
# Unit test for function build_schema
def test_build_schema():
    from .diff import Diff, DiffOperation
    
    @dataclass
    class MyDataClass:
        a:int
        b:int
        c:int = field(metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        d: typing.Optional[int] = None
        e: typing.Optional[int] = field(default=None)
        k: typing.Union[str, int, None] = None
        l: typing.Union[str, int, None] = field(default=None)
        f: typing.List[str]
        g: typing.List[str] = field(default_factory=lambda: [])
        h: typing.Dict[str, int]
        i: typing.MutableMapping[str, int]
        j: typing.OrderedDict

# Generated at 2022-06-13 19:23:53.496212
# Unit test for function build_schema
def test_build_schema():
    """
    Test whether we can convert a dataclass into a Schema
    """
    import typing
    import marshmallow.fields as fields
    @dataclass_json
    @dataclass
    class MyClass:
        field1: str
        field2: int = 3

    mixin = dataclass_json.DataClassJsonMixin
    fields_to_be_loaded = ['field1', 'field2']
    schema = build_schema(MyClass, mixin, True, False)
    assert schema.__name__ == "MyClassSchema"
    assert len(schema().fields) == len(fields_to_be_loaded)
    for key, field in schema().fields.items():
        assert isinstance(field, fields.String) or isinstance(field, fields.Integer)
        assert key in fields_

# Generated at 2022-06-13 19:24:05.122942
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    with warnings.catch_warnings(record=True) as warns:
        f = _TimestampField()
        assert len(warns) == 1
        assert isinstance(warns[0].message, DeprecationWarning)
        assert str(warns[0].message) == (
            'The class dataclasses_json._TimestampField is deprecated and '
            'will be removed in the next version. Use marshmallow.fields.Field '
            'instead.'
        )
    # TODO: Use assert_raises_regex to check arguments of error message.
    assert f.deserialize(None) is None
    assert f.deserialize('1234') == datetime(1970, 1, 1, 0, 20, 34)


# Generated at 2022-06-13 19:24:12.916514
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclasses.dataclass
    class A:
        foo: str = "foo"
        bar: int = 1

    schema = dacite.from_dict(SchemaF[A], dict(model=A))
    data = schema.dump([A(), A()], many=True)
    assert data == [{'foo': 'foo', 'bar': 1}, {'foo': 'foo', 'bar': 1}]

    data = schema.dump(A(), many=False)
    assert data == {'foo': 'foo', 'bar': 1}



# Generated at 2022-06-13 19:24:21.455057
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class DC:
        d: int

    assert DC.schema() == build_schema(DC, typing.Any, False, False)

    @dataclass
    class DC:
        d: int
        s: str

    assert DC.schema() == build_schema(DC, typing.Any, False, False)

    @dataclass
    class DC:
        d: int
        d2: typing.Optional[int]

    assert DC.schema() == build_schema(DC, typing.Any, False, False)



# Generated at 2022-06-13 19:24:49.982521
# Unit test for function build_schema
def test_build_schema():
    class Simple(Schema):
        name: str
        age: int
        id: UUID
        married: bool

    class Config:
        json_module = simplejson

    def test_function(cls, mixin, infer_missing, partial):
        return build_schema(cls, mixin, infer_missing, partial)

    assert test_function(Simple, Config, infer_missing=True, partial=True)
# End of unit test



# Generated at 2022-06-13 19:24:52.340323
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class X:
        pass
    s = SchemaF.load([{'x':0}, {'x':0}], many=True)
    assert type(s) is list



# Generated at 2022-06-13 19:25:01.613761
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from enum import IntEnum

    class MyEnum(IntEnum):
        A = 1
        B = 2

    @dataclass_json
    @dataclass
    class MyDataClass:
        value: str

    @dataclass_json
    @dataclass
    class MyDataClass1:
        value: MyEnum

    class MyDataClassSchema(SchemaF[MyDataClass]):
        value = fields.Str()

    class MyDataClassSchema1(SchemaF[MyDataClass1]):
        value = EnumField(MyEnum)

    data = '{"value": "hello world"}'
    MyDataClassSchema().loads(data, many=False)
    MyDataClassSchema().loads(data, many=True)

    data = '[{"value": "hello world"}]'

# Generated at 2022-06-13 19:25:09.432845
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from marshmallow import fields
    from dataclasses import field
    from typing import Optional, List
    from marshmallow_enum import EnumField
    from enum import Enum

    @dataclass
    class A:
        a: int = field(metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        b: str = 'b'
        c: str = None
        d: bool = False
        e: int = 1
        f: Optional[int] = None
        g: bool = field(default_factory=bool)
        h: List[int]
        i: List[int] = field(default_factory=list)
        j: List[int] = field(default_factory=lambda: [1,2,3])
        k

# Generated at 2022-06-13 19:25:17.682370
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    pass
    # FIXME write this test
    #my_list: typing.List[int] = [1]
    #my_int: int = 1
    #SchemaF[int]().dumps(my_list, many=True)
    #SchemaF[int]().dumps(my_int)
    #SchemaF[int]().dumps(1.1)  # will fail

    # see https://docs.python.org/3/library/typing.html#typing.Generic for how to use Generic
    # with ClassVar, TypeVar, and Any

# Generated at 2022-06-13 19:25:24.475103
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import List, Tuple, Optional
    from marshmallow import Schema

    class InnerSchema(Schema):
        i = fields.Int()

    class OuterSchema(Schema):
        b = fields.Bool()
        s = fields.Str()
        a = fields.List(fields.Int())
        t = fields.Tuple((fields.Int(), fields.Int()))
        e = fields.Nested(InnerSchema)
        opt_str = fields.Str(allow_none=True)

    obj = OuterSchema().dump({"b": True, "s": "hihi", "a": [1, 2, 3], "t": (1, 2), "e": {"i": 6}, "opt_str": None})

# Generated at 2022-06-13 19:25:31.907309
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from typing_extensions import Literal
    from marshmallow import fields
    from marshmallow.validate import OneOf

    class SchemaFStub(SchemaF):
        f = fields.Str(validate=OneOf(['1', '2', '3']))

    assert SchemaFStub.loads('{"f": "1"}') == SchemaFStub(f='1')
    assert SchemaFStub.loads('[{"f": "1"}, {"f": "2"}]') == [SchemaFStub(f='1'), SchemaFStub(f='2')]

    class SchemaFStub2(SchemaF):
        f = fields.Str(validate=OneOf(['1', '2', '3']))


# Generated at 2022-06-13 19:25:37.161901
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json, config
    import pytest
    from marshmallow import fields
    import marshmallow
    @dataclass
    class Person:
        name: str
        age: int = None

    @dataclass_json
    class PersonSchema(Person, Schema):
        __dataclass_fields__ = schema(Person, PersonSchema, config.INFER_MISSING)

    assert isinstance(PersonSchema.schema()['age'], fields.Integer)
    assert isinstance(PersonSchema.schema()['name'], fields.String)



# Generated at 2022-06-13 19:25:48.529683
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from typing import Dict, List, Union, TypeVar
    from marshmallow import Schema, fields, post_load
    from dataclasses import dataclass
    import json

    class NodeType(Enum):
        PROBLEM = 1
        SOLUTION = 2

    @dataclass
    class Node(SchemaF[A]):
        type: NodeType
        name: str
        children: List[A] = None

    @dataclass
    class NodeSchema(SchemaF[A]):
        type: NodeType = EnumField(NodeType, by_value=True, data_key='type')
        name: str = fields.Str()

# Generated at 2022-06-13 19:25:52.147956
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    assert f._deserialize("2018-10-11T09:52:45+00:00") == datetime(2018, 10, 11, 9, 52, 45)


# Generated at 2022-06-13 19:28:14.744905
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    @dataclass
    class Parent:
        num1: float
        num2: float

    @dataclass
    class Child:
        num: float
        parent: Parent


# Generated at 2022-06-13 19:28:20.555166
# Unit test for function schema
def test_schema():
    from marshmallow import fields
    from typing import Optional
    from dataclasses import dataclass, field
    import dataclasses_json
    @dataclass
    class Child:
        x: int = field(metadata=dataclasses_json.config(mm_field=fields.Int(required=True)))

    @dataclass
    class Parent:
        name: str
        child: Optional[Child] = None

    s = schema(Parent, dataclasses_json.DataClassJsonMixin, True)
    assert isinstance(s['child'], fields.Nested)
    assert s['child'].schema.__fields__['x'].required



# Generated at 2022-06-13 19:28:28.331122
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    assert field is not None

if sys.version_info >= (3, 7):
    from dataclasses import dataclass

    class _ConstructorSchema(Schema):
        @post_load
        def make_object(self, data, **kwargs):
            try:
                cls = dataclasses.dataclass(**data)
            except TypeError as te:
                raise ValidationError(f'{te}')
            return cls

# Generated at 2022-06-13 19:28:34.414154
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json.annotations import from_json, to_json
    from marshmallow import fields

    @dataclass
    class Foo:
        a: int = from_json(to_json(fields.Int()))
        b: str = from_json(to_json(fields.Str()))
        c: float = from_json(to_json(fields.Float()))
        d: str = from_json(to_json(fields.Str()), letter_case='camel')
        f: typing.List[int] = from_json(to_json(fields.List(fields.Int())))

# Generated at 2022-06-13 19:28:36.761721
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    obj = [1, 2, 3]
    many: bool = True
    *args, kwargs = (1, 2)
    SchemaF.dumps(obj, many, *args, **kwargs)
    assert many
    assert (1, 2) == args
    assert {} == kwargs


# Generated at 2022-06-13 19:28:44.173511
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import fields

    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    class PersonSchema(SchemaF[Person]):
        name = fields.String()
        age = fields.Integer()

    o = Person('bob', 26)
    schema = PersonSchema()
    x = schema.dump(o)
    assert x == {'name': 'bob', 'age': 26}


# Generated at 2022-06-13 19:28:52.150249
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class A:
        x: int

    @dataclass
    class B:
        a: int
        b: A

    the_schema = build_schema(B, None, False, False)
    x = the_schema()

    xx = x.dump(B(a=1, b=A(x=1)))
    assert xx == {'a': 1, 'b': {'x': 1}}

    assert x.load(xx) == B(a=1, b=A(x=1))
    xx = {"a": 1, "b": {"x": 1}}
    assert x.loads(json.dumps(xx)) == B(a=1, b=A(x=1))



# Generated at 2022-06-13 19:28:53.002869
# Unit test for function build_type
def test_build_type():
    pass


# Generated at 2022-06-13 19:29:05.686332
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    assert issubclass(SchemaF, Schema)
    assert issubclass(SchemaF[str], SchemaF)
    assert issubclass(SchemaF[str], Schema)
    assert issubclass(SchemaF[str], typing.Generic[str])
    try:
        SchemaF()
        assert False
    except NotImplementedError:
        pass
    import typing
    # type: ignore
    import dataclasses
    @dataclasses.dataclass
    class User:  # type: ignore
        name: str
        age: int
    class UserSchema(SchemaF[User]):  # type: ignore
        name = fields.String()
        age = fields.Integer()

# Generated at 2022-06-13 19:29:13.325026
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    obj = SchemaF[float]()
    obj.loads(b'[1, 2, 3]', many=True)  # passes
    obj.loads(b'{"x": "y"}')  # passes
    obj.loads(b'[1, 2, 3]')  # fails (many=None but input is a list)
