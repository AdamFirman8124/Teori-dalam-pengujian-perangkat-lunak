

# Generated at 2022-06-13 16:10:14.471021
# Unit test for function md5
def test_md5():

    filename = "test/utils/testfile"

    md5_hash = secure_hash(filename, _md5)
    sha1_hash = secure_hash(filename)

    stats = os.stat(filename)

    if stats.st_size > 100000:
        print("This test is too big to run in current directory.  Please move test directory to root of python tree.")
    elif md5_hash != "769c6f1b3d3be8e2b6c31ee9079607ba":
        print("md5 test failed.")
    elif sha1_hash != "0e4e4f9e9f4c84e879f49a7c7a12e97d7b7a13b8":
        print("sha1 test failed.")
    else:
        exit(0)

# Generated at 2022-06-13 16:10:24.171540
# Unit test for function checksum
def test_checksum():
    string1 = 'hello world'
    filename1 = 'test_file1'
    fd = open(filename1, 'w')
    fd.write(string1)
    fd.close()

    if checksum_s(string1) == '5eb63bbbe01eeed093cb22bb8f5acdc3':
        print('checksum_s test: pass')
    else:
        print('checksum_s test: fail')

    if checksum(filename1) == '5eb63bbbe01eeed093cb22bb8f5acdc3':
        print('checksum test: pass')
    else:
        print('checksum test: fail')


# Generated at 2022-06-13 16:10:31.647583
# Unit test for function checksum
def test_checksum():
    '''
    ansible.utils.checksum unit test
    '''
    # Create a temporary file
    import tempfile
    temp_fd, temp_file_name = tempfile.mkstemp()

    # Write to it, and obtain the checksum
    os.write(temp_fd, b"Hello World!")
    os.close(temp_fd)
    temp_checksum = checksum(temp_file_name)

    # Clean up
    os.unlink(temp_file_name)

    # Check the computed checksum
    assert temp_checksum == "5eb63bbbe01eeed093cb22bb8f5acdc3"

    # Check md5 algorithm
    assert md5(temp_file_name) is None

# Generated at 2022-06-13 16:10:35.138695
# Unit test for function checksum
def test_checksum():
    assert checksum("/bin/ls") == "33d925e19bba05505e7a1a09df0a145b"

# Generated at 2022-06-13 16:10:42.235754
# Unit test for function md5
def test_md5():
    import os
    import tempfile

    (fd, temp_path) = tempfile.mkstemp(prefix='ansible-test-md5')
    test_data = 'abc123'

    f = os.fdopen(fd, 'w')
    f.write(test_data)
    f.close()

    assert md5(temp_path) == 'e99a18c428cb38d5f260853678922e03'
    # Clean up temp file
    os.unlink(temp_path)

# Generated at 2022-06-13 16:10:44.069572
# Unit test for function md5s
def test_md5s():
    assert md5s('123') == '202cb962ac59075b964b07152d234b70'



# Generated at 2022-06-13 16:10:47.936457
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('test'*10) == 'dd33d9eb962b79c7fef5a6a5c6bc5dcf'


# Generated at 2022-06-13 16:10:55.567854
# Unit test for function checksum
def test_checksum():
    # Create a file named "hello" and write "hello" to the file
    correct_hash = '5d41402abc4b2a76b9719d911017c592'
    fd = open('hello', 'w')
    fd.write('hello')
    fd.close()

    # The function secure_hash return the string checksum of the file
    hash = secure_hash('hello')

    # Remove "hello" file
    os.remove('hello')

    assert hash == correct_hash

# Generated at 2022-06-13 16:11:06.866924
# Unit test for function checksum
def test_checksum():
    ''' test_checksum.py:  Tests the checksum module '''

    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    local_sum = checksum("ansible/module_utils/basic.py")
    assert local_sum == "6d5c6e5b5a5f5dac1d8d8f45a7e67e77014098b7"

    remote_sum = checksum("/usr/bin/ansible-config")
    assert remote_sum == "9aa7b208a6d5e7c90cb6cb5218a02f8d3fcd6e48"

    nonexist_sum = checksum("/tmp/does/not/exist")

