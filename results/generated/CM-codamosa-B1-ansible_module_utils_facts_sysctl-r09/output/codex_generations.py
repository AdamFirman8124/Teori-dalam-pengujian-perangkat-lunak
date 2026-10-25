

# Generated at 2026-10-24 20:17:55.772228
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

# Generated at 2026-10-24 20:17:57.104840
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

# Generated at 2026-10-24 20:17:58.517032
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

# Generated at 2026-10-24 20:17:59.850234
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

# Generated at 2026-10-24 20:18:01.197126
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

# Generated at 2026-10-24 20:18:02.534331
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

# Generated at 2026-10-24 20:18:03.934713
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

# Generated at 2026-10-24 20:18:05.270030
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

# Generated at 2026-10-24 20:18:06.727703
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

# Generated at 2026-10-24 20:18:09.268501
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:11.798731
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:14.215370
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:16.795426
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:19.341127
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:21.759001
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:24.204182
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:26.606663
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:29.172372
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:31.587392
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:34.003546
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:36.418925
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:38.836844
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:41.255664
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:43.673219
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:46.090938
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:48.507136
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:50.922183
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:53.338709
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:55.757790
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:18:58.174560
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:00.590697
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:03.012474
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:05.432267
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:07.852197
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:10.272176
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:12.688413
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:15.103773
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:17.525645
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:19.945691
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:22.362149
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:24.777669
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:27.194738
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:29.611491
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:44.934503
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:55.667770
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:19:57.008140
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

# Generated at 2026-10-24 20:19:58.322408
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

# Generated at 2026-10-24 20:19:59.654540
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

# Generated at 2026-10-24 20:20:00.979325
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

# Generated at 2026-10-24 20:20:02.400593
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

# Generated at 2026-10-24 20:20:03.772094
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

# Generated at 2026-10-24 20:20:05.205304
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

# Generated at 2026-10-24 20:20:06.623330
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

# Generated at 2026-10-24 20:20:08.088112
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

# Generated at 2026-10-24 20:20:09.415705
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

# Generated at 2026-10-24 20:20:10.820365
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

# Generated at 2026-10-24 20:20:12.156700
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

# Generated at 2026-10-24 20:20:13.810779
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

# Generated at 2026-10-24 20:20:15.255388
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

# Generated at 2026-10-24 20:20:16.677547
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

# Generated at 2026-10-24 20:20:18.006463
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

# Generated at 2026-10-24 20:20:20.657033
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:23.075363
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:25.493652
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:27.912039
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:30.332372
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:32.746666
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:35.162335
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:37.578335
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:39.994827
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:42.555311
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:44.971450
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:47.552731
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:20:48.924307
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

# Generated at 2026-10-24 20:20:50.363316
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

# Generated at 2026-10-24 20:20:51.703834
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

# Generated at 2026-10-24 20:20:53.024908
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

# Generated at 2026-10-24 20:20:55.186555
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

# Generated at 2026-10-24 20:20:56.514462
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

# Generated at 2026-10-24 20:20:57.836292
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

# Generated at 2026-10-24 20:20:59.157904
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

# Generated at 2026-10-24 20:21:00.605598
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

# Generated at 2026-10-24 20:21:01.926607
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

# Generated at 2026-10-24 20:21:03.339518
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

# Generated at 2026-10-24 20:21:04.665256
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

# Generated at 2026-10-24 20:21:05.984775
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

# Generated at 2026-10-24 20:21:07.312603
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

# Generated at 2026-10-24 20:21:13.751533
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

# Generated at 2026-10-24 20:21:15.118078
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

# Generated at 2026-10-24 20:21:17.641139
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:20.063035
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:22.478818
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:24.903092
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:27.320902
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:29.737978
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:32.156781
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:34.571650
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:36.989446
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:39.409111
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:41.830751
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:44.247810
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:46.663750
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:49.079202
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:51.495789
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:53.916382
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:56.333352
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:21:58.746894
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:01.164930
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:03.579469
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:05.996578
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:08.411194
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:10.828184
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:13.243263
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:24.784689
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:27.201800
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:29.618579
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:32.037080
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:34.452003
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:36.871808
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:39.289204
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:41.705227
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:44.123453
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:46.541115
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:48.958736
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:51.377328
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:53.793485
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:56.209058
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:22:58.625591
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:01.043530
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:03.460945
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:05.874808
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:08.290821
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:10.713063
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:13.129608
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:15.544978
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:17.963108
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:20.382883
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:22.796060
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:25.214071
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:27.632573
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:30.049661
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:32.465883
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:34.881953
# Unit test for function get_sysctl

# Generated at 2026-10-24 20:23:56.762270
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

# Generated at 2026-10-24 20:23:58.098761
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

# Generated at 2026-10-24 20:23:59.428615
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

# Generated at 2026-10-24 20:24:00.800748
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

# Generated at 2026-10-24 20:24:02.160022
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

# Generated at 2026-10-24 20:24:03.495806
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

# Generated at 2026-10-24 20:24:04.812058
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

# Generated at 2026-10-24 20:24:06.460671
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

# Generated at 2026-10-24 20:24:07.786057
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

# Generated at 2026-10-24 20:24:09.224625
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

# Generated at 2026-10-24 20:24:55.334566
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

# Generated at 2026-10-24 20:24:56.684488
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

# Generated at 2026-10-24 20:24:57.999357
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

# Generated at 2026-10-24 20:24:59.335498
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

# Generated at 2026-10-24 20:25:00.732724
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

# Generated at 2026-10-24 20:25:02.167473
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

# Generated at 2026-10-24 20:25:03.534647
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

# Generated at 2026-10-24 20:25:04.931495
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

# Generated at 2026-10-24 20:25:06.270393
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

# Generated at 2026-10-24 20:25:07.598238
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

# Generated at 2026-10-24 20:26:36.172723
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

# Generated at 2026-10-24 20:26:37.503680
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

# Generated at 2026-10-24 20:26:38.820242
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

# Generated at 2026-10-24 20:26:40.148750
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

# Generated at 2026-10-24 20:26:41.463372
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

# Generated at 2026-10-24 20:26:42.785682
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

# Generated at 2026-10-24 20:26:44.102669
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

# Generated at 2026-10-24 20:26:45.419092
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

# Generated at 2026-10-24 20:26:46.823915
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

# Generated at 2026-10-24 20:26:48.149896
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