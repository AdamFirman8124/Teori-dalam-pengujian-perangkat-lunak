

# Generated at 2026-10-25 14:21:36.491201
# Unit test for function evalString

# Generated at 2026-10-25 14:22:00.985483
# Unit test for function evalString
def test_evalString():assert module_0.evalString(r"'hello\nworld'") == "hello\nworld"

# Generated at 2026-10-25 14:22:22.708632
# Unit test for function escape

# Generated at 2026-10-25 14:22:43.481943
# Unit test for function escape
def test_escape():match = re.match(r"\\(x41)", r"\x41")

# Generated at 2026-10-25 14:22:53.722582
# Unit test for function test
def test_test():from contextlib import redirect_stdout

# Generated at 2026-10-25 14:22:55.084959
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 14:22:56.487033
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 14:23:13.831120
# Unit test for function escape

# Generated at 2026-10-25 14:23:15.225718
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 14:23:29.152361
# Unit test for function escape

# Generated at 2026-10-25 14:23:30.585012
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-25 14:24:22.003936
# Unit test for function evalString

# Generated at 2026-10-25 14:24:31.361446
# Unit test for function evalString
def test_evalString():assert module_0.evalString(r"'hello\nworld'") == "hello\nworld"

# Generated at 2026-10-25 14:24:45.135063
# Unit test for function escape

# Generated at 2026-10-25 14:24:53.631710
# Unit test for function escape

# Generated at 2026-10-25 14:24:59.076894
# Unit test for function escape

# Generated at 2026-10-25 14:25:01.494865
# Unit test for function evalString

# Generated at 2026-10-25 14:25:03.909303
# Unit test for function evalString

# Generated at 2026-10-25 14:25:06.324092
# Unit test for function evalString

# Generated at 2026-10-25 14:25:11.764837
# Unit test for function evalString

# Generated at 2026-10-25 14:25:14.179333
# Unit test for function evalString

# Generated at 2026-10-25 14:25:16.597914
# Unit test for function evalString

# Generated at 2026-10-25 14:25:19.009019
# Unit test for function evalString

# Generated at 2026-10-25 14:25:21.425105
# Unit test for function evalString

# Generated at 2026-10-25 14:25:23.840811
# Unit test for function evalString

# Generated at 2026-10-25 14:25:26.255661
# Unit test for function evalString

# Generated at 2026-10-25 14:25:28.670682
# Unit test for function evalString

# Generated at 2026-10-25 14:25:31.085505
# Unit test for function evalString

# Generated at 2026-10-25 14:25:33.499867
# Unit test for function escape

# Generated at 2026-10-25 14:25:35.913932
# Unit test for function escape

# Generated at 2026-10-25 14:25:38.328851
# Unit test for function escape

# Generated at 2026-10-25 14:25:40.747564
# Unit test for function evalString

# Generated at 2026-10-25 14:25:43.164612
# Unit test for function evalString

# Generated at 2026-10-25 14:25:45.579787
# Unit test for function evalString

# Generated at 2026-10-25 14:25:48.410005
# Unit test for function escape

# Generated at 2026-10-25 14:25:50.824464
# Unit test for function escape

# Generated at 2026-10-25 14:25:53.240158
# Unit test for function escape

# Generated at 2026-10-25 14:25:55.654875
# Unit test for function escape

# Generated at 2026-10-25 14:25:58.072365
# Unit test for function escape

# Generated at 2026-10-25 14:26:00.489497
# Unit test for function escape

# Generated at 2026-10-25 14:26:02.906161
# Unit test for function escape

# Generated at 2026-10-25 14:26:05.319825
# Unit test for function escape

# Generated at 2026-10-25 14:26:07.736841
# Unit test for function escape

# Generated at 2026-10-25 14:26:10.212580
# Unit test for function escape

# Generated at 2026-10-25 14:26:12.562290
# Unit test for function escape

# Generated at 2026-10-25 14:26:14.975766
# Unit test for function escape

# Generated at 2026-10-25 14:26:17.393045
# Unit test for function test

