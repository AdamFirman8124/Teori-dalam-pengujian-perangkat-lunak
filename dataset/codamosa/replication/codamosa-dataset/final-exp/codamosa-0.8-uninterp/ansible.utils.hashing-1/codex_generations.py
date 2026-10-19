

# Generated at 2022-06-13 16:10:12.851384
# Unit test for function checksum
def test_checksum():
    # This test is intended to verify that the function checksum is
    # returning the correct checksum for the file.
    file_name = os.path.join(os.path.dirname(__file__), 'hashsum_test')
    checksum_result = checksum(file_name)
    assert checksum_result == '51727f7c8d33249067b2975f4d435e53a8d4a4bd'


# Generated at 2022-06-13 16:10:22.284605
# Unit test for function md5
def test_md5():
    ''' utility to do a basic self test of md5 file hash'''

    import shutil

    tmpfile = "/tmp/ansible-test-md5"
    with open(tmpfile,"wb") as f:
        f.write("abcdefghijklmnopqrstuvwxyz1234567890\n")
        f.write("abcdefghijklmnopqrstuvwxyz1234567890\n")

    m = md5(tmpfile)
    if m == "feddb3a3b1aec32a95b28e0f63c8b2d9":
        print("Correct Checksum")
    else:
        print("Incorrect Checksum")
    os.unlink(tmpfile)

# Generated at 2022-06-13 16:10:30.783918
# Unit test for function checksum
def test_checksum():
    '''test_checksum: test checksum function'''
    assert checksum_s('abc') == 'a9993e364706816aba3e25717850c26c9cd0d89d'

    assert checksum('./lib/ansible/module_utils/basic.py', checksum_s) == '0d45c081f3e3d7c8a0f676aacb0e9b85db8b8e2d'

# Generated at 2022-06-13 16:10:33.647008
# Unit test for function md5s
def test_md5s():
    try:
        md5s('foo')
    except ValueError:
        print("md5s not working.  Probably in FIPS 140-2 mode")
    else:
        print("md5s is working")


# Generated at 2022-06-13 16:10:40.339785
# Unit test for function checksum
def test_checksum():
    sample = 'The quick brown fox jumped over the lazy dog'
    checksum_expected = '07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b5ed6e1bfd7097821233fa0538f3db854fee6'
    assert checksum_s(sample) == checksum_expected

