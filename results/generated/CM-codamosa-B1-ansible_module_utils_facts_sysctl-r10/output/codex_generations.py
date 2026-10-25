

# Generated at 2026-10-24 10:33:12.666922
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

# Generated at 2026-10-24 10:33:29.345879
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

# Generated at 2026-10-24 10:34:24.422515
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:34:43.878434
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:34:46.414138
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:34:47.773713
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:35:05.571533
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:07.021445
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:35:23.506086
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

# Generated at 2026-10-24 10:35:25.927222
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:28.372462
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:30.790415
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:33.373600
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:35.794150
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:38.210003
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:40.628375
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:43.048050
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:45.468633
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:47.886899
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:55.569249
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:35:56.968252
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:36:13.375922
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

# Generated at 2026-10-24 10:36:16.345160
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:36:17.771224
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:36:19.176155
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

# Generated at 2026-10-24 10:36:35.597981
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

# Generated at 2026-10-24 10:36:52.082849
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

# Generated at 2026-10-24 10:37:08.774814
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

# Generated at 2026-10-24 10:37:25.263278
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

# Generated at 2026-10-24 10:37:41.849141
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

# Generated at 2026-10-24 10:37:44.361587
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:46.780895
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:49.215284
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:51.825698
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:54.244308
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:56.663970
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:37:59.084095
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:38:00.485909
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:38:17.177750
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

# Generated at 2026-10-24 10:38:33.665312
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

# Generated at 2026-10-24 10:38:51.466483
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:38:53.884412
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:38:56.463698
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:38:58.880064
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:39:01.465794
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:39:02.953292
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:39:19.438343
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

# Generated at 2026-10-24 10:39:37.215936
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:39:38.595456
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:39:56.284266
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:39:58.702398
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:40:01.123624
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:40:03.542170
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:40:06.103494
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:40:07.422283
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:40:23.893306
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

# Generated at 2026-10-24 10:40:40.538434
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

# Generated at 2026-10-24 10:40:57.232675
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

# Generated at 2026-10-24 10:40:59.656605
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:41:02.075594
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:41:04.497044
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:41:22.350957
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:41:23.661660
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:41:41.504092
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:41:42.826057
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:41:59.593671
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

# Generated at 2026-10-24 10:42:02.016463
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:42:04.434853
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:42:07.003513
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:42:23.453144
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

# Generated at 2026-10-24 10:42:39.837052
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

# Generated at 2026-10-24 10:42:56.632776
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