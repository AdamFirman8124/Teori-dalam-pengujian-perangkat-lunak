

# Generated at 2022-06-13 16:10:13.406854
# Unit test for function checksum
def test_checksum():
    '''
    secure_hash checksum function test
    '''
    path = os.path.dirname(__file__)

    sample_data = u'hello'
    sample_md5s = '5d41402abc4b2a76b9719d911017c592'
    sample_md5 = '5d41402abc4b2a76b9719d911017c592'
    sample_sha1 = 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    sample_sha256 = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

    assert checksum_s(sample_data) == sample_sha1

# Generated at 2022-06-13 16:10:20.678850
# Unit test for function checksum
def test_checksum():
    if checksum("/dev/null") != "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e":
        raise ValueError("checksum function failed for file /dev/null")


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:10:29.997715
# Unit test for function checksum
def test_checksum():
    '''
    File and path creation for test_checksum
    
    File1:
        file1.sha1: b2cba4b6a4d1a4e4d4b1c35b7309fb2c77dbd845
        file1.md5: 29c11d199b8a578335334c9a3a3a24eb
    
     File2:
        file2.sha1: e2ad80e8a2a9f54420e1de98dbb8d8b05eafb1a1
        file2.md5: 5c635e8e1d9c9a57dcce2c09b371dbcb
    '''

    path = '/tmp/ansible_checksum' 
    filename = 'file1'
    

# Generated at 2022-06-13 16:10:37.489683
# Unit test for function md5
def test_md5():
    # Code
    def do_test_md5(plain, encrypted):
        assert md5s(plain) == encrypted, 'Failed md5s test'
        assert md5s(plain) == encrypted, 'Failed md5 test'

    # Tests
    do_test_md5('', 'd41d8cd98f00b204e9800998ecf8427e')
    do_test_md5('a', '0cc175b9c0f1b6a831c399e269772661')
    do_test_md5('b', '187ef4436122d1cc2f40dc2b92f0eba0')
    do_test_md5('c', '900150983cd24fb0d6963f7d28e17f72')
    do_test_md5

# Generated at 2022-06-13 16:10:45.434878
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.six import bytes_to_native_str
    test_string = '{"json":"obj"}'
    test_sum_string = 'e1a0e56cbf394bdbc40f21b38d9c4b4e4f04d78b'
    test_sum = checksum_s(test_string)
    assert test_sum == test_sum_string, "test_checksum_s() failed"
    assert isinstance(test_sum, bytes_to_native_str)
    test_sum = checksum('./test/utils/test_checksum.py')
    assert test_sum == test_sum_string, "test_checksum() failed"

if __name__ == "__main__":
    test_checksum()

# Generated at 2022-06-13 16:10:47.207306
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f"


# Generated at 2022-06-13 16:10:58.984414
# Unit test for function md5
def test_md5():
    import tempfile
    import unittest

    tfh, tf = tempfile.mkstemp()

    # Test for empty file
    with open(tf, 'w') as f:
        f.write('')
    if os.path.isfile(tf):
        tf_md5 = md5(tf)
        if sys.version_info >= (2, 7):
            tf_md5_v2_7 = 'd41d8cd98f00b204e9800998ecf8427e'
            self.assertEqual(tf_md5, tf_md5_v2_7)
        tf_md5_v2_6 = 'c9148c8a7d81050d2a61bde1ceb3efc7'

# Generated at 2022-06-13 16:11:03.400072
# Unit test for function md5s
def test_md5s():
    "md5s"
    import random
    x = str(random.random())
    y = md5s(x)
    z = "63b9d9c1e3d7d8bbb5d420c5ec24d5e5"
    assert(y == z)



# Generated at 2022-06-13 16:11:07.561105
# Unit test for function checksum
def test_checksum():
    assert checksum("../lib/ansible/module_utils/basic.py") == "1c216d1644d0ff933dbbe0fbe253c08866d8628c"
    assert checksum_s("foo") == "0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33"

