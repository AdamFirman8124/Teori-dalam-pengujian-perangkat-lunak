

# Generated at 2022-06-13 05:34:39.982427
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule=[]
    param=dict(flags=['SYN'], flags_set=[])
    append_tcp_flags(rule, param, '--tcp-flags')
    assert(rule == ['--tcp-flags', 'SYN', 'NONE'])
    rule = []
    param=dict(flags=[], flags_set=['SYN', 'ACK'])
    append_tcp_flags(rule, param, '--tcp-flags')
    assert(rule == ['--tcp-flags', 'ALL', 'SYN,ACK'])
    rule = []
    param = dict(flags=['SYN', 'ACK'], flags_set=[])
    append_tcp_flags(rule, param, '--tcp-flags')

# Generated at 2022-06-13 05:34:51.870558
# Unit test for function main

# Generated at 2022-06-13 05:34:55.337439
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', None, {
        'chain': 'INPUT',
    }) == None
    assert get_chain_policy('iptables', None, {
        'chain': 'INPUT',
        'policy': 'ACCEPT',
    }) == 'ACCEPT'



# Generated at 2022-06-13 05:34:57.058436
# Unit test for function check_present
def test_check_present():
    f = check_present('iptables', module, params)
    assert(f)



# Generated at 2022-06-13 05:35:08.457427
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-I', {
        'table': 'nat',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'jump': 'ACCEPT',
        'ip_version': 'ipv4',
    }, False) == [
        'iptables', '-t', 'nat', '-I', 'INPUT',
    ]

# Generated at 2022-06-13 05:35:23.672253
# Unit test for function get_chain_policy
def test_get_chain_policy():
    path = '/sbin/iptables'
    module = type('Module', (object, ), dict())
    module.run_command = lambda cmd, check_rc=True: (
        0,
        '''Chain INPUT (policy ACCEPT)
target     prot opt source               destination''',
        None)
    params = dict(
        table='filter',
        chain='INPUT',
        policy='ACCEPT'
    )
    assert get_chain_policy(path, module, params) == 'ACCEPT'
    module.run_command = lambda cmd, check_rc=True: (
        0,
        '''Chain INPUT (policy DROP)
target     prot opt source               destination''',
        None)
    params = dict(
        table='filter',
        chain='INPUT',
        policy='ACCEPT'
    )

# Generated at 2022-06-13 05:35:26.837921
# Unit test for function append_match_flag
def test_append_match_flag():
    assert append_match_flag('rule', 'match', '--syn', True) == ['--syn']
    assert append_match_flag('rule', 'negate', '--syn', True) == ['!', '--syn']



# Generated at 2022-06-13 05:35:27.742972
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('iptables', 'module', 'params') == None



# Generated at 2022-06-13 05:35:31.946604
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(protocol='tcp', jump='ACCEPT')) == [
        '-p', 'tcp', '-j', 'ACCEPT']
    assert construct_rule(dict(
        protocol='tcp',
        jump='ACCEPT',
        comment='my comment',
        ctstate='NEW,EST',
    )) == ['-p', 'tcp', '-m', 'conntrack', '--ctstate',
           'NEW,EST', '-m', 'comment', '--comment', 'my comment', '-j', 'ACCEPT']


# Generated at 2022-06-13 05:35:35.106522
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain_header = 'Chain INPUT (policy ACCEPT)'
    result = re.search(r'\(policy ([A-Z]+)\)', chain_header)
    assert result.group(1) == 'ACCEPT'



# Generated at 2022-06-13 05:36:00.535172
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:05.783312
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:13.223474
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = FakeAnsibleModule()
    assert not get_chain_policy(None, module, {"chain": "INPUT", "state": "present"})
    module.run_command.return_value = 0, " Chain INPUT (policy DROP)", ""
    assert get_chain_policy(None, module, {"chain": "INPUT", "state": "present"}) == "DROP"



# Generated at 2022-06-13 05:36:14.161492
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule({})
    module.check_mode = True



# Generated at 2022-06-13 05:36:19.563719
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy("iptables", "module", dict(
        table="filter",
        chain="INPUT",
        ip_version="ipv4"
    )) == "ACCEPT"
    assert get_chain_policy("iptables", "module", dict(
        table="filter",
        chain="OUTPUT",
        ip_version="ipv4"
    )) == "ACCEPT"
    assert get_chain_policy("iptables", "module", dict(
        table="filter",
        chain="FORWARD",
        ip_version="ipv4"
    )) == "ACCEPT"



