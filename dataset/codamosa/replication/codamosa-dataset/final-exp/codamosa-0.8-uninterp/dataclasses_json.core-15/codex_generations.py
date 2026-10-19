

# Generated at 2022-06-13 19:10:10.974667
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    def test_default(obj, expect):
        changable = copy.deepcopy(obj)
        result = e.default(changable)
        assert result == expect
        assert obj == changable
    test_default([1, 2, 3], [1, 2, 3])
    test_default((1, 2, 3), [1, 2, 3])
    test_default({'a': 1, 'b': 2}, {'a': 1, 'b': 2})
    test_default({'a': [1, 2, 3]}, {'a': [1, 2, 3]})
    test_default(datetime.now(), datetime.now().timestamp())

# Generated at 2022-06-13 19:10:18.761387
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    class TestMapping(Mapping):
        def __init__(self, keys):
            self.keys = keys

        def __getitem__(self, item):
            return item

        def __len__(self):
            return len(self.keys)

        def __iter__(self):
            return iter(self.keys)

    class TestCollection(Collection):
        def __init__(self, values):
            self.values = values

        def __contains__(self, item):
            return item in self.values

        def __iter__(self):
            return iter(self.values)

        def __len__(self):
            return len(self.values)
    class TestClass(object):
        pass

# Generated at 2022-06-13 19:10:27.182508
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    data = [1, 2, 3]
    assert _ExtendedEncoder().encode(data) == json.dumps(data)

    data = {'hello': 'world'}
    assert _ExtendedEncoder().encode(data) == json.dumps(data)

    data = datetime(2019, 8, 8, 12, 22, 22, tzinfo=timezone.utc)
    assert _ExtendedEncoder().encode(data) == json.dumps(data.timestamp())

    data = UUID('123e4567-e89b-12d3-a456-426655440000')
    assert _ExtendedEncoder().encode(data) == json.dumps(str(data))

    class MyEnum(Enum):
        one = 1
        two = 2
    data = MyEn

# Generated at 2022-06-13 19:10:38.165001
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()
    _ExtendedEncoder().default(None)
    _ExtendedEncoder().default(1)
    _ExtendedEncoder().default(1.1)
    _ExtendedEncoder().default([])
    _ExtendedEncoder().default({})
    _ExtendedEncoder().default(set())
    _ExtendedEncoder().default(True)
    _ExtendedEncoder().default(False)
    _ExtendedEncoder().default(datetime.now(timezone.utc))
    _ExtendedEncoder().default(UUID('11111111-1111-1111-1111-111111111111'))
    _ExtendedEncoder().default(Decimal('1.1'))
    _ExtendedEncoder().default(Exception())


# Generated at 2022-06-13 19:10:50.048332
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default((1, 2)) == [1, 2]
    assert encoder.default({'a': 1}) == {'a': 1}
    assert encoder.default(datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp()
    assert encoder.default(UUID('cbfd9e8d-ffb3-42b1-bcef-2ed3e3a5aac0')) == 'cbfd9e8d-ffb3-42b1-bcef-2ed3e3a5aac0'

# Generated at 2022-06-13 19:10:54.361917
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2, 'c': 3}) == '{"a": 1, "b": 2, "c": 3}'

# Unit tests for method encode of class _ExtendedEncoder

# Generated at 2022-06-13 19:11:01.643169
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    json_str = json.dumps({"a": {"b": {"c": [{"d": ['1', 2, 3.0]}]}}})
    assert json_str == '{"a": {"b": {"c": [{"d": ["1", 2, 3.0]}]}}}'



