

# Generated at 2022-06-13 01:16:47.264043
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = dict()
    words = ['en0:', '<unknown', 'type>', 'status:', 'active']
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, dict())
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == dict()
    print('Test passed')

if __name__ == '__main__':
    test_DarwinNetwork_parse_media_line()

# Generated at 2022-06-13 01:16:56.838915
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network = DarwinNetwork()
    words = ['media:', 'autoselect', '(none)', 'status:', 'active']
    current_if = dict()
    current_if['options'] = dict()
    current_if['addresses'] = dict()
    ips = dict()
    network.parse_media_line(words, current_if, ips)

    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == dict()

    words = ['media:', '<unknown', 'type>', 'status:', 'active']
    network.parse_media_line(words, current_if, ips)

    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:17:06.786231
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    input:  ['media:', 'autoselect', '(none)']
    output: ['media':'None', 'media_select':'autoselect', 'media_type':'none', 'media_options': None]
    """
    res = dict()
    d1 = DarwinNetwork()
    d1.parse_media_line(['media:', 'autoselect', '(none)'], res, None)
    assert res == {'media': 'None', 'media_select': 'autoselect', 'media_type': 'none', 'media_options': None}
    
    """
    input:  ['media:', '<unknown', 'type>']
    output: ['media':'Unknown', 'media_select':'Unknown', 'media_type':'unknown type', 'media_options': None]
    """
    res

# Generated at 2022-06-13 01:17:13.330627
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Test for DarwinNetwork method parse_media_line
    """
    # a stub for a list of words from ifconfig output
    words1 = ['media:', '<unknown', 'type>', "(e)"]

    # a stub for a dict that contains the current interface
    current_if1 = dict()
    current_if1['media'] = 'Unknown'

    # a stub for a dict that contains the IPs for an interface
    ips1 = dict()

    # Test for correct parsing of an unknown media type
    DarwinNetwork().parse_media_line(words1, current_if1, ips1)

    assert current_if1['media_select'] == 'Unknown'
    assert current_if1['media_type'] == 'unknown type'
    assert current_if1['media_options'] == ['e']

# Generated at 2022-06-13 01:17:16.434623
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    current_if['ifname'] = 'bond0.1234'
    d = DarwinNetwork()
    words = ['foo', 'bar', '<unknown', 'type>']
    ips = []
    d.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'bar'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:17:25.136434
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'name': 'en0', 'type': 'ether', 'macaddress': '5c:59:48:88:31:9a',
                  'media_select': '<unknown type>', 'media_type': 'unknown type',
                  'media_options': {}}
    DarwinNetwork.parse_media_line(['en0', '<unknown', 'type>'], current_if, [])
    assert current_if == {'name': 'en0', 'type': 'ether', 'macaddress': '5c:59:48:88:31:9a',
                          'media_select': 'Unknown', 'media_type': 'unknown type',
                          'media_options': {}}

# Generated at 2022-06-13 01:17:35.549395
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork(None, None, None)
    darwin_network.interface = 'lo0'

    current_if = {}
    words = []

    words = ['media:', '<unknown', 'type>']
    darwin_network.parse_media_line(words, current_if, None)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    words = ['media:', 'media_select', 'media_type']
    darwin_network.parse_media_line(words, current_if, None)
    assert current_if['media_select'] == 'media_select'
    assert current_if['media_type'] == 'media_type'

# Generated at 2022-06-13 01:17:42.727209
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    macos_interface1 = """\
low-power en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    inet6 fe80::3bc6:f7ff:fec6:8ed6%lo0 prefixlen 64 secured scopeid 0x6 
    inet 127.0.0.1 netmask 0xff000000 
    inet6 ::1 prefixlen 128 
    inet6 2601:1c1:8000:1911:f0:e7ff:fe22:cad7 prefixlen 64 auto_link 
    nd6 options=201<PERFORMNUD,DAD> 
    media: autoselect
    status: active"""

# Generated at 2022-06-13 01:17:54.822291
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = DarwinNetwork({})
    test.current_if = {'name': 'en0'}
    test.ips = {}
    test.parse_media_line(['media:', 'none', '(none)'], test.current_if,
                          test.ips)
    assert test.current_if['media'] == 'Unknown'
    assert test.current_if['media_select'] == 'none'
    assert test.current_if['media_type'] == 'none'
    assert test.current_if['media_options'] == []
    test.parse_media_line(
        ['media:', 'autoselect', '<unknown', 'type>', 'status:', 'inactive'],
        test.current_if, test.ips)
    assert test.current_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:18:03.808043
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    c = DarwinNetworkCollector(None)
    assert c.parse_media_line(['media:', '<unknown', 'type>', '(none)'], {}, {}) == \
        {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type', 'media_options': 'none'}
    assert c.parse_media_line(['media:', 'autoselect', '(none)'], {}, {}) == \
        {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': 'none'}