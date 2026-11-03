

# Generated at 2026-11-02 11:08:33.558798
# Unit test for function burp
def test_burp():import pytest


def test_burp(tmp_path, capsys, monkeypatch):
    # --- basic write (default mode 'w') ---
    target = tmp_path / "out.txt"
    module_0.burp(str(target), "hello world")
    assert target.read_text() == "hello world"

    # --- overwrite with mode 'w' ---
    module_0.burp(str(target), "second")
    assert target.read_text() == "second"

    # --- append with mode 'a' ---
    module_0.burp(str(target), " more", mode="a")
    assert target.read_text() == "second more"

    # --- binary mode ---
    bin_target = tmp_path / "out.bin"
    module_0.burp(str(bin_target), b"\x00\x01\x02", mode="wb")
    assert bin_target.read_bytes() == b"\x00\x01\x02"

    # --- filename '-' writes to stdout when allow_stdout=True (default) ---
    module_0.burp("-", "stdout content")
    captured = capsys.readouterr()
    assert captured.out == "stdout content"
    assert not (tmp_path / "-").exists()  # no file created

    # --- filename '-' with allow_stdout=False writes to a literal '-' file ---
    monkeypatch.chdir(tmp_path)
    module_0.burp("-", "file content", allow_stdout=False)
    assert (tmp_path / "-").read_text() == "file content"

    # --- expandvars=True expands $VARS in the filename ---
    monkeypatch.setenv("BURP_TEST_VAR", "expanded")
    module_0.burp(str(tmp_path / "$BURP_TEST_VAR"), "vars expanded")
    assert (tmp_path / "expanded").read_text() == "vars expanded"

    # --- expandvars=False leaves the name literal ---
    literal_file = tmp_path / "$BURP_TEST_VAR"
    module_0.burp(str(literal_file), "literal", expandvars=False)
    assert literal_file.read_text() == "literal"

    # --- expanduser=True expands '~' to the home directory ---
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("USERPROFILE", str(fake_home))  # Windows compatibility
    module_0.burp("~/tilde.txt", "home sweet home")
    assert (fake_home / "tilde.txt").read_text() == "home sweet home"

    # --- expanduser=False leaves '~' literal in the path ---
    monkeypatch.chdir(tmp_path)
    (tmp_path / "~").mkdir()
    module_0.burp("~/literal.txt", "no expansion", expanduser=False)
    assert (tmp_path / "~" / "literal.txt").read_text() == "no expansion"

    # --- burp returns None ---
    assert module_0.burp(str(tmp_path / "ret.txt"), "x") is None

# Generated at 2026-11-02 11:09:33.027399
# Unit test for function burp
def test_burp():
    import os
    import tempfile
    from io import StringIO
    from unittest import mock

    # Basic write to a real file
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'out.txt')
        module_0.burp(path, 'hello world')
        with open(path) as fh:
            assert fh.read() == 'hello world'

    # Append mode
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'out.txt')
        module_0.burp(path, 'one')
        module_0.burp(path, 'two', mode='a')
        with open(path) as fh:
            assert fh.read() == 'onetwo'

    # Binary mode
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'out.bin')
        module_0.burp(path, b'\x00\x01', mode='wb')
        with open(path, 'rb') as fh:
            assert fh.read() == b'\x00\x01'

    # Writing to '-' goes to stdout
    buf = StringIO()
    with mock.patch('sys.stdout', new=buf):
        module_0.burp('-', 'to stdout')
    assert buf.getvalue() == 'to stdout'

    # allow_stdout=False with '-' treats it as a literal filename
    with mock.patch('builtins.open', mock.mock_open()) as mopen:
        module_0.burp('-', 'data', allow_stdout=False)
        mopen.assert_called_once_with('-', 'w')
        mopen().write.assert_called_once_with('data')

    # expanduser is applied to the filename
    with mock.patch('os.path.expanduser', return_value='/expanded/path') as mu:
        with mock.patch('builtins.open', mock.mock_open()) as mopen:
            module_0.burp('~/file.txt', 'data')
            mu.assert_called_once_with('~/file.txt')
            mopen.assert_called_once_with('/expanded/path', 'w')

    # expandvars is applied to the filename
    with mock.patch('os.path.expandvars', return_value='/vars/path') as mv:
        with mock.patch('builtins.open', mock.mock_open()) as mopen:
            module_0.burp('$HOME/file.txt', 'data')
            mv.assert_called_once_with('$HOME/file.txt')
            mopen.assert_called_once_with('/vars/path', 'w')

    # expanduser/expandvars disabled leaves filename untouched
    with mock.patch('os.path.expanduser') as mu, \
         mock.patch('os.path.expandvars') as mv, \
         mock.patch('builtins.open', mock.mock_open()) as mopen:
        module_0.burp('~/plain/$VAR', 'data', expanduser=False, expandvars=False)
        assert not mu.called
        assert not mv.called
        mopen.assert_called_once_with('~/plain/$VAR', 'w')

