

# Generated at 2026-10-25 04:21:48.790626
# Unit test for function evalString

# Generated at 2026-10-25 04:21:51.214615
# Unit test for function evalString

# Generated at 2026-10-25 04:21:53.630224
# Unit test for function evalString

# Generated at 2026-10-25 04:21:56.170180
# Unit test for function evalString

# Generated at 2026-10-25 04:21:58.591931
# Unit test for function evalString

# Generated at 2026-10-25 04:22:01.010323
# Unit test for function evalString

# Generated at 2026-10-25 04:22:03.425541
# Unit test for function test

# Generated at 2026-10-25 04:22:05.844165
# Unit test for function test

# Generated at 2026-10-25 04:22:08.255520
# Unit test for function test

# Generated at 2026-10-25 04:22:10.680580
# Unit test for function escape

# Generated at 2026-10-25 04:22:13.096577
# Unit test for function escape

# Generated at 2026-10-25 04:22:15.691243
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-10-25 04:22:35.457828
# Unit test for function evalString

# Generated at 2026-10-25 04:22:42.334310
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'hello'") == "hello"

# Generated at 2026-10-25 04:22:52.424179
# Unit test for function escape

# Generated at 2026-10-25 04:22:57.837798
# Unit test for function escape
def test_escape():match = re.fullmatch(r"\\(n)", r"\n")

# Generated at 2026-10-25 04:23:00.254964
# Unit test for function escape

# Generated at 2026-10-25 04:23:02.669972
# Unit test for function escape

# Generated at 2026-10-25 04:23:05.083802
# Unit test for function escape

# Generated at 2026-10-25 04:23:07.662052
# Unit test for function escape

# Generated at 2026-10-25 04:23:10.076480
# Unit test for function escape

# Generated at 2026-10-25 04:23:12.493313
# Unit test for function escape

# Generated at 2026-10-25 04:23:14.907009
# Unit test for function evalString

# Generated at 2026-10-25 04:23:21.737343
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'hello\\nworld'") == "hello\nworld"

# Generated at 2026-10-25 04:23:36.790582
# Unit test for function escape

# Generated at 2026-10-25 04:23:40.682577
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-25 04:23:50.978826
# Unit test for function escape

# Generated at 2026-10-25 04:23:55.466408
# Unit test for function escape
def test_escape():match = re.match(r"\\(x[0-9A-Fa-f]{2})", r"\x41")

# Generated at 2026-10-25 04:23:57.895390
# Unit test for function escape

# Generated at 2026-10-25 04:24:00.420120
# Unit test for function escape

# Generated at 2026-10-25 04:24:02.836845
# Unit test for function escape

# Generated at 2026-10-25 04:24:05.250655
# Unit test for function escape

# Generated at 2026-10-25 04:24:07.841389
# Unit test for function escape

# Generated at 2026-10-25 04:24:10.256765
# Unit test for function escape

# Generated at 2026-10-25 04:24:12.673951
# Unit test for function evalString

# Generated at 2026-10-25 04:24:15.264432
# Unit test for function evalString

# Generated at 2026-10-25 04:24:17.683210
# Unit test for function evalString

# Generated at 2026-10-25 04:24:20.099402
# Unit test for function escape

# Generated at 2026-10-25 04:24:22.515033
# Unit test for function escape

# Generated at 2026-10-25 04:24:24.933168
# Unit test for function escape

# Generated at 2026-10-25 04:24:27.347990
# Unit test for function escape

# Generated at 2026-10-25 04:24:29.764621
# Unit test for function escape

# Generated at 2026-10-25 04:24:32.179716
# Unit test for function escape

# Generated at 2026-10-25 04:24:34.594430
# Unit test for function escape

# Generated at 2026-10-25 04:24:37.009300
# Unit test for function escape

# Generated at 2026-10-25 04:24:39.423983
# Unit test for function escape

# Generated at 2026-10-25 04:24:41.837046
# Unit test for function escape

# Generated at 2026-10-25 04:24:44.252480
# Unit test for function escape

# Generated at 2026-10-25 04:24:46.667095
# Unit test for function escape

# Generated at 2026-10-25 04:24:49.081659
# Unit test for function escape

# Generated at 2026-10-25 04:24:51.498836
# Unit test for function escape

# Generated at 2026-10-25 04:24:53.910064
# Unit test for function escape

# Generated at 2026-10-25 04:24:56.324771
# Unit test for function test

# Generated at 2026-10-25 04:24:58.743079
# Unit test for function test

# Generated at 2026-10-25 04:25:01.154773
# Unit test for function test

# Generated at 2026-10-25 04:25:03.571532
# Unit test for function test

# Generated at 2026-10-25 04:25:05.985635
# Unit test for function test

# Generated at 2026-10-25 04:25:08.403584
# Unit test for function test

# Generated at 2026-10-25 04:25:10.818890
# Unit test for function test

# Generated at 2026-10-25 04:25:13.233131
# Unit test for function test

# Generated at 2026-10-25 04:25:15.648592
# Unit test for function test

# Generated at 2026-10-25 04:25:18.065246
# Unit test for function evalString

