

# Generated at 2022-06-13 02:51:23.825604
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create test object
    dns = DnsFactCollector()
    # Get fact
    dns_fact = dns.collect()
    # Check if we have the DNS info in the fact
    assert 'dns' in dns_fact
    # Check if we have the nameserver in the fact
    assert 'nameservers' in dns_fact['dns']

# Generated at 2022-06-13 02:51:26.430030
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfact = DnsFactCollector()
    assert dnsfact.name == 'dns'
    assert dnsfact._fact_ids == set()


# Generated at 2022-06-13 02:51:37.207302
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import DnsFactCollector
    from ansible.module_utils.facts.collector import get_file_content
    from ansible.module_utils.facts.utils import get_file_content
    import mock
    import os

    with mock.patch('ansible.module_utils.facts.utils.get_file_content') as mock_get_file_content:
        if os.path.exists('/etc/resolv.conf'):
            mock_get_file_content.return_value = get_file_content('/etc/resolv.conf')
        else:
            mock_get_file_content.return_value = ''

        dns_facts = DnsFactCollector().collect()

# Generated at 2022-06-13 02:51:39.046734
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert isinstance(dns_facts,BaseFactCollector)

# Generated at 2022-06-13 02:51:48.061476
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fc = DnsFactCollector()
    facts = fc.collect()
    assert 'dns' in facts
    assert 'nameservers' in facts['dns']
    assert type(facts['dns']['nameservers']) == list
    assert 'domain' in facts['dns']
    assert type(facts['dns']['domain']) == unicode
    assert 'search' in facts['dns']
    assert type(facts['dns']['search']) == list
    assert 'sortlist' in facts['dns']
    assert type(facts['dns']['sortlist']) == list
    assert 'options' in facts['dns']
    assert 'timeout:30' in facts['dns']['options']

# Generated at 2022-06-13 02:51:49.829771
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fact_collection = DnsFactCollector()
    assert fact_collection.name == 'dns'
    assert fact_collection._fact_ids == set()


# Generated at 2022-06-13 02:51:52.189975
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fc = DnsFactCollector()

    # Test if returned result is non-empty and right-type
    assert (
        isinstance(
            dns_fc.collect(
                module=None,
                collected_facts={}
            ),
            dict
        )
    )

# Generated at 2022-06-13 02:51:53.916800
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()
    assert isinstance(DnsFactCollector._fact_ids, set)


