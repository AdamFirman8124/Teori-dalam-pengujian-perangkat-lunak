

# Generated at 2022-06-22 11:50:59.719816
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import pytest
    from . import rekey_on_member

    data = [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}, {'name': 'c', 'value': 3}]

    # test with list
    assert rekey_on_member(data, 'name', 'error') == {'a': {'name': 'a', 'value': 1},
                                                      'b': {'name': 'b', 'value': 2},
                                                      'c': {'name': 'c', 'value': 3}}

# Generated at 2022-06-22 11:51:09.007280
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0) == '0 B', "Failed on 0"
    assert human_readable(1) == '1 B', "Failed on 1"
    assert human_readable(1.1) == '1.1 B', "Failed on 1.1"
    assert human_readable(1.99) == '2 B', "Failed on 1.99"
    assert human_readable(999) == '999 B', "Failed on 999"
    assert human_readable(1024) == '1 KB', "Failed on 1024"
    assert human_readable(1025) == '1 KB', "Failed on 1025"
    assert human_readable(1 * 1048576) == '1 MB', "Failed on 1 MB"

# Generated at 2022-06-22 11:51:12.910230
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4]) == 4
    assert max([4, 1, 5, 2, 3]) == 5
    assert max([4, 1, 5, 2, 3], 1) == 5


# Generated at 2022-06-22 11:51:24.370472
# Unit test for function min
def test_min():
    assert 1 == min([1, 2, 3, 4])
    assert 1 == min([4, 1, 3, 2])
    assert 1 == min([1])
    assert 1 == min([1, 1, 1])
    assert 'a' == min(['a', 'b', 'c'])
    assert 'a' == min([4, 1, 3, 2], 'a')
    assert 1 == min([4, 1, 3, 2], 1)
    assert 1 == min([4, 1, 3, 2], 1, key=str)
    assert 'a' == min(['b', 'c', 'd', 'e'], 'a', key=len)


# Generated at 2022-06-22 11:51:28.948597
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4]) == 4
    assert max([1, 2, 4, 3]) == 4
    assert max([4, 1, 2, 3]) == 4
    assert max([4, 3, 2, 1]) == 4


# Generated at 2022-06-22 11:51:31.166516
# Unit test for function max
def test_max():
    test = [1, 5, 2, 4, 9, 5]
    assert 9 == max(test)



