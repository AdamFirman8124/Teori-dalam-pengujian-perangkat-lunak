

# Generated at 2026-10-25 12:27:39.844655
# Unit test for function burp
def test_burp():
    import io
    import os
    import tempfile
    from unittest import mock

    # 1. basic text write + overwrite + append
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.txt")
        module_0.burp(path, "hello world")

# Generated at 2026-10-25 12:27:58.072111
# Unit test for function burp
def test_burp():
    import io
    import os
    import tempfile
    from unittest import mock

    # 1. basic text write + overwrite + append
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.txt")
        module_0.burp(path, "hello world")

# Generated at 2026-10-25 12:28:20.089034
# Unit test for function burp
def test_burp():
    import io
    import os
    import tempfile
    from unittest import mock

    # 1. basic text write + overwrite + append
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.txt")
        module_0.burp(path, "hello world")

# Generated at 2026-10-25 12:28:42.923374
# Unit test for function islurp

# Generated at 2026-10-25 12:29:42.301695
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:29:43.939653
# Unit test for function burp
def test_burp():
    import io
    import os
    import tempfile
    from unittest import mock

    # 1. basic text write + overwrite + append
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.txt")
        module_0.burp(path, "hello world")

# Generated at 2026-10-25 12:29:46.998650
# Unit test for function islurp

# Generated at 2026-10-25 12:29:49.412796
# Unit test for function islurp

# Generated at 2026-10-25 12:29:52.082771
# Unit test for function islurp

# Generated at 2026-10-25 12:29:54.501218
# Unit test for function burp

# Generated at 2026-10-25 12:30:08.015075
# Unit test for function burp
def test_burp():import os

# Generated at 2026-10-25 12:30:10.976267
# Unit test for function islurp

# Generated at 2026-10-25 12:30:12.508662
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:30:40.169353
# Unit test for function islurp

# Generated at 2026-10-25 12:31:18.672862
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:32:23.585312
# Unit test for function islurp

# Generated at 2026-10-25 12:32:25.131291
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:33:13.130348
# Unit test for function islurp

# Generated at 2026-10-25 12:33:14.681736
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:33:16.147653
# Unit test for function burp
def test_burp():
    import io
    import os
    import tempfile
    from unittest import mock

    # 1. basic text write + overwrite + append
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.txt")
        module_0.burp(path, "hello world")

# Generated at 2026-10-25 12:33:19.700890
# Unit test for function islurp

# Generated at 2026-10-25 12:33:34.870131
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

# Generated at 2026-10-25 12:33:38.188973
# Unit test for function islurp

# Generated at 2026-10-25 12:33:59.791868
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

# Generated at 2026-10-25 12:34:02.204711
# Unit test for function burp

# Generated at 2026-10-25 12:34:04.618362
# Unit test for function burp

# Generated at 2026-10-25 12:34:07.031606
# Unit test for function burp

# Generated at 2026-10-25 12:34:09.444885
# Unit test for function islurp

# Generated at 2026-10-25 12:34:11.859950
# Unit test for function islurp

# Generated at 2026-10-25 12:34:14.275448
# Unit test for function islurp

# Generated at 2026-10-25 12:34:16.688831
# Unit test for function islurp

# Generated at 2026-10-25 12:34:34.251561
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

# Generated at 2026-10-25 12:34:36.819784
# Unit test for function burp

# Generated at 2026-10-25 12:34:38.356692
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 12:34:44.708046
# Unit test for function islurp

# Generated at 2026-10-25 12:35:01.401445
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-25 12:35:03.818385
# Unit test for function islurp

# Generated at 2026-10-25 12:35:06.232718
# Unit test for function islurp

# Generated at 2026-10-25 12:35:08.647223
# Unit test for function islurp

# Generated at 2026-10-25 12:35:11.059737
# Unit test for function islurp

# Generated at 2026-10-25 12:35:13.472409
# Unit test for function islurp

# Generated at 2026-10-25 12:35:15.886316
# Unit test for function islurp

# Generated at 2026-10-25 12:35:18.299509
# Unit test for function burp

# Generated at 2026-10-25 12:35:20.714162
# Unit test for function burp

# Generated at 2026-10-25 12:35:23.127333
# Unit test for function burp

# Generated at 2026-10-25 12:35:25.542172
# Unit test for function burp

# Generated at 2026-10-25 12:35:27.954592
# Unit test for function burp

# Generated at 2026-10-25 12:35:30.366937
# Unit test for function burp

# Generated at 2026-10-25 12:35:32.781465
# Unit test for function islurp

# Generated at 2026-10-25 12:35:37.042700
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

# Generated at 2026-10-25 12:35:38.464904
# Unit test for function burp

# Generated at 2026-10-25 12:35:40.000716
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-25 12:35:43.622595
# Unit test for function islurp

# Generated at 2026-10-25 12:35:45.150381
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

# Generated at 2026-10-25 12:35:55.566965
# Unit test for function islurp

# Generated at 2026-10-25 12:36:04.063007
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

# Generated at 2026-10-25 12:36:06.730108
# Unit test for function islurp

# Generated at 2026-10-25 12:36:09.531542
# Unit test for function islurp

# Generated at 2026-10-25 12:36:12.116400
# Unit test for function islurp

# Generated at 2026-10-25 12:36:14.531459
# Unit test for function islurp

# Generated at 2026-10-25 12:36:16.944366
# Unit test for function islurp

# Generated at 2026-10-25 12:36:19.357766
# Unit test for function islurp

# Generated at 2026-10-25 12:36:21.772254
# Unit test for function islurp

# Generated at 2026-10-25 12:36:24.184411
# Unit test for function islurp

# Generated at 2026-10-25 12:36:26.597244
# Unit test for function islurp

# Generated at 2026-10-25 12:36:29.011173
# Unit test for function burp

# Generated at 2026-10-25 12:36:31.425349
# Unit test for function burp

# Generated at 2026-10-25 12:36:34.108692
# Unit test for function burp

# Generated at 2026-10-25 12:36:36.524188
# Unit test for function burp

# Generated at 2026-10-25 12:36:38.939511
# Unit test for function burp

# Generated at 2026-10-25 12:36:41.352256
# Unit test for function burp

# Generated at 2026-10-25 12:36:43.765750
# Unit test for function burp

# Generated at 2026-10-25 12:36:46.180008
# Unit test for function burp

# Generated at 2026-10-25 12:36:48.596922
# Unit test for function burp

# Generated at 2026-10-25 12:36:51.012834
# Unit test for function islurp

# Generated at 2026-10-25 12:36:53.453408
# Unit test for function islurp

# Generated at 2026-10-25 12:36:55.839179
# Unit test for function islurp

# Generated at 2026-10-25 12:36:58.252854
# Unit test for function islurp

# Generated at 2026-10-25 12:37:00.669428
# Unit test for function islurp

# Generated at 2026-10-25 12:37:17.484154
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

# Generated at 2026-10-25 12:37:34.791182
# Unit test for function burp

# Generated at 2026-10-25 12:37:36.218470
# Unit test for function burp
def test_burp():import tempfile