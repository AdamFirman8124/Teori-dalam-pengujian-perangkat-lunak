

# Generated at 2022-06-13 02:51:22.886748
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFactCollector = DnsFactCollector()

    assert dnsFactCollector
    assert dnsFactCollector.name =='dns'

# Generated at 2022-06-13 02:51:24.628818
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'
    assert dns._fact_ids == set()


# Generated at 2022-06-13 02:51:31.358614
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collect = DnsFactCollector().collect()
    expected_collect = {
        'dns': {
            'search': [
                'test.example.com'
            ],
            'nameservers': [
                '192.0.2.1',
                '192.0.2.2'
            ],
            'options': {
                'edns0': True
            },
            'domain': 'example.com'
        }
    }
    assert collect == expected_collect

# Generated at 2022-06-13 02:51:32.280687
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'

# Generated at 2022-06-13 02:51:36.253459
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    dns_facts = dns.collect()
    assert dns_facts['dns']
    for key in dns_facts['dns']:
        assert key in ['nameservers', 'domain', 'search', 'sortlist', 'options']

# Generated at 2022-06-13 02:51:38.541982
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()
    assert DnsFactCollector.__name__ == 'DnsFactCollector'


# Generated at 2022-06-13 02:51:48.128300
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import sys
    import os
    import io
    import types
    import mock

    # ignore pytest idiom for mock
    # pylint: disable=no-member
    MockObject = mock.Mock()
    mock_fact_collector = types.InstanceType(MockObject)
    mock_fact_collector.get_file_content = get_file_content
    mock_fact_collector.name = 'dns'
    mock_fact_collector._fact_ids = set()

    dns_facts = {}

    dns_facts['dns'] = {}

    dns_facts['dns']['sortlist'] = ['192.168.0.0/24']
    dns_facts['dns']['options'] = {'rotate': True, 'timeout:1': True}
    dns

# Generated at 2022-06-13 02:51:50.663051
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert set(['dns']).issubset(set(dns_fact_collector._fact_ids))


# Generated at 2022-06-13 02:51:51.505745
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    facts_obj = DnsFactCollector()
    assert facts_obj is not None

# Generated at 2022-06-13 02:51:53.725556
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    dns_facts = DnsFactCollector().collect()

    assert isinstance(dns_facts, dict)
    assert isinstance(dns_facts['dns'], dict)

# Generated at 2022-06-13 02:52:11.251663
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    DnsFactCollector_inst = DnsFactCollector()

    facts = DnsFactCollector_inst.collect()
    assert(len(facts) == 1)
    assert(facts['dns']['nameservers'][0] == '8.8.8.8')
    assert(facts['dns']['domain'] == 'example.com')
    assert(facts['dns']['search'][0] == 'example.com')
    assert(facts['dns']['sortlist'][0] == '10.0.0.0/24')
    assert(facts['dns']['sortlist'][1] == '10.10.0.0/255.255.0.0')
    assert(facts['dns']['options']['timeout'])

# Generated at 2022-06-13 02:52:13.230907
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_sut = DnsFactCollector()
    dns_sut.collect(module=None, collected_facts=None)

# Generated at 2022-06-13 02:52:14.687549
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'
    assert dns._fact_ids == set()

    # TODO: test collect

# Generated at 2022-06-13 02:52:16.297438
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    x = DnsFactCollector()
    assert x.name == 'dns'

# Generated at 2022-06-13 02:52:17.761879
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector = DnsFactCollector()
    assert dns_collector.name == 'dns'



# Generated at 2022-06-13 02:52:21.275684
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # No config file
    dfc = DnsFactCollector(None)
    assert dfc.name == 'dns'
    assert dfc._fact_ids == set()


# Generated at 2022-06-13 02:52:23.547635
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()
    result = fact_collector.collect()
    assert result['dns'] is None

# Generated at 2022-06-13 02:52:25.466892
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    base_collector = BaseFactCollector()
    dns_obj = DnsFactCollector(base_collector)

# Generated at 2022-06-13 02:52:27.268473
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_DnsFactCollector = DnsFactCollector()
    test_DnsFactCollector.collect()

# Generated at 2022-06-13 02:52:29.527626
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()
    result = fact_collector.collect()
    assert result.get('dns')

# Generated at 2022-06-13 02:52:52.123263
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    def get_file_content(path, default=''):
        return '''#;
        #; Sample resolv.conf
        #;
        #; nameserver 127.0.0.53
        #; search example.com
        #; domain example.com
        #; resolv-file=/etc/resolv.conf.d/head
        #;
        #; Caching nameserver using dnsmasq
        nameserver 192.168.1.1
        nameserver 192.168.2.1
        nameserver 192.168.3.1
        domain example.com
        search example.com foo
        search bar example.com
        sortlist 192.168.10.1/16
        options debug
        options ndots:2
        options no-check-names
        options attempts:3
    '''