# Generated at 2022-06-13 16:11:18.561809
# Unit test for function checksum
def test_checksum():
    ''' test the checksum function.  Warning: if using system md5, this test
    case will fail, as it tries to use sha1 '''
    tmpfile = os.path.join('testdir', 'testfile')
    os.makedirs(os.path.dirname(tmpfile))
    fh = open(to_bytes(tmpfile, errors='surrogate_or_strict'), 'wb')
    try:
        fh.write(b"test1")
    finally:
        fh.close()
    shasum = checksum(tmpfile)
    assert shasum == '78843c12bdb6b71b77f4a06ffc24e0f6c63a41e4', 'sha1 failed'
    os.unlink(tmpfile)
    shasum = checks

# Generated at 2022-06-13 16:11:23.930608
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:11:34.905058
# Unit test for function md5
def test_md5():
    import os
    import shutil
    import tempfile
    import ansible.utils.path
    test_file_name = 'test.txt'
    test_file_path = os.path.join(tempfile.mkdtemp(), test_file_name)
    test_content = "This is a test"
    open(test_file_path, 'w').write(test_content)
    assert md5(test_file_path) == 'c4a46959e6c1c6e9d6b07e6d0f6b1711'
    shutil.rmtree(os.path.dirname(test_file_path))



# Generated at 2022-06-13 16:11:41.187065
# Unit test for function checksum
def test_checksum():
    import tempfile

    (fd, filename) = tempfile.mkstemp(prefix='ansible-test-checksum')
    f = os.fdopen(fd, 'wb')
    f.write(b"random data")
    f.close()

    sha = checksum(filename)
    os.remove(filename)
    print("sha1 = %s\n" % sha)
    return

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:11:42.553328
# Unit test for function checksum
def test_checksum():
    assert checksum('0', checksum_s('0')) == '0'

# Generated at 2022-06-13 16:11:45.542471
# Unit test for function md5s
def test_md5s():
    old = md5s('Test123')
    new = secure_hash_s(b'Test123')
    assert old == new, 'MD5 hashes do not match'


# Generated at 2022-06-13 16:11:49.764058
# Unit test for function md5s
def test_md5s():
    test_string = "TestString"
    test_string_md5 = "41b10fde5d5ddd90baa5fe853bab1d5e"
    if md5s(test_string) != test_string_md5:
        raise Exception("secure_hash_s() failed with md5")


# Generated at 2022-06-13 16:12:01.019295
# Unit test for function checksum
def test_checksum():
    assert checksum("/etc/passwd") == "9ad31f962da0f1eae53c8f4cc193c4e4e9a4b90a"
    assert checksum("/etc/shadow") == "37a3d3646080b908e9fbbcc19f2a0b7d"
    assert checksum("/etc/shadow-") is None
    assert checksum("/etc") is None
    assert checksum_s("hello world") == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"
    assert checksum_s("hello worl") == "0a987a0e3b9ab813143020d9df55b275"

# Generated at 2022-06-13 16:12:04.292560
# Unit test for function md5s
def test_md5s():
    import pytest

    with pytest.raises(ValueError):
        # Test that we cannot use md5 in FIPS mode
        md5s('test')

# Generated at 2022-06-13 16:12:07.010339
# Unit test for function md5
def test_md5():
    assert md5("/bin/false") == "d7bbe8f92e0f57ba6777f9e78f90d20a"


# Generated at 2022-06-13 16:12:10.237803
# Unit test for function checksum
def test_checksum():
    assert checksum('test/ansible/utils/test_module_utils/mkfifo.py') == '8c3a1d6dbfdae36da5e6a82a6f3cb7ab09539e3d'

# Generated at 2022-06-13 16:12:24.035499
# Unit test for function md5
def test_md5():
    ''' check function md5 '''
    from ansible.compat.tests import unittest

    class TestMd5(unittest.TestCase):
        ''' test md5 '''
        def test_md5(self):
            ''' make sure md5 works '''
            self.assertEqual(md5s('hello'), '5d41402abc4b2a76b9719d911017c592')
            if _md5:
                self.assertEqual(md5('/dev/null'), 'd41d8cd98f00b204e9800998ecf8427e')

    unittest.main(argv=['test_md5'], verbosity=0, exit=False)

