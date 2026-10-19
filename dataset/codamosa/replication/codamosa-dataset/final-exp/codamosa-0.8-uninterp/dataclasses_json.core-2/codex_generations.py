

# Generated at 2022-06-13 19:10:04.863483
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    _ExtendedEncoder().default([1,2,3]) == [1,2,3]
    _ExtendedEncoder().default({'a':1}) == {'a':1}
    _ExtendedEncoder().default(datetime(2019, 3, 12, tzinfo=timezone.utc)) == 1552384000  # type: ignore[comparison-overlap]
    _ExtendedEncoder().default(UUID(int=1)) == "00000000-0000-0000-0000-000000000001"  # type: ignore[comparison-overlap]
    _ExtendedEncoder().default(Decimal("1.2")) == "1.2"  # type: ignore[comparison-overlap]



# Generated at 2022-06-13 19:10:07.454298
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode(datetime(2014, 10, 17, 19, 44, 22, 582713)) == '1413626462.582713'



# Generated at 2022-06-13 19:10:15.221918
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    o = {
        1: 2,
        3: 4,
    }
    assert encoder.default(o) == o
    o = {
        1, 2,
    }
    assert encoder.default(o) == list(o)
    o = range(10)
    assert encoder.default(o) == list(o)
    o = datetime.now(timezone.utc)
    assert encoder.default(o) == o.timestamp()
    o = UUID("{12345678-1234-5678-1234-567812345678}")
    assert encoder.default(o) == "12345678123456781234567812345678"
    o = Decimal(1)

# Generated at 2022-06-13 19:10:20.086297
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(MISSING) is MISSING
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(dict()) == {}
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()



# Generated at 2022-06-13 19:10:21.518285
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    json_value = json.dumps(datetime(2020,5,5,tzinfo=timezone.utc), cls=_ExtendedEncoder)
    assert json_value == "1583568800.0"


# Generated at 2022-06-13 19:10:29.023170
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # _isinstance(o, type) does not work for unknown types.
    # Here we assume that user types are classes deriving from object
    from datetime import datetime
    from uuid import UUID
    from enum import Enum
    from decimal import Decimal

    class EnumTest(Enum):
        a = 1
        b = 2

    class UserType():
        pass

    class SubUserType(object):
        pass

    class SubSubSubUserType(SubUserType):
        pass

    encoder = _ExtendedEncoder(indent=2)
    assert encoder.default(UserType()) == '{}'
    assert encoder.default(SubUserType()) == '{}'
    assert encoder.default(SubSubSubUserType()) == '{}'

# Generated at 2022-06-13 19:10:40.566200
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(set()) == list(set())
    assert _ExtendedEncoder().default(set([1, 2])) == list(set([1, 2]))
    assert _ExtendedEncoder().default(frozenset([1, 2])) == list(frozenset([1, 2]))
    assert _ExtendedEncoder().default(object) == '<class \'object\'>'
    assert _ExtendedEncoder().default(object()) == '<object object at 0x7f0cbebe2830>'
    assert _ExtendedEncoder().default(Exception()) == 'Exception()'
    assert _ExtendedEncoder().default(Exception('test')) == 'Exception(\'test\',)'
    assert _ExtendedEncoder().default(1) == 1

# Generated at 2022-06-13 19:10:47.843441
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Unit test for _ExtendedEncoder
    assert _ExtendedEncoder().default(Collection()) is not None
    assert _ExtendedEncoder().default(Mapping()) is not None
    assert _ExtendedEncoder().default(Enum) is not None
    assert _ExtendedEncoder().default(datetime) is not None
    assert _ExtendedEncoder().default(UUID) is not None
    assert _ExtendedEncoder().default(Decimal) is not None


# Generated at 2022-06-13 19:10:53.327865
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [
        [1, 2, 3],
        {'key': 'value'},
        datetime.now(timezone.utc),
        UUID('ae3508fb-9f7c-44a4-ae7d-8e8e8a2429d4'),
        Decimal('3.3'),
    ]

    for d in data:
        _ExtendedEncoder().encode(d)  # type: ignore



