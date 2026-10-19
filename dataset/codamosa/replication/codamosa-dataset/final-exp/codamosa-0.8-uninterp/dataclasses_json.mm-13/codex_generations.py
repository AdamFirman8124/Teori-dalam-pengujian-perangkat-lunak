

# Generated at 2022-06-13 19:20:51.885018
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from dataclass_json import DataClassJsonMixin, config
    from marshmallow import Schema, fields

    @dataclass
    class DataNested(DataClassJsonMixin):
        name: str = config(field_name='user_name')

    @dataclass
    class Data(DataClassJsonMixin):
        name: str = config(field_name='user_name')
        age: int
        nested: DataNested

    schema = build_schema(Data, DataClassJsonMixin, True, False)
    assert issubclass(schema, Schema)
    assert set(schema().fields.keys()) == {'user_name', 'age', 'nested'}
    assert schema().fields['user_name'] == fields.Str
    assert schema

# Generated at 2022-06-13 19:20:55.515696
# Unit test for function build_type
def test_build_type():
    assert build_type(int,{},None,None,None)==fields.Int()
    assert build_type(float,{},None,None,None)==fields.Float()
    assert build_type(type(None),{},None,None,None)==fields.Raw()
    assert build_type(typing.Sequence,{},None,None,None)==fields.Sequence()


# Generated at 2022-06-13 19:21:04.822154
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    import json

    @dataclass_json
    @dataclass
    class Test:
        a: str = 'hello'

    class TestSchema(SchemaF[Test]):
        a: str = fields.Str()

    def test():
        schema = TestSchema()
        serialized = schema.dumps(Test())
        d = json.loads(serialized)
        b = schema.load(d)
        assert isinstance(b, Test)
        # we use the generic loads here so that we can specify a list of Test instances
        b = schema.loads(serialized, many=True)
        assert isinstance(b, typing.List)
        b = schema.load(d, many=True)
        assert isinstance(b, typing.List)
    test()



# Generated at 2022-06-13 19:21:17.719266
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from datetime import datetime
    from marshmallow import Schema, fields, post_process, pre_load
    from dataclasses import dataclass
    from decimal import Decimal

    @dataclass
    class Dummy:
        a: Decimal
        b: int
        c: float
        d: datetime
        e: typing.List[int]

        def __post_init__(self):
            self.a += 1

        @staticmethod
        def _deserialize_a(value):
            return Decimal(value) + 1

        @staticmethod
        def _deserialize_d(value):
            return datetime.fromisoformat(value)

    class DummySchema(Schema):
        a = fields.Decimal()
        b = fields.Int()
        c = fields.Float()
        d

# Generated at 2022-06-13 19:21:21.405627
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    t = datetime.now()
    t = _TimestampField()._serialize(t, None, None)
    assert _TimestampField()._deserialize(t, None, None)



# Generated at 2022-06-13 19:21:28.629211
# Unit test for function build_schema
def test_build_schema():
    class A:
        pass
    field = A()
    field.name = 'a'
    field.type = 1
    field.default = ...
    field.default_factory = ...
    field.metadata = None
    class B:
        a = 1
    with patch('marshmallow_dataclass.__main__.dc_fields',
               MagicMock(return_value=[field])):
        with patch('marshmallow_dataclass.__main__.schema',
                   MagicMock(return_value={'a': 'b'})):
            with patch('marshmallow_dataclass.__main__.SchemaType',
                       MagicMock()):
                res = build_schema(B, None, None, None)
                assert res is SchemaType



# Generated at 2022-06-13 19:21:36.024274
# Unit test for function build_schema
def test_build_schema():
    from typing import List
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin
    @dataclass
    class C(DataClassJsonMixin):
        x: int

    @dataclass
    class AAA(DataClassJsonMixin):
        t: typing.Optional[C]
    assert build_schema(AAA, DataClassJsonMixin, False, False)



# Generated at 2022-06-13 19:21:44.069124
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import mm
    from marshmallow import fields

    @dataclass
    class A:
        name: str

    @dataclass
    class B:
        id: int
        name: str

    @dataclass
    class C:
        a: typing.List[A]
        b: typing.List[B]

    class D:
        @classmethod
        def schema(cls):
            return mm.model_schema(cls, mm.Schema)

    @mm.model_schema
    @dataclass
    class E:
        a: typing.List[A]
        b: typing.List[B]


