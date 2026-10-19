

# Generated at 2022-06-13 19:20:44.155450
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(datetime.now())


# Generated at 2022-06-13 19:20:51.435586
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json.mm import M
    from marshmallow.fields import String, Integer
    @dataclass
    class Base:
        name: str

    @dataclass
    class Super(Base):
        id: int

    assert(schema(Super, M, False) == {
        'name': String(missing='__missing__'),
        'id': Integer(missing='__missing__'),
    })



# Generated at 2022-06-13 19:21:01.546963
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    for many in [None, True, False]:
        for partial in [None, True, False]:
            for unknown in [None, 'raise', 'EXCLUDE']:
                assert isinstance(SchemaF.loads([], many, partial=partial, unknown=unknown), list)
                assert isinstance(SchemaF.loads(b'', many, partial=partial, unknown=unknown), int)
    assert isinstance(SchemaF.loads([], many=True, partial=True, unknown='raise'), list)
    assert isinstance(SchemaF.loads(b'', many=True, partial=True, unknown='raise'), int)
    assert isinstance(SchemaF.loads(b'', many=True, partial=True, unknown='EXCLUDE'), int)

# Generated at 2022-06-13 19:21:06.570843
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    assert field._serialize(None, '', None) == None
    assert field._serialize(datetime.now(), '', None) != None
    assert field._deserialize(None, '', None) == None
    assert field._deserialize(12, '', None) != None
    assert field.required
    field.required = False
    assert not field.required


# Generated at 2022-06-13 19:21:11.854322
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class myclass:
        name: str
        surname: Optional[str] = None

    j = schema(myclass, 'test', False)
    if isinstance(j, dict):
        return True
    else:
        return False

# Generated at 2022-06-13 19:21:12.612416
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    pass

# Generated at 2022-06-13 19:21:17.690864
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    def test_loads_dict():
        sf = SchemaF[int]
        assert isinstance(sf.loads(b"1"),int)

    def test_loads_list():
        sf = SchemaF[int]
        assert isinstance(sf.loads(b"1",many=True),list)

    test_loads_dict()
    test_loads_list()


# Generated at 2022-06-13 19:21:27.191332
# Unit test for function schema
def test_schema():
    class Base:
        name: str
        @property
        def test(self):
            return self.name.upper()
        class Config:
            arbitrary_types_allowed = True

    class Mixin:
        id: str
        def foo(self):
            pass

    class A(Base, Mixin):
        max_len: int

    class B(A):
        pass

    m = schema(A, Mixin, False)
    m2 = schema(B, Mixin, False)
    assert m['name'] == fields.Str(required=True)
    assert m['id'] == fields.String(required=True)
    assert m['max_len'] == fields.Int(required=True)
    assert m2['name'] == fields.Str(required=True)

# Generated at 2022-06-13 19:21:39.366778
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    json_str = '{"a":1}'
    assert SchemaF[int].loads(json_str) == 1
    assert SchemaF[int].loads(json_str, many=False) == 1
    assert SchemaF[int].loads(json_str, many=True) == [1]
    assert SchemaF[int].load(json_str) == 1
    assert SchemaF[int].load(json_str, many=False) == 1
    assert SchemaF[int].load(json_str, many=True) == [1]
    assert SchemaF[int].load([json_str]) == [1]
    assert SchemaF[int].load([json_str], many=True) == [1]
    assert SchemaF[int].load([json_str], many=False) == 1
   

# Generated at 2022-06-13 19:21:39.909466
# Unit test for function schema
def test_schema():
    pass


# Generated at 2022-06-13 19:21:57.792222
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    timestamp_field = _TimestampField()
    assert timestamp_field._serialize(datetime.now(), None, None, None) is not None
    try:
        timestamp_field._serialize(None, None, None, None)
    except ValidationError:
        pass
    else:
        pytest.fail("_serialize should raise ValidationError")
    assert timestamp_field._deserialize(datetime.now().timestamp(), None, None, None) is not None
    try:
        timestamp_field._deserialize(None, None, None, None)
    except ValidationError:
        pass
    else:
        pytest.fail("_deserialize should raise ValidationError")


