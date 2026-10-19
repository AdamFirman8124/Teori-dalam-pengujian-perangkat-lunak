

# Generated at 2022-06-13 05:34:44.647943
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        table='filter',
        ip_version='ipv4',
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        comment='Accept tcp 80',
    )
    rule = construct_rule(params)

    assert ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept tcp 80'] == rule

# Generated at 2022-06-13 05:34:54.946630
# Unit test for function main

# Generated at 2022-06-13 05:34:57.017346
# Unit test for function set_chain_policy
def test_set_chain_policy():
    params = {'chain': 'INPUT', 'policy': 'DROP'}
    assert set_chain_policy(None, None, params) == ['-P', 'INPUT', 'DROP']



# Generated at 2022-06-13 05:35:01.998141
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = ['iptables', '-t', 'filter', '-A', 'INPUT', '-p', 'tcp']
    append_match_flag(rule, 'match', '--syn', True)
    assert rule == ['iptables', '-t', 'filter', '-A', 'INPUT', '-p', 'tcp', '--syn']



# Generated at 2022-06-13 05:35:13.160749
# Unit test for function construct_rule
def test_construct_rule():
    print(
        'test_construct_rule()')
    tables = 'raw', 'mangle', 'filter', 'nat', 'security'
    for table in tables:
        for chain in (
                'INPUT', 'OUTPUT', 'FORWARD', 'PREROUTING', 'POSTROUTING'):
            result = construct_rule(
                dict(
                    ip_version='ipv4',
                    chain=chain,
                    table=table,
                    protocol='tcp',
                )
            )
            assert rule_exists(chain, table, result), 'table %s chain %s rule %s not found' % (table, chain, result)
            print('table %s chain %s: %s' % (table, chain, result))


# Generated at 2022-06-13 05:35:15.740949
# Unit test for function construct_rule
def test_construct_rule():
    for input, expected in tests.test_construct_rule():
        rc = construct_rule(input)
        assert rc == expected, 'Expected %s, recieved %s' % (expected, rc)



# Generated at 2022-06-13 05:35:16.869666
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = "/sbin/iptables"
    print(push_arguments(iptables_path, '-I', params))

# Generated at 2022-06-13 05:35:21.832463
# Unit test for function construct_rule
def test_construct_rule():
    # test single format
    assert construct_rule(dict(
        protocol='tcp',
        source='192.168.1.100',
        destination='10.0.0.1',
        jump='ACCEPT',
        )) == ['-w', '-p', 'tcp', '-s', '192.168.1.100', '-d', '10.0.0.1', '-j', 'ACCEPT']
    # test multiple format

# Generated at 2022-06-13 05:35:23.333645
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy(None, None, dict(chain='INPUT', policy='DROP', table='raw')) == ['-t', 'raw', '-P', 'INPUT', 'DROP']



# Generated at 2022-06-13 05:35:28.770516
# Unit test for function construct_rule
def test_construct_rule():
    # Test chain and jump option
    rule = construct_rule(dict(chain='FORWARD', jump='REJECT'))
    assert rule == ['-j', 'REJECT']
    # Test log-level option
    rule = construct_rule(dict(chain='INPUT', jump='LOG', log_level='debug'))
    assert rule == ['-j', 'LOG', '--log-level', 'debug']
    # Test in_interface option
    rule = construct_rule(dict(chain='INPUT', in_interface='eth0'))
    assert rule == ['-i', 'eth0']
    # Test source destination options
    rule = construct_rule(dict(chain='INPUT', source='8.8.8.8', destination='10.10.10.10'))

# Generated at 2022-06-13 05:35:48.746919
# Unit test for function remove_rule
def test_remove_rule():
    params = dict()
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    params['protocol'] = 'tcp'
    params['destination_port'] = '22'
    params['ctstate'] = 'NEW'
    params['syn'] = 'match'
    params['jump'] = 'ACCEPT'
    params['comment'] = 'Accept new SSH connections.'
    iptables_path = 'iptables'
    remove_rule(iptables_path, '', params)
#test_remove_rule() end


# Generated at 2022-06-13 05:35:53.838898
# Unit test for function append_param
def test_append_param():
    rule = []
    append_param(rule, "test", "--test", False)
    assert rule == ['--test', 'test']

    rule = []
    append_param(rule, "!test", "--test", False)
    assert rule == ['!', '--test', 'test']

    rule = []
    append_param(rule, ["test1", "test2"], "--test", True)
    assert rule == ['--test', 'test1', '--test', 'test2']

    rule = []
    append_param(rule, ["!test1", "!test2"], "--test", True)
    assert rule == ['!', '--test', 'test1', '!', '--test', 'test2']



