

# Generated at 2022-06-13 05:34:24.694165
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        ip_version='ipv4',
        action='append',
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        comment='Test comment',
    )
    rule = construct_rule(params)
    assert rule == ['-A', 'INPUT', '-p', 'tcp', '-m', 'comment', '--comment', 'Test comment', '--dport', '80', '-j', 'ACCEPT']
# End unit test



# Generated at 2022-06-13 05:34:35.404027
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        ip_version='ipv4',
        chain='INPUT',
        source='8.8.8.8',
        jump='DROP',
        table='filter',
        comment='test comment',
    )

    iptables_path = 'iptables'

    action = '-A'
    cmd = push_arguments(iptables_path, action, params, make_rule=True)

    action = '-I'
    params['rule_num'] = 5
    cmd = push_arguments(iptables_path, action, params, make_rule=True)

    action = '-F'
    cmd = push_arguments(iptables_path, action, params, make_rule=False)

    action = '-E'

# Generated at 2022-06-13 05:34:49.404763
# Unit test for function push_arguments

# Generated at 2022-06-13 05:34:57.491051
# Unit test for function insert_rule
def test_insert_rule():
    import mock
    import datetime
    module = mock.MagicMock()
    module.run_command = mock.MagicMock(return_value=(0,'','',''))
    class params:
        protocol = 'tcp'
        destination_port = 8080
        jump = 'ACCEPT'
        rule_num = 5
        chain = 'INPUT'
        ip_version = 'ipv4'
        table = 'filter'
    p = params()
    assert insert_rule('iptables',module,p) == None



# Generated at 2022-06-13 05:35:09.114327
# Unit test for function push_arguments
def test_push_arguments():
    module = AnsibleModule({
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT',
        'rule_num': '1',
    })
    iptables_path = '/usr/bin/iptables'
    result = push_arguments(iptables_path, '-I', module.params, True)

# Generated at 2022-06-13 05:35:23.930688
# Unit test for function check_present
def test_check_present():
    # Dummy return codes and output
    rc = 0
    stdout = ''
    stderr = ''

    # Assertion functions
    def run_command(cmd, check_rc=False):
        print(cmd)
        return (rc, stdout, stderr)

    # Construct arguments
    iptables_path = 'iptables'
    module = type('', (object,), dict(run_command=run_command))()
    params = {
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '443',
        'jump': 'ACCEPT',
        'wait': '5'
    }

    # Call the function, pass in arguments and check the output
    assert check

# Generated at 2022-06-13 05:35:27.898256
# Unit test for function insert_rule
def test_insert_rule():
    assert insert_rule("iptable", "module", ["rule"]) == "-I rule"



# Generated at 2022-06-13 05:35:33.477332
# Unit test for function main

# Generated at 2022-06-13 05:35:45.066123
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        ip_version='ipv4',
        chain='INPUT',
        table='filter',
        action='-I',
        rule_num=8,
        log_prefix='IPTABLES:INFO: ',
        limit_burst=20,
        ctstate='ESTABLISHED',
        protocol='tcp',
        destination_port='80',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.'
    )
    cmd = push_arguments('iptables', '-I', params)

# Generated at 2022-06-13 05:35:48.794294
# Unit test for function set_chain_policy
def test_set_chain_policy():
    set_chain_policy("/sbin/iptables", {}, {
        'chain': 'INPUT',
        'policy': 'DROP',
        'table': 'filter'
    })
# End of unit test



# Generated at 2022-06-13 05:36:11.687895
# Unit test for function get_chain_policy
def test_get_chain_policy():
    table = 'filter'
    chain = 'OUTPUT'
    policy = 'ACCEPT'
    params = dict(
        table=table,
        chain=chain,
        policy=policy
    )
    iptables_path = "/sbin/iptables"
    iptables_command = "{0} -t {1} -P {2} {3}".format(iptables_path, table, chain, policy)
    iptables_command_check = "{0} -t {1} -L {2} -n".format(iptables_path, table, chain)
    module = AnsibleModule(argument_spec={})
    iptables_check = module.run_command(iptables_command_check, check_rc=True)

