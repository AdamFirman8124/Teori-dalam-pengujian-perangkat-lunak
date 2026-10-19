

# Generated at 2022-06-13 19:10:05.776365
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    rawdata = {'a': [1, 2],
               'b': {'b1': 'B1', 'b2': [1, 2, 3], 'b3': {'b31': 1, 'b32': [31, 32, 33]}},
               'c': datetime.now(timezone.utc),
               'd': UUID('a412f726-5b1f-4559-b847-4dfc4b2df4e4'),
               'e': 'e1',
               'f': 1.23456789,
               'g': 2,
               'h': True,
               'i': None}

    # Run
    jsonstr = json.dumps(rawdata, cls=_ExtendedEncoder)

    # Verify
    data_ = json.loads(jsonstr)


# Generated at 2022-06-13 19:10:07.200063
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(timezone.utc) == 'UTC'



# Generated at 2022-06-13 19:10:17.533943
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(0.1) == '0.1'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode('abc') == '"abc"'
    now = datetime.now(timezone.utc)
    assert _ExtendedEncoder().encode(now) == json.dumps(now.timestamp())

# Generated at 2022-06-13 19:10:26.298329
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert e.default(datetime.now()) == datetime.now().timestamp()
    assert e.default(UUID(hex='6ba7b810-9dad-11d1-80b4-00c04fd430c8')) == '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
    assert e.default(Decimal('1.5')) == '1.5'
    assert e.default(None) == None
    assert e.default(Exception()) == '{}'


# Generated at 2022-06-13 19:10:38.293065
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Decimal(1.1)) == '"1.1"'
    assert _ExtendedEncoder().encode({1, 2}) == '[1, 2]'
    assert _ExtendedEncoder().encode(set([1, 2])) == '[1, 2]'
    assert _ExtendedEncoder().encode({1: 'a', 2: 'b'}) == '{"1": "a", "2": "b"}'
    assert _ExtendedEncoder().encode(
        {('a', 1): 'a', ('b', 2): 'b'}) == '{"a 1": "a", "b 2": "b"}'

# Generated at 2022-06-13 19:10:50.128214
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [
        ([]),
        ([1, 2, 3]),
        ({}),
        ({'foo': 'bar'}),
        (set()),
        (set([1, 2, 3])),
        (datetime.now(timezone.utc)),
        (UUID('4189bd7c-f868-4c13-8d18-b1701c8debed')),
        (Decimal(1.1)),
        (Decimal('1.2')),
    ]
    data_default = [
        (object()),
        (dataclasses.dataclass()),
    ]
    encoder = _ExtendedEncoder()
    assert all([encoder.default(d) == d for d in data])

# Generated at 2022-06-13 19:10:52.668459
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ExtendedEncoder = _ExtendedEncoder()
    assert ExtendedEncoder.default(['1', 2, 3]) == ['1', 2, 3]


# Generated at 2022-06-13 19:10:58.811837
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    o = [[1, 2], [3, 4]]
    result = _ExtendedEncoder().default(o)
    assert result == o

    o = {'a': 1, 'b': 2}
    result = _ExtendedEncoder().default(o)
    assert result == o

    o = datetime.now()
    result = _ExtendedEncoder().default(o)
    assert result == o.timestamp()

    o = UUID('{12345678-1234-1234-1234-123456789ABC}')
    result = _ExtendedEncoder().default(o)
    assert result == str(o)

    assert _ExtendedEncoder().default('a') == 'a'
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(2.5)

# Generated at 2022-06-13 19:11:02.380935
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(object(), cls=_ExtendedEncoder)
    json.dumps(object, cls=_ExtendedEncoder)


# Generated at 2022-06-13 19:11:12.933322
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(1, cls=_ExtendedEncoder) == '1'
    assert json.dumps(1.1, cls=_ExtendedEncoder) == '1.1'
    assert json.dumps('a', cls=_ExtendedEncoder) == '"a"'
    assert json.dumps(None, cls=_ExtendedEncoder) == 'null'
    assert json.dumps(True, cls=_ExtendedEncoder) == 'true'
    assert json.dumps(False, cls=_ExtendedEncoder) == 'false'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'

# Generated at 2022-06-13 19:11:46.491266
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.JSONEncoder



# Generated at 2022-06-13 19:11:55.515380
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(list(range(10))) == '[]'
    assert _ExtendedEncoder().encode(dict(a='a')) == '{}'
    assert _ExtendedEncoder().encode(UUID(int=1)) == '"00000000-0000-0000-0000-000000000001"'
    assert _ExtendedEncoder().encode(Enum('a', 'b')) == '"a"'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == '{}'
    assert _ExtendedEncoder().encode(Decimal(1)) == '"1"'



