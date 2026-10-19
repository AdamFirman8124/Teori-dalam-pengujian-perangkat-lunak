

# Generated at 2022-06-13 07:17:38.397260
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify(None, True) == '{}'

    assert jsonify({}) == '{}'
    assert jsonify({}, True) == '{}'

    assert jsonify({ 'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({ 'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'

    assert jsonify({ 'foo': { 'bar': 'baz' }}) == '{"foo": {"bar": "baz"}}'
    assert jsonify({ 'foo': { 'bar': 'baz' }}, True) == '{\n    "foo": {\n        "bar": "baz"\n    }\n}'


# Generated at 2022-06-13 07:17:39.985326
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'a':1}) == '{"a": 1}'

# Generated at 2022-06-13 07:17:44.479342
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar', 'baz': 'qux'}) == '{"baz": "qux", "foo": "bar"}'
    assert jsonify({'foo': 'bar', 'baz': 'qux'}, True) == '{\n    "baz": "qux", \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:17:47.790412
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify(None) == '{}'
    assert jsonify(dict(foo='bar')) == '{"foo": "bar"}'
    assert jsonify(dict(foo='bar'), format=True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:17:54.744680
# Unit test for function jsonify
def test_jsonify():
    result = { "abcd" : 1, "bcde" : 2 }

    rval = jsonify(result, True)
    assert isinstance(rval, str)

    result2 = json.loads(rval)
    assert isinstance(result2, dict)
    assert result2 == result

    rval = jsonify(None, True)
    assert isinstance(rval, str)

    result2 = json.loads(rval)
    assert isinstance(result2, dict)
    assert result2 == {}



# Generated at 2022-06-13 07:18:03.707116
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify([]) == '[]'
    assert jsonify(dict(foo=1,bar=2)) == '{"bar": 2, "foo": 1}'
    assert jsonify(dict(foo=1,bar=2),True) == '{\n    "bar": 2, \n    "foo": 1\n}'
    assert jsonify(dict(foo=dict(bar="baz"),bar=2)) == '{"bar": 2, "foo": {"bar": "baz"}}'
    assert jsonify(dict(foo=dict(bar="baz"),bar=2),True) == '{\n    "bar": 2, \n    "foo": {\n        "bar": "baz"\n    }\n}'

# Generated at 2022-06-13 07:18:11.936712
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 'bar', 'bam': [1,2,3], 'boo': {'moo': 'cow'}}
    assert jsonify(result) == "{\"bam\": [1, 2, 3], \"boo\": {\"moo\": \"cow\"}, \"foo\": \"bar\"}"
    assert jsonify(result, True) == "{\n    \"bam\": [\n        1, \n        2, \n        3\n    ], \n    \"boo\": {\n        \"moo\": \"cow\"\n    }, \n    \"foo\": \"bar\"\n}"



# Generated at 2022-06-13 07:18:17.877242
# Unit test for function jsonify
def test_jsonify():
    # no error since result = None
    # This test fails with Ansible 1.4.4 and earlier
    assert jsonify(None) == "{}"

    # no error since indent = None
    assert jsonify({'a': 1, 'b': 2}, False) == '{"a": 1, "b": 2}'

    # return ASCII-only JSON
    assert jsonify({'a': 1, 'b': 2}, True) == '{\n    "a": 1, \n    "b": 2\n}'

    # error since result is a string
    try:
        jsonify('wrong type')
        assert False, "This should raise a TypeError"
    except TypeError as e:
        assert 'is not JSON serializable' in str(e), "e = %s" % e

    # error since result contains unicode
    result

# Generated at 2022-06-13 07:18:31.153786
# Unit test for function jsonify
def test_jsonify():
    result_to_test1 = { 'a': 'something' }
    result_to_test2 = { 'a': 'something', 'b': 'something else'}
    result_to_test3 = None
    expected1 = '{\n    "a": "something"\n}'
    expected2 = '{\n    "a": "something", \n    "b": "something else"\n}'
    expected3 = '{}'

    assert jsonify(result_to_test1, True) == expected1, "jsonify function failed"
    assert jsonify(result_to_test2, True) == expected2, "jsonify function failed"
    assert jsonify(result_to_test3) == expected3, "jsonify function failed"


# Generated at 2022-06-13 07:18:34.441674
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert jsonify({"a": 1, "b": 2}, format=True) in ('{\n    "a": 1,\n    "b": 2\n}', '{\n    "b": 2,\n    "a": 1\n}')

