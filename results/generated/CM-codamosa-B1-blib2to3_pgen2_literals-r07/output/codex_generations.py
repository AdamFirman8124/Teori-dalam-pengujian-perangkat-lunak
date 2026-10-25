

# Generated at 2026-10-24 19:12:56.571829
# Unit test for function test

# Generated at 2026-10-24 19:13:05.305978
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 19:13:07.838292
# Unit test for function escape

# Generated at 2026-10-24 19:13:10.255855
# Unit test for function escape

# Generated at 2026-10-24 19:13:12.672516
# Unit test for function escape

# Generated at 2026-10-24 19:13:15.088912
# Unit test for function escape

# Generated at 2026-10-24 19:13:17.504281
# Unit test for function escape

# Generated at 2026-10-24 19:13:19.920930
# Unit test for function escape

# Generated at 2026-10-24 19:13:37.940958
# Unit test for function escape

# Generated at 2026-10-24 19:13:55.646971
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:13:58.071500
# Unit test for function test

# Generated at 2026-10-24 19:14:00.487372
# Unit test for function test

# Generated at 2026-10-24 19:14:03.061313
# Unit test for function test

# Generated at 2026-10-24 19:14:05.483136
# Unit test for function test

# Generated at 2026-10-24 19:14:07.911914
# Unit test for function test

# Generated at 2026-10-24 19:14:10.320986
# Unit test for function test

# Generated at 2026-10-24 19:14:12.742556
# Unit test for function evalString

# Generated at 2026-10-24 19:14:15.308922
# Unit test for function evalString

# Generated at 2026-10-24 19:14:17.726016
# Unit test for function evalString

# Generated at 2026-10-24 19:14:20.146689
# Unit test for function escape

# Generated at 2026-10-24 19:14:22.561303
# Unit test for function escape

# Generated at 2026-10-24 19:14:24.982366
# Unit test for function escape

# Generated at 2026-10-24 19:14:27.399236
# Unit test for function test

# Generated at 2026-10-24 19:14:29.819938
# Unit test for function test

# Generated at 2026-10-24 19:14:32.237179
# Unit test for function test

# Generated at 2026-10-24 19:14:34.655755
# Unit test for function escape

# Generated at 2026-10-24 19:14:37.081390
# Unit test for function escape

# Generated at 2026-10-24 19:14:39.493661
# Unit test for function escape

# Generated at 2026-10-24 19:14:41.912499
# Unit test for function escape

# Generated at 2026-10-24 19:14:44.336527
# Unit test for function escape

# Generated at 2026-10-24 19:14:45.776024
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:14:47.101801
# Unit test for function escape

# Generated at 2026-10-24 19:14:48.458868
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:15:01.754072
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:15:03.117819
# Unit test for function escape

# Generated at 2026-10-24 19:15:05.536540
# Unit test for function escape

# Generated at 2026-10-24 19:15:07.957090
# Unit test for function escape

# Generated at 2026-10-24 19:15:10.541393
# Unit test for function escape

# Generated at 2026-10-24 19:15:12.955754
# Unit test for function escape

# Generated at 2026-10-24 19:15:15.374551
# Unit test for function escape

# Generated at 2026-10-24 19:15:17.867809
# Unit test for function escape

# Generated at 2026-10-24 19:15:20.285620
# Unit test for function escape

# Generated at 2026-10-24 19:15:22.700683
# Unit test for function escape

# Generated at 2026-10-24 19:15:25.116937
# Unit test for function test

# Generated at 2026-10-24 19:15:27.766826
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 19:15:29.126138
# Unit test for function escape