# Generated at 2022-06-13 19:12:03.362426
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [
        {'a': datetime(2020, 6, 1, 12, 0, 0, 0, tzinfo=timezone.utc)},
        {'a': UUID('30196985-9f74-4c11-a83e-94c8067a2e1c')},
        {'a': Decimal('3.14')},
        ]
    json_text = _ExtendedEncoder().encode(data)
    expected_json_text = '[{"a": 1591028800.0}, {"a": "30196985-9f74-4c11-a83e-94c8067a2e1c"}, {"a": "3.14"}]'
    assert json_text == expected_json_text



# Generated at 2022-06-13 19:12:11.233488
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = _ExtendedEncoder().default(MappingProxyType({}))
    assert o == {}
    o = _ExtendedEncoder().default(dict())
    assert o == {}
    o = _ExtendedEncoder().default(set())
    assert o == []
    o = _ExtendedEncoder().default(frozenset())
    assert o == []
    o = _ExtendedEncoder().default(datetime.now())
    assert type(o) is float
    o = _ExtendedEncoder().default(UUID('{12345678-1234-5678-1234-567812345678}'))
    assert type(o) is str
    o = _ExtendedEncoder().default(Decimal("100.35"))
    assert type(o) is str

# Generated at 2022-06-13 19:12:22.352125
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    a: Any = None
    a = _ExtendedEncoder.default(a, [1, 2, 3])
    assert a == [1, 2, 3]
    a = _ExtendedEncoder.default(a, (1, 2, 3))
    assert a == [1, 2, 3]
    a = _ExtendedEncoder.default(a, {1, 2, 3})
    assert a == [1, 2, 3]
    a = _ExtendedEncoder.default(a, {'test': 2})
    assert a == {'test': 2}
    d = datetime.now(tz=timezone.utc)
    a = _ExtendedEncoder.default(a, d)
    assert isinstance(a, float)

