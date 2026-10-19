

# Generated at 2022-06-13 05:34:39.766208
# Unit test for function construct_rule

# Generated at 2022-06-13 05:34:52.766008
# Unit test for function construct_rule

# Generated at 2022-06-13 05:34:56.047537
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('iptables', 'module', {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'ACCEPT'
    }) == ['iptables', '-t', 'filter', '-P', 'INPUT', 'ACCEPT']



# Generated at 2022-06-13 05:35:00.586859
# Unit test for function insert_rule
def test_insert_rule():
    import subprocess
    for i in range(10):
        cmd = ['iptables', '-I', 'MOCK_CHAIN', str(i)]
        subprocess.Popen(cmd).wait()


# Generated at 2022-06-13 05:35:03.622724
# Unit test for function set_chain_policy
def test_set_chain_policy():
    params = dict(
        chain='INPUT',
        table='filter',
        policy='DROP',
    )
    assert [
        'iptables',
        '-t', params['table'],
        '-P', params['chain'], params['policy'],
    ] == set_chain_policy('iptables', None, params)



# Generated at 2022-06-13 05:35:11.176533
# Unit test for function push_arguments
def test_push_arguments():
    params = {
        'ip_version': 'ipv4',
        'table': 'nat',
        'chain': 'PREROUTING',
        'action': '-I'
    }
    iptables_path = BINS['ipv4']
    rule = '-t nat -I PREROUTING'
    cmd = push_arguments(iptables_path, params['action'], params, False)
    assert cmd == [iptables_path, rule]



# Generated at 2022-06-13 05:35:25.333351
# Unit test for function main

# Generated at 2022-06-13 05:35:30.061725
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = list()
    append_match_flag(rule, 'match', '--u32', False)
    assert rule == ['--u32']
    append_match_flag(rule, None, '--u32', False)
    assert rule == ['--u32']
    rule = list()
    append_match_flag(rule, 'negate', '--u32', True)
    assert rule == ['!', '--u32']
    append_match_flag(rule, None, '--u32', True)
    assert rule == ['!', '--u32']
# end unit test



# Generated at 2022-06-13 05:35:40.025046
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-A', {'table': 'mangle', 'chain': 'PREROUTING', 'protocol': 'tcp', 'source': '8.8.8.8', 'jump': 'DROP'}) == ['iptables', '-t', 'mangle', '-A', 'PREROUTING', '-s', '8.8.8.8', '-p', 'tcp', '-j', 'DROP']

# Generated at 2022-06-13 05:35:51.969821
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    flag = '--tcp-flags'
    param = {}
    param['flags'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags_set'] = ['ACK', 'RST', 'SYN', 'FIN']
    rule = append_tcp_flags(rule, param, flag)
    assert rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,RST,SYN,FIN']
    param['flags'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags_set'] = ['ACK', 'RST']
    rule = append_tcp_flags(rule, param, flag)
    assert rule == ['--tcp-flags', 'ACK,RST', 'ACK,RST,SYN,FIN']


# Generated at 2022-06-13 05:36:06.887230
# Unit test for function insert_rule

# Generated at 2022-06-13 05:36:16.511861
# Unit test for function append_rule
def test_append_rule():
    module = AnsibleModule({})
    params = dict(
        table='nat',
        chain='PREROUTING',
        in_interface='eth0',
        protocol='tcp',
        match='tcp',
        destination_port='80',
        jump='REDIRECT',
        to_ports='8600',
    )
    iptables_path = 'iptables'
    cmd = push_arguments(iptables_path, '-A', params)

# Generated at 2022-06-13 05:36:24.123374
# Unit test for function remove_rule

# Generated at 2022-06-13 05:36:28.461003
# Unit test for function flush_table
def test_flush_table():
    iptables_path = '/bin/iptables'
    module = AnsibleModule(argument_spec=dict())
    params = {'chain': 'chain_name', 'table': 'fiter'}
    flush_table(iptables_path, module, params)



# Generated at 2022-06-13 05:36:30.189480
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:36:35.271279
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_path = "iptables"
    class module(object):
        def run_command(self, cmd, check_rc):
            out = "v1.6.2"
            return 0, out, None
    ipt = get_iptables_version(iptables_path, module)
    assert ipt == "1.6.2"



# Generated at 2022-06-13 05:36:42.939176
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    import json
    rule = []
    param = {}
    flag = "--tcp-flags"
    param['flags_set'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags'] = ['ACK', 'RST', 'SYN', 'FIN']
    append_tcp_flags(rule, param, flag)
    t_rule = '[' + ','.join(["'./--tcp-flags'", "'ACK,RST,SYN,FIN'", "'ACK,RST,SYN,FIN'"]) + ']'
    assert t_rule == json.dumps(rule)
    rule = []
    param = {}
    flag = "--tcp-flags"
    param['flags_set'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags']

# Generated at 2022-06-13 05:36:52.000957
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})

# Generated at 2022-06-13 05:36:56.773433
# Unit test for function main
def test_main():
    # This unit test only tests for action "insert" and "append".
    # Since, the source code for "insert" and "append" are same
    # hence only testing for "insert" action.
    import os
    import sys
    import pytest
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from ansible.modules.network.iptables import main as iptables
    from ansible.module_utils.basic import AnsibleModule

    # Create the module instance

# Generated at 2022-06-13 05:36:58.423350
# Unit test for function append_rule
def test_append_rule():
    assert append_rule('iptables', '', '-A') == 'iptables -A'
    assert append_rule('iptables', '-t', '-A') == 'iptables -t -A'


# Generated at 2022-06-13 05:37:11.614270
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'INPUT', 'policy': 'ACCEPT', 'table': 'filter'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'chain': 'INPUT', 'policy': 'DROP', 'table': 'filter'}) == 'DROP'



