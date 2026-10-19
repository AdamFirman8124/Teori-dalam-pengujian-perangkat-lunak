

# Generated at 2022-06-13 19:20:42.359920
# Unit test for function schema
def test_schema():
    from typing import Optional, MutableMapping, Union, List, Any
    from marshmallow import fields, Schema
    from marshmallow_dataclass import dataclass
    from marshmallow_dataclass.schema import build_type

    class MyCatchAllVarClass:
        def __init__(self, my_dict):
            self.my_dict = my_dict

        def get(self):
            return self.my_dict

    class MyCatchAllVar(CatchAllVar):
        __supertype__ = MutableMapping[str, str]
        __newtype__ = MyCatchAllVarClass

    class MyMixin:
        pass

    @dataclass
    class Item:
        name: str
        value: int

    @dataclass
    class MyClass(MyMixin):
        name: str

# Generated at 2022-06-13 19:20:53.359753
# Unit test for function build_type
def test_build_type():
    class Cls:
        class Schema(Schema):
            name = fields.Str()
            value = fields.Float()

        @classmethod
        def schema(cls):
            return Cls.Schema

    class EnumCls(Enum):
        ONE = 1
        TWO = 2

    class GenericCls(str):
        pass

    class GenericClsType(typing.Generic[GenericCls]):
        pass

    class UnionCls(typing.Union):
        def __init__(self, a: typing.List[Cls], b: GenericClsType[GenericCls]):
            pass

    @dataclass
    class Mixin:
        pass

    @dataclass_json
    class DcCls(Mixin):
        name: str
        cls: Cls
        enum

# Generated at 2022-06-13 19:21:02.660027
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import marshmallow.exceptions
    import marshmallow.fields
    import typing
    def dump_func(arg: SchemaF[int], arg_1: int, arg_2: int) -> int:
        return arg.dumps(arg_1)
    def dump_func_1(arg: SchemaF[int], arg_1: int, arg_2: int) -> typing.List[int]:
        return arg.dumps(arg_1)
    def dump_func_2(arg: SchemaF[int], arg_1: typing.List[int], arg_2: int) -> typing.List[int]:
        return arg.dumps(arg_1)
    class A(marshmallow.fields.Integer):
        pass
    dump_func(SchemaF[int](A()), 1, 2)
    dump_

# Generated at 2022-06-13 19:21:08.310066
# Unit test for constructor of class _IsoField
def test__IsoField():
    assert _IsoField()._serialize(datetime.fromisoformat("2020-09-21T20:47:26.971511"), None, None,) == "2020-09-21T20:47:26.971511"
    assert _IsoField()._deserialize("2020-09-21T20:47:26.971511", None, None) == datetime.fromisoformat("2020-09-21T20:47:26.971511")


# Generated at 2022-06-13 19:21:21.895447
# Unit test for function build_schema
def test_build_schema():
    a,b,c,d,e,f,g, h, i, j, k, l, m, n, o, p, q, r, s, t= 1,2,3,4,5,6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    @dataclass
    class A:
        b: int

    @dataclass
    class B:
        a: A
        c: int

    @dataclass
    class C:
        a: typing.List[int]
        b: typing.Optional[int]
        c: typing.Optional[int] = None

    @dataclass
    class D:
        a: typing.List[int]
        b: typing.Optional[int]

# Generated at 2022-06-13 19:21:23.053909
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    assert True

# Generated at 2022-06-13 19:21:36.617368
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    f = SchemaF()
    class A():
        def dumps(self): return self.__class__.__name__

    a = A()
    dumps_res = f.dumps(a)
    assert f.loads(dumps_res) == a
    assert f.loads(dumps_res, unknown='raise') == a
    assert f.loads(dumps_res, unknown='ignore') == a
    assert f.loads(dumps_res, unknown='EXCLUDE') == a
    assert f.loads(dumps_res, many=True) == [a]
    assert f.loads(dumps_res, many=True, unknown='raise') == [a]
    assert f.loads(dumps_res, many=True, unknown='ignore') == [a]

