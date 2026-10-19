

# Generated at 2022-06-13 02:51:28.997575
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content

    dns_facts_expected = {
        'dns': {
            'domain': 'openstacklocal',
            'nameservers': [
                '192.168.1.190',
                '192.168.1.191'
            ],
            'options': {
                'rotate': True,
                'timeout': 2
            },
            'search': [
                'openstacklocal',
                'localdomain'
            ]
        }
    }

    mock_get_file_content = __import__('mock').Mock(side_effect=lambda x, y=None: get_file_content(x, y))


# Generated at 2022-06-13 02:51:32.279447
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:51:33.119936
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'
    assert obj._fact_ids is not None

# Generated at 2022-06-13 02:51:33.907543
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'



# Generated at 2022-06-13 02:51:41.269339
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = {'dns': {'domain': 'corp.ansible.com',
                         'nameservers': ['192.168.42.250', '192.168.42.251'],
                         'options': {'rotate': True,
                                     'attempts': 5,
                                     'timeout': 5},
                         'search': ['corp.ansible.com', 'ansible.com'],
                         'sortlist': ['10.11.12.0/255.255.255.0',
                                      '10.11.13.0/255.255.255.0']}}
    dc = DnsFactCollector()
    res = dc.collect()
    assert res == dns_facts

# Generated at 2022-06-13 02:51:49.600110
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Test method 'collect' of class 'DnsFactCollector'.
    """
    # Content of sample file '/etc/resolv.conf'
    content = 'search domain1 domain2\nnameserver 10.0.0.1\nnameserver 10.0.0.2\nsortlist 10.0.0.3\noptions timeout:1\noptions attempts:3\n#INCLUDE "/etc/resolv-tail.conf"\n'
    test_facts = DnsFactCollector().collect(collected_facts=None, module=None)
    assert test_facts['dns']['search'] == ['domain1', 'domain2']
    assert test_facts['dns']['nameservers'] == ['10.0.0.1', '10.0.0.2']

# Generated at 2022-06-13 02:51:55.363175
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """ Return a fact in the format ansible would expect is the contents of the
        /etc/resolv.conf file is as below.
    """

    # Get test data
    input_data = """domain example.com\nsearch sub.example.com\nnameserver 192.0.2.2\nnameserver 192.0.2.3\nnameserver 192.0.2.4\noptions timeout:1 attempts:2 rotate single-request-reopen\n"""

    # Do not write the output file
    DnsFactCollector.write_file = False

    # Create test instance of DnsFactCollector
    dfc = DnsFactCollector()

    # Call the collect method of class DnsFactCollector with input_data

# Generated at 2022-06-13 02:51:58.613316
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fc = DnsFactCollector()
    collected_facts = dict()
    fc.collect()
    assert 'domain' or 'dns' in collected_facts


# Generated at 2022-06-13 02:52:09.125143
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    input = """
# This is a comment line
nameserver 192.168.0.1
nameserver 192.168.0.2
domain redhat.com
search example.com example.org
sortlist 192.168.1.0/24 192.168.2.0/24
options timeout:1 attempts:2 rotate"""

    with open('/etc/resolv.conf', 'w') as f:
      f.write(input)

    dns_facts = DnsFactCollector().collect()
    dns = dns_facts['dns']
    assert len(dns['nameservers']) == 2
    assert 'domain' in dns
    assert len(dns['search']) == 2
    assert len(dns['sortlist']) == 2
    assert len(dns['options']) == 3

# Generated at 2022-06-13 02:52:17.250052
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactManager

    test_content = '''# foo
nameserver 1.2.3.4
domain foo.bar
search baz
search qux
sortlist pqr
options a:b:c:d
'''

    def mock_get_file_content(file, default):
        if file == '/etc/resolv.conf':
            return test_content

        return default

    import ansible.module_utils.facts.utils
    ansible.module_utils.facts.utils.get_file_content = mock_get_file_content

    dns_fact_collector = Collector.fact_classes['dns']()
    fact_manager = FactManager()
    fact_data = dns_fact_collect

# Generated at 2022-06-13 02:52:41.829595
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    This unit test is designed to test the collect
    method of class DnsFactCollector.

    The method collect returns a dictionary of dictionaries.
    The first dictionary has a key which is the value of the
    public variable name of class DnsFactCollector.  The
    value of the first dictionary's key is a dictionary which
    contains the DNS information.
    """
    dns_facts = {
        'dns': {
            'nameservers': [
                '127.0.0.1', 
            ],
        }
    }

    def MockOpen(filename, mode):
        if filename == '/etc/resolv.conf':
            return MockFile(['nameserver 127.0.0.1'])

    dns_collector = DnsFactCollector() 
    dns_collector.get_

