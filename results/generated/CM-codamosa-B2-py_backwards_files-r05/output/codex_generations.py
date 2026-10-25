

# Generated at 2026-10-25 01:33:13.742649
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    output_dir = tmp_path / "output"

    # A non-Python input cannot be written to a Python file.
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            None,
        ))

    # Input must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

    # Python file to Python file.
    input_file = tmp_path / "source.py"
    input_file.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(tmp_path / "destination.py"),
        None,
    ))

    assert result == [
        InputOutput(input_file, tmp_path / "destination.py")
    ]

    # Python file to an output directory without an explicit root.
    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(input_file, output_dir / "source.py")
    ]

    # Python file to an output directory relative to an explicit root.
    package_dir = tmp_path / "project" / "package"
    package_dir.mkdir(parents=True)
    package_file = package_dir / "module.py"
    package_file.write_text("VALUE = 1")

    result = list(module_0.get_input_output_paths(
        str(package_file),
        str(output_dir),
        str(tmp_path / "project"),
    ))

    assert result == [
        InputOutput(package_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    nested_dir = input_dir / "nested"
    nested_dir.mkdir()
    python_file = nested_dir / "example.py"
    python_file.write_text("pass")
    (nested_dir / "ignored.txt").write_text("not Python")

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(
            python_file,
            output_dir / "nested" / "example.py",
        )
    ]

# Generated at 2026-10-25 01:33:30.435749
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from tempfile import TemporaryDirectory

    import pytest

    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        input_dir = base / "src"
        nested_dir = input_dir / "package"
        nested_dir.mkdir(parents=True)

        top_level_file = input_dir / "main.py"
        nested_file = nested_dir / "module.py"
        ignored_file = nested_dir / "README.txt"

        top_level_file.touch()
        nested_file.touch()
        ignored_file.touch()

        output_dir = base / "out"

        # A directory cannot be written to a single Python file.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(input_dir),
                str(base / "output.py"),
                None,
            ))

        # The input must exist.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(base / "missing"),
                str(output_dir),
                None,
            ))

        # Python file to Python file.
        output_file = base / "renamed.py"
        assert list(module_0.get_input_output_paths(
            str(top_level_file),
            str(output_file),
            None,
        )) == [
            InputOutput(top_level_file, output_file),
        ]

        # Python file to an output directory without a root.
        assert list(module_0.get_input_output_paths(
            str(top_level_file),
            str(output_dir),
            None,
        )) == [
            InputOutput(top_level_file, output_dir / "main.py"),
        ]

        # Python file to an output directory relative to an explicit root.
        assert list(module_0.get_input_output_paths(
            str(nested_file),
            str(output_dir),
            str(input_dir),
        )) == [
            InputOutput(nested_file, output_dir / "package" / "module.py"),
        ]

        # Directory input recursively includes only Python files.
        actual = list(module_0.get_input_output_paths(
            str(input_dir),
            str(output_dir),
            None,
        ))
        expected = [
            InputOutput(top_level_file, output_dir / "main.py"),
            InputOutput(
                nested_file,
                output_dir / "package" / "module.py",
            ),
        ]

        # glob ordering is not guaranteed.
        assert sorted(actual, key=repr) == sorted(expected, key=repr)

        # An explicit root preserves the input directory's relative path.
        actual = list(module_0.get_input_output_paths(
            str(input_dir),
            str(output_dir),
            str(base),
        ))
        expected = [
            InputOutput(
                top_level_file,
                output_dir / "src" / "main.py",
            ),
            InputOutput(
                nested_file,
                output_dir / "src" / "package" / "module.py",
            ),
        ]

        assert sorted(actual, key=repr) == sorted(expected, key=repr)

