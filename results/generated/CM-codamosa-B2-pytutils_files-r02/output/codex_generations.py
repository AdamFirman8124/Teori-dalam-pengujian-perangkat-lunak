

# Generated at 2026-11-03 00:04:17.967729
# Unit test for function burp
def test_burp():import os
import sys

import pytest


def test_burp_writes_contents_to_file(tmp_path):
    target = tmp_path / "out.txt"
    module_0.burp(str(target), "hello world")
    assert target.read_text() == "hello world"


def test_burp_overwrites_existing_file(tmp_path):
    target = tmp_path / "out.txt"
    target.write_text("old contents")
    module_0.burp(str(target), "new contents")
    assert target.read_text() == "new contents"


def test_burp_append_mode(tmp_path):
    target = tmp_path / "out.txt"
    module_0.burp(str(target), "first\n")
    module_0.burp(str(target), "second\n", mode="a")
    assert target.read_text() == "first\nsecond\n"


def test_burp_binary_mode(tmp_path):
    target = tmp_path / "out.bin"
    module_0.burp(str(target), b"\x00\x01\x02", mode="wb")
    assert target.read_bytes() == b"\x00\x01\x02"


def test_burp_stdout(tmp_path, capsys):
    module_0.burp("-", "to stdout")
    captured = capsys.readouterr()
    assert captured.out == "to stdout"


def test_burp_stdout_disabled_writes_literal_dash_file(tmp_path):
    target = tmp_path / "-"
    module_0.burp(str(target), "literal dash", allow_stdout=False)
    assert target.read_text() == "literal dash"


