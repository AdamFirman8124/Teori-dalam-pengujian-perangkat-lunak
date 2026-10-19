

# Generated at 2022-06-13 05:34:16.703285
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({'chain': 'INPUT', 'jump': 'ACCEPT'})
    params = module.params
    result = construct_rule(params)
    assert "-j ACCEPT" in result



# Generated at 2022-06-13 05:34:22.283403
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import os
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"ip_version":"ipv4","table":"filter","chain":"INPUT","set_module_args":1}'
    iptables_path = "/sbin/iptables"
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    chain_policy = get_chain_policy(iptables_path, module, module.params)
    assert chain_policy == "ACCEPT"



# Generated at 2022-06-13 05:34:30.341595
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        table='raw',
        chain='PREROUTING',
        action='-I',
        jump='NOTRACK',
    )
    expected = [
        'iptables',
        '-A', 'PREROUTING',
        '-j', 'NOTRACK'
    ]
    assert push_arguments('iptables', '-A', params) == expected

    assert push_arguments('ip6tables', '-A', params) == [
        'ip6tables',
        '-A', 'PREROUTING',
        '-j', 'NOTRACK'
    ]


# Generated at 2022-06-13 05:34:38.110445
# Unit test for function get_chain_policy
def test_get_chain_policy():
    def _ansible_module_wrapper(params):
        class _ModuleWrap(object):
            def run_command(self, cmd, check_rc):
                return 0, 'Chain test (policy DROP)', None
        return _ModuleWrap()

    assert get_chain_policy('failed', _ansible_module_wrapper({'chain': 'test'}), {'table': 'filter', 'chain': 'test'}) == 'DROP'



# Generated at 2022-06-13 05:34:46.478114
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class Args:
        chain = "test"
        table = "filter"

    class Module:
        run_command = lambda self, cmd, check_rc=False: (0, "Chain {} (policy ACCEPT)\n", "")
        params = Args()

    assert get_chain_policy("iptables", Module(), Module.params) == "ACCEPT"
    Module.run_command = lambda self, cmd, check_rc=False: (0, "Chain {} (policy DROP)\n", "")
    assert get_chain_policy("iptables", Module(), Module.params) == "DROP"
    Module.run_command = lambda self, cmd, check_rc=False: (0, "Chain {} (policy)\n", "")
    assert get_chain_policy("iptables", Module(), Module.params) is None



# Generated at 2022-06-13 05:34:59.176029
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('iptables', '') == '1.6.1'
    assert get_iptables_version('iptables', 'iptables v1.6.1 (nf_tables)') == '1.6.1'
    assert get_iptables_version('iptables', 'iptables v1.6.1') == '1.6.1'

get_iptables_version('iptables', '') == '1.6.1'
get_iptables_version('iptables', 'iptables v1.6.1 (nf_tables)') == '1.6.1'
get_iptables_version('iptables', 'iptables v1.6.1') == '1.6.1'



# Generated at 2022-06-13 05:35:10.947577
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule({
        'ip_version': 'ipv4',
        'protocol': 'tcp',
        'destination': '10.10.10.10',
        'destination_port': '22',
        'ctstate': [ 'NEW', 'ESTABLISHED', 'RELATED' ],
        'comment': 'This is a comment',
        'jump': 'ACCEPT',
        }) == [
            '-p', 'tcp',
            '-d', '10.10.10.10',
            '-m', 'conntrack',
            '--ctstate', 'NEW,ESTABLISHED,RELATED',
            '-m', 'comment',
            '--comment', 'This is a comment',
            '-j', 'ACCEPT'
        ]



# Generated at 2022-06-13 05:35:25.154582
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({}, {})

# Generated at 2022-06-13 05:35:30.605508
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        ip_version        = 'ipv4',
        protocol          = 'tcp',
        destination_port  = '1111',
        comment           = 'VyOS firewall',
        reject_with       = 'reject-with-tcp-reset',
        jump              = 'REJECT',
    )
    rule = construct_rule(params)
    assert(rule == [
        '-p', 'tcp',
        '--dport', '1111',
        '-j', 'REJECT',
        '--reject-with', 'reject-with-tcp-reset',
        '-m', 'comment',
        '--comment', '"VyOS firewall"'
    ])



