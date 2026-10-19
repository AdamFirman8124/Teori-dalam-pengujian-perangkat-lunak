

# Generated at 2022-06-13 19:10:04.081030
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({"1": 1}) == '{"1": 1}'
    assert _ExtendedEncoder().encode(UUID("00000000-0000-0000-0000-000000000000")) == '"00000000-0000-0000-0000-000000000000"'
    assert _ExtendedEncoder().encode(datetime(2020, 2, 15, 2, 30, tzinfo=timezone.utc)) == '1581770200.0'
    assert _ExtendedEncoder().encode(Decimal('1')) == '"1"'

_extended_encoder = _ExtendedEncoder()



# Generated at 2022-06-13 19:10:12.693807
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    a = _ExtendedEncoder()
    assert a.default(1) == 1
    assert a.default(1.0) == 1.0
    assert a.default('a') == 'a'
    assert a.default([1, 2, 3]) == [1, 2, 3]
    assert a.default(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert a.default((1, 2, 3)) == [1, 2, 3]
    assert a.default(('a', 'b', 'c')) == ['a', 'b', 'c']
    assert a.default({'a': 1}) == {'a': 1}
    dt = datetime.now(timezone.utc)
    assert a.default(dt) == dt.timestamp()
    uuid

# Generated at 2022-06-13 19:10:21.781576
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(['a', 'b', 'c']) == '["a", "b", "c"]'
    assert _ExtendedEncoder().encode({"a":1, "b":2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(UUID(int=0)) == '00000000-0000-0000-0000-000000000000'
    assert _ExtendedEncoder().encode(Enum('TestEnum', [('a', 1)])(1)) == '1'
    assert _ExtendedEncoder().encode(Decimal('3.14')) == '"3.14"'


# Generated at 2022-06-13 19:10:29.210620
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(set()) == list()
    assert encoder.default(tuple()) == list()
    assert encoder.default(frozenset()) == list()
    assert encoder.default(dict()) == dict()
    assert encoder.default(set((1, 2))) == list((1, 2))
    assert encoder.default(tuple((1, 2))) == list((1, 2))
    assert encoder.default(frozenset((1, 2))) == list((1, 2))
    assert encoder.default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert encoder.default(datetime(2001, 12, 12, 12, 12, 12, 12, tzinfo=timezone.utc)) == 100

# Generated at 2022-06-13 19:10:41.019497
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(1, cls=_ExtendedEncoder)
    json.dumps("", cls=_ExtendedEncoder)
    json.dumps(dict(), cls=_ExtendedEncoder)
    json.dumps(list(), cls=_ExtendedEncoder)
    json.dumps(set(), cls=_ExtendedEncoder)
    json.dumps(1.1, cls=_ExtendedEncoder)
    json.dumps(True, cls=_ExtendedEncoder)
    json.dumps(None, cls=_ExtendedEncoder)
    json.dumps(Decimal(1), cls=_ExtendedEncoder)
    json.dumps(UUID('12345678123456781234567812345678'), cls=_ExtendedEncoder)
   

# Generated at 2022-06-13 19:10:51.728537
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder(indent=4)
    assert encoder.encode(None) == 'null'
    assert encoder.encode(True) == 'true'
    assert encoder.encode(3) == '3'
    assert encoder.encode('string') == '"string"'
    assert encoder.encode('"quoted"') == '"\\"quoted\\""'
    assert encoder.encode([]) == '[]'
    assert encoder.encode({}) == '{}'
    assert encoder.encode([[]]) == '[[]]'
    assert encoder.encode(list(range(10))) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'


# Generated at 2022-06-13 19:10:58.064635
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from typing import Dict, Optional
    from dataclasses import dataclass
    import dataclasses
    import datetime
    import uuid
    import decimal
    import json

    @dataclass
    class Point:
        x: str
        y: int

    @dataclass
    class Data:
        spec: Optional[Dict[str, str]]

    def _assert_encode(obj, expected):
        encoded = json.dumps(obj, cls=_ExtendedEncoder)
        assert encoded == expected

    _assert_encode(u'привет', '"привет"')

# Generated at 2022-06-13 19:11:11.772084
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder(sort_keys=True, indent=4).default(2) == 2
    assert _ExtendedEncoder(sort_keys=True, indent=4).default('abc') == 'abc'
    assert _ExtendedEncoder().default(['a', 1]) == ['a', 1]
    assert _ExtendedEncoder().default({'a': 1}) == {'a': 1}
    assert _ExtendedEncoder().default(datetime(2000, 1, 2, 3, 4, 5, 0, tzinfo=timezone.utc)) == 946862245.0

# Generated at 2022-06-13 19:11:22.485618
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Verify that ExtendedEncoder works, and gives the same result as json.dumps
    # for some basic test cases
    for test_object in [
        [1, 2, 3],
        {"a": 1, "b": 2},
        True,
        False,
        None,
        "test",
        1.0,
        1,
        datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
        Decimal("1.0"),
        UUID("069a6570-41d3-4efc-a3e3-afe4b4e9f7e4")
    ]:
        assert json.loads(json.dumps(test_object)) == json.loads(_ExtendedEncoder().encode(test_object))
    # Verify that an unimple

# Generated at 2022-06-13 19:11:25.258921
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    obj = _ExtendedEncoder()
    assert obj.default(datetime.now()) > 0



# Generated at 2022-06-13 19:11:58.016661
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    ExtendedEncoder = _ExtendedEncoder()
    assert ExtendedEncoder.default(
        datetime.fromtimestamp(1, tz=timezone.utc)) == 1
    assert ExtendedEncoder.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert ExtendedEncoder.default(Enum('MyEnum', 'v1')) == 'v1'
    assert ExtendedEncoder.default(Decimal('123.45')) == '123.45'



# Generated at 2022-06-13 19:12:05.878625
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Unittest for default
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) is not None
    assert _ExtendedEncoder().default(datetime.now()) is not None
    assert _ExtendedEncoder().default(UUID('5f1c5e5f-dee4-4e16-b4f2-4ef9e16d2d67')) == \
           '5f1c5e5f-dee4-4e16-b4f2-4ef9e16d2d67'
    assert _ExtendedEncoder().default([3, 2, 1]) == [3, 2, 1]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _Extended

# Generated at 2022-06-13 19:12:11.225163
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): # noqa
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2, 3]) == [1, 2, 3], 'json.JSONEncoder(list) should return a list'
    assert encoder.default({'foo': 1, 'bar': 2}) == {'foo': 1, 'bar': 2}, 'json.JSONEncoder(dict) should return a dict'
    assert encoder.default(datetime(2020, 1, 4, 11, 33, tzinfo=timezone.utc)) == 1578194380.0, 'json.JSONEncoder(datetime) should return a number'

