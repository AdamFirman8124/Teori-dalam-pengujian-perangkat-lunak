

# Generated at 2022-06-13 07:17:35.348041
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule()
    b = jsonify(m.params)
    assert b == u'{"ANSIBLE_MODULE_ARGS": {}}'

# Generated at 2022-06-13 07:17:39.057706
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed=False)
    s = jsonify(result)
    assert s == json.dumps(result, sort_keys=True, indent=None)

# Generated at 2022-06-13 07:17:43.229180
# Unit test for function jsonify
def test_jsonify():
    # test if None
    assert jsonify(None) == "{}"

    # test if String
    assert jsonify("{'foo':'hello'}") == "{\"foo\": \"hello\"}"

    # test if Dict
    assert jsonify({'foo':'hello'}) == "{\"foo\": \"hello\"}"

# Generated at 2022-06-13 07:17:49.223676
# Unit test for function jsonify
def test_jsonify():
    # invalid JSON cannot be dumped
    assert None == jsonify("foo")

    # None is a valid JSON object
    assert '{}' == jsonify(None)

    # JSON object retains the original format if format=False
    unformatted_json = '{"foo": "bar"}'
    assert unformatted_json == jsonify(json.loads(unformatted_json))

    # JSON object is formatted if format=True
    formatted_json = '''{
    "foo": "bar"
}'''
    assert formatted_json == jsonify(json.loads(unformatted_json), format=True)

# Generated at 2022-06-13 07:17:52.238194
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({'a': 1, 'b': 2, 'c': [1, 2, 3]}, format=False) == "{\"a\": 1, \"b\": 2, \"c\": [1, 2, 3]}"

# Generated at 2022-06-13 07:17:59.016300
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return an empty string for None result '''
    assert jsonify(None) == "{}"
    assert jsonify(True) == "true"
    assert jsonify(1) == "1"
    assert jsonify("one") == "\"one\""
    assert jsonify(["one", True, 1]) == "[\"one\", true, 1]"
    assert jsonify({"one": 1, "two": 2}) == '{"one": 1, "two": 2}'


# Generated at 2022-06-13 07:18:01.119743
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":1}) == '{"a": 1}'
    assert jsonify({"a":1}, True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:18:04.249773
# Unit test for function jsonify
def test_jsonify():
    result = {"a": {"b": "c"}}
    assert jsonify(result, format=True) == '{\n    "a": {\n        "b": "c"\n    }\n}'
    result = {"a": {"b": "c"}}
    assert jsonify(result) == '{"a": {"b": "c"}}'
    result = None
    assert jsonify(result) == "{}"

# Generated at 2022-06-13 07:18:14.318779
# Unit test for function jsonify
def test_jsonify():

    from ansible.executor.muterunner import MuteRunner

    m = MuteRunner(None)
    m._config = dict()
    m._config['DEFAULT_JSON_FORMAT'] = True
    m._config['DEFAULT_MODULE_LANG'] = 'en_US.UTF-8'

    output = 'foo'

    result = {'contacted': {'127.0.0.1': {'invocation': {'module_args': {},
                                                         'module_name': 'command'},
                                           'rc': 0,
                                           'stderr': '',
                                           'stdout': output,
                                           'stdout_lines': [output]}}}


# Generated at 2022-06-13 07:18:18.666187
# Unit test for function jsonify
def test_jsonify():
    """
    jsonify: jsonify function
    """
    import sys

    if sys.version_info[0] > 2:
        assert jsonify({"a":2}) == '{"a": 2}'
    else:
        assert jsonify({"a":2}) == '{"a": 2}'

# Generated at 2022-06-13 07:18:24.704304
# Unit test for function jsonify
def test_jsonify():
    # a small test
    assert jsonify(dict(foo="bar")) == '{"foo": "bar"}'

    # a helpful error when being passed something other than a dict
    # (say, a string)
    try:
        jsonify("foo")
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 07:18:33.217224
# Unit test for function jsonify
def test_jsonify():
    import sys

    if sys.version_info < (2, 6):
        jsonify({}, True)
        return

    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify({"foo": ["bar", "baz"]}) == '{"foo": ["bar", "baz"]}'
    assert jsonify({"foo": ["bar", "baz"]}, True) == """{
    "foo": [
        "bar",
        "baz"
    ]
}"""

    assert jsonify({'foo': None}) == '{"foo": null}'

# Generated at 2022-06-13 07:18:41.360363
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify in human-readable (default) mode '''

    sample = {
        'a': 1,
        'c': {
            'd': 2,
            'e': None,
        },
        'b': [1, 2, 3],
    }

    assert(jsonify(sample) == '{"a": 1, "b": [1, 2, 3], "c": {"d": 2, "e": null}}')

    sample['c']['e'] = []
    assert(jsonify(sample) == '{"a": 1, "b": [1, 2, 3], "c": {"d": 2, "e": []}}')

    sample['c']['e'] = [{'f': 3}]

