

# Generated at 2022-06-13 16:10:14.424898
# Unit test for function checksum
def test_checksum():
    ''' ansible.utils.checksum.test_checksum() '''

    # Make a temporary TMP file
    import tempfile, atexit
    tmpdir = tempfile.mkdtemp()
    tmpfile, tmpfile_path = tempfile.mkstemp(dir=tmpdir)
    f = os.fdopen(tmpfile, 'w')
    f.write('Some contents for test_checksum')
    f.close()
    atexit.register(lambda: os.remove(tmpfile_path))

    # Test default args
    h1 = checksum_s('Some contents for test_checksum')
    h2 = checksum(tmpfile_path)
    assert(h1 == h2)

    # Test that checksum ignores newlines
    h1 = checksum_s('Some contents for test_checksum\n')

# Generated at 2022-06-13 16:10:24.136004
# Unit test for function checksum
def test_checksum():
    # Add some fake contents for testing
    original_content = "Hello World"
    content_hash_hexdigest = "ed076287532e86365e841e92bfc50d8c"

    # Random files
    with open('file_a.txt', 'w') as f:
        f.write(original_content)
    with open('file_b.txt', 'w') as f:
        f.write(original_content)

    # symlinks
    os.symlink('file_a.txt', 'file_c.txt')
    os.symlink('file_b.txt', 'file_d.txt')

    # directory
    os.mkdir('directory')

    # Check if Fake file exists
    assert os.path.isfile('file_a.txt')

# Generated at 2022-06-13 16:10:27.417920
# Unit test for function md5
def test_md5():
    # Non-existent file returns None
    assert md5('/tmp/') == None
    # Existing file returns md5
    assert md5('/etc/passwd') == 'c439e9a1e5c779df49ebbbe8fce2a266'

# Generated at 2022-06-13 16:10:36.160267
# Unit test for function md5
def test_md5():
    # Create a temporary file
    tmpfile = open('/tmp/testfile', 'w')
    tmpfile.write('Hello there this is a test file\n')
    tmpfile.close()

    # Generate md5 using the function md5
    md5_value = md5('/tmp/testfile')

    # Generate md5 using the command line interface
    import subprocess
    cmd = ['md5sum', '/tmp/testfile']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    md5_value_cmd = out.split()[0]

    # Compare both results
    if not md5_value_cmd == md5_value:
        raise Exception()

    # Remove the temporary

# Generated at 2022-06-13 16:10:45.691008
# Unit test for function md5s
def test_md5s():
    ''' test_md5s()

        Test function md5s() with test strings.
        Return: 
            - True if all tests are successful
            - False if at least one test fails
    '''

    # For test strings:
    # - Calculate the MD5 hash of the test string (use the common md5sum command)
    # - Call md5s() for the same test string
    # - Compare results
    #
    # Note:
    # For these test strings, the MD5 hash from OpenSSL is:
    # - "c3fcd3d76192e4007dfb496cca67e13b"
    # - "a5d57766f02bcf077dc1d10e8fbbf1a9"
    #
    # For these test strings, the MD5 hash from the common md5sum

# Generated at 2022-06-13 16:10:50.631504
# Unit test for function md5
def test_md5():
    ''' unit test for md5 '''
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils._text import to_bytes

    out = StringIO()
    data = to_bytes(u'foobar', errors='surrogate_or_strict')
    fp = cStringIO(data)
    assert md5(fp) == md5s(data)
    fp.close()

# Generated at 2022-06-13 16:10:57.958453
# Unit test for function md5s
def test_md5s():
    import unittest

    class TestMd5s(unittest.TestCase):
        def testmd5s(self):
            self.assertEqual("acbd18db4cc2f85cedef654fccc4a4d8", md5s("foo"))
            self.assertEqual("d3b07384d113edec49eaa6238ad5ff00", md5s("bar"))

    unittest.main()


