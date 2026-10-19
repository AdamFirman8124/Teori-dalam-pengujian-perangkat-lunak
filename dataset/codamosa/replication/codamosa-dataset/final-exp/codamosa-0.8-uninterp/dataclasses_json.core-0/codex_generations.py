

# Generated at 2022-06-13 19:10:16.981414
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    cls = _ExtendedEncoder()
    assert cls.encode({}) == '{}'
    assert cls.encode([]) == '[]'
    assert cls.encode({'a': 1}) == '{"a": 1}'
    assert cls.encode([1]) == '[1]'
    assert cls.encode({"a": [1]}) == '{"a": [1]}'
    assert cls.encode(1) == '1'
    assert cls.encode(True) == 'true'
    assert cls.encode(None) == 'null'
    assert cls.encode(datetime(year=2020, month=1, day=1)) == '1577836800.0'



# Generated at 2022-06-13 19:10:23.996244
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc)) == 946684800.0
    assert encoder.default(UUID('0d180a65-1b93-42ef-8e5f-f02b4d4b4040')) == '0d180a65-1b93-42ef-8e5f-f02b4d4b4040'
    assert encoder.default(Decimal('0.01234')) == '0.01234'



# Generated at 2022-06-13 19:10:29.381093
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(2019, 1, 1)) == "1546300800.0"
    assert _ExtendedEncoder().encode(UUID('1234567890')) == "12345678-9000-0000-0000-000000000000"
    assert _ExtendedEncoder().encode(
        Enum('Foo', {'foo': 1, 'bar': 2})
    ) == "1"
    assert _ExtendedEncoder().encode(Decimal(1.1)) == "1.1"

# An encoder that can encode an arbitrary object to json.

# Generated at 2022-06-13 19:10:41.167028
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1, 2, 3}) == json.dumps({1, 2, 3})
    assert _ExtendedEncoder().encode({1: 2}) == json.dumps({1: 2})
    assert _ExtendedEncoder().encode(
        datetime(2020, 1, 3, 17, 18, 19, tzinfo=timezone.utc)) == json.dumps(
            1578153499)
    assert _ExtendedEncoder().encode(
        UUID('fa3f68eb-b8e9-4e1e-9d5f-35f8c240f0a3')) == json.dumps(
            "fa3f68eb-b8e9-4e1e-9d5f-35f8c240f0a3")
   

# Generated at 2022-06-13 19:10:51.520581
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(UUID('cb2f4d4e-7326-4a3b-a657-81f4cfd4f4be')) == 'cb2f4d4e-7326-4a3b-a657-81f4cfd4f4be'
    assert encoder.default(Enum('Test', {'one': 1})) == 1
    assert encoder.default(Decimal('12.00')) == '12.00'
    assert encoder.default(Exception()) == 'Exception()'



# Generated at 2022-06-13 19:10:55.323260
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import pytest

    def check_str_type(result):
        assert result['a'] == 1
        assert result['b'] == 2
        assert result['c'] == 3

    @pytest.mark.parametrize(
        "obj, result", [
            (datetime.fromtimestamp(0, tz=timezone.utc), 0),
            (UUID(int=0), '00000000-0000-0000-0000-000000000000'),
            (Decimal('0.0'), '0.0')
        ])
    def test_default(obj, result):
        assert _ExtendedEncoder().default(obj) == result


UNDEFINED = object()



# Generated at 2022-06-13 19:11:10.957732
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode(['1', 2]) == '["1", 2]'
    assert encoder.encode({'a': 3}) == '{"a": 3}'
    assert encoder.encode(datetime.now(tz=timezone.utc)) == '["datetime", "1970-01-01T00:00:00.000000Z"]'
    assert encoder.encode(UUID('54f8c7b5-0e5e-4e61-bd0c-7e05426439b4')) == '"54f8c7b5-0e5e-4e61-bd0c-7e05426439b4"'
    assert encoder.encode(Decimal('3.14')) == '"3.14"'


