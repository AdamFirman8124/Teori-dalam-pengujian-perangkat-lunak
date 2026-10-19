

# Generated at 2022-06-13 05:34:39.822601
# Unit test for function remove_rule
def test_remove_rule():
  from ansible.module_utils._text import to_text
  from ansible.modules.network.iptables import (
      HAS_IPTABLES_WAIT,
      HAS_IPTABLES_WAIT_WITH_SECONDS)
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils.common.text.converters import to_bytes
  from ansible.module_utils.common.text.converters import to_text


# Generated at 2022-06-13 05:34:40.574546
# Unit test for function set_chain_policy
def test_set_chain_policy():
    pass



# Generated at 2022-06-13 05:34:46.073663
# Unit test for function push_arguments
def test_push_arguments():
    result = push_arguments('iptables', '-I', {'table': 'nat', 'chain': 'OUTPUT', 'rule_num': 5, 'ctstate': 'foo'})
    assert result == ['iptables', '-t', 'nat', '-I', 'OUTPUT', '5', '-m', 'conntrack', '--ctstate', 'foo']



# Generated at 2022-06-13 05:34:48.732037
# Unit test for function set_chain_policy
def test_set_chain_policy():
    ipt = 'iptables'
    module = AnsibleModule({'chain': 'INPUT', 'policy': 'ACCEPT'})
    
    cmd = push_arguments(ipt, '-P', module.params, make_rule=False)
    cmd.append(module.params['policy'])
    print(cmd)
test_set_chain_policy()


# Generated at 2022-06-13 05:34:57.104770
# Unit test for function get_chain_policy
def test_get_chain_policy():
    test_module = AnsibleModule({
        'argument_spec': {},
        'name': 'ansible',
    })
    test_iptables_path = '/usr/sbin/iptables'
    test_params = dict(
        table='filter',
        chain='INPUT',
    )
    expected_result = 'ACCEPT'
    result = get_chain_policy(test_iptables_path, test_module, test_params)
    assert result == expected_result
    test_params = dict(
        table='filter',
        chain='FORWARD',
    )
    expected_result = 'DROP'
    result = get_chain_policy(test_iptables_path, test_module, test_params)
    assert result == expected_result

# Generated at 2022-06-13 05:35:05.307747
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(
        argument_spec=dict(
            chain=dict(type='str', required=True),
            table=dict(type='str', default='filter'),
            policy=dict(type='str', required=True, choices=['ACCEPT', 'DROP', 'QUEUE', 'RETURN']),
            wait=dict(type='str'),
            ip_version=dict(type='str', required=True),
        )
    )
    params = dict(
        chain="INPUT",
        table='filter',
        policy='DROP',
        wait=None,
        ip_version='ipv4',
    )
    set_chain_policy(iptables_path, module, params)


# Generated at 2022-06-13 05:35:17.813332
# Unit test for function remove_rule

# Generated at 2022-06-13 05:35:27.100880
# Unit test for function remove_rule
def test_remove_rule():
    from iptables import Iptables

    iptables = Iptables(module='', use_ipv6=False)
    params=dict()
    params['chain'] = "INPUT"
    params['table'] = "filter"
    params['protocol'] = None
    params['state'] = "present"
    params['jump'] = "ACCEPT"
    params['ip_version'] = "ipv4"
    params['destination_port'] = None
    iptables_path = '/sbin/iptables-save'
    cmd = remove_rule(iptables_path,  iptables.module, params)

# Generated at 2022-06-13 05:35:35.366711
# Unit test for function append_rule
def test_append_rule():
    cmd = []
    cmd.extend(['-t', 'filter'])
    cmd.extend(['-A', 'INPUT'])
    cmd.extend(['-p', 'tcp'])
    cmd.extend(['-s', '192.168.1.1'])
    cmd.extend(['-d', '192.168.2.1'])
    cmd.extend(['-j', 'DROP'])
    cmd.extend(['-m', 'comment', '--comment', 'Testing'])
    return cmd;




# Generated at 2022-06-13 05:35:45.673211
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule, env_fallback
    from AnsibleModule_iptables import IPTABLES_ARGUMENT_SPEC
    module = AnsibleModule(argument_spec=IPTABLES_ARGUMENT_SPEC,
                           supports_check_mode=True)

    module.params = {
        'action': 'present',
        'chain': 'INPUT',
        'comment': 'test',
        'ip_version': 'ipv4',
        'jump': 'DROP',
        'protocol': 'tcp',
        'state': 'present',
        'table': 'filter',
    }
    rc = check_present(BINS['ipv4'], module, module.params)

