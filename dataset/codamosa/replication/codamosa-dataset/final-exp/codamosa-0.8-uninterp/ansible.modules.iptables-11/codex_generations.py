

# Generated at 2022-06-13 05:34:42.780374
# Unit test for function get_chain_policy
def test_get_chain_policy():
    class module_mock:
        def __init__(self):
            self.params = dict()

        def run_command(self, cmd, check_rc=True):
            if cmd == ['/sbin/iptables', '-L', '-t', 'filter', 'INPUT']:
                return 0, "Chain INPUT (policy ACCEPT) ", ''
            else:
                raise Exception('Unexpected command: %s' % ' '.join(cmd))

    class get_chain_policy_test(unittest.TestCase):
        def test_get_chain_policy(self):
            module = module_mock()
            iptables_path = '/sbin/iptables'
            params = dict(
                chain='INPUT',
                table='filter',
                policy='ACCEPT',
            )
            result = get

# Generated at 2022-06-13 05:34:53.983084
# Unit test for function append_match_flag
def test_append_match_flag():
    test_rule = []
    assert test_rule == []
    append_match_flag(test_rule, 'match', '--syn', True)
    assert test_rule == ['--syn']
    append_match_flag(test_rule, 'negate', '--syn', True)
    assert test_rule == ['--syn', '!', '--syn']
    append_match_flag(test_rule, 'match', '--fin', False)
    assert test_rule == ['--syn', '!', '--syn', '--fin']
    append_match_flag(test_rule, 'negate', '--fin', False)
    assert test_rule == ['--syn', '!', '--syn', '--fin']



# Generated at 2022-06-13 05:35:00.120990
# Unit test for function main

# Generated at 2022-06-13 05:35:11.983357
# Unit test for function append_rule
def test_append_rule():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from tempfile import mkdtemp
    from shutil import rmtree
    from contextlib import contextmanager
    from os.path import join

    @contextmanager
    def temp_dir():
        dir_path = mkdtemp()

        yield dir_path

        rmtree(dir_path)

    def write_file(path, content):
        with open(path, 'wb') as file:
            file.write(to_bytes(content))

    def read_file(path):
        with open(path, 'rb') as file:
            return file.read()

    def create_module(tmp_path, params):
        write_

# Generated at 2022-06-13 05:35:25.781125
# Unit test for function main
def test_main():
    iptables_version = '1.4.20'
    ip_version = 'ipv4'
    iptables_path = '/sbin/iptables'

# Generated at 2022-06-13 05:35:38.287219
# Unit test for function push_arguments

# Generated at 2022-06-13 05:35:39.291201
# Unit test for function append_rule
def test_append_rule():
    assert append_rule('iptables', module, params) == True


# Generated at 2022-06-13 05:35:45.384087
# Unit test for function append_match_flag
def test_append_match_flag():
    assert ['!', 'bar'] == append_match_flag(['foo'], 'negate', 'bar', True)
    assert ['foo'] == append_match_flag(['foo'], None, 'bar', True)
    assert ['bar'] == append_match_flag(['foo'], 'match', 'bar', False)



# Generated at 2022-06-13 05:35:49.298347
# Unit test for function push_arguments
def test_push_arguments():
    assert push_arguments("iptables", '-I', {'table': 'filter', 'chain': 'INPUT', 'rule_num': 4}) == ['iptables', '-t', 'filter', '-I', 'INPUT', '4']
assert test_push_arguments()


# Generated at 2022-06-13 05:35:53.980751
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('', None, {'chain':'>toto'}) == None
    assert get_chain_policy('', None, {'chain':'toto'}) == None
    assert get_chain_policy('', None, {'chain':'toto\n(policy DROP)'}) == 'DROP'


# Generated at 2022-06-13 05:36:15.427759
# Unit test for function get_iptables_version
def test_get_iptables_version():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({'binary': '/sbin/iptables'})

    if module.get_bin_path('iptables'):
        iptables_path = module.get_bin_path('iptables')
    elif module.get_bin_path('iptables-legacy'):
        iptables_path = module.get_bin_path('iptables-legacy')
    else:
        module.fail_json(msg="iptables binary not found.")
    assert get_iptables_version(iptables_path, module) == '1.8.0'