# Generated at 2022-06-13 02:51:58.507045
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Unit test for method collect of class DnsFactCollector
    """
    collector = DnsFactCollector()
    results = collector.collect()
    assert 'dns' in results
    assert 'nameservers' in results['dns']
    assert results['dns']['nameservers'][0] == '8.8.8.8'
    assert 'domain' in results['dns']
    assert results['dns']['domain'] == 'maas'
    assert 'search' in results['dns']
    assert len(results['dns']['search']) == 1
    assert results['dns']['search'][0] == 'maas'
    assert 'options' in results['dns']
    assert 'rotate' in results['dns']['options']

# Generated at 2022-06-13 02:52:01.352780
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()
    assert DnsFactCollector.collect.__name__ == 'collect'

# Generated at 2022-06-13 02:52:14.148876
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dnsfact_collector = DnsFactCollector()
    # when
    dns_facts = dnsfact_collector.collect()
    # then
    assert dns_facts['dns']
    assert dns_facts['dns']['nameservers']
    assert len(dns_facts['dns']['nameservers']) > 0

# Generated at 2022-06-13 02:52:14.772826
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 02:52:19.885463
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import collector
    import os
    import shutil
    content = 'search sample.com\nnameserver 1.2.3.4\nnameserver 5.6.7.8\n'
    collector.FactsCache._instance = None
    path = collector.FactsCache.cache_dir+'/example_dir'
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + '/resolv.conf'
    file = open(path, 'w')
    file.write(content)
    file.close()
    dns_facts_collector = DnsFactCollector()
    dns_facts = dns_facts_collector.collect()

# Generated at 2022-06-13 02:52:29.700675
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    ini = "nameserver 0.0.0.0\n" \
          "domain testdomain.com\n" \
          "search x.testdomain.com y.testdomain.com\n" \
          "sortlist 10.0.0.0/8\n" \
          "options timeout:50 attempts:1\n"
    content = get_file_content('/etc/resolv.conf', ini)

    # Check parsing of resolv.conf file
    dns_facts = DnsFactCollector()
    assert content == ini
    assert dns_facts.collect(collected_facts={})
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()

# Generated at 2022-06-13 02:52:33.610099
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    x = DnsFactCollector()
    assert x.name == 'dns'
    assert set(x._fact_ids) == set()


# Generated at 2022-06-13 02:52:41.501745
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFactCollector = DnsFactCollector('dns', None)

    assert dnsFactCollector is not None
    assert dnsFactCollector.name == 'dns'
    assert dnsFactCollector.collect() == {'dns': {}}

    dns_facts = dnsFactCollector.collect(None, {'dns': 'foo1'})
    assert dns_facts == {'dns': 'foo1'}

    dns_facts = dnsFactCollector.collect(None, {'dns': {'foo': 'bar'}})
    assert dns_facts == {'dns': {'foo': 'bar'}}

# Generated at 2022-06-13 02:52:51.348010
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    lines = []
    lines.append('')
    lines.append('# Comment 1')
    lines.append('nameserver ns1')
    lines.append('nameserver ns2')
    lines.append('domain example.com')
    lines.append('search foo bar')
    lines.append('sortlist 10.0.0.0/8')
    lines.append('options ndots:3')
    lines.append('options timeout:2')
    lines.append('options debug')
    lines.append('options attempt:2')
    lines.append('# Comment 2')
    lines.append('nameserver ns3')
    lines = '\n'.join(lines)
    with open('test_file', 'w') as f:
        f.write(lines)

    dns_collector = DnsFactCollector()
   

# Generated at 2022-06-13 02:53:01.584611
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    """
       Unit test: Test method collect of class DnsFactCollector without argument
       with read/write/execute permissions for all users on the file.

       Test case:
       Prints the nameserver and search, when /etc/resolv.conf contains nameserver and search.

    """
    lines = ['# Generated by resolvconf', 'nameserver 8.8.8.8', 'nameserver 4.4.4.4', 'search example.com']

    # Expected result
    exp_result = {'dns': {'nameservers': ['8.8.8.8', '4.4.4.4'], 'search': ['example.com']}}

    # Create instance of class DnsFactCollector
    dns = DnsFactCollector()

    # Call collect method
    result = dns.collect()

# Generated at 2022-06-13 02:53:04.592362
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    # create facts
    dns_facts = DnsFactCollector()
    # then we assert that the dns_facts is not empty
    assert dns_facts

# Generated at 2022-06-13 02:53:05.547151
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector().name == "dns"

# Generated at 2022-06-13 02:53:13.760848
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 02:53:15.873272
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    try:
        dns = DnsFactCollector()
    except Exception:
        assert 0, 'Error construct DnsFactCollector'


# Generated at 2022-06-13 02:53:16.996151
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    my_f = DnsFactCollector()
    print(my_f)

# Generated at 2022-06-13 02:53:17.523835
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:53:19.252817
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts_collector = DnsFactCollector()
    assert dns_facts_collector.name == 'dns'

# Generated at 2022-06-13 02:53:26.383894
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dnsFactCollector = DnsFactCollector()


# Generated at 2022-06-13 02:53:31.221712
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
  dns_facts = DnsFactCollector()
  dns_facts_collect = dns_facts.collect(module=None, collected_facts=None)
  assert dns_facts_collect
  assert dns_facts_collect['dns']
  assert dns_facts_collect['dns']['domain']

# Generated at 2022-06-13 02:53:33.016160
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()




# Generated at 2022-06-13 02:53:37.866932
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()
    result = fact_collector.collect()
    assert result['dns']
    assert 'nameservers' in result['dns']
    assert 'domain' in result['dns']
    assert 'search' in result['dns']
    assert 'options' in result['dns']

# Generated at 2022-06-13 02:53:42.740469
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_obj = DnsFactCollector()

    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import Collector

    #
    # ansible.module_utils.basic.AnsibleModule
    #
    test_module = None
    test_module = basic.AnsibleModule(
        argument_spec = dict(),
    )
    assert test_module is not None

    #
    # ansible.module_utils.facts.collector.Collector
    #
    test_collector = None
    test_collector = Collector()
    assert test_collector is not None

    assert hasattr(test_obj, 'collect')
    assert callable(test_obj.collect)
    result = test_obj.collect(test_module, test_collector)
    assert isinstance

# Generated at 2022-06-13 02:53:55.067310
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    print('Running test_DnsFactCollector')
    # Create a class object and check if the object is instance of BaseFactCollector
    dns_fact_collector = DnsFactCollector()
    assert isinstance(dns_fact_collector, BaseFactCollector)

    return


# Generated at 2022-06-13 02:53:57.259602
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFactCollector = DnsFactCollector()
    assert dnsFactCollector.name == 'dns'

# Generated at 2022-06-13 02:53:58.841763
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'

# Generated at 2022-06-13 02:54:00.218533
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 02:54:03.576963
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
	assert DnsFactCollector.name == 'dns'
	assert DnsFactCollector._fact_ids == set()
	x = DnsFactCollector()
	assert x.name == 'dns'
	assert x._fact_ids == set()


# Generated at 2022-06-13 02:54:09.010300
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    facts = dns_fact_collector.collect()
    assert facts['dns'] == {'nameservers': ['192.168.1.254'], 'domain': 'local.domain',
                            'search': ['local.domain'], 'sortlist': [],
                            'options': {'rotate': True, 'timeout': '2'}}

# Generated at 2022-06-13 02:54:14.286603
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fc = DnsFactCollector()
    facts = fc.collect()
    facts_dns = facts.get( 'dns' )

    assert facts_dns is not None
    assert facts_dns.get( 'nameservers' ) is not None
    assert facts_dns.get( 'domain' ) is not None
    assert facts_dns.get( 'search' ) is not None
    assert facts_dns.get( 'sortlist' ) is not None
    assert facts_dns.get( 'options' ) is not None

# vim: set expandtab:

# Generated at 2022-06-13 02:54:17.499164
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()



# Generated at 2022-06-13 02:54:19.468486
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    assert isinstance(collector, DnsFactCollector)
    assert 'dns' in collector.collect()

# Generated at 2022-06-13 02:54:28.660891
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    facts = {}

# Generated at 2022-06-13 02:54:48.495387
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import _get_collectors_names_from_directory
    from ansible.module_utils.facts.collector import get_collector_classes
    for klass in get_collector_classes("dns"):
        assert (klass.name == "dns")

# Generated at 2022-06-13 02:54:52.495434
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    dns_facts = FactCollector('dns')

    # Error case
    invalid_params = {u'resolv_conf': u'/fi/le/does/not/exist'}
    dns_facts.collect(invalid_params)
    assert dns_facts.collect() == {}

# Generated at 2022-06-13 02:54:53.055419
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 02:54:54.732432
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    foo = DnsFactCollector()
    assert foo.name == 'dns'
    assert foo._fact_ids == set()

# Generated at 2022-06-13 02:54:56.777553
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfc = DnsFactCollector()
    assert dnsfc.name == 'dns'
    assert dnsfc.collect().keys() == ['dns']

# Generated at 2022-06-13 02:54:59.225769
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fc = DnsFactCollector()
    assert isinstance(dns_fc, DnsFactCollector)
    assert dns_fc.name == 'dns'
    assert dns_fc._fact_ids == set()


# Generated at 2022-06-13 02:55:03.286107
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == "dns"
    assert DnsFactCollector._fact_ids == set()
    assert DnsFactCollector.collect() == {'dns': {'domain': 'cloud.lab', 'search': ['cloud.lab'], 'nameservers': ['192.168.122.11'], 'options': {'rotate': True, 'timeout': '2'}, 'sortlist': []}}

# Generated at 2022-06-13 02:55:04.871969
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fc = DnsFactCollector()
    assert dns_fc.name == 'dns'
    assert dns_fc._fact_ids == set()
    assert dns_fc.collect() == {}

# Generated at 2022-06-13 02:55:06.053725
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    my_test_obj = DnsFactCollector()
    print(my_test_obj.collect())


# Generated at 2022-06-13 02:55:06.766272
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    my_test = DnsFactCollector()
    assert my_test.collect()

# Generated at 2022-06-13 02:55:53.220688
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_file_content
    DnsFactCollector_test = get_collector_instance(DnsFactCollector, get_file_content, 'test_DnsFactCollector_collect')
    dns_facts = DnsFactCollector_test.collect()
    assert(dns_facts['dns']['nameservers'][0] == "192.168.1.1")
    assert(dns_facts['dns']['domain'] == "test_domain.com")
    assert(dns_facts['dns']['search'][0] == "test_search.com")

# Generated at 2022-06-13 02:55:57.398178
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector != None
    assert dns_fact_collector.collect() != None


# Generated at 2022-06-13 02:56:02.190812
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    content = dedent('''
    # Generated by NetworkManager
    nameserver 127.0.0.1
    ''')
    data = dns_fact_collector._parse_fact_data(content)
    assert data['dns'] == {
        'nameservers': ['127.0.0.1'],
    }

# Generated at 2022-06-13 02:56:05.670603
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector(None)
    test_facts = dfc.collect()
    assert('dns' in test_facts)
    assert('nameservers' in test_facts['dns'])
    assert('domain' in test_facts['dns'])
    assert('search' in test_facts['dns'])
    assert('sortlist' in test_facts['dns'])
    assert('options' in test_facts['dns'])


# Generated at 2022-06-13 02:56:07.680444
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:56:17.324298
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_lines = """
# search testdomain.com sub.testdomain.com
search testdomain.com sub.testdomain.com
domain testdomain.com
nameserver 192.168.2.2
nameserver 192.168.2.3
nameserver 192.168.2.4
domain othertestdomain.com
nameserver 192.168.2.5
nameserver 192.168.2.6
    """

    coll = DnsFactCollector()
    ret = coll.collect(get_file_content=lambda x, y: test_lines)

    assert ret['dns']['search'] == ['testdomain.com', 'sub.testdomain.com']

# Generated at 2022-06-13 02:56:20.831911
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert str(DnsFactCollector) == "<class 'ansible_collections.ansible.community.plugins.module_utils.facts.dns.DnsFactCollector'>"

# Generated at 2022-06-13 02:56:22.399312
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert isinstance(DnsFactCollector(None, None), DnsFactCollector)


# Generated at 2022-06-13 02:56:24.182713
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:56:26.542777
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()
    assert isinstance(DnsFactCollector._fact_ids, set)

# Generated at 2022-06-13 02:57:54.131119
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fact_collector = DnsFactCollector()
    assert fact_collector.name == 'dns'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:57:57.579694
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectedFacts

    collector = DnsFactCollector()
    facts = CollectedFacts(None)
    module_mock = MagicMock(params=dict(gather_subset='dns'))
    result = collector.collect(module=module_mock, collected_facts=facts)

    assert result

    # TODO: assert proper subset of result

# Generated at 2022-06-13 02:58:02.046978
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    '''Test DnsFactCollector.collect'''

    from ansible.module_utils.facts.collector import Collector, \
        DictFactCache
    
    from .collector_test_helper import get_collector_instance, \
        get_test_data_file_path, read_test_data_from_file
    
    new_instance = get_collector_instance(DnsFactCollector)
    assert isinstance(new_instance, DnsFactCollector)
    assert isinstance(new_instance, Collector)

    expected_dict = read_test_data_from_file(
        get_test_data_file_path('dns.json')
    )
    assert isinstance(expected_dict, dict)
    # print('EXPECTED: {}'.format(expected_dict))

    fact_cache

# Generated at 2022-06-13 02:58:04.801123
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_collected_facts = {}
    setattr(dns_collected_facts, 'dns',{"nameservers":["10.0.2.3"],"domain":"example.org"})
    assert isinstance(dns_collected_facts,dict)


# Generated at 2022-06-13 02:58:05.813107
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fact_collector = DnsFactCollector()
    assert fact_collector is not None

# Generated at 2022-06-13 02:58:06.299059
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:58:12.065159
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_test_dict = { 'nameservers': ['8.8.8.8', '192.168.1.1'],
                      'domain': 'example.com',
                      'search': ['example.com', 'foobar.com'],
                      'sortlist': [],
                      'options': {'timeout': '2'}
                    }

    class MockCollectorModule:
        def get_file_content(file_name, default=None):
            return '''nameserver 8.8.8.8
nameserver 192.168.1.1
domain example.com
search example.com foobar.com
options timeout:2'''

    def test_collect_dns_facts(self, module):
        return dns_test_dict

    dns_fact_collector = DnsFactCollector()
    dns

# Generated at 2022-06-13 02:58:19.116848
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os
    import sys
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.dns import DnsFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    def mock_env_variables(env_var, osname):
        if env_var == 'PATH':
            if osname == 'Linux':
                return '/sbin:/usr/sbin:/bin:/usr/bin'
            elif osname == 'OpenBSD':
                return '/usr/bin:/bin'
            elif osname == 'FreeBSD':
                return '/sbin:/bin'
        return None
    def mock_os_name(osname):
        return osname

# Generated at 2022-06-13 02:58:27.076357
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    # If file /etc/resolv.conf doesn't exists return empty dictionary
    def fake_get_file_content_empty():
        return ""
    get_file_content.side_effect = fake_get_file_content_empty

    dns_fact_collector = DnsFactCollector()
    res_empty_dict = dns_fact_collector.collect()
    assert res_empty_dict == {}

    # If file /etc/resolv.conf exists return dictionary with results
    def fake_get_file_content_exists():
        return """search dns.tld \nnameserver 10.0.0.1 \noption timeout:1 \n"""
    get_file_content.side_effect = fake_get_file_content_exists

    res_dict = dns_fact_collector.collect

# Generated at 2022-06-13 02:58:28.723250
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    # TODO