# Generated at 2022-06-13 16:12:30.705799
# Unit test for function md5s
def test_md5s():
    print(md5s('hello'))
    print(md5s(b'hello'))
    print(md5s(u'hello'))
    print(md5s(u'hellø'))
    print(md5s(u'hell\xa7'))



# Generated at 2022-06-13 16:12:35.195068
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == 'e170b3a3a6f507f8b1237f1ff7c1b98d'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:12:39.149183
# Unit test for function checksum
def test_checksum():
    result = checksum('lib/ansible/modules/core/files/file.py')
    assert result == '1a9ed9db32fefc7a2a3b3e4d0f4ee73c39b4fea4'

# Generated at 2022-06-13 16:12:41.444887
# Unit test for function md5s
def test_md5s():
    assert(md5s('hello')) == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:12:44.775267
# Unit test for function md5
def test_md5():
    data = "foobar"
    calculated_md5 = md5s(data)
    expected_md5 = '3858f62230ac3c915f300c664312c63f'
    assert calculated_md5 == expected_md5, 'MD5 mismatch, expect %s, get %s' % (expected_md5, calculated_md5)


# Generated at 2022-06-13 16:12:50.941658
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    fpath = os.path.join(os.getcwd(), 'lib/ansible/modules/core/system/ping.py')
    assert md5(fpath) == '17fbd9e9d16b0f2848ffd343db72c0c2'



# Generated at 2022-06-13 16:12:59.902850
# Unit test for function md5s
def test_md5s():
    '''test md5s'''

    string1 = u'this is a test'
    string1_md5 = 'c74fb26208e8a83f1fabc5aa05a7b38d'
    string2 = u'this is also a test'
    string2_md5 = '0b0f7f2ef2d3f3c3af08522c295f7d1c'

    # Using a unicode string
    assert md5s(string1) == string1_md5
    assert md5_s(string1) == string1_md5

    # Using a plain string
    assert md5s(string1.encode('utf-8')) == string1_md5
    assert md5_s(string1.encode('utf-8')) == string1_md5

   

# Generated at 2022-06-13 16:13:02.551590
# Unit test for function md5
def test_md5():
    s = "hello world"
    assert md5s(s) == 'ed076287532e86365e841e92bfc50d8c'

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:13:07.186083
# Unit test for function md5s
def test_md5s():
    output_1 = md5s('TestString1')
    output_2 = md5s('TestString2')
    assert(output_1 != output_2)

# Declaring a global variable to be used in tests
data = 'TestString1'


# Generated at 2022-06-13 16:13:15.918028
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abc') == md5s('abc')
    assert md5s('abc') != md5s('def')
    assert md5s('abc') != md5s('abcd')


# Generated at 2022-06-13 16:13:20.836937
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:13:23.611424
# Unit test for function md5
def test_md5():
    assert md5("/etc/passwd") == "931a9e00ccec8f818c450e615a32a54a"


# Generated at 2022-06-13 16:13:29.112030
# Unit test for function md5
def test_md5():
    ''' Checksum test '''

    # Create a file and test it's checksum
    import tempfile
    (fd, tfile) = tempfile.mkstemp()

    check = md5(tfile)
    assert check is not None

    os.close(fd)
    os.unlink(tfile)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:13:35.267348
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    # setup
    expected_output = 'd41d8cd98f00b204e9800998ecf8427e'
    input_data = ''

    # run the test
    output = md5s(input_data)

    # assert
    assert output == expected_output


# Generated at 2022-06-13 16:13:47.419404
# Unit test for function md5
def test_md5():
    # Ansible is running in FIPS 140-2 mode, which means that the hashlib
    # algorithm "md5" is not available.  This will raise a ValueError that
    # mimics what happens on FIPS-140-2 compliant systems.
    try:
        md5s('foo')
    except ValueError as e:
        assert "Possibly running in FIPS mode" in str(e)

    # Ansible is running in FIPS 140-2 mode, which means that the hashlib
    # algorithm "md5" is not available.  This will raise a ValueError that
    # mimics what happens on FIPS-140-2 compliant systems.
    try:
        md5('/foo/bar')
    except ValueError as e:
        assert "Possibly running in FIPS mode" in str(e)

    # Create a temporary file to