# Generated at 2022-06-13 05:36:00.734768
# Unit test for function construct_rule
def test_construct_rule():
    module = dict(chain='FORWARD', src_range='10.0.0.1-10.0.0.50',
                  dst_range='192.168.1.100-192.168.1.199', jump='ACCEPT')
    rule = construct_rule(module)
    assert '-p' not in rule
    assert '-s' not in rule
    assert '-d' not in rule
    assert '-m' not in rule
    assert '--tcp-flags' not in rule
    assert '-j' in rule
    assert '--to-destination' not in rule
    assert '--dports' not in rule
    assert '--to-source' not in rule
    assert '-g' not in rule
    assert '-i' not in rule
    assert '-o' not in rule

# Generated at 2022-06-13 05:36:07.099183
# Unit test for function get_chain_policy
def test_get_chain_policy():
    target_chain = 'INPUT'
    input_chains_policy = []
    input_chains_policy.append('Chain INPUT (policy INPUT)')
    input_chains_policy.append('Chain INPUT (policy ACCEPT)')
    print(get_chain_policy(None, None, {'chain': target_chain, 'chain_policy': input_chains_policy}))



# Generated at 2022-06-13 05:36:08.619776
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', '-C', params) == True

# Generated at 2022-06-13 05:36:13.813779
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='1.1.1.1',
        destination='2.2.2.2',
        destination_port=22
    )
    assert construct_rule(params) == [
        '-w', '-p', 'tcp', '-s', '1.1.1.1', '-d', '2.2.2.2', '-m',
        'multiport', '--dports', '22', '-j', 'ACCEPT'
    ]



# Generated at 2022-06-13 05:36:18.378686
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_version = get_iptables_version('echo', module)
    assert (iptables_version.startswith('1'))
    assert (iptables_version.endswith('\n'))



# Generated at 2022-06-13 05:36:23.866463
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    append_match_flag(rule, 'match', '--tcp-flags', True)
    assert rule == ['--tcp-flags']
    rule = []
    append_match_flag(rule, 'negate', '--tcp-flags', True)
    assert rule == ['!', '--tcp-flags']


# Generated at 2022-06-13 05:36:34.141252
# Unit test for function flush_table
def test_flush_table():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    sys.modules['ansible'] = AnsibleModule
    # Fix up the module_utils to load modules
    import os.path
    import re
    import sys
    import imp
    import traceback

    class FakeAnsibleModule(object):
        def __init__(self, params):
            self.params = params
            self.check_mode = False

        def run_command(self, cmd, check_rc=True):
            return self._run_command(cmd)

        def _run_command(self, cmd):
            """
            :param cmd: a list of parameters to be passed to subprocess.Popen
            :return: a tuple of rc (int), stdout (str), stderr (str)
            """
            import sys

# Generated at 2022-06-13 05:36:38.034206
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        rule_num='5'
    )
    assert ['iptables', '-t', 'filter', '-I', 'INPUT', '5']+construct_rule(params) == push_arguments('iptables', '-I', params, make_rule=True)



# Generated at 2022-06-13 05:36:58.762622
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    from ansible.module_utils.basic import load_platform_subclass


# Generated at 2022-06-13 05:36:59.731059
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables',None,'mock') == 'ACCEPT'



# Generated at 2022-06-13 05:37:03.827622
# Unit test for function get_chain_policy
def test_get_chain_policy():
    mapping = [
         ("Chain INPUT (policy ACCEPT)\n", "ACCEPT"),
         ("Chain INPUT (policy DROP)\n", "DROP"),
         ("Chain INPUT (policy ALLOW)\n", None),
         ("Chain INPUT (policy)\n", None)
    ]
    for test_string, expected in mapping:
        result = get_chain_policy('iptables', None, {"table": "filter", "chain": "INPUT"}, test_string)
        assert result == expected



# Generated at 2022-06-13 05:37:15.963485
# Unit test for function main

