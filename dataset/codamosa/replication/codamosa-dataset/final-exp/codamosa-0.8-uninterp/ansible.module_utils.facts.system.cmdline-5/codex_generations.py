

# Generated at 2022-06-13 02:30:22.599111
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_collector = CmdLineFactCollector()
    proc_cmdline_facts = fact_collector._get_proc_cmdline()
    cmdline_facts = fact_collector.collect()
    assert 'cmdline' in cmdline_facts
    assert cmdline_facts['cmdline']
    assert 'proc_cmdline' in cmdline_facts
    assert cmdline_facts['proc_cmdline']

# Generated at 2022-06-13 02:30:28.379991
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    from ansible.module_utils._text import to_bytes

    c = Collector()
    assert isinstance(c.collect_cmdline_facts(), dict) is False

    c = CmdLineFactCollector()
    result = c._get_proc_cmdline()
    if not result:
        assert isinstance(c.collect().pop(), dict)

    data = to_bytes('root=/dev/sda1')
    assert isinstance(c._parse_proc_cmdline(data), dict)


# Generated at 2022-06-13 02:30:30.772931
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'


# Generated at 2022-06-13 02:30:32.579791
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:30:39.890305
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector = CmdLineFactCollector()
    CmdLineFactCollector._get_proc_cmdline = lambda: """
ro root=/dev/mapper/s390_netboot-root rd_NO_LUKS LANG=en_US.UTF-8 rd_NO_MD rd_LVM_LV=s390_netboot/root rd_LVM_LV=s390_netboot/swap rd_NO_DM SYSFONT=latarcyrheb-sun16 crashkernel=256M
    """.strip()
    facts = CmdLineFactCollector.collect()
    assert facts['cmdline']['ro'] == True
    assert facts['cmdline']['root'] == '/dev/mapper/s390_netboot-root'

# Generated at 2022-06-13 02:30:50.797169
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    # Test the function with the file /proc/cmdline returns
    with open("tests/unit/module_utils/facts/files/cmdline", "r") as fp:
        data = fp.read()
        c._get_proc_cmdline = lambda : data
        res = c.collect()

# Generated at 2022-06-13 02:30:55.208855
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class FakeModule(object):
        pass

    cmdline_facts = CmdLineFactCollector.collect(FakeModule())
    assert cmdline_facts['cmdline']['console'] == 'tty1'
    assert cmdline_facts['proc_cmdline']['ro'] is True



# Generated at 2022-06-13 02:30:59.618380
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    _module = None
    _collected_facts = None
    _collector = CmdLineFactCollector()

    _cmdline_facts = _collector.collect(_module, _collected_facts)

    assert isinstance(_cmdline_facts, dict)
    assert _cmdline_facts['cmdline']
    assert _cmdline_facts['proc_cmdline']


# Generated at 2022-06-13 02:31:02.059893
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert not cmdline._fact_ids
    assert isinstance(cmdline._fact_ids, set)

# Generated at 2022-06-13 02:31:02.927579
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:09.077158
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_class = CmdLineFactCollector()
    assert test_class is not None


# Generated at 2022-06-13 02:31:13.636926
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    # Create a new instance of CmdLineFactCollector
    c = CmdLineFactCollector()

    # c.name should be 'cmdline'
    assert c.name == 'cmdline'

    # c.fact_ids should be empty
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:31:18.077219
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    This is the unit test for method collect of class CmdLineFactCollector.
    It captures all the outputs of the method for various inputs.
    For more details, refer the test case document.
    """
    cld = CmdLineFactCollector()
    cld.collect(module = None, collected_facts = None)


# Generated at 2022-06-13 02:31:23.224355
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {'proc_cmdline':{'rhgb':True, 'quiet':True},
         'cmdline':{'rhgb':True, 'quiet':True}}

    o_cc = CmdLineFactCollector()
    o_cc.parse_proc_cmdline = lambda x: {'rhgb':True, 'quiet':True}
    o_cc.parse_proc_cmdline_facts = lambda x: {'rhgb':True, 'quiet':True}
    o_cc.get_proc_cmdline = lambda: 'rhgb quiet'

    assert o_cc.collect() == cmdline_facts


# Generated at 2022-06-13 02:31:30.991761
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """ unittest for method collect of class CmdLineFactCollector """
    # initializing a class
    obj = (CmdLineFactCollector)

    # a sample data of the file /proc/cmdline
    sample_data = 'ro root=UUID=6f8d6f1c-75a0-4c18-8a39-c26785954865 rhgb quiet BOOT_IMAGE=vmlinuz-3.10.0-514.10.2.el7.x86_64 default_hugepagesz=1GB hugepagesz=1G hugepages=8 transparent_hugepage=defrag'

    # mocking the method _get_proc_cmdline
    obj._get_proc_cmdline = lambda self: sample_data

    # calling method collect
    result = obj.collect()

    # asserting the result obtained


# Generated at 2022-06-13 02:31:40.620573
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test the collect method of the class CmdLineFactCollector
    """
    import os
    CMDLINE_FILE = "/proc/cmdline"

    class MockModule(object):
        def get_bin_path(cmd, required=False, opt_dirs=[]):
            return "echo"

    mock_module = MockModule()

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Note: There is no way to test this function as is because it fetches
    # content of file /proc/cmdline which is not accounted by unit tests.
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    v  = CmdLineFactCollector(mock_module)
    assert v.collect() == {}