# Generated at 2022-06-22 11:51:40.919396
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import pytest
    d = { 'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2} }
    assert rekey_on_member(d, 'name') == { 'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2} }
    assert rekey_on_member([ d['a'], d['b'] ], 'name') == { 'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2} }
    assert rekey_on_member(d, 'value') == { 1: {'name': 'a', 'value': 1}, 2: {'name': 'b', 'value': 2} }
    assert rekey_on_member

# Generated at 2022-06-22 11:51:53.187981
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:52:02.309606
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    my_filter = FilterModule()
    filters = my_filter.filters()
    assert filters.get('rekey_on_member')

    rekey_on_member = filters['rekey_on_member']

    # Tests for the first argument must be iterable (set, list, etc.)
    # Tests for the second argument must be a string.
    # The third argument is optional and can be either 'error' or 'overwrite'.
    # The third argument must be a string.

    # Bad first argument: not an iterable
    data = 'TWO'
    key = 'one'
    dup = 'error'

# Generated at 2022-06-22 11:52:14.261139
# Unit test for function min
def test_min():
    assert min([1, 4, 2]) == 1
    assert min([1, 4, 2], attribute='age') == 1
    assert min([{'age': 10}, {'age': 4}, {'age': 5}], attribute='age') == {'age': 4}
    assert min([{'age': 10}, {'age': 4}, {'age': 5}], attribute='age', default=4) == {'age': 4}
    assert min([{'age': 10}, {'age': 4}, {'age': 5}], attribute='age', default=0) == {'age': 4}
    assert min([{'age': 10}, {'age': 4}, {'age': 5}], attribute='age', default=12) == {'age': 4}

# Generated at 2022-06-22 11:52:23.412522
# Unit test for function max
def test_max():
    data = [1, 2, 3, 4]
    result = max(data)
    assert result == 4



# Generated at 2022-06-22 11:52:35.096198
# Unit test for function min
def test_min():
    assert min([0, 1, 2, 3, 4, 5]) == 0
    assert min([5, 4, 3, 2, 1, 0]) == 0
    assert min([1, 2, 3, 2, 1]) == 1
    assert min(['z', 't', 'y', 'x']) == 't'
    assert min(['a', 'z', 't', 'y', 'x'], key=len) == 'z'
    assert min(['a', 'z', 't', 'y', 'x'], key=len, default='a') == 'x'
    assert min(['a', 'z', 't', 'y', 'x'], key=len, default='a', start=2) == 'x'

# Generated at 2022-06-22 11:52:44.401708
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], key=abs) == 3
    assert max([1, 0, 3], default=2) == 3
    assert max([1, 2, 3], 1) == 1

    assert max((1, 2, 3)) == 3
    assert max((1, 2, 3), default=1) == 1

    assert max({1, 2, 3}) == 3
    assert max({0: 1, 2: 0, 4: -1}) == 4

    assert max(['a', 'b', 'c']) == 'c'
    assert max(['foo', 'bar', 'test'], key=len) == 'test'

    assert max(text_type('abc')) == 'c'
    assert max('abc') == 'c'

# Generated at 2022-06-22 11:52:48.759536
# Unit test for function max
def test_max():
    assert max([1,2,3,4,5]) == 5
    assert max([5,1,2,3,4]) == 5
    assert max([]) == None
    assert max([1]) == 1
    assert max([1, 2, 3], 2, 3) == 3


# Generated at 2022-06-22 11:52:53.982456
# Unit test for function min
def test_min():
    """
    Test that minimum value is returned.
    """
    assert min([1, 2, 3]) == 1
    assert min([1, 2, 3], [2, 3, 4]) == 1
    assert min(['a', 'b', 'c'], ['c', 'b', 'a']) == 'a'



# Generated at 2022-06-22 11:52:57.178345
# Unit test for function min
def test_min():
    min_test = min([1, 2, 3])
    assert min_test == 1

    min_test_2 = min([4, 2, 3])
    assert min_test_2 == 2



# Generated at 2022-06-22 11:52:58.561541
# Unit test for function max
def test_max():
    assert max(range(10)) == 9


# Generated at 2022-06-22 11:53:09.561482
# Unit test for function min
def test_min():
    # Base tests
    assert min(1, 2) == 1
    assert min(2, 1) == 1
    assert min(1, 2, 3) == 1
    assert min(2, 3, 1) == 1
    assert min(3, 1, 2) == 1
    assert min(3, 2, 1) == 1

    # Tests using keyword arguments
    assert min([1, 2, 3]) == 1
    assert min(iterable=[1, 2, 3]) == 1
    assert min(1, 2, iterable=[1, 2, 3]) == 1

    # Tests using keyword argument `key`
    assert min(1, 2, key=lambda x: -x) == 2
    assert min(iterable=[1, 2, 3], key=lambda x: -x) == 3

# Generated at 2022-06-22 11:53:15.949231
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3
    assert max((1, 2, 3)) == 3
    assert max((3, 2, 1)) == 3
    assert max([1, 2, 3], key=str) == 3
    assert max([1, 2, 3], key=int) == 3
    assert max([1, 2, 3], key=float) == 3


# Generated at 2022-06-22 11:53:28.415414
# Unit test for function min
def test_min():
    ''' test min filter '''
    for x in [('0', '1', 0), ('1', '0', 0), (2, '0', 0), ('0', 2, 0)]:
        assert min(*x) == x[-1]

    assert min(1, 2, 3, 0) == 0
    assert min([1, 2, 3, 0]) == 0
    assert min('str', 'st0', 'str1', key=len) == 'str'
    assert min('str', 'st0', 'str1', True, key=len) == 'str'
    assert min('str', 'st0', 'str1', False, key=len) == 'st0'
    assert min('str', 'st0', 'str1', default='st0', key=len) == 'st0'

# Generated at 2022-06-22 11:53:40.904762
# Unit test for function min
def test_min():
    filters = FilterModule()
    test_input = [5, 4, 2, 6]
    assert filters.filters()['min'](None, test_input) == 2



# Generated at 2022-06-22 11:53:50.413524
# Unit test for function min
def test_min():
    hostvars = dict(
        test1=dict(var1=dict(var2="foo")),
        test2=dict(var1=dict(var2="bar")),
        test3=dict(var1=dict(var2="bar")),
        test4=dict(var1=dict(var2="baz")),
        test5=dict(var1=dict(var2="foo")),
        test6=dict(var1=dict()),
    )
    test_list = [1, 2, 3, 4, 5, 6]
    test_dict = dict(
        test1="++",
        test2="++",
        test3="+-",
    )
    # Check for builtin 'min'
    test_expected = 1

# Generated at 2022-06-22 11:54:00.976273
# Unit test for function human_readable
def test_human_readable():
    assert human_readable("1K") == "1.0 K"
    assert human_readable("1M") == "1.0 M"
    assert human_readable("1G") == "1.0 G"
    assert human_readable("1T") == "1.0 T"
    assert human_readable("10") == "10.0 B"
    assert human_readable("10.1") == "10.1 B"
    assert human_readable("1,000") == "1,000.0 B"
    assert human_readable(None) is None
    try:
        human_readable("BAD_DATA")
        assert False
    except AnsibleFilterError:
        pass


# Generated at 2022-06-22 11:54:12.071182
# Unit test for function min
def test_min():
    f = __import__('ansible').compat.filters.core.FilterModule().filters()['min']
    assert f([1, 2, 3]) == 1
    assert f([]) == 0
    assert f([0, 5]) == 0
    assert f([-1, 1]) == -1
    assert f([1.0, 2.0]) == 1.0
    assert f(['a', 'b', 'c']) == 'a'

    # Test key kwarg
    assert f([{'x': 2}, {'x': 1}], key='x') == {'x': 1}
    assert f([{'x': 0}, {'x': 1}], key='x') == {'x': 0}

    # Test attribute kwarg

# Generated at 2022-06-22 11:54:16.919253
# Unit test for function max
def test_max():
    assert max([1, 2, 4, 3]) == 4
    assert max(1, 2, 4, 3) == 4
    assert max([1, 2, 4, 3], default=0) == 4
    assert max([], default=0) == 0
    assert max(a=1, b=2, c=4, d=3) == 4

# Test for function min

# Generated at 2022-06-22 11:54:25.187612
# Unit test for function max
def test_max():

    assert(max([1, 2, 3]) == 3)
    assert(max([1, None, 3]) == 3)
    assert(max([None, None, None]) is None)
    assert(max([1, 2]) == 2)
    assert(max([1]) == 1)
    assert(max([]) is None)
    assert(max([1, 2, 3], key=lambda x: x**2) == 1)
    assert(max([1, 2, 3], key=lambda x: x*3) == 3)


# Generated at 2022-06-22 11:54:31.997549
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max((1, 2, 3)) == 3
    assert max({1, 2, 3}) == 3
    assert max({1: 'a', 2: 'b', 3: 'c'}) == 3
    assert max(range(1, 10), 3) == 3
    assert max(range(1, 10), 5) == 5

# Generated at 2022-06-22 11:54:38.846911
# Unit test for function max
def test_max():

    assert max(range(1, 6)) == 5

    assert max(range(6), 0, 5) == 5
    assert max(range(6), [0, 5]) == 5
    assert max(range(6), {0, 5}) == 5

    # max of one item should be the item itself
    value = 42
    assert max(value) == value

    # max of a string should be max(list)
    assert max('hello') == 'o'



# Generated at 2022-06-22 11:54:49.353062
# Unit test for function min
def test_min():
    from ansible.utils.display import Display
    display = Display()
    # Test 1
    # Function to test for empty list
    assert min([]) == min([]), "min function doesn't work"
    # Test 2,3
    # Function to test for one number
    assert min([1]) == 1, "min function doesn't work"
    assert min([0]) == 0, "min function doesn't work"
    # Test 4, 5
    # Function to test for one negative number
    assert min([-1]) == -1, "min function doesn't work"
    assert min([-10]) == -10, "min function doesn't work"
    # Test 6, 7
    # Function to test for multiple numbers
    assert min([1, 2, 3, 4]) == 1, "min function doesn't work"

# Generated at 2022-06-22 11:54:56.506996
# Unit test for function rekey_on_member
def test_rekey_on_member():
    """
    Test function rekey_on_member
    """

    data = [
        { "a": 1, "b": 1 },
        { "a": 2, "b": 2 },
        { "a": 1, "b": 3 },
    ]

    result = rekey_on_member(data, "b")

    assert result == {
        1: { "a": 1, "b": 1 },
        2: { "a": 2, "b": 2 },
        3: { "a": 1, "b": 3 },
    }

# Generated at 2022-06-22 11:55:22.513951
# Unit test for function max
def test_max():
    class TestClass:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __eq__(self, other):
            return self.name == other.name and self.value == other.value

    class TestClass2:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __eq__(self, other):
            return self.name == other.name and self.value == other.value

        def __gt__(self, other):
            return self.value > other.value

    class TestClass3:
        def __init__(self, name, value):
            self.name = name
            self.value = value


# Generated at 2022-06-22 11:55:34.744724
# Unit test for function min
def test_min():
    with open("test_min.txt", "r") as test_j2_file:
        test_j2_file_read = test_j2_file.read()
        print(test_j2_file_read)
        print("=======================")

        from ansible.parsing.dataloader import DataLoader
        from ansible.vars import VariableManager
        from ansible.inventory import Inventory
        from ansible.template import Template

        variable_manager = VariableManager()
        loader = DataLoader()
        inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
        variable_manager.set_inventory(inventory)

        my_vars = dict()

        template_file = "test_min.j2"

# Generated at 2022-06-22 11:55:43.987591
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:55:55.538083
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:56:07.113544
# Unit test for function rekey_on_member
def test_rekey_on_member():
    f = FilterModule().filters()
    d = {3: {'foo': 3, 'bar': 9, 'baz': 27}, 9: {'foo': 9, 'bar': 27, 'baz': 81}}
    assert f['rekey_on_member'](d, 'foo') == {3: {'bar': 9, 'foo': 3, 'baz': 27}, 9: {'bar': 27, 'foo': 9, 'baz': 81}}
    assert f['rekey_on_member'](d, 'bar') == {9: {'bar': 9, 'foo': 3, 'baz': 27}, 27: {'bar': 27, 'foo': 9, 'baz': 81}}

    l = [{'foo': 3, 'bar': 3}, {'foo': 1, 'bar': 1}]

# Generated at 2022-06-22 11:56:14.960444
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.module_utils._text import to_bytes
    import json

    # text_type is unicode on py2 and str on py3
    try:
        unicode
        text_type = unicode  # noqa
    except NameError:
        text_type = str

    try:
        long
        integer_type = long  # noqa
    except NameError:
        integer_type = int
    # Coerce bytes to text to properly test unicode coercion paths
    to_bytes = lambda x: x
    to_text = lambda x: x
    bytes_or_text = lambda x: isinstance(x, integer_type) and to_text(x) or x


# Generated at 2022-06-22 11:56:20.793236
# Unit test for function max
def test_max():
    data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 3},
        {'a': 2, 'b': 1},
    ]
    display.display(max(data, key=lambda x: x['a'] + x['b']))
    display.display(max(data, key=lambda x: x['a'] + x['b'], default='No data'))

