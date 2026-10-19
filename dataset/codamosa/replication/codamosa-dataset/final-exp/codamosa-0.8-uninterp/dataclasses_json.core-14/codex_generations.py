

# Generated at 2022-06-13 19:10:05.695766
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    t = datetime.now(timezone.utc)
    assert e.default(t) == t.timestamp()
    assert e.default(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    assert e.default(Decimal('1.2')) == '1.2'
    assert e.default(Exception()) == {}

# Generated at 2022-06-13 19:10:13.845776
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    a = _ExtendedEncoder().default(1)
    assert a == 1
    a = _ExtendedEncoder().default('a')
    assert a == 'a'
    a = _ExtendedEncoder().default(1.0)
    assert a == 1.0
    a = _ExtendedEncoder().default(True)
    assert a == True
    a = _ExtendedEncoder().default(None)
    assert a == None
    a = _ExtendedEncoder().default([])
    assert a == []
    a = _ExtendedEncoder().default([1])
    assert a == [1]
    a = _ExtendedEncoder().default((1,))
    assert a == [1]
    a = _ExtendedEncoder().default(
        {1, 2, 3})

# Generated at 2022-06-13 19:10:15.543328
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({datetime.now(timezone.utc)}) == '{}'



# Generated at 2022-06-13 19:10:25.507128
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(set([])) == '[]'
    assert json.dumps(set([1]), cls=_ExtendedEncoder) == '[1]'
    assert json.dumps([set([])]) == '[[]]'
    assert json.dumps([set([1])], cls=_ExtendedEncoder) == '[[1]]'
    assert json.dumps(frozenset([])) == '[]'
    assert json.dumps(frozenset([1]), cls=_ExtendedEncoder) == '[1]'
    assert json.dumps([frozenset([])]) == '[[]]'
    assert json.dumps([frozenset([1])], cls=_ExtendedEncoder) == '[[1]]'

# Generated at 2022-06-13 19:10:34.945536
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from datetime import datetime
    from decimal import Decimal
    from enum import Enum
    from uuid import uuid4
    from random import random
    o = [uuid4(),
         Decimal(str(random())),
         Enum('x', 'y z')('z'),
         datetime.now(timezone.utc)
         ]
    try:
        json.dumps(o, cls=_ExtendedEncoder)
    except Exception:
        print(o)
        raise
    return



# Generated at 2022-06-13 19:10:38.249539
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    expected = [1, 2, 3]
    encoded = encoder.encode(expected)
    decoded = json.loads(encoded)
    assert decoded == expected



# Generated at 2022-06-13 19:10:45.829214
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({1: "a"}) == '{"1": "a"}'
    assert _ExtendedEncoder().encode(datetime(2019, 1, 1, tzinfo=timezone.utc)) == '1546300800.0'
    assert _ExtendedEncoder().encode(Decimal(0.3)) == '"0.3"'



# Generated at 2022-06-13 19:10:53.171684
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().encode({'a': datetime(1970, 1, 1)}) == '{"a": 0}'
    assert _ExtendedEncoder().encode({'a': UUID('')}) == '{"a": "00000000-0000-0000-0000-000000000000"}'
    assert _ExtendedEncoder().encode({'a': Enum('', ())}) == '{"a": ""}'
    assert _ExtendedEncoder().encode({'a': Decimal('1')}) == '{"a": "1"}'



# Generated at 2022-06-13 19:10:59.163820
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # noinspection PyTypeChecker
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.1) == 1.1
    assert _ExtendedEncoder().default('string') == 'string'
    assert _ExtendedEncoder().default('string') == 'string'
    assert _ExtendedEncoder().default(UUID('01234567-89ab-cdef-0123-456789abcdef')) == '01234567-89ab-cdef-0123-456789abcdef'

