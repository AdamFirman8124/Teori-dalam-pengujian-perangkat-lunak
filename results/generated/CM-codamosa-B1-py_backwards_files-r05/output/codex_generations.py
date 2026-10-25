

# Generated at 2026-10-25 01:38:57.307935
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temporary_directory:
        base_path = Path(temporary_directory)

        # Output cannot be a Python file when input is not one.
        non_python_input = base_path / "input.txt"
        non_python_input.write_text("text")

        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(non_python_input),
                str(base_path / "output.py"),
                None,
            ))

        # Input must exist.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(base_path / "missing.py"),
                str(base_path / "output"),
                None,
            ))

        # Python file to Python file.
        input_file = base_path / "input.py"
        input_file.write_text("print('hello')")

        output_file = base_path / "output.py"
        assert list(module_0.get_input_output_paths(
            str(input_file),
            str(output_file),
            None,
        )) == [InputOutput(input_file, output_file)]

        # Python file to output directory without an explicit root.
        output_directory = base_path / "dist"
        assert list(module_0.get_input_output_paths(
            str(input_file),
            str(output_directory),
            None,
        )) == [
            InputOutput(input_file, output_directory / "input.py"),
        ]

        # Python file to output directory relative to an explicit root.
        project_root = base_path / "project"
        nested_input = project_root / "package" / "module.py"
        nested_input.parent.mkdir(parents=True)
        nested_input.write_text("VALUE = 1")

        assert list(module_0.get_input_output_paths(
            str(nested_input),
            str(output_directory),
            str(project_root),
        )) == [
            InputOutput(
                nested_input,
                output_directory / "package" / "module.py",
            ),
        ]

        # Directory input recursively discovers only Python files.
        source_directory = base_path / "src"
        first_input = source_directory / "first.py"
        second_input = source_directory / "nested" / "second.py"
        ignored_input = source_directory / "ignored.txt"

        second_input.parent.mkdir(parents=True)
        first_input.write_text("FIRST = 1")
        second_input.write_text("SECOND = 2")
        ignored_input.write_text("ignored")

        results = list(module_0.get_input_output_paths(
            str(source_directory),
            str(output_directory),
            None,
        ))

        assert len(results) == 2
        assert InputOutput(
            first_input,
            output_directory / "first.py",
        ) in results
        assert InputOutput(
            second_input,
            output_directory / "nested" / "second.py",
        ) in results

# Generated at 2026-10-25 01:39:11.865654
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace with the actual module containing get_input_output_paths.
from your_package.module import (
    get_input_output_paths,
    InputOutput,
    InvalidInputOutput,
    InputDoesntExists,
)


def test_get_input_output_paths(tmp_path):
    source_file = tmp_path / "src" / "example.py"
    source_file.parent.mkdir()
    source_file.write_text("print('hello')")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Preserve the path relative to an explicitly supplied root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(source_file, output_dir / "src" / "example.py")
    ]

    # Directory input recursively includes only Python files.
    nested_file = tmp_path / "src" / "package" / "nested.py"
    nested_file.parent.mkdir()
    nested_file.write_text("x = 1")

    ignored_file = tmp_path / "src" / "README.txt"
    ignored_file.write_text("ignored")

    results = list(module_0.get_input_output_paths(
        str(tmp_path / "src"), str(output_dir), None
    ))

    assert len(results) == 2
    assert InputOutput(source_file, output_dir / "example.py") in results
    assert InputOutput(
        nested_file, output_dir / "package" / "nested.py"
    ) in results

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(tmp_path / "src"), str(output_file), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:39:24.124662
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')\n")

    other_file = source_dir / "README.md"
    other_file.write_text("Not Python\n")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    target_file = tmp_path / "target.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(target_file), None
    )) == [
        InputOutput(source_file, target_file)
    ]

    # Python file to an output directory.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # Preserve the path relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # Recursively process Python files in a directory.
    second_file = source_dir / "second.py"
    second_file.write_text("x = 1\n")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(second_file, output_dir / "second.py"),
        InputOutput(source_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory/non-Python input cannot map to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(target_file), None
        ))

    # Generator execution must be forced for the exception to be raised.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-25 01:39:41.497339
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
    ignored_file.write_text("Not Python\n")

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(tmp_path / "output.py"),
            None,
        ))

    # Generators must be consumed for exceptions to be raised.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            None,
        ))

    # Python file to Python file.
    destination_file = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(main_file),
        str(destination_file),
        None,
    )) == [
        InputOutput(main_file, destination_file),
    ]

    # Python file to directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(main_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(main_file, output_dir / "main.py"),
    ]

    # Python file to directory relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(module_file),
        str(output_dir),
        str(source_dir),
    )) == [
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        None,
    ))

    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

