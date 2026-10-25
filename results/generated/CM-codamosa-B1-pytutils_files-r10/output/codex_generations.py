

# Generated at 2026-10-24 20:13:46.544155
# Unit test for function burp

# Generated at 2026-10-24 20:13:48.961537
# Unit test for function burp

# Generated at 2026-10-24 20:13:51.378380
# Unit test for function burp

# Generated at 2026-10-24 20:13:53.797865
# Unit test for function burp

# Generated at 2026-10-24 20:14:00.052629
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 20:14:21.551204
# Unit test for function islurp

# Generated at 2026-10-24 20:14:28.103749
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

# Generated at 2026-10-24 20:14:31.476473
# Unit test for function burp

# Generated at 2026-10-24 20:14:33.897361
# Unit test for function burp

# Generated at 2026-10-24 20:14:36.318992
# Unit test for function burp

# Generated at 2026-10-24 20:14:38.738785
# Unit test for function burp

# Generated at 2026-10-24 20:14:41.153961
# Unit test for function burp

# Generated at 2026-10-24 20:14:43.576965
# Unit test for function burp

# Generated at 2026-10-24 20:14:45.995797
# Unit test for function burp

# Generated at 2026-10-24 20:14:48.413406
# Unit test for function burp

# Generated at 2026-10-24 20:14:50.834566
# Unit test for function burp

# Generated at 2026-10-24 20:14:53.253247
# Unit test for function islurp

# Generated at 2026-10-24 20:14:55.671210
# Unit test for function islurp

# Generated at 2026-10-24 20:14:58.089422
# Unit test for function islurp

# Generated at 2026-10-24 20:15:00.506088
# Unit test for function burp

# Generated at 2026-10-24 20:15:02.921303
# Unit test for function burp

# Generated at 2026-10-24 20:15:05.340371
# Unit test for function burp

# Generated at 2026-10-24 20:15:07.754213
# Unit test for function burp

# Generated at 2026-10-24 20:15:10.169376
# Unit test for function burp

# Generated at 2026-10-24 20:15:12.586403
# Unit test for function burp

# Generated at 2026-10-24 20:15:15.005006
# Unit test for function islurp

# Generated at 2026-10-24 20:15:17.423166
# Unit test for function islurp

# Generated at 2026-10-24 20:15:23.090299
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 20:15:33.333033
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmpdir:
        # Write to a regular file.
        filename = os.path.join(tmpdir, 'output.txt')
        module_0.burp(filename, 'hello')
        with open(filename, 'r') as fh:
            assert fh.read() == 'hello'

        # Respect the requested file mode.
        module_0.burp(filename, ' world', mode='a')
        with open(filename, 'r') as fh:
            assert fh.read() == 'hello world'

        # Expand environment variables in the path.
        with patch.dict(os.environ, {'BURP_TEST_DIR': tmpdir}):
            module_0.burp(os.path.join('$BURP_TEST_DIR', 'expanded.txt'), 'expanded')
        with open(os.path.join(tmpdir, 'expanded.txt'), 'r') as fh:
            assert fh.read() == 'expanded'

        # Write "-" to stdout when allowed.
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            module_0.burp('-', 'console output')
        assert stdout.getvalue() == 'console output'

# Generated at 2026-10-24 20:15:46.121082
# Unit test for function burp
def test_burp():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, 'output.txt')

        module_0.burp(filename, 'hello')
        with open(filename, 'r') as fh:
            assert fh.read() == 'hello'

        module_0.burp(filename, ' world', mode='a')
        with open(filename, 'r') as fh:
            assert fh.read() == 'hello world'

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp('-', 'hello stdout')

    assert stdout.getvalue() == 'hello stdout'

# Generated at 2026-10-24 20:15:47.690187
# Unit test for function islurp

# Generated at 2026-10-24 20:15:49.012048
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

# Generated at 2026-10-24 20:15:50.347122
# Unit test for function islurp

# Generated at 2026-10-24 20:15:52.987284
# Unit test for function islurp

# Generated at 2026-10-24 20:15:55.406535
# Unit test for function islurp

# Generated at 2026-10-24 20:15:57.936024
# Unit test for function islurp

# Generated at 2026-10-24 20:16:00.349054
# Unit test for function islurp

# Generated at 2026-10-24 20:16:02.764370
# Unit test for function islurp

