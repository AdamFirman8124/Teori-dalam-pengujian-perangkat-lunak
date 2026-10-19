

# Generated at 2022-06-13 07:17:32.856488
# Unit test for function jsonify
def test_jsonify():

    # We will write tests for this function as it gets used more
    #assert False
    return

# Generated at 2022-06-13 07:17:35.825167
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({ 'foo': 'bar' })  == '{"foo": "bar"}'
    assert jsonify({ 'foo': 'bar' }, True)  == '{\n    "foo": "bar"\n}'
    assert jsonify(None)  == '{}'

# Generated at 2022-06-13 07:17:40.750564
# Unit test for function jsonify
def test_jsonify():
    result = {'a': {'b': 'c'}}
    assert jsonify(result, True) == '''{
    "a": {
        "b": "c"
    }
}
'''
    assert jsonify(result) == '{"a": {"b": "c"}}'
    assert jsonify(None) == '{}'

# FIXME: not even used in this file anymore

# Generated at 2022-06-13 07:17:46.110279
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 'bar'}

    # test with format=False
    assert jsonify(result, format=False) == '{"foo": "bar"}'

    # test with format=True
    assert jsonify(result, format=True) == '{\n    "foo": "bar"\n}'

    # test with result=None
    assert jsonify(None, format=False) == '{}'


test_jsonify()

# Generated at 2022-06-13 07:17:47.925935
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:17:58.284398
# Unit test for function jsonify
def test_jsonify():
    def _compare(a, b):
        return json.loads(a) == json.loads(b)

    assert _compare(jsonify({'a': 'b'}), '{"a": "b"}')
    assert _compare(jsonify({u'a': u'b'}), '{"a": "b"}')
    assert _compare(jsonify({'a': [1, 2, 3]}), '{"a": [1, 2, 3]}')
    assert _compare(jsonify({'a': {'b': {'c': 'd'}}}), '{"a": {"b": {"c": "d"}}}')
    assert _compare(jsonify({'a': 'b'}, True), '{\n    "a": "b"\n}')

