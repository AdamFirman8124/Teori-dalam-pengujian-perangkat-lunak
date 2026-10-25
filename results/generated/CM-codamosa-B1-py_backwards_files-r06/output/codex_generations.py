

# Generated at 2026-10-25 02:34:28.494539
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as directory:
        base = Path(directory)
        source_dir = base / "src"
        package_dir = source_dir / "package"
        package_dir.mkdir(parents=True)

        source_file = package_dir / "example.py"
        source_file.write_text("print('hello')\n")
        (package_dir / "ignored.txt").write_text("ignored")

        output_dir = base / "output"

        # Recursively maps Python files while preserving relative paths.
        results = list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_dir),
                root=None,
            )
        )
        assert results == [
            InputOutput(
                source_file,
                output_dir / "package" / "example.py",
            )
        ]

        # A single input file can map directly to another Python file.
        output_file = base / "result.py"
        assert list(
            module_0.get_input_output_paths(
                str(source_file),
                str(output_file),
                root=None,
            )
        ) == [InputOutput(source_file, output_file)]

        # A non-Python input cannot be mapped to a Python output file.
        with pytest.raises(InvalidInputOutput):
            list(
                module_0.get_input_output_paths(
                    str(source_dir),
                    str(output_file),
                    root=None,
                )
            )

        # Missing inputs are rejected.
        with pytest.raises(InputDoesntExists):
            list(
                module_0.get_input_output_paths(
                    str(base / "missing.py"),
                    str(output_dir),
                    root=None,
                )
            )

# Generated at 2026-10-25 02:34:46.907314
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    source_dir = root / "src"
    source_dir.mkdir(parents=True)

    source_file = source_dir / "example.py"
    source_file.write_text("print('hello')\n")

    # A Python file can be mapped directly to another Python file.
    target_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(target_file), None
    )) == [
        InputOutput(source_file, target_file)
    ]

    # Without root, only the input filename is appended.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # With root, the relative input path is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(root)
    )) == [
        InputOutput(source_file, output_dir / "src" / "example.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    (source_dir / "ignored.txt").write_text("ignored")
    assert list(module_0.get_input_output_paths(
        str(root), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "src" / "example.py")
    ]

    # A directory/non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(target_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:35:01.137195
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    source = tmp_path / "source.py"
    source.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(source),
        str(tmp_path / "result.py"),
        None,
    ))

    assert result == [
        InputOutput(source, tmp_path / "result.py"),
    ]

    # When output is a directory, preserve the filename.
    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(source),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(source, output_dir / "source.py"),
    ]

    # A root directory preserves the source path relative to that root.
    root = tmp_path / "root"
    nested_source = root / "package" / "module.py"
    nested_source.parent.mkdir(parents=True)
    nested_source.write_text("VALUE = 1")

    result = list(module_0.get_input_output_paths(
        str(nested_source),
        str(output_dir),
        str(root),
    ))

    assert result == [
        InputOutput(nested_source, output_dir / "package" / "module.py"),
    ]

    # Directories are searched recursively for Python files.
    input_dir = tmp_path / "input"
    first_source = input_dir / "first.py"
    second_source = input_dir / "nested" / "second.py"
    ignored_file = input_dir / "ignored.txt"

    second_source.parent.mkdir(parents=True)
    first_source.write_text("")
    second_source.write_text("")
    ignored_file.write_text("not Python")

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    expected = [
        InputOutput(first_source, output_dir / "first.py"),
        InputOutput(second_source, output_dir / "nested" / "second.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A directory/non-Python input cannot map to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "invalid.py"),
            None,
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 02:35:11.496510
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    output_dir = tmp_path / "output"

    # Python file to Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(tmp_path / "result.py"),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, tmp_path / "result.py")
    ]

    # Python file to output directory.
    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Preserve the path relative to an explicitly supplied root.
    source_dir = tmp_path / "project" / "src"
    source_dir.mkdir(parents=True)
    nested_file = source_dir / "module.py"
    nested_file.write_text("x = 1")

    result = list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        root=str(tmp_path / "project"),
    ))

    assert result == [
        InputOutput(nested_file, output_dir / "src" / "module.py")
    ]

    # Recursively process a directory.
    package_dir = tmp_path / "package"
    subdirectory = package_dir / "sub"
    subdirectory.mkdir(parents=True)

    first_file = package_dir / "first.py"
    second_file = subdirectory / "second.py"
    ignored_file = package_dir / "README.md"

    first_file.write_text("a = 1")
    second_file.write_text("b = 2")
    ignored_file.write_text("not Python")

    result = set(module_0.get_input_output_paths(
        str(package_dir),
        str(output_dir),
        root=None,
    ))

    assert result == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "sub" / "second.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package_dir),
            str(tmp_path / "output.py"),
            root=None,
        ))

    # The input must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            root=None,
        ))

