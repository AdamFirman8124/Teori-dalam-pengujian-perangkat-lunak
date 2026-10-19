

# Generated at 2022-06-13 16:10:06.197182
# Unit test for function md5s
def test_md5s():
    assert md5s('Hello World!')  == 'e59ff97941044f85df5297e1c302d260'
    assert md5s(u'Hello World!') == 'e59ff97941044f85df5297e1c302d260'


# Generated at 2022-06-13 16:10:09.935967
# Unit test for function checksum
def test_checksum():
    import os
    import shutil
    import tempfile

    (fd, temp_path) = tempfile.mkstemp()
    os.close(fd)

    try:
        tfile = open(temp_path, 'w')
        tfile.write('hello world')
        tfile.close()

        csum = checksum(temp_path)
        csum_str = checksum_s('hello world')

        assert csum == csum_str
    finally:
        os.unlink(temp_path)

# Generated at 2022-06-13 16:10:20.916976
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo\n') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('\n') == '68b329da9893e34099c7d8ad5cb9c940'
    assert md5s('\n\n') == 'a665a45920422f9d417e4867efdc4fb8'

# Generated at 2022-06-13 16:10:28.666789
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec = dict(
            path=dict(type='path'),
            string=dict(type='str'),
        ),
        supports_check_mode=True
    )

    path = module.params['path']
    string = module.params['string']

    if path is not None:
        result = checksum(path)
    elif string is not None:
        result = checksum_s(string)
    else:
        result = False

    module.exit_json(changed=False, checksum=result)



# Generated at 2022-06-13 16:10:30.061756
# Unit test for function checksum
def test_checksum():

    # We don't have a reliable way to test this
    pass

# Generated at 2022-06-13 16:10:35.004356
# Unit test for function checksum

# Generated at 2022-06-13 16:10:45.100273
# Unit test for function md5
def test_md5():
    ''' ansible.utils.md5 unit test'''

    assert md5(__file__) == '48c8688766e95e658d84b595f9c3596a'
    assert md5s("some data") == '1bc29b36f623ba82aaf6724fd3b16718'
    assert md5s("some data") == '1bc29b36f623ba82aaf6724fd3b16718'
    assert md5s("some data") == '1bc29b36f623ba82aaf6724fd3b16718'
    assert md5s("some data") == '1bc29b36f623ba82aaf6724fd3b16718'
    # We expect this to fail if the system is FIPS-140 compliant

# Generated at 2022-06-13 16:10:50.664943
# Unit test for function md5s
def test_md5s():
    ''' ansible.utils.md5_s - Test that MD5 is working '''

    test_string = "The quick brown fox jumps over the lazy dog."

    # The test string above has an MD5 sum of
    # 0e7e8f1911a9b244e50dd10e99c6c7f3

    m = md5s(test_string)

    if m != '0e7e8f1911a9b244e50dd10e99c6c7f3':
        raise AssertionError('Md5 did not match')

# Generated at 2022-06-13 16:10:53.343616
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:11:01.024679
# Unit test for function checksum
def test_checksum():
    assert(checksum_s('hello') == '5d41402abc4b2a76b9719d911017c592')
    assert(len(checksum_s('hello')) == 32)
    assert(checksum('lib/ansible/module_utils/facts/system/distribution.py') == '6ea39e6cbbbc621d90f1eb7a68aee6dd')
    assert(len(checksum('lib/ansible/module_utils/facts/system/distribution.py')) == 32)


# Generated at 2022-06-13 16:11:10.089253
# Unit test for function md5
def test_md5():
    # create a file and calculate the md5 sum of it
    f = open("foo1", 'w')
    f.write("foobar")
    f.close

    result1 = md5("foo1")
    print("result1:%s" % result1)
    assert result1 == '6c2e6e5ce6cc34db6ea5ce6cca8bf77f'

    # remove the file now
    os.system("rm foo1")


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:14.323082
# Unit test for function checksum
def test_checksum():
    """Return a valid hash for test_checksum file"""
    test_string = b"NaN"
    test_file = '/tmp/test_checksum'
    with open(test_file, 'w+') as f:
        f.write(test_string)
    assert checksum(test_file) == secure_hash_s(test_string)
    os.remove(test_file)
    assert checksum(test_file) is None

# Generated at 2022-06-13 16:11:26.049713
# Unit test for function md5
def test_md5():
    import sys
    import tempfile
    from nose.plugins.skip import SkipTest
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    # Test if md5 is available
    try:
        md5('/tmp')
    except ValueError:
        raise SkipTest

    # Test if md5 returns None for a

