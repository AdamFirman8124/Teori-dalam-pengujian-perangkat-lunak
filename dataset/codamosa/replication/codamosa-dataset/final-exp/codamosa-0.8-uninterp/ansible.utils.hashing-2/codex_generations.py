

# Generated at 2022-06-13 16:10:17.192768
# Unit test for function checksum
def test_checksum():
    import tempfile
    import shutil
    from ansible.utils.hashing import checksum

    text = "hello world\n"
    fd, testfile = tempfile.mkstemp()

    try:
        os.write(fd, text)
        os.close(fd)

        # check checksum against string
        assert checksum_s(text, sha1) == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed", "sha1 hash string failed"

        # check checksum against file
        assert checksum(testfile, sha1) == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed", "sha1 hash file failed"
    finally:
        os.unlink(testfile)

#

# Generated at 2022-06-13 16:10:21.371702
# Unit test for function checksum
def test_checksum():
    if checksum("test/utils.py") != "f272ccc22dffa59b9eab18c888a2e7d26c5b43f7":
        raise Exception("Checksum test failed")
    else:
        print("Checksum test passed")


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:10:30.377938
# Unit test for function md5s
def test_md5s():
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("a") == "0cc175b9c0f1b6a831c399e269772661"
    assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert md5s("message digest") == "f96b697d7cb7938d525a2f31aaf161d0"
    assert md5s("abcdefghijklmnopqrstuvwxyz") == "c3fcd3d76192e4007dfb496cca67e13b"

# Generated at 2022-06-13 16:10:40.872776
# Unit test for function checksum
def test_checksum():

    test_data = "abc"
    hashval = "a9993e364706816aba3e25717850c26c9cd0d89d"

    assert secure_hash_s(test_data) == hashval
    assert checksum_s(test_data) == hashval

    if _md5:
        assert md5s(test_data) == "900150983cd24fb0d6963f7d28e17f72"
        assert md5s(test_data) == secure_hash_s(test_data, _md5)
    else:
        try:
            md5s(test_data)
        except ValueError:
            pass
        else:
            assert False, "Expected ValueError"

# Generated at 2022-06-13 16:10:45.662222
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == secure_hash_s('hello')
    assert checksum_s('hello', _md5) == md5s('hello')

    assert checksum('test/files/test_file.txt') == secure_hash('test/files/test_file.txt')
    assert checksum('test/files/test_file.txt', _md5) == md5('test/files/test_file.txt')

# Generated at 2022-06-13 16:10:49.781663
# Unit test for function checksum
def test_checksum():
    s="12345"
    assert secure_hash_s(s) == '8cb2237d0679ca88db6464eac60da96345513964'
    assert secure_hash_s(s,'md5') == '827ccb0eea8a706c4c34a16891f84e7b'

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:10:55.533506
# Unit test for function checksum
def test_checksum():
    assert checksum('test/files/chmod.py') == '0fb4d81b6a0a3820c9b9e97f7b7b1dba502e0bfc'
    assert checksum('test/files/chmod.py', None) == '0fb4d81b6a0a3820c9b9e97f7b7b1dba502e0bfc'
    assert checksum('test/files/chmod.py', hash_func=_md5) == 'f9e2a2bf7255e5d6fda8cdd96b6ef10d'
    assert 'f9e2a2bf7255e5d6fda8cdd96b6ef10d' == md5('test/files/chmod.py')

# Generated at 2022-06-13 16:11:00.240710
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile

    # first test a string
    mystr = "hello world"
    myhash = '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert(md5s(mystr) == myhash)

    # next, test a file on disk
    fd = NamedTemporaryFile()
    fd.write(mystr)
    fd.flush()
    assert(md5(fd.name) == myhash)
    fd.close()

# Generated at 2022-06-13 16:11:05.280940
# Unit test for function md5
def test_md5():
    
    from tempfile import NamedTemporaryFile

    data = 'The quick brown fox jumped over the lazy dog'

    md5_digest = md5s(data)

    with NamedTemporaryFile() as f:
        f.write(data)
        f.flush()
        
        # Test the file based md5
        assert md5(f.name) == md5_digest
    
        # Test when the file does not exist
        assert md5('/tmp/does-not-exist.txt') == None