# Generated at 2022-06-13 05:37:21.217971
# Unit test for function construct_rule
def test_construct_rule():
    # Test rule generation
    params = dict(
        ip_version='ipv4',
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
    )

    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp',
        '--dport', '80',
        '-m', 'conntrack',
        '--ctstate', 'NEW',
        '--syn',
        '-m', 'comment',
        '--comment', 'Accept new SSH connections.',
        '-j', 'ACCEPT']



# Generated at 2022-06-13 05:37:24.180517
# Unit test for function get_chain_policy
def test_get_chain_policy():
    get_chain_policy("test", "module", "params")
    assert get_chain_policy("test", "module", "params") == None


# Generated at 2022-06-13 05:37:28.314796
# Unit test for function insert_rule
def test_insert_rule():
    assert(push_arguments('iptables', '-I', {'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination': '8.8.8.8', 'jump': 'ACCEPT', 'reject_with': 'tcp-reset', 'ip_version': 'ipv4'}) == ['iptables', '-t', 'filter', '-I', 'INPUT', '-p', 'tcp', '-d', '8.8.8.8', '-j', 'ACCEPT', '--reject-with', 'tcp-reset'])



# Generated at 2022-06-13 05:37:32.684649
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'policy': 'DROP'}) == 'DROP'
    assert get_chain_policy(None, None, {'policy': 'ACCEPT'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'policy': 'TEST'}) == 'TEST'



# Generated at 2022-06-13 05:37:37.429297
# Unit test for function get_chain_policy
def test_get_chain_policy():
    params = dict(
        ip_version='ipv4',
        table='filter',
        chain='FORWARD',
    )
    assert get_chain_policy('iptables', None, params) is None



# Generated at 2022-06-13 05:37:49.985398
# Unit test for function main

# Generated at 2022-06-13 05:38:12.626995
# Unit test for function construct_rule
def test_construct_rule():
    # simple rule - no matching
    params = dict(
        chain='INPUT',
        protocol='tcp',
        jump='ACCEPT',
    )

    expect = [ '-A', 'INPUT', '-p', 'tcp', '-j', 'ACCEPT' ]

    assert expect == construct_rule(params)

    # rule with comment
    params = dict(
        chain='INPUT',
        protocol='tcp',
        jump='ACCEPT',
        comment='Hello',
    )

    expect = [
        '-A', 'INPUT', '-p', 'tcp', '-j', 'ACCEPT',
        '--comment', 'Hello'
    ]

    assert expect == construct_rule(params)

    # rule with source

# Generated at 2022-06-13 05:38:20.470670
# Unit test for function construct_rule
def test_construct_rule():
    import random
    import string

    params = dict()
    params['protocol'] = None
    params['source'] = None
    params['destination'] = None
    params['match'] = None
    params['tcp_flags'] = None
    params['jump'] = None
    params['gateway'] = None
    params['log_prefix'] = None
    params['log_level'] = None
    params['to_destination'] = None
    params['destination_ports'] = None
    params['to_source'] = None
    params['goto'] = None
    params['in_interface'] = None
    params['out_interface'] = None
    params['fragment'] = None
    params['set_counters'] = None
    params['source_port'] = None
    params['destination_port'] = None


# Generated at 2022-06-13 05:38:27.790407
# Unit test for function main
def test_main():
    args = dict(
        rule="FROM 192.168.1.1 TO 10.10.10.10 ACCEPT".split(" "),
        chain='INPUT',
    )

# Generated at 2022-06-13 05:38:33.421369
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:44.357839
# Unit test for function push_arguments
def test_push_arguments():
    params = {}
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    params['log_prefix'] = 'test'
    params['source'] = '192.168.1.0/24'
    params['destination'] = '192.168.1.1'
    params['destination_port'] = '80'
    params['protocol'] = 'tcp'
    params['jump'] = 'ACCEPT'
    params['goto'] = 'drop_everything'
    params['in_interface'] = 'eth0'
    params['out_interface'] = 'eth1'
    params['fragment'] = 'yes'
    params['set_counters'] = 'yes'
    params['log_level'] = 'info'

# Generated at 2022-06-13 05:38:57.237820
# Unit test for function construct_rule
def test_construct_rule():
    '''
    Test construct_rule()
    '''
    if construct_rule(dict(protocol='tcp', source='12.34.56.78', jump='DROP')) != ['-p', 'tcp', '-s', '12.34.56.78', '-j', 'DROP']:
        raise AssertionError('Construct rule TCP with source failed.')
    if construct_rule(dict(protocol='tcp', destination='87.65.43.21', jump='DROP')) != ['-p', 'tcp', '-d', '87.65.43.21', '-j', 'DROP']:
        raise AssertionError('Construct rule TCP with destination failed.')