# Generated at 2022-06-13 19:12:22.350320
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode({}) == "{}"
    assert encoder.encode([]) == "[]"
    assert encoder.encode(()) == "[]"
    assert encoder.encode({datetime.now(): [1, 2, 3]}) == '{"' + datetime.now().timestamp().__str__() + '": [1, 2, 3]}'
    assert encoder.encode([1, 2, 3, UUID('a9b39c65-d169-4b78-8b98-c7f28b26e1b7')]) == "[1, 2, 3, \"a9b39c65-d169-4b78-8b98-c7f28b26e1b7\"]"

# Generated at 2022-06-13 19:12:27.295440
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test with a simple collection
    a = [1, 2, 3]
    assert _ExtendedEncoder().default(a) == a

    # test with a simple mapping
    a = {'a': 2, 'b': 3}
    assert _ExtendedEncoder().default(a) == a



# Generated at 2022-06-13 19:12:35.721299
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(['foo', 'bar']) == ['foo', 'bar']
    assert _ExtendedEncoder().default(('foo', 'bar')) == ['foo', 'bar']
    assert _ExtendedEncoder().default({'foo': 'bar'}) == {'foo': 'bar'}
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default({'foo': 'bar'}.keys()) == ['foo']
    assert _ExtendedEncoder().default({'foo': 'bar'}.values()) == ['bar']
    assert _ExtendedEncoder().default({'foo': 'bar'}.items()) == [('foo', 'bar')]

# Generated at 2022-06-13 19:12:43.593901
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({'a': 1}) == {'a': 1}
    ts = datetime(2019, 7, 3, 12, 10, 10, tzinfo=timezone.utc)
    assert encoder.default(ts) == 1562092210.0
    uid = UUID('{12345678-abcd-efab-cdef-0123456789ab}')
    assert encoder.default(uid) == '12345678-abcd-efab-cdef-0123456789ab'
    enum_val = MyEnum(1)
    assert encoder.default(enum_val) == 1
   