# Generated at 2022-06-13 19:11:12.081110
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    test_strings = [
        'Test', '', '\n'
    ]
    test_ints = [
        0, 10, -10
    ]
    test_floats = [
        0.0, 1.0, -1.0, 0.5, -0.5
    ]
    test_bools = [
        True, False
    ]
    test_none = [
        None
    ]
    test_dicts = [
        {}, {1: 'a', 2: 'b', 'c': 3}, {(1, 2): {1: 'a', 2: 'b', 'c': 3}},
        {'a': 1, 'b': '1', True: [0, 1, 2], False: {'a', 'b', 'c'}}
    ]

# Generated at 2022-06-13 19:11:34.179859
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().default(None)
    assert result == None



# Generated at 2022-06-13 19:11:40.227856
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(bytearray(b'abc')) == list(b'abc')
    assert _ExtendedEncoder().default(None) == None # type: ignore
    assert _ExtendedEncoder().default({1:2}) == {1:2}
    assert _ExtendedEncoder().default([1,2]) == [1,2]
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(uuid.uuid4()) == str(uuid.uuid4())
    assert _ExtendedEncoder().default(datetime(2020, 1, 2, 12, 20, tzinfo=timezone.utc)) == 1578011600.0



# Generated at 2022-06-13 19:11:46.629556
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder()
    assert json_encoder.default(None) == None
    assert json_encoder.default(True) == True
    assert json_encoder.default(False) == False
    assert json_encoder.default(0) == 0
    assert json_encoder.default(0.0) == 0.0
    assert json_encoder.default(0.0) == 0.0
    assert json_encoder.default('a') == 'a'
    assert json_encoder.default(b'a') == 'a'
    assert json_encoder.default([]) == []
    assert json_encoder.default(()) == []
    assert json_encoder.default({}) == {}
    assert json_encoder.default(set()) == []

# Generated at 2022-06-13 19:11:57.266324
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()

    assert encoder.default(list()) == []
    assert encoder.default(tuple()) == []
    assert encoder.default({}) == {}
    assert encoder.default(set()) == []

    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({1, 2, 3}) == [1, 2, 3]

    assert encoder.default({'a': 'b'}) == {'a': 'b'}
    assert encoder.default({'a': {'b': {'c': 'd'}}}) == {'a': {'b': {'c': 'd'}}}


# Generated at 2022-06-13 19:11:59.085309
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'



# Generated at 2022-06-13 19:12:06.514921
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(["element", 1]) == "[\"element\", 1]"
    assert _ExtendedEncoder().encode({"key": "value"}) == "{\"key\": \"value\"}"
    assert _ExtendedEncoder().encode({"key": {"nested": 1}}) == "{\"key\": {\"nested\": 1}}"
    assert _ExtendedEncoder().encode({"key": {"nested": ["e1", "e2"]}}) == "{\"key\": {\"nested\": [\"e1\", \"e2\"]}}"
    assert _ExtendedEncoder().encode(datetime.utcnow().replace(tzinfo=timezone.utc)) == "\"" + str(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()) + "\""

# Generated at 2022-06-13 19:12:12.281653
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode({1: 1, 2: 2}) == '{"1": 1, "2": 2}'
    assert _ExtendedEncoder().encode(b'123') == '"MTIz"'
    assert _ExtendedEncoder().encode((1, 2)) == '[1, 2]'
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1)) == '0.0'

# Generated at 2022-06-13 19:12:22.923368
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o1 = {'a': 1, 'b': 2}
    o2 = [1, 2, 3]
    o3 = datetime.now(timezone.utc)
    o4 = UUID('5e5fae70-353e-4b52-af81-a6df0b4c4b4f')
    o5 = Decimal('12.34')
    assert json.dumps(o1, cls=_ExtendedEncoder) == json.dumps(o1)
    assert json.dumps(o2, cls=_ExtendedEncoder) == json.dumps(o2)
    assert json.dumps(o3, cls=_ExtendedEncoder) == json.dumps(o3.timestamp())