# Generated at 2022-06-13 16:11:00.970763
# Unit test for function md5s
def test_md5s():
    # simple test for md5s
    val = u"hello world"
    assert md5s(val) == u"5eb63bbbe01eeed093cb22bb8f5acdc3"


# Generated at 2022-06-13 16:11:05.621034
# Unit test for function md5
def test_md5():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    path = loader.path_dwim_relative(None, 'test/support/test.cfg')
    if md5(path) != '44e7deeb1e42dde6fa0b45c790acd72c':
        return False
    return True

# Generated at 2022-06-13 16:11:08.138278
# Unit test for function checksum
def test_checksum():
    # This test uses the example from RFC1321
    assert checksum_s('abc') == 'a9993e364706816aba3e25717850c26c9cd0d89d', checksum_s('abc')

# Generated at 2022-06-13 16:11:13.458348
# Unit test for function md5s
def test_md5s():
    correct = 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2'
    assert md5s('a') == correct, 'md5s must return valid md5 hash'


# Generated at 2022-06-13 16:11:19.236613
# Unit test for function md5
def test_md5():
    # create a test file
    import tempfile
    fd, fname = tempfile.mkstemp(prefix='ansible_test_file_')
    os.close(fd)
    open(fname, 'w').write('test file')

    assert md5(fname) == '24a6d54e6e81d6b0c9b9e6684de8f7d7'
    assert md5s('string') == '32d10c7b8cf96570ca04ce37f2a19d84'

    # remove the test file
    os.remove(fname)

# Generated at 2022-06-13 16:11:21.777808
# Unit test for function md5s
def test_md5s():
    assert md5s("test") == "098f6bcd4621d373cade4e832627b4f6"

# Generated at 2022-06-13 16:11:29.868714
# Unit test for function md5
def test_md5():

    # Create a temp file with only the A character in it.
    import tempfile
    tmpfileh = tempfile.NamedTemporaryFile(delete=False)
    tmpfile = tmpfileh.name
    with open(tmpfile, 'w') as f:
        f.write('A')
    tmpfileh.close()

    # Verify the md5 checksum matches what is expected
    h = md5(tmpfile)
    assert h == '7fc56270e7a70fa81a5935b72eacbe29'

    # Cleanup by removing the file
    import os
    os.remove(tmpfile)

    print('Unit test for function md5: PASS')

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:35.949375
# Unit test for function md5s
def test_md5s():
    testdata = "The quick brown fox jumps over the lazy dog"
    testdata_hash = '9e107d9d372bb6826bd81d3542a419d6'
    h = md5s(testdata)
    if h != testdata_hash:
        raise AssertionError('Hash failure: "%s" != "%s"' % (h, testdata_hash))



# Generated at 2022-06-13 16:11:40.204150
# Unit test for function md5
def test_md5():
    expected = '5d41402abc4b2a76b9719d911017c592'
    result = md5s('hello')
    assert expected == result, "md5s('hello') == %s != %s" % (result, expected)


# Generated at 2022-06-13 16:11:50.304976
# Unit test for function md5
def test_md5():
    import tempfile
    def _test_md5(data, expected):
        (fd, fname) = tempfile.mkstemp()
        os.close(fd)
        with open(fname, "w") as f:
            f.write(data)
        if expected != secure_hash(fname, _md5):
            raise AssertionError('expecting "%s" got "%s"' % (expected, secure_hash(fname, _md5)))
        if expected != secure_hash_s(data, _md5):
            raise AssertionError('expecting "%s" got "%s"' % (expected, secure_hash_s(data, _md5)))
        os.unlink(fname)


# Generated at 2022-06-13 16:11:55.801332
# Unit test for function md5s
def test_md5s():
    import sys

    if sys.version_info >= (2, 5):
        assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
        assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'


# Generated at 2022-06-13 16:11:59.272412
# Unit test for function md5
def test_md5():
    assert md5s("HelloWorld") == "ed076287532e86365e841e92bfc50d8c"
    assert md5s("HelloWorlda") == "e6380098bae4c6aa4fd1fd5f1c5dce34"

