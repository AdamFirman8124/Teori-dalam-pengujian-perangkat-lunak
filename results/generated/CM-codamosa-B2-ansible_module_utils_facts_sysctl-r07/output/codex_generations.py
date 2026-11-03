

# Generated at 2026-11-03 02:42:40.364760
# Unit test for function get_sysctl
def test_get_sysctl():import pytest


class FakeModule(object):
    """Mimics AnsibleModule for testing get_sysctl."""

    def __init__(self, rc=0, out='', err='', exception=None):
        self.rc = rc
        self.out = out
        self.err = err
        self.exception = exception
        self.warnings = []
        self.commands = []

    def get_bin_path(self, name):
        return '/sbin/%s' % name

    def run_command(self, cmd):
        self.commands.append(cmd)
        if self.exception is not None:
            raise self.exception
        return self.rc, self.out, self.err

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_single_key_value():
    module = FakeModule(out='net.ipv4.ip_forward = 1\n')
    result = module_0.get_sysctl(module, ['net.ipv4.ip_forward'])
    assert result == {'net.ipv4.ip_forward': '1'}
    assert module.commands == [['/sbin/sysctl', 'net.ipv4.ip_forward']]
    assert module.warnings == []


def test_get_sysctl_multiple_keys():
    module = FakeModule(out='a = 1\nb = 2\nc = 3\n')
    result = module_0.get_sysctl(module, ['a', 'b', 'c'])
    assert result == {'a': '1', 'b': '2', 'c': '3'}


def test_get_sysctl_command_with_multiple_prefixes():
    module = FakeModule(out='a = 1\nb = 2\n')
    module_0.get_sysctl(module, ['a', 'b'])
    assert module.commands == [['/sbin/sysctl', 'a', 'b']]


def test_get_sysctl_colon_separator():
    module = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.0\n')
    result = module_0.get_sysctl(module, ['kern'])
    assert result == {'kern.ostype': 'FreeBSD', 'kern.osrelease': '13.0'}


def test_get_sysctl_multiline_value():
    out = 'vm.stat = a\n b\n c\nother = 2\n'
    module = FakeModule(out=out)
    result = module_0.get_sysctl(module, ['vm.stat'])
    assert result == {'vm.stat': 'a\n b\n c', 'other': '2'}


def test_get_sysctl_empty_lines_skipped():
    module = FakeModule(out='\n\nkey = value\n\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}


def test_get_sysctl_strips_whitespace():
    module = FakeModule(out='key =    value   \n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}


def test_get_sysctl_no_separator_zero_spaces():
    module = FakeModule(out='key=value\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(rc=1, out='', err='some error')
    result = module_0.get_sysctl(module, ['nonexistent'])
    assert result == {}


def test_get_sysctl_run_command_exception_returns_empty_dict():
    module = FakeModule(exception=IOError('boom'))
    result = module_0.get_sysctl(module, ['net'])
    assert result == {}
    assert module.warnings == ['Unable to read sysctl: boom']


def test_get_sysctl_run_command_oserror_returns_empty_dict():
    module = FakeModule(exception=OSError(2, 'No such file'))
    result = module_0.get_sysctl(module, ['net'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]


def test_get_sysctl_unparseable_line_warns():
    out = 'good = 1\nthis-line-has-no-separator\n'
    module = FakeModule(out=out)
    result = module_0.get_sysctl(module, ['good'])
    assert result == {'good': '1'}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]
    assert 'this-line-has-no-separator' in module.warnings[0]


def test_get_sysctl_empty_output():
    module = FakeModule(out='')
    result = module_0.get_sysctl(module, ['all'])
    assert result == {}
    assert module.warnings == []

# Generated at 2026-11-03 02:48:24.882688
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self, rc=0, out='', err='', raise_exc=None):
            self.rc = rc
            self.out = out
            self.err = err
            self.raise_exc = raise_exc
            self.warnings = []
            self.run_command_args = None

        def get_bin_path(self, name):
            return '/sbin/%s' % name

        def run_command(self, cmd):
            self.run_command_args = cmd
            if self.raise_exc is not None:
                raise self.raise_exc
            return self.rc, self.out, self.err

        def warn(self, msg):
            self.warnings.append(msg)

    # basic parsing with '=' and ':' separators, prefixes passed to command
    module = MockModule(out='net.ipv4.ip_forward = 1\nkernel.hostname: myhost\n')
    result = module_0.get_sysctl(module, ['net.ipv4.ip_forward', 'kernel.hostname'])
    assert module.run_command_args == ['/sbin/sysctl', 'net.ipv4.ip_forward', 'kernel.hostname']
    assert result == {'net.ipv4.ip_forward': '1', 'kernel.hostname': 'myhost'}

    # values are stripped of surrounding whitespace
    module = MockModule(out='key =    value   \n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}

    # multiline values keep the newline and internal spacing
    module = MockModule(out='key1 = value1\nkey2 = line1\n continued line\n')
    result = module_0.get_sysctl(module, ['key1', 'key2'])
    assert result == {'key1': 'value1', 'key2': 'line1\n continued line'}

    # blank and whitespace-only lines are skipped
    module = MockModule(out='key1 = value1\n\n   \nkey2 = value2\n')
    result = module_0.get_sysctl(module, ['key1', 'key2'])
    assert result == {'key1': 'value1', 'key2': 'value2'}

    # value containing '=' is preserved (split on first occurrence only)
    module = MockModule(out='key = a=b\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'a=b'}

    # non-zero return code yields an empty dict
    module = MockModule(rc=1, out='ignored', err='failure')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {}

    # empty output yields an empty dict
    module = MockModule(out='')
    assert module_0.get_sysctl(module, ['key']) == {}

    # IOError while running the command warns and returns an empty dict
    module = MockModule(raise_exc=IOError('boom'))
    result = module_0.get_sysctl(module, ['key'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]
    assert 'boom' in module.warnings[0]

    # OSError while running the command warns and returns an empty dict
    module = MockModule(raise_exc=OSError('nope'))
    result = module_0.get_sysctl(module, ['key'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]

    # unparseable line produces a warning but parsing continues
    module = MockModule(out='badline\nkey = value\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]
    assert 'badline' in module.warnings[0]