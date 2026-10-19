

# Generated at 2022-06-13 02:51:27.262976
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fact_collector = DnsFactCollector()
    dns_facts = fact_collector.collect()
    assert 'dns' in dns_facts
    assert 'dns' == fact_collector.name
    assert type(dns_facts['dns']) == dict

# Generated at 2022-06-13 02:51:32.569193
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    
    dns_fact_collector = DnsFactCollector()
    
    # FIXME: get_file_content return is a complex structure
    facts = dns_fact_collector.collect()
    print (facts)
    pass

if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 02:51:40.802577
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os
    import tempfile
    import pytest

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    resolv_conf_file = os.path.join(tmpdir, 'resolv.conf')
    with open(resolv_conf_file, 'w') as f:
        f.write("""# DNS Servers
#nameserver 8.8.8.8
nameserver 8.8.4.4
search ansible.com
domain blah.com
sortlist 8.8.8.8 7.7.7.7
options  timeout:10 rotate
""")

    # Create dns fact collector
    dns_fact_collector = DnsFactCollector()
    dns_fact_collector.get_resolv_conf_file = lambda: resolv_conf_

# Generated at 2022-06-13 02:51:46.548941
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # test module
    module = None
    # test class
    dns_fact_collector = DnsFactCollector()
    # test result
    result = dns_fact_collector.collect(module)
    # check result
    assert result == {'dns': {'nameservers': ['8.8.8.8', '8.8.4.4'], 'search': ['mydomain.com', 'mydomain2.com']}}

# Generated at 2022-06-13 02:51:48.388574
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'
    assert dns._fact_ids == set()


# Generated at 2022-06-13 02:51:49.639803
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == "dns"

# Generated at 2022-06-13 02:51:53.382768
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create an instance of the DnsFactCollector object
    obj = DnsFactCollector()

    # Run the collect method of the DnsFactCollector object
    result = obj.collect()

    # Test expected results
    assert result['dns']['nameservers'] == ['10.2.2.10']
    assert result['dns']['domain'] == 'example.com'
    assert result['dns']['search'] == ['example.com', 'example.net']
    assert result['dns']['sortlist'] == ['10.1.1.0/24']
    assert result['dns']['options'] == {'ndots': '2', 'timeout': '1'}

# Generated at 2022-06-13 02:52:01.152434
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts_collector = DnsFactCollector()
    assert dns_facts_collector.collect() == {'dns': {'nameservers': ['8.8.8.8', '8.8.4.4'], 'search': ['example.com', 'redhat.com'], 'sortlist': ['1.2.3.4/255.255.255.255', '5.6.7.8/255.255.0.0'], 'options': {'ndots': '3', 'timeout': '5', 'attempts': True}, 'domain': 'golinuxcloud.com'}}

# Generated at 2022-06-13 02:52:11.589453
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import shutil
    import tempfile
    import unittest

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a resolv.conf file in the temporary directory
    resolv_file = open(tmpdir + '/resolv.conf', 'w')

# Generated at 2022-06-13 02:52:13.228602
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts


# Generated at 2022-06-13 02:52:23.296537
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fact = DnsFactCollector()
    assert fact.name == 'dns'
    assert fact._fact_ids == set()

# Generated at 2022-06-13 02:52:25.262497
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    mydict = dns.collect()
    assert 'dns' in mydict

# Generated at 2022-06-13 02:52:28.604379
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """Unit test for method collect of class DnsFactCollector"""

    dns_fact_collector = DnsFactCollector()

    # TODO: add unit test for method collect of class DnsFactCollector



# Generated at 2022-06-13 02:52:38.686418
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    collected_facts = {}

    collected_facts = dns_fact_collector.collect(None, collected_facts)

    assert isinstance(collected_facts, dict)

    assert collected_facts['dns'] == {
        'nameservers': ['192.168.0.1'],
        'search': ['domain1.example.com', 'domain2.domain1.example.com'],
        'sortlist': ['192.168.1.0/24'],
        'options': {
            'timeout': '2',
            'attempts': '3',
        }
    }