# Generated at 2022-06-13 02:53:02.708599
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create instance of class DnsFactCollector
    dfc = DnsFactCollector()

    # Create dummy file /etc/resolv.conf

# Generated at 2022-06-13 02:53:06.032828
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fact_collector = DnsFactCollector()
    assert fact_collector is not None
    assert fact_collector.name == 'dns'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:53:07.840013
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:53:09.109438
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    d = DnsFactCollector()
    assert d.name == 'dns'
    assert d._fact_ids is None


# Generated at 2022-06-13 02:53:10.847387
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = {}

    # TODO: flatten
    dns_facts['dns'] = {}


# Generated at 2022-06-13 02:53:11.516596
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    DnsFactCollector()

# Generated at 2022-06-13 02:53:13.417507
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()


# Generated at 2022-06-13 02:53:14.801755
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()

    assert dns.name == 'dns'



# Generated at 2022-06-13 02:53:23.029823
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    module = None
    collection = FactCollector(module=module)
    dnsFactCollector = collection.get_collector("dns")

    #Test DNS resolv.conf with just one nameserver
    with open("/etc/resolv.conf", "w") as fp:
        fp.write("#This is a comment\n")
        fp.write("domain ansible.lab\n")
        fp.write("nameserver 192.168.1.2\n")

    assert(len(dnsFactCollector.collect()['dns']['nameservers']) == 1)

    #Test DNS resolv.conf with more than one nameserver

# Generated at 2022-06-13 02:53:59.712248
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    print("test_DnsFactCollector_collect: start")
    # Instantiate a DnsFactCollector.
    dns_collector = DnsFactCollector()
    # Invoke method collect of class DnsFactCollector
    results = dns_collector.collect();
    # Assert that method collect returns a list.
    assert(isinstance(results, dict));
    # Assert that method collect returns a list with a single element.
    assert(len(results) == 1);
    # Assert that method collect returns a list with a single element for
    # the key 'dns'.
    assert(len(results['dns']) > 0);
    # Assert that method collect returns a list with a single element for
    # the key 'dns' and that the returned element is a dict.

# Generated at 2022-06-13 02:54:03.449135
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()

    assert_none(dns_fact_collector)

    assert_equals(dns_fact_collector.name, 'dns')
    assert_equals(dns_fact_collector._fact_ids, set())


# Generated at 2022-06-13 02:54:06.163578
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact = DnsFactCollector()
    res = dns_fact.collect()
    assert (res.keys() == ['dns'])

# Generated at 2022-06-13 02:54:08.756114
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc is not None

# Local Variables:
# mode: python
# tab-width: 4
# indent-tabs-mode: nil
# End:

# Generated at 2022-06-13 02:54:10.118342
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()
    assert isinstance(DnsFactCollector.collect(), dict)

# Generated at 2022-06-13 02:54:10.957486
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    DnsFactCollector.collect()
    pass

# Generated at 2022-06-13 02:54:11.751401
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc is not None

# Generated at 2022-06-13 02:54:12.107715
# Unit test for constructor of class DnsFactCollector

# Generated at 2022-06-13 02:54:16.242596
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFactCollector = DnsFactCollector()
    assert dnsFactCollector.name == 'dns'
    assert dnsFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:54:25.084863
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import platform
    import unittest

    class TestDnsFactCollector(unittest.TestCase):

        def test_dns_fact_collector(self):
            from ansible.module_utils.facts.collector.dns import DnsFactCollector

            test_subject = DnsFactCollector()
            dns_facts = test_subject.collect()
            self.assertEqual(dns_facts['dns'], {'nameservers': {'8.8.8.8', '8.8.4.4'}})

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDnsFactCollector))
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 02:55:21.878366
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert 'dns' == DnsFactCollector().name

# Generated at 2022-06-13 02:55:27.623460
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()
    facts = fact_collector.collect()
    assert facts['dns'] == {'nameservers': ['2001:4860:4860::8888', '2001:4860:4860::8844', '8.8.8.8', '8.8.4.4'], 'search': ['lan'], 'domain': 'lan'}

# Generated at 2022-06-13 02:55:28.674805
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfc = DnsFactCollector()
    assert dnsfc

# Generated at 2022-06-13 02:55:32.218290
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """Test constructor of class DnsFactCollector"""
    dns_facts = DnsFactCollector()
    assert dns_facts.name == "dns"
    assert dns_facts._fact_ids == set()

    return dns_facts


# Generated at 2022-06-13 02:55:34.587096
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    sut = DnsFactCollector()
    assert sut.name == 'dns'
    assert sut.collect() == {}

# Generated at 2022-06-13 02:55:35.518826
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass # TODO: Implement test


