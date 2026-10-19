

# Generated at 2022-06-13 05:34:27.605267
# Unit test for function append_rule
def test_append_rule():
    pass


# Generated at 2022-06-13 05:34:36.381047
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule(dict(
        jump='DROP', ip_version='ipv4',
        reject_with='DROP', protocol='tcp',
        destination_port='80',
        comment='this is a test',
    )) == [
        '-j', 'DROP',
        '--reject-with', 'DROP',
        '-p', 'tcp',
        '--dport', '80',
        '-m', 'comment',
        '--comment', 'this is a test',
    ]



# Generated at 2022-06-13 05:34:49.812123
# Unit test for function construct_rule

# Generated at 2022-06-13 05:34:57.453029
# Unit test for function flush_table
def test_flush_table():
    class test_module():
        def run_command(self, cmd, check_rc=True):
            self.command = cmd
            self.rc = 0 if cmd == '/sbin/iptables -t filter -F INPUT' else 1
            return self.rc, '', ''
    test_mod = test_module()
    rc = flush_table('/sbin/iptables', test_mod, dict(table='filter', chain='INPUT'))
    assert test_mod.rc == rc
    rc = flush_table('/sbin/iptables', test_mod, dict(table='filter', chain='OUTPUT'))
    assert test_mod.rc == rc
    assert test_mod.command == '/sbin/iptables -t filter -F INPUT'
# Testing ends



# Generated at 2022-06-13 05:35:01.332201
# Unit test for function insert_rule
def test_insert_rule():
    assert insert_rule(iptables_path, module, params) == [iptables, '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT']


# Generated at 2022-06-13 05:35:05.569058
# Unit test for function main

# Generated at 2022-06-13 05:35:15.193000
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:17.174371
# Unit test for function construct_rule
def test_construct_rule():
    module = {}
    return construct_rule(module)



# Generated at 2022-06-13 05:35:23.928107
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    param = dict(flags=['ACK', 'RST', 'SYN', 'FIN'], flags_set=['ACK'])
    flag = '--tcp-flags'
    append_tcp_flags(rule, param, flag)
    print(rule)
    #['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK']


# Generated at 2022-06-13 05:35:27.883877
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = []
    param = {}
    param['flags'] = ['ACK','RST','SYN','FIN']
    param['flags_set'] = ['ACK','RST']
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK,RST']



# Generated at 2022-06-13 05:35:50.132214
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    append_match_flag(rule, "match", "--syn", True)
    assert rule == ['--syn']
    rule = []
    append_match_flag(rule, "negate", "--syn", True)
    assert rule == ['!', '--syn']
    rule = []
    append_match_flag(rule, "invalid", "--syn", True)
    assert rule == []
    rule = []
    append_match_flag(rule, "invalid", "--syn", False)
    assert rule == []



# Generated at 2022-06-13 05:36:00.265824
# Unit test for function get_iptables_version
def test_get_iptables_version():
    def test(ipt, opt):
        iptables_mock = MagicMock()
        iptables_mock.return_value = (0, opt, '')
        module_mock = MagicMock()
        module_mock.run_command.return_value = iptables_mock()
        assert get_iptables_version(ipt, module_mock) == ipt
    test('1.2.3', 'iptables v1.2.3')
    test('1.2.3', 'iptables v1.2.3\n')
    test('1.2.3', 'iptables v1.2.3\nmore stuff')
    test('1.2.3', 'v1.2.3\n')
    test('1.2.3', 'v1.2.3')



# Generated at 2022-06-13 05:36:03.058973
# Unit test for function check_present
def test_check_present():
    assert check_present(None, None, {}) == False



# Generated at 2022-06-13 05:36:06.814201
# Unit test for function flush_table
def test_flush_table():
    assert flush_table(None, None, None) is None



# Generated at 2022-06-13 05:36:16.248414
# Unit test for function push_arguments