# Generated at 2022-06-13 05:36:30.751593
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(ip_version='ipv4', chain='INPUT', protocol='tcp', dport='22', ctstate='NEW', syn='match', jump='ACCEPT', comment='Accept new SSH connections.')) == ['-w', '-p', 'tcp', '-m', 'conntrack', '--ctstate', 'NEW', '--syn', '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept new SSH connections.']

# Generated at 2022-06-13 05:36:38.023107
# Unit test for function check_present

# Generated at 2022-06-13 05:36:43.471394
# Unit test for function get_chain_policy
def test_get_chain_policy():
    policy = get_chain_policy(None, None, params={'chain':'OUTPUT'})
    assert policy == 'OUTPUT'
    policy = get_chain_policy(None, None, params={'chain':'FORWARD'})
    assert policy == 'ACCEPT'
    policy = get_chain_policy(None, None, params={'chain':'FOO'})
    assert policy == None



# Generated at 2022-06-13 05:36:48.934193
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = mock.MagicMock()
    params = dict(
        chain='INPUT',
        table='filter',
        ip_version='ipv4'
    )
    expected_out="""Chain INPUT (policy ACCEPT)
target     prot opt source               destination"""
    module.run_command.return_value = (0, expected_out, '')
    assert get_chain_policy('iptables', module, params) == 'ACCEPT'


# Generated at 2022-06-13 05:36:57.236012
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:19.995414
# Unit test for function main

# Generated at 2022-06-13 05:37:31.771435
# Unit test for function main
def test_main():
    # No chain specified
    with pytest.raises(SystemExit):
        main()

    # Check if chain is required
    with pytest.raises(SystemExit):
        main(dict(
            chain=None,
        ))

    # Add rule and flush table
    with mock.patch('builtins.open', mock.mock_open(read_data='data')):
        def get_bin_path(executable, required=False):
            return executable
        def check_mode():
            return True
        def run_command(cmd, check_rc=True):
            return 0, '', ''
        m = mock.Mock()
        m.get_bin_path = mock.Mock(side_effect=get_bin_path)
        m.check_mode = mock.Mock(side_effect=check_mode)

# Generated at 2022-06-13 05:37:34.267919
# Unit test for function main
def test_main():
    # Unit test for function main
    return

# Generated at 2022-06-13 05:37:39.377188
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:50.890417
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == ['-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']

    params['ip_version'] = 'ipv6'
    rule = construct_rule(params)
    assert rule == ['-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']

    params = dict(
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        in_interface='eth0',
        out_interface='eth1',
        ip_version='ipv4',
    )

# Generated at 2022-06-13 05:37:55.338046
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(argument_spec={})
    params = dict(policy=None)
    result = get_chain_policy(iptables_path, module, params)
    assert result is not None



# Generated at 2022-06-13 05:38:00.592694
# Unit test for function insert_rule

# Generated at 2022-06-13 05:38:03.635432
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('iptables', 'module', 'params') == r'''
[module]
-D [params]
  '''.strip()



# Generated at 2022-06-13 05:38:13.272646
# Unit test for function construct_rule
def test_construct_rule():
    '''
    # Test cases for construct_rule function
    '''
    # Test case 1: add rule with all parameters set except 'protocol', 'source',
    #              'destination'

# Generated at 2022-06-13 05:38:18.716062
# Unit test for function main
def test_main():
    from ansible.modules.network.firewall import iptables
    from ansible.module_utils.basic import AnsibleModule
    import doctest

    argspec = iptables.argument_spec
    argspec['ip_version'] = 'ipv4'
    argspec['table'] = 'filter'
    argspec['chain'] = 'INPUT'
    argspec['rule_num'] = None
    del argspec['flush']
    del argspec['policy']

    module = AnsibleModule(argument_spec=argspec)
    iptables.main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:38:38.594226
# Unit test for function main
def test_main():
    args = dict(
        ip_version = 'ipv4',
        table = 'filter',
        chain = 'filter',
        flush = True,
    )
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert result.value.args[0]['ip_version'] == args['ip_version']
    assert result.value.args[0]['table'] == args['table']
    assert result.value.args[0]['chain'] == args['chain']
    assert result.value.args[0]['flush'] == args['flush']


