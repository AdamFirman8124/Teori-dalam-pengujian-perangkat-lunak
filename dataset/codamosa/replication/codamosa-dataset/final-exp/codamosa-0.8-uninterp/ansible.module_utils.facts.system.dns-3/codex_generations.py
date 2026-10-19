

# Generated at 2022-06-13 02:51:23.715829
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    fc = DnsFactCollector()
    assert fc.name == 'dns'
    assert fc._fact_ids == set()


# Generated at 2022-06-13 02:51:29.224382
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    my_obj = DnsFactCollector()
    assert my_obj.collect() == {'dns': {'nameservers': ['8.8.8.8', '8.8.4.4'], 'domain': None, 'search': ['dev.lab'], 'sortlist': [], 'options': {'rotate': True, 'timeout:1': True, 'attempts:2': True}}}

# Generated at 2022-06-13 02:51:32.773814
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Collecting facts should succeed
    from ansible.module_utils.facts.collector import DnsFactCollector
    dnsFactCollector = DnsFactCollector()
    result = dnsFactCollector.collect()

# Generated at 2022-06-13 02:51:36.389953
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    '''Unit test for constructor of class DnsFactCollector'''
    dns_facts = DnsFactCollector()

    assert dns_facts.name == 'dns'
    assert len(dns_facts._fact_ids) == 0

# Generated at 2022-06-13 02:51:42.776717
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # This is a way of emulating a file /etc/resolv.conf
    class FakeModule():
        def __init__(self):
            self.params = {}
        def get_bin_path(self, app, opts=None, required=False):
            if app == 'getent':
                return None, None
            elif app == 'wbinfo':
                return None
        def fail_json(self, **args):
            self.fail_json_args = args
        def exit_json(self, **args):
            self.exit_json_args = args
    fake_module = FakeModule()
    fake_module.params["gather_subset"] = ["network"]
    fake_module.params["filter"] = "dns"
    fake_module.params["get_file_content_from_module"]

# Generated at 2022-06-13 02:51:43.638731
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector()

# Generated at 2022-06-13 02:51:45.991781
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
   test_dns = DnsFactCollector()
   assert test_dns.name == 'dns'

# all following tests verify the content of the returning data structure for the collect method


# Generated at 2022-06-13 02:51:52.341128
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fake_module = {}
    fake_module.get_bin_path = lambda x: '/bin/' + x
    fake_module.get_file_content = lambda x: file(x).read()
    collector = DnsFactCollector()
    dns_facts = collector.collect(fake_module)
    assert dns_facts['dns']['nameservers'] == ['192.168.1.1', '192.168.1.2']
    assert dns_facts['dns']['domain'] == 'example.com'
    assert dns_facts['dns']['options']['timeout'] == 1
    assert dns_facts['dns']['options']['attempts'] == '2'
    assert dns_facts['dns']['options']['rotate'] is True


# Generated at 2022-06-13 02:51:52.838199
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 02:51:55.321652
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc.name == 'dns'
    assert isinstance(dfc._fact_ids, set)
    assert dfc._fact_ids == set()


# Generated at 2022-06-13 02:52:03.369266
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 02:52:06.821513
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()

    result = collector.collect()
    assert result['dns']
    assert result['dns']['nameservers']
    assert result['dns']['options']

# Generated at 2022-06-13 02:52:15.912584
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCollector

    content = """
nameserver 1.2.3.4
nameserver 5.6.7.8
nameserver 9.10.11.12
domain local
sortlist
10.1.2.0/255.255.255.0
10.3.4.0/255.255.255.0
options attempts:3 timeout:1 rotate
search foo bar
;comment
""".lstrip()

    def get_file_content(name):
        return content

    module = None
    collected_facts = Collector()
    fact_collector = FactCollector(module=module, collected_facts=collected_facts)
    fact

# Generated at 2022-06-13 02:52:26.848501
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os
    import tempfile

    # create a temporary file
    (fd, filename) = tempfile.mkstemp()

    # delete the temporary file
    os.close(fd)
    if os.path.exists(filename):
        os.remove(filename)


    # create a temporary file with content
    file_content = """# comment
nameserver 10.10.10.10
nameserver 10.10.10.11
domain mydomain.local
search mydomain.local example.com otherdomain.internal
sortlist 192.168.1.0/24
options timeout:1 attempts:2
"""
    with open(filename, 'w') as f:
        f.write(file_content)

    d = DnsFactCollector()

    # test the collect method