# Generated at 2022-06-13 05:36:28.223416
# Unit test for function construct_rule
def test_construct_rule():
    # Test for simple rule for IPv4
    params = dict(
        protocol='tcp',
        source='10.0.0.1',
        destination='10.0.0.2',
        jump='REJECT',
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == [
        '-p', 'tcp', '-s', '10.0.0.1', '-d', '10.0.0.2', '-j', 'REJECT',
    ]
    # Test for simple rule for IPv6

# Generated at 2022-06-13 05:36:33.192310
# Unit test for function check_present
def test_check_present():
    path = '/sbin/iptables'
    i = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='',
        jump=None,
        comment=None,
    )
    assert check_present(path, dict(run_command=lambda x, **kw: (0, '', '')), i)



# Generated at 2022-06-13 05:36:41.828038
# Unit test for function main

# Generated at 2022-06-13 05:36:43.605980
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version("iptables", "--version") == "1.6.0"


# Generated at 2022-06-13 05:36:45.593657
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('iptables', 'iptables v1.6.1')  == '1.6.1'



# Generated at 2022-06-13 05:37:09.902370
# Unit test for function check_present
def test_check_present():
    import os
    import tempfile
    import shutil
    ipv4_bin = '/sbin/iptables'
    ipv6_bin = '/sbin/ip6tables'
    if os.path.exists('/usr/local/sbin/iptables'):
        ipv4_bin = '/usr/local/sbin/iptables'
    if os.path.exists('/usr/local/sbin/ip6tables'):
        ipv6_bin = '/usr/local/sbin/ip6tables'
    # Create a temp home for iptables-save and iptables-restore
    temp_dir = tempfile.mkdtemp()
    original_home = os.environ['HOME']
    os.environ['HOME'] = temp_dir

# Generated at 2022-06-13 05:37:14.266511
# Unit test for function set_chain_policy
def test_set_chain_policy():
    args = dict(
        iptables_path='iptables',
        module=object,
        params=dict(
            table='filter',
            chain='INPUT',
            policy='ACCEPT',
            wait=None
            )
        )
    return set_chain_policy(**args)


# Generated at 2022-06-13 05:37:20.491500
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:29.868062
# Unit test for function push_arguments
def test_push_arguments():
    module = AnsibleModule({})
    params={
        'chain':'INPUT',
        'table':'filter',
        'action':'-I',
        'rule_num':'3',
        'source_port':80
    }
    test_cmd = push_arguments('/sbin/iptables', '-I', params)
    assert test_cmd == ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '3', '-p', 'tcp', '--source-port', '80']



# Generated at 2022-06-13 05:37:31.383238
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:37:46.029523
# Unit test for function push_arguments
def test_push_arguments():
    args = dict(
        chain="INPUT",
        source="8.8.8.8",
        jump="DROP",
        protocol="tcp",
        uid_owner="!root",
        gid_owner="!root",
    )
    expected = [
        'iptables',
        '-t',
        'filter',
        '-A',
        'INPUT',
        '-s',
        '8.8.8.8',
        '-p',
        'tcp',
        '-m',
        'owner',
        '!',
        '--uid-owner',
        'root',
        '-m',
        'owner',
        '!',
        '--gid-owner',
        'root',
        '-j',
        'DROP']

# Generated at 2022-06-13 05:37:51.337323
# Unit test for function set_chain_policy
def test_set_chain_policy():
    params = {
        'chain': 'INPUT',
        'policy': 'DROP',
        'table': 'filter'
    }
    print(construct_rule(params))


# Generated at 2022-06-13 05:37:55.446988
# Unit test for function get_chain_policy
def test_get_chain_policy():
    module, _ = create_module()
    assert(get_chain_policy(*create_args(module)) == "ACCEPT")
    assert(get_chain_policy(*create_args(module, chain="LOGGING")) == "ACCEPT")


# Generated at 2022-06-13 05:38:08.392672
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('/sbin/iptables', '-I', {
        'chain': 'INPUT',
        'rule_num': '5',
        'table': 'filter',
        'protocol': 'tcp',
        'destination_port': '8080',
        'jump': 'ACCEPT',
        'ip_version': 'ipv4',
    }) == [
        '/sbin/iptables',
        '-t', 'filter',
        '-I', 'INPUT', '5',
        '-p', 'tcp',
        '--destination-port', '8080',
        '-j', 'ACCEPT']