# Generated at 2022-06-13 19:21:57.009750
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: str = "foo"

    s = SchemaF[A]()
    assert s.dumps(A(1, b="bar")) == '{"a": 1, "b": "bar"}'
    assert s.dumps(A(1), many=False) == '{"a": 1, "b": "foo"}'
    assert s.dumps([A(1, b="bar"), A(2, b="baz"), A(3)]) == '[{"a": 1, "b": "bar"}, {"a": 2, "b": "baz"}, {"a": 3, "b": "foo"}]'



# Generated at 2022-06-13 19:22:04.865438
# Unit test for function schema
def test_schema():
    import dataclasses
    import typing
    import marshmallow
    from dataclasses_json.mm import Config

    @dataclasses.dataclass
    class DC1:
        i: int
        s: str

    @dataclasses.dataclass
    class DC2(DC1):
        l: typing.List[int]

    @dataclasses.dataclass
    class DC3(DC2):
        d: typing.Dict[str, int]

    @dataclasses.dataclass
    class DC4(DC3):
        u: typing.Union[int, None]

    @dataclasses.dataclass
    class DC5(DC4):
        optional: typing.Optional[int]

    @dataclasses.dataclass
    class MyDC(DC5):
        optional_list: typing

# Generated at 2022-06-13 19:22:19.985209
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField()
    value = datetime.fromisoformat('2017-10-26T11:42:38.819500')
    assert field._serialize(value, None, None) == '2017-10-26T11:42:38.819500'


# Generated at 2022-06-13 19:22:27.706897
# Unit test for function schema
def test_schema():
    assert schema.__code__.co_argcount == 3



# Generated at 2022-06-13 19:22:35.318719
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass
    @dataclass
    class A:
        a: str
    a = A(a='3')
    f = SchemaF[A]()
    res: str = f.dumps(a)
    assert res == '{"a": "3"}'
    aList = [A(a='3'), A(a='4'), A(a='5')]
    resList: List[str] = f.dumps(aList)
    assert resList == ['{"a": "3"}', '{"a": "4"}', '{"a": "5"}']


# Generated at 2022-06-13 19:22:50.517164
# Unit test for function schema
def test_schema():
    import marshmallow.fields
    from dataclasses_json import dataclass_json
    from typing import Optional, Dict, List, Union

    @dataclass_json
    @dataclass
    class Inner:
        id: int

    @dataclass_json
    @dataclass
    class Mixin:
        name: str

    @dataclass_json
    @dataclass
    class Outer:
        inner: Inner
        age: int
        name: str = 'Jane'
        mixin: Mixin

    s = Schema.from_dict(schema(Outer, Mixin, False))
    assert type(s.declared_fields['inner']) == fields.Nested
    assert s.declared_fields['inner'].many == False

# Generated at 2022-06-13 19:22:59.520913
# Unit test for function schema
def test_schema():
    from typing import List, Optional
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class AC:
        a: int

    @dataclass
    class A:
        a: int
        b: List[int]
        c: Optional[AC]
        d: Optional[int]

    sd = schema(A, AC, False)
    assert isinstance(sd['a'], fields.Int)
    assert isinstance(sd['b'], fields.List)
    assert isinstance(sd['c'], fields.Nested)
    assert isinstance(sd['d'], fields.Int)



# Generated at 2022-06-13 19:23:07.811034
# Unit test for function build_schema
def test_build_schema():
    class Mixin:
        ...
    class A:
        pass
    def f():
        pass
    a1 = build_schema(A, Mixin, infer_missing=True, partial=True)
    a2 = build_schema(A, Mixin, infer_missing=True, partial=False)
    assert a1 == a2
    a3 = build_schema(A, Mixin, infer_missing=False, partial=True)
    assert a1 == a3
    a4 = build_schema(A, Mixin, infer_missing=False, partial=False)
    assert a1 == a4
    class B:
        pass
    b1 = build_schema(B, Mixin, infer_missing=True, partial=True)
    assert b1 != a1

# Generated at 2022-06-13 19:23:09.465052
# Unit test for function build_schema
def test_build_schema():
    pass


# Generated at 2022-06-13 19:23:20.027946
# Unit test for function build_type
def test_build_type():
    from dataclasses_json.mm_common import data_class_json

    @data_class_json
    class Simple:
        x: int

    @data_class_json
    class Container:
        a: typing.Optional[Simple]
        b: List[Simple]

    @data_class_json
    class Toto:
        x: typing.Optional[Simple]
        y: List[Simple]
        z: Simple

    # Check typed fields
    assert build_type(Simple, {}, data_class_json, Container.a, Container) == fields.Nested(Simple.schema())
    assert build_type(List[Simple], {'field_many': True}, data_class_json, Container.b, Container) == fields.Nested(Simple.schema(), many=True)


    # Check optional fields
    a

