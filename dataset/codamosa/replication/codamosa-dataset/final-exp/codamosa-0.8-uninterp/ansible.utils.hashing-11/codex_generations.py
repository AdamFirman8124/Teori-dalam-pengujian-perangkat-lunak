

# Generated at 2022-06-13 16:10:10.805855
# Unit test for function md5
def test_md5():
    # Ensures that the md5 function works as expected.
    from ansible.module_utils._text import to_native
    import tempfile

    (fd, fname) = tempfile.mkstemp(text=False)
    result = None
    f = os.fdopen(fd, 'wb')
    try:
        f.write(b"This is a test")
        f.close()
        result = md5(fname)
    finally:
        os.remove(to_native(fname, errors='surrogate_or_strict'))
    assert(result == '0cbc6611f5540bd0809a388dc95a615b')


# Generated at 2022-06-13 16:10:19.211828
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.basic import AnsibleModule
    results = dict(changed=False, rc=0)
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            checksum_algorithm = dict(default='sha1', choices=['sha1', 'md5'])
        ),
        supports_check_mode = False,
    )
    results['checksum'] = getattr(checksum,'sha1')(module.params['path'])
    module.exit_json(**results)


# Generated at 2022-06-13 16:10:24.635964
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s('HELLO WORLD') == '7d793037a0760186574b0282f2f435e7'



# Generated at 2022-06-13 16:10:28.897566
# Unit test for function md5s
def test_md5s():
    ''' test md5s function '''
    import random
    result = {}
    for i in range(0, 1000):
        data = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(50)])
        result[md5s(data)] = data
    assert(len(result.keys()) == 1000)

# Generated at 2022-06-13 16:10:31.086110
# Unit test for function md5
def test_md5():
    a = md5('/etc/passwd')
    b = md5('/etc/shadow')
    assert a != b


# Generated at 2022-06-13 16:10:36.673873
# Unit test for function md5s
def test_md5s():
    ''' md5s function returns a string '''
    from ansible.module_utils import basic
    (rc, out, err) = basic.run_command('echo foo')
    assert isinstance(md5s(out), basestring)


# Generated at 2022-06-13 16:10:46.328253
# Unit test for function checksum
def test_checksum():
    ''' test_checksum:
        Unit test for checksum function.
    '''

    import os
    import tempfile
    import shutil
    import filecmp
    import sys

    # Create temporary working directory
    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    # Create a test file to checksum
    test_file = "test_file"
    test_file_path = os.path.join(test_dir, test_file)
    fd = open(test_file_path, 'w')
    print("This is a test.", file=fd)
    fd.close()
    
    # Expected hash of test file
    # This value is known to be correct for the above text given
    # the default block_size of 64*1024
    #   sha1

# Generated at 2022-06-13 16:10:48.011944
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:10:51.793521
# Unit test for function md5s
def test_md5s():
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write('abcdefg')
    hashsum = md5s(tmp.name)
    os.unlink(tmp.name)
    assert hashsum == '7ac66c0f148de9519b8bd264312c4d64'


