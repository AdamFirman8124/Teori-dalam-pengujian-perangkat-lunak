

# Generated at 2026-10-24 21:52:38.689475
# Unit test for function islurp
def test_islurp():fh_next = (
            fh.readline
            if iter_by == LINEMODE
            else functools.partial(fh.read, iter_by)
        )


# Generated at 2026-10-24 21:52:41.109956
# Unit test for function islurp

# Generated at 2026-10-24 21:52:43.531687
# Unit test for function islurp

# Generated at 2026-10-24 21:52:45.951804
# Unit test for function burp

# Generated at 2026-10-24 21:52:48.371556
# Unit test for function burp

# Generated at 2026-10-24 21:52:50.788757
# Unit test for function burp

# Generated at 2026-10-24 21:52:53.208168
# Unit test for function burp

# Generated at 2026-10-24 21:52:55.629354
# Unit test for function burp

# Generated at 2026-10-24 21:52:58.044275
# Unit test for function burp

# Generated at 2026-10-24 21:53:00.461809
# Unit test for function burp

# Generated at 2026-10-24 21:53:02.880537
# Unit test for function burp

# Generated at 2026-10-24 21:53:05.297870
# Unit test for function burp

# Generated at 2026-10-24 21:53:07.721257
# Unit test for function burp

# Generated at 2026-10-24 21:53:10.136331
# Unit test for function burp

# Generated at 2026-10-24 21:53:12.555452
# Unit test for function burp

# Generated at 2026-10-24 21:53:14.971849
# Unit test for function islurp

# Generated at 2026-10-24 21:53:17.390090
# Unit test for function islurp

# Generated at 2026-10-24 21:53:19.811009
# Unit test for function islurp

# Generated at 2026-10-24 21:53:22.226413
# Unit test for function islurp

# Generated at 2026-10-24 21:53:24.644716
# Unit test for function islurp

# Generated at 2026-10-24 21:53:27.059669
# Unit test for function islurp

# Generated at 2026-10-24 21:53:29.478758
# Unit test for function burp

# Generated at 2026-10-24 21:53:31.897951
# Unit test for function burp

# Generated at 2026-10-24 21:53:34.315122
# Unit test for function burp

# Generated at 2026-10-24 21:53:36.732456
# Unit test for function burp

# Generated at 2026-10-24 21:53:39.150270
# Unit test for function burp

# Generated at 2026-10-24 21:53:41.568727
# Unit test for function burp

# Generated at 2026-10-24 21:53:43.986226
# Unit test for function islurp

# Generated at 2026-10-24 21:53:46.403160
# Unit test for function islurp

# Generated at 2026-10-24 21:53:48.819091
# Unit test for function islurp

# Generated at 2026-10-24 21:53:51.237632
# Unit test for function burp

# Generated at 2026-10-24 21:53:53.653216
# Unit test for function burp

# Generated at 2026-10-24 21:53:56.072330
# Unit test for function burp

# Generated at 2026-10-24 21:53:58.491057
# Unit test for function islurp

# Generated at 2026-10-24 21:54:00.906035
# Unit test for function islurp

# Generated at 2026-10-24 21:54:03.323075
# Unit test for function islurp

# Generated at 2026-10-24 21:54:05.742623
# Unit test for function islurp

# Generated at 2026-10-24 21:54:08.158098
# Unit test for function islurp

# Generated at 2026-10-24 21:54:10.578815
# Unit test for function islurp

# Generated at 2026-10-24 21:54:12.993950
# Unit test for function islurp

# Generated at 2026-10-24 21:54:15.412904
# Unit test for function islurp

# Generated at 2026-10-24 21:54:17.831739
# Unit test for function islurp

# Generated at 2026-10-24 21:54:20.248234
# Unit test for function islurp

# Generated at 2026-10-24 21:54:22.664245
# Unit test for function islurp

# Generated at 2026-10-24 21:54:25.078878
# Unit test for function islurp

# Generated at 2026-10-24 21:54:27.496354
# Unit test for function islurp

# Generated at 2026-10-24 21:54:29.915167
# Unit test for function islurp

# Generated at 2026-10-24 21:54:32.333311
# Unit test for function islurp

# Generated at 2026-10-24 21:54:34.750197
# Unit test for function burp

# Generated at 2026-10-24 21:54:37.172467
# Unit test for function burp

