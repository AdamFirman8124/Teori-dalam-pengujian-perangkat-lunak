

# Generated at 2026-10-25 02:42:52.433778
# Unit test for function islurp

# Generated at 2026-10-25 02:42:54.848823
# Unit test for function islurp

# Generated at 2026-10-25 02:42:57.264320
# Unit test for function islurp

# Generated at 2026-10-25 02:42:59.680606
# Unit test for function islurp

# Generated at 2026-10-25 02:43:02.093776
# Unit test for function islurp

# Generated at 2026-10-25 02:43:04.508277
# Unit test for function islurp

# Generated at 2026-10-25 02:43:06.925604
# Unit test for function burp

# Generated at 2026-10-25 02:43:09.338752
# Unit test for function burp

# Generated at 2026-10-25 02:43:11.753934
# Unit test for function burp

# Generated at 2026-10-25 02:43:14.170169
# Unit test for function islurp

# Generated at 2026-10-25 02:43:16.583201
# Unit test for function islurp

# Generated at 2026-10-25 02:43:18.999472
# Unit test for function islurp

# Generated at 2026-10-25 02:43:21.413314
# Unit test for function burp

# Generated at 2026-10-25 02:43:23.828374
# Unit test for function burp

# Generated at 2026-10-25 02:43:26.244029
# Unit test for function burp

# Generated at 2026-10-25 02:43:28.658768
# Unit test for function islurp

# Generated at 2026-10-25 02:43:31.321413
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-25 02:43:42.165427
# Unit test for function islurp

# Generated at 2026-10-25 02:43:49.537553
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 02:44:02.850269
# Unit test for function islurp

# Generated at 2026-10-25 02:44:10.165095
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 02:44:12.697944
# Unit test for function burp

# Generated at 2026-10-25 02:44:15.112190
# Unit test for function burp

# Generated at 2026-10-25 02:44:17.632040
# Unit test for function burp

# Generated at 2026-10-25 02:44:20.053201
# Unit test for function burp

# Generated at 2026-10-25 02:44:22.465644
# Unit test for function burp

# Generated at 2026-10-25 02:44:24.892487
# Unit test for function burp

# Generated at 2026-10-25 02:44:27.319429
# Unit test for function islurp

# Generated at 2026-10-25 02:44:29.734436
# Unit test for function islurp

# Generated at 2026-10-25 02:44:32.149976
# Unit test for function islurp

# Generated at 2026-10-25 02:44:34.565108
# Unit test for function islurp

# Generated at 2026-10-25 02:44:36.979916
# Unit test for function islurp

# Generated at 2026-10-25 02:44:39.394935
# Unit test for function islurp

# Generated at 2026-10-25 02:44:41.811715
# Unit test for function burp

# Generated at 2026-10-25 02:44:44.227407
# Unit test for function burp

# Generated at 2026-10-25 02:44:46.664638
# Unit test for function burp

# Generated at 2026-10-25 02:44:49.080235
# Unit test for function burp

# Generated at 2026-10-25 02:44:51.495707
# Unit test for function burp

# Generated at 2026-10-25 02:44:53.913631
# Unit test for function burp

# Generated at 2026-10-25 02:44:56.325085
# Unit test for function burp

# Generated at 2026-10-25 02:45:01.831543
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:45:42.064232
# Unit test for function burp

# Generated at 2026-10-25 02:45:43.409040
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:45:58.461573
# Unit test for function islurp
def test_islurp():import functools
import os
import sys

LINEMODE = 0


def module_0.islurp(
    filename,
    mode="r",
    iter_by=LINEMODE,
    allow_stdin=True,
    expanduser=True,
    expandvars=True,
):
    """
    Read [expanded] `filename` and yield each line or chunk.
    """
    if iter_by == "LINEMODE":
        iter_by = LINEMODE

    fh = None
    try:
        if filename == "-" and allow_stdin:
            fh = sys.stdin
        else:
            if expanduser:
                filename = os.path.expanduser(filename)
            if expandvars:
                filename = os.path.expandvars(filename)

            fh = open(filename, mode)

        fh_next = (
            fh.readline
            if iter_by == LINEMODE
            else functools.partial(fh.read, iter_by)
        )

        while True:
            buf = fh_next()
            if buf == "" or buf == b"":
                break
            yield buf
    finally:
        if fh is not None and fh is not sys.stdin:
            fh.close()


# convenience
islurp.LINEMODE = LINEMODE

# alias
slurp = islurp