# Generated at 2022-06-13 02:55:36.372870
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector().name == 'dns'

# Generated at 2022-06-13 02:55:45.474887
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    content = '''
# generated by /usr/sbin/dhclient-script
search domain.com sub.domain.com
nameserver 10.1.2.10
nameserver 10.1.2.11
nameserver 10.1.2.12
nameserver 10.1.2.13

'''
    contents = {'/etc/resolv.conf': content}
    dns_facts_collector = DnsFactCollector(None, contents)
    facts = dns_facts_collector.collect()
    if facts['dns']['search'] != ['domain.com', 'sub.domain.com']:
        print(facts['dns']['search'])
        raise Exception('search')

# Generated at 2022-06-13 02:55:52.483802
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleCollector
    from ansible.module_utils.facts.utils import get_file_content
    import os

    def get_file_content_side_effect(path, default=None):
        fake_content1 = '''
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 8.8.8.8
nameserver 8.8.4.4
#nameserver 4.4.4.4
search my.domain.com
sortlist
    '''

        if path == '/etc/resolv.conf':
            return fake_content1
        else:
            return 'Default'

   

# Generated at 2022-06-13 02:56:02.940063
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # set variables for unit testing
    test_content = '''# comment
domain example.org
search example.com example.net
options attempts:3 rotate
nameserver 192.168.0.101
nameserver 192.168.0.102'''
    test_output = {'dns':
                       {'domain': 'example.org',
                        'options': {'attempts': '3', 'rotate': True},
                        'nameservers': ['192.168.0.101', '192.168.0.102'],
                        'search': ['example.com', 'example.net']
                        }
                   }

    # setup mocking for unit testing

# Generated at 2022-06-13 02:58:38.607108
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    instance = DnsFactCollector()
    line = 'search abc.efg xyz.com'
    dns_facts = {}
    dns_facts['dns'] = {}
    dns_facts['dns']['search'] = []
    dns_facts['dns']['search'].append('abc.efg')
    dns_facts['dns']['search'].append('xyz.com')

    tokens = line.split()
    for suffix in tokens[1:]:
        dns_facts['dns']['search'].append(suffix)

    assert dns_facts == instance.collect()

# Generated at 2022-06-13 02:58:40.206151
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:58:48.197523
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    output = """
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
# 127.0.0.53 is the systemd-resolved stub resolver.
# run "systemd-resolve --status" to see details about the actual nameservers.

nameserver 8.8.8.8
nameserver 8.8.4.4
domain localdomain
search localdomain
options debug
    """

# Generated at 2022-06-13 02:58:51.142830
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    print(dns_fact_collector.name)
    dns_fact_collector.collect()

# Generated at 2022-06-13 02:58:55.015632
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()
    assert isinstance(dns_fact_collector, BaseFactCollector)



# Generated at 2022-06-13 02:59:01.414391
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_registry
    # Because ansible runtime make a deepcopy of collector_registry,
    # we need to use the same id to get output of the following code
    # in the testing code.
    collector_id = 'dns'
    dns_fact_collector = DnsFactCollector()
    collected_facts = {}
    # The output of dns_fact_collector.collect is equal to
    # 'collected_facts' after the following code.
    dns_fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts[collector_id] == dns_fact_collector.collect()

# Generated at 2022-06-13 02:59:03.942961
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    result = DnsFactCollector().collect()
    assert isinstance(result, dict)
    assert 'dns' in result
    assert isinstance(result['dns'], dict)

    # from resolv.conf on system I'm using to write this test
    assert result['dns']['search'] == ['example.com', 'other.example.com']

# Generated at 2022-06-13 02:59:06.273640
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    print('dns_fact_collector = %s' % dns_fact_collector)


# Generated at 2022-06-13 02:59:11.948966
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    #Prepare test data
    nameservers = ['4.4.4.4','8.8.8.8','1.1.1.1','9.9.9.9','2.2.2.2','8.8.4.4','1.1.1.1']
    domain = 'test.com'
    search = ['test.com','test.org']
    sortlist = ['10.0.1.1/255.255.255.0', '10.0.2.2/255.0.0.0']
    options = {'ndots':3, 'timeout':5}


# Generated at 2022-06-13 02:59:20.563021
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    import os
    if not os.path.exists('/etc/resolv.conf'):
        os.symlink('/var/run/resolvconf/resolv.conf', '/etc/resolv.conf')

    import ansible.module_utils.facts.collectors.dns as dns_collector
    dns_collector.get_file_content = get_file_content
    dns_collector.get_file_content = lambda x, y: "search foo.com bar.com\nnameserver 8.8.8.8\nnameserver 1.1.1.1"
    dns_collector.BaseFactCollector = BaseFactCollector
    dns_fact_collector = dns_collector.DnsFactCollector()

    facts_dict = dict()
    facts