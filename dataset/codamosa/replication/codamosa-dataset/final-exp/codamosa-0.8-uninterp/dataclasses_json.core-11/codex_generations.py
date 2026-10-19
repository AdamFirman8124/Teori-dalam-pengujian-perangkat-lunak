

# Generated at 2022-06-13 19:09:59.008457
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"


# Generated at 2022-06-13 19:10:07.628414
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1]) == [1]
    assert _ExtendedEncoder().default({1:1}) == {1:1}
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default('foo') == 'foo'
    assert _ExtendedEncoder().default(1.11) == 1.11
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'



# Generated at 2022-06-13 19:10:12.961682
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from decimal import Decimal
    from uuid import UUID
    from dataclasses_json.utils import _make_dataclass_class

    _ExtendedEncoder().default(Decimal('1.1'))
    _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000001'))
    _ExtendedEncoder().default(_make_dataclass_class('A'))
    _ExtendedEncoder().default(datetime.now().astimezone(timezone.utc))



# Generated at 2022-06-13 19:10:19.482182
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default('foobar') == 'foobar'
    assert encoder.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(datetime(2020, 1, 1, 12, 34, 56)) == 1577839296.0
    assert encoder.default(datetime(2020, 1, 1, 12, 34, 56, tzinfo=timezone.utc)) == 1577839296.0

# Generated at 2022-06-13 19:10:27.636852
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(10) == 10
    assert e.default(True) is True
    assert e.default(10.0) == 10.0
    assert e.default('test') == 'test'
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default((1, 2, 3)) == [1, 2, 3]
    assert e.default({1: 2, 'key': 'value'}) == {'1': 2, 'key': 'value'}
    assert e.default(datetime(2010, 1, 1)) == 1262304000.0

# Generated at 2022-06-13 19:10:38.935584
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    def t(obj: Any, expect: Json):
        r = _ExtendedEncoder().encode(obj)
        print(f'{obj} -> {r}')
        assert r == json.dumps(expect, indent=4)

    t({}, {})
    t([], [])
    t((1, 2, 3), [1, 2, 3])
    t(datetime(2020, 5, 14, 23, 1, 59, 0, tzinfo=timezone.utc), 1589464919.0)
    t(UUID('{12345678-1234-5678-1234-567812345678}'),
      '12345678-1234-5678-1234-567812345678')
    t(Decimal('1.0'), '1.0')

# Generated at 2022-06-13 19:10:50.900425
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import unittest
    import json

    json_test = {'test': '123', 'test2': None, 'test3': True, 'test4': 123.123, 'test5': {'test': 'test', 'list': [1, 2, 3]}}
    class TestClass:
        pass

    class TestClass2:
        def __init__(self):
            self.field = 1

        def __repr__(self):
            return f'{self.__dict__!r}'

        def __eq__(self, other):
            if not isinstance(other, TestClass2):
                return False
            return self.__dict__ == other.__dict__


# Generated at 2022-06-13 19:10:53.438072
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = {
        'test': True
    }
    j = json.dumps(o, cls=_ExtendedEncoder)
    assert j == '{"test": true}'



# Generated at 2022-06-13 19:10:58.526897
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(datetime(2001, 1, 1, 1, 1, 1, 1, timezone.utc))
    json.dumps({})
    json.dumps([])
    json.dumps(UUID('00000000-0000-0000-0000-000000000000'))
    json.dumps(Decimal('3.14'))
    class Foo(Enum):
        FOO = 1
    json.dumps(Foo.FOO)
    class Bar:
        pass
    try:
        json.dumps(Bar())
    except TypeError:
        pass
    else:
        assert False, "Expecting TypeError for non-JSON serializable object"


# Generated at 2022-06-13 19:11:11.896125
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default({"key": "value"}) == {"key": "value"}
    assert encoder.default("string") == "string"
    assert encoder.default(10) == 10
    assert encoder.default(10.1) == 10.1
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None
    assert encoder.default([datetime(2019, 12, 31, 1, 2, 3)]) == [1577836323]
    assert encoder.default({"date": datetime(2019, 12, 31, 1, 2, 3)}) == {"date": 1577836323}