# Generated at 2026-10-24 19:15:30.498913
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:15:43.071053
# Unit test for function evalString
def test_evalString():
    # Every single character must round-trip through repr()
    for i in range(256):
        c = chr(i)
        s = repr(c)
        assert module_0.evalString(s) == c, (i, c, s, module_0.evalString(s))

    # Plain strings, both quote styles
    assert module_0.evalString("'abc'") == "abc"
    assert module_0.evalString('"abc"') == "abc"

    # Simple escapes
    assert module_0.evalString(r"'\n'") == "\n"
    assert module_0.evalString(r"'\t'") == "\t"
    assert module_0.evalString(r"'\r'") == "\r"
    assert module_0.evalString(r"'\a'") == "\a"
    assert module_0.evalString(r"'\b'") == "\b"
    assert module_0.evalString(r"'\f'") == "\f"
    assert module_0.evalString(r"'\v'") == "\v"
    assert module_0.evalString(r"'\\'") == "\\"
    assert module_0.evalString(r"'\''") == "'"
    assert module_0.evalString(r'"\""') == '"'

    # Hex and octal escapes
    assert module_0.evalString(r"'\x41'") == "A"
    assert module_0.evalString(r"'\x00'") == "\x00"
    assert module_0.evalString(r"'\xff'") == "\xff"
    assert module_0.evalString(r"'\101'") == "A"
    assert module_0.evalString(r"'\0'") == "\0"
    assert module_0.evalString(r"'\377'") == "\xff"

    # Triple-quoted strings
    assert module_0.evalString("'''abc'''") == "abc"
    assert module_0.evalString('"""abc"""') == "abc"
    assert module_0.evalString('"""a\nb"""') == "a\nb"

    # Empty strings
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""
    assert module_0.evalString("''''''") == ""

    # Mixed content
    assert module_0.evalString(r"'a\tb\x41c\101d'") == "a\tbAcAd"
    assert module_0.evalString(r"'\n\t\\\''") == "\n\t\\'"

    # Invalid hex escapes raise ValueError
    for bad in (r"'\x'", r"'\x4'", r"'\xg1'"):
        try:
            module_0.evalString(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % (bad,))

    print("test_evalString passed")

# Generated at 2026-10-24 19:15:44.506340
# Unit test for function escape

# Generated at 2026-10-24 19:15:45.936797
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:15:47.266148
# Unit test for function escape

# Generated at 2026-10-24 19:15:48.701829
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:15:57.407452
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:15:59.940510
# Unit test for function escape

# Generated at 2026-10-24 19:16:02.362267
# Unit test for function escape

# Generated at 2026-10-24 19:16:04.940404
# Unit test for function escape

# Generated at 2026-10-24 19:16:07.357836
# Unit test for function escape

# Generated at 2026-10-24 19:16:09.978605
# Unit test for function escape

# Generated at 2026-10-24 19:16:12.409516
# Unit test for function escape

# Generated at 2026-10-24 19:16:14.825906
# Unit test for function test

# Generated at 2026-10-24 19:16:17.243154
# Unit test for function test

# Generated at 2026-10-24 19:16:19.662652
# Unit test for function test

# Generated at 2026-10-24 19:16:22.097623
# Unit test for function escape

# Generated at 2026-10-24 19:16:24.516017
# Unit test for function escape

# Generated at 2026-10-24 19:16:26.951752
# Unit test for function escape

# Generated at 2026-10-24 19:16:29.394730
# Unit test for function test

# Generated at 2026-10-24 19:16:31.810207
# Unit test for function test

# Generated at 2026-10-24 19:16:34.226212
# Unit test for function test

# Generated at 2026-10-24 19:16:36.641873
# Unit test for function evalString

# Generated at 2026-10-24 19:16:39.059824
# Unit test for function evalString

# Generated at 2026-10-24 19:16:41.479305
# Unit test for function evalString

# Generated at 2026-10-24 19:16:43.899338
# Unit test for function escape

# Generated at 2026-10-24 19:16:46.314643
# Unit test for function escape

# Generated at 2026-10-24 19:16:48.729926
# Unit test for function escape

# Generated at 2026-10-24 19:16:51.149973
# Unit test for function test

# Generated at 2026-10-24 19:16:53.567925
# Unit test for function test

# Generated at 2026-10-24 19:16:55.983981
# Unit test for function test

# Generated at 2026-10-24 19:16:58.402470
# Unit test for function evalString

# Generated at 2026-10-24 19:17:00.819193
# Unit test for function evalString

# Generated at 2026-10-24 19:17:03.235737
# Unit test for function evalString

# Generated at 2026-10-24 19:17:05.652747
# Unit test for function escape

# Generated at 2026-10-24 19:17:08.068630
# Unit test for function escape

# Generated at 2026-10-24 19:17:10.487133
# Unit test for function escape

# Generated at 2026-10-24 19:17:12.907625
# Unit test for function escape

# Generated at 2026-10-24 19:17:15.320052
# Unit test for function escape

# Generated at 2026-10-24 19:17:17.735677
# Unit test for function escape

# Generated at 2026-10-24 19:17:20.154685
# Unit test for function escape

# Generated at 2026-10-24 19:17:22.572046
# Unit test for function escape

# Generated at 2026-10-24 19:17:24.987795
# Unit test for function escape