# Generated at 2022-06-13 05:37:16.488859
# Unit test for function append_rule
def test_append_rule():
    module = AnsibleModule({})
    params = dict(
        table='filter',
        chain='INPUT',
        source='8.8.8.8',
        jump='DROP',
        wait='')
    cmd = push_arguments('iptables', '-A', params)
    assert cmd == ['iptables', '-t', 'filter', '-A', 'INPUT', '-s', '8.8.8.8', '-j', 'DROP']


# Generated at 2022-06-13 05:37:27.891257
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:33.568583
# Unit test for function get_chain_policy
def test_get_chain_policy():
    iptables_path = 'iptables'
    module = dict()
    module['run_command'] = lambda cmd, check_rc=True: (0, 'Chain INPUT (policy ACCEPT)', '')
    params = dict()
    params['ip_version'] = 'ipv4'
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    result = get_chain_policy(iptables_path, module, params)
    assert result == 'ACCEPT'



# Generated at 2022-06-13 05:37:36.658005
# Unit test for function remove_rule
def test_remove_rule():
    try:
        assert remove_rule('', '', {}) == 'iptables -D {}'.format('')
    except Exception as e:
        print('Error: {}'.format(e))


# Generated at 2022-06-13 05:37:43.071710
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    a = []
    append_tcp_flags(a, {'flags': [ 'ALL', 'NONE' ], 'flags_set': [ 'ACK', 'RST', 'SYN', 'FIN' ]}, '--tcp-flags')
    assert a == ['--tcp-flags', 'ALL,NONE', 'ACK,RST,SYN,FIN']


# Generated at 2022-06-13 05:37:51.591249
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class fake_module(object):
        def __init__(self, out):
            self.out = out
        def run_command(self, cmd, check_rc=True):
            self.cmd = cmd
            return 0, self.out, ''
    out = "\nChain INPUT (policy ACCEPT)\n"
    m = fake_module(out)
    params = dict(
        table='filter',
        chain='INPUT',
        ip_version='ipv4'
    )
    assert get_chain_policy('iptables', m, params) == 'ACCEPT'

    out = "\nChain OUTPUT (policy DROP)\n"
    m = fake_module(out)
    params = dict(
        table='filter',
        chain='OUTPUT',
        ip_version='ipv4'
    )

