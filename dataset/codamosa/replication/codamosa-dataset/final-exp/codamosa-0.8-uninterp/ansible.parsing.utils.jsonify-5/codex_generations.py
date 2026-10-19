

# Generated at 2022-06-13 07:17:32.816120
# Unit test for function jsonify
def test_jsonify():
    result = {}
    result['foo'] = 'bar'
    assert jsonify(result, True) == '{\n    "foo": "bar"\n}'
    assert jsonify(result) == '{"foo": "bar"}'

# Generated at 2022-06-13 07:17:46.171934
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"

    # Check the empty case
    my_dict = dict()
    assert jsonify(my_dict) == "{}"

    # Check an integer
    my_dict = dict(one=1)
    assert jsonify(my_dict) == '{"one": 1}'

    # Check an array
    my_dict = dict(one=1, two=2, three=[1,2,3])
    assert jsonify(my_dict) == '{"one": 1, "two": 2, "three": [1, 2, 3]}'

    # Check with unicode
    unicode_str = u'\u2713' # check mark
    my_dict = dict(one=1, two=unicode_str)

# Generated at 2022-06-13 07:17:56.895418
# Unit test for function jsonify
def test_jsonify():

    # Empty result
    assert jsonify(None) == '{}'

    # Simple Python hash
    test_result = {'a': 1, 'b': 2}
    assert jsonify(test_result) == '{"a": 1, "b": 2}'

    # More sophisticated Python hash
    test_result = {'False': False, 'True': True, 'None': None,
                   'float': 1.1, 'simple_list': [1,2,3],
                   'simple_dict': {'a':1, 'b':2}}

    assert jsonify(test_result) == '{"False": false, "None": null, "True": true, "float": 1.1, "simple_dict": {"a": 1, "b": 2}, "simple_list": [1, 2, 3]}'

    # List with hash

# Generated at 2022-06-13 07:18:05.375978
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should format JSON output (uncompressed or uncompressed) '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert jsonify({}) == '{}'
    assert jsonify({}, True) == '{\n    \n}'
    assert jsonify([]) == '[]'
    assert jsonify(AnsibleUnsafeText(b'abc')) == '"abc"'
    assert jsonify(AnsibleUnsafeText(u'abc')) == u'"abc"'
    assert jsonify(AnsibleUnsafeText(u'\\')) == u'"\\\\"'
    assert jsonify(AnsibleUnsafeText(b'\\')) == '"\\\\"'
            # Ensure the double escaped string is properly decoded back
            # to an "escaped" slash when being read by the json

# Generated at 2022-06-13 07:18:06.109720
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(failed=False, changed=False)) == "{}"

# Generated at 2022-06-13 07:18:14.072267
# Unit test for function jsonify
def test_jsonify():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from units.compat import unittest

    class TestJsonify(unittest.TestCase):

        def test_basic_jsonify(self):
            data = {'a':1}
            self.assertEqual(jsonify(data), '{\n    "a": 1\n}')

        def test_jsonify_none(self):
            self.assertEqual(jsonify(None), "{}")

    # Run it if invoked directly
    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 07:18:24.140544
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify

    # None input
    assert jsonify(None) == "{}"


    # Single string element
    test_input = { "test": "value" }
    test_result = jsonify(test_input)
    assert '"test": "value"' in test_result


    # Many elements
    test_input = {
        "test1": "test1value",
        "test2": "test2value",
        "test3": "test3value"
    }
    test_result = jsonify(test_input)
    assert '"test1": "test1value"' in test_result
    assert '"test2": "test2value"' in test_result
    assert '"test3": "test3value"' in test_result


    # Tuple

# Generated at 2022-06-13 07:18:33.734679
# Unit test for function jsonify
def test_jsonify():
    # We should always be able to serialize None
    assert jsonify(None) == "{}"

    # We should always be able to serialize integers
    assert jsonify(1) == '1'

    # We should always be able to serialize strings
    assert jsonify("some string") == '"some string"'

    # We should always be able to serialize lists of integers
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'

    # We should always be able to serialize dictionaries with integers
    assert jsonify({'foo': 1, 'bar': 2}) == '{"bar": 2, "foo": 1}'

    # We should always be able to serialize lists of mixed data
    assert jsonify([1, 2, "foo"]) == '[1, 2, "foo"]'

    # We should always be able to

