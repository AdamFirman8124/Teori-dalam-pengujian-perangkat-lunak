

# Generated at 2022-06-13 01:48:46.726921
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class LinuxNetworkTestModule(object):
        def __init__(self):
            self.bin_path = {}
            self.rc = 0
            self.stdout = ""
            self.args = None
            self.stderr = ""

        def get_bin_path(self, name):
            return self.bin_path[name]

        def run_command(self, args, errors):
            self.args = args
            return self.rc, self.stdout, self.stderr

    class LinuxNetworkTest(LinuxNetwork):
        def __init__(self, module):
            self.module = module
            self.ip_path = "ip"

    module = LinuxNetworkTestModule()
    m = LinuxNetworkTest(module)

    # test_get_ethtool_data_success_ip
    module.bin_path

# Generated at 2022-06-13 01:48:52.590362
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.common.utils import get_module


# Generated at 2022-06-13 01:49:03.404090
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Arrange
    module = MagicMock()

# Generated at 2022-06-13 01:49:11.892749
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    class FakeModule():
        def __init__(self, rc, stdout, stderr, bin_path):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr
            self.bin_path = bin_path

        def run_command(self, args, **kwargs):
            if args[0] == self.bin_path:
                return self.rc, self.stdout, self.stderr
            return -1, '', 'NOT FOUND'

        def get_bin_path(self, var):
            return self.bin_path

    fake_module = FakeModule(0, "", "", "ethtool")
    linux_network = LinuxNetwork(fake_module)
    assert not linux_network.get_ethtool_data("eth0")

    fake_

# Generated at 2022-06-13 01:49:19.232623
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(type='list', default=['!all', '!min']),
        'gather_network_resources': dict(type='list', elements='str', default=['interfaces', 'vlans', 'bonds', 'bridges', 'stacks']),
        'filter': dict(type='dict'),
    })
    network = LinuxNetwork(module)
    if not network.populate():
        # the populate() has a boolean return value, which means success or fail
        # FIXME: this kind of test is not a great fit for the unittest module
        # FIXME: this test needs to be rewritten to assert something and not just
        # run a function and check the return code
        module.fail_json(msg="failed to populate the network object")


# Generated at 2022-06-13 01:49:26.053575
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = NetworkModule()
    module.get_bin_path = lambda _: "/sbin/ethtool"
    module.run_command = lambda x: (0, "", "")

    ln = LinuxNetwork(module)
    assert_equal(ln.get_ethtool_data('dev'), {
        'features': {},
        'timestamping': [],
        'hw_timestamp_filters': [],
    })

    # FIXME: need a real test for timestamping for LinuxNetwork
    # get_ethtool_data's output format is different from its NetBSDNetwork counterpart
    # and is yet to be validated


# Generated at 2022-06-13 01:49:35.649264
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:49:47.054432
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:49:49.521323
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    linux_network = LinuxNetwork(module)
    assert linux_network.get_ethtool_data("lo") == {}



# Generated at 2022-06-13 01:49:53.545487
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    mock_module = AnsibleModuleMock()
    mock_module.run_command = lambda args, **kwargs: (0, '', '')
    interface = 'lo'
    ln = LinuxNetwork(mock_module)
    features = ln.get_ethtool_data(interface)['features']
    assert features == {}


# Generated at 2022-06-13 01:50:36.557386
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    # Patching module function run_command
    # FIXME: move this to a real unit test mock
    get_default_interfaces_from_ip = dict(
        v4='default via fec0:0:0:1::11 on dev eth0 proto static',
        v6='default via fe80::1 dev eth0 proto kernel metric 1024 expires 2591979sec mtu 1500 advmss 1440 hoplimit 0'
    )
    get_default_interfaces_from_ip_bad = dict(
        v4=None,
        v6=None
    )

