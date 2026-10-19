

# Generated at 2022-06-13 03:02:06.317935
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    params = dict(
        fact_path="test_facts_path"
    )

    config = dict(
        module_utils=dict(
            basic=dict(
                _AnsibleModule=dict(
                    params=params
                )
            )
        )
    )

    from ansible.module_utils.facts.collector import get_collector_instance
    local_fact_collector = get_collector_instance('local', config=config)
    # test normal execution
    test_result = local_fact_collector.collect()
    assert type(test_result) is dict
    assert 'local' in list(test_result.keys())
    assert type(test_result['local']) is dict
    assert type(test_result['local']['test_fact']) is dict
    assert 'test' in list

# Generated at 2022-06-13 03:02:07.695201
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'

# Generated at 2022-06-13 03:02:18.479662
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # Make sure there is some exception or error thrown
    # as soon as the constructor is called
    module_args = {
        'fact_path': None
    }

    setattr(module_args, '_ansible_debug', True)
    setattr(module_args, '_ansible_verbosity', 3)

    locals()['AnsibleModule'] = MockAnsibleModule()
    locals()['AnsibleModule'].params = module_args
    locals()['AnsibleModule'].run_command = run_command

    _local = LocalFactCollector()
    _local.collect()

    # This case should not reach here
    assert False



# Generated at 2022-06-13 03:02:21.217413
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_fact_collector = LocalFactCollector()
    local_fact_collector.collect('fact_path')
    local_fact_collector.collect()

# Generated at 2022-06-13 03:02:34.156446
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Here we create a mock of module class
    class MockModule():
        params = {'fact_path': '/path/to/something'}

        class RunCommand():
            def __call__(self, fact_path):
                return 0, json.dumps({'name': 'Ansible'}), ""

        run_command = RunCommand()

    module = MockModule()

    # Here we create a mock of collected_facts class
    class MockCollector():
        def __init__(self):
            pass

    collected_facts = MockCollector()

    # Create instance of LocalFactCollector class
    fact_collector_instance = LocalFactCollector()
    local_facts = fact_collector_instance.collect(module, collected_facts)

# Generated at 2022-06-13 03:02:42.372317
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    '''Unit test for method collect of class LocalFactCollector.'''
    from ansible.module_utils.facts.collector import TestModule
    module = TestModule()
    fact_path = os.path.join(os.path.dirname(__file__), "../../../../test/units/module_utils/local_facts/")
    module.params['fact_path'] = fact_path
    local_fact_collector = LocalFactCollector()
    facts = local_fact_collector.collect(module=module)
    assert(facts['local']['one_fact']['value'] == 'one_value')
    assert(facts['local']['two_facts']['two_value']['nested_fact'] == 'nested_value')

# Generated at 2022-06-13 03:02:45.477263
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:02:53.328088
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = type('', (), {})()
    module.params = lambda: None
    module.params.__getitem__ = lambda x, y: None
    module.params.get = lambda x, y: None
    module.warn = lambda x: None
    module.run_command = lambda x: 0

    local_facts = {}
    local_facts['local'] = {}

    fact_path = 'tests/unit/module_utils/facts/local._mock'
    local = {}
    # go over .fact files, run executables, read rest, skip bad with warning and note
    for fn in sorted(glob.glob(fact_path + '/*.fact')):
        # use filename for key where it will sit under local facts
        fact_base = os.path.basename(fn).replace('.fact', '')
       

# Generated at 2022-06-13 03:02:59.512285
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    """Test method of LocalFactCollector class to return a dictionary of all
    custom facts.
    """
    mock_module = Mock()
    mock_module.params = {'fact_path': './test_facts'}
    mock_module.run_command.return_value = (0, 'out', 'err')

    expected_facts = {
        'local': {
            'one': {
                'section': {
                    'a': '1',
                    'b': '2',
                }
            },
            'two': {
                'section': {
                    'c': '3',
                    'd': '4',
                }
            },
            'three': {
                'section': {
                    'e': '5',
                    'f': '6',
                }
            },
        },
    }

   

# Generated at 2022-06-13 03:03:01.353748
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts_collector = LocalFactCollector()
    assert local_facts_collector.name == 'local'