def test_islurp(tmp_path, monkeypatch):
    import io

    # Read a text file line by line.
    text_file = tmp_path / "sample.txt"
    text_file.write_text("first\nsecond\nlast", encoding="utf-8")

    assert list(module_0.islurp(str(text_file))) == [
        "first\n",
        "second\n",
        "last",
    ]

    # Read a text file in fixed-size chunks.
    assert list(module_0.islurp(str(text_file), iter_by=5)) == [
        "first",
        "\nseco",
        "nd\nla",
        "st",
    ]

    # Accept the string form of LINEMODE.
    assert list(module_0.islurp(str(text_file), iter_by="LINEMODE")) == [
        "first\n",
        "second\n",
        "last",
    ]

    # Read binary data and terminate correctly at b''.
    binary_file = tmp_path / "sample.bin"
    binary_file.write_bytes(b"\x00\x01\x02\x03\x04")

    assert list(module_0.islurp(str(binary_file), mode="rb", iter_by=2)) == [
        b"\x00\x01",
        b"\x02\x03",
        b"\x04",
    ]

    # Read from stdin.
    fake_stdin = io.StringIO("stdin line 1\nstdin line 2\n")
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    assert list(module_0.islurp("-")) == [
        "stdin line 1\n",
        "stdin line 2\n",
    ]
    assert not fake_stdin.closed

    # Expand environment variables in the path.
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))
    assert list(module_0.islurp("$ISLURP_TEST_DIR/sample.txt")) == [
        "first\n",
        "second\n",
        "last",
    ]

    # Verify the alias and convenience constant.
    assert slurp is islurp
    assert islurp.LINEMODE == LINEMODE

# Generated at 2026-10-25 02:46:01.312913
# Unit test for function burp

# Generated at 2026-10-25 02:46:02.760572
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:46:05.511131
# Unit test for function burp

# Generated at 2026-10-25 02:46:06.972573
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:46:18.143260
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile

    contents = "first line\nsecond line\nlast line"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fh:
        fh.write(contents)
        filename = fh.name

    try:
        # Line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Standard input
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO(contents)
            assert list(module_0.islurp("-")) == [
                "first line\n",
                "second line\n",
                "last line",
            ]
        finally:
            sys.stdin = original_stdin
    finally:
        os.unlink(filename)

# Generated at 2026-10-25 02:46:20.871749
# Unit test for function burp

# Generated at 2026-10-25 02:46:23.291040
# Unit test for function burp

# Generated at 2026-10-25 02:46:25.705615
# Unit test for function burp

# Generated at 2026-10-25 02:46:28.120926
# Unit test for function islurp

# Generated at 2026-10-25 02:46:30.536247
# Unit test for function islurp

# Generated at 2026-10-25 02:46:32.950536
# Unit test for function islurp

# Generated at 2026-10-25 02:46:35.365482
# Unit test for function burp

# Generated at 2026-10-25 02:46:37.782349
# Unit test for function burp

# Generated at 2026-10-25 02:46:40.195333
# Unit test for function burp

# Generated at 2026-10-25 02:46:42.806093
# Unit test for function burp

# Generated at 2026-10-25 02:46:45.218476
# Unit test for function burp

# Generated at 2026-10-25 02:46:47.637556
# Unit test for function burp

# Generated at 2026-10-25 02:46:50.050997
# Unit test for function islurp

# Generated at 2026-10-25 02:46:52.467292
# Unit test for function islurp

# Generated at 2026-10-25 02:46:54.882471
# Unit test for function islurp

# Generated at 2026-10-25 02:46:57.298616
# Unit test for function islurp

# Generated at 2026-10-25 02:46:59.716834
# Unit test for function islurp

# Generated at 2026-10-25 02:47:02.132244
# Unit test for function islurp

# Generated at 2026-10-25 02:47:04.546855
# Unit test for function islurp

# Generated at 2026-10-25 02:47:06.962782
# Unit test for function islurp

# Generated at 2026-10-25 02:47:09.378204
# Unit test for function islurp

# Generated at 2026-10-25 02:47:11.794084
# Unit test for function burp

# Generated at 2026-10-25 02:47:20.368879
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-25 02:47:42.453683
# Unit test for function islurp

# Generated at 2026-10-25 02:47:48.232543
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 02:47:51.101639
# Unit test for function burp

# Generated at 2026-10-25 02:47:52.434682
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:48:06.874599
# Unit test for function islurp

# Generated at 2026-10-25 02:48:11.682433
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-25 02:48:30.170771
# Unit test for function islurp
def test_islurp():
    import io
    import tempfile

    contents = "alpha\nbeta\n"

    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == ["alpha\n", "beta\n"]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "alpha\n",
            "beta\n",
        ]

        # Fixed-size chunks
        assert list(module_0.islurp(filename, iter_by=3)) == [
            "alp",
            "ha\n",
            "bet",
            "a\n",
        ]

        # Binary mode must stop at b''.
        iterator = module_0.islurp(filename, mode="rb", iter_by=100)
        assert next(iterator) == contents.encode()
        try:
            next(iterator)
        except StopIteration:
            pass
        else:
            raise AssertionError("Binary iteration did not stop at EOF")

        # Reading from stdin
        original_stdin = sys.stdin
        sys.stdin = io.StringIO(contents)
        try:
            assert list(module_0.islurp("-")) == ["alpha\n", "beta\n"]
        finally:
            sys.stdin = original_stdin

    finally:
        os.unlink(filename)

