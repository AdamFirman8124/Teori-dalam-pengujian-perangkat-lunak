

# Generated at 2022-06-13 06:10:07.934928
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:10:08.526418
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:10:16.068677
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible_collections.ansible.community.plugins.module_utils import basic
    from ansible_collections.ansible.community.plugins.module_utils.common.text.converters import to_native
    from ansible_collections.ansible.community.plugins.modules.files import slurp
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase

# Generated at 2022-06-13 06:10:19.761949
# Unit test for function main
def test_main():
    source = 'example.yml'
    with open(source, 'w') as f:
        f.write('foo')
    ret = main()
    assert ret.get('content') == b'Zm9v'
    os.remove('example.yml')

# Generated at 2022-06-13 06:10:29.239209
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_MODULE_UTILS_PATH'] = os.path.dirname(os.path.dirname(__file__))
    import ansible.module_utils.basic
    # mock module
    m = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # mock file system
    # mock function open
    m_open = mock.mock_open()
    # mock function b64encode
    m_b64encode = mock.Mock(return_value='b64encoded')
    # mock module os
    m_os = mock.MagicMock()
    m_os.path.exists.side_effect = [True]
    m_os.path.isdir.side_effect = [False]
    m_os.stat.return_value.st_size

# Generated at 2022-06-13 06:10:40.192197
# Unit test for function main

# Generated at 2022-06-13 06:10:42.921682
# Unit test for function main
def test_main():
    # This is a stub test
    # This test is not run because Ansible 2.9.1 is not being unit tested
    # This is used to test backward compatibility
    pass

# Generated at 2022-06-13 06:10:45.234891
# Unit test for function main
def test_main():
    '''Unit test for main'''
    pass

# Generated at 2022-06-13 06:10:55.349185
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.ansible_release import __version_info__
    from ansible.module_utils._text import to_bytes
    assert to_bytes(__version__) == b'2.12.2'
    assert to_bytes(__version_info__) == b'(2, 12, 2)'
    import tempfile
    tmpdir = tempfile.gettempdir()
    src = tmpdir + "/" + "testfile"
    with open(src, "w") as f:
        f.write("something")
    assert slurp_file(src) == b"something"
    assert slurp_file("/test/test/test") == (1, "unable to read file", None)

# Generated at 2022-06-13 06:11:01.993190
# Unit test for function main
def test_main():
    #
    # "Slurp" a temp file
    #
    tmp_file = None
    tmp_content = None
    try:
        # Create tmp file
        (tmp_fd, tmp_file) = tempfile.mkstemp()

        # Write some text to the "slurp" file
        tmp_content = "Hello, World!"
        os.write(tmp_fd, tmp_content.encode('utf-8'))
    finally:
        # Close the tmp file
        if tmp_fd is not None:
            os.close(tmp_fd)

    #
    # Test module invocation
    #

# Generated at 2022-06-13 06:11:19.777150
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

# Generated at 2022-06-13 06:11:29.845431
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

# Generated at 2022-06-13 06:11:40.864729
# Unit test for function main
def test_main():
    path = os.path.dirname(os.path.realpath(__file__))
    module = AnsibleModule(argument_spec=dict(src=dict(type='path', required=True, aliases=['path'])), supports_check_mode=True)
    module.params['src'] = path + '/test_slurp.py'
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:11:48.539268
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

# Generated at 2022-06-13 06:11:51.218910
# Unit test for function main
def test_main():
    src = './README.md'
    assert os.path.exists(src)
    assert os.path.isfile(src)
    with open(src, 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)

    assert data == main()

# Generated at 2022-06-13 06:11:57.755009
# Unit test for function main
def test_main():
    # Test with a nonexistent file
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    source = module.params['src'] = "doesnotexist"

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:12:03.186513
# Unit test for function main
def test_main():
    import tempfile
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(b'hello world')
        tmp.flush()
        module = AnsibleModule(argument_spec=dict(src=dict(type='path', required=True)))
        module.params['src'] = tmp.name
        main()
        tmp.close()


# Generated at 2022-06-13 06:12:13.337957
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