# Generated at 2022-06-13 07:18:39.418607
# Unit test for function jsonify
def test_jsonify():
    # Simply test for valid JSON to indicate if anything is wrong with the method itself
    # No need to go crazy here.
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:18:45.261268
# Unit test for function jsonify
def test_jsonify():
    # Test simple dictionary
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    # Test nested dictionary
    assert jsonify({"foo": {"foo": "bar"}}) == '{"foo": {"foo": "bar"}}'
    # Test simple list
    assert jsonify(["foo", "bar"]) == '["foo", "bar"]'
    # Test nested list
    assert jsonify([["foo", "bar"], ["foo", "bar"]]) == '[[\n    "foo", \n    "bar"\n], [\n    "foo", \n    "bar"\n]]'
    # Test simple string
    assert jsonify("foobar") == '"foobar"'

# Generated at 2022-06-13 07:18:56.753316
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils import jsonify
    from ansible.utils.unicode import to_unicode

    junk = u"foo"
    assert(jsonify(junk)) == '"foo"'

    junk = to_unicode(junk)
    assert(jsonify(junk)) == '"foo"'

    junk = { "foo": "bar", "biz": "baz" }
    assert(jsonify(junk)) == '{"biz": "baz", "foo": "bar"}'

    junk = { u"foo": u"bar", u"biz": u"baz" }
    assert(jsonify(junk)) == '{"biz": "baz", "foo": "bar"}'

    junk = [ 1, 2, 3 ]
    assert(jsonify(junk)) == '[1, 2, 3]'

   

# Generated at 2022-06-13 07:19:06.772675
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.jsonify import jsonify
    my_dict = dict(foo='bar', bam='boozle')
    my_list = ['foo', 'bar', my_dict]
    my_dict['list'] = my_list

# Generated at 2022-06-13 07:19:11.539360
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a': 'b'}, True) == '{\n    "a": "b"\n}'
    assert jsonify(['c'], False) == '["c"]'

# Generated at 2022-06-13 07:19:19.240343
# Unit test for function jsonify
def test_jsonify():
    print("testing jsonify")
    print("should have no indent and be a single line")
    print("%s" % jsonify({'foo': 'bar'}))
    print("should now have indent and be on new lines")
    print("%s" % jsonify({'foo': 'bar'}, True))

# Run unit tests when this module is run directly
if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:19:23.006168
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify(dict(a=1,b=2)) == '{"a": 1, "b": 2}'
    assert jsonify(dict(a=1,b=2), format=True)

# Generated at 2022-06-13 07:19:31.365540
# Unit test for function jsonify
def test_jsonify():
    output = jsonify(dict(a=1, b=2), format=True)
    assert output == '{\n    "a": 1, \n    "b": 2\n}'
    output = jsonify(dict(a=1, b=2), format=False)
    assert output == '{"a": 1, "b": 2}'
    output = jsonify(dict(a=1, b=2, c=dict(d=3)), format=True)
    assert output == '{\n    "a": 1, \n    "b": 2, \n    "c": {\n        "d": 3\n    }\n}'
    output = jsonify(dict(a=1, b=2, c=dict(d=3)), format=False)

# Generated at 2022-06-13 07:19:38.768648
# Unit test for function jsonify
def test_jsonify():
    test_result = {'test_result': 'test_jsonify'}
    test_json = '{"test_result": "test_jsonify"}'

    # Test JSON
    assert jsonify(test_result) == test_json

    # Test JSON with format
    assert jsonify(test_result, format=True) == '{\n    "test_result": "test_jsonify"\n}'

    # Test JSON with None
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:19:41.590210
# Unit test for function jsonify
def test_jsonify():
    ''' test_jsonify

    Basic test to ensure that jsonify returns a json object
    '''

    assert isinstance(jsonify({'a':'b'}), str)

# Generated at 2022-06-13 07:19:44.873668
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:50.429619
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify("") == "\"\""
    assert jsonify("a") == "\"a\""
    assert jsonify({"a": "b"}) == "{\"a\": \"b\"}"
    assert jsonify("a", format=True) == "\"a\""
    assert jsonify({"a": "b"}, format=True) == "{\n    \"a\": \"b\"\n}"

# Generated at 2022-06-13 07:20:01.292304
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''
    from ansible.utils import jsonify

    assert jsonify('{"foo": "bar"}') == '"{\\"foo\\": \\"bar\\"}"'
    assert jsonify({'foo': 'bar'}) == '"{\\"foo\\": \\"bar\\"}"'
    assert jsonify([1,2,3]) == '"[1, 2, 3]"'
    assert jsonify(3) == '3'
    assert jsonify([1,{'foo':'bar'},3]) == '"[1, {\\"foo\\": \\"bar\\"}, 3]"'
    assert jsonify({'foo':'bar','bar':'baz'}, format=True) == '{\n    "bar": "baz", \n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:20:04.617696