# Generated at 2026-10-25 04:25:24.003220
# Unit test for function evalString
def test_evalString():assert module_0.evalString(r"'hello\nworld'") == "hello\nworld"

# Generated at 2026-10-25 04:25:43.871264
# Unit test for function evalString

# Generated at 2026-10-25 04:25:49.708121
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'hello'") == "hello"

# Generated at 2026-10-25 04:25:59.788772
# Unit test for function escape
def test_escape():cases = {
        r"\a": "\a",
        r"\b": "\b",
        r"\f": "\f",
        r"\n": "\n",
        r"\r": "\r",
        r"\t": "\t",
        r"\v": "\v",
        r"\'": "'",
        r"\"": '"',
        r"\\": "\\",
        r"\x00": "\x00",
        r"\x41": "A",
        r"\xff": "\xff",
        r"\0": "\0",
        r"\7": "\7",
        r"\101": "A",
        r"\377": "\xff",
    }


# Generated at 2026-10-25 04:26:09.630536
# Unit test for function test

# Generated at 2026-10-25 04:26:12.354277
# Unit test for function test

# Generated at 2026-10-25 04:26:14.777654
# Unit test for function test

# Generated at 2026-10-25 04:26:17.189032
# Unit test for function escape

# Generated at 2026-10-25 04:26:19.603736
# Unit test for function escape

# Generated at 2026-10-25 04:26:22.017434
# Unit test for function escape

# Generated at 2026-10-25 04:26:33.739031
# Unit test for function escape

# Generated at 2026-10-25 04:26:38.141824
# Unit test for function escape
def test_escape():match = re.fullmatch(r"\\(x.{2})", r"\x41")

# Generated at 2026-10-25 04:26:48.894738
# Unit test for function escape

# Generated at 2026-10-25 04:26:51.311495
# Unit test for function escape

# Generated at 2026-10-25 04:26:53.726381
# Unit test for function escape

# Generated at 2026-10-25 04:26:56.289389
# Unit test for function escape

# Generated at 2026-10-25 04:26:58.704350
# Unit test for function escape

# Generated at 2026-10-25 04:27:01.118387
# Unit test for function escape

# Generated at 2026-10-25 04:27:03.534939
# Unit test for function test

# Generated at 2026-10-25 04:27:05.950464
# Unit test for function test

# Generated at 2026-10-25 04:27:08.365692
# Unit test for function test

# Generated at 2026-10-25 04:27:10.779848
# Unit test for function escape

# Generated at 2026-10-25 04:27:13.194641
# Unit test for function escape

# Generated at 2026-10-25 04:27:15.609253
# Unit test for function escape

# Generated at 2026-10-25 04:27:18.030507
# Unit test for function test

# Generated at 2026-10-25 04:27:20.450384
# Unit test for function test

# Generated at 2026-10-25 04:27:22.865618
# Unit test for function test

# Generated at 2026-10-25 04:27:25.281040
# Unit test for function evalString

# Generated at 2026-10-25 04:27:27.697770
# Unit test for function evalString

# Generated at 2026-10-25 04:27:30.114408
# Unit test for function evalString

# Generated at 2026-10-25 04:27:32.528199
# Unit test for function test

# Generated at 2026-10-25 04:27:34.946493
# Unit test for function test

# Generated at 2026-10-25 04:27:36.345030
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 04:27:49.900441
# Unit test for function escape

# Generated at 2026-10-25 04:27:54.922656
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-25 04:28:03.479826
# Unit test for function escape

# Generated at 2026-10-25 04:28:05.896294
# Unit test for function escape

# Generated at 2026-10-25 04:28:08.310677
# Unit test for function escape

# Generated at 2026-10-25 04:28:10.725659
# Unit test for function escape

# Generated at 2026-10-25 04:28:13.140112
# Unit test for function escape

# Generated at 2026-10-25 04:28:15.554358
# Unit test for function escape

# Generated at 2026-10-25 04:28:17.968281
# Unit test for function escape

# Generated at 2026-10-25 04:28:20.383158
# Unit test for function escape

# Generated at 2026-10-25 04:28:22.798560
# Unit test for function escape

# Generated at 2026-10-25 04:28:25.212281
# Unit test for function escape

# Generated at 2026-10-25 04:28:27.627467
# Unit test for function escape

# Generated at 2026-10-25 04:28:30.041718
# Unit test for function escape

# Generated at 2026-10-25 04:28:32.456698
# Unit test for function escape

# Generated at 2026-10-25 04:28:34.875247
# Unit test for function escape

# Generated at 2026-10-25 04:28:37.291590
# Unit test for function escape

# Generated at 2026-10-25 04:28:43.087886
# Unit test for function test

# Generated at 2026-10-25 04:28:44.504939
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 04:28:51.133150
# Unit test for function test

# Generated at 2026-10-25 04:28:52.463023
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 04:29:03.740258
# Unit test for function escape

# Generated at 2026-10-25 04:29:07.851309
# Unit test for function escape
def test_escape():match = re.fullmatch(r"\\(x41)", r"\x41")

# Generated at 2026-10-25 04:29:10.270589
# Unit test for function evalString