# Generated at 2026-10-25 02:48:40.252901
# Unit test for function islurp
def test_islurp():
    import tempfile

    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        contents = "first line\nsecond line\nlast line"
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default: iterate by line
        assert list(module_0.islurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Iterate by fixed-size chunks
        assert list(module_0.islurp(filename, iter_by=5)) == [
            contents[i:i + 5] for i in range(0, len(contents), 5)
        ]

        # Support the symbolic line-mode value
        assert "".join(module_0.islurp(filename, iter_by="LINEMODE")) == contents

    finally:
        os.remove(filename)

# Generated at 2026-10-25 02:48:43.039317
# Unit test for function burp

# Generated at 2026-10-25 02:48:44.362816
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:49:02.652425
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "first line\nsecond line\nlast line"

    fd, filename = tempfile.mkstemp()
    os.close(fd)

    try:
        with open(filename, "w") as fh:
            fh.write(contents)

        # Default: iterate by line
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

        # Iterate in fixed-size chunks
        assert list(module_0.islurp(filename, iter_by=4)) == [
            contents[i:i + 4] for i in range(0, len(contents), 4)
        ]

        # Verify the alias
        assert list(slurp(filename)) == [
            "first line\n",
            "second line\n",
            "last line",
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-25 02:49:05.070038
# Unit test for function burp

# Generated at 2026-10-25 02:49:07.485018
# Unit test for function burp

# Generated at 2026-10-25 02:49:10.018847
# Unit test for function burp

# Generated at 2026-10-25 02:49:12.436862
# Unit test for function islurp

# Generated at 2026-10-25 02:49:14.851832
# Unit test for function islurp

# Generated at 2026-10-25 02:49:17.266603
# Unit test for function islurp

# Generated at 2026-10-25 02:49:19.682857
# Unit test for function burp

# Generated at 2026-10-25 02:49:26.292641
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-25 02:49:39.240742
# Unit test for function islurp

# Generated at 2026-10-25 02:49:49.372887
# Unit test for function islurp
def test_islurp():import io

# Generated at 2026-10-25 02:50:01.252245
# Unit test for function islurp

# Generated at 2026-10-25 02:50:03.674320
# Unit test for function islurp

# Generated at 2026-10-25 02:50:06.090277
# Unit test for function islurp

# Generated at 2026-10-25 02:50:08.507077
# Unit test for function islurp

# Generated at 2026-10-25 02:50:10.921651
# Unit test for function islurp

# Generated at 2026-10-25 02:50:13.337156
# Unit test for function islurp

# Generated at 2026-10-25 02:50:15.751624
# Unit test for function islurp

# Generated at 2026-10-25 02:50:18.167556
# Unit test for function islurp

# Generated at 2026-10-25 02:50:20.583332
# Unit test for function islurp

# Generated at 2026-10-25 02:50:22.997660
# Unit test for function islurp

# Generated at 2026-10-25 02:50:25.412256
# Unit test for function islurp

# Generated at 2026-10-25 02:50:27.827372
# Unit test for function islurp

# Generated at 2026-10-25 02:50:30.241704
# Unit test for function islurp

# Generated at 2026-10-25 02:50:32.661810
# Unit test for function islurp

# Generated at 2026-10-25 02:50:35.077598
# Unit test for function islurp

# Generated at 2026-10-25 02:50:37.665102
# Unit test for function islurp

# Generated at 2026-10-25 02:50:43.234951
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 02:50:46.102759
# Unit test for function burp

# Generated at 2026-10-25 02:50:47.431493
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:50:50.163070
# Unit test for function burp

# Generated at 2026-10-25 02:50:51.631435
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 02:51:03.106418
# Unit test for function islurp
def test_islurp():import io


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "example.txt"
    path.write_text("first line\nsecond line\n", encoding="utf-8")

    # Default: iterate by line.
    assert list(module_0.islurp(str(path))) == [
        "first line\n",
        "second line\n",
    ]

    # Explicit line mode.
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "first line\n",
        "second line\n",
    ]

    # Iterate in fixed-size chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "first",
        " line",
        "\nseco",
        "nd li",
        "ne\n",
    ]

    # Read from stdin.
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin data\n"))
    assert list(module_0.islurp("-")) == ["stdin data\n"]

    # Binary mode.
    binary_path = tmp_path / "example.bin"
    binary_path.write_bytes(b"abcdef")
    assert list(module_0.islurp(str(binary_path), mode="rb", iter_by=2)) == [
        b"ab",
        b"cd",
        b"ef",
    ]