# Generated at 2022-06-13 19:10:59.258336
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    je = _ExtendedEncoder()
    assert je.default([]) == []
    assert je.default(set()) == []
    assert je.default({}) == {}
    assert je.default(set([])) == []
    assert je.default(frozenset([])) == []
    assert je.default(datetime.now(timezone.utc).replace(tzinfo=None)) == datetime.now(timezone.utc).replace(tzinfo=None).timestamp()
    assert je.default(UUID('6d0f6b04-6b68-4b0c-9ad9-decf2da22e6f')) == '6d0f6b04-6b68-4b0c-9ad9-decf2da22e6f'

# Generated at 2022-06-13 19:11:36.012592
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:11:43.115766
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default({'a': 1}) == {'a': 1}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(datetime.now()) >= 1574482881.645977
    assert encoder.default(UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'
    assert encoder.default(cfg.LetterCase.LOWERCASE) == 'lowercase'
    assert encoder.default(Decimal(123)) == '123'



# Generated at 2022-06-13 19:11:49.934240
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test dict
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    # test list
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    # test str
    assert _ExtendedEncoder().encode('abc') == '"abc"'
    # test int
    assert _ExtendedEncoder().encode(123) == '123'
    # test float
    assert _ExtendedEncoder().encode(123.456) == '123.456'
    # test bool
    assert _ExtendedEncoder().encode(True) == 'true'
    # test none
    assert _ExtendedEncoder().encode(None) == 'null'
    # test datetime

# Generated at 2022-06-13 19:12:00.133715
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(MappingProxyType({'a': 1})) == {'a': 1}
    assert e.default({'a': 1}) == {'a': 1}
    assert e.default([1, 'a']) == [1, 'a']
    assert e.default(datetime(2020, 1, 1)) == 1577836800.0
    assert e.default(UUID('56c6d676-0e23-4a75-9f9c-0b91d73fefd3')) == '56c6d676-0e23-4a75-9f9c-0b91d73fefd3'
    assert e.default(Decimal('1')) == '1'

# Generated at 2022-06-13 19:12:07.189263
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    ed = _ExtendedEncoder()
    assert ed.default(datetime.now(timezone.utc)) is not None
    assert ed.default(0) == 0
    assert ed.default(True)
    assert ed.default(None) is None
    assert ed.default('a') == 'a'
    assert ed.default(dict(a=1)) == {'a': 1}
    assert ed.default([1, 2, 3]) == [1, 2, 3]
    assert ed.default(UUID('d21314b1-a5a0-4717-b5e5-9a64c5011cbf')) == 'd21314b1-a5a0-4717-b5e5-9a64c5011cbf'
    assert ed.default(Decimal('3.55'))

# Generated at 2022-06-13 19:12:08.468003
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.JSONEncoder.default(_ExtendedEncoder(), datetime.now())



# Generated at 2022-06-13 19:12:11.628796
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_str = _ExtendedEncoder().encode(set([1, 2, 3]))
    assert json_str == '[1, 2, 3]'



# Generated at 2022-06-13 19:12:22.580913
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime(2019, 9, 23, 15, 10, 33, tzinfo=timezone.utc)) == 1569255233.0
    assert _ExtendedEncoder().default(UUID('4f4b1c75-a91e-4f21-a923-f3c3f3a665a4')) == '4f4b1c75-a91e-4f21-a923-f3c3f3a665a4'
    assert _ExtendedEncoder().default(Decimal('1.23')) == '1.23'
    extend = _ExtendedEncoder()
    with warnings.catch_warnings(record=True) as w:
        warnings.filterwarnings('always')

# Generated at 2022-06-13 19:12:33.138800
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(True) == True
    assert encoder.default(None) == None
    assert encoder.default(1.2) == 1.2
    assert encoder.default(1) == 1
    assert encoder.default('s') == 's'
    assert encoder.default(list()) == list()
    assert encoder.default(dict()) == dict()
    with warnings.catch_warnings(record=True) as wrn:
        encoder.default(set())  # type: ignore
        assert len(wrn) > 0
    assert isinstance(encoder.default(datetime.now(timezone.utc)), float)

