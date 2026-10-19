

# Generated at 2022-06-13 01:16:54.469415
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()

    media_line_1 = "media: <unknown type>".split()
    current_if_1 = {}
    ips_1 = []
    network.parse_media_line(media_line_1, current_if_1, ips_1)
    assert 'Unknown' == current_if_1['media_select']
    assert 'unknown type' == current_if_1['media_type']

    media_line_2 = "media: autoselect (1000baseT <full-duplex>)" .split()
    current_if_2 = {}
    ips_2 = []
    network.parse_media_line(media_line_2, current_if_2, ips_2)
    assert 'autoselect' == current_if_2['media_select']

# Generated at 2022-06-13 01:17:03.022419
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Setup a object of type DarwinNetwork and run parse_media_line on it
    network_obj = DarwinNetwork()
    actual_output_dict = network_obj.parse_media_line(
        ['Supported', 'media:', '<unknown type>'], {}, {})

    expected_output_dict = {'media': 'Unknown', 'media_select': 'Unknown',
                            'media_type': 'unknown type', 'media_options': {}}

    assert actual_output_dict == expected_output_dict, \
        "test_DarwinNetwork_parse_media_line() has failed"

# Generated at 2022-06-13 01:17:09.642284
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # setup
    current_if = {'media': '', 'media_select': '', 'media_type': '', 'media_options': ''}
    words = ['media:', 'autoselect', '<unknown', 'type>']

    # expected results
    expected_current_if = {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'unknown type',
                           'media_options': ''}

    # test
    DarwinNetwork.parse_media_line(None, words, current_if)
    assert expected_current_if == current_if

# Generated at 2022-06-13 01:17:10.517099
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    net = DarwinNetwork(None)
    assert net.platform == "Darwin"


# Generated at 2022-06-13 01:17:13.786233
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    macDarwin = DarwinNetwork()
    assert macDarwin.platform == 'Darwin'

# Generated at 2022-06-13 01:17:24.203211
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    t_obj = DarwinNetwork()

    # Test with 'B'
    test_input = {
        'devname': 'bge0',
        'type': 'bge',
        'ipv4': [{'address': '10.20.30.40', 'subnet': '255.255.0.0'}],
        'media': "1000baseBX-FD media: <unknown type>"
    }

# Generated at 2022-06-13 01:17:34.936922
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_if = DarwinNetwork()
    # test known case
    current_if = {}
    ips = {}
    words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    darwin_if.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == ''
    # test unknown case
    current_if = {}
    ips = {}
    words = ['media:', '<unknown', 'type>', 'status:', 'inactive']

# Generated at 2022-06-13 01:17:40.011930
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_mac = 'broadcast media'
    words = test_mac.split()
    current_if = dict()
    ips = dict()
    mac_network = DarwinNetwork(None)
    mac_network.parse_media_line(words, current_if, ips)
    assert 'Unknown' == current_if['media']
    assert 'broadcast' == current_if['media_select']
    assert 'media' == current_if['media_type']
    assert None == current_if['media_options']

# Generated at 2022-06-13 01:17:51.817091
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:18:00.949983
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_object = DarwinNetwork()
    assert test_object.parse_media_line(['media:', 'autoselect'], dict(), dict()) == dict(media='Unknown', media_select='autoselect')
    assert test_object.parse_media_line(['media:', 'autoselect', '(100baseTX)'], dict(), dict()) == dict(media='Unknown', media_select='autoselect', media_type='100baseTX')
    assert test_object.parse_media_line(['media:', 'autoselect', '(100baseTX)', 'full-duplex'], dict(), dict()) == dict(media='Unknown', media_select='autoselect', media_type='100baseTX', media_options=dict(full_duplex='full-duplex'))
    
    # Test for https://github.com/ansible

