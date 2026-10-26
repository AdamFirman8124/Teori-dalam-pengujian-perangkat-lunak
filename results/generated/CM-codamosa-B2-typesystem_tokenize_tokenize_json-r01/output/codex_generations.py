

# Generated at 2026-10-25 10:19:35.370899
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-25 10:19:37.913046
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-25 10:19:40.327914
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-25 10:19:42.990499
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:19:45.405892
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:19:47.932386
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:19:50.345354
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:19:52.762300
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:19:55.176012
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:20:04.062674
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 10:20:36.203709
# Unit test for function validate_json

# Generated at 2026-10-25 10:20:55.569173
# Unit test for function validate_json
def test_validate_json():from typesystem import String


# Generated at 2026-10-25 10:21:14.410924
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:21:32.331237
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:34.748970
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:37.163507
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:39.577104
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:41.991826
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:44.527116
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:46.941848
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:49.357926
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:51.772694
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:54.186336
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:56.601385
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:21:59.018491
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:22:01.442482
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:22:03.852169
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:22:20.974804
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:22:27.116760
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:22:58.418042
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:23:01.095834
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:03.510374
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:05.922581
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:08.337909
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:10.754187
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:32.346390
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:23:57.433015
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:23:59.848520
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:02.263137
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:04.679447
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:07.303545
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:09.719873
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:12.134604
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:14.548175
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:16.962936
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:19.377576
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:21.791834
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:24.207607
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:26.623330
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:29.037275
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:31.452622
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:33.867001
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:36.282374
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:38.722350
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:24:57.035007
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:25:16.629940
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:25:19.161280
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:21.579347
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:23.994077
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:26.410925
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:28.824254
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:31.237489
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:35.479051
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:37.871894
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:40.286953
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:42.700277
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:25:45.297132
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:12.503037
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:26:36.970471
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:26:39.383241
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:41.799027
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:44.248801
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:46.666360
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:49.080001
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:26:50.472331
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:26:54.789512
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:26:57.658138
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:27:17.728763
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:27:42.100741
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:27:44.522681
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:27:46.934776
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:27:49.350757
# Unit test for function tokenize_json

# Generated at 2026-10-25 10:28:16.307785
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:28:23.981305
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:28:27.165017
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:28:32.480468
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:28:57.167145
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:28:59.923881
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:29:02.997917
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:29:21.162458
# Unit test for function tokenize_json
def test_tokenize_json():import pytest

# Generated at 2026-10-25 10:29:50.409890
# Unit test for function tokenize_json
def test_tokenize_json():import pytest