

# Generated at 2022-06-13 01:16:50.938209
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    # a bridge, uninteresting
    dn.parse_media_line(['media:', '<unknown', 'type>', 'status:', 'inactive'], dict(), dict())
    # a picture
    dn.parse_media_line(
        ['media:', '<unknown', 'type>', 'status:', 'inactive', 'for', '10min', '30sec'], dict(), dict())
    # a picture, with media_select being one word
    dn.parse_media_line(['media:', '2', 'none', 'status:', 'inactive'], dict(), dict())
    # a regular interface
    dn.parse_media_line(['media:', 'autoselect', 'status:', 'active'], dict(), dict())
    # another one
    dn

# Generated at 2022-06-13 01:16:59.205449
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {'media': 'Unknown', 'media_select': 'none', 'media_type': 'autoselect', 'media_options': {}}
    
    # Testing for case where additional media_options are provided
    words = ['media:', 'none', '(autoselect)', 'status:', 'active', 'media_options:', 'FDX,100baseTX,100baseTX-FDX']
    collection = DarwinNetwork()
    collection.parse_media_line(words, current_if, ['10.1.1.1'])

    assert(current_if['media']) == 'Unknown'
    assert(current_if['media_select']) == 'none'
    assert(current_if['media_type']) == 'autoselect'

# Generated at 2022-06-13 01:17:03.485439
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ["media:", "<unknown", "type>", "status:", "inactive"]
    current_if = {'media': 'Unknown', 'media_select': 'Unknown'}
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, False)



# Generated at 2022-06-13 01:17:11.728995
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    words = ["media:", "autoselect", "(none)", "(none)"]
    current_if = dict()
    ips = dict()
    d.parse_media_line(words, current_if, ips)
    assert(current_if['media'] == 'Unknown')
    assert(current_if['media_select'] == 'autoselect')
    assert(current_if['media_type'] == '(none)')
    assert(current_if['media_options'] == '(none)')
    
    words = ["media:", "autoselect", "10baseT/UTP", "(none)"]
    current_if = dict()
    ips = dict()
    d.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:17:23.318322
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', 'autoselect', '(none)', '(none)']
    current_if = {}
    ips = {}
    d_obj = DarwinNetwork(None, None)
    d_obj.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Unknown', 'media_select': 'autoselect'}

    words = ['media:', 'autoselect', '100baseTX', 'full-duplex']
    current_if = {}
    ips = {}
    d_obj = DarwinNetwork(None, None)
    d_obj.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:17:29.348643
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()
    dn.parse_media_line(['media:', '<unknown', 'type>'], {}, {})
    assert dn.current_if['media'] == 'Unknown'
    assert dn.current_if['media_select'] == 'Unknown'
    assert dn.current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:17:38.413001
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
        words = ['media:', 'auto', '<unknown type>', 'mediaopt', 'mediaopt2']
        current_if = dict()
        ips = dict()
        collector = DarwinNetwork()
        collector.parse_media_line(words, current_if, ips)
        assert current_if['media'] == 'Unknown'  # Mac does not give us this
        assert current_if['media_select'] == 'auto'
        assert current_if['media_type'] == 'unknown type'
        assert current_if['media_options'] == ['mediaopt', 'mediaopt2']
        
        words = ['media:', 'auto', '1000baseT', 'mediaopt', 'mediaopt2']
        current_if = dict()
        collector.parse_media_line(words, current_if, ips)
        assert current_if

# Generated at 2022-06-13 01:17:43.156466
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin_network = DarwinNetwork()
    current_if = {}
    words = ['media:', 'auto', '<unknown', 'type>']
    darwin_network.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'auto'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:17:55.393831
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    ifc.iface = 'en0'
    words = ['media:', 'autoselect', '(100baseTX', '<full-duplex>,' '100baseTX', '<full-duplex>,' '100baseTX', '<full-duplex>,'
             '100baseTX', '<full-duplex>,' '100baseTX', '<full-duplex>,' '100baseTX', '<full-duplex>)' 'status:', 'active']
    ifc.parse_media_line(words, ifc.current, ifc.ip_interfaces)
    assert ifc.current['media'] == 'Unknown'
    assert ifc.current['media_select'] == 'autoselect'
    assert ifc.current['media_type'] == '100baseTX'

