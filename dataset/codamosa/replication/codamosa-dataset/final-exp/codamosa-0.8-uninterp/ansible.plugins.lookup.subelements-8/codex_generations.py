

# Generated at 2022-06-13 14:13:41.254867
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # This test is based on data from the jinja2 templating engine
    # that is used in Ansible. It is part of the Ansible source code.
    # It has been adapted to the present module.

    from ansible.module_utils import basic

    class FakeModule():
        def __init__(self):
            self.params = {}

    class FakeTempletor():
        def __init__(self):
            self._available_variables = variables

    module = FakeModule()
    templetor = FakeTempletor()
    lookup_module = LookupModule()
    lookup_module._templar = templetor
    lookup_module._templar._available_variables = variables
    lookup_module._templar.template = lambda x: x


# Generated at 2022-06-13 14:13:49.932965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    # set up dummy plugin, template and variable manager
    class DummyTemplate(Templar):
        def __init__(self, loader, variables=None):
            super(Templar, self).__init__(loader, variables)

        def template(self, thing, convert_bare=False, fail_on_undefined=True, override_vars=None, preserve_trailing_newlines=True, escape_backslashes=True, convert_data=True, remove_unsafe_templates=False, bare_deprecated=True):
            return thing

    dummy_loader = DataLoader()
    dummy_play

# Generated at 2022-06-13 14:13:58.826221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    lookup_plugin = LookupModule()

    # execute
    result = lookup_plugin.run([{
        'a': {
            'x': [1, 2],
            'y': [3, 4],
            'z': 'stam'
        },
        'b': {
            'x': [5, 6],
            'y': [7, 8],
            'z': 'stam'
        }
    }, 'a.x'])
    assert len(result) == 2
    assert (result[0][0]['a'], result[0][1]) == ({'x': [1, 2], 'y': [3, 4], 'z': 'stam'}, 1)

# Generated at 2022-06-13 14:14:10.083923
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    terms = [ [
        {
            'name': 'test1',
            'mysql': {
                'password': 'test1',
                'hosts': [ 'test1.example.com' ],
                'privs': [ 'test1:USERADMIN' ],
            }
        },
        {
            'name': 'test2',
            'mysql': {
                'password': 'test2',
                'hosts': [ 'test2.example.com' ],
                'privs': [ 'test2:USERADMIN' ],
            }
        },
    ], 'mysql.hosts']
    variables = {}
    lm = LookupModule()
    lm._templar = None
    lm._loader = None

# Generated at 2022-06-13 14:14:21.030562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """unit test for run method of LookupModule class"""
    # import module
    from ansible.plugins.lookup import LookupModule

    # construct an instance of the LookupModule
    class TestVars(object):
        # building mocks
        class TestLoader(object):
            pass
        testloader = TestLoader()

        class TestTemplar(object):
            # building mocks
            class TestTemplarFlags(object):
                pass
            templarflags = TestTemplarFlags()
        testtemplar = TestTemplar()


    testvars = TestVars()
    test_lookup_module = LookupModule()

    test_lookup_module._templar = testvars.testtemplar
    test_lookup_module._loader = testvars.testloader

    # test with

# Generated at 2022-06-13 14:14:25.154653
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import unittest
    import ansible.utils.listify
    import ansible.plugins.lookup.subelements
    dirname = os.path.dirname(sys.modules[ansible.utils.listify.__name__].__file__)
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[ansible.plugins.lookup.subelements.__name__])
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 14:14:36.879767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import lookups.subelements
    lookup_mod = lookups.subelements.LookupModule()

    class CallbackModule(object):
        def __init__(self, pattern, count):
            self.pattern = pattern
            self.count = count

        def _match(self, pattern, data):
            return pattern in data

        def _get_doc(self, data):
            return data.__doc__

        def match(self, pattern, data):
            self.count['match_called'] += 1
            return self._match(pattern, data)

        def get_doc(self, data):
            self.count['get_doc_called'] += 1
            return self._get_doc(data)


# Generated at 2022-06-13 14:14:47.512884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    subelements = LookupModule()

# Generated at 2022-06-13 14:15:00.352355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types

    # verify that results are correct for specific input
    def testrun(terms, expected):
        lookup_plugin = LookupModule()
        lookup_plugin.set_templar(None)
        lookup_plugin.set_loader(None)
        result = lookup_plugin.run(terms, None, boolean=boolean)
        if expected != result:
            raise Exception("unexpected result, got %s instead of %s" % (result, expected))

    # verifies that the specified exception is thrown by the run method
   

