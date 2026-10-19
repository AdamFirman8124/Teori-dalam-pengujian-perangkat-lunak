

# Generated at 2022-06-13 05:34:39.736920
# Unit test for function main

# Generated at 2022-06-13 05:34:51.373680
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    rule_param = dict(flags=['ACK', 'RST', 'SYN', 'FIN'], flags_set=['ACK', 'RST', 'SYN', 'FIN'])
    append_tcp_flags(rule, rule_param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,RST,SYN,FIN']
    rule = []
    rule_param = dict(flags=['ACK', 'RST', 'SYN', 'FIN'], flags_set=['ACK', 'SYN'])
    append_tcp_flags(rule, rule_param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,SYN']



# Generated at 2022-06-13 05:34:58.744676
# Unit test for function push_arguments
def test_push_arguments():
    bin_path = '/sbin/iptables'
    action = '-I'
    params = dict(
        table='filter',
        chain='INPUT',
        rule_num='5'
        )
    cmd = [
        bin_path,
        '-t',
        params['table'],
        action,
        params['chain'],
        params['rule_num']
    ]
    assert push_arguments(bin_path, action, params, False) == cmd
    assert push_arguments(bin_path, action, params) != cmd
# -------------------------------------------------------------------------


# Generated at 2022-06-13 05:35:01.189954
# Unit test for function flush_table
def test_flush_table():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(
        table=dict(type='str', choices=['filter', 'nat', 'mangle'], required=True),
        chain=dict(type='str', required=True),
    ))
    flush_table('/sbin/iptables', module, dict(table='filter', chain='INPUT'))



# Generated at 2022-06-13 05:35:07.484366
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec={})
    params = dict(
        table='filter',
        chain='INPUT',
        destination='8.8.8.8',
        jump='DROP',
    )
    assert check_present('iptables', module, params) is True



# Generated at 2022-06-13 05:35:22.717292
# Unit test for function construct_rule
def test_construct_rule():
    """Unit test for function construct_rule"""
    ipv4_rule = construct_rule({
        'action': 'append',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '80',
        'limit': '2/second',
        'limit_burst': '20',
        'jump': 'ACCEPT',
        'comment': 'rule',
        'ip_version': 'ipv4',
        'state': 'present',
        'wait': '5'
    })

# Generated at 2022-06-13 05:35:23.087933
# Unit test for function check_present
def test_check_present():
    pass



# Generated at 2022-06-13 05:35:26.286383
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('/sbin/iptables', None, {'table': 'filter', 'chain': 'INPUT', 'policy': 'DROP', 'ip_version': 'ipv4'})



# Generated at 2022-06-13 05:35:35.537805
# Unit test for function get_chain_policy
def test_get_chain_policy():
    print('Testing get_chain_policy')
    iptables_path = '/sbin/iptables'
    chain_name = 'INPUT'
    module_params = dict(
        chain=chain_name,
        table='filter',
        ip_version='ipv4',
    )
    cmd = push_arguments(iptables_path, '-L', module_params, make_rule=False)
    policy = get_chain_policy(iptables_path, None, module_params)
    assert policy == 'ACCEPT'
    print('get_chain_policy: OK')
test_get_chain_policy()



# Generated at 2022-06-13 05:35:43.638684
# Unit test for function main
def test_main():
    iptables_path = '/sbin/iptables'

# Generated at 2022-06-13 05:35:59.973713
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(
        argument_spec = dict(
            table = dict(default='filter', choices=['filter', 'nat', 'mangle', 'raw', 'security']),
            chain = dict(required=True),
            ip_version = dict(default='ipv4', choices=['ipv4', 'ipv6']),
            iptables_path = dict(default=BINS['ipv4']),
        ),
        supports_check_mode=False,
    )
    params = module.params.copy()
    assert get_chain_policy(params['iptables_path'], module, params) == 'DROP'


# Generated at 2022-06-13 05:36:08.728569
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec={})
    module.params = {
        'chain': 'INPUT',
        'table': 'filter',
        'ip_version': 'ipv4'
    }
    assert get_chain_policy(BINS[module.params['ip_version']], module, module.params) == None
    module.params['table'] = 'nat'
    assert get_chain_policy(BINS[module.params['ip_version']], module, module.params) == None



# Generated at 2022-06-13 05:36:10.773638
# Unit test for function get_iptables_version
def test_get_iptables_version():
    module = MockANSIModule()

    assert get_iptables_version(None, module) == '1.4.21'

# Generated at 2022-06-13 05:36:18.503001
# Unit test for function insert_rule

# Generated at 2022-06-13 05:36:22.554396
# Unit test for function construct_rule
def test_construct_rule():
    try:
        assert construct_rule({'comment': 'abc'}) == ['-m', 'comment', '--comment', 'abc']
    except AssertionError:
        raise Exception('Failed to construct rule')



# Generated at 2022-06-13 05:36:24.523500
# Unit test for function flush_table
def test_flush_table():
    cmd = ['/sbin/iptables', '-t', 'filter', '-F', 'INPUT']
    return cmd
# Test End