# Generated at 2026-10-25 01:39:44.148186
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:46.686756
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:49.210006
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:51.625618
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:54.189988
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:56.607731
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:39:59.023634
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:01.438691
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:03.852345
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:06.272374
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:40:16.247019
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:40:30.379644
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths_python_file_to_file(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_path),
        root=None,
    ))

    assert result == [InputOutput(input_path, output_path)]


def test_get_input_output_paths_python_file_to_directory(tmp_path):
    input_path = tmp_path / "input.py"
    output_directory = tmp_path / "dist"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_directory),
        root=None,
    ))

    assert result == [
        InputOutput(input_path, output_directory / "input.py")
    ]


def test_get_input_output_paths_file_with_root(tmp_path):
    root = tmp_path / "project"
    input_path = root / "src" / "input.py"
    output_directory = tmp_path / "dist"
    input_path.parent.mkdir(parents=True)
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_directory),
        root=str(root),
    ))

    assert result == [
        InputOutput(input_path, output_directory / "src" / "input.py")
    ]


def test_get_input_output_paths_directory(tmp_path):
    input_directory = tmp_path / "src"
    nested_directory = input_directory / "package"
    output_directory = tmp_path / "dist"

    nested_directory.mkdir(parents=True)
    first_input = input_directory / "first.py"
    second_input = nested_directory / "second.py"
    ignored_input = nested_directory / "notes.txt"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("ignored")

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

    assert len(result) == len(expected)
    assert all(item in result for item in expected)


def test_get_input_output_paths_missing_input(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            root=None,
        ))


def test_get_input_output_paths_rejects_directory_to_python_file(tmp_path):
    input_directory = tmp_path / "src"
    input_directory.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_directory),
            str(tmp_path / "output.py"),
            root=None,
        ))

# Generated at 2026-10-25 01:40:45.955131
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = package_dir / "module.py"
    module.write_text("print('hello')\n")

    nested_module = package_dir / "nested.py"
    nested_module.write_text("VALUE = 42\n")

    non_python_file = package_dir / "README.md"
    non_python_file.write_text("Ignored\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(
        str(module), str(output_file), None
    )) == [
        InputOutput(module, output_file)
    ]

    # Without root, only the input filename is appended.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), None
    )) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # With root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), str(source_dir)
    )) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory inputs recursively include only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(module, output_dir / "package" / "module.py"),
        InputOutput(nested_module, output_dir / "package" / "nested.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # A missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:41:04.792631
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A non-Python input cannot target a single Python file.
    non_python_input = tmp_path / "input.txt"
    non_python_input.write_text("content")

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(non_python_input),
            str(tmp_path / "output.py"),
            None,
        ))

    # Input must exist. The generator must be consumed to trigger validation.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            None,
        ))

    # Single Python file to single Python file.
    source_file = tmp_path / "source.py"
    source_file.write_text("print('hello')")

    destination_file = tmp_path / "destination.py"
    assert list(module_0.get_input_output_paths(
        str(source_file),
        str(destination_file),
        None,
    )) == [
        InputOutput(source_file, destination_file),
    ]

    # Single Python file to an output directory without a root.
    output_directory = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file),
        str(output_directory),
        None,
    )) == [
        InputOutput(source_file, output_directory / "source.py"),
    ]

    # Single Python file with its path preserved relative to root.
    source_root = tmp_path / "source-root"
    nested_source = source_root / "package" / "module.py"
    nested_source.parent.mkdir(parents=True)
    nested_source.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_source),
        str(output_directory),
        str(source_root),
    )) == [
        InputOutput(
            nested_source,
            output_directory / "package" / "module.py",
        ),
    ]

    # Directory input recursively includes only Python files.
    input_directory = tmp_path / "input"
    first_python_file = input_directory / "first.py"
    second_python_file = input_directory / "nested" / "second.py"
    ignored_file = input_directory / "nested" / "README.md"

    first_python_file.parent.mkdir(parents=True)
    second_python_file.parent.mkdir(parents=True)
    first_python_file.write_text("first = 1")
    second_python_file.write_text("second = 2")
    ignored_file.write_text("Not a Python file")

    results = list(module_0.get_input_output_paths(
        str(input_directory),
        str(output_directory),
        None,
    ))

    assert len(results) == 2
    assert InputOutput(
        first_python_file,
        output_directory / "first.py",
    ) in results
    assert InputOutput(
        second_python_file,
        output_directory / "nested" / "second.py",
    ) in results

