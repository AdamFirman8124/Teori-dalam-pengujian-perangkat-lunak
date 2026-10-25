

# Generated at 2026-10-24 13:12:51.615634
# Unit test for function validate_json

# Generated at 2026-10-24 13:13:29.890648
# Unit test for function validate_json

# Generated at 2026-10-24 13:13:32.757608
# Unit test for function validate_json

# Generated at 2026-10-24 13:14:12.284925
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 13:14:49.149974
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 13:14:51.901309
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 13:14:54.781417
# Unit test for function validate_json

# Generated at 2026-10-24 13:15:12.702485
# Unit test for function validate_json

# Generated at 2026-10-24 13:15:55.070992
# Unit test for function validate_json

# Generated at 2026-10-24 13:16:03.207401
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

# Generated at 2026-10-24 13:16:04.628286
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

# Generated at 2026-10-24 13:16:22.333637
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

# Generated at 2026-10-24 13:16:33.293786
# Unit test for function tokenize_json
def test_tokenize_json():
    # Valid string value.
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert token.start == 0
    assert token.end == 6
    assert token.content == '"hello"'

    # Bytes input is supported.
    token = module_0.tokenize_json(b"42")
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert token.start == 0
    assert token.end == 1

    # Empty content produces a position-aware error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   ")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Malformed JSON produces a parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1

# Generated at 2026-10-24 13:16:34.826596
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

# Generated at 2026-10-24 13:16:36.259579
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

# Generated at 2026-10-24 13:16:37.693241
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

# Generated at 2026-10-24 13:16:39.126840
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

# Generated at 2026-10-24 13:16:40.560875
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

# Generated at 2026-10-24 13:16:41.996895
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

# Generated at 2026-10-24 13:16:44.412783
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:16:46.826296
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:09.849184
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json("true")

# Generated at 2026-10-24 13:17:11.385150
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

# Generated at 2026-10-24 13:17:12.765891
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

# Generated at 2026-10-24 13:17:14.250402
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

# Generated at 2026-10-24 13:17:15.788379
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

# Generated at 2026-10-24 13:17:17.223393
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

# Generated at 2026-10-24 13:17:18.858623
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

# Generated at 2026-10-24 13:17:21.392215
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:23.839030
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:26.221681
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:28.830463
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:31.242566
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:33.657083
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:36.070067
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:38.484664
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:40.898244
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:43.313433
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:45.727066
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:48.140847
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:50.555181
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:52.973822
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:55.399052
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:17:57.810308
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:00.225870
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:02.639307
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:05.308720
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:23.367957
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:32.178775
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"name": "Alice", "active": true}')

# Generated at 2026-10-24 13:18:33.612467
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

# Generated at 2026-10-24 13:18:36.034700
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:38.459704
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:41.017369
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:43.579480
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:45.993980
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:48.563119
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:50.978827
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:53.395083
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:55.814810
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:18:58.235086
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:00.655171
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:03.071955
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:05.486393
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:07.901649
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:10.316154
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:12.731660
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:15.144873
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:17.559079
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:19.977480
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:22.388020
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:24.801845
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:27.477372
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:29.891613
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:32.305186
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:34.718924
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:37.134294
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:39.547341
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:41.961042
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:44.374866
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:46.789481
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:49.202142
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:51.614943
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:54.028398
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:56.442231
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:19:58.855714
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:01.269486
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:03.681609
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:06.095072
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:08.507869
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:10.920600
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:13.333877
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:15.748126
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:18.161382
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:20.576082
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:22.989409
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:25.403174
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:27.817299
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:30.231470
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:32.645686
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:35.058592
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:37.472226
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:42.505347
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:44.918474
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:47.339914
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:49.754665
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:52.170197
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:54.584883
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:56.998445
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:20:59.412957
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:01.826788
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:04.241702
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:06.658724
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:09.071289
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:11.485124
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:13.901939
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:16.313572
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:18.727885
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:21.140976
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:23.554831
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:25.969727
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:28.384182
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:30.810573
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:33.226756
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:35.646157
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:38.063157
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:40.481138
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:42.899626
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:45.314258
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:47.734915
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:50.150883
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:52.567833
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:57.045770
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:21:59.456472
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:01.869562
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:04.282112
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:06.695459
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:09.111829
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:11.521721
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:13.935224
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:16.348980
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:18.763029
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:21.177398
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:23.591353
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:26.005521
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:28.419536
# Unit test for function tokenize_json

# Generated at 2026-10-24 13:22:30.833656
# Unit test for function tokenize_json