# Generated at 2022-06-13 05:36:26.470024
# Unit test for function check_present
def test_check_present():
    params = {'chain':'INPUT', 'protocol': 'tcp',
              'destination_port': 22, 'ctstate': 'NEW', 'syn': 'match',
              'jump': 'ACCEPT', 'comment': 'Accept new SSH connections.'}
    assert check_present('/usr/sbin/iptables', module, params) == False



# Generated at 2022-06-13 05:36:27.675266
# Unit test for function remove_rule
def test_remove_rule():
    res = remove_rule('test', 'test', 'test')
    return res



# Generated at 2022-06-13 05:36:36.620432
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import os
    import tempfile

    TESTFILE = """
Chain INPUT (policy DROP)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
"""

    # save iptables-save output to TESTFILE
    (fd, fname) = tempfile.mkstemp()
    os.close(fd)
    with open(fname, 'w') as file:
        file.write(TESTFILE)

    test_params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT'
    )


# Generated at 2022-06-13 05:36:41.952458
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule(argument_spec={})
    module.params = dict(
        action='get_chain_policy',
        chain='filter',
        table='filter',
        flush='no',
        ip_version='ipv4',
    )
    iptables_path = BINS['ipv4']
    assert get_chain_policy(iptables_path, module, module.params)



# Generated at 2022-06-13 05:37:16.816193
# Unit test for function construct_rule
def test_construct_rule():
    """
    Function construct_rule
    """
    def test(params, expected_rule, ip_version='ipv4'):
        """
        Do the test
        """
        if not isinstance(expected_rule, list):
            expected_rule = [expected_rule]
        current_rule = construct_rule(dict({'ip_version': ip_version}, **params))
        if expected_rule != current_rule:
            raise AssertionError("construct_rule(%s) returned '%s' instead of '%s'" % (
                params, ' '.join(current_rule), ' '.join(expected_rule)))
    test(
        dict(jump='ACCEPT'),
        '-j ACCEPT',
    )

# Generated at 2022-06-13 05:37:22.426402
# Unit test for function flush_table
def test_flush_table():
    rev = ''
    cmd = ['/sbin/iptables',
           '-t',
           'filter',
           '-F',
           'INPUT',
           '1.2.3.4',
           '-s',
           '1.2.3.4',
           '-p',
           'tcp',
           '--sport',
           'sport_value'
           ]
    params = {'table': 'filter', 'chain': 'INPUT', 'ip_version': 'ipv4', 'source': '1.2.3.4', 'destination': '1.2.3.4', 'protocol': 'tcp',
              'source_port': 'sport_value', 'nnp': False, 'ip_version': 'ipv4'}

# Generated at 2022-06-13 05:37:32.147837
# Unit test for function construct_rule
def test_construct_rule():
    params1 = dict(
        ip_version='ipv4',
        protocol='tcp',
        source='10.0.0.1',
        destination='10.0.0.2',
        match=['iprange'],
        src_range='10.0.0.1-10.0.0.100',
        dst_range='10.0.0.200-10.0.0.255',
        jump='ACCEPT',
        set_counters='1234, 1345',
        source_port='8023',
        destination_port='80',
        to_ports='9000',
        uid_owner='48',
        limit='12/minute',
        limit_burst='15',
        comment='This is a test comment',
        wait='1',
    )

# Generated at 2022-06-13 05:37:46.537157
# Unit test for function main

# Generated at 2022-06-13 05:38:00.243621
# Unit test for function check_present
def test_check_present():
    from ansible.module_utils import basic
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible_collections.ansible.netcommon.plugins.modules.network.netcommon import iptables

    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)



# Generated at 2022-06-13 05:38:13.343023
# Unit test for function append_rule
def test_append_rule():
    iptables_path = 'iptables'

# Generated at 2022-06-13 05:38:16.162545
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:38:25.268305
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:31.120579
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        log_prefix="IPTABLES:INFO: ",
        log_level="info",
        match=['limit'],
        limit='2/second',
        limit_burst='20',

    )
    rule = construct_rule(params)
    assert rule == [
        '--log-prefix', 'IPTABLES:INFO: ',
        '--log-level', 'info',
        '-m', 'limit',
        '--limit', '2/second',
        '--limit-burst', '20',
        '-p', 'tcp',
        '--destination-port', '80',
        '-j', 'ACCEPT'
    ]



# Generated at 2022-06-13 05:38:41.648457
# Unit test for function get_chain_policy
def test_get_chain_policy():
    def test_out(value):
        return out
    params = {
        'ip_version': 'ipv4',
        'chain': 'INPUT',
        'policy': 'ACCEPT'
    }
    module = MagicMock()
    module.run_command.return_value = (0, test_out('''Chain INPUT (policy ACCEPT)
 target     prot opt source               destination
 ACCEPT     all  --  anywhere             anywhere
'''), '')
    # check iptables version for policy support
    iptables_path = 'iptables'
    assert get_chain_policy('iptables', module, params) == 'ACCEPT'
    module.run_command.return_value = (0, test_out('''Chain INPUT (policy ACCEPT)'''), '')
    assert get_chain_policy

