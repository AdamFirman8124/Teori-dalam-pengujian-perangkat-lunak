

# Generated at 2026-10-24 20:06:46.843140
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

# Generated at 2026-10-24 20:06:48.169565
# Unit test for function escape

# Generated at 2026-10-24 20:06:49.654058
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:06:50.966225
# Unit test for function escape

# Generated at 2026-10-24 20:06:52.420440
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:06:53.853651
# Unit test for function escape

# Generated at 2026-10-24 20:06:55.267218
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:06:57.930176
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

# Generated at 2026-10-24 20:07:00.007531
# Unit test for function escape

# Generated at 2026-10-24 20:07:01.357400
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:07:02.769041
# Unit test for function escape

# Generated at 2026-10-24 20:07:05.291480
# Unit test for function escape

# Generated at 2026-10-24 20:07:07.710808
# Unit test for function escape

# Generated at 2026-10-24 20:07:10.129812
# Unit test for function test

# Generated at 2026-10-24 20:07:12.552114
# Unit test for function test

# Generated at 2026-10-24 20:07:14.969094
# Unit test for function test

# Generated at 2026-10-24 20:07:17.388011
# Unit test for function test

# Generated at 2026-10-24 20:07:19.806413
# Unit test for function test

# Generated at 2026-10-24 20:07:22.229681
# Unit test for function test

# Generated at 2026-10-24 20:07:24.652181
# Unit test for function test

# Generated at 2026-10-24 20:07:27.064610
# Unit test for function test

# Generated at 2026-10-24 20:07:29.486182
# Unit test for function test

# Generated at 2026-10-24 20:07:31.904218
# Unit test for function escape

# Generated at 2026-10-24 20:07:34.320546
# Unit test for function escape

# Generated at 2026-10-24 20:07:36.739214
# Unit test for function escape

# Generated at 2026-10-24 20:07:39.155950
# Unit test for function test

# Generated at 2026-10-24 20:07:41.573034
# Unit test for function test

# Generated at 2026-10-24 20:07:43.990484
# Unit test for function test

# Generated at 2026-10-24 20:07:46.407836
# Unit test for function escape

# Generated at 2026-10-24 20:07:48.825392
# Unit test for function escape

# Generated at 2026-10-24 20:07:59.902231
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-10-24 20:08:01.335500
# Unit test for function escape

# Generated at 2026-10-24 20:08:02.873915
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:08:04.306891
# Unit test for function escape

# Generated at 2026-10-24 20:08:05.739796
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:08:07.056806
# Unit test for function escape

# Generated at 2026-10-24 20:08:08.439184
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:08:09.765155
# Unit test for function escape

# Generated at 2026-10-24 20:08:11.164612
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:08:22.021310
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 20:08:23.332351
# Unit test for function escape

# Generated at 2026-10-24 20:08:24.785706
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:08:27.205634
# Unit test for function test

# Generated at 2026-10-24 20:08:29.626495
# Unit test for function test

# Generated at 2026-10-24 20:08:32.146043
# Unit test for function test

# Generated at 2026-10-24 20:08:34.564033
# Unit test for function escape

# Generated at 2026-10-24 20:08:36.983511
# Unit test for function escape

# Generated at 2026-10-24 20:08:39.401660
# Unit test for function escape

# Generated at 2026-10-24 20:08:41.824844
# Unit test for function escape

# Generated at 2026-10-24 20:08:44.237900
# Unit test for function escape

# Generated at 2026-10-24 20:08:46.657128
# Unit test for function escape

# Generated at 2026-10-24 20:08:49.074330
# Unit test for function test

# Generated at 2026-10-24 20:08:51.489128
# Unit test for function test

# Generated at 2026-10-24 20:08:53.906696
# Unit test for function test

# Generated at 2026-10-24 20:08:56.325720
# Unit test for function test

# Generated at 2026-10-24 20:08:58.743007
# Unit test for function test

# Generated at 2026-10-24 20:09:01.163022
# Unit test for function test

# Generated at 2026-10-24 20:09:03.576814
# Unit test for function escape

# Generated at 2026-10-24 20:09:05.995291
# Unit test for function escape

# Generated at 2026-10-24 20:09:08.412757
# Unit test for function escape

# Generated at 2026-10-24 20:09:10.828705
# Unit test for function test

# Generated at 2026-10-24 20:09:12.215637
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 20:09:13.579379
# Unit test for function escape

# Generated at 2026-10-24 20:09:14.959556
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:09:23.744092
# Unit test for function test
def test_test():import contextlib

# Generated at 2026-10-24 20:09:25.070937
# Unit test for function escape

# Generated at 2026-10-24 20:09:26.531644
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:09:27.845539
# Unit test for function escape

