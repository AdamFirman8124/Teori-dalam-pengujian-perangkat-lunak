

# Generated at 2022-06-13 19:10:08.017583
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from datetime import datetime
    from uuid import UUID
    from dataclasses_json.undefined import Undefined  # type: ignore
    assert _ExtendedEncoder.default(None, Undefined) is Undefined
    assert _ExtendedEncoder.default(None, [Undefined, Undefined]) == [Undefined, Undefined] # type: ignore
    assert _ExtendedEncoder.default(None, tuple(range(3))) == list(range(3))
    assert _ExtendedEncoder.default(None, datetime.now())
    assert _ExtendedEncoder.default(None, UUID(int=0))



# Generated at 2022-06-13 19:10:15.654086
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert 'true' == _ExtendedEncoder().encode(True)
    assert '1' == _ExtendedEncoder().encode(1)
    assert '1.1' == _ExtendedEncoder().encode(1.1)
    assert '["a", "b"]' == _ExtendedEncoder().encode(['a', 'b'])
    assert '{"a": "a", "b": "b"}' == _ExtendedEncoder().encode({'a': 'a', 'b': 'b'})
    assert '1' == _ExtendedEncoder().encode(Decimal('1.0'))
    assert '"1"' == _ExtendedEncoder().encode(Decimal('1.0'), ensure_ascii=False)

# Generated at 2022-06-13 19:10:25.506958
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    def test_json_dumps_extended(json_obj, expected):
        assert _ExtendedEncoder().encode(json_obj) == expected

    # Test the datetime conversion to float
    test_json_dumps_extended(datetime(2019, 12, 20, 22, 15, 59, tzinfo=timezone.utc), "1577012959.0")
    test_json_dumps_extended(
        datetime(2019, 12, 20, 22, 15, 59, 123456, tzinfo=timezone.utc), "1577012959.123456"
    )
    # Test the extended UUID conversion to str

# Generated at 2022-06-13 19:10:38.073475
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode(datetime(2014, 5, 1, 12, 30)) == \
        '1401363400.0'
    assert _ExtendedEncoder().encode(datetime(2014, 5, 1, 12, 30, tzinfo=timezone.utc)) == \
        '1401363400.0'

# Generated at 2022-06-13 19:10:47.133643
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc))
    assert _ExtendedEncoder().default(UUID('14e9c23e-a8ca-4e1f-b0e6-bc0bc8c7a79a'))
    assert _ExtendedEncoder().default(datetime(year=2020, month=12, day=31, hour=23, minute=59, second=59, tzinfo=timezone.utc))
    assert _ExtendedEncoder().default(Decimal('1.234'))



# Generated at 2022-06-13 19:10:55.909578
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode('{}') == '"{}"'
    assert _ExtendedEncoder().encode(1.1) == '1.1'
    assert _ExtendedEncoder().encode(True) == 'true'
    assert _ExtendedEncoder().encode(False) == 'false'
    assert _ExtendedEncoder().encode(None) == 'null'
    assert _ExtendedEncoder().encode({1: 2}) == '{"1": 2}'
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'

# Generated at 2022-06-13 19:11:11.009763
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert(_ExtendedEncoder().encode([1,2,3]) == '[1, 2, 3]')
    assert(_ExtendedEncoder().encode(dict(a=1)) == '{"a": 1}')
    assert(_ExtendedEncoder().encode(datetime(2020,2,2,20,46)) == '1583215860.0')
    assert(_ExtendedEncoder().encode(UUID("db8b8f08-7703-4c9f-84de-8c09b2e2e3f3")) == '"db8b8f08-7703-4c9f-84de-8c09b2e2e3f3"')
    assert(_ExtendedEncoder().encode(Decimal("1.1")) == '"1.1"')

# Generated at 2022-06-13 19:11:16.813830
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default(frozenset([1, 2])) == [1, 2]
    assert e.default({1: 2}) == {1: 2}
    assert e.default(datetime(2020, 10, 1, 1, 2, 3, 0, timezone.utc)) == 1601577323.0
    assert e.default(UUID('bc547e82-2ea2-11ea-82c8-acde48001122')) == 'bc547e82-2ea2-11ea-82c8-acde48001122'
    assert e.default(Decimal(0.2)) == '0.2'