# Generated at 2022-06-13 19:12:35.154933
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(datetime.now(), cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:12:57.397342
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    extended_encoder = _ExtendedEncoder()
    extended_encoder.default([1,2,3,4])



# Generated at 2022-06-13 19:13:00.715215
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().encode(UUID('012ee8c8-45e1-4e75-b174-bb8fc9faa0d9'))
    

# Generated at 2022-06-13 19:13:19.574903
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import datetime
    from string import printable
    from uuid import uuid4
    from decimal import Decimal
    from enum import Enum

    # Test for Collection
    assert _ExtendedEncoder().default(tuple(range(10))) == list(range(10))
    assert _ExtendedEncoder().default(set(range(10))) == list(range(10))
    assert _ExtendedEncoder().default(list(range(10))) == list(range(10))

    # Test for Mapping
    assert _ExtendedEncoder().default(dict(zip(range(10), range(10)))) == dict(zip(range(10), range(10)))

    # Test for datetime
    assert _ExtendedEncoder().default(datetime.now()) == datetime.now().timestamp()

    # Test for UUID


# Generated at 2022-06-13 19:13:32.603521
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.loads(json.dumps([1, 2, 3], cls=_ExtendedEncoder)) == [1, 2, 3]
    assert json.loads(json.dumps([1, 2, 3])) == [1, 2, 3]
    assert json.loads(json.dumps({"a": 1, "b": 2})) == {'a': 1, 'b': 2}
    assert json.loads(json.dumps({"a": 1, "b": 2}, cls=_ExtendedEncoder)) == {'a': 1, 'b': 2}
    assert json.loads(json.dumps(datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc))) == None

# Generated at 2022-06-13 19:13:42.287382
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = {}
    assert _ExtendedEncoder().default(o) == {}
    o = [1, 2, 3]
    assert _ExtendedEncoder().default(o) == [1, 2, 3]
    o = {'one': 1, 'two': 2}
    assert _ExtendedEncoder().default(o) == {'one': 1, 'two': 2}
    o = datetime(2019, 10, 20, 15, 42, tzinfo=timezone.utc)
    assert _ExtendedEncoder().default(o) == 1571582520.0
    o = UUID('f27e3efa-d3f3-4edd-9b9d-b11471e5a1c5')

# Generated at 2022-06-13 19:13:52.324466
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'x': 1.0}) == '{"x": 1.0}'
    assert _ExtendedEncoder().encode(datetime(1990, 10, 1)) == \
        '"1990-10-01T00:00:00"'
    assert _ExtendedEncoder().encode(UUID('811c9d07-f9a9-4ecd-b8f7-c2e6d2176d3f')) == \
        '"811c9d07-f9a9-4ecd-b8f7-c2e6d2176d3f"'
    assert _ExtendedEncoder().encode(17) == '17'
    assert _

# Generated at 2022-06-13 19:13:58.412262
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    test_dict = {}
    test_dict['set'] = {1, 2, 3}
    test_dict['frozenset'] = frozenset((1, 2, 3))
    test_dict['tuple'] = (1, 2, 3)
    test_dict['list'] = [1, 2, 3]
    test_dict['dict'] = {a: a for a in [1, 2, 3]}
    test_dict['str'] = str(1)
    test_dict['int'] = int(1)
    test_dict['float'] = float(1)
    test_dict['bool'] = bool(1)
    test_dict['datetime'] = datetime(2000, 1, 1, 1, 1, 1, tzinfo=timezone.utc)
    test_dict['uuid'] = UUID

# Generated at 2022-06-13 19:14:07.492415
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(dict(a=1), cls=_ExtendedEncoder) == '{"a": 1}'
    assert json.dumps(['1', 2], cls=_ExtendedEncoder) == '["1", 2]'
    assert json.dumps((1,2), cls=_ExtendedEncoder) == '[1, 2]'
    assert json.dumps(datetime(2019, 2, 4, 1, 23, 45, tzinfo=timezone.utc), cls=_ExtendedEncoder) == '1549302225.000000'

