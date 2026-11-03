

# Generated at 2026-11-02 17:58:57.697964
# Unit test for function burp

# Generated at 2026-11-02 18:00:32.050302
# Unit test for function burp
def test_burp():
    with tempfile.TemporaryDirectory() as tmpdir:
        # basic text write
        path = os.path.join(tmpdir, 'out.txt')
        module_0.burp(path, 'hello world\n')
        with open(path, 'r') as fh:
            assert fh.read() == 'hello world\n'

        # binary mode
        binpath = os.path.join(tmpdir, 'out.bin')
        module_0.burp(binpath, b'\x00\x01\x02', mode='wb')
        with open(binpath, 'rb') as fh:
            assert fh.read() == b'\x00\x01\x02'

        # append mode
        apath = os.path.join(tmpdir, 'append.txt')
        module_0.burp(apath, 'a')
        module_0.burp(apath, 'b', mode='a')
        with open(apath, 'r') as fh:
            assert fh.read() == 'ab'

        # stdout mode via '-'
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        module_0.burp('-', 'stdout test\n')
        captured = sys.stdout.getvalue()
        sys.stdout = old_stdout
        assert captured == 'stdout test\n'

        # expandvars
        os.environ['BURP_TEST_VAR'] = tmpdir
        vpath = os.path.join(tmpdir, 'env.txt')
        module_0.burp('$BURP_TEST_VAR/env.txt', 'env contents')
        with open(vpath, 'r') as fh:
            assert fh.read() == 'env contents'

# Generated at 2026-11-02 18:04:45.672058
# Unit test for function islurp