# Generated at 2022-06-13 07:18:37.875682
# Unit test for function jsonify
def test_jsonify():

    # Test JSON output of various data structures
    data = [None, [1, 2, 3], { 'a': 1, 'b': 2 }, True, False, 'string']

    for d in data:
        print (jsonify(d, format=False))
        print (jsonify(d, format=True))

if __name__ == "__main__":
    test_jsonify()

# Generated at 2022-06-13 07:18:42.076174
# Unit test for function jsonify
def test_jsonify():
    result = {'abc': [1,2,3], 'foo': 'bar'}
    assert ( jsonify(result, False) == '{"abc": [1, 2, 3], "foo": "bar"}')
    assert ( jsonify(result, True ) == '''{
    "abc": [
        1,
        2,
        3
    ],
    "foo": "bar"
}''')

# Generated at 2022-06-13 07:18:48.194523
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('{"a":"b"}') == '{"a": "b"}'
    assert jsonify('{"a":"b"}', True) == '''\
{
    "a": "b"
}'''


# Generated at 2022-06-13 07:18:53.977664
# Unit test for function jsonify
def test_jsonify():
    result = dict(test=dict(a=1, b=2, c=3))
    assert jsonify(result) == '{"test": {"a": 1, "b": 2, "c": 3}}'
    assert jsonify(result, True) == '''{
    "test": {
        "a": 1,
        "b": 2,
        "c": 3
    }
}'''

# Generated at 2022-06-13 07:18:56.601688
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed='something')
    assert jsonify(result) == '{"changed": "something"}'
    assert jsonify(result, True) == '{\n    "changed": "something"\n}'



# Generated at 2022-06-13 07:19:06.773083
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    from ansible.parsing.ajson import AnsibleJSONEncoder

    my_dict = {'fooboozoo': {'unicode_field': '\xe9'},
               'boo': ['foo', 'bar', {'baz': 'abc'}]}
    expected = '{"boo": ["foo", "bar", {"baz": "abc"}], "fooboozoo": {"unicode_field": "\\u00e9"}}'

# Generated at 2022-06-13 07:19:12.614823
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'
    assert jsonify(None) == "{}"
    assert jsonify(dict()) == "{}"

# Generated at 2022-06-13 07:19:14.427132
# Unit test for function jsonify
def test_jsonify():
    j = jsonify(['foo', {'bar': ('baz', None, 1.0, 2)}])
    assert j == '["foo", {"bar": ["baz", null, 1.0, 2]}]'

# Generated at 2022-06-13 07:19:19.492833
# Unit test for function jsonify
def test_jsonify():
    assert "{}" == (jsonify(None))
    assert jsonify({}) == "{}"
    assert jsonify({'a':1}) == '{"a": 1}'
    assert jsonify({'a':1}, True) == '''{
    "a": 1
}'''

# Generated at 2022-06-13 07:19:24.778394
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'foo', 'b': 'bar'}) == '{"a": "foo", "b": "bar"}'
    assert jsonify({'a': 'foo', 'b': 'bar'}, True) == '{\n    "a": "foo", \n    "b": "bar"\n}'
    assert jsonify(None) == '{}'

# Generated at 2022-06-13 07:19:28.518464
# Unit test for function jsonify
def test_jsonify():
    result = {"msg":"#1 Succeeded"}
    assert jsonify(result, False) == "{\"msg\": \"#1 Succeeded\"}"
    assert jsonify(result, True) == "{\n    \"msg\": \"#1 Succeeded\"\n}"
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:35.188489
# Unit test for function jsonify
def test_jsonify():

    # Empty dict
    result = jsonify({})
    assert result == "{}"

    # Empty list
    result = jsonify([])
    assert result == "[]"

    # List of dicts
    result = jsonify([{'1':'2', '3':'4'}, {'5':'6', '7':'8'}])
    assert json.loads(result) == [{'1':'2', '3':'4'}, {'5':'6', '7':'8'}]

    # Dict of lists
    result = jsonify({'1':['2', '3'], '4':['5', '6']})
    assert json.loads(result) == {'1':['2', '3'], '4':['5', '6']}

    # Combination

# Generated at 2022-06-13 07:19:40.522577
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None, False) == "{}"
    assert jsonify("test", False) == "test"
    assert jsonify("test", True) == "test"