# Generated at 2022-06-13 16:11:13.012180
# Unit test for function checksum
def test_checksum():
    path = os.path.join(os.path.dirname(__file__), 'test_utils.py')
    assert checksum(path) == '2f1b9e9d83f90bab6bf3b3e8e0a44d82f7100a6f'
    assert checksum(path, hash_func=_md5) == '2985a6c194f84aa715f4f4c9ca4d2f2d'
    assert checksum_s('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    assert checksum_s('test', hash_func=_md5) == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s

# Generated at 2022-06-13 16:11:24.107633
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) == 1:
        h = secure_hash(args[0])
        if not h:
            print("file not found")
        else:
            print(h)
    else:
        s = ' '.join(args)
        print(secure_hash_s(s))

# Generated at 2022-06-13 16:11:30.138724
# Unit test for function md5s
def test_md5s():
    test_string = 'Hello World!'
    result = '0a4d55a8d778e5022fab701977c5d840bbc486d0'
    assert md5s(test_string) == result

if __name__ == "__main__":
    test_md5s()

# Generated at 2022-06-13 16:11:32.814703
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'



# Generated at 2022-06-13 16:11:35.548022
# Unit test for function md5s
def test_md5s():
    assert md5s('test1') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:11:42.642942
# Unit test for function checksum
def test_checksum():
    test_data = 'Hello World'
    test_sha = 'f58d3b15c97ceb3769db719c798ddbef8ead4b4a'
    test_md5 = 'd41d8cd98f00b204e9800998ecf8427e'
    assert(checksum_s(test_data) == test_sha)
    assert(md5s(test_data) == test_md5)

# Generated at 2022-06-13 16:11:44.780439
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:11:53.259962
# Unit test for function checksum
def test_checksum():
    ''' test_checksum.py:  Tests the functions in checksum. '''

    import os
    import sys
    import subprocess

    # Create our test files
    p = subprocess.Popen('echo "abcdefghijklmnopqrstuvwxyz" > test_checksum.txt', shell=True, universal_newlines=True)
    p.communicate()
    p = subprocess.Popen('echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" > test_checksum_two.txt', shell=True, universal_newlines=True)
    p.communicate()

    # Test to make sure output matches sha1sum command
    text_file = open('test_checksum.txt', 'rb')
    digest = sha1()

# Generated at 2022-06-13 16:11:57.545789
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('abcdef') == 'e9a74d82fb44c3233cef72a2dfb196d7'
    else:
        try:
            md5s('abcdef')
            assert False
        except ValueError:
            assert True


# Generated at 2022-06-13 16:12:00.345610
# Unit test for function md5
def test_md5():
    data = 'hello'
    result = '5d41402abc4b2a76b9719d911017c592'
    assert(md5s(data) == result), 'md5s() test failed'


# Generated at 2022-06-13 16:12:03.657704
# Unit test for function md5
def test_md5():
    assert md5('lib/ansible/module_utils/facts/system/__init__.py') == '07f7b92e9d9c7b52cfc0a253b91f15ac'


# Generated at 2022-06-13 16:12:13.645114
# Unit test for function checksum
def test_checksum():
    import tempfile
    tmpdir = tempfile.mkdtemp(dir='/tmp', prefix='ansible-tmp')
    f1 = os.path.join(tmpdir, 'f1')

    with open(f1, 'wb') as f:
        f.write('hello world! I am exactly 14 bytes!')

    assert checksum(f1) == '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684'
    os.remove(f1)
    os.rmdir(tmpdir)



# Generated at 2022-06-13 16:12:18.435822
# Unit test for function checksum
def test_checksum():
    '''Check if checksum function works with valid input
    The function should return a hex digest of the data.'''
    assert checksum_s('test_checksum') == secure_hash_s('test_checksum')



# Generated at 2022-06-13 16:12:24.663936
# Unit test for function md5
def test_md5():
    ''' test md5 function '''

    import ansible
    testfile = ansible.__file__.rstrip('c')

    # test md5 of a file
    if md5(testfile) != 'f2b6e4436037ce19e3bd863a27b2e2a7':
        return False

    # test md5 of a string
    if md5s('hello') != '5d41402abc4b2a76b9719d911017c592':
        return False

    return True