# Generated at 2022-06-13 19:12:25.797153
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    d = {}
    assert _ExtendedEncoder().encode(d) == '{}'
    assert _ExtendedEncoder().encode(Test) == '"Test"'



# Generated at 2022-06-13 19:12:27.237977
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    d = _ExtendedEncoder().encode(datetime(2018, 8, 27, 12, 0, 0, tzinfo=timezone.utc))
    assert d == "1535336800.0"



# Generated at 2022-06-13 19:12:48.123988
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = [1, 2, 3]
    encoder = _ExtendedEncoder()
    encoder.default(o)



# Generated at 2022-06-13 19:12:56.829716
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2, 'c': 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2, 'c': 3}) == \
           _ExtendedEncoder().encode(dict(a=1, b=2, c=3))
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(0) == '0'

# Generated at 2022-06-13 19:13:02.227079
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # type: () -> None
    test: Json = _ExtendedEncoder.default(None, [1, 2, 3])
    assert test == [1, 2, 3]
    test = _ExtendedEncoder.default(None, {'a': 1})
    assert test == {'a': 1}
    test = _ExtendedEncoder.default(None, datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc))
    assert test == 0
    test = _ExtendedEncoder.default(None, UUID('2ad2f425-a401-4d36-9d27-7a9f72d6ea7e'))
    assert test == '2ad2f425-a401-4d36-9d27-7a9f72d6ea7e'
   

# Generated at 2022-06-13 19:13:11.156789
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(42) == 42
    assert _ExtendedEncoder().default(3.14) == 3.14
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(datetime.utcnow()) == datetime.utcnow().timestamp()
    assert _ExtendedEncoder().default(UUID('0b1cf2b9-9b93-4215-8c14-ad0c71e75b7c')) == '0b1cf2b9-9b93-4215-8c14-ad0c71e75b7c'

# Generated at 2022-06-13 19:13:20.779205
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1,2,3]) == [1,2,3]
    assert encoder.default({"a": 100}) == {"a": 100}
    assert encoder.default(123) == 123
    assert encoder.default("abc") == "abc"
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None
    assert encoder.default(1.1) == 1.1
    assert encoder.default(datetime.now()) != None

# Generated at 2022-06-13 19:13:25.445387
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
  from datetime import datetime
  from uuid import uuid4, UUID
  from decimal import Decimal
  from enum import Enum

  class TestEnum(Enum):
    test = 1

  assert json.dumps({}, cls=_ExtendedEncoder) == "{}"
  assert json.dumps([], cls=_ExtendedEncoder) == "[]"
  assert json.dumps(datetime.now(), cls=_ExtendedEncoder)
  uuid = uuid4()
  assert json.dumps(uuid, cls=_ExtendedEncoder) == f'"{str(uuid)}"'
  assert json.dumps(Decimal(12.3), cls=_ExtendedEncoder) == '"12.3"'

# Generated at 2022-06-13 19:13:29.533395
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    u = UUID('bfd6c9f9-b856-4a6b-86bd-e8dea55a6aee')
    assert str(u) == _ExtendedEncoder().default(u)



# Generated at 2022-06-13 19:13:41.432994
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

    class Dummy(object):
        def __init__(self):
            pass

    assert encoder.default(Dummy()) == dict()



# Generated at 2022-06-13 19:13:51.944799
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode(frozenset()) == '[]'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(13) == '13'
    assert _ExtendedEncoder().encode(3.14) == '3.14'
    assert _ExtendedEncoder().encode("a") == '"a"'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    datetime_

