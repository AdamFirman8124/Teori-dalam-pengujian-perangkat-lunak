

# Generated at 2026-10-24 13:58:11.465244
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

# Generated at 2026-10-24 13:58:14.070061
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:16.575610
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:18.994394
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:21.407313
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:23.820824
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:26.403167
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:28.819893
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:31.628115
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:34.042118
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:36.456843
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:38.868209
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:53.746219
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:58:55.072900
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

# Generated at 2026-10-24 13:58:56.508289
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

# Generated at 2026-10-24 13:58:57.857284
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

# Generated at 2026-10-24 13:58:59.281654
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

# Generated at 2026-10-24 13:59:01.695931
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:04.211998
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:06.626563
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:09.136812
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:11.552520
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:13.972488
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:16.386912
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:18.803118
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:21.216445
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:23.626912
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:26.040217
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:28.454235
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:30.866220
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:33.280150
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:35.693720
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:38.108646
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:40.521098
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:42.935903
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:45.349036
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:47.765867
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:50.178269
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:52.591796
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:55.004094
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:57.417435
# Unit test for function get_sysctl

# Generated at 2026-10-24 13:59:59.830557
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:02.242678
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:03.719620
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:05.077605
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

# Generated at 2026-10-24 14:00:06.403703
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

# Generated at 2026-10-24 14:00:07.717269
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

# Generated at 2026-10-24 14:00:09.048416
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

# Generated at 2026-10-24 14:00:10.383355
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

# Generated at 2026-10-24 14:00:11.773094
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

# Generated at 2026-10-24 14:00:13.092252
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

# Generated at 2026-10-24 14:00:14.431938
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

# Generated at 2026-10-24 14:00:15.750516
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

# Generated at 2026-10-24 14:00:17.063064
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

# Generated at 2026-10-24 14:00:18.381639
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

# Generated at 2026-10-24 14:00:19.798620
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

# Generated at 2026-10-24 14:00:21.123414
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

# Generated at 2026-10-24 14:00:22.447432
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

# Generated at 2026-10-24 14:00:23.855634
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

# Generated at 2026-10-24 14:00:26.269561
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:28.682725
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:31.096630
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:33.509524
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:35.955980
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:38.586223
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:40.999116
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:43.411405
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:45.823866
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:48.236554
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:50.649148
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:53.221607
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:55.635644
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:00:58.049554
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:00.462121
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:02.877344
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:05.291190
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:07.703086
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:10.550586
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:11.986225
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:13.405415
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:14.783647
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

# Generated at 2026-10-24 14:01:16.103944
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

# Generated at 2026-10-24 14:01:17.422595
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

# Generated at 2026-10-24 14:01:18.805875
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

# Generated at 2026-10-24 14:01:20.279379
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

# Generated at 2026-10-24 14:01:22.804952
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

# Generated at 2026-10-24 14:01:24.382955
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

# Generated at 2026-10-24 14:01:25.704698
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

# Generated at 2026-10-24 14:01:27.067706
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

# Generated at 2026-10-24 14:01:28.432243
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

# Generated at 2026-10-24 14:01:30.009664
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

# Generated at 2026-10-24 14:01:31.321003
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

# Generated at 2026-10-24 14:01:32.624926
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

# Generated at 2026-10-24 14:01:34.000528
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

# Generated at 2026-10-24 14:01:35.319964
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

# Generated at 2026-10-24 14:01:41.379022
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:43.949904
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:46.368764
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:48.883157
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:51.298957
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:53.711888
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:56.126177
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:01:58.696487
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:01.107675
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:03.521194
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:05.932819
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:08.344018
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:10.757507
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:13.173413
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:15.582030
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:17.993427
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:20.407353
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:22.823470
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:25.233775
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:27.645913
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:30.058479
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:32.470630
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:34.885338
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:37.300054
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:39.710343
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:42.121829
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:44.537936
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:46.948542
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:49.370851
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:02:51.788605
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:02.679714
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

# Generated at 2026-10-24 14:03:04.117253
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

# Generated at 2026-10-24 14:03:05.548941
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

# Generated at 2026-10-24 14:03:07.158756
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

# Generated at 2026-10-24 14:03:08.483604
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

# Generated at 2026-10-24 14:03:10.155331
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

# Generated at 2026-10-24 14:03:11.898606
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

# Generated at 2026-10-24 14:03:13.328886
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

# Generated at 2026-10-24 14:03:14.762649
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

# Generated at 2026-10-24 14:03:16.195659
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

# Generated at 2026-10-24 14:03:35.928360
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:38.468701
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:40.882755
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:43.296906
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:45.721159
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:48.274486
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:50.809031
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:53.222412
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:55.640672
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:03:58.214840
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:00.629902
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:03.042313
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:05.458480
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:07.875467
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:10.289873
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:12.706677
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:15.118733
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:17.537283
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:19.964219
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:22.394772
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:24.812936
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:27.227073
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:29.640566
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:32.053842
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:34.466413
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:36.879885
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:39.292137
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:41.703440
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:44.117246
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:04:46.535621
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:20.739818
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:23.150944
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:25.567722
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:27.987274
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:30.398072
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:32.815392
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:35.233394
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:37.649425
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:40.063945
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:42.476750
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:44.890036
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:47.304531
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:49.717254
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:52.131519
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:54.545475
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:56.964542
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:05:59.372695
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:06:01.786128
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:06:04.199993
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:06:19.391772
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:06:20.823040
# Unit test for function get_sysctl

# Generated at 2026-10-24 14:06:22.152261
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

# Generated at 2026-10-24 14:06:23.472459
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

# Generated at 2026-10-24 14:06:24.794233
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

# Generated at 2026-10-24 14:07:44.082090
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

# Generated at 2026-10-24 14:07:45.398587
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

# Generated at 2026-10-24 14:07:46.850279
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

# Generated at 2026-10-24 14:07:48.220317
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

# Generated at 2026-10-24 14:07:49.555350
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

# Generated at 2026-10-24 14:07:50.887481
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

# Generated at 2026-10-24 14:07:52.382640
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

# Generated at 2026-10-24 14:07:53.712974
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

# Generated at 2026-10-24 14:07:55.138337
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

# Generated at 2026-10-24 14:07:56.450865
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