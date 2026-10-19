

# Generated at 2022-06-13 07:17:36.216766
# Unit test for function jsonify
def test_jsonify():
    result = jsonify(dict(foo=[1, 2, 3], bar=[4, 5, 6]))
    assert result == "{\"bar\": [4, 5, 6], \"foo\": [1, 2, 3]}"
    result = jsonify(dict(foo=[1, 2, 3], bar=[4, 5, 6]), True)
    assert result == "{\n    \"bar\": [\n        4, \n        5, \n        6\n    ], \n    \"foo\": [\n        1, \n        2, \n        3\n    ]\n}"

# Generated at 2022-06-13 07:17:39.789870
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify({"foo": "bar"}, format=True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:17:43.899274
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify

    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify(["a", "b"]) == '["a", "b"]'
    assert jsonify("") == '""'
    assert jsonify(1) == '1'

# Generated at 2022-06-13 07:17:47.070696
# Unit test for function jsonify
def test_jsonify():

    result = {'success': True}
    print(jsonify(result, True))

    result = {'success': u'Ünicode'}
    print(jsonify(result, True))

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:17:53.200147
# Unit test for function jsonify
def test_jsonify():
    result = { 'foo': 'bar', 'baz': 'qux' }

    # Test compact form
    compact_form = '{"baz": "qux", "foo": "bar"}'
    assert jsonify(result) == compact_form

    # Test formatted form
    formatted_form =  '{\n    "baz": "qux", \n    "foo": "bar"\n}'
    assert jsonify(result, True) == formatted_form


# Generated at 2022-06-13 07:17:57.439816
# Unit test for function jsonify
def test_jsonify():
    ''' make sure that our jsonify function works as advertised '''

    assert jsonify({'a':'b'}) == '{"a": "b"}'
    assert jsonify({'a':'b'}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:18:02.670582
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 1, 'b': 2}
    assert(jsonify(result) == '{"a": 1, "b": 2}')

    result = {u'a': u'\u039a'}
    assert(jsonify(result) == '{"a": "\\u039a"}')

    result = {u'a': u'\u039a'}
    assert(jsonify(result, True) == '{\n    "a": "\\u039a"\n}')

# Generated at 2022-06-13 07:18:08.735626
# Unit test for function jsonify
def test_jsonify():

    # Test the basic function of the module
    result = jsonify({'a': 'b', 'c': 'd'})
    assert result == '{"a": "b", "c": "d"}'

    # Test the results with format=True
    result = jsonify({'a': 'b', 'c': 'd'}, format=True)
    assert result == '{\n    "a": "b", \n    "c": "d"\n}'

# Generated at 2022-06-13 07:18:12.423512
# Unit test for function jsonify
def test_jsonify():
    test_result = { "key" : "value" , "key2" : [ "array", "of", "strings" ] }
    assert jsonify(test_result) == '{\"key\": \"value\", \"key2\": [\"array\", \"of\", \"strings\"]}'


# Generated at 2022-06-13 07:18:13.861618
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'content': 'some text'}) == '{"content": "some text"}'



# Generated at 2022-06-13 07:18:30.470924
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == "{}"
    assert jsonify({"a": "b"}) == '{"a": "b"}'
    assert jsonify({"a": ["b", "c"]}) == '{"a": ["b", "c"]}'
    assert jsonify({"a": ["b", "c"]}, True) == '{\n    "a": [\n        "b", \n        "c"\n    ]\n}'
    assert jsonify(["a", "b", "c"]) == '["a", "b", "c"]'
    assert jsonify(["a", "b", "c"], True) == '[\n    "a", \n    "b", \n    "c"\n]'

# Generated at 2022-06-13 07:18:37.928962
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    from ansible.compat.tests import unittest

    def to_text(o):
        if not isinstance(o, str):
            return to_unicode(o)
        return o

    result = {
        'a': 1,
        'b': to_text('text'),
        'c': {
            'd': 2,
            'e': to_text('text 2'),
        },
        'f': ['g', 3],
        'h': to_text('text 3'),
    }

    result = jsonify(result)
    print(result) # just to debug


# Generated at 2022-06-13 07:18:40.947314
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b':2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a': 1, 'b':2}, format=True) == """{
    "a": 1,
    "b": 2
}"""

