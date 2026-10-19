

# Generated at 2022-06-13 16:10:09.613743
# Unit test for function md5
def test_md5():
    assert md5s('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

# Generated at 2022-06-13 16:10:20.679484
# Unit test for function checksum
def test_checksum():
    tmp_file = os.path.join(os.path.dirname(__file__), 'test_checksum_tmp')
    tmp_file_s = os.path.join(os.path.dirname(__file__), 'test_checksum_tmp_s')
    with open(tmp_file, 'wb') as tmp_f:
        tmp_f.write(to_bytes('hello'))
    with open(tmp_file_s, 'wb') as tmp_f:
        tmp_f.write(to_bytes('hellobye'))

    sum1 = checksum(tmp_file)
    sum2 = checksum(tmp_file)
    print('comparing checksum of %s to %s' % (sum1, sum2))
    assert sum1 is not None
    assert sum2 is not None

# Generated at 2022-06-13 16:10:24.079494
# Unit test for function md5s
def test_md5s():
    input = 'this is my string'
    output = '67a09903c5e565812d0f5397b1c28ec7'
    assert md5s(input) == output

# Generated at 2022-06-13 16:10:26.329514
# Unit test for function md5
def test_md5():
    data = "hello world"
    digest = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5s(data) == digest

# Generated at 2022-06-13 16:10:30.440206
# Unit test for function md5
def test_md5():
    ''' md5 should return expected value of md5sums '''

    x = md5('/bin/ls')
    assert x == '0a3c3a8a396f8ab8a0e1e89d1af60c04'


# Generated at 2022-06-13 16:10:33.043509
# Unit test for function checksum
def test_checksum():
    assert checksum('lib/ansible/module_utils/basic.py') == 'b101307f20847c9d1a6984bbf0bcc68d8c8ea1080'


# Generated at 2022-06-13 16:10:37.738313
# Unit test for function md5s
def test_md5s():
    ''' md5s.py: Unit test'''
    data = 'abc'
    result = md5s(data)
    assert result == '900150983cd24fb0d6963f7d28e17f72' , 'md5s() failed'

# Generated at 2022-06-13 16:10:46.867249
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest
    from ansible.module_utils import basic
    import os
    import tempfile
    import shutil
    import StringIO

    class TestChecksum(unittest.TestCase):
        def setUp(self):
            self.local_tmp_path = tempfile.mkdtemp()
            self.test_file = os.path.join(self.local_tmp_path, "temp_file")
            fh = open(self.test_file, "w")
            fh.write("foo")
            fh.flush()
            fh.close()

        def tearDown(self):
            shutil.rmtree(self.local_tmp_path, True)

        # test checksum for file handles

# Generated at 2022-06-13 16:10:57.089097
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest
    from ansible.compat.tests import ansible_unittest
    from ansible.compat.tests.mock import patch, MagicMock

    class TestMd5(ansible_unittest.TestCase):
        @patch('ansible.utils.md5._md5')
        def test_md5(self, mocked_md5):
            mocked_md5.return_value = MagicMock()
            self.assertRaises(ValueError, md5, 'file')
            mocked_md5.return_value = _md5()
            self.assertEqual(md5('file'), None)

    unittest.main()


# Generated at 2022-06-13 16:11:08.637915
# Unit test for function checksum
def test_checksum():
    ''' test secure_hash_s and secure_hash functionality '''
    # Have to import here to avoid circular imports
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # Check secure_hash_s output - SHA1
    test_string = 'My test string.'
    correct_checksum = '7683e3cf3a8a8da782f290517d1958e86c7143fe'
    if checksum_s(test_string) != correct_checksum:
        module.fail_json(
            msg='checksum_s did not return correct output'
        )
    # Check secure_hash output - SHA1
    test_file = 'ansible_test_file.txt'

# Generated at 2022-06-13 16:11:14.250988
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:11:20.384184
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.basic import AnsibleModule

    def test(file, result, hexdigest, params):
        if checksum(file) != result:
            params['failed'] = True
        if checksum_s(hexdigest) != result:
            params['failed'] = True

    module = AnsibleModule(
        argument_spec=dict(
            file=dict(required=True),
            result=dict(required=True),
            hexdigest=dict(required=True)
        ),
    )

    params = module.params
    test(params['file'], params['result'], params['hexdigest'], params)
    module.exit_json(**params)



# Generated at 2022-06-13 16:11:22.143406
# Unit test for function md5
def test_md5():
    assert md5('/foo/bar/baz') is None

# Generated at 2022-06-13 16:11:23.374850
# Unit test for function md5
def test_md5():
    h = md5("h")
    assert h == "6f8db599de986fab7a21625b7916589c"


# Generated at 2022-06-13 16:11:36.199341
# Unit test for function md5
def test_md5():
    '''
    Validate that md5() and md5s() are proper FIPS replacements for
    secure_hash() and secure_hash_s() with an MD5 hash algorithm
    '''

    # Generate test data
    import random
    import string
    alphabet = string.ascii_letters + string.digits

    def data_generator(size=6, chars=alphabet):
        return ''.join(random.choice(chars) for _ in xrange(size))

    def md5_hash(data):
        import hashlib
        digest = hashlib.md5()
        digest.update(data)
        return digest.hexdigest()

    # Ensure that md5s produces the same value as md5_hash for the same inputs
    for _ in xrange(10):  # Make 10 random inputs
        data = data

# Generated at 2022-06-13 16:11:44.604621
# Unit test for function md5s
def test_md5s():
    # Test empty string
    if md5s('') != 'd41d8cd98f00b204e9800998ecf8427e':
        raise AssertionError('Empty string MD5 failed.')
    # Test utf-8 string
    if md5s('שלום') != 'c6234c19f12ddc6acb0d4b17dbf16309':
        raise AssertionError('UTF-8 string MD5 failed.')
    # Test unicode string
    if md5s(u'שלום') != 'c6234c19f12ddc6acb0d4b17dbf16309':
        raise AssertionError('Unicode string MD5 failed.')
    # Test byte string

# Generated at 2022-06-13 16:11:49.681822
# Unit test for function md5
def test_md5():
    # Test that md5s is a wrapper for secure_hash_s by passing the function itself into secure_hash_s and seeing if it comes back
    s = "foobarbaz"
    assert md5s(s) == secure_hash_s(s, md5s)

if __name__ == "__main__":
    import sys
    import doctest
    sys.exit(doctest.testmod()[0])

# Generated at 2022-06-13 16:11:52.551364
# Unit test for function md5s
def test_md5s():
    assert md5s(u'hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:12:01.837501
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls') == '6b8e6c2f6e08a6a8a6a1f6336c99ce1b98452a9a'
    assert checksum('/bin/ls', hash_func=_md5) == 'd092c9cd9a9ad507a518741b1eacacc1'
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum_s('hello world', hash_func=_md5) == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:12:06.310311
# Unit test for function md5
def test_md5():
    try:
        assert md5('test/files/test_file') == '3c15f13f026d18d23dcab3551b3be3cc'
    except AssertionError:
        print("Test failed")

# Generated at 2022-06-13 16:12:16.367247
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, name) = tempfile.mkstemp()

# Generated at 2022-06-13 16:12:23.761250
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil

    dirpath = tempfile.mkdtemp()

    # Check md5 algorithm with file test
    filename = os.path.join(dirpath, 'test_md5')
    data = "test_md5"
    f = open(filename, 'w')
    f.write(data)
    f.close()

    assert md5(filename) == md5s(data)

    # Remove test directory
    shutil.rmtree(dirpath, True)

# Generated at 2022-06-13 16:12:28.625839
# Unit test for function checksum
def test_checksum():
    import tempfile
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(b"blah")
        tmp.flush()

        assert(checksum(tmp.name) == "35bf7b7f72a84a1be7d2cf2e3e7ac1f38f9b769e")
        assert(checksum_s("blah") == "35bf7b7f72a84a1be7d2cf2e3e7ac1f38f9b769e")


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:39.009394
# Unit test for function checksum
def test_checksum():

    import tempfile

    tf = tempfile.NamedTemporaryFile()
    tf.write('this is some data')
    tf.flush()

    assert secure_hash(tf.name) == secure_hash_s('this is some data')
    assert secure_hash(tf.name) == '5d5e5f91ca5c5d5df2e5f9f9449fd1fd2b7e40ac'
    assert md5(tf.name) == md5s('this is some data')
    assert md5(tf.name) == 'd2296f5e5c5ed5a5d5d5e9f9449fd1fd'


# Generated at 2022-06-13 16:12:42.735810
# Unit test for function checksum
def test_checksum():
    ''' Test for function checksum '''

    assert checksum("examples/ansible-test.cfg") == "40d096c1b6f8b80a71a6a0d92f2a6a85c6f689e0"

# Generated at 2022-06-13 16:12:47.022734
# Unit test for function md5
def test_md5():
    '''
    Test to ensure that md5 and checksum produce the same results for backwards compatibility.
    This is needed to support checksum for yum and for dnf.  Once the yum module has been updated
    to return checksum instead of md5, this function can be removed.
    '''

    assert md5('/etc/passwd') == checksum('/etc/passwd')

# Generated at 2022-06-13 16:12:56.873761
# Unit test for function checksum
def test_checksum():
    demo_string = "abcabc"
    demo_string_checksum = "a448017aaf21d8525fc10ae87aa6729d"

    if checksum_s(demo_string) != demo_string_checksum:
        print("Failed checksum_s test")
        return False

    demo_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_fixtures/checksum_test.txt")
    demo_file_checksum = "a448017aaf21d8525fc10ae87aa6729d"

    if checksum(demo_file_path) != demo_file_checksum:
        print("Failed checksum test")
        return False

    return True

# Generated at 2022-06-13 16:12:59.276618
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:13:03.446265
# Unit test for function md5
def test_md5():
    if not _md5:
        return

    filename = "/bin/ls"
    assert md5(filename) == "a31d43a387f1aa244811a84b694acbc2"

    data = "123"
    assert md5s(data) == "202cb962ac59075b964b07152d234b70"


test_md5()



# Generated at 2022-06-13 16:13:12.219252
# Unit test for function checksum
def test_checksum():
    # This string is:
    # $1$JJsvHslm$Y6cNje5NO5vv5OowZ4YwP/
    data = b'$1$JJsvHslm$Y6cNje5NO5vv5OowZ4YwP/'
    assert checksum_s(data) == '1d8e9c7b3581c74b4e13b4e8f8a1aeb9d9adadf7'

if __name__ == "__main__":
    test_checksum()

# Generated at 2022-06-13 16:13:21.596651
# Unit test for function checksum
def test_checksum():
    test_string = b"HiHowAreYou"

    assert secure_hash_s(test_string) == "10b932a2bf6fb26b6d8b6f76fbb1797c29112b68"
    assert secure_hash_s(test_string, hash_func=_md5) == '97807c24d47a091af8b7e94b9355f18e'

# Generated at 2022-06-13 16:13:27.504830
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, tf) = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('abcdefg')
    f.close()
    assert(md5(tf) == '7ac66c0f148de9519b8bd264312c4d64')
    os.unlink(tf)
    assert(md5s('abcdefg') == '7ac66c0f148de9519b8bd264312c4d64')

