

# Generated at 2022-06-13 19:10:07.311240
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode([1,2]) == '[1, 2]'
    assert _ExtendedEncoder().encode(set([1,2])) == '[1, 2]'
    assert _ExtendedEncoder().encode(datetime(2019, 11, 26, 10, 10, 10)) == '1574789010.0'

# Generated at 2022-06-13 19:10:11.950814
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now(tz=timezone.utc))
    assert encoder.default(UUID('d4d4c7c4-a0a4-4bbb-8a1c-a65432ecc0bb'))
    assert encoder.default(Enum('Enum', [('value', 0)]))
    assert encoder.default(Decimal('1.0'))



# Generated at 2022-06-13 19:10:14.967436
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    o = Enum('SimpleEnum', (('Value1', 1), ('Value2', 2)))
    runner = _ExtendedEncoder()
    result = runner.default(o)
    assert result == 1

# Generated at 2022-06-13 19:10:21.561519
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    e = _ExtendedEncoder(sort_keys=True)
    assert e.default([1]) == [1]
    assert e.default(dict(a=1)) == {'a': 1}
    assert e.default(datetime.now(timezone.utc)) == 0
    assert e.default(UUID(int=1)) == '00000000-0000-0000-0000-000000000001'
    assert e.default(FooVar(1)) == {'value': 1}



# Generated at 2022-06-13 19:10:29.529406
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict()) == '{}'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(datetime(2016, 1, 1)) == '1451624400.0'

# Generated at 2022-06-13 19:10:37.549708
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [
        {'a': 1, 'b': 2},
        datetime(2019, 2, 19, tzinfo=timezone.utc),
        UUID('123e4567-e89b-12d3-a456-426655440000'),
        Decimal('1.2'),
        Enum('MyEnum', ['a', 'b', 'c'])('a')
    ]

    res = json.dumps(data, cls=_ExtendedEncoder)
    # print(res)



# Generated at 2022-06-13 19:10:40.120775
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(bytearray(b'\xe2\x98\x83')) == '☃'


# Generated at 2022-06-13 19:10:51.571705
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970,1,1,0,0,0, tzinfo=timezone.utc)) == '0.0'
    assert _ExtendedEncoder().encode(datetime(1970,1,1,0,0,0)) == '0.0'
    assert _ExtendedEncoder().encode(datetime(1970,1,1,0,0,1)) == '1.0'
    assert _ExtendedEncoder().encode(datetime(1970,1,1,0,0,1)) == '1.0'
    assert _ExtendedEncoder().encode(datetime(1970,1,1,0,0,1,tzinfo=timezone.utc)) == '1.0'

# Generated at 2022-06-13 19:10:52.691434
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    enc = _ExtendedEncoder()
    assert enc.default(Decimal('1.1')) == '1.1'



# Generated at 2022-06-13 19:10:58.833669
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2]) == "[1, 2]"
    assert _ExtendedEncoder().encode((1, 2)) == "[1, 2]"
    assert _ExtendedEncoder().encode({"1": "1", "2": "2"}) == '{"1": "1", "2": "2"}'
    assert _ExtendedEncoder().encode({"1", "2"}) == '["2", "1"]'
    assert _ExtendedEncoder().encode(1) == "1"
    assert _ExtendedEncoder().encode("1") == '"1"'
    assert _ExtendedEncoder().encode({"1"}) == '["1"]'
    assert _ExtendedEncoder().encode(None) == "null"
    assert _ExtendedEncoder().encode

# Generated at 2022-06-13 19:11:21.753053
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_string = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}],
                             cls=_ExtendedEncoder)
    assert json_string == '["foo", {"bar": ["baz", null, 1.0, 2]}]'



# Generated at 2022-06-13 19:11:32.154220
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode(['a']) == '["a"]'
    assert _ExtendedEncoder().encode((1,)) == '[1]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({1, 2, 3}) == '[1, 2, 3]'

# Generated at 2022-06-13 19:11:46.883193
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    class C1:
        pass
    c1 = C1()
    c1.a = 'A'
    c1.b = 'B'
    c1.c = 'C'
    assert _ExtendedEncoder().encode(c1) == '{"a": "A", "b": "B", "c": "C"}'


    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({3:'a', 4:'b', 5:'c'}) == '{"3": "a", "4": "b", "5": "c"}'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:11:57.468526
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    enc = _ExtendedEncoder()
    assert enc.default(5) == 5
    assert enc.default('a') == 'a'
    assert enc.default(5.23) == 5.23
    assert enc.default(True) is True
    assert enc.default(None) is None

    assert enc.default([1, 2, 3]) == [1, 2, 3]
    assert enc.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    dt = datetime.now(timezone.utc)
    assert enc.default(dt) == dt.timestamp()

    u = UUID('f2120978-cd97-43db-8f48-afc388d57b13')
    assert enc.default(u) == str(u)


