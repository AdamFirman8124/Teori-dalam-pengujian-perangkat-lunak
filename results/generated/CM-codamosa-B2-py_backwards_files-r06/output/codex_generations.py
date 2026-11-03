

# Generated at 2026-11-02 15:09:04.130070
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Create a package with some python files.
        pkg = tmp_path / 'pkg'
        sub = pkg / 'sub'
        sub.mkdir(parents=True)
        file_a = pkg / 'a.py'
        file_b = sub / 'b.py'
        file_a.write_text('# a\n')
        file_b.write_text('# b\n')
        out_dir = tmp_path / 'out'

        # Single .py input with .py output.
        result = list(module_0.get_input_output_paths(
            str(file_a), str(tmp_path / 'renamed.py'), None))
        assert [(io.input, io.output) for io in result] == [
            (file_a, tmp_path / 'renamed.py'),
        ]

        # Single .py input with directory output and no root.
        result = list(module_0.get_input_output_paths(str(file_a), str(out_dir), None))
        assert [(io.input, io.output) for io in result] == [
            (file_a, out_dir / 'a.py'),
        ]

        # Single .py input with directory output and a root.
        result = list(module_0.get_input_output_paths(
            str(file_a), str(out_dir), str(tmp_path)))
        assert [(io.input, io.output) for io in result] == [
            (file_a, out_dir / 'pkg' / 'a.py'),
        ]

        # Directory input with no root: paths relative to the input directory.
        result = sorted(
            module_0.get_input_output_paths(str(pkg), str(out_dir), None),
            key=lambda io: str(io.input))
        assert [(io.input, io.output) for io in result] == [
            (file_a, out_dir / 'a.py'),
            (file_b, out_dir / 'sub' / 'b.py'),
        ]

        # Directory input with a root: paths relative to the root.
        result = sorted(
            module_0.get_input_output_paths(str(pkg), str(out_dir), str(tmp_path)),
            key=lambda io: str(io.input))
        assert [(io.input, io.output) for io in result] == [
            (file_a, out_dir / 'pkg' / 'a.py'),
            (file_b, out_dir / 'pkg' / 'sub' / 'b.py'),
        ]

        # .py output with a non-.py input raises InvalidInputOutput.
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(str(pkg), str(out_dir / 'x.py'), None))

        # Nonexistent input raises InputDoesntExists.
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(tmp_path / 'missing.py'), str(out_dir), None))

# Generated at 2026-11-02 15:11:19.157928
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def test_get_input_output_paths(tmp_path):
    # Single .py file to single .py file
    input_file = tmp_path / 'input.py'
    input_file.touch()
    output_file = tmp_path / 'output.py'
    assert list(module_0.get_input_output_paths(str(input_file), str(output_file), None)) == [
        InputOutput(input_file, output_file),
    ]

    # Single .py file to directory (no root) -> output keeps the file name
    output_dir = tmp_path / 'output'
    assert list(module_0.get_input_output_paths(str(input_file), str(output_dir), None)) == [
        InputOutput(input_file, output_dir / 'input.py'),
    ]

    # Single .py file to directory with root -> path relative to root
    root = tmp_path / 'root'
    root.mkdir()
    nested_input = root / 'input.py'
    nested_input.touch()
    assert list(module_0.get_input_output_paths(str(nested_input), str(output_dir), str(root))) == [
        InputOutput(nested_input, output_dir / 'input.py'),
    ]

    # Directory input (no root) -> all nested .py files, relative to the input dir
    input_dir = tmp_path / 'input'
    input_dir.mkdir()
    (input_dir / 'a.py').touch()
    sub_dir = input_dir / 'sub'
    sub_dir.mkdir()
    (sub_dir / 'b.py').touch()
    results = sorted(module_0.get_input_output_paths(str(input_dir), str(output_dir), None),
                     key=lambda pair: str(pair.input))
    assert results == [
        InputOutput(input_dir / 'a.py', output_dir / 'a.py'),
        InputOutput(input_dir / 'sub' / 'b.py', output_dir / 'sub' / 'b.py'),
    ]

    # Directory input with root -> paths relative to root
    root2 = tmp_path / 'root2'
    nested_dir = root2 / 'input'
    nested_dir.mkdir(parents=True)
    (nested_dir / 'a.py').touch()
    assert list(module_0.get_input_output_paths(str(nested_dir), str(output_dir), str(root2))) == [
        InputOutput(nested_dir / 'a.py', output_dir / 'input' / 'a.py'),
    ]

    # Non-.py input with .py output -> InvalidInputOutput
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(input_dir), str(tmp_path / 'out.py'), None))

    # Non-existing input -> InputDoesntExists
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / 'missing.py'),
                                    str(tmp_path / 'out.py'), None))

# Generated at 2026-11-02 15:12:49.299813
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile

# Generated at 2026-11-02 15:15:00.770808
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as tmp_str:
        tmp = Path(tmp_str)

        # Output endswith .py but input doesn't -> InvalidInputOutput
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(str(tmp), str(tmp / 'out.py'), None))

        # Input doesn't exist -> InputDoesntExists
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(str(tmp / 'missing.py'), str(tmp / 'out'), None))

        # Single .py file -> single .py output
        src_file = tmp / 'src.py'
        src_file.write_text('x = 1\n')
        out_file = tmp / 'out.py'
        assert list(module_0.get_input_output_paths(str(src_file), str(out_file), None)) == [
            InputOutput(src_file, out_file)]

        # Single .py file -> directory output without root
        out_dir = tmp / 'out'
        assert list(module_0.get_input_output_paths(str(src_file), str(out_dir), None)) == [
            InputOutput(src_file, out_dir / 'src.py')]

        # Single .py file -> directory output with root
        root = tmp / 'project'
        pkg_dir = root / 'pkg'
        pkg_dir.mkdir(parents=True)
        nested_file = pkg_dir / 'mod.py'
        nested_file.write_text('y = 2\n')
        assert list(module_0.get_input_output_paths(
            str(nested_file), str(out_dir), str(root))) == [
            InputOutput(nested_file, out_dir / 'pkg' / 'mod.py')]

        # Directory input without root: only .py files, relative to input dir
        src_dir = tmp / 'srcdir'
        sub_dir = src_dir / 'sub'
        sub_dir.mkdir(parents=True)
        (src_dir / 'a.py').write_text('a = 1\n')
        (sub_dir / 'b.py').write_text('b = 2\n')
        (src_dir / 'c.txt').write_text('not python\n')

        results = sorted(
            module_0.get_input_output_paths(str(src_dir), str(out_dir), None),
            key=lambda io: str(io.input))
        assert results == [
            InputOutput(src_dir / 'a.py', out_dir / 'a.py'),
            InputOutput(sub_dir / 'b.py', out_dir / 'sub' / 'b.py'),
        ]

        # Directory input with root: paths relative to root
        results = sorted(
            module_0.get_input_output_paths(str(src_dir), str(out_dir), str(tmp)),
            key=lambda io: str(io.input))
        assert results == [
            InputOutput(src_dir / 'a.py', out_dir / 'srcdir' / 'a.py'),
            InputOutput(sub_dir / 'b.py', out_dir / 'srcdir' / 'sub' / 'b.py'),
        ]