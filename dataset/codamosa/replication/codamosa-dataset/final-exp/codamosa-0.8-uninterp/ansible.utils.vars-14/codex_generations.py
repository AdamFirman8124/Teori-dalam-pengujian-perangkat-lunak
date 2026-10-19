

# Generated at 2022-06-13 16:57:36.915056
# Unit test for function isidentifier
def test_isidentifier():
    assert isidentifier('a')
    assert isidentifier('_a')
    assert isidentifier('a_')
    assert isidentifier('a_b')
    assert isidentifier('_a_b')
    assert isidentifier('abc')
    assert isidentifier('abc123')
    assert isidentifier('abc_123')
    assert isidentifier('abc_123_def')
    assert isidentifier('abc_123_def_456')

    # Contains non-ascii characters
    assert not isidentifier('\u00e9')

    # Contains leading underscore
    assert not isidentifier('_')
    assert not isidentifier('_abc')
    assert not isidentifier('__a')
    assert not isidentifier('__a__')
    assert not isidentifier('__abc__')

    # Contains

# Generated at 2022-06-13 16:57:46.539840
# Unit test for function merge_hash
def test_merge_hash():
    def get_dict():
        def get_value(k, v):
            # we add a random value to the key to make sure
            # the order doesn't affect the result
            return "dict(%d, %s)" % (random.randint(0, 100), v)
        return {'key_%d' % x: get_value(x, 'dict(%d)' % x) for x in range(100)}

    def get_list(list_merge):
        def get_value(k):
            # we add a random value to the key to make sure
            # the order doesn't affect the result
            return "list(%d)" % random.randint(0, 100)
        A = ['a', 'b', 'c', 'd', 'e']

# Generated at 2022-06-13 16:57:54.980263
# Unit test for function combine_vars
def test_combine_vars():
    a = {'a': '1', 'b': {'b1': '1', 'b2': '2'}, 'c': ['a', 'b', 'c'], 'd': {'d1': {'d11': '1', 'd12': '2'}}}
    b = {'a': '1', 'b': {'b2': '2', 'b3': '3'}, 'c': ['d', 'e', 'f'], 'd': {'d1': {'d11': '1', 'd13': '3'}}}


# Generated at 2022-06-13 16:58:08.089986
# Unit test for function load_extra_vars
def test_load_extra_vars():
    import json
    some_var = "some_string"
    some_dict = {"key1": "value1", "key2": 2, "key3": {"k1": "v1", "k2": "v2"}}

    with open('/tmp/test_extra_vars.json', 'w') as f:
        json.dump(some_dict, f)

    for extra_vars_opt in [to_text(some_var), to_text('@/tmp/test_extra_vars.json')]:
        data = load_extra_vars(extra_vars_opt)
        assert isinstance(data, MutableMapping)
        if extra_vars_opt.startswith(u"@"):
            assert data.get('key1') == 'value1'

# Generated at 2022-06-13 16:58:22.114522
# Unit test for function merge_hash
def test_merge_hash():
    # create some test data
    d1 = {'a': {'x': 1}, 'b': 2}
    d2 = {'a': {'y': 3}, 'b': {'k': 4}}

    d3 = merge_hash(d1, d2)
    assert d1 == {'a': {'x': 1}, 'b': 2}
    assert d2 == {'a': {'y': 3}, 'b': {'k': 4}}
    assert d3 == {'a': {'y': 3, 'x': 1}, 'b': {'k': 4}}

    d1 = {'a': {'x': 1}, 'b': 2}
    d2 = {'a': {'y': 3}, 'b': {'k': 4}}


# Generated at 2022-06-13 16:58:31.834834
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    assert isinstance('a', str)
    assert isinstance('a', string_types)

    class mock_loader():
        def load_from_file(self, a):
            return {'a': {'b': 'c'}}

        def load(self, a):
            return {'a': {'b': 'c'}}

    class mock_cliargs():
        def __init__(self, a):
            self.extra_vars = a

    class mock_CLIARGS():
        @property
        def get(self):
            return self.b

        def __init__(self):
            self.b = None

    context.CLIARGS = mock_CLIARGS()