# Generated at 2022-06-22 11:56:32.773801
# Unit test for function unique
def test_unique():
    assert unique([1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5], case_sensitive=False) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5], case_sensitive=True) == [1, 2, 3, 4, 5]

# Generated at 2022-06-22 11:56:34.182669
# Unit test for function min
def test_min():
    assert FilterModule().filters()['min']([1, 2, 3, 4, 5]) == 1

# Generated at 2022-06-22 11:56:41.332559
# Unit test for function logarithm
def test_logarithm():
    test_cases = [
        ('x', 1, math.e),
        ('10', 1, 10),
        ('0', 1, 0),
        ('1', 1, 1),
        ('0.5', 1, math.log(0.5, math.e)),
        ('1.0', 10, 1),
        ('1.0', 0, math.e)
    ]

    for entry in test_cases:
        x = entry[0]
        y = entry[1]
        result = entry[2]
        assert logarithm(x, y) == result



# Generated at 2022-06-22 11:57:06.731381
# Unit test for function unique

# Generated at 2022-06-22 11:57:17.828897
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], absolute=True) == 3
    assert max([-1, -2, -3], absolute=True) == 3
    assert max([1, -2, 3], absolute=True) == 3
    assert max([1.5, 2.5, 3.5]) == 3.5
    assert max([1.5, -2.5, 3.5]) == 3.5
    assert max([1.5, -2.5, 3.5], absolute=True) == 3.5
    assert max([[1, 2], [3, 4]]) == [3, 4]
    assert max([[1, 2], [3, 4]], key=lambda x: x[1]) == [3, 4]