# Generated at 2022-06-13 02:52:44.333370
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """
    Unit test for constructor of DnsFactCollector.
    """
    DnsFactCollector()

# Generated at 2022-06-13 02:52:45.914960
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name in dns._fact_ids

# Generated at 2022-06-13 02:52:46.732005
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    assert DnsFactCollector().collect()

# Generated at 2022-06-13 02:52:47.241910
# Unit test for method collect of class DnsFactCollector

# Generated at 2022-06-13 02:52:54.841755
# Unit test for method collect of class DnsFactCollector

# Generated at 2022-06-13 02:52:55.772905
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    DnsFactCollector.collect()

# Generated at 2022-06-13 02:52:58.035594
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
  obj = DnsFactCollector()
  assert obj.name == 'dns'


# Generated at 2022-06-13 02:53:00.692044
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert type(DnsFactCollector._fact_ids) is set
    assert len(DnsFactCollector._fact_ids) == 0

# Generated at 2022-06-13 02:53:03.673151
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFacts = DnsFactCollector()
    assert dnsFacts.name == 'dns'
    assert dnsFacts._fact_ids == set()


# Generated at 2022-06-13 02:53:44.236823
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import sys
    import ansible.module_utils.facts.collectors.dns as dns
    content = """# Generated by NetworkManager
domain localdomain
 search localdomain
nameserver 127.0.0.1
nameserver 10.10.10.10
nameserver 10.10.10.11
nameserver 10.10.10.12
"""
    dns.get_file_content = lambda x,y: content
    res = dns.DnsFactCollector().collect()
    assert res['dns']['domain'] == 'localdomain'
    assert res['dns']['search'] == ['localdomain']
    assert res['dns'].get('sortlist') == None

