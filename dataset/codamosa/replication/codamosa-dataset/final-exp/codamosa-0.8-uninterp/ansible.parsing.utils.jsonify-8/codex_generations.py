

# Generated at 2022-06-13 07:17:43.356481
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == jsonify({"a": 1}, format=False) == "{\"a\": 1}"
    assert jsonify({"a": 1}, format=True) == "{\n    \"a\": 1\n}"
    assert jsonify({"numbers": [1,2,3]}) == jsonify({"numbers": [1,2,3]}, format=False) == "{\"numbers\": [1, 2, 3]}"
    assert jsonify({"numbers": [1,2,3]}, format=True) == "{\n    \"numbers\": [\n        1, \n        2, \n        3\n    ]\n}"
    assert jsonify({"string": "bar"}) == jsonify({"string": "bar"}, format=False) == "{\"string\": \"bar\"}"


# Generated at 2022-06-13 07:17:52.509151
# Unit test for function jsonify
def test_jsonify():
    result = {
        u'foo': 123,
        'bar': u'Árvíztűrő tükörfúrógép',
    }
    s = jsonify(result, True)
    assert s == u'{\n    "bar": "\\u00c1rv\\u00edzt\\u0171r\\u0151 t\\u00fck\\u00f6rf\\u00far\\u00f3g\\u00e9p", \n    "foo": 123\n}'
    s = jsonify(result, False)

# Generated at 2022-06-13 07:17:54.928090
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(False) == "false"
    assert jsonify(True) == "true"
    assert jsonify({}) == "{}"

# Generated at 2022-06-13 07:18:03.221619
# Unit test for function jsonify
def test_jsonify():
    result = { 'a': '1', 'b': 2, 'c': 'three', 'd': [ u'\u2654', u'\u2655', u'\u2656' ] }
    assert jsonify(result) == '{"a": "1", "b": 2, "c": "three", "d": ["\u2654", "\u2655", "\u2656"]}'
    assert jsonify(result, True) == '{\n    "a": "1", \n    "b": 2, \n    "c": "three", \n    "d": [\n        "\u2654", \n        "\u2655", \n        "\u2656"\n    ]\n}'

# Generated at 2022-06-13 07:18:07.431427
# Unit test for function jsonify
def test_jsonify():
    # this is a bit difficult to test, so we just make sure it returns a string
    from ansible.utils import jsonify
    data = { "test": "success" }
    assert type(jsonify(data)) == str
    assert type(jsonify(data, format=True)) == str

# Generated at 2022-06-13 07:18:09.366261
# Unit test for function jsonify
def test_jsonify():
    import datetime
    print(jsonify({"a": datetime.datetime.utcnow()}))

# Generated at 2022-06-13 07:18:12.460806
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify

    test_input = { 'foo': 'bar' }
    test_output = '{\n    "foo": "bar"\n}'

    assert jsonify(test_input, True) == test_output