# Generated at 2022-06-13 05:38:01.102823
# Unit test for function append_rule
def test_append_rule():
    assert callable(append_rule)
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    setattr(module, 'run_command', lambda cmd, check_rc=True: (0, '', ''))
    params = dict(
        chain='INPUT',
        table='filter',
        protocol='tcp',
        jump='ACCEPT',
        source_port='1234',
        comment='my comment',
        source='8.8.8.8',
        ip_version='ipv4',
        wait='3',
    )
    cmd = append_rule('/usr/bin/iptables', module, params)

# Generated at 2022-06-13 05:38:14.717460
# Unit test for function append_rule
def test_append_rule():
    try:
        import ansible.modules.system.iptables
        iptables_path = ansible.modules.system.iptables
    except ImportError:
        import ansible.modules.network.iptables
        iptables_path = ansible.modules.network.iptables
    except ImportError:
        print("Module network.iptables not available")

    main_module = ansible.modules.system.iptables
    class TestAnsibleModule():
        def __init__(self):
            self.run_command = main_module.run_command
            self.check_mode = False
    # This will throw an exception if ansible-runner implementation class is not available
    import ansible.runner
    test_module = TestAnsibleModule()

# Generated at 2022-06-13 05:38:20.642755
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:41.027957
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        action='append',
        rule_num='5',
        ip_version=BINS.keys(),
        comment='"First rule"',
    )
    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp',
        '--dport', '8080',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', '"First rule"'
    ]



# Generated at 2022-06-13 05:38:54.970769
# Unit test for function get_chain_policy
def test_get_chain_policy():
    '''
    Some unit tests for the get_chain_policy.
    '''

    assert get_chain_policy(None, None, None) == None

    # Construct fake module
    module = type('FakeModule', (object,), {})()

    # Construct fake module.run_command
    def run_command(command, check_rc):
        '''
        Fake run_command.
        '''

        assert command[0].endswith('iptables')

        return 0, '''Chain INPUT (policy ACCEPT)
target     prot opt source               destination''', ''

    module.run_command = run_command

    assert get_chain_policy('iptables', module, {
        'chain': 'INPUT',
        'policy': 'ACCEPT',
        'table': 'filter'
    }) == 'ACCEPT'



# Generated at 2022-06-13 05:39:06.310546
# Unit test for function main
def test_main():
    mock_module = MagicMock()

    mock_module.run_command.return_value = (0, 'version 1.4.21', '')
    mock_module.check_mode = False
    mock_module.params = {
        'ip_version': 'ipv4',
        'table':'filter',
        'chain':'INPUT',
        'rule_num':'1',
        'protocol':'tcp',
        'source':'192.168.1.1',
        'destination':'192.168.1.2',
        'jump':'ACCEPT',
        'ctstate':['NEW'],
        'state':'present',
        'action':'append',
    }

    main()

# Generated at 2022-06-13 05:39:12.949909
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:24.473978
# Unit test for function construct_rule
def test_construct_rule():
    def test_form(params, output):
        rule = construct_rule(params)
        assert(rule == output)

    params = dict(
        chain='INPUT',
        jump='ACCEPT',
        wait='1',
        log_prefix='',
        comment='foo-bar'
    )
    output = ['-w', '1', '-j', 'ACCEPT', '--comment', 'foo-bar']
    test_form(params, output)

    params = dict(
        chain='INPUT',
        jump='DROP',
        wait='30',
        log_prefix='',
        comment='foo-bar'
    )
    output = ['-w', '30', '-j', 'DROP', '--comment', 'foo-bar']
    test_form(params, output)


# Generated at 2022-06-13 05:39:28.398906
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule({})
    result = check_present('iptables', module, {'ip_version': 'ipv4', 'chain': 'INPUT', 'table': 'filter'})
    assert result == False


# Generated at 2022-06-13 05:39:39.438141
# Unit test for function flush_table
def test_flush_table():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(
        argument_spec=dict(
            ip_version=dict(default='ipv4', choices=['ipv4', 'ipv6']),
            chain=dict(required=True, default=None),
            flush=dict(required=True),
        ),
    )
    params = {'ip_version': 'ipv4', 'chain': 'test', 'flush': True}
    flush_table(iptables_path, module, params)



# Generated at 2022-06-13 05:39:44.593190
# Unit test for function push_arguments

