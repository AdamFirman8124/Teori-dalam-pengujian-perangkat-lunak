

# Generated at 2022-06-13 19:10:04.003598
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default({}) == {}
    assert encoder.default([]) == []
    assert encoder.default(set()) == []
    assert encoder.default(frozenset()) == []
    assert encoder.default(datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 0.0
    assert encoder.default(UUID('00000000-0000-0000-0000-000000000000')) == '00000000-0000-0000-0000-000000000000'



# Generated at 2022-06-13 19:10:07.486680
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    expected = {'a': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()}
    actual = json.dumps(expected, cls=_ExtendedEncoder)
    assert actual == '{"a": "%s"}' % expected['a']



# Generated at 2022-06-13 19:10:15.221042
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    from datetime import date
    from decimal import Decimal
    from enum import IntEnum
    from uuid import UUID
    from collections import deque


# Generated at 2022-06-13 19:10:24.504602
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()

    assert encoder.default([1, 2]) == [1, 2]
    assert encoder.default([1, 2, datetime(2019, 10, 10, tzinfo=timezone.utc)]) == [1, 2, 1570734400.0]
    encoder.default(UUID('4b4e6df4-3e5e-4c1d-b9f9-1d1acf362a35')) == '4b4e6df4-3e5e-4c1d-b9f9-1d1acf362a35'
    with pytest.raises(TypeError):
        encoder.default(5)



# Generated at 2022-06-13 19:10:26.083559
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) > 0



# Generated at 2022-06-13 19:10:35.913215
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.encode(datetime.strptime('January 1, 2000', '%B %d, %Y')) == '946684800.0'
    assert encoder.encode(Decimal('3.1')) == '"3.1"'
    assert encoder.encode(UUID('24832e5e-c051-40a1-b5d2-8cd36f02050b')) == '"24832e5e-c051-40a1-b5d2-8cd36f02050b"'



# Generated at 2022-06-13 19:10:41.319736
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()

# Generated at 2022-06-13 19:10:52.305637
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    # check if non-standard types are converted correctly
    _ExtendedEncoder().encode(set([1, 2, 3])) == '[1,2,3]'
    _ExtendedEncoder().encode(frozenset([1, 2, 3])) == '[1,2,3]'
    _ExtendedEncoder().encode(defaultdict(lambda: 1, {'a': 1})) == '{"a":1}'
    _ExtendedEncoder().encode({1, 2, 3}) == '[1,2,3]'
    _ExtendedEncoder().encode({'a': 1}) == '{"a":1}'
    _ExtendedEncoder().encode(datetime.now(timezone.utc)) == datetime.now().timestamp()

# Generated at 2022-06-13 19:10:57.327787
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(Decimal("1")) == "1"
    assert encoder.default(datetime(2019, 2, 1)) == datetime(2019, 2, 1).timestamp()
    assert encoder.default(UUID("12345678-1234-5678-1234-567812345678")) == "12345678-1234-5678-1234-567812345678"

# Decimal(1) == Decimal("1")
# assert encoder.encode([Decimal(1)]) == encoder.encode([Decimal("1")])



# Generated at 2022-06-13 19:11:11.526718
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    ee = _ExtendedEncoder()
    # Python 3.6 and 3.7 return different values from default
    assert ee.default(None) == 'null'
    assert ee.default(True) == 'true'
    assert ee.default(False) == 'false'
    assert ee.default(0) == '0'
    assert ee.default(1) == '1'
    assert ee.default(0.0) == '0.0'
    assert ee.default(1.0) == '1.0'
    assert ee.default('') == '""'
    assert ee.default('a') == '"a"'
    assert ee.default([]) == '[]'
    assert ee.default([1, 2]) == '[1, 2]'
    assert ee.default

# Generated at 2022-06-13 19:11:38.807791
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(0.5) == "0.5"
    assert _ExtendedEncoder().encode(123) == "123"
    assert _ExtendedEncoder().encode(True) == "true"


# Generated at 2022-06-13 19:11:48.330366
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([0,1,2]) == '[0, 1, 2]'
    assert _ExtendedEncoder().encode(['a', 'b', 'c']) == '["a", "b", "c"]'
    assert _ExtendedEncoder().encode({1:'a', 2:'b', 3:'c'}) == '{"1": "a", "2": "b", "3": "c"}'
    assert _ExtendedEncoder().encode(datetime(2020,1,2,3,4,5,6, timezone.utc)) == '1577835245.000006'

