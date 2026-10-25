

# Generated at 2026-10-24 21:08:52.209195
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:08:53.567887
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:08:54.921838
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:08:56.271164
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:08:57.681409
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:08:59.038164
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:09:01.562431
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:04.093810
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:06.610332
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:09.028700
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:11.441334
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:14.024711
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:16.442049
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:18.863347
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:21.277006
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:23.696639
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:26.111691
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:28.529980
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:30.941845
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:33.365619
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:35.778800
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:38.198984
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:40.615000
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:43.031314
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:45.450501
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:47.869703
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:50.286994
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:52.705102
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:55.122063
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:57.539726
# Unit test for function file_name_check

# Generated at 2026-10-24 21:09:59.957836
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:02.374321
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:04.794615
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:07.206989
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:09.623666
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:12.043104
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:14.457428
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:16.874394
# Unit test for function file_name_check

# Generated at 2026-10-24 21:10:20.500115
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-24 21:10:21.920320
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:23.354009
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:24.788831
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:26.151629
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:27.553928
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:28.986490
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:30.426312
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:31.808678
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:33.223550
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:34.623357
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:35.978564
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:52.921171
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"
    assert module_0.file_name_check("abc123.exe") == "Yes"
    assert module_0.file_name_check("example.pdf") == "No"
    assert file

# Generated at 2026-10-24 21:10:54.382605
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:55.815638
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:57.203746
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:10:58.683803
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:00.116379
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:01.549899
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:02.984477
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:04.419269
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:05.850483
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:08.394846
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:10.809628
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:13.228974
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:15.645264
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:18.063043
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:20.657975
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:23.075339
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:25.492546
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:27.908674
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:30.326560
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:32.744711
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:35.159702
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:37.577541
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:39.993206
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:42.407982
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:44.824511
# Unit test for function file_name_check

# Generated at 2026-10-24 21:11:49.343893
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-24 21:11:50.693765
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:52.043484
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:53.467697
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:54.901542
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:56.263996
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:57.668484
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:11:59.033389
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:00.434397
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:01.863645
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:03.225460
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:04.629046
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:07.189345
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:08.558316
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:10.055841
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:11.489672
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:12.841965
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:14.222232
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:15.687647
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:12:18.106965
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:20.526451
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:23.087883
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:25.507667
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:27.922992
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:30.342909
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:32.760230
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:35.175308
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:37.738671
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:40.557535
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:42.975157
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:45.392900
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:47.808416
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:50.227305
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:52.641759
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:55.061868
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:57.479481
# Unit test for function file_name_check

# Generated at 2026-10-24 21:12:59.896957
# Unit test for function file_name_check

# Generated at 2026-10-24 21:13:02.314471
# Unit test for function file_name_check

# Generated at 2026-10-24 21:13:04.731965
# Unit test for function file_name_check

# Generated at 2026-10-24 21:13:07.153086
# Unit test for function file_name_check

# Generated at 2026-10-24 21:13:09.755277
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"
    assert module_0.file_name_check("abc123.exe") == "Yes"
    assert module_0.file_name_check("example.pdf") == "No"
    assert file

# Generated at 2026-10-24 21:13:11.192088
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:13:12.625733
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:13:13.985009
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:13:15.394125
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 21:13:16.820867
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"