# Generated at 2026-10-25 01:33:47.433870
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A single Python file can be mapped directly to another Python file.
    source = tmp_path / "source.py"
    source.write_text("print('hello')\n")
    destination = tmp_path / "destination.py"

    assert list(module_0.get_input_output_paths(
        str(source), str(destination), root=None
    )) == [
        InputOutput(source, destination)
    ]

    # A Python file mapped to a directory retains its filename.
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(source), str(output_dir), root=None
    )) == [
        InputOutput(source, output_dir / "source.py")
    ]

    # A root directory preserves the source's relative path.
    package_dir = tmp_path / "package"
    nested_dir = package_dir / "nested"
    nested_dir.mkdir(parents=True)

    nested_source = nested_dir / "module.py"
    nested_source.write_text("value = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_source),
        str(output_dir),
        root=str(tmp_path),
    )) == [
        InputOutput(
            nested_source,
            output_dir / "package" / "nested" / "module.py",
        )
    ]

    # A directory input recursively includes only Python files.
    top_level_source = package_dir / "main.py"
    top_level_source.write_text("print('main')\n")
    (nested_dir / "ignored.txt").write_text("not Python\n")

    actual = list(module_0.get_input_output_paths(
        str(package_dir), str(output_dir), root=None
    ))
    expected = [
        InputOutput(top_level_source, output_dir / "main.py"),
        InputOutput(
            nested_source,
            output_dir / "nested" / "module.py",
        ),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory/non-Python input cannot be mapped to a .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package_dir),
            str(destination),
            root=None,
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            root=None,
        ))

# Generated at 2026-10-25 01:33:49.953242
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:33:52.367573
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:33:54.782512
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:33:57.201262
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:33:59.615726
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:02.207602
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:04.621667
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:07.036858
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:09.451840
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:11.866107
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:14.281690
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:16.696565
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:19.110609
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:21.525123
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:23.939630
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:26.354091
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:28.780138
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:31.194290
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:33.808875
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:34:44.978350
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:34:57.683636
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    first_input = source_dir / "main.py"
    second_input = package_dir / "module.py"
    ignored_input = source_dir / "README.md"

    first_input.write_text("print('main')")
    second_input.write_text("print('module')")
    ignored_input.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A directory input recursively maps only Python files.
    actual = list(
        module_0.get_input_output_paths(
            str(source_dir),
            str(output_dir),
            root=None,
        )
    )
    expected = [
        InputOutput(first_input, output_dir / "main.py"),
        InputOutput(second_input, output_dir / "package" / "module.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(
            str(first_input),
            str(output_file),
            root=None,
        )
    ) == [InputOutput(first_input, output_file)]

    # A Python file mapped to a directory keeps its path relative to root.
    rooted_output = list(
        module_0.get_input_output_paths(
            str(second_input),
            str(output_dir),
            root=str(source_dir),
        )
    )
    assert rooted_output == [
        InputOutput(second_input, output_dir / "package" / "module.py")
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_file),
                root=None,
            )
        )

    # Missing input paths are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                root=None,
            )
        )