# Generated at 2022-06-13 01:18:04.348788
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test: Media line is not given
    ifc0 = DarwinNetwork()
    current_if = {}
    ifc0.parse_media_line([""], current_if, {})
    assert current_if['media'] == 'Unknown'
    # test: Media line: <unknown type>
    current_if = {}
    ifc0.parse_media_line(["media:", "<unknown", "type>"], current_if, {})
    assert current_if['media'] == 'Unknown'
    # test: Media line: autoselect status: active
    current_if = {}
    ifc0.parse_media_line(["media:", "autoselect", "(none)"], current_if, {})
    assert current_if['media'] == 'Unknown'
    # test: Media line: autoselect status: inactive


# Generated at 2022-06-13 01:18:16.108065
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """ test the parse_media_line method of DarwinNetwork.
        The unit test below tests following media lines for Darwin:
        # media: autoselect (1000baseT <full-duplex>) status: active
        # media: none status: active
        # media: <unknown type> (none) status: active
        # media: autoselect (none) status: active
        # media: autoselect status: active
    """

    # Setup a test object of class DarwinNetwork and the expected resulting dict
    test_obj = DarwinNetwork()
    expected_result = {
        'media': 'Unknown',
        'media_select': 'autoselect',
        'media_type': '1000baseT',
        'media_options': 'full-duplex'
    }

    # Test auto select full duplex

# Generated at 2022-06-13 01:18:24.016444
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dwn = DarwinNetwork()
    iface = {'media': '', 'media_type': '', 'media_select': '', 'media_options': ''}
    dwn.parse_media_line(['media:', '<unknown', 'type>'], iface, {})
    assert iface == {'media': 'Unknown', 'media_type': 'unknown type', 'media_select': 'Unknown', 'media_options': ''}

# Generated at 2022-06-13 01:18:28.806647
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    fact = DarwinNetwork()
    words = ['media:', '<unknown', 'type>', 'status:', 'active']
    current_if = {'ifname': 'bridge100', 'iftype': 'bridge'}

    fact.parse_media_line(words, current_if, {})

    assert current_if['media_type'] == 'unknown type'
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:18:39.812778
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # test media lines from Mac VM and Macbook Air
    input_words = [
        # Mac VM
        ['media:', 'autoselect', '(100baseTX <full-duplex>)'],
        # Macbook Air
        ['media:', '<unknown', 'type>'],
    ]
    output_if = {}
    for words in input_words:
        DarwinNetwork().parse_media_line(words, output_if, None)
        assert output_if['media'] == 'Unknown'
        assert output_if['media_select'] == words[1]

# Generated at 2022-06-13 01:18:45.587408
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    """
    Test the parse_media_line method of the class DarwinNetwork
    """
    dwn = DarwinNetwork()
    # Test case where media line is 'media: Ethernet autoselect'
    media_line = ['media:', 'Ethernet', 'autoselect']
    interface = {}
    dwn.parse_media_line(media_line, interface, None)
    assert interface['media'] == 'Unknown'
    assert interface['media_type'] == 'autoselect'
    assert not interface['media_options']
    # Test case where media line is 'media: autoselect <unknown type>'
    media_line = ['media:', 'autoselect', '<unknown', 'type>']
    interface = {}
    dwn.parse_media_line(media_line, interface, None)
    assert interface['media']

# Generated at 2022-06-13 01:18:53.233372
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    words = ['media:', '<unknown', 'type>']
    DarwinNetwork.parse_media_line(DarwinNetwork, words, current_if, [])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert not 'media_options' in current_if


if __name__ == '__main__':
    test_DarwinNetwork_parse_media_line()