# Generated at 2022-06-13 19:11:36.870374
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    my_list = [1, 2, 3]
    my_dict = {"a": 1, "b": 2}
    my_datetime = datetime.now(timezone.utc)
    my_uuid = UUID("88045b39-1f72-40de-9c01-a1d54e3b3c08")
    my_enum = cfg.LetterCase.lowercase
    my_decimal = Decimal("1.11")
    my_any = True
    _ExtendedEncoder().default(my_list)
    _ExtendedEncoder().default(my_dict)
    _ExtendedEncoder().default(my_datetime)
    _ExtendedEncoder().default(my_uuid)
    _ExtendedEncoder().default(my_enum)
    _ExtendedEncoder().default

# Generated at 2022-06-13 19:11:42.441343
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test basic datatypes
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.1) == 1.1
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default('abc') == 'abc'
    assert _ExtendedEncoder().default((0, 1, 2)) == [0, 1, 2]
    assert _ExtendedEncoder().default({'a': 'b'}) == {'a': 'b'}
    assert _ExtendedEncoder().default(None) == None

    # test advanced datatypes
    assert _ExtendedEncoder().default(datetime(2020, 1, 1)) == 1577836800

# Generated at 2022-06-13 19:11:43.496028
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(Decimal('1')) == '1'

# Used to print a warning if the Field was not camelCase.

# Generated at 2022-06-13 19:11:46.375613
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().encode({1:1}) == '{"1": 1}'



# Generated at 2022-06-13 19:11:57.266728
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _ExtendedEncoder().default('a') == 'a'
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.0) == 1.0
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(None) == None

# Generated at 2022-06-13 19:12:05.331952
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    assert extended_encoder.default(MISSING) == MISSING
    assert extended_encoder.default({}) == {}
    assert extended_encoder.default([]) == []
    assert extended_encoder.default("") == ""
    assert extended_encoder.default(0) == 0
    assert extended_encoder.default(0.0) == 0.0
    assert extended_encoder.default(True) == True
    assert extended_encoder.default(False) == False
    assert extended_encoder.default(None) == None
    dt = datetime.now()
    assert extended_encoder.default(dt) == dt.timestamp()
    assert extended_encoder.default(uuid.uuid4()) == str(uuid.uuid4())


# Generated at 2022-06-13 19:12:05.783757
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    ...



# Generated at 2022-06-13 19:12:09.148660
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(Decimal('1.0')) == '1.0'
    assert _ExtendedEncoder().default(UUID('{123e4567-e89b-42d3-a456-556642440000}')) == '123e4567-e89b-42d3-a456-556642440000'
    assert _ExtendedEncoder().default([1,2]) == [1,2]



# Generated at 2022-06-13 19:12:16.511619
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'a': datetime(2000, 1, 1)}) == '{"a": 946684800.0}'
    assert _ExtendedEncoder().encode({'a': UUID(int=0)}) == '{"a": "00000000-0000-0000-0000-000000000000"}'
    assert _ExtendedEncoder().encode({'a': Decimal(1)}) == '{"a": "1"}'


# Generated at 2022-06-13 19:12:24.886087
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    u = UUID('1e99c43e-44f0-4411-9e64-9348f8d8b2c1')
    assert encoder.default(u) == '1e99c43e-44f0-4411-9e64-9348f8d8b2c1'
    assert encoder.default(None) == None
    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(1.0) == 1.0
    assert encoder.default(1) == 1
    assert encoder.default('a') == 'a'

# Generated at 2022-06-13 19:12:54.026393
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from dataclasses import dataclass

    @dataclass
    class Foo:
        i: int
        d: datetime

    f = Foo(i=1, d=datetime.now(timezone.utc))
    j = json.dumps(f, cls=_ExtendedEncoder)
    assert j == '{"i": 1, "d": ' + str(f.d.timestamp()) + '}'



# Generated at 2022-06-13 19:12:56.301698
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'selfie': {'me': 'myself'}}) == '{"selfie": {"me": "myself"}}'



