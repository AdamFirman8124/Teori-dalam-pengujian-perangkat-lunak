

# Generated at 2022-06-13 01:16:42.302589
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    DarwinNetwork.parse_media_line(None, 'en1 autoselect (none) status: inactive'.split(), None)

# Generated at 2022-06-13 01:16:46.530600
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'ifname': 'en0', 'name': 'en0', 'macaddress': '10:93:e9:11:02:56', 'module': 'ether', 'slaves': []}
    words = 'media: autoselect <unknown type> status: inactive'.split(" ")
    DarwinNetwork.parse_media_line(None, words, current_if, None)

# Generated at 2022-06-13 01:16:56.147476
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    '''
    Create a DarwinNetwork object and call parse_media_line
    '''

    # Create a DarwinNetwork object
    dn = DarwinNetwork()

    # init
    current_if = {}
    ips = {}

    #-----------------------------------------------------------------------
    # Test if we get right media_select, media_type and media_options
    #-----------------------------------------------------------------------
    words = ['media', 'autoselect', '(none)']
    dn.parse_media_line(words, current_if, ips)

    # Test if media_select is right
    assert current_if['media_select'] == "autoselect", 'DarwinNetwork parse_media_line failed: media_select is wrong'

    # Test if media_type is right

# Generated at 2022-06-13 01:17:06.016703
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
  """ Testing DarwinNetwork instantiation:
  """
  class FactCollector:
      def __init__(self):
          self.result = {}
          self.result['bootfile'] = 'bootfile.txt'
          self.result['domain'] = 'abc.com'
          self.result['fqdn'] = 'test.abc.com'
          self.result['hostname'] = 'test'
          self.result['nodename'] = 'test.local'
          self.result['os_family'] = 'Darwin'
          self.result['interpreter'] = '/usr/bin/python'
          self.result['system'] = 'Darwin'
          self.result['virtualization_role'] = 'guest'
          self.result['virtualization_type'] = 'virtualbox'
          self.result['architecture']

# Generated at 2022-06-13 01:17:12.637638
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    dn = DarwinNetwork()
    assert dn.default_if == 'lo0'
    assert dn.media_re[0] == 'media:'
    assert dn.media_re[1] == '<UNKNOWN>'
    assert dn.media_re[2] == '<none>'
    assert dn.media_re[3] == '\d+baseT'
    assert dn.media_re[4] == '\d+baseTx'
    assert dn.media_re[5] == '\d+baseT-(fd|hd)'
    assert dn.media_re[6] == '\d+baseTX-(fd|hd)'
    assert dn.media_re[7] == 'auto'

# Generated at 2022-06-13 01:17:23.423053
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    assert d.parse_media_line([], {}, []) == {}
    d.parse_media_line(['media:','autoselect','1000baseT','full-duplex'], {}, [])
    assert d.parse_media_line(['media:','autoselect','1000baseT','full-duplex'], {}, []).get('media_select') == 'autoselect'
    assert d.parse_media_line(['media:','autoselect','1000baseT','full-duplex'], {}, []).get('media_type') == '1000baseT'
    assert d.parse_media_line(['media:','autoselect','1000baseT','full-duplex'], {}, []).get('media_options') == 'full-duplex'
    assert d.parse_

# Generated at 2022-06-13 01:17:34.495736
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Create instance of DarwinNetwork class
    obj = DarwinNetwork()

    # Create instance of dummy interface
    dum = {}

    # Test media line with valid words
    words = ['media:', 'autoselect', '(100baseTX)', 'mediaopt', 'mediaopt', 'full-duplex']
    obj.parse_media_line(words, dum, None)
    assert dum['media'] == 'Unknown'
    assert dum['media_select'] == 'autoselect'
    assert dum['media_type'] == '100baseTX'
    assert dum['media_options'] == 'mediaopt mediaopt full-duplex'

    # Test media line with valid words
    words = ['media:', 'autoselect', '(100baseTX)', 'full-duplex']

# Generated at 2022-06-13 01:17:42.045290
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Arrange
    test_object = DarwinNetwork()
    test_object._parse_media_line = DarwinNetwork.parse_media_line
    test_object.facts = dict()
    test_object.current_if = dict()
    test_object.ips = dict()

    # Act
    test_object._parse_media_line(['media:','IEEE','802.11','D11'], test_object.current_if, test_object.ips)
    test_object._parse_media_line(['media:','<unknown','type>'], test_object.current_if, test_object.ips)

    # Assert
    assert 'IEEE' == test_object.current_if['media_select']
    assert '802.11' == test_object.current_if['media_type']

