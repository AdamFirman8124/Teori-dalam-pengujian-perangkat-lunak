

# Generated at 2022-06-13 05:34:27.082754
# Unit test for function get_chain_policy
def test_get_chain_policy():
    params = dict(
        table='filter',
        chain='INPUT',
    )
    assert get_chain_policy('iptables', None, params) == 'ACCEPT'



# Generated at 2022-06-13 05:34:38.261586
# Unit test for function construct_rule
def test_construct_rule():
    '''Verify construct_rule returns expected output'''
    module_args = {}
    module_args.update(
        {'ip_version': 'ipv4',
         'chain': 'INPUT',
         'destination_port': '22',
         'jump': 'ACCEPT',
         'protocol': 'tcp',
         'state': 'present',
         'comment': 'Accept new SSH connections.'})
    rule = construct_rule(module_args)
    assert rule == ['-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept new SSH connections.']



# Generated at 2022-06-13 05:34:51.506756
# Unit test for function push_arguments
def test_push_arguments():
    expected = ['/bin/iptables',
                '-t', 'filter',
                '-I', 'INPUT',
                '-p', 'tcp',
                '-s', '1.1.1.1',
                '-d', '2.2.2.2']

# Generated at 2022-06-13 05:34:57.158336
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/usr/sbin/iptables'
    module = AnsibleModule(argument_spec=dict(ip_version=dict(type='str', default='ipv4')))
    module.params = dict(
        ip_version = 'ipv4',
        table = 'filter',
        chain = 'FORWARD',
        policy = 'ACCEPT',
        )
    module.run_command = lambda cmd, check_rc=True: [0, '', '']
    set_chain_policy(iptables_path, module, module.params)



# Generated at 2022-06-13 05:35:00.207705
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('', {}, {'chain': 'INPUT'}) == "ACCEPT"
    assert get_chain_policy('', {}, {'chain': 'OUTPUT'}) == "ACCEPT"
    assert get_chain_policy('', {}, {'chain': 'FORWARD'}) == "DROP"
    assert get_chain_policy('', {}, {'chain': 'MY_CUSTOM_CHAIN'}) == None



# Generated at 2022-06-13 05:35:12.069184
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:25.091216
# Unit test for function flush_table
def test_flush_table():
    from ansible.modules.network.firewall import flush_table
    class Module(object):
        def __init__(self):
            self.run_command = MagicMock()
            self.run_command.return_value = (0,"","")
    params = dict()
    params['chain'] = "INPUT"
    params['table'] = 'filter'
    params['ip_version'] = 'ipv4'
    module = Module()
    flush_table(BINS[params['ip_version']], module, params)
    module.run_command.assert_called_once_with(
        [BINS[params['ip_version']], '-t', 'filter', '-F', 'INPUT'], check_rc=True)



# Generated at 2022-06-13 05:35:29.145033
# Unit test for function construct_rule
def test_construct_rule():
    params = {'ip_version': 'ipv4', 'rule': '-A INPUT -s 127.0.0.3/32 -d 127.0.0.4/32 -m comment --comment "Ansible Test" -j DROP'}
    expected = ['-A', 'INPUT', '-s', '127.0.0.3/32', '-d', '127.0.0.4/32', '-m', 'comment', '--comment', 'Ansible Test', '-j', 'DROP']
    result = construct_rule(params)
    assert result == expected

# Generated at 2022-06-13 05:35:34.435102
# Unit test for function construct_rule

# Generated at 2022-06-13 05:35:45.131526
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:58.031669
# Unit test for function append_match_flag
def test_append_match_flag():
    res1=[]
    res2=[]
    append_match_flag(res1, 'match', '--match-mark', False)
    append_match_flag(res2, 'negate', '--syn', True)
    assert res1 == ['--match-mark'], "Failed"
    assert res2 == ['!', '--syn'], "Failed"


# Generated at 2022-06-13 05:35:59.776715
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version(BINS['ipv4'], AnsibleModule) == IPTABLES_WAIT_SUPPORT_ADDED



# Generated at 2022-06-13 05:36:06.933836
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    param = dict(flags=[],flags_set=['SYN','ACK','FIN','RST'])
    assert append_tcp_flags(rule,param,'--tcp-flags') == [rule.extend(['--tcp-flags', ','.join(param['flags']), ','.join(param['flags_set'])])]