# Generated at 2022-06-13 19:12:05.422001
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(({}, )) == [{}]
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default(True) is True
    assert _ExtendedEncoder().default(False) is False
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.1) == 1.1
    assert _ExtendedEncoder().default(1 + 2j) == {'__complex__': True, 'real': 1, 'imag': 2}
    assert _ExtendedEncoder().default(frozenset((1, 2, 3))) == [1, 2, 3]

# Generated at 2022-06-13 19:12:11.725902
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3, (1, 2)]) == '[1, 2, 3, [1, 2]]'
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({1: 2, 3: 4}) == '{"1": 2, "3": 4}'
    assert _ExtendedEncoder().encode(UUID(int=1)) == '1'
    assert _ExtendedEncoder().encode(datetime(2019, 5, 1, tzinfo=timezone.utc)) == '1556754400.0'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:12:14.219957
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder is not None


# Generated at 2022-06-13 19:12:22.978427
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'foo': b'bar'}) == '{"foo": "bar"}'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(datetime.utcnow()) == '0.0'
    assert _ExtendedEncoder().encode(UUID('{12345678-1234-5678-1234-567812345678}')) == '"12345678-1234-5678-1234-567812345678"'
    assert _ExtendedEncoder().encode(Decimal('1.1')) == '"1.1"'



# Generated at 2022-06-13 19:12:28.421492
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import unittest.mock
    json_encoder = unittest.mock.Mock(json.JSONEncoder)
    extended_encoder = _ExtendedEncoder(json_encoder)
    assert extended_encoder._instance_caches == dict()
    assert extended_encoder.json_encoder == json_encoder



# Generated at 2022-06-13 19:12:36.612476
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    print(json.dumps(list(range(3)), cls=_ExtendedEncoder))
    print(json.dumps(dict(a=1, b=2), cls=_ExtendedEncoder))
    print(json.dumps(datetime(2020,1,1, tzinfo=timezone.utc), cls=_ExtendedEncoder))
    print(json.dumps(datetime(2020,1,1), cls=_ExtendedEncoder))
    print(json.dumps(UUID('12345678123456781234567812345678'), cls=_ExtendedEncoder))
    print(json.dumps(Enum('a', 1), cls=_ExtendedEncoder))
    print(json.dumps(Decimal(1), cls=_ExtendedEncoder))
   

# Generated at 2022-06-13 19:12:55.921084
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(123) == json.dumps(123)


# Generated at 2022-06-13 19:13:03.426810
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(_ExtendedEncoder().encode(['abc', 'def']))

#####
# The following code is used to convert from Python type definition to JSON schema definition.
# Reference: https://python-jsonschema.readthedocs.io/en/stable/index.html
#
# It is not used in the rest of the code.
# It is only used to generate the schema for a class.
#
# It is still Experimental.
# It is not yet used.
# It is not yet finished.
#####



# Generated at 2022-06-13 19:13:06.948365
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(datetime.now())
    _ExtendedEncoder().default(UUID('c39bcbe1-25c7-4d9f-8b1e-4b4f7da538cb'))


# Generated at 2022-06-13 19:13:07.478101
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    pass



# Generated at 2022-06-13 19:13:13.697797
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    result = _ExtendedEncoder().default(None)
    assert result == None

    result = _ExtendedEncoder().default(1)
    assert result == 1

    result = _ExtendedEncoder().default(1.0)
    assert result == 1.0

    result = _ExtendedEncoder().default('text')
    assert result == 'text'

    result = _ExtendedEncoder().default(True)
    assert result == True

    result = _ExtendedEncoder().default([1, 2, 3])
    assert result == [1, 2, 3]

    result = _ExtendedEncoder().default(('1', '2', '3'))
    assert result == ['1', '2', '3']

    result = _ExtendedEncoder().default({1, 2, 3})

# Generated at 2022-06-13 19:13:20.659089
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp()
    assert encoder.default(UUID('5e5b9dcf-5a21-4a5d-b2b4-466b2a846b4d')) == '5e5b9dcf-5a21-4a5d-b2b4-466b2a846b4d'
    assert encoder.default(Decimal('1234.5678')) == '1234.5678'



# Generated at 2022-06-13 19:13:21.866082
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():  # type: ignore
    class Foo(object):
        pass
    _ExtendedEncoder().default(Foo())



# Generated at 2022-06-13 19:13:34.076458
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default('abc') == 'abc'
    assert encoder.default(123) == 123
    assert encoder.default(123.45) == 123.45
    assert encoder.default(None) == None
    assert encoder.default(datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc)) == 1577836800.0
    assert encoder.default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    t = namedtuple('t', 'x, y')

