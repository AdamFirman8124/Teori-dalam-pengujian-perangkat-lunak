

# Generated at 2022-06-13 05:34:29.659032
# Unit test for function set_chain_policy
def test_set_chain_policy():
    """ Unit test for function set_chain_policy """
    from collections import namedtuple

    ipv4_iptables_path = '/sbin/iptables'
    ipv6_iptables_path = None

    module = namedtuple('module', ('run_command'))
    module.run_command = lambda command, **kwargs: (0, '', '')

    action = 'present'
    table = 'filter'
    chain = 'INPUT'
    ip_version = 'ipv4'
    jump = None
    protocol = None
    match = None
    destination = None
    destination_port = None
    destination_ports = None
    source = None
    source_port = None
    state = None
    tcp_flags = None
    to_destination = None
    to_ports = None
    to_source

# Generated at 2022-06-13 05:34:39.903828
# Unit test for function construct_rule

# Generated at 2022-06-13 05:34:52.896784
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:02.799746
# Unit test for function construct_rule
def test_construct_rule():
    rule = []

# Generated at 2022-06-13 05:35:14.047236
# Unit test for function construct_rule
def test_construct_rule():
    return_list = construct_rule(dict(
        protocol='tcp', jump='ACCEPT', destination_port='22',
        ctstate='NEW', syn='match', destination_ports=['22', '80', '81:82']))
    assert return_list == ['-p', 'tcp', '--dport', '22', '-m', 'conntrack', '--ctstate', 'NEW', '--syn', '-m', 'multiport', '--dports', '22,80,81:82', '-j', 'ACCEPT']

# Generated at 2022-06-13 05:35:26.799268
# Unit test for function set_chain_policy

# Generated at 2022-06-13 05:35:32.539676
# Unit test for function check_present
def test_check_present():
    from ansible.modules.network.firewall import check_present
    import ansible.module_utils.network.firewall.iptables as a_m_u
    module = a_m_u
    iptables_path = 'iptables'

# Generated at 2022-06-13 05:35:38.940972
# Unit test for function push_arguments
def test_push_arguments():
    assert(push_arguments('/bin/iptables', '-I',
        dict(chain='INPUT',
             rule_num='5',
             protocol='tcp',
             destination_port='8080',
             jump='ACCEPT')) ==
           ['/bin/iptables', '-t', 'filter', '-I', 'INPUT', '5',
            '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT'])


# Generated at 2022-06-13 05:35:46.096581
# Unit test for function push_arguments
def test_push_arguments():
    iptables_path = '/sbin/iptables'
    action = '-I'
    params = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        rule_num='5',
    )
    cmd = push_arguments(iptables_path, action, params)
    assert cmd == ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']


# Generated at 2022-06-13 05:35:55.906489
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        source='1.1.1.1',
        destination='2.2.2.2',
        jump='ACCEPT',
        comment='test-rule',
        ip_version='ipv4',
    )
    expeccted_result = [
        '-p',
        'tcp',
        '-s',
        '1.1.1.1',
        '-d',
        '2.2.2.2',
        '-j',
        'ACCEPT',
        '-m',
        'comment',
        '--comment',
        'test-rule',
    ]
    assert construct_rule(params) == expeccted_result
# ----------------------------------



# Generated at 2022-06-13 05:36:18.340043
# Unit test for function main
def test_main():
    if os.environ.get('TEST_UNIT') is None or os.environ.get('TEST_UNIT') == 'false':
        exit()

    if os.environ.get('TEST_INTEGRATION') is None or os.environ.get('TEST_INTEGRATION') == 'false':
        exit()


# Generated at 2022-06-13 05:36:30.500326
# Unit test for function main
def test_main():
    return (
        {'table': 'filter',
         'chain': 'test',
         'ip_version': 'ipv4',
         'state': 'present',
         'action': 'append',
         'protocol': 'tcp',
         'destination': '192.168.0.1',
         'jump': 'ACCEPT'
        },
        {'changed': False,
         'failed': False,
         'ip_version': 'ipv4',
         'table': 'filter',
         'chain': 'test',
         'flush': False,
         'rule': '-t filter -A test -p tcp -d 192.168.0.1 -j ACCEPT',
         'state': 'present'
        }
    )

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:36:34.537566
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/sbin/iptables', None, {'chain': 'FOOBAR'}) is None
    assert get_chain_policy('/sbin/iptables', None, {'chain': 'INPUT'}) == 'ACCEPT'