# Generated at 2026-10-25 01:41:16.625846
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = source_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not Python")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [InputOutput(first_file, output_file)]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [InputOutput(first_file, output_dir / "first.py")]

    # Supplying a root preserves the file's path relative to that root.
    rooted_result = list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_dir)
    ))
    assert rooted_result == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    directory_results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected_results = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]

    assert len(directory_results) == len(expected_results)
    for expected in expected_results:
        assert expected in directory_results

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

# Generated at 2026-10-25 01:41:30.495815
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.your_module import (
    InputOutput,
    InputDoesntExists,
    InvalidInputOutput,
    get_input_output_paths,
)


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "project"
    package_dir = source_root / "package"
    package_dir.mkdir(parents=True)

    source_file = package_dir / "example.py"
    source_file.write_text("print('hello')\n")

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(explicit_output), None)
    ) == [
        InputOutput(source_file, explicit_output)
    ]

    # Python file to output directory without a root.
    output_dir = tmp_path / "output"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_dir), None)
    ) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Python file to output directory while preserving its path from root.
    assert list(
        module_0.get_input_output_paths(
            str(source_file),
            str(output_dir),
            str(source_root),
        )
    ) == [
        InputOutput(source_file, output_dir / "package" / "example.py")
    ]

    # Directory input recursively discovers Python files.
    nested_dir = package_dir / "nested"
    nested_dir.mkdir()
    nested_file = nested_dir / "child.py"
    nested_file.write_text("pass\n")

    # Non-Python files are ignored.
    (package_dir / "README.txt").write_text("ignored\n")

    results = list(
        module_0.get_input_output_paths(str(package_dir), str(output_dir), None)
    )

    assert sorted(results, key=lambda item: str(item[0])) == sorted(
        [
            InputOutput(source_file, output_dir / "example.py"),
            InputOutput(
                nested_file,
                output_dir / "nested" / "child.py",
            ),
        ],
        key=lambda item: str(item[0]),
    )

    # A non-Python input cannot target a .py output.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(package_dir),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # Input must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:41:42.980531
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(Path(str(input_file)), Path(str(output_file)))
    ]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "build"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(input_file)),
            Path(str(output_dir / "input.py")),
        )
    ]

    # A root preserves the input file's relative path.
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    nested_input = package_dir / "module.py"
    nested_input.write_text("VALUE = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(source_dir)
    )) == [
        InputOutput(
            Path(str(nested_input)),
            Path(str(output_dir / "package" / "module.py")),
        )
    ]

    # Directories are searched recursively, ignoring non-Python files.
    (package_dir / "README.txt").write_text("ignored")

    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(nested_input)),
            Path(str(output_dir / "package" / "module.py")),
        )
    ]

    # A directory/non-Python input cannot map to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))

