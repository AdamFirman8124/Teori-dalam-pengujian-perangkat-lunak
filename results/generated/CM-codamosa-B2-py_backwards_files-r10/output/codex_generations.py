

# Generated at 2026-10-24 03:57:33.368997
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    package_dir = source_dir / "package"
    package_dir.mkdir()

    input_file = package_dir / "module.py"
    input_file.write_text("print('hello')")

    ignored_file = package_dir / "README.txt"
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "module.py")
    ]

    # A root directory preserves the relative path.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "package" / "module.py")
    ]

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

# Generated at 2026-10-24 03:57:44.367425
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    package_dir = source_dir / "package"
    package_dir.mkdir()

    python_file = package_dir / "module.py"
    python_file.write_text("print('hello')")

    other_file = package_dir / "README.txt"
    other_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(python_file), str(output_file), None
    )) == [
        InputOutput(Path(python_file), Path(output_file))
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(python_file), str(output_dir), None
    )) == [
        InputOutput(Path(python_file), output_dir / "module.py")
    ]

    # Preserve the path relative to the explicitly supplied root.
    assert list(module_0.get_input_output_paths(
        str(python_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(
            Path(python_file),
            output_dir / "package" / "module.py",
        )
    ]

    # Recursively process only Python files from an input directory.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(
            Path(python_file),
            output_dir / "package" / "module.py",
        )
    ]

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 03:58:03.489095
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_input = source_dir / "first.py"
    second_input = nested_dir / "second.py"
    ignored_input = source_dir / "README.txt"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # Python file to Python file.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # Python file to output directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # Python file to output directory while preserving its relative path.
    assert list(module_0.get_input_output_paths(
        str(second_input), str(output_dir), str(source_dir)
    )) == [
        InputOutput(second_input, output_dir / "nested" / "second.py")
    ]

    # Directory input includes Python files recursively and ignores other files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "nested" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 03:58:14.675242
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
    ignored_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [
        InputOutput(first_file, output_file)
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # A Python file mapped relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # A directory recursively maps only Python files.
    actual = set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    assert actual == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 03:58:27.569217
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Arrange a directory containing Python and non-Python files.
    source = tmp_path / "source"
    nested = source / "nested"
    nested.mkdir(parents=True)

    first_file = source / "first.py"
    second_file = nested / "second.py"
    ignored_file = nested / "notes.txt"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("ignored")

    output = tmp_path / "output"

    # A directory input recursively produces pairs only for Python files.
    result = list(module_0.get_input_output_paths(
        str(source),
        str(output),
        root=None,
    ))

    expected = [
        InputOutput(first_file, output / "first.py"),
        InputOutput(second_file, output / "nested" / "second.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A Python file and Python output are paired directly.
    explicit_output = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(first_file),
        str(explicit_output),
        root=None,
    )) == [InputOutput(first_file, explicit_output)]

    # A Python file with a directory output keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(first_file),
        str(output),
        root=None,
    )) == [InputOutput(first_file, output / "first.py")]

    # A directory input cannot target a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source),
            str(explicit_output),
            root=None,
        ))

    # A missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output),
            root=None,
        ))

# Generated at 2026-10-24 03:58:39.969753
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "input"
    nested_dir = input_dir / "nested"
    output_dir = tmp_path / "output"

    nested_dir.mkdir(parents=True)
    first_file = input_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = input_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("Ignored")

    # Directory input preserves the directory structure.
    result = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), root=None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "nested" / "second.py"),
    ]

    assert len(result) == len(expected)
    assert all(item in result for item in expected)

    # A Python file can map directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(direct_output), root=None
    )) == [InputOutput(first_file, direct_output)]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), root=None
    )) == [InputOutput(first_file, output_dir / "first.py")]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(direct_output), root=None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), root=None
        ))