# Generated at 2022-06-13 07:18:43.876953
# Unit test for function jsonify
def test_jsonify():
    # jsonify the list [1,2,3]
    assert '{"json": [1, 2, 3]}' == jsonify({'json': [1, 2, 3]})

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:18:52.294841
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return valid json output '''

    # simple test
    result = {"a":1, "b":2}
    assert jsonify(result) == "{\"a\": 1, \"b\": 2}"

    # should jsonify a dict
    result = { "foo": "bar" }
    assert jsonify(result) == '{"foo": "bar"}'

    # should jsonify a list
    result = ["foo", "bar"]
    assert jsonify(result) == '["foo", "bar"]'


# Generated at 2022-06-13 07:18:56.007909
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == "{}"
    assert jsonify(None) == "{}"
    assert jsonify({"test":1}) == "{\"test\": 1}"
    assert jsonify({"test":1},{"test":2}) == "{\"test\": 1}"


# Generated at 2022-06-13 07:19:00.867007
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == '{}'

    assert jsonify({"a": 1}) == '{"a": 1}'

    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'



# Generated at 2022-06-13 07:19:01.836765
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:04.160810
# Unit test for function jsonify
def test_jsonify():
    data = dict(a=1, b=2, c=3)
    assert jsonify(data, format=False) == jsonify(data, format=True)
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:10.129736
# Unit test for function jsonify
def test_jsonify():
    result = {
        "a": {"b": {"c": 1}},
        "d": {"e": "f"},
        "g": 1,
        "h": [1,2,3]
    }
    assert(jsonify(result)) == '{"a": {"b": {"c": 1}}, "d": {"e": "f"}, "g": 1, "h": [1, 2, 3]}'
    assert(jsonify(result, True)) == '{\n    "a": {\n        "b": {\n            "c": 1\n        }\n    }, \n    "d": {\n        "e": "f"\n    }, \n    "g": 1, \n    "h": [\n        1, \n        2, \n        3\n    ]\n}'

# Generated at 2022-06-13 07:19:18.192019
# Unit test for function jsonify
def test_jsonify():
    data = {
        'a': True,
    }
    json_str = jsonify(data, False)
    assert json_str == "{\"a\": true}"

    json_str = jsonify(data, True)
    assert json_str == """{
    "a": true
}"""

# Generated at 2022-06-13 07:19:28.176481
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return an empty dictionary when given None,
        a dictionary of two space indented JSON when given a hash,
        and a string of two space indented JSON when given a string.
    '''
    from ..defaults import *
    from ..module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(
            result      = dict(required=True, type='raw'),
            format      = dict(required=False, type='bool', default=False),
        ),
        supports_check_mode=True,
    )

    result = dict(foo='bar')
    result_json = '{\n    "foo": "bar"\n}'
    result_str = "foo"
    result_str_json = '"foo"'


# Generated at 2022-06-13 07:19:30.699335
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert jsonify(AnsibleUnsafeText('"test"', is_safe=True)) == '"test"'
    assert jsonify(u'å') == '"å"'

# Generated at 2022-06-13 07:19:38.446913
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify(None) == "{}"
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, True) == '{\n    "a": 1\n}'
    assert jsonify({u'unicode': u'value'}) == '{"unicode": "value"}'
    assert jsonify({u'unicode': u'value'}, True) == '{\n    "unicode": "value"\n}'


# Generated at 2022-06-13 07:19:39.094218
# Unit test for function jsonify
def test_jsonify():
    pass

# Generated at 2022-06-13 07:19:45.160717
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == "{}"
    assert jsonify({'a': 'b'}, True) == '{\n    "a": "b"\n}'
    assert jsonify('{"a": "b"}', False) == '"{\\"a\\": \\"b\\"}"'
    assert jsonify('{"a": "b"}', True) == '"{\\"a\\": \\"b\\"}"'

