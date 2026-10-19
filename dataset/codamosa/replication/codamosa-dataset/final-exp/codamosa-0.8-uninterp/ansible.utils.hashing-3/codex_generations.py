

# Generated at 2022-06-13 16:10:14.905651
# Unit test for function checksum
def test_checksum():
    import tempfile
    test_file = tempfile.mktemp()
    with open(test_file, 'wb') as f:
        f.write(b"foobar")
    assert checksum(test_file) == "8843d7f92416211de9ebb963ff4ce28125932878"
    # NOTE: python2.4 does not support utf-8 encoding and fails here
    try:
        assert checksum_s(u"\u30d1\u30fc\u30c6\u30a3") == "9c9a958c4f30bab7f4b4f61a4a1c3d3fb73810a9"
    except UnicodeEncodeError:
        pass
    os.remove(test_file)

# Generated at 2022-06-13 16:10:24.738170
# Unit test for function md5
def test_md5():
    # Test values against md5sum on CentOS 6
    # Output:
    # $ echo -n "hello world" | md5sum
    # 5eb63bbbe01eeed093cb22bb8f5acdc3
    #
    # $ md5sum tests/utils/test_md5
    # 3c364d0f1efb4a4c4c937d1f14261c50
    #
    # $ echo -n "hello world" > test_md5
    # $ md5sum test_md5
    # 5eb63bbbe01eeed093cb22bb8f5acdc3

    assert md5s('hello world'), '5eb63bbbe01eeed093cb22bb8f5acdc3'


# Generated at 2022-06-13 16:10:32.683401
# Unit test for function checksum
def test_checksum():
    # Need test data.  Pick the README file
    test_data = to_bytes("README.md")
    test_sum = '03f8e3c8be2c1a5d5af5b87e894549027d3a3f0d'
    assert secure_hash(test_data) == test_sum
    assert checksum(test_data) == test_sum
    assert checksum_s(test_data) == test_sum
    assert md5(test_data) == test_sum
    assert md5s(test_data) == test_sum

# Generated at 2022-06-13 16:10:37.925817
# Unit test for function md5s
def test_md5s():
    assert md5s("foo") == "acbd18db4cc2f85cedef654fccc4a4d8"
    assert md5s("foo\n") == "070a2cfe0f94c2bf823a9df65e0bcf18"


# Generated at 2022-06-13 16:10:43.031258
# Unit test for function md5
def test_md5():
    import tempfile

    tmpfile = tempfile.NamedTemporaryFile()
    with open(tmpfile.name, "w") as f:
        f.write("This is a test")
    hashed = md5(tmpfile.name)
    assert(hashed == '6959bc4e9c936d4a1bd2385b4c13d8b7')