# Generated at 2022-06-13 19:22:06.150090
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    # Test for the overloads of method loads
    s = SchemaF.__new__(SchemaF)
    s.loads(json_data=b'{"foo": "bar"}')
    s.loads(json_data=b'[{"foo": "bar"}]', many=True)
    s.loads(json_data='{"foo": "bar"}')
    s.loads(json_data='[{"foo": "bar"}]', many=True)



# Generated at 2022-06-13 19:22:08.768724
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    pass

# Generated at 2022-06-13 19:22:14.374125
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from unittest.mock import Mock, patch
    from typing import List

    mocked_method = Mock(return_value={'a': 1, 'b': 2})
    mocked_cls = Mock(return_value=mocked_method)
    arg = [{'a': 1}, {'b': 2}]

    with patch('marshmallow.Schema.dumps', mocked_cls):
        SchemaF.dumps(arg)

    mocked_cls.assert_called_with(arg, many=True)



# Generated at 2022-06-13 19:22:18.005255
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    value = datetime.now()
    serialized = field._serialize(value, None, None)
    assert isinstance(serialized, float)
    deserialized = field._deserialize(serialized)
    assert isinstance(deserialized, datetime)


# Generated at 2022-06-13 19:22:25.387733
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    schemaF = SchemaF()
    data = '{"a":[]}'
    assert schemaF.loads(data) == {'a': []}
    assert schemaF.loads(data, many=True) == [{'a': []}]
    assert schemaF.loads(data, many=False) == {'a': []}



# Generated at 2022-06-13 19:22:39.210964
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    def test_1(is_list: bool):
        sf = SchemaF[Adt]()
        data = sf.dump([Adt((1, 2))] if is_list else Adt((1, 2)))
        assert isinstance(data, list) if is_list else isinstance(data, dict)
        assert data['a'] == (1, 2)

    def test_2(is_list: bool):
        sf = SchemaF[typing.Tuple[typing.Tuple[int, ...], ...]]()
        data = sf.dump([((1, 2), (1, 2))] if is_list else ((1, 2), (1, 2)))
        assert isinstance(data, list) if is_list else isinstance(data, dict)

# Generated at 2022-06-13 19:22:48.176025
# Unit test for constructor of class _IsoField
def test__IsoField():
    field = _IsoField(required=False)
    assert field._deserialize('2019-05-07T20:27:22.031350') == datetime(2019, 5, 7, 20, 27, 22, 31350)
    assert field._serialize(datetime(2019, 5, 7, 20, 27, 22, 31350)) == '2019-05-07T20:27:22.031350'
    assert field._serialize(None) == None
    # raises error when the value is required and the value is None
    passes = False
    try:
        field._serialize(None) == None
    except ValidationError:
        passes = True
    assert passes == True


# Generated at 2022-06-13 19:22:49.859217
# Unit test for function schema
def test_schema():
    assert schema(1, 2, 3) == {}

# Generated at 2022-06-13 19:22:58.793306
# Unit test for function build_schema
def test_build_schema():
    from mixins import FromDictMixin
    from typing import List, Optional

    class TestDataSchema(Schema):
        something = fields.Int(load_only=True)
        something_else = fields.Int()
        __strict__ = False

    @dataclass_json(mm_schema=TestDataSchema)
    @dataclass
    class TestDict(FromDictMixin):
        a: str
        b: int = 2
        c: List[int] = field(default_factory=list)
        d: Optional[str] = None

    TestDataSchema(many=False)



# Generated at 2022-06-13 19:23:28.334270
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        d = _TimestampField()
        assert d._serialize(datetime(1970, 1, 1, 8), None, None) == 0
        d.required = False
        assert d._serialize(None, None, None) is None
        d.required = True
        assert d._serialize(None, None, None) is not None # exception

# Generated at 2022-06-13 19:23:32.204448
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass
    from typing import List, Dict

    @dataclass
    class Item:
        a: str
        b: int

    @dataclass
    class Item2:
        a: str

    @dataclass
    class Item3:
        a: str
        b: int
        c: Item
        d: List[Item]
        e: Dict[str, str]

    class ItemSchema(SchemaF[Item]):
        a = fields.Str()
        b = fields.Int()

    class Item2Schema(SchemaF[Item2]):
        a = fields.Str()

    class Item3Schema(SchemaF[Item3]):
        a = fields.Str()
        b = fields.Int()