# Generated at 2022-06-22 11:57:22.660000
# Unit test for function min
def test_min():
    assert min([24, 5, 11]) == 5
    assert min((24, 5, 11)) == 5
    assert min({24: "twenty-four", 5: "five", 11: "eleven"}) == 5


# Generated at 2022-06-22 11:57:32.671199
# Unit test for function human_readable

# Generated at 2022-06-22 11:57:38.645988
# Unit test for function min
def test_min():
    from ansible.modules.extras.cloud.cloudstack.cs_network import cs_network_acl
    filter_instance = cs_network_acl.FilterModule()
    filters = filter_instance.filters()
    assert filters['min']([5, 7, 1, 3, 8, 4, 6, 0, 2]) == 0
    assert filters['min']([5, 7, 1, 3, 8, 4, 6, 0, 2], key=abs) == 0



# Generated at 2022-06-22 11:57:48.804718
# Unit test for function unique
def test_unique():
    try:
        from jinja2.utils import soft_unicode
    except ImportError:
        # Jinja2 < 2.7
        from jinja2.utils import internalcode as soft_unicode  # pylint: disable=C0412

    TestFilterModule = FilterModule()
    MyFilter = TestFilterModule.filters()
    assert MyFilter['unique']([1, 2, 3, 4, 4, 2, 1, 2, 6]) == [1, 2, 3, 4, 6]
    assert MyFilter['unique'](['A', 'a', 'A', 'b'], case_sensitive=True) == ['A', 'a', 'b']
    assert MyFilter['unique'](['A', 'a', 'A', 'b'], case_sensitive=False) == ['A', 'b']
    assert My

