

# Generated at 2022-06-13 01:16:48.065307
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_str = " inet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255"
    words = test_str.split(' ')
    current_if = {'inet': {}, 'inet6': {}}
    DarwinNetwork().parse_media_line(words, current_if, ['192.168.1.1'])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'inet'
    assert current_if['media_type'] == ''
    assert current_if['media_options'] == ['192.168.1.1']

    test_str = " inet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255"
    words = test_str.split(' ')
    current_if

# Generated at 2022-06-13 01:16:57.618783
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    id = DarwinNetwork()
    current_if = {}
    ips = {}
    # Test case 1
    words = ['media:', 'autoselect', '(none)']
    id.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'autoselect' and current_if['media_options'] == []
    # Test case 2
    words = ['media:', '<unknown', 'type>', '(none)']
    id.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Unknown' and current_if['media_type'] == 'unknown type' and current_if['media_options'] == []
    # Test case 3
    words = ['media:', '<unknown', 'type>', 'supported']

# Generated at 2022-06-13 01:17:07.507760
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    current_if = {}
    ips = {}
    assert darwin_network.parse_media_line(['<unknown', 'type>'], current_if, ips) == {'media': 'Unknown', 'media_select': '<unknown', 'media_type': 'unknown type'}
    assert darwin_network.parse_media_line(['<unknown', 'word>'], current_if, ips) == {'media': 'Unknown', 'media_select': '<unknown', 'media_type': 'word>'}

# Generated at 2022-06-13 01:17:10.234826
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    words = ('media:', '<unknown', 'type>')
    current_if = {'name': 'bridge100'}

    expected_result = {'name': 'bridge100',
                       'media': 'Unknown',
                       'media_select': 'Unknown',
                       'media_type': 'unknown type'}

    DarwinNetwork.parse_media_line(DarwinNetwork, words,
                                   current_if, None)
    assert expected_result == current_if

# Generated at 2022-06-13 01:17:19.528278
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = DarwinNetwork()
    words = ['media:', 'autoselect', '<unknown type>']
    current_if = {'type': 'unknown'}
    ips = {}
    iface.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:17:26.689271
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork({}, None)
    test_cases = [
        ( ['media:', 'autoselect', '(100baseTX <full-duplex>)'], {
            'media': 'Unknown', 'media_select': 'autoselect',
            'media_type': '100baseTX <full-duplex>'
        } ),
        ( ['media:', '<unknown', 'type>', '(100baseTX <full-duplex>)'], {
            'media': 'Unknown', 'media_select': 'Unknown',
            'media_type': 'unknown type',
            'media_options': '100baseTX <full-duplex>'
        } ),
    ]
    for test_case in test_cases:
        words = test_case[0]
        expected = test_case[1]
        current_if = dict