# Generated at 2022-06-13 07:18:04.442981
# Unit test for function jsonify
def test_jsonify():

    data = {
        'foo' : 'bar',
        'spam' : 'eggs',
        'lorem_ipsum' : {
            'dolor': 'sit amet',
            'consectetur': 'adipiscing elit',
            'sed': 'do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        },
        'a': None
    }


# Generated at 2022-06-13 07:18:12.300462
# Unit test for function jsonify
def test_jsonify():
    test1 = jsonify(dict(failed=True, changed=False, msg="This is a test"))
    assert test1 == '{\n    "changed": false,\n    "failed": true,\n    "msg": "This is a test"\n}'
    test2 = jsonify(dict(failed=True, changed=False, msg="This is a test"), False)
    assert test2 == '{"failed": true, "changed": false, "msg": "This is a test"}'
    test3 = jsonify(None)
    assert test3 == "{}"

# Generated at 2022-06-13 07:18:15.059627
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'

    assert jsonify({'a': 'b'}) == '{"a": "b"}'

    assert jsonify({'a': 'b'}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:18:24.638249
# Unit test for function jsonify
def test_jsonify():
    # Test jsonify function
    assert jsonify(dict(changed=False, rc=1)) == '{"changed": false, "rc": 1}'
    assert jsonify(dict(changed=False, rc=1, debug=dict(value=1))) == '{"changed": false, "debug": {"value": 1}, "rc": 1}'
    assert jsonify(dict(changed=False, rc=1), format=True) == '{\n    "changed": false,\n    "rc": 1\n}'
    assert jsonify(dict(changed=False, object=1)) == '{"changed": false, "object": 1}'
    assert jsonify(dict(changed=True, actions=[1, 2, 3])) == '{"actions": [1, 2, 3], "changed": true}'

# Generated at 2022-06-13 07:18:33.651578
# Unit test for function jsonify
def test_jsonify():
    result = { 'foo': 'bar' }
    result_fmt = jsonify(result, True)
    result_unfmt = jsonify(result, False)
    assert(result_fmt == '''{
    "foo": "bar"
}''')
    assert(result_unfmt == '{"foo": "bar"}')

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:18:38.400584
# Unit test for function jsonify
def test_jsonify():
    test_dict = {'a': 'b', 'c': {'nested':'dictionary'}}

    assert jsonify(test_dict)       == '{"a": "b", "c": {"nested": "dictionary"}}'
    assert jsonify(test_dict, True) == '''{
    "a": "b",
    "c": {
        "nested": "dictionary"
    }
}'''

# Generated at 2022-06-13 07:18:41.776803
# Unit test for function jsonify
def test_jsonify():
    ''' unit tests for jsonify()'''
    assert jsonify(None) == '{}'
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'
    assert jsonify({'foo': 'bar'}, False) == '{"foo": "bar"}'

if __name__ == '__main__':
    import sys
    import doctest
    import json
    (failure_count, test_count) = doctest.testmod()
    sys.exit(failure_count)

# Generated at 2022-06-13 07:18:42.696490
# Unit test for function jsonify
def test_jsonify():
    import copy
    copy.copy({})

# Generated at 2022-06-13 07:18:54.231744
# Unit test for function jsonify
def test_jsonify():

    result = {
        "random": {
            "k1": "v1",
            "ak2": ["vv1", "vv2"],
            "ik1": 1,
        },
        "other": {
            "k2": "v2",
        }
    }

    output = jsonify(result)
    assert output == '{"other": {"k2": "v2"}, "random": {"ak2": ["vv1", "vv2"], "ik1": 1, "k1": "v1"}}'

    output = jsonify(result, format=True)

# Generated at 2022-06-13 07:19:05.314102
# Unit test for function jsonify
def test_jsonify():
    ''' `jsonify` function returns a json stringified value.

        inputs are tested as both unicode and string, with format True and False,
        and with both ascii and non-ascii characters.
    '''

    test_value_u    = u"{ 'key': 'value' }"
    test_value_s    = "{ 'key': 'value' }"
    test_value_ascii_u = "{ 'key': 'value' }"
    test_value_ascii_s = "{ 'key': 'value' }"
    test_value_non_ascii_u = u"{ 'key': 'v\xc3\xa6l\xc3\xb8\xc3\xa9' }"

# Generated at 2022-06-13 07:19:18.456327
# Unit test for function jsonify
def test_jsonify():

    data = { 'a': 'foo', 'b': [1, 2, 3, 'cow'], 'c': {'cow': 'moo'}}
    result = jsonify(data)

    # test when formatting is on
    formatted_result = jsonify(data, True)

    assert result == '{"a": "foo", "b": [1, 2, 3, "cow"], "c": {"cow": "moo"}}'
    assert formatted_result == '{\n    "a": "foo", \n    "b": [\n        1, \n        2, \n        3, \n        "cow"\n    ], \n    "c": {\n        "cow": "moo"\n    }\n}'

# Generated at 2022-06-13 07:19:25.184652
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": ["A", "B", "C"]}) == '{"a": ["A", "B", "C"]}', "Should be the same"
    assert jsonify({"a": ["A", "B", "C"]}, format=True) == '''{
    "a": [
        "A",
        "B",
        "C"
    ]
}''', "Should be the same"
    assert jsonify(None) == '{}', "Should be the same"

# Generated at 2022-06-13 07:19:31.106696
# Unit test for function jsonify
def test_jsonify():
    inp = dict(a='hello', b=['a', 'b', 'c'], c=3)
    outp = '{"a": "hello", "b": ["a", "b", "c"], "c": 3}'
    assert jsonify(inp) == outp
    assert jsonify(inp, format=True) == '''{
    "a": "hello",
    "b": [
        "a",
        "b",
        "c"
    ],
    "c": 3
}'''

# Test for non-ASCII

# Generated at 2022-06-13 07:19:34.962244
# Unit test for function jsonify
def test_jsonify():
    # Test None returns correct result
    assert jsonify(None) == "{}"

    # Test jsonify format (4 spaces indent)
    assert jsonify({'a':'b'}, format=True) == '{\n    "a": "b"\n}'
    assert jsonify(None, format=True) == "{}"

    # Test jsonify with unicode
    assert jsonify({u'a': u'b'}, format=False) == '{"a": "b"}'


# Generated at 2022-06-13 07:19:40.369870
# Unit test for function jsonify
def test_jsonify():
    x = jsonify({'a': 'b'})
    y = {'a': 'b'}

    assert json.loads(x) == y

# Generated at 2022-06-13 07:19:50.707288
# Unit test for function jsonify
def test_jsonify():
    # This is not really a unit test, but rather a sanity check for those working on the module
    # it will output the results of the jsonify() function for review.
    #
    # Example:
    #
    #    python lib/ansible/module_utils/basic.py
    #
    # --------------------------------------------------------------------
    from pprint import pprint

    result = {
        "banana": "good",
        "apple": True,
        "lemon": 12,
        "orange": 12.2
    }

    print("Result to jsonify()")
    pprint(result)
    print("-" * 80)
    print("result of jsonify(result)")
    print(jsonify(result))
    print("-" * 80)
    print("result of jsonify(result, True)")

# Generated at 2022-06-13 07:20:01.564833
# Unit test for function jsonify
def test_jsonify():
    from ansible import constants as C
    from ansible.utils import jsonify
    C.DEFAULT_MODULE_LANG = 'en_US.UTF-8'
    C.DEFAULT_MODULE_LANG = 'en_US.UTF-8'
    res = dict(changed=False, foo='bar')
    assert jsonify(res) == '{"changed": false, "foo": "bar"}'
    assert jsonify(res, True) == '{\n    "changed": false, \n    "foo": "bar"\n}'

    # non-ascii char
    res = dict(changed=False, foo='ça va')
    assert jsonify(res) == u'{"changed": false, "foo": "ça va"}'


# Generated at 2022-06-13 07:20:04.547805
# Unit test for function jsonify
def test_jsonify():
    results = {'a':1, 'b':2, 'c':{'c1':3,'c2':4}}
    assert jsonify(results) == '{"a": 1, "c": {"c1": 3, "c2": 4}, "b": 2}'

# Generated at 2022-06-13 07:20:08.598853
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=dict(b='c', d=dict(e=1)))) == '{"a": {"b": "c", "d": {"e": 1}}}'
    assert jsonify({'a': {'b': 'c', 'd': {'e': 1}}}, True) == '{\n    "a": {\n        "b": "c",\n        "d": {\n            "e": 1\n        }\n    }\n}'