# Generated at 2022-06-13 05:36:44.005097
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class FakeModule(object):
        def __init__(self, out=None, rc=0):
            self.out = out
            self.rc = rc

        def run_command(self, cmd, **kwargs):
            return self.rc, self.out, None

    fake_module = FakeModule(out="Chain INPUT (policy ACCEPT)")
    assert get_chain_policy('iptables', fake_module, {'chain': 'INPUT'}) == "ACCEPT"

    fake_module = FakeModule(out="Chain INPUT (policy DROP)")
    assert get_chain_policy('iptables', fake_module, {'chain': 'INPUT'}) == "DROP"

    fake_module = FakeModule(out="Chain INPUT (policy ACCEPT)")

# Generated at 2022-06-13 05:36:53.101510
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:00.171749
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:01.726794
# Unit test for function get_iptables_version
def test_get_iptables_version():
    return LooseVersion("1.6.0")
# End unit test for function get_iptables_version



# Generated at 2022-06-13 05:37:05.003460
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    param = None
    flag = '--foo'
    negatable = True
    append_match_flag(rule, param, flag, negatable)
    assert rule == []
    rule = []
    param = 'match'
    flag = '--foo'
    negatable = True
    append_match_flag(rule, param, flag, negatable)
    assert rule == ['--foo']
    rule = []
    param = 'negate'
    flag = '--foo'
    negatable = True
    append_match_flag(rule, param, flag, negatable)
    assert rule == ['!', '--foo']



# Generated at 2022-06-13 05:37:10.140926
# Unit test for function get_iptables_version
def test_get_iptables_version():
    # Asserts that we can extract the version from the string
    version = get_iptables_version('iptables', None)
    assert isinstance(version, str)
    assert len(version) > 0
    assert version.startswith('1.')



# Generated at 2022-06-13 05:37:19.231147
# Unit test for function main

# Generated at 2022-06-13 05:37:36.033247
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        protocol='tcp',
        source='8.8.8.8',
        jump='DROP',
    )) == ['-p', 'tcp', '-s', '8.8.8.8', '-j', 'DROP']
    assert construct_rule(dict(
        protocol='tcp',
        source='8.8.8.8',
        destination='8.8.4.4',
        destination_port='80',
        jump='DROP',
    )) == ['-p', 'tcp', '-s', '8.8.8.8', '-d', '8.8.4.4', '--dport', '80', '-j', 'DROP']

# Generated at 2022-06-13 05:37:41.441387
# Unit test for function construct_rule
def test_construct_rule():

    assert ['iptables', '-A', 'INPUT', '-p', 'tcp', '-m', 'comment',
            '--comment', 'Test', '-c', '0', '-j', 'ACCEPT'] == construct_rule(
                dict(chain='INPUT', protocol='tcp', comment='Test', jump='accept',
                     set_counters='0'))



# Generated at 2022-06-13 05:37:51.023005
# Unit test for function append_rule
def test_append_rule():
    iptables_path = "/usr/bin/iptables"
    module = AnsibleModule({
        "table": "filter",
        "chain": "INPUT",
        "destination_port": "22",
        "jump": "ACCEPT",
        "comment": "Accept new SSH connections.",
        "wait": "10"
    })
    params = module.params
    cmd = ["/usr/bin/iptables", "-t", "filter", "-A", "INPUT", "-w", "10", "-p", "tcp", "-d", "22", "-j", "ACCEPT", "--comment", "Accept new SSH connections."]
    test_cmd = push_arguments(iptables_path, '-A', params)
    assert cmd == test_cmd
# Test for function append_rule ended


