

# Generated at 2026-10-24 04:54:34.909067
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest
from pathlib import Path

# Adjust this import to match your project structure.
from your_package.your_module import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path: Path):
    source_root = tmp_path / "source"
    package_dir = source_root / "package"
    package_dir.mkdir(parents=True)

    first_input = source_root / "main.py"
    second_input = package_dir / "module.py"
    ignored_input = package_dir / "README.md"

    first_input.write_text("print('main')\n")
    second_input.write_text("print('module')\n")
    ignored_input.write_text("Not Python\n")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "generated.py"
    assert list(
        module_0.get_input_output_paths(str(first_input), str(output_file), None)
    ) == [
        InputOutput(first_input, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(
        module_0.get_input_output_paths(str(first_input), str(output_dir), None)
    ) == [
        InputOutput(first_input, output_dir / "main.py")
    ]

    # A Python file mapped relative to an explicit root.
    assert list(
        module_0.get_input_output_paths(str(second_input), str(output_dir), str(source_root))
    ) == [
        InputOutput(second_input, output_dir / "package" / "module.py")
    ]

    # A directory is searched recursively, and non-Python files are ignored.
    results = list(
        module_0.get_input_output_paths(str(source_root), str(output_dir), None)
    )
    assert len(results) == 2
    assert InputOutput(first_input, output_dir / "main.py") in results
    assert InputOutput(
        second_input, output_dir / "package" / "module.py"
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_root),
                str(tmp_path / "single.py"),
                None,
            )
        )

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 04:54:54.781851
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        source = root / "src"
        package = source / "package"
        source.mkdir()
        package.mkdir()

        main_file = source / "main.py"
        helper_file = package / "helper.py"
        ignored_file = source / "README.md"

        main_file.write_text("print('main')")
        helper_file.write_text("print('helper')")
        ignored_file.write_text("Not Python")

        output = root / "output"

        # A Python file can map directly to another Python file.
        destination_file = root / "result.py"
        assert list(
            module_0.get_input_output_paths(
                str(main_file), str(destination_file), root=None
            )
        ) == [InputOutput(main_file, destination_file)]

        # Without an explicit root, only the input filename is appended.
        assert list(
            module_0.get_input_output_paths(str(main_file), str(output), root=None)
        ) == [InputOutput(main_file, output / "main.py")]

        # With an explicit root, the relative directory structure is kept.
        assert list(
            module_0.get_input_output_paths(
                str(main_file), str(output), root=str(root)
            )
        ) == [InputOutput(main_file, output / "src" / "main.py")]

        # Directories are searched recursively, and non-Python files are ignored.
        actual = list(
            module_0.get_input_output_paths(str(source), str(output), root=None)
        )
        expected = [
            InputOutput(main_file, output / "main.py"),
            InputOutput(helper_file, output / "package" / "helper.py"),
        ]

        assert len(actual) == len(expected)
        assert all(item in actual for item in expected)

        # A directory cannot be mapped to a single Python output file.
        with pytest.raises(InvalidInputOutput):
            list(
                module_0.get_input_output_paths(
                    str(source), str(root / "combined.py"), root=None
                )
            )

        # Generator execution must be forced for the exception to be raised.
        with pytest.raises(InputDoesntExists):
            list(
                module_0.get_input_output_paths(
                    str(root / "missing"), str(output), root=None
                )
            )