# Generated at 2022-06-13 07:20:14.671169
# Unit test for function jsonify
def test_jsonify():
    # testing for valid json
    assert '"foo": "bar"' in jsonify({'foo': 'bar'}, format=True)
    # testing for valid json with unicode
    assert '"foo": "bar"' in jsonify({'foo': 'bar'.decode('utf-8')}, format=True)
    # testing for valid json unicode returned as ascii
    assert '"foo": "bar"' in jsonify({'foo': 'bar'.decode('utf-8')})

# Generated at 2022-06-13 07:20:25.025140
# Unit test for function jsonify
def test_jsonify():
    # tests for indenting
    result = dict(changed=True, failed=False, rc=0)
    assert jsonify(result, format=False) == '{"failed": false, "changed": true, "rc": 0}'
    assert jsonify(result, format=True) == '{\n    "changed": true, \n    "failed": false, \n    "rc": 0\n}'

    # tests for unicode decoding, should work both in python2 and python3
    result = dict(changed=True, failed=False, rc=0, results=dict(a=1, b=2, c=3))
    assert jsonify(result, format=False) == '{"results": {"a": 1, "c": 3, "b": 2}, "failed": false, "changed": true, "rc": 0}'
    assert json

# Generated at 2022-06-13 07:20:36.296385
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    result = dict(foo=1, bar=2)
    out1 = jsonify(result)
    assert out1 == "{\"bar\": 2, \"foo\": 1}"
    out2 = jsonify(result, format=True)
    assert out2 == "{\n    \"bar\": 2,\n    \"foo\": 1\n}"
    result = dict(foo=1, bar=AnsibleUnsafeText("unsafe"))
    out1 = jsonify(result)
    assert out1 == "{\"bar\": \"unsafe\", \"foo\": 1}"
    out2 = jsonify(result, format=True)
    assert out2 == "{\n    \"bar\": \"unsafe\",\n    \"foo\": 1\n}"

