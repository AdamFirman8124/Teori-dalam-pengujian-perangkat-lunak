

# Generated at 2022-06-13 05:34:38.801294
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        ip_version='ipv4',
        protocol='tcp',
        source='8.8.8.8',
        destination='192.168.1.1',
        destination_port='80',
        jump='DROP',
        reject_with='icmp-net-unreachable',
    )

    assert construct_rule(params) == [
        '-s', '8.8.8.8', '-d', '192.168.1.1', '-p', 'tcp',
        '--dport', '80', '-j', 'DROP', '--reject-with', 'icmp-net-unreachable',
    ]

# Generated at 2022-06-13 05:34:41.496111
# Unit test for function remove_rule
def test_remove_rule():
    params = {
        'chain': 'test_chain',
        'ip_version': 'test_ip_version'
    }
    assert remove_rule('test_iptables_path', 'test_module', params) == None



# Generated at 2022-06-13 05:34:53.401118
# Unit test for function construct_rule
def test_construct_rule():
    for ip_version in ('ipv4', 'ipv6'):
        params = dict()
        params['ip_version'] = ip_version
        params['protocol'] = 'tcp'
        params['source'] = '8.8.8.8'
        params['destination'] = '8.8.8.8'
        params['in_interface'] = 'eth0'
        params['out_interface'] = 'eth0'
        params['match'] = 'tcp'
        params['tcp_flags'] = dict(
            flags={'SYN', 'ACK', 'RST', 'FIN'},
            flags_set={'FIN', 'RST'})
        params['ctstate'] = ['ESTABLISHED', 'RELATED']
        params['destination_port'] = '8080'

# Generated at 2022-06-13 05:35:03.918211
# Unit test for function append_rule
def test_append_rule():
    print('test for function append_rule')
    print('default')
    p = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination='127.0.0.1',
        destination_port='8443',
        jump='ACCEPT'
    )
    append_rule(BINS['ipv4'], '', p)
    p = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination='127.0.0.1',
        destination_port='8443',
        jump='ACCEPT',
        ip_version='ipv4'
    )
    append_rule(BINS['ipv4'], '', p)

# Generated at 2022-06-13 05:35:14.791941
# Unit test for function construct_rule
def test_construct_rule():
    def assert_rule(expected, **kwargs):
        assert expected == construct_rule(dict(kwargs))
    assert_rule(['-p', 'tcp', '-s', '10.10.10.0/24', '-j', 'DROP'],
                protocol='tcp', source='10.10.10.0/24', jump='DROP')
    assert_rule(['-p', 'tcp', '-s', '10.10.10.0/24', '!',
                 '--destination-port', '80', '-j', 'DROP'],
                protocol='tcp', source='10.10.10.0/24', destination_port='!80',
                jump='DROP')

# Generated at 2022-06-13 05:35:27.100530
# Unit test for function construct_rule
def test_construct_rule():
    '''
    The following rule:
    iptables -I INPUT -p tcp -s 8.8.8.8 --dport 22 -j ACCEPT  -m comment --comment "SSH connect from 8.8.8.8" -w 60
    -A INPUT -i lo -j ACCEPT -m comment --comment "accept lo traffic"
    will be translated as:
    ['iptables', '-A', 'INPUT', '-i', 'lo', '-j', 'ACCEPT',
      '-m', 'comment', '--comment', 'accept lo traffic']
    '''

# Generated at 2022-06-13 05:35:32.103895
# Unit test for function set_chain_policy
def test_set_chain_policy():
    assert set_chain_policy('', {}, {'table': 'filter', 'chain':'INPUT', 'policy':'DROP'}) == [
        'iptables', '-t', 'filter', '-P', 'INPUT', 'DROP']



# Generated at 2022-06-13 05:35:40.804808
# Unit test for function push_arguments
def test_push_arguments():
    parameters = dict(
        chain='test-chain',
        protocol='tcp',
        source='1.1.1.1',
        destination='2.2.2.2',
        jump='ACCEPT',
        table='test-table',
        ip_version="ipv4",
        )
    assert push_arguments("iptables", "-I", parameters, False) == [
        'iptables', '-t', 'test-table', '-I', 'test-chain',
       ]

# Generated at 2022-06-13 05:35:50.030691
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:54.579898
# Unit test for function append_rule
def test_append_rule():
    module = AnsibleModule(argument_spec={})
    iptables_path = 'iptables'