# Unit test for function jsonify
def test_jsonify():
    assert '{"a": "b"}' == jsonify(dict(a='b'))
    #from ansible.utils import module_docs
    #docs = module_docs.get_docstring('user', 'junos')
    #assert docs is not None
    #assert 'failsafe' in docs

# Generated at 2022-06-13 07:20:10.586197
# Unit test for function jsonify
def test_jsonify():

    # Tests if None is correclty returned as {}
    result = None
    assert jsonify(result) == "{}"

    # Tests if list is correctly returned as JSON
    result = [1,2,3]
    #assert jsonify(result) == '[1, 2, 3]'

    # Tests if boolean is correctly returned as JSON
    result = True
    assert jsonify(result) == 'true'
    result = False
    assert jsonify(result) == 'false'

    # Tests if integer is correctly returned as JSON
    result = 123
    assert jsonify(result) == '123'

    # Tests if string is correctly returned as JSON
    result = "test"
    assert jsonify(result) == '"test"'

    # Tests if unicode string is correctly returned as JSON

# Generated at 2022-06-13 07:20:21.473893
# Unit test for function jsonify
def test_jsonify():

    class MyClass:
        ''' dummy class.  Note that this is not a documented feature of the json module. '''
        def __init__(self,value):
            self.value = value
        def __json__(self):
            return self.value

    assert jsonify( {"a": "b"}, format=False ) == '{"a": "b"}'
    assert jsonify( {"a": "b"}, format=True )  == '{\n    "a": "b"\n}'
    assert jsonify( [{"a": "b", "c": "d"}], format=False ) == '[{"a": "b", "c": "d"}]'

# Generated at 2022-06-13 07:20:32.271255
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({'a': 'b'}) == '{}'
    assert jsonify({'a': 'b'}, format=True) == '{}'
    assert jsonify({'a': 'b'}, format=False) == '{}'
    assert jsonify({'a': 'b'}) == "{}"
    assert jsonify({'a': 'b'}, format=True) == "{\n    \"a\": \"b\"\n}"
    assert jsonify({'a': 'b'}, format=False) == "{\"a\": \"b\"}"
    assert jsonify({'a': 'b'}, format=False) == '{"a": "b"}'
    assert jsonify({'a': 'b'}) == '{}'

# Generated at 2022-06-13 07:20:40.619056
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify(None, True) == '{}'
    assert jsonify({}) == '{}'
    assert jsonify(dict(changed=True)) == '{"changed": true}'
    assert jsonify(dict(changed=True), True) == '{\n    "changed": true\n}'
    assert jsonify(dict(changed=True, results=['ok', 'skipped'])) == '{"changed": true, "results": ["ok", "skipped"]}'
    assert jsonify(dict(changed=True, results=['ok', 'skipped']), True) == '{\n    "changed": true, \n    "results": [\n        "ok", \n        "skipped"\n    ]\n}'

# print_function
# unicode

# Generated at 2022-06-13 07:20:49.532858
# Unit test for function jsonify
def test_jsonify():

    # If result is None, it should return '{}'
    assert jsonify(None) == "{}"

    # Otherwise, it should return the json-ified version of the input
    assert jsonify(["foo", "bar", "baz"]) == '["foo", "bar", "baz"]'

    # The 'format' option should ensure indentation
    assert jsonify(["foo", "bar", "baz"], format=True) == '[\n    "foo", \n    "bar", \n    "baz"\n]'

    # The function should handle unicode
    assert jsonify(["foo", u"bar", "baz"]) == '["foo", "bar", "baz"]'
    
    # A dict with unicode values should also work

# Generated at 2022-06-13 07:21:00.208125
# Unit test for function jsonify
def test_jsonify():

    # result is None
    result = None
    assert jsonify(result) == "{}"

    # format is False
    result = dict(foo=1, bar=2)
    assert jsonify(result) == "{\"bar\": 2, \"foo\": 1}"

    # format is True
    result = dict(foo=1, bar=2)
    assert jsonify(result, format=True) == "{\n    \"bar\": 2, \n    \"foo\": 1\n}"

# How to run unit test:
# python -c 'from module_utils.common import jsonify; test_jsonify()'

# Generated at 2022-06-13 07:21:10.954007
# Unit test for function jsonify
def test_jsonify():
    data = {
        "foo": "bar",
        "spam": [ "ham", "eggs" ],
        "unicode": "föö",
        "int": 1,
        "float": 1.1,
        "bool": False,
        "dict": { "a": "b" },
        "list_of_dicts": [ { "x": "y" } ],
    }
    assert jsonify(data) == json.dumps(data, sort_keys=True, indent=None)
    assert jsonify(data, True) == json.dumps(data, sort_keys=True, indent=4)

