

# Generated at 2022-06-13 19:20:51.797019
# Unit test for function build_type
def test_build_type():
    def test_inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
            type_ = type_.__supertype__
        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(
                    _is_supported_generic(field.type) and _is_collection(
                        field.type))
                return fields.Nested(type_.schema(), **options)

# Generated at 2022-06-13 19:21:05.461137
# Unit test for function build_schema
def test_build_schema():
    from marshmallow import Schema, fields
    from marshmallow.validate import Range

    # @dataclass_json
    @dataclass_json(letter_case=LetterCase.CAMEL)
    class MyDC:
        a: float
        b: int
        c: str

    # @dataclass_json
    @dataclass_json()
    class MyDC2:
        a: float
        b: int
        c: str

    assert MyDC.schema.__name__ == 'MyDCSchema'
    assert MyDC2.schema.__name__ == 'MyDC2Schema'
    assert isinstance(MyDC.schema, type)
    assert issubclass(MyDC.schema, Schema)
    assert isinstance(MyDC.schema._declared_fields, dict)


# Generated at 2022-06-13 19:21:18.360414
# Unit test for function build_type
def test_build_type():
    from typing_extensions import NewType
    from datetime import datetime
    from marshmallow import fields

    T = typing.TypeVar('T')
    class SomeClass(typing.Generic[T]):
        pass

    options = {}
    assert build_type(typing.Mapping, options, None, None, None) == fields.Mapping
    options = {}
    assert build_type(typing.MutableMapping, options, None, None, None) == fields.Mapping
    options = {}
    assert build_type(typing.List, options, None, None, None) == fields.List
    options = {}
    assert build_type(typing.Dict, options, None, None, None) == fields.Dict
    options = {}

# Generated at 2022-06-13 19:21:23.493879
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class DC:
        a: str
        b: int

    assert "str" in str(build_schema(DC, None, None, None))
    assert "int" in str(build_schema(DC, None, None, None))
    assert "Meta" in str(build_schema(DC, None, None, None))
    assert "make_dc" in str(build_schema(DC, None, None, None))
    assert "dumps" in str(build_schema(DC, None, None, None))
    assert "dump" in str(build_schema(DC, None, None, None))




# Generated at 2022-06-13 19:21:29.020452
# Unit test for constructor of class _IsoField
def test__IsoField():
    f = _IsoField()
    data = '2020-04-29T12:00:09.043082+02:00'
    res = f._serialize(datetime.fromisoformat(data), None, None)
    assert res == data


# Generated at 2022-06-13 19:21:35.976687
# Unit test for function build_schema
def test_build_schema():
    import dataclasses
    @dataclasses.dataclass
    class Person:
        name: str
        phone: str
    
    @dataclasses.dataclass
    class PersonSchema():
        name: str
        phone: str

        @post_load
        def make_instance(self, kvs, **kwargs):
            return Person(**kvs)
    assert PersonSchema


# Generated at 2022-06-13 19:21:44.007846
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField()
    assert field._serialize(None, "attr", "obj") is None
    assert field._serialize(datetime(2019, 4, 25, 10, 15, 0), "attr", "obj") == 1556227100.0

    assert field._deserialize(None, "attr", "data") is None
    assert field._deserialize(1556227100.0, "attr", "data") == datetime(
        2019, 4, 25, 10, 15, 0
    )


if sys.version_info[:2] < (3, 7):
    from dataclasses import _is_dataclass_instance_v16

    def _is_dataclass_instance(obj):
        return _is_dataclass_instance_v16(obj)

# Generated at 2022-06-13 19:21:50.491936
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, asdict

    @dataclass
    class Test:
        a: int
        b: str

        class Config:
            fields = {'b': 'b'}

    assert asdict(Test(a=1, b='1')) == {'a': 1, 'b': '1'}



# Generated at 2022-06-13 19:21:58.376393
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    import marshmallow as mm
    import typing as tp

    def f(schema: SchemaF[tp.List[int]], obj: tp.List[int]) -> tp.List[dict]:
        return schema.dump(obj)  # type: ignore

    def f_err(schema: SchemaF[tp.List[int]], obj: tp.List[int]) -> tp.List[int]:
        return schema.dump(obj)  # type: ignore

# Generated at 2022-06-13 19:22:06.269253
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    from typing import List, Dict
    from marshmallow import SchemaF
    from marshmallow.fields import _MISSING_ERROR_MESSAGE_KEY
    class UserSchema(SchemaF[Dict[str, str]]):
        pass
    UserSchema().load({})  # type: ignore
    UserSchema().load({}, many=True)  # type: ignore
    UserSchema().load({}, partial=True)  # type: ignore


