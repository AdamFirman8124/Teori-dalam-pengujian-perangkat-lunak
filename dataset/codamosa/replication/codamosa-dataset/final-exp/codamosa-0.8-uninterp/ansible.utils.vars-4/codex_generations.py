

# Generated at 2022-06-13 16:57:26.087739
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    extra_vars_opt = u'@/tmp/foo.yml'
    data = loader.load_from_file(extra_vars_opt[1:])
    print(data['bar'])


if __name__ == '__main__':
    test_load_extra_vars()

# Generated at 2022-06-13 16:57:36.356335
# Unit test for function load_options_vars
def test_load_options_vars():
    option_vars = load_options_vars("1.0")
    assert 'ansible_version' in option_vars
    assert option_vars['ansible_version'] == '1.0'
    assert 'ansible_run_tags' in option_vars
    assert option_vars['ansible_run_tags'] is None
    assert 'ansible_skip_tags' in option_vars
    assert option_vars['ansible_skip_tags'] is None
    assert 'ansible_verbosity' in option_vars
    assert option_vars['ansible_verbosity'] is None
    assert 'ansible_diff_mode' in option_vars
    assert option_vars['ansible_diff_mode'] is False
    assert 'ansible_check_mode' in option_vars

# Generated at 2022-06-13 16:57:46.148781
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.parsing.loader import DataLoader

    # test for empty extra vars
    assert not load_extra_vars(DataLoader())

    # test for invalid extra vars
    # test for extra vars in the form of a list
    assert load_extra_vars(DataLoader())['extra_vars'] == []
    assert load_extra_vars(DataLoader())['extra_vars'] == [1, 2, 3]
    # test for invalid file
    assert '"extra_vars": "@invalid.yaml"' in load_extra_vars(DataLoader({"extra_vars": "@invalid.yaml"})).keys()
    # test for invalid yaml syntax

# Generated at 2022-06-13 16:57:47.172692
# Unit test for function load_extra_vars
def test_load_extra_vars():
    assert False, "nope"

# Generated at 2022-06-13 16:57:55.300757
# Unit test for function merge_hash
def test_merge_hash():
    # test 1: x and y are dicts
    # run with each possible value of recursive
    for recursive in (True, False):
        # run with each possible value of list_merge
        for list_merge in ("replace", "keep", "append", "prepend", "append_rp", "prepend_rp"):
            x = {"a": 1, "b": 2, "d": {"e": 4}, "y": 1, "z": 1}
            y = {"z": 3, "c": 3, "d": {"e": 5}, "t": 3}
            # expected dict

# Generated at 2022-06-13 16:58:08.463312
# Unit test for function merge_hash

# Generated at 2022-06-13 16:58:22.388148
# Unit test for function load_extra_vars
def test_load_extra_vars():

    # Define test case loader
    test_loader = MockLoader({
        'file_name_1.yml': {'a':'A', 'b':'B', 'c':'C'},
        'file_name_2.yml': {'c':'C1', 'd':'D'},
        'file_name_3.yml': {'e':'E'}
    })

    # Test AnsibleOptionsError exception
    # Test None argument - should not raise an exception
    try:
        load_extra_vars(test_loader)
    except Exception:
        raise AssertionError('load_extra_vars: None argument should not raise an exception')

    # Test empty string argument - should not raise an exception

# Generated at 2022-06-13 16:58:32.478880
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Test loading an empty extra_vars
    test_args = {}
    context.CLIARGS = type('obj', (object,), test_args)
    extra_vars = load_extra_vars(None)
    assert extra_vars == {}

    # Test loading a single extra_vars with @
    test_args = {}
    context.CLIARGS = type('obj', (object,), test_args)
    test_args['extra_vars'] = ['@test_files/extra_vars.yaml']
    extra_vars = load_extra_vars(None)
    assert extra_vars is not None
    assert extra_vars == {'key_1': 'value_1', 'key_2': 'value_2'}

    # Test loading a single extra_vars without @

# Generated at 2022-06-13 16:58:42.878204
# Unit test for function load_extra_vars
def test_load_extra_vars():

    import sys
    import unittest
    from ansible import constants as C
    from ansible.cli.adhoc import AdHocCLI
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import PluginLoader
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import AnsibleVars

    class MockVarsModule(object):
        def __init__(self, results):
            self.results = results

        def vars(self):
            return self.results

    class TestAdHocCLI(AdHocCLI):
        '''Test Class derived from AdHocCLI to allow testing private methods'''


