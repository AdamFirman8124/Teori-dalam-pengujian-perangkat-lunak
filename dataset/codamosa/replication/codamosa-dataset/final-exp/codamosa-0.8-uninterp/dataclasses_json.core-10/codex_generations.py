

# Generated at 2022-06-13 19:10:06.168516
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    def assertEqual(o, expected):
        assert _ExtendedEncoder().default(o) == expected

    assertEqual([1, 2, 3], [1, 2, 3])
    assertEqual({1: 1}, {1: 1})
    assertEqual(set([1]), [1])

    d = datetime.now(tz=timezone.utc)
    assertEqual(d, d.timestamp())

    u = UUID('5d5a5c6d-9e85-48f1-8f8d-6d249df50bca')
    assertEqual(u, str(u))

    assertEqual(DummyEnum.v1, DummyEnum.v1.value)
    assertEqual(Decimal('1.2'), '1.2')


# Generated at 2022-06-13 19:10:17.481276
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default({1: 1}) == {1: 1}
    assert encoder.default(datetime(2020, 6, 27, tzinfo=timezone.utc)) == 1593250400.0
    assert encoder.default(UUID("73b2e1ff-9b46-4d92-99c0-f3b6bb50ee6d")) == "73b2e1ff-9b46-4d92-99c0-f3b6bb50ee6d"
    assert encoder.default(Decimal("1.0")) == "1.0"


# Generated at 2022-06-13 19:10:26.229373
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.encode((1, 2, 3)) == '[1, 2, 3]'
    assert e.encode({'a': 1, 'b': 2, 'c': 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert e.encode(datetime(2020, 10, 10, 14, 0).replace(tzinfo=timezone.utc)) == '1602305200.0'

# Generated at 2022-06-13 19:10:38.291111
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) is None
    assert encoder.default(True) is True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default('str') == 'str'
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}
    assert encoder.default(set([1, 2])) == [1, 2]
    assert encoder.default(frozenset([1, 2])) == [1, 2]
    assert encoder.default(MyEnum.A) == 1
    assert encoder.default(MyEnumWithValue.A) == 'a'

# Generated at 2022-06-13 19:10:50.092757
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:10:54.916069
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(UUID('6837ac00-b7f8-4d32-a951-0fdc14e7a9a1')) == "6837ac00-b7f8-4d32-a951-0fdc14e7a9a1"
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == 1516368542.912971


# Generated at 2022-06-13 19:11:09.347465
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode({'a': [1, 2, 3]}) == '{"a": [1, 2, 3]}'
    dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    assert json.loads(_ExtendedEncoder().encode(dt)) == dt.timestamp()
    assert json.loads(_ExtendedEncoder().encode(Decimal('1.1'))) == '1.1'
    try:
        json.loads(_ExtendedEncoder().encode(None))
        assert False
    except TypeError:
        pass



