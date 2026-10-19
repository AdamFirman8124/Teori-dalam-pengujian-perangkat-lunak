

# Generated at 2022-06-13 01:16:54.997776
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {'status': 'administratively down', 'speed': 0, 'virtual': False, 'media_type': 'ethernet',
               'media_select': 'autoselect', 'media': 'unknown', 'options': [], 'ipv4': [], 'ipv6': [],
               'macaddress': '00:00:00:00:00:00', 'pciid': '', 'mtu': 0, 'device': 'lo0'}
    test_words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '16384']
    test_ips = []
    DarwinNetwork().parse_media_line(test_words, test_if, test_ips)

# Generated at 2022-06-13 01:17:05.834384
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """ Unit test for method parse_media_line of class DarwinNetwork """
    DarwinNetwork = __import__('ansible.module_utils.facts.network.darwin',
                               globals(), locals(), ['DarwinNetwork'], 0).DarwinNetwork
    dn = DarwinNetwork()

    words = ['media:', 'autoselect', '(1000baseT)', 'status:', 'active']
    current_if = {
        'media': 'Unknown'  # Mac does not give us this
    }
    ips = {}
    assert dn.parse_media_line(words, current_if, ips) == None
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '1000baseT'
    assert current_

# Generated at 2022-06-13 01:17:12.494201
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words1 = ['media:', 'auto', '<unknown type>', '(none)']
    words2 = ['media:', 'autoselect', '<unknown type>', '(none)']
    words3 = ['media:', '10Gbase-KR', '<unknown type>', '(none)']
    words4 = ['media:', 'autoselect', '10Gbase-KR', '(none)']

    current_if1 = {'media': 'Unknown', 'media_select': 'auto'}
    current_if2 = {'media': 'Unknown', 'media_select': 'autoselect'}
    current_if3 = {'media': 'Unknown', 'media_select': '10Gbase-KR'}
    current_if4 = {'media': 'Unknown', 'media_select': 'autoselect'}

    d

# Generated at 2022-06-13 01:17:23.351335
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.darwin import DarwinNetwork

    # input data for method parse_media_line

# Generated at 2022-06-13 01:17:32.133394
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    current_if = {}
    words = ['good', 'word1', 'word2']

    collector = DarwinNetwork()
    collector.parse_media_line(words, current_if, False)

    assert current_if['media'] == 'Unknown'  # Mac does not give us this
    assert current_if['media_select'] == 'good'
    assert current_if['media_type'] == 'word1'
    assert current_if['media_options'] == 'word2'

# Generated at 2022-06-13 01:17:37.182648
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()

    current_if = {}
    words = ['media:', '<unknown', 'type>']
    current_if = dn.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == ''

# Generated at 2022-06-13 01:17:43.607563
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test for common media line
    data = 'media: autoselect (1000baseT <full-duplex>)'.split()
    iface = {'media': 'autoselect', 'media_select': '1000baseT', 'media_type': 'full-duplex', 'media_options': None}
    DarwinNetwork.parse_media_line(data, iface)
    assert iface['media'] == 'autoselect'
    assert iface['media_select'] == '1000baseT'
    assert iface['media_type'] == 'full-duplex'
    assert iface['media_options'] is None

    # Test for '<unknown type>' media
    data = 'media: 1000baseT <unknown type>'.split()

# Generated at 2022-06-13 01:17:55.746974
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    # create interface dictionary
    current_if = network.current_if
    # create dummy interface name
    current_if['device'] = 'em1'
    # create empty address list
    ips = []
    # create a media line as an array of words
    media_line = "media: <unknown type> <full-duplex> <100baseTX> <auto>"
    words = media_line.split()
    # try to parse the media line
    network.parse_media_line(words, current_if, ips)
    # check if the interface contain the correct media
    assert 'Unknown' == current_if['media']
    # check if the interface contain the correct media select
    assert '<unknown' == current_if['media_select']
    # check if the interface contain the correct media type
   

# Generated at 2022-06-13 01:17:59.217623
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    assert d.parse_media_line(['media:', 'autoselect', '(100baseTX)'], {}, {}) == \
        {'media_select': 'autoselect', 'media_type': '(100baseTX)'}