# Generated at 2022-06-13 05:36:02.113969
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({})
    test_params = dict(
        protocol='tcp',
        source='192.168.1.1',
        destination='192.168.1.2',
        match=['tcp', 'state'],
        ctstate=['NEW', 'ESTABLISHED'],
        jump='ACCEPT',
        ip_version='ipv4',
        limit=None,
        limit_burst=None,
        reject_with=None,
        icmp_type=None,
        wait=None)
    rule = construct_rule(test_params)

# Generated at 2022-06-13 05:36:08.125062
# Unit test for function insert_rule
def test_insert_rule():
    assert(insert_rule("C:/Program Files/Git/usr/bin/iptables.exe", "ansible.module_utils.basic", {'chain': 'INPUT', 'action': 'insert', 'ip_version': 'ipv4', 'protocol': 'tcp', 'match': ['tcp'], 'destination_port': 8080, 'jump': 'ACCEPT', 'rule_num': 5}) == 0)

# Generated at 2022-06-13 05:36:13.225237
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = '/sbin/iptables'
    fake_module = []
    params = {
        'table': 'filter',
        'chain': 'INPUT'
    }
    fake_module.run_command = lambda x: (0, '', '')
    out = get_chain_policy(iptables_path, fake_module, params)
    assert out == 'ACCEPT', out



# Generated at 2022-06-13 05:36:14.813105
# Unit test for function remove_rule
def test_remove_rule():
    assert not remove_rule(None, None, None)



# Generated at 2022-06-13 05:36:18.915064
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    p = dict(flags=[ 'ALL', 'NONE' ], flags_set=[ 'ACK', 'SYN', 'RST' ])
    r = ['--tcp-flags', ','.join(p['flags']), ','.join(p['flags_set'])]
    t_rule = []
    append_tcp_flags(t_rule, p, '--tcp-flags')
    assert t_rule == r


# Generated at 2022-06-13 05:36:20.217790
# Unit test for function append_rule
def test_append_rule():
    append_rule('iptables', None, 'INPUT', '-p', 'tcp', '-j', 'ACCEPT')



# Generated at 2022-06-13 05:36:23.376250
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = "/usr/bin/iptables"
    action = "flush"
    params = dict(
        chain="INPUT",
        policy="DROP"
    )
    from mock import MagicMock
    module = MagicMock()
    module.run_command = MagicMock()
    set_chain_policy(iptables_path, module, params)
    module.run_command.assert_called_once_with(['/usr/bin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP'])