# Generated at 2022-06-13 19:11:56.824482
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([1,2,3]) == [1,2,3]
    assert encoder.default({"a":1}) == {"a":1}
    assert encoder.default(Decimal("1.2")) == "1.2"
    assert encoder.default(UUID("00000000-0000-0000-0000-000000000000")) == "00000000-0000-0000-0000-000000000000"
    assert encoder.default(datetime.now(timezone.utc)) == datetime.now(timezone.utc).timestamp()


# Generated at 2022-06-13 19:12:05.014177
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from .utils import _isinstance_safe
    from collections import OrderedDict
    from datetime import datetime
    from uuid import UUID
    from decimal import Decimal
    e = _ExtendedEncoder()
    assert e.default(UUID('6e0c6f83-f9fe-11e8-8eb2-f2801f1b9fd1')) == '6e0c6f83-f9fe-11e8-8eb2-f2801f1b9fd1'
    assert e.default(decimal.Decimal('1.1')) == '1.1'
    assert e.default(datetime(2018, 10, 2, 3, 4, 5)) == 1538403845.0

# Generated at 2022-06-13 19:12:10.028597
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(2) == 2
    assert _ExtendedEncoder().default(2.2) == 2.2
    assert _ExtendedEncoder().default('a') == 'a'
    assert _ExtendedEncoder().default(UUID('6ba47ce8-8f73-4d6f-b6f2-8e8c0895da70')) == '6ba47ce8-8f73-4d6f-b6f2-8e8c0895da70'
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == datetime.now().timestamp()
    assert _ExtendedEncoder().default({1: '1'}) == {1: '1'}

# Generated at 2022-06-13 19:12:21.540026
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    now = datetime.now()
    uid = UUID("967cff0b-c2b8-4b07-8822-ec47d1f56086")
    my_enum = cfg.LetterCase.CAMEL

    assert _ExtendedEncoder().encode({'a': [1,2,3]}) == '{"a": [1, 2, 3]}'
    assert _ExtendedEncoder().encode({'a': {'b': 'c'}}) == '{"a": {"b": "c"}}'
    assert _ExtendedEncoder().encode(datetime(2018, 9, 3, 0, 5)) == '1535886100.0'
    assert _ExtendedEncoder().encode(now) == str(now.timestamp())

# Generated at 2022-06-13 19:12:32.676137
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.dumps([], cls=_ExtendedEncoder) == '[]'
    assert json.dumps({}, cls=_ExtendedEncoder) == '{}'
    assert json.dumps(datetime(2019, 2, 3, 4, 5, 6, 7, tzinfo=timezone.utc), cls=_ExtendedEncoder) == '1549239906.000007'
    assert json.dumps(UUID('a95d1ec2-8e39-4b6b-b14d-1b2f90b44e97'), cls=_ExtendedEncoder) == '"a95d1ec2-8e39-4b6b-b14d-1b2f90b44e97"'

# Generated at 2022-06-13 19:12:42.286892
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    assert encoder.default([None]) == [None]
    assert encoder.default((None,)) == [None]
    assert encoder.default({"a":None}) == {"a":None}
    assert encoder.default(None) == None
    assert encoder.default(False) == False
    assert encoder.default(True) == True
    assert encoder.default(0) == 0
    assert encoder.default(0.123) == 0.123
    assert encoder.default("Hello") == "Hello"
    assert encoder.default(datetime.now()) == datetime.now().timestamp()
    assert encoder.default(UUID("046b6c7f-0b8a-43b9-b35d-6489e6daee91")) == str

# Generated at 2022-06-13 19:12:51.955810
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    from io import StringIO
    from typing import List
    class MyList(List):
        pass
    from dataclasses import dataclass
    from uuid import uuid4
    from decimal import Decimal
    @dataclass
    class MyClass:
        my_list: List[int] = [1, 2]
        my_set: set = {1, 2}
        my_dict: dict = {'a': 1, 'b': 2}
        my_uuid: UUID = uuid4()
        my_dec: Decimal = Decimal(1.5)
        my_MyList: MyList = MyList([1, 2])

    my_instance = MyClass()
    print(my_instance)
    print(type(my_instance.my_list))