# Generated at 2022-06-13 07:21:17.869537
# Unit test for function jsonify
def test_jsonify():
    result1 = jsonify(dict(foo='Hello', bar='World'))
    assert result1 == '{"bar": "World", "foo": "Hello"}'
    result2 = jsonify(dict(foo='Hello', bar='World'), format=True)
    assert result2 == '''{
    "bar": "World",
    "foo": "Hello"
}'''


# Generated at 2022-06-13 07:21:21.286838
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify({'foo': 'bar'}) == '{"foo": "bar"}')
    assert(jsonify({'foo': 'bar'}, format=True) == '{\n    "foo": "bar"\n}')
    assert(jsonify(None) == '{}')
    assert(jsonify({}) == '{}')
    assert(jsonify([1, 2, 3]) == '[1, 2, 3]')
    assert(jsonify({'foo': 'bar'}, format=False) == '{"foo": "bar"}')



# Generated at 2022-06-13 07:21:22.608814
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:21:37.017403
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None, format=False)                                  == "{}"
    assert jsonify({}, format=False)                                    == "{}"
    assert jsonify([], format=False)                                    == "[]"
    assert jsonify({"a": 1, "b": 2}, format=False)                      == '{"a": 1, "b": 2}'
    assert jsonify({'a': 'a', 'b': 'b'}, format=False)                  == '{"a": "a", "b": "b"}'
    assert jsonify({"a": 1, "b": [1, 2, 3]}, format=False)              == '{"a": 1, "b": [1, 2, 3]}'

# Generated at 2022-06-13 07:21:44.379677
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes
    struct1 = dict(a=1, b="2")
    struct2 = dict(a=1, b=to_bytes("2"))
    struct3 = dict(a=1, b=2, c=struct1)
    struct4 = dict(a=1, b=2, c=[struct1, struct2, struct3])
    assert "{\"a\": 1, \"b\": \"2\"}" == jsonify(struct1)
    assert "{\"a\": 1, \"b\": \"2\"}" == jsonify(struct2)
    assert "{\"a\": 1, \"b\": 2, \"c\": {\"a\": 1, \"b\": \"2\"}}" == jsonify(struct3)

# Generated at 2022-06-13 07:21:50.464890
# Unit test for function jsonify
def test_jsonify():
    data = {
        'foo': True,
        'bar': 42,
        'baz': None
    }

    result = jsonify(data)
    expected = '{"bar": 42, "baz": null, "foo": true}'

    assert result == expected

    result = jsonify(data, True)
    expected = '''{
    "bar": 42,
    "baz": null,
    "foo": true
}'''

    assert result == expected

# Generated at 2022-06-13 07:21:58.009444
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_bytes

    json_data = {
        'str': 'foo',
        'int': 42,
        'list': ['foo', 'bar'],
        'dict': {'foo': 'bar'}
    }

    compact = to_bytes(jsonify(json_data))
    assert compact == to_bytes(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

    pretty = to_bytes(jsonify(json_data, format=True))
    assert pretty == b"""{
    "dict": {
        "foo": "bar"
    },
    "int": 42,
    "list": [
        "foo",
        "bar"
    ],
    "str": "foo"
}"""

# Generated at 2022-06-13 07:22:06.103777
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(changed=True, rc=0)) == '{"changed": true, "rc": 0}'
    assert jsonify(dict(changed=True, rc=0), format=True) == '{\n    "changed": true, \n    "rc": 0\n}'
    assert jsonify(None) == '{}'
    assert jsonify(dict(results=[1,2,3,4])) == '{"results": [1, 2, 3, 4]}'

# --- json filter test case ---

# Generated at 2022-06-13 07:22:09.311158
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({'a': 1, 'b':2}, format=True)
    result2 = jsonify(None)
    assert(result == '{\n    "a": 1, \n    "b": 2\n}')
    assert(result2 == '{}')

# Generated at 2022-06-13 07:22:15.737575
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    data = { 'test': AnsibleUnsafeText('test') }
    assert '"test"' in jsonify(data, False)


# Generated at 2022-06-13 07:22:20.460559
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": "b"}) == '{"a": "b"}', 'simple fail'
    assert jsonify({"a": "b"}, format=True) == '{\n    "a": "b"\n}', 'format fail'

# Generated at 2022-06-13 07:22:25.489006
# Unit test for function jsonify
def test_jsonify():
    expected = '{"some": "random", "json": "data"}\n'

    data = {
        'json': 'data',
        'some': 'random'
    }

    assert jsonify(data, True) == expected
    assert jsonify(data, False) == expected.rstrip()