# Generated at 2022-06-13 02:31:41.367723
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:31:42.697641
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == "cmdline"
    assert collector._fact_ids == set()



# Generated at 2022-06-13 02:31:50.097158
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=/vmlinuz-4.4.0-18362-Microsoft'

    result = collector.collect()

    assert result == {'cmdline': {'BOOT_IMAGE': '/vmlinuz-4.4.0-18362-Microsoft'},
                      'proc_cmdline': {'BOOT_IMAGE': '/vmlinuz-4.4.0-18362-Microsoft'}}


# Generated at 2022-06-13 02:31:58.480818
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import json
    import os
    import sys
    import tempfile

    # Create temporary fake files and directories
    tmp_dir = tempfile.mkdtemp()
    fake_proc_cmdline_file = os.path.join(tmp_dir, 'cmdline')
    fake_proc_cmdline_content = 'root=/dev/sda2  ptable=dos rd.break=initqueue  init=/usr/lib/systemd/systemd  rhgb root=UUID=a8a06c13-9e9d-4cff-b1ed-85507a7512e6  LANG=en_US.UTF-8  ro console=tty0 console=ttyS0,115200'

    # Write fake file

# Generated at 2022-06-13 02:32:06.944614
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import imp

    # Make sure we can create an instance of CmdLineFactCollector
    obj = CmdLineFactCollector()

    # Make sure we get an instance of CmdLineFactCollector
    assert isinstance(obj, CmdLineFactCollector)

    # First argument of constructor is module
    assert obj.module is None

    # Second argument of constructor is collector
    assert obj.collector is None

# Generated at 2022-06-13 02:32:08.094733
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    # mock a module
    module = type('', (), {})()
    c.collect(module)