# Generated at 2022-06-13 05:36:18.692256
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.Mock(return_value=(0, '''Chain INPUT (policy ACCEPT)''', ''))
    assert get_chain_policy(None, module, dict(chain='INPUT')) == 'ACCEPT'
    assert get_chain_policy(None, module, dict(chain='INPUT', table='test')) == 'ACCEPT'
    module.run_command.assert_called_with(['iptables', '-t', None, '-L', 'INPUT'], check_rc=True)
    module.run_command.assert_called_with(['iptables', '-t', 'test', '-L', 'INPUT'], check_rc=True)


# Generated at 2022-06-13 05:36:21.913293
# Unit test for function get_chain_policy
def test_get_chain_policy():
    src = ['Chain HOSTS (policy ACCEPT)']
    module = AnsibleModule({'table': 'filter', 'chain': 'HOSTS'})
    module.run_command = lambda cmd, rc=True: (0, '\n'.join(src), '')
    ret = get_chain_policy('iptables', module, {'table': 'filter', 'chain': 'HOSTS'})
    assert ret == "ACCEPT"



# Generated at 2022-06-13 05:36:32.565378
# Unit test for function main
def test_main():
    err_msg = "Can't detect current policy"
    check_msg = "Checking the module"
    target_msg = "Target is already up to date"
    flush_msg = "Flushing the table"
    append_msg = 'Appending the rule'
    insert_msg = 'Inserting the rule'
    remove_msg = 'Removing the rule'
    success_msg = "Successfully completed"
    fail_msg = "Failed to complete"
    module_args = {
        'flush': True,
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
    }
    set_module_args(module_args)
    flush_cmd = ('iptables', '-t', 'filter', '-F', 'INPUT')

# Generated at 2022-06-13 05:36:37.209667
# Unit test for function check_present
def test_check_present():
    iptables_path = '/sbin/iptables'
    module = dict(
        params=dict(
            protocol='tcp',
            ctstate='NEW',
            jump='ACCEPT',
            chain='test',
            table='test',
        ),
    )
    params = module['params']
    cmd = push_arguments(iptables_path, '-C', params)
    rc, _, __ = module.run_command(cmd, check_rc=False)
    assert rc == 0

# Generated at 2022-06-13 05:36:39.880347
# Unit test for function append_match_flag
def test_append_match_flag():
    rule =[]
    append_match_flag(rule,'match','SYN',True)
    assert rule == ['SYN']
    rule = []
    append_match_flag(rule,'negate','SYN',True)
    assert rule == ['!', 'SYN']

# Generated at 2022-06-13 05:36:48.784525
# Unit test for function construct_rule
def test_construct_rule():
    """Test function construct_rule"""

# Generated at 2022-06-13 05:36:53.459916
# Unit test for function push_arguments
def test_push_arguments():
    # Construct arguments for rule
    for ip_version in ('ipv4', 'ipv6'):
        bin_name = BINS[ip_version]
        params = dict(
            ip_version=ip_version,
            table='nat',
            chain='PREROUTING',
            in_interface='eth0',
            protocol='tcp',
            match='tcp',
            destination_port='80',
            jump='REDIRECT',
            to_ports='8600',
            comment='Redirect web traffic to port 8600',
        )
        cmd = push_arguments(bin_name, '-I', params)

# Generated at 2022-06-13 05:37:04.194047
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:06.790399
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    flag = '--tcp-flags'
    param = dict(flags=['ALL'], flags_set=['ACK', 'RST', 'SYN', 'FIN'])
    append_tcp_flags(rule, param, flag)
    assert '--tcp-flags' in rule
    assert ','.join(param['flags']) in rule
    assert ','.join(param['flags_set']) in rule


# Generated at 2022-06-13 05:37:18.345248
# Unit test for function append_rule
def test_append_rule():
    assert append_rule('iptables', module, params) == 0