# Generated at 2022-06-13 16:13:57.340170
# Unit test for function checksum
def test_checksum():
    ''' test checksum function '''

    file1 = "./lib/ansible/module_utils/basic.py"

    if not os.path.exists(file1):
        raise Exception("file not found: %s" % file1)
    elif not os.path.isfile(file1):
        raise Exception("not a file: %s" % file1)
    else:
        chk1 = checksum(file1)
        chk2 = checksum("lib/ansible/module_utils/basic.py")
        chk3 = checksum(file1, hash_func=_md5)
        chk4 = checksum("lib/ansible/module_utils/basic.py", hash_func=_md5)

# Generated at 2022-06-13 16:14:03.771326
# Unit test for function md5
def test_md5():
    ''' md5.py: Test md5 function '''

    assert md5('lib/ansible/modules/extras/packaging/os/yum.py') == 'd710dd8c47ae1f0c27b6b0df6d828c7f'


# Generated at 2022-06-13 16:14:06.040485
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:14:15.953462
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    play_context.become = True
    play_context.become_method = 'sudo'
    play_context.become_user = 'root'
    module = AnsibleModule(
        argument_spec = dict(
            data=dict(default=None, type='str')
        ),
        supports_check_mode=True,
        check_invalid_arguments=False,
        bypass_checks=False
    )
    module.set_play_context(play_context)

    data = module.params['data']
    checksum = md5s(data)
    module.exit_json(changed=True, checksum=checksum)


# Generated at 2022-06-13 16:14:23.880314
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.basic import AnsibleModule

    def test_md5_impl(data):
        return md5s(data)

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(required=True, type='str'),
        ),
        supports_check_mode=True,
    )

    module.exit_json(changed=False, md5=test_md5_impl(module.params['data']))



# Generated at 2022-06-13 16:14:28.270620
# Unit test for function md5
def test_md5():
    ''' md5.py: Test md5()'''
    assert md5('/proc/modules') == 'e7ba18d6f96c6c88cf638f0d40e29b79'



# Generated at 2022-06-13 16:14:33.109951
# Unit test for function md5
def test_md5():
    ''' test md5s and md5 functions '''
    import tempfile
    fd, fname = tempfile.mkstemp()
    f = open(fname, 'w')
    f.write('hello')
    f.close()
    try:
        assert md5(fname) == md5s('hello')
    finally:
        os.remove(fname)

# Generated at 2022-06-13 16:14:36.639601
# Unit test for function md5s
def test_md5s():
    '''Test the basic functionality of md5s'''
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'



# Generated at 2022-06-13 16:14:40.785387
# Unit test for function checksum
def test_checksum():
    if checksum('/etc/passwd') != md5('/etc/passwd'):
        raise AnsibleError("checksum is not compatible with md5()")

if __name__ == '__main__':
    # Unit tests
    test_checksum()

# Generated at 2022-06-13 16:14:44.689161
# Unit test for function md5
def test_md5():
    import tempfile

    tf = tempfile.NamedTemporaryFile()
    tf.write("12345")

    # Check both the md5 and checksum versions work
    assert md5(tf.name) == checksum(tf.name)

    tf.close()

# Generated at 2022-06-13 16:14:49.723192
# Unit test for function md5
def test_md5():
    md5string = md5s('the-quick-brown-fox')
    assert(md5string == '6f4d6e8a80d2e6d2888d4d31f9f9b562')



# Generated at 2022-06-13 16:14:57.974038
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestMd5(unittest.TestCase):
        @patch('ansible.module_utils.basic.AnsibleModule.fail_json')
        @patch('ansible.utils.encrypt.md5')
        def test_md5_none(self, md5_mock, fail_json_mock):
            md5_mock.side_effect = ValueError()
            md5(None)
            fail_json_mock.assert_called_with(msg='MD5 not available.  Possibly running in FIPS mode', **{})


# Generated at 2022-06-13 16:15:00.466685
# Unit test for function md5s
def test_md5s():
    if hasattr(_md5, 'md5'):
        assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:15:09.061198