# Generated at 2022-06-13 02:32:19.349374
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''Unit test for method collect method of CmdLineFactCollector'''
    collector = CmdLineFactCollector()


# Generated at 2022-06-13 02:32:21.136275
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert cf._fact_ids == set()


# Generated at 2022-06-13 02:32:32.199027
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import os
    import tempfile

    # Create a temporary file
    fd, name = tempfile.mkstemp()

# Generated at 2022-06-13 02:32:34.775995
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert CmdLineFactCollector().collect().get('cmdline').get('root') == 'LABEL=/'

# Generated at 2022-06-13 02:32:39.456512
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector._get_proc_cmdline()
    if not cmdline_facts:
        raise AssertionError('Unable to obtain content of /proc/cmdline file')
    cmdline_facts = collector._parse_proc_cmdline(cmdline_facts)
    if not cmdline_facts:
        raise AssertionError('Unable to parse content of /proc/cmdline file')

# Generated at 2022-06-13 02:32:40.664447
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Test creation of instance
    obj = CmdLineFactCollector()


# Generated at 2022-06-13 02:32:43.961289
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    data = collector._get_proc_cmdline = lambda: 'foo=bar baz'
    cmdline_facts = collector.collect()
    assert cmdline_facts == {
        'cmdline': {
            'foo': 'bar',
            'baz': True,
        },
        'proc_cmdline': {
            'foo': 'bar',
            'baz': True,
        },
    }

# Generated at 2022-06-13 02:32:44.719620
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()


# Generated at 2022-06-13 02:32:53.766751
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    assert c.collect() == {}


# Generated at 2022-06-13 02:32:55.919973
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    try:
        cmdline_fact_collector = CmdLineFactCollector()
    except:
        assert False


# Generated at 2022-06-13 02:32:57.808196
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:33:08.190658
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Create instance of class CmdLineFactCollector
    cmdline_facts_collector = CmdLineFactCollector()
    # Execute Method
    cmdline_facts = cmdline_facts_collector.collect()

    # Check that cmdline_facts_collector.collect() method is not none
    assert cmdline_facts is not None

    # Check that cmdline_facts_collector.collect() returns a dictionnary
    assert isinstance(cmdline_facts, dict)

    # Check that cmdline_facts is not empty
    assert cmdline_facts != {}

    # Check that cmdline_facts contains specific keys
    cmdline_fact_keys = ['cmdline', 'proc_cmdline']
    assert set(cmdline_fact_keys) == set(cmdline_facts.keys())

    # Check that cmdline_facts['cmd

# Generated at 2022-06-13 02:33:09.404363
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    result = CmdLineFactCollector()
    assert result.name == 'cmdline'

# Generated at 2022-06-13 02:33:10.852607
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'


# Generated at 2022-06-13 02:33:21.022324
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.utils import FactsCollector, get_file_content
    from ansible.module_utils.facts.collectors import get_collector_class
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import timeout

    my_local_fact_collector_classes = [
        get_collector_class('CmdLineFactCollector')
    ]

    my_local_fact_collector_classes_indexed = {
        fact_class.name: fact_class for fact_class in my_local_fact_collector_classes
    }

    my_local_fact_collector = FactsCollector(my_local_fact_collector_classes_indexed, {})

    module = None
    collected_facts = None

    # Check when /proc

# Generated at 2022-06-13 02:33:30.357131
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import ast

    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector

    module = None
    collected_facts = None
    fact = CmdLineFactCollector()

    # Testing the return of collect method
    assert isinstance(fact.collect(module, collected_facts), dict)
    assert 'cmdline' in fact.collect(module, collected_facts)
    assert isinstance(fact.collect(module, collected_facts)['cmdline'], dict)
    assert 'proc_cmdline' in fact.collect(module, collected_facts)
    assert isinstance(fact.collect(module, collected_facts)['proc_cmdline'], dict)

    # Testing the return of _get_proc_cmdline method

# Generated at 2022-06-13 02:33:31.823468
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj


# Generated at 2022-06-13 02:33:32.939787
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:33:50.801431
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()

# Generated at 2022-06-13 02:33:51.571307
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    pass

# Generated at 2022-06-13 02:33:57.804515
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert cf._fact_ids == set()
    assert cf._get_proc_cmdline()
    assert cf._parse_proc_cmdline(cf._get_proc_cmdline())
    assert cf._parse_proc_cmdline_facts(cf._get_proc_cmdline())
    assert cf.collect()

# Generated at 2022-06-13 02:33:58.935955
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    r = CmdLineFactCollector()
    r.collect()

# Generated at 2022-06-13 02:34:05.797747
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Ensure the constructor for CmdLineFactCollector creates a
    # instance with the appropriate attributes and methods.
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import CmdLineFactCollector
    test_cmdline_fact_collector = CmdLineFactCollector()
    assert isinstance(test_cmdline_fact_collector, collector.BaseFactCollector)
    assert hasattr(test_cmdline_fact_collector, 'name')
    assert test_cmdline_fact_collector.name == 'cmdline'
    assert hasattr(test_cmdline_fact_collector, '_fact_ids')
    assert hasattr(test_cmdline_fact_collector, '_get_proc_cmdline')

# Generated at 2022-06-13 02:34:10.405100
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for method collect of class CmdLineFactCollector.

    :return: None
    """

    # This class is a little tricky to test but here goes...
    try:
        from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts import collector
        from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collector import BaseFactCollector
    except ImportError as e:
        # Older Ansible versions don't have collections.
        from ansible.module_utils.facts import collector
        from ansible.module_utils.facts.collector import BaseFactCollector

    def create_collector(name):
        """Helper function to create a private version of CmdLineFactCollector.

        :return: None
        """

# Generated at 2022-06-13 02:34:14.894491
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    class MockModule:
        def __init__(self, *args, **kwargs):
            self.params = {'gather_subset': ['!all', 'cmdline']}

    collector = CmdLineFactCollector()
    collector.collect(module=MockModule())

    assert collector._fact_ids == set(['cmdline'])

# Generated at 2022-06-13 02:34:17.260340
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFact = CmdLineFactCollector()
    assert cmdLineFact.name == "cmdline"
    assert len(cmdLineFact._fact_ids) == 0


# Generated at 2022-06-13 02:34:27.754807
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    This method tests the collect method of the CmdLineFactCollector class.
    """
    print('Testing CmdLineFactCollector collect method')
    cmdline_fact_collector = CmdLineFactCollector()


# Generated at 2022-06-13 02:34:30.914083
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:35:11.337651
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:35:16.264640
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mock_module = type('', (), dict(params=dict()))()
    mock_module.params = dict(gather_subset=['!all', 'cmdline'])
    mock_module.params['gather_timeout'] = 10
    mock_module.params['filter'] = 'ansible_cmdline'
    mock_cmdline_file_content = """BOOT_IMAGE=/vmlinuz-4.4.0-31-generic
root=/dev/mapper/ubuntu-root ro quiet splash vt.handoff=7 BOOT_IMAGE=/vmlinuz-4.4.0-31-generic root=/dev/mapper/ubuntu-root ro quiet splash vt.handoff=7"""

    collector = CmdLineFactCollector()
    mock_file_reader = type('', (), dict(read=None))()
   

# Generated at 2022-06-13 02:35:18.887041
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 02:35:20.539805
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:35:26.768109
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    data = 'console=ttyS0,9600n8 console=tty0 debug root=/dev/sda1 systemd.log_level=debug'
    expected_result = {
        'proc_cmdline': {
            'console': ['ttyS0,9600n8', 'tty0'],
            'debug': True,
            'root': '/dev/sda1',
            'systemd.log_level': 'debug'
        },
        'cmdline': {
            'console': 'ttyS0,9600n8',
            'debug': True,
            'root': '/dev/sda1',
            'systemd.log_level': 'debug'
        }
    }

    test = CmdLineFactCollector()

    collected_facts = test.collect({}, {})

    assert collected_facts == expected_result

# Generated at 2022-06-13 02:35:28.803342
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    collector.collect()

# Generated at 2022-06-13 02:35:36.184734
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:35:42.091247
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:35:43.672538
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set([])


# Generated at 2022-06-13 02:35:47.925020
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Init
    cmdline_collector = CmdLineFactCollector()

    cmdline_collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=/vmlinuz-2.6.32-5-amd64 root=/dev/mapper/debian-root ro quiet'

    # Test
    cmdline_facts = cmdline_collector.collect()

    # Asserts
    assert cmdline_facts['cmdline']['quiet'] == True
    assert cmdline_facts['cmdline']['BOOT_IMAGE'] == '/vmlinuz-2.6.32-5-amd64'
    assert cmdline_facts['cmdline']['root'] == '/dev/mapper/debian-root'

    assert cmdline_facts['proc_cmdline']['quiet'] == True
    assert cmdline_facts

# Generated at 2022-06-13 02:37:25.963157
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector

# Generated at 2022-06-13 02:37:27.593540
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:37:28.486165
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    dummy_class = CmdLineFactCollector()

# Generated at 2022-06-13 02:37:29.473718
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert 'cmdline' == CmdLineFactCollector.name

# Generated at 2022-06-13 02:37:30.802062
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
        x = CmdLineFactCollector()
        assert x.name == 'cmdline'


# Generated at 2022-06-13 02:37:32.856645
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:37:42.548769
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import json
    import os

    x = CmdLineFactCollector()
    assert set({'cmdline', 'proc_cmdline'}).issubset(x._fact_ids)

    with open('tests/unit/module_utils/facts/files/cmdline') as f:
        cmdline = f.read()

    assert cmdline == x._get_proc_cmdline()

    cmdline_dict = x._parse_proc_cmdline(cmdline)
    assert set({'a', 'b', 'c', 'd', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r'}).issubset(cmdline_dict)

    cmdline_dict = x._parse_proc_cmdline_facts(cmdline)

# Generated at 2022-06-13 02:37:43.955999
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()

# Generated at 2022-06-13 02:37:48.248301
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mocked_collector = CmdLineFactCollector()
    mocked_collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=(hd0,msdos1)/vmlinuz-3.10.0-1127.13.1.el7.x86_64 ro root=/dev/mapper/rhel-root LANG=en_US.UTF-8'

    existing_facts = dict(ansible_mounts=[], ansible_architecture='x86_64')
    facts = mocked_collector.collect(collected_facts=existing_facts)['cmdline']

    assert facts['BOOT_IMAGE'] == 'hd0,msdos1/vmlinuz-3.10.0-1127.13.1.el7.x86_64'
    assert facts['ro']

# Generated at 2022-06-13 02:37:51.989128
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact = CmdLineFactCollector()
    assert cmdline_fact.name == "cmdline"
    assert isinstance(cmdline_fact._fact_ids, set)
    assert cmdline_fact._fact_ids == set()