# Generated at 2026-10-24 21:54:39.592269
# Unit test for function burp

# Generated at 2026-10-24 21:54:42.007646
# Unit test for function burp

# Generated at 2026-10-24 21:54:44.423649
# Unit test for function burp

# Generated at 2026-10-24 21:54:46.842931
# Unit test for function burp

# Generated at 2026-10-24 21:54:49.257651
# Unit test for function islurp

# Generated at 2026-10-24 21:54:51.675200
# Unit test for function islurp

# Generated at 2026-10-24 21:54:54.097296
# Unit test for function islurp

# Generated at 2026-10-24 21:55:10.742084
# Unit test for function islurp

# Generated at 2026-10-24 21:55:12.071148
# Unit test for function islurp
def test_islurp():import os
import tempfile

fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as fh:
        fh.write("line1\nline2\nline3\n")

    # Read by line (default LINEMODE)
    lines = list(module_0.islurp(path))
    assert lines == ["line1\n", "line2\n", "line3\n"], lines

    # Read in fixed-size chunks of 6 bytes
    chunks = list(module_0.islurp(path, iter_by=6))
    assert chunks == ["line1\n", "line2\n", "line3\n"], chunks

    # Read in chunks of 4 bytes
    chunks4 = list(module_0.islurp(path, mode='r', iter_by=4))
    assert chunks4 == ["line", "1\nli", "ne2\n", "line", "3\n"], chunks4

    # Binary mode
    chunks_bin = list(module_0.islurp(path, mode='rb', iter_by=5))
    assert chunks_bin == [b"line1", b"\nline", b"2\nlin", b"e3\n"], chunks_bin

    # expanduser=False prevents ~ expansion (path with literal tilde won't open,
    # so verify expansion logic via a temp dir under HOME)
    home = os.path.expanduser("~")
    tilde_path = os.path.join(home, ".islurp_test_tmp.txt")
    try:
        with open(tilde_path, "w") as fh:
            fh.write("tilde\n")
        assert list(module_0.islurp("~/.islurp_test_tmp.txt")) == ["tilde\n"]
        assert list(module_0.islurp("~/.islurp_test_tmp.txt", expandvars=False)) == ["tilde\n"]
    finally:
        if os.path.exists(tilde_path):
            os.remove(tilde_path)

    # stdin via '-' filename
    import io
    real_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("from_stdin\n")
        assert list(module_0.islurp("-")) == ["from_stdin\n"]
    finally:
        sys.stdin = real_stdin
finally:
    if os.path.exists(path):
        os.remove(path)

# Generated at 2026-10-24 21:55:24.028484
# Unit test for function islurp

# Generated at 2026-10-24 21:55:25.500697
# Unit test for function islurp
def test_islurp():import os
import tempfile

fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as fh:
        fh.write("line1\nline2\nline3\n")

    # Read by line (default LINEMODE)
    lines = list(module_0.islurp(path))
    assert lines == ["line1\n", "line2\n", "line3\n"], lines

    # Read in fixed-size chunks of 6 bytes
    chunks = list(module_0.islurp(path, iter_by=6))
    assert chunks == ["line1\n", "line2\n", "line3\n"], chunks

    # Read in chunks of 4 bytes
    chunks4 = list(module_0.islurp(path, mode='r', iter_by=4))
    assert chunks4 == ["line", "1\nli", "ne2\n", "line", "3\n"], chunks4

    # Binary mode
    chunks_bin = list(module_0.islurp(path, mode='rb', iter_by=5))
    assert chunks_bin == [b"line1", b"\nline", b"2\nlin", b"e3\n"], chunks_bin

    # expanduser=False prevents ~ expansion (path with literal tilde won't open,
    # so verify expansion logic via a temp dir under HOME)
    home = os.path.expanduser("~")
    tilde_path = os.path.join(home, ".islurp_test_tmp.txt")
    try:
        with open(tilde_path, "w") as fh:
            fh.write("tilde\n")
        assert list(module_0.islurp("~/.islurp_test_tmp.txt")) == ["tilde\n"]
        assert list(module_0.islurp("~/.islurp_test_tmp.txt", expandvars=False)) == ["tilde\n"]
    finally:
        if os.path.exists(tilde_path):
            os.remove(tilde_path)

    # stdin via '-' filename
    import io
    real_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("from_stdin\n")
        assert list(module_0.islurp("-")) == ["from_stdin\n"]
    finally:
        sys.stdin = real_stdin