# Generated at 2022-06-13 19:23:28.157204
# Unit test for method loads of class SchemaF
def test_SchemaF_loads(): # NOQA
    class Foo(typing.NamedTuple):
        i: int

    class FooSchema(SchemaF[Foo]):
        i = fields.Integer()

        @post_load
        def make_foo(self, data, **kwargs):
            return Foo(**data)

    foo = FooSchema().loads(b'{"i": 3}')
    assert foo.i == 3

    foos = FooSchema().loads(b'[{"i": 3}]')
    assert foos[0].i == 3


if sys.version_info < (3, 7):
    class SchemaF(Schema):
        """Lift Schema into a type constructor"""


# Generated at 2022-06-13 19:23:28.935803
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField is not None


# Generated at 2022-06-13 19:23:56.387345
# Unit test for constructor of class _IsoField
def test__IsoField():
    pass


# Generated at 2022-06-13 19:24:05.424592
# Unit test for constructor of class _IsoField
def test__IsoField():
    isoFieldObj = _IsoField()
    testObj1 = datetime.now()
    testObj2 = isoFieldObj._serialize(testObj1, None, None)
    assert(testObj2 == testObj1.isoformat())
    testObj3 = isoFieldObj._deserialize(testObj1.isoformat(), None, None)
    assert(testObj3 == testObj1)

test__IsoField()


# Generated at 2022-06-13 19:24:16.859517
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from dataclasses_json import config, dataclass_json

    class ValidateClass:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def __call__(self, value):
            return value

    assert isinstance(schema(ValidateClass, ValidateClass, False), dict)
    assert not isinstance(schema(ValidateClass, ValidateClass, False), bool)

    @dataclass_json
    @dataclass
    class TestMeetRequirements:
        unknown_filed: typing.Any
        t: typing.Tuple[str, int]
        a: datetime
        b: UUID
        c: Decimal
        d: typing.List[str]
       

# Generated at 2022-06-13 19:24:21.764764
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    import pytest
    from marshmallow import fields
    from src.dataclasses_json import DataClassJSONMixin

    @dataclass
    class Test(DataClassJSONMixin):
        text: str

    assert schema(Test, DataClassJSONMixin, False) == {
        "text": fields.String}

# Generated at 2022-06-13 19:24:24.670178
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    schema = SchemaF[int]()
    res: str = schema.dumps(1)
    assert res
    res = schema.dumps([1])
    assert res


# Generated at 2022-06-13 19:24:34.381977
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert SchemaF.loads('1', 1, '2', many=True, partial=True,
                         unknown='3', kwarg='4') == dict({'1': 1, '2': '3', 'kwarg': '4'})


if sys.version_info >= (3, 6):
    class _StaticSchema(Schema):
        """
        Create schema for dataclass.
        """

        @classmethod
        def load(cls, *args, **kwargs):
            return super().load(*args, **kwargs)  # type: ignore

        @classmethod
        def loads(cls, *args, **kwargs):
            return super().loads(*args, **kwargs)  # type: ignore

        @classmethod
        def dump(cls, *args, **kwargs):
            return super().dump

# Generated at 2022-06-13 19:24:41.875202
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass

    class TestMixin:
        pass

    @dataclass
    class Test(TestMixin):
        f1: str
        f2: typing.List[int]

    s = schema(Test, TestMixin, True)
    assert isinstance(s['f1'], fields.Str)
    assert isinstance(s['f2'], fields.List)
    assert isinstance(s['f2'].container, fields.Int)



# Generated at 2022-06-13 19:24:52.998311
# Unit test for constructor of class _IsoField
def test__IsoField():
    timestamp = _TimestampField()
    field = _IsoField()
    assert field._serialize(datetime.fromisoformat("2018-11-13T20:20:39+07:00"), "attr", "obj",
                            raw_data=1) == timestamp._serialize(datetime.fromisoformat("2018-11-13T20:20:39+07:00"),
                                                               "attr", "obj",
                                                               raw_data=1)


# Generated at 2022-06-13 19:25:01.967438
# Unit test for function schema
def test_schema():
    from dataclasses_json.api import add_decoder, add_encoder
    @add_decoder(UUID)
    def UUID_decode(s: str):
        return UUID(s)
    @add_encoder(UUID)
    def UUID_encode(u: UUID):
        return str(u)
    class Foo:
        class Bar:
            pass
        a = typing.Optional[int]
        b = typing.Optional[str]
        c = typing.List[Foo.Bar]
        d = typing.List[typing.List[str]]
        e = typing.Dict[str, Foo.Bar]
        f = typing.Optional[UUID]
    class MySchema(SchemaType):
        class Meta:
            unknown = "EXCLUDE"