# Generated at 2026-10-25 01:35:18.294296
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    source_dir.mkdir()
    nested_dir.mkdir()

    main_file = source_dir / "main.py"
    helper_file = nested_dir / "helper.py"
    ignored_file = source_dir / "README.md"

    main_file.write_text("print('main')")
    helper_file.write_text("print('helper')")
    ignored_file.write_text("Not a Python file")

    # A Python file mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(direct_output), None
    )) == [
        InputOutput(main_file, direct_output)
    ]

    # A Python file mapped into an output directory.
    output_dir = tmp_path / "build"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # A root preserves the file's path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(main_file, output_dir / "src" / "main.py")
    ]

    # A directory is searched recursively, ignoring non-Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(helper_file, output_dir / "package" / "helper.py"),
    ]

    assert len(actual) == len(expected)
    for pair in expected:
        assert pair in actual

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "output.py"), None
        ))

    # Errors in a generator are raised when it is consumed.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:35:20.835042
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:23.353038
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:25.882014
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:28.492556
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:30.906937
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:33.482903
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:35.900894
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:38.311721
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:35:48.776360
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:36:04.542086
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace `your_module` with the module containing the function.
from your_module import (
    InputOutput,
    InputDoesntExists,
    InvalidInputOutput,
    get_input_output_paths,
)


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    main_file = source_root / "main.py"
    module_file = package / "module.py"
    ignored_file = package / "README.txt"

    main_file.write_text("print('main')\n")
    module_file.write_text("print('module')\n")
    ignored_file.write_text("ignored\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(main_file, output_file)
    ]

    # Python file to output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Python file to output directory relative to a root.
    result = list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(source_root)
    ))
    assert result == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    result = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:36:15.585038
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [
        InputOutput(Path(first_file), Path(output_file))
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(Path(first_file), Path(output_dir / "first.py"))
    ]

    # A root path preserves the file's path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(input_dir)
    )) == [
        InputOutput(
            Path(second_file),
            Path(output_dir / "package" / "second.py"),
        )
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    assert set(results) == {
        InputOutput(
            Path(first_file),
            Path(output_dir / "first.py"),
        ),
        InputOutput(
            Path(second_file),
            Path(output_dir / "package" / "second.py"),
        ),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:36:28.201211
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    source_file = package_dir / "module.py"
    source_file.write_text("print('hello')")

    nested_file = package_dir / "nested.py"
    nested_file.write_text("print('nested')")

    non_python_file = package_dir / "README.md"
    non_python_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    explicit_output = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(explicit_output), None)
    ) == [
        InputOutput(source_file, explicit_output)
    ]

    # Without a root, only the input filename is appended.
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_dir), None)
    ) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # With a root, the input's path relative to that root is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(source_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively and non-Python files are ignored.
    actual = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(source_file, output_dir / "package" / "module.py"),
        InputOutput(nested_file, output_dir / "package" / "nested.py"),
    ]
    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:36:30.730712
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:33.149971
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:35.685351
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:38.203558
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:40.617104
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:43.032423
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:45.609828
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:36:56.982786
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:37:09.267266
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    first_file = source_root / "main.py"
    second_file = package / "module.py"
    ignored_file = package / "README.txt"

    first_file.write_text("print('main')", encoding="utf-8")
    second_file.write_text("print('module')", encoding="utf-8")
    ignored_file.write_text("ignored", encoding="utf-8")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(first_file), str(output_file), None)) == [
        InputOutput(first_file, output_file)
    ]

    # A Python file mapped to a directory retains its filename.
    assert list(module_0.get_input_output_paths(str(first_file), str(output_dir), None)) == [
        InputOutput(first_file, output_dir / "main.py")
    ]

    # A root directory preserves the file's relative path.
    assert list(
        module_0.get_input_output_paths(
            str(second_file),
            str(output_dir),
            str(source_root),
        )
    ) == [
        InputOutput(second_file, output_dir / "package" / "module.py")
    ]

    # A directory input recursively includes only Python files.
    results = list(
        module_0.get_input_output_paths(str(source_root), str(output_dir), None)
    )
    assert set(results) == {
        InputOutput(first_file, output_dir / "main.py"),
        InputOutput(second_file, output_dir / "package" / "module.py"),
    }

    # A directory cannot be mapped to a single Python file.
    # The generator must be consumed for the exception to be raised.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_root),
                str(output_file),
                None,
            )
        )

    # A nonexistent input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:37:27.780125
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = source_dir / "README.md"

    first_file.write_text("print('first')\n")
    second_file.write_text("print('second')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(first_file), str(output_file), None)) == [
        InputOutput(first_file, output_file)
    ]

    # Without a root, the source filename is appended to the output directory.
    assert list(module_0.get_input_output_paths(str(first_file), str(output_dir), None)) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # With a root, the source path relative to that root is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(second_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    pairs = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    assert len(pairs) == 2
    assert InputOutput(first_file, output_dir / "first.py") in pairs
    assert InputOutput(
        second_file,
        output_dir / "package" / "second.py",
    ) in pairs

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_file),
                None,
            )
        )

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:37:30.321815
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:32.859351
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:35.381569
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:37.797871
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:40.331075
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:42.746431
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:45.162736
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:47.580421
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:49.994441
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:37:52.535012
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:38:04.764252
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:38:18.188531
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    package_dir = source_dir / "package"
    package_dir.mkdir()

    first_input = source_dir / "first.py"
    second_input = package_dir / "second.py"
    ignored_input = source_dir / "README.md"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input),
        str(output_file),
        None,
    )) == [
        InputOutput(first_input, output_file),
    ]

    # With a directory output, the input filename is preserved.
    assert list(module_0.get_input_output_paths(
        str(first_input),
        str(output_dir),
        None,
    )) == [
        InputOutput(first_input, output_dir / "first.py"),
    ]

    # An explicit root preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(second_input),
        str(output_dir),
        str(source_dir),
    )) == [
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    # Directories are searched recursively, ignoring non-Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        None,
    ))
    expected = [
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # Exceptions are raised while consuming the generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(tmp_path / "invalid.py"),
            None,
        ))

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 01:38:45.416577
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:38:47.833742
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:38:50.248229
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:38:52.663244
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:38:55.078499
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:03.528588
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-25 01:39:16.740341
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.exceptions import InvalidInputOutput, InputDoesntExists
from your_package.types import InputOutput
from your_package.paths import get_input_output_paths  # Adjust module path


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    nested_dir = source_root / "package"
    nested_dir.mkdir(parents=True)

    main_file = source_root / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_root / "README.md"

    main_file.write_text("print('main')", encoding="utf-8")
    nested_file.write_text("print('module')", encoding="utf-8")
    ignored_file.write_text("Not Python", encoding="utf-8")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = output_dir / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(main_file, output_file)
    ]

    # Python file to output directory.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Python file to output directory while preserving its path from root.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    assert len(results) == 2
    assert InputOutput(main_file, output_dir / "main.py") in results
    assert InputOutput(
        nested_file, output_dir / "package" / "module.py"
    ) in results

    # A directory/non-Python input cannot produce one Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_dir / "result.py"), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:39:30.169575
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace with the actual module path.
from your_package.module import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path):
    input_file = tmp_path / "source.py"
    input_file.write_text("print('hello')", encoding="utf-8")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file to an output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "source.py")
    ]

    # Python file to an output directory relative to a root.
    source_dir = tmp_path / "src"
    nested_file = source_dir / "package" / "module.py"
    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("VALUE = 1", encoding="utf-8")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Input directory: recursively find only Python files.
    second_file = source_dir / "main.py"
    second_file.write_text("print('main')", encoding="utf-8")
    (source_dir / "ignored.txt").write_text("ignored", encoding="utf-8")

    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(path, output_dir / path.relative_to(source_dir))
        for path in source_dir.glob("**/*.py")
    ]

    assert actual == expected

    # A directory cannot be written to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-25 01:39:43.377092
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    source_dir = root / "src"
    source_dir.mkdir(parents=True)

    source_file = source_dir / "example.py"
    source_file.write_text("print('hello')\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(Path(source_file), Path(output_file))
    ]

    # Python file to an output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(Path(source_file), Path(output_dir / "example.py"))
    ]

    # Preserve the path relative to an explicitly supplied root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(root)
    )) == [
        InputOutput(
            Path(source_file),
            Path(output_dir / "src" / "example.py"),
        )
    ]

    # Recursively process Python files while ignoring other files.
    nested_dir = source_dir / "nested"
    nested_dir.mkdir()
    nested_file = nested_dir / "module.py"
    nested_file.write_text("value = 1\n")
    (nested_dir / "README.txt").write_text("ignored\n")

    assert set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == {
        InputOutput(Path(source_file), Path(output_dir / "example.py")),
        InputOutput(
            Path(nested_file),
            Path(output_dir / "nested" / "module.py"),
        ),
    }

    # A directory/non-Python input cannot map to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:39:45.793229
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:48.209341
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:50.623513
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:53.040716
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:55.451537
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:57.865516
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:00.285281
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:02.697355
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:05.113627
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:07.696925
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:22.063544
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:40:36.425251
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file -> output directory
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Python file -> output directory, preserving path relative to root
    root = tmp_path / "project"
    nested_input = root / "src" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "src" / "module.py")
    ]

    # Input directory -> recursively discovered Python files
    source_dir = tmp_path / "source"
    first_file = source_dir / "first.py"
    second_file = source_dir / "package" / "second.py"
    ignored_file = source_dir / "README.txt"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("first = True")
    second_file.write_text("second = True")
    ignored_file.write_text("not Python")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    missing_input = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))