# Generated at 2022-06-13 07:19:44.393321
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 2}) == "{\"a\": 2}"
    assert jsonify([], True) == "[]"
    assert jsonify({"a": 2}, True) == "{\n    \"a\": 2\n}"


# Generated at 2022-06-13 07:19:47.609664
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == "{}"
    assert jsonify('''{ "foo": "bar" }''') == '''{
    "foo": "bar"
}'''
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:19:51.130509
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 42, "b": "foo"}) == '{"a": 42, "b": "foo"}'
    assert jsonify({"a": 42, "b": "foo"}, True) == '{\n    "a": 42,\n    "b": "foo"\n}'

# Generated at 2022-06-13 07:19:55.339300
# Unit test for function jsonify
def test_jsonify():
    test_result = { 'a': 'b' }
    json_str = jsonify(test_result)
    assert type(json_str) == str
    assert json_str == '''{
    "a": "b"
}'''

# Generated at 2022-06-13 07:20:05.870179
# Unit test for function jsonify
def test_jsonify():
    class testclass:
        def __init__(self):
            self.attr1 = 'value1'
            self.attr2 = ['value2', 'value3']

    myobj = testclass()
    assert jsonify(myobj) == '{"attr1": "value1", "attr2": ["value2", "value3"]}'
    assert jsonify(myobj, format=True) == '{\n    "attr1": "value1", \n    "attr2": [\n        "value2", \n        "value3"\n    ]\n}'


# Generated at 2022-06-13 07:20:12.764003
# Unit test for function jsonify
def test_jsonify():
    def _helper(result, format, output):
        assert jsonify(result, format) == output

    _helper(dict(a=1, b=2, c=3), False, '{"a": 1, "b": 2, "c": 3}')
    _helper(dict(a=1, b=2, c=3), True, '{\n    "a": 1, \n    "b": 2, \n    "c": 3\n}')

# Generated at 2022-06-13 07:20:19.494529
# Unit test for function jsonify
def test_jsonify():

    # Test jsonify with None
    assert jsonify(None) == "{}"

    # Test jsonify with an empty dictionary
    assert jsonify({}) == "{}"

    # Test jsonify with a dictionary
    assert jsonify({ "foo": "bar" }) == '{"foo": "bar"}'

    # Test jsonify with a dictionary and format
    assert jsonify({ "foo": "bar" }, format=True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:20:27.685265
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(changed=False, foo='bar', bam=['baz','qux'])) == '{"bam": ["baz", "qux"], "changed": false, "foo": "bar"}'
    assert jsonify(dict(changed=False, foo='bar', bam=['baz','qux']), True) == '''{
    "bam": [
        "baz",
        "qux"
    ],
    "changed": false,
    "foo": "bar"
}'''
    assert jsonify(True) == 'true'
    assert jsonify(False) == 'false'
    assert jsonify(None) == 'null'
    assert jsonify(0) == '0'
    assert jsonify(1) == '1'

# Generated at 2022-06-13 07:20:34.677236
# Unit test for function jsonify
def test_jsonify():
    ''' Ansible module to jsonify a python data structure '''
    test_result = {'a': 1, 'b': ['foo', 'bar']}
    assert jsonify(test_result, True) == '''{
    "a": 1,
    "b": [
        "foo",
        "bar"
    ]
}'''
    assert jsonify(test_result, False) == '{"a": 1, "b": ["foo", "bar"]}'



# Generated at 2022-06-13 07:20:36.896118
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None).strip() == '{}'

# Generated at 2022-06-13 07:20:47.279218
# Unit test for function jsonify
def test_jsonify():
    ''' test function jsonify '''
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'
    assert jsonify([1, 2, 3], format=True) == '[\n    1, \n    2, \n    3\n]'
    assert jsonify({'a': 1, 'b': [1, 2, {'c': u'\u1234'}]}) == '{"a": 1, "b": [1, 2, {"c": "\\u1234"}]}'

# Generated at 2022-06-13 07:20:50.354098
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo=42, bar='some text')) == '{"bar": "some text", "foo": 42}'

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:20:53.399977
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1}) == "{\"a\": 1}"
    assert jsonify({"a": 2}, True) == "{\n    \"a\": 2\n}"