# Generated at 2022-06-13 07:18:20.155897
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify '''

    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, format=True) == '{\n    "foo": "bar"\n}'
    assert jsonify({'foo': 'bar\n', 'bam': 10}, format=True) == '{\n    "bam": 10, \n    "foo": "bar\\n"\n}'

# Generated at 2022-06-13 07:18:24.036656
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"spam": "eggs"}) == '{"spam": "eggs"}'
    assert jsonify({"spam": "eggs"}, format=True) == '{\n    "spam": "eggs"\n}'

# Generated at 2022-06-13 07:18:27.442651
# Unit test for function jsonify
def test_jsonify():
    test_dict = dict(foo='bar', bam=[1,2,3])
    assert jsonify(test_dict, format=False) == '{"bam": [1, 2, 3], "foo": "bar"}'
    assert jsonify(test_dict, format=True) == '{\n    "bam": [\n        1, \n        2, \n        3\n    ], \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:18:32.138875
# Unit test for function jsonify
def test_jsonify():
    result = { 'foo': 'bar' }
    assert jsonify(result, format=True) == '''{
    "foo": "bar"
}'''
    assert jsonify(result, format=False) == '{"foo": "bar"}'
    assert jsonify(None, format=False) == '{}'

# Generated at 2022-06-13 07:18:34.062785
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1}) == '{"a": 1}'

    assert jsonify({'a': 1}, format=True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:18:36.142777
# Unit test for function jsonify
def test_jsonify():
    expected_result = '''{
    "a": "b"
}'''
    result = jsonify({'a': 'b'}, format=True)
    assert result == expected_result

# Generated at 2022-06-13 07:18:42.872479
# Unit test for function jsonify
def test_jsonify():
    some_dict = {'a': ['b1', 'b2'], 'c': {'d': ['e1', 'e2']}}
    assert jsonify(some_dict, True) == dedent("""\
    {
        "a": [
            "b1",
            "b2"
        ],
        "c": {
            "d": [
                "e1",
                "e2"
            ]
        }
    }""")
    assert jsonify(some_dict, False) == dedent("""\
    {"a": ["b1", "b2"], "c": {"d": ["e1", "e2"]}}""")

# Generated at 2022-06-13 07:18:51.593969
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({'a':'b'}) == '{"a": "b"}'
    assert jsonify({'a':'b'}, format=False) == '{"a": "b"}'
    assert jsonify({'a':'b'}, format=True) == '''{\n    "a": "b"\n}'''
    assert jsonify({'a':'b', 'c': 'd'}, format=True) == '''{\n    "a": "b", \n    "c": "d"\n}'''

# Generated at 2022-06-13 07:18:54.323234
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({},True) == "{}"
    assert jsonify({u'abc': [b'123']},True) == '{"abc": ["123"]}'

# Generated at 2022-06-13 07:19:05.355102
# Unit test for function jsonify
def test_jsonify():

    # Test with an empty dictionary
    result = jsonify({})
    assert result == '{}'

    # Test with an empty array
    result = jsonify([])
    assert result == '[]'

    # Test with sample data

# Generated at 2022-06-13 07:19:10.823249
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':1,'b':2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a':1,'b':2}, format=True) == '''{
    "a": 1,
    "b": 2
}'''

# Generated at 2022-06-13 07:19:17.125691
# Unit test for function jsonify
def test_jsonify():
    o = {'a': 1, 'b': 2, 'c': 3}
    assert jsonify(o) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify(o, True) == '{\n    "a": 1, \n    "b": 2, \n    "c": 3\n}'

# Generated at 2022-06-13 07:19:23.477598
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None, format=False) == "{}"
    assert jsonify([1,2,3,4,5], format=False) == "[1, 2, 3, 4, 5]"
    assert jsonify(None, format=True) == "{}"
    assert jsonify([1,2,3,4,5], format=True) == "[\n    1,\n    2,\n    3,\n    4,\n    5\n]"

# Generated at 2022-06-13 07:19:28.774264
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify
    assert jsonify(dict(a=1, b=2, c=3)) == '{"a": 1, "b": 2, "c": 3}'

# Generated at 2022-06-13 07:19:30.109322
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:19:32.207011
# Unit test for function jsonify
def test_jsonify():
    data = dict(foo='one', bar='two')
    assert jsonify(data) == jsonify(data)
    assert jsonify(data, format=True) == jsonify(data, format=True)

# Generated at 2022-06-13 07:19:44.156715
# Unit test for function jsonify
def test_jsonify():

    def assert_json_eq(a, b):
        if a != b:
            raise ValueError("%s != %s" % (a, b))

    # we should be able to serialize dicts and lists, regardless of contents
    assert_json_eq(jsonify(dict(foo="bar")), '{"foo": "bar"}')
    assert_json_eq(jsonify(dict(foo=dict(bar="baz"))), '{"foo": {"bar": "baz"}}')
    assert_json_eq(jsonify(["foo", "bar", "baz"]), '["foo", "bar", "baz"]')
    assert_json_eq(jsonify("foo"), '"foo"')

    # unserializable contents should fail

# Generated at 2022-06-13 07:19:45.893684
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify([]) == "[]"
    assert jsonify({}) == "{}"

# Generated at 2022-06-13 07:19:48.296059
# Unit test for function jsonify
def test_jsonify():
    # test empty result
    assert jsonify(None) == "{}"
    # test list with empty result
    assert jsonify([ None ]) == "[{}]"

# Generated at 2022-06-13 07:19:53.180879
# Unit test for function jsonify
def test_jsonify():
    res = {'a': 1, 'b': 2, 'c': 3}
    assert jsonify(res) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify(res, True) == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:20:07.597959
# Unit test for function jsonify
def test_jsonify():
    from ansible import constants as C
    from ansible.module_utils.common._collections_compat import MutableMapping

    # Set format for testing
    C.DEFAULT_STDOUT_JSON = True

    result = { 'rc': 0, 'stdout': 'foo', 'stdout_lines': [ "foo", "bar", "baz" ], 'stderr': '', 'failed': False, 'changed': True }
    assert jsonify(result) == '{\n    "changed": true, \n    "failed": false, \n    "rc": 0, \n    "stderr": "", \n    "stdout": "foo", \n    "stdout_lines": [\n        "foo", \n        "bar", \n        "baz"\n    ]\n}'

    # Make sure we do

# Generated at 2022-06-13 07:20:11.258223
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":2}) == '{"a": 2}'
    assert jsonify({"a":{"b":1}}, format=True) == '{\n    "a": {\n        "b": 1\n    }\n}'

# Generated at 2022-06-13 07:20:13.616512
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar', 'bam': None}) == '{"bam": null, "foo": "bar"}'
    assert jsonify({'foo': 'bar', 'bam': None}, True) == '{\n    "bam": null, \n    "foo": "bar"\n}'


# Generated at 2022-06-13 07:20:27.401575
# Unit test for function jsonify
def test_jsonify():
    def old_jsonify(result):
        ''' format JSON output in old style '''

        if result is None:
            return "{}"

        try:
            return json.dumps(result, sort_keys=True)
        except UnicodeDecodeError:
            return json.dumps(result, sort_keys=True)

    # test None
    assert jsonify(None) == '{}'
    assert jsonify(None, True) == '{}'

    # test empty dict
    assert jsonify({}) == '{}'
    assert jsonify({}, True) == '{}'

    # test example dict 1
    assert jsonify({'example1': {'example2': 'example3'}}) == '{"example1": {"example2": "example3"}}'

# Generated at 2022-06-13 07:20:32.220994
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return an empty string when passed None, a string when passed a string, and a json string when passed a dict. '''

    assert jsonify(None) == "{}"
    assert jsonify("test") == '"test"'
    assert jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:20:37.551226
