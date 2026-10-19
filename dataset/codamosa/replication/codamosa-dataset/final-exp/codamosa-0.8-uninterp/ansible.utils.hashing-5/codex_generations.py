

# Generated at 2022-06-13 16:10:10.557313
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    teststring = "To be or not to be, that is the question"
    result = md5s(teststring)
    if result != "60ca1e8533ecfc51e0c18cb890a5174c":
        raise AssertionError("md5s() failed")


# Generated at 2022-06-13 16:10:21.448135
# Unit test for function md5
def test_md5():  # pragma: no cover
    '''
    verify that md5 hash checksums are generated correctly.
    '''
    import os.path
    import sys

    _test_file = '/tmp/z/a/b/c/d/e/f/a'
    _test_file_sum = '36e24c7ed8ce3dfe2a1e6e32d6c28734'
    _test_string = 'hello'
    _test_string_sum = '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:10:25.393754
# Unit test for function checksum
def test_checksum():
    ret1 = checksum('/bin/ls')
    ret2 = checksum('/bin/ls')
    if ret1 != ret2:
        raise ValueError('checksum failed')


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:10:28.007669
# Unit test for function checksum
def test_checksum():
    data = {"a": "b"}
    assert secure_hash_s(data) == '1e50210a0202497fb79bc38b6ade6c48fbc4f06f'

# Generated at 2022-06-13 16:10:33.207928
# Unit test for function md5
def test_md5():
    filename = os.path.basename(__file__)
    actual_filename = os.path.join(os.path.dirname(__file__), filename)
    md5sum = 'c14b75e731c3fafb8a34933ee73444d7'

    assert md5(actual_filename) == md5sum
    assert md5sum == md5(actual_filename)


# Generated at 2022-06-13 16:10:40.730731
# Unit test for function checksum
def test_checksum():
    ''' test_checksum
    Make sure the checksum() function is returning the same result
    in both Python 2 and 3.
    '''
    from ansible.module_utils._text import to_bytes
    assert to_bytes(checksum("hello", sha1)) == to_bytes("5d41402abc4b2a76b9719d911017c592")
    assert to_bytes(checksum_s("hello", sha1)) == to_bytes("5d41402abc4b2a76b9719d911017c592")

# Generated at 2022-06-13 16:10:45.175272
# Unit test for function md5s
def test_md5s():
    # md5s - md5 of python string
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"
    # md5 - md5 of local file
    assert md5("ansible/module_utils/hashing.py") == "b8c723eadfba58f263c8313ea0d67b91"



# Generated at 2022-06-13 16:10:47.287547
# Unit test for function md5s
def test_md5s():
    r = md5s(b"hello")
    assert r == "5d41402abc4b2a76b9719d911017c592"


# Generated at 2022-06-13 16:10:51.804254
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo') != '1cc2f85cedef654fccc4a4d8acbd18db' # noqa

# Generated at 2022-06-13 16:11:01.423479
# Unit test for function md5s
def test_md5s():
    expected_md5sum = 'be58f2b6cbbb6a9ac6d91c6e3da6a28e'
    #expected_md5sum = '5e543256c480ac577d30f76f9120eb74'
    input = "a test string"
    md5 = md5s(input)
    if md5 == expected_md5sum:
        print("MD5 checksum for '%s' is %s" % (input, md5))
    else:
        print("Error: expecting MD5 checksum for '%s' to be %s, got %s" % (input, expected_md5sum, md5))



# Generated at 2022-06-13 16:11:08.648584
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f"
    else:
        try:
            md5s("foobar")
            assert False, "Expected md5 not available in FIPS mode error"
        except ValueError:
            pass



# Generated at 2022-06-13 16:11:16.113779
# Unit test for function md5
def test_md5():

    import pytest
    import tempfile
    from ansible.module_utils.urls import open_url

    def md5_sum_is_present(fn):
        with open_url('http://www.mirrorservice.org/sites/ftp.openbsd.org/pub/OpenBSD/6.1/md5.txt') as f:
            for line in f.readlines():
                m = line.decode('utf-8').split()[0]
                if m == fn:
                    return True
        return False