# Generated at 2022-06-13 07:19:50.029660
# Unit test for function jsonify
def test_jsonify():
    result = dict(
        test1='test1',
        test2='test2'
    )
    assert jsonify(result) == '{"test1": "test1", "test2": "test2"}'
    assert jsonify(result, True) == '{\n    "test1": "test1",\n    "test2": "test2"\n}'

# Generated at 2022-06-13 07:19:54.486481
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'b'}) == '{\"a\": \"b\"}'
    assert jsonify({'a': 'b'}, format=True) == '{\n    \"a\": \"b\"\n}'

# Generated at 2022-06-13 07:19:57.422129
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'


# Generated at 2022-06-13 07:20:04.325841
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == "{}"
    assert jsonify(True) == "true"
    assert jsonify(False) == "false"

    assert jsonify(dict(foo='bar')) == '{"foo": "bar"}'
    assert jsonify(dict(foo=dict(bar='baz'))) == '{"foo": {"bar": "baz"}}'

# Generated at 2022-06-13 07:20:17.558288
# Unit test for function jsonify
def test_jsonify():
    from ansible.plugins.action.normal import ResultGatheringProcessor


# Generated at 2022-06-13 07:20:26.593558
# Unit test for function jsonify
def test_jsonify():
    import os
    from ansible.module_utils._text import to_bytes

    # make sure we're using the right json module
    import ansible.module_utils
    assert ansible.module_utils.json == json

    # unicode input
    assert '\xe2\x98\x83' in jsonify({'test': u'\u2603'})

    p = os.path.normpath(os.path.join("lib", "ansible", "modules", "commands", "command.py"))
    b_p = to_bytes(p)
    assert p == b_p

    # binary input
    assert jsonify(b_p) == '"%s"' % p
    assert jsonify(to_bytes("{'test': u'\u2603'}"))

# Generated at 2022-06-13 07:20:31.357637
# Unit test for function jsonify
def test_jsonify():
    ''' this is a very basic test that only covers what I implemented '''
    assert jsonify(None) == '{}'
    assert jsonify(dict(a=1, b=dict(c=3))) is not None

# if __name__ == '__main__':
#     test_jsonify()

# Generated at 2022-06-13 07:20:33.863766
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo='bar'), format=True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:20:38.215054
# Unit test for function jsonify
def test_jsonify():
    test_cases = [
        (None, "{}"),
        ({'key': 'test'}, '{\n    "key": "test"\n}'),
        ({"key": "test"}, '{"key": "test"}')
    ]

    for test_case in test_cases:
        yield check_jsonify, test_case[0], test_case[1]


# Generated at 2022-06-13 07:20:48.566451
# Unit test for function jsonify
def test_jsonify():
    '''
    ansible.utils.jsonify test cases
    '''

    # None result
    assert jsonify(None) == '{}'

    # Dict result
    assert jsonify({'msg': 'Hello World'}) == '{"msg": "Hello World"}'

    # Array result
    assert jsonify(['a', 'b', 'c']) == '["a", "b", "c"]'

    # Dict result with unicode
    assert jsonify({'msg': u'Hello World'}) == u'{"msg": "Hello World"}'

    # Array result with unicode
    assert jsonify([u'a', u'b', u'c']) == u'["a", "b", "c"]'

    # Dict result with unicode and format

# Generated at 2022-06-13 07:20:56.857146
# Unit test for function jsonify
def test_jsonify():
    from collections import namedtuple

    # namedtuple is not JSON serializable, but jsonify should
    # automatically detect this and return a dict instead.
    result = namedtuple("Result", "foo bar baz")
    result.foo = "Foo"
    result.bar = "Bar"
    result.baz = "Baz"

    # No formatting
    actual_result = jsonify(result, format=False)
    assert actual_result == '{"bar": "Bar", "foo": "Foo", "baz": "Baz"}'

    # With formatting
    actual_result = jsonify(result, format=True)
    expected_result = '''{
    "bar": "Bar",
    "baz": "Baz",
    "foo": "Foo"
}'''
    assert actual_result == expected

# Generated at 2022-06-13 07:20:59.873313
# Unit test for function jsonify
def test_jsonify():
    output = jsonify({'foo': 'bar'}, True)
    assert output == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:21:14.059699