# Generated at 2022-06-13 19:14:14.006981
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default('test') == 'test'
    assert encoder.default(5) == 5
    assert encoder.default(3.1415926) == 3.1415926
    assert encoder.default(True) == True
    assert encoder.default({'a': 5}) == {'a': 5}
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default(datetime.now(timezone.utc)) in range(datetime.now().timestamp(),
                                                                datetime.now().timestamp() + 1)

# Generated at 2022-06-13 19:14:15.610022
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:14:36.668069
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now()) is not None



# Generated at 2022-06-13 19:14:43.420749
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode == json.JSONEncoder().encode
    for cls in (bool, int, float, str, list, dict, None):
        assert _ExtendedEncoder().encode(cls()) == json.JSONEncoder().encode(cls())
    assert _ExtendedEncoder().default == _ExtendedEncoder().default

Document = namedtuple("Document", ["data", "errors"])



# Generated at 2022-06-13 19:14:48.652666
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default([UUID('550e8400-e29b-41d4-a716-446655440000')]) == [
        '550e8400-e29b-41d4-a716-446655440000']



# Generated at 2022-06-13 19:14:56.691408
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    with pytest.warns(None) as record:
        json.dumps([1, 2, 3], cls=_ExtendedEncoder)
        json.dumps([1, 2, 3], cls=_ExtendedEncoder, skipkeys=True)
        json.dumps([1, 2, 3], cls=_ExtendedEncoder, sort_keys=True)
        json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder)
        json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder, skipkeys=True)
        json.dumps({'a': 1, 'b': 2}, cls=_ExtendedEncoder, sort_keys=True)

# Generated at 2022-06-13 19:15:02.809256
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:15:05.163475
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2.0, 'c', 4]) == "[1, 2.0, \"c\", 4]"


# Generated at 2022-06-13 19:15:12.137915
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    d = json.dumps([], cls=_ExtendedEncoder)
    assert d == "[]"

    d = json.dumps({"a": "abc"}, cls=_ExtendedEncoder)
    assert d == '{"a": "abc"}'

    t = datetime(2020, 3, 3, 0, 0, tzinfo=timezone.utc)
    d = json.dumps(t, cls=_ExtendedEncoder)
    assert d == '1583245200.0'

    uuid_str = '922e7c6a-5d98-4ae5-ad6b-b72c60f6a7e6'
    uuid_value = UUID(uuid_str)
    d = json.dumps(uuid_value, cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:15:24.704522
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder()
    assert ee.default(1.1) == 1.1
    assert ee.default(datetime.now()) == 1558117753.260268
    assert ee.default({1: 1}) == {1: 1}
    assert ee.default([1, 2, 3]) == [1, 2, 3]
    assert ee.default(UUID('1b6f0742-a124-4dba-b1f8-7b2adc689527')) == '1b6f0742-a124-4dba-b1f8-7b2adc689527'
    assert ee.default(Exception()) == 'Exception()'
    assert ee.default(Decimal('1.5')) == '1.5'



# Generated at 2022-06-13 19:15:29.947625
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now()) # type:ignore
    assert _ExtendedEncoder().encode(datetime.now().replace(tzinfo=timezone.utc)) # type:ignore
    assert _ExtendedEncoder().encode(UUID("12345678-1234-5678-1234-567812345678")) # type:ignore
    assert _ExtendedEncoder().encode(Decimal(0.1)) # type:ignore
    # noinspection PyTypeChecker
    assert _ExtendedEncoder().encode(Decimal('NaN')) # type:ignore
    assert _ExtendedEncoder().encode(Decimal('Infinity')) # type:ignore
    assert _ExtendedEncoder().encode(Decimal('-Infinity')) # type:ignore


# Generated at 2022-06-13 19:15:33.465405
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder(sort_keys=True).encode(dict(a=1,b=2)) == '{"a": 1, "b": 2}'


