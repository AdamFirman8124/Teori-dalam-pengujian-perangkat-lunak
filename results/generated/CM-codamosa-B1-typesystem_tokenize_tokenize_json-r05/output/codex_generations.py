

# Generated at 2026-10-24 10:46:26.494875
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:46:47.715138
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 10:46:50.133807
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 10:46:52.551716
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 10:46:54.966632
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:46:57.580114
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:46:59.999395
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:02.413750
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:04.829456
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:07.249720
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:09.665110
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:12.082462
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:14.499961
# Unit test for function validate_json

# Generated at 2026-10-24 10:47:16.920404
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:19.339627
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:21.758648
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:24.177897
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:26.598814
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:29.020572
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:31.437142
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:33.857940
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:36.288377
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:38.707278
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:41.125866
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:47:43.548602
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:01.577364
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:27.380427
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:29.799920
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:32.382446
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:34.795084
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:37.318198
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:39.734302
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:42.151998
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:44.706385
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:47.126789
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:49.545776
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:51.962847
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:54.384546
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:56.804183
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:48:59.218447
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:01.637699
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:04.055586
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:06.472865
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:08.891370
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:11.306183
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:13.723097
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:16.139568
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:18.557385
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:20.973755
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:23.392956
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:25.811254
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:28.228229
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:30.645043
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:33.061943
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:35.480499
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:37.896203
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:40.313710
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:42.727752
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:45.143788
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:47.584259
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:49.995755
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:52.413204
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:54.834215
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:57.255924
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:49:59.671240
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:02.088821
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:04.507412
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:06.924486
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:09.340545
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:11.760488
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:14.176929
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:16.594954
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:19.014048
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:21.732702
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:24.147954
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:26.563535
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:28.980856
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:31.396716
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:33.816174
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:36.231653
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:38.647728
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:41.075344
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:43.493906
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:45.912628
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:48.329406
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:50:50.747507
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:12.504177
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:15.316511
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:16.821799
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:51:18.281563
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:51:19.655918
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:51:21.054468
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:51:23.473701
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:25.982525
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:28.400323
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:32.065924
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:34.480472
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:37.046114
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:39.575224
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:41.992014
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:44.414388
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:46.833405
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:49.249592
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:51.666653
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:54.082811
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:56.500157
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:51:58.919189
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:01.335101
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:03.750436
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:06.166098
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:08.587823
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:11.001183
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:13.418033
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:15.835521
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:18.254528
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:20.671290
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:23.085065
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:25.504725
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:27.923596
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:30.343471
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:32.759181
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:35.177978
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:37.594369
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:40.007929
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:52:42.425650
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:11.850110
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:53:13.283610
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:53:14.646833
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:53:16.018751
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:53:18.523231
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:20.938567
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:23.357305
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:25.773637
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:28.188055
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:30.607085
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:33.031489
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:35.448602
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:37.867394
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:40.290859
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:42.713603
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:45.131561
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:47.549297
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:49.970869
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:52.390159
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:54.806555
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:57.224541
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:53:59.642818
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:14.958745
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:17.377782
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:19.796894
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:22.216124
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:24.637431
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:27.057382
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:29.474838
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:31.895076
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:34.312221
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:36.730405
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:39.150365
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:41.566664
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:44.022642
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:46.748002
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:49.438187
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:54:50.877071
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:54:52.238334
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:54:53.607949
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:54:54.982277
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:54:56.401949
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:55:26.853601
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:29.273334
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:31.694307
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:34.116004
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:36.532611
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:38.954204
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:41.375709
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:43.797741
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:46.218109
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:48.637416
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:51.055297
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:53.475425
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:55.891015
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:55:58.306204
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:00.726718
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:03.147193
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:05.568294
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:07.987508
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:10.407236
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:12.829181
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:15.251743
# Unit test for function tokenize_json

# Generated at 2026-10-24 10:56:16.787160
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:56:18.219521
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 10:56:19.653415
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar