

# Generated at 2026-10-24 05:54:16.903109
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    source = project / "src"
    package = source / "package"
    package.mkdir(parents=True)

    main_file = source / "main.py"
    module_file = package / "module.py"
    ignored_file = package / "README.txt"

    main_file.write_text("print('main')\n")
    module_file.write_text("print('module')\n")
    ignored_file.write_text("Not Python\n")

    output = tmp_path / "output"

    # A Python file mapped directly to another Python file.
    target_file = output / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(target_file), None
    )) == [
        InputOutput(main_file, target_file)
    ]

    # A Python file mapped to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output), None
    )) == [
        InputOutput(module_file, output / "module.py")
    ]

    # A Python file mapped relative to a specified root.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output), str(project)
    )) == [
        InputOutput(module_file, output / "src" / "package" / "module.py")
    ]

    # A directory is searched recursively, ignoring non-Python files.
    results = list(module_0.get_input_output_paths(
        str(source), str(output), None
    ))

    assert len(results) == 2
    assert InputOutput(main_file, output / "main.py") in results
    assert InputOutput(
        module_file, output / "package" / "module.py"
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source), str(output / "single.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output), None
        ))

# Generated at 2026-10-24 05:54:40.450155
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # A non-Python input cannot map to a single Python file.
        input_directory = temp_path / "input"
        input_directory.mkdir()

        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(input_directory),
                str(temp_path / "output.py"),
                None,
            ))

        # The input must exist.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(temp_path / "missing.py"),
                str(temp_path / "output"),
                None,
            ))

        # A Python file can map directly to another Python file.
        input_file = temp_path / "input.py"
        input_file.write_text("print('test')\n", encoding="utf-8")
        output_file = temp_path / "output.py"

        assert list(module_0.get_input_output_paths(
            str(input_file),
            str(output_file),
            None,
        )) == [InputOutput(input_file, output_file)]

        # A Python file mapped to a directory keeps its file name.
        output_directory = temp_path / "output"

        assert list(module_0.get_input_output_paths(
            str(input_file),
            str(output_directory),
            None,
        )) == [
            InputOutput(input_file, output_directory / "input.py")
        ]

        # When root is provided, the path relative to root is preserved.
        project_root = temp_path / "project"
        nested_input = project_root / "src" / "package" / "module.py"
        nested_input.parent.mkdir(parents=True)
        nested_input.write_text("value = 1\n", encoding="utf-8")

        assert list(module_0.get_input_output_paths(
            str(nested_input),
            str(output_directory),
            str(project_root),
        )) == [
            InputOutput(
                nested_input,
                output_directory / "src" / "package" / "module.py",
            )
        ]

        # Directory inputs recursively include only Python files.
        source_directory = temp_path / "sources"
        first_file = source_directory / "first.py"
        second_file = source_directory / "nested" / "second.py"
        ignored_file = source_directory / "nested" / "README.txt"

        second_file.parent.mkdir(parents=True)
        first_file.write_text("first = 1\n", encoding="utf-8")
        second_file.write_text("second = 2\n", encoding="utf-8")
        ignored_file.write_text("ignored\n", encoding="utf-8")

        actual = list(module_0.get_input_output_paths(
            str(source_directory),
            str(output_directory),
            None,
        ))
        expected = [
            InputOutput(first_file, output_directory / "first.py"),
            InputOutput(
                second_file,
                output_directory / "nested" / "second.py",
            ),
        ]

        # glob ordering is not guaranteed.
        assert sorted(actual, key=repr) == sorted(expected, key=repr)

# Generated at 2026-10-24 05:54:54.686960
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 05:55:09.838479
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-24 05:55:24.056512
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    output_dir = tmp_path / "output"

    # A Python file can be mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")

    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # A supplied root preserves the path relative to that root.
    root = tmp_path / "root"
    nested_dir = root / "package"
    nested_dir.mkdir(parents=True)
    nested_file = nested_dir / "module.py"
    nested_file.write_text("x = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_file), str(output_dir), str(root)
    )) == [
        InputOutput(nested_file, output_dir / "package" / "module.py")
    ]

    # A directory input recursively includes only Python files.
    source_dir = tmp_path / "source"
    subdirectory = source_dir / "subdirectory"
    subdirectory.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = subdirectory / "second.py"
    ignored_file = source_dir / "ignored.txt"

    first_file.write_text("a = 1\n")
    second_file.write_text("b = 2\n")
    ignored_file.write_text("not Python\n")

    results = set(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))

    assert results == {
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(
            second_file,
            output_dir / "subdirectory" / "second.py",
        ),
    }

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

