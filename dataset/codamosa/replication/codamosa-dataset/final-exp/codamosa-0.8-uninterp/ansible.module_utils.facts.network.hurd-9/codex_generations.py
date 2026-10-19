

# Generated at 2022-06-13 01:37:55.522143
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = FakeModule()
    linux_facts = HurdPfinetNetwork(module=module)
    network_facts = {}
    network_facts = linux_facts.assign_network_facts(
        network_facts,
        './tests/unit/module_utils/facts/network/fsysopts',
        './tests/unit/module_utils/facts/network/socket'
    )

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.122.12'
    assert network_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:37:57.622149
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    fact = HurdNetworkCollector()
    assert fact._platform == 'GNU'
    assert fact._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:01.669521
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = HurdPfinetNetwork._create_fake_module()
    hurd_pfinet_network = HurdPfinetNetwork(module)

    assert HurdPfinetNetwork.platform == 'GNU'
    assert hurd_pfinet_network.platform == 'GNU'

# Generated at 2022-06-13 01:38:04.732952
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # TODO: implement HurdPfinetNetwork.test_HurdPfinetNetwork()
    pass

# Generated at 2022-06-13 01:38:14.727501
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import tempfile
    import shutil
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.utils import get_file_content

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp(dir="/tmp")

    # Create the socket directory
    sockdir = os.path.join(tmpdir, 'servers/socket')
    os.makedirs(sockdir)

    # Create the socket link
    sockfile = os.path.join(sockdir, 'inet')
    os.symlink('/dev/eth0', sockfile)

    module = MockModule(tmpdir)

    # Create the instance of HurdPfinetNetwork
    hurd_net = HurdPfinetNetwork(module)
   

# Generated at 2022-06-13 01:38:17.505697
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({'PATH': '/bin:/usr/bin'})
    assert network.module is None
    assert network.platform == 'GNU'


