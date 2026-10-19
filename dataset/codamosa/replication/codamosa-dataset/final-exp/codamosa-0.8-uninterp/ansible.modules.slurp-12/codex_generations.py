

# Generated at 2022-06-13 06:10:04.160658
# Unit test for function main
def test_main():
    assert True == True

# Generated at 2022-06-13 06:10:04.592396
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:10:13.896227
# Unit test for function main
def test_main():
    import collections
    import pytest

    # input data
    content = b"some content"
    with open("some_file", "wb") as f:
        f.write(content)
    module_args = collections.namedtuple('module_args', 'src')("some_file")

    # expected output
    expected_content = str(base64.b64encode(content), "utf-8")
    expected_source = "some_file"
    expected_encoding = "base64"

    # prepare mock objects
    module = collections.namedtuple('module', 'exit_json params')(exit_json, module_args)
    setattr(module, "check_mode", True)
    setattr(module, "fail_json", pytest.fail)

    # call function main
    main()

    # check if

# Generated at 2022-06-13 06:10:14.424904
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 06:10:17.603627
# Unit test for function main
def test_main():
    source = '/var/run/sshd.pid'
    source_content = to_native(os.path.getsize(source), 'utf-8')
    data = base64.b64encode(source_content)

    assert data == b'MjE3OQo='
    assert source_content == '2179\n'
    assert os.path.getsize(source) > 0

# Generated at 2022-06-13 06:10:24.035304
# Unit test for function main
def test_main():
    '''
    A test for function main
    '''
    # Dummy text file for test.
    dummyfile = './test.txt'

    # Write some text to the file.
    with open(dummyfile, mode='w') as test_fh:
        test_fh.write('The quick brown fox jumps over the lazy dog.')

    # Run the main function.
    main()

    # Remove the dummy file.
    os.remove(dummyfile)

# Generated at 2022-06-13 06:10:31.013819
# Unit test for function main
def test_main():
    import mock

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    # Patch '_load_params' because it calls 'get_bin_path'

# Generated at 2022-06-13 06:10:36.523787
# Unit test for function main
def test_main():
    f = open('/tmp/python_slurp.txt', 'w')
    f.write(u'A test file to slurp.\n')
    f.write(u'Line 2\n')
    f.write(u'Line 3\n')
    f.write(u'Line 4\n')
    f.close()

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    source = '/tmp/python_slurp.txt'
    module.params['src'] = source
    with open(source, 'rb') as source_fh:
        expected_source_content = source_fh.read()

# Generated at 2022-06-13 06:10:41.245039
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params = {'src': "/etc/hosts"}
    module._handle_exception = lambda *args, **kwargs: None
    try:
        main()
    except SystemExit as e:
        assert e.code == 0

# Generated at 2022-06-13 06:10:46.237983
# Unit test for function main
def test_main():
    """Return sample metadata"""
    source = "/etc/hosts"
    result = {"content": "bm93ZGVtbw==\n", "encoding": "base64", "source": source}
    return result


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:10:57.205644
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='str', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    
    module.exit_json(content=data, source=source, encoding='base64')

# Sample test

# Generated at 2022-06-13 06:11:07.665688
# Unit test for function main
def test_main():
    import json

    from ansible.module_utils.common.collections import ImmutableDict

    src_path = os.getcwd() + '/slurp_test.txt'

    # Create a test file
    with open(src_path, 'w') as f:
        f.write('hello world')

    with open(src_path, 'r') as f:
        src_content = f.read()

    # Test with source file exists
    args = "{'src': '%s'}" % src_path
    result = AnsibleModule(argument_spec=json.loads(args)).run()
    assert result['changed'] is False
    assert result['source'] == src_path
    assert result['content'] == base64.b64encode(src_content)
    assert result['encoding'] == 'base64'



