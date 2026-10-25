

# Generated at 2026-10-25 00:19:05.568478
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "hello\nworld\n"

    # Writes text to a file.
    with tempfile.TemporaryDirectory() as directory:
        filename = os.path.join(directory, "output.txt")
        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

        # Supports binary mode.
        binary_filename = os.path.join(directory, "output.bin")
        binary_contents = b"\x00\x01\xff"
        module_0.burp(binary_filename, binary_contents, mode="wb")

        with open(binary_filename, "rb") as fh:
            assert fh.read() == binary_contents

    # Writes to stdout when filename is "-".
    output = io.StringIO()
    with redirect_stdout(output):
        module_0.burp("-", contents)

    assert output.getvalue() == contents

# Generated at 2026-10-25 00:19:19.152075
# Unit test for function islurp

# Generated at 2026-10-25 00:19:20.619894
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

# Generated at 2026-10-25 00:19:37.571410
# Unit test for function islurp

# Generated at 2026-10-25 00:19:38.949640
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

# Generated at 2026-10-25 00:19:48.238930
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "Hello,\nworld!\n"

    # Verify writing to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")
        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Verify writing to stdout when filename is "-".
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-25 00:19:54.412193
# Unit test for function burp

# Generated at 2026-10-25 00:19:59.327360
# Unit test for function burp
def test_burp():import tempfile


# Generated at 2026-10-25 00:20:10.073801
# Unit test for function islurp
def test_islurp():
    import tempfile

    fd, filename = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, 'w') as fh:
            fh.write('first line\nsecond line\nlast line')

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            'first line\n',
            'second line\n',
            'last line',
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=5)) == [
            'first',
            ' line',
            '\nseco',
            'nd li',
            'ne\nla',
            'st li',
            'ne',
        ]

        # String form of the line-mode constant
        assert list(module_0.islurp(filename, iter_by='LINEMODE')) == [
            'first line\n',
            'second line\n',
            'last line',
        ]
    finally:
        os.remove(filename)

# Generated at 2026-10-25 00:20:19.602795
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "hello\nworld\n"

    # Writes text to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")
        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-25 00:20:30.542825
# Unit test for function islurp

# Generated at 2026-10-25 00:20:31.871580
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

# Generated at 2026-10-25 00:20:49.197146
# Unit test for function islurp
def test_islurp():import io


def test_islurp(tmp_path, monkeypatch):
    input_file = tmp_path / "input.txt"
    input_file.write_text("alpha\nbeta\n", encoding="utf-8")

    # Default: iterate by line.
    assert list(module_0.islurp(str(input_file))) == [
        "alpha\n",
        "beta\n",
    ]

    # Explicit and symbolic line modes.
    assert list(module_0.islurp(str(input_file), iter_by=LINEMODE)) == [
        "alpha\n",
        "beta\n",
    ]
    assert list(module_0.islurp(str(input_file), iter_by="LINEMODE")) == [
        "alpha\n",
        "beta\n",
    ]

    # Iterate in fixed-size chunks.
    assert list(module_0.islurp(str(input_file), iter_by=4)) == [
        "alph",
        "a\nbe",
        "ta\n",
    ]

    # Expand environment variables in the path.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert list(module_0.islurp("$ISLURP_TEST_DIR/input.txt")) == [
        "alpha\n",
        "beta\n",
    ]

    # Read from stdin.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin line\n"))
    assert list(module_0.islurp("-")) == ["stdin line\n"]

    # Binary mode.
    binary_file = tmp_path / "input.bin"
    binary_file.write_bytes(b"abcde")
    assert list(module_0.islurp(str(binary_file), mode="rb", iter_by=2)) == [
        b"ab",
        b"cd",
        b"e",
    ]

# Generated at 2026-10-25 00:20:57.904121
# Unit test for function burp
def test_burp():
    import io

# Generated at 2026-10-25 00:21:07.100728
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    fd, filename = tempfile.mkstemp()
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(contents)

        # Default: iterate by line.
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Explicit line mode.
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

# Generated at 2026-10-25 00:21:09.636816
# Unit test for function islurp

# Generated at 2026-10-25 00:21:12.050851
# Unit test for function islurp

# Generated at 2026-10-25 00:21:14.467876
# Unit test for function islurp

# Generated at 2026-10-25 00:21:16.886285
# Unit test for function islurp

# Generated at 2026-10-25 00:21:19.302641
# Unit test for function islurp

# Generated at 2026-10-25 00:21:21.727302
# Unit test for function islurp

# Generated at 2026-10-25 00:21:24.141926
# Unit test for function islurp