# Generated at 2022-06-13 16:11:10.138744
# Unit test for function md5
def test_md5():
    if not _md5:
        return
    h = "3a5f86d9c5b1fe23a5f96d1cdcf07b75"
    hh = md5("../lib/ansible/utils/module_docs_fragments/archive.py")
    assert h == hh

# Generated at 2022-06-13 16:11:17.644570
# Unit test for function md5s
def test_md5s():
    assert md5s("1") == 'c4ca4238a0b923820dcc509a6f75849b'
    assert md5s("foo") == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:11:23.350656
# Unit test for function md5s
def test_md5s():
    # FIPS-140-2 modifies the new hashlib module to disallow MD5, so those
    # systems will report 'None' for MD5 hashes.
    if _md5:
        assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
        assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
        assert md5s('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
        assert md5s('The quick brown fox jumps over the lazy dog.') == 'e4d909c290d0fb1ca068ffaddf22cbd0'

# Generated at 2022-06-13 16:11:28.079707
# Unit test for function md5s
def test_md5s():
    # We know the md5s of these two strings.  If the checksum of the string is the same, then this method is verified to work
    assert md5s("test") == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s("test2") == '5a105e8b9d40e1329780d62ea2265d8a'

# Generated at 2022-06-13 16:11:34.833349
# Unit test for function md5s
def test_md5s():
    fails = []

    test_results = [
        {
            'in': 'foo',
            'out': 'acbd18db4cc2f85cedef654fccc4a4d8'
        },
        {
            'in': 'bar',
            'out': '37b51d194a7513e45b56f6524f2d51f2'
        }
    ]

    for result in test_results:
        input = result['in']
        expected = result['out']

        output = md5s(input)
        if output != expected:
            fails.append("Input: '{}' - expected: '{}', actual: '{}'".format(input, expected, output))


# Generated at 2022-06-13 16:11:40.339078
# Unit test for function md5s
def test_md5s():
    import random
    import string 
    for i in range(100):
        test_string = ''.join(random.choice(string.ascii_letters) for x in range(100))
        assert md5s(test_string) == secure_hash_s(test_string, _md5)

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:11:50.414685
# Unit test for function checksum
def test_checksum():
    # The following checksums are based on 'ansible/modules/files/get_url.py'
    test_file = os.path.join(os.path.dirname(__file__), 'test_files', 'ls')
    test_file_md5sum = 'e59ff97941044f85df5297e1c302d260'
    test_file_sha1sum = 'a3b3a29eab73975f86e1cc7d437b39ca3e7f2a8c'
    test_file_sha256sum = '9ce97d827de0a5675f99e7e23bafd94b7cf2b43bccab7c9f8e8ef1d393554da0'

# Generated at 2022-06-13 16:11:53.409247
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'



# Generated at 2022-06-13 16:11:58.010955
# Unit test for function md5
def test_md5():
    assert md5('/Users/anandkandekar/Downloads/test') == 'b9c7b936c51b812a197c3bf3cc7f4a4f'
    assert md5('/Users/anandkandekar/Downloads/test_non_existing') == None


# Generated at 2022-06-13 16:12:07.789050
# Unit test for function checksum
def test_checksum():

    # Testing checksum
    file_content = 'This is a test file\n'
    file_path1 = './test.txt'

    # Create file and checksum
    with open(file_path1, 'wb') as f:
        f.write(file_content.encode("utf-8"))
    cs1 = checksum(file_path1)

    # Check file content and checksum
    with open(file_path1, 'rb') as f:
        file_content1 = f.read()
        assert file_content == file_content1.decode("utf-8")
    assert cs1 == checksum(file_path1)

    # Append file
    with open(file_path1, 'a') as f:
        f.write("Again, this is a test file\n")

# Generated at 2022-06-13 16:12:10.282089
# Unit test for function md5s
def test_md5s():
    assert md5s('test123') == 'f4b4d4aa4286e1b6c1ac6cd7b3499053'


# Generated at 2022-06-13 16:12:21.418576
# Unit test for function checksum
def test_checksum():
    import tempfile
    # Create a dummy file with some content
    file = tempfile.NamedTemporaryFile(delete=False)
    file.write(b"Hello World")
    file.close()
    checksum_value = checksum(file.name)
    assert len(checksum_value) == 40
    checksum_value = checksum_s(b"Hello World")
    assert len(checksum_value) == 40
    os.unlink(file.name)

# Generated at 2022-06-13 16:12:24.481729
# Unit test for function md5
def test_md5():
    if _md5 is not None:
        assert md5('files/test.txt') == 'f66a8a1d2e30a90dd9a4236274b4203a'
        assert md5('files/doesnt_exist') == None

# Generated at 2022-06-13 16:12:27.458118
# Unit test for function md5
def test_md5():
   assert md5("/etc/group") == "6adfb183a4a2c94a2d9977b85c3eb0ad"

# Generated at 2022-06-13 16:12:35.049391
# Unit test for function checksum
def test_checksum():
    # Just test that we can calculate checksum
    assert secure_hash_s('hello') is not None
    assert secure_hash('/bin/ls') is not None


# check for the function names we expect
_checksum_funcs = set(['checksum', 'checksum_s', 'md5', 'md5s'])

assert _checksum_funcs.issubset(set(globals()))

# Generated at 2022-06-13 16:12:45.379307
# Unit test for function md5s
def test_md5s():
    ''' md5s should return the same value as md5sum, if the input is a file '''

    import tempfile
    import subprocess

    # write file
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(b"this is some file data")
    tf.close()

    # compute the md5 of the file
    m = md5s(tf.name)
    # use a shell command to compute the hash of the file
    # Note, this means that the md5s function does not run on all platforms
    m2 = subprocess.check_output(["md5sum", tf.name]).split()[0].strip()
    os.unlink(tf.name)

    # make sure the two match
    assert m == m2



# Generated at 2022-06-13 16:12:49.660205
# Unit test for function md5
def test_md5():
    ''' md5 unit test '''
    assert md5("lib/ansible/module_utils/basic.py") == "08a5c5d066e3f8415fc5cfccb7f0a5c5"

# Generated at 2022-06-13 16:12:55.285613
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5s("ansible123") == "a56a1c8fd668c1d076a55a6e0a6acf8e"


# Generated at 2022-06-13 16:12:58.524087
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'


# Generated at 2022-06-13 16:13:00.612634
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"
    assert md5s("foo\n") == "19fa61d75522a4669b44e39c1d2e1726"

# Generated at 2022-06-13 16:13:13.249052
# Unit test for function checksum
def test_checksum():
    # check checksum functions
    test_file = os.path.join(os.path.dirname(__file__), "checksum.py")
    test_dir = os.path.dirname(test_file)

# Generated at 2022-06-13 16:13:22.169127
# Unit test for function md5
def test_md5():
    a = md5("/bin/cat")
    if ( a != "d41d8cd98f00b204e9800998ecf8427e" ):
        print("FAIL: " + a)
        sys.exit(2)

# Run the unit tests
if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:13:24.228091
# Unit test for function md5s
def test_md5s():
    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'


# Generated at 2022-06-13 16:13:31.988026
# Unit test for function md5s
def test_md5s():
    # Replace the global function with a mock function for unit test
    global md5s

    # Define the test cases
    test_ok = (
        (None, 'd41d8cd98f00b204e9800998ecf8427e'),
        ('', 'd41d8cd98f00b204e9800998ecf8427e'),
        ('The quick brown fox jumps over the lazy dog', '9e107d9d372bb6826bd81d3542a419d6'),
        ('The quick brown fox jumps over the lazy dog.', 'e4d909c290d0fb1ca068ffaddf22cbd0'),
    )


# Generated at 2022-06-13 16:13:39.591747
# Unit test for function checksum
def test_checksum():
    import tempfile
    import ansible.utils.checksum as checksum
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestChecksum(unittest.TestCase):

        def setUp(self):
            self.test_file = tempfile.NamedTemporaryFile(delete=False)
            self.test_file_name = self.test_file.name
            self.test_file.write(b'1234567890')
            self.test_file.close()

        def test_md5(self):
            result = checksum.md5(self.test_file_name)
            self.assertTrue(result == '81dc9bdb52d04dc20036dbd8313ed055')


# Generated at 2022-06-13 16:13:49.169898
# Unit test for function checksum
def test_checksum():
    ''' verify checksum returns expected result '''
    _cs_str_data = "Hello World"
    _cs_str_data_sha1_hexdigest = "0a4d55a8d778e5022fab701977c5d840bbc486d0"
    _cs_unicode_data = u"\u1400\u1401\u1402"
    _cs_unicode_data_sha1_hexdigest = "c0a26b5d3ef8bc12bc0052faa398538f9c783e8e"
    _cs_unix_file = "/etc/passwd"

# Generated at 2022-06-13 16:13:54.716002
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum('test/units/modules/test_checksum.py') == 'f7c83d9d9a2bea76fba85ddf28de1a187508c1b1'

# Generated at 2022-06-13 16:13:56.845800
# Unit test for function md5s
def test_md5s():
    text = "this is a test"
    assert md5s(text) == "6f8db599de986fab7a21625b7916589c"


# Generated at 2022-06-13 16:14:06.040548
# Unit test for function checksum
def test_checksum():
    import tempfile

    tmpfile = tempfile.NamedTemporaryFile()

    # test with a nonexistant file
    assert checksum("/does/not/exist") is None

    # test a directory
    assert checksum("/tmp") is None

    # test with a file
    tmpfile.write("This is some data to write to the tempfile")
    tmpfile.seek(0)

    assert checksum(tmpfile.name)==checksum(tmpfile.name)
    tmpfile.close()

# Generated at 2022-06-13 16:14:09.743423
# Unit test for function md5s
def test_md5s():
    test_data = 'one two three'
    test_hash = 'b23bd27aa7589cb09e5a47b5f17d7f45'
    assert md5s(test_data) == test_hash


# Generated at 2022-06-13 16:14:14.540615
# Unit test for function md5
def test_md5():
    testval = "test"
    testfile = "testfile"
    expected = "098f6bcd4621d373cade4e832627b4f6"
    test_f = open(testfile, 'w')
    test_f.write(testval)
    test_f.close()
    assert expected == md5(testfile)
    assert expected == md5(testfile, _md5)

# Generated at 2022-06-13 16:14:20.737354
# Unit test for function md5s
def test_md5s():
    result = md5s('test data')
    assert '0cbc6611f5540bd0809a388dc95a615b' == result, 'md5s failed'



# Generated at 2022-06-13 16:14:22.298455
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:14:26.391709
# Unit test for function md5
def test_md5():
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert md5("/bin/true") == "a06aa7d4f19e27a7a4ae4d4bd7b955c9"



# Generated at 2022-06-13 16:14:31.825884
# Unit test for function checksum
def test_checksum():
    checksum_val = checksum(__file__)
    assert isinstance(checksum_val, basestring)
    assert len(checksum_val) == 40
    assert checksum_val == 'be90b2fcf050a822ae8eeb15336e1e9d527e28bd'


# Generated at 2022-06-13 16:14:38.672689
# Unit test for function md5
def test_md5():
    if not _md5:
        raise Exception('MD5 not available.  Possibly running in FIPS mode')
    assert md5('/bin/ls') == 'aec070645fe53ee3b3763059376134f2'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:14:46.977644
# Unit test for function md5s
def test_md5s():
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("a") == "0cc175b9c0f1b6a831c399e269772661"
    assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert md5s("message digest") == "f96b697d7cb7938d525a2f31aaf161d0"
    assert md5s("abcdefghijklmnopqrstuvwxyz") == "c3fcd3d76192e4007dfb496cca67e13b"

# Generated at 2022-06-13 16:14:56.879895
# Unit test for function md5s
def test_md5s():
    # Test md5s against known values
    test_data = [
        (b'', 'd41d8cd98f00b204e9800998ecf8427e'),
        (b'hello world', '5eb63bbbe01eeed093cb22bb8f5acdc3'),
        (b'HELLO WORLD', 'e4c4d8f3bf76b692de791a173e053211'),
    ]

    for data, correct_md5 in test_data:
        assert md5s(data) == correct_md5

    # Test for bytes warning if non-ASCII data passed to md5s

# Generated at 2022-06-13 16:15:00.171821
# Unit test for function md5
def test_md5():
    assert md5('/etc/passwd') == 'b4f163d6c7caa9c938e2641dc2b2c47c'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:15:10.188650
# Unit test for function checksum
def test_checksum():
    import tempfile

    def test_checksum(filename, checksum, incorrect_checksum):
        assert checksum(filename) == incorrect_checksum
        f = open(filename, 'w')
        f.write("default")
        f.close()
        assert checksum(filename) == '02d0f9fbfcb0cc1b8dcdd27e0be1fd7a'
        os.unlink(filename)

    tmpdir = tempfile.mkdtemp()

    filename = '%s/test.txt' % tmpdir
    test_checksum(filename, checksum, None)
    test_checksum(filename, checksum_s, 'da39a3ee5e6b4b0d3255bfef95601890afd80709')

    os.rmdir(tmpdir)

# Generated at 2022-06-13 16:15:17.791884
# Unit test for function md5s
def test_md5s():
    assert md5s(b'hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(u'hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s(b'hello\xe8') == 'a6aa104e29f7e70783baa8b7a1a2f530'
    assert md5s(b'hello\xe8') == 'a6aa104e29f7e70783baa8b7a1a2f530'

# Generated at 2022-06-13 16:15:25.655068
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s(u'foo') == u'acbd18db4cc2f85cedef654fccc4a4d8'
    else:
        try:
            md5s(u'foo')
            assert False, "Should not get here"
        except:
            pass

# Generated at 2022-06-13 16:15:30.265549
# Unit test for function md5
def test_md5():
    assert md5('./test/units/lib/ansible/module_utils/basic.py') == 'b02e76bfa8daeb6d0c2fb79f1f6f9b93'



# Generated at 2022-06-13 16:15:35.596837
# Unit test for function md5s
def test_md5s():
    import random
    import string
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
    md5_result = md5s(random_string)
    assert len(md5_result) == 32
    assert md5_result == '8cb2237d0679ca88db6464eac60da96345513964'


# Generated at 2022-06-13 16:15:38.371072
# Unit test for function md5s
def test_md5s():
    data = 'test'
    md5_digest = '098f6bcd4621d373cade4e832627b4f6'
    assert md5_digest == md5s(data)

# Generated at 2022-06-13 16:15:45.424275
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    assert md5s("abc") == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s("") == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s("hello world") == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:15:52.706226
# Unit test for function md5
def test_md5():
    """
    Tests either Python's built-in md5 implementation or the one
    provided with this module.
    """

    try:
        import hashlib
    except ImportError:
        if not _md5:
            raise "Cannot test md5 implementation because hashlib is not available and the one provided with Ansible is not working."

    message = "The quick brown fox jumped over the lazy dog."
    expected_md5hash = '9e107d9d372bb6826bd81d3542a419d6'
    md5hash = md5s(message)
    if md5hash != expected_md5hash:
        raise "MD5 hash failed! Expected: %s Got: %s" % (expected_md5hash, md5hash)

    # That's all folks.


# Generated at 2022-06-13 16:15:56.030859
# Unit test for function md5
def test_md5():
    md5_expected = '098f6bcd4621d373cade4e832627b4f6'
    md5_string = md5s('test')
    print(md5_string)
    assert md5_string == md5_expected


# Generated at 2022-06-13 16:15:57.890110
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:16:05.447952
# Unit test for function md5s
def test_md5s():
    # Uncomment the following to run test on your system
    #a = os.getcwd() + "/test_md5s.py"
    #b = os.getcwd() + "/plug_in/module_utils/hashivault.py"
    #c = os.getcwd() + "/test_md5s_test.py"

    assert md5s("1234567890") == "e807f1fcf82d132f9bb018ca6738a19f"
    assert md5s("1234567890123456789012345678901234567890123456789012345678901234567890") == "57544d23b2c2bdb98e7e1d3fd00bfe06"

# Generated at 2022-06-13 16:16:10.223680
# Unit test for function md5s
def test_md5s():
    test_data = 'foo bar baz'
    result = md5s(test_data)
    expected_result = '2bfb6f16c7e63b9f39e7f0fb6aef828d'
    assert result == expected_result, 'expected: %s got %s' % (expected_result, result)


# Generated at 2022-06-13 16:16:17.688898
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('world') == '7d793037a0760186574b0282f2f435e7'


# Generated at 2022-06-13 16:16:22.545533
# Unit test for function md5
def test_md5():
    '''md5 should return a string of hex digits or raise ValueError'''

    assert isinstance(md5('/dev/null'), str) or md5('/dev/null') is None
    try:
        assert isinstance(md5s(''), str)
    except ValueError as ve:
        assert 'not available' in str(ve)


# Generated at 2022-06-13 16:16:28.823542
# Unit test for function md5
def test_md5():
    file = open("test_md5.txt","w+")
    file.write("Testing the functionality of md5 by writing this string to a file")
    file.close()
    hashed_value = md5("test_md5.txt")
    assert hashed_value == "5950c1d7f482a8d829bde2a2a2a7a1cc"
    os.remove("test_md5.txt")



# Generated at 2022-06-13 16:16:37.625277
# Unit test for function md5
def test_md5():
    assert md5s(b'') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:16:46.734199
# Unit test for function checksum
def test_checksum():
    ''' checksum.py: Test for checksum correctness'''

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import mock_open, patch

    class TestChecksum(unittest.TestCase):

        @patch('os.path.exists', return_value=True)
        @patch('os.path.isdir', return_value=False)
        @patch('__builtin__.open', mock_open(read_data='foobar'))
        def test_checksum(self, *args):
            self.assertEqual(checksum('dummy'), '8843d7f92416211de9ebb963ff4ce28125932878')


# Generated at 2022-06-13 16:16:54.708244
# Unit test for function md5
def test_md5():
    ''' test_md5.py: Unit test for function md5 '''

    from StringIO import StringIO
    import tempfile

    # md5 hash for data
    data = 'Hello World!'
    md5_hash = 'fa1dcba65f3bbea3a8a80083577c9aa5'
    omd5_hash = md5s(data)
    assert md5_hash == omd5_hash

    # md5 hash for a file

# Generated at 2022-06-13 16:17:01.573441
# Unit test for function checksum
def test_checksum():
    ''' test_checksum()

    This test is only run when this module is called directly.
    '''

    filename = "/etc/passwd"
    checksum = secure_hash(filename)
    checksum_s = secure_hash_s("ABCD")

    print("Checksum for " + filename + " is " + checksum)
    print("Checksum for data ABCD is " + checksum_s)


if __name__ == "__main__":
    test_checksum()

# Generated at 2022-06-13 16:17:03.978790
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:17:07.922878
# Unit test for function md5s
def test_md5s():
    ''' md5s() returns a md5 digest given a string '''
    if _md5:
        assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:17:14.005522
# Unit test for function md5
def test_md5():
    test_file_path = 'test/testdata/test.cfg'
    md5_digest = '80bab6e4c87d3eafbba1e0d5fc87d35c'
    result = md5(test_file_path)
    assert result == md5_digest, "md5 digest value doesn't match"


# Generated at 2022-06-13 16:17:21.443759
# Unit test for function md5s
def test_md5s():
    # md5s of an empty string is d41d8cd98f00b204e9800998ecf8427e
    assert('d41d8cd98f00b204e9800998ecf8427e' == md5s(''))



# Generated at 2022-06-13 16:17:29.339581
# Unit test for function md5
def test_md5():
    # Test md5 of a string
    md5_str = md5s('''
test:
  - a
  - b
  - c
''')
    assert md5_str == '8a18a23b1675c7f2ccc8a858ff40fde9'

    # Test md5 of a file
    md5_file = md5('lib/ansible/modules/core/debug/__init__.py')
    assert md5_file == '9786b040d6e00a8f365b4099ffc85ec9'


# Generated at 2022-06-13 16:17:33.909209
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    # test with an existing file
    assert md5('/etc/redhat-release')

    # test with a non existing file
    assert not md5('/non/existing/file/path')


# Generated at 2022-06-13 16:17:45.858726
# Unit test for function md5
def test_md5():
    import os
    from ansible.utils.path import unfrackpath
    from tempfile import mkstemp

    basefile = "./test_utils_path_md5"
    (tmp_fd, tmp_file) = mkstemp(prefix=basefile, suffix=".tmp")
    os.close(tmp_fd)
    os.unlink(tmp_file)
    with open(tmp_file, "w") as f:
        f.write("foo")

    try:
        if md5(unfrackpath("~/%s"%basefile)) != md5(tmp_file):
            print("ERROR: generated md5 doesn't match")
    except ValueError:
        print("MD5 not available.  Possibly running in FIPS mode")
    finally:
        os.unlink(tmp_file)

# Generated at 2022-06-13 16:17:50.456623
# Unit test for function md5s
def test_md5s():
    '''
    SHA1 is always available in python 2.4+, but MD5 is not if running in FIPS mode
    '''
    try:
        assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'
    except ValueError as e:
        if 'MD5 not available.  Possibly running in FIPS mode' in str(e):
            pass
        else:
            raise

# Generated at 2022-06-13 16:17:56.266509
# Unit test for function md5s
def test_md5s():
   
    assert (len(md5s("abcd")) == 32)
    assert (md5s("abcd") == "e2fc714c4727ee9395f324cd2e7f331f")
    assert (md5s("abcd") != md5s("abcd "))
 

# Generated at 2022-06-13 16:17:58.114299
# Unit test for function md5s
def test_md5s():
    result = md5s("foobar")
    assert result == "acbd18db4cc2f85cedef654fccc4a4d8"

# Generated at 2022-06-13 16:18:05.157066
# Unit test for function md5
def test_md5():

    # Create dummy file
    f = open('/tmp/myfile.txt', 'w')
    f.write('Some text to be written')
    f.close()

    # Compute md5
    mymd5 = md5('/tmp/myfile.txt')
    assert (mymd5 == '9646b8bc5cdfcfa7d92a3966af5b5e3b')

if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:18:08.623557
# Unit test for function checksum
def test_checksum():
    sha1_digest = checksum_s('hello')
    # Checksum generated with sha1sum
    assert sha1_digest == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'

# Generated at 2022-06-13 16:18:11.120042
# Unit test for function checksum
def test_checksum():
    ''' checksum unit test. '''

    if os.path.exists('/etc/ansible/hacking/env-setup'):
        if os.path.exists('/etc/ansible/hacking/env-setup.bak'):
            os.remove('/etc/ansible/hacking/env-setup.bak')

# Generated at 2022-06-13 16:18:18.571591
# Unit test for function checksum
def test_checksum():
    assert checksum_s('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    assert checksum_s('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'



# Generated at 2022-06-13 16:18:31.109186
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('testing') == 'ae2b1fca515949e5d54fb22b8ed95575'
    assert md5s('testing') == 'ae2b1fca515949e5d54fb22b8ed95575'
    assert md5s('testing') == 'ae2b1fca515949e5d54fb22b8ed95575'


# Generated at 2022-06-13 16:18:34.229015
# Unit test for function md5s
def test_md5s():
    # FIPS mode will raise an error
    if _md5:
        md5s('test_md5s')


# Generated at 2022-06-13 16:18:40.162530
# Unit test for function md5s
def test_md5s():
    from ansible.compat.tests import unittest

    class TestMD5S(unittest.TestCase):

        def test_md5s(self):
            self.assertEqual(md5s('FOO'), 'acbd18db4cc2f85cedef654fccc4a4d8')
            self.assertEqual(md5s('bar'), '37b51d194a7513e45b56f6524f2d51f2')

    unittest.main()


# Generated at 2022-06-13 16:18:47.834549
# Unit test for function checksum
def test_checksum():
    filename = 'testfile'
    blocksize = 64 * 1024
    infile = open(filename, 'wb')
    for i in range(0x40):
        block = os.urandom(blocksize)
        infile.write(block)
    infile.close()
    hex_digest = checksum(filename)
    if hex_digest is not None:
        os.remove(filename)
    assert len(hex_digest) == 40

# Generated at 2022-06-13 16:18:48.908792
# Unit test for function md5s
def test_md5s():
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'


# Generated at 2022-06-13 16:18:51.578950
# Unit test for function md5s
def test_md5s():
    return md5s("abc123") == "e99a18c428cb38d5f260853678922e03"


# Generated at 2022-06-13 16:18:56.047707
# Unit test for function md5
def test_md5():
    assert md5('setup.py') == '94800c97aa7ec91a59dfc5d15f5c5da5'


# Generated at 2022-06-13 16:18:59.787013
# Unit test for function md5
def test_md5():
    ''' md5.py: md5 test'''
    assert md5("/bin/ls") == "8b8e881f2382f0709fea2a8afd34f76e"


# Generated at 2022-06-13 16:19:04.867697
# Unit test for function md5
def test_md5():
    '''Unit test for function md5'''
    fname = './lib/ansible/modules/system/yum.py'
    assert md5(fname) == md5(fname)

# Generated at 2022-06-13 16:19:17.806343
# Unit test for function checksum
def test_checksum():
    from tempfile import NamedTemporaryFile
    import shutil
    testfile = NamedTemporaryFile(delete=False)
    testfile.write('hello world')
    testfile.close()

    # sha1
    assert checksum(filename=testfile.name) == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    # md5
    assert md5(filename=testfile.name) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:19:19.549881
# Unit test for function md5s
def test_md5s():
    assert md5s("Hello World!") == "b10a8db164e0754105b7a99be72e3fe5"


# Generated at 2022-06-13 16:19:21.164470
# Unit test for function md5s
def test_md5s():
    assert md5s('data') == '1f3870be274f6c49b3e31a0c6728957f'



# Generated at 2022-06-13 16:19:23.450795
# Unit test for function md5s
def test_md5s():
    ''' secure_hash_s.md5s should return a string '''
    from ansible.utils.hashing import secure_hash_s
    assert isinstance(secure_hash_s.md5s("Hello World"), basestring)



# Generated at 2022-06-13 16:19:33.483173
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import random
    import string

    temp_dir = tempfile.mkdtemp()
    dummy1 = os.path.join(temp_dir, "dummy.txt")
    dummy2 = os.path.join(temp_dir, "dummy2.txt")

    # create dummy files
    f1 = open(dummy1, "w")
    f2 = open(dummy2, "w")
    for x in range(0, 10):
        f1.write(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(100)]))
        f2.write(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(100)]))
    f1.flush()
   