def test_burp_allow_stdout_false_with_dash(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module_0.burp("-", "file not stdout", allow_stdout=False)
    assert (tmp_path / "-").read_text() == "file not stdout"


def test_burp_expanduser(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    module_0.burp("~/burp_test.txt", "expanded home")
    assert (tmp_path / "burp_test.txt").read_text() == "expanded home"


def test_burp_expandvars(tmp_path, monkeypatch):
    monkeypatch.setenv("BURP_DIR", str(tmp_path))
    module_0.burp("$BURP_DIR/vars.txt", "expanded vars")
    assert (tmp_path / "vars.txt").read_text() == "expanded vars"


def test_burp_no_expandvars(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("BURP_VAR", str(tmp_path))
    filename = "$BURP_VAR/literal.txt"
    module_0.burp(filename, "no expansion", expandvars=False)
    assert (tmp_path / "$BURP_VAR" / "literal.txt").read_text() == "no expansion"


def test_burp_no_expanduser(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    filename = "~/noexpand.txt"
    module_0.burp(filename, "no tilde expansion", expanduser=False)
    assert (tmp_path / "~" / "noexpand.txt").read_text() == "no tilde expansion"

# Generated at 2026-11-03 00:07:22.506585
# Unit test for function islurp

# Generated at 2026-11-03 00:09:28.036058
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-11-03 00:11:33.783734
# Unit test for function burp
def test_burp():
    import tempfile
    import io
    from contextlib import redirect_stdout

    with tempfile.TemporaryDirectory() as tmpdir:
        # Basic write
        path = os.path.join(tmpdir, 'test.txt')
        module_0.burp(path, 'hello world')
        with open(path) as fh:
            assert fh.read() == 'hello world'

        # Append mode
        module_0.burp(path, ' more', mode='a')
        with open(path) as fh:
            assert fh.read() == 'hello world more'

        # Binary mode
        binpath = os.path.join(tmpdir, 'test.bin')
        module_0.burp(binpath, b'\x00\x01\x02', mode='wb')
        with open(binpath, 'rb') as fh:
            assert fh.read() == b'\x00\x01\x02'

        # Write to stdout when filename is '-'
        buf = io.StringIO()
        with redirect_stdout(buf):
            module_0.burp('-', 'to stdout')
        assert buf.getvalue() == 'to stdout'

        # allow_stdout=False means '-' is treated as a literal filename
        dash_path = os.path.join(tmpdir, 'dash')
        module_0.burp(dash_path, 'to file', allow_stdout=False)
        with open(dash_path) as fh:
            assert fh.read() == 'to file'

        # expanduser expands ~
        old_home = os.environ.get('HOME')
        os.environ['HOME'] = os.path.join(tmpdir, 'fakehome')
        try:
            module_0.burp('~/file.txt', 'expanded user')
            with open(os.path.join(tmpdir, 'fakehome', 'file.txt')) as fh:
                assert fh.read() == 'expanded user'
        finally:
            if old_home is not None:
                os.environ['HOME'] = old_home

        # expandvars expands environment variables
        os.environ['BURP_TEST_VAR'] = tmpdir
        try:
            module_0.burp('$BURP_TEST_VAR/vars.txt', 'vars expanded')
            with open(os.path.join(tmpdir, 'vars.txt')) as fh:
                assert fh.read() == 'vars expanded'

            # expandvars=False leaves env vars untouched
            noexpand_dir = os.path.join(tmpdir, 'noexpand')
            os.makedirs(noexpand_dir, exist_ok=True)
            module_0.burp(os.path.join(noexpand_dir, '$BURP_TEST_VAR'), 'raw',
                 expandvars=False)
            with open(os.path.join(noexpand_dir, '$BURP_TEST_VAR')) as fh:
                assert fh.read() == 'raw'

            # expanduser=False leaves ~ untouched
            module_0.burp(os.path.join(tmpdir, '~literal'), 'raw',
                 expanduser=False)
            with open(os.path.join(tmpdir, '~literal')) as fh:
                assert fh.read() == 'raw'
        finally:
            del os.environ['BURP_TEST_VAR']
# nonce:4a615de1

# Generated at 2026-11-03 00:13:51.412863
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from unittest import mock

    tmpdir = tempfile.mkdtemp()

    # 1. Basic write to a file
    path = os.path.join(tmpdir, 'out.txt')
    module_0.burp(path, 'hello world')
    with open(path) as fh:
        assert fh.read() == 'hello world'

    # 2. Append mode
    module_0.burp(path, ' more', mode='a')
    with open(path) as fh:
        assert fh.read() == 'hello world more'

    # 3. Writing to stdout when filename is '-' and allow_stdout is True
    buf = io.StringIO()
    with mock.patch.object(sys, 'stdout', buf):
        module_0.burp('-', 'to stdout')
    assert buf.getvalue() == 'to stdout'

    # 4. allow_stdout=False writes to a literal '-' file
    module_0.burp('-', 'to file', allow_stdout=False)
    try:
        with open('-') as fh:
            assert fh.read() == 'to file'
    finally:
        os.remove('-')

    # 5. expandvars expands environment variables in the filename
    with mock.patch.dict(os.environ, {'BURP_TEST_VAR': 'expanded'}):
        var_path = os.path.join(tmpdir, '$BURP_TEST_VAR.txt')
        expected = os.path.join(tmpdir, 'expanded.txt')
        module_0.burp(var_path, 'vars expanded')
        with open(expected) as fh:
            assert fh.read() == 'vars expanded'

    # 6. expanduser is applied to the filename
    home_file = os.path.join(tmpdir, 'homefile.txt')
    with mock.patch('os.path.expanduser', return_value=home_file):
        module_0.burp('~/homefile.txt', 'user expanded')
    with open(home_file) as fh:
        assert fh.read() == 'user expanded'

    # 7. expanduser/expandvars disabled leaves the filename untouched
    raw = os.path.join(tmpdir, '$NOVAR$.txt')
    with mock.patch.dict(os.environ, {'NOVAR': 'x'}):
        module_0.burp(raw, 'raw', expandvars=False, expanduser=False)
    with open(raw) as fh:
        assert fh.read() == 'raw'

    # 8. Binary mode write
    bin_path = os.path.join(tmpdir, 'out.bin')
    module_0.burp(bin_path, b'\x00\x01', mode='wb')
    with open(bin_path, 'rb') as fh:
        assert fh.read() == b'\x00\x01'

    # cleanup
    for name in os.listdir(tmpdir):
        os.remove(os.path.join(tmpdir, name))
    os.rmdir(tmpdir)