# Generated at 2022-06-13 16:12:09.354016
# Unit test for function md5s
def test_md5s():
    # First check if md5s is defined
    if not 'md5s' in globals():
        return False

    # Check for md5s of an empty string
    test_str = ''
    expected_md5s = 'd41d8cd98f00b204e9800998ecf8427e'
    actual_md5s = md5s(test_str)
    if actual_md5s != expected_md5s:
        print('Error: md5s(%s): expected %s, got %s' % (test_str,
                                                        expected_md5s, actual_md5s))
        return False

    # Check for md5s of a string
    test_str = 'test string'

# Generated at 2022-06-13 16:12:24.392986
# Unit test for function md5
def test_md5():
    hasher = _md5()
    hasher.update(b'hello world')
    assert hasher.hexdigest() == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    hasher = _md5()
    hasher.update(u'hello world'.encode('utf-8'))
    assert hasher.hexdigest() == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    hasher = _md5()
    hasher.update(b'hello world')
    hasher.update(u'hello world'.encode('utf-8'))
    assert hasher.hexdigest() == 'f2a2911fa948a2b51eafe0c1b7d90b08'
    hasher = _md5()

# Generated at 2022-06-13 16:12:28.452732
# Unit test for function md5s
def test_md5s():
    # Test with invalid input
    try:
        md5s(1)
    except ValueError:
        pass
    else:
        raise AssertionError('md5s did not reject invalid input')

    # Test against known output
    if md5s('ansible') != 'd033e22ae348aeb5660fc2140aec35850c4da997':
        raise AssertionError('md5s failed to return the correct output for the word "ansible"')


# Generated at 2022-06-13 16:12:31.997517
# Unit test for function md5s
def test_md5s():
    assert md5s("Hello world!") == "ed076287532e86365e841e92bfc50d8c"

# Generated at 2022-06-13 16:12:36.952168
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, fp) = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        f.write('hello')
    assert md5(fp) == '5d41402abc4b2a76b9719d911017c592'
    os.unlink(fp)


# Generated at 2022-06-13 16:12:46.005971
# Unit test for function md5s
def test_md5s():
    ''' Function for unit test for md5s()  '''

    test_string_1 = "Hi there.  What is your name?"
    test_string_2 = "Hi there.  What is your name?  My name is Fred."
    test_result_1 = "deb5b87f5543c9a46b9e86b70d2f8766"
    test_result_2 = "4e810844dff7fc9b1059de0d92f8ae37"

    if md5s(test_string_1) == test_result_1 and md5s(test_string_2) == test_result_2:
        return True
    else:
        return False

# Generated at 2022-06-13 16:12:50.643628
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == '9a0a865967d4c5d6a64ed0d5ee1a5f92'
    assert checksum('/bin/ls') == 'd05b56dffb2a2d118194913d9c970651a47c9cf9'

# Generated at 2022-06-13 16:12:53.270435
# Unit test for function md5s
def test_md5s():
    data = "My message"
    result = "0adf238d3fbb63c58ae2d259c9f7d730"
    assert md5s(data) == result

# Generated at 2022-06-13 16:13:01.286999
# Unit test for function checksum
def test_checksum():
    '''
    ansible.utils.checksum test
    This module tests the ansible.utils.checksum function
    '''

    import tempfile
    import shutil
    import os

    from ansible.utils import checksum

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # create a file in the temporary directory
    fname = os.path.join(tmpdir, "test")
    with open(fname, "w") as f:
        f.write("test")

    # checksum the file
    result = checksum(fname)

    # remove the temporary directory
    shutil.rmtree(tmpdir)

    return result == "098f6bcd4621d373cade4e832627b4f6"

# Generated at 2022-06-13 16:13:04.242358
# Unit test for function md5
def test_md5():
    md5str = md5('/etc/rc.local')
    print(md5str)