# Generated at 2026-10-25 01:41:55.913745
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:42:08.784861
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:42:25.374006
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('hello')\n")

    nested = package / "nested"
    nested.mkdir()
    second_module = nested / "other.py"
    second_module.write_text("x = 1\n")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(Path(module), Path(output_file))
    ]

    # Python file to directory without a root preserves only the filename.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(Path(module), Path(output_dir / "module.py"))
    ]

    # Python file to directory with a root preserves its relative path.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(project))
    ) == [
        InputOutput(
            Path(module),
            Path(output_dir / "package" / "module.py"),
        )
    ]

    # Directory input discovers Python files recursively.
    results = list(
        module_0.get_input_output_paths(str(package), str(output_dir), None)
    )
    expected = [
        InputOutput(Path(module), Path(output_dir / "module.py")),
        InputOutput(
            Path(second_module),
            Path(output_dir / "nested" / "other.py"),
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(package),
                str(tmp_path / "single.py"),
                None,
            )
        )

    # The input must exist.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:42:37.209329
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .exceptions import InvalidInputOutput, InputDoesntExists
from .types import InputOutput
from .paths import get_input_output_paths  # Adjust to the actual module name


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "source"
    package = source_root / "package"
    package.mkdir(parents=True)

    source_file = package / "example.py"
    source_file.write_text("print('example')\n")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = output_dir / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(explicit_output), None
    )) == [
        InputOutput(source_file, explicit_output)
    ]

    # Python file to output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Python file to output directory relative to a specified root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(source_file, output_dir / "package" / "example.py")
    ]

    # Directory input recursively discovers Python files.
    assert list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "example.py")
    ]

    # Directory input with an explicit root preserves relative directories.
    assert list(module_0.get_input_output_paths(
        str(package), str(output_dir), str(source_root)
    )) == [
        InputOutput(source_file, output_dir / "package" / "example.py")
    ]

    # A directory/non-Python input cannot target a single .py file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(output_dir / "result.py"), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:42:49.130156
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can map directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped to a directory retains its filename.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # When root is provided, the relative input path is retained.
    root = tmp_path / "project"
    nested_input = root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively for Python files.
    source_dir = tmp_path / "src"
    child_input = source_dir / "subpackage" / "child.py"
    child_input.parent.mkdir(parents=True)
    child_input.write_text("value = 2")
    (source_dir / "ignored.txt").write_text("not Python")

    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(child_input, output_dir / "subpackage" / "child.py")
    ]

    # A directory/non-Python input cannot map to a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:42:58.755740
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Single Python file -> single Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(tmp_path / "output.py"),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, tmp_path / "output.py")
    ]

    # Single Python file -> output directory
    output_dir = tmp_path / "dist"
    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Directory input -> recursively preserve relative paths
    source_dir = tmp_path / "src"
    nested_file = source_dir / "package" / "module.py"
    ignored_file = source_dir / "package" / "README.md"

    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("x = 1")
    ignored_file.write_text("Not Python")

    result = list(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # A directory cannot be mapped to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(tmp_path / "combined.py"),
            root=None,
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            root=None,
        ))

# Generated at 2026-10-25 01:43:11.533293
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    package_dir = source_dir / "package"
    package_dir.mkdir()

    first_file = source_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = source_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not Python")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_file), None)
    ) == [
        InputOutput(first_file, output_file)
    ]

    # Without root, a Python file keeps only its filename.
    assert list(
        module_0.get_input_output_paths(str(first_file), str(output_dir), None)
    ) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # With root, the path relative to root is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(second_file),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(
            second_file,
            output_dir / "package" / "second.py",
        )
    ]

    # Directories are searched recursively, ignoring non-Python files.
    results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(
            second_file,
            output_dir / "package" / "second.py",
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

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
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:43:23.946457
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped to a directory retains its filename.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # When root is supplied, the path relative to root is retained.
    root = tmp_path / "project"
    nested_input = root / "src" / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "src" / "package" / "module.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    source_dir = tmp_path / "sources"
    child_input = source_dir / "package" / "child.py"
    child_input.parent.mkdir(parents=True)
    child_input.write_text("value = 2")
    (source_dir / "ignored.txt").write_text("not Python")

    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(child_input, output_dir / "package" / "child.py")
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input paths are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:43:39.818854
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = source_dir / "module.py"
    nested_module = package_dir / "nested.py"
    ignored_file = package_dir / "README.md"

    module.write_text("print('module')\n")
    nested_module.write_text("print('nested')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "generated.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # Without a root, a Python file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(nested_module),
            str(output_dir),
            str(source_dir),
        )
    ) == [
        InputOutput(nested_module, output_dir / "package" / "nested.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    actual = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    expected = [
        InputOutput(module, output_dir / "module.py"),
        InputOutput(nested_module, output_dir / "package" / "nested.py"),
    ]
    assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A directory cannot map to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(output_file),
                None,
            )
        )

    # Missing inputs are rejected.
    missing = tmp_path / "missing"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(missing), str(output_dir), None))

