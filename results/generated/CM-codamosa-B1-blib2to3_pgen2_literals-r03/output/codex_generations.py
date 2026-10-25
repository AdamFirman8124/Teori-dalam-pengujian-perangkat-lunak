

# Generated at 2026-10-25 03:07:58.990030
# Unit test for function test

# Generated at 2026-10-25 03:08:01.405503
# Unit test for function test

# Generated at 2026-10-25 03:08:03.938085
# Unit test for function test

# Generated at 2026-10-25 03:08:06.359129
# Unit test for function escape

# Generated at 2026-10-25 03:08:08.777588
# Unit test for function escape

# Generated at 2026-10-25 03:08:11.194593
# Unit test for function escape

# Generated at 2026-10-25 03:08:13.780664
# Unit test for function evalString

# Generated at 2026-10-25 03:08:16.195201
# Unit test for function evalString

# Generated at 2026-10-25 03:08:18.607153
# Unit test for function evalString

# Generated at 2026-10-25 03:08:21.021479
# Unit test for function escape

# Generated at 2026-10-25 03:08:23.437379
# Unit test for function escape

# Generated at 2026-10-25 03:08:25.850761
# Unit test for function escape

# Generated at 2026-10-25 03:08:28.268711
# Unit test for function escape

# Generated at 2026-10-25 03:08:30.687520
# Unit test for function escape

# Generated at 2026-10-25 03:08:33.101747
# Unit test for function escape

# Generated at 2026-10-25 03:08:35.517611
# Unit test for function test

# Generated at 2026-10-25 03:08:37.931909
# Unit test for function test

# Generated at 2026-10-25 03:08:40.346802
# Unit test for function test

# Generated at 2026-10-25 03:08:42.758702
# Unit test for function evalString

# Generated at 2026-10-25 03:08:45.171721
# Unit test for function evalString

# Generated at 2026-10-25 03:08:47.587244
# Unit test for function evalString

# Generated at 2026-10-25 03:08:50.003200
# Unit test for function escape

# Generated at 2026-10-25 03:08:52.419333
# Unit test for function escape

# Generated at 2026-10-25 03:08:54.836352
# Unit test for function escape

# Generated at 2026-10-25 03:08:57.257174
# Unit test for function escape

# Generated at 2026-10-25 03:08:59.671992
# Unit test for function escape

# Generated at 2026-10-25 03:09:02.086697
# Unit test for function escape

# Generated at 2026-10-25 03:09:04.500311
# Unit test for function evalString

# Generated at 2026-10-25 03:09:06.916346
# Unit test for function evalString

# Generated at 2026-10-25 03:09:09.334093
# Unit test for function evalString

# Generated at 2026-10-25 03:09:11.748195
# Unit test for function evalString

# Generated at 2026-10-25 03:09:14.161534
# Unit test for function evalString

# Generated at 2026-10-25 03:09:16.578042
# Unit test for function evalString

# Generated at 2026-10-25 03:09:18.992672
# Unit test for function escape

# Generated at 2026-10-25 03:09:21.408984
# Unit test for function escape

# Generated at 2026-10-25 03:09:23.824481
# Unit test for function escape

# Generated at 2026-10-25 03:09:26.240409
# Unit test for function escape

# Generated at 2026-10-25 03:09:28.656146
# Unit test for function escape

# Generated at 2026-10-25 03:09:31.071634
# Unit test for function escape

# Generated at 2026-10-25 03:09:33.488911
# Unit test for function evalString

# Generated at 2026-10-25 03:09:35.905895
# Unit test for function evalString

# Generated at 2026-10-25 03:09:38.321914
# Unit test for function evalString

# Generated at 2026-10-25 03:09:40.736920
# Unit test for function test

# Generated at 2026-10-25 03:09:43.150298
# Unit test for function test

# Generated at 2026-10-25 03:09:45.566855
# Unit test for function test

# Generated at 2026-10-25 03:09:48.835291
# Unit test for function escape

# Generated at 2026-10-25 03:09:51.250747
# Unit test for function escape

# Generated at 2026-10-25 03:09:53.665962
# Unit test for function escape