# Generated at 2022-06-13 19:22:24.532978
# Unit test for function build_schema
def test_build_schema():
    from .types import DataclassJsonMixin
    from . import validate

    @dataclass
    class Foo(DataclassJsonMixin):
        b: str

    result = build_schema(Foo, DataclassJsonMixin, False, False)
    assert type(result.b).__name__ == "Str"


if sys.version_info >= (3, 7):
    def store_dc_info(cls):
        try:
            _store_dc_info(cls)
        except Exception as e:
            raise RuntimeError(
                f'Unable to store dataclass info for {cls.__name__}') from e



# Generated at 2022-06-13 19:22:30.299695
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from marshmallow import fields, Schema
    class Foo(typing.Generic[str], Schema):
        bar = fields.String()
    data = {'bar': 'baz'}
    f = Foo()
    assert f.dump(data) == data



# Generated at 2022-06-13 19:22:42.547536
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from typing import List

    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from marshmallow.validate import Length

    class TestSchema(SchemaF[List[int]]):
        """No init on purpose"""

        one = fields.Integer(validate=Length(max=255))
        two = fields.Integer(validate=Length(max=255))

    schema = TestSchema()

    result = schema.dumps([1, 2, 3])
    expected = '[{"one": 1, "two": 2, "__type": "List"}, ' \
               '{"one": 1, "two": 3, "__type": "List"}]'
    assert result == expected

    result = schema.dumps([1, 2, 3, 'A'])
    assert result == expected

    result = schema

# Generated at 2022-06-13 19:22:48.297265
# Unit test for method load of class SchemaF
def test_SchemaF_load():  # type: ignore
    from dataclasses import dataclass
    from marshmallow import Schema
    from typing import List

    @dataclass
    class Person:
        name: str
        age: int

    class PersonSchema(Schema):
        name = fields.Str()
        age = fields.Int()

    schema = PersonSchema()
    assert isinstance(schema.load([{'name': 'John'}], many=True),
                      List[Person])  # type: ignore



# Generated at 2022-06-13 19:22:53.240803
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    x = SchemaF[int]()
    assert isinstance(x.loads('[1,2,3]'), list)

    y = SchemaF[str]()
    assert isinstance(y.loads('foo'), str)


# Generated at 2022-06-13 19:23:03.141711
# Unit test for function build_type
def test_build_type():
    from .core import DataclassJsonMixin, dataclass_json
    from datetime import date
    from uuid import uuid4
    from typing import List, Optional


    class EmptyDc(DataclassJsonMixin):
        a: int

    class MixinDc(EmptyDc):
        b: str

    @dataclass_json
    class Dc(DataclassJsonMixin):
        a: int
        b: str
        c: List[str]
        d: Optional[str]
        e: date
        f: uuid4
        g: EmptyDc
        h: EmptyDc
        i: Dc
        j: EmptyDc
        k: MixinDc
        l: EmptyDc
        m: EmptyDc
        n: EmptyDc
        o

# Generated at 2022-06-13 19:23:06.829807
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    s = SchemaF()
    if sys.version_info >= (3, 7):
        assert s.dump([1, 2, 3]) == [1, 2, 3]
        assert s.dump(1) == 1
    assert s.dump([1, 2, 3], many=True) == [1, 2, 3]
    assert s.dump(1, many=False) == 1
test_SchemaF_dump()


# Generated at 2022-06-13 19:23:18.777861
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    import jsons
    class Foo:
        x: int
        y: str
    class Bar(SchemaF[Foo]):
        x = fields.Int()
        y = fields.Str()

    bar = Bar()
    assert bar.load(jsons.loads('{"x":5,"y":"5"}')) == Foo(x=5, y='5')
    assert bar.load([jsons.loads('{"x":5,"y":"5"}')]) == [Foo(x=5, y='5')]
    assert bar.load(jsons.loads('{"x":5,"y":"5"}'), many=True) == [Foo(x=5, y='5')]

# Generated at 2022-06-13 19:23:26.270028
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class ExampleSchema:
        foo: Optional[str]
        bar: Optional[str]

        dataclass_json_config = dataclass_json(_DecoderConfig(
            fields={'foo': mm_field(Str(required=True)),
                    'bar': mm_field(Str())}))

    _cls = build_schema(ExampleSchema,
                        None,
                        None,
                        None)
    assert _cls is not None
    schem = _cls()
    assert type(schem) is not Schema
    assert type(schem.fields['foo'].dump_to) is str
    assert type(schem.fields['bar'].dump_to) is str

# Generated at 2022-06-13 19:23:32.969096
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from dataclasses import dataclass

    @dataclass
    class In:
        int: int
        str: str
        date: datetime

    class InSchema(SchemaF[In]):
        int = fields.Int()
        str = fields.Str()
        date = _IsoField()

    dataclass_to_seralized = In(10, "test", datetime.now())
    list_of_dataclass_to_seralized = [In(10, "test", datetime.now())]

    assert InSchema().dump(dataclass_to_seralized, many=False) == {
        'int': 10,
        'str': 'test',
        'date': dataclass_to_seralized.date.isoformat()
    }