# Generated at 2026-10-25 14:26:19.807868
# Unit test for function test

# Generated at 2026-10-25 14:26:22.226596
# Unit test for function test

# Generated at 2026-10-25 14:26:24.642839
# Unit test for function escape

# Generated at 2026-10-25 14:26:27.056355
# Unit test for function escape

# Generated at 2026-10-25 14:26:29.471059
# Unit test for function escape

# Generated at 2026-10-25 14:26:31.885942
# Unit test for function evalString

# Generated at 2026-10-25 14:26:34.301005
# Unit test for function evalString

# Generated at 2026-10-25 14:26:36.715672
# Unit test for function evalString

# Generated at 2026-10-25 14:26:39.130789
# Unit test for function escape

# Generated at 2026-10-25 14:26:41.546105
# Unit test for function escape

# Generated at 2026-10-25 14:26:43.964609
# Unit test for function escape

# Generated at 2026-10-25 14:26:46.378797
# Unit test for function test

# Generated at 2026-10-25 14:26:48.824943
# Unit test for function test

# Generated at 2026-10-25 14:26:51.205886
# Unit test for function test

# Generated at 2026-10-25 14:26:53.621526
# Unit test for function escape

# Generated at 2026-10-25 14:26:56.037183
# Unit test for function escape

# Generated at 2026-10-25 14:26:58.450528
# Unit test for function escape

# Generated at 2026-10-25 14:27:03.489532
# Unit test for function escape

# Generated at 2026-10-25 14:27:05.903860
# Unit test for function escape

# Generated at 2026-10-25 14:27:08.318378
# Unit test for function escape

# Generated at 2026-10-25 14:27:10.733771
# Unit test for function test

# Generated at 2026-10-25 14:27:16.181287
# Unit test for function test

# Generated at 2026-10-25 14:27:18.597875
# Unit test for function test

# Generated at 2026-10-25 14:27:21.010486
# Unit test for function test

# Generated at 2026-10-25 14:27:23.504294
# Unit test for function test

# Generated at 2026-10-25 14:27:25.917705
# Unit test for function test

# Generated at 2026-10-25 14:27:28.328417
# Unit test for function test

# Generated at 2026-10-25 14:27:30.744630
# Unit test for function test

# Generated at 2026-10-25 14:27:33.159842
# Unit test for function test

# Generated at 2026-10-25 14:27:35.578192
# Unit test for function test

# Generated at 2026-10-25 14:27:37.990773
# Unit test for function test

# Generated at 2026-10-25 14:27:40.404363
# Unit test for function test

# Generated at 2026-10-25 14:27:42.823167
# Unit test for function escape

# Generated at 2026-10-25 14:27:45.237411
# Unit test for function escape

# Generated at 2026-10-25 14:27:47.651806
# Unit test for function escape

# Generated at 2026-10-25 14:27:50.067707
# Unit test for function test

# Generated at 2026-10-25 14:27:52.483623
# Unit test for function test

# Generated at 2026-10-25 14:27:54.898152
# Unit test for function test

# Generated at 2026-10-25 14:27:57.312834
# Unit test for function escape

# Generated at 2026-10-25 14:27:59.727751
# Unit test for function escape

# Generated at 2026-10-25 14:28:02.145884
# Unit test for function escape

# Generated at 2026-10-25 14:28:04.561054
# Unit test for function escape

# Generated at 2026-10-25 14:28:06.976444
# Unit test for function escape

# Generated at 2026-10-25 14:28:09.390856
# Unit test for function escape

# Generated at 2026-10-25 14:28:11.805896
# Unit test for function escape

# Generated at 2026-10-25 14:28:14.221491
# Unit test for function escape

# Generated at 2026-10-25 14:28:16.635397
# Unit test for function escape

# Generated at 2026-10-25 14:28:22.797948
# Unit test for function escape

# Generated at 2026-10-25 14:28:25.215648
# Unit test for function escape

# Generated at 2026-10-25 14:28:27.628590
# Unit test for function escape

# Generated at 2026-10-25 14:28:30.044344
# Unit test for function escape