# Generated at 2022-06-13 01:50:45.430440
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)
    assert 'features' in ln.get_ethtool_data('enp4s0')
    assert 'foo' not in ln.get_ethtool_data('enp4s0')
    assert 'timestamping' in ln.get_ethtool_data('enp4s0')
    assert 'hw_timestamp_filters' in ln.get_ethtool_data('enp4s0')
    assert 'phc_index' in ln.get_ethtool_data('enp4s0')


# Generated at 2022-06-13 01:50:57.088350
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    def generate_mock_file(filename, content):
        try:
            os.remove(filename)
        except OSError:
            pass
        f = open(filename, 'w+')
        if content is not None:
            f.write(content)
        f.close()

    # TODO: needs to be improved
    def generate_mock_from_file(filename, content):
        if os.path.exists(filename) and os.path.isfile(filename):
            return True

# Generated at 2022-06-13 01:50:57.974513
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    nc = LinuxNetworkCollector(NetworkModule)
    assert nc._platform == "Linux"

# Generated at 2022-06-13 01:51:10.472062
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    import os

    mock_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list'),
            gather_timeout=dict(type='int')
        )
    )
    mock_module.get_bin_path = lambda i: i
    mock_module.run_command = lambda i, **kw: ['', '', 0]
    mock_module.get_file_content = lambda i: ""

    linux_network = LinuxNetwork(mock_module)
    expected = {'default_ipv4': {}, 'default_ipv6': {}}

# Generated at 2022-06-13 01:51:23.004688
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:51:26.810511
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    set_module_args({
        'config': 'present',
        'description': 'management',
        'state': 'absent',
        'name': 'management',
    })
    m = module()
    linux = LinuxNetwork(m)
    data = linux.get_ethtool_data("test")
    assert isinstance(data, dict)

if __name__ == '__main__':
    test_LinuxNetwork_get_ethtool_data()

# Generated at 2022-06-13 01:51:38.834309
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create an object
    module = AnsibleModule(supports_check_mode=True)
    module.params = {
        'gather_subset': ['all', 'default'],
    }
    n = LinuxNetwork(module)
    # Hack the module so we can test method
    n.module = module
    # Replace get_interfaces_info with a mocked version

# Generated at 2022-06-13 01:51:47.289738
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule

    # Invoke constructor from class AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '{ "cmd_done" : "done"}', ''))

    # Invoke constructor from class LinuxNetwork by using module provided by AnsibleModule
    # Note: name of the instance is arbitrary but should be unique
    r = LinuxNetwork(module)
    # The output will be written to this variable
    out = r.populate()

    # Example of assert
    assert out['default_ipv4']['address'] == '192.168.42.42'



# Generated at 2022-06-13 01:51:57.368802
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    out_d = dict()

# Generated at 2022-06-13 01:52:37.896943
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    os_net = LinuxNetwork()
    # mock the module, so we can test this in a sane way
    module = Mock()
    module.get_bin_path = MagicMock()
    module.run_command = MagicMock()
    module.run_command.return_value = (0, '', '')
    os_net.module = module

    # this is ethtool output from a test machine

# Generated at 2022-06-13 01:52:38.941042
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    n = LinuxNetwor

# Generated at 2022-06-13 01:52:46.865268
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # initialize module params
    a = dict(
        ips=None,
        default_ipv4=None,
        default_ipv6=None,
        interfaces=None
    )
    # initialize class LinuxNetwork
    b = LinuxNetwork()
    # call method get_default_interfaces of class LinuxNetwork
    # with module params and with initialized class
    c = b.get_default_interfaces(a)
    # expected result is a tuple that contain None and None
    # because the value is not initialized
    assert c == (None, None)



# Generated at 2022-06-13 01:52:55.169124
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    linux_network = LinuxNetwork(module)

    # TODO: replace this with local test data
    ip_path = linux_network.module.get_bin_path("ip")
    default_ipv4 = {}
    default_ipv6 = {}

    # {'interfaces': {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    interfaces = linux_network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)

    # {'eth0': {'type': 'ethernet', 'mtu': 1500, 'device': 'eth0', 'macaddress': '00:1b:21:e4:11:a8'},
    #