# Generated at 2026-10-25 03:09:56.079565
# Unit test for function escape

# Generated at 2026-10-25 03:09:58.495063
# Unit test for function escape

# Generated at 2026-10-25 03:10:00.910920
# Unit test for function escape

# Generated at 2026-10-25 03:10:03.324750
# Unit test for function evalString

# Generated at 2026-10-25 03:10:05.739160
# Unit test for function evalString

# Generated at 2026-10-25 03:10:08.154022
# Unit test for function evalString

# Generated at 2026-10-25 03:10:10.569421
# Unit test for function escape

# Generated at 2026-10-25 03:10:12.984378
# Unit test for function escape

# Generated at 2026-10-25 03:10:15.398413
# Unit test for function escape

# Generated at 2026-10-25 03:10:17.813869
# Unit test for function evalString

# Generated at 2026-10-25 03:10:20.228020
# Unit test for function evalString

# Generated at 2026-10-25 03:10:26.644523
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'hello'") == "hello"

# Generated at 2026-10-25 03:10:36.692359
# Unit test for function test

# Generated at 2026-10-25 03:10:45.551681
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 03:11:10.403290
# Unit test for function evalString
def test_evalString():import pytest


def test_evalString() -> None:
    # Plain and empty strings.
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello"') == "hello"

    # Triple-quoted strings.
    assert module_0.evalString("'''hello\nworld'''") == "hello\nworld"
    assert module_0.evalString('"""hello\nworld"""') == "hello\nworld"

    # Simple escapes.
    for tail, expected in simple_escapes.items():
        literal = "'" + "\\" + tail + "'"
        assert module_0.evalString(literal) == expected

    # Hexadecimal and octal escapes.
    assert module_0.evalString(r"'\x41'") == "A"
    assert module_0.evalString(r"'\101'") == "A"
    assert module_0.evalString(r"'\x414'") == "A4"
    assert module_0.evalString(r"'\777'") == chr(0o777)

    # Unknown escapes are preserved.
    assert module_0.evalString(r"'\q'") == r"\q"

    # Every character representable by one byte.
    for value in range(256):
        character = chr(value)
        assert module_0.evalString(repr(character)) == character

    # Invalid hexadecimal escapes.
    for literal in (r"'\x'", r"'\x1'", r"'\xGG'", r"'\x4G'"):
        with pytest.raises(ValueError, match="invalid hex string escape"):
            module_0.evalString(literal)

    # Missing or mismatched delimiters.
    for literal in ("", "hello", "'unterminated", "'''unterminated'"):
        with pytest.raises(AssertionError):
            module_0.evalString(literal)

# Generated at 2026-10-25 03:11:12.819868
# Unit test for function test

# Generated at 2026-10-25 03:11:15.237360
# Unit test for function test

# Generated at 2026-10-25 03:11:17.814288
# Unit test for function test

# Generated at 2026-10-25 03:11:20.229729
# Unit test for function escape

# Generated at 2026-10-25 03:11:22.648384
# Unit test for function escape

# Generated at 2026-10-25 03:11:25.061530
# Unit test for function escape

# Generated at 2026-10-25 03:11:27.476818
# Unit test for function escape

# Generated at 2026-10-25 03:11:29.891336
# Unit test for function escape

# Generated at 2026-10-25 03:11:32.305597
# Unit test for function escape

# Generated at 2026-10-25 03:11:45.013733
# Unit test for function escape

# Generated at 2026-10-25 03:11:49.109711
# Unit test for function escape
def test_escape():match = re.match(r"\\(n)", r"\n")

# Generated at 2026-10-25 03:11:57.511954
# Unit test for function test

# Generated at 2026-10-25 03:11:58.860799
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 03:12:01.280117
# Unit test for function test

# Generated at 2026-10-25 03:12:03.698051
# Unit test for function test

# Generated at 2026-10-25 03:12:06.238292
# Unit test for function test

# Generated at 2026-10-25 03:12:08.652984
# Unit test for function escape

# Generated at 2026-10-25 03:12:11.212254
# Unit test for function escape

