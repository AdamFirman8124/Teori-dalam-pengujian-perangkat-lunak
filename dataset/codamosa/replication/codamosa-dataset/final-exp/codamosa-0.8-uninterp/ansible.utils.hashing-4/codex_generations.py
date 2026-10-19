

# Generated at 2022-06-13 16:10:04.282466
# Unit test for function md5s
def test_md5s():
    hashsum = md5s('foo')
    if hashsum != 'acbd18db4cc2f85cedef654fccc4a4d8':
        raise AssertionError('md5s does not generate correct hash for \'foo\'')



# Generated at 2022-06-13 16:10:08.258912
# Unit test for function checksum
def test_checksum():
    checksum_file = checksum('/bin/ls')
    if checksum_file != '1c87afb11d62f99b9dd2868b8c950579b32db81b':
        raise Exception('checksum failure!')

# Generated at 2022-06-13 16:10:20.190205
# Unit test for function checksum
def test_checksum():
    import tempfile
    from random import randrange
    from shutil import rmtree

    tmp_dir = tempfile.mkdtemp()
    tmp_file = tmp_dir + "/file"
    tmp_sha1 = tmp_dir + "/file.sha1"
    tmp_md5 = tmp_dir + "/file.md5"
    tmp_content = ""
    for i in range(0, 4):
        tmp_content = tmp_content + chr(randrange(0, 256, 1))
    f = open(tmp_file, "w")
    f.write(tmp_content)
    f.close()
    f = open(tmp_sha1, "w")
    f.write(secure_hash(tmp_file))
    f.close()

# Generated at 2022-06-13 16:10:29.744233
# Unit test for function checksum
def test_checksum():
    import os
    import tempfile

    # Create a test file
    (test_fd, test_path) = tempfile.mkstemp()
    test_data = 'a'*1048576
    os.write(test_fd, test_data)
    os.close(test_fd)

    # Compute its checksum
    test_sha1 = checksum(test_path)

    # Remove the test file
    os.unlink(test_path)

    # Compare
    assert test_sha1 == '7c011ebdf91c5f170f0797e54844aca7b19455e4', test_sha1

    # Create a test file
    (test_fd, test_path) = tempfile.mkstemp()
    test_data = 'b'*1048576

# Generated at 2022-06-13 16:10:31.824859
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"



# Generated at 2022-06-13 16:10:34.289394
# Unit test for function checksum
def test_checksum():
    assert checksum('/bin/ls')