# Generated at 2026-10-24 03:59:04.650080
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_dir / "README.md"

    main_file.write_text("print('main')")
    nested_file.write_text("print('module')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(Path(str(main_file)), Path(str(output_file)))
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(main_file)),
            Path(str(output_dir / "main.py")),
        )
    ]

    # A Python file with a root preserves its relative path.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(
            Path(str(nested_file)),
            Path(str(output_dir / "nested" / "module.py")),
        )
    ]

    # A directory recursively maps only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(
            Path(str(main_file)),
            Path(str(output_dir / "main.py")),
        ),
        InputOutput(
            Path(str(nested_file)),
            Path(str(output_dir / "nested" / "module.py")),
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

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

# Generated at 2026-10-24 03:59:18.268541
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        source_root = base / "src"
        package = source_root / "package"
        package.mkdir(parents=True)

        module = package / "module.py"
        module.write_text("print('hello')\n")

        nested = package / "nested"
        nested.mkdir()
        nested_module = nested / "other.py"
        nested_module.write_text("print('other')\n")

        # Non-Python files should be ignored when processing a directory.
        (package / "README.md").write_text("documentation")

        output_dir = base / "output"

        # A Python file can be mapped directly to another Python file.
        output_file = base / "generated.py"
        assert list(module_0.get_input_output_paths(
            str(module), str(output_file), None
        )) == [
            InputOutput(module, output_file)
        ]

        # Without a root, a Python file keeps its basename.
        assert list(module_0.get_input_output_paths(
            str(module), str(output_dir), None
        )) == [
            InputOutput(module, output_dir / "module.py")
        ]

        # With a root, the file's path relative to that root is preserved.
        assert list(module_0.get_input_output_paths(
            str(module), str(output_dir), str(source_root)
        )) == [
            InputOutput(module, output_dir / "package" / "module.py")
        ]

        # Directory input recursively includes only Python files.
        actual = set(module_0.get_input_output_paths(
            str(package), str(output_dir), None
        ))
        expected = {
            InputOutput(module, output_dir / "module.py"),
            InputOutput(
                nested_module,
                output_dir / "nested" / "other.py",
            ),
        }
        assert actual == expected

        # A directory cannot be mapped to a single Python file.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(package), str(output_file), None
            ))

        # Missing inputs raise InputDoesntExists.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(base / "missing.py"), str(output_dir), None
            ))

# Generated at 2026-10-24 03:59:20.773187
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 03:59:23.274872
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 03:59:38.959229
# Unit test for function get_input_output_paths
def test_get_input_output_paths():from pathlib import Path