# Generated at 2022-06-13 05:36:26.904956
# Unit test for function construct_rule
def test_construct_rule():
    '''Function construct_rule test'''

# Generated at 2022-06-13 05:36:30.445824
# Unit test for function set_chain_policy
def test_set_chain_policy():
    import sys
    import mock
    MODULE_ARGS = {
        'chain': 'INPUT',
        'policy': 'DROP',
        'bin': None,
        'table': 'filter',
        'wait': None,
    }
    module_mock = mock.Mock()
    def run_command(cmd, check_rc=None):
        print(cmd)
        return 0, 'output', 'error'
    module_mock.run_command = run_command
    set_chain_policy('iptables', module_mock, MODULE_ARGS)
    sys.modules['ansible'].module_utils.netcommon = None



# Generated at 2022-06-13 05:36:37.816473
# Unit test for function construct_rule

# Generated at 2022-06-13 05:36:46.015912
# Unit test for function append_tcp_flags
def test_append_tcp_flags():
    rule = ['iptables']
    append_tcp_flags(rule, dict(flags=['ACK', 'RST'], flags_set=['SYN', 'FIN']), '--tcp-flags')
    assert(rule == ['iptables', '--tcp-flags', 'ACK,RST', 'SYN,FIN'])
    append_tcp_flags(rule, dict(flags=['ACK', 'RST', 'SYN'], flags_set=['ACK', 'FIN']), '--tcp-flags')
    assert(rule == ['iptables', '--tcp-flags', 'ACK,RST', 'SYN,FIN'])

# Generated at 2022-06-13 05:36:48.696725
# Unit test for function append_rule
def test_append_rule():
    module = AnsibleModule()
    params = {'chain': 'INPUT', 'table': 'filter', 'jump': 'ACCEPT'}
    append_rule('/sbin/iptables', module, params)



# Generated at 2022-06-13 05:36:57.026898
# Unit test for function construct_rule
def test_construct_rule():
    def assert_rule(**kwargs):
        rule = construct_rule(kwargs)
        assert isinstance(rule, list)

    assert_rule(protocol='udp', source='192.0.2.1', jump='ACCEPT')
    assert_rule(protocol='udp', source='192.0.2.1', comment='test')
    assert_rule(protocol='udp', source='192.0.2.1', match='comment')
    assert_rule(protocol='udp', source='192.0.2.1', wait='1')
    assert_rule(protocol='udp', source='192.0.2.1', dst_range='10.0.0.1-10.0.0.50')

# Generated at 2022-06-13 05:37:02.393313
# Unit test for function get_chain_policy
def test_get_chain_policy():
    result = get_chain_policy('/etc/iptables', dict(run_command=lambda *args, **kwargs: (0, 'Chain INPUT (policy ACCEPT)', '')), dict(chain='INPUT', policy='ACCEPT'))
    assert result == 'ACCEPT', 'The chain policy of INPUT chain should be ACCEPT but is %s.' % result
    result = get_chain_policy('/etc/iptables', dict(run_command=lambda *args, **kwargs: (0, 'Chain INPUT (policy DROP)', '')), dict(chain='INPUT', policy='DROP'))
    assert result == 'DROP', 'The chain policy of INPUT chain should be DROP but is %s.' % result



# Generated at 2022-06-13 05:37:03.519686
# Unit test for function remove_rule
def test_remove_rule():
    assert remove_rule("iptables","module","params") == (-1, 'stdout', 'stderr')



# Generated at 2022-06-13 05:37:14.614339
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec={'command': dict(type='list')})
    module.run_command = MagicMock(return_value=(0, '', ''))
    cmd = ['iptables', '-t', 'mangle', '-C', 'FORWARD', '-s', '172.16.1.1', '!', '-d', '172.16.1.1', '-p', 'tcp', '-m', 'conntrack', '--ctstate', 'RELATED', '-m', 'limit', '--limit', '1/second', '-j', 'DROP']

# Generated at 2022-06-13 05:37:34.288316
# Unit test for function main
def test_main():
    ''' Unit test for function main '''

# Generated at 2022-06-13 05:37:41.385515
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, dict(table='filter', chain="INPUT")) == 'DROP'
    assert get_chain_policy(None, None, dict(table='filter', chain="OUTPUT")) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(table='filter', chain="FORWARD")) == 'ACCEPT'
    assert get_chain_policy(None, None, dict(table='filter', chain="CUSTOM_CHAIN")) == None