# Generated at 2022-06-13 05:35:31.976332
# Unit test for function main
def test_main():
    iptables_path = '/sbin/iptables'
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:35:46.324967
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('iptables', {'run_command': [], 'check_rc': True}, {'chain': 'INPUT', 'policy': 'DROP'}) == None

# Generated at 2022-06-13 05:35:50.216668
# Unit test for function insert_rule
def test_insert_rule():
    module = AnsibleModule(argument_spec=dict())
    chain = 'INPUT'
    params = dict(table='filter', chain= chain, protocol='tcp', destination_port='8080', jump='ACCEPT', action='insert', rule_num='5')
    insert_rule('iptables', module, params)
    assert module.run_command.called
    assert module.run_command.call_args[0][0] == ['iptables', '-t', 'filter', '-I', chain, '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']
    assert module.run_command.call_args[0][1] == {'check_rc': True}


# Generated at 2022-06-13 05:35:54.740683
# Unit test for function append_rule
def test_append_rule():
    print('In test_append_rule() function')

    # Unit test for function append_rule()
    #
    # Replace iptables with mocked version
    #
    # - returns exit code 0 if rule is already present
    # - returns exit code 1 otherwise
    #
    params = dict(chain='INPUT', comment='foo')
    cmd = ['/usr/bin/iptables', '-t', 'filter', '-A', 'INPUT']
    for key in params:
        cmd.extend([key, params[key]])
    cmd.extend(['-m', 'comment', '--comment', 'foo'])
    cmd.extend(['-w', '10'])


# Generated at 2022-06-13 05:35:59.286583
# Unit test for function flush_table
def test_flush_table():
    iptables_path='iptables'
    module = AnsibleModule(argument_spec=dict(
        chain = dict(required = True, type = 'str'),
        table=dict(required=True, type='str'),
    ))

    chain = module.params['chain']
    table = module.params['table']
    cmd = push_arguments(iptables_path, '-F', dict(
        chain=chain,
        table=table,
    ))
    print(cmd)



# Generated at 2022-06-13 05:36:04.694538
# Unit test for function construct_rule
def test_construct_rule():
    if not hasattr(test_construct_rule, "errormsg"):
        test_construct_rule.errormsg = []
    if not hasattr(test_construct_rule, "cnt"):
        test_construct_rule.cnt = 0

    def check_rule(params, expect):
        global test_construct_rule
        rule = construct_rule(params)
        if sorted(rule) != sorted(expect):
            test_construct_rule.errormsg.append(
                "construct_rule({}) fails - {}".format(
                    params, rule))
        test_construct_rule.cnt += 1

    # Test all options.

# Generated at 2022-06-13 05:36:13.537724
# Unit test for function get_chain_policy
def test_get_chain_policy():
    table = "filter"
    chain = "INPUT"
    policy = "DROP"
    iptables_path = '/sbin/iptables'
    test_get_chain_policy_cmd = [iptables_path, '-t', table, '-P', chain, policy]
    test_get_chain_policy_cmd_out = "(policy DROP)"
    test_get_chain_policy_cmd_rc = 0
    test_get_chain_policy_params = dict(table='filter', chain='INPUT', policy='DROP', ip_version='ipv4')
    assert get_chain_policy(iptables_path, test_get_chain_policy_params) == "DROP"


# Generated at 2022-06-13 05:36:20.397986
# Unit test for function check_present
def test_check_present():
    module = mock.MagicMock()
    iptables_path = 'iptables'