# Generated at 2022-06-13 16:58:53.154304
# Unit test for function merge_hash
def test_merge_hash():

    def test(args):
        kwargs = {key: value for key, value in args.items() if key != 'x' and key != 'y'}
        merge_hash(*args['x'], **kwargs) == args['expected']

    def test_all(merge = None):
        X = dict(el1='val1')
        Y = dict(el1='val1b', el2='val2')
        if merge is None:
            expected = C.DEFAULT_HASH_BEHAVIOUR == 'merge' and dict(el1='val1b', el2='val2') or dict(el2='val2')
        else:
            expected = merge and dict(el1='val1b', el2='val2') or dict(el2='val2')

# Generated at 2022-06-13 16:59:10.123087
# Unit test for function merge_hash
def test_merge_hash():
    # dicts
    assert merge_hash({}, {}) == {}
    assert merge_hash({}, {'a': 1}) == {'a': 1}
    assert merge_hash({'a': 1}, {}) == {'a': 1}
    assert merge_hash({'a': 1}, {'a': 1}) == {'a': 1}
    assert merge_hash({'a': 1, 'b': {'c': 1}}, {'a': 1, 'b': {'c': 1}}) == {'a': 1, 'b': {'c': 1}}
    assert merge_hash({'a': 1, 'b': {'c': 1}}, {'a': 2, 'b': {'d': 2}}) == {'a': 2, 'b': {'c': 1, 'd': 2}}

# Generated at 2022-06-13 16:59:22.433979
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.plugins.loader import loader_module

    loader = loader_module.get(C.DEFAULT_LOADER)

    # Test if extra_vars passed as command line argument to ansible-playbook
    # are being processed correctly
    extra_vars_options = {
        'extra_vars': [
            u'@/dev/null',
            u'@/dev/zero',
            u'@/dev/null extra_key=extra_value',
            u'@/dev/zero extra_key=extra_value',
            u'/dev/null extra_key=extra_value',
            u'/dev/zero extra_key=extra_value',
        ],
    }

    extra_vars = load_extra_vars(loader)

    assert extra_vars == {}

    extra_vars = load

# Generated at 2022-06-13 16:59:31.338779
# Unit test for function load_extra_vars
def test_load_extra_vars():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    dl = DataLoader()
    v = VariableManager()

    # test load_extra_vars with empty list
    result = load_extra_vars(dl)
    assert result == {}, "expecting empty dict to be returned with empty list for extra vars"

    # test load_extra_vars with valid key-value
    C.CLIARGS = {'extra_vars': [u'{"a": "b", "c": "d"}']}
    result = load_extra_vars(dl)
    assert result == {
        u'a': u'b',
        u'c': u'd'
    }, "expecting key-value to be returned with a single extra_vars key"



# Generated at 2022-06-13 16:59:43.578772
# Unit test for function merge_hash
def test_merge_hash():
    debug_info = ''
    success = True

    def test_equal(x, y, r, recursive=True, list_merge='replace', debug_info=''):
        result = merge_hash(x, y, recursive, list_merge)
        if result != r:
            raise AssertionError('%s: %s != %s' % (debug_info, result, r))

    test_equal({}, {}, {}, debug_info='empty hash')

    test_equal({'x': 1}, {'x': 1}, {'x': 1}, debug_info='equal hash')
    test_equal({'x': 1}, {'x': 2}, {'x': 2}, debug_info='different hash')