# Generated at 2026-10-24 05:55:44.652613
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with TemporaryDirectory() as tmp:
        base = Path(tmp)

        # A Python file mapped directly to another Python file.
        source = base / "source.py"
        source.write_text("print('hello')\n")
        target = base / "target.py"

        assert list(module_0.get_input_output_paths(str(source), str(target), None)) == [
            InputOutput(source, target)
        ]

        # A Python file mapped into an output directory.
        output_dir = base / "dist"

        assert list(
            module_0.get_input_output_paths(str(source), str(output_dir), None)
        ) == [
            InputOutput(source, output_dir / "source.py")
        ]

        # Preserve the path relative to a supplied root.
        project = base / "project"
        nested_source = project / "package" / "module.py"
        nested_source.parent.mkdir(parents=True)
        nested_source.write_text("VALUE = 1\n")

        assert list(
            module_0.get_input_output_paths(
                str(nested_source),
                str(output_dir),
                str(project),
            )
        ) == [
            InputOutput(nested_source, output_dir / "package" / "module.py")
        ]

        # Recursively process Python files in an input directory.
        input_dir = base / "src"
        first = input_dir / "first.py"
        second = input_dir / "nested" / "second.py"
        ignored = input_dir / "nested" / "ignored.txt"

        second.parent.mkdir(parents=True)
        first.write_text("FIRST = 1\n")
        second.write_text("SECOND = 2\n")
        ignored.write_text("not Python\n")

        results = list(
            module_0.get_input_output_paths(str(input_dir), str(output_dir), None)
        )
        expected = [
            InputOutput(first, output_dir / "first.py"),
            InputOutput(second, output_dir / "nested" / "second.py"),
        ]

        assert len(results) == len(expected)
        assert all(item in results for item in expected)

        # A directory cannot be mapped to a single Python file.
        with pytest.raises(InvalidInputOutput):
            list(
                module_0.get_input_output_paths(
                    str(input_dir),
                    str(base / "combined.py"),
                    None,
                )
            )

        # Missing inputs are rejected.
        with pytest.raises(InputDoesntExists):
            list(
                module_0.get_input_output_paths(
                    str(base / "missing.py"),
                    str(output_dir),
                    None,
                )
            )

# Generated at 2026-10-24 05:56:04.416922
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path: Path) -> None:
    source_root = tmp_path / "project"
    source_dir = source_root / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    first_file = source_dir / "first.py"
    second_file = package_dir / "second.py"
    ignored_file = source_dir / "README.txt"

    first_file.write_text("print('first')")
    second_file.write_text("print('second')")
    ignored_file.write_text("not Python")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_file), str(explicit_output), None
    )) == [
        InputOutput(first_file, explicit_output)
    ]

    # Python file to an output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(first_file), str(output_dir), None
    )) == [
        InputOutput(first_file, output_dir / "first.py")
    ]

    # Python file to an output directory while preserving its root-relative path.
    assert list(module_0.get_input_output_paths(
        str(second_file), str(output_dir), str(source_root)
    )) == [
        InputOutput(
            second_file,
            output_dir / "src" / "package" / "second.py",
        )
    ]

    # Directory input includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(first_file, output_dir / "first.py"),
        InputOutput(
            second_file,
            output_dir / "package" / "second.py",
        ),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(tmp_path / "combined.py"), None
        ))

    # A nonexistent input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:56:19.161355
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

    output_dir = tmp_path / "out"

    # Directory input recursively maps Python files to the output directory.
    results = list(
        module_0.get_input_output_paths(str(input_dir), str(output_dir), root=None)
    )

    assert len(results) == 2
    assert InputOutput(first_input, output_dir / "main.py") in results
    assert InputOutput(
        second_input, output_dir / "package" / "module.py"
    ) in results

    # A single Python file can be mapped directly to another Python file.
    output_file = tmp_path / "generated.py"
    assert list(
        module_0.get_input_output_paths(str(first_input), str(output_file), root=None)
    ) == [InputOutput(first_input, output_file)]

    # A single file mapped to a directory preserves its path relative to root.
    rooted_results = list(
        module_0.get_input_output_paths(
            str(second_input),
            str(output_dir),
            root=str(input_dir),
        )
    )
    assert rooted_results == [
        InputOutput(second_input, output_dir / "package" / "module.py")
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

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                root=None,
            )
        )

