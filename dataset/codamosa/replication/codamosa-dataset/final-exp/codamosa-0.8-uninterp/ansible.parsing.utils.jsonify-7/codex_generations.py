

# Generated at 2022-06-13 07:17:31.621879
# Unit test for function jsonify
def test_jsonify():
    # Test for None
    assert "{}" == jsonify(None)
    # Test for empty string
    assert '""' == jsonify("")
    # Test for string
    assert '"simple string"' == jsonify("simple string")
    # Test for dict
    assert '{}' == jsonify({})
    assert '{"a": "b"}' == jsonify({"a":"b"})

# Generated at 2022-06-13 07:17:44.096022
# Unit test for function jsonify
def test_jsonify():
    a = { "a" : 1, "b" : 2, "c" : { "c1" : 1, "c2" : 2 } }
    assert jsonify(a, True) == '{\n    "a": 1,\n    "b": 2,\n    "c": {\n        "c1": 1,\n        "c2": 2\n    }\n}'
    assert jsonify(a, False) == '{"a": 1, "b": 2, "c": {"c1": 1, "c2": 2}}'
    assert jsonify(None, True) == '{}'
    assert jsonify(None, False) == '{}'


# Generated at 2022-06-13 07:17:49.323212
# Unit test for function jsonify
def test_jsonify():
    # This function is just a wrapper around json.dumps so only sanity checking
    # is done here
    assert jsonify(dict(a=1, b=2)) == '{'\
                                          '"a":1,'\
                                          '"b":2'\
                                          '}'

    assert jsonify(dict(a=1, b=2), True) == '{\n'\
                                          '    "a":1,\n'\
                                          '    "b":2\n'\
                                          '}'

# Generated at 2022-06-13 07:17:56.819195
# Unit test for function jsonify
def test_jsonify():
    data = { "key1" : "value1", "key2" : { "key3" : [ 1, 2, 3 ] } }
    assert jsonify(data) == '{"key1": "value1", "key2": {"key3": [1, 2, 3]}}'
    assert jsonify(data, True) == '''{
    "key1": "value1",
    "key2": {
        "key3": [
            1,
            2,
            3
        ]
    }
}'''

# Generated at 2022-06-13 07:18:01.040491
# Unit test for function jsonify
def test_jsonify():
    '''
    Test case for ansible.utils.jsonify
    '''
    result = jsonify({'foo':'bar'})
    assert result == '{"foo": "bar"}'

    # --
    result = jsonify({'foo':'bar'}, format=True)
    assert result == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:18:11.131883
# Unit test for function jsonify
def test_jsonify():
    my_var = {
        'a': 'b',
        'c': 'd',
        'e': {
            'f': 'g',
            'h': 'i'
        }
    }
    result = jsonify(my_var, format=True)
    assert result == '''{
    "a": "b",
    "c": "d",
    "e": {
        "f": "g",
        "h": "i"
    }
}'''
    result = jsonify(my_var, format=False)
    assert result == '{"a": "b", "c": "d", "e": {"f": "g", "h": "i"}}'
    result = jsonify(my_var)

# Generated at 2022-06-13 07:18:15.688825
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.utils.json_safe_prep import json_safe_prep_value
    from ansible.runner.return_data import ReturnData
    import ansible

    # This is a subset of the data that ReturnData would normally
    # return to the runner.  We will use it to test the jsonify
    # function.

# Generated at 2022-06-13 07:18:20.197456
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unsafe_proxy import wrap_var

    data = wrap_var({
        'test': 1234,
        'test2': 'test'
    })

    expected = '''{
    "test": 1234,
    "test2": "test"
}'''

    assert jsonify(data, True) == expected

