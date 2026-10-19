

# Generated at 2022-06-13 16:10:06.985242
# Unit test for function checksum
def test_checksum():
    '''Unit test for function checksum'''

    test_file = 'test/files/changeme'
    with open(test_file, 'w') as f:
        f.write('#pw+cT/MjZbwd2e1E3rqjmQ==')
    csum = checksum(test_file)
    os.remove(test_file)
    assert csum == '5a828376f5c24d5e5df2037b1f35daa5a5c5d49b'



# Generated at 2022-06-13 16:10:13.524104
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    m = md5s("hello world")
    print("md5s: ", m)
    if m != "5EB63BBBE01EEED093CB22BB8F5ACDC3":
        raise ValueError("md5s is wrong")

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:10:14.187447
# Unit test for function checksum
def test_checksum():
    pass

# Generated at 2022-06-13 16:10:16.886546
# Unit test for function checksum
def test_checksum():
    import tempfile

    (result_fd, result_file) = tempfile.mkstemp()
    file_test = '''test_file
test_file_2
test_file_3
test_file_4
'''

    with os.fdopen(result_fd, "wb") as r:
        r.write(file_test)

    if checksum(result_file) == secure_hash(result_file):
        return True
    else:
        return False

# Generated at 2022-06-13 16:10:19.135516
# Unit test for function checksum
def test_checksum():
    assert secure_hash('test/unit/module_utils/test_utils.py') == '01c5f07fd8e9a5d6e5d5c534eba5390d0e1e94d6'



# Generated at 2022-06-13 16:10:25.326417
# Unit test for function md5
def test_md5():
    s = 'hello world'
    checksum = md5s(s)
    assert checksum == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5('/etc/passwd') == '2d8b7eb590c30f18a766df634863dc4c'


# Generated at 2022-06-13 16:10:30.055533
# Unit test for function md5s
def test_md5s():
    import tempfile
    fd, fname = tempfile.mkstemp()
    fh = os.fdopen(fd, 'w')
    fh.write('t' * 10)
    fh.close()
    try:
        assert md5(fname) == 'c8a0aeea9c0b9ad9e4c0d4200d6cde58'
    finally:
        os.unlink(fname)

# Generated at 2022-06-13 16:10:35.105094
# Unit test for function checksum
def test_checksum():
    assert checksum("test/support/test.py") == 'f68a6b5e6b5a6fc5e6d4c4d17a6c28d6dbd044b0'
    assert checksum("test/support/test.py", "sha224") == 'a7aee27414d91af7ba9e9fbf0b9e0b13f55b623bb3255a3c3f8090f7a'


# Generated at 2022-06-13 16:10:42.193720
# Unit test for function md5s
def test_md5s():
    if not _md5:
        # We're in FIPS mode and we can't run this test
        return

    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'

# Generated at 2022-06-13 16:10:50.135292
# Unit test for function md5s
def test_md5s():
    ''' Test md5s '''
    if _md5:
        # Test with a simple string
        if not md5s('test string') == '1b332bf3aaf824f8d64409d31a19a964':
            raise ValueError('Test failed for md5s')

        # Test with a unicode string and with a unicode character
        if not md5s(u'test string\u2665') == '69a879b8e7d80fafc0ac47e9e058f711':
            raise ValueError('Test failed for md5s')

    # Test with a non-existing file
    try:
        md5('/usr/bin/nonexistent')
    except ValueError:
        pass
    else:
        raise ValueError('Test failed for md5')

   

# Generated at 2022-06-13 16:10:58.890631
# Unit test for function md5
def test_md5():
    current_dir = os.path.dirname(__file__)
    test_data = os.path.join(current_dir, 'unittest_data/')
    md5sum = '0cc175b9c0f1b6a831c399e269772661'
    assert md5(os.path.join(test_data, 'test1')) == md5sum

# Generated at 2022-06-13 16:11:06.977565
# Unit test for function md5
def test_md5():

    # Assume this file is in the same directory as md5sum.py
    test_file = '../lib/ansible/module_utils/basic.py'
    expected_md5 = '2c18cf0a4dcef8ac6a62eb0d0dd6f9c6'

    calculated_md5 = md5(test_file)

    assert calculated_md5 == expected_md5, \
        "Computed MD5 %s does not match the expected MD5 %s" % (calculated_md5, expected_md5)