# Generated at 2026-10-25 01:40:48.815084
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')")

    ignored_file = nested_dir / "README.md"
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(explicit_output), None
    )) == [
        InputOutput(source_file, explicit_output)
    ]

    # Python file to output directory, without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # Python file to output directory, preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(explicit_output), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:41:05.666504
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "source"
    source_dir.mkdir()

    source_file = source_dir / "example.py"
    source_file.write_text("print('hello')")

    nested_dir = source_dir / "nested"
    nested_dir.mkdir()

    nested_file = nested_dir / "module.py"
    nested_file.write_text("value = 42")

    ignored_file = nested_dir / "README.txt"
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_file), None)
    ) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_dir), None)
    ) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # A Python file mapped relative to an explicit root.
    assert list(
        module_0.get_input_output_paths(
            str(nested_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(nested_file, output_dir / "nested" / "module.py")
    ]

    # A directory recursively maps only Python files.
    results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )

    assert len(results) == 2
    assert InputOutput(source_file, output_dir / "example.py") in results
    assert InputOutput(
        nested_file,
        output_dir / "nested" / "module.py",
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_file),
                None,
            )
        )

    # The input path must exist.
    missing_path = tmp_path / "missing"

    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(missing_path),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:41:19.103962
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "project"
    source_root.mkdir()

    source_file = source_root / "example.py"
    source_file.write_text("print('hello')", encoding="utf-8")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Python file to output directory while preserving its root-relative path.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source_file, output_dir / "project" / "example.py")
    ]