# Generated at 2022-06-13 07:20:40.964752
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1}) == '{"a": 1}'
    assert jsonify({'a': 1}, format=True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:20:54.809227
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    from ansible.module_utils._text import to_text
    result = {u'foo': u'bar', to_text(u'foo'): to_text(u'bar')}
    result_json = jsonify(result)
    assert result_json == '{"foo": "bar"}'
    result_json = jsonify(result, True)
    assert result_json == '{\n    "foo": "bar"\n}'
    result_json = jsonify(to_unicode(result))
    assert result_json == '{"foo": "bar"}'
    result_json = jsonify(to_unicode(result), True)
    assert result_json == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:21:06.473014
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a': 1, 'b': 2}, format=True) == '{\n    "a": 1,\n    "b": 2\n}'


# Generated at 2022-06-13 07:21:09.415344
# Unit test for function jsonify
def test_jsonify():
    a_string = '{"a":1,"b":2}'
    a_dict = json.loads(a_string)
    assert jsonify(a_string) == a_string
    assert jsonify(a_dict) == a_string



# Generated at 2022-06-13 07:21:13.958294
# Unit test for function jsonify
def test_jsonify():
    # Testing for Jsonify function
    from ansibullbot.utils.jsonify import jsonify
    j = jsonify({'foo': 'bar'})
    assert j == '{"foo": "bar"}'

    j = jsonify({'foo': 'bar'}, format=True)
    assert j == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:21:19.200168
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify("{}") == "\"{}\""
    assert jsonify("{\"my\": \"values\"}") == "\"{\\\"my\\\": \\\"values\\\"}\""
    assert jsonify("{\"my\": [\"values\", \"are\", \"here\"]}") == "\"{\\\"my\\\": [\\\"values\\\", \\\"are\\\", \\\"here\\\"]}\""
    assert jsonify({'my': 'values'}) == "{\"my\": \"values\"}"
    assert jsonify("{\"my\": \"values\"}", format=True) == jsonify("{\"my\": \"values\"}", format=False)

# Generated at 2022-06-13 07:21:23.920951
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:21:26.431213
# Unit test for function jsonify
def test_jsonify():
    assert '"foo": "bar"' in jsonify({'foo': 'bar'})
    assert '"foo": "bar"' in jsonify({'foo': 'bar'}, True)

# Generated at 2022-06-13 07:21:28.029018
# Unit test for function jsonify
def test_jsonify():
    result = { 'test': [ { 'a': 1, 'b': 2 } ] }
    print ("%s" % jsonify(result, True))

# Generated at 2022-06-13 07:21:33.228593
# Unit test for function jsonify
def test_jsonify():

    # Test with no indentation
    sample_data = {"foo": ["bar", "baz"], "bam": {"baz": "bar"}}
    expected_output = '{"foo": ["bar", "baz"], "bam": {"baz": "bar"}}'
    assert jsonify(sample_data) == expected_output

    # Test with indentation
    sample_data = {"foo": ["bar", "baz"], "bam": {"baz": "bar"}}
    expected_output = '''{
    "foo": [
        "bar",
        "baz"
    ],
    "bam": {
        "baz": "bar"
    }
}'''
    assert jsonify(sample_data, True) == expected_output

# Generated at 2022-06-13 07:21:41.429168
# Unit test for function jsonify
def test_jsonify():
    result = {'a':1, 'b':[1,2,3], 'c':{'d':{'e':'f','g':'h','i':'j'}}}
    assert jsonify(result, False) == '{"a": 1, "b": [1, 2, 3], "c": {"d": {"g": "h", "e": "f", "i": "j"}}}'
    assert jsonify(result, True) == '{\n    "a": 1, \n    "b": [\n        1, \n        2, \n        3\n    ], \n    "c": {\n        "d": {\n            "g": "h", \n            "e": "f", \n            "i": "j"\n        }\n    }\n}'

# Generated at 2022-06-13 07:21:47.812669
# Unit test for function jsonify
def test_jsonify():

    test_hash = dict(
        ansible_facts = dict(
            one = 1
        ),
        ansible_facts_cacheable = dict(
            two = 2
        )
    )

    # Compare with non-pretty
    expected = '{"ansible_facts": {"one": 1}, "ansible_facts_cacheable": {"two": 2}}'
    result = jsonify(test_hash)
    assert expected == result

    expected = '{\n' + \
               '    "ansible_facts": {\n' + \
               '        "one": 1\n' + \
               '    },\n' + \
               '    "ansible_facts_cacheable": {\n' + \
               '        "two": 2\n' + \
               '    }\n' + \
               '}'
   

# Generated at 2022-06-13 07:22:09.946300
# Unit test for function jsonify
def test_jsonify():
    from ansible.compat.tests import unittest

    class TestJsonify(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_jsonify(self):

            expected_formatted_json = '''{
    "a": "b",
    "c": [
        "d",
        "e"
    ]
}'''

            expected_json = '{"a": "b", "c": ["d", "e"]}'

            self.assertEqual(expected_json, jsonify({'a': 'b', 'c':['d', 'e']}))
            self.assertEqual(expected_formatted_json, jsonify({'a': 'b', 'c':['d', 'e']}, format=True))

   

# Generated at 2022-06-13 07:22:21.619404
# Unit test for function jsonify
def test_jsonify():
    from ansible.template import Templar
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    def load_result(result):
        return json.loads(result)

    module = AnsibleModule(argument_spec={})
    templar = Templar(loader=DataLoader(), variables={})

    result = jsonify({'foo': 'bar'})
    assert type(load_result(result)) == dict
    assert load_result(result) == {'foo': 'bar'}

    result = jsonify({'foo': ['bar', 'baz']})
    assert type(load_result(result)) == dict

# Generated at 2022-06-13 07:22:29.496148
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed=False, rc=0)
    assert jsonify(result, format=True) == '''{
    "changed": false,
    "rc": 0
}'''
    assert jsonify(result, format=False) == '{"changed":false,"rc":0}'
    assert jsonify(result, format=0) == '{"changed":false,"rc":0}'
    assert jsonify(result, format=1) == '''{
    "changed": false,
    "rc": 0
}'''
    assert jsonify(result, format=2) == '''{
    "changed": false,
    "rc": 0
}'''
    result = dict(changed=False, rc=0, results=dict(a=1, b=2, c=3))

# Generated at 2022-06-13 07:22:43.703111
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''


# Generated at 2022-06-13 07:22:48.339660
# Unit test for function jsonify
def test_jsonify():
    # Test for None input
    assert jsonify(None) == "{}"

    # Test for dictionary input
    assert jsonify({u'foo': u'bar', u'baz': u'foo'}) == '{\n    "baz": "foo", \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:22:59.731308
# Unit test for function jsonify
def test_jsonify():
    # Test with None
    result = jsonify(None)
    assert result == "{}"

    # Test with scalar
    result = jsonify('foo')
    assert result == '"foo"'

    # Test with list
    result = jsonify([1, 2, 3])
    assert result == '[1, 2, 3]'

    # Test with dict
    result = jsonify({'a' : 1, 'b' : 2})
    assert result == '{"a": 1, "b": 2}'

    # Test with list w/indentation
    result = jsonify([1, 2, 3], True)
    assert result == '[\n    1,\n    2,\n    3\n]'

    # Test with dict w/indentation

# Generated at 2022-06-13 07:23:02.250500
# Unit test for function jsonify
def test_jsonify():
    json_data = jsonify({"foo": "bar"})
    data = json.loads(json_data)
    assert 'foo' in data
    assert data['foo'] == 'bar'

# Generated at 2022-06-13 07:23:08.297990
# Unit test for function jsonify
def test_jsonify():
    class Test(object):
        def __init__(self, value):
            self.value = value

        def __json__(self):
            return self.value

    test_object = Test('test_value')
    result = {
        'ansible_facts': {
            'test_key': 'test_value',
            'test_object': test_object,
        },
    }
    jsonified_result = jsonify(result, True)
    assert jsonified_result == """{
    "ansible_facts": {
        "test_key": "test_value",
        "test_object": "test_value"
    }
}"""

# Generated at 2022-06-13 07:23:17.260699
# Unit test for function jsonify
def test_jsonify():
    results = jsonify({})
    assert results == '{}'

    results = jsonify(None)
    assert results == '{}'

    results = jsonify({'a': {'b': 1 }})
    assert results == '{"a": {"b": 1}}'

    results = jsonify({'a': {'b': 1 }}, format=True)
    assert results == '{\n    "a": {\n        "b": 1\n    }\n}'

    results = jsonify({'a': {'b': 1 }}, format=True)
    assert results == '{\n    "a": {\n        "b": 1\n    }\n}'

    results = jsonify({'a': {'b': u'\u2019' }}, format=True)

# Generated at 2022-06-13 07:23:20.881865
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for function jsonify '''

    test = {}
    assert jsonify(test) == "{}"

    test = {'a': 'b'}
    assert jsonify(test, True) == """{
    \"a\": \"b\"
}"""

# Generated at 2022-06-13 07:23:48.353496
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"hello": "world"}) == '{"hello": "world"}'
    assert jsonify({"hello": "world"}, True) == '''{
    "hello": "world"
}'''

# Generated at 2022-06-13 07:23:55.604336
# Unit test for function jsonify
def test_jsonify():
    import re

    results = {}
    results['success'] = True
    results['changed'] = False
    results['msg'] = "yo"
    results['ignored'] = "Failed as requested from time to time"
    results['failed']   = False
    results['ansible_facts'] = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5],
        'd': { 'e': 6 }
    }
    results['ansible_facts']['c'].append(results['ansible_facts']['d'])
    results['_ansible_no_log'] = False

    out1 = jsonify(results)
    results['_ansible_verbose_override'] = True
    results['_ansible_no_log'] = True

# Generated at 2022-06-13 07:24:05.819096
# Unit test for function jsonify
def test_jsonify():

    # Test with a bunch of basic scalars
    assert jsonify(1) == '1'
    assert jsonify(True) == 'true'
    assert jsonify(None) == 'null'

    # Test with a bunch of complex data types
    d1 = { "k1": "foo", "k2": "bar" }
    assert jsonify(d1) == '{"k1": "foo", "k2": "bar"}'
    d2 = [ "foo", "bar", 123 ]
    assert jsonify(d2) == '["foo", "bar", 123]'
    d3 = [ { "k1": "foo" }, { "k2": "bar" } ]
    assert jsonify(d3) == '[{"k1": "foo"}, {"k2": "bar"}]'

# Generated at 2022-06-13 07:24:07.623038
# Unit test for function jsonify
def test_jsonify():
    result = jsonify(
        {"msg": "Hello", "changed": True}, True)
    print(result)

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:24:13.791206
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'

    assert jsonify({'a': 1, 'b': 2}, format=True) == """{
    "a": 1,
    "b": 2
}"""

#
# ----- end of library file ----
#

# Generated at 2022-06-13 07:24:17.732082
# Unit test for function jsonify
def test_jsonify():
    import ansible.callbacks as callbacks
    assert isinstance(callbacks.jsonify({"foo": "bar"}), basestring)
    assert isinstance(callbacks.jsonify({}), basestring)
    assert isinstance(callbacks.jsonify(None), basestring)

# Generated at 2022-06-13 07:24:22.998944
# Unit test for function jsonify
def test_jsonify():

    test_result = { "key1": "value1", "key2": "value2"}

    assert jsonify(test_result) == '{"key2": "value2", "key1": "value1"}'

    assert jsonify(test_result, True) == '{\n    "key2": "value2", \n    "key1": "value1"\n}'

# Generated at 2022-06-13 07:24:33.784443
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic
    from ansible.executor.task_result import TaskResult

    data = {
        "skipped": False,
        "changed": True,
        "diff": {
            "before": {
                "opt1": "foo",
                "dict1": {
                    "key1": "foo",
                    "key2": "bar"
                }
            },
            "after": {
                "opt1": "bar",
                "dict1": {
                    "key1": "bar",
                    "key2": "bar"
                }
            }
        }
    }

# Generated at 2022-06-13 07:24:36.494238
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": "b"}) == '{"a": "b"}'
    assert jsonify({"a": "b"}, True) == '{\n    "a": "b"\n}'
    assert jsonify(None) == "{}"



# Generated at 2022-06-13 07:24:38.772380
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":1}) == "{\"a\": 1}"
    assert jsonify({"a":1}, True) == "{\n    \"a\": 1\n}"

# Generated at 2022-06-13 07:25:33.527079
# Unit test for function jsonify
def test_jsonify():
    result = { "foo": [ 1,2,3, { 'a': 'b','c': { 'd': 'e', 'f': [ 1,2,3 ] } } ], "bar": { '1': '2','3': { '4': '5', '6': [ 7,8,9 ] } } }

# Generated at 2022-06-13 07:25:42.591132
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for function jsonify '''

    assert jsonify({}) == "{}"
    assert jsonify(None) == "{}"

    assert jsonify({'test':'test'}) == '{"test": "test"}'
    assert jsonify({'test':'test'}, True) == '{\n    "test": "test"\n}'

    assert jsonify({'test':{'test':'test'}}) == '{"test": {"test": "test"}}'
    assert jsonify({'test':{'test':'test'}}, True) == '{\n    "test": {\n        "test": "test"\n    }\n}'

    assert jsonify({'test':[1,2,3]}) == '{"test": [1, 2, 3]}'

# Generated at 2022-06-13 07:25:55.928651
# Unit test for function jsonify
def test_jsonify():
    result = {
        'failed': False,
        'msg': 'success',
        'changed': True,
        'failed_hosts': {},
        'skipped_hosts': {},
        'contacted': {
            'localhost': {
                'failed': False,
                'msg': 'success',
                'changed': True,
                'rc': 0
            }
        }
    }
    assert jsonify(result) == '{"contacted": {"localhost": {"msg": "success", "failed": false, "changed": true, "rc": 0}}, "skipped_hosts": {}, "failed_hosts": {}, "msg": "success", "changed": true, "failed": false}'

# Generated at 2022-06-13 07:26:03.679749
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify("echo") == '"echo"'
    assert jsonify("{}") == '"{}"'
    assert jsonify({"a":"b", "c":"d"}) == '{"a": "b", "c": "d"}'
    assert jsonify({"a":"b", "c":"d"}, True) == '{\n    "a": "b", \n    "c": "d"\n}'

# Generated at 2022-06-13 07:26:09.563541
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == "{}"
    assert jsonify(None) == "{}"
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": "1"}) == '{"a": "1"}'
    assert jsonify({"a": "1"}, True) == '{\n    "a": "1"\n}'

# Generated at 2022-06-13 07:26:10.647132
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'

# Generated at 2022-06-13 07:26:14.457328
# Unit test for function jsonify
def test_jsonify():
    data = {'foo': 'bar'}

    result = jsonify(data)
    assert result == '{"foo": "bar"}'

    result = jsonify(data, format=True)
    assert result == '{\n    "foo": "bar"\n}'

    result = jsonify(None)
    assert result == "{}"

# Generated at 2022-06-13 07:26:19.433172
# Unit test for function jsonify
def test_jsonify():
    result = {
        "failed": True,
        "parsed": False
    }
    json_result = jsonify(result)
    assert result == json.loads(json_result)

    json_result = jsonify(result, format=True)
    assert result == json.loads(json_result)

# Generated at 2022-06-13 07:26:22.554008
# Unit test for function jsonify
def test_jsonify():
    result = { 'a': 'hello world', 'b': 2 }
    assert( jsonify(result, format=True) == '{\n    "a": "hello world", \n    "b": 2\n}' )

# Generated at 2022-06-13 07:26:25.032306
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a': 1}, True) == '{\n    "a": 1\n}\n'
