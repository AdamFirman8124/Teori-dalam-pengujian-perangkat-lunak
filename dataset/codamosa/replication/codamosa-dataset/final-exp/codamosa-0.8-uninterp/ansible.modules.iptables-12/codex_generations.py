

# Generated at 2022-06-13 05:34:37.173865
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='192.0.2.1',
        destination='192.0.2.2',
        jump='REJECT',
        in_interface='eth0',
        out_interface='eth1',
        icmp_type='echo-request',
        ip_version='ipv4',
    )
    result = construct_rule(params)
    assert result == ['--icmp-type', 'echo-request', '-p', 'tcp', '-s', '192.0.2.1', '-d', '192.0.2.2', '-i', 'eth0', '-o', 'eth1', '-j', 'REJECT']

# Generated at 2022-06-13 05:34:41.352953
# Unit test for function set_chain_policy
def test_set_chain_policy():
    cmd = set_chain_policy("/sbin/iptables", {}, {"table": "filter", "chain": "ACCEPT", "policy": "ACCEPT"})
    assert cmd == ['/sbin/iptables', '-t', 'filter', '-P', 'ACCEPT', 'ACCEPT']



# Generated at 2022-06-13 05:34:50.564662
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('/sbin/iptables', '-I', dict(
        table='filter',
        chain='INPUT',
        rule_num='5',
        protocol='tcp',
        destination_port='443',
        jump='ACCEPT',
    )) == ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--dport', '443', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:34:58.162734
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    assert append_tcp_flags([], None, None) == []
    assert append_tcp_flags([], {}, None) == []
    assert append_tcp_flags([], {'flags': None}, None) == []
    assert append_tcp_flags([], {'flags_set': None}, None) == []
    assert append_tcp_flags([], {'flags': None, 'flags_set': None}, None) == []
    assert append_tcp_flags([], {'flags': ['SYN']}, None) == []
    assert append_tcp_flags([], {'flags_set': ['SYN']}, None) == []
    assert append_tcp_flags([], {'flags': ['SYN'], 'flags_set': ['SYN']}, None) == []

# Generated at 2022-06-13 05:35:09.878552
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:35:21.619136
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import sys
    sys.path.append("/usr/share/ansible")
    from ansible.module_utils import basic

    import iptables

    # module = AnsibleModule(argument_spec={})

    # without policy set
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = lambda a, b: (0, "Chain INPUT (policy ACCEPT)\n", '')
    assert iptables.get_chain_policy("/bin/iptables", module, {
        'chain': 'INPUT'
    }) == 'ACCEPT'

    # with policy set
    module.run_command = lambda a, b: (0, "Chain INPUT (policy DROP)\n", '')

# Generated at 2022-06-13 05:35:25.291896
# Unit test for function push_arguments
def test_push_arguments():
    cmd = push_arguments('iptables', '-I', dict(table='filter', chain='INPUT',
                                               rule_num=1, protocol='tcp',
                                               source='127.0.0.1', comment='test rule'))
    assert(cmd == ['iptables', '-t', 'filter', '-I', 'INPUT', '1', '-p', 'tcp', '-s', '127.0.0.1', '-m', 'comment', '--comment', 'test rule'])



# Generated at 2022-06-13 05:35:38.215395
# Unit test for function push_arguments
def test_push_arguments():
    import tempfile
    import os
    path = tempfile.mkdtemp()

# Generated at 2022-06-13 05:35:43.804824
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert None == get_chain_policy(
        'iptables', None, dict(
            table='filter',
            chain='input',
            policy=None))
    assert 'ACCEPT' == get_chain_policy(
        'iptables', None, dict(
            table='filter',
            chain='input',
            policy='ACCEPT'))



# Generated at 2022-06-13 05:35:54.829019
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class ModuleMock:
        def run_command(self, cmd, check_rc=True):
            if cmd == ['iptables', '-L', 'INPUT', '-t', 'filter', '-n', '-v']:
                return 0, """Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
""", ''
            if cmd == ['iptables', '-L', 'INPUT', '-t', 'filter']:
                return 0, """Chain INPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
""", ''

# Generated at 2022-06-13 05:36:15.355581
# Unit test for function flush_table

# Generated at 2022-06-13 05:36:21.232664
# Unit test for function flush_table
def test_flush_table():
    ip_mod = AnsibleModule
    ip_mod.run_command = run_command
    ip_mod.fail_json = fail_json
    ip_mod.exit_json = exit_json

    flush_table("iptables", ip_mod, dict(table='nat', chain='OUTPUT'))



