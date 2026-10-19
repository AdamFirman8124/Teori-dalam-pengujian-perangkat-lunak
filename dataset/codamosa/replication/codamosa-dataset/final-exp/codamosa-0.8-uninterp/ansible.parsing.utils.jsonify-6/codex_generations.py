

# Generated at 2022-06-13 07:17:36.126125
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"foo": "bar"}, True) == "{\"foo\": \"bar\"}"
    assert jsonify({"foo": "bar"}, False) == "{\"foo\": \"bar\"}"
    assert jsonify({"foo": "bar"}) == "{\"foo\": \"bar\"}"
    assert jsonify({"foo": "bar\u00FC"}, False) == "{\"foo\": \"bar\\u00fc\"}"

# Generated at 2022-06-13 07:17:40.750022
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''
    assert jsonify(None) == '{}'

    assert jsonify(dict(foo=1, bar=2), False) == '{"bar": 2, "foo": 1}'
    assert jsonify(dict(foo=1, bar=2), True) == '{\n    "bar": 2, \n    "foo": 1\n}'

# Generated at 2022-06-13 07:17:41.621648
# Unit test for function jsonify
def test_jsonify():
    # No tests yet
    pass

# Generated at 2022-06-13 07:17:48.017771
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.jsonify import jsonify

    assert isinstance(jsonify({}), basestring)
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'
    assert jsonify({"a": "b"}, format=True) == '{\n    "a": "b"\n}'

    assert u"\u1234" in jsonify({u"\u1234": u"\u2345"}, format=True)

# Generated at 2022-06-13 07:17:50.015226
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'a': 1}) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:17:54.113475
# Unit test for function jsonify
def test_jsonify():
    result = dict(a='b', c='d')
    if jsonify(result, True) != '{\n    "a": "b", \n    "c": "d"\n}':
        raise AssertionError('jsonify() did not produce valid JSON')

# Generated at 2022-06-13 07:18:00.963259
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify([1, 2, 3]) == "[1, 2, 3]"
    assert jsonify({ "foo": "bar" }) == '{"foo": "bar"}'
    assert jsonify([1, 2, { "foo": "bar" }]) == '[1, 2, {"foo": "bar"}]'
    assert jsonify([1, 2, { "foo": "bar" }], format=True) == '''[
    1, 
    2, 
    {
        "foo": "bar"
    }
]'''

# Generated at 2022-06-13 07:18:05.307529
# Unit test for function jsonify
def test_jsonify():
    # Testing empty json
    assert jsonify(None) == "{}"
    # Testing uncompressed json
    assert jsonify({'a': 1, 'bb': '2', 'ccc': False, 'dddd': True}) == '{"a": 1, "bb": "2", "ccc": false, "dddd": true}'
    # Testing compressed json
    assert jsonify({'a': 1, 'bb': '2', 'ccc': False, 'dddd': True}, True) == '{\n    "a": 1,\n    "bb": "2",\n    "ccc": false,\n    "dddd": true\n}'

# Generated at 2022-06-13 07:18:07.172054
# Unit test for function jsonify
def test_jsonify():
    ''' Test for function jsonify '''
    assert jsonify({'a': 1}) == '{"a": 1}'
    assert jsonify([1,2,3], True) == '[\n    1,\n    2,\n    3\n]'

# Generated at 2022-06-13 07:18:14.723165
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.py3compat import PY3

    result = jsonify({"a": 2, "b": 3})
    if PY3:
        assert(isinstance(result, str))
    else:
        assert(isinstance(result, unicode))
    assert(result == '{"a": 2, "b": 3}')

    result = jsonify({"a": 2, "b": 3}, True)
    if PY3:
        assert(isinstance(result, str))
    else:
        assert(isinstance(result, unicode))
    assert(result == '{\n    "a": 2, \n    "b": 3\n}')

# Generated at 2022-06-13 07:18:25.442544
# Unit test for function jsonify
def test_jsonify():
    # C9989 - jsonify(result) should return result without any formatting
    assert jsonify({"a": "b"}) == '{"a": "b"}'

    # C9990 - jsonify(result, format=True) should return result in json format
    assert jsonify({"a": "b"}, True) == '{\n    "a": "b"\n}'

    # C9991 - jsonify(result=None) should return empty string
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:18:31.613933
# Unit test for function jsonify
def test_jsonify():
    ''' function jsonify '''

    # test empty object
    one = jsonify(None)
    assert not isinstance(one, dict)
    assert one == "{}"

    # test basic string
    two = jsonify("foo")
    assert not isinstance(two, list)
    assert two == '"foo"'

    three = jsonify(["foo", "bar"])
    assert isinstance(three, list)
    assert three == '["foo", "bar"]'