finally:
    if os.path.exists(path):
        os.remove(path)

# Generated at 2026-10-24 21:55:35.843861
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"
    fd, filename = tempfile.mkstemp(text=True)
    os.close(fd)

    try:
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate in fixed-size chunks.
        chunks = list(module_0.islurp(filename, iter_by=5))
        assert "".join(chunks) == contents
        assert all(len(chunk) <= 5 for chunk in chunks)

        # The string compatibility value also selects line mode.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]
    finally:
        os.remove(filename)

# Generated at 2026-10-24 21:55:38.267637
# Unit test for function islurp

# Generated at 2026-10-24 21:55:40.689761
# Unit test for function islurp

# Generated at 2026-10-24 21:55:43.108222
# Unit test for function islurp

# Generated at 2026-10-24 21:55:45.527273
# Unit test for function burp

# Generated at 2026-10-24 21:55:48.115520
# Unit test for function burp

# Generated at 2026-10-24 21:55:50.532378
# Unit test for function burp

# Generated at 2026-10-24 21:55:52.947836
# Unit test for function burp

# Generated at 2026-10-24 21:55:55.365925
# Unit test for function burp

# Generated at 2026-10-24 21:55:57.788351
# Unit test for function burp

# Generated at 2026-10-24 21:56:00.203988
# Unit test for function burp

# Generated at 2026-10-24 21:56:02.620304
# Unit test for function burp

# Generated at 2026-10-24 21:56:05.474578
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 21:56:13.424848
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "hello\nworld\n"

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")
        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writes to stdout when filename is "-".
    output = io.StringIO()
    with redirect_stdout(output):
        module_0.burp("-", contents)

    assert output.getvalue() == contents

# Generated at 2026-10-24 21:56:26.837382
# Unit test for function islurp

# Generated at 2026-10-24 21:56:28.270076
# Unit test for function islurp
def test_islurp():import os
import tempfile

fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as fh:
        fh.write("line1\nline2\nline3\n")

    # Read by line (default LINEMODE)
    lines = list(module_0.islurp(path))
    assert lines == ["line1\n", "line2\n", "line3\n"], lines

    # Read in fixed-size chunks of 6 bytes
    chunks = list(module_0.islurp(path, iter_by=6))
    assert chunks == ["line1\n", "line2\n", "line3\n"], chunks

    # Read in chunks of 4 bytes
    chunks4 = list(module_0.islurp(path, mode='r', iter_by=4))
    assert chunks4 == ["line", "1\nli", "ne2\n", "line", "3\n"], chunks4

    # Binary mode
    chunks_bin = list(module_0.islurp(path, mode='rb', iter_by=5))
    assert chunks_bin == [b"line1", b"\nline", b"2\nlin", b"e3\n"], chunks_bin

    # expanduser=False prevents ~ expansion (path with literal tilde won't open,
    # so verify expansion logic via a temp dir under HOME)
    home = os.path.expanduser("~")
    tilde_path = os.path.join(home, ".islurp_test_tmp.txt")
    try:
        with open(tilde_path, "w") as fh:
            fh.write("tilde\n")
        assert list(module_0.islurp("~/.islurp_test_tmp.txt")) == ["tilde\n"]
        assert list(module_0.islurp("~/.islurp_test_tmp.txt", expandvars=False)) == ["tilde\n"]
    finally:
        if os.path.exists(tilde_path):
            os.remove(tilde_path)

    # stdin via '-' filename
    import io
    real_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("from_stdin\n")
        assert list(module_0.islurp("-")) == ["from_stdin\n"]
    finally:
        sys.stdin = real_stdin
finally:
    if os.path.exists(path):
        os.remove(path)

# Generated at 2026-10-24 21:56:46.911594
# Unit test for function islurp
def test_islurp():import io
import sys
import pytest