# Generated at 2022-06-13 16:10:38.770928
# Unit test for function md5s
def test_md5s():
    assert md5s("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5("../lib/ansible/utils/unicode.py") == "948c509a8e8a364b0795af4e146c7ea2"

# Generated at 2022-06-13 16:10:41.597597
# Unit test for function checksum
def test_checksum():
    filename = "test/data/plugin_loader/module_data/ping.py"
    assert checksum(filename) == 'c5d9a5e5a5f5e5d5'

# Generated at 2022-06-13 16:10:46.365663
# Unit test for function md5s
def test_md5s():
    try:
        md5s('foo')
    except ValueError as ve:
        # If we got an error, verify it was the right one
        if str(ve) == 'MD5 not available.  Possibly running in FIPS mode':
            pass
        else:
            raise ve
    else:
        # Should have raised an exception
        raise Exception('No exception was raised')

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:10:58.504018
# Unit test for function checksum
def test_checksum():
    import tempfile

    t = tempfile.NamedTemporaryFile(mode='w')
    t.write('abc')
    t.flush()

    sha = secure_hash(t.name)     # sha256 is the default
    assert sha == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    sha = checksum(t.name)
    assert sha == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'

    # Test with unicode because this also happens to catch a py2/py3 bug
    sha = secure_hash(u'abc')

# Generated at 2022-06-13 16:11:05.518635
# Unit test for function md5
def test_md5():

    data = 'hello world'
    assert md5s(data) == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    test_path = os.path.abspath(__file__)
    assert md5(test_path) == md5s(open(test_path, 'rb').read())

# Generated at 2022-06-13 16:11:11.422962
# Unit test for function checksum
def test_checksum():
    ''' test checksum function '''

    assert checksum("/bin/ls") is not None
    assert checksum("/bin/ls") == checksum("/bin/ls")
    assert checksum("/bin/ls") != checksum("/bin/cat")
    assert checksum("/bin/ls") != checksum("/usr/bin/ls")

# Generated at 2022-06-13 16:11:21.359619
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import os

    try:
        d = tempfile.mkdtemp()
        f = open(os.path.join(d, "foo"), "w")
        f.write("hello world\n")
        f.close()

        h = md5(os.path.join(d, "foo"))
        if h != "5eb63bbbe01eeed093cb22bb8f5acdc3":
            raise Exception("failed md5 test")

        h = md5(os.path.join(d, "bar"))
        if h is not None:
            raise Exception("failed md5 test: bar should not exist")
    finally:
        shutil.rmtree(d)

# Generated at 2022-06-13 16:11:30.605091
# Unit test for function md5s
def test_md5s():
    # Test case 1: an empty string should return d41d8cd98f00b204e9800998ecf8427e
    empty_string = ''
    assert md5s(empty_string) == 'd41d8cd98f00b204e9800998ecf8427e'

    # Test case 2: a string of 'Hello' should return b1946ac92492d2347c6235b4d2611184
    test_string = 'Hello'
    assert md5s(test_string) == 'b1946ac92492d2347c6235b4d2611184'

    # Test case 3: a string of 'HelloHello' should return d1b8bbb39c28b77dce1892809b6bb948
    test_string = 'HelloHello'
    assert md5s

# Generated at 2022-06-13 16:11:32.851674
# Unit test for function md5s
def test_md5s():
    return md5s("foo") == 'acbd18db4cc2f85cedef654fccc4a4d8'



# Generated at 2022-06-13 16:11:40.121412
# Unit test for function md5
def test_md5():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={'value':dict(required=True)})

    value = module.params.get('value')
    value_md5 = md5s(value)
    result = {
        'changed': True,
        'hexdigest': value_md5,
    }

    module.exit_json(**result)

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:46.401716
# Unit test for function md5
def test_md5():
    filename = "test_utils_md5"
    f = open(filename, "w")
    f.write("foo")
    f.close()

    h = '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert h == md5(filename)

    try:
        os.unlink(filename)
    except OSError:
        pass



# Generated at 2022-06-13 16:11:49.883091
# Unit test for function md5s
def test_md5s():
    return md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'


# Generated at 2022-06-13 16:11:54.527826
# Unit test for function md5s
def test_md5s():
    expected = "81b82f6d34a0f035c64c39e2d163c09b"
    assert md5s("aaa\n") == expected

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:12:04.341068
# Unit test for function md5s
def test_md5s():
    ''' test_md5s:
        test the md5s function against a known md5 hash
     '''

    from ansible.utils.hashing import md5s, md5

    test_string = "I am the very model of a modern major general."
    test_string_hash = "fa9883f1c55d9eedbff1b8f46f25d4c4"

    # Test function md5s with string
    result = md5s(test_string)
    assert result == test_string_hash

    # Test function md5 with test string as file
    tmp_file = 'tempfile'
    open(tmp_file, 'w').write(test_string)
    result = md5(tmp_file)
    os.unlink(tmp_file)
    assert result == test_string_hash



# Generated at 2022-06-13 16:12:10.272882
# Unit test for function md5s
def test_md5s():
    h = md5s('test')
    assert h == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:12:13.328338
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return
    test_data = 'test_md5s-data'
    assert md5s(test_data) == '9006b60604b7e0b2a79c9d9f892c6e30'

# Generated at 2022-06-13 16:12:25.197903
# Unit test for function checksum
def test_checksum():
    import hashlib
    from ansible.module_utils.basic import AnsibleModule

    def _assert(expected, test_value, msg):
        if expected != test_value:
            module.fail_json(msg='checksum: {0}'.format(msg))

    module = AnsibleModule(argument_spec={
            'data': dict(type='str'),
            'path': dict(type='path'),
            'algorithm': dict(type='str', default='sha1')
    })

    data = module.params['data']
    path = module.params['path']
    algorithm = module.params['algorithm'].lower()