# Generated at 2022-06-13 19:11:25.255059
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode(1) == '1'
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode('s') == '"s"'
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode(1.0) == '1.0'
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode(None) == 'null'
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode(True) == 'true'
    assert _ExtendedEncoder(indent=4, sort_keys=True).encode(False) == 'false'
    assert _ExtendedEncoder(indent=4, sort_keys=True).en

# Generated at 2022-06-13 19:11:34.338711
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import pytest
    enc = _ExtendedEncoder()
    # Test with a list instance
    assert enc.default([1, 2, 3]) == [1, 2, 3]
    # Test with a list of data types that must be converted to JSON
    assert enc.default([1, datetime.now(timezone.utc), Decimal(1.0), UUID('5dd5beb7-977d-455b-93da-e4e4c4d13589')]) == \
           [1, datetime.now(timezone.utc).timestamp(), '1.0', str(UUID('5dd5beb7-977d-455b-93da-e4e4c4d13589'))]
    # Test with a dictionary that should not be changed

# Generated at 2022-06-13 19:11:39.861784
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now(timezone.utc))
    assert encoder.default([1, 2, 3])
    assert encoder.default({"a": 1, "b": 2, "c": 3})
    assert encoder.default(set([1, 2, 3]))
    assert encoder.default(frozenset([1, 2, 3]))
    assert encoder.default(UUID("192b7915-1a6a-410c-8e39-f5e7e0ad0cac"))
    assert encoder.default(Decimal("12.34"))



# Generated at 2022-06-13 19:12:08.620524
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode(set()) == '[]'
    assert encoder.encode(frozenset()) == '[]'
    assert encoder.encode(b'foo') == '"foo"'
    assert encoder.encode(bytearray(b'foo')) == '"foo"'
    assert encoder.encode(bytes([97, 98, 99])) == '"abc"'
    assert encoder.encode(bytes(['a', 'b', 'c'])) == '"abc"'
    assert encoder.encode(datetime.now(timezone.utc)) == '"{}"'.format(datetime.now(timezone.utc).timestamp())

# Generated at 2022-06-13 19:12:19.977755
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(0) == 0
    assert encoder.default(0.0) == 0.0
    assert encoder.default("") == ""
    assert encoder.default([]) == []
    assert encoder.default(()) == []
    assert encoder.default(set()) == []
    assert encoder.default(dict()) == {}
    assert encoder.default(frozenset()) == []
    assert encoder.default(True) is True
    assert encoder.default(False) is False
    assert encoder.default(None) is None
    assert encoder.default(datetime.utcnow()) == datetime.utcnow().timestamp()


# Generated at 2022-06-13 19:12:31.647795
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default({1, 2, 3}) == [1, 2, 3]
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert encoder.default(datetime.now(tz=timezone.utc)) == \
           datetime.now(tz=timezone.utc).timestamp()
    assert encoder.default(UUID('85769edf-eabe-4b55-9f32-8ce6415d1b41')) == \
           '85769edf-eabe-4b55-9f32-8ce6415d1b41'
    assert encoder.default