# Generated at 2022-06-13 16:58:42.542706
# Unit test for function merge_hash
def test_merge_hash():
    def dict2str(d):
        return '\n'.join(sorted(["%s: %s" % (k, d[k]) for k in sorted(d.keys())]))

    class TestException(Exception):
        pass

    def test(name, desc, deep, merge, lmerge, a, b, exp_result):
        result = merge_hash(a, b, deep, lmerge)
        if result != exp_result:
            raise TestException("%s\nMerge %s\nWith %s\nExpected:\n%s\nGot:\n%s" % (name, dict2str(a), dict2str(b), dict2str(exp_result), dict2str(result)))

    a = {'A': 1, 'B': 2, 'C': {'D': 4}}


# Generated at 2022-06-13 16:58:53.081800
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()

    inv = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager.set_inventory(inv)

    vars = []

    vars.append('@tests/vars_file.yml')
    vars.append('@tests/vars_file.json')
    vars.append('@tests/vars_file.json5')
    vars.append('key1=value1 key2=value2')
    vars.append('key3=value3 key4=value4')

    options_vars = load_extra_vars(loader)

   

# Generated at 2022-06-13 16:59:04.110552
# Unit test for function load_extra_vars
def test_load_extra_vars():
    """
    This function tests load_extra_vars with valid and
    invalid arguments
    """

    from ansible.plugins.loader import add_all_plugin_dirs, plugins
    add_all_plugin_dirs()

    # Invalid test cases
    extra_vars = "@#@&123=="
    try:
        load_extra_vars(plugins.vars_loader)
        assert False, 'test should have failed'
    except Exception:
        pass

    # valid test cases
    extra_vars = {'new_var': 'test_var'}
    extra_vars = load_extra_vars(plugins.vars_loader)
    assert isinstance(extra_vars, dict), 'test should have passed'



# Generated at 2022-06-13 16:59:12.769035
# Unit test for function load_extra_vars
def test_load_extra_vars():

    class LoaderTest(object):
        def __init__(self):
            self.files = {
                'keyvalue.txt': "1=2\n3=4",
                'dict.txt': "{'a': 'b'}",
                'json.json': "{\"name\":\"john\"}",
                'yaml.yml': "name: john",
                'yaml2.yml': "name: '{{name}}'",
                'yaml3.yml': "name: \"{{name}}\""
            }
            self.cur_file = None

        def load_from_file(self, file_name):
            if file_name not in self.files:
                raise Exception("File not found")
            self.cur_file = file_name
            data = self.files[file_name]
           

# Generated at 2022-06-13 16:59:30.164908
# Unit test for function combine_vars
def test_combine_vars():
    """
    Test function when used with a non-recursive merge and a recursive merge.
    Note: no assert is used in this test case so that we can get a complete traceback
    if an error occurs.
    """
    import inspect
    import pprint
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.vars import combine_vars

    def merge_hash(x, y, recursive=True):
        """
        Return a new dictionary result of the merges of y into x,
        so that keys from y take precedence over keys from x.
        (x and y aren't modified)
        """
        # verify x & y are dicts
        _validate_mutable_mappings(x, y)

        # to speed things up: if x is empty or equal to y,

# Generated at 2022-06-13 16:59:42.885212
# Unit test for function merge_hash
def test_merge_hash():
    # replace mode
    assert merge_hash({}, {'a': 1}, recursive=False) == {'a': 1}
    assert merge_hash({'a': 1}, {'a': 2}, recursive=False) == {'a': 2}
    assert merge_hash({'a': 1, 'b': 2}, {'c': 3}, recursive=False) == {'a': 1, 'b': 2, 'c': 3}
    assert merge_hash({'a': 1}, {'a': [1, 2, 3]}, recursive=False) == {'a': [1, 2, 3]}

    # merge mode
    assert merge_hash({}, {'a': 1}) == {'a': 1}
    assert merge_hash({'a': 1}, {'a': 2}) == {'a': 2}
    assert merge_hash

