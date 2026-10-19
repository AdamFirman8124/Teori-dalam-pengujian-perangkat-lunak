

# Generated at 2022-06-13 19:10:05.015790
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'1': 1, '2': 2, '3': 3}) == '{"1": 1, "2": 2, "3": 3}'
    assert _ExtendedEncoder().encode(datetime.now()) == '"{}"'.format(datetime.now().timestamp())
    assert _ExtendedEncoder().encode(UUID('01234567-89ab-cdef-0123456789ab')) == '"01234567-89ab-cdef-0123456789ab"'
    assert _ExtendedEncoder().encode(Decimal('1.2345678e9')) == '"12.345678E+8"'


# noinspection

# Generated at 2022-06-13 19:10:13.524599
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    x = _ExtendedEncoder().encode(['a', 'b', 1.0, 2.1])
    assert '["a", "b", 1.0, 2.1]' == x
    x = _ExtendedEncoder().encode(['a', 'b', 1, 2])
    assert '["a", "b", 1, 2]' == x
    x = _ExtendedEncoder().encode({'a': 1, 'b': 2})
    assert '{"a": 1, "b": 2}' == x
    x = _ExtendedEncoder().encode(['a', 'b', datetime(2018, 7, 28, 10, 51)])
    assert '["a", "b", 1532769460.0]' == x

# Generated at 2022-06-13 19:10:19.782296
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({
        1: 1,
        'test': 'test',
        None: None,
    }, cls=_ExtendedEncoder) == '''\
{"1": 1, "test": "test", "null": null}'''

    assert json.dumps({
        datetime(2000, 1, 1, 1, 1, 1, 0, timezone.utc): 1,
        'test': 'test',
    }, cls=_ExtendedEncoder) == '''\
{"2000-01-01T01:01:01+00:00": 1, "test": "test"}'''


# Generated at 2022-06-13 19:10:25.942435
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [1, 2, 3, 4]
    result = _ExtendedEncoder().encode(data)
    assert result == '[1, 2, 3, 4]'

    data = {'a': 1, 'b': 2}
    result = _ExtendedEncoder().encode(data)
    assert result == '{"a": 1, "b": 2}'

    data = datetime(1970, 1, 1, tzinfo=timezone.utc)
    result = _ExtendedEncoder().encode(data)
    assert result == '0'



# Generated at 2022-06-13 19:10:28.887462
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Decimal("3.14")) == "\"3.14\""



# Generated at 2022-06-13 19:10:38.767408
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = _ExtendedEncoder().default({"test": list})
    assert isinstance(result, dict)
    result = _ExtendedEncoder().default([1, 2])
    assert isinstance(result, list)
    result = _ExtendedEncoder().default(datetime.now(timezone.utc))
    assert isinstance(result, float)
    result = _ExtendedEncoder().default(UUID("0a235d37-0b57-4e00-8ad9-d9fe6f7ce6a1"))
    assert isinstance(result, str)
    result = _ExtendedEncoder().default(Decimal('123.456'))
    assert isinstance(result, str)



# Generated at 2022-06-13 19:10:45.524651
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default('test') == 'test'
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None
    assert (_ExtendedEncoder().default(datetime(2000, 1, 1, tzinfo=timezone.utc))
            == datetime(2000, 1, 1, tzinfo=timezone.utc).timestamp())



# Generated at 2022-06-13 19:10:55.392798
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

    # Test for collections
    for collection in [dict(), [], tuple()]:
        assert encoder.default(collection) == collection

    # Test for datetime
    date = datetime(year=2019, month=8, day=5, tzinfo=timezone.utc)
    assert encoder.default(date) == 1565020800.0

    # Test for UUID
    uuid = UUID('6e8bc430-9c3a-11d9-9669-0800200c9a66')
    assert encoder.default(uuid) == '6e8bc430-9c3a-11d9-9669-0800200c9a66'

    # Test for Enum
    class TestEnum(Enum):
        FIRST = 'first'


# Generated at 2022-06-13 19:10:59.131520
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'foo': datetime(1970, 1, 1)}) == json.dumps({'foo': 0})


# Generated at 2022-06-13 19:11:03.369449
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = [1, 2, 3]
    j = json.dumps(o, cls=_ExtendedEncoder)
    assert j == "[1, 2, 3]"



