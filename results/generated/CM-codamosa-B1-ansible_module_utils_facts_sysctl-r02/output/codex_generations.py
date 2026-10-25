

# Generated at 2026-10-24 21:45:54.491412
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:45:56.908389
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:45:59.324579
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:11.603328
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:12.920923
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:14.242935
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:15.565448
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:16.885162
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:18.269947
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:19.704904
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:21.028205
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:22.349751
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:23.677991
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:25.004680
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:26.338124
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:27.659631
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:28.988434
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:46:31.407703
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:33.823701
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:36.239163
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:38.656610
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:41.074953
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:43.649254
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:46.066034
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:48.484884
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:50.901940
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:53.476577
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:55.896809
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:46:58.311640
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:00.732155
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:02.117104
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:03.467725
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:04.965994
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:06.399273
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:07.714506
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:09.043338
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:10.426155
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:11.740991
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:13.070302
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:14.396368
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:15.730376
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:17.088005
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:18.447569
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:19.792331
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:21.119179
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:47:23.652987
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:26.177997
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:28.593983
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:31.013737
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:33.434023
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:35.855637
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:38.274712
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:40.690698
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:43.111699
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:45.529856
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:47.955605
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:50.375228
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:53.286324
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:55.705938
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:47:58.125649
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:00.543872
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:02.965118
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:05.385537
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:07.801621
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:10.218905
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:12.637046
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:15.055083
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:17.472239
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:19.891912
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:22.307833
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:24.726805
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:27.144046
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:29.564729
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:31.982217
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:34.398913
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:48:35.784248
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:37.182260
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:38.504737
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:39.828873
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:42.700840
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:44.070362
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:45.398585
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:46.730771
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:48.050948
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:49.381133
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:50.728742
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:52.060320
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:53.385465
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:48:54.701817
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:49:02.020743
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:04.437557
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:06.855967
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:09.272429
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:11.688556
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:14.106507
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:16.528007
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:18.944789
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:21.365892
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:23.883572
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:26.304230
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:28.720080
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:31.137891
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:33.554120
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:35.969142
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:38.384219
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:40.802848
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:43.220866
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:45.635306
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:48.055154
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:50.471084
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:52.888900
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:55.308631
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:49:57.727386
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:09.287885
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:10.608946
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:12.050006
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:13.373628
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:50:25.466396
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:50:26.835370
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:50:28.164187
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:50:29.494915
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:50:32.017305
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:34.434054
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:36.955428
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:39.371828
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:41.790381
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:44.212920
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:46.626707
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:49.042886
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:51.460923
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:53.876880
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:56.461093
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:50:58.877292
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:10.624600
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:11.939357
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:13.266090
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:14.637667
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:51:38.806478
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:41.222152
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:43.639999
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:46.058862
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:48.477442
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:50.892439
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:53.311512
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:55.728674
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:51:58.147078
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:52:00.566684
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:52:03.154172
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:52:04.478426
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:52:05.879116
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:07.202336
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:08.522846
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:09.841844
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:11.161020
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:12.484168
# Unit test for function get_sysctl
def test_get_sysctl():
    # --- normal single-line output (Linux style) ---
    mod = FakeModule(out='net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n')
    result = module_0.get_sysctl(mod, ['net.ipv4', 'kernel'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost',
    }, result

    # --- FreeBSD style (colon separator) ---
    mod = FakeModule(out='kern.ostype: FreeBSD\nkern.osrelease: 13.1\n')
    result = module_0.get_sysctl(mod, ['kern'])
    assert result == {
        'kern.ostype': 'FreeBSD',
        'kern.osrelease': '13.1',
    }, result

    # --- multiline value keeps embedded newlines, strips trailing whitespace ---
    out = 'kernel.some_list = a\n b\n c\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['kernel'])
    assert result == {'kernel.some_list': 'a\n b\n c'}, repr(result)

    # --- non-zero rc returns empty dict ---
    mod = FakeModule(rc=1, out='garbage')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result

    # --- run_command raising OSError warns and returns empty dict ---
    mod = FakeModule(raise_exc=True)
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result
    assert len(mod.warnings) == 1
    assert 'Unable to read sysctl' in mod.warnings[0]

    # --- unparseable line warns, last valid key still captured ---
    out = 'good.key = 1\nbroken-line-no-separator\n'
    mod = FakeModule(out=out)
    result = module_0.get_sysctl(mod, ['good'])
    assert result.get('good.key') == '1', result
    assert len(mod.warnings) == 1
    assert 'Unable to split sysctl line' in mod.warnings[0]

    # --- empty output ---
    mod = FakeModule(out='')
    result = module_0.get_sysctl(mod, ['x'])
    assert result == {}, result


if __name__ == '__main__':
    test_get_sysctl()
    print('all tests passed')

# Generated at 2026-10-24 21:52:59.988406
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:02.405835
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:04.822081
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:07.239796
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:09.658119
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:12.073785
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:14.490125
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:16.905991
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:19.324376
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:21.740882
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:24.158797
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:26.573697
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:28.990156
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:31.406619
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:33.822986
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:36.241953
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:38.656881
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:41.076933
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:43.493753
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:45.909527
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:48.326802
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:50.743442
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:53.160448
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:55.575984
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:53:57.991927
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:54:00.411991
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:54:02.827065
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:54:05.245529
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:54:07.661034
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:54:10.077931
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:43.356520
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:45.780172
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:48.197691
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:50.617446
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:53.032937
# Unit test for function get_sysctl

# Generated at 2026-10-24 21:55:55.451608
# Unit test for function get_sysctl