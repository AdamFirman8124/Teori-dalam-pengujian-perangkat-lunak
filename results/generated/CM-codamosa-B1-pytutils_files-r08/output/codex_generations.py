

# Generated at 2026-10-25 09:23:35.714964
# Unit test for function islurp

# Generated at 2026-10-25 09:23:38.128799
# Unit test for function islurp

# Generated at 2026-10-25 09:23:40.542927
# Unit test for function islurp

# Generated at 2026-10-25 09:23:42.956766
# Unit test for function islurp

# Generated at 2026-10-25 09:23:45.375419
# Unit test for function islurp

# Generated at 2026-10-25 09:23:47.792796
# Unit test for function islurp

# Generated at 2026-10-25 09:23:50.207459
# Unit test for function islurp

# Generated at 2026-10-25 09:23:52.620970
# Unit test for function islurp

# Generated at 2026-10-25 09:23:55.035760
# Unit test for function islurp

# Generated at 2026-10-25 09:23:57.451881
# Unit test for function islurp

# Generated at 2026-10-25 09:23:59.866977
# Unit test for function islurp

# Generated at 2026-10-25 09:24:02.284738
# Unit test for function islurp

# Generated at 2026-10-25 09:24:04.698480
# Unit test for function burp

# Generated at 2026-10-25 09:24:07.114267
# Unit test for function burp

# Generated at 2026-10-25 09:24:09.529884
# Unit test for function burp

# Generated at 2026-10-25 09:24:11.944611
# Unit test for function islurp

# Generated at 2026-10-25 09:24:14.360040
# Unit test for function islurp

# Generated at 2026-10-25 09:24:16.773745
# Unit test for function islurp

# Generated at 2026-10-25 09:24:19.188340
# Unit test for function islurp

# Generated at 2026-10-25 09:24:21.604939
# Unit test for function islurp

# Generated at 2026-10-25 09:24:24.019540
# Unit test for function islurp

# Generated at 2026-10-25 09:24:26.434863
# Unit test for function burp

# Generated at 2026-10-25 09:24:28.848877
# Unit test for function burp

# Generated at 2026-10-25 09:24:31.263745
# Unit test for function burp

# Generated at 2026-10-25 09:24:33.678710
# Unit test for function burp

# Generated at 2026-10-25 09:24:36.126368
# Unit test for function burp

# Generated at 2026-10-25 09:24:38.540091
# Unit test for function burp

# Generated at 2026-10-25 09:24:40.954628
# Unit test for function islurp

# Generated at 2026-10-25 09:24:43.369102
# Unit test for function islurp

# Generated at 2026-10-25 09:24:45.784602
# Unit test for function islurp

# Generated at 2026-10-25 09:24:48.209066
# Unit test for function islurp

# Generated at 2026-10-25 09:24:50.624226
# Unit test for function islurp

# Generated at 2026-10-25 09:24:53.037512
# Unit test for function islurp

# Generated at 2026-10-25 09:24:55.452604
# Unit test for function islurp

# Generated at 2026-10-25 09:24:57.865718
# Unit test for function islurp

# Generated at 2026-10-25 09:25:00.346726
# Unit test for function islurp

# Generated at 2026-10-25 09:25:02.759958
# Unit test for function islurp

# Generated at 2026-10-25 09:25:05.174524
# Unit test for function islurp

# Generated at 2026-10-25 09:25:07.589965
# Unit test for function islurp

# Generated at 2026-10-25 09:25:10.005630
# Unit test for function burp

# Generated at 2026-10-25 09:25:12.422892
# Unit test for function burp

# Generated at 2026-10-25 09:25:14.834926
# Unit test for function burp

# Generated at 2026-10-25 09:25:17.248668
# Unit test for function islurp

# Generated at 2026-10-25 09:25:19.785147
# Unit test for function islurp

# Generated at 2026-10-25 09:25:22.134669
# Unit test for function islurp

# Generated at 2026-10-25 09:25:24.550662
# Unit test for function islurp

# Generated at 2026-10-25 09:25:26.963649
# Unit test for function islurp

# Generated at 2026-10-25 09:25:29.378386
# Unit test for function islurp

# Generated at 2026-10-25 09:25:31.870050
# Unit test for function burp

# Generated at 2026-10-25 09:25:34.224789
# Unit test for function burp

# Generated at 2026-10-25 09:25:36.639792
# Unit test for function burp

# Generated at 2026-10-25 09:25:39.054288
# Unit test for function islurp

# Generated at 2026-10-25 09:25:41.469583
# Unit test for function islurp

# Generated at 2026-10-25 09:25:43.884395
# Unit test for function islurp

# Generated at 2026-10-25 09:25:46.299119
# Unit test for function islurp

# Generated at 2026-10-25 09:25:48.713991
# Unit test for function islurp

# Generated at 2026-10-25 09:25:51.127968
# Unit test for function islurp

# Generated at 2026-10-25 09:26:11.380927
# Unit test for function islurp