# Generated at 2022-06-13 16:13:29.838028
# Unit test for function md5s
def test_md5s():
    if _md5:
        print("md5s('hello world') = %s" % md5s('hello world'))
    else:
        print('md5s() not available on this system')


# Generated at 2022-06-13 16:13:32.572354
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('mystring') == 'f96b697d7cb7938d525a2f31aaf161d0'



# Generated at 2022-06-13 16:13:39.862615
# Unit test for function md5s
def test_md5s():
    from ansible.compat.tests import unittest
    import ansible.module_utils.basic

    class Md5sTestCase(unittest.TestCase):
        def test_md5s_normal(self):
            text = "hello world"
            hash = "5eb63bbbe01eeed093cb22bb8f5acdc3" # 'md5 -s "hello world"'
            self.assertEqual(ansible.module_utils.basic.md5s(text), hash)

        def test_md5_no_fips(self):
            text = "hello world"
            with self.assertRaises(ValueError):
                ansible.module_utils.basic.md5(text)

        def test_md5_no_file(self):
            text = "/dev/null"

# Generated at 2022-06-13 16:13:44.945278
# Unit test for function checksum
def test_checksum():
    # Test secure_hash function
    test_str = 'nginx'
    res_str = '9bcfe50ce1ba98b82d60fa1fb0e97fda55b40ec2'
    assert res_str == secure_hash_s(test_str)


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:13:49.481654
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert('d41d8cd98f00b204e9800998ecf8427e' == md5(None))
        assert('d41d8cd98f00b204e9800998ecf8427e' == md5(''))
        assert('900150983cd24fb0d6963f7d28e17f72' == md5('abc'))