# Generated at 2026-10-24 03:59:59.372577
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source = tmp_path / "src"
    package = source / "package"
    package.mkdir(parents=True)

    top_level_file = source / "main.py"
    nested_file = package / "module.py"
    ignored_file = package / "README.txt"

    top_level_file.write_text("print('main')")
    nested_file.write_text("print('module')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A directory input cannot be written to a single .py file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source),
            str(tmp_path / "output.py"),
            None,
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

    # A single Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(top_level_file),
        str(direct_output),
        None,
    )) == [
        InputOutput(top_level_file, direct_output),
    ]

    # Without a root, a single file is placed directly in the output folder.
    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(nested_file, output_dir / "module.py"),
    ]

    # With a root, the input file's relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        str(source),
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    # Directory inputs recursively include only Python files.
    results = list(module_0.get_input_output_paths(
        str(source),
        str(output_dir),
        None,
    ))

    expected = [
        InputOutput(top_level_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

# Generated at 2026-10-24 04:00:19.714668
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path):
    project = tmp_path / "project"
    source = project / "src"
    package = source / "package"
    package.mkdir(parents=True)

    main_file = source / "main.py"
    helper_file = package / "helper.py"
    ignored_file = source / "README.md"

    main_file.write_text("print('main')\n")
    helper_file.write_text("print('helper')\n")
    ignored_file.write_text("Not a Python file\n")

    def assert_pairs(actual, expected):
        # Path.glob() ordering is not guaranteed.
        assert sorted(actual, key=repr) == sorted(expected, key=repr)

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(str(main_file), str(output_file), None)) == [
        InputOutput(main_file, output_file)
    ]

    # Without a root, the original filename is appended to the output dir.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(str(main_file), str(output_dir), None)) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # With a root, the file's path relative to that root is preserved.
    assert list(
        module_0.get_input_output_paths(
            str(main_file),
            str(output_dir),
            str(project),
        )
    ) == [
        InputOutput(main_file, output_dir / "src" / "main.py")
    ]

    # Directory input recursively includes only Python files.
    assert_pairs(
        list(module_0.get_input_output_paths(str(source), str(output_dir), None)),
        [
            InputOutput(main_file, output_dir / "main.py"),
            InputOutput(helper_file, output_dir / "package" / "helper.py"),
        ],
    )

    # A supplied root is also respected for directory input.
    assert_pairs(
        list(
            module_0.get_input_output_paths(
                str(source),
                str(output_dir),
                str(project),
            )
        ),
        [
            InputOutput(main_file, output_dir / "src" / "main.py"),
            InputOutput(
                helper_file,
                output_dir / "src" / "package" / "helper.py",
            ),
        ],
    )

    # A non-file input cannot be mapped to a single .py output.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source),
                str(tmp_path / "output.py"),
                None,
            )
        )

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 04:00:35.887660
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    module = source_dir / "module.py"
    module.write_text("print('hello')\n")

    nested_dir = source_dir / "package"
    nested_dir.mkdir()

    nested_module = nested_dir / "nested.py"
    nested_module.write_text("x = 1\n")

    ignored_file = source_dir / "README.md"
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(module), str(explicit_output), None
    )) == [
        InputOutput(module, explicit_output)
    ]

    # Python file to output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), None
    )) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to output directory relative to a supplied root.
    assert list(module_0.get_input_output_paths(
        str(nested_module), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_module, output_dir / "package" / "nested.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(module, output_dir / "module.py"),
        InputOutput(nested_module, output_dir / "package" / "nested.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory/non-Python input cannot target a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "result.py"), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:00:50.023886
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A non-Python input cannot produce a single Python output file.
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            None,
        ))

    # Input must exist. Calling list() evaluates the generator.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            None,
        ))

    # Python file -> Python file.
    input_file = input_dir / "module.py"
    input_file.write_text("print('hello')\n")

    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # Python file -> output directory, without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(input_file, output_dir / "module.py"),
    ]

    # Python file -> output directory, preserving its path relative to root.
    package_dir = input_dir / "package"
    package_dir.mkdir()
    nested_file = package_dir / "nested.py"
    nested_file.write_text("value = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        str(input_dir),
    )) == [
        InputOutput(nested_file, output_dir / "package" / "nested.py"),
    ]

    # Directory input recursively includes only Python files.
    text_file = package_dir / "ignored.txt"
    text_file.write_text("not Python\n")

    results = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert sorted(results, key=lambda pair: str(pair[0])) == sorted(
        [
            InputOutput(input_file, output_dir / "module.py"),
            InputOutput(
                nested_file,
                output_dir / "package" / "nested.py",
            ),
        ],
        key=lambda pair: str(pair[0]),
    )