# Generated at 2022-06-13 05:36:07.687901
# Unit test for function insert_rule
def test_insert_rule():
    print(insert_rule('iptables',None,{'table': 'filter', 'chain': 'INPUT', 'protocol': 'tcp', 'destination_port': 8080, 'jump': 'ACCEPT', 'action': 'insert', 'rule_num': 5}))


# Generated at 2022-06-13 05:36:17.894881
# Unit test for function push_arguments
def test_push_arguments():
    try:
        import json
    except ImportError:
        import simplejson as json

    # Test with make_rule True
    params = {
        'chain': 'INPUT',
        'source': '192.0.2.0/24',
        'protocol': 'tcp',
        'destination_port': 22,
        'jump': 'ACCEPT',
        'ip_version': 'ipv4',
        'make_rule': True,
    }
    result = push_arguments('/sbin/iptables', '-A', params, True)

# Generated at 2022-06-13 05:36:19.122325
# Unit test for function insert_rule
def test_insert_rule():
  print(insert_rule(iptables_path='iptables', module=module, params=params))
test_insert_rule()


# Generated at 2022-06-13 05:36:25.144509
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
  test_param = {'flags':['ACK', 'RST', 'SYN', 'FIN'], 'flags_set':['ACK']}
  test_flag = '--tcp-flags'
  test_rule = []
  append_tcp_flags(test_rule,test_param,test_flag)
  assert test_rule == ['--tcp-flags', 'ACK,RST,SYN,FIN', 'ACK']


# Generated at 2022-06-13 05:36:26.781702
# Unit test for function append_rule
def test_append_rule():
    assert append_rule(None, None, None) is None



# Generated at 2022-06-13 05:36:34.025468
# Unit test for function remove_rule
def test_remove_rule():
    params = dict(
        table="filter",
        chain="INPUT",
        protocol="tcp",
        destination="localhost",
        jump="ACCEPT",
    )
    # The following will fail on travis
    # module.run_command(cmd, check_rc=True)
    cmd = push_arguments("iptables", '-D', params)
    assert (cmd == ['iptables', '-t', 'filter', '-D', 'INPUT', '-p', 'tcp', '-d', 'localhost', '-j', 'ACCEPT'])
    assert (remove_rule("iptables", "module", params) == None)


# Generated at 2022-06-13 05:36:40.147692
# Unit test for function push_arguments

# Generated at 2022-06-13 05:36:43.075449
# Unit test for function append_match_flag
def test_append_match_flag():
    assert append_match_flag(rule, 'match', '--syn', True) == ['--syn']
    assert append_match_flag(rule, 'negate', '--syn', True) == ['!', '--syn']



# Generated at 2022-06-13 05:36:47.600500
# Unit test for function flush_table
def test_flush_table():
    iptables_path = '/sbin/iptables'
    table='filter'
    chain=''
    params = dict(ip_version='ipv4', table=table, chain=chain, flush=True, policy='ACCEPT',
                   verbose=False, fail_dst=False)
    flush_table(iptables_path, module, params)


# Generated at 2022-06-13 05:36:56.127424
# Unit test for function construct_rule

# Generated at 2022-06-13 05:37:16.067142
# Unit test for function main

# Generated at 2022-06-13 05:37:22.606278
# Unit test for function append_match_flag
def test_append_match_flag():
    rule = []
    param = 'match'
    flag = '--syn'
    negatable = True
    test_rule = ['--syn']
    append_match_flag(rule, param, flag, negatable)
    assert rule == test_rule
    rule = []
    param = 'negate'
    test_rule = ['!', '--syn']
    append_match_flag(rule, param, flag, negatable)
    assert rule == test_rule
    rule = []
    param = None
    test_rule = []
    append_match_flag(rule, param, flag, negatable)
    assert rule == test_rule


# Generated at 2022-06-13 05:37:30.366035
# Unit test for function remove_rule
def test_remove_rule():
  module_ = AnsibleModule(argument_spec = dict(
    test = dict(type = 'bool', require = True),
    chain = dict(type = 'str', require = True),
    ip_version = dict(type = 'str', require = True)
  ))
  module_.params['test'] = True
  module_.params['chain'] = 'INPUT'
  module_.params['ip_version'] = 'ipv4'
  remove_rule('/usr/sbin/iptables', module_, module_.params)