# Generated at 2022-06-13 07:18:27.512200
# Unit test for function jsonify
def test_jsonify():
    # Empty resultset
    data = []
    out = jsonify(data, True)
    assert out == json.dumps(data, sort_keys=True, indent=4)

    # Valid resultset
    data = [{u'foo': u'bar'}]
    out = jsonify(data, True)
    assert out == json.dumps(data, sort_keys=True, indent=4)

    # Invalid resultset
    data = [{u'foo': u'bar', 'baz': u'qux'}]
    out = jsonify(data, True)
    assert out == json.dumps(data, sort_keys=True, indent=4)

    # output=no_format resultset
    data = [{u'foo': u'bar', 'baz': u'qux'}]
   

# Generated at 2022-06-13 07:18:34.689710
# Unit test for function jsonify
def test_jsonify():
    result = {
        "changed": True,
        "foo": "bar",
        "empty": "",
        "a": 1,
        "b": 2,
        "c": 3,
        "d": {
            "e": 4,
            "f": 5,
            "g": 6,
            "h": [7, 8, 9],
            "i": {
                "j": 10,
                "k": 11,
                "l": 12
            }
        }
    }

    # unordered

# Generated at 2022-06-13 07:18:43.629996
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":1}) == '{"a": 1}'
    assert jsonify({"a":1}, True) == '{\n    "a": 1\n}'
    assert jsonify({"b":2, "a":1}, True) == '{\n    "a": 1, \n    "b": 2\n}'
    assert jsonify({"b":2, "a":1}, False) == '{"a": 1, "b": 2}'
    assert jsonify(["a","b","c"], False) == '["a", "b", "c"]'
    assert jsonify({"a":"\u3042"}, True) == '{\n    "a": "\u3042"\n}'

# Generated at 2022-06-13 07:18:55.555499
# Unit test for function jsonify
def test_jsonify():

    class _RawText:
        def __init__(self, text):
            self.text = text
        def __unicode__(self):
            return unicode(self.text)
        def __str__(self):
            return self.text

    # check the no-op case
    assert jsonify(None) == "{}"

    # check formatting
    result = {'a': {'b': 'c'}}
    assert jsonify(result, format=True) == '{\n    "a": {\n        "b": "c"\n    }\n}'

    # check that formatting also works for lists
    result = ['a', {'b': 'c'}]

# Generated at 2022-06-13 07:19:01.509161
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify([]) == '[]'
    assert jsonify({"a":1})
    assert jsonify(["a"])
    assert jsonify({"a": [1,2,3], "b": [4,5,6]})

# -- not really a filter but close enough


# Generated at 2022-06-13 07:19:08.811116
# Unit test for function jsonify
def test_jsonify():

    def _ensure(result, expected):
        result = jsonify(result, format=True)
        assert result == expected, "%s != %s" % (result, expected)

    _ensure(None, '{}')
    _ensure('foo', '"foo"')
    _ensure([1,2,3], '[\n    1, \n    2, \n    3\n]')
    _ensure({'a':1, 'b':2}, '{\n    "a": 1, \n    "b": 2\n}')

    # extra testing for unicode (with utf-8)
    if 'sure'.encode('utf-8') == 'sure'.encode():
        _ensure(u'sure', '"sure"')

# Generated at 2022-06-13 07:19:16.741060
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(changed=True, rc=0, stdout="hello")) == '{"changed": true, "rc": 0, "stdout": "hello"}'
    assert jsonify(dict(changed=True, rc=0, stdout="hello"), True) == '{\n    "changed": true, \n    "rc": 0, \n    "stdout": "hello"\n}'
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:20.145761
# Unit test for function jsonify
def test_jsonify():
    data = {"a": 1}
    assert jsonify(data) == json.dumps(data)
    assert jsonify(data, format=True) == json.dumps(data, sort_keys=True, indent=4)