# Generated at 2022-06-13 19:11:35.980706
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import datetime
    import decimal
    import json
    import uuid
    from enum import Enum
    from dataclasses import dataclass, field

    @dataclass
    class TestDcClass:
        i: int
        uuid: uuid.UUID
        d: datetime.datetime
        f: float
        d1: decimal.Decimal
        s: str
        b: bool
        l: list
        dict: dict
        t: tuple
        e1: "EnumDcClass"
        e2: "EnumDcClass2"
        e3: "EnumDcClass3"
        e4: "EnumDcClass4"
        e5: "EnumDcClass5"
        e6: "EnumDcClass6"

# Generated at 2022-06-13 19:11:41.830555
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # test for mapping
    f = open("test_extended_encoder.txt", 'w')
    f.write("test for mapping")
    f.write("\n")
    test_mapping = {1: 'a', 2: 'b'}
    f.write(json.dumps(test_mapping, cls=_ExtendedEncoder))
    f.write("\n")
    f.close()
    # test for collection
    f = open("test_extended_encoder.txt", 'a')
    f.write("test for collection")
    f.write("\n")
    test_collection = ['a', 'b', 'c']
    f.write(json.dumps(test_collection, cls=_ExtendedEncoder))
    f.write("\n")
    f.close

# Generated at 2022-06-13 19:11:45.499452
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    """Unit test for constructor of class _ExtendedEncoder."""
    assert _ExtendedEncoder().encode(datetime(2019, 1, 12, 0, 0, 0, tzinfo=timezone.utc)) == '"1547033600.0"'



# Generated at 2022-06-13 19:11:49.988952
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from decimal import Decimal
    from uuid import UUID
    from datetime import datetime
    import json
    
    d = datetime(2018, 12, 15, 12, 12, 12, tzinfo=timezone.utc)
    u = UUID('{12345678-1234-5678-1234-567812345678}')
    dec = Decimal("2.2250738585072011e-308")
    e = _ExtendedEncoder()
    assert e.default(d) == 1544863132.0
    assert e.default(dec) == '2.2250738585072011e-308'
    assert e.default(u) == '12345678-1234-5678-1234-567812345678'
    assert e.default("str") == "str"




# Generated at 2022-06-13 19:11:53.814757
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    res = json.dumps(cfg.encode_tzinfo,
                     cls=_ExtendedEncoder)
    assert res == '"' + cfg.encode_tzinfo.name + '"'


# Generated at 2022-06-13 19:12:02.535506
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = {
        'Bool': False,
        'String': 'My name is',
        'List': [1, 2, 3, 'what'],
        'Dict': {'a': 1, 'b': 2, 'c': [3, 4, 5]},
        'Datetime': datetime(2018, 11, 15, 6, 14, 54, tzinfo=timezone.utc),
        'UUID': UUID('9bd9e0f0-a9b4-4a41-ba70-4f4fc3d3e2bf'),
        'Decimal': Decimal("12.345"),
    }

# Generated at 2022-06-13 19:12:10.643776
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    expected_mapping_dict = {
        'key1': 'val1',
        'key2': 'val2',
    }
    expected_list = ['a', 'b', 'c']
    expected_datetime = datetime.now(timezone.utc)
    expected_uuid = UUID('aaf4c61d-404d-4ab3-b3a9-cf6d70b864d6')
    expected_enum = cfg.enforce_enum(Color)('blue')
    expected_decimal = Decimal('1.2')

    data = _ExtendedEncoder().encode([
        expected_mapping_dict,
        expected_list,
        expected_datetime,
        expected_uuid,
        expected_enum,
        expected_decimal,
    ])

# Generated at 2022-06-13 19:12:22.034297
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    class MyClass:
        def __init__(self, x):
            self.x = x
        def __repr__(self):
            return 'MyClass({})'.format(self.x)

    assert json.loads(_ExtendedEncoder().encode(dict(a=1, b=2))) == dict(a=1, b=2)
    assert json.loads(_ExtendedEncoder().encode([1, 2, 3])) == [1, 2, 3]

# Generated at 2022-06-13 19:12:32.821159
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.loads(json.dumps(datetime(2017, 1, 1, 12, 0, 0), cls=_ExtendedEncoder)) == 1483292800
    assert json.loads(json.dumps(set([1, 2, 3]), cls=_ExtendedEncoder)) == [1, 2, 3]
    assert json.loads(json.dumps({"1": 1, "2": 2}, cls=_ExtendedEncoder)) == {"1": 1, "2": 2}