# Generated at 2022-06-22 11:58:01.006857
# Unit test for function min
def test_min():
    input_list = ['foo', 'bar', 'baz']
    input_list_legacy = ['foo', 'bar', 'baz']
    input_dict = {'foo': 'bar', 'bar': 1, 'baz': 'foo'}
    input_dict_legacy = {'foo': 'bar', 'bar': 1, 'baz': 'foo'}

    # Test first list element
    # input, expected, kwargs
    tests = [
        (input_list, 'foo', {}),
        (input_list_legacy, 'foo', {}),
        (input_dict, 'bar', {'attribute': 'bar'}),
        (input_dict_legacy, 'bar', {'attribute': 'bar'}),
    ]

# Generated at 2022-06-22 11:58:11.483887
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([-1, -2, -3]) == -3
    assert min(["foo", "bar", "baz"]) == "bar"
    assert min([[1, 2], [1, 3], [2, 3], [2, 2]]) == [1, 2]
    assert min([1, [1], [3], [2]]) == 1
    assert min(["foo", "bar", "baz"], by=len) == "foo"
    assert min([[1, 2], [1, 3], [2, 3]], by=sum) == [1, 2]
    assert min([[1, 2], [1, 3], [2, 3]], by="sum") == [1, 2]

# Generated at 2022-06-22 11:58:18.690843
# Unit test for function max
def test_max():
    data = [
        [[1, 2, 3], 3],
        [[1, 6, 3], 6],
        [[1, 2, 11], 11],
        [[1, 2, 'not_a_int'], AnsibleFilterTypeError],
        [['not_a_int', 2, 3], AnsibleFilterTypeError],
    ]
    for test_data in data:
        assert max(test_data[0]) == test_data[1]


# Generated at 2022-06-22 11:58:30.362625
# Unit test for function rekey_on_member
def test_rekey_on_member():
    orig_list = [
        {'site': 'foo', 'host': 'foo1'},
        {'site': 'foo', 'host': 'foo2'},
        {'site': 'bar', 'host': 'bar1'},
        {'site': 'bar', 'host': 'bar2'},
        {'site': 'baz', 'host': 'baz1'},
        {'site': 'baz', 'host': 'baz2'},
    ]

    orig_dict1 = {
        'foo': {'site': 'foo', 'host': 'foo1'},
        'bar': {'site': 'bar', 'host': 'bar1'},
        'baz': {'site': 'baz', 'host': 'baz1'},
    }


