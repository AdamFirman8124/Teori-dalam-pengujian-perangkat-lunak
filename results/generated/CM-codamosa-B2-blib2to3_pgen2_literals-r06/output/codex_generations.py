

# Generated at 2026-10-24 11:39:42.996099
# Unit test for function escape

# Generated at 2026-10-24 11:39:45.613576
# Unit test for function escape

# Generated at 2026-10-24 11:39:48.034873
# Unit test for function escape

# Generated at 2026-10-24 11:39:50.452667
# Unit test for function evalString

# Generated at 2026-10-24 11:39:52.872002
# Unit test for function evalString

# Generated at 2026-10-24 11:39:55.290295
# Unit test for function evalString

# Generated at 2026-10-24 11:39:57.703644
# Unit test for function evalString

# Generated at 2026-10-24 11:40:00.120874
# Unit test for function evalString

# Generated at 2026-10-24 11:40:02.539986
# Unit test for function evalString

# Generated at 2026-10-24 11:40:04.951346
# Unit test for function test

# Generated at 2026-10-24 11:40:07.375324
# Unit test for function test

# Generated at 2026-10-24 11:40:09.792319
# Unit test for function test

# Generated at 2026-10-24 11:40:12.208523
# Unit test for function escape

# Generated at 2026-10-24 11:40:14.629014
# Unit test for function escape

# Generated at 2026-10-24 11:40:17.046309
# Unit test for function escape

# Generated at 2026-10-24 11:40:19.753771
# Unit test for function evalString

# Generated at 2026-10-24 11:40:22.173870
# Unit test for function evalString

# Generated at 2026-10-24 11:40:24.591945
# Unit test for function evalString

# Generated at 2026-10-24 11:40:27.012549
# Unit test for function test

# Generated at 2026-10-24 11:40:29.428744
# Unit test for function test

# Generated at 2026-10-24 11:40:31.846388
# Unit test for function test

# Generated at 2026-10-24 11:40:51.798381
# Unit test for function escape

# Generated at 2026-10-24 11:40:59.466303
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-24 11:41:16.866450
# Unit test for function escape

# Generated at 2026-10-24 11:41:19.281832
# Unit test for function escape

# Generated at 2026-10-24 11:41:21.700746
# Unit test for function escape

# Generated at 2026-10-24 11:41:24.118918
# Unit test for function test

# Generated at 2026-10-24 11:41:26.535675
# Unit test for function test

# Generated at 2026-10-24 11:41:28.953367
# Unit test for function test

# Generated at 2026-10-24 11:41:31.375558
# Unit test for function escape

# Generated at 2026-10-24 11:41:33.972386
# Unit test for function escape

# Generated at 2026-10-24 11:41:36.386399
# Unit test for function escape

# Generated at 2026-10-24 11:41:38.807610
# Unit test for function escape

# Generated at 2026-10-24 11:41:41.225733
# Unit test for function escape

# Generated at 2026-10-24 11:41:43.645384
# Unit test for function escape

# Generated at 2026-10-24 11:41:46.062060
# Unit test for function test

# Generated at 2026-10-24 11:41:48.481200
# Unit test for function test

# Generated at 2026-10-24 11:41:50.898660
# Unit test for function test

# Generated at 2026-10-24 11:41:53.315805
# Unit test for function evalString

# Generated at 2026-10-24 11:41:55.733373
# Unit test for function evalString

# Generated at 2026-10-24 11:41:58.150937
# Unit test for function evalString

# Generated at 2026-10-24 11:42:00.571607
# Unit test for function escape

# Generated at 2026-10-24 11:42:02.988029
# Unit test for function escape

# Generated at 2026-10-24 11:42:05.407289
# Unit test for function escape

# Generated at 2026-10-24 11:42:07.821553
# Unit test for function escape

# Generated at 2026-10-24 11:42:10.242277
# Unit test for function escape

# Generated at 2026-10-24 11:42:12.665166
# Unit test for function escape

# Generated at 2026-10-24 11:42:15.083604
# Unit test for function escape

# Generated at 2026-10-24 11:42:17.499216
# Unit test for function escape

# Generated at 2026-10-24 11:42:19.916851
# Unit test for function escape

# Generated at 2026-10-24 11:42:22.335634
# Unit test for function escape