# Generated at 2022-06-13 07:19:24.277504
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == '{"a": 1}'
    assert jsonify({"a": 1}, format=True) == '{\n    "a": 1\n}'
    assert jsonify({"a": [2, 3, None, {"c": "d"}]}, format=True) == '''{
    "a": [
        2,
        3,
        null,
        {
            "c": "d"
        }
    ]
}'''

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:19:32.218400
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == "{\"a\": 1}"
    assert jsonify({"a": ["b", "c"]}) == "{\"a\": [\"b\", \"c\"]}"
    assert jsonify({"a": {"b": "c"}}) == "{\"a\": {\"b\": \"c\"}}"
    assert jsonify(None) == "{}"
    assert jsonify({"a": 1}, True) == "{\n    \"a\": 1\n}"
    assert jsonify({"a": ["b", "c"]}, True) == "{\n    \"a\": [\n        \"b\", \n        \"c\"\n    ]\n}"
    assert jsonify({"a": {"b": "c"}}) == "{\"a\": {\"b\": \"c\"}}"
    assert jsonify(None)

# Generated at 2022-06-13 07:19:41.639283
# Unit test for function jsonify
def test_jsonify():
    # Make sure we can take any object and successfully JSON-ify it

    # Test string
    input_string = "this is a test string"
    expected_string = '"this is a test string"'
    assert jsonify(input_string) == expected_string

    # Test dictionary
    input_dict = {'foo':'bar'}
    expected_dict = '{"foo": "bar"}'
    assert jsonify(input_dict) == expected_dict

    # Test list
    input_list = ['foo', 'bar']
    expected_list = '["foo", "bar"]'
    assert jsonify(input_list) == expected_list

# Generated at 2022-06-13 07:19:51.061794
# Unit test for function jsonify
def test_jsonify():

    # Test for None
    assert jsonify(None) == "{}"

    # Test for empty list
    assert jsonify([]) == "[]"

    # Test for list
    assert jsonify([1,2,3]) == "[1, 2, 3]"

    # Test for empty dict
    assert jsonify({}) == "{}"

    # Test for dict
    assert jsonify({"one":1, "two":2, "three":3}) == '{"three": 3, "two": 2, "one": 1}'

    # Test for formatting
    assert jsonify({"one":1, "two":2, "three":3}, format=True) == '{\n    "three": 3,\n    "two": 2,\n    "one": 1\n}'