# Generated at 2022-06-13 16:13:56.471027
# Unit test for function md5s
def test_md5s():
    import sys
    if sys.version_info < (2, 5):
        return False
    else:
        print("Testing md5s()")
        if md5s("hello") != "5d41402abc4b2a76b9719d911017c592":
            print("md5s('hello') failed.\n%s" % md5s("hello"))
            return False
        else:
            print("md5s('hello') = %s" % md5s("hello"))
            return True

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:14:07.979212
# Unit test for function md5
def test_md5():
    data_list = [
        ['abc', '900150983cd24fb0d6963f7d28e17f72'],
        ['abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq', '8215ef0796a20bcaaae116d3876c664a'],
        ['', 'd41d8cd98f00b204e9800998ecf8427e'],
        ['hello', '5d41402abc4b2a76b9719d911017c592'],
    ]
    for (string, expected_result) in data_list:
        result = md5s(string)
        assert result == expected_result


# Generated at 2022-06-13 16:14:17.137441
# Unit test for function checksum
def test_checksum():
    # Create a test file
    import random

    test_file_name = 'test_file'
    test_file_len = 2000
    if os.path.exists(test_file_name):
        raise Exception("Test file %s already exists" % test_file_name)
    with open(test_file_name, 'w') as test_file:
        for i in xrange(test_file_len):
            test_file.write(str(random.randint(0, 9)))

    # Compute the checksum
    expected_checksum = 'bccb1d67ae086c838f9edabbe9a7bbf0'
    checksum_result = checksum(test_file_name)