# Generated at 2022-06-13 05:36:26.653901
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(
        argument_spec=dict(
            table=dict(required=True, default='filter'),
            chain=dict(default=None),
            flush=dict(default=False, type='bool'),
            ip_version=dict(default='ipv4', choices=['ipv4', 'ipv6']),
        ),
        supports_check_mode=True,
    )
    flush_table()



# Generated at 2022-06-13 05:36:36.253379
# Unit test for function construct_rule
def test_construct_rule():
    test_params = dict(
        protocol='tcp',
        source='192.168.0.1',
        jump='ACCEPT',
        comment='Accept SSH',
    )
    result = construct_rule(test_params)
    assert result == [
        '-p', 'tcp',
        '-s', '192.168.0.1',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', 'Accept SSH',
        ]
    test_params = dict(
        protocol='tcp',
        source='192.168.0.1',
        jump='ACCEPT',
        log_level='info',
        log_prefix='my_rule',
        comment='Accept SSH',
    )
    result = construct_rule(test_params)

# Generated at 2022-06-13 05:36:44.085940
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:52.156924
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': "INPUT"}) == "ACCEPT"
    assert get_chain_policy(None, None, {'chain': "OUTPUT"}) == "ACCEPT"
    assert get_chain_policy(None, None, {'chain': "FORWARD"}) == "ACCEPT"
    assert get_chain_policy(None, None, {'chain': "FORWARD"}) == "ACCEPT"
    assert get_chain_policy(None, None, {'chain': "INPUT", "table": "nat"}) == "ACCEPT"
    assert get_chain_policy(None, None, {'chain': "OUTPUT", "table": "nat"}) == "ACCEPT"

# Generated at 2022-06-13 05:36:59.574573
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = 'iptables'
    fake_module = type(
        'AnsibleModule',
        (object,),
        dict(
            run_command=lambda x, check_rc: (0, 'policies: DROP', ''),
            fail_json=lambda x: None,
            check_mode=False,
            no_log=False,
        ))
    fake_module = fake_module()
    params = dict(
        chain='INPUT',
        ip_version='ipv4',
        table='filter')
    assert get_chain_policy(iptables_path, fake_module, params) == 'DROP'


    # in case the header doesn't contains `policy` option

# Generated at 2022-06-13 05:37:11.829150
# Unit test for function main
def test_main():
    # Populate params with valid data to create fake objects
    # to pass to main()

    params = dict(
        table='filter',
        state='present',
        action='append',
        ip_version='ipv4',
        chain='INPUT',
        protocol='tcp',
        destination='192.168.0.1',
        destination_ports=['22'],
        jump='ACCEPT'
    )

    # Create a magic mock for module
    module = Mock()

    # Create fake return values for AnsibleModule.
    # The fakes will be used for the side_effect
    # of AnsibleModule.run_command when called
    # with iptables command

    # Fake for already added rule. Return code is 0.
    # No change occurs.

# Generated at 2022-06-13 05:37:19.004720
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(jump='foo', protocol=None, comment='bar')) == ['-j', 'foo', '-m', 'comment', '--comment', 'bar']
    assert construct_rule(dict(jump='foo', protocol='bar', comment='baz')) == ['-j', 'foo', '-p', 'bar', '-m', 'comment', '--comment', 'baz']
    assert construct_rule(dict(jump='foo', protocol='bar', comment=None)) == ['-j', 'foo', '-p', 'bar']
    assert construct_rule(dict(jump='foo', protocol='bar', comment=True)) == ['-j', 'foo', '-p', 'bar']

# Generated at 2022-06-13 05:37:27.669697
# Unit test for function remove_rule
def test_remove_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='22',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
        ip_version='ipv4',
        table='filter')
    assert(remove_rule('iptables', 1, params) == [
        'iptables', '-t', 'filter', '-D', 'INPUT',
        '!', '--syn', '-p', 'tcp', '--destination-port', '22', '-m', 'conntrack', '--ctstate', 'NEW',
        '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept new SSH connections.'])



# Generated at 2022-06-13 05:38:39.942858
# Unit test for function main

# Generated at 2022-06-13 05:38:54.090886
# Unit test for function construct_rule
def test_construct_rule():
    test_cases = [
        dict(
            name='REJECT all input',
            module_args=dict(
                table='filter',
                chain='INPUT',
                ip_version='ipv4',
                jump='REJECT',
                reject_with='icmp-host-prohibited',
            ),
            result=['-w', '-j', 'REJECT', '--reject-with', 'icmp-host-prohibited'],
        ),
    ]
    for test_case in test_cases:
        name = test_case['name']
        args = test_case['module_args']
        result = test_case['result']
        test_rule = construct_rule(args)