# Generated at 2026-10-25 02:35:32.385108
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # When root is provided, the path relative to root is preserved.
    root = tmp_path / "project"
    nested_input = root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    source_dir = tmp_path / "src"
    first_input = source_dir / "first.py"
    second_input = source_dir / "nested" / "second.py"
    ignored_input = source_dir / "nested" / "notes.txt"

    second_input.parent.mkdir(parents=True)
    first_input.write_text("FIRST = True")
    second_input.write_text("SECOND = True")
    ignored_input.write_text("not Python")

    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "nested" / "second.py"),
    ]

    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:35:44.731822
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "input"
    nested_dir = input_dir / "nested"
    output_dir = tmp_path / "output"

    nested_dir.mkdir(parents=True)
    source_file = input_dir / "main.py"
    nested_source_file = nested_dir / "module.py"
    ignored_file = input_dir / "README.md"

    source_file.write_text("print('main')")
    nested_source_file.write_text("print('module')")
    ignored_file.write_text("Not Python")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_file), None)
    ) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file mapped to a directory retains its filename.
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_dir), None)
    ) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # An explicit root preserves the path relative to that root.
    assert list(
        module_0.get_input_output_paths(
            str(nested_source_file),
            str(output_dir),
            str(input_dir),
        )
    ) == [
        InputOutput(nested_source_file, output_dir / "nested" / "module.py")
    ]

    # A directory is searched recursively, ignoring non-Python files.
    actual = list(
        module_0.get_input_output_paths(str(input_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(source_file, output_dir / "main.py"),
        InputOutput(
            nested_source_file,
            output_dir / "nested" / "module.py",
        ),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(input_dir),
                str(output_file),
                None,
            )
        )

    # The input must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 02:35:56.347388
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    package.mkdir(parents=True)

    source = package / "example.py"
    source.write_text("print('hello')\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(source), str(output_file), None)) == [
        InputOutput(source, output_file)
    ]

    # Python file to an output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(source), str(output_dir), None)) == [
        InputOutput(source, output_dir / "example.py")
    ]

    # Python file to an output directory while preserving its root-relative path.
    assert list(
        module_0.get_input_output_paths(str(source), str(output_dir), str(tmp_path))
    ) == [
        InputOutput(source, output_dir / "project" / "package" / "example.py")
    ]

    # Directory input recursively discovers Python files.
    assert list(
        module_0.get_input_output_paths(str(project), str(output_dir), None)
    ) == [
        InputOutput(source, output_dir / "package" / "example.py")
    ]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(project),
            str(tmp_path / "invalid.py"),
            None,
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 02:36:10.273882
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust this import to match the module containing the function.
# from your_package.your_module import get_input_output_paths
# from your_package.exceptions import InvalidInputOutput, InputDoesntExists
# from your_package.types import InputOutput


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    source_dir.mkdir()
    nested_dir.mkdir()

    first_file = source_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = source_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(first_file), str(direct_output), None)
    ) == [
        InputOutput(first_file, direct_output)
    ]

    # A Python file mapped into an output directory.
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_dir), None)
    ) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # A directory is searched recursively, excluding non-Python files.
    result = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]
    assert sorted(result, key=lambda item: str(item)) == sorted(
        expected, key=lambda item: str(item)
    )

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 02:36:29.693814
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths_for_single_file(tmp_path):
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        root=None,
    ))

    assert result == [InputOutput(input_file, output_file)]


def test_get_input_output_paths_for_single_file_to_directory(tmp_path):
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, output_dir / "input.py")
    ]


def test_get_input_output_paths_for_single_file_with_root(tmp_path):
    root = tmp_path / "project"
    input_file = root / "src" / "input.py"
    input_file.parent.mkdir(parents=True)
    input_file.write_text("print('hello')")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=str(root),
    ))

    assert result == [
        InputOutput(input_file, output_dir / "src" / "input.py")
    ]