# Generated at 2022-06-22 11:59:09.331913
# Unit test for function min
def test_min():
    assert min([1, 2]) == 1
    assert min([2, 1]) == 1
    assert min([2, 1, 3]) == 1
    assert min([1, 2, 3]) == 1
    assert min([]) is None


# Generated at 2022-06-22 11:59:21.093943
# Unit test for function human_to_bytes
def test_human_to_bytes():
    filter_module = FilterModule()
    assert filter_module.filters()['human_to_bytes']("2048") == 2048
    assert filter_module.filters()['human_to_bytes']("2Ki") == 2048
    assert filter_module.filters()['human_to_bytes']("2K") == 2048
    assert filter_module.filters()['human_to_bytes']("2KiB") == 2048
    assert filter_module.filters()['human_to_bytes']("1Mi") == 1048576
    assert filter_module.filters()['human_to_bytes']("1MiB") == 1048576
    assert filter_module.filters()['human_to_bytes']("1M") == 1048576

# Generated at 2022-06-22 11:59:22.020508
# Unit test for function human_readable
def test_human_readable():
    human_readable(1, 2, 3)

# Generated at 2022-06-22 11:59:24.306535
# Unit test for function min
def test_min():
    assert min([1,2, 3]) == 1, "test_min() test failed"



# Generated at 2022-06-22 11:59:27.936313
# Unit test for function logarithm
def test_logarithm():
    filter_module = FilterModule()
    filters = filter_module.filters()
    log_filter = filters['log']

    assert log_filter(10) == 2.30258509299
    assert log_filter(10, 10) == 1
    assert log_filter(15, 2) == 3.90689059561


# Generated at 2022-06-22 11:59:33.178069
# Unit test for function max
def test_max():
    import ansible.errors
    import ansible.utils
    f = ansible.utils.plugins.filter_loader._filters['max']
    assert f([2, 3, 1]) == 3
    assert f(['a', 'bb', 'ccc']) == 'ccc'
    assert f(['a', 2, 'bb']) == 'bb'
    assert f([2, 3, 1], 1, 2) == 3
    assert f([2, 3, 1], b=2, a=1) == 3
    try:
        f([1], True, attribute='foo')
    except ansible.errors.AnsibleFilterError:
        assert True
    else:
        assert False

# Generated at 2022-06-22 11:59:44.143427
# Unit test for function unique
def test_unique():
    assert unique([1, 2, 4, 2, 1, 4, 4, 4]) == [1, 2, 4], 'failed to remove duplicates'
    assert unique([1, 2, 4, 2, 1, 4, 4, 4], case_sensitive=False) == [1, 2, 4], \
        'failed to remove case insensitive duplicates'
    assert unique([1, 2, 4, 2, 1, 4, 4, 4], case_sensitive=True) == [1, 2, 4], \
        'failed to remove case sensitive duplicates'
    assert unique([{'foo': 'bar', 'baz': 1}, {'foo': 'bar', 'baz': 2}], attribute='foo') == [{'foo': 'bar', 'baz': 1}], \
        'failed to remove duplicates by attribute'

# Generated at 2022-06-22 11:59:54.235970
# Unit test for function rekey_on_member
def test_rekey_on_member():
    ''' Test rekey_on_member jinja2 filter '''

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    def assert_same_members(a, b):
        for key in a:
            assert key in b
            assert a[key] == b[key]
        for key in b:
            assert key in a

    # Test with a dict of dicts

# Generated at 2022-06-22 11:59:58.890580
# Unit test for function logarithm
def test_logarithm():
    l = logarithm(100)
    assert (4.6051701859880918 < l < 4.6051701859880921)
    assert logarithm(5, 25) == 0.32192809488736227
    try:
        logarithm('foo')
        assert False
    except AnsibleFilterTypeError:
        pass



# Generated at 2022-06-22 12:00:10.274952
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import itertools
    from ansible.module_utils.six import string_types