# Generated at 2022-06-13 03:03:13.999796
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Concrete AnsibleModule mock
    class AnsibleModuleMock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, cmd):
            import subprocess
            cmd = cmd.replace('$', '\\$')
            process = subprocess.Popen(['bash', '-c', cmd], close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (stdout, stderr) = process.communicate()
            stdout = to_text(stdout, errors='surrogate_or_strict')
            stderr = to_text(stderr, errors='surrogate_or_strict')
            return process.returncode, stdout, stderr


# Generated at 2022-06-13 03:03:16.165902
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert type(lfc.collect()) == dict


# Generated at 2022-06-13 03:03:18.681755
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    '''Unit test for method collect of class LocalFactCollector'''
    local_fact_collector = LocalFactCollector()
    local_fact_collector.collect()

# Generated at 2022-06-13 03:03:20.519166
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    cls = LocalFactCollector()
    assert cls.name == 'local'
    assert cls._fact_ids == set()


# Generated at 2022-06-13 03:03:31.035769
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = MockModule()
    module.params = { 'fact_path': '/home/facts' }
    c = LocalFactCollector(module=module)
    c._fact_ids = { 'foo' }
    result = c.collect()
    assert 'local' in result
    assert result['local'] == {}
    assert result['foo'] == {}

    # init the module again with a fake fact path (for testing)
    module.params = { 'fact_path': 'tests/unit/module_utils/facts/local_facts/fact_path' }

    # test some executables that are not executable
    module.warn.reset_mock()
    result = c.collect()
    assert result['local'] == {}
    assert result['foo'] == {}
    assert len(module.warn.mock_calls) == 1
   

# Generated at 2022-06-13 03:03:32.626171
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_collector = LocalFactCollector()
    assert fact_collector.name == 'local'

# Generated at 2022-06-13 03:03:40.152196
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={})
    module.params = {}
    module.params['fact_path'] = ''
    module.run_command = None

    if os.path.exists(module.params['fact_path']):
        fc = LocalFactCollector()
        assert fc.name == 'local'
        assert fc._fact_ids == set()
        assert fc.collect(module)
    else:
        print("%s doesn't exist. Test aborted" % module.params['fact_path'])

# Generated at 2022-06-13 03:03:42.994003
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()
    assert local_fact_collector.collect() == {'local': {}}


# Generated at 2022-06-13 03:03:43.660627
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local != None

# Generated at 2022-06-13 03:03:44.525185
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'

# Generated at 2022-06-13 03:04:07.621943
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import MWrapper
    from ansible.module_utils._text import to_text

    def fake_get_file_content(fn, default=''):
        if to_text(fn).endswith('non_existing.fact'):
            raise Exception("Non existent file")
        return '''
[main]
path = /home/user
'''
    # fake_module=MWrapper has the same attributes as ansible.module_utls.basic.AnsibleModule
    # but allows to define additional attributes
    fake_module = MWrapper(basic.AnsibleModule(
        argument_spec=dict(fact_path=dict(type='str')),
        supports_check_mode=True))

# Generated at 2022-06-13 03:04:08.943415
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'

# Generated at 2022-06-13 03:04:09.809184
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    assert False, "Need to write unit tests"

# Generated at 2022-06-13 03:04:13.704278
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:04:16.679114
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    ''' Unit test for constructor of class LocalFactCollector '''
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector is not None
    return True

# Generated at 2022-06-13 03:04:21.505454
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    config_dict = {
        'fact_path': '/etc/ansible/facts.d'
    }

    lf_collector = LocalFactCollector(config=config_dict, interceptor=None)
    assert lf_collector.name == 'local'
    assert isinstance(lf_collector._fact_ids, set)
    assert lf_collector._fact_ids == set()
    assert lf_collector.config == config_dict

# Generated at 2022-06-13 03:04:27.064273
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # pylint: disable=protected-access
    """ Check that creating new instance of LocalFactCollector class without errors.
    """
    if 'darwin' not in __file__:
        # TODO: Fix for OSX.
        local = LocalFactCollector()
        assert local._name == 'local'
        assert len(local._fact_ids) == 0

