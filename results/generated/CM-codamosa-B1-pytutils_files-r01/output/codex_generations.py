

# Generated at 2026-10-24 05:47:32.413173
# Unit test for function burp

# Generated at 2026-10-24 05:47:33.845188
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:47:54.067200
# Unit test for function burp

# Generated at 2026-10-24 05:47:55.416962
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:48:28.333654
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        fh.write(contents)
        filename = fh.name

    try:
        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate in fixed-size chunks.
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5]
            for i in range(0, len(contents), 5)
        ]

        # Compatibility string for line mode.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 05:48:44.813440
# Unit test for function islurp

# Generated at 2026-10-24 05:48:52.593290
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:48:57.311813
# Unit test for function burp

# Generated at 2026-10-24 05:48:58.857618
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:49:15.349376
# Unit test for function islurp

# Generated at 2026-10-24 05:49:22.802454
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:49:29.354286
# Unit test for function burp
def test_burp():
    import tempfile

    contents = "Hello, world!\nSecond line.\n"
    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents
    finally:
        os.remove(filename)

# Generated at 2026-10-24 05:50:03.455400
# Unit test for function islurp

# Generated at 2026-10-24 05:50:08.470483
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 05:50:44.108411
# Unit test for function islurp
def test_islurp():
    import tempfile

    # --- Test 1: iterate by line (default LINEMODE) ---
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    try:
        assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']

        # --- Test 2: explicit LINEMODE via string sentinel ---
        assert list(module_0.islurp(path, iter_by='LINEMODE')) == ['alpha\n', 'beta\n', 'gamma\n']

        # --- Test 3: iterate by fixed byte chunks ---
        assert list(module_0.islurp(path, iter_by=5)) == ['alpha', '\nbeta', '\ngam', 'ma\n']

        # --- Test 4: binary mode with chunking ---
        assert list(module_0.islurp(path, mode='rb', iter_by=4)) == [
            b'alph', b'a\nbe', b'ta\n', b'gamm', b'a\n'
        ]

        # --- Test 5: expandvars expands environment variables in the path ---
        os.environ['ISLURP_TEST_VAR'] = path
        try:
            assert list(module_0.islurp('$ISLURP_TEST_VAR', expandvars=True)) == [
                'alpha\n', 'beta\n', 'gamma\n'
            ]
        finally:
            del os.environ['ISLURP_TEST_VAR']

        # --- Test 6: expanduser/expandvars disabled leaves raw path intact ---
        assert list(module_0.islurp(path, expanduser=False, expandvars=False)) == [
            'alpha\n', 'beta\n', 'gamma\n'
        ]

        # --- Test 7: empty file yields nothing ---
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
            empty_path = fh.name
        try:
            assert list(module_0.islurp(empty_path)) == []
        finally:
            os.remove(empty_path)

        # --- Test 8: missing file raises an IOError ---
        missing = os.path.join(tempfile.gettempdir(), 'islurp_no_such_file_test')
        raised = False
        try:
            list(module_0.islurp(missing))
        except IOError:
            raised = True
        assert raised, "Expected IOError for a nonexistent file"

        # --- Test 9: generator is lazy (no read before iteration) ---
        gen = module_0.islurp(path)
        assert list(gen) == ['alpha\n', 'beta\n', 'gamma\n']
    finally:
        os.remove(path)

# Generated at 2026-10-24 05:50:52.708519
# Unit test for function burp

# Generated at 2026-10-24 05:50:55.225086
# Unit test for function burp

# Generated at 2026-10-24 05:50:57.637066
# Unit test for function burp

# Generated at 2026-10-24 05:51:00.051539
# Unit test for function islurp

# Generated at 2026-10-24 05:51:02.466532
# Unit test for function islurp

# Generated at 2026-10-24 05:51:04.883233
# Unit test for function islurp

# Generated at 2026-10-24 05:51:07.493926
# Unit test for function islurp
def test_islurp():
    import tempfile

    # --- Test 1: iterate by line (default LINEMODE) ---
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    try:
        assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']

        # --- Test 2: explicit LINEMODE via string sentinel ---
        assert list(module_0.islurp(path, iter_by='LINEMODE')) == ['alpha\n', 'beta\n', 'gamma\n']

        # --- Test 3: iterate by fixed byte chunks ---
        assert list(module_0.islurp(path, iter_by=5)) == ['alpha', '\nbeta', '\ngam', 'ma\n']

        # --- Test 4: binary mode with chunking ---
        assert list(module_0.islurp(path, mode='rb', iter_by=4)) == [
            b'alph', b'a\nbe', b'ta\n', b'gamm', b'a\n'
        ]

        # --- Test 5: expandvars expands environment variables in the path ---
        os.environ['ISLURP_TEST_VAR'] = path
        try:
            assert list(module_0.islurp('$ISLURP_TEST_VAR', expandvars=True)) == [
                'alpha\n', 'beta\n', 'gamma\n'
            ]
        finally:
            del os.environ['ISLURP_TEST_VAR']

        # --- Test 6: expanduser/expandvars disabled leaves raw path intact ---
        assert list(module_0.islurp(path, expanduser=False, expandvars=False)) == [
            'alpha\n', 'beta\n', 'gamma\n'
        ]

        # --- Test 7: empty file yields nothing ---
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
            empty_path = fh.name
        try:
            assert list(module_0.islurp(empty_path)) == []
        finally:
            os.remove(empty_path)

        # --- Test 8: missing file raises an IOError ---
        missing = os.path.join(tempfile.gettempdir(), 'islurp_no_such_file_test')
        raised = False
        try:
            list(module_0.islurp(missing))
        except IOError:
            raised = True
        assert raised, "Expected IOError for a nonexistent file"

        # --- Test 9: generator is lazy (no read before iteration) ---
        gen = module_0.islurp(path)
        assert list(gen) == ['alpha\n', 'beta\n', 'gamma\n']
    finally:
        os.remove(path)