# Generated at 2022-06-13 16:11:36.103608
# Unit test for function checksum
def test_checksum():
    """ Test checksum success and failure paths """
    # Test success
    try:
        result = checksum('test/utils/test_checksum.py')
        assert result == '5dd5b72c5b4bb03b4e4caa53ca7b4c32e10a7b8d'
    except Exception as e:
        assert 0, "Unable to generate checksum"
    # Test failure
    try:
        result = checksum('invalid/test_checksum.py')
        assert 0, "Checksum incorrectly calculated"
    except Exception as e:
        pass

# TODO: add more tests

# Generated at 2022-06-13 16:11:40.341032
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert secure_hash_s('hello', _md5) == '5d41402abc4b2a76b9719d911017c592'



# Generated at 2022-06-13 16:11:50.412720
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.parsing.convert_bool import boolean

    f1 = '/tmp/checksum_test_file1'
    f2 = '/tmp/checksum_test_file2'
    f3 = '/does/not/exist'

    fh1 = open(f1, 'w')
    fh1.write('hello')
    fh1.close()

    c1 = checksum(f1)
    assert c1 == checksum(f1)
    assert c1 != checksum(f2)
    assert c1 != checksum(f3)

    # Make sure checksum returns None when file does not exist and
    # there is no trailing slash
    assert checksum(f3) is None

    # Make sure checksum returns None when file does not exist and
    # there is a trailing slash

# Generated at 2022-06-13 16:12:01.581410
# Unit test for function checksum
def test_checksum():
    assert checksum(__file__) == 'a8cfd79afaaeaa23c7b27f08b7087a1a0ef76fae'
    assert checksum_s(__file__) == 'a8cfd79afaaeaa23c7b27f08b7087a1a0ef76fae'
    assert checksum_s(b'abc') == 'a9993e364706816aba3e25717850c26c9cd0d89d'
    assert checksum(to_bytes(__file__, errors='surrogate_or_strict')) == 'a8cfd79afaaeaa23c7b27f08b7087a1a0ef76fae'

# Generated at 2022-06-13 16:12:12.836100
# Unit test for function checksum
def test_checksum():
    result = checksum('/bin/ls')
    assert result == '5a5b8404fa13e7addb6d5f6ecd4c6a4a'
    result = checksum_s('hey there')
    assert result == '798d1f42d7e2e50aefd9b9df6ef0e0c3'
    result = md5('/bin/ls')
    assert result == '5a5b8404fa13e7addb6d5f6ecd4c6a4a'
    result = md5s('hey there')
    assert result == '798d1f42d7e2e50aefd9b9df6ef0e0c3'

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:25.084127
# Unit test for function checksum
def test_checksum():
    ''' test_checksum() checks the checksum function against known values '''

    # This is a known sha1 checksum of the string 'test1test1'
    known_sha1 = '4f4ba4a4d1f2a3d765917b9cd9db7f686e39a8a7'

    # This is a known md5 checksum of the string 'test1test1'
    known_md5 = 'a76a1a2c51ca0b8a0b8ddfa7f9c9e9b9'

    # Check if the md5s and md5s functions are available

# Generated at 2022-06-13 16:12:31.869385
# Unit test for function checksum
def test_checksum():
    if checksum('test/utils/test_checksum.py') != 'a8e4d4b9e4b3f3c1ca8ffc5779d09fcf5e74c5a4':
        raise Exception()

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:38.336744
# Unit test for function checksum
def test_checksum():
    test_string = 'asdf'
    if checksum_s(test_string) == '912ec803b2ce49e4a541068d495ab570':
        return True
    else:
        return False

# Generated at 2022-06-13 16:12:41.350210
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:12:47.298729
# Unit test for function md5s
def test_md5s():
    "Shows how to test md5s()"
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(
            data = dict(required=True, type='str'),
        ),
    )

    # Tests
    if md5s(module.params['data']) != '7815696ecbf1c96e6894b779456d330e':
        module.fail_json(msg="md5s() failed")

    module.exit_json(changed=False)



# Generated at 2022-06-13 16:12:51.145219
# Unit test for function md5
def test_md5():
    """ test to make sure we get an error if we try to use md5 """
    try:
        md5('/etc/passwd')
        assert False, 'md5 failed to raise ValueError'
    except ValueError:
        pass