# Generated at 2022-06-13 16:59:47.112618
# Unit test for function isidentifier
def test_isidentifier():
    """
    Should return True for valid identifiers and False for anything else
    """

    valid_identifiers = ['_asdf', 'asdf', 'foo', 'foo_bar']
    invalid_identifiers = ['', 'foo bar', 'foo-bar', 'foo.bar', 'foo*bar',
                           '1foo', 'foo!', 'foo%', 'foo@', 'foo^', 'foo&',
                           'foo(', 'foo)', 'foo+', 'foo=', 'foo?', 'foo/',
                           'None', 'True', 'False', '0x50']

    # Python 2 specific
    if not PY3:
        valid_identifiers.extend(['\xac', '\u03D2'])
        invalid_identifiers.append('\u03D2\xac')


# Generated at 2022-06-13 16:59:58.971719
# Unit test for function combine_vars
def test_combine_vars():
    assert combine_vars({}, {}) == {} # both empty
    assert combine_vars({'a': 1}, {}) == {'a': 1} # one empty
    assert combine_vars({'a': 1}, {'a': 2}) == {'a': 2} # replace => replace
    assert combine_vars({'a': 1}, {'a': 2}, merge=False) == {'a': 2} # replace => replace
    assert combine_vars({'a': 1}, {'a': 2}, merge=True) == {'a': 2} # merge => replace

    # merge => merge
    assert combine_vars({'a': 1}, {'a': 2}, merge=None) == {'a': 2}

# Generated at 2022-06-13 17:00:06.651552
# Unit test for function merge_hash
def test_merge_hash():
    x = {'a': '1', 'b': {'b_1': '1', 'b_2': '2', 'b_3': '3'}, 'c': {'c_1': {'c_1_1': '1'}, 'c_2': '2'}}
    y = {'a': '2', 'b': {'b_1': '2', 'b_2': '2', 'b_4': '4'}, 'c': {'c_1': {'c_1_2': '2'}, 'c_3': '3'}}

    # recursive merge test

# Generated at 2022-06-13 17:00:18.275975
# Unit test for function merge_hash
def test_merge_hash():
    d1 = {'a1': 'b1', 'a2': 'b2', 'a3': 'b3'}
    d2 = {'a1': 'b1', 'a2': 'b2', 'a3': 'b3'}
    # should return a copy of d2
    assert merge_hash(d1, d2) == d2

    d3 = {'a1': 'b1', 'a2': 'b2', 'a3': 'b4', 'a4': 'b4'}
    d4 = {'a1': 'b1', 'a2': 'b2', 'a3': 'b3'}
    # should return {'a1': 'b1', 'a2': 'b2', 'a3': 'b4', 'a4': 'b4'}

# Generated at 2022-06-13 17:00:27.650218
# Unit test for function merge_hash
def test_merge_hash():
    x = {
        "a": {
            "a": 1,
            "b": 2
        },
        "b": [1, 2, 3],
        "c": [4, 5, 6],
        "d": [7, 8, 9]
    }
    y = {
        "a": {
            "c": 3,
            "b": 4
        },
        "b": [11, 12, 13],
        "c": [14],
        "e": [15]
    }
    z = merge_hash(x, y, False)
    assert z["a"] == y["a"]
    assert z["b"] == y["b"]
    assert z["c"] == y["c"]
    assert z["d"] == x["d"]
    assert "e" in z
    z = merge_

# Generated at 2022-06-13 17:00:31.239923
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # what this should do is check that load_extra_vars
    # correctly loads a file or a string of json/yaml
    # and does the correct thing based on whether the string
    # or file is a dictionary or a list/string/whatever else
    pass