# Generated at 2026-10-24 19:17:27.556627
# Unit test for function escape
def test_escape():
    def make(s):
        # Build a Match whose group(0) starts with a backslash and
        # group(1) is the escape tail, mirroring evalString's regex.
        return re.match(r"\\(.+)", s)

    # Simple escapes
    assert module_0.escape(make(r"\n")) == "\n"
    assert module_0.escape(make(r"\t")) == "\t"
    assert module_0.escape(make(r"\r")) == "\r"
    assert module_0.escape(make(r"\a")) == "\a"
    assert module_0.escape(make(r"\b")) == "\b"
    assert module_0.escape(make(r"\f")) == "\f"
    assert module_0.escape(make(r"\v")) == "\v"
    assert module_0.escape(make(r"\'")) == "'"
    assert module_0.escape(make(r'\"')) == '"'
    assert module_0.escape(make(r"\\")) == "\\"

    # Hex escapes
    assert module_0.escape(make(r"\x41")) == "A"
    assert module_0.escape(make(r"\x7a")) == "z"
    assert module_0.escape(make(r"\xff")) == chr(255)
    assert module_0.escape(make(r"\x00")) == "\x00"

    # Octal escapes
    assert module_0.escape(make(r"\101")) == "A"
    assert module_0.escape(make(r"\0")) == "\0"
    assert module_0.escape(make(r"\7")) == "\a"
    assert module_0.escape(make(r"\377")) == chr(255)
    assert module_0.escape(make(r"\012")) == "\n"

    # Invalid escapes must raise ValueError
    for bad in (r"\x", r"\x4", r"\xzz", r"\xg1", r"\8", r"\9"):
        try:
            module_0.escape(make(bad))
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

# Generated at 2026-10-24 19:17:39.852757
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:17:41.175097
# Unit test for function escape

# Generated at 2026-10-24 19:17:42.533816
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:17:52.199291
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:17:54.620059
# Unit test for function test

# Generated at 2026-10-24 19:17:57.036307
# Unit test for function test

# Generated at 2026-10-24 19:17:59.451507
# Unit test for function test

# Generated at 2026-10-24 19:18:01.868822
# Unit test for function escape

# Generated at 2026-10-24 19:18:04.286430
# Unit test for function escape

# Generated at 2026-10-24 19:18:06.704316
# Unit test for function escape

# Generated at 2026-10-24 19:18:09.121203
# Unit test for function test

# Generated at 2026-10-24 19:18:11.540988
# Unit test for function test

# Generated at 2026-10-24 19:18:14.130043
# Unit test for function test

# Generated at 2026-10-24 19:18:16.546852
# Unit test for function escape

# Generated at 2026-10-24 19:18:18.964416
# Unit test for function escape

# Generated at 2026-10-24 19:18:21.380022
# Unit test for function escape

# Generated at 2026-10-24 19:18:23.798583
# Unit test for function evalString

# Generated at 2026-10-24 19:18:26.213398
# Unit test for function evalString

# Generated at 2026-10-24 19:18:28.631937
# Unit test for function evalString

# Generated at 2026-10-24 19:18:31.049872
# Unit test for function escape

# Generated at 2026-10-24 19:18:33.469644
# Unit test for function escape

# Generated at 2026-10-24 19:18:35.882887
# Unit test for function escape

# Generated at 2026-10-24 19:18:38.301802
# Unit test for function test

# Generated at 2026-10-24 19:18:40.719278
# Unit test for function test

# Generated at 2026-10-24 19:18:43.139520
# Unit test for function test

# Generated at 2026-10-24 19:18:49.641614
# Unit test for function escape

# Generated at 2026-10-24 19:18:52.057210
# Unit test for function escape

# Generated at 2026-10-24 19:18:54.471667
# Unit test for function escape

# Generated at 2026-10-24 19:18:56.890282
# Unit test for function test

# Generated at 2026-10-24 19:18:59.307241
# Unit test for function test

# Generated at 2026-10-24 19:19:01.741006
# Unit test for function test

# Generated at 2026-10-24 19:19:04.170600
# Unit test for function test

# Generated at 2026-10-24 19:19:06.598781
# Unit test for function test

# Generated at 2026-10-24 19:19:09.042029
# Unit test for function test

# Generated at 2026-10-24 19:19:11.472917
# Unit test for function test

# Generated at 2026-10-24 19:19:13.886669
# Unit test for function test

# Generated at 2026-10-24 19:19:16.302246
# Unit test for function test

# Generated at 2026-10-24 19:19:24.525075
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints one line per mismatch; capture stdout and require silence.
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "round-trip mismatches for repr/evalString:\n%s" % buf.getvalue()

    # Direct round-trip check as a belt-and-braces assertion.
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, (i, c, repr(c), evalString(repr(c)))

    # Spot-check the documented escape handling.
    assert evalString(r'"a\nb"') == "a\nb"
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\''") == "'"