# Generated at 2022-06-13 19:12:42.345359
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '{"@set":{"1":true,"2":true,"3":true}}'
    assert _ExtendedEncoder().encode(frozenset([1, 2, 3])) == '{"@frozenset":{"1":true,"2":true,"3":true}}'
    assert _ExtendedEncoder().encode(
        datetime(2020, 3, 26, 15, 20, 11, 649015, tzinfo=timezone.utc)) == '1585217911.649015'
    assert _ExtendedEncoder().encode(
        UUID('{11111111-2222-3333-4444-555555555555}')) == '11111111-2222-3333-4444-555555555555'

# Generated at 2022-06-13 19:13:16.145541
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(Decimal()) == "0"
    assert _ExtendedEncoder().default(UUID(int=0)) == "00000000-0000-0000-0000-000000000000"
    with pytest.raises(TypeError):
        _ExtendedEncoder().default(Exception())


# noinspection PyMethodMayBeStatic

# Generated at 2022-06-13 19:13:18.972515
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([]) == "[]"
    assert _ExtendedEncoder().encode({}) == "{}"
    assert _ExtendedEncoder().encode({"a": 1}) == '{"a": 1}'



# Generated at 2022-06-13 19:13:32.094699
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert _ExtendedEncoder().default(UUID('a8a609a4-9cbc-4e91-823b-4d4f53a45b84')) == 'a8a609a4-9cbc-4e91-823b-4d4f53a45b84'
    assert _Extended

# Generated at 2022-06-13 19:13:38.124320
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(['foo', 'bar']) == ['foo', 'bar']
    assert _ExtendedEncoder().default(('foo', 'bar')) == ['foo', 'bar']
    assert _ExtendedEncoder().default(set(['foo', 'bar'])) == ['foo', 'bar']
    assert _ExtendedEncoder().default({'foo': 'bar'}) == {'foo': 'bar'}

    t = datetime.now(timezone.utc)
    assert _ExtendedEncoder().default(t) == t.timestamp()
    assert _ExtendedEncoder().default(UUID(int=1)) == '00000000-0000-0000-0000-000000000001'

# Generated at 2022-06-13 19:13:40.649178
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime(2020, 2, 20, 15, 5, 2)) == 1582221602.0


# Generated at 2022-06-13 19:13:47.231623
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()
    # test for collections
    assert enc.default((1, 2, 3)) == [1, 2, 3]
    assert enc.default([1, 2, 3]) == [1, 2, 3]
    assert enc.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert enc.default({1, 2, 3}) == [1, 2, 3]
    # test for datetime
    dt = datetime(2019, 7, 27, 12, 34, 56, 123456, timezone.utc)
    assert enc.default(dt) == 1564084896.123456




# Generated at 2022-06-13 19:13:48.493338
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    print(_ExtendedEncoder().encode({"x": 5}))

test__ExtendedEncoder()



# Generated at 2022-06-13 19:13:55.497688
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1, 2, 3}) == "{1, 2, 3}"
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({1:2}) == "{1: 2}"
    assert _ExtendedEncoder().encode({'a':2}) == '{"a": 2}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == '1.549514014e+09'
    assert _ExtendedEncoder().encode(UUID('01234567-89ab-cdef-0123-456789abcdef')) == '"01234567-89ab-cdef-0123-456789abcdef"'
    assert _ExtendedEnc

# Generated at 2022-06-13 19:14:01.627796
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime.utcnow()) == datetime.utcnow().timestamp()
    assert encoder.default(Decimal('12.34')) == '12.34'
    assert encoder.default(set()) == list(set())
    assert encoder.default(UUID('2755fe55-1f38-4384-80f7-6e8d6e2c6004')) == '2755fe55-1f38-4384-80f7-6e8d6e2c6004'
    assert encoder.default(Enum('TEST', 'TEST1 TEST2')) == 'TEST1'



# Generated at 2022-06-13 19:14:06.323578
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({'a': datetime(2019, 12, 8, 16, 41, 8, 549508,
                                                    timezone.utc)}) == '{"a": 1575796868.549508}'



# Generated at 2022-06-13 19:14:54.605882
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default('a') == 'a'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(()) == []
    assert _ExtendedEncoder().default([]) == []
    assert _ExtendedEncoder().default({}) == {}
    assert _ExtendedEncoder().default(set()) == []
    assert _ExtendedEncoder().default(frozenset()) == []
    assert _ExtendedEncoder().default(UUID('7f6f83d6-7dc6-11ea-adc1-0242ac120002')) == '7f6f83d6-7dc6-11ea-adc1-0242ac120002'