# Generated at 2022-06-13 05:39:51.625833
# Unit test for function append_param
def test_append_param():
    rule = []
    append_param(rule, ['one', 'two', 'three'], '--flag', True)
    assert rule == ['--flag', 'one', '--flag', 'two', '--flag', 'three']
    rule = []
    append_param(rule, ['!one', '!two', 'three'], '--flag', True)
    assert rule == ['!', '--flag', 'one', '!', '--flag', 'two', '--flag', 'three']
    rule = []
    append_param(rule, None, '--flag', False)
    assert rule == []
    rule = []
    append_param(rule, '', '--flag', False)
    assert rule == []
    rule = []
    append_param(rule, 'one', '--flag', False)

# Generated at 2022-06-13 05:40:03.958268
# Unit test for function main

# Generated at 2022-06-13 05:40:26.416863
# Unit test for function main

# Generated at 2022-06-13 05:40:31.157064
# Unit test for function check_present
def test_check_present():
    import json
    import ansible.module_utils.basic
    test_params = {
        "table": "filter",
        "chain": "INPUT",
        "protocol": "tcp",
        "destination": "192.168.1.1",
        "destination_port": "80",
        "jump": "ACCEPT"
    }
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert False == check_present("ipv6tables", module, test_params)


# Generated at 2022-06-13 05:40:32.517236
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert(get_chain_policy(None, None,
                            dict(table='filter', chain='INPUT', policy='ACCEPT'))
           == 'ACCEPT')



# Generated at 2022-06-13 05:40:34.358783
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'ip_version':'ipv4','chain': 'INPUT','table':'filter','policy':'ACCEPT'}) == 'ACCEPT'
# End of unit test



# Generated at 2022-06-13 05:40:40.348760
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = "/sbin/iptables"
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    params = {}
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    params['rule_num'] = '3'
    params['protocol'] = 'tcp'
    params['destination_port'] = '80'
    params['jump']= 'ACCEPT'
    ansible_args = module.parse_args()
    insert_rule(iptables_path, module, params)
    print(module.run_command("/sbin/iptables -S"))


# Generated at 2022-06-13 05:40:41.444529
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:40:47.688234
# Unit test for function main

# Generated at 2022-06-13 05:40:58.141756
# Unit test for function main
def test_main():
    
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.check_mode = False
            self.fail_json = None
            self.run_command = None
            
        def fail_json(self, msg):
            raise Exception(msg)
        
        def run_command(self, cmd, check_rc):
            return 0, None, None
            
        def get_bin_path(self, name, opt_dirs):
            return '/sbin/iptables'
        

# Generated at 2022-06-13 05:40:59.466886
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'policy':'DROP'} ) == 'DROP'


# Generated at 2022-06-13 05:41:02.794084
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    params = {}
    params['table'] = "filter"
    params['chain'] = "INPUT"
    iptables_path = 'iptables'
    out = get_chain_policy(iptables_path,module,params)
    assert out == None


# Generated at 2022-06-13 05:41:19.628082
# Unit test for function append_rule
def test_append_rule():
    assert True



# Generated at 2022-06-13 05:41:31.098450
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='192.168.1.0/24',
        jump='LOG',
        limit='5/m',
        log_prefix='MYPREFIX: ',
        log_level='err',
        comment='This is a comment',
        ip_version='ipv4',
        in_interface='eth0',
        out_interface='eth1',
        icmp_type='echo-request',
        match=['comment', 'conntrack'],
        ctstate=['NEW', 'INVALID'],
        set_counters='24',
        destination_port='22')

# Generated at 2022-06-13 05:41:41.017911
# Unit test for function check_present
def test_check_present():
    params = dict(
        table='filter',
        ip_version='ipv4',
        chain='INPUT',
        protocol='tcp',
        destination='1.1.1.1',
        destination_port='443',
        jump='ACCEPT',
        match=['state'],
        ctstate=['ESTABLISHED', 'RELATED'],
        syn='match',
        comment='Allow related and established connections',
    )
    expected_cmd = [
        'iptables',
        '-t', 'filter',
        '-C', 'INPUT',
    ]
    expected_cmd.extend(construct_rule(params))
    assert expected_cmd == push_arguments('iptables', '-C', params)