# Generated at 2022-06-13 16:13:14.488233
# Unit test for function md5
def test_md5():
    assert checksum_s('hello') == md5s('hello')
    assert checksum_s('hello', _md5) == md5s('hello')
    assert checksum_s('hello', hash_func=_md5) == md5s('hello')
    assert checksum_s('hello', hash_func=sha1) != md5s('hello')

    assert checksum('/bin/ls') == md5('/bin/ls')
    assert checksum('/bin/ls', _md5) == md5('/bin/ls')
    assert checksum('/bin/ls', hash_func=_md5) == md5('/bin/ls')
    assert checksum('/bin/ls', hash_func=sha1) != md5('/bin/ls')


# Generated at 2022-06-13 16:13:19.332122
# Unit test for function md5
def test_md5():
    assert(md5s('hello') == '5d41402abc4b2a76b9719d911017c592')



# Generated at 2022-06-13 16:13:23.746278
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5('/bin/ls') == 'b6f0e90e06a7a4d4d4b0a2b0f8bbe1d1'

# Generated at 2022-06-13 16:13:26.505099
# Unit test for function md5
def test_md5():
    filename = "/etc/ansible/hosts"
    assert md5(filename) == "4d4c9446523f4682d07c5e5b5f71511d"


# Generated at 2022-06-13 16:13:30.626146
# Unit test for function md5s
def test_md5s():
    assert md5s('Hello') == '8b1a9953c4611296a827abf8c47804d7'
    assert md5s('Hello-8b1a9953c4611296a827abf8c47804d7') == 'f5dbb6d73c65954eb56655e3b3d3b3c8'


# Generated at 2022-06-13 16:13:36.182751
# Unit test for function md5
def test_md5():
    ''' Hashes the file "test.txt" which contains the word "hashtest" without newline. Should return the hash "711a1a04a762a0ed2c2aadf7db9903b1". '''
    assert md5("test/integration/filter_plugins/test.txt") == "711a1a04a762a0ed2c2aadf7db9903b1"

# Generated at 2022-06-13 16:13:43.428919
# Unit test for function checksum
def test_checksum():
    from io import StringIO
    data = 'test'
    result = secure_hash(StringIO(data))
    print('Checksum: %s' % result)
    assert result == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:13:47.609485
# Unit test for function md5
def test_md5():
    data = "abcdefghijklmnopqrstuvwxyz0123456789"
    assert md5s(data) == "c1359c2bf076cc8a3344507e6f7d54b1"


if __name__ == '__main__':
    print(md5s('foobar'))

# Generated at 2022-06-13 16:13:50.298838
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:13:56.509900
# Unit test for function md5s
def test_md5s():
    ''' md5s() can run, but only if the platform supports it '''
    if not _md5:
        try:
            md5s('hello world')
        except ValueError as e:
            assert 'not available' in str(e)
        else:
            assert False, 'md5s() should be not available on FIPS platforms'
    else:
        assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:14:08.274863
# Unit test for function md5s
def test_md5s():
    ''' md5s() has specified behavior with FIPS-140 '''
    _md5_bak = _md5

# Generated at 2022-06-13 16:14:12.427037
# Unit test for function md5s
def test_md5s():
    # Function md5s() should not be called
    # This function is for unit test only
    pass

# Generated at 2022-06-13 16:14:20.904377
# Unit test for function checksum
def test_checksum():
    data = "Hello World"
    cksum = checksum_s(data)
    assert cksum == '0a4d55a8d778e5022fab701977c5d840bbc486d0'

    data = "HELLO wORLd"
    cksum = checksum_s(data)
    assert cksum == 'd3486ae9136e7856bc42212385ea797094475802'

    # Make sure it doesn't error out on unicode strings
    cksum = checksum_s(to_bytes(data, errors='surrogate_or_strict'))
    assert cksum == 'd3486ae9136e7856bc42212385ea797094475802'