# Generated at 2022-06-13 16:11:26.136741
# Unit test for function md5
def test_md5():
    local_file = 'test/test-data/test-hash.txt'

    # the actual MD5 of test-hash.txt
    md5_expected = 'b72f1bac4a80a0d3da20e0c4a4a7d8a4'

    # should be the same as in ShellModule.checksum() method
    md5_result = md5(local_file)
    assert md5_expected == md5_result
    md5_result = md5s('test')
    assert '098f6bcd4621d373cade4e832627b4f6' == md5_result

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:32.412483
# Unit test for function md5
def test_md5():
    value = 'a value'

    # Calling method directly not to bypass checks for FIPS-140-2 mode
    import hashlib
    if not hashlib.md5:
        raise RuntimeError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s(value) == hashlib.md5(value.encode('utf-8')).hexdigest()

# Generated at 2022-06-13 16:11:35.498821
# Unit test for function md5s
def test_md5s():
    md5 = md5s('testing')
    assert md5 == 'ae2b1fca515949e5d54fb22b8ed95575'


# Generated at 2022-06-13 16:11:44.240888
# Unit test for function checksum
def test_checksum():
    from ansible.playbook.play_tests import module_loader

    TestMD5 = module_loader.get_module_class('checksum')
    test_md5_obj = TestMD5.load({'path': os.path.realpath(__file__)})
    result = test_md5_obj.run()
    assert result.get('md5') == md5(os.path.realpath(__file__))
    assert result.get('sha1') == secure_hash(os.path.realpath(__file__))
    assert result.get('checksum') == result.get('sha1')

    # Test with some bad input and see if it fails
    # As we have already tested that these functions work
    # We are just doing basic test to prove that these functions
    # do work

# Generated at 2022-06-13 16:11:46.548962
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:11:52.604228
# Unit test for function md5
def test_md5():
    myfile = open("testfile", "w")
    myfile.write("this is a test")
    myfile.close()
    assert md5("testfile") == '7a65f6b23a53f82ca5c5dd5e5a99f9d7'


# Generated at 2022-06-13 16:11:54.972407
# Unit test for function md5s
def test_md5s():
    result = md5s('TestString')
    assert result == '4124bc0a9335c27f086f24ba207a4912'

# Generated at 2022-06-13 16:12:00.210994
# Unit test for function md5s
def test_md5s():
    # The test vector of http://www.faqs.org/rfcs/rfc2202.html
    in_str='Hi There'
    out_str='9294727a3638bb1c13f48ef8158bfc9d'
    assert md5s(in_str) == out_str

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:12:06.615815
# Unit test for function md5
def test_md5():
    path=os.path.dirname(os.path.realpath(__file__))
    filename=os.path.join(path,'checkmodule.py')
    assert checksum(filename) == checksum(filename)

# Generated at 2022-06-13 16:12:10.898917
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    else:
        try:
            md5s('')
            assert False
        except ValueError as e:
            assert 'not available' in to_bytes(e)

# Generated at 2022-06-13 16:12:17.912587
# Unit test for function md5s
def test_md5s():
    """
    Unit test for function md5s
    """
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    h1 = b'md5s'
    md5s_h1 = md5s(h1)
    assert md5s_h1 == 'c0d9f9ebad1c3b3fbdf7b6be0b6f0b6c'

    h2 = b'md5s\n'
    md5s_h2 = md5s(h2)
    assert md5s_h2 == 'b9fb5c38e5a5a5a5a5a5a5a5a5a5a5a5'

    h3 = u'md5s\n'
    md5s_h3 = md5s(h3)


# Generated at 2022-06-13 16:12:26.793499
# Unit test for function checksum
def test_checksum():
    TEST_STRING = 'abc'
    TEST_STRING_RESULT = 'a9993e364706816aba3e25717850c26c9cd0d89d'
    TEST_FILE = 'test/module_utils/basic'
    TEST_FILE_RESULT = '2f7e10d5ad5b81438b7542efd7be9a1a'
    TEST_FILE_BIG_RESULT = 'fd2c45b3fdc3e3a9a711eec5f75f8a2c'

    if not os.path.exists(TEST_FILE):
        print("creating test file")
        os.system("echo -n 'abc' > '%s'" % TEST_FILE)

    assert checksum(TEST_FILE) == TEST_FILE_RESULT

# Generated at 2022-06-13 16:12:31.053248
# Unit test for function md5
def test_md5():
    m = md5s('Foo')
    assert(m == "acbd18db4cc2f85cedef654fccc4a4d8")



# Generated at 2022-06-13 16:12:34.550331
# Unit test for function md5s
def test_md5s():
    assert('f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0' == md5s('foobar'))


