

# Generated at 2022-06-13 07:17:34.423454
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({}) == "{}"
    assert jsonify({'a':'b'}, True) == '''\
{
    "a": "b"
}'''




# Generated at 2022-06-13 07:17:46.524595
# Unit test for function jsonify
def test_jsonify():
    testdata = {
        'json_data_none': (None, '{}'),
        'json_data_simple': (
            {'foo': 'bar'},
            '{'
            + '\n    "foo": "bar"'
            + '\n}'
        ),
        'json_data_complex': (
            {
                'foo': 'bar',
                'nested': {
                    'this': 'that'
                }
            },
            '{'
            + '\n    "foo": "bar",'
            + '\n    "nested": {'
            + '\n        "this": "that"'
            + '\n    }'
            + '\n}'
        )
    }


# Generated at 2022-06-13 07:17:49.793712
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should accept None, return a string and be json-parseable '''
    r = jsonify(None)
    assert r == '{}'
    assert isinstance(r, str)
    assert json.loads(r) == {}

# Generated at 2022-06-13 07:17:59.973072
# Unit test for function jsonify
def test_jsonify():
    import os
    from ansible.utils.color import stringc

    # save off the environment variable, we'll restore it in a moment
    non_colorized = 'nocolor'
    if 'ANSIBLE_NOCOLOR' in os.environ:
        non_colorized = os.environ['ANSIBLE_NOCOLOR']
    # force colorized output for the test
    os.environ['ANSIBLE_NOCOLOR'] = ''

    # The string should be wrapped in the color class, but the color reset
    # and the curly-braces should not be.
    s = jsonify({u"hello": u"world"})
    assert type(s) == str
    assert s == stringc("{", 'blue') + stringc('"hello"', 'green') + stringc(": ", 'blue') + stringc

# Generated at 2022-06-13 07:18:00.861084
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == "{}"

# Generated at 2022-06-13 07:18:03.881714
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 'bar'}
    assert jsonify(result, False) == '{"foo": "bar"}'

    result = {'foo': 'bar'}
    assert jsonify(result, True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:18:05.152230
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == "{\"a\": 1}"


# Generated at 2022-06-13 07:18:12.950086
# Unit test for function jsonify
def test_jsonify():
    dummy_result = {"a": "b"}
    json_result = jsonify(dummy_result)
    assert json_result == "{\"a\": \"b\"}"

    json_result = jsonify(True)
    assert json_result == "{}"

    json_result = jsonify(False)
    assert json_result == "{}"

    json_result = jsonify(None)
    assert json_result == "{}"

    json_result = jsonify(dummy_result, format=True)
    assert json_result == "{\n    \"a\": \"b\"\n}"

# Generated at 2022-06-13 07:18:17.635510
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert '"foo": "bar"' in jsonify({'foo': 'bar'})
    assert '"foo": "bar",' in jsonify({'foo': 'bar'}, True)

# Generated at 2022-06-13 07:18:21.650473
# Unit test for function jsonify
def test_jsonify():
    result = {u'foo': u'the foo', u'bar': u'the bar'}
    print(jsonify(result, format=True))
    print(jsonify(result, format=False))

# Generated at 2022-06-13 07:18:29.717028
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 'bar'}
    assert jsonify(result) == '{"foo": "bar"}'

    result = {'foo': 'bar', 'baz': 'qux'}
    assert jsonify(result, True) == '{\n    "baz": "qux", \n    "foo": "bar"\n}'


# Generated at 2022-06-13 07:18:31.795915
# Unit test for function jsonify
def test_jsonify():
    data = { 'foo': 'bar' }

    assert jsonify(data) == '{"foo": "bar"}'

##############
# for integration testing

# Generated at 2022-06-13 07:18:37.668802
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"foo": 1}) == '{"foo": 1}'
    assert jsonify({"foo": 1}, format=True) == '{\n    "foo": 1\n}'
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify(1) == '1'

    # Non-ascii chars
    obj = {u"\u00ef"}
    assert jsonify(obj) == '["\u00ef"]'
    assert jsonify(obj, format=True) == '[\n    "\u00ef"\n]'

# Generated at 2022-06-13 07:18:44.831824
# Unit test for function jsonify

# Generated at 2022-06-13 07:18:56.447866
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for jsonify '''
    import os

    from ansible.compat.tests import unittest

    class TestJsonify(unittest.TestCase):
        ''' test unit for jsonify '''

        def setUp(self):
            os.environ['LANG'] = 'en_US.UTF-8'

        def tearDown(self):
            del os.environ['LANG']

        def test_jsonify_utf8(self):
            ''' test jsonify with utf-8 string '''