# Generated at 2022-06-13 19:23:35.698857
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass_json
    @dataclass
    class Foo:
        a: str
        b: int = 0

    assert isinstance(SchemaF[Foo].load([{'a': 'a', 'b': 1}],
                                        many=True), typing.List[Foo])



# Generated at 2022-06-13 19:23:45.529922
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    def _have_method(schemas, cls):
        for schema in schemas:
            if not isinstance(schema, cls):
                return False
        return True

    if not _have_method([SchemaF[int]], SchemaF):
        raise Exception()

    if not _have_method([SchemaF[typing.List[int]]], SchemaF):
        raise Exception()

    if not _have_method([SchemaF[typing.List[int]]], SchemaF):
        raise Exception()

    if not _have_method([SchemaF[list], SchemaF[list], SchemaF[list]], SchemaF):
        raise Exception()


# Generated at 2022-06-13 19:23:50.712808
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from typing import List
    from dataclasses import dataclass

    @dataclass
    class A:
        b: int = 1

    @dataclass
    class B:
        a: str = 'test'
        c: List[A] = field(default_factory=lambda: [A()])

    # Test basic usage
    assert SchemaF[A]().dump(A()) == {'b': 1}

    # Test mapping
    assert SchemaF[B]().dump(B()) == {'a': 'test', 'c': [{'b': 1}]}

    # Test list

# Generated at 2022-06-13 19:23:53.623467
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    @dataclass
    class Test:
        a: int = field(metadata={'required': True})
    schema = SchemaF[Test]()
    result = schema.loads(b'{"a": 100}')


# Generated at 2022-06-13 19:24:05.256569
# Unit test for function schema
def test_schema():
    import sqlalchemy
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, DateTime, Boolean
    from dataclasses import dataclass, fields
    from dataclasses_json import DataClassJsonMixin, dataclass_json
    from typing import List, Optional, Dict, Union

    Base = declarative_base()

    @dataclass
    class User(DataClassJsonMixin, Base):
        __tablename__ = 'users'
        id: int = None
        username: str = None
        email: str = None
        password: str = None
        created_at: datetime = None
        is_active: Boolean = None
        bio: Optional[str] = None
        followers: List[int] = None
        friends: List

# Generated at 2022-06-13 19:24:16.656437
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import marshmallow as mm

    class A:
        a: int

    class A2(A):
        b: int

    class A3(A):
        c: int

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class B:
        a: typing.Union[A, A2, A3]

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class C:
        b: typing.List[B]

    assert SchemaF[B].dump(B(A(1)), many=False) == {'a': {'a': 1, 'b': None, 'c': None, '__type': 'A'}}

# Generated at 2022-06-13 19:24:26.772282
# Unit test for function schema
def test_schema():
    from typing import Optional, Union
    from dataclasses import dataclass, field
    from marshmallow.exceptions import ValidationError
    from marshmallow import fields as F
    from marshmallow_enum import EnumField as EE  # type: ignore
    from enum import Enum

    class A(Enum):
        a = 'a'
        b = 'b'

    @dataclass
    class B:
        x: int

    @dataclass
    class C:
        y: int = field(metadata={'dataclasses_json':{'mm_field':F.Int()}})

    @dataclass
    class D:
        y: int = field(metadata={'dataclasses_json':{'letter_case':str.upper}})

    @dataclass
    class E:
        z: int



# Generated at 2022-06-13 19:24:36.622533
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass
    class Human:
        name: str

    @dataclass_json(mm_field=fields.List)
    @dataclass
    class Employee:
        name: str
        friends: typing.List[Human]