# Generated at 2022-06-13 19:12:45.271459
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:12:51.005244
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, tzinfo=timezone.utc)) == "0.0"
    assert _ExtendedEncoder().encode(UUID('936DA01F9ABD4d9d80C702AF85C822A8')) == "'936da01f-9abd-4d9d-80c7-02af85c822a8'"

_JsonData = Union[Json, bytes, str]



# Generated at 2022-06-13 19:12:52.498433
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(1) == 1


# Generated at 2022-06-13 19:13:41.431660
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

    assert encoder.default(UUID('12341234-1234-1234-1234-123412341234')) == '12341234-1234-1234-1234-123412341234'
    assert encoder.default(datetime(2019, 1, 1, 0, 0, 0, 0, timezone.utc)) == 1546300800.0
    assert encoder.default(Decimal('1.1')) == '1.1'
    assert encoder.default(['a', 'b']) == ['a', 'b']
    assert encoder.default((1,2,3)) == [1,2,3]
    assert encoder.default((1,)) == [1]
    assert encoder.default([1]) == [1]

# Generated at 2022-06-13 19:13:46.626169
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default([1,2,3]) == [1,2,3]
    assert encoder.default({'a':1,'c':3}) == {'a':1,'c':3}
    assert encoder.default(datetime(2018,10,7,12,0,0,tzinfo=timezone.utc)) == 1538882400
    assert encoder.default(Decimal('10.1')) == '10.1'
# end



# Generated at 2022-06-13 19:13:53.040094
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode('test') == '"test"'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(1.1) == '1.1'
    assert _ExtendedEncoder().encode(datetime(2020, 1, 1, 12, tzinfo=timezone.utc)) == '1577797200.0'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:13:56.911186
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(dict()) == dict()
    assert encoder.default([]) == list()
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(UUID('{12345678-1234-5678-1234-567812345678}')) == str(UUID('{12345678-1234-5678-1234-567812345678}'))
    assert encoder.default(Decimal('123.45')) == '123.45'
    assert encoder.default(['test']) == ['test']



# Generated at 2022-06-13 19:14:01.477882
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import unittest
    import dataclasses
    import uuid
    import decimal
    import time

    class myenum(Enum):
        a = 1
        b = 2
        c = 3

    @dataclasses.dataclass
    class testclass:
        a: int
        b: str
        c: uuid.UUID
        d: decimal.Decimal
        e: datetime
        f: myenum
        g: Mapping
        h: Collection

    tc: testclass = dataclasses.replace(testclass(1, "2", uuid.uuid4(), 10, datetime.now(timezone.utc), myenum.a, {1: 2}, [1, 2, 3]))

    encoder: _ExtendedEncoder = _ExtendedEncoder()

# Generated at 2022-06-13 19:14:07.129635
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479')) == '"f47ac10b-58cc-4372-a567-0e02b2c3d479"'



# Generated at 2022-06-13 19:14:09.175097
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Test for constructor of class _ExtendedEncoder
    _ExtendedEncoder()



# Generated at 2022-06-13 19:14:19.272999
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(dict(a=1), cls=_ExtendedEncoder) == '{"a": 1}'
    assert json.dumps([1, 2, 3], cls=_ExtendedEncoder) == '[1, 2, 3]'
    assert json.dumps('str', cls=_ExtendedEncoder) == '"str"'
    assert json.dumps(1, cls=_ExtendedEncoder) == '1'
    assert json.dumps(1.0, cls=_ExtendedEncoder) == '1.0'
    assert json.dumps(True, cls=_ExtendedEncoder) == 'true'
    assert json.dumps(None, cls=_ExtendedEncoder) == 'null'

    class Test:
        pass
    test = Test()

# Generated at 2022-06-13 19:14:22.063820
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    assert isinstance(extended_encoder, json.JSONEncoder)


# Generated at 2022-06-13 19:14:24.192495
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(Decimal('3.14')) == '3.14'
    assert _ExtendedEncoder().default(timezone.utc) == 0.0



# Generated at 2022-06-13 19:16:12.907804
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(123) == 123
    assert _ExtendedEncoder().default('123') == '123'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(datetime.utcnow()) == datetime.utcnow().timestamp()
    assert _ExtendedEncoder().default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert _ExtendedEncoder().default(Decimal('12345')) == '12345'