# Generated at 2022-06-13 01:52:59.734809
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    network = LinuxNetwork(module)
    assert network.get_default_interfaces() == network.get_default_interfaces()



# Generated at 2022-06-13 01:53:12.686847
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:53:21.688033
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    BASE_PATHS = {
        '/etc/system-release-cpe': '/etc/system-release-cpe',
        '/etc/*-release': '/etc/*-release',
        '/etc/redhat-release': '/etc/redhat-release',
        '/usr/share/clear/version': '/usr/share/clear/version',
        '/etc/os-release': '/etc/os-release',
    }
    PATHS = {
        'clear': '/usr/share/clear/version',
        'debian': '/etc/os-release',
        'rhel': '/etc/redhat-release',
    }
    PATHS.update(BASE_PATHS)

# Generated at 2022-06-13 01:53:25.092848
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    ln = LinuxNetwork(dict(
        module=dict(
            fail_json=dict(
                side_effect=lambda msg: msg['msg'],
            ),
        ),
    ))
    expected = dict(
        changed=True,
        msg="Please install net-tools or iproute2 tools",
        failed=True
    )
    assert ln._populate(expected['msg']) == expected


# Generated at 2022-06-13 01:53:25.639565
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    pass

# Generated at 2022-06-13 01:53:34.494357
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    n = LinuxNetwork()

    # first test: no response from netstat
    n.module.run_command = MagicMock(return_value=(1, '', ''))
    n.populate()
    assert n.data == {}

    # second test: invalid netstat output (no column)
    n.module.run_command = MagicMock(return_value=(0, 'invalid netstat response', ''))
    n.populate()
    assert n.data == {}

    # third test: invalid netstat output (too many columns)
    n.module.run_command = MagicMock(return_value=(0, 'tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      26062/sendmail: acce', ''))
    n.populate()
   

# Generated at 2022-06-13 01:54:09.198189
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    module = MockModule()
    lnc = LinuxNetworkCollector(module)
    assert isinstance(lnc, LinuxNetworkCollector)
    assert isinstance(lnc.net, LinuxNetwork)
    #assert isinstance(lnc.module, MockModule)

# Generated at 2022-06-13 01:54:14.494083
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # inputs
    check_ip_path = '/sbin/check_ip'
    #constructor
    l = LinuxNetwork(module=None, ip_path=check_ip_path, default_ipv4={}, default_ipv6={})
    #method to test
    result = l.get_default_interfaces()

    #asserts
    #assert that the result is not none
    assert result is not None
    #assert that the result contains the key 'default_ipv4'
    assert('default_ipv4' in result)
    #assert that the result contains the key 'default_ipv6'
    assert('default_ipv6' in result)


# Generated at 2022-06-13 01:54:20.340356
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    net = LinuxNetwork(module)
    net.get_default_interfaces = MagicMock(return_value=({"some_key": "some_value"}, {"some_key": "some_value"}))
    net.test_gather()
    assert {"some_key": "some_value"} == module.params['default_ipv4']
    assert {"some_key": "some_value"} == module.params['default_ipv6']



# Generated at 2022-06-13 01:54:23.679561
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Execute the method under test with different parameters
    ln = LinuxNetwork()
    default_ipv4, default_ipv6 = ln.get_default_interfaces()
    # Check the results
    assert isinstance(default_ipv4, dict)
    assert isinstance(default_ipv6, dict) is False


