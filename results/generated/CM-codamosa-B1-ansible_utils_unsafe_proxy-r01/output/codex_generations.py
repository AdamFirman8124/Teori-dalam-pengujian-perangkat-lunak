

# Generated at 2026-10-25 06:35:06.649648
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    # str input -> wrapped as AnsibleUnsafeBytes
    result = module_0.to_unsafe_bytes(u'test string')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'test string'
    assert getattr(result, '__UNSAFE__', False) is True

    # already-bytes input -> still wrapped
    result = module_0.to_unsafe_bytes(b'raw bytes')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'raw bytes'

    # None passes through unchanged
    assert module_0.to_unsafe_bytes(None) is None

    # decode() on the result keeps the unsafe context
    decoded = module_0.to_unsafe_bytes(u'test string').decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'test string'

# Generated at 2026-10-25 06:35:09.069691
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:11.484754
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:13.902380
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:16.317115
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:18.730214
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:21.385409
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:23.799207
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:26.218472
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:28.604744
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 06:35:31.023708
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 06:35:33.442910
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 06:35:35.858371
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 06:35:38.275626
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:40.693531
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:43.107868
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:45.525835
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:47.945616
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:50.363133
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:35:53.118728
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:05.307039
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy


# Generated at 2026-10-25 06:36:16.588732
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 06:36:19.011780
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:21.710862
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:24.287892
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:26.884378
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:29.302180
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:31.719362
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:34.133822
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:36.791986
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:39.210334
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:41.623682
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:44.040656
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:46.457447
# Unit test for function wrap_var

# Generated at 2026-10-25 06:36:48.871541
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:51.289158
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:53.708096
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:56.122580
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:36:58.537449
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:37:00.955687
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 06:37:03.445680
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:05.862093
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:08.276844
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:10.717632
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:13.135332
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:15.553600
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:17.974872
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:20.390431
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:22.805433
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:25.220826
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:27.638496
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:30.051328
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:32.466606
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:34.886169
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:37.296499
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:39.712350
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:42.126083
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:44.539158
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:47.018660
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:49.401292
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:51.814876
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:54.229547
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:56.647820
# Unit test for function wrap_var

# Generated at 2026-10-25 06:37:59.065586
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:01.478929
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:03.897492
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:06.314374
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:08.728861
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:11.144650
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:13.557287
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:15.972837
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:18.390806
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:20.806463
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:23.223715
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:25.637881
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:28.054992
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:30.468548
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:32.888736
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:35.305455
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:37.757214
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:40.177006
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:42.592122
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:45.106601
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:47.523504
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:49.937388
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:52.351105
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:54.766122
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:57.183966
# Unit test for function wrap_var

# Generated at 2026-10-25 06:38:59.599411
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:02.019509
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:04.430849
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:06.845836
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:09.261439
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:11.674529
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:14.088947
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:16.598859
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:19.011586
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:21.426523
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:23.841539
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:26.256662
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:28.671429
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:31.173312
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:33.590971
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:36.006364
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:38.421110
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:40.839942
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:43.255666
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:45.672650
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:48.089815
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:50.504234
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:52.932551
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:55.350436
# Unit test for function wrap_var

# Generated at 2026-10-25 06:39:57.772833
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:00.179974
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:02.595595
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:05.010593
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:07.425463
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:09.843613
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:12.287959
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:14.700670
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:17.118409
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:19.536091
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:21.948868
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:24.366626
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:26.780719
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:29.189915
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:31.606866
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:34.021402
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:36.437902
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:38.857875
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:41.271577
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:43.687547
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:46.104181
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:48.516049
# Unit test for function wrap_var

# Generated at 2026-10-25 06:40:50.929368
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:06.381032
# Unit test for function wrap_var
def test_wrap_var():assert module_0.wrap_var(None) is None

# Generated at 2026-10-25 06:41:27.046134
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:29.460869
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:31.977058
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:34.387918
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:36.802321
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:39.577507
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:41.872928
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:44.281150
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:46.695407
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:49.110409
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:51.525110
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:53.943644
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:56.360920
# Unit test for function wrap_var

# Generated at 2026-10-25 06:41:58.776087
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:01.190984
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:03.652432
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:06.023907
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:08.445948
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:23.264681
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:29.452483
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:42:32.264488
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:33.658443
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:42:36.598428
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:37.988921
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:42:41.114655
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:43.749255
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:46.174747
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:48.588442
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:51.005288
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:53.419378
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:55.836639
# Unit test for function wrap_var

# Generated at 2026-10-25 06:42:58.254187
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:00.824061
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:03.241212
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:05.657203
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:08.106811
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:10.532676
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:12.948644
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:15.365205
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:17.782063
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:20.200170
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:22.615964
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:25.237620
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:26.771961
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:43:29.743099
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:31.167753
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:43:34.044113
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:35.476132
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:43:39.675958
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:41.211066
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:43:43.627317
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:46.100838
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:48.497164
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:50.913856
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:53.425727
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:55.816490
# Unit test for function wrap_var

# Generated at 2026-10-25 06:43:58.235576
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:00.694578
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:03.107042
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:05.523698
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:07.941324
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:10.353974
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:12.766775
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:15.181043
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:17.595387
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:20.010230
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:22.423041
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:24.836703
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:27.254143
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:29.716112
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:32.128029
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:34.546208
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:36.995467
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:39.397124
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:41.811769
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:44.243300
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:46.659493
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:53.916410
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:55.347958
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:44:58.276679
# Unit test for function wrap_var

# Generated at 2026-10-25 06:44:59.752676
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 06:45:02.620433
# Unit test for function wrap_var

# Generated at 2026-10-25 06:45:04.051483
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2