# Generated at 2022-06-13 19:24:13.121445
# Unit test for constructor of class _IsoField
def test__IsoField():
    class TestSchema(Schema):
        valid1 = _IsoField()
        valid2 = _IsoField(required=False)
        invalid1 = _IsoField(required=True)
        invalid2 = _IsoField(required=True)

    valid_data = {'valid1': '2020-01-01T12:00:00',
                  'valid2': None}
    valid_obj = TestSchema().load(valid_data)
    assert valid_obj == {'valid1': datetime(2020, 1, 1, 12, 0, 0),
                         'valid2': None}

    invalid_data = {'invalid1': None,
                    'invalid2': None}

# Generated at 2022-06-13 19:24:15.732204
# Unit test for function build_type
def test_build_type():
    assert build_type(str, {}, None, None, None)(str, {}) == TYPES[str]



# Generated at 2022-06-13 19:24:26.006516
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass

    from marshmallow import fields

    mm_field_options = {"load_from": "test_key"}
    mm_field_mixin = None

    @dataclass
    class TestClass:
        an_int_field: int
        another_int_field: int = 9
        an_optional_int_field: typing.Optional[int] = None
        a_uuid_field: UUID
        a_str_field: str
        a_bool_field: bool
        a_float_field: float
        an_optional_str_field: typing.Optional[str] = None
        a_list_field: typing.List
        a_tuple_field: typing.Tuple
        a_dict_field: typing.Mapping

# Generated at 2022-06-13 19:24:34.123478
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    class RestrictiveType(str):
        pass

    class RestrictiveSchema(SchemaF[RestrictiveType]):
        pass

    RestrictiveType('bla')  # type check
    RestrictiveSchema().load(RestrictiveType('bla'))  # type check

# Generated at 2022-06-13 19:24:45.198917
# Unit test for function build_schema
def test_build_schema():

    import dataclasses_json
    import marshmallow_dataclass
    import marshmallow as mm
    import typing

    class MyClass(object):
        pass

    @dataclasses_json.dataclass_json
    @dataclasses.dataclass
    class MyDataClass(object):
        a: int
        b: str

    @dataclasses.dataclass
    class MyDataClass2(object):
        c: int
        d: MyDataClass

    @dataclasses.dataclass
    class MyDataClass3(object):
        e: typing.Optional[str]
        f: typing.Optional[int]

    @dataclasses.dataclass
    class MyDataClass4(MyClass, MyDataClass):
        g: int
        h: str


# Generated at 2022-06-13 19:24:55.435669
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class ExampleSchema(SchemaF[A]):
        value = fields.Int()

        @post_load
        def make_object(self, data, **kwargs) -> A:
            # this method is intended to create the expected
            # type A with all data of the data dict
            pass

    schema = ExampleSchema()
    data = {"value": 1}
    # mm has the wrong return type annotation (dict) so we can ignore the mypy error
    # for the return type overlap
    x: str = schema.dumps(data)
    # mm has the wrong return type annotation (dict) so we can ignore the mypy error
    # for the return type overlap
    x: str = schema.dumps(data, many=False)
    # mm has the wrong return type annotation (dict) so we can ignore the mypy error
   

# Generated at 2022-06-13 19:24:57.087066
# Unit test for function schema
def test_schema():
    from .mm_schema_test import test_schema as module_test
    module_test()

# Generated at 2022-06-13 19:25:04.559840
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class Person:
        name: str
        age: int

    @dataclass_json
    @dataclass
    class Person2:
        name: str
        age: int

    @dataclass_json
    @dataclass
    class Person3:
        name: str
        age: int

    @dataclass_json
    @dataclass
    class Person4:
        name: str
        age: int

    class Person5:
        pass

    @dataclass_json
    @dataclass
    class Person6:
        name: str
        age: Union[str, Person, Person5]


# Generated at 2022-06-13 19:25:11.479343
# Unit test for function schema
def test_schema():
    @dataclass_json
    @dataclass
    class T:
        a: int = field(metadata=dataclasses_json.config(mm_field=fields.String))
        b: int = field(metadata=dataclasses_json.config('b'))
        c: Enum = field(metadata=dataclasses_json.config(mm_field=fields.String))
        d: bool = field(metadata=dataclasses_json.config(mm_field=fields.Bool))
        e: Any = field(metadata=dataclasses_json.config(mm_field=fields.Raw))
        f: typing.Mapping = field(metadata=dataclasses_json.config())
        g: typing.MutableMapping = field(metadata=dataclasses_json.config())