# Generated at 2022-06-13 16:59:56.624317
# Unit test for function merge_hash
def test_merge_hash():

    from collections import OrderedDict

    # define some functions used below in the tests
    def _dict_compare(d1, d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        same = set(o for o in intersect_keys if d1[o] == d2[o])
        return added, removed, modified, same


# Generated at 2022-06-13 17:00:04.997350
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.config.loader import ConfigLoader
    from ansible.module_utils.common.collections import ImmutableDict

    # v1.1: to_yaml no longer used
    # from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # def to_yaml(value):
    #    return AnsibleUnsafeText(dumps(value, default_flow_style=False))

    cl = ConfigLoader(None)

    # Empty string should yield empty dict
    assert load_extra_vars(cl) == {}

    # Empty dictionary
    data = cl.load("{}")
    assert isinstance(data, MutableMapping)
    assert load_extra_vars(cl) == data

    # Key-value string
    data = parse_kv("a=b")
    assert isinstance

# Generated at 2022-06-13 17:00:17.223348
# Unit test for function merge_hash

# Generated at 2022-06-13 17:00:26.782337
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing import vault

    # Test with json
    vars = load_extra_vars(vault.VaultLib())
    assert vars == {}

    # Test with yaml
    vars = load_extra_vars(vault.VaultLib(), '@tests/test_playbooks/test_playbook.yml')
    assert vars == {'test': 3}

    # Test with @file and with Vault
    vars = load_extra_vars(vault.VaultLib())
    assert vars == {}
    vars = load_extra_vars(vault.VaultLib(), '@tests/test_playbooks/test_vault_playbook.yml', '!vault 1.1')
    assert vars == {'test': 3}
    vars = load_

# Generated at 2022-06-13 17:00:36.348420
# Unit test for function isidentifier
def test_isidentifier():
    """
    This function tests the isidentifier function by generating a large number of
    identifier names at run time and testing them.

    A side effect of this test is to verify that 2to3 will properly translate this
    file when run with the -w option
    """

    # Python 2 and Python 3 differ in the characters that are valid in an identifier
    # Python 2 allows the following characters:
    valid_identifier_start = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    valid_identifier_char = valid_identifier_start + u'0123456789'

    # Python 3 allows the following characters:
    # valid_identifier_start = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP

# Generated at 2022-06-13 17:00:48.956562
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing import vault
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Take an example extra_vars from AnsibleCLI
    example_extra_vars = [
        '{"foo": "bar", "fu": {"bar": "baz"}, "f": ["foo", "bar", "baz"]}',
        '{"fu": ["baz", "foo"], "f": "bar"}',
        '@/etc/ansible/playbook.yml',
        '@/etc/ansible/playbook.json',
        '@/etc/ansible/playbook.yml'
    ]

    # Set example extra_vars
    context.CLIARGS['extra_vars'] = example_extra_vars

    # Parse Y

# Generated at 2022-06-13 17:01:06.722794
# Unit test for function combine_vars
def test_combine_vars():
    # Put in some variables
    a = dict(
        # Put in some lists
        list=["x", "y"],
        list_inline=["x", "y"],
        # Put in some dicts
        dict={
            "a": 1,
            "b": 2,
        },
        dict_inline={
            "a": 1,
            "b": 2,
        }
    )


# Generated at 2022-06-13 17:01:19.009027
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible import context
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins import vars_loader

    cli = CLI(['ansible-playbook', '--extra-vars', '@file.yml', '--extra-vars', '@file2.json', '--extra-vars', '{ "a": 1, "b": 2 }', '--extra-vars', 'a=1 b=2', 'test.yml'])
    cli.parse()
    _ = context.CLIARGS
    context.CLIARGS = cli.options

    loader = DataLoader()
    loader.set_vars_loader(vars_loader)
    res = load_extra_vars(loader)


# Generated at 2022-06-13 17:01:24.992258
# Unit test for function combine_vars
def test_combine_vars():
    a = {
        "a": {
            "b": 1,
            "c": [1, 2, 3],
            "d": {
                "e": {
                    "f": 1,
                    }
                }
            },
        "g": [1, 2, 3],
        "h": {
            "i": 1,
            }
        }


# Generated at 2022-06-13 17:01:37.824627
# Unit test for function load_extra_vars
def test_load_extra_vars():
    loader_good = DictDataLoader({
        '@/etc/ansible/good.yml': '''
{
    "foo": "bar"
}
''',
        '@/etc/ansible/good.json': '''
{
    "foo": "bar"
}
''',
        '@/etc/ansible/good.other': '''
not yaml or json
'''
    })
    assert load_extra_vars(loader_good) == {u'foo': u'bar'}

    loader_bad = DictDataLoader({
        '@/etc/ansible/bad.yml': '''
{
    "key": "value
}
'''
    })

# Generated at 2022-06-13 17:01:47.028929
# Unit test for function load_extra_vars
def test_load_extra_vars():
    import tempfile

    # we don't want to use file name of existing files, so we create a temporary directory
    # and use that to generate file names
    tempdir = tempfile.TemporaryDirectory()

    # there is no way to create a file unknown to Ansible, so we create a temporary file
    # and remove it, so that Ansible does not know about it
    tempfile1 = tempfile.NamedTemporaryFile(delete=False)
    tempfile1.close()
    tempfile1_name = tempfile1.name
    os.unlink(tempfile1_name)

    tempfile2 = tempfile.NamedTemporaryFile(delete=False)
    tempfile2.close()
    tempfile2_name = tempfile2.name
    os.unlink(tempfile2_name)

    # since we are going to

# Generated at 2022-06-13 17:01:55.190193
# Unit test for function merge_hash
def test_merge_hash():
    """
    This tests the merge_hash function.
    """
    a = {'a': {'a': 'a', 'b': 'b', 'c': 'c', 'e': {'a': 'a', 'b': 'b', 'c': 'c'}}, 'b': 'b', 'c': 'c', 'd': 'd',
         'e': {'a': 'a', 'b': 'b', 'c': 'c'}, 'f': ['a', 'b', 'c']}

# Generated at 2022-06-13 17:02:06.162882
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(None)
    loader = DataLoader()

    extra_vars = {'host_var': {'hostvar_k': 'hostvar_v'},
                  'var_k': 'var_v'}

    extra_vars_arg = 'host_var={"hostvar_k":"hostvar_v"} var_k=var_v'

    result = load_extra_vars(loader)
    assert result == extra_vars

    context.CLIARGS = {'extra_vars': [extra_vars_arg]}
    result = load_extra_vars(loader)
    assert result == extra_vars

# Generated at 2022-06-13 17:02:11.869623
# Unit test for function load_extra_vars
def test_load_extra_vars():
    assert load_extra_vars([
        '@/dev/null',
        '@/tmp/does/not/exist.yaml',
        '@/tmp/does/not/exist.json',
        '@/tmp/does/exist.yaml',
        '@/tmp/does/exist.json',
        '@/tmp/does/exist.txt',
        '@/tmp/does/exist2.txt',
    ]) == {}

# Generated at 2022-06-13 17:02:16.966260
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play_context import PlayContext

    assert isinstance(load_extra_vars(DataLoader()), dict)

    loader = AnsibleLoader(None, None)
    assert isinstance(load_extra_vars(loader), dict)

    play_context = PlayContext()
    assert isinstance(load_extra_vars(loader), dict)

test_load_extra_vars()

# Generated at 2022-06-13 17:02:21.702748
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    var_manager = VariableManager()

    var_manager.extra_vars = load_extra_vars(loader)


# Generated at 2022-06-13 17:02:45.799856
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None, None)

    # Test data
    opt_1 = u'key_1=value_1 key_2=value_2 key_3=value_3'
    opt_2 = u'@test_1.yml @test_2.yml @test_3.yml'
    opt_3 = u'{key_4: value_4, key_5: value_5}'

    # Test case 1: extra vars with key=value format
    result = load_extra_vars(loader)
    assert result == {}

    result = load_extra_vars(loader, extra_vars_opt=opt_1)

