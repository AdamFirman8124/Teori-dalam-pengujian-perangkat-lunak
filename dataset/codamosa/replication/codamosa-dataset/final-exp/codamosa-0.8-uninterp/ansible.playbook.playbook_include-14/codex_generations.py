

# Generated at 2022-06-13 08:41:54.963842
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    class variable_manager:

        def __init__(self):
            self.vars = dict()

        def get_vars(self):
            return self.vars

    class loader:

        def __init__(self):
            self.basedir = '../tests/'
            self.templar = None

        def set_basedir(self, basedir):
            self.basedir = basedir

        def set_templar(self, templar):
            self.templar = templar

        def load_from_file(self, name):
            return name

    class templar:

        def __init__(self):
            self.vars = dict()

        def template(self, value):
            return value

    class play:

        def __init__(self):
            self._attributes

# Generated at 2022-06-13 08:42:07.928796
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_password = 'ansible'
    plain_text = u'foo: bar\n'
    cipher_text = b'$ANSIBLE_VAULT;1.1;AES256\n36303436653731316666313236376437343864366231396365373535636338633034393738333532\n30336462366164326662643437663933373036363837653765393564366534646633653530343338\n636466\n'
    cipher = VaultLib(vault_password)
    cipher_text = cipher.encrypt(plain_text)

# Generated at 2022-06-13 08:42:08.625127
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:19.127665
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # We have to run this func before importing ansible.template since
    # ansible/ansible#47455
    Templar._get_exception_on_undefined_error_method()

    playbook_include = PlaybookInclude()
    pb = Playbook()

    # Create fake content
    playbook = 'Test playbook'
    data = dict(
        import_playbook=playbook,
    )

    # Run load data
    result_pb = playbook_include.load_data(data, '/TestBaseDir/', VariableManager())

    assert isinstance(result_pb, Playbook)

    assert result_pb.filename is None
    assert result

# Generated at 2022-06-13 08:42:27.360799
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    data = dict(
        import_playbook = dict(
            foo = dict(
                bar = dict(
                    baz = 42
                ),
                caz = dict(
                    baz = 22
                )
            ),
            import_playbook = dict(
                foo = dict(
                    baz = 23
                )
            )
        )
    )

    expected_data = dict(
        import_playbook = 'foo',
        vars = dict(
            bar = dict(
                baz = 42
            ),
            caz = dict(
                baz = 22
            )
        )
    )

    import_ds = PlaybookInclude.preprocess_data(data)
    assert import_ds == expected_data

# Generated at 2022-06-13 08:42:33.074498
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

  #test_PlaybookInclude_load_data with None file_name
  playbook_include = PlaybookInclude()
  try:
    playbook_include.load_data('TESTING', 'TESTING', 'TESTING', None)
  except:
    pass

  #test_PlaybookInclude_load_data with file_name
  playbook_include_2 = PlaybookInclude()
  try:
    playbook_include_2.load_data('TESTING', 'TESTING', 'TESTING', 'TESTING')
  except:
    pass

# Generated at 2022-06-13 08:42:41.121402
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    test_data = dict(
        import_playbook='test_playbook_file.yml',
        test_key='test_value'
    )

    new_data = dict(
        import_playbook='test_playbook_file.yml',
        vars=dict(
            test_key='test_value'
        ),
        tags=None,
        when=None
    )

    t = PlaybookInclude()
    results = t.preprocess_data(data=test_data)

    assert results == new_data