# Generated at 2022-06-13 01:19:01.149111
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    '''
    Unit test for method parse_media_line of class DarwinNetwork
    '''
    # create test object of class DarwinNetwork
    test_obj = DarwinNetwork()
    # create test dictionary of data
    test_dict = {}
    # create test list of words
    test_list = ['media:','1000baseT','<full-duplex>','media','1000baseT','<full-duplex>','media','1000baseT','<full-duplex>']
    # run method parse_media_line
    test_obj.parse_media_line(words=test_list, current_if=test_dict)
    # test result of method parse_media_line - check media_select
    assert test_dict['media_select'] == '1000baseT'
    # test result of method parse_media_line - check media_type


# Generated at 2022-06-13 01:19:08.211857
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media_line = ['media:','autoselect','<unknown','type>']
    # current interface
    current_if = {}
    # list of all IPs
    ips = []
    # call class method
    DarwinNetwork.parse_media_line(DarwinNetwork, media_line, current_if, ips)
    # check the result
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:19:15.696120
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media_line = 'media: <unknown type>'
    words = media_line.split()
    current_if = dict()
    ips = dict()
    result = DarwinNetwork(False).parse_media_line(words, current_if, ips)
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_select'] == 'Unknown'

    media_line = 'media: autoselect (100baseTX <full-duplex>)'
    words = media_line.split()
    current_if = dict()
    ips = dict()
    result = DarwinNetwork(False).parse_media_line(words, current_if, ips)
    assert current_if['media_type'] == '100baseTX'
    assert current_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:19:22.121173
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    data = {'GigabitEthernet1': {'mtu': '1500', 'macaddress': '52:54:00:27:63:d7', 'active': True, 'speed': '1000',
                                 'type': 'Ethernet', 'addresses': {'10.78.42.157': {'address': '10.78.42.157',
                                                                                     'prefixlen': 24, 'netmask':
                                                                                     '255.255.255.0'}},
            'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '1000baseTX',
            'media_options': {'mediaopt': 'none'}}}

    collector = DarwinNetworkCollector()

# Generated at 2022-06-13 01:19:36.937069
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    col_obj = DarwinNetwork(None)
    test_dict = {}
    col_obj.parse_media_line(['media:', 'autoselect', '(none)'], test_dict, [])
    assert test_dict['media'] == 'Unknown'
    assert test_dict['media_select'] == 'autoselect'
    assert test_dict['media_type'] == '(none)'
    assert 'media_options' not in test_dict
    test_dict.clear()
    col_obj.parse_media_line(['media:', 'autoselect', '(none)', '(none)'], test_dict, [])
    assert test_dict['media'] == 'Unknown'
    assert test_dict['media_select'] == 'autoselect'
    assert test_dict['media_type'] == '(none)'
    assert test_

# Generated at 2022-06-13 01:19:46.047458
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    if_data = {}
    if_data['media'] = 'unknown'
    if_data['media_select'] = 'autoselect'
    if_data['media_type'] = 'none'
    if_data['media_options'] = 'none'

    words = ['media:', 'autoselect', 'none', 'none']
    DarwinNetwork().parse_media_line(words, if_data, {})
    assert if_data['media'] == 'Unknown'
    assert if_data['media_select'] == 'autoselect'

    words = ['media:', '<unknown', 'type>']
    DarwinNetwork().parse_media_line(words, if_data, {})
    assert if_data['media_select'] == 'Unknown'

# Generated at 2022-06-13 01:19:55.595008
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Test start
    test_object = DarwinNetwork(['lo0', 'media', 'autoselect',
                                 '(none)', 'status:', 'inactive',
                                 'lladdr', '00:00:00:00:00:00'], {})
    current_if = {'media': 'Unknown'}
    words = ['media', 'autoselect', '(none)']

    # Testing the parse_media_line function of the DarwinNetwork class
    test_object.parse_media_line(words, current_if, {})
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'none'
    assert 'media_options' not in current_if

    # One more test with media type
    test