# Generated at 2022-06-13 07:20:07.736164
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for function jsonify '''

    from ansible.utils.boolean import boolean

    # verify empty result created when None passed
    result = jsonify(None)
    assert result == '{}'

    # test dictionary gets jsonified
    result = jsonify({ 'test': 'result' })
    assert result == '{"test": "result"}'

    # test complex dictionary gets jsonified
    result = jsonify({ 'test': { 'inner': 'result' } })
    assert result == '{"test": {"inner": "result"}}'

    # test list gets jsonified
    result = jsonify(['test', 'result'])
    assert result == '["test", "result"]'

    # test boolean True gets jsonified
    result = jsonify(boolean(True))
    assert result == 'true'

    # test

# Generated at 2022-06-13 07:20:11.010842
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify([{'a':'a'}]) == '[\n    {\n        "a": "a"\n    }\n]'



# Generated at 2022-06-13 07:20:13.574383
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:20:18.781121
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == "{}"
    assert jsonify({ 'a': 1, 'b': 2 }) == '{"a": 1, "b": 2}'
    assert jsonify({ 'a': 1, 'b': 2 }, format=True) == '{\n    "a": 1, \n    "b": 2\n}'

# Generated at 2022-06-13 07:20:27.496058
# Unit test for function jsonify
def test_jsonify():

    def result_noformat(result):
        assert jsonify(result, format=False) == '{"a": "foo", "b": "bar"}'

    def result_noformat_none(result):
        assert jsonify(result, format=False) == "{}"

    def result_format(result):
        assert jsonify(result, format=True) == '''{
    "a": "foo",
    "b": "bar"
}'''

    def result_format_none(result):
        assert jsonify(result, format=True) == "{}"

    # results are utf-8
    result_noformat({u'a': u'foo', u'b': u'bar'})
    result_format({u'a': u'foo', u'b': u'bar'})

# Generated at 2022-06-13 07:20:30.729044
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":"b"}) == '{"a": "b"}'
    assert jsonify({"a":"b"}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:20:38.443873
# Unit test for function jsonify
def test_jsonify():
    # Test empty result
    result = None
    assert jsonify(result) == "{}"

    # Test formatted and unformatted json
    result = {'a': 1, 'b': 2, 'c': 3}
    assert jsonify(result, True) == "{\"a\": 1, \"b\": 2, \"c\": 3}"

    # Test json with unicode characters
    result = {'a': 1, 'b': 2, u'\u10c8': 3}
    assert jsonify(result) == "{\"a\": 1, \"b\": 2, \"\u10c8\": 3}"


# Generated at 2022-06-13 07:20:44.600082
# Unit test for function jsonify
def test_jsonify():
    # Testing jsonify with non-dict (should return dict)
    result = None
    print(jsonify(result))

    # Testing jsonify with empty dict and format=True
    result = {}
    print(jsonify(result, True))

    # Testing jsonify with dict result and format=True
    result = dict(changed=False, rc=0)
    print(jsonify(result, True))

# Run test
test_jsonify()

# Generated at 2022-06-13 07:20:56.482800
# Unit test for function jsonify
def test_jsonify():
    result = {
        '1': 'a',
        '2': 'b',
        '3': 'c'
    }
    result2 = {
        '4': None
    }
    result_str = '{\n    "1": "a", \n    "2": "b", \n    "3": "c"\n}'
    result2_str = '{\n    "4": null\n}'
    assert(jsonify(result, True) == result_str)
    assert(jsonify(result) == json.dumps(result, sort_keys=True))
    assert(jsonify(result2, True) == result2_str)

# Generated at 2022-06-13 07:21:02.465569
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":1}) == "{\"a\": 1}"
    assert jsonify({"a":1}, format=True) == "{\n    \"a\": 1\n}"
    assert jsonify({"a":1}, format='yes') == "{\n    \"a\": 1\n}"

if __name__ == '__main__':
    import nose
    nose.runmodule()

# Generated at 2022-06-13 07:21:18.285196
# Unit test for function jsonify
def test_jsonify():
    data = { 'a': 'foo', 'b': [1, 2, 3], 'c': set([4,5,6]) }
    assert jsonify(data, format=True) == '{\n    "a": "foo", \n    "b": [\n        1, \n        2, \n        3\n    ], \n    "c": [\n        4, \n        5, \n        6\n    ]\n}\n'
    assert jsonify(data, format=False) == '{"a": "foo", "b": [1, 2, 3], "c": [4, 5, 6]}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:21:32.511281
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(None) == "{}"
    assert jsonify('foo') == "\"foo\""
    assert jsonify({"foo":"bar"}) == "{\"foo\": \"bar\"}"
    assert jsonify({"foo":"bar"},format=True) == "{\n    \"foo\": \"bar\"\n}"

    # test byte string input
    assert jsonify({"foo": b"bar"}) == "{\"foo\": \"bar\"}"

    # test float input
    assert jsonify({"foo":1.0}) == "{\"foo\": 1.0}"

    # test int input
    assert jsonify({"foo":1}) == "{\"foo\": 1}"

    # test boolean input
    assert jsonify({"foo":True}) == "{\"foo\": true}"

    # test None input

# Generated at 2022-06-13 07:21:41.053160
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify(None, True) == "{}"
    assert jsonify({"a": True, "b": False, "c": None}) == '{"a": true, "b": false, "c": null}'
    assert jsonify({"a": True, "b": False, "c": None}, True) == '{\n    "a": true, \n    "b": false, \n    "c": null\n}'
    assert jsonify({'a': u'\u0430', 'b': u'\u0431'}) in (u'{"a": "а", "b": "б"}', u'{"b": "б", "a": "а"}')

# Generated at 2022-06-13 07:21:42.656478
# Unit test for function jsonify
def test_jsonify():
    result = dict(foo="bar")
    assert jsonify(result, format=True) == '''{
    "foo": "bar"
}'''

# Generated at 2022-06-13 07:21:52.949561
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(
        {
            "changed": True,
            "msg": "This is a long message that will be encoded in JSON "
                   "and therefore not wrap under most circumstances.  "
                   "Much longer than what would fit on one line of "
                   "output printed to an 80 column wide terminal.",
            "ping": "pong",
        }) == json.dumps(
        {
            "changed": True,
            "msg": "This is a long message that will be encoded in JSON "
                   "and therefore not wrap under most circumstances.  "
                   "Much longer than what would fit on one line of "
                   "output printed to an 80 column wide terminal.",
            "ping": "pong",
        }, sort_keys=True, indent=4, ensure_ascii=False)

# Generated at 2022-06-13 07:21:57.997054
# Unit test for function jsonify

# Generated at 2022-06-13 07:22:06.057512
# Unit test for function jsonify
def test_jsonify():
    j = { "boo" : 5, "foo" : [1, 2, 3, {"foo" : "bar"}] }
    assert jsonify(j) == '{"boo": 5, "foo": [1, 2, 3, {"foo": "bar"}]}'
    assert jsonify(j, format=True) == '{\n    "boo": 5, \n    "foo": [\n        1, \n        2, \n        3, \n        {\n            "foo": "bar"\n        }\n    ]\n}'

# Generated at 2022-06-13 07:22:13.275586
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":"b"}) == '{"a": "b"}'
    assert jsonify({"a":"b"}, True) == '{\n    "a": "b"\n}'
    assert jsonify({"a":"b"}, False) == '{"a": "b"}'
    assert jsonify({"a":"b"}, True) == '{\n    "a": "b"\n}'
    assert jsonify({"a":"b"}, False) == '{"a": "b"}'
    assert jsonify({"a":[1,2,3]}, True) == '{\n    "a": [\n        1, \n        2, \n        3\n    ]\n}'
    assert jsonify({"a": {"b": "c"}}) == '{"a": {"b": "c"}}'

# Generated at 2022-06-13 07:22:21.029673
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify() returns JSON
    '''

    # jsonify(None) returns "{}"
    assert jsonify(None) == '{}'

    # jsonify(dict) returns json string
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'

    # jsonify must be able to handle unicode characters
    assert jsonify({'perl': 'Dürst'}) == '{"perl": "Dürst"}'

