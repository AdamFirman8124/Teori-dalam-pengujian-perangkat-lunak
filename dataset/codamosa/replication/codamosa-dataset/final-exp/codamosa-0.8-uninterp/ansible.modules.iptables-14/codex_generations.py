

# Generated at 2022-06-13 05:34:26.524518
# Unit test for function construct_rule

# Generated at 2022-06-13 05:34:33.905534
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule({'iptables_path': '/sbin/iptables', 'table': 'filter', 'chain': 'INPUT', 'flush': True})
    flush_table(module.params['iptables_path'], module, module.params)



# Generated at 2022-06-13 05:34:37.010973
# Unit test for function check_present
def test_check_present():
    assert check_present(iptables_path, module, params)


# Generated at 2022-06-13 05:34:43.466523
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/usr/bin/iptables_mock'
    params = {
        'chain': 'INPUT',
        'ip_version': 'ipv4',
        'policy': 'DROP',
    }
    function_result = set_chain_policy(iptables_path, 'module', params)
    assert function_result == ['/usr/bin/iptables_mock', '-t', 'filter', '-P', 'INPUT', 'DROP']



# Generated at 2022-06-13 05:34:54.871595
# Unit test for function check_present
def test_check_present():
    _iptables_path = "/sbin/iptables"

# Generated at 2022-06-13 05:35:06.050823
# Unit test for function push_arguments
def test_push_arguments():
    assert_equal(
        push_arguments('/sbin/iptables', '-A', dict(table='filter', chain='INPUT')),
        ['/sbin/iptables', '-t', 'filter', '-A', 'INPUT'])
    assert_equal(
        push_arguments('/sbin/iptables', '-A', dict(table='filter', chain='INPUT', comment='Hello world')),
        ['/sbin/iptables', '-t', 'filter', '-A', 'INPUT', '-m', 'comment', '--comment', 'Hello world'])

# Generated at 2022-06-13 05:35:08.386969
# Unit test for function set_chain_policy
def test_set_chain_policy():
    args = dict(
        chain='INPUT',
        table='filter',
        policy='DROP'
    )
    rc, out, err = module.run_command(push_arguments('iptables', '-P', args, make_rule=False), check_rc=True)
    assert rc == 0, err



# Generated at 2022-06-13 05:35:11.286903
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, params) == True



# Generated at 2022-06-13 05:35:21.403995
# Unit test for function push_arguments
def test_push_arguments():
    iptables_path = '/sbin/iptables'
    action = '-A'
    params = dict(
        source='0.0.0.0',
        jump='ACCEPT',
        chain='INPUT',
        table='filter',
    )
    cmd = push_arguments(iptables_path, action, params, True)
    expected = [
        '/sbin/iptables',
        '-t',
        'filter',
        '-A',
        'INPUT',
        '-s',
        '0.0.0.0',
        '-j',
        'ACCEPT',
    ]
    assert cmd == expected

# Generated at 2022-06-13 05:35:26.733886
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec=dict())
    assert get_chain_policy('/path/iptables', module, {'policy':'DROP', 'chain':'INPUT'}) == 'DROP'
    assert get_chain_policy('/path/iptables', module, {'policy':'', 'chain':'FORWARD'}) == None


# Generated at 2022-06-13 05:35:46.789841
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    append_match_flag(rule, 'match', '--syn', True)
    assert rule == ['--syn']
    rule = []
    append_match_flag(rule, 'negate', '--syn', True)
    assert rule == ['!', '--syn']
    rule = []
    append_match_flag(rule, 'match', '--syn', False)
    assert rule == ['--syn']



# Generated at 2022-06-13 05:35:56.690692
# Unit test for function main

# Generated at 2022-06-13 05:36:03.621334
# Unit test for function append_rule
def test_append_rule():
    params = {'table': 'filter',
              'chain': 'INPUT',
              'protocol': 'tcp',
              'jump': 'ACCEPT',
              'ip_version': 'ipv4'}
    check_present(BINS['ipv4'], module, params)
    append_rule(BINS['ipv4'], module, params)



# Generated at 2022-06-13 05:36:11.671547
# Unit test for function construct_rule
def test_construct_rule():
    chain_param = 'INPUT'
    params = dict(
        chain=chain_param,
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        action='append',
        rule_num=5,
    )
    assert construct_rule(params) == ['-w', '-A', chain_param, '-p', 'tcp',
                                      '--destination-port', '8080', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:36:23.128217
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='10.0.0.0/8',
        destination='8.8.8.8',
        match='state',
        ctstate='NEW,RELATED',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
        ip_version='ipv4',
    )
    rule = construct_rule(params)