# Generated at 2022-06-13 02:52:29.527388
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()



# Generated at 2022-06-13 02:52:30.898858
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'

# Generated at 2022-06-13 02:52:41.640021
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Test collect function of the class DnsFactCollector.
    """
    # Create a new instance of class DnsFactCollector
    test_collector = DnsFactCollector()

    # Create mock content of file /etc/resolv.conf
    test_resolv_conf_content = '''
# This file is being maintained by Puppet.
# DO NOT EDIT
nameserver 127.0.0.1
search example.com
# search example.org
# search example.net
nameserver 8.8.8.8
options timeout:3
'''

    # Create a dictionary of test results

# Generated at 2022-06-13 02:52:44.232556
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    dns_fact_collector.collect()

# Generated at 2022-06-13 02:52:52.684986
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import (
        Collector,
    )
    from ansible.module_utils.facts.collector.dns import DnsFactCollector

    file_content = '''
#
# Mac OS X Notice
#
# This file is not  used  by  the  host name and address resolution
# or the DNS query routing mechanisms used by most processes on
# this Mac OS X system.
#
# This file is automatically generated.
#
domain example.jdauphant.net
nameserver 192.168.1.1
nameserver 192.168.1.2
options ndots:1 timeout:10
#sortlist 208.185.138.0/24 208.185.139.0/24
'''

    c = Collector()
    dfc = DnsFactCollector(c)


# Generated at 2022-06-13 02:52:57.481196
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Test with a file containing nameserver and search
    test_file_content = '''search tux.das.domain
nameserver 172.16.1.1
'''
    test_facts = DnsFactCollector().collect({}, test_file_content)
    assert 'dns' in test_facts
    dns_facts = test_facts['dns']
    assert 'domain' not in dns_facts
    assert 'nameservers' in dns_facts
    assert '172.16.1.1' in dns_facts['nameservers']
    assert 'search' in dns_facts
    assert 'tux.das.domain' in dns_facts['search']
    assert 'sortlist' not in dns_facts
    assert 'options' not in dns_facts

    # Test with a file containing

# Generated at 2022-06-13 02:53:09.521385
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # Using constructor
    collector = DnsFactCollector()
    assert collector.name == 'dns'
    assert collector._fact_ids == set()

    # Using collect()
    facts = collector.collect()['dns']
    assert len(facts) > 0

    # Check some facts
    assert 'domain' in facts
    assert 'nameservers' in facts
    assert 'search' in facts
    assert 'sortlist' in facts
    assert 'options' in facts

# Generated at 2022-06-13 02:53:11.599043
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import Collector

    collector = Collector()
    facts = collector.collect(None, None)
    assert isinstance(facts, dict)
    assert 'dns' in facts

# Generated at 2022-06-13 02:53:13.758601
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector = DnsFactCollector()

    assert dns_collector.name == 'dns'

# Generated at 2022-06-13 02:53:17.520539
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import collector
    import sys

    x = collector.get_collector_class('dns')
    m = x()
    sys.modules['ansible'] = type('FakeAnsibleModule', (object,), {})
    m.collect()

# Generated at 2022-06-13 02:53:25.044486
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Test case #1
    config = """search test.org
