

# Generated at 2022-06-13 16:10:10.764040
# Unit test for function md5
def test_md5():
    from tempfile import mkstemp
    from shutil import move
    from os import remove, close

    test_fn = "testfile"
    temp_file, temp_filename = mkstemp()
    with open(temp_filename, 'w') as f:
        f.write("#!/bin/bash\necho hello world\n")
    move(temp_filename, test_fn)

    def _md5file(fn):
        f = open(fn, 'r')
        digest = _md5()
        blocksize = 64 * 1024
        block = f.read(blocksize)
        while block:
            digest.update(block)
            block = f.read(blocksize)
        return digest.hexdigest()
    assert _md5file(test_fn) == md5(test_fn)

# Generated at 2022-06-13 16:10:13.610562
# Unit test for function checksum
def test_checksum():
    assert checksum_s('abc') == 'a9993e364706816aba3e25717850c26c9cd0d89d'



# Generated at 2022-06-13 16:10:16.697525
# Unit test for function md5s
def test_md5s():
    expected = '78e731027d8fd50ed642340b7c9a63b3'
    assert md5s('abc') == expected


# Backwards compat unit test

# Generated at 2022-06-13 16:10:20.994269
# Unit test for function checksum
def test_checksum():
    filename = './lib/ansible/module_utils/basic.py'
    assert checksum_s(open(filename, 'r').read()) == checksum(filename)


if __name__ == '__main__':

    test_checksum()

    print(md5_s('hello'))
    print(md5('hashes.py'))

# Generated at 2022-06-13 16:10:29.349761
# Unit test for function md5
def test_md5():
    print("Running md5 unit test ...")
    data="ansible"
    out=md5s(data)
    print( "md5s = %s" % out)
    if out != "af2c1d3619e9b9393b95ff8310e455d4":
        print("md5s unit test failed!")
        return False

    out=md5("/etc/hosts")
    print( "md5 = %s" % out)
    if out != "efa9b1d7f5f5e1a7fb09fabf39fe34be":
        print("md5 unit test failed!")
        return False
    print("md5 unit test passed!")
    return True

# Generated at 2022-06-13 16:10:37.296253
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    x = 'abcdefgh'
    y = md5s(x)
    assert y == 'eef9b3ac8a8dc9a9decf47b361135f8d'
    x = 'ABCDEFGH'
    y = md5s(x)
    assert y == '45b305da8b36afa5f6d23c2b5f6e8aa6'
    x = 'hijklmno'
    y = md5s(x)
    assert y == '4ab8fb25eff9a9ecb2c2577e93e3780c'
    x = 'IJKLMNOP'
    y = md5s(x)

# Generated at 2022-06-13 16:10:40.256847
# Unit test for function md5s
def test_md5s():
    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'



# Generated at 2022-06-13 16:10:45.691667
# Unit test for function checksum
def test_checksum():
    ''' test_ansible_checksum.py '''
    import os

    filename = os.path.join(os.path.dirname(__file__), 'test_ansible_checksum.py')
    result = checksum(filename)
    expected = '98c6770e8d0912d93c3d3e3e1b3a8a15183e946f'
    assert result == expected, "%s != %s" % (result, expected)



# Generated at 2022-06-13 16:10:48.556456
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:10:55.498783
# Unit test for function checksum
def test_checksum():
    teststring = 'Hello World!'
    testsha = '3e25960a79dbc69b674cd4ec67a72c62'
    testsha2 = '0a4d55a8d778e5022fab701977c5d840bbc486d0'
    firstsha = checksum_s(teststring)
    secondsha = checksum_s(teststring)

    assert firstsha == testsha, \
        'Computed sha doesnt match expected: %s != %s' % (firstsha, testsha)
    assert secondsha == testsha, \
        'Computed sha doesnt match expected: %s != %s' % (firstsha, testsha)
    assert firstsha == secondsha, \
        'Repeated sha computed different: %s != %s' % (firstsha, secondsha)

   

# Generated at 2022-06-13 16:11:00.788515
# Unit test for function md5
def test_md5():
    assert md5("/bin/ls") == "23f7efd239b16c71789daae8e1c19f60"

# Generated at 2022-06-13 16:11:03.495495
# Unit test for function checksum
def test_checksum():
    assert checksum('hashutils.py') == checksum('hashutils.py')
    assert checksum('foobaz') != checksum('hashutils.py')