# Generated at 2022-06-13 05:38:53.284385
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:59.350780
# Unit test for function construct_rule
def test_construct_rule():
    parameters = dict(destination='8.8.8.8', jump='DROP')
    expected = ['-d', '8.8.8.8', '-j', 'DROP']
    assert construct_rule(parameters) == expected



# Generated at 2022-06-13 05:39:00.747267
# Unit test for function check_present
def test_check_present():
    assert check_present('/sbin/iptables', None, {
        'ip_version': 'ipv4',
        'chain': 'INPUT',
        'table': 'filter'
    }) == True



# Generated at 2022-06-13 05:39:03.765413
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(chain='INPUT', table='filter')) == 'DROP'



# Generated at 2022-06-13 05:39:15.723376
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(match=['conntrack'], ctstate=['RELATED', 'ESTABLISHED'])) == ['-m', 'conntrack', '--ctstate', 'RELATED,ESTABLISHED']
    assert construct_rule(dict(match=['conntrack'], ctstate=['NEW'])) == ['-m', 'conntrack', '--ctstate', 'NEW']
    assert construct_rule(dict(match=['conntrack'])) == []
    assert construct_rule(dict(match=['state'], ctstate=['RELATED', 'ESTABLISHED'])) == ['-m', 'state', '--state', 'RELATED,ESTABLISHED']

# Generated at 2022-06-13 05:39:16.706255
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule(iptables_path, module, params) == None



# Generated at 2022-06-13 05:39:19.262236
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, {'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:39:23.481574
# Unit test for function set_chain_policy
def test_set_chain_policy():
    with open('./test/test_set_chain_policy.txt', 'r') as f:
        expected = f.read().splitlines()
    iptables_path = '/sbin/iptables'
    module = MockModule(params={'chain': 'INPUT', 'policy': 'DROP', 'ip_version': 'ipv4'})
    result = set_chain_policy(iptables_path, module, module.params)
    assert result == module.run_command(expected, check_rc=True)


# Generated at 2022-06-13 05:39:30.167762
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule({})
    cmd = push_arguments('iptables', '-C', {
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '23'
    })
    module.run_command(cmd, check_rc=False)
    module.exit_json(stdout='-A INPUT -p tcp -m multiport --dports 23 -j DROP\n')



# Generated at 2022-06-13 05:40:05.023430
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.ansible_release import __version__
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import MagicMock

    def get_chain_policy_out(chain, policy):
        data_chain = []
        data_chain.append("Chain %s (policy %s)" % (chain, policy))
        data_chain.append("target     prot opt source               destination")
        data_chain.append("")
        out = "\n".join(data_chain)
        return out

    module = MagicMock()
    module.run_command = MagicMock()
    policy = dict(
        ipv4='iptables',
        ipv6='ip6tables',
    )

# Generated at 2022-06-13 05:40:17.668605
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:27.727388
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path='iptables'
    module=object()

# Generated at 2022-06-13 05:40:31.153038
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(jump='DROP', source='1.1.1.1')) == ['-s', '1.1.1.1', '-j', 'DROP']
    assert construct_rule(dict(jump=None, source='1.1.1.1')) == ['-s', '1.1.1.1']