# Generated at 2022-06-13 01:17:54.022749
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = 'media: autoselect (<unknown type>)'
    ft = NetworkCollector.fact_class.generate_instance({})
    line_words = line.split()
    current_if = {'inet': '127.0.0.1', 'netmask': '255.0.0.0',
                  'broadcast': '127.255.255.255', 'inet6': '::1', 'hwaddr': '12:34:56:78:90:12'}
    ft.parse_media_line(line_words, current_if, "")
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'Unknown'
    assert current_if['media_options'] == ""

# Generated at 2022-06-13 01:18:02.836704
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # setup
    darwin_net_test = DarwinNetwork({})
    darwin_net_test.current_if = {'media': 'Unknown', 'media_select': '', 'media_type': '', 'media_options': []}

    # test positive
    lines = (
        ('fiber', '100baseTX', 'full-duplex'),
        ('fiber', '100baseTX'),
        ('fiber', 'full-duplex'),
        ('fiber', 'full-duplex', '1000baseSX'),
        ('fiber', 'full-duplex', '100baseTX'),
        ('1000baseSX', 'full-duplex', '100baseTX'),
    )

# Generated at 2022-06-13 01:18:07.761249
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    class_under_test = DarwinNetwork()

    assert class_under_test.fact_class == DarwinNetwork
    assert class_under_test.platform == 'Darwin'



# Generated at 2022-06-13 01:18:09.355294
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    darwin_network = DarwinNetwork()
    assert darwin_network is not None


# Generated at 2022-06-13 01:18:17.447684
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create object
    dnx = DarwinNetwork({})

    # test known good input
    media_line = "media: autoselect (<unknown type>) status: active"
    words = media_line.split()
    ip = {}
    dnx.parse_media_line(words, ip, {})
    assert ip == {'media': 'Unknown', 'media_type': 'unknown type', 'media_select': 'autoselect', 'media_options': None}

    # test known good input 2
    media_line = "media: autoselect (100baseTX <half-duplex,flow-control>) status: active"
    words = media_line.split()
    ip = {}
    dnx.parse_media_line(words, ip, {})

# Generated at 2022-06-13 01:18:21.041653
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    """ test the constructor of FreeBSDNetwork class
    """
    obj = DarwinNetwork()
    assert obj._platform == 'Darwin'
    assert obj.get_option_value("10Gfull") == '10Gfull'

# Generated at 2022-06-13 01:18:25.618166
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    # Initialize the class
    darwin_network = DarwinNetwork()

    # Teardown this class
    try:
        darwin_network_teardown = darwin_network
        darwin_network_teardown.teardown()
    except _platform as e:
        pass

# Generated at 2022-06-13 01:18:37.493465
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Example ifconfig output from MacOSX
    test_data = [
        ["\tmedia: <unknown type>"],
        ["\tmedia: 10baseT/UTP <full-duplex>"],
        ["\tmedia: 10baseT/UTP <full-duplex> <flow-control-tx>"]
    ]
    d = DarwinNetwork()
    for line in test_data:
        result = d.parse_media_line(line)
        print(result)
        assert result['media_select'] == 'Unknown'
        assert result['media_type'] == 'unknown type'
        assert not result['media_options']

    result = d.parse_media_line(test_data[1])
    print(result)
    assert result['media_type'] == "full-duplex"

# Generated at 2022-06-13 01:18:43.113815
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    sample_line = "media: <unknown type> (<unknown>) status: inactive"
    d_net = DarwinNetwork()
    current_if = {'ipv4': [], 'ipv6': []}
    ips = []
    d_net.parse_media_line(sample_line.split(), current_if, ips)
    # Check returns
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media' not in current_if
    assert 'media_options' not in current_if

# Generated at 2022-06-13 01:18:51.670402
# Unit test for constructor of class DarwinNetwork
def test_DarwinNetwork():
    d = DarwinNetwork()
    # TODO: Replace assertTrue with assertRaises and assertEqual
    assert(d is not None)
    d.add_entry("candy", [1, 2, 3])
    d.add_entry("pop", [1, 2, 3])
    assert(d.interfaces == {'candy': {'candy': [1, 2, 3]}, 'pop': {'pop': [1, 2, 3]}})
    assert(d.interfaces_list == ['candy', 'pop'])
    assert(d.has_value("candy", "candy") is True)

