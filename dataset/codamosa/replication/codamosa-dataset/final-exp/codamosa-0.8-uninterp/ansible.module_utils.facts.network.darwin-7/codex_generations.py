

# Generated at 2022-06-13 01:16:43.727236
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'media': '', 'media_select': '', 'media_type': ''}
    words = ['media:', '<unknown', 'type>', '']
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, '')
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'



# Generated at 2022-06-13 01:16:45.431111
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    myDarwinNet = DarwinNetwork()
    res = myDarwinNet.platform
    assert res == 'Darwin'

# Generated at 2022-06-13 01:16:48.102408
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    x = DarwinNetwork()
    assert x.platform == 'Darwin'
    assert x.__class__.__name__ == 'DarwinNetwork'
    assert x.get_device_info.__name__ == 'get_device_info'

# Generated at 2022-06-13 01:16:57.658903
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test normal media line
    # media: autoselect (1000baseT <full-duplex>) status: active
    current_if = {}
    line = 'media: autoselect (1000baseT <full-duplex>) status: active'
    words = line.split()
    DarwinNetwork._parse_media_line(words, current_if, {})

    assert 'media' in current_if
    assert current_if['media'] == 'Unknown'  # MacOSX does not give us it
    assert 'media_select' in current_if
    assert current_if['media_select'] == 'autoselect'
    assert 'media_type' in current_if
    assert current_if['media_type'] == '1000baseT'
    assert 'media_options' in current_if
    assert current_if['media_options']

# Generated at 2022-06-13 01:17:04.238299
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    net = DarwinNetwork()
    assert net.platform == 'Darwin'
    assert net.ipv4_interfaces == set()
    assert net.ipv6_interfaces == set()
    assert net.interfaces == set()
    assert net.all_ipv4_addresses == dict()
    assert net.all_ipv6_addresses == dict()
    assert net.all_ipv4_routes == []
    assert net.all_ipv6_routes == []


