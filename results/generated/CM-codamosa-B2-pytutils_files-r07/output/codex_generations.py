

# Generated at 2026-10-24 04:04:14.569112
# Unit test for function burp

# Generated at 2026-10-24 04:04:26.288481
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:04:43.900989
# Unit test for function burp

# Generated at 2026-10-24 04:04:45.203215
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:04:51.375201
# Unit test for function burp

# Generated at 2026-10-24 04:04:52.709868
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:05:23.121538
# Unit test for function islurp

# Generated at 2026-10-24 04:05:30.018981
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:05:43.088513
# Unit test for function burp
def test_burp():
    import tempfile

    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        contents = "Hello, world!\nSecond line.\n"
        module_0.burp(filename, contents)

        with open(filename, 'r') as fh:
            assert fh.read() == contents
    finally:
        os.remove(filename)

# Generated at 2026-10-24 04:06:18.936373
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "line one\nline two\n"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        filename = fh.name
        fh.write(contents)

    try:
        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "line one\n",
            "line two\n",
        ]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "line one\n",
            "line two\n",
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=5)) == [
            "line ",
            "one\nl",
            "ine t",
            "wo\n",
        ]
    finally:
        os.remove(filename)

# Generated at 2026-10-24 04:06:21.358976
# Unit test for function islurp

# Generated at 2026-10-24 04:06:23.779464
# Unit test for function islurp

# Generated at 2026-10-24 04:06:30.076998
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:06:59.481337
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "input.txt")
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Explicit symbolic line mode.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate in fixed-size chunks.
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Expand environment variables in the path.
        old_tmpdir = os.environ.get("ISLURP_TEST_DIR")
        os.environ["ISLURP_TEST_DIR"] = tmpdir
        try:
            expanded_path = os.path.join("$ISLURP_TEST_DIR", "input.txt")
            assert "".join(module_0.islurp(expanded_path)) == contents
        finally:
            if old_tmpdir is None:
                os.environ.pop("ISLURP_TEST_DIR", None)
            else:
                os.environ["ISLURP_TEST_DIR"] = old_tmpdir

    # Read from standard input.
    old_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(contents)
        assert "".join(module_0.islurp("-")) == contents
    finally:
        sys.stdin = old_stdin

# Generated at 2026-10-24 04:07:35.487368
# Unit test for function islurp
def test_islurp():import io
import sys

import pytest


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "sample.txt"
    path.write_text("first line\nsecond line\nlast", encoding="utf-8")

    # Default line-by-line iteration.
    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
        "last",
    ]

    # Fixed-size text chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\nla",
        "st",
    ]

    # String form of LINEMODE.
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "first line\n",
        "second line\n",
        "last",
    ]

    # Environment-variable expansion.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert list(module_0.islurp("$ISLURP_TEST_DIR/sample.txt"))[0] == "first line\n"

    # stdin support.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin line\n"))
    assert list(module_0.islurp("-")) == ["stdin line\n"]


def test_islurp_binary_eof(tmp_path):
    path = tmp_path / "sample.bin"
    path.write_bytes(b"abcdef")

    chunks = module_0.islurp(str(path), mode="rb", iter_by=4)

    assert next(chunks) == b"abcd"
    assert next(chunks) == b"ef"

    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-24 04:07:44.126487
# Unit test for function burp

# Generated at 2026-10-24 04:07:45.444294
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:07:54.500783
# Unit test for function burp

# Generated at 2026-10-24 04:07:55.805585
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:08:30.411269
# Unit test for function islurp

# Generated at 2026-10-24 04:08:32.833678
# Unit test for function islurp

# Generated at 2026-10-24 04:08:35.246888
# Unit test for function islurp

# Generated at 2026-10-24 04:08:37.663693
# Unit test for function islurp

# Generated at 2026-10-24 04:08:40.077844
# Unit test for function islurp

# Generated at 2026-10-24 04:08:46.383635
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:09:27.578427
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        text_path = os.path.join(tmpdir, 'input.txt')
        binary_path = os.path.join(tmpdir, 'input.bin')

        with open(text_path, 'w') as fh:
            fh.write('first line\nsecond line\n')

        # Default line-by-line iteration
        assert list(module_0.islurp(text_path)) == [
            'first line\n',
            'second line\n',
        ]

        # Explicit line mode
        assert list(module_0.islurp(text_path, iter_by='LINEMODE')) == [
            'first line\n',
            'second line\n',
        ]

        # Fixed-size chunks
        assert list(module_0.islurp(text_path, iter_by=5)) == [
            'first',
            ' line',
            '\nseco',
            'nd li',
            'ne\n',
        ]

        # stdin support
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('stdin line 1\nstdin line 2\n')
            assert list(module_0.islurp('-')) == [
                'stdin line 1\n',
                'stdin line 2\n',
            ]
        finally:
            sys.stdin = original_stdin

        # Binary input and binary EOF
        with open(binary_path, 'wb') as fh:
            fh.write(b'abcde')

        reader = module_0.islurp(binary_path, mode='rb', iter_by=2)
        assert next(reader) == b'ab'
        assert next(reader) == b'cd'
        assert next(reader) == b'e'

        try:
            next(reader)
        except StopIteration:
            pass
        else:
            raise AssertionError('Binary reader did not stop at EOF')