# Generated at 2022-06-13 19:13:58.138441
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder.default(None, {"a": [1, 2, 3]}) == {"a": [1, 2, 3]}
    assert _ExtendedEncoder.default(None, [1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder.default(None, datetime.now()) == 1603225088.0
    assert _ExtendedEncoder.default(None, datetime.now(timezone.utc)) == 1603225568.0
    assert _ExtendedEncoder.default(None, UUID('6ccd780c-baba-1026-9564-0040f4311e29')) == "6ccd780c-baba-1026-9564-0040f4311e29"

# Generated at 2022-06-13 19:14:49.107712
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Test the default encoder
    assert _ExtendedEncoder().encode(Decimal(2) / Decimal(3)) == '"0.6666666666666667"'
    assert _ExtendedEncoder().encode(Decimal(2) / Decimal(15)) == '"0.13333333333333333"'
    assert (
        _ExtendedEncoder().encode(datetime(year=1970, month=1, day=1, tzinfo=timezone.utc)) ==
        '0'
    )
    assert _ExtendedEncoder().encode([True]) == '[true]'
    assert _ExtendedEncoder().encode({'a': False}) == '{"a":false}'

# Generated at 2022-06-13 19:14:57.090972
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(True, cls=_ExtendedEncoder) == 'true'

    assert json.dumps(None, cls=_ExtendedEncoder) == 'null'

    assert json.dumps('string', cls=_ExtendedEncoder) == '"string"'

    assert json.dumps(1, cls=_ExtendedEncoder) == '1'

    assert json.dumps(1.0, cls=_ExtendedEncoder) == '1.0'

    assert json.dumps(1.1, cls=_ExtendedEncoder) == '1.1'

    assert json.dumps([1, 2.0, '3', True, None], cls=_ExtendedEncoder) == \
        '[1, 2.0, "3", true, null]'


# Generated at 2022-06-13 19:15:06.612910
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1,2,3]) == '[1,2,3]'
    assert _ExtendedEncoder().encode([1,2,3]) == _ExtendedEncoder().encode((1,2,3))
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a":1,"b":2}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == _ExtendedEncoder().encode(dict([('a', 1), ('b', 2)]))
    assert _ExtendedEncoder().encode(datetime.fromtimestamp(1000000.0, timezone.utc)) == '1000000.0'

# Generated at 2022-06-13 19:15:08.475267
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from dataclasses import dataclass

    @dataclass
    class Dummy:
        pass

    assert _ExtendedEncoder().default(Dummy()) == None



# Generated at 2022-06-13 19:15:14.433867
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # noinspection PyUnusedLocal
    def _assert(obj: Any, expected: Json):
        actual = _ExtendedEncoder().encode(obj)
        assert actual == expected
        return
    
    _assert(['a', 'b'], '[\n    "a",\n    "b"\n]')
    _assert({'a': 'b'}, '{\n    "a": "b"\n}')
    _assert(datetime(2020, 4, 1, 16, 0, 0, tzinfo=timezone.utc), '1585753600.0')

# Generated at 2022-06-13 19:15:18.876077
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    meta = {"a": 1, "b": [1, 2], "c": {"d": None}}
    assert _ExtendedEncoder().encode(meta) == json.dumps(meta, cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:15:25.868901
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode([1, 2, {'a': 1, 'b': 2}]) == '[1, 2, {"a": 1, "b": 2}]'



# Generated at 2022-06-13 19:15:31.512516
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import json
    import pytest
    from uuid import uuid4
    from datetime import datetime
    from decimal import Decimal
    from typing import Dict
    class SomeEnum(Enum):
        a = 2
    class SomeClass:
        class_field: str = "a"
        def __eq__(self, other):
            return (type(self) == type(other) and
                    self.class_field == other.class_field)
        def __repr__(self):
            return f"SomeClass({self.class_field!r})"
    @dataclass
    class Record:
        name: str
        value: int
    @dataclass
    class SomeDataClass:
        uuid_field: UUID = uuid4()
        datetime_field: datetime = datetime.now

# Generated at 2022-06-13 19:15:38.481011
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    def check(data, expected):
        actual = _ExtendedEncoder().encode(data)
        assert actual == expected

    check([1, 2, 3], '[1, 2, 3]')
    check({'a': 1, 'b': 2}, '{"a": 1, "b": 2}')
    check(datetime(2017, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc), '1514671999.999999')
    check(UUID('6ba7b811-9dad-11d1-80b4-00c04fd430c8'), '"6ba7b811-9dad-11d1-80b4-00c04fd430c8"')

# Generated at 2022-06-13 19:15:47.218040
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict(a=1, b=2)) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(3.14) == '3.14'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'