# Generated at 2022-06-13 19:11:11.212155
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps([1, 2, 3], cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:11:17.511747
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(tuple([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(dict({1: 2, 2: 3})) == {1: 2, 2: 3}
    assert encoder.default(datetime.now(timezone.utc))
    assert encoder.default(UUID('dbea0948-7c1b-4ec6-9b9d-cdd6e723e89b')) == 'dbea0948-7c1b-4ec6-9b9d-cdd6e723e89b'
    assert encoder.default(Decimal('1.1'))

# Generated at 2022-06-13 19:11:22.639014
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    from struct import Struct

    pair = Struct('!d')

    assert encoder.default(pair) == {'format': '!d', 'size': 8}

    assert encoder.default(Struct('> if')) == {'format': '> if', 'size': 12}

    assert encoder.default(list(pair)) == [8, '!d']

    assert encoder.default(list(Struct('> if'))) == [12, '> if']



# Generated at 2022-06-13 19:12:06.113908
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()

    assert enc.default(list()) == []
    assert enc.default(tuple()) == []
    assert enc.default(dict()) == {}
    assert enc.default({1: '1', 2: '2'}) == {1: '1', 2: '2'}
    assert enc.default(set([1, 2, 3])) == [1, 2, 3]
    assert enc.default(frozenset([1, 2, 3])) == [1, 2, 3]

    assert (enc.default(datetime.now(timezone.utc)) -
            datetime.now(timezone.utc).timestamp() <= 1)



# Generated at 2022-06-13 19:12:11.382851
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from random import Random
    from datetime import datetime, timedelta
    
    from dataclasses_json.utils import _issubclass_safe
    
    
    
    def test(value):
        return json.loads(json.dumps(value, cls=_ExtendedEncoder))

    # Iterables
    assert test(('a', 'b', 'c')) == ['a', 'b', 'c']
    assert test(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert test({'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}
    
    # datetime objects
    now = datetime.now(timezone.utc)

    assert test(now) == now.timestamp()

# Generated at 2022-06-13 19:12:22.448600
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default([None]) == [None]
    assert _ExtendedEncoder().default([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert _ExtendedEncoder().default([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert _ExtendedEncoder().default({"test": None}) == {"test": None}
    assert _ExtendedEncoder().default({"test": 1}) == {"test": 1}
    assert _ExtendedEncoder().default({"test": [1, 2]}) == {"test": [1, 2]}

# Generated at 2022-06-13 19:12:33.070609
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from datetime import date
    from decimal import Decimal
    from enum import Enum
    from uuid import uuid4
    from unittest.mock import ANY, patch
    from .dataclasses_ import (B, A, AnEnum, AnIntEnum, AnStrEnum,
                               AList, AMap, AnIntList, AnIntTuple)
    # pylint: disable=no-member, protected-access
    with patch.object(json.JSONEncoder, 'default') as default:
        encoder = _ExtendedEncoder()
    args = dict(o=ANY)
    encoder._ExtendedEncoder__check_circular = False
    with patch.object(json.JSONEncoder, 'default') as default:
        encoder.default(AnEnum.enum1)
    default.assert_

# Generated at 2022-06-13 19:12:42.476967
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1, 2, 3}) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({1:123, 2:234}) == '{"1": 123, "2": 234}'
    assert _ExtendedEncoder().encode(datetime(2019, 12, 25, 12, 12, 12, 0, timezone.utc)) == "1577353932.0"
    assert _ExtendedEncoder().encode(UUID('1e8d5b33-1b7f-4337-a383-3baf5f5fe5e5')) == '"1e8d5b33-1b7f-4337-a383-3baf5f5fe5e5"'

# Generated at 2022-06-13 19:12:50.003898
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) is None
    assert encoder.default(1) == 1
    assert encoder.default('a') == 'a'
    assert encoder.default(1.1) == 1.1
    assert encoder.default(True) == True
    assert encoder.default(['a']) == ['a']
    assert encoder.default({'a': 1}) == {'a': 1}
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(Enum)



# Generated at 2022-06-13 19:12:57.558849
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Allow to test class _ExtendedEncoder
    assert _ExtendedEncoder().encode({"a": datetime.now()})
    assert _ExtendedEncoder().encode({"a": Decimal(100.0)})
    assert _ExtendedEncoder().encode({"a": UUID('345b96f6-b4d4-4f8d-8b1c-a94dc1362d9c')})
    assert _ExtendedEncoder().encode({"a": set([1, 2, 3])})
    assert _ExtendedEncoder().encode({"a": NamedTuple('b', 'c')})
    assert _ExtendedEncoder().encode({"a": NamedTuple('b', 'c')})


# Generated at 2022-06-13 19:13:06.179048
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime(1970, 1, 1, tzinfo=timezone.utc)) == 0.0
    assert _ExtendedEncoder().default(UUID('212c2f2d-25d0-4ed7-b34a-e9ba5d5f60c5')) == '212c2f2d-25d0-4ed7-b34a-e9ba5d5f60c5'
    assert _ExtendedEncoder().default(Decimal('3.1415926')) == '3.1415926'

# noinspection PyProtectedMember

# Generated at 2022-06-13 19:13:12.791854
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([]) == "[]"
    assert _ExtendedEncoder().encode({}) == "{}"
    assert _ExtendedEncoder().encode(datetime.fromtimestamp(0, tz=timezone.utc)) == "0"
    assert _ExtendedEncoder().encode(UUID('{00112233-4455-6677-8899-aabbccddeeff}')) == "00112233-4455-6677-8899-aabbccddeeff"
    assert _ExtendedEncoder().encode(Decimal('1.0')) == '1.0'
    try:
        assert _ExtendedEncoder().encode(object()) == '{}'
        assert False
    except:
        pass



# Generated at 2022-06-13 19:13:15.804335
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    '''
    Test the constructor of class _ExtendedEncoder
    '''
    json = _ExtendedEncoder()
    assert is_dataclass(json) == True


# Generated at 2022-06-13 19:13:38.043134
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps({'t': [set(), 1, 2, 3]},
               cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:13:42.818412
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    xe = _ExtendedEncoder()
    assert xe.default([1,2,3]) == [1,2,3]
    assert xe.default({"a":1}) == {"a":1}
    assert xe.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert xe.default(1) == 1



# Generated at 2022-06-13 19:13:46.121456
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(UUID('6d77bb6c-9c2b-4fd1-8ad0-83a614ac6182')) == '"6d77bb6c-9c2b-4fd1-8ad0-83a614ac6182"'



# Generated at 2022-06-13 19:13:48.727943
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = json.dumps({'now': datetime.now()}, cls=_ExtendedEncoder)
    assert isinstance(result, str)
    assert '"now":' in result
    assert '.' in result
    assert result[-2:] == '}'



# Generated at 2022-06-13 19:13:55.690960
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder()
    assert json_encoder.default(defaultdict(int, {1: 2})) == {1: 2}
    assert json_encoder.default((1,)) == [1]
    assert json_encoder.default(datetime(2021, 1, 1, tzinfo=timezone.utc)) == 1609459200.0
    assert json_encoder.default(UUID('723a0a49-e7d4-4c4d-ac91-b1c5a918b591')) == '723a0a49-e7d4-4c4d-ac91-b1c5a918b591'
    assert json_encoder.default(Decimal('12.3456')) == '12.3456'



# Generated at 2022-06-13 19:14:04.757064
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) is not None
    assert _ExtendedEncoder().default(UUID('a28e4b42-4a4f-49e4-9084-f88e8b8d7891')) is not None
    assert _ExtendedEncoder().default(Decimal(10.99)) is not None
    assert _ExtendedEncoder().default(Decimal(0.8)) is not None


# Generated at 2022-06-13 19:14:08.660289
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder().encode([{'a': 1, 'b': 2}, (3, 4, 5)])
    assert ee == '[{"a": 1, "b": 2}, [3, 4, 5]]'



# Generated at 2022-06-13 19:14:18.919093
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, {'x': "y"}, 3]) == '[1, {"x": "y"}, 3]'
    assert _ExtendedEncoder().encode({'x': "y", 'z': 1}) == '{"x": "y", "z": 1}'
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(set([1, {'x': "y"}, 3])) == '[1, {"x": "y"}, 3]'

# Generated at 2022-06-13 19:14:20.833662
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    dc = _ExtendedEncoder()
    assert dc



# Generated at 2022-06-13 19:14:28.690061
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([]) == []
    assert e.default({}) == {}
    assert e.default(set()) == list(set())
    assert e.default(frozenset()) == list(frozenset())
    assert e.default(datetime.utcnow()) == datetime.utcnow().timestamp()
    assert e.default(UUID('11111111-2222-3333-4444-555555555555')) == '11111111-2222-3333-4444-555555555555'
    assert e.default(Enum('Enum', 'a b c')('a')) == 'a'
    assert e.default(Decimal('1.1')) == '1.1'
    assert e.default(None) is None



# Generated at 2022-06-13 19:14:54.570448
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.JSONEncoder().default(dict())


# Generated at 2022-06-13 19:15:04.200788
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default({"abc": 123}) == {"abc": 123}
    assert _ExtendedEncoder().default(1000.01) == 1000.01
    assert _ExtendedEncoder().default(datetime(2019, 10, 1, tzinfo=timezone.utc)) == 1569894400.0
    uuid = UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479")
    assert _ExtendedEncoder().default(uuid) == "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    assert _ExtendedEncoder().default(True) == True


# Generated at 2022-06-13 19:15:06.516810
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1969, 7, 21, 5, 17, 40, tzinfo=timezone.utc)) == '-146789.795833'



# Generated at 2022-06-13 19:15:07.871434
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    j = json.dumps(True, cls=_ExtendedEncoder)
    assert j == 'true'



# Generated at 2022-06-13 19:15:13.998864
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = _ExtendedEncoder()
    assert o.default(None) == None
    assert o.default(1) == 1
    assert o.default(1.1) == 1.1
    assert o.default(True) == True
    assert o.default(False) == False
    assert o.default(1j) == 1j
    assert o.default('a') == 'a'
    assert o.default(list(range(4))) == [0, 1, 2, 3]
    assert o.default(tuple(range(4))) == [0, 1, 2, 3]
    assert o.default(dict(a=1)) == dict(a=1)
    assert o.default(set(range(4))) == [0, 1, 2, 3]

# Generated at 2022-06-13 19:15:14.776652
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    pass



# Generated at 2022-06-13 19:15:25.156987
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    enc = _ExtendedEncoder()
    assert enc.default({}) == {}
    assert enc.default(set()) == list(set())
    assert enc.default(datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp()
    assert enc.default(UUID('7ea89ede-d1c7-48fe-bcdc-57b7837f1ccd')) == '7ea89ede-d1c7-48fe-bcdc-57b7837f1ccd'
    assert enc.default(Decimal('0.10000')) == '0.10000'


# noinspection PyMissingConstructor

# Generated at 2022-06-13 19:15:29.492182
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(2019, 7, 22, 10, 20, 30)) == '1563762030.0'
    assert _ExtendedEncoder().encode(UUID('0e1ecaab-c510-4812-982b-ad4dd6f4e6f4')) == '0e1ecaab-c510-4812-982b-ad4dd6f4e6f4'
    assert _ExtendedEncoder().encode(Decimal('3.14')) == '"3.14"'
    assert _ExtendedEncoder().encode(Decimal('3.14')) == '"3.14"'



# Generated at 2022-06-13 19:15:32.344860
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1: 2}) == '{"1": 2}'


# Generated at 2022-06-13 19:15:45.380388
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_str = json.dumps([1, 2, 3], cls=_ExtendedEncoder)
    assert json_str == '[1, 2, 3]'
    json_str = json.dumps({'a':1,'b':2}, cls=_ExtendedEncoder)
    assert json_str == '{"a": 1, "b": 2}'
    array_like = [1,2,3]
    json_str = json.dumps(array_like, cls=_ExtendedEncoder)
    assert json_str == '[1, 2, 3]'
    json_str = json.dumps({'a':1,'b':2}, cls=_ExtendedEncoder)
    assert json_str == '{"a": 1, "b": 2}'


# Generated at 2022-06-13 19:16:27.208295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default({'a': 9.4}) == {'a': 9.4}
    assert encoder.default([{'a': 9.4}]) == [{'a': 9.4}]
    assert encoder.default([9.4]) == [9.4]
    assert encoder.default(datetime(1996, 10, 12, 12, 12, 12)) == 841038332.0
    assert encoder.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(cfg.NaN) == 'NaN'
    assert encoder.default(cfg.INF) == 'Infinity'
    assert encoder.default

# Generated at 2022-06-13 19:16:32.741006
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(['a', 1, {'b': 2}]) == ['a', 1, {'b': 2}]
    assert e.default(['a', 1, {'b': 2}]) == ['a', 1, {'b': 2}]
    assert e.default({'a': 1}) == {'a': 1}
    assert e.default(['a', 1, {'b': 2}]) == ['a', 1, {'b': 2}]


# Generated at 2022-06-13 19:16:34.242107
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(datetime.now(), cls=_ExtendedEncoder) is not None


# Generated at 2022-06-13 19:16:37.844464
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now())
    assert _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000000'))