# Generated at 2022-06-13 05:37:42.464379
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule('/sbin/iptables','/',{'table':'filter','chain':'INPUT','protocol':'tcp','destination_port':'22','ctstate':'NEW','syn':'match','jump':'ACCEPT','comment':'Accept new SSH connections.','rule_num':'5'}) == ['/sbin/iptables', '-t', 'filter', '-D', 'INPUT', '5', '-p', 'tcp', '--dport', '22', '-m', 'conntrack', '--ctstate', 'NEW', '--syn', '-j', 'ACCEPT', '-m', 'comment', '--comment', 'Accept new SSH connections.']


# Generated at 2022-06-13 05:37:51.181759
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:01.153845
# Unit test for function main

# Generated at 2022-06-13 05:38:07.892990
# Unit test for function append_match_flag
def test_append_match_flag():
    assert append_match_flag(['list'], 'match', 'test', False) == ['list', 'test']
    assert append_match_flag(['list'], 'negate', 'test', True) == ['list', '!', 'test']
    assert append_match_flag(['list'], 'non_match', 'test', True) == ['list']
    assert append_match_flag(['list'], 'non_match', 'test', False) == ['list']



# Generated at 2022-06-13 05:38:16.409940
# Unit test for function main

# Generated at 2022-06-13 05:38:19.351202
# Unit test for function append_rule
def test_append_rule():
    iptables_path = 'iptables'
    module = AnsibleModule()
    ips = {'protocol': 'tcp', 'destination_port': '22'}
    params = dict(
        chain='INPUT',
        protocol='tcp',
        destination_port='22',
        jump='ACCEPT')
    params.update(ips)
    cmd = push_arguments(iptables_path, '-A', params)
    module.run_command(cmd, check_rc=True)
    return True



# Generated at 2022-06-13 05:38:23.522439
# Unit test for function construct_rule

# Generated at 2022-06-13 05:38:41.465925
# Unit test for function append_rule
def test_append_rule():
    test_params = [
        '-A INPUT -p tcp -m conntrack --ctstate NEW -m tcp --dport 80 -j ACCEPT',
        '-A INPUT --protocol tcp --ctstate NEW --destination-port 80 --jump ACCEPT',
        '--append INPUT --protocol tcp --ctstate NEW --destination-port 80 --jump ACCEPT'
    ]
    for test_param in test_params:
        assert (append_rule('iptables', test_param) == test_param.split())



# Generated at 2022-06-13 05:38:46.824936
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'chain': 'INPUT', 'table': 'filter'}) == 'ACCEPT'
    assert get_chain_policy(None, None, {'chain': 'INPUT', 'table': 'nat'}) == None



# Generated at 2022-06-13 05:38:58.356907
# Unit test for function construct_rule
def test_construct_rule():
    """
    This is a unit test to test the rule construction logic.
    """
    import json


# Generated at 2022-06-13 05:39:05.272650
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {
        "chain": "INPUT",
    }) == "ACCEPT"
    assert get_chain_policy(None, None, {
        "chain": "FORWARD",
    }) == "ACCEPT"
    assert get_chain_policy(None, None, {
        "chain": "OUTPUT",
    }) == "ACCEPT"
    assert get_chain_policy(None, None, {
        "chain": "test_fail",
    }) is None



# Generated at 2022-06-13 05:39:07.894846
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, chain="INPUT",table="filter",jump="ACCEPT") == False


# Generated at 2022-06-13 05:39:12.672828
# Unit test for function check_present
def test_check_present():
    assert check_present('/sbin/iptables', module, {'table':'filter', 'chain': 'INPUT', 'source': '8.8.8.8'})
    assert not check_present('/sbin/iptables', module, {'table':'filter', 'chain': 'INPUT', 'source': '1.1.1.1'})



# Generated at 2022-06-13 05:39:17.336432
# Unit test for function main
def test_main():
    args = dict(state='present', table='filter', chain='INPUT', jump='ACCEPT', protocol='tcp', destination_port='80', ip_version='ipv4')

# Generated at 2022-06-13 05:39:25.742428
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(chain='INPUT')) is None
    assert get_chain_policy(None, None, dict(chain='INPUT', stdout='foo', stdout_lines=['--ignore','(policy DROP)','foo'], rc=0)) == 'DROP'
    assert get_chain_policy(None, None, dict(chain='INPUT', stdout='foo', stdout_lines=['--ignore','(policy --negate)','foo'], rc=0)) == '--negate'
    assert get_chain_policy(None, None, dict(chain='INPUT', stdout='foo', stdout_lines=['--ignore','policy DROP)','foo'], rc=0)) is None