# Generated at 2022-06-13 07:22:27.582812
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None, format=False) == "{}"
    assert jsonify(None, format=True) == "{}"
    # test jsonify function with different input values
    assert jsonify({'a':'b'}, format=False) == '{"a": "b"}'
    assert jsonify({'a':'b'}, format=True) == '{\n    "a": "b"\n}'
    assert jsonify([1,2,3], format=True) == '[\n    1, \n    2, \n    3\n]'

# Generated at 2022-06-13 07:22:45.773310
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    result = {u'a': [1, 2, 3, u'4'],
              u'b': u'a string',
              u'c': {u'a subdict': u'with a string value'},
             }
    result_unicode = to_unicode(jsonify(result))
    result_compact = to_unicode(jsonify(result, format=False))
    # The "result_formatted" value must be exactly as it is below (spaces and new lines)
    # to make sure that it is correctly parsed regardless of the OS in use (and to prevent
    # any undesired code reformating by the editor).

# Generated at 2022-06-13 07:22:47.779708
# Unit test for function jsonify
def test_jsonify():
    js = jsonify({'foo': 'bar'})
    assert js == '{"foo": "bar"}'

# Generated at 2022-06-13 07:22:48.899614
# Unit test for function jsonify
def test_jsonify():
    # TODO implement this
    pass