# Generated at 2022-06-13 01:17:10.014078
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    media_line = ['media:', 'autoselect', '(none)']
    current_if = {}
    ips = {}
    network.parse_media_line(media_line, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'][0] == 'unknown type'

# Generated at 2022-06-13 01:17:13.691755
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    network = DarwinNetwork()
    assert network.platform == 'Darwin'
    assert network

# Generated at 2022-06-13 01:17:24.135740
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()

    darwin_net.parse_media_line(['', 'autoselect', 'none'],
                                {'options': 'some option'},
                                {})
    assert darwin_net.facts['interfaces']['bridge0']['media_select'] == 'autoselect'
    assert not 'media_type' in darwin_net.facts['interfaces']['bridge0']
    assert not 'media' in darwin_net.facts['interfaces']['bridge0']

    darwin_net.parse_media_line(['', 'autoselect', '100baseTX', 'full-duplex'],
                                {'options': 'some option'},
                                {})

# Generated at 2022-06-13 01:17:25.689469
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    darwinn = DarwinNetwork()
    assert darwinn.platform == "Darwin"

# Generated at 2022-06-13 01:17:36.274662
# Unit test for constructor of class DarwinNetwork

# Generated at 2022-06-13 01:17:39.016098
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    net = DarwinNetwork()
    assert net is not None

# Generated at 2022-06-13 01:17:47.652146
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    # given
    mod_args = dict(gather_subset='all')
    ansible_module_mock = MagicMock()
    ansible_module_mock.params = mod_args
    # when
    darwin_network = DarwinNetwork(ansible_module_mock)
    # then
    assert darwin_network.platform == 'Darwin'
    assert darwin_network._fact_class == DarwinNetwork
    assert darwin_network._platform == 'Darwin'

if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 01:17:49.668676
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    network = DarwinNetwork()
    assert network
    assert network.ifconfig_path == '/sbin/ifconfig'

# Generated at 2022-06-13 01:17:51.404989
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    darwinNetwork = DarwinNetwork(None)
    assert darwinNetwork.platform == 'Darwin'

# Generated at 2022-06-13 01:17:53.741087
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    mod = DarwinNetwork({'module': 'test'})
    assert mod.platform == 'Darwin'
    assert isinstance(mod, DarwinNetwork)



# Generated at 2022-06-13 01:18:02.514440
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Expected output for the following input is a dictionary
    words = ['media:', 'autoselect', '(100baseTX', 'full-duplex)']
    current_if = dict()
    ips = dict()
    expected_dict = dict()
    expected_dict['media'] = 'Unknown'
    expected_dict['media_select'] = 'autoselect'
    expected_dict['media_type'] = '100baseTX full-duplex'
    expected_dict['media_options'] = dict()
    expected_dict['media_options']['full-duplex'] = True

    DarwinNetwork().parse_media_line(words, current_if, ips)
    assert current_if['media'] == expected_dict['media']
    assert current_if['media_select'] == expected_dict['media_select']

# Generated at 2022-06-13 01:18:05.129176
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():

    network = DarwinNetwork()
    assert network.platform == "Darwin"
    assert network.group_counts == {}
    assert network.groups == {}
    assert network.interfaces == {}
    assert network.interface_counts == {}

# Generated at 2022-06-13 01:18:14.435078
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    ips = {}
    current_if = {}

    # test 1: no words
    words = []
    d.parse_media_line(words, current_if, ips)
    assert 'media' not in current_if

    # test 2: 1 word
    words = ['1']
    d.parse_media_line(words, current_if, ips)
    assert 'media' not in current_if

    # test 3: 2 words
    words = ['1', '<unknown']
    d.parse_media_line(words, current_if, ips)
    assert 'media' not in current_if
    assert current_if['media_select'] == '<unknown'

    # test 3: 3 words
    words = ['1', '<unknown', 'type>']

# Generated at 2022-06-13 01:18:20.780571
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Setup necessary inputs
    test_obj = DarwinNetwork()
    test_words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    test_current_if = {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'}
    test_ips = {}

    # Call method with necessary inputs
    test_obj.parse_media_line(test_words, test_current_if, test_ips)

    # Check results
    # test method should update media_select, media_type and media_options with values in words
    # the final values are stored in test_current_if
    assert test_current_if['media_select'] == '<unknown'
    assert test_current_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:18:29.473107
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Test case 1: with media_type
    #   Input:  ['media:', 'autoselect', '(100baseTX)']
    #   Output: ['media:', 'autoselect', '(100baseTX)']
    darwin_if = DarwinNetwork()
    testcase = ['media:', 'autoselect', '(100baseTX)']
    darwin_if.parse_media_line(testcase, dict(), dict())
    assert testcase == ['media:', 'autoselect', '(100baseTX)']

    # Test case 2: with media_select
    #   Input:  ['media:', 'none', 'status:', 'inactive']
    #   Output: ['media:', 'none', 'status:', 'inactive']

# Generated at 2022-06-13 01:18:42.641898
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()


# Generated at 2022-06-13 01:18:53.364866
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    ips = []
    d = DarwinNetwork()
    d.parse_media_line(['media:', '<unknown', 'type>'], current_if, ips)
    assert current_if['media_select'] == 'Unknown'
    current_if = {}
    ips = []
    d.parse_media_line(['media:', 'automatic', '(none)'], current_if, ips)
    assert current_if['media_select'] == 'automatic'
    assert current_if['media_type'] == '(none)'
    current_if = {}
    ips = []
    d.parse_media_line(['media:', '10baseT/UTP', '<full-duplex>', '(none)'], current_if, ips)

# Generated at 2022-06-13 01:19:01.235082
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:19:11.088906
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    data = DarwinNetwork({}, {})
    current_if = {}
    assert data.parse_media_line(['media:','802.11','Wi-Fi','status:','inactive'], current_if) == None
    assert current_if == {'media_options': {}, 'media_select': '802.11', 'media_type': 'Wi-Fi', 'media': 'Unknown'}
    current_if = {}
    assert data.parse_media_line(['media:','802.11','Wi-Fi','(autoselect)','status:','inactive'], current_if) == None
    assert current_if == {'media_options': {'autoselect': 1}, 'media_select': '802.11', 'media_type': 'Wi-Fi', 'media': 'Unknown'}
    current_if = {}


# Generated at 2022-06-13 01:19:21.072513
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', 'autoselect', '(none)' ]
    current_if = {'name': 'lo0', 'type': 'Unknown', 'flags': [], 'state': 'Unknown', 'macaddress': '', 'mtu': 0}
    ips = []
    d = DarwinNetwork()
    d.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == '[]'
    words = ["media:", "autoselect", "(none)"]
    d.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:19:32.061316
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test for words[1] == '<unknown' and words[2] == 'type>'
    words = ['media:', '<unknown type>', 'status:', 'inactive']
    current_if = {}
    DarwinNetwork().parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == {}

    # Test for words[1] != '<unknown' and words[2] == 'type>'
    words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    current_if = {}

# Generated at 2022-06-13 01:19:39.852281
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork() #initialize
    # initialize a dictionary with a few simple interface attributes
    current_if = {'device': 'lo0',
                  'state': 'UP',
                  'mtu': ''}
    # initialize a list of tuples of interface and addresses
    ips = []

    # test with media line of '    media: <unknown type>'
    # current_if and ips should remain unchanged
    d.parse_media_line(['    media:', '<unknown', 'type>'], current_if, ips)
    assert current_if == {'device': 'lo0', 'state': 'UP', 'mtu': ''}
    assert ips == []
    # test with media line of '    media: autoselect (100baseTX <full-duplex>) status: active'
    d.parse_

# Generated at 2022-06-13 01:19:46.578464
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Create test class instance
    test_instance = DarwinNetwork()

    # Create expected ifconfig output
    expected_output = [{'media': 'Unknown',
                        'media_select': 'media',
                        'media_type': '<unknown type>',
                        'media_options': ''}]

    # Create test input and call test method
    test_input = ['media', 'media', '<unknown', 'type>']
    assert test_instance.parse_media_line(test_input,
                                          {},
                                          {}) == expected_output

# Generated at 2022-06-13 01:19:55.639786
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d_net = DarwinNetwork()
    test_if = {}
    test_ips = {}
    test_words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    d_net.parse_media_line(test_words, test_if, test_ips)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == '(none)'
    assert test_if['media_options'] == []
    test_words = ['media:', 'autoselect', '(none)', 'status:', 'inactive', 'extra_info']
    d_net.parse_media_line(test_words, test_if, test_ips)

# Generated at 2022-06-13 01:20:03.402364
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # DarwinNetwork class
    fact_class = DarwinNetwork
    # initialize the method
    fact_class.parse_media_line(fact_class, 'media: <unknown type> status: inactive'.split(), {}, {})
    # test a full-blown example
    result = fact_class.parse_media_line(fact_class,
                                         'media: autoselect (1000baseT <full-duplex>) status: active'.split(),
                                         {}, {})
    assert result == {'media': 'Unknown',
                      'media_select': 'autoselect',
                      'media_type': '(1000baseT <full-duplex>)'}

# Generated at 2022-06-13 01:20:13.887902
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = '\tmedia: <unknown type>'
    iface = {}
    DarwinNetwork.parse_media_line(test.split(), iface, {})
    assert iface['media'] == 'Unknown'
    assert iface['media_select'] == 'media:'
    assert iface['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:20:22.157318
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    data = {
        "media_select": "",
        "media_type": "",
        "media_options": "",
    }
    test = GenericBsdIfconfigNetwork()
    # media line can't be parsed because of an unknown type
    test.parse_media_line(["status:", "<unknown", "type>"], data, [])
    assert data == {
        "media_select": "Unknown",
        "media_type": "unknown type",
        "media_options": "",
    }
    # media line can't be parsed because of multiple unknown types
    test.parse_media_line(["status:", "<unknown1", "type1>", "<unknown2",
                           "type2>"], data, [])

# Generated at 2022-06-13 01:20:32.908397
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.generic_bsd import Interface
    test_interface = Interface()
    test_interface.name = 'bridge100'
    test_words = ['media:', '<unknown', 'type>']
    test_result = {
        'name': u'bridge100',
        'media': u'Unknown',
        'media_type': u'unknown type',
        'media_select': u'<unknown'
    }
    DarwinNetwork().parse_media_line(test_words,
                                     test_interface,
                                     {})
    assert test_interface.__dict__ == test_result
    test_result['media_select'] = 'autoselect'
    test_words = ['media:', 'autoselect', '(none)']
    test_interface.name = 'en0'


# Generated at 2022-06-13 01:20:43.258490
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # no options
    words = "status: active\n".split()
    darwin_if = DarwinNetwork()
    darwin_if.parse_media_line(words, {}, {})
    assert darwin_if['media'] == 'Unknown'
    assert darwin_if['media_select'] == 'active'
    assert darwin_if['media_type'] == ''
    assert darwin_if['media_options'] == {}

    # with options
    words = "media: autoselect (1000baseT full-duplex)\n".split()
    darwin_if = DarwinNetwork()
    darwin_if.parse_media_line(words, {}, {})
    assert darwin_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:20:54.087762
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    test_line = 'media: <unknown type> (none)'
    words = test_line.split()
    current_if = {}
    ips = {}
    dn.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type', 'media_options': ['none']}
    test_line = 'media: autoselect (1000baseTX <full-duplex>)'
    words = test_line.split()
    current_if = {}
    ips = {}
    dn.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:20:59.344983
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # check if a media line is parsed correctly
    test_line = 'media: autoselect (<unknown type>) status: inactive'
    result_dict = {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': None, 'media_type': 'unknown type'}
    temp_netif = DarwinNetwork({})
    assert temp_netif.parse_media_line(test_line.split(), {}, {}) == result_dict

    # check if an incomplete media line is parsed correctly
    test_line = 'media: autoselect (<unknown type>'
    result_dict = {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': None, 'media_type': 'unknown type'}
    temp_netif = DarwinNetwork({})
    assert temp_netif.parse_

# Generated at 2022-06-13 01:21:03.646653
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = '  media: <unknown type>'.split()
    mac = DarwinNetwork(None)
    iface = dict()
    ips = dict()
    mac.parse_media_line(words, iface, ips)
    if iface['media_select'] != 'Unknown':
        raise AssertionError("media_select %s is not 'Unknown'" %
                             iface['media_select'])

# Generated at 2022-06-13 01:21:10.550980
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """Unit test for parsing of media line for Darwin"""
    current_if = {}
    ips = {}
    obj = DarwinNetwork(NetworkCollector)
    obj.parse_media_line(['media', 'auto', '10baseT/UTP', '(none)'], current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'auto'
    assert current_if['media_type'] == '10baseT/UTP'
    assert current_if['media_options'] == '(none)'
    current_if = {}
    obj.parse_media_line(['media:', 'auto', '10baseT/UTP', '(none)'], current_if, ips)
    assert 'media' in current_if

# Generated at 2022-06-13 01:21:19.791469
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Test 1 - test if media options are parsed correctly
    if_name = 'en0'
    current_if = {}
    words = ['media:', 'autoselect', '(100baseTX', 'full-duplex,flow-control)', 'status:', 'active']
    ips = []
    expected_output = {'media': 'Unknown',
                       'media_select': 'autoselect',
                       'media_type': '100baseTX',
                       'media_options': 'full-duplex,flow-control'}

    d_net = DarwinNetwork()
    d_net.parse_media_line(words, current_if, ips)

    assert current_if == expected_output

    # Test 2 - test if media options are parsed correctly when '<unknown type>' is given
    if_name = 'en0'


# Generated at 2022-06-13 01:21:28.043009
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    macnet = DarwinNetwork()
    current_if = {}
    macnet.parse_media_line(['media:', 'link', 'status:', 'active'], current_if, {})
    assert current_if['media_select'] == 'link'
    assert current_if['media_status'] == 'active'

    macnet.parse_media_line(['media:', '<unknown', 'type>'], current_if, {})
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    macnet.parse_media_line(['media:', 'autoselect', '(none)'], current_if, {})
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'none'

# Generated at 2022-06-13 01:21:47.563794
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Testing DarwinNetwork (method parse_media_line)
    # Preparation
    darwin_network = DarwinNetwork()
    current_if = {}
    ips = {}
    # Executing
    darwin_network.parse_media_line(['media:', '10baseT', '<half-duplex>', '(10baseT/half-duplex)' ], current_if, ips)
    # Verification
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '10baseT'
    assert current_if['media_type'] == 'half-duplex'
    assert current_if['media_options'] == '10baseT/half-duplex'
    # Executing

# Generated at 2022-06-13 01:21:55.099417
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media_line_1 = ['media:', 'autoselect', '(none)', '(none)']
    media_line_2 = ['media:', '<unknown', 'type>']
    media_line_3 = ['media:', 'autoselect', '100baseTX', 'full-duplex']

    current_if = {}
    ips = {}

    dn = DarwinNetwork()
    dn.parse_media_line(media_line_1, current_if, ips)
    assert(current_if['media_select'] == 'autoselect')
    assert(current_if['media_type'] == '(none)')
    assert(current_if['media_options']  == '(none)')

    current_if = {}
    dn = DarwinNetwork()

# Generated at 2022-06-13 01:22:06.345738
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """Test parsing of media line"""
    parser = DarwinNetwork()
    current_if = {}
    ips = []
    words = ['media:', '10baseT/UTP', '<link>']
    parser.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '10baseT/UTP'
    assert current_if['media_type'] == 'link'
    words = ['media:', '10baseT/UTP', '<unknown', 'type>']
    parser.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:22:13.188250
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Mac:    media: autoselect (none)
    #         media: autoselect status: inactive
    # MacOSX: media: <unknown type>

    dn = DarwinNetwork()
    ifc = dict()
    ifc['address'] = dict()
    ifc['address']['ipv4'] = list()
    ifc['address']['ipv6'] = list()
    dn.parse_media_line(['media:', 'autoselect', '(none)'], ifc, dict())
    assert ifc['media'] == 'Unknown'
    assert ifc['media_select'] == 'autoselect'
    assert ifc['media_type'] == 'none'
    assert ifc['media_options'] == dict()
    del ifc['media']
    del ifc['media_select']
   

# Generated at 2022-06-13 01:22:18.181478
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()

    # line is 'media: autoselect (none)'
    retval = darwin_net.parse_media_line(['media:', 'autoselect', '(none)'], {}, {})
    assert retval['media'] == 'Unknown'
    assert retval['media_select'] == 'autoselect'
    assert retval['media_type'] == 'none'
    assert retval['media_options'] == ''

    # line is 'media: <unknown type>'
    retval = darwin_net.parse_media_line(['media:', '<unknown', 'type>'], {}, {})
    assert retval['media'] == 'Unknown'
    assert retval['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:22:25.928495
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Arrange
    words = ['media:', '<unknown', 'type>', '(none)']
    current_if = {}
    ips = None
    # Act:
    obj = DarwinNetwork(None, None, None)
    obj.parse_media_line(words, current_if, ips)
    # Assert
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == {'none': None}

# Generated at 2022-06-13 01:22:31.969154
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    mac_media_line = "media: autoselect <unknown type> status: inactive"
    words = mac_media_line.split()
    current_if = dict()
    ips = dict()
    darwin_network = DarwinNetwork()
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'



# Generated at 2022-06-13 01:22:36.818145
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_line_1 = ['media:', '<unknown type>', '(none)', 'status:', 'inactive']
    test_line_2 = ['media:', 'autoselect', '(100baseTX)', 'status:', 'active']
    test_line_3 = ['media:', '10baseT/UTP', 'autoselect', '(10baseT/UTP)', 'status:', 'active']
    current_if = {}
    ips = None
    test_network = DarwinNetwork()
    # Test line_1 - media: <unknown type> (none)
    test_network.parse_media_line(test_line_1, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:22:44.535722
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # empty dictionary for current_if
    current_if = {}
    # media line from macOS
    # media: autoselect <unknown type> (none) status: inactive
    line = 'media: autoselect <unknown type> (none) status: inactive'
    words = line.split()
    # object to access class method
    network = DarwinNetwork()
    network.parse_media_line(words, current_if, ips=None)
    result_dict = {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'unknown type', 'media_options': 'none'}
    assert current_if == result_dict

# Generated at 2022-06-13 01:22:52.026093
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    parser = DarwinNetwork()
    current_if = {}
    ips = []
    words = ['media:', 'autoselect', 'status:', 'active']

    parser.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'status:'
    assert current_if['media_options'] == 'active'

    words = ['media:', '<unknown', 'type>', '(none)']
    parser.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'