# Generated at 2022-06-13 05:38:16.937293
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = 'iptables'
    module = AnsibleModule('')
    params = {'ip_version': 'ipv4', 'action': 'insert', 'table': 'mangle',
        'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '8080',
        'jump': 'ACCEPT', 'rule_num': '5'}
    cmd_result = insert_rule(iptables_path, module, params)
    print(cmd_result)
#test_insert_rule()


# Generated at 2022-06-13 05:38:32.836757
# Unit test for function push_arguments

# Generated at 2022-06-13 05:38:41.687393
# Unit test for function check_present
def test_check_present():
    module = None
    iptables_path = 'iptables'
    params = dict(
        ip_version = 'ipv4',
        chain = 'INPUT',
        source = '192.168.1.10',
        jump = 'DROP'
    )
    assert check_present(iptables_path, module, params) == False
    iptables_path = 'iptables'
    params = dict(
        ip_version = 'ipv4',
        chain = 'INPUT',
        source = '192.168.1.10',
        jump = 'ALLOW'
    )
    assert check_present(iptables_path, module, params) == True


# Generated at 2022-06-13 05:38:44.539518
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy() == -1


# Generated at 2022-06-13 05:38:48.687703
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    params = dict(
        ip_version='ipv4',
        table='filter',
        chain='INPUT',
    )
    policy_name = get_chain_policy('iptables', module, params)
    assert policy_name in ['ACCEPT', 'DROP']



# Generated at 2022-06-13 05:38:59.173367
# Unit test for function main

# Generated at 2022-06-13 05:39:08.189801
# Unit test for function push_arguments
def test_push_arguments():
    # The rule is the same for ipv4 and ipv6
    rule = dict(ip_version='ipv4')
    rule.update(dict(
        chain='test_chain',
        action='-I',
        table='mangle',
        limit='1/s',
        limit_burst='10',
        ))
    assert push_arguments('iptables', '-I', rule) == [
        'iptables',
        '-t', 'mangle',
        '-I', 'test_chain',
        '-m', 'limit',
        '--limit', '1/s',
        '--limit-burst', '10',
        ]
    rule.update(dict(
        rule_num=5,
        ))

# Generated at 2022-06-13 05:39:17.394338
# Unit test for function construct_rule
def test_construct_rule():
    rule = construct_rule(dict(
        destination='8.8.8.8',
        jump='DROP',
    ))
    assert rule == ['!', '-p', 'all', '-d', '8.8.8.8', '-j', 'DROP']

    rule = construct_rule(dict(
        source='8.8.8.8',
        jump='ACCEPT',
    ))
    assert rule == ['!', '-p', 'all', '-s', '8.8.8.8', '-j', 'ACCEPT']

    rule = construct_rule(dict(
        destination='8.8.8.8',
        protocol='tcp',
        jump='ACCEPT',
        destination_port='80',
    ))

# Generated at 2022-06-13 05:39:18.435367
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:39:26.906511
# Unit test for function check_present
def test_check_present():
    ipvversion = 'ipv4'
    iptables_path = '/usr/local/bin/iptables'
    module = AnsibleModule()
    params = {
        'action': 'present',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'destination_port': '22',
        'ctstate': 'NEW,ESTABLISHED',
        'syn': 'match',
        'jump': 'ACCEPT',
        'comment': 'Accept new SSH connections.',
        'ip_version': ipvversion,
        'table': 'filter',
    }
    cmd = push_arguments(iptables_path, '-C', params)
    rc, _, __ = module.run_command(cmd, check_rc=False)
    print(rc)