# Generated at 2022-06-13 05:39:28.009973
# Unit test for function flush_table
def test_flush_table():
    params = {'table': 'test',
              'chain': 'test'}
    flush_table('ix', None, params)

# Generated at 2022-06-13 05:39:35.802179
# Unit test for function insert_rule
def test_insert_rule():
    params = dict(
        chain='TEST',
        table='filter',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        rule_num='5',
    )
    assert insert_rule(module, params) == ['/sbin/iptables', '-t', 'filter', '-I', 'TEST', '5', '-p', 'tcp', '--dport', '8080', '-j', 'ACCEPT', '-w']



# Generated at 2022-06-13 05:39:53.819835
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        chain='OUTPUT',
        protocol='tcp',
        destination_port='22',
        ctstate='NEW',
        syn='match',
        jump='ACCEPT',
        comment='Accept new SSH connections.',
        ip_version='ipv4'
    )
    expected = [
        '-p', 'tcp', '--dport', '22', '-m', 'conntrack', '--ctstate',
        'NEW', '--syn', '-j', 'ACCEPT', '-m', 'comment', '--comment',
        'Accept new SSH connections.'
    ]
    assert construct_rule(params) == expected


# Generated at 2022-06-13 05:40:01.686820
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('dummy', None, {'chain': 'INPUT', 'table': 'filter'}) == "ACCEPT"
    assert get_chain_policy('dummy', None, {'chain': 'INPUT', 'table': 'nat'}) == "ACCEPT"
    assert get_chain_policy('dummy', None, {'chain': 'INPUT', 'table': 'mangle'}) == "ACCEPT"
    assert get_chain_policy('dummy', None, {'chain': 'FORWARD', 'table': 'filter'}) == "ACCEPT"
    assert get_chain_policy('dummy', None, {'chain': 'FORWARD', 'table': 'nat'}) == None

# Generated at 2022-06-13 05:40:10.019015
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule
    m.run_command = MagicMock(return_value=(0,'',''))
    rule = dict()
    rule['table'] = 'filter'
    rule['chain'] = 'INPUT'
    rule['source'] = '192.168.1.100'
    rule['protocol'] = 'icmp'
    rule['jump'] = 'ACCEPT'
    rule['ip_version'] = 'ipv4'
    assert check_present('iptables', module, rule) == True


# Generated at 2022-06-13 05:40:19.912609
# Unit test for function main
def test_main():
    print("Starting test_main")
    iptables_path = '/sbin/iptables-restore'

# Generated at 2022-06-13 05:40:28.923629
# Unit test for function check_present
def test_check_present():
    test_dict = dict(
        iptables_path='iptables',
        module=Mock(),
        params=dict(
            table='filter',
            chain='INPUT',
            comment='comment',
        ),
    )
    test_dict['module'].run_command.return_value = 0, '', ''
    assert check_present(**test_dict)
    assert test_dict['module'].run_command.call_args[0][0] == \
        [test_dict['iptables_path'], '-t', test_dict['params']['table'], '-C',
        test_dict['params']['chain'], '-m', 'comment', '--comment',
        test_dict['params']['comment']]



# Generated at 2022-06-13 05:40:35.490330
# Unit test for function construct_rule

# Generated at 2022-06-13 05:40:36.744577
# Unit test for function get_chain_policy
def test_get_chain_policy():
    get_chain_policy('iptables', None, dict(chain='INPUT', table='filter'))



# Generated at 2022-06-13 05:40:48.628588
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert '1.4.20' == get_iptables_version('iptables', '1.4.20')
    assert '1.4.20' == get_iptables_version('iptables', 'iptables v1.4.20')
    assert '1.6.0' == get_iptables_version('iptables', 'iptables v1.6.0')
    assert '1.6.0' == get_iptables_version('iptables', 'iptables v1.6.0 (nf_tables)')
    assert '1.4.20' == get_iptables_version('ip6tables', '1.4.20')
    assert '1.4.20' == get_iptables_version('ip6tables', 'ip6tables v1.4.20')

# Generated at 2022-06-13 05:40:51.955410
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert 'ACCEPT' == get_chain_policy(None, None, dict(table='filter', chain='INPUT'))
    assert 'DROP' == get_chain_policy(None, None, dict(table='filter', chain='OUTPUT'))
    assert 'ACCEPT' == get_chain_policy(None, None, dict(table='filter', chain='FORWARD'))
    assert None == get_chain_policy(None, None, dict(table='filter', chain='TEST'))