def test_islurp(tmp_path, monkeypatch):
    text_file = tmp_path / "example.txt"
    text_file.write_text("first line\nsecond line\n", encoding="utf-8")

    # Default line-by-line iteration.
    assert list(module_0.islurp(str(text_file))) == [
        "first line\n",
        "second line\n",
    ]

    # Explicit line mode.
    assert list(module_0.islurp(str(text_file), iter_by="LINEMODE")) == [
        "first line\n",
        "second line\n",
    ]

    # Fixed-size text chunks.
    assert list(module_0.islurp(str(text_file), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\n",
    ]

    # Environment-variable expansion.
    monkeypatch.setenv("ISLURP_TEST_FILE", str(text_file))
    assert "".join(module_0.islurp("$ISLURP_TEST_FILE")) == (
        "first line\nsecond line\n"
    )

    # Standard input.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin line\n"))
    assert list(module_0.islurp("-")) == ["stdin line\n"]

    # Binary chunks.
    binary_file = tmp_path / "example.bin"
    binary_file.write_bytes(b"\x00\x01\x02\x03\x04")

    chunks = iter(module_0.islurp(str(binary_file), mode="rb", iter_by=2))
    assert next(chunks) == b"\x00\x01"
    assert next(chunks) == b"\x02\x03"
    assert next(chunks) == b"\x04"
    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-24 21:56:49.429451
# Unit test for function burp

# Generated at 2026-10-24 21:56:51.845168
# Unit test for function burp

# Generated at 2026-10-24 21:56:54.262420
# Unit test for function burp

# Generated at 2026-10-24 21:56:56.679573
# Unit test for function islurp

# Generated at 2026-10-24 21:56:59.093947
# Unit test for function islurp

# Generated at 2026-10-24 21:57:01.511241
# Unit test for function islurp

# Generated at 2026-10-24 21:57:03.928077
# Unit test for function islurp

# Generated at 2026-10-24 21:57:06.345432
# Unit test for function islurp

# Generated at 2026-10-24 21:57:08.760247
# Unit test for function islurp

# Generated at 2026-10-24 21:57:35.754730
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile

    contents = "alpha\nbeta\nlast"

    with tempfile.TemporaryDirectory() as dirname:
        filename = os.path.join(dirname, "input.txt")
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default line-by-line iteration.
        assert list(module_0.islurp(filename)) == [
            "alpha\n",
            "beta\n",
            "last",
        ]

        # Fixed-size text chunks.
        assert list(module_0.islurp(filename, iter_by=4)) == [
            "alph",
            "a\nbe",
            "ta\nl",
            "ast",
        ]

        # Binary mode and correct termination at b''.
        chunks = module_0.islurp(filename, mode="rb", iter_by=4)
        assert next(chunks) == b"alph"
        assert next(chunks) == b"a\nbe"
        assert next(chunks) == b"ta\nl"
        assert next(chunks) == b"ast"

        try:
            extra = next(chunks)
        except StopIteration:
            pass
        else:
            chunks.close()
            raise AssertionError(
                "Binary iteration did not stop at EOF; got {!r}".format(extra)
            )

        # Environment-variable expansion.
        variable = "ISLURP_TEST_FILE"
        previous = os.environ.get(variable)
        os.environ[variable] = filename
        try:
            assert list(module_0.islurp("$" + variable)) == [
                "alpha\n",
                "beta\n",
                "last",
            ]
        finally:
            if previous is None:
                os.environ.pop(variable, None)
            else:
                os.environ[variable] = previous

    # Reading from stdin, without closing stdin.
    previous_stdin = sys.stdin
    fake_stdin = io.StringIO("first\nsecond\n")
    sys.stdin = fake_stdin
    try:
        assert list(module_0.islurp("-")) == ["first\n", "second\n"]
    finally:
        sys.stdin = previous_stdin

    assert not fake_stdin.closed

# Generated at 2026-10-24 21:57:46.160486
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "hello\nworld\n"

    # Writing to a file
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writing to stdout
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-24 21:57:57.359630
# Unit test for function islurp

# Generated at 2026-10-24 21:57:59.782993
# Unit test for function islurp

# Generated at 2026-10-24 21:58:02.202502
# Unit test for function islurp

# Generated at 2026-10-24 21:58:04.732566
# Unit test for function islurp

# Generated at 2026-10-24 21:58:07.150661
# Unit test for function islurp

# Generated at 2026-10-24 21:58:09.570799
# Unit test for function islurp

# Generated at 2026-10-24 21:58:11.989261
# Unit test for function islurp

# Generated at 2026-10-24 21:58:14.406154
# Unit test for function islurp

# Generated at 2026-10-24 21:58:16.822424
# Unit test for function islurp

# Generated at 2026-10-24 21:58:19.241265
# Unit test for function islurp

# Generated at 2026-10-24 21:58:21.656997
# Unit test for function islurp

# Generated at 2026-10-24 21:58:24.075286
# Unit test for function islurp

# Generated at 2026-10-24 21:58:37.771088
# Unit test for function islurp
def test_islurp():import io
import os
import pytest


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "input.txt"
    path.write_text("first line\nsecond line\n", encoding="utf-8")

    # Default line-by-line iteration.
    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
    ]

    # Explicit LINEMODE compatibility.
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "first line\n",
        "second line\n",
    ]

    # Fixed-size text chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\n",
    ]

    # Environment-variable expansion.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert "".join(module_0.islurp("$ISLURP_TEST_DIR/input.txt")) == (
        "first line\nsecond line\n"
    )

    # Standard input.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin data\n"))
    assert list(module_0.islurp("-")) == ["stdin data\n"]

    # Binary reads must stop at b'' rather than yielding forever.
    binary_path = tmp_path / "input.bin"
    binary_path.write_bytes(b"abcde")

    chunks = module_0.islurp(str(binary_path), mode="rb", iter_by=2)
    assert next(chunks) == b"ab"
    assert next(chunks) == b"cd"
    assert next(chunks) == b"e"
    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-24 21:58:45.085946
