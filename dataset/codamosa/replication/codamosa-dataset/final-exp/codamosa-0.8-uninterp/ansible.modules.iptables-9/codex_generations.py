

# Generated at 2022-06-13 05:34:29.732778
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-A', {
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'rule_num': None,
        'source': '127.0.0.1',
        'jump': 'ACCEPT',
        }
    ) == [
        'iptables', '-t', 'filter', '-A', 'INPUT',
        '-s', '127.0.0.1', '-j', 'ACCEPT'
    ]


# Generated at 2022-06-13 05:34:39.904228
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:34:51.634750
# Unit test for function construct_rule

# Generated at 2022-06-13 05:35:01.299899
# Unit test for function push_arguments
def test_push_arguments():
    from distutils.version import StrictVersion
    # pre Ansible 2.9.0

# Generated at 2022-06-13 05:35:13.159908
# Unit test for function construct_rule
def test_construct_rule():
    mod = AnsibleModule(argument_spec=get_argument_spec())

# Generated at 2022-06-13 05:35:25.025799
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # test with a non-existent chain
    ipv4_policy = get_chain_policy('iptables', {}, {
        'table': 'filter',
        'chain': 'this-chain-does-not-exist',
    })
    assert ipv4_policy is None, 'Unexpected result for a non-existent chain.'

    # test with an existing chain
    ipv4_policy = get_chain_policy('iptables', {}, {
        'table': 'filter',
        'chain': 'INPUT',
    })
    assert ipv4_policy == 'ACCEPT', \
        'Unexpected result for an existing default chain: %s' % ipv4_policy



# Generated at 2022-06-13 05:35:30.158416
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        state='present',
        ip_version='ipv4',
        in_interface='eth0',
        destination='192.168.1.1',
        destination_port='80',
        log_prefix='FOO',
        comment='COMMENT',
    )
    expected = [
        '-w',
        '-i', 'eth0',
        '-d', '192.168.1.1',
        '--dport', '80',
        '--comment', 'COMMENT',
        '-m', 'comment',
        '--log-prefix', 'FOO',
    ]
    assert construct_rule(params) == expected


# Generated at 2022-06-13 05:35:31.679587
# Unit test for function insert_rule
def test_insert_rule():
    check_null_present()



# Generated at 2022-06-13 05:35:33.272753
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    param = 'match'
    append_match_flag(rule, param, '--tcp-flags', False)
    assert rule == ['--tcp-flags']



# Generated at 2022-06-13 05:35:35.568225
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    test_rule = []
    test_param = {'flags': ['ACK', 'RST', 'SYN'], 'flags_set': ['FIN']}
    append_tcp_flags(test_rule, test_param, '-m tcp --tcp-flags')
    assert test_rule == ['-m tcp --tcp-flags', 'ACK,RST,SYN', 'FIN']



# Generated at 2022-06-13 05:36:13.944765
# Unit test for function push_arguments
def test_push_arguments():
    ipv4_table = 'INPUT'
    ipv4_chain = 'FORWARD'
    ipv4_action = '-I'
    ipv4_params = {
        'table': ipv4_table,
        'chain': ipv4_chain,
        'action': ipv4_action,
    }
    ipv4_expected = [
        'iptables',
        '-t',
        ipv4_table,
        ipv4_action,
        ipv4_chain,
    ]
    ipv4_result = push_arguments('iptables', ipv4_action, ipv4_params, False)
    assert ipv4_expected == ipv4_result


# Generated at 2022-06-13 05:36:26.145225
# Unit test for function push_arguments
def test_push_arguments():
    module = AnsibleModule({})
    params = dict(table='mangle', chain='INPUT', protocol='tcp',
             destination_port='80', jump='TEE', ip_version='ipv4')
    iptables_path = '/sbin/iptables'
    cmd = ['iptables', '-t', 'mangle', '-A', 'INPUT', '-p', 'tcp', '--destination-port', '80', '-j', 'TEE']
    assert push_arguments(iptables_path, '-A', params) == cmd
    # -m argument with limit option
    params['limit'] = '2/second'
    cmd.extend(['-m', 'limit', '--limit', '2/second'])