# Generated at 2026-10-24 20:16:05.184628
# Unit test for function burp

# Generated at 2026-10-24 20:16:07.601385
# Unit test for function burp

# Generated at 2026-10-24 20:16:10.020403
# Unit test for function burp

# Generated at 2026-10-24 20:16:12.679417
# Unit test for function islurp

# Generated at 2026-10-24 20:16:15.100380
# Unit test for function islurp

# Generated at 2026-10-24 20:16:17.517612
# Unit test for function islurp

# Generated at 2026-10-24 20:16:19.935906
# Unit test for function islurp

# Generated at 2026-10-24 20:16:22.354448
# Unit test for function islurp

# Generated at 2026-10-24 20:16:24.773549
# Unit test for function islurp

# Generated at 2026-10-24 20:16:27.201389
# Unit test for function islurp

# Generated at 2026-10-24 20:16:29.615190
# Unit test for function islurp

# Generated at 2026-10-24 20:16:32.032506
# Unit test for function islurp

# Generated at 2026-10-24 20:16:34.446695
# Unit test for function islurp

# Generated at 2026-10-24 20:16:36.865859
# Unit test for function islurp

# Generated at 2026-10-24 20:16:39.284936
# Unit test for function islurp

# Generated at 2026-10-24 20:16:41.699203
# Unit test for function islurp

# Generated at 2026-10-24 20:16:44.114237
# Unit test for function islurp

# Generated at 2026-10-24 20:16:46.531710
# Unit test for function islurp

# Generated at 2026-10-24 20:16:48.949575
# Unit test for function burp

# Generated at 2026-10-24 20:16:51.365196
# Unit test for function burp

# Generated at 2026-10-24 20:16:53.783854
# Unit test for function burp

# Generated at 2026-10-24 20:16:56.201483
# Unit test for function islurp

# Generated at 2026-10-24 20:16:58.622079
# Unit test for function islurp

# Generated at 2026-10-24 20:17:01.038511
# Unit test for function islurp

# Generated at 2026-10-24 20:17:03.454491
# Unit test for function islurp

# Generated at 2026-10-24 20:17:05.872838
# Unit test for function islurp

# Generated at 2026-10-24 20:17:08.294078
# Unit test for function islurp

# Generated at 2026-10-24 20:17:10.705218
# Unit test for function islurp

# Generated at 2026-10-24 20:17:13.120636
# Unit test for function islurp

# Generated at 2026-10-24 20:17:15.540377
# Unit test for function islurp

# Generated at 2026-10-24 20:17:17.957668
# Unit test for function islurp

# Generated at 2026-10-24 20:17:20.579617
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 20:17:21.891561
# Unit test for function islurp

# Generated at 2026-10-24 20:17:23.309257
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

# Generated at 2026-10-24 20:17:24.745010
# Unit test for function islurp

# Generated at 2026-10-24 20:17:26.091029
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

# Generated at 2026-10-24 20:17:27.510855
# Unit test for function islurp

# Generated at 2026-10-24 20:17:28.848710
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

# Generated at 2026-10-24 20:17:30.274529
# Unit test for function islurp

# Generated at 2026-10-24 20:17:31.610376
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

# Generated at 2026-10-24 20:17:32.931698
# Unit test for function islurp

# Generated at 2026-10-24 20:17:34.262093
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

# Generated at 2026-10-24 20:17:35.583230
# Unit test for function islurp

# Generated at 2026-10-24 20:17:36.913741
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

# Generated at 2026-10-24 20:17:38.235426
# Unit test for function islurp

# Generated at 2026-10-24 20:17:39.660377
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

# Generated at 2026-10-24 20:17:55.365167
# Unit test for function burp

# Generated at 2026-10-24 20:18:00.890026
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 20:18:09.696362
# Unit test for function burp

# Generated at 2026-10-24 20:18:12.115180
# Unit test for function burp

# Generated at 2026-10-24 20:18:14.534471
# Unit test for function burp

# Generated at 2026-10-24 20:18:16.951266
# Unit test for function islurp

# Generated at 2026-10-24 20:18:19.368884
# Unit test for function islurp

# Generated at 2026-10-24 20:18:21.786462
# Unit test for function islurp

# Generated at 2026-10-24 20:18:24.226216
# Unit test for function burp

