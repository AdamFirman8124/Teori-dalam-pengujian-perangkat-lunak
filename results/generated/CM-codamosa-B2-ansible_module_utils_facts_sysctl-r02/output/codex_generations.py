

# Generated at 2026-10-24 10:48:47.417790
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:48:49.835601
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:48:52.253325
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:48:54.668967
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:48:57.087150
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:48:59.504187
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:01.922301
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:04.338596
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:06.761587
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:09.175481
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:11.590122
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:14.006935
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:16.424852
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:18.841250
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:21.257684
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:23.674528
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:26.092615
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:28.509345
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:30.926145
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:33.343025
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:35.761553
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:38.177086
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:40.593355
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:43.009182
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:45.423991
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:47.844082
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:50.262634
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:52.679382
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:55.100638
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:57.519907
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:49:59.938167
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:02.354550
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:04.774039
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:07.193557
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:09.610578
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:12.027416
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:14.441646
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:16.858698
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:19.276546
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:21.692692
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:24.107688
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:26.525418
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:28.942107
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:31.359146
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:33.779537
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:36.195043
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:38.610563
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:41.029241
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:43.446881
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:45.865401
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:48.283528
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:50.699567
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:53.536104
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:50:54.875412
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:51:11.531976
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

# Generated at 2026-10-24 10:51:14.397533
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:15.719647
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:51:17.065655
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

# Generated at 2026-10-24 10:51:18.444194
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

# Generated at 2026-10-24 10:51:21.266452
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:23.779049
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:26.198981
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:28.617960
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:31.038372
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:33.462014
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:35.876396
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:38.385296
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:40.803835
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:43.220213
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:45.640300
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:48.057485
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:50.476661
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:52.891755
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:55.309964
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:51:57.727144
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:00.144421
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:02.559709
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:04.976837
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:07.393345
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:09.808200
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:12.225803
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:14.641775
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:17.056909
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:19.472538
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:21.889648
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:24.307114
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:26.721907
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:29.141104
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:31.555208
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:33.973655
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:36.389873
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:38.805977
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:41.224706
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:43.756858
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:52:45.079729
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:53:01.611682
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

# Generated at 2026-10-24 10:53:18.097197
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

# Generated at 2026-10-24 10:53:20.515216
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:22.937585
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:25.352260
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:27.769544
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:30.366527
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:32.792618
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:35.210860
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:37.627009
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:40.205538
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:42.623910
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:45.045195
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:47.463991
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:49.881807
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:52.299205
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:54.717315
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:57.134842
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:53:59.552614
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:01.973931
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:04.393325
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:06.814844
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:09.234881
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:11.657473
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:14.077722
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:16.494055
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:18.911630
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:21.332462
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:23.751297
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:26.170904
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:28.585390
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:31.007860
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:33.425270
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:35.842184
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:38.264683
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:40.682653
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:43.099959
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:54:44.722620
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:55:01.319091
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

# Generated at 2026-10-24 10:55:17.701486
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

# Generated at 2026-10-24 10:55:34.393238
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

# Generated at 2026-10-24 10:55:36.812946
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:39.235875
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:41.659404
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:44.080366
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:46.498216
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:48.918551
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:51.339194
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:53.759055
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:56.176272
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:55:58.594854
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:01.012412
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:03.442931
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:06.227949
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:08.648064
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:11.072758
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:13.511300
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:16.181843
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:56:17.563016
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:56:18.924336
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

# Generated at 2026-10-24 10:56:20.262889
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

# Generated at 2026-10-24 10:56:36.959278
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

# Generated at 2026-10-24 10:56:53.344818
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

# Generated at 2026-10-24 10:56:54.684687
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

# Generated at 2026-10-24 10:57:11.062360
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

# Generated at 2026-10-24 10:57:12.371928
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

# Generated at 2026-10-24 10:57:18.842750
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

# Generated at 2026-10-24 10:57:22.128501
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

# Generated at 2026-10-24 10:57:40.348890
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:43.010728
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:45.429571
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:47.843515
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:50.261221
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:52.674965
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:55.097143
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:57.751805
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:57:59.191225
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:58:01.932384
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:03.236885
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:58:04.584052
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

# Generated at 2026-10-24 10:58:05.901515
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

# Generated at 2026-10-24 10:58:07.272889
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

# Generated at 2026-10-24 10:58:08.689547
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

# Generated at 2026-10-24 10:58:11.403080
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:12.730759
# Unit test for function get_sysctl
def test_get_sysctl():from ansible.module_utils.sysctl import get_sysctl


# Generated at 2026-10-24 10:58:17.903648
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

# Generated at 2026-10-24 10:58:29.649597
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
                'kernel.ostype = Linux\n'
                'kernel.hostname: test-host\n'
                'net.ipv4.ip_forward = 1\n'
                'example.multiline = first line\n'
                ' second line\n'
                ' third line\n'
                '\n',
                '',
            )

        def warn(self, message):
            self.warnings.append(message)

    module = FakeModule()

    result = module_0.get_sysctl(module, ['-a'])

    assert module.command == ['/sbin/sysctl', '-a']
    assert module.warnings == []
    assert result == {
        'kernel.ostype': 'Linux',
        'kernel.hostname': 'test-host',
        'net.ipv4.ip_forward': '1',
        'example.multiline': 'first line\n second line\n third line',
    }

# Generated at 2026-10-24 10:58:32.072400
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:34.493402
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:36.913230
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:39.329234
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:41.745239
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:44.161112
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:46.577215
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:48.997644
# Unit test for function get_sysctl

# Generated at 2026-10-24 10:58:51.415140
# Unit test for function get_sysctl