# Generated at 2022-06-13 01:17:36.994022
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    assert dn.parse_media_line(['media:', 'autoselect', '(none)'], {}, {}) == \
        { 'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '(none)' }
    assert dn.parse_media_line(['media:', 'autoselect', '(none)', 'full-duplex'], {}, {}) == \
        { 'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '(none)', 'media_options': 'full-duplex' }

# Generated at 2022-06-13 01:17:46.254974
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    current_if = {}
    dn.parse_media_line(["media:", "auto", "(none)"], current_if, {})
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'auto'
    assert current_if['media_type'] == '(none)'
    assert 'media_options' not in current_if

    dn.parse_media_line(["media:", "<unknown", "type>"], current_if, {})
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in current_if

# Generated at 2022-06-13 01:17:55.206597
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    my_DarwinNetwork = DarwinNetwork()

    # set up a dictionary to pass to parse_media_line
    words = ['media:', 'autoselect', '<unknown type>']
    current_if = {'media': 'Unknown'}
    ips = 'none'

    # call the method to be tested
    my_DarwinNetwork.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:18:03.230241
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()

    darwin_mock_line = ['media: <unknown type>', 'unknown', 'type>']
    darwin_current_if = {}
    darwin_ips = {}
    darwin_network.parse_media_line(line=darwin_mock_line, current_if=darwin_current_if, ips=darwin_ips)
    assert darwin_current_if['media_select'] == 'Unknown'
    assert darwin_current_if['media_type'] == 'unknown type'
    assert darwin_current_if['media_options'] == []

test_DarwinNetwork_parse_media_line()

# Generated at 2022-06-13 01:18:15.452031
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface1 = {'name': 'en0'}
    iface2 = {'name': 'en1'}
    ips = []
    dn = DarwinNetwork()

    # media line is different to the default FreeBSD one
    words = dn.parse_media_line(['media:', 'autoselect', '(none)'], iface1, ips)
    assert words is None
    assert iface1['media'] == 'Unknown'
    assert iface1['media_select'] == 'autoselect'
    assert iface1['media_type'] == '(none)'
    assert iface1['media_options'] == ''

    words = dn.parse_media_line(['media:', 'autoselect', '(100baseTX)'], iface2, ips)
    assert words is None
    assert iface2

# Generated at 2022-06-13 01:18:21.384545
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    w = [None, 'none']
    i = {}
    i['media'] = 'Unknown'
    i['media_select'] = 'none'
    DarwinNetwork._parse_media_line(w, i)

    w = [None, 'manual', '(100baseTX)', 'full-duplex']
    i = {}
    i['media'] = 'Unknown'
    i['media_select'] = 'manual'
    i['media_type'] = '100baseTX)'
    i['media_options'] = ['full-duplex']
    DarwinNetwork._parse_media_line(w, i)

    w = [None, '<unknown', 'type']
    i = {}
    i['media'] = 'Unknown'
    i['media_select'] = 'Unknown'

# Generated at 2022-06-13 01:18:27.935438
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    This test is to ensure that parsing of media lines of Darwin platform
    works as expected.
    """
    # call to DarwinNetwork
    net = DarwinNetwork()

    # Set dummy variables
    media_words = ["media:",
                   "autoselect",
                   "status:",
                   "inactive"]
    ips = dict()
    current_if = dict()
    current_if['name'] = 'en0'

    # Call parse_media_line
    net.parse_media_line(media_words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_status'] == 'inactive'

    # Reset dummy variables
    current_if = dict()

# Generated at 2022-06-13 01:18:39.214641
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()

    # Test if the length of words is 2
    line = 'media: Ethernet autoselect (1000baseT <full-duplex>)  '
    words = line.split()
    current_if = {}
    ips = {}
    dn.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Ethernet'
    assert current_if['media_type'] == '1000baseT'
    assert current_if['media_options'] == 'full-duplex'

    # Test if the length of words is 3
    line = 'media: Ethernet autoselect <unknown type>  '
    words = line.split()
    current_if = {}
    ips = {}
    d

# Generated at 2022-06-13 01:18:42.354790
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = "media: <unknown type> <unknown subtype>"
    words = line.split()
    current_if = {"name": "igb0"}
    ips = []
    network = DarwinNetwork(current_if, ips)
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '<unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:18:49.209273
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    collector = DarwinNetworkCollector()
    d = DarwinNetwork()
    
    current_if = {}
    ips = []
    words = ['media:','autoselect','<unknown','type>']
    d.parse_media_line(words, current_if, ips)

    assert current_if == {'media': 'Unknown', 
                          'media_select': 'autoselect', 
                          'media_type': 'unknown type'}
    assert ips == []

# Generated at 2022-06-13 01:18:58.100949
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Test for parse_media_line
    """
    network = DarwinNetwork()

    current_if = {'device': 'en0', 'macaddress': '02:00:00:00:00:00'}
    words = ['media:', 'autoselect', '10baseT/UTP', '(none)']

    network.parse_media_line(words, current_if, {})

    assert 'media' in current_if
    assert current_if['media'] == 'Unknown'
    assert 'media_select' in current_if
    assert current_if['media_select'] == 'autoselect'
    assert 'media_type' in current_if
    assert current_if['media_type'] == '10baseT/UTP'



# Generated at 2022-06-13 01:19:09.178211
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'media': 'Unknown'}
    words = ['inet6', 'fe80::5e72:5fff:fe51:5ba5%awdl0', 'prefixlen', '64', 'scopeid', '0x9']
    expected_current_if = {'media': 'Unknown'}
    # MacOSX sets the media to '<unknown type>' for bridge interface
    # and parsing splits this into two words; this if/else helps
    current_if = DarwinNetwork().parse_media_line(words, current_if, None)
    assert current_if == expected_current_if, "current_if did not meet expectations"

    words = ['inet6', '<unknown', 'type>']

# Generated at 2022-06-13 01:19:20.869132
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Apple MacOS includes the media type in the output of ifconfig
    # but not the media speed (unlike FreeBSD)
    current_if = {'name': 'en0'}
    line = "media: <unknown type> status: inactive"
    words = line.split()
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, None)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == ''
    assert current_if['media'] == 'Unknown'
    assert current_if['status'] == 'inactive'

    current_if = {'name': 'en0'}
    line = "media: autoselect <full-duplex> status: inactive"