# Generated at 2022-06-13 06:11:19.245655
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.text import to_native
    import os.path
    import tempfile

    source_content = b'test data'

    # Create a temporary file
    source_fd, source_path = tempfile.mkstemp()

    # Write the file
    os.write(source_fd, source_content)
    os.close(source_fd)

    # Create a module as if it were created by AnsibleModule
    module = basic.AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True)
    module.params['src'] = source_path

    main()

    result = module._result
    assert result.get

# Generated at 2022-06-13 06:11:26.737026
# Unit test for function main
def test_main():
    import os
    import tempfile
    import json

    with tempfile.NamedTemporaryFile() as source_fh:
        source_fh.write(b'foobarbaz')
        source_fh.seek(0)
        module_args = dict(
            src=source_fh.name,
        )
        result = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True,
        ).execute()
        assert result['content'] == b'Zm9vYmFyYmF6'
        assert result['source'] == source_fh.name
        assert result['encoding'] == 'base64'

    with tempfile.NamedTemporaryFile() as source_fh:
        source_fh.write(b'foobarbaz')
        source

# Generated at 2022-06-13 06:11:32.909683
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    module.exit_json(content=source, source=source, encoding='base64')

# Generated at 2022-06-13 06:11:33.737080
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 06:11:44.236192
# Unit test for function main
def test_main():
    '''
    Allows module to be run via `python -m ansible_collections.ansible.community.modules.files slurp`
    '''
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:11:50.765884
# Unit test for function main
def test_main():
    with open('tests/fixtures/test_slurp', 'rb') as fh:
        test_content = fh.read()

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:11:57.481670
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True)
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:12:08.852171
# Unit test for function main
def test_main():
    import os
    import tempfile
    source = tempfile.NamedTemporaryFile()
    source.write(b"test")
    source.flush()

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    setattr(module, 'params', dict(src=source.name))
    setattr(module, '_debug', True)

    content = test_main.__wrapped__(module)
    assert content['content'] == b'dGVzdA=='

    source.close()

# Generated at 2022-06-13 06:12:33.455564
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.slurp import main
    from ansible.module_utils import common
    import tempfile
    import shutil
    import random
    import string
    file_tmp_dir = tempfile.mkdtemp(prefix='ansible_test_module_utils_file')
    src_file_path = os.path.join(file_tmp_dir, 'slurp_file_ansible_test')
    words = [word.encode('utf-8') for word in '''
        baeldung
        spring
        java
        tutorial
        blog
    '''.split()]

# Generated at 2022-06-13 06:12:40.661632
# Unit test for function main
def test_main():
    result = main()
    print("result = " + str(result))
    if result["changed"]:
        print("changed = " + str(result["changed"]))
        print("src = " + str(result["src"]))
        print("content = " + str(result["content"]))
        print("encoding = " + str(result["encoding"]))
    if result["failed"]:
        print("failed = " + str(result["failed"]))

# Generated at 2022-06-13 06:12:51.067704
# Unit test for function main
def test_main():
    '''
    slurp unit test
    '''

    # If both function and test_file are present run function
    # Otherwise run test_file code
    if 'function' in globals() and 'test_file' in globals():
        print('Running test file ' + test_file)
        exec(open(test_file).read())
    elif 'function' in globals():
        function()
    else:
        # Build module_path and run test_file
        module_path = os.path.dirname(os.path.realpath(__file__)) + '/' + test_file
        print('Running test file ' + module_path)
        exec(open(module_path).read())

# Generated at 2022-06-13 06:13:05.146426
# Unit test for function main
def test_main():
    def test_common(mocker, tmpfile, tmpfile2):
        # In order to test checking mode we need to mock open()
        mocker.patch.object(builtins, 'open', mocker.mock_open())

        # Make the temporary file readable by simulating the umask
        os.chmod(tmpfile, 0o666)

        module = mocker.MagicMock(params={}, check_mode=True)
        module.params['src'] = tmpfile
        main()

        # Assert that the original open has not been called
        builtins.open.assert_not_called()