# Generated at 2022-06-13 17:00:37.007808
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None)
    my_list = ['extra_vars=@sample_vars_file', 'extra_vars={test: 1}', 'extra_vars=key=value']
    my_dict = load_extra_vars(loader)
    assert my_dict.get('test') == 1
    assert my_dict.get('key') == 'value'
    assert my_dict.get('port') == 22

# Generated at 2022-06-13 17:00:49.784190
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    # Test for the file that doesn't exist
    try:
        load_extra_vars(loader)
    except AnsibleError as e:
        assert e.args[0] == "The file specified as extra_vars does not exist.\n{0}".format("extra_vars value: 'file_not_exists'")

    # Test for the dictionary
    try:
        load_extra_vars(loader)
    except AnsibleError as e:
        assert e.args[0] == "The file specified as extra_vars does not exist.\n{0}".format("extra_vars value: 'file_not_exists'")

    # Test for the value as '@file_not_exists'


# Generated at 2022-06-13 17:01:06.320555
# Unit test for function combine_vars
def test_combine_vars():
    '''
    Test combine_vars function
    '''

    from ansible.compat.tests import unittest

    class TestCombineVars(unittest.TestCase):
        '''
        Test combine_vars function
        '''

        def test_combine_vars_raises(self):
            '''
            Parameters must be dictionaries
            '''
            with self.assertRaises(AnsibleError):
                combine_vars([], 1)

            with self.assertRaises(AnsibleError):
                combine_vars(1, [])

            with self.assertRaises(AnsibleError):
                combine_vars([], {})

            with self.assertRaises(AnsibleError):
                combine_vars({}, [])


# Generated at 2022-06-13 17:01:11.228834
# Unit test for function load_extra_vars
def test_load_extra_vars():
    loader, template_ds = mock_loader()
    opt = '[{"foo": "bar"}]'
    data = loader.load(opt)
    assert not isinstance(data, MutableSequence)
    assert isinstance(data, MutableMapping)



# Generated at 2022-06-13 17:01:22.471785
# Unit test for function merge_hash

# Generated at 2022-06-13 17:01:30.068072
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Create a test class that can mock AnsibleLoader
    class MockAnsibleLoader:
        def __init__(self, *args, **kwargs):
            pass

        def load_from_file(self, filename):
            if filename == "f1":
                return dict(key1="value1")
            elif filename == "f2":
                return dict(key2="value2")
            else:
                return dict()

        def load(self, filename):
            if filename == "{'key3': 'value3'}":
                return dict(key3="value3")
            else:
                return dict()

    # Create a test class that can mock CLIARGS

# Generated at 2022-06-13 17:01:41.383780
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # pylint: disable=unused-variable
    class MockConfig:
        ''' mock object for config file '''
        class _const:
            ''' mock for CONSTANTS '''
            DEFAULT_HASH_BEHAVIOUR = "replace"

    # pylint: disable=unused-variable,too-many-branches,too-many-statements,too-many-nested-blocks
    class MockLoader:
        ''' mock loader object '''
        def __init__(self, read_data=None):
            self.read_data = read_data
            self.read_count = 0

        def load(self, stream, file_name=''):
            ''' read data from file or stream '''

# Generated at 2022-06-13 17:01:50.901583
# Unit test for function combine_vars
def test_combine_vars():

    # define a dict that will be used as a "default" dict
    x = {
        'a': 'x.a',
        'b': {
            'b1': 'x.b.b1',
            'b2': 'x.b.b2',
            'b3': [
                'x.b.b3.0',
                'x.b.b3.1',
            ],
        },
        'c': 'x.c',
        'd': [
            'x.d.0',
            'x.d.1',
            'x.d.2',
        ],
    }

    # define a dict that will be used to "patch" the "default" dict

