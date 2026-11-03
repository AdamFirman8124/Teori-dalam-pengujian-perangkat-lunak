

# Generated at 2026-11-02 23:21:41.327196
# Unit test for function get_sysctl

# Generated at 2026-11-02 23:24:05.299807
# Unit test for function get_sysctl

# Generated at 2026-11-02 23:25:57.846235
# Unit test for function get_sysctl

# Generated at 2026-11-02 23:28:26.216944
# Unit test for function get_sysctl
def test_get_sysctl():
    # Basic "key = value" parsing
    module = MockSysctlModule(out='kernel.hostname = myhost\nkernel.osrelease = 4.15.0\n')
    result = module_0.get_sysctl(module, ['kernel'])
    assert result == {'kernel.hostname': 'myhost', 'kernel.osrelease': '4.15.0'}
    assert module.commands == [['/sbin/sysctl', 'kernel']]