# Generated at 2026-10-24 04:01:10.596818
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    helper_file = package_dir / "helper.py"
    ignored_file = source_dir / "README.md"

    main_file.write_text("print('main')")
    helper_file.write_text("print('helper')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(explicit_output), None
    )) == [
        InputOutput(main_file, explicit_output)
    ]

    # Python file to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Python file to an output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(helper_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(helper_file, output_dir / "package" / "helper.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(helper_file, output_dir / "package" / "helper.py"),
    ]

    assert len(actual) == len(expected)
    assert all(item in actual for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "result.py"), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:01:28.828460
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path):
    source_root = tmp_path / "src"
    source_root.mkdir()

    input_file = source_root / "example.py"
    input_file.write_text("print('hello')")

    # Python file to Python file.
    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file to output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "example.py")
    ]

    # Python file to output directory relative to an explicit root.
    nested_dir = source_root / "package"
    nested_dir.mkdir()
    nested_file = nested_dir / "module.py"
    nested_file.write_text("x = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    second_file = nested_dir / "second.py"
    second_file.write_text("y = 2")
    ignored_file = nested_dir / "README.txt"
    ignored_file.write_text("ignored")

    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))

    expected = [
        InputOutput(input_file, output_dir / "example.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory/non-Python input cannot target a Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # A missing input raises InputDoesntExists.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-24 04:01:42.861567
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "nested"
    output_dir = tmp_path / "output"

    nested_dir.mkdir(parents=True)

    input_file = input_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = input_dir / "README.md"

    input_file.write_text("print('main')\n")
    nested_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Without a root, a file keeps its name inside the output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "main.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(input_dir)
    )) == [
        InputOutput(nested_file, output_dir / "nested" / "module.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    results = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(input_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "nested" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:02:01.675589
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    input_dir = root / "src"
    package_dir = input_dir / "package"
    package_dir.mkdir(parents=True)

    input_file = package_dir / "module.py"
    input_file.write_text("print('hello')\n")

    # Non-Python files should be ignored when processing a directory.
    (package_dir / "README.txt").write_text("Not Python")

    output_dir = tmp_path / "output"
    output_file = tmp_path / "result.py"

    # Python file to Python file.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(Path(str(input_file)), Path(str(output_file)))
    ]

    # Python file to directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(input_file)),
            Path(str(output_dir / "module.py")),
        )
    ]

    # Python file to directory while preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(root)
    )) == [
        InputOutput(
            Path(str(input_file)),
            Path(str(output_dir / "src" / "package" / "module.py")),
        )
    ]

    # Directory input recursively discovers Python files.
    assert list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    )) == [
        InputOutput(
            Path(str(input_file)),
            Path(str(output_dir / "package" / "module.py")),
        )
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:02:16.854508
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    nested_file = package_dir / "module.py"
    ignored_file = package_dir / "README.md"

    main_file.write_text("print('main')\n")
    nested_file.write_text("print('module')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "build"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(main_file), str(output_file), None)) == [
        InputOutput(main_file, output_file)
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(str(main_file), str(output_dir), None)) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # A root directory preserves the path relative to that root.
    assert list(
        module_0.get_input_output_paths(str(nested_file), str(output_dir), str(source_dir))
    ) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # A directory is searched recursively, ignoring non-Python files.
    results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    assert set(results) == {
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "output.py"),
                None,
            )
        )

    # Missing input paths are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 04:02:29.248364
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = package_dir / "module.py"
    module.write_text("print('hello')")

    nested_module = package_dir / "nested.py"
    nested_module.write_text("print('nested')")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # Python file to output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to output directory relative to an explicit root.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(source_dir))
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes all Python files.
    results = list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    )
    assert set(results) == {
        InputOutput(module, output_dir / "package" / "module.py"),
        InputOutput(nested_module, output_dir / "package" / "nested.py"),
    }

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "single.py"),
                None,
            )
        )

    # Missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 04:02:42.765094
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = package_dir / "module.py"
    module.write_text("print('hello')\n")

    ignored_file = package_dir / "README.md"
    ignored_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(module, output_file)
    ]

    # Python file to directory without an explicit root.
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(module, output_dir / "module.py")
    ]

    # Python file to directory while preserving its path relative to root.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(source_dir))
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    assert list(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None)
    ) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(output_file),
            None,
        ))

    # Generator exceptions are raised when it is consumed.
    missing_input = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(output_dir),
            None,
        ))

# Generated at 2026-10-24 04:02:56.393382
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package_dir = source_root / "package"
    package_dir.mkdir(parents=True)

    first_input = package_dir / "first.py"
    second_input = package_dir / "second.py"
    ignored_input = package_dir / "README.md"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("ignored")

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(explicit_output), None
    )) == [
        InputOutput(first_input, explicit_output)
    ]

    # Python file to output directory.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # Preserve the path relative to the configured root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(first_input, output_dir / "package" / "first.py")
    ]

    # Recursively process only Python files from an input directory.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(first_input, output_dir / "package" / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(explicit_output), None
        ))

    # A missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:03:08.976665
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 04:03:21.383100
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-24 04:03:42.360217
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        source_root = base / "src"
        package_dir = source_root / "package"
        package_dir.mkdir(parents=True)

        first_input = source_root / "first.py"
        second_input = package_dir / "second.py"
        ignored_input = package_dir / "README.txt"

        first_input.write_text("print('first')")
        second_input.write_text("print('second')")
        ignored_input.write_text("not Python")

        # Python file to Python file.
        output_file = base / "result.py"
        assert list(module_0.get_input_output_paths(
            str(first_input), str(output_file), None
        )) == [
            InputOutput(first_input, output_file)
        ]

        # Python file to output directory without an explicit root.
        output_dir = base / "output"
        assert list(module_0.get_input_output_paths(
            str(first_input), str(output_dir), None
        )) == [
            InputOutput(first_input, output_dir / "first.py")
        ]

        # Python file to output directory, preserving its path from root.
        assert list(module_0.get_input_output_paths(
            str(second_input), str(output_dir), str(source_root)
        )) == [
            InputOutput(second_input, output_dir / "package" / "second.py")
        ]

        # Directory input recursively includes only Python files.
        results = list(module_0.get_input_output_paths(
            str(source_root), str(output_dir), None
        ))
        expected = [
            InputOutput(first_input, output_dir / "first.py"),
            InputOutput(second_input, output_dir / "package" / "second.py"),
        ]

        assert len(results) == len(expected)
        for item in expected:
            assert item in results

        # A directory/non-Python input cannot map to a single Python file.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(source_root), str(output_file), None
            ))

        # Missing inputs are rejected.
        missing_input = source_root / "missing.py"
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(missing_input), str(output_dir), None
            ))