# Generated at 2022-06-13 19:12:41.713891
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json1 = json.dumps({1, 2, 3, 4}, cls=_ExtendedEncoder)
    assert json1 == '[1, 2, 3, 4]'
    json2 = json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder)
    assert json2 == '{"a": 1, "b": 2}'
    json3 = json.dumps(datetime(year=2020, month=6, day=6, tzinfo=timezone.utc), cls=_ExtendedEncoder)
    assert json3 == '1591459200.0'
    json4 = json.dumps(UUID('c82a14a2-f4d9-4908-aa36-9ec0e7c34b05'), cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:12:43.059333
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # type: () -> None
    _ExtendedEncoder()


# Generated at 2022-06-13 19:12:45.861138
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_str = _ExtendedEncoder().encode([1,2,3])
    assert json_str == '[]'


# Generated at 2022-06-13 19:13:04.472064
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(None) is None
    assert e.default(True) is True
    assert e.default(1) == 1
    assert e.default(1.0) == 1.0
    assert e.default('foo') == 'foo'
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default([('a', 1), ('b', 2)]) == [('a', 1), ('b', 2)]
    assert e.default((1,)) == [1]
    assert e.default(set({1, 2})) == [1, 2]
    assert e.default(set(('a', 'b'))) == ['a', 'b']

# Generated at 2022-06-13 19:13:12.223228
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(dict(a=1)) == {"a": 1}
    assert _ExtendedEncoder().default(list(range(5))) == [0, 1, 2, 3, 4]
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert _ExtendedEncoder().default(UUID('123e4567-e89b-12d3-a456-426655440000')) == '123e4567-e89b-12d3-a456-426655440000'
    assert _ExtendedEncoder().default(MockEnum.v1) == 1

# Generated at 2022-06-13 19:13:13.207839
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(list(range(2)), cls=_ExtendedEncoder) == '2'


# Generated at 2022-06-13 19:13:17.925735
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({"1": "2"}) == '{"1": "2"}'
    assert _ExtendedEncoder().encode(datetime.strptime('2009-10-17', '%Y-%m-%d').replace(tzinfo=timezone.utc)) == '1255999600.0'


# Generated at 2022-06-13 19:14:03.514098
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # type: () -> None
    assert _ExtendedEncoder().default({'a': 1}) == {'a': 1}
    assert _ExtendedEncoder().default([1, 2]) == [1, 2]
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(0.1) == 0.1
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(None) is None
    with pytest.raises(TypeError) as exc:
        _ExtendedEncoder().default(set())
    assert "is not JSON serializable" in str(exc.value)

# Generated at 2022-06-13 19:14:10.498476
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    obj = object()
    obj_id = id(obj)

    encoder = e.encode(obj)
    decoder = json.loads(encoder)

    assert type(decoder) == dict
    assert decoder['__class__'] == '__main__.object'
    assert decoder['__module__'] == '__main__'
    assert decoder['__args__']['id'] == obj_id

    # TODO: test for collections, UUID, Enum, etc.


# Generated at 2022-06-13 19:14:20.366799
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # 1) Collection
    # 1.1) Mapping
    assert _ExtendedEncoder().default({'test': 'test'}) == {'test': 'test'}
    # 1.2) List
    assert _ExtendedEncoder().default(['test']) == ['test']

    # 2) datetime
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()

    # 3) UUID
    uuid = UUID('123e4567-e89b-12d3-a456-426655440000')
    assert _ExtendedEncoder().default(uuid) == str(uuid)

    # 4) Enum
    class E(Enum):
        A = 1
        B = 2
        C = 3

# Generated at 2022-06-13 19:14:27.305606
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoded = _ExtendedEncoder().encode([1, 2, 3])
    assert encoded == 'json.encoder.JSONEncoder().encode([1, 2, 3])'
    encoded = _ExtendedEncoder().encode({'a': 1, 'b': 2})

# Generated at 2022-06-13 19:14:37.615196
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    # Field of datetime
    t = datetime.now(tz=timezone.utc)
    assert _ExtendedEncoder().encode(t) == str(t.timestamp())

# Generated at 2022-06-13 19:14:45.053344
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    my_encoder = _ExtendedEncoder()
    assert True == my_encoder.default(('abc',))
    assert True == my_encoder.default(['abc'])
    assert True == my_encoder.default({'abc':123})
    assert True == my_encoder.default(123)
    assert True == my_encoder.default('abc')
    assert True == my_encoder.default(True)
    assert True == my_encoder.default(None)



# Generated at 2022-06-13 19:14:46.948449
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()
    _ExtendedEncoder.default(None, 1)



# Generated at 2022-06-13 19:14:49.865454
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Given
    instance = _ExtendedEncoder()

    # When
    result = instance.default({"a": 1, "b": 2})

    # Then
    assert result == {'a': 1, 'b': 2}




# Generated at 2022-06-13 19:14:57.855247
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # Test 1
    result = _ExtendedEncoder().default([1,2,3])
    assert result == [1,2,3]
    # Test 2
    result = _ExtendedEncoder().default({'a':1,'b':2, 'c':3})
    assert result == {'a':1,'b':2, 'c':3}
    # Test 3
    result = _ExtendedEncoder().default(datetime(2020, 1, 2, 22, 2, 20, tzinfo=timezone.utc))
    assert result == 1578133340.0
    # Test 4
    result = _ExtendedEncoder().default(UUID('6ad58d6d-68c6-4444-8581-e023c7709bcf'))

# Generated at 2022-06-13 19:15:06.996959
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) == json.JSONEncoder().default(datetime.now())
    assert _ExtendedEncoder().default(tuple()) == json.JSONEncoder().default(tuple())
    assert _ExtendedEncoder().default(set()) == json.JSONEncoder().default(set())
    assert _ExtendedEncoder().default(frozenset()) == json.JSONEncoder().default(frozenset())
    assert _ExtendedEncoder().default(list()) == json.JSONEncoder().default(list())
    assert _ExtendedEncoder().default(dict()) == json.JSONEncoder().default(dict())