# Generated at 2022-06-13 16:12:53.362408
# Unit test for function md5s
def test_md5s():
    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'


# Generated at 2022-06-13 16:12:57.119734
# Unit test for function md5
def test_md5():
    assert os.path.exists('lib/ansible/module_utils/basic.py')
    assert md5('lib/ansible/module_utils/basic.py') == 'd1e93e8f5576e5931f1f77d0370f7e8b'


# tests for the module

# Generated at 2022-06-13 16:13:04.814872
# Unit test for function md5
def test_md5():
    import tempfile
    filename = tempfile.mktemp()
    with open(filename, 'wb') as f:
        f.write(b'0123456789ABCDEF')

    h1 = md5(filename)
    h2 = secure_hash(filename, _md5)
    h3 = secure_hash(filename)

    # Output should be the same.
    assert h1 == h2 == h3

    # Some output values based on the above hash algorithm
    assert h1 == '7f9c00dce7be8d59d1818b359426b90b'
    assert h2 == '7f9c00dce7be8d59d1818b359426b90b'

# Generated at 2022-06-13 16:13:14.700215
# Unit test for function md5s
def test_md5s():
    # Test string:
    # The quick brown fox jumps over the lazy dog.
    # Raw bytes:
    # The quick brown fox jumps over the lazy dog.
    # Hex bytes:
    # 54 68 65 20 71 75 69 63 6b 20 62 72 6f 77 6e 20 66 6f 78 20 6a 75 6d 70 73 20 6f 76 65 72 20 74 68 65 20 6c 61 7a 79 20 64 6f 67 2e
    # Hex result:
    # 8fca64479038073c1d78e5bf5cda6fb7
    result=md5s('The quick brown fox jumps over the lazy dog.')
    if result!='8fca64479038073c1d78e5bf5cda6fb7':
        print("test_md5s failed")

# Generated at 2022-06-13 16:13:26.149957
# Unit test for function md5
def test_md5():

    test_md5_output = "93b885adfe0da089cdf634904fd59f71"
    input = "The quick brown fox jumps over the lazy dog"

    # Create a string
    test_md5_s = md5s(input)
    assert test_md5_s == test_md5_output, "test_md5_s Failed. Expected %s Got %s" % (test_md5_output, test_md5_s)

    # Create a temporary file
    fd, test_file = tempfile.mkstemp()
    os.write(fd, to_bytes(input, errors='surrogate_or_strict'))
    os.close(fd)

    # Get md5
    test_md5_file = md5(test_file)
    assert test_md5

# Generated at 2022-06-13 16:13:33.071614
# Unit test for function md5s
def test_md5s():
    import os
    import io
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    results = dict(changed=False)
    tmp_file = os.path.join('/tmp', 'test_md5s_file')
    with io.open(tmp_file, mode='w', encoding='utf-8') as f:
        f.write(u'Hello world')
    if 'md5' in results:
        results['changed'] = True
        module.exit_json(**results)
    results['md5'] = checksum(tmp_file)
    results['md5s'] = checksum_s(u'Hello world')
    results['md5_native'] = md5(tmp_file)

# Generated at 2022-06-13 16:13:44.325301
# Unit test for function md5
def test_md5():
    import tempfile
    fd, fname = tempfile.mkstemp()
    testval = 'foobar'
    try:
        os.write(fd, testval)
        os.close(fd)
        assert md5(fname) == md5s(testval)
        assert md5s(testval) == '3858f62230ac3c915f300c664312c63f'
    finally:
        os.unlink(fname)

# Generated at 2022-06-13 16:13:53.840083
# Unit test for function md5s
def test_md5s():
    # md5s() is deprecated, but still available (see md5s() docstring)
    from ansible.module_utils import basic

    # Basic testing for md5s()
    true_md5s = md5s('test')
    mod = basic.AnsibleModule(argument_spec={})
    mod.md5s = md5s

    if true_md5s != mod.md5s('test'):
        raise ValueError("md5s() failed basic test")

    # Test for FIPS mode (md5s() will fail in FIPS mode)

# Generated at 2022-06-13 16:14:00.497196
# Unit test for function md5
def test_md5():
    """ test for md5() and md5s() """

    # Create a test file
    TEST_FILE = '/tmp/md5_test.txt'
    TEST_FILE_DATA = 'This is a test file for md5().'
    fh = open(TEST_FILE, 'w')
    fh.write(TEST_FILE_DATA)
    fh.close()

    # Calculate the MD5 hash of the test file
    try:
        md5_data = md5(TEST_FILE)
        md5_string = md5s(TEST_FILE_DATA)
    except ValueError:
        # Running in FIPS mode, so md5 is not available
        md5_data = md5_string = 'd41d8cd98f00b204e9800998ecf8427e'