# Generated at 2026-10-24 11:42:24.753194
# Unit test for function escape

# Generated at 2026-10-24 11:42:27.171732
# Unit test for function escape

# Generated at 2026-10-24 11:42:29.591662
# Unit test for function escape

# Generated at 2026-10-24 11:42:32.008112
# Unit test for function escape

# Generated at 2026-10-24 11:42:34.426052
# Unit test for function escape

# Generated at 2026-10-24 11:42:44.151866
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    # module_0.test() prints a line for every character whose round-trip fails;
    # a correct implementation must print nothing.
    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()
    output = buf.getvalue()
    assert output == "", "module_0.test() reported mismatches:\n%s" % output

    # Directly verify the round-trip property for all 256 characters.
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, "round-trip failed: (i=%r, c=%r, s=%r, e=%r)" % (i, c, s, e)

    # Spot-check known escape forms are decoded correctly.
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString("'''a\\nb'''") == "a\nb"

# Generated at 2026-10-24 11:43:04.100973
# Unit test for function escape
def test_escape():
    # 1. Simple escapes: every entry of the table round-trips.
    for tail, expected in simple_escapes.items():
        assert run_escape("\\" + tail) == expected, tail

    # 2. Hex escapes: valid, decoded via chr().
    assert run_escape("\\x41") == "A"
    assert run_escape("\\x7f") == "\x7f"
    assert run_escape("\\xff") == "\xff"

    # 3. Hex escapes: too short -> ValueError.
    for bad in ("\\x", "\\x4"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 4. Hex escapes: non-hex digits -> ValueError.
    try:
        run_escape("\\xzz")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for '\\xzz'")

    # 5. Octal escapes: valid, including 1- and 3-digit forms.
    assert run_escape("\\0") == "\x00"
    assert run_escape("\\101") == "A"
    assert run_escape("\\777") == chr(0o777)

    # 6. Octal escapes: digits outside base 8 -> ValueError.
    for bad in ("\\8", "\\9"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 7. The assert: group(0) must start with a backslash.
    #    Build a match whose group(0) is 'xn' (no backslash).
    m = re.match(r"(x)(n)", "xn")
    assert m is not None
    try:
        module_0.escape(m)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    print("test_escape: all assertions passed")

# Generated at 2026-10-24 11:43:06.523307
# Unit test for function test

# Generated at 2026-10-24 11:43:09.094942
# Unit test for function test

# Generated at 2026-10-24 11:43:11.515498
# Unit test for function test

# Generated at 2026-10-24 11:43:13.938025
# Unit test for function escape

# Generated at 2026-10-24 11:43:16.357225
# Unit test for function escape

# Generated at 2026-10-24 11:43:18.780819
# Unit test for function escape

# Generated at 2026-10-24 11:43:21.195587
# Unit test for function evalString

# Generated at 2026-10-24 11:43:23.615098
# Unit test for function evalString

# Generated at 2026-10-24 11:43:26.029467
# Unit test for function evalString

# Generated at 2026-10-24 11:43:28.445546
# Unit test for function escape

# Generated at 2026-10-24 11:43:30.861508
# Unit test for function escape

# Generated at 2026-10-24 11:43:33.278844
# Unit test for function escape

# Generated at 2026-10-24 11:43:35.692495
# Unit test for function evalString

# Generated at 2026-10-24 11:43:38.110285
# Unit test for function evalString

# Generated at 2026-10-24 11:43:40.527272
# Unit test for function evalString

# Generated at 2026-10-24 11:43:42.945077
# Unit test for function escape

# Generated at 2026-10-24 11:43:45.360654
# Unit test for function escape

# Generated at 2026-10-24 11:43:47.781132
# Unit test for function escape

# Generated at 2026-10-24 11:43:50.197056
# Unit test for function test

# Generated at 2026-10-24 11:43:52.617308
# Unit test for function test

# Generated at 2026-10-24 11:43:55.034186
# Unit test for function test

# Generated at 2026-10-24 11:43:57.452947
# Unit test for function test

# Generated at 2026-10-24 11:43:59.868842
# Unit test for function test

# Generated at 2026-10-24 11:44:02.284848
# Unit test for function test

# Generated at 2026-10-24 11:44:04.699842
# Unit test for function escape

# Generated at 2026-10-24 11:44:06.066021
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-24 11:44:46.238767
# Unit test for function evalString

# Generated at 2026-10-24 11:44:48.663360
# Unit test for function evalString

# Generated at 2026-10-24 11:45:05.677576
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'abc'") == "abc"

# Generated at 2026-10-24 11:45:08.098851
# Unit test for function escape

# Generated at 2026-10-24 11:45:10.521346
# Unit test for function escape

# Generated at 2026-10-24 11:45:12.937925
# Unit test for function escape

# Generated at 2026-10-24 11:45:15.359633
# Unit test for function test

# Generated at 2026-10-24 11:45:17.780651
# Unit test for function test

# Generated at 2026-10-24 11:45:20.198810
# Unit test for function test

# Generated at 2026-10-24 11:45:22.620797
# Unit test for function escape

# Generated at 2026-10-24 11:45:25.038646
# Unit test for function escape

# Generated at 2026-10-24 11:45:27.455997
# Unit test for function escape

# Generated at 2026-10-24 11:45:29.872972
# Unit test for function evalString

# Generated at 2026-10-24 11:45:32.291332
# Unit test for function evalString

# Generated at 2026-10-24 11:45:34.706024
# Unit test for function evalString

# Generated at 2026-10-24 11:45:37.162611
# Unit test for function evalString

# Generated at 2026-10-24 11:45:39.577569
# Unit test for function evalString

# Generated at 2026-10-24 11:45:41.993622
# Unit test for function evalString

# Generated at 2026-10-24 11:45:44.408235
# Unit test for function test

# Generated at 2026-10-24 11:45:46.826132
# Unit test for function test

# Generated at 2026-10-24 11:45:49.244018
# Unit test for function test

# Generated at 2026-10-24 11:45:51.666586
# Unit test for function test

# Generated at 2026-10-24 11:45:54.083079
# Unit test for function test

# Generated at 2026-10-24 11:45:56.499857
# Unit test for function test

# Generated at 2026-10-24 11:45:58.916616
# Unit test for function test

# Generated at 2026-10-24 11:46:01.333951
# Unit test for function test

# Generated at 2026-10-24 11:46:03.750819
# Unit test for function test

# Generated at 2026-10-24 11:46:06.167897
# Unit test for function test

# Generated at 2026-10-24 11:46:08.585576
# Unit test for function test

# Generated at 2026-10-24 11:46:11.003480
# Unit test for function test

# Generated at 2026-10-24 11:46:13.424220
# Unit test for function evalString

# Generated at 2026-10-24 11:46:15.842728
# Unit test for function evalString

# Generated at 2026-10-24 11:46:18.262998
# Unit test for function evalString

# Generated at 2026-10-24 11:46:20.679368
# Unit test for function test

# Generated at 2026-10-24 11:46:23.093269
# Unit test for function test

# Generated at 2026-10-24 11:46:25.509894
# Unit test for function test

# Generated at 2026-10-24 11:46:27.923813
# Unit test for function test

# Generated at 2026-10-24 11:46:30.343031
# Unit test for function test

# Generated at 2026-10-24 11:46:32.757285
# Unit test for function test

# Generated at 2026-10-24 11:46:35.171993
# Unit test for function test

# Generated at 2026-10-24 11:46:37.588476
# Unit test for function test

# Generated at 2026-10-24 11:46:40.006246
# Unit test for function test

# Generated at 2026-10-24 11:46:42.422743
# Unit test for function escape

# Generated at 2026-10-24 11:46:44.841376
# Unit test for function escape

# Generated at 2026-10-24 11:46:47.257178
# Unit test for function escape

# Generated at 2026-10-24 11:46:50.587517
# Unit test for function test

# Generated at 2026-10-24 11:46:53.004284
# Unit test for function test

# Generated at 2026-10-24 11:46:55.420264
# Unit test for function test

# Generated at 2026-10-24 11:46:57.835412
# Unit test for function escape

# Generated at 2026-10-24 11:47:00.249374
# Unit test for function escape

# Generated at 2026-10-24 11:47:02.668537
# Unit test for function escape

# Generated at 2026-10-24 11:47:05.086648
# Unit test for function evalString

# Generated at 2026-10-24 11:47:07.505733
# Unit test for function evalString

# Generated at 2026-10-24 11:47:09.924515
# Unit test for function evalString

# Generated at 2026-10-24 11:47:12.339386
# Unit test for function test

# Generated at 2026-10-24 11:47:14.756788
# Unit test for function test

# Generated at 2026-10-24 11:47:17.171971
# Unit test for function test

# Generated at 2026-10-24 11:47:19.589264
# Unit test for function test

# Generated at 2026-10-24 11:47:22.006303
# Unit test for function test

# Generated at 2026-10-24 11:47:51.842574
# Unit test for function test
def test_test():assert module_0.test() is None

# Generated at 2026-10-24 11:47:54.352360
# Unit test for function test

# Generated at 2026-10-24 11:47:56.769468
# Unit test for function test

# Generated at 2026-10-24 11:47:59.315078
# Unit test for function test

# Generated at 2026-10-24 11:48:01.732215
# Unit test for function escape

# Generated at 2026-10-24 11:48:04.148264
# Unit test for function escape

# Generated at 2026-10-24 11:48:06.566443
# Unit test for function escape

# Generated at 2026-10-24 11:48:08.981982
# Unit test for function escape

# Generated at 2026-10-24 11:48:11.397612
# Unit test for function escape

# Generated at 2026-10-24 11:48:13.818708
# Unit test for function escape

# Generated at 2026-10-24 11:48:16.230299
# Unit test for function test

# Generated at 2026-10-24 11:48:18.647424
# Unit test for function test

# Generated at 2026-10-24 11:48:21.061837
# Unit test for function test

# Generated at 2026-10-24 11:48:23.481044
# Unit test for function escape

# Generated at 2026-10-24 11:48:25.900738
# Unit test for function escape

# Generated at 2026-10-24 11:48:28.326325
# Unit test for function escape

# Generated at 2026-10-24 11:48:34.132909
# Unit test for function escape

# Generated at 2026-10-24 11:48:36.550840
# Unit test for function escape

# Generated at 2026-10-24 11:48:38.970030
# Unit test for function escape

# Generated at 2026-10-24 11:48:41.389594
# Unit test for function test

# Generated at 2026-10-24 11:48:43.809756
# Unit test for function test

# Generated at 2026-10-24 11:48:46.231717
# Unit test for function test

# Generated at 2026-10-24 11:48:49.703251
# Unit test for function evalString

# Generated at 2026-10-24 11:48:51.018657
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'abc'") == "abc"

# Generated at 2026-10-24 11:49:21.137096
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() found mismatches:\n%s" % buf.getvalue()


if __name__ == "__main__":
    test_test()
    print("test_test passed")

# Generated at 2026-10-24 11:49:23.655751
# Unit test for function escape

# Generated at 2026-10-24 11:49:26.165219
# Unit test for function escape

# Generated at 2026-10-24 11:49:28.582606
# Unit test for function escape

# Generated at 2026-10-24 11:49:31.169512
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    # module_0.test() prints a line for every character whose round-trip fails;
    # a correct implementation must print nothing.
    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()
    output = buf.getvalue()
    assert output == "", "module_0.test() reported mismatches:\n%s" % output

    # Directly verify the round-trip property for all 256 characters.
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, "round-trip failed: (i=%r, c=%r, s=%r, e=%r)" % (i, c, s, e)

    # Spot-check known escape forms are decoded correctly.
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString("'''a\\nb'''") == "a\nb"

# Generated at 2026-10-24 11:49:32.487309
# Unit test for function escape
def test_escape():
    # 1. Simple escapes: every entry of the table round-trips.
    for tail, expected in simple_escapes.items():
        assert run_escape("\\" + tail) == expected, tail

    # 2. Hex escapes: valid, decoded via chr().
    assert run_escape("\\x41") == "A"
    assert run_escape("\\x7f") == "\x7f"
    assert run_escape("\\xff") == "\xff"

    # 3. Hex escapes: too short -> ValueError.
    for bad in ("\\x", "\\x4"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 4. Hex escapes: non-hex digits -> ValueError.
    try:
        run_escape("\\xzz")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for '\\xzz'")

    # 5. Octal escapes: valid, including 1- and 3-digit forms.
    assert run_escape("\\0") == "\x00"
    assert run_escape("\\101") == "A"
    assert run_escape("\\777") == chr(0o777)

    # 6. Octal escapes: digits outside base 8 -> ValueError.
    for bad in ("\\8", "\\9"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 7. The assert: group(0) must start with a backslash.
    #    Build a match whose group(0) is 'xn' (no backslash).
    m = re.match(r"(x)(n)", "xn")
    assert m is not None
    try:
        module_0.escape(m)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    print("test_escape: all assertions passed")

# Generated at 2026-10-24 11:49:33.852470
# Unit test for function escape
def test_escape():
    # 1. Simple escapes: every entry of the table round-trips.
    for tail, expected in simple_escapes.items():
        assert run_escape("\\" + tail) == expected, tail

    # 2. Hex escapes: valid, decoded via chr().
    assert run_escape("\\x41") == "A"
    assert run_escape("\\x7f") == "\x7f"
    assert run_escape("\\xff") == "\xff"

    # 3. Hex escapes: too short -> ValueError.
    for bad in ("\\x", "\\x4"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 4. Hex escapes: non-hex digits -> ValueError.
    try:
        run_escape("\\xzz")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for '\\xzz'")

    # 5. Octal escapes: valid, including 1- and 3-digit forms.
    assert run_escape("\\0") == "\x00"
    assert run_escape("\\101") == "A"
    assert run_escape("\\777") == chr(0o777)

    # 6. Octal escapes: digits outside base 8 -> ValueError.
    for bad in ("\\8", "\\9"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 7. The assert: group(0) must start with a backslash.
    #    Build a match whose group(0) is 'xn' (no backslash).
    m = re.match(r"(x)(n)", "xn")
    assert m is not None
    try:
        module_0.escape(m)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    print("test_escape: all assertions passed")

# Generated at 2026-10-24 11:49:35.170449
# Unit test for function escape
def test_escape():
    # 1. Simple escapes: every entry of the table round-trips.
    for tail, expected in simple_escapes.items():
        assert run_escape("\\" + tail) == expected, tail

    # 2. Hex escapes: valid, decoded via chr().
    assert run_escape("\\x41") == "A"
    assert run_escape("\\x7f") == "\x7f"
    assert run_escape("\\xff") == "\xff"

    # 3. Hex escapes: too short -> ValueError.
    for bad in ("\\x", "\\x4"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 4. Hex escapes: non-hex digits -> ValueError.
    try:
        run_escape("\\xzz")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for '\\xzz'")

    # 5. Octal escapes: valid, including 1- and 3-digit forms.
    assert run_escape("\\0") == "\x00"
    assert run_escape("\\101") == "A"
    assert run_escape("\\777") == chr(0o777)

    # 6. Octal escapes: digits outside base 8 -> ValueError.
    for bad in ("\\8", "\\9"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 7. The assert: group(0) must start with a backslash.
    #    Build a match whose group(0) is 'xn' (no backslash).
    m = re.match(r"(x)(n)", "xn")
    assert m is not None
    try:
        module_0.escape(m)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    print("test_escape: all assertions passed")

# Generated at 2026-10-24 11:49:36.548323
# Unit test for function escape
def test_escape():
    # 1. Simple escapes: every entry of the table round-trips.
    for tail, expected in simple_escapes.items():
        assert run_escape("\\" + tail) == expected, tail

    # 2. Hex escapes: valid, decoded via chr().
    assert run_escape("\\x41") == "A"
    assert run_escape("\\x7f") == "\x7f"
    assert run_escape("\\xff") == "\xff"

    # 3. Hex escapes: too short -> ValueError.
    for bad in ("\\x", "\\x4"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 4. Hex escapes: non-hex digits -> ValueError.
    try:
        run_escape("\\xzz")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for '\\xzz'")

    # 5. Octal escapes: valid, including 1- and 3-digit forms.
    assert run_escape("\\0") == "\x00"
    assert run_escape("\\101") == "A"
    assert run_escape("\\777") == chr(0o777)

    # 6. Octal escapes: digits outside base 8 -> ValueError.
    for bad in ("\\8", "\\9"):
        try:
            run_escape(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 7. The assert: group(0) must start with a backslash.
    #    Build a match whose group(0) is 'xn' (no backslash).
    m = re.match(r"(x)(n)", "xn")
    assert m is not None
    try:
        module_0.escape(m)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    print("test_escape: all assertions passed")