# Generated at 2026-10-24 05:56:33.601786
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
    nested_file.write_text("print('nested')")
    ignored_file.write_text("Not Python")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = output_dir / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_file), None
    )) == [
        InputOutput(main_file, output_file)
    ]

    # A Python file mapped to a directory keeps its file name.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # An explicit root preserves the path relative to that root.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(main_file, output_dir / "src" / "main.py")
    ]

    # Directories are searched recursively, excluding non-Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(main_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "nested" / "module.py"),
    ]

    assert len(results) == len(expected)
    for pair in expected:
        assert pair in results

    # A directory/non-Python input cannot map to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_dir / "single.py"), None
        ))

    # Missing inputs are rejected when the generator is consumed.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:56:51.355401
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    root = tmp_path / "project"
    source_dir = root / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')\n")

    other_file = nested_dir / "README.md"
    other_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # Python file to directory, preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(root)
    )) == [
        InputOutput(
            source_file,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    ))
    assert results == [
        InputOutput(
            source_file,
            output_dir / "package" / "module.py",
        )
    ]

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # Missing input raises the expected exception.
    missing_file = tmp_path / "missing.py"
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_file), str(output_dir), None
        ))

# Generated at 2026-10-24 05:57:04.833979
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "src"
    package = source_root / "package"
    package.mkdir(parents=True)

    first_input = package / "first.py"
    second_input = package / "second.py"
    ignored_input = package / "notes.txt"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    ignored_input.write_text("ignored")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_file), None
    )) == [
        InputOutput(first_input, output_file)
    ]

    # Python file to a directory without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), None
    )) == [
        InputOutput(first_input, output_dir / "first.py")
    ]

    # Python file to a directory while preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(first_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(first_input, output_dir / "package" / "first.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(source_root), str(output_dir), None
    ))
    expected = [
        InputOutput(first_input, output_dir / "package" / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_root), str(output_file), None
        ))

    # A missing input raises InputDoesntExists.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:57:26.234792
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    source_dir = project / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    source_file = nested_dir / "module.py"
    source_file.write_text("print('hello')\n")

    non_python_file = nested_dir / "README.txt"
    non_python_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    output_file = output_dir / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Python file to directory, without an explicit root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "module.py")
    ]

    # Python file to directory, preserving its path relative to root.
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_dir), str(project)
    )) == [
        InputOutput(
            source_file,
            output_dir / "src" / "package" / "module.py",
        )
    ]

    # Directory input recursively discovers only Python files.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(
            source_file,
            output_dir / "package" / "module.py",
        )
    ]

    # Directory input with an explicit root preserves the input directory.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), str(project)
    )) == [
        InputOutput(
            source_file,
            output_dir / "src" / "package" / "module.py",
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

# Generated at 2026-10-24 05:57:39.034369
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    # Python file to Python file.
    output_file = tmp_path / "output.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # Python file to an output directory.
    output_dir = tmp_path / "dist"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "input.py")
    ]

    # Preserve the path relative to the specified root.
    source_root = tmp_path / "project"
    nested_input = source_root / "src" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("value = 1")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(source_root)
    )) == [
        InputOutput(nested_input, output_dir / "src" / "module.py")
    ]

    # Recursively process Python files in an input directory.
    package = tmp_path / "package"
    nested_file = package / "sub" / "example.py"
    nested_file.parent.mkdir(parents=True)
    nested_file.write_text("value = 2")
    (package / "ignored.txt").write_text("not Python")

    assert list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    )) == [
        InputOutput(nested_file, output_dir / "sub" / "example.py")
    ]

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(output_file), None
        ))

    # The input must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:57:58.185225
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "input"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    python_file = nested_dir / "module.py"
    python_file.write_text("print('hello')")

    # Non-Python files should be ignored.
    (nested_dir / "README.md").write_text("documentation")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(
            python_file,
            output_dir / "package" / "module.py",
        )
    ]