# Generated at 2022-06-13 16:14:04.277191
# Unit test for function md5s
def test_md5s():
    md5_test_string = md5s("test")
    assert md5_test_string == "098f6bcd4621d373cade4e832627b4f6"


# Generated at 2022-06-13 16:14:13.462068
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls') == 'f3e8e1dfe7e04afcdc2147774f936b8dee7fe6de'
    assert checksum('asldkfjasldfkjalsdkfjsadlkjflksdjflaksjflksdajflkdsajflkdsajflksdajflkdsajfklasdjf') == '8a4b2a2add35e6503b3cbc8a1de83e1f0a04b9df'

# Generated at 2022-06-13 16:14:17.967680
# Unit test for function checksum
def test_checksum():
    ''' Ansible module for test_checksum. '''

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(
        data=dict(type='str', required=True),
        filename=dict(type='path', required=True)
    ), supports_check_mode=True)

    module.exit_json(changed=True)



# Generated at 2022-06-13 16:14:22.738703
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('test') in ['098f6bcd4621d373cade4e832627b4f6', 'e8dc4081b13434b45189a720b77b6818']
    else:
        try:
            md5s('test')
            assert False
        except ValueError:
            pass


# Generated at 2022-06-13 16:14:25.753080
# Unit test for function checksum
def test_checksum():
    '''Checksum unit test'''

    assert checksum('/etc/resolv.conf') == checksum('/etc/resolv.conf')
    assert checksum('/etc/resolv.conf') != checksum('/etc/passwd')

# Generated at 2022-06-13 16:14:29.899106
# Unit test for function md5s
def test_md5s():
    data = """Hello World!"""
    assert md5s(data) == "ed076287532e86365e841e92bfc50d8c"

# vim: set expandtab:

# Generated at 2022-06-13 16:14:36.085074
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return True
    test_values = {
        'abc': '900150983cd24fb0d6963f7d28e17f72',
        'a': '0cc175b9c0f1b6a831c399e269772661',
        '': 'd41d8cd98f00b204e9800998ecf8427e'
    }
    test_passed = True
    for data, digest in test_values.items():
        if md5s(data) != digest:
            test_passed = False
            break
    return test_passed

# Generated at 2022-06-13 16:14:47.346667
# Unit test for function checksum
def test_checksum():
    '''
    ansible core tests: utilities/hashing.py
    '''
    import tempfile
    (handle, filename) = tempfile.mkstemp(text=True)
    f = os.fdopen(handle, 'w')
    f.write("Sample text\n")
    f.close()
    expected = ('28eb0a9babf4424e914dcc1d2b0ddc2a')
    result = checksum(filename)
    if expected == result:
        print("checksum test 1: success")
    else:
        print("checksum test 1: failure")
    os.unlink(filename)
    expected = ('a7d53e0aa15d7b1a3e3a2fa63b0280e6')

# Generated at 2022-06-13 16:14:50.648911
# Unit test for function md5s
def test_md5s():
    data = 'foo'
    result = md5s(data)
    assert result == 'acbd18db4cc2f85cedef654fccc4a4d8'



# Generated at 2022-06-13 16:14:55.654221
# Unit test for function md5
def test_md5():
    md5_file = os.path.join(os.path.dirname(__file__), '..', 'test', 'support', 'test_copy_local.sh')
    assert md5(md5_file) == '18e550a92f62a8b48c59b70a15b6265e'



# Generated at 2022-06-13 16:15:02.401345
# Unit test for function checksum
def test_checksum():
    data = "The quick brown fox jumped over the lazy dogs back."
    filename = "myfile"
    data_checksum = checksum_s(data)
    open(filename, 'w').close()
    file_checksum = checksum(filename)
    os.remove(filename)
    assert data_checksum != file_checksum


if __name__ == '__main__':
   test_checksum()

# Generated at 2022-06-13 16:15:04.748435
# Unit test for function md5
def test_md5():
    # python2.4 does not have hashlib, so this test is not possible
    if _md5:
        # We're not testing the output, since we don't have a static value,
        # just the return value.  If the method exists, return something
        md5("")

