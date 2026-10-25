

# Generated at 2026-10-24 21:36:54.902889
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

# Generated at 2026-10-24 21:36:56.279381
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

# Generated at 2026-10-24 21:36:57.734618
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

# Generated at 2026-10-24 21:36:59.164808
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

# Generated at 2026-10-24 21:37:01.858483
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:04.389743
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:06.814617
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:09.391107
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:11.918962
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:14.338931
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:16.906286
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:19.326050
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:21.743692
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:24.163251
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:26.581795
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:29.000212
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:31.426683
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:35.982576
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-24 21:37:37.346702
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

# Generated at 2026-10-24 21:37:38.710179
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

# Generated at 2026-10-24 21:37:40.074565
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

# Generated at 2026-10-24 21:37:41.443872
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

# Generated at 2026-10-24 21:37:42.827119
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

# Generated at 2026-10-24 21:37:44.235800
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

# Generated at 2026-10-24 21:37:45.593122
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

# Generated at 2026-10-24 21:37:46.984780
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

# Generated at 2026-10-24 21:37:48.347707
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

# Generated at 2026-10-24 21:37:49.748657
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

# Generated at 2026-10-24 21:37:51.183103
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

# Generated at 2026-10-24 21:37:52.589994
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

# Generated at 2026-10-24 21:37:55.089992
# Unit test for function file_name_check

# Generated at 2026-10-24 21:37:57.609128
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:00.023962
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:02.442143
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:05.021756
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:07.438740
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:09.857780
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:12.274767
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:14.691768
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:17.112600
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:19.536639
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:21.958105
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:24.375223
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:26.792361
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:29.213923
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:31.633795
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:34.050203
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:36.467242
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:38.885520
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:41.306603
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:43.723687
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:46.140718
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:48.558225
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:50.975288
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:53.394110
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:55.811027
# Unit test for function file_name_check

# Generated at 2026-10-24 21:38:58.230697
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:00.644936
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:03.064547
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:05.480680
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:07.901080
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:17.185867
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("file.txt") == 'Yes'

# Generated at 2026-10-24 21:39:18.559465
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

# Generated at 2026-10-24 21:39:19.912951
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

# Generated at 2026-10-24 21:39:21.267609
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

# Generated at 2026-10-24 21:39:22.638728
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

# Generated at 2026-10-24 21:39:24.006645
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

# Generated at 2026-10-24 21:39:25.354628
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

# Generated at 2026-10-24 21:39:26.716185
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

# Generated at 2026-10-24 21:39:28.066619
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

# Generated at 2026-10-24 21:39:29.488265
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

# Generated at 2026-10-24 21:39:30.843279
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

# Generated at 2026-10-24 21:39:32.224929
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

# Generated at 2026-10-24 21:39:34.742756
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:37.160179
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:39.577156
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:41.995196
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:44.413656
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:46.830018
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:50.035615
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:52.452136
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:54.870349
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:57.285842
# Unit test for function file_name_check

# Generated at 2026-10-24 21:39:59.701890
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:02.117997
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:04.533320
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:06.950256
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:09.367558
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:10.779531
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

# Generated at 2026-10-24 21:40:12.181796
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

# Generated at 2026-10-24 21:40:13.538364
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

# Generated at 2026-10-24 21:40:14.892827
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

# Generated at 2026-10-24 21:40:16.248029
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

# Generated at 2026-10-24 21:40:17.622868
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

# Generated at 2026-10-24 21:40:18.974636
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

# Generated at 2026-10-24 21:40:21.464441
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

# Generated at 2026-10-24 21:40:22.816097
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

# Generated at 2026-10-24 21:40:24.198351
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

# Generated at 2026-10-24 21:40:25.553127
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

# Generated at 2026-10-24 21:40:26.904320
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

# Generated at 2026-10-24 21:40:28.263572
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

# Generated at 2026-10-24 21:40:29.630985
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

# Generated at 2026-10-24 21:40:30.992201
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

# Generated at 2026-10-24 21:40:33.549020
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:35.966796
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:38.389114
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:40.812469
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:43.226669
# Unit test for function file_name_check

# Generated at 2026-10-24 21:40:45.642016
# Unit test for function file_name_check