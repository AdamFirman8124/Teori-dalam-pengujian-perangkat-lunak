

# Generated at 2026-11-01 20:43:32.523112
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import os
    import shutil
    import tempfile

    import pytest

    temp_dir = tempfile.mkdtemp()
    try:
        project_dir = os.path.join(temp_dir, 'project')
        nested_dir = os.path.join(project_dir, 'nested')
        os.makedirs(nested_dir)

        foo_py = os.path.join(project_dir, 'foo.py')
        bar_py = os.path.join(nested_dir, 'bar.py')
        baz_txt = os.path.join(project_dir, 'baz.txt')
        for path in (foo_py, bar_py, baz_txt):
            with open(path, 'w') as f:
                f.write('\n')

        out_dir = os.path.join(temp_dir, 'out')
        os.makedirs(out_dir)

        # Single .py input to single .py output
        target_py = os.path.join(out_dir, 'target.py')
        results = list(module_0.get_input_output_paths(foo_py, target_py, None))
        assert len(results) == 1
        assert results[0][0] == Path(foo_py)
        assert results[0][1] == Path(target_py)

        # Single .py input to directory output without root
        results = list(module_0.get_input_output_paths(foo_py, out_dir, None))
        assert len(results) == 1
        assert results[0][0] == Path(foo_py)
        assert results[0][1] == Path(out_dir) / 'foo.py'

        # Single .py input to directory output with matching root
        results = list(module_0.get_input_output_paths(foo_py, out_dir, project_dir))
        assert len(results) == 1
        assert results[0][1] == Path(out_dir) / 'foo.py'

        # Nested .py input preserves structure relative to root
        results = list(module_0.get_input_output_paths(bar_py, out_dir, project_dir))
        assert len(results) == 1
        assert results[0][1] == Path(out_dir) / 'nested' / 'bar.py'

        # Nested .py input with outer root keeps parent directories
        results = list(module_0.get_input_output_paths(bar_py, out_dir, temp_dir))
        assert len(results) == 1
        assert results[0][1] == Path(out_dir) / 'project' / 'nested' / 'bar.py'

        # Directory input collects every .py file recursively
        results = sorted(
            module_0.get_input_output_paths(project_dir, out_dir, None),
            key=lambda pair: str(pair[0]),
        )
        assert len(results) == 2
        assert {str(r[0]): r[1] for r in results} == {
            str(Path(foo_py)): Path(out_dir) / 'foo.py',
            str(Path(bar_py)): Path(out_dir) / 'nested' / 'bar.py',
        }

        # Directory input with explicit root
        results = list(module_0.get_input_output_paths(project_dir, out_dir, temp_dir))
        assert len(results) == 2
        outputs = {r[1] for r in results}
        assert Path(out_dir) / 'project' / 'foo.py' in outputs
        assert Path(out_dir) / 'project' / 'nested' / 'bar.py' in outputs

        # Non-.py input with .py output is invalid
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(baz_txt,
                                        os.path.join(out_dir, 'x.py'), None))

        # Missing input file raises InputDoesntExists
        missing_py = os.path.join(temp_dir, 'missing.py')
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(missing_py, out_dir, None))
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

# Generated at 2026-11-01 20:44:22.602264
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Single .py file -> single .py file.
        source = tmp / 'source.py'
        source.write_text('')
        target = tmp / 'target.py'
        assert list(module_0.get_input_output_paths(str(source), str(target), None)) == [
            InputOutput(source, target)]

        # Single .py file -> directory (no root): keeps the file name.
        out_dir = tmp / 'out'
        out_dir.mkdir()
        assert list(module_0.get_input_output_paths(str(source), str(out_dir), None)) == [
            InputOutput(source, out_dir / 'source.py')]

        # Single .py file -> directory with explicit root.
        pkg = tmp / 'pkg'
        pkg.mkdir()
        module = pkg / 'module.py'
        module.write_text('')
        assert list(module_0.get_input_output_paths(str(module), str(out_dir),
                                           str(tmp))) == [
            InputOutput(module, out_dir / 'pkg' / 'module.py')]

        # Directory input: recursively collects all *.py files.
        (pkg / '__init__.py').write_text('')
        sub = pkg / 'sub'
        sub.mkdir()
        (sub / 'inner.py').write_text('')

        results = sorted(module_0.get_input_output_paths(str(pkg), str(out_dir), None),
                         key=lambda pair: str(pair.input))
        expected = sorted(
            [InputOutput(pkg / '__init__.py', out_dir / '__init__.py'),
             InputOutput(pkg / 'module.py', out_dir / 'module.py'),
             InputOutput(sub / 'inner.py', out_dir / 'sub' / 'inner.py')],
            key=lambda pair: str(pair.input))
        assert results == expected

        # Directory input with external root: paths relative to root.
        results = sorted(module_0.get_input_output_paths(str(pkg), str(out_dir),
                                                str(tmp)),
                         key=lambda pair: str(pair.input))
        expected = sorted(
            [InputOutput(pkg / '__init__.py',
                         out_dir / 'pkg' / '__init__.py'),
             InputOutput(pkg / 'module.py',
                         out_dir / 'pkg' / 'module.py'),
             InputOutput(sub / 'inner.py',
                         out_dir / 'pkg' / 'sub' / 'inner.py')],
            key=lambda pair: str(pair.input))
        assert results == expected

        # Non-.py input with .py output -> InvalidInputOutput.
        text_file = tmp / 'notes.txt'
        text_file.write_text('')
        _expect_raises(InvalidInputOutput, get_input_output_paths,
                       str(text_file), str(tmp / 'result.py'), None)

        # Missing input -> InputDoesntExists.
        _expect_raises(InputDoesntExists, get_input_output_paths,
                       str(tmp / 'missing.py'), str(tmp / 'result.py'), None)