# Generated at 2022-06-13 16:12:37.182553
# Unit test for function md5
def test_md5():
    import shutil
    import tempfile
    import time

    mytmpdir=tempfile.mkdtemp()
    # Create a temporary file and wait 1 second so it has a different timestamp
    if os.path.exists(mytmpdir):
        fd, testfile = tempfile.mkstemp(dir=mytmpdir)
        os.write(fd, b'test')
        os.close(fd)
        time.sleep(1)

        fd, testfile2 = tempfile.mkstemp(dir=mytmpdir)
        os.write(fd, b'test')
        os.close(fd)

        m1 = md5(testfile)
        m2 = md5(testfile2)
        assert(m1 != m2)

        m1s = md5s("test")

# Generated at 2022-06-13 16:12:46.721846
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import filecmp

    try:
        # Lets generate a temp directory to work on
        tmpdir = tempfile.mkdtemp()

        # Create an empty regular file
        src = os.path.join(tmpdir, "src")
        open(src, 'a').close()
        # Create a directory
        dst = os.path.join(tmpdir, "dst")
        os.mkdir(dst)

        result = md5(src)
        assert result

        result = md5(dst)
        assert result is None

        result = md5("/non-existent/file")
        assert result is None

    finally:
        # Clean up
        shutil.rmtree(tmpdir)


# Generated at 2022-06-13 16:12:54.094538
# Unit test for function checksum
def test_checksum():
    test_path = os.path.join(os.path.dirname(__file__), "test_checksum")
    print("Testing checksum() with file: %s" % test_path)
    hash_correct = "8e9afa73af6c13e1db3816e5e0a109f2d295880a"
    hash = secure_hash(test_path)
    assert hash_correct == hash
    print("Passed checksum() test")

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:59.615817
# Unit test for function checksum
def test_checksum():
    p = os.path.join(os.path.dirname(__file__), 'test_checksum')
    if not os.path.exists(p):
        os.mkdir(p)
    paths = [
        os.path.join(p, 'foo'),
        os.path.join(p, 'bar', 'foo'),
        os.path.join(p, 'bar', 'baz'),
        os.path.join(p, 'bar', 'baz', 'foo'),
    ]
    for path in paths:
        with open(path, 'w') as f:
            f.write('foo')
    # check directory
    ans = checksum(p)
    assert ans is None
    # check file
    ans = checksum(paths[0])

# Generated at 2022-06-13 16:13:04.392531
# Unit test for function md5
def test_md5():
    test_str = 'abcdefghijklmnopqrstuvwxyz'
    test_result = 'c3fcd3d76192e4007dfb496cca67e13b'

    result = md5s(test_str)
    assert result == test_result, "%s != %s" % (result, test_result)


if __name__ == '__main__':
    test_md5()

# vim: set ft=python ts=4 sw=4 expandtab :

# Generated at 2022-06-13 16:13:14.522565
# Unit test for function checksum
def test_checksum():
    from tempfile import mkstemp

    # Create temporary file
    fn = mkstemp()[1]
    text = "Hello World!"
    with open(fn, 'w') as f:
        f.write(text)

    # Checksum a file/directory
    assert checksum(fn) == 'ed076287532e86365e841e92bfc50d8c'
    assert checksum(__file__) == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'

    # Checksum a string
    assert checksum_s(text) == 'ed076287532e86365e841e92bfc50d8c'

# Generated at 2022-06-13 16:13:24.012947
# Unit test for function md5
def test_md5():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Create a temporary file
    tmp_file = open('/tmp/test_md5', 'w')
    tmp_file.write('123456789')
    tmp_file.close()

    # Get the md5 of the temporary file
    tmp_file_md5 = md5('/tmp/test_md5')

    # Delete the temporary file
    os.remove('/tmp/test_md5')

    assert tmp_file_md5 == AnsibleUnsafeText('e807f1fcf82d132f9bb018ca6738a19f')


# Generated at 2022-06-13 16:13:37.375313
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'
    assert md5s('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') == 'd174ab98d277d9f5a5611c2c9f419d9f'

# Generated at 2022-06-13 16:13:45.544657
# Unit test for function md5
def test_md5():
    '''
        This function is for debugging purpose only, which can be run like this:
        python -c "import os, sys, hashlib; sys.path.append(os.getcwd()); \
            from ansible.utils.hashing import *; \
            print(md5s('random string here'))"
    '''
    print(md5s('random string here'))
    print(md5('/etc/passwd'))

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:13:49.870885
# Unit test for function md5s
def test_md5s():
    ''' unit test for md5s which is for backwards compat '''

    h = md5s("foobar")
    assert h == "8843d7f92416211de9ebb963ff4ce28125932878"