# Generated at 2026-10-24 04:09:29.998520
# Unit test for function islurp

# Generated at 2026-10-24 04:09:32.564071
# Unit test for function islurp

# Generated at 2026-10-24 04:09:34.980464
# Unit test for function islurp

# Generated at 2026-10-24 04:09:54.174086
# Unit test for function burp
def test_burp():import io

# Generated at 2026-10-24 04:10:23.565789
# Unit test for function islurp

# Generated at 2026-10-24 04:10:29.399490
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:10:39.397667
# Unit test for function burp

# Generated at 2026-10-24 04:10:40.717531
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:11:08.619826
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    fd, filename = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(contents)

        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Explicit line-mode compatibility.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate in fixed-size chunks.
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 04:11:57.271114
# Unit test for function islurp

# Generated at 2026-10-24 04:12:02.284122
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:12:12.845798
# Unit test for function burp
def test_burp():
    import contextlib
    import io
    import tempfile

    contents = "first line\nsecond line\n"

    # Writes to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

        # Honors the requested file mode.
        module_0.burp(filename, "appended\n", mode="a")

        with open(filename, "r") as fh:
            assert fh.read() == contents + "appended\n"

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-24 04:12:29.211892
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        # Write to a regular file.
        module_0.burp(filename, "hello")
        with open(filename, "r") as fh:
            assert fh.read() == "hello"

        # Honor the requested file mode.
        module_0.burp(filename, " world", mode="a")
        with open(filename, "r") as fh:
            assert fh.read() == "hello world"

        # Expand user and environment-variable paths.
        expanded_filename = os.path.join(tmpdir, "expanded.txt")
        with patch.object(
            os.path, "expanduser", return_value=expanded_filename
        ) as expanduser, patch.object(
            os.path, "expandvars", side_effect=lambda path: path
        ) as expandvars:
            module_0.burp("~/expanded.txt", "expanded")

        expanduser.assert_called_once_with("~/expanded.txt")
        expandvars.assert_called_once_with(expanded_filename)
        with open(expanded_filename, "r") as fh:
            assert fh.read() == "expanded"

        # Skip expansion when explicitly disabled.
        unexpanded_filename = os.path.join(tmpdir, "unexpanded.txt")
        with patch.object(os.path, "expanduser") as expanduser, patch.object(
            os.path, "expandvars"
        ) as expandvars:
            module_0.burp(
                unexpanded_filename,
                "literal",
                expanduser=False,
                expandvars=False,
            )

        expanduser.assert_not_called()
        expandvars.assert_not_called()

        # Write "-" to a file when stdout handling is disabled.
        previous_cwd = os.getcwd()
        try:
            os.chdir(tmpdir)
            module_0.burp("-", "not stdout", allow_stdout=False)
            with open("-", "r") as fh:
                assert fh.read() == "not stdout"
        finally:
            os.chdir(previous_cwd)

    # Write to stdout when filename is "-".
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", "hello stdout")

    assert stdout.getvalue() == "hello stdout"

# Generated at 2026-10-24 04:13:00.750685
# Unit test for function islurp
def test_islurp():import io


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "example.txt"
    path.write_text("first line\nsecond line\n", encoding="utf-8")

    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
    ]

    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\n",
    ]

    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin line\n"))
    assert list(module_0.islurp("-")) == ["stdin line\n"]

# Generated at 2026-10-24 04:13:07.856618
# Unit test for function burp

# Generated at 2026-10-24 04:13:09.269408
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:13:19.487015
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from unittest import mock

    contents = "hello\nworld\n"

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with mock.patch.object(sys, "stdout", stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-24 04:13:22.008237
# Unit test for function burp

# Generated at 2026-10-24 04:13:24.420877
# Unit test for function burp

# Generated at 2026-10-24 04:13:26.846291
# Unit test for function burp

# Generated at 2026-10-24 04:13:29.260853
# Unit test for function burp

# Generated at 2026-10-24 04:13:31.680496
# Unit test for function burp

# Generated at 2026-10-24 04:13:34.099889
# Unit test for function burp

# Generated at 2026-10-24 04:13:36.510481
# Unit test for function islurp

# Generated at 2026-10-24 04:13:38.928304
# Unit test for function islurp

# Generated at 2026-10-24 04:13:41.483653
# Unit test for function islurp

# Generated at 2026-10-24 04:13:43.899959
# Unit test for function islurp

# Generated at 2026-10-24 04:13:46.317596
# Unit test for function islurp

# Generated at 2026-10-24 04:13:48.735104
# Unit test for function islurp

# Generated at 2026-10-24 04:13:51.151433
# Unit test for function islurp

# Generated at 2026-10-24 04:13:53.567660
# Unit test for function islurp

# Generated at 2026-10-24 04:13:55.983680
# Unit test for function islurp

# Generated at 2026-10-24 04:13:58.417033
# Unit test for function islurp

# Generated at 2026-10-24 04:14:00.828945
# Unit test for function islurp

# Generated at 2026-10-24 04:14:03.243935
# Unit test for function islurp

# Generated at 2026-10-24 04:14:05.658855
# Unit test for function burp

# Generated at 2026-10-24 04:14:08.077117
# Unit test for function burp

# Generated at 2026-10-24 04:14:10.494028
# Unit test for function burp