# Generated at 2022-06-13 17:02:49.258587
# Unit test for function load_options_vars
def test_load_options_vars():
    opt_vars_1 = load_options_vars(None)
    assert opt_vars_1 == {'ansible_version': 'Unknown'}, 'Wrong version taken'
    opt_vars_2 = load_options_vars("2.2")
    assert opt_vars_2 == {'ansible_version': '2.2'}, 'Wrong version taken'

    # Unit test for function isidentifier



# Generated at 2022-06-13 17:03:00.535540
# Unit test for function combine_vars
def test_combine_vars():
    # Setup some test data
    a = {
        'foo': 'bar',
        'bar': ['foo', 'bar'],
        'biz': {'baz': 'foo'},
        'baz': ['a', 'b', 'c'],
    }
    b = {
        'foo': 'foo',
        'bar': ['a', 'b', 'c'],
        'biz': {'baz': 'bar'},
        'baz': 'foo',
    }

    # Combine both and make sure they are the same
    assert combine_vars(a, b) == {
        'foo': 'foo',
        'bar': ['foo', 'bar', 'a', 'b', 'c'],
        'biz': {'baz': 'bar'},
        'baz': 'foo',
    }

# Generated at 2022-06-13 17:03:10.847932
# Unit test for function isidentifier
def test_isidentifier():

    # These are valid identifiers in Python 3
    assert isidentifier("valid")
    assert isidentifier("_valid")
    assert isidentifier("__valid")
    assert isidentifier("__válid")
    assert isidentifier("_válid")
    assert not isidentifier("_válid_")
    assert not isidentifier("1valid")
    assert not isidentifier("if")
    assert not isidentifier("while")
    assert not isidentifier("")
    assert not isidentifier("1")
    assert not isidentifier("True")
    assert not isidentifier("None")
    assert not isidentifier("False")

    # These are valid identifiers in Python 2
    assert isidentifier("True")
    assert isidentifier("None")
    assert isidentifier("False")

    #