# Generated at 2022-06-13 05:39:33.820051
# Unit test for function get_chain_policy
def test_get_chain_policy():
  from mock import patch, Mock

  iptables_path = 'iptables'
  module = Mock()
  params = {
    'action': 'present',
    'chain': 'INPUT',
    'table': 'filter',
    'ip_version': 'ipv4'
  }
  chain_header = 'Chain INPUT (policy ACCEPT)'
  out = chain_header + "\n"
  rc = 0

  with patch('ansible.module_utils.basic.AnsibleModule.run_command') as mock_module:
    mock_module.return_value = (rc, out, '')
    assert get_chain_policy(iptables_path, module, params) == 'ACCEPT'

  chain_header = 'Chain INPUT (policy DROP)'
  out = chain_header + "\n"


# Generated at 2022-06-13 05:40:03.379812
# Unit test for function check_present
def test_check_present():
    assert check_present(BINS['ipv4'], None, {'table': 'filter', 'chain': 'INPUT'}) == True
    assert check_present(BINS['ipv4'], None, {'table': 'filter', 'chain': 'mychain'}) == False



# Generated at 2022-06-13 05:40:16.326027
# Unit test for function construct_rule
def test_construct_rule():
    """
    Unit test for function construct_rule
    """

# Generated at 2022-06-13 05:40:30.257686
# Unit test for function main

# Generated at 2022-06-13 05:40:32.964567
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/sbin/iptables'
    module = None
    params = {}
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    params['policy'] = 'DROP'
    set_chain_policy(iptables_path, module, params)



# Generated at 2022-06-13 05:40:33.727385
# Unit test for function append_rule
def test_append_rule():
    assert append_rule('/sbin/iptables', module, params) == None


# Generated at 2022-06-13 05:40:41.891522
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = "/sbin/iptables"
    module = AnsibleModule(argument_spec=dict())
    params = dict()
    params['ip_version'] = 'ipv4'
    params['table'] = 'filter'
    params['chain'] = 'INPUT'
    params['protocol'] = None
    params['source'] = None
    params['destination'] = None
    params['jump'] = None
    params['reject_with'] = None
    params['icmp_type'] = None
    params['action'] = 'remove'
    params['state'] = 'present'
    params['wait'] = None
    params['match_set'] = None
    params['match_set_flags'] = None
    cmd = push_arguments(iptables_path, '-D', params)
    rc,

# Generated at 2022-06-13 05:40:43.044080
# Unit test for function set_chain_policy
def test_set_chain_policy():
    return_value = set_chain_policy('/sbin/iptables', '/sbin/iptables', {"policy":"DROP"})
    return return_value



# Generated at 2022-06-13 05:40:48.454221
# Unit test for function push_arguments
def test_push_arguments():
    params = dict(
        chain='FORWARD',
        src_range='192.168.1.100-192.168.1.199',
        dst_range='10.0.0.1-10.0.0.50',
        jump='ACCEPT',
        table='filter',
        ip_version='ipv4',
        protocol='tcp'
    )
    cmd = push_arguments('iptables', '-A', params)
    assert '-t' in cmd
    assert '-m' in cmd
    assert 'iprange' in cmd
    assert '--src-range' in cmd
    assert '--dst-range' in cmd
    assert '-j' in cmd
    assert 'ACCEPT' in cmd



# Generated at 2022-06-13 05:40:54.663586
# Unit test for function flush_table
def test_flush_table():
    params=dict(
    table="filter",
    chain="INPUT",
    ip_version="ipv4",
    wait="2",
    log_prefix="[test_prefix]",
    log_level="debug",
    to_destination="10.20.30.40:50000",
    to_ports="8080",
    set_dscp_mark="0x2e",
    set_dscp_mark_class="EF",
    syn='match',
    comment="test_comment"
    )
    flush_table(BINS[params['ip_version']], module, params)


# Generated at 2022-06-13 05:40:55.735823
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, params) == True


# Generated at 2022-06-13 05:41:58.134922
# Unit test for function insert_rule
def test_insert_rule():
    rule = construct_rule(dict(
        protocol='tcp',
        destination_port=443,
        jump=None,
    ))
    assert len(rule) == 5
    assert rule == ['-p', 'tcp', '--dport', '443', '-j', 'DROP']
