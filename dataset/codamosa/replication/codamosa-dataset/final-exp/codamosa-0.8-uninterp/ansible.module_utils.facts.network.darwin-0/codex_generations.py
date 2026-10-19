

# Generated at 2022-06-13 01:16:49.917298
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    ifc.parse_media_line(['foo0:', '<unknown', 'type>', 'status:', 'active'],
                         {'device': 'foo0'},
                         [])
    ifc.parse_media_line(['foo0:', 'media:', 'auto', 'status:', 'active'],
                         {'device': 'foo0'},
                         [])
    ifc.parse_media_line(['foo0:', 'media:', 'auto', '(autoselect)', 'status:', 'active'],
                         {'device': 'foo0'},
                         [])

# Generated at 2022-06-13 01:16:58.634235
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'name':'en0'}
    ifnet = DarwinNetwork()
    words = ['inet6', 'fe80:0000:0000:0000:4a4d:4147:4152:4f4e%en0', 'prefixlen', '64', 'scopeid', '0x5']
    ifnet.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'inet6'
    assert current_if['media_type'] == 'fe80:0000:0000:0000:4a4d:4147:4152:4f4e%en0'
    assert current_if['media_options'] == 'prefixlen 64 scopeid 0x5'
    # now with other words

# Generated at 2022-06-13 01:17:05.879862
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ["media:", "<unknown", "type>", "options:", "[", "none]"]
    current_if = {}
    ips = None
    dn = DarwinNetwork(None)
    dn.parse_media_line(words, current_if, ips)
    assert current_if["media"] == "Unknown"
    assert current_if["media_select"] == "Unknown"
    assert current_if["media_type"] == "unknown type"
    assert current_if["media_options"] == {"none": ""}

# Generated at 2022-06-13 01:17:12.494680
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    DarwinNetwork = __import__('ansible.module_utils.facts.network.darwin.DarwinNetwork', fromlist=['DarwinNetwork'])
    network = DarwinNetwork()
    words = ['media', 'autoselect(1000baseT)', 'status:', 'inactive', '(']
    current_if = {}
    ips = {}
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_type'] == '1000baseT'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_options'] == {}
    words = ['media', '1000baseT', '(autoselect)']
    network.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:17:23.353052
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    '''
    test for parse_media_line class method
    '''
    # test for correct output from this method
    dummy_words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    dummy_current_if = {
        'media': 'Unknown',
        'media_select': 'autoselect',
        'media_options': '(none)',
        'media_type': 'none',
    }
    dummy_ips = None
    darwin_network = DarwinNetwork()
    result = darwin_network.parse_media_line(dummy_words, dummy_current_if,
                                             dummy_ips)

# Generated at 2022-06-13 01:17:27.262083
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = DarwinNetwork()
    iface.parse_media_line(['media:', '<unknown', 'type>'], {}, [])
    assert iface.current_if['media_select'] == 'Unknown'
    assert iface.current_if['media_type'] == 'unknown type'
    iface.parse_media_line(['media:', 'autoselect', '(none)'], {}, [])
    assert iface.current_if['media_select'] == 'autoselect'
    assert iface.current_if['media_type'] == 'none'
    assert iface.current_if['media_options'] == {}
    iface.parse_media_line(['media:', 'autoselect', '10baseT/UTP', '(100baseTX<full-duplex>)'], {}, [])


# Generated at 2022-06-13 01:17:37.448858
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_class = DarwinNetwork(None, None)
    assert test_class.parse_media_line(['media:', 'autoselect', '(none)'], None, None) == \
        dict(media='Unknown', media_select='autoselect', media_type='none')
    assert test_class.parse_media_line(['media:', 'none', '(none)'], None, None) == \
        dict(media='Unknown', media_select='none', media_type='none')
    assert test_class.parse_media_line(['media:', '10baseT/UTP', '(none)'], None, None) == \
        dict(media='Unknown', media_select='10baseT/UTP', media_type='none')

# Generated at 2022-06-13 01:17:43.156466
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    assert dn.parse_media_line(['media:', 'autoselect', 'status:', 'inactive'], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect'}
    assert dn.parse_media_line(['media:', 'autoselect', '(', 'none', ')', 'status:', 'active'], {}, {}) == {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'none'}

# Generated at 2022-06-13 01:17:52.352970
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', '<unknown', 'type>', 'status:', 'inactive', 'supported:', 'none,', 'none']
    current_if = dict()
    ips = dict()
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == []



# Generated at 2022-06-13 01:18:00.810189
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    # Mocking the class DarwinNetwork
    DarwinNetwork = SystemDarwinNetwork()

    # Mocking the method parse_media_line of class DarwinNetwork
    def parse_media_line_mock(*args, **kwargs):
        return DarwinNetwork.parse_media_line(*args, **kwargs)

    # Calling the method parse_media_line of class DarwinNetwork
    # with different inputs
    parse_media_line_mock(['media:', 'autoselect', '(none)'], {}, {})
    parse_media_line_mock(['media:', '1000baseT'], {}, {})
    parse_media_line_mock(['media:', '1000baseT', '(none)'], {}, {})