# Generated at 2022-06-13 16:11:03.114419
# Unit test for function md5
def test_md5():
    assert secure_hash('/etc/passwd') == '91365e1ea19a7e80a0a3b7f3a3aeb873'
    assert secure_hash('/usr/share/dict/words') == 'af35bddf2b0438dcf8d7e9c90ba58e7d'
    assert secure_hash('olag') == 'cef9053c3c0d828c9f46a51ca55d89df'
    assert secure_hash('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert secure_hash('test/foobar') == 'cffa5f5a5b5207e8324e3c2a8e26a0e1'
    assert secure_hash('')

# Generated at 2022-06-13 16:11:09.625735
# Unit test for function md5
def test_md5():
    # verify that the sha1 and md5 work the same on the same string
    # which they should, since md5 is the first 16 bits of sha1
    assert md5s('hello') == secure_hash_s('hello', _md5).lower()
    assert md5('/bin/ls') == secure_hash('/bin/ls', _md5).lower()



# Generated at 2022-06-13 16:11:13.680263
# Unit test for function md5s
def test_md5s():
    def md5_check(data):
        import hashlib
        m = hashlib.md5()
        m.update(data)
        return m.hexdigest()
    test_str = "Hello World"
    ret = md5s(test_str)
    assert ret, md5_check(test_str)


# Generated at 2022-06-13 16:11:17.694874
# Unit test for function md5
def test_md5():
    if secure_hash('/etc/passwd') == md5('/etc/passwd'):
        return True
    else:
        return False

# The following functions are all deprecated in 2.3
from ansible.utils.hashing import hash_salt_and
from ansible.utils.hashing import hash_vault_salt
from ansible.utils.hashing import crypt

# Generated at 2022-06-13 16:11:19.798302
# Unit test for function md5s
def test_md5s():
    assert(md5s('hello') == '5d41402abc4b2a76b9719d911017c592')



# Generated at 2022-06-13 16:11:22.285345
# Unit test for function md5s
def test_md5s():
    assert md5s(u"foobar") == '3858f62230ac3c915f300c664312c63f'



# Generated at 2022-06-13 16:11:31.232945
# Unit test for function checksum
def test_checksum():
    """Unit test for checksum"""
    # content of test file
    data1 = '''
    #!/usr/bin/python
    print "hello world"
    '''
    data2 = '''
    #!/usr/bin/python
    print "hello world"
    '''
    data3 = '''
    #!/usr/bin/python
    print "hello world"
    print "test"
    '''
    # test if 2 files with same content have same file digest
    file1 = open('test1', 'w')
    file1.write(data1)
    file1.close()
    file2 = open('test2', 'w')
    file2.write(data2)
    file2.close()
    assert checksum('test1') == checksum('test2')

    # test if 2 files

# Generated at 2022-06-13 16:11:39.512871
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    correct_md5s = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
    test_md5s = md5s("test")
    assert correct_md5s == test_md5s, "test_md5s() failed"

# Generated at 2022-06-13 16:11:45.693092
# Unit test for function md5
def test_md5():
    fname = "test_md5_file"
    fdata = "this is a test file"
    fd = open(fname, "w")
    fd.write(fdata)
    fd.close()
    assert(md5(fname) == "5bd0f1d9c9f28fd9efc3d8f8ceef5c89")
    os.unlink(fname)

# Generated at 2022-06-13 16:11:49.557593
# Unit test for function md5
def test_md5():
    import tempfile
    with tempfile.NamedTemporaryFile() as test_file:
        test_file.write('test')
        test_file.flush()
        assert md5(test_file.name) == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:12:00.919348
# Unit test for function md5

# Generated at 2022-06-13 16:12:12.530990
# Unit test for function md5s
def test_md5s():

    from ansible.module_utils.six.moves.urllib.parse import urlparse
    from ansible.module_utils._text import to_bytes, to_text

    url = urlparse('http://www.python.org/')
    got = md5s(to_bytes(url.netloc))
    expected = '0a65b17eeae205e6f2e6d0b162f7ce3e'
    assert got == expected

    data = to_bytes('foo')
    got = md5s(data)
    expected = 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert got == expected

# Generated at 2022-06-13 16:12:14.229362
# Unit test for function md5
def test_md5():
    msg = 'test'
    assert md5s(msg) == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:12:17.013520
# Unit test for function md5s
def test_md5s():
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'



# Generated at 2022-06-13 16:12:20.358371
# Unit test for function md5s
def test_md5s():
    data = "abcdefg"
    result = md5s(data)
    assert result == "7ac66c0f148de9519b8bd264312c4d64"

# Generated at 2022-06-13 16:12:26.302505
# Unit test for function md5s
def test_md5s():
    ''' test_md5s '''
    assert md5s(b'string') == '25b7c51d7558e277c9d31a016125b1fa'
    assert md5s('string') == '25b7c51d7558e277c9d31a016125b1fa'

    # Unit test for function md5
    f = '/bin/ls'
    assert md5(f) == '5ca5f5aab33d8eb7fc6f19859b3a1b0f'

# Generated at 2022-06-13 16:12:32.586883
# Unit test for function md5
def test_md5():
    '''
    Test to see if the md5 function returns the correct value
    '''
    test_string = 'test123'
    assert md5s(test_string) == '57c3ac09e788c8db3a65eff5a5f5e5b5'


# Generated at 2022-06-13 16:12:39.384854
# Unit test for function checksum
def test_checksum():
    assert checksum('test/utils/test_checksum.py') == 'b4ec4b4eefce6eaccd7f9c6a9cc8f93b41f071e5'
    assert checksum('test/utils/test_checksum.py', sha1) == 'b4ec4b4eefce6eaccd7f9c6a9cc8f93b41f071e5'
    assert checksum('test/utils/test_checksum.py', md5) == 'c71e179933c9e0b0e06b00d63f4c17c4'


# Generated at 2022-06-13 16:12:41.830183
# Unit test for function md5s
def test_md5s():
    assert md5s('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'



# Generated at 2022-06-13 16:12:48.188483
# Unit test for function checksum
def test_checksum():
    this_dir, this_filename = os.path.split(__file__)
    test_file = os.path.join(this_dir, "../test/test_utils/test_utils.py")
    ref_checksum = "d446c3e3e0edc5b9a7a8e5adc0242e1f38772359"
    return_checksum = checksum(test_file)
    if ref_checksum != return_checksum:
        raise AssertionError("Checksum failed.\nExpected: %s\nReturned: %s" % (ref_checksum, return_checksum))


# Generated at 2022-06-13 16:12:57.952341
# Unit test for function md5
def test_md5():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, mock_open
    from ansible.module_utils._text import to_bytes

    if _md5:
        datadir = os.path.join(os.path.dirname(__file__), 'data')
        datafile = 'test_md5.txt'
        datapath = os.path.join(datadir, datafile)
        datahash = '0a9e0e68d087c7fae60a30ca92d7d0af'

        result = md5(datapath)
        assert result == datahash

        # Test that we can read a file opened in text mode
        data = 'some text'

# Generated at 2022-06-13 16:13:05.609377
# Unit test for function md5s
def test_md5s():
    ''' md5s() basic tests '''

    from ansible.module_utils.six import PY3

    if PY3:
        # Ensure that the error is raised for python3 to catch
        try:
            md5s('foo')
        except ValueError as e:
            error_message = e.args[0]
        else:
            error_message = None
        assert error_message == 'MD5 not available.  Possibly running in FIPS mode'
    else:
        assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:13:15.761235
# Unit test for function md5
def test_md5():
    from tempfile import NamedTemporaryFile
    s = 'nothing much to see here'
    nt = NamedTemporaryFile()
    nt.write(s)
    nt.flush()
    # We need to read the file name again because we are closing and reopening it.
    name = nt.name
    nt.close()
    digest = md5(name)
    print("test_md5: len(digest)=%d, digest=%s" % (len(digest), digest))
    assert(len(digest) == 32)
    assert(digest == '6bf33a6c8326b30fae6e3900b337dbb6')

# This is for backwards compatibility for modules that include md5s in their return values
#
# Example:
#  return {'file': filename,


# Generated at 2022-06-13 16:13:25.950448
# Unit test for function checksum
def test_checksum():

    data_filename = "data_filename"
    data_data = "data_data"
    data_filename_sha1 = "0f00d1b9e733c858bc12e3d7d3e883020f724f6f"
    data_data_sha1 = "0073da9b3bb7f3d796a11db7b337579080d47cc6"

    assert checksum(data_filename) == data_filename_sha1
    assert checksum_s(data_data) == data_data_sha1
    print("checksum_s(data_data): %s" % checksum_s(data_data))

test_checksum()

# Generated at 2022-06-13 16:13:30.158959
# Unit test for function md5
def test_md5():
    # we need to skip this test on OSX/FreeBSD and others which use libmd
    import platform
    if platform.system() in ['Darwin', 'FreeBSD'] and not hasattr(hashlib, 'algorithms_guaranteed'):
        raise SkipTest

    assert md5(__file__) == '57d9b4c4f8fa4d46aa7299dac3a05c88'

# Generated at 2022-06-13 16:13:33.617359
# Unit test for function md5s
def test_md5s():
    """ md5s should give well known answers """
    assert md5s("asdf") == "912ec803b2ce49e4a541068d495ab570"


# Generated at 2022-06-13 16:13:44.652906
# Unit test for function checksum
def test_checksum():
    assert(checksum_s('') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709')
    assert(checksum_s('12345') == '8cb2237d0679ca88db6464eac60da96345513964')
    assert(checksum('CHANGELOG') == '28b7bf5b86f5d5ad5e27c52380bbf77e04d7dce1')
    assert(checksum('test/test_utils.py') == 'b0ac194c2bd504d0d6c2f06b897e5f9d9a737b9e')

# Generated at 2022-06-13 16:13:46.947475
# Unit test for function checksum
def test_checksum():
    assert checksum('/etc/hosts') == secure_hash('/etc/hosts')
    assert checksum_s('hello') == secure_hash_s('hello')

# Generated at 2022-06-13 16:13:49.720278
# Unit test for function md5s
def test_md5s():
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:13:54.582149
# Unit test for function checksum
def test_checksum():
    if not checksum("lib/ansible/module_utils/basic.py") == "1e89f43a7da2cc4d2c2d3ddd8d4f9784e6798fc7":
        raise ValueError("lib/ansible/module_utils/basic.py")


# Generated at 2022-06-13 16:14:00.515387
# Unit test for function checksum
def test_checksum():
    # Test sha1
    assert secure_hash_s(b'hello') == secure_hash(os.path.join(os.path.dirname(__file__), 'test_data', 'checksum_test_sha1'))
    # Test md5
    if _md5:
        assert md5(os.path.join(os.path.dirname(__file__), 'test_data', 'checksum_test_md5')) == 'f6542e6b8651cf2f2a59a33eb94b31e9'

# Generated at 2022-06-13 16:14:13.230176
# Unit test for function md5s
def test_md5s():
    ''' test MD5 digest algorithm. '''
    from ansible.module_utils.six import PY3

    # We need to return a different value than something that includes a b'' for python3.
    if PY3:
        assert md5s('TestRôle') == 'a2fbe0daf04b821c6f3911ed2c242e3c'
    else:
        assert md5s('TestRôle') == 'a2fbe0daf04b821c6f3911ed2c242e3c'

if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-13 16:14:18.845126
# Unit test for function md5s
def test_md5s():
    import tempfile
    from ansible.module_utils._text import to_text
    (dummy, temp_path) = tempfile.mkstemp()

    # Create file
    open(temp_path, 'w').close()

    try:
        assert md5s(temp_path) == md5(temp_path)
    except IOError:
        msg = "Could not open %s, is it missing or a directory?" % to_text(temp_path)
        print(msg)
    

# unit test for function md5

# Generated at 2022-06-13 16:14:20.904903
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == "5d41402abc4b2a76b9719d911017c592"


# Generated at 2022-06-13 16:14:26.970842
# Unit test for function checksum
def test_checksum():
    assert checksum('test/ansible/hacking/test_module_style.py') == '3f4c4a4e4e72f70a8d1435c0a2a07c36ed6efb28'
    assert checksum('test/ansible/hacking/test_module_style-missing_file') is None
    assert checksum('test/ansible/hacking') is None
    assert checksum('test/ansible/hacking/') is None
    assert checksum('test/ansible/hacking/test_module_style.py', 'sha1') == '3f4c4a4e4e72f70a8d1435c0a2a07c36ed6efb28'

# Generated at 2022-06-13 16:14:28.801182
# Unit test for function md5
def test_md5():
    md5('/dev/null')

# Generated at 2022-06-13 16:14:34.289800
# Unit test for function md5s
def test_md5s():
    assert md5s("1234567890") == 'e807f1fcf82d132f9bb018ca6738a19f'
    assert md5s("The quick brown fox jumps over the lazy dog") == '9e107d9d372bb6826bd81d3542a419d6'
    assert md5s("The quick brown fox jumps over the lazy dog.") == 'e4d909c290d0fb1ca068ffaddf22cbd0'

# Generated at 2022-06-13 16:14:45.080220
# Unit test for function checksum
def test_checksum():
    pass

if __name__ == '__main__':
    import ansible.utils.hashs
    from ansible.module_utils.hashs import *
    from ansible.module_utils.hashs import md5s, md5
    import os
    import time
    import string
    import random
    import tempfile
    import errno

    def test_hash_func(hash_func):
        assert hash_func('abc') == 'a9993e364706816aba3e25717850c26c9cd0d89d'

    test_hash_func(secure_hash_s)
    test_hash_func(checksum_s)
    test_hash_func(ansible.utils.hashs.checksum_s)

# Generated at 2022-06-13 16:14:55.752856
# Unit test for function md5s
def test_md5s():
    import unittest
    class md5sTestCase(unittest.TestCase):
        def test_md5s(self):
            self.assertEqual(md5s('hello world'), '5eb63bbbe01eeed093cb22bb8f5acdc3')

        def test_md5s_unicode(self):
            self.assertEqual(md5s(u'hello world'), '5eb63bbbe01eeed093cb22bb8f5acdc3')

        def test_md5s_utf8(self):
            self.assertEqual(md5s(u'\u716e'.encode('utf-8')), 'c8ca7ac3d3b3fdc44ef6e66f64d3a1a4')


# Generated at 2022-06-13 16:15:06.729771
# Unit test for function md5s
def test_md5s():
    # MD5 of a empty string
    assert md5s("") == "d41d8cd98f00b204e9800998ecf8427e"
    # MD5 of 'a'
    assert md5s("a") == "0cc175b9c0f1b6a831c399e269772661"
    # MD5 of 'ansible'
    assert md5s("ansible") == "ceccd97bf25b7d3f9f9d7c4c4e4d4cc4"
    # MD5 of unicode
    assert md5s("中文".encode("utf-8")) == "f6d8eaea09b72dbe76d895893ebe90f9"

# Generated at 2022-06-13 16:15:09.142847
# Unit test for function md5s
def test_md5s():
    assert md5s("ansible") == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"


# Generated at 2022-06-13 16:15:20.680172
# Unit test for function checksum
def test_checksum():
    ''' test checksums '''

    from tempfile import NamedTemporaryFile

    test_file1 = NamedTemporaryFile(delete=False)
    test_file1.write(b"foo")
    test_file1.close()

    test_file2 = NamedTemporaryFile(delete=False)
    test_file2.write(b"bar")
    test_file2.close()


# Generated at 2022-06-13 16:15:25.066137
# Unit test for function md5
def test_md5():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5('/bin/ls') == '2f3d3c83b7f1c0864f9da9bac00f70eb'

# Generated at 2022-06-13 16:15:26.759456
# Unit test for function md5s
def test_md5s():
    md5s("abc")

# Generated at 2022-06-13 16:15:28.597417
# Unit test for function md5s
def test_md5s():
    # TODO: write some unit tests for this function
    pass


# Generated at 2022-06-13 16:15:36.917321
# Unit test for function checksum
def test_checksum():
    test_str = "hello world"
    test_file = os.path.join(os.path.dirname(__file__), "test_checksum.txt")
    with open(test_file, "w") as f:
        f.write(test_str)

    # test string
    ret = checksum_s(test_str)
    assert ret == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"

    # test file
    ret = checksum(test_file)
    assert ret == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"

    os.unlink(test_file)

# Generated at 2022-06-13 16:15:39.340386
# Unit test for function checksum
def test_checksum():
    results = checksum("test_utils.py")
    assert results == "54e0ebe9990eba919c9d6a1b6c55b6e2b6ccdbf8"

# Generated at 2022-06-13 16:15:47.934550
# Unit test for function md5
def test_md5():
    import filecmp
    import tempfile
    import shutil

    fd, temp_path = tempfile.mkstemp()
    with open(temp_path, 'wb') as f:
        f.write("Hello, world!")
    f.close()

    md5 = md5(temp_path)
    assert md5 == 'fc3ff98e8c6a0d3087d515c0473f8677'

    os.close(fd)
    os.remove(temp_path)
    assert not os.path.exists(temp_path)



# Generated at 2022-06-13 16:15:51.280823
# Unit test for function md5s
def test_md5s():
    return md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:15:53.443179
# Unit test for function md5
def test_md5():
    assert md5s("abc") == '900150983cd24fb0d6963f7d28e17f72'


# Generated at 2022-06-13 16:15:59.096089
# Unit test for function md5
def test_md5():
    filename = '/bin/ansible'
    #print("%s is %s" % (filename, checksum(filename)))
    assert checksum(filename) == '7e6adb54e95e8d3b0e2c89882f3ea21a'

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:16:13.078355
# Unit test for function md5s
def test_md5s():
    assert md5s(b"foo") == "acbd18db4cc2f85cedef654fccc4a4d8"
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"
    import sys
    if sys.version_info < (2, 6):
        assert md5s("foo".decode("utf-8")) == "acbd18db4cc2f85cedef654fccc4a4d8"
    else:
        assert md5s("foo".decode("utf-8")) == "acbd18db4cc2f85cedef654fccc4a4d8"


# Generated at 2022-06-13 16:16:16.646480
# Unit test for function md5
def test_md5():
    ''' md5 Unit test'''
    import os
    filename = 'test_module'
    try:
        open(filename, 'w+')
        assert(None != md5(filename))
    finally:
        os.remove(filename)

# Generated at 2022-06-13 16:16:20.694986
# Unit test for function md5s
def test_md5s():
    assert 12 == len(md5s('abc'))
    assert 32 == len(md5s(b'abc'))
    assert md5s(b'abc') == md5s('abc')

if __name__ == "__main__":
    test_md5s()

# Generated at 2022-06-13 16:16:30.798873
# Unit test for function checksum
def test_checksum():
    if not os.path.exists('/bin/ls'):
        return 'ls not found, skipping checksum test'
    ls_sha1 = checksum('/bin/ls')
    ls_md5 = md5('/bin/ls')
    cmd = "find /bin/ls -type f -printf '%s %m %n %u %g %D %i %A@ %C@ %T@ %p\n'"
    (rc, out, err) = module.run_command(cmd)
    fields = out.split()
    # We don't have the following file attributes of /bin/ls so hard-code them here:
    # st_uid=0
    # st_gid=0
    # st_atime=...
    # st_ctime=...
    # st_mtime=...
    fields

# Generated at 2022-06-13 16:16:34.780076
# Unit test for function md5
def test_md5():
    dummy_file = '/tmp/test.txt'
    dummy_content = "This is a test file"
    f = open(dummy_file, "w")
    f.write(dummy_content)
    f.close()
    test_md5_digest = _md5(dummy_content.encode('utf-8')).hexdigest()
    assert test_md5_digest == md5(dummy_file)
    os.unlink(dummy_file)
    

# Generated at 2022-06-13 16:16:38.011339
# Unit test for function md5
def test_md5():
    # Generate MD5 hash of file
    current_md5 = md5("tests/md5.data")

    # Make sure we received an actual MD5 hash
    if current_md5 is None:
        print("Could not obtain an MD5 hash for the file")
        return False

    # Compare expected MD5 hash with the actual MD5 hash
    if current_md5 == "821f205d4c1058f3ccb7fa6f627a6b18":
        print("MD5 hash matches")
        return True
    else:
        print("MD5 hash does not match")
        return False



# Generated at 2022-06-13 16:16:40.929116
# Unit test for function md5
def test_md5():
    assert md5("/etc/ssh/ssh_config") == "a0c6c1884b8c9713ba2b0daf711a0569"


__all__ = [ 'checksum', 'checksum_s', 'md5', 'md5s' ]

# Generated at 2022-06-13 16:16:49.548149
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    digest = _md5()
    blocksize = 64 * 1024
    try:
        infile = open(os.path.join(os.path.dirname(__file__), 'checksum.py'), 'rb')
        block = infile.read(blocksize)
        while block:
            digest.update(block)
            block = infile.read(blocksize)
        infile.close()
    except IOError as e:
        raise AnsibleError("error while accessing the file %s, error was: %s" % (filename, e))

    file_hash_value = 'aff0f8ad23e6c424b6342409c9607b39'

# Generated at 2022-06-13 16:17:01.924988
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest

    class TestChecksum(unittest.TestCase):
        """Unit test for ansible.utils.checksum"""
        def setUp(self):
            self.temp_file = None
            self.temp_dir = None

        def tearDown(self):
            # Remove temp file
            if self.temp_file:
                os.unlink(self.temp_file)
            # Remove temp dir
            if self.temp_dir:
                os.rmdir(self.temp_dir)

        @staticmethod
        def calculate_content_hash(content):
            return secure_hash_s(content)


# Generated at 2022-06-13 16:17:11.397585
# Unit test for function checksum
def test_checksum():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    DATA = "hello world"
    EXPECTED_SHA1S = '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    if _md5:
        EXPECTED_MD5S = '5eb63bbbe01eeed093cb22bb8f5acdc3'

    class TestChecksum(unittest.TestCase):

        def test_checksum_s(self):
            self.assertEqual(checksum_s(DATA), EXPECTED_SHA1S)

        def test_checksum(self):
            filename = '/tmp/test_checksum.txt'


# Generated at 2022-06-13 16:17:22.511476
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('test data') == 'cacb07e5d9a5b9969b44e7e9d0f22c69'
    else:
        try:
            md5s('test data')
            assert False
        except ValueError:
            assert True

# vim: set et ts=4 sw=4:

# Generated at 2022-06-13 16:17:27.140002
# Unit test for function md5
def test_md5():
    result1 = md5("/etc/passwd")
    result2 = md5("/etc/passwd")
    assert result1 == result2

    result1 = md5("/nonexistent")
    result2 = md5("/nonexistent")
    assert result1 == result2
    assert result1 == None


# Generated at 2022-06-13 16:17:29.687586
# Unit test for function md5s
def test_md5s():
    assert(md5s('test') == '098f6bcd4621d373cade4e832627b4f6')


# Generated at 2022-06-13 16:17:33.373973
# Unit test for function checksum
def test_checksum():
    """ make sure checksum can run without errors """
    try:
        checksum('/etc/passwd')
        return True
    except Exception as e:
        print(e)
        return False

# Generated at 2022-06-13 16:17:36.316956
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:17:43.426141
# Unit test for function checksum
def test_checksum():
    # Create a temporary file
    fh = open("/tmp/ansible_test_checksum", "w")
    fh.write("ANSIBLE TEST FILE")
    fh.close()

    # Check the checksum
    assert checksum("/tmp/ansible_test_checksum") == checksum_s("ANSIBLE TEST FILE")

    # Remove the temporary file
    os.remove("/tmp/ansible_test_checksum")



# Generated at 2022-06-13 16:17:51.629496
# Unit test for function md5
def test_md5():
    import tempfile
    file_name = "/tmp/md5.tst"
    content = "this is a test string"
    # Create a file
    with tempfile.NamedTemporaryFile(delete=False) as f:
        file_name = f.name
        f.write(content)
    # Compute md5 hash
    file_md5 = md5(file_name)
    # Check hash
    assert file_md5 == '5f187b5c85b5f3b5f5e5e5fe5c5b5f185b5c5f5d5e5e5f5c5e5f5e5d5b5f5c5f'
    # Remove file
    os.remove(file_name)

# Generated at 2022-06-13 16:18:00.932294
# Unit test for function md5
def test_md5():

    import tempfile
    import shutil

    tmpdir = None


# Generated at 2022-06-13 16:18:08.699697
# Unit test for function md5
def test_md5():
    import tempfile
    h = md5s(b"test")
    assert h == '098f6bcd4621d373cade4e832627b4f6', "md5s wrong: %s" % h
    fd, fname = tempfile.mkstemp()
    os.write(fd, b"test")
    os.close(fd)
    h = md5(fname)
    os.unlink(fname)
    assert h == '098f6bcd4621d373cade4e832627b4f6', "md5 wrong: %s" % h

# Generated at 2022-06-13 16:18:10.221526
# Unit test for function md5s
def test_md5s():
    if _md5:
        print('MD5: %s' % md5s('abcd'))
        return True
    print('MD5: NOT AVAILABLE')
    return True


# Generated at 2022-06-13 16:18:19.222940
# Unit test for function md5
def test_md5():
    test_string = "Hello world, my name is Svetlin Kandur"
    assert(md5s(test_string) == 'e1f7f2d3c86d373b056c12638d7e7e13')

# Generated at 2022-06-13 16:18:24.700736
# Unit test for function checksum
def test_checksum():
    assert checksum_s("blah") == "900150983cd24fb0d6963f7d28e17f72"
    assert checksum_s("blah") != checksum_s("blah ")

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:18:25.347130
# Unit test for function checksum
def test_checksum():
    # FIXME: write unit tests for this
    pass



# Generated at 2022-06-13 16:18:29.392216
# Unit test for function md5s
def test_md5s():
    import random
    r = random.random()
    assert md5s("%s"%(r)) == md5("tests/support/md5s-%s"%(r))


# Generated at 2022-06-13 16:18:36.868884
# Unit test for function checksum
def test_checksum():
    import os
    import tempfile

    temp_file = tempfile.NamedTemporaryFile('wb', delete=False)
    test_string = 'this is a test'
    temp_file.write(test_string)
    temp_file.close()

    assert checksum(temp_file.name) == '5c5bc5d0ed67b8a34084b48f7db6c2b9757f8d8f', 'sha1 checksum of temp_file does not match'
    assert md5(temp_file.name) == 'd133e98f0b3670c5f67d5a25b5e7413b', 'md5 checksum of temp_file does not match'

    os.unlink(temp_file.name)


# Generated at 2022-06-13 16:18:43.345576
# Unit test for function md5
def test_md5():
    ''' md5 unit test'''
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert md5('/etc/passwd') == '1f96e0e894c4f7ffa0b4f927b9d59bb8'


# Generated at 2022-06-13 16:18:52.879550
# Unit test for function md5s
def test_md5s():
    """ md5s unit test """

    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(u'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'\xe4') == 'b4f6d2d3ddf3935aab7e9bae6d46d6dd'
    assert md5s(u'\u00e4') == 'b4f6d2d3ddf3935aab7e9bae6d46d6dd'

# Generated at 2022-06-13 16:18:57.468977
# Unit test for function md5s
def test_md5s():
    expected = '86e749c8c6eca1519c7f50cf3c43c8b6'
    current = md5s('hello')
    assert expected == current

# Generated at 2022-06-13 16:19:04.775669
# Unit test for function md5
def test_md5():
    import tempfile

    # Create a temporary file and write to it
    tmpfd, tmpfname = tempfile.mkstemp()
    try:
        fcntl.lockf(tmpfd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        # Resource is busy, skip the test
        os.unlink(tmpfname)
        return

    tmpfile = os.fdopen(tmpfd, 'w')
    tmpfile.write('blah')
    tmpfile.close()

    # Calculate the MD5 checksum
    md5sum = md5(tmpfname)

    # Compare it to an expected value
    if md5sum != '8d900c8a6aaaf4b4ddc4a4d4f8e0114e':
        raise Exception

# Generated at 2022-06-13 16:19:10.057752
# Unit test for function md5
def test_md5():
  data = u'abcdefg'
  assert md5s(data) == '7ac66c0f148de9519b8bd264312c4d64'
  assert md5(__file__) == '7c416647073a1fdc003f7565be103faa'

# Generated at 2022-06-13 16:19:22.360246
# Unit test for function checksum
def test_checksum():
    test_file = open('test_checksum.txt', 'w')
    test_file.write('test file')
    test_file.close()
    h1 = checksum('test_checksum.txt')
    os.remove('test_checksum.txt')
    h2 = checksum('test_checksum.txt')
    assert h1 == 'dea06c0c47b9d7516d1741d7ca1607bb7085fc0d'
    assert h2 == None
    h3 = checksum_s('test')
    assert h3 == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

# Generated at 2022-06-13 16:19:25.210281
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"

# Generated at 2022-06-13 16:19:27.954300
# Unit test for function md5
def test_md5():
    assert(md5('/usr/share/ansible/test/utils/test_md5.input') == '8b1ec634c228f2a2d7c0a8defebc7d32')

# Generated at 2022-06-13 16:19:29.764283
# Unit test for function md5s
def test_md5s():
    ''' test_md5s '''

    md5s('RAh9ZapH')

# Generated at 2022-06-13 16:19:34.135945
# Unit test for function md5s
def test_md5s():
    ''' test_md5s '''
    assert md5s('Hello') == '8b1a9953c4611296a827abf8c47804d7'
    assert md5s('World') == '7d793037a0760186574b0282f2f435e7'
    assert md5s('HelloWorld') == '12827a6a9a3c3d6a7b8f1743df7cecc3'
    assert md5s('HelloWorld'*100) == '69ce21c7a0faaba68e6a665b19af96f6'



# Generated at 2022-06-13 16:19:38.829211
# Unit test for function md5s
def test_md5s():
    print("md5s(\"hello world\") = ", md5s("hello world"))
    print("md5s(\"hello world\", \"utf-8\") = ", md5s("hello world", "utf-8"))


# Generated at 2022-06-13 16:19:46.384992
# Unit test for function checksum
def test_checksum():
    ''' Unit test for function checksum '''

    import tempfile

    # Create temporary file with content
    fd, fname = tempfile.mkstemp()
    os.write(fd, "Hello World!")
    os.close(fd)

    # Calc checksum
    cksum = checksum(fname)

    # Remove temporary file
    os.unlink(fname)

    # Validate checksum
    if cksum != "0a4d55a8d778e5022fab701977c5d840bbc486d0":
        raise AnsibleError("checksum test failed! (0a4d55a8d778e5022fab701977c5d840bbc486d0 != %s)" % cksum)



# Generated at 2022-06-13 16:19:54.962443
# Unit test for function md5
def test_md5():
    """Checks that secure_hash_s and secure_hash works correctly for various
    inputs. Test cases are based on values calculated with md5sum which is
    compatible with secure_hash.
    """
    # check that md5 and sha1 work in FIPS mode
    fips_md5 = secure_hash_s('', _md5)
    fips_sha1 = secure_hash_s('')
    assert(fips_md5 == fips_sha1 == 'da39a3ee5e6b4b0d3255bfef95601890afd80709')
