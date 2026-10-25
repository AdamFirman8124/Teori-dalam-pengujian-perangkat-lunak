

# Generated at 2026-10-25 04:33:02.026947
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:04.441667
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:07.013859
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:09.428767
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:11.845408
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:14.259303
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:16.673683
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:19.088154
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:21.502541
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:23.917621
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:26.332553
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:28.750019
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:31.164246
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:33.579243
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:35.993334
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:38.408209
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:40.825945
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:43.237365
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:45.651745
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:48.068594
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:50.484560
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:52.901303
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:55.316089
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:33:57.734924
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:00.148469
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:02.565672
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:04.979002
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:07.394737
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:09.812363
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:17.510634
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:34:30.003854
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
                '\n'.join([
                    'net.ipv4.ip_forward = 1',
                    '',
                    'kernel.core_pattern: core.%e',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                ]),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['net.ipv4', 'kernel', 'example'])

    assert module.commands == [[
        '/sbin/sysctl',
        'net.ipv4',
        'kernel',
        'example',
    ]]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.core_pattern': 'core.%e',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:34:40.666557
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
                'kernel.hostname = testhost\n'
                'vm.swappiness: 10\n'
                '\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'vm', 'example'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel',
        'vm',
        'example',
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'testhost',
        'vm.swappiness': '10',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:34:51.917701
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                ''
            )

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
    }

# Generated at 2026-10-25 04:35:02.191579
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
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward=1',
                    'kern.securelevel: 0',
                    '',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                ]),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kern.securelevel': '0',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:35:04.736536
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:07.284948
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:09.702908
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:12.129560
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:14.545627
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:16.959287
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:35:28.717238
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
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward = 1',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                    'security.feature: enabled',
                    '',
                ]),
                '',
            )

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
        'security.feature': 'enabled',
    }

# Generated at 2026-10-25 04:35:39.636625
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            assert command == [
                '/sbin/sysctl',
                'kernel',
                'net.ipv4',
                'security',
            ]
            return (
                0,
                (
                    'kernel.hostname = test-host\n'
                    '\n'
                    'net.ipv4.ip_forward = 1\n'
                    'security.example: first line\n'
                    ' second line\n'
                    ' third line\n'
                ),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(
        module,
        ['kernel', 'net.ipv4', 'security'],
    )

    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'security.example': 'first line\n second line\n third line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 04:35:51.207764
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
                'kernel.hostname = test-host\n'
                'net.inet.ip.forwarding: 0\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n'
                'vm.swappiness = 10\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.inet.ip.forwarding': '0',
        'example.multiline': 'first line\n second line\n third line',
        'vm.swappiness': '10',
    }

# Generated at 2026-10-25 04:36:01.961593
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self):
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            assert command == ['/sbin/sysctl', 'kernel', 'vm']
            return (
                0,
                'kernel.hostname = test-host\n'
                'kernel.printk = 4 4 1 7\n'
                ' continued value\n'
                'vm.swappiness: 10\n'
                '\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel', 'vm'])

    assert result == {
        'kernel.hostname': 'test-host',
        'kernel.printk': '4 4 1 7\n continued value',
        'vm.swappiness': '10',
    }
    assert module.warnings == []

# Generated at 2026-10-25 04:36:11.893439
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
                (
                    'kernel.hostname = test-host\n'
                    'kern.maxfiles: 12288\n'
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
        'kernel.hostname': 'test-host',
        'kern.maxfiles': '12288',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:36:14.310804
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:16.731253
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:19.139992
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:21.555913
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:29.992232
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:36.263089
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:36:47.743485
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
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
                (
                    'kernel.hostname = test-host\n'
                    'kern.boottime: 12345\n'
                    'example.multiline = first line\n'
                    ' second line\n'
                    ' third line\n'
                    '\n'
                    'net.ipv4.ip_forward = 1\n'
                ),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.command == ['/sbin/sysctl', '-a']
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'kern.boottime': '12345',
        'example.multiline': 'first line\n second line\n third line',
        'net.ipv4.ip_forward': '1',
    }

# Generated at 2026-10-25 04:37:01.491928
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
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward = 1',
                    'user.cs_path: /usr/bin:/bin',
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

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'user.cs_path': '/usr/bin:/bin',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:37:11.804836
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
                'kernel.hostname = testhost\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.example = first line\n'
                ' second line\n'
                '\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'testhost',
        'net.ipv4.ip_forward': '1',
        'kernel.example': 'first line\n second line',
    }