# Generated at 2022-06-13 05:36:33.080921
# Unit test for function check_present
def test_check_present():
    iptables_path = 'ipext'
    module = AnsibleModule({'table' : 'filter', 'chain' : 'INPUT', 'src_range' : '192.168.1.100-192.168.1.199', 'destination_port' : '80', 'jump' : 'ACCEPT'}, check_invalid_arguments=False)
    params = module.params
    assert check_present(iptables_path, module, params) == True




# Generated at 2022-06-13 05:36:34.455806
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec={})
    assert not check_present(None, module, {})



# Generated at 2022-06-13 05:36:35.016109
# Unit test for function set_chain_policy
def test_set_chain_policy():
    return True



# Generated at 2022-06-13 05:36:42.545451
# Unit test for function construct_rule
def test_construct_rule():
    params = {}
    params['wait'] = '5'
    params['protocol'] = 'tcp'
    params['source'] = '10.10.0.0/8'
    params['destination'] = '192.168.1.1'
    params['match'] = ['conntrack']
    params['jump'] = 'ACCEPT'
    params['log_prefix'] = 'IPTABLES:INFO: '
    params['log_level'] = 'info'
    params['to_destination'] = '192.168.1.2'
    params['destination_ports'] = ['80', '443', '8081:8083']
    params['to_source'] = '192.168.1.3'
    params['goto'] = None
    params['in_interface'] = 'eth0'
    params

# Generated at 2022-06-13 05:36:50.228990
# Unit test for function construct_rule
def test_construct_rule():
    test_chain = dict(
        chain='INPUT',
        protocol='tcp',
        destination='10.0.1.1',
        syn='match',
        comment='Test comment',
        icmp_type='echo-request',
        ip_version='ipv4',
    )
    expect_rule = ['--syn', '-p', 'tcp', '-d', '10.0.1.1', '-m', 'comment',
                   '--comment', 'Test comment', '--icmp-type', 'echo-request']
    assert construct_rule(test_chain) == expect_rule
# END OF Unit test for function construct_rule



# Generated at 2022-06-13 05:36:54.613563
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path='/sbin/iptables'
    module=AnsibleModule(argument_spec=dict())
    params = dict(
        table='filter',
        chain='INPUT',
        policy='DROP',
    )
    set_chain_policy(iptables_path, module, params)
# end of function test_set_chain_policy


# Generated at 2022-06-13 05:37:00.555078
# Unit test for function construct_rule
def test_construct_rule():
    assert(construct_rule(dict(
        source='192.168.1.1',
        protocol='tcp',
        destination_port='22',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
        ip_version='ipv4'
    )) == ['-w', '-p', 'tcp', '-s', '192.168.1.1', '-d', '--dport', '22',
           '-m', 'conntrack', '--ctstate', 'NEW', '--syn', '-j', 'ACCEPT',
           '-m', 'comment', '--comment', 'Accept new SSH connections.'])



# Generated at 2022-06-13 05:37:01.945226
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(iptables_path="/usr/sbin/iptables", module=module) == "INPUT"


# Generated at 2022-06-13 05:37:20.197622
# Unit test for function construct_rule
def test_construct_rule():
    pass
    # Test if this function is stable
    #params = dict(
    #    protocol="tcp",
    #    source=None,
    #    destination=None,
    #    match=None,
    #    jump=None,
    #    log_prefix=None,
    #    log_level=None,
    #    to_destination=None,
    #    destination_ports=None,
    #    to_source=None,
    #    goto=None,
    #    in_interface=None,
    #    out_interface=None,
    #    fragment=None,
    #    set_counters=None,
    #    source_port=None,
    #    destination_port=None,
    #    to_ports=None,
    #    set_dscp_mark=

# Generated at 2022-06-13 05:37:21.237511
# Unit test for function set_chain_policy
def test_set_chain_policy():
    function_set_chain_policy(iptables_path, module, params)



# Generated at 2022-06-13 05:37:32.155141
# Unit test for function main

# Generated at 2022-06-13 05:37:46.535177
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:49.499886
# Unit test for function append_rule
def test_append_rule():
    assert append_rule() == True


