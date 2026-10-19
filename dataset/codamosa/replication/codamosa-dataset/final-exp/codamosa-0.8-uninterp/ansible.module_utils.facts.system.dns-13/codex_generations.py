

# Generated at 2022-06-13 02:51:20.840142
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    f = DnsFactCollector()
    print(f)
    #assert f.name == 'dns'
    #assert 'dns' in f._fact_ids


# Generated at 2022-06-13 02:51:22.148902
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # TODO: write unit test for method collect of class DnsFactCollector
    pass

# Generated at 2022-06-13 02:51:25.231146
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import pprint

    dns_fact_collector = DnsFactCollector()
    pprint.pprint(dns_fact_collector.collect())

if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 02:51:35.783611
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Arrange
    module = None
    collected_facts = None
    collector = DnsFactCollector()

    # Act
    res = collector.collect(module, collected_facts)

    # Assert
    assert res['dns']['domain'] == u'ubuntu.com' # pylint: disable=undefined-loop-variable
    assert res['dns']['nameservers'] == [u'127.0.1.1'] # pylint: disable=undefined-loop-variable
    assert res['dns']['options'][u'ndots'] == u'3' # pylint: disable=undefined-loop-variable
    assert res['dns']['search'] == [u'ubuntu.com'] # pylint: disable=undefined-loop-variable

# Generated at 2022-06-13 02:51:42.389202
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_file_lines
    dns_facts_collector = DnsFactCollector()
    Collector._fact_collectors['dns'] = DnsFactCollector
    assert len(dns_facts_collector._fact_ids) == 0
    assert 'dns' in Collector._fact_collectors
    assert len(Collector._fact_collectors) == 1
    # Generate /etc/resolv.conf file

# Generated at 2022-06-13 02:51:43.501826
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts_collector = DnsFactCollector()
    assert dns_facts_collector != None

# Generated at 2022-06-13 02:51:51.090483
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    def _is_subdict(sub_dict, superset):
        for k, v in sub_dict.items():
            if k not in superset or superset[k] != v:
                return False
        return True

    # Setup
    class MockModule:
        def __init__(self):
            self.params = {}

    mock_module = MockModule()

    dns_fact_collector = DnsFactCollector(mock_module)

    # Test with no results

# Generated at 2022-06-13 02:51:56.924401
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # TODO: Fix this to use a mock module.  The use of a dict for the module parameter
    #       is causing name collisions within the tests.
    module = {}
    # Basic testing of the collect method of the DnsFactCollector class
    dns_fact_collector = DnsFactCollector(module)
    collected_facts = dns_fact_collector.collect(module)
    assert 'dns' == collected_facts['dns']['dns']['domain']

# Generated at 2022-06-13 02:51:57.854700
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:51:59.733129
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
	obj = DnsFactCollector()
	assert obj.name == 'dns'
	assert obj._fact_ids == set()


# Generated at 2022-06-13 02:52:15.943244
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    def check_resolv_conf(resolv_conf, output):
        with open('/tmp/resolv.conf', 'w') as f:
            f.write(resolv_conf)
        module = {}
        collected_facts = {}
        dns_fact_collector = DnsFactCollector()
        dns_facts = dns_fact_collector.collect(module, collected_facts)

        for key in output:
            assert key in dns_facts['dns']
            assert dns_facts['dns'][key] == output[key]


# Generated at 2022-06-13 02:52:18.663821
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()

    assert dns_facts.name == 'dns'
    assert isinstance(dns_facts._fact_ids, set)


# Generated at 2022-06-13 02:52:24.728990
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    facts = DnsFactCollector()

    # Test with correct options
    assert facts.name == "dns"
    assert facts._fact_ids == set()

    # Test with missing "name" option
    # TODO: find a way to re-initialize class properly
    del facts.name
    assert not hasattr(facts, "name")
    assert facts.name == "dns"

# Generated at 2022-06-13 02:52:27.738291
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()

    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()



# Generated at 2022-06-13 02:52:39.265869
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolver = DnsFactCollector()
    dns_facts = resolver.collect()

    assert 'dns' in dns_facts, "Facts: %s" % (dns_facts)
    assert isinstance(dns_facts['dns'], dict), "dns_facts: %s" % (dns_facts)
    assert 'nameservers' in dns_facts['dns'], "dns_facts: %s" % (dns_facts)
    assert isinstance(dns_facts['dns']['nameservers'], list), "dns_facts: %s" % (dns_facts)
    assert 'domain' in dns_facts['dns'], "dns_facts: %s" % (dns_facts)

# Generated at 2022-06-13 02:52:42.868721
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()
    assert dns_facts['dns']['nameservers'] == ['10.20.30.152', '10.20.30.151']
    assert dns_facts['dns']['search'] == ['example.com', 'example.net']
    assert dns_facts['dns']['options']['timeout'] == '2'

