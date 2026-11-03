

# Generated at 2026-11-02 13:59:47.762583
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        pkg = tmp_path / 'pkg'
        sub = pkg / 'sub'
        sub.mkdir(parents=True)
        (pkg / '__init__.py').write_text('')
        (pkg / 'main.py').write_text('')
        (sub / 'mod.py').write_text('')

        # Single .py input to single .py output
        result = list(module_0.get_input_output_paths(
            str(pkg / 'main.py'), str(tmp_path / 'out.py'), None))
        assert result == [InputOutput(pkg / 'main.py', tmp_path / 'out.py')]

        # Single .py input to directory output (no root)
        result = list(module_0.get_input_output_paths(
            str(pkg / 'main.py'), str(tmp_path / 'build'), None))
        assert result == [InputOutput(pkg / 'main.py',
                                      tmp_path / 'build' / 'main.py')]

        # Single .py input to directory output (with root)
        result = list(module_0.get_input_output_paths(
            str(pkg / 'main.py'), str(tmp_path / 'build'), str(tmp_path)))
        assert result == [InputOutput(pkg / 'main.py',
                                      tmp_path / 'build' / 'pkg' / 'main.py')]

        # Directory input to directory output (no root)
        result = list(module_0.get_input_output_paths(
            str(pkg), str(tmp_path / 'build'), None))
        expected = [
            InputOutput(pkg / '__init__.py',
                        tmp_path / 'build' / '__init__.py'),
            InputOutput(pkg / 'main.py', tmp_path / 'build' / 'main.py'),
            InputOutput(pkg / 'sub' / 'mod.py',
                        tmp_path / 'build' / 'sub' / 'mod.py'),
        ]
        assert len(result) == len(expected)
        for item in expected:
            assert item in result

        # Directory input to directory output (with root)
        result = list(module_0.get_input_output_paths(
            str(pkg), str(tmp_path / 'build'), str(tmp_path)))
        expected = [
            InputOutput(pkg / '__init__.py',
                        tmp_path / 'build' / 'pkg' / '__init__.py'),
            InputOutput(pkg / 'main.py',
                        tmp_path / 'build' / 'pkg' / 'main.py'),
            InputOutput(pkg / 'sub' / 'mod.py',
                        tmp_path / 'build' / 'pkg' / 'sub' / 'mod.py'),
        ]
        assert len(result) == len(expected)
        for item in expected:
            assert item in result

        # .py output with non-.py input raises InvalidInputOutput
        with pytest.raises(InvalidInputOutput):
            list(module_0.get_input_output_paths(str(pkg),
                                        str(tmp_path / 'out.py'), None))

        # Nonexistent input raises InputDoesntExists
        with pytest.raises(InputDoesntExists):
            list(module_0.get_input_output_paths(
                str(tmp_path / 'missing.py'),
                str(tmp_path / 'out.py'), None))

# Generated at 2026-11-02 14:04:18.589123
# Unit test for function get_input_output_paths

# Generated at 2026-11-02 14:05:34.430095
# Unit test for function get_input_output_paths
def test_get_input_output_paths():input_file = tmp_path / "a.py"