# Generated at 2022-06-13 19:25:04.906531
# Unit test for constructor of class _IsoField
def test__IsoField():
    iso = '2000-01-01T00:00:00.000000'
    dt = datetime.fromisoformat(iso)
    assert dt == _IsoField()._deserialize(iso, 'year', {})


# Generated at 2022-06-13 19:26:04.152853
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    from marshmallow.exceptions import ValidationError
    class S(SchemaF[int]):
        g = fields.Integer()

    with pytest.raises(ValidationError):
        S().loads('{"g": ""}')

# Generated at 2022-06-13 19:26:10.969256
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # type: () -> None
    class A(object):
        def __init__(self, a: int, b: int, c: int) -> None:
            self.a = a
            self.b = b
            self.c = c

    class SchemaFImpl(SchemaF[A]):
        a = fields.Int()
        b = fields.Int()
        c = fields.Int()

    @post_load
    def make_a(self, data, **kwargs):
        return A(**data)

    data = dict(a=31, b=21565, c=0)

    schema = SchemaFImpl()
    result = schema.load(data)
    assert result == A(**data)

    result = schema.loads(repr(data))
    assert result == A(**data)



# Generated at 2022-06-13 19:26:18.265627
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
        b: str

    s = SchemaF.from_dataclass(A)
    a1 = s.load({'a': 1, 'b': 'x'})
    a2 = s.load([{'a': 1, 'b': 'x'}])
    a3 = s.load({'a': 1, 'b': 'x'}, many=True)
    a4 = s.load([{'a': 1, 'b': 'x'}], many=False)
    a1 = s.loads(b'{"a": 1, "b": "x"}')
    a2 = s.loads(b'[{"a": 1, "b": "x"}]')

# Generated at 2022-06-13 19:26:28.188127
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class A:
        pass


    class B(A):
        pass


    class C(A):
        pass


    class X(SchemaF[A]):
        class Meta:
            additional = ('a',)

        a = fields.Int(data_key='a', required=True)


    x = X(many=True)

    assert x.dump([A(), B(), C()], many=True) == [{'a': 0}, {'a': 0}, {'a': 0}]  # type: ignore
    assert x.dump(A()) == {'a': 0}  # type: ignore
    assert x.dump(B()) == {'a': 0}  # type: ignore
    assert x.dump(C()) == {'a': 0}  # type: ignore



# Generated at 2022-06-13 19:26:33.143549
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    
    @dataclass
    class DC:
        a: str

    assert len(schema(DC, DC, False)) == 1
    assert len(schema(DC, DC, False)[0]) == 1
    
    
    

# Generated at 2022-06-13 19:26:45.702002
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    @dataclass
    class MyClass:
        a: float
        b: str = "123"
        c: typing.Union[str, float] = "123"
    schema_ = schema(MyClass, dataclass_json, False)
    assert isinstance(schema_["a"], fields.Float)
    assert isinstance(schema_["b"], fields.Str)
    assert isinstance(schema_["c"], _UnionField)
    schema_ = schema(MyClass, dataclass_json, True)
    assert isinstance(schema_["a"], fields.Float)
    assert isinstance(schema_["b"], fields.Str)
    assert isinstance(schema_["c"], _UnionField)




# Generated at 2022-06-13 19:26:55.010930
# Unit test for function schema
def test_schema():
    try:
        from marshmallow import validate
    except ImportError:
        return

    from dataclasses_json.api import DataClassJsonMixin
    from dataclasses import dataclass

    validator = lambda n: n if n is not None else ""
    validator2 = lambda n: n if n is not None else ""

    @dataclass_json
    @dataclass
    class Example(DataClassJsonMixin):
        a: str
        b: str = validator
        c: str = field(default=validator2)
        d: str = None
        e: int = 12
        f: ValidatorStr = validate.OneOf(["a", "b", "c"])
        g: ValidatorInt = validate.OneOf([1, 2, 3])

# Generated at 2022-06-13 19:27:04.944519
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class IgnoreUnknown(Schema):
        __mapper_args__ = {'unknown': 'EXCLUDE'}

    @dataclass
    class Person:
        name: str
        age: int
        address: typing.Optional[str] = None
        foo: int = 100

    class PersonSchema(SchemaF[Person]):
        def __init__(self):
            super().__init__(cls=Person,
                             base_schema=IgnoreUnknown,
                             unknown=fields.EXCLUDE)

    p = Person(name='foo', age=42)
    s = PersonSchema().dump(p)
    assert s == {'name': 'foo', 'age': 42, 'foo': 100}