# Generated at 2022-06-13 06:12:14.086925
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:12:26.328683
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    # test successful read of file
    source = os.path.realpath(__file__)
    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        raise Exception(e)

    data = base64.b64encode(source_content)
    module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:12:50.503436
# Unit test for function main
def test_main():
    import os
    import tempfile
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    # Test with no file
    source = os.path.join(tempfile.gettempdir(), "notexistingfile")
    assert os.path.exists(source) == False
    module.params['src'] = source
    try:
        main()
    except SystemExit as se:
        assert se.code == 1
    else:
        assert False
    # Test with a readable file
    source = os.path.join(tempfile.gettempdir(), "testfile")
    assert os.path.exists(source) == False
    os.environ["SOURCE"] = source

# Generated at 2022-06-13 06:13:03.330174
# Unit test for function main
def test_main():
    """This is a unit test for function ``ansible.builtin.slurp.main``"""
    # mock an actual path to a file
    real_path_filename = "/proc/mounts"
    file_content = os.fdopen(os.open(real_path_filename, os.O_RDONLY)).read()
    # mock the input arguments
    mock_args = dict(src=real_path_filename)
    # assert the function runs without a problem
    assert main(mock_args) == (
        dict(
            source=real_path_filename,
            content=base64.b64encode(file_content),
            encoding="base64",
        ),
        None
    )

# Generated at 2022-06-13 06:13:12.889238
# Unit test for function main
def test_main():
    source = './test_slurp_script'
    with open(source, 'wb') as f:
        f.write(b'Hello world!')

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    module.params['src'] = source
    module.check_mode = False

    try:
        main()
    except SystemExit as e:
        if e.code != 0:
            raise e

    os.remove('./test_slurp_script')

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:13:25.295476
# Unit test for function main
def test_main():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat import unittest
    from ansible_collections.notmintest.not_a_real_collection.plugins.modules import slurp
    from ansible.module_utils import basic

    class TestSlurpModule(unittest.TestCase):
        def setUp(self):
            self.mock_module = basic.AnsibleModule(
                argument_spec=dict(
                    src=dict(type='path', required=True, aliases=['path']),
                ),
                supports_check_mode=False,
            )

        def tearDown(self):
            pass


# Generated at 2022-06-13 06:13:36.262856
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.text.converters import to_native
    import ansible.module_utils.common.json as json

    # test
    data = dict(
        src='/etc/hosts',
        supports_check_mode=True,
    )

    data_in = dict(
        ANSIBLE_MODULE_ARGS=data,
    )
    module = basic._ANSIBLE_ARGS

    with open(data['src'], 'rb') as source_fh:
        source_content = source_fh.read()

    content = dict(
        content=base64.b64encode(source_content),
        source=data['src'],
        encoding='base64',
    )


# Generated at 2022-06-13 06:13:49.222908
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_bytes

    test_dir = tempfile.mkdtemp()

    try:
        fd, src = tempfile.mkstemp(dir=test_dir)
        os.write(fd, to_bytes('Hello World'))
        os.close(fd)

        module = AnsibleModule(
            argument_spec=dict(
                src=dict(type='path', required=True, aliases=['path']),
            ),
        )
        module.params['src'] = src
        main()
    finally:
        shutil.rmtree(test_dir)

# Generated at 2022-06-13 06:13:51.274044
# Unit test for function main
def test_main():
    '''
    Function main() will run the module functions in order
    '''
    pass  # Nothing to do

# Generated at 2022-06-13 06:13:56.490793
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={'src': {'type': 'path', 'required': False, 'aliases': ['path']}})
# Get the file size with os.stat(your_file).st_size
    with open('/tmp/testfile', 'wb') as fh:
        fh.write(os.urandom(100))

    main()
    if os.path.exists('/tmp/testfile'):
        os.remove('/tmp/testfile')

# Generated at 2022-06-13 06:13:58.716560
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"src":"/path/to/file"}'
    os.environ['ANSIBLE_REMOTE_TMP'] = '/tmp'
    main()

# Generated at 2022-06-13 06:13:59.143542
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:14:28.733526
# Unit test for function main
def test_main():
    os.system('rm -rf TEST_FILE')
    os.system('touch TEST_FILE')
    assert(main() == 'encoded_file_content')
    os.system('rm -rf TEST_FILE')