# Generated at 2022-06-13 07:18:43.566313
# Unit test for function jsonify
def test_jsonify():
    '''Test jsonify function'''
    assert jsonify({"a": "b"}, format=False) == '{"a": "b"}'
    assert jsonify({"a": "b"}, format=True) == '''{
    "a": "b"
}'''

# Generated at 2022-06-13 07:18:45.533617
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify returns JSON string of a Python data structure '''

    assert jsonify(True) == "true"
    assert jsonify({ 'a': 1 }) == '{"a": 1}'
    assert '\n' in jsonify({ 'a': 1 }, format=True)


# Generated at 2022-06-13 07:18:52.095685
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"a":"1","b":"2"}) == '{"a": "1", "b": "2"}'
    assert jsonify({"a":"1","b":"2"}, format=True) == '{\n    "a": "1",\n    "b": "2"\n}'



# Generated at 2022-06-13 07:19:00.000371
# Unit test for function jsonify
def test_jsonify():
    # Adding 2 tests here unittests/test_utils/test_jsonify
    utils.jsonify(1) == str(1)
    utils.jsonify({u'non-ascii':u'f\xf1bar'}) == json.dumps({u'non-ascii':u'f\xf1bar'})
    # jsonify should preserve None return values
    utils.jsonify(None) == json.dumps({})
    # test string formatting
    utils.jsonify(str('foo')) == '"foo"'
    utils.jsonify({'foo':'bar'}) == json.dumps({'foo':'bar'})
    # test unicode formatting
    utils.jsonify(unicode('foo')) == '"foo"'

# Generated at 2022-06-13 07:19:06.225672
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(spam=dict(ham=list(['eggs', 'bacon', 'sausage']),
                                  cheese='stilton'))) == '{"spam": {"ham": ["eggs", "bacon", "sausage"], "cheese": "stilton"}}'

    assert jsonify(dict(spam=dict(ham=list(['eggs', 'bacon', 'sausage']),
                                  cheese='stilton')), True) == '''{
    "spam": {
        "cheese": "stilton",
        "ham": [
            "eggs",
            "bacon",
            "sausage"
        ]
    }
}'''

    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:19:12.547755
# Unit test for function jsonify
def test_jsonify():
    result = {'A': 'a', 'B': 'b'}
    assert(jsonify(result, False) == '{"A": "a", "B": "b"}')
    assert(jsonify(result, True)  == '{\n    "A": "a", \n    "B": "b"\n}')

# Generated at 2022-06-13 07:19:20.373616
# Unit test for function jsonify
def test_jsonify():
    class MyClass(object):
        pass
    assert jsonify(1, True) == "1"
    assert jsonify(True, True) == "true"
    assert jsonify("foo", True) == "\"foo\""
    assert jsonify({"foo": "bar"}, True) == """{
    "foo": "bar"
}"""
    assert jsonify({"foo": ["bar", "baz"]}, True) == """{
    "foo": [
        "bar",
        "baz"
    ]
}"""
    assert jsonify(["bar", "baz"], True) == """[
    "bar",
    "baz"
]"""
    assert jsonify(MyClass, True) == 'null'

# Generated at 2022-06-13 07:19:27.291278
# Unit test for function jsonify
def test_jsonify():
    result = dict(rc=0, stdout='test', changed=False)
    assert jsonify(result, False) == '{"rc": 0, "changed": false, "stdout": "test"}'
    assert jsonify(result, True) == '{\n    "changed": false, \n    "rc": 0, \n    "stdout": "test"\n}'

# Generated at 2022-06-13 07:19:30.731636
# Unit test for function jsonify
def test_jsonify():
    a = None
    assert jsonify(a) == "{}"

    a = {"a": "b" }
    assert jsonify(a) == '{"a": "b"}'

    a = {"a": "b" }
    assert jsonify(a, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:19:34.149498
# Unit test for function jsonify
def test_jsonify():
    result = [1,2,3]
    assert jsonify(result, True) == '[\n    1, \n    2, \n    3\n]'
    assert jsonify(result, False) == '[1, 2, 3]'

# Generated at 2022-06-13 07:19:42.526983
# Unit test for function jsonify
def test_jsonify():

    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook import Playbook

    pb = Playbook.load('/path/to/playbook', cli_variables=dict(foo='bar'), variable_manager=PlaybookCLI().variable_manager)
    assert jsonify(pb, True) == '{\n    "extra_vars": {\n        "foo": "bar"\n    }, \n    "inventory": "path/to/playbook", \n    "playbook": "path/to/playbook"\n}'

# Generated at 2022-06-13 07:19:52.157082
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, True) == '{\n    "a": 1\n}'
    assert jsonify({"b": [1, 2, 3]}, True) == '{\n    "b": [\n        1, \n        2, \n        3\n    ]\n}'
    assert jsonify({"d": {"a": "hello world", "b": [1, 2, 3]}, "c": 3}, True) == '{\n    "c": 3, \n    "d": {\n        "a": "hello world", \n        "b": [\n            1, \n            2, \n            3\n        ]\n    }\n}'


# Generated at 2022-06-13 07:20:01.772634
# Unit test for function jsonify
def test_jsonify():
    ''' test the jsonify function '''
    jsonify_data1 = {'a': 'b'}
    jsonify_data2 = {'a': 'b', 'c': 'd'}

    jsonify_string1 = '{"a": "b"}'
    jsonify_string2 = '{"a": "b", "c": "d"}'

    assert jsonify(jsonify_data1) == jsonify_string1
    assert jsonify(jsonify_data2) == jsonify_string2
    assert jsonify(jsonify_data1, True) == jsonify_string1 + '\n'
    assert jsonify(jsonify_data2, True) == '''{
    "a": "b",
    "c": "d"
}
'''



# Generated at 2022-06-13 07:20:04.160234
# Unit test for function jsonify
def test_jsonify():
    assert '"foo": "bar"' in jsonify({'foo': 'bar'}, format=False)
    assert '"foo": "bar"' in jsonify({'foo': 'bar'}, format=True)



# Generated at 2022-06-13 07:20:12.210890
# Unit test for function jsonify
def test_jsonify():
    assert '{\n    "a": "foo", \n    "b": "bar"\n}' == jsonify({'a': 'foo', 'b': 'bar'}, format=True)
    assert '{"a": "foo", "b": "bar"}' == jsonify({'a': 'foo', 'b': 'bar'}, format=False)
    assert '{"a": "foo", "b": "bar"}' == jsonify({'a': 'foo', 'b': 'bar'})
    assert 'null' == jsonify(None)

# Generated at 2022-06-13 07:20:18.261902
# Unit test for function jsonify
def test_jsonify():
    from nose.tools import assert_true, assert_equals

    assert_equals(jsonify(None), "{}")
    # Make sure that a unicode object within a different object is able to be dumped
    assert_true(isinstance(jsonify({u"foo":"\u7684"}), unicode))
    # Make sure that a unicode object is able to be dumped
    assert_true(isinstance(jsonify(u"\u7684"), unicode))

# Generated at 2022-06-13 07:20:25.598661
# Unit test for function jsonify
def test_jsonify():

    # An empty structure
    assert jsonify(result=None) == '{}'

    data = {}
    data['foo'] = { 'bar': 1, 'bam': ['a', 'b'] }

    # python nested structure
    assert eval(jsonify(result=data)) == data

    # formatted
    assert jsonify(result=data, format=True) == '''{
    "foo": {
        "bar": 1,
        "bam": [
            "a",
            "b"
        ]
    }
}'''

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:20:41.605638
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.jsonify import jsonify
    result1 = {'a': 1, 'b': 2}
    result2 = {u'a': 1, u'b': 2}
    assert jsonify(result1) == '{"a": 1, "b": 2}'
    assert jsonify(result2) == '{"a": 1, "b": 2}'
    assert jsonify(result2, format=True) == '{\n    "a": 1,\n    "b": 2\n}'
    assert jsonify(None) == '{}'
    thedict = {"a": 1, "b": 2, "c": {"d": 3}}
    assert jsonify(thedict) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:20:45.828345
# Unit test for function jsonify
def test_jsonify():
    assert(type(jsonify(None)) == str)
    assert(jsonify(None) == '{}')
    assert(jsonify({"a": "b"}) == '{"a": "b"}')



# Generated at 2022-06-13 07:20:54.430896
# Unit test for function jsonify
def test_jsonify():
    import json
    test_dict = {'test':'string', 'test2':123, 'test3':{'test':'string'}}
    json_str = '{"test3": {"test": "string"}, "test": "string", "test2": 123}'
    json_dict = json.loads(json_str)
    assert(jsonify(test_dict) == json_str)
    assert(jsonify(test_dict, True) == json.dumps(json_dict, sort_keys=True, indent=4))
    assert(jsonify(test_dict, False) == json_str)

# Compatibility with 2.6 where json.dumps does not accept ensure_ascii param

# Generated at 2022-06-13 07:20:56.085380
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'test': 1}) == '{"test": 1}'

# Generated at 2022-06-13 07:21:08.457287
# Unit test for function jsonify
def test_jsonify():
    ''' test_jsonify '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    try:
        import __builtin__
        json = __builtin__.__dict__['json']
    except:
        import json