# Generated at 2026-11-01 20:44:47.269172
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .types import InputOutput
from .exceptions import InvalidInputOutput, InputDoesntExists


def test_get_input_output_paths(tmp_path):
    # Build a fake project layout:
    # tmp_path/
    #   input_dir/a.py
    #   input_dir/sub/b.py
    #   output_dir/
    input_dir = tmp_path / 'input_dir'
    sub_dir = input_dir / 'sub'
    sub_dir.mkdir(parents=True)
    (input_dir / 'a.py').write_text('x = 1\n')
    (sub_dir / 'b.py').write_text('y = 2\n')
    output_dir = tmp_path / 'output_dir'
    output_dir.mkdir()

    # Output ends with .py but input does not -> InvalidInputOutput
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(
            str(input_dir), str(output_dir / 'out.py'), None))

    # Input does not exist -> InputDoesntExists
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / 'missing.py'), str(output_dir), None))

    # Single .py input, single .py output
    single_in = input_dir / 'a.py'
    single_out = output_dir / 'renamed.py'
    result = list(module_0.get_input_output_paths(
        str(single_in), str(single_out), None))
    assert result == [InputOutput(single_in, single_out)]

    # Single .py input, directory output, no root -> filename joined to output
    result = list(module_0.get_input_output_paths(
        str(single_in), str(output_dir), None))
    assert result == [InputOutput(single_in, output_dir / 'a.py')]

    # Single .py input, directory output, root given -> relative path to root
    result = list(module_0.get_input_output_paths(
        str(single_in), str(output_dir), str(input_dir)))
    assert result == [InputOutput(single_in, output_dir / 'a.py')]

    result = list(module_0.get_input_output_paths(
        str(single_in), str(output_dir), str(tmp_path)))
    assert result == [InputOutput(single_in, output_dir / 'input_dir' / 'a.py')]

    # Directory input, directory output, no root -> paths relative to input dir
    result = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None))
    assert set(result) == {
        InputOutput(input_dir / 'a.py', output_dir / 'a.py'),
        InputOutput(input_dir / 'sub' / 'b.py', output_dir / 'sub' / 'b.py'),
    }

    # Directory input, directory output, root given -> paths relative to root
    result = list(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), str(tmp_path)))
    assert set(result) == {
        InputOutput(input_dir / 'a.py',
                    output_dir / 'input_dir' / 'a.py'),
        InputOutput(input_dir / 'sub' / 'b.py',
                    output_dir / 'input_dir' / 'sub' / 'b.py'),
    }

# Generated at 2026-11-01 20:46:34.292960
# Unit test for function get_input_output_paths

# Generated at 2026-11-01 20:47:57.227522
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile


# Generated at 2026-11-01 20:48:27.676612
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest


def _create_project(tmp_path):
    """Create a sample project tree and return its root path."""
    pkg = tmp_path / 'pkg'
    sub = pkg / 'sub'
    sub.mkdir(parents=True)
    (pkg / '__init__.py').write_text('# init')
    (pkg / 'main.py').write_text('# main')
    (sub / 'helper.py').write_text('# helper')
    (pkg / 'data.txt').write_text('not python')
    return pkg


def test_file_to_file(tmp_path):
    src = tmp_path / 'hello.py'
    src.write_text('')
    dst = tmp_path / 'renamed.py'

    result = list(module_0.get_input_output_paths(str(src), str(dst), None))

    assert result == [InputOutput(src, dst)]