# Generated at 2022-06-13 06:14:41.263779
# Unit test for function main
def test_main():
    args = dict(src='/var/run/sshd.pid')
    module_args = dict(
        src=dict(type='path', required=True, aliases=['path']),
    )
    try:
        fake_source = open(r'test_file','w+')
        source_content = fake_source.read()
    finally:
        fake_source.close()
    try:
        with open(args['src'], 'rb') as source_fh:
            assert source_fh.read() == source_content
    except (IOError, OSError) as e:
        assert e.errno == errno.ENOENT
        msg = "file not found: %s" % args['src']
        assert msg == "file not found: test_file"

# Generated at 2022-06-13 06:14:51.702935
# Unit test for function main
def test_main():
    source = "test_file.txt"
    src_content = "This is line 1\nThis is line 2\n"

    source_fh = open(source, 'w')
    source_fh.write(src_content)
    source_fh.close()

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params = {"src": source}

    try:
        result = main()
    except:
        import traceback
        traceback.print_exc()

    assert result["content"] == base64.b64encode(src_content)
    assert result["source"] == source
    assert result["encoding"] == "base64"

# Generated at 2022-06-13 06:14:53.847181
# Unit test for function main
def test_main():
    '''
    test_main() returns the content value to check if it is really base64 encoded.
    '''
    r = main()
    return r

# Generated at 2022-06-13 06:14:55.197860
# Unit test for function main
def test_main():
    #exit 1 if failed
	assert main()==0

# Generated at 2022-06-13 06:15:09.431529
# Unit test for function main
def test_main():
    import os
    import shutil
    import sys
    import tempfile
    import textwrap
    import unittest
    import yaml

    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils import basic
    from ansible.module_utils.common.text.converters import to_bytes

    # Set up and change to a temp dir for testing
    tmpdir = tempfile.mkdtemp(prefix="ansible_test_ansible_module_")
    olddir = os.getcwd()
    os.chdir(tmpdir)

    # Create a temp file for testing
    temp_fh, temp_fname = tempfile.mkstemp(dir=tmpdir)

# Generated at 2022-06-13 06:15:10.509817
# Unit test for function main
def test_main():
    print('main')


# Generated at 2022-06-13 06:15:19.134444
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_MODULE_TEST'] = '1'
    curdir = os.getcwd()
    source = '%s/../module_utils/shell.py' % curdir
    args = {
        'src': source,
    }

    if os.path.exists(source):
        try:
            print('Running slurp module with arguments %s' % args)
            with open(os.devnull, 'w') as fnull:
                rc = main()
                if rc == 0:
                    return True
                else:
                    return False
        except (IOError, OSError) as e:
            if e.errno == errno.ENOENT:
                msg = "file not found: %s" % source

# Generated at 2022-06-13 06:15:21.151848
# Unit test for function main
def test_main():
    # a seemingly random number of tests
    # not sure if there is a better way here
    # maybe use pytest 
    # however, magic number 5 is still here
    for x in range(5):
        test_main()

# Generated at 2022-06-13 06:15:26.568080
# Unit test for function main
def test_main():
    os.system("touch /tmp/test")
    test_module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True),
        ),
        supports_check_mode=True,
    )
    test_module.params['src'] = '/tmp/test'
    # The source file doesn't exist
    assert main() == 1
    # The source file exist
    test_module.params['src'] = '/etc/passwd'
    assert main() == 0

# Generated at 2022-06-13 06:16:27.815963
# Unit test for function main
def test_main():
    src_path = os.path.join(os.path.dirname(__file__), 'test-data', 'test.txt')
    raw_bytes_content = open(src_path, 'rb').read()
    bytes_content = base64.b64encode(raw_bytes_content)
    expected_result = dict(
        content=bytes_content,
        source=src_path,
        encoding='base64',
    )
    module = AnsibleModule(argument_spec=dict(src=dict(required=True, type='path', aliases=['path'], default=src_path)))
    assert main() == expected_result

# Generated at 2022-06-13 06:16:40.216170
# Unit test for function main
def test_main():
    class ModuleArgs(object):
        def __init__(self, src):
            self.src = src
    import tempfile
    def get_arg(name):
        return getattr(module.params, name)
    def fail_json(*args, **kwargs):
        return module.fail_json(*args, **kwargs)

    # Init module object
    global module