# Generated at 2026-10-24 04:03:54.566575
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
    ignored_file.write_text("not Python\n")

    output_dir = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(direct_output), None
    )) == [
        InputOutput(main_file, direct_output)
    ]

    # A Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Root preserves the input file's relative path.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(module_file, output_dir / "package" / "module.py")
    ]

    # A directory recursively includes only Python files.
    actual = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(module_file, output_dir / "package" / "module.py"),
    ]
    assert sorted(actual, key=lambda item: str(item[0])) == sorted(
        expected, key=lambda item: str(item[0])
    )

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(direct_output), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:04:07.447079
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped into an output directory.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Preserve the path relative to an explicit root.
    source_dir = tmp_path / "project" / "src"
    source_dir.mkdir(parents=True)
    nested_input = source_dir / "package" / "module.py"
    nested_input.parent.mkdir()
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(tmp_path / "project")
    )) == [
        InputOutput(
            nested_input,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # Recursively process Python files in an input directory.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(
            nested_input,
            output_dir / "package" / "module.py",
        )
    ]

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

# Generated at 2026-10-24 04:04:20.556713
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    module = source_dir / "module.py"
    nested_module = package_dir / "nested.py"
    ignored_file = source_dir / "README.md"

    module.write_text("print('module')")
    nested_module.write_text("print('nested')")
    ignored_file.write_text("Not a Python file")

    # A Python file mapped directly to another Python file.
    result = list(module_0.get_input_output_paths(
        str(module),
        str(tmp_path / "result.py"),
        None,
    ))
    assert result == [
        InputOutput(Path(str(module)), Path(str(tmp_path / "result.py")))
    ]

    # A Python file mapped into an output directory.
    result = list(module_0.get_input_output_paths(
        str(module),
        str(tmp_path / "output"),
        None,
    ))
    assert result == [
        InputOutput(
            Path(str(module)),
            Path(str(tmp_path / "output" / "module.py")),
        )
    ]

    # A directory is searched recursively, ignoring non-Python files.
    result = list(module_0.get_input_output_paths(
        str(source_dir),
        str(tmp_path / "output"),
        None,
    ))
    expected = [
        InputOutput(
            Path(str(module)),
            Path(str(tmp_path / "output" / "module.py")),
        ),
        InputOutput(
            Path(str(nested_module)),
            Path(str(tmp_path / "output" / "package" / "nested.py")),
        ),
    ]
    assert sorted(result, key=repr) == sorted(expected, key=repr)

    # The supplied root controls the relative output path.
    result = list(module_0.get_input_output_paths(
        str(nested_module),
        str(tmp_path / "output"),
        str(source_dir),
    ))
    assert result == [
        InputOutput(
            Path(str(nested_module)),
            Path(str(tmp_path / "output" / "package" / "nested.py")),
        )
    ]

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
            str(tmp_path / "result.py"),
            None,
        ))

    # Missing input paths are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(tmp_path / "output"),
            None,
        ))