# Generated at 2026-10-24 20:18:26.639226
# Unit test for function burp

# Generated at 2026-10-24 20:18:29.210673
# Unit test for function burp

# Generated at 2026-10-24 20:18:31.628562
# Unit test for function islurp

# Generated at 2026-10-24 20:18:34.042433
# Unit test for function islurp

# Generated at 2026-10-24 20:18:36.457561
# Unit test for function islurp

# Generated at 2026-10-24 20:18:38.875062
# Unit test for function islurp

# Generated at 2026-10-24 20:18:41.291285
# Unit test for function islurp

# Generated at 2026-10-24 20:18:43.710600
# Unit test for function islurp

# Generated at 2026-10-24 20:18:46.128369
# Unit test for function islurp

# Generated at 2026-10-24 20:18:48.546112
# Unit test for function islurp

# Generated at 2026-10-24 20:18:50.965569
# Unit test for function islurp

# Generated at 2026-10-24 20:18:53.384843
# Unit test for function burp

# Generated at 2026-10-24 20:18:55.800543
# Unit test for function burp

# Generated at 2026-10-24 20:18:58.216237
# Unit test for function burp

# Generated at 2026-10-24 20:19:00.631330
# Unit test for function islurp

# Generated at 2026-10-24 20:19:03.050869
# Unit test for function islurp

# Generated at 2026-10-24 20:19:05.470364
# Unit test for function islurp

# Generated at 2026-10-24 20:19:07.886910
# Unit test for function islurp

# Generated at 2026-10-24 20:19:10.306903
# Unit test for function islurp

# Generated at 2026-10-24 20:19:12.724570
# Unit test for function islurp

# Generated at 2026-10-24 20:19:15.140182
# Unit test for function islurp

# Generated at 2026-10-24 20:19:17.561011
# Unit test for function islurp

# Generated at 2026-10-24 20:19:19.980866
# Unit test for function islurp

# Generated at 2026-10-24 20:19:22.396316
# Unit test for function islurp

# Generated at 2026-10-24 20:19:24.812756
# Unit test for function islurp

# Generated at 2026-10-24 20:19:27.228965
# Unit test for function islurp

# Generated at 2026-10-24 20:19:29.789512
# Unit test for function islurp

# Generated at 2026-10-24 20:19:32.363064
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 20:19:49.743916
# Unit test for function islurp

# Generated at 2026-10-24 20:19:51.175231
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

# Generated at 2026-10-24 20:20:08.339806
# Unit test for function islurp

# Generated at 2026-10-24 20:20:09.679432
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

# Generated at 2026-10-24 20:20:20.719990
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    fd, filename = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, 'w') as fh:
            fh.write(contents)

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Alias behaves identically
        assert ''.join(slurp(filename)) == contents
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 20:20:23.141217
# Unit test for function islurp

# Generated at 2026-10-24 20:20:25.557783
# Unit test for function islurp

# Generated at 2026-10-24 20:20:27.974099
# Unit test for function islurp

# Generated at 2026-10-24 20:20:30.392237
# Unit test for function islurp

# Generated at 2026-10-24 20:20:32.807550
# Unit test for function islurp

# Generated at 2026-10-24 20:20:35.224304
# Unit test for function islurp

# Generated at 2026-10-24 20:20:37.803840
# Unit test for function islurp

# Generated at 2026-10-24 20:20:40.219538
# Unit test for function islurp

# Generated at 2026-10-24 20:20:42.636212
# Unit test for function islurp

# Generated at 2026-10-24 20:20:45.052504
# Unit test for function burp

# Generated at 2026-10-24 20:20:59.582721
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 20:21:11.564082
# Unit test for function burp

# Generated at 2026-10-24 20:21:16.269587
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-24 20:21:18.846652
# Unit test for function islurp

# Generated at 2026-10-24 20:21:21.267421
# Unit test for function islurp

# Generated at 2026-10-24 20:21:23.684551
# Unit test for function islurp

# Generated at 2026-10-24 20:21:29.391371
# Unit test for function islurp

# Generated at 2026-10-24 20:21:31.807608
# Unit test for function islurp

# Generated at 2026-10-24 20:21:34.227311
# Unit test for function islurp

# Generated at 2026-10-24 20:21:36.645498
# Unit test for function islurp

