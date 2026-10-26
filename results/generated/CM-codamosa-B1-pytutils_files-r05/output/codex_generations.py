

# Generated at 2026-10-25 10:29:39.352917
# Unit test for function islurp

# Generated at 2026-10-25 10:29:42.728126
# Unit test for function islurp
def test_islurp():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']
    assert list(module_0.islurp(path, iter_by=4)) == ['alph', 'a\nbe', 'ta\ng', 'amma', '\n']
    assert list(module_0.islurp(path, iter_by=100)) == ['alpha\nbeta\ngamma\n']
    assert list(module_0.islurp(path, expanduser=True, expandvars=True)) == ['alpha\n', 'beta\n', 'gamma\n']

    os.remove(path)

# Generated at 2026-10-25 10:29:45.575438
# Unit test for function islurp

# Generated at 2026-10-25 10:29:47.991926
# Unit test for function islurp

# Generated at 2026-10-25 10:29:50.719933
# Unit test for function islurp

# Generated at 2026-10-25 10:30:16.015098
# Unit test for function islurp

# Generated at 2026-10-25 10:30:32.703474
# Unit test for function islurp
def test_islurp():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']
    assert list(module_0.islurp(path, iter_by=4)) == ['alph', 'a\nbe', 'ta\ng', 'amma', '\n']
    assert list(module_0.islurp(path, iter_by=100)) == ['alpha\nbeta\ngamma\n']
    assert list(module_0.islurp(path, expanduser=True, expandvars=True)) == ['alpha\n', 'beta\n', 'gamma\n']

    os.remove(path)

# Generated at 2026-10-25 10:30:35.116041
# Unit test for function islurp

# Generated at 2026-10-25 10:30:37.531710
# Unit test for function islurp

# Generated at 2026-10-25 10:30:39.946608
# Unit test for function islurp

# Generated at 2026-10-25 10:30:42.364802
# Unit test for function islurp

# Generated at 2026-10-25 10:30:45.093582
# Unit test for function islurp

# Generated at 2026-10-25 10:30:47.641584
# Unit test for function islurp

# Generated at 2026-10-25 10:30:50.192166
# Unit test for function islurp

# Generated at 2026-10-25 10:30:52.605604
# Unit test for function islurp

# Generated at 2026-10-25 10:30:55.026629
# Unit test for function islurp

# Generated at 2026-10-25 10:30:57.441479
# Unit test for function islurp

# Generated at 2026-10-25 10:30:59.855588
# Unit test for function islurp

# Generated at 2026-10-25 10:31:02.272430
# Unit test for function islurp

# Generated at 2026-10-25 10:31:04.687978
# Unit test for function islurp

# Generated at 2026-10-25 10:31:07.106749
# Unit test for function islurp

# Generated at 2026-10-25 10:31:09.523228
# Unit test for function islurp

# Generated at 2026-10-25 10:31:11.999003
# Unit test for function burp

# Generated at 2026-10-25 10:31:14.398110
# Unit test for function burp

# Generated at 2026-10-25 10:31:16.813680
# Unit test for function burp

# Generated at 2026-10-25 10:31:19.242905
# Unit test for function islurp

# Generated at 2026-10-25 10:31:21.651873
# Unit test for function islurp

# Generated at 2026-10-25 10:31:24.068682
# Unit test for function islurp

# Generated at 2026-10-25 10:31:26.488126
# Unit test for function islurp

# Generated at 2026-10-25 10:31:28.905657
# Unit test for function islurp

# Generated at 2026-10-25 10:31:31.327914
# Unit test for function islurp

# Generated at 2026-10-25 10:31:33.746879
# Unit test for function islurp

# Generated at 2026-10-25 10:31:36.166934
# Unit test for function islurp

# Generated at 2026-10-25 10:31:38.584532
# Unit test for function islurp

# Generated at 2026-10-25 10:31:41.075837
# Unit test for function burp