# Generated at 2022-06-13 19:12:32.186009
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder.default(None, 10) == 10
    assert _ExtendedEncoder.default(None, [1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder.default(None, {}) == {}
    assert _ExtendedEncoder.default(None, datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp()
    assert _ExtendedEncoder.default(None, UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'
    assert _ExtendedEncoder.default(None, cfg.MISSING_ERROR) is MISSING


# Generated at 2022-06-13 19:12:42.015323
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    o = {'key': 'value'}
    assert encoder.default(o) is o
    o = {'key': 'value'}
    assert encoder.default(o) is o
    assert encoder.default(datetime.now()) > 0
    assert encoder.default(UUID('7c64edf8-1a99-43d5-9c9b-8ce4905c3418')) == '7c64edf8-1a99-43d5-9c9b-8ce4905c3418'
    o = Enum('FooEnum', 'bar baz')('baz')
    assert encoder.default(o) == o.value

# TODO: test if exceptions are raised as required
# see: https://github

# Generated at 2022-06-13 19:12:42.929830
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(123)



# Generated at 2022-06-13 19:12:52.499009
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(1, cls=_ExtendedEncoder) == '1'
    assert json.dumps([1], cls=_ExtendedEncoder) == '[1]'
    assert json.dumps({1: 1}, cls=_ExtendedEncoder) == '{"1": 1}'
    assert json.dumps(datetime(1970, 1, 1, 1, 1, 1, tzinfo=timezone.utc),
                      cls=_ExtendedEncoder) == '3601'
    assert json.dumps(UUID('00000000-0000-0000-0000-000000000000'),
                      cls=_ExtendedEncoder) == '"00000000-0000-0000-0000-000000000000"'
    assert json.dumps(None, cls=_ExtendedEncoder) is None  # type: ignore

# Generated at 2022-06-13 19:13:04.901794
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == \
        '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == \
        '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == \
        '[1, 2, 3]'
    assert _ExtendedEncoder().encode(['word1', 'word2', 'word3']) == \
        '["word1", "word2", "word3"]'
    assert _ExtendedEncoder().encode({'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}) == \
        '{"key1": "val1", "key2": "val2", "key3": "val3"}'

# Generated at 2022-06-13 19:13:29.139422
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.now())
    assert encoder.default(UUID('a7d6218e-e828-4a27-9235-c2f2fc8a735d'))
    assert encoder.default(Decimal('1.22'))
    assert encoder.default([1, 2, 3])
    assert encoder.default({'a': 1, 'b': 2})
    assert encoder.default(True)



# Generated at 2022-06-13 19:13:32.715749
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Constructor
    ExtendedEncoder = _ExtendedEncoder(indent='  ')
    assert ExtendedEncoder is not None


# Generated at 2022-06-13 19:13:33.879546
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(
        1234,
        cls=_ExtendedEncoder
    ) == '1234'



# Generated at 2022-06-13 19:13:47.762847
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(tz=timezone.utc))
    assert _ExtendedEncoder().default(UUID('123e4567-e89b-12d3-a456-426655440000'))
    assert _ExtendedEncoder().default(Decimal(0.1))



# Generated at 2022-06-13 19:13:54.956253
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode(dict()) == '{}'
    assert _ExtendedEncoder().encode(set()) == '[]'
    assert _ExtendedEncoder().encode(frozenset()) == '[]'
    assert _ExtendedEncoder().encode(list()) == '[]'
    assert _ExtendedEncoder().encode(tuple()) == '[]'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode(1.0) == '1.0'
    assert _ExtendedEncoder().encode(True) == 'true'

# Generated at 2022-06-13 19:14:00.193746
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder().encode
    assert e(3) == '3'
    assert e([3, 4]) == '[3, 4]'
    assert e({'a': 3, 'b': 4}) == '{"a": 3, "b": 4}'
    assert e({'a', 3, 4}) == '[3, 4, "a"]'
    assert e(datetime.now(timezone.utc)) == e(datetime.now(timezone.utc).timestamp())
    assert e(UUID('c9bf9e57-1685-4c89-bafb-ff5af830be8a')) == '"c9bf9e57-1685-4c89-bafb-ff5af830be8a"'

# Generated at 2022-06-13 19:14:08.393192
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    # dict
    assert _ExtendedEncoder().default({1: 2}) == {1: 2}
    assert _ExtendedEncoder().default(MappingProxyType({1: 2})) == {1: 2}
    # list
    assert _ExtendedEncoder().default([1, 2]) == [1, 2]
    assert _ExtendedEncoder().default(UserList([1, 2])) == [1, 2]
    assert _ExtendedEncoder().default(UserList([1, 2])) == [1, 2]
    assert _ExtendedEncoder().default(UserList([1, 2])) == [1, 2]
    # Set
    assert _ExtendedEncoder().default({1, 2}) == [1, 2]

# Generated at 2022-06-13 19:14:14.189778
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(DefaultFrozenOrderDict([(1, 1)])) == \
           DefaultFrozenOrderDict([(1, 1)])
    assert _ExtendedEncoder().default(DefaultFrozenOrderDict({1: 1})) == \
           DefaultFrozenOrderDict({1: 1})
    assert _ExtendedEncoder().default(DefaultFrozenOrderDict()) == \
           DefaultFrozenOrderDict()
    assert _ExtendedEncoder().default(DefaultFrozenOrderDict({})) == \
           DefaultFrozenOrderDict({})
    assert _ExtendedEncoder().default(DefaultFrozenOrderDict({1: [1, 2]})) == \
           DefaultFrozenOrderDict({1: [1, 2]})

# Generated at 2022-06-13 19:14:24.431674
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(set([])) == []
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(dict()) == {}
    assert encoder.default(dict({"a": 1, "b": 2})) == {"a": 1, "b": 2}
    assert encoder.default(datetime(2020, 1, 1)) == 1577836800.0
    assert encoder.default(datetime(2020, 1, 1, 12, 30, tzinfo=timezone.utc)) == 1577863800.0

# Generated at 2022-06-13 19:14:29.208285
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.encode([{'a': 1, 'b': 2}]) == '[{"a": 1, "b": 2}]'
    assert e.encode(UUID('8e445908-9ce6-4c04-8c6c-4f4b4f4b4f4b')) == '"8e445908-9ce6-4c04-8c6c-4f4b4f4b4f4b"'
    assert e.encode(datetime.now(timezone.utc)) == json.dumps(datetime.now(timezone.utc).timestamp())
    assert e.encode(Decimal(1) / Decimal(7)) == '"0.14285714285714285"'
    assert e.en

# Generated at 2022-06-13 19:15:22.933549
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    actual = _ExtendedEncoder().default(datetime.fromtimestamp(0, tz=timezone.utc))
    expect = 0.0
    assert actual == expect

# Generated at 2022-06-13 19:15:37.448362
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # jsons = [1, 2, 3]
    # jsons = {'a': {'b': 1, 'c': 2, 'd': 3}, 'b': 5}
    jsons = {'a': 1, 'b': 5}
    encoder = _ExtendedEncoder()
    encoder.encode(jsons)
    # assert encoder.encode(jsons) == '[1,2,3]'
    # assert encoder.encode(jsons) == '{"a":{"b":1,"c":2,"d":3},"b":5}'
    assert encoder.encode(jsons) == '{"a":1,"b":5}'


# Generated at 2022-06-13 19:15:54.309679
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(dict([('key', 'value')])) == json.dumps(dict([('key', 'value')]))
    assert _ExtendedEncoder().encode(set(['value'])) == json.dumps(['value'])
    assert _ExtendedEncoder().encode(datetime(2018, 1, 1, 12, tzinfo=timezone.utc)) == json.dumps(1514806400.0)
    assert _ExtendedEncoder().encode(UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')) == json.dumps('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')
    assert _ExtendedEncoder().encode

# Generated at 2022-06-13 19:15:56.116705
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(_ExtendedEncoder()) == '{}'



# Generated at 2022-06-13 19:16:02.849498
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _ExtendedEncoder().default(datetime(2020, 9, 11, 17, 37)) == 1599989820.0
    assert _ExtendedEncoder().default(datetime.fromtimestamp(1599989820.0, timezone.utc)) == 1599989820.0
    assert _ExtendedEncoder().default(UUID('7e175e86-9d7c-42d5-abe7-104de93fb8e3')) == '7e175e86-9d7c-42d5-abe7-104de93fb8e3'


# Generated at 2022-06-13 19:16:10.211051
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    test_input = [
        ({}, dict),
        ({'a': 1}, dict),
        ([], list),
        ([1], list),
        ('a', str),
        ('', str),
        (12345, int),
        (12.34, float),
        (True, bool),
        (False, bool),
        (None, type(None)),
        (datetime(2019, 11, 12, 12, 12, 12, 123000, tzinfo=timezone.utc), float),
        (UUID('000011112222-3333-4444-5555-666677778888'), str),
        (EnumSample.VALUE1, int),
        (Decimal('0.1'), str)
    ]

# Generated at 2022-06-13 19:16:14.345853
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(Decimal('3.14')) == '3.14'
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert _ExtendedEncoder().default(UUID('8fa9be69-1d80-4cbb-a8a5-c6e98f7f1f30')) == '8fa9be69-1d80-4cbb-a8a5-c6e98f7f1f30'



# Generated at 2022-06-13 19:16:26.769404
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:16:33.027274
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default({1: 2}) == {1: 2}
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert encoder.default(UUID("c9bf9e57-1685-4c89-bafb-ff5af830be8a")) == "c9bf9e57-1685-4c89-bafb-ff5af830be8a"



# Generated at 2022-06-13 19:16:43.854282
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == str(datetime.now(timezone.utc))

# Generated at 2022-06-13 19:18:49.152693
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.utcnow()) > 0


# Generated at 2022-06-13 19:18:56.316331
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = _ExtendedEncoder().default('abc')
    assert o == 'abc'
    o = _ExtendedEncoder().default(1)
    assert o == 1
    o = _ExtendedEncoder().default(1.2)
    assert o == 1.2
    o = _ExtendedEncoder().default(True)
    assert o == True
    o = _ExtendedEncoder().default(False)
    assert o == False
    o = _ExtendedEncoder().default(None)
    assert o == None
    o = _ExtendedEncoder().default([1, 2])
    assert o == [1, 2]
    o = _ExtendedEncoder().default({2: 3})
    assert o == {2: 3}
    o = _ExtendedEncoder().default(['a', 2])

# Generated at 2022-06-13 19:19:06.611237
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from random import randint
    from uuid import uuid4
    from datetime import timedelta
    from decimal import Decimal
    from enum import Enum
    class DummyEnum(Enum):
        VALUE = "value"
        NIL = None


# Generated at 2022-06-13 19:19:16.447692
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([1, 2, 3]) == [1, 2, 3]
    assert e.default({"a": 1}) == {"a": 1}
    assert e.default(1) == 1
    assert e.default(1.0) == 1.0
    assert e.default(True) == True
    assert e.default(None) == None
    assert e.default((1, 2, {'a': 1})) == [1, 2, {'a': 1}]
    assert e.default(datetime(1990, 1, 1)) == 631152000.0
    assert e.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert e

# Generated at 2022-06-13 19:19:23.784292
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder()
    assert ee.default([1,2,3]) == [1,2,3]
    assert ee.default([(1,2),(3,4)]) == [[1,2],[3,4]]
    assert ee.default({'a':1,'b':'c'}) == {'a':1,'b':'c'}
    assert ee.default({1:'a',2:'b'}) == {1:'a',2:'b'}
    assert ee.default(datetime.now(timezone.utc)) == pytest.approx(datetime.now().timestamp())

# Generated at 2022-06-13 19:19:31.999381
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # assert that on encoding the data, we get the expected JSON output
    class Test:
        a = 0
    output = json.dumps(
        Test(),
        cls=_ExtendedEncoder,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        indent=4
    )
    assert output == '{\n    "a": 0\n}'


# Generated at 2022-06-13 19:19:35.359576
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now())
    assert _ExtendedEncoder().encode(UUID('94d2a5f5-f5a5-44cd-9357-06b478a5c5ae'))
    assert _ExtendedEncoder().encode(datetime.utcnow())
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc))