# Generated at 2022-06-13 16:14:23.084140
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('asdf') == '912ec803b2ce49e4a541068d495ab570'
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:14:25.961941
# Unit test for function md5s
def test_md5s():
    test_value = "ABC123"
    expected_result = "6f3d6df28e5da5f5c5f9d79a5cd813e4"
    md5s_result = md5s(test_value)
    assert(md5s_result == expected_result)


# Generated at 2022-06-13 16:14:32.867076
# Unit test for function md5s
def test_md5s():
    x = md5s("hello world 123")
    y = md5s("hello world 123")
    assert x == y
    x = md5s("hello world")
    y = md5s("hello world 123")
    assert x != y
    x = md5s("hello world")
    y = md5s("hello world")
    assert x == y
    print("md5s() unit test successful")

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:14:44.346425
# Unit test for function md5
def test_md5():
    '''Unit test for function md5'''
    from tempfile import NamedTemporaryFile

    tf = NamedTemporaryFile()
    tf.write('hello world')
    tf.flush()
    assert md5(tf.name) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    tf.close()


if __name__ == '__main__':
    import sys, json

# Generated at 2022-06-13 16:14:50.358027
# Unit test for function md5
def test_md5():
    if _md5:
        assert md5(__file__) == 'b1a8ec8a901a43797f46b9c711f8ab86'
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'



# Generated at 2022-06-13 16:14:53.799426
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls') == "d7e2c94ae60e7f9d9e9db9c97fbb5e0f0e5b58a1"



# Generated at 2022-06-13 16:15:02.412442
# Unit test for function md5s
def test_md5s():
    ''' unit test for md5s function '''
    # simple string
    assert md5s(b"test") == "098f6bcd4621d373cade4e832627b4f6"

    # simple unicode string
    assert md5s(u"test") == "098f6bcd4621d373cade4e832627b4f6"

    # with a unicode char
    assert md5s(u"test\u2013") == "e6d18ce4ca4a4d8f6dcfbf96581d01e2"

    # with a UTF-8 BOM
    assert md5s(u"\ufefftest\u2013") == "e6d18ce4ca4a4d8f6dcfbf96581d01e2"

    # with

# Generated at 2022-06-13 16:15:07.144304
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5("/etc/passwd") is not None
    assert md5("/path/to/file/which/does/not/exist") is None
    assert md5("/dev/null") == "d41d8cd98f00b204e9800998ecf8427e"

# Generated at 2022-06-13 16:15:09.182302
# Unit test for function md5s
def test_md5s():
    assert md5s('abcdef') == 'ef797c8118f02dfb649607dd5d3f8c76'