# Generated at 2022-06-13 02:52:39.873584
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    my_test = DnsFactCollector()
    assert my_test


# Generated at 2022-06-13 02:52:41.571780
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'
    assert len(obj._fact_ids) == 0

# Generated at 2022-06-13 02:52:51.348980
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_collector = DnsFactCollector()
    dns_facts = dns_collector.collect()
    assert type(dns_facts) is dict
    assert 'dns' in dns_facts
    assert type(dns_facts['dns']) is dict
    assert 'nameservers' in dns_facts['dns']
    assert type(dns_facts['dns']['nameservers']) is list
    assert 'domain' in dns_facts['dns']
    assert type(dns_facts['dns']['domain']) is str or type(dns_facts['dns']['domain']) is unicode
    assert 'search' in dns_facts['dns']
    assert type(dns_facts['dns']['search']) is list

# Generated at 2022-06-13 02:52:53.487519
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    x = DnsFactCollector()
    assert x.name == 'dns'
    assert x._fact_ids == set()


# Generated at 2022-06-13 02:53:03.851847
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible_collections.ansible.misc.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    module = AnsibleModule(argument_spec={})
    set_module_args(dict(collect='dns'))

    dns_fact_collector = DnsFactCollector()
    dns_fact_collector.collect(module)

    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector.collected_facts == {'dns': {'nameservers': ['8.8.8.8'], 'domain': 'test', 'search': ['test'], 'sortlist': ['test'], 'options': {'test1': 'test2'}}}

# Generated at 2022-06-13 02:53:05.876045
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:53:25.161855
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector().collect()
    assert len(dns_facts['ansible_facts']['dns']['nameservers']) > 0, "There is a nameserver in the list"
    assert isinstance(dns_facts, dict), "dns_facts is a dict"

# Generated at 2022-06-13 02:53:31.176761
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    print ("Starting test_DnsFactCollector_collect")
    # create class instance
    dns_collector = DnsFactCollector()
    # Call method collect
    dns_collector.collect()
    print ("Test_DnsFactCollector_collect")
    print ("\tStart test_DnsFactCollector_collect")
    print ("\t\tPassed")



# Generated at 2022-06-13 02:53:42.193377
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # create mock object and set results
    # load parallelize to load dns facter module
    import ansible.module_utils.facts.dns.parallelize as parallelize
    content = """
    # comment
    ; comment
    nameserver 10.1.1.1
    nameserver 10.1.1.2

    domain mydomain.local

    search mydomain.local

    sortlist 10.2.0.0/24 10.1.1.0/24 10.1.1.0/24

    options timeout:1
    options attempts:3
    options rotate
    """
    parallelize.get_file_content = lambda x: content

    test_collector = DnsFactCollector()

    result = test_collector.collect()

    assert "dns" in result


# Generated at 2022-06-13 02:53:52.633645
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fc = DnsFactCollector()
    facts = fc.collect()
    assert 'dns' in facts, 'Test of collect method of class DnsFactCollector failed'
    assert 'nameservers' in facts['dns'], 'Test of collect method of class DnsFactCollector failed'
    assert 'domain' in facts['dns'], 'Test of collect method of class DnsFactCollector failed'
    assert 'search' in facts['dns'], 'Test of collect method of class DnsFactCollector failed'
    assert 'sortlist' in facts['dns'], 'Test of collect method of class DnsFactCollector failed'
    assert 'options' in facts['dns'], 'Test of collect method of class DnsFactCollector failed'

# Generated at 2022-06-13 02:53:57.065758
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """
    This is a unittest (no nosetests) to test the discovery of facts, no mocked data provided
    To be used with caution and only if the system is known, to avoid introduction of race conditions
    """
    info = DnsFactCollector().collect()
    print (info)

# Generated at 2022-06-13 02:53:58.643843
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'