# Generated at 2022-06-13 05:40:36.391495
# Unit test for function get_chain_policy
def test_get_chain_policy():
    """
    Test for the get_chain_policy function.
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            chain='INPUT',
            table='filter',
        ),
        supports_check_mode=True,
    )

    iptables_path = 'iptables'
    params = dict(chain='INPUT', table='filter')
    cmd = push_arguments(iptables_path, '-L', params, make_rule=False)
    rc, out, _ = module

# Generated at 2022-06-13 05:40:48.060547
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'table': 'filter', 'chain': 'INPUT'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'table': 'filter', 'chain': 'FORWARD'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'table': 'filter', 'chain': 'OUTPUT'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'table': 'nat', 'chain': 'PREROUTING'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'table': 'nat', 'chain': 'OUTPUT'}) == 'ACCEPT'

# Generated at 2022-06-13 05:40:55.941892
# Unit test for function get_iptables_version
def test_get_iptables_version():
    # mock iptables_path, module and their results
    iptables_path = 'iptables'
    module = Mock(run_command=Mock(return_value=(0, 'iptables v1.6.1\n', '')))
    assert get_iptables_version(iptables_path, module) == '1.6.1'
    module = Mock(run_command=Mock(return_value=(0, 'iptables v1.4.20\n', '')))
    assert get_iptables_version(iptables_path, module) == '1.4.20'



# Generated at 2022-06-13 05:40:59.110856
# Unit test for function flush_table
def test_flush_table():
    iptables_path = '/usr/bin/iptables'
    module = AnsibleModule(argument_spec={})
    params = dict(table='nat', chain='OUTPUT', ip_version='ipv4')
    flush_table(iptables_path, module, params)

# Generated at 2022-06-13 05:41:05.147860
# Unit test for function construct_rule
def test_construct_rule():
    ##########################################################################
    # Build result
    mod_args = dict(chain='INPUT',
                    protocol='tcp',
                    destination_port='8080',
                    jump='ACCEPT')
    rule = construct_rule(mod_args)
    assert rule == ['-w', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']

    mod_args = dict(chain='INPUT',
                    protocol='tcp',
                    destination_port='8080',
                    jump='ACCEPT',
                    ctstate='RELATED,ESTABLISHED')
    rule = construct_rule(mod_args)

# Generated at 2022-06-13 05:41:13.728292
# Unit test for function flush_table
def test_flush_table():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.ansible_test import AnsibleTest
    from ansible.module_utils.compat.version import LooseVersion
    ip_version = 'ipv4'
    table = 'filter'
    chain = 'INPUT'
    action = 'flush'
    iptables_path = BINS[ip_version]
    params = dict(ip_version=ip_version, table=table, chain=chain, action=action)
    test = AnsibleTest(ansible_version="2.7.12")
    iptables_path = test.get_bin_path(iptables_path, required=True)
    flush_table(iptables_path, test.get_module(), params)

# Generated at 2022-06-13 05:42:19.920155
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:29.119019
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils.basic import AnsibleModule
    class MockModule(object):
        def __init__(self):
            self.params = {'ip_version': 'ipv4', 'table': 'filter', 'policy': 'ACCEPT', 'chain': 'INPUT', 'wait': '10'}
            self.check_mode = False
        def run_command(self, cmd, check_rc=True):
            if self.params['policy'] == 'ACCEPT':
                return 0, 'Chain INPUT (policy ACCEPT)', ''
            elif self.params['policy'] == 'DROP':
                return 0, 'Chain INPUT (policy DROP)', ''
    module = MockModule()
    assert get_chain_policy('iptables', module, module.params) == module.params['policy']
# End of

# Generated at 2022-06-13 05:42:38.665411
# Unit test for function main

# Generated at 2022-06-13 05:42:39.338492
# Unit test for function append_rule
def test_append_rule():
    assert append_rule('iptables', '-A', True) == True


# Generated at 2022-06-13 05:42:41.353924
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('iptables',object,object) == object



# Generated at 2022-06-13 05:42:43.716246
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/usr/bin/iptables', 'INPUT', 'policy') == None



# Generated at 2022-06-13 05:42:53.236924
# Unit test for function construct_rule
def test_construct_rule():
    """
    Test for constructing rule for iptables-restore
    """
    import json
    import sys
    import os
    file_dir = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(file_dir, '..', '..', 'utils'))

    # Insert test libs
    import ansible_test
    ansible_test.gather_entries_from_file('iptables_construct_rule',
                                          __file__,
                                          'construct_rule',
                                          globals(),
                                          json.dumps)
    sys.path.pop(0)



# Generated at 2022-06-13 05:43:00.167148
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(
        argument_spec=dict(
            table='filter',
            chain='INPUT',
            ip_version='ipv4',
        ),
        supports_check_mode=True,
    )
    iptables_path = module.get_bin_path('iptables', required=True)
    if iptables_path is None:
        module.fail_json(msg='Unable to locate iptables binary')
    module.run_command([iptables_path, '-P', 'INPUT', 'ACCEPT'],
                       check_rc=True)
    policy = get_chain_policy(iptables_path, module, module.params)
    assert policy == 'ACCEPT'

# Generated at 2022-06-13 05:43:04.447417
# Unit test for function main

# Generated at 2022-06-13 05:43:17.697567
# Unit test for function main