# Generated at 2022-06-13 19:25:34.251065
# Unit test for function build_type
def test_build_type():
    # when type is dataclass
    class Part(Schema):
        id = fields.Int()
        name = fields.String()

    class Product(Schema):
        part = fields.Nested(Part)

    # when type is not dataclass
    class Product(Schema):
        part = fields.Field()

    # when type is optional
    class Product(Schema):
        part = fields.Field(allow_none=True)

    # when type is list of dataclass
    class Part(Schema):
        id = fields.Int()
        name = fields.String()

    class Product(Schema):
        part = fields.List(fields.Nested(Part))

    # when type is list of not dataclass
    class Product(Schema):
        part = fields.List(fields.Field())

    #

# Generated at 2022-06-13 19:25:40.050865
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type: () -> None
    class NotAnnotated(SchemaF):
        pass
    n = NotAnnotated()
    # type: typing.List[int]
    arg = [1, 2, 3]
    res = n.dumps(arg)
    assert isinstance(res, str)
    assert res == '[1, 2, 3]'
    # type: int
    arg = 1
    res = n.dumps(arg)
    assert isinstance(res, str)
    assert res == '1'
    class NotAnnotated2(SchemaF):
        pass
    n2 = NotAnnotated2()
    # type: typing.Tuple[int]
    arg = (1,)
    res = n2.dumps(arg)
    assert isinstance(res, str)

# Generated at 2022-06-13 19:25:49.762917
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field
    from typing import Type
    from marshmallow import Schema

    def create_schema(cls, mixin, infer_missing, test_type):
        # type: (Type, Type, bool, type) -> Schema
        not_implemented_kwargs = ['many', 'only', 'exclude', 'context', 'load_only', 'dump_only', 'partial']
        args = {k: k for k in not_implemented_kwargs}
        return Schema(**args)

    @dataclass
    class Foo:
        bar: str
        baz: str

    @dataclass
    class Bar:
        foo: Foo
        data: typing.Any
        data2: typing.Any


# Generated at 2022-06-13 19:25:53.192038
# Unit test for constructor of class _TimestampField
def test__TimestampField():  # noqa
    import pytest
    from datetime import datetime, timezone
    field = _TimestampField()
    assert field._serialize(datetime.now(timezone.utc)) is not None


# Generated at 2022-06-13 19:25:56.164674
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    @dataclass
    class A:
        a: int

    a = A(1)
    s = SchemaF[A].from_dataclass(A)
    assert isinstance(s.dump(a), dict)


# Generated at 2022-06-13 19:26:05.548121
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class SchemaF(Schema):
        a: str
    assert SchemaF().loads({"a": "a"}).a == "a"
    assert SchemaF().loads({"a": "a"}, many=None).a == "a"
    assert SchemaF().loads({"a": "a"}, many=False).a == "a"
    assert SchemaF().loads({"a": "a"}, many=False).a == "a"
    assert SchemaF().loads({"a": "a"}, many=False).a == "a"
    assert SchemaF(many=False).loads({"a": "a"}).a == "a"
    assert SchemaF(many=False).loads({"a": "a"}, many=False).a == "a"

# Generated at 2022-06-13 19:26:13.993700
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass


    @dataclass
    class Base:
        a: str = 'default'


    @dataclass
    class Intermediate(Base):
        b: int = 1


    @dataclass
    class Nested(Intermediate):
        c: str


    @dataclass
    class Top(Nested):
        d: str


    s = build_schema(Top, DataclassJsonMixin, False, False)
    assert isinstance(s, type)
    assert issubclass(s, SchemaType)
    assert 'a' in s._declared_fields
    assert 'd' in s._declared_fields
    assert s._declared_fields['d'].required
    assert not s._declared_fields['a'].required

# Generated at 2022-06-13 19:26:22.323736
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    @dataclass
    class A:
        pass
    @dataclass
    class B(A):
        pass
    @dataclass
    class C(B):
        pass

    assert len(build_schema(A, A, infer_missing=False, partial=False)) == 1
    assert len(build_schema(B, B, infer_missing=False, partial=False)) == 2
    assert len(build_schema(C, C, infer_missing=False, partial=False)) == 3


# Generated at 2022-06-13 19:26:27.177969
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type: (...) -> None
    """SchemaF dumps method should have the right annotations."""
    s: Schema

# Generated at 2022-06-13 19:26:28.378066
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()