def test_get_input_output_paths_for_directory(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "main.py"
    second_file = nested_dir / "module.py"
    ignored_file = nested_dir / "README.txt"

    first_file.write_text("")
    second_file.write_text("")
    ignored_file.write_text("ignored")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        root=None,
    ))

    expected = [
        InputOutput(first_file, output_dir / "main.py"),
        InputOutput(second_file, output_dir / "package" / "module.py"),
    ]

    assert len(result) == len(expected)
    for pair in expected:
        assert pair in result


def test_get_input_output_paths_raises_for_directory_to_python_file(tmp_path):
    input_dir = tmp_path / "src"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        # The function is a generator, so it must be consumed to raise.
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            root=None,
        ))


def test_get_input_output_paths_raises_for_missing_input(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(tmp_path / "output"),
            root=None,
        ))

# Generated at 2026-10-25 02:36:42.381426
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:36:49.586432
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-25 02:37:02.179573
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust this import to match your package/module structure.
from your_package.module import (
    get_input_output_paths,
    InputOutput,
    InvalidInputOutput,
    InputDoesntExists,
)


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    source_file = source_dir / "example.py"
    source_file.write_text("print('example')\n")

    nested_dir = source_dir / "nested"
    nested_dir.mkdir()
    nested_file = nested_dir / "other.py"
    nested_file.write_text("print('other')\n")

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file mapped into an output directory.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Preserve the path relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "nested" / "other.py")
    ]

    # Recursively map all Python files in a directory.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(source_file, output_dir / "example.py"),
        InputOutput(nested_file, output_dir / "nested" / "other.py"),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:37:16.827571
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    package.mkdir(parents=True)

    main_file = project / "main.py"
    module_file = package / "module.py"
    ignored_file = package / "README.md"

    main_file.write_text("print('main')")
    module_file.write_text("print('module')")
    ignored_file.write_text("Not Python")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(main_file), str(output_file), None)) == [
        InputOutput(main_file, output_file)
    ]

    # Without root, preserve only the input file's name.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # With root, preserve the path relative to root.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(project)
    )) == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    actual = list(module_0.get_input_output_paths(
        str(project), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A directory/non-Python input cannot be mapped to a .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(project), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:37:35.553954
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    source_file = source_dir / "main.py"
    nested_file = nested_dir / "helper.py"
    ignored_file = source_dir / "README.md"

    source_file.write_text("print('main')")
    nested_file.write_text("print('helper')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Without a root, a single file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # With a root, the source path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source_file, output_dir / "src" / "main.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(source_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "nested" / "helper.py"),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # Because this function is a generator, it must be consumed for
    # validation exceptions to be raised.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    missing_input = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))

# Generated at 2026-10-25 02:37:52.570871
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package_dir = source_root / "package"
    package_dir.mkdir(parents=True)

    input_file = package_dir / "module.py"
    input_file.write_text("print('hello')\n")

    # A Python file mapped directly to another Python file.
    direct_output = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(direct_output), None
    )) == [
        InputOutput(input_file, direct_output)
    ]

    # A Python file mapped into an output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "module.py")
    ]

    # A Python file mapped into an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # A directory is searched recursively for Python files.
    assert list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # A non-Python input cannot be mapped to a Python output file.
    text_file = tmp_path / "input.txt"
    text_file.write_text("text")

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(text_file), str(tmp_path / "output.py"), None
        ))

    # The generator must be consumed for its validation code to execute.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:38:04.460522
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('hello')\n")

    nested = package / "nested"
    nested.mkdir()
    nested_module = nested / "other.py"
    nested_module.write_text("print('other')\n")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # Without a root, the source filename is appended to the output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # With a root, the relative source path is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(module),
            str(output_dir),
            str(source_root),
        )
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively for Python files.
    actual = set(module_0.get_input_output_paths(
        str(package),
        str(output_dir),
        None,
    ))
    assert actual == {
        InputOutput(module, output_dir / "module.py"),
        InputOutput(nested_module, output_dir / "nested" / "other.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package),
            str(output_file),
            None,
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 02:38:22.983194
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
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    source_file = package_dir / "example.py"
    source_file.write_text("print('hello')")

    # Non-Python files must be ignored when processing a directory.
    (package_dir / "README.txt").write_text("documentation")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # Python file to Python file.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Python file to output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(source_file, output_dir / "package" / "example.py")
    ]

    # Directory input without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "package" / "example.py")
    ]

    # Directory input relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(
            source_file,
            output_dir / "src" / "package" / "example.py",
        )
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input path.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:38:36.808741
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .exceptions import InvalidInputOutput, InputDoesntExists
from .types import InputOutput
from .paths import get_input_output_paths  # Adjust module name if necessary