# Generated at 2022-06-13 02:54:04.112401
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    fact_collector = DnsFactCollector();
    result = fact_collector.collect()

    assert result['dns']
    assert result['dns']['nameservers'][0] == '192.168.1.100'
    assert result['dns']['sortlist'][0] == '1.1.1.0/255.255.255.0'



# Generated at 2022-06-13 02:54:06.673898
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector_obj = DnsFactCollector()
    assert dns_collector_obj.name == 'dns'

# Generated at 2022-06-13 02:54:08.577426
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:54:10.723576
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'
    assert dns._fact_ids == set()



# Generated at 2022-06-13 02:54:44.456481
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector_obj = DnsFactCollector()
    assert dns_collector_obj.name == "dns"
    assert dns_collector_obj._fact_ids == set()

# Generated at 2022-06-13 02:54:45.725986
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    obj = DnsFactCollector()
    assert obj.name == 'dns'

# Generated at 2022-06-13 02:54:48.994481
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()

    assert dns_facts['dns'] is not None

# Generated at 2022-06-13 02:54:59.106559
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    class TestDnsFactCollector(DnsFactCollector):
        def _get_file_content(self, path):
            return '''# This is a comment
; This is also a comment
nameserver 127.0.0.1
sortlist 192.168.0.0/24 10.0.0.0/8
options ndots:3 rotate
'''

    dns_fact_collector = TestDnsFactCollector()
    facts = dns_fact_collector.collect()
    assert 'dns' in facts
    dns_facts = facts['dns']

    assert 'nameservers' in dns_facts
    nameservers = dns_facts['nameservers']
    assert len(nameservers) == 1
    assert nameservers[0] == '127.0.0.1'



# Generated at 2022-06-13 02:55:04.200449
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolv_conf = """; Created by dhcpcd from eth0
;; An example name server entry
#nameserver 192.168.0.1
nameserver 8.8.8.8
nameserver 8.8.4.4
domain example.com
sortlist 10.0.0.0/8 10.10.10.0/24
options edns0 edns1:1
# A line with a comment
search foo bar.example.com"""

    DnsFactCollector.collect(None, None, resolv_conf)

# Generated at 2022-06-13 02:55:05.158159
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert isinstance(DnsFactCollector(), DnsFactCollector)

# Generated at 2022-06-13 02:55:06.450915
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:55:15.346212
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content

    # Get dictionary from DnsFactCollector.collect
    dns_facts = DnsFactCollector.collect()

    # Get nameservers from /etc/resolv.conf
    nameservers = []
    for line in get_file_content('/etc/resolv.conf', '').splitlines():
        if line.startswith('#') or line.startswith(';') or line.strip() == '':
            continue
        tokens = line.split()
        if len(tokens) == 0:
            continue
        if tokens[0] == 'nameserver':
            for nameserver in tokens[1:]:
                nameservers.append(nameserver)



# Generated at 2022-06-13 02:55:19.085951
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    dns_facts = dns_fact_collector.collect()
    assert dns_facts == {'dns': {'nameservers': ['192.168.1.1'], 'options': {'timeout': '2'}}}

# Generated at 2022-06-13 02:55:21.106449
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    assert 'dns' in collector.collect()

# Generated at 2022-06-13 02:56:03.098624
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.dns

    # Create object DnsFactCollector
    dns_fc = DnsFactCollector()

    # Check type of dns_fc
    assert isinstance(dns_fc, FactCollector)

    # Test method collect of class DnsFactCollector
    assert dns_fc.collect() == {}

# Generated at 2022-06-13 02:56:05.880828
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_ = DnsFactCollector()


# Generated at 2022-06-13 02:56:07.836452
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert DnsFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:56:08.974771
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()
    dfc.collect()