# Generated at 2022-06-13 01:54:35.216630
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Unit tests for class LinuxNetwork method get_interfaces_info
    """
    # TODO: refactor tests to be less fragile. There are long dicts as string literals here.
    # NOTE: This tests in src/unittest/ansible_collections/ansible/netcommon/tests/unit/modules/linux_net_interfaces.py
    #       are testing a lot of the same things and are probably more reliable.
    m = AnsibleModule(dict(type='command'))
    ln = LinuxNet(m)

    # FIXME: is there a less fragile way to do this?

# Generated at 2022-06-13 01:54:40.312903
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Module input data
    module_args = {}

# Generated at 2022-06-13 01:54:50.338692
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock()

    mock_ethtool_path = '/bin/ethtool'
    mock_ip_path = '/bin/ip'

    def mock_get_bin_path(arg, opt_dirs=[]):
        if arg == 'ethtool':
            return mock_ethtool_path
        elif arg == 'ip':
            return mock_ip_path
        else:
            return None

    module.get_bin_path = MagicMock(side_effect=mock_get_bin_path)
    module.params = {}

    linux_network = LinuxNetwork(module)

    assert linux_network.module == module
    assert linux_network.ethtool_path == mock_ethtool_path
    assert linux_network.ip_path

# Generated at 2022-06-13 01:54:56.855727
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    linux_network = LinuxNetwork({'changed': False, 'failed': False, 'warnings': []})
    assert isinstance(linux_network.get_interfaces_info(), tuple)
    assert isinstance(linux_network.get_interfaces_info()[0], dict)
    assert isinstance(linux_network.get_interfaces_info()[1], dict)


# Generated at 2022-06-13 01:55:06.852319
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import linux_network
    import os
    import glob

    # TODO: these can be made more realistic
    default_ipv4 = {}
    default_ipv6 = {}

    network = linux_network.LinuxNetwork()

    # FIXME: a bit of a hack to access private member
    # TODO: find a better way to do this
    for path in glob.glob('/sys/class/net/*'):
        if not os.path.isdir(path):
            continue
        device = os.path.basename(path)
        if os.path.exists(os.path.join(path, 'address')):
            network.INTERFACE_TYPE = {'1': 'ethernet'}
            break

    network.get_interfaces_info(1, default_ipv4, default_ipv6)

# Generated at 2022-06-13 01:55:08.478362
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    # FIXME: is this unit test needed?  It doesn't appear to do anything
    # If we fix the main LinuxNetworkCollector then we can make this a real test.
    # LinuxNetworkCollector()
    pass


# Generated at 2022-06-13 01:55:54.610607
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:56:01.628493
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.network import NetworkModule
    from ansible.module_utils.linux import LinuxNetwork
    # Build fake ethtool executable

# Generated at 2022-06-13 01:56:08.102775
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({})
    i = LinuxNetwork(module)

    default_ipv4 = {'address': '1.2.3.4'}
    default_ipv6 = {'address': '::1'}
    ip_path = '/sbin/ip'
    # FIXME: probably better to use test data here instead of actual output from the system

# Generated at 2022-06-13 01:56:18.942633
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = LinuxNetwork()
    module.IP_VERSION = {'v4': 4, 'v6': 6}
    module.DEFAULT_IP_VERSION = 4
    module.DEFAULT_IP_VERSION = {4: 'v4', 6: 'v6'}
    module.__metaclass__

    # check for assertions

# Generated at 2022-06-13 01:56:25.483130
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    hostname = 'mytest'
    module = MagicMock()
    module.run_command.return_value = (0, '127.0.0.1   localhost', '')
    network = LinuxNetwork(module)
    default_ipv4, default_ipv6 = network.get_default_interfaces()
    assert default_ipv4 == {"address": "127.0.0.1"}
    assert default_ipv6 == {"address": "::1"}

# Generated at 2022-06-13 01:56:33.763335
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = AnsibleModule(argument_spec=dict())
    n = LinuxNetwork(module=m)

    # Test for kernel feature data

# Generated at 2022-06-13 01:56:42.921928
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    net = LinuxNetwork(module=None)

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = {
                'gather_subset': [],
                'gather_timeout': 10,
                'filter': '',
                'match': '',
                'exclude': '',
                'config': '',
            }
            self.params.update(kwargs)

        def get_bin_path(self, arg):
            # only required by get_ethtool_data
            return '/path/to/ethtool'

        def run_command(self, *args, **kwargs):
            return 0, '', ''


# Generated at 2022-06-13 01:56:49.886211
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    result = LinuxNetwork.get_ethtool_data("em2")
    assert result['features']['rx_csum_offload'] == 'on'
    assert result['timestamping'] == ['hw', 'software', 'tx_software', 'rx_software']

# Generated at 2022-06-13 01:56:59.369145
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    # Attributes to test
    # device = None
    # errors = 'surrogate_then_replace'

    # Create an instance of the class to test
    linux_network = LinuxNetwork()

    # Use the fake ethtool command to return a valid (fake) output
    # from get_ethtool_data
    _module = linux_network.module
    _module.get_bin_path = MagicMock(return_value=os.path.join(DATA_DIR, 'fake_ethtool'))
    _module.run_command = MagicMock(return_value=(0, get_file_content(os.path.join(DATA_DIR, 'fake_ethtool_data')), ''))


# Generated at 2022-06-13 01:57:03.408568
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    module = AnsibleModuleMock()
    collector = LinuxNetworkCollector(module)
    assert collector.platform == 'Linux'
    assert collector.fact_class == LinuxNetwork
    assert collector.required_facts == set(['distribution', 'platform'])


# Generated at 2022-06-13 01:57:50.322830
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import socket
    import struct
    import sys
    import tempfile
    import textwrap

    class TestModule(object):
        @staticmethod
        def run_command(command, **kwargs):
            return 1, None, None

        @staticmethod
        def get_bin_path(name, **kwargs):
            return None

    test_helpers = {
        'socket': socket,
        'struct': struct,
        'tempfile': tempfile,
        'textwrap': textwrap,
        'os': os,
        'sys': sys,
        'module': TestModule,
    }

    network_module = LinuxNetwork()
    network_module.module = TestModule()
    for k, v in test_helpers.items():
        setattr(network_module, k, v)


# Generated at 2022-06-13 01:58:01.419601
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible.module_utils.six.moves import StringIO
    # had to override the actual run_command method

    # This is what os.path.exists('/sys/class/net/bond0') will return
    # inside the get_interfaces_info method.
    # returned_value == True if bond0 exists
    returned_value = True

    # This is what open('/sys/class/net/bond0/bonding/slaves') will return
    # inside the get_interfaces_info method.
    # returned_value == contents of /sys/class/net/bond0/bonding/slaves
    #                  if bond0 exists
    # returned_value == '' otherwise
    return_value = StringIO()
    return_value.write('slave0\nslave1')

# Generated at 2022-06-13 01:58:04.727909
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    nm = LinuxNetwork(module)
    default_ipv4, default_ipv6 = nm.get_default_interfaces()
    for k in default_ipv4:
        assert k in ['address', 'broadcast', 'netmask', 'network', 'macaddress', 'mtu', 'type'], 'Invalid key %s' % k
    module.fail_json(msg='test_LinuxNetwork_get_default_interfaces failed')



# Generated at 2022-06-13 01:58:12.075681
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # This is an integration test of the method get_interfaces_info of the class LinuxNetwork

    # Create a temporary file with the data we want to read
    # The content of this file will be /sys/class/net/ens3/address
    tmp_file = tempfile.NamedTemporaryFile()
    tmp_file.write(b'00:11:22:33:44:55')
    tmp_file.flush()
    # Create a temporary directory
    # A /sys/class/net/ens3 directory will be created in this directory
    tmp_dir = tempfile.TemporaryDirectory()
    os.makedirs(os.path.join(tmp_dir.name, 'sys/class/net/ens3/device/driver/module'))
    # Create a file witch will represent the module name