# Generated at 2022-06-13 01:18:59.604892
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = {'media': 'Unknown'}
    words = ['media:', 'autoselect', '<unknown type>']
    DarwinNetwork._parse_media_line(iface, words)
    assert iface['media_select'] == 'autoselect'
    assert iface['media_type'] == 'unknown type'
    assert iface['media_options'] == ''

    iface = {'media': 'Unknown'}
    words = ['media:', 'autoselect', 'none']
    DarwinNetwork._parse_media_line(iface, words)
    assert iface['media_select'] == 'autoselect'
    assert iface['media_type'] == 'none'
    assert iface['media_options'] == ''

# Generated at 2022-06-13 01:19:09.845435
# Unit test for constructor of class DarwinNetwork

# Generated at 2022-06-13 01:19:20.145095
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dif = DarwinNetwork({})
    iface = {}
    words = ['media:', '<unknown', 'type>']
    dif._parse_media_line(words, iface, '')
    assert iface['media_select'] == 'Unknown'
    assert iface['media_type'] == 'unknown type'
    assert iface['media_options'] == 'none'
    assert iface['media'] == 'Unknown'
    iface = {}
    words = ['media:', 'auto', '<unknown', 'type>', 'none']
    dif._parse_media_line(words, iface, '')
    assert iface['media_select'] == 'auto'
    assert iface['media_type'] == 'unknown type'
    assert iface['media_options'] == 'none'

# Generated at 2022-06-13 01:19:24.201818
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Testing with one media line from real data
    # media: autoselect (<unknown type>)
    words = ['media:', 'autoselect', '(<unknown', 'type>)']
    mac_current_if = {'media': 'Unknown', 'media_select': 'autoselect'}
    mac_current_if = DarwinNetwork.parse_media_line(self=None,words=words, current_if=mac_current_if, ips=None)
    assert mac_current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:19:33.534798
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()

    words = ['media:', 'autoselect', '(none)']
    current_if = {}
    ips = {}
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': 'none'}

    words = ['media:', '<unknown', 'type>']
    current_if = {}
    ips = {}
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'}

# Generated at 2022-06-13 01:19:40.863123
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    # prepare a test input
    words = ['<unknown', 'type>']
    current_if = {}
    ips = []
    # invoke the method to test
    network.parse_media_line(words, current_if, ips)
    # check the updated current_if
    if 'media' not in current_if:
        raise Exception ("'media' not in current_if")
    if current_if['media'] != 'Unknown':
        raise Exception ("current_if['media'] is not 'Unknown'")
    if 'media_select' not in current_if:
        raise Exception ("'media_select' not in current_if")
    if current_if['media_select'] != 'Unknown':
        raise Exception ("current_if['media_select'] is not 'Unknown'")

# Generated at 2022-06-13 01:19:48.546077
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create a DarwinNetwork class instance
    darwin_network = DarwinNetwork()
    # some valid test data
    words = [
        "media:",
        "<unknown type>",
        "status:",
        "inactive"
    ]

    # call the method
    current_if = darwin_network.parse_media_line(words, {}, [])
    # check the result
    assert current_if == {
                        'media': 'Unknown',
                        'media_select': 'Unknown',
                        'media_type': 'unknown type',
                        'media_options': ''
                      }

# Generated at 2022-06-13 01:19:56.762914
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Setup test case
    test_case = DarwinNetwork()
    test_case.current_if = dict()
    test_case.ips = dict()
    # Case where words[1] == '<unknown' and words[2] == 'type>'
    _words = ['media', '<unknown', 'type>']
    _current_if = dict()
    _ips = dict()
    _expected = dict()
    _expected['media'] = 'Unknown'
    _expected['media_select'] = 'Unknown'
    _expected['media_type'] = 'unknown type'
    # Execute method being tested
    test_case.parse_media_line(_words, _current_if, _ips)
    # Assert the results
    assert test_case.current_if == _expected

# Generated at 2022-06-13 01:20:03.976513
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ''' This function test method parse_media_line of class DarwinNetwork '''
    darwin_network = DarwinNetwork()
    current_if = {}
    ips = {}
    media = "media: autoselect (1000baseT <full-duplex>)"
    words = media.split()
    darwin_network.parse_media_line(words, current_if, ips)
    assert 'media' in current_if
    assert 'media_select' in current_if
    assert 'media_type' in current_if


# Generated at 2022-06-13 01:20:11.267778
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'name': 'en0', 'type': 'ether'}
    test_words = ['media:', 'autoselect', '(1000baseT)', 'status:', 'active', 'media_select:', 'autoselect']
    test_result = DarwinNetwork.parse_media_line(current_if, test_words)
    assert test_result['media'] == 'Unknown'
    assert test_result['media_select'] == 'autoselect'
    assert test_result['media_type'] == '1000baseT'
    assert test_result['media_options'] == ''