# Generated at 2022-06-13 19:16:42.509379
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) > 0
    assert _ExtendedEncoder().default(Decimal('10.0')) == '10.0'
    assert _ExtendedEncoder().default(UUID('11111111-1111-1111-1111-111111111111')) == '11111111-1111-1111-1111-111111111111'


# Generated at 2022-06-13 19:16:48.793322
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    asserte = assert_equal
    asserte(json.dumps({'now': datetime.now()}, cls=_ExtendedEncoder),
            '{"now": %f}' % (datetime.now().timestamp()))
    asserte(json.dumps({'now': datetime.now(timezone.utc)}, cls=_ExtendedEncoder),
            '{"now": %f}' % (datetime.now(timezone.utc).timestamp()))
    asserte(json.dumps({'now': datetime.utcnow()}, cls=_ExtendedEncoder),
            '{"now": %f}' % (datetime.utcnow().timestamp()))

# Generated at 2022-06-13 19:16:51.958105
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({"a": "b", "c": 1}) == '{"a": "b", "c": 1}'


# Generated at 2022-06-13 19:17:02.082561
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(()) == ()
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default(MappingProxyType({})) == {}
    assert _ExtendedEncoder().default(Counter()) == []
    assert _ExtendedEncoder().default(OrderedDict()) == {}
    assert _ExtendedEncoder().default(ValueError()) == \
        '{"args": [], "attributes": {}}'