# Generated at 2022-06-13 19:21:42.158344
# Unit test for function build_schema
def test_build_schema():
    @dataclass_json
    @dataclass
    class test_case:
        a: int
        b: str
    test_case_mixin = build_schema(test_case, None, True, False)
    test_case_instance = test_case_mixin()
    assert isinstance(test_case_instance, Schema) is True
    assert isinstance(test_case_instance.opts.fields, tuple) is True
    assert isinstance(test_case_instance.opts.fields[0], str) is True
    assert test_case_instance.opts.fields[0] == 'a'
    assert test_case_instance.opts.fields[1] == 'b'
    assert isinstance(test_case_instance.opts.ordered, bool) is True

# Generated at 2022-06-13 19:21:47.255285
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Person:
        first_name: str = field(repr=False)
        last_name: str
        age: int = 27
        test: Optional[List[int]] = None
        no_serialization_test: str = field(metadata={'dataclasses_json': {'exclude': True}})

    @dataclass
    class AllTypes:
        a: str = field(repr=False)
        b: int
        c: float = 1.0
        d: bool = True
        e: Optional[str] = None
        f: datetime
        g: dict
        h: typing.List[str]
        i: typing.Dict[str, int]
        j: typing.List[Person]
        k: Person
        l: typing.Callable[[str], str]

# Generated at 2022-06-13 19:21:58.549034
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    # type: () -> None
    class F(SchemaF):
        pass

    class L(SchemaF):
        pass

    # test wrong inheritance
    with pytest.raises(NotImplementedError):
        F(strict=True).dump(["a", "b"], many=True)
    with pytest.raises(NotImplementedError):
        F(strict=True).dump("a", many=False)
    with pytest.raises(NotImplementedError):
        L(strict=True).dump(["a", "b"])
    with pytest.raises(NotImplementedError):
        L(strict=True).dump("a")

    class A(SchemaF):
        x = fields.List(fields.Int())
        y = fields.Int()


# Generated at 2022-06-13 19:22:26.202539
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class DataClass:
        id: int = 4
        age: float = 3.2
        name: str = "Kevin"
        flags: typing.List[int] = field(default_factory=lambda: [1, 2, 3])

    mixin = dataclass_json.DataClassJsonMixin
    infer_missing = True
    partial = True

    schema = build_schema(DataClass, mixin, infer_missing, partial)

    assert type(schema.Meta) == type('Meta', (), {
        'fields': ('id', 'age', 'name', 'flags'),
    })
    assert schema.id is not None
    assert schema.age is not None
    assert schema.name is not None
    assert schema.flags is not None

# Generated at 2022-06-13 19:22:36.285502
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json
    from typing import Optional, Union, Mapping

    @dataclass_json
    @dataclass
    class NoMixin:
        str: str

    @dataclass_json
    @dataclass
    class Mixin:
        str: str

    @dataclass_json
    @dataclass
    class Parent:
        nm: NoMixin
        m: Mixin

        @property
        def prop(self):
            return 1

    assert(build_type(NoMixin, {}, Mixin, dc_fields(Parent)[0], Parent).__class__ == fields.Field)

# Generated at 2022-06-13 19:22:47.095481
# Unit test for function build_type
def test_build_type():
    import dataclasses
    from typing import Optional

    _pass = True

    @dataclasses.dataclass
    class A():
        a: Optional[int]

    @dataclasses.dataclass
    class B(A):
        b: Optional[int]

    @dataclasses.dataclass
    class C(B):
        c: Optional[int]

    class D():
        pass

    @dataclasses.dataclass
    class E(D):
        e: Optional[int]

    @dataclasses.dataclass
    class F():
        f: Optional[int]

    @dataclasses.dataclass
    class G():
        field: Optional[A]
        field8: Optional[B]
        field9: Optional[C]
        field10: Optional[D]
        field

# Generated at 2022-06-13 19:22:47.992751
# Unit test for constructor of class _IsoField
def test__IsoField():
    pass



# Generated at 2022-06-13 19:22:51.648846
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    schema = SchemaF[TEncoded]()
    result = schema.loads(json_data={'hello': 'world'})
    assert result == {'hello': 'world'}