# Generated at 2022-06-13 16:12:45.604127
# Unit test for function checksum
def test_checksum():
    checksum_file = 'test/test_checksum.txt'
    assert checksum(checksum_file) == 'd78c6db8e7d2a783a983d939ca0001dd'
    assert checksum_s('') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    #assert checksum_s(u'this is a text') == 'a9fa2fea876d5e5d5b5c5f5e5155f20f'
    assert md5(checksum_file) == '8b1a9953c4611296a827abf8c47804d7'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'

# Generated at 2022-06-13 16:12:56.252513
# Unit test for function md5
def test_md5():
    '''
    This should probably be moved to a unit test, but we don't have a unit
    test framework yet.  You can test this function by running it like:

    $ ansible/hacking/test-module -m util_tools.test_md5

    This requires the 'test' module be in your configured library path, which
    defaults to /usr/share/ansible
    '''
    module = AnsibleModule({'param': 'string'}, check_invalid_arguments=False)

    actual = md5s("string")
    expected = "a8d14c3bcebf0c0f67242e6d45d1e2e6"

# Generated at 2022-06-13 16:12:59.083611
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == 'f5d5d5c5e5ccb2c724ed1d8f5f83b0f2'



# Generated at 2022-06-13 16:13:05.380745
# Unit test for function md5s
def test_md5s():
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("Hello") == "8b1a9953c4611296a827abf8c47804d7"
    assert md5s("Hello World") == "65a8e27d8879283831b664bd8b7f0ad4"
    assert md5s("007") == "e5c5a98d5c5a98d5c5a98d5c5a98d5c5"
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"

# Generated at 2022-06-13 16:13:12.243950
# Unit test for function md5s
def test_md5s():
    import os
    md5s_data=md5s(b"123")
    md5s_data_1=md5s(b"1234")
    if md5s_data==md5s_data_1:
        return 0
    else:
        return 1


# Generated at 2022-06-13 16:13:18.387168
# Unit test for function md5
def test_md5():
    assert secure_hash('/etc/passwd') == secure_hash('/etc/passwd', _md5)
    assert secure_hash('/etc/shadow') == secure_hash('/etc/shadow', _md5)
    assert secure_hash_s('hello world') == secure_hash_s('hello world', _md5)
    assert secure_hash_s('hello world!') == secure_hash_s('hello world!', _md5)


# Generated at 2022-06-13 16:13:25.098859
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert os.path.exists(__file__)
    assert md5(__file__) == 'e6c5a6fdb8c9b14067af74a262ad0a7a'

# Generated at 2022-06-13 16:13:27.034339
# Unit test for function md5
def test_md5():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:13:29.076519
# Unit test for function md5
def test_md5():
    md5_1 = md5s('hello')
    assert md5_1 == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:13:37.404423
# Unit test for function checksum
def test_checksum():
    # Test if checksum returns a hash string
    import os
    import platform

    if platform.system() != 'Darwin':
        # (cpaulik) skipping this test on MacOSX as /bin/sh is linked to bash
        # and complains about the use of undefined variables in the heredoc
        script_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'utils', 'test_checksum.sh')
        rc, out, err = module_common.run_command(script_file)
        assert rc == 0
        out = out.strip()
        assert out

# Generated at 2022-06-13 16:13:48.381817
# Unit test for function checksum
def test_checksum():
    '''
    Ansible module function checksum unit test
    '''
    from ansible.module_utils import basic

    f = open("/etc/fstab","r")
    s = f.read()
    f.close()

    data = basic.AnsibleModule(
        argument_spec = dict(
            data=dict(default=None, type='str'),
            path=dict(default=None, type='str'),
            hash=dict(default='sha1', type='str'),
        ),

    ).check_mode
    data = dict(data=s, path=filename, hash='sha1',)

    c = checksum(filename)
    print("==> md5(%s) = %s" % (filename, c))

    c = checksum_s(s)

# Generated at 2022-06-13 16:13:57.932705
# Unit test for function checksum
def test_checksum():
    for func in ('sha1', 'sha1sum'):
        try:
            from hashlib import sha1 as sha1sum
        except ImportError:
            from sha import sha as sha1sum
        sha1sum_s = secure_hash_s
        sha1sum = secure_hash
        assert(func == 'sha1')

    test_file = 'lib/ansible/modules/system/copy.py'
    assert(checksum(test_file) == sha1sum(test_file))
    assert(checksum_s('test string') == sha1sum_s('test string'))

    # test backwards compat with md5
    test_file = 'lib/ansible/modules/system/copy.py'
    assert(md5(test_file) == checksum(test_file))