# Generated at 2022-06-13 05:36:13.355613
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(b'iptables v1.10.0')
    fp.close()
    module = AnsibleModule()
    assert get_iptables_version(fp.name, module) == '1.10.0'



# Generated at 2022-06-13 05:36:25.534492
# Unit test for function main

# Generated at 2022-06-13 05:36:29.880542
# Unit test for function append_rule
def test_append_rule():
    module = {"run_command": return_true}
    params = {"table": "filter", "chain": "INPUT", "protocol": "tcp", "destination": "192.168.10.0/24", "destination_port": "80", "jump": "ACCEPT", "ip_version": "ipv4"}
    append_rule("/usr/sbin/iptables", module, params)

# Generated at 2022-06-13 05:36:32.633814
# Unit test for function set_chain_policy
def test_set_chain_policy():
    module_args = dict(
        chain='INPUT',
        policy='DROP',
    )
    module = AnsibleModule(argument_spec=module_args)
    set_chain_policy('/sbin/iptables', module, module_args)



# Generated at 2022-06-13 05:36:39.266497
# Unit test for function construct_rule
def test_construct_rule():
    from ansible.module_utils._text import to_bytes

# Generated at 2022-06-13 05:36:42.223883
# Unit test for function set_chain_policy
def test_set_chain_policy():
    params = {
        'chain': 'INPUT',
        'policy': 'DROP',
        'table': 'filter',
        'ip_version': 'ipv4',
    }
    set_chain_policy('iptables', None, params)



# Generated at 2022-06-13 05:36:48.581618
# Unit test for function append_match_flag
def test_append_match_flag():
    # Given
    rule = []
    # When
    append_match_flag(rule, 'match', '-p', True)
    # Then
    assert rule == ['-p']
    # When
    append_match_flag(rule, None, '-p', True)
    # Then
    assert rule == ['-p']
    # When
    append_match_flag(rule, 'negate', '--log-tcp-sequence', True)
    # Then
    assert rule == ['-p', '--log-tcp-sequence']



# Generated at 2022-06-13 05:37:14.504702
# Unit test for function push_arguments

# Generated at 2022-06-13 05:37:16.760748
# Unit test for function get_iptables_version
def test_get_iptables_version():
    args = dict(
        iptables_path='/usr/sbin/iptables',
        module=dict(
            run_command=lambda *args, **kwargs: (0, 'v1.2.3\n', ''),
        ),
    )
    assert get_iptables_version(**args) == '1.2.3'



# Generated at 2022-06-13 05:37:28.306969
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:32.113136
# Unit test for function check_present
def test_check_present():
    cmd = ['/sbin/iptables', '-C', 'INPUT', '-s', '1.1.1.1']
    rc, _, __ = module.run_command(cmd, check_rc=False)
    return (rc == 0)



# Generated at 2022-06-13 05:37:45.030946
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import tempfile
    import os
    import shutil
    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 05:37:58.677957
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:38:10.352799
# Unit test for function construct_rule
def test_construct_rule():
    params = {}
    params['ip_version'] = 'ipv4'
    params['wait'] = 1
    params['protocol'] = 'tcp'
    params['source'] = '1.1.1.1'
    params['destination'] = '2.2.2.2'
    params['match'] = 'match'
    params['jump'] = 'jump'
    params['log_prefix'] = 'IPTABLES:INFO: '
    params['log_level'] = 'info'
    params['to_destination'] = '3.3.3.3'
    params['destination_ports'] = [ 80, 443 ]
    params['to_source'] = '4.4.4.4'
    params['goto'] = 'goto'
    params['in_interface'] = 'eth0'


# Generated at 2022-06-13 05:38:13.940387
# Unit test for function append_rule
def test_append_rule():
    fake_module = type('', (), dict(run_command=lambda *args, **kwargs: (0, '', 0)))
    append_rule('iptables', fake_module, dict(chain='INPUT', table='filter'))



# Generated at 2022-06-13 05:38:16.308118
# Unit test for function get_iptables_version
def test_get_iptables_version():
    import ansible.module_utils.basic
    iptables_path = '/usr/sbin/iptables'
    iptables_version = get_iptables_version(iptables_path, AnsibleModule(argument_spec={}))
    assert iptables_version == '1.6.0'


# Generated at 2022-06-13 05:38:17.034506
# Unit test for function append_rule
def test_append_rule():
    assert append_rule(iptables_path='ip') == True