def test_get_input_output_paths_for_single_file(tmp_path):
    input_file = tmp_path / "source.py"
    input_file.write_text("x = 1")

    output_file = tmp_path / "compiled.py"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        root=None,
    ))

    assert result == [InputOutput(input_file, output_file)]


def test_get_input_output_paths_for_single_file_to_directory(tmp_path):
    input_file = tmp_path / "source.py"
    input_file.write_text("x = 1")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=None,
    ))

    assert result == [
        InputOutput(input_file, output_dir / "source.py")
    ]


def test_get_input_output_paths_with_root(tmp_path):
    root = tmp_path / "project"
    input_file = root / "package" / "source.py"
    input_file.parent.mkdir(parents=True)
    input_file.write_text("x = 1")

    output_dir = tmp_path / "output"

    result = list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        root=str(root),
    ))

    assert result == [
        InputOutput(input_file, output_dir / "package" / "source.py")
    ]


def test_get_input_output_paths_rejects_directory_to_python_file(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        # Iteration is required because the function is a generator.
        list(module_0.get_input_output_paths(
            str(input_dir),
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

# Generated at 2026-10-24 05:58:13.462638
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

# Replace `your_package.module` with the module containing the function.
from your_package.module import get_input_output_paths
from your_package.types import InputOutput
from your_package.exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths_file_to_file(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_path),
        None,
    ))

    assert result == [InputOutput(input_path, output_path)]


def test_get_input_output_paths_file_to_directory(tmp_path):
    input_path = tmp_path / "input.py"
    output_dir = tmp_path / "output"
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_dir),
        None,
    ))

    assert result == [
        InputOutput(input_path, output_dir / "input.py"),
    ]


def test_get_input_output_paths_file_to_directory_with_root(tmp_path):
    root = tmp_path / "source"
    input_path = root / "package" / "input.py"
    output_dir = tmp_path / "output"

    input_path.parent.mkdir(parents=True)
    input_path.write_text("print('hello')")

    result = list(module_0.get_input_output_paths(
        str(input_path),
        str(output_dir),
        str(root),
    ))

    assert result == [
        InputOutput(input_path, output_dir / "package" / "input.py"),
    ]


def test_get_input_output_paths_directory(tmp_path):
    input_dir = tmp_path / "source"
    nested_dir = input_dir / "package"
    output_dir = tmp_path / "output"

    nested_dir.mkdir(parents=True)
    first_input = input_dir / "first.py"
    second_input = nested_dir / "second.py"

    first_input.write_text("print('first')")
    second_input.write_text("print('second')")
    (input_dir / "ignored.txt").write_text("not Python")

    result = list(module_0.get_input_output_paths(
        str(input_dir),
        str(output_dir),
        None,
    ))

    assert set(result) == {
        InputOutput(first_input, output_dir / "first.py"),
        InputOutput(second_input, output_dir / "package" / "second.py"),
    }


def test_get_input_output_paths_rejects_directory_to_python_file(tmp_path):
    input_dir = tmp_path / "source"
    input_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir),
            str(tmp_path / "output.py"),
            None,
        ))


def test_get_input_output_paths_rejects_missing_input(tmp_path):
    missing_input = tmp_path / "missing.py"

    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(missing_input),
            str(tmp_path / "output"),
            None,
        ))

