

# Generated at 2026-10-25 01:09:05.698916
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    input_dir = root / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_input = input_dir / "first.py"
    second_input = nested_dir / "second.py"
    ignored_input = nested_dir / "README.md"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("ignored")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # Without a root, a single file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # With a root, the file's relative path is preserved.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(root)
    )) == [
        InputOutput(first_input, output_dir / "src" / "first.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    actual = set(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    assert actual == {
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    }

    # An explicit root is also respected for directory inputs.
    actual = set(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), str(root)
    ))
    assert actual == {
        InputOutput(first_input, output_dir / "src" / "first.py"),
        InputOutput(
            second_input,
            output_dir / "src" / "package" / "second.py",
        ),
    }

    # Generator functions do not execute until iterated, hence list(...).
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(tmp_path / "invalid.py"), None
        ))

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:09:08.116651
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:10.528570
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:13.060678
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:15.474475
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:17.889058
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:20.304839
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:22.719470
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:25.134257
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:09:31.997579
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:09:44.826638
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # type: ignore


def test_get_input_output_paths(tmp_path):
    # A Python file mapped directly to another Python file.
    source = tmp_path / "source.py"
    source.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(source),
        str(tmp_path / "result.py"),
        None,
    ))

    assert result == [
        InputOutput(source, tmp_path / "result.py")
    ]

    # A Python file mapped into an output directory.
    output_dir = tmp_path / "output"
    result = list(module_0.get_input_output_paths(
        str(source),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(source, output_dir / "source.py")
    ]

    # A directory is searched recursively for Python files.
    input_dir = tmp_path / "input"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "README.txt"

    first_file.write_text("")
    second_file.write_text("")
    ignored_file.write_text("ignored")

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert sorted(result, key=lambda item: str(item)) == sorted([
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ], key=lambda item: str(item))

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "single.py"),
            None,
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 01:10:03.349832
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path) -> None:
    source = tmp_path / "src" / "main.py"
    source.parent.mkdir()
    source.write_text("print('hello')")

    # Python file to Python file.
    destination_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source), str(destination_file), None
    )) == [
        InputOutput(source, destination_file)
    ]

    # Python file to output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source), str(output_dir), None
    )) == [
        InputOutput(source, output_dir / "main.py")
    ]

    # Python file to output directory relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source, output_dir / "src" / "main.py")
    ]

    # Directory input recursively includes only Python files.
    package_dir = tmp_path / "package"
    module = package_dir / "nested" / "module.py"
    module.parent.mkdir(parents=True)
    module.write_text("VALUE = 1")
    (module.parent / "ignored.txt").write_text("not Python")

    assert list(module_0.get_input_output_paths(
        str(package_dir), str(output_dir), None
    )) == [
        InputOutput(module, output_dir / "nested" / "module.py")
    ]

    # Directory input relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(package_dir), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(module, output_dir / "package" / "nested" / "module.py")
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package_dir), str(destination_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:10:05.765879
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:08.180619
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:10.594926
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:13.009035
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:15.424293
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:17.839539
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:20.254537
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:22.669969
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:25.085567
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:27.685770
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:30.102340
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:32.517305
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:10:44.622694
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:14.145321
# Unit test for function get_input_output_paths
def test_get_input_output_paths():from pathlib import Path

# Generated at 2026-10-25 01:11:27.636069
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "project"
    package_dir = source_root / "package"
    package_dir.mkdir(parents=True)

    first_input = package_dir / "first.py"
    second_input = package_dir / "nested" / "second.py"
    second_input.parent.mkdir()
    first_input.write_text("print('first')", encoding="utf-8")
    second_input.write_text("print('second')", encoding="utf-8")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # Without a root, a single file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(first_input, output_dir / "package" / "first.py")
    ]

    # Directory inputs recursively include all Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    assert len(results) == 2
    assert InputOutput(
        first_input, output_dir / "package" / "first.py"
    ) in results
    assert InputOutput(
        second_input, output_dir / "package" / "nested" / "second.py"
    ) in results

    # A directory/non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:11:30.053256
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:32.470760
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:34.886438
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:37.302438
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:39.717848
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:11:48.614932
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-25 01:12:03.465242
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.paths import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths_file_to_file(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_path),
        root=None,
    ))

    assert result == [InputOutput(input_path, output_path)]


def test_get_input_output_paths_file_to_directory(tmp_path):
    input_path = tmp_path / "input.py"
    output_directory = tmp_path / "output"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_directory),
        root=None,
    ))

    assert result == [
        InputOutput(input_path, output_directory / "input.py")
    ]


def test_get_input_output_paths_file_to_directory_with_root(tmp_path):
    root = tmp_path / "source"
    input_path = root / "package" / "input.py"
    output_directory = tmp_path / "output"

    input_path.parent.mkdir(parents=True)
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_directory),
        root=str(root),
    ))

    assert result == [
        InputOutput(
            input_path,
            output_directory / "package" / "input.py",
        )
    ]


