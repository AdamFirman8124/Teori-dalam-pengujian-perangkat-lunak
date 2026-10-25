

# Generated at 2026-10-24 12:19:25.641697
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

# Generated at 2026-10-24 12:19:28.066291
# Unit test for function file_name_check

# Generated at 2026-10-24 12:19:30.485189
# Unit test for function file_name_check

# Generated at 2026-10-24 12:19:32.904073
# Unit test for function file_name_check

# Generated at 2026-10-24 12:19:35.326117
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:05.839960
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-24 12:20:07.520462
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

# Generated at 2026-10-24 12:20:08.953703
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

# Generated at 2026-10-24 12:20:10.338151
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

# Generated at 2026-10-24 12:20:11.708144
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

# Generated at 2026-10-24 12:20:13.152440
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

# Generated at 2026-10-24 12:20:14.587761
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

# Generated at 2026-10-24 12:20:16.021986
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

# Generated at 2026-10-24 12:20:17.456261
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

# Generated at 2026-10-24 12:20:18.896536
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

# Generated at 2026-10-24 12:20:21.412693
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:23.920757
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:26.337337
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:28.874700
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:31.292844
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:33.712689
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:36.251270
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:38.670550
# Unit test for function file_name_check

# Generated at 2026-10-24 12:20:56.487700
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-24 12:20:57.864892
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

# Generated at 2026-10-24 12:20:59.337926
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

# Generated at 2026-10-24 12:21:00.752650
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

# Generated at 2026-10-24 12:21:02.154957
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

# Generated at 2026-10-24 12:21:03.513031
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

# Generated at 2026-10-24 12:21:04.969362
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

# Generated at 2026-10-24 12:21:06.403957
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

# Generated at 2026-10-24 12:21:07.938126
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

# Generated at 2026-10-24 12:21:09.312615
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

# Generated at 2026-10-24 12:21:10.808288
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

# Generated at 2026-10-24 12:21:13.558105
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

# Generated at 2026-10-24 12:21:14.971915
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

# Generated at 2026-10-24 12:21:16.407424
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

# Generated at 2026-10-24 12:21:17.874220
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

# Generated at 2026-10-24 12:21:19.304067
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

# Generated at 2026-10-24 12:21:20.673198
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

# Generated at 2026-10-24 12:21:23.195341
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:25.616314
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:28.038265
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:30.453619
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:32.872375
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:35.291210
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:37.709907
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:40.129283
# Unit test for function file_name_check

# Generated at 2026-10-24 12:21:42.545091
# Unit test for function file_name_check

# Generated at 2026-10-24 12:22:03.028626
# Unit test for function file_name_check
def test_file_name_check():# Valid cases
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("Abc.exe") == "Yes"
    assert module_0.file_name_check("a123.txt") == "Yes"      # exactly 3 digits
    assert module_0.file_name_check("x1y2z3.dll") == "Yes"

    # Wrong suffix
    assert module_0.file_name_check("a.pdf") == "No"
    assert module_0.file_name_check("a.TXT") == "No"
    assert module_0.file_name_check("a.tx1") == "No"
    assert module_0.file_name_check("a.txt ") == "No"

    # Dot-count problems
    assert module_0.file_name_check("a") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a..txt") == "No"
    assert module_0.file_name_check("") == "No"

    # Empty name part
    assert module_0.file_name_check(".txt") == "No"

    # First char not a letter
    assert module_0.file_name_check("1a.txt") == "No"
    assert module_0.file_name_check("_a.txt") == "No"

    # Too many digits
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("123.txt") == "No"