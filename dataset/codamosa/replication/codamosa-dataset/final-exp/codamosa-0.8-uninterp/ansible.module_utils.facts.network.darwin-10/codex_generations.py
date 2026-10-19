

# Generated at 2022-06-13 01:16:38.991544
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    d = DarwinNetwork()

    assert d.platform == 'Darwin'

# Generated at 2022-06-13 01:16:45.626262
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """ Unit test for method parse_media_line of class DarwinNetwork """

    # Initialize the class
    darwin_network = DarwinNetwork()

    # test input
    words = ['media:', '<unknown', 'type>']

    # expected output
    expected_media_select = 'Unknown'
    expected_media_type = 'unknown type'

    # call the method
    darwin_network.parse_media_line(words, {}, {})

    # get output
    output_media_select = darwin_network.current_if['media_select']
    output_media_type = darwin_network.current_if['media_type']

    # assert statements
    assert output_media_select == expected_media_select
    assert output_media_type == expected_media_type

# Generated at 2022-06-13 01:16:48.255517
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    """
    Test if a single DarwinNetwork() object is created when running
    the DarwinNetwork() constructor
    """
    darwin_net = DarwinNetwork()

    assert isinstance(darwin_net, DarwinNetwork)


# Generated at 2022-06-13 01:16:57.799506
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # case 1: line is ['media:', 'autoselect', '(none)', 'status:']
    line = ['media:', 'autoselect', '(none)', 'status:']
    current_if = {'options': [], 'type': 'Ethernet', 'duplex': 'Full', 'macaddress': '00:00:00:00:00:00',
                  'mtu': 1500, 'inet': [{'address': '127.0.0.1', 'netmask': '255.0.0.0', 'broadcast': '127.255.255.255'}],
                  'inet6': [], 'status': 'active', 'options_enabled': []}

# Generated at 2022-06-13 01:17:00.960887
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    a = DarwinNetwork()
    assert a.platform == "Darwin"
    assert a._platform == "Darwin"
    assert a._fact_class.__name__ == 'DarwinNetwork'


# Generated at 2022-06-13 01:17:06.574291
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    """
    Unit test for constructor of class DarwinNetwork
    """
    darw_network = DarwinNetwork()
    assert darw_network.get_option('media_type') == 'unknown type'
    assert darw_network.get_option('media') == 'Unknown'
    assert darw_network.get_option('media_select') == 'Unknown'
    assert darw_network.get_option('media_options') is None

# Generated at 2022-06-13 01:17:07.762926
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    d = DarwinNetwork({}, {}, {}, {})
    assert d.platform == 'Darwin'

# Generated at 2022-06-13 01:17:08.555478
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    net = DarwinNetwork()
    assert net.platform == 'Darwin'

# Generated at 2022-06-13 01:17:14.773998
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    fake_if = {}
    fake_if['iface'] = 'en1'
    fake_if['type'] = 'en'
    fake_if['mac_address'] = 'a0:b1:c2:d3:e4:f5'
    fake_if['inet'] = '192.168.1.1'
    fake_if['netmask'] = '0xffffff00'
    fake_if['broadcast'] = '192.168.1.255'
    fake_if['options'] = 'none'
    fake_if['mediatype'] = 'none'
    fake_if['media_options'] = 'none'

    test_network = DarwinNetwork()
    test_network.get_options = lambda x: x

    media_line = 'media: autoselect ()'

# Generated at 2022-06-13 01:17:16.212467
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    d = DarwinNetwork()
    assert(isinstance(d, DarwinNetwork))

# Generated at 2022-06-13 01:17:26.414074
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:17:36.766339
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    words = [1, 1, 1, 1]

    darwin_network = DarwinNetwork({})

    darwin_network.parse_media_line(words, current_if, {})
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 1
    assert current_if['media_type'] == 1
    assert current_if['media_options'] == 1

    words = [1, '<unknown', 'type>', 1]
    darwin_network.parse_media_line(words, current_if, {})
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options']