# Generated at 2022-06-13 05:37:42.290465
# Unit test for function check_present
def test_check_present():
    assert check_present('iptables', module, params) == (rc == 0)



# Generated at 2022-06-13 05:37:45.108237
# Unit test for function check_present
def test_check_present():
    assert check_present(None, None, {'chain': 'INPUT', 'ip_version': 'ipv4'}) == (0 == 0)


# Generated at 2022-06-13 05:37:55.416835
# Unit test for function construct_rule
def test_construct_rule():
    params = dict(
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        ip_version='ipv4',
    )
    test_rule_ipv4 = '-p tcp --destination-port 8080 -j ACCEPT'
    assert ' '.join(construct_rule(params)) == test_rule_ipv4
    params['ip_version'] = 'ipv6'
    test_rule_ipv6 = '-p tcp --destination-port 8080 -j ACCEPT'
    assert ' '.join(construct_rule(params)) == test_rule_ipv6

# Generated at 2022-06-13 05:38:08.361073
# Unit test for function construct_rule
def test_construct_rule():
    module = AnsibleModule({
        'chain': 'INPUT',
        'jump': 'DROP',
        'exists': 'false',
    })
    result = construct_rule(module.params)
    assert result == ['-j', 'DROP'], "construct_rule should be ['-j', 'DROP']"

    module = AnsibleModule({
        'chain': 'INPUT',
        'jump': 'DROP',
        'exists': 'true',
        'reject_with': 'tcp-reset',
    })
    result = construct_rule(module.params)

# Generated at 2022-06-13 05:38:16.656506
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = '/sbin/iptables'

# Generated at 2022-06-13 05:38:28.390622
# Unit test for function check_present

# Generated at 2022-06-13 05:38:30.673990
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = '/usr/bin/iptables'
    module = 'module'
    params = {
        'chain': 'INPUT',
        'jump': ACCEPT,
        'table': 'filter'
    }
    cmd = push_arguments(iptables_path, '-D', params)
    module.run_command(cmd, check_rc=True)



# Generated at 2022-06-13 05:38:37.219774
# Unit test for function set_chain_policy
def test_set_chain_policy():
    params = dict(
        chain='INPUT',
        policy='DROP',
    )
    iptables_path = '/sbin/iptables'
    action = '-P'
    cmd = push_arguments(iptables_path, action, params, make_rule=False)
    assert cmd == ['/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP']
# End of unit test



# Generated at 2022-06-13 05:38:58.998632
# Unit test for function construct_rule
def test_construct_rule():
    rule = [
        '-w', '-p', 'tcp', '-s', '127.0.0.1', '-d', '127.0.0.1', '-m', 'comment',
        '--comment', 'Test rule', '-j', 'ACCEPT', '-w', '5', '-p', 'tcp', '-s',
        '127.0.0.1', '-d', '127.0.0.1', '-m', 'comment', '--comment', 'Test rule',
        '-j', 'ACCEPT'
    ]

# Generated at 2022-06-13 05:39:00.891572
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule(argument_spec={'append': {'required': True}, 'table': {'required': True}, 'chain': {'required': True}})
    check_present('iptables', module, {'append': True, 'table': 'mangle', 'chain': 'INPUT'}) == True



# Generated at 2022-06-13 05:39:09.621514
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:15.395296
# Unit test for function construct_rule
def test_construct_rule():
    # Set params
    params = dict(
        chain='INPUT',
        jump='DROP',
        protocol='tcp',
        destination='1.2.3.4',
        table='filter',
        ip_version='ipv4'
    )
    assert construct_rule(params) == ['-p', 'tcp', '-d', '1.2.3.4', '-j', 'DROP']



# Generated at 2022-06-13 05:39:24.810377
# Unit test for function get_chain_policy
def test_get_chain_policy():
    from ansible.module_utils import basic
    ipt_path = '/bin/iptables'
    module = basic.AnsibleModule(argument_spec=dict())
    module.exit_json = lambda **kwargs: None
    module.run_command = lambda cmd, **kwargs: (0, 'Chain INPUT (policy DROP)', '')
    assert get_chain_policy(ipt_path, module, dict(chain='INPUT', ip_version='ipv4')) == 'DROP'
    module.run_command = lambda cmd, **kwargs: (0, 'Chain INPUT', '')
    assert get_chain_policy(ipt_path, module, dict(chain='INPUT', ip_version='ipv4')) is None


