

# Generated at 2022-06-13 14:13:46.511704
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import needed parts
    from ansible.module_utils.six import iteritems
    # setup
    lookup_obj = LookupModule()
    lookup_obj._templar = None
    lookup_obj._loader = None
    # test-1
    data = dict(
        skipped=False,
        name="alice",
        authorized=[
            dict(
                skipped=False,
                filename="/tmp/alice/onekey.pub",
                state="present"
            ),
            dict(
                skipped=False,
                filename="/tmp/alice/twokey.pub",
                state="present"
            ),
        ]
    )
    terms = [data, "authorized", dict(skip_missing=False)]

# Generated at 2022-06-13 14:13:56.454904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import os.path
    import __builtin__
    import tempfile
    import ansible
    import ansible.utils
    import ansible.inventory
    import doctest
    from ansible.utils.unicode import to_str
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.listify import listify_lookup_plugin_terms


# Generated at 2022-06-13 14:14:06.347249
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestAnsibleModule():
        params = {}

    test_ansible_module = TestAnsibleModule()

    # test subelements lookup with a list of dictionaries
    terms = ['users', 'groups']
    users = [
        {'name': 'alice', 'groups': ['wheel', 'jail']},
        {'name': 'bob', 'groups': ['nobody']},
    ]
    users_list = [
        {'name': 'alice', 'groups': ['wheel', 'jail']},
        {'name': 'bob', 'groups': ['nobody']},
    ]

    ret = LookupModule.run(terms, users, variables=None, **test_ansible_module.params)

# Generated at 2022-06-13 14:14:18.635540
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def get_LookupModule_instance():
        return LookupModule()

    def get_LookupModule_vars():
        return {'users': [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
                          {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'skipped': True}]}

    def get_LookupModule_terms():
        return [[{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}], 'authorized']


    class get_LookupModule_loader:
        def __init__(self):
            pass

# Generated at 2022-06-13 14:14:27.711396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create class and test variables
    tlm = LookupModule()
    tusers = {'users': [{'name': 'alice', 'mysql': {'password': 'mysql-password'}}, {'name': 'bob', 'mysql': {'password': 'other-mysql-password'}}]}
    tvariables = dict(users=tusers)
    tterms = [['users'], 'mysql.password']

    # perform lookup
    ret = tlm.run(tterms, tvariables)

    # perform test and assert results
    assert isinstance(ret, list)
    assert ret == ['mysql-password', 'other-mysql-password']


# Generated at 2022-06-13 14:14:38.657621
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize the class
    lookup = LookupModule()

    # Define the input variables

# Generated at 2022-06-13 14:14:48.572537
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Initialize class and variables needed for the tests
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({})
    lookup_plugin._templar = None
    lookup_plugin._loader = None

    # Test case with lists

# Generated at 2022-06-13 14:15:01.260921
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   # setup
   import ansible.plugins.loader
   import ansible.utils.module_docs_fragments

   lmp = LookupModule()
   class FakeTemplar:
      def template(self, x):
         return x
   lmp._templar = FakeTemplar()
   lmp._loader = ansible.plugins.loader

   # function tested: run
   ret = lmp.run([], {}, variable_manager=None, loader=None, templar=None, modified_vars=None)
   assert ret == None, "dummy returned %s" % ret

   ret = lmp.run([['skipped'], 'subelements', {'skip_missing': True}], {}, variable_manager=None, loader=None, templar=None, modified_vars=None)
   assert ret

# Generated at 2022-06-13 14:15:11.637490
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test "Basic subkey lookup"
    lookup_module = LookupModule()
    terms = [{'users': [{'authorized': ['/tmp/user-one/id_rsa.pub',
                                        '/tmp/user-two/id_rsa.pub'],
                          'name': 'user_one'},
                         {'authorized': ['/tmp/user-two/id_rsa.pub'],
                          'name': 'user_two'},
                         {'authorized': ['/tmp/user-three/id_rsa.pub',
                                         '/tmp/user-four/id_rsa.pub'],
                          'name': 'user_three'}]},
            'authorized']

# Generated at 2022-06-13 14:15:19.307219
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    user_list = [
        {'name': 'alice',
         'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': 'bob',
         'authorized': ['/tmp/bob/id_rsa.pub']}
        ]
    # tuple of (return_value, [args])