# Generated at 2022-06-13 14:15:00.945127
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:15:16.056209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    if PY2:
        from ansible.module_utils.compat import return_values
        from ansible.module_utils.compat import type_compat
    else:
        # PY3
        from ansible.module_utils.parsing.convert_bool import return_values
        from ansible.module_utils.parsing.convert_bool import type_compat

    skip_missing = return_values.get('skip_missing')

    # create the mock class
    lookuper = LookupModule()
    lookuper.set_options({})

    # check what happens when no term is given

# Generated at 2022-06-13 14:15:27.385513
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mock_loader = AnsibleLoader(None, None, True)
    mock_loader._templar = Templar(loader=mock_loader)

    # test wrong number of terms
    l = LookupModule()
    l.set_loader(mock_loader)
    terms_list = [
        [],
        [1,2,3,4,5],
        [1,2,3,'flag1=True', 'flag2=False']
    ]
    for terms in terms_list:
        try:
            l.run(terms, None)
        except AnsibleError as e:
            assert "subelements lookup expects" in str(e)
        else:
            raise AssertionError('AnsibleError not raised')

    # test missing key
    l = LookupModule()

# Generated at 2022-06-13 14:15:28.285410
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: method to be implemented
    assert False

# Generated at 2022-06-13 14:15:40.270768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:15:53.305499
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import OrderedDict
    from ansible.utils.vars import combine_vars
    from ansible.plugins.lookup import LookupBase

    record_data = '{"record_hash":"12345", "record_name": "test", "record_value": "true"}'

    record_data_list = [
        {"record_hash": "12345", "record_name": "test", "record_value": "true"},
        {"record_hash": "67890", "record_name": "test", "record_value": "false"}
    ]

    class LookupModuleUnitTest(LookupBase):
        def __init__(self, loader=None, templar=None, **kwargs):
            super(LookupModuleUnitTest, self).__init__(loader, templar)