# Generated at 2022-06-13 01:17:41.279840
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    Darwin_words = ['mtu', '1500', 'options', '=']
    current_if = {}
    ips = []
    Darwin_expected_result = {'media': 'Unknown',
                              'media_select': '1500',
                              'media_type': 'options',
                              'media_options': '='}
    Darwin_result = DarwinNetwork.parse_media_line(Darwin_words, current_if, ips)
    assert Darwin_result == Darwin_expected_result

# Generated at 2022-06-13 01:17:53.245874
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test method with valid data
    current_if = dict()
    words = ['media:', '10baseT', '/full', '<unknown type>']
    DarwinNetwork.parse_media_line(DarwinNetwork(), words, current_if, None)
    assert (current_if['media'] == 'Unknown')
    assert (current_if['media_select'] == '10baseT')
    assert (current_if['media_type'] == 'unknown type')
    assert (current_if['media_options'] == {'full': None})
    # test method with invalid data
    current_if = dict()
    words = ['media:', '10baseT', '/full']
    DarwinNetwork.parse_media_line(DarwinNetwork(), words, current_if, None)
    assert ('media' not in current_if)

# Generated at 2022-06-13 01:18:01.429669
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    current_if = {'media': 'Unknown'}
    ifc = DarwinNetwork()
    ifc.parse_media_line(words, current_if, None)
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == 'status: inactive'

    words = ['media:', '<unknown', 'type>']
    current_if = {'media': 'Unknown'}
    ifc = DarwinNetwork()
    ifc.parse_media_line(words, current_if, None)
    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:18:08.162211
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()
    words = ['media:', 'autoselect', '(none)']
    current_if = {}
    ips = {}
    darwin_net.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    current_if = {}
    words = ['media:', '<unknown', 'type>']
    darwin_net.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:18:15.376231
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media = {'media_select': 'fixed', 'media_options': {}}
    # normal media line
    d = DarwinNetwork()
    words = ['media:', 'fixed', '10Gbase-LR', 'mediaopt', 'subtype', '0x1']
    d.parse_media_line(words, {}, '')
    assert d.current_if == media
    # media line with spaces
    d = DarwinNetwork()
    words = ['media:', 'fixed', '10Gbase-LR', 'subtype', '0x1', 'mediaopt']
    d.parse_media_line(words, {}, '')
    assert d.current_if == media


# Generated at 2022-06-13 01:18:21.340355
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """ Unit test for method parse_media_line of class DarwinNetwork """
    # test 1
    words = ["media:", "autoselect", "<unknown", "type>"]
    current_if = {}
    ips = {}
    darwin_network = DarwinNetwork()
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'
    assert len(current_if['media_options']) == 0

    # test 2
    words = ["media:", "autoselect", "<unknown", "type>", "(none)"]
    current_if = {}
    ips = {}
    darwin_network

# Generated at 2022-06-13 01:18:26.591420
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    media_line = 'media: <unknown type> no carrier status: inactive'
    words = media_line.split()
    current_if = {}
    ips = {}
    d.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:18:38.991905
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:18:48.391235
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Arrange
    words = ["media", "<unknown", "type>"]
    current_if = {}
    ips = {}
    darwin_network = DarwinNetwork(None, '', '', '')

    # Act
    darwin_network.parse_media_line(words, current_if, ips)

    # Assert
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:18:56.883947
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    print('Testing DarwinNetwork.parse_media_line()')

    # Netplan facts
    netplan_data = {
        "media": "Unknown",
        "media_select": "Autoselect",
        "media_type": "no carrier",
        "media_options": {}
    }
    # Expected result
    netplan_expected = netplan_data

    # Init class
    test_class = DarwinNetwork()

    # Test method parse_media_line()
    result = test_class.parse_media_line(
        ["media:", "Autoselect", "(no", "carrier)"],
        netplan_data,
        {}
    )

    assert result == netplan_expected