# Generated at 2022-06-13 19:13:44.549395
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extendedEncoder = _ExtendedEncoder()
    actual_result = extendedEncoder.default(None)
    assert actual_result == None


# Generated at 2022-06-13 19:13:52.605677
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ = _ExtendedEncoder()
    assert _.default(datetime.now(tz=timezone.utc)) > 0.1
    assert _.default(1) == 1
    assert _.default('a') == 'a'
    assert _.default(True) is True
    assert _.default(False) is False
    assert _.default(None) is None
    assert _.default(Decimal('0.5')) == '0.5'
    assert _.default(UUID('123e4567-e89b-12d3-a456-426655440000')) == '123e4567-e89b-12d3-a456-426655440000'



# Generated at 2022-06-13 19:14:18.348302
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    x = _ExtendedEncoder()
    assert x.encode(dict(a=1)) == '{"a":1}'


_default_encoder = _ExtendedEncoder().encode
_default_decoder = json.JSONDecoder().decode


# Generated at 2022-06-13 19:14:26.435800
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(UUID('9836e2b7-a6c2-4e61-97a1-52dff67079e0')) == str(UUID('9836e2b7-a6c2-4e61-97a1-52dff67079e0'))
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()
    assert _ExtendedEncoder().default(list()) == list()
    assert _ExtendedEncoder().default(range(10)) == list(range(10))
    assert _ExtendedEncoder().default(NGram(4, 'ciao')) == ('ciao', 4)
    assert _ExtendedEncoder().default({'ciao': 4}) == {'ciao': 4}
    assert _Extended

# Generated at 2022-06-13 19:14:36.525161
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import pytest
    from json import dumps
    from uuid import uuid4
    from decimal import Decimal as decimal
    from enum import Enum as enum
    from dataclasses import dataclass

    @dataclass
    class User:
        id: int
        name: str
        email: str
        friends: list
        payments: dict

    @dataclass
    class Address:
        city: str
        state: str

    @dataclass
    class Lead:
        address: Address = None

    class UserType(enum):
        admin = 1
        guest = 2

    @dataclass
    class NewUser:
        id: UUID
        type: UserType
        amount: decimal


# Generated at 2022-06-13 19:14:37.576912
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'



# Generated at 2022-06-13 19:14:48.577810
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder(indent=2).encode({
        list(range(5)): [1, {2: 3}],
        dict(zip(range(10), range(10))): [1, {2: 3}]
    }) == '''{
  "[0, 1, 2, 3, 4]": [
    1,
    {
      "2": 3
    }
  ],
  "{\'0\': 0, \'1\': 1, \'2\': 2, \'3\': 3, \'4\': 4, \'5\': 5, \'6\': 6, \'7\': 7, \'8\': 8, \'9\': 9}": [
    1,
    {
      "2": 3
    }
  ]
}'''

    assert _ExtendedEncoder().encode

# Generated at 2022-06-13 19:14:52.591855
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode(frozenset()) == '[]'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == '0'



# Generated at 2022-06-13 19:14:54.530662
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(2019, 1, 1, tzinfo=timezone.utc)) == '1546300800.0'


# Generated at 2022-06-13 19:14:56.758618
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) \
        == datetime.now(timezone.utc).timestamp()


# noinspection PyAbstractClass

# Generated at 2022-06-13 19:15:06.400150
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Basic Python data types
    assert json.dumps({'a': 'A'}, cls=_ExtendedEncoder) == '{"a": "A"}'
    assert json.dumps([1, '2'], cls=_ExtendedEncoder) == '[1, "2"]'
    assert json.dumps(3) == '3'
    assert json.dumps('4', cls=_ExtendedEncoder) == '"4"'
    assert json.dumps(True, cls=_ExtendedEncoder) == 'true'
    assert json.dumps(None, cls=_ExtendedEncoder) == 'null'
    # Common Python data types

# Generated at 2022-06-13 19:15:12.981604
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(2017, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == '"2017-01-01T00:00:00+00:00"'
    assert _ExtendedEncoder().encode(datetime(2017, 1, 1, 12, 0, 0, tzinfo=timezone.utc)) == '"2017-01-01T12:00:00+00:00"'
    assert _ExtendedEncoder().encode(datetime(2017, 1, 1, 12, 0, 0, 123, tzinfo=timezone.utc)) == '"2017-01-01T12:00:00.123000+00:00"'

# Generated at 2022-06-13 19:16:15.112861
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'1': '2', '3': '4'}) == {'1': '2', '3': '4'}
    assert encoder.default(datetime.now()) == time.time()
    assert encoder.default(UUID('3fa85f64-5717-4562-b3fc-2c963f66afa6')) == '3fa85f64-5717-4562-b3fc-2c963f66afa6'
    assert encoder.default(Decimal(1.5)) == '1.5'
    assert encoder.default(5) == 5
    assert encoder.default('x') == 'x'
   