# Unit test for function burp

# Generated at 2026-10-24 21:58:49.582017
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 21:59:01.565201
# Unit test for function islurp

# Generated at 2026-10-24 21:59:04.094456
# Unit test for function islurp

# Generated at 2026-10-24 21:59:06.615456
# Unit test for function islurp

# Generated at 2026-10-24 21:59:09.031652
# Unit test for function burp

# Generated at 2026-10-24 21:59:11.450205
# Unit test for function burp

# Generated at 2026-10-24 21:59:13.866992
# Unit test for function burp

# Generated at 2026-10-24 21:59:16.381842
# Unit test for function burp

# Generated at 2026-10-24 21:59:18.798864
# Unit test for function burp

# Generated at 2026-10-24 21:59:21.217037
# Unit test for function burp

# Generated at 2026-10-24 21:59:23.633780
# Unit test for function islurp

# Generated at 2026-10-24 21:59:26.051171
# Unit test for function islurp

# Generated at 2026-10-24 21:59:28.471167
# Unit test for function islurp

# Generated at 2026-10-24 21:59:30.889276
# Unit test for function burp

# Generated at 2026-10-24 21:59:35.765945
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 21:59:45.802222
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        filename = fh.name
        fh.write(contents)

    try:
        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Fixed-size chunk iteration
        chunk_size = 5
        assert list(module_0.islurp(filename, iter_by=chunk_size)) == [
            contents[i:i + chunk_size]
            for i in range(0, len(contents), chunk_size)
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 22:00:08.851725
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.TemporaryDirectory() as directory:
        filename = os.path.join(directory, "sample.txt")

        with open(filename, "w") as fh:
            fh.write(contents)

        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Explicit line-mode alias.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate in fixed-size chunks.
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Empty files yield no values.
        empty_filename = os.path.join(directory, "empty.txt")
        with open(empty_filename, "w"):
            pass

        assert list(module_0.islurp(empty_filename)) == []

# Generated at 2026-10-24 22:00:26.468393
# Unit test for function islurp
def test_islurp():import io
import pytest


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "example.txt"
    path.write_text("alpha\nbeta\ngamma")

    # Default line-by-line iteration.
    assert list(module_0.islurp(str(path))) == [
        "alpha\n",
        "beta\n",
        "gamma",
    ]

    # Explicit line mode.
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "alpha\n",
        "beta\n",
        "gamma",
    ]

    # Fixed-size text chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "alpha",
        "\nbeta",
        "\ngamm",
        "a",
    ]

    # Environment-variable expansion.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert "".join(module_0.islurp("$ISLURP_TEST_DIR/example.txt")) == "alpha\nbeta\ngamma"

    # Standard input.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin data\n"))
    assert list(module_0.islurp("-")) == ["stdin data\n"]

    # Binary input must stop at b''.
    binary_path = tmp_path / "example.bin"
    binary_path.write_bytes(b"abcdef")

    chunks = module_0.islurp(str(binary_path), mode="rb", iter_by=4)
    assert next(chunks) == b"abcd"
    assert next(chunks) == b"ef"
    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-24 22:00:38.844694