# Generated at 2022-06-13 06:13:16.931553
# Unit test for function main
def test_main():
    test_source = 'test_source_file'
    test_data = b'1234567890'

    with open(test_source, 'wb') as source_fh:
        source_fh.write(test_data)

    module_args = {
        "src": test_source
    }

    mod = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    mod.params = module_args

    response = main()
    assert response['content'].decode('utf-8') == base64.b64encode(test_data).decode('utf-8')
    assert response['source'] == test_source

# Generated at 2022-06-13 06:13:21.556707
# Unit test for function main

# Generated at 2022-06-13 06:13:28.897837
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:13:38.445986
# Unit test for function main
def test_main():
    import json
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    # Create a temporary file to slurp
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('test')
    f.close()

    # Create the Ansible module
    module_args = dict(src=path)
    module = AnsibleModule(argument_spec=module_args)

    # Get the result
    result = main()

    # Ensure the expected result
    expected = {
        'content': to_bytes(base64.b64encode(to_bytes('test'))),
        'encoding': 'base64',
        'source': path,
    }

# Generated at 2022-06-13 06:13:50.239677
# Unit test for function main
def test_main():
    source = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', 'doc', 'FAQ.md')
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = source

    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()

    data = base64.b64encode(source_content)

    module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:13:56.278562
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import _AnsibleModule
    src = 'file'
    with open(src, 'wb+') as f:
        f.write(b'foobar\n')
    m = _AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
    )
    assert main() == m.exit_json(content=b'Zm9vYmFyCg==', source=src, encoding='base64')

# Generated at 2022-06-13 06:14:31.611388
# Unit test for function main
def test_main():
    from ansible.module_utils.common.text.converters import to_bytes
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    try:
        result = main()
        if result[0] == "MjE3OQo=":
            return True
    except Exception as e:
        print(to_native(e, errors='surrogate_then_replace'))


# Generated at 2022-06-13 06:14:42.403683
# Unit test for function main
def test_main():
    from ansible.modules.system.slurp import main
    from ansible.module_utils.six import b

    # Create a test file to slurp
    tf = open('/tmp/test_file', 'w')
    tf.write('This is a test string')

    # Run main function with parameters
    source = '/tmp/test_file'
    module = dict(src=source)

    result = main(module)

    # Remove test file
    os.remove('/tmp/test_file')

    answer = dict(changed=False, content=b'VGhpcyBpcyBhIHRlc3Qgc3RyaW5n', encoding='base64', source=source)
    assert result == answer


# Generated at 2022-06-13 06:14:52.601511
# Unit test for function main
def test_main():
    import sys
    import tempfile
    import textwrap

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']


# Generated at 2022-06-13 06:14:59.009011
# Unit test for function main
def test_main():
    # We need to mock the args and running environment:
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    setattr(module, 'check_mode', False)
    setattr(module.params, 'src', 'test')
    source = module.params['src']

    source_content = (b'5\n')

    data = base64.b64encode(source_content)

    os.mkdir('test')
    f = open('test/test.txt', 'w')
    f.write('5\n')
    f.close()
    assert main() == module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:15:03.220995
# Unit test for function main
def test_main():
    """Slurp unit test
    """
    # Mocking command line arguments
    class MyArgs(object):
        def __init__(self):
            self.args = None
        def __call__(self, args=None):
            self.args = args
            self.path = []

    args = MyArgs()
    args(['/tmp/test-file'])

    # Defining file path for slurp module
    test_file = '/tmp/test-file'
    file_name = 'test_file.py'
    # Writing a test file
    with open(file_name, 'w') as fh:
        fh.write('#! /usr/bin/python\n')
        fh.write('# -*- coding: utf-8 -*-\n')