# Generated at 2026-10-24 05:51:15.749435
# Unit test for function burp
def test_burp():
    import tempfile

    contents = "Hello, world!\n"

    with tempfile.TemporaryDirectory() as directory:
        filename = os.path.join(directory, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

# Generated at 2026-10-24 05:51:24.312250
# Unit test for function burp

# Generated at 2026-10-24 05:51:25.622749
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:51:54.558983
# Unit test for function islurp

# Generated at 2026-10-24 05:51:56.975342
# Unit test for function islurp

# Generated at 2026-10-24 05:51:59.394227
# Unit test for function islurp

# Generated at 2026-10-24 05:52:01.808690
# Unit test for function islurp

# Generated at 2026-10-24 05:52:04.224031
# Unit test for function islurp

# Generated at 2026-10-24 05:52:06.639467
# Unit test for function islurp

# Generated at 2026-10-24 05:52:17.291405
# Unit test for function burp
def test_burp():
    import io

# Generated at 2026-10-24 05:52:27.429530
# Unit test for function burp

# Generated at 2026-10-24 05:52:28.766205
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:53:06.034377
# Unit test for function islurp
def test_islurp():import io
import pytest


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "example.txt"
    path.write_text("first line\nsecond line\n", encoding="utf-8")

    # Default line-by-line iteration
    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
    ]

    # Fixed-size chunks
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\n",
    ]

    # Environment-variable expansion
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert list(module_0.islurp("$ISLURP_TEST_DIR/example.txt")) == [
        "first line\n",
        "second line\n",
    ]

    # Standard input should be supported and must not be closed
    stdin = io.StringIO("stdin line 1\nstdin line 2\n")
    monkeypatch.setattr(sys, "stdin", stdin)

    assert list(module_0.islurp("-")) == [
        "stdin line 1\n",
        "stdin line 2\n",
    ]
    assert not stdin.closed

    # Binary mode must stop at b'' rather than yielding it forever
    binary_path = tmp_path / "example.bin"
    binary_path.write_bytes(b"\x01\x02")

    chunks = module_0.islurp(str(binary_path), mode="rb", iter_by=2)
    assert next(chunks) == b"\x01\x02"
    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-24 05:53:08.451923
# Unit test for function burp

# Generated at 2026-10-24 05:53:10.865619
# Unit test for function burp

# Generated at 2026-10-24 05:53:13.282266
# Unit test for function burp

# Generated at 2026-10-24 05:53:29.773460
# Unit test for function islurp

# Generated at 2026-10-24 05:53:35.324739
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:53:47.406338
# Unit test for function burp
def test_burp():
    import io

# Generated at 2026-10-24 05:54:03.890252
# Unit test for function islurp

# Generated at 2026-10-24 05:54:10.136639
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:54:12.786392
# Unit test for function burp

# Generated at 2026-10-24 05:54:19.774087
# Unit test for function burp
def test_burp():import tempfile


# Generated at 2026-10-24 05:54:27.034786
# Unit test for function burp

# Generated at 2026-10-24 05:54:28.465786
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:55:06.682777
# Unit test for function islurp

# Generated at 2026-10-24 05:55:13.640015
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:55:16.146966
# Unit test for function burp

# Generated at 2026-10-24 05:55:17.444792
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:55:33.902451
# Unit test for function islurp

# Generated at 2026-10-24 05:55:38.509434
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:55:50.371194
# Unit test for function burp

# Generated at 2026-10-24 05:55:51.683040
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:56:01.967268
# Unit test for function burp
def test_burp():
    import io

# Generated at 2026-10-24 05:56:18.443558
# Unit test for function islurp

# Generated at 2026-10-24 05:56:24.485488
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 05:56:35.956076
# Unit test for function burp

# Generated at 2026-10-24 05:56:37.349558
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 05:56:50.710964
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from unittest.mock import patch

    contents = "hello\nworld\n"

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "output.txt")

        result = module_0.burp(filename, contents)

        assert result is None
        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with patch.object(sys, "stdout", stdout):
        result = module_0.burp("-", contents)

    assert result is None
    assert stdout.getvalue() == contents

# Generated at 2026-10-24 05:57:21.756553
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "line 1\nline 2\n"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        fh.write(contents)
        filename = fh.name

    try:
        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == ["line 1\n", "line 2\n"]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "line 1\n",
            "line 2\n",
        ]

        # Fixed-size chunks
        assert list(module_0.islurp(filename, iter_by=4)) == [
            "line",
            " 1\nl",
            "ine ",
            "2\n",
        ]

        # Alias
        assert slurp is islurp
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 05:57:38.243722
# Unit test for function islurp

# Generated at 2026-10-24 05:57:44.776476
# Unit test for function islurp
def test_islurp():import os