# Unit test for function jsonify
def test_jsonify():
    result = {'spam': 'foo', 'bar': 'baz'}
    res = jsonify(result)
    assert res == '{"bar": "baz", "spam": "foo"}'
    res = jsonify(result, True)
    assert res == '{\n    "bar": "baz", \n    "spam": "foo"\n}'

# Generated at 2022-06-13 07:20:47.589448
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(False) == "false"
    assert jsonify(True) == "true"
    assert jsonify('foo') == "\"foo\""
    assert jsonify(42) == "42"
    assert jsonify(3.14) == "3.14"
    assert jsonify([1, 2, 3]) == "[1, 2, 3]"
    assert jsonify([[1, 2], [3, 4]]) == "[[1, 2], [3, 4]]"
    assert jsonify(dict(a=1, b=2)) == "{\"a\": 1, \"b\": 2}"

# Generated at 2022-06-13 07:20:51.157545
# Unit test for function jsonify
def test_jsonify():
    ''' Just test if function jsonify runs through'''

    result = '{"free_space": "923.8 MB", "total_space": "1.2 GB", "mount": "/boot"}'

    assert type(jsonify(result)) is str


# Generated at 2022-06-13 07:20:56.849566
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(dict(changed=True)) == '{"changed": true}'
    assert jsonify(dict(changed=True, rc=0)) == '{"changed": true, "rc": 0}'
    assert jsonify(dict(changed=True, rc=0, msg="test")) == '{"changed": true, "msg": "test", "rc": 0}'