# Generated at 2022-06-13 19:11:10.615520
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({"a": 1, "b": 2, "c": 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert _ExtendedEncoder().encode(UUID("2a6c9d9c-441b-47fa-a2fa-b81f7aa1e89d")) == "\"2a6c9d9c-441b-47fa-a2fa-b81f7aa1e89d\""

# Generated at 2022-06-13 19:11:24.896479
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # Test for output of collections
    test_list = [1, 2, 3]
    result = json.dumps(test_list, cls=_ExtendedEncoder)
    expected = '[1, 2, 3]'
    assert(result == expected)
    
    test_set = set(test_list)
    result = json.dumps(test_set, cls=_ExtendedEncoder)
    expected = '[1, 2, 3]'
    assert(result == expected)
    
    test_dict = {'i': 1, 'j': 2}
    result = json.dumps(test_dict, cls=_ExtendedEncoder)
    expected = '{"i": 1, "j": 2}'
    assert(result == expected)
    
    # Test for output of datetime

# Generated at 2022-06-13 19:11:34.057597
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        o = [1, 2, 3]
        assert _ExtendedEncoder().default(o) == o

        o = {'a': 'b'}
        assert _ExtendedEncoder().default(o) == o

        o = datetime.now(timezone.utc)
        assert _ExtendedEncoder().default(o) == int(o.timestamp())

        o = UUID('{123e4567-e89b-12d3-a456-426655440000}')
        assert _ExtendedEncoder().default(o) == '123e4567e89b12d3a456426655440000'

        o = Decimal('1.2')

# Generated at 2022-06-13 19:12:02.785047
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    json = _ExtendedEncoder().encode({'a': {'b': {'c': 1}}})
    assert json == '{"a": {"b": {"c": 1}}}'
    assert _ExtendedEncoder().encode({'a': 1}) == '{"a": 1}'
    assert _ExtendedEncoder().encode({'a': [1]}) == '{"a": [1]}'
    assert _ExtendedEncoder().encode({'a': {'b': [1]}}) == '{"a": {"b": [1]}}'
    assert _ExtendedEncoder().encode({'a': set()}) == '{"a": []}'
    assert _ExtendedEncoder().encode(set()) == '[]'

# Generated at 2022-06-13 19:12:10.590924
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    assert encoder.default({"":""}) == {"":""}
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(UUID("00000000-0000-0000-0000-000000000000")) == "00000000-0000-0000-0000-000000000000"
    assert encoder.default(True) == True
    assert encoder.default(1) == 1
    assert encoder.default(b"") == ""
    assert encoder.default("") == ""
    assert encoder.default(1.0) == 1.0
    assert encoder.default([1]) == [1]



# Generated at 2022-06-13 19:12:21.694028
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(list('abc')) == list('abc')
    assert _ExtendedEncoder().default(dict(a=1, b=2, c=3)) == {'a': 1, 'b': 2, 'c': 3}
    assert _ExtendedEncoder().default(UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'
    assert _ExtendedEncoder().default(b'bytes') == 'bytes'
    date = datetime(2010, 1, 1, tzinfo=timezone.utc)
    assert _ExtendedEncoder().default(date) == date.timestamp()
    assert _ExtendedEncoder().default(Decimal('1.0')) == '1.0'



# Generated at 2022-06-13 19:12:26.522090
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    res = json.dumps([1, 2, 3.7, {'username': '中文'}, b'\"'], cls=_ExtendedEncoder)
    assert res == '[1, 2, 3.7, {"username": "\u4e2d\u6587"}, "\\""]'



# Generated at 2022-06-13 19:12:31.367088
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    test_values = [list(), dict(), datetime.now(), UUID('{12345678-1234-5678-1234-567812345678}'),
                   Decimal('1.000001')]
    for i in test_values:
        assert _ExtendedEncoder().encode(i)


# Generated at 2022-06-13 19:12:38.287251
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    examples = [
        {"key": [1, 2, 3]},
        ["1", "2", "3"],
        datetime.now(tz=timezone.utc),
        UUID('ffa879b4-4c7c-4a0e-80f8-5f2a5de5bcb4'),
        Decimal('1.23'),
        Enum('TestEnum', [('TestEnum1', '1'), ('TestEnum2', '2')]),
    ]

# Generated at 2022-06-13 19:12:48.772888
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode(None) == 'null'
    assert encoder.encode('abc') == '"abc"'
    assert encoder.encode(123) == '123'
    assert encoder.encode([1, 2, 3]) == '[1, 2, 3]'
    assert encoder.encode({'a': 2, 'c': 3}) == '{"a": 2, "c": 3}'
    assert encoder.encode(datetime(2000, 1, 1)) == '946684800.'

# Generated at 2022-06-13 19:12:57.381824
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    container = ['hello', [1, 'world'], {'key1': 'value1', 'key2': 'value2'}]
    o = encoder.default(container)
    assert isinstance(o, list) and o == container
    o = encoder.default(datetime.now())
    assert isinstance(o, float)
    assert isinstance(encoder.default(UUID('2a9e9261-b0ec-4e33-a6e4-6f13e4b535d3')), str)
    assert isinstance(encoder.default(Decimal('9994.33')), str)
    assert isinstance(encoder.default(1.9), float)
    assert isinstance(encoder.default('string'), str)



# Generated at 2022-06-13 19:13:07.357214
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default({})
    _ExtendedEncoder().default([])
    _ExtendedEncoder().default(set())
    _ExtendedEncoder().default(frozenset())
    _ExtendedEncoder().default(())
    _ExtendedEncoder().default('')
    _ExtendedEncoder().default(0)
    _ExtendedEncoder().default(0.0)
    _ExtendedEncoder().default(False)
    _ExtendedEncoder().default(None)
    _ExtendedEncoder().default(datetime.now())
    _ExtendedEncoder().default(UUID('{12345678-1234-5678-1234567890ab}'))
    _ExtendedEncoder().default(Decimal(1.1))



# Generated at 2022-06-13 19:13:10.090960
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        result = json.dumps([], cls=_ExtendedEncoder)
    assert result == '[]'


# noinspection PyProtectedMember

# Generated at 2022-06-13 19:14:01.684361
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)) == "0.0"
    assert _ExtendedEncoder().encode(datetime(2014, 4, 18, 1, 56, 17, 0, timezone.utc)) == "1397994977.0"
    assert _ExtendedEncoder().encode(UUID("10adc39f-48d1-5647-9a39-c1756febc438")) == '"10adc39f-48d1-5647-9a39-c1756febc438"'
    assert _ExtendedEncoder().encode(None) == "null"
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
   

# Generated at 2022-06-13 19:14:08.497519
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o1 = object()
    o = [o1]
    o2 = object()
    o = {o1: o2}
    o = datetime(2020, 1, 1)  # type: ignore
    o = UUID('00000000-0000-0000-0000-000000000000')
    o = Enum
    o = Decimal('0.0')



# Generated at 2022-06-13 19:14:14.219676
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    x = _ExtendedEncoder()

# Generated at 2022-06-13 19:14:15.765784
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder()



# Generated at 2022-06-13 19:14:21.017019
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.now())
    assert _ExtendedEncoder().encode(UUID('1b371d03-28f2-11ea-adc1-0242ac120002'))
    assert _ExtendedEncoder().encode(1)