# Generated at 2022-06-13 07:19:06.737894
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify() '''

    result = {'a': 'test', 'b': 1, 'c': True}
    result_json = jsonify(result, format=False)
    assert result_json == '{"a": "test", "b": 1, "c": true}'
    result_json = jsonify(result, format=True)
    assert result_json == '''{
    "a": "test",
    "b": 1,
    "c": true
}'''

    # try to encode some garbage:
    garbage = [ int ]
    result_json = jsonify(garbage, format=False)
    # it should return "{}"
    assert result_json == "{}"

    # try to encode some unicode text:

# Generated at 2022-06-13 07:19:10.822403
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo="bar")) == '{"foo": "bar"}'
    assert jsonify(dict(foo="bar"), True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:19:21.190429
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify(None, True) == '{}'
    assert jsonify([1,"foo",2,"bar"]) == '[1, "foo", 2, "bar"]'
    assert jsonify([1,"foo",2,"bar"], True) == '[\n    1,\n    "foo",\n    2,\n    "bar"\n]'
    assert jsonify({"a":"b"}) == '{"a": "b"}'
    assert jsonify({"a":"b"}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:19:30.217019
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import ansible.parsing.dataloader
    x = '{"A": "B"}'
    assert jsonify(x) == x
    assert jsonify(x, format=True) == '{\n    "A": "B"\n}'
    assert jsonify(u'A') == '"A"'
    assert jsonify('') == '""'
    assert jsonify(None) == "{}"
    assert jsonify(True) == "true"
    assert jsonify([x]) == "['{}']".format(x)
    dl = ansible.parsing.dataloader.DataLoader()
    assert jsonify(AnsibleUnsafeText(u'A')) == u'"A"'

# Generated at 2022-06-13 07:19:32.883514
# Unit test for function jsonify
def test_jsonify():
   assert jsonify({"a": "b", "c": "d"}) == '{"a": "b", "c": "d"}'
   assert jsonify({"a": "b", "c": "d"}, True) == '{\n    "a": "b", \n    "c": "d"\n}'

# Generated at 2022-06-13 07:19:45.990673
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"key": 1}) == '{"key": 1}'
    assert jsonify({"key": ["a", "b"]}) == '{"key": ["a", "b"]}'
    assert jsonify({"key": {"key": "value"}}) == '{"key": {"key": "value"}}'
    assert jsonify({"key": 1}, format=True) == "{\n    \"key\": 1\n}"
    assert jsonify({"key": ["a", "b"]}, format=True) == "{\n    \"key\": [\n        \"a\", \n        \"b\"\n    ]\n}"

# Generated at 2022-06-13 07:19:51.530119
# Unit test for function jsonify
def test_jsonify():
    testargs = [({"a": "b"}, True, "{\"a\": \"b\"}"), ({"a": "b"}, False, "{\"a\": \"b\"}"), ({"a": u"\u0430"}, True, "{\"a\": \"\\u0430\"}"), ({"a": u"\u0430"}, False, "{\"a\": \"\u0430\"}")]
    for args, format, answer in testargs:
        assert jsonify(args, format=format) == answer

# Generated at 2022-06-13 07:20:01.688945
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils.basic import AnsibleModule

    # Test input for empty dictionary
    result = { }
    if jsonify(result) != "{}":
        raise Exception("jsonify returned unexpected result")

    # Test input for non-empty dictionary
    result = { 'a': 1, 'b': 2 }
    if jsonify(result) != '{"a":1,"b":2}':
        raise Exception("jsonify returned unexpected result")

    # Test input for non-empty dictionary
    result = { 'x': [1, 2, 3, 4], 'y': { 'a': 1, 'b': 2 } }
    if jsonify(result) != '{"x":[1,2,3,4],"y":{"a":1,"b":2}}':
        raise Exception("jsonify returned unexpected result")

    # Test input for empty

# Generated at 2022-06-13 07:20:03.194522
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}')

# Generated at 2022-06-13 07:20:05.736965
# Unit test for function jsonify
def test_jsonify():
    result = {'msg': 'the message', 'changed': False}
    jsonstring = jsonify(result)
    # jsonify removes None values
    result = {'msg': None, 'changed': False}
    jsonstring = jsonify(result)

# Generated at 2022-06-13 07:20:11.235331
# Unit test for function jsonify
def test_jsonify():

    if jsonify(None) != "{}":
        print("ERROR, expected empty dict for None")
        exit(1)

    if jsonify({"a": "b"}) != '{"a": "b"}' or jsonify({"a": "b"}, True) != '{\n    "a": "b"\n}':
        print("ERROR, expected dict for dict")
        exit(1)

    if jsonify([]) != "[]":
        print("ERROR, expected empty list for empty list")
        exit(1)

    if jsonify([1,2,3]) != "[1, 2, 3]" or jsonify([1,2,3], True) != "[\n    1, \n    2, \n    3\n]":
        print("ERROR, expected list for list")
        exit(1)


# Generated at 2022-06-13 07:20:15.111597
# Unit test for function jsonify
def test_jsonify():
    """
    Insert a bunch of test cases for jsonify()
    """

    import copy
    import json
    import ansible.utils.unicode

    # Test ascii
    result = { u"a" : [1,2,3], u"b" : { u"c" : "a\tstring\u00A0with\u00A0non-ascii\u2030chars" } }
    result_ascii = jsonify(result)
    assert(result_ascii == '{"b": {"c": "a\\tstring with non-ascii\\u2030chars"}, "a": [1, 2, 3]}')
    assert(json.loads(result_ascii) == result)

    # Test non-ascii

# Generated at 2022-06-13 07:20:22.111205
# Unit test for function jsonify
def test_jsonify():
    import pytest
    result = jsonify({'my': 'world', 'is': {'great': True, 'flat': False}})
    assert result == '{"is": {"flat": false, "great": true}, "my": "world"}'
    assert jsonify(None) == "{}"
    assert jsonify({}) == "{}"

if __name__ == "__main__":
    import pytest
    pytest.main([__file__,'-v'])

# Generated at 2022-06-13 07:20:26.817223
# Unit test for function jsonify
def test_jsonify():
    from nose.tools import assert_true

    test1 = {'foo':'bar', 'test':'pass'}
    test2 = None

    result1 = jsonify(test1)
    result2 = jsonify(test2)
    result3 = jsonify(test1, format=True)

    assert_true(type(result1) == str)
    assert_true(type(result2) == str)
    assert_true(type(result3) == str)

# Generated at 2022-06-13 07:20:34.098096
# Unit test for function jsonify
def test_jsonify():
    data = [{'a': 1, 'b': {'c': 4}}]
    assert jsonify(data, format=False) == '[{"a": 1, "b": {"c": 4}}]'
    assert jsonify(data, format=True) == '[\n    {\n        "a": 1, \n        "b": {\n            "c": 4\n        }\n    }\n]'
    assert jsonify(None) == '{}'


# Generated at 2022-06-13 07:20:47.240611
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({'a': 1, 'b': 2}, format=True) == '{\n    "a": 1,\n    "b": 2\n}'

# Generated at 2022-06-13 07:20:53.031267
# Unit test for function jsonify
def test_jsonify():
    result = { 'a': 1, 'b': 2, 'c': 3 }
    json_result = jsonify(result)
    assert json_result == '{"a": 1, "b": 2, "c": 3}'

    json_result = jsonify(result, format=True)
    assert json_result == '''{
    "a": 1,
    "b": 2,
    "c": 3
}'''

# Generated at 2022-06-13 07:20:59.352036
# Unit test for function jsonify
def test_jsonify():
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))

    # generate the test data
    test_data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key4': 'value4',
            'key5': 'value5',
        },
    }

    # generate the expected result
    expected_result = '''{
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key4": "value4",
        "key5": "value5"
    }
}'''

    # make sure the result matches the expected result
    result = jsonify(test_data, True)
    assert expected_result == result

# Generated at 2022-06-13 07:21:01.362251
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1,b=2,c=3)) == "{\"a\": 1, \"b\": 2, \"c\": 3}"

# Generated at 2022-06-13 07:21:15.191194
# Unit test for function jsonify
def test_jsonify():
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR

    expected_result = { 'hash_behaviour': DEFAULT_HASH_BEHAVIOUR, 'ignore_errors': False, 'rc': 0, 'results': [ { 'changed': True, 'msg': 'fake changed' }, { 'changed': False, 'msg': 'fake unchanged' } ], 'stdout': 'fake stdout', 'stdout_lines': [ 'fake line 1', 'fake line 2' ] }

    assert jsonify({}) == "{}"


# Generated at 2022-06-13 07:21:18.501284
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:21:32.706408
# Unit test for function jsonify
def test_jsonify():

    result = { 'a' : 1, 'b' : 2, 'c' : 3 }
    formatted = jsonify(result, True)
    assert "\n" in formatted
    assert " " in formatted
    not_formatted = jsonify(result, False)
    assert "\n" not in not_formatted
    assert " " not in not_formatted

    unicode_string = u'\u20ac'
    result = { 'a' : unicode_string }
    formatted = jsonify(result, True)
    assert unicode_string in formatted
    assert isinstance(formatted, str)
    not_formatted = jsonify(result, False)
    assert unicode_string in not_formatted
    assert isinstance(not_formatted, str)

    result = None
    formatted = jsonify(result, True)

# Generated at 2022-06-13 07:21:35.763946
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == "{'foo': 'bar'}"
    assert jsonify({'foo': 'bar'}, True) == "{\n    'foo': 'bar'\n}"

# Generated at 2022-06-13 07:21:40.097904
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({1: "a"}) == '{"1": "a"}'
    assert jsonify({1: "a"}, format=True) == '{\n    "1": "a"\n}'
    assert jsonify(["a"]) == '["a"]'
    assert jsonify(["a"], format=True) == '[\n    "a"\n]'

# Generated at 2022-06-13 07:21:48.705131
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None, True) == "{}"
    assert jsonify(42) == "42"
    assert jsonify("\"cake\"") == "\"\\\"cake\\\"\""
    assert jsonify("cake") == "\"cake\""
    assert jsonify(["candy", "cookies", "cake"]) == "[\"candy\", \"cookies\", \"cake\"]"
    assert jsonify(dict()) == "{}"
    assert jsonify({"candy": "cookies", "cake": "candles"}) == "{\"cake\": \"candles\", \"candy\": \"cookies\"}"

# Generated at 2022-06-13 07:22:02.434462
# Unit test for function jsonify
def test_jsonify():
    j = jsonify({'a': 1, 'b':2})
    assert j == '{"a": 1, "b": 2}'

    j = jsonify({'a': 1, 'b':2}, True)
    assert j == '{\n    "a": 1, \n    "b": 2\n}'

    j = jsonify(None, True)
    assert j == '{}'

    # ensure non-ASCII works
    j = jsonify({'a':'\xc3\x86'}, True)
    assert j == '{\n    "a": "\\u00c6"\n}'

# Generated at 2022-06-13 07:22:11.156338
# Unit test for function jsonify
def test_jsonify():
    if jsonify(None) != "{}":
        raise AssertionError("jsonify(None) did not return '{}'")

    if jsonify({"a": [{"b": "c", "e": "f"}]}, True) != '''{
    "a": [
        {
            "b": "c",
            "e": "f"
        }
    ]
}''':
        raise AssertionError("jsonify(..., True) did not return correctly formatted string")

    if jsonify({"a": [{"b": "c", "e": "f"}]}, False) != '{"a": [{"b": "c", "e": "f"}]}':
        raise AssertionError("jsonify(..., False) did not return correct not-formatted string")

# Generated at 2022-06-13 07:22:25.544397
# Unit test for function jsonify
def test_jsonify():
    ''' Test jsonify function '''

    i = {
        'a': [{'b':'c', 'd':'e'}],
        'f': 'g',
        'h': [1,2,{'i':'j', 'k':'l'}],
    }
    assert jsonify(i) == ('{"a": [{"b": "c", "d": "e"}], "f": "g", "h": [1, 2, {"i": "j", "k": "l"}]}')

# Generated at 2022-06-13 07:22:34.963192
# Unit test for function jsonify
def test_jsonify():
    data = [1,2,3,{'a':'b'}]
    json = jsonify(data)
    assert json == '[1, 2, 3, {"a": "b"}]'
    assert jsonify(None) == '{}'
    assert jsonify(None, True) == '{}'
    assert jsonify(data, True) == '[\n    1,\n    2,\n    3,\n    {\n        "a": "b"\n    }\n]'

# Generated at 2022-06-13 07:22:46.803542
# Unit test for function jsonify
def test_jsonify():
    """Test the ``jsonify`` function"""
    from ansible.utils.jsonify import jsonify
    from ansible.module_utils import basic
    from ansible.utils import to_bytes

    # Test for the new jsonify
    foo = jsonify(basic.ansible_module_common_args())
    bar = to_bytes(json.dumps(basic.ansible_module_common_args()))
    assert foo == bar

    foo = jsonify({'hello': 'world'}, True)
    bar = to_bytes('{\n    "hello": "world"\n}')
    assert foo == bar

    # Test conversion of non-ascii
    foo = jsonify({'hello': 'Zoë'}, True)
    bar = to_bytes('{\n    "hello": "Zoë"\n}')


# Generated at 2022-06-13 07:22:58.514111
# Unit test for function jsonify
def test_jsonify():
    a_list = ['foo', 'bar', {'k1':['v1', "v2"]}]
    a_dict = {'foo':'bar', 'abc':12345}

    from ansible.utils import jsonify

    print("----")
    print(jsonify(a_list))
    print("----")
    print(jsonify(a_dict))
    print("----")
    print(jsonify(a_list, format=True))
    print("----")
    print(jsonify(a_dict, format=True))
    print("----")


# ----
# [ "foo", "bar", { "k1": [ "v1", "v2" ] } ]
# ----
# { "abc": 12345, "foo": "bar" }
# ----
# [
#     "foo",


# Generated at 2022-06-13 07:23:06.069962
# Unit test for function jsonify
def test_jsonify():
    assert '{}' == jsonify(None)

    assert 'null' == jsonify(None, True)

    assert '{}' == jsonify({})
    assert '{"a": 1, "b": 2}' == jsonify({'a': 1, 'b': 2})

    assert '''{
    "a": 1,
    "b": 2
}''' == jsonify({'a': 1, 'b': 2}, True)

    # also test unicode handling
    assert '{"foo": "bar"}' == jsonify({u'foo': u'bar'})
    assert '{"foo": "bar"}' == jsonify({'foo': b'bar'})

# Generated at 2022-06-13 07:23:10.095439
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo='bar', baz='qux')) == '{"baz": "qux", "foo": "bar"}'
    assert jsonify(dict(foo='bar', baz='qux'), format=True) == '{\n    "baz": "qux", \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:23:18.515276
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify([]) == '[]'
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'
    assert jsonify(dict(a=[1,2,3])) == '{"a": [1, 2, 3]}'
    assert jsonify(dict(a=dict(b=dict(c=dict(d=[1,2,3]))))) == '{"a": {"b": {"c": {"d": [1, 2, 3]}}}}'

# Generated at 2022-06-13 07:23:21.413933
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == '{}'
    assert jsonify({'a':1}) == '{"a": 1}'
    assert jsonify({'a':1}, True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:23:37.465146
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify({'a': ['b', 'c']}, True) == '''{
    "a": [
        "b",
        "c"
    ]
}'''

# Generated at 2022-06-13 07:23:43.918830
# Unit test for function jsonify
def test_jsonify():
    result = { "failed": False, "changed": True, "ping": "pong" }
    output = jsonify(result)
    print(output)
    assert output == '{"changed": true, "failed": false, "ping": "pong"}'

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:23:47.397116
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify: basic function
    '''
    assert jsonify({}) == "{}"
    assert jsonify(None) == "{}"