# Generated at 2022-06-13 16:11:07.328538
# Unit test for function md5
def test_md5():
    """
    md5: return the hex digest of a message

    >>> test = md5s("abc")
    >>> test
    '900150983cd24fb0d6963f7d28e17f72'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:11:14.689807
# Unit test for function md5
def test_md5():

    fh = open("testfile.txt", "w")
    fh.write("Hello World")
    fh.close()

    fh = open("testfile.txt", "rb")
    data = fh.read()
    fh.close()

    # In order to test backwards compat, we need to use _md5
    assert secure_hash_s(data, _md5) == md5s(data)
    assert secure_hash(filename="testfile.txt", hash_func=_md5) == md5(filename="testfile.txt")

    os.unlink("testfile.txt")

# Generated at 2022-06-13 16:11:20.672034
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('test\n') == '4c4f4d0a2cd08d3e0462aa83f737359d'

    # Windows is a special snowflake
    if os.name == "nt":
        assert md5('/dev/null') is None
    else:
        assert md5('/dev/null') == 'd41d8cd98f00b204e9800998ecf8427e'



# Generated at 2022-06-13 16:11:23.695442
# Unit test for function md5
def test_md5():

    print('md5: ' + md5('md5'))
    print('md5s: ' + md5s('md5s'))


# Generated at 2022-06-13 16:11:26.948039
# Unit test for function checksum
def test_checksum():
    data="asdf"
    hashed=sha1(data)
    checksummed=checksum_s(data)
    assert(hashed.hexdigest() == checksummed)

# Generated at 2022-06-13 16:11:30.341914
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:11:35.999570
# Unit test for function md5
def test_md5():
    print("testing md5() and md5s()")
    test_string = "hello world"
    print("testing string: [" + test_string + "]")
    print("md5s: " + md5s(test_string))
    print("md5: " + md5("/dev/null"))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:38.872577
# Unit test for function md5s
def test_md5s():
    h = md5s('data')
    assert h == '1f4008ac1afb85a471bbf46b8d7b12af'

# Generated at 2022-06-13 16:11:50.448523
# Unit test for function md5
def test_md5():
    ''' md5.py: md5 checksum test'''

    # Make sure that our unit test is correct.  Generate a checksum of a
    # known string using md5sum, then verify that our md5 function returns
    # that checksum.
    test_string = 'The quick brown fox jumped over the lazy dog'
    md5sum = '9e107d9d372bb6826bd81d3542a419d6'
    my_md5sum = md5s(test_string)
    if my_md5sum != md5sum:
        raise AnsibleError("ERROR: md5 test failed.  Expected %s, got %s" % (md5sum, my_md5sum))

# Generated at 2022-06-13 16:11:53.460265
# Unit test for function md5
def test_md5():
    md5 = md5s("hello")
    assert md5 == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2022-06-13 16:12:03.439346
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestChecksum(unittest.TestCase):

        def setUp(self):
            self.fake_path_exists = os.path.exists
            self.fake_path_isdir = os.path.isdir

        def tearDown(self):
            os.path.exists = self.fake_path_exists
            os.path.isdir = self.fake_path_isdir

        @patch('ansible.module_utils.checksum.secure_hash')
        def test_checksum_with_file(self, mock_secure_hash):
            os.path.exists = lambda x: True
            os.path.isdir = lambda x: False

# Generated at 2022-06-13 16:12:13.353959
# Unit test for function checksum
def test_checksum():
    '''Return this string's sha1 checksum both as a hex string and as a file on disk'''
    import tempfile
    import shutil
    fd, tmp_name = tempfile.mkstemp()
    os.write(fd, "foobar")
    os.close(fd)
    real_hash = '8843d7f92416211de9ebb963ff4ce28125932878'
    # function checksum
    assert checksum(tmp_name) == real_hash
    assert checksum(tmp_name, hash_func=sha1) == real_hash
    assert checksum(tmp_name, hash_func=_md5) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    # function checksum_s
    assert checksum_s

# Generated at 2022-06-13 16:12:17.210433
# Unit test for function md5s
def test_md5s():
    assert md5s("password") == '5f4dcc3b5aa765d61d8327deb882cf99', "wrong md5sum calculated, check code"


# Generated at 2022-06-13 16:12:20.931150
# Unit test for function md5
def test_md5():
    '''tucks.py: test_md5'''

    assert md5("/etc/passwd") == "1f1298bcdc4ce56f4b4e4c5130bd6502"

# Generated at 2022-06-13 16:12:26.488709
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f", "MD5 of 'foobar' failed"
    assert md5s("foo\nbar") == "c7ef86197a693b636fefaa9d9c00187b", "MD5 of 'foobar\\n' failed"
    assert md5s(1) == "c4ca4238a0b923820dcc509a6f75849b", "MD5 of '1' failed"



# Generated at 2022-06-13 16:12:32.853320
# Unit test for function md5s
def test_md5s():
    h1 = md5s('hello')
    h2 = md5s('hello')
    assert h1 == h2

    # this is the md5 hash of the string 'hello'
    assert h1 == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:12:35.158092
# Unit test for function md5s
def test_md5s():
    ''' test md5s() function '''
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    module.exit_json(changed=False, md5s='1')


# Generated at 2022-06-13 16:12:44.266691
# Unit test for function md5s
def test_md5s():
    # compute the md5 sum of an a string
    s = md5s("this is the string to test")
    if s != "1d15e1b2379f3dd2ea8b3a3b9f72e80a":
        return False

    # compute the md5 sum of a unicode string
    s = md5s(u"unicode string \u0E0A\u0E49\u0E32\u0E22")
    if s != "e9a4833f6cc8db8bef31a5ccb7f45ce6":
        return False

    return True


# Generated at 2022-06-13 16:12:50.448916
# Unit test for function md5s
def test_md5s():
    data = "foobar"
    d = md5s(data)
    assert (d == "3858f62230ac3c915f300c664312c63f")


# Generated at 2022-06-13 16:12:55.244249
# Unit test for function md5
def test_md5():
  # data
  data = u'ABCDEFG'
  # expected result
  expected = u'7ac66c0f148de9519b8bd264312c4d64'
  # actual result
  actual = md5s(data)
  # compare result
  assert(actual == expected)


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:57.550652
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls')
    assert checksum_s('hello world!')
    assert md5_s('hello world!')
# end of test_checksum

# Generated at 2022-06-13 16:13:02.359666
# Unit test for function md5
def test_md5():
    f = open('/tmp/ansible_hash_test', 'w')
    f.write("This is a test file for the md5 unit tests\n")
    f.close()
    value = md5("/tmp/ansible_hash_test")
    if value != "a61525b31e7b062cdc34bdaa7c8b8ae9":
        return "test_md5() failed"
    else:
        return "test_md5() passed"


# Generated at 2022-06-13 16:13:13.534872
# Unit test for function md5
def test_md5():
    import os
    import sys
    import shutil
    import tempfile
    import unittest

    # Cleanup the test file
    def cleanup(filename):
        try:
            os.unlink(filename)
        except OSError:
            pass

    class TestMd5(unittest.TestCase):

        # Test md5 function
        def test_md5(self):
            filename = tempfile.mktemp()
            if os.path.exists(filename):
                raise Exception('Failed to create temporary file')

            # Create a file
            open(filename, "w").close()
            self.assertEqual(md5(filename), 'd41d8cd98f00b204e9800998ecf8427e')
            cleanup(filename)

            # Create a file with some data

# Generated at 2022-06-13 16:13:21.214401
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/passwd') == "1f2c2d025e9d9a43e194374322396a47"
    assert checksum('/no/such/file/or/dir') is None
    assert checksum('/etc') is None
    assert checksum(to_bytes('/etc/passwd', errors='surrogate_or_strict')) == "1f2c2d025e9d9a43e194374322396a47"
    assert checksum(to_bytes('/no/such/file/or/dir', errors='surrogate_or_strict')) is None
    assert checksum(to_bytes('/etc', errors='surrogate_or_strict')) is None


# Generated at 2022-06-13 16:13:28.651431
# Unit test for function checksum
def test_checksum():
    # Create temp file for test
    test_file = open('/tmp/test', 'wb')
    test_file.write('Hello world')
    test_file.close()
    assert checksum('/tmp/test', sha1) == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum('/tmp/test') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'


# Generated at 2022-06-13 16:13:34.513069
# Unit test for function md5
def test_md5():
    import tempfile
    f, tfname = tempfile.mkstemp()
    with open(tfname, 'wb') as f:
        f.write(b'foobarbaz')
    assert md5(tfname) == '9d9e9c4a9f9f9dd99a90a3c3c3f3e3e'
    os.remove(tfname)

# Generated at 2022-06-13 16:13:39.078143
# Unit test for function md5s
def test_md5s():
    if not _md5:
        print("MD5 not available.  Possibly running in FIPS mode")
        return
    import nose.plugins.skip
    raise nose.plugins.skip.SkipTest('TODO')

# Generated at 2022-06-13 16:13:40.129964
# Unit test for function md5
def test_md5():
    assert checksum_s('hello world', _md5) == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:13:43.863404
# Unit test for function md5
def test_md5():
    data="foobar"
    return



# Generated at 2022-06-13 16:13:47.206569
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:13:50.344446
# Unit test for function md5
def test_md5():
    assert md5('test/utils/test_md5.py') == 'a47cba7b9f8e520e3257d44e18ccdda7'

# Generated at 2022-06-13 16:13:55.590408
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return

    from random import choice
    from string import ascii_letters

    for x in range(100):
        a_string = ''.join([choice(ascii_letters) for i in range(4096)])
        assert md5s(a_string) == secure_hash_s(a_string, _md5), "Something went wrong with md5s()"

# Generated at 2022-06-13 16:13:58.512112
# Unit test for function md5
def test_md5():

    s = 'abcdef'
    s_md5 = md5s(s)
    assert(s_md5 == '900150983cd24fb0d6963f7d28e17f72')


if __name__ == '__main__':
    # Run tests explicitly
    test_md5()

# Generated at 2022-06-13 16:14:02.758991
# Unit test for function md5
def test_md5():
    assert md5(__file__) == '3a8e9e9b27e76ea4950cf0fb784d7b51'


# Generated at 2022-06-13 16:14:12.239477
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    import ansible.utils.checksum as checksum_utils

    class TestChecksumCase(unittest.TestCase):
        def test_md5_s(self):
            with self.assertRaises(ValueError):
                checksum_utils.md5s('random_string')

        def test_md5(self):
            with self.assertRaises(ValueError):
                checksum_utils.md5('random_string')

        def test_checksum_s(self):
            with patch('ansible.utils.checksum.sha1', autospec=True) as mock_sha:
                checksum_utils.checksum_s('random_string')
                mock_sha.assert_called_once

# Generated at 2022-06-13 16:14:19.906688
# Unit test for function md5s
def test_md5s():

    assert md5s("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert md5s("testing") == "ae2b1fca515949e5d54fb22b8ed95575"
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s(" ") == "7215ee9c7d9dc229d2921a40e899ec5f"
    assert md5s("a" * 1024) == "1a2dc7a97c5587b0be0ab6937df2e732"

# Generated at 2022-06-13 16:14:30.669080
# Unit test for function checksum
def test_checksum():
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR
    from ansible.module_utils.six import PY3

    test_path = os.path.join(os.path.dirname(__file__), 'test_checksum')

    # Test with a file
    with open(os.path.join(test_path, 'test_file'), 'rb') as test_file:
        test_string = test_file.read()

    assert checksum_s(test_string) == 'e42f6ab0e8fd8fd70db24fd7c5b0d088166a9a9b'

    if not PY3:
        assert md5s(test_string) == '03c2d2f955705a9aad1bfde83c0cc13a'

    #

# Generated at 2022-06-13 16:14:36.277595
# Unit test for function md5
def test_md5():
    """ Unit test for function md5 """
    # For file zic
    zic_md5 = md5("/usr/sbin/zic")
    assert zic_md5 == "9d230e9ccba4c4e4e11a8f75834848d4"
    # For file stat
    stat_md5 = md5("/usr/bin/stat")
    assert stat_md5 == "b6ffb821764c9dde13d6fa934f05e0e0"
    print("Unit test completed for function: md5")



# Generated at 2022-06-13 16:14:41.426084
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:14:44.787603
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:14:55.752903
# Unit test for function md5s
def test_md5s():
    # Test the simplest possible case
    assert secure_hash_s(u'') == u'd41d8cd98f00b204e9800998ecf8427e'
    assert secure_hash_s(b'') == u'd41d8cd98f00b204e9800998ecf8427e'

    # Test one character
    for c in [u'a', u'z', u'\u2603', u'\u00e9', u'\u00ae']:
        assert secure_hash_s(c) == secure_hash_s(u'%s' % c)

    # Test adding one character at a time
    s = u''
    for i in range(2048):
        s = s + u'\u2603'
        assert len(s) == i + 1
        assert secure_

# Generated at 2022-06-13 16:14:57.746727
# Unit test for function md5s
def test_md5s():
    assert md5s('testdata') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:14:58.606077
# Unit test for function md5
def test_md5():
    assert md5('/tmp/fake-file') is None

# Generated at 2022-06-13 16:15:00.433644
# Unit test for function md5
def test_md5():
    assert md5('/dev/null') == 'd41d8cd98f00b204e9800998ecf8427e'


# Generated at 2022-06-13 16:15:10.189959
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest

    class TestModuleUtilsCrypto(unittest.TestCase):

        def test_md5(self):
            # First test case has no md5 library
            global _md5
            _md5 = None
            self.assertRaises(ValueError, md5, "/no/such/file")

            # Second test case has md5 library available
            _md5 = sha1
            self.assertEqual(md5("/no/such/file"), None)
            # Note: file /etc/resolv.conf must exist on the test system.
            # Change the file name if different on your test system.

# Generated at 2022-06-13 16:15:14.127878
# Unit test for function md5
def test_md5():
    ''' this test needs to be in the same file as md5() so we can
        compile the FIPS module if needed.
    '''
    import random
    import string
    random_string = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(128))
    md5_digest = md5s(random_string)
    assert md5_digest == '7de8c8f0e354b0f9d15e7b816b8761b7'
    assert md5("fake_md5_file") is None

# Generated at 2022-06-13 16:15:21.602511
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    else:
        try:
            md5s('foo')
            raise Exception('Expected a ValueError')
        except ValueError:
            pass



# Generated at 2022-06-13 16:15:26.963615
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert checksum('/bin/ls') == 'c207bdc2740b842de0d5a5fd5c36b5c1'
    assert checksum('/bin/ls', hash_func=_md5) == '4b4acbe656a8e3e194cac81b260f86d2'

# Generated at 2022-06-13 16:15:35.521830
# Unit test for function md5s
def test_md5s():
    data = "1234567890"
    assert 'e807f1fcf82d132f9bb018ca6738a19f' == md5s(data)
    assert 'e807f1fcf82d132f9bb018ca6738a19f' == md5s(u"%s" % data)
    assert 'e807f1fcf82d132f9bb018ca6738a19f' == md5s(to_bytes(data))



# Generated at 2022-06-13 16:15:40.658396
# Unit test for function md5
def test_md5():
    assert md5s('abc123') == 'e99a18c428cb38d5f260853678922e03'
    assert md5('/etc/passwd') == 'd5f567cbe8693dd9d483829fe0256c8b'
    assert md5('/etc/passwd_not_exists') is None



# Generated at 2022-06-13 16:15:43.586128
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f"


# Generated at 2022-06-13 16:15:50.705845
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    assert md5s(b"hello") == u'5d41402abc4b2a76b9719d911017c592'
    assert md5s(b"hello\n") == u'9dd4e461268c8034f5c8564e155c67a6'
    assert md5s(b'AAAA') == u'93b885adfe0da089cdf634904fd59f71'
    assert md5s(b'AAAA\n') == u'b3b0e9e3cbd632f832a51f6a23c73937'

# Generated at 2022-06-13 16:15:59.801425
# Unit test for function md5
def test_md5():
    assert md5(os.path.join(os.path.dirname(__file__), '../test/support/files/checksumtest_one.txt')) == 'b6d9f9a470e6a51d06c2a03a1d6ca8b6'
    assert md5(os.path.join(os.path.dirname(__file__), '../test/support/files/checksumtest_two.txt')) == '9e8dc93e900aab4e6d3cdb7abb2a96a1'

# Generated at 2022-06-13 16:16:04.456417
# Unit test for function md5
def test_md5():
    '''
    Test if function md5() provides the same value as hashlib.md5() does.
    '''
    try:
        import hashlib
    except:
        import md5 as hashlib

    expected_digest = hashlib.md5(b'sample data').hexdigest()
    result_digest = md5s('sample data')
    assert expected_digest == result_digest, 'md5s() = %s, expected: %s' % (result_digest, expected_digest)

# Generated at 2022-06-13 16:16:12.397059
# Unit test for function md5
def test_md5():
    assert md5s('ABC') == '902fbdd2b1df0c4f70b4a5d23525e932'
    assert md5('/bin/ls') == '2b3a1af3f966d7d9fa9b5dd5f5d57f5d'

if __name__ == "__main__":
    import sys
    import doctest
    import logging
    logging.basicConfig(stream=sys.stdout)
    logging.info('Starting tests for hash_util...')
    (failure_count, test_count) = doctest.testmod(report=True)
    logging.info('Doctest done, %d failures out of %d tests', failure_count, test_count)
    logging.info('Starting tests for md5...')
    test_md5()

# Generated at 2022-06-13 16:16:17.993535
# Unit test for function md5s
def test_md5s():
    s = "abc123"
    assert md5s(s) == "202cb962ac59075b964b07152d234b70"
    # Binary test
    s = "\x00\xff\n"
    assert md5s(s) == "33bdadd93830b9e527fbf5f5b5f09b30"

# Generated at 2022-06-13 16:16:24.015425
# Unit test for function checksum
def test_checksum():
    test_file = './test/support/ansible-checksum-test.txt'

    assert checksum(test_file) == '4a4b0974f9ccb4a4a4efc14f2221a7d8a2ae2e24', 'md5'
    assert checksum(test_file, sha1) == 'f05b8d49f3c20d2e2c56a7a8762b9173d45f1cb3', 'sha1'

# Generated at 2022-06-13 16:16:26.260841
# Unit test for function checksum
def test_checksum():
    file_name = __file__
    assert checksum(file_name).endswith('4423fcb59a9c1ecc06f7fa96d221b84')



# Generated at 2022-06-13 16:16:33.353330
# Unit test for function md5
def test_md5():
    assert md5("/dev/null") in ['d41d8cd98f00b204e9800998ecf8427e', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']

#
# End backwards compat functions
#

# Generated at 2022-06-13 16:16:41.246748
# Unit test for function md5s
def test_md5s():
    assert md5s(b'') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'P@ssw0rd') == '3b52a4b4c95547a8bab2e6ce20959bbd'
    assert md5s(b'P@ssw0rd\x00foo') == 'e0b3e3b67d75fe0fb62bdc1fdfd26f32'

# Generated at 2022-06-13 16:16:43.942638
# Unit test for function md5
def test_md5():
    value = 'this is a test'
    m = _md5()
    m.update(to_bytes(value, errors='surrogate_or_strict'))
    assert md5s(value) == m.hexdigest()
    assert md5(__file__) == secure_hash(__file__, _md5)

# Generated at 2022-06-13 16:16:48.117278
# Unit test for function md5
def test_md5():
    assert md5('/etc/hosts') == '2f8a7d0a82a67c7f1b9f275a050943b0'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:16:54.998071
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert(md5s('test') == '098f6bcd4621d373cade4e832627b4f6')
    assert(md5s('') == 'd41d8cd98f00b204e9800998ecf8427e')


# Generated at 2022-06-13 16:17:06.290182
# Unit test for function md5s
def test_md5s():
    data1 = '0123456789'
    data2 = '01234567890'
    data3 = '0123456789abcdef'
    md1 = md5s(data1)
    md2 = md5s(data2)
    md3 = md5s(data3)
    assert(len(md1) == 32)
    assert(len(md2) == 32)
    assert(len(md3) == 32)
    assert(md1 != md2)
    assert(md2 != md3)
    assert(md3 != md1)
    assert(md1 == '781e5e245d69b566979b86e28d23f2c7')
    assert(md2 == 'c9e93b6abd2b06eb9815385fffe5d5ea')

# Generated at 2022-06-13 16:17:13.077911
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest

    class TestMd5(unittest.TestCase):
        def setUp(self):
            self.md5_digest = 'd41d8cd98f00b204e9800998ecf8427e'
            self.md5_digest_nonascii = '5b75f65c5d5e5381c2f2acb1fc53f8e9'
            self.md5_file = os.path.join(os.path.dirname(__file__), 'test_md5')

        def tearDown(self):
            pass

        def test_md5_s(self):
            self.assertEqual(md5s('foo'), self.md5_digest)


# Generated at 2022-06-13 16:17:20.281127
# Unit test for function md5
def test_md5():
    """
    This test is to unit test the md5 module

    """
    from ansible.module_utils.basic import AnsibleModule

    # Define the test case to be run
    module = AnsibleModule(
        argument_spec = dict(
            value = dict(required=True)
        )
    )

    module.exit_json(changed=False, ansible_facts={'md5': md5(module.params['value'])})

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:17:25.695628
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils import basic
    (rc, out, err) = basic.run_command("python -c 'print(\"Hello, world!\")'")
    h = md5s(out)
    assert h == "f0e4c2f76c58916ec258f246851bea09"


# Generated at 2022-06-13 16:17:32.319596
# Unit test for function md5
def test_md5():
    import os

    temp_file_name = '__tmp_ansible_test_file.txt'
    try:
        with open(temp_file_name, "w") as f:
            f.write("hello world\n")

        assert md5(temp_file_name) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
        assert md5(temp_file_name + 'x') is None
        assert md5('/doesnotexist') is None
        assert md5(temp_file_name) == md5s('hello world\n')
    finally:
        os.unlink(temp_file_name)


# Generated at 2022-06-13 16:17:46.486096
# Unit test for function md5s
def test_md5s():
    ''' test md5s() function '''

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.errors import AnsibleError

    # Are we in FIPS mode?
    try:
        from hashlib import md5 as _md5
    except ImportError:
        try:
            from md5 import md5 as _md5
        except ImportError:
            # Assume we're running in FIPS mode here
            _md5 = None

    # Return None if we are in FIPS mode
    if _md5 is None:
        assert md5s(b'test') is None
        assert md5s(u'test') is None
    else:
        assert md5s(b'test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:17:50.529104
# Unit test for function md5
def test_md5():
    data = "I am a test"
    if not _md5:
        try:
            md5s(data)
        except ValueError as e:
            assert "MD5" in e
    else:
        assert md5s(data) == "4a1d4dbc1e193ec3ab2e9213876ceb8a"


# Generated at 2022-06-13 16:17:56.659359
# Unit test for function md5
def test_md5():
    assert md5('./test/unit/utils/data/ansible_module_md5.py') == '1dbf71aafd76a65c47b8e9c947a0a0a9'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:18:08.507155
# Unit test for function md5
def test_md5():
    import unittest
    import tempfile
    class HashTest(unittest.TestCase):
        def setUp(self):
            pass

        def testEmptyFile(self):
            (fd, name) = tempfile.mkstemp()
            os.close(fd)
            try:
                assert md5(name) == "d41d8cd98f00b204e9800998ecf8427e"
            finally:
                os.unlink(name)

        def testNonEmptyFile(self, filename):
            (fd, name) = tempfile.mkstemp()
            os.write(fd, b"Test")
            os.close(fd)

# Generated at 2022-06-13 16:18:11.370824
# Unit test for function checksum
def test_checksum():
    text = "abcd"
    text_sha1 = "81fe8bfe87576c3ecb22426f8e57847382917acf"

    assert checksum_s(text) == text_sha1
    assert checksum(__file__)

# Generated at 2022-06-13 16:18:19.781623
# Unit test for function checksum
def test_checksum():
    assert checksum(os.path.join(os.path.dirname(__file__), 'test_utils.py')) == 'f6c16d2f34bb0a8e8a2e2f1ae26a1a3fce6403c9'
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert md5(os.path.join(os.path.dirname(__file__), 'test_utils.py')) == '6af54bb3e5a5d543d93bc7b1015d6c22'
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:18:29.966743
# Unit test for function md5s
def test_md5s():
    ''' md5s test '''

    md5s_file = "test_md5s"

    f = open(md5s_file, "w")
    f.write("test")
    f.close()

    f = open(md5s_file, "r")
    md5s_test = md5s(f.read())
    f.close()

    os.remove(md5s_file)

    if md5s_test == '098f6bcd4621d373cade4e832627b4f6':
        return True
    else:
        return 'md5s failed'

# Generated at 2022-06-13 16:18:34.468769
# Unit test for function md5
def test_md5():
    filename = "/tmp/foo"

    # Open file for writing binary data
    fd = open(filename, "wb")

    # Write binary data
    fd.write(b"Hello World")

    # Close file
    fd.close()
    assert md5(filename) == "b10a8db164e0754105b7a99be72e3fe5"

    # Remove file
    os.remove(filename)

# Generated at 2022-06-13 16:18:40.808598
# Unit test for function checksum
def test_checksum():
    ''' checkum.py: Test secure hash and secure hash_s functions '''

    import tempfile

    # secure_hash_s test
    test_string = 'this is a test'
    result = '41a7d8d81c47e3b3ca3c3f68a9e33d35'
    if secure_hash_s(test_string) != result:
        print("Error in secure_hash_s function")

    # secure_hash test
    test_file = tempfile.NamedTemporaryFile()
    test_file.write("Hello world")
    test_file.file.flush()
    result = '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'

# Generated at 2022-06-13 16:18:45.839004
# Unit test for function md5
def test_md5():
    md5_1 =  md5("/etc/passwd")
    md5_2 =  md5("/etc/passwd")

    # Will always be consistent on the same file
    assert md5_1 == md5_2


# Generated at 2022-06-13 16:18:55.097128
# Unit test for function md5
def test_md5():
    f1 = "test/test.py"
    f2 = "test/test.ini"
    f3 = "test/test.pyc"
    f4 = "test/notfound"

    assert(md5s("Hello World!") == "b10a8db164e0754105b7a99be72e3fe5")
    assert(md5(f1) == "0c460f6e973a9f9a469ffd6e2890db06")
    assert(md5(f2) == "eea71a9b59c84bd8d3a3bcd6cfb80a92")
    assert(md5(f3) is None)
    assert(md5(f4) is None)



# Generated at 2022-06-13 16:18:59.081630
# Unit test for function checksum
def test_checksum():

    temp_handle, temp_file = tempfile.mkstemp()

    # Write some data to a temporary file
    with os.fdopen(temp_handle, 'w') as fh:
        fh.write("some data")
        fh.flush()

    temp_handle, temp_file_bad = tempfile.mkstemp()
    os.write(temp_handle, "some data")
    os.close(temp_handle)

    # Make sure they match
    assert checksum(temp_file) == checksum_s("some data")

    # Make sure the two files are similar
    assert checksum(temp_file) == checksum(temp_file_bad)

    # Cleanup
    os.unlink(temp_file)
    os.unlink(temp_file_bad)

# Generated at 2022-06-13 16:19:10.383153
# Unit test for function checksum
def test_checksum():
    import tempfile
    import filecmp

    for hash_func in (sha1, _md5):
        (_, path1) = tempfile.mkstemp()
        (_, path2) = tempfile.mkstemp()
        temp1 = open(path1, "w")
        temp1.write("foo")
        temp1.close()
        temp2 = open(path2, "w")
        temp2.write("foo")
        temp2.close()
        checksum1 = secure_hash(path1, hash_func)
        checksum2 = secure_hash(path2, hash_func)
        assert checksum1 == checksum2
        checksum1 = secure_hash_s('foo', hash_func)
        checksum2 = secure_hash_s('foo', hash_func)

# Generated at 2022-06-13 16:19:19.233046
# Unit test for function md5
def test_md5():
    '''
    This function runs a test for the md5 function
    '''

    import tempfile
    import shutil
    import stat

    tmpdir = tempfile.mkdtemp()

    test_file_path = os.path.join(tmpdir, 'test')
    test_file_contents = b'The quick brown fox jumped over the lazy dog'
    expected_hash = '9e107d9d372bb6826bd81d3542a419d6'

    # Write test file
    with open(test_file_path, 'wb') as tf:
        tf.write(test_file_contents)

    # Confirm that the expected hash matches
    assert md5(test_file_path) == expected_hash

    # Change file permissions.  This should not affect hash

# Generated at 2022-06-13 16:19:21.980836
# Unit test for function md5
def test_md5():
    assert len(md5s('')) == 32
    assert len(md5s('abc')) == 32
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'


# Generated at 2022-06-13 16:19:26.871811
# Unit test for function checksum
def test_checksum():
    '''
    test_checksum: function checksum test
    '''

    # Create a temporary file containing a random string
    from tempfile import NamedTemporaryFile
    from string import digits, ascii_letters
    from random import choice
    filename = NamedTemporaryFile(delete=False)
    randstr = ''.join([choice(digest) for i in range(0, 20)])
    filename.write(randstr)
    filename.close()

    # Assert that the checksum of the string and the file are identical
    assert checksum_s(randstr) == checksum(filename.name)

    # Clean up
    os.remove(filename.name)

# Generated at 2022-06-13 16:19:28.975395
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:19:33.402687
# Unit test for function md5
def test_md5():
    x = md5s('hello')
    assert x == '5d41402abc4b2a76b9719d911017c592'
    x2 = md5s('hello')
    assert x2 == x
    x3 = md5s('hallo')
    assert x3 != x

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:19:37.840663
# Unit test for function md5s
def test_md5s():
    # This is result of running Python3 shell:
    #    >>> import hashlib
    #    >>> hashlib.md5(b"foobar").hexdigest()
    #    '3858f62230ac3c915f300c664312c63f'
    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'

# Generated at 2022-06-13 16:19:40.537994
# Unit test for function md5s
def test_md5s():
    my_md5 = md5s('Hello World!')
    assert my_md5 == 'ed076287532e86365e841e92bfc50d8c'


# Generated at 2022-06-13 16:19:52.446638
# Unit test for function md5
def test_md5():
    filename = 'test_md5.tmp'
    test_string = 'test'
    try:
        with open(filename, 'w') as f:
            f.write(test_string)

        assert md5(filename) == '098f6bcd4621d373cade4e832627b4f6'
        assert md5s(test_string) == '098f6bcd4621d373cade4e832627b4f6'
    except ValueError:
        # MD5 not available on this platform
        pass
    finally:
        os.remove(filename)

# Generated at 2022-06-13 16:19:59.416000
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('This is an md5 test') == '3e3e5c8b5d5d5010a2e7158b1f8832fe'
    assert md5s(b'This is a test') == '67e6be16b4e4c1316f53a7aec6ed4b70'
    assert md5s(' ') == '7215ee9c7d9dc229d2921a40e899ec5f'
    assert md5s(to_bytes(' ')) == '7215ee9c7d9dc229d2921a40e899ec5f'