# Generated at 2026-10-24 04:55:15.984175
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    source_dir = root / "src"
    source_dir.mkdir(parents=True)

    source_file = source_dir / "module.py"
    source_file.write_text("print('hello')\n", encoding="utf-8")

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(direct_output), None
    )) == [
        InputOutput(Path(str(source_file)), Path(str(direct_output)))
    ]

    # Without a root, only the input filename is appended.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(source_file)),
            Path(str(output_dir / "module.py")),
        )
    ]

    # With a root, the input path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(root)
    )) == [
        InputOutput(
            Path(str(source_file)),
            Path(str(output_dir / "src" / "module.py")),
        )
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    package_dir = tmp_path / "package"
    nested_dir = package_dir / "nested"
    nested_dir.mkdir(parents=True)

    nested_file = nested_dir / "example.py"
    nested_file.write_text("x = 1\n", encoding="utf-8")
    (nested_dir / "ignored.txt").write_text("ignored\n", encoding="utf-8")

    assert list(module_0.get_input_output_paths(
        str(package_dir), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(nested_file)),
            Path(str(output_dir / "nested" / "example.py")),
        )
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package_dir), str(tmp_path / "single.py"), None
        ))

    # Validation occurs when the generator is consumed.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-24 04:55:30.314643
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace `your_package.your_module` with the module containing the function.
from your_package.your_module import (
    InputOutput,
    InputDoesntExists,
    InvalidInputOutput,
    get_input_output_paths,
)


def test_get_input_output_paths(tmp_path):
    source = tmp_path / "source"
    source.mkdir()

    package = source / "package"
    package.mkdir()

    module = package / "module.py"
    module.write_text("print('hello')")

    second_module = source / "other.py"
    second_module.write_text("x = 1")

    ignored_file = source / "README.md"
    ignored_file.write_text("Not a Python file")

    output = tmp_path / "output"

    # Python file to Python file.
    explicit_output = output / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(module), str(explicit_output), None
    )) == [
        InputOutput(module, explicit_output)
    ]

    # Python file to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output), None
    )) == [
        InputOutput(module, output / "module.py")
    ]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output), str(source)
    )) == [
        InputOutput(module, output / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source), str(output), None
    ))
    expected = [
        InputOutput(module, output / "package" / "module.py"),
        InputOutput(second_module, output / "other.py"),
    ]
    assert sorted(actual, key=lambda item: str(item)) == sorted(
        expected, key=lambda item: str(item)
    )

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source), str(output / "result.py"), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output), None
        ))

# Generated at 2026-10-24 04:55:43.935696
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = input_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(first_file), str(output_file), None)) == [
        InputOutput(first_file, output_file)
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(str(first_file), str(output_dir), None)) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # Supplying a root preserves the path relative to that root.
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_dir), str(tmp_path))
    ) == [
        InputOutput(first_file, output_dir / "src" / "first.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    results = list(
        module_0.get_input_output_paths(str(input_dir), str(output_dir), None)
    )
    assert len(results) == 2
    assert InputOutput(first_file, output_dir / "first.py") in results
    assert InputOutput(second_file, output_dir / "nested" / "second.py") in results

    # A directory cannot be mapped to a single Python file.
    # list() is required because this function is a generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
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

# Generated at 2026-10-24 04:56:00.214668
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    input_dir = root / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    input_file = nested_dir / "module.py"
    input_file.write_text("print('hello')\n", encoding="utf-8")

    # Python file to Python file.
    explicit_output = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(explicit_output), None
    )) == [
        InputOutput(input_file, explicit_output)
    ]

    # Python file to an output directory, without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "module.py")
    ]

    # Python file to an output directory, preserving its path from root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(root)
    )) == [
        InputOutput(input_file, output_dir / "src/package/module.py")
    ]

    # Directory input is searched recursively.
    assert list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "package/module.py")
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(tmp_path / "output.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:56:19.993854
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    input_file = package / "example.py"
    input_file.write_text("print('hello')\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file to an output directory without a root.
    output_directory = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_directory), None
    )) == [
        InputOutput(input_file, output_directory / "example.py")
    ]

    # Python file to an output directory while preserving its root-relative path.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_directory), str(source_root)
    )) == [
        InputOutput(
            input_file,
            output_directory / "package" / "example.py",
        )
    ]

    # Directory input recursively includes only Python files.
    ignored_file = package / "README.txt"
    ignored_file.write_text("ignored\n")

    assert list(module_0.get_input_output_paths(
        str(source_root), str(output_directory), None
    )) == [
        InputOutput(
            input_file,
            output_directory / "package" / "example.py",
        )
    ]

    # A directory/non-Python input cannot target a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # The input must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_directory), None
        ))