# Generated at 2022-06-13 05:36:25.009065
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(table='filter', chain='INPUT', ip_version='ipv4')) == 'ACCEPT'

# Generated at 2022-06-13 05:36:34.549014
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import sys
    import mock
    class MyModule(object):
        def __init__(self):
            self.exit_json = mock.MagicMock()
            self.return_value = {
                "ipv4": {
                    "added": [],
                    "removed": []
                },
                "ipv6": {
                    "added": [],
                    "removed": []
                },
                "changed": False
            }
            self.fail_json = mock.MagicMock()
            self.check_mode = False
            self.fail_json = mock.MagicMock()
            self.params = {}
            self.ansible_version = '2.5.1'

# Generated at 2022-06-13 05:36:41.109548
# Unit test for function set_chain_policy
def test_set_chain_policy():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = lambda _, x: '/bin/bin/iptables'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'ip_version': 'ipv4',
        'policy': 'DROP'
    }
    set_chain_policy('/bin/bin/iptables', module, params)
    assert module.run_command.called
    module.run_command.assert_called_once_with(
        ['/bin/bin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP'],
        check_rc=True)



# Generated at 2022-06-13 05:36:50.061478
# Unit test for function remove_rule
def test_remove_rule():
    params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
        source='192.168.0.3',
        jump='DROP',
        protocol='tcp',
        destination_port=8080
    )
    cmd = push_arguments("iptables", '-D', params)
    assert cmd == [
        "iptables",
        "-t",
        "filter",
        "-D",
        "INPUT",
        "-s",
        "192.168.0.3",
        "-p",
        "tcp",
        "--dport",
        "8080",
        "-j",
        "DROP"
    ]


# Generated at 2022-06-13 05:36:52.781621
# Unit test for function remove_rule
def test_remove_rule():
    check_present(iptables_path, module, params)
    append_rule(iptables_path, module, params)
    remove_rule(iptables_path, module, params)



# Generated at 2022-06-13 05:37:13.555411
# Unit test for function insert_rule
def test_insert_rule():
    module = AnsibleModule({})
    params = dict(
        chain='INPUT',
        rule_num=5,
        ip_version='ipv4',
        protocol='tcp',
        destination_port=8080,
        jump='ACCEPT',
        )
    iptables_path = 'iptables'

    cmd = push_arguments(iptables_path, '-I', params)
    assert cmd == [iptables_path, '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']



# Generated at 2022-06-13 05:37:21.141181
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import os
    import shutil
    iptables_path = BINS['ipv4']
    iptables_rules = '/tmp/iptables-rules'
    with open(iptables_path, 'rb') as f_iptables:
        shutil.copyfileobj(f_iptables, open(iptables_rules, 'wb'))
    params = dict(table='filter', chain='INPUT', policy='DROP')
    chain_policy = get_chain_policy(iptables_rules, None, params)
    assert chain_policy == 'ACCEPT', chain_policy
    os.unlink(iptables_rules)



# Generated at 2022-06-13 05:37:32.063469
# Unit test for function main

# Generated at 2022-06-13 05:37:44.915787
# Unit test for function insert_rule
def test_insert_rule():
    args = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        action='insert',
        rule_num='5',
    )


# Generated at 2022-06-13 05:37:55.263949
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule({
        'protocol': 'tcp',
        'source': '192.0.2.0/24',
        'match': ['state', 'recent'],
        'jump': 'ACCEPT',
    }) == [
        '-p', 'tcp',
        '-s', '192.0.2.0/24',
        '-m', 'state',
        '--state', 'NEW',
        '-m', 'recent',
        '--set',
        '-j', 'ACCEPT',
    ]

# Generated at 2022-06-13 05:38:08.303972
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:14.375481
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        ip_version='ipv4',
        source='8.8.8.8',
        jump='DROP'
    )) == ['--ipv4', '-s', '8.8.8.8', '-j', 'DROP']

    assert construct_rule(dict(
        ip_version='ipv4',
        source='8.8.8.8',
        protocol='tcp',
        jump='DROP'
    )) == ['--ipv4', '-s', '8.8.8.8', '-p', 'tcp', '-j', 'DROP']


# Generated at 2022-06-13 05:38:15.610816
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert(get_iptables_version('iptables', '1.6.1') == '1.6.1')



# Generated at 2022-06-13 05:38:25.146014
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = "iptables"
    module = AnsibleModule
    params = dict()
    params['table'] = 'nat'
    params['chain'] = 'PREROUTING'
    params['protocol'] = 'tcp'
    params['destination_port'] = "80"
    params['jump'] = 'REDIRECT'
    params['to_ports'] = '8600'
    params['comment'] = "Redirect web traffic to port 8600"
    params['rule_num'] = '5'
    insert_rule(iptables_path, module, params)