# Generated at 2026-10-24 04:04:38.678852
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Python file -> Python file
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")

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
    source_root = tmp_path / "src"
    nested_input = source_root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Input directory -> recursively discovered Python files
    project_dir = tmp_path / "project"
    first_file = project_dir / "first.py"
    second_file = project_dir / "nested" / "second.py"
    ignored_file = project_dir / "nested" / "README.txt"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("first = True\n")
    second_file.write_text("second = True\n")
    ignored_file.write_text("Not a Python file\n")

    results = list(module_0.get_input_output_paths(
        str(project_dir), str(output_dir), None
    ))

    assert set(results) == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "nested" / "second.py"),
    }

    # A directory cannot be written to a single .py output
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(project_dir), str(output_file), None
        ))

    # Missing input raises InputDoesntExists
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:04:52.632281
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped into an output directory.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Root preserves the input file's relative path.
    source_root = tmp_path / "src"
    nested_input = source_root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Directories are searched recursively and non-Python files are ignored.
    another_input = source_root / "main.py"
    another_input.write_text("print('main')")
    ignored_file = source_root / "README.md"
    ignored_file.write_text("Not Python")

    result = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))

    assert set(result) == {
        InputOutput(another_input, output_dir / "main.py"),
        InputOutput(
            nested_input,
            output_dir / "package" / "module.py",
        ),
    }

    # A directory/non-Python input cannot map to a single Python output.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:05:06.983008
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    output_dir = tmp_path / "output"

    # Missing input.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"),
            str(output_dir),
            None,
        ))

    # A directory cannot be written to a single Python file.
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            None,
        ))

    # Python file to Python file.
    input_file = input_dir / "module.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [
        InputOutput(input_file, output_file),
    ]

    # Python file to output directory.
    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(input_file, output_dir / "module.py"),
    ]

    # Preserve the path relative to a provided root.
    project_root = tmp_path / "project"
    nested_dir = project_root / "src" / "package"
    nested_dir.mkdir(parents=True)
    nested_file = nested_dir / "nested.py"
    nested_file.write_text("x = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_file),
        str(output_dir),
        str(project_root),
    )) == [
        InputOutput(
            nested_file,
            output_dir / "src" / "package" / "nested.py",
        ),
    ]

    # Recursively process only Python files from an input directory.
    second_file = input_dir / "package" / "second.py"
    second_file.parent.mkdir()
    second_file.write_text("y = 2")
    (input_dir / "ignored.txt").write_text("not Python")

    results = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert sorted(results, key=lambda item: str(item[0])) == sorted(
        [
            InputOutput(input_file, output_dir / "module.py"),
            InputOutput(
                second_file,
                output_dir / "package" / "second.py",
            ),
        ],
        key=lambda item: str(item[0]),
    )

# Generated at 2026-10-24 04:05:20.560649
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    nested_dir = package_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_input = package_dir / "first.py"
    second_input = nested_dir / "second.py"
    ignored_input = package_dir / "README.md"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    direct_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(direct_output), None
    )) == [
        InputOutput(first_input, direct_output)
    ]

    # Without a root, only the input filename is appended.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(second_input), str(output_dir), str(source_dir)
    )) == [
        InputOutput(
            second_input,
            output_dir / "package" / "nested" / "second.py",
        )
    ]

    # Directory input recursively includes only Python files.
    actual = set(module_0.get_input_output_paths(
        str(package_dir), str(output_dir), None
    ))
    expected = {
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "nested" / "second.py"),
    }
    assert actual == expected

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package_dir), str(tmp_path / "result.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:05:36.945173
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    input_dir = root / "src"
    nested_dir = input_dir / "nested"
    nested_dir.mkdir(parents=True)

    main_file = input_dir / "main.py"
    helper_file = nested_dir / "helper.py"
    ignored_file = input_dir / "README.txt"

    main_file.write_text("print('main')")
    helper_file.write_text("print('helper')")
    ignored_file.write_text("Not Python")

    # A non-Python input cannot target a Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(ignored_file),
            str(tmp_path / "result.py"),
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
    output_file = tmp_path / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(main_file),
        str(output_file),
        None,
    )) == [
        InputOutput(main_file, output_file),
    ]

    # Python file to output directory without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(main_file),
        str(output_dir),
        None,
    )) == [
        InputOutput(main_file, output_dir / "main.py"),
    ]

    # Python file to output directory relative to an explicit root.
    assert list(module_0.get_input_output_paths(
        str(main_file),
        str(output_dir),
        str(root),
    )) == [
        InputOutput(main_file, output_dir / "src" / "main.py"),
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert len(results) == 2
    assert InputOutput(main_file, output_dir / "main.py") in results
    assert InputOutput(
        helper_file,
        output_dir / "nested" / "helper.py",
    ) in results

    # An explicit root preserves the input directory's relative path.
    results = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        str(root),
    ))

    assert len(results) == 2
    assert InputOutput(
        main_file,
        output_dir / "src" / "main.py",
    ) in results
    assert InputOutput(
        helper_file,
        output_dir / "src" / "nested" / "helper.py",
    ) in results

# Generated at 2026-10-24 04:05:59.089683
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.paths import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def sorted_pairs(pairs):
    """Sort results without depending on pathlib glob ordering."""
    return sorted(pairs, key=repr)