# Generated at 2022-06-13 07:23:00.191984
# Unit test for function jsonify
def test_jsonify():

    def check(result, expected, **kwargs):
        actual = jsonify(result, **kwargs)
        assert actual == expected

    check(None, "{}")
    check(dict(a=1), '{"a": 1}')
    check(dict(a=1), '{\n    "a": 1\n}', format=True)
    check(dict(a=u"\u1234"), u'{"a": "\u1234"}') # utf-8
    check(dict(a=u"\u1234"), u'{\n    "a": "\u1234"\n}', format=True) # utf-8
    check(dict(a=u"\u1234".encode("utf-16")), u'{"a": "\ufffd"}') # utf-16

# Generated at 2022-06-13 07:23:02.726541
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify(None) == "{}")
    assert(jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}')

# Generated at 2022-06-13 07:23:06.095826
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify('foo') == '"foo"'
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify({'foo':True}) == '{"foo": true}'

# Generated at 2022-06-13 07:23:15.261589
# Unit test for function jsonify
def test_jsonify():

    # Normal dictionary
    dictionary = {
        'foo' : 'bar',
        'boo' : 'baz'
    }

    # Encode dictionary as json
    json_string = jsonify(dictionary)

    # Expect the result to be a JSON string
    assert isinstance(json_string, str)

    # Decode the string into a dictionary
    json_dict = json.loads(json_string)

    # Expect the result to be the same dictionary
    assert dictionary == json_dict


    # Fail Case : Non Dictionary Input
    non_dict_value = set([1,2,3])

    # Expect an exception when trying to encode
    try:
        jsonify(non_dict_value)
    except TypeError:
        pass

# Generated at 2022-06-13 07:23:19.758116
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify([]) == "[]"
    assert jsonify({}) == "{}"
    assert jsonify({'a':1}) == '{"a": 1}'
    assert jsonify([1,2]) == "[1, 2]"


# Generated at 2022-06-13 07:23:23.835830
# Unit test for function jsonify
def test_jsonify():
    results = [{"a": 1}, None, {}, {"a": 1, "b": 2}]
    expected = ['{"a": 1}', "{}", "{}", '{"a": 1, "b": 2}']

    for i in range(len(results)):
        assert jsonify(results[i]) == expected[i]

# Generated at 2022-06-13 07:23:26.324699
# Unit test for function jsonify
def test_jsonify():
    assert type(jsonify("{}")) == type("")
    assert jsonify({"key1": "value1"}) == '{"key1": "value1"}'

# Generated at 2022-06-13 07:23:53.304628
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None).encode('utf-8') == "{}"
    assert jsonify({'a': 'b'}).encode('utf-8') == '{"a": "b"}'
    assert jsonify({'a': 'b'}, True).encode('utf-8') == '{\n    "a": "b"\n}'
    assert jsonify([1,2,3]).encode('utf-8') == '[1, 2, 3]'
    assert jsonify([1,2,3], True).encode('utf-8') == '[\n    1,\n    2,\n    3\n]'

# Generated at 2022-06-13 07:24:02.720333
# Unit test for function jsonify
def test_jsonify():
    result = {'foo': 1, 'bar': 456, 'bam': ['a','b','c'], 'baz': 'string'}
    plain  = jsonify(result)

    assert plain == '{"bar": 456, "bam": ["a", "b", "c"], "foo": 1, "baz": "string"}'

    pretty = jsonify(result, format=True)

    print(pretty)

    assert pretty == '{\n    "bar": 456, \n    "bam": [\n        "a", \n        "b", \n        "c"\n    ], \n    "foo": 1, \n    "baz": "string"\n}'

# Generated at 2022-06-13 07:24:04.279320
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'test': 'result'}, format=True) == '''{
    "test": "result"
}'''

    assert jsonify({'test': 'result'}, format=False) == '{"test": "result"}'