# Generated at 2022-06-13 06:16:51.320071
# Unit test for function main
def test_main():
    # Read the contents of the file to slurp from disk
    test_path = os.path.join(os.path.dirname(__file__), 'fetch_file')
    with open(test_path, 'rb') as fd:
        expected_content = fd.read()

    # Create a fake module
    module = AnsibleModule(argument_spec={'src': dict(type='path', required=True, aliases=['path'])})

    # Set the passed in argument to the test_path variable
    module.params = {'src': test_path}

    # Call the function to slurp the file
    main()

    # Assert we exited without error
    assert not module.fail_json.called

    # Assert we got the correct content back

# Generated at 2022-06-13 06:17:04.393880
# Unit test for function main
def test_main():

    # Testing function main
    #
    # Input parameters:
    #   src : The file on the remote system to fetch. This I(must) be a file, not a directory.

    def mock_AnsibleModule_init(self, argument_spec, supports_check_mode=False, bypass_checks=False, no_log=False,
        check_invalid_arguments=True, mutually_exclusive=None, required_together=None, required_one_of=None,
        add_file_common_args=False, supports_diff=False):
        self.argument_spec = argument_spec
        self.supports_check_mode = supports_check_mode
        self.bypass_checks = bypass_checks
        self.no_log = no_log
        self.check_invalid_arguments = check_invalid_arguments

# Generated at 2022-06-13 06:17:08.207901
# Unit test for function main
def test_main():
    fields_
    with mock.patch.object(module_util, 'AnsibleModule') as obj:
        with mock.patch.object(obj, 'exit_json') as obj1:
            main()
            obj1.assert_called_with(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:17:19.602534
# Unit test for function main
def test_main():
    test_spec = dict(
        src=dict(type='path', required=True, aliases=['path']),
    )

    # Test This Module with good path
    with open('/etc/passwd', 'rb') as source_fh:
        source_content = source_fh.read()
    
    test_params = dict(src='/etc/passwd')
    test_set_module = AnsibleModule(argument_spec=test_spec, supports_check_mode=True)
    test_set_module.params = test_params

    with open('/etc/passwd', 'rb') as source_fh:
        source_content = source_fh.read()


# Generated at 2022-06-13 06:17:30.962858
# Unit test for function main
def test_main():
    # Initialize function parameters
    module_args = {
        "src": "test_value_src",
    }
    # Without exception
    result = {}

    try:
        module = AnsibleModule(
            argument_spec=module_args,
        )
    except:
        pass

    try:
        with open("test_value_src", 'rb') as source_fh:
            source_content = source_fh.read()
    except:
        pass

    try:
        data = base64.b64encode(source_content)
    except:
        pass

    module.exit_json(changed=False, content=data, source="test_value_src", encoding='base64')

    assert result['content'] == data
    assert result['source'] == "test_value_src"

# Generated at 2022-06-13 06:17:37.894671
# Unit test for function main
def test_main():
    module_args = dict(
        src='/etc/hosts'
    )
    module = AnsibleModule(argument_spec=module_args)
    source_content = "127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback"
    with open('/etc/hosts', 'w') as file:
        file.write(source_content)
    main()
    os.remove('/etc/hosts')

# Generated at 2022-06-13 06:17:38.996799
# Unit test for function main
def test_main():
    assert main() is not None

# Generated at 2022-06-13 06:17:46.027303
# Unit test for function main
def test_main():
    # AnsibleModule(argument_spec, bypass_checks=False, check_invalid_arguments=None, check_required_arguments=None)
    # Returns a new instance of AnsibleModule, with the specified spec, also passing along anykwargs
    # that AnsibleModule() accepts
    # path to the module
    mod_path = os.path.join(os.path.dirname(__file__), '../files/library/slurp.py')
    # load up the module
    module = load_module('slurp', mod_path, validate_imports=False)
    # set the module args 
    args = dict(
                src=dict(type='path', required=True, aliases=['path'])
               )
    module.params = args
    # execute the main function
    result = module.main()