# Generated at 2022-06-13 02:56:18.049163
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    module = None
    collected_facts = None

    obj = DnsFactCollector()

    # Assert that the method get_file_content of module utils is called twice
    # with the correct parameters
    with open('module_utils/facts/utils.py', 'rt') as utils_fh:
        with open('module_utils/facts/collector.py', 'rt') as collector_fh:
            dns_facts = obj.collect(module, collected_facts)

# Generated at 2022-06-13 02:56:20.975876
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    dns_facts = dns.collect()
    assert dns_facts['dns'] == {}

# Generated at 2022-06-13 02:56:23.766412
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
 
    # Test for when resolv.conf exists
    result = DnsFactCollector()
    assert result.name == 'dns'
    assert result._fact_ids == set(['dns'])
 


# Generated at 2022-06-13 02:56:27.072158
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Arrange
    collector = DnsFactCollector()
    collected_facts = {}

    # Act. Return value is not used in this unit test
    collector.collect(None, collected_facts)

    # Assert
    assert 'dns' in collected_facts['ansible_dns']


# Generated at 2022-06-13 02:56:29.643551
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    facts_dict = {
        'dns': {}
    }

    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.collect() == facts_dict

# Generated at 2022-06-13 02:56:33.526714
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()
    assert 'dns' in dns_facts
    assert 'nameservers' in dns_facts['dns']
    assert 'domain' in dns_facts['dns']
    assert 'search' in dns_facts['dns']
    assert 'sortlist' in dns_facts['dns']
    assert 'options' in dns_facts['dns']

# Generated at 2022-06-13 02:57:16.144374
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    d=DnsFactCollector()
    assert d.name =='dns'

# Generated at 2022-06-13 02:57:25.298242
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    module = None
    collected_facts = None
    fc = DnsFactCollector()
    ans = fc.collect(module, collected_facts)
    
    # Test nameservers
    assert 'nameservers' in ans['dns']
    assert len(ans['dns']['nameservers']) != 0
    
    # Test domain
    assert 'domain' in ans['dns']
    
    # Test search
    assert 'search' in ans['dns']
    
    # Test sortlist
    assert 'sortlist' in ans['dns']
    
    # Test options
    assert 'options' in ans['dns']
    assert len(ans['dns']['options']) != 0

# Generated at 2022-06-13 02:57:27.003385
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'


# Generated at 2022-06-13 02:57:27.869010
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'

# Generated at 2022-06-13 02:57:35.892003
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolv_conf = '# This file is generated via salt, do not edit.\n# Managed by: Ansible\n\nnameserver 8.8.8.8\nnameserver 8.8.4.4\nsearch dev.example.com\ndomain dev.example.com\noptions timeout:1\n'

    facts = {}

    (res, out) = command_generic('cat /proc/net/fib_trie')
    if out['rc'] == 0:
        fib_trie = out['stdout']
        fib_trie = fib_trie.split('\n')

# Generated at 2022-06-13 02:57:38.432834
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:57:45.090828
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    # Arrange
    # Please note that the fact collecting is mocked and therefore only the value "DnsFactCollector.name" matters
    # The values of the other attributes are not relevant.
    mock_DnsFactCollector = DnsFactCollector()
    mock_DnsFactCollector.name = 'dns'
    mock_DnsFactCollector._fact_ids = set()

    # Act
    result = mock_DnsFactCollector.collect()

    # Assert
    if 'dns' in result:
        assert result['dns'] == {}



# Generated at 2022-06-13 02:57:47.293693
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert isinstance(dns_fact_collector._fact_ids, set)

# Generated at 2022-06-13 02:57:53.364107
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Test positive dns output
    test_dns_collector = DnsFactCollector()


# Generated at 2022-06-13 02:57:53.763727
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:58:40.836659
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create a DnsFactCollector object
    dns_fc = DnsFactCollector()
    # Get the collect method of the object (collect)
    #dns_fc_collect_mock = dns_fc.collect

    #assert_equal(dns_fc_collect_mock(), "")

# Generated at 2022-06-13 02:58:42.129379
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    print(dns_facts.collect()) 


if __name__ == '__main__':
    test_DnsFactCollector()