# Generated at 2022-06-13 01:19:08.648344
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', 'Autoselect', '(none)', 'status:', 'inactive']
    current_if = {'ifconfig_interfaces': []}
    ips = []
    d = DarwinNetwork(current_if, ips)
    d.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Autoselect'
    assert current_if['media_type'] == '(none)'

    words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    current_if = {'ifconfig_interfaces': []}
    ips = []
    d = DarwinNetwork(current_if, ips)

# Generated at 2022-06-13 01:19:20.796095
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = {'ifname': 'en0', 'ifindex': '2'}
    parsed_line = ['media:', '<unknown type>']
    network = DarwinNetwork(None)
    network.parse_media_line(parsed_line, iface, {})
    assert iface['media'] == 'Unknown'
    assert iface['media_select'] == 'Unknown'

    parsed_line = ['media:', 'Auto', '<unknown type>']
    network.parse_media_line(parsed_line, iface, {})
    assert iface['media_type'] == 'unknown type'

    parsed_line = ['media:', 'Auto', '<unknown type>', 'full-duplex']
    network.parse_media_line(parsed_line, iface, {})
    assert iface

# Generated at 2022-06-13 01:19:31.782944
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = [
        'media:',
        'autoselect',
        '(none)',
    ]

    current_if = {}

    d = DarwinNetwork()
    d.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert 'media_options' not in current_if

    words = [
        'media:',
        '<unknown',
        'type>',
        'status:',
        'inactive',
    ]

    current_if = {}

    d.parse_media_line(words, current_if, None)
    assert current_if['media_select'] == 'Unknown'
    assert current_

# Generated at 2022-06-13 01:19:36.907719
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    cls = DarwinNetwork
    current_if = {}
    # media line with third unknown word
    ret_val = cls.parse_media_line(['media:', '<unknown', 'type>'], current_if, [])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    # media line with fourth options word
    ret_val = cls.parse_media_line(['media:', 'autoselect', '10baseT/UTP', '(none)'], current_if, [])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:19:42.918653
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test the case of correct line
    test_line1 = ('media: <unknown type> <unknown type> status: inactive'
                  ' restart_cnt: 1')
    test_words1 = test_line1.split()
    current_if1 = {}
    ips1 = {}
    mytest_test_DarwinNetwork_parse_media_line1 = DarwinNetwork(None)
    mytest_test_DarwinNetwork_parse_media_line1.parse_media_line(test_words1,
                                                                 current_if1,
                                                                 ips1)
    assert current_if1['media'] == 'Unknown'
    assert current_if1['media_select'] == 'Unknown'
    assert current_if1['media_type'] == 'unknown type'

    # test the case of incorrect line
    test

# Generated at 2022-06-13 01:19:52.397684
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    net = DarwinNetwork()
    x = {'macaddress': '00:11:2f:4d:aa:b7', 'type': 'en', 'mtu': 1500, 'active': True, 'ipv4': [{'address': '172.16.0.2', 'netmask': '255.248.0.0', 'broadcast': '172.23.255.255'}], 'ipv6': [], 'name': 'en0'}
    net.parse_media_line(['media:', 'auto'], x, [])
    assert x['media'] == 'Unknown'
    assert x['media_select'] == 'auto'
    net.parse_media_line(['media:', '10baseT/UTP'], x, [])
    assert x['media'] == 'Unknown'

# Generated at 2022-06-13 01:19:57.750213
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # media line:
    # media: autoselect (<unknown type>)
    m_line = ['media:', 'autoselect', '<unknown', 'type>']
    ifclass = DarwinNetwork('')
    ifclass.parse_media_line(m_line, {}, [])
    assert ifclass._current_if['media'] == 'Unknown'
    assert ifclass._current_if['media_select'] == 'autoselect'
    assert ifclass._current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:20:00.255010
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    mac_bridge_media = ['media:', '<unknown', 'type>']
    darwin_network.parse_media_line(mac_bridge_media, {}, [])
    assert mac_bridge_media[1:] == ['Unknown', 'unknown type']