# Generated at 2026-10-25 10:31:42.949532
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 10:32:03.633571
# Unit test for function islurp

# Generated at 2026-10-25 10:32:19.873148
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 10:32:22.282614
# Unit test for function islurp

# Generated at 2026-10-25 10:32:24.697892
# Unit test for function islurp

# Generated at 2026-10-25 10:32:27.396897
# Unit test for function islurp

# Generated at 2026-10-25 10:32:30.018878
# Unit test for function islurp

# Generated at 2026-10-25 10:32:32.430685
# Unit test for function islurp

# Generated at 2026-10-25 10:32:34.848436
# Unit test for function islurp

# Generated at 2026-10-25 10:32:37.261018
# Unit test for function burp

# Generated at 2026-10-25 10:32:39.935419
# Unit test for function burp

# Generated at 2026-10-25 10:32:42.354408
# Unit test for function burp

# Generated at 2026-10-25 10:32:44.769117
# Unit test for function burp

# Generated at 2026-10-25 10:32:47.183575
# Unit test for function burp

# Generated at 2026-10-25 10:32:49.602431
# Unit test for function burp

# Generated at 2026-10-25 10:32:52.016555
# Unit test for function islurp

# Generated at 2026-10-25 10:32:54.436418
# Unit test for function islurp

# Generated at 2026-10-25 10:32:56.852727
# Unit test for function islurp

# Generated at 2026-10-25 10:32:59.271463
# Unit test for function burp

# Generated at 2026-10-25 10:33:01.685380
# Unit test for function burp

# Generated at 2026-10-25 10:33:04.101025
# Unit test for function burp

# Generated at 2026-10-25 10:33:06.519481
# Unit test for function burp

# Generated at 2026-10-25 10:33:08.934787
# Unit test for function burp

# Generated at 2026-10-25 10:33:11.350827
# Unit test for function burp

# Generated at 2026-10-25 10:33:13.765821
# Unit test for function islurp

# Generated at 2026-10-25 10:33:16.181491
# Unit test for function islurp

# Generated at 2026-10-25 10:33:18.595435
# Unit test for function islurp

# Generated at 2026-10-25 10:33:21.013660
# Unit test for function burp

# Generated at 2026-10-25 10:33:23.430835
# Unit test for function burp

# Generated at 2026-10-25 10:33:25.844692
# Unit test for function burp

# Generated at 2026-10-25 10:33:28.313656
# Unit test for function islurp

# Generated at 2026-10-25 10:33:30.728165
# Unit test for function islurp

# Generated at 2026-10-25 10:33:33.141727
# Unit test for function islurp

# Generated at 2026-10-25 10:33:35.556471
# Unit test for function burp

# Generated at 2026-10-25 10:33:37.970730
# Unit test for function burp

# Generated at 2026-10-25 10:33:40.385230
# Unit test for function burp

# Generated at 2026-10-25 10:33:42.799447
# Unit test for function islurp

# Generated at 2026-10-25 10:33:45.215009
# Unit test for function islurp

# Generated at 2026-10-25 10:33:47.633887
# Unit test for function islurp

# Generated at 2026-10-25 10:33:50.050601
# Unit test for function islurp

# Generated at 2026-10-25 10:33:52.463408
# Unit test for function islurp

# Generated at 2026-10-25 10:33:54.877487
# Unit test for function islurp

# Generated at 2026-10-25 10:33:57.292084
# Unit test for function burp

# Generated at 2026-10-25 10:33:59.708969
# Unit test for function burp

# Generated at 2026-10-25 10:34:02.127248
# Unit test for function burp

# Generated at 2026-10-25 10:34:04.540972
# Unit test for function islurp

# Generated at 2026-10-25 10:34:07.003732
# Unit test for function islurp

# Generated at 2026-10-25 10:34:09.397215
# Unit test for function islurp

# Generated at 2026-10-25 10:34:11.814141
# Unit test for function burp