# Generated at 2022-06-13 19:13:01.768817
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(1) == 1
    _ExtendedEncoder().default(dict(a=1, b=2)) == dict(a=1, b=2)
    _ExtendedEncoder().default(list('a')) == ['a']
    _ExtendedEncoder().default('a') == 'a'
    _ExtendedEncoder().default(Decimal(1)) == '1'
    _ExtendedEncoder().default(datetime(2020, 1, 1)) > 1577836800
    _ExtendedEncoder().default(datetime(2020, 1, 1)) < 1577923200



# Generated at 2022-06-13 19:13:47.593017
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode([]) == '[]'



# Generated at 2022-06-13 19:13:54.046924
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(datetime(2019, 12, 2, tzinfo=timezone.utc)) == 1575374400.0
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default(123) == 123
    assert _ExtendedEncoder().default({'a': 1}) == {'a': 1}
    assert _ExtendedEncoder().default(UUID('dd6c669c-eefc-4899-be87-b47a34b05f69')) == 'dd6c669c-eefc-4899-be87-b47a34b05f69'



# Generated at 2022-06-13 19:13:59.625008
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert list(json.JSONEncoder().encode([datetime(2002, 10, 27, 12, 0, 0)])) == '["2002-10-27T12:00:00"]'
    assert list(json.JSONEncoder().encode([UUID('12345678123456781234567812345678')])) == '["12345678-1234-5678-1234-567812345678"]'
    assert list(json.JSONEncoder().encode([Enum('TestEnum', {'A':1})()])) == '["A"]'
    assert list(json.JSONEncoder().encode([Decimal('10.5')])) == '["10.5"]'
    assert list(json.JSONEncoder().encode([10.5])) == '[10.5]'