# Generated at 2022-06-13 07:23:57.847726
# Unit test for function jsonify
def test_jsonify():

    results = {
        'foo': 'bar',
        1: 2.012345,
        'qux': 'quux',
    }

    assert jsonify(results) == '{"1": 2.012345, "foo": "bar", "qux": "quux"}'
    assert jsonify(results, format=True) == """{
    "1": 2.012345,
    "foo": "bar",
    "qux": "quux"
}"""

    assert jsonify(None, format=True) == "{}"

    results = {
        'foo': 'bar',
        1: 'a\xc3\xb1o',
        'qux': 'quux',
    }


# Generated at 2022-06-13 07:24:02.484087
# Unit test for function jsonify
def test_jsonify():
    ''' Verify function jsonify
    '''
    result = { 'a': '1', 'b': '2', 'c': '3' }
    assert jsonify(result) == '{"a": "1", "b": "2", "c": "3"}'
    result = None
    assert jsonify(result) == '{}'

# Generated at 2022-06-13 07:24:05.696700
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify unit tests '''

    assert jsonify({'a': 1}) == '{"a": 1}'
    assert jsonify({'a': 1}, True) == '''{
    "a": 1
}'''

# Generated at 2022-06-13 07:24:08.769451
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'
    assert jsonify({'foo': 'bar'}, False) == '{"foo": "bar"}'
    assert jsonify({}, False) == '{}'

# Generated at 2022-06-13 07:24:15.781703
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 1, 'b': 2}
    assert jsonify(result, False) == "{\"a\": 1, \"b\": 2}"
    assert jsonify(result, True) == "{\n    \"a\": 1,\n    \"b\": 2\n}".encode('utf-8')

# ==============================================================
# JSONFILTER: filter to format JSON output


# Generated at 2022-06-13 07:24:23.056588
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({}) == '{}'
    assert jsonify({1: 1}) == '{"1": 1}'

    assert jsonify([]) == '[]'
    assert jsonify(['a', 'b', 'c']) == '["a", "b", "c"]'
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'

    assert jsonify(1) == '1'
    assert jsonify(1.1) == '1.1'
    assert jsonify(None) == 'null'
    assert jsonify(True) == 'true'
    assert jsonify(False) == 'false'
    assert jsonify('string') == '"string"'
    assert jsonify(u'\u2016') == '"\u2016"'

# Generated at 2022-06-13 07:24:33.816100
# Unit test for function jsonify

# Generated at 2022-06-13 07:25:01.116766
# Unit test for function jsonify
def test_jsonify():

    x = {
        "changed" : True,
        "ping"    : "pong",
    }
    y = jsonify(x)
    z = json.loads(y)
    assert x == z

    x = {
        'changed' : True,
        'invocation': {
            'module_name': "fake",
            'module_args': {},
        },
        'ping': 'pong',
    }
    y = jsonify(x, format=True)
    assert json.loads(y) == x
    assert y.startswith('{\n    ')

# Generated at 2022-06-13 07:25:04.942739
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({}) == "{}"
    assert jsonify({'a': [1, 2, 3]}) == '{"a": [1, 2, 3]}'
    assert json.loads(jsonify({'a': [1, 2, 3]})) == {'a': [1, 2, 3]}
    assert json.loads(jsonify({'a': [1, 2, 3]}, True)) == {'a': [1, 2, 3]}

# Generated at 2022-06-13 07:25:10.218238
# Unit test for function jsonify
def test_jsonify():

    # Test 1: Test with no input
    result = jsonify(None)
    assert result == "{}"

    # Test 2: Test with output in pretty format
    result = jsonify({"test": "success"}, True)
    assert result == '{\n    "test": "success"\n}'

    # Test 3: Test with output not in pretty format
    result = jsonify({"test": "success"}, False)
    assert result == '{"test": "success"}'

# Generated at 2022-06-13 07:25:13.498109
# Unit test for function jsonify
def test_jsonify():
    res = jsonify("foo")
    assert res == "\"foo\""

    res = jsonify("foo", format=True)
    assert res == "\"foo\""

    res = jsonify({"a": 1, "b": 2})
    assert res == "{\"a\": 1, \"b\": 2}"

    res = jsonify({"a": 1, "b": 2}, format=True)
    assert res == "{\n    \"a\": 1, \n    \"b\": 2\n}"

# Generated at 2022-06-13 07:25:22.606931
# Unit test for function jsonify
def test_jsonify():
    ''' Check that jsonify converts python data to JSON data
        Check that jsonify doesn't convert already converted JSON data to JSON
    '''
    import ansible.utils.jsonify as jsonify
    from ansible.module_utils.basic import json_dict_unicode_to_bytes, AnsibleModule

    data = { "data": { "key1": "value1" }, "temp1": "value2" }
    jdata = json_dict_unicode_to_bytes(data)
    jdstring = jsonify.jsonify(data, False)
    jdstring_format = jsonify.jsonify(data, True)
    jdjson = jsonify.jsonify(jdata, False)
    jdjson_format = jsonify.jsonify(jdata, True)


# Generated at 2022-06-13 07:25:32.587048
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.color import stringc
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    from ansible.plugins.callback.default import CallbackModule

    loader = DataLoader()
    variable_manager = VariableManager()

    host = Host('test')
    variable_manager.set_host_variable(host, 'ansible_ssh_pass', 'pass')

    task = Task()
   

# Generated at 2022-06-13 07:25:35.621508
# Unit test for function jsonify
def test_jsonify():
    results = dict(changed=False, foo="bar")
    assert jsonify(results, format=True) == '{\n    "changed": false, \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:25:39.725593
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':1,'b':[1,2,3]}) == '{"a": 1, "b": [1, 2, 3]}'
    assert jsonify({'a':1,'b':[1,2,3]}, True) == '''
{
    "a": 1,
    "b": [
        1,
        2,
        3
    ]
}
'''

# Generated at 2022-06-13 07:25:52.838337
# Unit test for function jsonify
def test_jsonify():
    """
    Test the jsonify function.
    """
    # Test empty dict
    assert jsonify(None) == '{}'

    # Test empty dict
    assert jsonify({'x': 'y'}) == '{"x": "y"}'

    # Test a simple dict and compare formatting.
    result = jsonify({'x': 'y', 'a': 'b'}, True)
    assert result == '{\n    "a": "b", \n    "x": "y"\n}'

    # Test a simple dict and compare formatting.
    result = jsonify({'x': 'y', 'a': 'b'}, False)
    assert result == '{"a": "b", "x": "y"}'

# Generated at 2022-06-13 07:25:57.420305
# Unit test for function jsonify
def test_jsonify():
    input = {'foo': 1, 'bar': 2, 'baz': 3}
    output = jsonify(input, 1)
    assert output == json.dumps(input, sort_keys=True, indent=4, ensure_ascii=False)

    input = {'foo': {'foo': 1, 'bar': 2, 'baz': 3}}
    output = jsonify(input, 1)
    assert output == json.dumps(input, sort_keys=True, indent=4, ensure_ascii=False)

# Generated at 2022-06-13 07:26:46.596219
# Unit test for function jsonify
def test_jsonify():
    result = {
        'foo' : "bar",
        'spam': "eggs",
        'list': [1,2,3,4],
        'dict': {"a": "b"},
    }

    assert jsonify(result) == "{\"dict\": {\"a\": \"b\"}, \"foo\": \"bar\", \"list\": [1, 2, 3, 4], \"spam\": \"eggs\"}"
    assert jsonify(result, True) == "{\n    \"dict\": {\n        \"a\": \"b\"\n    }, \n    \"foo\": \"bar\", \n    \"list\": [\n        1, \n        2, \n        3, \n        4\n    ], \n    \"spam\": \"eggs\"\n}"

# Generated at 2022-06-13 07:26:49.216532
# Unit test for function jsonify
def test_jsonify():
    result = [1, 2, 3]
    assert jsonify(result, True) == '[\n    1,\n    2,\n    3\n]\n'
    assert jsonify(result, False) == '[1, 2, 3]'

# Generated at 2022-06-13 07:26:53.195525
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}, format=True) == '''{
    "foo": "bar"
}'''
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:26:58.754085
# Unit test for function jsonify
def test_jsonify():
    # Test function should return a json string
    assert isinstance(jsonify(dict(foo=1,bar=2)),(str, unicode))

    # Check jsonify displays the expected result
    assert jsonify(dict(foo=1,bar=2)) == '{"bar": 2, "foo": 1}'

    # Check jsonify returns a blank dictionary if None
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:27:04.016620
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for function jsonify '''
    result = {'foo': 'bar'}
    assert jsonify(result, format=False) == '{"foo": "bar"}'
    assert jsonify(result, format=True) == '{\n    "foo": "bar"\n}'
    assert jsonify(None) == '{}'