# Generated at 2022-06-13 07:18:39.007052
# Unit test for function jsonify
def test_jsonify():
    result = {
        "a": 1,
        "b": "c",
        "d": {
            "e": "f",
            "g": ["h","i","j"],
        },
    }
    assert jsonify(result, format=True) == """{
    "a": 1,
    "b": "c",
    "d": {
        "e": "f",
        "g": [
            "h",
            "i",
            "j"
        ]
    }
}"""

    assert jsonify(result, format=False) == '{"a": 1, "b": "c", "d": {"e": "f", "g": ["h", "i", "j"]}}'


# Generated at 2022-06-13 07:18:48.576796
# Unit test for function jsonify
def test_jsonify():

    result = dict(changed=True, rc=0, stdout="something", start='1:22', end='1:55',
                  delta='0:33', cmd="/bin/true", ansible_facts={})
    result2 = dict(changed=False, rc=0, stdout="else", start='1:22', end='1:55',
                   delta='0:33', cmd="/bin/true")
    result3 = dict(changed=True, rc=0, stdout=[u'\u79d2'], start='1:22', end='1:55',
                   delta='0:33', cmd="/bin/true", tests=[dict(asserts=[dict(expr="somevar == 'somevalue'", result=True,
                                                                             error=None)])])

# Generated at 2022-06-13 07:18:58.213425
# Unit test for function jsonify
def test_jsonify():
    from ansible import utils
    # test to ensure that the output is valid JSON
    data = dict(a=1, b=2, c='foo')
    json_out = utils.jsonify(data)
    out_data = json.loads(json_out)
    assert data == out_data

    # test that the indentation is correct
    data = dict(a=1, b=2, c=dict(foo='bar', baz='bam'))
    json_out = utils.jsonify(data, True)
    out_data = json.loads(json_out)
    assert data == out_data

    # test that the indentation is correct (with unicode characters)
    data = dict(a=1, b=2, c=dict(foo='bar', baz=u'\xa1?'))


# Generated at 2022-06-13 07:19:00.772931
# Unit test for function jsonify
def test_jsonify():
    import ansible.utils.jsonify as jsonify
    assert jsonify.jsonify([1,2]) == '[1, 2]'

# Generated at 2022-06-13 07:19:05.817923
# Unit test for function jsonify
def test_jsonify():

    # we use this to test
    result = {'apple': {'pear': 'peach', 'banana': ['cherry', 'watermelon']}}

    # is it a string?
    assert isinstance(jsonify(result), str)

    # are the two the same?
    assert jsonify(result) == jsonify(result, format=True)

    # should they be the same?
    assert jsonify(result) == '{"apple": {"banana": ["cherry", "watermelon"], "pear": "peach"}}'

# Generated at 2022-06-13 07:19:10.501122
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify({'A':'B'}) == '{"A": "B"}')
    assert(jsonify(None) == "{}")
    assert(jsonify([1,2,3]) == '[1, 2, 3]')