# Generated at 2022-06-13 01:19:31.859265
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Method parse_media_line => test with differents values
    """
    def assertMediaLine(words, current_if, ips, expected):
        instance = DarwinNetwork()
        instance.parse_media_line(words, current_if, ips)

        assert(current_if['media'] == expected['media'])
        assert(current_if['media_select'] == expected['media_select'])
        assert(current_if['media_type'] == expected['media_type'])
        assert(current_if['media_options'] == expected['media_options'])

    # MacOSX sets the media to '<unknown type>' for bridge interface
    # and parsing splits this into two words; this test helps
    # to verify that the method parse_media_line work as expected

# Generated at 2022-06-13 01:19:40.530235
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_line = 'media: autoselect (<unknown type>) status: inactive'
    current_if = dict()
    ips = dict()
    import copy
    dn = copy.deepcopy(DarwinNetwork())
    dn.parse_media_line(test_line.split(), current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == 'inactive'

# Generated at 2022-06-13 01:19:50.485718
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test 1
    ifconfig = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 2c:f0:ee:4a:4a:4a
	inet6 fe80::2ef0:eeff:fe4a:4a4a%en0 prefixlen 64 secured scopeid 0x5
	inet 192.168.1.102 netmask 0xffffff00 broadcast 192.168.1.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (1000baseT <full-duplex,flow-control>)
	status: active
"""
    network = DarwinNetwork()
    # The last line of the output starts with a media, so the words are in this order:

# Generated at 2022-06-13 01:19:58.398429
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    net = DarwinNetwork()
    assert net.parse_media_line(['media:', 'IEEE802.11', '802.11b'], {}, {})['media_select'] == 'IEEE802.11'
    assert net.parse_media_line(['media:', 'IEEE802.11', '802.11b'], {}, {})['media_type'] == "802.11b"
    assert net.parse_media_line(['media:', 'IEEE802.11', '802.11b'], {}, {})['media'] == 'Unknown'
    assert net.parse_media_line(['media:', 'IEEE802.11', '802.11b', 'mediaopt'], {}, {})['media_options'] == 'mediaopt'

# Generated at 2022-06-13 01:20:09.353191
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test for case: words = ['media:', 'autoselect']
    # Test for case: words = ['media:', 'autoselect', '(none)']
    # Test for case: words = ['media:', 'autoselect', '(100baseTX <full-duplex>)', 'status:', 'active']
    # Test for case: words = ['media:', '<unknown type>', 'status:', 'active']
    # Test for case: words = ['media:', '<unknown', 'type>', 'status:', 'active']
    darwin_net = DarwinNetwork()
    line = 'media: autoselect'
    current_if = dict()
    ips = dict()
    darwin_net.parse_media_line(line.split(), current_if, ips)

# Generated at 2022-06-13 01:20:19.022340
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    class TestDarwinNetwork:
        def __init__(self):
            self.current_if = {}

    t0 = TestDarwinNetwork()
    d0 = DarwinNetwork(t0)
    d0.parse_media_line(['', 'auto', '(none)'], t0.current_if, None)
    assert t0.current_if['media'] == 'Unknown'
    assert t0.current_if['media_select'] == 'auto'
    assert t0.current_if['media_type'] == '(none)'
    assert not t0.current_if.get('media_options')

    t1 = TestDarwinNetwork()
    d1 = DarwinNetwork(t1)