# Generated at 2022-06-13 17:03:23.214323
# Unit test for function merge_hash
def test_merge_hash():
    m1 = {'a': {'b': "1", 'c': "2"}, 'k': "3", 'l': [], 'n': {}}

    # simple test
    m = merge_hash(m1, {'a': {'b': "2", 'd': "4"}})
    assert m1['a'] == {'b': "1", 'c': "2"} and m['a'] == {'b': "2", "c": "2", "d": "4"}
    assert m['k'] == "3" and m['l'] == [] and m['n'] == {}

    # recursive test
    m = merge_hash(m1, {'a': {'b': {'c': "2"}}}, recursive=True)

# Generated at 2022-06-13 17:03:34.515259
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    # given a loader
    loader = DataLoader()

    # when I load some empty extra vars
    extra_vars = load_extra_vars(loader)

    # then I expect an empty variables list
    assert extra_vars == {}, "Expected empty variable list, got '%s'" % extra_vars

    # when I load some ansible extra vars
    extra_vars="@/path/to/file/with/vars.yml"
    extra_vars = load_extra_vars(loader)

    # then I expect an empty variables list
    assert extra_vars == {}, "Expected empty variable list, got '%s'" % extra_vars

    #

# Generated at 2022-06-13 17:03:42.319004
# Unit test for function load_extra_vars
def test_load_extra_vars():
    loader = DictDataLoader({'@test.yml': '{"a": 1, "b": 2, "c": 3}'})
    extra_vars = load_extra_vars(loader)
    assert extra_vars == {'a': 1, 'b': 2, 'c': 3}

    extra_vars = load_extra_vars(loader)
    assert extra_vars == {'a': 1, 'b': 2, 'c': 3}

    extra_vars = load_extra_vars(loader)
    assert extra_vars == {'a': 1, 'b': 2, 'c': 3}



# Generated at 2022-06-13 17:03:52.149285
# Unit test for function combine_vars
def test_combine_vars():
    x = {
        'a': {
            'b': '1',
            'c': '2',
            'e': '3',
        },
        'd': {
            'f': '4',
            'g': '5',
        },
        'h': '6',
    }
    y = {
        'i': '7',
        'a': {
            'b': '8',
            'j': '9',
        },
        'd': {
            'k': '10',
        },
    }

    # Merge the two dictionaries
    # x has lower priority than y
    # so y's value for 'a', 'b' override x's one
    # and same for y's value for 'a', 'j'
    # as x and y both have a key named d, we merge the

# Generated at 2022-06-13 17:04:03.699240
# Unit test for function merge_hash
def test_merge_hash():
    # this test doesn't test all possible cases
    # it only tests some cases that can be relevant in Ansible modules

    # check that the three basic variables are working ('replace', 'keep' and 'append')
    x = {u'a': [u'x', u'y'], u'b': {u'foo': u'bar'}, u'c': u'x'}
    y = {u'a': [u'y', u'z'], u'b': {u'foo': u'baz'}, u'c': u'y'}
    r = merge_hash(x, y, recursive=False, list_merge='replace')
    assert r == {u'a': [u'y', u'z'], u'b': {u'foo': u'baz'}, u'c': u'y'}