# Generated at 2022-06-13 19:23:02.010782
# Unit test for function build_schema
def test_build_schema():
    import datetime
    import enum
    import typing
    import uuid

    from dataclasses import dataclass, field
    from typing import Union

    from marshmallow import Schema, fields
    from dataclasses import dataclass, field
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class SubClass(DataClassJsonMixin):
        sub_field: str = "SubClass"

    @dataclass
    class MyClass(DataClassJsonMixin):
        a: str
        int_f: int = field(metadata={'dataclasses_json': {'mm_field': fields.Int(required=False)}})
        sub_class: SubClass = SubClass()
        # TODO make mixin DatetimeField to test it
        datetime_f: datetime.dat

# Generated at 2022-06-13 19:23:12.094025
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class Common:
        name: str

    @dataclass
    class A(Common):
        value: str

    @dataclass
    class B(Common):
        value: int

    @dataclass
    class T(A, B):
        name: Optional[str]

    t = T('joe', 'hi', 4)
    t_s = T.schema().dump(t)

    assert t_s['name'] == 'joe'
    assert t_s['value'] == 'hi'
    assert t_s['value_'] == 4
test_build_schema()

# Generated at 2022-06-13 19:23:19.424591
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    initial = 'string'
    result = SchemaF().dumps(initial)
    assert result == '"string"'
    initial = 'string'
    result = SchemaF().dumps(initial, many=False)
    assert result == '"string"'
    initial = ['string']
    result = SchemaF().dumps(initial)
    assert result == '["string"]'
    initial = ['string']
    result = SchemaF().dumps(initial, many=True)
    assert result == '["string"]'

# Generated at 2022-06-13 19:23:27.573445
# Unit test for function build_schema
def test_build_schema():
    @dataclass
    class Person:
        name: str
        age: int
        married: bool
        hobbies: List[str]
        height: Optional[float]

    assert Person.schema().Meta.fields == ('name', 'age', 'married', 'hobbies', 'height')
    assert Person.schema()._declared_fields['name'].required is True
    assert Person.schema()._declared_fields['hobbies'].required is False
    assert Person.schema()._declared_fields['height'].required is False

    person = Person('Jan', 29, True, ['Aikido', 'Jogging'], 1.84)
    dumped_person = Person.schema().dump(person)

# Generated at 2022-06-13 19:23:32.635464
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    class C(typing.Generic[A]):
        # type: ignore
        pass
    a = typing.TypeVar('A', covariant=True)
    b = typing.TypeVar('B', covariant=True)
    assert issubclass(SchemaF[a, b], Schema)
    assert C[a, b] == C[a, b]
    assert C[a, b] != C[b, a]
    assert C[a, b] == C  # type: ignore
    assert C != SchemaF[a, b]  # type: ignore
    assert C == SchemaF  # type: ignore



# Generated at 2022-06-13 19:23:57.905332
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    # type: () -> None
    def my_dumps(self, obj: typing.List[A], many: bool = None) -> typing.List[TEncoded]: pass  # noqa
    SchemaF.dumps = my_dumps  # type: ignore


# Generated at 2022-06-13 19:24:09.636138
# Unit test for function build_type
def test_build_type():
    from typing import Dict, List
    from marshmallow import Schema, fields

    foo_cls = dc_fields(str, List[str], Dict[str, int])[0]
    options = {'allow_none': True}
    assert build_type(Optional[Dict[str, int]], options, Schema, foo_cls, Schema)
    assert build_type(Dict[str, int], options, Schema, foo_cls, Schema)
    assert build_type(List[int], options, Schema, foo_cls, Schema)

    assert build_type(_get_type_origin(List[int]), options, Schema, foo_cls, Schema)

# Generated at 2022-06-13 19:24:20.525390
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    record = dataclasses.dataclass(lambda: None)
    record.field = typing.List[dataclasses.dataclass]
    record.field.inner = str
    sf = SchemaF(record) # type: ignore
    actual = sf.dumps(typing.List[record.field.inner]()) # type: ignore
    assert actual == ''