# Generated at 2022-06-13 14:16:04.202485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test the LookupModule method run with the following testdata:
        Testcases:
            001: Test with no input data
            002: Test with empty list
            003: Test with empty dictionary
            004: Test with non-dictionary input data
            005: Test with missing subkey, skip_missing not set
            006: Test with missing subkey, skip_missing set

    """
    # Testcase 001
    lookup_obj = LookupModule()
    terms = []
    with pytest.raises(AnsibleError) as excinfo:
        lookup_obj.run(terms, None)
    assert 'subelements lookup expects' in str(excinfo.value)

    # Testcase 002
    lookup_obj = LookupModule()
    terms = [[]]

# Generated at 2022-06-13 14:16:13.846618
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init
    lookup_instance = LookupModule()

    # build list of dictionaries

# Generated at 2022-06-13 14:16:20.341655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = (
        ['alice', 'bob'],
        'authorized',
        {'skip_missing': True}
    )
    options = {
        "var": {
            "users": [
                {
                    'password': 'mysql-password',
                    'name': 'alice'
                },
                {
                    'password': 'other-mysql-password',
                    'name': 'bob'
                }
            ]
        }
    }

    l = LookupModule()
    l.set_options(var=options)
    assert l.run(terms, options) == [
        ({'name': 'alice', 'password': 'mysql-password'}, 'alice'),
        ({'name': 'bob', 'password': 'other-mysql-password'}, 'bob')
    ]

# Generated at 2022-06-13 14:16:25.225727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import json
    print("Testing method run of class LookupModule")
    class MockTemplar:
        def __init__(self):
            self.template_data = None
            self.template_uid = None
            self.template_gid = None
            self.template_mode = None
            self.template_seuser = None
            self.template_serole = None
            self.template_selevel = None
            self.template_setype = None
            self.template_default_filters = []
            self.template_add_filters = []
        def template(self, template_data=None, preserve_trailing_newlines=True, escape_backslashes=True,
                     fail_on_undefined=True, override_vars=None):
            if template_data is None:
                return

# Generated at 2022-06-13 14:16:36.136471
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six.moves import StringIO

    l = LookupModule()
    l._loader = DictDataLoader()
    l._templar = Templar(loader=l._loader, variables={})
    terms = ['foo', 'bar']
    variables = {'foo': {'bar': ['one', 'two']}}
    result = [x for x in l.run(terms, variables)]
    assert len(result) == 2
    assert result[0][0] == variables['foo']
    assert result[0][1] == 'one'
    assert result[1][0] == variables['foo']
    assert result[1][1] == 'two'



# Generated at 2022-06-13 14:16:54.251239
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass  # TODO

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:17:00.810516
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _mock_templar(value):
        return 'TEMPLATED_' + value

    module = LookupModule()
    module._templar = _mock_templar
    module._loader = None
    result = module.run(['TEMPLATE', 'TEMPLATE2'])
    assert result is None


test_LookupModule_run()

# Generated at 2022-06-13 14:17:10.516333
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # import needed modules
    from ansible.utils.unsafe_proxy import wrap_var
    import os

    # define test variables

# Generated at 2022-06-13 14:17:19.591475
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import iteritems
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('subelements')


# Generated at 2022-06-13 14:17:31.575032
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test for 'subelements' lookup, need to run this with ansible -m ansiblelib.test.test_lookup_subelements
    from ansiblelib.test import AnsibleExitJson
    from ansiblelib.test import AnsibleFailJson
    from ansiblelib.test import display
    from ansiblelib.test import Mock
    from ansiblelib.test import patch

    L = LookupModule()
    L.set_options({})

    # check error

# Generated at 2022-06-13 14:17:44.390480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    if PY3:
        from importlib import reload

    lookup_plugin = LookupModule()

    # test 1: look for 'var' in a list of dicts
    #         expected result: 'a', 'b'
    lookup_plugin.set_options({'skip_missing': False})
    terms = [
        [{'var': 'a'}, {'var': 'b'}, {'var': 'c'}],
        'var'
    ]
    assert  ['a', 'b', 'c'] == lookup_plugin.run(terms, None)

    # test 2: look for 'var' in a dict of dicts,
    #         expected result: 'a', 'b'

# Generated at 2022-06-13 14:17:55.571917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Opts:
        def __init__(self):
            self.connection = "local"
            self.module_path = None
            self.forks = 100
            self.become = True
            self.become_method = "sudo"
            self.become_user = "root"
            self.check = False
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.syntax = None
            self.tags = ["all"]


# Generated at 2022-06-13 14:18:05.085222
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO

    # Make a mock templar object and loader object for test purposes
    class YourLookupModule(LookupModule):
        def __init__(self, templar, loader, basedir=None, **kwargs):
            self._templar = templar
            self._loader = loader

    your_lookup_module_instance = YourLookupModule(None, None)


# Generated at 2022-06-13 14:18:16.934404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    myhosts = [{'hostname': 'server01', 'puppetclass': 'role::mysql', 'mysql': {'password': 'secret-01', 'root': True}},
               {'hostname': 'server02', 'puppetclass': 'role::mysql', 'mysql': {'password': 'secret-02', 'root': False}},
               {'hostname': 'server03', 'puppetclass': 'role::app', 'mysql': {'password': 'secret-03', 'root': False}}]

# Generated at 2022-06-13 14:18:24.274917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants as C
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import lookup_loader

    class Options(object):
        def __init__(self, connection, module_path, forks, become, become_method, become_user, check, diff):
            self.connection = connection
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.become_user = become_user


# Generated at 2022-06-13 14:19:01.984707
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setting up test data
    terms = [
        {'test1': {'a': 1, 'b': 2, 'c': 3}},
        'c',
    ]

    # setting up lookup instance
    lookup_instance = LookupModule()

    # executing the method under test
    result = lookup_instance.run(terms=terms, variables=None)

    # verifying the result
    assert result == [(terms[0]['test1'], 3)]

# Generated at 2022-06-13 14:19:14.649323
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Done: Define test vars
    import os
    import sys
    import json
    import unittest

    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_iterable
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    plugin_cls = LookupModule

    class LookupModule_runTest(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-13 14:19:26.516929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Use fixture params to check the number of expected calls
    # Return values of these calls are set using the fixture mocks
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-13 14:19:34.486699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing import vault

    lookupper = LookupModule()

    # example vars

# Generated at 2022-06-13 14:19:47.370435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Use a test-inventory and a test-vars-file to check if the lookup behaves as expected.
    """
    import os
    import sys
    import tempfile
    import unittest

    class Test_LookupModule(unittest.TestCase):

        def setUp(self):
            self.loader = None
            self.basedir = os.path.join(os.path.dirname(__file__), 'test/')
            self.tmpdir = tempfile.mkdtemp()
            self.inventory = os.path.join(self.tmpdir, "inventory.ini")
            self.vars = os.path.join(self.tmpdir, "vars.yml")

            # write inventory file