def test_get_input_output_paths_for_file_to_file(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_path),
        root=None,
    ))

    assert result == [InputOutput(input_path, output_path)]


def test_get_input_output_paths_for_file_to_directory(tmp_path):
    input_path = tmp_path / "input.py"
    output_dir = tmp_path / "output"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(input_path, output_dir / "input.py"),
    ]


def test_get_input_output_paths_preserves_path_relative_to_root(tmp_path):
    root = tmp_path / "project"
    input_path = root / "src" / "input.py"
    output_dir = tmp_path / "output"

    input_path.parent.mkdir(parents=True)
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_dir),
        root=str(root),
    ))

    assert result == [
        InputOutput(input_path, output_dir / "src" / "input.py"),
    ]


def test_get_input_output_paths_for_directory(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"

    first_input = input_dir / "first.py"
    second_input = input_dir / "nested" / "second.py"
    ignored_input = input_dir / "ignored.txt"

    second_input.parent.mkdir(parents=True)
    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    result = set(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        root=None,
    ))

    assert result == {
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "nested" / "second.py"),
    }


def test_get_input_output_paths_raises_for_directory_to_python_file(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            root=None,
        ))


def test_get_input_output_paths_raises_when_input_does_not_exist(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(tmp_path / "output"),
            root=None,
        ))

# Generated at 2026-10-25 02:38:48.369784
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')\n")

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Without root, a file is placed directly inside the output directory.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # With root, the input's relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes Python files and ignores others.
    (nested_dir / "ignored.txt").write_text("ignored\n")
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # A directory/non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:39:00.564798
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.your_module import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path):
    source = tmp_path / "source"
    output = tmp_path / "output"
    source.mkdir()

    # A Python file mapped directly to another Python file.
    input_file = source / "module.py"
    input_file.write_text("print('hello')\n")

    output_file = output / "renamed.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        root=None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output),
        root=None,
    )) == [
        InputOutput(input_file, output / "module.py"),
    ]

    # Supplying root preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output),
        root=str(tmp_path),
    )) == [
        InputOutput(input_file, output / "source" / "module.py"),
    ]

    # A directory is searched recursively, ignoring non-Python files.
    package = source / "package"
    package.mkdir()
    nested_file = package / "nested.py"
    nested_file.write_text("value = 1\n")
    (package / "README.txt").write_text("ignored\n")

    actual = list(module_0.get_input_output_paths(
        str(source),
        str(output),
        root=None,
    ))

    assert set(actual) == {
        InputOutput(input_file, output / "module.py"),
        InputOutput(nested_file, output / "package" / "nested.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source),
            str(output_file),
            root=None,
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output),
            root=None,
        ))

# Generated at 2026-10-25 02:39:12.564487
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file copied directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(tmp_path / "output.py"),
        None,
    )) == [
        InputOutput(input_file, tmp_path / "output.py")
    ]

    # A Python file copied into an output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(tmp_path / "dist"),
        None,
    )) == [
        InputOutput(input_file, tmp_path / "dist" / "input.py")
    ]

    # Preserve the path relative to an explicitly supplied root.
    source_root = tmp_path / "source"
    nested_file = source_root / "package" / "module.py"
    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(tmp_path / "build"),
        str(source_root),
    )) == [
        InputOutput(nested_file, tmp_path / "build" / "package" / "module.py")
    ]

    # Recursively process only Python files in an input directory.
    project = tmp_path / "project"
    first_file = project / "first.py"
    second_file = project / "package" / "second.py"
    ignored_file = project / "README.md"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("")
    second_file.write_text("")
    ignored_file.write_text("ignored")

    results = list(module_0.get_input_output_paths(
        str(project),
        str(tmp_path / "output"),
        None,
    ))

    expected = [
        InputOutput(first_file, tmp_path / "output" / "first.py"),
        InputOutput(
            second_file,
            tmp_path / "output" / "package" / "second.py",
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # Generator exceptions are raised when it is consumed.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(project),
            str(tmp_path / "invalid.py"),
            None,
        ))

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            None,
        ))