# Generated at 2022-06-13 16:19:41.154268
# Unit test for function md5
def test_md5():

    def filecmp(a,b):
        with open(a, 'rb') as f1:
            with open(b, 'rb') as f2:
                return f1.read() == f2.read()

    test_text_file = 'test/files/test_text_file'
    test_bin_file = 'test/files/test_bin_file'

    assert md5(test_text_file) == 'b10a8db164e0754105b7a99be72e3fe5', "test file not hashed correctly"
    assert md5(test_bin_file) == '1a5f38a34b05146e8d6d8c7b0f6dbc5a', "test file not hashed correctly"

    # verify that multiple runs do not change the hash

# Generated at 2022-06-13 16:19:44.385096
# Unit test for function md5
def test_md5():
    data = 'abcdefghijklmnopqrstuvwxyz'
    md5_output = md5s(data)
    assert md5_output == 'c3fcd3d76192e4007dfb496cca67e13b'



# Generated at 2022-06-13 16:19:48.343380
# Unit test for function md5
def test_md5():
    if not _md5:
        raise Exception('MD5 not available.  Possibly running in FIPS mode')


#
# Old checksum algorithm.  It is needed to support old variables
#


# Generated at 2022-06-13 16:19:56.457807
# Unit test for function checksum
def test_checksum():
    def test_checksum_semantics():
        '''
        Makes sure that checksums are matching and different between files
        '''

        # ensure the same data yields the same checksum
        same_data_same_checksum = checksum_s('same_data_same_checksum')

        # ensure identical contents yield the same checksum
        f1 = open('test_checksum_1.txt', 'w')
        f2 = open('test_checksum_2.txt', 'w')
        f1.write('this is test data')
        f2.write('this is test data')
        assert checksum('test_checksum_1.txt') == checksum('test_checksum_2.txt')

        # ensure different contents yield different checksums
        f1 = open('test_checksum_1.txt', 'w')


# Generated at 2022-06-13 16:19:59.909518
# Unit test for function md5
def test_md5():
    import tempfile
    fd, path = tempfile.mkstemp()
    os.write(fd, b"some data")
    os.close(fd)
    checksum = md5(path)
    os.remove(path)
    assert checksum == '958e9a94f7d6f1cb2533f8a2421b76dc'