# Generated at 2026-10-25 09:26:19.163563
# Unit test for function islurp
def test_islurp():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as fh:
        fh.write('alpha\nbeta\ngamma\n')
        path = fh.name

    assert list(module_0.islurp(path)) == ['alpha\n', 'beta\n', 'gamma\n']
    assert list(module_0.islurp(path, iter_by=4)) == ['alph', 'a\nbe', 'ta\ng', 'amma', '\n']
    assert list(module_0.islurp(path, iter_by=100)) == ['alpha\nbeta\ngamma\n']
    assert list(module_0.islurp(path, expanduser=True, expandvars=True)) == ['alpha\n', 'beta\n', 'gamma\n']

    os.remove(path)

# Generated at 2026-10-25 09:26:27.048350
# Unit test for function burp

# Generated at 2026-10-25 09:26:28.425656
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 09:26:30.846061
# Unit test for function burp

# Generated at 2026-10-25 09:26:33.268027
# Unit test for function burp

# Generated at 2026-10-25 09:26:35.682712
# Unit test for function burp

# Generated at 2026-10-25 09:26:38.093496
# Unit test for function burp

# Generated at 2026-10-25 09:26:40.506494
# Unit test for function burp

# Generated at 2026-10-25 09:26:42.920890
# Unit test for function burp

# Generated at 2026-10-25 09:26:45.711261
# Unit test for function islurp

# Generated at 2026-10-25 09:26:48.121897
# Unit test for function islurp

# Generated at 2026-10-25 09:26:50.537210
# Unit test for function islurp

# Generated at 2026-10-25 09:26:54.646551
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 09:27:12.699076
# Unit test for function islurp

# Generated at 2026-10-25 09:27:39.547497
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 09:27:41.964218
# Unit test for function burp

# Generated at 2026-10-25 09:27:44.381500
# Unit test for function burp

# Generated at 2026-10-25 09:27:46.878020
# Unit test for function burp

# Generated at 2026-10-25 09:27:49.259116
# Unit test for function islurp

# Generated at 2026-10-25 09:27:51.673167
# Unit test for function islurp

# Generated at 2026-10-25 09:27:54.085210
# Unit test for function islurp

# Generated at 2026-10-25 09:27:56.499372
# Unit test for function islurp

# Generated at 2026-10-25 09:27:58.915541
# Unit test for function islurp

# Generated at 2026-10-25 09:28:16.413863
# Unit test for function islurp
def test_islurp():
    import io
    import os
    import sys
    import tempfile

    assert slurp is islurp
    assert islurp.LINEMODE == 0

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "sample.txt")
        burp(path, "alpha\nbeta\ngamma\n")

        # line mode (default)
        assert list(module_0.islurp(path)) == ["alpha\n", "beta\n", "gamma\n"]
        # chunk mode
        assert list(module_0.islurp(path, iter_by=4)) == ["alph", "a\nbe", "ta\ng", "amma", "\n"]
        # append then re-read
        burp(path, "delta\n", mode="a")
        assert list(module_0.islurp(path)) == ["alpha\n", "beta\n", "gamma\n", "delta\n"]

        # expandvars
        os.environ["ISLURP_TEST_FILE"] = path
        assert list(module_0.islurp("$ISLURP_TEST_FILE")) == ["alpha\n", "beta\n", "gamma\n", "delta\n"]
        del os.environ["ISLURP_TEST_FILE"]

        # expanduser
        saved_home = os.environ.get("HOME")
        os.environ["HOME"] = tmpdir
        assert list(module_0.islurp("~/sample.txt")) == ["alpha\n", "beta\n", "gamma\n", "delta\n"]
        if saved_home is None:
            del os.environ["HOME"]
        else:
            os.environ["HOME"] = saved_home

    # burp to stdout
    saved_stdout = sys.stdout
    sys.stdout = io.StringIO()
    burp("-", "hello")
    assert sys.stdout.getvalue() == "hello"

# Generated at 2026-10-25 09:28:45.121419
# Unit test for function burp

# Generated at 2026-10-25 09:28:46.517008
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 09:29:06.280863
# Unit test for function burp

# Generated at 2026-10-25 09:29:07.674662
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 09:29:27.888315
# Unit test for function islurp

# Generated at 2026-10-25 09:29:30.304281
# Unit test for function islurp

# Generated at 2026-10-25 09:29:32.719149
# Unit test for function islurp

# Generated at 2026-10-25 09:29:35.134459
# Unit test for function islurp

# Generated at 2026-10-25 09:29:37.580629
# Unit test for function islurp

# Generated at 2026-10-25 09:29:39.961266
# Unit test for function islurp

# Generated at 2026-10-25 09:29:42.376615
# Unit test for function islurp

# Generated at 2026-10-25 09:29:44.791888
# Unit test for function islurp

# Generated at 2026-10-25 09:29:47.209380
# Unit test for function islurp

# Generated at 2026-10-25 09:29:49.618024
# Unit test for function islurp

# Generated at 2026-10-25 09:29:52.031146
# Unit test for function islurp