# Generated at 2026-10-25 10:34:14.229444
# Unit test for function burp

# Generated at 2026-10-25 10:34:16.688697
# Unit test for function burp

# Generated at 2026-10-25 10:34:19.103913
# Unit test for function islurp

# Generated at 2026-10-25 10:34:21.518859
# Unit test for function islurp

# Generated at 2026-10-25 10:34:23.934576
# Unit test for function islurp

# Generated at 2026-10-25 10:34:26.354002
# Unit test for function burp

# Generated at 2026-10-25 10:34:28.772526
# Unit test for function burp

# Generated at 2026-10-25 10:34:31.213497
# Unit test for function burp

# Generated at 2026-10-25 10:34:33.629669
# Unit test for function islurp

# Generated at 2026-10-25 10:34:36.044339
# Unit test for function islurp

# Generated at 2026-10-25 10:34:38.463480
# Unit test for function islurp

# Generated at 2026-10-25 10:34:40.880138
# Unit test for function islurp

# Generated at 2026-10-25 10:34:43.294812
# Unit test for function islurp

# Generated at 2026-10-25 10:34:45.710316
# Unit test for function islurp

# Generated at 2026-10-25 10:34:48.127425
# Unit test for function islurp

# Generated at 2026-10-25 10:34:50.542132
# Unit test for function islurp

# Generated at 2026-10-25 10:34:52.955515
# Unit test for function islurp

# Generated at 2026-10-25 10:34:55.369345
# Unit test for function islurp

# Generated at 2026-10-25 10:34:57.786165
# Unit test for function islurp

# Generated at 2026-10-25 10:35:00.201354
# Unit test for function islurp

# Generated at 2026-10-25 10:35:02.616223
# Unit test for function islurp

# Generated at 2026-10-25 10:35:05.030269
# Unit test for function islurp

# Generated at 2026-10-25 10:35:07.445422
# Unit test for function islurp

# Generated at 2026-10-25 10:35:09.863186
# Unit test for function islurp

# Generated at 2026-10-25 10:35:12.280424
# Unit test for function islurp

# Generated at 2026-10-25 10:35:14.691282
# Unit test for function islurp

# Generated at 2026-10-25 10:35:17.105266
# Unit test for function islurp

# Generated at 2026-10-25 10:35:19.518472
# Unit test for function islurp

# Generated at 2026-10-25 10:35:21.932638
# Unit test for function islurp

# Generated at 2026-10-25 10:35:24.354099
# Unit test for function islurp

# Generated at 2026-10-25 10:35:26.767986
# Unit test for function islurp

# Generated at 2026-10-25 10:35:29.184751
# Unit test for function islurp

# Generated at 2026-10-25 10:35:31.598066
# Unit test for function islurp

# Generated at 2026-10-25 10:35:34.009331
# Unit test for function islurp

# Generated at 2026-10-25 10:35:36.424755
# Unit test for function islurp

# Generated at 2026-10-25 10:35:38.840709
# Unit test for function burp

# Generated at 2026-10-25 10:35:41.253172
# Unit test for function burp

# Generated at 2026-10-25 10:35:43.667665
# Unit test for function burp

# Generated at 2026-10-25 10:35:46.081681
# Unit test for function burp

# Generated at 2026-10-25 10:35:48.495016
# Unit test for function burp

# Generated at 2026-10-25 10:35:50.909684
# Unit test for function burp

# Generated at 2026-10-25 10:35:53.324139
# Unit test for function islurp

# Generated at 2026-10-25 10:35:55.741539
# Unit test for function islurp

# Generated at 2026-10-25 10:35:58.158897
# Unit test for function islurp

# Generated at 2026-10-25 10:36:00.572691
# Unit test for function burp

# Generated at 2026-10-25 10:36:02.989192
# Unit test for function burp

# Generated at 2026-10-25 10:36:05.404539
# Unit test for function burp

# Generated at 2026-10-25 10:36:07.819607
# Unit test for function islurp