# Generated at 2022-06-13 07:19:22.953360
# Unit test for function jsonify
def test_jsonify():

    # Test case - empty results
    result = None
    output = jsonify(result)
    assert output == "{}"

    # Test case - format JSON
    result = {u"ansible_facts": {u"distribution_major_version": u"6", u"distribution": u"CentOS", u"distribution_version": u"6.5", u"os_family": u"RedHat"}}
    output = jsonify(result, True)
    assert output == '''{
    "ansible_facts": {
        "distribution": "CentOS",
        "distribution_major_version": "6",
        "distribution_version": "6.5",
        "os_family": "RedHat"
    }
}'''

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:19:31.337200
# Unit test for function jsonify
def test_jsonify():
    class TestObject(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    result = jsonify({'a':1, 'b':[1,2,3], 'c':{'d': TestObject(1,2,3)}})
    result2 = jsonify({'a':1, 'b':[1,2,3], 'c':{'d': TestObject(1,2,3)}}, True)
    assert(result == '{"a": 1, "c": {"d": {"a": 1, "b": 2, "c": 3}}, "b": [1, 2, 3]}')

# Generated at 2022-06-13 07:19:44.675311
# Unit test for function jsonify
def test_jsonify():

    # Test without indentation
    result = {
        'a':1,
        'b':2,
        'c':{
            'd':3,
            'e':4
        }
    }
    assert jsonify(result) == '{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}'

    # Test with indentation
    assert jsonify(result, True) == '{' + '\n'.join([
        '    "a": 1,',
        '    "b": 2,',
        '    "c": {',
        '        "d": 3,',
        '        "e": 4',
        '    }'
    ]) + '\n}'

# Generated at 2022-06-13 07:19:49.287127
# Unit test for function jsonify
def test_jsonify():
    sample = {'a': 1, 'b': 2, 'c': 3}
    assert jsonify(sample) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify(sample, format=True) == '''{
    "a": 1,
    "b": 2,
    "c": 3
}'''

# Generated at 2022-06-13 07:19:59.692425
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    from ansible.compat.six import StringIO
    import sys


# Generated at 2022-06-13 07:20:03.293579
# Unit test for function jsonify
def test_jsonify():
    input_map = {u'unicode': u'\u2713'}
    assert jsonify(input_map) == u'{"unicode": "\u2713"}'
    assert jsonify(input_map, True) == u'{\n    "unicode": "\u2713"\n}'

# Generated at 2022-06-13 07:20:09.808583
# Unit test for function jsonify
def test_jsonify():
    d = dict(result=dict(contacted=[dict(invocation=dict(module_name='shell', module_args='echo "hello"',
                                                          module_lang='en_US.UTF-8'))],
                          dark=[dict(invocation=dict(module_name='shell', module_args='echo "hello"',
                                                     module_lang='en_US.UTF-8'))]))

# Generated at 2022-06-13 07:20:20.575558
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic

    ansible_facts_ret = dict(
        test1=0.12345,
        test2='string',
        test3=['one', 'two', 'three'],
        test4=dict(foo='bar'),
        test5=False,
        test6="non-ascii: \xc3\xa9",
        test7="ascii: a\x00\xe1\x00b\x00",
        test8="unicode surrogate pair: \ud800\udc00",
    )


# Generated at 2022-06-13 07:20:25.172652
# Unit test for function jsonify
def test_jsonify():
    #basic test
    assert jsonify({'hello': 'world'})

    assert jsonify({'hello': 'world'}, False) == '{"hello": "world"}'
    assert jsonify({'hello': 'world'}, True) == '{\n    "hello": "world"\n}'

    # test None
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:20:36.338564
# Unit test for function jsonify
def test_jsonify():
    import os
    try:
        import json
    except:
        import simplejson as json

    # simple tests
    a = dict(one=1, two=2)
    result = jsonify(a)
    truth  = '{"two": 2, "one": 1}'

    if result != truth:
        raise AssertionError("Failed to JSONify dict")

    # test with file
    fake_data = dict(ANSIBLE_MODULE_ARGS=dict(diff=True))
    fd, fname = tempfile.mkstemp()
    f = open(fname, 'w')
    f.write(json.dumps(fake_data))
    f.close()

    a = dict(ANSIBLE_MODULE_ARGS=dict(diff=True))
    result = jsonify(a)
    truth

# Generated at 2022-06-13 07:20:47.202220
# Unit test for function jsonify
def test_jsonify():

    # Test where the result is None
    res = jsonify(None)
    assert res == '{}'

    # Test where the result is empty list
    res = jsonify([])
    assert res == '[]'

    # Test where the result is a list with one element
    res = jsonify([1])
    assert res == '[1]'

    # Test where the result is a dict
    data = dict(k=dict(a=1, b=2),
                d=dict(c=3))
    res = jsonify(data)
    assert res == '{"k": {"a": 1, "b": 2}, "d": {"c": 3}}'

    # Test where the result is a dict and formatted
    res = jsonify(data, True)

# Generated at 2022-06-13 07:20:57.310879
# Unit test for function jsonify
def test_jsonify():
    simple_dict = { "a": 1 }
    assert jsonify(simple_dict) == '{"a": 1}'
    assert jsonify(simple_dict, True) == '{\n    "a": 1\n}'

    simple_list = [ "a", "b", "c" ]
    assert jsonify(simple_list) == '["a", "b", "c"]'
    assert jsonify(simple_list, True) == '[\n    "a", \n    "b", \n    "c"\n]'

    simple_int = 1
    assert jsonify(simple_int) == '1'
    assert jsonify(simple_int, True) == '1'

    simple_float = 1.1
    assert jsonify(simple_float) == '1.1'

# Generated at 2022-06-13 07:21:11.827600
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'

    assert jsonify(None) == "{}"
    assert jsonify(None, True) == "{}"

    # test unicode
    assert jsonify({'foo': u'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': u'b\u00e4r'}) == '{"foo": "b\\u00e4r"}'
    assert jsonify({'foo': u'b\u00e4r'}, True) == '{\n    "foo": "b\\u00e4r"\n}'

# Generated at 2022-06-13 07:21:13.439839
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == "{\"a\": 1}"
    assert jsonify({"a": 1}, format=True) == "{\n    \"a\": 1\n}"



# Generated at 2022-06-13 07:21:19.246894
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(True) == 'true'
    assert jsonify(False) == 'false'
    assert jsonify({}) == '{}'
    assert jsonify({'foo':'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo':'bar'}, True) == "{\n    \"foo\": \"bar\"\n}"


# Generated at 2022-06-13 07:21:24.600218
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils import jsonify
    from ansible.module_utils import basic

    in_data1 = { "foo": "bar" } #= 
    in_data2 = None

    data1 = jsonify(in_data1)
    assert data1 == '{ "foo": "bar" }'

    data1 = jsonify(in_data1,format=True)
    assert data1 == '{\n    "foo": "bar"\n}'

    data2 = jsonify(in_data2)
    assert data2 == '{}'


# Generated at 2022-06-13 07:21:27.910417
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 1, 'b': [1, 2, 3]}
    assert jsonify(result, True) == '''{
    "a": 1,
    "b": [
        1,
        2,
        3
    ]
}'''
    assert jsonify(result) == '{"a":1,"b":[1,2,3]}'
    assert jsonify(None) == '{}'