# Generated at 2022-06-13 07:21:14.816007
# Unit test for function jsonify
def test_jsonify():

    # test to make sure that jsonify can at least run on the data
    # structures that are returned from Runner() and PlayBook() runs
    # (which is a list or a dict)
    #
    # this used to have more tests, but they have moved to the files
    # in test/units/callbacks/test_json.py as they are specific to
    # the json callback

    assert isinstance(jsonify([{'foo':'bar'}]), (str, unicode))
    assert isinstance(jsonify({'foo':'bar'}), (str, unicode))

# Generated at 2022-06-13 07:21:21.465193
# Unit test for function jsonify
def test_jsonify():
    result = {
        "key1": "value",
        "key2": ["value1", "value2"],
        "key3": {
            "key31": "value1",
            "key32": "value2"
        }
    }
    result_json = jsonify(result)
    assert result_json == "{\"key1\": \"value\", \"key2\": [\"value1\", \"value2\"], \"key3\": {\"key32\": \"value2\", \"key31\": \"value1\"}}"

# Generated at 2022-06-13 07:21:31.267807
# Unit test for function jsonify
def test_jsonify():

    from ansible.cli import CLI

    cli = CLI()

    test_results = [
        None,
        [['a', 'b', 'c']],
        {'a': 1, 'b': 2, 'c': 3},
        {'a': [1,2,3]},
    ]

    # Should generate the same output, regardless of formatting option
    for result in test_results:
        uncompressed = jsonify(result, format=False)
        compressed = jsonify(result, format=True)
        assert(uncompressed == compressed)