# Generated at 2022-06-13 05:38:29.259070
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    append_tcp_flags(rule, {'flags': ['ACK'], 'flags_set': ['ACK']}, '--tcp-flags')
    assert rule == ['--tcp-flags', 'ACK', 'ACK']



# Generated at 2022-06-13 05:38:58.311439
# Unit test for function main
def test_main():
    ip_version = 'ipv4'
    table = 'filter'
    chain = 'INPUT'
    flush = False
    rule = '-p tcp --destination-port 22'
    state = 'present'


    class TestModule(object):
        def __init__(self, ip_version, table, chain, flush, rule, state):
            self.params = dict(
                ip_version=ip_version,
                table=table,
                chain=chain,
                flush=flush,
                rule=rule,
                state=state,
            )


# Generated at 2022-06-13 05:39:07.665004
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:15.465786
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    import sys
    import os

    iptables_path = get_bin_path('iptables')
    if not iptables_path:
        sys.exit('iptables was not found. Try to install iptables.')
    iptables_version = get_iptables_version(iptables_path, basic.AnsibleModule(
        argument_spec=dict()))
    assert isinstance(iptables_version, str)
    assert iptables_version.strip()



# Generated at 2022-06-13 05:39:17.494285
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('/sbin/iptables', None) == '1.4.21'



# Generated at 2022-06-13 05:39:22.077727
# Unit test for function flush_table

# Generated at 2022-06-13 05:39:23.248612
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert callable(set_chain_policy), \
        "Function set_chain_policy has no definition"


# Generated at 2022-06-13 05:39:27.825113
# Unit test for function get_chain_policy
def test_get_chain_policy():
    if get_chain_policy('iptables', None, dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
    )) == 'ACCEPT':
        print("Success: get_chain_policy")
    else:
        print("Failure: get_chain_policy")



# Generated at 2022-06-13 05:39:40.199847
# Unit test for function flush_table
def test_flush_table():
    assert flush_table('iptables', 'module', {'table':'nat', 'chain':'PREROUTING'}) == ['iptables', '-t', 'nat', '-F', 'PREROUTING']
    assert flush_table('iptables', 'module', {'table':'filter', 'chain':'INPUT'}) == ['iptables', '-t', 'filter', '-F', 'INPUT']
    assert flush_table('iptables', 'module', {'table':'mangle', 'chain':'FORWARD'}) == ['iptables', '-t', 'mangle', '-F', 'FORWARD']


# Generated at 2022-06-13 05:39:46.416450
# Unit test for function main
def test_main():
    # Does not work on Travis CI, so disabled
    return
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    try:
        __main__(module)
    except SystemExit as e:
        sys.exit(e)
    except Exception as ex:
        traceback.print_exc()
        sys.exit(1)



# Generated at 2022-06-13 05:39:48.307630
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy() == 'ACCEPT'


# Generated at 2022-06-13 05:40:02.125634
# Unit test for function append_rule
def test_append_rule():
    prepare_test_params()
    print(append_rule(params['iptables_path'], params['module'], params))


# Generated at 2022-06-13 05:40:15.000322
# Unit test for function construct_rule
def test_construct_rule():
    for ip_version in ['ipv4', 'ipv6']:
        assert construct_rule(dict(
            protocol='tcp',
            source='127.0.0.1',
            jump='ACCEPT',
            source_port='10001',
            ip_version=ip_version)) == [
            '-p', 'tcp', '-s', '127.0.0.1', '-m', 'multiport',
            '-m', 'owner', '--source-port', '10001', '-j', 'ACCEPT']

# Generated at 2022-06-13 05:40:22.553649
# Unit test for function main

# Generated at 2022-06-13 05:40:34.498196
# Unit test for function main

# Generated at 2022-06-13 05:40:39.898989
# Unit test for function check_present
def test_check_present():
    assert check_present("iptables", None, {"table":"filter", "chain":"INPUT", "protocol":"tcp", "destination_port":"22", "ctstate":"NEW", "syn":"match", "jump":"ACCEPT", "comment":"Accept new SSH connections.", "ip_version":"ipv4"})
    assert not check_present("iptables", None, {"table":"filter", "chain":"INPUT", "protocol":"tcp", "destination_port":"22", "ctstate":"NEW", "syn":"match", "jump":"DROP", "comment":"Accept new SSH connections.", "ip_version":"ipv4"})