# Generated at 2022-06-13 07:24:07.169455
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify({"foo": "bar"}, True) == jsonify({"foo": "bar"}, False)
    assert '\n' in jsonify({"foo": "bar"}, True)



# Generated at 2022-06-13 07:24:13.386701
# Unit test for function jsonify
def test_jsonify():

    # list, format=True
    data_in = ["hello", "world"]
    data_out = jsonify(data_in, True)
    assert data_out == '[\n    "hello", \n    "world"\n]'

    # dict, format=True
    data_in = {"hello": "world"}
    data_out = jsonify(data_in, True)
    assert data_out == '{\n    "hello": "world"\n}'

    # dict, format=False
    data_in = {"hello": "world"}
    data_out = jsonify(data_in, False)
    assert data_out == '{"hello": "world"}'

    # dict with unicode, format=True
    data_in = {"hello": u"wörld"}

# Generated at 2022-06-13 07:24:19.411933
# Unit test for function jsonify
def test_jsonify():

    # Catch JSON dump exceptions, but let other exceptions raise to the caller
    try:
        assert jsonify(None) == "{}"
    except Exception:
        assert False

    try:
        assert jsonify({'a': 1}) == '{"a": 1}'
    except Exception:
        assert False

    try:
       assert jsonify({'a': 1}, format=True) == '''{
    "a": 1
}'''
    except Exception:
        assert False

# Generated at 2022-06-13 07:24:33.425814
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({'foo': 'bar'}, format=False)
    assert result == '{"foo": "bar"}', result

    result = jsonify({'foo': 'bar'}, format=True)
    assert result == '{\n    "foo": "bar"\n}', result

    result = jsonify({u'宮本': {u'岬': u'鋸'}}, format=False)
    assert result == '{"\xe5\xae\xae\xe6\x9c\xac": {"\xe5\xb2\xac": "\xe9\x8b\xb8"}}', result

    result = jsonify({u'宮本': {u'岬': u'鋸'}}, format=True)

# Generated at 2022-06-13 07:24:39.936253
# Unit test for function jsonify
def test_jsonify():
    ''' make sure the jsonify function works as expected '''

    results = {'a':1,'b':2}

    # Does it handle a none value?
    assert jsonify(None) == '{}'

    # Does it handle a unicode value?
    assert jsonify(u'\xf4') == u'"\xf4"'

    # Does it produce a properly formatted unicode string?
    assert jsonify(u'\xf4', True) == u'"\xf4"'

    # Does it produce a properly formatted output?
    assert jsonify(results, True) == '{\n    "a": 1, \n    "b": 2\n}'

    # Does it produce a properly formatted output?
    assert jsonify(results) == '{"a":1,"b":2}'



# Generated at 2022-06-13 07:24:49.279844
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils.encrypt import do_encrypt, do_decrypt

    test_data = dict(
        a = {
            'b': 'c',
        }
    )

    encrypted_data = do_encrypt(jsonify(test_data), b'ansible')

    assert jsonify(test_data) == '''{
    "a": {
        "b": "c"
    }
}'''

    assert jsonify(test_data, format=True) == '''{
    "a": {
        "b": "c"
    }
}'''

    assert jsonify(json.loads(jsonify(test_data))) == jsonify(test_data)

# Generated at 2022-06-13 07:24:56.235327
# Unit test for function jsonify
def test_jsonify():
    results = {
        'contacted': {
            'localhost': {
                'changed': True,
                'ping': 'pong'
            }
        },
        'dark': {},
    }
    jsonified = jsonify(results, True)
    assert jsonified == '{\n    "contacted": {\n        "localhost": {\n            "changed": true, \n            "ping": "pong"\n        }\n    }, \n    "dark": {}\n}'