# Generated at 2022-06-13 19:13:06.960311
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode('foo') == '"foo"'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(1.5) == '1.5'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode(frozenset()) == '[]'

    assert _ExtendedEncoder().encode({'foo': 'bar'}) == '{"foo": "bar"}'

# Generated at 2022-06-13 19:13:13.425641
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default("Hello") == "Hello"
    assert _ExtendedEncoder().default(dict(a=[])) == {"a": []}

    dt = datetime.now(timezone.utc)
    dt_json = _ExtendedEncoder().default(dt)
    dt2 = datetime.fromtimestamp(dt_json, timezone.utc)
    assert dt.isoformat() == dt2.isoformat()

    u = UUID('0d8b6a73-6edc-4b53-b9c9-71c1a7b00faa')
    assert _ExtendedEncoder().default(u) == str(u)

    Color

# Generated at 2022-06-13 19:13:15.228114
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) is not None


# Generated at 2022-06-13 19:13:21.433184
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == 1596687436.706935
    assert _ExtendedEncoder().default(UUID('{12345678-1234-5678-1234-567812345678}')) == '12345678-1234-5678-1234-567812345678'
    assert _ExtendedEncoder().default(Decimal('0.00000000000000000')) == '0'


# Generated at 2022-06-13 19:13:33.809111
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    if cfg.ENABLE_EXTENDED_ENCODERS:
        encoder = _ExtendedEncoder()
        result = encoder.encode(datetime.now(timezone.utc))
        assert(isinstance(result, str))
        result = encoder.encode(UUID('{12345678-1234-5678-1234-567812345678}'))
        assert(isinstance(result, str))
        result = encoder.encode(Decimal('1.1'))
        assert(isinstance(result, str))
        result = encoder.encode(cfg.MM_PAT)
        assert(isinstance(result, str))


# Generated at 2022-06-13 19:13:35.217916
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    res = _ExtendedEncoder().encode({'date': datetime.now(timezone.utc)})
    assert res is not None, res



# Generated at 2022-06-13 19:13:43.251745
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    class _ExtendedEncoder(json.JSONEncoder):
        def default(self, o) -> Json:
            result: Json
            if _isinstance_safe(o, Collection):
                if _isinstance_safe(o, Mapping):
                    result = dict(o)
                else:
                    result = list(o)
            elif _isinstance_safe(o, datetime):
                result = o.timestamp()
            elif _isinstance_safe(o, UUID):
                result = str(o)
            elif _isinstance_safe(o, Enum):
                result = o.value
            elif _isinstance_safe(o, Decimal):
                result = str(o)
            else:
                result = json.JSONEncoder.default(self, o)
            return result



# Generated at 2022-06-13 19:13:50.460505
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import date, datetime, timezone
    from datetime import time
    from enum import Enum
    from uuid import UUID
    import decimal
    import datetime
    ExtendedEncoder = _ExtendedEncoder()
    assert ExtendedEncoder.default(list) == list
    assert ExtendedEncoder.default(dict) == dict
    assert ExtendedEncoder.default(date.today()) == 1555574400
    assert ExtendedEncoder.default(datetime.now(timezone.utc)) == 1551357407.227574

# Generated at 2022-06-13 19:14:19.763877
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [True, False, None, 3.4, 3, 353535353535, 'asdad',
            [1, 2, 3, 4], {'a': 1, 'b': 2}, {1, 2, 3, 4},
            UUID('8d8c43dc-da7a-4c3d-8a88-c2156e7b22bc'),
            datetime(2020, 5, 1, 10, 0, 0, tzinfo=timezone.utc),
            Enum('TestEnum', [('A', 'a')]),
            Decimal('3.14')]
    encoder = json.JSONEncoder()
    ext_encoder = _ExtendedEncoder()
    for i in data:
        assert encoder.encode(i) == ext_encoder.encode(i)