# Generated at 2022-06-13 05:38:04.179828
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:09.155168
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', None, dict(chain='INPUT', table='filter')) == 'ACCEPT'
    assert get_chain_policy('iptables', None, dict(chain='LOGGING', table='filter')) == 'ACCEPT'
    assert get_chain_policy('iptables', None, dict(chain='foobar', table='filter')) is None


# Generated at 2022-06-13 05:38:17.124281
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils.basic import AnsibleModule
    args = dict(
        table = 'mangle',
        chain = 'PREROUTING',
        ip_version = 'ipv4',
        source = '8.8.8.8',
        jump = 'DROP',
    )
    module = AnsibleModule(
        argument_spec=dict(
            table=dict(required=True, type='str'),
            chain=dict(required=True, type='str'),
            ip_version=dict(required=True, type='str', choices=['ipv4', 'ipv6']),
            source=dict(required=True, type='str'),
            jump=dict(required=True, type='str'),
        )
    )

# Generated at 2022-06-13 05:38:29.121350
# Unit test for function insert_rule
def test_insert_rule():
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT',
        'rule_num': '5'
    }
    cmd = push_arguments('iptables', '-I', params)
    assert cmd == ['iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT'
    }
    cmd = push_arguments

# Generated at 2022-06-13 05:38:39.910108
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:55.769222
# Unit test for function set_chain_policy
def test_set_chain_policy():
    module = AnsibleModule(dict(
        chain="INPUT",
        policy="ACCEPT",
    ))
    set_chain_policy("/bin/iptables", module, module.params)



# Generated at 2022-06-13 05:38:56.606720
# Unit test for function get_chain_policy
def test_get_chain_policy():
    get_chain_policy(None, None, {'chain': 'output', 'table': 'filter'})



# Generated at 2022-06-13 05:39:00.250008
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/usr/sbin/iptables'
    module = []
    params = ['ipv4', 'filter', 'INPUT', 'policy', 'ACCEPT']
    cmd = push_arguments(iptables_path, '-P', params, make_rule=False)
    print(cmd)
    cmd.append(params['policy'])
    module.run_command(cmd, check_rc=True)



# Generated at 2022-06-13 05:39:00.723677
# Unit test for function insert_rule
def test_insert_rule():
    return



# Generated at 2022-06-13 05:39:09.519917
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict()) == []
    assert construct_rule(dict(protocol='tcp')) == ['-p', 'tcp']
    assert construct_rule(dict(source='8.8.8.8')) == ['-s', '8.8.8.8']
    assert construct_rule(dict(destination='8.8.8.8')) == ['-d', '8.8.8.8']
    assert construct_rule(dict(match='tcp')) == ['-m', 'tcp']
    assert construct_rule(dict(match=['tcp', 'udp'])) == ['-m', 'tcp', '-m', 'udp']
    assert construct_rule(dict(jump='ACCEPT')) == ['-j', 'ACCEPT']

# Generated at 2022-06-13 05:39:18.873781
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:27.010966
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:33.852528
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('test', 'test', {"table": "filter", "chain": "INPUT"}) == None
    assert get_chain_policy('test', 'test', {"table": "filter", "chain": "CCCC"}) == None
    assert get_chain_policy('test', 'test', {"table": "filter", "chain": "FORWARD"}) == "ACCEPT"
    assert get_chain_policy('test', 'test', {"table": "filter", "chain": "OUTPUT"}) == "ACCEPT"
    assert get_chain_policy('test', 'test', {"table": "nat", "chain": "PREROUTING"}) == "ACCEPT"
    assert get_chain_policy('test', 'test', {"table": "nat", "chain": "INPUT"}) == "ACCEPT"
    assert get_

# Generated at 2022-06-13 05:39:36.580853
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = "/bin/iptables"
    module = {}
    params = {"table": "mangle", "ip_version": "ipv4", "chain": "OUTPUT", "jump": "DROP", "protocol": "tcp", "set_dscp_mark": "8"}
    cmd = push_arguments(iptables_path, '-D', params)