# Generated at 2022-06-13 16:15:12.797021
# Unit test for function md5
def test_md5():
    '''
    ansible hashutils -m hashutils -a "test_md5"
    '''
    try:
        md5('test_md5')
    except ValueError as e:
        return {'failed': True, 'msg': str(e)}
    else:
        return {'failed': False}

# Generated at 2022-06-13 16:15:17.999003
# Unit test for function md5
def test_md5():
    filename = '_test_md5.txt'
    try:
        with open(filename, 'w') as f:
            f.write('test')
        assert md5(filename) == '098f6bcd4621d373cade4e832627b4f6'
    finally:
        os.unlink(filename)

# Generated at 2022-06-13 16:15:26.651820
# Unit test for function md5
def test_md5():
    assert md5s("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert md5s("test" * 1024) == "3d7f2b01d5eb98ff9c9f3d3b2099c173"
    assert md5("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert md5("test" * 1024) == "3d7f2b01d5eb98ff9c9f3d3b2099c173"

# unit test for function checksum

# Generated at 2022-06-13 16:15:29.585102
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"



# Generated at 2022-06-13 16:15:35.522400
# Unit test for function md5s
def test_md5s():
    md5s_test_results = (
        ("", "d41d8cd98f00b204e9800998ecf8427e"),
        ("HelloWorld", "2ef7bde608ce5404e97d5f042f95f89f")
    )
    for test in md5s_test_results:
        if md5s(test[0]) != test[1]:
            raise Exception("md5s test failed")


# Generated at 2022-06-13 16:15:38.288347
# Unit test for function md5
def test_md5():
    assert md5('./lib/ansible/module_utils/basic.py') == 'de8e1cd332ef80c0f0b79a9b9afa2b2a'


# Generated at 2022-06-13 16:15:47.388130
# Unit test for function md5
def test_md5():
    random_data = "test_md5"
    assert(md5s(random_data) == "32b023f7a9fb10b79e1f816e3eba7bb3")
    assert(md5("./test/ansible/unit/modules/utils/test/test_md5.py") == "a5b33d92b54a2c5a1e9401c6f2bc3daf")

if __name__ == '__main__':
    # Test
    print("Testing md5")
    test_md5()
    print("md5 passes")

# Generated at 2022-06-13 16:15:50.923981
# Unit test for function md5s
def test_md5s():
    assert md5s(b"test") == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:15:59.330253
# Unit test for function checksum
def test_checksum():
    import tempfile

    fd, path = tempfile.mkstemp()
    fh = os.fdopen(fd, 'w')
    msg = 'file with content'
    fh.write(msg)
    fh.close()
    try:
        ansible_sha1 = checksum(path)
        assert ansible_sha1 == 'e40a5c87e71562d2a88864c9f977f9af68bd2cdd'

        ansible_sha1 = checksum_s(msg)
        assert ansible_sha1 == 'e40a5c87e71562d2a88864c9f977f9af68bd2cdd'
    finally:
        os.remove(path)

# Generated at 2022-06-13 16:16:02.399355
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == "acbd18db4cc2f85cedef654fccc4a4d8"
    try:
        md5s(None)
        raise Exception("Test should have failed.")
    except:
        pass


# Generated at 2022-06-13 16:16:12.894122
# Unit test for function md5
def test_md5():
    filename = "/etc/passwd"
    if os.path.exists(filename):
        assert md5(filename) == 'd3b07384d113edec49eaa6238ad5ff00'
        assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# end backwards compat functions

#
# The new way forward:
#
# The "secure_hash" is sha1 for now, but will likely change to sha256
# in the future.  It should be used for anything that might be user
# visible.  The "secure_hash_s" will be used for internal purposes
# where collision risk is low and the algorithm will be free to change.
#

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:24.423419
# Unit test for function md5
def test_md5():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='path'),
        ),
        supports_check_mode=True
    )

    if not os.path.exists(module.params['path']):
        module.fail_json(msg="path not exists.")
    else:
        module.exit_json(changed=False, ansible_facts=dict(path_md5=md5(module.params['path'])))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:26.605243
# Unit test for function md5s
def test_md5s():
    result = md5s('hello')
    assert result == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:16:32.175270
# Unit test for function checksum
def test_checksum():
    exe_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_checksum')
    return os.access(exe_file, os.X_OK) and checksum(exe_file) == "e7bef96bbe1de7c8098a8c66e947d3ec"