# Generated at 2026-10-25 03:12:13.627824
# Unit test for function escape

# Generated at 2026-10-25 03:12:16.043648
# Unit test for function test

# Generated at 2026-10-25 03:12:18.458072
# Unit test for function test

# Generated at 2026-10-25 03:12:20.873314
# Unit test for function test

# Generated at 2026-10-25 03:12:23.289748
# Unit test for function test

# Generated at 2026-10-25 03:12:25.704472
# Unit test for function test

# Generated at 2026-10-25 03:12:28.120969
# Unit test for function test

# Generated at 2026-10-25 03:12:30.534605
# Unit test for function escape

# Generated at 2026-10-25 03:12:32.949901
# Unit test for function escape

# Generated at 2026-10-25 03:12:35.364171
# Unit test for function escape

# Generated at 2026-10-25 03:12:37.783021
# Unit test for function escape

# Generated at 2026-10-25 03:12:40.197240
# Unit test for function escape

# Generated at 2026-10-25 03:12:42.612491
# Unit test for function escape

# Generated at 2026-10-25 03:12:45.028773
# Unit test for function escape

# Generated at 2026-10-25 03:12:47.445408
# Unit test for function escape

# Generated at 2026-10-25 03:12:49.857913
# Unit test for function escape

# Generated at 2026-10-25 03:13:03.334857
# Unit test for function escape

# Generated at 2026-10-25 03:13:08.162605
# Unit test for function escape
def test_escape():simple_match = re.fullmatch(r"\\(.*)", r"\n")

# Generated at 2026-10-25 03:13:11.885111
# Unit test for function escape

# Generated at 2026-10-25 03:13:14.299404
# Unit test for function escape

# Generated at 2026-10-25 03:13:16.714588
# Unit test for function escape

# Generated at 2026-10-25 03:13:19.128693
# Unit test for function escape

# Generated at 2026-10-25 03:13:21.702768
# Unit test for function escape

# Generated at 2026-10-25 03:13:24.116682
# Unit test for function escape

# Generated at 2026-10-25 03:13:26.530777
# Unit test for function escape

# Generated at 2026-10-25 03:13:28.951043
# Unit test for function escape

# Generated at 2026-10-25 03:13:31.369213
# Unit test for function escape

# Generated at 2026-10-25 03:13:33.790870
# Unit test for function escape

# Generated at 2026-10-25 03:13:36.205338
# Unit test for function escape

# Generated at 2026-10-25 03:13:38.621182
# Unit test for function escape

# Generated at 2026-10-25 03:13:41.035122
# Unit test for function test

# Generated at 2026-10-25 03:13:43.451887
# Unit test for function test

# Generated at 2026-10-25 03:13:45.865796
# Unit test for function test

# Generated at 2026-10-25 03:13:48.280142
# Unit test for function escape

# Generated at 2026-10-25 03:13:50.695477
# Unit test for function escape

# Generated at 2026-10-25 03:13:53.588966
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-10-25 03:14:03.564743
# Unit test for function escape

# Generated at 2026-10-25 03:14:08.989380
# Unit test for function escape
def test_escape():match = re.fullmatch(r"\\(x41)", r"\x41")

# Generated at 2026-10-25 03:14:18.819542
# Unit test for function escape

# Generated at 2026-10-25 03:14:21.236179
# Unit test for function escape

# Generated at 2026-10-25 03:14:23.653881
# Unit test for function escape

# Generated at 2026-10-25 03:14:26.065027
# Unit test for function test

# Generated at 2026-10-25 03:14:28.479798
# Unit test for function test

# Generated at 2026-10-25 03:14:30.897920
# Unit test for function test

# Generated at 2026-10-25 03:14:33.308477
# Unit test for function test

# Generated at 2026-10-25 03:14:35.722589
# Unit test for function test

# Generated at 2026-10-25 03:14:38.137152
# Unit test for function test

# Generated at 2026-10-25 03:14:44.048635
# Unit test for function test

# Generated at 2026-10-25 03:14:46.462984
# Unit test for function test

# Generated at 2026-10-25 03:14:48.877627
# Unit test for function test