# Unit test for function islurp
def test_islurp():import io


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "sample.txt"
    path.write_text("first\nsecond\nlast", encoding="utf-8")

    # Default: iterate by line.
    assert list(module_0.islurp(str(path))) == [
        "first\n",
        "second\n",
        "last",
    ]

    # Iterate by fixed-size chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        "\nseco",
        "nd\nla",
        "st",
    ]

    # The string LINEMODE alias is accepted.
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "first\n",
        "second\n",
        "last",
    ]

    # Environment variables in paths are expanded.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert "".join(module_0.islurp("$ISLURP_TEST_DIR/sample.txt")) == (
        "first\nsecond\nlast"
    )

    # "-" reads from stdin when enabled.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin\ncontent"))
    assert list(module_0.islurp("-")) == ["stdin\n", "content"]

# Generated at 2026-10-24 22:00:49.817484
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "Hello, world!\nSecond line.\n"

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

        # Honors the requested file mode.
        module_0.burp(filename, "Appended.\n", mode="a")

        with open(filename, "r") as fh:
            assert fh.read() == contents + "Appended.\n"

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-24 22:01:06.902969
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        fh.write(contents)
        filename = fh.name

    try:
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]
    finally:
        os.remove(filename)

# Generated at 2026-10-24 22:01:20.074407
# Unit test for function islurp
def test_islurp():import io
import os
import sys


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "sample.txt"
    path.write_text("first line\nsecond line\n", encoding="utf-8")

    # Default line-by-line reading
    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
    ]

    # Explicit line mode
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
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
    expanded_path = os.path.join("$ISLURP_TEST_DIR", "sample.txt")
    assert "".join(module_0.islurp(expanded_path)) == "first line\nsecond line\n"

    # stdin support
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin line\n"))
    assert list(module_0.islurp("-")) == ["stdin line\n"]

    # Binary mode must stop at b''.
    binary_path = tmp_path / "sample.bin"
    binary_path.write_bytes(b"abcdef")

    chunks = module_0.islurp(str(binary_path), mode="rb", iter_by=3)
    assert next(chunks) == b"abc"
    assert next(chunks) == b"def"

    try:
        next(chunks)
    except StopIteration:
        pass
    else:
        raise AssertionError("Binary iteration did not stop at EOF")

# Generated at 2026-10-24 22:01:22.645278
# Unit test for function islurp

# Generated at 2026-10-24 22:01:25.065630
# Unit test for function islurp

# Generated at 2026-10-24 22:01:27.680504
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 22:01:39.161032
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"
    expected_lines = [
        "first line\n",
        "second line\n",
        "last line",
    ]

    fd, filename = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(contents)

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == expected_lines

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == expected_lines

        # Fixed-size chunk iteration
        chunks = list(module_0.islurp(filename, iter_by=5))
        assert "".join(chunks) == contents
        assert all(len(chunk) == 5 for chunk in chunks[:-1])
        assert len(chunks[-1]) <= 5
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 22:01:50.254348
# Unit test for function islurp

# Generated at 2026-10-24 22:01:51.574286
# Unit test for function islurp
def test_islurp():import os
import tempfile

fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as fh:
        fh.write("line1\nline2\nline3\n")

    # Read by line (default LINEMODE)
    lines = list(module_0.islurp(path))
    assert lines == ["line1\n", "line2\n", "line3\n"], lines

    # Read in fixed-size chunks of 6 bytes
    chunks = list(module_0.islurp(path, iter_by=6))
    assert chunks == ["line1\n", "line2\n", "line3\n"], chunks

    # Read in chunks of 4 bytes
    chunks4 = list(module_0.islurp(path, mode='r', iter_by=4))
    assert chunks4 == ["line", "1\nli", "ne2\n", "line", "3\n"], chunks4

    # Binary mode
    chunks_bin = list(module_0.islurp(path, mode='rb', iter_by=5))
    assert chunks_bin == [b"line1", b"\nline", b"2\nlin", b"e3\n"], chunks_bin

    # expanduser=False prevents ~ expansion (path with literal tilde won't open,
    # so verify expansion logic via a temp dir under HOME)
    home = os.path.expanduser("~")
    tilde_path = os.path.join(home, ".islurp_test_tmp.txt")
    try:
        with open(tilde_path, "w") as fh:
            fh.write("tilde\n")
        assert list(module_0.islurp("~/.islurp_test_tmp.txt")) == ["tilde\n"]
        assert list(module_0.islurp("~/.islurp_test_tmp.txt", expandvars=False)) == ["tilde\n"]
    finally:
        if os.path.exists(tilde_path):
            os.remove(tilde_path)

    # stdin via '-' filename
    import io
    real_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("from_stdin\n")
        assert list(module_0.islurp("-")) == ["from_stdin\n"]
    finally:
        sys.stdin = real_stdin