# Generated at 2022-06-13 07:25:43.299011
# Unit test for function jsonify
def test_jsonify():
    test_data_non_unicode = {
        'a' : 1,
        'b' : 'simple string',
        'c' : None,
        'd' : [ 'one', 'two', 'three' ],
        'e' : { 'one' : 1, 'two' : 2, 'three' : 3 }
    }
    assert jsonify(test_data_non_unicode, False) == '{"a": 1, "c": null, "b": "simple string", "e": {"one": 1, "three": 3, "two": 2}, "d": ["one", "two", "three"]}'

# Generated at 2022-06-13 07:25:49.167464
# Unit test for function jsonify
def test_jsonify():
    result = {
        'msg': 'system information as requested',
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python'
        }
    }
    print(jsonify(result))

if __name__ == "__main__":
    test_jsonify()

# Generated at 2022-06-13 07:25:54.740529
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({u'a': u'b'}) == jsonify({'a': 'b'})
    assert jsonify({u'a': u'b'}) == '{"a": "b"}'
    assert jsonify({u'a': u'b'}, True) == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 07:26:00.818466
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a":1}) == '{"a": 1}'
    assert jsonify({"a":1}, format=True) == '''{
    "a": 1
}'''
    # Test some default JSON 'special' characters
    assert jsonify({"a":"\b\f\n\r\t"}) == '{"a": "\\b\\f\\n\\r\\t"}'

# Generated at 2022-06-13 07:26:13.395984
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify: Return JSON from data structure

    >>> jsonify({"foo": "bar"})
    '{"foo": "bar"}'
    >>> jsonify({"foo": ["bar", "baz"]})
    '{"foo": ["bar", "baz"]}'
    >>> jsonify({"foo": ["bar", {"baz": "qux"}]})
    '{"foo": ["bar", {"baz": "qux"}]}'
    >>> jsonify({"foo": {"bar": "baz", "qux": "quux"}})
    '{"foo": {"bar": "baz", "qux": "quux"}}'
    '''
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:26:19.051206
# Unit test for function jsonify
def test_jsonify():
    result = {'a': 'b'}
    assert jsonify(result) == jsonify(result, True) == '{\n    "a": "b"\n}'
    result = {'a': 'b', 'c': 'd'}
    assert jsonify(result) == jsonify(result, True) == '{"a": "b", "c": "d"}'


# Generated at 2022-06-13 07:26:22.950534
# Unit test for function jsonify
def test_jsonify():
    ''' unit test for ansible.utils.jsonify '''
    assert jsonify([1,2,3]) == '[1, 2, 3]'
    assert jsonify([1,2,3],format=True) == '''[
    1,
    2,
    3
]'''

# Generated at 2022-06-13 07:26:28.903034
# Unit test for function jsonify
def test_jsonify():

    assert jsonify(dict(a=(1,2,3), b=dict(c=9))) == \
        '{"a": [1, 2, 3], "b": {"c": 9}}'

    assert jsonify(dict(a=(1,2,3), b=dict(c=9)), True) == \
        '{\n    "a": [\n        1, \n        2, \n        3\n    ], \n    "b": {\n        "c": 9\n    }\n}'

# Generated at 2022-06-13 07:26:36.148570
# Unit test for function jsonify
def test_jsonify():

    import re
    import sys

    if sys.version_info[0] >= 3:
        unicodestring = 'u\''
    else:
        unicodestring = 'u'

    data = {"blah": "foo", "foo": "blah"}
    result = jsonify(data)
    assert result == '{"blah": "foo", "foo": "blah"}', result

    jsonstr = re.compile(r'^\s*\{\n\s+"blah": "foo",\n\s+"foo": "blah"\n\s*\}\s*$')
    result = jsonify(data, format=True)
    assert jsonstr.match(result), result


# Generated at 2022-06-13 07:26:41.880131
# Unit test for function jsonify
def test_jsonify():
    data = {'test':{'test2':{'test3':{'test4':'test5'}}}}
    assert jsonify(data, format=True) == '{\n    "test": {\n        "test2": {\n            "test3": {\n                "test4": "test5"\n            }\n        }\n    }\n}'