# Generated at 2022-06-13 01:20:25.151136
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {}
    test_ips = []
    test_words = [ 'media:', 'none', 'status:', 'inactive' ]
    DarwinNetwork.parse_media_line(test_if, test_ips, test_words)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'none'
    assert test_if['media_type'] == 'none'
    assert test_if['media_options'] == 'none'

    test_words = ['media:', 'autoselect', 'status:', 'active']
    DarwinNetwork.parse_media_line(test_if, test_ips, test_words)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:20:32.420668
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    current_if = {}
    ips = {}
    words = ['media:', 'autoselect', 'status:', 'inactive']
    d.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == words[1]
    assert current_if['media_type'] == ''
    assert current_if['media_options'] == ''
    assert current_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:20:42.787690
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    ifc.parse_media_line(['media:', 'autoselect', '(none)'], {}, {})
    assert ifc.current_if['media'] == 'Unknown'
    assert ifc.current_if['media_select'] == 'autoselect'
    assert ifc.current_if['media_type'] == '(none)'

    ifc.parse_media_line(['media:', 'autoselect', '<unknown type>'], {}, {})
    assert ifc.current_if['media'] == 'Unknown'
    assert ifc.current_if['media_select'] == 'Unknown'
    assert ifc.current_if['media_type'] == 'unknown type'