finally:
    if os.path.exists(path):
        os.remove(path)

# Generated at 2026-10-24 22:02:03.326185
# Unit test for function islurp

# Generated at 2026-10-24 22:02:04.758340
# Unit test for function islurp
def test_islurp():import os
import tempfile

fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as fh:
        fh.write("line1\nline2\nline3\n")

    # Read by line (default LINEMODE)
    lines = list(module_0.islurp(path))
    assert lines == ["line1\n", "line2\n", "line3\n"], lines

    # Read in fixed-size chunks of 6 bytes
    chunks = list(module_0.islurp(path, iter_by=6))
    assert chunks == ["line1\n", "line2\n", "line3\n"], chunks

    # Read in chunks of 4 bytes
    chunks4 = list(module_0.islurp(path, mode='r', iter_by=4))
    assert chunks4 == ["line", "1\nli", "ne2\n", "line", "3\n"], chunks4

    # Binary mode
    chunks_bin = list(module_0.islurp(path, mode='rb', iter_by=5))
    assert chunks_bin == [b"line1", b"\nline", b"2\nlin", b"e3\n"], chunks_bin

    # expanduser=False prevents ~ expansion (path with literal tilde won't open,
    # so verify expansion logic via a temp dir under HOME)
    home = os.path.expanduser("~")
    tilde_path = os.path.join(home, ".islurp_test_tmp.txt")
    try:
        with open(tilde_path, "w") as fh:
            fh.write("tilde\n")
        assert list(module_0.islurp("~/.islurp_test_tmp.txt")) == ["tilde\n"]
        assert list(module_0.islurp("~/.islurp_test_tmp.txt", expandvars=False)) == ["tilde\n"]
    finally:
        if os.path.exists(tilde_path):
            os.remove(tilde_path)

    # stdin via '-' filename
    import io
    real_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("from_stdin\n")
        assert list(module_0.islurp("-")) == ["from_stdin\n"]
    finally:
        sys.stdin = real_stdin
finally:
    if os.path.exists(path):
        os.remove(path)

# Generated at 2026-10-24 22:02:18.142442
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "test.txt")
        contents = "first line\nsecond line\nlast line"

        with open(filename, "w") as fh:
            fh.write(contents)

        # Read line by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Read fixed-size chunks.
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Accept the documented string form of LINEMODE.
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Expand environment variables in paths.
        with patch.dict(os.environ, {"ISLURP_TEST_DIR": tmpdir}):
            expanded = os.path.join("$ISLURP_TEST_DIR", "test.txt")
            assert "".join(module_0.islurp(expanded)) == contents

        # Binary mode must stop at b''.
        binary_filename = os.path.join(tmpdir, "test.bin")
        with open(binary_filename, "wb") as fh:
            fh.write(b"abcdef")

        binary_iterator = module_0.islurp(binary_filename, mode="rb", iter_by=2)
        assert next(binary_iterator) == b"ab"
        assert next(binary_iterator) == b"cd"
        assert next(binary_iterator) == b"ef"

        try:
            next(binary_iterator)
        except StopIteration:
            pass
        else:
            raise AssertionError("Binary iterator did not stop at EOF")

    # Read from stdin without closing it.
    stdin = io.StringIO("stdin line 1\nstdin line 2\n")
    with patch.object(sys, "stdin", stdin):
        assert list(module_0.islurp("-")) == [
            "stdin line 1\n",
            "stdin line 2\n",
        ]
        assert not stdin.closed

# Generated at 2026-10-24 22:02:20.563925
# Unit test for function burp

# Generated at 2026-10-24 22:02:22.980762
# Unit test for function burp

# Generated at 2026-10-24 22:02:25.506741
# Unit test for function burp