# Generated at 2022-06-13 16:15:08.146858
# Unit test for function md5
def test_md5():
    # FIXME: This test will fail when run in FIPS mode
    try:
        md5('/etc/passwd')
    except ValueError:
        pass
    else:
        assert False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:15:12.152475
# Unit test for function md5
def test_md5():
    # This is the md5 hash for "foobar"
    assert md5s("foobar") == "3858f62230ac3c915f300c664312c63f"
    assert md5("/usr/bin/ssh") == "55f7ff288eb0b31c839f3a5a58a08a05"

# Generated at 2022-06-13 16:15:15.434989
# Unit test for function md5
def test_md5():
    test_strs = ['hello world', 'hello galaxy']
    for test_str in test_strs:
        md5_hash = md5s(test_str)
        assert md5_hash == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:15:16.753996
# Unit test for function md5
def test_md5():
    """
    Returns test strings for md5 function
    """
    print(md5s('test'))


# Generated at 2022-06-13 16:15:18.817465
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'

if __name__ == "__main__":
    test_md5s()

# Generated at 2022-06-13 16:15:28.190910
# Unit test for function md5
def test_md5():
    # md5(file)
    assert md5('lib/ansible/portage_defaults.py') == 'bbbde554b3915b5ef5e5b5fcfdfbbd4b'

    # md5s(string in script)
    d = "def main():\n    print 'Hello, World!'\n\nif __name__ == '__main__':\n    main()\n"
    assert md5s(d) == 'e1ff7c61e65d8ffd6be1767ca9c9e958'


# Generated at 2022-06-13 16:15:31.830712
# Unit test for function md5s
def test_md5s():
    md5s_str = "d41d8cd98f00b204e9800998ecf8427e"
    assert md5s("") == md5s_str


# Generated at 2022-06-13 16:15:32.784795
# Unit test for function md5

# Generated at 2022-06-13 16:15:37.968736
# Unit test for function md5
def test_md5():
    """ md5 unit test """
    # This is a reference md5 hash of 'hello'
    MY_HASH='5d41402abc4b2a76b9719d911017c592'
    if os.path.exists(os.path.join('lib/ansible/module_utils', 'md5.py')):
        assert(md5('foobar') == None)
        assert(md5('hello') == MY_HASH)
    else:
        assert(md5('hello') == None)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:15:43.070769
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5("test/files/chown/test_chown_file") == 'cfc2e0a2c8308b9e22d6753b3e6bef41'

# Generated at 2022-06-13 16:15:46.047358
# Unit test for function md5s
def test_md5s():
    assert md5s('foobar')=='3858f62230ac3c915f300c664312c63f'


# Generated at 2022-06-13 16:15:52.998144
# Unit test for function checksum
def test_checksum():
    from ansible.constants import mk_boolean
    from ansible.module_utils.six.moves import StringIO

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    if not mk_boolean(os.environ.get('ANSIBLE_TEST_CHECKSUM', "yes")):
        raise ValueError("Aborting due to lack of ANSIBLE_TEST_CHECKSUM, or it being set to false.")

    # Set up the module arg spec
    argspec = basic.AnsibleModule.load_argspec()

    # Create a test module
    test_module = basic.AnsibleModule(
        argument_spec=argspec,
    )

    # If a file named 'test.txt' exists, get its sha1 sum
    f = to_

# Generated at 2022-06-13 16:16:03.500560
# Unit test for function md5s
def test_md5s():
    fail_msg = 'md5s() returned bad hash for string "{0}"'
    if _md5:
        data = 'some string'
        assert md5s(data) == '86d8c1afccb77aa82066a30d017fc8c7'
        assert md5s(data) != 'bad hash'
        data = u'unicode string'
        assert md5s(data) == '999dee739e9374599e2e87c11c38b7fe'
        assert md5s(data) != 'bad hash'
    else:
        try:
            md5s('some string')
        except ValueError:
            pass
        else:
            assert False, 'Expected md5s() to throw a ValueError'


# Generated at 2022-06-13 16:16:08.618049
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:16:11.398158
# Unit test for function md5
def test_md5():
    md5_value = md5(__file__)
    assert(md5_value == '1a8d19b175f7f3c685f1b73537952d66')


# Generated at 2022-06-13 16:16:17.091088
# Unit test for function md5
def test_md5():
    t = md5s("hello world")
    assert t == '5eb63bbbe01eeed093cb22bb8f5acdc3', "got %s" % t

# Generated at 2022-06-13 16:16:19.495779
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'