# Generated at 2022-06-13 01:38:27.851465
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = DummyAnsibleModule()
    fsysopts_path = module.get_bin_path('fsysopts')
    if fsysopts_path is None:
        return

    socket_path = None

    for l in ('inet', 'inet6'):
        link = '/servers/socket/' + l
        if os.path.exists(link):
            socket_path = link
            break

    if socket_path is None:
        return

    hm = HurdPfinetNetwork(module)
    network_facts = hm.assign_network_facts({}, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:38:30.742869
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Unit test for the constructor of class HurdNetworkCollector
    """

    hurdNetworkCollector = HurdNetworkCollector()
    assert hurdNetworkCollector._platform == 'GNU'
    assert hurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:38:41.549976
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    def socket_exists(path):
        assert path == '/servers/socket/inet'
        return False
    def fsysopts_exists(path):
        assert path == 'fsysopts'
        return False
    module = type('AnsibleModule', (object,), {
        'run_command': lambda self, cmd, check_rc=True: (0, '', ''),
        'get_bin_path': lambda self, name, opt_dirs=[] : name,
        'exit_json': lambda self, ansible_facts=None, **kwargs: True,
    })
    hpn = HurdPfinetNetwork(module)
    hpn.populate()

    module.get_bin_path = lambda self, name, opt_dirs=[] : None
    hpn = HurdPfinet

# Generated at 2022-06-13 01:38:47.409398
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.hurd.collector import HurdPfinetNetwork
    instance = HurdPfinetNetwork()
    assert isinstance(instance, HurdPfinetNetwork)


# Generated at 2022-06-13 01:39:03.821265
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    network = HurdPfinetNetwork(module)
    network._socket_dir = 'tests/unit/utils/network/hurd_socket_test'
    network_facts = network.assign_network_facts({}, 'fake_fsysopts_path',
                                                 'fake_socket_path')

# Generated at 2022-06-13 01:39:06.106559
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:39:08.929743
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    my_HurdPfinetNetwork = HurdPfinetNetwork(None, {}, {})

    assert my_HurdPfinetNetwork


# Generated at 2022-06-13 01:39:20.134336
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import tempfile

    storage = {
        '/servers/socket/inet': """
        --interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0
        --address6=fe80::6276:c6ff:fe6d:a6a6/64 --address6=fd50:fad6:a6a6:c6c6::1/64
        """,
        '/servers/socket/inet6': '/servers/socket/inet',
    }

    def readlink(path):
        return storage[path]

    def listdir(path):
        return storage.keys()

    def exists(path):
        return path in storage


# Generated at 2022-06-13 01:39:27.085730
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    fsysopts_path = os.path.join(os.path.dirname(__file__), 'fsysopts')
    hurd_pfinet_network = HurdPfinetNetwork(module=module)
    hurd_pfinet_network.assign_network_facts = lambda network_facts, p, s: network_facts
    network_facts = hurd_pfinet_network.populate()

# Generated at 2022-06-13 01:39:28.269543
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # FIXME: Implement a unit test for this method
    pass

# Generated at 2022-06-13 01:39:29.876387
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:39:30.912868
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = HurdPfinetNetwork(dict())
    assert isinstance(module, Network)

# Generated at 2022-06-13 01:39:31.636810
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork(None)

# Generated at 2022-06-13 01:39:37.057820
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import os
    import tempfile
    input_file = tempfile.NamedTemporaryFile(mode='w+')
    input_file.write('--interface=/dev/eth1\n--interface=/dev/eth0\n--address=192.168.1.2\n--address6=fe80::e147:43ff:fe51:4c4b/64\n--netmask=255.255.255.0\n--address=10.1.1.1\n--address6=::1/128')
    input_file.flush()
    module = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'lib', 'ansible', 'module_utils', 'basic.py')
    module = os.path.normpath(module)
    loader

# Generated at 2022-06-13 01:39:50.608146
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    result = HurdNetworkCollector()
    assert isinstance(result._platform, str)
    assert isinstance(result._fact_class, (object, type))

# Generated at 2022-06-13 01:39:56.379262
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    This unit test check the constructor for the GNU Hurd subclass
    of Network.
    """
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork
    network = HurdPfinetNetwork({})
    assert isinstance(network, Network)
    assert network.platform == 'GNU'


# Generated at 2022-06-13 01:39:57.180094
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({})
    assert network



# Generated at 2022-06-13 01:39:59.505081
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    instance = HurdPfinetNetwork(dict())
    assert not instance.populate()
    assert instance.platform == 'GNU'
    assert instance._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:40:02.266279
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.fact_class == HurdPfinetNetwork
    assert collector.platform == 'GNU'

# Generated at 2022-06-13 01:40:06.366735
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    obj = HurdPfinetNetwork(module)
    cores = obj.populate()
    assert len(cores) != 0

# Generated at 2022-06-13 01:40:14.808463
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import tempfile

    class MockModule:
        def get_bin_path(self, *args, **kwargs):
            return '/path/to/fsysopts'

        def run_command(self, *args, **kwargs):
            # FIXME: maybe better use fsysopts.c.tmpl
            fd, name = tempfile.mkstemp()
            os.write(fd, '''
                --address=192.168.0.2
                --interface=/dev/eth0
                --netmask=255.255.255.0
                --address6=fd00::1/64
                --address6=fd00::2/64
            ''')
            os.close(fd)

            return 0, name, ''

    network_facts = HurdPfinetNetwork({}, MockModule()).populate()

# Generated at 2022-06-13 01:40:21.936003
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Initialize:
    out = '--interface=/dev/eth0 --address=10.0.0.2 --netmask=255.255.255.0 --interface=/dev/eth1 --address=10.1.1.1 --netmask=255.255.255.0 --address6=2001:cafe:babe::1/64 --address6=2001:cafe:babe::2/64'
    network_facts = {}
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet'

    # Expected result

# Generated at 2022-06-13 01:40:25.810968
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu_hurd.interface_pfinet import HurdPfinetNetwork
    obj = HurdPfinetNetwork(ansible_module=None)
    instance = isinstance(obj, HurdPfinetNetwork)
    assert instance

# Generated at 2022-06-13 01:40:26.549071
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    sut = HurdNetworkCollector()
    assert sut._platform == 'GNU'

# Generated at 2022-06-13 01:40:55.798775
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Create a minimal fake module
    module = type('AnsibleModule', (object,), {'run_command': run_command})

    # Create a fake AnsibleModule object
    module = type('AnsibleModule', (object,), {'run_command': run_command})()

    # Create a new HurdPfinetNetwork object
    fact_class = HurdPfinetNetwork(module)

    # Call method populate
    network_facts = fact_class.populate()

    # Check if method populate return the good value

# Generated at 2022-06-13 01:40:59.129954
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    assert HurdPfinetNetwork().assign_network_facts({}, None, None) == {}
    assert HurdPfinetNetwork().assign_network_facts({}, None, None) == {}
    assert HurdPfinetNetwork().assign_network_facts({}, None, None) == {}

# Generated at 2022-06-13 01:41:04.106347
# Unit test for method assign_network_facts of class HurdPfinetNetwork

# Generated at 2022-06-13 01:41:05.121947
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # TODO
    pass


# Generated at 2022-06-13 01:41:15.577353
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    fsysopts_path = '/foo/bar/fsysopts'
    socket_path = '/foo/bar/socket'

    class Object(object):
        module = Object()
    class Module(object):
        run_command = Object()

    obj_obj = Object()
    obj_obj.run_command = Module.run_command
    obj_obj.run_command.return_value = (0, '--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=::1/128 --address6=fd00::/64', '')
    network_facts = obj_obj.assign_network_facts(network_facts, fsysopts_path, socket_path)


# Generated at 2022-06-13 01:41:16.787477
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetwork = HurdNetworkCollector().collect()
    assert HurdNetwork

# Generated at 2022-06-13 01:41:19.970864
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector(None, None)._platform == 'GNU'
    assert str(HurdNetworkCollector(None, None)._fact_class) == "<class 'ansible.module_utils.facts.network.gnu_hurd.HurdPfinetNetwork'>"

# Generated at 2022-06-13 01:41:20.754855
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector is not None

# Generated at 2022-06-13 01:41:22.826490
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c._platform == 'GNU'
    assert isinstance(c.get_network_facts(), HurdPfinetNetwork)



# Generated at 2022-06-13 01:41:32.828539
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import json
    import os
    import re
    import tempfile
    import unittest

    _platform = 'GNU'
    _fact_class = HurdPfinetNetwork
    # Use a temporary directory a fake fsysopts command
    tmpdir = tempfile.mkdtemp()
    fsysopts = os.path.join(tmpdir, 'fsysopts')
    fsysopts_content = """\
#! /bin/sh
cat <<EOF
Interface: /dev/eth0
Address: 192.168.1.200
Netmask: 255.255.255.0
Address6: fe80::8240:6aff:fe6f:bcf9/64
Address6: 2001:db8::2666:6aff:fe6f:bcf9/64
EOF
exit 0
"""


# Generated at 2022-06-13 01:42:27.396009
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = type('AnsibleModule', (object,), {
        'run_command': lambda *args: (0, '''
--interface=/dev/eth0 --address=10.0.0.9 --netmask=255.255.255.0
--interface=/dev/eth1 --address=192.168.2.2 --netmask=255.255.255.0
--interface=/dev/eth1 --address=fe80::20d:3fff:fe95:9d0a
--interface=/dev/eth1 --address6=fd00:10:192:168::2/64''', '')
    })()
    fsysopts_path = ''
    socket_path = ''
    network_facts = {}

# Generated at 2022-06-13 01:42:32.789163
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    fsysopts_path = '/hurd/fsysopts'
    socket_path = '/hurd/fsysopts'
    network_facts = {}
    # test with no argument
    network_facts = HurdPfinetNetwork(None, 0).assign_network_facts(
        network_facts, fsysopts_path, socket_path)
    if network_facts != {}:
        return False
    # test with one interface
    out = '''options = hostname=toto; \
interface=/dev/eth0; \
address=10.0.2.15; \
netmask=255.255.255.0;'''
    network_facts = {}

# Generated at 2022-06-13 01:42:41.310073
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class FakeModule(object):
        def run_command(self, args):
            # Return output from fsysopts -L
            # FIXME: this output maybe not complete
            return 0, '''--receive-broadcaster=yes
--mode=direct
--interface=/dev/eth0
--transport=raw-ethernet
--address=192.168.1.3
--netmask=255.255.255.0
--address6=fe80::ea8e:9dff:fed2:1e26/10''', None
    pfinet_network = HurdPfinetNetwork(FakeModule())
    # FIXME: add more test cases

# Generated at 2022-06-13 01:42:47.419326
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.facts import Facts
    m = Facts()
    o = HurdPfinetNetwork(m)
    assert o.platform == 'GNU'

# Generated at 2022-06-13 01:42:50.390774
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hnp = HurdPfinetNetwork(None)
    assert hnp.platform == 'GNU'
    assert hnp._socket_dir == '/servers/socket/'



# Generated at 2022-06-13 01:42:52.032143
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    fact = HurdPfinetNetwork(dict())
    assert 'GNU' == fact.platform

# Generated at 2022-06-13 01:43:02.223376
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.network.hurd.facts import HurdPfinetNetwork
    module = AnsibleModuleMock()
    module.run_command = run_command_mock

    fact = HurdPfinetNetwork(module)
    
    # simulate the content of '/servers/socket/inet'
    os.environ['ANSIBLE_HURD_SOCKET_PATH'] = '/servers/socket/inet'

    # test both ipv4 and ipv6 case

# Generated at 2022-06-13 01:43:11.861099
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    Unit test for testing assign_network_facts.
    """
    test_module = HurdPfinetNetwork({})
    test_fsysopts_path = "./tests/unit/helpers/fsysopts"
    test_socket_path = "./tests/unit/helpers/server_socket"
    network_facts = {
        'interfaces': []
    }
    network_facts = test_module.assign_network_facts(network_facts, test_fsysopts_path, test_socket_path)

# Generated at 2022-06-13 01:43:21.830451
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class module():
        run_command = lambda f, cmd, check_rc=True: (0, '', '')

    class HurdPfinetNetwork(HurdPfinetNetwork):
        def __init__(self):
            self.module = module()

    network_facts = {}
    fsysopts_path = '/hurd/pfinet'
    socket_path = '/servers/socket/inet'
    network = HurdPfinetNetwork()
    network.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.1'

# Generated at 2022-06-13 01:43:30.223916
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

    test_network = HurdPfinetNetwork()
    test_network.module = object
    setattr(
        test_network.module,
        'run_command',
        lambda cmd: ('', '--interface=eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=2607:f0d0:1002:51::4/64 --address6=fe80::a00:27ff:fea1:6df3/64 --mtu=1500 --duplex=full --speed=1000 Mbps --link=yes --multicast=yes --broadcast=yes', '')
    )

    # Populate the attributes of the test case
    test_network_facts = {}
    f

# Generated at 2022-06-13 01:45:34.403239
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.gnu.pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu.pfinet import HurdNetworkCollector

    module = basic.AnsibleModule(
        argument_spec=dict(gather_subset=dict(type='list', elements='str'),
                           gather_network_resources=dict(type='list', elements='str')),
        supports_check_mode=True)

    # Initialize Network object
    network_obj = HurdNetworkCollector(module=module)

    # Initialize Facts object
    facts_obj = Collector(module=module)

    #

# Generated at 2022-06-13 01:45:36.237742
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    my_obj = HurdNetworkCollector()
    assert my_obj.platform == "GNU"
    assert my_obj._fact_class == HurdPfinetNetwork
    assert isinstance(my_obj._fact_class, type)


# Generated at 2022-06-13 01:45:42.689081
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.gnu.facts import HurdPfinetNetwork
    from ansible.module_utils.facts.facts import AnsibleFacts

    ansible_facts = AnsibleFacts({})
    ansible_facts._module = MockModule()
    ansible_network = HurdPfinetNetwork(ansible_facts, ansible_facts.get_module())
    ansible_network.populate()



# Generated at 2022-06-13 01:45:46.285506
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    platforms = c.get_supported_os()
    assert 'GNU' in platforms
    fact_class = c.get_network_fact_class()
    assert fact_class.platform == c._platform


# Generated at 2022-06-13 01:45:47.242327
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork()

# Generated at 2022-06-13 01:45:49.088119
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector_object = HurdNetworkCollector()
    assert network_collector_object._platform == 'GNU'


# Generated at 2022-06-13 01:45:51.586845
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    fact_class = HurdPfinetNetwork()
    assert fact_class._platform == 'GNU'
    assert fact_class._fact_class == HurdPfinetNetwork



# Generated at 2022-06-13 01:45:57.927995
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector

    hp = HurdPfinetNetwork()
    hnc = HurdNetworkCollector()

    collected_facts = {'network': {'interfaces': {}}, 'ansible_facts': {'network': {}}}

    # test empty case
    hp.assign_network_facts(collected_facts['ansible_facts']['network'], 'fsysopts', '/servers/socket/inet')
    assert collected_facts == {'network': {'interfaces': {}}, 'ansible_facts': {'network': {}}}

    # test out == ''
    hp.module = MagicMock()
    hp.module.run

# Generated at 2022-06-13 01:45:59.465110
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    h = HurdPfinetNetwork()
    if h is not None:
        print("Pass")

# Generated at 2022-06-13 01:46:08.809473
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    hob_path = os.path.dirname(os.path.realpath(__file__))

    fsysopts_path = os.path.join(hob_path, '../../../../../../tests/shippable/support/ansible-test')
    socket_path = os.path.join(hob_path, '../../../../../../tests/shippable/support/files/socket/inet')

    hpn = HurdPfinetNetwork(module)

    network_facts = {
        'interfaces': [],
    }

    network_facts = hpn.assign_network_facts(network_facts, fsysopts_path, socket_path)

    # the dict with the