# Generated at 2022-06-13 19:15:01.290922
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({}, cls=_ExtendedEncoder) == '{}'
    assert json.dumps([0, 1], cls=_ExtendedEncoder) == '[0, 1]'
    assert json.dumps({0: 'a', 1: 'b'}, cls=_ExtendedEncoder) == '{"0": "a", "1": "b"}'
    assert json.dumps(['a', 'b'], cls=_ExtendedEncoder) == '["a", "b"]'
    assert json.dumps(datetime.now(tz=timezone.utc), cls=_ExtendedEncoder) == '{}'

# Generated at 2022-06-13 19:15:09.027148
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({1: 1.1, 2: 2.2}) == '{"1": 1.1, "2": 2.2}'
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode(datetime.now(tz=timezone.utc)) == '{}'.format(datetime.now().timestamp())
    assert _ExtendedEncoder().encode(datetime.now(tz=timezone.utc).date()) == '"{}"'.format(datetime.now().date())

# Generated at 2022-06-13 19:15:14.847659
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:15:25.623594
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(frozenset([1, 2])) == [1, 2]
    assert encoder.default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(timezone(datetime.timedelta(hours=-5), '-5')) == '-5:00'
    assert encoder.default(datetime(2020, 2, 3, 8, 45, 2, 409130, tzinfo=timezone(datetime.timedelta(hours=-4)))) == 1580723702.409130



# Generated at 2022-06-13 19:15:31.389538
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder(indent=2)

    def assert_equal(x: Json, y: Json):
        assert x == y, f'{x!r} should equal {y!r}'

    # test normal behaviors
    with warnings.catch_warnings(record=True) as w:
        encode_result = encoder.encode([1, 2])
        assert len(w) == 0
        assert_equal(encode_result, '[1, 2]')
    with warnings.catch_warnings(record=True) as w:
        encode_result = encoder.encode([1, '2'])
        assert len(w) == 0
        assert_equal(encode_result, '[1, "2"]')

    # test custom behaviors

# Generated at 2022-06-13 19:15:35.248831
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, tzinfo=timezone.utc)) == "0"
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1)) == "0"


# Generated at 2022-06-13 19:15:44.966122
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    d_in = {"name": "Foo", "age": 20, "gender": 'M'}
    assert _ExtendedEncoder().encode(d_in) == '{"name": "Foo", "age": 20, "gender": "M"}'

    d_out = json.loads(_ExtendedEncoder().encode(d_in), object_hook=cfg.from_dict)
    assert d_out == d_in



# Generated at 2022-06-13 19:15:49.711258
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode(1.1) == '1.1'
    assert _ExtendedEncoder().encode(1) == '1'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({"key": "value"}) == '{"key": "value"}'

# Generated at 2022-06-13 19:15:56.290574
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    def test_encoding(o: Any, result: Any) -> None:
        assert json.loads(json.dumps(o, cls=_ExtendedEncoder)) == result
    test_encoding([1, 2, 3], [1, 2, 3])
    test_encoding({"a": 1}, {"a": 1})
    test_encoding(datetime(2020, 2, 28, 13, 20, 2, 4, timezone.utc),
                  1582919202.000004)
    test_encoding(UUID('c9bf9e57-1685-4c89-b503-e7b5e3d803e3'),
                  'c9bf9e57-1685-4c89-b503-e7b5e3d803e3')


# Generated at 2022-06-13 19:17:28.825893
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default({'a': 123}) == {'a': 123}
    assert encoder.default([123]) == [123]
    assert encoder.default(datetime(2020, 3, 13, 13, 48)) == 1584136880.0
    assert encoder.default(UUID('1234567890abcdef')) == '1234567890abcdef'
    assert encoder.default(Enum('TestEnum', 'a')) == 'a'
    assert encoder.default(Decimal('1.1')) == '1.1'



# Generated at 2022-06-13 19:17:39.101586
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    def checkDefault(o):
        assert isinstance(o, _ExtendedEncoder)
        obj = o.default('str')
        assert obj == 'str'
        obj = o.default(1)
        assert obj == 1
        obj = o.default(1.01)
        assert obj == 1.01
        obj = o.default(True)
        assert obj == True
        obj = o.default(False)
        assert obj == False
        obj = o.default(None)
        assert obj == None
        obj = o.default([])
        assert obj == []
        obj = o.default([1,2,3])
        assert obj == [1,2,3]
        obj = o.default({})
        assert obj == {}
        obj = o.default({'key': 'value'})