# Generated at 2026-10-25 09:29:54.444441
# Unit test for function islurp

# Generated at 2026-10-25 09:29:56.859145
# Unit test for function islurp

# Generated at 2026-10-25 09:29:59.507520
# Unit test for function islurp

# Generated at 2026-10-25 09:30:01.922062
# Unit test for function islurp

# Generated at 2026-10-25 09:30:04.336841
# Unit test for function islurp

# Generated at 2026-10-25 09:30:06.754685
# Unit test for function islurp

# Generated at 2026-10-25 09:30:09.168042
# Unit test for function islurp

# Generated at 2026-10-25 09:30:11.588053
# Unit test for function islurp

# Generated at 2026-10-25 09:30:13.999170
# Unit test for function islurp

# Generated at 2026-10-25 09:30:16.413827
# Unit test for function islurp

# Generated at 2026-10-25 09:30:18.830802
# Unit test for function islurp

# Generated at 2026-10-25 09:30:21.244648
# Unit test for function islurp

# Generated at 2026-10-25 09:30:23.658654
# Unit test for function islurp

# Generated at 2026-10-25 09:30:26.073268
# Unit test for function islurp

# Generated at 2026-10-25 09:30:28.486629
# Unit test for function islurp

# Generated at 2026-10-25 09:30:30.902202
# Unit test for function islurp

# Generated at 2026-10-25 09:30:53.001483
# Unit test for function islurp
def test_islurp():import io

# Generated at 2026-10-25 09:31:21.451771
# Unit test for function islurp
def test_islurp():import tempfile


# Generated at 2026-10-25 09:31:24.092951
# Unit test for function islurp

# Generated at 2026-10-25 09:31:26.506801
# Unit test for function islurp

# Generated at 2026-10-25 09:31:28.920623
# Unit test for function islurp

# Generated at 2026-10-25 09:31:31.335991
# Unit test for function burp

# Generated at 2026-10-25 09:31:33.751501
# Unit test for function burp

# Generated at 2026-10-25 09:31:36.165399
# Unit test for function burp

# Generated at 2026-10-25 09:31:38.580824
# Unit test for function islurp

# Generated at 2026-10-25 09:31:41.124803
# Unit test for function islurp

# Generated at 2026-10-25 09:31:43.451170
# Unit test for function islurp

# Generated at 2026-10-25 09:31:45.865368
# Unit test for function burp

# Generated at 2026-10-25 09:31:48.279179
# Unit test for function burp

# Generated at 2026-10-25 09:31:50.694249
# Unit test for function burp

# Generated at 2026-10-25 09:32:07.735948
# Unit test for function islurp

# Generated at 2026-10-25 09:32:10.153308
# Unit test for function islurp

# Generated at 2026-10-25 09:32:12.567040
# Unit test for function islurp

# Generated at 2026-10-25 09:32:14.981345
# Unit test for function burp

# Generated at 2026-10-25 09:32:17.396876
# Unit test for function burp

# Generated at 2026-10-25 09:32:19.813152
# Unit test for function burp

# Generated at 2026-10-25 09:32:22.229294
# Unit test for function islurp

# Generated at 2026-10-25 09:32:24.645734
# Unit test for function islurp

# Generated at 2026-10-25 09:32:27.058650
# Unit test for function islurp

# Generated at 2026-10-25 09:32:29.472766
# Unit test for function islurp

# Generated at 2026-10-25 09:32:31.888488
# Unit test for function islurp

# Generated at 2026-10-25 09:32:34.303037
# Unit test for function islurp

# Generated at 2026-10-25 09:32:36.718166
# Unit test for function islurp

# Generated at 2026-10-25 09:32:39.131713
# Unit test for function islurp

# Generated at 2026-10-25 09:32:41.710730
# Unit test for function islurp

# Generated at 2026-10-25 09:32:44.124880
# Unit test for function islurp

# Generated at 2026-10-25 09:32:46.543218
# Unit test for function islurp

# Generated at 2026-10-25 09:32:48.954915
# Unit test for function islurp

# Generated at 2026-10-25 09:32:51.368069
# Unit test for function burp

# Generated at 2026-10-25 09:32:53.782581
# Unit test for function burp

# Generated at 2026-10-25 09:32:56.196477
# Unit test for function burp

# Generated at 2026-10-25 09:32:58.611612
# Unit test for function burp

# Generated at 2026-10-25 09:33:01.028554
# Unit test for function burp

# Generated at 2026-10-25 09:33:03.440576
# Unit test for function burp

# Generated at 2026-10-25 09:33:05.854111
# Unit test for function burp

# Generated at 2026-10-25 09:33:08.337864
# Unit test for function burp

# Generated at 2026-10-25 09:33:10.756848
# Unit test for function burp

# Generated at 2026-10-25 09:33:13.659796
# Unit test for function islurp

# Generated at 2026-10-25 09:33:15.999466
# Unit test for function islurp

# Generated at 2026-10-25 09:33:18.410477
# Unit test for function islurp