# Generated at 2022-06-13 07:21:35.682140
# Unit test for function jsonify
def test_jsonify():
    test_list = ['test', {'test': 'data'}]
    test_string = jsonify(test_list, True)
    assert test_string == '''[
    "test", 
    {
        "test": "data"
    }
]'''

# Generated at 2022-06-13 07:21:38.677247
# Unit test for function jsonify
def test_jsonify():
    results = jsonify({"a": 1})
    assert '{\n"a": 1\n}' == results
    assert '{"a": 1}' == jsonify({"a": 1}, format=False)
    assert isinstance(results, str)

# Generated at 2022-06-13 07:21:49.626003
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(dict(changed=False)) == '{"changed": false}'

# Generated at 2022-06-13 07:21:55.496715
# Unit test for function jsonify
def test_jsonify():
    '''
    Basic unit tests for the jsonify() function
    '''

    # Test a valid and formatted JSON
    assert jsonify({"test": "value"}, True) == '{\n    "test": "value"\n}'

    # Test a valid and formatted JSON (with custom indent)
    assert jsonify({"test": "value"}, 4) == '{\n    "test": "value"\n}'

    # Test a valid and not formatted JSON
    assert jsonify({"test": "value"}) == '{"test":"value"}'

# Generated at 2022-06-13 07:22:06.819277
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('a') == '"a"'
    assert jsonify(2) == '2'
    assert jsonify(None) == '{}'
    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'
    assert jsonify('Apples and Oranges') == '"Apples and Oranges"'
    assert jsonify(dict(a=1, b=2), format=True) == '{\n    "a": 1, \n    "b": 2\n}'