# Generated at 2026-10-24 05:58:31.155713
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    source_file = package_dir / "module.py"
    source_file.write_text("print('hello')\n")

    ignored_file = package_dir / "README.txt"
    ignored_file.write_text("Not a Python file\n")

    output_dir = tmp_path / "build"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "compiled.py"
    assert list(module_0.get_input_output_paths(
        str(source_file), str(output_file), None
    )) == [
        InputOutput(source_file, output_file)
    ]

    # Without root, the input filename is appended to the output directory.
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

    # Directory input recursively includes only Python files.
    assert list(module_0.get_input_output_paths(
        str(source_dir), str(output_dir), None
    )) == [
        InputOutput(source_file, output_dir / "package" / "module.py")
    ]

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_file), None
        ))

    # The input path must exist.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:58:44.065589
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A single Python file mapped to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')")

    output_file = tmp_path / "output.py"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_file),
        None,
    )) == [InputOutput(input_file, output_file)]

    # A single Python file mapped into an output directory.
    output_dir = tmp_path / "dist"

    assert list(module_0.get_input_output_paths(
        str(input_file),
        str(output_dir),
        None,
    )) == [InputOutput(input_file, output_dir / "input.py")]

    # A directory is searched recursively, ignoring non-Python files.
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "package"
    nested_dir.mkdir(parents=True)

    first_file = source_dir / "main.py"
    second_file = nested_dir / "module.py"
    ignored_file = nested_dir / "README.txt"

    first_file.write_text("print('main')")
    second_file.write_text("VALUE = 1")
    ignored_file.write_text("ignored")

    results = set(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        None,
    ))

    assert results == {
        InputOutput(first_file, output_dir / "main.py"),
        InputOutput(second_file, output_dir / "package" / "module.py"),
    }

    # An explicit root is preserved in the output's relative structure.
    results = set(module_0.get_input_output_paths(
        str(source_dir),
        str(output_dir),
        str(tmp_path),
    ))

    assert results == {
        InputOutput(first_file, output_dir / "src" / "main.py"),
        InputOutput(
            second_file,
            output_dir / "src" / "package" / "module.py",
        ),
    }

    # A directory cannot be mapped to a single .py output file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir),
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

# Generated at 2026-10-24 05:58:57.878136
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        input_dir = tmp_path / "input"
        nested_dir = input_dir / "package"
        output_dir = tmp_path / "output"

        nested_dir.mkdir(parents=True)

        first_file = input_dir / "first.py"
        second_file = nested_dir / "second.py"
        ignored_file = input_dir / "README.md"

        first_file.write_text("print('first')")
        second_file.write_text("print('second')")
        ignored_file.write_text("Not a Python file")

        # A Python file mapped directly to another Python file.
        explicit_output = tmp_path / "result.py"
        assert list(module_0.get_input_output_paths(
            str(first_file), str(explicit_output), None
        )) == [
            InputOutput(first_file, explicit_output)
        ]

        # A Python file mapped into an output directory.
        assert list(module_0.get_input_output_paths(
            str(first_file), str(output_dir), None
        )) == [
            InputOutput(first_file, output_dir / "first.py")
        ]

        # The root directory is used to preserve the relative path.
        assert list(module_0.get_input_output_paths(
            str(second_file), str(output_dir), str(input_dir)
        )) == [
            InputOutput(second_file, output_dir / "package" / "second.py")
        ]

        # Directories are searched recursively, and non-Python files are ignored.
        actual = list(module_0.get_input_output_paths(
            str(input_dir), str(output_dir), None
        ))
        expected = [
            InputOutput(first_file, output_dir / "first.py"),
            InputOutput(second_file, output_dir / "package" / "second.py"),
        ]
        assert sorted(actual, key=lambda pair: str(pair.input)) == sorted(
            expected, key=lambda pair: str(pair.input)
        )

        # Generator functions do not execute until iterated, hence list(...).
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(input_dir), str(tmp_path / "output.py"), None
            ))

        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(tmp_path / "missing.py"), str(output_dir), None
            ))