# Generated at 2022-06-13 16:11:14.631887
# Unit test for function checksum
def test_checksum():
    assert to_bytes(checksum('ansible/test/utils/__init__.py')) == to_bytes(
        'a8cf06ee35f0cc2b7a3a3a2ffde9def948d345c7'
    )
    assert to_bytes(checksum(filename='ansible/test/utils/__init__.py')) == to_bytes(
        'a8cf06ee35f0cc2b7a3a3a2ffde9def948d345c7'
    )
    assert to_bytes(checksum(path='ansible/test/utils/__init__.py')) == to_bytes(
        'a8cf06ee35f0cc2b7a3a3a2ffde9def948d345c7'
    )
    assert to

# Generated at 2022-06-13 16:11:18.127278
# Unit test for function md5
def test_md5():
    test_file = "./test.md5"
    fp = open(test_file, "wb")
    fp.write(b'abc')
    fp.close()
    assert md5(test_file) == '900150983cd24fb0d6963f7d28e17f72'
    os.remove(test_file)


# Generated at 2022-06-13 16:11:22.143437
# Unit test for function md5
def test_md5():
    filename = "/usr/bin/python"
    hash = md5(filename)
    assert hash == "8b3a65b7c1f0a680c7fa8cf91206f7a0", "Expected hash to match"


# Generated at 2022-06-13 16:11:24.406422
# Unit test for function md5
def test_md5():
    print(secure_hash('/etc/hosts'))


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:37.006092
# Unit test for function md5
def test_md5():
    import sys
    import tempfile
    # create temporary file
    afile = tempfile.NamedTemporaryFile(delete=False)
    filename = afile.name
    hash_expected = 0x4b7e1323c4b4d32f
    # try all endianess combinations
    for i in range(4):
        # write bytes
        bytes = [(hash_expected & (0xff << (i*8))) >> (i*8)]
        afile.write(bytearray(bytes))
        # close file and re-open in read only
        afile.close()
        afile = open(filename, 'rb')
        # read bytes and calculate hash
        bytes = afile.read(1)
        hash_calculated = int(md5(filename), 16)
        # compare

# Generated at 2022-06-13 16:11:41.553100
# Unit test for function md5
def test_md5():
    data = 'hello world'
    assert md5s(data) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5(__file__) == 'b90a376f2f9d3d3c6c66b366f8741d65'


# Generated at 2022-06-13 16:11:51.317252
# Unit test for function checksum
def test_checksum():
    if checksum_s('hello', hash_func=sha1) != 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d':
        raise AnsibleError("chechsum: expected aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d, got %s" % checksum_s('hello', hash_func=sha1))
    if checksum_s('hello', hash_func=_md5) != '5d41402abc4b2a76b9719d911017c592':
        raise AnsibleError("chechsum: expected 5d41402abc4b2a76b9719d911017c592, got %s" % checksum_s('hello', hash_func=_md5))

# Generated at 2022-06-13 16:11:58.219254
# Unit test for function md5s
def test_md5s():
    if not _md5:
        print('MD5 not available.  Possibly running in FIPS mode.  Skipping test')
        return

    actual_result = md5s('foo')
    expected_result = 'acbd18db4cc2f85cedef654fccc4a4d8'
    if actual_result != expected_result:
        raise AssertionError('test_md5s() failed.  actual: %s, expected: %s' % (actual_result, expected_result))



# Generated at 2022-06-13 16:12:11.195014
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests import unittest

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
        ),
        supports_check_mode=True
    )
    path = module.params['path']

    if os.path.exists(path):
        result = checksum(path)
        module.exit_json(changed=False, ansible_facts=dict(checksum=result))
    else:
        module.fail_json(msg="File not found")


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:13.546937
# Unit test for function md5s
def test_md5s():
    data = 'test'
    res = md5s(data)
    assert res == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:12:24.379908
