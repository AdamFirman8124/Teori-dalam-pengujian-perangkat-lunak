

# Generated at 2026-10-23 18:25:15.758154
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir/file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir/file2.txt"),
    ]

# Generated at 2026-10-23 18:25:24.689072
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir/file2.txt", "file3.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir/file2.txt"),
        os.path.join(parent, "file3.txt"),
    ]

# Generated at 2026-10-23 18:25:28.982272
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

# Generated at 2026-10-23 18:25:33.595838
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir/file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir/file2.txt"),
    ]

# Generated at 2026-10-23 18:25:40.650314
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir/file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir/file2.txt"),
    ]