# Generated at 2026-11-02 11:11:34.793248
# Unit test for function burp

# Generated at 2026-11-02 11:14:03.012096
# Unit test for function burp
def test_burp():import io

# Generated at 2026-11-02 11:18:06.181257
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = 'line1\nline2\nline3\n'
    fd, path = tempfile.mkstemp(suffix='.txt')
    with os.fdopen(fd, 'w') as f:
        f.write(contents)

    try:
        # Basic line-by-line reading (LINEMODE default)
        lines = list(module_0.islurp(path))
        assert lines == ['line1\n', 'line2\n', 'line3\n']

        # iter_by='LINEMODE' string is accepted and behaves like default
        assert list(module_0.islurp(path, iter_by='LINEMODE')) == lines

        # Iterate by chunks of bytes
        chunks = list(module_0.islurp(path, iter_by=5))
        assert ''.join(chunks) == contents
        assert all(0 < len(c) <= 5 for c in chunks)

        # Binary mode
        bchunks = list(module_0.islurp(path, mode='rb', iter_by=4))
        assert b''.join(bchunks) == contents.encode('utf-8')

        # expandvars: env var in filename is expanded
        os.environ['ISLURP_TEST_VAR'] = path
        assert list(module_0.islurp('$ISLURP_TEST_VAR')) == lines

        # expandvars=False: literal '$...' does not resolve -> open fails
        try:
            list(module_0.islurp('$ISLURP_TEST_VAR', expandvars=False))
            raised = False
        except IOError:
            raised = True
        assert raised

        del os.environ['ISLURP_TEST_VAR']

        # expanduser: '~' expands to home directory
        home_file = os.path.join(os.path.expanduser('~'), os.path.basename(path))
        try:
            # place the file in home dir under a temp name and read via '~'
            tmp_in_home = os.path.join(os.path.expanduser('~'), '.islurp_test_tmp')
            with open(tmp_in_home, 'w') as f:
                f.write(contents)
            assert list(module_0.islurp('~/.islurp_test_tmp')) == lines
            os.remove(tmp_in_home)
        except Exception:
            if os.path.exists(os.path.join(os.path.expanduser('~'), '.islurp_test_tmp')):
                os.remove(os.path.join(os.path.expanduser('~'), '.islurp_test_tmp'))
            raise

        # expanduser=False: '~' is literal -> open fails
        try:
            list(module_0.islurp('~/definitely_missing_file_xyz', expanduser=False))
            raised = False
        except IOError:
            raised = True
        assert raised

        # Missing file raises IOError
        try:
            list(module_0.islurp(os.path.join(path, 'no_such_dir', 'no_file')))
            raised = False
        except IOError:
            raised = True
        assert raised

        # Convenience attributes and alias
        assert islurp.LINEMODE == LINEMODE == 0
        assert slurp is islurp
    finally:
        if os.path.exists(path):
            os.remove(path)