# Generated at 2022-06-13 05:36:31.397158
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:38.383664
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:46.979147
# Unit test for function construct_rule
def test_construct_rule():
    test = dict()
    test['protocol'] = 'tcp'
    test['source'] = None
    test['destination'] = '1.2.3.4'
    test['match'] = None
    test['jump'] = 'ACCEPT'
    test['log_prefix'] = None
    test['log_level'] = None
    test['to_destination'] = None
    test['destination_ports'] = [80, 443]
    test['to_source'] = None
    test['goto'] = None
    test['in_interface'] = None
    test['out_interface'] = None
    test['fragment'] = None
    test['set_counters'] = None
    test['source_port'] = None
    test['destination_port'] = None
    test['to_ports'] = None


# Generated at 2022-06-13 05:37:09.996613
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        destination='8.8.8.8',
        match='tcp',
        name='test',
        protocol='tcp',
        jump='DROP',
        log_level='info',
        log_prefix='IPTABLES:INFO: ',
        limit='5/second',
        limit_burst='10',
        source='192.168.100.100',
        source_port='80',
        destination_port='8080',
        to_port='80',
        to_source='192.168.100.100',
        to_dstination='8.8.8.8',
        icmp_type='echo-request',
        uid_owner='root'
    )

# Generated at 2022-06-13 05:37:10.868755
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:37:18.025855
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(table='filter',
                  ip_version='ipv4',
                  chain='INPUT',
                  state='present',
                  action='-I',
                  rule_num='3',
                  protocol='tcp',
                  destination_port='8080',
                  jump='ACCEPT',
                  comment='Test comment')
    assert push_arguments(BINS['ipv4'], params['action'], params) == \
           ['iptables', '-t', params['table'], '-I', params['chain'], '3',
            '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT', '-m', 'comment',
            '--comment', 'Test comment']



# Generated at 2022-06-13 05:37:24.639601
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    append_match_flag(rule, 'match', '--some-match', True)
    assert rule == ['--some-match']
    rule = []
    append_match_flag(rule, 'negate', '--some-match', True)
    assert rule == ['!', '--some-match']
    rule = []
    append_match_flag(rule, None, '--some-match', True)
    assert rule == []
    rule = []
    append_match_flag(rule, 'match', '--some-match', False)
    assert rule == ['--some-match']
    rule = []
    append_match_flag(rule, 'negate', '--some-match', False)
    assert rule == ['--some-match']
    rule = []

# Generated at 2022-06-13 05:37:33.799914
# Unit test for function main

# Generated at 2022-06-13 05:37:41.313879
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(
        argument_spec=dict(
            chain=dict(required=True),
            policy=dict(required=False),
            ip_version=dict(choices=['ipv4', 'ipv6'], default='ipv4'),
            table=dict(default='filter'),
        )
    )
    flush_table(iptables_path, module, params)


# Generated at 2022-06-13 05:37:45.449468
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('test', 'module', {'table': 'test', 'chain': 'test', 'rule_num': 'test'}) == ['test', '-t', 'test', '-D', 'test', 'test']



# Generated at 2022-06-13 05:37:46.783636
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(
        None, None, dict(chain='INPUT', policy='ACCEPT')) == 'ACCEPT'



# Generated at 2022-06-13 05:37:56.951276
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:01.201363
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = 'iptables'
    params = {'chain': 'INPUT', 'table': 'filter', 'policy': 'DROP'}
    module = MockAnsibleModule(params)
    assert get_chain_policy(iptables_path, module, params) == 'DROP'
    params = {'chain': 'INPUT', 'table': 'filter', 'policy': 'ACCEPT'}
    assert get_chain_policy(iptables_path, module, params) == 'ACCEPT'



# Generated at 2022-06-13 05:38:16.018946
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-A', dict(table='filter',chain='INPUT',destination='1.1.1.1',jump='DROP')) == [
        'iptables',
        '-t',
        'filter',
        '-A',
        'INPUT',
        '-d',
        '1.1.1.1',
        '-j',
        'DROP',
    ]