# Generated at 2022-06-13 19:16:32.355166
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(['foo', 'bar']) == ['foo', 'bar']
    assert _ExtendedEncoder().default(('foo', 'bar')) == ['foo', 'bar']
    assert _ExtendedEncoder().default({'foo': 'bar'}) == {'foo': 'bar'}
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert _ExtendedEncoder().default(UUID('{12345678-1234-5678-1234-567812345678}')) == '12345678-1234-5678-1234-567812345678'



# Generated at 2022-06-13 19:16:43.527859
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert(encoder.encode({'a':[1,2,4]}) == '{"a": [1, 2, 4]}')
    assert(encoder.encode({'b':{'c':'d'}}) == '{"b": {"c": "d"}}')
    assert(encoder.encode({'c':1.5}) == '{"c": 1.5}')
    assert(encoder.encode({'d':True}) == '{"d": true}')
    assert(encoder.encode({'e':False}) == '{"e": false}')
    assert(encoder.encode({'f':None}) == '{"f": null}')

# Generated at 2022-06-13 19:16:49.333480
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from dataclasses import dataclass, field
    from dataclasses_json.config import dataclasses_json_config
    from decimal import Decimal

    @dataclass
    class Data:
        name: str
        value: int
        main_field: Decimal = field(metadata=cfg(decoder=Decimal))

    @dataclasses_json_config(encoder=_ExtendedEncoder, letter_case=cfg.LetterCase.CAMEL)
    @dataclass
    class Main:
        name: str
        data: Data
        value: int = field(metadata=cfg(mm_field=cfg.FieldName.CAMEL))
        hidden_field: str = field(metadata=cfg(exclude=True))


# Generated at 2022-06-13 19:17:00.741699
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now())
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc))
    assert _ExtendedEncoder().encode(UUID('00000000-0000-0000-0000-000000000000'))
    assert _ExtendedEncoder().encode({})
    assert _ExtendedEncoder().encode([])
    assert _ExtendedEncoder().encode({'test': 'test'})
    assert _ExtendedEncoder().encode(['test'])
    assert _ExtendedEncoder().encode(Decimal('1.2'))

    class A:
        pass
    assert _ExtendedEncoder().encode(A()) is not None



# Generated at 2022-06-13 19:17:07.899267
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().encode([])
    _ExtendedEncoder().encode(set())
    _ExtendedEncoder().encode(0)
    _ExtendedEncoder().encode(1)
    _ExtendedEncoder().encode(1.0)
    _ExtendedEncoder().encode(1/3)
    _ExtendedEncoder().encode(None)
    _ExtendedEncoder().encode(False)
    _ExtendedEncoder().encode(True)
    _ExtendedEncoder().encode({"list": [1, 2]})
    _ExtendedEncoder().encode({"set": {1, 2}})
    _ExtendedEncoder().encode({"dict": {"key": "val"}})

# Generated at 2022-06-13 19:17:15.330902
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    j = _ExtendedEncoder().encode(
        {'a': [1, 2.5, True, 'string', [1, 2], {'a': True}], 'b': 1, 'c': {'a': 1}})
    assert j == (
        '{"a": [1, 2.5, true, "string", [1, 2], {"a": true}], '
        '"b": 1, "c": {"a": 1}}'
    )



# Generated at 2022-06-13 19:17:27.549722
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(5) == 5
    _ExtendedEncoder().default([]) == []
    _ExtendedEncoder().default(()) == []
    _ExtendedEncoder().default({}) == {}
    _ExtendedEncoder().default(set()) == []
    _ExtendedEncoder().default(frozenset()) == []
    _ExtendedEncoder().default(datetime.fromtimestamp(0, timezone.utc)) == 0
    _ExtendedEncoder().default(UUID('6b9bc6e5-6b96-49b5-85db-c5a2deee2e2d')) == '6b9bc6e5-6b96-49b5-85db-c5a2deee2e2d'