# Generated at 2022-06-13 14:15:39.891631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.listify import listify_lookup_plugin_terms

    class UserDefinedClass(AnsibleBaseYAMLObject):
        _instance_class = dict
        _namespaceless_members = ["_instance_class"]

        yaml_tag = u'!UserDefinedClass'

        def __init__(self, value):
            self._instance_class = value

        @staticmethod
        def to_yaml(dumper, value):
            return dumper.represent_mapping(u'!UserDefinedClass', value._instance_class)


# Generated at 2022-06-13 14:15:53.001910
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()
    terms = [[{'firstname': 'Mike', 'lastname': 'Smith', 'skipped': False},
              {'firstname': 'John', 'lastname': 'Doe', 'skipped': False},
              {'firstname': 'Jane', 'lastname': 'Doe', 'skipped': True},
              {'skipped': True}],
             'lastname']
    ret = test_LookupModule.run(terms, {})
    assert ret == [('Mike', 'Smith'), ('John', 'Doe')]
    terms = [[{'skipped': True}], 'lastname']
    ret = test_LookupModule.run(terms, {})
    assert ret == []

# Generated at 2022-06-13 14:16:03.930108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_term(value):
        return {
            '_terms': value,
            '_key': None,
            '_ds': None,
        }

    l = LookupModule()

    # terms is not a list
    assert_error_raises(l, 'subelements lookup expects a list of two or three items, ', 'notalist')

    # terms is list with too few items
    assert_error_raises(l, 'subelements lookup expects a list of two or three items, ', [1, 2, 3, 4])

    # first term is not a dict or a list
    assert_error_raises(l, 'subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey',
                        [1, 'subkey'])

    # second term is

# Generated at 2022-06-13 14:16:15.666934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

# Generated at 2022-06-13 14:16:24.743716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Create a class
    class ClassLookupModule(LookupModule):
        """Subclass of LookupModule"""

        def __init__(self, templar=None, loader=None, basedir=None, **kwargs):
            super(ClassLookupModule, self).__init__(
                templar=templar, loader=loader, **kwargs)

    basedir = os.path.abspath(os.path.dirname(__file__))
    loader = DataLoader()

    # Create the vars dict
    vars = dict()

# Generated at 2022-06-13 14:16:30.178033
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:42.987551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    class Item0(object):
        def __init__(self, dict_value): self.__dict__.update(dict_value)
    class Item1(object):
        def __init__(self, dict_value): self.__dict__.update(dict_value)

# Generated at 2022-06-13 14:16:50.280911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # simple test
    terms = [
        [{
            'name': 'alice',
            'authorized': [
                'x',
                'y',
                'z'
            ],
            'mysql': {
                'hosts': [
                    'a',
                    'b',
                    'c'
                ]
            }
        }, {
            'name': 'bob',
            'authorized': [
                'x',
                'y',
                'z'
            ],
            'mysql': {
                'hosts': [
                    'a',
                    'b',
                    'c'
                ]
            }
        }],
        "authorized"
    ]
    results = module.run(terms, None)

# Generated at 2022-06-13 14:17:03.407380
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Some test data:
    test_data = '''---
users:
  - name: alice
    authorized:
      - /tmp/alice/onekey.pub
      - /tmp/alice/twokey.pub
  - name: bob
    authorized:
      - /tmp/bob/id_rsa.pub
'''
    # Variables
    loader = DataLoader()
    vars_manager = VariableManager()

    # Setup
    lm = LookupModule()
    lm.set_options({'_variables': vars_manager, '_loader': loader})
    lm._templar = None  # t

    # result of run
    result = lm.run

# Generated at 2022-06-13 14:17:11.945638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set up test
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, "testvars.yml")
    if not os.path.exists(test_file):
        raise Exception("Test file not found: " + test_file)
    test_data = yaml.safe_load(open(test_file))
    # invoke test
    lu = LookupModule()
    result = lu.run([test_data["users"]], terms=["mysql.hosts"])
    # check test result
    assert len(result) == 4
    assert result[0] == (test_data["users"][0], test_data["users"][0]["mysql"]["hosts"][0])
   

# Generated at 2022-06-13 14:17:42.258473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ LookupModule - run() test cases """
    # Initialize a LookupModule object
    lookup_plugin = LookupModule()

    # Test case - empty list
    terms = []
    variables = {}
    result = lookup_plugin._templar.template('{{ q("subelements", %s, "bar", {"skip_missing": True}) }}' % terms, variables)
    assert result == []

    # Test case - list with 1 element
    terms = [ {} ]
    variables = {}
    result = lookup_plugin._templar.template('{{ q("subelements", %s, "bar", {"skip_missing": True}) }}' % terms, variables)
    assert result == []

    # Test case - list with 2 elements
    terms = [ {}, "foo" ]
    variables = {}
    result = lookup_plugin._

