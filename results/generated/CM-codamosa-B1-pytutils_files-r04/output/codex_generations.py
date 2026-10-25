

# Generated at 2026-10-24 04:23:05.630404
# Unit test for function islurp
def test_islurp():import io


def test_islurp(tmp_path, monkeypatch):
    path = tmp_path / "sample.txt"
    path.write_text("alpha\nbeta\ngamma", encoding="utf-8")

    # Default: iterate by line.
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

    # Iterate in fixed-size chunks.
    assert list(module_0.islurp(str(path), iter_by=5)) == [
        "alpha",
        "\nbeta",
        "\ngamm",
        "a",
    ]

    # Expand environment variables in the path.
    monkeypatch.setenv("ISLURP_TEST_FILE", str(path))
    assert "".join(module_0.islurp("$ISLURP_TEST_FILE")) == "alpha\nbeta\ngamma"

    # Read from stdin.
    monkeypatch.setattr(sys, "stdin", io.StringIO("from\nstdin\n"))
    assert list(module_0.islurp("-")) == ["from\n", "stdin\n"]

# Generated at 2026-10-24 04:23:15.766170
# Unit test for function burp

# Generated at 2026-10-24 04:23:17.419572
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:23:34.205013
# Unit test for function islurp

# Generated at 2026-10-24 04:23:41.230390
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:24:07.690944
# Unit test for function islurp

# Generated at 2026-10-24 04:24:14.301237
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:24:28.469731
# Unit test for function burp

# Generated at 2026-10-24 04:24:29.825151
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:24:40.143321
# Unit test for function burp
def test_burp():
    import io
    import tempfile
    from contextlib import redirect_stdout

    contents = "first line\nsecond line\n"

    # Writes contents to a file.
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "output.txt")

        result = module_0.burp(filename, contents)

        assert result is None
        with open(filename, "r") as fh:
            assert fh.read() == contents

    # Writes to stdout when filename is "-".
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        module_0.burp("-", contents)

    assert stdout.getvalue() == contents

# Generated at 2026-10-24 04:24:46.596858
# Unit test for function burp
def test_burp():
    import tempfile

    contents = "Hello, world!\nSecond line.\n"

    with tempfile.TemporaryDirectory() as directory:
        filename = os.path.join(directory, "output.txt")

        module_0.burp(filename, contents)

        with open(filename, "r") as fh:
            assert fh.read() == contents

# Generated at 2026-10-24 04:24:49.017156
# Unit test for function burp

# Generated at 2026-10-24 04:24:51.432311
# Unit test for function burp

# Generated at 2026-10-24 04:24:53.849819
# Unit test for function burp

# Generated at 2026-10-24 04:24:56.263490
# Unit test for function burp

# Generated at 2026-10-24 04:24:57.670945
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:25:32.849701
# Unit test for function islurp

# Generated at 2026-10-24 04:25:35.264943
# Unit test for function islurp

# Generated at 2026-10-24 04:25:37.773511
# Unit test for function islurp

# Generated at 2026-10-24 04:25:40.189287
# Unit test for function burp

# Generated at 2026-10-24 04:25:42.604000
# Unit test for function burp

# Generated at 2026-10-24 04:25:45.018849
# Unit test for function burp

# Generated at 2026-10-24 04:25:47.432142
# Unit test for function islurp

# Generated at 2026-10-24 04:25:49.848594
# Unit test for function islurp

# Generated at 2026-10-24 04:25:52.264604
# Unit test for function islurp

# Generated at 2026-10-24 04:25:54.681136
# Unit test for function islurp

# Generated at 2026-10-24 04:25:57.096579
# Unit test for function islurp

# Generated at 2026-10-24 04:25:59.510135
# Unit test for function islurp

# Generated at 2026-10-24 04:26:01.928015
# Unit test for function islurp

# Generated at 2026-10-24 04:26:04.343753
# Unit test for function islurp

# Generated at 2026-10-24 04:26:06.759067
# Unit test for function islurp

# Generated at 2026-10-24 04:26:09.172977
# Unit test for function burp

# Generated at 2026-10-24 04:26:11.587826
# Unit test for function burp

# Generated at 2026-10-24 04:26:12.955765
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:26:41.075419
# Unit test for function islurp
def test_islurp():
    import tempfile
    from unittest.mock import patch
    from io import StringIO

    contents = "first line\nsecond line\nlast line"

    fd, filename = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, "w") as fh:
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

        # String form of LINEMODE
        assert list(module_0.islurp(filename, iter_by="LINEMODE")) == [
            "first line\n",
            "second line\n",
            "last line",
        ]

        # Standard input
        with patch("sys.stdin", StringIO(contents)):
            assert "".join(module_0.islurp("-")) == contents
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 04:26:43.492341
# Unit test for function islurp

# Generated at 2026-10-24 04:26:45.906483
# Unit test for function islurp