# Generated at 2022-06-13 07:20:59.053109
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.unicode import to_unicode
    assert jsonify({}) == to_unicode('{}')
    assert jsonify({'a': '1'}) == to_unicode('{"a": "1"}')
    assert jsonify({'a': '1'}, format=True) == to_unicode('{\n    "a": "1"\n}')

# Generated at 2022-06-13 07:21:08.053936
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([]) == '[]'
    assert jsonify({}) == '{}'
    data = {'test':'pizza'}
    assert jsonify(data) == '{"test": "pizza"}'
    assert jsonify(data, True) == '{\n    "test": "pizza"\n}'

    try:
        jsonify(str(data))
        raise AssertionError
    except:
        pass

if __name__ == "__main__":
    import pytest
    pytest.main(['-x', 'ansible/utils/jsonify.py'])

# Generated at 2022-06-13 07:21:16.319697
# Unit test for function jsonify
def test_jsonify():
    # Nothing
    assert jsonify(None) == "{}"
    # True
    assert jsonify(True) == "true"
    # False
    assert jsonify(False) == "false"
    # Int
    assert jsonify(42) == "42"
    # Float
    assert jsonify(42.0) == "42.0"
    # String
    assert jsonify("string") == "\"string\""
    # Unicode
    assert jsonify(u"string") == "\"string\""
    # Dict
    assert jsonify({"key": "value"}) == '{"key": "value"}'
    # List
    assert jsonify(["string"]) == "[\"string\"]"
    # Tuple
    assert jsonify(("string",)) == "[\"string\"]"
    # Dict sorted
    assert jsonify