# Generated at 2022-06-13 05:40:46.408442
# Unit test for function check_present
def test_check_present():
    module = MagicMock()
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port=80,
        jump='ACCEPT',
    )
    iptables_path = '/usr/sbin/iptables'
    cmd = push_arguments(iptables_path, '-C', params)
    rc = 0
    module.run_command.return_value = (rc, '', '')
    assert check_present(iptables_path, module, params) is True
    assert module.run_command.called is True
    assert module.run_command.call_args[0] == (cmd, )
    assert module.run_command.call_args[1] == dict(check_rc=False)
    module.reset_mock()
    rc = 1
    module.run

# Generated at 2022-06-13 05:40:50.298685
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(chain='testing')) == None
    assert get_chain_policy(None, None, dict(chain='INPUT')) == 'ACCEPT'



# Generated at 2022-06-13 05:40:54.414548
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {},{
        'policy': 'ACCEPT',
        'table': 'filter',
        'chain': 'INPUT',
        'state': 'present',
        '_ansible_check_mode': True,
    }) == 'ACCEPT'



# Generated at 2022-06-13 05:41:01.713846
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:06.101374
# Unit test for function set_chain_policy
def test_set_chain_policy():
    cmd_result = {
        "changed": True,
        "stderr": "",
        "stdout": "",
        "stdout_lines": [],
        "warnings": []
    }
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda cmd, check_rc=False: cmd_result
    iptables_path = "/usr/sbin/iptables"
    params = {
        "table": "filter",
        "chain": "INPUT",
        "policy": "ACCEPT",
        "ip_version": "ipv4",
    }
    assert set_chain_policy(iptables_path, module, params) == None



# Generated at 2022-06-13 05:41:48.431354
# Unit test for function main

# Generated at 2022-06-13 05:41:56.584748
# Unit test for function get_chain_policy
def test_get_chain_policy():
    """
    Execute unit test for get_chain_policy
    """
    cmd = 'iptables --check -L INPUT'
    rc, out, _ = module.run_command(cmd, check_rc=True)
    chain_header = out.split("\n")[0]
    #print(chain_header)
    result = re.search(r'\(policy ([A-Z]+)\)', chain_header)
    #print(result.group(1))
    return result



# Generated at 2022-06-13 05:42:06.458520
# Unit test for function push_arguments
def test_push_arguments():
    '''
    Test function push_arguments
    '''
    params = {
        "table": "filter",
        "chain": "INPUT",
        "rule_num": "1",
        "protocol": "tcp",
        "destination_port": "8080",
        "jump": "ACCEPT"
    }
    t = ['/sbin/iptables', '-t', 'filter', '-A', 'INPUT']
    t.extend(construct_rule(params))
    # Test if action is insert with rule_num
    a = push_arguments('/sbin/iptables', '-I', params)
    assert a == t
    # Test if action is append
    a = push_arguments('/sbin/iptables', '-A', params)
    assert a == t
   

# Generated at 2022-06-13 05:42:13.099269
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:42:18.209687
# Unit test for function insert_rule
def test_insert_rule():
    from ansible.modules.network.firewall import iptables
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.compat.version import LooseVersion

    module_args = dict(
        chain='INPUT',
        source='8.8.8.8',
        jump='DROP',
        rule_num=5,
        table='filter',
        wait='2s'
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    ipv = "ipv4"
    iptables_path = iptables.BINS[ipv]
    iptables.insert_rule(iptables_path, module, module_args)



# Generated at 2022-06-13 05:42:28.084010
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({'chain': 'INPUT'})

# Generated at 2022-06-13 05:42:36.635453
# Unit test for function set_chain_policy
def test_set_chain_policy():
    module = AnsibleModule(argument_spec = {
        "chain": {"type": "str", "required": True},
        "policy": {"type": "str", "required": True},
        "table": {"type": "str", "default": "filter", "choices": ["filter", "nat", "mangle", "raw", "security"]},
        "ip_version": {"type": "str", "default": "ipv4", "choices": ["ipv4", "ipv6"]},
        "wait": {"type": "str"}
    })
    print(construct_rule(module.params))


# Generated at 2022-06-13 05:42:42.509406
# Unit test for function construct_rule
def test_construct_rule():
    assert(construct_rule(dict(
        ip_version='ipv4',
        protocol='tcp',
        source='8.8.8.8',
        jump='DROP',
    )) == ['iptables', '-s', '8.8.8.8', '-p', 'tcp', '-j', 'DROP'])



# Generated at 2022-06-13 05:42:44.122835
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:55.639491
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_native


# Generated at 2022-06-13 05:43:48.756019
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec=dict())