# Generated at 2022-06-13 07:22:29.406531
# Unit test for function jsonify
def test_jsonify():
    # print('Testing jsonify')
    json_output1 = jsonify(dict(test=1))
    assert 'test' in json_output1
    return True



# Generated at 2022-06-13 07:22:37.898620
# Unit test for function jsonify
def test_jsonify():
    test_result = {
        'a': 1,
        'b': 2,
        'c': {
            'a': 1,
            'b': 2,
            '3': 3,
        },
    }
    result = jsonify(test_result, True)
    assert result == '''{
    "a": 1,
    "b": 2,
    "c": {
        "3": 3,
        "a": 1,
        "b": 2
    }
}'''

# Generated at 2022-06-13 07:22:47.255687
# Unit test for function jsonify
def test_jsonify():

    result = {
        'ms-win': {
            'version': 'Windows 2003 R2 SP2'
        },
        'ansible_facts': {
            'test_item': 'a test'
        },
        'changed': False,
        'ansible_ssh_host_key_fingerprint': '1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f',
        'invocation': {
            'module_name': 'setup'
        }
    }

    assert jsonify(result, format=True) == jsonify(result, format=False)

# Generated at 2022-06-13 07:22:58.870128
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert jsonify(None) == "{}"
    assert jsonify(dict()) == "{}"
    assert jsonify([]) == "[]"
    assert jsonify(dict(changed=False)) == '{"changed": false}'
    assert jsonify(dict(changed=True)) == '{"changed": true}'
    assert jsonify(dict(changed=False, results=[])) == '{"changed": false, "results": []}'
    assert jsonify(dict(changed=True, results=[])) == '{"changed": true, "results": []}'
    assert jsonify(dict(changed=False, results=[dict(foo='bar')])) == '{"changed": false, "results": [{"foo": "bar"}]}'

# Generated at 2022-06-13 07:23:06.369471
# Unit test for function jsonify
def test_jsonify():
    # Try it with and without formatting
    assert jsonify({}) == "{}"
    assert jsonify({"a": "b"}) == "{\"a\": \"b\"}"

    assert jsonify({}, format=True) == "{\n}"
    assert jsonify({"a": "b"}, format=True) == "{\n    \"a\": \"b\"\n}"

    # Try it with compression in unicode and non-unicode strings
    assert jsonify({"a": "b", "c": u"\u0105\u0107\u017c"}) == "{\"a\": \"b\", \"c\": \"\u0105\u0107\u017c\"}"

# Generated at 2022-06-13 07:23:11.629455
# Unit test for function jsonify
def test_jsonify():
    import sys
    from ansible.compat.tests import unittest

    class TestJsonify(unittest.TestCase):
        def test_jsonify_none(self):
            self.assertEqual('{}', jsonify(None))
            self.assertEqual('{}', jsonify(None, True))

        def test_jsonify_dict(self):
            self.assertEqual('{"a": "b"}', jsonify({'a': 'b'}))
            self.assertEqual('{"a": "b"}', jsonify({'a': 'b'}, False))
            self.assertEqual('''{\n    "a": "b"\n}''', jsonify({'a': 'b'}, True))


    # Run unit tests

# Generated at 2022-06-13 07:23:21.699332
# Unit test for function jsonify
def test_jsonify():
    bad_value_ansible_variables = dict(
        ansible_distribution         = "",
        ansible_distribution_release = "",
        ansible_distribution_version = "",
        ansible_os_family            = "",
    )
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(loader.load_inventory("tests/inventory_empty"))
    variable_manager.extra_vars = bad_value_ansible_variables
    variable_manager.options_vars = bad_value_ansible_variables
    variable_manager.set_globals(bad_value_ansible_variables)
    variable_manager.set_

# Generated at 2022-06-13 07:23:35.277763
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(changed=False, rc=0, stdout="foo")) == '{"changed": false, "rc": 0, "stdout": "foo"}'
    assert jsonify(dict(changed=False, rc=0, stdout=u"foo\u2014")) == '{"changed": false, "rc": 0, "stdout": "foo\u2014"}'
    assert jsonify(dict(changed=False, rc=0, stdout=u"foo\u2014"), format=True) == '{\n    "changed": false, \n    "rc": 0, \n    "stdout": "foo\u2014"\n}'

# Generated at 2022-06-13 07:23:37.949946
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(changed=True, rc=0)) == '{"changed": true, "rc": 0}'