# Generated at 2022-06-13 08:42:54.426753
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Test case 1: check if a playbook is loaded
    '''

    # We need a fake playbook that we can use for our test
    playbook_data = {}
    playbook_data['plays'] = []

    # We create a play obj
    play_data = {}
    play_data['playbook'] = 'test_playbook'
    play_data['name'] = 'test_play_name'
    play_data['included_vars'] = {}
    playbook_data['plays'].append(play_data)

    # We'll need a fake variable manager to make the fake playbook work
    variable_manager_data = {}

    # We need a fake loader to make the fake variable manager work
    loader_data = {}

    # Create the fake playbook
    pb = Playbook(loader=loader_data)
    pb

# Generated at 2022-06-13 08:43:06.395417
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert PlaybookInclude.load('- import_playbook: test_name.yml')\
        .load_data(ds='- import_playbook: test_name.yml', basedir='/some/path/to/playbook',
                   loader=None, variable_manager=None)._load_playbook_data\
        .call_count == 1
    assert PlaybookInclude.load('- import_playbook: test_name.yml')\
        .load_data(ds='- import_playbook: test_name.yml', basedir='/some/path/to/playbook', loader=None,
                   variable_manager=None)._set_loader_basedir\
        .call_count == 1
    assert PlaybookInclude.load('- import_playbook: test_name.yml')\
       

# Generated at 2022-06-13 08:43:08.442321
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:27.239400
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # load_data() returns a Playbook object with modified Plays
    pbi = PlaybookInclude()
    pb_obj = pbi.load_data({'import_playbook': 'pb1', 'tags': 'tag1'}, '')
    assert isinstance(pb_obj, Playbook)
    assert len(pb_obj._entries) == 1
    assert isinstance(pb_obj._entries[0], Play)
    assert pb_obj._entries[0].tags == ['tag1']

# Generated at 2022-06-13 08:43:27.887862
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:29.088448
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:43:29.740985
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:35.708725
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import json
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    class Options(object):
        connection = 'local'
        module_path = '/usr/share/ansible'
        forks = 10
        remote_user = 'vagrant'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = 'sudo'
        become_user = 'root'
        verbosity = 1
        check = False
        diff = False

# Generated at 2022-06-13 08:43:48.466419
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    # PlaybookInclude.load_data() is a class method and we use it as instance method
    # to not have to mock all of PlaybookInclude to get an instance of it
    task = PlaybookInclude()

    # pretend that the playbook to load contains a single play with an empty task
    task_name = 'foobar'
    fields = {'tasks': [{'name': task_name}]}
    data = {'import_playbook': 'playbook_in_memory.yml'}
    playbook = Playbook.load(data, '.')
    playbook.dump('playbook_in_memory.yml')

    # now load this play into our PlaybookInclude instance
    result = task.load_data(data, '.')

    # check that the result is a

# Generated at 2022-06-13 08:43:58.648068
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import tempfile
    import yaml
    from ansible.parsing import vault
    from ansible.parsing.yaml import objects
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # file with vault secret
    (fd, vault_secret_file) = tempfile.mkstemp()
    os.write(fd, b"123")
    os.close(fd)

    # test playbook
    (fd, playbook) = tempfile.mkstemp()
    os.write(fd, b"include_playbook: import_playbook.yml\nvars_file: vars_file.yml")
    os.close(fd)

    # the playbook to import

# Generated at 2022-06-13 08:44:14.158408
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    import ansible.constants as C

    C._action_plugins = []
    C._lookup_plugins = []
    C._cache_plugins = []
    C._connection_plugins = []
    C._filter_plugins = []
    C._test_plugins = []
    C._terminal_plugins = []
    C._loader_plugins = []
    C._stdout_plugins = []

    from ansible.playbook.play import Play


# Generated at 2022-06-13 08:44:24.859480
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler_include import HandlerInclude
    from ansible.playbook.hosts import Hosts

    #Test if returned type is Playbook
    pb1 = PlaybookInclude().load_data('test_pb', '.')
    assert isinstance(pb1, Playbook)

    #Test if returned type is Playbook
    pb2

# Generated at 2022-06-13 08:44:36.958841
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook

    # First test when we don't have a collection
    # We need to create a fake playbook

    # First test when we don't have a collection
    file_name = "../ansible/test/units/include/test_config.yml"
    pb = PlaybookInclude(loader=None)
    pb.import_playbook = file_name
    result = pb.load_data(ds=pb, basedir="./test/units/include/", variable_manager=None, loader=None)

    assert isinstance(result, Playbook)
    assert len(result._entries) == 1
    assert isinstance(result._entries[0], PlaybookInclude)
    assert result._entries[0].import_playbook == "test_config.yml"

    #

# Generated at 2022-06-13 08:44:51.701446
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Set up the object
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    import ansible.playbook.role.include as role_include
    m_loader = None
    m_basedir = "."
    m_variable_manager = None
    m_ds = dict()
    m_ds["import_playbook"] = "test_include"

    m_pb = PlaybookInclude()
    m_pb = m_pb.load_data(m_ds, m_basedir, m_variable_manager, m_loader)

    # Test result object

# Generated at 2022-06-13 08:45:01.688260
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    # Test loading not FQCN playbook path
    playbook = '../test_playbook_vars.yaml'
    mock_variable_manager = dict()

    test_obj = PlaybookInclude.load(
        data=dict(
            import_playbook=playbook,
        ),
        basedir='',
        variable_manager=mock_variable_manager,
    )

    assert isinstance(test_obj, Play)
    test_obj_vars = test_obj.vars
    assert test_obj_vars == {
        'qwerty': "456",
        'asdfg': "123",
    }

    # Test loading FQCN playbook path
    playbook = 'ansible.posix.file.copy'
    mock_variable_manager = dict()

# Generated at 2022-06-13 08:45:09.073851
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    variable_manager = "variable_manager"
    loader = "loader"
    basedir = "basedir"

    fake_self = "fake_self"
    fake_ds = {"k": "v"}
    assert isinstance(PlaybookInclude.preprocess_data(fake_self, fake_ds), AnsibleMapping)

    fake_self = PlaybookInclude()
    fake_ds = {"k": "v"}
    assert isinstance(PlaybookInclude.preprocess_data(fake_self, fake_ds), AnsibleMapping)

    fake_self = PlaybookInclude()
    fake_ds = {"import_playbook": "fake_import_playbook"}
    assert isinstance(PlaybookInclude.preprocess_data(fake_self, fake_ds), AnsibleMapping)

    fake_self = PlaybookIn

# Generated at 2022-06-13 08:45:19.392504
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import sys
    sys.path.append("../..")
    # Define the variables
    playbook_include = PlaybookInclude()

    # Create data type object
    empty_ds = AnsibleMapping()
    none_ds = AnsibleMapping()
    none_ds['import_playbook'] = None
    basic_ds = AnsibleMapping()
    basic_ds['import_playbook'] = "file.yml"
    basic_ds['vars'] = {'param1': 'value1'}
    dict_ds = AnsibleMapping()
    dict_ds['import_playbook'] = {'param1': 'value1'}
    dict_ds['vars'] = {'param2': 'value2'}
    dict_ds['tags'] = 'tag1,tag2'

# Generated at 2022-06-13 08:45:32.257879
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    def _load(data, expected, loader=None):
        pii = PlaybookInclude()
        pb = pii.load_data(data, '/', loader=loader)
        if expected[0] is not None:
            assert pb._entries[0]._included_path == expected[0]
        if expected[1] is not None:
            assert pb._entries[0].vars == expected[1]
        if expected[2] is not None:
            assert pb._entries[0].tags == expected[2]
        if expected[3] is not None:
            assert pb._entries[0]._included_conditional == expected[3]

    # 0. include with extra vars and tags

# Generated at 2022-06-13 08:45:39.645722
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    from ansible.parsing.yaml.data import AnsibleUnicode

    data = AnsibleMapping(data={
        'import_playbook': AnsibleUnicode('playbook1.yml'),
        'vars': AnsibleMapping(data={'foo': 'bar'}),
        'tags': AnsibleUnicode('tag1')
    })
    expected = AnsibleMapping(data={
        'import_playbook': 'playbook1.yml',
        'vars': {'foo': 'bar'},
        'tags': 'tag1',
    })
    playbook_include = PlaybookInclude()
    actual = playbook_include.preprocess_data(data)
    assert actual == expected

# Generated at 2022-06-13 08:45:52.337975
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    There are a number of places in the code that override load_data
    to take a different approach to doing the normal preprocessing.
    This test is designed to make sure that they actually work by
    overriding it with a function that returns a different class
    and make sure the return object is of the expected type.
    '''
    class MockLoader():
        class templates():
            class templar:
                class basedir:
                    test = "test"
    temp_load_data = PlaybookInclude.load_data
    PlaybookInclude.load_data = lambda self,ds, basedir=None, variable_manager=None, loader=None: 'MockedOut'
    temp_preprocess_data = PlaybookInclude.preprocess_data
    PlaybookInclude.preprocess_data = lambda self,ds: ds
   