# Generated at 2022-06-13 05:40:01.169364
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('/sbin/iptables', test_module, test_params) == 'expected_cmd'
    assert remove_rule('/sbin/iptables', test_module, test_params) == 'expected_cmd'



# Generated at 2022-06-13 05:40:14.139555
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:16.604141
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('', '', {'policy': 'ACCEPT'}) == 'ACCEPT'
    assert get_chain_policy('', '', {}) is None



# Generated at 2022-06-13 05:40:26.849855
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:31.067352
# Unit test for function append_rule
def test_append_rule():
    assert append_rule("/usr/bin/iptables", "test", {
        'chain': 'INPUT',
        'table': 'filter',
        'protocol': 'tcp',
        'destination': '1.2.3.4',
        'destination_port': '22',
        'jump': 'ACCEPT',
        'comment': 'this is a comment',
    }) == [
        '/usr/bin/iptables',
        '-t', 'filter',
        '-A', 'INPUT',
        '-p', 'tcp',
        '-d', '1.2.3.4',
        '--dport', '22',
        '-m', 'comment',
        '--comment', 'this is a comment',
        '-j', 'ACCEPT'
    ]

# Unit test

# Generated at 2022-06-13 05:40:36.293955
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class Module():
        def __init__(self):
            self.run_command_rc = 0
            self.run_command_out = "Chain INPUT (policy ACCEPT)\n"
        def run_command(self, cmd, check_rc):
            self.run_command_cmd = cmd
            return (self.run_command_rc, self.run_command_out)
    module = Module()
    params = dict(
        table='filter',
        chain='INPUT',
    )
    cmd = push_arguments('/sbin/iptables', '-L', params, make_rule=False)
    result = get_chain_policy('/sbin/iptables', module, params)
    assert result == 'ACCEPT'
    # Test when chain_header doesn't have policy
    module.run_command_out

# Generated at 2022-06-13 05:40:47.782586
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(
        dict(ip_version='ipv4',
             destination_port='80')) == ['-p', 'tcp', '--dport', '80']
    assert construct_rule(
        dict(ip_version='ipv6',
             destination_port='80')) == ['-p', 'tcp', '--dport', '80']


# Generated at 2022-06-13 05:40:52.858490
# Unit test for function append_rule

# Generated at 2022-06-13 05:40:54.719798
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert 'ACCEPT' == get_chain_policy([],[],{'chain':'INPUT', 'policy':'ACCEPT'})



# Generated at 2022-06-13 05:40:59.170907
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = AnsibleModule({})
    iptables_path = 'iptables'
    params = {
        'chain': 'INPUT',
        'table': 'filter',
        'ip_version': 'ipv4',
    }
    result = get_chain_policy(iptables_path, module, params)
    assert result == 'DROP'



# Generated at 2022-06-13 05:43:00.785573
# Unit test for function main
def test_main():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, **kwargs):
            raise Exception('FAILED')

        def exit_json(self, **kwargs):
            raise Exception('DONE')

        def run_command(self, cmd, check_rc=True):
            if cmd == 'iptables --version':
                return 0, 'iptables v1.4.7\n', ''
            elif cmd == 'ip6tables --version':
                return 0, 'ip6tables v1.4.7\n', ''
            return 0, '', ''

        def get_bin_path(self, executable, required=False):
            return 'path/to/{}'.format(executable)

    # Try a simple append

# Generated at 2022-06-13 05:43:06.376096
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:17.398118
# Unit test for function check_present
def test_check_present():
    module, params = get_module_params()
    params['protocol'] = 'tcp'
    params['jump'] = 'accept'
    cmd = push_arguments('iptables', '-C', params)
    assert cmd == ['iptables', '-t', 'filter', '-C', 'INPUT', '-p', 'tcp', '-j', 'ACCEPT'] == ['iptables', '-t', 'filter', '-C', 'INPUT', '-p', 'tcp', '-j', 'ACCEPT']
    rc = 0
    out=''
    err=''
    assert check_present('iptables', module, params) == True



# Generated at 2022-06-13 05:43:23.854201
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:27.163962
# Unit test for function flush_table
def test_flush_table():
    iptables_path = 'iptables'
    module = AnsibleModule()
    params = {
        'table': 'filter',
        'chain': 'INPUT',
    }
    flush_table(iptables_path, module, params)



# Generated at 2022-06-13 05:43:29.994155
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'DUMMY'}) is None
    assert get_chain_policy(None, None, {'chain': 'INPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:43:32.164492
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', 'module', {'table': 'filter',
                                                   'chain': 'INPUT'}) == 'DROP'



# Generated at 2022-06-13 05:43:33.920633
# Unit test for function append_rule
def test_append_rule():
    assert(append_rule('table:nat', 'proto:tcp') == ['-t', 'nat', '-A', 'INPUT', '-p', 'tcp'])



# Generated at 2022-06-13 05:43:35.738157
# Unit test for function get_iptables_version
def test_get_iptables_version():
    try:
        assert get_iptables_version('/usr/bin/iptables', None) == '1.6.1'
    except AssertionError as e:
        raise AssertionError(e)


# Generated at 2022-06-13 05:43:45.264862
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import copy