def test_get_input_output_paths_directory_recursively(tmp_path):
    input_directory = tmp_path / "source"
    output_directory = tmp_path / "output"

    first_input = input_directory / "first.py"
    second_input = input_directory / "package" / "second.py"
    ignored_input = input_directory / "package" / "README.txt"

    second_input.parent.mkdir(parents=True)
    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    result = list(module_0.get_input_output_paths(
        str(input_directory),
        str(output_directory),
        root=None,
    ))

    expected = [
        InputOutput(first_input, output_directory / "first.py"),
        InputOutput(
            second_input,
            output_directory / "package" / "second.py",
        ),
    ]

    # Avoid depending on filesystem traversal order.
    assert sorted(result, key=repr) == sorted(expected, key=repr)


def test_get_input_output_paths_rejects_directory_to_python_file(tmp_path):
    input_directory = tmp_path / "source"
    input_directory.mkdir()

    with pytest.raises(InvalidInputOutput):
        # The function is a generator, so it must be consumed to execute it.
        list(module_0.get_input_output_paths(
            str(input_directory),
            str(tmp_path / "output.py"),
            root=None,
        ))


def test_get_input_output_paths_rejects_missing_input(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(tmp_path / "output.py"),
            root=None,
        ))

# Generated at 2026-10-25 01:12:17.187149
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust this import to match your project structure.
from your_package.your_module import (
    get_input_output_paths,
    InputOutput,
    InputDoesntExists,
    InvalidInputOutput,
)


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    nested_dir = source_root / "package"
    nested_dir.mkdir(parents=True)

    source_file = source_root / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_root / "README.md"

    source_file.write_text("print('main')")
    nested_file.write_text("print('module')")
    ignored_file.write_text("Not Python")

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file maps to its filename inside an output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # When root is specified, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # A directory recursively maps only its Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))

    assert sorted(results, key=lambda pair: str(pair[0])) == sorted(
        [
            InputOutput(source_file, output_dir / "main.py"),
            InputOutput(nested_file, output_dir / "package" / "module.py"),
        ],
        key=lambda pair: str(pair[0]),
    )

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # A missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:12:19.712096
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:22.126126
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:24.647466
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:27.065136
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:29.656900
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:32.071837
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:34.486124
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:36.901969
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:39.319065
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:41.745493
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:44.159106
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:46.574590
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:48.989700
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:51.414735
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:53.828134
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:56.243305
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:12:58.657673
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:01.071841
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:03.486834
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:05.903616
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:08.317781
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:26.940342
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    source_file = package_dir / "module.py"
    source_file.write_text("print('hello')\n")

    ignored_file = package_dir / "README.txt"
    ignored_file.write_text("Ignored\n")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # A root preserves the source file's relative path.
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

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:13:37.601124
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    source_file = package / "module.py"
    source_file.write_text("print('hello')\n")

    ignored_file = package / "README.md"
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "dist"

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(explicit_output), None
    )) == [
        InputOutput(source_file, explicit_output)
    ]

    # Python file to a directory, without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # Python file to a directory, preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    assert list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(tmp_path / "result.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:13:50.062631
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    input_dir.mkdir()

    python_file = input_dir / "module.py"
    python_file.write_text("print('hello')")

    nested_dir = input_dir / "package"
    nested_dir.mkdir()
    nested_file = nested_dir / "nested.py"
    nested_file.write_text("pass")

    non_python_file = input_dir / "README.md"
    non_python_file.write_text("Not Python")

    output_dir = tmp_path / "dist"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(python_file), str(output_file), None
    )) == [
        InputOutput(python_file, output_file)
    ]

    # Without a root, a single file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(
        str(python_file), str(output_dir), None
    )) == [
        InputOutput(python_file, output_dir / "module.py")
    ]

    # With a root, the file's relative path is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(input_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "nested.py")
    ]

    # Directory input recursively includes only Python files.
    assert set(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    )) == {
        InputOutput(python_file, output_dir / "module.py"),
        InputOutput(nested_file, output_dir / "package" / "nested.py"),
    }

    # A directory/non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:13:52.479873
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:55.044294
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:57.460614
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:13:59.875759
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:02.290787
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:04.704836
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:07.119034
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:09.646905
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:19.758410
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-25 01:14:39.139051
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