# Generated at 2022-06-13 08:45:53.973210
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pb = PlaybookInclude()
    assert pb is not None

# Generated at 2022-06-13 08:46:08.943204
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # import here to avoid a dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # prepare args to simulate data in a playbook
    basedir = '/path/to/playbook'

    # create test object
    pb_include = PlaybookInclude()

    # create dummy class to test the loader
    class DummyLoader:
        def get_basedir(self):
            return basedir

    loader = DummyLoader()

    # create dummy class to test the variable manager
    class DummyVars:
        def get_vars(self):
            return {'test_var': 'test_value'}

    variable_manager = DummyVars()

    # simulate ansible dump data

# Generated at 2022-06-13 08:46:19.399658
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    playbook_include = PlaybookInclude()
    playbook_include.load_data({
        'import_playbook': 'test_playbook.yml',
        'when': 'test_condition',
        'tags': 'test_tag'
    })
    assert playbook_include.import_playbook == 'test_playbook.yml'
    assert playbook_include.when == ['test_condition']
    assert playbook_include.tags == ['test_tag']


# Generated at 2022-06-13 08:46:34.939404
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import playbook by FQCN
    playbook_collection_path = 'namespace.collection/playbooks/playbook.yml'
    import_playbook = 'collection:' + playbook_collection_path
    pbi = PlaybookInclude()
    pbi.import_playbook = import_playbook
    pb = pbi.load_data(None, None, None, None)  # dont care about the pb, only side effects of load_data
    collection_name = _get_collection_name_from_path(playbook_path=playbook_collection_path)
    assert collection_name == 'namespace.collection', 'incorrect collection name'
    assert AnsibleCollectionConfig.playbook_paths[0].endswith('namespace/collection/playbooks'), 'incorrect playbook paths'
    assert AnsibleCollectionConfig.default_