# Generated at 2022-06-13 05:38:35.493141
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    param = dict(
        flags=['SYN', 'ACK', 'RST', 'FIN'],
        flags_set=['SYN'],
    )
    flag = '--tcp-flags'
    append_tcp_flags(rule, param, flag)
    assert rule == ['--tcp-flags', 'SYN,ACK,RST,FIN', 'SYN']
test_append_tcp_flags()



# Generated at 2022-06-13 05:38:41.793381
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.compat.version import LooseVersion
    module = AnsibleModule(argument_spec={})
    result = get_iptables_version('iptables', module)
    assert (LooseVersion(result) >= LooseVersion('1.4'))
    assert (LooseVersion(result) < LooseVersion('2.0'))



# Generated at 2022-06-13 05:38:42.746220
# Unit test for function append_rule
def test_append_rule():
    assert False



# Generated at 2022-06-13 05:38:48.072921
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-D', dict(
        table='mangle',
        chain='PREROUTING',
        rule_num='1',
        protocol='tcp',
        jump='DROP',
        source='10.0.0.1')) == ['iptables', '-t', 'mangle', '-D', 'PREROUTING', '1', '-p', 'tcp', '-j', 'DROP', '-s', '10.0.0.1']



# Generated at 2022-06-13 05:38:49.357826
# Unit test for function remove_rule
def test_remove_rule():
    assert 1 == 1



# Generated at 2022-06-13 05:38:59.430840
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:11.590270
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module_args = {
        'ip_version': 'ipv4',
        'chain': 'RH-Firewall-1-INPUT',
        'table': 'filter',
        'chain_policy': 'ACCEPT'
    }
    module = AnsibleModule(argument_spec=dict(
        chain=dict(required=True),
        table=dict(required=True),
        ip_version=dict(choices=['ipv4', 'ipv6']),
        chain_policy=dict(required=True),
    ), supports_check_mode=True)
    ip_version = module.params['ip_version']
    bin_path = BINS[ip_version]
    policy = get_chain_policy(bin_path, module, module.params)
    if policy == module.params['chain_policy']:
        module

# Generated at 2022-06-13 05:39:20.225983
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = 'iptables'
    action = '-I'
    params = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        rule_num=5
    )
    cmd = push_arguments(iptables_path, action, params)

# Generated at 2022-06-13 05:39:30.936571
# Unit test for function flush_table
def test_flush_table():
    fake_module = AnsibleModule(
        argument_spec=dict(
            ip_version=dict(default="ipv4", type="str"),
            table=dict(default="filter", type="str"),
            chain=dict(default=None, type="str"),
        )
    )

    params = fake_module.params
    test_params = {
        'ip_version': "ipv4",
        'table': "filter",
        'chain': "test",
    }
    assert test_params == params
    iptables_path = BINS[params['ip_version']]
    flush_table(iptables_path, fake_module, params)
    assert ['iptables', '-t', 'filter', '-F', 'test'] == fake_module.run_command_args
test_flush_table()




# Generated at 2022-06-13 05:39:38.842606
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    expected = ['--tcp-flags', 'ALL', 'ACK,RST,SYN,FIN']
    assert (append_tcp_flags([], {
                            'flags': ['ALL'],
                            'flags_set': ['ACK', 'RST', 'SYN', 'FIN']
                         }, '--tcp-flags') == expected) is True



# Generated at 2022-06-13 05:39:53.169049
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {
        'chain': 'FILTER',
        'table': 'filter',
    }) == 'ACCEPT'



# Generated at 2022-06-13 05:40:02.014837
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
        wait='5',
        ip_version='ipv4'
    )) == [
        '-w', '5',
        '-p', 'tcp',
        '--destination-port', '80',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', 'Accept new SSH connections.'
    ]



# Generated at 2022-06-13 05:40:14.990905
# Unit test for function main

# Generated at 2022-06-13 05:40:17.535203
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_version = get_iptables_version('iptables', None)
    assert re.match(r'^[\d.]+$', iptables_version)



# Generated at 2022-06-13 05:40:31.127487
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    # Define module parameters

# Generated at 2022-06-13 05:40:37.295061
# Unit test for function check_present

# Generated at 2022-06-13 05:40:39.073904
# Unit test for function get_chain_policy
def test_get_chain_policy():
    print(get_chain_policy('iptables', None, {'ip_version': 'ipv4', 'chain': 'INPUT'}))