# Generated at 2022-06-13 05:37:26.486277
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = "iptables"
    action = "-D"

# Generated at 2022-06-13 05:37:34.834279
# Unit test for function construct_rule
def test_construct_rule():
    # Testing basic rule
    args = dict(
        ip_version='ipv4',
        protocol='tcp',
        source='127.0.0.1',
        destination='127.0.0.1',
        match=['state'],
        ctstate=['RELATED', 'ESTABLISHED'],
        jump='ACCEPT',
        comment='comment_test',
        syn='negate',
    )

# Generated at 2022-06-13 05:37:43.705049
# Unit test for function get_chain_policy
def test_get_chain_policy():
  assert get_chain_policy(None, None, { "table": "filter", "chain": "INPUT" }) == "DROP"
  assert get_chain_policy(None, None, { "table": "filter", "chain": "FORWARD" }) == "ACCEPT"
  assert get_chain_policy(None, None, { "table": "filter", "chain": "OUTPUT" }) == "ACCEPT"
  assert get_chain_policy(None, None, { "table": "nat", "chain": "INPUT" }) == "ACCEPT"
  assert get_chain_policy(None, None, { "table": "nat", "chain": "OUTPUT" }) == "ACCEPT"

# Generated at 2022-06-13 05:37:50.349490
# Unit test for function get_iptables_version
def test_get_iptables_version():
    # Test 1.
    # Test case - iptables version is 1.4.20
    # Return - '1.4.20'
    test_params = dict(
        iptables_path='/sbin/iptables',
        module=AnsibleModule(argument_spec=dict()),
        )
    out = b'iptables v1.4.20'
    test_params['module'].run_command = MagicMock(return_value=(0, out, ''))
    assert get_iptables_version(**test_params) == '1.4.20'



# Generated at 2022-06-13 05:38:04.855319
# Unit test for function main

# Generated at 2022-06-13 05:38:12.196916
# Unit test for function construct_rule
def test_construct_rule():
    test_params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_ports=['80', '443', '8081:8083'],
        jump='ACCEPT',
        comment='Accept new SSH connections.',
    )
    test_rule = construct_rule(test_params)
    assert test_rule == [
        '-p', 'tcp', '-m', 'multiport', '--dports', '80,443,8081:8083',
        '-m', 'comment', '--comment', 'Accept new SSH connections.', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:38:14.406661
# Unit test for function check_present
def test_check_present():
    assert check_present('test', {}, {'chain':'LOGGING', 'table':'filter', 'protocol':'tcp', 'action':'present'}) == True


# Generated at 2022-06-13 05:38:16.816377
# Unit test for function append_rule
def test_append_rule():
    assert 0 == append_rule(iptables_path, module, params)



# Generated at 2022-06-13 05:38:25.806465
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        table='filter',
        chain='OUTPUT',
        rule_num='1',
        destination_port='8081')
    cmd = push_arguments('iptables', '-A', params)
    assert cmd == ['iptables',
                    '-t', 'filter',
                    '-A', 'OUTPUT',
                    '--dport', '8081'
                    ]

# Generated at 2022-06-13 05:38:46.054536
# Unit test for function main
def test_main():
    import tempfile

    def test_module(module_args, result):
        t_path = tempfile.mktemp()
        os.environ['PATH'] = os.path.dirname(t_path) + os.pathsep + os.environ['PATH']
        f = open(t_path, 'w+')
        f.write("#!/bin/env bash\necho yes")
        f.close()

# Generated at 2022-06-13 05:38:48.756139
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_version = 'iptables v1.6.1\n'
    module = AnsibleModule({})
    assert get_iptables_version('/sbin/iptables', module) == '1.6.1'



# Generated at 2022-06-13 05:38:59.188912
# Unit test for function main
def test_main():
    # Test module args
    module_args = dict(
        wait='0.01',
        table='filter',
        ip_version='ipv4',
        chain='INPUT',
        source='192.168.0.1',
        jump='ACCEPT',
        flush=False,
        comment='test',
        gid_owner=10000,
        policy='DROP',
    )
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params = module_args

