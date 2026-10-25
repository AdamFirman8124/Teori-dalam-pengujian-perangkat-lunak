

# Generated at 2026-10-24 11:27:19.430508
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:21.850031
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:24.268831
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:26.689867
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:29.115763
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:31.530944
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:34.053629
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:36.475286
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:38.895496
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:41.315506
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:43.724643
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:46.146058
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:48.564645
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:50.987257
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:53.407317
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:55.828653
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:27:58.251750
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:28:00.665433
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:28:03.085996
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:28:05.502885
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:28:07.926564
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:28:24.461313
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:28:40.834616
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:29:07.017786
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.commands = []
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.commands.append(command)
            return (
                0,
                'kernel.ostype = Linux\n'
                'net.ipv4.ip_forward = 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                'example.colon: colon value\n'
                '\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4'])

    assert module.commands == [
        ['/sbin/sysctl', 'kernel', 'net.ipv4']
    ]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
        'example.colon': 'colon value',
    }

# Generated at 2026-10-24 11:29:09.532628
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:29:10.841938
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 11:29:36.774400
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.command = None
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.command = command
            return (
                0,
                'kernel.hostname = test-host\n'
                'vm.swappiness: 10\n'
                'kernel.core_pattern = first line\n'
                ' second line\n'
                ' third line\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'vm'])

    assert module.command == ['/sbin/sysctl', 'kernel', 'vm']
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'vm.swappiness': '10',
        'kernel.core_pattern': 'first line\n second line\n third line',
    }

# Generated at 2026-10-24 11:29:38.208712
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:29:47.939240
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self):
            self.commands = []
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.commands.append(command)
            return (
                0,
                (
                    'net.ipv4.ip_forward = 1\n'
                    'kernel.hostname: test-host\n'
                    'kernel.core_pattern = first line\n'
                    '  second line\n'
                    '\tthird line\n'
                    '\n'
                ),
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['net.ipv4', 'kernel'])

    assert module.commands == [
        ['/sbin/sysctl', 'net.ipv4', 'kernel']
    ]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'test-host',
        'kernel.core_pattern': 'first line\n  second line\n\tthird line',
    }

# Generated at 2026-10-24 11:29:50.363803
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:29:52.781385
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:29:55.204679
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:29:57.619667
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:00.037030
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:02.453188
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:04.869216
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:07.289755
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:09.708381
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:12.125369
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:14.542753
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:16.956172
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:19.374129
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:21.793520
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:24.212577
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:26.633852
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:29.061540
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:31.480015
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:33.898107
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:36.314408
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:38.731754
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:41.149338
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:43.565645
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:45.982859
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:48.397747
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:50.814888
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:53.230437
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:55.646916
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:30:58.064244
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:00.489143
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:02.903197
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:05.323935
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:07.738379
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:10.156990
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:12.574913
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:15.501687
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:31:27.366684
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.commands = []
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.commands.append(command)
            return 0, (
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward = 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                'example.colon: colon value\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
        'example.colon': 'colon value',
    }

# Generated at 2026-10-24 11:31:28.693855
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:31:45.386968
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:32:01.977261
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:32:04.399363
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:06.816334
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:09.454546
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:11.902973
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:14.463086
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:16.882437
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:19.299702
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:21.718051
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:24.133640
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:26.552425
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:28.969330
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:31.387282
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:33.803181
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:36.221251
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:38.642456
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:41.060083
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:43.477510
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:45.893210
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:48.310276
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:50.727186
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:32:53.288863
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:11.395854
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:12.710933
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 11:33:30.530681
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:33.048536
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:35.464035
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:37.886847
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:40.303727
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:42.721234
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:45.287273
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:47.705786
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:50.123963
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:52.544191
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:54.958598
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:33:57.593652
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:14.032448
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:34:30.701700
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:34:33.253406
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:35.670342
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:38.086558
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:40.502060
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:42.922607
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:45.339240
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:47.914885
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:50.333829
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:52.749012
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:55.167837
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:34:57.585295
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:00.005536
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:02.418574
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:04.838550
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:07.254134
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:23.983894
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:35:40.704240
# Unit test for function get_sysctl
def test_get_sysctl():
    # 1. Simple single-line output
    out = 'net.ipv4.ip_forward = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}, result

    # 2. Colon-separated format (BSD style)
    out = 'kern.ostype: Darwin\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kern'])
    assert result == {'kern.ostype': 'Darwin'}, result

    # 3. Multiple keys
    out = 'net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 0\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '0',
    }, result

    # 4. Multiline value (continuation lines start with a space)
    out = 'user.contract = line one\n line two\n line three\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['user'])
    assert result == {'user.contract': 'line one\n line two\n line three'}, result

    # 5. Value containing '=' â must split on first separator only
    out = 'kernel.something = a=b=c\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.something': 'a=b=c'}, result

    # 6. Non-zero rc returns empty dict
    m = FakeModule(1, '')
    result = module_0.get_sysctl(m, ['net'])
    assert result == {}, result

    # 7. Blank lines are skipped
    out = 'net.ipv4.ip_forward = 1\n\n   \nnet.ipv4.tcp_syncookies = 1\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['net'])
    assert len(result) == 2, result

    # 8. Warning is issued on rc failure path via exception â skip,
    #    but verify warn() collects messages when split fails silently
    out = 'malformed line without separator\n'
    m = FakeModule(0, out)
    result = module_0.get_sysctl(m, ['kernel'])
    # key stays '' and nothing is added â no crash
    assert result == {}, result

    print('test_get_sysctl: all assertions passed')


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2026-10-24 11:35:43.208677
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:45.627962
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:48.044485
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:50.462809
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:52.879330
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:55.296720
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:35:57.715924
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:00.280460
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:02.697030
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:05.115634
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:07.530732
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:09.946202
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:12.830018
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:15.248769
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:17.665390
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:20.081672
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:22.498593
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:24.918250
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:27.336201
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:29.753943
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:32.172505
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:34.587996
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:37.004542
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:39.422148
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:41.842071
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:44.262378
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:46.677765
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:49.094615
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:51.511894
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:53.925760
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:56.345465
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:36:58.765543
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:37:01.187628
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:37:03.605386
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:37:06.025916
# Unit test for function get_sysctl

# Generated at 2026-10-24 11:37:08.446446
# Unit test for function get_sysctl