# Generated at 2022-06-13 05:39:41.639376
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(policy='ACCEPT')) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(policy='DROP')) == 'DROP'
    assert get_chain_policy(None, None, {}) is None



# Generated at 2022-06-13 05:40:11.032559
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {"chain": "INPUT", "table": "filter"}) == "DROP"
    assert get_chain_policy(None, None, {"chain": "OUTPUT", "table": "filter"}) == "ACCEPT"
    assert get_chain_policy(None, None, {"chain": "FORWARD", "table": "filter"}) == "DROP"
# /Unit test



# Generated at 2022-06-13 05:40:14.065220
# Unit test for function set_chain_policy
def test_set_chain_policy():
    mock_module = (
        'ansible.module_utils.basic'
    )
    cmd=["IPTABLES" , "-t", "iptables" , "-P" , "INPUT" , "ACCEPT"]
    mock_run_command(mock_module, cmd)
    params = dict(
        chain = 'INPUT',
        table = 'iptables',
        policy = 'ACCEPT'
    )
    set_chain_policy('IPTABLES', mock_module, params)

# Generated at 2022-06-13 05:40:21.748002
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:33.826677
# Unit test for function main

# Generated at 2022-06-13 05:40:34.977872
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('iptables', None) == '1.4.21'



# Generated at 2022-06-13 05:40:36.673710
# Unit test for function insert_rule
def test_insert_rule():
    assert insert_rule('iptables', '-I', 'INPUT')==['iptables', '-t', 'filter', '-I', 'INPUT']



# Generated at 2022-06-13 05:40:40.459813
# Unit test for function check_present
def test_check_present():
    params = dict(
        table='filter',
        chain='INPUT',
        action='present',
        source='10.0.0.0/26',
        jump='ACCEPT',
        state='present'
    )
    if check_present('/usr/bin/iptables', None, params):
        assert 0 == 1
    else:
        assert 1 == 1


# Generated at 2022-06-13 05:40:46.948490
# Unit test for function main
def test_main():
    test_args = {
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'flush': False,
        'rule': '-p tcp -s 1.2.3.4/24 --dport 80 -m state --state NEW -j ACCEPT',
        'state': 'present',
    }
    test_sys_exit = {
        'failed': False,
        'ip_version': 'ipv4',
        'table': 'filter',
        'changed': False,
        'chain': 'INPUT',
        'flush': False,
        'rule': '-p tcp -s 1.2.3.4/24 --dport 80 -m state --state NEW -j ACCEPT',
        'state': 'present',
    }

# Generated at 2022-06-13 05:40:52.591620
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, {'table': 'nat', 'chain': 'PREROUTING', 'policy': 'ACCEPT'}) == 'ACCEPT'
    assert get_chain_policy('iptables', {}, {'table': 'nat', 'chain': 'PREROUTING', 'policy': 'DROP'}) == 'DROP'



# Generated at 2022-06-13 05:40:58.109534
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'policy' : None}) is None
    assert get_chain_policy(None, None, {'policy' : 'ACCEPT'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'policy' : 'DROP'}) == 'DROP'
    assert get_chain_policy(None, None, {'policy' : 'INVALID'}) is None



# Generated at 2022-06-13 05:41:43.265859
# Unit test for function check_present
def test_check_present():
    class TestModule(object):
        def __init__(self, ip_version):
            self.ip_version = ip_version
        def run_command(self, cmd, check_rc=False):
            if cmd[0].endswith(BINS[self.ip_version]):
                if cmd == ['/sbin/' + BINS[self.ip_version], '-t', 'filter', '-C', 'INPUT', '-p', 'udp', '-m', 'conntrack', '--ctstate', 'INVALID', '-j', 'DROP']:
                    return (0, '', '')

# Generated at 2022-06-13 05:41:46.908820
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = 'iptables'
    module = AnsibleModule({})
    module.run_command = lambda cmd, check_rc=True: 0
    params = dict(chain='INPUT', table='filter')
    assert remove_rule(iptables_path, module, params) == None