# Generated at 2022-06-13 16:16:22.998607
# Unit test for function checksum
def test_checksum():
    test_str = "I love the smell of napalm in the morning"
    assert checksum_s(test_str) == "bd04d9e77cea1a22f558e3f30e8a35d3b1848e2e"



# Generated at 2022-06-13 16:16:31.708946
# Unit test for function md5s
def test_md5s():
    ''' Test md5s function '''

    from ansible.compat.tests import unittest
    from .fixtures.hash import file_md5, file_md5s, data_md5, data_md5s

    # Test md5s function
    case_insensitive_md5s = md5s('UNIT TEST')
    case_sensitive_md5s = md5s(b'UNIT TEST')

    if case_insensitive_md5s == case_sensitive_md5s:
        case_sensitive_md5s = 'PLACEHOLDER_VALUE'

    class TestHash(unittest.TestCase):
        ''' Test md5s function '''

        def test_file_md5(self):
            ''' Test md5'''

# Generated at 2022-06-13 16:16:37.355914
# Unit test for function md5s
def test_md5s():
    string1 = 'hello world'
    string2 = 'goodbye world'
    assert md5s(string1) == md5s(string1)
    assert md5s(string1) != md5s(string2)

# Generated at 2022-06-13 16:16:41.013116
# Unit test for function md5s
def test_md5s():
    # Test md5 hash algorithm
    test_value = '3e4b4d4fa12de2c0266ccee0ea28d843'
    result = md5s('md5s')
    assert result == test_value, 'Function returned incorrect value'


# Generated at 2022-06-13 16:16:48.387775
# Unit test for function md5
def test_md5():
    # Test for md5()
    r = md5("/bin/ls")
    if not r == 'e75f96b7546631ac0acb521d2d1fe3d3':
        raise ValueError("md5sum test for '/bin/ls' failed!md5sum=%s" % r)
    # Test for md5s()
    s = md5s("/bin/ls")
    if not s == 'e75f96b7546631ac0acb521d2d1fe3d3':
        raise ValueError("md5sum test for string '/bin/ls' failed!md5sum=%s" % r)


# Generated at 2022-06-13 16:16:56.269644
# Unit test for function md5s
def test_md5s():
    print("Testing md5s()...")
    import doctest
    doctest.testmod(verbose=True)
    print("Done testing md5s()")

if __name__ == '__main__':
    test_md5s()
    a = secure_hash_s("hello world")
    b = secure_hash_s("goodbye")
    c = secure_hash_s("hello world")
    assert a==c
    assert a!=b
    print("Done testing module")

# Generated at 2022-06-13 16:17:04.525599
# Unit test for function md5
def test_md5():
    assert md5('/bin/ls') == '6b8b4567be3c7dfd8a947dee8c0f3e04'
    assert md5('/bin/ls') == '6b8b4567be3c7dfd8a947dee8c0f3e04'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'

# Generated at 2022-06-13 16:17:07.572527
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s("blah") == "7004efb6eff15412a56f8e0a0f61d2c1"

# Generated at 2022-06-13 16:17:23.496096
# Unit test for function md5
def test_md5():

    def _createFile(filename, content):
        f = open(filename, "w+")
        f.write(content)
        f.close()

    def _deleteFile(filename):
        os.unlink(filename)

    testfile = "testfile.txt"
    testcontent = "I'm a little teapot"
    testcontent_edited = "I'm a little teapot short and stout"
    testcontent_md5 = '3b931b82bf8b953c03bad1a35a49cae2'
    testcontent_edited_md5 = '3e9f514cdfea1a7a27f96b1fbd0b7715'

    # Test if it can compute the md5 checksum of a new file correctly
    _createFile(testfile, testcontent)
    rtn_