# Generated at 2022-06-13 07:21:20.045629
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify '''
    assert jsonify({"a": "b"}) == "{\"a\": \"b\"}"
    assert jsonify({"a": "b"}, format=True) == "{\n    \"a\": \"b\"\n}"
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:21:29.274514
# Unit test for function jsonify
def test_jsonify():
    assert "{}" == jsonify(None)
    assert "{}" == jsonify(False)
    assert "{}" == jsonify(0)
    assert "[]" == jsonify([])
    assert "[]" == jsonify([False])
    assert "[1,2,3]" == jsonify([1, 2, 3])
    assert '["A","B","C"]' == jsonify(["A", "B", "C"])
    assert '{"A":"B","C":"D","E":"F"}' == jsonify({"A":"B","C":"D","E":"F"})
    assert '{"A":"B","C":"D","E":"F"}' == jsonify({"C": "D", "E": "F", "A": "B"})

# Generated at 2022-06-13 07:21:36.630169
# Unit test for function jsonify
def test_jsonify():
    # Check that it works with a dict
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'

    # Check that it fails with an int
    try:
        jsonify(5)
    except:
        pass
    else:
        assert False, "jsonify should have failed with an int"

    # Check that it fails with a string
    try:
        jsonify("a")
    except:
        pass
    else:
        assert False, "jsonify should have failed with a string"

# Generated at 2022-06-13 07:21:45.836391
# Unit test for function jsonify
def test_jsonify():
    result = {
        'localhost'   : {
            'item1': True,
            'item2': False
        },
        'otherserver' : {
            'item1': False,
            'item2': False,
        }
    }
    results = jsonify(result)
    assert results == '{"localhost": {"item1": true, "item2": false}, "otherserver": {"item1": false, "item2": false}}'

    results = jsonify(result, format=True)
    assert results == '{\n    "localhost": {\n        "item1": true, \n        "item2": false\n    }, \n    "otherserver": {\n        "item1": false, \n        "item2": false\n    }\n}'

# Generated at 2022-06-13 07:21:54.467513
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.color import stringc

    datum = {
        'two' : 'foo',
        'five': 5,
        'one' : 'bar'
    }
    assert stringc(jsonify(datum, format=False)) == stringc("""{"five": 5, "one": "bar", "two": "foo"}""")
    assert stringc(jsonify(datum, format=True)) == stringc("""{
    "five": 5,
    "one": "bar",
    "two": "foo"
}""")

    assert stringc(jsonify(None, format=False)) == stringc("""{}""")
    assert stringc(jsonify(None, format=True)) == stringc("""{}""")

# Generated at 2022-06-13 07:21:59.198234
# Unit test for function jsonify
def test_jsonify():
    '''
    This test asserts the correct return value of the jsonify function
    '''

    assert jsonify({'foo': 'bar'}) == '{"foo": "bar"}'
    assert jsonify({'foo': 'bar'}, True) == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 07:22:02.371690
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1, 'b': 2}) == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 07:22:05.634903
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"name": "test"}) == '{"name": "test"}'
    assert jsonify({"name": "test"}, True) == '''{
    "name": "test"
}
'''

# Generated at 2022-06-13 07:22:10.974646
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({'a': 'b'}, True)
    assert result == '''{
    "a": "b"
}'''
    result = jsonify({'a': u'\u0080b'}, True)
    if not isinstance(result, str):
        result = result.encode('utf8')
    assert result == '''{
    "a": "\u0080b"
}''' or result == '''{
    "a": "\\u0080b"
}'''

# Generated at 2022-06-13 07:22:20.741534
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": ["b"]}) == '{"a": ["b"]}'
    assert jsonify("string") == '"string"'
    assert jsonify(True) == 'true'
    assert jsonify({'title': u'\u2603'}) == '{"title": "\\u2603"}'
    # format=True uses 4 spaces for indentation
    assert jsonify({'title': u'\u2603'}, format=True) == '{\n    "title": "\\u2603"\n}'

# Generated at 2022-06-13 07:22:29.057106
# Unit test for function jsonify
def test_jsonify():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.module_utils.basic import AnsibleModule

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])
    variable_manager.set_inventory(inventory)

    # play_source contains a single task

# Generated at 2022-06-13 07:22:39.906837
# Unit test for function jsonify
def test_jsonify():
    jsonify_test = {}
    jsonify_test['test'] = {1: {'test':{'test': 'string'}}}
    jsonify_test['test2'] = 'test'
    assert jsonify(jsonify_test) == '{"test": {"1": {"test": {"test": "string"}}}, "test2": "test"}'
    assert jsonify(jsonify_test, True) == '{\n    "test": {\n        "1": {\n            "test": {\n                "test": "string"\n            }\n        }\n    }, \n    "test2": "test"\n}\n'

if __name__ == "__main__":
    test_jsonify()

# Generated at 2022-06-13 07:22:50.277086
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils import jsonify

    assert jsonify({"a": "b"}) == '{"a": "b"}'
    assert jsonify({"a": "b"}, True) == '''{
    "a": "b"
}'''
    assert jsonify({"a": ["b", "c"]}, True) == '''{
    "a": [
        "b",
        "c"
    ]
}'''

# Generated at 2022-06-13 07:23:05.313867
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':1,'b':2}) == '{"a": 1, "b": 2}'
    assert jsonify({'a':1,'b':2},True) == '{\n    "a": 1, \n    "b": 2\n}'
    assert jsonify(None) == "{}"
    assert jsonify({}) == "{}"
    assert jsonify({'some_key': {'some_value': u'T\xc3\xa4nk\xc3\xa5\xc2\x80\xc2\x99s'}}) == '{"some_key": {"some_value": "T\\u00e4nk\\u00e5\\u20ac\\u2019s"}}'

# Generated at 2022-06-13 07:23:09.713959
# Unit test for function jsonify
def test_jsonify():
    result = { "test": ["one", "two"] }
    assert jsonify(result, False) == '{"test": ["one", "two"]}'
    assert jsonify(result, True) == '{\n    "test": [\n        "one", \n        "two"\n    ]\n}'
    assert jsonify(None) == '{}'
    assert jsonify(["testing", "newlines"]) == '["testing", "newlines"]'
    assert jsonify("testing unicode \u1234") == '"testing unicode \u1234"'

# Generated at 2022-06-13 07:23:17.945004
# Unit test for function jsonify
def test_jsonify():

    from ansible.utils.color import stringc
    from ansible.module_utils.basic import AnsibleModule

    ansible_module_args = {}
    module = AnsibleModule(argument_spec=ansible_module_args)

    results = None
    results = jsonify(results)
    assert results == "{}"


# Generated at 2022-06-13 07:23:21.911701
# Unit test for function jsonify
def test_jsonify():
    data = {"a": 1, "b": 2}
    assert jsonify(data, True) == '''{
    "a": 1,
    "b": 2
}'''
    assert jsonify(data, False) == '{"a":1,"b":2}'

    # Try non-ascii characters.
    data = {"a": "b\u200c"}
    assert jsonify(data, True) == '{"a":"b\\u200c"}'
    assert jsonify(data, False) == '{"a":"b\\u200c"}'

# Generated at 2022-06-13 07:23:30.133256
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify'''
    from ansible.utils.debug import verbose_debug
    from ansible.runner import Runner
    import sys
    from ansible.playbook import PlayBook
    from ansible.inventory import Inventory
    from ansible import callbacks
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
    inventory = Inventory(sys.argv[1])
    variable_manager = VariableManager(loader=playbook_loader, inventory=inventory)