# Generated at 2022-06-13 01:18:04.848783
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    This test tests that parse_media_line correctly parses the media line
    present on Mac OS.
    """
    darwin = DarwinNetwork()
    words = ['media:', '<unknown', 'type>', '']
    current_if = {}
    ips = []
    darwin.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'Unknown',
                          'media_type': 'unknown type'}

# Generated at 2022-06-13 01:18:15.784767
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Initialised instance of DarwinNetwork class
    darwin_network = DarwinNetwork()

    # Valid media line for known type
    words = ["media:", "autoselect", "10baseT/UTP", "status:", "active"]
    assert darwin_network.parse_media_line(words, {}, []) == {}
    assert darwin_network.media == "Unknown"
    assert darwin_network.media_select == "autoselect"
    assert darwin_network.media_type == "10baseT/UTP"
    assert darwin_network.media_options == {}

    # Valid media line for unknown type
    words = ["media:", "<unknown", "type>", "(0x20000)", "status:", "active"]

# Generated at 2022-06-13 01:18:27.612502
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    ifc.parse_media_line(['media:' 'active', 'autoselect'], {}, {})
    assert 'active' == ifc.current_if['media_select']
    assert 'autoselect' == ifc.current_if['media_type']
    ifc.current_if = {}
    ifc.parse_media_line(['media:' 'active', 'autoselect', '(none)'], {}, {})
    assert 'active' == ifc.current_if['media_select']
    assert 'autoselect' == ifc.current_if['media_type']
    ifc.current_if = {}
    ifc.parse_media_line(['media:' 'active', 'autoselect', '10baset'], {}, {})

# Generated at 2022-06-13 01:18:39.128651
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    # Cover the case where the media line is completely included
    words = ["media:", "autoselect", "(none)", "status:", "inactive"]
    current_if = {}
    ips = {}
    d.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '(none)', 'media_options': None}
    # Cover the case where the media line is split in more words
    words = ["media:", "autoselect", "(ra", "opt)"]
    current_if = {}
    ips = {}
    d.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:18:43.738883
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    current_if = {'name': 'lo0'}
    ips = []

    # Check if parse_media_line method raise exception with incorrect number of words in media line
    media_line = 'line_with_incorrect_number_of_words'
    words = media_line.split()
    try:
        network.parse_media_line(words, current_if, ips)
        assert 'This exception must be raised because media line contains incorrect number of words'
    except Exception:
        pass

    # Check if parse_media_line method works properly with correct number of words in media line
    media_line = 'media: <unknown type>'
    words = media_line.split()

# Generated at 2022-06-13 01:18:54.422922
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network_class = DarwinNetwork()
    # test case 1 - default
    darwin_network_class.current_if = {'media': 'Unknown', 'media_select': 'none'}
    words = ['media:', 'link', '10Gbase-T']
    darwin_network_class.parse_media_line(words, darwin_network_class.current_if, {})
    assert darwin_network_class.current_if == {'media': 'Unknown', 'media_select': 'link', 'media_type': 'Base-T'}

    # test case 2 - bridge interface
    darwin_network_class.current_if = {'media': 'Unknown', 'media_select': 'none'}
    words = ['media:', '<unknown', 'type>']
    d

# Generated at 2022-06-13 01:18:58.923395
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = "media: <unknown type>"
    parsed_config = DarwinNetwork()
    parsed_config.parse_media_line(line.split(), {}, {})
    assert(parsed_config.interfaces['media'] == 'Unknown')
    assert(parsed_config.interfaces['media_select'] == '<unknown')
    assert(parsed_config.interfaces['media_type'] == 'unknown type')

# Generated at 2022-06-13 01:19:09.614582
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    fact_class = DarwinNetwork()
    # case for valid media line
    current_if = {'media': 'Unknown'}
    words = ['media:', 'autoselect', '(none)', '(none)']
    fact_class.parse_media_line(words, current_if, {})
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'none'
    assert current_if['media_options'] == {}
    # case for invalid media line
    current_if = {'media': 'Unknown'}
    words = ['media:', 'fixed', '(none)']
    fact_class.parse_media_line(words, current_if, {})
    assert current_if['media_select'] == 'fixed'
    assert current_if['media_type']

# Generated at 2022-06-13 01:19:14.059719
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # example line
    line = "media: <unknown type>"
    current_if = {}
    words = line.split()
    ips = []
    DarwinNetwork(None).parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '<unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in cu

# Generated at 2022-06-13 01:19:20.874712
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_module = DarwinNetwork()

# Generated at 2022-06-13 01:19:31.893177
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Creating instance of DarwinNetwork
    darwin_network = DarwinNetwork()

    # Create dictionary 'current_if'
    current_if = {}

    # Calling 'parse_media_line' method to test it
    darwin_network.parse_media_line(["media:", "autoselect", "(none)"], current_if, None)

    # Assert not equal
    assert current_if.get('media') != 'Unknown', "The input parameter media is unknown"

    # Calling 'parse_media_line' method to test it
    darwin_network.parse_media_line(["media:", "autoselect", "10baseT/UTP"], current_if, None)

    # Assert the output
    assert current_if.get('media') == 'Unknown', "The input parameter media is not unknown"

# Generated at 2022-06-13 01:19:42.614984
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = DarwinNetwork({'netstat_path':'/bin/netstat'})
    # test case: Mac OS X 10.12.6, en0 interface
    words = ['en0', '(autoselect)', 'active', 'none']
    current_if = {}
    ips = {}
    iface.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'active'
    assert current_if['media_options'] == 'none'

    # test case: MacOSX sets the media to '<unknown type>' for bridge interface
    # and parsing splits this into two words; this if/else helps

# Generated at 2022-06-13 01:19:48.373637
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork(None)

    current_if = dict()
    ips = dict()

    words = ['unknown', '<unknown', 'type>']
    ifc.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:19:56.946060
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    fake_current_if = dict()
    fake_ips = dict()

    test_DarwinNetwork = DarwinNetwork('')

    # fake_words = ['']
    # test_DarwinNetwork.parse_media_line(fake_words)

    # fake_words = ['']
    # test_DarwinNetwork.parse_media_line(fake_words, fake_current_if, fake_ips)

    # fake_words = ['unknown']
    # test_DarwinNetwork.parse_media_line(fake_words, fake_current_if, fake_ips)

    # fake_words = ['unknown']
    # test_DarwinNetwork.parse_media_line(fake_words, fake_current_if, fake_ips)

    # fake_words = ['unknown']
    # test_DarwinNetwork.parse_media_

# Generated at 2022-06-13 01:20:05.309411
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media_line_1 = '<unknown type>'
    words_1 = media_line_1.split()
    current_if_1 = {}
    ips_1 = {}

    DarwinNetwork.parse_media_line(words_1, current_if_1, ips_1)

    assert current_if_1.get('media') == 'Unknown'
    assert current_if_1.get('media_select') == '<unknown'
    assert current_if_1.get('media_type') == 'type>'
    assert current_if_1.get('media_options') == None

# Generated at 2022-06-13 01:20:15.586273
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """Unit test of DarwinNetwork.parse_media_line"""
    f = DarwinNetwork()
    current_if = {'if': 'lo0'}
    media_line = 'media: autoselect '
    # test a media line with no options
    words = media_line.split()
    f.parse_media_line(words, current_if, [])
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] is None
    assert current_if['media_options'] is None
    # test a media line with options
    media_line = 'media: autoselect (10baseT/UTP <half-duplex>)'
    # test a media line with no options
    words = media_line.split()

# Generated at 2022-06-13 01:20:23.275530
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    m_interfaces = {'en0': {}}

    dn = DarwinNetwork(m_interfaces)

    dn.parse_media_line(['en0', 'autoselect', '<unknown type>'], m_interfaces['en0'], None)
    assert {'media': 'Unknown', 'media_select': 'autoselect'} == m_interfaces['en0']

    dn.parse_media_line(['en0', '10baseT/UTP', '<unknown type>'], m_interfaces['en0'], None)
    assert {'media': 'Unknown', 'media_select': '10baseT/UTP', 'media_type': 'unknown type'} == m_interfaces['en0']


# Generated at 2022-06-13 01:20:32.979478
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = "media: <unknown type> <unknown ssid> <unknown> <warning, no country information>"
    line_as_words = ['media:', '<unknown', 'type>', '<unknown', 'ssid>', '<unknown>', '<warning,', 'no', 'country', 'information>']
    interface = dict()
    ansible_network.DarwinNetwork.parse_media_line(line_as_words, interface, {})
    assert interface['media'] == 'Unknown'
    assert interface['media_select'] == '<unknown type>'
    assert interface['media_type'] == 'unknown type'
    assert interface['media_options'] == 'unknown ssid,unknown,warning, no country information'

# Generated at 2022-06-13 01:20:43.338824
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    assert DarwinNetwork.parse_media_line(None, ['media', '1000baseTX'], None) == \
        {'media': 'Unknown', 'media_select': '1000baseTX', 'media_type': '1000baseTX'}
    assert DarwinNetwork.parse_media_line(None, ['media', '10GbaseT', '(', '10GbaseT'], None) == \
        {'media': 'Unknown', 'media_select': '10GbaseT', 'media_type': '10GbaseT'}

# Generated at 2022-06-13 01:20:47.762437
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_words = ['media:', 'autoselect', '<unknown type>', '(none)', '(none)']
    assert DarwinNetwork.parse_media_line(DarwinNetwork, test_words, {}, None) == \
           (None, {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'unknown type', 'media_options': ['none']})

# Generated at 2022-06-13 01:20:55.936687
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'inet': [], 'inet6': []}
    if_lines = {'media': '<unknown type>'}
    facts = DarwinNetwork({'module_hw': False}, if_lines)

    # Test 1 - function should set media_select to 'Unknown'
    facts.parse_media_line(if_lines['media'].split(), current_if, {})
    assert current_if['media_select'] == 'Unknown'

    # Test 2 - function should set media_type to 'unknown type'
    assert current_if['media_type'] == 'unknown type'