# Generated at 2022-06-13 08:46:45.717123
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task.include import IncludeTask
    from ansible.playbook.task.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude

    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task.include
    import ansible.playbook.task.task
    import ansible.playbook.task_include
    import ansible.playbook.role.include

    # Note: This does not test the full functionality of this class, only the
    # main functionality that is being tested for the sake of coverage.
    mock_loader = object()
    mock_variable_manager = object()

# Generated at 2022-06-13 08:46:59.410545
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    playbook_content = '''
    - hosts: localhost
      vars:
        a_var: true
      tasks:
        - debug:
            var: a_var
        - debug:
            var: b_var
    '''

    ds = {'import_playbook': 'playbook.yaml',
          'vars': {'b_var': False}}

    with tempfile.NamedTemporaryFile(mode='wt') as tf:
        tf.write(playbook_content)
        tf.flush()
        ds['import_playbook'] = tf.name
        variable_manager = VariableManager()
        dl = DataLoader()
        pb = PlaybookIn

# Generated at 2022-06-13 08:47:11.275363
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    import ansible.playbook.playbook
    from units.mock.loader import DictDataLoader

    input_data = dict(
        import_playbook='test1.yaml',
        when=['we_condition'],
        tags=['we_tag'],
        vars=dict(
            some_param='some_value'
        )
    )
    basedir = '/tmp'
    p = PlaybookInclude.load(input_data, basedir)
    assert p.import_playbook == 'test1.yaml'
    assert p.tags == input_data['tags']
    assert p.when == input_data['when']
    assert p.vars == input_data['vars']