# Generated at 2026-10-25 01:43:49.956378
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = input_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # Directory input: recursively include only Python files.
    result = list(
        module_0.get_input_output_paths(
            str(input_dir),
            str(output_dir),
            root=None,
        )
    )

    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # Single Python file to a directory.
    result = list(
        module_0.get_input_output_paths(
            str(first_file),
            str(output_dir),
            root=None,
        )
    )
    assert result == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # Single Python file to a Python file.
    output_file = tmp_path / "generated.py"
    result = list(
        module_0.get_input_output_paths(
            str(first_file),
            str(output_file),
            root=None,
        )
    )
    assert result == [InputOutput(first_file, output_file)]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(input_dir),
                str(output_file),
                root=None,
            )
        )

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                root=None,
            )
        )

# Generated at 2026-10-25 01:43:52.601614
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:43:55.011703
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:43:57.427567
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:43:59.842706
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:02.257703
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:04.672782
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:07.090175
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:09.501817
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:11.916923
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:24.047523
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # Python file -> output directory
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(input_file, output_dir / "input.py"),
    ]

    # Directory input recursively maps Python files to the output directory.
    input_dir = tmp_path / "src"
    package_dir = input_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = package_dir / "README.txt"

    first_file.write_text("x = 1")
    second_file.write_text("x = 2")
    ignored_file.write_text("not Python")

    results = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert len(results) == 2
    assert InputOutput(first_file, output_dir / "first.py") in results
    assert InputOutput(
        second_file,
        output_dir / "package" / "second.py",
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(output_file),
            None,
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-25 01:44:41.464574
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:54.569391
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:44:57.088955
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:44:59.504211
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:01.922306
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:04.335783
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:06.751099
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:09.166850
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:11.582141
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:13.997844
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:16.412614
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:18.829609
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:21.243359
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:23.659788
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:26.074808
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:28.489917
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:30.904289
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:33.319009
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:45:45.464397
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:46:03.595984
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Adjust this import to match your package.
from your_package.exceptions import InvalidInputOutput, InputDoesntExists
from your_package.types import InputOutput
from your_package.paths import get_input_output_paths


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file -> output directory, without root.
    output_directory = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_directory),
        None,
    )) == [
        InputOutput(input_file, output_directory / "input.py")
    ]

    # Python file -> output directory, relative to root.
    root = tmp_path / "project"
    nested_input = root / "src" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input),
        str(output_directory),
        str(root),
    )) == [
        InputOutput(
            nested_input,
            output_directory / "src" / "module.py",
        )
    ]

    # Input directory -> recursively discovered Python files.
    source_directory = tmp_path / "sources"
    child_input = source_directory / "package" / "child.py"
    child_input.parent.mkdir(parents=True)
    child_input.write_text("value = 2")

    # Non-Python files must be ignored.
    (source_directory / "README.md").write_text("documentation")

    assert list(module_0.get_input_output_paths(
        str(source_directory),
        str(output_directory),
        None,
    )) == [
        InputOutput(
            child_input,
            output_directory / "package" / "child.py",
        )
    ]

    # A directory/non-Python input cannot map to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_directory),
            str(output_file),
            None,
        ))

    # Missing input raises InputDoesntExists.
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(output_directory),
            None,
        ))

# Generated at 2026-10-25 01:46:19.692454
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "input"
    nested_dir = input_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "ignored.txt"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("not Python")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = output_dir / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [InputOutput(first_file, output_file)]

    # A Python file mapped to a directory retains its filename.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [InputOutput(first_file, output_dir / "first.py")]

    # Supplying a root retains the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(input_dir)
    )) == [
        InputOutput(second_file, output_dir / "nested" / "second.py")
    ]

    # Directories are traversed recursively, ignoring non-Python files.
    results = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "nested" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_dir / "result.py"), None
        ))

    # The generator must be consumed for validation to execute.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:46:22.106499
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:24.533003
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:26.948336
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:29.363571
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:31.778563
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:34.193552
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:36.607794
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:39.025659
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:41.441994
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:43.856469
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:46.273653
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:48.690375
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:51.108831
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:53.534565
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:55.948459
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:46:58.365308
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:47:00.779147
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:47:03.193466
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:47:05.780965
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:47:15.046196
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-25 01:47:28.097198
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    input_file = source_dir / "example.py"
    input_file.write_text("print('hello')\n")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # A Python file can map directly to another Python file.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), root=None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped to a directory retains its filename.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), root=None
    )) == [
        InputOutput(input_file, output_dir / "example.py")
    ]

    # Root-relative paths are retained in the output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), root=str(tmp_path)
    )) == [
        InputOutput(input_file, output_dir / "src" / "example.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    nested_dir = source_dir / "nested"
    nested_dir.mkdir()
    nested_file = nested_dir / "module.py"
    nested_file.write_text("VALUE = 1\n")
    (nested_dir / "README.txt").write_text("ignored\n")

    assert set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), root=None
    )) == {
        InputOutput(input_file, output_dir / "example.py"),
        InputOutput(nested_file, output_dir / "nested" / "module.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), root=None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), root=None
        ))