# Generated at 2022-06-13 07:21:06.097878
# Unit test for function jsonify
def test_jsonify():
    data = {
        'a': 'foo',
        'b': 'bar',
        'c': 'baz',
        'd': {
            'e': 'foo',
            'f': 'bar',
            'g': 'baz',
        }
    }
    data_json_string = jsonify(data)
    assert data == json.loads(data_json_string)
    data_json_string_formatted = jsonify(data, format=True)
    assert data_json_string != data_json_string_formatted
    assert data == json.loads(data_json_string_formatted)

# Generated at 2022-06-13 07:21:12.189077
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({}, True)
    assert result == '{}'
    result = jsonify({'foo': 'bar'}, True)
    assert result == '{\n    "foo": "bar"\n}'
    result = jsonify({'foo': 'bar'})
    assert result == '{"foo": "bar"}'

# Generated at 2022-06-13 07:21:22.366255
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(1) == '1'
    assert jsonify(1, True) == '1'
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify([1,2,3], True) == '[1, 2, 3]'
    assert jsonify({'a':'hello', 'b':'world', 'c':[1,2,3]}) == '{"a": "hello", "b": "world", "c": [1, 2, 3]}'

# Generated at 2022-06-13 07:21:36.297444
# Unit test for function jsonify
def test_jsonify():
    my_dict = {
        'a': 'I am the first letter of the alphabet!',
        'b': 'I am the second letter of the alphabet!',
        'c': 'I am the third letter of the alphabet!'
    }

    # Test format=False
    assert jsonify(my_dict, False) == "{\"a\": \"I am the first letter of the alphabet!\", \"c\": \"I am the third letter of the alphabet!\", \"b\": \"I am the second letter of the alphabet!\"}"

    # Test format=True
    assert jsonify(my_dict, True) == "{\n    \"a\": \"I am the first letter of the alphabet!\", \n    \"c\": \"I am the third letter of the alphabet!\", \n    \"b\": \"I am the second letter of the alphabet!\"\n}"

    # Test

# Generated at 2022-06-13 07:21:48.574580
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 1}) == '{"foo": 1}'
    assert jsonify({'foo': 1}, True) == '{\n    "foo": 1\n}'

# Generated at 2022-06-13 07:21:49.847512
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:21:57.625243
# Unit test for function jsonify
def test_jsonify():
    result = dict(a=1, z=dict(b=2, y=dict(c=3, x="a\u1234")))
    assert jsonify(result, False) == jsonify(result, True)
    assert jsonify(result, False) == '{"a": 1, "z": {"b": 2, "y": {"c": 3, "x": "a\\u1234"}}}'
    assert jsonify(result, True) == '''{
    "a": 1,
    "z": {
        "b": 2,
        "y": {
            "c": 3,
            "x": "a\\u1234"
        }
    }
}'''
    assert jsonify(None, False) == "{}"
    assert jsonify(None, True) == "{}"

# Generated at 2022-06-13 07:22:03.059358
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return a pre-formatted string for debug purposes '''

    test_input = {"foo": "bar"}
    expected_output = '{\n    "foo": "bar"\n}'

    print(jsonify(test_input, format=True))
    assert jsonify(test_input, format=True) == expected_output

# Generated at 2022-06-13 07:22:09.574501
# Unit test for function jsonify
def test_jsonify():
    ''' Test the jsonify function '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    result = { "myvar": AnsibleUnsafeText(u'myvalue') }

    jsonstr = jsonify(result, True)
    assert jsonstr == '{\n    "myvar": "myvalue"\n}'
    jsonstr = jsonify(result)
    assert jsonstr == '{"myvar": "myvalue"}'
    jsonstr = jsonify(None)
    assert jsonstr == '{}'

# Generated at 2022-06-13 07:22:10.866545
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}, True)=='{}'

# Generated at 2022-06-13 07:22:23.311514
# Unit test for function jsonify
def test_jsonify():
    result = { 'a': 1, 'b':[2,3], 'c':{'b':9} }

    # test reserialization
    assert jsonify(jsonify(result)) == json.dumps(result)

    # test pretty printing
    assert jsonify(result, True) == json.dumps(result, indent=4, sort_keys=True)

    # test unicode handling
    result['unicode_key'] = u"\u5341\u5341\u5341"
    result['unicode_val'] = u"\u5341\u5341\u5341"
    assert json.dumps(result) == jsonify(result)