def test_file_to_directory_without_root(tmp_path):
    src_dir = tmp_path / 'src'
    src_dir.mkdir()
    src = src_dir / 'hello.py'
    src.write_text('')
    out_dir = tmp_path / 'build'

    result = list(module_0.get_input_output_paths(str(src), str(out_dir), None))

    assert result == [InputOutput(src, out_dir / 'hello.py')]


def test_file_to_directory_with_root(tmp_path):
    project = tmp_path / 'project'
    package = project / 'package'
    package.mkdir(parents=True)
    src = package / 'module.py'
    src.write_text('')
    out_dir = tmp_path / 'build'

    result = list(module_0.get_input_output_paths(str(src), str(out_dir), str(project)))

    assert result == [InputOutput(src, out_dir / 'package' / 'module.py')]


def test_directory_recursively_finds_python_files(tmp_path):
    root = _create_project(tmp_path)
    out_dir = tmp_path / 'build'

    result = list(module_0.get_input_output_paths(str(root), str(out_dir), None))

    mapping = {io.input: io.output for io in result}
    assert mapping == {
        root / 'pkg' / '__init__.py': out_dir / 'pkg' / '__init__.py',
        root / 'pkg' / 'main.py': out_dir / 'pkg' / 'main.py',
        root / 'pkg' / 'sub' / 'helper.py': out_dir / 'pkg' / 'sub' / 'helper.py',
    }


def test_directory_ignores_non_python_files(tmp_path):
    root = _create_project(tmp_path)
    out_dir = tmp_path / 'build'

    inputs = [io.input for io in
              module_0.get_input_output_paths(str(root), str(out_dir), None)]

    assert root / 'pkg' / 'data.txt' not in inputs


def test_directory_output_respects_root_argument(tmp_path):
    root = _create_project(tmp_path)
    out_dir = tmp_path / 'build'

    mapping = {str(io.input): str(io.output)
               for io in module_0.get_input_output_paths(str(root), str(out_dir),
                                                str(root))}

    assert mapping[str(root / 'pkg' / 'main.py')] == \
        str(out_dir / 'pkg' / 'main.py')


def test_output_ends_with_py_but_input_is_directory_raises(tmp_path):
    src_dir = tmp_path / 'src'
    src_dir.mkdir()

    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(src_dir), str(tmp_path / 'out.py'),
                                    None))


def test_nonexistent_input_file_raises(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / 'missing.py'),
                                    str(tmp_path / 'out.py'), None))


def test_nonexistent_input_directory_raises(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / 'missing'),
                                    str(tmp_path / 'out'), None))


def test_invalid_output_checked_before_existence(tmp_path):
    # Input is missing and output ends with '.py' while input does not:
    # InvalidInputOutput must take precedence over InputDoesntExists.
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(tmp_path / 'missing'),
                                    str(tmp_path / 'out.py'), None))

# Generated at 2026-11-01 20:49:13.609793
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .exceptions import InvalidInputOutput, InputDoesntExists
from .types import InputOutput


def test_get_input_output_paths(tmp_path):
    input_dir = tmp_path / 'input'
    input_dir.mkdir()
    output_dir = tmp_path / 'output'
    output_dir.mkdir()

    input_file = input_dir / 'one.py'
    input_file.write_text('# one')

    # Single file -> single file
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir / 'one.py'), None)) == [
        InputOutput(input_file, output_dir / 'one.py'),
    ]

    # Single file -> directory (output gets input's name)
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), None)) == [
        InputOutput(input_file, output_dir / 'one.py'),
    ]

    # Single file -> directory with root (relative path preserved)
    assert list(module_0.get_input_output_paths(
        str(input_file), str(output_dir), str(tmp_path))) == [
        InputOutput(input_file, output_dir / 'input' / 'one.py'),
    ]

    # Directory -> directory (recursive glob)
    sub = input_dir / 'sub'
    sub.mkdir()
    second_file = sub / 'two.py'
    second_file.write_text('# two')

    assert sorted(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), None)) == [
        InputOutput(input_file, output_dir / 'one.py'),
        InputOutput(second_file, output_dir / 'sub' / 'two.py'),
    ]

    # Directory -> directory with root
    assert sorted(module_0.get_input_output_paths(
        str(input_dir), str(output_dir), str(tmp_path))) == [
        InputOutput(input_file, output_dir / 'input' / 'one.py'),
        InputOutput(second_file, output_dir / 'input' / 'sub' / 'two.py'),
    ]


def test_get_input_output_paths_invalid_output(tmp_path):
    # Output ends with .py but input does not
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths('input.txt', str(tmp_path / 'out.py'), None))


def test_get_input_output_paths_input_doesnt_exist(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(
            str(tmp_path / 'missing.py'), str(tmp_path / 'out'), None))

# Generated at 2026-11-01 20:50:36.218289
# Unit test for function get_input_output_paths