# Generated at 2026-10-24 20:21:39.214694
# Unit test for function islurp

# Generated at 2026-10-24 20:21:41.633057
# Unit test for function islurp

# Generated at 2026-10-24 20:21:44.052522
# Unit test for function islurp

# Generated at 2026-10-24 20:21:46.472099
# Unit test for function islurp

# Generated at 2026-10-24 20:21:48.885014
# Unit test for function islurp

# Generated at 2026-10-24 20:21:51.301552
# Unit test for function islurp

# Generated at 2026-10-24 20:21:53.722915
# Unit test for function islurp

# Generated at 2026-10-24 20:21:56.138321
# Unit test for function islurp

# Generated at 2026-10-24 20:21:58.553695
# Unit test for function islurp

# Generated at 2026-10-24 20:22:00.990690
# Unit test for function islurp

# Generated at 2026-10-24 20:22:03.396998
# Unit test for function islurp

# Generated at 2026-10-24 20:22:05.814320
# Unit test for function islurp

# Generated at 2026-10-24 20:22:08.236319
# Unit test for function islurp

# Generated at 2026-10-24 20:22:10.650901
# Unit test for function islurp

# Generated at 2026-10-24 20:22:13.065955
# Unit test for function islurp

# Generated at 2026-10-24 20:22:15.483277
# Unit test for function islurp

# Generated at 2026-10-24 20:22:17.900319
# Unit test for function islurp

# Generated at 2026-10-24 20:22:20.319471
# Unit test for function islurp

# Generated at 2026-10-24 20:22:22.733783
# Unit test for function islurp

# Generated at 2026-10-24 20:22:25.149362
# Unit test for function islurp

# Generated at 2026-10-24 20:22:27.565496
# Unit test for function islurp

# Generated at 2026-10-24 20:22:29.984796
# Unit test for function islurp

# Generated at 2026-10-24 20:22:32.402984
# Unit test for function islurp

# Generated at 2026-10-24 20:22:34.819380
# Unit test for function islurp

# Generated at 2026-10-24 20:22:37.236148
# Unit test for function islurp

# Generated at 2026-10-24 20:22:39.650777
# Unit test for function islurp

# Generated at 2026-10-24 20:22:46.474725
# Unit test for function islurp

# Generated at 2026-10-24 20:22:48.892026
# Unit test for function islurp

# Generated at 2026-10-24 20:22:51.308571
# Unit test for function islurp

# Generated at 2026-10-24 20:22:53.726881
# Unit test for function burp

# Generated at 2026-10-24 20:22:56.143307
# Unit test for function burp

# Generated at 2026-10-24 20:22:58.561528
# Unit test for function burp

# Generated at 2026-10-24 20:23:00.980858
# Unit test for function islurp

# Generated at 2026-10-24 20:23:03.395574
# Unit test for function islurp

# Generated at 2026-10-24 20:23:05.812345
# Unit test for function islurp

# Generated at 2026-10-24 20:23:08.229037
# Unit test for function burp

# Generated at 2026-10-24 20:23:10.649397
# Unit test for function burp

# Generated at 2026-10-24 20:23:13.065023
# Unit test for function burp

# Generated at 2026-10-24 20:23:15.480808
# Unit test for function islurp

# Generated at 2026-10-24 20:23:17.898981
# Unit test for function islurp

# Generated at 2026-10-24 20:23:20.318567
# Unit test for function islurp

# Generated at 2026-10-24 20:23:22.734630
# Unit test for function islurp

# Generated at 2026-10-24 20:23:25.152847
# Unit test for function islurp

# Generated at 2026-10-24 20:23:27.570634
# Unit test for function islurp

# Generated at 2026-10-24 20:23:29.987978
# Unit test for function islurp

# Generated at 2026-10-24 20:23:32.406297
# Unit test for function islurp

# Generated at 2026-10-24 20:23:34.822154
# Unit test for function islurp

# Generated at 2026-10-24 20:23:37.237259
# Unit test for function burp

# Generated at 2026-10-24 20:23:39.651858
# Unit test for function burp

# Generated at 2026-10-24 20:23:42.067628
# Unit test for function burp

# Generated at 2026-10-24 20:23:44.484417
# Unit test for function islurp

# Generated at 2026-10-24 20:23:47.092888
# Unit test for function islurp
def test_islurp():import tempfile