# Unit test for function md5s
def test_md5s():
    # Test normal cases
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('test') == md5('test')
    # Test unicode data
    assert md5s(u'test\u1234') == 'eea9e0e928f45ca319f0b30ba8d80c15'
    assert md5s(u'test\u1234') == md5(u'test\u1234')
    # Test some binary data
    assert md5s('\0\1\2') == '7791c1e568dbb483cda1bc77d21148ae'
    assert md5s('\0\1\2') == md5('\0\1\2')
    # Test some more

# Generated at 2022-06-13 16:15:13.071598
# Unit test for function md5s
def test_md5s():
    assert md5s('0000000000') == '356a192b7913b04c54574d18c28d46e6395428ab'

# Generated at 2022-06-13 16:15:15.687129
# Unit test for function md5
def test_md5():
    filename = "/etc/passwd"
    h = md5(filename)
    hs = md5s("foo")
    assert( isinstance(h, basestring))
    assert( isinstance(hs, basestring))


# Generated at 2022-06-13 16:15:21.840350
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils._text import to_bytes
    assert md5s("hello world") == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s(to_bytes("hello world")) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:15:25.968373
# Unit test for function md5s
def test_md5s():
    from nose.tools import assert_equals
    assert_equals(md5s('hello'), '5d41402abc4b2a76b9719d911017c592')
    assert_equals(md5s('123456'), 'e10adc3949ba59abbe56e057f20f883e')

# Generated at 2022-06-13 16:15:34.735004
# Unit test for function md5
def test_md5():

    teststr = 'hello world'
    assert md5s(teststr) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5(__file__) == 'a1f44c47f00d819720ca082b2d84fdf9'

    assert checksum(__file__) == 'a1f44c47f00d819720ca082b2d84fdf9'
    assert checksum_s(teststr) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:15:36.027934
# Unit test for function md5s
def test_md5s():
    print(md5s("test_md5s()"))


# Generated at 2022-06-13 16:15:38.765427
# Unit test for function md5s
def test_md5s():

    data = to_bytes('hello world', errors='surrogate_or_strict')
    assert md5s(data) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:15:46.331029
# Unit test for function md5
def test_md5():
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    f.file.write('hello world')
    f.file.close()
    hashed = md5(f.name)
    os.unlink(to_bytes(f.name, errors='surrogate_or_strict'))
    print(hashed)
    assert hashed == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:15:49.522589
# Unit test for function md5
def test_md5():
    assert md5s("Apache") == '36d7a3e3d18f72afef272283e0c1d805'
    assert md5("/etc/passwd") == '8fe8f02bae0ea08fea2e14d3ac8762ae'

# Generated at 2022-06-13 16:15:56.147521
# Unit test for function checksum
def test_checksum():
    import tempfile
    import os

    fd, filename = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('hello')
    f.close()
    print(filename)

    h = checksum(filename)
    assert(h == checksum(filename))
    f = open(filename)
    h = checksum_s(f.read())
    assert (h == checksum_s('hello'))

    os.remove(filename)

# Generated at 2022-06-13 16:16:04.645237
# Unit test for function md5
def test_md5():
    '''
    ansible core: testing module utils.crypto md5 function
    '''
    md5_test_file = 'test/utils/sha1sum/random_file'
    assert md5(md5_test_file) == "d41d8cd98f00b204e9800998ecf8427e"

# Generated at 2022-06-13 16:16:13.018632
# Unit test for function checksum
def test_checksum():
    import os
    filename = 'test_checksum'
    f = open(filename,'w')
    f.write('foo')
    f.close()
    checksum_file = secure_hash(filename)
    assert checksum_file == 'f3a3a3c2a1c0f3cf8e5b6f49af5d798150ea68a8', checksum_file
    checksum_s = secure_hash_s('foo')
    assert checksum_s == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33', checksum_s
    os.remove(filename)

# Generated at 2022-06-13 16:16:15.359772
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == 'ed076287532e86365e841e92bfc50d8c'