# Generated at 2022-06-13 05:39:33.150264
# Unit test for function construct_rule

# Generated at 2022-06-13 05:39:45.585998
# Unit test for function flush_table
def test_flush_table():
    assert flush_table('/usr/bin/iptables',{'run_command': lambda x,y: None, 'test': True},{'table':'filter', 'chain': 'INPUT'})
    assert flush_table('/usr/bin/iptables',{'run_command': lambda x,y: None, 'test': True},{'table':'filter', 'chain': 'OUTPUT'})
    assert flush_table('/usr/bin/iptables',{'run_command': lambda x,y: None, 'test': True},{'table':'filter', 'chain': 'FORWARD'})
    assert flush_table('/usr/bin/iptables',{'run_command': lambda x,y: None, 'test': True},{'table':'nat', 'chain': 'PREROUTING'})
    assert flush_

# Generated at 2022-06-13 05:39:50.617076
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('/bin/iptables', None, {'table': 'filter', 'chain': 'INPUT'}) == 'ACCEPT'
    assert get_chain_policy('/bin/iptables', None, {'table': 'filter', 'chain': 'OUTPUT'}) == 'ACCEPT'
    assert get_chain_policy('/bin/iptables', None, {'table': 'filter', 'chain': 'FORWARD'}) == 'ACCEPT'
    assert get_chain_policy('/bin/iptables', None, {'table': 'filter', 'chain': 'NEW_CHAIN'}) == None



# Generated at 2022-06-13 05:39:52.968576
# Unit test for function get_chain_policy
def test_get_chain_policy():
    params = init_params()
    params['chain'] = 'INPUT'
    params['policy'] = 'DROP'
    params['ip_version'] = 'ipv4'
    assert get_chain_policy(BINS[params['ip_version']], module, params) == 'DROP'


# Generated at 2022-06-13 05:39:53.349398
# Unit test for function append_rule
def test_append_rule():
    return None



# Generated at 2022-06-13 05:40:16.935065
# Unit test for function construct_rule
def test_construct_rule():
    params_rule=dict(
        protocol='tcp',
        destination_port='22',
        destination='192.168.1.0/24',
        source='192.168.1.100/32',
        in_interface='eth0',
        out_interface='eth1',
        jump='DROP',
        ip_version='ipv4'
    )
    rule = construct_rule(params_rule)
    assert rule ==['-p', 'tcp', '-d', '192.168.1.0/24', '-s', '192.168.1.100/32', '-i', 'eth0', '-o', 'eth1', '--destination-port', '22', '-j', 'DROP']



# Generated at 2022-06-13 05:40:23.689091
# Unit test for function main
def test_main():
    def fail_json(msg):
        print(msg)
        sys.exit(1)

    def exit_json(**kwargs):
        print(kwargs)
        sys.exit(0)

    class FakeModule:
        def __init__(self, exit_function, fail_function):
            self.exit_json = exit_function
            self.fail_json = fail_function

        def get_bin_path(self, executable):
            return "/sbin/iptables"

        def check_mode(self):
            return False


# Generated at 2022-06-13 05:40:25.343876
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None,None,"INPUT") == "ACCEPT"



# Generated at 2022-06-13 05:40:28.217229
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {'policy': 'INPUT'}) is None
    assert get_chain_policy(None, None, {'policy': 'DROP'}) == 'DROP'



# Generated at 2022-06-13 05:40:33.707866
# Unit test for function get_chain_policy
def test_get_chain_policy():
    import StringIO
    module = type('', (object,), {})
    module.run_command = lambda cmd, check_rc=True: (0, "Chain INPUT (policy ACCEPT)", "")
    assert get_chain_policy('/sbin/iptables', module, dict(chain="INPUT")) == 'ACCEPT'
    module.run_command = lambda cmd, check_rc=True: (0, "Chain INPUT (policy DROP)", "")
    assert get_chain_policy('/sbin/iptables', module, dict(chain="INPUT")) == 'DROP'
    module.run_command = lambda cmd, check_rc=True: (0, "", "")
    assert get_chain_policy('/sbin/iptables', module, dict(chain="INPUT")) is None