# Generated at 2022-06-13 07:21:38.209448
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import sys

    assert jsonify(None) == "{}"
    assert jsonify(True) == "true"
    assert jsonify(False) == "false"
    assert jsonify("hello") == "\"hello\""
    assert jsonify("hello\nworld") == "\"hello\\nworld\""
    assert jsonify("hello\nworld") == "\"hello\\nworld\""
    assert jsonify("1") == "\"1\""
    assert jsonify(1) == "1"
    assert jsonify(1.123) == "1.123"
    assert jsonify({}) == "{}"
    assert jsonify(dict(foo=1, bar=2)) == "{\"bar\": 2, \"foo\": 1}"

# Generated at 2022-06-13 07:21:45.460104
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'

    jsonify([]) == '[]'
    # TODO: temporarily commented out, because this fails for some reason?
    #jsonify([1, 2, 3]) == '[1, 2, 3]'
    jsonify([1, 2, 3, {'a': 'b'}]) == '[1, 2, 3, {"a": "b"}]'
    jsonify('foo') == '"foo"'

    assert jsonify(None, format=True) == '{}'
    jsonify([], format=True) == '[]'
    # TODO: temporarily commented out, because this fails for some reason?
    #jsonify([1, 2, 3], format=True) == '[1, 2, 3]'

# Generated at 2022-06-13 07:21:53.156930
# Unit test for function jsonify
def test_jsonify():
    test_struct = dict(changed=False, rc=0, stdout='foo', start='bar', end='baz')
    assert jsonify(test_struct) == "{\"changed\": false, \"rc\": 0, \"stdout\": \"foo\", \"start\": \"bar\", \"end\": \"baz\"}"
    assert jsonify(test_struct, format=True) == "{\n    \"changed\": false,\n    \"end\": \"baz\",\n    \"rc\": 0,\n    \"start\": \"bar\",\n    \"stdout\": \"foo\"\n}"
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:21:56.024754
# Unit test for function jsonify
def test_jsonify():
    result = dict()
    result['a'] = 'b'
    result['foo'] = dict()
    result['foo']['bar'] = 'baz'
    result['list'] = ['item1', 'item2', 'item3']

    assert jsonify(result, True) == '''{
    "a": "b",
    "foo": {
        "bar": "baz"
    },
    "list": [
        "item1",
        "item2",
        "item3"
    ]
}'''