# Generated at 2022-06-13 01:20:20.777609
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network_obj = DarwinNetwork()
    darwin_network_obj.parse_media_line(["media:", "none", "status:", "inactive"], {}, None)
    assert darwin_network_obj._current_if['media'] == 'Unknown'
    assert darwin_network_obj._current_if['media_select'] == 'none'

    darwin_network_obj.parse_media_line(["media:", "autoselect", "(none)", "status:", "inactive"], {}, None)
    assert darwin_network_obj._current_if['media'] == 'Unknown'
    assert darwin_network_obj._current_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:20:28.093071
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dm = DarwinNetwork()
    assert dm.parse_media_line(
        ['media:','autoselect','<unknown type>'],
        {}, {}) == 'Unknown'
    assert dm.parse_media_line(
        ['media:', 'autoselect', '10baseT/UTP', '<full-duplex>'],
        {}, {}) == '10baseT/UTP <full-duplex>'

# Generated at 2022-06-13 01:20:41.871224
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    facts = DarwinNetwork()
    words = ['media:', '<unknown', 'type>']
    current_if = {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'}
    curr_if = facts.parse_media_line(words, current_if, ips)
    assert curr_if == current_if

# Generated at 2022-06-13 01:20:46.693288
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {'media': 'Unknown', 'media_select': 'ieee80211',
               'media_type': 'autoselect', 'media_options': {'mode': 'autoselect'}}
    dn = DarwinNetwork()
    result = dn.parse_media_line(['media:', 'ieee80211', 'autoselect', '(mode', 'autoselect)'], {}, {})

    assert test_if == result

# Generated at 2022-06-13 01:20:53.036371
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    mn = DarwinNetwork({}, {}, {})
    d = dict()
    mn.parse_media_line(['media', 'selector', '<value>'], d, {})
    assert d['media'] == 'Unknown'
    assert d['media_select'] == 'selector'
    assert d['media_type'] == 'value'
    assert d['media_options'] == None

# Generated at 2022-06-13 01:21:02.779224
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    dn = DarwinNetwork()

    # media line with all possible parameters
    words = ['media', 'auto', '<full-duplex>', 'status:', 'active', 'supported:', '1Gb,', '2Gb,', '10Gb,', 'auto,', 'none']
    dn.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'auto'
    assert current_if['media_type'] == 'full-duplex'
    assert current_if['media_options'] == ['status: active', 'supported: 1Gb, 2Gb, 10Gb, auto, none']

    # media line without options
    current_if = {}

# Generated at 2022-06-13 01:21:09.865430
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    words = ["media:", "autoselect", "(100baseTX)"]
    ips = {}
    dnetwork = DarwinNetwork()
    dnetwork.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '100baseTX',
                          'media_options': {}}
    words2 = ["media:", "<unknown", "type>", "<full-duplex>"]
    dnetwork.parse_media_line(words2, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type',
                          'media_options': {'full-duplex': ''}}


# Unit

# Generated at 2022-06-13 01:21:17.847832
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    DarwinNetwork = DarwinNetwork()
    string = 'media: autoselect (1000baseT <full-duplex>)'
    words = string.split(' ')
    current_if = {'name': 'eth0', 'device': 'eth0'}
    ips = {}
    DarwinNetwork.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '1000baseT'
    assert current_if['media_options'] == 'full-duplex'



# Generated at 2022-06-13 01:21:25.449518
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    parsed = DarwinNetwork().parse_media_line(['media:', 'autoselect', '(none)'], {}, {})
    assert parsed == {'media': 'Unknown', 'media_select': 'autoselect'}

    parsed = DarwinNetwork().parse_media_line(['media:', 'autoselect', '(none)', 'status:', 'active'], {}, {})
    assert parsed == {'media': 'Unknown', 'media_select': 'autoselect'}

    parsed = DarwinNetwork().parse_media_line(['media:', '<unknown', 'type>', 'status:', 'active'], {}, {})
    assert parsed == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'}