# Generated at 2022-06-13 19:24:29.592371
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass


    @dataclass
    class TestClass:
        field: str


    @dataclass
    class TestClass2:
        field: str
        field2: int


    @dataclass
    class TestClass3:
        field: str
        field2: int
        field3: TestClass


    @dataclass
    class TestClass4:
        field: str
        field2: int
        field3: TestClass2
        field4: bool


    schema = build_schema(TestClass, mixin=None, infer_missing=True, partial=True)

    assert isinstance(schema.fields['field'], fields.Str)
    assert isinstance(schema, Schema)
    assert schema._declared_fields['field'].required

    schema2

# Generated at 2022-06-13 19:24:31.732635
# Unit test for constructor of class _IsoField
def test__IsoField():
    _IsoField()._deserialize("2020-11-01", "attr", data=None)



# Generated at 2022-06-13 19:24:39.958560
# Unit test for function build_schema
def test_build_schema():
    class A:
        pass
    class B:
        pass
    class C:
        pass
    class D(C):
        pass
    class E():
        pass
    class F:
        pass
    @dataclass_json
    @dataclass
    class G:
        a: A
        b: B
        c: C
        d: D
        e: typing.Optional[E]
        f: typing.Optional[F]

# Generated at 2022-06-13 19:24:47.746007
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    class S(SchemaF[int]):
        pass

    assert S().dump([1, 2]) == [1, 2]
    assert S().dump(1) == 1

    class S(SchemaF[str]):
        pass

    assert S().dump(["1", "2"]) == ["1", "2"]
    assert S().dump("1") == "1"

    class S(SchemaF[A]):
        pass

    s = S()
    s.dump([1, 2]) == [1, 2]
    s.dump([1, '2']) == [1, '2']
    s.dump(1) == 1
    s.dump('1') == '1'



# Generated at 2022-06-13 19:24:57.870925
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from typing import Optional

    from marshmallow import fields

    from marshmallow_enum import EnumField

    # some test field types not available in older Python versions
    try:
        from typing import Literal
        from typing import TypedDict
    except ImportError:
        Literal = None
        TypedDict = None

    @dataclass
    class Nested(object):
        pass

    class Enum(Enum):
        ITEM1 = 0
        ITEM2 = 1

    @dataclass
    class MyClass(object):
        item1: int
        item2: Optional[int]
        item3: Optional[List[int]]
        item4: List[int]
        item5: Tuple[int, str]
        item6: Nested

# Generated at 2022-06-13 19:25:05.920415
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    assert _TimestampField()._serialize(None, "attr", "obj") is None
    with pytest.raises(ValidationError):
        _TimestampField(required=True)._serialize(None, "attr", "obj")
    assert _TimestampField()._deserialize(None, "attr", "obj") is None
    with pytest.raises(ValidationError):
        _TimestampField(required=True)._deserialize(None, "attr", "obj")

    assert isinstance(_TimestampField()._serialize(datetime.now(), "attr", "obj"), float)
    assert isinstance(_TimestampField()._deserialize(datetime.now().timestamp(), "attr", "obj"), datetime)


# Generated at 2022-06-13 19:25:14.963471
# Unit test for constructor of class _IsoField
def test__IsoField():
    # Test constructor
    iso_field = _IsoField()
    assert iso_field.attribute is None
    assert iso_field.default is None
    assert iso_field.missing is None
    assert iso_field.data_key is None
    assert iso_field.load_from is None
    assert iso_field.dump_to is None
    assert iso_field.load_only is False
    assert iso_field.dump_only is False
    assert iso_field.error_messages == {}
    assert iso_field.validators == ()
    assert iso_field.required is False
    assert iso_field.allow_none is False
    assert iso_field.load_only is False
    assert iso_field.dump_only is False
    assert iso_field.validate_always is True


# Generated at 2022-06-13 19:26:06.745133
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import Schema, fields
    from typing import List
    obj = ['1', '2', '3']
    s = SchemaF[List[str]]()
    assert isinstance(s, Schema)
    assert s.dump(obj) == obj
    assert s.dump([]) == []