# Generated at 2026-10-25 02:51:20.716768
# Unit test for function islurp
def test_islurp():import io
import sys
import pytest


def test_islurp_lines(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("alpha\nbeta\n", encoding="utf-8")

    assert list(module_0.islurp(str(path))) == ["alpha\n", "beta\n"]
    assert list(module_0.islurp(str(path), iter_by="LINEMODE")) == [
        "alpha\n",
        "beta\n",
    ]


def test_islurp_chunks(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("alpha\nbeta\n", encoding="utf-8")

    assert list(module_0.islurp(str(path), iter_by=4)) == [
        "alph",
        "a\nbe",
        "ta\n",
    ]


def test_islurp_expands_environment_variables(tmp_path, monkeypatch):
    path = tmp_path / "sample.txt"
    path.write_text("contents\n", encoding="utf-8")
    monkeypatch.setenv("ISLURP_TEST_DIR", str(tmp_path))

    assert list(module_0.islurp("$ISLURP_TEST_DIR/sample.txt")) == ["contents\n"]


def test_islurp_reads_stdin(monkeypatch):
    stdin = io.StringIO("first\nsecond\n")
    monkeypatch.setattr(sys, "stdin", stdin)

    assert list(module_0.islurp("-")) == ["first\n", "second\n"]
    assert not stdin.closed


def test_islurp_binary_eof(tmp_path):
    path = tmp_path / "sample.bin"
    path.write_bytes(b"abcdef")

    chunks = module_0.islurp(str(path), mode="rb", iter_by=4)

    assert next(chunks) == b"abcd"
    assert next(chunks) == b"ef"

    with pytest.raises(StopIteration):
        next(chunks)

# Generated at 2026-10-25 02:51:23.133042
# Unit test for function burp

# Generated at 2026-10-25 02:51:25.547774
# Unit test for function burp

# Generated at 2026-10-25 02:51:27.963830
# Unit test for function burp

# Generated at 2026-10-25 02:51:30.378806
# Unit test for function burp

# Generated at 2026-10-25 02:51:32.794963
# Unit test for function burp

# Generated at 2026-10-25 02:51:35.213132
# Unit test for function burp

# Generated at 2026-10-25 02:51:37.624753
# Unit test for function burp

# Generated at 2026-10-25 02:51:40.040226
# Unit test for function burp

# Generated at 2026-10-25 02:51:42.459126
# Unit test for function burp

# Generated at 2026-10-25 02:51:44.884159
# Unit test for function islurp

# Generated at 2026-10-25 02:51:47.298574
# Unit test for function islurp

# Generated at 2026-10-25 02:51:49.712987
# Unit test for function islurp

# Generated at 2026-10-25 02:51:52.128179
# Unit test for function burp

# Generated at 2026-10-25 02:51:54.543417
# Unit test for function burp

# Generated at 2026-10-25 02:51:56.959167
# Unit test for function burp

# Generated at 2026-10-25 02:51:59.372765
# Unit test for function burp

# Generated at 2026-10-25 02:52:01.787039
# Unit test for function burp

# Generated at 2026-10-25 02:52:04.201955
# Unit test for function burp

# Generated at 2026-10-25 02:52:06.619721
# Unit test for function islurp

# Generated at 2026-10-25 02:52:09.031430
# Unit test for function islurp

# Generated at 2026-10-25 02:52:11.445845
# Unit test for function islurp

# Generated at 2026-10-25 02:52:13.863219
# Unit test for function burp

# Generated at 2026-10-25 02:52:16.280253
# Unit test for function burp

# Generated at 2026-10-25 02:52:18.698595
# Unit test for function burp

# Generated at 2026-10-25 02:52:21.114832
# Unit test for function burp

# Generated at 2026-10-25 02:52:23.529469
# Unit test for function burp

# Generated at 2026-10-25 02:52:25.944362
# Unit test for function burp

# Generated at 2026-10-25 02:52:28.360212
# Unit test for function islurp

# Generated at 2026-10-25 02:52:30.774402
# Unit test for function islurp

# Generated at 2026-10-25 02:52:33.189472
# Unit test for function islurp

# Generated at 2026-10-25 02:52:35.603384
# Unit test for function burp

# Generated at 2026-10-25 02:52:38.019281
# Unit test for function burp

# Generated at 2026-10-25 02:52:40.433481
# Unit test for function burp

# Generated at 2026-10-25 02:52:42.849001
# Unit test for function islurp

# Generated at 2026-10-25 02:52:45.266678
# Unit test for function islurp

# Generated at 2026-10-25 02:52:47.677942
# Unit test for function islurp

# Generated at 2026-10-25 02:52:50.091891
# Unit test for function islurp

# Generated at 2026-10-25 02:52:52.509526
# Unit test for function islurp

# Generated at 2026-10-25 02:52:54.920901
# Unit test for function islurp