# Generated at 2022-06-13 16:10:48.584775
# Unit test for function checksum
def test_checksum():
    import os
    import tempfile

    fd = tempfile.NamedTemporaryFile()
    fd.write(b"hello")
    fd.flush()

    # Test checksum with file
    assert checksum(fd.name) == "5d41402abc4b2a76b9719d911017c592"
    assert checksum_s("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test with directory
    assert checksum_s(os.path.dirname(fd.name)) is None

    # Test fallback to sha1 if md5 is not available
    _md5 = None
    assert checksum(fd.name) == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2022-06-13 16:10:55.549248
# Unit test for function md5
def test_md5():
    from tempfile import mkstemp
    from shutil import rmtree


# Generated at 2022-06-13 16:10:57.270922
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello\x00') == 'f0a7042d8fadc21d7cef0b66e7c8f8d1'


# Generated at 2022-06-13 16:11:02.186227
# Unit test for function md5
def test_md5():
    ''' md5 should return expected value on known data '''

    test_data = "AnsibleTestString"
    expected_checksum = "01e1e30bdc11b67c07c1ebb6f3b3c9d6"

    calculated_checksum = md5s(test_data)

    if expected_checksum != calculated_checksum:
        print("md5 failed: expected %s, got %s" % (expected_checksum, calculated_checksum))
        return False

    return True



# Generated at 2022-06-13 16:11:06.987514
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'
    else:
        failed = False
        try:
            md5s('foobar')
        except ValueError:
            failed = True
        assert failed

# Generated at 2022-06-13 16:11:15.736984
# Unit test for function md5
def test_md5():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    # Create a temporary test file
    tempfile = 'test_md5.txt'
    with open(tempfile, 'w') as f:
        f.write('hello')

    assert md5(tempfile) == '5d41402abc4b2a76b9719d911017c592'

    os.remove(tempfile)


# Generated at 2022-06-13 16:11:21.626390
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as f:
        f.write('Hello')
        f.flush()
        assert md5(f.name) == '8b1a9953c4611296a827abf8c47804d7'

md5sum = md5

# Generated at 2022-06-13 16:11:28.128790
# Unit test for function checksum
def test_checksum():
    import tempfile
    import filecmp

    with tempfile.NamedTemporaryFile(mode='wb') as tempf:
        tempf.write(b"Hello World!")
        tempf.seek(0)
        checksum_value = checksum(tempf.name)
        checksum_s_value = checksum_s("Hello World!")

        assert "b10a8db164e0754105b7a99be72e3fe5" == checksum_value
        assert checksum_value == checksum_s_value

# Generated at 2022-06-13 16:11:32.021110
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/passwd') == '75dca93fde7e5a9f1c7bab52e2fa2ccb1da5c386'


# Generated at 2022-06-13 16:11:38.629250
# Unit test for function md5s
def test_md5s():
    ''' test_md5s is a simple unit test.
        It will test that the md5s function returns the correct
        value, the md5 hash of a given string.
    '''
    # The correct md5 hash of the string "test".
    test_hash = '098f6bcd4621d373cade4e832627b4f6'

    assert md5s('test') == test_hash

# Generated at 2022-06-13 16:11:49.842623
# Unit test for function checksum
def test_checksum():
    import sys

    # The test will fail in FIPS mode because the 'md5' module is not available
    if not _md5:
        sys.stderr.write('Skipping md5 checksum tests because md5 is not available in FIPS mode\n')
        return

    h = to_bytes('hello world', errors='surrogate_or_strict')

    assert checksum_s(h) == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert md5s(h) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    # verify that we can run both md5 and sha1 in the same process
    md5s(h)
    checksum_s(h)


# Generated at 2022-06-13 16:11:57.714184
# Unit test for function md5s
def test_md5s():
    test_str = '''I solemnly swear that I will support and defend the Constitution of the United
    States against all enemies, foreign and domestic; that I will bear true faith and
    allegiance to the same; and that I will obey the orders of the President of the United
    States and the orders of the officers appointed over me, according to regulations and
    the Uniform Code of Military Justice. So help me God.'''

    assert md5s(test_str) == 'b5d3b7a5b5c5e7284d1f3300a7cf811e'

# Generated at 2022-06-13 16:12:08.580232
# Unit test for function md5
def test_md5():
    test_file = 'test_file_for_checksum'
    test_contents = 'test of checksum function'
    test_md5 = '0cbc6611f5540bd0809a388dc95a615b'

    # Test with new file
    try:
        f = open(test_file, 'wb')
        f.write(test_contents)
        f.close()
        assert md5(test_file) == test_md5
    finally:
        os.remove(test_file)

    # Test with empty file

# Generated at 2022-06-13 16:12:11.378191
# Unit test for function md5
def test_md5():
    assert md5("helpers/test/test_utils.py") == 'e3c2e2ac8a0f9a2b9d09c5789c5fb6e1'


# Generated at 2022-06-13 16:12:18.043121
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.basic import AnsibleModule

    def test_md5_sha1(data):
        md5_check = md5s(to_bytes(data, errors='surrogate_or_strict')).upper()
        sha1_check = checksum_s(data).upper()
        return (md5_check, sha1_check)

    module = AnsibleModule(
        argument_spec = dict(
            data = dict(required=True),
        ),
    )

    s = "foo"
    (md5_check, sha1_check) = test_md5_sha1(s)
    module.exit_json(changed=False, md5s=md5_check, checksum=sha1_check)


# Generated at 2022-06-13 16:12:22.247019
# Unit test for function checksum
def test_checksum():
    print(checksum_s('abc'))
    print(checksum('/etc/ssh/ssh_config'))

# Generated at 2022-06-13 16:12:28.503300
# Unit test for function checksum
def test_checksum():
    '''
    Ensure we can compute the checksum of a file
    '''

    test_file_name = 'checksum_test_file.txt'
    test_file_contents = 'SOME TEXT\nLINE TWO\nLAST LINE\n'

    test_file = open(test_file_name, 'w')
    test_file.write(test_file_contents)
    test_file.close()

    sha1sum = secure_hash(test_file_name)

    assert sha1sum == '4d5a70ec266da928fde57b8a5e1f1183ab31f190'

    os.remove(test_file_name)



# Generated at 2022-06-13 16:12:35.151697
# Unit test for function md5
def test_md5():
    """This is not a real test. It is just a collection of test vectors to help
    with debugging and testing.
    """
    md5("/bin/bash")
    md5("/bin/dne")
    md5(None)
    md5("")
    md5("/etc/group-")


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:39.149011
# Unit test for function checksum
def test_checksum():
    """ Test the ansible.utils.checksum function with a simple string """
    assert checksum_s('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'


# Generated at 2022-06-13 16:12:45.292405
# Unit test for function md5
def test_md5():
    test_file = os.path.join(os.path.dirname(__file__), 'test_md5.txt')
    f = open(test_file, 'w')
    f.write('hello')
    f.close()
    assert md5(test_file) == '5d41402abc4b2a76b9719d911017c592'
    os.unlink(test_file)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:54.544889
# Unit test for function md5
def test_md5():
    from StringIO import StringIO
    from tempfile import NamedTemporaryFile
    from os import unlink
    # Test for md5 for StringIO
    s = StringIO('abcdef')
    if md5(s) != '7ac66c0f148de9519b8bd264312c4d64':
        return False

    # Test for md5 for normal file
    f = NamedTemporaryFile()
    f.write('abcdef')
    f.flush()
    if md5(f.name) != '7ac66c0f148de9519b8bd264312c4d64':
        return False
    f.close()
    return True


# Generated at 2022-06-13 16:13:03.783256
# Unit test for function checksum

# Generated at 2022-06-13 16:13:14.384601
# Unit test for function checksum
def test_checksum():
    test_file = 'test_checksum'
    test_file_content = 'test'
    checksum = secure_hash(test_file)
    assert checksum == u'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff', checksum
    checksum_sum = secure_hash_s(test_file_content)
    assert checksum_sum == u'900150983cd24fb0d6963f7d28e17f72', checksum_sum

if __name__ == '__main__':
    test_checksum

# Generated at 2022-06-13 16:13:18.596589
# Unit test for function md5s
def test_md5s():
    test_data = "A"
    hashed_data = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"
    assert md5s(test_data) == hashed_data

# Generated at 2022-06-13 16:13:25.618973
# Unit test for function checksum
def test_checksum():
    chksum = checksum(__file__)
    assert chksum == checksum(__file__)
    assert checksum_s(__file__) == chksum

    chksum = checksum_s(__file__)
    assert chksum == checksum_s(__file__)
    assert checksum(__file__) == chksum

    try:
        checksum('/dev/null')
        assert False
    except AnsibleError as e:
        pass



# Generated at 2022-06-13 16:13:35.396212
# Unit test for function md5
def test_md5():
    if _md5:
        assert "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c" == md5('/etc/resolv.conf')
    else:
        try:
            md5('/etc/resolv.conf')
            assert False
        except ValueError as e:
            assert "MD5 not available.  Possibly running in FIPS mode" in str(e)


# Generated at 2022-06-13 16:13:40.648627
# Unit test for function md5
def test_md5():
    """Unit test for function md5"""

    result = md5('data/ansible_test.ini')
    assert result == '22a31e0a0e3d9f9a4794e58b717bce91'



# Generated at 2022-06-13 16:13:46.327058
# Unit test for function checksum
def test_checksum():
    '''test md5 checksum'''

    assert checksum_s('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'

    assert checksum('test/files/checksum/foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'



# Generated at 2022-06-13 16:13:56.883544
# Unit test for function checksum
def test_checksum():
    checksum_of_empty_string = secure_hash_s('')
    assert checksum_of_empty_string == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    checksum_of_empty_file = secure_hash('checksum_test_file.zip')
    assert checksum_of_empty_file == 'c4e6db4466dfe1a908929380c88928b046eba956'
    checksum_of_non_empty_string = secure_hash_s('This is a non empty string')
    assert checksum_of_non_empty_string == 'e4820b45d2277f3844eac66c903e84be'

# Generated at 2022-06-13 16:14:06.130790
# Unit test for function md5
def test_md5():
    # Open file sample.txt for reading in binary mode
    fo = open("sample.txt", "rb")
    str = fo.read();

    # Close opend file
    fo.close()

    # Unit test for function md5s
    print("Md5 checksum for sample.txt is : ", md5s(str))
    # Unit test for function md5
    print("Md5 checksum for sample.txt is : ", md5("sample.txt"))

# Call unit test function
test_md5()

# Generated at 2022-06-13 16:14:10.711275
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as f:
        f.write(b'Hello, World!')
        f.flush()
        assert md5(f.name) == '0a0a9f2a6772942557ab5355d76af442'

# Generated at 2022-06-13 16:14:17.431180
# Unit test for function checksum
def test_checksum():
    data = "testdata"
    if checksum_s(data) != 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3':
        raise Exception("checksum_s returned a bad checksum")
    if (not os.path.exists('./testfile')):
        raise Exception("testfile doesn't exist")
    if checksum('./testfile') != 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3':
        raise Exception("checksum returned a bad checksum")

# Generated at 2022-06-13 16:14:19.011722
# Unit test for function md5s
def test_md5s():
    result = md5s('test')
    assert result == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:14:24.049128
# Unit test for function md5s
def test_md5s():
    data = "hello"
    md5_hash = md5s(data)
    assert md5_hash == '5d41402abc4b2a76b9719d911017c592', 'md5s hash of %s is %s' % (data, md5_hash)
    sha1_hash = checksum_s(data)
    assert sha1_hash == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d', 'sha1 hash of %s is %s' % (data, sha1_hash)



# Generated at 2022-06-13 16:14:29.693274
# Unit test for function md5s
def test_md5s():
    h = md5s("Hello world!")
    if h != "ed076287532e86365e841e92bfc50d8c":
        raise Exception("md5 hash of 'Hello world!' does not match sample.")
    else:
        print("md5 hash of 'Hello world!': %s" % h)


# Generated at 2022-06-13 16:14:44.270693
# Unit test for function checksum
def test_checksum():
    """
    Tests the checksum() functions with strings and files.
    """
    assert checksum_s("test") == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "Failed to verify sha1 digest of a string with checksum_s()"
    assert checksum_s("test", hash_func=_md5) == "098f6bcd4621d373cade4e832627b4f6", "Failed to verify md5 digest of a string with checksum_s()"
    assert checksum("test.py") == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "Failed to verify sha1 digest of a file with checksum()"

# Generated at 2022-06-13 16:14:48.150200
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"


# Generated at 2022-06-13 16:14:52.470922
# Unit test for function md5
def test_md5():
    data = "abcdefghijklmnopqrstuvwxyz"
    result = md5s(data)
    # The checksum algorithm must match with the algorithm in ShellModule.checksum() method
    assert result == "c3fcd3d76192e4007dfb496cca67e13b"

# Generated at 2022-06-13 16:15:01.591215
# Unit test for function checksum
def test_checksum():
    test_file = "./test/unit/utils/test_checksum.txt"
    test_file2 = "./test/unit/utils/test_sha.txt"

    # Test checksum function
    cksum1 = checksum(test_file)
    assert cksum1 == '7e0f8d15d7c9b9eba5a5d68f6a59c6a5'

    cksum2 = checksum(test_file)
    assert cksum2 == cksum1

    # Test checksum_s function
    cksum1 = checksum_s("hello world")
    assert cksum1 == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'


# Generated at 2022-06-13 16:15:10.985679
# Unit test for function checksum
def test_checksum():
    ''' test checksum function '''
    import tempfile
    test_string = 'This is a test string'
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(test_string)
    tmp.flush()
    assert checksum(tmp.name) == '2e8f97d2c2dae0fa6c9a6f66e7a0c0e4cfc43283'
    tmp.close()
    assert checksum_s(test_string) == '2e8f97d2c2dae0fa6c9a6f66e7a0c0e4cfc43283'
    if _md5:
        assert md5(tmp.name) == 'f13532de866a1cdfdb8e5d2f5a67f245'
        assert md

# Generated at 2022-06-13 16:15:13.070631
# Unit test for function md5
def test_md5():
    assert md5("/bin/true") == "2f1011b0c8f7f1d9c486fa9b0f61b0dd"


# Generated at 2022-06-13 16:15:14.810244
# Unit test for function md5s
def test_md5s():
    assert md5s('1') == 'c4ca4238a0b923820dcc509a6f75849b'

# Generated at 2022-06-13 16:15:16.722337
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert(md5s("my test string") == "a030aec5f5ffc8b814c7b5f5c539f53a")

# Generated at 2022-06-13 16:15:21.887991
# Unit test for function md5s
def test_md5s():
     data = """one
two
three
"""
     assert md5s(data) == '6a5ef6c079173c8b26a4b4d504b4a1a6'
     # TODO: add more unit tests


# Generated at 2022-06-13 16:15:29.751390
# Unit test for function md5
def test_md5():
    assert md5s("abcdef") == md5s("abcdef")
    assert md5s("abcdef") != md5s("abcdefg")
    assert md5s("abcdef") != md5s("abcdeg")
    assert md5s("abcdef") != md5s("bcdef")
    assert md5s("abcdef") != md5s("bcdefg")
    assert md5s("abcdef") != md5s("abcdeg")
    assert md5s("abcdef") != md5s("bcdef")
    assert md5s("abcdef") != md5s("bcdefg")
    assert md5s("abcdef") != md5s("abcdefxxabcdef")


# Generated at 2022-06-13 16:15:35.522555
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5('/dev/null') == 'd41d8cd98f00b204e9800998ecf8427e'


# Generated at 2022-06-13 16:15:38.610614
# Unit test for function md5s
def test_md5s():
    if md5s('foobar') == '3858f62230ac3c915f300c664312c63f':
        return True
    else:
        raise AssertionError('md5s returned a bad checksum')


# Generated at 2022-06-13 16:15:42.969632
# Unit test for function md5
def test_md5():
    filename="ansible/test/hash_test.txt"
    expected = "1b914ddc7a0f3d0b726d70b574895c3"
    current = md5(filename)
    assert current == expected

# Generated at 2022-06-13 16:15:46.904101
# Unit test for function md5
def test_md5():
    ''' md5sum tests '''

    md5 = secure_hash
    md5_s = secure_hash_s

    # test data
    data = b'''Hello world\n'''
    md5_s_hex = '5eb63bbbe01eeed093cb22bb8f5acdc3'
    md5_hex = 'ed076287532e86365e841e92bfc50d8c'

    # tests
    assert md5_s(data) == md5_s_hex
    assert md5_s(data) != md5(data)

    # write data to file
    with open('/tmp/md5_test.txt', 'wb') as f:
        f.write(data)

    # test with file

# Generated at 2022-06-13 16:15:50.643814
# Unit test for function md5
def test_md5():
    text1 = 'abc'
    text2 = 'abcdefghijklmnopqrstuvwxyz'
    assert md5s(text1) == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s(text2) == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:15:53.619045
# Unit test for function md5s
def test_md5s():
    assert(md5s('hello') == '5d41402abc4b2a76b9719d911017c592')


if __name__ == "__main__":
    test_md5s()

# Generated at 2022-06-13 16:15:58.649247
# Unit test for function md5s
def test_md5s():
    # Actual value of "abc" md5 hash is 900150983cd24fb0d6963f7d28e17f72
    assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"

# Generated at 2022-06-13 16:16:05.679588
# Unit test for function checksum
def test_checksum():
    ''' unit test for checksum '''

    import tempfile

    tf = tempfile.NamedTemporaryFile()
    tf.write(b'foobar')
    tf.flush()
    assert checksum(tf.name) == checksum_s('foobar')
    tf.close()


if __name__ == '__main__':
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-13 16:16:13.222674
# Unit test for function md5s
def test_md5s():
    case1 = "The quick brown fox jumps over the lazy dog"
    case1_result = "9e107d9d372bb6826bd81d3542a419d6"
    case1_result_fail = "9e107d9d372bb6826bd81d3542a419d7"
    case2 = ""
    case2_result = "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s(case1) == case1_result
    assert md5s(case1) != case1_result_fail
    assert md5s(case2) == case2_result


# Generated at 2022-06-13 16:16:15.909346
# Unit test for function md5s
def test_md5s():
    assert md5s('ansible') == 'b3bd2ef31f1f3e9ce5be5e5b5f5b5ecc'



# Generated at 2022-06-13 16:16:23.731115
# Unit test for function checksum
def test_checksum():
    import tempfile

    fd, filename = tempfile.mkstemp()
    f = os.fdopen(fd, 'wb')
    f.write("Hello World")
    f.close()
    checksum = secure_hash(filename)
    assert checksum == 'f6cde2cdaacd82338c0e4d3d4e7dc949adaa4ded'
    os.unlink(filename)

# Generated at 2022-06-13 16:16:25.814888
# Unit test for function md5s
def test_md5s():
    import os
    md5_val = md5s(os.urandom(100))
    assert len(md5_val) == 32


# Generated at 2022-06-13 16:16:30.174903
# Unit test for function md5s
def test_md5s():
    hello = "hello"
    hello_sum = "5d41402abc4b2a76b9719d911017c592"
    assert md5s(hello) == hello_sum


# Generated at 2022-06-13 16:16:38.772828
# Unit test for function md5
def test_md5():
    "md5 Unit test."
    test_string = 'This is a unit test'
    test_file = '/tmp/ansible_test_md5.txt'

    try:
        # Write a test file
        file = open(test_file, 'w')
        file.write(test_string)
        file.close()

        if md5s(test_string) != '03b334c31e8ffc636e55f14064d6d98e' or md5(test_file) != '03b334c31e8ffc636e55f14064d6d98e':
            return False
    finally:
        os.remove(test_file)

    return True

if __name__ == '__main__':
    print('Running md5 Unit Tests')

# Generated at 2022-06-13 16:16:41.361302
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello there') == 'a79169c64f756d746f1c33b8b9e08a9f'


# Generated at 2022-06-13 16:16:43.324397
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:16:45.168050
# Unit test for function md5s
def test_md5s():
    "Unit test for function md5s"
    result = md5s('testData')
    print(result)



# Generated at 2022-06-13 16:16:50.766542
# Unit test for function md5s
def test_md5s():
    assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert md5s("def") == "4d186321c1a7f0f354b297e8914ab240"
    assert md5s("abcdef") == "e80b5017098950fc58aad83c8c14978e"

# Generated at 2022-06-13 16:17:00.249700
# Unit test for function md5
def test_md5():
    filename = os.path.join(os.path.dirname(__file__), "test_md5.py")
    expected_md5 = "6efcef6a9b01e3273abd3fdbf0a8878e"
    print("md5 of %s is %s, expected_md5 is %s" % (filename, md5(filename), expected_md5))
    if expected_md5 == md5(filename):
        print("md5 test passed")
    else:
        print("md5 test failed")


# Generated at 2022-06-13 16:17:04.178554
# Unit test for function md5
def test_md5():
    if _md5:
        assert md5('test/test.py') == 'e5c539b06a2d77f0c835daae22e7f67e'
    else:
        assert md5('test/test.py') == None


# Generated at 2022-06-13 16:17:14.255430
# Unit test for function checksum
def test_checksum():

    assert(checksum_s("abcd") == 'e2fc714c4727ee9395f324cd2e7f331f')
    assert(checksum_s("abcd", sha1) == 'e2fc714c4727ee9395f324cd2e7f331f')
    assert(checksum_s("abcd", _md5) == '900150983cd24fb0d6963f7d28e17f72')

# Generated at 2022-06-13 16:17:16.946131
# Unit test for function md5s
def test_md5s():
    res = md5s('hello')
    assert res == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:17:27.307191
# Unit test for function md5s
def test_md5s():
    test_data = [('abcdef', 'e80b5017098950fc58aad83c8c14978e'),
                 ('ABCDEF', 'b0633c29348604b0e6fbdcec8b07d841'),
                 ('1234567890', '031bf4468a8c72b58e6a1d1a5d8d5471'),
                 ('1234567890123456789987654321', '7e4b4f8c7f4d0c2ac7fd900017a64cad')]
    for (data, md5sum) in test_data:
        new_md5sum = md5s(data)
        assert(new_md5sum == md5sum)

# Generated at 2022-06-13 16:17:35.270023
# Unit test for function checksum
def test_checksum():
    '''Unit test function checksum'''

    data = 'pipeline'
    assert checksum_s(data) == '30d193a737d75e6322f7a2a2b4e7d57b0fef5c6e'

    data = ''
    assert checksum_s(data) == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'

    data = '\xff'
    assert checksum_s(data) == 'acb6ce80981ca2c06fbc9a3716ec6fe5b6b527a0'



# Generated at 2022-06-13 16:17:45.014128
# Unit test for function md5
def test_md5():
    import os
    from tempfile import mkstemp
    (fd, md5file) = mkstemp(prefix='ansible_test_md5_')
    os.close(fd)
    with open(md5file, 'wb') as f:
        f.write('hello world ping')
    try:
        assert md5(md5file) == 'b026324c6904b2a9cb4b88d6d61c81d1'
    finally:
        os.remove(md5file)
    assert md5s('hello world ping') == 'b026324c6904b2a9cb4b88d6d61c81d1'

# Generated at 2022-06-13 16:17:48.179907
# Unit test for function md5s
def test_md5s():
    assert md5s('when in the course of human events') == 'c7e832ba5e5e5c25fbeb7d5c5f650b7c'


# Generated at 2022-06-13 16:17:54.267824
# Unit test for function md5
def test_md5():
    import os
    if not _md5:
        if os.environ.get('ANSIBLE_HASH_BEHAVIOUR', 'replace') == 'replace':
            return True  # Test should pass at this point
        else:
            raise AssertionError("MD5 not available.  Possibly running in FIPS mode")
    print("MD5:")
    print("Data:")
    sdata = "The quick brown fox jumped over the lazy dog."
    print("  '%s' -> %s" % (sdata, md5s(sdata)))
    sdata = "Abash'd the devil stood, and felt how awful goodness is."
    print("  '%s' -> %s" % (sdata, md5s(sdata)))
    sdata = "Imagination bodies forth the form of things unknown."

# Generated at 2022-06-13 16:17:59.196678
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s('hello world\n') == 'f2c7bb88b3102c1d9f91a9c8ba595c68'
    assert md5s('{"foo":1}') == '691bf2c2e7d19a59ed65ab7b35e6d470'

# Generated at 2022-06-13 16:18:09.258423
# Unit test for function checksum
def test_checksum():
    '''test checksum function'''

    CHECKSUM_TEST_DATA = 'The quick brown fox jumped over the lazy dog'

    if checksum_s(CHECKSUM_TEST_DATA) != '7c451fa91c602451d0a6b0f7e13e15b9dc7bb76f':
        raise Exception("secure_hash_s() failed unit test")

    CHECKSUM_TEST_FILE = '/tmp/ansible_test_checksum_file'
    with open(CHECKSUM_TEST_FILE, 'wb') as f:
        f.write(to_bytes(CHECKSUM_TEST_DATA, errors='surrogate_or_strict'))
    os.chmod(CHECKSUM_TEST_FILE, 0o644)


# Generated at 2022-06-13 16:18:15.508365
# Unit test for function md5
def test_md5():
    import tempfile

    tmp_handle, tmp_path = tempfile.mkstemp()
    # File exists
    assert md5(tmp_path) is not None

    # No file
    assert md5(tmp_path + 'foo') is None
    os.close(tmp_handle)
    os.remove(tmp_path)


# Generated at 2022-06-13 16:18:29.485870
# Unit test for function md5
def test_md5():
    """ make sure the md5 function works as expected """

    try:
        md5("/tmp/foo/bar")
    except ValueError as e:
        print("Caught expected ValueError: %s" % to_native(e))
    else:
        print("md5([invalid path]), expected ValueError, got None")

    res = md5("/bin/ls")
    if res != "9f79b08a53efa07c84b0130deb3d1c89":
        print("md5([valid path]), expected 9f79b08a53efa07c84b0130deb3d1c89, got %s" % res)

# Generated at 2022-06-13 16:18:37.193436
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import tempfile

    old_path = os.getcwd()

    tmp_dir = tempfile.mkdtemp()
    # Write some test data to a temporary file
    test_data = "foo"
    (fd, tmp_file) = tempfile.mkstemp()
    os.write(fd, test_data)
    os.close(fd)

    # Make sure none of the above steps errored
    assert(tmp_dir)
    assert(tmp_file)

    # Make sure we can find the test file we just created
    os.chdir(tmp_dir)
    assert(os.path.exists(tmp_file))

    # Run test
    output = md5(tmp_file)
    expected = md5s(test_data)

# Generated at 2022-06-13 16:18:40.617288
# Unit test for function md5
def test_md5():
    filename = 'test_get_checksum.txt'

    with open(filename, 'w') as f:
        f.write('this is a test')

    s = md5(filename)
    assert s == 'e80b5017098950fc58aad83c8c14978e'
    os.remove(filename)

# Generated at 2022-06-13 16:18:45.651857
# Unit test for function md5s
def test_md5s():
    ''' md5s() returns strings '''
    assert isinstance(md5s(''), str)
    assert isinstance(md5s('foo'), str)
    assert isinstance(md5s(u'foo'), str)



# Generated at 2022-06-13 16:18:48.066157
# Unit test for function md5s
def test_md5s():
    assert md5s('this is some crap') == 'ad2292b9a57af73264430b5ce5ddcf95'


# Generated at 2022-06-13 16:18:54.978490
# Unit test for function md5s
def test_md5s():
    # IMPORTANT:
    # The data must be consistent on all platforms and python versions
    # or the md5 sum will be different!
    data_to_hash = """Hello world, this data is consistent across all python versions on all linux platforms.
# This is a comment line which should be ignored
This is not a comment line.
Also not a comment: \\\\
# This is a comment line which should be ignored
"""
    assert md5s(data_to_hash) == '550a1e8f90a45b0c065f7c4e4db2f622'
    assert md5s(data_to_hash) == md5s(to_bytes(data_to_hash, errors='surrogate_or_strict'))

# Generated at 2022-06-13 16:19:01.498428
# Unit test for function md5
def test_md5():
    import tempfile
    tf = tempfile.NamedTemporaryFile()
    tf.write('foobar')
    tf.flush()
    tf.seek(0)
    assert md5(tf.name) == '3858f62230ac3c915f300c664312c63f'
    if _md5:
        assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'
    tf.close()


# Generated at 2022-06-13 16:19:05.319052
# Unit test for function md5s
def test_md5s():
    assert md5s(b'foobar') == '3858f62230ac3c915f300c664312c63f'


# Generated at 2022-06-13 16:19:08.842681
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"


# Generated at 2022-06-13 16:19:17.965349
# Unit test for function md5
def test_md5():

    p1 = '/etc/passwd'
    p2 = '/tmp/foo'
    p3 = '/tmp/bar'

    f1 = open(p2, 'w')
    f1.write('foo')
    f1.close()

    f2 = open(p3, 'w')
    f2.write('bar')
    f2.close()

    for (path, expected) in ((p1, '943a702d06f34599aee1f8da8ef9f729'),
                             (p2, 'acbd18db4cc2f85cedef654fccc4a4d8'),
                             (p3, '37b51d194a7513e45b56f6524f2d51f2')):

        test_val = md5(path)

# Generated at 2022-06-13 16:19:23.591525
# Unit test for function checksum
def test_checksum():

    # temp file for testing
    (handle, tmpfile) = tempfile.mkstemp()
    os.close(handle)

    try:
        # shouldn't be empty
        assert checksum(tmpfile) is not None
    finally:
        os.remove(tmpfile)

# Generated at 2022-06-13 16:19:31.198955
# Unit test for function md5
def test_md5():
    test_file = open("/tmp/test_md5", 'w+')
    test_file.write("this is a test")
    test_file.close()

    assert md5("/tmp/test_md5") == "8b1a9953c4611296a827abf8c47804d7"
    #assert md5("/tmp/test_md5") == "7bef57ec7f65c078e54bf8af7fa0631f"

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:19:34.318544
# Unit test for function md5s
def test_md5s():
    import base64
    md5_test = base64.b64decode('mF+n/Uzpu8hYdZqSe3TnCw==')
    assert(md5s('hello') == md5_test)


# Generated at 2022-06-13 16:19:39.208192
# Unit test for function checksum
def test_checksum():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils', 'checksum_test_file')
    hexdigest = 'f149e57fe9c7661477dcb5a5a5f5d5f5'
    assert checksum(filename) == hexdigest, "test_checksum function failed"
    print('test_checksum function passed')

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:19:46.907727
# Unit test for function md5s
def test_md5s():
    # Source: http://www.nsrl.nist.gov/testdata/
    #         "A Compilation of MD5 Test Vectors" by Chris Loomis
    _checksum = "8350e5a3e24c153df2275c9f80692773"
    assert md5s("") == _checksum

    _checksum = "32ec01ec4a6dac72c0ab96fb34c0b5d1"
    assert md5s("a") == _checksum

    _checksum = "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("abc") == _checksum

    _checksum = "0cc175b9c0f1b6a831c399e269772661"

# Generated at 2022-06-13 16:19:55.339395
# Unit test for function checksum
def test_checksum():
    ''' unit test for checksum.py '''

    import tempfile
    from ansible.compat.tests import unittest

    TEST_FILE = '''
hello world!
'''
    TEST_FILE_MD5 = '8f4d41988f4f9c9e9ef558646c19f5d5'
    TEST_FILE_SHA1 = '0a1b2c7fbe15e943a8ca44c27b42d7e5a5b691fb'

    class TestChecksum(unittest.TestCase):

        def setUp(self):
            self.test_file = tempfile.NamedTemporaryFile(delete=False)
            self.test_file.write(TEST_FILE)
            self.test_file.close()


# Generated at 2022-06-13 16:20:01.041919
# Unit test for function md5
def test_md5():
    '''
    test checksum to verify that it works like md5
    '''

    fd, path = tempfile.mkstemp(prefix='ansible_test_md5')
    try:
        os.write(fd, "abcdef")
    finally:
        os.close(fd)
    fd, path2 = tempfile.mkstemp(prefix='ansible_test_md5')
    try:
        os.write(fd, "abcdef")
    finally:
        os.close(fd)
    s = 'abcdef'
    assert (md5(path) == md5(path2))
    assert (md5s(s) == md5(path))
    os.unlink(path)
    os.unlink(path2)


# Generated at 2022-06-13 16:20:05.978569
# Unit test for function checksum
def test_checksum():
    import tempfile
    import os
    (handle, fname) = tempfile.mkstemp()
    f = os.fdopen(handle, 'w+')
    f.write("Hello world")
    f.close()
    chk = checksum(fname)
    os.unlink(fname)