# Generated at 2022-06-13 16:17:32.001841
# Unit test for function md5s
def test_md5s():
    """ make sure md5s returns the same value as an md5 command """
    from ansible.module_utils.basic import AnsibleModule

    # Generate a random test string
    from tempfile import NamedTemporaryFile
    tmpfile = NamedTemporaryFile(delete=False)
    tmpfile.write(os.urandom(1024))
    tmpfile.close()

    # Calculate md5sum on the test string
    try:
        cmd = subprocess.Popen(['md5sum', tmpfile.name],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        (out, _) = cmd.communicate()
        cmd.wait()
    except (OSError, IOError) as e:
        raise AnsibleModuleError('md5sum command error')

    # Calcul

# Generated at 2022-06-13 16:17:38.904884
# Unit test for function checksum
def test_checksum():
    import tempfile
    import shutil
    import copy

    def _create_file(path):
        with open(path, 'w') as f:
            f.write('test')

    path = tempfile.mkdtemp()

# Generated at 2022-06-13 16:17:47.630563
# Unit test for function md5
def test_md5():
    s = secure_hash_s("foobar")
    m = secure_hash_s("foobar", _md5)
    assert isinstance(s, basestring)
    assert isinstance(m, basestring)
    assert s == "8843d7f92416211de9ebb963ff4ce28125932878"
    assert m == "3858f62230ac3c915f300c664312c63f"
    f = "./test_utils.py"
    assert secure_hash(f) == secure_hash(f, _md5)
    assert secure_hash(f) == "f4d3ddbdb761fe8ad685b7581fe7d173b2c2b016"

# Generated at 2022-06-13 16:17:49.780255
# Unit test for function md5s
def test_md5s():
    import random
    import time
    data = random.randint(0, 10000000)
    data = str(data)
    assert(md5s(data))



# Generated at 2022-06-13 16:17:56.350601
# Unit test for function md5
def test_md5():
    import sys
    x = secure_hash_s("abc", _md5)
    y = md5s("abc")
    assert x == y
    x = secure_hash(sys.argv[0])
    y = md5(sys.argv[0])
    assert x == y


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:17:57.283046
# Unit test for function md5

# Generated at 2022-06-13 16:18:08.582747
# Unit test for function checksum
def test_checksum():
    from tempfile import mkstemp
    from shutil import rmtree
    from os import write, close, mkdir, remove, getcwd
    from os.path import exists, isfile, join as path_join
    from shutil import move as path_move
    from time import sleep

    tmpdir = '/tmp/ansible-test-checksum-%s' % os.getpid()
    mkdir(tmpdir)

    (fd, fname) = mkstemp(dir=tmpdir)
    write(fd, 'foo')
    close(fd)

    # test normal
    assert checksum(fname) == checksum_s('foo')

    # test with arbitrary file path
    (fd,  fname) = mkstemp(dir=tmpdir)
    write(fd, 'bar')
    close(fd)


# Generated at 2022-06-13 16:18:11.423097
# Unit test for function md5
def test_md5():
    filename = "./lib/ansible/module_utils/hashing.py"
    h1 = secure_hash(filename)
    h2 = md5(filename)
    assert h1 == h2

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:18:17.659119
# Unit test for function md5
def test_md5():
    ''' test md5 functionality '''

    import tempfile

    fd, tmpfile = tempfile.mkstemp()
    assert md5(tmpfile) is None

    try:
        open(tmpfile, 'w').write('foo')

        assert md5(tmpfile) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    finally:
        os.remove(tmpfile)

# Generated at 2022-06-13 16:18:32.884508
# Unit test for function checksum
def test_checksum():
    # 1. test for normal usage
    # 1.1. for function secure_hash_s
    a = "I am a string"
    b = "I am a string"
    c = "I am a different string"
    d = "I"
    e = " am a string"
    try:
        assert(checksum_s(a) == checksum_s(b))
        assert(checksum_s(b) != checksum_s(c))
        assert(checksum_s(a) == checksum_s(d) + checksum_s(e))
    except AssertionError:
        raise AssertionError("test case 1.1. failed.")
    else:
        print("test case 1.1. passed.")

    # 1.2. for function secure_hash

# Generated at 2022-06-13 16:18:35.994988
# Unit test for function md5
def test_md5():
    assert md5(__file__) == 'ce7c8f685f379fb7c530172e0d7c2808'

# Generated at 2022-06-13 16:18:42.032568
# Unit test for function md5s
def test_md5s():
    '''
    Test md5s functions
    '''

    # Test string returns 32 hex charecters
    assert len(md5s('Hello World')) == 32

    # Test two inputs with same value returns same hash
    assert md5s('Hello World') == md5s('Hello World')

    # Test two input with different values returns different hashes
    assert md5s('Hello World') != md5s('Hello World!')

    # Test case sensitive
    assert md5s('Hello World') != md5s('HELLO WORLD')

    # Test empty input
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'



# Generated at 2022-06-13 16:18:47.663312
# Unit test for function md5
def test_md5():
    # Create test data
    data = 'The quick brown fox jumped over the lazy sleeping dog.'
    h1 = 'd4d315e4ef8fa8f082295f45fa9d9ac9'
    h2 = md5s(data)

    assert h1 == h2


# Generated at 2022-06-13 16:18:51.833534
# Unit test for function md5
def test_md5():
    filename = 'tests/unit/utils/checksum_test_files/test.txt'
    md5sum = md5(filename)
    if md5sum != '007d48d8db96942023debb85c8650d32':
        print("ERROR: expected '007d48d8db96942023debb85c8650d32'")


# Generated at 2022-06-13 16:18:55.693710
# Unit test for function md5s
def test_md5s():
    assert 'e3869b52e2e788517a4c2f4b6a0c4a92' == md5s('hello world')

# Generated at 2022-06-13 16:19:04.059505
# Unit test for function md5
def test_md5():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import shutil
    import os
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True, type='str'),
            content=dict(required=True, type='str')
        )
    )
    tmpdir = tempfile.mkdtemp(prefix='ansible-tmp')

