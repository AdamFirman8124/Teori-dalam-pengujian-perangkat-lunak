

# Generated at 2022-06-13 01:16:45.093445
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    '''
    Test to make sure parse_media_line returns correct if options
    '''


# Generated at 2022-06-13 01:16:54.672613
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create a DarwinNetwork object
    d = DarwinNetwork()
    # known words will come from method get_interfaces_info of class DarwinNetwork
    words = [
        "0x2",
        "media:",
        "<unknown type>",
        "(none)",
    ]
    # current_if will come from method get_interfaces_info of class DarwinNetwork

# Generated at 2022-06-13 01:17:05.795616
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    current_if = {}
    ips = {}

    # first test case if words is ['media:', '<unknown type>']
    darwin_network.parse_media_line(['media:', '<unknown type>'], current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == None
    assert ips == {}
    current_if.clear()

    # second test case if words is ['media:', 'IEEE', '802.11', '(autoselect)']

# Generated at 2022-06-13 01:17:12.434873
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    ips = {}
    words = ['media:', 'IEEE', '802.11', '(autoselect)', 'status:', 'inactive']
    expected_if = {'media_select': 'IEEE', 'media_type': '802.11', 'media': 'Unknown', 'media_options': '(autoselect)'}
    net = DarwinNetwork()
    net.parse_media_line(words, current_if, ips)
    assert(current_if == expected_if)

    current_if = {}
    ips = {}
    words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    expected_if = {'media_select': 'Unknown', 'media': 'Unknown', 'media_type': 'unknown type'}
    net = DarwinNetwork()

# Generated at 2022-06-13 01:17:23.351618
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {}
    test_ips = []

    # words will have only media_type
    test_words = ["media:", "autoselect", "10baseT/UTP"]
    # the code to test
    DarwinNetwork._parse_media_line(test_if, test_words, test_ips)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == '10baseT/UTP'
    assert test_if['media_options'] == None

    # words will have both media_select and media_type
    test_words = ["media:", "10baseT/UTP", "(none)"]
    # the code to test

# Generated at 2022-06-13 01:17:34.456915
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Fake module
    module = type('module', (), dict(params={}, failure=lambda x: False))

    drwinNetwork = DarwinNetwork(module)

    # init the current_if dictionary
    current_if = dict(name={}, type={})

    # Case 1:
    # media line is "media: autoselect (1000baseT <full-duplex>) status: inactive"
    words = ['media:', 'autoselect', '1000baseT', '<full-duplex>', 'status:', 'inactive']
    drwinNetwork.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '1000baseT'

# Generated at 2022-06-13 01:17:37.760741
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # For more information about the unit test see also
    # modules/utils/facts/network/generic_bsd.py
    # method test_GenericBsdIfconfigNetwork_parse_media_line()
    test_ifc = {'name': 'en0'}
    test_ips = []
    darwin_network = DarwinNetwork(None)

    # Test case: no 'media:' line in ifconfig output
    test_words = ['media:', 'no', 'media']
    test_ifc['media'] = 'Unknown'
    test_ifc['media_select'] = 'no'

    new_ifc = darwin_network.parse_media_line(test_words, test_ifc, test_ips)

# Generated at 2022-06-13 01:17:48.652127
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = DarwinNetwork()
    media_tests = [
        (('media:' + 'autoselect'), {'media_select': 'autoselect'}),
        (('media:' + '100baseTX', 'mediaopt', 'full-duplex'), {'media_select': '100baseTX', 'media_options': 'full-duplex', 'media_type': 'mediaopt'}),
        (('media:', '<unknown', 'type>'), {'media_select': 'Unknown', 'media_type': 'unknown type'}),
    ]
    current_if = {}
    ips = []
    for test_line, result in media_tests:
        # Set
        test.parse_media_line(test_line, current_if, ips)
        # Test

# Generated at 2022-06-13 01:17:58.220317
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    current_if = {'name': 'eth0'}

    words = ['media', 'ethernet', '10baseT/UTP']
    dn.parse_media_line(words, current_if, {})
    expected_dict = {'name': 'eth0', 'media': 'Unknown',
                     'media_select': 'ethernet', 'media_type': '10baseT/UTP',
                     'media_options': None}
    assert current_if == expected_dict

    words = ['media', 'ethernet', '10baseT/UTP', '(HDx4)']
    dn.parse_media_line(words, current_if, {})

# Generated at 2022-06-13 01:18:06.427005
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = dict()
    words = list()
    # media line is different to the default FreeBSD one
    # media line, which is the only difference to the parent class
    # not sure, if this is useful, since we also drop information
    ifc = DarwinNetwork(0, 0)
    words = ['media:', '<unknown', 'type>', 'autoselect']
    ifc.parse_media_line(words, current_if, list())
    assert current_if == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type', 'media_options': {'autoselect': 'on'}}
    words = ['media:', 'autoselect', '100baseTX', 'autoselect']
    ifc.parse_media_line(words, current_if, list())