# Generated at 2022-06-13 05:38:28.119382
# Unit test for function insert_rule
def test_insert_rule():
    import mock
    import textwrap
    module_obj = mock.Mock()
    module_obj.run_command.return_value = 0, '', ''
    param = {'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '22', 'jump': 'ACCEPT', 'action': 'insert', 'rule_num': 5}
    insert_rule('/usr/sbin/iptables', module_obj, param)
    assert module_obj.run_command.call_args[0][0] == ['iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--destination-port', '22', '-j', 'ACCEPT']

# end unit test


# Generated at 2022-06-13 05:38:31.883928
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'systest'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:38:37.560770
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = "/sbin/iptables"
    module = None
    params = dict (
    chain = "INPUT",
    policy = "DROP",
    table = "filter",
    ip_version = "ipv4",
    wait = None,
    )
    set_chain_policy(iptables_path, module, params)



# Generated at 2022-06-13 05:38:45.886823
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import module_utils.basic

    module = module_utils.basic.AnsibleModule(
        argument_spec={
            'chain': {'required': True, 'type': 'str'},
        },
    )
    assert get_chain_policy('iptables', module, dict(chain='INPUT', table='filter')) == 'ACCEPT'
    assert get_chain_policy('iptables', module, dict(chain='OUTPUT', table='filter')) == 'ACCEPT'
    assert get_chain_policy('iptables', module, dict(chain='FORWARD', table='filter')) == 'DROP'
    assert get_chain_policy('iptables', module, dict(chain='INPUT', table='nat')) == 'ACCEPT'

# Generated at 2022-06-13 05:38:53.207398
# Unit test for function push_arguments
def test_push_arguments():
    module_args = dict(
        ip_version='ipv4',
        table='nat',
        chain='PREROUTING',
        in_interface='eth0',
        protocol='tcp',
        match='tcp',
        destination_port=80,
        jump='REDIRECT',
        to_ports=8600,
        comment='Redirect web traffic to port 8600',
    )

# Generated at 2022-06-13 05:38:56.829569
# Unit test for function main
def test_main():
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 05:39:07.297140
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, cmd, check_rc=False):
            if 'iptables' in cmd:
                return 0, 'iptables v1.0.0', ''
            elif 'ip6tables' in cmd:
                return 0, 'ip6tables v1.0.0', ''
            else:
                return 1, '', ''

    params = dict(ip_version='ipv4')
    module = MockModule(params)
    result = get_iptables_version('iptables', module)
    assert result == '1.0.0'

   

# Generated at 2022-06-13 05:39:15.174047
# Unit test for function append_rule
def test_append_rule():
    params = dict(
        table='filter',
        chain='INPUT',
        action='append',
        source='8.8.8.8',
        jump='DROP',
        ip_version='ipv4',
    )
    iptables_path = BINS[params['ip_version']]
    cmd = push_arguments(iptables_path, '-A', params)
    return cmd == [iptables_path, '-t', params['table'], '-A', params['chain'], '-s', '8.8.8.8', '-j', 'DROP']



# Generated at 2022-06-13 05:39:16.216090
# Unit test for function append_rule
def test_append_rule():
    append_rule


# Generated at 2022-06-13 05:39:33.443305
# Unit test for function append_rule
def test_append_rule():
    iptables_path = "/sbin/iptables"
    module = None
    params = dict(chain="INPUT", ip_version="ipv4",
              table="filter", jump="ACCEPT")
    cmd = push_arguments(iptables_path, '-A', params)
    module.run_command(cmd, check_rc=True)

# Generated at 2022-06-13 05:39:45.666353
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:52.006332
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({})
    params = dict(
        ip_version='ipv4',
        protocol='tcp',
        source='192.168.1.1',
        destination='192.168.1.2',
        match=['tcp', 'state'],
        jump='ACCEPT',
        comment='myrule',
    )

