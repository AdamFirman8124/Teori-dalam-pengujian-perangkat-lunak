

# Generated at 2026-10-24 04:35:46.249451
# Unit test for function test

# Generated at 2026-10-24 04:35:48.663699
# Unit test for function test

# Generated at 2026-10-24 04:35:51.075682
# Unit test for function test

# Generated at 2026-10-24 04:35:53.486766
# Unit test for function escape

# Generated at 2026-10-24 04:35:55.899192
# Unit test for function escape

# Generated at 2026-10-24 04:35:58.310644
# Unit test for function escape

# Generated at 2026-10-24 04:36:00.722233
# Unit test for function evalString

# Generated at 2026-10-24 04:36:03.134690
# Unit test for function evalString

# Generated at 2026-10-24 04:36:05.831433
# Unit test for function evalString

# Generated at 2026-10-24 04:36:08.242329
# Unit test for function escape

# Generated at 2026-10-24 04:36:10.654490
# Unit test for function escape

# Generated at 2026-10-24 04:36:13.065809
# Unit test for function escape

# Generated at 2026-10-24 04:36:15.477275
# Unit test for function escape

# Generated at 2026-10-24 04:36:17.889395
# Unit test for function escape

# Generated at 2026-10-24 04:36:20.302520
# Unit test for function escape

# Generated at 2026-10-24 04:36:22.714257
# Unit test for function evalString

# Generated at 2026-10-24 04:36:25.135947
# Unit test for function evalString

# Generated at 2026-10-24 04:36:27.537241
# Unit test for function evalString

# Generated at 2026-10-24 04:36:29.949708
# Unit test for function escape

# Generated at 2026-10-24 04:36:32.361688
# Unit test for function escape

# Generated at 2026-10-24 04:36:34.773137
# Unit test for function escape

# Generated at 2026-10-24 04:36:37.183498
# Unit test for function escape

# Generated at 2026-10-24 04:36:39.595553
# Unit test for function escape

# Generated at 2026-10-24 04:36:42.007457
# Unit test for function escape

# Generated at 2026-10-24 04:36:59.783976
# Unit test for function escape

# Generated at 2026-10-24 04:37:15.066621
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:37:23.230603
# Unit test for function test

# Generated at 2026-10-24 04:37:25.644070
# Unit test for function test

# Generated at 2026-10-24 04:37:28.055867
# Unit test for function test

# Generated at 2026-10-24 04:37:30.469278
# Unit test for function escape

# Generated at 2026-10-24 04:37:32.880278
# Unit test for function escape

# Generated at 2026-10-24 04:37:35.294055
# Unit test for function escape

# Generated at 2026-10-24 04:37:37.708408
# Unit test for function escape