# Generated at 2022-06-13 16:12:37.403522
# Unit test for function md5
def test_md5():
    data1 = 'Mary had a little lamb. '
    data2 = b'Its fleece was white as snow. '
    data3 = b"And everywhere that Mary went, the lamb was sure to go. "

    h = _md5()
    h.update(data1)
    h.update(data2)
    h.update(data3)
    assert md5s(data1 + data2 + data3) == h.hexdigest()
    assert md5s(data1) == md5s(data1)
    assert md5s(data1) != md5s(data2)

    f = open('/tmp/test_md5.out', 'w')
    f.write(data1)
    f.write(data2)
    f.write(data3)
    f.close()

    assert md

# Generated at 2022-06-13 16:12:47.080394
# Unit test for function md5
def test_md5():

    # 1) Test md5s
    s = 'Test data'
    d = md5s(s)
    if d != 'a6a89dc8b2759d8365a6a2b6e8cd8d34':
        raise AssertionError("unexpected md5s result: %s, expected: a6a89dc8b2759d8365a6a2b6e8cd8d34" % d)
    s = 'Test data\n'
    d = md5s(s)

# Generated at 2022-06-13 16:12:50.100716
# Unit test for function md5
def test_md5():
    data = "Hello World"
    assert md5s(data) == "b10a8db164e0754105b7a99be72e3fe5"

# Generated at 2022-06-13 16:12:54.944877
# Unit test for function md5
def test_md5():
    try:
        import hashlib
        hashlib.md5()
    except ImportError:
        try:
            from md5 import md5
        except ImportError:
            return True

    if md5('README.md') == '1e9b7a8a1a1c0f7d95b0a8b325bbb840':
        return True

# Generated at 2022-06-13 16:12:59.183316
# Unit test for function md5s
def test_md5s():
    #pylint: disable=missing-docstring
    import random
    import string
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    length = random.randint(5000, 10000)
    rand_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    assert len(md5s(rand_string)) == 32

# Generated at 2022-06-13 16:13:02.260704
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:13:12.538194
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import os

    dir_name = tempfile.mkdtemp()
    file_name = os.path.join(dir_name, 'ansible_test.tmp')
    with open(file_name, 'wb') as f:
        f.write(b'foo')     # Writing str crashes on Python 3, as it expects bytes
    try:
        checksum = md5(file_name)
        assert checksum == 'acbd18db4cc2f85cedef654fccc4a4d8'
    finally:
        shutil.rmtree(dir_name)


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:13:23.480406
# Unit test for function checksum
def test_checksum():
    import os

    # Setup
    test_file = "test"
    handle = open(test_file, "wb")

    handle.write(b'foo')
    handle.close()

    # Execute
    test_result = checksum(test_file)
    test_expected = 'acbd18db4cc2f85cedef654fccc4a4d8'

    # Verify
    assert test_result == test_expected, "Unexpected checksum result - %s" % test_result

    # Cleanup
    os.unlink(test_file)


# Generated at 2022-06-13 16:13:31.508954
# Unit test for function md5s

# Generated at 2022-06-13 16:13:35.478894
# Unit test for function md5
def test_md5():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5('/usr/bin/python') == '17a2e2afd32f493c8e39b1e16c2da9fc'

# Generated at 2022-06-13 16:13:47.497022
# Unit test for function md5
def test_md5():
    assert md5s("Hello World") == 'fc3ff98e8c6a0d3087d515c0473f8677'
    assert md5s("Hello World1") == '6f5902ac237024bdd0c176cb93063dc4'
    assert md5s(r"c:\test\test1") == '5a92d5f9b9a5fed5a7319d009ed66b55'
    assert md5s(r"c:\test\test2\test2") == '67d4a0b4d8c46b0e258cc577f64a86d0'
    assert md5s(r"/test/test1") == 'dc98c7e06f6e2b4634f051c9f1edec21'

