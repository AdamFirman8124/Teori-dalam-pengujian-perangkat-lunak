

# Generated at 2022-06-13 16:10:05.448771
# Unit test for function md5
def test_md5():
    filename = "./test.txt"
    f = open(filename, "wb")
    f.write("abc")
    f.close()
    assert md5(filename) == '900150983cd24fb0d6963f7d28e17f72'
    os.unlink(filename)



# Generated at 2022-06-13 16:10:13.324716
# Unit test for function checksum
def test_checksum():
    assert checksum_s('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert checksum_s(u'foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert checksum('test/test_utils/test_checksum.py') == '06b88e722b9f9ac9c2b6752a03c86fefda180d48'

# Generated at 2022-06-13 16:10:23.202443
# Unit test for function md5s
def test_md5s():
    file1 = {'file1': secure_hash_s('File1 contents')}
    file2 = {'file2': secure_hash_s('File2 contents')}
    file3 = {'file3': secure_hash_s('File3 contents')}
    file4 = {'file4': secure_hash_s('File4 contents')}

    assert md5s(secure_hash_s('File1 contents')) == file1['file1']
    assert md5s(secure_hash_s('File2 contents')) == file2['file2']
    assert md5s(secure_hash_s('File3 contents')) == file3['file3']
    assert md5s(secure_hash_s('File4 contents')) == file4['file4']

# Generated at 2022-06-13 16:10:30.489646
# Unit test for function checksum
def test_checksum():
    ''' unit test for function checksum '''

    import os

    # tempfile to use for unit test
    (dummy_fd, filename) = tempfile.mkstemp()
    f = open(filename, 'w')
    # write something to the file
    f.write('foobar')
    f.close()

    # calculate secure hash
    sha_checksum = checksum(filename)

    # assert secure hash is right
    assert sha_checksum == '8843d7f92416211de9ebb963ff4ce28125932878'

    os.remove(filename)

__all__ = ['checksum', 'checksum_s', 'md5', 'md5s']

# Generated at 2022-06-13 16:10:35.171971
# Unit test for function checksum
def test_checksum():
    ''' basic test for checksum function '''
    (rc, out, err) = module.run_command("echo testforchecksum | md5sum")
    assert checksum_s("testforchecksum", _md5) == out.split()[0]

if __name__ == "__main__":
    # Unit test for function checksum
    module.exit_json(changed=True, msg="Unit test for function checksum")

# Generated at 2022-06-13 16:10:42.599138
# Unit test for function checksum
def test_checksum():
    data = {"filename": "test_checksum.py", "checksum": "599b8e3c86a88e2cce7f234cd9adbf15b90ac1ac"}
    assert checksum(data['filename']) == data['checksum']
    data = {"filename": "test_checksum.py", "md5sum": "599b8e3c86a88e2cce7f234cd9adbf15"}
    assert md5(data['filename']) == data['md5sum']



# Generated at 2022-06-13 16:10:44.434779
# Unit test for function md5s
def test_md5s():
    assert md5s('string') == 'ae2b1fca515949e5d54fb22b8ed95575'


# Generated at 2022-06-13 16:10:51.910085
# Unit test for function checksum
def test_checksum():
    assert secure_hash_s('Hello World') == '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    assert secure_hash_s(u'Hello World') == '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    assert secure_hash_s(b'Hello World') == '2ef7bde608ce5404e97d5f042f95f89f1c232871'

    assert secure_hash('/bin/ls') == '1f9c9f32f9b57d0fb494765fa6d0322cc0d33124'

# Generated at 2022-06-13 16:10:57.130282
# Unit test for function md5s
def test_md5s():
    s = 'hello world'
    h1 = md5s(s)
    h2 = md5s(s)
    assert h1 == h2
    assert len(h1) == 32
    assert md5s(s) == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:11:00.157010
# Unit test for function md5s
def test_md5s():
    s = md5s('test')
    assert s == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:11:11.581338
# Unit test for function md5
def test_md5():
    ''' md5.py: Test md5 function '''
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    from ansible.module_utils.common.hash import md5

    class TestMD5(unittest.TestCase):
        @patch('ansible.module_utils.common.hash.os.path.exists')
        def test_os_exists(self, mock_exists):
            ''' calling md5 with a filename when os.path.exists returns False should return None '''
            mock_exists.return_value = False
            filename = 'test_filename'
            expected = None
            result = md5(filename)
            self.assertEqual(expected, result)


# Generated at 2022-06-13 16:11:20.127618
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(u'hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'

    # For this to work, the file must be named: test/test-utils/hello
    # In the checkout of the source tree.
    assert md5('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:11:29.449191
# Unit test for function checksum
def test_checksum():
    '''
    ansible.utils.crypto: Test for function checksum
    '''

    # Checks with a temporary file
    from tempfile import mkstemp
    from shutil import copyfileobj
    from ansible.module_utils.six import StringIO

    # The content of the temporary file
    content = StringIO(b"Sample content")

    # Create a temporary file and compute the checksum
    (handle, filename) = mkstemp()
    with os.fdopen(handle, 'wb') as f:
        copyfileobj(content, f)

    computed_checksum = secure_hash(filename)

    # Known sha1 for this content
    known_checksum = 'd2f7c3b889a94d7f5cfdbbb9c7a1f5fc1c0e357d'

    os

# Generated at 2022-06-13 16:11:40.727535
# Unit test for function md5s
def test_md5s():

    test_hash = "b4fa9be790df4b4f24b7da7c5605560d"

    assert md5s("test") == test_hash

    # test that md5s produces consistent results when called multiple times
    assert md5s("test") == test_hash
    assert md5s("test") == test_hash
    assert md5s("test") == test_hash
    assert md5s("test") == test_hash

    # test that md5s produces correct results for unicode input
    assert md5s(u"test") == test_hash
    assert md5s(u"test") == test_hash
    assert md5s(u"test") == test_hash
    assert md5s(u"test") == test_hash

    # test that md5s produces correct results for bytes input
   

# Generated at 2022-06-13 16:11:50.655955
# Unit test for function checksum
def test_checksum():
    from tempfile import NamedTemporaryFile
    from shutil import copyfileobj

    for hash_function in [sha1, _md5]:
        # Create a temporary file with some content
        t_file = NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 16:11:56.758142
# Unit test for function checksum
def test_checksum():
    filename = os.path.join(os.path.dirname(__file__), 'hashlib_test_file')
    expected_sha1 = '913b3e7ff6d3f95461a7f039b352c04d6a30b818'
    sha1_digest = checksum(filename)
    assert sha1_digest == expected_sha1, "checksum mismatch, expected %s, got %s" % (expected_sha1, sha1_digest)

    expected_md5 = '5e9fc5a54a96f4f4d4f4a4d48b304653'
    md5_digest = md5(filename)

# Generated at 2022-06-13 16:12:04.670241
# Unit test for function checksum
def test_checksum():
    """ returns a tuple of True/False in the form of
    (was test successful, test id, success message, error message)
    """
    # test for file checksum
    filename = 'hacking/env-setup'
    test_hash = "ed61b560c38ee71d7fd8e34505739329f1cf96f9"
    res = checksum(filename)
    if checksum(filename) == test_hash:
        return (True, 0, "checksum test passed", "")
    else:
        return (False, 0, "checksum test failed", "should have returned %s , got %s" % (test_hash, res))


# Generated at 2022-06-13 16:12:12.558741
# Unit test for function checksum
def test_checksum():
    assert checksum("https://www.ansible.com/") ==  "4897a2d49a5ef6c516eff3b9c9e13d2f21a200d8"
    #the following test will fail if you don't have access to https://www.ansible.com/
    assert checksum("https://www.ansible.com/robots.txt") == "5e5f2d0e0d6c5ad6b568c8222896a7e0"

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:16.665535
# Unit test for function checksum
def test_checksum():
    assert checksum("/etc/hosts") == "28d8e895771612b9f0dcdaffd38d542e"


# Generated at 2022-06-13 16:12:22.417801
# Unit test for function md5s
def test_md5s():
    # Check that a known string has an expected MD5
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    # Check that a Unicode string has an expected MD5
    assert md5s(u'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:12:27.920580
# Unit test for function md5s
def test_md5s():
    assert md5s(b"abc") == "900150983cd24fb0d6963f7d28e17f72"



# Generated at 2022-06-13 16:12:38.853476
# Unit test for function checksum
def test_checksum():
    filename = "/etc/ansible/hosts"
    assert checksum(filename) == checksum(filename)
    assert checksum_s(b"123") == "40bd001563085fc35165329ea1ff5c5ecbdbbeef"
    # Assumes the file /etc/ansible/hosts contains only one line
    # localhost ansible_connection=local
    assert checksum_s(b"localhost ansible_connection=local") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

# Generated at 2022-06-13 16:12:43.430529
# Unit test for function md5
def test_md5():
    filename = "./lib/ansible/utils/md5sums"
    assert md5(filename) == "c2bcf42cab0a9d97416c31b67a65b8a8"


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:46.721539
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5('/etc/passwd') == 'a448017fadc10d7bda1b02e96ce7fdd0'

# unit test for function md5s

# Generated at 2022-06-13 16:12:51.792343
# Unit test for function checksum
def test_checksum():
    checksum_val = checksum(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../lib/ansible/utils/__init__.py'))
    assert checksum_val == '33a05f34d73e76ccb5f22f91cc2c98e75484f14f'

# Generated at 2022-06-13 16:12:55.369843
# Unit test for function checksum
def test_checksum():
    filename = './test/test_utils.py'
    result = checksum(filename)
    answer = '172b3f31393d76b32b837df3e788ef64d2a94a1e'
    assert result == answer


# Generated at 2022-06-13 16:13:00.888409
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/hosts') == '9df3b09a11cdf8ecdc1a6d4c3d8f6ae3a34e0242'
    assert checksum_s('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'



# Generated at 2022-06-13 16:13:07.423974
# Unit test for function checksum
def test_checksum():
    path='./hacking/test/utils/checksum'
    assert checksum(path) == '0cc175b9c0f1b6a831c399e269772661'
    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:13:13.260416
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f"
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"


__all__ = ['secure_hash_s', 'secure_hash', 'checksum_s', 'checksum', 'md5s', 'md5']

# Generated at 2022-06-13 16:13:18.012400
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert secure_hash_s(b'1234', _md5) == md5s(b'1234')
    else:
        import pytest
        with pytest.raises(ValueError):
            md5s(b'1234')

# Generated at 2022-06-13 16:13:26.700325
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    expected_result = 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo') == expected_result
    assert md5s('foo\x00') == expected_result
    assert md5s('foo\x00\r') != expected_result
    print("test_md5s(): ok")


# Generated at 2022-06-13 16:13:33.531427
# Unit test for function md5
def test_md5():
    ''' test_md5 '''
    test_data = "hello world"
    test_file = "test_file"
    test_md5 = md5s(test_data)
    assert test_md5 == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    open(test_file, 'w').close()
    test_md5 = md5(test_file)
    assert test_md5 == 'd41d8cd98f00b204e9800998ecf8427e'

    f = open(test_file, 'w')
    f.write(test_data)
    f.close()
    test_md5 = md5(test_file)

# Generated at 2022-06-13 16:13:46.027241
# Unit test for function md5
def test_md5():

    test_data = {
        'string': "hi",
        'unicode': u"hi",
        'file': "file.txt",
        'nofile': "nofile.txt"
    }
    assert md5s(test_data['string']) == '49f68a5c8493ec2c0bf489821c21fc3b', "Failed to calculate md5 of string"
    assert md5s(test_data['unicode']) == '49f68a5c8493ec2c0bf489821c21fc3b', "Failed to calculate md5 of unicode"

# Generated at 2022-06-13 16:13:50.758930
# Unit test for function md5s
def test_md5s():
    assert md5s(b'hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:13:52.733349
# Unit test for function md5
def test_md5():
    digest = md5('/etc/passwd')
    assert len(digest) == 32


# Generated at 2022-06-13 16:13:54.732451
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:13:57.543396
# Unit test for function md5s
def test_md5s():
    data = b"Hello World!"
    assert(md5s(data) == "b10a8db164e0754105b7a99be72e3fe5")

# Generated at 2022-06-13 16:14:08.748695
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile

    # Write some data to a temporary file and calculate its md5 checksum
    test_data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tfile = NamedTemporaryFile(delete=False)
    tfile.write(to_bytes(test_data, errors='surrogate_or_strict'))
    tfile.close()

    md5sum = md5(tfile.name)
    os.unlink(tfile.name)

    # Verify checksum

# Generated at 2022-06-13 16:14:12.384385
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('world') == '7d793037a0760186574b0282f2f435e7'


# Generated at 2022-06-13 16:14:20.342417
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.six import PY3
    from hashlib import sha1, sha256, sha512

    if not PY3:
        from ansible.module_utils.pycompat24 import md5

    test_string = '''This is a test of the emergency broadcast system.'''
    test_string_bytes = '''This is a test of the emergency broadcast system. bytes'''.encode('utf-8')
    test_string_unicode = '''This is a test of the emergency broadcast system. unicode'''


# Generated at 2022-06-13 16:14:33.747016
# Unit test for function checksum
def test_checksum():
    ''' test_checksum()  - checksum() is a wrapper around secure_hash()
        which runs in FIPS mode.  Checksum should not be used for
        new code.  It is kept for backwards compatibility.

        Checksum() can also return md5sums.  As of ansible-1.8, modules
        should return sha1 sums via "checksum" instead of md5 sums

        Modules which need to return md5 sums for backwards compatibility
        should use "md5" instead of "checksum"
    '''

    test_fname = 'test_checksum.txt'
    test_fname_out = 'test_checksum_out.txt'
    test_fname_out2 = 'test_checksum_out2.txt'


# Generated at 2022-06-13 16:14:38.486586
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:14:45.076703
# Unit test for function md5
def test_md5():
    import random
    import string
    random = random.SystemRandom()
    # Can't use os.urandom here because it will always return the same value
    char_set = string.ascii_uppercase + string.digits
    rand_string = ''.join(random.choice(char_set) for _ in range(20))
    h = md5s(rand_string)

    import hashlib
    m = hashlib.md5()
    m.update(rand_string)
    ph = m.hexdigest()
    if ph != h:
        raise Exception("Test failed", h, ph)
    else:
        print("Md5 test passed")

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:14:48.418205
# Unit test for function md5s
def test_md5s():
    assert md5s("ansible") == "80c6a1444ec07ffb12e9f9aac7f2fa88"

# Generated at 2022-06-13 16:14:58.231283
# Unit test for function md5
def test_md5():
    """
    md5 unit test
    """
    assert md5("/bin/cat") == "c9e0b7c15f1a21a67b8a8b64f4e4bc4a"
    assert md5("/bin/echo") == "e5e7b0b5fb5b5ecb69f4b0e7d13e0e68"
    assert md5("/bin/sh") == "3d3a2ac2ac83b30ac26efd964e86a1c1"
    assert md5("/bin/invalid-file") == None
    assert md5("/bin") == None
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2022-06-13 16:15:01.978241
# Unit test for function md5s
def test_md5s():
    assert md5s('ansible') == 'c33d91ad49e517580c378ef577a0c01f'
    assert md5s('ansible1') == 'a5f5e8fb5b2e2e7c24aac9ee0cab07f1'
    assert md5s('ansible2') == '1af170fa251dad62fa9b9fa8c0d4f2e4'
    assert md5s('ansible3') == 'ec1b047c9eb2d02d972fddfff95bfdcb'

# Generated at 2022-06-13 16:15:05.558947
# Unit test for function md5s
def test_md5s():
    import pytest
    md5s = md5s('abcd')
    assert md5s == 'e2fc714c4727ee9395f324cd2e7f331f'

# Unit test

# Generated at 2022-06-13 16:15:10.429318
# Unit test for function md5
def test_md5():
    my_file = '/tmp/test.txt'
    result ='e807f1fcf82d132f9bb018ca6738a19f'
    f = open(my_file, 'w')
    f.write('test123')
    f.close()
    assert md5(my_file) == result
    os.remove(my_file)

# Generated at 2022-06-13 16:15:12.716362
# Unit test for function md5
def test_md5():
    return md5('lib/ansible/module_utils/basic.py') == '9acd0f1a06a59c41a8b529f423af0c47'

# Generated at 2022-06-13 16:15:16.143996
# Unit test for function md5s
def test_md5s():
    md5s_expected = '81dc9bdb52d04dc20036dbd8313ed055'
    md5s_result = md5s('test')
    assert md5s_result == md5s_expected, 'test_md5s: expected %s, but got %s' % (md5s_expected, md5s_result)

# Generated at 2022-06-13 16:15:24.733055
# Unit test for function md5
def test_md5():
    if _md5:
        assert md5("/bin/ls") == "6b8be1ad9f2dcf226ba103542a1a5c1c"
        assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"

# Generated at 2022-06-13 16:15:31.417646
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return

    # generated via: md5sum /etc/redhat-release on Fed22 machine
    assert md5s("Red Hat Enterprise Linux Workstation release 7.0 (Maipo)") == "86d4a791d4af1f2c655e69ea9e7bf491"


# Generated at 2022-06-13 16:15:33.667072
# Unit test for function md5
def test_md5():
    d = md5s("something")
    assert d == "3949d6a7d55c46bbd35e8c0e1e90ac97"

# Generated at 2022-06-13 16:15:36.384371
# Unit test for function md5
def test_md5():
    assert md5s(b"foobar") == "acbd18db4cc2f85cedef654fccc4a4d8"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:15:39.621329
# Unit test for function md5
def test_md5():
    fd, testfile = tempfile.mkstemp()
    os.write(fd, b'hello')
    os.close(fd)
    assert '5d41402abc4b2a76b9719d911017c592' == md5(testfile)

# Generated at 2022-06-13 16:15:50.048626
# Unit test for function checksum
def test_checksum():
    # Test with good parameters
    try:
        assert(checksum('test/utils/test_checksum.py') == checksum('test/utils/test_checksum.py'))
        assert(checksum('test/utils/test_checksum.py') != checksum('test/utils/test_checksum2.py'))
    except AssertionError:
        raise AssertionError

    # Test with bad parameters
    try:
        assert(checksum('test/utils/test_checksum.py') != checksum('tests/utils/test_checksum.py'))
    except AssertionError:
        raise AssertionError

    # Test with nonexistent file
    try:
        assert(checksum('test/utils/test_checksum.fake') == None)
    except AssertionError:
        raise Assert

# Generated at 2022-06-13 16:15:52.568967
# Unit test for function md5
def test_md5():

    """Return a message showing that the function was tested
    """

    return "Test of md5 function passed"


if __name__ == '__main__':
    print(test_md5())

# Generated at 2022-06-13 16:16:00.957020
# Unit test for function md5s
def test_md5s():
    ''' unit test for function "md5s" '''
    import sys
    if sys.hexversion >= 0x2070000 :
        assert secure_hash_s(u"abc") == md5s(u"abc")
        assert secure_hash_s(u"abc".encode('utf-8')) == md5s(u"abc")
    else:
        assert secure_hash_s("abc") == md5s("abc")
        assert secure_hash_s("abc".encode('utf-8')) == md5s("abc")



# Generated at 2022-06-13 16:16:05.540615
# Unit test for function md5
def test_md5():
    print("md5_s('hello world')=%s" % md5s("hello world"))
    print("md5('setup.py')=%s" % md5("setup.py"))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:08.226101
# Unit test for function md5s
def test_md5s():
    assert md5s('blahblah') == '4e1aef314e0e326a14f4830c5d682e68'


# Generated at 2022-06-13 16:16:22.546543
# Unit test for function md5s
def test_md5s():

    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('ab') == '187ef4436122d1cc2f40dc2b92f0eba0'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'
    assert md5s('abcde') == 'ab56b4d92b40713acc5af89985d4b786'
    assert md5s('abcdefg') == 'e80b5017098950fc58aad83c8c14978e'

# Generated at 2022-06-13 16:16:25.774877
# Unit test for function md5
def test_md5():
    if md5(__file__) == '4bc8c4d9a6877f064e26ddbacfc8d0f5':
        return 'ok'
    else:
        return 'not ok'

# Generated at 2022-06-13 16:16:32.998169
# Unit test for function md5
def test_md5():
    import tempfile

    filename = tempfile.mktemp()

    try:
        file(filename, "wb").write("foobar")
        assert md5(filename) == "3858f62230ac3c915f300c664312c63f", md5(filename)
    finally:
        os.unlink(filename)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    test_md5()

# Generated at 2022-06-13 16:16:40.969532
# Unit test for function md5s
def test_md5s():
    test_file_checksum = 'd41d8cd98f00b204e9800998ecf8427e'
    test_file_checksum_large = 'c1c9b8af42d1d80bb76ba0e20e39b35c'

    assert md5s('') == test_file_checksum
    assert md5s('teststring') == '098f6bcd4621d373cade4e832627b4f6'

    if os.path.exists('test_md5s.txt'):
        # test_md5s.txt is a 8MB file with a known md5sum
        # the md5 function will read in 64Kish chunks
        assert md5('test_md5s.txt') == test_file_checksum_large


# Generated at 2022-06-13 16:16:43.054273
# Unit test for function md5
def test_md5():
    assert md5("/bin/sh") == '3f36c3e70d2b2c08d1dc18b1f47b57d0'

# Generated at 2022-06-13 16:16:45.368177
# Unit test for function md5
def test_md5():
    assert md5(__file__) == 'b976198e4bf2a8c0061fec4bcaa6c04f'


# Generated at 2022-06-13 16:16:49.281816
# Unit test for function checksum
def test_checksum():
    file = os.path.realpath(__file__)
    assert checksum(file) == secure_hash(file)
    assert checksum_s(file) == secure_hash_s(file)


# Generated at 2022-06-13 16:16:58.889711
# Unit test for function checksum
def test_checksum():
    # invalid file path
    assert checksum('not_a_file') is None

    # file not found
    bogus_file = '/tmp/ansible-test-file-not-found'
    assert checksum(bogus_file) is None

    # actual file
    file_name = 'test/units/modules/test_template.j2'
    expected = 'e188b8f9c906e4215a51f0dd0f8022eab6a2b2c0'
    assert checksum(file_name) == expected



# Generated at 2022-06-13 16:17:05.753959
# Unit test for function md5s
def test_md5s():
    if _md5:
        # MD5 should always return the same value for a given string
        assert md5s("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"
        assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    else:
        md5s("")
        assert True, 'md5s did not raise a ValueError'


# Generated at 2022-06-13 16:17:09.532775
# Unit test for function md5
def test_md5():
    assert md5(__file__) == md5(__file__)
    assert md5(__file__) != md5('/bin/ls')
    assert md5s('data_string') == md5s('data_string')
    assert md5s('data_string') != md5s('data_string_2')

# Generated at 2022-06-13 16:17:15.742860
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.six import b
    assert md5s('blah') == b('8d777f385d3dfec8815d20f7496026dc')

# Generated at 2022-06-13 16:17:27.098355
# Unit test for function checksum
def test_checksum():
    ''' checksum should create a perfect hash for unicode and ascii strings '''
    
    import sys
    
    #
    # Python 2.4 does not have hashlib, and md5 is deprecated then
    #
    if sys.version_info[0] == 2 and sys.version_info[1] == 4:
        import md5
        test_string = u'hello'
        test_hash = '5d41402abc4b2a76b9719d911017c592'
    else:
        import hashlib
        test_string = u'hello'
        test_hash = '5d41402abc4b2a76b9719d911017c592'
    
    #
    # If we're running in FIPS mode, skip the tests
    # 

# Generated at 2022-06-13 16:17:30.079040
# Unit test for function md5
def test_md5():
    d = md5s('hello')
    assert d == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:17:34.380294
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    test_string = 'hi'
    assert md5s(data=test_string) == '49f68a5c8493ec2c0bf489821c21fc3b'


# Generated at 2022-06-13 16:17:39.937947
# Unit test for function md5s
def test_md5s():
    '''Unit test for function md5s'''
    import unittest
    try:
        md5s('foo')
    except ValueError:
        # Test passes if exception is raised
        pass
    else:
        raise unittest.SkipTest("MD5 is available")

# Generated at 2022-06-13 16:17:42.767605
# Unit test for function md5s
def test_md5s():
    input = 'test'
    result = md5s(input)
    assert result == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:17:48.150914
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == md5s(b'/bin/ls') == 'f5d66dff8a9ece5ee5d89c9bb1b5da5c'
    assert md5('/bin/grep') == md5s(b'/bin/grep') == '5e5294ad0c30b7a79a22a2f8133562e5'



# Generated at 2022-06-13 16:17:51.209157
# Unit test for function md5
def test_md5():
    filename = "/etc/passwd"
    assert md5(filename) == "4b0250e756022350dabddd798b664279"
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"



# Generated at 2022-06-13 16:17:57.623657
# Unit test for function checksum
def test_checksum():
    def check_checksum(filename, checksum_type="sha1"):
        if checksum_type == "sha1":
            assert secure_hash(filename) == secure_hash(filename)
        else:
            assert md5(filename) == md5(filename)
    check_checksum("/dev/null")
    check_checksum("/dev/null", checksum_type="md5")

# Generated at 2022-06-13 16:18:08.661759
# Unit test for function md5s
def test_md5s():
    from ansible.compat.tests import unittest
    import sys

    class TestMd5s(unittest.TestCase):
        def test_md5s(self):
            self.assertEqual(md5s(b'foo'), b"acbd18db4cc2f85cedef654fccc4a4d8")
            # With Python3, we also have to test for the type of
            # md5s as it depends on the type of the input.
            # With Python2, this will always be a str.
            if sys.version_info[0] >= 3:
                self.assertEqual(type(md5s(b'foo')), str)
                self.assertEqual(type(md5s(u'foo')), str)

# Generated at 2022-06-13 16:18:15.054762
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == '6b8be1e9d5189a4aa6fe707f602e97f6'


# Generated at 2022-06-13 16:18:18.522832
# Unit test for function checksum
def test_checksum():
    sha1_sum = '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    sha1_sum_s = 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

    assert secure_hash('/bin/ls', sha1) == sha1_sum
    assert secure_hash_s('hello, world', sha1) == sha1_sum_s

# Generated at 2022-06-13 16:18:26.726230
# Unit test for function md5s
def test_md5s():
    import os
    import tempfile

    fd, fname = tempfile.mkstemp()
    f = os.fdopen(fd, "w+b")
    f.write("some test data")
    f.close()
    assert md5(fname) == "4f1b94e52d78a7e9c913f5a827bbc76d"
    os.remove(fname)


# Generated at 2022-06-13 16:18:29.841109
# Unit test for function md5s
def test_md5s():
    print(md5s('test data'))
    print(md5('/etc/passwd'))

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:18:32.500941
# Unit test for function md5s
def test_md5s():

    text = 'abcdefghijklmnopqrstuvwxyz'
    assert md5s(to_bytes(text)) == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:18:40.073492
# Unit test for function checksum
def test_checksum():
    try:
        import doctest

        # Some modules, including this one, have tests written using the
        # python standard library doctest module.  The following block of
        # code allows those tests to run when the module is run standalone
        # as well as when it is imported as a module.
        # See:  http://code.activestate.com/recipes/577452-standalone-unit-test-for-doctest-code-unit-test-p/
        if __name__ == '__main__':
            doctest.testmod()
    except ImportError:
        pass
    return

# Generated at 2022-06-13 16:18:51.457474
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils import basic
    if not basic.HAVE_HASHLIB:
        raise ValueError('Test cannot be run.  Possibly running in FIPS mode')

    if md5s('blah') != "8fc3f093ee6dcd2e2c99772dd04f78b5":
        raise AssertionError('md5s test failed')

    if os.path.exists('/etc/passwd'):
        try:
            md5('/etc/passwd')
        except ValueError:
            raise AssertionError('md5 test failed')

        if md5('/etc/passwd') != "e47d7f25e34f3ec843f3e061e7cf2d2b":
            raise AssertionError('md5 test failed')


# Generated at 2022-06-13 16:18:56.818862
# Unit test for function md5s
def test_md5s():
    if _md5:
        # Force md5s to be called even if above md5s is not called,
        # because md5 might raise exception if this system is FIPS-140
        # compliant.
        md5s('abc')

# Generated at 2022-06-13 16:19:03.084115
# Unit test for function md5s
def test_md5s():
    assert md5s('My test string\n') == '4c4dd9d9f7e1f6e0e7d2409f8743c8d8'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s(None) == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s(13) == 'd41d8cd98f00b204e9800998ecf8427e'


# Generated at 2022-06-13 16:19:09.672015
# Unit test for function md5s
def test_md5s():
    """
    md5s: Return a secure hash in hex format for the given string using MD5.
    """
    test_string = '''
        The quick brown fox jumps over the lazy dog.
        '''

    # The checksum of the given test string must be the following:
    test_checksum = 'de9f2c7fd25e1b3afad3e85a0bd17d9b100db4b3'

    # test md5s
    assert md5s(test_string) == test_checksum


# Generated at 2022-06-13 16:19:15.798080
# Unit test for function md5s
def test_md5s():
    assert md5s('hi there') == '49f68a5c8493ec2c0bf489821c21fc3b'

# Generated at 2022-06-13 16:19:18.002384
# Unit test for function md5
def test_md5():
    assert md5("ansible/module_utils/basic.py") == "a8b73d420f9203e0f9b2d47d8f6c1fc6"

# Generated at 2022-06-13 16:19:20.326825
# Unit test for function md5s
def test_md5s():
    data="Hello World"
    assert md5s(data)=="65a8e27d8879283831b664bd8b7f0ad4"


# Generated at 2022-06-13 16:19:23.449660
# Unit test for function md5s
def test_md5s():
    '''
    SHA-1 is preferred, and this is a bit of a test against change.
    The output of this function may change if ansible is run in FIPS mode
    '''
    assert md5s('testdata') == '6f8db599de986fab7a21625b7916589c'


# Generated at 2022-06-13 16:19:26.615940
# Unit test for function checksum
def test_checksum():
    assert checksum(__file__) == 'a0a0a9b9f964edfcada6e09db951c69d6ea1f8e3'

# Generated at 2022-06-13 16:19:30.587375
# Unit test for function md5s
def test_md5s():

    result = md5s('hello')
    assert result == '5d41402abc4b2a76b9719d911017c592', result
    result = md5s('hello')
    assert result == '5d41402abc4b2a76b9719d911017c592', result


# Generated at 2022-06-13 16:19:33.238822
# Unit test for function md5s
def test_md5s():
    data = "hello"
    checksum = md5s(data)
    assert checksum == "5d41402abc4b2a76b9719d911017c592"


# Generated at 2022-06-13 16:19:40.073460
# Unit test for function md5
def test_md5():
    from tempfile import mkstemp

    fd, f = mkstemp()
    try:
        with os.fdopen(fd, 'w') as fd:
            fd.write("this is a test")
        if not md5(f) == "81dc9bdb52d04dc20036dbd8313ed055":
            raise Exception("md5 broken")
        if not md5s("this is a test") == "81dc9bdb52d04dc20036dbd8313ed055":
            raise Exception("md5s broken")
    finally:
        os.unlink(f)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:19:44.195013
# Unit test for function md5
def test_md5():
    test_str = 'pennyroyal tea'
    assert md5s(test_str) == "5ea0f5ff5061d8465322308c7f75bb5c"

if __name__ == '__main__':
    print(md5s('pennyroyal tea'))
    print(md5('boondock_saints.jpg'))

# Generated at 2022-06-13 16:19:48.448570
# Unit test for function md5
def test_md5():
    # In FIPS-140-2 mode, it should return ValueException
    # In non FIPS-140-2 mode, it should return hash value of file
    if _md5:
        assert md5("/etc/hosts") == "3f5b0860a0d8f7e07f32e1a7a0a8a14c"
    else:
        try:
            md5("/etc/hosts")
        except ValueError:
            return True
        else:
            return False

# Generated at 2022-06-13 16:19:54.050899
# Unit test for function md5
def test_md5():
    data = 'foo bar'
    assert md5s(data) == 'f7bc83f430538424b13298e6aa6fb143'



# Generated at 2022-06-13 16:19:57.188750
# Unit test for function md5
def test_md5():
    if _md5:
        # ensure we're compatible with Python's hashlib
        assert(md5('setup.py') == 'acb5a5f1273924c9aaf0f7dcafb37039')
        assert(md5('setup.py') == secure_hash('setup.py', _md5))