# Generated at 2022-06-13 19:14:27.034291
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    x = _ExtendedEncoder().default({"a": "b"})
    assert isinstance(x, dict)
    assert x == {"a": "b"}
    x = _ExtendedEncoder().default({"a": "b"})
    assert isinstance(x, dict)
    assert x == {"a": "b"}
    x = _ExtendedEncoder().default({"a": "b"})
    assert isinstance(x, dict)
    assert x == {"a": "b"}
    x = _ExtendedEncoder().default(["a", "b"])
    assert isinstance(x, list)
    assert x == ["a", "b"]
    x = _ExtendedEncoder().default(["a", "b"])
    assert isinstance(x, list)
    assert x == ["a", "b"]

# Generated at 2022-06-13 19:14:37.273747
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(1) == 1
    assert encoder.default('A') == 'A'
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default({'a': 10}) == {'a': 10}
    assert encoder.default(datetime.fromtimestamp(123, tz=timezone.utc)) == 123
    assert encoder.default(UUID('3e81a8c0-1b13-11e9-a6e2-b442095969c9')) == '3e81a8c0-1b13-11e9-a6e2-b442095969c9'
    assert encoder.default(Enum()) == 0

# Generated at 2022-06-13 19:14:38.211519
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()


# Generated at 2022-06-13 19:14:49.144815
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode({3:2, 3:3}) == '{"3":3}'
    assert _ExtendedEncoder().encode([1,2,[3,4]]) == '[1,2,[3,4]]'
    assert _ExtendedEncoder().encode('foo bar') == '"foo bar"'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(1.1) == '1.1'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode([1,2,3,4]) == '[1,2,3,4]'
    assert _ExtendedEncoder().encode({})

# Generated at 2022-06-13 19:14:57.123000
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # Setup
    e = _ExtendedEncoder()
    # Exercise
    try:
        # Verify
        assert e.default([]) == []
        assert e.default({}) == {}
        assert e.default(datetime.utcnow()) == datetime.utcnow().timestamp()
        assert e.default(UUID(int=0)) == '00000000-0000-0000-0000-000000000000'
        assert e.default(Enum('MyEnum', 'a')) == 'a'
        assert e.default([1, Decimal(0), 'c', Decimal('3.14'), 4, 5]) == [1, '0', 'c' , '3.14', 4, 5]
    except Exception as ex:
        raise Exception("Exception caught in _ExtendedEncoder_default") from ex



# Generated at 2022-06-13 19:15:06.611135
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(MISSING) == 'null'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(1.1) == '1.1'
    assert _ExtendedEncoder().encode("test") == '"test"'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({"test": 123}) == '{"test": 123}'

# Generated at 2022-06-13 19:15:13.126504
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(UUID('1c18b555-151e-45f0-8f1d-c939fd9f3878')) == '1c18b555-151e-45f0-8f1d-c939fd9f3878'
    assert encoder.default(datetime(2019, 9, 1, 12, 0, 0)) == 1567439600.0
    assert encoder.default(datetime(2019, 9, 1, 12, 0, 0, tzinfo=timezone.utc)) == 1567439600.0
    assert encoder.default(datetime(2019, 9, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=4)))) == 1567439600.0

# Generated at 2022-06-13 19:15:25.211246
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default({1:2, 3:4}) == {1:2, 3:4}
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default(tuple([1, 2, 3])) == [1, 2, 3]
    assert e.default(datetime(2018, 12, 31, 23, 59, 59, 0, tzinfo=timezone.utc)) == 1546300799.0
    assert e.default(UUID('{123e4567-e89b-12d3-a456-426655440000}')) == '123e4567-e89b-12d3-a456-426655440000'

# Generated at 2022-06-13 19:15:28.081218
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import unittest

    from unittest.mock import MagicMock, patch

    _ExtendedEncoder(MagicMock())

    with patch('json.JSONEncoder') as mock:
        mock.default = MagicMock()
        obj = object()
        _ExtendedEncoder.default(None, obj)
        mock.default.assert_called_once_with(None, obj)



