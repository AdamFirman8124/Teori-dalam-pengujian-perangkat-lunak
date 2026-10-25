

# Generated at 2026-10-25 03:53:54.623076
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-25 03:54:02.502810
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-25 03:54:09.053387
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("file.txt") == "Yes"

# Generated at 2026-10-25 03:54:14.583507
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("file.txt") == "Yes"

# Generated at 2026-10-25 03:54:17.225301
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:19.747083
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:22.163206
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:24.578624
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:27.003233
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:29.406929
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:31.822195
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:34.237230
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:36.651235
# Unit test for function file_name_check

# Generated at 2026-10-25 03:54:43.355502
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-25 03:54:50.534331
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-25 03:55:03.942348
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-25 03:55:10.695941
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-25 03:55:17.049098
# Unit test for function file_name_check
def test_file_name_check():cases = {
        "file.txt": "Yes",
        "app.exe": "Yes",
        "library.dll": "Yes",
        "a123.txt": "Yes",
        "file": "No",
        "file.txt.exe": "No",
        ".txt": "No",
        "1file.txt": "No",
        "file.pdf": "No",
        "file.EXE": "No",
        "a1234.dll": "No",
        "": "No",
    }


# Generated at 2026-10-25 03:55:19.465741
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:21.988303
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:24.402880
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:26.829090
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:29.233142
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:31.820992
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:34.232114
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:36.648047
# Unit test for function file_name_check

# Generated at 2026-10-25 03:55:43.488175
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-25 03:55:51.047543
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-25 03:55:57.291276
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check('example.txt') == 'Yes'

# Generated at 2026-10-25 03:56:04.563753
# Unit test for function file_name_check
def test_file_name_check():valid_cases = [
        ("example.txt", "Yes"),
        ("a.exe", "Yes"),
        ("file123.dll", "Yes"),
    ]

# Generated at 2026-10-25 03:56:10.705287
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check('example.txt') == 'Yes'

# Generated at 2026-10-25 03:56:18.702158
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("file.txt") == "Yes"

# Generated at 2026-10-25 03:56:25.049756
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("example.txt") == "Yes"

# Generated at 2026-10-25 03:56:27.467746
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:29.996543
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:32.413220
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:34.828500
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:37.243091
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:39.661568
# Unit test for function file_name_check

# Generated at 2026-10-25 03:56:46.628869
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("file.txt") == "Yes"

# Generated at 2026-10-25 03:56:52.994897
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("app.exe") == "Yes"
    assert module_0.file_name_check("lib.dll") == "Yes"
    assert module_0.file_name_check("file123.txt") == "Yes"

    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check(".txt") == "No"
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("file1234.txt") == "No"
    assert module_0.file_name_check("file.pdf") == "No"
    assert module_0.file_name_check("file.TXT") == "No"
    assert module_0.file_name_check("file") == "No"
    assert module_0.file_name_check("file.txt.exe") == "No"