# Generated at 2022-06-13 01:21:32.325302
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test parse_media_line when media = 'Unknown'
    dn = DarwinNetwork()
    media_words = ['media:', 'autoselect', '(none)']
    current_if = {}
    ips = []
    dn.parse_media_line(media_words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == []

    # test parse_media_line when media is set
    current_if = {}
    ips = []
    media_words = ['media:', 'autoselect', '10baseT/UTP', '(TX)']

# Generated at 2022-06-13 01:21:40.668330
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = DarwinNetwork()
    expected = []
    expected.append({'media': 'Unknown', 'media_select': 'media:', 'media_type': 'autoselect', 'media_options': None})
    expected.append({'media': 'Unknown', 'media_select': 'media:', 'media_type': 'autoselect', 'media_options': None})
    expected.append({'media': 'Unknown', 'media_select': 'media:', 'media_type': 'autoselect', 'media_options': None})
    expected.append({'media': 'Unknown', 'media_select': 'media:', 'media_type': 'autoselect', 'media_options': None})

# Generated at 2022-06-13 01:21:48.358677
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test with a '<unknown type>' line
    testline = 'media: <unknown type>'
    words = testline.split()
    current_if = {}
    ips = {}
    test_DarwinNetwork = DarwinNetwork()
    test_DarwinNetwork.parse_media_line(words, current_if, ips)
    assert 'media' not in current_if
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in current_if

    # Test with a 'auto' line
    testline = 'media: autoselect (none)'
    words = testline.split()
    current_if = {}
    ips = {}
    test_DarwinNetwork = DarwinNetwork()
    test_Darwin

# Generated at 2022-06-13 01:22:08.333270
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    dn = DarwinNetwork()
    current_if = {}
    ips = {}
    words = ['media', '<unknown', 'type>']
    dn.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert len(current_if['media_options'].keys()) == 0

# Generated at 2022-06-13 01:22:14.744360
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # create a test class
    testClass = DarwinNetwork()

    # create a test dictionary
    testDict = {}

    # define test input and expected output
    testInput = ['media:', 'autoselect', 'status:', 'inactive']
    expectedOutput = {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': {'status': 'inactive'}}

    # run test parse_media_line method
    output = testClass.parse_media_line(testInput,testDict)

    # print output to screen
    # print(output)

    # assert test results
    assert output == expectedOutput


# Generated at 2022-06-13 01:22:18.409923
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test of macOS darwin
    d = DarwinNetwork()
    if_details = {}
    d.parse_media_line(["media:","autoselect","10baseT/UTP"], if_details, {})
    assert if_details['media'] == 'Unknown'
    assert if_details['media_select'] == "autoselect"
    assert if_details['media_type'] == "10baseT/UTP"

# Generated at 2022-06-13 01:22:28.560663
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:22:36.516292
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_mac_media_line = 'media: autoselect status: active'
    test_bridge_media_line = 'media: <unknown type> status: active'
    words = test_mac_media_line.split()
    current_if = {'network':
                      {'interfaces':
                           {'en7': {'ipv4': {'address': '192.168.1.1'}}}}
                  }
    ips = []
    if_class = DarwinNetwork(current_if, ips)
    if_class.parse_media_line(words, current_if, ips)
    # test media_select, media_type and media_options are added in
    assert 'media_select' in current_if
    assert 'media_type' in current_if
    assert 'media_options' in current_

# Generated at 2022-06-13 01:22:44.059436
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dl = DarwinNetwork()
    current_if = {}
    words = ['media', 'autoselect', '\"status:', 'active\"', '(not', 'in', 'use)']
    ips = {}
    dl.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'status:'
    assert current_if['media_options'] == {'active': None, 'not': None, 'in': None, 'use': None}

# Generated at 2022-06-13 01:22:48.612264
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    expected = {'media_type': '100baseTX', 'media_select': '1000baseT', 'media': 'Unknown', 'media_options': {}}
    dn.parse_media_line(["media:", "1000baseT", "<full-duplex>", "media", "100baseTX", "<full-duplex>"], {}, {})
    actual = dn._current_if
    assert actual == expected

# Generated at 2022-06-13 01:22:55.166792
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = {}
    w = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    DarwinNetwork.parse_media_line(DarwinNetwork(), w, iface, None)
    assert iface['media'] == 'Unknown'
    assert iface['media_select'] == 'autoselect'
    assert iface['media_type'] == '(none)'

    iface = {}
    w = ['media:', '<unknown', 'type>', '(none)', 'status:', 'inactive']
    DarwinNetwork.parse_media_line(DarwinNetwork(), w, iface, None)
    assert iface['media'] == 'Unknown'
    assert iface['media_select'] == 'Unknown'
    assert iface['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:22:58.193189
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    _current_if = {}
    _words = ['media:', '<unknown', 'type>']
    _ips = {}
    ex = DarwinNetwork('/sbin/ifconfig')
    ex.parse_media_line(_words, _current_if, _ips)
    assert(_current_if == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'})

# Generated at 2022-06-13 01:23:04.778940
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """Unit test for method parse_media_line of class DarwinNetwork"""

    # Initialize a DarwinNetwork object
    darwin_network = DarwinNetwork()

    # Define the test case array