# Generated at 2022-06-13 08:47:23.409097
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.plugins import callback_loader
    import json
    import os

    # 初始化回调对象
    callback = callback_loader.get('json')
    # 初始化加载器对象，并设置 DataLoader 的路径
    loader = DataLoader()
    loader.set_basedir(os.getcwd())

    # 设置变量管理器
    variable_manager = VariableManager()
    # 设置变量
    variable

# Generated at 2022-06-13 08:47:28.372773
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    pbi = PlaybookInclude()
    pbi.vars = {'keyA': 'valueA'}
    pbi.import_playbook = 'myfile.yml'
    pbi.tags = ['tagA']
    pbi.when = ['A is true']

    pb = pbi.load_data(pbi.serialize(), '/tmp')

    assert len(pb._entries) == 1
    assert pb._entries[0].vars == {'keyA': 'valueA'}
    assert pb._entries[0].tags == ['tagA']
    assert pb._entries[0].when == ['A is true']

    pbi.vars = {'keyB': 'valueB', 'tags': 'tagB'}

# Generated at 2022-06-13 08:47:40.683748
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost']))

    basedir = os.path.dirname(__file__) + '/../../data/playbook_include_test'
    playbook_path = os.path.join(basedir, 'playbook.yml')

    ds1 = AnsibleMapping()
    ds1['import_playbook'] = 'test1.yml'
    ds1['vars'] = AnsibleMapping()
    ds1['vars']['test1'] = 'test1'

    ds2 = Ans

# Generated at 2022-06-13 08:47:50.872126
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    mock_data = {
        u'include': u'../collection/pass/playbook.yml',
        u'vars': {
            u'test': u'Hello',
            u'my_host': u'{{ hostname }}'
        }
    }
    mock_file_name = u'../collection/pass/playbook.yml'
    mock_basedir = u'/tmp/test'
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

# Generated at 2022-06-13 08:48:03.602838
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # import here to avoid a dependency loop
    from ansible.parsing.yaml.objects import AnsibleMapping

    # tests

# Generated at 2022-06-13 08:48:15.132919
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook_include import PlaybookInclude

    # Test the case where an exception is raised because import_playbook is missing
    test_dict = {}
    try:
        PlaybookInclude.load(test_dict, "")
        raise RuntimeError("AnsibleAssertionError was not raised")
    except AnsibleAssertionError:
        pass

    # Test the case where an exception is raised because import_playbook is None
    test_dict = {'import_playbook': None}
    try:
        PlaybookInclude.load(test_dict, "")
        raise RuntimeError("AnsibleParserError was not raised")
    except AnsibleParserError:
        pass

    # Test the case where an exception is raised because import_playbook is not a string

# Generated at 2022-06-13 08:48:29.539878
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Test the case of dict parameter ds with keys 'import_playbook' and 'vars'
    ds = dict(import_playbook='playbook.yml', vars=dict())
    res = PlaybookInclude.preprocess_data(None, ds)
    assert ds == res

    # Test the case of dict parameter ds with keys 'include', 'tags' and 'vars'
    ds = dict(import_playbook='playbook.yml', tags='tag1',vars=dict())
    res = PlaybookInclude.preprocess_data(None, ds)
    assert ds == res

    # Test the case of dict parameter ds with keys 'import_playbook' and 'import_playbook_roles'

# Generated at 2022-06-13 08:48:36.835486
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    # Import test_utils so that we can use it to setup ansible path
    test_utils_path = os.path.join(os.path.dirname(__file__), 'test_utils')
    sys.path.insert(0, test_utils_path)
    from test_utils import setup_ansible_module_path

    try:
        import ansible.constants as C
        import ansible.inventory.host
        import ansible.parsing.dataloader
        import ansible.template
        import ansible.vars.manager
    except ImportError:
        raise AssertionError("Failed to import ansible modules")

    setup_ansible_module_path()

    # initialize PlaybookInclude
    playbook_include = PlaybookInclude()

    # Initialize Ansible

# Generated at 2022-06-13 08:48:38.976043
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Needs to be further updated
    assert False