# Generated at 2026-10-25 02:39:25.835746
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')", encoding="utf-8")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file -> output directory
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Input directory -> recursively mapped Python files
    source_dir = tmp_path / "source"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    nested_file = nested_dir / "module.py"
    nested_file.write_text("value = 42", encoding="utf-8")
    (nested_dir / "ignored.txt").write_text("ignored", encoding="utf-8")

    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Explicit root is preserved in the output-relative path
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(
            nested_file,
            output_dir / "source" / "package" / "module.py",
        )
    ]

    # A non-Python input cannot target a Python output file
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_file), None
        ))

# Generated at 2026-10-25 02:39:28.391004
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:30.809272
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:33.221849
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:35.633209
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:38.045761
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:40.461391
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:42.881852
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:45.303672
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:47.704934
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:50.119178
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:52.535769
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:54.950274
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:57.364792
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:39:59.785950
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:02.201063
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:04.615889
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:12.448436
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 02:40:27.502529
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    nested = package / "nested"
    nested.mkdir(parents=True)

    module = package / "module.py"
    nested_module = nested / "other.py"
    ignored_file = package / "README.md"

    module.write_text("print('module')")
    nested_module.write_text("print('other')")
    ignored_file.write_text("Not a Python file")

    # A single input file and a single output file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # A single input file copied into an output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # A root path preserves the input's relative directory structure.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(source_root))
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # A directory input recursively includes only Python files.
    results = list(
        module_0.get_input_output_paths(str(package), str(output_dir), str(source_root))
    )
    expected = [
        InputOutput(module, output_dir / "package" / "module.py"),
        InputOutput(
            nested_module,
            output_dir / "package" / "nested" / "other.py",
        ),
    ]
    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package),
            str(tmp_path / "invalid.py"),
            None,
        ))

    # Validation happens when the generator is iterated.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 02:40:40.536991
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')\n")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Without root, a file mapped to a directory keeps only its filename.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # With root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    (nested_dir / "ignored.txt").write_text("not Python")
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(
            source_file,
            output_dir / "package" / "module.py",
        )
    ]

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        # Conversion to list is required because this is a generator function.
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:40:42.955129
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:45.369417
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:47.785228
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:50.199060
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:52.614277
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:55.030645
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:57.448730
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:40:59.860785
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:41:02.276272
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:41:04.690885
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:41:14.605611
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 02:41:26.638839
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path):
    source_root = tmp_path / "source"
    package = source_root / "package"
    package.mkdir(parents=True)

    input_file = package / "module.py"
    input_file.write_text("print('hello')\n")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # Python file to Python file.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file to output directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "module.py")
    ]

    # Python file to output directory, preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # Input directory to output directory.
    assert list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:41:39.695528
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
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)
    nested_file = nested_dir / "module.py"
    nested_file.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Input directory -> output directory
    second_file = source_dir / "main.py"
    second_file.write_text("print('main')")
    ignored_file = source_dir / "README.txt"
    ignored_file.write_text("ignored")

    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(nested_file, output_dir / "package" / "module.py"),
        InputOutput(second_file, output_dir / "main.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory/non-Python input cannot map to a Python file
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input path
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-25 02:41:54.132343
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path) -> None:
    # A directory cannot be written to a single .py file.
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
            str(tmp_path / "output"),
            None,
        ))

    # Python file to Python file.
    input_file = input_dir / "source.py"
    input_file.touch()
    output_file = tmp_path / "renamed.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # Python file to output directory, without an explicit root.
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(input_file, output_dir / "source.py"),
    ]

    # Python file to output directory, preserving its path relative to root.
    nested_file = input_dir / "package" / "module.py"
    nested_file.parent.mkdir()
    nested_file.touch()

    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        str(input_dir),
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    # Recursively process only Python files in a directory.
    ignored_file = input_dir / "package" / "README.txt"
    ignored_file.touch()

    assert set(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    )) == {
        InputOutput(input_file, output_dir / "source.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    }

# Generated at 2026-10-25 02:41:56.549382
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:41:58.962969
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:01.377499
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:03.791536
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:06.207923
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:08.622241
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:20.877256
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    module_file = package_dir / "module.py"
    ignored_file = package_dir / "README.txt"

    main_file.write_text("print('main')\n")
    module_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python input can be mapped directly to a Python output.
    direct_output = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(main_file), str(direct_output), None)
    ) == [
        InputOutput(main_file, direct_output),
    ]

    # Without a root, a single file retains only its filename.
    assert list(
        module_0.get_input_output_paths(str(main_file), str(output_dir), None)
    ) == [
        InputOutput(main_file, output_dir / "main.py"),
    ]

    # With a root, a single file retains its path relative to that root.
    assert list(
        module_0.get_input_output_paths(
            str(module_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    actual = set(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = {
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    }
    assert actual == expected

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "result.py"),
                None,
            )
        )

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 02:42:33.045725
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = package_dir / "module.py"
    module.write_text("print('hello')\n")

    nested_module = package_dir / "nested.py"
    nested_module.write_text("x = 1\n")

    non_python_file = package_dir / "README.md"
    non_python_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = output_dir / "renamed.py"
    result = list(module_0.get_input_output_paths(
        str(module), str(output_file), root=None
    ))
    assert result == [InputOutput(module, output_file)]

    # Python file to directory without an explicit root.
    result = list(module_0.get_input_output_paths(
        str(module), str(output_dir), root=None
    ))
    assert result == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to directory relative to an explicit root.
    result = list(module_0.get_input_output_paths(
        str(module), str(output_dir), root=str(source_dir)
    ))
    assert result == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    result = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), root=None
    ))
    expected = [
        InputOutput(
            module,
            output_dir / "package" / "module.py",
        ),
        InputOutput(
            nested_module,
            output_dir / "package" / "nested.py",
        ),
    ]
    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_dir / "result.py"), root=None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), root=None
        ))