# Generated at 2026-10-25 10:36:10.235454
# Unit test for function islurp

# Generated at 2026-10-25 10:36:12.656704
# Unit test for function islurp

# Generated at 2026-10-25 10:36:15.077815
# Unit test for function islurp

# Generated at 2026-10-25 10:36:17.492612
# Unit test for function islurp

# Generated at 2026-10-25 10:36:37.096003
# Unit test for function islurp
def test_islurp():import tempfile


# Generated at 2026-10-25 10:36:55.243035
# Unit test for function islurp

# Generated at 2026-10-25 10:36:57.911127
# Unit test for function islurp

# Generated at 2026-10-25 10:37:00.364659
# Unit test for function islurp

# Generated at 2026-10-25 10:37:02.743908
# Unit test for function islurp

# Generated at 2026-10-25 10:37:05.313170
# Unit test for function islurp

# Generated at 2026-10-25 10:37:07.727165
# Unit test for function islurp

# Generated at 2026-10-25 10:37:10.142027
# Unit test for function burp

# Generated at 2026-10-25 10:37:12.556231
# Unit test for function burp

# Generated at 2026-10-25 10:37:14.973908
# Unit test for function burp

# Generated at 2026-10-25 10:37:17.390026
# Unit test for function islurp

# Generated at 2026-10-25 10:37:19.802249
# Unit test for function islurp

# Generated at 2026-10-25 10:37:22.217127
# Unit test for function islurp

# Generated at 2026-10-25 10:37:57.223311
# Unit test for function islurp

# Generated at 2026-10-25 10:38:13.699516
# Unit test for function islurp
def test_islurp():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']
    assert list(module_0.islurp(path, iter_by=4)) == ['alph', 'a\nbe', 'ta\ng', 'amma', '\n']
    assert list(module_0.islurp(path, iter_by=100)) == ['alpha\nbeta\ngamma\n']
    assert list(module_0.islurp(path, expanduser=True, expandvars=True)) == ['alpha\n', 'beta\n', 'gamma\n']

    os.remove(path)

# Generated at 2026-10-25 10:38:16.349284
# Unit test for function islurp

# Generated at 2026-10-25 10:38:18.960193
# Unit test for function islurp

# Generated at 2026-10-25 10:38:21.594063
# Unit test for function islurp

# Generated at 2026-10-25 10:38:24.011177
# Unit test for function islurp

# Generated at 2026-10-25 10:38:40.585685
# Unit test for function islurp
def test_islurp():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']
    assert list(module_0.islurp(path, iter_by=4)) == ['alph', 'a\nbe', 'ta\ng', 'amma', '\n']
    assert list(module_0.islurp(path, iter_by=100)) == ['alpha\nbeta\ngamma\n']
    assert list(module_0.islurp(path, expanduser=True, expandvars=True)) == ['alpha\n', 'beta\n', 'gamma\n']

    os.remove(path)

# Generated at 2026-10-25 10:38:58.215973
# Unit test for function burp

# Generated at 2026-10-25 10:39:00.632975
# Unit test for function burp

# Generated at 2026-10-25 10:39:03.061633
# Unit test for function burp

# Generated at 2026-10-25 10:39:05.809367
# Unit test for function islurp

# Generated at 2026-10-25 10:39:08.223278
# Unit test for function islurp

# Generated at 2026-10-25 10:39:10.635634
# Unit test for function islurp

# Generated at 2026-10-25 10:39:13.301927
# Unit test for function islurp

# Generated at 2026-10-25 10:39:15.716778
# Unit test for function islurp

# Generated at 2026-10-25 10:39:18.164887
# Unit test for function islurp

# Generated at 2026-10-25 10:39:20.546782
# Unit test for function islurp

# Generated at 2026-10-25 10:39:22.961584
# Unit test for function islurp

# Generated at 2026-10-25 10:39:25.377694
# Unit test for function islurp