# Generated at 2022-06-13 01:20:52.785170
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
  darwin_network = DarwinNetwork()
  current_if = {}
  ips = {}

  # Positional case
  words = ["media:", "autoselect", "(none)", "status:", "inactive"]
  darwin_network.parse_media_line(words, current_if, ips)
  assert current_if == {"media": "Unknown", "media_select": "autoselect", "media_type": "none", "media_options": {}}

  # Positional case with more than 4 elements
  words = ["media:", "autoselect", "(none)", "status:", "inactive", "test:", "test1", "test2", "test3"]
  darwin_network.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:21:02.538546
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    assert dn._parse_media_line(['media:','autoselect','<unknown type>'], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect'}
    assert dn._parse_media_line(['media:','<unknown','type>'], {}, {}) == {'media': 'Unknown', 'media_select': '<unknown'}
    assert dn._parse_media_line(['media:','autoselect','<ether>'], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'ether'}

# Generated at 2022-06-13 01:21:19.349386
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    current_if = {}

    # Test good value
    words = ['media:', 'autoselect', '(none)', 'status:', 'active']
    dn.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_options'] == 'none'
    assert current_if['media_type'] == 'unknown type'

    # Test good value with quotes
    words = ['media:', 'autoselect', '(\'full-duplex\',autoselect)', 'status:', 'active']
    dn.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
   

# Generated at 2022-06-13 01:21:27.339870
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    net_cls = DarwinNetwork()
    words = ['media', 'autoselect', '(none)']

    net_cls.parse_media_line(words, current_if, {})
    assert current_if == {'media_select': 'autoselect', 'media': 'Unknown', 'media_type': u'none'}

    current_if = {}
    words = ['media', 'autoselect', '(none)', '<full-duplex>']
    net_cls.parse_media_line(words, current_if, {})
    assert current_if == {'media_select': 'autoselect', 'media': 'Unknown',
                          'media_type': u'none', 'media_options': [u'full-duplex']}

# Generated at 2022-06-13 01:21:32.516449
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = "media: autoselect (<unknown type>)"
    ifs = dict()
    current_if = dict()
    ips = dict()
    DarwinNetwork.parse_media_line(DarwinNetwork, line.split(), current_if, ips)
    assert 'media' in current_if
    assert current_if['media'] == 'Unknown'
    assert 'media_select' in current_if
    assert current_if['media_select'] == 'autoselect'
    assert 'media_type' in current_if
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in current_if
    return

# Generated at 2022-06-13 01:21:40.861085
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # noinspection PyUnusedLocal
    def __init__(word):
        pass
    # create a copy of the class
    # noinspection PyTypeChecker
    network = DarwinNetwork(__init__)
    # get the method parse_media_line
    method_parse_media_line = getattr(network, 'parse_media_line')
    # create a list of words
    words = ['media:', 'autoselect', '(none)']
    # create a dict
    current_if = dict()
    # execute method
    method_parse_media_line(words, current_if, ips=None)
    # test element
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'none'

# Generated at 2022-06-13 01:21:49.494690
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Do not use assertIsInstance from six.moves.assert_moves because it does not exist in Python 2.7.5
    # see https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance
    assertion = isinstance(DarwinNetwork(), NetworkCollector)
    assert assertion, "DarwinNetwork() should be an instance of class NetworkCollector"

    # Do not use assertIsNone from six.moves.assert_moves because it does not exist in Python 2.7.5
    # see https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone
    assertion = isinstance(DarwinNetwork().parse_media_line([],'eth0', {}), None)

# Generated at 2022-06-13 01:21:56.436568
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    current_if = {}
    darwin_network.parse_media_line(['media:', 'autoselect', '(none)'], current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    current_if = {}

# Generated at 2022-06-13 01:22:07.174499
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()

# Generated at 2022-06-13 01:22:15.207916
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    # Single element
    current_if = {}
    words = "media: <unknown type>"
    darwin_network.parse_media_line(words, current_if)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    # Three element
    current_if = {}
    words = "media: autoselect (none)"
    darwin_network.parse_media_line(words, current_if)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'None'

    # Another 3 elements

# Generated at 2022-06-13 01:22:25.672371
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    mac_network = DarwinNetwork()
    current_if = {'name': 'en0',
                  'mac_address': '00:0a:f7:8e:bd:b1',
                  'type': 'ether',
                  'mtu': '1500',
                  'flags': ['UP'],
                  'ipv4': {'address': '192.168.1.103', 'netmask': '255.255.255.0', 'broadcast': '192.168.1.255'}}
    mac_network.parse_media_line(['media:', 'autoselect', 'status:', 'inactive'], current_if, {})
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_options'] == {'status': 'inactive'}


# Generated at 2022-06-13 01:22:34.275704
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    module = DarwinNetwork()

# Generated at 2022-06-13 01:22:50.104964
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Example data:
    # media: autoselect nonegotiate status: inactive
    # media: <unknown type> none none
    # media: <unknown type> none <unknown type>
    # media: 1000baseTX <full-duplex> none
    # media: 1000baseTX <full-duplex> <flow-control>
    words = ['media:', '1000baseTX', '<full-duplex>', '<flow-control>']
    current_if = dict()
    ips = dict()
    DarwinNetwork().parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == '1000baseTX'
    assert current_if['media_type'] == 'full-duplex'
    assert current_if['media_options'] == 'flow-control'

# Generated at 2022-06-13 01:22:54.139964
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = {}
    test_words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    DarwinNetwork.parse_media_line(test_words, iface, None)
    assert iface['media'] == 'Unknown'
    assert iface['media_select'] == 'Unknown'
    assert iface['media_type'] == 'unknown type'
    assert iface['media_options'] is None

# Generated at 2022-06-13 01:22:58.063563
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()

    # test for media_line with unknown type
    media_line = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    current_if = {'media': 'Unknown'}
    darwin_net.parse_media_line(media_line, current_if, None)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] is None

# Generated at 2022-06-13 01:23:02.724587
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_instance = DarwinNetwork()
    words = ['<unknown', 'type>']
    current_if = {}
    ips = []
    test_instance.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    words = ['auto']
    current_if = {}
    ips = []
    test_instance.parse_media_line(words, current_if, ips)
    assert current_if == {}


# Generated at 2022-06-13 01:23:11.214253
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test parsing of media line with no options
    words = ['media:', 'autoselect', '100baseTX', '(100baseTX)']
    current_if = {}
    ips = []
    DarwinNetwork().parse_media_line(words, current_if, ips)
    true_if = {'media': 'Unknown',
               'media_select': 'autoselect',
               'media_type': '100baseTX',
               'media_options': '(100baseTX)'}
    assert current_if == true_if

    # Test parsing of media line with options
    words = ['media:', 'autoselect', '100baseTX', '(100baseTX,media_opt=val)']
    current_if = {}
    ips = []

# Generated at 2022-06-13 01:23:18.705982
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    drwn = DarwinNetwork()
    test_data = [
        (['', 'autoselect', '<host>,', 'ieee80211', 'channel', '8'], {'media_select': 'autoselect', 'media_type': 'host'}, {'ieee80211': 'channel 8'}),
        (['', 'autoselect', 'unknown', 'type>'], {'media_select': 'autoselect', 'media_type': 'unknown type'}, {}),
    ]
    for words, media_out, media_options_out in test_data:
        current_if = {}
        ips = {}
        drwn.parse_media_line(words, current_if, ips)
        assert media_out == current_if['media_select']

# Generated at 2022-06-13 01:23:26.858194
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    ifc.parse_media_line(['media:', 'media_select', 'media_type', 'media_options_1', 'media_options_2'],
                         {'current_if': {}}, None)
    assert ifc.interface['current_if']['media'] == 'Unknown'
    assert ifc.interface['current_if']['media_select'] == 'media_select'
    assert ifc.interface['current_if']['media_type'] == 'media_type'
    assert ifc.interface['current_if']['media_options']['media_options_1'] == ''
    assert ifc.interface['current_if']['media_options']['media_options_2'] == ''

# Generated at 2022-06-13 01:23:33.930145
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    cif = DarwinNetwork()
    line = "media: autoselect (100baseTX <full-duplex>)"
    initial_if = {}
    ips = {}
    cif.parse_media_line(line.split(), initial_if, ips)
    assert initial_if['media_select'] == "autoselect"
    assert initial_if['media_type'] == "100baseTX"
    assert initial_if['media_options'] == "full-duplex"
    initial_if = {}
    ips = {}
    line = "media: <unknown type>"
    cif.parse_media_line(line.split(), initial_if, ips)
    assert initial_if['media_select'] == "Unknown"
    assert initial_if['media_type'] == "unknown type"

# Generated at 2022-06-13 01:23:39.486818
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_lines = """
media: autoselect (none) status: inactive
media: autoselect (1000baseT <full-duplex>) status: inactive
media: autoselect (1000baseT <full-duplex>) status: active
media: <unknown type> (none) status: inactive
media: <unknown type> (none) status: active
"""

    if_info = {'name': 'en0',
               'macaddr': '00:00:00:00:00:00',
               'module': '',
               'mtu': '1500',
               'state': '',
               'type': 'Ethernet',
               'ipv4': [],
               'ipv6': []}

# Generated at 2022-06-13 01:23:45.065069
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    words = ['media:','<unknown','type>','full-duplex','options=none<CSMA/CD>','status:','active']
    obj = DarwinNetwork()
    obj.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == 'full-duplex'

# Generated at 2022-06-13 01:24:09.557960
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:24:13.096803
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    words = ['media:', '<unknown', 'type>']
    current_if = {}
    ips = {}
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:24:23.107749
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()

# Generated at 2022-06-13 01:24:32.005817
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_input_data = [["media:", "autoselect", "<unknown type>"],
                       ["media:", "autoselect", "10baseT/UTP"],
                       ["media:", "autoselect", "10baseT/UTP", "(none)"]]
    test_expected_dict = {"media": "Unknown",
                          "media_select": "autoselect",
                          "media_type": "unknown type",
                          "media_options": {}}
    test_DarwinNetwork = DarwinNetwork()
    for test_input in test_input_data:
        test_DarwinNetwork.parse_media_line(test_input, test_expected_dict, None)

# Generated at 2022-06-13 01:24:41.256111
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test of the generic case
    test_obj = DarwinNetwork()
    words = ['media:', 'none']
    current_if = {'media': '', 'media_type': '', 'media_select': '', 'media_options': ''}
    ips = {'inet': {}, 'inet6': {}}
    test_obj.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'none'
    assert current_if['media_type'] == ''
    assert current_if['media_options'] == ''
    # Test of the 'bridge' media type
    test_obj = DarwinNetwork()
    words = ['media:', '<unknown', 'type>']

# Generated at 2022-06-13 01:24:48.694200
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    testObj = DarwinNetwork()
    testIf = dict()
    testWords = ['media:', 'autoselect', '<unknown', 'type>']
    testObj.parse_media_line(testWords, testIf, dict())
    assert testIf['media'] == 'Unknown'
    assert testIf['media_select'] == 'autoselect'
    assert testIf['media_type'] == 'unknown type'
    assert testIf['media_options'] == dict()

    testIf = dict()
    testWords = ['media:', 'autoselect', '10baseT/UTP', '<full-duplex>']
    testObj.parse_media_line(testWords, testIf, dict())
    assert testIf['media'] == 'Unknown'
    assert testIf['media_select'] == 'autoselect'
    assert test

# Generated at 2022-06-13 01:24:54.955342
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test_if config with media line
    test_if = {'name': 'en0', 'ipv4': [], 'ipv6': [], 'type': 'ether'}
    line = '  media: <unknown type> autoselect status: inactive'
    words = line.split()
    DarwinNetwork().parse_media_line(words, test_if, {})
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == 'unknown type'
    assert test_if['media_options'] == {}

    # test_if config without media line
    test_if = {'name': 'en0', 'ipv4': [], 'ipv6': [], 'type': 'ether'}

# Generated at 2022-06-13 01:25:03.196780
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    # test for condition not mentioned in code for both cases
    assert dn.parse_media_line(['status:', 'inactive'], {}, '') == {'media': 'Unknown', 'media_select': 'inactive'}
    assert dn.parse_media_line(['status:', 'active', 'media', 'media_type'], {}, '') == {'media': 'Unknown', 'media_select': 'active', 'media_type': 'media_type'}
    # test for elif and elif:else
    assert dn.parse_media_line(['status:', 'active', '<unknown', 'type>'], {}, '') == {'media': 'Unknown', 'media_select': 'active', 'media_type': 'unknown type'}
    assert dn.parse

# Generated at 2022-06-13 01:25:09.857708
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # valid media line example, see man page for ifconfig
    words_valid = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    current_if_valid = {}
    media_type_valid = 'none'
    media_select_valid = 'autoselect'
    ips_valid = {}

    # invalid media line example, see man page for ifconfig
    words_invalid = ['media:', 'Unknown']
    current_if_invalid = {}
    media_type_invalid = 'Unknown'
    media_select_invalid = 'Unknown'
    ips_invalid = {}

    # testing parse_media_line method with valid input
    DarwinNetwork.parse_media_line(DarwinNetwork(), words_valid, current_if_valid, ips_valid)
    assert current

# Generated at 2022-06-13 01:25:17.733001
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()

    words = ['media:', 'autoselect', '(1000baseT <full-duplex>)', 'status:', 'active']
    line = ' '.join(words)
    current_if = {}
    ips = {}
    network.parse_media_line(line, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '1000baseT <full-duplex>'
    assert current_if['media_options'] == {'full-duplex': None}

    words = ['media:', '<unknown', 'type>', 'status:', 'active']
    line = ' '.join(words)
    current_if = {}
    ips = {}

# Generated at 2022-06-13 01:25:37.621703
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    DarwinNetwork has special handling for parsing the media line.
    """

    # In this test, the parse_media_line is modified to stricly return
    # the current_if, so we can add an assert to the test_module.
    def parse_media_line(self, words, current_if, ips):
        # not sure if this is useful - we also drop information
        current_if['media'] = 'Unknown'  # Mac does not give us this
        current_if['media_select'] = words[1]
        if len(words) > 2:
            # MacOSX sets the media to '<unknown type>' for bridge interface
            # and parsing splits this into two words; this if/else helps
            if words[1] == '<unknown' and words[2] == 'type>':
                current_if

# Generated at 2022-06-13 01:25:41.827338
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net_parser = DarwinNetwork()

    media_line = ['media:', 'autoselect', '(none)']
    darwin_net_parser.parse_media_line(media_line, None, None)

    media_line = ['media:', 'autoselect', '(1000baseTX)']
    darwin_net_parser.parse_media_line(media_line, None, None)

    media_line = ['media:', '<unknown', 'type>']
    darwin_net_parser.parse_media_line(media_line, None, None)

# Generated at 2022-06-13 01:25:51.504106
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Test for standard (ethernet) media line
    my_network = DarwinNetwork()
    my_network.current_if = {}
    my_network.parse_media_line(['media:', 'autoselect', '10gbase-sr', '(TX)'], my_network.current_if, my_network.ips)
    my_network.parse_media_line(['media:', 'autoselect', '1000base-t', '(TX)'], my_network.current_if, my_network.ips)

    assert my_network.current_if['media'] == 'Unknown'
    assert my_network.current_if['media_select'] == 'autoselect'
    assert my_network.current_if['media_type'] == '1000base-t'

# Generated at 2022-06-13 01:25:59.534136
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    test_data = [
        {'words': ['media:', '<unknown', 'type>'],
         'want': {'media': 'Unknown',
                  'media_select': 'Unknown',
                  'media_type': 'unknown type'}},
        {'words': ['media:', 'autoselect', '(none)'],
         'want': {'media': 'Unknown',
                  'media_select': 'autoselect',
                  'media_type': '(none)'}},
    ]
    for td in test_data:
        dn.parse_media_line(td['words'], dict(), dict())
        got = dn.interfaces['lo0']
        assert got == td['want']

# Generated at 2022-06-13 01:26:05.637096
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from test.units.facts.network.base_bsd import TestGenericBsdIfconfigNetwork
    # This object must be a subclass of GenericBsdIfconfigNetwork
    test_object = TestGenericBsdIfconfigNetwork(DarwinNetwork)

    test_object._current_if = {'media': 'unknown',
                               'media_select': 'test1',
                               'media_type': 'test2',
                               'media_options': 'test3'}

    # First test with words 'foo bar'
    test_object.words = ['foo', 'bar']
    test_object.parse_media_line()
    assert test_object._current_if['media'] == 'Unknown'
    assert test_object._current_if['media_select'] == 'foo'

    # Second test with words 'foo bar foobar'
    test

# Generated at 2022-06-13 01:26:09.713658
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network_instance = DarwinNetwork()
    expected_result = ('autoselect', 'ieee80211', {'mode' : '11a'})
    actual_result = network_instance.parse_media_line(['media:', 'autoselect', 'ieee80211', 'mode', '11a'], {}, {})
    assert expected_result == actual_result

# Generated at 2022-06-13 01:26:15.811424
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = DarwinNetwork()
    test.set_current_if({'configured': True, 'name': 'lo0', 'macaddress': 'N/A', 'type': 'Unknown', 'type': 'Unknown', 'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'Unknown', 'media_options': 'Unknown', 'state': 'up', 'inet': []})
    words = ['media:', '<unknown', 'type>', 'status:', 'active']
    test.parse_media_line(words, test.get_current_if(), test.get_if_index_ip_address())
    assert test.get_current_if()['media'] == 'Unknown'
    assert test.get_current_if()['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:26:21.735087
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_net = DarwinNetwork()
    current_if = {'name': 'test_if'}
    # no media line
    assert not darwin_net.parse_media_line(['any_string'], current_if, {})
    assert 'media' not in current_if

    # mac media line containing '<unknown type>'
    assert darwin_net.parse_media_line(['media:', '<unknown', 'type>'], current_if, {})
    assert 'media' in current_if
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    # mac media line without options

# Generated at 2022-06-13 01:26:27.533362
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dd = DarwinNetwork()
    assert dd._platform == 'Darwin'

# Generated at 2022-06-13 01:26:32.469004
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    eth_if = {'name': 'eth0',
              'flags': ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']}
    ifconfig_output = ['media: <unknown type> ']
    ifconfig_output.append('status: no carrier')
    darwin_network = DarwinNetwork()
    darwin_network.parse_media_line(ifconfig_output[0].split(), eth_if, {})
    assert eth_if['media'] == 'Unknown'
    assert eth_if['media_select'] == '<unknown'
    assert eth_if['media_type'] == 'unknown type'
    assert eth_if['media_options'] == {}