# Generated at 2022-06-13 14:17:53.483875
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:03.928859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = __import__("subelements")
    lookup = module.LookupModule()
    assert lookup.run([['a'], 'b'], False) == []
    assert lookup.run([{'a': 'b', 'c': 'd'}, 'e'], False) == []
    assert lookup.run([[{'a': 'b'}], 'a'], False) == [('b', )]
    assert lookup.run([[{'a': 'b'}], 'a', {'skip_missing': True}], False) == []
    assert lookup.run([[{'a': 'b'}], 'b', {'skip_missing': True}], False) == []
    assert lookup.run([[{'a': 'b'}], 'b', {'skip_missing': False}], False) == AnsibleError

# Generated at 2022-06-13 14:18:16.224873
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.vars import combine_vars

    # setup mocks
    class Loader:
        def __init__(self):
            self.vars = {}

        def get_basedir(self):
            return ''

        def get_vars(self):
            return self.vars

    class LookupBase(object):

        def __init__(self):
            self._templar = Templar()
            self._loader = Loader()

        @property
        def loader(self):
            return self._loader

        @property
        def templar(self):
            return self._templar

    from ansible.template.template import Templar
    lookup_base = LookupBase()

# Generated at 2022-06-13 14:18:24.319318
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # preparations
    class FMock(dict):
        ''' Mock class to fake self.listfilter() '''
        def listfilter(self, list_name, whitelist=None, blacklist=None, expand=True, strict=False):
            return self[list_name]

    class AnsibleModuleMock(object):
        ''' Mock class to fake AnsibleModule() from ansible.module_utils '''
        def __init__(self, *args, **kwargs):
            self.run_result = kwargs.get('run_command')
        def fail_json(self, *args, **kwargs):
            return "fail_json"
        def exit_json(self, *args, **kwargs):
            return "exit_json"
        def get_bin_path(self, *args, **kwargs):
            return

# Generated at 2022-06-13 14:18:37.127709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

# Generated at 2022-06-13 14:18:47.797211
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.inventory.host import Host, Group
    from ansible.inventory.group import Group


# Generated at 2022-06-13 14:19:00.302236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=loader, sources='')
    variable_manager.set_inventory(inventory_manager)
    play_context = dict(
        loader=loader,
        variable_manager=variable_manager,
        inventory=inventory_manager
    )

    lu = LookupModule()
    lu.set_options(plugins=directory, variables=None)


# Generated at 2022-06-13 14:19:08.057649
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test-data
    terms = [
      {
        'Alice': {
          'groups': ['wheel'],
          'authorized': [
            '/tmp/alice/onekey.pub',
            '/tmp/alice/twokey.pub'
            ]
          },
        'Bob': {
          'groups': [
            'wheel',
            'staff'
            ],
          'authorized': [
            '/tmp/bob/id_rsa.pub'
            ]
          }
      },
      'authorized',
      {
        'skip_missing': False
      }
    ]

# Generated at 2022-06-13 14:19:18.670068
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    users = [
        {'name': 'alice',
         'mysql': {'password': 'mysql-password',
                   'privs': ['*.*:SELECT', 'DB1.*:ALL'],
                   'hosts': ["localhost", "127.0.0.1", "::1"]}},
        {'name': 'bob'},
        {'name': 'charly'},
    ]

    subkey = 'mysql.hosts'

    res = lm.run([users, subkey])

    assert res == [(users[0], 'localhost'), (users[0], '127.0.0.1'), (users[0], '::1')]



# Generated at 2022-06-13 14:20:01.048360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    user_alice = {
        'name': 'alice',
        'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
        'mysql': {
            'password': 'mysql-password',
            'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
            'privs': ['*.*:SELECT', 'DB1.*:ALL']
        },
        'groups': ['wheel']
    }


# Generated at 2022-06-13 14:20:09.745987
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:18.036055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants
    constants.HOST_KEY_CHECKING = False

    lookup_module = LookupModule()
    # users_vars_content is defined in test_subels_playbook
    # -*- coding: utf-8 -*-
    # {'vars': {'users': [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel'], 'mysql': {'password': 'mysql-password', 'hosts': ['%', '127.0.0.1', '::1', 'localhost'], 'privs': ['*.*:SELECT', 'DB1.*:ALL']}}, {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.