# Generated at 2026-10-24 04:26:48.326725
# Unit test for function islurp

# Generated at 2026-10-24 04:26:50.740777
# Unit test for function islurp

# Generated at 2026-10-24 04:26:53.160414
# Unit test for function islurp

# Generated at 2026-10-24 04:26:55.575498
# Unit test for function islurp

# Generated at 2026-10-24 04:26:57.996543
# Unit test for function burp

# Generated at 2026-10-24 04:27:00.552436
# Unit test for function burp

# Generated at 2026-10-24 04:27:02.978427
# Unit test for function burp

# Generated at 2026-10-24 04:27:05.394557
# Unit test for function burp

# Generated at 2026-10-24 04:27:07.810748
# Unit test for function burp

# Generated at 2026-10-24 04:27:10.227577
# Unit test for function burp

# Generated at 2026-10-24 04:27:12.639880
# Unit test for function burp

# Generated at 2026-10-24 04:27:15.056350
# Unit test for function burp

# Generated at 2026-10-24 04:27:17.471538
# Unit test for function burp

# Generated at 2026-10-24 04:27:19.890519
# Unit test for function islurp

# Generated at 2026-10-24 04:27:22.327952
# Unit test for function islurp

# Generated at 2026-10-24 04:27:24.739081
# Unit test for function islurp

# Generated at 2026-10-24 04:27:56.665674
# Unit test for function islurp
def test_islurp():
    import tempfile

    contents = "alpha\nbeta\ngamma"
    fd, filename = tempfile.mkstemp(text=True)

    try:
        with os.fdopen(fd, 'w') as fh:
            fh.write(contents)

        # Default line-by-line iteration
        assert list(module_0.islurp(filename)) == [
            "alpha\n",
            "beta\n",
            "gamma",
        ]

        # Explicit line mode
        assert list(module_0.islurp(filename, iter_by='LINEMODE')) == [
            "alpha\n",
            "beta\n",
            "gamma",
        ]

        # Fixed-size chunk iteration
        assert list(module_0.islurp(filename, iter_by=4)) == [
            "alph",
            "a\nbe",
            "ta\ng",
            "amma",
        ]
    finally:
        os.unlink(filename)

# Generated at 2026-10-24 04:27:59.083268
# Unit test for function islurp

# Generated at 2026-10-24 04:28:01.499854
# Unit test for function islurp

# Generated at 2026-10-24 04:28:03.912800
# Unit test for function islurp

# Generated at 2026-10-24 04:28:06.324639
# Unit test for function burp

# Generated at 2026-10-24 04:28:08.736172
# Unit test for function burp

# Generated at 2026-10-24 04:28:11.320511
# Unit test for function burp

# Generated at 2026-10-24 04:28:13.732655
# Unit test for function islurp

# Generated at 2026-10-24 04:28:16.145205
# Unit test for function islurp

# Generated at 2026-10-24 04:28:18.556357
# Unit test for function islurp

# Generated at 2026-10-24 04:28:20.967977
# Unit test for function islurp

# Generated at 2026-10-24 04:28:23.379425
# Unit test for function islurp

# Generated at 2026-10-24 04:28:25.790962
# Unit test for function islurp

# Generated at 2026-10-24 04:28:28.213803
# Unit test for function islurp

# Generated at 2026-10-24 04:28:30.614261
# Unit test for function islurp

# Generated at 2026-10-24 04:28:33.025773
# Unit test for function islurp

# Generated at 2026-10-24 04:28:35.437080
# Unit test for function islurp

# Generated at 2026-10-24 04:28:37.849350
# Unit test for function islurp

# Generated at 2026-10-24 04:28:40.261004
# Unit test for function islurp

# Generated at 2026-10-24 04:28:42.672396
# Unit test for function burp

# Generated at 2026-10-24 04:28:45.083575
# Unit test for function burp

# Generated at 2026-10-24 04:28:47.496403
# Unit test for function burp

# Generated at 2026-10-24 04:28:49.908441
# Unit test for function islurp

# Generated at 2026-10-24 04:28:52.319462
# Unit test for function islurp

# Generated at 2026-10-24 04:28:54.731826
# Unit test for function islurp

# Generated at 2026-10-24 04:28:57.143460
# Unit test for function islurp

# Generated at 2026-10-24 04:28:59.556306
# Unit test for function islurp

# Generated at 2026-10-24 04:29:01.967570
# Unit test for function islurp

# Generated at 2026-10-24 04:29:04.380179
# Unit test for function islurp

# Generated at 2026-10-24 04:29:06.791684
# Unit test for function islurp

# Generated at 2026-10-24 04:29:09.202910
# Unit test for function islurp

# Generated at 2026-10-24 04:29:11.614600
# Unit test for function islurp

# Generated at 2026-10-24 04:29:14.026017
# Unit test for function islurp