# Generated at 2022-06-13 05:37:55.527343
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:38:00.763605
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('', '', {'chain': 'INPUT'}) == 'DROP'
    assert get_chain_policy('', '', {'chain': 'FORWARD'}) == 'DROP'
    assert get_chain_policy('', '', {'chain': 'OUTPUT'}) == 'ACCEPT'



# Generated at 2022-06-13 05:38:03.473228
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'policy': 'test'}) == 'test'



# Generated at 2022-06-13 05:38:13.235085
# Unit test for function main
def test_main():
    ip_version = 'ipv4'
    iptables_path = module.get_bin_path(BINS[ip_version], True)
    flush = True
    check_mode = False
    chain = 'INPUT'
    table = 'filter'
    args = dict(
        changed=False,
        failed=False,
        ip_version=ip_version,
        table=table,
        chain=chain,
        flush=flush,
        rule=' '.join(construct_rule(module.params)),
        state=module.params['state'],
    )
    check_chain_exists = False
    iptables_version = LooseVersion(get_iptables_version(iptables_path, module))

# Generated at 2022-06-13 05:38:17.584571
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module = MockModule(
        dict(
            chain='test',
            policy=None,
            bin='iptables',
            ip_version='ipv4',
            table='filter',
        )
    )
    iptables_path = module.params['bin']
    iptables_policy = get_chain_policy(iptables_path, module, module.params)
    assert iptables_policy == 'ACCEPT', 'Unit test for get_chain_policy failed'



# Generated at 2022-06-13 05:38:21.348050
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = ["q", "q"]
    param = {"flags": "ACK", "flags_set": "RST"}
    flag = '--tcp-flags'
    print(append_tcp_flags(rule, param, flag))



# Generated at 2022-06-13 05:38:28.402803
# Unit test for function construct_rule
def test_construct_rule():
    '''
    Test various combinations of options to construct_rule
    '''
    assert construct_rule({'wait': '1'}) == ['-w', '1']
    assert construct_rule({'protocol': 'tcp'}) == ['-p', 'tcp']
    assert construct_rule({'protocol': '!tcp'}) == ['!', '-p', 'tcp']
    assert construct_rule({'source': '8.8.8.8'}) == ['-s', '8.8.8.8']
    assert construct_rule({'source': '!8.8.8.8'}) == ['!', '-s', '8.8.8.8']