# Generated at 2022-06-13 16:14:02.336711
# Unit test for function md5
def test_md5():
    try:
        secure_hash_s('test', _md5)
    except:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

# Generated at 2022-06-13 16:14:05.210068
# Unit test for function md5
def test_md5():
    assert md5("/bin/ls") == "5ee6c0a6dffa6fce9c9d7ac2b07e1b07"

# Generated at 2022-06-13 16:14:13.839814
# Unit test for function md5s
def test_md5s():
    # Note, sha1 is the only hash algorithm compatible with python2.4 and with
    # FIPS-140 mode (as of 11-2014)
    from ansible.utils.hashing import md5s

    assert (md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8')
    assert (md5s('bar') == '37b51d194a7513e45b56f6524f2d51f2')

# Generated at 2022-06-13 16:14:18.811678
# Unit test for function md5
def test_md5():
    ''' test md5() http://www.python.org/dev/peps/pep-0276/'''
    import tempfile
    fd, fname = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('1234')
    f.close()
    assert md5(fname) == '81dc9bdb52d04dc20036dbd8313ed055'
    os.unlink(fname)

# Generated at 2022-06-13 16:14:23.635164
# Unit test for function checksum
def test_checksum():
    test_name = "checksum"
    test_file = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + os.path.sep + "test" + os.path.sep + "test.yml"
    expected = "1c6feca73a422f0a0f750e389169ff21c3d8cebf"
    actual = checksum(test_file)
    assert expected == actual
    print(test_name + " Test PASS")


# Generated at 2022-06-13 16:14:28.859759
# Unit test for function md5
def test_md5():
    with open("test-file", "w") as f:
        f.write("test file")
    result = md5("test-file")
    assert result == "be9ac79dcfc1b6d1c620105b638228f6"
    os.remove("test-file")


# Generated at 2022-06-13 16:14:32.531764
# Unit test for function md5s
def test_md5s():
    # sha1 hash for ansible
    expected = 'beb25b5d5ea31ce1d2f9dc0daf7ea6f7f8a2ca01'
    computed = md5s('ansible')
    assert computed == expected


# Generated at 2022-06-13 16:14:36.591226
# Unit test for function md5
def test_md5():
    test_input = "Hello World"
    test_output = "b10a8db164e0754105b7a99be72e3fe5"
    
    assert md5s(test_input) == test_output

# Generated at 2022-06-13 16:14:44.985942
# Unit test for function checksum
def test_checksum():
    sample_data = "sample text\n"
    sample_sha1 = 'ad4419a81009b9ff7fbd65d2e0fb8562c2e81ea4'
    assert secure_hash_s(sample_data) == sample_sha1
    assert secure_hash_s(sample_data) == checksum_s(sample_data)

    # md5 is not available in FIPS-140 mode
    if _md5:
        sample_md5 = "e8dc4081b13434b45189a720b77b6818"
        assert md5s(sample_data) == sample_md5

# Generated at 2022-06-13 16:14:54.545542
# Unit test for function md5
def test_md5():
    import tempfile

    tempfh, tempfn = tempfile.mkstemp()
    try:
        import shutil
        shutil.copyfile('test/ansible/module_utils/basic.py', tempfn)
        assert md5(tempfn) == 'c1e52fb7f5f3e5b7e5b5f37a6a57d2c3'
        assert md5s('bogus') == '3b5f7b0c5a5e7d0cacbb5f7b5c5f7d9c'
    finally:
        os.close(tempfh)
        os.remove(tempfn)

# Generated at 2022-06-13 16:15:02.154490
# Unit test for function md5
def test_md5():
    ''' md5 test '''
    from ansible.utils.encrypt import decrypt_text

    assert md5('lib/ansible/module_utils/basic.py') == 'e874f4e1b1a35d7a9a0f9ed9a3a2f3c3'
    assert md5s(u'\u9234') == '2bb2e9b9f6989e10f7c1e106b8d7e351'
    assert decrypt_text(u'$1$V0xeFpNe$cG7EuLukjbVhctzZ/HXZr0', 'ansible', 'md5crypt') == u'foo'



# Generated at 2022-06-13 16:15:04.839773
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/passwd') == "c65bd15e7ae2c1347583aa02d76bf357"



# Generated at 2022-06-13 16:15:12.628850
# Unit test for function md5
def test_md5():

    # The output of this function is not constant across python implementations
    # So we test it with the output of a known implementation for comparison
    if md5("ansible/module_utils/basic.py") != "7f70a65a76e7b3fab3c3ab7ea2e9b54d":
        raise AssertionError("md5 returns incorrect value")

    if md5s("foo") != "acbd18db4cc2f85cedef654fccc4a4d8":
        raise AssertionError("md5s returns incorrect value")

# Generated at 2022-06-13 16:15:16.161122
# Unit test for function md5s
def test_md5s():
    '''md5 test'''
    s = 'test'
    m = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    assert md5s(s) == m


# Generated at 2022-06-13 16:15:22.605025
# Unit test for function checksum
def test_checksum():
    data = "secret"
    assert(checksum_s(data) == "5ebe2294ecd0e0f08eab7690d2a6ee69")
    assert(checksum(os.devnull) == "d41d8cd98f00b204e9800998ecf8427e")

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:15:24.868734
# Unit test for function md5
def test_md5():
    data = "hello world"
    assert md5s(data) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5(__file__) == '9dc068d626e8b990db52f98abf7f2e1b'


# Generated at 2022-06-13 16:15:28.414558
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:15:32.379386
# Unit test for function checksum
def test_checksum():
    assert checksum('lib/ansible/modules/core/cloud/rackspace/rax.py') == '7acafd9149c876ceb1d0cdda2f5a08f8134e8849'


# Generated at 2022-06-13 16:15:34.595060
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:15:37.557583
# Unit test for function md5s
def test_md5s():
    md5s_data = md5s('hello')
    assert md5s_data == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:15:45.274608
# Unit test for function md5
def test_md5():
    '''Unit test for md5'''
    import os
    import tempfile

    fd, tmppath = tempfile.mkstemp(text=True)
    with os.fdopen(fd, 'a') as f:
        f.write('hello')

    try:
        assert md5(tmppath) == '5d41402abc4b2a76b9719d911017c592'
    finally:
        os.remove(tmppath)

# Generated at 2022-06-13 16:15:49.135569
# Unit test for function md5s
def test_md5s():
    if check_md5_available():
        assert md5s("http://docs.ansible.com/ansible")=="d94a8b657950b86c22a7d0c71ab8e7bb"
    else:
        print("Running in FIPS mode - md5 not available")


# Generated at 2022-06-13 16:16:00.768809
# Unit test for function md5
def test_md5():
    ''' md5 should return the same value as md5sum if available '''
    return_value = []
    try:
        import subprocess
        import tempfile
    except ImportError:
        return_value = ['unable to import subprocess or tempfile']

    filename = tempfile.NamedTemporaryFile()
    # Write data to the file
    filename.write('hello world')
    filename.flush()
    # Calculate the MD5 hash
    # Note this doesn't actually test random files as it uses a static string
    filename_hash = md5(filename.name)
    # Use md5sum to calculate the hash

# Generated at 2022-06-13 16:16:03.903352
# Unit test for function md5s
def test_md5s():
    data = "foo"
    expected_result = "acbd18db4cc2f85cedef654fccc4a4d8"
    computed_result = md5s(data)
    assert(computed_result == expected_result)


# Generated at 2022-06-13 16:16:13.785920
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, sentinel

    def _md5_init_mock_return(orig_init):
        def _md5_init_mock(self):
            self.hexdigest = sentinel.hexdigest
            orig_init(self)
        return _md5_init_mock

    def _md5_mock_return(orig_md5):
        class _md5_mock(object):
            digest = sentinel.digest
            def __init__(self):
                orig_md5.__init__(self)
                self.update = sentinel.update
        _md5_mock.__init__ = _md5_init_mock_return(orig_md5.__init__)

# Generated at 2022-06-13 16:16:23.769959
# Unit test for function md5
def test_md5():
    # test_md5s
    hash_func = md5s
    assert hash_func("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert hash_func(" ") == "7215ee9c7d9dc229d2921a40e899ec5f"
    assert hash_func("abcd") == "e2fc714c4727ee9395f324cd2e7f331f"
    assert hash_func("abcd ") == "9f4ee4b3ff141ea22310f858d72cbf76"
    assert hash_func("abcd e") == "6eafb6cfa277c7d8859298ef844c3249"

# Generated at 2022-06-13 16:16:30.486889
# Unit test for function md5
def test_md5():
    # the data used to test this function
    data = "Hello World"

    # test md5s
    expected_md5 = "b10a8db164e0754105b7a99be72e3fe5"
    calculated_md5 = md5s(data)
    assert(calculated_md5 == expected_md5)

    # test md5
    expected_md5 = "ed076287532e86365e841e92bfc50d8c"
    calculated_md5 = md5(__file__)
    assert(calculated_md5 == expected_md5)

# Generated at 2022-06-13 16:16:39.017292
# Unit test for function md5s
def test_md5s():
    assert(md5s('teststring') == '8db2f0c2b77480064662d8aca8b82b3b')
    # This sort of hardcoded test is not great. But it is simple to work with.
    # We might have a better idea in the future. Possibly use strace to see
    # what is really happening in the code.
    #
    # Trying to use a function to generate this string is not good because we
    # can't be sure what the hash will be after upgrading or changing the
    # version of hashlib.
    assert(md5s('example/files/test_module.py') == '4afb4da107a2e5866f02c2d38534b67a')


if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:16:42.258733
# Unit test for function md5
def test_md5():
    try:
        assert md5("/etc/passwd") == "2d711642b726b04401627ca9fbac32f5"
    except ValueError:
        pass

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:47.372674
# Unit test for function md5s
def test_md5s():
    '''Unit test for md5s'''
    if not _md5:
        return

    h1 = md5s('')
    h2 = md5s('The quick brown fox jumped over the lazy dog')
    h3 = md5s('The quick brown fox jumped over the lazy dog.')
    h4 = md5s('The quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dog')

    assert h1 == 'd41d8cd98f00b204e9800998ecf8427e'
    assert h2 == '9e107d9d372bb6826bd81d3542a419d6'
    assert h3 == 'e4d909c290d0fb1ca068ffaddf22cbd0'

# Generated at 2022-06-13 16:16:54.886021
# Unit test for function md5
def test_md5():
    import tempfile
    import json

    filename = tempfile.mktemp()
    text = '#!/bin/sh\n\necho "The $WORD is $COLOR"'
    with open(filename, 'w') as f:
        f.write(text)

    assert md5(filename) == secure_hash(filename, _md5)
    assert secure_hash(filename) != secure_hash(filename, _md5)

    # hash of a json-dumped dictionary
    data = {'one': 'two'}
    assert md5s(json.dumps(data)) == secure_hash_s(json.dumps(data), _md5)
    assert secure_hash_s(json.dumps(data)) != secure_hash_s(json.dumps(data), _md5)

# Generated at 2022-06-13 16:16:59.470453
# Unit test for function checksum
def test_checksum():
    h = secure_hash_s('test')
    # The below test is not guaranteed to work forever, but it seems unlikely
    # to fail on sha1 any time soon.
    assert h == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

# Generated at 2022-06-13 16:17:11.723783
# Unit test for function checksum
def test_checksum():
    from tempfile import NamedTemporaryFile

    def fail_checksum(filename, hash_string, func):
        print("%s %s %s" % (filename, hash_string, func.__name__))
        assert func(filename) == hash_string

    f = NamedTemporaryFile()
    f.write(b"abcdef")
    f.flush()

    fail_checksum(__file__,
                  'edeca3b8e52c1d45cedd65ceba98a36a9b819e25',
                  checksum)

    fail_checksum(f.name,
                  '7e240de74fb1ed08fa08d38063f6a6a91462a815',
                  checksum)


# Generated at 2022-06-13 16:17:21.057489
# Unit test for function checksum
def test_checksum():
    import tempfile

    h1 = checksum("/bin/ls")
    h2 = checksum("/bin/ls")
    assert h1 == h2

    fd, fname = tempfile.mkstemp()
    try:
        os.write(fd, "hello world")
        os.close(fd)
        assert checksum(fname) == checksum("hello world")
        assert checksum("/bin/ls") != checksum("/bin/false")
    finally:
        os.unlink(fname)


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:17:24.785093
# Unit test for function md5s
def test_md5s():
    ''' md5s should return the md5 hash of the data '''
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:17:32.754387
# Unit test for function checksum
def test_checksum():
    '''
    sha1 of empty string is:
    da39a3ee5e6b4b0d3255bfef95601890afd80709
    '''

    MESSAGE = '''
    vserver!
    '''

    # Assert sha1 == sha1
    assert checksum_s(MESSAGE) == '7d50d8b580f14ab941e9fd57d0fb8fe77f8089cf'
    assert checksum_s(MESSAGE) == checksum_s(MESSAGE)

    # Assert sha1 != sha1
    assert checksum_s(MESSAGE) != checksum_s(MESSAGE + ' ')

    # Test the function with a file

# Generated at 2022-06-13 16:17:35.270128
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    valid_md5 = '2f1c6b5a6e1d6d5f28b17c6bff8ccc4f'
    assert valid_md5 == md5s('Hello World')


# Generated at 2022-06-13 16:17:43.067955
# Unit test for function md5s
def test_md5s():
    ''' test for function md5s '''
    data = 'This is some data for the md5 test.'
    md5_return = md5s(data)
    assert isinstance(md5_return, (str, unicode))
    assert len(md5_return) == 32
    assert md5_return == '17cd1bd3dc66284cd55d8d50c1fb9f63'


if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:17:51.101834
# Unit test for function md5
def test_md5():
    import tempfile
    # Create a new file in the system to compare md5 with
    filename = tempfile.mktemp()
    open(filename, 'w').close()
    # Calculate md5 for the new file
    expected_md5 = 'd41d8cd98f00b204e9800998ecf8427e'
    md5_result = md5(filename)
    # Check the result
    if md5_result != expected_md5:
        raise AnsibleError('md5() returned %s instead of %s' % (md5_result, expected_md5))
    else:
        # Clean up and print a success message
        os.unlink(filename)
        print('Success')


# Generated at 2022-06-13 16:17:58.383682
# Unit test for function md5
def test_md5():
    data = 'Hello ansible!'
    data_hash = '6daa3e3d67c8d1ffb53eafae6d7d6129'
    filename = 'filename'
    file_hash = '1e0f35955f950f2d6afea7f6879f87c9'

    assert md5s(data) == data_hash
    assert md5(filename) == file_hash


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:18:00.900261
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'

# Generated at 2022-06-13 16:18:04.365832
# Unit test for function md5s
def test_md5s():
    ''' This function will test the md5s function '''
    assert md5s("Hello World") == 'ed076287532e86365e841e92bfc50d8c'



# Generated at 2022-06-13 16:18:17.282575
# Unit test for function checksum
def test_checksum():
    data = b"Roses are red, violets are blue, sugar is sweet, and so are you!"
    assert checksum_s(data) == "ffc9e4f4a4e2a8e1bc80b2f66cc1a5fa6a834b61"
    assert checksum_s(b'', hash_func=_md5) == "d41d8cd98f00b204e9800998ecf8427e"


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:18:29.212105
# Unit test for function md5
def test_md5():
    '''
    checksum.test_md5()
    '''

    test_file = os.path.join(os.path.dirname(__file__), 'test_checksum.py')
    a0 = md5(test_file)
    a1 = md5s('slinging hash')
    a2 = md5(a2)
    assert(a0 == 'be93a6b9b7579cb1c0a711f34e324d5e')
    assert(a1 == '9a9779d5f543b0e4b2d2f0cdeacf1a8b')
    assert(a2 is None)

# Generated at 2022-06-13 16:18:36.488900
# Unit test for function md5s
def test_md5s():
    file = open('/tmp/ansible_test_md5s.txt','w')
    file.write('Ansible is the best')
    file.close()

    md5sum = md5s( 'Ansible is the best' )
    assert( md5sum == '9b8f2f49c6ef96bf1d77d594bfd8a844' )

    md5sum = md5s( open('/tmp/ansible_test_md5s.txt') )
    assert( md5sum == '9b8f2f49c6ef96bf1d77d594bfd8a844' )

    os.remove( '/tmp/ansible_test_md5s.txt' )


# Generated at 2022-06-13 16:18:38.995025
# Unit test for function md5s
def test_md5s():
    # Checksum of Test md5s result
    assert '2a0217c6905fe578de3936990e0e472b' == secure_hash_s('Test')


# Generated at 2022-06-13 16:18:43.120851
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:18:50.309229
# Unit test for function md5s
def test_md5s():
    ''' tests the md5s function against known results '''
    import unittest
    class TestMd5s(unittest.TestCase):
        '''Test md5s function'''

        def test_md5s(self):
            '''Test md5s function'''
            self.assertEqual(md5s("elvis:elvispw"), "eec1d35bf4be7b089c181fee4cc04cbb")

    unittest.main(argv=[''])

# Generated at 2022-06-13 16:18:53.640497
# Unit test for function md5s
def test_md5s():
    s = md5s("foo")
    assert s == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:19:00.428665
# Unit test for function md5
def test_md5():
    testfile = os.path.join(os.path.dirname(__file__), 'md5s.py')
    assert md5(testfile) == "1487b0c3b08d4219a52ec9b937c2e71e"
    assert md5s("abcd") == "e2fc714c4727ee9395f324cd2e7f331f"



# Generated at 2022-06-13 16:19:06.241288
# Unit test for function md5s
def test_md5s():
    import random
    import string

    for i in range(10):
        s = ''.join(random.choice(string.lowercase) for _ in range(1000))
        assert secure_hash_s(s, _md5) == md5s(s)


# Generated at 2022-06-13 16:19:12.497113
# Unit test for function md5s
def test_md5s():
    assert md5s(u'secure_hash_s(): ü') == u'db9745c9ec914f94e8f5e5cf543b35a6'
    assert md5s(u'secure_hash_s(): ü'.encode('utf-8')) == u'db9745c9ec914f94e8f5e5cf543b35a6'


# Generated at 2022-06-13 16:19:19.733919
# Unit test for function md5s
def test_md5s():
    """Generate a hash and compare it to the reference value"""
    string = b'something'
    assert md5s(string) == '9ac57ebc17d4b4e43b0f3b7c3be3d8de'


# Generated at 2022-06-13 16:19:26.007109
# Unit test for function checksum
def test_checksum():
    '''Unit test for function checksum'''
    import os
    import tempfile

    # Create temp file
    fd, test_file = tempfile.mkstemp()
    os.close(fd)
    os.remove(test_file)

    assert checksum(test_file) is None
    assert checksum_s("") == checksum("/dev/null")

    assert checksum(__file__) == checksum_s(open(__file__, 'rb').read())


# Generated at 2022-06-13 16:19:33.440157
# Unit test for function md5s
def test_md5s():
    import tempfile

    try:
        h = md5s('hello world')
    except ValueError as e:
        return

    fd, fn = tempfile.mkstemp()
    f = os.fdopen(fd, 'wb')
    f.write(b'foo bar')
    f.close()

    assert h == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5(fn) == '8843d7f92416211de9ebb963ff4ce28125932878'

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:19:37.609557
# Unit test for function md5
def test_md5():
    '''This is a test case for md5 function'''
    expected = '5ebe2294ecd0e0f08eab7690d2a6ee69'
    actual = md5('/tmp/test.txt')
    assert expected == actual, "Expected %s, but got %s" % (expected, actual)

# unit test for function md5s

# Generated at 2022-06-13 16:19:41.783923
# Unit test for function md5
def test_md5():

    h1 = md5("/etc/passwd")
    h2 = md5("/etc/shadow")

    assert h1 != h2
    assert isinstance(h1, basestring)

    h3 = md5s("hello")
    assert isinstance(h3, basestring)
    assert h3 != h2
    assert h3 != h1

# Generated at 2022-06-13 16:19:48.858192
# Unit test for function md5
def test_md5():
    test_md5_filename = "test/units/utils/md5_test"
    test_md5_hash = "f74fd47d1b8c0554e7144c947d9a9b8c"

    # Assert that an IOError is raised if the file does not exist
    try:
        md5("does/not/exist")
    except IOError:
        pass
    # Assert that an IOError is raised if the path is a directory
    try:
        md5("test/units/utils")
    except IOError:
        pass
    # Assert that the md5 hash of a file is returned if the file exists
    assert md5(test_md5_filename) == test_md5_hash
    # Assert that None is returned if the file does not exist

# Generated at 2022-06-13 16:19:53.414583
# Unit test for function md5
def test_md5():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5('test/test-data/test.cfg') == 'f8a8a50d682ee79a9a929f8c38aa6d58'

# Generated at 2022-06-13 16:19:56.289575
# Unit test for function md5s
def test_md5s():
    try:
        result = md5s('my-secret')
    except ValueError:
        result = 'not-available'
    assert result in ('48552fa2640ce7f2c6d2b7d49391258c', 'not-available')