# Generated at 2022-06-13 16:16:34.209162
# Unit test for function md5s
def test_md5s():

    assert md5s('xyz') == 'b87325c07fbc3f1f9b9d1f36c21fba74'

# Generated at 2022-06-13 16:16:39.376698
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest

    class TestMd5(unittest.TestCase):
        md5_s = md5s('test')

        def test_md5_s_generate_same_output(self):
            self.assertEqual(self.md5_s, '098f6bcd4621d373cade4e832627b4f6')

    unittest.main()


if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:16:42.778310
# Unit test for function md5
def test_md5():
    h = md5('test/test.ini')
    assert h
    assert h == 'b5fdd6c0a0007d93c49bb8cd9cd9f9c0'
    h = md5('test/test.ini.notfound')
    assert not h
    h = md5('test')
    assert not h


# Generated at 2022-06-13 16:16:47.708939
# Unit test for function md5
def test_md5():
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests import unittest
    from ansible.module_utils.six import PY3

    if not PY3:
        # These tests mock out the use of hashlib and md5, which is unsupported in Python 3
        class TestMd5(unittest.TestCase):

            @patch('ansible.module_utils.basic.md5.md5', return_value='test')
            def test_md5(self, md5):
                self.assertEqual(ansible.module_utils.basic.md5('test1'), 'test')


# Generated at 2022-06-13 16:16:51.594789
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    try:
        md5s(1)
        assert False
    except TypeError:
        pass
    try:
        md5s(None)
        assert False
    except TypeError:
        pass


# Generated at 2022-06-13 16:16:59.072830
# Unit test for function md5s
def test_md5s():
    import os
    import tempfile
    (fd, fname) = tempfile.mkstemp()
    os.write(fd, b'hello')
    os.close(fd)

    assert(md5s('hello') == '5d41402abc4b2a76b9719d911017c592')
    assert(md5(fname) == '5d41402abc4b2a76b9719d911017c592')

    os.remove(fname)

# Generated at 2022-06-13 16:17:01.237044
# Unit test for function md5
def test_md5():
    print(md5('/etc/passwd'))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:17:09.532667
# Unit test for function md5s
def test_md5s():
    '''
    Basic sanity test to ensure the md5s() works properly in Python 2 and Python 3.
    '''

    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    string = 'hello world'
    expected_hash = '5eb63bbbe01eeed093cb22bb8f5acdc3'

    assert md5s(string) == expected_hash

# Generated at 2022-06-13 16:17:13.006222
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s(u'abc') == u'900150983cd24fb0d6963f7d28e17f72'
        assert md5s('abc') == u'900150983cd24fb0d6963f7d28e17f72'


# Generated at 2022-06-13 16:17:15.570809
# Unit test for function md5
def test_md5():
    assert md5(None) == None
    assert md5('tests/test_utils/test1') == '5a35f5d5fbd2a4094a5d5b79a5a42223'
    assert md5('tests/test_utils/test2') == '18bdc1eccd1a7fd6dcef6b7a8b9a6d2e'



# Generated at 2022-06-13 16:17:23.353437
# Unit test for function md5
def test_md5():
    s = """This is a string to md5.
It covers more than one line
"""
    f = '__test_md5_file'

    with open(f, 'w') as fd:
        fd.write(s)

    assert md5(f)  == md5s(s)
    assert md5s(s) == '5e5018b7f9b9d30b7fb174ddd8f4be4b'

    os.unlink(f)


# Generated at 2022-06-13 16:17:31.942587
# Unit test for function md5
def test_md5():
    '''
    Make sure that the md5 function returns the expected hashes
    '''

    import random
    import string

    random.seed()

    try:
        tmp_file = open('/tmp/ansible-md5', 'w')
        tmp_file.write("".join(random.choice(string.letters) for _ in xrange(10*1024)))
    finally:
        tmp_file.close()

    try:
        assert md5(filename='/tmp/ansible-md5') == '9b9f044ac186f3e70d80c39e4e4da4c4'
    finally:
        os.unlink('/tmp/ansible-md5')

    assert md5(filename='/tmp/ansible-md5-not-found') == None