# ignore the following test if _ansible_version is not defined, it is part of ansible-base
_ansible_version = getattr(__builtins__, '_ansible_version', None)

# Generated at 2022-06-13 07:22:12.403023
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify({'a': 'b'}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:22:22.506393
# Unit test for function jsonify
def test_jsonify():
    # Test valid JSON
    test1 = dict(foo='bar')
    assert jsonify(test1) == '{"foo": "bar"}'
    assert jsonify(test1, format=True) == '{\n    "foo": "bar"\n}'

    # Test invalid character handled
    test2 = dict(foo=u'\xA4')
    assert jsonify(test2) == '{"foo": "?"}'
    assert jsonify(test2, format=True) == '{\n    "foo": "?"\n}'

# Generated at 2022-06-13 07:22:27.283951
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({"a":"b"}) == '{"a": "b"}'
    assert jsonify({"a":"b"}, format=False) == '{"a": "b"}'
    assert jsonify({"a":"b"}, format=True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:22:33.073939
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''
    assert jsonify('{"a": 1}') == '{"a": 1}'
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'

# Generated at 2022-06-13 07:22:38.992977
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''
    test1 = { "foo": "bar" }
    assert jsonify(test1) == '{\"foo\": \"bar\"}'
    assert jsonify(test1, format=True) == '{\n    \"foo\": \"bar\"\n}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:22:40.868833
# Unit test for function jsonify
def test_jsonify():
    r = jsonify({'a':'a'}, True)
    assert r.startswith("{\n  ")


# Generated at 2022-06-13 07:22:50.889643
# Unit test for function jsonify
def test_jsonify():
    from ansible.compat.tests import unittest
    from ansible.utils.jsonify import jsonify

    class TestJsonify(unittest.TestCase):

        def test_jsonify_dict(self):
            result = {'a': 'b'}
            expected = '{"a": "b"}'
            self.assertEqual(jsonify(result), expected)

        def test_jsonify_dict_format(self):
            result = {'a': 'b'}
            expected = '{\n    "a": "b"\n}\n'
            self.assertEqual(jsonify(result, format=True), expected)

        def test_jsonify_none(self):
            result = None
            expected = "{}"
            self.assertEqual(jsonify(result), expected)

    unittest

# Generated at 2022-06-13 07:23:05.628327
# Unit test for function jsonify
def test_jsonify():
    assert "{}" == jsonify(None, False)
    assert "{}" == jsonify(None, True)

# Load modules in ./library so they can be tested easily
from ansible.module_utils import basic
from ansible.module_utils import templates
from ansible.module_utils.facts import *

# add leap seconds for testing
basic.TZ_OFFSETS.setdefault('LEAP', (0, 0, 0, 1, 0, 0))

# Generated at 2022-06-13 07:23:08.625797
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a': 1, 'b': 2}, format=True) == '''{
    "a": 1,
    "b": 2
}'''

# Generated at 2022-06-13 07:23:17.494285
# Unit test for function jsonify
def test_jsonify():

    # Test empty or no input
    assert jsonify() == jsonify(None) == "{}"

    # Test empty JSON object
    assert jsonify({}) == "{}"

    # Test JSON object with only one key
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'

    # Test JSON object with multiple keys
    assert jsonify({"foo": "bar", "bar": "foo"}) == '{"bar": "foo", "foo": "bar"}'

    # Test JSON object with unicode
    assert jsonify({"foo": u"bar"}) == '{"foo": "bar"}'

    # Test JSON object with unicode
    assert jsonify({"foo": u"bar", "bar": u"foo"}) == '{"bar": "foo", "foo": "bar"}'

    # Test string concatenation

# Generated at 2022-06-13 07:23:26.923363
# Unit test for function jsonify
def test_jsonify():
    # test for string
    result = {'1': 'foo', '2': 'bar', '3': 'baz'}
    assert jsonify(result, format=False) == '{"1": "foo", "2": "bar", "3": "baz"}'
    assert jsonify(result, format=True) == '''{
    "1": "foo",
    "2": "bar",
    "3": "baz"
}
'''
    # test for list
    result = ['foo', 'bar', 'baz']
    assert jsonify(result, format=False) == '["foo", "bar", "baz"]'
    assert jsonify(result, format=True) == '''[
    "foo",
    "bar",
    "baz"
]
'''

    # test for True


# Generated at 2022-06-13 07:23:36.907796
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('foo') == '"foo"'
    assert jsonify(42) == '42'
    assert jsonify(True) == 'true'
    assert jsonify(False) == 'false'
    assert jsonify(None) == 'null'
    assert jsonify([]) == '[]'
    assert jsonify({}) == '{}'
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify({'a': 'b'}, format=True) == '{\n    "a": "b"\n}'
    assert jsonify({'n': None}) == '{"n": null}'
    assert jsonify({'n': None}, format=True) == '{\n    "n": null\n}'

# Generated at 2022-06-13 07:23:42.255214
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should always return JSON string or empty JSON object for None '''

    assert jsonify(None) == "{}"
    assert jsonify(1) == "1"
    assert jsonify({}) == "{}"
    assert jsonify([]) == "[]"
    assert jsonify("foo") == "\"foo\""
    # ensure_ascii=False ensures that we get JSON with Unicode characters intact
    assert jsonify("é") == "\"é\""
    assert jsonify("\u2014") == "\"\u2014\""

    assert jsonify({1: 2, 3: 4}, format=True) == "{\n    \"1\": 2, \n    \"3\": 4\n}"

# Generated at 2022-06-13 07:23:47.498482
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'test': 1}) == '{\"test\": 1}'
    assert jsonify({'test': 1}, True) == '{\n    \"test\": 1\n}'
    assert jsonify({'test': 1, 'test2': 'test'}, True) == '{\n    \"test\": 1, \n    \"test2\": \"test\"\n}'
    assert jsonify(None) == '{}'
    assert jsonify('test') == '\"test\"'