# Generated at 2022-06-13 19:25:19.145139
# Unit test for function schema
def test_schema():
  import unittest
  from dataclasses import dataclass, field

  from dataclasses_json import config, DataClassJsonMixin, dataclass_json

  from marshmallow import ValidationError

  from typing import Optional, Union, Dict, List, Any


  @dataclass_json
  @dataclass
  class Simple(DataClassJsonMixin):
      name: str
      age: int
      is_employed: bool
      created_at: datetime
      nested_test: Optional['Simple'] = field(default=None)


  @dataclass_json(mm_field=fields.Field())
  @dataclass
  class Special:
      name: str
      age: int
      is_employed: bool
      created_at: datetime
      nested_test: Optional[Special] = field

# Generated at 2022-06-13 19:26:12.567513
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass

    @dataclass
    class A:
        a: int
    s = SchemaF[A]()
    assert s.dumps([A(a=1), A(a=2)], many=True) == \
    '[{"a": 1}, {"a": 2}]'

    assert s.dumps(A(a=1), many=False) == '{"a": 1}'

    assert s.dumps(A(a=1), many=None) == '{"a": 1}'

    assert s.dumps(A(a=1)) == '{"a": 1}'



# Generated at 2022-06-13 19:26:14.061889
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    _ = SchemaF[int].loads('')



# Generated at 2022-06-13 19:26:15.088243
# Unit test for constructor of class _IsoField
def test__IsoField():
    some_field = _IsoField()
    assert some_field is not None



# Generated at 2022-06-13 19:26:16.792155
# Unit test for function build_type
def test_build_type():
    assert build_type(int, {}, None, None, None) == fields.Int



# Generated at 2022-06-13 19:26:27.342305
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass
    from marshmallow import Schema

    @dataclass
    class User:
        username: str
        email: str

    class UserSchema(Schema):
        username = fields.Str()
        email = fields.Email()

    # dump the data class
    schema = SchemaF[User](exclude=['email'], strict=True)
    result = schema.dump(User('foo', 'bar'))
    assert user_schema.dump(User('foo', 'bar')) == result == {'username': 'foo'}

    # dump a list of data classes
    schema = SchemaF[User](exclude=['email'], many=True, strict=True)
    result = schema.dump([User('foo', 'bar'), User('baz', 'qux')])

# Generated at 2022-06-13 19:26:31.332568
# Unit test for function schema
def test_schema():
    
    @dataclass
    class Test:
        name: str
        surname: str
    
    
    schema(Test, None, None)



# Generated at 2022-06-13 19:26:40.717276
# Unit test for function build_type
def test_build_type():
    assert build_type(1, {}, 1, 1, 1)(1, {}) == fields.Int()
    assert build_type(UUID, {}, 1, 1, 1)(UUID, {}) == fields.UUID()
    assert build_type(CatchAllVar, {}, 1, 1, 1)(CatchAllVar, {}) == fields.Dict()
    assert build_type(typing.List, {}, 1, 1, 1)(typing.List, {}) == fields.List()
    assert build_type(typing.Dict, {}, 1, 1, 1)(typing.Dict, {}) == fields.Dict()
    assert build_type(typing.Mapping, {}, 1, 1, 1)(typing.Mapping, {}) == fields.Mapping()

# Generated at 2022-06-13 19:26:48.907472
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    obj: typing.List[int] = SchemaF[int]().loads('[1, 2]')
    assert obj[0] == 1
    assert obj[1] == 2
    obj2: typing.List[int] = SchemaF[int](many=True).loads('[1, 2]')
    assert obj2[0] == 1
    assert obj2[1] == 2
    obj3: typing.List[int] = SchemaF[int](many=True).loads(b'[1, 2]')
    assert obj3[0] == 1
    assert obj3[1] == 2

    obj4: int = SchemaF[int]().loads('1')
    assert obj4 == 1
    obj5: int = SchemaF[int](many=False).loads('1')
    assert obj5 == 1


# Generated at 2022-06-13 19:26:52.615787
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    @dataclass_json
    @dataclass
    class A:
        a: int
    a = A(a = 1)
    res = SchemaF[A].dumps(a)
    assert res == str({'a': 1})



# Generated at 2022-06-13 19:26:59.326499
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    class SchemaF(Schema, typing.Generic[A]):
        @typing.overload # type: ignore
        def loads(self, json_data: JsonData, many: bool = True, partial: bool = None, unknown: str = None, **kwargs) -> typing.List[A]:
            pass

        @typing.overload
        def loads(self, json_data: JsonData, many: None = None, partial: bool = None, unknown: str = None, **kwargs) -> A:
            pass

        def loads(self, json_data: JsonData, many: bool = None, partial: bool = None, unknown: str = None, **kwargs) -> TOneOrMulti:
            pass

    class MyClass(typing.NamedTuple):
        foo: int
        bar: str

    s