# Unit test for function jsonify
def test_jsonify():
    if jsonify(None, True) != '{}':
        raise Exception("jsonify returned non-empty for None")
    if jsonify({}) != '{}':
        raise Exception("jsonify returned non-empty for empty dictionary")
    if jsonify([]) != '[]':
        raise Exception("jsonify returned non-empty for empty list")

    if jsonify({"name": "John Doe"}) != '{"name": "John Doe"}':
        raise Exception("jsonify returned incorrect result")
    if jsonify(["first", "second"]) != '["first", "second"]':
        raise Exception("jsonify returned incorrect result")

    # Test formatting option
    if jsonify({"name": "John Doe"}, True) != '{\n    "name": "John Doe"\n}':
        raise Exception("jsonify returned incorrect result")
   

# Generated at 2022-06-13 07:21:18.201287
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1}, True) == '{\n    "a": 1\n}'
    assert jsonify({'b': 2}) == '{"b":2}'

# Generated at 2022-06-13 07:21:36.715685
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'
    assert jsonify({'x': 1, 'y': 2}) == '{"x": 1, "y": 2}'
    assert jsonify('{"x": 1, "y": 2}') == '"{\\"x\\": 1, \\"y\\": 2}"'
    assert jsonify(['a', {'b': {'c': 'd'}}, ['f', 1, 2]]) == '["a", {"b": {"c": "d"}}, ["f", 1, 2]]'
    assert jsonify({'x': [1, 2, 3], 'y': {'a': True, 'b': False}}) == '{"x": [1, 2, 3], "y": {"a": true, "b": false}}'
    assert jsonify

# Generated at 2022-06-13 07:21:40.905347
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 'foo', 'b': 'bar', 'c': None}
    assert jsonify(result) == '{"a": "foo", "b": "bar", "c": null}'
    assert jsonify(result, True) == '{\n    "a": "foo", \n    "b": "bar", \n    "c": null\n}\n'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:21:46.376456
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 5, 'b': 6}
    assert jsonify(result) == '{"a": 5, "b": 6}'
    assert jsonify(result, format=True) == '{\n    "a": 5, \n    "b": 6\n}'


# Generated at 2022-06-13 07:21:55.533176
# Unit test for function jsonify

# Generated at 2022-06-13 07:22:05.682625
# Unit test for function jsonify
def test_jsonify():
    from ansible import constants as C
    from ansible.module_utils import basic

    original_value = C.DEFAULT_TRANSFORM_INVALID_GROUP_CHARS
    C.DEFAULT_TRANSFORM_INVALID_GROUP_CHARS = False
    data = {'hello': 'world', 'foo': {'bar': 1}, 'list': [1, 2, 3]}
    valid_json = jsonify(data, True)
    assert valid_json == basic._json_dict_unicode_to_bytes(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))

    C.DEFAULT_TRANSFORM_INVALID_GROUP_CHARS = original_value

# Generated at 2022-06-13 07:22:13.089599
# Unit test for function jsonify
def test_jsonify():
    import tempfile
    from . import constants

    result = dict(changed=False, msg='', rc=0)
    results = [result]
    ansible_result = dict(contacted=results, dark=results)
    new_result = jsonify(ansible_result, format=True)
    assert new_result == constants.JSONIFY_RESULT_WITH_FORMAT

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(new_result)
    temp_file_name = temp_file.name
    temp_file.close()
    f = open(temp_file_name, 'r')
    read_json = json.load(f)
    assert read_json == constants.JSONIFY_RESULT_READ

    import os

# Generated at 2022-06-13 07:22:20.185019
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert jsonify(dict(foo=u'bar', bam=AnsibleUnsafeText(u'foo\'s bar')))=='{"bam": "foo\\u0027s bar", "foo": "bar"}'

    assert jsonify(dict(foo=u'bar'))=='{"foo": "bar"}'



# Generated at 2022-06-13 07:22:25.586800
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({1: 2}) == "{\"1\": 2}"
    assert jsonify({1: [2]}) == "{\"1\": [2]}"
    assert jsonify({1: [2]}, format=True) == "{\n    \"1\": [\n        2\n    ]\n}"