# Generated at 2022-06-13 05:39:11.131561
# Unit test for function get_chain_policy
def test_get_chain_policy():
    test_module = None
    test_params = dict(
        table='filter',
        chain='INPUT',
    )
    assert get_chain_policy(
        '/sbin/iptables',
        test_module,
        test_params
    ) == 'ACCEPT'
    test_params.update(dict(chain='OUTPUT'))
    assert get_chain_policy(
        '/sbin/iptables',
        test_module,
        test_params
    ) == 'ACCEPT'
    test_params.update(dict(chain='FORWARD'))
    assert get_chain_policy(
        '/sbin/iptables',
        test_module,
        test_params
    ) == 'ACCEPT'
    test_params.update(dict(chain='bogus'))
    assert get_chain_policy

# Generated at 2022-06-13 05:39:24.190106
# Unit test for function insert_rule
def test_insert_rule():
    import tempfile
    module_args = {}
    module_args['ip_version'] = 'ipv4'
    module_args['chain'] = 'INPUT'
    module_args['protocol'] = 'tcp'
    module_args['destination_port'] = '80'
    module_args['jump'] = 'ACCEPT'
    module_args['comment'] = 'Accept new SSH connections.'
    module_args['action'] = 'insert'
    module_args['rule_num'] = '5'

    with tempfile.NamedTemporaryFile() as temp:
        setattr(temp, 'name', 'iptables')
        module = AnsibleModule(argument_spec={})
        assert insert_rule(temp.name, module, module_args) == None
# End of unit test



# Generated at 2022-06-13 05:39:32.486416
# Unit test for function append_rule
def test_append_rule():
    ansible_module = AnsibleModule({
        'ip_version': 'ipv4',
        'bin_path': 'mock',
        'chain': 'INPUT',
        'table': 'filter',
        'source': '1.1.1.1',
        'obtain_lock': False
    })
    cmd = [ansible_module.params['bin_path'], '-t', ansible_module.params['table'], '-A', ansible_module.params['chain'], '-s', '1.1.1.1']
    append_rule(ansible_module.params['bin_path'], ansible_module, ansible_module.params)
    assert(cmd == ansible_module.run_command.call_args[0][0])



# Generated at 2022-06-13 05:39:45.538915
# Unit test for function check_present
def test_check_present():
    params = dict(
        ip_version='ipv4',
        chain='INPUT',
        table='filter',
        in_interface='eth0',
        out_interface='eth1',
        protocol='tcp',
        destination='127.0.0.1/8',
        destination_port='53',
        jump='ACCEPT',
        source='10.0.0.0/8',
        source_port='80',
        state=['INVALID', 'NEW'],
        to_ports='8080',
        source_port='80',
        comment='Test rule for unit test'
    )
    cmd = push_arguments('/sbin/iptables', '-C', params)

# Generated at 2022-06-13 05:39:51.887304
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    assert append_tcp_flags(
        ['iptables', '-A'],
        {'flags': ['ACK', 'RST', 'SYN', 'FIN'], 'flags_set': ['ACK', 'RST', 'SYN', 'FIN']},
        '--tcp-flags'
    ) == ['iptables', '-A', '--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,RST,SYN,FIN']



# Generated at 2022-06-13 05:39:53.983735
# Unit test for function get_chain_policy
def test_get_chain_policy():
    set_chain_policy(iptables_path, module, params)
    policy = get_chain_policy(iptables_path, module, params)
    assert policy == 'DROP'



# Generated at 2022-06-13 05:39:54.627900
# Unit test for function append_rule
def test_append_rule():
    assert append_rule(__, __, __) == None



# Generated at 2022-06-13 05:40:18.025345
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:40:22.416403
# Unit test for function check_present
def test_check_present():
    assert check_present(['iptables', '-C'], {'iptables': '-t', 'table': 'filter'},
                         {'chain': 'INPUT', 'action': '-C',
                          'ip_version': 'ipv4', 'table': 'filter'}) == True