# Generated at 2022-06-13 05:40:51.983710
# Unit test for function insert_rule
def test_insert_rule():
    iptables_bin = 'iptables'
    iptables_version = LooseVersion('1.4.20')

# Generated at 2022-06-13 05:40:59.771728
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:01.375066
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy("/usr/bin/iptables",None,{"table":"filter","chain":"INPUT"}) == "ACCEPT"


# Generated at 2022-06-13 05:41:29.221343
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='8.8.8.8',
        jump='DROP',
        comment='My test',
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp',
        '-s', '8.8.8.8',
        '-j', 'DROP',
        '-m', 'comment',
        '--comment', 'My test',
    ]
    params = dict(
        protocol='tcp',
        source='8.8.8.8',
        jump='DROP',
        comment='My test',
        ip_version='ipv4',
    )
    rule = construct_rule(params)

# Generated at 2022-06-13 05:41:39.933095
# Unit test for function check_present

# Generated at 2022-06-13 05:41:45.854062
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    module = AnsibleModule({})
    if to_text(get_iptables_version(get_bin_path('iptables', opt_dirs=['/sbin']), module)).strip() == '1.6.1':
        assert True
    else:
        assert False


# Generated at 2022-06-13 05:41:50.885016
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # Testing the rule INPUT
    ret1 = get_chain_policy(None, None, {'chain':'INPUT', 'policy':'ACCEPT'})
    assert ret1 == "ACCEPT"
    # Testing the rule OUTPUT
    ret2 = get_chain_policy(None, None, {'chain':'OUTPUT', 'policy':'ACCEPT'})
    assert ret2 == "ACCEPT"
    # Testing the rule FORWARD
    ret3 = get_chain_policy(None, None, {'chain':'FORWARD', 'policy':'DROP'})
    assert ret3 == "DROP"



# Generated at 2022-06-13 05:42:02.802062
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule('')
    ans = check_present('iptables', module,
        {'protocol': 'tcp', 'table': 'filter', 'chain': 'INPUT', 'jump': 'DROP'})
    assert not ans
    assert module.run_command.call_count == 1
    assert module.run_command.call_args[0] == ['iptables',
        '-t', 'filter', '-C', 'INPUT', '-p', 'tcp', '-j', 'DROP']
    module.run_command.reset_mock()
    module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 05:42:10.051550
# Unit test for function construct_rule
def test_construct_rule():
    param = dict(
        protocol='tcp',
        source='8.8.8.8',
        jump='DROP',
        log_prefix="IPTABLES:INFO: ",
        source_port='22',
        destination_port='22',
        limits='2/sec',
        limit_burst='5',
        uid_owner='!root',
        gid_owner='root',
        reject_with='icmp-port-unreachable',
        icmp_type='echo-request',
        comment='test comment',
        wait=5,
        syn='match',
        ip_version='ipv4',
        action='insert',
    )

# Generated at 2022-06-13 05:42:13.394028
# Unit test for function flush_table
def test_flush_table():
    iptables_path = ''
    module = ''
    params = []
    assert(flush_table(iptables_path, module, params) == 0)



# Generated at 2022-06-13 05:42:26.297601
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:37.195201
# Unit test for function main

# Generated at 2022-06-13 05:42:46.306636
# Unit test for function get_chain_policy
def test_get_chain_policy():
    data = {
        "table": "filter",
        "chain": "INPUT",
        "policy": None,
        "ip_version": "ipv4"
    }
    module = AnsibleModule({'table': 'filter', 'chain': 'INPUT', 'policy': None, 'ip_version': 'ipv4'})
    iptables_path = BINS[data['ip_version']]
    assert get_chain_policy(iptables_path, module, data) == "ACCEPT"



# Generated at 2022-06-13 05:43:46.177964
# Unit test for function check_present
def test_check_present():
    iptables_path = '/usr/bin/iptables'
    module = AnsibleModule()
    params = {
        'table': 'filter',
        'rule_num': '1',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'source': '8.8.8.8',
        'jump': 'DROP'
    }
    assert check_present(iptables_path, module, params) == True


# Generated at 2022-06-13 05:43:49.059877
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {
        "chain": "INPUT",
        "policy": "ACCEPT"
    }) == "ACCEPT"
    # not found
    assert get_chain_policy(None, None, {
        "chain": "INPUT",
        "policy": "DROP"
    }) is None



# Generated at 2022-06-13 05:43:54.694722
# Unit test for function construct_rule