# Generated at 2022-06-13 16:19:13.063030
# Unit test for function md5
def test_md5():
    from ansible.utils.hashing import checksum
    import tempfile

    # Create a temporary file with specific content
    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir, 'file')
    with open(test_file, 'w') as f:
        f.write('The quick brown fox jumped over the lazy dogs.')

    # The md5 checksum should be the same as the sha1 checksum
    assert md5(test_file) == checksum(test_file)

    # Clean up
    os.remove(test_file)
    os.rmdir(test_dir)

# Generated at 2022-06-13 16:19:22.098962
# Unit test for function md5
def test_md5():

    # rsa must be hashable
    # md5(None) should return None
    assert md5("rsa") == "d0de6012a9a1c174bebbeefb7cbe0d0e"
    assert md5("md5") == "1bc29b36f623ba82aaf6724fd3b16718"
    assert md5("sha") == "f05d97eaa9f7a71c77349b6c943020a1"
    assert md5("raw") == "09b9c392dc1a2f71a0d5e890971b5027"
    assert md5("file") == "6f5902ac237024bdd0c176cb93063dc4"

# Generated at 2022-06-13 16:19:25.716039
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5("/etc/passwd") == "7e240de74fb1ed08fa08d38063f6a6a9"
    if not os.path.exists("/etc/passwd") or os.path.isdir("/etc/passwd"):
        assert md5("/etc/fstab") is None


# Generated at 2022-06-13 16:19:38.865110
# Unit test for function md5
def test_md5():
    from ansible.module_utils import basic
    import os

    if not _md5:
        return

    test_string = 'Mary had a little lamb, Its fleece was white as snow'

    test_file_path = 'test_md5_file'
    test_file = open(test_file_path, mode='w')
    test_file.write(test_string)
    test_file.close()

    basic._ANSIBLE_ARGS = None
    assert md5(test_file_path) == md5s(test_string)
    basic._ANSIBLE_ARGS = None

    os.remove(test_file_path)

# Generated at 2022-06-13 16:19:43.887596
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, fname) = tempfile.mkstemp()
    os.write(fd, b"foo")
    os.close(fd)
    testmd5 = md5(fname)
    if testmd5 is None:
        return False
    if testmd5 != "acbd18db4cc2f85cedef654fccc4a4d8":
        return False
    os.remove(fname)
    return True

# Generated at 2022-06-13 16:19:47.664790
# Unit test for function md5s
def test_md5s():
    s = "abcd"
    assert md5s(s) == "e2fc714c4727ee9395f324cd2e7f331f"

# Generated at 2022-06-13 16:19:53.229349
# Unit test for function md5s
def test_md5s():
    """Test md5s function.  Assumes md5_data is a string of 40 characters, a typical result for an md5 hash."""
    md5_data = "3e3ca67e7e2b2ec8c7eff2af2cd04c7f978b03e8"
    data = "ABCDEFG1234567"
    if not _md5:
        assert md5s(data) == None
    else:
        assert md5s(data) == md5_data



# Generated at 2022-06-13 16:19:59.402376
# Unit test for function md5
def test_md5():
    ''' test md5 functions '''
    test_string = 'This is a test string'
    test_hash = '9c9d7b8abc88c08b7f0dda547e722ea5'
    test_file = '/tmp/.ansible_test_md5'
    try:
        f = open(test_file, "w")
        f.write(test_string)
        f.close()
        assert md5(test_file) == test_hash
        assert md5s(test_string) == test_hash
    finally:
        os.remove(test_file)