def test_get_input_output_paths_for_directory(tmp_path):
    input_dir = tmp_path / "src"
    package_dir = input_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = input_dir / "main.py"
    second_file = package_dir / "module.py"
    ignored_file = package_dir / "README.md"

    first_file.write_text("", encoding="utf-8")
    second_file.write_text("", encoding="utf-8")
    ignored_file.write_text("", encoding="utf-8")

    output_dir = tmp_path / "output"

    result = set(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))

    assert result == {
        InputOutput(first_file, output_dir / "main.py"),
        InputOutput(second_file, output_dir / "package" / "module.py"),
    }


def test_get_input_output_paths_for_directory_with_root(tmp_path):
    root = tmp_path / "project"
    input_dir = root / "src"
    input_dir.mkdir(parents=True)

    source_file = input_dir / "main.py"
    source_file.write_text("", encoding="utf-8")

    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), str(root)
    )) == [
        InputOutput(source_file, output_dir / "src" / "main.py")
    ]


def test_get_input_output_paths_rejects_file_output_for_directory(tmp_path):
    input_dir = tmp_path / "src"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(tmp_path / "output.py"), None
        ))


def test_get_input_output_paths_rejects_missing_input(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(tmp_path / "output"), None
        ))

# Generated at 2026-10-25 01:41:30.910899
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")
    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # Python file -> output directory
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # Directory -> recursively discovered Python files
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "README.txt"

    first_file.write_text("")
    second_file.write_text("")
    ignored_file.write_text("ignored")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    assert set(results) == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    }

    # Explicit root preserves the path relative to that root
    results = list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(tmp_path)
    ))

    assert results == [
        InputOutput(
            second_file,
            output_dir / "src" / "package" / "second.py",
        )
    ]

    # Invalid input/output combination
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:41:51.786163
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    source_file = source_dir / "module.py"
    nested_file = nested_dir / "child.py"
    ignored_file = source_dir / "README.md"

    source_file.write_text("print('module')\n")
    nested_file.write_text("print('child')\n")
    ignored_file.write_text("Not a Python file\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [InputOutput(source_file, output_file)]

    # Python file to an output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [InputOutput(source_file, output_dir / "module.py")]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source_file, output_dir / "src" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(source_file, output_dir / "module.py"),
        InputOutput(nested_file, output_dir / "nested" / "child.py"),
    ]

    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "combined.py"), None
        ))

    # Exceptions are raised during iteration because this is a generator.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:42:04.382522
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    module_file = package_dir / "module.py"
    ignored_file = package_dir / "README.md"

    main_file.write_text("print('main')\n")
    module_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(direct_output), None
    )) == [
        InputOutput(main_file, direct_output)
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # A root directory preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "combined.py"), None
        ))

    # A missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "missing-output.py"),
            None,
        ))