# Generated at 2022-06-13 05:40:40.684197
# Unit test for function check_present
def test_check_present():
    module = AnsibleModule({})

# Generated at 2022-06-13 05:40:54.225552
# Unit test for function main

# Generated at 2022-06-13 05:41:00.126931
# Unit test for function remove_rule
def test_remove_rule():
    module = AnsibleModule(dict())
    params = dict(
        chain='INPUT',
        rule_num='2',
    )
    cmd = push_arguments('iptables', module, params)
    assert cmd == ['iptables', '-t', 'filter', '-D', 'INPUT', '2']
    params['rule_num'] = None
    cmd = push_arguments('iptables', module, params)
    assert cmd == ['iptables', '-t', 'filter', '-D', 'INPUT']



# Generated at 2022-06-13 05:41:05.690153
# Unit test for function construct_rule

# Generated at 2022-06-13 05:41:11.839323
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = '/usr/bin/iptables'

# Generated at 2022-06-13 05:41:44.987767
# Unit test for function set_chain_policy
def test_set_chain_policy():
    print(set_chain_policy('iptables',None,{'chain':'INPUT','policy':'DROP','table':'filter'}))



# Generated at 2022-06-13 05:41:52.292812
# Unit test for function construct_rule
def test_construct_rule():
    test_params = dict(
        chain='INPUT',
        state='absent',
        ip_version='ipv4',
        protocol='tcp',
        source='192.168.0.5',
        destination='192.168.0.0/16',
        jump='ACCEPT',
        in_interface='eth0',
        out_interface='eth1',
        destination_port='80',
        limit='100/hour',
        log_prefix='all ',
        log_level='warning',
        comment='Some comment',
    )
    test_rule = construct_rule(test_params)

# Generated at 2022-06-13 05:41:55.528413
# Unit test for function set_chain_policy
def test_set_chain_policy():
    set_chain_policy('/sbin/iptables', 'module', 'params')



# Generated at 2022-06-13 05:42:00.959908
# Unit test for function main
def test_main():
    ip_version = 'ipv4'
    iptables_path = module.get_bin_path(BINS[ip_version], True)

# Generated at 2022-06-13 05:42:02.169104
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy() == 'ACCEPT'


# Generated at 2022-06-13 05:42:08.028064
# Unit test for function set_chain_policy
def test_set_chain_policy():
    iptables_path = '/usr/sbin/iptables'
    module = AnsibleModule()
    module.run_command = MagicMock(return_value=[0, "1", ""])
    params = dict(chain="INPUT", policy="DROP")
    set_chain_policy(iptables_path, module, params)
    module.run_command.assert_called_with(['/usr/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP'])

# Unit tests for functions append_rule and check_present

# Generated at 2022-06-13 05:42:10.694961
# Unit test for function append_rule
def test_append_rule():
    cmd = push_arguments("/usr/sbin/iptables", '-A', params)
    module.run_command(cmd, check_rc=True)



# Generated at 2022-06-13 05:42:16.137315
# Unit test for function remove_rule
def test_remove_rule():
    iptables_path = '/usr/bin/iptables'
    action = '-D'
    table = 'filter'
    chain = 'INPUT'
    target = 'ACCEPT'
    protocol = 'tcp'
    source = None
    destination = '10.0.0.4'
    match = None
    tcp_flags = None
    jump = 'ACCEPT'
    log_prefix = None
    log_level = None
    to_destination = None
    destination_ports = None
    to_source = None
    goto = None
    comment = None
    in_interface = None
    out_interface = None
    fragment = None
    set_counters = None
    source_port = None
    destination_port = '443'
    to_ports = None
    set_dscp_mark = None

# Generated at 2022-06-13 05:42:19.623513
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('', '', dict(chain='INPUT', table='filter')) is None
    assert get_chain_policy('', '', dict(chain='INPUT', table='nat')) == 'ACCEPT'
    assert get_chain_policy('', '', dict(chain='OUTPUT', table='filter')) == 'ACCEPT'



# Generated at 2022-06-13 05:42:28.870152
# Unit test for function construct_rule