# Generated at 2022-06-13 07:27:10.988762
# Unit test for function jsonify
def test_jsonify():
    result = {
        "example": {
            "foo": True,
            "bar": 42,
            "baz": 3.14,
            "blam": [1, 2, 3, 4, 5],
        },
    }

    # pylint: disable=protected-access
    assert jsonify(result, format=False) == jsonify._json_encoder.encode(result)
    assert jsonify(result, format=True)  == jsonify._json_encoder.encode(result).replace(' ', '    ')

# Generated at 2022-06-13 07:27:15.897311
# Unit test for function jsonify
def test_jsonify():
    complex_list = ['localhost', { 'failed': False, 'changed': False }]
    assert(jsonify(complex_list, True) == jsonify(complex_list))
    assert(jsonify(complex_list, True) == '[\n    "localhost", \n    {\n        "failed": false, \n        "changed": false\n    }\n]')

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:27:19.281900
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic
    import ansible.constants as C

    result = basic.AnsibleModule(argument_spec={}, supports_check_mode=True).jsonify({'foo': 'bar'})
    assert result == "{\"foo\": \"bar\"}"

# Generated at 2022-06-13 07:27:23.913069
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a':1,'b':'foo'}, True) == '{\n    "a": 1, \n    "b": "foo"\n}'
    assert jsonify({'a':1,'b':'foo'}) == '{"a":1,"b":"foo"}'

# Generated at 2022-06-13 07:27:28.789922
# Unit test for function jsonify
def test_jsonify():
    result = {"a":1, "b":2}
    assert jsonify(result) == "{\"a\": 1, \"b\": 2}"
    assert jsonify(result, True) == "{\n    \"a\": 1, \n    \"b\": 2\n}"