# Generated at 2022-06-13 19:17:08.378385
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # I'm sorry if this is too complicated
    from dataclasses import dataclass

    @dataclass
    class Dummy:
        name: str
        age: int

    @dataclass
    class Dummy2:
        name: str
        age: int
        dummy: Dummy

    @dataclass
    class Dummy3:
        name: str
        age: int
        dummy: Dummy
        bird: str
    # 1-d array
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    # 2-d array
    assert _ExtendedEncoder().default([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    # dict

# Generated at 2022-06-13 19:17:18.751178
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 'simple', 'list']) == '[1, "simple", "list"]'
    assert _ExtendedEncoder().encode({'1': 'dictionary'}) == '{"1": "dictionary"}'
    assert _ExtendedEncoder().encode(datetime(2000, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == '946684800.0'
    assert _ExtendedEncoder().encode(UUID('{12345678-1234-5678-1234-567812345678}')) == '"12345678-1234-5678-1234-567812345678"'
    assert _ExtendedEncoder().encode(Decimal(1.323)) == '"1.323"'
    assert _ExtendedEnc

# Generated at 2022-06-13 19:18:38.554000
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default('a') == 'a'
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.1) == 1.1
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    some_date = datetime.now(tz=timezone.utc)
    assert _ExtendedEncoder().default(some_date) == some_date.timestamp()

# Generated at 2022-06-13 19:18:45.708759
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()

# Generated at 2022-06-13 19:18:55.475804
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(UUID('00112233-4455-6677-8899-aabbccddeeff')) == '00112233-4455-6677-8899-aabbccddeeff'
    assert encoder.default(datetime.fromtimestamp(0, tz=timezone.utc)) == 0.0
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert encoder.default('abc') == 'abc'
    assert encoder.default(None) is None
    assert encoder.default(True) is True
    assert encoder.default(1) == 1

# Generated at 2022-06-13 19:19:06.264266
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(['a', 'b']) == '["a", "b"]'
    assert _ExtendedEncoder().encode([['a', 'b'], ['c', 'd']]) == \
        '[[["a", "b"], ["c", "d"]]]'
    assert _ExtendedEncoder().encode({'a': 'b'}) == '{"a": "b"}'
    assert _ExtendedEncoder().encode({'a': {'b': {'c': 'd'}}}) == \
        '{"a": {"b": {"c": "d"}}}'
    assert _ExtendedEncoder().encode('a') == '"a"'
    assert _ExtendedEncoder().encode(1) == '1'

# Generated at 2022-06-13 19:19:12.653624
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    obj = _ExtendedEncoder()
    assert obj.default([]) == []
    assert obj.default({}) == {}
    assert obj.default(set()) == list(set())
    assert obj.default({'key': 'value'}) == {'key': 'value'}
    assert obj.default(datetime.now()) == (datetime.now()).timestamp()
    assert obj.default(UUID(int=1)) == '00000000-0000-0000-0000-000000000001'
    assert obj.default(Enum('Enum', 'a b')) == 'a'
    assert obj.default(Enum('Enum', 'a b', module='__main__')) == 'a'
    assert obj.default(Decimal('1.1')) == '1.1'

# Generated at 2022-06-13 19:19:22.225183
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(42) == '42'
    assert _ExtendedEncoder().encode(42.42) == '42.42'
    assert _ExtendedEncoder().encode('42') == '"42"'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode(()) == '[]'
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 19:19:36.694251
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    dec = Decimal(1)
    ext = _ExtendedEncoder()
    if ext.default(dec) != str(dec):
        raise AssertionError("_ExtendedEncoder test failed")
    if ext.default(MappingProxyType({})) != {}:
        raise AssertionError("_ExtendedEncoder test failed")
    if ext.default(defaultdict(int)) != {}:
        raise AssertionError("_ExtendedEncoder test failed")
    if ext.default(defaultdict(list)) != {}:
        raise AssertionError("_ExtendedEncoder test failed")
    if ext.default(ChainMap({})) != {}:
        raise AssertionError("_ExtendedEncoder test failed")