# Generated at 2026-10-24 04:29:21.640896
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 04:29:31.070638
# Unit test for function burp

# Generated at 2026-10-24 04:29:32.377674
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:29:42.819380
# Unit test for function burp

# Generated at 2026-10-24 04:29:44.142181
# Unit test for function burp
def test_burp():import contextlib

# Generated at 2026-10-24 04:30:00.887105
# Unit test for function islurp

# Generated at 2026-10-24 04:30:03.515765
# Unit test for function islurp

# Generated at 2026-10-24 04:30:05.926549
# Unit test for function islurp

# Generated at 2026-10-24 04:30:08.338744
# Unit test for function islurp

# Generated at 2026-10-24 04:30:10.750563
# Unit test for function islurp

# Generated at 2026-10-24 04:30:13.162184
# Unit test for function islurp

# Generated at 2026-10-24 04:30:15.573469
# Unit test for function burp

# Generated at 2026-10-24 04:30:17.985094
# Unit test for function burp

# Generated at 2026-10-24 04:30:20.399134
# Unit test for function burp

# Generated at 2026-10-24 04:30:22.809635
# Unit test for function islurp

# Generated at 2026-10-24 04:30:25.378510
# Unit test for function islurp

# Generated at 2026-10-24 04:30:27.801096
# Unit test for function islurp

# Generated at 2026-10-24 04:30:30.200853
# Unit test for function islurp

# Generated at 2026-10-24 04:30:32.618117
# Unit test for function islurp

# Generated at 2026-10-24 04:30:35.025661
# Unit test for function islurp

# Generated at 2026-10-24 04:30:37.436774
# Unit test for function islurp

# Generated at 2026-10-24 04:30:39.848788
# Unit test for function islurp

# Generated at 2026-10-24 04:30:42.260646
# Unit test for function islurp

# Generated at 2026-10-24 04:30:44.672382
# Unit test for function islurp

# Generated at 2026-10-24 04:30:47.083615
# Unit test for function islurp

# Generated at 2026-10-24 04:30:49.494893
# Unit test for function islurp

# Generated at 2026-10-24 04:30:51.906838
# Unit test for function burp

# Generated at 2026-10-24 04:30:54.318070
# Unit test for function burp

# Generated at 2026-10-24 04:30:56.730191
# Unit test for function burp

# Generated at 2026-10-24 04:30:59.141312
# Unit test for function burp

# Generated at 2026-10-24 04:31:01.552554
# Unit test for function burp

# Generated at 2026-10-24 04:31:03.966463
# Unit test for function burp

# Generated at 2026-10-24 04:31:06.376194
# Unit test for function islurp

# Generated at 2026-10-24 04:31:08.788005
# Unit test for function islurp

# Generated at 2026-10-24 04:31:11.200488
# Unit test for function islurp

# Generated at 2026-10-24 04:31:13.623446
# Unit test for function islurp

# Generated at 2026-10-24 04:31:16.029556
# Unit test for function islurp

# Generated at 2026-10-24 04:31:18.440286
# Unit test for function islurp

# Generated at 2026-10-24 04:31:20.854760
# Unit test for function islurp

# Generated at 2026-10-24 04:31:23.263022
# Unit test for function islurp

# Generated at 2026-10-24 04:31:25.676496
# Unit test for function islurp

# Generated at 2026-10-24 04:31:28.085635
# Unit test for function burp

# Generated at 2026-10-24 04:31:30.497580
# Unit test for function burp

# Generated at 2026-10-24 04:31:32.909597
# Unit test for function burp

# Generated at 2026-10-24 04:31:35.321283
# Unit test for function burp

# Generated at 2026-10-24 04:31:37.732459
# Unit test for function burp

# Generated at 2026-10-24 04:31:40.143890
# Unit test for function burp

# Generated at 2026-10-24 04:31:42.555517
# Unit test for function burp

# Generated at 2026-10-24 04:31:44.968493
# Unit test for function burp

# Generated at 2026-10-24 04:31:47.379015
# Unit test for function burp

# Generated at 2026-10-24 04:31:49.790127
# Unit test for function burp

# Generated at 2026-10-24 04:31:52.204472
# Unit test for function burp

# Generated at 2026-10-24 04:31:54.616414
# Unit test for function burp

# Generated at 2026-10-24 04:31:57.028811
# Unit test for function islurp

# Generated at 2026-10-24 04:31:59.440631
# Unit test for function islurp

# Generated at 2026-10-24 04:32:01.853762
# Unit test for function islurp

# Generated at 2026-10-24 04:32:04.572084
# Unit test for function burp
def test_burp():import io

# Generated at 2026-10-24 04:32:32.926737
# Unit test for function islurp

# Generated at 2026-10-24 04:32:40.112796
# Unit test for function islurp
def test_islurp():import tempfile
