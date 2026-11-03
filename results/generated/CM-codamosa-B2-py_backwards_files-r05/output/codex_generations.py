

# Generated at 2026-11-03 00:48:30.667502
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # Build a source tree:
        # src/module.py
        # src/package/inner.py
        # src/not_python.txt
        src = tmp_path / 'src'
        package = src / 'package'
        package.mkdir(parents=True)
        (src / 'module.py').write_text('x = 1\n')
        (package / 'inner.py').write_text('y = 2\n')
        (src / 'not_python.txt').write_text('nope')

        out = tmp_path / 'out'
        out.mkdir()

        # Single .py input with .py output -> direct mapping
        pairs = list(module_0.get_input_output_paths(
            str(src / 'module.py'), str(tmp_path / 'renamed.py'), None))
        assert pairs == [
            InputOutput(src / 'module.py', tmp_path / 'renamed.py'),
        ]

        # Single .py input with directory output, no root -> output dir + file name
        pairs = list(module_0.get_input_output_paths(
            str(src / 'module.py'), str(out), None))
        assert pairs == [
            InputOutput(src / 'module.py', out / 'module.py'),
        ]

        # Single .py input with directory output and root -> output dir + relative path
        pairs = list(module_0.get_input_output_paths(
            str(package / 'inner.py'), str(out), str(src)))
        assert pairs == [
            InputOutput(package / 'inner.py', out / 'package' / 'inner.py'),
        ]

        # Directory input, no root -> all .py files relative to input dir
        pairs = sorted(module_0.get_input_output_paths(str(src), str(out), None),
                       key=lambda p: str(p.input))
        assert pairs == [
            InputOutput(src / 'module.py', out / 'module.py'),
            InputOutput(package / 'inner.py', out / 'package' / 'inner.py'),
        ]

        # Directory input with root outside input dir -> relative to root
        pairs = sorted(module_0.get_input_output_paths(str(src), str(out), str(tmp_path)),
                       key=lambda p: str(p.input))
        assert pairs == [
            InputOutput(src / 'module.py', out / 'src' / 'module.py'),
            InputOutput(package / 'inner.py', out / 'src' / 'package' / 'inner.py'),
        ]

        # Output ends with .py but input is a directory -> InvalidInputOutput
        try:
            list(module_0.get_input_output_paths(str(src), str(tmp_path / 'bad.py'), None))
        except InvalidInputOutput:
            pass
        else:
            raise AssertionError('Expected InvalidInputOutput')

        # Nonexistent input -> InputDoesntExists
        try:
            list(module_0.get_input_output_paths(
                str(tmp_path / 'missing.py'),
                str(tmp_path / 'missing_out.py'), None))
        except InputDoesntExists:
            pass
        else:
            raise AssertionError('Expected InputDoesntExists')

# Generated at 2026-11-03 00:50:53.824836
# Unit test for function get_input_output_paths

# Generated at 2026-11-03 00:53:43.810889
# Unit test for function get_input_output_paths
def test_get_input_output_paths():from pathlib import Path