# Generated at 2022-06-13 16:16:20.695776
# Unit test for function md5
def test_md5():
    s = md5s('hello world')
    assert(s == '5eb63bbbe01eeed093cb22bb8f5acdc3')
    s = md5('/etc/passwd')
    assert(s == '6a3539e22d3a85c9e9f89a80e59a96b1')


# Generated at 2022-06-13 16:16:30.086609
# Unit test for function md5s
def test_md5s():
    '''
    Unit test for function md5s
    '''
    if _md5:
        # md5s not available in FIPS mode
        assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
        assert md5s('1234') == '81dc9bdb52d04dc20036dbd8313ed055'
        assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    else:
        try:
            md5s('test')
            assert True == False
        except ValueError:
            assert True == True



# Generated at 2022-06-13 16:16:33.590679
# Unit test for function md5
def test_md5():
    in_str = 'Hello World'
    out_str = to_bytes('ED076287532E86365E841E92BFC50D8C', errors='strict')
    result = md5s(in_str)
    assert result == out_str

# Generated at 2022-06-13 16:16:41.343905
# Unit test for function md5
def test_md5():
    data1 = "foobar"
    data2 = "foo"
    data3 = "bar"
    assert md5s(data1) == "3858f62230ac3c915f300c664312c63f"
    assert md5s(data2) == "acbd18db4cc2f85cedef654fccc4a4d8"
    assert md5s(data3) == "37b51d194a7513e45b56f6524f2d51f2"
    assert md5s(data1 + data2) == "f2aa67b599a1b422c8b7d4e913ce4046"

# Generated at 2022-06-13 16:16:45.036087
# Unit test for function md5s
def test_md5s():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert md5s(s) == '3cd5e122f6e19c6f8ab9267582405e64'


if __name__ == "__main__":
    test_md5s()

# Generated at 2022-06-13 16:16:46.732869
# Unit test for function md5s
def test_md5s():
    assert md5s(b"hello") == "5d41402abc4b2a76b9719d911017c592"


# Generated at 2022-06-13 16:16:50.263359
# Unit test for function md5
def test_md5():
    """
    Lets take a simple string and compare against an expected hash
    """
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"



# Generated at 2022-06-13 16:17:04.333585
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    assert md5s("asd") == "37b51d194a7513e45b56f6524f2d51f2"
    assert md5s("asdf") == "912ec803b2ce49e4a541068d495ab570"
    assert md5s("asdf1234") == "d6015ecc6ebadb5f1b0eac85950a42c9"
    assert md5s("aasdf1234") == "ea22d4e4e4a8f935c07e5f67413a4619"

# Generated at 2022-06-13 16:17:08.789324
# Unit test for function md5s
def test_md5s():
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abc').startswith('9')
    if _md5:
        assert md5s('abc').endswith('72')



# Generated at 2022-06-13 16:17:11.058166
# Unit test for function md5s
def test_md5s():
    assert md5s("The quick brown fox jumped over the lazy dog's back") == '9e107d9d372bb6826bd81d3542a419d6'


# Generated at 2022-06-13 16:17:17.963919
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    filename = 'ansible/module_utils/facts/redhat.py'
    print("md5 hash of %s = %s" % (filename, md5(filename)))