# Generated at 2022-06-13 07:23:57.965903
# Unit test for function jsonify
def test_jsonify():
    result = {'key': 'value'}
    assert jsonify(result) == '{"key": "value"}'
    assert jsonify(result, format=True) == '{\n    "key": "value"\n}'

# this is the standard ansible magic variable to hold onto results
# from a task execution.  It should always be named 'ansible_facts'
# so it can be auto-loaded by /usr/bin/ansible, but it can be
# overridden per task.

# next is a list of hosts taken from the inventory, which is also
# used by /usr/bin/ansible for the --list-hosts option.

# the last item is a special item where a module developer can include
# additional facts, which will be included in the 'setup' module output.


# Generated at 2022-06-13 07:24:03.422235
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':1, 'b':2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a':1, 'b':2}, format=True) == """{
    "a": 1,
    "b": 2
}"""
    assert jsonify(None, format=True) == '{}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:24:09.912682
# Unit test for function jsonify
def test_jsonify():
    # Test empty dict
    obj = {}
    assert jsonify(obj) == '{}', "Return value is not empty bracket"

    # Test simple dict
    obj = {'a':'b'}
    assert jsonify(obj) == '{"a": "b"}', "Return value does not match"

    # Test empty list
    obj = []
    assert jsonify(obj) == '[]', "Return value does not match"

    # Test simple list
    obj = ['a']
    assert jsonify(obj) == '["a"]', "Return value does not match"

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:24:28.025138
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"key": "value"}) == '{"key": "value"}'
    assert jsonify({"key": "value"}, format=True) == '{\n    "key": "value"\n}'
    assert jsonify({"key": "value\u2019"}) == '{"key": "value\u2019"}'
    assert jsonify({"key": "value\u2019"}, format=True) == '{\n    "key": "value\u2019"\n}'

# Generated at 2022-06-13 07:24:33.681603
# Unit test for function jsonify
def test_jsonify():
    # With non-empty string
    result = jsonify("foo")
    assert(result == '"foo"')

    # With empty string
    result = jsonify("")
    assert(result == '""')

    # With None
    result = jsonify(None)
    assert(result == '{}')

    # With None
    result = jsonify({'foo': 1})
    assert(result == '{"foo": 1}')