# Generated at 2022-06-13 19:26:15.171347
# Unit test for method dump of class SchemaF
def test_SchemaF_dump():
    from marshmallow import fields
    from dataclasses import dataclass

    @dataclass
    class DataClass:
        a: int

    class Schema(SchemaF[DataClass]):
        a = fields.Int()

    schema = Schema()
    schema.dump(DataClass(1))
    schema.dump([DataClass(1), DataClass(2)])

    schema.dump([])
    schema.dump(None)

    schema.dumps(DataClass(1))
    schema.dumps([DataClass(1), DataClass(2)])



# Generated at 2022-06-13 19:26:26.095634
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from typing import Union, Optional
    from marshmallow import Schema

    @dataclass
    class A:
        x: int

    @dataclass
    class B(A.schema(), Schema):
        y: Union[A, int]

    @dataclass
    class C(B.schema(), Schema):
        x: Optional[str]

    @dataclass
    class D(C.schema(), Schema):
        a: Union[int, str]

    assert isinstance(build_type(int, {}, dataclasses_json.Schema,
                               dc_fields(A)[0], A), fields.Int)

# Generated at 2022-06-13 19:26:32.496474
# Unit test for function build_type
def test_build_type():
    from typing import Dict

    assert build_type(int, {}, None, None, None) == fields.Int
    assert build_type(Dict[str, int], {}, None, None, None) == fields.Dict
# assert build_type(Dict[int, str], {}, None, None) == fields.Dict



# Generated at 2022-06-13 19:26:34.826943
# Unit test for function build_schema
def test_build_schema():
    pass  # TODO Write



# Generated at 2022-06-13 19:26:46.227495
# Unit test for function schema
def test_schema():
    import typing
    import dataclasses
    import dataclasses_json
    from dataclasses_json.mm import Schema

    @dataclasses.dataclass
    class A:
        name: str
        number: typing.Union[int, float]

    @dataclasses.dataclass
    class B:
        a: typing.Optional[A]

    assert schema(B, dataclasses_json.Mm, False) == {'a': {'name': fields.Str, 'number': fields.Field}, '__type': '__type'}

    @dataclasses.dataclass
    class C:
        name: str
        number: typing.Optional[int]

    assert schema(C, dataclasses_json.Mm, False) == {'name': fields.Str, 'number': fields.Field}



# Generated at 2022-06-13 19:26:55.456363
# Unit test for method load of class SchemaF
def test_SchemaF_load():
    @dataclass_json
    @dataclass
    class A(object):
        a: int
    @dataclass_json
    @dataclass
    class B(object):
        b: int
    a = A(1)
    b = B(2)
    assert A.SchemaF().load([a]) == [a]
    assert A.SchemaF().load(a) == a
    assert A.SchemaF().load({'a': 1}) == a
    assert A.SchemaF().load([{'a': 1}]) == [a]
    assert A.SchemaF().load({'b': 2}) == b
    assert A.SchemaF().load([{'b': 2}]) == [b]
    assert A.SchemaF().load(b) == b


# mm seems

# Generated at 2022-06-13 19:26:58.889360
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass

    @dataclass
    class Dummy:
        pass

    assert build_schema(Dummy, False, False, False)

# Generated at 2022-06-13 19:27:07.723439
# Unit test for function build_schema
def test_build_schema():
    def f(a):
        pass
    def g(a):
        pass
    @dataclass_json
    @dataclass
    class A:
        i: int
        s: str
        d: datetime
        f: float
        b: bool
        lst: typing.List[str]
        tup: typing.Tuple[str, int, float]
        dct: typing.Dict[str, str]
        u: UUID
        dc: A
        f1: f
        f2: g
        e: Enum
        s1: typing.Set[str]
        m: typing.Mapping[str, str]
        m2: typing.MutableMapping[str, str]
        u1: typing.Union[int, str]

# Generated at 2022-06-13 19:27:10.126992
# Unit test for function build_schema
def test_build_schema():
    from dataclasses import dataclass
    @dataclass
    class User:
        name: str
    assert type(build_schema(User, None, True, True))(partial=True) == build_schema(User, None, True, True)(partial=True)

