

# Generated at 2022-06-13 01:16:49.562557
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    current_if = {}
    ips = {}
    # test for words[1] == '<unknown' and words[2] == 'type>'
    d = DarwinNetwork(current_if, ips)
    d.parse_media_line(['media', '<unknown', 'type>'], current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    # test for words[1] != '<unknown' and words[2] == 'type>'
    d.parse_media_line(['media', 'autoselect', '<unknown type>'], current_if, ips)
    assert current_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:16:58.357663
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    darwin = DarwinNetwork()

# Generated at 2022-06-13 01:17:08.318759
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    # Input data
    words1 = ['media:', 'autoselect', '(none)', 'status:', 'inactive']  # no media
    words2 = ['media:', 'AUI', '(autoselect)', 'status:', 'inactive']  # media with brackets
    words3 = ['media:', '<unknown', 'type>', 'status:', 'inactive']  # unknown type
    # Expected output data
    exp_words1 = {'media': 'Unknown', 'media_select': 'autoselect', 'media_options': 'none'}
    exp_words2 = {'media': 'Unknown', 'media_select': 'AUI', 'media_type': 'autoselect'}

# Generated at 2022-06-13 01:17:10.065244
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    t = DarwinNetwork()
    words = ["media:", "<unknown", "type>", "status:", "active"]
    current_if = {}
    t.parse_media_line(words, current_if, [{}])
    assert current_if['media_select'] == "Unknown"
    assert current_if['media_type'] == "unknown type"

# Generated at 2022-06-13 01:17:18.711073
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    d = DarwinNetwork({})
    m = {'media': 'Unknown', 'media_select': 'autoselect', 'media_type': 'none', 'media_options': 'none'}
    i = {'hw_addr': '00:00:00:00:00:00'}
    d.parse_media_line('autoselect', i)
    assert i == m


# Generated at 2022-06-13 01:17:24.956075
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    media_line = {'media': 'Unknown',
                  'media_select': 'autoselect',
                  'media_options': {},
                  'media_type': 'none'}
    line = 'autoselect status: active'
    test_if = {'media': 'Unknown',
                  'media_select': 'autoselect',
                  'media_options': {},
                  'media_type': 'none'}
    dn = DarwinNetwork()
    dn.parse_media_line(line.split(), test_if, {})
    assert test_if == media_line

# Generated at 2022-06-13 01:17:35.711500
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test = DarwinNetwork()
    current_if = {'media': 'Unknown'}
    test.parse_media_line(['media:', 'media_select', 'media_type', 'media_options'], current_if, None)
    assert (current_if['media'] == 'Unknown')
    assert (current_if['media_select'] == 'media_select')
    assert (current_if['media_type'] == 'media_type')
    assert (current_if['media_options'] == 'media_options')
    current_if = {'media': 'Unknown'}
    test.parse_media_line(['media:', 'media_select', 'media_type'], current_if, None)
    assert (current_if['media'] == 'Unknown')

# Generated at 2022-06-13 01:17:43.535934
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    from ansible.module_utils.facts.network.darwin.ifconfig import DarwinNetwork
    from collections import namedtuple
    # test scenario with 'media_select', 'media_type' and 'media_options' set
    # {'media_options': 'none', 'media_select': 'autoselect', 'media_type': '10baseT/UTP <link>', 'media': 'Unknown'}

    def get_options(param):
        return None

    DarwinNetwork.get_options = get_options
    test_data = namedtuple('words', 'word1 word2 word3 word4')
    word_list = test_data(word1='media:', word2='autoselect', word3='<10baseT/UTP>', word4='status:')
    current_if = {}
    ips = []


# Generated at 2022-06-13 01:17:53.036515
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    test_if = {}
    line = "media: autoselect (autoselect)"
    current_if = {}
    ips = []
    DarwinNetwork().parse_media_line(line.split(), current_if, ips)
    assert current_if == test_if
    line = "media: autoselect (none)"
    DarwinNetwork().parse_media_line(line.split(), current_if, ips)
    test_if['media_select'] = 'none'
    test_if['media_type'] = 'autoselect'
    assert current_if == test_if



# Generated at 2022-06-13 01:17:59.303394
# Unit test for method parse_media_line of class DarwinNetwork
def test_DarwinNetwork_parse_media_line():
    dn = DarwinNetwork(None)
    interface = {}
    dn.parse_media_line(['media:', 'auto', '10baseT/UTP'], interface, None)
    assert(interface == {'media': 'Unknown', 'media_select': 'auto', 'media_type': '10baseT/UTP'})
    interface = {}
    dn.parse_media_line(['media:', '<unknown', 'type>'], interface, None)
    assert(interface == {'media': 'Unknown', 'media_select': 'Unknown', 'media_type': 'unknown type'})