# Generated at 2022-06-13 03:04:28.729226
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_fact_collector = LocalFactCollector()
    local_fact_collector.collect()

# Generated at 2022-06-13 03:04:32.430770
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = '.'
    module = 'test'
    facts = LocalFactCollector(module, fact_path)
    assert facts.name == 'local'
    assert facts._fact_ids == set()
    assert facts.module is module
    assert facts.fact_path == fact_path

# Generated at 2022-06-13 03:04:38.743135
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import pytest
    import glob
    import os

    # Read the file structure

    # Create a local fact_path directory
    test_dir = './local_facts_dir'
    if os.path.isdir(test_dir):
        for filename in glob.glob(os.path.join(test_dir, '*')):
            os.remove(filename)
        os.rmdir(test_dir)
    os.mkdir(test_dir)
    # Create a json-formated fact file
    with open(os.path.join(test_dir, 'fact1.fact'), 'w') as jsonfile:
        jsonfile.write('{"key": "value"}')
    # Create a json-formated fact with invalid syntax

# Generated at 2022-06-13 03:05:12.063604
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collectors.local import LocalFactCollector
    from ansible.module_utils.facts.utils import mock_get_file_content
    from ansible.module_utils.facts.utils import mock_exists


    with mock.patch("ansible.module_utils.facts.collectors.local.os.path.exists", mock_exists(True)):
        with mock.patch("ansible.module_utils.facts.utils.get_file_content", mock_get_file_content('{"some": "fact", "stuff": "here"}')):
            local_collector = LocalFactCollector()
            results = local_collector.collect()
            assert results == {"local": {"test": {"some": "fact", "stuff": "here"}}}


# Generated at 2022-06-13 03:05:12.933878
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:05:14.875861
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    result = LocalFactCollector()

    assert result.name == 'local'
    assert result._fact_ids == set()


# Generated at 2022-06-13 03:05:16.441293
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    helper = BaseFactCollector(None)
    assert isinstance(helper, BaseFactCollector)

# Generated at 2022-06-13 03:05:17.991141
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    assert LocalFactCollector._fact_ids == set()



# Generated at 2022-06-13 03:05:20.349935
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:05:21.546081
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    obj = LocalFactCollector()
    assert obj
    assert obj.name == 'local'

# Generated at 2022-06-13 03:05:24.290331
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    m = AnsibleModule(argument_spec={'fact_path':{'type':'path','required':True}})
    obj = LocalFactCollector()
    obj.collect(m)

# Generated at 2022-06-13 03:05:25.107585
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector().name == 'local'

# Generated at 2022-06-13 03:05:27.964961
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert bool(lfc) == True
    assert lfc.name == 'local'
    assert isinstance(lfc._fact_ids, set)
    assert bool(lfc._fact_ids) == False

# Generated at 2022-06-13 03:06:35.549309
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:06:36.946728
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lc = LocalFactCollector()
    assert lc.name == 'local'
    assert not lc._fact_ids

# Generated at 2022-06-13 03:06:50.714122
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule
    import ansible.module_utils.facts.collectors.local

    module = AnsibleModule(argument_spec={'fact_path':dict(type='path', default='/tmp/facts')})
    ansible.module_utils.facts.collectors.local.LocalFactCollector().collect(module)
    assert module.params['fact_path'] == '/tmp/facts'
    assert module.run_command == module.run_command
    assert module.warn == module.warn


# Generated at 2022-06-13 03:06:51.835016
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    localFact = LocalFactCollector()
    assert localFact.name == 'local'

# Generated at 2022-06-13 03:06:57.317373
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils import basic

    # Create a fake module
    module = basic.AnsibleModule(argument_spec={
        'fact_path': {'required': True, 'type': 'path'},
    })

    module.params['fact_path'] = os.path.join(os.path.dirname(__file__), 'fixtures', 'local_facts')
    module.run_command = lambda x: (0, '{"foo": "bar"}\n', '')
    expected = {
        'local': {
            'executable': {'foo': 'bar'},
            'text': {'foo': 'bar'},
        }
    }

    fact_collector = LocalFactCollector()
    collected_facts = fact_collector.collect(module, collected_facts={})