# Generated at 2022-06-13 17:04:17.636051
# Unit test for function merge_hash
def test_merge_hash():

    from ansible.playbook.play_context import PlayContext

    def display_result(res):
        print('\n'.join(['\t{}: {}'.format(k, repr(v)) for k, v in sorted(res.items())]))

    # default context

# Generated at 2022-06-13 17:04:38.536466
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Check loading data from yaml file
    data = load_extra_vars(loader)
    assert type(data) is dict
    assert len(data) == 0

    cliargs = {'extra_vars': ['@/dev/null']}
    data = load_extra_vars(loader)
    assert type(data) is dict
    assert len(data) == 0

    cliargs = {'extra_vars': ['@/non-existent-file']}

# Generated at 2022-06-13 17:04:50.754468
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import fragment_loader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    loader = fragment_loader.FragmentLoader()
    assert load_extra_vars(loader) == {}

    # normal YAML file
    extra_vars = [u"@tests/utils/vars1.yml"]
    assert load_extra_vars(loader) == {u'foo': u'bar'}

    # YAML file with a vault encrypted string
    extra_vars = [u"@tests/utils/vars2.yml"]
    result = load_extra_vars(loader)
    assert isinstance(result, dict)

# Generated at 2022-06-13 17:04:54.495033
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None)
    extra_vars = load_extra_vars(loader)
    assert extra_vars == {}



# Generated at 2022-06-13 17:04:58.600313
# Unit test for function load_extra_vars
def test_load_extra_vars():
    module = AnsibleModule(argument_spec=dict())

    with pytest.raises(AnsibleOptionsError):
        load_extra_vars(loader=DataLoader())


# Generated at 2022-06-13 17:05:09.989864
# Unit test for function combine_vars

# Generated at 2022-06-13 17:05:14.640906
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    assert load_extra_vars(loader) == {'@a': 'b', 'c': 'd'}

# Generated at 2022-06-13 17:05:21.424151
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Test that function loads a dictionary from a string
    assert load_extra_vars("string") == {'string': ''}
    assert load_extra_vars("a=b") == {'a': 'b'}
    assert load_extra_vars("a=b b=c") == {'a': 'b', 'b': 'c'}
    assert load_extra_vars("a=b b=c c=d") == {'a': 'b', 'b': 'c', 'c': 'd'}
    # Test that function loads a dictionary from a file
    assert load_extra_vars("@path") == {'path': ''}

# Generated at 2022-06-13 17:05:32.421698
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    assert load_extra_vars(loader) == {}

    assert load_extra_vars(loader) == {}, "Empty extra_vars should not change the result."
    assert load_extra_vars(loader, extra_vars=[]) == {}, "Empty extra_vars should not change the result."
    assert load_extra_vars(loader, extra_vars=None) == {}, "Empty extra_vars should not change the result."
    assert load_extra_vars(loader, extra_vars=False) == {}, "Empty extra_vars should not change the result."


# Generated at 2022-06-13 17:05:45.030754
# Unit test for function merge_hash
def test_merge_hash():
    from collections import OrderedDict
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeDict, AnsibleUnsafeList, AnsibleUnsafeText

    dict_no_recursive = {
        'foo': 'bar',
        'baz': {'foo': 'foo', 'bar': 'bar'},
        'list': ['foo', 'baz'],
    }

    dict_recursive = dict_no_recursive

# Generated at 2022-06-13 17:05:56.953741
# Unit test for function merge_hash
def test_merge_hash():
    import copy

    # -- test recursive = False
    x = {'a': 1, 'b': {'a': 1, 'b': {'a': 1, 'b': 1, 'c': 1}, 'c': 1}, 'c': 1}
    y = {'a': 2, 'b': {'a': 2, 'b': {'a': 2, 'd': 2, 'e': 2}, 'd': 2}, 'd': 2}
    z = copy.deepcopy(x)
    assert merge_hash(z, y, recursive=False, list_merge='replace') == y
    z = copy.deepcopy(x)
    assert merge_hash(z, y, recursive=False, list_merge='append') == x

    # -- test recursive = True and list_merge = 'replace'
    z = copy