# Generated at 2026-10-25 00:21:26.557408
# Unit test for function islurp

# Generated at 2026-10-25 00:21:28.973124
# Unit test for function islurp

# Generated at 2026-10-25 00:21:31.390392
# Unit test for function islurp

# Generated at 2026-10-25 00:21:33.803459
# Unit test for function islurp

# Generated at 2026-10-25 00:21:36.217586
# Unit test for function islurp

# Generated at 2026-10-25 00:21:48.512801
# Unit test for function islurp
def test_islurp():import tempfile


# Generated at 2026-10-25 00:22:05.479254
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\n"

    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
        ]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=5)) == [
            "first",
            " line",
            "\nseco",
            "nd li",
            "ne\n",
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-25 00:22:08.010756
# Unit test for function islurp

# Generated at 2026-10-25 00:22:10.544802
# Unit test for function islurp

# Generated at 2026-10-25 00:22:12.961357
# Unit test for function islurp

# Generated at 2026-10-25 00:22:15.373861
# Unit test for function burp

# Generated at 2026-10-25 00:22:17.787955
# Unit test for function burp

# Generated at 2026-10-25 00:22:20.203690
# Unit test for function burp

# Generated at 2026-10-25 00:22:22.619763
# Unit test for function islurp

# Generated at 2026-10-25 00:22:25.033851
# Unit test for function islurp

# Generated at 2026-10-25 00:22:27.448153
# Unit test for function islurp

# Generated at 2026-10-25 00:22:30.047805
# Unit test for function burp

# Generated at 2026-10-25 00:22:32.464957
# Unit test for function burp

# Generated at 2026-10-25 00:22:34.881820
# Unit test for function burp

# Generated at 2026-10-25 00:22:37.297293
# Unit test for function burp

# Generated at 2026-10-25 00:22:39.712209
# Unit test for function burp

# Generated at 2026-10-25 00:22:42.138636
# Unit test for function burp

# Generated at 2026-10-25 00:22:44.579976
# Unit test for function islurp

# Generated at 2026-10-25 00:22:47.008003
# Unit test for function islurp

# Generated at 2026-10-25 00:22:49.422757
# Unit test for function islurp

# Generated at 2026-10-25 00:22:51.850445
# Unit test for function islurp

# Generated at 2026-10-25 00:22:54.292489
# Unit test for function islurp

# Generated at 2026-10-25 00:22:56.711387
# Unit test for function islurp

# Generated at 2026-10-25 00:22:59.125215
# Unit test for function islurp

# Generated at 2026-10-25 00:23:01.540811
# Unit test for function islurp

# Generated at 2026-10-25 00:23:03.956791
# Unit test for function islurp

# Generated at 2026-10-25 00:23:06.370972
# Unit test for function islurp

# Generated at 2026-10-25 00:23:08.796322
# Unit test for function islurp

# Generated at 2026-10-25 00:23:11.210765
# Unit test for function islurp

# Generated at 2026-10-25 00:23:13.627847
# Unit test for function burp

# Generated at 2026-10-25 00:23:16.043172
# Unit test for function burp

# Generated at 2026-10-25 00:23:18.457686
# Unit test for function burp

# Generated at 2026-10-25 00:23:20.872221
# Unit test for function burp

# Generated at 2026-10-25 00:23:23.291136
# Unit test for function burp

# Generated at 2026-10-25 00:23:25.710254
# Unit test for function burp

# Generated at 2026-10-25 00:23:28.126632
# Unit test for function islurp

# Generated at 2026-10-25 00:23:30.541899
# Unit test for function islurp

# Generated at 2026-10-25 00:23:32.956571
# Unit test for function islurp

# Generated at 2026-10-25 00:23:50.753844
# Unit test for function islurp

# Generated at 2026-10-25 00:23:52.076813
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

# Generated at 2026-10-25 00:23:59.149830
# Unit test for function burp

# Generated at 2026-10-25 00:24:03.860519
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-25 00:24:06.278102
# Unit test for function islurp

# Generated at 2026-10-25 00:24:08.816641
# Unit test for function islurp

# Generated at 2026-10-25 00:24:11.240353
# Unit test for function islurp

# Generated at 2026-10-25 00:24:13.653818
# Unit test for function islurp

# Generated at 2026-10-25 00:24:16.069410
# Unit test for function islurp

# Generated at 2026-10-25 00:24:18.484396
# Unit test for function islurp

# Generated at 2026-10-25 00:24:20.899686
# Unit test for function islurp

# Generated at 2026-10-25 00:24:23.313964
# Unit test for function islurp

# Generated at 2026-10-25 00:24:25.729367
# Unit test for function islurp

# Generated at 2026-10-25 00:24:28.144460
# Unit test for function burp

# Generated at 2026-10-25 00:24:30.561922
# Unit test for function burp

# Generated at 2026-10-25 00:24:32.975806
# Unit test for function burp

# Generated at 2026-10-25 00:24:35.395837
# Unit test for function islurp

# Generated at 2026-10-25 00:24:37.816206
# Unit test for function islurp

# Generated at 2026-10-25 00:24:40.236030
# Unit test for function islurp

# Generated at 2026-10-25 00:24:42.657824
# Unit test for function islurp

# Generated at 2026-10-25 00:24:45.073913
# Unit test for function islurp

# Generated at 2026-10-25 00:24:47.488062
# Unit test for function islurp

# Generated at 2026-10-25 00:24:49.914263
# Unit test for function islurp

# Generated at 2026-10-25 00:24:52.323793
# Unit test for function islurp

# Generated at 2026-10-25 00:24:54.770831
# Unit test for function islurp

# Generated at 2026-10-25 00:24:57.208525
# Unit test for function burp

# Generated at 2026-10-25 00:24:59.649300
# Unit test for function burp

# Generated at 2026-10-25 00:25:02.091593
# Unit test for function burp

# Generated at 2026-10-25 00:25:04.520221
# Unit test for function burp

# Generated at 2026-10-25 00:25:06.936285
# Unit test for function burp

# Generated at 2026-10-25 00:25:09.350653
# Unit test for function burp

# Generated at 2026-10-25 00:25:11.769099
# Unit test for function islurp

# Generated at 2026-10-25 00:25:14.184142
# Unit test for function islurp

# Generated at 2026-10-25 00:25:16.613553
# Unit test for function islurp

# Generated at 2026-10-25 00:25:19.020723
# Unit test for function burp

# Generated at 2026-10-25 00:25:27.317838
# Unit test for function burp
def test_burp():import io
import os
import sys
import tempfile

    # Round-trip write/read to a real file

# Generated at 2026-10-25 00:25:34.356067
# Unit test for function burp

# Generated at 2026-10-25 00:25:39.744678
# Unit test for function burp
def test_burp():import tempfile


# Generated at 2026-10-25 00:25:50.868119
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from unittest.mock import patch

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        module_0.burp(filename, "hello")
        with open(filename, "r") as fh:
            assert fh.read() == "hello"

        # Honors the requested file mode.
        module_0.burp(filename, " world", mode="a")
        with open(filename, "r") as fh:
            assert fh.read() == "hello world"

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with patch.object(sys, "stdout", stdout):
        module_0.burp("-", "console output")

    assert stdout.getvalue() == "console output"

# Generated at 2026-10-25 00:25:53.397314
# Unit test for function islurp

# Generated at 2026-10-25 00:25:55.811991
# Unit test for function islurp

# Generated at 2026-10-25 00:25:58.226599
# Unit test for function islurp

# Generated at 2026-10-25 00:26:00.641778
# Unit test for function islurp

# Generated at 2026-10-25 00:26:03.056619
# Unit test for function islurp

# Generated at 2026-10-25 00:26:05.474838
# Unit test for function islurp

# Generated at 2026-10-25 00:26:07.890924
# Unit test for function burp

# Generated at 2026-10-25 00:26:10.308505
# Unit test for function burp

# Generated at 2026-10-25 00:26:12.721374
# Unit test for function burp

# Generated at 2026-10-25 00:26:15.135957
# Unit test for function islurp

# Generated at 2026-10-25 00:26:17.552007
# Unit test for function islurp

# Generated at 2026-10-25 00:26:19.967903
# Unit test for function islurp

# Generated at 2026-10-25 00:26:22.386092
# Unit test for function burp

# Generated at 2026-10-25 00:26:24.957509
# Unit test for function burp
def test_burp():import io
import os
import sys
import tempfile

    # Round-trip write/read to a real file

# Generated at 2026-10-25 00:26:45.150499
# Unit test for function islurp
def test_islurp():
    import io
    import os
    import sys
    import tempfile

    def assert_exhausted(iterator):
        try:
            next(iterator)
        except StopIteration:
            return
        raise AssertionError("iterator did not stop at EOF")

    with tempfile.TemporaryDirectory() as tmpdir:
        text_path = os.path.join(tmpdir, "example.txt")
        binary_path = os.path.join(tmpdir, "example.bin")

        with open(text_path, "w") as fh:
            fh.write("first\nsecond\nlast")

        with open(binary_path, "wb") as fh:
            fh.write(b"abcdef")

        # Default line-by-line iteration.
        assert list(module_0.islurp(text_path)) == [
            "first\n",
            "second\n",
            "last",
        ]

        # Named line mode.
        assert list(module_0.islurp(text_path, iter_by="LINEMODE")) == [
            "first\n",
            "second\n",
            "last",
        ]

        # Fixed-size text chunks.
        assert list(module_0.islurp(text_path, iter_by=5)) == [
            "first",
            "\nseco",
            "nd\nla",
            "st",
        ]

        # Environment-variable expansion.
        variable = "ISLURP_TEST_FILE"
        previous_value = os.environ.get(variable)
        os.environ[variable] = text_path
        try:
            assert list(module_0.islurp("$" + variable)) == [
                "first\n",
                "second\n",
                "last",
            ]
        finally:
            if previous_value is None:
                os.environ.pop(variable, None)
            else:
                os.environ[variable] = previous_value

        # Binary chunks must terminate on b''.
        iterator = module_0.islurp(binary_path, mode="rb", iter_by=3)
        assert next(iterator) == b"abc"
        assert next(iterator) == b"def"
        assert_exhausted(iterator)

        # Reading from standard input.
        previous_stdin = sys.stdin
        sys.stdin = io.StringIO("stdin line 1\nstdin line 2\n")
        try:
            assert list(module_0.islurp("-")) == [
                "stdin line 1\n",
                "stdin line 2\n",
            ]
        finally:
            sys.stdin = previous_stdin

# Generated at 2026-10-25 00:27:03.168211
# Unit test for function islurp

# Generated at 2026-10-25 00:27:05.599393
# Unit test for function islurp

# Generated at 2026-10-25 00:27:08.014371
# Unit test for function islurp

# Generated at 2026-10-25 00:27:10.429585
# Unit test for function islurp

# Generated at 2026-10-25 00:27:12.844318
# Unit test for function islurp

# Generated at 2026-10-25 00:27:15.258955
# Unit test for function islurp

# Generated at 2026-10-25 00:27:17.674092
# Unit test for function islurp

# Generated at 2026-10-25 00:27:20.091575
# Unit test for function islurp

# Generated at 2026-10-25 00:27:22.506584
# Unit test for function islurp

# Generated at 2026-10-25 00:27:24.921915
# Unit test for function burp

# Generated at 2026-10-25 00:27:27.337565
# Unit test for function burp

# Generated at 2026-10-25 00:27:29.752480
# Unit test for function burp

# Generated at 2026-10-25 00:27:32.174067
# Unit test for function burp

# Generated at 2026-10-25 00:27:34.586387
# Unit test for function burp

# Generated at 2026-10-25 00:27:37.001128
# Unit test for function burp

# Generated at 2026-10-25 00:27:39.418875
# Unit test for function islurp

# Generated at 2026-10-25 00:27:41.829613
# Unit test for function islurp

# Generated at 2026-10-25 00:27:44.243755
# Unit test for function islurp

# Generated at 2026-10-25 00:27:46.656962
# Unit test for function burp

# Generated at 2026-10-25 00:27:49.070192
# Unit test for function burp

# Generated at 2026-10-25 00:27:51.485149
# Unit test for function burp

# Generated at 2026-10-25 00:27:53.898269
# Unit test for function burp

# Generated at 2026-10-25 00:27:58.259094
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-25 00:28:11.979135
# Unit test for function islurp

# Generated at 2026-10-25 00:28:13.302205
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

# Generated at 2026-10-25 00:28:23.499342
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

        # Fixed-size chunks
        assert "".join(module_0.islurp(filename, iter_by=4)) == contents

        # Alias
        assert "".join(slurp(filename)) == contents
    finally:
        os.unlink(filename)

# Generated at 2026-10-25 00:28:31.297179
# Unit test for function burp

# Generated at 2026-10-25 00:28:36.454603
# Unit test for function burp
def test_burp():import tempfile


# Generated at 2026-10-25 00:28:38.870014
# Unit test for function islurp

# Generated at 2026-10-25 00:28:41.285031
# Unit test for function islurp

# Generated at 2026-10-25 00:28:43.701333
# Unit test for function islurp

# Generated at 2026-10-25 00:28:46.115246
# Unit test for function islurp

# Generated at 2026-10-25 00:28:48.533763
# Unit test for function islurp

# Generated at 2026-10-25 00:28:50.946199
# Unit test for function islurp

# Generated at 2026-10-25 00:28:53.361002
# Unit test for function burp

# Generated at 2026-10-25 00:28:55.776962
# Unit test for function burp

# Generated at 2026-10-25 00:28:58.192193
# Unit test for function burp