# Generated at 2022-06-13 05:41:55.481430
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # Test case 1: policy is set
    module = AnsibleModule(argument_spec={})
    params = dict(
        table='filter',
        chain='INPUT',
        ip_version='ipv4',
    )
    current_policy = get_chain_policy('iptables', module, params)
    assert current_policy in ['ACCEPT', 'DROP']
    # Test case 2: policy is not set
    params = dict(
        table='filter',
        chain='guest',
        ip_version='ipv4',
    )
    current_policy = get_chain_policy('iptables', module, params)
    assert current_policy is None


# Generated at 2022-06-13 05:41:58.344589
# Unit test for function construct_rule
def test_construct_rule():
    params = {
        'chain': 'INPUT',
        'jump': 'DROP',
        'protocol': 'tcp',
        'source': '8.8.8.8',
    }
    assert construct_rule(params) == ['-p', 'tcp', '-s', '8.8.8.8', '-j', 'DROP']



# Generated at 2022-06-13 05:42:08.552475
# Unit test for function construct_rule
def test_construct_rule():
    '''
    NOTE:
    - This is not a "real test".
    - We cannot assert the result in a deterministic way,
    because iptables ordering is not deterministic.
    - The purpose of this test is simply to check
    if the rule is constructed without error.
    '''
    # @helpers.run_once
    def test_rule(params):
        return construct_rule(params)

    params = dict(
        ip_version='ipv4',
        state='present',
        protocol='tcp',
        destination='1.1.1.1',
        destination_port=500,
        jump='ACCEPT',
        comment='test comment',
    )
    assert test_rule(params)


# Generated at 2022-06-13 05:42:10.879844
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(module, 'INPUT') == 'DROP'

# Generated at 2022-06-13 05:42:17.031107
# Unit test for function construct_rule
def test_construct_rule():
    test_params = {
        'jump': 'DROP', 'ip_version': 'ipv4',
        'chain': 'FORWARD', 'table': 'filter',
    }
    assert construct_rule(test_params) == [
        '-w', '-p', '-m', 'comment', '--comment']


# Generated at 2022-06-13 05:42:24.632571
# Unit test for function check_present
def test_check_present():
    assert True == check_present(
        'iptables',
        dict(run_command=lambda cmd, check_rc=False: (0, '', '')),
        dict(chain='INPUT', table='nat'))
    assert False == check_present(
        'iptables',
        dict(run_command=lambda cmd, check_rc=False: (1, '', '')),
        dict(chain='INPUT', table='nat'))


# Generated at 2022-06-13 05:42:28.245691
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy({}, {}, {'chain': 'ACCEPT'}) == 'ACCEPT'
    assert not get_chain_policy({}, {}, {'chain': 'ACCE'})



# Generated at 2022-06-13 05:42:31.073352
# Unit test for function insert_rule
def test_insert_rule():
       assert insert_rule("iptables",module,params) == [
        'iptables',
        '--table',
        'nat',
        '--insert',
        'PREROUTING',
        '--rule-num',
        '5',
        '--protocol',
        'tcp',
        '--destination-port',
        '80',
        '--jump',
        'ACCEPT',
        '--comment',
        'Test insert rule'
]


# Generated at 2022-06-13 05:43:23.098916
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:32.516920
# Unit test for function construct_rule
def test_construct_rule():
    import textwrap
    params = dict(
        ip_version='ipv4',
        chain='INPUT',
        action='insert',
        in_interface='eth1',
        protocol='tcp',
        source='192.168.0.0/24',
        source_port='80',
        comment='Block incoming traffic from net 192.168.0.0/24',
        match='state',
        ctstate='NEW',
        match_set='admin_hosts',
        match_set_flags='dst',
        jump='DROP',
        comment='Matches all packets that are part of an existing connection.',
        uid_owner='1000-2000',
    )
    rule = construct_rule(params)
    # pretty-printing is done to help reviewing
    # and only to help reviewing.
    txt

# Generated at 2022-06-13 05:43:35.063068
# Unit test for function append_match_flag
def test_append_match_flag():
    assert append_match_flag('test') == 'test'


# Generated at 2022-06-13 05:43:44.231913
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:50.747491
# Unit test for function construct_rule