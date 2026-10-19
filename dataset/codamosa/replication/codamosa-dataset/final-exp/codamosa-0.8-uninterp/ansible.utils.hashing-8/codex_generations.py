

# Generated at 2022-06-13 16:10:01.329247
# Unit test for function md5
def test_md5():
    assert md5('/tmp/fakefile') is None
    assert md5('/dev') is None
    try:
        md5s('hello')
    except ValueError:
        pass

# Generated at 2022-06-13 16:10:11.675359
# Unit test for function checksum
def test_checksum():
    '''Unit test for checksum function'''

    import tempfile

    with tempfile.NamedTemporaryFile() as tmp:

        # Test success with file
        f = tmp.write(b'foobar')
        tmp.flush()
        # Function should return a string
        assert isinstance(checksum(tmp.name), str)
        # Should match known value
        assert checksum(tmp.name) == '8843d7f92416211de9ebb963ff4ce28125932878'

        # Test failure with directory
        assert checksum('/tmp') is None

        # Test failure with non-existent file
        assert checksum('/tmp/foobar') is None


# Generated at 2022-06-13 16:10:13.366424
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:10:19.510765
# Unit test for function checksum
def test_checksum():
    import tempfile
    import random

    fd, tf = tempfile.mkstemp()
    b = os.urandom(random.randint(1,1024*1024))
    os.write(fd, b)
    os.close(fd)
    assert checksum(tf) == checksum_s(b), "%s != %s" % (checksum(tf), checksum_s(b))
    os.unlink(tf)


# Generated at 2022-06-13 16:10:30.392057
# Unit test for function checksum
def test_checksum():
    test_sha = 'd95c61dfea57a2e4cbfb4a4f14d4e944f7e4582b'
    test_md5 = 'd41d8cd98f00b204e9800998ecf8427e'
    test_file = open('test_file', 'w')
    test_file.write('This is a test file')
    test_file.close()
    if secure_hash('test_file') != test_sha:
        raise Exception('SHA of file failed')
    if secure_hash_s('This is a test file') != test_sha:
        raise Exception('SHA of string failed')
    if _md5 and secure_hash('test_file', _md5) != test_md5:
        raise Exception('MD5 of file failed')

# Generated at 2022-06-13 16:10:35.845724
# Unit test for function checksum
def test_checksum():
    import sys
    if sys.version_info.major == 2:
        data = "The quick brown fox jumps over the lazy dog"
    else:
        data = "The quick brown fox jumps over the lazy dog".encode("utf-8")

    expected = "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"
    actual = checksum_s(data)
    assert(expected == actual), "checksum_s failed with python3, expected %s got %s" % (expected, actual)

# Generated at 2022-06-13 16:10:39.670254
# Unit test for function md5
def test_md5():
    """
    Checksum:function:md5 test
    """
    assert md5("/bin/ls") == '1ac8c83d0a1e3a41f0ca0f8c46e47a9c'

# Generated at 2022-06-13 16:10:46.173200
# Unit test for function checksum
def test_checksum():
    # Execute checksum function and check results
    filename = "test_checksum_file.txt"
    data = "Test checksum function\n"

    fh = open(filename, "wb")
    fh.write(data)
    fh.close()

    if checksum(filename) == sha1(data).hexdigest():
        # Cleanup the test file
        os.remove(filename)

        # Test passed
        return
    else:
        # Cleanup the test file
        os.remove(filename)

        # Test failed
        raise Exception("test_checksum() failed")