# Generated at 2026-10-24 04:37:44.873614
# Unit test for function escape
def test_escape():assert module_0.escape(re.fullmatch(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-24 04:37:57.024418
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def match_escape(value: Text) -> Match[Text]:
        match = re.fullmatch(r"\\(.*)", value)
        assert match is not None
        return match

    # Simple named and punctuation escapes.
    for tail, expected in simple_escapes.items():
        assert module_0.escape(match_escape("\\" + tail)) == expected

    # Hexadecimal escapes.
    assert module_0.escape(match_escape(r"\x00")) == "\x00"
    assert module_0.escape(match_escape(r"\x41")) == "A"
    assert module_0.escape(match_escape(r"\xff")) == "\xff"

    # Octal escapes.
    assert module_0.escape(match_escape(r"\0")) == "\0"
    assert module_0.escape(match_escape(r"\101")) == "A"
    assert module_0.escape(match_escape(r"\377")) == "\xff"

    # Invalid hexadecimal and octal escapes.
    for value in (r"\x", r"\x1", r"\xGG", r"\8", r"\invalid"):
        with pytest.raises(ValueError):
            module_0.escape(match_escape(value))

# Generated at 2026-10-24 04:38:07.274215
# Unit test for function escape

# Generated at 2026-10-24 04:38:08.616760
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:38:20.574970
# Unit test for function evalString

# Generated at 2026-10-24 04:38:22.989107
# Unit test for function evalString

# Generated at 2026-10-24 04:38:25.400476
# Unit test for function evalString

# Generated at 2026-10-24 04:38:27.815551
# Unit test for function evalString

# Generated at 2026-10-24 04:38:30.390723
# Unit test for function evalString

# Generated at 2026-10-24 04:38:32.803444
# Unit test for function evalString

# Generated at 2026-10-24 04:38:35.220201
# Unit test for function escape

# Generated at 2026-10-24 04:38:37.631610
# Unit test for function escape

# Generated at 2026-10-24 04:38:40.047643
# Unit test for function escape

# Generated at 2026-10-24 04:38:55.268067
# Unit test for function escape

# Generated at 2026-10-24 04:38:56.721034
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:39:06.897765
# Unit test for function escape

# Generated at 2026-10-24 04:39:08.395367
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:39:19.543242
# Unit test for function escape

# Generated at 2026-10-24 04:39:22.046440
# Unit test for function escape

# Generated at 2026-10-24 04:39:24.545607
# Unit test for function escape

# Generated at 2026-10-24 04:39:26.957467
# Unit test for function escape

# Generated at 2026-10-24 04:39:29.367857
# Unit test for function escape

# Generated at 2026-10-24 04:39:31.779427
# Unit test for function escape

# Generated at 2026-10-24 04:39:34.191195
# Unit test for function escape

# Generated at 2026-10-24 04:39:36.734930
# Unit test for function escape

# Generated at 2026-10-24 04:39:39.149645
# Unit test for function escape

# Generated at 2026-10-24 04:39:41.568530
# Unit test for function test

# Generated at 2026-10-24 04:39:49.918186
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:40:07.888016
# Unit test for function escape

# Generated at 2026-10-24 04:40:09.267672
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:40:20.895349
# Unit test for function escape

# Generated at 2026-10-24 04:40:22.310425
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:40:35.231726
# Unit test for function evalString

# Generated at 2026-10-24 04:40:37.645071
# Unit test for function evalString

# Generated at 2026-10-24 04:40:40.057184
# Unit test for function evalString

# Generated at 2026-10-24 04:40:42.468114
# Unit test for function evalString

# Generated at 2026-10-24 04:40:49.362033
# Unit test for function evalString
def test_evalString():assert module_0.evalString(r"'hello\n\x57\157rld'") == "hello\nWorld"

# Generated at 2026-10-24 04:41:01.038915
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def match_escape(value: Text) -> Match[Text]:
        match = re.fullmatch(r"\\(.*)", value, flags=re.DOTALL)
        assert match is not None
        return match

    for tail, expected in simple_escapes.items():
        assert module_0.escape(match_escape("\\" + tail)) == expected

    assert module_0.escape(match_escape(r"\x00")) == "\x00"
    assert module_0.escape(match_escape(r"\x41")) == "A"
    assert module_0.escape(match_escape(r"\xff")) == "\xff"

    assert module_0.escape(match_escape(r"\0")) == "\0"
    assert module_0.escape(match_escape(r"\7")) == "\7"
    assert module_0.escape(match_escape(r"\101")) == "A"
    assert module_0.escape(match_escape(r"\377")) == "\xff"

    for invalid in (r"\x", r"\x1", r"\xGG", "\\", r"\8", r"\z"):
        with pytest.raises(ValueError):
            module_0.escape(match_escape(invalid))

# Generated at 2026-10-24 04:41:13.224410
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def make_match(tail: Text) -> Match[Text]:
        match = re.fullmatch(r"\\(.*)", "\\" + tail)
        assert match is not None
        return match

    for tail, expected in simple_escapes.items():
        assert module_0.escape(make_match(tail)) == expected

    assert module_0.escape(make_match("x00")) == "\x00"
    assert module_0.escape(make_match("x41")) == "A"
    assert module_0.escape(make_match("xFF")) == "\xff"

    assert module_0.escape(make_match("0")) == "\0"
    assert module_0.escape(make_match("12")) == "\n"
    assert module_0.escape(make_match("101")) == "A"
    assert module_0.escape(make_match("377")) == "\xff"

    for tail in ("x", "x1", "xGG"):
        with pytest.raises(ValueError) as exc_info:
            module_0.escape(make_match(tail))
        assert str(exc_info.value) == (
            "invalid hex string module_0.escape('\\%s')" % tail
        )

    for tail in ("8", "9", "xyz"):
        with pytest.raises(ValueError) as exc_info:
            module_0.escape(make_match(tail))
        assert str(exc_info.value) == (
            "invalid octal string module_0.escape('\\%s')" % tail
        )

# Generated at 2026-10-24 04:41:27.762323
# Unit test for function escape

# Generated at 2026-10-24 04:41:30.173962
# Unit test for function escape

# Generated at 2026-10-24 04:41:32.586624
# Unit test for function escape

# Generated at 2026-10-24 04:41:34.997177
# Unit test for function escape

# Generated at 2026-10-24 04:41:37.408568
# Unit test for function escape

# Generated at 2026-10-24 04:41:39.820725
# Unit test for function escape

# Generated at 2026-10-24 04:41:42.231863
# Unit test for function evalString

# Generated at 2026-10-24 04:41:44.643591
# Unit test for function evalString

# Generated at 2026-10-24 04:41:47.061820
# Unit test for function evalString

# Generated at 2026-10-24 04:41:49.473255
# Unit test for function escape

# Generated at 2026-10-24 04:41:51.889595
# Unit test for function escape

# Generated at 2026-10-24 04:41:54.299788
# Unit test for function escape

# Generated at 2026-10-24 04:41:56.710368
# Unit test for function test

# Generated at 2026-10-24 04:41:59.123043
# Unit test for function test

# Generated at 2026-10-24 04:42:06.100975
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:42:18.041744
# Unit test for function escape

# Generated at 2026-10-24 04:42:19.473903
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 04:42:27.771441
# Unit test for function test

# Generated at 2026-10-24 04:42:29.179778
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:42:36.577024
# Unit test for function test

# Generated at 2026-10-24 04:42:39.087278
# Unit test for function test

# Generated at 2026-10-24 04:42:41.998166
# Unit test for function test

# Generated at 2026-10-24 04:42:44.411094
# Unit test for function escape

# Generated at 2026-10-24 04:42:46.901534
# Unit test for function escape

# Generated at 2026-10-24 04:42:49.317731
# Unit test for function escape

# Generated at 2026-10-24 04:42:51.735039
# Unit test for function escape

# Generated at 2026-10-24 04:42:54.368762
# Unit test for function escape

# Generated at 2026-10-24 04:42:56.782785
# Unit test for function escape

# Generated at 2026-10-24 04:42:59.192618
# Unit test for function test

# Generated at 2026-10-24 04:43:01.605969
# Unit test for function test

# Generated at 2026-10-24 04:43:04.017634
# Unit test for function test

# Generated at 2026-10-24 04:43:06.433807
# Unit test for function escape

# Generated at 2026-10-24 04:43:08.850810
# Unit test for function escape

# Generated at 2026-10-24 04:43:11.263046
# Unit test for function escape

# Generated at 2026-10-24 04:43:13.676961
# Unit test for function escape

# Generated at 2026-10-24 04:43:16.089511
# Unit test for function escape

# Generated at 2026-10-24 04:43:18.505345
# Unit test for function escape

# Generated at 2026-10-24 04:43:20.916120
# Unit test for function escape

# Generated at 2026-10-24 04:43:23.331801
# Unit test for function escape

# Generated at 2026-10-24 04:43:25.741624
# Unit test for function escape

# Generated at 2026-10-24 04:43:28.154637
# Unit test for function test

# Generated at 2026-10-24 04:43:30.568568
# Unit test for function test

# Generated at 2026-10-24 04:43:32.984471
# Unit test for function test

# Generated at 2026-10-24 04:43:35.396624
# Unit test for function escape

# Generated at 2026-10-24 04:43:37.813328
# Unit test for function escape

# Generated at 2026-10-24 04:43:40.227561
# Unit test for function escape

# Generated at 2026-10-24 04:43:42.812777
# Unit test for function test

# Generated at 2026-10-24 04:43:45.227166
# Unit test for function test

# Generated at 2026-10-24 04:43:47.639311
# Unit test for function test

# Generated at 2026-10-24 04:43:50.053441
# Unit test for function escape

# Generated at 2026-10-24 04:43:52.465993
# Unit test for function escape

# Generated at 2026-10-24 04:43:54.878345
# Unit test for function escape

# Generated at 2026-10-24 04:43:57.290357
# Unit test for function test

# Generated at 2026-10-24 04:43:58.850340
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:44:09.761190
# Unit test for function test

# Generated at 2026-10-24 04:44:11.196323
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:44:18.862488
# Unit test for function test

# Generated at 2026-10-24 04:44:20.308614
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 04:44:33.327496
# Unit test for function escape

# Generated at 2026-10-24 04:44:35.828696
# Unit test for function escape

# Generated at 2026-10-24 04:44:38.243394
# Unit test for function escape

# Generated at 2026-10-24 04:44:40.654302
# Unit test for function test

# Generated at 2026-10-24 04:44:43.065898
# Unit test for function test

# Generated at 2026-10-24 04:44:45.480467
# Unit test for function test

# Generated at 2026-10-24 04:44:47.893997
# Unit test for function escape

# Generated at 2026-10-24 04:44:50.306610
# Unit test for function escape

# Generated at 2026-10-24 04:44:52.719236
# Unit test for function escape

# Generated at 2026-10-24 04:44:55.130514
# Unit test for function test

# Generated at 2026-10-24 04:44:57.541864
# Unit test for function test

# Generated at 2026-10-24 04:44:59.951459
# Unit test for function test

# Generated at 2026-10-24 04:45:02.363911
# Unit test for function escape

# Generated at 2026-10-24 04:45:04.777006
# Unit test for function escape

# Generated at 2026-10-24 04:45:07.188443
# Unit test for function escape

# Generated at 2026-10-24 04:45:11.172610
# Unit test for function escape

# Generated at 2026-10-24 04:45:13.585432
# Unit test for function escape

# Generated at 2026-10-24 04:45:15.997755
# Unit test for function escape

# Generated at 2026-10-24 04:45:18.409607
# Unit test for function escape

# Generated at 2026-10-24 04:45:20.820247
# Unit test for function escape

# Generated at 2026-10-24 04:45:23.232608
# Unit test for function escape

# Generated at 2026-10-24 04:45:25.644169
# Unit test for function escape

# Generated at 2026-10-24 04:45:28.055063
# Unit test for function escape

# Generated at 2026-10-24 04:45:30.466734
# Unit test for function escape

# Generated at 2026-10-24 04:45:32.879115
# Unit test for function escape

# Generated at 2026-10-24 04:45:35.292033
# Unit test for function escape

# Generated at 2026-10-24 04:45:37.704679
# Unit test for function escape

# Generated at 2026-10-24 04:45:40.117458
# Unit test for function test

# Generated at 2026-10-24 04:45:42.532350
# Unit test for function test

# Generated at 2026-10-24 04:45:44.944055
# Unit test for function test