# Generated at 2022-06-13 07:24:37.485737
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify([1,2,3]) == "[1, 2, 3]"
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a': 1, 'b': 2}, True) == '''{\n    "a": 1, \n    "b": 2\n}'''

# Generated at 2022-06-13 07:24:42.422412
# Unit test for function jsonify
def test_jsonify():
    import os

    # no result
    result = jsonify(None)
    assert result == "{}"

    # format JSON
    result = jsonify({'foo': 'bar'}, True)
    assert result == "{\n    \"foo\": \"bar\"\n}"

    # unformat JSON
    result = jsonify({'foo': 'bar'})
    assert result == '{"foo": "bar"}'

    # non-ASCII character in string
    result = jsonify({'foo': "bar\xe4"})
    assert result == "{u'foo': u'bar\u00e4'}"

    # non-ASCII character in key
    result = jsonify({'f\xe4': 'bar'})
    assert result == "{u'f\u00e4': 'bar'}"

    # non-ASCII character in key

# Generated at 2022-06-13 07:24:51.650707
# Unit test for function jsonify
def test_jsonify():
    result = dict(
         ansible_facts=dict(distribution='RedHat', version='6.5'),
         ansible_module_name='mymodule',
         changed=False,
         invocation=dict(module_args=dict(arg1='val1',arg2='val2')),
    )
    expected = """{
    "ansible_facts": {
        "distribution": "RedHat",
        "version": "6.5"
    },
    "ansible_module_name": "mymodule",
    "changed": false,
    "invocation": {
        "module_args": {
            "arg1": "val1",
            "arg2": "val2"
        }
    }
}"""

    assert expected == jsonify(result, format=True)


# Generated at 2022-06-13 07:24:58.063291
# Unit test for function jsonify
def test_jsonify():
    # Test with empty data
    data = "{}"
    assert jsonify(None) == data

    # Test with a simple python object
    data = '{"simple": "object"}'
    assert jsonify({"simple": "object"}) == data

    # Test with a complex python object
    data = '{"a": 1, "b": 2}'
    assert jsonify({"a": 1, "b": 2}) == data

# Generated at 2022-06-13 07:25:00.926408
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic

    assert jsonify(basic.AnsibleModule(
        argument_spec={},
    ).exit_json(changed=True, foo='bar')) == '{"changed": true, "foo": "bar"}'

# Generated at 2022-06-13 07:25:03.707299
# Unit test for function jsonify
def test_jsonify():
    # Test None input
    assert(jsonify(None) == "{}")

    # Test non-dictionary
    assert(jsonify('foo') == "\"foo\"")

    # Test dictionary with one key
    assert(jsonify({'foo': 'bar'}) == "{\"foo\": \"bar\"}")

# Generated at 2022-06-13 07:25:08.698202
# Unit test for function jsonify
def test_jsonify():
    import __main__
    __main__.jsonify = jsonify
    from ansible.module_utils.basic import *
    if sys.version_info >= (2, 6):
        assert jsonify({'foo': 'bar'}) == u'{"foo": "bar"}'
    else:
        assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify(dict(foo='bar', bar='baz')) == '{"bar": "baz", "foo": "bar"}'
    assert jsonify(dict(foo=dict(bar='baz'))) == '{"foo": {"bar": "baz"}}'
    assert jsonify(dict(foo=['bar', 'baz'])) == '{"foo": ["bar", "baz"]}'

# Generated at 2022-06-13 07:25:16.827407
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify
    from ansible import constants as C

    # Set ansible.cfg to use 'json' as the stdout_callback
    import ansible.constants as C
    import ansible.callbacks
    C.config.DEFAULT_STDOUT_CALLBACK = "json"
    C.config.STDOUT_CALLBACK = ansible.callbacks.__name__

    # Set up results to jsonify
    result_success = {
        "contacted": {
            "foo.example.com": {
                "invocation": {
                    "module_args": "",
                },
                "changed": False,
                "ping": "pong",
            }
        },
        "dark": {
        }
    }


# Generated at 2022-06-13 07:25:51.131329
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.compat.six import text_type

    testdict = dict(a=1, b="abc", c=dict(d=5, e="{{inventory_hostname}}"),
                    f=["a","b",text_type("c")],
                    g=AnsibleUnsafeText(u"\u2018"))

    assert(jsonify(testdict, format=False) == "{\"a\": 1, \"c\": {\"e\": \"{{inventory_hostname}}\", \"d\": 5}, \"b\": \"abc\", \"f\": [\"a\", \"b\", \"c\"], \"g\": \"\\u2018\"}")

# Generated at 2022-06-13 07:25:58.425284
# Unit test for function jsonify
def test_jsonify():
    assert u'{"changed": false, "failed": false, "ping": "pong"}' == jsonify(dict(failed=False, ping='pong', changed=False))
    assert u'{"changed": false, "failed": false, "ping": "pong"}' == jsonify(dict(failed=False, ping=u'pong', changed=False))
    assert u"{}" == jsonify(None)
    assert u'{"changed": false, "failures": 0, "ok": 1, "ping": ["pong"]}' == jsonify(dict(ping=["pong"], ok=1, failures=0, changed=False))

# Generated at 2022-06-13 07:26:02.277315
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("Hello World") == '"Hello World"'
    assert jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:26:12.271178
# Unit test for function jsonify
def test_jsonify():
    # test for function jsonify with defaul parameter "format"
    assert jsonify({"a": "b"}) == '{"a": "b"}', 'test_jsonify1 failed'
    # test for function jsonify with parameter "format" = True
    assert jsonify({'c': 'd'}, True) == "{\n    \"c\": \"d\"\n}", 'test_jsonify2 failed'
    # test for function jsonify with "result" = None
    assert jsonify(None) == "{}", 'test_jsonify3 failed'
    # test for function jsonify with ascii
    assert jsonify({u'a': u'b'}) == '{"a": "b"}', 'test_jsonify4 failed'


# Generated at 2022-06-13 07:26:15.771744
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"a":1,"b":2}) == '{"a": 1, "b": 2}'
    assert jsonify(dict(a=1,b=2)) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:26:26.529259
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO

    data = {
        'changed': True,
        'failed': False,
        'invocation': {
            'module_args': {
                'a': 'b',
                'c': 'd'
            },
        },
        'state': 'present'
    }
    stdout = StringIO()
    basic._ANSIBLE_ARGS = None
    basic.jsonify(data, stdout)

# Generated at 2022-06-13 07:26:35.580755
# Unit test for function jsonify
def test_jsonify():
    ''' make sure function behaves as expected '''

    assert jsonify('foo') == '"foo"'
    assert jsonify('foo', format=True) == '"foo"'
    assert jsonify(['foo', 'bar']) == '["foo", "bar"]'
    assert jsonify(['foo', 'bar'], format=True) == '["foo", "bar"]'
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, format=True) == '''{
    "foo": "bar"
}'''
    assert jsonify({'foo': 'bar', 'a': 'b'}, format=True) == '''{
    "a": "b",
    "foo": "bar"
}'''

# Generated at 2022-06-13 07:26:40.356779
# Unit test for function jsonify
def test_jsonify():
    json_string = jsonify({'ping': 'pong'})
    assert json_string == "{\"ping\": \"pong\"}"

    json_string = jsonify({'ping': 'pong'}, True)
    assert json_string == "{\n    \"ping\": \"pong\"\n}"


# Generated at 2022-06-13 07:26:47.231639
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 2}) == '{"a": 2}'
    assert jsonify({"a": 2}, format=True) == '{\n    "a": 2\n}'
    assert jsonify(None) == '{}'
    assert jsonify(None, format=True) == '{}'
    assert jsonify({'example': '\xe3'}) == '{"example": "\\u00e3"}'

# Generated at 2022-06-13 07:26:59.146124
# Unit test for function jsonify
def test_jsonify():
    result = jsonify(None)
    assert result == "{}"

    result = jsonify(None, format=True)
    assert result == "{\n    \n}"

    result = jsonify({'foo': [1, 2, 3], 'bar': {'baz': 'qux'}})
    assert result == "{\"bar\": {\"baz\": \"qux\"}, \"foo\": [1, 2, 3]}"

    result = jsonify({'foo': [1, 2, 3], 'bar': {'baz': 'qux'}}, format=True)

# Generated at 2022-06-13 07:27:27.774665
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':'A', 'b':'B'}) == '{"a": "A", "b": "B"}'
    assert jsonify({'a':'A', 'b':'B'}, format=True) == '{\n    "a": "A",\n    "b": "B"\n}'