# Generated at 2022-06-13 05:40:04.280912
# Unit test for function construct_rule
def test_construct_rule():
    def test_append_match_flag():
        rule = []
        append_match_flag(rule, 'match', '--syn', True)
        assert rule == ['--syn']
        rule = []
        append_match_flag(rule, 'negate', '--syn', True)
        assert rule == ['!', '--syn']
        rule = []
        append_match_flag(rule, 'negate', '--syn', False)
        assert rule == []

    def test_append_csv():
        rule = []
        append_csv(rule, ['80', '443'], '--dports')
        assert rule == ['--dports', '80,443']
        rule = []
        append_csv(rule, None, '--dports')
        assert rule == []


# Generated at 2022-06-13 05:40:17.151156
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        table='filter',
        chain='INPUT',
        rule_num=None,
        protocol=None,
        source=None,
        destination=None,
        jump=None,
        in_interface=None,
        out_interface=None,
        ctstate=None,
        source_port=None,
        destination_port=None,
        reject_with=None,
        icmp_type=None,
        to_destination=None,
        to_source=None,
        set_counters=None,
        comment=None,
        limit=None,
        limit_burst=None,
        syn=None,
        ip_version='ipv4',
    )
    action = '-A'
    iptables_path = BINS[params['ip_version']]



# Generated at 2022-06-13 05:40:30.778431
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
  # all flags
  params = dict(flags=['ACK', 'SYN', 'FIN', 'RST', 'URG', 'PSH'],
                flags_set=['ACK', 'SYN', 'FIN', 'RST', 'URG', 'PSH'])
  rule = []
  append_tcp_flags(rule, params, '--tcp-flags')
  assert rule == ['--tcp-flags', 'ACK,SYN,FIN,RST,URG,PSH', 'ACK,SYN,FIN,RST,URG,PSH']
  # select flags
  params = dict(flags=['ACK', 'SYN', 'FIN', 'RST', 'URG', 'PSH'],
                flags_set=['ACK', 'SYN', 'FIN'])
  rule = []
  append_tcp

# Generated at 2022-06-13 05:40:32.291777
# Unit test for function flush_table
def test_flush_table():
    '''
    Remove the state
    '''
    params = {'chain': 'INPUT', 'table': 'filter'}
    flush_table(BINS['ipv4'], None, params)


# Generated at 2022-06-13 05:40:38.377363
# Unit test for function check_present

# Generated at 2022-06-13 05:40:44.007773
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            ip_version=dict(type='str', default='ipv4', choices=['ipv4', 'ipv6']),
        ),
    )
    module.exit_json(changed=False, failed=False, ip_version=module.params['ip_version'])

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:40:51.763122
# Unit test for function get_chain_policy
def test_get_chain_policy():
    def test_func(module, *args, **kwargs):
        return 0, 'Chain INPUT\n pkts bytes target     prot opt in     out     source               destination          \n(policy ACCEPT)', ''
    cmd = push_arguments('iptables', '-L', 'INPUT', make_rule=False)
    result = get_chain_policy('iptables', test_func, cmd)
    assert result == 'ACCEPT'


# Generated at 2022-06-13 05:41:12.807931
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:18.703600
# Unit test for function push_arguments

# Generated at 2022-06-13 05:41:29.728942
# Unit test for function remove_rule

# Generated at 2022-06-13 05:41:35.589170
# Unit test for function push_arguments

# Generated at 2022-06-13 05:41:45.684816
# Unit test for function check_present
def test_check_present():
    assert check_present([], mock_config, 'INPUT', {'protocol': 'tcp', 'destination_port': '22'}) == True
    assert check_present([], mock_config, 'INPUT', {'protocol': 'tcp', 'destination_port': '47'}) == False
    assert check_present([], mock_config, 'INPUT', {'protocol': 'tcp', 'destination_port': '22', 'ctstate': ['NEW']}) == False
    assert check_present([], mock_config, 'INPUT', {'protocol': 'tcp', 'destination_port': '22', 'ctstate': ['NEW', 'ESTABLISHED']}) == True

# Generated at 2022-06-13 05:41:46.801364
# Unit test for function append_rule
def test_append_rule():
    module = AnsibleModule({})