# Generated at 2026-10-25 04:29:12.689337
# Unit test for function evalString

# Generated at 2026-10-25 04:29:16.560873
# Unit test for function evalString

# Generated at 2026-10-25 04:29:19.746548
# Unit test for function evalString

# Generated at 2026-10-25 04:29:22.159754
# Unit test for function evalString

# Generated at 2026-10-25 04:29:24.574053
# Unit test for function evalString

# Generated at 2026-10-25 04:29:26.988072
# Unit test for function test

# Generated at 2026-10-25 04:29:29.403484
# Unit test for function test

# Generated at 2026-10-25 04:29:31.828962
# Unit test for function test

# Generated at 2026-10-25 04:29:34.235098
# Unit test for function evalString

# Generated at 2026-10-25 04:29:36.650951
# Unit test for function evalString

# Generated at 2026-10-25 04:29:39.069309
# Unit test for function evalString

# Generated at 2026-10-25 04:29:45.199589
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 04:29:53.552074
# Unit test for function test

# Generated at 2026-10-25 04:29:54.880080
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 04:30:06.834289
# Unit test for function escape

# Generated at 2026-10-25 04:30:09.264957
# Unit test for function escape

# Generated at 2026-10-25 04:30:11.784113
# Unit test for function escape

# Generated at 2026-10-25 04:30:14.311107
# Unit test for function escape

# Generated at 2026-10-25 04:30:16.726524
# Unit test for function escape

# Generated at 2026-10-25 04:30:19.143189
# Unit test for function escape

# Generated at 2026-10-25 04:30:21.554715
# Unit test for function test

# Generated at 2026-10-25 04:30:23.970422
# Unit test for function test

# Generated at 2026-10-25 04:30:26.385298
# Unit test for function test

# Generated at 2026-10-25 04:30:28.800865
# Unit test for function escape

# Generated at 2026-10-25 04:30:31.211009
# Unit test for function escape

# Generated at 2026-10-25 04:30:33.626360
# Unit test for function escape

# Generated at 2026-10-25 04:30:36.042525
# Unit test for function escape

# Generated at 2026-10-25 04:30:38.456796
# Unit test for function escape

# Generated at 2026-10-25 04:30:40.879349
# Unit test for function escape

# Generated at 2026-10-25 04:30:49.204796
# Unit test for function escape

# Generated at 2026-10-25 04:30:51.620086
# Unit test for function escape

# Generated at 2026-10-25 04:30:54.036786
# Unit test for function escape

# Generated at 2026-10-25 04:30:56.448569
# Unit test for function evalString

# Generated at 2026-10-25 04:30:58.865258
# Unit test for function evalString

# Generated at 2026-10-25 04:31:01.282303
# Unit test for function evalString

# Generated at 2026-10-25 04:31:03.704378
# Unit test for function escape

# Generated at 2026-10-25 04:31:06.115049
# Unit test for function escape

# Generated at 2026-10-25 04:31:08.530617
# Unit test for function escape

# Generated at 2026-10-25 04:31:20.563188
# Unit test for function escape

# Generated at 2026-10-25 04:31:25.375161
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-25 04:31:44.834046
# Unit test for function evalString
def test_evalString():
    import pytest

    # Empty and ordinary strings
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""
    assert module_0.evalString("'hello world'") == "hello world"
    assert module_0.evalString('"hello world"') == "hello world"

    # Triple-quoted strings
    assert module_0.evalString("'''line 1\nline 2'''") == "line 1\nline 2"
    assert module_0.evalString('"""line 1\nline 2"""') == "line 1\nline 2"

    # Quotes and simple escape sequences
    assert module_0.evalString(r"'it\'s valid'") == "it's valid"
    assert module_0.evalString(r'"say \""') == 'say "'
    assert module_0.evalString(r"'\a\b\f\n\r\t\v\\'") == (
        "\a\b\f\n\r\t\v\\"
    )

    # Hexadecimal and octal escapes
    assert module_0.evalString(r"'\x48\x65\x6c\x6c\x6f'") == "Hello"
    assert module_0.evalString(r"'\101\102\103'") == "ABC"
    assert module_0.evalString(r"'\0\07\377'") == "\0\07\xff"

    # Unknown escapes are preserved
    assert module_0.evalString(r"'\q'") == r"\q"
    assert module_0.evalString(r"'\8'") == r"\8"

    # Every single-byte character should round-trip through repr().
    for value in range(256):
        character = chr(value)
        assert module_0.evalString(repr(character)) == character

    # Malformed hexadecimal escapes
    for literal in (r"'\x'", r"'\x1'", r"'\xGG'"):
        with pytest.raises(ValueError, match="invalid hex string escape"):
            module_0.evalString(literal)

    # Invalid or mismatched delimiters
    for literal in ("unquoted", "'mismatched\"", "'''incomplete'"):
        with pytest.raises(AssertionError):
            module_0.evalString(literal)

# Generated at 2026-10-25 04:31:55.788574
# Unit test for function escape

# Generated at 2026-10-25 04:31:58.206042
# Unit test for function escape