# End of unit test for function insert_rule



# Generated at 2022-06-13 05:41:59.452290
# Unit test for function flush_table
def test_flush_table():
    flush_table('/usr/bin/iptables', '', dict(table='nat', chain='OUTPUT')) == ['iptables', '-t', 'nat', '-F', 'OUTPUT']


# Generated at 2022-06-13 05:42:06.422352
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = 'iptables'
    action = '-P'
    params = {}
    params['table'] = 'nat'
    params['chain'] = 'INPUT'
    params['ip_version'] = 'ipv4'
    params['policy'] = 'ACCEPT'
    cmd = push_arguments(iptables_path, action, params, make_rule=False)
    cmd.append(params['policy'])
    print("cmd: ", cmd)
    #module.run_command(cmd, check_rc=True)
    
# unit test for function construct_rule

# Generated at 2022-06-13 05:42:20.174411
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('iptables', False, {'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': '80', 'jump': 'ACCEPT'}) == [
        'iptables', '-t', 'filter', '-D', 'INPUT', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    assert remove_rule('ip6tables', False, {'protocol': 'tcp', 'destination_port': '80', 'jump': 'ACCEPT'}) == [
        'ip6tables', '-t', 'filter', '-D', 'INPUT', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']

# Generated at 2022-06-13 05:42:29.153127
# Unit test for function construct_rule
def test_construct_rule():
    params = {}
    params['jump'] = 'ACCEPT'
    params['source'] = '1.1.1.1'
    params['destination'] = '2.2.2.2'
    params['ctstate'] = ['NEW']
    params['destination_port'] = '80'
    params['protocol'] = 'tcp'
    params['match'] = 'state'
    params['reject_with'] = 'icmp-port-unreachable'
    params['comment'] = 'This is a comment'
    params['set_dscp_mark'] = '0x10'
    params['limit'] = '10/minute'
    params['limit_burst'] = '20'
    params['syn'] = None
    params['ip_version'] = 'ipv4'
    params['match_set']

# Generated at 2022-06-13 05:42:34.154517
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments('iptables', '-I', dict(chain='INPUT', rule_num=3)) == [
        'iptables', '-t', 'filter', '-I', 'INPUT', '3']
    assert push_arguments('iptables', '-I', dict(chain='INPUT', rule_num=3), False) == [
        'iptables', '-t', 'filter', '-I', 'INPUT', '3']
    assert push_arguments('iptables', '-I', dict(chain='INPUT', rule_num=0), False) == [
        'iptables', '-t', 'filter', '-I', 'INPUT']



# Generated at 2022-06-13 05:42:36.817879
# Unit test for function insert_rule
def test_insert_rule():
    module = AnsibleModule(argument_spec=dict())
    params = dict(ip_version='ipv4',
                  table='filter',
                  chain='INPUT',
                  action='insert',
                  protocol='tcp',
                  destination_port='8080',
                  jump='ACCEPT',
                  rule_num='5')
    cmd = push_arguments('iptables', module, params)
    print(cmd)
test_insert_rule()

# Generated at 2022-06-13 05:42:45.783880
# Unit test for function check_present
def test_check_present():
    # TODO: Move BINS and ICMP_TYPE_OPTIONS to module_utils/basic.py
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.compat.version import LooseVersion

    ipset_bin = '/usr/sbin/ipset'
    iptables_path = BINS['ipv4']
    for iptables_version in ['1.4.20', '1.6.0']:
        if LooseVersion(iptables_version) < LooseVersion(IPTABLES_WAIT_SUPPORT_ADDED):
            wait_avail = False
        else:
            wait_avail = True

# Generated at 2022-06-13 05:42:48.384169
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = 'iptables'
    module = AnsibleModule()
    params = {
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'ACCEPT',
        'wait': None
    }
    cmd = ['iptables', '-P', 'INPUT', 'ACCEPT']
    assert set_chain_policy(iptables_path, module, params) == cmd



# Generated at 2022-06-13 05:42:57.398730
# Unit test for function construct_rule