# Generated at 2026-10-25 03:14:51.292054
# Unit test for function escape

# Generated at 2026-10-25 03:14:53.707482
# Unit test for function escape

# Generated at 2026-10-25 03:14:56.123295
# Unit test for function escape

# Generated at 2026-10-25 03:14:58.537045
# Unit test for function escape

# Generated at 2026-10-25 03:15:00.951973
# Unit test for function escape

# Generated at 2026-10-25 03:15:03.366472
# Unit test for function escape

# Generated at 2026-10-25 03:15:05.780775
# Unit test for function test

# Generated at 2026-10-25 03:15:08.195144
# Unit test for function test

# Generated at 2026-10-25 03:15:10.609304
# Unit test for function test

# Generated at 2026-10-25 03:15:13.023504
# Unit test for function test

# Generated at 2026-10-25 03:15:15.442477
# Unit test for function test

# Generated at 2026-10-25 03:15:17.858162
# Unit test for function test

# Generated at 2026-10-25 03:15:20.272172
# Unit test for function escape

# Generated at 2026-10-25 03:15:22.687979
# Unit test for function escape

# Generated at 2026-10-25 03:15:25.102118
# Unit test for function escape

# Generated at 2026-10-25 03:15:27.517691
# Unit test for function escape

# Generated at 2026-10-25 03:15:29.934897
# Unit test for function escape

# Generated at 2026-10-25 03:15:32.349390
# Unit test for function escape

# Generated at 2026-10-25 03:15:34.764043
# Unit test for function test

# Generated at 2026-10-25 03:15:36.536435
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 03:15:48.977684
# Unit test for function escape

# Generated at 2026-10-25 03:15:53.539441
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(n)", r"\n")) == "\n"

# Generated at 2026-10-25 03:16:03.366945
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()
    with redirect_stdout(output):
        module_0.test()

    assert output.getvalue() == ""

# Generated at 2026-10-25 03:16:21.090163
# Unit test for function escape

# Generated at 2026-10-25 03:16:26.224970
# Unit test for function escape
def test_escape():match = re.match(r"\\(n)", r"\n")

# Generated at 2026-10-25 03:16:37.675805
# Unit test for function escape

# Generated at 2026-10-25 03:16:40.096007
# Unit test for function escape

# Generated at 2026-10-25 03:16:42.511057
# Unit test for function escape

# Generated at 2026-10-25 03:16:53.225126
# Unit test for function escape

# Generated at 2026-10-25 03:16:59.383519
# Unit test for function escape
def test_escape():match = re.fullmatch(r"\\(.*)", r"\n")

# Generated at 2026-10-25 03:17:07.276430
# Unit test for function escape

# Generated at 2026-10-25 03:17:11.879830
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-25 03:17:18.636835
# Unit test for function test

# Generated at 2026-10-25 03:17:21.055627
# Unit test for function test

# Generated at 2026-10-25 03:17:23.471752
# Unit test for function test

# Generated at 2026-10-25 03:17:25.890317
# Unit test for function escape

# Generated at 2026-10-25 03:17:28.309249
# Unit test for function escape

# Generated at 2026-10-25 03:17:30.722859
# Unit test for function escape

# Generated at 2026-10-25 03:17:33.138589
# Unit test for function test

# Generated at 2026-10-25 03:17:35.557426
# Unit test for function test

# Generated at 2026-10-25 03:17:37.970142
# Unit test for function test

# Generated at 2026-10-25 03:17:40.387888
# Unit test for function escape

# Generated at 2026-10-25 03:17:42.816859
# Unit test for function escape

# Generated at 2026-10-25 03:17:45.231485
# Unit test for function escape

# Generated at 2026-10-25 03:17:47.643663
# Unit test for function escape

# Generated at 2026-10-25 03:17:50.058613
# Unit test for function escape

# Generated at 2026-10-25 03:17:52.470584
# Unit test for function escape

# Generated at 2026-10-25 03:17:54.892198
# Unit test for function escape

# Generated at 2026-10-25 03:17:57.306219
# Unit test for function escape

# Generated at 2026-10-25 03:17:59.720127
# Unit test for function escape