# Generated at 2022-06-13 05:41:47.856984
# Unit test for function append_rule
def test_append_rule():
    append_rule('iptables', 'iptables', '-A', params)



# Generated at 2022-06-13 05:41:49.154745
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy("/sbin/iptables","mock_module","params") == "ACCEPT"


# Generated at 2022-06-13 05:41:54.421155
# Unit test for function main

# Generated at 2022-06-13 05:42:05.010917
# Unit test for function remove_rule
def test_remove_rule():
    """
    test remove_rule function
    """

# Generated at 2022-06-13 05:42:27.800515
# Unit test for function flush_table
def test_flush_table():
    flush_table('test', 'test', 'test')



# Generated at 2022-06-13 05:42:34.068296
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', 'module', {'chain': 'INPUT'}) == 'ACCEPT'
    assert get_chain_policy('iptables', 'module', {'chain': 'FORWARD'} ) == None
    assert get_chain_policy('iptables', 'module', {'chain': 'OUTPUT'}) == 'ACCEPT'


# Generated at 2022-06-13 05:42:40.976551
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(chain='INPUT')) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(chain='FORWARD')) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(chain='OUTPUT')) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(chain='FOOBAR')) == 'RETURN'



# Generated at 2022-06-13 05:42:46.907259
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(argument_spec=dict(
        table=dict(type='str', default='filter'),
        chain=dict(type='str', default='INPUT'),
    ))

# Generated at 2022-06-13 05:42:52.181118
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain="INPUT",
        protocol="tcp",
        destination_port="22",
        ctstate="NEW",
        syn="match",
        jump="ACCEPT",
        comment="Accept new SSH connections.",
    )

    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp',
        '-m', 'conntrack',
        '--ctstate', 'NEW',
        '--syn',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', 'Accept new SSH connections.',
    ]


# Generated at 2022-06-13 05:42:58.648876
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('/sbin/iptables', '-A', dict(
        ip_version='ipv4',
        jump='ACCEPT',
        table='nat',
        chain='INPUT')) == [
            '/sbin/iptables',
            '-t', 'nat',
            '-A', 'INPUT',
            '-p', 'tcp',
            '--dport', '80',
            '-j', 'ACCEPT']

# Generated at 2022-06-13 05:43:02.917904
# Unit test for function construct_rule
def test_construct_rule():
    def rule_test(testcase):
        params = testcase['params']

        rule = construct_rule(params)
        if testcase.get('skip_msg'):
            return True

        if len(rule) != len(testcase['expected']):
            print('expected: {}'.format(testcase['expected']))
            print('actual: {}'.format(rule))
            return False

        for i, val in enumerate(testcase['expected']):
            if val != rule[i]:
                print('expected: {}'.format(testcase['expected']))
                print('actual: {}'.format(rule))
                return False

        return True


# Generated at 2022-06-13 05:43:06.068880
# Unit test for function get_chain_policy
def test_get_chain_policy():
    out = (
        'Chain INPUT (policy DROP 0 packets, 0 bytes)')
    result = re.search(r'\(policy ([A-Z]+)\)', out)
    assert result.group(1) == 'DROP'
    out = (
        'Chain INPUT (policy!'
    )
    result = re.search(r'\(policy ([A-Z]+)\)', out)
    assert result is None



# Generated at 2022-06-13 05:43:18.449977
# Unit test for function construct_rule
def test_construct_rule():
    test_params = dict(
        chain='INPUT',
        source='8.8.8.8',
        jump='DROP',
        table='filter',
        ip_version='ipv4'
    )
    assert construct_rule(test_params) == ['--table', 'filter', '-A', 'INPUT', '-s', '8.8.8.8', '-j', 'DROP']
    test_params = dict(
        chain='INPUT',
        match='tcp',
        protocol='tcp',
        destination_port=80,
        jump='REJECT',
        table='filter',
        ip_version='ipv4'
    )

# Generated at 2022-06-13 05:43:29.945103
# Unit test for function construct_rule