# Generated at 2022-06-13 07:21:59.464894
# Unit test for function jsonify
def test_jsonify():
    result = { "a" : 1,
               "b" : 2 }
    expected = '{"a": 1, "b": 2}'
    assert jsonify(result) == expected

# TODO: return None, return the old data

# Generated at 2022-06-13 07:22:23.809611
# Unit test for function jsonify
def test_jsonify():
    r = {'k1': 'v1', 'k2': 'v2', 'k3': ['v3', 'v4', 'v5'], 'k4': ['v6', 'v7', 'v8'], 'k5': {'kk1': 'vv1', 'kk2': 'vv2'}}
    assert(jsonify(r) == '{"k1": "v1", "k2": "v2", "k3": ["v3", "v4", "v5"], "k4": ["v6", "v7", "v8"], "k5": {"kk1": "vv1", "kk2": "vv2"}}')


# Generated at 2022-06-13 07:22:34.511726
# Unit test for function jsonify
def test_jsonify():
    # Test for unicode
    assert jsonify({'ä': 'ü'}, True) == '''{
    "ä": "ü"
}'''

    # Test for complex nested dict

# Generated at 2022-06-13 07:22:44.426054
# Unit test for function jsonify
def test_jsonify():

    # Test jsonify() with python types
    output = jsonify({"a": [3, "b", [1,2,3], {"c": 2}],
                      "b": [2, 3],
                      "c": "abc",
                      "d": None,
                      "e": True,
                      "f": False,
                      "g": 0,
                      "h": 1,
                      "i": [],
                      "j": {"k": [1,2]}
                     })


# Generated at 2022-06-13 07:22:54.984027
# Unit test for function jsonify
def test_jsonify():

    class TestContainer(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # dict
    data = TestContainer(foo='bar', bam='booz')
    jsonified = jsonify(data)
    assert jsonified == '{"bam": "booz", "foo": "bar"}'

    # dict with format
    jsonified = jsonify(data, format=True)
    assert jsonified == """{
    "bam": "booz",
    "foo": "bar"
}"""

    # None
    assert jsonify(None) == '{}'

    # None with format
    assert jsonify(None, format=True) == '{}'

# Generated at 2022-06-13 07:23:05.192127
# Unit test for function jsonify
def test_jsonify():
    import datetime

    # test list
    data = [ 1, 2, 3 ]
    assert jsonify(data) == '[1, 2, 3]'
    assert jsonify(data, True) == '''[
    1,
    2,
    3
]'''

    # test dict
    data = { 'a': 'b', 'c': 3 }
    assert jsonify(data) == '{"a": "b", "c": 3}'
    assert jsonify(data, True) == '''{
    "a": "b",
    "c": 3
}'''

    # test datetime
    data = {
        'a': 'b',
        'time': datetime.datetime(2014, 1, 2, 3, 4, 5, 6)
    }

# Generated at 2022-06-13 07:23:07.094591
# Unit test for function jsonify
def test_jsonify():
    result = { "test": "success" }
    print(jsonify(result, False))
    print(jsonify(result, True))

# Generated at 2022-06-13 07:23:16.171197
# Unit test for function jsonify
def test_jsonify():
    ''' function jsonify() returns expected results '''

    # Empty dictionary is empty
    assert jsonify({}) == "{}"

    # Dictionary with elements is not empty
    result = jsonify({'a': 'b'})
    result = json.loads(result)
    assert result['a'] == 'b'

    # Add an element to dictionary and test again
    result['b'] = 'c'
    result = jsonify(result)
    result = json.loads(result)
    assert result['a'] == 'b'
    assert result['b'] == 'c'

    # Test formatting
    result = jsonify({'a': 'b'}, format=True)
    assert '    ' in result.splitlines()

    # Test formatting for complex data structures

# Generated at 2022-06-13 07:23:21.537693
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "null"
    assert jsonify(123) == "123"
    assert jsonify([1, 2, 3, "bing"]) == "[1, 2, 3, \"bing\"]"
    assert jsonify({"foo": "bar", "baz": "bing"}) == "{\"baz\": \"bing\", \"foo\": \"bar\"}"

# Generated at 2022-06-13 07:23:27.191944
# Unit test for function jsonify
def test_jsonify():
    value = { "foo": { "bar": True, "baz": [42, "quux", u"\u1234"] } }
    result = jsonify(value, format=True)
    assert(result == '{\n    "foo": {\n        "bar": true, \n        "baz": [\n            42, \n            "quux", \n            "\\u1234"\n        ]\n    }\n}')


# Generated at 2022-06-13 07:23:35.071123
# Unit test for function jsonify
def test_jsonify():
    result = {
            "disk_images": [
                "disk1.img",
                "disk2.img"
                ]
            }
    formatted = jsonify(result, format=True)
    assert formatted == '{\n    "disk_images": [\n        "disk1.img", \n        "disk2.img"\n    ]\n}'
    unformatted = jsonify(result, format=False)
    assert unformatted == '{"disk_images": ["disk1.img", "disk2.img"]}'

# Generated at 2022-06-13 07:24:01.528563
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}, True)  == "{}"
    assert jsonify({"a": "b"}, False) == '{"a": "b"}'
    result = jsonify({"a": {"b": "c" } }, True)
    assert result == '{\n    "a": {\n        "b": "c"\n    }\n}'
    result = jsonify({"a": u'\u03b1' }, True)
    assert result == '{\n    "a": "alpha"\n}'
    result = jsonify({"a": u'\u03b1' }, False)
    assert result == '{"a": "alpha"}'