# Generated at 2022-06-13 16:17:38.881206
# Unit test for function checksum
def test_checksum():
    try:
        from hashlib import sha256
    except ImportError:
        sha256 = None

    if not os.path.exists(to_bytes('/usr/bin/coreutils', errors='surrogate_or_strict')) or os.path.isdir(to_bytes('/usr/bin/coreutils', errors='surrogate_or_strict')):
        print('/usr/bin/coreutils not found. Skipping checksum test')
        return

    def _test_checksum(filename, hasher):
        if hasher is None:
            return
        file_hasher = hasher()
        checksum_hasher = hasher()
        blocksize = 64 * 1024
        infile = open(to_bytes(filename, errors='surrogate_or_strict'), 'rb')
        block

# Generated at 2022-06-13 16:17:43.201179
# Unit test for function md5s
def test_md5s():
    test_input = 'abcdefghijklmnopqrstuvwxyz'
    test_output = 'c3fcd3d76192e4007dfb496cca67e13b'
    assert test_output == md5s(test_input), 'md5s failed'



# Generated at 2022-06-13 16:17:47.776157
# Unit test for function md5
def test_md5():
    h = md5("/bin/ls")
    print("md5(/bin/ls) = %s" % h)
    print("md5(/bin/ls) = 9f20b451147f3ce3e3c9e9e40f980ae8")
    assert(h == "9f20b451147f3ce3e3c9e9e40f980ae8")

# Generated at 2022-06-13 16:17:53.100511
# Unit test for function md5s
def test_md5s():
    import os

    data = 'Hello World'
    target_md5 = '65a8e27d8879283831b664bd8b7f0ad4'
    test_md5 = md5s(data)

    if target_md5 != test_md5:
        print(os.path.basename(__file__), 'test_md5s')
        raise AssertionError('md5s error, target_md5 =', target_md5, 'test_md5 =', test_md5)


# Generated at 2022-06-13 16:17:56.578687
# Unit test for function md5s
def test_md5s():
    """This is a unit test for md5s."""
    print(md5s('test'))

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:18:08.776799
# Unit test for function md5
def test_md5():
    filename = "/usr/bin/python2.7"
    md5_x = "d5f5a5d5c7e5f25b5e7d36a812e8f1e1"
    md5_y = md5(filename)
    if md5_x == md5_y:
        print("test md5 success")
        print("md5_x: %s" % md5_x)
        print("md5_y: %s" % md5_y)
    else:
        print("test md5 failed")
        print("md5_x: %s" % md5_x)
        print("md5_y: %s" % md5_y)


# Generated at 2022-06-13 16:18:11.796140
# Unit test for function md5
def test_md5():
    test_file = 'test_file'
    test_string = 'test string'

    with open(test_file, 'wb') as myfile:
        myfile.write(test_string)

    assert md5(test_file) == '9a0364b9e99bb480dd25e1f0284c8555'
    os.remove(test_file)

# Generated at 2022-06-13 16:18:14.409077
# Unit test for function md5
def test_md5():
    assert md5('test/test_md5sum.py') == 'f83d3b3e440b8905360edcd1a55adf68'

# Generated at 2022-06-13 16:18:18.910083
# Unit test for function md5
def test_md5():
    ''' sha1 should be the default while md5 should raise errors '''
    if not _md5:
        try:
            md5('/etc/hosts')
            assert False, 'This should have raised an error'
        except ValueError:
            pass
    else:
        assert md5('/etc/hosts') == 'e2151e8f7cb62afb4a9a1c95744a524e'

# Generated at 2022-06-13 16:18:23.688801
# Unit test for function md5
def test_md5():
    ''' md5 should return an md5 hash of the test file '''
    assert(md5("test/test-module-utils-checksum/test-file") == 'b275e77bc8e696dfaef2f4864c9a843f')


# Generated at 2022-06-13 16:18:32.541245
# Unit test for function checksum
def test_checksum():

    filename = '/etc/hosts'
    expected_checksum = '5f5d5f5a5a5c5d5e5a5e5a5f5e5a5a5d5e5d5c5a5b5c5d5a5e5f5e5e5d5c5b5a5d5a5a5b5c5d5f5c5d5d'
    checksum_result = secure_hash(filename, md5)
    assert(checksum_result == expected_checksum)

test_checksum()

# Generated at 2022-06-13 16:18:37.284084
# Unit test for function md5
def test_md5():
    assert md5('/etc/passwd') == '6fa8f9d394bccc7f685f0d3ae8397bfb'
    assert md5('/bin/notexist') is None
    assert md5('/dev/tty') is None


