

# Generated at 2026-11-02 18:25:11.175637
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self, rc=0, out='', err='', exc=None):
            self.rc = rc
            self.out = out
            self.err = err
            self.exc = exc
            self.warnings = []
            self.commands = []

        def get_bin_path(self, name):
            assert name == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, cmd):
            self.commands.append(cmd)
            if self.exc is not None:
                raise self.exc
            return self.rc, self.out, self.err

        def warn(self, msg):
            self.warnings.append(msg)

    # Simple "key = value" output
    m = FakeModule(out='kernel.hostname = testhost\nkernel.osrelease = 1.2.3\n')
    result = module_0.get_sysctl(m, ['kernel'])
    assert result == {'kernel.hostname': 'testhost', 'kernel.osrelease': '1.2.3'}
    assert m.commands == [['/sbin/sysctl', 'kernel']]
    assert m.warnings == []

    # Colon separated output (e.g. BSD style)
    m = FakeModule(out='hw.model: MacBookPro\nhw.ncpu: 4\n')
    result = module_0.get_sysctl(m, ['hw'])
    assert result == {'hw.model': 'MacBookPro', 'hw.ncpu': '4'}

    # Values are stripped of surrounding whitespace
    m = FakeModule(out='a  =   spaced   \nb=2\n')
    result = module_0.get_sysctl(m, [])
    assert result == {'a': 'spaced', 'b': '2'}

    # Multi-line values: continuation lines start with a space, newline is preserved
    m = FakeModule(out='key = first\n second line\nother = 2\n')
    result = module_0.get_sysctl(m, ['k'])
    assert result == {'key': 'first\nsecond line', 'other': '2'}

    # Blank lines are ignored
    m = FakeModule(out='\na = 1\n\n\nb = 2\n\n')
    result = module_0.get_sysctl(m, ['x'])
    assert result == {'a': '1', 'b': '2'}

    # Empty output yields an empty dict
    m = FakeModule(out='')
    assert module_0.get_sysctl(m, ['x']) == {}

    # Multiple prefixes are appended to the command line
    m = FakeModule(out='a = 1\n')
    result = module_0.get_sysctl(m, ['a', 'b', 'c'])
    assert m.commands == [['/sbin/sysctl', 'a', 'b', 'c']]
    assert result == {'a': '1'}

    # Non-zero return code yields an empty dict without warnings
    m = FakeModule(rc=1, out='a = 1\n')
    result = module_0.get_sysctl(m, ['a'])
    assert result == {}
    assert m.warnings == []

    # IOError/OSError while running the command warns and returns an empty dict

# Generated at 2026-11-02 18:26:51.822057
# Unit test for function get_sysctl
def test_get_sysctl():import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class MockModule(object):
    def __init__(self, rc=0, out='', err='', raise_error=False):
        self.rc = rc
        self.out = out
        self.err = err
        self.raise_error = raise_error
        self.warnings = []
        self.cmd = None

    def get_bin_path(self, name):
        return '/sbin/%s' % name

    def run_command(self, cmd):
        if self.raise_error:
            raise IOError('unable to run sysctl')
        self.cmd = cmd
        return self.rc, self.out, self.err

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_single_key():
    module = MockModule(out='kernel.hostname = test.example.com\n')
    result = module_0.get_sysctl(module, ['kernel.hostname'])
    assert result == {'kernel.hostname': 'test.example.com'}


def test_get_sysctl_multiple_keys():
    out = 'kernel.hostname = host1\nkernel.ostype = Linux\nkernel.osrelease = 4.19.0\n'
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['kernel.hostname', 'kernel.ostype', 'kernel.osrelease'])
    assert result == {
        'kernel.hostname': 'host1',
        'kernel.ostype': 'Linux',
        'kernel.osrelease': '4.19.0',
    }


def test_get_sysctl_colon_separator():
    module = MockModule(out='net.ipv4.tcp_sack: 1\n')
    result = module_0.get_sysctl(module, ['net.ipv4.tcp_sack'])
    assert result == {'net.ipv4.tcp_sack': '1'}


def test_get_sysctl_multiline_value():
    out = 'key.one = line1\n line2\n line3\nkey.two = value\n'
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['key.one', 'key.two'])
    assert result == {
        'key.one': 'line1\n line2\n line3',
        'key.two': 'value',
    }


def test_get_sysctl_blank_lines_ignored():
    module = MockModule(out='\n\nkey = value\n\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}


def test_get_sysctl_strips_whitespace():
    module = MockModule(out='key   =   value  \n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {'key': 'value'}


def test_get_sysctl_nonzero_rc_returns_empty():
    module = MockModule(rc=1, out='key = value\n')
    result = module_0.get_sysctl(module, ['key'])
    assert result == {}


def test_get_sysctl_run_command_exception_warns():
    module = MockModule(raise_error=True)
    result = module_0.get_sysctl(module, ['kernel.hostname'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]


def test_get_sysctl_unsplittable_line_warns():
    module = MockModule(out='badline\n')
    result = module_0.get_sysctl(module, ['badline'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]


def test_get_sysctl_command_construction():
    module = MockModule(out='')
    module_0.get_sysctl(module, ['a', 'b'])
    assert module.cmd == ['/sbin/sysctl', 'a', 'b']

# Generated at 2026-11-02 18:32:14.494675
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self, rc=0, out='', err='', raise_exc=False):
            self.rc = rc
            self.out = out
            self.err = err
            self.raise_exc = raise_exc
            self.warnings = []
            self.commands = []

        def get_bin_path(self, binary):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            self.commands.append(cmd)
            if self.raise_exc:
                raise IOError('mock failure')
            return self.rc, self.out, self.err

        def warn(self, message):
            self.warnings.append(message)

    # Basic '=' separated keys, prefixes appended to the command
    module = MockModule(out='kernel.hostname = test.example.com\nkernel.ostype = Linux\n')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'kernel.hostname': 'test.example.com', 'kernel.ostype': 'Linux'}
    assert module.commands == [['/sbin/sysctl', '-a']]

    # ':' separated keys
    module = MockModule(out='hw.model: MacBookPro\nhw.ncpu: 4\n')
    result = module_0.get_sysctl(module, ['hw'])
    assert result == {'hw.model': 'MacBookPro', 'hw.ncpu': '4'}

    # Multiline values keep embedded newlines and leading spaces
    module = MockModule(out='vm.stat = a\n b\n c\nkernel.ostype = Linux\n')
    result = module_0.get_sysctl(module, ['vm'])
    assert result == {'vm.stat': 'a\n b\n c', 'kernel.ostype': 'Linux'}

    # Blank lines are ignored
    module = MockModule(out='kernel.hostname = test\n\nkernel.ostype = Linux\n')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {'kernel.hostname': 'test', 'kernel.ostype': 'Linux'}

    # Values containing separators are kept intact (maxsplit=1)
    module = MockModule(out='kernel.cfg = a = b : c\n')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {'kernel.cfg': 'a = b : c'}

    # Non-zero return code yields empty dict
    module = MockModule(rc=1, out='kernel.hostname = test\n', err='failure')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {}

    # Empty output yields empty dict
    module = MockModule(out='')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {}

    # run_command raising IOError results in a warning and empty dict
    module = MockModule(raise_exc=True)
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]

    # Unparseable line triggers a warning but other keys are still parsed
    module = MockModule(out='kernel.hostname = test\nbrokenline\nkernel.ostype = Linux\n')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {'kernel.hostname': 'test', 'kernel.ostype': 'Linux'}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]