

# Generated at 2026-10-23 18:25:15.963546
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

# Generated at 2026-10-23 18:25:23.720378
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    paths = ["file1.txt", "subdir/file2.txt"]

    result = list(module_0.join_each(parent, paths))

    assert result == [
        os.path.join(parent, "file1.txt"),
        os.path.join(parent, "subdir/file2.txt"),
    ]

# Generated at 2026-10-23 18:25:30.821829
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

# Generated at 2026-10-23 18:25:34.887589
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

# Generated at 2026-10-23 18:25:40.122387
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