# Generated at 2022-06-13 19:29:27.183751
# Unit test for function schema
def test_schema():
    @dataclass
    class User:
        name: str
        value: int = 3
        uuid: UUID
        optional_uuid: Optional[UUID] = None
        special_name: str = field(metadata={'dataclasses_json': {'letter_case': str.lower}})
        enum: Optional[Enum] = None

    assert schema(User, None, False) == {
        'name': fields.Field(),
        'value': fields.Field(default=3),
        'uuid': fields.UUID(),
        'optional_uuid': fields.UUID(),
        'special_name': fields.Field(data_key='special_name'),
        'enum': fields.Field(missing=None)
    }



# Generated at 2022-06-13 19:29:41.464466
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    class Test:
        def __init__(self, x, y=None):
            self.x = x
            self.y = y

    class TestSchema(Schema):
        x = _TimestampField()
        y = _TimestampField(required=False)

    d = datetime.now()
    ts = d.timestamp()
    assert ts == TestSchema().dump(Test(d)).data['x']
    assert TestSchema().dump(Test(d, d)).data['y'] == ts

    assert TestSchema().load({'x': ts}).data.x == d
    assert TestSchema().load({'x': ts, 'y': ts}).data.y == d

    assert TestSchema().load({'x': ts}).data.y is None

# Generated at 2022-06-13 19:29:46.188023
# Unit test for method loads of class SchemaF
def test_SchemaF_loads():
    assert SchemaF(many=True).loads([{'a': 1}]) == [{'a': 1}]

# Generated at 2022-06-13 19:29:54.510611
# Unit test for function build_schema
def test_build_schema():
    from unittest.mock import MagicMock
    from dataclasses import dataclass, field
    from marshmallow import Schema

    class ExampleSchema(Schema):
        class Meta:
            fields = ('name',)

    @dataclass
    class User:
        name: str
        email: str = None
    user = User('John', 'john@example.com')

    schema = build_schema(User, None, False, False)
    assert isinstance(schema(), ExampleSchema) is True
    assert schema().dump(user) == {'name': 'John'}

    assert isinstance(build_schema(User, None, False, False), ExampleSchema) is True


# Generated at 2022-06-13 19:30:05.402222
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    from dataclasses import dataclass

    @dataclass
    class Dc:
        a: int
        b: str

    @dataclass
    class Dc2:
        c: Dc = MISSING

    s = SchemaF.from_dataclass(Dc2)
    assert isinstance(s, SchemaF[Dc2])
    assert s.dumps(Dc2()) == '{"c": null}'
    d = s.loads('{"c": {"a": 1, "b": "bla"}}')
    assert isinstance(d, Dc2)
    assert isinstance(d.c, Dc)
    assert d.c.a == 1
    assert d.c.b == "bla"


# Generated at 2022-06-13 19:30:12.092322
# Unit test for method dumps of class SchemaF
def test_SchemaF_dumps():
    import marshmallow as mm
    @mm.post_load
    def make(self, data, **kwargs):
        return self.opts.dataclass(**data)  # type: ignore


    class DummySchemaF(SchemaF):
        def __init__(self, dataclass):
            super().__init__(unknown=mm.EXCLUDE, dataclass=dataclass)


    import dataclasses
    
    
    
    @dataclasses.dataclass
    class Dummy:
        name: str
    
    
    schema = DummySchemaF(Dummy)
    data = Dummy(name="Test")
    v = schema.dump(data)
    assert v == {"name": "Test"}



# Generated at 2022-06-13 19:30:20.999718
# Unit test for function build_schema
def test_build_schema():
    class Test1:
        pass

    class Test2(Test1):
        pass

    class Test3(Test1):
        pass

    @dataclass_json
    @dataclass
    class TestCls:
        a: 'Test1'

    assert type(TestCls).__name__ == 'TestCls'

    schema = build_schema(TestCls, None, False, False)

    try:
        assert hasattr(schema, 'Meta')
        assert issubclass(schema, Schema)
        assert hasattr(schema, 'a')
        assert isinstance(schema.a, fields.Field)
    except AssertionError:
        _logger.error("Invalid schema for `TestCls`: %s", schema)
        raise

