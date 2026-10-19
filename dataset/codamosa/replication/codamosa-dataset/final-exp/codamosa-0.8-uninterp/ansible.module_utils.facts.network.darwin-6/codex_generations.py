

# Generated at 2022-06-13 01:16:45.545073
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork('eth1')
    dn.parsers[0] = {'media': dn.parse_media_line}

    params = ['media', 'autoselect', '(none)']
    current_if = {'name': 'eth1'}
    ips = []
    dn.parse_media_line(params, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] is None
    assert current_if['media_options'] == []

    params = ['media', '1000baseT', '(TX)', 'full-duplex,hw-loopback']
    current_if = {'name': 'eth1'}
    dn.parse_media_

# Generated at 2022-06-13 01:16:53.447574
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    d.parse_media_line(['media:', 'autoselect', '(none)'], {}, {})
    assert d.current_if['media'] == 'Unknown'
    assert d.current_if['media_select'] == 'autoselect'
    assert d.current_if['media_type'] == '(none)'
    d.parse_media_line(['media:', '<unknown', 'type>', 'status:', 'inactive'], {}, {})
    assert d.current_if['media_select'] == 'Unknown'
    assert d.current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:17:00.793809
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Create a DarwinNetwork object
    net_coll_obj=DarwinNetwork()
    # Create a dict
    expected={}
    # Set the values of the dict
    expected['media'] = 'Unknown'
    expected['media_select'] = 'autoselect'
    expected['media_type'] = 'unknown type'

    # Parse the media line of a bridge interface and verify the output
    actual = net_coll_obj.parse_media_line(['media', 'autoselect', '<unknown', 'type>'], {}, {})
    assert expected == actual

    # Set the values of the dict
    expected['media'] = 'Unknown'
    expected['media_select'] = '10baseT/UTP'
    expected['media_type'] = ''

# Generated at 2022-06-13 01:17:07.084787
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'device': 'lo0'}
    d = DarwinNetwork()
    d.parse_media_line(['lo0:', '<Loopback,', 'UP,', 'LOWER_UP>', 'mtu', '16384'], current_if, None)
    assert current_if['media_select'] == '<Loopback,'
    assert current_if['media_type'] == 'UP,'
    assert current_if['media_options'] == 'LOWER_UP>'

# Generated at 2022-06-13 01:17:13.429512
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    result = {}
    assert DarwinNetwork().parse_media_line(['media:', 'autoselect', '(none)'], result, {}) == result
    assert result['media'] == 'Unknown'
    assert result['media_select'] == 'autoselect'
    assert result['media_type'] == '(none)'
    assert result['media_options'] == []
    result = {}
    assert DarwinNetwork().parse_media_line(['media:', 'autoselect'], result, {}) == result
    assert result['media'] == 'Unknown'
    assert result['media_select'] == 'autoselect'
    assert 'media_type' not in result
    assert result['media_options'] == []
    result = {}