# Generated at 2022-06-13 14:19:56.798856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    params = []
    results = []
    raise_error = True
    first_iteration = True
    for term, result in zip(params, results):
        lookup = LookupModule()
        if raise_error:
            assert isinstance(result, AnsibleError)
            try:
                lookup.run(terms=term, variables={})
            except AnsibleError as e:
                assert e.message == result.message
        else:
            assert lookup.run(terms=term, variables={}) == result
        if first_iteration:
            raise_error = False
            first_iteration = False

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:20:07.238245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    class FakeTemplar(object):
        def __init__(self, loader):
            self._loader = loader

        def template(self, value, convert_bare=True, preserve_trailing_newlines=True, escape_backslashes=True, fail_on_undefined=True, overrides=None):
            return self._loader.load(value, variable_manager)

    class FakeVarsModule(object):
        def __init__(self, loader, templar):
            self._loader = loader
            self._templar = templar

        def add_reference(self, other, name=None):
            pass

        def set_fact(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 14:20:16.782129
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init lookup
    lookup = LookupModule()

    # init terms
    terms = []
    terms.append({"test":{"test2":"aaaa","test3":"bbbb"}})
    terms.append(["test","test3"])
    terms.append({"skip_missing":True})
    # run tests with one term
    ret = lookup._flatten(lookup.run(terms, None))
    assert ret == ["bbbb"]
    # run tests with a list of dictionaries
    terms[0] = [{"test":{"test1":["aaaa","bbbb"],"test3":"cccc"}},{"test":{"test2":["ffff"],"test3":"eeee"}}]
    ret = lookup._flatten(lookup.run(terms, None))
    assert len(ret) == 3
    assert ret[0] == "cccc"
    assert ret

# Generated at 2022-06-13 14:20:28.885844
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import PY3
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    lookup_module = LookupModule()

    class MockUnsafeText(AnsibleUnsafeText):
        def __str__(self):
            return to_text(self)

    class MockTemplate(object):
        def __init__(self, loader, shared_loader_obj, searchpath):
            self.loader = loader
            self.searchpath = searchpath
            self.basedir = '.'
            self.environment = None


# Generated at 2022-06-13 14:20:38.401907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Tests if the run() method is able to return a list of subelements (description)
    corresponding to the lookup ansible plugin of the same name (see description)

    :return: None
    """
    # Unit tests for run() method
    import copy
    import unittest

    # define the test data used
    loader = None
    templar = None

# Generated at 2022-06-13 14:21:49.414705
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:22:00.339626
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # with users as list, should produce an error since 'authorized' key is not in the users list
    try:
        result = LookupModule().run([{'name': 'alice'}, 'authorized'], {})
        raise AssertionError('trying to lookup a list without the subkey should fail')
    except AnsibleError as e:
        assert str(e) == "could not find 'authorized' key in iterated item '{'name': 'alice'}'"

    # with users as list, should produce an error since 'authorized' key is a string, not a list

# Generated at 2022-06-13 14:22:09.493339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.display import Display
    # initialize display
    display = Display()

    # initialize lookup-plugin:
    lookupModule = LookupModule()
    lookupModule._templar = "templar"
    lookupModule._loader = "loader"

    # Test with a simple dictionary
    test_dict = {'hosts': ['host1', 'host2'], 'username': 'ansible', 'run_as': 'foo'}
    test_dict_result = [(test_dict, 'host1'), (test_dict, 'host2')]

# Generated at 2022-06-13 14:22:14.480349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Todo: Implement unit test for LookupModule.run()

    class fake_class:
        class fake_templar:
            # Todo: Implement fake_templar
            pass
        class fake_loader:
            # Todo: Implement fake_templar
            pass
    os.path.abspath = lambda x: x
    l = LookupModule(loader=fake_class.fake_loader(), templar=fake_class.fake_templar())

    l.run([[{'a': 'b'}, {'a': {'b': 'c'}}], 'a'])

# Generated at 2022-06-13 14:22:23.241120
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # arrange
    terms = [([{'a': 1}, {'a': 2}], 'a')]
    variables = {'a': 1}
    lookup_obj = LookupModule()

    # act
    loop_result = []
    for item in lookup_obj.run(terms, variables):
        loop_result.append(item)

    # assert
    expected_result = [(dict({'a': 1}), 1), (dict({'a': 2}), 2)]
    assert loop_result == expected_result



# Generated at 2022-06-13 14:22:35.991070
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Construct object
    lookup_module = LookupModule()

    # Construct test data

# Generated at 2022-06-13 14:22:49.473511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Test for arguments error
    l = LookupModule()
    try:
        l.run(terms=[], variables={}, **{})
        assert False
    except AnsibleError as e:
        assert e.message.startswith('subelements lookup expects a list of two or three items')

    # Test for terms error
    try:
        l.run(terms=['foo'], variables={}, **{})
        assert False
    except AnsibleError as e:
        assert e.message.startswith('subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey')

    # Test for flags error

# Generated at 2022-06-13 14:23:01.562712
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest

    l = LookupModule()
    l._templar = None
    l._loader = None

# Generated at 2022-06-13 14:23:12.622273
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup testdata
    ua = {'name': 'alice',
          'authorized': ['/tmp/alice/onekey.pub',
                         '/tmp/alice/twokey.pub'],
          'mysql': {'password': 'mysql-password',
                    'hosts': ['%',
                              '127.0.0.1',
                              '::1',
                              'localhost'],
                    'privs': ['*.*:SELECT',
                              'DB1.*:ALL']},
          'groups': ['wheel']}

# Generated at 2022-06-13 14:23:24.600892
# Unit test for method run of class LookupModule