def test_get_input_output_paths_for_python_file(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('hello')")

    result = list(
        module_0.get_input_output_paths(
            str(input_path),
            str(output_path),
            root=None,
        )
    )

    assert result == [InputOutput(input_path, output_path)]


def test_get_input_output_paths_for_file_and_output_directory(tmp_path):
    input_path = tmp_path / "source" / "input.py"
    output_dir = tmp_path / "output"

    input_path.parent.mkdir()
    input_path.write_text("print('hello')")

    result = list(
        module_0.get_input_output_paths(
            str(input_path),
            str(output_dir),
            root=None,
        )
    )

    assert result == [
        InputOutput(input_path, output_dir / "input.py"),
    ]


def test_get_input_output_paths_for_file_with_root(tmp_path):
    root = tmp_path / "source"
    input_path = root / "package" / "input.py"
    output_dir = tmp_path / "output"

    input_path.parent.mkdir(parents=True)
    input_path.write_text("print('hello')")

    result = list(
        module_0.get_input_output_paths(
            str(input_path),
            str(output_dir),
            root=str(root),
        )
    )

    assert result == [
        InputOutput(input_path, output_dir / "package" / "input.py"),
    ]


def test_get_input_output_paths_for_directory(tmp_path):
    input_dir = tmp_path / "source"
    output_dir = tmp_path / "output"

    first_input = input_dir / "first.py"
    second_input = input_dir / "package" / "second.py"
    ignored_input = input_dir / "package" / "README.txt"

    second_input.parent.mkdir(parents=True)
    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("Not a Python file")

    result = list(
        module_0.get_input_output_paths(
            str(input_dir),
            str(output_dir),
            root=None,
        )
    )

    expected = [
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    assert sorted_pairs(result) == sorted_pairs(expected)


def test_get_input_output_paths_rejects_directory_to_python_file(tmp_path):
    input_dir = tmp_path / "source"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        # The function is a generator, so it must be consumed to raise.
        list(
            module_0.get_input_output_paths(
                str(input_dir),
                str(tmp_path / "output.py"),
                root=None,
            )
        )


def test_get_input_output_paths_rejects_missing_input(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        # The function is a generator, so it must be consumed to raise.
        list(
            module_0.get_input_output_paths(
                str(missing_input),
                str(tmp_path / "output.py"),
                root=None,
            )
        )

# Generated at 2026-10-24 04:06:15.959530
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    nested = package / "nested"
    nested.mkdir(parents=True)

    first_file = package / "first.py"
    second_file = nested / "second.py"
    ignored_file = package / "README.md"

    first_file.write_text("print('first')\n")
    second_file.write_text("print('second')\n")
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [
        InputOutput(first_file, output_file)
    ]

    # Without a root, a file is placed directly in the output directory.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # With a root, the relative directory structure is preserved.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(first_file, output_dir / "package" / "first.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    results = list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    ))

    assert len(results) == 2
    assert InputOutput(first_file, output_dir / "first.py") in results
    assert InputOutput(
        second_file, output_dir / "nested" / "second.py"
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(output_file), None
        ))

    # Generator execution is forced with list() so the exception is raised.
    missing_input = tmp_path / "missing"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input), str(output_dir), None
        ))