# Generated at 2022-06-13 01:17:23.112761
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    current_if = dict()
    ips = dict()
    test_object = DarwinNetwork(directory='/',
                                command='fake-bin/ifconfig',
                                interface_prefix='fakedir/ifconfig')
    test_object.parse_media_line(test_words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    del test_object
    del test_words
    del current_if
    del ips



# Generated at 2022-06-13 01:17:34.456887
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Dict with ifconfig output (without media line)
    current_if = {'device': 'utun0',
                  'macaddress': '00:00:00:00:00:00',
                  'mtu': '1380',
                  'promisc': False,
                  'state': 'up',
                  'type': 'UTUN'}
    # List of words representing media line to be parsed
    # Resulting dictionary will contain the following keys
    # with these values:
    #  'media': 'Unknown',
    #  'media_select': 'autoselect',
    #  'media_options': {'nwid': '0', 'powersave': 'off'}
    words = ["media:", "autoselect", "(nwid", "0", "powersave", "off)"]
    dn = DarwinNetwork()


# Generated at 2022-06-13 01:17:42.017498
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork({'ansible_host': 'hostname'})

    # Test 1: For a line with the standard media field, we should have the right
    # attributes set
    words = ['media:', 'autoselect', '<unknown type>']
    current_if = dict()
    dn.parse_media_line(words, current_if, dict())
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == words[1]
    assert current_if['media_type'] == words[2][1:-1]
    assert 'media_options' not in current_if

    # Test 2: For a line with the standard media field, we should have the right
    # attributes set
    words = ['media:', 'media_select', 'media_type', 'media_options']

# Generated at 2022-06-13 01:17:53.984018
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    sample_ifconfig_output = """
    media: <unknown type>
    status: inactive

    media: autoselect (1000baseT <full-duplex,flow-control>)
    status: active
    """

    network = DarwinNetwork()
    words = network.parse_media_line(
        sample_ifconfig_output.split(),
        {},
        {},
    )
    assert words['media'] == 'Unknown'
    assert words['media_select'] == '<unknown type>'

    network = DarwinNetwork()
    words = network.parse_media_line(
        sample_ifconfig_output.split(),
        {},
        {},
    )
    assert words['media_select'] == 'autoselect'
    assert words['media_type'] == '1000baseT'
    assert words['media_options']

# Generated at 2022-06-13 01:17:59.218318
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    interface = 'ethernet'
    words = ['ethernet', 'media', '<unknown', 'type>']
    current_if = {}
    ips = {}
    network = DarwinNetwork()

    network.parse_media_line(words, current_if, ips)

    assert current_if.get('media') == 'Unknown'
    assert current_if.get('media_select') == 'media'
    assert current_if.get('media_type') == 'unknown type'

# Generated at 2022-06-13 01:18:07.181313
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    media_line = ['media:', 'autoselect (1000baseT <full-duplex,flow-control>)', 'status:', 'active']
    current_if = {}
    ips = {}
    dn.parse_media_line(media_line, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '1000baseT <full-duplex,flow-control>'

# Generated at 2022-06-13 01:18:15.675416
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # test when media line contains  3 words
    media_line = ['media:', '<unknown type>', 'status:', 'active']
    darwin_network = DarwinNetwork()
    darwin_network.parse_media_line(media_line, {}, {})
    assert darwin_network._current_if['media_select'] == 'Unknown'

    # test when media line contains 4 words
    media_line = ['media:', 'autoselect', '(10baseT', '<full-duplex>)', 'status:', 'active']
    darwin_network = DarwinNetwork()
    darwin_network.parse_media_line(media_line, {}, {})
    assert darwin_network._current_if['media_select'] == 'autoselect'
    assert darwin_network._current_

# Generated at 2022-06-13 01:18:27.611763
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    current_if = {}
    ips = []
    current_if['media'] = 'Unknown'
    words = ''.split()
    current_if['media_select'] = 'Unknown'
    assert ('Unknown' == current_if['media_select'])
    word = ''.split()
    words = word
    current_if['media_select'] = 'Unknown'
    assert ('Unknown' == current_if['media_select'])
    word1 = '<unknown'.split()
    words = word1
    current_if['media_select'] = 'Unknown'
    assert ('Unknown' == current_if['media_select'])
    word2 = 'type>'.split()
    words = word2
    current_if['media_type'] = 'unknown type'

# Generated at 2022-06-13 01:18:39.128159
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    collector = DarwinNetworkCollector()
    network = DarwinNetwork()
    network.collect(collector)

    # From macOS 10.12 'ifconfig en0' output
    # Current ifconfig media line format is: "media: autoselect (<unknown type>)"
    words = ['media:', 'autoselect', '(<unknown', 'type>)']
    ips = []
    current_if={}
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'

    # From macOS 10.12 'ifconfig en0' output
    # Current ifconfig media line format is: "media: autoselect 1000baseT"
    words

# Generated at 2022-06-13 01:18:43.484690
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()

    # 1st test
    words = ['media:', 'auto', '10baseT/UTP', '(<unknown type>)' ]
    current_if = {'valid_keys': ['device']}
    ips = {}
    dn.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'auto'
    assert current_if['media_type'] == '10baseT/UTP'
    assert current_if['media_options'] == {'unknown type': None}
    assert ips == {}
    assert current_if['valid_keys'] == ['device', 'media', 'media_select', 'media_type', 'media_options']

    # 2nd test

# Generated at 2022-06-13 01:18:54.206956
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork, DarwinNetwork

    # media line is different to the default FreeBSD one
    def parse_media_line(self, words, current_if, ips):
        # not sure if this is useful - we also drop information
        current_if['media'] = 'Unknown'  # Mac does not give us this
        current_if['media_select'] = words[1]
        if len(words) > 2:
            # MacOSX sets the media to '<unknown type>' for bridge interface
            # and parsing splits this into two words; this if/else helps
            if words[1] == '<unknown' and words[2] == 'type>':
                current_if['media_select'] = 'Unknown'
                current_if['media_type']

# Generated at 2022-06-13 01:19:01.761341
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork({})
    current_if = {}
    ips = {}
    words_1 = ['media:', 'none', 'status:', 'inactive']
    darwin_network.parse_media_line(words_1, current_if, ips)
    assert(current_if['media'] == 'None')
    assert(current_if['media_type'] == 'None')
    assert(current_if['media_select'] == 'None')

    words_2 = ['media:', '10baseT/UTP', '<link>', '10baseT/UTP', '<link>', '<link>', '10baseT/UTP', '<link>', '<link>', '10baseT/UTP']

# Generated at 2022-06-13 01:19:11.421308
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    current_if = {}
    ips = {}
    words = ['media:', '<unknown type>']
    darwin_network.parse_media_line(words, current_if, ips)
    expected_result = {'media': 'Unknown',
                       'media_select': 'Unknown',
                       'media_type': 'unknown type',
                       'media_options': {}}
    assert current_if == expected_result
    current_if = {}
    darwin_network.parse_media_line(words, current_if, ips)
    expected_result = {'media': 'Unknown',
                       'media_select': 'Unknown',
                       'media_type': 'unknown type',
                       'media_options': {}}
    assert current_if == expected_result

# Generated at 2022-06-13 01:19:17.572631
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dummy_if = {}
    ifconfig = u'media: autoselect <unknown type>'
    ifconfig = ifconfig.split(' ')
    DarwinNetwork.parse_media_line(DarwinNetwork, ifconfig, dummy_if, {})
    assert dummy_if['media'] == 'Unknown'
    assert dummy_if['media_select'] == 'autoselect'
    assert dummy_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:19:21.953799
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'device': 'en0', 'type': 'ethernet'}
    words = "media: autoselect (<unknown type>)"
    DarwinNetwork.parse_media_line(DarwinNetwork, words.split(), current_if, {})
    assert current_if['media'] == 'Unknown' and current_if['media_select'] == 'autoselect' and current_if['media_options'] == {}

# Generated at 2022-06-13 01:19:26.155390
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    current_if = {}
    dn.parse_media_line(['media:', 'autoselect', '10baseT/UTP', 'status:', 'inactive'], current_if, [])
    assert current_if.get('media') == 'Unknown'
    assert current_if.get('media_select') == 'autoselect'
    assert current_if.get('media_type') == '10baseT/UTP'

# Generated at 2022-06-13 01:19:35.917581
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    drwinnw = DarwinNetwork()
    nettype = dict()

    words = ['-', '<unknown', 'type>']
    drwinnw.parse_media_line(words, nettype, 1)
    assert nettype['media_select'] == 'Unknown'
    assert nettype['media_type'] == 'unknown type'

    words = ['media', 'autoselect', '(1000baseT']
    drwinnw.parse_media_line(words, nettype, 1)
    assert nettype['media_select'] == 'autoselect'
    assert nettype['media_type'] == '(1000baseT'
    assert nettype['media_options'] == {}

    words = ['media', 'media', 'media', 'media']
    drwinnw.parse_media_line(words, nettype, 1)
   

# Generated at 2022-06-13 01:19:42.406138
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Unit tests method parse_media_line of class DarwinNetwork
    """
    iface = DarwinNetwork('ens33')
    current_if = {}
    ips = {}
    iface.parse_media_line(['media:', 'autoselect', '(1000baseT)'], current_if, ips)
    assert current_if == { 'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '(1000baseT)', 'media_options': '' }
    iface.parse_media_line(['media:', '<unknown', 'type>'], current_if, ips)
    assert current_if == { 'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type', 'media_options': '' }

# Generated at 2022-06-13 01:19:51.922821
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Unit test for method parse_media_line of class DarwinNetwork
    """
    import sys, os
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../..")
    from ansible.module_utils.facts.network.darwin import DarwinNetwork
    d = DarwinNetwork()
    # Case 1: words is empty list
    current_if = {
        'device': 'en0'
    }
    media_line = []
    d.parse_media_line(media_line, current_if)
    assert current_if['media'] == 'Unknown'  # Default value if no value is set in the list
    assert current_if['media_select'] == ''  # Default value if no value is set in the list

# Generated at 2022-06-13 01:19:59.558119
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """Tests the media line of DarwinNetwork with various examples"""
    # Create a dictionary where to store the result
    result = dict()
    # Create a list to store the words of the line
    words = ["media:", "autoselect", "(none)"]
    # Create a DarwinNetwork collector
    collector = DarwinNetwork({})
    # Execute the method parse_media_line with the list of words as argument
    collector.parse_media_line(words, result, {})
    # Check that the result is as expected
    assert(result['media'] == 'Unknown')
    assert(result['media_select'] == 'autoselect')
    assert(result['media_type'] == 'none')
    assert(result['media_options'] == {})
    # Create a dictionary where to store the result
    result = dict()
    # Create a

# Generated at 2022-06-13 01:20:10.590137
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_nw = DarwinNetwork()
    assert darwin_nw.parse_media_line(["media:", "autoselect", "ieee80211", "status:", "inactive"], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'ieee80211', 'media_options': None}
    assert darwin_nw.parse_media_line(["media:", "autoselect", "ieee80211", "noflavor", "status:", "inactive"], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'ieee80211', 'media_options': "noflavor"}

# Generated at 2022-06-13 01:20:20.142454
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:20:29.786078
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    sample_if = {}
    dn = DarwinNetwork()
    dn.parse_media_line(['media:', 'autoselect', 'none'], sample_if, None)
    assert sample_if['media'] == 'Unknown'
    assert sample_if['media_select'] == 'autoselect'
    assert sample_if['media_type'] == 'none'
    sample_if = {}
    dn.parse_media_line(['media:', '<unknown', 'type>'], sample_if, None)
    assert sample_if['media_select'] == 'Unknown'
    assert sample_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:20:40.240214
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    import json
    # create instance of DarwinNetwork
    d = DarwinNetwork()

    current_if = {}

    # line to parse
    words = ['inet', 'capabilities', '0xfc', '(autoselect', 'full-duplex,flowcontrol,auto-negotiate)', 'status', 'active']
    # call method
    d.parse_media_line(words, current_if, {})
    print(json.dumps(current_if, indent=2, sort_keys=True))
    # assert if current_if contains expected keys
    assert ('media' and 'media_select' and 'media_type' and 'media_options') in current_if

    current_if = {}
    # line to parse
    words = ['inet', '<unknown', 'type>']
    # call method
    d.parse_media

# Generated at 2022-06-13 01:20:45.484522
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    w = 'media: <unknown type> '.split()
    d = DarwinNetwork()
    d.parse_media_line(w, {}, {})
    assert d.dicts['default']['en0']['media'] == 'Unknown'
    assert d.dicts['default']['en0']['media_select'] == '<unknown'
    assert d.dicts['default']['en0']['media_type'] == 'unknown type'