# Generated at 2022-06-13 07:23:42.946334
# Unit test for function jsonify
def test_jsonify():
    data = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
    # jsonify turns unicode into bytes, so we need to encode it to compare.
    result = jsonify(data, False)
    assert result == '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    result = jsonify(data, True)
    assert result == '''{
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}'''

if __name__ == '__main__':
    test_jsonify()

# Generated at 2022-06-13 07:23:49.727538
# Unit test for function jsonify
def test_jsonify():
    def strip_newlines(a):
        return a.replace("\r","").replace("\n","")

    assert strip_newlines(jsonify(None)) == "{}"
    assert jsonify({"a":1}) == '{"a": 1}'
    assert strip_newlines(jsonify({"a":1}, True)) == '''{\
    "a": 1\
}'''

    # Test with non-ascii characters
    assert jsonify({"a":"\xc3\xbc"}) == u'{"a": "\xfc"}'
    assert strip_newlines(jsonify({"a":"\xc3\xbc"}, True)) == u'''{\
    "a": "\xfc"\
}'''

# Generated at 2022-06-13 07:23:55.886644
# Unit test for function jsonify
def test_jsonify():

    result = jsonify(dict(a=1, b=2, c=True))
    assert result == '{"a": 1, "b": 2, "c": true}'

    result = jsonify(dict(a=1, b=2, c=True), format=True)
    assert result == """{
    "a": 1,
    "b": 2,
    "c": true
}"""

# Generated at 2022-06-13 07:24:02.818736
# Unit test for function jsonify
def test_jsonify():
    result = {"unittest": True, "da": "rue", "list": [1,2,3]}
    # FIXME - add a test for indent with a non-ascii char
    assert jsonify(result) == json.dumps(result, sort_keys=True)
    assert jsonify(result, True) == json.dumps(result, sort_keys=True, indent=4)
    assert jsonify(result, False) == json.dumps(result, sort_keys=True)

# Generated at 2022-06-13 07:24:07.103482
# Unit test for function jsonify
def test_jsonify():
    result = dict(changed=True, rc=0, stdout="hello", stderr="")
    json_out = jsonify(result, format=False)
    # commented out because to_json() does not work in Python 3
    # assert jsonify(result, False) == result.to_json()
    assert jsonify(None, False) == "{}"
    assert jsonify(None, True) == "{}"


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(jsonify(dict(changed=True, rc=0, stdout="hello", stderr=""), format=False))
    print(jsonify(dict(changed=True, rc=0, stdout="hello", stderr=""), format=True))
    print(jsonify(None, format=False))


# Generated at 2022-06-13 07:24:20.532167
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify({'a': 'b'}, format=True) == '{\n    "a": "b"\n}'
    assert isinstance(jsonify({'a': 'b'}), basic.AnsibleModule) == False