# Generated at 2022-06-13 01:20:01.815263
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    fact_module = DarwinNetwork()
    current_if = {'device': 'en0', 'ips': []}
    fact_module.parse_media_line(['media:', 'autoselect', '<unknown type>'], current_if, [])
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == 'unknown type'
    fact_module.parse_media_line(['media:', 'autoselect', '10baseT/UTP'], current_if, [])
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '10baseT/UTP'
    fact_module.parse_media_line(['media:', '<unknown', 'type>'], current_if, [])


# Generated at 2022-06-13 01:20:11.954131
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # testing Darwin's media parse line as it is different to FreeBSD's (we do not have the media field)
    t_iface = {
        'device': 'bridge0',
        'operstate': 'down',
        'address': 'b2:5b:26:69:44:2d',
        'type': 'Bridge'
    }
    n = DarwinNetwork()
    t_line = 'media: <unknown type> autoselect status: inactive'
    n.parse_media_line(t_line.split(), t_iface, ['127.0.0.1'])
    assert t_iface['media_select'] == 'Unknown'
    assert t_iface['media_type'] == 'unknown type'
    assert not t_iface.get('media_options')

# Generated at 2022-06-13 01:20:20.951758
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    import json

    darwin_network = DarwinNetwork()
    words = ['media:', 'autoselect', '(1000baseT <full-duplex,flow-control>)', 'status:', 'active']
    i = {'options': dict(), 'addresses': dict()}

    darwin_network.parse_media_line(words, i, i['addresses'])

    print(json.dumps(i, sort_keys=True, indent=4, separators=(',', ': ')))

    assert i['media'] == 'Unknown'
    assert i['media_select'] == 'autoselect'
    assert i['media_type'] == '1000baseT'
    assert i['media_options'] == {'full-duplex': None, 'flow-control': None}


test_DarwinNetwork_parse_media_

# Generated at 2022-06-13 01:20:32.119446
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    net = DarwinNetwork()
    current_if = dict()

    # Check for 'unknown type' in media line
    words = ['media', '<unknown', 'type>']
    net.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    # Check for valid media line
    words = ['media', 'autoselect', '(none)']
    net.parse_media_line(words, current_if, None)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'