# Generated at 2022-06-13 19:14:08.224838
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder.default(
        _ExtendedEncoder(), [0, 1, 2, 3]) == [0, 1, 2, 3]
    assert _ExtendedEncoder.default(
        _ExtendedEncoder(), [0, 1, 2, 3]) == [0, 1, 2, 3]
    assert _ExtendedEncoder.default(
        _ExtendedEncoder(), {'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _ExtendedEncoder.default(
        _ExtendedEncoder(), Decimal('2.12345678901234567890')) == '2.12345678901234567890'

# Generated at 2022-06-13 19:14:09.655230
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    obj = _ExtendedEncoder()
    assert isinstance(obj, _ExtendedEncoder)


# Generated at 2022-06-13 19:14:14.864068
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    _ExtendedEncoder().default(1.2)
    _ExtendedEncoder().default(True)
    _ExtendedEncoder().default('a string')
    _ExtendedEncoder().default(list())
    _ExtendedEncoder().default(tuple())
    _ExtendedEncoder().default(set())
    _ExtendedEncoder().default(dict())
    _ExtendedEncoder().default(object())



# Generated at 2022-06-13 19:14:23.050761
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(datetime.utcnow())
    assert _ExtendedEncoder().encode(UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479'))
    assert _ExtendedEncoder().encode(Enum('Test', ['X']))
    assert _ExtendedEncoder().encode(Decimal('1.2345'))

_ENCODER = _ExtendedEncoder()
_TZ = timezone.utc



# Generated at 2022-06-13 19:14:30.217202
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([1, 2]) == '[1, 2]'
    assert _ExtendedEncoder().encode({'1': 2}) == '{"1": 2}'
    assert _ExtendedEncoder().encode(datetime.now(timezone.utc)) == 'null'
    assert (_ExtendedEncoder().encode(UUID('5d1e05e2-c55d-4c4e-9d0f-6b854301df57'))
            == '"5d1e05e2-c55d-4c4e-9d0f-6b854301df57"')
    assert _ExtendedEncoder().encode(Decimal('0.01')) == '"0.01"'



# Generated at 2022-06-13 19:14:31.228425
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(None) == 'null'


# Generated at 2022-06-13 19:14:37.547249
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    e = _ExtendedEncoder()
    assert e.encode([1, 2, 3]) == '[1, 2, 3]'
    assert e.encode({'a': 1}) == '{"a": 1}'
    assert e.encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert e.encode({1, 2, 3}) == '[1, 2, 3]'
    assert e.encode(frozenset({1, 2, 3})) == '[1, 2, 3]'
    assert e.encode(datetime.now(tz=timezone.utc)) == str(datetime.now(tz=timezone.utc).timestamp())
    assert e.encode(UUID(int=1)) == '00000000-0000-0000-0000-000000000001'
    assert e

# Generated at 2022-06-13 19:16:43.491237
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode([]) == '[]'
    assert _ExtendedEncoder().encode({}) == '{}'
    assert _ExtendedEncoder().encode({1: 1, 2: 2}) == '{"1": 1, "2": 2}'
    assert _ExtendedEncoder().encode(['a', 'b', 'c']) == '["a", "b", "c"]'
    assert (str(_ExtendedEncoder().encode(
        datetime(1970, 1, 1, tzinfo=timezone.utc))) == '0.0')
    assert _ExtendedEncoder().encode(
        UUID('12345678123456781234567812345678')) == '"12345678-1234-5678-1234-567812345678"'
    assert _

# Generated at 2022-06-13 19:16:45.457331
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert json.loads(json.dumps(set([1, 2, 3]), cls=_ExtendedEncoder)) == [1, 2, 3]



# Generated at 2022-06-13 19:16:58.645289
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().encode(set([1, 2, 3])) == '[1, 2, 3]'
    assert _ExtendedEncoder().encode({'a': 1, 'b': None}) == '{"a": 1, "b": null}'
    assert _ExtendedEncoder().encode(datetime.now()) == _ExtendedEncoder().encode(datetime.now().timestamp())
    assert _ExtendedEncoder().encode(datetime(2020, 8, 31, 21, 0, 0, 0, tzinfo=timezone.utc)) == '1598915600.0'

# Generated at 2022-06-13 19:17:09.540663
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():
    encoder = _ExtendedEncoder()
    assert encoder.default(dict(key=123)) == {'key':123}
    assert encoder.default([1,2,3]) == [1,2,3]
    assert encoder.default('abc') == 'abc'
    assert encoder.default(123) == 123
    assert encoder.default(1.23) == 1.23
    assert encoder.default(True) == True
    assert encoder.default(None) == None
    assert encoder.default(datetime(2020, 7, 11, tzinfo=timezone.utc)) == 1594499200.0

# Generated at 2022-06-13 19:17:19.083826
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = [1, 2, 3, [4, 5, 6], {'a': 'b', 'c': 'd'}, True, None, 1.2, 3.14, UUID('87c7f8f9-a791-4014-8f54-a4c7ca8634cf'), datetime.now(timezone.utc), Decimal('12.34')]
    expected = [1, 2, 3, [4, 5, 6], {'a': 'b', 'c': 'd'}, True, None, 1.2, 3.14, '87c7f8f9-a791-4014-8f54-a4c7ca8634cf', datetime.now(timezone.utc).timestamp(), '12.34']
    result = _ExtendedEncoder().default(o)

# Generated at 2022-06-13 19:17:25.380899
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    o = _ExtendedEncoder()
    assert o.default([]) == []
    assert o.default({}) == {}
    assert o.default(datetime.now(tz=timezone.utc)) == datetime.now(tz=timezone.utc).timestamp()
    assert o.default(UUID('d6e1f6a9-96ed-41cb-b3fd-7d12f4be4b88')) == 'd6e1f6a9-96ed-41cb-b3fd-7d12f4be4b88'
    assert o.default(Decimal('1.11')) == '1.11'


# Generated at 2022-06-13 19:17:30.749116
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(UUID('6ba7b814-9dad-11d1-80b4-00c04fd430c8')) == '6ba7b814-9dad-11d1-80b4-00c04fd430c8'
    assert _ExtendedEncoder().default(datetime.now(timezone.utc)) == 1581777331.688845
    assert _ExtendedEncoder().default(Decimal('1000.00')) == '1000.00'
    assert _ExtendedEncoder().default(True) == True
    assert _ExtendedEncoder().default(False) == False


# Generated at 2022-06-13 19:17:39.905911
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    encoder = _ExtendedEncoder()
    # noinspection PyTypeChecker
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    # noinspection PyTypeChecker
    assert encoder.default({'a': 1}) == {'a': 1}
    # noinspection PyTypeChecker
    assert encoder.default(datetime(2019, 1, 1, 10, 0, 0, 0, tzinfo=timezone.utc)) == 1546300800
    # noinspection PyTypeChecker
    assert encoder.default(UUID('01234567-89ab-cdef-0123-456789abcdef')) == '01234567-89ab-cdef-0123-456789abcdef'
    # noinspection PyTypeChecker

# Generated at 2022-06-13 19:17:40.833060
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    json.dumps(list(range(5)), cls=_ExtendedEncoder)
    assert True



# Generated at 2022-06-13 19:17:41.422513
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():
    assert _ExtendedEncoder().default(None) == None