# Unit test for function checksum
def test_checksum():
    import tempfile
    text = '''
    hello world this is a test
    of the emergency broadcast network
    '''
    fd, path = tempfile.mkstemp()
    fh = os.fdopen(fd, 'w')
    fh.write(text)
    fh.close()
    digest = secure_hash(path)
    os.unlink(path)
    if digest != "900faffbb29f583918b32d4a3c4bb62e9aa9574f":
        raise Exception("%s != 900faffbb29f583918b32d4a3c4bb62e9aa9574f" % digest)


# Generated at 2022-06-13 16:12:31.595166
# Unit test for function checksum
def test_checksum():
    # The test itself is not very meaningful, since we know that the function works.
    # However, it allows us to detect misuse of the function (wrong parameters).
    p = os.path.join(os.path.dirname(__file__), '__init__.py')
    checksum(p)
    checksum_s('123')

# Generated at 2022-06-13 16:12:33.815674
# Unit test for function md5
def test_md5():
    filename = 'md5.py'
    assert checksum(filename) == checksum(filename)


# Generated at 2022-06-13 16:12:35.920071
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"


# Generated at 2022-06-13 16:12:41.346765
# Unit test for function checksum
def test_checksum():
    import sys
    import os
    import tempfile

    temp = tempfile.NamedTemporaryFile()
    temp.write('foo')
    temp.flush()
    temp.seek(0)
    assert checksum(temp.name) == checksum_s('foo')
    temp.close()

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:45.778646
# Unit test for function md5s
def test_md5s():
    data1 = 'test'
    data2 = 'test2'
    assert md5s(data1) == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s(data2) == '8e07b6eb08480ce7029c2a540b4c4c01'

# Generated at 2022-06-13 16:12:52.089566
# Unit test for function md5
def test_md5():
    if (_md5):
        f = open('./lib/ansible/module_utils/hashing.py','r')
        try:
            content = f.read()
        finally:
            f.close()
        assert(md5s(content) == 'faff30978a01d8f6f0a6a5a0bc1e7616')

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:58.028961
# Unit test for function md5s
def test_md5s():
    # check is md5s returns expected result
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    # check if md5s() raise ValueError if _md5 is not available
    _md5 = None
    try:
        md5s('foo')
        raise Exception('md5s() should raise ValueError if _md5 is not available')
    except ValueError:
        pass
    _md5 = md5


# Generated at 2022-06-13 16:13:02.204134
# Unit test for function md5s
def test_md5s():
    string = 'Hello World!'
    hash_string = '0a4d55a8d778e5022fab701977c5d840bbc486d0'
    assert md5s(string) == hash_string
    return True


# Generated at 2022-06-13 16:13:07.336747
# Unit test for function md5
def test_md5():
    assert md5("/etc/passwd") == "6b9cd9ed8d79e75c2c7f6bf800f96a8a"
    assert md5("/etc/files_that_do_not_exist") is None
    assert md5("/etc/") is None



# Generated at 2022-06-13 16:13:11.240054
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:13:17.527957
# Unit test for function md5
def test_md5():
    data = b"hello world"
    expected = b'5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert(md5s(data) == expected)
    assert(md5s(to_bytes(data, errors='surrogate_or_strict')) == expected)


if __name__ == '__main__':

    # FIXME: this should be in an automated test, not in this file
    # test md5s
    test_md5()

# Generated at 2022-06-13 16:13:22.303414
# Unit test for function md5
def test_md5():
    import tempfile
    fd, name = tempfile.mkstemp()
    expected = 'd41d8cd98f00b204e9800998ecf8427e'
    actual = md5(name)
    assert expected == actual
    os.close(fd)
    os.unlink(name)

# Generated at 2022-06-13 16:13:26.231658
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    test_data = "foo"
    test_ans = md5s(test_data)
    assert test_ans == secure_hash_s(test_data, _md5)