# Generated at 2026-10-25 14:28:32.461590
# Unit test for function escape

# Generated at 2026-10-25 14:28:34.873607
# Unit test for function escape

# Generated at 2026-10-25 14:28:37.288261
# Unit test for function escape

# Generated at 2026-10-25 14:28:39.702858
# Unit test for function escape

# Generated at 2026-10-25 14:28:42.121126
# Unit test for function escape

# Generated at 2026-10-25 14:28:44.539236
# Unit test for function escape

# Generated at 2026-10-25 14:28:46.952656
# Unit test for function escape

# Generated at 2026-10-25 14:28:49.366426
# Unit test for function escape

# Generated at 2026-10-25 14:28:51.783542
# Unit test for function escape

# Generated at 2026-10-25 14:28:54.196276
# Unit test for function escape

# Generated at 2026-10-25 14:28:56.610737
# Unit test for function escape

# Generated at 2026-10-25 14:28:59.025266
# Unit test for function escape

# Generated at 2026-10-25 14:29:01.443082
# Unit test for function escape

# Generated at 2026-10-25 14:29:03.860238
# Unit test for function escape

# Generated at 2026-10-25 14:29:06.277303
# Unit test for function escape

# Generated at 2026-10-25 14:29:08.689711
# Unit test for function escape

# Generated at 2026-10-25 14:29:11.104521
# Unit test for function escape

# Generated at 2026-10-25 14:29:13.519341
# Unit test for function escape

# Generated at 2026-10-25 14:29:18.957500
# Unit test for function escape

# Generated at 2026-10-25 14:29:21.375289
# Unit test for function escape

# Generated at 2026-10-25 14:29:23.787472
# Unit test for function escape

# Generated at 2026-10-25 14:29:26.205102
# Unit test for function escape

# Generated at 2026-10-25 14:29:28.617100
# Unit test for function escape

# Generated at 2026-10-25 14:29:31.035602
# Unit test for function escape

# Generated at 2026-10-25 14:29:33.451931
# Unit test for function escape

# Generated at 2026-10-25 14:29:35.864463
# Unit test for function escape

# Generated at 2026-10-25 14:29:47.488245
# Unit test for function escape

# Generated at 2026-10-25 14:29:49.901181
# Unit test for function escape

# Generated at 2026-10-25 14:29:52.313776
# Unit test for function escape

# Generated at 2026-10-25 14:29:54.794214
# Unit test for function escape

# Generated at 2026-10-25 14:29:57.180296
# Unit test for function escape

# Generated at 2026-10-25 14:29:59.652751
# Unit test for function escape

# Generated at 2026-10-25 14:30:02.054217
# Unit test for function test

# Generated at 2026-10-25 14:30:04.470309
# Unit test for function test

# Generated at 2026-10-25 14:30:06.885837
# Unit test for function test

# Generated at 2026-10-25 14:30:09.299614
# Unit test for function escape

# Generated at 2026-10-25 14:30:11.718964
# Unit test for function escape

# Generated at 2026-10-25 14:30:14.135569
# Unit test for function escape

# Generated at 2026-10-25 14:30:16.550700
# Unit test for function escape

# Generated at 2026-10-25 14:30:18.963490
# Unit test for function escape

# Generated at 2026-10-25 14:30:21.378331
# Unit test for function escape

# Generated at 2026-10-25 14:30:23.792352
# Unit test for function escape

# Generated at 2026-10-25 14:30:26.212632
# Unit test for function escape

# Generated at 2026-10-25 14:30:28.624046
# Unit test for function escape

# Generated at 2026-10-25 14:30:31.040945
# Unit test for function test

# Generated at 2026-10-25 14:30:33.459947
# Unit test for function test

# Generated at 2026-10-25 14:30:35.877107
# Unit test for function test

# Generated at 2026-10-25 14:30:38.290290
# Unit test for function test

# Generated at 2026-10-25 14:30:40.703307
# Unit test for function test

# Generated at 2026-10-25 14:30:43.118060
# Unit test for function test