# Generated at 2022-06-13 01:18:08.751769
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media', '<unknown', 'type>']
    current_if = {}
    ips = []
    DarwinNetwork.parse_media_line(None, words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:18:17.016717
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words1 = ['media:', 'autoselect', '100baseTX', 'full-duplex']
    current_if1 = {'macaddress': '08:00:27:67:69:d2'}
    DarwinNetwork.parse_media_line(DarwinNetwork(), words1, current_if1, {})
    assert current_if1['media'] == 'Unknown'
    assert current_if1['media_select'] == words1[1]
    assert current_if1['media_type'] == words1[2]
    assert current_if1['media_options'] == 'full-duplex'

    words2 = ['media:', '<unknown', 'type>']
    current_if2 = {}
    DarwinNetwork.parse_media_line(DarwinNetwork(), words2, current_if2, {})
    assert current

# Generated at 2022-06-13 01:18:27.718481
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dnetwork = DarwinNetwork()
    #media line has 4 words
    words = ['media:', '<unknown', 'type>', '']
    current_if = {}
    ips = []
    dnetwork.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == {}
    #media line has 3 words
    words = ['media:', '<autoselect>', '(100baseTX <full-duplex>)']
    current_if = {}
    ips = []
    dnetwork.parse_media_line(words, current_if, ips)
    assert current_if['media']

# Generated at 2022-06-13 01:18:39.128972
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test parsing devices of type: en:ethernet and de:ethernet
    current_if = {}
    words = ["media:", "autoselect", "1000baseT", "mediaopt", "full-duplex"]
    DarwinNetwork().parse_media_line(words, current_if, [])
    assert current_if['media'] == "Unknown"
    assert current_if['media_select'] == words[1]
    assert current_if['media_type'] == words[2]
    assert current_if['media_options'] == words[3:]

    # test parsing devices of type: de:bridge
    current_if = {}
    words = ["media:", "<unknown", "type>"]
    DarwinNetwork().parse_media_line(words, current_if, [])

# Generated at 2022-06-13 01:18:45.292861
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Using state
    # media: <unknown type>
    # media_select: <unknown type>
    # media_type: unknown type
    # and parsing
    # ('<unknown type>', '<unknown type>')
    current_if = {}
    result_if = {'media': 'Unknown',
                 'media_select': '<unknown type>',
                 'media_type': 'unknown type'}
    DarwinNetwork.parse_media_line(('<unknown type>', '<unknown type>'), current_if, "")
    assert current_if == result_if

    # Using state
    # media: <unknown type>
    # media_select: <unknown type>
    # media_type: unknown type
    # and parsing
    # ('<unknown', 'type>')
    current_if = {}
    result_if

# Generated at 2022-06-13 01:18:52.970460
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    expected_if = {
        'media': 'Unknown',
        'media_type': 'unknown type',
        'media_select': '<unknown',
        'media_options': {}
    }
    actual_if = {}
    current_if = {}
    ips = {}
    words = ['media:', '<unknown', 'type>']
    DarwinNetwork().parse_media_line(words, current_if, ips)
    # compare dictionary values
    actual_if = current_if
    assert expected_if == actual_if

# Generated at 2022-06-13 01:18:59.121602
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = {'media': '', 'media_options': '', 'media_select': '', 'media_type': ''}
    words = ['media:', '<unknown', 'type>']
    expected = {'media': 'Unknown', 'media_options': '', 'media_select': 'Unknown', 'media_type': 'unknown type'}

    DarwinNetwork.parse_media_line(None, words, iface)

    assert iface == expected

# Generated at 2022-06-13 01:19:05.798213
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    collector = DarwinNetwork(None)
    current_if = {'ifname': 'bridge0'}
    words = ['media:', '<unknown', 'type>', '(', 'automatic', ')']
    collector.parse_media_line(words, current_if, [])
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options']['automatic']

# Generated at 2022-06-13 01:19:09.116592
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()
    darwin_net_current_if = dict()

    darwin_net_words = ['media:', 'autoselect', '<unknown type>']
    darwin_net.parse_media_line(darwin_net_words, darwin_net_current_if, dict())
    assert darwin_net_current_if['media'] == 'Unknown'
    assert darwin_net_current_if['media_select'] == 'autoselect'
    assert darwin_net_current_if['media_type'] == 'unknown type'

    darwin_net_words = ['media:', 'autoselect', '100baseTX', '(100baseTX<half-duplex>)']

# Generated at 2022-06-13 01:19:20.871473
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create a new DarwinNetwork object and test the parse_media_line() method
    current_if = {}  # initialise the 'current_if' list
    words = []  # initialise the 'words' list
    darwin = DarwinNetwork()

    # check the following cases:
    # - media_select is first in line
    # - media_type has spaces and needs to be split into two words
    # - media_options is set
    # - media_options is set, but has quotes
    # - no media_type, so it defaults to 'Unknown'
    # - no media_options, but media_type is set

    # define the following lists to test:
    media_select = ['media:', 'media:', 'media:', 'media:', 'media:', 'media:']