# Generated at 2022-06-13 19:16:58.304823
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import json
    import uuid
    from datetime import datetime
    from enum import Enum
    from decimal import Decimal
    import jsonpickle
    import uuid
    from datetime import datetime
    from enum import Enum
    from decimal import Decimal
    from typing import List, Dict, Set, Mapping
    from unittest import TestCase

    class TestEnum(Enum):
        A = 1
    class TestCls:
        def __init__(self):
            self.a = 1
            self.b = 'b'
    class TestCls2:
        def __init__(self, a, b):
            self.a = a
            self.b = b

# Generated at 2022-06-13 19:16:59.159184
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'



# Generated at 2022-06-13 19:17:09.542518
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    obj = _ExtendedEncoder()
    dt = datetime.now()
    assert obj.default(dt) == dt.timestamp()
    test_list = [1, 2, 3, 4]
    assert obj.default(test_list) == test_list
    test_dict = {'key': 'a'}
    assert obj.default(test_dict) == test_dict
    test_uuid = UUID('12345678123456781234567812345678')
    assert obj.default(test_uuid) == str(test_uuid)
    assert obj.default(0.1) == 0.1
    assert obj.default(None) == None
    assert obj.default('a') == 'a'
    assert obj.default(True) == True



# Generated at 2022-06-13 19:17:10.757260
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode



# Generated at 2022-06-13 19:17:19.443196
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

# Generated at 2022-06-13 19:17:37.467283
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(None) == None
    assert e.default(True) == True
    assert e.default(False) == False
    assert e.default(1) == 1
    assert e.default(1.1) == 1.1
    assert e.default('abc') == 'abc'
    assert e.default(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert e.default({'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}
    assert e.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()

# Generated at 2022-06-13 19:17:42.429763
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:17:48.513815
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_obj = json.loads(json.dumps(_ExtendedEncoder().default(set([1, 2, 3]))))
    assert 1 in json_obj
    assert 2 in json_obj
    assert 3 in json_obj
    assert len(json_obj) == 3



# Generated at 2022-06-13 19:17:55.467174
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(datetime(1970, 1, 1, 1, 0, tzinfo=timezone.utc)) == 3600
    assert _ExtendedEncoder().default(UUID('59ff49e8-c6d7-4a9d-947b-880ba1d2ff19')) == '59ff49e8-c6d7-4a9d-947b-880ba1d2ff19'
    assert _ExtendedEncoder().default(Decimal('1.0')) == '1.0'

_Empty = namedtuple('_Empty', 'sentinel')()



# Generated at 2022-06-13 19:18:06.485421
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    structured_data = {'a': 1, 'b': 2}
    structured_data_encoded = json.dumps(structured_data, cls=_ExtendedEncoder)
    assert structured_data_encoded == '{"a": 1, "b": 2}'

    structured_data = ['a', 1, 2]
    structured_data_encoded = json.dumps(structured_data, cls=_ExtendedEncoder)
    assert structured_data_encoded == '["a", 1, 2]'

    unstructured_data = 1
    unstructured_data_encoded = json.dumps(unstructured_data, cls=_ExtendedEncoder)
    assert unstructured_data_encoded == '1'

    unstructured_data = 1.1
    unstructured_data_