# Generated at 2022-06-13 19:16:27.038242
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import date
    from enum import IntEnum
    from uuid import UUID
    from decimal import Decimal

    from _pytest.monkeypatch import MonkeyPatch

    def check(obj, expected):
        mp = MonkeyPatch()
        tmp = json.JSONEncoder.default
        mp.setattr(json.JSONEncoder, 'default', lambda x, y: tmp(y))
        if _isinstance_safe(obj, Enum):
            obj = copy.deepcopy(obj)
        result = json.dumps(obj, cls=_ExtendedEncoder)
        mp.undo()
        assert result == expected

    check(date(2019, 4, 16), '"2019-04-16"')

    class EnumTest(IntEnum):
        a = 1
        b = 2


# Generated at 2022-06-13 19:16:33.245996
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, tzinfo=timezone.utc)) == '0.0'
    assert _ExtendedEncoder().encode(UUID('31337000-f000-f000-f000-133713371337')) == '"31337000-f000-f000-f000-133713371337"'
    assert _ExtendedEncoder().encode(Enum('Enum', [('VALUE', 1)])) == '1'
    assert _ExtendedEncoder().encode(Decimal('123.123')) == '"123.123"'



# Generated at 2022-06-13 19:16:43.964548
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    json_encoder = _ExtendedEncoder()
    assert [1, 2, 3] == json_encoder.default([1, 2, 3])
    assert {'a': 1, 'b': 2} == json_encoder.default({'a': 1, 'b': 2})
    assert {'a': [1, 2], 'b': [3, 4]} == json_encoder.default({'a': [1, 2], 'b': [3, 4]})
    dt = datetime(1970, 1, 1, 0, 0, tzinfo=timezone.utc)
    assert 0 == json_encoder.default(dt)
    dt = datetime(1970, 1, 1, 10, 10, tzinfo=timezone.utc)
    assert 36600 == json_encoder.default(dt)


# Generated at 2022-06-13 19:16:47.997396
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps([1, 2, 3], cls=_ExtendedEncoder)
    json.dumps({'a': 1}, cls=_ExtendedEncoder)
    json.dumps(datetime.now(), cls=_ExtendedEncoder)
    json.dumps(UUID('12345678123456781234567812345678'), cls=_ExtendedEncoder)
    json.dumps(Decimal('12.3'), cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:16:48.918636
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    pass



# Generated at 2022-06-13 19:17:01.988947
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
   # Test for empty mapping
   assert _ExtendedEncoder().default({}) == {}
   # Test for empty sequence
   assert _ExtendedEncoder().default([]) == []
   # Test for empty Set
   assert _ExtendedEncoder().default(set({})) == []
   # Test for empty sequence
   assert _ExtendedEncoder().default(()) == []
   # Test for empty FrozenSet
   assert _ExtendedEncoder().default(frozenset({})) == []
   # Test for empty mappin
   assert _ExtendedEncoder().default(frozenset({})) == []
   # Test for empty mapping
   assert _ExtendedEncoder().default(dict()) == {}
   # Test for empty mapping
   assert _ExtendedEncoder().default(dict()) == {}
   # Test for empty mapping
   assert _Ext

# Generated at 2022-06-13 19:17:04.184868
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:17:16.591231
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test if _ExtendedEncoder works as expected
    assert json.dumps(1, cls=_ExtendedEncoder) == "1"
    assert json.dumps(1.1, cls=_ExtendedEncoder) == "1.1"
    assert json.dumps(True, cls=_ExtendedEncoder) == "true"
    assert json.dumps(None, cls=_ExtendedEncoder) == "null"
    assert json.dumps("a", cls=_ExtendedEncoder) == "\"a\""
    assert json.dumps(b"a", cls=_ExtendedEncoder) == "\"a\""
    assert json.dumps([1, "a"], cls=_ExtendedEncoder) == "[1, \"a\"]"

# Generated at 2022-06-13 19:17:26.942211
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()
    o = {'a': 1, 'b': 'two', 'c': [1, 2, 3.0]}
    assert o == enc.default(o)
    o = [1, 2, 3]
    assert o == enc.default(o)
    o = (1, 2, 3)
    assert list(o) == enc.default(o)
    o = set([1, 2, 3])
    assert list(o) == enc.default(o)
    o = frozenset([1, 2, 3])
    assert list(o) == enc.default(o)



# Generated at 2022-06-13 19:19:41.422779
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1,2,3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2, 'c': 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert _ExtendedEncoder().encode('string') == '"string"'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(Decimal(0.1)) == '"0.1000000000000000055511151231257827021181583404541015625"'
    assert _ExtendedEncoder().encode(datetime.now()) == f"{datetime.now().timestamp()}"