# Generated at 2026-10-25 04:37:22.347217
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
                (
                    'kernel.hostname = test-host\n'
                    'net.ipv4.ip_forward = 1\n'
                    'example.colon: colon-value\n'
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
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.colon': 'colon-value',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:37:24.764428
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:37:30.126712
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:37:37.908247
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:37:51.735642
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
                'kern.maxfiles: 12288\n'
                'vm.swappiness = 10\n'
                'kernel.random.uuid = first line\n'
                '    second line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kern', 'vm'])

    assert module.commands == [['/sbin/sysctl', 'kern', 'vm']]
    assert module.warnings == []
    assert result == {
        'kern.maxfiles': '12288',
        'vm.swappiness': '10',
        'kernel.random.uuid': 'first line\n    second line',
    }

# Generated at 2026-10-25 04:38:03.303802
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
                'kernel.ostype = Linux\n'
                'kernel.domainname: example.com\n'
                'kernel.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel'])

    assert module.commands == [['/sbin/sysctl', 'kernel']]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'kernel.domainname': 'example.com',
        'kernel.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:38:15.489837
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
                'net.ipv4.ip_forward = 1\n'
                'kernel.hostname: test-host\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(
        module,
        ['net.ipv4.ip_forward', 'kernel.hostname', 'example.multiline']
    )

    assert module.command == [
        '/sbin/sysctl',
        'net.ipv4.ip_forward',
        'kernel.hostname',
        'example.multiline',
    ]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'test-host',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:38:17.906631
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:20.321688
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:22.736052
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:25.150390
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:27.564867
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:35.457957
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:38:46.311825
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []
            self.commands = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            self.commands.append(command)
            return (
                0,
                (
                    'kernel.ostype = Linux\n'
                    '\n'
                    'net.example = first line\n'
                    ' second line\n'
                    ' third line\n'
                    'hw.ncpu: 8\n'
                ),
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel.ostype', 'net.example', 'hw.ncpu'])

    assert module.commands == [[
        '/sbin/sysctl',
        'kernel.ostype',
        'net.example',
        'hw.ncpu',
    ]]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'net.example': 'first line\n second line\n third line',
        'hw.ncpu': '8',
    }

# Generated at 2026-10-25 04:38:57.986494
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
                    'example.multiline = first line\n'
                    ' second line\n'
                    ' third line\n'
                    '\n'
                    'vm.swappiness = 10\n'
                ),
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['net', 'kernel', 'vm'])

    assert module.commands == [
        ['/sbin/sysctl', 'net', 'kernel', 'vm']
    ]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'test-host',
        'example.multiline': 'first line\n second line\n third line',
        'vm.swappiness': '10',
    }

# Generated at 2026-10-25 04:39:08.023184
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import MagicMock

    module = MagicMock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (
        0,
        (
            'kernel.ostype = Linux\n'
            'net.ipv4.tcp_available_congestion_control = reno cubic\n'
            '    bbr\n'
            'vm.swappiness: 60\n'
            '\n'
        ),
        ''
    )

    result = module_0.get_sysctl(module, ['kernel', 'net', 'vm'])

    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.tcp_available_congestion_control': 'reno cubic\n    bbr',
        'vm.swappiness': '60',
    }
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(
        ['/sbin/sysctl', 'kernel', 'net', 'vm']
    )
    module.warn.assert_not_called()

# Generated at 2026-10-25 04:39:18.950301
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
                'net.ipv4.ip_forward: 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net'])

    assert module.commands == [['/sbin/sysctl', 'kernel', 'net']]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:39:28.501296
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
                'net.ipv4.ip_forward: 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net', 'example'])

    assert module.commands == [
        ['/sbin/sysctl', 'kernel', 'net', 'example']
    ]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:39:42.018363
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
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward: 1',
                    '',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                ]),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4', 'example'])

    assert module.commands == [
        ['/sbin/sysctl', 'kernel', 'net.ipv4', 'example']
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:39:53.596046
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
                (
                    'net.ipv4.ip_forward = 1\n'
                    'kernel.hostname: test-host\n'
                    'kernel.printk = 4 4 1 7\n'
                    'multiline.value = first line\n'
                    ' second line\n'
                    ' third line\n'
                    '\n'
                ),
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['net.ipv4', 'kernel'])

    assert module.commands == [
        ['/sbin/sysctl', 'net.ipv4', 'kernel']
    ]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'test-host',
        'kernel.printk': '4 4 1 7',
        'multiline.value': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:40:04.443184
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            assert command == ['/sbin/sysctl', 'kernel', 'net.ipv4']
            return (
                0,
                (
                    'kernel.hostname = test-host\n'
                    'kernel.domainname: example.com\n'
                    '\n'
                    'net.ipv4.ip_forward = 1\n'
                    'net.ipv4.tcp_allowed_congestion_control = reno\n'
                    ' cubic\n'
                ),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4'])

    assert result == {
        'kernel.hostname': 'test-host',
        'kernel.domainname': 'example.com',
        'net.ipv4.ip_forward': '1',
        'net.ipv4.tcp_allowed_congestion_control': 'reno\n cubic',
    }
    assert module.warnings == []

# Generated at 2026-10-25 04:40:13.627982
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.random.uuid = first line\n'
                ' second line\n'
                ' third line\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel.hostname', 'net.ipv4.ip_forward'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel.hostname',
        'net.ipv4.ip_forward',
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.random.uuid': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:40:26.764780
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                '\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                '',
            )

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
    }