# Generated at 2022-06-13 05:40:30.484815
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule({'_ansible_check_mode': False})
    params = dict(
        chain="INPUT",
        table="filter",
        ip_version='ipv4',
        policy=None,
    )
    assert get_chain_policy("iptables", module, params) == "ACCEPT"
    params = dict(
        chain="OUTPUT",
        table="filter",
        ip_version='ipv4',
        policy=None,
    )
    assert get_chain_policy("iptables", module, params) == "ACCEPT"
    params = dict(
        chain="FORWARD",
        table="filter",
        ip_version='ipv4',
        policy=None,
    )
    assert get_chain_policy("iptables", module, params) == "ACCEPT"



# Generated at 2022-06-13 05:40:31.986286
# Unit test for function flush_table
def test_flush_table():
    iptables_path='iptables'
    cmd = push_arguments(iptables_path, '-F', params, make_rule=False)
    assert "iptables -F" in str(cmd)



# Generated at 2022-06-13 05:40:40.787156
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain="INPUT",
        source="8.8.8.8",
        jump="DROP",
        ip_version="ipv4"
    )
    rule = construct_rule(params)
    assert rule == [
        '-s', '8.8.8.8', '-j', 'DROP'
    ]

    params = dict(
        chain="INPUT",
        protocol="tcp",
        destination_port="8080",
        jump="ACCEPT",
        state="present",
        rule_num=5,
        ip_version="ipv4"
    )
    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp', '--destination-port', '8080', '-j', 'ACCEPT'
    ]

   

# Generated at 2022-06-13 05:40:54.225286
# Unit test for function append_rule
def test_append_rule():
    import sys
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict(iptables_path=dict(required=False), params=dict(required=False)))

# Generated at 2022-06-13 05:41:01.409468
# Unit test for function main
def test_main():
    from ansible.modules.network.firewall import iptables
    iptables.iptables_path = '/bin/true'
    iptables.iptables_version = '1.4.1'


# Generated at 2022-06-13 05:41:06.612384
# Unit test for function check_present
def test_check_present():
    params = dict(
        table='filter',
        chain='FORWARD',
        source='192.168.1.100/24',
    )
    iptables_path = '/sbin/iptables'
    cmd = push_arguments(iptables_path, '-C', params)
    rc, _, __ = module.run_command(cmd, check_rc=False)
    assert(rc == 0)



# Generated at 2022-06-13 05:41:08.076580
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/sbin/iptables',None, {'table': 'filter', 'chain': 'INPUT'}) == 'DROP'


# Generated at 2022-06-13 05:41:15.851464
# Unit test for function insert_rule
def test_insert_rule():
    params = {
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT',
        'action': 'insert',
        'rule_num': 5
    }
    path = 'iptables'
    cmd = push_arguments(path, '-I', params)
    if (cmd == ['iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--destination-port', '8080', '-j', 'ACCEPT']):
        return True
    else:
        return False
    #return (rc == 0)



# Generated at 2022-06-13 05:41:42.731492
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # Try parsing a chain with policy DROP
    module = AnsibleModule(argument_spec={})
    def run_command_mock(*args, **kwargs):
        return 0, "Chain OUTPUT (policy DROP)\n", ''
    module.run_command = run_command_mock
    assert get_chain_policy("/usr/bin/iptables", module, {"table": "filter", "chain": "OUTPUT"}) == "DROP"

    # Try parsing a chain with policy ACCEPT
    module = AnsibleModule(argument_spec={})
    def run_command_mock(*args, **kwargs):
        return 0, "Chain INPUT (policy ACCEPT)\n", ''
    module.run_command = run_command_mock

# Generated at 2022-06-13 05:41:50.370076
# Unit test for function main

# Generated at 2022-06-13 05:41:51.917454
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', 'module', 'params') == 'None'