# Generated at 2022-06-13 02:52:52.087378
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create a new instance of the class under test
    dns_fact_collector = DnsFactCollector()

    # Set data to be returned by get_file_content
    get_file_content.data = "# comment\n" \
                            "nameserver 192.168.0.1\n" \
                            "nameserver 192.168.0.2\n" \
                            "domain example.com\n" \
                            "search example.com example.net\n" \
                            "sortlist 192.168.0.0/255.255.0.0\n" \
                            "options debug ndots:3\n"

    # Call the collect method
    result = dns_fact_collector.collect()

    # Test the returned data

# Generated at 2022-06-13 02:53:02.667259
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()


# Generated at 2022-06-13 02:53:03.897962
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass

# Generated at 2022-06-13 02:53:11.831137
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolv_content = '''
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 1.1.1.1
nameserver 4.4.4.4
options timeout:1 attempts:2 rotate '''.lstrip()

    resolv_hdlr = DnsFactCollector({})
    resolv_hdlr.get_file_content = lambda f: resolv_content
    resolv_hdlr.get_file_content.__name__ = 'mock_func'


# Generated at 2022-06-13 02:53:38.207716
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Setup
    dns_collector = DnsFactCollector()

    # Fake the content of the file /etc/resolv.conf
    resolv_content = '\n'.join([
        '# dynamic resolv.conf(5) file for glibc resolver(3) generated by '
        'resolvconf(8)',
        '#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE '
        'OVERWRITTEN',
        'nameserver 127.0.0.1',
        'nameserver 123.123.123.123',
        'search example.com',
        'domain example.com',
        'sortlist 192.168.0.0/255.255.0.0'
    ])

    # Expected result

# Generated at 2022-06-13 02:53:49.268585
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()
    dns_facts = dfc.collect()
    assert dns_facts['dns']['nameservers'] == ['8.8.8.8', '8.8.4.4']
    assert dns_facts['dns']['domain'] == 'company.com'
    assert dns_facts['dns']['search'] == ['company.com']
    assert dns_facts['dns']['sortlist'] == ['10.1.0.0/255.255.0.0']
    assert dns_facts['dns']['options']['edns0'] == True
    assert dns_facts['dns']['options']['timeout'] == '2'

# Generated at 2022-06-13 02:53:50.918738
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
  x = DnsFactCollector()
  assert x.name == "dns"
  assert x.collect() != None

# Generated at 2022-06-13 02:53:56.295137
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Testing method collect of class DnsFactCollector
    #
    # Setup:
    #
    # Mock input parameters
    #
    # Mock modules
    #
    # Mock classes
    #
    #
    # Test:
    #
    # Assertion 1:
    #
    #
    #
    # Cleanup:
    #

    pass

# Generated at 2022-06-13 02:54:04.103803
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    input_str = """
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 127.0.0.1
nameserver 127.0.1.1
search us.gadt.example.com foo.bar baz.example.com
sortlist 10.0.0.0/8 20.0.0.0/8 30.0.0.0/8
options rotate timeout:1 attempts:1
;
; this is a comment that should be ignored
;
    """

# Generated at 2022-06-13 02:54:05.998260
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fc = DnsFactCollector()
    fc.collect()
    assert 0

# Generated at 2022-06-13 02:54:07.192104
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector = DnsFactCollector()


# Generated at 2022-06-13 02:54:14.626759
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils import facts
    from ansible.module_utils.facts.utils import get_file_content
    import os.path
    import json

    content = '''# This is the primary configuration file for the BIND DNS server named.
#
# Please read /usr/share/doc/bind9/README.Debian.gz for information on the
# structure of BIND configuration files in Debian, *BEFORE* you customize
# this configuration file.
#
# If you are just adding zones, please do that in /etc/bind/named.conf.local

include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";
'''


# Generated at 2022-06-13 02:54:16.371984
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.__name__ == 'DnsFactCollector'

# Generated at 2022-06-13 02:54:25.523756
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    f.file.write("""
# comment
domain test.com
search foo.com bar.com
nameserver 127.0.0.1
nameserver 192.168.0.1
options timeout:2 attempts:2
sortlist 1.2.3.4/255.255.255.0 0.0.0.0/0.0.0.0
""")
    f.close()
    DnsFactCollector._FILE_NAME_RESOLV_CONF = f.name
    facts = DnsFactCollector.collect()
    assert facts['dns']['domain'] == 'test.com'
    assert facts['dns']['search'] == ['foo.com', 'bar.com']