# Generated at 2022-06-13 03:06:58.683474
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector is not None

# Generated at 2022-06-13 03:07:02.981522
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import ansible.module_utils.facts.transform
    module = ansible.module_utils.facts.transform._AnsibleModuleStub()
    module.params = {'fact_path': '.'}
    LFC = LocalFactCollector(module)
    assert isinstance(LFC.collect(), dict)


# Generated at 2022-06-13 03:07:04.882549
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    c = LocalFactCollector()
    assert 'local' == c.name
    assert c._fact_ids == set()


# Generated at 2022-06-13 03:07:12.487582
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import sys
    sys.path.append('/')
    
    import collections
    import stat
    
    import ansible.module_utils.facts.collectors.local
    import ansible.module_utils.facts.utils
    import ansible.module_utils.facts
    import ansible.module_utils.common.process
    
    class MockModule():
        class Warnings():
            def append(self, val):
                pass
        def __init__(self):
            self.params = collections.defaultdict(lambda: None)
            self.warnings = self.Warnings()
        def warn(self, fact):
            self.warnings.append(fact)
        def run_command(self, fn):
            return 0, '', ''
    

# Generated at 2022-06-13 03:07:22.136390
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import os
    import tempfile

    basedir = os.path.join(tempfile.gettempdir(), 'ansible_test_local_fact_path')
    os.mkdir(basedir, 0o700)

# Generated at 2022-06-13 03:10:06.548218
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_collector = LocalFactCollector()
    assert local_collector.name == 'local'
    assert local_collector._fact_ids == set()

# Generated at 2022-06-13 03:10:08.970272
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    c = LocalFactCollector()
    assert c.name == 'local'
    assert c._fact_ids is None

# Generated at 2022-06-13 03:10:17.367420
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Configure the parameters that would be returned by the AnsibleModule
    params = {
        'fact_path': '/tmp/facts'
    }

    # Configure the AnsibleModule with the parameters that would be returned by the AnsibleModule
    module = AnsibleModule(argument_spec=dict(params))

    # Setup a file to be used as the fact path
    fact_path = mkdtemp()
    fact_file = fact_path + '/test.fact'
    fact_content = 'test_fact: test_value'


# Generated at 2022-06-13 03:10:22.525490
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts import ansible_collected_facts
    from ansible.module_utils.facts.collector.local import LocalFactCollector
    import shutil
    import tempfile
    import json

    test_dir = tempfile.mkdtemp()
    test_dir1 = tempfile.mkdtemp()
    test_dir2 = tempfile.mkdtemp()
    test1_k1 = 'ansible_local'
    test1_v1 = '1'
    test2_k1 = 'test'
    test2_v1 = '2'
    test3_k1 = 'test'
    test3_v1 = '3'
    test4_k1 = 'test'
    test4_v1 = '4'
    test4_v2 = '4'
    test

# Generated at 2022-06-13 03:10:24.739566
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    """Unit test for constructor of class LocalFactCollector"""
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:10:27.872522
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact = LocalFactCollector()
    assert local_fact.name == 'local'
    assert local_fact._fact_ids == set()

# Generated at 2022-06-13 03:10:32.843740
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    facts = Collector().get_facts()
    assert type(facts) is dict, 'get_facts() should return a dict.'
    assert 'local' in facts, '`local` fact should be present in get_facts().'
    assert 'ipaddr' in facts['local'], '`ipaddr` fact should be present under `local` in get_facts().'
    assert 'ipaddr' in facts['local'], '`ipaddr6` fact should be present under `local` in get_facts().'

# Generated at 2022-06-13 03:10:34.513440
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    assert set(LocalFactCollector._fact_ids) == set(['local'])

# Generated at 2022-06-13 03:10:37.286900
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local', local.name
    assert repr(local) == '<local>', repr(local)
    assert local.priority == 60, local.priority

# Generated at 2022-06-13 03:10:40.251425
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert isinstance(LocalFactCollector(), LocalFactCollector)
    assert isinstance(LocalFactCollector().collect(), dict)