# Generated at 2022-06-13 17:02:01.236386
# Unit test for function load_extra_vars
def test_load_extra_vars():
    loader = DictDataLoader({})

    def test_loader(v, f):
        return load_extra_vars(DictDataLoader({'a.yml': f}))

    assert test_loader('a.yml: {"foo":"bar"}', {'foo': 'bar'}) == {'foo': 'bar'}
    assert test_loader('@a.yml', {'foo': 'bar'}) == {'foo': 'bar'}
    assert test_loader('a.yml', {'foo': 'bar'}) == {'foo': 'bar'}
    assert test_loader('a=b c=d', {'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-13 17:02:09.091694
# Unit test for function load_extra_vars
def test_load_extra_vars():
    context.CLIARGS = {'loader': None}
    context.CLIARGS['extra_vars'] = ['@vars.yaml', '@vars.yaml']
    # Test True/False are converted to boolean True/False
    extra_vars = load_extra_vars(context.CLIARGS['loader'])
    assert isinstance(extra_vars['test'], bool)


# Generated at 2022-06-13 17:02:17.105673
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader

    class CallbackModule(object):
        def __init__(self):
            self.extra_vars = None

        def v2_playbook_on_task_start(self, task, is_conditional):
            self.extra_vars = task.extra_vars

    # Create a fake playbook object to pass to load_extra_vars
    # The object needs to have a loader attribute or things explode
    class FakePlaybook(object):
        def __init__(self):
            self.loader = DataLoader()

    loader = DataLoader()

    # Initialize the callback module and fake playbook
    callback_module = CallbackModule()
    fake_playbook = FakePlaybook()
    test_vars

# Generated at 2022-06-13 17:02:23.125768
# Unit test for function combine_vars
def test_combine_vars():
    yaml_loader = None
    def test(x, y, merge, result):
        _combine = combine_vars(x, y, merge)
        _merge   = merge_hash(x, y)

        _x = dumps(x, sort_keys=True)
        _y = dumps(y, sort_keys=True)
        _r = dumps(result, sort_keys=True)
        _combine = dumps(_combine, sort_keys=True)
        _merge   = dumps(_merge, sort_keys=True)

        _x = to_text(_x)
        _y = to_text(_y)
        _r = to_text(_r)
        _combine = to_text(_combine)
        _merge   = to_text(_merge)


# Generated at 2022-06-13 17:02:40.200484
# Unit test for function merge_hash
def test_merge_hash():
    a = dict(one=1, two=2, three=3, four=dict(a=1, b=2, c=3))
    b = dict(two=22, three=33, four=dict(b=22, c=33, d=4))
    c = dict(four=dict(e=5))

    print("a:", a)
    print("b:", b)
    print("c:", c)

    print("")
    print("a + b:", merge_hash(a, b))
    print("a + c:", merge_hash(a, c))

    print("")
    print("a + b + c:", merge_hash(merge_hash(a, b), c))

# Generated at 2022-06-13 17:02:49.578413
# Unit test for function merge_hash
def test_merge_hash():
    """
    This test suite doesn't validate "list_merge" use cases
    see test_merge_hash_list_merge.py for them
    """

    def assertEqual(obj, obj_ref, message=None):
        if obj == obj_ref:
            return
        if message is None:
            message = "%s is not %s" % (obj, obj_ref)
        raise AssertionError(message)

    def assertRaises(exc, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exc:
            return
        raise AssertionError("didn't raise %s on function called %s(%s, %s)" % (exc, func.__name__, args, kwargs))


# Generated at 2022-06-13 17:03:01.539706
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    vars1 = {'foo': 'bar'}
    vars2 = {'one': 1, 'two': 2}
    vars3 = {'red': 'blue', 'green': 'yellow'}
    vars4 = {'a': 1, 'b': 2, 'c': {'foo': 'bar'}}
    # DataLoader calculates checksum on string representation of the object,
    # so convert to text if necessary.
    v1 = to_text(vars1)
    v2 = to_text(vars2)
    v3 = to_text(vars3)
    v4 = to_text(vars4)

    # Load valid variables and check result

# Generated at 2022-06-13 17:03:11.054184
# Unit test for function load_extra_vars
def test_load_extra_vars():
    import os
    import json
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    loader = AnsibleLoader(None, vault_password_file=None)

    # Test file argument
    yaml_result = {'foo': 'bar'}
    json_result = {'foo': 'bar'}
    assert load_extra_vars(loader) == {}
    assert load_extra_vars(loader) == {}
    assert load_extra_vars(loader) == {}
    assert load_extra_vars(loader) == {}
   

# Generated at 2022-06-13 17:03:23.300048
# Unit test for function merge_hash
def test_merge_hash():
    assert merge_hash({}, {}) == {}
    assert merge_hash({}, {'a': 1}) == {'a': 1}
    assert merge_hash({'a': 1}, {}) == {'a': 1}
    assert merge_hash({'a': 1}, {'a': 2}, False) == {'a': 2}
    assert merge_hash({'a': 1}, {'a': 2}, True) == {'a': 2}

    assert merge_hash({'a': {'b': 1}}, {'a': {'c': 2}}) == {'a': {'b': 1, 'c': 2}}
    assert merge_hash({'a': {'b': 1}}, {'a': {'c': 2}}, False) == {'a': {'c': 2}}

# Generated at 2022-06-13 17:03:34.566205
# Unit test for function merge_hash
def test_merge_hash():
    from ansible.module_utils import six
    data1 = {
        'foo': 5,
        'bar': {
            'baz': 3,
            'qux': 4,
            },
        'list': [ 'a', 'b', 'c' ],
        'list2': [ 'd', 'e', 'f' ],
        }
    data2 = {
        'foo': 7,
        'bar': {
            'qux': 3,
            'zoo': 4,
            },
        'list': [ 'g', 'h' ],
        'list2': [ 'i', 'j' ],
        'dict': {
            'k': 'l',
            'm': 'n',
            },
        }

# Generated at 2022-06-13 17:03:37.151508
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    result = load_extra_vars(loader)
    assert result == {}

# Generated at 2022-06-13 17:03:45.518143
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 17:03:55.044677
# Unit test for function isidentifier
def test_isidentifier():
    import sys

    for x in ['', '1', '1a', 'a 1', 'a!', 'if', 'pass', '_a', '_a1', '_a1b', 'a_b', 'a1b', 'a1_b', 'a1_b1',
              u'a', u'\u00DF']:
        if PY3:
            if isidentifier(x):
                print("%r is a valid ident on Python %s but shouldn't be" % (x, sys.version_info[0]))
        else:
            if not isidentifier(x):
                print("%r is not a valid ident on Python %s but should be" % (x, sys.version_info[0]))


# Generated at 2022-06-13 17:04:05.168097
# Unit test for function merge_hash
def test_merge_hash():
    x = dict(
        # keys
        key1 = "val1",
        key2 = "val2",
        key3 = "val3",
        key4 = "val4",
        key5 = "val5",
        key6 = "val6",
        key7 = "val7"
    )

    y = dict(
        # keys
        key3 = "VAL3",
        key4 = "VAL4"
    )

    z = dict(
        # keys
        key7 = "val7",
        key5 = "val5",
        key6 = "val6"
    )

    # the keys to test
    test_keys = ("key1", "key2", "key3", "key4", "key5", "key6", "key7")

    # the expected value of keys when "merged

# Generated at 2022-06-13 17:04:22.040564
# Unit test for function load_extra_vars

# Generated at 2022-06-13 17:04:33.528853
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class OptionsModule:
        def __init__(self):
            self.extra_vars = []

    import os
    import tempfile

    options = OptionsModule()
    options.extra_vars = []
    context.CLIARGS = options
    loader = AnsibleLoader(None, None, None)

    # Test load_extra_vars without extra vars
    extra_vars = load_extra_vars(loader)
    assert len(extra_vars) == 0

    # Test load_extra_vars parsing extra_vars containing strings
    test_vars = "{\"key\":\"value\"}"

# Generated at 2022-06-13 17:04:46.461320
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Make sure any environment variables don't interfere with the test
    for i in ('ANSIBLE_EXTRA_VARS', 'EXTRA_VARS', 'ANSIBLE_DEBUG'):
        if i in os.environ:
            del os.environ[i]

    def setup_args(extra_vars):
        if isinstance(extra_vars, dict):
            extra_vars = [extra_vars]
        else:
            for i in extra_vars:
                if isinstance(i, dict):
                    i.update({'ANSIBLE_CONFIG': './ansible/cfg/unittests/ansible.cfg'})
                else:
                    extra_vars = [extra_vars]

    def raise_unparsed(unparsed):
        if unparsed:
            raise Assertion

# Generated at 2022-06-13 17:04:54.831516
# Unit test for function load_extra_vars
def test_load_extra_vars():
    test_loader = DictDataLoader(dict())
    res = load_extra_vars(test_loader)
    assert res is not None
    assert len(res) == 0

    test_loader = DictDataLoader({'host_vars/hostname.yml': """
ip: "{{ hostvars['hostname']['ansible_default_ipv4']['address'] }}"
"""})
    # Test empty extra_vars
    res = load_extra_vars(test_loader)
    assert res is not None
    assert len(res) == 0

    # Test default behavior
    context.CLIARGS = {'extra_vars': [u'@path/to/file.yml']}
    res = load_extra_vars(test_loader)
    assert res is not None


# Generated at 2022-06-13 17:05:07.953073
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.clean import combine_vars, isidentifier

    assert load_extra_vars(DataLoader()) == {}

    # Test JSON format
    extra_vars1 = {'poll_interval': 0.5, 'log_path': '/var/log/foo.log', 'log_level': 'ERROR'}
    assert load_extra_vars(DataLoader(extra_vars1)) == extra_vars1

    # Test non-JSON format
    extra_vars2 = {'poll_interval': 0.5, 'log_path': '/var/log/foo.log', 'log_level': 'ERROR'}
    assert load_extra_vars(DataLoader(extra_vars2)) == extra_vars2



# Generated at 2022-06-13 17:05:19.438104
# Unit test for function merge_hash
def test_merge_hash():
    from ansible.module_utils.six import PY3

    def assert_equal(x, y, msg=None):
        if not msg:
            msg = "x:%s, y:%s" % (x, y)
        assert x == y, msg

    def assert_not_equal(x, y, msg=None):
        if not msg:
            msg = "x:%s, y:%s" % (x, y)
        assert x != y, msg

    def assert_identical(x, y, msg=None):
        if not msg:
            msg = "x:%s, y:%s" % (x, y)
        assert x is y, msg


# Generated at 2022-06-13 17:05:31.133999
# Unit test for function load_extra_vars
def test_load_extra_vars():
    import ansible.constants as C
    import tempfile

    try:
        # Imports to avoid cross-dependency and allow for testing on systems
        # that don't have yaml/json available
        from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
        from ansible.parsing.yaml.loader import AnsibleLoader
    except ImportError:
        raise ImportError("Unable to import modules needed for testing load_extra_vars function")


# Generated at 2022-06-13 17:05:43.653128
# Unit test for function merge_hash
def test_merge_hash():
    dict1 = dict(ansible_facts=dict(pkg_mgr='dnf'),
                 my_host=dict(name='foo', ip='192.168.1.1'))
    dict2 = dict(ansible_facts=dict(pkg_mgr='zypper'),
                 my_host=dict(name='bar', ip='192.168.1.2'))

    dict_merged = merge_hash(dict1, dict2)
    assert dict_merged == dict(ansible_facts=dict(pkg_mgr='zypper'),
                               my_host=dict(name='bar', ip='192.168.1.2'))

    dict1 = dict(a=dict(b='c', d='e'))
    dict2 = dict(a='b')


# Generated at 2022-06-13 17:05:49.831537
# Unit test for function isidentifier
def test_isidentifier():
    from nose.tools import assert_false, assert_true

    assert_true(isidentifier("foo"))
    assert_true(isidentifier("_X9"))
    assert_true(isidentifier("_"))
    assert_true(isidentifier("_x"))
    assert_true(isidentifier("x_"))

    assert_false(isidentifier("9x"))
    assert_false(isidentifier(""))
    assert_false(isidentifier("False"))
    assert_false(isidentifier("if"))
    assert_false(isidentifier("+"))
    assert_false(isidentifier("9"))
    assert_false(isidentifier("1A"))
    assert_false(isidentifier("a b"))



# Generated at 2022-06-13 17:06:00.554831
# Unit test for function load_extra_vars
def test_load_extra_vars():
    import sys
    import os

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    # Create samples files
    f1 = 'sample1.yml'
    f2 = 'sample2.yml'
    f3 = 'sample3.txt'

    with open(f1, 'w+') as fd:
        fd.write("""

a: 1
b: 2
c: 3
b: 4
""")

    with open(f2, 'w+') as fd:
        fd.write("""
---
a: 1
b: 2
c: 3
b: 4
""")


# Generated at 2022-06-13 17:06:18.248700
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.cli import CLI
    from ansible.cli.arguments import option_helpers as opt_help

    import sys
    opt_help.validate_conflicts(CLI.base_parser,
                                sys.argv[1:])

    test_loader = AnsibleLoader(None, None)


# Generated at 2022-06-13 17:06:25.432760
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Setup
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Tests for loading extra vars in form of a file
    assert (load_extra_vars(loader) == {'name': 'Rich', 'age': 50, 'children': ['John', 'Jane', 'Jill']}) == load_extra_vars(loader)

    # Tests for loading extra vars in form of key-value pairs
    assert (load_extra_vars(loader) == {'name': 'Rich', 'age': 50, 'children': ['John', 'Jane', 'Jill']}) == load_extra_vars(loader)



# Generated at 2022-06-13 17:06:34.996017
# Unit test for function isidentifier
def test_isidentifier():
    assert isidentifier("abc123")
    assert isidentifier("abc_123")
    assert isidentifier("abc_123_def")
    assert isidentifier("_abc_123")
    assert isidentifier("_")
    assert isidentifier("__")
    assert isidentifier("__init__")

    assert not isidentifier("123")
    assert not isidentifier("123abc")
    assert not isidentifier("`~!@#$%^&*()-_=+[]{}\\|;:'\",<>/?")
    assert not isidentifier("abc 123")
    assert not isidentifier("abc\n123")
    assert not isidentifier("abc\t123")
    assert not isidentifier("abc\r123")
    assert not isidentifier("")
    assert not isidentifier(" ")

# Generated at 2022-06-13 17:06:40.115388
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader

    config_data = """{
        "@/tmp/extravars.yml": {
            "foo": "bar"
        },
        "@/tmp/.extravars.yml": {
            "fizz": "buzz"
        },
        "baz": "boo",
        "foo": "baz"
    }"""

    loader = DataLoader()
    config_data = loader.load(config_data)

    assert load_extra_vars(loader) == config_data

# Generated at 2022-06-13 17:06:51.598125
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.cli import CLI

    def find_file(name, paths):
        if name == "test":
            return "tests/test.json"
        else:
            return None

    cli_options = [
        "ansible-playbook",
        "tests/roles/test/tasks/",
        "-e", "@test",
        "-e", "{\"a\": \"c\"}",
        "-e", "[\"d\", \"e\"]",
        "-e", "f=g",
        "-e", "h='i'",
        "-e", "j=k"
    ]

    options = CLI.parse(cli_options)
    loader = DataLoader()
   

# Generated at 2022-06-13 17:07:04.431716
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    set1 = {u'foo': u'bar', u'hello': u'world'}
    set2 = {u'one': 1, u'two': 2, u'three': {u'four': 4, u'five': [5, 5, 5]}}

    # load extra_vars from string
    extra_vars = load_extra_vars(loader)
    assert extra_vars == {}, "Empty extra_vars should be {}"

    # load extra_vars from string
    extra_vars = load_extra_vars(loader)
    assert extra_vars == {}, "Empty extra_vars should be {}"