# Generated at 2022-06-13 05:39:06.983143
# Unit test for function construct_rule
def test_construct_rule():
    # "iptables -w 5 -p tcp -s 192.168.1.100-192.168.1.199 -d 10.0.0.1-10.0.0.50 -j ACCEPT"
    params = dict(
        protocol='tcp',
        source='192.168.1.100-192.168.1.199',
        destination='10.0.0.1-10.0.0.50',
        jump='ACCEPT',
        wait='5'
    )
    rule = construct_rule(params)

# Generated at 2022-06-13 05:39:16.585318
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = type("module", (object,), {'fail_json': {}, 'run_command': {}})
    module.run_command = run_command_mock
    params = {'ip_version': 'ipv4', 'table': 'filter', 'chain': 'INPUT', 'cmd_rc': 0, 'cmd_output': 'Chain INPUT (policy ACCEPT)\n', 'policy': ''}
    iptables_path = '/sbin/iptables'
    current_policy = get_chain_policy(iptables_path, module, params)
    assert current_policy == 'ACCEPT'


# Generated at 2022-06-13 05:39:25.072726
# Unit test for function main
def test_main():
    args = dict(
        state='present',
        action='insert',
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
        flush=True,
        rule='-m comment --comment "0001" -j ACCEPT',
    )
    assert main(args) == dict(
        changed=True,
        failed=False,
        ip_version="ipv4",
        state='present',
        table='filter',
        chain='INPUT',
        flush=True,
        rule='-m comment --comment "0001" -j ACCEPT',
    )

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:39:26.734573
# Unit test for function insert_rule
def test_insert_rule():
    print(">>>>>>>>>>>>>>>>")



# Generated at 2022-06-13 05:39:45.805244
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec={
            "table": {"required": True, "type": "str"},
            "chain": {"required": True, "type": "str"},
        }
    )
    assert get_chain_policy("/sbin/iptables", module, {
                            "table": "filter", "chain": "INPUT"}) == "ACCEPT"



# Generated at 2022-06-13 05:39:51.402512
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    append_tcp_flags(rule,
                     dict(flags=['ACK', 'RST', 'SYN', 'FIN'],
                          flags_set=['ACK', 'RST', 'SYN']),
                     '--tcp-flags')
    assert rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,RST,SYN']



# Generated at 2022-06-13 05:40:03.661311
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:16.542318
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', {}, { 'ip_version': 'ipv4', 'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '22', 'jump': 'ACCEPT'}) == False
    assert check_present('iptables', {}, { 'ip_version': 'ipv6', 'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '22', 'jump': 'ACCEPT'}) == False
    assert check_present('iptables', {}, { 'ip_version': 'ipv4', 'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '22', 'jump': 'ACCEPT', 'comment': 'test'}) == False


# Generated at 2022-06-13 05:40:27.383512
# Unit test for function remove_rule
def test_remove_rule():
    args = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='22',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.'
    )
    params = dict(
        table='filter',
        ip_version='ipv4',
        state='present',
        action='append',
        **args
    )
    change_rule(params)
    params['action'] = 'remove'
    remove_rule(params['ip_version'], params)
    change_rule(params)
    chk_rm_rule(params)



# Generated at 2022-06-13 05:40:28.868861
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule({})
    module.run_command = lambda x, **kwargs: (0, '', '')
    assert flush_table('iptables', module, dict(table='filter', chain='INPUT')) == None



# Generated at 2022-06-13 05:40:33.303342
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    test_param = dict(
        flags=['ALL'],
        flags_set=['ACK', 'RST', 'SYN', 'FIN']
    )
    test_rule = list()
    test_flag = '--tcp-flags'
    append_tcp_flags(test_rule, test_param, test_flag)
    assert test_rule == [test_flag, ','.join(test_param['flags']), ','.join(test_param['flags_set'])]


# Generated at 2022-06-13 05:40:38.230790
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        table='filter',
        chain='INPUT',
        rule_num='3',
        protocol='tcp',
        destination_port='80',
    )
    cmd = push_arguments(
        iptables_path='/sbin/iptables',
        action='-I',
        params=params,
        make_rule=True)
    expected = [
        '/sbin/iptables',
        '-t', params['table'],
        '-I', params['chain'], params['rule_num'],
        '-p', 'tcp',
        '--destination-port', '80',
    ]
    assert cmd == expected



# Generated at 2022-06-13 05:40:39.740905
# Unit test for function check_present
def test_check_present():
    check_present(None, None, {})



# Generated at 2022-06-13 05:40:50.959368
# Unit test for function get_chain_policy
def test_get_chain_policy():
    test_params = dict(
        table="filter",
        chain="INPUT",
        policy="DROP"
    )
    result = get_chain_policy(
        '/usr/bin/iptables',
        AnsibleModule(argument_spec={}),
        test_params)
    assert result in ['DROP', 'ACCEPT', 'REJECT', 'RETURN']
    test_params['chain'] = 'make_it_fail'
    result = get_chain_policy(
        '/usr/bin/iptables',
        AnsibleModule(argument_spec={}),
        test_params)
    assert result is None



# Generated at 2022-06-13 05:41:12.806184
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        ip_version='ipv4',
        protocol='tcp',
        source='8.8.8.8',
        log_prefix='IPTABLES:INFO: ',
        log_level='info',
        jump='LOG'
    )) == [
        '-w',
        '-p', 'tcp',
        '-s', '8.8.8.8',
        '-m', 'limit',
        '--log-prefix', 'IPTABLES:INFO: ',
        '--log-level', 'info',
        '-j', 'LOG'
    ]