# Generated at 2022-06-13 05:38:53.481969
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    # Flag is the first parameter in the rule
    rule = []
    param = {}
    param['flags'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags_set'] = ['ACK', 'RST', 'SYN', 'FIN']
    flag = '--tcp-flags'
    append_tcp_flags(rule, param, flag)
    assert rule == [flag, ','.join(param['flags']), ','.join(param['flags_set'])]
    # Flag is not the first parameter in the rule
    rule = ['-d', '192.0.2.1']
    param = {}
    param['flags'] = ['ACK', 'RST', 'SYN', 'FIN']
    param['flags_set'] = ['ACK', 'RST', 'SYN', 'FIN']

# Generated at 2022-06-13 05:39:06.273429
# Unit test for function remove_rule
def test_remove_rule():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught in the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught in the test case"""
        pass

    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return data into an exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)


# Generated at 2022-06-13 05:39:12.926676
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(jump='ACCEPT')) == '-j ACCEPT'
    assert construct_rule(dict(
        chain='FORWARD',
        protocol='tcp',
        log_level='4',
        log_prefix='IPTABLES: ',
        jump='ACCEPT')
    ) == '-A FORWARD -p tcp --log-level 4 --log-prefix "IPTABLES: " -j ACCEPT'

# Generated at 2022-06-13 05:39:23.394816
# Unit test for function get_chain_policy
def test_get_chain_policy():
    params = dict(chain='test_chain_policy', policy='test_policy')
    iptables_path = 'iptables'
    module = dict(
        run_command=dict(
            return_value=(0, 'Chain TEST_CHAIN_POLICY (policy TEST_POLICY)', '')))
    assert get_chain_policy(iptables_path, module, params) == 'TEST_POLICY'
    module = dict(
        run_command=dict(
            return_value=(0, 'Chain TEST_CHAIN (policy ACCEPT)', '')))
    assert get_chain_policy(iptables_path, module, params) == 'ACCEPT'



# Generated at 2022-06-13 05:39:24.933682
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, {'chain':'INPUT'}) is None


# Generated at 2022-06-13 05:39:32.058043
# Unit test for function flush_table
def test_flush_table():
    iptables_path = "/sbin/iptables"
    module = AnsibleModule(argument_spec={
        'table': {'default': 'filter', 'type': 'str'},
        'chain': {'type': 'str'},
        'flush': {'type': 'bool', 'default': True},
        'wait': {'type': 'str'}, 
    })    
    params = {
        'table': 'nat',
        'chain': 'INPUT',
        'flush': True,
        'wait': '4',
    }
    assert flush_table(iptables_path, module, params) == None



# Generated at 2022-06-13 05:39:45.423359
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule({
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '80',
        'source': '8.8.8.8',
        'jump': 'ACCEPT',
    }) == ['-A', 'INPUT', '-s', '8.8.8.8', '-p', 'tcp',
           '--destination-port', '80', '-j', 'ACCEPT']


# Generated at 2022-06-13 05:39:51.809299
# Unit test for function construct_rule
def test_construct_rule():
    """
    Test construct rule based on params
    """

# Generated at 2022-06-13 05:40:01.606054
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        source='10.10.10.10',
        in_interface='eth0',
        jump='ACCEPT',
        set_counters='10:20',
        log_prefix='Test: ',
        comment='Test comment'
    )
    assert construct_rule(params) == ['-s', '10.10.10.10', '-i', 'eth0', '-j', 'ACCEPT', '-c', '10:20', '--comment', 'Test comment', '-p', 'tcp', '-w', '5']



# Generated at 2022-06-13 05:40:03.572103
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy(True, True, {"policy": "DROP"}) == None


# Generated at 2022-06-13 05:40:18.511730
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    unit_test_utils = UnitTestUtils(module)
    unit_test_utils.run_unit_tests(PATH, project_root)

# Generated at 2022-06-13 05:40:25.005340
# Unit test for function check_present
def test_check_present():
    params = dict(
        ip_version='ipv4',
        table='filter',
        action='insert',
        chain='INPUT',
        protocol='tcp',
        destination_port='80',
        jump='ACCEPT',
        comment=None,
        rule_num=None,
    )
    module = AnsibleModule(argument_spec=dict())
    iptables_path = 'iptables'
    rc = check_present(iptables_path, module, params)
    assert rc == False

# Generated at 2022-06-13 05:40:30.892034
# Unit test for function get_iptables_version
def test_get_iptables_version():
    a = dict(
        ipv4='iptables',
        ipv6='ip6tables'
    )
    for key, value in a.items():
        iptables_path = value
        for num in range(1, 11):
            b = dict(
                ipv4='iptables v' + str(num),
                ipv6='ip6tables v' + str(num)
            )
            module = dict(
                run_command=lambda x, y: (0, b[key], '')
            )
            assert get_iptables_version(iptables_path, module) == str(num)



# Generated at 2022-06-13 05:40:33.896808
# Unit test for function flush_table
def test_flush_table():
    module = AnsibleModule(
        argument_spec=dict(
            table=dict(default='filter'),
            chain=dict(default=None),
        ),
    )
    try:
        flush_table('/sbin/iptables', module, dict(table='filter', chain='INPUT'))
    except Exception as ex:
        module.fail_json(msg=ex)
    module.exit_json(changed=False)
# end unit test



# Generated at 2022-06-13 05:40:41.213505
# Unit test for function construct_rule
def test_construct_rule():
    p = dict(
        protocol='tcp',
        source='172.16.1.1',
        destination='172.16.1.2',
        match=['state'],
        ctstate=['RELATED', 'ESTABLISHED'],
        jump='ACCEPT',
        comment='allow established connections',
    )
    assert construct_rule(p) == [
        '-p', 'tcp',
        '-s', '172.16.1.1',
        '-d', '172.16.1.2',
        '-m', 'state',
        '--state', 'RELATED,ESTABLISHED',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', 'allow established connections',
    ]
    p['destination'] = '!' + p

# Generated at 2022-06-13 05:40:47.562683
# Unit test for function get_iptables_version
def test_get_iptables_version():
    iptables_path = '/usr/bin/iptables'
    out = 'v1.4.21\n'
    print(get_iptables_version(iptables_path, out))
    #return out.split('v')[1].rstrip('\n')


# Generated at 2022-06-13 05:40:53.269507
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    param = {'flags':['SYN','ACK','FIN','PSH'], 'flags_set': ['ACK','RST']}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'SYN,ACK,FIN,PSH', 'ACK,RST']



# Generated at 2022-06-13 05:41:00.580239
# Unit test for function push_arguments

# Generated at 2022-06-13 05:41:03.418632
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = list()
    param = {'flags': 'ALL', 'flags_set': ['ACK', 'RST', 'SYN', 'FIN']}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'ALL', 'ACK,RST,SYN,FIN']



# Generated at 2022-06-13 05:41:12.485645
# Unit test for function construct_rule
def test_construct_rule():
    rule = construct_rule({
        'protocol': 'tcp',
        'destination': '192.168.1.1',
        'destination_port': '80',
        'jump': 'ACCEPT',
        'comment': 'foo'
    })
    assert rule == ['-p', 'tcp', '-d', '192.168.1.1', '--dport', '80', '-j', 'ACCEPT',
                    '-m', 'comment', '--comment', 'foo']

    rule = construct_rule({
        'protocol': 'tcp',
        'destination': '192.168.1.1',
        'destination_port': '80',
        'jump': 'ACCEPT',
        'comment': 'foo',
        'ip_version': 'ipv6',
    })
   

# Generated at 2022-06-13 05:41:46.321816
# Unit test for function construct_rule
def test_construct_rule():
    result = construct_rule(dict(
        ip_version='ipv4',
        chain='INPUT',
        destination='80.80.80.80',
        jump='ACCEPT',
        comment='This rule is for testing purposes only'
    ))
    assert result == [
        '-d', '80.80.80.80',
        '-j', 'ACCEPT',
        '-m', 'comment',
        '--comment', 'This rule is for testing purposes only'
    ]
    result = construct_rule(dict(
        ip_version='ipv4',
        chain='INPUT',
        destination='80.80.80.80',
        destination_port='80',
        jump='ACCEPT',
        comment='This rule is for testing purposes only'
    ))

# Generated at 2022-06-13 05:41:53.257807
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:59.025123
# Unit test for function construct_rule
def test_construct_rule():
    # function testing
    ipv4_test_params = {
        'ip_version': 'ipv4',
        'protocol': 'tcp',
        'destination_port': '22',
        'ctstate': 'NEW',
        'syn': 'match',
        'jump': 'ACCEPT',
        'comment': 'Accept new SSH connections.'
    }
    rule = construct_rule(ipv4_test_params)
    assert rule == ['-w', '-p', 'tcp', '--destination-port', '22',
                    '-m', 'conntrack', '--ctstate', 'NEW', '--syn',
                    '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept new SSH connections.']


# Generated at 2022-06-13 05:42:07.872515
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = '/usr/bin/iptables'
    module = AnsibleModule(argument_spec=dict())
    params = {
        'ip_version': 'ipv4',
        'chain': 'INPUT',
        'action': 'insert',
        'table': 'filter',
        'rule_num': '3',
        'destination_port': '8080',
        'protocol': 'tcp',
        'jump': 'ACCEPT',
    }
    module.params = params
    cmd = push_arguments(iptables_path, '-I', params)
    print(cmd)
    rc, _, __ = module.run_command(cmd, check_rc=False)
    print(rc)
    print(_)
    print(__)

# Generated at 2022-06-13 05:42:18.112486
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        src_range='0.0.0.0-255.255.255.255',
        jump='ACCEPT',
        reject_with='icmp-net-unreachable',
        syn='match',
        syn='negate',
        icmp_type='echo-request',
        comment='Ansible managed',
    )

# Generated at 2022-06-13 05:42:21.424366
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('iptables', None, dict(chain='INPUT', table='filter')) == ['iptables', '-t', 'filter', '-D', 'INPUT']


# Generated at 2022-06-13 05:42:29.684260
# Unit test for function push_arguments
def test_push_arguments():
    params = {
        'ip_version': 'ipv4',
        'action': '-A',
        'chain': 'INPUT',
        'table': 'filter',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT',
    }
    result = push_arguments(BINS['ipv4'], params['action'], params)
    assert result == [
        'iptables',
        '-t', 'filter',
        '-A', 'INPUT',
        '-p', 'tcp',
        '--destination-port', '8080',
        '-j', 'ACCEPT',
    ]
    params['rule_num'] = 10

# Generated at 2022-06-13 05:42:33.787364
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('iptables', None, {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP',
    }) == "iptables -t filter -P INPUT DROP"
# End of unit test



# Generated at 2022-06-13 05:42:36.943350
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('iptables', {'run_command': return_something('v1.6.0', 0, 'nothing')}) == '1.6.0'
    assert get_iptables_version('iptables', {'run_command': return_something('V1.6.0', 0, 'nothing')}) == '1.6.0'
    assert get_iptables_version('iptables', {'run_command': return_something('1.6.0', 0, 'nothing')}) == '1.6.0'


# Generated at 2022-06-13 05:42:49.395501
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = "/usr/sbin/iptables"
    module = AnsibleModule

# Generated at 2022-06-13 05:43:05.082574
# Unit test for function construct_rule
def test_construct_rule():
    rule = construct_rule('', {
        'jump': 'ACCEPT',
        'comment': 'Test comment',
        'protocol': 'tcp',
        'destination_port': '80',
        'ctstate': 'NEW',
        'syn': 'match',
        'limit': '1/s',
        'limit_burst': '3',
        'uid_owner': 'nobody',
        'gid_owner': 'nobody',
        'reject_with': 'tcp-reset',
    })


# Generated at 2022-06-13 05:43:09.508143
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class TestModule(object):

        def __init__(self, out):
            self.params = dict(table='filter', chain='INPUT', policy='ACCEPT')
            self.run_command_counter = 0
            self.out = out

        def run_command(self, cmd, check_rc=True):
            self.run_command_counter += 1
            return 0, self.out, None

    # Test 1
    test = TestModule("Chain INPUT (policy ACCEPT)\n")
    out = get_chain_policy(None, test, test.params)
    assert out == "ACCEPT"
    assert test.run_command_counter == 1

    # Test 2
    test = TestModule("")
    out = get_chain_policy(None, test, test.params)
    assert out is None
    assert test

# Generated at 2022-06-13 05:43:20.115876
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:23.861772
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/bin/iptables', 'ipv4', 'INPUT') == 'ACCEPT'



# Generated at 2022-06-13 05:43:24.578232
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('iptables_path', 'module', 'params') == None



# Generated at 2022-06-13 05:43:33.395998
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='INPUT',
        protocol='tcp',
        source='1.1.1.1',
        destination='8.8.8.8',
        in_interface='eth0',
        out_interface='eth1',
        destination_port='80',
        destination_ports=['80', '443'],
        jump='ACCEPT',
        log_level='info',
        log_prefix='foobar',
        to_destination='127.0.0.1',
        goto='10',
        uid_owner='!root',
        ctstate='!ESTABLISHED,RELATED',
        icmp_type='0/0',
        reject_with='icmp-port-unreachable',
        comment='test',
        wait='5',
    )
    result = construct_

# Generated at 2022-06-13 05:43:41.826686
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:43.507140
# Unit test for function main
def test_main():
    pass

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:43:46.357971
# Unit test for function append_param
def test_append_param():
    rule = []
    append_param(rule, None, '--test-param', False)
    assert rule == []
    append_param(rule, 'TestParam', '--test-param', False)
    assert rule == ['--test-param', 'TestParam']
    rule = []
    append_param(rule, ['TestParam1', '!TestParam2'], '--test-param', True)
    assert rule == ['--test-param', 'TestParam1', '--test-param', '!TestParam2']



# Generated at 2022-06-13 05:43:56.822272
# Unit test for function main