# Generated at 2026-10-25 02:42:45.326452
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_file = tmp_path / "source.py"
    source_file.write_text("print('hello')\n")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # Python file to Python file.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to output directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "source.py")
    ]

    # Python file to output directory with an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source_file, output_dir / "source.py")
    ]

    # Directory input recursively includes only Python files.
    input_dir = tmp_path / "package"
    nested_dir = input_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_python_file = input_dir / "first.py"
    second_python_file = nested_dir / "second.py"
    ignored_file = nested_dir / "README.md"

    first_python_file.write_text("x = 1\n")
    second_python_file.write_text("x = 2\n")
    ignored_file.write_text("Not Python\n")

    result = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))

    assert len(result) == 2
    assert InputOutput(
        first_python_file,
        output_dir / "first.py",
    ) in result
    assert InputOutput(
        second_python_file,
        output_dir / "nested" / "second.py",
    ) in result

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    missing_input = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))

# Generated at 2026-10-25 02:42:47.744919
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:50.160302
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:52.574410
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:54.990109
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:42:57.406047
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:00.001731
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:02.419367
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:04.830585
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:07.245898
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:09.661289
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:12.078242
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:14.493773
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:16.909466
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:19.324198
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:21.738973
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:24.153412
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:26.571610
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:28.981701
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:31.557883
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:43:42.576875
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 02:43:53.963118
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = source_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_dir / "README.md"

    source_file.write_text("print('main')\n")
    nested_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Without a root, a file keeps its name under the output directory.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # With a root, the path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively; non-Python files are ignored.
    assert set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == {
        InputOutput(source_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    }

    # A directory/non-Python input cannot map to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-25 02:44:10.428288
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "project" / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    module_file = package_dir / "module.py"
    non_python_file = package_dir / "README.md"

    main_file.write_text("print('main')", encoding="utf-8")
    module_file.write_text("print('module')", encoding="utf-8")
    non_python_file.write_text("Not Python", encoding="utf-8")

    output_dir = tmp_path / "output"

    # A Python input file can map directly to a Python output file.
    output_file = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(main_file, output_file)
    ]

    # Without a root, a file keeps its name under the output directory.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # With a root, the file's path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # A directory cannot be mapped to a single Python file.
    # list() is required because this function is a lazy generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 02:44:12.846684
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:44:15.262286
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:44:17.676077
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:44:20.091264
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:44:22.504956
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 02:44:24.921378
# Unit test for function get_input_output_paths