# Generated at 2022-06-13 17:06:12.836204
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible.parsing.dataloader import DataLoader

    extra_vars = load_extra_vars(DataLoader())
    assert 'TEST_ANSIBLE_VERSION' in extra_vars
    assert isinstance(extra_vars['TEST_ANSIBLE_VERSION'], basestring)

# Generated at 2022-06-13 17:06:22.929874
# Unit test for function merge_hash
def test_merge_hash():
    import copy

    # quick tests
    assert merge_hash({}, {}, False, 'replace') == {}
    assert merge_hash({}, {'foo': 42}, False, 'replace') == {'foo': 42}
    assert merge_hash({'foo': 42}, {}, False, 'replace') == {'foo': 42}

    assert merge_hash({}, {}, False, 'keep') == {}
    assert merge_hash({}, {'foo': 42}, False, 'keep') == {'foo': 42}
    assert merge_hash({'foo': 42}, {}, False, 'keep') == {'foo': 42}

    assert merge_hash({}, {}, False, 'append') == {}
    assert merge_hash({}, {'foo': 42}, False, 'append') == {'foo': 42}

# Generated at 2022-06-13 17:06:30.496697
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # simple test
    extra_vars = load_extra_vars(None)
    assert extra_vars == {}
    # simple test
    extra_vars = load_extra_vars(None)
    assert extra_vars == {}
    # simple test
    extra_vars = load_extra_vars(None)
    assert extra_vars == {}
    # simple test
    extra_vars = load_extra_vars(None)
    assert extra_vars == {}

# Generated at 2022-06-13 17:06:38.684519
# Unit test for function load_extra_vars
def test_load_extra_vars():
    # Need a dummy class
    class FakeLoader:
        pass

    loader = FakeLoader()

    def load(data):
        if isinstance(data, dict):
            return data
        raise Exception("Can't load")

    loader.load = load

    def load_from_file(data):
        if isinstance(data, dict):
            return data
        raise Exception("Can't load")

    loader.load_from_file = load_from_file

    def test_load_extra_vars_yaml(data):
        return load_extra_vars(loader)

    fake_args = {
        "extra_vars": [
            "@/path/to/yaml",
            "a=1",
            "{\"b\":2}",
            "[(a),(b)]"
        ]
    }

    context

# Generated at 2022-06-13 17:06:50.576480
# Unit test for function merge_hash
def test_merge_hash():
    h1 = {'a':1}
    h2 = {'a':2}
    h3 = merge_hash(h1,h2)
    assert h3['a'] == 2

    h1 = {'a':{'b':1}}
    h2 = {'a':{'c':2}}
    h3 = merge_hash(h1,h2)
    assert h3['a']['b'] == 1
    assert h3['a']['c'] == 2

    h1 = {'a':{'b':1}}
    h2 = {'a':{'b':2}}
    h3 = merge_hash(h1,h2)
    assert h3['a']['b'] == 2
    assert len(h3['a']) == 1


# Generated at 2022-06-13 17:06:57.827275
# Unit test for function load_extra_vars
def test_load_extra_vars():
    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader
    C.DEFAULT_HASH_BEHAVIOUR = "replace"
    loader = DataLoader()
    extra_vars = {}
    extra_vars = combine_vars(extra_vars, loader.load_from_file('test/test_load_extra_vars.yml'))
    assert extra_vars['foo']['bar'] == 'new'
    assert extra_vars['foo']['baz'] == 'old'
    assert extra_vars['foo']['barlist'] == [1, 2, 3]
    assert extra_vars['foo']['newlist'] == [5, 6, 7]

# Generated at 2022-06-13 17:07:09.228951
# Unit test for function merge_hash
def test_merge_hash():
    assert merge_hash({}, {}, True, 'replace') == {}

    test_dict = merge_hash({'a': '1', 'b': '2'}, {'b': '3', 'c': '4'}, True, 'replace')
    assert test_dict == {'a': '1', 'b': '3', 'c': '4'}

    test_dict = merge_hash({'a': ['1', '2']}, {'a': ['3', '4']}, True, 'replace')
    assert test_dict == {'a': ['3', '4']}

    test_dict = merge_hash({'a': ['1', '2']}, {'a': ['3', '4']}, True, 'keep')
    assert test_dict == {'a': ['1', '2', '3', '4']}