# Generated at 2022-06-13 16:13:33.121499
# Unit test for function checksum
def test_checksum():
    test_string = 'testing123.'

    assert(checksum(test_string) == 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0')
    assert(checksum(u'testing123.') == 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0')

    # Test for the fallback case of Python 2.4
    old_sha1 = sha1
    def sha1():
        return old_sha1()
    assert(checksum(test_string) == 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0')

# Generated at 2022-06-13 16:13:39.141512
# Unit test for function md5
def test_md5():
    m = md5('/etc/passwd')
    assert m == 'c57ca1f11985e2a3f9d4ee2b2a369a31'
    m = md5s('hello')
    assert m == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:13:42.215315
# Unit test for function md5
def test_md5():
    test_file = "./test_md5.txt"
    open(test_file, 'a').close()
    calculated_md5 = md5(test_file)
    os.remove(test_file)
    assert calculated_md5 == 'd41d8cd98f00b204e9800998ecf8427e', calculated_md5

# Generated at 2022-06-13 16:13:49.640874
# Unit test for function checksum
def test_checksum():
    if not os.path.exists('/tmp/test_checksum_1'):
        os.mkdir('/tmp/test_checksum_1')
    f = open('/tmp/test_checksum_1/test_checksum_2', 'w')
    f.write('hello')
    f.close()
    assert checksum('/tmp/test_checksum_1/test_checksum_2') == '5d41402abc4b2a76b9719d911017c592'
    os.remove('/tmp/test_checksum_1/test_checksum_2')
    os.rmdir('/tmp/test_checksum_1')

# Generated at 2022-06-13 16:13:58.436507
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'
        assert md5s(u'hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    else:
        try:
            md5s(b'hello')
        except ValueError:
            pass
        else:
            assert False, 'The md5 should be disabled under FIPS mode'


# Generated at 2022-06-13 16:14:05.375701
# Unit test for function md5
def test_md5():
    '''ansible all -i inventory -m raw -a "python -c 'import os; import sys; import hashlib; print os.path.exists(\"/etc/ansible/hosts\"); sys.exit(0)'"'''
    import os
    import sys
    import hashlib
    assert os.path.exists("/etc/ansible/hosts")

# Generated at 2022-06-13 16:14:12.036734
# Unit test for function md5
def test_md5():
    '''
    Ensure that md5 works on a known file
    '''
    import sys
    cur_file = os.path.abspath(__file__)
    cur_file_md5 = '55876a7c43f5ced5a5a07a56932de7cc'
    if md5(cur_file) != cur_file_md5:
        sys.exit(1)
    else:
        print('Successfully verified md5 of %s' % cur_file)


# Generated at 2022-06-13 16:14:14.583274
# Unit test for function md5s
def test_md5s():
    md5s_result = md5s("A test string")
    assert md5s_result == "d6c35a6f0f827e825b0a32b05a233762"


# Generated at 2022-06-13 16:14:17.213882
# Unit test for function md5s
def test_md5s():
    md5s_test = md5s('test')
    assert md5s_test == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:14:19.046845
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == '5c5d73ee5f1f16bac3f57a17f68d7073'


# Generated at 2022-06-13 16:14:29.746639
# Unit test for function md5
def test_md5():
    from random import randint
    from tempfile import mkstemp
    import os

    fd, fname = mkstemp()
    os.write(fd, "12345")
    os.close(fd)

    try:
        assert md5(fname) == "827ccb0eea8a706c4c34a16891f84e7b"
    finally:
        os.unlink(fname)


if __name__ == '__main__':
    import sys
    import os.path

    if len(sys.argv) < 2:
        print("usage: %s <file>" % os.path.basename(sys.argv[0]))
        sys.exit(0)

    print("sha1sum:     %s" % checksum(sys.argv[1]))



# Generated at 2022-06-13 16:14:32.906584
# Unit test for function md5s
def test_md5s():
    assert md5s('test message') == '6f8db599de986fab7a21625b7916589c'

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 16:14:40.920347
# Unit test for function md5s
def test_md5s():
    if _md5:
        # md5 is always 128 bits or 16 bytes
        assert len(md5s('hello')) == 16*2
        assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
        assert md5s(u'hello') == '5d41402abc4b2a76b9719d911017c592'
        assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:14:44.233533
# Unit test for function md5s
def test_md5s():
   assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:14:54.370955
# Unit test for function checksum
def test_checksum():
    ''' test checksum functionality '''

    test_string = 'hi my name is jay and I am testing.'
    assert checksum_s(test_string) == '34b831e2284f982d2f7b30c0b9da7ff33e0e5f62'

    try:
        md5
    except NameError:
        print('md5 checksum unavailable')
    else:
        assert md5(__file__) == '3c3aec5c1e29e5b9b1ebc39a78d6a38a'

# Generated at 2022-06-13 16:14:59.952428
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert md5s("hello\n") == "e2c2b70c9d7916ef8e6b9a95a4ee4c4f"
    assert md5s("hello\n\n") == "8e8e29f4afd06e4e4c4e4b44a4b44d3b"

# Generated at 2022-06-13 16:15:09.069648
# Unit test for function md5s
def test_md5s():
    import hashlib
    # Test with a string
    s = "Hello world!\n"
    assert md5s(s) == hashlib.md5(s).hexdigest()
    # Test with a unicode string
    s = u"Hello world!\n"
    assert md5s(s) == hashlib.md5(s.encode('utf8')).hexdigest()
    # Test with a unicode string with non-ascii characters
    s = u"Hello world with UTF-8 character äöü\n"
    assert md5s(s) == hashlib.md5(s.encode('utf8')).hexdigest()

# Generated at 2022-06-13 16:15:13.297466
# Unit test for function md5
def test_md5():
    import tempfile
    nfd, nfn = tempfile.mkstemp()
    with open(nfn, 'w') as f:
        f.write('hello')
    assert md5(nfn) == '5d41402abc4b2a76b9719d911017c592'
    os.close(nfd)
    os.unlink(nfn)

# Generated at 2022-06-13 16:15:17.360622
# Unit test for function md5
def test_md5():
    import tempfile
    with tempfile.NamedTemporaryFile(prefix='ansible-test-', delete=False) as tf:
        tf.write(b'hello')

    try:
        assert(md5(tf.name) == '5d41402abc4b2a76b9719d911017c592')
    finally:
        os.unlink(tf.name)

# Generated at 2022-06-13 16:15:26.466454
# Unit test for function md5
def test_md5():
    from ansible.compat.six import StringIO
    b_data = b"my string to hash\n"
    a_data = b_data.decode('utf-8')
    md5_hash = md5(StringIO(b_data))
    md5_hash_s = md5s(a_data)
    assert md5_hash == "2c5e5e5f5bcf0dc115a55bf3f3f0bd24"
    assert md5_hash_s == "2c5e5e5f5bcf0dc115a55bf3f3f0bd24"


# Generated at 2022-06-13 16:15:36.650029
# Unit test for function checksum
def test_checksum():
    '''
    ansible core.utils.checksum
    '''
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock, mock_open

    class TestChecksum(unittest.TestCase):

        @patch('os.path.exists')
        @patch('os.path.isdir')
        def test_checksum_with_no_file(self, isdir, exists):
            ''' checksum should return None for a non-existent file '''
            exists.return_value = False
            isdir.return_value = False

            result = checksum('foo')
            self.assertEqual(None, result)


# Generated at 2022-06-13 16:15:38.881841
# Unit test for function md5
def test_md5():
    assert(md5(__file__) == "d3f3a2217fa3f46eb7d84861f1bd7f44")


# Generated at 2022-06-13 16:15:44.846801
# Unit test for function md5
def test_md5():
    assert(md5('test/test_utils/test_checksum.py') == '6fd9d6247d4b2f3b139a8ba8c27e33d1')
    assert(md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3')

# Generated at 2022-06-13 16:15:49.060892
# Unit test for function md5
def test_md5():
    md5_txt = 'foo'
    assert(md5_txt == 'acbd18db4cc2f85cedef654fccc4a4d8')
    assert(md5s(md5_txt) == 'acbd18db4cc2f85cedef654fccc4a4d8')


# Generated at 2022-06-13 16:15:52.572480
# Unit test for function md5
def test_md5():
    md5('/bin/ls')


# Generated at 2022-06-13 16:15:54.931982
# Unit test for function md5s
def test_md5s():
    result = md5s("test")
    assert result == "098f6bcd4621d373cade4e832627b4f6"


# Generated at 2022-06-13 16:15:57.778215
# Unit test for function md5s
def test_md5s():
    ''' md5s() with md5 hash'''
    data = 'Hello World!'
    assert md5s(data) == 'ed076287532e86365e841e92bfc50d8c'


# Generated at 2022-06-13 16:16:00.904659
# Unit test for function md5
def test_md5():
    """Test custom md5 function"""
    import md5
    md5_hash = md5.new()
    md5_hash.update("Ansible")
    assert md5s("Ansible") == md5_hash.hexdigest()


# Generated at 2022-06-13 16:16:06.418551
# Unit test for function md5
def test_md5():
    "sha1 hashlib test"
    data = 'test'
    s = md5s(data)
    assert s == "098f6bcd4621d373cade4e832627b4f6", "Failed"

#####################################################################
# For testing
if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:11.760534
# Unit test for function md5
def test_md5():
    import os
    import tempfile

    # Create a temp file
    (fd, fn) = tempfile.mkstemp()
    os.write(fd, "test")
    os.close(fd)

    try:
        m = md5(fn)
    finally:
        # Remove the temp file
        os.unlink(fn)

    assert(m == "098f6bcd4621d373cade4e832627b4f6")

# Generated at 2022-06-13 16:16:18.561692
# Unit test for function md5
def test_md5():
    md5_test_file = os.path.join(os.getcwd(), 'test/sanity/test_support/test_templates/unix_file1.j2')
    assert md5(md5_test_file) == '771df7e73a1a1cc7f0fd8f29918d9b3b'


if __name__ == "__main__":
    test_md5()
    print("Successfully completed")

# Generated at 2022-06-13 16:16:20.486857
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:16:23.780481
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:16:32.062114
# Unit test for function md5
def test_md5():
    ''' md5 : validate md5 function from ansible'''
    from ansible.compat.tests import unittest
    import ansible.utils.crypto as crypto_utils

    class TestMd5(unittest.TestCase):
        ''' validate md5 function from ansible '''

        def test_md5s(self):
            ''' validate md5s function from ansible '''
            self.assertEqual(crypto_utils.md5s('test'), '098f6bcd4621d373cade4e832627b4f6')

        def test_md5(self):
            ''' validate md5 function from ansible '''

# Generated at 2022-06-13 16:16:40.769075
# Unit test for function checksum
def test_checksum():
    data = bytes("foobar")
    assert checksum_s(data) == "8843d7f92416211de9ebb963ff4ce28125932878"
    assert checksum(os.path.dirname(__file__) + "/test_utils.py") == "8843d7f92416211de9ebb963ff4ce28125932878"

# Generated at 2022-06-13 16:16:43.302131
# Unit test for function md5s
def test_md5s():
    '''
    Test md5s
    '''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(required=True),
        ),
    )
    result = md5s(module.params['data'])
    module.exit_json(changed=True, diff={'after_header': 'md5s', 'before_header': 'data', 'before': module.params['data'], 'after': result})


# Generated at 2022-06-13 16:16:45.544863
# Unit test for function md5s
def test_md5s():
    r = md5s('ansible')
    assert r == 'ab56a4d92b40713acc5af89985d4b786'


# Generated at 2022-06-13 16:16:49.283077
# Unit test for function md5s
def test_md5s():
    data = 'test'
    expected = '098f6bcd4621d373cade4e832627b4f6'
    result = md5s(data)
    assert result == expected


# Generated at 2022-06-13 16:16:54.446581
# Unit test for function md5
def test_md5():
    ''' md5 should return same value as sha1'''
    data = b"The quick brown fox jumped over the lazy dog"
    assert secure_hash_s(data) == secure_hash_s(data, md5s)


# Generated at 2022-06-13 16:16:58.333604
# Unit test for function md5s
def test_md5s():
    # Verify md5s and md5 return consistent results
    assert md5s('hello') == md5('/tmp/hello')


if __name__ == '__main__':
    # If called as a program, do unit tests
    test_md5s()

# Generated at 2022-06-13 16:17:03.826910
# Unit test for function md5
def test_md5():
    import tempfile
    import filecmp

    f = tempfile.NamedTemporaryFile()
    f.write(b"Hello World! 123\n")
    f.flush()
    fname = f.name

    md5sum = "b10a8db164e0754105b7a99be72e3fe5"
    assert md5(fname) == md5sum

    f.close()

# Generated at 2022-06-13 16:17:09.089760
# Unit test for function md5s
def test_md5s():
    assert md5s(3) == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('3') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:17:12.730851
# Unit test for function md5s
def test_md5s():
    '''test for function md5s'''

    assert md5s('hello world') == md5s(to_bytes('hello world', errors='surrogate_or_strict'))
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:17:23.601621
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum('/bin/ls') == 'd5e8a31ab71102545f57ec2b1d9d931d'
    try:
        assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
        assert md5('/bin/ls') == 'd5e8a31ab71102545f57ec2b1d9d931d'
    except ValueError:
        pass

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:17:33.354454
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, mock_open

    class TestUtils(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_md5_colon_separated(self):
            s = md5s('asdf')
            self.assertTrue(s.startswith('90015098'))

        @patch('ansible.utils.md5.open', mock_open(), create=True)
        def test_colon_separated_filename(self):
            s = md5('/tmp/foo')
            self.assertTrue(s.startswith('90015098'))


# Generated at 2022-06-13 16:17:45.110762
# Unit test for function md5s
def test_md5s():

    if not _md5:
        return None

    assert md5s('') == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s('a') == "0cc175b9c0f1b6a831c399e269772661"
    assert md5s('abc') == "900150983cd24fb0d6963f7d28e17f72"
    assert md5s('message digest') == "f96b697d7cb7938d525a2f31aaf161d0"
    assert md5s('abcdefghijklmnopqrstuvwxyz') == "c3fcd3d76192e4007dfb496cca67e13b"

# Generated at 2022-06-13 16:17:49.421147
# Unit test for function md5s
def test_md5s():
    my_md5_1 = md5s('mydata')
    my_md5_2 = md5s('mydata')
    assert my_md5_1 == my_md5_2

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-13 16:17:51.401427
# Unit test for function md5
def test_md5():
    assert md5s(b'asdfasdf') == '912ec803b2ce49e4a541068d495ab570'



# Generated at 2022-06-13 16:17:54.716621
# Unit test for function md5
def test_md5():
    assert md5("/bin/false") == "3b37c81111bd254c5d07ffb25a348b6c"

# Generated at 2022-06-13 16:17:57.941319
# Unit test for function md5
def test_md5():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5(__file__) == md5s(open(__file__,'rb').read())



# Generated at 2022-06-13 16:18:02.368236
# Unit test for function md5
def test_md5():
    b = b'hello world'
    h = '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s(b) == h

# Backwards compat only
hexdigest = checksum_s

# Generated at 2022-06-13 16:18:10.799351
# Unit test for function checksum
def test_checksum():
    from os.path import dirname, join

    file = join(dirname(__file__), 'hashtest')
    assert checksum(file) == 'c104cfb2e8a0942efb48216f4d4f4b4d74f29c94'
    assert checksum_s('Hello World') == '0a4d55a8d778e5022fab701977c5d840bbc486d0'
    assert md5s('Hello World') == '65a8e27d8879283831b664bd8b7f0ad4'
    assert md5(file) == '6a5b8e073618c7a6a8b6a7b8130072c1'

# Generated at 2022-06-13 16:18:19.707340
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:18:32.061624
# Unit test for function md5
def test_md5():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import tempfile

    # Create a temporary file
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'wb') as tmp:
        tmp.write(b"ansible")
    # Calculate its md5 sum
    m = md5(path)
    # Remove it
    os.unlink(path)

    assert(type(md5s("ansible")) is str)
    assert(type(md5("ansible")) is str)

    assert(type(md5s(u"ansible")) is str)
    assert(type(m) is str)
    assert(type(md5s(b"ansible")) is str)
    assert(type(md5(b"ansible")) is str)

   

# Generated at 2022-06-13 16:18:37.771884
# Unit test for function md5
def test_md5():
    d = "test string"
    md5_test1 = md5s(d)
    md5_test2 = md5(__file__)

    assert md5_test1 == "5f873c2d0d8e3a41f9cc9f486324e0b3"
    assert md5_test2 is not None

# Generated at 2022-06-13 16:18:41.369824
# Unit test for function md5s
def test_md5s():
    data = 'This is a test'
    expected = 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0'
    h = md5s(data)
    print("Testing md5s(%s)" % data)
    print("Expected (%s) Got (%s)" % (expected, h))
    assert h == expected


# Generated at 2022-06-13 16:18:52.191599
# Unit test for function md5
def test_md5():
    assert md5s(u'hello world') == u'5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s(u'hello world!') == u'4b6f859eb67b0d05b0c1b84a49d8a072'
    assert md5s(u'HELLO WORLD') == u'7cdda3bf3d7c81d0f00a7b3acbdf3e3a'
    assert md5s(u'HELLO WORLD!') == u'101f7ff74b9c5b5fb873e8de2d7fce69'

# Generated at 2022-06-13 16:18:58.466173
# Unit test for function md5s
def test_md5s():
    ansible_md5 = md5s("ansible")
    if ansible_md5 != "3d1049eb7a2a40d75dd7b8c9a08aa7ff":
        raise Exception("Test for function md5s failed: %s" % ansible_md5)


# Generated at 2022-06-13 16:19:07.816487
# Unit test for function checksum
def test_checksum():
    assert checksum('lib/ansible/module_utils/urls.py') == 'a5d8101d9b80e8fe6ce3c3ceb5a39b0784c4496f'
    assert checksum_s('a test string') == '65a8e27d8879283831b664bd8b7f0ad4'
    assert checksum_s(u'a test string') == '65a8e27d8879283831b664bd8b7f0ad4'

# Generated at 2022-06-13 16:19:17.079787
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest

    class TestModuleUtilsChecksum(unittest.TestCase):
        def test_returns_none_for_missing_file(self):
            self.assertIsNone(checksum('/no/such/file/here'))

        def test_returns_none_for_directory(self):
            self.assertIsNone(checksum('.'))

        def test_returns_none_for_file_with_no_read_access(self):
            self.assertIsNone(checksum('/dev/kmsg'))

        def test_returns_proper_value_for_file(self):
            self.assertEqual('acbd18db4cc2f85cedef654fccc4a4d8', checksum(__file__))


# Generated at 2022-06-13 16:19:20.958207
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, filename) = tempfile.mkstemp(prefix='ansible_unit_test')
    os.write(fd, 'test')
    os.close(fd)
    assert(md5(filename) == '098f6bcd4621d373cade4e832627b4f6')
    os.remove(filename)

# Generated at 2022-06-13 16:19:23.982879
# Unit test for function checksum
def test_checksum():
    assert checksum_s('foo', hash_func=sha1) == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert checksum_s('foo', hash_func=_md5) == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:19:33.828032
# Unit test for function md5s
def test_md5s():
    import unittest

    class TestMd5s(unittest.TestCase):
        md5_result = md5s('ansible')
        secure_hash_s_result = secure_hash_s('ansible')
        secure_hash_s_result_with_md5 = secure_hash_s('ansible', _md5)

        def test_md5s_with_md5(self):
            self.assertEqual(self.md5_result, 'edfb5d8e1e3359778c3e3b74f4cfbaf4')


# Generated at 2022-06-13 16:19:41.309906
# Unit test for function md5s
def test_md5s():
    import sys

    def sha256s(value):
        import hashlib
        m = hashlib.sha256()
        m.update(value)
        return m.hexdigest()

    if sys.version_info >= (2, 5):
        assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
        assert md5s(b'hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
        assert sha256s(b'test value') == '0f4d6d4bb0ff0c06f4eb4b7e1e0fbee9a9c9b2f0786f7d775a8de1a93510019c'

# Generated at 2022-06-13 16:19:44.814674
# Unit test for function checksum
def test_checksum():
    filename = '/etc/passwd'
    value = secure_hash(filename)
    assert value is not None

# Generated at 2022-06-13 16:19:48.047740
# Unit test for function md5
def test_md5():
    rval = md5("/etc/motd")
    assert rval == "d41d8cd98f00b204e9800998ecf8427e"

# Generated at 2022-06-13 16:19:50.957157
# Unit test for function checksum
def test_checksum():
    assert checksum("/bin/ls") == "2a3ecb654f3e6c912d35f2f3cbf6eeb3238d527a"


# Generated at 2022-06-13 16:19:52.554301
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:19:55.511722
# Unit test for function md5
def test_md5():
    assert md5('lib/ansible/module_utils/hashivault.py') == md5s('lib/ansible/module_utils/hashivault.py')
    assert md5(None) == None
    assert md5s(None) == None