# Generated at 2022-06-13 19:11:21.224955
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(Decimal('45.5')) == "45.5"
    assert encoder.default([1,2,3,4]) == [1,2,3,4]
    assert encoder.default({"key":"value"}) == {"key":"value"}
    assert encoder.default(datetime.now(timezone.utc)) == \
           datetime.now(timezone.utc).timestamp()
    assert encoder.default({"key": datetime.now(timezone.utc)}) == \
           {"key": datetime.now(timezone.utc).timestamp()}

# Generated at 2022-06-13 19:11:22.141606
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:11:44.796862
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(Decimal('3.14')) == '3.14'
    assert encoder.default(datetime.now()) == 1561702674.471759
    assert encoder.default(datetime.now(timezone.utc)) == 1561702674.471409



# Generated at 2022-06-13 19:11:46.292961
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # type: () -> None
    assert _ExtendedEncoder().encode("hello") == '"hello"'



# Generated at 2022-06-13 19:11:56.033826
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default([]) == []
    assert e.default({}) == {}
    assert e.default(set()) == []
    assert e.default(frozenset()) == []
    assert e.default(datetime(2020, 1, 1, 12, 30, 0, 0, timezone.utc)) == 1577823400.0
    assert e.default(UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'
    assert e.default(Enum) == Enum
    assert e.default(Decimal(5)) == '5'
    assert e.default('foo') == 'foo'


# Generated at 2022-06-13 19:12:04.339961
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([3, 1, 4]) == '[3, 1, 4]'
    assert _ExtendedEncoder().encode({1: 2, 3: 4}) == '{"1": 2, "3": 4}'
    assert _ExtendedEncoder().encode([1, {2: 3}, [4, 5], 6]) == '[1, {"2": 3}, [4, 5], 6]'
    assert _ExtendedEncoder().encode(set(range(10))) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
    assert _ExtendedEncoder().encode(frozenset(range(10))) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'

# Generated at 2022-06-13 19:12:11.377221
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ex_encoder = _ExtendedEncoder()
    assert type(ex_encoder.default(dict())) == dict
    assert type(ex_encoder.default(list())) == list
    assert type(ex_encoder.default(set())) == list
    assert type(ex_encoder.default(frozenset())) == list
    assert isinstance(ex_encoder.default(1), int)
    assert isinstance(ex_encoder.default(1.0), float)
    assert isinstance(ex_encoder.default(True), bool)
    assert isinstance(ex_encoder.default(None), bool)
    assert isinstance(ex_encoder.default("a"), str)
    assert ex_encoder.default(uuid.uuid4()) == str(uuid.uuid4())
   

# Generated at 2022-06-13 19:12:18.788004
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([None, 1, [], [], {'a': 1}, datetime.now(), UUID('00000000-0000-0000-0000-000000000001'), Enum('Test', {'A': 1}), Decimal('1.1')]) == '[null,1,[],[],{"a":1},1593320466.777601,00000000-0000-0000-0000-000000000001,1,"1.1"]'



# Generated at 2022-06-13 19:12:25.656136
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    enc = _ExtendedEncoder()
    assert enc.default(list()) == []
    assert enc.default(dict()) == {}
    assert enc.default(True) == True
    assert enc.default(False) == False
    assert enc.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert enc.default(UUID("b0d800e7-0f1e-4b27-98a6-f064a940501f")) == "b0d800e7-0f1e-4b27-98a6-f064a940501f"
    assert enc.default(Decimal("3.14")) == "3.14"
    assert enc.default("other") == "other"

# Generated at 2022-06-13 19:12:35.011182
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    js = json.dumps([1, 2, 3], cls=_ExtendedEncoder)
    assert js == '[1, 2, 3]'

    js = json.dumps(((1, 2), (3, 4)), cls=_ExtendedEncoder)
    assert js == '[[1, 2], [3, 4]]'

    js = json.dumps(dict(a=1, b=2), cls=_ExtendedEncoder)
    assert js == '{"a": 1, "b": 2}'

    d = datetime.now(timezone.utc)
    js = json.dumps(d, cls=_ExtendedEncoder)
    assert js == str(d.timestamp())


# Generated at 2022-06-13 19:12:39.345129
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(list([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(dict({1: 2, 3: 4})) == {1: 2, 3: 4}


# Generated at 2022-06-13 19:12:44.029190
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json_encoder = _ExtendedEncoder(indent=4, sort_keys=True)
    utc_now = datetime.now(timezone.utc)
    example = {
        'datetime': utc_now,
        'list': [1, 2, 3, 4],
        'tuple': (5, 6, 7, 8),
        'dict': {'a': 1, 'b': 2},
        'set': {9, 10},
        'frozenset': frozenset([11, 12]),
        'uuid': UUID('2d2a9b88-b38c-428a-a145-aa1999f017c5'),
        'enum': Color.RED,
        'Decimal': Decimal('1.1'),
    }


# Generated at 2022-06-13 19:13:32.824400
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    a = json.dumps(-2, cls=_ExtendedEncoder)
    b = '-2'
    assert a == b

    a = json.dumps(2.2, cls=_ExtendedEncoder)
    b = '2.2'
    assert a == b

    a = json.dumps('a', cls=_ExtendedEncoder)
    b = '"a"'
    assert a == b

    a = json.dumps(True, cls=_ExtendedEncoder)
    b = 'true'
    assert a == b

    a = json.dumps(None, cls=_ExtendedEncoder)
    b = 'null'
    assert a == b

    a = json.dumps({'a': 'b'}, cls=_ExtendedEncoder)

# Generated at 2022-06-13 19:13:34.111421
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = {'a': 1, 'b': set(), 'c': [1, 2]}
    json.dumps(o, cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:13:44.548607
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Construct _ExtendedEncoder.
    _ExtendedEncoder()

_EXTENDED_ENCODER = _ExtendedEncoder()



# Generated at 2022-06-13 19:13:51.288960
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps(dict(a=1), cls=_ExtendedEncoder) == '{"a": 1}'
    assert json.dumps(list(range(10)), cls=_ExtendedEncoder) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
    assert json.dumps(datetime.now(), cls=_ExtendedEncoder) == json.dumps(datetime.now().timestamp())
    assert json.dumps(UUID('{12345678-1234-5678-1234-567812345678}'), cls=_ExtendedEncoder) == '"{12345678-1234-5678-1234-567812345678}"'

# Generated at 2022-06-13 19:13:57.601418
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.0) == 1.0
    assert _ExtendedEncoder().default('abc') == 'abc'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default(1.0) == 1.0
    assert _ExtendedEncoder().default('abc') == 'abc'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False
    assert _ExtendedEncoder().default(None) == None
    # Testing Collections

# Generated at 2022-06-13 19:13:59.055822
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:14:08.034046
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from dataclasses import dataclass, field
    import datetime
    from uuid import UUID
    from enum import Enum
    from decimal import Decimal
    from collections import namedtuple
    @dataclass
    class D:
        a: str = "a"
        b: datetime = field(default_factory=datetime.datetime.now)
        c: UUID = field(default_factory=lambda: UUID("b32aee42-d8f5-4e47-a0ca-ac2365a8b30a"))
        d: Enum = field(default_factory=lambda: EnumData(1))
        e: Decimal = field(default_factory=lambda: Decimal('3.14'))

# Generated at 2022-06-13 19:14:14.047416
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default(None) == None
    assert encoder.default(True) == True
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0
    assert encoder.default(1.2) == 1.2
    assert encoder.default('str') == 'str'
    assert encoder.default({'a':'b'}) == {'a':'b'}
    assert encoder.default(set()) == list()
    assert encoder.default({1,2,3}) == [1,2,3]
    assert encoder.default(frozenset()) == list()
    assert encoder.default(datetime.now()) == datetime.now().timestamp()

# Generated at 2022-06-13 19:14:24.192777
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = {
        'first': [1, 2, 3],
        'second': [{'a': 1}, {'b': 2}, {'c': 3}],
        'third': {'a': 1},
        'fourth': 'str',
        'fifth': b'bytes',
        'sixth': 1,
        'seventh': 1.0,
        'eighth': True,
        'ninth': None,
        'tenth': datetime.now(timezone.utc),
        'eleventh': UUID('12345678123456781234567812345678'),
        'twelfth': Decimal('3.14'),
    }
    assert json.loads(json.dumps(data, cls=_ExtendedEncoder)) == data



# Generated at 2022-06-13 19:14:25.306741
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()

_extended_encoder = _ExtendedEncoder()



# Generated at 2022-06-13 19:15:28.931683
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({'a': 'b'}, cls=_ExtendedEncoder) == '{"a": "b"}'
    assert json.dumps({'a': 'b'}, sort_keys=True, cls=_ExtendedEncoder) == '{"a": "b"}'
    assert json.dumps([{'a': 'b'}], cls=_ExtendedEncoder) == '[{"a": "b"}]'
    assert json.dumps(['c', 'd'], cls=_ExtendedEncoder) == '["c", "d"]'
    assert json.dumps(defaultdict(list, {'a': 'b'}), cls=_ExtendedEncoder) == '{"a": "b"}'

# Generated at 2022-06-13 19:15:40.484713
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:15:47.721212
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    d = json.dumps(42, cls=_ExtendedEncoder)
    assert d == '42'
    d = json.dumps({42: 42}, cls=_ExtendedEncoder)
    assert d == '{"42": 42}'
    d = json.dumps([42], cls=_ExtendedEncoder)
    assert d == '[42]'
    d = json.dumps('test string', cls=_ExtendedEncoder)
    assert d == '"test string"'
    # the date time is converted to timestamp (float value)
    t = datetime.now()
    d = json.dumps(t, cls=_ExtendedEncoder)
    assert isinstance(json.loads(d), float)
    # the UUID is converted to string (str value)

# Generated at 2022-06-13 19:15:55.657318
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(Decimal('0.5')) == '0.5'
    assert _ExtendedEncoder().default(Enum('TestEnum', 'a b')) == 'a'
    assert _ExtendedEncoder().default(1) == '1'
    assert _ExtendedEncoder().default(None) is None
    assert _ExtendedEncoder().default(type(None)) is None
    assert _ExtendedEncoder().default(float('nan')) == 'NaN'
    assert _ExtendedEncoder().default(float('inf')) == 'Infinity'
    assert _ExtendedEncoder().default(float('-inf')) == '-Infinity'
    assert _ExtendedEncoder().default(datetime(2000, 11, 13, 13, 13, 13)) == 973186193.0


# Generated at 2022-06-13 19:16:02.608155
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default((1, 2)) == [1, 2]
    assert encoder.default({1: 'a', 2: 'b'}) == {1: 'a', 2: 'b'}
    assert encoder.default(datetime(2019, 12, 31, 13, 23, 45, tzinfo=timezone.utc)) == datetime(2019, 12, 31, 13, 23, 45, tzinfo=timezone.utc).timestamp()

# Generated at 2022-06-13 19:16:06.462106
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([datetime.now(), UUID('123'), 2, Decimal(1.1)]) == "[1542080320.000685, \"123\", 2, \"1.1\"]"



# Generated at 2022-06-13 19:16:07.590247
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    import json
    json.dumps(set(), cls=_ExtendedEncoder)



# Generated at 2022-06-13 19:16:09.450144
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    result = json.dumps(set([1, 2, 3]), cls=_ExtendedEncoder)
    assert result == json.dumps([1, 2, 3])



# Generated at 2022-06-13 19:16:14.930155
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ext_encoder = _ExtendedEncoder()

    assert ext_encoder.default(None) == None
    assert ext_encoder.default(True) == True
    assert ext_encoder.default(False) == False
    assert ext_encoder.default(1) == 1
    assert ext_encoder.default(1.1) == 1.1
    assert ext_encoder.default("hello") == "hello"
    assert ext_encoder.default(list()) == list()
    assert ext_encoder.default(dict()) == dict()
    assert ext_encoder.default(datetime(2020, 1, 1, tzinfo=timezone.utc)) == 1577833200

# Generated at 2022-06-13 19:16:26.975989
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null', 'Unexpected result of _ExtendedEncoder().encode(None)'
    assert _ExtendedEncoder().encode(123) == '123', 'Unexpected result of _ExtendedEncoder().encode(123)'
    assert _ExtendedEncoder().encode(123.456) == '123.456', 'Unexpected result of _ExtendedEncoder().encode(123.456)'
    assert _ExtendedEncoder().encode(123.456e79) == '1.23456e+81', 'Unexpected result of _ExtendedEncoder().encode(123.456e79)'
    assert _ExtendedEncoder().encode(True) == 'true', 'Unexpected result of _ExtendedEncoder().encode(True)'
    assert _ExtendedEncoder().en

# Generated at 2022-06-13 19:18:32.107510
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({"a": [1, 2, 3]}, cls=_ExtendedEncoder) == '{"a": [1, 2, 3]}'
    assert json.dumps({"a": {"b": "c"}}, cls=_ExtendedEncoder) == '{"a": {"b": "c"}}'
    t = datetime.now(timezone.utc)
    assert json.dumps({"a": t}, cls=_ExtendedEncoder) == '{"a": ' + str(t.timestamp()) + '}'

# Generated at 2022-06-13 19:18:34.686463
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default({'a': 1}) == {'a': 1}
    assert _ExtendedEncoder().default(('a',)) == ['a']
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]


# Generated at 2022-06-13 19:18:40.849732
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([0, 1, 2]) == [0, 1, 2]
    assert encoder.default({'a': 3, 'b': 4}) == {'a': 3, 'b': 4}
    assert encoder.default('abc') == 'abc'
    assert encoder.default(3.14) == 3.14
    assert encoder.default(True) == True
    assert encoder.default(None) == None
    assert encoder.default(datetime(2020,3,4,0,0)) == 1583315200.0
    assert encoder.default(datetime(2020,3,4,0,0, tzinfo=timezone.utc)) == 1583315200.0

# Generated at 2022-06-13 19:18:45.262892
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == json.dumps(datetime.now(timezone.utc).timestamp())
    assert _ExtendedEncoder().encode(UUID('d8ac038b-c594-4a9d-8e8a-61b6c5e6d5e6')) == '"d8ac038b-c594-4a9d-8e8a-61b6c5e6d5e6"'

# Generated at 2022-06-13 19:18:55.252157
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from datetime import datetime
    from dataclasses import dataclass
    from dataclasses_json import DataClassJsonMixin

    @dataclass
    class Klass(DataClassJsonMixin):
        a: int
        b: int
        c: str
        d: datetime
    obj = Klass(a=1, b=2, c='str', d=datetime(2019, 5, 17, 1, 2, 3, tzinfo=timezone.utc))
    result = _ExtendedEncoder().default(obj)
    assert isinstance(result, dict)
    assert len(result) == 4
    assert result['a'] == 1
    assert result['b'] == 2
    assert result['c'] == 'str'
    assert result['d'] == 1557933123.0


_PROT

# Generated at 2022-06-13 19:19:06.156333
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps({'x': []}, cls=_ExtendedEncoder) == '{"x": []}'
    assert json.dumps({'x': {}}, cls=_ExtendedEncoder) == '{"x": {}}'
    assert json.dumps({'x': datetime.now(timezone.utc)}, cls=_ExtendedEncoder) == '{"x":' in json.dumps({'x': datetime.now(timezone.utc)}, cls=_ExtendedEncoder)
    assert json.dumps({'x': UUID('{12345678-1234-5678-1234-567812345678}')}, cls=_ExtendedEncoder) == '{"x": "12345678-1234-5678-1234-567812345678"}'


# Generated at 2022-06-13 19:19:12.568837
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode(datetime(2019, 7, 30, 13, 41, 12, 13)) == "1564559672.000013"
    assert _ExtendedEncoder().encode(datetime(2019, 7, 30, 13, 41, 12, 13, timezone.utc)) == "1564559672.000013"

# Generated at 2022-06-13 19:19:16.364845
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()

# Generated at 2022-06-13 19:19:22.947668
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(Decimal('12.34')) == '"12.34"'
    assert _ExtendedEncoder().encode(dict(a=1)) == '{"a": 1}'
    assert _ExtendedEncoder().encode(list(range(3))) == '[0, 1, 2]'
    assert _ExtendedEncoder().encode(UUID('74124e17-d8c6-4b1e-8c44-ff7e9f6c33ff')) == \
            '"74124e17-d8c6-4b1e-8c44-ff7e9f6c33ff"'



# Generated at 2022-06-13 19:19:30.200886
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import datetime
    from uuid import UUID
    from decimal import Decimal

    json.dumps(set(), cls=_ExtendedEncoder)
    json.dumps(frozenset(), cls=_ExtendedEncoder)
    json.dumps(range(0), cls=_ExtendedEncoder)
    json.dumps({}, cls=_ExtendedEncoder)
    json.dumps(set(), cls=_ExtendedEncoder)
    json.dumps(frozenset(), cls=_ExtendedEncoder)
    json.dumps(range(0), cls=_ExtendedEncoder)
    json.dumps(datetime(year=2017, month=2, day=1), cls=_ExtendedEncoder)