# Generated at 2022-06-13 05:41:49.235246
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:55.805756
# Unit test for function construct_rule
def test_construct_rule():
    # test construct_rule with no param (table,chain,name)
    params = dict(
        action='insert',
        name='test_rule',
        state='present',
        rule_num=1,
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == ['-I', 'INPUT', '1', '-m', 'comment', '--comment', 'test_rule']

    # test construct_rule with protocol in param
    params = dict(
        action='insert',
        name='test_rule',
        state='present',
        rule_num=1,
        ip_version='ipv4',
        protocol='tcp'
    )
    rule = construct_rule(params)

# Generated at 2022-06-13 05:41:58.261784
# Unit test for function get_chain_policy
def test_get_chain_policy():
    chain_policy = get_chain_policy('iptables', None, {'policy':'ACCEPT', 'chain':'INPUT'})
    assert chain_policy == "ACCEPT"


# Generated at 2022-06-13 05:42:07.808438
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:21.183441
# Unit test for function main

# Generated at 2022-06-13 05:42:26.614409
# Unit test for function get_chain_policy
def test_get_chain_policy():
    # Test policy_set = False
    params = dict(
        chain='INPUT',
        table='filter',
        policy=None,
    )
    assert get_chain_policy("iptables", None, params) == None

    # Test policy_set = True
    params = dict(
        chain='INPUT',
        table='filter',
        policy='ACCEPT',
    )
    assert get_chain_policy("iptables", None, params) == 'ACCEPT'



# Generated at 2022-06-13 05:42:27.927503
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:51.995418
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('iptables', 'iptables v1.6.0') == '1.6.0'



# Generated at 2022-06-13 05:42:58.822899
# Unit test for function insert_rule
def test_insert_rule():
    import os
    import collections
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            k=dict(required=True, type='str'),
        ),
        supports_check_mode=True,
    )
    ansible.module_utils.basic.AnsibleModule = my_AnsibleModule
    cmd = push_arguments("/sbin/iptables", "/test/ansible_modlib.basic.py", "-I", params)
    assert(cmd == ['/sbin/iptables', '-t', 'filter', '-A', 'INPUT', '-j', 'ACCEPT'])

# Generated at 2022-06-13 05:43:04.114878
# Unit test for function check_present
def test_check_present():
    import os, tempfile
    from ansible.module_utils.basic import AnsibleModule
    # Create a temporary file in this directory
    fd, tmpfile = tempfile.mkstemp()
    # Use the temporary file as stdin

# Generated at 2022-06-13 05:43:17.055339
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:23.673964
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:32.850657
# Unit test for function append_rule
def test_append_rule():
    '''
    Append rule of module iptables.
    '''
    # Create the module instance

# Generated at 2022-06-13 05:43:33.597699
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('a', 'b', 'c') == None



# Generated at 2022-06-13 05:43:37.975814
# Unit test for function push_arguments
def test_push_arguments():
    data = {
        'name': 'test',
        'chain': 'INPUT',
        'action': '',
        'protocol': 'tcp',
        'ip_version': 'ipv4',
        'source': '192.168.0.1',
        'destination': None,
        'in_interface': None,
        'destination_port': '23',
        'to_destination': None,
        'jump': 'DROP',
        'table': 'filter',
        'reject_with': 'icmp-port-unreachable',
        'icmp_type': None,
        'tcp_flags': None,
        'comment': None,
        'log_prefix': None,
        'log_level': None
    }
    rule = ['iptables']

# Generated at 2022-06-13 05:43:44.146175
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, 'INPUT') == 'ACCEPT'
    assert get_chain_policy('iptables', {}, 'FORWARD') == 'ACCEPT'
    assert get_chain_policy('iptables', {}, 'OUTPUT') == 'ACCEPT'
    assert get_chain_policy('iptables', {}, 'NONEXISTENT') is None

# Generated at 2022-06-13 05:43:46.364095
# Unit test for function flush_table
def test_flush_table():
    cmd_test = 'iptables -t nat -F'
    result = flush_table('iptables', 'module', dict(table='nat'))
    assert result == cmd_test