# Generated at 2026-10-24 19:19:27.264510
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints one line per mismatch; capture stdout and require silence.
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "round-trip mismatches for repr/evalString:\n%s" % buf.getvalue()

    # Direct round-trip check as a belt-and-braces assertion.
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, (i, c, repr(c), evalString(repr(c)))

    # Spot-check the documented escape handling.
    assert evalString(r'"a\nb"') == "a\nb"
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\''") == "'"

# Generated at 2026-10-24 19:19:28.590537
# Unit test for function escape

# Generated at 2026-10-24 19:19:29.969363
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:19:31.288294
# Unit test for function escape

# Generated at 2026-10-24 19:19:32.754689
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:19:34.078446
# Unit test for function escape

# Generated at 2026-10-24 19:19:35.518731
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:19:36.842227
# Unit test for function escape

# Generated at 2026-10-24 19:19:39.388898
# Unit test for function escape

# Generated at 2026-10-24 19:19:41.804089
# Unit test for function escape

# Generated at 2026-10-24 19:19:49.008586
# Unit test for function escape

# Generated at 2026-10-24 19:19:51.425917
# Unit test for function escape

# Generated at 2026-10-24 19:19:53.842947
# Unit test for function escape

# Generated at 2026-10-24 19:19:56.260362
# Unit test for function test

# Generated at 2026-10-24 19:19:58.678296
# Unit test for function test

# Generated at 2026-10-24 19:20:01.267023
# Unit test for function test

# Generated at 2026-10-24 19:20:03.682765
# Unit test for function escape

# Generated at 2026-10-24 19:20:06.101344
# Unit test for function escape

# Generated at 2026-10-24 19:20:08.520525
# Unit test for function escape

# Generated at 2026-10-24 19:20:10.995796
# Unit test for function test

# Generated at 2026-10-24 19:20:13.354839
# Unit test for function test

# Generated at 2026-10-24 19:20:15.772418
# Unit test for function test

# Generated at 2026-10-24 19:20:18.188725
# Unit test for function escape

# Generated at 2026-10-24 19:20:20.606979
# Unit test for function escape

# Generated at 2026-10-24 19:20:23.023788
# Unit test for function escape

# Generated at 2026-10-24 19:20:25.441683
# Unit test for function escape

# Generated at 2026-10-24 19:20:27.857762
# Unit test for function escape

# Generated at 2026-10-24 19:20:29.269200
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:20:30.602287
# Unit test for function escape

# Generated at 2026-10-24 19:20:31.951920
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:20:45.868321
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:20:48.289650
# Unit test for function test

# Generated at 2026-10-24 19:20:50.706918
# Unit test for function test

# Generated at 2026-10-24 19:20:53.271121
# Unit test for function test

# Generated at 2026-10-24 19:20:55.686838
# Unit test for function test

# Generated at 2026-10-24 19:20:58.101940
# Unit test for function test

# Generated at 2026-10-24 19:21:00.520623
# Unit test for function test

# Generated at 2026-10-24 19:21:12.813913
# Unit test for function escape

# Generated at 2026-10-24 19:21:15.229433
# Unit test for function escape

# Generated at 2026-10-24 19:21:17.648825
# Unit test for function escape

# Generated at 2026-10-24 19:21:20.064508
# Unit test for function test

# Generated at 2026-10-24 19:21:22.480294
# Unit test for function test

# Generated at 2026-10-24 19:21:24.896431
# Unit test for function test

# Generated at 2026-10-24 19:21:27.310845
# Unit test for function test

# Generated at 2026-10-24 19:21:29.904969
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 19:21:40.448853
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:21:41.882419
# Unit test for function escape

# Generated at 2026-10-24 19:21:43.314491
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 19:21:54.067077
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 19:21:56.485346
# Unit test for function escape

# Generated at 2026-10-24 19:21:58.903500
# Unit test for function escape

# Generated at 2026-10-24 19:22:01.431425
# Unit test for function escape

# Generated at 2026-10-24 19:22:03.960449
# Unit test for function escape

# Generated at 2026-10-24 19:22:06.480942
# Unit test for function escape

# Generated at 2026-10-24 19:22:08.897629
# Unit test for function escape

# Generated at 2026-10-24 19:22:11.316292
# Unit test for function test

# Generated at 2026-10-24 19:22:13.832418
# Unit test for function test

# Generated at 2026-10-24 19:22:16.247777
# Unit test for function test

# Generated at 2026-10-24 19:22:18.665418
# Unit test for function escape

# Generated at 2026-10-24 19:22:21.086122
# Unit test for function escape

# Generated at 2026-10-24 19:22:23.499172
# Unit test for function escape