# Generated at 2022-06-13 19:16:40.873805
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    for o in [
            [],
            {},
            datetime(2020, 4, 4, 11, 11, tzinfo=timezone.utc),
            UUID('12345678123456781234567812345678'),
            Decimal(1.0),
            Decimal('1.1'),
            Decimal('1e+1'),
            Decimal('1E+1'),
    ]:
        assert encoder.default(o) == o


# Generated at 2022-06-13 19:16:47.827067
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(
        datetime.fromtimestamp(10000, timezone.utc).replace(microsecond=1234)
    ) == 10000.012
    assert _ExtendedEncoder().default(UUID('e6338911-e898-4efd-adfc-eb3e8e1f4d1c')) == 'e6338911-e898-4efd-adfc-eb3e8e1f4d1c'
    assert _ExtendedEncoder().default(
        Decimal('1.001')
    ) == '1.001'
    assert _ExtendedEncoder().default(
        {'a': 1, 'b': 2}
    ) == {'a': 1, 'b': 2}

# Generated at 2022-06-13 19:17:00.518640
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Python 3.8 compatibility
    datetime_ = datetime.fromtimestamp(1, timezone.utc)
    encoder = _ExtendedEncoder()
    test_cases = [
        ([[], {}], [[], {}]),
        (True, True),
        (False, False),
        (None, None),
        (datetime_, datetime_.timestamp()),
        (Decimal('1.2'), '1.2'),
        (UUID('3b6b21e9-9f82-4770-93a7-1eb86c16e764'), '3b6b21e9-9f82-4770-93a7-1eb86c16e764'),
    ]
    for (obj, expected) in test_cases:
        actual = encoder.default(obj)
       

# Generated at 2022-06-13 19:17:07.250981
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode({'a': 1}) == '{"a": 1}'
    assert encoder.encode([1, 2, 3]) == '[1, 2, 3]'
    assert encoder.encode(datetime.now(timezone.utc)) == '0.0'
    assert encoder.encode(UUID('49a1e351-1ee4-4b0c-ac62-0a4a4e173574')) == '"49a1e351-1ee4-4b0c-ac62-0a4a4e173574"'
    assert encoder.encode(Decimal('1.1')) == '"1.1"'



# Generated at 2022-06-13 19:17:18.369755
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_str = json.dumps(
        [dict(a=1), [1, 2, 3], datetime(2020, 1, 1, tzinfo=timezone.utc), UUID('c6efc50b-2bba-4b1f-aba6-c7b3faa6a225'),
         Enum('a', 'a b c'), Decimal('1.1')], cls=_ExtendedEncoder)
    expected_json_str = '''[{"a": 1}, [1, 2, 3], 1577836800.0, "c6efc50b-2bba-4b1f-aba6-c7b3faa6a225", "a", "1.1"]'''
    assert json_str == expected_json_str



# Generated at 2022-06-13 19:17:22.607537
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({"A": 1, "B": 2}) == '{"A": 1, "B": 2}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == 'null'


# Generated at 2022-06-13 19:17:29.364323
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    enc = _ExtendedEncoder()
    assert enc.default([]) == []
    assert enc.default({}) == {}
    assert enc.default(set()) == []
    assert enc.default(frozenset()) == []
    assert enc.default((1,2)) == [1,2]
    assert enc.default({'a': 1}) == {'a': 1}
    dt = datetime.now(tz=timezone.utc)
    assert enc.default(dt) == dt.timestamp()
    assert enc.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert enc.default(cfg.ENRICH_JSON_ENCODER) == True