# Generated at 2022-06-13 16:10:50.821608
# Unit test for function checksum
def test_checksum():
    '''Test the checksum function.'''
    f = open('/etc/passwd', 'rb')
    cksum = checksum(f.fileno())
    f.close()
    assert cksum == checksum('/etc/passwd')

    assert checksum_s(u'hello') == checksum_s('hello')
    assert checksum_s('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'

# Generated at 2022-06-13 16:10:58.219884
# Unit test for function md5
def test_md5():
    for filename, expected_md5_hash in [
            ('/etc/passwd', 'cacf6f5d939bab3d9b1f1fc7724d1f65'),
            ('/etc/shadow', '473e22b5ce5d5ff5eda3034e1031ffc5'),
            ('/etc/group', '26a05ba9c921d5ff5eff10c5e5ff31d5'),
            ('/etc/gshadow', '0ca7c0f9abeb3faa3e1eaf3a3c2d432a')]:
        md5_hash = md5(filename)

# Generated at 2022-06-13 16:11:01.292645
# Unit test for function md5s
def test_md5s():
    mystring = "Hello world!"
    myhash = "ed076287532e86365e841e92bfc50d8c"
    assert md5s(mystring) == myhash


# Generated at 2022-06-13 16:11:10.275896
# Unit test for function md5
def test_md5():

    # Test script
    test_script = """
#!/bin/sh
res="$(prog1 $1)"
echo $res
"""
    # Create temporary script
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile(mode='w+t') as script:
        script.write(test_script)
        script.flush()
        # Execute test script
        from subprocess import Popen, PIPE
        p = Popen([script.name, 'test'], stdout=PIPE)
        assert to_bytes(p.communicate()[0]) == to_bytes('test')

# backwards compat only

# Generated at 2022-06-13 16:11:15.738328
# Unit test for function checksum
def test_checksum():
    f = open('/tmp/test','w')
    f.write('foo')
    f.close()
    assert checksum('/bin/ls') == '6b8e3ef4a90a0f91e713c43aa9b4cbb2'
    assert checksum('/tmp/test') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert checksum('/tmp') == None
    assert checksum('/tmp2') == None

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:11:20.686983
# Unit test for function md5
def test_md5():
    print(secure_hash('/etc/ansible/ansible.cfg'))


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:11:25.101590
# Unit test for function checksum
def test_checksum():
    import tempfile

    _, path = tempfile.mkstemp()

    with open(path, 'w') as f:
        f.write("x")

    assert checksum(path) == '11f6ad8ec52a2984abaafd7c3b516503785c2072'


# Generated at 2022-06-13 16:11:30.394020
# Unit test for function md5
def test_md5():
    assert md5s('Hello') == '8b1a9953c4611296a827abf8c47804d7'
    assert md5s('World') == '7d793037a0760186574b0282f2f435e7'

# Generated at 2022-06-13 16:11:38.259438
# Unit test for function md5s
def test_md5s():
    '''
    >>> md5s('test')
    '098f6bcd4621d373cade4e832627b4f6'
    >>> md5s(b'test')
    '098f6bcd4621d373cade4e832627b4f6'
    >>> md5s(u'test')
    '098f6bcd4621d373cade4e832627b4f6'
    >>>
    '''
    pass



# Generated at 2022-06-13 16:11:45.139402
# Unit test for function md5
def test_md5():
    import tempfile

    fd, f = tempfile.mkstemp()
    with open(f, 'w') as fo:
        fo.write("Hello World\n")
    sum = md5(f)
    assert (sum == "b10a8db164e0754105b7a99be72e3fe5"), "invalid md5sum: %s" % (sum)
    os.unlink(f)

# Generated at 2022-06-13 16:11:57.376908
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
    assert md5s('The quick brown fox jumps over the lazy dog.') == 'e4d909c290d0fb1ca068ffaddf22cbd0'
    assert md5s('The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog') == 'dfa4f0af0f7adf2afd08ffd522fb1a9f'


# Generated at 2022-06-13 16:12:03.096709
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    assert(md5s(b"value") == '7e240de74fb1ed08fa08d38063f6a6a9')
    assert(md5(__file__) == 'd751713988987e9331980363e24189ce')


# Generated at 2022-06-13 16:12:13.335847
# Unit test for function md5
def test_md5():
    ''' function md5 unit test '''

    from ansible.module_utils.basic import AnsibleModule

    def _test_md5(data, expected):
        hashed = md5s(data)
        if hashed != expected:
            module.fail_json(msg="md5 hash of %s did not match expected %s" % (data, expected))

    module = AnsibleModule(argument_spec=dict())
    fname = os.path.join(os.path.dirname(__file__), 'test_utils_md5.txt')

    # Test the string version
    _test_md5("hello", "5d41402abc4b2a76b9719d911017c592")

# Generated at 2022-06-13 16:12:25.204156
# Unit test for function checksum
def test_checksum():

    def make_word_string(word_len):
        ''' Generate a random string of ascii letters of length word_len '''
        import random
        import string

        word = ''
        while len(word) != word_len:
            word += random.choice(string.ascii_letters)
        return word

    def make_file_with_lines(filepath, num_lines):
        ''' Create a file with x number of random lines and a trailing newline '''
        import random
        import string

        f = open(filepath, 'wb')
        for line in range(num_lines):
            f.write(make_word_string(random.randint(0,255)) + b'\n')
        f.close()

    # Create some files to test against
    from tempfile import NamedTemporaryFile

# Generated at 2022-06-13 16:12:36.205136
# Unit test for function md5s
def test_md5s():
    import time
    import random
    import string
    s = ''.join(random.choice(string.letters)
                for i in range(random.randint(1, 200)))
    t1 = time.time()
    t2 = time.time()
    while (t2 - t1) < 1:
        md5s(s)
        t2 = time.time()
    print("%d calls to md5s() in %.3f sec" %
          (int(t2 - t1), t2 - t1))
    print("%.0f md5s() per second" % (int(t2 - t1) / (t2 - t1)))

# Generated at 2022-06-13 16:12:43.477808
# Unit test for function md5
def test_md5():
    data = 'foo'
    assert md5s(data) == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5(__file__) == '9cad06b25bb75c3b0614e2de7d5e83bf'

# Generated at 2022-06-13 16:12:47.497318
# Unit test for function checksum
def test_checksum():
    try:
        secure_hash_s('')
    except Exception:
        pass
    else:
        raise ValueError('secure_hash_s() with empty string should fail')

    try:
        md5s('')
    except Exception:
        pass
    else:
        raise ValueError('md5s() with empty string should fail')

    file_name = "/bin/ls"
    checksum_results = checksum(file_name)
    md5_results = md5(file_name)

    for key in checksum_results:
        if(checksum_results[key] != md5_results[key]):
            raise ValueError('CHECKSUM IS BROKEN!')

# Generated at 2022-06-13 16:12:51.344504
# Unit test for function md5s
def test_md5s():
    data = "hello world"
    md5sum_data = "ed076287532e86365e841e92bfc50d8c"
    h = md5s(data)
    assert h == md5sum_data



# Generated at 2022-06-13 16:12:56.126774
# Unit test for function md5
def test_md5():
    md5_checksum = md5("../lib/ansible/module_utils/basic.py")
    if md5_checksum != "f0c0f17ac42c1f06e205c0a9a38a0c2b" :
        raise ValueError("md5 function failed. The checksum is not equal to the expected value.")
    print("md5 function passed.")

# Generated at 2022-06-13 16:13:01.886151
# Unit test for function checksum
def test_checksum():
    real_sum = '5d41402abc4b2a76b9719d911017c592'
    test_sum = checksum_s('hello')
    assert real_sum == test_sum
    assert checksum_s(b'hello') == test_sum
    assert checksum_s(u('hello')) == test_sum
    assert checksum_s(to_bytes(u('hello'), errors='surrogate_or_strict')) == test_sum


# Generated at 2022-06-13 16:13:05.592877
# Unit test for function checksum
def test_checksum():
    ''' Unit test for function checksum '''
    curdir = os.getcwd()
    path = os.path.dirname(__file__)
    if path:
        os.chdir(path)
    assert(checksum('test/files/ansible.cfg') == '4d55b9f9t9216b77d2cbb16a6313df3f')
    if curdir != path:
        os.chdir(curdir)

# Generated at 2022-06-13 16:13:09.623420
# Unit test for function md5
def test_md5():
    import os
    os.environ['LANG'] = 'en_US.UTF-8'
    assert md5("/bin/cat") == "dbe51d2b2b04f702c3db4799181f85d8"

# Generated at 2022-06-13 16:13:12.196955
# Unit test for function md5s
def test_md5s():
    ansible_md5s = md5s('test')
    assert ansible_md5s == '098f6bcd4621d373cade4e832627b4f6'

# Generated at 2022-06-13 16:13:21.023446
# Unit test for function md5s
def test_md5s():
    ''' Test md5s function.  '''
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert md5s('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'

# Generated at 2022-06-13 16:13:32.305126
# Unit test for function md5
def test_md5():
    ''' unit tests for md5 '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import ansible_module
    from ansible.module_utils.basic import to_bytes
    from ansible.module_utils.basic import to_text

    module = AnsibleModule({}, supports_check_mode=True)

    def _test(md5_string, md5_expected, data_passed):
        md5_obtained = md5(module, md5_string)
        assert md5_obtained == md5_expected, \
            to_text("md5 function failed to generate md5 hash. "
                    "Expected {0} but got {1}".format(md5_expected, md5_obtained), errors='surrogate_or_strict')

   

# Generated at 2022-06-13 16:13:42.615146
# Unit test for function md5
def test_md5():
    import tempfile
    tf, tfn = tempfile.mkstemp()
    tfh = os.fdopen(tf, 'w')
    tfh.write('abc')
    tfh.close()
    assert(md5(tfn) == '900150983cd24fb0d6963f7d28e17f72')
    os.remove(tfn)

# Generated at 2022-06-13 16:13:47.854468
# Unit test for function checksum
def test_checksum():
    assert checksum_s('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    assert checksum('CHANGELOG.md') == 'b6a93b2b1c0f303bea1996433932c45e9f827b01'

# Generated at 2022-06-13 16:13:50.965701
# Unit test for function md5s
def test_md5s():
    s = md5s('hello')
    assert s == '5d41402abc4b2a76b9719d911017c592'


# Generated at 2022-06-13 16:13:57.512448
# Unit test for function checksum
def test_checksum():
    test_str = "hello this is test string"
    test_file = open("./test_checksum", "w")
    test_file.write(test_str)
    test_file.close()
    data = checksum_s(test_str)
    file = checksum("./test_checksum")
    if not data:
        print("checksum_s(%s) returns None" %(test_str))
    if not file:
        print("checksum(./test_checksum) returns None")
    os.remove("./test_checksum")

# Generated at 2022-06-13 16:14:08.748502
# Unit test for function md5s
def test_md5s():

    from ansible.playbook.play_context import PlayContext

    results = dict()
    results['md5sum'] = '098f6bcd4621d373cade4e832627b4f6'
    play_context = PlayContext()
    play_context.MD5_CHECKSUM = False
    result = checksum_s('test', play_context=play_context)
    assert result == results['md5sum'], \
        "md5s('test') returned %s instead of 098f6bcd4621d373cade4e832627b4f6" % result

    del results['md5sum']
    results['checksum'] = 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    play_context.MD5_CHECKS

# Generated at 2022-06-13 16:14:17.607546
# Unit test for function md5
def test_md5():
    # Check for expected exception
    if _md5:
        try:
            md5(None)
            raise AssertionError("md5(None) should throw exception")
        except ValueError as e:
            pass
    else:
        try:
            md5(None)
            raise AssertionError("md5(None) should throw exception")
        except ValueError as e:
            pass
    # Check that identical files have the same hashes
    h1 = md5('test/files/test01')
    h2 = md5('test/files/test02')
    assert h1 == h2
    # Check that different files have different hashes
    h2 = md5('test/files/test03')
    assert h1 != h2


# Generated at 2022-06-13 16:14:28.217883
# Unit test for function md5
def test_md5():

    # Check if the function md5 is working fine
    # Create a dummy file
    temporary_file='/tmp/ansible-ansible-tmp-file'
    temporary_file_handle=open(temporary_file, 'a+')
    temporary_file_handle.write('Hello World from ansible')
    temporary_file_handle.close()

    # Check if the function md5 returning the expected checksum
    assert(md5(temporary_file) == '93c6f4642eeccd8c2f25b96f03bba1d9')

    # Check if the function md5 returning the expected checksum for the sample string
    assert(md5s('Ansible Test') == 'd4c6ff30df6aad2fcbf5d5e564f724bd')

    # Cleanup by removing the

# Generated at 2022-06-13 16:14:33.374630
# Unit test for function md5s
def test_md5s():
    assert md5s('Bob') == '8afdb7c612d9da4a4ec137a6b9d1b4e1'
    assert md5s('I love you, Mary Jane, forever. !!!!') == '842c7bdc368ab135d50f56a1a8a7c885'


if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:14:44.415939
# Unit test for function checksum
def test_checksum():
    ''' ansible.utils.checksum '''

    import tempfile
    import os

    fd, fn = tempfile.mkstemp()

# Generated at 2022-06-13 16:14:49.185486
# Unit test for function md5s
def test_md5s():
    assert md5s('He is clever, he is not handsome') == '9f9b0c7b50edb5b5e1d8eacf4904e4ea'


# Generated at 2022-06-13 16:14:57.807637
# Unit test for function md5
def test_md5():
    import os
    f = open("unittest.txt", "w")
    f.write("this is a test")
    f.close()
    # md5 function should return the md5 sum of file
    assert md5("unittest.txt") == "4e87b25ba749c59e2b8a2b18ee93b472"
    os.unlink("unittest.txt")

# Generated at 2022-06-13 16:15:02.666017
# Unit test for function md5
def test_md5():
    import sys
    import os
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, 'test.txt')
    if sys.version_info >= (3,):
        test_text = b"this is a test"
    else:
        test_text = "this is a test"
    try:
        with open(tmpfile, 'wb') as f:
            f.write(test_text)
        assert(md5(tmpfile) == "a3f4596dcb7fb1b9c1b7ab13e08c7723")
    except:
        assert(False)
    finally:
        shutil.rmtree(tmpdir)


# Generated at 2022-06-13 16:15:09.923721
# Unit test for function checksum
def test_checksum():
    str1 = to_bytes('hello world')
    str2 = to_bytes('hello world')
    file1 = 'test1.txt'
    file2 = 'test2.txt'
    f1 = open(file1, 'wb')
    f1.write(str1)
    f1.close()
    f2 = open(file2, 'wb')
    f2.write(str2)
    f2.close()
    chk = checksum(file1)
    chk1 = checksum(file2)
    os.remove(file1)
    os.remove(file2)
    assert chk == chk1

# Generated at 2022-06-13 16:15:15.581717
# Unit test for function md5
def test_md5():
    ''' Unit test for md5. There is no file with pre-computed hash, so we just test for ValueError in FIPS mode.
    '''
    try:
        from hashlib import md5 as _md5
        return None
    except ImportError:
        try:
            from md5 import md5 as _md5
        except ImportError:
            # Assume we're running in FIPS mode here
            _md5 = None

    if _md5:
        return None
    else:
        return md5

# Generated at 2022-06-13 16:15:16.873692
# Unit test for function md5s
def test_md5s():
    assert md5s("test") == md5("test")

# Generated at 2022-06-13 16:15:20.130271
# Unit test for function md5s
def test_md5s():
    print('Testing md5s()')
    assert len(secure_hash_s('test')) == 40
    assert len(secure_hash_s(b'test')) == 40
    assert secure_hash_s('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'



# Generated at 2022-06-13 16:15:22.604360
# Unit test for function md5s
def test_md5s():
    assert md5s('data') == '1e50210a82024b0aaf4b054822a475aa'



# Generated at 2022-06-13 16:15:26.540882
# Unit test for function md5
def test_md5():
    assert md5('lib/ansible/module_utils/basic.py') == 'f1c427e07d8404d7b42c3b3f7b508261'
    assert md5s('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

# Generated at 2022-06-13 16:15:34.730813
# Unit test for function md5
def test_md5():
    # Create random data
    import random
    import string
    data = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    data_hash = md5s(data)
    # Create temporary file
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile()
    # Write random data to temporary file
    tmpfile.write(data)
    tmpfile.seek(0)
    # Compute md5 hash of temporary file and compare to data hash
    assert md5(tmpfile.name) == data_hash

# Generated at 2022-06-13 16:15:38.246570
# Unit test for function checksum
def test_checksum():
    ''' test checksum function '''
    print("####### checksum #########")
    try:
        print(checksum("/bin/ls"))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:15:44.547632
# Unit test for function md5s
def test_md5s():
    assert md5s('foobar') == '3858f62230ac3c915f300c664312c63f'



# Generated at 2022-06-13 16:15:49.697320
# Unit test for function md5
def test_md5():
    filename = 'test_file.txt'
    test_content = 'This is a test file!'
    checksum_value = md5(filename)

    f = open(filename, 'w')
    f.write(test_content)
    f.close()

    assert checksum_value == '23ed2532d55a470b75c2bbaa4b4ee168', checksum_value
    os.remove(filename)

# Generated at 2022-06-13 16:15:59.443933
# Unit test for function checksum
def test_checksum():
    from ansible.utils.path import makedirs_safe
    import tempfile

    tfile = tempfile.NamedTemporaryFile('w', delete=False)
    tfile.write(u"hello world\n")
    tfile.close()
    assert checksum(tfile.name) == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    os.unlink(tfile.name)

    assert checksum_s(u"hello world\n") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    tfile = tempfile.NamedTemporaryFile('w', delete=False)
    tfile.write(u"hello world\n")
    tfile.close()

# Generated at 2022-06-13 16:16:02.221142
# Unit test for function md5s
def test_md5s():
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert len(md5s('foo')) == 32



# Generated at 2022-06-13 16:16:05.634022
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'



# Generated at 2022-06-13 16:16:10.986812
# Unit test for function md5s
def test_md5s():
    assert md5s("foobar") == '3858f62230ac3c915f300c664312c63f'
    try:
        assert md5s(u"foobar") == '3858f62230ac3c915f300c664312c63f'
    except AssertionError:
        print("md5s() does not handle unicode")


# Generated at 2022-06-13 16:16:15.071156
# Unit test for function md5s
def test_md5s():
    text = 'I am the walrus'
    r = md5s(text)
    assert r == 'e34a7d71fc4f4a67a0f8c2f79b677a0b'


# Generated at 2022-06-13 16:16:21.860359
# Unit test for function md5s
def test_md5s():
    correct_md5 = 'b3a8e54c6d9a9ee9f6c16f2b73ab6b1e'
    if not _md5:
        try:
            md5s('a')
        except ValueError:
            pass
        else:
            assert False, 'MD5 available in FIPS mode'
    else:
        assert md5s('a') == correct_md5
        assert md5s(u'a') == correct_md5

# Generated at 2022-06-13 16:16:28.585623
# Unit test for function md5
def test_md5():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    filename = os.path.join(os.path.dirname(__file__), 'test.py')
    assert(md5(filename) == '4e4d8c88cba4a9b9f887462ce0b8aa42')
    assert(md5s('ABCDEFG') == '1bc29b36f623ba82aaf6724fd3b16718')

# Generated at 2022-06-13 16:16:32.203440
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    s = "hello world"
    s2 = "hello world2"

    assert md5s(s) == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s(s) != md5s(s2)


# Generated at 2022-06-13 16:16:38.389468
# Unit test for function checksum
def test_checksum():
    checksum_str = checksum('/etc/hosts')
    print(checksum_str)

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:16:46.212493
# Unit test for function md5s
def test_md5s():
    assert md5s('') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('a') == '0cc175b9c0f1b6a831c399e269772661'
    assert md5s('ab') == '187ef4436122d1cc2f40dc2b92f0eba0'
    assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert md5s('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'


# Generated at 2022-06-13 16:16:54.602760
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    import random
    import string

    # Create a temp dir
    tmpdir = tempfile.mkdtemp()
    # Create a temp file
    testfile = tmpdir + '/testfile'
    fd = open(testfile, 'wb')
    # Create a random string of size > 2*block size
    rndstr = ''.join(random.choice(string.ascii_uppercase) for _ in range(2*64*1024))
    rnddata = rndstr.encode('utf-8')
    fd.write(rnddata)
    fd.close()
    # Get an md5 hash for the data
    m = md5(testfile)
    # Remove the file and the dir
    os.remove(testfile)

# Generated at 2022-06-13 16:17:05.806748
# Unit test for function md5s
def test_md5s():
    import os
    import random
    import string
    import tempfile
    import unittest

    class TestChecksum(unittest.TestCase):

        def setUp(self):
            rand_chars = string.ascii_lowercase + string.digits
            self.data = ''.join(random.choice(rand_chars) for _ in range(1024))
            (fd, self.fname) = tempfile.mkstemp()
            os.close(fd)
            with open(self.fname, 'w') as f:
                f.write(self.data)

        def test_md5s(self):
            result = md5s(self.data)

# Generated at 2022-06-13 16:17:09.855099
# Unit test for function md5s
def test_md5s():
    s = "this is a string"
    h = md5s(s)
    if h != "e627c0d36e61d17668a8db1b3c3278ae":
        print("test_md5s: h is '%s'" % (h))
        raise ValueError("test_md5s: failed")



# Generated at 2022-06-13 16:17:12.984855
# Unit test for function md5s
def test_md5s():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    s = md5s('12345')
    assert s == '827ccb0eea8a706c4c34a16891f84e7b'



# Generated at 2022-06-13 16:17:17.169872
# Unit test for function checksum
def test_checksum():
    import tempfile
    import shutil

    # Create a temp directory and a temp file
    tmp_dir = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(dir=tmp_dir)
    tmp_file_path = tmp_file.name
    # Write a string to the temp file
    tmp_file.write("shawn")
    tmp_file.flush()

    # Calculate the secure hash
    sha1_val = checksum(tmp_file_path)
    assert sha1_val == "7f89851cb27cb7f93c1f570b39d80c4e4dc7d81c"

    # Clean up
    tmp_file.close()
    shutil.rmtree(tmp_dir)


# Generated at 2022-06-13 16:17:22.311559
# Unit test for function md5s
def test_md5s():
    '''Test module method'''
    assert md5s(b'') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert md5s('foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert md5s('foo' * 10) == '37b51d194a7513e45b56f6524f2d51f2'
    assert md5s('foo' * 1000) == 'c4e4d770502a106b2633f99dcc8d6eef'


# Generated at 2022-06-13 16:17:31.300493
# Unit test for function checksum
def test_checksum():
    ret = checksum('/bin/ls')
    if ret != '3ba2f8828df9e0271d964ff50bcee183':
        print('TEST FAILED!  checksum /bin/ls returned %s' % ret)
        return False
    ret = checksum('/bin/notfound')
    if ret != None:
        print('TEST FAILED!  checksum /bin/notfound returned %s' % ret)
        return False
    ret = checksum('/bin/')
    if ret != None:
        print('TEST FAILED!  checksum /bin/ returned %s' % ret)
        return False
    ret = checksum_s('hello')
    if ret != '5d41402abc4b2a76b9719d911017c592':
        print

# Generated at 2022-06-13 16:17:33.189995
# Unit test for function checksum
def test_checksum():
    # Placeholder.  No testing of this module.
    pass

# Generated at 2022-06-13 16:17:46.794024
# Unit test for function md5
def test_md5():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    file = module.get_bin_path('ansible', True, ['/usr/local/bin'])
    res = module.run_command([file, "--version"])
    out = res[1]

    computed = md5s(out)
    known = "d6a0f1c81ab8697d2513ea60b6edb34e"

    assert computed == known


# Generated at 2022-06-13 16:17:48.748749
# Unit test for function md5s
def test_md5s():
    assert md5s('test') == '098f6bcd4621d373cade4e832627b4f6'


# Generated at 2022-06-13 16:17:51.698950
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s('abc') == '900150983cd24fb0d6963f7d28e17f72'
    else:
        try:
            md5s('abc')
            assert False # We should have raised an exception
        except ValueError:
            pass

# Generated at 2022-06-13 16:17:58.183222
# Unit test for function md5
def test_md5():
    assert md5('lib/ansible/modules/core/files/file.py') == "735de2e774513d7ae1c8bbea0b187d12"


if __name__ == "__main__":
    import sys
    try:
        assert sys.argv[1]
        print(md5(sys.argv[1]))
    except:
        print("need a filename as argument")

# Generated at 2022-06-13 16:18:04.208955
# Unit test for function md5
def test_md5():
    '''test the md5 function'''
    from shutil import copyfileobj

    # Notes on obtaining output files:
    # Slashes are doubled to prevent shell from interpreting them as escape
    # Example:
    #     echo -n "foo" > t; md5sum t
    # Should use double quotes around sha1sum argument to prevent shell
    # interpretation of asterisk
    # Example:
    #     echo -n "foo" > t; sha1sum "t"
    # Python 3 adds a newline to the output of print(), so to use this script
    # to generate data files, remove the final string slice

    # Use /dev/null input to avoid printing newline at end of string
    data = md5(os.devnull)

# Generated at 2022-06-13 16:18:07.456114
# Unit test for function checksum
def test_checksum():
    assert checksum("/bin/ls") == "55f2bf4f7a4b00a96a7e12d9f14b7eddca2c00e7"
    assert checksum("/bin/fake") is None


# Generated at 2022-06-13 16:18:17.357087
# Unit test for function md5
def test_md5():
    data = 'hello'
    if not _md5:
        try:
            md5s(data)
        except ValueError as e:
            assert str(e) == 'MD5 not available.  Possibly running in FIPS mode'
    else:
        assert md5s(data) == '5d41402abc4b2a76b9719d911017c592'
        filename = '/bin/ls'
        assert md5(filename) == 'e85220b7437c1c3e3f9b97972b7f6b40'

# Generated at 2022-06-13 16:18:20.805773
# Unit test for function md5s
def test_md5s():
    assert md5s(b'foo') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-13 16:18:27.013142
# Unit test for function md5s
def test_md5s():
    if _md5:
        assert md5s("abc") == "900150983cd24fb0d6963f7d28e17f72"
    else:
        try:
            md5s("abc")
            assert False, "md5s should not be available, but was."
        except ValueError:
            pass

# Generated at 2022-06-13 16:18:33.090570
# Unit test for function md5
def test_md5():
    import tempfile
    import shutil
    d = tempfile.mkdtemp()
    try:
        f = open(d+'/test_md5', 'w')
        f.write("test data")
        f.close()
        checksum = md5(d+'/test_md5')
        assert checksum == '5a105e8b9d40e1329780d62ea2265d8a'
    finally:
        shutil.rmtree(d)

# Generated at 2022-06-13 16:18:50.469614
# Unit test for function md5s
def test_md5s():
    ''' shasum test_module_utils.py  | cut -d' ' -f1 '''
    test_data = "767d9b5cafb8a24bfa7a77d78aef0d40"
    # Load file
    data = open(__file__, 'r').read()
    # Compute md5s for test_module_utils.py
    my_md5 = md5s(data)
    # Assert if the result is the same
    assert test_data == my_md5
    print("test_module_utils: md5s passed")

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:18:52.876672
# Unit test for function checksum
def test_checksum():
    filename = "test/ansible/modules/files/foo.txt"
    assert checksum(filename) == checksum_s('something')


# Generated at 2022-06-13 16:18:58.410818
# Unit test for function md5
def test_md5():
    assert md5s('1234') == '81dc9bdb52d04dc20036dbd8313ed055'
    assert md5s(u'1234') == '81dc9bdb52d04dc20036dbd8313ed055'

# Generated at 2022-06-13 16:19:10.274568
# Unit test for function md5s
def test_md5s():
    import unittest

    class MD5TestCase(unittest.TestCase):
        ''' test md5s function '''
        def runTest(self):
            self.assertEqual(md5s('hello'), '5d41402abc4b2a76b9719d911017c592')
            self.assertEqual(md5s('hello\n'), 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d')
            self.assertEqual(md5s('{"foo": "bar"}'), '65e644e80c2a6d8c384ff0749e89cc1b')

# Generated at 2022-06-13 16:19:15.582969
# Unit test for function md5s
def test_md5s():

    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')

    # call md5s once to trigger the import of hashlib
    hash_md5s = md5s('hi')
    if hash_md5s != "49f68a5c8493ec2c0bf489821c21fc3b":
        raise ValueError('MD5 failed to hash string')


# Generated at 2022-06-13 16:19:20.239497
# Unit test for function md5s
def test_md5s():
    ''' return a valid checksum for a string '''

    string = 'test string'
    hexdigest = md5s(string)

    if hexdigest != 'e2cbf6920d9fc7b281b0372e1f5a7dc5' :
        raise Exception("md5s error: invalid checksum for string '%s': %s" % (string, hexdigest))
    else:
        return True



# Generated at 2022-06-13 16:19:22.107175
# Unit test for function md5s
def test_md5s():
    '''Function to test md5s'''
    assert md5s('ansible') == '3b61797dab8a5a62e52933b07ff209d9'

# Generated at 2022-06-13 16:19:28.664460
# Unit test for function checksum
def test_checksum():
    assert checksum(__file__) == checksum(__file__)
    assert checksum(__file__) == checksum_s(open(__file__).read())
    if _md5:
        assert md5(__file__) == md5(__file__)
        assert md5(__file__) == md5s(open(__file__).read())

#
# Unit tests for checksum_s
# These unit tests also ensure compatibility for md5s
#

# Generated at 2022-06-13 16:19:32.108001
# Unit test for function md5
def test_md5():
    assert md5("lib/ansible/modules/core/system/setup.py") == "4d3647b469d1f527a3f0b3c9a9fa49d2"

if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:19:35.526293
# Unit test for function md5s
def test_md5s():
    import binascii
    md5_rv = md5s('test')
    md5_rv = binascii.unhexlify(md5_rv)
    assert(len(md5_rv) == 16)


# Generated at 2022-06-13 16:19:47.794680
# Unit test for function md5s
def test_md5s():
    from tempfile import NamedTemporaryFile
    tmpfile = NamedTemporaryFile(delete=False)
    try:
        tmpfile.write(b'xyz123')
        tmpfile.close()

        assert secure_hash_s(b'xyz123') == secure_hash(tmpfile.name)
        assert secure_hash_s(b'xyz123', hash_func=_md5) == md5s('xyz123')
        assert secure_hash(tmpfile.name, hash_func=_md5) == md5(tmpfile.name)
    finally:
        os.unlink(tmpfile.name)

# Generated at 2022-06-13 16:19:56.041866
# Unit test for function md5
def test_md5():
    print("Testing md5 function")
    test_data = 'asdasdasd'
    md5_sum = 'd57d9a9b4db4b3ec4e4d67d4e69cc0f2'
    print("Testing md5 of string")
    assert(md5s(test_data) == md5_sum)
    print("Testing md5 of local file")
    test_file = os.path.join(sys.path[0], 'test_file.txt')
    test_file_sum = '914df7a4e3cfe4fd67d4d73edb7f100b'
    with open(test_file, 'w') as f:
        f.write(test_data)
    assert(md5(test_file) == test_file_sum)
   

# Generated at 2022-06-13 16:20:01.668359
# Unit test for function md5s
def test_md5s():
    ''' unit tests for md5s and md5 '''

    # MD5S
    # Verify string
    assert md5s("sample string") == "b16fa2b0cf3bfc9a7cab8e1359bcdac3"

    # Verify unicode string
    assert md5s(u"sample unicode string") == "dadb543c00f616d18debd97c433f06eb"

    # Verify integer
    assert md5s(1) == "c4ca4238a0b923820dcc509a6f75849b"

    # Verify integer string
    assert md5s("1") == "c4ca4238a0b923820dcc509a6f75849b"

    # Verify empty string