# Generated at 2022-06-13 07:22:29.859259
# Unit test for function jsonify
def test_jsonify():
    import sys
    import io
    import ansible.utils.jsonify as jsonify
    from ansible.utils.jsonify import *

    def test_fail_on_exception(exception):
        try:
            raise exception
        except Exception:
            return "failed"

    def test_pass_on_exception(exception):
        try:
            raise exception
        except Exception:
            pass

    orig_stdout = sys.stdout
    sys.stdout = io.StringIO.StringIO()

# Generated at 2022-06-13 07:22:32.623699
# Unit test for function jsonify
def test_jsonify():
    result = {'foo':'bar'}
    expected = '{"foo": "bar"}'
    assert (jsonify(result) == expected)


# Generated at 2022-06-13 07:22:36.709288
# Unit test for function jsonify
def test_jsonify():
    ''' test format JSON output (uncompressed or uncompressed) '''

    result = {'apples':1, 'oranges':2}
    assert jsonify(result, format=False).count("\n") == 0

# Generated at 2022-06-13 07:22:56.918529
# Unit test for function jsonify
def test_jsonify():
    lst = ['a', 'b', 'c', 'd']
    assert jsonify(lst) == '["a", "b", "c", "d"]'
    assert jsonify(lst, True) == '[\n    "a", \n    "b", \n    "c", \n    "d"\n]'

    dct = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
    assert jsonify(dct) == '{"a": 1, "b": 2, "c": 3, "d": 4}'
    assert jsonify(dct, True) == '{\n    "a": 1, \n    "b": 2, \n    "c": 3, \n    "d": 4\n}'

    assert jsonify(None) == "{}"
   