# Generated at 2022-06-13 01:20:40.023712
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.darwin import DarwinNetwork
    dn = DarwinNetwork({})
    # Simulate ifconfig output for a Mac OS X bridge
    # the media_select is '<unknown' and media_type is 'type>'
    line = '<unknown type>'
    words = line.split(' ')
    i = {}
    dn.parse_media_line(words=words, current_if=i, ips=[])
    assert i['media_select'] == 'Unknown'
    assert i['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:20:48.043993
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dnw = DarwinNetwork()
    ifc = {}
    ips = {}
    flds = []

    flds.append('media:')
    assert ifc == {}
    dnw.parse_media_line(flds,ifc,ips)
    assert ifc['media'] == 'Unknown'
    assert ifc['media_select'] == ''
    assert 'media_type' not in ifc
    assert 'media_options' not in ifc
    flds.clear()

    flds.append('media:')
    flds.append('media_select')
    ifc['media'] = ''
    assert 'media_select' not in ifc
    dnw.parse_media_line(flds,ifc,ips)

# Generated at 2022-06-13 01:20:54.717668
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin = DarwinNetwork()
    current_if = {}
    words = ["media:", '<unknown', 'type>', "status:", "inactive"]
    darwin.parse_media_line(words, current_if, [])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:21:11.824190
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    iface = DarwinNetwork()
    iface.parse_media_line(['media:'], {}, {})
    assert iface.facts['interfaces']['eth0']['media'] == 'Unknown'
    # media select
    iface.parse_media_line(['media:', '10baseT/UTP'], {}, {})
    assert iface.facts['interfaces']['eth0']['media_select'] == '10baseT/UTP'
    # media type
    iface.parse_media_line(['media:', '10baseT/UTP', '<link>'], {}, {})
    assert iface.facts['interfaces']['eth0']['media_type'] == 'link'
    # media options

# Generated at 2022-06-13 01:21:20.997522
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    ifd = {'media_capabilities': None, 'media_options': None, 'media_type': None}
    # case where all expected values are present
    words = ['media:', 'autoselect', '(none)', 'mediaopt', 'mediaopt2']
    d.parse_media_line(words, ifd, [])
    assert ifd['media'] == 'Unknown'
    assert ifd['media_select'] == 'autoselect'
    assert ifd['media_type'] == 'none'
    assert ifd['media_options'] == 'mediaopt mediaopt2'
    # case where media_type is split into two words
    ifd['media'] = None
    ifd['media_select'] = None
    ifd['media_type'] = None

# Generated at 2022-06-13 01:21:29.024524
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    mac = DarwinNetwork()
    current_if = {}
    ips = {}
    # Test with one word
    words = "media: '<unknown type>'"
    mac.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '<unknown'
    assert current_if['media_type'] == 'unknown type'
    # Test with three words
    words = "media: 1000baseTX mediaopt: HD media: Full-duplex"
    mac.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == '1000baseTX'
    assert current_if['media_type'] == 'Full-duplex'


# Generated at 2022-06-13 01:21:34.607502
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    
    class FakeIf(dict):
        pass
            
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    
    fact = DarwinNetwork()
    fake_if = FakeIf()
    words = ['media:', '<unknown type>', 'autoselect', 'status:', 'inactive']
    fake_if['media'] = ''
    fake_if['media_select'] = ''
    fake_if['media_type'] = ''
    fake_if['media_options'] = ''
    fact.parse_media_line(words, fake_if, {})
    assert fake_if['media'] == 'Unknown'
    assert fake_if['media_select'] == 'Unknown'
    assert fake_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:21:38.898461
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = dict()
    test_ips = dict()
    test_line = "media: autoselect <unknown type>"
    test_words = test_line.split()
    DarwinNetwork().parse_media_line(test_words, test_if, test_ips)
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == 'unknown type'



# Generated at 2022-06-13 01:21:43.694864
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    ips = []
    ifconfig_output = []
    ifconfig_output.append('<unknown if>')
    ifconfig_output.append('!<bridge>')
    ifconfig_output.append('!<noaddr>')
    darwin_network = DarwinNetwork()
    words = ['', '<unknown', 'type>']
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

    words = ['', 'Uknown']
    darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media_select'] == 'Uknown'
    assert 'media_type'

# Generated at 2022-06-13 01:21:51.086148
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create object to test DarwinNetwork
    dn = DarwinNetwork()
    # create empty dict for dn.interfaces
    dn.interfaces = {}
    # create the test lines
    line1 = ['media:','<unknown type>','None']
    line2 = ['media:','<unknown','type>','None']
    line3 = ['media:','autoselect','10baseT/UTP','None']
    line4 = ['media:','autoselect','10baseT/UTP','active']
    # create an empty dict to test the changes
    current_if = {}
    # call the method to be tested
    dn.parse_media_line(line1, current_if, {})
    # test the results
    assert current_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:21:54.841269
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_line = "media: <unknown type> status: inactive"
    words = test_line.split()
    test_if = {}
    test_ips = {}
    DarwinNetwork.parse_media_line(DarwinNetwork(), words, test_if, test_ips)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'Unknown'
    assert test_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:22:06.307468
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.generic_bsd import NetworkIf
    from ansible.module_utils.facts.network.generic_bsd import NetworkInterface

    this_if = NetworkIf()
    this_if.update(name='lo0', inet=['127.0.0.1'], inet6=[],
                   media='Unknown', media_select='autoselect', media_type='',
                   media_options={})
    this_if = NetworkInterface(**this_if)
    test_if = NetworkIf()
    test_if.update(name='lo0', inet=['127.0.0.1'], inet6=[],
                   media='Unknown', media_select='autoselect', media_type='',
                   media_options={})

# Generated at 2022-06-13 01:22:13.165623
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:22:41.744715
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    current_if = dict()
    ips = dict()
    network = DarwinNetwork()
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in current_if


# Generated at 2022-06-13 01:22:45.291434
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Init
    facts = DarwinNetwork()

    # Set up variables
    expected_media_select = 'autoselect'
    expected_media_type = '10baseT/UTP'
    expected_media_options = '<link-detect>'
    words = ['autoselect', '10baseT/UTP', '<link-detect>']
    current_if = {'media': 'Unknown'}

    # Actual call
    facts.parse_media_line(words, current_if, None)

    # Assertions
    assert current_if['media_select'] == expected_media_select
    assert current_if['media_type'] == expected_media_type
    assert current_if['media_options'] == expected_media_options

# Generated at 2022-06-13 01:22:52.587267
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    mac = DarwinNetwork(None)
    words = ["media:", "IEEE", "802.11", "(autoselect)"]
    current_if = {

    }
    ips = None
    mac.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown' and current_if['media_select'] == 'IEEE' and current_if['media_type'] == '802.11' and current_if['media_options'] == 'autoselect'

    words = ["media:", "autoselect", "(none)"]
    current_if = {

    }
    ips = None
    mac.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:22:58.758903
# Unit test for method parse_media_line of class DarwinNetwork

# Generated at 2022-06-13 01:23:03.200902
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    line = 'media: autoselect (100baseTX <full-duplex>)'
    words = line.split()
    current_if = {'name': 'e0'}
    ips = {}
    d.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '100baseTX'
    assert current_if['media_options']['full-duplex']



# Generated at 2022-06-13 01:23:11.821553
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork()
    d.parse_media_line(['media:', '10baseT/UTP', '(none)'], None, None)

    # Result I am expecting - looks like the FreeBSD result
    # {'media': '10baseT/UTP',
    #            'media_type': 'none',
    #            'media_select': 'media'}

    # What is currently produced by this code
    # {'media': 'Unknown',
    #            'media_select': '10baseT/UTP'}

    # It looks like it relies on the passed in words array being formatted
    # correctly (i.e. the word none is in a different place to the FreeBSD
    # result.
    #
    # This looks like a bug in the way the media line is read.

# Generated at 2022-06-13 01:23:19.123320
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():

    #create an instance of DarwinNetwork
    darwin_nw = DarwinNetwork()

    #test parse_media_line method with different combination of input words
    test_word_1 = ["media:", "none", "(none)"]
    test_word_2 = ["media:", "1000baseT", "(1000baseT)"]
    test_word_3 = ["media:", "none", "(none/full)"]
    test_word_4 = ["media:", "<unknown", "type>"]
    test_word_5 = ["media:", "auto", "(1000baseT/Full)"]
    test_word_6 = ["media:", "none", "(none/half)"]

    # set current_if to a default value so that we can access its value in assert statements

# Generated at 2022-06-13 01:23:26.032387
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    t_network = DarwinNetwork({})
    t_if = {}
    t_ips = {}
    result = t_network.parse_media_line(['media:', '10baseT/UTP', '(none)'],
                                        t_if, t_ips)
    assert result == None  # parse_media_line does not return anything
    # check content of t_if
    assert t_if['media'] == 'Unknown'
    assert t_if['media_select'] == '10baseT/UTP'
    assert t_if['media_options'] == {}
    assert t_if['media_type'] == '(none)'

# Generated at 2022-06-13 01:23:32.970584
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # pylint: disable=R0903
    #        Too few public methods (1/2)
    network = DarwinNetwork()
    media = network.parse_media_line(['media:', '<unknown type>', 'unknown type'], {}, {})
    assert media.get('media') == 'Unknown'
    assert media.get('media_select') == 'Unknown'
    assert media.get('media_type') == 'unknown type'

    media = network.parse_media_line(['media:', 'autoselect', '<unknown type>', 'unknown type'], {}, {})
    assert media.get('media') == 'Unknown'
    assert media.get('media_select') == 'autoselect'
    assert media.get('media_type') == 'unknown type'

# Generated at 2022-06-13 01:23:38.758424
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    import sys
    import pytest
    if sys.version_info < (2, 7):
        pytest.skip("not compatible with python < 2.7.0")

    current_if = {'inet': [], 'inet6': [], 'media': None, 'media_select': None, 'media_type': None, 'media_options': None, 'ether': None}

    # Testing for weird cases for MacOSX
    data1 = ['media:', '<unknown', 'type>', 'status:', 'inactive']
    data2 = ['media:', '<unknown', 'type>']
    obj = DarwinNetwork

# Generated at 2022-06-13 01:24:31.128566
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    network_class = DarwinNetwork()
    test_data = [
        ['media:', 'autoselect', '(none)'],
        ['media:', 'autoselect', '(none)'],
        ['media:', '<unknown', 'type>'],
        ['supported', 'media:', 'autoselect', '10baseT/UTP', '10baseT/UTP*'],
        ['status:', 'active'],
        ['supported', 'operations:', 'hardware'],
        ['status:', 'inactive'],
        ['supported', 'capabilities:', 'hardware'],
        ['supported', 'media:', '100baseTX', '100baseTX*', '100baseTX-FD', '100baseTX-FD*'],
    ]

# Generated at 2022-06-13 01:24:40.348357
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_class = DarwinNetwork()
    test_if = {}

    words = ["media:", "autoselect"]
    test_class.parse_media_line(words, test_if, {})
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert 'media_type' not in test_if
    assert 'media_options' not in test_if

    words = ["media:", "autoselect", "(none)"]
    test_class.parse_media_line(words, test_if, {})
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == 'none'
    assert 'media_options' not in test_if

# Generated at 2022-06-13 01:24:48.048470
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    ifc = DarwinNetwork()
    current_if = dict()
    ips = dict()
    # media line is different to the default FreeBSD one
    # and this method provides the first example in the code of
    # parsing a Darwin media line
    #
    # media line is different to the default FreeBSD one
    # and this method provides the first example in the code of
    # parsing a Darwin media line

# Generated at 2022-06-13 01:24:52.085776
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    words = [':', '<unknown', 'type>', 'status:', 'inactive']
    current_if = {}
    ips = {}
    d = DarwinNetwork()
    d.parse_media_line(words, current_if, ips)
    assert len(current_if) == 3
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:24:56.580947
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_line = ['media:', '<unknown', 'type>', '(none)']
    test_if = {}

    DarwinNetwork.parse_media_line(test_line, test_if)

    expected = {'media': 'Unknown', 'media_select': 'Unknown',
                'media_type': 'unknown type', 'media_options': None}
    assert expected == test_if

# Generated at 2022-06-13 01:25:04.900869
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork()

    test_list_1 = ["media:", "", "", "", "", "", "", "", "", "", "", "", "status:", "active"]
    test_if_1 = {}
    dn.parse_media_line(test_list_1, test_if_1, {})
    assert test_if_1['media'] == 'Unknown'
    assert test_if_1['media_select'] == ''

    test_list_2 = ["media:", "autoselect", "(none)", "", "", "", "", "", "", "", "", "", "status:", "active"]
    test_if_2 = {}
    dn.parse_media_line(test_list_2, test_if_2, {})
    assert test_if_2

# Generated at 2022-06-13 01:25:11.054994
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # The test here is based on the actual output of ifconfig on Mac OS Sierra,
    # which is different than other platforms
    test_if = {
        'iface': 'lo0',
        'inet': ['fe80::1%lo0', '127.0.0.1'],
        'inet6': ['fe80::1%lo0', '::1'],
        'macaddress': '00:00:00:00:00:00',
    }

    n = DarwinNetwork()

    # Test words after media line is 2
    test_words = ['media:', 'autoselect', 'status:', 'inactive']
    n.parse_media_line(test_words, test_if, dict())
    assert test_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:25:16.125402
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    entry = {}
    line = 'media: <unknown type>'
    lineWords = line.split()
    (entry['media'], entry['media_select'], entry['media_type'], entry['media_options']) = DarwinNetwork.parse_media_line(DarwinNetwork, lineWords, entry, entry)
    assert entry['media'] == 'Unknown'
    assert entry['media_select'] == '<unknown'
    assert entry['media_type'] == 'type>'
    assert entry['media_options'] == None

# Generated at 2022-06-13 01:25:20.614191
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    line = 'media: <unknown type>'
    current_if = {
        'device' : 'lo0',
        'ipv4' : [],
        'ipv6' : []
    }
    words = line.split()
    testNetwork = DarwinNetwork(current_if)
    testNetwork.parse_media_line(words, current_if, [])
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

# Generated at 2022-06-13 01:25:28.580259
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    DarwinNetwork_class = DarwinNetwork()
    test_parameter = [
        {'input': ['media:', '<unknown type>'], 'expected_output': {'media': 'Unknown', 'media_select': '<unknown type>'}},
        {'input': ['media:', 'autoselect', '(none)'], 'expected_output': {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': '(none)'}}
    ]
    for test in test_parameter:
        DarwinNetwork_class.parse_media_line(test['input'], {}, [])
        assert DarwinNetwork_class.current_if == test['expected_output']

# Generated at 2022-06-13 01:26:16.454201
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {}
    dn = DarwinNetwork()

    # standard media values
    words = ['media:', 'autoselect', '(none)', 'status:', 'inactive']
    dn.parse_media_line(words, test_if, None)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'autoselect'
    assert test_if['media_type'] == 'none'
    assert test_if['media_options'] == []

    # drop information
    dn.parse_media_line(['media:', '10baseT/UTP', '(none)', 'status:', 'active'], test_if, None)
    assert test_if['media'] == 'Unknown'

# Generated at 2022-06-13 01:26:22.301231
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    doc = DarwinNetwork()
    test_if = {}
    test_parse_media_line1 = doc.parse_media_line(['media:','auto','1000baseT','<full-duplex>','none'], test_if)
    assert test_if['media'] == 'Unknown'
    assert test_if['media_select'] == 'auto'
    assert test_if['media_type'] == '1000baseT'
    assert test_if['media_options'] == 'full-duplex'

    test_if_2 = {}
    test_parse_media_line2 = doc.parse_media_line(['media:','manual', '<unknown', 'type>', 'none'], test_if_2)
    assert test_if_2['media_select'] == 'manual'

# Generated at 2022-06-13 01:26:28.057504
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    # sample media line with media_options
    words = 'media: autoselect (100baseTX <full-duplex>,10baseT/UTP <half-duplex>)'
    ips = []
    DarwinNetwork().parse_media_line(words.split(), current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '100baseTX full-duplex 10baseT/UTP half-duplex'
    assert current_if['media_options'] == 'full-duplex,half-duplex'
    # sample media line without media_options
    words = 'media: autoselect (1000baseT <full-duplex>)'
    current_if = {}

# Generated at 2022-06-13 01:26:32.539772
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    words = ['media:', 'IEEE', '802.11', 'Diversity']
    ips = []

    # Initialise DarwinNetwork object
    darwin_network = DarwinNetwork()

    # Parse the media line
    darwin_network.parse_media_line(words, current_if, ips)

    # Some assertions
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'IEEE'
    assert current_if['media_type'] == '802.11'
    assert current_if['media_options']['Diversity'] is None

# Generated at 2022-06-13 01:26:36.888110
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # create test object
    mac_if = DarwinNetwork()
    # create dictionary for current interface - ifconfig result for interface en0
    current_if = {}

    # test #1 - set up media values for en0
    words = ['unknown', 'type']
    current_if['media'] = 'Unknown'
    current_if['media_select'] = words[1]
    mac_if.parse_media_line(words, current_if, 0)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert current_if['media_options'] == None

# Generated at 2022-06-13 01:26:40.267438
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    actual_result = DarwinNetwork().parse_media_line(['media:', 'autoselect', '<unknown type>'], {}, {})
    expected_result = {
        'media': 'Unknown',
        'media_select': 'autoselect',
        'media_options': {},
        'media_type': 'unknown type'
    }
    assert actual_result == expected_result