# Generated at 2022-06-13 19:17:42.855800
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now())
    assert _ExtendedEncoder().default([1, 2, 3])
    assert _ExtendedEncoder().default({})
    assert _ExtendedEncoder().default(True)
    assert _ExtendedEncoder().default(1)
    assert _ExtendedEncoder().default(3.4)
    assert _ExtendedEncoder().default(UUID('12345678123456781234567812345678'))



# Generated at 2022-06-13 19:17:54.026483
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    test_dict = {'a': 1, 'b': 2}
    test_list = [1, 2, 3]
    assert encoder.default(test_dict) == test_dict
    assert encoder.default(test_list) == test_list
    assert encoder.default(datetime(year=2020, month=3, day=27, hour=9)) == 1585306800.0
    assert encoder.default(UUID('51965b96-fbdb-4367-9d08-c4100f3ee47e')) == '51965b96-fbdb-4367-9d08-c4100f3ee47e'
    class MockEnum(Enum):
        ASDF = 0
        QWER = 1

# Generated at 2022-06-13 19:17:58.814346
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().default(set([1, 2, 3])) == [1, 2, 3]
    assert _ExtendedEncoder().default(123) == 123
    assert _ExtendedEncoder().default(Decimal('123.45')) == '123.45'
    assert _ExtendedEncoder().default(datetime(2019, 12, 31, 23, 59, 59, tzinfo=timezone.utc)) == 1577750399.0
    assert _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'
    assert 'not a real type' in str(_ExtendedEncoder().default(NotImplemented))



# Generated at 2022-06-13 19:18:07.044842
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = {
        'string': 'string',
        'integer': 123,
        'float': 1.23,
        'true': True,
        'false': False,
        'null': None,
        'list': ['a', 'b', 'c'],
        'dict': {'k1': 'v1', 'k2': 'v2'},
        'datetime': datetime(1999, 12, 31, 23, 59, 59, 0, timezone.utc),
        'uuid': UUID('cdc85d2b-4a20-4d66-b291-ffc0be9dfcbf'),
        'enum': ExampleEnum.A,
        'decimal': Decimal('3.14'),
    }

# Generated at 2022-06-13 19:18:13.107113
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
  encoder = _ExtendedEncoder()

  assert encoder.default(MISSING) == MISSING
  assert encoder.default(1.1) == 1.1
  assert encoder.default(['1', '2', '3']) == ['1', '2', '3']
  assert encoder.default({'1': 1, '2': 2, '3': 3}) == {'1': 1, '2': 2, '3': 3}
  assert encoder.default(Enum('TestEnum', 'A B')) == 'A'

# Generated at 2022-06-13 19:18:23.371791
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder()

    class A():
        name = 'A'

    class B():
        name = 'B'
        def default(self, o) -> Json:
            return self.name

    # class A -> {'name': 'A'}
    assert json_encoder.default(A()) == A().__dict__

    # class B -> {'name': 'B'}
    assert json_encoder.default(B()) == 'B'

    # set
    assert json_encoder.default(set([1, 2])) == [1, 2]

    # set
    assert json_encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # datetime

# Generated at 2022-06-13 19:18:33.231295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(1) == 1
    assert encoder.default([True, False]) == [True, False]
    assert encoder.default((1, 2)) == [1, 2]
    assert encoder.default({1: 2}) == {1: 2}
    assert encoder.default(set([1, 2])) == [1, 2]
    assert encoder.default(frozenset([1, 2])) == [1, 2]
    assert encoder.default(datetime(1970, 1, 1, tzinfo=timezone.utc)) == 0
    assert encoder.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'

# Generated at 2022-06-13 19:18:39.628671
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Test the basic behavior
    e = _ExtendedEncoder()
    assert e.default(set()) == []
    assert e.default(frozenset()) == []
    assert e.default(list()) == []
    assert e.default(tuple()) == []
    assert e.default(dict()) == {}
    assert e.default(UUID('{12345678-1234-5678-1234-567812345678}')) == '12345678-1234-5678-1234-567812345678'
    # Note: the following is current behavior but perhaps not desirable long term.
    #       It is not possible to encode these objects with json.dumps() so 
    #       _ExtendedEncoder.default() is not called, and an exception is raised
    # assert e.default(frozenset({