# Generated at 2026-10-24 20:09:29.221265
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:09:30.553026
# Unit test for function escape

# Generated at 2026-10-24 20:09:31.926303
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:09:33.265635
# Unit test for function escape

# Generated at 2026-10-24 20:09:34.639317
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:09:37.160250
# Unit test for function escape

# Generated at 2026-10-24 20:09:39.577539
# Unit test for function escape

# Generated at 2026-10-24 20:09:42.153022
# Unit test for function escape

# Generated at 2026-10-24 20:09:44.569614
# Unit test for function escape

# Generated at 2026-10-24 20:09:46.990795
# Unit test for function escape

# Generated at 2026-10-24 20:09:49.564586
# Unit test for function escape

# Generated at 2026-10-24 20:09:51.983786
# Unit test for function escape

# Generated at 2026-10-24 20:09:54.507714
# Unit test for function escape

# Generated at 2026-10-24 20:09:56.928792
# Unit test for function escape

# Generated at 2026-10-24 20:09:59.275205
# Unit test for function escape

# Generated at 2026-10-24 20:10:00.735427
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:02.168094
# Unit test for function escape

# Generated at 2026-10-24 20:10:03.600626
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:04.923877
# Unit test for function escape

# Generated at 2026-10-24 20:10:06.569938
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:08.004511
# Unit test for function escape

# Generated at 2026-10-24 20:10:09.422560
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:10.749145
# Unit test for function escape

# Generated at 2026-10-24 20:10:12.202061
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:13.636857
# Unit test for function escape

# Generated at 2026-10-24 20:10:15.068937
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:16.386572
# Unit test for function escape

# Generated at 2026-10-24 20:10:17.833693
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:19.206427
# Unit test for function escape

# Generated at 2026-10-24 20:10:20.598327
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:21.913868
# Unit test for function escape

# Generated at 2026-10-24 20:10:23.261665
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:10:25.679724
# Unit test for function escape

# Generated at 2026-10-24 20:10:28.096236
# Unit test for function escape

# Generated at 2026-10-24 20:10:30.513314
# Unit test for function escape

# Generated at 2026-10-24 20:10:36.675321
# Unit test for function escape

# Generated at 2026-10-24 20:10:39.302668
# Unit test for function escape

# Generated at 2026-10-24 20:10:41.722118
# Unit test for function escape

# Generated at 2026-10-24 20:10:44.139127
# Unit test for function escape

# Generated at 2026-10-24 20:10:46.558546
# Unit test for function escape

# Generated at 2026-10-24 20:10:48.976503
# Unit test for function escape

# Generated at 2026-10-24 20:10:51.392055
# Unit test for function test

# Generated at 2026-10-24 20:10:53.809094
# Unit test for function test

# Generated at 2026-10-24 20:10:56.228428
# Unit test for function test

# Generated at 2026-10-24 20:10:58.644812
# Unit test for function escape

# Generated at 2026-10-24 20:11:01.059985
# Unit test for function escape

# Generated at 2026-10-24 20:11:03.669481
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-10-24 20:11:04.989411
# Unit test for function escape

# Generated at 2026-10-24 20:11:06.372989
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:11:07.806528
# Unit test for function escape

# Generated at 2026-10-24 20:11:09.239411
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:11:10.596702
# Unit test for function escape

# Generated at 2026-10-24 20:11:12.006878
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:11:13.324892
# Unit test for function escape

# Generated at 2026-10-24 20:11:14.769202
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:11:16.113238
# Unit test for function escape

# Generated at 2026-10-24 20:11:17.533802
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:11:26.964715
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 20:11:39.026292
# Unit test for function escape

# Generated at 2026-10-24 20:11:41.442029
# Unit test for function escape

# Generated at 2026-10-24 20:11:43.860056
# Unit test for function escape

# Generated at 2026-10-24 20:11:46.428568
# Unit test for function escape

# Generated at 2026-10-24 20:11:48.851064
# Unit test for function escape

# Generated at 2026-10-24 20:11:51.270067
# Unit test for function escape

# Generated at 2026-10-24 20:11:53.688376
# Unit test for function escape

# Generated at 2026-10-24 20:11:56.108411
# Unit test for function escape

# Generated at 2026-10-24 20:11:58.523126
# Unit test for function escape

# Generated at 2026-10-24 20:12:00.939803
# Unit test for function escape

# Generated at 2026-10-24 20:12:03.359004
# Unit test for function escape

# Generated at 2026-10-24 20:12:05.775492
# Unit test for function escape

# Generated at 2026-10-24 20:12:08.192806
# Unit test for function escape