# Generated at 2026-10-24 04:56:34.724663
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A single Python file mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')", encoding="utf-8")

    output_file = tmp_path / "output.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A single Python file mapped into an output directory.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # A single Python file with its path preserved relative to root.
    source_dir = tmp_path / "src"
    nested_file = source_dir / "package" / "module.py"
    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("value = 1", encoding="utf-8")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # A directory recursively maps only Python files.
    another_file = source_dir / "main.py"
    another_file.write_text("from package import module", encoding="utf-8")
    ignored_file = source_dir / "README.md"
    ignored_file.write_text("Ignored", encoding="utf-8")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    assert set(results) == {
        InputOutput(another_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    }

    # A directory cannot be mapped to a single .py output.
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

# Generated at 2026-10-24 04:56:49.372059
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "source"
    package = source_root / "package"
    package.mkdir(parents=True)

    main_file = source_root / "main.py"
    child_file = package / "child.py"
    ignored_file = package / "README.txt"

    main_file.write_text("print('main')\n")
    child_file.write_text("print('child')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(main_file), str(output_file), None)) == [
        InputOutput(main_file, output_file)
    ]

    # With a directory output and no root, retain only the filename.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # With an explicit root, retain the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(child_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(child_file, output_dir / "package" / "child.py")
    ]

    # Directory inputs are searched recursively for Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(child_file, output_dir / "package" / "child.py"),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # An explicit parent root preserves the input directory name.
    actual = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), str(tmp_path)
    ))
    expected = [
        InputOutput(main_file, output_dir / "source" / "main.py"),
        InputOutput(
            child_file,
            output_dir / "source" / "package" / "child.py",
        ),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A directory input cannot map to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:57:03.808669
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    top_level_file = source_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = nested_dir / "README.md"

    top_level_file.write_text("print('main')")
    nested_file.write_text("print('module')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    target_file = tmp_path / "target.py"
    assert list(module_0.get_input_output_paths(
        str(top_level_file), str(target_file), None
    )) == [
        InputOutput(top_level_file, target_file)
    ]

    # Python file to output directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), None
    )) == [
        InputOutput(nested_file, output_dir / "module.py")
    ]

    # Python file to output directory relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    actual = set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = {
        InputOutput(top_level_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    }
    assert actual == expected

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(target_file), None
        ))

    # Input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:57:06.309303
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:08.723410
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:11.134984
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:13.545229
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:15.958254
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:18.369097
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:20.781253
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:23.190508
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:25.602093
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:28.013718
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:30.424700
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:32.836561
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:35.249139
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:37.661716
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:40.072933
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:42.485261
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:57:44.918880
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:07.908102
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:28.900508
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:31.316677
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:33.731640
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:36.143104
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:38.556903
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:40.972338
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:43.398124
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:45.796414
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:48.212745
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:50.628375
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:53.040711
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:58:55.455799
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:59:16.929505
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-24 04:59:44.479998
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "root"
    package = root / "package"
    nested = package / "nested"
    nested.mkdir(parents=True)

    first_input = package / "first.py"
    second_input = nested / "second.py"
    ignored_input = package / "ignored.txt"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(explicit_output), None
    )) == [
        InputOutput(Path(first_input), Path(explicit_output))
    ]

    # Python file to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(Path(first_input), Path(output_dir / "first.py"))
    ]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(root)
    )) == [
        InputOutput(
            Path(first_input),
            Path(output_dir / "package" / "first.py"),
        )
    ]

    # Directory input recursively includes only Python files.
    pairs = list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    ))
    assert len(pairs) == 2
    assert InputOutput(
        Path(first_input), Path(output_dir / "first.py")
    ) in pairs
    assert InputOutput(
        Path(second_input), Path(output_dir / "nested" / "second.py")
    ) in pairs

    # Directory input with an explicit root preserves its relative path.
    rooted_pairs = list(module_0.get_input_output_paths(
        str(package), str(output_dir), str(root)
    ))
    assert len(rooted_pairs) == 2
    assert InputOutput(
        Path(first_input),
        Path(output_dir / "package" / "first.py"),
    ) in rooted_pairs
    assert InputOutput(
        Path(second_input),
        Path(output_dir / "package" / "nested" / "second.py"),
    ) in rooted_pairs

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(tmp_path / "output.py"), None
        ))

    # Missing input raises when the generator is consumed.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:59:58.912120
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")
    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # Python file -> output directory.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # Preserve the path relative to an explicit root.
    root = tmp_path / "project"
    nested_input = root / "src" / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("pass\n")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(
            nested_input,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # Input directory -> recursively discovered Python files.
    source_dir = tmp_path / "sources"
    first_file = source_dir / "first.py"
    second_file = source_dir / "nested" / "second.py"
    ignored_file = source_dir / "nested" / "ignored.txt"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("pass\n")
    second_file.write_text("pass\n")
    ignored_file.write_text("not Python\n")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    assert len(results) == 2
    assert InputOutput(first_file, output_dir / "first.py") in results
    assert InputOutput(
        second_file, output_dir / "nested" / "second.py"
    ) in results

    # A directory cannot be mapped to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:00:13.685535
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    main_file = source_dir / "main.py"
    main_file.write_text("print('main')")

    nested_dir = source_dir / "package"
    nested_dir.mkdir()

    nested_file = nested_dir / "module.py"
    nested_file.write_text("print('module')")

    ignored_file = nested_dir / "README.txt"
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(main_file, output_file)
    ]

    # Without a root, the input filename is appended to the output directory.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # With a root, the input path relative to that root is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # A nonexistent input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:00:28.328261
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust this import to match your package structure.
# from your_package.module import get_input_output_paths
# from your_package.types import InputOutput
# from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "source"
    package = source_root / "package"
    package.mkdir(parents=True)

    first_file = source_root / "first.py"
    second_file = package / "second.py"
    ignored_file = source_root / "README.md"

    first_file.write_text("print('first')", encoding="utf-8")
    second_file.write_text("print('second')", encoding="utf-8")
    ignored_file.write_text("Not Python", encoding="utf-8")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(direct_output), None
    )) == [
        InputOutput(first_file, direct_output)
    ]

    # Without root, a file is placed under output using its basename.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # With root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]
    assert sorted(map(repr, actual)) == sorted(map(repr, expected))

    # A directory/non-Python input cannot map to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(tmp_path / "result.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:00:42.036564
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('module')\n")

    ignored_file = package / "README.md"
    ignored_file.write_text("Not a Python file\n")

    # Python file to Python file.
    output_file = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(module), str(output_file), None
    )) == [
        InputOutput(module, output_file)
    ]

    # Python file to an output directory, without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), None
    )) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to an output directory, preserving its path from root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), str(source_root)
    )) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    assert results == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # A directory cannot be mapped to a single Python output file.
    # list() is required because this function is a generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:01:02.298451
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file to Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")
    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # Python file to output directory without an explicit root.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # Directory input, preserving paths relative to the input directory.
    root_dir = tmp_path / "project"
    nested_dir = root_dir / "package"
    nested_dir.mkdir(parents=True)

    nested_file = nested_dir / "module.py"
    nested_file.write_text("VALUE = 1\n")
    (nested_dir / "ignored.txt").write_text("not Python\n")

    assert list(module_0.get_input_output_paths(
        str(root_dir), str(output_dir), None
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Explicit root preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(root_dir), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(
            nested_file,
            output_dir / "project" / "package" / "module.py",
        )
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(root_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-24 05:01:16.647776
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust these imports to match your package/module structure.
from your_package.module import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    first_file = source_root / "main.py"
    second_file = package / "module.py"
    ignored_file = source_root / "README.md"

    first_file.write_text("print('main')\n")
    second_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(direct_output), None
    )) == [
        InputOutput(first_file, direct_output)
    ]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "main.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(second_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    actual = set(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    assert actual == {
        InputOutput(first_file, output_dir / "main.py"),
        InputOutput(second_file, output_dir / "package" / "module.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(direct_output), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:01:31.795823
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    source_dir = project / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_dir / "README.md"

    main_file.write_text("print('main')\n")
    nested_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "renamed.py"
    assert list(
        module_0.get_input_output_paths(str(main_file), str(direct_output), None)
    ) == [InputOutput(main_file, direct_output)]

    # Without root, a file keeps its filename under the output directory.
    output_dir = tmp_path / "output"
    assert list(
        module_0.get_input_output_paths(str(main_file), str(output_dir), None)
    ) == [InputOutput(main_file, output_dir / "main.py")]

    # With root, the source path relative to root is preserved.
    rooted_output = tmp_path / "rooted-output"
    assert list(
        module_0.get_input_output_paths(
            str(nested_file),
            str(rooted_output),
            str(project),
        )
    ) == [
        InputOutput(
            nested_file,
            rooted_output / "src" / "package" / "module.py",
        )
    ]

    # Directories are searched recursively, ignoring non-Python files.
    directory_results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected_results = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    assert len(directory_results) == len(expected_results)
    assert all(result in directory_results for result in expected_results)

    # A directory or non-Python input cannot map to a single .py output.
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
                str(tmp_path / "does-not-exist"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 05:01:46.041504
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_input = input_dir / "main.py"
    second_input = nested_dir / "module.py"
    ignored_input = input_dir / "README.md"

    first_input.write_text("print('main')")
    second_input.write_text("print('module')")
    ignored_input.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # Directory input: recursively returns only Python files.
    results = set(
        module_0.get_input_output_paths(str(input_dir), str(output_dir), root=None)
    )

    assert results == {
        InputOutput(first_input, output_dir / "main.py"),
        InputOutput(second_input, output_dir / "package" / "module.py"),
    }

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(first_input), str(output_file), root=None)
    ) == [
        InputOutput(first_input, output_file),
    ]

    # Python file to directory without an explicit root.
    assert list(
        module_0.get_input_output_paths(str(first_input), str(output_dir), root=None)
    ) == [
        InputOutput(first_input, output_dir / "main.py"),
    ]

    # Python file to directory with an explicit root.
    assert list(
        module_0.get_input_output_paths(
            str(second_input),
            str(output_dir),
            root=str(input_dir),
        )
    ) == [
        InputOutput(second_input, output_dir / "package" / "module.py"),
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(input_dir),
                str(output_file),
                root=None,
            )
        )

    # Missing input path.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                root=None,
            )
        )