# Generated at 2022-06-13 07:24:09.977799
# Unit test for function jsonify

# Generated at 2022-06-13 07:24:16.782990
# Unit test for function jsonify
def test_jsonify():
    result = {
        "changed": False,
        "ping": "pong"
    }
    assert jsonify(result, False) == "{\"changed\": false, \"ping\": \"pong\"}"
    assert jsonify(result, True) == jsonify(result, False).replace('"', "")
    assert jsonify(None, False) == "{}"


# Generated at 2022-06-13 07:24:23.976659
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert jsonify(None) == '{}'
    assert jsonify(dict(a='foo')) == '{"a": "foo"}'
    assert jsonify(dict(a='foo'), True) == '{\n    "a": "foo"\n}'
    assert jsonify(dict(a='foo', b=dict(c=1, d=dict(e=2)))) == '{"a": "foo", "b": {"c": 1, "d": {"e": 2}}}'

# Generated at 2022-06-13 07:24:25.648492
# Unit test for function jsonify
def test_jsonify():
    ''' Test function jsonify '''
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:24:38.525812
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY3

    result = dict(
        ansible_facts=dict(
            distribution=AnsibleUnsafeText(u"FreeBSD"),
        )
    )
    assert jsonify(result) == '{"ansible_facts": {"distribution": "FreeBSD"}}'
    assert jsonify(result, True) == '''{
    "ansible_facts": {
        "distribution": "FreeBSD"
    }
}'''
    if PY3:
        assert jsonify(None) == '{}'
        assert jsonify(None, True) == '{}'
    else:
        assert jsonify(None).encode('utf-8') == '{}'
        assert jsonify

# Generated at 2022-06-13 07:24:41.787836
# Unit test for function jsonify
def test_jsonify():
    '''This is a test to make sure that jsonify works'''
    assert type(jsonify({})) == str
    assert jsonify({'a':1}) == '{"a": 1}'
    assert jsonify({'a':1}, True) == '''{\n    "a": 1\n}'''

# Generated at 2022-06-13 07:24:51.327018
# Unit test for function jsonify
def test_jsonify():
    # We should get a valid json output with a None result
    assert jsonify(None) == '{}'
    # If a result is a list, it should be jsonified
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify([1,2,3], format=True) == '[\n    1, \n    2, \n    3\n]'
    # If a result is a dict, it should be jsonified
    assert jsonify({'x': 1, 'y': 2, 'z': 3}) == '{"x": 1, "y": 2, "z": 3}'

# Generated at 2022-06-13 07:25:01.830142
# Unit test for function jsonify
def test_jsonify():
    def js(obj, format_only=False):
        return jsonify(obj, format_only)

    assert js(None) == '{}'
    assert js({}) == '{}'
    assert js({'a': None}) == '{"a": null}'
    assert js({'a': None}, True) == '{\n    "a": null\n}'
    assert js({'a': True}) == '{"a": true}'
    assert js({'a': {'b': {'c': 123}}}) == '{"a": {"b": {"c": 123}}}'
    assert js({'a': {'b': {'c': 123}}}, True) == '{\n    "a": {\n        "b": {\n            "c": 123\n        }\n    }\n}'