# Generated at 2022-06-13 05:36:33.734369
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments("/usr/bin/iptables", "-A", {"table": "nat", "chain": "PREROUTING", "protocol": "tcp", "destination_port": "80", "jump": "REDIRECT", "to_ports": "8600", "comment": "Redirect web traffic to port 8600"}, True) == ['/usr/bin/iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '--dport', '80', '-j', 'REDIRECT', '--to-ports', '8600', '-m', 'comment', '--comment', '"Redirect web traffic to port 8600"']

# Generated at 2022-06-13 05:36:38.806933
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(argument_spec=dict(
        ip_version=dict(required=False, choices=['ipv4', 'ipv6'], default='ipv4'),
        table=dict(required=False, choices=['filter', 'nat', 'mangle', 'raw', 'security']),
        chain=dict(required=True),
    ), supports_check_mode=True)
    module.params = {'ip_version':'ipv4', 'table':'filter', 'chain':'INPUT'}
    flush_table('iptables', module, module.params)



# Generated at 2022-06-13 05:36:44.225964
# Unit test for function check_present
def test_check_present():
    assert check_present('/sbin/iptables', {'run_command':[ 0, '-C', '']}, {
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': 22,
        'ctstate': 'NEW',
        'syn': 'match',
        'jump': 'ACCEPT',
        'comment': 'Accept new SSH connections.',
        'table': 'filter',
        'rule_num': None
    }) == True


# Generated at 2022-06-13 05:37:02.283330
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy("iptables", "module", "params") == "ACCEPT"


# Generated at 2022-06-13 05:37:14.054862
# Unit test for function insert_rule
def test_insert_rule():
    test_params = {'chain': 'INPUT',
                   'destination_port': '80',
                   'ip_version': 'ipv4',
                   'jump': 'ALLOW',
                   'protocol': 'tcp',
                   'rule_num': '5',
                   'table': 'filter',
                   'wait': '10'}
    cmd = ['/sbin/iptables', '-t', test_params['table'], '-I', test_params['chain'], '5']
    cmd.extend([
        '-p', test_params['protocol'],
        '--destination-port', test_params['destination_port'],
        '-j', test_params['jump'],
        '-w', test_params['wait']])
    return cmd



# Generated at 2022-06-13 05:37:15.740596
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = '/sbin/iptables'
    params = {
        'chain': 'INPUT',
        'table': 'filter'
    }
    policy = get_chain_policy(iptables_path, module, params)
    assert policy == 'DROP'



# Generated at 2022-06-13 05:37:22.862323
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    param = 'match'
    flag = '--syn'
    append_match_flag(rule, param, flag, True)
    assert len(rule) == 1
    assert rule[0] == '--syn'
    rule = []
    param = 'negate'
    flag = '--syn'
    append_match_flag(rule, param, flag, True)
    assert len(rule) == 2
    assert rule[0] == '!'
    assert rule[1] == '--syn'
    rule = []
    param = 'fail'
    flag = '--syn'
    append_match_flag(rule, param, flag, True)
    assert len(rule) == 0



# Generated at 2022-06-13 05:37:28.122145
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = list()
    append_match_flag(rule, 'match', '--syn', True)
    assert rule == ['--syn']
    rule = list()
    append_match_flag(rule, 'negate', '--syn', True)
    assert rule == ['!', '--syn']
    rule = list()
    append_match_flag(rule, None, '--syn', True)
    assert not rule
    rule = list()
    append_match_flag(rule, 'match', '--syn', False)
    assert rule == ['--syn']
    with pytest.raises(Exception) as e:
        append_match_flag(rule, 'negate', '--syn', False)
    assert 'Unknown match value: "negate"' in str(e.value)



# Generated at 2022-06-13 05:37:30.205470
# Unit test for function remove_rule
def test_remove_rule():
    # This function is not tested because the remove_rule function does not return a value.
    return



# Generated at 2022-06-13 05:37:36.011574
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule({'ip_version': 'ipv4'})
    assert get_chain_policy('/sbin/iptables', module, {'table': 'filter', 'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:37:47.475837
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination='www.example.org',
        jump='REJECT',
        source='192.168.1.2',
        comment='Block tcp to www.example.org from 192.168.1.2',
    )
    rule = construct_rule(params)
    assert rule == ['-A', 'INPUT', '-s', '192.168.1.2', '-d', 'www.example.org', '-p', 'tcp', '-j', 'REJECT', '-m', 'comment', '--comment', 'Block tcp to www.example.org from 192.168.1.2']



# Generated at 2022-06-13 05:37:58.634229
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = "iptables"
    params = {
    'table': 'filter',
    'chain': 'INPUT',
    'protocol': 'tcp',
    'destination_port': '8080',
    'jump': 'ACCEPT',
    'action': 'insert',
    'rule_num': '5'
    }
    cmd = push_arguments(iptables_path, '-I', params)
    assert cmd == ['iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--destination-port', '8080', '-j', 'ACCEPT']

# Generated at 2022-06-13 05:38:10.352511
# Unit test for function get_chain_policy
def test_get_chain_policy():
    param_1 = dict(
        iptables_path='iptables',
        chain='INPUT',
        table='filter',
        action='-L',
        ip_version='ipv4',
    )
    test_output_1 = "Chain INPUT (policy ACCEPT)"
    param_2 = dict(
        iptables_path='iptables',
        chain='FORWARD',
        table='filter',
        action='-L',
        ip_version='ipv4',
    )
    test_output_2 = "Chain FORWARD (policy ACCEPT)"
    param_3 = dict(
        iptables_path='iptables',
        chain='OUTPUT',
        table='filter',
        action='-L',
        ip_version='ipv4',
    )
    test_output_3

# Generated at 2022-06-13 05:38:24.935795
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        match='tcp',
        destination_port='443',
        jump='ACCEPT',
        comment='test'
    )
    rule = construct_rule(params)
    expected_rule = ['-p', 'tcp', '-m', 'tcp', '--dport', '443', '-j', 'ACCEPT', '-m', 'comment', '--comment', '"test"']
    assert rule == expected_rule



# Generated at 2022-06-13 05:38:31.995158
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # Test case: Success
    output = b"Chain INPUT (policy ACCEPT)\n"
    result = get_chain_policy(None, None, {"chain": "INPUT"})
    assert result == "ACCEPT"
    # Test case: No such chain
    output = b"Chain INPUT (policy ACCEPT)\n"
    result = get_chain_policy(None, None, {"chain": "INPUTT"})
    assert result == None



# Generated at 2022-06-13 05:38:35.446301
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy("", None, dict(chain="INPUT")) == None
    assert get_chain_policy("", None, dict(chain="OUTPUT")) == None
    assert get_chain_policy("", None, dict(chain="FORWARD")) == None


# Generated at 2022-06-13 05:38:45.151129
# Unit test for function check_present

# Generated at 2022-06-13 05:38:57.617877
# Unit test for function main

# Generated at 2022-06-13 05:38:58.077431
# Unit test for function get_iptables_version
def test_get_iptables_version():
    pass



# Generated at 2022-06-13 05:39:07.483231
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:13.317012
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_path = '/usr/sbin/iptables'
    class ModuleFakes:
        def run_command(self, cmd, check_rc):
            rc = 0
            out = 'iptables v1.6.0 (nf_tables)'
            return rc, out, None
    m = ModuleFakes()
    result = get_iptables_version(iptables_path, m)
    assert result == '1.6.0'



# Generated at 2022-06-13 05:39:14.206608
# Unit test for function flush_table

# Generated at 2022-06-13 05:39:24.656853
# Unit test for function construct_rule
def test_construct_rule():
    params_1 = {
        'ctstate': ['NEW'],
        'destination': '10.0.0.0/24',
        'destination_port': '22',
        'jump': 'ACCEPT',
        'protocol': 'tcp',
        'set_counters': '5/10',
        'wait': '5',
        'ip_version': 'ipv4',
    }
    expected = [
        '-w', '5',
        '-p', 'tcp',
        '-d', '10.0.0.0/24',
        '-m', 'conntrack',
        '--ctstate', 'NEW',
        '--dport', '22',
        '-j', 'ACCEPT',
        '-c', '5/10',
    ]
    assert construct

# Generated at 2022-06-13 05:39:54.904588
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:03.599661
# Unit test for function construct_rule
def test_construct_rule():
    def assert_rule(params):
        assert construct_rule(params) == params['expected']

    for i in range(1, 4):
        if i == 1:
            assert_rule(dict(
                protocol='tcp',
                source='192.168.1.1',
                comment='ansible',
                dst_range='192.0.2.1-192.0.2.250',
                expected=[
                    '-p', 'tcp',
                    '-s', '192.168.1.1',
                    '-m', 'iprange',
                    '--dst-range', '192.0.2.1-192.0.2.250',
                    '-m', 'comment',
                    '--comment', 'ansible',
                ],
            ))
        elif i == 2:
            assert_rule

# Generated at 2022-06-13 05:40:13.768798
# Unit test for function check_present
def test_check_present():
    cmd = ['/sbin/iptables', '-t', 'filter', '-C', 'INPUT', '-p', 'tcp',
           '-s', '8.8.8.8', '-j', 'DROP']
    if check_present(cmd[0], params={'table': 'filter', 'chain': 'INPUT',
                                     'protocol': 'tcp', 'source': '8.8.8.8', 'jump': 'DROP'}):
        assert False
    else:
        assert True
# End of Unit test



# Generated at 2022-06-13 05:40:21.574669
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:29.975552
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = 'iptables'
    iptables_bin_path = '../../../../../../bin/iptables'
    module = AnsibleModule(argument_spec=dict())
    params = dict(
        table='filter',
        chain='INPUT',
        protocol='icmp',
        source='1.1.1.1',
        jump='ACCEPT',
        ip_version='ipv4',
    )
    remove_rule(iptables_bin_path, module, params)


# Generated at 2022-06-13 05:40:32.425982
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule({})
    params = dict(
        table='filter',
        chain='INPUT',
        ip_version='ipv4',
    )
    result = get_chain_policy(iptables_path, module, params)
    assert result is not None



# Generated at 2022-06-13 05:40:41.132809
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:49.278876
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain = 'INPUT'
    policy = 'ACCEPT'
    iptables_path = 'iptables'
    for version in ['ipv4', 'ipv6']:
        rule = {'chain': chain, 'policy': policy, 'ip_version': version}
        assert(policy == get_chain_policy(iptables_path, rule))



# Generated at 2022-06-13 05:40:54.793228
# Unit test for function get_chain_policy
def test_get_chain_policy():
    xtable = dict(
        table='filter',
        chain='INPUT',
        ip_version='ipv4',
        wait=None
    )
    xargs = ['/bin/iptables', '-t', 'filter', '-L', 'INPUT']
    result = get_chain_policy(xargs[0], xtable, xargs[1:])
    assert(result == 'ACCEPT')



# Generated at 2022-06-13 05:41:00.941575
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        source='1.2.3.4',
        destination='4.3.2.1',
        protocol='tcp',
        destination_port=80,
        jump='ACCEPT',
        ip_version='ipv4',
        comment='test comment',
    )

    rule = construct_rule(params)
    assert [
        '-p', 'tcp',
        '-s', '1.2.3.4',
        '-d', '4.3.2.1',
        '--dport', '80',
        '-j', 'ACCEPT',
        '--comment', 'test comment',
    ] == rule