# Generated at 2022-06-13 07:23:50.430329
# Unit test for function jsonify
def test_jsonify():
    def check_jsonify(result, expected_result):
        actual_result = jsonify(result)
        assert actual_result == expected_result, 'jsonify(%s) failed, expected: %s, actual: %s' % (repr(result), expected_result, actual_result)

    check_jsonify(None, "{}")
    check_jsonify({}, "{}")
    check_jsonify({"a":1}, '{"a": 1}')
    check_jsonify({"a":[1,2,3]}, '{"a": [1, 2, 3]}')
    check_jsonify([{"a": 1}, {"b": "foo"}], '[{"a": 1}, {"b": "foo"}]')
    check_jsonify([1,2,3], '[1, 2, 3]')
    check_json

# Generated at 2022-06-13 07:24:01.673103
# Unit test for function jsonify
def test_jsonify():
    import io
    import ast
    import yaml
    fact_data = {'ansible_eth0': {'ipv4': {'address': '172.17.0.2', 'netmask': '255.255.0.0', 'network': '172.17.0.0'}, 'ipv6': [{'address': 'fe80::42:acff:fe11:2', 'prefix': '64', 'scope': 'link'}], 'macaddress': '02:42:ac:11:00:02', 'module': 'e1000', 'mtu': 1500, 'type': 'ether'}}

    # Format JSON output (uncompressed or uncompressed)
    r1 = jsonify(fact_data, format=False)

# Generated at 2022-06-13 07:24:05.696362
# Unit test for function jsonify
def test_jsonify():
    data = {
        "key1": "value1",
        "key2": "value2"
    }

    output = jsonify(data, format=True)
    assert output == '''{
    "key1": "value1",
    "key2": "value2"
}'''

# Generated at 2022-06-13 07:24:08.920710
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}, format=True) == "{}"
    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'
    assert jsonify({"a": 1}, format=False) == '{"a": 1}'

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 07:24:14.549836
# Unit test for function jsonify
def test_jsonify():
    ''' unit tests for jsonify() '''
    result = dict(changed=True, foo='bar', baz=dict(arg1='value1', arg2=2))
    assert jsonify(result) == "{u'changed': True, u'baz': {u'arg1': u'value1', u'arg2': 2}, u'foo': u'bar'}"
    assert jsonify(result, format=True) == "{\n    \"changed\": true, \n    \"baz\": {\n        \"arg1\": \"value1\", \n        \"arg2\": 2\n    }, \n    \"foo\": \"bar\"\n}"
    result = dict(changed=True, foo='bar', baz=[dict(arg1='value1', arg2=2), dict(arg1='value1', arg2=3)])
   

# Generated at 2022-06-13 07:24:21.950591
# Unit test for function jsonify
def test_jsonify():
    ''' test for function jsonify '''

    json_result = jsonify(None, True)

    assert json_result == "{}"

    json_result = jsonify({'a': 1, 'b': 'foo'}, True)

    assert json_result == '''{
    "a": 1,
    "b": "foo"
}'''

    json_result = jsonify({u'a': 1, u'b': u'f\xf6\xf6'}, True)

    assert json_result == '''{
    "a": 1,
    "b": "f\xf6\xf6"
}'''


if __name__ == "__main__":
    import pytest
    pytest.main(['-s', __file__])

# Generated at 2022-06-13 07:24:29.176342
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify({"results": [{"foo": "bar"}, {"foo": "baz"}]}) == '{"results": [{"foo": "bar"}, {"foo": "baz"}]}'
    assert jsonify({"results": [{"foo": "\u3042"}, {"foo": "baz"}]}) == '{"results": [{"foo": "\u3042"}, {"foo": "baz"}]}'

# Generated at 2022-06-13 07:24:32.057737
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({}) == '{}'
    assert jsonify({'a':42}) == '{"a": 42}'


# Generated at 2022-06-13 07:24:46.220958
# Unit test for function jsonify
def test_jsonify():
    test_dict = {'a': 1234, 'b': [1, 2, 3], 'c': {'d': 4, 'e': 5}}
    test_none = None
    assert jsonify(test_dict) == '{"a": 1234, "b": [1, 2, 3], "c": {"d": 4, "e": 5}}'
    assert jsonify(test_dict, True) == '''{
    "a": 1234,
    "b": [
        1,
        2,
        3
    ],
    "c": {
        "d": 4,
        "e": 5
    }
}'''
    assert jsonify(test_none) == '{}'

# Generated at 2022-06-13 07:24:53.892692
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(['foo', 'bar']) == '["foo", "bar"]'
    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify("foo") == '"foo"'
    assert jsonify(1) == '1'
    assert jsonify(1) == '1'
    assert jsonify(False) == 'false'
    assert jsonify(None) == '{}'
    assert jsonify([]) == '[]'
    assert jsonify({}) == '{}'
    assert jsonify({}, format=True) == '{\n}'
    assert jsonify({"foo": ["bar", "baz"]}, format=True) == '{\n    "foo": [\n        "bar", \n        "baz"\n    ]\n}'