# Generated at 2022-06-13 07:22:39.987516
# Unit test for function jsonify
def test_jsonify():

    # None resultset
    result = jsonify(None)
    assert result == '{}'

    result = jsonify(None, True)
    assert result == '{}'

    # Real resultset
    real_result = {
        'changed': True,
        'test_key': 'test_value',
        'test_subd': {
            'subd_key': {
                'subd_sub_key': 'subd_sub_value',
                'subd_sub_key2': 'subd_sub_value2'
            }
        }
    }
    result = jsonify(real_result)

# Generated at 2022-06-13 07:22:42.815751
# Unit test for function jsonify
def test_jsonify():
    result = [{'foo': True, 'bar': False}]

    assert jsonify(result, True) == json.dumps(result, sort_keys=True, indent=4)
    assert jsonify(result) == json.dumps(result, sort_keys=True)

# Generated at 2022-06-13 07:23:00.626215
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify({"f\xc3\xa9e": "bar"}) == '{"f\xc3\xa9e": "bar"}'
    assert jsonify({"foo": "bar"}, True) == '{\n    "foo": "bar"\n}'
    assert jsonify({"\xc3\x9f": "foo"}, True) == '{\n    "\xc3\x9f": "foo"\n}'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:23:05.228518
# Unit test for function jsonify
def test_jsonify():
    import pytest

    test_data = {"test_data": True}
    assert jsonify(test_data) == '{"test_data": true}'
    assert jsonify(test_data, True) == '{\n    "test_data": true\n}'

    broken_json = "?"
    with pytest.raises(Exception):
        jsonify(broken_json)

# Generated at 2022-06-13 07:23:12.082650
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(1) == jsonify(1, True) == "1"
    assert jsonify([1, 2, 3]) == jsonify([1, 2, 3], True) == "[1, 2, 3]"
    assert jsonify({'a': 1, 'b': 2}) == jsonify({'a': 1, 'b': 2}, True) == '{"a": 1, "b": 2}'
    assert jsonify('{"a":"b"}') == jsonify('{"a":"b"}', True) == '"{\\"a\\":\\"b\\"}"'

# Generated at 2022-06-13 07:23:16.447083
# Unit test for function jsonify
def test_jsonify():
    result = {"changed": True,
            "comment": "something",
            "name": "somethingelse"}
    assert jsonify(result, True) == '''{
    "changed": true,
    "comment": "something",
    "name": "somethingelse"
}'''
    assert jsonify(result, False) == '{"changed": true, "comment": "something", "name": "somethingelse"}'

# Generated at 2022-06-13 07:23:26.405599
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleUnicode
    data = {
        'a': 1,
        'b': 'foo',
        'c': True,
        'd': { 'a': 2.1, 'b': 2.2 },
        'e': [ 1, 2, 3],
        'f': AnsibleUnsafeText(u'Jos\xe9'),
        'g': AnsibleUnicode('Jos\xc3\xa9'),
    }
    result_json = jsonify(data)
    assert json.loads(result_json) == data
    result_jsonf = jsonify(data, format=True)
    assert json.loads(result_jsonf) == data
    assert result_jsonf

# Generated at 2022-06-13 07:23:36.726207
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.jsonify import jsonify
    from ansible.utils import pycompat
    import json

    if not pycompat.PY3:
        data = [u'one', u'two', u'three']
    else:
        data = [b'one', b'two', b'three']

    output = jsonify(data, True)
    assert output == '[\n    "one", \n    "two", \n    "three"\n]'

    if not pycompat.PY3:
        output = jsonify(data, False)
        assert output == '["one", "two", "three"]'

        output = jsonify(u'test')
        assert output == '"test"'

        output = jsonify(u'snowman: \u2603')

# Generated at 2022-06-13 07:23:40.367465
# Unit test for function jsonify
def test_jsonify():
    a = { 'a': 1, 'b': 2 }
    assert jsonify(a) == "{}"
    assert jsonify(a, format=True) == "{}"

# Generated at 2022-06-13 07:23:47.648471
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b': 2}, True) == u'{\n    "a": 1,\n    "b": 2\n}'
    assert jsonify({'a': 1, 'b': 2}, False) == u'{"a": 1, "b": 2}'
    assert jsonify(None, False) == u'{}'