# Generated at 2022-06-13 05:42:55.165923
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy(None, None, {"chain": "INPUT"}) == "INPUT"
    assert get_chain_policy(None, None, {"chain": "FORWARD"}) == "FORWARD"
    assert get_chain_policy(None, None, {"chain": "OUTPUT"}) == "OUTPUT"
    assert get_chain_policy(None, None, {"chain": "test"}) is None



# Generated at 2022-06-13 05:43:03.441425
# Unit test for function append_rule
def test_append_rule():
    assert append_rule(['iptables','-t','nat','-A','OUTPUT'],['-p','tcp','-d','10.25.2.2','--dport','22','-j','ACCEPT']) == ['iptables','-t','nat','-A','OUTPUT','-p','tcp','-d','10.25.2.2','--dport','22','-j','ACCEPT']



# Generated at 2022-06-13 05:43:08.751005
# Unit test for function check_present
def test_check_present():
    import tempfile
    from ansible.module_utils.common._collections_compat import Mapping

    class DummyModule(object):
        def __init__(self, params):
            self.params = params
            self.run_command_count = 0

        def run_command(self, cmd, check_rc=True):
            self.run_command_count += 1
            if isinstance(cmd, list):
                cmd = ' '.join(cmd)
            expected = self.params['expected_command']
            if isinstance(expected, list):
                expected = ' '.join(expected)
            assert cmd == expected
            return self.params['return_code'], None, None

    def test_it(desc, params, present):
        tempfd, tempfn = tempfile.mkstemp()
        params['expected_command']

# Generated at 2022-06-13 05:43:10.089969
# Unit test for function main
def test_main():
    rv = main()

# Generated at 2022-06-13 05:43:14.473135
# Unit test for function insert_rule
def test_insert_rule():
    iptables_path = '/sbin/iptables'
    module = AnsibleModule(argument_spec={})
    params = dict(
        table='filter',
        chain='INPUT',
        protocol='tcp',
        destination_port='8080',
        jump='ACCEPT',
        action='insert',
        rule_num=5)
    cmd = push_arguments(iptables_path, '-I', params)
    assert (cmd == ['/sbin/iptables', '-t', 'filter', '-I', 'INPUT', '5', '-p', 'tcp', '--destination-port', '8080', '-j', 'ACCEPT'])



# Generated at 2022-06-13 05:43:16.225340
# Unit test for function get_chain_policy
def test_get_chain_policy():
    assert get_chain_policy('iptables', 'INPUT') == 'ACCEPT'



# Generated at 2022-06-13 05:43:23.224234
# Unit test for function construct_rule
def test_construct_rule():
    assert construct_rule({}) == []
    assert construct_rule(dict(protocol='tcp')) == ['-p', 'tcp']
    assert construct_rule(dict(source='8.8.8.8')) == ['-s', '8.8.8.8']
    assert construct_rule(dict(destination='8.8.8.8')) == ['-d', '8.8.8.8']
    assert construct_rule(dict(match='state')) == ['-m', 'state']
    assert construct_rule(dict(match='state', ctstate='x')) == ['-m', 'state', '--state', 'x']
    assert construct_rule(dict(jump='DROP')) == ['-j', 'DROP']

# Generated at 2022-06-13 05:43:32.617851
# Unit test for function construct_rule

# Generated at 2022-06-13 05:43:36.372885
# Unit test for function check_present
def test_check_present():
    import os
    ipv4_path = BINS['ipv4']
    if os.path.exists(ipv4_path):
        rule = ['-t', 'filter', '-C', 'INPUT']
        rule.extend(construct_rule(params))
        cmd = [ipv4_path]
        cmd.extend(rule)
        print(cmd)
        rc, _, __ = module.run_command(cmd, check_rc=False)
        return rc == 0
    else:
        return False



# Generated at 2022-06-13 05:43:47.854196
# Unit test for function main
def test_main():
    # Get test function parameters
    table = 'filter'
    state = 'present'
    action = 'append'
    ip_version = 'ipv4'
    chain = 'test-chain'
    rule_num = '0'
    protocol = 'tcp'
    source = '1.2.3.4'
    destination = '4.3.2.1'
    match = []
    tcp_flags = {'flags': ['SYN'], 'flags_set': []}
    jump = 'ACCEPT'
    log_prefix = 'HOST-OUT'
    log_level = 'warning'
    to_source = '5.6.7.8'
    to_destination = '10.9.8.7'
    goto = 'test-chain'
    in_interface = ''