# Generated at 2026-10-25 01:42:06.798355
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:42:17.182830
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:42:37.120763
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace `your_package.your_module` with the module containing the function.
from your_package.your_module import (
    get_input_output_paths,
    InputDoesntExists,
    InputOutput,
    InvalidInputOutput,
)


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "root"
    source_dir = root / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "ignored.txt"

    first_file.write_text("print('first')\n")
    second_file.write_text("print('second')\n")
    ignored_file.write_text("not Python\n")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [
        InputOutput(first_file, output_file)
    ]

    # Python file to output directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # Python file to output directory relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), str(root)
    )) == [
        InputOutput(first_file, output_dir / "src" / "first.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    assert len(results) == 2
    assert InputOutput(first_file, output_dir / "first.py") in results
    assert InputOutput(
        second_file, output_dir / "nested" / "second.py"
    ) in results

    # Explicit root is preserved in generated output paths.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), str(root)
    ))
    assert len(results) == 2
    assert InputOutput(
        first_file, output_dir / "src" / "first.py"
    ) in results
    assert InputOutput(
        second_file, output_dir / "src" / "nested" / "second.py"
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_file), None
        ))

# Generated at 2026-10-25 01:42:50.051378
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can map directly to another Python file.
    source = tmp_path / "source.py"
    source.write_text("print('hello')\n")

    result = list(module_0.get_input_output_paths(
        str(source),
        str(tmp_path / "result.py"),
        root=None,
    ))

    assert result == [
        InputOutput(source, tmp_path / "result.py"),
    ]

    # A Python file mapped to a directory retains its filename.
    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(source),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(source, output_dir / "source.py"),
    ]

    # Supplying a root preserves the source's path relative to that root.
    root = tmp_path / "project"
    nested_source = root / "package" / "module.py"
    nested_source.parent.mkdir(parents=True)
    nested_source.write_text("VALUE = 1\n")

    result = list(module_0.get_input_output_paths(
        str(nested_source),
        str(output_dir),
        root=str(root),
    ))

    assert result == [
        InputOutput(nested_source, output_dir / "package" / "module.py"),
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    input_dir = tmp_path / "inputs"
    first = input_dir / "first.py"
    second = input_dir / "nested" / "second.py"
    ignored = input_dir / "nested" / "notes.txt"

    second.parent.mkdir(parents=True)
    first.write_text("FIRST = True\n")
    second.write_text("SECOND = True\n")
    ignored.write_text("Not Python\n")

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        root=None,
    ))

    assert set(result) == {
        InputOutput(first, output_dir / "first.py"),
        InputOutput(second, output_dir / "nested" / "second.py"),
    }

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "single.py"),
            root=None,
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            root=None,
        ))

# Generated at 2026-10-25 01:43:03.224007
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")
    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # A supplied root preserves the file's path relative to that root.
    root = tmp_path / "project"
    nested_input = root / "src" / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(
            nested_input,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    source_dir = tmp_path / "sources"
    first_file = source_dir / "first.py"
    second_file = source_dir / "nested" / "second.py"
    ignored_file = source_dir / "nested" / "README.txt"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("FIRST = True\n")
    second_file.write_text("SECOND = True\n")
    ignored_file.write_text("ignored\n")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "nested" / "second.py"),
    ]

    assert len(results) == len(expected)
    for item in expected:
        assert item in results

    # A directory/non-Python input cannot be mapped to a .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Generator exceptions are raised when the generator is consumed.
    missing_input = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))