# Generated at 2022-06-13 07:24:56.982463
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify '''
    json.dumps({})
    json.dumps({}, indent=4)
    json.dumps('foo')
    json.dumps('foo', indent=4)

# Generated at 2022-06-13 07:25:02.778962
# Unit test for function jsonify
def test_jsonify():
    result = None
    assert jsonify(result) == "{}"

    result = dict(a=1)
    assert jsonify(result) == '{"a": 1}'
    assert jsonify(result, True) == '{\n    "a": 1\n}'

    result = dict(a=1, b=2)
    assert jsonify(result) == '{"a": 1, "b": 2}'
    assert jsonify(result, True) == '{\n    "a": 1, \n    "b": 2\n}'

# Generated at 2022-06-13 07:25:04.736848
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"test":0}) == '{"test": 0}'
    assert jsonify(["test"]) == '["test"]'
    assert jsonify("test") == '"test"'

# Generated at 2022-06-13 07:25:07.242027
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert '{\n    "result": "ok"\n}' == jsonify({'result': 'ok'}, True)

# Generated at 2022-06-13 07:25:11.017802
# Unit test for function jsonify
def test_jsonify():
    d = {u"val1": u"asdf", u"val2": [u'a', u'b', u'c'], u"val3": {u'key1': u'val1'}}
    j = jsonify(d)
    d2 = json.loads(j)
    assert(d == d2)

# Generated at 2022-06-13 07:25:18.680815
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic

    class FakeModule(object):
        def __init__(self):
            self.basic = basic.AnsibleModule
            basic.AnsibleModule.fail_json = lambda self, **kwargs: json.dumps(kwargs, sort_keys=True, indent=4)

    result = {
        "changed": False,
        "failed": False,
        "meta": {
            "x": "y"
        },
        "msg": "All items completed",
        "results": [
            {
                "item": "a",
                "msg": "ok",
            },
            {
                "item": "b",
                "msg": "ok",
            }
        ]
    }

    # print json results
    print(jsonify(result, format=True))



# Generated at 2022-06-13 07:25:24.235110
# Unit test for function jsonify
def test_jsonify():
    import sys
    import os
    from lib.ansible.module_utils.basic import AnsibleModule

    fields = {
        "changed": {
            "required": False,
            "type": "bool",
            "default": False
        },
        "failed": {
            "required": False,
            "type": "bool",
            "default": False
        },
        "warnings": {
            "required": False,
            "type": "list"
        },
        "invocation": {
            "required": False,
            "type": "dict"
        },
        "diff": {
            "required": False,
            "type": "dict"
        }
    }

    # We do not want to force people to install the package `six`

# Generated at 2022-06-13 07:25:27.486429
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 'this is some arbritrary data'}
    assert jsonify(result, True) == '''{
    "a": "this is some arbritrary data"
}'''

# Generated at 2022-06-13 07:25:42.084683
# Unit test for function jsonify
def test_jsonify():
    input = {'a': 1}
    assert jsonify(input, format=True) == '{\n    "a": 1\n}'
    assert jsonify(input, format=False) == '{"a": 1}'

# Generated at 2022-06-13 07:25:46.213597
# Unit test for function jsonify
def test_jsonify():
    import sys
    if sys.version_info.major == 2:
        assert jsonify("test") == "\"test\""
    else:
        assert jsonify("test") == "\"test\""


# Generated at 2022-06-13 07:25:57.020726
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'
    assert jsonify(dict(a=1, b=2), format=True) == '''{
    "a": 1,
    "b": 2
}
'''

    assert jsonify(dict(a=1, b=2, c=AnsibleUnsafeText(u'\u00e9'))) == u'{"a": 1, "b": 2, "c": "\\u00e9"}'

# Generated at 2022-06-13 07:26:11.266003
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic

    myinstance = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    # None -> {}
    assert jsonify(None) == u'{}'
    # {u'failed': False, u'invocation': {u'module_args': {}}, u'changed': False} ->
    # {
    #   "changed": false,
    #   "failed": false,
    #   "invocation": {
    #       "module_args": {}
    #   }
    # }
    assert jsonify(myinstance.exit_json(), format=True) == u'{\n    "changed": false, \n    "failed": false, \n    "invocation": {\n        "module_args": {}\n    }\n}'

   

# Generated at 2022-06-13 07:26:20.760122
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(jsonify(None)) == "{}"
    assert jsonify({"a": "b"}) == '{"a": "b"}'
    assert jsonify({"a": "b"}, True) == '{\n    "a": "b"\n}'
    assert jsonify([{"a": "b"}, {"c": "d"}]) == '[\n    {\n        "a": "b"\n    }, \n    {\n        "c": "d"\n    }\n]'
    assert jsonify([{"a": "b"}, {"c": "d"}], True) == '[\n    {\n        "a": "b"\n    }, \n    {\n        "c": "d"\n    }\n]'

# Generated at 2022-06-13 07:26:28.023482
# Unit test for function jsonify
def test_jsonify():
    # Unit test for function jsonify
    assert jsonify(dict(changed=False, rc=0)) == '{"rc": 0, "changed": false}'
    assert jsonify(dict(changed=True, rc=100)) == '{"rc": 100, "changed": true}'
    assert jsonify(dict(changed=True, rc=100), True) == '''{
    "rc": 100,
    "changed": true
}'''
    assert jsonify(dict(changed=False, rc=0), True) == '''{
    "rc": 0,
    "changed": false
}'''

# Generated at 2022-06-13 07:26:35.672984
# Unit test for function jsonify
def test_jsonify():
    from ansible.executor import module_common as mc
    from ansible.module_utils import basic

    result = dict(a=1, b=2)
    result = basic.AnsibleModule(argument_spec={}).exit_json(**result)
    result = jsonify(mc.add_paths('', result))
    assert result == '{"_ansible_no_log": false, "_ansible_verbose_always": true, "a": 1, "b": 2}'
    result = jsonify(mc.add_paths('', result), format=True)
    assert result == '{\n    "_ansible_no_log": false,\n    "_ansible_verbose_always": true,\n    "a": 1,\n    "b": 2\n}'

# Generated at 2022-06-13 07:26:44.476297
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

    assert jsonify(42) == "42"
    assert jsonify(42) != "24"

    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}) != '{"foo": "baz"}'

    assert jsonify({'foo': 'bar', 'baz': 42}) == '{"baz": 42, "foo": "bar"}'
    assert jsonify({'foo': 'bar', 'baz': 42}) != '{"baz": 24, "foo": "bar"}'

# Generated at 2022-06-13 07:26:49.347212
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(3) == "3"
    assert jsonify(3, True) == "3"
    assert jsonify({"a":1, "b":2}) == '{"a": 1, "b": 2}'
    assert jsonify({"a":1, "b":2}, True) == '{\n    "a": 1, \n    "b": 2\n}'

# Generated at 2022-06-13 07:27:00.055199
# Unit test for function jsonify
def test_jsonify():
    from subprocess import Popen, PIPE
    test_results = {
        "A": {
            "B": 1,
            "C": 2
        }
    }
    formatted = jsonify(test_results, True)
    unformatted = jsonify(test_results, False)
    # JSON should format like this
    assert(formatted == b'{\n    "A": {\n        "B": 1, \n        "C": 2\n    }\n}')
    # JSON should not format like this
    assert(unformatted == b'{"A": {"B": 1, "C": 2}}')
    # Test the JSON formatting with python -mjson.tool
    test_process = Popen(["python", "-mjson.tool"], stdin=PIPE, stdout=PIPE)
    test

# Generated at 2022-06-13 07:27:14.464879
# Unit test for function jsonify
def test_jsonify():
    # test a simple jsonify
    assert jsonify({'a':1, 'b':2}) == '{"a": 1, "b": 2}'

    # test an inplace jsonify
    assert jsonify({'a':1, 'b':2}, 'format') == '{\n    "a": 1, \n    "b": 2\n}'

# Generated at 2022-06-13 07:27:20.339175
# Unit test for function jsonify
def test_jsonify():
    def check(a, b):
        assert(a == b)

    check(jsonify(None), '{}')
    check(jsonify(42), '42')
    check(jsonify(42, True), '42')
    check(jsonify([1,2]), '[1, 2]')
    check(jsonify([1,2], True), '[\n    1,\n    2\n]')
    check(jsonify(dict(a=1,b=2)), '{"a": 1, "b": 2}')
    check(jsonify(dict(a=1,b=2), True), '{\n    "a": 1, \n    "b": 2\n}')

# Generated at 2022-06-13 07:27:30.993688
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1, b=2, c=3)) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify(dict(a=1, b=2, c=3), True) == '''{
    "a": 1,
    "b": 2,
    "c": 3
}'''
    assert jsonify(None) == "{}"
    assert jsonify("blah") == '"blah"'
    assert jsonify(["a", 1]) == '["a", 1]'