# Generated at 2022-06-13 02:53:50.014344
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Test if the collect method of the DnsFactCollector class returns a dictionary with a list of nameservers
    """
    collector = DnsFactCollector()
    nameservers = collector.collect()['dns']['nameservers']
    assert nameservers == ['127.0.0.1'], 'Unexpected DNS nameservers: %s' % nameservers

# Generated at 2022-06-13 02:54:00.635671
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os
    import filecmp


# Generated at 2022-06-13 02:54:03.698308
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    dns_facts = dns_fact_collector.collect()
    assert 'dns' in dns_facts
    assert dns_facts['dns'] is not None

# Generated at 2022-06-13 02:54:05.735286
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    assert not dns.collect()

# Generated at 2022-06-13 02:54:08.301612
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.__name__ == 'DnsFactCollector'
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:54:10.144481
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'


# Generated at 2022-06-13 02:54:11.872459
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    for dns_key, dns_value in dns_facts.collect()['dns'].items():
        if dns_value:
            assert True
        else:
            assert False

# Generated at 2022-06-13 02:54:14.437153
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    facts = collector.collect()

    assert(facts['dns'] == {'domain': 'eng.ansible.com',
                            'nameservers': ['8.8.8.8', '8.8.4.4'],
                            'options': {'rotate': True,
                                        'timeout': 2},
                            'search': ['eng.ansible.com', 'redhat.com']})

# Generated at 2022-06-13 02:54:22.395637
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector_obj = DnsFactCollector()
    result = dns_fact_collector_obj.collect()
    assert result.has_key('dns')
    assert result['dns']
    assert result['dns'].has_key('nameservers')
    assert result['dns'].has_key('domain')
    assert result['dns'].has_key('search')
    assert result['dns'].has_key('sortlist')
    assert result['dns'].has_key('options')

if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 02:54:57.796783
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # test without argument
    dnsFactCollector = DnsFactCollector()
    assert dnsFactCollector.name == 'dns'
    assert dnsFactCollector._fact_ids == set()

    # test with argument
    dnsFactCollector = DnsFactCollector(name='test', collect_subset=['!all', 'dns'])
    assert dnsFactCollector.name == 'test'
    assert dnsFactCollector._fact_ids == set(['dns'])


# Generated at 2022-06-13 02:55:00.606035
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
  print(DnsFactCollector().collect())
  # expected output: {'dns': {'nameservers': ['8.8.8.8'], 'domain': 'localdomain', 'search': [], 'sortlist': []}}

# Generated at 2022-06-13 02:55:01.033069
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 02:55:03.516414
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    check_collector = DnsFactCollector()

    assert check_collector.name == "dns"
    assert check_collector._fact_ids == set()


# Generated at 2022-06-13 02:55:08.400113
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    # Test default values
    def test_default(config, expected_nameservers=[], expected_domain=None, expected_search=None, expected_sortlist=None, expected_options=None):
        test_config = config
        def get_file_content(file, default=None):
            return test_config
        from ansible.module_utils.facts.collector import DnsFactCollector 
        collector = DnsFactCollector()
        collector.get_file_content = get_file_content
        facts = collector.collect()
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == expected_nameservers
        if expected_domain is not None:
            assert 'domain' in facts['dns']

# Generated at 2022-06-13 02:55:09.967269
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()

    assert dns_facts.name == 'dns'

# Generated at 2022-06-13 02:55:12.212975
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts_collector = DnsFactCollector()

    assert dns_facts_collector.name == 'dns'
    assert dns_facts_collector._fact_ids == set()

# Generated at 2022-06-13 02:55:15.053807
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()
    dns_facts = dfc.collect()
    assert dns_facts['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']

# Generated at 2022-06-13 02:55:16.418137
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    # check name attribute exists
    assert dns_facts.name

# Generated at 2022-06-13 02:55:26.519196
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()

    # Set the content of file '/etc/resolv.conf'
    content = ('# Generated by NetworkManager\n\n'
               'nameserver 8.8.8.8\n'
               'nameserver 8.8.4.4\n'
               '#nameserver 10.1.1.1\n'
               'search example.com\n'
               'domain example.com\n'
               'sortlist 1.1.1.1 2.2.2.2\n'
               'options attempts:5 timeout:15')

    # Set the value of the file_exists method of File module to return true
    import ansible.module_utils.facts.hardware.dns

# Generated at 2022-06-13 02:56:43.772014
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'

# Generated at 2022-06-13 02:56:50.165987
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Test a collected fact for DnsFactCollector
    The method DnsFactCollector.collect() returns a dictionary with
    DNS information from /etc/resolv.conf
    :return:
    """
    test_path = os.path.dirname(os.path.abspath(__file__))
    my_file = open(os.path.join(test_path, 'resolv.conf.example'), 'r')
    content = my_file.read()
    my_file.close()
    test_content = StringIO(content)
    test_file = open('/mocked/resolv.conf', 'w+')
    test_file.write(test_content.read())
    test_file.close()

    dns_collector = DnsFactCollector()

# Generated at 2022-06-13 02:56:58.861768
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os, tempfile
    try:
        dns = DnsFactCollector()
        fd, path = tempfile.mkstemp()
        content = """search calix.local
nameserver 192.168.12.1
nameserver 192.168.6.1
"""
        os.write(fd, content.encode('utf-8'))
        os.close(fd)
        facts = dns.collect(collected_facts=None, module=None)
        assert facts['dns']['search'] == ['calix.local']
        assert facts['dns']['nameservers'] == [u'192.168.12.1', u'192.168.6.1']
        os.remove(path)
    finally:
        os.remove(path)