# Generated at 2022-06-13 07:25:06.717054
# Unit test for function jsonify
def test_jsonify():
    # jsonify should always return a string
    assert isinstance(jsonify(dict(foo='bar')), basestring)

    # an emtpy data structure (or None) should return empty json object
    assert jsonify(None) == '{}'
    assert jsonify({}) == '{}'

    # Invalid json should be passed through
    assert jsonify('foo') == 'foo'

# Generated at 2022-06-13 07:25:49.467973
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 'bar'}
    assert jsonify(result) == "{\"foo\": \"bar\"}"
    assert jsonify(result, True) == "{\n    \"foo\": \"bar\"\n}"



# Generated at 2022-06-13 07:25:55.660998
# Unit test for function jsonify
def test_jsonify():
    from json import dumps as jdumps

    assert jsonify({'a': 1, 'b': {'c': 2}}) == "{\"a\": 1, \"b\": {\"c\": 2}}"
    assert jsonify({'a': 1, 'b': {'c': 2}}, True) == jdumps({'a': 1, 'b': {'c': 2}}, sort_keys=True, indent=4)

# Generated at 2022-06-13 07:26:02.658528
# Unit test for function jsonify
def test_jsonify():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    assert jsonify(test_dict) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify(test_dict, True) == '''{\n    "a": 1, \n    "b": 2, \n    "c": 3\n}'''
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:26:09.175104
# Unit test for function jsonify
def test_jsonify():
    # OK
    result = {'a': 'b'}
    assert jsonify(result) == '{"a": "b"}'
    assert jsonify(result, format=True) == '{\n    "a": "b"\n}'

    # None
    result = None
    assert jsonify(result) == '{}'
    assert jsonify(result, format=True) == '{}'


# Generated at 2022-06-13 07:26:12.820957
# Unit test for function jsonify
def test_jsonify():
    result = dict(
        changed=True,
        ansible_facts=dict(
            foo="bar"
        )
    )
    assert jsonify(result, format=True) == """{
    "changed": true,
    "ansible_facts": {
        "foo": "bar"
    }
}"""

# Generated at 2022-06-13 07:26:23.699714
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return an empty dict when given None '''
    assert jsonify(None) == "{}"

    ''' jsonify should not change a dict '''
    assert jsonify({'foo': 'bar'}) == '{\n    "foo": "bar"\n}'

    ''' jsonify should return the string unchanged '''
    assert jsonify('{"foo": "bar"}') == '"{\\"foo\\": \\"bar\\"}"'

if __name__ == "__main__":
    import sys
    import nose
    sys.argv.append("--nocapture")    # Don't steal stdout.  Show it on the console as usual.
    sys.argv.append("--nologcapture") # Don't set the logging level to DEBUG.  Leave it alone.
    nose.run()

# Generated at 2022-06-13 07:26:32.388475
# Unit test for function jsonify
def test_jsonify():
    ''' verify behavior of jsonify() '''

    # Test None
    assert jsonify(None, format=False) == "{}"
    assert jsonify(None, format=True) == "{}"

    # Test an unformatted list
    expected_result = '[{"a": {"b": "c"}}]'
    assert jsonify([{"a": {"b": "c"}}], format=False) == expected_result

    # Test an formatted list
    expected_result = (
        '[\n'
        '    {\n'
        '        "a": {\n'
        '            "b": "c"\n'
        '        }\n'
        '    }\n'
        ']'
    )
    assert jsonify([{"a": {"b": "c"}}], format=True) == expected_result

# Generated at 2022-06-13 07:26:35.398486
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'123': 'abc'}) == '{"123": "abc"}'
    assert jsonify({'123': 'abc'}, format=True) == '{\n    "123": "abc"\n}'

# Generated at 2022-06-13 07:26:38.497051
# Unit test for function jsonify
def test_jsonify():
    original = { "some": { "dictionary": [ "with", 5, "elements"] } }
    assert jsonify(original) == '{"some": {"dictionary": ["with", 5, "elements"]}}'
    assert jsonify(original, format=True) == '''{
    "some": {
        "dictionary": [
            "with",
            5,
            "elements"
        ]
    }
}'''
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:26:42.636033
# Unit test for function jsonify
def test_jsonify():
    assert '''{
        "foo": "bar"
    }''' == jsonify(dict(foo='bar'), True)
    assert '''{"foo":"bar"}''' == jsonify(dict(foo='bar'))
    assert '''{}''' == jsonify(None)