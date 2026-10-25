

# Generated at 2026-10-23 19:45:13.333464
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "file2.txt", os.path.join("subdir", "file3.txt")]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "file2.txt"),
        os.path.join(parent, "subdir", "file3.txt"),
    ]

# Generated at 2026-10-23 19:45:17.532048
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir", "file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir"),
        os.path.join(parent, "file2.txt"),
    ]

# Generated at 2026-10-23 19:45:26.440354
# Unit test for function join_each
def test_join_each():
    parent = os.path.join("root", "parent")
    paths = ["file1.txt", "file2.txt", os.path.join("subdir", "file3.txt")]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "file2.txt"),
        os.path.join(parent, "subdir", "file3.txt"),
    ]

# Generated at 2026-10-23 19:45:31.459986
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir", "file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir"),
        os.path.join(parent, "file2.txt"),
    ]
    assert list(module_0.join_each(parent, [])) == []

# Generated at 2026-10-23 19:45:38.320303
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "file2.txt", "subdir/file3.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "file2.txt"),
        os.path.join(parent, "subdir/file3.txt"),
    ]