# Generated at 2022-06-13 16:14:25.046456
# Unit test for function md5
def test_md5():
    data_1 = "The quick brown fox jumps over the lazy dog"
    data_2 = "The quick brown fox jumps over the lazy dog."
    assert md5s(data_1) == md5s(data_2)
    assert md5s(data_1) == "e4d909c290d0fb1ca068ffaddf22cbd0"
    assert md5(__file__) != md5(__file__ + ".tmp")
    assert md5(__file__) == md5(__file__)

# Generated at 2022-06-13 16:14:34.224196
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import os

    test_data = "this is some test data"

    # create a test file
    tmpdir = tempfile.mkdtemp()
    test_file = os.path.join(tmpdir, "test_file")
    with open(test_file, "w") as f:
        f.write(test_data)

    # test md5
    test_md5sum = md5(test_file)
    shutil.rmtree(tmpdir)

    assert(test_md5sum == "394da4912e3c9c9e79d869b5a641a5e5")



# Generated at 2022-06-13 16:14:45.051164
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('français') == 'ed42f8ee81a96488d68cc12fe709e7a1'
    assert md5s('日本語') == 'c58d9e33e05f34bc2bc49786bbcfc6b7'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(u'hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:14:50.890627
# Unit test for function md5
def test_md5():
    import pytest

    test_values = [('foo', 'acbd18db4cc2f85cedef654fccc4a4d8'),
                   ('', 'd41d8cd98f00b204e9800998ecf8427e')]
    for data, expected in test_values:
        assert md5s(data) == expected

# Generated at 2022-06-13 16:15:00.570755
# Unit test for function md5
def test_md5():
    import tempfile
    from ansible.utils.hashs import md5,md5s

    # We create a temporary file for testing
    (os_fd, os_path) = tempfile.mkstemp()

    # We define a string for testing
    string_base = "This is the base string for testing"

    # And create a file with the content of the string
    open(os_path, "wb").write(string_base)

    # Then we try to compute the md5 both on the string and on the file
    assert md5(os_path) == 'be5d5d37542d75f93a87094459f76678'
    assert md5s(string_base) == 'be5d5d37542d75f93a87094459f76678'

    #We remove the temporary file
    os

# Generated at 2022-06-13 16:15:03.327996
# Unit test for function checksum
def test_checksum():
    assert checksum("/dev/null") is not None
    assert checksum("/dev/zero") is not None



# Generated at 2022-06-13 16:15:07.948011
# Unit test for function md5
def test_md5():

    data = 'test'
    digest = md5s(data)
    assert digest == '098f6bcd4621d373cade4e832627b4f6'

    filename = '/etc/hosts'
    digest = md5(filename)
    assert digest == 'c6efbfbd6e1bb835dcee905dc482725e'



# Generated at 2022-06-13 16:15:16.175779
# Unit test for function md5
def test_md5():
    """
    Test md5 function returns the correct results
    :return: None or throws assertion error
    """
    import os
    import tempfile

    if not _md5:
        try:
            import hashlib
            hashlib.md5()
        except ValueError as e:
            # md5 is not supported in FIPS mode, so skip the test if
            # we are running in FIPS mode
            return

    test_text = 'The rain in Spain stays mainly in the plain'
    test_hash = 'a6ff1e093d813f70a50bdea6b14269ce'

    # write string to a file
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write(test_text)
    f.close()

   

# Generated at 2022-06-13 16:15:39.652660
# Unit test for function md5
def test_md5():
    # make sure md5 is working on a different system
    fd = open("/etc/passwd")
    if (md5("/etc/passwd") != 'dff6fd9a9a6047e42d54e3c04f3bfb78'):
        return False
    fd.close()
    return True


# Generated at 2022-06-13 16:15:50.039229
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile, mktemp
    from shutil import rmtree

    dirname = mktemp()
    os.makedirs(dirname)
    f = NamedTemporaryFile(dir=dirname)
    f.write("hello world")
    f.flush()

    # md5 test
    assert md5(f.name) == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5("{0}/{1}".format(dirname, f.name)) == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5("/tmp/doesnotexist") is None
    assert md5("/tmp/") is None

# Generated at 2022-06-13 16:15:51.128598
# Unit test for function md5
def test_md5():
    print (md5s("test"))
    print (md5s("test"))

# Generated at 2022-06-13 16:15:53.638331
# Unit test for function md5s
def test_md5s():
    """ md5s function testing """
    assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'


# Generated at 2022-06-13 16:16:03.808701
# Unit test for function checksum
def test_checksum():
    ''' test_checksum.py:  Tests for utils.checksum '''

    from StringIO import StringIO

    import sys
    import tempfile

    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'

    # create temp file filled with "hello"
    infile = tempfile.NamedTemporaryFile(delete=False, prefix='ansible-test-')
    infile.write('hello')
    infile.close()
    assert checksum(infile.name) == '5d41402abc4b2a76b9719d911017c592'

    # capture output to stdout
    stdout = StringIO()
    sys.stdout = stdout
    # use main() to test command line usage

# Generated at 2022-06-13 16:16:09.274316
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls') == 'fc028c68b2d4022f7b97aebb98d7b91a'
    assert checksum('/bin/cat') == 'f1b70c79cc8b48613681e7d6b0e0a9fa'


# Generated at 2022-06-13 16:16:14.813843
# Unit test for function md5s
def test_md5s():
    test_data = 'test data'
    test_data_len = len(test_data)
    test_data_md5 = '47bce5c74f589f4867dbd57e9ca9f808'
    if (md5s(test_data) != test_data_md5 or
            md5('./lib/ansible/module_utils/hashivault.py') != '3a1d37c2b2e3e3a6b79462cb14cbcc1f'):
        raise AssertionError('Test md5s failed')
test_md5s()

# Generated at 2022-06-13 16:16:24.423765
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.basic import AnsibleModule

    def fail(msg):
        assert False, msg

    def success(msg):
        assert True, msg

    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('') != 'foo'
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo') != 'foo'
    assert md5s('bar') == '37b51d194a7513e45b56f6524f2d51f2'
    assert md5s('bar') != 'foo'

# Generated at 2022-06-13 16:16:26.643104
# Unit test for function md5
def test_md5():
    assert md5(__file__) == 'aacd74df8dc49c948e973a5c5a8d5e3e'


# Generated at 2022-06-13 16:16:31.886733
# Unit test for function md5
def test_md5():
    md5_sum = md5(__file__)
    expected = 'de20ad630bcca5f1a2aae41afdfb6d5e'.encode('utf-8')
    assert(md5_sum == expected)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:48.937426
# Unit test for function md5s
def test_md5s():
    ''' md5s unit test '''

    def run(data, expected):
        rval = md5s(data)
        assert rval == expected, "md5s() test failed. value=%s, expected=%s" % (rval, expected)
    run('12345', '827ccb0eea8a706c4c34a16891f84e7b')
    run('abcdef', 'e80b5017098950fc58aad83c8c14978e')

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:17:01.094694
# Unit test for function checksum
def test_checksum():
    """ test_checksum - Make sure checksum returns what we expect it to """
    # It is possible that we have no _md5.  If so, skip test.
    if _md5:
        test_string = "Hello World"
        sha1_hex_digest = secure_hash_s(test_string)
        md5_hex_digest = md5s(test_string)
        assert sha1_hex_digest == "0a4d55a8d778e5022fab701977c5d840bbc486d0"
        assert md5_hex_digest == "ed076287532e86365e841e92bfc50d8c"
        assert checksum_s(test_string) == sha1_hex_digest

# Generated at 2022-06-13 16:17:06.921126
# Unit test for function checksum
def test_checksum():
    test_file = "/tmp/test_checksum"
    with open(test_file, "w") as f:
        f.write("Hello World!")
    cs_sha1 = checksum(test_file)
    return cs_sha1 == "0a0a9f2a6772942557ab5355d76af442f8f65e01"

# Generated at 2022-06-13 16:17:19.167509
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils import basic

    test_file_name = 'test_checksum'
    test_file_size = 1000000

    # Write a test file
    f = open(test_file_name, 'wb')
    f.write('1234567890')
    f.seek(test_file_size - 1)
    f.write('0')
    f.close()

    # Read checksum
    checksum_value = basic.AnsibleModule(argument_spec={}).run_command(['sha1sum', test_file_name])
    os.remove(test_file_name)

    # Test checksum()
    assert checksum(test_file_name) == None
    assert checksum(test_file_name, sha1) == None

# Generated at 2022-06-13 16:17:24.059922
# Unit test for function md5
def test_md5():
    filename = 'test/units/module_utils/tmp/ansible_test_file'
    checksum = 'ef5027b02f61f662a95b94c8123b1ec0'
    assert md5(filename) == checksum, 'md5 function failed'


# Generated at 2022-06-13 16:17:28.994666
# Unit test for function md5
def test_md5():
    import tempfile
    fd, fname = tempfile.mkstemp()
    os.write(fd, b'hello')
    os.close(fd)
    try:
        md5 = secure_hash(fname)
        assert md5 == '5d41402abc4b2a76b9719d911017c592'
    finally:
        os.remove(fname)


# Generated at 2022-06-13 16:17:32.156292
# Unit test for function md5
def test_md5():
    test_md5 = md5(filename=__file__)
    assert test_md5 == '4d4251aa96f5e5e33b5d5a5be5d86ef2'

# Generated at 2022-06-13 16:17:33.530454
# Unit test for function md5s
def test_md5s():
    pass



# Generated at 2022-06-13 16:17:37.152435
# Unit test for function md5s
def test_md5s():
    assert (md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592')


# Generated at 2022-06-13 16:17:40.829648
# Unit test for function md5
def test_md5():
    assert md5s("This is a test") == "ae2b1fca515949e5d54fb22b8ed95575"

# Unit tests for function md5s

# Generated at 2022-06-13 16:17:58.747719
# Unit test for function md5
def test_md5():
    data = 'The quick brown fox jumps over the lazy dog.'
    md5_data = md5s(data)
    assert md5_data == '9e107d9d372bb6826bd81d3542a419d6'

    filename = '/etc/hosts'
    md5_filename = md5(filename)
    assert md5_filename == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'



# Generated at 2022-06-13 16:18:09.004175
# Unit test for function checksum
def test_checksum():
    fail = True
    try:
        string_test_md5 = md5s("ansible")
        fail = False
    except:
        fail = True
    if fail:
        print("* test_md5: not available on this system")
    else:
        if string_test_md5 != '9cd28f3658b523c91b0d567c7f2a2124':
            print("* test_md5: FAILED")
        else:
            print("* test_md5: OK")


# Generated at 2022-06-13 16:18:12.360418
# Unit test for function md5s
def test_md5s():
    # test string is 'foobar'
    # md5 hash is 3858f62230ac3c915f300c664312c63f
    if md5s('foobar') != '3858f62230ac3c915f300c664312c63f':
        return 'fail'
    else:
        return 'success'

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:18:16.588418
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert(md5s('blah') == 'e4d909c290d0fb1ca068ffaddf22cbd0')


# Generated at 2022-06-13 16:18:19.952344
# Unit test for function md5
def test_md5():
    '''
    Test md5 function.
    '''
    assert md5s('test') is not None
    assert md5('test') is not None

# Generated at 2022-06-13 16:18:30.769325
# Unit test for function md5s
def test_md5s():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestCrypto(unittest.TestCase):

        @patch('ansible.module_utils.basic.AnsibleModule.fail_json')
        def test_md5_not_available(self, fail_json):
            try:
                md5s('some data')
            except ValueError as e:
                self.assertEqual(str(e), 'MD5 not available.  Possibly running in FIPS mode')
            else:
                self.fail('Expected ValueError but no exception raised')

    unittest.main()



# Generated at 2022-06-13 16:18:32.697659
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:18:35.309116
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:18:42.305753
# Unit test for function md5
def test_md5():
    import unittest
    from ansible.module_utils.basic import AnsibleModule

    class TestMD5(unittest.TestCase):
        def test_md5(self):
            module = AnsibleModule(argument_spec=dict(
                data=dict(required=False, type='str'),
                filename=dict(required=False, type='str'),
            ))
            try:
                hash = md5(module.params['filename'])
                assert hash == secure_hash(module.params['filename'])
            except ValueError:
                hash = "MD5 not available.  Possibly running in FIPS mode"

            module.exit_json(changed=False, md5=hash)

    import sys
    sys.modules['ansible'] = None
    unittest.main()



# Generated at 2022-06-13 16:18:44.065705
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == md5('test')

# Generated at 2022-06-13 16:18:58.308027
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:19:02.514024
# Unit test for function md5s
def test_md5s():
    success = True
    if not _md5:
        try:
            md5s("string")
            success = False
        except:
            pass
    else:
        result = md5s("string")
        if result != 'a287479b220ee7bdb34e9b9e1fcf964b':
            success = False
    return success


# Generated at 2022-06-13 16:19:07.191428
# Unit test for function md5s
def test_md5s():
    assert md5s('ansible') == 'fa0540134b0f50af3f54ae8c8ffd2ae2'
    assert md5s('ansible1') == 'a5d6b18f5e5e5a5fdd49b13c83d74ae1'



# Generated at 2022-06-13 16:19:11.520915
# Unit test for function md5s
def test_md5s():
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'{"ansible": "2.91"}') == '9f07b8c8eec51203d7988dcefcfdd05a'


# Generated at 2022-06-13 16:19:15.718216
# Unit test for function md5s
def test_md5s():
    test_data = 'this will be a checksum'
    test_result = 'c50a912e6b54c67b876a081c29376ea3'

    if md5s(test_data) != test_result:
        raise AssertionError("md5s test_data failed")


# Generated at 2022-06-13 16:19:23.306922
# Unit test for function checksum
def test_checksum():
    FAKE_CHECKSUM = '1234567890'
    TEST_FILE_NAME = '/tmp/test_checksum_file.txt'

# Generated at 2022-06-13 16:19:33.361227
# Unit test for function md5s
def test_md5s():
    import sys
    if sys.version_info < (2, 6):
        print("Sorry, md5s requires Python 2.6 or later.")
        sys.exit(1)

    import unittest
    class TestMd5s(unittest.TestCase):
        def setUp(self):
            # simple data
            self.data = u"foobar"
            # unicode
            self.data_unicode = u"fööbär"
            # binary data
            self.data_bin = b"\x00\x01\x02\x03"

        def test_data(self):
            self.assertEqual(md5s(self.data), "3858f62230ac3c915f300c664312c63f")

# Generated at 2022-06-13 16:19:37.261272
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert checksum('lib/ansible/modules/core/system/ping.py') == '6a726f3344b79c7a17a1a64d743e0ea3'

# Generated at 2022-06-13 16:19:43.265619
# Unit test for function md5s
def test_md5s():
    """Test md5s function.

    Validate known md5sums
    """
    # These are all known md5sums
    known_md5sums = [
        ('hello', '5d41402abc4b2a76b9719d911017c592'),
        ('world', '7d793037a0760186574b0282f2f435e7'),
    ]

    for plaintext, md5sum in known_md5sums:
        assert md5s(plaintext) == md5sum


# Generated at 2022-06-13 16:19:49.665587
# Unit test for function md5s
def test_md5s():
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("a") == "0cc175b9c0f1b6a831c399e269772661"
    assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert md5s("message digest") == "f96b697d7cb7938d525a2f31aaf161d0"
    assert md5s("abcdefghijklmnopqrstuvwxyz") == "c3fcd3d76192e4007dfb496cca67e13b"