# Generated at 2026-10-25 04:40:37.621864
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
                'kernel.ostype = Linux\n'
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

    result = module_0.get_sysctl(module, ['kernel', 'net.ipv4', 'example'])

    assert module.commands == [[
        '/sbin/sysctl',
        'kernel',
        'net.ipv4',
        'example',
    ]]
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:40:47.247200
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.random.uuid = first line\n'
                ' second line\n'
                ' third line\n',
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
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.random.uuid': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:40:58.231022
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:41:11.178065
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
                '\n'
                'test.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                ''
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['kernel', 'net', 'test'])

    assert module.command == [
        '/sbin/sysctl',
        'kernel',
        'net',
        'test',
    ]
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'test.multiline': 'first line\n second line\n third line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 04:41:22.025593
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
                'net.ipv4.ip_forward = 1\n'
                'kernel.hostname: example-host\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['net.ipv4', 'kernel', 'example'])

    assert module.commands == [[
        '/sbin/sysctl',
        'net.ipv4',
        'kernel',
        'example',
    ]]
    assert module.warnings == []
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'example-host',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:41:24.551301
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:41:26.965673
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:41:29.380409
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:41:38.247650
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule:
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
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.example = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel.hostname', 'net.ipv4.ip_forward'])

    assert module.commands == [[
        '/sbin/sysctl',
        'kernel.hostname',
        'net.ipv4.ip_forward',
    ]]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.example': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:41:46.954649
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self):
            self.warnings = []

        def get_bin_path(self, command):
            assert command == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, command):
            assert command == [
                '/sbin/sysctl',
                'kernel.hostname',
                'net.ipv4.ip_forward',
                'example.multiline',
            ]
            return (
                0,
                'kernel.hostname = test-host\n'
                'net.ipv4.ip_forward: 1\n'
                '\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, [
        'kernel.hostname',
        'net.ipv4.ip_forward',
        'example.multiline',
    ])

    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }
    assert module.warnings == []

# Generated at 2026-10-25 04:41:55.175768
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
                '\n'.join([
                    'kernel.hostname = test-host',
                    'net.ipv4.ip_forward: 1',
                    '',
                    'example.multiline = first line',
                    ' second line',
                    ' third line',
                ]),
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['kernel', 'net', 'example'])

    assert module.commands == [
        ['/sbin/sysctl', 'kernel', 'net', 'example']
    ]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-25 04:42:05.427639
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
                'net.ipv4.tcp_allowed_congestion_control = reno\n'
                ' cubic\n'
                '\n'
                'vm.swappiness: 60\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.commands == [['/sbin/sysctl', '-a']]
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.tcp_allowed_congestion_control': 'reno\n cubic',
        'vm.swappiness': '60',
    }

# Generated at 2026-10-25 04:42:07.844600
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:10.261392
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:12.677813
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:15.094450
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:17.510613
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:19.926842
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:22.339717
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:24.754889
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:27.171047
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:29.584879
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:31.998996
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:34.423283
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:36.837508
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:44.597186
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:42:50.851117
# Unit test for function get_sysctl

# Generated at 2026-10-25 04:43:00.879574
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
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
                '\n'
                'net.ipv4.ip_forward: 1\n'
                'kernel.test = first line\n'
                ' second line\n'
                ' third line\n'
            ), ''

        def warn(self, message):
            self.warnings.append(message)

    module = MockModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.command == ['/sbin/sysctl', '-a']
    assert module.warnings == []
    assert result == {
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'kernel.test': 'first line\n second line\n third line',
    }