# Generated at 2022-06-13 19:16:29.255189
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    # str
    assert encoder.default("abc") == "abc"
    # int
    assert encoder.default(1) == 1
    # float
    assert encoder.default(1.1) == 1.1
    # bool
    assert encoder.default(True) == True
    # None
    assert encoder.default(None) == None
    # datetime.datetime
    from datetime import datetime
    dt = datetime.fromisoformat("1970-01-01T00:00:00+00:00")
    assert encoder.default(dt) == 0.0
    # datetime.date
    from datetime import date
    dt = date(1970, 1, 1)
    assert encoder.default(dt) == "1970-01-01"

# Generated at 2022-06-13 19:16:35.592390
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    e = _ExtendedEncoder()
    assert e.default(None) is None
    assert e.default(True)
    assert e.default(False) == False
    assert e.default(1) == 1
    assert e.default(1.0) == 1.0
    assert e.default(1 + 5j) == (1, 5)
    assert e.default('abc') == 'abc'
    assert e.default(bytearray(b'abc')) == 'YWJj'
    assert e.default({'a': 'b', 'c': 1}) == {'a': 'b', 'c': 1}
    assert e.default(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert e.default(datetime(2020, 1, 1)) == 1577836

# Generated at 2022-06-13 19:16:38.672191
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # This is a very sofisticated unit test because it instantiates the class.
    # noinspection PyUnusedLocal
    extended_encoder = _ExtendedEncoder()


# Generated at 2022-06-13 19:16:46.629981
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder(sort_keys=True)  # type: ignore
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default({"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert e.default(True) == True
    assert e.default(False) == False
    assert e.default(None) is None
    assert str(e.default(UUID("a8098c1a-f86e-11da-bd1a-00112444be1e"))) == \
           '"a8098c1a-f86e-11da-bd1a-00112444be1e"'
    assert e.default(datetime.now(timezone.utc)) > 0



# Generated at 2022-06-13 19:16:52.317587
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoded = _ExtendedEncoder().encode({"a": [1, 1], "b": True})
    decoded = json.loads(encoded, cls=json.JSONDecoder)
    assert decoded["a"] == [1, 1]
    assert decoded["b"] == True



# Generated at 2022-06-13 19:16:54.153158
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.utcnow())

# Generated at 2022-06-13 19:16:57.446075
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder()
    result = ee.default(datetime.now())
    assert isinstance(result, float)


# Generated at 2022-06-13 19:17:04.117831
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    '''
    Ensure that _ExtendedEncoder.default() works correctly.
    '''
    # testing collections
    obj = [1, 2, 3]
    encoder = _ExtendedEncoder()
    assert encoder.default(obj) == obj

    obj = {'a': 1, 'b': 2, 'c': 3}
    assert encoder.default(obj) == obj

    # testing datetime.datetime
    obj = datetime(2020, 10, 10, tzinfo=timezone.utc)
    assert encoder.default(obj) == obj.timestamp()

    # testing uuid.UUID
    obj = UUID('36497985-0c1a-471f-bcf0-b7f96350a353')

# Generated at 2022-06-13 19:17:16.536730
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, tzinfo=timezone.utc)) == '0'
    assert _ExtendedEncoder().encode({1: 2}) == '{"1": 2}'
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode('a') == '"a"'
    assert _ExtendedEncoder().encode(UUID('1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed')) == '"1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"'
    assert _Ext

# Generated at 2022-06-13 19:17:17.842888
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(1)



# Generated at 2022-06-13 19:19:35.601742
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    inst0 = _ExtendedEncoder()
    assert isinstance(inst0, json.JSONEncoder)

    inst1 = _ExtendedEncoder()
    assert inst1.default([]) == []
    assert inst1.default({}) == {}
    assert inst1.default('') == ''
    assert inst1.default(0.0) == 0.0
    assert inst1.default(1) == 1
    assert inst1.default(True) is True
    assert inst1.default(None) is None
    assert inst1.default(()) == ()
    assert inst1.default(set()) == set()
    assert inst1.default(frozenset()) == frozenset()
    
    dt1 = datetime.now(timezone.utc)