# Generated at 2022-06-13 05:41:18.678000
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:29.728774
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, {'chain': 'INPUT'}) is None
    assert get_chain_policy('iptables', {}, {'table': 'nat', 'chain': 'PREROUTING'}) == 'ACCEPT'
    assert get_chain_policy('iptables', {}, {'table': 'nat', 'chain': 'OUTPUT'}) == 'ACCEPT'
    assert get_chain_policy('iptables', {}, {'table': 'nat', 'chain': 'POSTROUTING'}) == 'ACCEPT'
    assert get_chain_policy('iptables', {}, {'table': 'filter', 'chain': 'FORWARD'}) == 'DROP'
    assert get_chain_policy('iptables', {}, {'chain': 'INPUT'}) == 'DROP'
    assert get_chain

# Generated at 2022-06-13 05:41:34.814527
# Unit test for function insert_rule
def test_insert_rule():
    assert construct_rule(dict(
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        action='insert',
        rule_num='5'
    )) == ['-w', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:41:38.685238
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(argument_spec=dict(
        ip_version=dict(required=True, type='str', choices=['ipv4', 'ipv6']),
        table=dict(required=True, type='str', choices=['filter', 'nat', 'mangle', 'raw', 'security']),
        chain=dict(required=False, type='str'),
    ))
    iptables_path = BINS[module.params['ip_version']]
    params = module.params
    flush_table(iptables_path, module, params)


# Generated at 2022-06-13 05:41:46.170146
# Unit test for function main
def test_main():
    args={}
    args['table']='filter'
    args['chain']='INPUT'
    args['ip_version']='ipv4'
    args['protocol']='tcp'
    args['source']='127.0.0.1'
    args['destination']='127.0.0.1'
    args['jump']='ACCEPT'
    import json
    _json = json.dumps(args)
    print(_json)
    print(construct_rule(args))
    assert main() == None
if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:41:52.281522
# Unit test for function construct_rule
def test_construct_rule():
    params1 = dict(
        source='8.8.8.8',
        jump='DROP'
    )
    params2 = dict(
        table='nat',
        chain='PREROUTING',
        in_interface='eth0',
        protocol='tcp',
        match='tcp',
        destination_port='80',
        jump='REDIRECT',
        to_ports='8600',
        comment='Redirect web traffic to port 8600',
        ip_version='ipv4'
    )
    params3 = dict(
        chain='INPUT',
        ctstate=['ESTABLISHED', 'RELATED'],
        jump='ACCEPT',
        ip_version='ipv4'
    )

# Generated at 2022-06-13 05:41:58.238734
# Unit test for function main

# Generated at 2022-06-13 05:42:00.571804
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert(get_chain_policy(None, None, dict(chain='testchain')) == 'testpolicy')



# Generated at 2022-06-13 05:42:11.518770
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:56.078608
# Unit test for function main

# Generated at 2022-06-13 05:42:59.368765
# Unit test for function get_chain_policy
def test_get_chain_policy():
    print("This is a test")
    try:
        assert(get_chain_policy("iptables", "module", "-L -t filter")=="ACCEPT")
        assert(get_chain_policy("iptables", "module", "-L -t filter chain") == "DROP")
        print("The test is successful")
    except:
        print("The test encountered an error")
    return


# Generated at 2022-06-13 05:43:01.673261
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec={})
    iptables_path = 'iptables'
    params = dict(
        table='filter',
        chain='INPUT',
    )
    res = get_chain_policy(iptables_path, module, params)
    assert res == 'DROP'