# Generated at 2022-06-13 07:23:55.175564
# Unit test for function jsonify
def test_jsonify():
    result = { "foo" : "bar" }
    assert jsonify(result) == '{"foo": "bar"}'
    assert jsonify(result, format=True) == '{\n    "foo": "bar"\n}'

    # Unicode test
    result = { "f\xe5o" : "bar" }
    assert jsonify(result) == '{"f\xc3\xa5o": "bar"}'
    assert jsonify(result, format=True) == '{\n    "f\xc3\xa5o": "bar"\n}'

# Generated at 2022-06-13 07:24:04.376236
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({ "foo": "bar", "this": "that", "1": 5 })
    assert result == '{"1": 5, "foo": "bar", "this": "that"}'

    # This will normally throw the exception.
    nonascii = "문자 추가".encode("utf-8")
    result = jsonify({ "key": nonascii })
    assert result == '{"key": "문자 추가"}'

    result = jsonify({ "key": nonascii }, format=True)
    assert result == '{\n    "key": "문자 추가"\n}'

# Generated at 2022-06-13 07:24:30.311436
# Unit test for function jsonify
def test_jsonify():
    test_dict = { 'a': 1, 'b': [2, 3], 'c': { 'd': 4, 'e': [5, 6] } }
    test_string = jsonify(test_dict)
    assert 'b' in test_string
    assert '[2, 3]' in test_string
    assert 'e' in test_string
    assert '4' in test_string


# Generated at 2022-06-13 07:24:42.057214
# Unit test for function jsonify
def test_jsonify():

    # test empty dict
    assert "{}" == jsonify(None)
    assert "{}" == jsonify({})

    # test plain dict
    assert '{"a": 1}' == jsonify({"a": 1})
    assert '{"a": 2}' == jsonify({"a": 2})

    # test indenting
    assert """{
    "a": 2
}""" == jsonify({"a": 2}, format=True)

    # test list
    assert "[1, 2, 3]" == jsonify([1,2,3])
    assert '["a", "b", "c"]' == jsonify(["a","b","c"])

    # test unicode
    assert '{"a": "\\u03b1"}' == jsonify({"a": u"\u03b1"})