# Generated at 2022-06-13 16:13:59.833708
# Unit test for function md5s
def test_md5s():
    import ansible.utils.hashing

    assert ansible.utils.hashing.md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert ansible.utils.hashing.md5s('Hello') == '8b1a9953c4611296a827abf8c47804d7'
    assert ansible.utils.hashing.md5s('The quick brown fox jumped over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
    assert ansible.utils.hashing.md5s('Axe') == '93dfb8303948cdfd8473d7e58c1f1603'



# Generated at 2022-06-13 16:14:04.598977
# Unit test for function md5
def test_md5():
    # There is no portable way to create an MD5 hash in a known state,
    # so we cannot test the method.  Just make sure it runs.
    assert md5s('test')
    assert md5('sha1.py')

# Generated at 2022-06-13 16:14:08.634339
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/passwd') == '91788efc7b0d66b56df7351263f6c56f'
    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:14:17.645336
# Unit test for function checksum
def test_checksum():
    test_string = 'Hello World!'
    assert checksum_s(test_string) == '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    assert md5s(test_string) == '65a8e27d8879283831b664bd8b7f0ad4'
    assert checksum('/bin/ls') == 'f5c9c63d0d5f1f0bc453bc29ca5af78d0d35b0ce'
    assert md5('/bin/ls') == 'f5c9c63d0d5f1f0bc453bc29ca5af78d'

    # Test a directory.  The result will be None
    assert checksum('/bin') == None
    assert md5('/bin')

# Generated at 2022-06-13 16:14:24.252565
# Unit test for function md5s
def test_md5s():
    ''' Test md5s() with some known values. '''
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:14:28.217495
# Unit test for function md5s
def test_md5s():
    data = 'some data'
    assert(md5s(data) == '4f4d2c3082fef5a5d82db23e5a3a5a5c')



# Generated at 2022-06-13 16:14:34.478356
# Unit test for function checksum
def test_checksum():

    # Create a test file
    (fd, path) = tempfile.mkstemp()
    os.close(fd)

    try:
        # Write some data
        f = open(path, 'w')
        f.write('1234')
        f.close()

        # Verify checksum of test file
        if checksum(path) != '81dc9bdb52d04dc20036dbd8313ed055':
            assert False, 'Failed checksum test'
    finally:
        os.unlink(path)

# Generated at 2022-06-13 16:14:46.040549
# Unit test for function md5
def test_md5():
    ''' simple test for md5 '''

    import sys

    if sys.version_info < (2, 5):
        print("Skipping test_md5, python 2.4 or older doesn't have hashlib")
        return True

    filename = os.path.join(os.path.dirname(__file__), 'hashlib_data/file1')

    # Test hashlib with different hash algorithm
    # MD5 is the default checksum algorithm in the old version
    assert md5(filename) == u'68b329da9893e34099c7d8ad5cb9c940'
    assert md5s(u"hello\n") == u'5d41402abc4b2a76b9719d911017c592'

test_md5()

# Generated at 2022-06-13 16:14:56.344304
# Unit test for function md5
def test_md5():
    # Create a sample file
    from tempfile import mkstemp
    sample_file = os.path.abspath(mkstemp()[1])
    # Write some data to the file
    sample_data = "Mary had a little lamb, its fleece was white as snow"
    open(sample_file, 'w').write(sample_data)
    # Calculate the md5 of the data
    sample_md5 = md5(sample_file)
    # Calculate the md5 of the data
    data_md5 = md5s(sample_data)
    # Check that the two md5s are the same
    assert sample_md5 == data_md5
    # Clean up
    os.unlink(sample_file)
    print("Successfully calculated the md5 of a file")

# Generated at 2022-06-13 16:14:59.603845
# Unit test for function md5s
def test_md5s():
    assert(md5s("asdf") == '912ec803b2ce49e4a541068d495ab570')
    assert(md5s("asdfg") == 'd6e4b4af8b4b17d664e0b1283aab31ac')
    assert(md5s("asdflkasdfasdf") == 'd3e6e7f6b3f3b8e5085e543b7d929fcf')

# Generated at 2022-06-13 16:15:03.894394
# Unit test for function md5s
def test_md5s():
    data = "testdinara"
    m = md5s(data)
    assert m == 'b9394ed9dff796d72a86565593f78601'


# Generated at 2022-06-13 16:15:08.046706
# Unit test for function md5s
def test_md5s():
    error_msg = 'md5s() test failed'
    assert md5s('string') == '1bc29b36f623ba82aaf6724fd3b16718', error_msg
    assert md5s(1) == 'c4ca4238a0b923820dcc509a6f75849b', error_msg


# Generated at 2022-06-13 16:15:10.634388
# Unit test for function md5s
def test_md5s():
    if _md5:
        test_val = 'foobar'
        assert md5s(test_val) == '3858f62230ac3c915f300c664312c63f'



# Generated at 2022-06-13 16:15:18.448364
# Unit test for function md5s
def test_md5s():
    """
    Test that md5s matches the output of the md5sum CLI program

    I have verified that the same data and salt produce the same
    results, but one iteration is too few.
    """

    data = 'Jefe'
    salt = 'what do ya want for nothing?'

    # Calculate the hash
    hashed = md5s(data + salt)

    # Run the native md5 program to verify
    from subprocess import Popen, PIPE

    # The hash algorithm is specified on the command line
    cmd = ['md5sum', '-b']
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(input="%s%s" % (data, salt))

# Generated at 2022-06-13 16:15:27.221263
# Unit test for function checksum
def test_checksum():
    ''' test_checksum()  - check that checksum works for data and for files,
    calling the same underlying functions.
    '''

    checksum_data = checksum_s('hello world!')
    checksum_file = checksum('/bin/ls')
    if checksum_data == None or checksum_file == None:
        print ("Failure in checksum_s or checksum function")
        return (1)

    return (0)

# Run unit tests if executed directly
if __name__ == '__main__':
    if test_checksum() != 0:
        exit(1)
    exit(0)

# Generated at 2022-06-13 16:15:34.181791
# Unit test for function checksum
def test_checksum():
    # Create a file
    with open('/tmp/ansible_test_file', 'w') as f:
        f.write('foobar')
        f.close()
    # Get the checksum
    checksum_value = checksum('/tmp/ansible_test_file')
    # Check the checksum value
    assert checksum_value == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'

# Generated at 2022-06-13 16:15:38.147398
# Unit test for function checksum
def test_checksum():
    def _assert(actual, expected):
        if actual != expected:
            raise AssertionError("%s should be %s" % (repr(actual), repr(expected)))

    _assert(checksum("data", hash_func=hashlib.md5), hashlib.md5("data").hexdigest())
    _assert(checksum("data", hash_func=hashlib.sha1), hashlib.sha1("data").hexdigest())



# Generated at 2022-06-13 16:15:45.563915
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == 'e5cd0838aee1b72c8d9b155c326bab1d'
    assert md5s('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'



# Generated at 2022-06-13 16:15:52.791345
# Unit test for function md5s
def test_md5s():
    assert md5s("") == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s("a") == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s("abc") == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s("message digest") == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s("abcdefghijklmnopqrstuvwxyz") == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:15:59.842726
# Unit test for function checksum
def test_checksum():
    ''' test checksum function '''

    if not os.path.exists('/bin/cat'):
        print("SKIPPED: /bin/cat not found")
        return

    testfile = "/tmp/ansible_test_checksum"

    f = open(testfile, "w")
    try:
        f.write("hello world")
        f.close()

        # test normal
        assert checksum(testfile) == checksum_s("hello world")

        # test cached
        assert checksum(testfile, False) == checksum_s("hello world")
    finally:
        os.remove(testfile)

# Generated at 2022-06-13 16:16:02.477030
# Unit test for function md5s
def test_md5s():
    teststr = 'abc123 \n'
    teststrsum = 'e99a18c428cb38d5f260853678922e03'
    assert md5s(teststr) == teststrsum

# Generated at 2022-06-13 16:16:09.970769
# Unit test for function md5
def test_md5():
    '''test md5'''

    assert md5("/dev/null") == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5("/dev/zero") == '8b8f7901df47c04d361d48bb929cce9c'
    assert md5("/dev/random") == '2e4d22f6c2cfa0cad1c9fadba48d6bd0'

# Generated at 2022-06-13 16:16:14.360329
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    data = {'foo': 'bar'}
    assert md5s(data) == '37b51d194a7513e45b56f6524f2d51f2'

# Generated at 2022-06-13 16:16:24.146771
# Unit test for function checksum
def test_checksum():
    import random
    import string
    import filecmp
    import tempfile
    import shutil

    MAX_SIZE = 100000
    NUM_CYCLES = 50
    NUM_PROCESSES = 4

    def run_checksum(content):
        fd, path = tempfile.mkstemp()
        f = os.fdopen(fd,'w')
        f.write(content)
        f.close()
        csum = checksum(path)
        os.remove(path)
        return csum

    def test_content(content):
        csum = run_checksum(content)
        assert csum == checksum_s(content)

    def test_random_content(size):
        content = ''.join(random.choice(string.ascii_lowercase) for x in range(size))
       

# Generated at 2022-06-13 16:16:26.682441
# Unit test for function md5
def test_md5():
    md5s_return = md5s('test')
    assert md5s_return == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:16:29.529349
# Unit test for function md5s
def test_md5s():
    assert md5s('dummy') == '1f3870be274f6c49b3e31a0c6728957f'


# Generated at 2022-06-13 16:16:37.576509
# Unit test for function checksum
def test_checksum():
    ''' Test checksum() module '''
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    task = Task()

    task.args = {
        'src': "foobar",
        'checksum_algorithm': 'sha1'
    }

    task.args = {
        'src': "foobar",
        'checksum_algorithm': 'md5'
    }

# Generated at 2022-06-13 16:17:06.920514
# Unit test for function checksum
def test_checksum():
    assert checksum('tests/test/support/md5sum.py') == 'cbbaf64d594d7cdf524b54f47329bbca'

# Generated at 2022-06-13 16:17:09.681660
# Unit test for function md5
def test_md5():
    assert md5("abc") == "900150983cd24fb0d6963f7d28e17f72"


# Generated at 2022-06-13 16:17:14.983146
# Unit test for function md5s
def test_md5s():
    print("md5s('dummy text') = %s expected: 3e2bd0d12c46a8a4e4e3f3e4f9c9d2fd" % md5s('dummy text'))
    print("md5s('dummy text') = %s expected: 3e2bd0d12c46a8a4e4e3f3e4f9c9d2fd" % md5s('dummy text'))
    assert md5s('dummy text') == '3e2bd0d12c46a8a4e4e3f3e4f9c9d2fd'
    assert md5('/tmp/xyz') is None

# Generated at 2022-06-13 16:17:21.651277
# Unit test for function md5
def test_md5():
    import os
    import tempfile

    testfile = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    data = os.urandom(64)
    testfile.write(data)
    testfile.close()

    data_md5 = md5s(data)
    testfile_md5 = md5(testfile.name)

    assert data_md5 == testfile_md5

    os.unlink(testfile.name)



# Generated at 2022-06-13 16:17:31.234151
# Unit test for function md5
def test_md5():
    data = 'abcdefghijklmnop'
    value = '74e6f7298a9c2d168935f58c001bad88'
    assert(md5s(data) == value)
    assert(md5s(unicode(data)) == value)

    # only the unicode test should raise an exception
    try:
        md5s(data.encode('ascii'))
    except UnicodeError:
        raise AssertionError('UnicodeError')
    except ValueError as e:
        if 'not available' not in str(e):
            raise AssertionError('unknown ValueError')
    else:
        raise AssertionError('no exception raised')

    try:
        md5s(data.encode('utf-8'))
    except UnicodeError:
        raise Assertion

# Generated at 2022-06-13 16:17:34.204242
# Unit test for function md5
def test_md5():
    h = md5("unit/module_utils/basic.py")
    assert h == "0d35c7a9f9b9fce2c3e25f7cadaff8da"



# Generated at 2022-06-13 16:17:44.462767
# Unit test for function md5s
def test_md5s():
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('ab') == '187ef4436122d1cc2f40dc2b92f0eba0'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'
    assert md5s('abcde') == 'ab56b4d92b40713acc5af89985d4b786'

# Generated at 2022-06-13 16:17:50.699547
# Unit test for function md5
def test_md5():
    test_file = 'sample_file.txt'
    file_content = "This is a simple test for md5()"
    f = open(test_file, 'wb')
    try:
        f.write(file_content)
    except IOError as e:
        raise AnsibleError("error while writing a file %s, error was: %s" % (test_file, e))
    f.close()
    assert md5(test_file) == '5918ca8f70265c2772ece0d7ff87b902', "md5 function failed"
    os.remove(test_file)



# Generated at 2022-06-13 16:18:00.604858
# Unit test for function checksum
def test_checksum():
    try:
        import ansible
    except ImportError:
        raise ImportError("ansible is required for this module")

    if not hasattr(ansible, '__version__'):
        raise AssertionError("ansible not loaded")
    else:
        ver = ansible.__version__

    # Check if we are using ansible version older than 2.1
    if ver.split('.')[0] == "2" and ver.split('.')[1] <= "1":
        if checksum("/bin/ls") != "27b790a0b94be4782b7e68dc844a3d26fb0c0bef":
            raise AssertionError("checksum does not return correct checksum for /bin/ls")

# Generated at 2022-06-13 16:18:09.858067
# Unit test for function md5
def test_md5():
    import tempfile
    g = tempfile.NamedTemporaryFile()
    g.write(b"blah")
    g.flush()

    # first test that the function returns something
    assert md5(g.name)

    # next test that it returns the same value that the md5sum unix command returns
    assert md5(g.name) == "07f7d30b093f3deb3a5c5f5b31c2e5a5"

    # next test that it raises an error when md5 is not available (FIPS-140-2 mode)
    try:
        old = _md5
        _md5 = None
        assert 1 == 0, 'Expected ValueError'
    except ValueError:
        pass
    finally:
        _md5 = old

# Generated at 2022-06-13 16:18:17.626149
# Unit test for function checksum
def test_checksum():
    import tempfile

    file_name=tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write('foo')
    assert checksum(file_name) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    os.unlink(file_name)

# Generated at 2022-06-13 16:18:22.115907
# Unit test for function md5
def test_md5():
    """Unit test for the md5 function."""
    h = md5('CHANGELOG')
    assert h == '2aa191ce40678cdb50c38b8e9ae93978', h


# Generated at 2022-06-13 16:18:30.370727
# Unit test for function md5s
def test_md5s():
    test_data = """
    this is a test of md5s function
    """
    test_data_result = '1d018f65a7e321bce491777c9e8ab78d'
    assert test_data_result == md5s(test_data)


if __name__ == '__main__':
    import sys
    for i in sys.argv[1:]:
        print("%s: %s" % (i, checksum(i)))

# Generated at 2022-06-13 16:18:37.803519
# Unit test for function md5
def test_md5():
    test_md5_file = "test_md5"
    text1 = to_bytes("The quick brown fox jumps over the lazy dog")
    text2 = to_bytes("Blah blah blah, not the same")
    text3 = to_bytes("The quick brown fox jumps over the lazy dog")
    hash1 = md5s(text1)
    assert hash1 == '9e107d9d372bb6826bd81d3542a419d6'

    # Test for file
    open(test_md5_file, 'wb').write(text2)
    hash2 = md5(test_md5_file)
    assert hash2 == '1abb1188d979e9e95540f459c0c10e7f'

    # Test for file with hash1

# Generated at 2022-06-13 16:18:41.765810
# Unit test for function md5
def test_md5():
    import tempfile

    data = 'some string'
    hash = md5s(data)
    assert hash == '9f9ad072a2a7d0b0e6634a6f206d6b91'

    (handle, filename) = tempfile.mkstemp()
    handle = os.fdopen(handle, 'w')
    handle.write(data)
    handle.close()

    assert md5(filename) == hash
    os.remove(filename)

# Generated at 2022-06-13 16:18:52.374232
# Unit test for function checksum
def test_checksum():
    c1 = checksum_s(b'hello')
    if c1 != '5d41402abc4b2a76b9719d911017c592':
        print(c1)
        raise Exception("FAILURE: checksum_s('hello') is %s, expected 5d41402abc4b2a76b9719d911017c592" % c1)
    c2 = checksum_s('hello')
    if c2 != '5d41402abc4b2a76b9719d911017c592':
        print(c2)
        raise Exception("FAILURE: checksum_s('hello') is %s, expected 5d41402abc4b2a76b9719d911017c592" % c2)
    c3 = checksum('/etc/passwd')

# Generated at 2022-06-13 16:18:58.728602
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == '5d41402abc4b2a76b9719d911017c592'
    assert md5('/usr/bin/python') == 'bbd886d2468e34ba28a8c7d9f917d9f4'


# Generated at 2022-06-13 16:19:09.833660
# Unit test for function md5s
def test_md5s():
    print('Testing md5s()')
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    md5s_data = "test123"
    md5s_checksum = 'f2b1e0edfce09c07f426b85dc9fde921'
    if md5s_checksum == md5s(md5s_data):
        print('md5s() return successfull')
    else:
        print('md5() returned: %s' % md5s(md5s_data))
        print('Successful return should be: %s' % md5s_checksum)
        print('md5s() check failed')


# Generated at 2022-06-13 16:19:11.924918
# Unit test for function checksum
def test_checksum():
    assert checksum("Hello World") == checksum_s("Hello World")

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:19:15.078790
# Unit test for function md5
def test_md5():
    ''' This unit test will fail if running in FIPS mode and md5 is needed for compatibility'''
    if not _md5:
        return True
    else:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

# Generated at 2022-06-13 16:19:22.033253
# Unit test for function md5
def test_md5():
    assert (md5('lib/ansible/module_utils/basic.py') == 'd6744b0a66357107f24287b8d7e0f3c3'), 'MD5 of lib/ansible/module_utils/basic.py is d6744b0a66357107f24287b8d7e0f3c3'

# Generated at 2022-06-13 16:19:27.662878
# Unit test for function md5
def test_md5():
    md5_str = md5s('abc')
    assert md5_str == '900150983cd24fb0d6963f7d28e17f72'


# End backwards compat functions

if __name__ == '__main__':
    import os
    from ansible.module_utils.six import b
    from ansible.module_utils._text import to_bytes

    print(secure_hash_s(b('')))
    print(secure_hash_s(b('abc')))
    print(secure_hash_s(b('abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq')))

    current_path = os.path.dirname(os.path.realpath(__file__))

# Generated at 2022-06-13 16:19:32.933624
# Unit test for function md5
def test_md5():
    ''' test_md5.py:  This test checks to see if the md5 of a file matches the md5 of the file when written. '''
    import tempfile
    filename = tempfile.mktemp()
    fd = open(filename, 'w')
    fd.write('This is a test')
    fd.close()
    assert(md5(filename) == md5(filename))
    os.unlink(filename)

# Generated at 2022-06-13 16:19:35.318476
# Unit test for function md5s
def test_md5s():
    expected = '202cb962ac59075b964b07152d234b70'
    assert md5s('123') == expected, 'md5 failed'


# Generated at 2022-06-13 16:19:39.617237
# Unit test for function md5s
def test_md5s():
    assert(md5s('test') == '098f6bcd4621d373cade4e832627b4f6')
    assert(md5s(b'test') == '098f6bcd4621d373cade4e832627b4f6')


# Generated at 2022-06-13 16:19:47.212227
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s("foo", 0) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s("foo", 1) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s("foo", None, None, None) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s("foo", None, None, "foo") == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:19:52.232741
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    d1 = md5s("hello")
    d2 = md5s(u"hello")
    d3 = md5s("not the same")
    assert d1 == d2 == "5d41402abc4b2a76b9719d911017c592"
    assert d1 != d3


# Generated at 2022-06-13 16:19:54.847055
# Unit test for function md5s
def test_md5s():
    print('Testing md5s')
    test_string = 'Hello world!'
    assert md5s(test_string) == 'ed076287532e86365e841e92bfc50d8c'



# Generated at 2022-06-13 16:19:59.652675
# Unit test for function md5s
def test_md5s():
    assert md5s('HelloWorld') == '6cd3556deb0da54bca060b4c39479839'
    assert md5s(b'HelloWorld') == '6cd3556deb0da54bca060b4c39479839'
    try:
        md5s(u'HelloWorld')
    except UnicodeDecodeError as e:
        pass
    else:
        assert False, "md5s did not raise an exception for unicode input"


# Generated at 2022-06-13 16:20:05.520755
# Unit test for function checksum
def test_checksum():
    data = "secure hash test string"
    data_file = "test/file"
    testfile = open(data_file, 'w')
    testfile.write(data)
    testfile.close()

    chksum_s = secure_hash_s(data)
    chksum = secure_hash(data_file)

    print('chksum_s: %s' % chksum_s)
    print('chksum: %s' % chksum)

    assert chksum_s == chksum