# Unit test for function get_input_output_paths
def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    package_dir = input_dir / "package"
    package_dir.mkdir(parents=True)

    input_file = package_dir / "module.py"
    input_file.write_text("print('hello')\n")

    # Non-Python files should be ignored when processing a directory.
    (package_dir / "README.md").write_text("documentation")

    output_dir = tmp_path / "build"

    # A Python input file can map directly to a Python output file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Without a root, only the input file name is appended.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "module.py")
    ]

    # With a root, the input's path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(input_dir)
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # Directory inputs are searched recursively for Python files.
    assert list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # An explicit root is also honored for directory inputs.
    assert list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(
            input_file,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # A directory input cannot map to a single Python output file.
    # list() is required because the function is a lazy generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # Missing inputs raise InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:14:41.553260
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:43.966616
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:46.492928
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:48.904348
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:51.322145
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:53.736676
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:56.150943
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:14:58.715189
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:01.130427
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:03.545019
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:06.144606
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:08.559979
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:10.974691
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:13.393510
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:15.803276
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:18.218901
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:20.635243
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:23.051702
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:25.466870
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:27.882206
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:30.297650
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:32.712425
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:35.127851
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:37.545563
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:39.958613
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:42.372875
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:44.790794
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:47.204360
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:49.621181
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:52.034033
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:54.448973
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:56.864621
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:15:59.278950
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:01.696029
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:04.112249
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:06.528345
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:08.942687
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:11.357383
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:13.773454
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:16.188607
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:18.604128
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:21.020499
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:23.437835
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:25.851297
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:28.273156
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:30.687970
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:33.105707
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:35.520047
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:37.933243
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:40.350913
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:42.764367
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:45.181360
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:47.597741
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:50.011434
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:52.425875
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:54.841807
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:57.259827
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:16:59.671133
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:02.086171
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:04.502825
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:06.919566
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:09.332169
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:11.746994
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:14.161362
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:25.395616
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:17:37.935922
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    source = tmp_path / "source.py"
    source.write_text("print('hello')\n")
    destination = tmp_path / "destination.py"

    assert list(module_0.get_input_output_paths(
        str(source), str(destination), None
    )) == [InputOutput(source, destination)]

    # Python file -> output directory
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(source), str(output_dir), None
    )) == [InputOutput(source, output_dir / "source.py")]

    # Python file -> output directory, preserving path relative to root
    project = tmp_path / "project"
    nested_source = project / "package" / "module.py"
    nested_source.parent.mkdir(parents=True)
    nested_source.write_text("value = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_source), str(output_dir), str(project)
    )) == [
        InputOutput(nested_source, output_dir / "package" / "module.py")
    ]

    # Input directory -> recursively discovered Python files
    input_dir = tmp_path / "inputs"
    first = input_dir / "first.py"
    second = input_dir / "nested" / "second.py"
    ignored = input_dir / "nested" / "README.txt"

    second.parent.mkdir(parents=True)
    first.write_text("first = True\n")
    second.write_text("second = True\n")
    ignored.write_text("not Python\n")

    actual = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first, output_dir / "first.py"),
        InputOutput(second, output_dir / "nested" / "second.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(tmp_path / "combined.py"), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:17:49.987636
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    package.mkdir(parents=True)

    first_file = package / "first.py"
    second_file = package / "nested" / "second.py"
    ignored_file = package / "README.md"

    first_file.write_text("print('first')")
    second_file.parent.mkdir()
    second_file.write_text("print('second')")
    ignored_file.write_text("Not a Python file")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [InputOutput(first_file, output_file)]

    # Python file to an output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [InputOutput(first_file, output_dir / "first.py")]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), str(project)
    )) == [InputOutput(first_file, output_dir / "package" / "first.py")]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(package), str(output_dir), str(project)
    ))
    expected = [
        InputOutput(first_file, output_dir / "package" / "first.py"),
        InputOutput(
            second_file,
            output_dir / "package" / "nested" / "second.py",
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(tmp_path / "combined.py"), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:17:52.506821
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:54.920990
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:57.338256
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:17:59.751331
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:02.338548
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:04.754528
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:07.169618
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:09.583375
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:12.002405
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:14.418326
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:18:29.703985
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:18:43.133536
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        input_dir = root / "src"
        package_dir = input_dir / "package"
        output_dir = root / "output"

        package_dir.mkdir(parents=True)

        main_file = input_dir / "main.py"
        module_file = package_dir / "module.py"
        ignored_file = package_dir / "README.md"

        main_file.write_text("print('main')\n")
        module_file.write_text("print('module')\n")
        ignored_file.write_text("Not a Python file\n")

        # Python file to Python file.
        explicit_output = root / "result.py"
        assert list(module_0.get_input_output_paths(
            str(main_file), str(explicit_output), None
        )) == [
            InputOutput(main_file, explicit_output)
        ]

        # Python file to an output directory.
        assert list(module_0.get_input_output_paths(
            str(main_file), str(output_dir), None
        )) == [
            InputOutput(main_file, output_dir / "main.py")
        ]

        # Directory input is traversed recursively; non-Python files are ignored.
        results = list(module_0.get_input_output_paths(
            str(input_dir), str(output_dir), None
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
                str(input_dir), str(root / "output.py"), None
            ))

        # The input path must exist.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(root / "missing.py"), str(output_dir), None
            ))

# Generated at 2026-10-25 01:18:58.186316
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('module')")

    top_level = source_root / "main.py"
    top_level.write_text("print('main')")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(module), str(explicit_output), None
    )) == [
        InputOutput(module, explicit_output)
    ]

    # Python file to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), None
    )) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), str(source_root)
    )) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively discovers Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(top_level, output_dir / "main.py"),
        InputOutput(module, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(explicit_output), None
        ))

    # Input must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))