# Generated at 2022-06-13 08:48:50.151704
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = dict(a=5, import_playbook='test_playbook')
    assert PlaybookInclude.preprocess_data(ds) == dict(import_playbook='test_playbook', a=5)

    ds = dict(import_playbook='test_playbook var1=val1 var2=val2')
    assert PlaybookInclude.preprocess_data(ds) == dict(import_playbook='test_playbook',
                                                      vars=dict(var1='val1', var2='val2'))
    ds = dict(import_playbook='test_playbook var1="val1 val2"')

# Generated at 2022-06-13 08:48:50.698782
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:48:58.759760
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    p = Playbook()
    foo_task_list = [dict(action=dict(module='raw', args='echo foo'))]
    bar_task_list = [dict(action=dict(module='raw', args='echo bar'))]
    p.load(dict(hosts='all', name='foo', tasks=foo_task_list), variable_manager=VariableManager(), loader=None)
    p.load(dict(hosts='all', name='bar', tasks=bar_task_list), variable_manager=VariableManager(), loader=None)

    variable_manager = VariableManager()

# Generated at 2022-06-13 08:49:12.771209
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    This is a unit test for the load_data method of the PlaybookInclude class.
    '''
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.yaml import YAML

    from io import StringIO
    from os import path
    from tempfile import mkdtemp

    collection1_dir = mkdtemp()
    collection2_dir = mkdtemp()


# Generated at 2022-06-13 08:49:28.171898
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    basedir = module.get_bin_path()
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(host='host1')
    ds = dict(import_playbook='include.yml', tags=dict(one=1, two=2))

    # Include a data structure (ds) to load with "load_data()" method
    playbook_include = PlaybookInclude()
    pb = playbook_include.load_data(ds=ds, basedir=basedir, variable_manager=variable_manager, loader=loader)

    # test that the imported model is a Playbook object
    assert type(pb) is Playbook
    # test that the imported

# Generated at 2022-06-13 08:49:36.788805
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Understand why the mocking is done, and add explanation here
    # and potentially move mocking library outside the unit test file.
    # TODO: Understand why the mocking is done, and add explanation here
    # and potentially move mocking library outside the unit test file.
    class Mock():
        def __init__(self, ansible_pos=None, data='test_data', basedir='/etc/test', variable_manager=None, loader=None):
            self.ansible_pos = ansible_pos
            self.data = data
            self.basedir = basedir
            self.variable_manager = variable_manager
            self.loader = loader
        def get_vars(self):
            return self.variable_manager

    from ansible.module_utils import basic
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 08:49:49.363317
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Test ds is not an instance of dict
    ds = []
    try:
        PlaybookInclude.load(data=ds, basedir='.')
    except AnsibleAssertionError as e:
        assert to_bytes(e) == "ds ([]) should be a dict but was a <type 'list'>"

    # Test ds contains no import_playbook key
    ds = {'vars': {'foo': 'bar'}}
    try:
        PlaybookInclude.load(data=ds, basedir='.')
    except AnsibleAssertionError as e:
        assert to_bytes(e) == 'No playbook given to "import_playbook"'

    # Test ds contains multiple import_playbook keys
   

# Generated at 2022-06-13 08:50:07.711408
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds1 = dict(
        import_playbook='foo/bar/baz.yml'
    )
    pbi = PlaybookInclude()
    pbi.load_data(ds1, 'no_basedir')
    assert pbi.import_playbook == 'foo/bar/baz.yml'

    ds2 = dict(
        import_playbook=dict(
            file='foo/bar/baz.yml',
            name='baz'
        )
    )
    pbi = PlaybookInclude()
    pbi.load_data(ds2, 'no_basedir')
    assert pbi.import_playbook == 'foo/bar/baz.yml'


# Generated at 2022-06-13 08:50:17.585866
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("test_PlaybookInclude_load_data")

    import json
    import ansible.playbook.play

    all_vars = {'foo': 'bar'}

    # define an instance
    pi = PlaybookInclude()

    # define a datastructure
    ds = '''
---
- import_playbook: include.yml
  variables:
    foo: foo
    tags: test
    var1: 1
  when: foo