# Generated at 2022-06-13 02:55:00.445404
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    from ansible.module_utils.facts.collector.dns import DnsFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    fc = DnsFactCollector()
    assert isinstance(fc, DnsFactCollector)
    result = fc.collect(None, None)
    assert 'dns' in result
    assert 'nameservers' in result['dns']
    assert 'domain' in result['dns']
    assert 'search' in result['dns']
    assert 'sortlist' in result['dns']
    assert 'options' in result['dns']
    assert result['dns']['nameservers'] == ["1.2.3.4"]
    assert result['dns']['domain'] == "example.com"

# Generated at 2022-06-13 02:55:01.928393
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    collector = DnsFactCollector()
    assert collector.name == 'dns'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:55:03.367225
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # Check that name is set
    assert DnsFactCollector().name == 'dns'

# Generated at 2022-06-13 02:55:08.099175
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolv_conf_file_contents = '''
; generated by /sbin/dhclient-script
search foo.example.com bar.example.com
nameserver 192.0.2.1
nameserver 192.0.2.2
nameserver 192.0.2.3
options timeout:1 attempts:5 ndots:1
'''
    module = None
    collected_facts = None

    # Mock the file module
    file_module = AnsibleModule(
        argument_spec=dict()
    )
    file_module.params = {}
    file_module.fail_json = fail_json
    file_module.exit_json = exit_json
    setattr(file_module, 'run_command', run_command)

# Generated at 2022-06-13 02:55:10.122657
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector({})
    f = dfc.collect()
    assert isinstance(f, dict)


# Generated at 2022-06-13 02:55:12.675964
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance

    util_collector = get_collector_instance(DnsFactCollector)

    res = util_collector.collect({}, {})

    assert res is not None

# Generated at 2022-06-13 02:55:13.384097
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    pass


# Generated at 2022-06-13 02:55:16.769295
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    import sys
    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins
    if hasattr(builtins, '__IPYTHON__'):
        del builtins.module
    assert DnsFactCollector.name == "dns"

# Generated at 2022-06-13 02:55:27.365726
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    import os.path

    resolv_conf_content = '''
options ndots:1
sortlist 1.2.3.4/16 1.2.3.4/24 1.2.3.4/32
search example.com notareal.com
nameserver 1.2.3.4
nameserver 2.4.6.8
nameserver 3.6.9.12
domain mydomain.com
'''
    resolv_conf_path = os.path.join('/tmp/test.dns', 'resolv.conf')
    os.makedirs(os.path.join('/tmp/test.dns'))

    with open(resolv_conf_path, 'w') as f:
        f.write(resolv_conf_content)
    dns_facts = Dns

# Generated at 2022-06-13 02:55:36.501945
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    with open("test_resolv.conf") as f:
        resolv = f.readlines()
    content = "".join(resolv)
    dns_collector = DnsFactCollector()
    actual_resolv = dns_collector.collect(None,None)
    expected_result = {'dns': {'nameservers': ['10.5.5.5', '8.8.8.8'], 
                                'search': ['home.local', 'test.in.local'],
                                'sortlist': ['10.5.5.5'],
                                'options': {'ndots': '1', 'timeout': '3', 'attempts': '2'}, 
                                'domain': 'home.local'}
                        }

# Generated at 2022-06-13 02:56:49.539594
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    results = dns_fact_collector.collect()

    assert 'dns' in results
    assert results['dns']['nameservers'][0] == '10.0.2.3'
    assert results['dns']['domain'] == 'domain.cisco.com'
    assert results['dns']['search'][1] == 'cisco.com'
    assert len(results['dns']['sortlist']) == 0
    assert results['dns']['options']['ndots'] == '1'

# Generated at 2022-06-13 02:56:58.800496
# Unit test for method collect of class DnsFactCollector

# Generated at 2022-06-13 02:57:01.007182
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collector = DnsFactCollector()
    results = collector.collect()
    assert 'dns' in results
    assert 'nameservers' in results['dns']
    assert len(results['dns']['nameservers']) >= 1

# Generated at 2022-06-13 02:57:01.471137
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass
    # TODO

# Generated at 2022-06-13 02:57:03.032664
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()

    try:
        res = dns_facts.collect()
        assert 'dns' in res
    except AssertionError:
        raise AssertionError('DnsFactCollector should collect "dns" facts')

# Generated at 2022-06-13 02:57:12.011799
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Only testing values, structure is tested by AnsibleFacts
    test_files = [
        '/etc/resolv.conf',
        '/etc/resolv.conf.content',
    ]
    for test_file in test_files:
        collector = DnsFactCollector(None, test_file)
        facts = collector.collect(None, None)
        if test_file == '/etc/resolv.conf':
            assert 'dns' in facts
            assert facts['dns']['nameservers'] == ['1.2.3.4']
            assert facts['dns']['domain'] == 'example.com'
            assert facts['dns']['search'] == ['example.com', 'example2.com']