# Generated at 2022-06-13 19:17:39.367148
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1]) == [1]
    assert _ExtendedEncoder().default({1: 2}) == {1: 2}
    assert _ExtendedEncoder().default(datetime(2018, 1, 1, 1, 0, 0, tzinfo=timezone.utc)) == 1514764800
    assert _ExtendedEncoder().default(Decimal('1.1')) == '1.1'
    assert _ExtendedEncoder().default(UUID('{12345678-1234-5678-1234-567812345678}')) == '12345678-1234-5678-1234-567812345678'
    assert _ExtendedEncoder().default(Enum('Test', 'foo bar')('foo')) == 'foo'

# Generated at 2022-06-13 19:17:44.931033
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert str(UUID('123e4567-e89b-42d3-a456-556642440000')) == encoder.default(UUID('123e4567-e89b-42d3-a456-556642440000'))
    assert {'foo': 10} == encoder.default({'foo': 10})
    assert datetime(2020, 8, 28, 16, 8, 39, 485551, tzinfo=timezone.utc).timestamp() == encoder.default(datetime(2020, 8, 28, 16, 8, 39, 485551, tzinfo=timezone.utc))
    assert '123' == encoder.default(Decimal('123'))

# Generated at 2022-06-13 19:17:54.563366
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(['a', 'b']) == ['a', 'b']
    assert _ExtendedEncoder().default(dict(a='a', b='b')) == dict(a='a', b='b')
    assert _ExtendedEncoder().default(UUID('467fa5f5-4181-4a4c-9d9c-c39f6600fe29')) == '467fa5f5-4181-4a4c-9d9c-c39f6600fe29'
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == '1569479255'
    assert _ExtendedEncoder().default(Decimal('1.1')) == '1.1'



# Generated at 2022-06-13 19:19:02.601766
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps([12, 34, 56], cls=_ExtendedEncoder)
    assert True

_EXT_ENCODER = _ExtendedEncoder()


# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 19:19:10.011901
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == "{}"
    assert _ExtendedEncoder().encode([]) == "[]"
    assert _ExtendedEncoder().encode(True) == "true"
    assert _ExtendedEncoder().encode(False) == "false"
    assert _ExtendedEncoder().encode(None) == "null"
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(datetime(2020, 12, 1, 12, tzinfo=timezone.utc)) == "1606857200.0"
    assert _ExtendedEncoder().encode

# Generated at 2022-06-13 19:19:20.030672
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(map(lambda x: x**2, range(5))) == '[0, 1, 4, 9, 16]'
    assert _ExtendedEncoder().encode({0: 1, 1: 2}) == '{"0": 1, "1": 2}'
    assert _ExtendedEncoder().encode(datetime(2018, 9, 19, 12, 31, tzinfo=timezone.utc)) == '1537294660000.0'
    assert _ExtendedEncoder().encode(UUID('123e4567-e89b-12d3-a456-426655440000')) == '"123e4567-e89b-12d3-a456-426655440000"'
    assert _ExtendedEncoder().encode(1.5) == '1.5'

# Generated at 2022-06-13 19:19:28.851382
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Decimal(1.1)) == json.dumps(str(Decimal(1.1)))
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == json.dumps(datetime.now(timezone.utc).timestamp())
    assert _ExtendedEncoder().encode(UUID('12345678123456781234567812345678')) == json.dumps(str(UUID('12345678123456781234567812345678')))
    assert _ExtendedEncoder().encode(Enum) == json.dumps(Enum.value)

# Generated at 2022-06-13 19:19:35.559935
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(frozenset([1, 2, 3])) == [1, 2, 3]
    assert encoder.default({1: 1, 2: 2}) == {1: 1, 2: 2}
    assert encoder.default(datetime(2020, 4, 22)) == 1587481600.0
    assert encoder.default(datetime(2020, 4, 22, tzinfo=timezone.utc)) == 1587481600.0