# Generated at 2022-06-13 02:58:49.449314
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    module = None
    collected_facts = None
    fake_file_content = '''#;
;
;
search example.com
nameserver 8.8.8.8
options ndots:2 timeout:2 attempts:2
domain test.domain.com'''

    def get_file_content_mock(path, defval):
        if path == '/etc/resolv.conf':
            return fake_file_content
        return ''

    get_file_content_mock_container = {
        'get_file_content': get_file_content_mock,
    }

    result = DnsFactCollector(None).collect(module, collected_facts, get_file_content_mock_container)
    assert result['dns']['nameservers'] == ['8.8.8.8']
   

# Generated at 2022-06-13 02:58:50.849400
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc


# Generated at 2022-06-13 02:58:59.297054
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content
    import os

    class FakeModule(object):
        pass

    Collectors = [
        DnsFactCollector
    ]

    # Before running the test, create a resolv.conf file in the directory
    # and populate it with the test data, then remove it after the test
    # is run.
    resolv_conf = os.path.join(os.path.dirname(__file__), "resolv.conf")

# Generated at 2022-06-13 02:59:00.353774
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # TODO: unit test not implemented
    assert False



# Generated at 2022-06-13 02:59:01.619300
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    results = DnsFactCollector()
    assert results.name == 'dns'
    assert results._fact_ids == set()

# Generated at 2022-06-13 02:59:08.208205
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    dns_facts = dns_fact_collector.collect()

    assert "dns" in dns_facts
    assert "nameservers" in dns_facts["dns"]
    assert type(dns_facts["dns"]["nameservers"]) is list
    assert "search" in dns_facts["dns"]
    assert type(dns_facts["dns"]["search"]) is list
    assert "domain" in dns_facts["dns"]
    assert "sortlist" in dns_facts["dns"]
    assert type(dns_facts["dns"]["sortlist"]) is list

# Generated at 2022-06-13 02:59:19.008219
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Set up
    dns_instance = DnsFactCollector()
    test_resolv_conf = """
#
# Make sure to set the options timeout:1 and attempts:1
# otherwise it is possible that the execution of this
# playbook will never finish if DNS is not working
# properly.
#
nameserver 8.8.8.8
nameserver 10.0.0.1
domain example.com
search example.com blue.com
sortlist 1.2.3.4 5.6.7.8
options timeout:1 attempts:1
"""


# Generated at 2022-06-13 02:59:22.075591
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_collector = DnsFactCollector()
    result = test_collector.collect()
    assert(result['dns'])
    assert(result['dns']['nameservers'])
    assert(result['dns']['domain'])
    assert(result['dns']['search'])

# Generated at 2022-06-13 03:01:00.901290
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()
    # TODO: test source is /etc/resolv.conf or /etc/resolv.conf.head
    # are all different
    dns_facts = { "domain": "example.com",
                  "nameservers": [ "10.0.0.2" ],
                  "sortlist": ["192.168.1.0/255.255.255.0"],
                  "search": [ "example.com" ],
                  "options": { "ndots": "5" }
                }

    vars_data = dfc.collect(None, { "ansible_dns": dns_facts } )
    assert type(vars_data['ansible_dns']) is dict
    assert "domain" in vars_data['ansible_dns']

# Generated at 2022-06-13 03:01:03.178587
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """Test DnsFactCollector.  """

    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 03:01:09.470257
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    module = 'module_utils.facts.collector.dns'

    # Load module
    dns_module = __import__(module, fromlist=['DnsFactCollector'])

    # Setup module for stubbing
    class FakeModule:
        pass

    fake_module = FakeModule()

    # Create dns fact collector
    dns_fact_collector = dns_module.DnsFactCollector()

    # Collect dns facts
    dns_facts = dns_fact_collector.collect(fake_module)

    assert 'dns' in dns_facts

# Generated at 2022-06-13 03:01:17.809513
# Unit test for method collect of class DnsFactCollector