# Generated at 2022-06-13 05:41:55.710489
# Unit test for function get_chain_policy
def test_get_chain_policy():
    result = get_chain_policy(None, None, {"chain":"INPUT","table":"filter"})
    assert result == "ACCEPT"


# Generated at 2022-06-13 05:41:57.351544
# Unit test for function insert_rule
def test_insert_rule():
    assert insert_rule('ipv4', init_module('', '', ''), {}) == 'Insert rule'



# Generated at 2022-06-13 05:42:05.724841
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:09.470004
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/sbin/iptables', None, {'table': 'filter', 'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:42:22.257394
# Unit test for function remove_rule

# Generated at 2022-06-13 05:42:30.244345
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import subprocess
    module = type('obj', (object,), dict(params=dict(), run_command=lambda *_, **k: ('', subprocess.Popen(*_, **k).communicate(), 0)))()
    module.params['iptables_path'] = sys.executable
    module.params['table'] = 'filter'
    module.params['chain'] = 'test'
    assert check_present(module.params['iptables_path'], module, module.params) == False
    module.params['table'] = 'nat'
    assert check_present(module.params['iptables_path'], module, module.params) == False
    module.params['protocol'] = 'tcp'

# Generated at 2022-06-13 05:42:32.618488
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, params) == True
    assert check_present('ip6tables', module, params) == True


# Generated at 2022-06-13 05:42:58.146802
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'INPUT'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'chain': 'FORWARD'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'chain': 'OUTPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:43:03.996170
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:16.884731
# Unit test for function main

# Generated at 2022-06-13 05:43:22.494325
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain_header_pending = 'Chain INPUT (policy ACCEPT)'
    chain_header_accept = 'Chain INPUT (policy ACCEPT)'
    chain_header_drop = 'Chain INPUT (policy DROP)'

    assert get_chain_policy(None, None, chain_header_pending) == 'ACCEPT'
    assert get_chain_policy(None, None, chain_header_accept) == 'ACCEPT'
    assert get_chain_policy(None, None, chain_header_drop) == 'DROP'



# Generated at 2022-06-13 05:43:25.035513
# Unit test for function insert_rule
def test_insert_rule():
    cmd = push_arguments("iptables", '-I', params)
    module.run_command(cmd, check_rc=True)



# Generated at 2022-06-13 05:43:27.108705
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', None, dict(chain='INPUT', table='filter')) == 'ACCEPT'



# Generated at 2022-06-13 05:43:34.975585
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        action='append',
        state='present',
        limit='2/second',
        limit_burst='20',
        log_prefix='"IPTABLES:INFO: "',
        log_level='info',
        wait='',
        source='8.8.8.8',
        jump='DROP',
        comment='"foo"',
        ip_version='ipv4',
    )

# Generated at 2022-06-13 05:43:40.933374
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(chain='INPUT', ctstate=['RELATED', 'ESTABLISHED'],
                  jump='ACCEPT', comment='Test Rule')
    rule = construct_rule(params)
    assert rule == ['-j', 'ACCEPT', '-m', 'conntrack', '--ctstate',
                    'RELATED,ESTABLISHED', '-m', 'comment', '--comment', 'Test Rule']



# Generated at 2022-06-13 05:43:47.699502
# Unit test for function get_chain_policy
def test_get_chain_policy():
    out = """Chain relay_lan_in (policy ACCEPT)
target     prot opt source               destination
"""
    assert get_chain_policy(None, None, None) == None
    assert get_chain_policy(None, None, {}) == None
    assert get_chain_policy(None, None, dict(out='(policy None)')) == None
    assert get_chain_policy(None, None, dict(out=out)) == 'ACCEPT'
    out = """Chain relay_lan_in (policy TEST)
target     prot opt source               destination
"""
    assert get_chain_policy(None, None, dict(out=out)) == 'TEST'
    out = """Chain relay_lan_in (policy DROP)
target     prot opt source               destination
"""

# Generated at 2022-06-13 05:43:53.721933
# Unit test for function construct_rule