# Generated at 2026-10-24 05:59:11.399482
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    source_dir = project / "src"
    package_dir = source_dir / "package"
    package_dir.mkdir(parents=True)

    main_file = source_dir / "main.py"
    module_file = package_dir / "module.py"
    ignored_file = package_dir / "README.txt"

    main_file.write_text("print('main')")
    module_file.write_text("print('module')")
    ignored_file.write_text("Not Python")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = output_dir / "renamed.py"
    assert list(module_0.get_input_output_paths(
        str(main_file), str(explicit_output), None
    )) == [
        InputOutput(main_file, explicit_output)
    ]

    # Python file to output directory without a root.
    assert list(module_0.get_input_output_paths(
        str(main_file), str(output_dir), None
    )) == [
        InputOutput(main_file, output_dir / "main.py")
    ]

    # Python file to output directory relative to a root.
    assert list(module_0.get_input_output_paths(
        str(module_file), str(output_dir), str(project)
    )) == [
        InputOutput(module_file, output_dir / "src" / "package" / "module.py")
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

    # A directory cannot be written to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(source_dir), str(output_dir / "combined.py"), None
        ))

    # Missing inputs are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 05:59:29.013138
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    def assert_pairs(actual, expected):
        actual = list(actual)
        assert len(actual) == len(expected)
        assert all(pair in actual for pair in expected)

    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    nested_dir.mkdir(parents=True)

    source_file = source_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = source_dir / "README.md"

    source_file.write_text("print('main')\n")
    nested_file.write_text("print('module')\n")
    ignored_file.write_text("Not Python\n")

    # A Python file can be mapped directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_file), None)
    ) == [
        InputOutput(source_file, output_file)
    ]

    # A Python file mapped to a directory keeps its filename.
    output_dir = tmp_path / "output"
    assert list(
        module_0.get_input_output_paths(str(source_file), str(output_dir), None)
    ) == [
        InputOutput(source_file, output_dir / "main.py")
    ]

    # Supplying a root preserves the path relative to that root.
    assert list(
        module_0.get_input_output_paths(
            str(source_file),
            str(output_dir),
            str(tmp_path),
        )
    ) == [
        InputOutput(source_file, output_dir / "src" / "main.py")
    ]

    # Directory input recursively includes only Python files.
    assert_pairs(
        module_0.get_input_output_paths(str(source_dir), str(output_dir), None),
        [
            InputOutput(source_file, output_dir / "main.py"),
            InputOutput(nested_file, output_dir / "nested" / "module.py"),
        ],
    )

    # A directory cannot be mapped to a single Python output file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "combined.py"),
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

# Generated at 2026-10-24 05:59:46.933675
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_root = tmp_path / "source"
    package = source_root / "package"
    package.mkdir(parents=True)

    module = package / "module.py"
    module.write_text("print('hello')\n")

    nested = package / "nested"
    nested.mkdir()
    nested_module = nested / "other.py"
    nested_module.write_text("print('other')\n")

    non_python_file = package / "README.md"
    non_python_file.write_text("Ignored")

    output_dir = tmp_path / "output"

    # Python file to Python file.
    explicit_output = output_dir / "renamed.py"
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

    # Python file to output directory while preserving its root-relative path.
    assert list(module_0.get_input_output_paths(
        str(module), str(output_dir), str(source_root)
    )) == [
        InputOutput(module, output_dir / "package" / "module.py")
    ]

    # Directory input recursively includes only Python files.
    results = list(module_0.get_input_output_paths(
        str(package), str(output_dir), None
    ))
    assert len(results) == 2
    assert InputOutput(module, output_dir / "module.py") in results
    assert InputOutput(
        nested_module, output_dir / "nested" / "other.py"
    ) in results

    # A directory cannot be mapped to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(package), str(output_dir / "single.py"), None
        ))

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 06:00:04.231928
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / "src"
    nested_dir = input_dir / "package"
    nested_dir.mkdir(parents=True)

    input_file = input_dir / "main.py"
    nested_file = nested_dir / "module.py"
    ignored_file = nested_dir / "README.md"

    input_file.write_text("print('main')")
    nested_file.write_text("print('module')")
    ignored_file.write_text("Not a Python file")

    output_dir = tmp_path / "output"

    # A Python file can map directly to another Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_file), None
    )) == [
        InputOutput(input_file, output_file)
    ]

    # A Python file mapped to a directory keeps its filename.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None
    )) == [
        InputOutput(input_file, output_dir / "main.py")
    ]

    # When root is supplied, the relative directory structure is retained.
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(tmp_path)
    )) == [
        InputOutput(input_file, output_dir / "src" / "main.py")
    ]

    # Directories are searched recursively, and non-Python files are ignored.
    results = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None
    ))
    expected = [
        InputOutput(input_file, output_dir / "main.py"),
        InputOutput(nested_file, output_dir / "package" / "module.py"),
    ]

    assert len(results) == len(expected)
    assert all(item in results for item in expected)

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