# Generated at 2022-06-13 07:24:46.007523
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify: basic functionality
    '''
    assert jsonify(None) == '{}'
    assert jsonify({ 'a': 1, 'b': 2 }) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:24:49.965585
# Unit test for function jsonify
def test_jsonify():
    ''' unit tests for jsonify function '''

    from ansible.module_utils import basic
    from ansible.module_utils.six import BytesIO

    # Test catching exception when unable to serialize to unicode
    test_obj = {"test": BytesIO()}
    assert isinstance(jsonify(test_obj), basestring) is True

# Generated at 2022-06-13 07:25:00.438131
# Unit test for function jsonify
def test_jsonify():
    """ Test jsonify function. """

    import unittest
    import sys
    import os

    PY3 = sys.version_info[0] == 3
    if PY3:
        # On Python 3 we need to convert the string to bytes
        PlainString = str
    else:
        # On python 2 we need to convert the string to unicode
        PlainString = unicode

    class TestJsonify(unittest.TestCase):

        def test_jsonify(self):
            ''' test jsonify'''

            result = dict(changed=True, rc=0, stdout="foo", stderr="bar")

# Generated at 2022-06-13 07:25:03.233310
# Unit test for function jsonify
def test_jsonify():
    result = {}

    # We can't compare JSON strings directly, so use a dictionary
    assert json.loads(jsonify(result)) == result
    assert json.loads(jsonify(result, True)) == result

    result = {"foo": "one", "bar": "two"}

    assert json.loads(jsonify(result)) == result
    assert json.loads(jsonify(result, True)) == result

# Generated at 2022-06-13 07:25:07.091721
# Unit test for function jsonify
def test_jsonify():
    tests = [(None, "{}"),
             (['foo', 'bar'], '["bar", "foo"]'),
             ({"a": "b"}, '{"a": "b"}')]
    for test, expected in tests:
        result = jsonify(test)
        if result != expected:
            print("Error: expecting %s, got %s" % (expected, result))
            return False
    return True

if __name__ == '__main__':
    import sys
    import pdb
    if not test_jsonify():
        sys.exit(1)

# Generated at 2022-06-13 07:25:10.861213
# Unit test for function jsonify
def test_jsonify():
    b_value = {u'changed': True, u'reboot_required': False, u'reboot_required_command': u'init 6'}
    a_value = {'changed': True, 'reboot_required': False, 'reboot_required_command': 'init 6'}

    assert jsonify(b_value) == jsonify(a_value)

# Generated at 2022-06-13 07:25:15.841550
# Unit test for function jsonify
def test_jsonify():
    import types

    test_value = { 'foo': 'bar' }
    test_data = (
        (test_value, False),
        (test_value, True),
    )

    for value, format in test_data:
        result = jsonify(value, format=format)
        assert result is not None
        assert type(result) == types.StringType

    # Test that None is handled correctly
    result = jsonify(None)
    assert result == "{}"

# Generated at 2022-06-13 07:25:20.775766
# Unit test for function jsonify
def test_jsonify():
    result = dict(foo=1, bar=2)
    result_compressed  = jsonify(result)
    result_uncompressed  = jsonify(result, format=True)
    assert result_compressed == result_uncompressed == '{"bar": 2, "foo": 1}'

    nil_result = None
    nil_compressed_result = jsonify(nil_result)
    nil_uncompressed_result = jsonify(nil_result, format=True)
    assert nil_compressed_result == nil_uncompressed_result == '{}'

# Generated at 2022-06-13 07:26:04.694774
# Unit test for function jsonify
def test_jsonify():
    ''' returns the result of jsonify from a dictionary '''
    from ansible.utils import jsonify as jsonify_util
    result = {'host': '127.0.0.1', 'connection': 'local'}
    return jsonify_util.jsonify(result)

# Generated at 2022-06-13 07:26:13.699610
# Unit test for function jsonify
def test_jsonify():
    data = {'status': 'ok', 'results': []}
    assert jsonify(data) == '{"results": [], "status": "ok"}'
    assert jsonify(data, format=True) == '{\n    "results": [], \n    "status": "ok"\n}'

    data = {'status': 'ok', 'results': [1, 2, 3, 4]}
    assert jsonify(data) == '{"results": [1, 2, 3, 4], "status": "ok"}'
    assert jsonify(data, format=True) == '{\n    "results": [\n        1, \n        2, \n        3, \n        4\n    ], \n    "status": "ok"\n}'

    data = None
    assert jsonify(data) == "{}"
   

# Generated at 2022-06-13 07:26:17.461771
# Unit test for function jsonify
def test_jsonify():
    # testing no options
    assert jsonify(None) == '{}'

    # testing format
    assert jsonify(None, True) == '{}'

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:26:21.212540
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(5) == '5'
    assert jsonify('hello') == '"hello"'
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:26:27.083593
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    test_input = dict(a=1, b=2, c=[3, 4, AnsibleUnsafeText('\x00')])
    try:
        test_output = json.loads(jsonify(test_input))
    except ValueError:
        assert False, 'jsonify() call returned non-JSON output'

    assert test_output == test_input, 'jsonify() call returned incomplete or otherwise incorrect output'

# Generated at 2022-06-13 07:26:28.272923
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == "{}"


# Generated at 2022-06-13 07:26:34.451748
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed=False, failed=False, msg='')
    result['foo'] = 'bar'
    # test with format=True
    assert jsonify(result, format=True) == '{\n    "changed": false, \n    "failed": false, \n    "foo": "bar", \n    "msg": ""\n}'
    # test with format=False
    assert jsonify(result, format=False) == '{"msg": "", "foo": "bar", "failed": false, "changed": false}'
    # test with result=None
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:26:44.378835
# Unit test for function jsonify
def test_jsonify():

    """
    test_jsonify: function provides a unit test over this behaviour
    """

    def assert_equals(x, y):
        return x == y

    result = jsonify({"a": 1, "b": 2}, True)
    assert_equals('    {\n        "a": 1, \n        "b": 2\n    }', result)

    result = jsonify(None)
    assert_equals('{}', result)

    result = jsonify({"a": 1, "b": 2}, False)
    assert_equals('{"a": 1, "b": 2}', result)

    result = jsonify({})
    assert_equals('{}', result)

# Generated at 2022-06-13 07:26:46.495427
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'b'}) == '{"a": "b"}'

# Generated at 2022-06-13 07:26:49.109241
# Unit test for function jsonify
def test_jsonify():
    print(jsonify({'test': ['1','2','3']}))
    print(jsonify({'test': ['1','2','3']}, format=True))

if __name__ == '__main__':
    test_jsonify()