# Generated at 2022-06-13 19:27:09.623614
# Unit test for function build_schema
def test_build_schema():
    # To test for function build_schema
    class Mixin:
        ...
    
    @dataclass_json
    @dataclass
    class DataClass:
        dct: typing.Dict[str, int]
        tpl: typing.Tuple[int, int]
        lst: typing.List[int]
        string: str
        integer: int
        float_: float
        boolean: bool
        datetime_: datetime

    # Test for building schema
    DataClassSchema = build_schema(
        DataClass, Mixin, False, False)

# Generated at 2022-06-13 19:27:18.012890
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():  # type: () -> None
    @dataclass_json
    @dataclass
    class Message:
        data: str

    @dataclass_json
    @dataclass
    class MessageList:
        messages: typing.List[Message]

    class MessageListSchema(SchemaF[typing.Union[MessageList, Message]]):
        pass

    assert load(MessageListSchema, {'messages': [{'data': 'Foo'}]}) \
        == MessageList(messages=[Message(data='Foo')])
    assert loads(MessageListSchema, '{"messages": [{"data": "Foo"}]}') \
        == MessageList(messages=[Message(data='Foo')])

# Generated at 2022-06-13 19:29:34.081213
# Unit test for function schema
def test_schema():
    import marshmallow
    import typing
    import dataclasses
    class Meta(type):
        def __new__(cls, name, bases, attrs):
            attrs['__annotations__'] = {'a': 'a', 'b': 'b'}
            return type.__new__(cls, name, bases, attrs)
    class Mixin:
        pass
    class Dataclass(Mixin, metaclass=Meta):
        pass
    schema(Dataclass, Mixin, infer_missing=False)

# Generated at 2022-06-13 19:29:44.766363
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json(mm_field=fields.Str(load_from='name', dump_to='fullname'))
    class Person:
        name: str

    # pylint: disable=unused-variable
    Schema = build_schema(Person, None, False, False)
    assert Schema.__name__ == 'PersonSchema'
    assert hasattr(Schema.Meta, 'fields')
    assert hasattr(Schema.Meta, 'render_module')
    assert hasattr(Schema, 'make_person')
    assert hasattr(Schema, 'name')


# Generated at 2022-06-13 19:29:46.858742
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    # type: () -> None
    class ASchema(SchemaF[A]):
        pass

    class A():
        pass



# Generated at 2022-06-13 19:29:56.814475
# Unit test for function build_schema
def test_build_schema():
    class A:
        def __init__(self, a):
            self.a = a
    from dataclasses_json.core import DataclassJsonMixin
    from dataclasses import dataclass
    from dataclasses import field
    @dataclass_json
    @dataclass
    class Hello(DataclassJsonMixin):
        v: int = field(metadata={'dataclasses_json': {'mm_field': fields.Int()}})
        str: str = field(metadata={'dataclasses_json': {'mm_field': fields.Str()}})
    scheme = build_schema(Hello, DataclassJsonMixin, True, False)
    assert isinstance(scheme.Meta.fields, tuple)
    assert len(scheme.Meta.fields) == 2
    assert scheme

# Generated at 2022-06-13 19:30:03.001968
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    @dataclasses.dataclass()
    class User:
        name: str

    class UserSchema(SchemaF[User]):
        name = fields.Str()

    data = User(name='Danny')
    schema = UserSchema()
    result = schema.dumps(data)

    assert result == '{"name": "Danny"}'


# Generated at 2022-06-13 19:30:10.845440
# Unit test for function build_type
def test_build_type():
    import pytest
    class Mixin:
        pass
    class A(Mixin):
        def __init__(self, x):
            self.x = x
    class B(Mixin):
        def __init__(self, y):
            self.y = y
    class C(Mixin, metaclass=SchemaABCMeta):
        def __init__(self, z):
            self.z = z

    from typing import Optional, List
    from enum import Enum
    class E(Enum):
        A = 1
        B = 2

    @dataclass_json
    class D(Schema):
        x: Optional[A]
        y: B
        z: C
        e: E
        l: List[C]


# Generated at 2022-06-13 19:30:14.195175
# Unit test for function schema
def test_schema():
    class TestSchema(Schema):
        foo = fields.Int(missing=1)

    ts = TestSchema()
    assert ts.fields['foo'].missing == 1



# Generated at 2022-06-13 19:30:19.406696
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    dt = datetime.now()
    assert _TimestampField()._serialize(dt, None, None) == dt.timestamp()
    assert _TimestampField()._deserialize(dt.timestamp(), None, None) == dt