# Generated at 2026-10-24 20:12:10.609608
# Unit test for function escape

# Generated at 2026-10-24 20:12:13.027067
# Unit test for function escape

# Generated at 2026-10-24 20:12:15.445738
# Unit test for function escape

# Generated at 2026-10-24 20:12:17.863579
# Unit test for function escape

# Generated at 2026-10-24 20:12:20.278987
# Unit test for function escape

# Generated at 2026-10-24 20:12:22.696731
# Unit test for function test

# Generated at 2026-10-24 20:12:25.112430
# Unit test for function test

# Generated at 2026-10-24 20:12:27.531693
# Unit test for function test

# Generated at 2026-10-24 20:12:29.948645
# Unit test for function escape

# Generated at 2026-10-24 20:12:32.367140
# Unit test for function escape

# Generated at 2026-10-24 20:12:34.782127
# Unit test for function escape

# Generated at 2026-10-24 20:12:37.201319
# Unit test for function escape

# Generated at 2026-10-24 20:12:39.616551
# Unit test for function escape

# Generated at 2026-10-24 20:12:42.033191
# Unit test for function escape

# Generated at 2026-10-24 20:12:44.449369
# Unit test for function escape

# Generated at 2026-10-24 20:12:46.864479
# Unit test for function escape

# Generated at 2026-10-24 20:12:49.281864
# Unit test for function escape

# Generated at 2026-10-24 20:13:11.033165
# Unit test for function escape

# Generated at 2026-10-24 20:13:13.451082
# Unit test for function escape

# Generated at 2026-10-24 20:13:15.869644
# Unit test for function escape

# Generated at 2026-10-24 20:13:18.289891
# Unit test for function escape

# Generated at 2026-10-24 20:13:20.703527
# Unit test for function escape

# Generated at 2026-10-24 20:13:23.120957
# Unit test for function escape

# Generated at 2026-10-24 20:13:25.536153
# Unit test for function test

# Generated at 2026-10-24 20:13:27.952512
# Unit test for function test

# Generated at 2026-10-24 20:13:30.368959
# Unit test for function test

# Generated at 2026-10-24 20:13:32.787754
# Unit test for function escape

# Generated at 2026-10-24 20:13:35.206863
# Unit test for function escape

# Generated at 2026-10-24 20:13:37.620251
# Unit test for function escape

# Generated at 2026-10-24 20:13:40.041857
# Unit test for function escape

# Generated at 2026-10-24 20:13:42.456372
# Unit test for function escape

# Generated at 2026-10-24 20:13:44.873480
# Unit test for function escape

# Generated at 2026-10-24 20:13:47.289487
# Unit test for function escape

# Generated at 2026-10-24 20:13:49.710928
# Unit test for function escape

# Generated at 2026-10-24 20:13:52.127385
# Unit test for function escape

# Generated at 2026-10-24 20:13:54.858388
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

# Generated at 2026-10-24 20:13:56.204408
# Unit test for function escape

# Generated at 2026-10-24 20:13:57.585810
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:14:08.372034
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 20:14:09.694702
# Unit test for function escape

# Generated at 2026-10-24 20:14:11.102513
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:15:00.008657
# Unit test for function escape

# Generated at 2026-10-24 20:15:02.424728
# Unit test for function escape

# Generated at 2026-10-24 20:15:04.841041
# Unit test for function escape

# Generated at 2026-10-24 20:15:07.255583
# Unit test for function escape

# Generated at 2026-10-24 20:15:09.672498
# Unit test for function escape

# Generated at 2026-10-24 20:15:12.093077
# Unit test for function escape

# Generated at 2026-10-24 20:15:14.512225
# Unit test for function test

# Generated at 2026-10-24 20:15:16.928695
# Unit test for function test

# Generated at 2026-10-24 20:15:19.542013
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 20:15:21.190888
# Unit test for function escape

# Generated at 2026-10-24 20:15:22.613648
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:15:23.945062
# Unit test for function escape

# Generated at 2026-10-24 20:15:25.355314
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:15:36.302003
# Unit test for function test
def test_test():import contextlib

# Generated at 2026-10-24 20:15:46.118501
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 20:15:47.687484
# Unit test for function escape

# Generated at 2026-10-24 20:15:49.055398
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 20:15:50.379844
# Unit test for function escape

# Generated at 2026-10-24 20:15:53.036594
# Unit test for function escape

# Generated at 2026-10-24 20:15:55.455942
# Unit test for function escape

# Generated at 2026-10-24 20:15:57.983670
# Unit test for function escape

# Generated at 2026-10-24 20:16:00.399293
# Unit test for function escape

# Generated at 2026-10-24 20:16:02.818875
# Unit test for function escape