# Generated at 2022-06-13 05:41:59.590340
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    table = 'filter'
    chain = 'INPUT'
    params = dict(
      table=table,
      chain=chain,
      ip_version='ipv4',
    )
    iptables_path = BINS[params['ip_version']]
    policy = get_chain_policy(iptables_path, module, params)
    assert policy == 'ACCEPT'

# Generated at 2022-06-13 05:42:04.026068
# Unit test for function main

# Generated at 2022-06-13 05:42:17.421248
# Unit test for function remove_rule
def test_remove_rule():
    params = dict(chain='test_chain', table='test_table')
    remove_rule('test_iptables_path', 'test_module', params)
    params.update(rule_num=1)
    remove_rule('test_iptables_path', 'test_module', params)
    params.update(source='10.0.0.1')
    remove_rule('test_iptables_path', 'test_module', params)
    params.update(destination='10.0.0.2')
    remove_rule('test_iptables_path', 'test_module', params)
    params.update(protocol='udp')
    remove_rule('test_iptables_path', 'test_module', params)



# Generated at 2022-06-13 05:42:30.489682
# Unit test for function main
def test_main():
    iptables_version = get_iptables_version(IPTABLES_PATH, AnsibleModule(argument_spec={}))

# Generated at 2022-06-13 05:42:40.789751
# Unit test for function check_present
def test_check_present():
    test_ipv4_present = True
    test_ipv6_present = True
    test_params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='22',
        match='tcp',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment="Accept new SSH connections"
    )
    test_cmd = ['/sbin/iptables']
    test_cmd.extend(['-t', test_params['table']])
    test_cmd.extend(['-C', test_params['chain']])
    test_cmd.extend(construct_rule(test_params))

# Generated at 2022-06-13 05:42:44.141700
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain_header = 'Chain INPUT (policy ACCEPT)\n'
    result = re.search(r'\(policy ([A-Z]+)\)', chain_header)
    if result:
        return result.group(1)
    return None
print(test_get_chain_policy())


# Generated at 2022-06-13 05:42:47.499512
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain_info = dict(chain='INPUT', ip_version='ipv4')
    get_chain_policy('iptables', chain_info)



# Generated at 2022-06-13 05:42:57.251339
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:59.783862
# Unit test for function get_iptables_version
def test_get_iptables_version():
    """
    Unit test for function get_iptables_version.
    """
    class Module:
        @staticmethod
        def run_command(cmd, check_rc=True):
            return 0, 'v1.4.20', ''
    iptables_path = '/bin/iptables'
    module = Module()
    assert get_iptables_version(iptables_path, module) == '1.4.20'



# Generated at 2022-06-13 05:43:03.367899
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils.basic import AnsibleModule
    ipset_cmd_path = "ipset"
    module = AnsibleModule({
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'jump': 'ACCEPT',
        'goto': 'LOGGING',
    })
    assert check_present(ipset_cmd_path, module, module.params) is False