# Generated at 2026-10-25 01:47:44.385705
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file.
    source_file = tmp_path / "source.py"
    source_file.write_text("print('hello')")

    target_file = tmp_path / "target.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(target_file), None
    )) == [InputOutput(source_file, target_file)]

    # Python file -> output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [InputOutput(source_file, output_dir / "source.py")]

    # Python file -> output directory, preserving the path relative to root.
    package_dir = tmp_path / "package"
    package_dir.mkdir()
    nested_file = package_dir / "module.py"
    nested_file.write_text("VALUE = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Input directory -> recursively discovered Python files.
    input_dir = tmp_path / "src"
    input_dir.mkdir()
    subdirectory = input_dir / "sub"
    subdirectory.mkdir()

    first_file = input_dir / "first.py"
    second_file = subdirectory / "second.py"
    ignored_file = subdirectory / "ignored.txt"

    first_file.write_text("")
    second_file.write_text("")
    ignored_file.write_text("not Python")

    results = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "sub" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(target_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-25 01:48:01.974945
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    package = project / "package"
    nested = package / "nested"
    nested.mkdir(parents=True)

    module = package / "module.py"
    child_module = nested / "child.py"
    ignored_file = package / "README.txt"

    module.write_text("print('module')\n")
    child_module.write_text("print('child')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # With no root, a single file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # With a root, the file's path relative to that root is preserved.
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
        InputOutput(child_module, output_dir / "nested" / "child.py"),
    ]

    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # An explicit root preserves the input directory itself in output paths.
    actual = list(
        module_0.get_input_output_paths(str(package), str(output_dir), str(project))
    )
    expected = [
        InputOutput(module, output_dir / "package" / "module.py"),
        InputOutput(
            child_module,
            output_dir / "package" / "nested" / "child.py",
        ),
    ]

    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(package),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # Generator execution must be forced with list() to trigger exceptions.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-25 01:48:04.513078
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:48:06.925047
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:48:14.764203
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-25 01:48:32.508169
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        tmp_path = Path(temp_dir)

        source_dir = tmp_path / "src"
        package_dir = source_dir / "package"
        package_dir.mkdir(parents=True)

        module = package_dir / "module.py"
        module.write_text("print('hello')")

        top_level_module = source_dir / "main.py"
        top_level_module.write_text("print('main')")

        # Non-Python files should be ignored when scanning directories.
        (package_dir / "README.txt").write_text("documentation")

        output_dir = tmp_path / "dist"

        # Python file to Python file.
        explicit_output = tmp_path / "generated.py"
        assert list(module_0.get_input_output_paths(
            str(module), str(explicit_output), None
        )) == [
            InputOutput(module, explicit_output)
        ]

        # Python file to output directory without an explicit root.
        assert list(module_0.get_input_output_paths(
            str(module), str(output_dir), None
        )) == [
            InputOutput(module, output_dir / "module.py")
        ]

        # Python file to output directory while preserving the root-relative path.
        assert list(module_0.get_input_output_paths(
            str(module), str(output_dir), str(source_dir)
        )) == [
            InputOutput(module, output_dir / "package" / "module.py")
        ]

        # Recursively process a directory and include only Python files.
        results = list(module_0.get_input_output_paths(
            str(source_dir), str(output_dir), None
        ))

        assert len(results) == 2
        assert InputOutput(
            top_level_module,
            output_dir / "main.py",
        ) in results
        assert InputOutput(
            module,
            output_dir / "package" / "module.py",
        ) in results

        # A directory cannot be mapped to a single Python file.
        # list() is required because this is a generator function.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(source_dir), str(tmp_path / "output.py"), None
            ))

        # Missing inputs should be rejected.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(tmp_path / "missing.py"), str(output_dir), None
            ))

# Generated at 2026-10-25 01:48:46.628815
# Unit test for function get_input_output_paths

# Generated at 2026-10-25 01:48:57.404870
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile