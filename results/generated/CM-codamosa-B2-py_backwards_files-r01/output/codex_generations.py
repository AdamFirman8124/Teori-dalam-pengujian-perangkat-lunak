

# Generated at 2026-11-02 13:02:31.223245
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # output ends with .py but input does not -> InvalidInputOutput
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(str(tmp_path), 'out.py', None))

        # input does not exist -> InputDoesntExists
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(tmp_path / 'missing.py'), 'out.py', None))

        # single .py file to single .py output
        src = tmp_path / 'a.py'
        src.write_text('')
        pairs = list(module_0.get_input_output_paths(
            str(src), str(tmp_path / 'b.py'), None))
        assert pairs == [InputOutput(src, tmp_path / 'b.py')]

        # single .py file to directory output (no root)
        out_dir = tmp_path / 'out'
        pairs = list(module_0.get_input_output_paths(str(src), str(out_dir), None))
        assert pairs == [InputOutput(src, out_dir / 'a.py')]

        # single .py file to directory output (with root)
        pairs = list(module_0.get_input_output_paths(
            str(src), str(out_dir), str(tmp_path)))
        assert pairs == [InputOutput(src, out_dir / 'a.py')]

        # directory input (no root): paths relative to the input dir
        pkg = tmp_path / 'pkg'
        sub = pkg / 'sub'
        sub.mkdir(parents=True)
        (pkg / 'x.py').write_text('')
        (sub / 'y.py').write_text('')

        pairs = list(module_0.get_input_output_paths(str(pkg), str(out_dir), None))
        assert set(pairs) == {
            InputOutput(pkg / 'x.py', out_dir / 'x.py'),
            InputOutput(sub / 'y.py', out_dir / 'sub' / 'y.py'),
        }

        # directory input (with root): paths relative to the given root
        pairs = list(module_0.get_input_output_paths(
            str(pkg), str(out_dir), str(tmp_path)))
        assert set(pairs) == {
            InputOutput(pkg / 'x.py', out_dir / 'pkg' / 'x.py'),
            InputOutput(sub / 'y.py', out_dir / 'pkg' / 'sub' / 'y.py'),
        }

# Generated at 2026-11-02 13:05:40.036763
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .exceptions import InputDoesntExists, InvalidInputOutput


def test_get_input_output_paths(tmp_path):
    # Single .py input -> single .py output
    src = tmp_path / 'src.py'
    src.write_text('')
    assert list(module_0.get_input_output_paths(str(src), str(tmp_path / 'dst.py'), None)) == [
        InputOutput(src, tmp_path / 'dst.py')]

    # Single .py input -> directory output (no root)
    assert list(module_0.get_input_output_paths(str(src), str(tmp_path / 'out'), None)) == [
        InputOutput(src, tmp_path / 'out' / 'src.py')]

    # Single .py input -> directory output (with root)
    assert list(module_0.get_input_output_paths(str(src), str(tmp_path / 'out'), str(tmp_path))) == [
        InputOutput(src, tmp_path / 'out' / 'src.py')]

    # Directory input -> directory output (no root)
    pkg = tmp_path / 'pkg'
    (pkg / 'sub').mkdir(parents=True)
    (pkg / 'a.py').write_text('')
    (pkg / 'sub' / 'b.py').write_text('')
    results = list(module_0.get_input_output_paths(str(pkg), str(tmp_path / 'out'), None))
    assert sorted(results, key=lambda io: str(io.input)) == [
        InputOutput(pkg / 'a.py', tmp_path / 'out' / 'a.py'),
        InputOutput(pkg / 'sub' / 'b.py', tmp_path / 'out' / 'sub' / 'b.py')]

    # Directory input -> directory output (with root)
    results = list(module_0.get_input_output_paths(str(pkg), str(tmp_path / 'out'), str(tmp_path)))
    assert sorted(results, key=lambda io: str(io.input)) == [
        InputOutput(pkg / 'a.py', tmp_path / 'out' / 'pkg' / 'a.py'),
        InputOutput(pkg / 'sub' / 'b.py', tmp_path / 'out' / 'pkg' / 'sub' / 'b.py')]

    # Output ends with .py but input doesn't -> InvalidInputOutput
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(pkg), str(tmp_path / 'out.py'), None))

    # Input doesn't exist -> InputDoesntExists
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / 'missing.py'),
                                    str(tmp_path / 'out.py'), None))