# Generated at 2022-06-13 19:17:38.509355
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    s = json.dumps([datetime(2018, 3, 3, 10, 36, 0),  # datetime
                    datetime(2018, 3, 3, 10, 36, 0, tzinfo=timezone.utc),  # datetime with timezone
                    [1, 2, 3, 4],  # list
                    {'a': 1, 'b': 2},  # dict
                    Enum('x', 'y z'),  # enum
                    UUID('123e4567-e89b-12d3-a456-426655440000'),  # UUID
                    Decimal(10.24)  # Decimal
                    ], cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:17:44.453461
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:17:54.589460
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(dict(foo=1)) == '{"foo": 1}'
    assert _ExtendedEncoder().encode(dict(foo='bar')) == '{"foo": "bar"}'
    assert _ExtendedEncoder().encode(dict(foo=(1, 2, 3))) == '{"foo": [1, 2, 3]}'
    assert _ExtendedEncoder().encode(dict(foo=True)) == '{"foo": true}'
    assert _ExtendedEncoder().encode(dict(foo=1.0)) == '{"foo": 1.0}'

# Generated at 2022-06-13 19:19:04.346615
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'foo': datetime(2020, 1, 1)}) == '{"foo": 1577836800.0}'
    assert _ExtendedEncoder().encode({'baz': Decimal('1.23')}) == '{"baz": "1.23"}'

_extended_encoder = _ExtendedEncoder()



# Generated at 2022-06-13 19:19:06.190696
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import doctest

    assert doctest.testmod().failed == 0

# test for methods of class _ExtendedEncoder

# Generated at 2022-06-13 19:19:12.598003
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    a = json.dumps({'a': 0.01, 'b': 0.001},
                   cls=_ExtendedEncoder)
    assert a == '{"a": 0.01, "b": 0.001}'
    a = json.dumps({'a': datetime(2018, 10, 20, 11, 0, 59, 1000, timezone.utc),
                    'b': datetime(2018, 10, 20, 11, 0, 59, timezone.utc)},
                   cls=_ExtendedEncoder)
    assert a == '{"a": 1540049659.001, "b": 1540049659.0}'

# Generated at 2022-06-13 19:19:15.325618
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({123: 456}) == '{"123": 456}'


# Generated at 2022-06-13 19:19:23.156385
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(Decimal('1.234')) == '"1.234"'
    assert _ExtendedEncoder().encode(UUID('e74c522f-6b90-4558-864d-a3b3a861a18e')) == '"e74c522f-6b90-4558-864d-a3b3a861a18e"'
    assert _ExtendedEncoder().encode(datetime(2019, 3, 6, 9, 30, 0, 0)) == '1551871800.0'
   

# Generated at 2022-06-13 19:19:27.800186
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoded = json.dumps(
        [
            datetime.now(timezone.utc),
            UUID('0e0c2ece-ba9c-4c0b-ab38-0c8aeb7d4bfd')
        ],
        cls=_ExtendedEncoder)
    assert encoded == '[1578602250.290984, "0e0c2ece-ba9c-4c0b-ab38-0c8aeb7d4bfd"]'


# Generated at 2022-06-13 19:19:35.133322
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import pytest
    e = _ExtendedEncoder()
    with pytest.raises(TypeError):
        e.default(0)
        e.default(1)
        e.default(0.0)
        e.default(None)
        e.default(True)
        e.default(False)
        e.default('test')
        e.default(b'binary')
        e.default(bytearray(2))
        e.default(['test list'])

        class TestClass: pass
        e.default(TestClass)
        e.default(TestClass())

        class TestClass:
            def __eq__(self, other):
                return False
        assert e.default(TestClass()) == TestClass()
        test_class_instance = TestClass()

# Generated at 2022-06-13 19:19:41.161392
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(UUID('6eda64e6-c07f-4f6d-b6a2-1e272979020c')) == '6eda64e6-c07f-4f6d-b6a2-1e272979020c'
    assert _ExtendedEncoder().default(datetime(2000, 1, 1, tzinfo=timezone.utc)) == 946684800.0