# Generated at 2022-06-13 19:14:24.071824
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    values = [['a', 'b'], {'a': 1, 'b': 2}, datetime(2000, 1, 1, tzinfo=timezone.utc)]
    for i in values:
        assert json.loads(json.dumps(i, cls=_ExtendedEncoder)) == i



# Generated at 2022-06-13 19:14:25.413226
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    obj = _ExtendedEncoder()
    assert _issubclass_safe(obj, json.JSONEncoder)


# Generated at 2022-06-13 19:14:32.423099
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # We can't test on plain Python because it may needs
    # more than one imports
    assert json.dumps(1, cls=_ExtendedEncoder) == "1"
    assert json.dumps(1.1, cls=_ExtendedEncoder) == "1.1"
    assert json.dumps(True, cls=_ExtendedEncoder) == "true"
    assert json.dumps(None, cls=_ExtendedEncoder) == "null"
    assert json.dumps([1, 2], cls=_ExtendedEncoder) == "[1, 2]"
    assert json.dumps({"a": 1}, cls=_ExtendedEncoder) == '{"a": 1}'

# Generated at 2022-06-13 19:14:37.576137
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    ee = _ExtendedEncoder()
    assert ee.default([1, 2, 3]) == [1, 2, 3]
    assert ee.default({'a': 1}) == {'a': 1}
    assert ee.default(['a', 'b']) == ['a', 'b']
    assert ee.default(datetime(2020, 5, 23, 17, 59, tzinfo=timezone.utc)) == 1590255940.0
    assert ee.default(UUID(int=0)) == '00000000-0000-0000-0000-000000000000'
    assert ee.default(Decimal('1.23')) == '1.23'