# Generated at 2022-06-13 16:18:45.519156
# Unit test for function checksum
def test_checksum():
    def _test_checksum(hash_func=sha1):
        assert checksum_s('test') == hash_func('test').hexdigest()

        tests = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9']
        assert checksum_s(tests) == hash_func(''.join(tests)).hexdigest()

    _test_checksum()

# Generated at 2022-06-13 16:18:49.041733
# Unit test for function md5
def test_md5():
    # This is a md5 test vector from RFC 1321
    test_data = "abc"
    assert md5s(test_data) == "900150983cd24fb0d6963f7d28e17f72"



# Generated at 2022-06-13 16:18:57.939489
# Unit test for function md5
def test_md5():
    # Create a test file for hashing
    fd, path = tempfile.mkstemp()
    fp = os.fdopen(fd, 'w')
    fp.write('Hello World')
    fp.close()

    # Get the md5 has sum
    h = md5(path)
    os.unlink(path)

    # Test to verify the correct hashing.
    assert(h == 'b10a8db164e0754105b7a99be72e3fe5')


# Generated at 2022-06-13 16:19:05.517505
# Unit test for function md5s
def test_md5s():
    results = md5s("password")
    assert results == '5f4dcc3b5aa765d61d8327deb882cf99'


# Generated at 2022-06-13 16:19:16.216672
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('1234567890') == '25d55ad283aa400af464c76d713c07ad'
    assert md5s('1234567890'*4) == '939eae2c835e6ef36da6d0240d15cbd6'
    assert md5s('1234567890'*400) == '9715fef6d0dee7c0b259468b7d5046c9'

# Generated at 2022-06-13 16:19:19.323488
# Unit test for function md5
def test_md5():
    import tempfile
    f = tempfile.NamedTemporaryFile()
    f.write('foobar')
    f.flush()

    assert md5(f.name) == '3858f62230ac3c915f300c664312c63f'

# Generated at 2022-06-13 16:19:21.780470
# Unit test for function md5s
def test_md5s():
  assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
  assert md5s("world") == "7d793037a0760186574b0282f2f435e7"

# Generated at 2022-06-13 16:19:26.489713
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5('/etc/passwd') == '4c7b1ed23c48ae9d84e3ea36ec0c0d8e'


# Generated at 2022-06-13 16:19:35.727823
# Unit test for function md5s
def test_md5s():
    import textwrap
    a = "this is a test"
    b = textwrap.dedent("""\
        this
        is a
        test""")
    c = textwrap.dedent("""\
        this
        is a
        test
        """)
    d = textwrap.dedent("""\
        this


        is a


        test


        """)
    assert md5s("") == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s("a") == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s("abc") == '900150983cd24fb0d6963f7d28e17f72'

# Generated at 2022-06-13 16:19:37.755781
# Unit test for function md5s
def test_md5s():
    assert md5s("1234") == "81dc9bdb52d04dc20036dbd8313ed055"



# Generated at 2022-06-13 16:19:46.028407
# Unit test for function md5s
def test_md5s():
    '''
    basic function test
    '''
    import os

    assert md5s("foobar") == "8843d7f92416211de9ebb963ff4ce28125932878"
    assert md5s("foobar") == "8843d7f92416211de9ebb963ff4ce28125932878"
    assert md5s(u"foobar") == "8843d7f92416211de9ebb963ff4ce28125932878"
    assert md5s(u"foobar") == "8843d7f92416211de9ebb963ff4ce28125932878"

# Generated at 2022-06-13 16:19:52.555004
# Unit test for function md5
def test_md5():
    if _md5:
        assert md5('/etc/passwd') == secure_hash('/etc/passwd', _md5)
        assert md5s('hello') == secure_hash_s('hello', _md5)
    else:
        try:
            assert md5('/etc/passwd')
        except ValueError:
            pass
        else:
            assert False, 'Expect ValueError'

        try:
            assert md5s('hello')
        except ValueError:
            pass
        else:
            assert False, 'Expect ValueError'

# Generated at 2022-06-13 16:19:55.222218
# Unit test for function md5
def test_md5():
    ''' test md5 for this system'''
    if _md5:
        print(md5('md5'))
    else:
        print('md5 not available')

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:20:03.569131
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == "098f6bcd4621d373cade4e832627b4f6"