# Generated at 2022-06-13 02:57:16.260428
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    class MockModule:
        pass

    mock_module = MockModule()
    mock_facts = {
        'dns': {
            'nameservers': ['8.8.8.8'],
            'domain': None,
            'search': None,
            'options': {}
        }
    }

    module_returned_facts = DnsFactCollector().collect(mock_module, mock_facts)

    assert isinstance(module_returned_facts, dict)
    assert module_returned_facts == mock_facts

# Generated at 2022-06-13 02:57:17.594204
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_collector = DnsFactCollector()
    assert dns_collector.name == 'dns'
    assert dns_collector._fact_ids == set()


# Generated at 2022-06-13 02:57:20.478321
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    collected_facts = DnsFactCollector.collect()
    assert collected_facts == {}

# Generated at 2022-06-13 02:57:27.934382
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    Test the method DnsFactCollector.collect
    :return:
    """
    # Test 1:
    # Test dns_facts that are returned by the collect method
    dns_facts = DnsFactCollector.collect(BaseFactCollector, {})

    assert isinstance(dns_facts, dict)
    assert dns_facts.keys() == ['dns']

    # with open('/etc/resolv.conf.test1') as f:
    #     resolv_conf = f.read()




if __name__ == '__main__':
    test_DnsFactCollector_collect()

# Generated at 2022-06-13 03:00:26.931344
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    facts = dns_fact_collector.collect()

    assert facts['dns']['domain'] == 'dylan-y'
    assert facts['dns']['search'] == ['dylan-y']
    assert facts['dns']['nameservers'] == ['192.168.1.1']
    assert type(facts) is dict
    assert type(facts['dns']) is dict

# Generated at 2022-06-13 03:00:30.047249
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    # Check DnsFactCollector has name field
    assert DnsFactCollector.name == 'dns'

    # Check DnsFactCollector has _fact_ids set
    assert DnsFactCollector._fact_ids != None


# Generated at 2022-06-13 03:00:36.205266
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.plugins.system.dns import DnsFactCollector

    content = """
nameserver 8.8.8.8
search foo.example.com bar.example.org
domain example.com
    """
    dns_facts = DnsFactCollector().collect(collected_facts=dict())
    assert dns_facts == {'dns': {
        'nameservers': ['8.8.8.8', '8.8.4.4'],
        'search': ['foo.example.com', 'bar.example.org'],
        'domain': 'example.com'
    }}


# Generated at 2022-06-13 03:00:41.290207
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    """
    This method does the testing for DnsFactCollector.collect()
    'dns' is a dictionary of subdictionaries, so the testing is more complex.

    Test cases:
    1. Test for simple entry of name servers
    2. Test for multiple name servers
    3. Test for simple entry of domain
    4. Test for multiple search
    5. Test for sortlist
    6. Test for options
    7. Test for comments
    8. Test for other lines
    9. Test for empty file
    10. Test for non-existent file
    """

    # Create a fake module and options
    module = []
    options = []

    # Create an empty collected facts and call the method collect of class DnsFactCollector
    collected_facts = {}
    dns_fact_collector = DnsFactCollector()
    d

# Generated at 2022-06-13 03:00:43.287104
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 03:00:48.161996
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """Test DnsFactCollector class"""
    dns_fact_collector = DnsFactCollector()

    # Test if instance
    assert isinstance(dns_fact_collector, DnsFactCollector)

    # Test if subclass
    assert issubclass(DnsFactCollector, BaseFactCollector)

    # Test name
    assert dns_fact_collector.name == 'dns'

    # Test _fact_ids
    assert dns_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:00:49.228015
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == 'dns'

# Generated at 2022-06-13 03:00:50.251355
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector != None


# Generated at 2022-06-13 03:00:58.872359
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_file_content = '''# comment
    options timeout:1 attempts:5
    nameserver 10.10.10.10
    nameserver 8.8.8.8
    sortlist 172.16.0.0/255.255.0.0
    domain example.com
    search s1.example.com s2.example.com
    '''
    collect_mock = {
        "module_utils.basic.AnsibleModule": None,
        "ansible.module_utils.facts.utils.get_file_content": lambda x: dns_file_content
    }

    import __builtin__
    builtin_mock = {
        "__import__": __builtin__.__import__,
        "open": __builtin__.open
    }


# Generated at 2022-06-13 03:01:03.149884
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
	fact_collector_obj = DnsFactCollector()
	assert len(fact_collector_obj.collect()['dns']['options'].keys()) == 1
	assert len(fact_collector_obj.collect()['dns']['nameservers']) == 2