# Generated at 2022-06-13 07:24:34.722011
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify '''

    assert jsonify("foo") == '"foo"'
    assert jsonify("foo\n") == '"foo\\n"'
    assert jsonify("foo\nbar") == '"foo\\nbar"'

    assert jsonify({"foo": "bar"}) == '{"foo": "bar"}'
    assert jsonify({"foo": "bar\n"}) == '{"foo": "bar\\n"}'
    assert jsonify({"foo": "bar\nbar"}) == '{"foo": "bar\\nbar"}'

    assert jsonify({"foo": "bar", "baz": "bam"}) == '{"baz": "bam", "foo": "bar"}'

# Generated at 2022-06-13 07:24:39.613733
# Unit test for function jsonify
def test_jsonify():

    assert(jsonify(None)    == "{}")
    assert(jsonify({})      == "{}")
    assert(jsonify(1)       == "1")
    assert(jsonify("11111") == "\"11111\"")
    assert(jsonify([])      == "[]")
    assert(jsonify(["11111", 2, ("a", "b"), { "k": "v" }]) == '[\n    "11111",\n    2,\n    [\n        "a",\n        "b"\n    ],\n    {\n        "k": "v"\n    }\n]')

# Generated at 2022-06-13 07:24:46.615166
# Unit test for function jsonify
def test_jsonify():
    stdout = {'stdout': u'\nabc'}
    assert '"stdout": "\\nabc"\n' == jsonify(stdout, False)
    assert '"stdout": "\\nabc"\n' == jsonify(stdout, True)
    assert '''{
    "stdout": "\\nabc"
}''' == jsonify(stdout, True)
    print('test_jsonify: all tests passed')


# Generated at 2022-06-13 07:24:54.114877
# Unit test for function jsonify
def test_jsonify():
    from ansible.compat.tests import unittest

    class TestJsonify(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        # Test with different data types
        def test_jsonify(self):
            results = jsonify(None)
            self.assertEqual(results, "{}")

            results = jsonify({"test":"test"})
            self.assertEqual(results, '{\n    "test": "test"\n}')

            results = jsonify(dict(test={"test":"test"}))
            self.assertEqual(results, '{\n    "test": {\n        "test": "test"\n    }\n}')

            results = jsonify(["test"])

# Generated at 2022-06-13 07:25:03.005887
# Unit test for function jsonify
def test_jsonify():
    def test(input_string, expected_result, expected_format_result, test_name):
        result = jsonify(input_string)
        assert result == expected_result, test_name
        result = jsonify(input_string, True)
        assert result == expected_format_result, test_name

    test(None, "{}", "{\n    \n}", "test_jsonify: null")
    test(True, "true", "true", "test_jsonify: boolean")
    test(True, "true", "true", "test_jsonify: boolean")
    test(False, "false", "false", "test_jsonify: boolean")
    test(1, "1", "1", "test_jsonify: integer")

# Generated at 2022-06-13 07:25:07.399079
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify: return formatted json output
    '''
    data = {"a": "b"}

    # jsonify should return valid json with indent of 4
    assert jsonify(data, True) == '''{
    "a": "b"
}'''
    assert jsonify(data, False) == '{"a": "b"}'

# Generated at 2022-06-13 07:25:15.663303
# Unit test for function jsonify
def test_jsonify():
    data = {'foo': 'bar'}
    ret = jsonify(data)
    assert ret == '{"foo": "bar"}'

    ret = jsonify(data, True)
    assert ret == '{\n    "foo": "bar"\n}'

    ret = jsonify(data, False)
    assert ret == '{"foo": "bar"}'

    data = '{"foo": "bar"}'
    ret = jsonify(data)
    assert ret == '"{\\"foo\\": \\"bar\\"}"'

    ret = jsonify(data, True)
    assert ret == '"{\n    \\"foo\\": \\"bar\\"\n}"'

    ret = jsonify(data, False)
    assert ret == '"{\\"foo\\": \\"bar\\"}"'

# Generated at 2022-06-13 07:25:22.121229
# Unit test for function jsonify
def test_jsonify():
    ''' jsonify should return a valid JSON string '''
    # result is a dict
    result = dict(changed=False, rc=0, stdout='{"test": "success"}')
    json_result = jsonify(result)
    assert json_result == '{"changed": false, "rc": 0, "stdout": "{\u0022test\u0022: \u0022success\u0022}"}'
    # result is a list
    result = dict(changed=False, rc=0, stdout='["item1", "item2"]')
    json_result = jsonify(result)
    assert json_result == '{"changed": false, "rc": 0, "stdout": "[\u0022item1\u0022, \u0022item2\u0022]"}'
    # result is neither a list

# Generated at 2022-06-13 07:25:32.271444
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils.jsonify import jsonify
    from ansible.compat.tests import unittest

    class JsonifyTests(unittest.TestCase):
        def test_bool_true(self):
            self.assertEqual(jsonify(True), "true")
        def test_bool_false(self):
            self.assertEqual(jsonify(False), "false")
        def test_none(self):
            self.assertEqual(jsonify(None), "{}")
        def test_generator(self):
            self.assertEqual(jsonify((x for x in range(2))), "[0,1]")
        def test_list(self):
            self.assertEqual(jsonify(["a", "b"]), '["a","b"]')