# Generated at 2022-06-13 05:43:06.959125
# Unit test for function construct_rule
def test_construct_rule():
    module_params = dict(
        chain='INPUT',
        source='10.0.0.0/8',
        destination='172.16.0.0/12',
        jump='DROP',
        state='present',
        ip_version='ipv4',
        wait='5',
    )

    # ip4tables -w 5 -I INPUT -s 10.0.0.0/8 -d 172.16.0.0/12 -j DROP
    check_rule = '-w 15 -I INPUT -s 10.0.0.0/8 -d 172.16.0.0/12 -j DROP'.split()
    rule = construct_rule(module_params)

    assert rule == check_rule
    assert rule is not None
    assert rule[0] == '-w'

# Generated at 2022-06-13 05:43:10.661517
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule({})
    assert get_chain_policy('/bin/iptables', module, {'ip_version': 'ipv4', 'chain': 'INPUT'}) == 'ACCEPT'
    assert get_chain_policy('/bin/iptables', module, {'ip_version': 'ipv4', 'chain': 'FORWARD'}) == 'ACCEPT'
    assert get_chain_policy('/bin/iptables', module, {'ip_version': 'ipv4', 'chain': 'OUTPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:43:20.928971
# Unit test for function get_chain_policy
def test_get_chain_policy():
    #test1
    module = AnsibleModule(argument_spec=dict(
        chain="INPUT",
        table="filter",
        policy=dict(type='str', default=None),
        state=dict(type='str', choices=['present', 'absent'], default='present'),
        action=dict(type='str', default='append'),
        ip_version=dict(type='str', choices=['ipv4', 'ipv6'],
                        default='ipv4'),
        chain_state=dict(type='str', choices=['enabled', 'disabled'],
                         default=None)
    ))
    cmd = 'iptables -L INPUT -n --line-numbers'
    rc, out, _ = module.run_command(cmd, check_rc=True)

# Generated at 2022-06-13 05:43:31.385786
# Unit test for function flush_table
def test_flush_table():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(
        argument_spec = dict(
            ip_version = dict(type='str', choices=['ipv4', 'ipv6'], default='ipv4'),
            table = dict(type='str', default='filter'),
            chain = dict(type='str', default='INPUT'),
            wait = dict(type='str'),
        )
    )
    module.params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
    )
    assert flush_table(iptables_path, module, module.params) == ['sbin/iptables', '-t', 'filter', '-F', 'INPUT']


# Generated at 2022-06-13 05:43:35.629370
# Unit test for function construct_rule
def test_construct_rule():
    # Expected iptables command
    # iptables -A INPUT -p tcp -s 192.168.1.1 -j ACCEPT --comment abc
    test_param = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
        protocol='tcp',
        source='192.168.1.1',
        jump='ACCEPT',
        comment='abc',
    )
    assert construct_rule(test_param) == [
        'iptables', '-t', 'filter', '-A', 'INPUT', '-p', 'tcp', '-s',
        '192.168.1.1', '-j', 'ACCEPT', '--comment', 'abc'
    ]



# Generated at 2022-06-13 05:43:40.878384
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        protocol='tcp',
        source='10.0.0.1',
        destination='10.0.0.2',
        comment='foobar',
        in_interface='eth0',
        ip_version='ipv4',
        jump='DROP',
        destination_port=80,
    )) == (
        ['-s', '10.0.0.1', '-d', '10.0.0.2', '-p', 'tcp', '-i', 'eth0',
         '-m', 'comment', '--comment', 'foobar', '-j', 'DROP',
         '--dport', '80']
    )

# Generated at 2022-06-13 05:43:45.337321
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='192.168.0.0/24',
        jump='DROP',
        comment='This is my rule',
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == ['-p', 'tcp', '-s', '192.168.0.0/24', '-j', 'DROP', '-m', 'comment', '--comment', 'This is my rule']