# Generated at 2026-10-24 05:02:01.384171
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Arrange
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    main_file = input_dir / "main.py"
    module_file = nested_dir / "module.py"
    ignored_file = nested_dir / "README.md"

    main_file.write_text("")
    module_file.write_text("")
    ignored_file.write_text("")

    output_dir = tmp_path / "output"

    # Python file -> Python file
    explicit_output = tmp_path / "result.py"
    result = list(module_0.get_input_output_paths(
        str(main_file),
        str(explicit_output),
        None,
    ))

    assert result == [InputOutput(main_file, explicit_output)]

    # Python file -> output directory
    result = list(module_0.get_input_output_paths(
        str(main_file),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(main_file, output_dir / "main.py"),
    ]

    # Directory -> output directory
    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A directory cannot be written to a single .py file
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(explicit_output),
            None,
        ))

    # Missing input
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-24 05:02:22.069720
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('hello')")

    nested = package / "nested"
    nested.mkdir()
    second_module = nested / "second.py"
    second_module.write_text("pass")

    non_python = package / "README.txt"
    non_python.write_text("ignored")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # Python file to an output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to an output directory relative to a supplied root.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(project))
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(
        module_0.get_input_output_paths(str(package), str(output_dir), None)
    )
    expected = [
        InputOutput(module, output_dir / "module.py"),
        InputOutput(second_module, output_dir / "nested" / "second.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A non-Python input cannot produce a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(non_python),
            str(output_file),
            None,
        ))

    # Missing input raises InputDoesntExists.
    missing = tmp_path / "missing"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-24 05:03:07.021496
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

    # When output is a directory, preserve the input filename.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # Preserve the path relative to the supplied root.
    root = tmp_path / "project"
    nested_input = root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Recursively map only Python files from an input directory.
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    first = source_dir / "first.py"
    second = source_dir / "nested" / "second.py"
    ignored = source_dir / "nested" / "notes.txt"

    second.parent.mkdir()
    first.write_text("FIRST = True")
    second.write_text("SECOND = True")
    ignored.write_text("not Python")

    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first, output_dir / "first.py"),
        InputOutput(second, output_dir / "nested" / "second.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:03:22.279466
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    first_input = package / "first.py"
    second_input = package / "nested" / "second.py"
    ignored_input = package / "ignored.txt"

    second_input.parent.mkdir()
    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # Without root, a single file keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # With root, a single file keeps its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(first_input, output_dir / "package" / "first.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    pairs = list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    ))
    assert len(pairs) == 2
    assert InputOutput(first_input, output_dir / "first.py") in pairs
    assert InputOutput(
        second_input, output_dir / "nested" / "second.py"
    ) in pairs

    # A custom root is also respected for directory input.
    pairs = list(module_0.get_input_output_paths(
        str(package), str(output_dir), str(source_root)
    ))
    assert len(pairs) == 2
    assert InputOutput(
        first_input, output_dir / "package" / "first.py"
    ) in pairs
    assert InputOutput(
        second_input, output_dir / "package" / "nested" / "second.py"
    ) in pairs

    # A directory cannot be mapped to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:03:34.207733
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = package_dir / "README.md"

    first_file.write_text("print('first')\n")
    second_file.write_text("print('second')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_file), None)
    ) == [
        InputOutput(first_file, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_dir), None)
    ) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # Preserve the path relative to an explicitly supplied root.
    assert list(
        module_0.get_input_output_paths(
            str(second_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # Recursively map all Python files in a directory.
    results = set(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    assert results == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_file),
                None,
            )
        )

    # A missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 05:03:53.819634
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    module_file = package_dir / "module.py"
    ignored_file = package_dir / "README.txt"

    main_file.write_text("print('main')", encoding="utf-8")
    module_file.write_text("print('module')", encoding="utf-8")
    ignored_file.write_text("ignored", encoding="utf-8")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(main_file), str(output_file), None)
    ) == [
        InputOutput(main_file, output_file)
    ]

    # Python file to an output directory without a root.
    output_dir = tmp_path / "output"
    assert list(
        module_0.get_input_output_paths(str(main_file), str(output_dir), None)
    ) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Python file to an output directory while preserving its root-relative path.
    assert list(
        module_0.get_input_output_paths(
            str(module_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 05:04:07.632038
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 05:04:15.961172
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-24 05:04:39.004019
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')", encoding="utf-8")
    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        root=None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # Python file -> output directory
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=None,
    )) == [
        InputOutput(input_file, output_dir / "input.py"),
    ]

    # Python file -> output directory with a custom root
    project_root = tmp_path / "project"
    nested_file = project_root / "package" / "module.py"
    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("VALUE = 1", encoding="utf-8")

    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        root=str(project_root),
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    # Input directory -> recursively discovered Python files
    source_dir = tmp_path / "src"
    first_file = source_dir / "first.py"
    second_file = source_dir / "nested" / "second.py"
    ignored_file = source_dir / "nested" / "notes.txt"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("", encoding="utf-8")
    second_file.write_text("", encoding="utf-8")
    ignored_file.write_text("", encoding="utf-8")

    results = list(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        root=None,
    ))

    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "nested" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(output_file),
            root=None,
        ))

    # Missing input
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            root=None,
        ))