# Generated at 2022-06-13 07:23:06.337625
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify() should take a python object and return a json string '''
    import random

    # test boolean value
    assert jsonify(True) == "true"
    assert jsonify(False) == "false"

    # test int or float value
    assert jsonify(412) == "412"
    assert jsonify(412.34) == "412.34"

    # test string value
    assert jsonify("test") == "\"test\""

    # test list of int value
    assert jsonify([1,2,3,4,5]) == "[1, 2, 3, 4, 5]"

    # test dict of int value
    assert jsonify({'a':1, 'b':2, 'c':3}) == "{\"a\": 1, \"b\": 2, \"c\": 3}"

    # test dict of int value with

# Generated at 2022-06-13 07:23:14.337362
# Unit test for function jsonify
def test_jsonify():

    # Test jsonify without indent
    result1 = {}
    result1['a'] = 'b'
    result1['c'] = 'd'
    result1['e'] = 'f'
    result1['g'] = 'h'
    json_result = jsonify(result1)
    assert (json_result == '{"a": "b", "c": "d", "e": "f", "g": "h"}'), "jsonify() without indent failed"

    # Test jsonify with indent
    json_result = jsonify(result1, True)
    assert (json_result == '{\n    "a": "b",\n    "c": "d",\n    "e": "f",\n    "g": "h"\n}'), "jsonify() with indent failed"

    # Test jsonify with None result

# Generated at 2022-06-13 07:23:15.761181
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify

    assert jsonify(dict(foo=42)) == "{\"foo\": 42}"

# Generated at 2022-06-13 07:23:22.118293
# Unit test for function jsonify
def test_jsonify():
    given1 = {"a":"b"}
    expected1 = "{\"a\": \"b\"}"
    assert jsonify(given1)==expected1

    given2 = {"a":"b"}
    expected2 = "{\n    \"a\": \"b\"\n}"
    assert jsonify(given2, True)==expected2

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', 'tests/test_jsonify.py'])

# Generated at 2022-06-13 07:23:30.232924
# Unit test for function jsonify
def test_jsonify():
    # Test that None is properly handled
    assert jsonify(None) == '{}'

    my_dict = dict(
        a=1,
        b=dict(
            c=dict(
                d=dict(
                    e=dict(
                        f=2,
                        g=3,
                    ),
                    h=4,
                    i=5,
                    j=6,
                ),
                k=7,
                l=8,
                m=9,
                n=[1,2,3,4],
            ),
            o=10,
            p=11,
            q=12,
        ),
        r=13,
        s=14,
        t=15,
    )
    # Asserts that the original dict (my_dict) matches the JSON string
    # that we generate.

# Generated at 2022-06-13 07:23:34.992401
# Unit test for function jsonify
def test_jsonify():
    import ast

    result = { 'some': 'thing' }
    output = jsonify(result)
    try:
        output = ast.literal_eval(output)
    except:
        print("JSON test failed.")

test_jsonify()

# Generated at 2022-06-13 07:23:38.813678
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:23:51.091452
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert jsonify(dict(a=1, b=2, c=3)) == json.dumps(dict(a=1, b=2, c=3), sort_keys=True, indent=None, ensure_ascii=False)
    assert jsonify(dict(a=1, b=2, c=3), format=True) == json.dumps(dict(a=1, b=2, c=3), sort_keys=True, indent=4, ensure_ascii=False)
    assert jsonify(dict(a=1, b=2, c=3), format=True) == json.dumps(dict(a=1, b=2, c=3), sort_keys=True, indent=4)

# Generated at 2022-06-13 07:23:56.406274
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'b', 'c': 'd'}) == '{"a": "b", "c": "d"}'
    assert jsonify({'a': 'b', 'c': 'd'}, format=True) == '{\n    "a": "b", \n    "c": "d"\n}'

# Generated at 2022-06-13 07:24:22.699378
# Unit test for function jsonify
def test_jsonify():
    """
    Basic function unit test for function jsonify
    """

    ####################################
    # Test "compressed" output
    ####################################

    result = [{"foo":"bar"}, {"bam":"boop"}, {"jim":"tam"}]
    json_out = jsonify(result)

    assert json_out == '{"bam": "boop", "foo": "bar", "jim": "tam"}', \
        "Uncompressed expected, but got: %s" % json_out

    ####################################
    # Test "formatted" output
    ####################################

    result = [{"foo":"bar"}, {"bam":"boop"}, {"jim":"tam"}]
    json_out = jsonify(result, format=True)


# Generated at 2022-06-13 07:24:29.007680
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({"a": "b", "c": "d"})
    assert result == '{"a": "b", "c": "d"}', "uncompressed JSON failed"
    result = jsonify({"a": "b", "c": "d"}, True)
    assert result == '{\n    "a": "b",\n    "c": "d"\n}', "compressed JSON failed"

# Generated at 2022-06-13 07:24:35.392983
# Unit test for function jsonify
def test_jsonify():
    import sys

    if sys.version_info < (2, 7, 0):
        from nose.plugins.skip import SkipTest
        raise SkipTest("jsonify tests require python2.7")

    # make sure jsonify works with utf-8
    r1 = jsonify({ "foo": u"\u0430" })
    r2 = jsonify({ "foo": u"\u0430" }, format=True)
    assert r1 == '{"foo": "\\u0430"}'
    assert r2 == '{\n    "foo": "\\u0430"\n}'

# Generated at 2022-06-13 07:24:43.215684
# Unit test for function jsonify
def test_jsonify():
    '''Test jsonify'''

    a = {'a': 'test'}
    b = jsonify(a)
    assert b == '{"a": "test"}'
    a = {'a': 'test', 'b': 'test'}
    b = jsonify(a)
    assert b == '{"a": "test", "b": "test"}'
    b = jsonify(a, True)
    assert b == '{\n    "a": "test", \n    "b": "test"\n}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:24:48.524456
# Unit test for function jsonify
def test_jsonify():
    result = { "a": 1, "b": 2, "c": 3 }
    assert jsonify(result) == json.dumps(result)
    assert jsonify(None) == "{}"
    assert jsonify(result, True) == json.dumps(result, indent=4)
    assert jsonify(None, True) == "{}"

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:24:52.086660
# Unit test for function jsonify
def test_jsonify():
    res = {}
    res['failed'] = False
    res['changed'] = True

    assert jsonify(res, False) == '{"changed": true, "failed": false}'
    assert jsonify(res, True) == '''{
    "changed": true,
    "failed": false
}'''

# Generated at 2022-06-13 07:24:55.675038
# Unit test for function jsonify
def test_jsonify():
    res = {'a': ['a','b','c']}
    assert jsonify(res) == jsonify(res)
    assert jsonify(res, True) != jsonify(res)

# Generated at 2022-06-13 07:24:58.375070
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1)) == "{\"a\": 1}"
    assert jsonify(dict(a=1), True) == "{\n    \"a\": 1\n}"

# Generated at 2022-06-13 07:25:02.167420
# Unit test for function jsonify
def test_jsonify():
    result = { "foo": "bar" }
    assert jsonify(result, False) == '{"foo": "bar"}'
    assert jsonify(result, True) == '{\n    "foo": "bar"\n}'
    assert jsonify(None, False) == '{}'
    assert jsonify(None, True) == '{}'

# Generated at 2022-06-13 07:25:06.393048
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed=False, rc=0, stdout="testing", stderr="")
    result = jsonify(result, format=True)
    result = jsonify(result, format=False)
    result = jsonify(12345, format=False)
    result = jsonify("asdf", format=False)



# Generated at 2022-06-13 07:25:50.351456
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify({'a': 'b'}, True) == '''{
    "a": "b"
}'''

# Generated at 2022-06-13 07:25:53.407294
# Unit test for function jsonify
def test_jsonify():
    ''' unit tests for jsonify '''

    result = jsonify(None, False)
    assert result == "{}"

# Generated at 2022-06-13 07:26:00.765142
# Unit test for function jsonify
def test_jsonify():
    ''' Unit test for function ansible.utils.jsonify '''
    from ansible.utils import jsonify

    # sample data
    result = dict(changed=True, rc=0)

    # direct test
    assert jsonify(result) == '{"changed": true, "rc": 0}'
    assert jsonify(result, format=True) == '{\n    "changed": true, \n    "rc": 0\n}'

    # test typing integer
    result = 69
    assert jsonify(result) == '69'
    assert jsonify(result, format=True) == '69'

    # test typing list
    result = ['1','2','3']
    assert jsonify(result) == '["1", "2", "3"]'

# Generated at 2022-06-13 07:26:02.425960
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:26:12.821476
# Unit test for function jsonify
def test_jsonify():
    my_result = dict(a=1, b=2, c=3)
    assert jsonify(None) == '{}'
    assert jsonify(my_result, format=True) == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'
    assert jsonify(my_result, format=False) == '{"a": 1, "b": 2, "c": 3}'
    my_result = dict(a=1, b=2, c=unichr(40960))
    assert jsonify(my_result, format=True) == '{\n    "a": 1,\n    "b": 2,\n    "c": "\\ud840\\udc00"\n}'

# Generated at 2022-06-13 07:26:17.248844
# Unit test for function jsonify
def test_jsonify():
    from ansible import constants as C
    from ansible.utils.unicode import to_bytes

    C.DEFAULT_UNDEFINED_JSON = 'stringify'

    assert jsonify(dict(foo='bar'), True) == to_bytes('{\n    "foo": "bar"\n}')

# Generated at 2022-06-13 07:26:18.993168
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(hello='world')) == '{"hello": "world"}'

# Generated at 2022-06-13 07:26:22.505182
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':1, 'b':2, 'c':3}) == "{\"a\": 1, \"b\": 2, \"c\": 3}"

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:26:27.386474
# Unit test for function jsonify
def test_jsonify():
    result = { 'foo': 'bar', 'baz': 'qux' }

    assert jsonify(result, True) == '''{
    "baz": "qux",
    "foo": "bar"
}'''
    assert jsonify(result, False) == '{"baz": "qux", "foo": "bar"}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:26:35.278952
# Unit test for function jsonify
def test_jsonify():
    from units.compat import unittest
    from units.compat.mock import patch, MagicMock

    class TestJsonify(unittest.TestCase):

        def setUp(self):
            self.mock_json = { 'a': 1, 'b': 2 }

        def test_jsonify(self):
            with patch('ansible.utils.jsonify.json') as mock_json:
                mock_json.dumps.return_value = json.dumps(self.mock_json, sort_keys=True, indent=4)
                self.assertEqual(jsonify(self.mock_json, format=True), mock_json.dumps.return_value)