# Generated at 2026-10-24 06:00:18.777766
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        input_dir = base / "input"
        nested_dir = input_dir / "package"
        output_dir = base / "output"

        nested_dir.mkdir(parents=True)

        first_file = input_dir / "main.py"
        second_file = nested_dir / "module.py"
        ignored_file = nested_dir / "README.txt"

        first_file.write_text("print('main')")
        second_file.write_text("print('module')")
        ignored_file.write_text("not Python")

        # Python file to Python file.
        explicit_output = base / "result.py"
        assert list(module_0.get_input_output_paths(
            str(first_file), str(explicit_output), None
        )) == [
            InputOutput(first_file, explicit_output)
        ]

        # Python file to an output directory.
        assert list(module_0.get_input_output_paths(
            str(first_file), str(output_dir), None
        )) == [
            InputOutput(first_file, output_dir / "main.py")
        ]

        # Python file to an output directory relative to a root.
        assert list(module_0.get_input_output_paths(
            str(second_file), str(output_dir), str(input_dir)
        )) == [
            InputOutput(second_file, output_dir / "package" / "module.py")
        ]

        # Recursively process only Python files in a directory.
        results = list(module_0.get_input_output_paths(
            str(input_dir), str(output_dir), None
        ))
        assert sorted(results, key=lambda item: str(item.input)) == sorted(
            [
                InputOutput(first_file, output_dir / "main.py"),
                InputOutput(
                    second_file,
                    output_dir / "package" / "module.py",
                ),
            ],
            key=lambda item: str(item.input),
        )

        # A directory cannot be mapped to a single Python file.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(
                str(input_dir), str(explicit_output), None
            ))

        # The input path must exist.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(base / "missing.py"), str(output_dir), None
            ))

# Generated at 2026-10-24 06:00:21.194097
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:00:24.056027
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:00:34.140600
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-10-24 06:00:50.341403
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # A Python file mapped directly to another Python file.
    input_file = tmp_path / "input.py"
    input_file.write_text("print('hello')\n")

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

    # Preserve the path relative to an explicitly supplied root.
    root = tmp_path / "src"
    nested_input = root / "package" / "module.py"
    nested_input.parent.mkdir(parents=True)
    nested_input.write_text("VALUE = 1\n")

    assert list(module_0.get_input_output_paths(
        str(nested_input), str(output_dir), str(root)
    )) == [
        InputOutput(nested_input, output_dir / "package" / "module.py")
    ]

    # Recursively map Python files from an input directory.
    another_input = root / "top_level.py"
    another_input.write_text("VALUE = 2\n")
    ignored_file = root / "package" / "README.txt"
    ignored_file.write_text("Not a Python file\n")

    actual = list(module_0.get_input_output_paths(
        str(root), str(output_dir), None
    ))
    expected = [
        InputOutput(another_input, output_dir / "top_level.py"),
        InputOutput(nested_input, output_dir / "package" / "module.py"),
    ]
    assert sorted(actual, key=lambda item: str(item.input)) == sorted(
        expected, key=lambda item: str(item.input)
    )

    # A non-Python input cannot be mapped to a single .py output.
    non_python_input = tmp_path / "input.txt"
    non_python_input.write_text("text\n")

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(non_python_input), str(output_file), None
        ))

    # Missing input paths are rejected.
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / "missing.py"), str(output_dir), None
        ))