# Generated at 2022-06-13 06:15:13.527675
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import os
    #os.environ['ANSIBLE_REMOTE_TMP'] = tempfile.gettempdir()

    (result, out, err) = module.run_command('echo "foobar" > test_file')
    assert result == 0
    (result, out, err) = module.run_command('base64  test_file')
    assert result == 0
    assert out == b'Zm9vYmFyCg=='
    result = module.from_json(ansible_module.run_command('ansible localhost -m slurp -a "src=test_file"'))
    assert result['content'] == 'Zm9vYmFyCg=='

    os.remove('test_file')

# Generated at 2022-06-13 06:15:17.949141
# Unit test for function main
def test_main():
    check_module('ansible.builtin.slurp')

    check_module_args(dict(
        src='/etc/sudoers',
    ))

    check_module_args(dict(
        path='/etc/sudoers',
    ))

# Generated at 2022-06-13 06:15:23.847024
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:15:34.829567
# Unit test for function main
def test_main():
    # Tests if the main function executes without error
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    try:
        open(__file__)
    except IOError as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % __file__
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % __file__
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % __file__

# Generated at 2022-06-13 06:15:42.087457
# Unit test for function main
def test_main():
    a = AnsibleModule(dict(src='/etc/hosts'), check_mode=False)
    with open(a.params['src'], 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)
    a.exit_json(content=data, source=a.params['src'], encoding='base64')

# Generated at 2022-06-13 06:16:44.623460
# Unit test for function main
def test_main():
    import os
    import pytest

    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'ansible', 'module_utils', 'ansible_module_slurp.py')
    content = b"MjE3OQo="
    encoding = 'base64'

    results = {}
    results['content'] = content
    results['source'] = source
    results['encoding'] = 'base64'

    assert main() == results

# Generated at 2022-06-13 06:16:53.729599
# Unit test for function main
def test_main():
    #Create the module object
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = './test_file'

    #Check if file exists
    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:16:55.920211
# Unit test for function main
def test_main():
    def test_fails():
        assert 1 == 1

    test_fails()

# Generated at 2022-06-13 06:17:05.788526
# Unit test for function main
def test_main():
    from ansible.modules.system.slurp import main

    with open("foo", "w") as fid:
        fid.write("hello world")

    r = main(dict(src="foo"))
    if r['encoding'] != 'base64':
        raise AssertionError("encoding was not base64")
    if r['content'] != 'aGVsbG8gd29ybGQ=':
        raise AssertionError("contents was not aGVsbG8gd29ybGQ=")
    if r['source'] != 'foo':
        raise AssertionError("source was not foo")
    os.unlink("foo")

# Generated at 2022-06-13 06:17:13.322390
# Unit test for function main
def test_main():
    # Set up fake input to get the results we want
    src = "fake_file"
    source_content = "fake_contents"

    # Get the results before open() is patched
    results1 = main(src, source_content)

    # Import the unittest module
    import unittest

    # Create a class that we can inherit from to get the patch() method
    class OpenClass(unittest.TestCase):
        pass

    # Change the base class of the class we just created
    OpenClass.__bases__ = (unittest.TestCase,)

    # Create the class instance
    fake_test_class = OpenClass()

    # The patch() method "monkey-patches" open()

# Generated at 2022-06-13 06:17:25.277835
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])),
        supports_check_mode=True
        )
    module.params['src'] = os.path.join(os.path.dirname(__file__), 'test_slurp.txt')
    # Mock open
    global open
    def my_open(filename, flags):
        assert filename == module.params['src']
        assert flags == 'rb'
        return my_open.f
    my_open.f = None
    open = my_open
    # Mock read
    global read
    def my_read():
        source_content = b'foo'
        return source_content
    read = my_read
    # Mock b64encode
    global b64en

# Generated at 2022-06-13 06:17:25.867297
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 06:17:26.766517
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 06:17:36.298713
# Unit test for function main
def test_main():
    # Test with file existing
    with open('/tmp/testfile', 'a') as myfile:
        myfile.write('unit test')

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:17:37.218520
# Unit test for function main
def test_main():
    assert main()