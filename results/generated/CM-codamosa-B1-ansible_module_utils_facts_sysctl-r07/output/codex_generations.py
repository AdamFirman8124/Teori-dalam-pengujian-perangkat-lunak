

# Generated at 2026-10-25 08:23:29.839128
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:32.447583
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:34.862698
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:37.282935
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:39.780367
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:42.198476
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:44.614871
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:47.045361
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:49.462441
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:51.880997
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:54.312380
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:56.726992
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:23:59.149560
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:07.791543
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:09.270024
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:21.106295
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule:
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
                    'kernel.ostype = Linux\n'
                    'hw.ncpu: 8\n'
                    'example.multiline = first line\n'
                    ' second line\n'
                    ' third line\n'
                    '\n'
                ),
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'hw.ncpu': '8',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 08:24:32.574614
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []
            self.command = None

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.command = command
            return 0, (
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward = 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                'vm.swapusage: total = 1024M\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(
        module,
        ['kernel.hostname', 'net.ipv4.ip_forward', 'example.multiline',
         'vm.swapusage'],
    )

    assert module.command == [
        '/sbin/sysctl',
        'kernel.hostname',
        'net.ipv4.ip_forward',
        'example.multiline',
        'vm.swapusage',
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
        'vm.swapusage': 'total = 1024M',
    }

# Generated at 2026-10-25 08:24:34.995411
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:37.415884
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:39.833743
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:42.417069
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:44.836628
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:47.250512
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:49.671618
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:52.087428
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:54.506191
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:56.920124
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:24:59.338842
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:01.757775
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:04.179266
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:06.599656
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:09.016101
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:11.436067
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:13.854454
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:16.270611
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:28.075041
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:29.509117
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:30.944738
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:41.390651
# Unit test for function get_sysctl
def test_get_sysctl():
    class ModuleStub(object):
        def __init__(self):
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            assert command == ['/sbin/sysctl', '-a']
            return (
                0,
                'kernel.ostype = Linux\n'
                'net.ipv4.ip_forward: 1\n'
                '\n'
                'example.multiline = first line\n'
                ' second line\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = ModuleStub()

    result = module_0.get_sysctl(module, ['-a'])

    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 08:25:52.714511
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
            return 0, (
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward = 1\n'
                'kernel.seccomp.actions_avail = kill_process kill_thread\n'
                ' log trap errno user_notif\n'
                '\n'
                'hw.model: Test Model\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel', 'net', 'hw'])

    assert module.commands == [
        ['/sbin/sysctl', 'kernel', 'net', 'hw']
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.seccomp.actions_avail': (
            'kill_process kill_thread\n'
            ' log trap errno user_notif'
        ),
        'hw.model': 'Test Model',
    }

# Generated at 2026-10-25 08:25:55.133413
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:25:57.867593
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:00.284617
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:14.874140
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
                    '\n'
                    'kernel.hostname: test-host\n'
                    'example.multiline = first line\n'
                    ' second line\n'
                    ' third line\n'
                ),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['net.ipv4', 'kernel', 'example'])

    assert module.commands == [
        ['/sbin/sysctl', 'net.ipv4', 'kernel', 'example']
    ]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'test-host',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 08:26:24.601382
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
            return 0, (
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 0\n'
                '\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                'kernel.pid_max = 4194304\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4', 'example'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel',
        'net.ipv4',
        'example',
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '0',
        'example.multiline': 'first line\n second line\n third line',
        'kernel.pid_max': '4194304',
    }

# Generated at 2026-10-25 08:26:27.029229
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:29.447207
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:31.865076
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:34.328138
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:36.747786
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:39.336385
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:41.753378
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:44.169377
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:46.589199
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:49.006439
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:51.605539
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:54.021811
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:56.458559
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:26:58.873820
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:01.301480
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:03.720538
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:06.140758
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:16.719267
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:27.780556
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
                'net.ipv4.ip_forward: 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(
        module,
        ['kernel.hostname', 'net.ipv4.ip_forward', 'example.multiline'],
    )

    assert module.command == [
        '/sbin/sysctl',
        'kernel.hostname',
        'net.ipv4.ip_forward',
        'example.multiline',
    ]
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 08:27:37.692000
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []
            self.command = None

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.command = command
            return (
                0,
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward: 1',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                    '',
                ]),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4', 'example'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel',
        'net.ipv4',
        'example',
    ]
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 08:27:40.110148
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:42.531781
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:44.945077
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:47.363376
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:49.778136
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:52.195573
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:54.615207
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:57.437150
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:27:59.879105
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:02.347177
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:04.760863
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:07.180431
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:09.596659
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:12.013009
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:14.457902
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:16.884190
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:19.298965
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:21.714631
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:24.132167
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:26.549089
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:29.048010
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:31.464593
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:33.884476
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:36.302265
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:38.718459
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:41.135745
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:43.550448
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:45.968690
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:48.384144
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:50.882095
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:53.297732
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:55.717239
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:28:58.136872
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:10.186436
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:11.717953
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:13.055440
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:32.811856
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
                '\n'
                'example.multiline = first line\n'
                '  second line\n'
                'net.ipv4.ip_forward: 1\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel.hostname', 'net.ipv4'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel.hostname',
        'net.ipv4',
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'example.multiline': 'first line\n  second line',
        'net.ipv4.ip_forward': '1',
    }

# Generated at 2026-10-25 08:29:35.232008
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:37.648576
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:40.090404
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:42.755278
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:45.171467
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:47.584438
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:50.079478
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:52.462350
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:54.878706
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:57.294995
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:29:59.713150
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:30:02.130948
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:30:04.547786
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:30:06.964564
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:30:08.307244
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:30:56.255624
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 08:30:58.673908
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:01.142519
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:03.545409
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:05.960851
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:08.375932
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:10.790537
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:31:28.526699
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 08:32:02.213699
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:04.633957
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:07.048945
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:09.468825
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:12.158750
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:14.578628
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:17.126180
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:19.543772
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:21.956197
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:24.370386
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:26.786072
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:29.202895
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:31.618495
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:34.037110
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:36.499060
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:38.917651
# Unit test for function get_sysctl

# Generated at 2026-10-25 08:32:41.333882
# Unit test for function get_sysctl