# Generated at 2022-06-13 05:38:57.762171
# Unit test for function append_match_flag
def test_append_match_flag():
    result = []
    append_match_flag(result, 'match', 'flag', True)
    assert result == ['flag']
    result = []
    append_match_flag(result, 'negate', 'flag', True)
    assert result == ['!', 'flag']
    result = []
    append_match_flag(result, None, 'flag', False)
    assert result == []



# Generated at 2022-06-13 05:39:03.899408
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(argument_spec={})
    params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
    )
    cmd = push_arguments(iptables_path, '-D', params)
    assert cmd == ['/sbin/iptables', '-t', 'filter', '-D', 'INPUT']



# Generated at 2022-06-13 05:39:07.879696
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, params) is False
    assert check_present('ip6tables', module, params) is False



# Generated at 2022-06-13 05:39:16.276082
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec=dict())
    module.params = dict(table='filter',
                         ip_version='ipv4',
                         chain='INPUT',
                         protocol=None,
                         dest='192.0.2.1')
    module.run_command = mock.Mock(return_value=(0, '', ''))
    assert check_present(BINS['ipv4'], module, module.params)
    module.run_command.assert_called_with(['iptables', '-t', 'filter', '-C', 'INPUT', '-d', '192.0.2.1'], check_rc=False)



# Generated at 2022-06-13 05:39:20.272513
# Unit test for function check_present
def test_check_present():
  assert check_present(None, None, dict(
    table='filter', chain='INPUT', state=None,
    ip_version='ipv4', rule_num=True,
  )) == True


# Generated at 2022-06-13 05:39:23.770088
# Unit test for function check_present
def test_check_present():
    pass
    #assert check_present(iptables_path, module, params) == ("iptables_path","module", "params")



# Generated at 2022-06-13 05:39:32.534484
# Unit test for function main
def test_main():
    # import needed modules
    import sys
    import os
    import pytest
    import testinfra

    # load the module source file
    src_file = 'modules/system/firewall_rule.py'
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    module = importlib.import_module('firewall_rule')
    module.AnsibleModule = AnsibleModule

    # load the module parameters

# Generated at 2022-06-13 05:39:37.321290
# Unit test for function get_iptables_version
def test_get_iptables_version():
    out = 'iptables v1.4.20'
    iptables_version = get_iptables_version('/sbin/iptables', None, out)
    assert iptables_version == '1.4.20'


# Generated at 2022-06-13 05:41:14.201510
# Unit test for function check_present
def test_check_present():
    assert check_present(None, None, {'table': None, 'chain': None, 'ip_version': 'ipv4'}) == False


# Generated at 2022-06-13 05:41:20.773879
# Unit test for function construct_rule
def test_construct_rule():
    """
    Construct rule with iptables module parameter
    """

# Generated at 2022-06-13 05:41:33.010688
# Unit test for function append_rule

# Generated at 2022-06-13 05:41:43.707564
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:46.759134
# Unit test for function get_chain_policy
def test_get_chain_policy():
    test_iptables_path='/sbin/iptables'
    test_params = dict(chain='INPUT', table='filter')
    assert get_chain_policy(test_iptables_path, module, test_params) == 'ACCEPT'



# Generated at 2022-06-13 05:41:49.461699
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # if none
    assert get_chain_policy('iptables', None, params={}) is None

    # if a policy is set
    assert get_chain_policy('iptables', None, params={'policy': 'ACCEPT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:41:56.667743
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = '/usr/bin/iptables'
    module = AnsibleModule(argument_spec={})
    params = {'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '80', 'jump': 'ACCEPT', 'action': 'insert', 'rule_num': 5}
    insert_rule(iptables_path, module, params)



# Generated at 2022-06-13 05:42:01.952759
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:09.593490
# Unit test for function construct_rule
def test_construct_rule():
    ''' Unit test for function construct_rule '''
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_ports=['80', '443'],
        jump='ACCEPT',
        ip_version='ipv4')
    result = construct_rule(params)
    assert result == ['-p', 'tcp', '-m', 'multiport', '--dports', '80,443', '-j', 'ACCEPT']

    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        ip_version='ipv4')
    result = construct_rule(params)
    assert result == ['-p', 'tcp', '--destination-port', '80', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:42:22.378552
# Unit test for function construct_rule
def test_construct_rule():
    input_parameters = dict(
        chain='INPUT',
        ip_version='ipv4',
        protocol='tcp',
        source='192.168.0.0/24',
        destination='192.168.1.1',
        match=['state'],
        ctstate=['RELATED'],
        jump=None,
        comment=None,
        load_basename=None
    )

    expected = [
        '-A', 'INPUT',
        '-s', '192.168.0.0/24',
        '-d', '192.168.1.1',
        '-p', 'tcp',
        '-m', 'state',
        '--state', 'RELATED'
    ]

    actual = construct_rule(input_parameters)

    assert expected == actual