# Generated at 2022-06-13 19:16:18.143598
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(True) == "true"
    assert _ExtendedEncoder().encode(None) == "null"
    assert _ExtendedEncoder().encode(123) == "123"
    assert _ExtendedEncoder().encode(123.4) == "123.4"
    assert _ExtendedEncoder().encode(UUID(int=0)) == "00000000-0000-0000-0000-000000000000"
    assert _ExtendedEncoder().encode(datetime.now()) == _ExtendedEncoder().encode(datetime.now().timestamp())
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == _ExtendedEncoder().encode(datetime.now(timezone.utc).timestamp())
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:16:28.020715
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(dict(a=1, b=2, c=3)) == {'a':1, 'b':2, 'c':3}
    assert _ExtendedEncoder().default(set([1,2,3])) == [1,2,3]
    from enum import Enum
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    assert _ExtendedEncoder().default(Color.GREEN) == 2
    import uuid
    assert _ExtendedEncoder().default(uuid.uuid4()) == print(uuid.uuid4())
    import datetime
    assert _ExtendedEncoder().default(datetime.datetime.now()) == print(datetime.datetime.now())



# Generated at 2022-06-13 19:16:34.834270
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == json.JSONEncoder().encode({})
    assert _ExtendedEncoder().encode([]) == json.JSONEncoder().encode([])
    assert _ExtendedEncoder().encode({'date': datetime.now()}) \
        == json.JSONEncoder().encode({'date': datetime.now()})
    assert _ExtendedEncoder().encode({'uuid': UUID('8fea4313-76e0-46f3-938b-074c1a80a4e4')}) \
        == json.JSONEncoder().encode({'uuid': UUID('8fea4313-76e0-46f3-938b-074c1a80a4e4')})
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:16:36.580269
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:16:38.527789
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().encode({datetime.now(): timezone.utc})



# Generated at 2022-06-13 19:16:46.547494
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) is not None
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) is not None
    assert _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000000')) is not None
    assert _ExtendedEncoder().default(cfg.enforce_string) is not None
    assert _ExtendedEncoder().default(cfg.enforce_string_strict) is not None
    assert _ExtendedEncoder().default(cfg.enforce_float) is not None
    assert _ExtendedEncoder().default([1, 2, 3]) is not None
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) is not None

# Generated at 2022-06-13 19:16:54.135290
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import json
    from uuid import uuid4, UUID
    from enum import Enum

    class MyEnum(Enum):
        field_1 = 0
        field_2 = 1

    u = uuid4()
    d = datetime.now()

    print(json.dumps({
        'set': {1, 2, 3},
        'frozenset': frozenset({1, 2, 3}),
        'myenum': MyEnum.field_1,
        'uuid': u,
        'datetime': d,
        'decimal': Decimal("0.126")
    }, cls=_ExtendedEncoder))



# Generated at 2022-06-13 19:17:05.365696
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert {'a': 'b'}.encode(_ExtendedEncoder) == b'{"a":"b"}'
    assert ['a', 1].encode(_ExtendedEncoder) == b'["a",1]'
    assert 'a'.encode(_ExtendedEncoder) == b'"a"'

# Generated at 2022-06-13 19:17:08.909839
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) > 0
    assert _ExtendedEncoder().default(datetime.utcnow()) > 0



# Generated at 2022-06-13 19:19:22.365374
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    dump = _ExtendedEncoder().encode
    assert dump(12) == json.dumps(12)
    assert dump([1, 2, 3]) == json.dumps([1, 2, 3])
    assert dump({"a": 1, "b": "b"}) == json.dumps({"a": 1, "b": "b"})
    assert dump(json.dumps({"a": 1, "b": "b"})) == json.dumps(json.dumps({"a": 1, "b": "b"}))
    assert dump({"a": [1, 2]}) == json.dumps({"a": [1, 2]})
    assert dump(datetime.now(timezone.utc)) == json.dumps(datetime.now(timezone.utc).timestamp())

# Generated at 2022-06-13 19:19:36.841871
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import unittest.mock
    assert _ExtendedEncoder().default(unittest.mock.sentinel.x) == unittest.mock.sentinel.x
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(0) == 0
    assert _ExtendedEncoder().default(0.0) == 0.0
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default("") == ""
    assert _ExtendedEncoder().default(b"\0") == b"\0"
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(()) == []
    assert _ExtendedEncoder().default({"a": "b"}) == {"a": "b"}