'''
    ds = json.loads(ds)
    assert isinstance(ds, dict)

    # load the datastructure
    pb = pi.load_data(ds, '', variable_manager='', loader='')

    # validate the playbook object
    assert isinstance(pb, ansible.playbook.playbook.Playbook)

    # validate the

# Generated at 2022-06-13 08:50:29.931838
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    This method uses the unittest framework to test the load_data method of the PlaybookInclude class
    """

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import unittest

    test = unittest.TestSuite()

    #Create a PlaybookInclude instance
    playbook_include = PlaybookInclude()


    #Test case: ds is not a dictionary
    ds = "string"
    ret = playbook_include.load_data(ds, basedir='.')
    test.addTest(unittest.makeSuite(TypeError))

    #Test case: ds is a dictionary
    ds = {'k': 'v'}
    ret = playbook_include.load_data(ds, basedir='.')

# Generated at 2022-06-13 08:50:40.752934
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook, Play

    playbook_include = PlaybookInclude()

    # Test for AnsibleParserError for playbook import parameter is missing
    input_ds = dict(TEST="Value")
    with pytest.raises(AnsibleParserError):
        playbook_include.load_data(ds=input_ds, basedir='/path')

    # Test for AnsibleParserError for playbook import statements must specify the file name to import
    input_ds = dict(import_playbook="")
    with pytest.raises(AnsibleParserError):
        playbook_include.load_data(ds=input_ds, basedir='/path')

    # Test for AnsibleParserError for playbook import parameter must be a string
    input_ds = dict(import_playbook=dict())

# Generated at 2022-06-13 08:50:50.485956
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Testing PlaybookInclude.load_data()
    import ansible.playbook.play

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # Basic test-case of creation and load_data()
    #
    # Create an instance of the PlaybookInclude class
    # (PlaybookInclude is an AnsibleBaseYAMLObject due to its use of
    # the FieldAttribute base class)
    include = PlaybookInclude()
    assert isinstance(include, PlaybookInclude)

    # Load a YAML fragment of data into the object
    #
    # Load the data into the object from YAML, but don't check the
    # generated data structure (check_ds=False) as that is tested in
    # test_PlaybookInclude_preprocess_data

# Generated at 2022-06-13 08:51:03.727763
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    pb_entry = PlaybookInclude()

    pb = Playbook()
    pb._load_playbook_data(file_name=['test/unit/lib/ansible/playbook/fixtures/pb_include_simple.yml'], variable_manager=None, vars=dict())

    assert pb._entries[0]._included_path == 'test/unit/lib/ansible/playbook/fixtures'

    # Test simple.yml with vars
    pb = Playbook()

# Generated at 2022-06-13 08:51:06.654159
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert PlaybookInclude.load({'import_playbook': 'pb2.yml', 'vars': {'a': 'A'}})

# Generated at 2022-06-13 08:51:18.678591
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.vars import combine_vars

    ds = dict(
        import_playbook='this/is/my.yml',
        vars=dict(
            alpha='varalpha',
            bravo='varbravo',
        ),
        tags=['tag1', 'tag2'],
    )

    templar = Templar(variables=dict(alpha='varalpha', bravo='varbravo'))
    basedir = '/this/is/my/playbook.yml'
    vars_manager = VariableManager()

    f = PlaybookInclude()

# Generated at 2022-06-13 08:51:29.226634
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Test 'preprocess_data' method of class PlaybookInclude with # parameters equal to 1
    data_input = {'include': 'testPlaybook'}
    data_output = {'import_playbook': 'testPlaybook', 'vars': {}}
    test_playbook_include = PlaybookInclude()
    assert test_playbook_include.preprocess_data(data_input) == data_output

    # Test 'preprocess_data' method of class PlaybookInclude with # parameters greater than 1
    data_input = {'include': 'testPlaybook param1=value1'}
    data_output = {'import_playbook': 'testPlaybook', 'vars': {'param1': 'value1'}}
    test_playbook_include = PlaybookInclude()

# Generated at 2022-06-13 08:51:40.491988
# Unit test for method preprocess_data of class PlaybookInclude