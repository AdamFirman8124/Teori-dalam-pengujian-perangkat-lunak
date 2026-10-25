

# Generated at 2026-10-24 11:37:21.151508
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:23.571820
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:25.993559
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:28.415419
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 11:37:30.831804
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 11:37:33.248524
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 11:37:35.674237
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:38.098182
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:40.514226
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:42.931847
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:37:45.351329
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:37:47.771342
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:37:50.188861
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:52.612200
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:55.029277
# Unit test for function validate_json

# Generated at 2026-10-24 11:37:57.448832
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:37:59.865987
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:02.289524
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:04.710820
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:07.128480
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:10.109333
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:11.542068
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

# Generated at 2026-10-24 11:38:12.973490
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

# Generated at 2026-10-24 11:38:14.439859
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

# Generated at 2026-10-24 11:38:15.844197
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

# Generated at 2026-10-24 11:38:17.278239
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

# Generated at 2026-10-24 11:38:18.716642
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

# Generated at 2026-10-24 11:38:20.149859
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

# Generated at 2026-10-24 11:38:21.526885
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

# Generated at 2026-10-24 11:38:22.975176
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

# Generated at 2026-10-24 11:38:24.649429
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

# Generated at 2026-10-24 11:38:26.081414
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

# Generated at 2026-10-24 11:38:27.510144
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

# Generated at 2026-10-24 11:38:28.961957
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

# Generated at 2026-10-24 11:38:30.386630
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

# Generated at 2026-10-24 11:38:31.769154
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

# Generated at 2026-10-24 11:38:34.290696
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:36.716184
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:39.273376
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:41.690644
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:44.114923
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:46.543526
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:48.968957
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:51.390272
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:53.812219
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:56.226211
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:38:58.644462
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:01.062131
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:03.481453
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:05.900958
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:08.336157
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:10.752788
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:13.377572
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:16.154851
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:17.536073
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

# Generated at 2026-10-24 11:39:18.918853
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

# Generated at 2026-10-24 11:39:20.353796
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

# Generated at 2026-10-24 11:39:21.786612
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

# Generated at 2026-10-24 11:39:23.228617
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

# Generated at 2026-10-24 11:39:24.653193
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

# Generated at 2026-10-24 11:39:26.098688
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

# Generated at 2026-10-24 11:39:29.058103
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

# Generated at 2026-10-24 11:39:30.506956
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

# Generated at 2026-10-24 11:39:31.879509
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

# Generated at 2026-10-24 11:39:33.264445
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

# Generated at 2026-10-24 11:39:35.692725
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:38.114769
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:40.693850
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:43.113325
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:45.675360
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:48.101820
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:50.513239
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:52.932221
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:55.349358
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:39:57.766587
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:00.184631
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:02.601466
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:05.016914
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:07.431057
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:09.854855
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:12.271948
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:14.694507
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:17.111865
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:22.548552
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:24.968867
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:27.396091
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:29.811189
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:32.227772
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:34.823720
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:40:36.336161
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

# Generated at 2026-10-24 11:40:37.769909
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

# Generated at 2026-10-24 11:40:39.200307
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

# Generated at 2026-10-24 11:40:40.633650
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

# Generated at 2026-10-24 11:40:42.067514
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

# Generated at 2026-10-24 11:40:43.503734
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

# Generated at 2026-10-24 11:40:44.935964
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

# Generated at 2026-10-24 11:40:46.461097
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

# Generated at 2026-10-24 11:40:55.074934
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

# Generated at 2026-10-24 11:40:56.507805
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

# Generated at 2026-10-24 11:40:57.938964
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

# Generated at 2026-10-24 11:40:59.508280
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

# Generated at 2026-10-24 11:41:00.962850
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

# Generated at 2026-10-24 11:41:03.545434
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:06.104994
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:08.524588
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:11.053261
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:13.469600
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:16.094401
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:18.513087
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:20.932934
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:23.349480
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:25.768106
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:28.196672
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:30.616010
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:33.035508
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:35.452210
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:41:37.871334
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:02.831160
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:05.248085
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:07.665591
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:10.089004
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:12.511083
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:14.929927
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:17.346407
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:19.767020
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:22.185863
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:24.600991
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:27.019018
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:29.439967
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:31.855679
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:34.274339
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:36.689744
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:42:38.057288
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

# Generated at 2026-10-24 11:42:41.176735
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

# Generated at 2026-10-24 11:42:42.593568
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

# Generated at 2026-10-24 11:42:43.979919
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

# Generated at 2026-10-24 11:42:45.670826
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

# Generated at 2026-10-24 11:43:21.041142
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:23.460706
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:25.878716
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:28.297559
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:30.715866
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:33.128413
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:35.547993
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:37.966067
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:40.383228
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:42.796148
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:45.212500
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:47.629879
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:50.048111
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:52.464711
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:54.883060
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:57.302147
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:43:59.718475
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:02.136033
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:04.552837
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:07.574057
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:10.236427
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:11.597801
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

# Generated at 2026-10-24 11:44:13.012469
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

# Generated at 2026-10-24 11:44:14.550203
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

# Generated at 2026-10-24 11:44:41.189645
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:43.604265
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:46.147508
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:48.567769
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:51.345623
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:54.105968
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:44:55.490155
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

# Generated at 2026-10-24 11:44:56.943373
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

# Generated at 2026-10-24 11:44:58.376084
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

# Generated at 2026-10-24 11:44:59.813419
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

# Generated at 2026-10-24 11:45:01.346310
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

# Generated at 2026-10-24 11:45:02.783645
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

# Generated at 2026-10-24 11:45:04.433575
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

# Generated at 2026-10-24 11:45:06.957655
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:45:09.377846
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:45:11.799370
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:19.936388
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:22.352939
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:24.769307
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:27.187987
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:29.602813
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:32.090081
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:34.436867
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:36.854576
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:39.269806
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:41.685039
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:44.101096
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:46.518152
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:48.936489
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:51.353835
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:53.768639
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:56.184319
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:46:58.601697
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:01.017592
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:03.436103
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:05.853735
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:08.269858
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:10.689650
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:13.106983
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:15.521821
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:17.940036
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:20.357373
# Unit test for function tokenize_json

# Generated at 2026-10-24 11:47:22.776088
# Unit test for function tokenize_json