domain test.org
nameserver 8.8.8.8
nameserver 2001:4860:4860::8888
sortlist 192.168.1.0/24
options rotate
"""
    with open('/etc/resolv.conf', 'w') as f:
        f.write(config)

    dns_facts = DnsFactCollector()
    facts = dns_facts.collect({})

# Generated at 2022-06-13 02:53:28.293073
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
	dnsFactCollector = DnsFactCollector()
	assert dnsFactCollector.name == 'dns'
	assert dnsFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:53:33.272705
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:53:34.715039
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector('', {})


# Generated at 2022-06-13 02:53:45.716100
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.dns.collector import DnsFactCollector

    collector = Collector()
    collector.add_collector(DnsFactCollector())

    BaseFactCollector._load_cache = lambda self: None  # pylint: disable=protected-access

# Generated at 2022-06-13 02:53:49.402153
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # Arrange
    test_collector = DnsFactCollector()

    # Assert
    assert test_collector.name == 'dns'
    assert test_collector._fact_ids == set()

# Generated at 2022-06-13 02:54:06.162518
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    res = DnsFactCollector.collect()
    assert res.get('dns') is not None
    assert res.get('dns').get('nameservers') is not None



# Generated at 2022-06-13 02:54:09.397183
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector({})
    dns_facts = dns_fact_collector.collect({}, {})
    print(dns_facts)

if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 02:54:10.849629
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """Test constructor of class DnsFactCollector"""

    obj = DnsFactCollector()
    assert obj.name == 'dns'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 02:54:11.652559
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc is not None

# Generated at 2022-06-13 02:54:13.258474
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()
    assert dns_facts['ansible_dns'] == dns_facts['dns']

# Generated at 2022-06-13 02:54:23.999409
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    mock_module = 'test_module'

    test_resolv_conf = '''
nameserver 8.8.8.8
nameserver 8.8.4.4

domain google.com
search google.com
sortlist 168.100.189.0 255.255.255.0 10.1.1.0 10.1.1.255
timeout:3
rotate
attempts:3
no-check-names

domain google.com
search google.com
search google.org
sortlist 168.100.189.0 255.255.255.0 10.1.1.0 10.1.1.255
timeout:3
rotate
attempts:3
no-check-names

# comment
; another comment
domain foobar.com
nameserver 10.10.10.10
'''

    d

# Generated at 2022-06-13 02:54:24.860960
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    a = DnsFactCollector()
    assert a

# Generated at 2022-06-13 02:54:27.579865
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:54:37.611268
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import DnsFactCollector

    collected_facts = {}
    fact_collector = FactCollector(collected_facts=collected_facts,
                                   exclude_list=['*'],
                                   gather_subset=[DnsFactCollector.name])
    fact_collector.collect(module=None)
    assert collected_facts == {}

    fact_collector = FactCollector(collected_facts=collected_facts,
                                   exclude_list=[],
                                   gather_subset=[DnsFactCollector.name])
    fact_collector.collect(module=None)

    assert 'dns' in collected_facts
    assert 'nameservers' in collected_facts['dns']

# Generated at 2022-06-13 02:54:38.878669
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()

# Generated at 2022-06-13 02:55:09.683246
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    ansible_dns_facts = ["nameserver 8.8.8.8", "domain google.com"]
    res = DnsFactCollector()
    res.get_file_content = lambda x, y: '\n'.join(ansible_dns_facts)
    res_dict = res.collect()
    assert 'dns' in res_dict
    assert res_dict['dns']['nameservers'] == ['8.8.8.8']
    assert res_dict['dns']['domain'] == 'google.com'

# Generated at 2022-06-13 02:55:11.400008
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_obj = DnsFactCollector()
    assert dns_obj.name == 'dns'

    assert not dns_obj.collect()

# Generated at 2022-06-13 02:55:12.546964
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    tfact = DnsFactCollector()
    assert tfact.name == 'dns'

# Generated at 2022-06-13 02:55:14.719393
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfc = DnsFactCollector()
    assert dnsfc.name == 'dns'
    assert dnsfc._fact_ids == set()


# Generated at 2022-06-13 02:55:16.417297
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    facts = dns_fact_collector.collect()
    assert facts != None

# Generated at 2022-06-13 02:55:19.612432
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()
    assert dns_facts.collect() == {'dns': {}}

# Generated at 2022-06-13 02:55:29.335915
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts import get_collector_instance
    # Mock standard output for Collectors
    import sys
    saved_stdout = sys.stdout
    sys.stdout = open('/dev/null', 'w')

    # Collect a list of Facts from the DnsFactCollector
    collected_facts = get_collector_instance(DnsFactCollector, ModuleStub)
    # Check that the collect method of the DnsFactCollector
    # returns valid Facts
    assert isinstance(collected_facts, dict)
    assert len(collected_facts) > 0
    assert 'dns' in collected_facts.keys()
    assert isinstance(collected_facts['dns'], dict)

# Generated at 2022-06-13 02:55:32.047816
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsFacts = DnsFactCollector()
    assert dnsFacts.name == 'dns'
    assert dnsFacts._fact_ids == set()


# Generated at 2022-06-13 02:55:40.147225
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    module = None
    collected_facts = {}
    fact_collector  = DnsFactCollector()
    dns_facts       = fact_collector.collect(module, collected_facts)
    assert dns_facts == {'dns': {'domain': 'gugus.ch', 
                                 'nameservers': ['10.0.0.1'], 
                                 'options': {'edns0': True, 
                                             'timeout': '2'}, 
                                 'sortlist': [], 
                                 'search': ['gugus.ch', 
                                           'guru.ch']}}

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:55:42.639994
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    # noinspection PyTypeChecker
    assert isinstance(DnsFactCollector._fact_ids, set)
    assert DnsFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:56:55.805634
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Test 1:
    # DNS facts are not gathered on the collector side, so
    # this test should just return an empty dictionary.
    # If the module is not using it, no need to collect it.
    dns_facts = DnsFactCollector().collect()
    assert isinstance(dns_facts, dict)
    assert isinstance(dns_facts['dns'], dict)
    assert len(dns_facts['dns']) == 0



# Generated at 2022-06-13 02:57:00.153618
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts_collector = DnsFactCollector()
    dns_facts_collector.collect()
    dns_dict = dns_facts_collector.facts
    for keys,values in dns_dict.items():
        print(keys, values)


# Execute this from command line to test the method collect of class DnsFactCollector
if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 02:57:01.580200
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 02:57:03.100203
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsfact = DnsFactCollector()
    assert dnsfact.name == 'dns'
    assert dnsfact._fact_ids == set()


# Generated at 2022-06-13 02:57:04.213892
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
  DnsFactCollector()

# Generated at 2022-06-13 02:57:04.670458
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:57:06.547399
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dnsfact_collector_obj = DnsFactCollector()
    dnsfact_collector_obj.collect()

# Generated at 2022-06-13 02:57:07.590576
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    my_dns_facts = DnsFactCollector().collect()
    return my_dns_facts


# Generated at 2022-06-13 02:57:08.757099
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    col = DnsFactCollector()
    assert col.name == 'dns'
    assert col._fact_ids == set()

# Generated at 2022-06-13 02:57:09.603544
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns = DnsFactCollector()
    assert dns.collect() != None

# Generated at 2022-06-13 03:00:11.063698
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    res = collector.collect()
    assert 'dns' in res
# End of unit test for method collect of class DnsFactCollector

# Generated at 2022-06-13 03:00:12.509576
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'

# Generated at 2022-06-13 03:00:17.041466
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    content = 'a\nb\nc\n'
    dns_facts = {}
    dns_facts['dns'] = {}
    dns_facts['dns']['nameservers'] = ['a', 'b', 'c']
    assert dns_fact_collector._collect(content) == dns_facts

# Generated at 2022-06-13 03:00:17.518430
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 03:00:19.619546
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dnsCollector = DnsFactCollector()
    assert dnsCollector.name == 'dns'
    assert dnsCollector._fact_ids == set()


# Generated at 2022-06-13 03:00:26.138227
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_data = 'search_test\nnameserver 10.0.2.3\nnameserver 8.8.8.8\nnameserver 127.0.0.123\ndomain domain_test\noptions timeout:1 attempts:2\nsortlist 192.168.1.0/24 192.168.2.0/24'
    test_object = DnsFactCollector()
    result = test_object.collect({'file': {'content': test_data}}, {})

# Generated at 2022-06-13 03:00:26.957758
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 03:00:29.722711
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts
    assert dns_facts.name == 'dns'
    assert dns_facts._fact_ids == set()


# Generated at 2022-06-13 03:00:31.489705
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    dfc.collect()
    assert dfc.name == 'dns'

# Generated at 2022-06-13 03:00:38.064856
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    expected_result = {}
    expected_result['dns'] = {
        'nameservers': [
            '8.8.8.8',
            '8.8.4.4'
        ],
        'domain': 'example.com',
        'search': [
            'example.com',
            'subdomain.example.com'
        ],
        'sortlist': [
            '8.8.8.0/255.255.255.0'
        ],
        'options': {
            'ndots': 1,
            'timeout': 2
        }
    }