# Generated at 2022-06-13 19:14:42.440363
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    test_data = (
        (list, [], []),
        (dict, {}, {}),
        (datetime, datetime.now(), datetime.now().timestamp()),
        (UUID, UUID('8ff3a5e5-5c5e-4283-8cdb-e21d6c0d6eeb'), '8ff3a5e5-5c5e-4283-8cdb-e21d6c0d6eeb'),
        (Enum, classmethod, classmethod.value),
        (Decimal, Decimal(123.45), '123.45'),
    )
    
    for cls, data, expected_result in test_data:
        result = encoder.default(data)

# Generated at 2022-06-13 19:16:45.256668
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default(): # pylint: disable=unused-variable
    class Test(Enum):
        @classmethod
        def __str__(cls):
            return 'TEST'

        U = 'u'

    assert _ExtendedEncoder().default(Test.U) == Test.U.value



# Generated at 2022-06-13 19:16:49.021781
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(o=datetime(1970, 1, 1, tzinfo=timezone.utc)) == 0.0


# Generated at 2022-06-13 19:17:01.029804
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert _ExtendedEncoder().encode({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert _ExtendedEncoder().encode({'a': 1, 'b': {'a': 1, 'b': 2}}) == '{"a": 1, "b": {"a": 1, "b": 2}}'
    assert _ExtendedEncoder().encode([1, {'a': 1, 'b': 2}, 3]) == "[1, {\"a\": 1, \"b\": 2}, 3]"

# Generated at 2022-06-13 19:17:05.220055
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from decimal import Decimal
    from datetime import datetime
    from uuid import UUID

    obj = [datetime(2019, 3, 4, tzinfo=timezone.utc), UUID('00000000-0000-0000-0000-000000000000'), Decimal('3.14')]
    json.dumps(obj, cls=_ExtendedEncoder)


# Generated at 2022-06-13 19:17:17.554344
# Unit test for constructor of class _ExtendedEncoder

# Generated at 2022-06-13 19:17:27.543334
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert isinstance(encoder.default('foo'), str)
    assert isinstance(encoder.default(dict(foo="bar")), dict)
    assert isinstance(encoder.default(['foo']), list)
    assert isinstance(encoder.default(datetime(2020, 1, 1, 12, 0, 0)), float)
    assert isinstance(encoder.default(UUID('c4a760a8-dbcf-5254-a0d9-6a4474bd1b62')), str)
    assert isinstance(encoder.default(Decimal('1.0')), str)


# Generated at 2022-06-13 19:17:31.719596
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([[["a", "b", "c", "d", "e", "f"]]]) == '[[["a", "b", "c", "d", "e", "f"]]]'

# Generated at 2022-06-13 19:17:33.516273
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    try:
        json.dumps(1, cls=_ExtendedEncoder)
    except Exception as e:
        assert False, str(e)

_EXCLUSION = object()



# Generated at 2022-06-13 19:17:38.150595
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default({1:2}) == {1:2}
    assert encoder.default([1,2]) == [1,2]
    assert encoder.default(UUID(int=1)) == '00000000-0000-0000-0000-000000000001'
    assert encoder.default(datetime(1,1,1,1,1,1,1, timezone(timedelta(days=1)))) == -62135596800.001
    assert encoder.default(Enum('Foo', [(1,2)])) == 1
    assert encoder.default(Decimal('3.14')) == '3.14'
    assert encoder.default(object()) == 'Object'


# Generated at 2022-06-13 19:17:44.317869
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.default({}) == {}
    assert e.default([]) == []
    assert e.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()
    assert e.default(UUID('27a9d938-b839-4eac-afce-1daf1431a098')) == '27a9d938-b839-4eac-afce-1daf1431a098'
    class Bar:
        def __init__(self, x: int) -> None:
            self.x = x
        def __repr__(self) -> str:
            return f'Bar({self.x})'
    assert e.default(Bar(1)) == Bar(1).__