if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:17:22.904712
# Unit test for function md5
def test_md5():
    data = "The quick brown fox jumped over the lazy dog."
    md5_val = md5s(data)
    assert md5_val == '8d777f385d3dfec8815d20f7496026dc'


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:17:25.592838
# Unit test for function md5
def test_md5():
    filename="sha1sum.py"
    print("md5: %s" % md5(filename))


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:17:28.916063
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert checksum_s('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'

# Generated at 2022-06-13 16:17:31.670491
# Unit test for function md5s
def test_md5s():
    assert md5s('Helo World')  == '8aefa0adc7d86b8a59058690d30dbd58'



# Generated at 2022-06-13 16:17:34.008286
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:17:38.914552
# Unit test for function md5
def test_md5():
    # requires /usr/bin/md5sum
    assert md5(__file__) == 'f4bbd4b8e8b030f7e9f3d3d0c8c9768a'

# Generated at 2022-06-13 16:17:46.279799
# Unit test for function md5s
def test_md5s():
    md5s1 = md5s('hello world')
    md5s2 = md5s('hello world')
    assert(md5s1 == md5s2)
    assert(len(md5s1) == 32)

# Generated at 2022-06-13 16:17:49.438326
# Unit test for function md5
def test_md5():
    ''' return a dictionary with a datum and a string so that it can be tested'''
    return {'data': md5s('ansible'), 'string': md5(__file__)}

if __name__ == '__main__':
    print(test_md5())

# Generated at 2022-06-13 16:17:54.961275
# Unit test for function md5
def test_md5():
    "Simple MD5 sanity test"
    import unittest

    class TestMd5(unittest.TestCase):
        def test_md5(self):
            f1 = os.path.join(os.path.dirname(__file__), 'files', 'test_file.txt')
            f2 = os.path.join(os.path.dirname(__file__), 'files', 'test_file2.txt')

            sum1 = md5(f1)
            sum2 = md5(f2)
            sum3 = md5(f2)

            self.assertEqual(sum1, "d41d8cd98f00b204e9800998ecf8427e")
            self.assertTrue(sum1 != sum2)
            self.assertEqual(sum2, sum3)

    return

# Generated at 2022-06-13 16:18:02.249708
# Unit test for function md5
def test_md5():
    ''' ansible.utils.checksum test_md5 '''

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestChecksumMD5(unittest.TestCase):

        dummy_md5 = b'dummy_md5'

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-13 16:18:10.142624
# Unit test for function md5
def test_md5():
    from ansible.module_utils.basic import AnsibleModule as am
    from ansible.module_utils.basic import get_exception
    m = am.AnsibleModule(
        argument_spec=dict(
            filename='/etc/passwd',
            data='foo',
        )
    )
    try:
        m.exit_json(changed=False, filename=m.params['filename'], md5=md5(m.params['filename']), md5s=md5s(m.params['data']))
    except Exception as e:
        m.fail_json(msg=get_exception(e))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:18:13.689868
# Unit test for function checksum
def test_checksum():
    data = checksum("test/files/ansible_file")
    assert data == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2022-06-13 16:18:18.283791
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('test') == "098f6bcd4621d373cade4e832627b4f6"
    else:
        try:
            md5s('test')
            assert False
        except ValueError as e:
            assert str(e) == 'MD5 not available.  Possibly running in FIPS mode'



# Generated at 2022-06-13 16:18:31.251509
# Unit test for function checksum
def test_checksum():
    ''' Test checksum function against common MD5 and SHA-1 files '''

    # Test MD5 checksum
    md5sum = '86fb269d190d2c85f6e0468ceca42a20'
    chksum = checksum(filename='./test/utils/MD5SUMS')
    assert chksum == md5sum, \
        "Checksum of file %s did not match MD5 of file, got %s instead of %s." % \
        ('./test/utils/MD5SUMS', chksum, md5sum)

    # Test SHA-1 checksum
    sha1sum = 'e2c68fef6c549b6bb6270bf8cc7fada6c0a6f9e8'

# Generated at 2022-06-13 16:18:40.905918
# Unit test for function checksum
def test_checksum():
    assert checksum("/bin/ls") == "6fdc3fed3a52c0d2f18db7e8b0aa3e4f"
    assert checksum_s("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert checksum_s(u"hello") == "5d41402abc4b2a76b9719d911017c592"
    assert checksum_s(u"\u1234") == "2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c"

# Generated at 2022-06-13 16:18:45.191282
# Unit test for function md5
def test_md5():
    assert md5(__file__) == '6e068a2a336c19f78e8a8bbd406469d0'


# Generated at 2022-06-13 16:18:57.186994
# Unit test for function md5
def test_md5():

    assert md5("/etc/passwd") == "9bf9f774578e29a1b0ad068c64b6d5ae"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:19:00.182221
# Unit test for function md5
def test_md5():
    from StringIO import StringIO
    string = 'The quick brown fox jumped over the lazy dog'
    # This is the result from Perl's Digest::MD5 module.
    expected_res = '9e107d9d372bb6826bd81d3542a419d6'
    res = md5s(string)
    assert res == expected_res
    res = md5s(StringIO(string))
    assert res == expected_res

# Generated at 2022-06-13 16:19:10.957664
# Unit test for function checksum
def test_checksum():
    import tempfile

    with tempfile.NamedTemporaryFile() as tf_in:
        with open(tf_in.name, 'w') as tf:
            tf.write('new text')
        tf_in.seek(0)

        with tempfile.NamedTemporaryFile() as tf_out:
            tf_out.write(checksum(tf_in.name))
            tf_out.seek(0)
            assert len(tf_out.read()) == 40
            assert tf_out.read(1) == ''
            assert tf_out.read() == ''

            tf_out.seek(0)
            assert tf_out.read() == checksum(tf_in.name)

            tf_out.seek(0)
            assert tf_out.read() != '0000000000000000000000000000000000000000'

            tf_out.seek

# Generated at 2022-06-13 16:19:15.173463
# Unit test for function md5s
def test_md5s():
    """
    If this function fails, please check whether you have FIPS enabled and if so, please
    disable it and run the test again.
    """
    hashed_text = md5s("Hello World")
    assert hashed_text == "b10a8db164e0754105b7a99be72e3fe5"


# Generated at 2022-06-13 16:19:18.270138
# Unit test for function checksum
def test_checksum():
    test_str = 'Hello world!'
    if checksum_s(test_str) != '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed':
        return False
    return True

# Generated at 2022-06-13 16:19:25.060514
# Unit test for function md5
def test_md5():
    ''' test md5 function '''
    # The checksum algorithm must match with the algorithm in ShellModule.checksum() method
    assert md5('test/copy/to.txt') == '8af5e5e2f5fe24d5d060162b4f4cf4c1'
    assert md5s('to\n') == '8af5e5e2f5fe24d5d060162b4f4cf4c1'
    assert checksum('test/copy/to.txt') == '8af5e5e2f5fe24d5d060162b4f4cf4c1'
    assert checksum_s('to\n') == '8af5e5e2f5fe24d5d060162b4f4cf4c1'

# Generated at 2022-06-13 16:19:29.722145
# Unit test for function md5s
def test_md5s():
    # this function returns None if the hash algorithm is unavailable
    # which is the case on FIPS systems.  Otherwise, an md5 hash
    # for the string is returned
    val = md5s("hello")
    if val is not None:
        assert val == '5d41402abc4b2a76b9719d911017c592'
        return True
    return False

# Generated at 2022-06-13 16:19:31.122954
# Unit test for function checksum
def test_checksum():
    assert(checksum('README.md') == 'ee4ed7d9c3b8d7e9997f00210cee6cdd7812218e')

# Generated at 2022-06-13 16:19:34.940342
# Unit test for function md5s
def test_md5s():
    """ md5s: Test md5s.
        returns: True, on failure.
    """
    if md5s("Hello World") != "ed076287532e86365e841e92bfc50d8c":
        print("md5s failed")
        return False
    return True

# Generated at 2022-06-13 16:19:36.821375
# Unit test for function md5s
def test_md5s():
    assert md5s('123') == _md5('123').hexdigest()

# Generated at 2022-06-13 16:19:55.691318
# Unit test for function md5
def test_md5():
    if _md5 is None:
        raise Exception("MD5 not in hashlib")
    print('Test: md5()')
    print('md5(hello.txt) = ', md5('x.y/hello.txt'))
    print('md5(hello.txt) = ', md5('x.y/a/hello.txt'))
    print('md5(hello.txt) = ', md5('x.y/a/hello.txt'))
    print('md5(hello.txt) = ', md5('x.y/a/hello.txt'))
    print('md5(hello.txt) = ', md5('x.y/a/hello.txt'))
    print('md5(hello.txt) = ', md5('x.y/a/hello.txt'))

# Generated at 2022-06-13 16:19:57.786793
# Unit test for function md5s
def test_md5s():
    s = "hello"
    val = md5s(s)
    print ("5d41402abc4b2a76b9719d911017c592 should be " + val)