# Generated at 2022-06-13 05:40:59.814273
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import load_platform_subclass
    from ansible.module_utils.six import PY3

    if not PY3:
        try:
            from ansible.module_utils.ansible_release import __version__ as ansible_version
        except ImportError:
            ansible_version = '2.7.0'

        if LooseVersion(ansible_version) >= LooseVersion('2.8.0'):
            pytestmark = pytest.mark.skip("Current python version is unable to run this test case.")
    else:
        pytestmark = pytest.mark.skip("Current python version is unable to run this test case.")

    # Load the platform subclass module

# Generated at 2022-06-13 05:41:36.268613
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:46.359586
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:50.733321
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        destination='www.example.com',
        match='comment',
        comment='accept web traffic',
        ip_version='ipv4',
    )
    rule = construct_rule(params)
    assert rule == [
        '-p', params['protocol'],
        '-d', params['destination'],
        '-m', params['match'],
        '--comment', params['comment'],
    ]



# Generated at 2022-06-13 05:41:51.915326
# Unit test for function check_present
def test_check_present():
    assert check_present(iptables_path, module, params)


# Generated at 2022-06-13 05:41:57.885834
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:04.049951
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = "/sbin/iptables"
    action = "-I"
    chain = "INPUT"
    rule_num = "2"
    rule = ['-p', 'tcp', '-s', '8.8.8.8', '-j', 'DROP']
    # cmd = push_arguments(iptables_path, action, chain, rule_num, rule)
    # return cmd

    return rule


# Generated at 2022-06-13 05:42:07.336117
# Unit test for function get_chain_policy
def test_get_chain_policy():
  assert get_chain_policy('dummy', 'dummy', {
    'table': 'filter',
    'chain': 'FORWARD'
  }) == 'ACCEPT'


# Generated at 2022-06-13 05:42:14.725176
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule
    params = dict(
        table='filter',
        chain='INPUT',
        rule_num='1',
        protocol="tcp",
        destination_port="80",
        jump="ACCEPT",
        comment="accept new SSH connections"
    )
    cmd = push_arguments(iptables_path, '-I', params)
    print(cmd)
    module.run_command(cmd, check_rc=True)



# Generated at 2022-06-13 05:42:27.466232
# Unit test for function remove_rule
def test_remove_rule():
    module = AnsibleModule(argument_spec={})
    iptables_path = BINS['ipv4']

# Generated at 2022-06-13 05:42:38.046787
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:15.314564
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule({'iptables_path':iptables_path,
                            'table':'filter',
                            'chain':'INPUT',
                             'protocol':'tcp',
                             'destination_port':'22',
                             'ctstate':'NEW',
                            'syn':'match',
                            'jump':'ACCEPT',
                            'comment':'Accept new SSH connections.'}, check_invalid_arguments=False)

# Generated at 2022-06-13 05:43:22.730681
# Unit test for function construct_rule
def test_construct_rule():
    '''
    Unit test for function _construct_rule
    '''

# Generated at 2022-06-13 05:43:24.847516
# Unit test for function get_iptables_version
def test_get_iptables_version():
    assert get_iptables_version('/sbin/iptables', None) == '1.6.2'



# Generated at 2022-06-13 05:43:33.522616
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:41.681171
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', {}, {'chain': 'INPUT', 'policy': 'ACCEPT', 'table': 'filter'}) == 'INPUT'
    assert get_chain_policy('iptables', {}, {'chain': 'OUTPUT', 'policy': 'ACCEPT', 'table': 'filter'}) == 'OUTPUT'
    assert get_chain_policy('iptables', {}, {'chain': 'FORWARD', 'policy': 'ACCEPT', 'table': 'filter'}) == 'FORWARD'
    assert get_chain_policy('iptables', {}, {'chain': 'POSTROUTING', 'policy': 'ACCEPT', 'table': 'nat'}) == 'POSTROUTING'

# Generated at 2022-06-13 05:43:50.608752
# Unit test for function main

# Generated at 2022-06-13 05:44:03.093152
# Unit test for function construct_rule
def test_construct_rule():
    # Without conntrack match
    assert(construct_rule(dict(
        rule_num=None,
        protocol='tcp',
        source=None,
        destination_port=None,
        jump='DROP',
        comment='some-drop',
        ctstate=None,
        ip_version='ipv4',
    )) == ['iptables', '-p', 'tcp', '-j', 'DROP', '-m', 'comment', '--comment', 'some-drop'])

    # Without conntrack match