# Generated at 2022-06-13 16:13:52.390929
# Unit test for function md5s
def test_md5s():
    assert _md5 and md5s('foobar') == '3858f62230ac3c915f300c664312c63f'
    assert not _md5 or md5s('foobar') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:13:58.023857
# Unit test for function checksum
def test_checksum():
    testfile = "/etc/passwd"
    normalhash = "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86"
    ansiblehash = secure_hash(testfile)
    assert normalhash == ansiblehash

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:14:02.446386
# Unit test for function md5s
def test_md5s():
    print("Testing md5s")
    assert md5s("1234") == "81dc9bdb52d04dc20036dbd8313ed055"


# Generated at 2022-06-13 16:14:06.385800
# Unit test for function md5s
def test_md5s():
    string_to_hash = "abcdefghijklmnopqrstuvwxyz"
    assert md5s(string_to_hash) == "c3fcd3d76192e4007dfb496cca67e13b"


# Generated at 2022-06-13 16:14:12.079768
# Unit test for function md5
def test_md5():
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('b') == '92eb5ffee6ae2fec3ad71c777531578f'
    assert md5s('The quick brown fox jumped over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

# Generated at 2022-06-13 16:14:20.127896
# Unit test for function checksum
def test_checksum():
    # test for md5() and md5s()
    if _md5:
        expected_md5 = '6e4bb6d8398e4fca6a5413c4b57037bb'
        assert md5('test/utils/test_hash.py') == expected_md5
        assert md5s('test/utils/test_hash.py') == expected_md5

    # test for checksum() and checksum_s()
    expected_sha1 = 'd075730f9158e5a26674fcd865c8e3466a1c5df8'
    assert checksum('test/utils/test_hash.py') == expected_sha1
    assert checksum_s('test/utils/test_hash.py') == expected_sha1


# Backwards compat only

# Generated at 2022-06-13 16:14:25.642112
# Unit test for function checksum
def test_checksum():
    assert checksum('foobar') == '8843d7f92416211de9ebb963ff4ce28125932878'



# Generated at 2022-06-13 16:14:31.828884
# Unit test for function md5s
def test_md5s():
    if not _md5:
        print('MD5 not available.  Possibly running in FIPS mode')
        return
    hsh = md5s('abc')
    if hsh != '900150983cd24fb0d6963f7d28e17f72':
        raise errors.AnsibleError('md5s() returned the wrong result: %s' % hsh)

# Generated at 2022-06-13 16:14:39.426322
# Unit test for function md5s
def test_md5s():
    import random
    import string

    def test_md5s_loop(test_string, iterations):
        for i in range(0, iterations):
            test_string += random.choice(string.ascii_letters +
                                         string.digits + string.punctuation)
            md5s(test_string)

    test_md5s_loop("asdfghjklm", 10)



# Generated at 2022-06-13 16:14:46.783921
# Unit test for function md5
def test_md5():

    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    filename = os.path.join(os.path.dirname(__file__), 'test_md5.py')

    #
    # These values have been generated by another tool
    #
    assert md5(filename) == 'b0425f251d76dfc1d5668e8f0c9d1b60'
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s('Hello World') == '6cd3556deb0da54bca060b4c39479839'


# Generated at 2022-06-13 16:14:53.422917
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'
    try:
        md5s(u'test')
    except ValueError as e:
        assert u'must be encoded string without NULL bytes' in e.message
    assert md5s('test'.encode('utf8')) == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:14:57.371268
# Unit test for function md5
def test_md5():
    md5_dict = dict(file='/etc/shadow', hash='c81474b4fbf4f4b4aa6c2a1f64e1eb0c')
    hash = md5(md5_dict['file'])
    assert hash == md5_dict['hash']


# Look at the file extension and return the appropriate hash algorithm

# Generated at 2022-06-13 16:15:02.283886
# Unit test for function md5s
def test_md5s():
    assert md5s('helloworld') == 'fc5e038d38a57032085441e7fe7010b0'
    assert md5s('helloworld\n') == '210f1fe8cde5b95feaf0294f5fd86414'
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s(None) == 'cfcd208495d565ef66e7dff9f98764da'
    assert md5s(5) == '37b51d194a7513e45b56f6524f2d51f2'
    assert md5s(True) == 'b326b5062b2f0e69046810717534cb09'

# Generated at 2022-06-13 16:15:05.009520
# Unit test for function md5s
def test_md5s():
    assert md5s("hello") == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:15:10.673807
# Unit test for function md5
def test_md5():
    assert md5s('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert md5s(b'Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert md5s(u'Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

# Generated at 2022-06-13 16:15:14.450513
# Unit test for function md5
def test_md5():
    fd = open('/tmp/c', 'w')
    print('test', file=fd)
    fd.close()
    assert md5('/tmp/c') == '7fda534a05e7a0f197d8f7ac472c9b9a'
    os.unlink('/tmp/c')


# Generated at 2022-06-13 16:15:19.751153
# Unit test for function md5s
def test_md5s():
    data = 'test'
    assert md5s(data) == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:15:21.804301
# Unit test for function checksum
def test_checksum():
    import tempfile
    try:
        (fd, fname) = tempfile.mkstemp()
        os.write(fd, b'hello')
        os.close(fd)
        assert checksum(fname) == '5d41402abc4b2a76b9719d911017c592'
    finally:
        os.remove(fname)

# Generated at 2022-06-13 16:15:24.208274
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'

# Generated at 2022-06-13 16:15:35.880195
# Unit test for function md5
def test_md5():
    # FIPS mode
    if not _md5:
        try:
            md5('/etc/passwd')
            assert False, 'md5 should fail in FIPS mode'
        except ValueError:
            pass
        return
    # Non-FIPS mode
    # Check file-based hashing
    known_md5s = ['7a157cacadb897a8e6c9e7d9b9fede2f',
                  'd12f7ac377b50ac19d7e8e8d342e087b',
                  '098f6bcd4621d373cade4e832627b4f6']
    # File md5s calculated with md5sum on system with the following versions of OpenSSL:
    #   OpenSSL 1.0.0e-fips 6 Sep 2011
    #

# Generated at 2022-06-13 16:15:42.724388
# Unit test for function md5s
def test_md5s():
    import tempfile
    #  nb:  %YAML1.1 is needed below in order to force ansible to format this
    #       as YAML 1.1.  If %YAML1.1 is omitted it will format as YAML 1.2,
    #       which would cause the test to fail (because the output of md5s would
    #       be quoted when printed to the terminal)
    tmp = tempfile.NamedTemporaryFile(mode="w+t", suffix='.yml')

# Generated at 2022-06-13 16:15:46.967143
# Unit test for function md5s
def test_md5s():
    dummy_data = 'Pretend that this is some data.'
    expected_result = '2e0faeadf2e68c900611aa28d55230c7'
    result = md5s(dummy_data)
    assert result == expected_result


# Generated at 2022-06-13 16:15:51.822488
# Unit test for function md5s
def test_md5s():
    # Python 2.6.6 and 2.6.8 both give different results for the
    # same input.  I'm not sure which one is the correct result
    # So just check that they are both the same.
    md5s_result = md5s('hi')
    assert (md5s_result == '49f68a5c8493ec2c0bf489821c21fc3b') or (md5s_result == 'cfcd208495d565ef66e7dff9f98764da')


# Generated at 2022-06-13 16:15:54.773645
# Unit test for function md5
def test_md5():
    assert md5("/bin/ls") == 'e2c9a9f4c4ef3a3d4a97b4dcc68d1b16'

# Generated at 2022-06-13 16:15:58.039411
# Unit test for function md5
def test_md5():
    file = "/etc/passwd"
    md5_value = md5(file)
    assert type(md5_value).__name__ == "str"

test_md5()

# Generated at 2022-06-13 16:16:01.144820
# Unit test for function md5
def test_md5():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'

# End backwards compat functions

# require basic docstring
# pylint: disable=missing-docstring
import unittest


# Generated at 2022-06-13 16:16:11.970264
# Unit test for function md5
def test_md5():
    import tempfile
    (fd, fname) = tempfile.mkstemp()
    fh = os.fdopen(fd, 'w')
    try:
        fh.write("123456789")
        fh.flush()
        the_md5 = md5(fname)
        print("md5(" + fname + ")=" + the_md5)
        assert (the_md5 == '25d55ad283aa400af464c76d713c07ad')
    finally:
        fh.close()
        os.remove(fname)


# Generated at 2022-06-13 16:16:22.835397
# Unit test for function md5s
def test_md5s():
    assert "81dc9bdb52d04dc20036dbd8313ed055" == md5s("hello world")
    assert "5eb63bbbe01eeed093cb22bb8f5acdc3" == md5s("foobar")
    assert "5e543256c480ac577d30f76f9120eb74" == md5s("pytools")
    assert "a9993e364706816aba3e25717850c26c9cd0d89d" == md5s("1234567890"*8)
    assert "cbfdac6008f9cab4083784cbd1874f76618d2a97" == md5s("1234567890"*9)

# Generated at 2022-06-13 16:16:29.879405
# Unit test for function md5s
def test_md5s():
    import sys
    # For python3, we must cast to bytes
    if sys.version_info >= (3,):
        check = 'b4e4d0e4e4d1e4d0e4b1e4e4e4d0e4e4e4d0e4b1ca'
    else:
        check = 'b4e4d0e4e4d1e4d0e4b1e4e4e4d0e4e4e4d0e4b1ca'
    assert(md5s('test') == check)

# Generated at 2022-06-13 16:16:33.909057
# Unit test for function md5
def test_md5():
    """ Test md5, same results as md5sum / sha1sum """

    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'
    f = 'myfile'
    assert md5(f) == md5s(open(f,'r').read())
    assert md5('notafile') == None
    assert md5(None) == None

if __name__ == "__main__":
    test_md5()

# Generated at 2022-06-13 16:16:39.093755
# Unit test for function checksum
def test_checksum():
    import os
    import shutil
    import tempfile

    # Create a dummy file to calculate checksum
    temp_dir = tempfile.mkdtemp()
    filename = os.path.join(temp_dir, 'test')
    try:
        with open(filename, 'w') as f:
            f.write('Hello World!')
        checksum_value = checksum(filename)
        assert checksum_value == '3a1865f03b89c8d57a0466a3c18fd07136128985'
        checksum_s_value = checksum_s('Hello World!')
        assert checksum_s_value == '3a1865f03b89c8d57a0466a3c18fd07136128985'
    finally:
        shutil.rmtree(temp_dir)


# Generated at 2022-06-13 16:16:47.497636
# Unit test for function md5s
def test_md5s():
    assert(md5s("hello world") == '5eb63bbbe01eeed093cb22bb8f5acdc3')
    assert(md5s("Hello World") == 'b10a8db164e0754105b7a99be72e3fe5')
    assert(md5s("hello world, how are you") == 'd0c9c0547a7bdde2253fe8b3e70c3e68')
    assert(md5s("HELLO WORLD") == '2ef7bde608ce5404e97d5f042f95f89f')
    assert(md5s("hello world, how are you?") == '7552cfc139815bce1da52831e0f9c9b2')

# Generated at 2022-06-13 16:16:53.292918
# Unit test for function md5s
def test_md5s():
    import random

    rand_str = "".join(random.sample("abcdefghijklmnop", 128))
    rand_digest = 'e787b8cde5c5dc5b23be5b547fce5aea'
    assert rand_digest == md5s(rand_str)



# Generated at 2022-06-13 16:16:59.049159
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert checksum_s(b'hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert checksum('test/support/files/chars \u00e1\u00e9\u00ed\u00f3\u00fa.txt') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'

# Generated at 2022-06-13 16:17:04.832222
# Unit test for function md5s
def test_md5s():
    input_string = b'ansible'
    expected_md5 = '86c955f184e8e6fe0322d3916c6ed490'
    actual_md5 = md5s(input_string)
    assert actual_md5 == expected_md5, "Actual md5 {0} doesn't match expected md5 {1}".format(actual_md5, expected_md5)

# Generated at 2022-06-13 16:17:07.390311
# Unit test for function md5s
def test_md5s():
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:17:12.025751
# Unit test for function md5s
def test_md5s():
    res = md5s('foo')
    assert res == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:17:20.280087
# Unit test for function md5
def test_md5():
    data = "Hello World!"
    assert(md5s(data) == "ed076287532e86365e841e92bfc50d8c")
    assert(md5s(data.encode('utf-8')) == "ed076287532e86365e841e92bfc50d8c")
    assert(md5(to_bytes('/dev/zero', errors='surrogate_or_strict')) == "e3b0c44298fc1c149afbf4c8996fb924")

# Generated at 2022-06-13 16:17:27.550740
# Unit test for function md5
def test_md5():
    # Python 2.4 does not have md5
    import sys
    if sys.version_info[:2] > (2, 4):
        try:
            from hashlib import md5 as _md5
        except ImportError:
            from md5 import md5 as _md5

        if __name__ == '__main__':
            import doctest
            doctest.testmod()
    else:
        print("not testing md5, python too old")

# unit test for function sha1

# Generated at 2022-06-13 16:17:36.359008
# Unit test for function md5
def test_md5():
    '''keywords'''
    from ansible.utils.encrypt import encrypt, decrypt
    import os
    import tempfile
    import shutil

    (fd, name) = tempfile.mkstemp(text=True)
    f = os.fdopen(fd, 'w')
    data = encrypt('test', 'password', 1)
    f.write(data)
    f.flush()

    hash = md5(name)
    assert hash == '0d9da09b39e12903d8c98dce50c86e6e'

    f.write(data)
    f.flush()

    hash = md5(name)
    assert hash == '5b32ed68f93a3fdf9d37b2a78a68a852'

    os.unlink(name)

    shutil

# Generated at 2022-06-13 16:17:39.468777
# Unit test for function checksum
def test_checksum():
    assert secure_hash_s('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert secure_hash('lib/ansible/modules/core/files/synchronize.py') == '7fff77aac4912a7e9e9b14edb410423e'

# Generated at 2022-06-13 16:17:43.382015
# Unit test for function md5
def test_md5():
    assert md5("/dev/null") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5("/dev/zero") == "cf83e1357eefb8bdf1542850d66d8007"


# Generated at 2022-06-13 16:17:49.600568
# Unit test for function md5s
def test_md5s():
    test_string = "Hello World"
    test_string_b = to_bytes(test_string, errors='surrogate_or_strict')
    test_md5 = _md5()
    test_md5.update(test_string_b)

    assert test_md5.hexdigest() == md5s(test_string)

    # Test the case where data is already a bytes object

    assert test_md5.hexdigest() == md5s(test_string_b)

# Generated at 2022-06-13 16:18:00.145101
# Unit test for function checksum
def test_checksum():
    '''Generates test data, then verifies that the checksums match'''

    import tempfile

    uniq = os.urandom(10)

    # Generate a tmp file for our tests
    fd, f_name = tempfile.mkstemp(prefix='ansible-test-')
    with os.fdopen(fd, "wb") as f:
        f.write(uniq)

    expected_sha1_digest = secure_hash_s(uniq)
    generated_sha1_digest = checksum_s(uniq)

    assert expected_sha1_digest == generated_sha1_digest
    assert checksum(f_name) == generated_sha1_digest

    os.unlink(f_name)


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:18:08.344809
# Unit test for function checksum
def test_checksum():
    # Create a temp file, compute checksum and then remove the temp file
    (fd, checksum_file) = tempfile.mkstemp()
    try:
        os.write(fd, b"hello, world\n")
        os.close(fd)
        if secure_hash(checksum_file) != '5eb63bbbe01eeed093cb22bb8f5acdc3':
            raise AssertionError("secure_hash(%s) != '5eb63bbbe01eeed093cb22bb8f5acdc3'" % checksum_file)
    finally:
        os.unlink(checksum_file)

# Generated at 2022-06-13 16:18:11.288293
# Unit test for function checksum
def test_checksum():
    '''
    Returns a hash of the string "HelloWorld"
    '''

    if checksum_s('Hello World') != '0a4d55a8d778e5022fab701977c5d840bbc486d0':
        return False
    return True

# Generated at 2022-06-13 16:18:31.223992
# Unit test for function checksum
def test_checksum():
    from ansible.module_utils.basic import AnsibleModule

    filename = "/bin/sh"

    module = AnsibleModule(
        argument_spec = dict(
        path = dict(required=True),
        ),
        )
    module.exit_json(changed=False, checksum=checksum(filename))



# Generated at 2022-06-13 16:18:37.203666
# Unit test for function md5
def test_md5():
    if _md5 == None:
        return

    filename = "/tmp/testfile"
    data = "This is a test."
    try:
        f = open(filename, 'w')
        f.write(data)
        f.close()
        assert md5(filename) == md5s(data)
    finally:
        os.remove(filename)

# Generated at 2022-06-13 16:18:46.414423
# Unit test for function md5
def test_md5():
    s = "Hello world"
    d = md5s(s)
    assert(d == "5eb63bbbe01eeed093cb22bb8f5acdc3")
    filename = "/tmp/md5.test"
    tmp = open(filename, "w")
    tmp.write(s)
    tmp.close()
    d = md5(filename)
    assert(d == "5eb63bbbe01eeed093cb22bb8f5acdc3")
    os.remove(filename)

# Generated at 2022-06-13 16:18:48.563850
# Unit test for function md5s
def test_md5s():
    assert(md5s("teststring") == "c7a16ec8c73b7a97f77a389a7e446dfb")

# Generated at 2022-06-13 16:18:51.934376
# Unit test for function md5
def test_md5():
    from tempfile import mkstemp

    (dummy, tmpFile) = mkstemp()
    assert(md5(tmpFile) is None)
    assert(md5s('my data') == '6f8db599de986fab7a21625b7916589c')
    os.remove(tmpFile)

# Generated at 2022-06-13 16:19:02.946325
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils.basic import AnsibleModule

    def test(module, data, expected):
        result = md5s(data)
        if result != expected:
            module.fail_json(msg="%s did not match %s" % (result, expected))

    module = AnsibleModule({},
                           supports_check_mode=False)

    test(module, "ansible", "e1faaff0c908f3cf3ff9b7a0608450ef")
    test(module, 1234, "81dc9bdb52d04dc20036dbd8313ed055")
    test(module, "a", "0cc175b9c0f1b6a831c399e269772661")

# Generated at 2022-06-13 16:19:09.867257
# Unit test for function checksum
def test_checksum():
    data = 'hello'
    # Python 2.4 sha module does not have hexdigest()
    assert '5d41402abc4b2a76b9719d911017c592' == sha1(data).hexdigest()
    assert '5d41402abc4b2a76b9719d911017c592' == checksum_s(data)
    assert 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d' == checksum_s(data, sha1)


# Generated at 2022-06-13 16:19:13.461352
# Unit test for function md5s
def test_md5s():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    results = md5s("foobar")
    module.exit_json(changed=False, ansible_facts={'test_hash_md5': results})


# Generated at 2022-06-13 16:19:18.121649
# Unit test for function md5s
def test_md5s():
    assert md5s("Hello, world!") == 'ed076287532e86365e841e92bfc50d8c'
    assert md5s("Hello, world!") == 'ed076287532e86365e841e92bfc50d8c'
    if _md5:
        assert md5s("Hello, world!") == secure_hash_s("Hello, world!")

# Generated at 2022-06-13 16:19:23.353446
# Unit test for function md5s
def test_md5s():
    from ansible.module_utils import basic
    basic._ANSIBLE_ARGS = basic.AnsibleOptions(connection='local', module_path=None, forks=100, become=True,
                                               become_method='sudo', become_user='root', check=False, diff=False)
    assert md5s(u'hello') == '5d41402abc4b2a76b9719d911017c592'
    assert md5s('hello') == '5d41402abc4b2a76b9719d911017c592'