# Generated at 2022-06-13 14:20:30.315113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = LookupModule()
    terms = [
        [
            {
                "a": {"b": [1, 2, 3]},
                "x": {"y": [4, 5, 6], "z": [7, 8, 9]}
            },
            {
                "a": {"b": [10, 11, 12]},
                "x": {"y": [13, 14, 15], "z": [16, 17, 18]}
            },
            {
                "a": {"b": [19, 20, 21]},
                "x": {"y": [22, 23, 24], "z": [25, 26, 27]}
            }
        ],
        "x.y"
    ]
    result = f.run(terms, None)

# Generated at 2022-06-13 14:20:39.212029
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    module = LookupModule()
    terms = [
        {
            'rule1': {
                'host': 'host1',
                'tables': [
                    'table1',
                    'table2'
                ]
            },
            'rule2': {
                'host': 'host2',
                'tables': [
                    'table1',
                    'table2',
                    'table3'
                ]
            }
        },
        'tables'
    ]
    # when
    result = module.run(terms, None)
    # then

# Generated at 2022-06-13 14:20:51.833273
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Check the subelements lookup (in general, not with any specific set of terms)
    def check_subelements(terms, expected):
        lookup_module = LookupModule()
        assert expected == lookup_module.run(terms, None)

    # Check the subelements lookup with the given terms
    def check_subelements_with_terms(terms, expected, msg):
        lookup_module = LookupModule()
        try:
            result = lookup_module.run(terms, None)
        except:
            assert False, msg
        assert expected == result, msg

    # Run the subelements lookup with the given terms, and expect the given error message to be raised
    def check_subelements_error_with_terms(terms, msg):
        lookup_module = LookupModule()

# Generated at 2022-06-13 14:21:01.287147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class VarManager:
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    lm = LookupModule()
    lm.set_loader(None)
    lm.set_variable_manager(VarManager({'testvar': [{'name': 'joe'}, {'name': 'alice'}]}))
    assert len(lm.run([['testvar'], 'name'])) == 2
    assert len(lm.run([[{'testvar': [{'name': 'joe'}, {'name': 'alice'}]}], 'testvar.name'])) == 2

# Generated at 2022-06-13 14:21:14.065716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for method run of class LookupModule"""

    users = [
        {
            "name": "alice",
            "authorized":
            [
                "/tmp/alice/onekey.pub",
                "/tmp/alice/twokey.pub"
            ]
        },
        {
            "name": "bob",
            "authorized":
            [
                "/tmp/bob/id_rsa.pub"
            ]
        }
    ]

    lu = LookupModule()
    result = lu.run([users, 'authorized'], [], templar=None, loader=None)
    assert len(result) == 3
    assert len(result[0]) == 2
    assert isinstance(result[0][0], dict)

# Generated at 2022-06-13 14:21:21.527890
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestClass(object):
        """Used to test class LookupModule with method run
        """

        def __init__(self):
            """Init the class
            """
            self._templar = None
            self._loader = None

    class TestVar(object):
        """Used to simulate the vars
        """

        def __init__(self, value):
            """Init the class
            """
            self.value = value

        def __getitem__(self, key):
            """To simulate vars[key]
            """
            return self.value[key]

    # vars
    vars = TestVar({'test': {'subelements': ['one', 'two', 'three']}})

    # initialize the test class
    lookup = LookupModule()
    lookup._templar = TestVar({})


# Generated at 2022-06-13 14:21:32.795539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar


# Generated at 2022-06-13 14:22:51.729351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    lookup = LookupModule()
    users = [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel']},
             {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'groups': ['other']}]
    terms = [users, 'authorized']

# Generated at 2022-06-13 14:23:04.546290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import context
    from ansible.module_utils.six import BytesIO
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    lookup_module = LookupModule()
    lookup_module._templar = context.CLIARGS['module_setup']._templar
    lookup_module._loader = DataLoader()


# Generated at 2022-06-13 14:23:12.787666
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:23:24.741935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ###############################
    # init LookupModule
    ###############################
    import ansible.parsing.yaml.objects

    class FakeTemplar(object):
        def __init__(self):
            self.vars = {}

        def template(self, value):
            if isinstance(value, ansible.parsing.yaml.objects.AnsibleUnicode):
                return unicode(value)
            else:
                return str(value)

    lookup_module = LookupModule()
    lookup_module._templar = FakeTemplar()
    lookup_module._loader = None
    ###############################