# Generated at 2026-10-24 06:01:04.039975
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    source_dir = tmp_path / "src"
    source_dir.mkdir()

    module = source_dir / "module.py"
    module.write_text("print('module')\n", encoding="utf-8")

    nested_dir = source_dir / "package"
    nested_dir.mkdir()

    nested_module = nested_dir / "nested.py"
    nested_module.write_text("print('nested')\n", encoding="utf-8")

    non_python_file = source_dir / "README.md"
    non_python_file.write_text("Documentation", encoding="utf-8")

    output_dir = tmp_path / "output"

    # A Python input file can map directly to a Python output file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(module), str(output_file), None)) == [
        InputOutput(Path(module), Path(output_file))
    ]

    # A Python input file mapped to a directory retains its filename.
    assert list(module_0.get_input_output_paths(str(module), str(output_dir), None)) == [
        InputOutput(Path(module), Path(output_dir / "module.py"))
    ]

    # An explicit root preserves the path relative to that root.
    assert list(
        module_0.get_input_output_paths(str(module), str(output_dir), str(tmp_path))
    ) == [
        InputOutput(Path(module), Path(output_dir / "src" / "module.py"))
    ]

    # Directory input recursively includes only Python files.
    actual = set(module_0.get_input_output_paths(str(source_dir), str(output_dir), None))
    expected = {
        InputOutput(Path(module), Path(output_dir / "module.py")),
        InputOutput(
            Path(nested_module),
            Path(output_dir / "package" / "nested.py"),
        ),
    }
    assert actual == expected

    # A directory cannot map to a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(source_dir),
                str(tmp_path / "combined.py"),
                None,
            )
        )

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 06:01:06.457227
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:08.870567
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:11.284861
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:13.848950
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:16.263473
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:18.676751
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:21.095761
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:23.507101
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:25.920957
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:28.337185
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:30.751557
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:33.167498
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:35.579714
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:37.995204
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:40.409038
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:42.823983
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:45.240193
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:47.653803
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:50.067949
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:52.483318
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:54.897405
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:57.310751
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:01:59.727037
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:02.143014
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:04.558756
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:06.974953
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:09.391947
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:11.803720
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:14.218618
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:16.635360
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:19.048553
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:21.462967
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:23.878280
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:02:42.132080
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-10-24 06:03:08.355969
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    project = tmp_path / "project"
    source = project / "pkg" / "main.py"
    second_source = project / "lib" / "utils.py"
    ignored_file = project / "README.txt"

    source.parent.mkdir(parents=True)
    second_source.parent.mkdir(parents=True)
    source.write_text("print('main')\n", encoding="utf-8")
    second_source.write_text("print('utils')\n", encoding="utf-8")
    ignored_file.write_text("Not a Python file", encoding="utf-8")

    # Python file to Python file.
    output_file = tmp_path / "result.py"
    assert list(module_0.get_input_output_paths(str(source), str(output_file), None)) == [
        InputOutput(source, output_file)
    ]

    # Python file to output directory, without an explicit root.
    output_dir = tmp_path / "output"
    assert list(module_0.get_input_output_paths(str(source), str(output_dir), None)) == [
        InputOutput(source, output_dir / "main.py")
    ]

    # Python file to output directory, preserving its path relative to root.
    assert list(
        module_0.get_input_output_paths(str(source), str(output_dir), str(project))
    ) == [
        InputOutput(source, output_dir / "pkg" / "main.py")
    ]

    # Directory input recursively includes only Python files.
    actual = list(
        module_0.get_input_output_paths(str(project), str(output_dir), None)
    )
    expected = [
        InputOutput(source, output_dir / "pkg" / "main.py"),
        InputOutput(second_source, output_dir / "lib" / "utils.py"),
    ]
    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # An explicit root is also respected for directory input.
    actual = list(
        module_0.get_input_output_paths(str(project), str(output_dir), str(tmp_path))
    )
    expected = [
        InputOutput(source, output_dir / "project" / "pkg" / "main.py"),
        InputOutput(
            second_source,
            output_dir / "project" / "lib" / "utils.py",
        ),
    ]
    assert len(actual) == len(expected)
    assert all(pair in actual for pair in expected)

    # A directory cannot be converted into a single Python file.
    with pytest.raises(InvalidInputOutput):
        list(
            module_0.get_input_output_paths(
                str(project),
                str(tmp_path / "invalid.py"),
                None,
            )
        )

    # Missing input raises the expected exception.
    with pytest.raises(InputDoesntExists):
        list(
            module_0.get_input_output_paths(
                str(tmp_path / "missing.py"),
                str(output_dir),
                None,
            )
        )

# Generated at 2026-10-24 06:03:10.771019
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:13.187379
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:15.602929
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:18.018857
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:20.434905
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:22.847852
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:25.262722
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:27.676718
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:30.091103
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:32.507785
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:34.920649
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:37.334058
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:39.748643
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:42.163357
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:44.577906
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:46.991773
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:49.408986
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 06:03:51.823891
# Unit test for function get_input_output_paths