# Generated at 2026-10-24 04:06:29.375430
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "source.py"
    input_file.write_text("print('hello')\n")

    output_file = tmp_path / "result.py"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [InputOutput(input_file, output_file)]

    # When output is a directory, preserve the input filename.
    output_dir = tmp_path / "output"

    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [InputOutput(input_file, output_dir / "source.py")]

    # Preserve paths relative to an explicitly supplied root.
    nested_input = tmp_path / "src" / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(tmp_path / "src")
    )) == [
        InputOutput(
            nested_input,
            output_dir / "package" / "module.py",
        )
    ]

    # Recursively map Python files from an input directory.
    source_dir = tmp_path / "project"
    first_file = source_dir / "first.py"
    second_file = source_dir / "subpackage" / "second.py"
    ignored_file = source_dir / "README.md"

    second_file.parent.mkdir(parents=True)
    first_file.write_text("FIRST = 1\n")
    second_file.write_text("SECOND = 2\n")
    ignored_file.write_text("Not a Python file\n")

    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    assert sorted(results, key=lambda pair: str(pair[0])) == sorted(
        [
            InputOutput(first_file, output_dir / "first.py"),
            InputOutput(
                second_file,
                output_dir / "subpackage" / "second.py",
            ),
        ],
        key=lambda pair: str(pair[0]),
    )

    # A directory/non-Python input cannot target a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:06:43.334038
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from your_package.exceptions import InvalidInputOutput, InputDoesntExists
from your_package.types import InputOutput
from your_package.paths import get_input_output_paths  # Adjust module path


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = nested_dir / "second.py"
    ignored_file = nested_dir / "README.md"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("ignored")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_file), None
    )) == [InputOutput(first_file, output_file)]

    # Python file to output directory without a root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [InputOutput(first_file, output_dir / "first.py")]

    # Python file to output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(second_file, output_dir / "package" / "second.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(second_file, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory input cannot map to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 04:07:03.324412
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile

    import pytest

    with tempfile.TemporaryDirectory() as temporary_directory:
        base = Path(temporary_directory)
        project = base / 'project'
        package = project / 'package'
        nested = package / 'nested'
        nested.mkdir(parents=True)

        first_input = package / 'first.py'
        second_input = nested / 'second.py'
        ignored_input = nested / 'README.txt'

        first_input.write_text('print("first")')
        second_input.write_text('print("second")')
        ignored_input.write_text('not Python')

        # Python file to Python file.
        output_file = base / 'result.py'
        assert list(module_0.get_input_output_paths(
            str(first_input), str(output_file), None
        )) == [InputOutput(first_input, output_file)]

        # Python file to an output directory.
        output_directory = base / 'output'
        assert list(module_0.get_input_output_paths(
            str(first_input), str(output_directory), None
        )) == [
            InputOutput(first_input, output_directory / 'first.py')
        ]

        # Python file to an output directory relative to a root.
        assert list(module_0.get_input_output_paths(
            str(first_input), str(output_directory), str(project)
        )) == [
            InputOutput(
                first_input,
                output_directory / 'package' / 'first.py',
            )
        ]

        # Directory input recursively includes only Python files.
        results = list(module_0.get_input_output_paths(
            str(package), str(output_directory), None
        ))
        expected = [
            InputOutput(first_input, output_directory / 'first.py'),
            InputOutput(
                second_input,
                output_directory / 'nested' / 'second.py',
            ),
        ]

        assert len(results) == len(expected)
        for pair in expected:
            assert pair in results

        # A directory/non-Python input cannot map to one Python file.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(package), str(output_file), None
            ))

        # Missing inputs are rejected.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(base / 'missing.py'),
                str(output_directory),
                None,
            ))

# Generated at 2026-10-24 04:07:16.694964
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    output_dir = tmp_path / "output"

    package_dir.mkdir(parents=True)

    first_input = source_dir / "first.py"
    second_input = package_dir / "second.py"
    ignored_input = source_dir / "README.txt"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("not Python")

    # A single Python file mapped to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), root=None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # A single Python file mapped into an output directory.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), root=None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # Explicit root preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), root=str(tmp_path)
    )) == [
        InputOutput(first_input, output_dir / "src" / "first.py")
    ]

    # A directory is searched recursively, ignoring non-Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), root=None
    ))
    expected = [
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), root=None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), root=None
        ))

# Generated at 2026-10-24 04:07:30.836371
# Unit test for function get_input_output_paths
def test_get_input_output_paths():from pathlib import Path

import pytest

# Replace `your_package.module` with the module containing the function.
from your_package.module import get_input_output_paths
from your_package.exceptions import InvalidInputOutput, InputDoesntExists
from your_package.types import InputOutput


def test_get_input_output_paths(tmp_path: Path):
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    source_file = source_dir / "main.py"
    nested_file = nested_dir / "helper.py"
    ignored_file = nested_dir / "README.txt"

    source_file.write_text("print('main')\n")
    nested_file.write_text("print('helper')\n")
    ignored_file.write_text("not Python\n")

    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # With a directory output, the source filename is preserved.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # A root preserves the source path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(source_dir)
    )) == [
        InputOutput(nested_file, output_dir / "nested" / "helper.py")
    ]

    # Directories are searched recursively, ignoring non-Python files.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "nested" / "helper.py"),
    ]

    # A directory cannot be mapped to a single Python file.
    # list() is required because the function is a generator.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))