# Generated at 2022-06-13 16:10:50.848814
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s("test") == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:10:55.936198
# Unit test for function checksum
def test_checksum():
    import tempfile

    filename = tempfile.mktemp()
    try:
        f=open(filename, 'w')
        f.write('hello, world')
        f.close()
        assert checksum(filename) == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed', checksum(filename)
        assert checksum_s('hello, world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed', checksum_s('hello, world')
    finally:
        os.unlink(filename)

# Generated at 2022-06-13 16:11:09.569333
# Unit test for function checksum
def test_checksum():
    data = b''
    assert checksum_s(data) == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    assert checksum_s(data, sha1) == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    assert checksum_s(data, _md5) == 'd41d8cd98f00b204e9800998ecf8427e'
    assert checksum_s(data, lambda: _md5()) == 'd41d8cd98f00b204e9800998ecf8427e'

# Generated at 2022-06-13 16:11:20.191552
# Unit test for function md5
def test_md5():

    '''
    This function is used to unit test md5 function
    '''
    import unittest
    import os
    import tempfile
    import time
    import textwrap

    class TestSequenceFunctions(unittest.TestCase):

        '''
        This class is used for test md5 function
        '''

        def setUp(self):
            '''
            This function is called before test_md5 function
            '''
            self.test_file = tempfile.NamedTemporaryFile()

        def tearDown(self):
            '''
            This function is called after test_md5 function
            '''
            self.test_file.close()
            del self.test_file


# Generated at 2022-06-13 16:11:26.653369
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('test') == md5s(b'test')
    assert md5('changelogs/CHANGELOG-v1.8.0.txt') == '44b4a262cdbbb8ddb0edeb55fde5b7cc'


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:38.914520
# Unit test for function md5s
def test_md5s():
    # FIPS mode is only enabled when using the file module, which is done in a
    # separate process.  Let's see if we can trick it into thinking we're in FIPS
    # mode.
    with open('/proc/sys/crypto/fips_enabled', 'wb') as f:
        f.write(b'1')

    try:
        # This should raise an error
        md5s('asdf')
    except ValueError:
        # Good, we're in FIPS mode.  Revert the changes.
        with open('/proc/sys/crypto/fips_enabled', 'wb') as f:
            f.write(b'0')
    else:
        assert False, 'md5s is available when it should not be'



# Generated at 2022-06-13 16:11:41.778603
# Unit test for function md5
def test_md5():
    data = 'test'
    assert md5(data) == '6f8db599de986fab7a21625b7916589c'
    assert md5s(data) == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:11:43.392180
# Unit test for function md5s
def test_md5s():
    import doctest
    doctest.testmod(md5s)

# Generated at 2022-06-13 16:11:48.338731
# Unit test for function md5
def test_md5():
    assert md5('/etc/hosts') == '04ed6dd9a6ba7a01d91b3b7ff3c3f685'
    assert md5('/etc/passwd-') is None
    assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'



# Generated at 2022-06-13 16:11:52.550893
# Unit test for function md5
def test_md5():
    assert md5('__init__.py') == '0ed4e8ca64a8a7a27a9e3abf6c1e91e7'

# Test function md5s

# Generated at 2022-06-13 16:12:00.343343
# Unit test for function md5
def test_md5():
    assert md5('/etc/passwd') == '18215b78c29eec47cba8e2e54b16364c'
    assert md5('/bin/ls') == 'e699f072d1d4c4e840a71900b3cdb0d7'
    assert md5('/bin/false') == 'f7d8c874b36734c0bcc77f82cec9e9f5'
    assert md5('/bin/true') == 'b82e7e5cde1914a742c8f48f02dfa3a3'

# Generated at 2022-06-13 16:12:10.074712
# Unit test for function md5s
def test_md5s():
    import random
    import string
    def randomString(length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    # test case from `man 3 md5`
    if md5s('The quick brown fox jumps over the lazy dog') != '9e107d9d372bb6826bd81d3542a419d6':
        return False
    # test case from `man 3 md5`
    if md5s('The quick brown fox jumps over the lazy dog.') != 'e4d909c290d0fb1ca068ffaddf22cbd0':
        return False
    # check that md5s do not colide
    if md5s(randomString(100)) == md5s(randomString(100)):
        return False


# Generated at 2022-06-13 16:12:24.892414
# Unit test for function md5
def test_md5():
    import os

    # Checksum of an empty string
    if md5s("") != 'd41d8cd98f00b204e9800998ecf8427e':
        print("test_md5 1 failed")

    # Checksum of a string
    if md5s("This is a file") != 'a9e6e8fe90198ec221c2d2e2b1fad2c3':
        print("test_md5 2 failed")

    # Checksum of an empty file
    with open("slask_file", "w") as f:
        pass

    if md5("slask_file") != 'd41d8cd98f00b204e9800998ecf8427e':
        print("test_md5 3 failed")
    os.remove("slask_file")

    # Checksum

# Generated at 2022-06-13 16:12:31.256651
# Unit test for function checksum
def test_checksum():
    plain_text = "Hello World!"
    assert checksum_s(plain_text) == "0a4d55a8d778e5022fab701977c5d840bbc486d0", "Fail: checksum_s()"

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:33.915250
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:12:36.952107
# Unit test for function md5s
def test_md5s():
    "This should return the same result as 'echo -n string | md5sum'"
    if _md5:
        assert md5s('string') == '5a47d12a5e8f64441e2c8fd512e3d7dc'

# Generated at 2022-06-13 16:12:42.456228
# Unit test for function md5
def test_md5():
    try:
        digest = md5s('foo')
    except ValueError:
        digest = None
    assert digest

    assert md5('/etc/passwd')
    assert not md5('/etc/passwds')
    assert not md5('/etc/')

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:44.622813
# Unit test for function md5s
def test_md5s():
    assert md5s('val') == '2063c1608d6e0baf80249c42e2be5804'


# Generated at 2022-06-13 16:12:49.894149
# Unit test for function checksum
def test_checksum():
    assert checksum("/etc/passwd") == "f4a4c4d4f2b091e6bb0c6d81b6a0c6ca3bb6fbb8"
    assert checksum("helloworld") == 'ed076287532e86365e841e92bfc50d8c'


# Generated at 2022-06-13 16:12:52.939487
# Unit test for function md5s
def test_md5s():
    data = 'mystring'
    print('Using md5s')
    print('  string: %s' % data)
    print('    hash: %s' % md5s(data))


# Generated at 2022-06-13 16:13:01.286989
# Unit test for function md5
def test_md5():
    from shutil import copy
    from tempfile import mkstemp
    from os import remove, close

    (testfd, testfile) = mkstemp()
    test_string = 'test'
    test_digest = '098f6bcd4621d373cade4e832627b4f6'
    test_filename = '/etc/motd'

    # Test secure_hash_s
    assert secure_hash_s(test_string) == test_digest

    # Test secure_hash with string
    f = open(testfile, 'w')
    f.write(test_string)
    f.close()
    assert secure_hash(testfile) == test_digest

    # Test secure_hash with file object
    f = open(testfile, 'r')
    assert secure_hash(f) == test

# Generated at 2022-06-13 16:13:10.619791
# Unit test for function md5s
def test_md5s():
    ''' test_md5s '''
    if _md5:
        # Verify md5s() against md5sum(1)
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
        assert secure_hash_s('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    else:
        # Verify that md5s() works.  We don't have a known result to compare against.
        assert md5s('foo')

# Generated at 2022-06-13 16:13:15.199236
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == "098f6bcd4621d373cade4e832627b4f6"


# Generated at 2022-06-13 16:13:21.495877
# Unit test for function md5
def test_md5():
    md5_value = md5('/etc/passwd')
    if md5_value == '5e5a5a5d140e6b8d814b614526b6f0e6':
        print('Passed unit test!')
    else:
        print('Failed unit test!')


# Generated at 2022-06-13 16:13:23.568338
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:13:30.331920
# Unit test for function md5s
def test_md5s():
    '''
    Run the test from the command line
    python -c 'from ansible.utils.hashing import md5s; print md5s("hi")'
    '''
    msg = "hi"

    if _md5 is None:
        # FIPS mode
        assert md5s(msg) == "1f7c3f3d2c7ddbf109f2c0d0b8c87db7"

    else:
        # -AES modes
        assert md5s(msg) == "49f68a5c8493ec2c0bf489821c21fc3b"


# Generated at 2022-06-13 16:13:34.222641
# Unit test for function checksum
def test_checksum():
    data = 'hello'
    cksum_1 = checksum_s(data)
    assert cksum_1 == checksum(os.path.join(os.path.dirname(__file__), '../files/sha1sum_test'))

# Generated at 2022-06-13 16:13:40.948185
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum_s(u'hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'


# Generated at 2022-06-13 16:13:49.832228
# Unit test for function md5s
def test_md5s():
    """
    This is a simple unit test for the md5s function.
    """
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    # Testing with an empty string
    first_md5 = md5s("")
    if first_md5 != "d41d8cd98f00b204e9800998ecf8427e":
        raise ValueError("md5s failed to return the correct checksum")

    # Testing with a simple string
    second_md5 = md5s("hello world")
    if second_md5 != "5eb63bbbe01eeed093cb22bb8f5acdc3":
        raise ValueError("md5s failed to return the correct checksum")



# Generated at 2022-06-13 16:13:53.804885
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('world') == '7d793037a0760186574b0282f2f435e7'

# test_md5()

# Generated at 2022-06-13 16:13:57.732816
# Unit test for function md5
def test_md5():
    test_md5_val = md5s('test')
    assert test_md5_val == '098f6bcd4621d373cade4e832627b4f6', 'md5s() failed, got %s' % test_md5_val

# Generated at 2022-06-13 16:14:06.041850
# Unit test for function md5
def test_md5():

    # Create a file for input
    filename = "test"
    test_file = open(filename,"w")
    test_file.write("test")
    test_file.close()

    # Calculate the md5 hash
    m = md5(filename)

    # Remove the test file
    os.remove(filename)

    # Should return "7ea2a8f99fa7ac1fa60f1a7e64d8e8c7"
    return m


# Generated at 2022-06-13 16:14:10.937202
# Unit test for function md5s
def test_md5s():
    "Tests for the md5s function"
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"


# Generated at 2022-06-13 16:14:16.403018
# Unit test for function md5
def test_md5():
    import shutil
    import tempfile
    import os

    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'wb') as tmp:
            tmp.write(b"foo")

        # Test the function
        assert md5(path) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    finally:
        os.unlink(path)


# Generated at 2022-06-13 16:14:19.178817
# Unit test for function md5s
def test_md5s():
    assert len(sha1().hexdigest()) == len(md5s('hello'))
    # Test that md5s returns string value
    assert type(md5s('hello')) is str

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:14:21.602158
# Unit test for function md5s
def test_md5s():
    hash = md5s(to_bytes('hello'))
    assert hash == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:14:22.266882
# Unit test for function checksum
def test_checksum():
    print("test checksum")


# Generated at 2022-06-13 16:14:27.315310
# Unit test for function checksum
def test_checksum():
    ''' test_checksum is a utility function to test the checksum function '''
    print("testing checksum function")

    data = 'hello world'
    print("testing string checksum: %s" % checksum_s(data))

    filename = "checksum_test.txt"
    try:
        with open(filename, "w") as f:
            f.write(data)
        print("file %s written" % filename)
    except IOError as e:
        print("error writing test file %s, error was: %s" % (filename, e))

    print("testing file checksum: %s" % checksum(filename))

    os.remove(filename)
    print("file %s removed" % filename)

# Generated at 2022-06-13 16:14:33.069005
# Unit test for function checksum
def test_checksum():
    import tempfile
    tf = tempfile.NamedTemporaryFile()
    tf.write('foobar')
    tf.flush()
    s = checksum(tf.name)
    tf.close()
    print("Should be d3b07384d113edec49eaa6238ad5ff00: %s" % s)

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:14:44.345497
# Unit test for function checksum
def test_checksum():
    import tempfile, shutil
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    def _mock__md5_available():
        return True

    class TestChecksum(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.tmpdir)

        def test_sha1(self):
            (fd, fname) = tempfile.mkstemp(dir=self.tmpdir)
            f = os.fdopen(fd, 'w')
            f.write("foo")
            f.close()

# Generated at 2022-06-13 16:14:51.700513
# Unit test for function md5
def test_md5():
    import tempfile
    handle, path = tempfile.mkstemp()
    try:
        os.write(handle, b"foo\n")
        os.close(handle)
        os.path.isfile(path)
        assert md5(path) == "acbd18db4cc2f85cedef654fccc4a4d8"
    finally:
        os.unlink(path)



# Generated at 2022-06-13 16:15:01.005881
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('ab') == '187ef4436122d1cc2f40dc2b92f0eba0'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'
    assert md5s('abcde') == 'ab56b4d92b40713acc5af89985d4b786'

# Generated at 2022-06-13 16:15:06.284783
# Unit test for function md5s
def test_md5s():
    text = 'hello world!'
    assert(md5s(text) == '5eb63bbbe01eeed093cb22bb8f5acdc3')



# Generated at 2022-06-13 16:15:12.354503
# Unit test for function md5
def test_md5():
    # Create a test file
    (fd, fname) = tempfile.mkstemp()
    os.write(fd, b"abcdefg")
    os.close(fd)

    # Test if md5sum is correct
    if not md5(fname) == "7ac66c0f148de9519b8bd264312c4d64":
        raise Exception("Check failed on file: %s" % fname)

    # Delete the test file
    os.remove(fname)


# Generated at 2022-06-13 16:15:17.177131
# Unit test for function md5s
def test_md5s():
    import tempfile
    fd, tmpfile = tempfile.mkstemp()
    os.close(fd)
    try:
        with open(tmpfile, 'w') as f:
            f.write('foo')
        m = md5(tmpfile)
        assert m == 'acbd18db4cc2f85cedef654fccc4a4d8'
    finally:
        os.unlink(tmpfile)

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:15:21.743395
# Unit test for function checksum
def test_checksum():
    ''' test_checksum is a test function for the function checksum. '''

    digest = checksum('../../lib/ansible/module_utils/basic.py')

    assert digest is not None, 'There is no data in the file'

# Generated at 2022-06-13 16:15:26.199381
# Unit test for function md5
def test_md5():

    test_file = "/tmp/md5_test"

    with open(test_file, "wb") as f:
        f.write(b"1234")

    assert md5(test_file) == '81dc9bdb52d04dc20036dbd8313ed055'

    os.remove(test_file)

# Generated at 2022-06-13 16:15:29.171141
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')


# Generated at 2022-06-13 16:15:37.708611
# Unit test for function checksum
def test_checksum():
    """
    Function to test the checksum function.
    """
    import sys
    import tempfile
    import shutil

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary file
    tmpfile = tempfile.NamedTemporaryFile(dir=tmpdir, delete=False)
    # Write a test string to the temp file
    data = "abcdefghijklmnopqrstuvxyz\n"
    tmpfile.write(data)
    tmpfile.close()

    # sha1 checksum of the data
    expected = 'c11807b8c373e1ed5abaac86c99b9d9b4e4a4fbe'

    # Get the file checksum
    result = checksum(tmpfile.name)
    
    # Remove the temporary

# Generated at 2022-06-13 16:15:41.968607
# Unit test for function md5s
def test_md5s():
    assert md5s('ansible') == 'c2b7a317d2df54b448a11b83f9f9d8c3'
    assert md5s('ansible') == md5_s('ansible')


# Generated at 2022-06-13 16:15:44.348026
# Unit test for function md5s
def test_md5s():
    assert md5s('asdf') == '912ec803b2ce49e4a541068d495ab570'

# Generated at 2022-06-13 16:15:49.277811
# Unit test for function checksum
def test_checksum():
    assert checksum("/bin/ls") == "14b9f4835a6a0b31ff3d22d19a8e94c38ad1eef5"
    assert checksum("/bin/ls", "md5") == "8a30439d1f1c017eaeb94c7e75e15d56"

if __name__ == "__main__":
    test_checksum()

# Generated at 2022-06-13 16:15:54.048871
# Unit test for function md5
def test_md5():
    assert md5('/etc/passwd') == 'cffa2ca0f2bc07fcd8c25926f7e1e5c6'


# Generated at 2022-06-13 16:15:57.980637
# Unit test for function md5s
def test_md5s():
    ''' This function is used to test md5s() function '''

    class md5_class:
        def update(self, text):
            pass
        def hexdigest(self):
            return '8929eda828d12096ff2c6a24a6e73549'
    assert md5s('This is a test string') == '8929eda828d12096ff2c6a24a6e73549'

#
# END BACKWARDS COMPAT
#


# Generated at 2022-06-13 16:16:04.867758
# Unit test for function checksum
def test_checksum():
    import tempfile
    import random

    randfun = random.SystemRandom()
    randfun.seed()

    filename = tempfile.mktemp()
    try:
        fd = open(filename, 'w')
        try:
            for i in range(1000):
                print >>fd, randfun.randint(1, 1000000)
        finally:
            fd.close()

        val1 = checksum(filename)
        val2 = checksum(filename)
        if val1 != val2:
            raise AssertionError('%s != %s' % (val1, val2))
    finally:
        os.remove(filename)

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:16:09.194490
# Unit test for function md5
def test_md5():
    assert md5('file_does_not_exist') is None
    assert md5('test/ansible/hashing/fips.py') == '85b9bc8d8d48bc1dc2cfb08a52957c8e'


# Generated at 2022-06-13 16:16:20.479559
# Unit test for function checksum
def test_checksum():
    assert checksum('./test/ansible/test_utils/test_checksum.py') == 'c6e8b6f70c6f1f6ea24d6f8e6246c9fbdbd3a68a'
    assert checksum('./test/ansible/test_utils/test_checksum.py') == checksum_s("./test/ansible/test_utils/test_checksum.py")
    assert checksum('./test/ansible/test_utils/test_checksum.py') == checksum_s(open('./test/ansible/test_utils/test_checksum.py', 'rb').read())

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:16:23.769910
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(u'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'



# Generated at 2022-06-13 16:16:27.083719
# Unit test for function md5s
def test_md5s():
    # local test function
    from ansible.utils.encrypt import crypt_string
    md5_hash = md5s('foo')
    ansible_hash = crypt_string('foo')
    return (md5_hash == ansible_hash)



# Generated at 2022-06-13 16:16:36.574226
# Unit test for function checksum
def test_checksum():
    """Test checksum function."""
    import io
    import os
    import tempfile
    import stat
    import unittest

    DATA = '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

    # Prepare temporary files

# Generated at 2022-06-13 16:16:41.401897
# Unit test for function checksum
def test_checksum():
    assert checksum_s('string') == '90d31fe16f142ce1528ba838c19b18f5b57e58b0'
    assert checksum('/bin/ls') == 'f60a8c981b1c61ebc566b7a0c921c5f5d5b3a30a'

# Generated at 2022-06-13 16:16:49.799360
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:17:03.878645
# Unit test for function checksum
def test_checksum():
    ''' test the checksum function with different inputs and make sure it returns what we expect '''

    # Test file not existing
    assert checksum('/nothing/here/file') is None
    # Test with directory
    assert checksum('./') is None
    # Test hash for a file
    assert checksum('hashes.py') == '3e6c48b6e8d6fb53f654337e913d094d1eb4b2ea'
    # Test hash for a string
    assert checksum_s('I should be hashed') == '278eb8b6d79c940eae534e11448148d86725c9f9'

    # Old test which uses md5 as the default

# Generated at 2022-06-13 16:17:10.261017
# Unit test for function checksum
def test_checksum():
    if os.path.exists('/usr/bin/python'):
        sum = secure_hash('/usr/bin/python')
        if sum != 'e1c9f963749b32f06b7fa7340428274a':
            raise Exception("checksum failed.  Got %s instead of e1c9f963749b32f06b7fa7340428274a" % sum)
        return True
    raise Exception("checksum failed: /usr/bin/python does not exist on this system")

# Generated at 2022-06-13 16:17:12.852989
# Unit test for function md5
def test_md5():
    md5 = secure_hash(filename='/bin/ls', hash_func=_md5)
    assert md5 == '6a9b6acb5af5eba6ec2a7e1e6c1a8f17'

# Generated at 2022-06-13 16:17:16.902257
# Unit test for function md5s
def test_md5s():
    '''
    >>> md5s("hello world")
    '5eb63bbbe01eeed093cb22bb8f5acdc3'
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:17:23.353771
# Unit test for function checksum
def test_checksum():
    assert checksum(__file__) == 'f306e6d2479be05b34a83b8d2f2aecb2c1ee9078'
    assert checksum_s("hello world") == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'


if __name__ == "__main__":
    test_checksum()

# Generated at 2022-06-13 16:17:29.976003
# Unit test for function md5
def test_md5():
    print('Testing md5()')
    test_file = 'test_file'
    test_data = 'test string'
    test_md5_hash = '7f1d5f5c7d5aef6f643cf6acd5be8a51'

    open(test_file, 'w').write(test_data)
    m = md5(test_file)
    assert m == test_md5_hash, 'MD5 failed'
    print('MD5 passed')


if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:17:36.359098
# Unit test for function checksum
def test_checksum():
    ''' test_checksum.py:  Unit test for function checksum '''

    filename = '/etc/hosts'
    import os

    if os.path.exists(filename):
        print("file %s exists" % filename)
        test_checksum = checksum(filename)
        print("checksum of file %s = %s" % (filename, test_checksum))
        if len(test_checksum) == 40:
            print("checksum function formats a 40 character hash")
        else:
            print("! checksum function does not format a 40 character hash")
    else:
        print("! file %s does not exist" % filename)

# Generated at 2022-06-13 16:17:44.127564
# Unit test for function md5s
def test_md5s():
    ''' check md5s function '''

    import sys
    if sys.version_info.major == 3:
        value = "test"
        expected = "098f6bcd4621d373cade4e832627b4f6"
    else:
        value = unicode("test")
        expected = "098f6bcd4621d373cade4e832627b4f6"

    result = md5s(value)
    if result != expected:
        raise Exception('md5s() failed, returned "%s" instead of "%s"' % (result, expected))

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:17:51.642978
# Unit test for function md5s
def test_md5s():
    ''' Test hash algorithm md5s. Test content same as md5s result of string "foo". '''
    assert secure_hash_s('foo', _md5) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert secure_hash_s(b'foo', _md5) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert secure_hash_s('foo', _md5, 'utf8') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:17:56.224004
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'

# Generated at 2022-06-13 16:18:02.966150
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:18:06.697651
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    try:
        md5s(u'hello')
        assert False, "Unicode strings should not be accepted"
    except UnicodeEncodeError:
        pass

# Generated at 2022-06-13 16:18:09.724763
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:18:13.028479
# Unit test for function md5s
def test_md5s():

    assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'

# Generated at 2022-06-13 16:18:17.357373
# Unit test for function md5
def test_md5():
    "test for secure_hash_s"
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert md5s("world") == "7d793037a0760186574b0282f2f435e7"

# Generated at 2022-06-13 16:18:18.723528
# Unit test for function md5
def test_md5():
    md5("md5.py")


# Generated at 2022-06-13 16:18:22.850404
# Unit test for function md5s
def test_md5s():
    to_test = 'test string'
    expected_hash = '098f6bcd4621d373cade4e832627b4f6'
    obtained_hash = md5s(to_test)
    assert obtained_hash == expected_hash

# Generated at 2022-06-13 16:18:27.427194
# Unit test for function md5s
def test_md5s():
    assert md5s("633ea197fc7c74f71c818450307b6ef1") == "633ea197fc7c74f71c818450307b6ef1"

# Generated at 2022-06-13 16:18:34.124612
# Unit test for function md5
def test_md5():
    ''' md5(filename) unit test'''

    import tempfile

    # Create a tempfile, write some data to it, close.
    (fo, fn) = tempfile.mkstemp()
    os.write(fo, b"data")
    os.close(fo)

    # Check the md5 sum.
    r = md5(fn)
    assert r == "6d5dae2d1efe839e6382a21d98f978bd"

    # Clean up and return.
    os.unlink(fn)


# Generated at 2022-06-13 16:18:39.234779
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'

# Generated at 2022-06-13 16:18:47.840474
# Unit test for function md5
def test_md5():
    ''' unit test for md5 '''

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestMD5(unittest.TestCase):

        @patch('ansible.utils.md5s')
        def test_md5s(self, md5s_mock):
            md5s_mock.return_value = 'some_expected_value'
            self.assertEqual('some_expected_value', md5s('some_data'))
            md5s_mock.assert_called_with('some_data', md5)

        @patch('ansible.utils.md5')
        def test_md5(self, md5_mock):
            md5_mock.return_value = 'some_expected_value'


# Generated at 2022-06-13 16:18:49.520548
# Unit test for function checksum
def test_checksum():
    '''a test to ensure that checksum function does something'''
    assert checksum('/etc/passwd') is not None, 'checksum function failed'

# Generated at 2022-06-13 16:18:55.693539
# Unit test for function md5s
def test_md5s():
    if _md5:
        # Value from MD5 hash calculator http://www.miraclesalad.com/webtools/md5.php
        assert(md5s('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5')



# Generated at 2022-06-13 16:19:04.035328
# Unit test for function md5s
def test_md5s():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestMd5s(unittest.TestCase):
        def test_md5_not_available(self):
            with patch('ansible.module_utils.basic.md5._md5', None):
                self.assertRaises(ValueError, md5s, 'foo')

        @patch('ansible.module_utils.basic.md5._md5', return_value=None)
        @patch('ansible.module_utils.basic.secure_hash_s')
        def test_md5s_called(self, secure_hash_s_mock, unused_md5_mock):
            md5s('foo')

# Generated at 2022-06-13 16:19:14.903808
# Unit test for function md5
def test_md5():
    (rc, out, err) = module.run_command(["md5sum"], data='foobar')
    if rc != 0:
        module.fail_json(msg="unable to calculate md5 of 'foobar'")
    md5sum = out.split()[0]
    if md5sum != md5s('foobar'):
       module.fail_json(msg="md5s('foobar') should be '%s' but it is '%s'" % (md5sum, md5s('foobar')))
    module.exit_json(changed=False)


# Generated at 2022-06-13 16:19:18.606084
# Unit test for function md5s
def test_md5s():
    print("Testing md5s ...")
    if md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3":
        print("Passed")
    else:
        print("Failed")


# Generated at 2022-06-13 16:19:21.980241
# Unit test for function md5s
def test_md5s():
    base_string = "teststring"
    md5_string_test = md5s(base_string)
    assert md5_string_test == "6944e6f3a3a9b1fba25dbf92c28a6d7f"

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:19:25.566740
# Unit test for function md5s
def test_md5s():
  testString = 'This is a test string'
  assert md5s(testString) == '5f5a5a5b72d4a93c7a85633b4c7a59f9'

# Generated at 2022-06-13 16:19:29.930358
# Unit test for function md5s
def test_md5s():
    md5test = 'e9e1d7b5d5b5f5b5eaafafafafa7a7a7'
    if md5s('test') != md5test:
        print('secure_hash_s or md5 test failed')
    else:
        print('secure_hash_s or md5 test passed')


# Generated at 2022-06-13 16:19:37.298014
# Unit test for function checksum
def test_checksum():
    r'''
    ansible core checksum tests

    localhost ansible_connection=local
    '''

    module = AnsibleModule(
        argument_spec = dict(
            src = dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )

    results = (os.path.exists and os.path.exists(module.params['src'])) or False
    if results:
        results = open(module.params['src'], 'r').read()
        results = secure_hash(results)

    module.exit_json(changed=module.params['src'], src=module.params['src'], checksum=results)