# Generated at 2022-06-13 07:25:54.494025
# Unit test for function jsonify
def test_jsonify():
    ''' Unit test for function jsonify '''
    assert jsonify({}) == "{}"
    assert jsonify({'a':1}) == '{"a": 1}'

# Generated at 2022-06-13 07:26:00.198480
# Unit test for function jsonify
def test_jsonify():
    data = {"a": 1, "b": 2, "c": 3}
    formatted = jsonify(data, True)
    assert formatted == '''{
    "a": 1,
    "b": 2,
    "c": 3
}'''

    not_formatted = jsonify(data)
    assert not_formatted == '{"a": 1, "b": 2, "c": 3}'

# Generated at 2022-06-13 07:26:02.265713
# Unit test for function jsonify
def test_jsonify():
    # test None input
    assert jsonify(None) == "{}"


# Generated at 2022-06-13 07:26:07.864720
# Unit test for function jsonify
def test_jsonify():
    '''Make sure jsonify is working'''

    import ansible.utils.jsonify as j

    assert isinstance(j.jsonify(None), str)
    assert isinstance(j.jsonify({'a': 'b'}), str)
    assert isinstance(j.jsonify({'a': 'b'}, format=True), str)

# Generated at 2022-06-13 07:26:10.331207
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1, b=2, c=3)) == '{"a": 1, "b": 2, "c": 3}'

# Generated at 2022-06-13 07:26:13.344663
# Unit test for function jsonify
def test_jsonify():
    test_result = {'a': 1, 'b': 2}
    assert jsonify(test_result) == "{\"a\": 1, \"b\": 2}"
    assert jsonify(test_result, True) == "{\n    \"a\": 1,\n    \"b\": 2\n}"
    assert jsonify(None) == "{}"

# Generated at 2022-06-13 07:26:17.462101
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'spam': 'eggs'}, format=False) == '{\"spam\": \"eggs\"}'
    assert jsonify({'spam': 'eggs'}, format=True) == '{\n    \"spam\": \"eggs\"\n}'

# Generated at 2022-06-13 07:26:24.026526
# Unit test for function jsonify
def test_jsonify():
    # simple test
    result = {'a':1, 'b':2, 'c':3 }
    assert jsonify(result), '{"a": 1, "b": 2, "c": 3}'

    # unicode test
    result = {'a':1, 'b':2, 'c':u'\u03a3' }
    assert jsonify(result), '{"a": 1, "b": 2, "c": "\u03a3"}'

# Generated at 2022-06-13 07:26:32.649368
# Unit test for function jsonify
def test_jsonify():
    test_data = {'a': 2, 'b': {'a': 1, 'b': 2, 'c': [1, 2, 3]}, 'c': [1, 2, 3]}

    test_result = jsonify(test_data)
    assert test_result == '{"a": 2, "b": {"a": 1, "b": 2, "c": [1, 2, 3]}, "c": [1, 2, 3]}'
    test_result = jsonify(test_data, True)

# Generated at 2022-06-13 07:26:35.700563
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == '{}'
    assert jsonify({'a': 1}) == '{"a": 1}'
    assert jsonify({'a': 'b'}) == '{"a": "b"}'

# Generated at 2022-06-13 07:27:24.828513
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(None) == "{}"
    assert jsonify([]) == "[]"
    assert jsonify(dict()) == "{}"
    assert jsonify([1,2,3]) == "[1, 2, 3]"
    assert jsonify(dict(a=1,b=2,c=3)) == "{\"a\": 1, \"b\": 2, \"c\": 3}"
    assert jsonify(dict(a=[1,2,3])) == "{\"a\": [1, 2, 3]}"
    assert jsonify(dict(a=1,b=dict(c=2,d=3))) == "{\"a\": 1, \"b\": {\"c\": 2, \"d\": 3}}"
    assert jsonify(dict(a=1,b=[2,3])) == "{\"a\": 1, \"b\": [2, 3]}"

# Generated at 2022-06-13 07:27:29.239587
# Unit test for function jsonify
def test_jsonify():

    # Ensure results are JSON formatted
    assert jsonify({'a':'test'}, True) == '{\n    "a": "test"\n}'

    # Ensure that None results are handled gracefuly
    assert jsonify(None) == '{}'