# Generated at 2022-06-13 02:57:02.478611
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    sut = DnsFactCollector()
    test_data = get_DnsFactCollector_collect_test_data()

    result = sut.collect(test_data, None)

    assert result is not None
    assert len(result) == 1
    assert 'dns' in result
    assert result['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']


# Generated at 2022-06-13 02:57:03.859134
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    facts = collector.collect()

    assert(len(facts['dns']['nameservers']) > 0)
    assert(len(facts['dns']['options']) > 0)

# Generated at 2022-06-13 02:57:04.570244
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 02:57:05.478831
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns is not None

# Unit test of collect method of class DnsFactCollector

# Generated at 2022-06-13 02:57:09.124545
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    input = '''
; generated by /usr/sbin/dhclient-script
search lan
nameserver 1.2.3.4
nameserver 5.6.7.8
nameserver 9.10.11.12
options edns0
    '''
    expected_output = {
        'dns': {
            'nameservers': [
                '1.2.3.4',
                '5.6.7.8',
                '9.10.11.12',
            ],
            'search': [
                'lan',
            ],
            'options': {
                'edns0': True,
            },
        }
    }
    result = DnsFactCollector().collect(None, None)
    assert result == expected_output

# Generated at 2022-06-13 02:57:12.539032
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # TODO: remove this test once unit tests are written for all collectors

    # Setup
    module = None
    collected_facts = {}
    dns_collector = DnsFactCollector()

    # Test
    dns_facts = dns_collector.collect(module, collected_facts)
    assert isinstance(dns_facts, dict)


# vim: set filetype=python

# Generated at 2022-06-13 02:57:13.480486
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.collect()

# Generated at 2022-06-13 03:00:29.966354
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsF

# Generated at 2022-06-13 03:00:32.653539
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert isinstance(dns_fact_collector, DnsFactCollector)
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 03:00:38.790265
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    # Initialize the collector instance
    dns_fact_collector = DnsFactCollector()

    file_content = """
# Comment
nameserver 1.2.3.4
nameserver 5.6.7.8 # Comment
; More comment
domain example.com
search example.com example2.com
"""
    # Test case no.1.
    def test_file_content_no_1():
        return file_content
    dns_fact_collector.get_file_content = test_file_content_no_1

    # Collect the facts
    result = dns_fact_collector.collect(None, None)

    # Check the facts

# Generated at 2022-06-13 03:00:43.332819
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import timeout
    import os
    import textwrap
    import pytest

    my_env = os.environ.copy()
    my_env.update({
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "ANSIBLE_LOCAL_TMP": "/tmp/ansible_local",
    })


# Generated at 2022-06-13 03:00:44.793698
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfact = DnsFactCollector()
    assert dnsfact.name == 'dns'

# Generated at 2022-06-13 03:00:45.818776
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    # TODO: Write unit test

# Generated at 2022-06-13 03:00:46.599872
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    DnsFactCollector().collect()

# Generated at 2022-06-13 03:00:48.797499
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dnsFactCollector = DnsFactCollector()
    result = dnsFactCollector.collect()
    assert result is not None and len(result) == 1, "Failed to collect dns facts"

# Generated at 2022-06-13 03:00:57.548547
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector

    class DummyFile(object):
        def read(self):
            return """
# I am a comment
nameserver    8.8.8.8
domain        foo.bar
search        foo.bar
search        foobar.bar
sortlist      192.168.1.0/255.255.255.0
options       debug
options       timeout:1
options       attempts:1
options       rotate
options       ndots:2
nameserver    4.2.2.2
nameserver    4.2.2.1
"""
        def close(self):
            return

    # TODO: there might be a better way to inject content.
    dummy_content = DummyFile

# Generated at 2022-06-13 03:01:06.602943
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_result = {
        'dns': {
            'nameservers': [
                '127.0.0.1'
            ],
            'search': [
                'test.example.com',
                'example.com'
            ],
            'domain': 'test.example.com',
            'sortlist': [
                '1.1.1.1/2.2.2.2',
                '2.2.2.2/1.1.1.1'
            ],
            'options': {
                'timeout': '2',
                'ndots': '3'
            }
        }
    }
